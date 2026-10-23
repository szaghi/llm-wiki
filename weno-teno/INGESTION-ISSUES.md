# Ingestion issues — weno-teno

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 8 — multi-resolution WENO, TENO and THINC variants, DG limiters, MHD and shallow-water schemes (2026-10-23)

Sources (20): chen-2024, chudzik-2024, delgrosso-2024, dematte-2024,
ding-2024-b, fan-2024, kolluru-2024, liang-2024, lin-2024-b, lin-2024,
naudet-2024, nguyen-2024, teissier-2024, wakimura-2024, wei-2024,
zhang-2024-b, zhang-2024-c, zhang-2024, zuo-2024-b, zuo-2024. 159 of 207
ingested, 200 concept pages plus the registry, 4666 bibliography entries.

### Decisions for the human

1. **New open contradiction — order of TENO at a second-order critical
   point** on [targeted ENO](wiki/methods/targeted-eno.md): Fu (2023,
   §3.1, Eq. (18)) states that the TENO order "does not degenerate even
   for the test function with a second-order critical point"; Zhang et
   al. (2024b, Eqs. (13), (15), Table 3) measure rate 2 for TENO6 at such
   a point with a global indicator of the same form ($C=1$, $q=6$,
   $\epsilon=10^{-40}$, $C_T=10^{-7}$). Checked in both PDFs; *Open*.
   Residual doubt: Zhang et al. measure the rate of the reconstructed
   derivative, Fu does not say what was measured.
2. **Priority of symmetry preservation for two-phase flow:** Wakimura et
   al. (2024, App. A; received 24 Feb 2024, online 7 Jun 2024) write that
   no symmetry-preserving method for two-phase flow had been proposed;
   Zhang et al. (2024a; received 7 Aug 2023, online 28 Nov 2023) call
   their THINC "symmetry-preserving" (§5) on the five-equation model and
   show it on a Mach 10 water column (Fig. 13), and Wakimura et al. do
   not cite them. The pages state the dates and the two statements only;
   not entered as a contradiction (a claim of novelty, not of fact about
   a method).
3. **Zuo & Zhu (2024a) and (2024b), same authors and journal, different
   indicators:** of their 216 accuracy-table error entries, 15 differ
   (all in the seventh- and ninth-order part of Table 3.2, by at most 3 %
   relative); Tables 3.3–3.4 agree digit for digit; the six MR-WENO CPU
   times for the double Mach reflection and Taylor–Green vortex are
   identical. Recorded as counts on both Source pages, without an
   explanation.
4. **Still open from chunks 1–7:** the archive re-download (Feng 2026,
   Li 2024, Wu 2023); the open contradictions (TENO $\tau_K$,
   conservation of WCNS, entropy-filter tolerance, cost of WENO-Z against
   mapped WENO); wrong-year keys; the berberich and karniadakis pairs;
   the label convention; book printings.
5. **Bibliography rulings to confirm:** `micchelli-1984` and
   `micchelli-1986` kept distinct; book printings folded into the first
   printing in line with the chunk-2 pending ruling (`whitham-2011` →
   1974, `leveque-2004` → 2002, `hesthaven-2017`/`-2008` → 2018/2007).
6. **Bundle fit (no D17 copy made):** teissier-2024 (forced MHD
   turbulence, astrophysical motivation) and dematte-2024 (magnetically
   dominated visco-resistive MHD) also fit astrophysical-simulation-codes;
   kolluru-2024 (spectral relaxation and purging of tygers) is mainly a
   spectral-methods paper.

### Identity and metadata

- Versions read that are not the version of record: arXiv preprints
  fan-2024 (2409.09632v1), kolluru-2024 (2402.17688v2), nguyen-2024
  (2310.01196v1), teissier-2024 (2306.09856v2, earlier title "High-order
  finite-volume integration schemes for subsonic MHD", Teissier & Müller;
  identity through its arXiv DOI field and Crossref); HAL preprint
  delgrosso-2024 (hal-04177987v1). The other 15 are versions of record.
- Citation labels: Zuo & Zhu 2024a/b (`zuo-2024`, `zuo-2024-b`), Zhang et
  al. 2024a/b (`zhang-2024`, `zhang-2024-b`; `zhang-2024-c` is Zhang &
  Zhu), Liang & Fu 2024a/b (`liang-2024`, `liang-2024-b`) applied on every
  page except the append-only log. Ding & Wu (2024) stays bare until
  `ding-2024` (chunk 9) is ingested.
- Zuo & Zhu's ref. [28] (Wang, Tian, Zhu & Zhao 2023) is `wang-2023-d`
  (not ingested), not the ingested `wang-2023-c`; corrected on the
  troubled-cell page and both Source pages.
- Zhang et al. (2024b) credit their sensor coefficients to S. Li et al.
  (J. Sci. Comput. 2022), not to the ingested Li et al. (2023b); both
  attributions are recorded as printed.
- Crossref corrections in the merge: miczek-2015, leidi-2022-b (published)
  against leidi-2022 (preprint), ha-2013-b vol. 51, kuzmin-2013-b
  pp. 1178–1190, shu-2005 pp. 1–27, markert-2023 = markert-2021
  online-first. The DOIs that wakimura-2024 prints for refs. [21] and
  [26] resolve to other works and were not adopted.

### Printed slips (the Source pages list them in full)

- zhang-2024-b: Eqs. (11), (21), (23), (31), (47) and the $G_1$
  condition; band limit 1.732 against 1.726.
- zhang-2024: Eq. (8) deformation tensor; §3.3 $\rho c^2$ against Eq.
  (16); a 0.064 m cylinder in a 0.03 m domain; Tables 6–7 post-shock
  states.
- lin-2024: Table 1 rates (2.11 and 2.47 recomputed, 1.11 and 2.74
  printed); Eq. (50) upper case; Eqs. (5), (22), (41), (45), (63);
  $\lambda_i$ of Eq. (52) undefined. The Eq. (50) middle ramp
  $\tfrac12-\tfrac12\sin(\cdot)$ is the one Pazner prints (Eq. 69) and runs
  from 1 to 0, the reverse of the outer cases (labelled compiler check).
- naudet-2024: Eq. (47) initial condition, the same as Huang & Zahr's
  Eq. (78); slab heights adding to 1.2 on the interval $(0,1)$; "160
  simplices from 20 elements" left undecided.
- wakimura-2024: HLLC Eq. (41) with $(p_L-p_R)$, against the Batten form
  printed by Wong et al. (2021); dodecane table "for 300–500 K" used at
  600 K; isothermal-state density.
