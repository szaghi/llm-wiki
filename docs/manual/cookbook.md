---
title: Cookbook
---

# Cookbook

Short answers to "how do I ...?". Each recipe gives the prompt to type in Claude Code or the command to run. Commands
run from the repository root. Replace `<bundle>` with a bundle directory name, such as `div-free-amr`. The
[reference](/reference/page-types) has the details, and the [tutorial](/manual/) walks through the same steps in
order.

Prompts are what you type in a Claude Code session. For building recipes, the session runs inside the repository, so
it loads the constitution (`CLAUDE.md`). For consulting recipes, it can run in any directory where the consultation
skill is installed.

[[toc]]

## Consulting

### Find what the wiki says about a subject

On the site, start at the bundle's reading guide (`/bundles/<bundle>/`), or type the subject in the search box. With
Claude, ask the question directly:

::: tip Prompt
What does the wiki say about the accuracy of WENO-Z at critical points? Cite the pages.
:::

The answer cites concept pages and the Source pages they rest on. If the wiki has no page on the subject, the skill
says so explicitly before it falls back on anything else.

### Install the consultation skill

As a Claude Code plugin, from any directory:

```text
/plugin marketplace add szaghi/llm-wiki
/plugin install llm-wiki@llm-wiki
```

You can then call it explicitly with `/llm-wiki:llm-wiki`. You can also install it from a clone, as a personal skill
that is called with `/llm-wiki`:

```bash
ln -s "$PWD/skills/llm-wiki" ~/.claude/skills/llm-wiki
```

### Update the plugin to the latest bundles

```bash
claude plugin marketplace update llm-wiki
claude plugin update llm-wiki@llm-wiki
```

Then run `/reload-plugins` in the running session. A symlinked clone is updated with `git pull`.

### List every hypothesis page

A hypothesis page is a concept page whose main claim a published source could still overturn (`status: hypothesis`).
Report it as a hypothesis, never as literature fact.

```bash
grep -rl '^status: hypothesis' */wiki
```

### List the contested pages

A contested page has a `## Contradictions` section: sources disagree, and the page records both sides with citations.

```bash
grep -rl '^## Contradictions' <bundle>/wiki
```

To read every entry with some context:

```bash
grep -rn -A6 '^## Contradictions' <bundle>/wiki
```

Each entry says whether it is open or closed. A closed entry names what closed it: either a superseding source, or a
human decision recorded as one.

### Find the meaning of a symbol

The bundle's notation registry is normative: every concept page writes mathematics with its symbols. Search it:

```bash
grep -n 'P_D' <bundle>/wiki/notation.md
```

To see how each paper's own symbols were translated, search the `# Notation map` sections of the Source pages:

```bash
grep -rn -A15 '^# Notation map' <bundle>/wiki/sources | grep 'P_D'
```

### Trace a claim to its source

Every claim on a concept page carries a link to a Source page. The Source page records the identifier (`resource`: a
DOI, an arXiv id or a URL), the authors, the venue and the version that was read. It also lists, section by section,
what the source claims. On the site, the metadata bar at the top of a Source page links the DOI.

The PDFs themselves are not distributed. The `local_file` field names the compiler's own copy, and the DOI is how you
get yours.

### Find which ingested sources cite a work

The bibliography's `citedby` field lists the ingested sources whose reference lists cite the work:

```bash
grep -A20 '{berger-colella-1989,$' <bundle>/wiki/bibliography.bib | grep -m1 citedby
```

On the site, the bundle's bibliography page shows the same list after each entry ("Cited by").

### Read the ingestion frontier

The frontier is the works the ingested sources cite but the bundle has not ingested. The generated bibliography sorts
them by how many ingested sources cite them, so the top of the list is the bundle's own reading list:

```bash
sed -n '/^## Cited, not ingested/,$p' <bundle>/wiki/bibliography.md | head -30
```

### List the sources whose reference lists are not merged yet

```bash
python3 tools/bib_to_md.py <bundle>/wiki --pending
```

The command prints one slug per line on standard output and the count on standard error.

### Use a bundle in Obsidian

Open `<bundle>/wiki/` as a vault. The pages are plain Markdown with YAML frontmatter. Their links are relative to the
bundle root, which is the vault root, so the graph view and backlinks work. Obsidian renders `$...$` math.

### Ask across bundles

The consultation skill reads every bundle whose domain matches the question:

::: tip Prompt
Compare how the div-free-amr and astrophysical-simulation-codes bundles describe constrained transport on AMR
hierarchies. Cite both.
:::

Bundles never link to each other. To see where they overlap (shared cited works, sources compiled in both, pages
with the same name), open the [bundle map](/bundles/).

## Building

### Scaffold a new bundle

