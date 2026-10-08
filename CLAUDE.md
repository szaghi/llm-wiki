# OKF Wiki Compiler Constitution

You (Claude Code) are the **stateful compiler** of the knowledge bundles in this
repository. This file is repo-wide law. Each bundle adds its own `CLAUDE.md` with
bundle-specific law. Rationale for every rule lives in `DECISIONS.md` — challenge
rules there, not by silently deviating.

## Repository topology

```
~/llm-wiki/
├── CLAUDE.md            # this file — repo-wide law
├── DECISIONS.md         # rationale record (ADR-lite)
├── tools/               # deterministic tooling (linter, bib generator/merger, worklist)
└── <bundle>/            # one directory per knowledge bundle
    ├── CLAUDE.md        # bundle law (corpus location, domain notes)
    ├── raw/             # Layer 1 captures: web/ (md snapshots), docs/
    └── wiki/            # Layer 2: OKF v0.1 bundle root
```

Bundles are mutually independent and **agnostic of any external repository**.
Never reference, read from, or depend on other projects' repos in bundle content.

## Layer rules

- **Layer 1 (immutable):** `raw/` captures and every externally referenced source
  location (e.g. a PDF archive named in bundle law) are read-only. Never modify,
  rename, or delete. Captures are written once at ingestion, then frozen.
- **Sibling-project records** (docs, issues, run data of another repository)
  enter only as a frozen capture under `raw/docs/<slug>/`, pinned to a commit
  or date, never read live. Their claims are `hypothesis` and can neither
  promote a claim to `established` nor close a `Contradictions` entry on
  their own. An evolved record gets a new capture and a new slug (D12
  amendment).
- **Layer 2 (compiler-owned):** `wiki/` is yours to write. The human browses it.
- Anything git-ignored or stateful (caches, indexes) is disposable.

## OKF conformance (v0.1)

- Every non-reserved `.md` under `wiki/` is a **Concept Document**: parseable YAML
  frontmatter with a non-empty `type`, then a Markdown body.
- Reserved files: `index.md` (directory catalog, **no frontmatter** — except the
  bundle root `index.md`, which carries only `okf_version: "0.1"`), `log.md`
  (append-only change history, no frontmatter, newest-first `## YYYY-MM-DD` groups),
  and `bibliography.md` (generated citation record, no frontmatter, never
  hand-edited — see **Bibliography**).
- Filenames: kebab-case.
- Conventional body sections where applicable: `# Schema`, `# Examples`,
  `# Citations`, plus this repo's `# Notation map` (Source pages) and
  `## Contradictions` (concept pages).

## Type taxonomy and folder map

| `type` | folder | covers |
|---|---|---|
| `Definition` | `definitions/` | precise domain terms |
| `Method` | `methods/` | algorithms and schemes |
| `Operator` | `operators/` | discrete operators with an algebraic identity |
| `Result` | `results/` | theorems, proved properties, impossibility results |
| `Property` | `properties/` | constraints/invariants a method can hold |
| `Benchmark` | `benchmarks/` | standard test problems |
| `Software` | `software/` | codes embodying methods |
| `Source` | `sources/` | one page per ingested source |

`type` and folder must agree. Root-level concept pages (e.g. `notation.md`) are
permitted. A conjecture is `type: Result` + `status: hypothesis` — there is no
separate Conjecture type.

## Frontmatter schemas

**Concept page** (all types except `Source`):

```yaml
---
type: Operator                     # REQUIRED, from the taxonomy
title: "Divergence-space prolongation $P_D$"
description: "One-sentence summary."
status: established                # REQUIRED: established | hypothesis
symbol: "$P_D$"                    # Operator pages only
aliases: [div-preserving prolongation]   # optional
tags: [amr-interface]              # bundle-native vocabulary, emergent
timestamp: 2026-07-08T00:00:00Z    # ISO 8601, last meaningful change
---
```

