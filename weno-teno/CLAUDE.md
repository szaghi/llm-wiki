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
  207 PDFs at founding, named `year_Crossref_Journal_Surname_Title-prefix.pdf`.
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
    ingested from it as `wang-2023`.
  Two works are therefore missing: Feng et al. 2026 (Phys. Fluids
  38:011302) and Li et al. 2024 (JCP 519:113375). The list for the
  re-download is `~/papers/mosaic/weno-teno-redownload.csv`. These sources
  and `wang-2023` are ingested last (chunk 11).
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

**Chunk 1 staged 2026-10-21 (scaffold, D29):** the 20 reviews and
vocabulary papers; 20 of 207 ingested, 82 concept pages plus the registry,
860 bibliography entries, deep lint done, one contradiction open (accuracy
condition on $\tau_K$ of TENO). Next: chunk 2 per the archive's order.
