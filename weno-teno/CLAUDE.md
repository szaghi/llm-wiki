# Bundle law — weno-teno

Domain (user decision, 2026-10-21, `DECISIONS.md` D29): high-order
discretizations of hyperbolic conservation laws and compressible flows, as
collected in the user's research bibliography of 2021–2026.

* reconstruction: ENO, WENO and its variants (Jiang–Shu, Z, Z+, ZN,
  mapped, affine-invariant, alternative/A-WENO, multi-resolution, Hermite,
  weighted compact/WCNS), TENO, CWENO, THINC and hybrid interface
  capturing, gradient-based and RBF reconstruction, data-driven and
  learned weights;
* fluxes: flux splitting, characteristic decomposition, Riemann solvers,
  central-upwind schemes, path-conservative schemes, kinetic-energy- and
  entropy-preserving split forms;
* element methods: discontinuous Galerkin and flux reconstruction (DGSEM,
  entropy-stable DG, subcell and convex limiting, OEDG, filtering,
  artificial viscosity), Active Flux;
* structure preservation: bound and positivity preservation (geometric
  quasilinearization, optimal cell-average decomposition),
  well-balancing, asymptotic preservation, divergence-free MHD;
* geometry and physics: shock tracking and moving meshes, immersed
  boundaries, compressible multiphase flows, MHD and relativistic flows;
* software: the GPU and AMR solvers that implement these schemes.

Time integration enters only as the stepper of the semi-discrete scheme
(SSP Runge–Kutta, IMEX, semi-implicit). The bundle is a standalone second
brain, independent of every other bundle and agnostic of every other
repository (`DECISIONS.md` D12, D17, D29): several of its subjects also
live in `high-order-capturing-schemes`, and a shared work is read again
here, in this bundle's notation.

## Corpus

- Primary archive: `~/papers/mosaic/weno-teno/*.pdf` (read-only; Layer 1),
  207 PDFs at founding (217 after the human added ten founding papers on
  2026-10-30, ingested as chunk 12), named `year_Crossref_Journal_Surname_Title-prefix.pdf`.
  The year in the filename is the online year, the surname is sometimes
  a given name (`Dinshaw` for Balsara, `C` for C. B. Sousa), and roughly a
  third of the files are arXiv, HAL or SSRN preprints despite the "Crossref" in
  their name. Treat the filename as a hint and verify identity against
  page 1 and Crossref.
- Known archive defects (2026-10-21, page-1 and checksum check), awaiting
  the human's decision:
  - the "Wang 2023" C&F file (`2023_..._Wang_Fifth_order_AWENO_...`) is a
    byte copy of Li et al. 2022 (WENO-ZN, C&F 244:105547);
  - the "Li 2024" JCP file (`2024_..._Li_A_family_of_TENOA-THINC-MOOD_...`)
    is a byte copy of Liang et al. 2022 (TENO, JCP 467:111465);
  - the "Feng 2026" Physics of Fluids file holds Wang, Don & Wang 2023
    (AWENO with adaptive numerical diffusion, C&F 251:105743), which is
    ingested from it as `wang-2023`;
  - the "Wu 2023" SIAM J. Numer. Anal. file holds only the 9-page
    Supplementary Materials of Wu & Shu's positivity-preserving central
    DG paper (found 2026-10-23, chunk 7).
  Three works are therefore missing or incomplete: Feng et al. 2026
  (Phys. Fluids 38:011302), Li et al. 2024 (JCP 519:113375) and Wu &
  Shu 2023 (SINUM 61:250-285). The list for the re-download is
  `~/papers/mosaic/weno-teno-redownload.csv`. `wang-2023` was
  ingested from the "Feng" file in chunk 11 (2026-10-24); the three
  missing works are ingested once their PDFs are in the archive.
- **Version rule:** the Source page records the version read (arXiv vN,
  HAL, SSRN, accepted manuscript, version of record); its metadata is the
  published identity from Crossref. Claims and equations are those of the
  version read.
