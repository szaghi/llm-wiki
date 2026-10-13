---
title: 4. The first ingestion
---

# 4. The first ingestion

**Ingesting** a source means: Claude reads it completely, merges what it says into the bundle's concept pages, writes
its Source page, merges its reference list into the citation record, and stages the result for you to review. This
chapter runs a pilot of two sources, then shows the protocol behind it.

## Start with a pilot

Pick two sources: one clean (a recent paper with a good text layer) and one hard (a scanned PDF, or a long book).
The hard one shows you early how Claude handles what goes wrong. In Claude Code, in the repository root:

::: tip Prompt
Run a pilot ingestion on `<bundle>`: ingest `<path-to-source-A>` and `<path-to-source-B>`, then stop for my audit.
:::

When Claude stops, audit before you commit:

- open each **Source page** next to the PDF. Are the key claims really in the paper, at the cited section or
  equation? Is the metadata (authors, year, venue, DOI) right?
- read the **Notation map**. Every symbol the paper uses differently from your registry should be there;
- open each **concept page** Claude created or updated (the Source page lists them). Does each claim cite the source
  it came from? Did the page earn its existence, or is it a stub?
- read the new entry at the top of `wiki/log.md`.

Correct what is wrong by telling Claude, not by editing the pages yourself: the correction then goes through the
same protocol and the same lint. When you are satisfied, commit with the message Claude gave you, for example:

```bash
git commit -m "docs(<bundle>): ingest <source-slug>"
```

Then continue in bulk:

::: tip Prompt
Continue ingesting the `<bundle>` sources, foundations first. Stage after each source.
:::

## The protocol, step by step

Every ingestion follows the same atomic protocol, one source at a time. *Atomic* means a source is either fully
ingested and staged, or discarded: there is no half-ingested state.

1. **Read fully.** Text extraction first; for image-only scans, page by page, visually. An illegible passage is
   recorded on the Source page as a gap. An equation is never guessed.
2. **Extract concepts** the source touches, and decide which deserve a page. A page needs either two sources, or one
   source that presents it as a named contribution (a method, theorem or benchmark that is the point of the paper),
   or an exact identity, or a load-bearing definition. Everything else stays inline in a parent page. There are no
   stubs.
3. **Create or merge** concept pages, in the bundle's notation:
   - the source *agrees* with a page: its citation is added; several citations are visible evidence;
   - it *extends* a page: the new material is integrated, cited;
   - it *contradicts* a page: both sides are recorded under `## Contradictions`, attributed. The newer claim does not
     win by being newer, and nothing is silently overwritten.
4. **Write the Source page**: metadata verified against page 1 of the source (never taken from the filename), the
   `# Notation map`, and the list of every page created or updated.
5. **Merge the reference list** into `wiki/bibliography.bib`, complete and unfiltered, and regenerate
   `bibliography.md` ([chapter 5](/manual/tutorial/05-citations)).
6. **Append to `log.md`**: date, source, pages touched.
7. **Update the folder indexes** (and the reading guide when the bundle's structure changes).
8. **Lint**: `python3 tools/lint_okf.py <bundle>/wiki` must pass.
9. **Stage and hand off**: `git add -A`, and the commit message `docs(<bundle>): ingest <source-slug>`.

If a session ends in the middle, `git status` tells the next one what happened: a clean tree means you committed;
a fully staged tree means an ingestion is complete and waiting for your commit; unstaged changes mean an aborted
ingestion, to be discarded with `git checkout`.

## What is left to ingest

Whether a source is ingested has exactly one answer: its Source page exists. There is no queue file to go stale.
For an archive of PDFs, the worklist is derived:

```bash
./tools/worklist.sh <bundle>
```

It lists every PDF in the bundle's archive that no Source page references, then `pending: N / M`. The script reads
the archive path from the `corpus` key of the bundle's `bundle.toml`; without that key it looks in
`~/papers/mosaic/<bundle>/`, this repository's convention.

## Sources of every kind

Sources are not only papers. You reviewed each one, so it is trusted; Claude still verifies its *identity*
(page-1 metadata, the DOI against Crossref), because trust and identity are different things.

**A paper already in the archive:**

::: tip Prompt
Ingest `~/papers/<archive>/<file>.pdf` into `<bundle>`.
:::

**A paper you have only as a DOI.** Claude asks you for the PDF (or fetches an open-access copy, if one exists and you
agree). It does not get around paywalls or anti-bot pages.

::: tip Prompt
Ingest doi:10.xxxx/yyyy into `<bundle>`.
:::

**A web page or blog post.** Captured to `raw/web/` first, so link rot cannot take the source away:

::: tip Prompt
Ingest https://example.org/post into `<bundle>`. Capture it to raw/.
:::

**Your own notes, slides or report.** Claims that are yours become `status: hypothesis`: a published source can
overturn them, and they cannot promote anything to `established`:

::: tip Prompt
Ingest my notes at `<path>` into `<bundle>`. These are working hypotheses; mark them as such.
:::

**A book or long thesis**, as a scoped read. The Source page records which chapters were read, and the reference
list may be scoped to them:

::: tip Prompt
Ingest `<path-to-book>` into `<bundle>` as a scoped read: chapters X to Y in depth; record the coverage.
:::

In every case Claude ends at *staged plus a commit message*, and you commit.

**Next:** [5. The citation record](/manual/tutorial/05-citations).