- lin-2024-b: Schardin state, 4th entry 1.79567 matching neither $p$ nor
  $E$; Table 3.3 order; Sod state order; ref. [47] year.
- zhang-2024-c: shock–vortex upstream velocity $\sqrt\gamma$ (Mach 1) for
  a Mach 1.1 shock; Eq. (2.27) range; table headings.
- fan-2024: OCAD weight needs the $(\cdot)^{3/2}$ printed by Ding & Wu;
  Tables 3.1–3.2 $\ell^2$ order columns copy the $\ell^1$ ones.
- ding-2024-b: tests at $\Delta t=0.25\Delta x$ above the proved bounds
  ($1/12$ in 1D, $1/8$ in 2D), stated factually; Lemma 2.2 $p^*_m$; empty
  interval $0.5<x\le0.5$.
- chudzik-2024: Table 1 Maxwell orders falling below the third order of
  Theorem 3.1 (recorded as a qualification); "constant vorticity (i.e.
  irrotational flow)".
- kolluru-2024: $p=(\gamma-1)\rho$; App. B Eqs. (23b), (30); parameter
  values differing between text and captions; dam-break depths and $g$
  not printed.
- dematte-2024: Eqs. (21), (34), (39), (49), (51), (63); $A=\nabla\times B$.
- zuo-2024: Eqs. (2.31)–(2.32); unstated sign pairing; double-Mach grid
  extent ($[0,3]$ or $[0,4]$) unstated. zuo-2024-b: order columns.
- delgrosso-2024, chen-2024, teissier-2024, nguyen-2024, wei-2024,
  liang-2024: minor (Source pages).

### Candidates for later pages

- Evolution-Galerkin operators (chudzik-2024), adaptive linear weights
  (lin-2024-b), central DG on overlapping meshes (ding-2024-b, with the
  deferred wu-2023), nonlinear spectral analysis (inline on the
  dispersion-relation page), a static-drop Laplace-law benchmark (inline
  on the oscillating droplet), Wei & Xia's jump indicator (could merge
  into the KXRCF section).
- Registry: $\mathcal E$ is now both the vortex strength and the MHD
  electric field, $\mathcal A$ both the THINC parameter and the vector
  potential, $\lambda_{\mathrm s}$ both Qin et al.'s scaling and the RBF
  shape parameter; no page uses both meanings (§10 notes). A whole-bundle
  pass could give them distinct letters.
- Tag near-synonyms for a whole-bundle pass: filtering/solution-filtering/
  entropy-filtering, compact-scheme/compact-stencil, riemann-problem/
  riemann-solver, positivity/bound-preserving, high-order/very-high-order,
  diffuse-interface/interface-capturing, imex/semi-implicit,
  low-dissipation/numerical-dissipation.

## Chunk 7 — TENO variants, limiters, ADER, well-balanced and multiphase solvers (2026-10-23)

Sources (19): baskaya-2024, berta-2024, cai-2024, cernetic-2023,
ciallella-2024, duronio-2024, gaburro-2024, goudon-2024, huang-2024,
ji-2023, jiang-2024, jiao-2024, liang-2024-b, mcquaid-2024,
nogueira-2024, ruedaramirez-2024, tang-2024, trojak-2024, yu-2023. 139 of
207 ingested, 191 concept pages plus the registry, 4315 bibliography
entries.

### Decisions for the human

1. **New archive defect — wu-2023** (Wu & Shu, SIAM J. Numer. Anal.
   61:250-285, positivity-preserving central DG for MHD): the archive
   file holds only the 9-page Supplementary Materials (no article, no
   tests, no reference list). Deferred to chunk 11 with the other
   defects and added to `~/papers/mosaic/weno-teno-redownload.csv`.
   Chunk 7 therefore stages 19 sources.
2. **Still open from chunks 1–6:** the archive re-download (now three
   works: Feng 2026, Li 2024, Wu 2023); the open contradictions (TENO
   $\tau_K$, conservation of WCNS, entropy-filter tolerance); wrong-year
   keys; the berberich and karniadakis pairs; the label convention.
3. **New open contradiction — cost of WENO-Z against mapped WENO**
   (`wiki/methods/weno-z.md`): Deng (2023, §1, after Borges et al.)
   calls WENO-Z cheaper than WENO-M; McQuaid & Brehm (2024, after Brehm
   et al. 2015) call it more expensive. Neither prints a timing.
4. **Bibliography calls to confirm:** wrong-year keys `hickel-2023`
   (Phys. Fluids 26:106101, 2014) and `eulderink-1994` (A&AS 110:587,
   1995) kept with notes; `andrianov-2004` recorded at JCP 212:434 while
   jiao-2024 prints 195:434; `modesti-2016-b` (arXiv:1612.05223) linked
   to `modesti-2017` as its preprint only on the reader's reading (the
   printed titles differ); undated citations keyed by their Crossref
   issue year (`duronio-2023`, `mohapatra-2023`, `loseille-2022`,
   `couplet-2021`, `wissink-2009`, which mcquaid-2024 prints as 2020);
   the DOI mcquaid-2024 prints for `zibitsker-2022` resolves to another
   work (McQuaid et al. 2021) and was removed with a note.
5. **Bundle fit (no D17 copy made):** cernetic-2023 (TENET, GPU DG for
   astrophysical turbulence) also fits astrophysical-simulation-codes;
   baskaya-2024 and mcquaid-2024 are mainly hypersonic gas–surface and
   heat-flux papers; duronio-2024 is an OpenFOAM application paper;
   jiao-2024 and jiang-2024 are cavitation/multiphase solvers.

### Identity and metadata

- Versions read that are not the version of record: arXiv preprints
  berta-2024 (v4), cai-2024 (v1), cernetic-2023 (v2, accepted),
  ciallella-2024 (v1), gaburro-2024 (v1), ruedaramirez-2024 (v1),
  trojak-2024 (v1), yu-2023 (v1); author preprint baskaya-2024; HAL wrap
  of the version of record goudon-2024.
- ji-2023 calls its dual stencil selection new; ji-2022 already used
  the two-step structure with one cut-off ($C_T=10^{-6}$). New here are
  the pair of cut-offs ($10^{-7}$, $10^{-5}$) and the seventh order.
- Nogueira et al.'s "WENO5-NN" is a different scheme from Stevens &
  Colonius's WENO5-NN; the learned-weights page keeps them apart.
