#!/usr/bin/env python3
"""OKF bundle linter — conformance (OKF v0.1) plus this repository's law.

Usage: python3 tools/lint_okf.py <bundle>/wiki

Checks (see CLAUDE.md):
  OKF   frontmatter parseable, non-empty ``type``; reserved files carry none
        (root index.md may carry only ``okf_version``).
  Law   valid ``status`` on concept pages; Source pages carry ``resource`` and
        ``source_kind``; ``type`` agrees with folder; kebab-case filenames;
        ISO-8601 ``timestamp``.
  Links every bundle-relative link resolves (error — stricter than OKF).
  Index every concept listed exactly once in its folder's index.md, with the
        index description matching frontmatter ``description``.
  Math  no ``\\(``/``\\[`` delimiters; balanced ``$``/``$$`` outside code.
  Bib   bibliography.bib parses and validates (keys, citedby slugs, sort);
        bibliography.md is the freshly generated view (sync enforced).
  Graph orphan concept pages (warning only).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

RESERVED = {"index.md", "log.md", "bibliography.md"}
TYPE_FOLDERS = {
    "definitions": "Definition",
    "methods": "Method",
    "operators": "Operator",
    "results": "Result",
    "properties": "Property",
    "benchmarks": "Benchmark",
    "software": "Software",
    "sources": "Source",
}
STATUS_VALUES = {"established", "hypothesis"}
SOURCE_KINDS = {"paper", "book", "thesis", "blog", "notes", "slides", "code", "report"}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
ISO8601 = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:\d{2})?)?$")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
INDEX_ENTRY = re.compile(r"^[*-]\s+\[([^\]]+)\]\(([^)\s]+)\)\s+[—-]\s+(.*\S)\s*$")

errors: list[str] = []
warnings: list[str] = []


def fail(path: Path, msg: str) -> None:
    errors.append(f"[FAIL] {path}: {msg}")


def warn(path: Path, msg: str) -> None:
    warnings.append(f"[warn] {path}: {msg}")


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter_yaml, body). Delimiter = leading '---' line plus the
    next line that is exactly '---'; immune to '---' later in the body."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "".join(lines[1:i]), "".join(lines[i + 1 :])
    return "", text  # unclosed sentinel: caller treats '' as unclosed


def strip_code(body: str) -> str:
    body = re.sub(r"^```.*?^```", "", body, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", body)


def check_math(path: Path, body: str) -> None:
    text = strip_code(body)
    if re.search(r"\\[\[\(]", text):
        fail(path, r"forbidden LaTeX delimiter \( or \[ — use $...$ / $$...$$")
    # balance: strip $$...$$ pairs, then unescaped $ must pair up
    no_display = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    if no_display.count("$$") % 2:
        fail(path, "unbalanced $$ display-math delimiters")
    singles = len(re.findall(r"(?<!\\)\$", no_display.replace("$$", "")))
    if singles % 2:
        fail(path, "unbalanced $ inline-math delimiters")


def resolve_link(wiki: Path, src: Path, target: str) -> bool:
    target = target.split("#")[0]
    if not target or target.startswith(("http://", "https://", "doi:", "mailto:")):
        return True
    if target.startswith("/"):
        return (wiki / target.lstrip("/")).exists()
    return (src.parent / target).exists()


def main(wiki_dir: str) -> int:
    wiki = Path(wiki_dir).resolve()
    if not wiki.is_dir():
        print(f"no such directory: {wiki}")
        return 2

    pages: dict[Path, dict] = {}  # concept pages: path -> frontmatter
    incoming: set[str] = set()  # wiki-relative posix paths that are link targets

    for path in sorted(wiki.rglob("*.md")):
        rel = path.relative_to(wiki)
        text = path.read_text(encoding="utf-8")
        fm_text, body = split_frontmatter(text)

        if path.name in RESERVED:
            if fm_text is not None:
                if rel == Path("index.md"):
                    meta = yaml.safe_load(fm_text) or {}
                    if set(meta) - {"okf_version"}:
                        fail(rel, "root index.md frontmatter may carry only okf_version")
                else:
                    fail(rel, f"reserved file {path.name} must have no frontmatter")
            for line in body.splitlines():
                m = MD_LINK.search(line)
                if m and not resolve_link(wiki, path, m.group(1)):
                    fail(rel, f"broken link: {m.group(1)}")
            continue

        # --- concept document ---
        if not KEBAB.match(path.name):
            fail(rel, "filename is not kebab-case")
        if fm_text is None:
            fail(rel, "missing YAML frontmatter")
            continue
        if fm_text == "":
            fail(rel, "unclosed YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(fm_text) or {}
        except yaml.YAMLError as e:
            fail(rel, f"frontmatter YAML error: {e}")
            continue

        ctype = str(meta.get("type", "") or "").strip()
        if not ctype:
            fail(rel, "frontmatter missing non-empty 'type'")
        folder = rel.parts[0] if len(rel.parts) > 1 else None
        if folder in TYPE_FOLDERS and ctype and ctype != TYPE_FOLDERS[folder]:
            fail(rel, f"type '{ctype}' disagrees with folder '{folder}/'")
        if folder is not None and folder not in TYPE_FOLDERS:
            warn(rel, f"folder '{folder}/' is not in the taxonomy map")

        if ctype == "Source":
            if not str(meta.get("resource", "") or "").strip():
                fail(rel, "Source page missing 'resource'")
            if meta.get("source_kind") not in SOURCE_KINDS:
                fail(rel, f"Source page 'source_kind' must be one of {sorted(SOURCE_KINDS)}")
        elif ctype:
            if meta.get("status") not in STATUS_VALUES:
                fail(rel, "concept page 'status' must be 'established' or 'hypothesis'")

        ts = meta.get("timestamp")
        if ts is None or not ISO8601.match(str(ts).replace(" ", "T", 1)):
            fail(rel, "missing or non-ISO-8601 'timestamp'")

        check_math(rel, body)
        for m in MD_LINK.finditer(strip_code(body)):
            target = m.group(1)
            if not resolve_link(wiki, path, target):
                fail(rel, f"broken link: {target}")
            elif target.startswith("/"):
                incoming.add(target.lstrip("/").split("#")[0])
            elif not target.startswith(("http://", "https://", "doi:", "mailto:")):
                resolved = (path.parent / target.split("#")[0]).resolve()
                if resolved.is_relative_to(wiki):
                    incoming.add(resolved.relative_to(wiki).as_posix())
        pages[rel] = meta

    # --- index completeness & description consistency ---
    for folder in sorted({p.parts[0] for p in pages if len(p.parts) > 1}):
        idx = wiki / folder / "index.md"
        members = {p for p in pages if len(p.parts) > 1 and p.parts[0] == folder}
        if not idx.exists():
            fail(Path(folder) / "index.md", "missing folder index.md")
            continue
        _, idx_body = split_frontmatter(idx.read_text(encoding="utf-8"))
        listed: dict[str, str] = {}
        for line in idx_body.splitlines():
            m = INDEX_ENTRY.match(line.strip())
            if m:
                key = m.group(2).lstrip("/").split("#")[0]
                if key in listed:
                    fail(Path(folder) / "index.md", f"duplicate index entry: {key}")
                listed[key] = m.group(3)
        for page in sorted(members):
            key = page.as_posix()
            if key not in listed:
                fail(Path(folder) / "index.md", f"concept not listed: {key}")
            else:
                desc = str(pages[page].get("description", "") or "").strip().rstrip(".")
                if listed[key].strip().rstrip(".") != desc:
                    fail(
                        Path(folder) / "index.md",
                        f"description drift for {key} (index line != frontmatter)",
                    )

    # --- bibliography: canonical .bib valid, .md view in sync ---
    bib, bib_md = wiki / "bibliography.bib", wiki / "bibliography.md"
    if bib.exists() or bib_md.exists():
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import bib_to_md

        if not bib.exists():
            fail(Path("bibliography.md"), "exists without canonical bibliography.bib")
        else:
            try:
                entries = bib_to_md.parse_bib(bib.read_text(encoding="utf-8"))
            except ValueError as e:
                fail(Path("bibliography.bib"), str(e))
            else:
                for msg in bib_to_md.validate(entries, wiki):
                    fail(Path("bibliography.bib"), msg)
                if not bib_md.exists() or bib_md.read_text(
                    encoding="utf-8"
                ) != bib_to_md.render_md(entries, wiki):
                    fail(
                        Path("bibliography.md"),
                        "out of sync with bibliography.bib — run tools/bib_to_md.py",
                    )
                todo = bib_to_md.pending(entries, wiki)
                if todo:
                    warn(
                        Path("bibliography.bib"),
                        f"{len(todo)} ingested source(s) with no reference list "
                        f"merged (tools/bib_to_md.py --pending)",
                    )

    # --- orphans (warning) ---
    for page in sorted(pages):
        if page.as_posix() not in incoming and page.parts[-1] != "notation.md":
            warn(page, "orphan: no incoming links")

    for line in errors + warnings:
        print(line)
    n_pages = len(pages)
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) across {n_pages} concept pages.")
        return 1
    print(f"\nOK: {n_pages} concept pages conformant; {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "wiki"))
