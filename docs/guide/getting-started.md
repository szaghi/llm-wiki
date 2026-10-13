---
title: Getting started
---

# Getting started

There are three ways into the bundles. None of them requires installing anything for reading; building and
compiling need the tools listed at the end.

## 1. Browse this site

Start at the [bundle list](/bundles/). Each bundle opens on its **reading guide**: the bundle's root index, ordered by
conceptual importance rather than alphabetically. From there:

- the **notation registry** (`/bundles/<bundle>/notation`) defines every symbol the concept pages use;
- the **page graph** (`/bundles/<bundle>/graph`) shows every page and link of the bundle, coloured by page type;
- the **folder indexes** (Methods, Benchmarks, Sources, …) list every page of one type with its one-line description;
- the **bibliography** lists every cited work, ingested or not, with the sources that cite it;
- the **search box** (top bar) searches every page of every bundle, except the bibliographies.

Every wiki page opens with a metadata bar: its bundle, its type, its status (*established* or *hypothesis*) and its
tags. A Source page also shows authors, year, venue and a link to the DOI or URL. The
[bundle map](/bundles/#the-bundle-map) shows what the bundles share and lets you cross from one to another.

## 2. Clone and read the Markdown

The bundles are plain files. Clone the repository and read them with anything:

```bash
git clone https://github.com/szaghi/llm-wiki.git
cd llm-wiki
ls */wiki/index.md          # one reading guide per bundle
```

- **Any Markdown editor.** Links are absolute *from the bundle root*: `/methods/weno.md` in a page of
  `high-order-capturing-schemes` means `high-order-capturing-schemes/wiki/methods/weno.md`.
- **Obsidian.** Open `<bundle>/wiki/` (not the repository root) as a vault; the graph view works because links are
  plain Markdown links. Math renders with Obsidian's built-in MathJax.
- **grep.** Navigation is the query engine, and grep is its fastest form:

```bash
grep -rl "status: hypothesis" */wiki                  # every conjecture
grep -rl "^## Contradictions" */wiki                  # every page where sources disagree
grep -rn "tags:.*weno" high-order-capturing-schemes/wiki
```

The [cookbook](/manual/cookbook) has many more such recipes.

## 3. Ask Claude {#ask-claude}

The repository ships a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill, `llm-wiki`, that consults
the bundles from any directory. It enters at a bundle's reading guide, follows links, respects claim kind (it reports a
hypothesis as a hypothesis) and cites the pages its answer rests on. It never edits the bundles. Install it one of two
ways.

**As a plugin** (no clone needed). In Claude Code 2.1.275 or later:

```text
/plugin install llm-wiki --marketplace szaghi/llm-wiki
```

In older versions, add the marketplace first, then install:

```text
/plugin marketplace add szaghi/llm-wiki
/plugin install llm-wiki@llm-wiki
```

or from a shell:

```bash
claude plugin marketplace add szaghi/llm-wiki
claude plugin install llm-wiki@llm-wiki
```

The plugin installs a snapshot of the whole repository, bundles included, into Claude Code's plugin cache. To get
newer bundles later:

```bash
claude plugin marketplace update llm-wiki
claude plugin update llm-wiki@llm-wiki
```

then run `/reload-plugins` in Claude Code. As a plugin, the skill is invoked as `/llm-wiki:llm-wiki`.

**From a clone** (reads your live copy, so `git pull` is the update):

```bash
cd llm-wiki
ln -s "$PWD/skills/llm-wiki" ~/.claude/skills/llm-wiki
```

As a personal skill it is invoked as `/llm-wiki`.

Either way, you rarely need to invoke it by name: the skill triggers on its own when a question falls in a bundle's
domain, or when you say "check the wiki". [Tutorial chapter 2](/manual/tutorial/02-consulting) shows a session.

## Requirements for building

Reading needs nothing. To run the tools, build the site or compile your own bundles you need:

| Tool | Used for |
| --- | --- |
| Python ≥ 3.11 with PyYAML | the linter, the bibliography tools, the bundle registry, the site generator |
| Node.js ≥ 20 | the documentation site (VitePress) |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | compiling: ingestion, audits, consultation |
| git | everything: the compiler stages, you commit |

The Makefile at the repository root is the entry point:

```bash
make dev        # create .venv and install the tools with their development extras
make check      # lint every bundle and check that the bundle registry is in sync
make test       # run the test suite
make docs-dev   # generate the bundle pages and serve this site locally with live reload
make docs       # build the site into docs/.vitepress/dist
```

Next: [How a bundle works](/guide/concepts), or go straight to the
[tutorial](/manual/tutorial/01-reading).