- Future label family: liang-2024 (planned, chunk 8) shares "Liang & Fu
  (2024)" with liang-2024-b; letters will be applied then.

### Printed slips (the Source pages list them in full)

- huang-2024: Eq. (38) sign; Table 2 $L^\infty$ exponent.
- tang-2024: Eq. (15) exponent sign (as printed every $\delta_k$ is 0);
  Table 5 ratio; double-Mach states given in conservative variables.
- ciallella-2024: Eq. (38) $(\gamma+1)/2$ for $(\gamma-1)/2$; Table 5
  orders not reproducible from its errors.
- gaburro-2024: $\Gamma_0$ identically zero; bubble time scale and air
  density inconsistent; Table 1 $P_3$ orders.
- goudon-2024: equilibrium relation and positivity-CFL signs.
- ruedaramirez-2024: Eqs. (33), (39); a "Ma = 1.4" state that is Mach 4.
- trojak-2024: helium–air post-shock state fits no Rankine–Hugoniot
  state; Taylor–Green $\cos(2z+2)$.
- cernetic-2023: Eq. (35) prefactor; Eq. (39) not trace-free; "3096"
  cells inconsistent with the stated doubling.
- berta-2024: Eqs. (27), (28), (37); Eq. (46) Lorentz factor.
- jiao-2024: THINC normalisation; Table 4.3 velocity sign; units.
- mcquaid-2024: Eq. (22) MUSCL right state independent of $\kappa$.
- jiang-2024: Tables 1b, 2b; the point-value WENO5 gives a second-order
  midpoint value; water pressure 0.000359 against $3.059\times10^{-4}$
  printed by Zheng et al. (2021) and Tsoutsanis et al. (2021).
- cai-2024: tests at "CFL 0.6" against the proved bound $1/12$.
- liang-2024-b: Eq. (30) against Algorithm 1 (energy flux);
  baskaya-2024, duronio-2024, yu-2023, ji-2023, nogueira-2024: minor.

### Candidates for later pages

- Quirk–Karni shock/helium-slab tube (trojak-2024, gaburro-2024) —
  qualifies now; hydrostatic reconstruction (goudon-2024 collocated and
  staggered); TENO-AZ and TENO-S; reconstruction for off-site data;
  upwind constrained transport; quasi-conservative schemes; the Jameson
  pressure sensor; a shock–cylinder benchmark.
- Tag near-synonyms for a whole-bundle pass: amr/adaptive-mesh-refinement,
  troubled-cell/troubled-cell-indicator, compact-scheme/compact-stencil,
  positivity/bound-preserving, multicomponent/multiphase,
  cut-cell/ghost-cell/immersed-boundary, solution-filtering/entropy-filtering,
  ducros-sensor, split-form.

## Chunk 6 — WCNS weights, flux globalization, entropy-stable DG for air, interface methods (2026-10-23)

Sources (20): chen-2023, demichele-2023-b, fujiwara-2023, gu-2023,
huang-2023, kurganov-2023, li-2023-b, lin-2023, liu-2023-b, liu-2023,
long-2023, maltsev-2023, paula-2023, peyvan-2023, ramani-2023,
wang-2023-c, zhao-2023, zhong-2023, calhoun-2023, ciallella-2023. 120 of
207 ingested, 181 concept pages plus the registry, 3765 bibliography
entries.

### Decisions for the human

1. **Still open from chunks 1–5:** the archive re-download and overwrite
   (Feng 2026, Li 2024); the open contradictions (TENO $\tau_K$,
   conservation of WCNS); the wrong-year keys `boscarino-2008`,
   `gande-2020`, `ranocha-2021-b`/`-c`; the citation-label convention
   (now applied bundle-wide: letters by slug suffix, Li et al. 2022a–d,
   2023a/b, Liu et al. 2023a/b, De Michele & Coppola 2023a/b, Wang et al.
   2023b/c, Chamarthi 2023a/b, De Vanna et al. 2023a/b/c); the earlier
   merger and book-printing calls.
2. **New open contradiction — is the entropy-filter tolerance problem
   dependent?** ([entropy filtering](wiki/methods/entropy-filtering.md)):
   Dzanic & Witherden (2022, §6) call the filter "free of
   problem-dependent tunable parameters"; Peyvan et al. (2023, §4.2) say
   the threshold "must be tuned according to the problem". Peyvan et
   al.'s side rests on one figure with no run at another threshold.
3. **Bibliography calls to confirm:** `berberich-2021-b` (Comput. Fluids
   219:104858, cited by ciallella-2023) and `berberich-2019` (same title
   and authors, printed by kanbar-2022 as "J. Comput. Phys. 2019" with no
   volume) kept as two entries; `karniadakis-2005` and `-2013` (same book
   title, edition or reprint unverified) kept distinct; the compiler
   re-keyed `gupta-2021` (a placeholder year) to `gupta-1990`, the year
   peyvan-2023 prints; `johnsen-2012` for fujiwara-2023's "JCP 231 (2006)".
4. **Bundle fit (no D17 copy made):** zhao-2023 (gas-kinetic direct
   modelling) and liu-2023-b (RBF-DQ with a gas-kinetic viscous flux) sit
   at the edge of the bundle; ramani-2023 is mainly mesh generation;
   long-2023 and paula-2023 are multiphase-physics papers; kurganov-2023
   and ciallella-2023 treat shallow-water and nozzle balance laws.

### Identity and metadata

- Versions read that are not the version of record: arXiv preprints
  demichele-2023-b (v2), calhoun-2023 (v2), zhao-2023 (v1 of 2021),
  peyvan-2023 (v1), lin-2023 (v2), ramani-2023 (v2); author manuscript
  ciallella-2023 (dated 4 January 2024).
- Key traps resolved: chen-2023 and maltsev-2023 print `li-2022`/`-b` and
  `tsoutsanis-2021`/`-b` in swapped order; dzanic-2022 → dzanic-2022-b in
  lin-2023 and peyvan-2023; zhong-2023 cites five different works under
  planned slugs (`li-2022`, `li-2022-b`, `li-2023`, `li-2023-b`,
  `luo-2021`); ramani-2023 cites the arXiv preprint of li-2022-c (kept
  distinct).

### Printed slips (the Source pages list them in full)

- zhong-2023: Eqs. (40)–(41) give only $O(\Delta x^2)$ for
  $\omega_s-d_s$ at second-order critical points; the fifth order rests
  on Table 4.
