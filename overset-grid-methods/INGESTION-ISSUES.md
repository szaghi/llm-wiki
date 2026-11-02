# Ingestion issues — overset-grid-methods

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 6 — Glaubitz et al. 2027; archive complete; whole-bundle deep lint (2026-11-02)

Source (1): glaubitz-2027 (arXiv 2509.21442v2, targeted reading). 51 of
51 ingested, 53 concept pages plus the registry, 1756 bibliography
entries.

### Decisions for the human (whole night)

1. **Bundle name** `overset-grid-methods` (D31) — confirm or rename
   before committing.
2. **Reading depth of chunks 4–6** — targeted (abstract, introduction,
   structure, results, conclusions), stated on each Source page; chunks 1–2
   were read in full by reader subagents, chunk 3 from full reader notes.
   A later full reading of the 21 targeted papers would add printed-slip
   hunting and section-level claims.
3. **Reference lists of chunks 4–6** come from the Crossref deposited
   records (complete for every paper); entries without a DOI carry the
   first author only. A printed-list pass could complete the author lists.
4. **Deep lint depth** — chunks 1–2 had four-auditor deep lints; chunks 3–6
   compiler self-audits and one whole-bundle sweep (owner's no-subagent
   instruction).
5. Earlier open items: see the chunk 1–5 sections (year re-keys,
   `volkov-1968` translation fold, `reyna-1982`/`reyna-1986`, AEDC report
   year).

### Contradictions

None open in the bundle.

### Closing bibliography sweeps

`--dupes` clean; no venue/volume/page collision; the fuzzy-title sweep
found only version pairs already kept distinct (conference or report vs
journal) and Shu & Osher parts I/II.

## Chunk 5 — Kopriva et al. 2025, Wang et al. 2025, Ding et al. 2025, Luo & Fan 2025, Ding et al. 2026, Kumar et al. 2026, Wang et al. 2026, Abgrall et al. 2026, Carter et al. 2026, Hu et al. 2027 (2026-11-02)

Sources (10): kopriva-2025, wang-2025, ding-2025, luo-2025, ding-2026,
kumar-2026, wang-2026, abgrall-2026, carter-2026, hu-2027. 50 of 51
ingested, 53 concept pages plus the registry, 1706 bibliography entries.
Same recipe as chunk 4: targeted reading (stated on each Source page),
reference lists from the Crossref deposited records.

### Decisions for the human

1. **Kumar et al.'s Meakin reference** prints the year "19895" for the
   12th AIAA CFD Conference paper (1995); merged into `meakin-1995-b`.
2. **Abgrall et al. (2026)** use "overlapping meshes" for staggered meshes
   of one discretization (like Tian et al. 2024); kept and described as a
   homonym on `definitions/overset-grid.md`.
3. **Web items** of Wang et al. (2025) (STAR-CCM+, ANSYS Fluent, OpenFOAM)
   are keyed by corporate author and citing year.

### Contradictions

None open.

### Identity and versions

- kopriva-2025 read in arXiv 2405.04668v2; the others versions of record.
- hu-2027 is a 2027 issue published online in 2026.

### Bundle fit

Luo & Fan (2025) (solar-corona MHD on Yin–Yang grids) would also fit
`astrophysical-simulation-codes`; Wang et al. (2026) (particle-laden DNS)
`turbulence-modelling`. D17 candidates, no copy made.

## Chunk 4 — Bergmann et al. 2022a, Xiao et al. 2023, Devlin et al. 2023, Kochi & Ramakrishna 2023, Angel et al. 2023, Tian et al. 2024, Carlino & Boscheri 2024, Oh et al. 2024, Zhou et al. 2024, Carson et al. 2025 (2026-11-02)

Sources (10): bergmann-2022, xiao-2023, devlin-2023, kochi-2023,
angel-2023, tian-2024, carlino-2024, oh-2024, zhou-2024, carson-2025.
40 of 51 ingested, 52 concept pages plus the registry, 1290 bibliography
entries.

### Decisions for the human

1. **Reading depth (taken on your behalf, reversible).** Without reader
   subagents, the chunk-4 papers were read in a targeted way: abstract,
   introduction, section structure, main results and conclusions closely,
   derivations skimmed. Each Source page says so in `# Version read`, and
   claims are limited to the parts read. Printed slips were not hunted
   ("None recorded (targeted reading)"). A full reading can be done later
   per paper.
2. **Reference lists from Crossref.** Fragments were generated from the
   Crossref deposited reference lists (all ten papers have complete
   deposits); references with a DOI carry the full Crossref author list,
   those without carry the first author only ("and others", noted). Three
   empty deposited records in Kochi & Ramakrishna (2023) were completed
   from the printed list.
3. **Overlapping meshes in Tian et al. (2024)** are staggered meshes of one
   discretization, not overset component grids; the paper is in the archive
   and was ingested, with the difference stated on the pages.

