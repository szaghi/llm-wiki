# Bundle law — high-order-capturing-schemes

Domain: high-order shock-capturing schemes for hyperbolic conservation laws.
Scope is broad by user decision (2026-10-08):
* ENO and WENO, finite difference and finite volume, and their variants:
  mapped (WENO-M), WENO-Z, adaptive-order (WENO-AO), targeted ENO (TENO),
  central WENO (CWENO), multi-resolution and compact/hybrid schemes, and
  GP-WENO;
* monotonicity-preserving (MP) and PPM reconstruction;
* ADER and space–time predictors, and a posteriori (MOOD/subcell) limiting
  of high-order schemes, including WENO-limited DG;
* positivity-preserving and physical-constraint-preserving limiters;
* SSP time discretization, as the time half of a capturing scheme, and
  time integration more broadly (Runge–Kutta theory, low storage,
  step-size control, multistep, relaxation and positivity adaptation;
  added by user decision, 2026-10-12, with the time-integration class of
  the ADAM paper collection; weather leapfrog filters were left out);
* numerical boundary treatment for high-order FD (inverse Lax–Wendroff,
  weighted extrapolation), and immersed-boundary and cut-cell
  (embedded-boundary) methods with their small-cell cures (added by user
  decision, 2026-10-12, with the immersed-boundary class of the ADAM paper
  collection);
* high-order AMR (refinement interfaces for capturing schemes);
* extensions to MHD, including how a capturing scheme coexists with a
  divergence constraint;
* Riemann-solver design as it bears on capturing schemes: numerical shock
  instabilities (carbuncle, odd–even decoupling, slowly moving shocks) and
  their cures, HLL-type solvers with sub-structure (HLLEM/HLLI), low-Mach
  fluxes and well-balancing (added by user decision, 2026-10-12, when the
  Riemann-solver class of the ADAM paper collection was assigned here).

This bundle is a standalone second brain on this field. It is independent
of every other bundle and agnostic of every other repository (see
`DECISIONS.md` D12, D17). Works that another bundle has also ingested
are re-ingested here from scratch: a separate Source page, read for this
bundle's subject, written in this bundle's notation. There are no links
to another bundle.

## Corpus

- Primary archive: `~/papers/mosaic/high-order-capturing-schemes/*.pdf`
  (read-only; Layer 1). It is self-contained: works shared with another
  bundle's archive are copied in, not referenced (D17).
- Filenames follow `year-journal-firstauthorsurname-doi.pdf`. The DOI is
  punctuation-stripped; preprints use `arXiv` as the journal and the
  arXiv DOI, and reports carry their report number. Treat the filename as
  a hint: verify identity and metadata against page 1 and Crossref.