- wang-2023-c: Eq. (3.20) misses the cross term $-3495756\,u_iu_{i+1}$.
- huang-2023: Eq. (C.2) is false in general (gap in the TVD proof of
  Thm C.1; the bounds theorem is unaffected); Eq. (50) phase labels.
- chen-2023: the exponential weights change under $u\to\sigma u$, against
  the paper's "no dimensional scale" claim.
- li-2023-b: Table 1 $d_3$ sign; Eqs. (12), (30), (32).
- kurganov-2023: $E\equiv5.5$ printed for $\gamma=1.6$ (data give 14/3).
- peyvan-2023: Mach-10 Shu–Osher with the Mach-3 density 27/7; Leblanc
  density ratio $10^5$ for $2\times10^3$.
- lin-2023: Shu–Osher interface at $x=4$ (shock leaves the domain);
  vortex minimum density $10^{-4}$ scale; Table 5c exponent; Eq. (18)/(20).
- ciallella-2023: Eq. (36) sign; Table 1 orders computed with $N_e-1$.
- calhoun-2023: Table 4 AMR orders; maltsev-2023: Table 1 6.69 for 6.96;
  ramani-2023: Table 3 speed-ups; long-2023: droplet placed behind the
  initial shock; gu-2023, fujiwara-2023, paula-2023, zhao-2023,
  demichele-2023-b (TGV $\cos2x+2$, as in demichele-2023): minor slips.

### Candidates for later pages

- Fujiwara et al.'s FC/PE scheme, smooth adaptive meshing (ramani-2023),
  hybrid DG–FV switching (maltsev-2023), asymptotically
  entropy-conservative fluxes (demichele-2023-b), the S2O4 two-stage
  fourth-order time stepping with its temporal limiter (zhao-2023),
  ForestClaw, the Baer–Nunziato model, Schardin's problem, the
  Rider–Kothe vortex deformation, a lake-at-rest / flow-over-a-bump
  benchmark: each has one source so far.
- Tag near-synonyms for a whole-bundle pass: limiter/limiting,
  unstructured/unstructured-mesh, compact-scheme/compact-stencil,
  positivity/bound-preserving, high-order/very-high-order,
  entropy-filtering/solution-filtering, multicomponent/multiphase.

## Chunk 5 — gradient-based schemes, wall-modelled LES, structure-preserving MHD, GPU codes (2026-10-23)

Sources (20): bernardini-2023, bezgin-2023, devanna-2023-b,
lopezmiralles-2023, bielawski-2023, chamarthi-2023, chandravamsi-2023,
devanna-2023, demichele-2023, devanna-2023-c, dzanic-2023, funada-2023,
qin-2023, wei-2023, weng-2023, zaghi-2023, zhou-2023, bhoriya-2023,
chamarthi-2023-b, chen-2023-b. 100 of 207 ingested, 167 concept pages
plus the registry, 3291 bibliography entries.

### Decisions for the human

1. **Still open from chunks 1–4:** the archive re-download and overwrite
   (Feng 2026, Li 2024); the open contradictions (TENO $\tau_K$,
   conservation of WCNS — Qin et al. 2023 add a globally conservative
   staggered explicit WCNS, which settles nothing for the compact form);
   book printings; kanbar-2022 ref [4]; abgrall-2017-b; Bai & Li's DG
   remark; Boscarino et al.'s SI-IMEX(4,4,3); jin-2010 → jin-2012 and the
   other chunk-4 merger calls.
2. **Bhoriya et al. (2023), ARK3 Table 5:** the printed stiff weights
   $b^{[S]}$ give $\sum_lb_lc_l^2=0.345754\ne1/3$ (the explicit weights
   give 1/3): as printed the implicit part is second order. Recorded as a
   compiler check on the IMEX and Source pages; nothing is said about what
   the code used. The version read is arXiv v2; the version of record
   could settle it.
3. **Bibliography keys with a year that disagrees with the venue**
   (set in earlier chunks, not renamed): `boscarino-2008` (SIAM J. Numer.
   Anal. 45, 2007), `gande-2020` (Numer. Algorithms 88, 2021),
   `ranocha-2021-b`/`-c` (volume 4, 2022). Renaming changes keys that
   other entries' `citedby` and Source pages use; your call.
4. **Merger calls to confirm:** chandravamsi-2023's openacc.org citation
   folded onto `openacc-2022` (same page); `jiang-1995` → `jiang-1996`
   and `tsoutsanis-2023-b` → `tsoutsanis-2021` aliased as misprinted
   years (venue and pages match); `poinsot-1992` keeps the DOI that
   Crossref places at JCP 101:104 (devanna-2023 and devanna-2023-c print
   a DOI resolving to JCP 99:352); bezgin-2023's ref [80] (printed Vinet
   & Zhedanov 2011, used for Pope's book) kept as printed with a note.
5. **Citation labels:** same-author-year works are cited in prose as
   Chamarthi (2023a/b) and De Vanna et al. (2023a/b/c), letters in slug
   order; the Source-page titles keep the bare year (the paper title
   disambiguates). Confirm the convention.
6. **Bundle fit (no D17 copy made):** lopezmiralles-2023 (relativistic
   radiation MHD, a PVM Riemann solver) also fits
   astrophysical-simulation-codes; weng-2023 (OpenFOAM real-gas
   detonation, second-order numerics) and bielawski-2023 (GPU OpenFOAM
   reacting flows, chemistry integration) are weak fits; bernardini-2023,
   zaghi-2023, devanna-2023-b and bezgin-2023 are mainly software papers,
   devanna-2023 and devanna-2023-c mainly turbulence modelling, wei-2023 a
   second-order unstructured boundary treatment.
7. **Pronouns:** the compiler replaced gendered pronouns for single
   authors on concept and Source pages (chunks 1–5) by names or "the
   author"; authors' pronouns are not stated in the sources.

### Identity and metadata

- Versions read that are not the version of record: arXiv preprints
  bezgin-2023 (v1, filename says CPC), lopezmiralles-2023 (v1),
  chamarthi-2023 (v2), chandravamsi-2023 (v1), demichele-2023 (v1),
  dzanic-2023 (v2), bhoriya-2023 (v2), chamarthi-2023-b (v1),
  chen-2023-b (v1); accepted manuscript bielawski-2023.
- bernardini-2023 is a two-page program summary (STREAmS-2.0): every
  claim on its page is Stated.
