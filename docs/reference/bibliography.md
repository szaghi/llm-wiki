---
title: Bibliography format
---

# Bibliography format

Each bundle with scholarly sources keeps a **complete citation record**: every work cited by any ingested source,
whether or not it is itself ingested. Ingesting a paper means reading its reference list, and that reading is
captured, not discarded (D15).

## Files

| File | Role |
| --- | --- |
| `wiki/bibliography.bib` | canonical store, written by the compiler, in a strict BibTeX subset |
| `wiki/bibliography.md` | generated view, written by `tools/bib_to_md.py`, never edited |

The `.bib` is the canonical one: LaTeX can use it directly, and it accepts the custom `citedby` field. The lint fails
when `bibliography.md` differs from what the `.bib` generates. The site publishes each bundle's `.bib` for download at
`/bundles/<bundle>/bibliography.bib`.

## The BibTeX subset

```bibtex
% comment lines start with % outside entries
@article{berger-colella-1989,
  author = {Berger, M.J. and Colella, P.},
  title = {Local adaptive mesh refinement for shock hydrodynamics},
  journal = {J. Comput. Phys. 82:64-84},
  year = {1989},
  doi = {10.1016/0021-9991(89)90035-1},
  citedby = {almgren-1998, almgren-2010, balsara-2001},
}
```

The parser (`parse_bib` in `tools/bib_to_md.py`) accepts exactly this:

* `@type{key,` opens an entry. The type is free, lower-cased on reading.
* Fields are `name = {value}`, with balanced braces. Field names match `[a-z][a-z0-9_-]*`, and a field may appear only
  once per entry. Quoted (`"..."`) values are rejected.
* `}` closes the entry.
* `%` starts a comment line, outside entries only.

Whitespace inside a value is collapsed to single spaces. A parse error names its line number.

### Validation

`bib_to_md.py` and the lint check that:

* keys are unique and kebab-case, and the entries are sorted by key;
* every entry has a non-empty `title` and a four-digit `year`;
* each `citedby` is sorted, has no duplicates, does not contain the entry's own key, and names only slugs that have a
  Source page.

Title-less citation styles (ApJ, PRD, A&A) are entered with the placeholder title
`[title not printed in citing reference]`. For these, the venue numbers (journal, volume, page) decide the work's
identity.

### Fields used

`author`, `editor`, `title`, `journal`, `booktitle`, `school`, `institution`, `publisher`, `howpublished`, `series`,
`year`, `doi`, `eprint` (arXiv id), `url`, `isbn`, `note`, `citedby`. The generated view shows the first venue field
present, then the DOI, else the arXiv id, else the URL, then the ISBN and the note.

## Keys and ingested-ness

Keys follow the Source-page slug convention: `firstauthor-year[-disambiguator]`, kebab-case, for example
`balsara-2009-b`. The high-order-capturing-schemes bundle uses the year of the published issue. An entry whose key
equals a Source page's slug (`sources/<key>.md`) **is** that ingested source: whether a work is ingested is derived
from the key match and never stored in a field (D8). DOIs are included only when they are printed in the reference
list or verified, never invented.

## The citedby graph

`citedby = {slug-1, slug-2}` lists the ingested sources whose reference lists cite the work. It is the bundle's
citation graph. Two quantities are derived from it:

* **Merge progress.** A source's reference list is merged if and only if its slug appears in at least one `citedby`.
  `python3 tools/bib_to_md.py <bundle>/wiki --pending` lists the sources still missing.
* **The ingestion frontier.** Cited works that are not ingested, ranked by how many ingested sources cite them. They
  are what the corpus itself says it is missing. The generated view lists them under "Cited, not ingested", most
  cited first.

Reference lists are merged complete and unfiltered: filtering by relevance is a judgement call that destroys data, and
deduplication plus the `citedby` counts do the ranking. For scoped reads (books, long reviews), the extraction may be
limited to the chapters read, and the Source page records the scope.

## The generated view

`bibliography.md` opens with the totals: how many works, how many ingested, how many reference lists merged. It has
two sections:

1. **Ingested sources**, sorted by key. Each entry links its Source page and lists the ingested sources that cite it.
2. **Cited, not ingested**, sorted by citation count (descending) and then by key.

## Adding one source

