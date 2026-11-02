# Ingestion issues — overset-grid-methods

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 1 — founding papers: Benek et al. 1983 and 1985, Meakin & Suhs 1989, Chesshire & Henshaw 1990, Henshaw 1994, Wang 1995, Lee & Baeder 2003, Rogers et al. 2003, Kageyama & Sato 2004, Noack 2005 (2026-11-02)

Sources (10): benek-1983, benek-1985, meakin-1989, chesshire-1990,
henshaw-1994, wang-1995, lee-2003, rogers-2003, kageyama-2004,
noack-2005. 10 of 51 ingested, 28 concept pages plus the registry, 209
bibliography entries. Deep lint A1–A4 over all pages done. Compiled
unattended (night protocol, D31).

### Decisions for the human

1. **Bundle name.** The compiler named the bundle `overset-grid-methods`
   (the archive is `overset-chimera`). Rename before the first commit if
   you prefer another name (directory, `bundle.toml`, D31, commit
   messages).
2. **Bibliography year re-keys.** Citations printed with a wrong year were
   keyed by the true year: `ying-1986` (Meakin & Suhs print AIAA Paper
   86-2179 dated 1989; Crossref), `roe-1981` (printed 1983; JCP 43:357,
   Crossref), `steger-1983` (Benek et al. 1985 and Wang 1995 print 1985
   for the same ASME FED-Vol. 5 chapter), `baker-1988` (printed 1989,
   same venue and page). The last two are not Crossref-checked. Confirm.
3. **Unverified printed venue.** Henshaw (1994) ref. [12], Harlow & Welch,
   is printed "J. Comput. Phys. 8, 2182"; kept as printed, not checked.
4. **Benek 1985 AEDC report** (AEDC-TR-85-64) is keyed `benek-1985-b`;
   chunk 2 shows another citing list printing April 1986 for it. Year
   unverified.

### Contradictions

None open. One drafting-time contradiction was reclassified by the deep
lint: whether hole points must be excluded from the solution update
(Benek et al. 1983, 1985 and Meakin & Suhs 1989, who blank holes in an
implicit approximate-factorization solve with a one-layer fringe, against
Lee & Baeder 2003, who argue a fringe thicker than the information travel
per step makes blanking unnecessary). The sources answer it for different
solvers and fringe widths; it is a qualification on
`definitions/point-classification.md` and `methods/implicit-hole-cutting.md`.

### Identity and versions

- All 51 archive files are distinct works whose filename titles match
  Crossref. Sixteen carry no DOI on page 1 (the AIAA conference papers of
  1983–2005 and several accepted manuscripts) and were identified from
  title and author.
- kageyama-2004 was read in its arXiv version physics/0403123v1; locators
  are those of the preprint. The venue is the Crossref record, G-cubed
  5(9):2004GC000734.
- benek-1983, benek-1985, meakin-1989, lee-2003, chesshire-1990,
  henshaw-1994 and wang-1995 are scans (most with no usable text layer
  for the equations); the readers read the equations from the page images.

### Printed slips (recorded on the Source pages, `# Printed slips`)

- Noack (2005): Table 2 rows sum one $81^3$ grid short of the printed
  totals; the C130 setup parts sum to 349 s, printed 335 s; page-1
  conference date "2006".
- Rogers et al. (2003): the cell-difference parameter as printed is below
  3 and can be negative, while the text calls 0 the best and says values
  run "to very large"; abstract speedup 30 against 33 in the body.
- Lee & Baeder (2003): the inside test printed on p. 10 is identically
  zero; Fig. 10 shows the working test.
- Meakin & Suhs (1989): sign of the first time-metric term; $\hat{\mathbf q}$
  without $J^{-1}$; both difference operators called "forward".
- Chesshire & Henshaw (1990): nineteen slips (pseudo-code Steps 5–6,
  determinant double count, Table I $d=0.5$ for $0.5h$, Tables V, VIII, IX
  arithmetic, nondimensionalization).
- Henshaw (1994): $D_4$ second-derivative denominator 24 for 12; Eq. (17)
  second-order coefficients halved; Table I pressure rate 4.0 printed,
  4.30 refitted; sphere grid 47,550 points in the text against 17,550 in
  Table VIII (undecided).
- Wang (1995): Eq. (9) sign; Eq. (16) interval bound; Table I imbalance.
- Kageyama & Sato (2004): Eq. (3) argument order; a silent sign change in
  Eq. (21); "$\mathsf P^2=1$" in Eq. (25) false as a matrix identity.
- Benek et al. (1983): Fig. 13 legend "G12" for $G_{21}$. Benek et al.
  (1985): fuselage contour formula inconsistent; figure numbers in Fig. 5
  one too low.

### Bundle fit

All ten papers are overset methods proper. Kageyama & Sato (2004) is a
geophysics grid paper; it belongs here by construction (two overlapping
component grids) and also touches spherical-grid literature that no other
bundle holds.

### Candidate pages (not created, inline)

Cartesian hole map and tree-based hole cutting (Rogers et al., Noack;
needs a second ingested source describing it); hole-motion constraint
(Meakin & Suhs; chunk 2 brings Henshaw 2006's exposed points); collar
grids; Schwarz-alternating lineage; Wannier flow (three pages describe
it); CGINS (one source); pressure-Poisson boundary condition.