`status` is **claim-kind, not trust**: `established` = published, peer-reviewed
result; `hypothesis` = a claim that a published source could still overturn
(including claims originating from the human's own notes). Sources are trusted
ab origine — there is no trust field.

**Source page:**

```yaml
---
type: Source
title: "Evans & Hawley (1988) — Constrained transport"
description: "One-sentence summary of the source's contribution."
resource: "doi:10.1086/166684"     # REQUIRED: DOI | URL | permanent identifier
source_kind: paper                 # REQUIRED: paper|book|thesis|blog|notes|slides|code|report
authors: [Evans C.R., Hawley J.F.]
year: 1988
venue: "Astrophys. J."
local_file: "/absolute/path/to/file.pdf"   # where the raw source lives
tags: []
timestamp: 2026-07-08T00:00:00Z
---
```

Metadata is derived from the source itself (page-1 content), never from
filenames or embedded metadata alone. Never fabricate a DOI; if no permanent
identifier is recoverable, use the best stable URL and say so in the body.

## Mathematics (binding)

1. **Syntax:** `$...$` / `$$...$$` only (KaTeX-renderable). Never `\(...\)` or
   `\[...\]`. Multi-line derivations in `$$\begin{aligned}...\end{aligned}$$`.
2. **Canonical notation is law in concept pages.** The bundle's `wiki/notation.md`
   is the single normative symbol registry. Concept pages must not use
   paper-native notation. Extend the registry (and log the extension) when a new
   operator family appears.
3. **Source pages carry a `# Notation map`** translating the source's native
   symbols to canonical ones whenever they differ. This is the audit trail for
   every translation decision.

## Linking

- **Absolute bundle-relative Markdown links only**: `[$P_D$](/operators/divergence-prolongation.md)`.
  Relative links tolerated only between same-folder siblings. No `[[wikilinks]]`.
- Link semantics live in the surrounding prose ("*is algebraically equivalent
  to*", "*contradicts*", "*is tested on*"), never in link machinery.
- A broken link is a compiler error (stricter than OKF): the linter fails on it.

## Indexes

- Every folder gets an `index.md`: entries `[Title](/path.md) — one-line description.`
- Maintained by the compiler at every ingestion; the linter enforces completeness
  (every concept listed exactly once in its folder's index) and description
  consistency (index line matches frontmatter `description`).
- The bundle root `index.md` is **curated** for progressive disclosure: ordered by
  conceptual importance, with a short reading guide. It is the entry point every
  session reads first.

## Bibliography

Each bundle with scholarly sources maintains a **complete citation record**:
every work cited by any ingested source, whether or not it is itself ingested.
Ingesting a paper means reading its reference list — that reading is captured,
not discarded. (Rationale: D15.)

- **Canonical store: `wiki/bibliography.bib`** — a compiler-owned data artifact
  (not a Concept Document) in a strict BibTeX subset (`field = {value}`, one
  entry per work, entries sorted by key, `%` comments). Entry keys use the same
  kebab-case `firstauthor-year[-disambig]` convention as Source-page slugs; an
  entry whose key matches `sources/<key>.md` **is** that ingested source —
  ingested-ness is derived from the key match, never stored in a field.
- Every entry carries the custom field `citedby = {slug-1, slug-2}` (sorted,
  duplicate-free): the ingested sources in whose reference lists the work
  appears. This is the bundle's citation graph; heavily cited non-ingested
  entries are the **derived ingestion frontier** — candidates the corpus
  itself does not yet contain.
- Reference lists are merged **complete, unfiltered**: relevance filtering is a
  judgment call that destroys data; dedup and `citedby` counts do the ranking.
  For scoped reads (books, long reviews), the reference extraction may be
  scoped to the chapters read — record the scope on the Source page.
- Metadata comes from the citing source's reference list (and from page 1 of
  the PDF for ingested works). Never fabricate a DOI: include one only when
  printed in the reference list or verified.
- **Generated view: `wiki/bibliography.md`** — written by
  `python3 tools/bib_to_md.py <bundle>/wiki`, never hand-edited. The linter
  fails when it is out of sync with the `.bib`.
- Progress is derived, never stored (D8): a source's reference list is merged
  iff its slug appears in ≥1 `citedby` field;
  `python3 tools/bib_to_md.py <bundle>/wiki --pending` lists the remainder.
- **Batched backfill merger: `tools/bib_merge.py`** (D16). For merging **many**
  pre-existing sources' reference lists at once (the D15 backfill of a corpus
  that predates the citation record), not the ordinary per-source ingestion
  step — for one new source, hand-edit the `.bib`. It merges `frag-<slug>.bib`
  fragments under a human-reviewed resolutions module, **flags** every identity
  collision (same-key different-work `[conflict]`, placeholder-title venue
  mismatch `[venuecheck]`, near-duplicate `[suspect]`) and refuses `--write`
  until `FLAGS: 0`. Its `--dupes` mode is a **mandatory closing sweep after the
  final batch**: the per-batch merge dedups by key and keys follow each citing
  source's spelling, so the same work under two first-author spellings (OCR
  variants, mis-transcribed or reordered authors) lands under two keys that no
  per-batch check can relate — only a whole-corpus title+year sweep finds them.
  Full workflow and resolution-table semantics are in the tool's docstring.
  A `[venuecheck]` flag is the decisive signal for title-less (ApJ/PRD/A&A)
  citations — heed it; and treat a `SILENCED` pair as a verified claim, never a
  convenient dismissal.

