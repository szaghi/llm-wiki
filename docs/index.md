---
layout: home

hero:
  name: llm-wiki
  image:
    light: /brand/logos/llm-wiki-logo.svg
    dark: /brand/logos/llm-wiki-logo-dark.svg
    alt: llm-wiki, the tree of the sciences in brush strokes
  text: Scientific literature, compiled into wikis
  tagline: "An LLM reads each paper once and merges what it says into a curated web of Markdown pages: one notation per field, every claim cited, every disagreement between sources recorded instead of overwritten."
  actions:
    - theme: brand
      text: Browse the bundles
      link: /bundles/
    - theme: alt
      text: Tutorial
      link: /manual/tutorial/01-reading
    - theme: alt
      text: Cookbook
      link: /manual/cookbook
    - theme: alt
      text: Start here
      link: /guide/
    - theme: alt
      text: View on GitHub
      link: https://github.com/szaghi/llm-wiki

features:
  - icon: { light: /brand/icons/light/compiled.svg, dark: /brand/icons/dark/compiled.svg, width: 24, height: 24 }
    title: Compiled, not retrieved
    details: "Each source is read once, in full, and merged into concept pages. Questions are answered by navigating the result, not by searching raw text chunks at every query."
    link: /guide/
    linkText: Introduction
  - icon: { light: /brand/icons/light/notation.svg, dark: /brand/icons/dark/notation.svg, width: 24, height: 24 }
    title: One notation per field
    details: "A normative symbol registry per bundle. Concept pages use only its symbols; every Source page records how the paper's own symbols translate."
    link: /guide/concepts#notation
    linkText: Notation registry and maps
  - icon: { light: /brand/icons/light/contradictions.svg, dark: /brand/icons/dark/contradictions.svg, width: 24, height: 24 }
    title: Contradictions are content
    details: "When sources disagree, the page records both sides, attributed and cited. A newer paper does not win by being newer, and nothing is silently overwritten."
    link: /guide/concepts#contradictions
    linkText: How disagreements are kept
  - icon: { light: /brand/icons/light/status.svg, dark: /brand/icons/dark/status.svg, width: 24, height: 24 }
    title: Claim kind on every page
    details: "status: established marks published results; status: hypothesis marks claims a published source could still overturn. The wiki never passes a conjecture off as literature."
    link: /guide/concepts#claim-kind
    linkText: Status
  - icon: { light: /brand/icons/light/citations.svg, dark: /brand/icons/dark/citations.svg, width: 24, height: 24 }
    title: A complete citation record
    details: "Ingesting a paper means reading its reference list too. Every cited work enters the bundle's bibliography with the sources that cite it: the citation graph and the reading frontier come for free."
    link: /guide/concepts#citation-record
    linkText: Citation record
  - icon: { light: /brand/icons/light/graph.svg, dark: /brand/icons/dark/graph.svg, width: 24, height: 24 }
    title: Page graphs and a bundle map
    details: "An interactive graph of every bundle's pages and links, and a map of what the bundles share: cited works, papers compiled twice, related concepts."
    link: /bundles/
    linkText: Bundle map
  - icon: { light: /brand/icons/light/ask.svg, dark: /brand/icons/dark/ask.svg, width: 24, height: 24 }
    title: Ask Claude, get cited answers
    details: "A Claude Code skill consults the bundles from any directory: it navigates from the reading guide, respects claim kind and cites the pages its answer rests on."
    link: /guide/getting-started#ask-claude
    linkText: Install the skill
  - icon: { light: /brand/icons/light/build.svg, dark: /brand/icons/dark/build.svg, width: 24, height: 24 }
    title: Build your own bundle
    details: "The law, the linter and the tools are domain-agnostic. Point Claude Code at a folder of papers and compile a wiki on your own field."
    link: /manual/tutorial/03-new-bundle
    linkText: A bundle of your own
---

## The bundles

<BundleCards />