- Key traps resolved: devanna-2023-c's refs [46]/[68] printed with
  swapped suffixes; dzanic-2023's Dao & Nazarov CMAME, chen-2023-b's
  Huang, Xing & Xiong, zhou-2023's Tsoutsanis & Dumbser, chandravamsi's
  own Phys. Fluids paper and Chamarthi's C&F paper re-keyed away from
  planned slugs; zaghi-2023's Berger & Colella / Berger & LeVeque pair
  remapped; qin-2023's Fernández (DCDR) and bezgin-2023's Fleischmann
  2020 suffixed; bielawski-2023's printed duplicates [26]/[43] and
  [27]/[36] folded.

### Printed slips (the Source pages list them in full)

- zaghi-2023: the printed post-shock state is the Rankine–Hugoniot state
  of a Mach 2.81 shock, not the stated 2.89; grind-time units; "8
  billions" cells; vortex appendix exponent and coordinate slips.
- chamarthi-2023: Table 2 MIG4 orders do not follow from its errors
  (3.93/3.98/3.88); Woodward–Colella right break at 0.8 (others 0.9,
  also chamarthi-2023-b); shock–mixing layer at Re 1000 (others 500).
- chamarthi-2023-b: WCNS sub-stencil Eq. (42) sums to 18/16; the mapping
  denominator of Eq. (48) has a sign slip; "at least 40% cheaper" not
  supported by Table 2 (28–49%).
- demichele-2023: §3.1 lists the $\xi$ values in reverse.
- dzanic-2023: vortex data as printed give a minimum pressure of about
  −1.72; plasma beta $2.5\cdot10^{-6}$, not $10^{-4}$; Orszag–Tang $B_1$
  sign opposite to the other sources (misprint or convention cannot be
  decided from the paper).
- qin-2023: Eq. (40) states list momenta, not velocities; the Eq. (41)
  shock–bubble inflow is not a Rankine–Hugoniot state; Buckley–Leverett
  shock position at $t=0.31$ not reproduced (left off the pages).
- devanna-2023: Mach 5.86 $\Delta x^+=90$ needs $N_x=1200$ (1400
  printed, giving 77.1); devanna-2023-b: abstract's 1024-GPU ~80%
  efficiency against weak scaling shown up to 256.
- bezgin-2023 (JAX-Fluids): 2D implosion with density and pressure
  swapped relative to the bundle's Liska–Wendroff records; "~400 M DOFs"
  not supported.
- bhoriya-2023: ARK3 (item 2); GEM initial data ($\tan$ for $\tanh$,
  negative pressure); 2D time-step formula.
- lopezmiralles-2023, chandravamsi-2023, funada-2023, wei-2023,
  weng-2023, chen-2023-b, zhou-2023: minor slips listed on their pages.

### Deep-lint repairs by the compiler

- An auditor's script turned 13 `\rho` on `properties/bound-preservation.md`
  into line breaks; repaired, and the 2023 entropy margin's sign
  corrected (Dzanic & Witherden 2023 print
  $\Gamma_3=\sigma-\sigma_{\min}-\epsilon>0$: a margin to exceed, not a
  relaxation).
- One unlabelled judgement on the KNP viscous terms (Bielawski et al.)
  removed; the printed sentence stays attributed.

### Candidates for later pages

- Compact (Lele-family) first-derivative schemes: chamarthi-2023,
  chamarthi-2023-b, chandravamsi-2023 — qualifies now.
- MHD shock–cloud interaction (dzanic-2023, duan-2022); global
  conservation property (qin-2023); slowly moving shocks
  (qin-2023); Barth eigenvector scaling (bhoriya-2023 and earlier); WENO
  for Hamilton–Jacobi equations (chen-2023-b, bezgin-2023); the M1
  radiation closure; the double-flux method; a split of
  `gas-liquid-riemann-problems` into gas–gas and gas–liquid problems.
- Tag near-synonyms reported by the auditors and left for a whole-bundle
  pass: compact-scheme/compact-stencil, positivity/bound-preserving,
  entropy-filtering/solution-filtering, multicomponent/multiphase,
  cut-cell/ghost-cell/immersed-boundary, sharp-interface/level-set.

## Chunk 4 — TENO variants, positivity for Navier–Stokes, shock tracking, all-Mach IMEX, codes (2026-10-23)

Sources (20): fan-2022, huang-2022, hu-2022, jain-2022, jeong-2022,
kou-2022, li-2022, liang-2022, wan-2022, dao-2022, hong-2022, ji-2022,
li-2023, mossier-2022, boscarino-2022, balsara-2023, lesur-2023,
huang-2023-b, abgrall-2024, fan-2023. 80 of 207 ingested, 149 concept
pages plus the registry, 2688 bibliography entries.

### Decisions for the human

1. **Still open from chunks 1–3:** the archive re-download and overwrite
   (Feng 2026, Li 2024); the open contradictions (TENO $\tau_K$,
   conservation of WCNS); book printings (leveque, hesthaven, osher);
   kanbar-2022 ref [4]; abgrall-2017-b; Bai & Li's DG remark.
2. **Boscarino et al. (2022), SI-IMEX(4,4,3):** the printed tableau fails
   the explicit third-order condition $b^\top\tilde A\tilde c=1/6$ (0.19885),
   all other conditions up to order 3 holding; checked twice on the page
   image. Either a coefficient is misprinted or the explicit coupling is
   second order. Recorded as a compiler check on the IMEX and Source
   pages; a reading of the version of record could settle it.
3. **Bibliography calls by the merger to confirm:** `jin-2010` (summer
   school lecture notes printed with a journal's pages) folded onto
   `jin-2012`; godlewski-2014 (no 2014 edition known), feiereisen-1983
   (thesis vs the 1981 report) and nocedal-2006 (2nd edition) kept
   distinct; li-2023's `fu-2016` printed at JCP 352:498 (2018), a place
   where Crossref has no Fu paper, keyed by title and authors. The
   compiler moved huang-2023-b's citations of the Springer reprint
   collection onto `shu-1989-b` and a new `harten-1987-c`, and split the
   "accepted" Bai et al. citation of ji-2022 into `bai-2022-c`, by the
   reprint and preprint rules.
4. **Bundle fit (no D17 copy made):** lesur-2023 (IDEFIX) is mainly a
   software paper whose numerics are cited standard methods — it also
   fits astrophysical-simulation-codes; boscarino-2022 and abgrall-2024
   are as much time-integration papers (ode-integration).

### Identity and metadata

- Versions read that are not the version of record: arXiv preprints
  huang-2022 (v2), jain-2022 (v1), dao-2022 (v1, despite the filename),
  boscarino-2022 (v2), lesur-2023 (v1), huang-2023-b (v1); author preprint
  ji-2022.
- The archive's byte-copy file named "Li 2024" holds liang-2022 (chunk-1
  defect); liang-2022 is ingested from its own file.

