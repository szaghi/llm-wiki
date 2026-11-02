# Bundle law — overset-grid-methods

Domain (user decision, 2026-11-02, `DECISIONS.md` D31): overset, Chimera
and composite overlapping grid methods, as collected in the user's
overset-grid bibliography (papers of 1983–2027).

* grid embedding and composite overlapping grids: component grids, their
  mappings, point classification, overlap requirements;
* domain connectivity and overset grid assembly: explicit, implicit and
  wall-distance-based hole cutting, donor search, fringe (receptor) and
  orphan points, overlap optimization, the assembly tools (PEGASUS,
  SUGGAR, composite-grid generators) and their parallel algorithms;
* inter-grid communication: interpolation, its order and width, its
  effect on accuracy, conservation and stability; conservative interface
  algorithms, flux corrections, nonlinear (WENO-type) interpolation,
  interpolation-free coupling;
* moving overset grids, relative body motion, adaptive mesh refinement on
  overlapping grids; overset grids combined with immersed boundaries;
* discretizations on overlapping grids: compact finite differences,
  discontinuous Galerkin and spectral elements, ADER and Lax–Wendroff
  schemes, upwind schemes for wave equations, implicit–explicit time
  stepping; the energy-stability and summation-by-parts theory of
  overlapping grids;
* flows and physics on overset grids: incompressible and compressible
  flow, shock capturing, multiphase flow, fluid–structure interaction,
  Maxwell's equations, spherical (Yin–Yang) grids for geophysics and
  astrophysics; GPU and parallel implementations; applications.

The bundle is a standalone second brain, independent of every other bundle
and agnostic of every other repository (`DECISIONS.md` D12, D17, D31):
curvilinear mappings and metric identities also live in
`curvilinear-metric-discretization`, high-order and shock-capturing
schemes in `weno-teno` and `high-order-capturing-schemes`, turbulence in
`turbulence-modelling`; a shared work is read again here, in this bundle's
notation.

## Corpus

- Primary archive: `~/papers/mosaic/overset-chimera/*.pdf` (read-only;
  Layer 1), 51 PDFs at founding (2026-11-02), named
  `year_Crossref_Venue_Surname_Title-prefix.pdf`. Papers added later are
  ingested in further chunks, found with
  `tools/worklist.sh overset-grid-methods`.
- The page-1 and checksum check of 2026-11-02 found 51 distinct works and
  no byte copies. Sixteen files (the conference papers of 1983–2005 and
  several accepted manuscripts) carry no DOI on page 1; their identity was
  found on Crossref from title and author and confirmed on page 1. The
  year in the filename is the online year; the slug uses the year of the
  published issue (hu-2027 and glaubitz-2027 are 2027 issues published
  online in 2026). Treat the filename as a hint and verify identity
  against page 1 and Crossref.
- **Version rule:** the Source page records the version read (scan of a
  conference paper, arXiv vN, HAL, accepted manuscript, version of
  record); its metadata is the published identity from Crossref. Claims
  and equations are those of the version read.
- Chunks (user decision): 10 sources each, in archive (chronological)
  order, so chunk 1 holds the founding papers (Benek et al. 1983 and
  1985, Meakin & Suhs 1989, Chesshire & Henshaw 1990, Henshaw 1994,
  Wang 1995, Lee & Baeder 2003, Rogers et al. 2003, Kageyama & Sato 2004,
  Noack 2005) from which the registry and the reading guide are built;
  chunk 6 holds the last paper with the whole-bundle deep lint and the
  closing bibliography sweeps.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII with spaces, hyphens and particles joined, the year
  that of the published issue. Same-author same-year papers take
  suffixes in publication order.
- Chunks are read by parallel subagents into scratch notes, compiled by
  the main session, and handed to the human as one unit with one commit
  message; the human reviews and commits before the next chunk is
  committed (D26). The founding chunks were compiled unattended under the
  night protocol (D31): each chunk is one snapshot step, committed by the
  human in order. Reference lists are merged with `tools/bib_merge.py`
  (D16); `--dupes` and a fuzzy-title sweep after the final chunk.
- Issues file: [`INGESTION-ISSUES.md`](INGESTION-ISSUES.md) (bundle root,
  outside the wiki) records per chunk every contradiction opened, every
  printed inconsistency, identity or metadata problem, every paper that
  would fit another bundle better, and every decision left to the human.
  The `## Contradictions` sections of concept pages stay the normative
  record; the file is the reviewer's digest.
- Bibliography preprints: a citation printed in pre-publication form
  (submitted, accepted, in preparation, to appear, arXiv) is its own entry,
  keyed by the year of that form, and is never folded into the published
  entry.
- Timestamps come from the real clock (`date -u`), never planned times.
- Worklist: `tools/worklist.sh overset-grid-methods`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py overset-grid-methods/wiki --pending`.
- Lint: `python3 tools/lint_okf.py overset-grid-methods/wiki`. It must
  pass before commit.
- Commits: `docs(overset-grid-methods): ingest chunk N: <slugs>`.

## Status

**Chunk 5 compiled 2026-11-02 (night step 05-chunk-5):** 10 papers of
2025–2027; 50 of 51 ingested, 53 concept pages plus the registry, 1706
bibliography entries; targeted reading and Crossref reference lists; no
contradiction open. Chunk 6 (the last paper, with the whole-bundle deep
lint and closing sweeps) follows.

**Chunk 4 compiled 2026-11-02 (night step 04-chunk-4):** 10 papers of
2022–2025; 40 of 51 ingested, 52 concept pages plus the registry, 1290
bibliography entries; targeted reading and Crossref reference lists (no
subagents, owner's instruction); no contradiction open.

**Chunk 3 compiled 2026-11-02 (night step 03-chunk-3):** 10 papers of
2022; 30 of 51 ingested, 49 concept pages plus the registry, 1009
bibliography entries, compiler self-audit (no subagents, owner's
instruction), no contradiction open.

**Chunk 2 compiled 2026-11-02 (night step 02-chunk-2):** 10 papers of
2005–2021; 20 of 51 ingested, 40 concept pages plus the registry, 636
bibliography entries, deep lint done, no contradiction open.

**Chunk 1 compiled 2026-11-02 (night step 01-chunk-1):** the 10 founding
papers of 1983–2005; 10 of 51 ingested, 28 concept pages plus the
registry, 209 bibliography entries, deep lint done, no contradiction open.
