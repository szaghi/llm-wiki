---
title: 5. The citation record
---

# 5. The citation record

Ingesting a paper means reading its reference list too, and that reading is kept. Each bundle has a **citation
record**: every work cited by any ingested source, whether or not it is ingested itself. This chapter shows what it
contains and what it is for.

## Two files

| File | What it is | Who writes it |
| --- | --- | --- |
| `wiki/bibliography.bib` | the canonical record, in a strict subset of BibTeX | Claude, at every ingestion |
| `wiki/bibliography.md` | a readable view of the same record | `tools/bib_to_md.py`, never by hand |

The `.bib` is strict: one entry per work, `field = {value}` only, entries sorted by key, `%` for comments. The key
follows the Source-page slug convention, `firstauthor-year` with a suffix when needed (`balsara-2009`,
`balsara-2009-b`). An entry whose key matches a Source page **is** that ingested source; ingestion status is never
stored in a field.

Every entry carries one custom field, `citedby`. A real entry, from the high-order shock-capturing schemes bundle
(its `citedby` list shortened here):

```bibtex
@article{roe-1981,
  author = {Roe, P.L.},
  title = {Approximate Riemann Solvers, Parameter Vectors, and Difference Schemes},
  journal = {J. Comput. Phys. 43:357},
  year = {1981},
  doi = {10.1016/0021-9991(81)90128-5},
  note = {cited by jiang-1996 with venue misprinted as J. Comput. Phys. 27:1 (1978), Sod's venue; ...},
  citedby = {balsara-2000, balsara-2016-b, balsara-2017-b, ..., toro-1997, woodward-1984},
}
```

The `note` field records what the citing sources printed when it disagrees with the verified record: misprints are
kept as data, not silently corrected. `citedby` lists the ingested sources whose reference lists contain the work: sorted, without duplicates. Across all
entries, this is the bundle's **citation graph**.

The reference lists are merged complete and unfiltered. Deciding which references are relevant would be a judgment
call that destroys data; the `citedby` counts do the ranking instead. A DOI enters an entry only when it is printed in
the reference list or verified.

## Regenerate and check

After any change to the `.bib`:

```bash
python3 tools/bib_to_md.py <bundle>/wiki            # rewrite bibliography.md
python3 tools/bib_to_md.py <bundle>/wiki --check    # exit 1 if the .md is out of sync
```

The linter runs the same check, so an out-of-date `bibliography.md` fails the lint.

Progress is derived too: a source's reference list counts as merged when its slug appears in at least one `citedby`.
To list the ingested sources whose lists are not merged yet:

```bash
python3 tools/bib_to_md.py <bundle>/wiki --pending
```

## The frontier: a reading list from the literature

`bibliography.md` lists the ingested sources first, then the works **cited but not ingested**, sorted by how many
ingested sources cite them. The top of that list is the **ingestion frontier**: what your corpus keeps citing and
does not yet contain. It is the best answer to "what should I read next?" that does not depend on anyone's taste.
See it on the site in any bundle's bibliography, for example
[high-order shock-capturing schemes](/bundles/high-order-capturing-schemes/bibliography).

::: tip Prompt
List the ten most cited works in the `<bundle>` frontier and tell me which of them are in my archive.
:::

## Backfilling many sources at once

For one new source, Claude edits the `.bib` directly. If you adopt the citation record on a bundle that already has
many sources, merging their reference lists one by one is where duplicates multiply: the same paper is cited with
different author spellings, misprinted years, or no title at all (common in ApJ-style lists). For that case there is
a batched merger, `tools/bib_merge.py`:

```bash
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions r.py --report   # repeat until FLAGS: 0
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions r.py --write
python3 tools/bib_merge.py <bundle>/wiki --dupes                                     # after the final batch
```

It merges per-source fragments (`frag-<slug>.bib`) under a resolutions file you review, and it never guesses an
identity: it flags every collision and refuses to write until each flag is resolved. The closing `--dupes` sweep is
mandatory: only a whole-corpus comparison finds the same work entered under two keys. The
[bibliography reference](/reference/bibliography) and [tools reference](/reference/tools) have the details.

**Next:** [6. Keeping it honest](/manual/tutorial/06-quality).
