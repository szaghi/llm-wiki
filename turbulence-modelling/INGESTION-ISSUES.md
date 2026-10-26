# Ingestion issues — turbulence-modelling

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 3 — 2022–2023 papers: learned SGS and RANS closures, immersed boundaries, GPU codes, shock–boundary-layer interaction, plasma and wave turbulence (2026-10-26)

Sources (20): maeyama-2022, coelho-2022, fischer-2022, davidovits-2022,
kochurin-2022, helm-2022, cai-2022, dang-2022, eivazi-2022, kim-2022,
mcconkey-2022, seyedi-2022, dahlin-2022, ferrand-2022, gan-2022,
placco-2023, ferrer-2023, blind-2023, carlsson-2023, cato-2023. 60 of 134
ingested, 84 concept pages plus the registry, 3573 bibliography entries.
Deep lint A1–A7 over the chunk-3 content done.

### Decisions for the human

1. **Two new archive files.** Wang & Roy (2023), J. Comput. Phys.
   474:111760 (error transport for DG), and Elzaabalawy et al. (2023),
   J. Comput. Phys. 483:112059, appeared after founding; both are planned
   in chunk 7 (now 14 sources) as `wang-2023` and `elzaabalawy-2023`. To keep
   suffixes in publication order, the planned GPU gas-kinetic paper
   (J. Comput. Phys. 476:111899, chunk 4) becomes `wang-2023-b` and the
   EnKF SGS paper (Phys. Fluids 35:085107, chunk 5) `wang-2023-c`.
2. **Bibliography calls left by the resolver:** ferrer-2023's Reed & Hill
   Los Alamos report was folded into `reed-1973` (the conference entry), as
   in chunk 2; `pope-2006` (a reprint printed by helm-2022) was folded into
   `pope-2000`, while `pope-2010` and `karniadakis-2005`/`karniadakis-2013`
   remain separate entries; ferrand-2022's Kolmogorov (1941) citation
   (Russian edition, page 16 against 19) was folded into
   `kolmogorov-1941` without a Crossref check. Split or keep on your word.
3. **carlsson-2023 ref. [28]** prints the title and authors of its ref.
   [35] with a different DOI; the DOI resolves to Probst, Löwe, Reuß, Knopp
   & Kessler, AIAA J. 54:2972, which matches the text's "Löwe [28]". The
   entry (`probst-2016`) now follows the DOI's record.
4. **Versions read.** Sixteen of the 20 files are preprints or author
   manuscripts (13 arXiv, 2 HAL, 1 author manuscript); the Source pages say which
   and cite their locators. blind-2023's arXiv title ("Grid-adaptation for
   wall-modeled large eddy simulation using unstructured high-order
   methods") differs from the published one; ferrer-2023's arXiv version
   prints 13 authors where Crossref lists 14 (Marbona H. added).
5. **Optimal eddy viscosity page?** McConkey et al. (Eqs. 6–7), Cato et
   al. (Eq. 18), Abe (2021) and Vela-Martín (2022) use the same projection
   of a reference stress on the strain rate (compiler check). It is now
   inline on the Boussinesq page; a page of its own qualifies.

### Contradictions

None open. Considered and kept as attributed qualifications:
**modelled-energy threshold of LES** — Haering et al. recall the 10% of
Jiménez & Moser but run well past it; Seyedi & Zayernouri use 10% as the
line between LES and very-large-eddy simulation; Helm & Martín say 25–30%
"may be possible"; Blind et al. cite Toosi & Larsson's finding that the
ratio correlates poorly with length scales; the four define the fraction
differently ([large-eddy simulation](wiki/definitions/large-eddy-simulation.md)).
Also: Kim et al. (eddy-viscosity form limiting for a learned SGS model)
against Cato et al. (stress misalignment immaterial to the reconstructed
mean flow); best-fit eddy viscosity of the stress (McConkey) against that
of the mean velocity (Cato); Gan et al.'s Alfvén anisotropy exponent
against Schekochihin's local-field argument; Kochurin et al.'s weak
turbulence of a non-conducting ferrofluid against Schekochihin's critique
of weak MHD turbulence; Seyedi & Zayernouri against Kim et al. on
backscatter; Ferrer et al. against Flad & Gassner on DG for implicit LES;
Cogo et al. against Placco et al. on the schemes of STREAmS; the Trettel–
Larsson transformation printed with the square root over the whole
integrand (Carlsson et al., Eq. 26) and without it (Cogo et al., Huang et
al.). The FLEXI mortar types of Krais et al. (2:1, 4:1) and Blind et al.
(2-to-1) were found to describe the same halving.

