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
* SSP time discretization, as the time half of a capturing scheme;
* numerical boundary treatment for high-order FD (inverse Lax–Wendroff,
  weighted extrapolation);
* high-order AMR (refinement interfaces for capturing schemes);
* extensions to MHD, including how a capturing scheme coexists with a
  divergence constraint.

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
  - Not yet in the archive: Zaghi, Salvadore & Di Mascio (2023,
    doi:10.1016/j.compfluid.2023.106040) and Dumbser & Balsara (2016,
    HLLEM, doi:10.1016/j.jcp.2015.10.014).
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
