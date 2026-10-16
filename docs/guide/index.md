---
title: Introduction
---

# Introduction

llm-wiki is a set of **knowledge bundles**: wikis on research domains in computational physics, each compiled by an
LLM (Claude, through Claude Code) from a curated set of sources, papers above all. Each bundle has its own sources,
concept pages, symbol registry and citation record. The [bundle list](/bundles/) shows what exists today.

The repository holds two things that can be used separately:

- **the bundles**, which you can read on this site, in any Markdown editor or through Claude;
- **the machinery that builds them**: a written law for the compiler (`CLAUDE.md`), the rationale behind each rule
  (`DECISIONS.md`) and deterministic tools (a linter, a bibliography generator and merger, a bundle registry, this
  site's generator). None of it is specific to the current domains, so you can build bundles on your own field.

## Compiled, not retrieved

The common way to give an LLM a document collection is **retrieval-augmented generation** (RAG): split the documents
into chunks, embed them as vectors, and at every question retrieve the chunks most similar to it. Retrieval is
stateless: every question starts from raw chunks, so the model rediscovers the same connections each time, and it
cannot notice that two papers disagree unless both chunks happen to be retrieved together.

The **LLM Wiki** pattern, proposed by Andrej Karpathy, moves the work to ingestion time. The LLM acts as a
**stateful compiler**: it reads each source once, in full, and *merges* what the source says into a web of concept
pages that already holds everything read before. A claim that agrees with the wiki adds a citation; a claim that
extends it is integrated; a claim that contradicts it is recorded next to the opposing claim, both attributed. The
result is plain Markdown that a human or a model navigates from an index, following links.

| | Retrieval (RAG) | Compiled wiki |
| --- | --- | --- |
| State | none: rebuilt from chunks at every query | accumulated: each source merged into the pages |
| Disagreements between sources | invisible unless co-retrieved | recorded on the page, both sides cited |
| Notation | as many dialects as sources | one registry per bundle, translations recorded |
| Infrastructure | vector store, embedding model, retriever | files, a linter, git |
| Cost | cheap ingestion, cost at every query | expensive ingestion, near-free queries |
| Scale | millions of documents | hundreds of curated sources per bundle |

## The Open Knowledge Format

The on-disk format is Google's [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).
A bundle is a directory of Markdown files, each with a YAML frontmatter that declares its `type`, plus reserved
files: an `index.md` in every folder (the catalogue) and a `log.md` (the change history). Any editor, any model and
any script can read it; there is no SDK and no build step.

## What this repository adds for science

Stock OKF is a container. A scientific knowledge base needs more, and this repository's law adds it:

| Addition | What it does |
| --- | --- |
| Math everywhere | `$...$` and `$$...$$` in every page, KaTeX syntax, checked by the linter |
| Notation registry | one normative symbol table per bundle (`notation.md`); concept pages may use only its symbols |
| Notation maps | every Source page records how the source's own symbols translate to the registry |
| Claim kind | `status: established` or `status: hypothesis` on every concept page |
| Contradictions | disagreements between sources are kept in a `Contradictions` section, attributed and cited; recency never wins |
| Verified identity | metadata from the source's first page, DOIs checked against Crossref, never invented |
| Citation record | every work any ingested source cites, in `bibliography.bib`, with the sources that cite it |

[How a bundle works](/guide/concepts) explains each of these.

## Who it is for

- **Readers** of the existing bundles: researchers and students in numerical methods for fluid dynamics and plasmas
  (shock capturing, MHD, fusion and plasma-propulsion simulation, astrophysical and aerospace flows) and in the
  mathematical methods beneath them, who want a cited, cross-linked map of a literature, with its notation unified and
  its open questions marked.
- **Claude Code users** who want answers grounded in those bundles, with the pages they rest on cited.
- **Builders** who want to compile their own literature the same way.

## What it is not

- **Not a retrieval system.** There are no embeddings and no vector search: navigation is the query engine.
- **Not a substitute for the papers.** A page condenses what its sources say, in a unified notation, and says where.
  For a proof, a figure or a number that matters, follow the citation to the source.
- **Not a distribution of the sources.** The PDFs stay in the compiler's local archive and are not in the repository.
  A Source page names its source by DOI or URL; its local path is provenance only.
- **Not infallible.** The compiler is an LLM. The law, the linter and periodic audits catch a lot; the citations let
  you check the rest. A wrong page is a bug: see [Contributing](/project/contributing).

## Lineage

The pattern is Karpathy's *LLM Wiki* proposal; the format is Google's OKF v0.1. The scientific additions (notation
registry, claim kind, contradiction protocol, verified identifiers, citation record) are this repository's own,
written down in the [constitution](/reference/constitution) and argued for in the
[decision record](/reference/decisions).

Next: [Getting started](/guide/getting-started).
