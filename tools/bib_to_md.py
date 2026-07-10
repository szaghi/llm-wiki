#!/usr/bin/env python3
"""Bundle bibliography — canonical .bib, generated .md (see CLAUDE.md, D15).

``wiki/bibliography.bib`` is the canonical citation record: one entry per work
cited by any ingested source (ingested or not), keyed by the Source-page slug
convention. The custom field ``citedby = {slug-1, slug-2}`` lists the ingested
sources in whose reference lists the work appears. ``wiki/bibliography.md`` is
a generated view — never hand-edited.

Usage:
  python3 tools/bib_to_md.py <bundle>/wiki             # (re)write bibliography.md
  python3 tools/bib_to_md.py <bundle>/wiki --check     # exit 1 if md out of sync
  python3 tools/bib_to_md.py <bundle>/wiki --pending   # ingested sources whose
                                                       # reference lists are not
                                                       # yet merged into the .bib
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

KEBAB_KEY = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FIELD_NAME = re.compile(r"^[a-z][a-z0-9_-]*$")
VENUE_FIELDS = ("journal", "booktitle", "school", "institution", "publisher", "howpublished", "series")


def parse_bib(text: str) -> list[dict]:
    """Parse the strict, compiler-owned BibTeX subset:
    ``@type{key,`` then ``name = {value}`` fields (balanced braces), ``}``.
    ``%`` starts a comment outside entries. Raises ValueError with a line number.
    """
    entries: list[dict] = []
    pos = 0

    def lineno(p: int) -> int:
        return text.count("\n", 0, p) + 1

    def err(p: int, msg: str) -> ValueError:
        return ValueError(f"line {lineno(p)}: {msg}")

    while True:
        while pos < len(text) and text[pos].isspace():
            pos += 1
        if pos >= len(text):
            return entries
        if text[pos] == "%":
            nl = text.find("\n", pos)
            pos = len(text) if nl < 0 else nl + 1
            continue
        if text[pos] != "@":
            raise err(pos, f"expected '@' or '%' comment, got {text[pos]!r}")
        brace = text.find("{", pos)
        if brace < 0:
            raise err(pos, "expected '{' after entry type")
        etype = text[pos + 1 : brace].strip().lower()
        comma = text.find(",", brace)
        if comma < 0:
            raise err(brace, "expected ',' after entry key")
        key = text[brace + 1 : comma].strip()
        pos = comma + 1
        fields: dict[str, str] = {}
        while True:
            while pos < len(text) and (text[pos].isspace() or text[pos] == ","):
                pos += 1
            if pos >= len(text):
                raise err(pos - 1, f"unterminated entry {key!r}")
            if text[pos] == "}":
                pos += 1
                break
            eq = text.find("=", pos)
            if eq < 0:
                raise err(pos, f"expected 'name = {{value}}' in entry {key!r}")
            name = text[pos:eq].strip().lower()
            if not FIELD_NAME.match(name):
                raise err(pos, f"bad field name {name!r} in entry {key!r}")
            vpos = eq + 1
            while vpos < len(text) and text[vpos].isspace():
                vpos += 1
            if vpos >= len(text) or text[vpos] != "{":
                raise err(vpos if vpos < len(text) else eq, f"field {name!r} of {key!r}: value must be brace-delimited")
            depth = 0
            vend = vpos
            while vend < len(text):
                if text[vend] == "{":
                    depth += 1
                elif text[vend] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                vend += 1
            if depth != 0:
                raise err(vpos, f"unbalanced braces in field {name!r} of {key!r}")
            if name in fields:
                raise err(pos, f"duplicate field {name!r} in entry {key!r}")
            fields[name] = " ".join(text[vpos + 1 : vend].split())
            pos = vend + 1
        entries.append({"type": etype, "key": key, "fields": fields})


def citedby(entry: dict) -> list[str]:
    raw = entry["fields"].get("citedby", "").strip()
    return [s.strip() for s in raw.split(",") if s.strip()] if raw else []


def source_slugs(wiki: Path) -> set[str]:
    sources = wiki / "sources"
    if not sources.is_dir():
        return set()
    return {p.stem for p in sources.glob("*.md")} - {"index"}


def validate(entries: list[dict], wiki: Path) -> list[str]:
    """Repository-law checks on parsed entries; returns error messages."""
    msgs: list[str] = []
    slugs = source_slugs(wiki)
    keys = [e["key"] for e in entries]
    seen: set[str] = set()
    for e in entries:
        key, f = e["key"], e["fields"]
        if key in seen:
            msgs.append(f"duplicate key: {key}")
        seen.add(key)
        if not KEBAB_KEY.match(key):
            msgs.append(f"key not kebab-case: {key}")
        if not f.get("title", "").strip():
            msgs.append(f"{key}: missing required field 'title'")
        if not re.fullmatch(r"\d{4}", f.get("year", "")):
            msgs.append(f"{key}: 'year' must be a 4-digit year")
        cb = citedby(e)
        if cb != sorted(set(cb)):
            msgs.append(f"{key}: citedby must be sorted and duplicate-free")
        if key in cb:
            msgs.append(f"{key}: citedby must not contain the entry's own key")
        for slug in cb:
            if slug not in slugs:
                msgs.append(f"{key}: citedby slug '{slug}' has no Source page")
    if keys != sorted(keys):
        msgs.append("entries must be sorted by key")
    return msgs


def _format_work(entry: dict) -> str:
    f = entry["fields"]
    who = (f.get("author") or f.get("editor", "")).replace(" and ", "; ")
    out = f"{who} ({f['year']}). *{f['title']}*." if who else f"({f['year']}). *{f['title']}*."
    venue = next((f[k] for k in VENUE_FIELDS if f.get(k)), "")
    if venue:
        out += f" {venue}."
    if f.get("doi"):
        target = f["doi"].replace("(", "%28").replace(")", "%29")
        out += f" [doi:{f['doi']}](https://doi.org/{target})"
    elif f.get("eprint"):
        out += f" [arXiv:{f['eprint']}](https://arxiv.org/abs/{f['eprint']})"
    elif f.get("url"):
        out += f" <{f['url']}>"
    if f.get("isbn"):
        out += f" ISBN {f['isbn']}."
    if f.get("note"):
        out += f" {f['note']}."
    return out


def _cited_by_suffix(entry: dict) -> str:
    cb = citedby(entry)
    if not cb:
        return " Cited by 0 ingested sources."
    links = ", ".join(f"[{s}](/sources/{s}.md)" for s in cb)
    return f" Cited by {len(cb)}: {links}."

def render_md(entries: list[dict], wiki: Path) -> str:
    slugs = source_slugs(wiki)
    ingested = sorted((e for e in entries if e["key"] in slugs), key=lambda e: e["key"])
    frontier = sorted(
        (e for e in entries if e["key"] not in slugs),
        key=lambda e: (-len(citedby(e)), e["key"]),
    )
    processed = {s for e in entries for s in citedby(e)}
    lines = [
        "# Bibliography",
        "",
        "<!-- Generated by tools/bib_to_md.py from bibliography.bib — do not edit. -->",
        "",
        f"Complete citation record of the bundle: every work cited by any ingested "
        f"source, ingested or not. **{len(entries)} works** — {len(ingested)} ingested, "
        f"{len(frontier)} cited but not ingested. \"Cited by\" counts the ingested "
        f"sources in whose reference lists the work appears "
        f"({len(processed)}/{len(slugs)} reference lists merged).",
        "",
        f"## Ingested sources ({len(ingested)})",
        "",
    ]
    for e in ingested:
        lines.append(f"* [{e['key']}](/sources/{e['key']}.md) — {_format_work(e)}{_cited_by_suffix(e)}")
    lines += ["", f"## Cited, not ingested ({len(frontier)})", ""]
    if frontier:
        lines.append("Sorted by citation count — the top entries are the derived ingestion frontier.")
        lines.append("")
    for e in frontier:
        lines.append(f"* **{e['key']}** — {_format_work(e)}{_cited_by_suffix(e)}")
    return "\n".join(lines) + "\n"


def pending(entries: list[dict], wiki: Path) -> list[str]:
    """Ingested sources whose reference lists are not yet merged (derived:
    a source's references are extracted iff its slug appears in >=1 citedby)."""
    processed = {s for e in entries for s in citedby(e)}
    return sorted(source_slugs(wiki) - processed)


def main(argv: list[str]) -> int:
    if not argv or argv[0].startswith("--"):
        print(__doc__.strip())
        return 2
    wiki = Path(argv[0]).resolve()
    mode = argv[1] if len(argv) > 1 else ""
    bib = wiki / "bibliography.bib"
    md = wiki / "bibliography.md"
    if not bib.is_file():
        print(f"no such file: {bib}")
        return 2
    try:
        entries = parse_bib(bib.read_text(encoding="utf-8"))
    except ValueError as e:
        print(f"[FAIL] bibliography.bib: {e}")
        return 1
    problems = validate(entries, wiki)
    for p in problems:
        print(f"[FAIL] bibliography.bib: {p}")
    if problems:
        return 1
    if mode == "--pending":
        todo = pending(entries, wiki)
        for slug in todo:
            print(slug)
        print("---", file=sys.stderr)
        print(f"pending reference lists: {len(todo)} / {len(source_slugs(wiki))}", file=sys.stderr)
        return 0
    rendered = render_md(entries, wiki)
    if mode == "--check":
        if not md.is_file() or md.read_text(encoding="utf-8") != rendered:
            print("[FAIL] bibliography.md out of sync — run tools/bib_to_md.py")
            return 1
        print("OK: bibliography.md in sync")
        return 0
    md.write_text(rendered, encoding="utf-8")
    print(f"wrote {md} ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
