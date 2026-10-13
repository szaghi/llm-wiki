#!/usr/bin/env python3
"""Generate the documentation site's bundle pages and graph data.

Usage: python3 tools/site_sync.py [docs-dir]        (default: docs)

For every bundle of the registry (tools/bundles.py) it writes, under the
documentation tree, generated files that are git-ignored and never edited:

  bundles/<slug>/**.md      the wiki, with bundle-root links (``/methods/x.md``)
                            rewritten to site links (``/bundles/<slug>/methods/x.md``)
                            and a frontmatter the site theme reads
  bundles/<slug>/graph.md   the interactive page graph of the bundle
  public/data/<slug>.graph.json   nodes (pages) and edges (links) of the bundle
  public/data/bundles.json        the registry plus the cross-bundle overlaps
  public/bundles/<slug>/bibliography.bib   the citation record, for download
  .vitepress/generated/bundles.json   the bundle sidebars and navigation menu

The bundles themselves are never modified. Cross-bundle overlaps (shared cited
works, sources ingested in several bundles, concepts with the same name) are
computed here, at build time only: bundle content never links across bundles
(D12), the site does.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from dataclasses import asdict
from itertools import combinations
from pathlib import Path

import yaml
from bib_to_md import parse_bib
from bundles import ROOT, Bundle, registry

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ROOT_LINK = re.compile(r"\]\(/(?!/)")
PAGE_LINK = re.compile(r"\]\((/[^)\s#]+\.md)(?:#[^)\s]*)?\)")
MATH = re.compile(r"\$+([^$]*)\$+")
FENCE = re.compile(r"^\s*(```|~~~)")
RESERVED = {"index.md", "log.md", "bibliography.md"}
FOLDER_TITLES = {
    "definitions": "Definitions",
    "methods": "Methods",
    "operators": "Operators",
    "results": "Results",
    "properties": "Properties",
    "benchmarks": "Benchmarks",
    "software": "Software",
    "sources": "Sources",
}


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return the parsed YAML frontmatter (empty if none) and the body."""
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end() :]


def plain(title: str) -> str:
    """A title without math delimiters, for the HTML title and graph labels."""
    return " ".join(MATH.sub(r"\1", title).replace("\\", "").replace("{", "").replace("}", "").split())


def rewrite_links(body: str, slug: str) -> str:
    """Prefix bundle-root links with ``/bundles/<slug>``, outside code fences."""
    out, fenced = [], False
    for line in body.splitlines(keepends=True):
        if FENCE.match(line):
            fenced = not fenced
        out.append(line if fenced else ROOT_LINK.sub(f"](/bundles/{slug}/", line))
    return "".join(out)


def page_frontmatter(meta: dict, rel: Path, bundle: Bundle) -> dict:
    """The frontmatter of a generated page: the wiki's own plus site keys."""
    fm = {k: v for k, v in meta.items() if k != "okf_version"}
    fm["bundle"] = bundle.slug
    fm["bundleTitle"] = bundle.title
    fm["wikiPath"] = rel.as_posix()
    if rel == Path("index.md"):
        fm["title"] = bundle.title
    elif rel.name == "index.md":
        fm["title"] = f"{FOLDER_TITLES.get(rel.parent.name, rel.parent.name)} | {bundle.title}"
    elif rel.name in RESERVED:
        fm["title"] = f"{rel.stem.capitalize()} | {bundle.title}"
    if "title" in fm:
        fm["okfTitle"] = fm["title"]
        fm["title"] = plain(str(fm["title"]))
    return fm


def emit(fm: dict, body: str) -> str:
    """Serialize a page with YAML frontmatter."""
    head = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1_000_000)
    return f"---\n{head}---\n\n{body.lstrip()}"


