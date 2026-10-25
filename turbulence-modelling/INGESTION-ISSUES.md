# Ingestion issues — turbulence-modelling

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

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