- Known archive notes:
  - `1994-JCP-Liu-…` (Liu, Osher & Chan, WENO) is an image-only scan:
    `pdftotext` yields nothing. Read it visually, page by page, and never
    guess an equation.
  - `1997-ICASE-Shu-NASA-CR-97-206253.pdf` is the ICASE report 97-65,
    the report form of the Lecture Notes in Mathematics 1697 chapter
    (1998, same title). Its slug is `shu-1998` and its resource the LNM
    DOI; the Source page records that the report was read (decided at
    batch 1, reversing the scaffold note, for consistency with the slug
    rule below).
  - `1988-JCP-Shu-…` is ICASE Report 87-33 (May 1987), not the typeset
    JCP article; `1996-JCP-Jiang-…` is a 40-page preprint. Both are
    ingested under their published slugs with the version recorded.
  - Files that are arXiv preprints or author manuscripts of published
    works: `2013-arXiv-Dumbser-…` (JCP 2013), `2014-arXiv-Guo-…`,
    `2016-arXiv-Rathan-…`, and — despite journal-style names —
    `2013-JCP-Hu-…` (arXiv:1203.1540v5), `2024-CAMC-Balsara-…` (author
    manuscript of CAMC 7, 2025), `2016-JSC-Baeza-…` (accepted
    manuscript, arXiv:2501.17106), `2014-JCP-Dumbser-…`
    (arXiv:1406.7416v3) and `2015-CompFluids-Zanotti-…`
    (arXiv:1412.0081v2), `2016-JCP-Chen-…` (accepted manuscript) and
    `2018-CompFluids-Owen-…` (author manuscript). `2025-arXiv-Wang-…`
    (arXiv:2511.08335v1) has no published version on Crossref; a later JCP
    paper by four of its five authors, with a different title, is not
    taken as the same work. Batch 6 added `2009-JCP-Balsara-…` (author
    manuscript, most likely the submitted version), `2010-JCP-Mignone-…`
    (arXiv:1001.2832v2), `2014-JCP-Christlieb-…` (arXiv:1309.3344v2),
    `2024-JCP-Berta-…` (arXiv:2310.11831v4) and `2024-SISC-Ding-…`
    (arXiv:2305.14820v1). For any future file, check on Crossref whether a
    published version exists, and record the version read.
  - Slugs reserved for archived works whose bare key a same-year homonym
    already holds (decided at batch 3): Balsara 2009 divergence-free
    reconstruction + WENO (JCP 228:5040) → `balsara-2009-b` (ADER-WENO,
    JCP 228:2480, is `balsara-2009`); Balsara & Kim 2016 subluminal RMHD
    (JCP 312:357) → `balsara-2016-b` (WENO-AO is `balsara-2016`). The
    bare keys `balsara-2023` (curl-constraint paper, CAMC 5:235),
    `mignone-2010` (GLM-MHD FD, JCP 229:5896) and `chen-2016` (Chen, Tóth
    & Gombosi) were kept free for their archived files.
  - Batch 8 files (all preprints or author manuscripts; each Source page
    records the version):
    - `2019-JCP-Simon-…` is arXiv:1803.04922v1;
    - `2019-IJNMF-Simon-…` is arXiv:1806.03187v1, whose arXiv record wrongly
      carries the JCP DOI;
    - `2015-A&A-Miczek-…` is arXiv:1409.8289v2;
    - `2021-A&A-Edelmann-…` is arXiv:2102.13111v2;
    - `2021-CAMWA-Xie-…` is arXiv:1901.01866v3, with a different fifth
      author from the published record;
    - `2016-JCP-Dumbser-…` is the revised author manuscript (Trento IRIS);
    - `2019-JCP-NavasMontilla-…` is an author manuscript (Zaragoza
      Zaguan);
    - `2019-AIAAJ-Kitamura-…` is the R1 author manuscript (Yokohama NU).

    The `&` in the A&A filenames needs quoting in shells.
  - Batch 9 files:
    - `2020-SISC-Ranocha-…` is arXiv:1905.09129v4;
    - `2021-CAMCoS-Nusslein-…` is arXiv:2005.06268v2;
    - `2016-SINUM-Hadjimichael-…` is arXiv:1504.04107v2;
    - `2019-JSC-Higueras-…` is arXiv:1809.04807v1;
    - `2022-CAMC-Ranocha-…` is the publisher PDF (open access);
    - `1895-MathAnn-Runge-…` is the publisher scan (German, image only).
  - Batch 10 files:
    - `2002-ActaNumer-Peskin-…` is the published article;
    - `2021-JCP-Berger-…` is arXiv:2005.05734v1 (collection key "marsha-2020");
    - `2022-JCP-Giuliani-…` is arXiv:2112.12360v2;
    - `2024-JCP-BarrioSanchez-…` is arXiv:2309.06372v1;
    - `2022-JCP-Natarajan-…` is arXiv:2108.00126v1;
    - `2020-CompFluids-Seshadri-…` is the author manuscript;
    - `2024-CompFluids-Baskaya-…` is arXiv:2309.09657v1.
  - Not yet in the archive: Zaghi, Salvadore & Di Mascio (2023,
    doi:10.1016/j.compfluid.2023.106040). A repository copy now sits in
    `~/papers/re-download/`; the user assigned the ADAM AMR-framework class
    to div-free-amr (2026-10-12).
- Future sources of any kind land per repo law (capture to `raw/` if
  undurable).

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative for
  every concept page. Extend it, and log the extension, before writing math
  that needs a symbol it lacks.
  - Two collisions are settled by the registry: $h$ is the grid spacing,
    so Shu–Osher's flux function is $\mathcal{H}$; $\alpha$ is the
    Lax–Friedrichs speed, so unnormalized weights are $\tilde\omega_k$.