During an ordinary ingestion (step 5 of the protocol), the compiler edits the `.bib` by hand. It adds an entry for
each newly cited work and appends the new slug to the `citedby` of each work already present. Then it regenerates the
view:

```bash
python3 tools/bib_to_md.py <bundle>/wiki
```

## The batched merger

`tools/bib_merge.py` exists for one situation: merging the reference lists of many sources at once, as when a whole
corpus predates its citation record (D16). Its machinery earns its cost at around ten fragments per run, not for a
single source.

### Workflow

1. Extract each source's printed reference list into `frag-<slug>.bib` in a scratch directory, one entry per printed
   reference, with keys in the slug convention.
2. Write a resolutions module: a plain Python file with the tables below. Start it with `ORDER` only.
3. Run `--report` and read the flags.
4. Resolve every flag by editing the module, and run again until `FLAGS: 0`.
5. Run `--write`, then regenerate the view and lint.
6. After the **final** batch, run `--dupes`.

```bash
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions r.py --report
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions r.py --write
python3 tools/bib_to_md.py <bundle>/wiki && python3 tools/lint_okf.py <bundle>/wiki
python3 tools/bib_merge.py <bundle>/wiki --dupes
```

### Resolution tables

| Table | Type | Meaning |
| --- | --- | --- |
| `ORDER` | `list[str]` | slugs to merge, in processing order; `frag-<slug>.bib` must exist for each. Required. |
| `ALIASES` | `dict[str, str]` | fragment key to canonical key. A scoped `"slug:key"` beats a bare `"key"`: the same printed key can mean different works in different fragments. |
| `NOTES` | `dict[str, str]` | text appended to an entry's `note` (year or venue variants, misprints, the reason for an identity decision) |
| `SILENCED` | `set[tuple[str, str]]` | reviewed pairs that need no action: distinct works that trip the heuristics, or `(k, k)` title-form variants |
| `REPAIRS` | `list[tuple[str, str, str]]` | `(dup, canon, note)`: fold an existing duplicate into its canonical entry (citedby union plus note) before the batch runs |
| `FIXUPS` | `dict[str, dict]` | field overrides applied to a final key after the merge |

### Flags

| Flag | Meaning | Resolution |
| --- | --- | --- |
| `[conflict]` | the same key carries two dissimilar real titles, or a conflicting DOI or eprint | `ALIASES` one fragment key to a distinct key |
| `[venuecheck]` | a placeholder-title merge whose journal, volume and page numbers do not overlap the existing entry | verify the venues, then `ALIASES` or `SILENCED` |
| `[suspect]` | a new key resembles an existing one (near-identical title, or same stem and year) | same work: `ALIASES`; distinct works: `SILENCED` |
| `[error]` | a `FIXUPS` or `NOTES` key does not exist after the merge | correct the key |

`--write` refuses to run while any flag is open (exit code 1). `[venuecheck]` is the decisive signal for title-less
reference lists: heed it. **A silenced pair is a claim, not a dismissal.** Silencing asserts that the two keys are
distinct works, and that assertion needs the same scrutiny as a merge. Wrong silences hid real duplicates twice in the
first backfill.

### Fixed merge rules

* Entries are deduplicated by key. An existing key gains the citing slug in its `citedby`, kept sorted and free of
  duplicates.
* A placeholder title is upgraded when a fragment supplies the real printed one.
* A missing `doi` or `eprint` is filled in from a fragment. A conflicting one is flagged, never overwritten: the
  identifier on the ingested Source page wins.
* Author initials are normalized (`J. U.` becomes `J.U.`).
* The output is sorted by key, in the same subset `bib_to_md.py` parses.

### The duplicate sweep

The per-batch merge deduplicates by key, and keys follow each citing source's spelling of the first author. The same
work cited under two spellings (an OCR error, a mis-transcribed or reordered author list) therefore lands under two
keys that no per-batch check can relate. `--dupes` groups the whole `.bib` by normalized title and year, skipping
placeholder titles, and marks each group whose keys have different author stems as `CROSS-STEM`. Review every one:
merge the same work (union of `citedby`), and leave distinct works alone. The sweep cannot see placeholder titles or
year misprints. For those, compare venue numbers, and search titles fuzzily across years.
