---
layout: home

hero:
  name: llm-wiki
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
  - icon: 🧠
    title: Compiled, not retrieved
    details: "Each source is read once, in full, and merged into concept pages. Questions are answered by navigating the result, not by searching raw text chunks at every query."
    link: /guide/
    linkText: Introduction
  - icon: 🔣
    title: One notation per field
    details: "A normative symbol registry per bundle. Concept pages use only its symbols; every Source page records how the paper's own symbols translate."
    link: /guide/concepts#notation
    linkText: Notation registry and maps
  - icon: ⚖️
    title: Contradictions are content
    details: "When sources disagree, the page records both sides, attributed and cited. A newer paper does not win by being newer, and nothing is silently overwritten."
    link: /guide/concepts#contradictions
    linkText: How disagreements are kept
  - icon: 🏷️
    title: Claim kind on every page
    details: "status: established marks published results; status: hypothesis marks claims a published source could still overturn. The wiki never passes a conjecture off as literature."
    link: /guide/concepts#claim-kind
    linkText: Status
  - icon: 📚
    title: A complete citation record
    details: "Ingesting a paper means reading its reference list too. Every cited work enters the bundle's bibliography with the sources that cite it: the citation graph and the reading frontier come for free."
    link: /guide/concepts#citation-record
    linkText: Citation record
  - icon: 🕸️
    title: Page graphs and a bundle map
    details: "An interactive graph of every bundle's pages and links, and a map of what the bundles share: cited works, papers compiled twice, related concepts."
    link: /bundles/
    linkText: Bundle map
  - icon: 💬
    title: Ask Claude, get cited answers
    details: "A Claude Code skill consults the bundles from any directory: it navigates from the reading guide, respects claim kind and cites the pages its answer rests on."
    link: /guide/getting-started#ask-claude
    linkText: Install the skill
  - icon: 🛠️
    title: Build your own bundle
    details: "The law, the linter and the tools are domain-agnostic. Point Claude Code at a folder of papers and compile a wiki on your own field."
    link: /manual/tutorial/03-new-bundle
    linkText: A bundle of your own
---

## The bundles

<BundleCards />
