<div align="center">

# llm-wiki

#### *Stefano's second brain — the curated knowledge his AI assistant actually runs on*

### Personal LLM-compiled knowledge bundles in the Open Knowledge Format

> Multi-modal sources go in — papers, books, theses, blog posts, personal notes, slides, code.
> A linted, cross-linked, contradiction-aware Markdown wiki comes out.
> No vector database, no embeddings, no retrieval lottery — the knowledge is **compiled once, navigated forever**.

[![OKF](https://img.shields.io/badge/OKF-v0.1-blue)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[![Bundles](https://img.shields.io/badge/bundles-1-blue)](#-bundles)
[![Lint](https://img.shields.io/badge/okf%20lint-passing-brightgreen)](tools/lint_okf.py)
[![Math](https://img.shields.io/badge/math-KaTeX-orange)](div-free-amr/wiki/notation.md)
[![Compiler](https://img.shields.io/badge/compiler-Claude-8A2BE2)](CLAUDE.md)
[![Format](https://img.shields.io/badge/format-markdown%20%2B%20YAML-lightgrey)](DECISIONS.md)

**[Constitution](CLAUDE.md)** · **[Decision record](DECISIONS.md)** · **[Bundles](#-bundles)** · **[Tutorial](#-tutorial)**

</div>

## 🧠 What this is

An implementation of the **LLM Wiki pattern**: instead of feeding raw documents to a
retrieval pipeline at every question (stateless, forgetful, blind to cross-document
contradictions), an LLM acts as a **stateful compiler** — it reads each source once,
*merges* its claims into a curated web of concept pages, records contradictions with
attribution, and keeps a normative notation registry so that hundreds of sources written
in as many dialects speak one mathematical language.

Sources are **multi-modal by design**: peer-reviewed papers, books and theses (scoped,
chapters-of-interest reads with coverage recorded), blog posts and web pages (captured as
snapshots against link rot), personal notes, slides, reports, code. Every source is
personally reviewed by the human before ingestion — trust is a property of the ingestion
act, not a metadata field.

The on-disk format is the [Google Open Knowledge Format (OKF) v0.1][okf]: plain Markdown
files with YAML frontmatter, organized as a *Knowledge Bundle* — readable by any human,
any editor, any model, with no SDK and no build step. This repository extends stock OKF
with what a **scientific** knowledge base needs:

| Extension | What it does |
| --- | --- |
| KaTeX math, everywhere | `$...$` / `$$...$$` in every page; `\[...\]` is a lint error |
| Notation registry | one normative symbol table per bundle; concept pages *must* use it |
| Notation maps | every Source page records how the source's native symbols translate |
| `status: established \| hypothesis` | claim-kind on every page — the wiki always knows what is literature and what is conjecture |
| `## Contradictions` blocks | disagreements between sources are content, attributed and cited — recency never wins |
| Verified identifiers | DOIs checked against page 1 and Crossref; filenames are never trusted (several wrong ones caught already) |

## 🏛️ Architecture

Three layers, five rules.

| Layer | Contents | Who writes it |
| --- | --- | --- |
| **Layer 1 — sources** | managed archives (referenced in place) + `raw/` captures for anything without a durable home | nobody, ever — immutable |
| **Layer 2 — bundle** | the OKF wiki: concept pages, Source pages, notation registry, curated indexes, journal | the compiler (Claude) |
| **Layer 0 — law** | `CLAUDE.md` constitution + `DECISIONS.md` rationale + `tools/` | the human, via grilling sessions |

The load-bearing rules, in one breath: **Layer 1 is never written**; the compiler owns
Layer 2; every source is one atomic unit (*complete-and-stage or discard*); the compiler
**stages but never commits** (commits are the human's, GPG-signed); progress is *derived* —
a source is ingested iff its Source page exists, so no queue file can go stale — and
nothing load-bearing lives in conversation memory: any fresh session resumes from
`CLAUDE.md` + `git log` alone.

```text
llm-wiki/
├── CLAUDE.md            # the constitution — compiler law, auto-loaded every session
├── DECISIONS.md         # ADR-lite rationale for every rule
├── README.md            # you are here
├── tools/
│   ├── lint_okf.py      # OKF conformance + repo law + links + indexes + math syntax
│   └── worklist.sh      # derived worklist: corpus minus existing Source pages
└── <bundle>/            # one directory per knowledge bundle
    ├── CLAUDE.md        # bundle law: corpus path, domain notes, status
    ├── raw/             # captures only (web/, docs/) — archives stay where they live
    └── wiki/            # the OKF bundle root
        ├── index.md     # curated entry point with a reading guide
        ├── log.md       # append-only journal of every ingestion and audit
        ├── notation.md  # the normative symbol registry
        └── {definitions,methods,operators,properties,results,benchmarks,software,sources}/
```

## 📦 Bundles

| Bundle | Domain | Scale | Entry point |
| --- | --- | --- | --- |
| [`div-free-amr`](div-free-amr/wiki/index.md) | Discrete divergence constraints ($D_h B_h = 0$, incompressibility) across numerical discretizations — staggered/CT, mimetic, Whitney/FEEC, SBP, DEC — with particular depth on high-order methods and 2:1 AMR interfaces | dozens of multi-modal sources (1965–2025), ~100 pages, corpus complete | [reading guide](div-free-amr/wiki/index.md) · [log](div-free-amr/wiki/log.md) |

Future bundles are siblings: same constitution, same linter, same worklist — see the
[tutorial](#-tutorial) below.

## 🎓 Tutorial

Two actors throughout. **You** review sources, make decisions, and commit. **Claude**
(the compiler) reads, writes wiki pages, lints, and stages. The division is law
([CLAUDE.md](CLAUDE.md)), not etiquette.

| | You (the human) | Claude (the compiler) |
| --- | --- | --- |
| Sources | choose, review, vouch for | read fully (visually if scanned), never modify |
| Content | audit pages, challenge claims | create/merge pages, notation maps, contradictions |
| Quality | spot-check, request audits | deterministic lint every ingestion, deep lint every ~10 |
| Git | **commit** (GPG-signed) | stage + hand you the commit message |

### 1️⃣ Create a new bundle

Open Claude Code in `~/llm-wiki` (resident mode — the constitution auto-loads) and say:

```text
Create a new bundle named <name> for <one-sentence domain description>.
The primary corpus lives at <path-to-archive>. Seed the notation registry with <conventions, if any>.
```

Claude scaffolds `<name>/{CLAUDE.md, raw/, wiki/...}`, writes the bundle law, seeds
`notation.md` / `index.md` / `log.md`, lints, and stages. **You** review the scaffold and
commit:

```bash
cd ~/llm-wiki && git commit -m "docs: scaffold <name> bundle"
```

### 2️⃣ Populate it (bulk compilation)

Recommended: start with a **two-source pilot** (one clean source, one hard case — a
scanned PDF, a long book) and audit the resulting pages before bulk work. Prompts:

```text
Run a pilot ingestion on <bundle>: ingest <source A> and <source B>, then stop for my audit.
```

then, after your audit:

```text
Continue ingesting the <bundle> sources, foundations first. Stage after each source.
```

Claude works in tranches — each source atomically (read → extract → create-or-merge →
notation map → log → indexes → lint → stage) — and reports what entered the wiki, with
the prepared commit message. **You** commit after each tranche (or per source, if you
prefer fine-grained history). Check remaining work anytime:

```bash
./tools/worklist.sh <bundle>
```

### 3️⃣ Add a single new source to an existing bundle

Any modality. You reviewed it, so it is trusted; Claude will still verify its
*identity* (page-1 metadata, DOI against Crossref) because trust and identity are
different things. Prompts by source type:

```text
# a paper already in the archive
Ingest ~/papers/<archive>/<file>.pdf into <bundle>.

# a paper not yet downloaded — Claude will ask for or fetch the PDF as agreed
Ingest doi:10.xxxx/yyyy into <bundle>.

# a blog post / web page — captured to raw/web/ first, against link rot
Ingest https://example.org/post into <bundle>. Capture it to raw/.

# your own notes / slides / a report — claims that are yours get status: hypothesis
Ingest my notes at <path> into <bundle>. These are working hypotheses, mark them as such.

# a book or long thesis — scoped read
Ingest <path-to-book> into <bundle> as a scoped read: chapters <X–Y> in depth, record coverage.
```

In every case Claude ends at **staged + commit message**; you commit.

### 4️⃣ Periodic maintenance

The deterministic linter runs automatically at every ingestion, but you can invoke
everything on demand:

```text
# fast conformance check (also directly: python3 tools/lint_okf.py <bundle>/wiki)
Lint the <bundle> wiki.

# semantic audit — notation drift, tag synonyms, stale contradictions, orphans
Run a deep lint on <bundle>.

# targeted audits
Audit the Contradictions blocks in <bundle> — anything superseded by newer ingestions?
Audit the notation maps of the last five Source pages against the originals.
Recurate the root index of <bundle> — the reading guide is stale.
```

Deep lints are also mandatory by law every ~10 ingestions; findings land in the bundle's
`log.md` with fixes applied in the same pass.

### 5️⃣ Consult the second brain

| Mode | How |
| --- | --- |
| **Ambient** (daily work) | from *any* directory, ask a domain question or say `/llm-wiki` — the skill navigates from the bundle index, respects `status:`, and cites pages |
| **Resident** (deep sessions) | run Claude Code in `~/llm-wiki` and ask directly; ingestion and audits happen here |
| **Human** | open `<bundle>/wiki/` as an Obsidian vault (graph view works — links are plain Markdown), or just `grep` |

Consultation is read-only from outside the repo; gaps found while consulting become
ingestion suggestions, executed in resident mode.

### 6️⃣ Commit conventions

Conventional Commits, `docs(<bundle>): ingest <source-slug>` for ingestions; the compiler
prepares every message but **only you run `git commit`** — GPG-signed, no
`Co-authored-by` lines, ever.

## 👥 Authors

**[Stefano Zaghi](https://github.com/szaghi)** · stefano.zaghi@gmail.com
> *Chief Yak Shaver & Curator of Unread PDFs* — CFD researcher who downloaded a folder of papers "for a quick literature check," realized he'd need a second brain to hold them, and — being constitutionally incapable of using an existing tool when a new repository could be founded — commissioned one. Now the proud owner of a wiki that knows his own conjectures are conjectures.

**[Claude](https://claude.ai)** (Anthropic)
> *Stateful Compiler & Recovering DOI Fabricator* — AI second brain, responsible for reading every page of every scan (including the 1988 ones), translating dozens of notations into one, and being caught by its own linter more than once. Holds strong opinions about staggered grids it acquired approximately last Tuesday.

## 🙏 Lineage

The pattern follows Andrej Karpathy's *LLM Wiki* proposal; the on-disk format is
Google's [Open Knowledge Format v0.1][okf]. The scientific extensions (notation
registry, claim-kind status, contradiction protocol, verified identifiers) are this
repository's own — codified in [CLAUDE.md](CLAUDE.md) and argued for in
[DECISIONS.md](DECISIONS.md).

[okf]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