- **Keys and slugs.** Every bibliography key and every Source slug is
  `firstauthor-year[-b, -c, …]`, with the first author's surname in
  lowercase ASCII (no spaces or apostrophes). The year is that of the
  published version — the issue (volume) year when an article appeared
  online first, as in the standard "vol (year) pages" citation (decided
  at batch 3: `reyes-2018`, `balsara-2025`); an ingested source takes the
  bare key and a cited homonym takes a suffix. An undated citation takes the citing date,
  noted in the entry. One rule for both makes later citations of an
  ingested work land on its key without aliases.
- **Batches.** The user authorized autonomous ingestion in batches of 10
  (2026-10-08), each staged as one unit with a single commit message
  naming every slug, reviewed by the user between batches. A batch's
  reference lists are merged with `tools/bib_merge.py` (D16) and closed
  with `--dupes` plus the venue and fuzzy-title sweeps. Before `--write`,
  also compare the printed vol:page of every same-key merge with the entry
  it lands on, because `bib_merge` flags same-key conflicts only for
  dissimilar titles (decided at batch 4, after it found series siblings
  such as Cockburn & Shu 1989 II/III merged under one key).
- Ingestion order for the initial corpus: foundations first, so that early
  papers define the concepts and later papers exercise the merge path.
  1. Origins: PPM, ENO (Harten et al. 1987; Shu & Osher 1988, 1989).
  2. WENO: Liu–Osher–Chan 1994, Jiang–Shu 1996, then Shu's ICASE notes.
  3. Variants: MPWENO, MP5, CWENO, compact hybrids, WENO-M, WENO-Z,
     bandwidth-optimized and central-upwind weights, TENO, WENO-AO, and
     the newer FD-WENO and weight designs.
  4. Time and positivity: SSP, the Zhang–Shu limiters and their
     successors.
  5. Multi-D FV and ADER, a posteriori limiting, and WENO-limited DG.
  6. Boundaries: ILW and weighted extrapolation.
  7. High-order AMR.
  8. MHD.
  9. Reviews (Shu 2009, 2020) and codes.
- Worklist: `tools/worklist.sh high-order-capturing-schemes` (corpus minus
  existing Source pages).
- Bibliography: `wiki/bibliography.bib` (canonical) plus the generated
  `wiki/bibliography.md`, per repo law (D15). Pending reference-list
  extractions:
  `python3 tools/bib_to_md.py high-order-capturing-schemes/wiki --pending`.
- Lint: `python3 tools/lint_okf.py high-order-capturing-schemes/wiki`. It
  must pass before commit.
- Commits: `docs(high-order-capturing-schemes): ingest <source-slug>`.

## Status

**Batch 12 staged 2026-10-13:** 111 of 111 archived sources ingested (the
second half of the user's manual downloads): the shock-diffraction and
reflection papers bryson-1961, kleine-1995, kleine-2006, gnani-2014,
zhang-2017-c, brahmi-2020, brahmi-2020-b, martyushov-2016, yeom-2010 and
tsai-2012, plus Toro's book (toro-1997; 1st edition, scoped read of
Ch. 4, 6, 9–12 and §§17.1–17.2, full reference list). All are publisher
versions; bryson-1961, kleine-1995 and toro-1997 are scans read from page
images where the OCR layer fails. A deep lint (11 ingestions since the
last) ran with this batch. Still missing: Mittal et al. (2008).

**Batch 11 staged 2026-10-13:** 100 of 111 archived sources ingested.
From the user's manual downloads of 2026-10-13 (the ADAM benchmarks and
experiments class plus missing papers of classes 2, 3 and 9): sod-1978,
woodward-1984, brio-1988, dai-1994, balsara-1999, falcovitz-1997,
deng-2019-b, balsara-2017-b, vanleer-2005 and poinsot-1992. A deep lint
(100 ingestions) ran with this batch. Next (batch 12): the shock-diffraction
papers bryson-1961, kleine-1995, kleine-2006, gnani-2014, zhang-2017-c,
brahmi-2020, brahmi-2020-b, martyushov-2016, yeom-2010 and tsai-2012, plus
Toro (1997, toro-1997, scoped read). Still missing: Mittal et al. (2008).
Slugs: the archived Balsara & Nkonga (2017, JCP 346:25) is
`balsara-2017-b` and Deng, Boivin & Xiao (2019) is `deng-2019-b`, because
the bare keys belong to same-year homonyms (the batch-3 rule); Zhang et al.
(2017, Shock Waves) will be `zhang-2017-c`.

