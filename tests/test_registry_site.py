"""tools/bundles.py (registry) and tools/site_sync.py (site generator) on the fixture repository."""

from __future__ import annotations

import json
from pathlib import Path

import bib_to_md
import bundles
import pytest
import site_sync
from conftest import write_bundle


def test_registry_derives_counts(repo: Path) -> None:
    (b,) = bundles.registry(repo)
    assert (b.slug, b.title, b.sources, b.concepts) == ("mini", "Mini bundle", 1, 1)
    assert b.by_type == {"methods": 1}
    assert (b.cited_works, b.frontier, b.contested, b.hypotheses) == (2, 1, 1, 0)
    assert b.updated == "2026-01-02"


def test_registry_rejects_incomplete_card(repo: Path) -> None:
    (repo / "mini" / "bundle.toml").write_text('title = "x"\n', encoding="utf-8")
    with pytest.raises(bundles.RegistryError, match="missing"):
        bundles.registry(repo)


def test_generated_regions(repo: Path) -> None:
    files = bundles.generated_files(bundles.registry(repo), repo)
    readme = files[repo / "README.md"]
    assert "[Mini bundle](mini/wiki/index.md)" in readme
    skill = files[repo / "skills" / "llm-wiki" / "SKILL.md"]
    assert skill.splitlines()[2].startswith('description: "Consult')
    assert "mini (foo, bar)" in skill
    assert "Mini bundle (`mini/wiki/`)" in skill


def test_missing_markers_raise(repo: Path) -> None:
    (repo / "README.md").write_text("# no markers\n", encoding="utf-8")
    with pytest.raises(bundles.RegistryError, match="markers"):
        bundles.generated_files(bundles.registry(repo), repo)


def test_rewrite_links_skips_code() -> None:
    body = "See [a](/methods/a.md).\n```\n[b](/methods/b.md)\n```\nand [c](https://x.org/c).\n"
    out = site_sync.rewrite_links(body, "mini")
    assert "[a](/bundles/mini/methods/a.md)" in out
    assert "[b](/methods/b.md)" in out
    assert "[c](https://x.org/c)" in out


def test_plain_strips_math() -> None:
    assert site_sync.plain(r"SBP interpolation $I_{C2F}$") == "SBP interpolation I_C2F"


def test_site_sync_writes_pages_and_data(repo: Path) -> None:
    out = repo / "docs"
    assert site_sync.main(["site_sync.py", str(out)], root=repo) == 0
    page = (out / "bundles" / "mini" / "methods" / "foo.md").read_text(encoding="utf-8")
    meta, body = site_sync.split_frontmatter(page)
    assert meta["bundle"] == "mini" and meta["wikiPath"] == "methods/foo.md" and meta["type"] == "Method"
    assert "(/bundles/mini/sources/bar-2020.md)" in body
    assert (out / "bundles" / "mini" / "graph.md").is_file()
    assert (out / "public" / "bundles" / "mini" / "bibliography.bib").is_file()
    assert "bibliography.bib" in (out / "bundles" / "mini" / "bibliography.md").read_text(encoding="utf-8")
    graph = json.loads((out / "public" / "data" / "mini.graph.json").read_text(encoding="utf-8"))
    ids = {n["id"] for n in graph["nodes"]}
    assert ids == {"/notation.md", "/methods/foo.md", "/sources/bar-2020.md"}
    assert {"source": "/methods/foo.md", "target": "/sources/bar-2020.md"} in graph["links"]
    sidebars = json.loads((out / ".vitepress" / "generated" / "bundles.json").read_text(encoding="utf-8"))
    assert "/bundles/mini/" in sidebars["sidebars"]


def test_overlaps_between_bundles(repo: Path) -> None:
    wiki = write_bundle(repo, "other")
    assert bib_to_md.main([str(wiki)]) == 0
    (pair,) = site_sync.overlaps(bundles.registry(repo), repo)
    assert pair["sharedWorks"] == 2
    assert len(pair["sharedSources"]) == 1
    (concept,) = pair["sharedConcepts"]
    assert concept["samePage"] and "foo" in concept["names"]
