---
title: 2. Asking Claude
---

# 2. Asking Claude

The bundles are plain Markdown, so any reader works. With [Claude Code](https://claude.com/claude-code) you can also
ask questions in plain language, from any directory, and get answers that cite the wiki's pages. This chapter
installs the **consultation skill** that does it.

## Install the skill

The skill lives in the repository at `skills/llm-wiki/SKILL.md`. Install it one of two ways.

**As a Claude Code plugin** (no clone needed). Inside Claude Code 2.1.275 or later:

```text
/plugin install llm-wiki --marketplace szaghi/llm-wiki
```

With older versions, add the marketplace first, then install:

```text
/plugin marketplace add szaghi/llm-wiki
/plugin install llm-wiki@llm-wiki
```

From a shell, the two steps are `claude plugin marketplace add szaghi/llm-wiki` and
`claude plugin install llm-wiki@llm-wiki`. The plugin installs a snapshot of the whole repository, bundles included,
into Claude Code's plugin cache. To pick up new content later:

```bash
claude plugin marketplace update llm-wiki
claude plugin update llm-wiki@llm-wiki
```

then run `/reload-plugins` in Claude Code.

**From a clone** (reads your working copy, so it is always current):

```bash
git clone https://github.com/szaghi/llm-wiki.git
cd llm-wiki
ln -s "$PWD/skills/llm-wiki" ~/.claude/skills/llm-wiki
```

Either way, the skill triggers on its own when a question falls in a bundle's domain: its description lists every
bundle's keywords, generated from the bundles themselves. You can also invoke it by name: `/llm-wiki:llm-wiki` when
installed as a plugin, `/llm-wiki` when symlinked.

## Ask

Open Claude Code in any directory and ask. Some questions the current bundles can answer:

::: tip Prompt
Is fifth-order WENO-JS fifth order at smooth extrema? What does the wiki say fixes it?
:::

::: tip Prompt
What do the sources disagree on about projection versus constrained transport for div B = 0?
:::

::: tip Prompt
How do Athena++ and AthenaK differ in their AMR and GPU design, according to the wiki?
:::

::: tip Prompt
Which benchmarks does the wiki use to test positivity-preserving limiters?
:::

## What a good answer looks like

The skill follows a fixed protocol:

1. **It enters at the catalog.** It reads the bundle's root `index.md` and follows links, the way
   [chapter 1](/manual/tutorial/01-reading) does by hand; for a symbol, tag or alias it searches the bundle's files.
2. **It keeps the bundle's notation.** Formulas in the answer use the symbols of the bundle's notation registry.
3. **It respects status.** A claim from a `status: hypothesis` page is reported as a hypothesis, never as
   literature fact.
4. **It cites pages.** The answer names the concept pages it used and, for provenance, the Source pages behind them,
   which carry DOIs.
5. **It says when the wiki is silent.** Compilation is incremental, so a missing page is not proof of a missing
   literature. When the wiki lacks the answer, Claude says so explicitly and labels whatever it adds from general
   knowledge as such.
6. **It reads only.** Consultation never edits a bundle. A gap worth filling becomes a suggestion for an ingestion,
   done in the repository (chapters 3 and 4).

Hold answers to this standard. An answer that cites no page did not come from the wiki.

## Ambient and resident mode

| Mode | Where Claude runs | Use it for |
| --- | --- | --- |
| **Ambient** | any directory, through the skill | questions during daily work: a scheme's order, a benchmark's setup, what a paper claims |
| **Resident** | inside the repository clone | deep sessions, audits, and all ingestion: the repository's `CLAUDE.md` loads as law |

In resident mode you can ask the same questions directly, without the skill; that is also where Claude writes to the
wiki (from [chapter 3](/manual/tutorial/03-new-bundle) on).

## Without Claude

Nothing in a bundle needs Claude to be read:

- **any editor**: each bundle is `<bundle>/wiki/`, Markdown with YAML frontmatter; start at `index.md`;
- **Obsidian**: open `<bundle>/wiki/` as a vault. Links are ordinary Markdown links, so the graph view works;
- **grep**: tags, aliases and symbols are plain text. For example, every page that records a disagreement:

  ```bash
  grep -l '^## Contradictions' */wiki/*/*.md
  ```

  every page whose main claim is a hypothesis:

  ```bash
  grep -l '^status: hypothesis' */wiki/*/*.md
  ```

**Next:** to build a wiki of your own, [3. A bundle of your own](/manual/tutorial/03-new-bundle).
