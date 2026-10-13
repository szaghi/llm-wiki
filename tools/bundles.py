#!/usr/bin/env python3
"""Bundle registry: the derived list of the repository's knowledge bundles.

Usage:
  python3 tools/bundles.py             print the registry as a Markdown table
  python3 tools/bundles.py --json      print the registry as JSON
  python3 tools/bundles.py --write     rewrite the generated regions of README.md
                                       and skills/llm-wiki/SKILL.md
  python3 tools/bundles.py --check     exit 1 if those regions are stale

A bundle is a top-level directory holding ``bundle.toml`` and ``wiki/index.md``.
``bundle.toml`` carries the only hand-written facts (title, summary, keywords,
and an optional ``corpus`` path read by tools/worklist.sh);
every count and date is derived from the wiki at call time (D8), so the README
table and the consultation skill can be regenerated, never edited.

Generated regions are delimited by ``<!-- bundles:start -->`` and
``<!-- bundles:end -->``; the skill's frontmatter ``description:`` line is
regenerated whole.
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from dataclasses import asdict, dataclass, field
from pathlib import Path

from bib_to_md import parse_bib

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/szaghi/llm-wiki"
SITE_URL = "https://szaghi.github.io/llm-wiki"
START, END = "<!-- bundles:start -->", "<!-- bundles:end -->"
CONCEPT_FOLDERS = ("definitions", "methods", "operators", "results", "properties", "benchmarks", "software")
CONTRA_HEADING = re.compile(r"^## Contradictions\s*$", re.MULTILINE)
DATE_HEADING = re.compile(r"^## (\d{4}-\d{2}-\d{2})\s*$")
STATUS_LINE = re.compile(r"^status:\s*(\S+)", re.MULTILINE)


class RegistryError(Exception):
    """A bundle directory is malformed (missing or invalid ``bundle.toml``)."""


@dataclass
class Bundle:
    """One knowledge bundle with its derived statistics."""

    slug: str
    title: str
    summary: str
    keywords: list[str]
    sources: int = 0
    concepts: int = 0
    by_type: dict[str, int] = field(default_factory=dict)
    hypotheses: int = 0
    contested: int = 0
    cited_works: int = 0
    frontier: int = 0
    updated: str = ""


def bundle_dirs(root: Path = ROOT) -> list[Path]:
    """Return the bundle directories under ``root``, sorted by name."""
    return sorted(p.parent for p in root.glob("*/bundle.toml") if (p.parent / "wiki" / "index.md").is_file())


def load(bdir: Path) -> Bundle:
    """Read ``bundle.toml`` and derive the statistics of one bundle."""
    try:
        card = tomllib.loads((bdir / "bundle.toml").read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as err:
        raise RegistryError(f"{bdir.name}/bundle.toml: {err}") from err
    missing = {"title", "summary", "keywords"} - set(card)
    if missing:
        raise RegistryError(f"{bdir.name}/bundle.toml: missing {sorted(missing)}")
    b = Bundle(slug=bdir.name, title=card["title"], summary=card["summary"], keywords=list(card["keywords"]))
    wiki = bdir / "wiki"
    b.sources = sum(1 for p in (wiki / "sources").glob("*.md") if p.name != "index.md")
    for folder in CONCEPT_FOLDERS:
        pages = [p for p in (wiki / folder).glob("*.md") if p.name != "index.md"]
        if pages:
            b.by_type[folder] = len(pages)
        for page in pages:
            text = page.read_text(encoding="utf-8")
            m = STATUS_LINE.search(text)
            b.hypotheses += bool(m and m.group(1) == "hypothesis")
            b.contested += bool(CONTRA_HEADING.search(text))
    b.concepts = sum(b.by_type.values())
    bib = wiki / "bibliography.bib"
    if bib.is_file():
        entries = parse_bib(bib.read_text(encoding="utf-8"))
        b.cited_works = len(entries)
        ingested = {p.stem for p in (wiki / "sources").glob("*.md")}
        b.frontier = sum(1 for e in entries if e["key"] not in ingested)  # as bibliography.md counts it
    log = wiki / "log.md"
    if log.is_file():
        for line in log.read_text(encoding="utf-8").splitlines():
            m = DATE_HEADING.match(line)
            if m:
                b.updated = m.group(1)
                break
    return b


def registry(root: Path = ROOT) -> list[Bundle]:
    """Return every bundle of the repository with derived statistics."""
    return [load(d) for d in bundle_dirs(root)]


def markdown_table(bundles: list[Bundle], links: str = "repo") -> str:
    """Render the registry as a Markdown table.

    ``links="repo"`` points at the wiki in the repository (README); ``"site"``
    at the rendered bundle on the documentation site; ``"local"`` names the
    bundle path relative to the repository root (the consultation skill).
    """
    head = "| Bundle | Domain | Sources | Concept pages | Cited works | Updated |\n| --- | --- | ---: | ---: | ---: | --- |\n"
    rows = []
    for b in bundles:
        if links == "site":
            name = f"[{b.title}]({SITE_URL}/bundles/{b.slug}/)"
        elif links == "local":
            name = f"{b.title} (`{b.slug}/wiki/`)"
        else:
            name = f"[{b.title}]({b.slug}/wiki/index.md)"
        rows.append(f"| {name} | {b.summary} | {b.sources} | {b.concepts} | {b.cited_works} | {b.updated} |")
    return head + "\n".join(rows) + "\n"


def skill_description(bundles: list[Bundle]) -> str:
    """The consultation skill's trigger description, one YAML line."""
    domains = "; ".join(f"{b.slug} ({', '.join(b.keywords)})" for b in bundles)
    text = (
        "Consult the compiled OKF knowledge bundles of the llm-wiki repository. "
        f"TRIGGER whenever a question falls in a bundle's domain: {domains}. "
        'Also trigger on "llm-wiki", "second brain", "check the wiki", "what does the wiki say". '
        "Read-only consultation from any directory; ingestion happens inside the repository under its CLAUDE.md."
    )
    return "description: " + json.dumps(text, ensure_ascii=False)


