"""tools/lint_okf.py: a clean bundle passes, each law violation fails."""

from __future__ import annotations

from pathlib import Path

import bib_to_md
import lint_okf
import pytest


def lint(wiki: Path) -> tuple[int, str]:
    code = lint_okf.main(str(wiki))
    return code, "\n".join(lint_okf.errors + lint_okf.warnings)


def test_clean_bundle_passes(repo: Path) -> None:
    code, out = lint(repo / "mini" / "wiki")
    assert code == 0, out


def test_second_run_starts_clean(repo: Path) -> None:
    wiki = repo / "mini" / "wiki"
    page = wiki / "methods" / "foo.md"
    good = page.read_text(encoding="utf-8")
    page.write_text("no frontmatter\n", encoding="utf-8")
    assert lint(wiki)[0] == 1
    page.write_text(good, encoding="utf-8")
    code, out = lint(wiki)
    assert code == 0, out


def test_every_link_of_a_reserved_file_is_checked(repo: Path) -> None:
    wiki = repo / "mini" / "wiki"
    with (wiki / "log.md").open("a", encoding="utf-8") as f:
        f.write("* [ok](/methods/foo.md) and [gone](/methods/missing.md)\n")
    code, out = lint(wiki)
    assert code == 1
    assert "broken link: /methods/missing.md" in out


@pytest.mark.parametrize(
    ("old", "new", "message"),
    [
        ("status: established", "status: proven", "'status' must be"),
        ("type: Method", "type: Result", "disagrees with folder"),
        ("Updates $u$", r"Updates \(u\)", "forbidden LaTeX delimiter"),
        ("Updates $u$", "Updates $u", "unbalanced $ inline-math"),
        ('title: "Foo scheme"\n', "", "missing non-empty 'title'"),
        ("timestamp: 2026-01-01T00:00:00Z", "timestamp: yesterday", "ISO-8601"),
        ("[registry](/notation.md)", "[registry](/notation-gone.md)", "broken link"),
        ('description: "A scheme for $u$."', 'description: "Another description."', "description drift"),
    ],
)
def test_violations_fail(repo: Path, old: str, new: str, message: str) -> None:
    page = repo / "mini" / "wiki" / "methods" / "foo.md"
    page.write_text(page.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
    code, out = lint(repo / "mini" / "wiki")
    assert code == 1
    assert message in out


def _add_orphan_source(wiki: Path, tags: str) -> None:
    page = wiki / "sources" / "baz-2021.md"
    page.write_text(
        '---\ntype: Source\ntitle: "Baz (2021) — Off topic"\ndescription: "An off-topic paper."\n'
        f'resource: "doi:10.1000/baz"\nsource_kind: paper\ntags: {tags}\n'
        "timestamp: 2026-01-01T00:00:00Z\n---\n\n# Summary\n\nOff topic.\n",
        encoding="utf-8",
    )
    with (wiki / "sources" / "index.md").open("a", encoding="utf-8") as f:
        f.write("* [Baz (2021) — Off topic](/sources/baz-2021.md) — An off-topic paper.\n")
    assert bib_to_md.main([str(wiki)]) == 0  # the generated view tracks ingested sources


@pytest.mark.parametrize(("tags", "warned"), [("[context]", False), ("[demo]", True), ("[]", True)])
def test_context_source_is_exempt_from_orphan_warning(repo: Path, tags: str, warned: bool) -> None:
    wiki = repo / "mini" / "wiki"
    _add_orphan_source(wiki, tags)
    code, out = lint(wiki)
    assert code == 0, out
    assert ("sources/baz-2021.md: orphan" in out) is warned


def test_context_tag_does_not_exempt_a_concept_page(repo: Path) -> None:
    wiki = repo / "mini" / "wiki"
    for rel, old, new in [
        ("methods/foo.md", "tags: [demo]", "tags: [context]"),
        ("index.md", "[Foo](/methods/foo.md)", "Foo"),
        ("sources/bar-2020.md", "[Foo](/methods/foo.md)", "Foo"),
    ]:
        page = wiki / rel
        page.write_text(page.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
    _, out = lint(wiki)
    assert "methods/foo.md: orphan" in out, out


def test_unlisted_concept_fails(repo: Path) -> None:
    wiki = repo / "mini" / "wiki"
    (wiki / "methods" / "index.md").write_text("# Methods\n", encoding="utf-8")
    code, out = lint(wiki)
    assert code == 1
    assert "concept not listed: methods/foo.md" in out


def test_source_needs_resource(repo: Path) -> None:
    page = repo / "mini" / "wiki" / "sources" / "bar-2020.md"
    page.write_text(page.read_text(encoding="utf-8").replace('resource: "doi:10.1000/bar"\n', ""), encoding="utf-8")
    code, out = lint(repo / "mini" / "wiki")
    assert code == 1
    assert "missing 'resource'" in out


def test_stale_bibliography_view_fails(repo: Path) -> None:
    wiki = repo / "mini" / "wiki"
    md = wiki / "bibliography.md"
    md.write_text(md.read_text(encoding="utf-8") + "\nhand edit\n", encoding="utf-8")
    code, out = lint(wiki)
    assert code == 1
    assert "out of sync" in out


def test_tilde_fences_are_code(repo: Path) -> None:
    page = repo / "mini" / "wiki" / "methods" / "foo.md"
    page.write_text(page.read_text(encoding="utf-8") + "\n~~~\nprice: $5\n~~~\n", encoding="utf-8")
    code, out = lint(repo / "mini" / "wiki")
    assert code == 0, out


def test_reserved_files_are_math_checked(repo: Path) -> None:
    wiki = repo / "mini" / "wiki"
    with (wiki / "log.md").open("a", encoding="utf-8") as f:
        f.write("* used \\[x\\] here\n")
    code, out = lint(wiki)
    assert code == 1
    assert "forbidden LaTeX delimiter" in out


def test_corporate_author_braces_are_not_rendered() -> None:
    # {{ ... }} in the generated Markdown is Vue interpolation on the site
    entry = {
        "key": "sundials-2021",
        "fields": {"author": "{{SUNDIALS Team}} and Smith, J.", "year": "2021", "title": "T"},
    }
    out = bib_to_md._format_work(entry)
    assert "{{" not in out and out.startswith("SUNDIALS Team; Smith, J. (2021).")
