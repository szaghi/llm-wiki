# Bundle law — immersed-boundary-methods

Domain (user decision, 2026-11-08, `DECISIONS.md` D32): immersed boundary,
embedded boundary and fictitious-domain methods, as collected in the user's
immersed-boundary bibliography (papers of 1972–2026).

* the classical immersed boundary method for fluid–structure interaction:
  Lagrangian structures, regularized delta functions, spreading and
  interpolation, stiffness and time stepping;
* continuous forcing (feedback forcing, volume/Brinkman penalization) and
  discrete forcing (direct forcing, velocity reconstruction, mass sources);
* sharp-interface methods: ghost-cell, immersed interface and ghost fluid
  methods, inverse Lax–Wendroff boundary treatments;
* cut-cell (embedded-boundary) finite volumes and the small-cell problem:
  cell merging, flux and state redistribution, AMR;
* finite-element immersed methods: CutFEM, the shifted boundary method,
  stability and conditioning of immersed finite elements;
* high-order and discontinuous Galerkin immersed discretizations,
  compressible and shock–obstacle flows, moving bodies, fluid–structure
  interaction, plasma–wall and MHD embedded boundaries, GPU implementations.

The bundle is a standalone second brain, independent of every other bundle
and agnostic of every other repository (`DECISIONS.md` D12, D17, D32):
immersed boundaries on overlapping grids also live in
`overset-grid-methods`, high-order and cut-cell DG schemes in
`high-order-capturing-schemes` and `weno-teno`, constrained-transport MHD in
`div-free-amr`; a shared work is read again here, in this bundle's notation.

## Corpus

- Primary archive: `~/papers/mosaic/immersed-boundary/*.pdf` (read-only;
  Layer 1), 57 PDFs at founding (2026-11-08), 65 since chunk 7 (2026-11-13), named
  `year_Crossref_Venue_Surname_Title-prefix.pdf`. Papers added later are
  ingested in further chunks, found with
  `tools/worklist.sh immersed-boundary-methods`.
- The page-1 and checksum check of 2026-11-08 found 57 distinct works and
  no byte copies; all identities were confirmed on Crossref, 22 of them by
  bibliographic search because page 1 carries no DOI. Two files are
  image-only scans read through OCR (goldstein-1993, pember-1995). Seven
  works are also Source pages of other bundles; they are read again here
  (D12). The year in the filename is the online or archive year; the slug
  uses the year of the published issue (burman-2015 is filed as 2014). Treat
  the filename as a hint and verify identity against page 1 and Crossref.
- **Version rule:** the Source page records the version read; its metadata
  is the published identity from Crossref, corrected from page 1 where
  Crossref misspells (pember-1995: Crutchfield).
- Chunks (user decision): 10 sources each, in archive (chronological)
  order; chunk 1 holds the founding papers of 1972–2002 from which the
  registry and the reading guide are built; chunk 6 holds the last seven
  papers with the whole-bundle deep lint and the closing bibliography sweeps.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative for
  every concept page. Extend it, and log the extension, before writing math
  that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname in
  lowercase ASCII with spaces, hyphens and particles joined (de Prenter →
  `deprenter`, Ménez → `menez`), the year that of the published issue.
  Same-author same-year papers take suffixes in publication order
  (giuliani-2022 is the SISC paper of February 2022, giuliani-2022-b the JCP
  paper of September 2022).
- Chunks are compiled inline by the main session, without subagents (the
  owner's standing instruction), and handed to the human as one unit with
  one commit message (D26). The founding ingestion runs under the night
  protocol (D32): each chunk is one snapshot step, committed by the human
  in order. Reference lists come from the Crossref deposited records where
  they exist and are transcribed from the printed list otherwise; they are
  merged with `tools/bib_merge.py` (D16); `--dupes` and a fuzzy-title sweep
  after the final chunk.
- Issues file: [`INGESTION-ISSUES.md`](INGESTION-ISSUES.md) (bundle root,
  outside the wiki) records per chunk every contradiction opened, every
  printed inconsistency, identity or metadata problem, every paper that
  would fit another bundle better, and every decision left to the human.
  The `## Contradictions` sections of concept pages stay the normative
  record; the file is the reviewer's digest.
- Bibliography preprints: a citation printed in pre-publication form
  (submitted, accepted, in preparation, to appear, arXiv) is its own entry,
  keyed by the year of that form — the citing paper's year when none is
  printed — and is never folded into the published entry.
- Timestamps come from the real clock (`date -u`), never planned times.
- Worklist: `tools/worklist.sh immersed-boundary-methods`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py immersed-boundary-methods/wiki --pending`.
- Lint: `python3 tools/lint_okf.py immersed-boundary-methods/wiki`. It must
  pass before commit.
- Commits: `docs(immersed-boundary-methods): ingest chunk N: <slugs>`.

## Status

**Chunk 7 snapshot 2026-11-13 (night protocol, awaiting the owner's commit):** the 8 papers of the owner's
moving-cut-cell list (1993–2023); 65 of 65 ingested, 32 concept pages plus
the registry, 2767 bibliography entries, one contradiction open
(spurious-force-oscillations).

**Chunk 6 committed 2026-11-08 (ad2cb2e): archive complete,** 57 of 57 ingested, 30 concept pages plus the
registry, 2598 bibliography entries after the closing duplicate sweep,
whole-bundle deep lint done, no contradiction open.

**Chunk 5 committed 2026-11-08 (36bb8df):** 10 papers of 2023–2025; 50 of 57 ingested, 30 concept pages plus
the registry, 2287 bibliography entries, compiler self-audit done, no
contradiction open.

**Chunk 4 committed 2026-11-08 (523731b):** 10 papers of 2022–2023; 40 of 57 ingested, 29 concept pages plus
the registry, 1780 bibliography entries, compiler self-audit done, no
contradiction open.

**Chunk 3 committed 2026-11-08 (dff2dcc):** 10 papers of 2014–2022; 30 of 57 ingested, 27 concept pages plus
the registry, 1186 bibliography entries, compiler self-audit done, no
contradiction open.

**Chunk 2 committed 2026-11-08 (ef78af8):** 10 papers of 2003–2015; 20 of 57 ingested, 24 concept pages plus
the registry, 609 bibliography entries, compiler self-audit done, no
contradiction open.

**Chunk 1 committed 2026-11-08 (c7a1a0a):** the 10 founding papers of 1972–2002; 10 of 57 ingested, 18
concept pages plus the registry, 312 bibliography entries, compiler
self-audit done, no contradiction open.
