"""tools/lint_okf.py: a clean bundle passes, each law violation fails."""

from __future__ import annotations

from pathlib import Path

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
