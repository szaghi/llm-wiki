"""Shared fixtures: a minimal, lint-clean repository with one bundle, built in a temporary directory."""

from __future__ import annotations

from pathlib import Path

import bib_to_md
import pytest

INDEX = """---
okf_version: "0.1"
---

# mini — Knowledge Bundle

Start at the [notation registry](/notation.md), then [Foo](/methods/foo.md).
"""

NOTATION = """---
type: Concept
title: "Notation registry"
description: "Canonical symbols of the mini bundle."
status: established
timestamp: 2026-01-01T00:00:00Z
---

# Notation registry

| Symbol | Meaning |
| --- | --- |
| $u$ | the conserved variable |
"""

FOO = """---
type: Method
title: "Foo scheme"
description: "A scheme for $u$."
status: established
aliases: [foo method]
tags: [demo]
timestamp: 2026-01-01T00:00:00Z
---

# Foo scheme

Updates $u$ ([Bar (2020)](/sources/bar-2020.md)); see the [registry](/notation.md).

## Contradictions

* **Is foo stable?** *Open.* Bar says yes ([Bar (2020)](/sources/bar-2020.md)).

# Citations

1. [Bar (2020)](/sources/bar-2020.md)
"""

BAR = """---
type: Source
title: "Bar (2020) — The foo scheme"
description: "Introduces the foo scheme."
resource: "doi:10.1000/bar"
source_kind: paper
authors: [Bar B.]
year: 2020
venue: "J. Demo"
tags: []
timestamp: 2026-01-01T00:00:00Z
---

# Summary

Introduces [Foo](/methods/foo.md).

# Notation map

| Paper | Canonical |
| --- | --- |
| $q$ | $u$ |
"""

BIB = """% citation record of the mini bundle
@article{bar-2020,
  title = {The foo scheme},
  author = {Bar, B.},
  year = {2020},
  journal = {J. Demo},
  doi = {10.1000/bar},
}

@article{old-1990,
  title = {An old method},
  author = {Old, O.},
  year = {1990},
  journal = {J. Demo},
  doi = {10.1000/old},
  citedby = {bar-2020},
}
"""

CARD = """title = "Mini bundle"
summary = "A minimal bundle for the tests."
keywords = ["foo", "bar"]
"""

GENERATED = "<!-- bundles:start -->\n<!-- bundles:end -->\n"


def write_bundle(root: Path, slug: str = "mini") -> Path:
    """Write a lint-clean bundle ``slug`` under ``root``; return its wiki directory."""
    wiki = root / slug / "wiki"
    for rel, text in {
        "index.md": INDEX,
        "log.md": "# Log\n\n## 2026-01-02\n\n* Ingested [Bar (2020)](/sources/bar-2020.md).\n",
        "notation.md": NOTATION,
        "methods/index.md": "# Methods\n\n* [Foo scheme](/methods/foo.md) — A scheme for $u$.\n",
        "methods/foo.md": FOO,
        "sources/index.md": "# Sources\n\n* [Bar (2020) — The foo scheme](/sources/bar-2020.md) — Introduces the foo scheme.\n",
        "sources/bar-2020.md": BAR,
        "bibliography.bib": BIB,
    }.items():
        path = wiki / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    (root / slug / "bundle.toml").write_text(CARD, encoding="utf-8")
    assert bib_to_md.main([str(wiki)]) == 0  # generate bibliography.md
    return wiki


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A repository root with one bundle, a README and a skill carrying generated regions."""
    write_bundle(tmp_path)
    (tmp_path / "README.md").write_text("# Readme\n\n" + GENERATED, encoding="utf-8")
    skill = tmp_path / "skills" / "llm-wiki"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: llm-wiki\ndescription: x\n---\n\n" + GENERATED, encoding="utf-8")
    return tmp_path
