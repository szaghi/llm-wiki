---
title: Bundles
aside: false
---

# Bundles

A **bundle** is a self-contained wiki on one research domain: its own sources, concept pages, notation registry and
citation record. Bundles are independent by law: no page of one bundle links to a page of another, and a claim in one
bundle never rests on another bundle's pages. Each card below opens the bundle's reading guide, its interactive page
graph, its notation registry and its bibliography.

Every number on this page is counted from the wiki files when the site is built (`tools/bundles.py`), so it cannot
drift from the content.

<BundleCards />

## The bundle map

The bundles do not link to one another, but they overlap: they cite the same papers, a few papers are compiled in
more than one bundle, and some subjects (constrained transport, the Orszag–Tang vortex, AMR) have a page in each
domain that uses them. The map computes these overlaps from the files and lets you cross from one bundle to another
where they meet.

<BundleMap />

## Reading the numbers

| Number | Meaning |
| --- | --- |
| Sources | Source pages: the papers, books, notes and web pages compiled into the bundle, one page each |
| Concept pages | Definitions, methods, operators, results, properties, benchmarks and software pages |
| Cited works | Entries of the bundle's citation record: every work any ingested source cites, ingested or not |
| Frontier | Cited works not yet ingested: the bundle's own reading list, ranked in its bibliography by how often they are cited |
| Contested pages | Concept pages with a `Contradictions` section, where sources disagree and the page records both sides |
| Hypotheses | Concept pages whose main claim is not established literature (`status: hypothesis`) |