### Contradictions

None open.

### Identity and versions

- bergmann-2022 read in HAL hal-03615757; carlino-2024 in arXiv
  2308.02686v1; carson-2025 in arXiv 2404.14592v1; the others versions of
  record.
- Zhou et al.'s own citation keyed `zhou-2024` (Mar. Struct. 93:103527) is
  a different work, re-keyed `zhou-2024-b`.

### Bundle fit

Zhou et al. (2024) (ship hydroelasticity in potential flow) and Tian et
al. (2024) (staggered LDG) are peripheral; Carson et al. (2025) and Angel
et al. (2023) are wave-propagation numerics whose overset content is
central.

### Candidate pages (not created, inline)

Virtual-face finite volumes (Devlin et al.; one source); shock-aligned
overset grids (Kochi & Ramakrishna 2023); generalized modes for
hydroelasticity.

## Chunk 3 — Chandar & Sitaraman, Hedayat et al., Wang & Stern, Bergmann et al. (b), Kopriva et al., Li & Wang, Delcour et al., Kochi & Ramakrishna, Zhao et al., Teschner & Mundt, all 2022 (2026-11-02)

Sources (10): chandar-2022, hedayat-2022, wang-2022, bergmann-2022-b,
kopriva-2022, li-2022, delcour-2022, kochi-2022, zhao-2022, teschner-2022.
30 of 51 ingested, 49 concept pages plus the registry, 1009 bibliography
entries. **Compiled in the main session without subagents** (owner's
instruction during the night): pages are leaner, and the deep lint is a
compiler self-audit (forbidden-word sweep, labelled compiler checks,
locator spot checks on the PDFs), not the four-auditor pass of chunks 1–2.
A full-bundle deep lint is due with chunk 6.

### Decisions for the human

1. **`volkov-1968`:** Bergmann et al. (2022b) cite the AMS translation
   (1970) of Volkov's Proc. Steklov paper; the resolver folded it into
   `volkov-1968`. Keep folded or make the translation a distinct entry?
2. **Deep-lint depth:** confirm that a self-audit per chunk plus one
   whole-bundle deep lint at chunk 6 is acceptable, given the token budget.

### Contradictions