def replace_region(text: str, body: str, path: Path) -> str:
    """Replace the content between the bundles markers of ``text``."""
    i, j = text.find(START), text.find(END)
    if i < 0 or j < i:
        raise RegistryError(f"{path}: missing {START} / {END} markers")
    return text[: i + len(START)] + "\n" + body + text[j:]


def generated_files(bundles: list[Bundle], root: Path = ROOT) -> dict[Path, str]:
    """Return the new content of every file with a generated region."""
    out: dict[Path, str] = {}
    readme = root / "README.md"
    out[readme] = replace_region(readme.read_text(encoding="utf-8"), markdown_table(bundles), readme)
    skill = root / "skills" / "llm-wiki" / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    text = re.sub(r"^description: .*$", lambda _: skill_description(bundles), text, count=1, flags=re.MULTILINE)
    out[skill] = replace_region(text, markdown_table(bundles, links="local"), skill)
    return out


def main(argv: list[str]) -> int:
    mode = argv[1] if len(argv) > 1 else ""
    try:
        bundles = registry()
        if mode == "--json":
            print(json.dumps([asdict(b) for b in bundles], indent=2, ensure_ascii=False))
        elif mode in ("--write", "--check"):
            stale = []
            for path, new in generated_files(bundles).items():
                if path.read_text(encoding="utf-8") != new:
                    stale.append(path.relative_to(ROOT))
                    if mode == "--write":
                        path.write_text(new, encoding="utf-8")
            if mode == "--check" and stale:
                print("stale bundle registry in: " + ", ".join(map(str, stale)) + " (run tools/bundles.py --write)")
                return 1
            print(
                ("updated: " + ", ".join(map(str, stale)))
                if stale and mode == "--write"
                else "OK: bundle registry in sync"
            )
        elif mode == "":
            print(markdown_table(bundles), end="")
        else:
            print(__doc__)
            return 2
    except RegistryError as err:
        print(f"error: {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