Run Claude Code in the repository and describe the domain and the corpus:

::: tip Prompt
Create a new bundle named `turbulence-models` for RANS and LES closure models. The primary corpus lives at
`~/papers/mosaic/turbulence-models/`. Seed the notation registry with the usual Reynolds-averaging conventions.
:::

Claude writes the bundle law (`<bundle>/CLAUDE.md`), the bundle card (`<bundle>/bundle.toml`), `raw/` and the
`wiki/` skeleton (root `index.md`, `log.md`, `notation.md`, one folder per type). It then lints and stages. You
review and commit:

```bash
git commit -m "docs: scaffold turbulence-models bundle"
```

### Ingest a PDF from the archive

::: tip Prompt
Ingest ~/papers/mosaic/&lt;bundle&gt;/2008-JCP-Mittal-101016jjcp200801028.pdf into &lt;bundle&gt;.
:::

The ingestion is atomic. Claude reads the whole source and creates or merges concept pages. It writes the Source page
with its notation map and merges the reference list into `bibliography.bib`. Then it appends to `log.md`, updates
the indexes, lints and stages everything. It ends by printing the commit message, for example
`docs(<bundle>): ingest mittal-2008`. You commit.

### Ingest a paper by DOI

::: tip Prompt
Ingest doi:10.1016/j.jcp.2008.01.028 into &lt;bundle&gt;.
:::

Claude needs the full text: it asks you for the PDF, or fetches an open copy you approve. It checks the identity of
the file on page 1 against the DOI before writing anything.

### Ingest a web page

::: tip Prompt
Ingest https://example.org/post into &lt;bundle&gt;. Capture it to raw/.
:::

Web pages rot, so the page is first captured as a Markdown snapshot under `<bundle>/raw/web/`. The Source page then
points at both the URL and the capture.

### Ingest your own notes

::: tip Prompt
Ingest my notes at ~/notes/seam-divergence.md into &lt;bundle&gt;. These are working hypotheses, mark them as such.
:::

Claims that originate in your notes get `status: hypothesis`. Notes from a sibling project are captured frozen under
`raw/docs/<slug>/`. They can neither promote a claim to `established` nor close a contradiction (D12 amendment).

### Ingest a book as a scoped read

::: tip Prompt
Ingest ~/papers/mosaic/&lt;bundle&gt;/toro-riemann-solvers.pdf into &lt;bundle&gt; as a scoped read: chapters 4 to 10 in depth,
record the coverage.
:::

The Source page records which chapters were read, and the reference extraction is limited to them.

### Discard an interrupted ingestion

An ingestion is complete and staged, or it is discarded. When a session stopped halfway (unstaged changes), discard
the changes and start the source again:

```bash
git status                 # staged = complete, awaiting your commit; unstaged = aborted
git checkout -- . && git clean -fd <bundle>/wiki
```

`git clean` deletes untracked files. Run `git clean -n` first to see what it would remove.

### Extend the notation registry

A concept page may only use registry symbols. When a new operator family appears, the registry is extended first:

::: tip Prompt
Extend the &lt;bundle&gt; notation registry with a symbol for the coarse-fine flux correction, log the extension, then
update the pages that need it.
:::

The new row goes into `notation.md`, with the date it was added, and `log.md` records the extension.

### Record a contradiction

Contradictions are recorded during ingestion, not resolved. To add one by hand:

::: tip Prompt
On &lt;bundle&gt;/wiki/methods/projection-method.md, record as a contradiction that Balsara & Kim (2004) find projection
unsuitable for turbulence, against Tóth (2000). Cite both sides.
:::

The entry goes under `## Contradictions`, attributed, with both sides cited. A more recent source does not win by
being more recent.

### Close a contradiction by fiat

A contradiction closes only when a source explicitly supersedes the other (an erratum, a corrected proof), or when
you decide:

::: tip Prompt
Close the flat-extremum contradiction on the monotonicity-preserving limiter page by my decision, in favour of
Balsara & Shu. Record it as a fiat closure.
:::

The entry stays on the page, marked as closed by human fiat, with the date. The resolution is attributed as
`status: hypothesis`: it is your judgement, not literature. For an example, see the
[MP limiter page](/bundles/high-order-capturing-schemes/methods/monotonicity-preserving-limiter).

### Split a page

A page splits when it collects sub-variants that contradict each other. The split boundary is where the contradiction
lives:

::: tip Prompt
The &lt;bundle&gt; page on approximate Riemann solvers now mixes HLL-family claims that contradict each other. Split it
where the contradiction lives, and keep every citation and every incoming link working.
:::

### Merge two pages on the same concept

