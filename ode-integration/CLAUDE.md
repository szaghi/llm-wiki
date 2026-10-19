# Bundle law — ode-integration

Domain (user decision, 2026-10-19, `DECISIONS.md` D27): the numerical time
integration of ordinary differential equations and of method-of-lines
semi-discretizations of partial differential equations.

* theory: Runge–Kutta order conditions, rooted trees and B-series, stage
  order, weak stage order and order reduction, stability functions and
  stability polynomials, A-, L-, B- and algebraic stability, strong
  stability preservation (SSP) and contractivity, energy and entropy
  laws of the fully discrete scheme;
* method families: explicit, diagonally implicit and fully implicit
  Runge–Kutta; Rosenbrock–Wanner; BDF and linear multistep methods;
  additive, partitioned and generalized-additive (GARK) methods, IMEX;
  multirate, multirate-infinitesimal and local time stepping;
  exponential integrators; stabilized (Chebyshev, Legendre) and
  paired-explicit Runge–Kutta; low-storage schemes; splitting and
  composition; deferred correction, ADER and multiderivative methods;
  Patankar-type and other positivity-preserving schemes; relaxation
  Runge–Kutta and other structure-preserving time stepping;
  asymptotic-preserving schemes for multiscale problems;
* practice: step-size control and error estimation, solvers and
  preconditioners for implicit stages, parallel-in-time methods
  (Parareal, ParaDiag, parallel SDC), integrator software (SUNDIALS,
  ARKODE, Irksome, Julia DifferentialEquations), mixed precision,
  learned integrators.

Spatial discretizations (DG, flux reconstruction, finite volumes,
shock capturing) enter only as the generator of the semi-discrete system
or where they are coupled to the time scheme (ADER, Lax–Wendroff flux
reconstruction, flux limiting in time). It is a standalone second brain,
independent of every other bundle and agnostic of every other repository
(`DECISIONS.md` D12, D17, D27).

## Corpus

- Primary archive: `~/papers/mosaic/ode-integration/*.pdf` (read-only;
  Layer 1), 117 PDFs at founding, 120 after the re-download (2026-10-19), named
  `year_Crossref_Journal_Surname_Title-prefix.pdf`. Many files are arXiv or
  HAL preprints despite the "Crossref" in their name, and the year in the
  filename is the online year. Treat the filename as a hint and verify
  identity against page 1 and Crossref.
- Known archive defects (2026-10-19, page-1 check): two files hold a
  different paper than their name says and are ingested under their true
  identity (the short-titled "Vermeire 2021" file is Al Jahdali et al.
  2022; the short-titled "Izgin 2022" file is Belardo et al. 2026). Five
  files were download errors; by the human's authorization the compiler
  overwrote four of them with the right papers (Abdulle 2022, Goswami 2023,
  Maurya 2021, Wei 2026) and added the Buvoli 2023 main paper beside its
  supplement and the real Vermeire 2021 and Izgin 2022 under full-title
  filenames. Li et al. 2022 was dropped by the human, who removes its
  file (an issue front matter). These seven sources are ingested last
  (chunk 6).
- **Version rule:** the Source page records the version read (arXiv vN,
  HAL, accepted manuscript, version of record); its metadata is the
  published identity from Crossref. Claims and equations are those of the
  version read.
- Chunks (user decision): 20 sources each. Chunk 1 holds the reviews, the
  software papers and the core Runge–Kutta theory, so that the registry and
  the reading guide are built from them.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII with spaces and particles joined (`hanveiga`,
  `hedayatinasab`, `quezadadeluna`), the year that of the published issue.
  Same-author same-year papers take suffixes in publication order.
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
- Bibliography preprints (as in plasma-propulsion-simulation and
  fusion-mhd-simulation): a citation printed in pre-publication form
  (submitted, accepted, in preparation, to appear, arXiv) is its own entry,
  keyed by the year of that form, and is never folded into the published
  entry.
- Worklist: `tools/worklist.sh ode-integration`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py ode-integration/wiki --pending`.
- Lint: `python3 tools/lint_okf.py ode-integration/wiki`. It must pass
  before commit.
- Commits: `docs(ode-integration): ingest chunk N: <slugs>`.

## Status

**Chunk 4 staged 2026-10-20:** 20 sources on local time stepping,
multirate and exponential methods, NPRK, EIN and Quinpi; 80 of 118
ingested, 113 concept pages, 2766 bibliography entries. Next: chunk 5
(exponential and parallel-in-time, DeC/ADER/multiderivative, positivity
and Patankar).

**Chunk 3 committed 2026-10-19 (47079a7):** multistep and BDF methods,
IMEX for relaxation and low-Mach problems, implicit stage solvers.

**Chunk 2 committed 2026-10-19 (43bb24b):** relaxation, stabilized and
paired-explicit methods, step-size control.

**Chunk 1 committed 2026-10-19 (864b713):** scaffold (D27) and the 20
reviews, software and Runge–Kutta theory papers.
