# Bundle law — astrophysical-simulation-codes

Domain: the numerical design of production simulation codes for
astrophysical and compressible flows, and of the physics modules they
carry. Scope by user decision (2026-10-12, classes 7 and 8 of the ADAM
paper collection, "codes of both kinds"):
* astrophysical (magneto)hydrodynamics codes and frameworks — Athena,
  Athena++, AthenaK, PLUTO, Castro, Enzo, RAMSES-RT, GAMER, Cholla,
  IDEFIX, Quokka, GRaM-X and their peers — their solvers, mesh and AMR
  design, time stepping, and verification;
* physics modules as numerical methods: self-gravity (Poisson solvers,
  energy-conserving coupling), sink particles and the Jeans condition,
  radiative cooling and chemistry, radiation hydrodynamics (moment
  methods), general equations of state, relativistic MHD (primitive
  recovery), pseudo-Newtonian potentials;
* code-comparison and application papers, for what they establish about
  the codes;
* GPU and performance-portable frameworks for compressible flow, astro or
  not (Kokkos- and CUDA-based astrophysics codes; STREAmS, Neko, GPU AMR
  for CFD), including parallel efficiency and data layout.

The bundle is about how codes work and what they are shown to do, not
about astrophysical results for their own sake. It is a standalone second
brain, independent of every other bundle and agnostic of every other
repository (`DECISIONS.md` D12, D17, D18). Works another bundle has
ingested (Athena++, PLUTO, Castro, STREAmS, GPU AMR) are re-ingested here
from scratch for their code-design content, with no links across bundles.

## Corpus

- Primary archive: `~/papers/mosaic/astrophysical-simulation-codes/*.pdf`
  (read-only; Layer 1), self-contained per D17. Filenames follow
  `year-journal-firstauthorsurname-doi.pdf` with the published DOI
  stripped of punctuation; treat the filename as a hint and verify
  identity against page 1 and Crossref.
- Scaffolded with 35 PDFs (2026-10-12):
  - 29 from the ADAM paper collection: 21 copied from `~/papers/adam`
    (most are arXiv preprints of the published works; each Source page
    records the version read) and 8 moved from `~/papers/re-download/`
    (krumholz-2004, federrath-2010, skinner-2013, kim-2017,
    villasenor-2021, mullen-2021, ohlmann-2016, jansson-2024).
  - The collection's keys use first names (emilio-2013, joakim-2013, …);
    slugs here use surnames and issue years: tejeda-2013, rosdahl-2013,
    bryan-2014, katz-2016, siegel-2018, coleman-2020, kastaun-2021,
    mathew-2021, wibking-2022, shankar-2023, tomida-2023, caddy-2024,
    rossazza-2026.
  - `2024-arXiv-Stone-…` (AthenaK, arXiv:2409.16053v1) was published as
    ApJS 283:27 (2026, doi:10.3847/1538-4365/ae3717; found on Crossref
    at ingestion, batch 3), so its slug follows the published year:
    `stone-2026`. The archive file keeps its preprint name.
  - 6 copied from sibling archives (D17): Athena (stone-2008), Athena++
    (stone-2020), PLUTO AMR (mignone-2012), Castro (almgren-2010) and GPU
    AMR (zaghi-2023) from div-free-amr; STREAmS (bernardini-2021) from
    high-order-capturing-schemes. These are the frameworks the class-7
    papers extend.
  - The `&` in the A&A filename needs quoting in shells.
- Truelove et al. (1997, the Jeans condition, doi:10.1086/310975): the
  collection held an HTML page; the user's manual download was filed as
  `1997-ApJL-Truelove-101086310975.pdf` (2026-10-13).

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks.
- Software pages carry the weight here: one `Software` page per code that
  a source presents as a substantive contribution, with its solvers, mesh,
  parallelization and verification, each claim cited.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII, the year that of the published issue (as in the
  other bundles). An undated citation takes the citing date, noted in the
  entry.