### Printed slips (the Source pages list them in full)

- hu-2022 and chertock-2023: the Titarev–Toro shock labelled "Mach 1.1" is
  a Mach 1.3 state, with $\sin(20x)$ where other sources print
  $\sin(20\pi x)$; which wavenumber the original uses is not settled by
  any ingested source.
- li-2022 Eq. (44): coefficient 271799 for 271779 (the coefficients then
  sum to 20 instead of 0).
- fan-2023: wrong sign on a $q_0$ coefficient (fails on $f=x$); the
  printed limiter indicator is not that of the stated quartic.
- lesur-2023: viscous stress and heat flux anti-diffusive as printed
  (sign-convention dependent); Sod test printed with $p_L=p_R$.
- abgrall-2024: amplification factor $G_4$ with $1/(2\theta)$, the
  bound 1.745 (1.321 from the norm condition), swapped symbol maxima;
  Table 1 not reproducible from the text.
- boscarino-2022: Gresho middle pressure branch with the wrong log sign;
  Table 5.2 exponent.
- dao-2022: sound speed without the square root; negative initial
  pressure of the MHD vortex.
- jeong-2022 Eq. (19): 47/30 for 47/60.
- huang-2022: initial condition (78) contradicts its exact solution (79).
- fan-2022: Mach 2000 jet inflow density printed as 0.5.

### Candidates for later pages

TENO-M and unstructured TENO (long variant sections on the TENO page),
linear and matrix shock-stability analysis, volume penalization,
residual-based viscosity, the interface-equilibrium condition and the
conservative diffuse-interface method, steady-state convergence, the MHD
rotor (five sources), blunt-body bow shock, decaying isotropic
turbulence, Jiang–Shu multi-wave linear advection, the Quirk and Elling
carbuncle tests.

## Chunk 3 — flux reconstruction, entropy correction, limiters, multiphase and relativistic flows (2026-10-22)

Sources (20): browne-2022, dzanic-2022, hiejima-2022, nguyen-2022,
peng-2022, wang-2022, yu-2022, abgrall-2022, bai-2022, bezgin-2022,
sousa-2022, chen-2022-b, chen-2022, chu-2022, cicchino-2022, duan-2022,
du-2022, du-2022-b, dzanic-2022-b, edoh-2022. 60 of 207 ingested, 127
concept pages plus the registry, 2250 bibliography entries.

### Decisions for the human

1. **Still open from chunks 1–2:** the archive re-download and overwrite
   (Feng 2026, Li 2024); the two open contradictions (TENO $\tau_K$,
   conservation of WCNS); book printings (leveque, hesthaven); kanbar-2022
   ref [4].
