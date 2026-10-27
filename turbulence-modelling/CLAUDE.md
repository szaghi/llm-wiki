# Bundle law — turbulence-modelling

Domain (user decision, 2026-10-25, `DECISIONS.md` D30): the modelling
and simulation of turbulent flows, as collected in the user's turbulence
modelling bibliography (papers of 2017–2026).

* Reynolds-averaged closures: eddy-viscosity models (Spalart–Allmaras,
  $k$-$\omega$ SST, algebraic models), Reynolds-stress models, wall laws,
  laminar–turbulent transition models ($\gamma$-$Re_\theta$, algebraic,
  laminar kinetic energy);
* large-eddy simulation: filtering, subgrid-scale models (eddy viscosity,
  similarity, mixed, tensorial, nonlocal), explicit against implicit LES,
  numerical dissipation as a model, high-order filtering and
  regularization;
* wall modelling: equilibrium and non-equilibrium wall models, compressible
  velocity transformations, grid design and adaptation for wall-modelled
  LES;
* hybrid RANS/LES: detached-eddy simulation and its zonal and delayed
  forms, partially-averaged Navier–Stokes, model-split approaches;
* data-driven closures: field inversion and data assimilation, symbolic
  regression, neural-network closures, reinforcement-learning models,
  physics-informed networks and neural operators, the a priori against
  a posteriori question;
* discretizations for scale-resolving simulation: discontinuous Galerkin,
  flux reconstruction, spectral elements, gas-kinetic and lattice Boltzmann
  schemes, kinetic-energy- and entropy-preserving schemes, immersed
  boundaries, mesh adaptation, and the GPU codes that run them;
* direct numerical simulation of canonical and compressible flows
  (boundary layers up to hypersonic speeds, isotropic turbulence);
* turbulent combustion, and MHD, astrophysical and plasma turbulence
  (dynamos, subgrid models for astrophysical codes, turbulence in fusion
  devices).

The bundle is a standalone second brain, independent of every other bundle
and agnostic of every other repository (`DECISIONS.md` D12, D17, D30):
discretization subjects also live in `weno-teno` and
`high-order-capturing-schemes`, plasma turbulence in
`fusion-mhd-simulation`, astrophysical codes in
`astrophysical-simulation-codes`; a shared work is read again here, in this
bundle's notation.

## Corpus

- Primary archive: `~/papers/mosaic/turbulence_modelling/*.pdf`
  (read-only; Layer 1), 131 PDFs at founding (2026-10-25), named
  `year_Crossref_Journal_Surname_Title-prefix.pdf`. **The archive is still
  growing** (the human is adding papers): the founding plan covers the 131
  files present on 2026-10-25; files added later are appended to the plan
  (ghidoni-2026, wang-2023, elzaabalawy-2023, chunk 7; 134 files on
  2026-10-25) or ingested in further chunks after them, found with `tools/worklist.sh turbulence-modelling`.
  On 2026-10-26 the archive held 160 files: the 26 added since founding
  (all distinct works, identified by page 1 and Crossref) fill chunk 7 to
  20 and make chunk 8. On 2026-10-27 it held 307 files: the 147 added
  (all distinct works, none a second version of a planned one, identified
  by the page-1 DOI and Crossref) make chunks 9–15 of 20 and chunk 16 of 7,
  in archive order.
- The page-1 and checksum check of 2026-10-25 found 131 distinct works and
  no byte copies. The year in the filename is the online year (the slug
  uses the year of the published issue), and more than half of the files
  (78 by a page-1 stamp scan) are arXiv, HAL, Research Square or
  accepted-manuscript versions despite the "Crossref" in their name. Treat the filename as a hint and verify
  identity against page 1 and Crossref.
- **Version rule:** the Source page records the version read (arXiv vN,
  HAL, preprint server, accepted manuscript, version of record); its
  metadata is the published identity from Crossref. Claims and equations
  are those of the version read.
