#!/usr/bin/env python3
"""Reference-list fragment merger for the D15 bibliography backfill.

Merges per-source reference-list fragments (``frag-<slug>.bib``) into a
bundle's canonical ``wiki/bibliography.bib``, applying human-reviewed identity
resolutions, and reports every collision that needs a human decision. It never
guesses an identity: it *flags*, you *resolve*, it *re-runs clean*.

WHEN to use this
----------------
Only for the **D15 bibliography backfill** — merging the reference lists of
already-ingested sources into ``bibliography.bib`` in batches. This is the tool
that produced the div-free-amr citation record (see that bundle's log.md,
"Bibliography backfill batch 1..6").

Do NOT use it for the ordinary per-source ingestion step 5 (a single new
source's reference list): for one source, edit ``bibliography.bib`` directly and
regenerate with ``bib_to_md.py``. This tool earns its complexity only when
merging ~10 fragments at once, where cross-fragment key collisions are dense.

HOW the workflow goes (per batch)
---------------------------------
1. Extract each source's printed reference list into ``frag-<slug>.bib`` in a
   scratch directory (one ``@type{key, ...}`` entry per printed reference, keys
   following the Source-page slug convention; ``[title not printed in citing
   reference]`` for title-less citation styles; see the extraction brief this
   repo's ingestion sessions use).
2. Write a resolutions module (``--resolutions <file.py>``) — a plain Python
   file defining ORDER, ALIASES, NOTES, SILENCED, REPAIRS, FIXUPS (all optional
   except ORDER). Start it empty.
3. ``python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions r.py --report``
   Read the FLAGS. Each flag is a collision the merge cannot resolve alone:
     [conflict]   same key, two dissimilar real titles → two different works
                  share a key. Add an ALIASES entry giving one a distinct key.
     [venuecheck] a placeholder-title merge whose journal/volume/page numbers
                  do not overlap the existing entry → almost always a wrong
                  merge of two title-less works. Verify venues, then ALIAS or
                  SILENCE. (This check is the single most valuable safeguard for
                  ApJ/PRD/A&A-style lists; heed it.)
     [suspect]    a new key resembles an existing one (near-title, or same
                  stem+year). Genuinely distinct → SILENCE the pair; same work
                  → ALIAS the fragment key onto the canonical one.
4. Resolve every flag by editing the resolutions module; re-run ``--report``
   until ``FLAGS: 0``. **A silence is a claim, not a dismissal** — verify each
   pair is really two works before silencing (a wrong silence hides a real
   duplicate; this bit us twice in the div-free-amr backfill).
5. ``--write`` to apply, then regenerate and lint:
     python3 tools/bib_to_md.py <bundle>/wiki
     python3 tools/lint_okf.py  <bundle>/wiki
6. After the FINAL batch, run ``--dupes`` (below) — the batch process is
   structurally blind to the same work entered under two different
   first-author spellings across sources; only a whole-corpus sweep finds them.

Resolution-table semantics
---------------------------
ORDER    list[str] — slugs to merge, in processing order. A fragment file
         ``frag-<slug>.bib`` must exist for each. Order matters when a
         published-form entry must exist before a preprint-form citation
         aliases onto it.
ALIASES  dict[str,str] — fragment key -> canonical key. A scoped key
         ``"slug:key"`` beats the bare ``"key"`` (the same printed key can mean
         different works in different fragments — always prefer scoped unless
         the mapping is a true global identity like a first-author-only
         citation of an ingested source).
NOTES    dict[str,str] — text appended to an entry's ``note`` field (records
         year/venue variants, misprints, identity rationale).
SILENCED set[tuple[str,str]] — reviewed (key_a, key_b) pairs confirmed to need
         no action: genuinely distinct works that trip the heuristics, or
         same-key informational title-form variants ``(k, k)``.
REPAIRS  list[tuple[dup, canon, note]] — pre-merge master repairs: fold a
         pre-existing duplicate ``dup`` into ``canon`` (citedby union + note)
         before the batch runs.
FIXUPS   dict[str, dict] — post-merge field overrides on a final key.

Merge rules (fixed; not configurable)
-------------------------------------
- dedup by key; an existing key gains the citing slug in its citedby (sorted,
  duplicate-free).
- a placeholder title is upgraded when a fragment supplies the real printed one.
- a missing doi/eprint is filled from a fragment; a *conflicting* one is FLAGGED,
  never overwritten (the ingested Source page's identifier is authoritative).
- author initials normalized ``"J. U." -> "J.U."`` (a real duplicate-producing
  defect from an early batch).
- output sorted by key, strict-subset format identical to bib_to_md's parser.

Usage
-----
  bib_merge.py <wiki> --frags <dir> --resolutions <r.py> --report
  bib_merge.py <wiki> --frags <dir> --resolutions <r.py> --write
  bib_merge.py <wiki> --dupes        # whole-corpus cross-key duplicate sweep
"""

