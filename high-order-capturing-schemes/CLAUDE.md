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
  - `1997-ICASE-Shu-NASA-CR-97-206253.pdf` is the ICASE report 97-65.
    It is not the Lecture Notes in Mathematics 1697 chapter (1998),
    which is a distinct publication. The Source page identifies the
    report, not the LNM DOI.
  - Three files are arXiv preprints of published works:
    `2013-arXiv-Dumbser-…` (JCP 2013), `2014-arXiv-Guo-…`, and
    `2016-arXiv-Rathan-…`. Before ingesting each, check on Crossref
    whether a published version exists, and record the version read.
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

**Scaffolded 2026-10-08:** 62 PDFs in the archive, 0 ingested. The
worklist is authoritative.
