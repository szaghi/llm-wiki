---
title: 6. Keeping it honest
---

# 6. Keeping it honest

A wiki written by a language model can drift: a notation slowly forked, a claim promoted beyond its evidence, a
disagreement quietly resolved in favour of the last paper read, a DOI that looks right and is not. This chapter shows
the checks that stop each of these, and which of them you run.

## Deterministic lint, at every ingestion

```bash
python3 tools/lint_okf.py <bundle>/wiki
make check     # every bundle, plus the bundle registry
```

The linter enforces the format and the repository law. It fails on:

- a page without parseable frontmatter or `type`; a reserved file (`index.md`, `log.md`, `bibliography.md`) with
  frontmatter it must not have;
- a missing or invalid `status`; a Source page without `resource` or `source_kind`; a `type` that does not match the
  page's folder; a filename that is not kebab-case; a `timestamp` that is not ISO 8601;
- a broken link: stricter than OKF, a dead link is an error;
- a page missing from its folder index, or listed twice, or with an index line that differs from its frontmatter
  `description`;
- math written as `\(...\)` or `\[...\]`, or unbalanced `$`;
- a `bibliography.bib` that does not parse or validate, or a `bibliography.md` out of sync with it.

Orphan pages (no incoming link from a concept or Source page; links from `index.md`, `log.md` and
`bibliography.md` do not count) are reported as warnings. A Source page tagged `context` is exempt (D24): a bundle
uses that tag for sources it ingests but, by its own scope rule, never cites from a concept page, such as the
off-domain journal papers of `plasma-propulsion-simulation`. The tag hides the warning, so it never goes on an
in-scope page. An ingestion is not staged until the lint passes.

## Deep lint, every ten ingestions or every chunk

The linter checks form; it cannot read. Every ten ingestions (in chunked ingestion, with every chunk), and before any milestone you declare, Claude runs a
**deep lint**: it re-reads pages against the notation registry and against each other, and looks for:

- **notation drift**: a symbol used with two meanings, or two symbols for one thing;
- **stale contradictions**: entries a newer source has explicitly superseded, or that were recorded inaccurately;
- **tag synonyms**: two tags for one idea (`dg` and `discontinuous-galerkin`);
- claims that outgrew their evidence, missing cross-links, index descriptions that no longer match.

Findings and fixes go into `log.md`, so you can see what changed and why.

::: tip Prompt
Run a deep lint on `<bundle>`.
:::

Narrower audits are useful between deep lints:

::: tip Prompt
Audit the Contradictions blocks in `<bundle>`: has any been superseded by a later ingestion?
:::

::: tip Prompt
Audit the notation maps of the last five Source pages against the original papers.
:::

::: tip Prompt
Recurate the reading guide of `<bundle>`: it no longer matches the bundle.
:::

## Contradictions are content

When sources disagree, the page records both sides under `## Contradictions`, each attributed and cited. Three
rules:

1. **Recency never wins.** A newer paper does not overwrite an older one by being newer.
2. **An entry closes only** when a source explicitly supersedes another (and the page says which and where), or when
   you close it by decision. A decision closure is recorded as yours, with `status: hypothesis` attribution: it is
   your judgment, not the literature's.
3. **Nothing is silently overwritten.** A closed entry stays on the page, with the losing claim.

[Chapter 1](/manual/tutorial/01-reading) walks through one closed and one open entry. To close one yourself:

::: tip Prompt
Close the contradiction on `<page>` by my decision: I consider `<side>` settled because `<reason>`. Record it as a
fiat closure.
:::

## Status is claim kind, not trust

Every concept page carries `status: established` (a published, peer-reviewed result) or `status: hypothesis` (a claim
a published source could still overturn). Sources are trusted as they enter; there is no trust field. Two
consequences:

- your own notes, conjectures and unpublished results enter as `hypothesis`, and stay so until a published source
  establishes them;
- records of other projects (their issues, docs, run data) can be ingested only as frozen captures under
  `raw/docs/<slug>/`, as hypotheses; they can never promote a claim to `established` or close a contradiction on
  their own.

## Identity is verified, not assumed

A filename, an embedded PDF metadata field or an arXiv record can name the wrong paper. Metadata on Source pages
comes from page 1 of the source itself, and a DOI is written only when it is printed or verified against Crossref.
When no permanent identifier exists, the Source page uses the best stable URL and says so. A DOI is never invented.

## Your part

The checks above run without you. What only you can do:

- **spot-check** a Source page against its PDF now and then, especially on scanned sources;
- **challenge** a claim that reads stronger than its citation;
- **decide** scope questions and fiat closures, and record them;
- **read the log** before committing: every change is listed there.

**Next:** [7. Publishing](/manual/tutorial/07-publishing).