- Chunks (user decision): 20 sources each, 11 chunks. Chunk 1 holds the
  reviews and the papers that fix the vocabulary (TENO review, geometric
  quasilinearization, the unified compact-stencil framework, affine-invariant
  and A-WENO, WENO-Z+ and ZN, entropy-stable DG, subcell and convex
  limiting, OEDG, Active Flux, kinetic-energy preservation), so that the
  registry and the reading guide are built from them; the other chunks
  follow the archive's order.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII with spaces, hyphens and particles joined
  (`ruedaramirez`, `devanna`, `delgrosso`, `lopezmiralles`), the year that
  of the published issue. Same-author same-year papers take suffixes in
  publication order.
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
- Worklist: `tools/worklist.sh weno-teno`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py weno-teno/wiki --pending`.
- Lint: `python3 tools/lint_okf.py weno-teno/wiki`. It must pass before
  commit.
- Commits: `docs(weno-teno): ingest chunk N: <slugs>`.

## Status

**Chunk 12 completed 2026-10-30 (night protocol, commit pending):** ten
founding papers added by the human (van Leer 1979, Harten 1983, Harten et
al. 1987, Shu & Osher 1988, Liu et al. 1994, Jiang & Shu 1996, Borges et
al. 2008, Shu 2009, Zhang & Shu 2010, Fu et al. 2016); 214 of 217 ingested
(feng-2026, li-2024 and wu-2023 still await a re-download), 230 concept
pages plus the registry, 5733 bibliography entries, eight contradictions
open (new: order of WENO-JS at critical points).

**Chunk 11 committed 2026-10-24 (3e40199), archive complete at the time:** the last five
sources, the whole-bundle deep lint and the closing bibliography sweeps;
204 of 207 ingested (feng-2026, li-2024 and wu-2023 await a re-download),
224 concept pages plus the registry, 5567 bibliography entries, seven
contradictions open (the six of chunk 10 and whether the Brio–Wu compound
wave is part of the solution). Next: ingest the three defective works once
their PDFs are in the archive.

**Chunk 10 committed 2026-10-23 (be807d5):** converged ENO, learned and adaptive
TENO/WCNS, Active Flux variants, entropy-stable MHD DG, low-Mach and
multiphase codes; 199 of 207 ingested, 221 concept pages plus the
registry, 5442 bibliography entries, deep lint done, six contradictions
open (the five of chunk 9 and whether HLL is carbuncle-free under
high-order reconstruction).

**Chunk 9 committed 2026-10-23 (e275831):** PAMPA, tensor-train and AENO
reconstruction, entropy projection, central-upwind and relativistic MHD
schemes; 179 of 207 ingested, 212 concept pages plus the registry, 5027
bibliography entries, deep lint done, five contradictions open (TENO
$\tau_K$; conservation of WCNS; entropy-filter tolerance; cost of WENO-Z
against mapped WENO; order of TENO at a second-order critical point).

**Chunk 8 committed 2026-10-23 (22017c3):** multi-resolution WENO, TENO and THINC
variants, DG limiters, MHD and shallow-water schemes; 159 of 207
ingested, 200 concept pages plus the registry, 4666 bibliography
entries, deep lint done, five contradictions open (TENO $\tau_K$;
conservation of WCNS; entropy-filter tolerance; cost of WENO-Z against
mapped WENO; order of TENO at a second-order critical point).

**Chunk 7 committed 2026-10-23 (2dafcd9):** TENO variants, limiters, ADER,
well-balanced and multiphase solvers; 139 of 207 ingested (wu-2023
deferred: the archive file holds only its supplement), 191 concept pages
plus the registry, 4315 bibliography entries, four contradictions open.

**Chunk 6 committed 2026-10-23 (82b0c9e):** WCNS weights, flux globalization,
entropy-stable DG for air, interface methods; 120 of 207 ingested, 181
concept pages plus the registry, 3765 bibliography entries, deep lint
done, three contradictions open (TENO $\tau_K$; conservation of WCNS;
entropy-filter tolerance).

**Chunk 5 committed 2026-10-22 (a001f6a):** gradient-based schemes, wall-modelled LES,
structure-preserving MHD, GPU codes; 100 of 207 ingested, 167 concept
pages plus the registry, 3291 bibliography entries, deep lint done, two
contradictions open (TENO $\tau_K$; conservation of WCNS).

**Chunk 4 committed 2026-10-22 (9324881):** TENO variants, positivity for
Navier–Stokes, shock tracking, all-Mach IMEX, codes.

**Chunk 3 committed 2026-10-23 (0a9f822):** flux reconstruction, entropy
correction, DG limiters, multiphase and relativistic flows.

**Chunk 2 committed 2026-10-22 (fb1b286):** WENO variants, entropy-stable
DG, multiphase models, shock tracking.

**Chunk 1 committed 2026-10-22 (3bc58e0):** scaffold (D29) and the 20
reviews and vocabulary papers.