One chunk-2 error corrected: the channel page called the PANS fraction
$\beta_k$ "resolved"; it is the unresolved fraction. Cato et al. print
$c_{w1}=c_{b1}/\kappa^2+\dots$ with Alauzet et al.'s constants, which
confirms the chunk-2 compiler check on Alauzet et al.'s $c_{b1}/\kappa$.

### Printed slips (recorded on the Source pages)

- helm-2022: separation-length increase 32% (abstract) against 30%
  (§§IV F, V); 25% and 18% for the same wall value; 12% (§V) against 14%
  (§III B); Table III wide-domain row duplicates the narrow one; rescaling
  lengths 29δ/7δ attached to the wrong simulation types; index slips.
- dang-2022: 24 567 against 24 576 GPUs; Table 6 total ($10^{12}$ against
  the rows' $10^{11}$, compiler check); weak- and strong-scaling
  efficiencies against the printed times; WENO-SYMBO operation count 216
  against 262; Eqs. 12, 13, 15–16, 19, 27, 38; companion Part 2 cited but
  not listed.
- blind-2023: test-level factor 1.59 (1.31 from the printed degrees,
  compiler check); Table 4 captioned $Re_\tau=550$; 512 DOF per element
  against degree 5; Table 2 row $l=2$.
- fischer-2022: Table 1 header $n$, Table 2 38-node time, $E=6840$ against
  6480, 248× against 234×, operation count of §2.3.
- seyedi-2022: order "$2\alpha\in(1,2]$" against $\alpha\in(0,1]$;
  swapped labels in Eq. 24; inconsistent symbols in Eqs. 7, 10, 19, 21.
- placco-2023: $C_P$ without the square on the Mach number; "order of
  magnitude" reduction against Table 3 (factor 2.2–4.6, compiler check).
- cato-2023: Eqs. 2b, 9, A16; ref. [9] cited as "Duraisamy et al." (first
  author Singh); threshold 0.86 against 0.8.
- carlsson-2023: LD2 credited to "Löwe et al. [28]"; $C_{dw}$/$C_w$; figure
  and equation cross-references.
- maeyama-2022: $\Omega_i$ for $\Omega_e$; phase velocities 42.7, 45.1
  against 47.3, 42.6 from the printed values (compiler check).
- ferrand-2022: $d_i=0.05/L_0$; missing $\sqrt{\mu_0}$ in Eqs. 17, 23
  (compiler check); $F_{F21}$ for $F_{A18}$.
- dahlin-2022: "just over 15×" against 18 (compiler check); kochurin-2022:
  $\omega\sim k^{-3/2}$ for $k^{+3/2}$ (Fig. 4); gan-2022: run C wave
  fraction 0.271 against "less than ∼25%", run A fast fraction; davidovits-
  2022: Fig. 6 Mach numbers against Table I; cai-2022: Eqs. 16, 18
  consistent only for $\Delta=1$; kim-2022: run length; mcconkey-2022:
  Table II duplicates, invariant count; ferrer-2023: Eq. 2, Fortran
  2003/2008, scaling "up to 1000 processors"; eivazi-2022, coelho-2022:
  minor.

### Bibliography

3573 entries (+805); 87 aliases, about 55 verified silences, 2 printed
duplicates folded (ferrer-2023 refs [16]/[40]; gan-2022 Meyrand 2016),
`FLAGS: 0`, `--dupes` clean. Printed keys equal to a Source slug for a
different work re-keyed: `li-2022-c` (Li, Chen & Ren, JCP 448, cited by
dang-2022), `li-2022-d` (Li, He & Liu, PoF 34, cato-2023), `li-2022-e`
(Tianwen-1, Astrodynamics, placco-2023), `cai-2022-c`, `kim-2022-b`;
self-citations kept as `@misc` entries `maeyama-2022-b` (code and data)
and `kochurin-2022-b` (supplemental material). Preprints kept distinct:
`mateogabin-2021`, `duraisamy-2020`. Corrected from Crossref:
`ohyabu-1994` (printed 1984), `paruta-2018` (volume 25), `priest-1996`
(Phil. Trans. A), `lumley-1978` (pages 123–176), `probst-2016`.

### Bundle fit (D17 candidates, no copy made)

- maeyama-2022 (gyrokinetic cross-scale turbulence) and coelho-2022
  (stellarator edge turbulence with GBS): `fusion-mhd-simulation`.
- dahlin-2022 (coronal helicity condensation; its "subgrid-scale model" is
  a parametrized source term, not an LES closure), ferrand-2022 and gan-2022
  (space-plasma and compressible MHD turbulence): `astrophysical-simulation-codes`.
- kochurin-2022 (magneto-capillary wave turbulence), davidovits-2022
  (laboratory shock-generated turbulence), placco-2023 (planetary entry),
  fischer-2022 and ferrer-2023 (software papers): peripheral to closure
  modelling.

### Candidate pages (kept inline until a second source)

Optimal eddy viscosity (qualifies, see decision 5); constrained LES;
lattice Boltzmann method and ProLB; Ahmed body; continuous spectral
element method; Ducros and Jameson shock sensors; Reynolds-stress
anisotropy invariants; Reynolds-force vector; Richtmyer–Meshkov
instability; very-large-eddy simulation; v2-f model; WALE model;
gyrokinetics and GKV; drift-reduced Braginskii model and GBS; MHD
wave-mode decomposition; proper orthogonal decomposition.

## Chunk 2 — 2021–2023 papers: SGS clipping, PANS, mesh adaptation, DES, transition, wall laws, gas-kinetic DNS, RL wall models, dynamos (2026-10-25)

Sources (20): abe-2021, pereira-2021, prakash-2022, mozaffari-2022,
hoy-2022, basile-2023, carrenoruiz-2022, gillyns-2022, knopp-2022,
yan-2022, alauzet-2022, cao-2022, mateogabin-2022, cogo-2022, huang-2022,
francois-2022, liu-2022, martinalvarez-2022, seta-2022, bae-2022. 40 of 132
ingested, 68 concept pages plus the registry, 2768 bibliography entries.
Deep lint A1–A7 over the chunk-2 content done.

### Decisions for the human

1. **New archive file.** Ghidoni et al. (2026), J. Comput. Phys.
   550:114637 (explicit wall function for high-order DG RANS), appeared in
   the archive after founding; identity checked on Crossref and page 1,
   planned as `ghidoni-2026` in chunk 7 (now 12 sources).
2. **Bibliography calls left by the resolver:** the chunk-1 key
   `langtry-2004` holds Langtry et al. Part II, J. Turbomach. 128:423, whose
   print issue is 2006 (the year-of-issue rule would make it
   `langtry-2006`); `duan-2011-b` (Part 3, JFM 672) precedes `duan-2011`
   (Part 4, 684), so the suffixes are not in publication order; Reed & Hill,
   printed "1977, p. 23" with no venue by mateogabin-2022, was folded into
   `reed-1973` on authors and title alone. Rename or split on your word.
3. **Version read of bae-2022** is the Research Square preprint v1 (June
   2021); the Nature Communications version may differ in numbers and
   wording, and the pages cite the preprint.

### Contradictions

None open. One opened at drafting and reclassified: **log-layer mismatch
of the Bae & Koumoutsakos RL wall model** — Bae & Koumoutsakos (2022,
preprint) report a friction-velocity error below 5% from $Re_\tau=5200$
to $10^6$; Vadrot et al. (2023b, Table III) measure log-layer mismatches of
$+1$ to $+2$ and $-0.9$ to $-3.2$ in their re-implementation. Different
quantities, solvers and matching heights ($h^+_{\mathrm{wm}}$ about 4.7
times lower in Vadrot et al., compiler check), and Vadrot et al. attribute
the difference to grid resolution: now a qualification on
[machine-learning wall models](wiki/methods/machine-learning-wall-model.md),
cross-referenced from the RL-closure, log-layer-mismatch and benchmark
pages. Near-conflicts kept as attributed qualifications: Yan et al.'s
strain-based baseline SA against Li & Liu; two printed forms of the DDES
shielding function (François et al., Yan et al.); unsteady RANS judged
incorrect (Mozaffari et al.) and needed (Carreño Ruiz & D'Ambrosio) in
different regimes; Abe (2021) and Cao et al. (2022) on implicit LES in
different settings.

### Printed slips (recorded on the Source pages)

- alauzet-2022: $c_{w1}$ printed with $c_{b1}/\kappa$ (the log-layer
  balance gives $c_{b1}/\kappa^2$, 3.24 against 2.76, compiler check);
  destruction-term sign in Eq. 13; inverted anisotropic-ratio formula;
  Table 2 mass-flow ratios of the elsA rows.
- pereira-2021: production-sign slip between Eqs. 5 and 17; the "half-width"
  growth rate of Eq. A9 is that of the full height.
- yan-2022: SA destruction term without the square; training hill shapes
  (text 0.5/0.8, captions 0.8/1.2); Table 4 against Table 3.
- cao-2022: Eq. 11 sign; $k_{\max}$ formula against Table 8.
- cogo-2022: Table 2 shape factor of case M6L (10.9 printed, 13.4 from the
  row); Eqs. 5.9–5.10 exponent. huang-2022: Table 3 ratios; $H_{12}$
  against the Hopkins correlation.
- basile-2023: `max` in Eq. 18 against the marking rules.
- bae-2022: reward sign (Eq. 9) and $\beta$ update (Eq. 8).
- seta-2022: compression-term sign reading; Table 3 parts against the
  Table 2 total; Lorentz force labelled "dyne".
- martinalvarez-2022: §3.2 exponent pairing; liu-2022: $q=10^3$ caption,
  Eq. 13 primes, units of $E_{\mathrm{mag}}$.
- knopp-2022: constant 1.78 kept in §7.4 after the revision to 1.68;
  prakash-2022: correlation-coefficient normalization (Eq. 19);
  mateogabin-2022, mozaffari-2022, francois-2022, carrenoruiz-2022,
  gillyns-2022, hoy-2022, abe-2021: minor slips.

### Bibliography

2768 entries (+953 from 1248 printed references); 105 aliases, 38 verified
silences, 3 printed duplicates folded (liu-2022 Kretschmer 2019/2020 and
Schmidt 2011a/b; martinalvarez-2022 Attia 2021), `FLAGS: 0`. Keys corrected
from Crossref: `pudritz-1989` (printed 2002), `vazza-2018`,
`steinwandel-2020`, `kretschmer-2020`, `beck-2016-b`; cao-2022's
`jeffrey-2014` aliased to `slotnick-2014`, carrenoruiz-2022's
`menter-1994` to `menter-1994-b`.

### Bundle fit (D17 candidates, no copy made)

- liu-2022, martinalvarez-2022, seta-2022 (dynamos in galaxy and
  interstellar-medium simulations): `astrophysical-simulation-codes`.
- mateogabin-2022 (entropy-stable SVV and shock capturing for DG) and
  cao-2022 (gas-kinetic schemes): `weno-teno`.
- alauzet-2022 (adjoint-based anisotropic mesh adaptation for steady RANS)
  and hoy-2022 (fluid–structure interaction under shock/boundary-layer
  interaction): peripheral to closure modelling.

### Candidate pages (kept inline until a second source)

Stabilized mixed model; approximate deconvolution; anisotropic
minimum-dissipation model; laminar separation bubble; SD7003 airfoil;
nonequilibrium turbulence; discrete adjoint (Yan, Alauzet); strong
Reynolds analogy; uniform momentum zones; inflow turbulence generation
(Bae, Cogo, Huang); shock/boundary-layer interaction; dilatational
dissipation; wall-model input filtering; spectral elements and Nek5000;
quasi-Eulerian refinement; mean-field dynamo; solenoidal and compressive
forcing.

## Chunk 1 — reviews and vocabulary papers (2026-10-25)

Sources (20): duraisamy-2019, duraisamy-2021, schekochihin-2022,
vadrot-2023-b, goc-2021, domingo-2023, vicentecruz-2023, velamartin-2022,
menter-2022, haering-2022, dzanic-2022, flad-2017, krais-2021, fowler-2022,
griffin-2023, lozanoduran-2022, agrawal-2022, beck-2023, li-2022,
agdestein-2025. 55 concept pages plus the registry, 1815 bibliography
entries. Deep lint A1–A7 over all 75 pages done.

### Decisions for the human

1. **Bundle name and scope.** The bundle is `turbulence-modelling` (the
   archive's spelling) and takes the whole archive, including turbulent
   combustion, MHD and plasma turbulence, and DG/FR numerics (D30). Rename
   or narrow it now if you want: the slug sets every path.
2. **Periodic-hill period: $9h$ or $9.5h$?** Haering et al. (2022, §V B)
   print the domain of the ERCOFTAC case UFR 3-30 as "$9.5h\times3.035h\times
   4.5h$"; Dzanic et al. (2022, §3.1) give $9h$ crest to crest for the
   Fröhlich et al. configuration. Opened as a contradiction at drafting,
   moved to Qualifications on
   [periodic hill](wiki/benchmarks/periodic-hill.md) by the deep lint (the
   papers make no claim about each other's domain). The auditor found that
   the ERCOFTAC knowledge-base page of UFR 3-30 gives $9h$; that web page
   is not an ingested source and is not used as evidence in the wiki. If
   you rule the $9.5h$ a printed slip, the qualification can say so.
3. **WMLES cost exponent, $Re^{4/3}$ against $Re^{1.1}$.** Opened as a
   contradiction at drafting on
   [grid-point requirements](wiki/results/les-grid-point-requirements.md),
   moved to Qualifications by the deep lint: Goc et al. (2021, §4) assume
   their own time-step scaling for an aircraft at chord Reynolds number,
   Griffin et al. (2023) and Vadrot et al. (2023b) quote Yang & Griffin
   (2021) for a flat plate. Ingesting Yang & Griffin (2021) would settle
   the exponent; it is on the bibliography frontier.
4. **Three MHD pages carry `status: hypothesis`**
   ([dynamic alignment](wiki/properties/dynamic-alignment.md),
   [tearing-mediated turbulence](wiki/results/tearing-mediated-mhd-turbulence.md),
   [small-scale dynamo](wiki/results/small-scale-dynamo.md)), because
   Schekochihin (2022) calls these theories "hotly debated … still subject
   to verification" (§8.2) and the dynamo evidence "tentative" (§13).

### Contradictions

None open. Two opened at drafting and moved to Qualifications (items 2 and
3 above). Near-conflicts recorded as qualifications with both sides
attributed: Beck & Kurz (2023) against Agdestein & Sanderse (2025) on
whether a closure must be trained inside the solver (different
discretizations); Duraisamy et al. (2019) "enforces" against Duraisamy
(2021) "promotes" model consistency; Haering et al. (2022) against
Dzanic et al. (2022) on numerical dissipation and PANS; Vela-Martín (2022,
isotropic turbulence) against Li & Liu (2022, rotating RANS flow) on
backscatter.

### Printed slips (recorded on the Source pages)

- schekochihin-2022: Eq. (7.17) prints $\varepsilon^{-3/4}$ (dimensionally
  $\varepsilon^{-1/4}$); §12.5.2 decay exponent $t^{-1/2}$ against $t^{-2/3}$
  from the printed exponents; p. 111 (§13.3.4) and footnote 79 print
  positive $Rm$ exponents for $\lambda_R$ against Eq. (13.9).
- flad-2017: filter width printed as a volume; $C_S$ squared in App. A–B,
  unsquared in C–D; dynamic procedure (D.2/D.4) sign and unsquared width
  ratio; Eq. C.3 drops the plateau term.
- dzanic-2022: Eq. 11 destruction term dimensionally short of $\omega_u$;
  Eq. 23 not the log transform of Eq. 11; DNS spanwise resolution ratio.
- krais-2021: Eq. 31 weight ratio inverted; Eq. 46 interpolation matrices
  swapped; Eq. 64 flux arguments; Fig. 20 legend off by one power of two.
- vicentecruz-2023: Eq. 23 sign, Eq. 38 missing $4\pi k^2$, Eq. 39 missing
  $\nu$.
- beck-2023: Eq. 18 reward exponent sign (always $\ge1$ as printed).
- fowler-2022: Eq. 3.6 leading minus.
- griffin-2023: Eq. 1.2 damping exponent sign; $\kappa$ printed "4.1";
  "4Δ" against 3.6Δ.
- goc-2021: viscous stress without the factor 2; "<4 h" and "7.5 days"
  against Table 1.
- haering-2022: Eq. 1 short of $\nu^2$; the $9.5h$ period (item 2).
- lozanoduran-2022: twelve number and label slips ($m\approx-1/7$, $+5/6$,
  $\alpha_q$ for $\alpha_p$, Re values, figure captions).
- menter-2022, velamartin-2022, agdestein-2025, agrawal-2022,
  duraisamy-2019, duraisamy-2021, domingo-2023, vadrot-2023-b, li-2022:
  minor slips (labels, cross-references, reference-list defects).

### Identity and metadata

- No archive defects: 131 distinct works, no byte copies, no misfiled
  papers. Twelve files carried preprint DOIs (Research Square, SSRN,
  conference); their published identities were taken from Crossref and
  checked against page 1.
- Versions read in chunk 1: eight arXiv preprints (duraisamy-2019,
  schekochihin-2022, dzanic-2022, flad-2017, krais-2021, lozanoduran-2022,
  beck-2023, agdestein-2025), four CHORUS accepted manuscripts
  (duraisamy-2021, vadrot-2023-b, haering-2022, agrawal-2022), two HAL
  author manuscripts (domingo-2023, vicentecruz-2023), six versions of
  record. Locators are those of the version read.

### Bibliography

1815 entries from 2083 printed references; 119 aliases, 42 verified
silences, 6 printed duplicates folded (haering Girimaji [22]/[34],
duraisamy-2021 Mishra [32]/[79], four pairs in domingo-2023), `FLAGS: 0`,
`--dupes` clean. Keys printed with a Source slug for a different work were
re-keyed (`cai-2022-b`, `li-2022-b`, `liu-2022-b`, `schekochihin-2022-b`,
`bae-2022-b`, `sirignano-2023-b`, `goc-2021-b`, `goc-2021-c`). Calls left to
the human:

1. vicentecruz-2023 prints Lilly's NCAR 1966 title with the 1967 IBM
   symposium venue and year; folded by title into `lilly-1966` (it could be
   `lilly-1967`).
2. `wu-2018-e` (duraisamy-2021, "in preparation") is probably the study of
   the arXiv preprint `wu-2018-d`; kept distinct (preprint rule).
3. A "Pope 2001, IOP" citation was folded into the book `pope-2000`.
4. menter-2022's printed DOIs for Ge 2015 (resolves to a dissertation) and
   Suluksna 2009 (resolves to Int. J. Heat Fluid Flow) disagree with the
   printed venues; kept as printed, with notes.
5. beck-2023 cites its own published version (ref. [84]); the entry is kept
   without a self-`citedby`, as the linter requires.

### Bundle fit (D17 candidates, no copy made)

- krais-2021 (FLEXI) and flad-2017 (kinetic-energy-preserving DG): also in
  the subject of `weno-teno`, which has a FLEXI page of its own.
- schekochihin-2022 (MHD turbulence theory): `fusion-mhd-simulation` or
  `astrophysical-simulation-codes`.
- domingo-2023 (DNS of turbulent combustion): peripheral to closure
  modelling.

### Candidate pages (kept inline until a second source)

Kolmogorov flow; equipartition spectrum; split forms and summation by
parts; polynomial de-aliasing; flux reconstruction and PyFR; quasi-DNS;
commutation error and computational subgrid stress; approximate
deconvolution; Lagrangian dynamic and anisotropic minimum-dissipation
models; variational multiscale LES; detached-eddy simulation; resolution
tensor and modelled-stress depletion; quadratic constitutive relation;
transition hysteresis; circular cylinder at $Re_D=3900$; Gaussian bump;
dynamic slip and integral wall models; extrapolation theorem; reconnection
and plasmoids; Saffman-type invariants; weak and imbalanced MHD turbulence.
