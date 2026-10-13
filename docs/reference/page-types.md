---
title: Page types and frontmatter
---

# Page types and frontmatter

A bundle's `wiki/` directory is an [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle root. Every `.md` file under it is either a **concept document** or a **reserved file**. This page states the
rules. Each rule comes from the constitution ([`CLAUDE.md`](/reference/constitution)), and the notes say which rules
`tools/lint_okf.py` enforces.

## Type taxonomy and folder map

Every concept document has a `type`, and its folder must agree with that type (D4):

| `type` | Folder | Covers |
| --- | --- | --- |
| `Definition` | `definitions/` | precise domain terms |
| `Method` | `methods/` | algorithms and schemes |
| `Operator` | `operators/` | discrete operators with an algebraic identity |
| `Result` | `results/` | theorems, proved properties, impossibility results |
| `Property` | `properties/` | constraints and invariants a method can hold |
| `Benchmark` | `benchmarks/` | standard test problems |
| `Software` | `software/` | codes that embody methods |
| `Source` | `sources/` | one page per ingested source |

Concept pages may also sit at the bundle root. The notation registry, `notation.md`, is one of them (`type:
Definition`). There is no `Conjecture` type: a conjecture is a `Result` with `status: hypothesis`. There is no `Person`
type either: authors are metadata of the sources.

The lint fails when a page's `type` disagrees with its folder. It warns when a page sits in a folder outside the map.

## Concept page frontmatter

This schema applies to every type except `Source`:

```yaml
---
type: Operator                     # required, from the taxonomy
title: "Divergence-space prolongation $P_D$"
description: "One-sentence summary."
status: established                # required: established | hypothesis
symbol: "$P_D$"                    # Operator pages only
aliases: [div-preserving prolongation]   # optional
tags: [amr-interface]              # optional; bundle-native vocabulary
timestamp: 2026-07-08T00:00:00Z    # required: ISO 8601, last meaningful change
---
```

| Field | Required | Values |
| --- | --- | --- |
| `type` | yes | one of the eight types; must agree with the folder |
| `title` | yes | display name; may contain `$...$` math |
| `description` | yes | one sentence; the folder index line repeats it verbatim |
| `status` | yes | `established` or `hypothesis` |
| `symbol` | Operator pages | the operator's canonical symbol, from the notation registry |
| `aliases` | no | other names; the site's bundle map also matches them across bundles |
| `tags` | no | emergent, bundle-native vocabulary; a deep lint merges synonyms |
| `timestamp` | yes | ISO 8601 date or date-time |

The lint checks every required field. It also checks the description against its folder index line (see
[Indexes](/reference/conventions#indexes)). It does not check `symbol` on Operator pages.

## Source page frontmatter

```yaml
---
type: Source
title: "Evans & Hawley (1988) — Constrained transport"
description: "One-sentence summary of the source's contribution."
resource: "doi:10.1086/166684"     # required: DOI | URL | permanent identifier
source_kind: paper                 # required
authors: [Evans C.R., Hawley J.F.]
year: 1988
venue: "Astrophys. J."
local_file: "/absolute/path/to/file.pdf"   # where the raw source lives
tags: []
timestamp: 2026-07-08T00:00:00Z
---
```

| Field | Required | Values |
| --- | --- | --- |
| `resource` | yes | `doi:...`, an arXiv id, a URL or another permanent identifier |
| `source_kind` | yes | `paper`, `book`, `thesis`, `blog`, `notes`, `slides`, `code`, `report` |
| `authors`, `year`, `venue` | by schema | from page 1 of the source itself |
| `local_file` | by schema | absolute path of the compiler's copy; not distributed |
| `title`, `description` | yes | as on concept pages |
| `timestamp` | yes | ISO 8601 |

Source pages carry no `status`. Sources are trusted from the start, because the human reviewed each one before
ingestion (D2). The metadata comes from the source's page 1, never from file names or embedded PDF metadata. A DOI is
never invented: when no permanent identifier can be recovered, `resource` holds the best stable URL, and the body
says so.

The page slug, which is also the file name, follows `firstauthor-year[-disambiguator]`, for example `balsara-2009-b`.
The same key names the work in `bibliography.bib`, and that match is what makes the work count as ingested (see
[Bibliography format](/reference/bibliography)).

## Body sections

| Section | Where |
| --- | --- |
| `# Schema`, `# Examples`, `# Citations` | OKF conventional sections, where they apply |
| `# Notation map` | every Source page whose native symbols differ from the registry |
| `## Contradictions` | concept pages where sources disagree |
| `# Pages created or updated` | Source pages: the audit list of the ingestion run |

## Reserved files

| File | Frontmatter | Content |
| --- | --- | --- |
| `index.md` | none (the bundle root `index.md` carries only `okf_version: "0.1"`) | catalog of the directory |
| `log.md` | none | append-only change history, in newest-first `## YYYY-MM-DD` groups |
| `bibliography.md` | none | generated by `tools/bib_to_md.py`, never edited |

The lint fails when a reserved file carries frontmatter (other than the root `okf_version`). It checks every link in
reserved files as well.

File names are kebab-case: `[a-z0-9]+(-[a-z0-9]+)*.md`.

## Status: claim kind, not trust

`status` says what kind of claim a page makes, not how far to trust it (D3):

* **`established`**: a published, peer-reviewed result.
* **`hypothesis`**: a claim a published source could still overturn. This includes claims from your own notes, from
  frozen captures of sibling projects, and contradictions closed by human fiat.

Without the distinction, a wiki turns your hypotheses into literature facts and serves them back to you as outside
confirmation. Anyone who reads or quotes a `hypothesis` page reports it as a hypothesis.

## Granularity: what earns a page

A page must meet at least one of these conditions (D11):

1. **Evidence or substance**: two or more sources touch it, or one source presents it as a substantive named
   contribution, such as the method, theorem or benchmark that is the point of the paper.
2. **Algebraic identity**: an operator or property with its own exact statement.
3. **Load-bearing definition**: a term whose precise meaning decides how the domain classifies things.

Everything else stays inline in its parent page until it qualifies. Stubs are forbidden: the minimum page is
frontmatter, a real definition and one citation. A page splits when it accumulates sub-variants that contradict each
other, and the split boundary is where the contradiction lives.
