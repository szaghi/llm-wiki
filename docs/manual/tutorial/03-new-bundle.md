---
title: 3. A bundle of your own
---

# 3. A bundle of your own

From this chapter on, you build. You will have Claude Code compile a wiki from your own sources, under the same law
as the bundles on this site. This chapter sets up the repository and scaffolds an empty bundle.

## Two actors

The work is split between you and Claude, and the split is law, not etiquette:

| | You | Claude (the compiler) |
| --- | --- | --- |
| Sources | choose, review, vouch for | read fully, never modify |
| Content | audit pages, challenge claims, decide | create and merge pages, notation maps, contradictions |
| Quality | spot-check, ask for audits | lint at every ingestion, deep lint every 10 |
| Git | **commit** | stage, and hand you the commit message |

Claude never runs `git commit`. Every change reaches history through you.

## Get the repository

Fork [szaghi/llm-wiki](https://github.com/szaghi/llm-wiki) on GitHub, or clone it directly:

```bash
git clone https://github.com/<you>/llm-wiki.git
cd llm-wiki
make dev     # creates .venv and installs the tools' dependencies (PyYAML, ruff, pytest)
make check   # lints every bundle and checks the bundle registry
```

`make check` must pass on a fresh clone. You need Python 3.11 or newer and git; Node 20 or newer only for the site
([chapter 7](/manual/tutorial/07-publishing)).

## What is generic, what is ours

| Path | What it is | Keep it? |
| --- | --- | --- |
| `CLAUDE.md` | the constitution: repository-wide law every session loads | yes; change it only through a recorded decision |
| `DECISIONS.md` | the rationale of every rule (D1, D2, ...) | yes; add your own decisions after ours |
| `tools/` | linter, bibliography tools, registry, site generator | yes |
| `docs/`, `skills/` | this site and the consultation skill | yes |
| `<bundle>/` (every top-level directory with a `bundle.toml`) | our bundles; `python3 tools/bundles.py` lists them | your choice |

The bundles are independent of each other and of the tools: you can keep them (to consult them next to yours) or
delete their directories. After deleting, run `make registry` so the README and the skill stop listing them.

Read `CLAUDE.md` once before you start. It is short, and it is what Claude will obey. The
[constitution page](/reference/constitution) renders it, and the [decision record](/reference/decisions) explains
each rule.

## Decide where your sources live

A bundle never stores its sources in git. **Layer 1** is the set of original sources: a folder of PDFs, a set of
captured web pages, your notes. It is read-only: Claude never modifies, renames or deletes a source. Two kinds:

- **an archive** you already keep, referenced in place: each Source page records the file in its `local_file`
  field. Name its path in the `corpus` key of `bundle.toml`, which `tools/worklist.sh` reads
  (see [chapter 4](/manual/tutorial/04-ingestion)); without the key the script assumes this repository's convention,
  one archive per bundle at `~/papers/mosaic/<bundle>/`;
- **captures**, for anything without a durable home (a web page, a loose document): written once into the bundle's
  `raw/web/` or `raw/docs/` and then frozen.

## Scaffold the bundle

Open Claude Code in the repository root. The constitution loads automatically. Ask:

::: tip Prompt
Create a new bundle named `<name>` for `<one-sentence domain description>`. The primary corpus lives at
`<path-to-archive>`. Seed the notation registry with `<conventions you want, if any>`.
:::

Use a kebab-case name (`turbulence-closures`, not `Turbulence Closures`). Claude creates:

```text
<name>/
├── CLAUDE.md          # bundle law: domain and scope, corpus location, bundle-specific conventions
├── bundle.toml        # bundle card: title, summary, keywords, optional corpus path
├── raw/
│   ├── web/           # captured web pages
│   └── docs/          # captured loose documents
└── wiki/              # the OKF bundle root
    ├── index.md       # reading guide (carries only okf_version in its frontmatter)
    ├── log.md         # append-only journal, newest first
    ├── notation.md    # the normative symbol registry
    └── definitions/ methods/ operators/ results/ properties/ benchmarks/ software/ sources/
                       # one folder per page type, each with its index.md
```

The `bibliography.bib` and its generated `bibliography.md` appear with the first ingested reference list. Claude
then lints the bundle, regenerates the registry, stages everything, and gives you a commit message.

## Review and commit

Check three things before committing:

1. **The scope** in `<name>/CLAUDE.md`. Every later ingestion is judged against it: what is in, what is out. Be
   explicit; a vague scope produces a vague wiki.
2. **The notation registry.** If your field has a dominant convention, have it seeded now. Changing a symbol later
   means touching every page that uses it.
3. **`bundle.toml`.** The `keywords` are what makes the consultation skill trigger on questions in your domain.

Then:

```bash
git commit -m "docs: scaffold <name> bundle"
```

**Next:** [4. The first ingestion](/manual/tutorial/04-ingestion).
