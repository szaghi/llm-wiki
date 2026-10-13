---
title: 1. Reading a bundle
---

# 1. Reading a bundle

This chapter answers one real question from a bundle on this site, and on the way shows every part of a bundle you
will meet again. The question:

> Is fifth-order WENO really fifth order at a smooth extremum, and if not, what fixes it?

It lives in the bundle [High-order shock-capturing schemes](/bundles/high-order-capturing-schemes/).

## Enter at the reading guide

Every bundle opens on its **reading guide**, the bundle's root `index.md`: a short description of the domain and
the corpus, then a numbered reading order, from foundations to specialised topics. It is curated by the compiler,
not generated, and it is the entry point every session (human or Claude) reads first.

Open [the reading guide](/bundles/high-order-capturing-schemes/) and skim the numbered list. Item 3, on adaptive and
weighted stencils, leads to [WENO](/bundles/high-order-capturing-schemes/methods/weno); item 4 lists the family
after WENO-JS; item 6, *Where order is lost*, opens with the property this question is about:
[accuracy at critical points](/bundles/high-order-capturing-schemes/properties/accuracy-at-critical-points).

There are two other ways in:

- the sidebar lists the **folder indexes**: one per page type (definitions, methods, operators, results,
  properties, benchmarks, software, sources), each line a link and the page's one-sentence description;
- the search box (top bar) searches every page of every bundle, except the bibliographies.

## Read the metadata bar

Open [Accuracy at critical points](/bundles/high-order-capturing-schemes/properties/accuracy-at-critical-points).
Above the title is a bar with:

- the **bundle** the page belongs to;
- the **type** (`Property` here): one of eight, and the folder the page lives in. The
  [page types reference](/reference/page-types) lists them;
- the **status**, either `established` (a published, peer-reviewed result) or `hypothesis` (a claim a published
  source could still overturn, including the author's own conjectures). Status says what kind of claim the page
  makes, not how much to trust it;
- the **tags**, the bundle's own vocabulary;
- the description in italics: the one sentence that also appears in the folder index.

## Follow the claims to their sources

The page lists, family by family, what each source claims about accuracy at critical points. Every claim carries
a link to a **Source page**, one per ingested paper, book or note. Follow
[Henrick, Aslam & Powers (2005)](/bundles/high-order-capturing-schemes/sources/henrick-2005).

A Source page has:

- the bibliographic record in the metadata bar: authors, year, venue, and the DOI as a link. The note *local copy
  not distributed* means the compiler read a local PDF that this repository does not ship; the DOI takes you to the
  publisher;
- a summary and numbered **key claims**, with section and equation numbers, so you can check them in the paper;
- a **Notation map**: a table translating the paper's own symbols into the bundle's. Henrick et al. write
  $\epsilon$ for the weight regularization and $p$ for its exponent; the bundle writes $\varepsilon$ and $q$;
- the list of pages the ingestion created or updated, and the citation with how the paper was read.

## Use the notation registry

Concept pages never use a paper's own symbols. Each bundle has one normative symbol table, the
[notation registry](/bundles/high-order-capturing-schemes/notation), and every formula on every concept page uses
it. When a symbol on a page is unclear, look it up there, not in the paper. This is what lets fifty papers written
in fifty notations be read as one text.

## Read a contradiction

Back on [Accuracy at critical points](/bundles/high-order-capturing-schemes/properties/accuracy-at-critical-points),
scroll to **Contradictions**. A contradiction entry records a disagreement between sources, with both sides cited.
Here:

- Jiang & Shu (1996) state that their weights keep fifth order at critical points;
- Henrick et al. (2005) show that WENO5 drops to third order where $f' = 0$ and $f''' \neq 0$, and explain why
  the original tests missed it;
- the entry is **closed**, because Henrick et al. explicitly supersede the earlier claim, and two later sources
  confirm it. The entry also records Shu's later position, without reopening it.

That is the answer to the question: WENO5-JS is third order at such points (first-order critical points),
[mapped WENO](/bundles/high-order-capturing-schemes/methods/mapped-weno) restores fifth order there, and
[WENO-Z](/bundles/high-order-capturing-schemes/methods/weno-z) reaches fourth or fifth order depending on its
exponent $q$.

Two rules make contradictions trustworthy. A newer source does not win because it is newer: an entry closes only
when a source explicitly supersedes another, or when the human closes it by decision, recorded as such. And nothing
is silently overwritten: the losing claim stays on the page, attributed. For an entry that is still open, see
[Slowly moving shock anomaly](/bundles/high-order-capturing-schemes/definitions/slowly-moving-shock-anomaly): its
sources disagree on whether the anomaly depends on the Riemann solver.

## Look at the bibliography

The [bibliography](/bundles/high-order-capturing-schemes/bibliography) is the bundle's **citation record**: every
work cited by any ingested source, whether ingested or not. It has two parts:

- **Ingested sources**, each linked to its Source page;
- **Cited, not ingested**, sorted by how many ingested sources cite each work. The top of this list is the
  **frontier**: the papers the corpus keeps citing but does not yet contain. It is a reading list derived from the
  literature itself.

The `.bib` file behind it can be downloaded from the bibliography page. [Chapter 5](/manual/tutorial/05-citations)
explains how it is built.

## Navigate visually

Two views show the structure instead of the text:

- the [page graph](/bundles/high-order-capturing-schemes/graph) of a bundle draws every page as a node and every
  link as an edge, coloured by type. Type `critical` in its search box to find this chapter's page, hover it to see
  its neighbours, click to open it. Turn on *Source* to see which papers each concept rests on;
- the [bundle map](/bundles/) draws the bundles and what they share: works cited by both, papers ingested in both,
  and concepts with the same name. Click an edge to list them, and to cross from one bundle to another where they
  meet. Bundles never link to each other in their content; the map computes these bridges when the site is built.

## What you have seen

| Part | Where |
| --- | --- |
| Reading guide | the bundle's root page |
| Folder indexes | sidebar, one per page type |
| Metadata bar: type, status, tags | top of every wiki page |
| Source page and notation map | `sources/`, one per ingested work |
| Notation registry | `notation`, normative for every concept page |
| Contradictions | a section on concept pages where sources disagree |
| Bibliography and frontier | `bibliography` |
| Page graph and bundle map | `graph`, and [Bundles](/bundles/) |

**Next:** [2. Asking Claude](/manual/tutorial/02-consulting), to get the same answers by asking a question.