def sync_bundle(bundle: Bundle, out: Path, root: Path = ROOT) -> dict:
    """Write one bundle's pages; return its graph (nodes and edges)."""
    wiki = root / bundle.slug / "wiki"
    dest = out / "bundles" / bundle.slug
    if dest.exists():
        shutil.rmtree(dest)
    nodes, edges = {}, set()
    for path in sorted(wiki.rglob("*.md")):
        rel = path.relative_to(wiki)
        meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        page = rewrite_links(body, bundle.slug)
        if rel == Path("bibliography.md"):
            page = page.replace(
                "\n\n",
                f"\n\nDownload the citation record as BibTeX: [bibliography.bib](/bundles/{bundle.slug}/bibliography.bib).\n\n",
                1,
            )
        target.write_text(emit(page_frontmatter(meta, rel, bundle), page), encoding="utf-8")
        if rel.name in RESERVED:
            continue
        node_id = "/" + rel.as_posix()
        nodes[node_id] = {
            "id": node_id,
            "title": plain(str(meta.get("title", rel.stem))),
            "type": str(meta.get("type", "")),
            "status": str(meta.get("status", "")),
            "url": f"/bundles/{bundle.slug}/{rel.with_suffix('').as_posix()}",
        }
        for m in PAGE_LINK.finditer(body):
            if m.group(1) != node_id:
                edges.add(tuple(sorted((node_id, m.group(1)))))
    bib = wiki / "bibliography.bib"
    if bib.is_file():
        public = out / "public" / "bundles" / bundle.slug
        public.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(bib, public / "bibliography.bib")
    (dest / "graph.md").write_text(
        emit(
            {
                "title": f"Page graph | {bundle.title}",
                "layout": "page",
                "bundle": bundle.slug,
                "bundleTitle": bundle.title,
            },
            f'<PageGraph bundle="{bundle.slug}" />\n',
        ),
        encoding="utf-8",
    )
    links = [{"source": a, "target": b} for a, b in sorted(edges) if a in nodes and b in nodes]
    return {"bundle": bundle.slug, "title": bundle.title, "nodes": list(nodes.values()), "links": links}


def sidebar(graph: dict, bundle: Bundle) -> list[dict]:
    """The site sidebar of one bundle: its entry pages, then one link per folder index.

    Pages are not listed one by one: VitePress renders the sidebar into every
    page, and a folder index already lists its pages with their descriptions.
    """
    base = f"/bundles/{bundle.slug}/"
    count: dict[str, int] = {}
    for node in graph["nodes"]:
        parts = node["id"].strip("/").split("/")
        if len(parts) > 1:
            count[parts[0]] = count.get(parts[0], 0) + 1
    return [
        {
            "text": bundle.title,
            "items": [
                {"text": "Reading guide", "link": base},
                {"text": "Notation registry", "link": base + "notation"},
                {"text": "Page graph", "link": base + "graph"},
                {"text": "Bibliography", "link": base + "bibliography"},
                {"text": "Log", "link": base + "log"},
            ],
        },
        {
            "text": "Pages by type",
            "items": [
                {"text": f"{FOLDER_TITLES[f]} ({count[f]})", "link": f"{base}{f}/"} for f in FOLDER_TITLES if f in count
            ],
        },
        {"text": "All bundles", "items": [{"text": "Bundle list and map", "link": "/bundles/"}]},
    ]


def work_identity(fields: dict) -> str:
    """A cross-bundle identity for a cited work: DOI, else normalized title and year."""
    doi = fields.get("doi", "").strip().lower()
    if doi:
        return "doi:" + doi
    title = re.sub(r"[^a-z0-9]+", " ", fields.get("title", "").lower()).strip()
    return f"title:{title}|{fields.get('year', '')}" if title else ""


def source_identity(meta: dict) -> str:
    """A cross-bundle identity for an ingested source: its ``resource``."""
    return str(meta.get("resource", "")).strip().lower()