## Ingestion protocol (atomic per source)

For each source, in order:

1. **Read fully.** PDFs: prefer text extraction; when it fails (image-only scans),
   read page-by-page visually. If genuinely illegible, the Source page records the
   gap explicitly — never guess an equation.
2. **Extract concepts** the source touches; apply the granularity rules below.
3. **Create or merge** concept pages:
   - *Agrees with existing claim* → add the citation (multiple citations = visible
     evidence strength).
   - *Extends* → integrate in canonical notation, cited.
   - *Contradicts* → record under `## Contradictions`, attributed, both sides
     cited. **Recency never wins; nothing is silently overwritten.** A
     contradiction closes only when a source explicitly supersedes another, or the
     human closes it by fiat — a fiat closure is recorded and carries
     `status: hypothesis` attribution.
4. **Write the Source page**: verified metadata, `# Notation map`, and an audit
   list of every page created or updated in this run.
5. **Merge the reference list** into `wiki/bibliography.bib` (see
   **Bibliography**): one entry per cited work, complete and unfiltered; dedup
   by key; append this source's slug to each cited entry's `citedby`; then
   regenerate `wiki/bibliography.md` (`python3 tools/bib_to_md.py <bundle>/wiki`).
6. **Append to `log.md`** (dated entry, pages touched).
7. **Update affected `index.md` files.**
8. **Lint**: `python3 tools/lint_okf.py <bundle>/wiki` must pass.
9. **Stage and hand off**: `git add -A`, then present the prepared commit
   message `docs(<bundle>): ingest <source-slug>` to the human. **The compiler
   never commits** — commits are reserved to the human (GPG-signed).

"Is it ingested?" has exactly one answer: a Source page exists. There is no
inbox, no queue file — the worklist is derived (`tools/worklist.sh`).

**Interrupted work:** ingestion is atomic at source granularity —
complete-and-stage or discard (`git checkout`). The resume point is always the
last commit; `git status` tells any session how the previous one ended:
clean = committed by the human; fully staged = ingestion complete, awaiting the
human's commit; unstaged noise = aborted mid-source, discard it.

## Granularity — what earns a page

A page must satisfy at least one of:

1. **Evidence or substance:** ≥2 sources touch it, *or* a single source presents
   it as a substantive named contribution (a method, theorem, benchmark that is
   the point of the paper, not a passing mention);
2. **Algebraic identity:** an operator or property with its own exact statement;
3. **Load-bearing definition:** a term whose precise meaning decides domain
   classifications.

Everything else stays inline in its parent page until it qualifies. **No stubs:**
minimum page = frontmatter + real definition + one citation. A page splits when it
accumulates internally contradicting sub-variants; the split boundary is where the
contradiction lives.

## Verification

- **Deterministic lint** (`tools/lint_okf.py`) at every ingestion; must pass
  before commit.
- **Deep lint** (LLM audit) every 10 ingestions and before any human-declared
  milestone: re-read a folder against `notation.md` and related pages; flag
  notation drift, stale contradictions, tag synonyms; record findings in `log.md`;
  fix with human visibility.

## Query

Navigation **is** the query engine: enter at the root `index.md`, follow links,
`grep` symbols and tags. No vector search, no embedding infrastructure, no
external search dependency. Revisit only if the bundle outgrows navigation
(record any such change in `DECISIONS.md`).

## Git discipline

- Conventional Commits. **Never** add `Co-authored-by` lines.
- **The compiler stages; the human commits.** One staged unit + prepared
  message per ingested source (`docs(<bundle>): ingest <source-slug>`); the
  human commits with their GPG key. The compiler never runs `git commit` and
  never touches `commit.gpgsign`. (Rule corrected 2026-07-08 — see D14.)