None open. Recorded as qualifications: the two meanings of "conservative"
for interpolation-free coupling (Wang 1995's discrete flux balance against
Teschner & Mundt's shared points with enthalpy evidence), on
`methods/interpolation-free-overset-coupling.md`.

### Identity and versions

- hedayat-2022 was read in arXiv 1910.09315v1, which prints two authors;
  the published paper adds Akbarzadeh as second author.
- kochi-2022 (arXiv 2106.06285v1) and kopriva-2022 (arXiv 2105.04664v1)
  are preprints; delcour-2022 is an anonymised author manuscript (authors
  from Crossref).
- Key collisions re-keyed: Zhao et al.'s ref. 36 → `zhao-2022-b`; Li &
  Wang's `wang-2021` → `wang-2021-d`; Teschner & Mundt's second Wang 1995
  → `wang-1995-b` (AIAA 95-0077).

### Printed slips (recorded on the Source pages)

- Kochi & Ramakrishna: WENO weights with the sum in the denominator
  (linear as printed); element size 1/20 for 1/4; background spacing 1/400
  vs 1/200.
- Kopriva et al.: sign of the lower-right block of Eq. (126); several
  index and cross-reference slips.
- Bergmann et al. (2022b): Taylor–Green pressure $\sin2y$ for $\cos2y$;
  Eqs. (35)–(36), (40), (42), (48); negative relaxation bound from the
  printed $C_2$.
- Hedayat et al.: trilinear weights not summing to one (Eq. 14).
- Zhao et al.: distance bound $0.5h$ for $\tfrac{\sqrt2}{2}h$; dimensions in
  Eqs. (16)–(17).
- Wang & Stern: terminal-velocity correlation without the liquid density.
- Chandar & Sitaraman: cavity extents transposed.
- Li & Wang: 1.8 % for 2.02 %; "<5 %" overhead vs 6.5 % in total.

### Bundle fit

Delcour et al. (fluid–structure flutter with a commercial Chimera mesh)
and Wang & Stern (ship two-phase flow) use overset grids as an
ingredient. Kopriva et al. is pure theory of the overset problem.

### Candidate pages (not created, inline)

RBF interpolation (Sharma et al., Chandar & Sitaraman: now two sources);
flux-balance cell; WENO inter-grid reconstruction; CFDShip-Iowa;
sedimenting cylinder; oscillating cylinder (Hedayat et al., Zhao et al.);
2-D Riemann problems and shock tubes.

## Chunk 2 — Sherer & Scott 2005, Henshaw & Schwendeman 2006, Henshaw 2006, Chan 2009, Roget & Sitaraman 2014, Banks et al. 2016, Picard et al. 2021, Horne & Mahesh 2021, Sharma et al. 2021, Wang et al. 2021 (2026-11-02)

Sources (10): sherer-2005, henshaw-2006, henshaw-2006-b, chan-2009,
roget-2014, banks-2016, picard-2021, horne-2021, sharma-2021, wang-2021.
20 of 51 ingested, 40 concept pages plus the registry, 636 bibliography
entries. Deep lint A1–A4 over the chunk-2 content done. Compiled unattended
(night protocol, D31); a session usage limit interrupted the chunk midway,
and the work resumed from scratch notes without loss.

### Decisions for the human

1. **AEDC-TR-85-64** (`benek-1985-b`): Sherer & Scott and Picard et al.
   print it as April 1986; keyed 1985 as in chunk 1. Year unverified.
2. **`reyna-1982` and `reyna-1986`:** probably the same Caltech thesis
   (one printed "Part III. On Composite Meshes", one only "Thesis"); kept
   separate.
3. **`partenander-1994`:** DOI added from Crossref, which gives first page
   551; one citing list prints 555.

### Contradictions

None open. Recorded as qualifications, not conflicts: the tolerated
cell-size ratio between overlapping grids (Picard et al. at most 4; Sherer
& Scott a volume ratio of 16; Lee & Baeder 2:1 — different schemes and
measures, tabulated on `methods/overlap-optimization.md`); exposed points
forbidden by a hole-motion limit (Meakin & Suhs) against filled after the
move (Henshaw & Schwendeman), on `definitions/exposed-point.md`; Picard et
al. against Pärt-Enander & Sjögreen (not ingested) on refining the patch.

### Identity and versions

- picard-2021 was read in the HAL deposit hal-03779335v1 (revised author
  manuscript); the others are versions of record.
- Keys printed with an ingested slug for a different work were re-keyed:
  Henshaw & Schwendeman's `lee-2003` (Lee & LeVeque) → `lee-2003-b`;
  Henshaw's `henshaw-1994` (Henshaw, Kreiss & Reyna, Comput. Fluids) →
  `henshaw-1994-e`; Wang et al.'s two other 2021 papers → `wang-2021-b`,
  `-c`. Roget & Sitaraman's garbled ref. [11] is Brown, Henshaw & Quinlan
  (1999), Overture (`brown-1999`, Crossref).
- Sharma et al.'s ref. [64] is Noack (2007), a direct-cut hole-cutting
  paper, not SUGGAR.

### Printed slips (recorded on the Source pages)

- Henshaw (2006, Maxwell): $\alpha_1=-1/6$ printed on p. 1738, the
  expansion gives $-1/24$ (consistent with Eq. (5.12)); Lemma 8.1 factor
  2; $D^{(4)}_{r_m}$ coefficient $\tfrac1{12}$ for $\tfrac16$; $256^3$ printed
  1.78e7; Table 1 $E_x$ rate 4.40 against 4.35 from the printed errors.
- Henshaw & Schwendeman (2006): figure time labels; exposed-point test
  printed with "<" where the paper's Fig. 4 needs "≤"; §7.1 spacing off by
  a factor 10 against the grid definitions (which value is wrong is not
  decidable from the paper).
- Banks et al. (2016): post-shock pressure printed 1.191 (= $p/\rho$),
  1.805 from the shock relations; solid-grid domain of zero width.
- Picard et al. (2021): Table 1 order 1.595 for 1.549; Table 5 0.47 % for
  0.412 %; §4.4 domain ranges swapped.
- Horne & Mahesh (2021): Algorithm 1 update sign; Taylor–Green pressure
  sign; speed-ups 15–50× (conclusion) against 8–56× (§4.2.2).
- Sharma et al. (2021): Algorithms 1–2 update sign; Eq. (27) bracket;
  $O(h^{-2})$ corrector growth stated, Table 1 gives an exponent near 1.
- Sherer & Scott (2005): Eq. (17) exponent; B-spline support; figure
  references. Roget & Sitaraman (2014): section numbering, 68 % for 67 %.

### Bundle fit

Wang et al. (2021) (propeller-wake turbulence with a rotating grid) and
Banks et al. (2016) (fluid–structure interaction) use overset grids as an
ingredient; Wang et al. (2021) would fit `turbulence-modelling` (D17
candidate, no copy made). Henshaw (2006) is an electromagnetics paper
whose high-order composite-grid content is central here.

### Candidate pages (not created, inline)

PUNDIT and TIOGA; alternating digital tree and exact inverse map; collar
and zipper grids, object X-rays, off-body Cartesian grids (Chan); added-mass
partitioned algorithm; symmetric curvilinear Laplacian and compatibility
boundary conditions (Henshaw 2006); RBF fringe interpolation and overset
Schwarz coupling (Sharma et al.; chunk 3 brings a second RBF source);
PEC-sphere scattering.

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