2. **Bai & Li (2022) on DG local conservation** ("can not be easily
   guaranteed", §1): recorded as an attributed qualification on the DG
   and local-conservation pages, against the flux-form conservation
   results there. Promote to a contradiction if you read it as a claim.
3. **Bibliography calls:** `osher-2002` folded onto `osher-2003` (the
   first edition printed with year 2002 by bai-2022) — a year variant
   under the merger's reading, a separate entry under a strict edition
   rule; `abgrall-2017-b` ("Comp. Fluids 19 (2017)", no pages) kept as
   printed, unresolved.
4. **Bundle fit (no D17 copy made):** browne-2022 (hypersonic transition
   prediction), sousa-2022 (LES closure with shock capturing),
   peng-2022 (AMROC combustion solver), wang-2022 (second-order ghost-cell
   immersed boundaries) sit at the edge of this bundle.

### Identity and metadata

- Versions read that are not the version of record: arXiv preprints
  dzanic-2022 (v2), abgrall-2022 (v4), sousa-2022 (v2), chen-2022-b (v1),
  cicchino-2022 (v1), duan-2022 (v1), dzanic-2022-b (v3); author
  manuscript peng-2022.
- yu-2022: the printed title reads "Galekin"; Crossref carries the same
  spelling and the page keeps it.
- sousa-2022: Crossref gives the family name "C. B. Sousa" (first author
  Victor C. B. Sousa); slug `sousa-2022`.

### Printed slips (the Source pages list them in full)

- dzanic-2022-b: the SSP-RK3 stages of Algs. 3–4 lack the 1/4 and 2/3
  factors (not first-order consistent as printed); tables print $L^2<L^1$
  errors, which its own definitions exclude.
- hiejima-2022: the double Mach reflection labels (A)/(B) are swapped
  against Eq. (29); the WCNS-T flux derivative is a two-point interface
  difference, formally second order (compiler check).
- wang-2022: the printed post-shock velocity 1566.2 m/s is the shock
  speed (Rankine–Hugoniot gives about 1240.7 m/s); Eq. (23) sign slip.
- chen-2022-b: the strong vortex requires $\gamma=1.4$ (the stated
  default is 5/3); the relativistic double-Mach state satisfies the jump
  conditions only with $v_2=0$, the shock-diffraction state only with
  $\gamma=5/3$.
- nguyen-2022: the exact phasic mass conservation claimed is reached only
  to $O(\Delta t^2)$ by the primitive-variable update (compiler check).
- sousa-2022: the closed-form Fejér weights do not match Eq. (30).
- edoh-2022: the Taylor–Green time step printed both as $t_c/10^4$ and
  $10^{-3}$; the vortex diameter 2.1 m against about 3.3 m from the formula
  (assuming $\gamma=1.4$, not printed).
- bai-2022: the copper stiffening constant printed in bar (must be Pa);
  the HLLC/HLL switch of Eqs. (16)–(19) reads, as printed, partly opposite
  to its stated aim (Mach numbers in the mesh frame).
- abgrall-2022: the "rotation" test field of Eq. (43) is a saddle.

### Candidates for later pages

Kept inline until a second source or a named contribution arrives:
primitive-variable recovery for relativistic flows, spectral vanishing
viscosity and local artificial diffusivity, Du & Yang's conservative
modified exponential Runge–Kutta, two-layer shallow-water equations
(chu-2022, balsara-2024), AUSM-family fluxes (peng-2022, hiejima-2022),
residual distribution, solution filtering, the Div-rot splitting, the
Prandtl–Meyer expansion, the Daru–Tenaud viscous shock tube, the MHD
rotor, the Gresho vortex, the dam break.

## Chunk 2 — WENO variants, entropy-stable DG, multiphase, shock tracking (2026-10-22)

Sources (20): pazner-2021, bryngelson-2021, sciacovelli-2021, wang-2021,
fan-2021, liu-2021, luo-2021, matsushita-2021, renac-2021,
ruedaramirez-2021, wong-2021, zheng-2021, tsoutsanis-2021, kanbar-2022,
li-2022-d, puppo-2023, li-2022-c, zheng-2022, arun-2022, basile-2022. 40 of
207 ingested, 109 concept pages plus the registry, 1619 bibliography
entries.

### Decisions for the human

1. **Archive defects of chunk 1** (still open): re-download of Feng et al.
   2026 and Li et al. 2024, and the overwrite of the three misnamed files.
2. **Contradiction "conservation of WCNS"** ([WCNS](wiki/methods/weighted-compact-nonlinear-scheme.md)):
   Fu (2023, §3.7) calls the lack of conservation "the main flaw" of WCNS
   family schemes; Wong et al. (2021, §4.1) show their compact WCNS in
   flux-difference form and call it conservative (their compact case is
   relayed from Subramaniam et al., not ingested). The auditor found both
   speak of the compact interface-to-node form. *Open*; the TENO $\tau_K$
   entry of chunk 1 also stays open.
3. **Book printings folded by the merger:** `leveque-2004` onto
   `leveque-2002` and `hesthaven-2008` onto `hesthaven-2007` (same book,
   reprint or copyright year). In ode-integration the same question
   (same-DOI printings kept apart by printed year) is still open; one
   ruling could serve both bundles. `sedov-1993` (CRC edition) kept apart
   from `sedov-1959`.
4. **kanbar-2022 ref [4]** (`brackbill-2004`): printed with Brackbill &
   Barnes' authors and title but the venue J. Comput. Phys. 201:261–285
   (2004), which on Crossref is Balbás, Tadmor & Wu. Kept as printed and
   marked unresolved.
5. **Bundle fit (no D17 copy made):** arun-2022 (first order, mostly
   time integration and asymptotics) is a candidate for a copy into
   ode-integration, which has an asymptotic-preserving page;
   matsushita-2021 (GPU two-phase low-Mach solver) and basile-2022 (h/hp
   adaptivity for steady subsonic RANS, no shocks) sit at the edge of
   this bundle; bryngelson-2021 is mainly a software paper.

### Identity and metadata

- Versions read that are not the version of record: arXiv preprints
  pazner-2021 (v1, 2020; Rueda-Ramírez et al. 2022 cite its Eqs. (34)/(35),
  which are Eq. (23) and Prop. 5 in v1), bryngelson-2021 (v1, 2019),
  sciacovelli-2021, renac-2021 (v3), ruedaramirez-2021 (v1), wong-2021,
  kanbar-2022 (14 pp. against 21 published), li-2022-d, puppo-2023 (v2),
  li-2022-c, arun-2022; author manuscripts luo-2021 and basile-2022.
- luo-2021: page 1 reads "Interface Conservation Enforcement", Crossref
  "interface condition enforcement"; the published title is used.
- Page-1 initials used where they differ from Crossref (arun-2022
  "Arun K.R.", Qiu J.-M., Chapelier J.-B.).
- luo-2021: a drafter "corrected" the third author of Dennis, Gay & Walsh
  to Welsch from memory; Crossref lists Walsh, as printed, and the page
  keeps the printed name.

### Printed slips (the Source pages list them in full)

- kanbar-2022: the off-diagonal magnetic stress ($-\tfrac12B_iB_j$ for
  $-B_iB_j$), the $x$-flux of the induction equation, and the MHD vortex
  (not divergence-free, pressure negative for $r>\sqrt2$); the scheme keeps
  the reference state by construction, so the test cannot reveal it
  (compiler checks).
- pazner-2021: the time-step bound (40) negative as printed.
- sciacovelli-2021: $k_\varepsilon$ printed as the inverse of what the
  equations use; the sign of the general dissipation formula against its
  four explicit members.
- fan-2021: SSP-RK3 positivity CFL "one third" of forward Euler; Wong et
  al. (2021) §5.3 keep the forward-Euler bound — recorded as two
  sufficient conditions.
- matsushita-2021: Weber number 0.26 printed (13.1 from the printed data),
  "<7 %" error (−12 %, +17 %), volume error 1.5 % in the text and 0.16 % in
  the figure.
- tsoutsanis-2021: CWENO cost "60–80 %" of WENO (0.55–0.94 from Table 1);
  water-column diameter 96 mm against the printed geometry (9.6 mm fits);
  refs [37] and [39] print the DOIs of refs [13] and [34].
- kanbar-2022 and li-2022-c print the $x>0,y>0$ state of the same MHD
  four-state problem with opposite signs (+0.5 / −0.5); neither comments.
- wang-2021: which linear weights "New WENO5" uses is ambiguous.
- puppo-2023: CWENO3 indicator factor 52/3 printed, 13/3 from its own
  definition.

### Candidates for later pages

Kept inline until a second source or a named contribution arrives: the
relaxation Riemann solver (Renac), hydrostatic reconstruction (Arun), DIRK
and IMEX stepping, JST-type high-order dissipation and the product shock
sensor (Sciacovelli), graph viscosity, constrained transport and the
Godunov–Powell source term, interface pressure–velocity equilibrium and
primitive-variable reconstruction (four sources), the Noh problem and wall
overheating, Richtmyer–Meshkov, the triple-point problem, GEM
reconnection, Brio–Wu, the viscous shock tube.

## Chunk 1 — founding chunk: reviews and vocabulary (2026-10-21)

Sources (20): fu-2023, wu-2023-b, deng-2023, huang-2026, balsara-2024,
wang-2022-b, ye-2022, fu-2021, luo-2021-b, li-2022-b, ranocha-2023,
chertock-2023, wang-2023-b, takagi-2022, peng-2024, abgrall-2023,
coppola-2023, ruedaramirez-2022, cui-2024, kuzmin-2023. 82 concept pages,
the registry, 20 Source pages, 860 bibliography entries.

### Decisions for the human

1. **Archive defects (page-1 and checksum check of all 207 files).** Two
   files are byte copies of other files and one holds another paper than
   its name says:
   - `2023_..._Computers_amp_Fluids_Wang_Fifth_order_AWENO_...pdf` is a byte
     copy of Li et al. 2022 (WENO-ZN, C&F 244:105547);
   - `2024_..._Journal_of_Computational_Physics_Li_A_family_of_TENOA-THINC-MOOD_...pdf`
     is a byte copy of Liang et al. 2022 (TENO, JCP 467:111465);
   - `2026_..._Physics_of_Fluids_Feng_Improvements_of_weighted_...pdf`
     holds Wang, Don & Wang 2023 (C&F 251:105743), which will be ingested
     from it as `wang-2023` in chunk 11.

   Missing works, listed with DOIs in `~/papers/mosaic/weno-teno-redownload.csv`:
   Feng et al. 2026 (Phys. Fluids 38:011302, `10.1063/5.0303368`) and Li et
   al. 2024 (JCP 519:113375, `10.1016/j.jcp.2024.113375`). Proposal, as for
   ode-integration: you re-download both into `~/papers/re-download`, and
   authorize the compiler to overwrite the three files so that every
   filename names its content (Li 2024 into the TENOA-THINC-MOOD file;
   the Wang 2023 paper into the AWENO-named file; Feng 2026 into the
   Feng-named file). Until then the two byte-copy filenames stay on the
   worklist as pending.
2. **Contradiction "accuracy condition on $\tau_K$"** ([TENO](wiki/methods/targeted-eno.md)).
   Fu (2023, §3.1, Eq. 17) states that $\tau_K/(\beta_k+\epsilon)=O(\Delta x^s)$
   for any $s>0$ gives the design order; Ye et al. (2022, §3.5, Eqs. 36–38)
   state that $O(\Delta x^{K-2})$, i.e. $\tau_K=O(\Delta x^K)$, "need[s] to be
   satisfied". Three auditors read both papers as incompatible claims about
   the same property and kept the entry *Open*; a fourth reads Ye et al.'s
   "need" as a stronger sufficient condition (their own Eq. 39 uses a
   sixth-order $\tau$ for every $K$) and would move it to Qualifications.
   It stays open; you may close it by fiat.
3. **Bibliography calls to confirm:**
   - `ranocha-2018-c`: Ranocha's 2018 thesis (cited by ranocha-2023) and its
     Cuvillier book edition (cited by ruedaramirez-2022) merged as one work.
   - `liu-2021-b` (no venue printed) kept apart from `liu-2022` (SISC
     44:A230), of which it is probably the preprint; it was not printed as
     a preprint.
   - `toro-2009` and `toro-2013` kept distinct as printed.
   - `sonntag-2014`: ruedaramirez-2022 ref [4] printed without a year, keyed
     by its venue (FVCA VII, 2014).
   - `harten-1997` and `shu-1989-b` treated as reprints in the Springer
     collection "Upwind and High-Resolution Schemes", silenced against the
     originals.
   - `demichele-2023-c`: the "submitted" form of `demichele-2023`, its own
     entry by the preprint rule.
4. **Bundle fit (no D17 copy made).** ranocha-2023 is mainly a
   software/HPC paper on DG kernels (fits a codes bundle as well);
   kuzmin-2023 is a continuous-finite-element paper; balsara-2024's test
   systems are multiphase models. All are in scope here. None of the 20
   chunk-1 works is a Source page of another bundle.

### Identity and metadata

- Version read differs from the version of record for 13 sources:
  arXiv preprints wu-2023-b (v1, 28 pp.; the SIAM Review paper has 43, so
  numbering may differ), ranocha-2023 (v2), chertock-2023 (v2), fu-2021
  (v1), peng-2024 (v1), kuzmin-2023 (v1), coppola-2023 (v1),
  ruedaramirez-2022 (v2), cui-2024 (v1); author or accepted manuscripts
  deng-2023, balsara-2024, abgrall-2023. Each Source page records the
  version and cites its numbering.
- peng-2024: Crossref has no volume or pages yet (online 30 July 2024);
  the venue is "Math. Comp." only.
- coppola-2023: page 1 prints the second author as A. E. P. Veldman
  (Crossref: A. E.); the page-1 form is used.
- Filenames name a given name in place of the surname for Balsara
  ("Dinshaw", a chunk-4 source) and Sousa ("C", chunk 3).

### Printed slips (the Source pages list them in full)

- li-2022-b Table 2, $r=5$, $k=4$: 77/20 for 77/60 (row sum 214/60).
- ye-2022 Tables 1, 3, 5: signs and order of several interpolation
  coefficients (re-derived exactly).
- abgrall-2023 Eqs. (51)–(52): quadrature weights that do not sum to 1;
  Eqs. (55)–(56) swapped; Eq. (111) claims one order too many.
- wu-2023-b Eq. (6.21): exponent $+1/2$ of $\rho$ where $-1/2$ holds (arXiv v1;
  whether the version of record fixes it is unknown).
- cui-2024 Example 3: Rankine–Hugoniot pressure ratio with $M^2+1$ for $M^2-1$.
- balsara-2024 §VIII.b: anti-diffusion "switched off" together with
  $\psi=1$ (full anti-diffusion); §III "we don't consider well-balancing"
  against well-balanced results in §VIII.
- fu-2023 and takagi-2022: double Mach reflection captioned at $t=2.0$
  (Takagi et al.'s text gives $t=0.2$; the review's figure carries the same caption); fu-2023's hierarchical voting count
  (14 cases by Eq. 20 as printed, not 9).
- chertock-2023: the Titarev–Toro-type state is a Mach 1.3 shock, not 1.1,
  and its density drops a digit against Luo & Wu and Fu 2021.
- deng-2023 Eq. 6.6: the new WENO weight stays $O(1)$ away from the linear
  weight at the accuracy point, so the scheme is formally second order,
  not uniformly third (compiler check).
- ranocha-2023 §4.2: the text's speed-up ranges disagree with its own
  Table 2.
- coppola-2023 Eq. (6): a missing minus sign.
- Double Mach reflection post-shock pressure: 116.8333 (fu-2021,
  takagi-2022, ye-2022, huang-2026) against the Rankine–Hugoniot value
  116.5 (peng-2024, wang-2023-b): a setup difference, not a contradiction.

### Candidates for later pages

Kept inline until a second source or a named contribution arrives: the
Hu–Adams–Shu positivity flux limiter (fu-2021, takagi-2022, wang-2022-b
use it), bar states and invariant domains, OFDG, the logarithmic mean,
entropy projection, TENO-N, hybrid and unstructured TENO, multi-resolution
WENO as its own page, WENO-P/P+, the convection boundedness criterion, the
Titarev–Toro problem, the Leblanc shock tube, two-dimensional explosion and
implosion problems.