def concept_names(meta: dict, stem: str) -> set[str]:
    """Normalized names of a concept page: file stem, title and aliases.

    Two pages of different bundles sharing a name are *related*, not
    identical: an alias match (``samePage`` false) can be loose.
    """
    names = {stem}
    for raw in [meta.get("title", ""), *(meta.get("aliases") or [])]:
        name = re.sub(r"\([^)]*\)", "", plain(str(raw)).lower())
        name = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
        if len(name) > 3:
            names.add(name)
    return names


def overlaps(bundles: list[Bundle], root: Path = ROOT) -> list[dict]:
    """Pairwise overlaps between bundles: shared cited works, sources and concepts."""
    works, sources, concepts = {}, {}, {}
    for b in bundles:
        wiki = root / b.slug / "wiki"
        bib = wiki / "bibliography.bib"
        works[b.slug] = (
            {i for e in parse_bib(bib.read_text(encoding="utf-8")) if (i := work_identity(e["fields"]))}
            if bib.is_file()
            else set()
        )
        sources[b.slug], concepts[b.slug] = {}, {}
        for path in sorted(wiki.rglob("*.md")):
            if path.name in RESERVED:
                continue
            meta, _ = split_frontmatter(path.read_text(encoding="utf-8"))
            rel = path.relative_to(wiki)
            page = {
                "title": plain(str(meta.get("title", path.stem))),
                "url": f"/bundles/{b.slug}/{rel.with_suffix('').as_posix()}",
            }
            if meta.get("type") == "Source":
                if ident := source_identity(meta):
                    sources[b.slug][ident] = page
            elif rel.parent != Path("."):
                for name in concept_names(meta, path.stem):
                    concepts[b.slug].setdefault(name, page)
    pairs = []
    for a, b in combinations([x.slug for x in bundles], 2):
        shared_sources = [{"a": sources[a][i], "b": sources[b][i]} for i in sorted(set(sources[a]) & set(sources[b]))]
        matched: dict[tuple[str, str], dict] = {}
        for name in sorted(set(concepts[a]) & set(concepts[b])):
            pa, pb = concepts[a][name], concepts[b][name]
            pair = matched.setdefault((pa["url"], pb["url"]), {"a": pa, "b": pb, "names": []})
            pair["names"].append(name)
        shared_concepts = []
        for pair in matched.values():
            pair["samePage"] = pair["a"]["url"].rsplit("/", 1)[1] == pair["b"]["url"].rsplit("/", 1)[1]
            shared_concepts.append(pair)
        shared_concepts.sort(key=lambda p: (not p["samePage"], p["a"]["title"].lower()))
        pairs.append(
            {
                "a": a,
                "b": b,
                "sharedWorks": len(works[a] & works[b]),
                "sharedSources": shared_sources,
                "sharedConcepts": shared_concepts,
            }
        )
    return pairs


def main(argv: list[str], root: Path = ROOT) -> int:
    out = Path(argv[1]) if len(argv) > 1 else root / "docs"
    data = out / "public" / "data"
    data.mkdir(parents=True, exist_ok=True)
    bundles = registry(root)
    sidebars = {}
    for b in bundles:
        graph = sync_bundle(b, out, root)
        (data / f"{b.slug}.graph.json").write_text(json.dumps(graph, ensure_ascii=False), encoding="utf-8")
        sidebars[f"/bundles/{b.slug}/"] = sidebar(graph, b)
        print(f"{b.slug}: {len(graph['nodes'])} pages, {len(graph['links'])} links")
    generated = out / ".vitepress" / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    nav = [{"text": b.title, "link": f"/bundles/{b.slug}/"} for b in bundles]
    (generated / "bundles.json").write_text(
        json.dumps({"sidebars": sidebars, "nav": nav}, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    payload = {"bundles": [asdict(b) for b in bundles], "overlaps": overlaps(bundles, root)}
    (data / "bundles.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    for p in payload["overlaps"]:
        print(
            f"{p['a']} x {p['b']}: {p['sharedWorks']} cited works, "
            f"{len(p['sharedSources'])} sources, {len(p['sharedConcepts'])} concepts"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