- Batches: about 10 sources per batch, staged as one unit with one commit
  message naming every slug, read by parallel subagents into scratch
  notes and compiled by the main session (the mode the user authorized
  for high-order-capturing-schemes, carried over). Reference lists are
  merged with `tools/bib_merge.py` (D16), with the venue check, the
  same-key vol:page check and the per-fragment final-key collision check
  before `--write`, then `--dupes` and a fuzzy-title sweep.
- Ingestion order: frameworks first (Athena, Athena++, PLUTO, Castro,
  Enzo), so early papers define the solver and mesh vocabulary; then the
  module papers; then the GPU codes; then comparisons and applications.
- Worklist: `tools/worklist.sh astrophysical-simulation-codes`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py astrophysical-simulation-codes/wiki --pending`.
- Lint: `python3 tools/lint_okf.py astrophysical-simulation-codes/wiki`.
  It must pass before commit.
- Commits: `docs(astrophysical-simulation-codes): ingest <source-slug>`.

## Status

**Frontier batch 7 staged 2026-10-13:** evans-1988 and sod-1978, copied
from sibling archives (D17); 41 of 41. No contradiction opened. Deep lint:
6 ingestions since #3.

**Frontier batch 6 staged 2026-10-13:** the bundle's most-cited works not
yet ingested, whose PDFs were already in sibling archives and were copied
into this bundle's archive (D17): colella-1984 (PPM), berger-1989 and
gardiner-2005 (39 of 39). New page: methods/ppm. No contradiction opened.
Deep lint: 4 ingestions since #3.

**Truelove et al. (1997) staged 2026-10-13:** the manual download was
filed and ingested (`truelove-1997`, 36 of 36). It opened a contradiction
on the Jeans criterion's scope. Deep lint: 1 ingestion since #3.

**Batch 4 staged 2026-10-12:** all 35 archived sources ingested (the
comparisons and applications: porth-2019, kim-2017, villasenor-2021,
ohlmann-2016, bai-2017, mathew-2021). Deep lint #3 (35 ingestions) ran
with this batch. Still outside the archive: Truelove et al. (1997), which
needs a manual download. The next deep lint is due after 10 more
ingestions.

**Batch 3 staged 2026-10-12:** 29 of 35 archived sources ingested (the
GPU codes: lesur-2023, caddy-2024, stone-2026, rossazza-2026,
wibking-2022, shankar-2023, zaghi-2023, bernardini-2021, jansson-2024).
Next: comparisons and applications (porth-2019, kim-2017,
villasenor-2021, ohlmann-2016, bai-2017, mathew-2021). Deep lint: 9
ingestions since #2, with a batch audit; #3 is due with the next batch.

**Batch 2 staged 2026-10-12:** 20 of 35 archived sources ingested (the
physics modules: krumholz-2004, federrath-2010, townsend-2009, smith-2017,
jiang-2013, siegel-2018, kastaun-2021, tejeda-2013, coleman-2020,
katz-2016). Next: the GPU codes (lesur-2023, caddy-2024, stone-2024,
rossazza-2026, wibking-2022, shankar-2023, zaghi-2023, bernardini-2021,
jansson-2024), then comparisons and applications. Deep lint #2 (20
ingestions) ran with this batch as its audit; the next is due after 10 more.

**Batch 1 staged 2026-10-12:** 10 of 35 archived sources ingested (the
frameworks: stone-2008, stone-2020, mignone-2012, almgren-2010, bryan-2014,
zhang-2018, rosdahl-2013, skinner-2013, tomida-2023, mullen-2021). Next:
the module papers (sinks, Jeans, cooling, chemistry, self-gravity energy,
relativistic primitive recovery, EOS, pseudo-Newtonian potential), then
the GPU codes, then comparisons and applications. The first deep lint ran
with this batch (see `log.md`); the next is due after 10 more ingestions.
