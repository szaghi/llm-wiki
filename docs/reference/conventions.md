---
title: Writing rules
---

# Writing rules

These rules apply to every page the compiler writes. They come from the constitution
([`CLAUDE.md`](/reference/constitution)); the decision numbers (D1, D2, ...) point into the
[decision record](/reference/decisions), where each rule's rationale is kept. Where `tools/lint_okf.py` enforces a
rule, the rule says so.

## Mathematics

1. **Syntax.** Only `$...$` (inline) and `$$...$$` (display), which KaTeX can render. Multi-line derivations go in
   `$$\begin{aligned}...\end{aligned}$$`. The lint fails on `\(` or `\[` delimiters, and on unbalanced `$` or `$$`,
   outside code.
2. **Canonical notation in concept pages.** The bundle's `wiki/notation.md` is the only normative symbol registry.
   Concept pages must not use the notation of the paper they came from (D5).
3. **Extend before use.** When a new operator family needs a symbol, the registry is extended first and the extension
   is logged. Registry rows added later carry their date.
4. **Notation maps.** Each Source page has a `# Notation map` that translates the source's own symbols into canonical
   ones, wherever they differ. It is the audit trail of every translation decision: a mistranslated symbol is how a
   compiled wiki silently corrupts a theorem's hypotheses.

The site renders math with KaTeX at build time, so it also checks this rule: a formula KaTeX cannot parse is shown in
red.

## Linking

* Links are **absolute and bundle-relative**: `[$P_D$](/operators/divergence-prolongation.md)`. Relative links are
  tolerated only between pages in the same folder.
* No `[[wikilinks]]`. They are one viewer's dialect, and they break `grep` and conformance (D9).
* The meaning of a link lives in the sentence around it ("*is algebraically equivalent to*", "*contradicts*", "*is
  tested on*"), never in the link itself. OKF links are untyped by design.
* A broken link is an error, stricter than OKF requires. The lint resolves every link in every page and reserved file:
  `http(s)://`, `doi:` and `mailto:` targets are skipped, and `#anchors` are ignored.
* Bundles never link to one another (D12). The site computes cross-bundle overlaps at build time instead (see the
  [bundle map](/bundles/)).

## Indexes

* Every folder has an `index.md` with one line per page:

  ```markdown
  * [Title](/methods/page.md) — One-line description.
  ```

* The description in the index line must match the page's frontmatter `description` (a trailing period is ignored).
  The lint fails on a page missing from its folder index, on a duplicate entry, and on drift between the two
  descriptions.
* The bundle root `index.md` is **curated**, not generated: a reading guide ordered by conceptual importance. It is the
  entry point every session reads first (D9).
* Folder indexes are kept in a stable order, but not always alphabetical (one bundle lists its Source pages newest
  first). Check the existing order before inserting a line.

## The log

`wiki/log.md` is the bundle's append-only journal. It has no frontmatter, and its entries are grouped under
`## YYYY-MM-DD` headings, newest first. Each ingestion, deep lint, registry extension or fiat closure adds an entry
that names the pages it touched. The site uses the newest date as the bundle's "updated" date.

## Merging claims

When a new source touches an existing page (D7):

* **It agrees**: add the citation. Several citations are visible evidence strength.
* **It extends**: integrate it in canonical notation, cited.
* **It contradicts**: record the disagreement under `## Contradictions`, attributed, with both sides cited. A more
  recent source does not win by being more recent, and nothing is silently overwritten.

A contradiction closes only in two ways:

* a source explicitly supersedes the other (an erratum, a corrected proof);
* the human closes it by fiat. The fiat closure is recorded on the page, attributed as `status: hypothesis`.

## Layers

| Layer | Contents | Who writes it |
| --- | --- | --- |
| 1: sources | external archives (referenced in place through `local_file`) and `raw/` captures | nobody: immutable |
| 2: bundle | `wiki/`: concept pages, Source pages, registry, indexes, log, bibliography | the compiler |
| 0: law | `CLAUDE.md`, `DECISIONS.md`, `tools/`, bundle `CLAUDE.md` and `bundle.toml` | the human |

* Layer 1 is never modified, renamed or deleted. Captures are written once at ingestion, then frozen.
* Durable sources are referenced, never copied (D6). Only content that could disappear (web pages, loose documents)
  is captured, under `raw/web/` or `raw/docs/`.
* Another project's records enter only as a frozen capture under `raw/docs/<slug>/`, pinned to a commit or date.
  Their claims are hypotheses, and they cannot promote a claim or close a contradiction on their own (D12 amendment).

## Git

* Conventional Commits. An ingestion is one staged unit with the message `docs(<bundle>): ingest <source-slug>`. A
  bundle whose law ingests in chunks stages one unit per chunk, `docs(<bundle>): ingest chunk N: <slugs>`.
* **The compiler stages; the human commits** (D14). Claude runs `git add -A` and prints the message; you commit, with
  your GPG key if you sign. The compiler never runs `git commit` and never touches `commit.gpgsign`.
* Never add `Co-authored-by` lines.
* The resume point is always the last commit. `git status` shows how the previous session ended:

| State | Meaning | Action |
| --- | --- | --- |
| clean | the human committed | continue |
| fully staged | ingestion complete, awaiting the human's commit | review and commit |
| unstaged changes | aborted mid-source | discard them and start the source again |
