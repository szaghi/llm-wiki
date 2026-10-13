---
title: Tutorial
---

# Tutorial

The tutorial has two tracks. You can stop after the first.

| Track | Chapters | For you if | You need |
| --- | --- | --- | --- |
| **Consume** | [1. Reading a bundle](/manual/tutorial/01-reading), [2. Asking Claude](/manual/tutorial/02-consulting) | you want to use the existing bundles: read them, query them, cite them | a browser; optionally [Claude Code](https://claude.com/claude-code) |
| **Build** | [3. A bundle of your own](/manual/tutorial/03-new-bundle) to [7. Publishing](/manual/tutorial/07-publishing) | you want Claude to compile a wiki from your own sources | Claude Code, git, Python 3.11 or newer with PyYAML; Node 20 or newer to build the site |

The consume track takes about half an hour. The build track takes an afternoon for the setup and a pilot ingestion
of two sources; after that, a bundle grows one source at a time, at the pace you review it.

## What each chapter does

1. **[Reading a bundle](/manual/tutorial/01-reading).** Answer a real question from a bundle on this site: enter at the
   reading guide, follow links, read the status of a claim, a Source page and its notation map, a contradiction, the
   bibliography, the page graph and the bundle map.
2. **[Asking Claude](/manual/tutorial/02-consulting).** Install the consultation skill and ask questions from any
   directory; Claude navigates the bundle, cites pages and keeps hypotheses apart from literature.
3. **[A bundle of your own](/manual/tutorial/03-new-bundle).** Clone the repository and have Claude scaffold a new
   bundle for your domain.
4. **[The first ingestion](/manual/tutorial/04-ingestion).** Run a pilot of two sources and learn the atomic
   ingestion protocol: what Claude does, what you review, when you commit.
5. **[The citation record](/manual/tutorial/05-citations).** Every reference list of every source, merged into one
   `bibliography.bib`, and the reading list it gives you.
6. **[Keeping it honest](/manual/tutorial/06-quality).** Lint, deep lint, contradictions, claim status and identity
   checks: how the wiki avoids drifting into confident nonsense.
7. **[Publishing](/manual/tutorial/07-publishing).** The bundle registry, the checks and this documentation site.

Two words recur throughout. A **bundle** is one wiki on one domain, with its own sources, pages, notation and
bibliography. The **compiler** is Claude Code working inside the repository under its constitution
([CLAUDE.md](/reference/constitution)): it reads sources and writes the wiki, and you review and commit.

**Next:** [1. Reading a bundle](/manual/tutorial/01-reading).