**Batch 10 staged 2026-10-12:** 90 of 90 archived sources ingested. The
batch took the immersed- and embedded-boundary class of the ADAM paper
collection: peskin-2002, berger-2021, giuliani-2022, barriosanchez-2024,
natarajan-2022, seshadri-2020 and baskaya-2024 (Secchi's MHD
well-posedness note deferred as out of scope). With batch 9 that is 13
ingestions since the last deep lint, so a deep lint ran with this batch
(see `log.md`). Remaining ADAM class assigned here: benchmarks and
experiments (no PDFs yet).

**Batch 9 staged 2026-10-12:** 83 of 83 archived sources ingested. The
batch took the time-integration class of the ADAM paper collection:
ranocha-2020, ranocha-2022, nusslein-2021, hadjimichael-2016,
higueras-2019 and runge-1895. Runge (1895) has no reference list, so it
stays on `--pending` by design (lint warning). Deep lint: 6 ingestions
since the 2026-10-12 lint; the next is due after 4 more. Remaining ADAM
classes assigned here: immersed and embedded boundaries, benchmarks and
experiments.

**Batch 8 staged 2026-10-12:** 77 of 77 archived sources ingested. The
batch took the Riemann-solver and shock-anomaly class of the ADAM paper
collection: simon-2019, simon-2019-b, miczek-2015, edelmann-2021,
xie-2021, dumbser-2016, navasmontilla-2019 and kitamura-2019. The deep lint
for batches 7–8 ran on 2026-10-12 (see `log.md`); the next is due after
10 further ingestions. Remaining ADAM classes assigned here (time integration, immersed
and embedded boundaries, benchmarks and experiments) await later batches.

**Batch 7 staged 2026-10-09:** 69 of 69 archived sources ingested. The batch
closed gaps found against the ADAM paper collection: ryu-1995 (arXiv preprint,
no figures or tables), balsara-2001, mignone-2010-b (arXiv v1), zhang-2017
(author's revised preprint), balsara-2017-d (NSF PAR author manuscript, not
arXiv v1), derigs-2018 (arXiv v3) and tomida-2026 (arXiv v2). Their archive
copies came from the div-free-amr archive (D17), the ADAM collection, or a
fresh download where the collection held HTML error pages.

**Batch 6 staged 2026-10-08:** all 62 archived sources ingested (batch 1: origins, ENO,
WENO, MP, CWENO, MPWENO; batch 2: mapped WENO, WENO-Z, WENO-CU6, TENO,
WENO-AO/ZQ, bandwidth-optimized and hybrid compact schemes; batch 3: SSP
theory, 3D FV-WENO, positivity limiters, compact and GP WENO, AFD-WENO,
single-step MHD and divergence-preserving AFD-WENO; batch 4: ADER and
polynomial WENO, WENO-limited and a posteriori subcell-limited DG, ADER
AMR, energy-stable WENO boundary closures, inverse Lax–Wendroff and
weighted extrapolation; batch 5: the rest of the ILW line (sign-changing
wind, conservation, moving bodies, fluid–structure interfaces),
block-structured high-order AMR in FV and FD, and FD-WENO for MHD;
batch 6: MHD divergence treatments (divergence-free reconstruction, GLM,
high-order and upwind CT, trace projection with provable positivity),
relativistic MHD, curl-preserving reconstruction, the STREAmS code, and
Shu's 2009 and 2020 surveys). Deep lints ran at batches 3, 4, 5 and 6, and
the closing bibliography sweeps (`--dupes`, venue, fuzzy title) ran over
the whole corpus after batch 6. A new source added to the archive is
ingested per source, with a hand-edited `.bib` (repo law), and a deep
lint is due every 10 further ingestions. The worklist is authoritative.