- Chunks (user decision): 20 sources each, 7 chunks for the founding
  archive. Chunk 1 holds the reviews and the papers that fix the
  vocabulary (data-driven modelling reviews, MHD turbulence review, the
  wall-model survey, LES of aircraft, DNS of combustion, explicit against
  implicit LES, backscatter, transition, hybrid RANS/LES and PANS,
  kinetic-energy-preserving DG and FLEXI, equilibrium and compressible wall
  models, wall-modelled LES on boundary-layer-conforming grids, tensorial
  SGS models, discretization-consistent and divergence-consistent learned
  closures, Spalart–Allmaras corrections), so that the registry and the
  reading guide are built from them; the other chunks follow the archive's
  order.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII with spaces, hyphens and particles joined
  (`lozanoduran`, `carrenoruiz`, `vangastelen`, `prietosaavedra`), the
  year that of the published issue. Same-author same-year papers take
  suffixes in publication order.
- Chunks are read by parallel subagents into scratch notes, compiled by
  the main session, staged as one unit with one commit message; the human
  reviews and commits before the next chunk starts (D26). Reference lists
  are merged with `tools/bib_merge.py` (D16); `--dupes` and a fuzzy-title
  sweep after the final chunk.
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
- Worklist: `tools/worklist.sh turbulence-modelling`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py turbulence-modelling/wiki --pending`.
- Lint: `python3 tools/lint_okf.py turbulence-modelling/wiki`. It must
  pass before commit.
- Commits: `docs(turbulence-modelling): ingest chunk N: <slugs>`.

## Status

**Chunk 9 staged 2026-10-27:** 20 papers of 2013–2022; 180 of 307
ingested, 153 concept pages plus the registry, 8241 bibliography entries,
deep lint done, five contradictions open. Chunk 10 follows with the
whole-bundle deep lint (190 ingestions).

**Chunk 8 committed 2026-10-27 (b24d200):** 20 papers of 2022–2026; 160 of 307
ingested, 148 concept pages plus the registry, 7232 bibliography entries,
deep lint done, five contradictions open (the fifth: the exponent of the
Langtry–Menter $F_3$). Chunks 9–16 (the 147 papers added on 2026-10-27)
follow; the whole-bundle deep lint is due with chunk 10 (190 ingestions),
the closing bibliography sweeps with the chunk that completes the archive.

**Chunk 7 committed 2026-10-26 (bed1245):** 20 papers of 2021–2026; 140 of 160
ingested, 143 concept pages plus the registry, 6521 bibliography entries,
first whole-bundle deep lint done (D26; due again by 190 ingestions or
with the chunk that completes the archive), four contradictions open.
Chunk 8 (20 papers added in October 2026) followed.

**Chunk 6 committed 2026-10-26 (58aad80):** 20 papers of 2024–2026; 120 of 134
ingested, 134 concept pages plus the registry, 5882 bibliography entries,
deep lint done, four contradictions open (sparse-regression coefficients;
gas-kinetic dissipation; constants of the Cai & Sagaut inverse wall law;
Ahmed-body slant topology).

**Chunk 5 committed 2026-10-26 (fdc020d):** 20 papers of 2023–2025; 100 of 134
ingested, 115 concept pages plus the registry, 4987 bibliography entries,
deep lint done, three contradictions open.

**Chunk 4 committed 2026-10-26 (cc8d2c6):** 20 papers of 2023–2024; 103
concept pages, 4241 bibliography entries, deep lint done, two
contradictions open.

**Chunk 3 committed 2026-10-26 (ea8bf9f):** 20 papers of 2022–2023; 84
concept pages, 3573 bibliography entries, deep lint done, no contradiction
open.

**Chunk 2 committed 2026-10-25 (eeda52f):** 20 papers of 2021–2023; 68
concept pages, 2768 bibliography entries, deep lint done, no contradiction
open.

**Chunk 1 committed 2026-10-25 (6271a4e):** scaffold (D30) and the 20
reviews and vocabulary papers; 55 concept pages plus the registry, 1815
bibliography entries, deep lint done, no contradiction open.