from __future__ import annotations

import argparse
import difflib
import importlib.util
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
from bib_to_md import parse_bib  # noqa: E402

PLACEHOLDER = "[title not printed in citing reference]"
FIELD_ORDER = [
    "author", "editor", "title", "journal", "booktitle", "school",
    "institution", "publisher", "howpublished", "series", "year",
    "doi", "eprint", "url", "isbn", "note", "citedby",
]
VENUE_FIELDS = ("journal", "booktitle", "school", "institution",
                "publisher", "howpublished", "series")


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def norm_initials(author: str) -> str:
    return re.sub(r"\.\s+(?=[A-Z]\.)", ".", author)


def stem(key: str) -> str:
    m = re.match(r"^(.*?)-(\d{4})(-[a-z])?$", key)
    return m.group(1) if m else key


def key_year(key: str) -> int:
    m = re.match(r"^.*?-(\d{4})(-[a-z])?$", key)
    return int(m.group(1)) if m else 0


def title_sim(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()


def venue_nums(f: dict) -> set[str]:
    v = next((f[k] for k in VENUE_FIELDS if f.get(k)), "")
    return set(re.findall(r"\d+", v)) - {f.get("year", "")}


def fmt_entry(e: dict) -> str:
    fields = e["fields"]
    lines = [f"@{e['type']}{{{e['key']},"]
    ordered = [k for k in FIELD_ORDER if k in fields]
    ordered += [k for k in fields if k not in FIELD_ORDER]
    for k in ordered:
        lines.append(f"  {k} = {{{fields[k]}}},")
    lines.append("}")
    return "\n".join(lines)


def load_resolutions(path: Path):
    """Load a resolutions module; return (ORDER, ALIASES, NOTES, SILENCED,
    REPAIRS, FIXUPS) with sensible empty defaults for anything absent."""
    spec = importlib.util.spec_from_file_location("resolutions", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return (
        list(getattr(mod, "ORDER", [])),
        dict(getattr(mod, "ALIASES", {})),
        dict(getattr(mod, "NOTES", {})),
        set(getattr(mod, "SILENCED", set())),
        list(getattr(mod, "REPAIRS", [])),
        dict(getattr(mod, "FIXUPS", {})),
    )


def merge(master: Path, frag_dir: Path, res: Path, write: bool) -> int:
    ORDER, ALIASES, NOTES, SILENCED, REPAIRS, FIXUPS = load_resolutions(res)
    if not ORDER:
        print("resolutions module defines no ORDER (nothing to merge)")
        return 2

    master_text = master.read_text(encoding="utf-8")
    header = "".join(ln + "\n" for ln in master_text.splitlines()
                     if ln.startswith("%"))
    entries = {e["key"]: e for e in parse_bib(master_text)}

    for dup, canon, note in REPAIRS:
        if dup not in entries or canon not in entries:
            print(f"REPAIR keys missing: {dup} -> {canon}")
            return 2
        d, c = entries.pop(dup), entries[canon]
        cb = {s.strip() for s in c["fields"].get("citedby", "").split(",") if s.strip()}
        cb |= {s.strip() for s in d["fields"].get("citedby", "").split(",") if s.strip()}
        c["fields"]["citedby"] = ", ".join(sorted(cb))
        c["fields"]["note"] = ((c["fields"]["note"] + "; ")
                               if c["fields"].get("note") else "") + note

    flags: list[str] = []
    stats: dict[str, dict] = {}
    frags = [frag_dir / f"frag-{s}.bib" for s in ORDER]
    missing = [f.name for f in frags if not f.is_file()]
    if missing:
        print(f"missing fragments in {frag_dir}: {missing}")
        return 2

    for frag in frags:
        slug = frag.stem.removeprefix("frag-")
        new = parse_bib(frag.read_text(encoding="utf-8"))
        st = {"printed": len(new), "added": 0, "cited_existing": 0,
              "title_upgrades": 0, "id_filled": 0}
        stats[slug] = st
        for e in new:
            key, f = e["key"], e["fields"]
            key = ALIASES.get(f"{slug}:{key}", ALIASES.get(key, key))
            e["key"] = key
            if "author" in f:
                f["author"] = norm_initials(f["author"])
            f.pop("citedby", None)
            if key in entries:
                mf = entries[key]["fields"]
                cb = [s for s in mf.get("citedby", "").split(",") if s.strip()]
                mf["citedby"] = ", ".join(sorted({s.strip() for s in cb} | {slug}))
                st["cited_existing"] += 1
                mt, nt = mf.get("title", ""), f.get("title", "")
                if mt == PLACEHOLDER and nt and nt != PLACEHOLDER:
                    mf["title"] = nt
                    st["title_upgrades"] += 1
                elif (nt and nt != PLACEHOLDER and mt != PLACEHOLDER
                      and title_sim(mt, nt) < 0.55 and (key, key) not in SILENCED):
                    flags.append(f"[conflict] {key} (via {slug}): master title "
                                 f"{mt!r} vs printed {nt!r}")
                if (mt == PLACEHOLDER or nt == PLACEHOLDER) and (key, key) not in SILENCED:
                    mn, fn = venue_nums(mf), venue_nums(f)
                    if mn and fn and not (mn & fn):
                        flags.append(f"[venuecheck] {key} (via {slug}): no shared "
                                     f"venue numbers, master {sorted(mn)} vs "
                                     f"printed {sorted(fn)}")
                for idf in ("doi", "eprint"):
                    if f.get(idf) and not mf.get(idf):
                        mf[idf] = f[idf]
                        st["id_filled"] += 1
                    elif (f.get(idf) and mf.get(idf) and f[idf] != mf[idf]
                          and (key, key) not in SILENCED):
                        flags.append(f"[conflict] {key} (via {slug}): {idf} "
                                     f"{mf[idf]!r} vs {f[idf]!r}")
            else:
                s, y = stem(key), key_year(key)
                nt = f.get("title", "")
                for ok, oe in entries.items():
                    os_ = stem(ok)
                    related = (os_ == s or os_.startswith(s + "-")
                               or s.startswith(os_ + "-"))
                    if ok == key or not related or abs(key_year(ok) - y) > 1:
                        continue
                    if (key, ok) in SILENCED:
                        continue
                    ot = oe["fields"].get("title", "")
                    sim = title_sim(ot, nt) if PLACEHOLDER not in (ot, nt) else -1.0
                    if os_ != s or sim >= 0.7 or (key_year(ok) == y and sim < 0):
                        flags.append(f"[suspect] new {key} (via {slug}) ~ existing "
                                     f"{ok}: sim={sim:.2f} new={nt!r} old={ot!r}")
                e["fields"]["citedby"] = slug
                entries[key] = e
                st["added"] += 1

    for key, overrides in FIXUPS.items():
        if key in entries:
            entries[key]["fields"].update(overrides)
        else:
            flags.append(f"[error] FIXUPS key not present after merge: {key}")
    for key, extra in NOTES.items():
        if key in entries:
            nf = entries[key]["fields"]
            if extra not in nf.get("note", ""):
                nf["note"] = (nf["note"] + "; " if nf.get("note") else "") + extra
        else:
            flags.append(f"[error] NOTES key not present after merge: {key}")

    for slug, st in sorted(stats.items()):
        print(f"{slug}: {st['printed']} refs -> {st['added']} new, "
              f"{st['cited_existing']} existing, {st['title_upgrades']} title "
              f"upgrades, {st['id_filled']} doi/eprint filled")
    print(f"\nTOTAL entries after merge: {len(entries)}")
    print(f"FLAGS: {len(flags)}")
    for fl in flags:
        print(" ", fl)

    if write:
        if flags:
            print("\nrefusing to --write with open FLAGS; resolve them first.")
            return 1
        body = "\n\n".join(fmt_entry(entries[k]) for k in sorted(entries))
        master.write_text(header + "\n" + body + "\n", encoding="utf-8")
        print(f"\nwrote {master} ({len(entries)} entries)")
    return 0


def dupes(master: Path) -> int:
    """Whole-corpus cross-key duplicate sweep. The batch merger dedups by KEY,
    and keys derive from each citing source's spelling — so the same work
    entered under two first-author spellings (OCR variants, mis-transcribed
    authors, author-order swaps) lands under two keys the per-batch checks
    cannot relate. This groups by (normalized-title, year) across ALL keys and
    reports collisions, flagging cross-stem ones (different surname => suspect
    spelling variant). Run after the final batch. It only reports; you review
    and merge duplicates by hand."""
    entries = parse_bib(master.read_text(encoding="utf-8"))
    from collections import defaultdict
    byt: dict = defaultdict(list)
    for e in entries:
        t = e["fields"].get("title", "")
        if t == PLACEHOLDER or not t.strip():
            continue
        byt[(norm_title(t), e["fields"].get("year", ""))].append(e["key"])
    groups = {k: v for k, v in byt.items() if len(v) > 1}
    cross = 0
    print(f"cross-key identical-title+year groups: {len(groups)}")
    for (t, y), ks in sorted(groups.items()):
        stems = {stem(k) for k in ks}
        tag = "  <-- CROSS-STEM (likely spelling variant)" if len(stems) > 1 else ""
        if len(stems) > 1:
            cross += 1
        print(f"  [{y}] {ks}{tag}")
        if len(stems) > 1:
            print(f"        {t[:76]}")
    print(f"\n{cross} cross-stem group(s) — review each; same work under two "
          f"spellings must be merged (citedby union), distinct works left alone.")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="D15 bibliography fragment merger.")
    ap.add_argument("wiki", help="bundle wiki dir containing bibliography.bib")
    ap.add_argument("--frags", help="dir holding frag-<slug>.bib fragments")
    ap.add_argument("--resolutions", help="Python module of resolution tables")
    ap.add_argument("--report", action="store_true", help="dry run: plan + flags")
    ap.add_argument("--write", action="store_true", help="apply (refused if flags)")
    ap.add_argument("--dupes", action="store_true",
                    help="whole-corpus cross-key duplicate sweep (post-final)")
    a = ap.parse_args(argv)
    master = Path(a.wiki).resolve() / "bibliography.bib"
    if not master.is_file():
        print(f"no such file: {master}")
        return 2
    if a.dupes:
        return dupes(master)
    if not (a.report or a.write):
        ap.error("choose --report, --write, or --dupes")
    if not a.frags or not a.resolutions:
        ap.error("--frags and --resolutions are required for --report/--write")
    return merge(master, Path(a.frags).resolve(),
                 Path(a.resolutions).resolve(), a.write)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