::: tip Prompt
methods/glm-cleaning.md and methods/hyperbolic-divergence-cleaning.md in &lt;bundle&gt; describe the same method. Merge them
into one page, move the aliases, rewrite every link and fix the indexes.
:::

The lint fails if a link or an index line is left behind.

## Citation record

### Merge one source's reference list by hand

For one new source, edit `bibliography.bib` directly. Add one entry per cited work, or add the source's slug to the
`citedby` of an entry that already exists. Keep the entries sorted by key. Then regenerate the view:

```bash
python3 tools/bib_to_md.py <bundle>/wiki
```

Claude does this as step 5 of every ingestion.

### Backfill many reference lists at once

For many sources whose reference lists were never merged, use the batched merger. Extract each list into
`frag-<slug>.bib` in a scratch directory. Write a resolutions module that defines at least `ORDER`. Then iterate until
the report shows `FLAGS: 0`:

```bash
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions r.py --report
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions r.py --write
python3 tools/bib_to_md.py <bundle>/wiki
python3 tools/lint_okf.py <bundle>/wiki
```

`--write` refuses while any flag is open. The [bibliography reference](/reference/bibliography#the-batched-merger)
explains each flag and resolution table.

### Sweep for duplicates after the last batch

The same work cited under two spellings of the first author lands under two keys, and no per-batch check can see it.
After the final batch, run the whole-corpus sweep:

```bash
python3 tools/bib_merge.py <bundle>/wiki --dupes
```

Review each `CROSS-STEM` group. If it is the same work, merge the two entries and take the union of their `citedby`.
If they are distinct works, leave them alone.

### Regenerate or check the bibliography view

```bash
python3 tools/bib_to_md.py <bundle>/wiki            # rewrite bibliography.md
python3 tools/bib_to_md.py <bundle>/wiki --check    # exit 1 if it is out of sync
```

Never edit `bibliography.md` by hand. The lint fails when it differs from what the `.bib` generates.

## Quality

### Lint a bundle

```bash
python3 tools/lint_okf.py <bundle>/wiki
make check        # every bundle, plus the bundle registry
```

A lint error blocks the commit. Orphan pages and unmerged reference lists are warnings; Source pages tagged
`context` (out of the bundle's scope, D24) raise no orphan warning.

### Run a deep lint

The deterministic lint cannot judge notation drift, stale contradictions or tag synonyms. A deep lint is an LLM audit,
due every 10 ingestions, or with every chunk in chunked ingestion (whole-bundle every 50):

::: tip Prompt
Run a deep lint on &lt;bundle&gt;.
:::

The findings are recorded in the bundle's `log.md`, and the fixes are applied in the same pass, where you can see
them.

### Spot-check the notation maps

::: tip Prompt
Audit the notation maps of the last five Source pages of &lt;bundle&gt; against the original PDFs.
:::

### Audit the contradictions

::: tip Prompt
Audit the Contradictions sections of &lt;bundle&gt;: has a later ingestion superseded any of them?
:::

### See what is left to ingest

```bash
tools/worklist.sh <bundle>
```

The script lists the PDFs of the bundle's archive that no Source page names. The archive is the `corpus` key of
`<bundle>/bundle.toml`, or `~/papers/mosaic/<bundle>/` without it. The list is derived, so it cannot go stale.

## Site

### Preview the site locally

```bash
make docs-dev
```

The target runs `npm install` in `docs/`, regenerates the bundle pages (`tools/site_sync.py`) and starts the
VitePress dev server. Node 20 or newer is required.

### Build the site

```bash
make docs
```

The output is in `docs/.vitepress/dist/`. A dead link fails the build.

### Add a new bundle to the site

You don't need to. Every top-level directory with a `bundle.toml` and a `wiki/index.md` is a bundle: the next build
gives it pages, a page graph, a sidebar, a navigation entry and a place on the [bundle map](/bundles/).

### Update the bundle list

The bundle tables in `README.md` and in the consultation skill are generated from the bundle cards and the wiki
files:

```bash
make registry     # python3 tools/bundles.py --write
```

CI runs `python3 tools/bundles.py --check` and fails while the tables are stale. Edit a bundle's title, summary or
keywords in its `bundle.toml`, never in the generated tables.

### Why a formula shows in red

The site renders math with KaTeX when it builds. A formula KaTeX cannot parse is shown in red instead of failing the
build. Since the wiki's math law is KaTeX syntax, red math is a defect in the wiki page: fix the page, not the site.
To list the affected pages after a build:

```bash
grep -rl 'katex-error' docs/.vitepress/dist --include='*.html'
```

### Deploy the site

Push to `main`. The `docs.yml` workflow builds the site and publishes it on GitHub Pages at
<https://szaghi.github.io/llm-wiki/>.
