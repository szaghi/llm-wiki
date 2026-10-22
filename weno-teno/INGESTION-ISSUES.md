# Ingestion issues — weno-teno

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

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
