---
type: Definition
title: "Boundary variation diminishing (BVD)"
description: "BVD is the selection principle that picks, cell by cell, the candidate reconstruction (polynomial versus THINC) with the smallest jump of interface values, hence the least Riemann-flux dissipation; the page records its definitions, an interface-wise variant, a compact DG-limiter form, a relaxed troubled-element test and a neural-network predictor of the selection."
status: established
aliases: [BVD, BVD principle, boundary variation diminishing algorithm]
tags: [reconstruction, low-dissipation, interface-capturing, finite-volume, riemann-solver]
timestamp: 2026-10-24T05:59:00Z
---

# Boundary variation diminishing (BVD)

**Boundary variation diminishing** (BVD), introduced by Sun, Inaba and Xiao
(2016) as recalled by the sources, is a parameter-free rule for hybridizing
reconstructions in a Godunov-type finite-volume scheme: each cell carries two
(or more) candidate reconstructions, typically a polynomial one (linear, WENO or
TENO) and a [THINC](/methods/thinc-reconstruction.md) one, and the candidate
selected is the one that minimizes the jump $[\![u]\!]_{i+1/2}=u^+_{i+1/2}-u^-_{i+1/2}$
of the reconstructed values at the cell boundaries
([Takagi et al. (2022)](/sources/takagi-2022.md), §1;
[Fu (2023)](/sources/fu-2023.md), §3.6).

## Why the interface jump

Fu (2023) and Huang et al. (2026) write the finite-volume flux in the unified form

$$\hat f_{i+1/2}=\tfrac12\big(f(u^-_{i+1/2})+f(u^+_{i+1/2})\big)-\tfrac12\lvert\tilde a_{i+1/2}\rvert\big(u^+_{i+1/2}-u^-_{i+1/2}\big),$$

where $\tilde a_{i+1/2}$ is an averaged signal speed fixed by the Riemann solver
(Roe, Rusanov, HLL, HLLC) ([Fu (2023)](/sources/fu-2023.md), §3.6, Eq. (29),
printed with the symbol $\tilde\partial_{i+1/2}$; the same form in
[Huang et al. (2026)](/sources/huang-2026.md), §2.1, Eq. (2.5), which prints the
jump with the wrong sign). The upwind dissipation of the flux is proportional to
the interface jump, so the candidate with the smaller jump is the less
dissipative one; [Deng (2023)](/sources/deng-2023.md) (Remark 7.2) accordingly
describes BVD as minimizing "the absolute dissipation error at a cell boundary".
*(Compiler check, not in the sources: the proportionality follows from the
printed flux form; the sources do not state a theorem on it.)*

[Wakimura et al. (2024)](/sources/wakimura-2024.md) (§3.2.1, Eq. (26)) give the
same rationale on the scalar model $f=au$: the Riemann flux is
$\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac{\lvert a\rvert}2(u^+-u^-)$, the boundary
variation is $\lvert u^+-u^-\rvert$, and the BVD principle is that it "should be
diminished" to reduce numerical dissipation.

## The minimum-total-boundary-variation selection

Wakimura et al. (§3.2.4, Eqs. (35)–(36)) print the cell-wise selection they take from
Deng et al. (2018) for two candidates A and B in each cell. For a candidate
$\Xi\in\{\mathrm A,\mathrm B\}$ of cell $i$, the total boundary variation is minimized over
the choices $X,Y\in\{\mathrm A,\mathrm B\}$ of the neighbours (page-local symbols):

$$\mathrm{mTBV}^\Xi_i=\min_{X,Y\in\{\mathrm A,\mathrm B\}}\Big(\big\lvert u^{X,-}_{i-1/2}-u^{\Xi,+}_{i-1/2}\big\rvert+\big\lvert u^{\Xi,-}_{i+1/2}-u^{Y,+}_{i+1/2}\big\rvert\Big),$$

where $u^{\Xi,+}_{i-1/2}$ and $u^{\Xi,-}_{i+1/2}$ are the two face values of cell $i$
with candidate $\Xi$ and $u^{X,-}_{i-1/2}$, $u^{Y,+}_{i+1/2}$ those of the neighbours.
Cell $i$ takes A if $\mathrm{mTBV}^{\mathrm A}_i<\mathrm{mTBV}^{\mathrm B}_i$ and B
otherwise, so ties go to B. In MUSCL-THINC-BVD, A is MUSCL with the van Leer limiter
and B is [THINC](/methods/thinc-reconstruction.md) with $\beta_{\mathrm T}=1.6$; in
Adaptive THINC-BVD, A is THINC with $\beta_{\mathrm T}=1.1$ and B THINC with $1.6$.
This answers, for these two schemes, the gap noted under Qualifications: the comparison
uses both faces of the cell and all four neighbour combinations.

[Huang et al. (2025b)](/sources/huang-2025-b.md) (§3.2, Eqs. (24)–(26)) print the same
MUSCL-THINC-BVD selection of Deng et al. (A = MUSCL with the van Leer limiter, B = THINC
with $\beta_{\mathrm T}=1.6$), with the total boundary variation minimized over the four
neighbour combinations, and with two further admission conditions on the THINC candidate:
the normalized position of the cell average in the jump must lie in $(\delta_{\mathrm B},1-\delta_{\mathrm B})$,
$\delta_{\mathrm B}=10^{-8}$ (page-local), and the data must be locally monotone,
$(\bar u_{i+1}-\bar u_i)(\bar u_i-\bar u_{i-1})>0$. THINC is taken only if
$\mathrm{mTBV}^{\mathrm B}_i<\mathrm{mTBV}^{\mathrm A}_i$ strictly, so in their print ties go to
MUSCL, whereas Wakimura et al.'s print sends ties to THINC — a convention difference between
the two prints of the same rule. The decision for cell $i$ needs the five cells
$I_{i-2},\dots,I_{i+2}$, because the neighbours' own candidate values enter
(Huang et al. 2025b, Fig. 2).

## Predicting the selection with a neural network (deepMTBVD)

Huang et al. (2025b) observe that a BVD scheme builds every candidate in every cell before
it selects one (§1, §3.3), and replace the a-posteriori comparison by an a-priori
prediction, the **deepMTBVD** scheme (§3.3, Algorithm 2):

- **Two invariance results.** Conclusion 1 (Appendix A) proves that for strictly monotone
  $\bar u_{i-1},\bar u_i,\bar u_{i+1}$ both the MUSCL (van Leer) and the THINC reconstruction
  in $I_i$ stay strictly between the neighbour averages. Conclusion 2 (Appendix B) proves
  that, if the five averages of the stencil are not all equal, the min–max normalization
  $\tilde u_j=(\bar u_j-\min_S\bar u)/(\max_S\bar u-\min_S\bar u)$ over the five-cell
  stencil $S$ leaves the BVD choice unchanged, because every boundary variation is divided
  by the same range (Eqs. (34)–(35)).
- **The predictor.** A fully connected network with six inputs (the five normalized averages
  and a monotonicity flag that is $0$ at a local extremum), two hidden layers of eight
  sigmoid neurons and one output in $[0,1]$, the probability that the cell should take THINC
  (§3.3.1–3.3.2, Eqs. (29)–(30)); zero inputs are fed where the stencil range is below
  $10^{-15}$ or the flag is $0$. Labels are the choices of MUSCL-THINC-BVD itself on six 1D
  Euler Riemann problems advanced ten SSP-RK3 steps at CFL $0.1$ on four meshes
  (Algorithm 1, Table 6); 8000 training and 2000 validation samples, a weighted focal loss
  that penalizes MUSCL cells predicted as THINC (class weights $1:5$), and a decision
  threshold $0.45$ (Eqs. (31)–(32), Remark 2, Appendices C, E). The network trained on 1D
  Euler data is applied unchanged to every variable, to the five-equation model and, by
  dimensional splitting, in 2D (Remark 1).
- **What is gained.** Only the selected reconstruction is built. On linear advection of
  $\sin(\pi x)$ ($t=10$, 400 to 12800 cells) MUSCL and deepMTBVD converge at second order
  in $L^1$ while MUSCL-THINC-BVD converges at first order (§4.1, Fig. 4). On the Sod, Lax and
  strong Lax tubes, the double Mach reflection, the Mach 3 step, an underwater explosion and a
  shock–R22 bubble the resolution is comparable to that of MUSCL-THINC-BVD and sharper than
  that of MUSCL (§§4.2–4.3). The selection time grows (network inference) and the
  reconstruction time falls; the printed totals are, MUSCL-THINC-BVD against deepMTBVD,
  $40.04$ against $32.67$ s, $55.30$ against $45.01$ s and $45.36$ against $34.51$ s on the
  three 1D tubes with $10^4$ cells (Table 1) and $6265.50$ against $2566.02$ s, $7268.35$
  against $3926.57$ s and $5975.97$ against $3635.13$ s with $10^5$ cells (Table 2); no
  hardware is stated.

## Uses in the sources

- **BVD with TENO.** BVD-TENO5-THINC, the BVD selection between TENO5 and THINC,
  performs better than BVD-WENOZ-THINC (as recalled by
  [Fu (2023)](/sources/fu-2023.md), §3.6); the floating-point treatment that
  restores mirror symmetry for TENO5 has been carried over to BVD schemes
  (§3.8; see [symmetry preservation](/properties/symmetry-preservation.md)).
- **An alternative switch: TENO flags.** [Takagi et al. (2022)](/sources/takagi-2022.md)
  (§1, §3) present [TENO-THINC](/methods/teno-thinc.md) as an alternative to
  BVD: instead of comparing interface jumps of the two candidates, the THINC
  candidate is invoked where the binary stencil flags $\delta_k$ of TENO5 display
  the pattern of a cell containing a discontinuity. Both rules are free of tunable
  parameters; Takagi et al. work in finite difference (on split point
  fluxes), whereas BVD is recalled as a finite-volume rule.
- **Interface-wise BVD inside a Riemann solver.** [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md)
  (§4.2, Eqs. (4.7)–(4.9)) write their shock-stable HLLEM flux as a central part plus a
  dissipation term, $\hat f_{i+1/2}=\tfrac12\big(f(u^-_{i+1/2})+f(u^+_{i+1/2})\big)+D_{i+1/2}$
  (page-local $D_{i+1/2}$), and compute the density *inside $D_{i+1/2}$ only* from the
  combination of MUSCL (P) and THINC (T) interface values with the smallest jump,
  $$\lvert\rho^+-\rho^-\rvert=\min\big(\lvert\rho^{\mathrm T,+}-\rho^{\mathrm T,-}\rvert,\ \lvert\rho^{\mathrm P,+}-\rho^{\mathrm P,-}\rvert,\ \lvert\rho^{\mathrm T,+}-\rho^{\mathrm P,-}\rvert,\ \lvert\rho^{\mathrm P,+}-\rho^{\mathrm T,-}\rvert\big),$$
  an interface-wise selection over all four left/right pairs for one variable, not the
  cell-wise selection recalled above. Whether the central part uses these values is not
  stated. The resulting RHLLEM-LD solver resolves contacts and interfaces more sharply than the
  solvers it is compared with (HLLE and HLLEM) on an isolated
  contact, the blast wave, Titarev–Toro, Richtmyer–Meshkov and Kelvin–Helmholtz tests at
  second order (§5, Figs. 5.1–5.6), and the
  BVD step does not change the robustness of the solver at strong shocks: HLLEM with BVD
  alone stays unstable on the stationary inclined shock, the shock-stable version stays
  stable (Fig. 5.7, §5.7; see [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md),
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **BVD in a two-phase model with phase change.** Wakimura et al. (2024) apply the two
  selections above to the six-equation model of Pelanti and Shyue with infinite-rate
  pressure, temperature and Gibbs relaxation
  ([five- and six-equation models](/definitions/five-equation-model.md)). Reconstruction
  acts on $(\phi_1,\phi_1\rho_1,\phi_2\rho_2,v,p)$, and the BVD switch only on the volume
  fraction and the two partial densities; velocity and pressure always take MUSCL (or THINC
  with $1.1$) (§3.2.4). For a 1D cavitation tube with rarefactions at $\lvert v\rvert=500$
  m/s, THINC with $1.6$ is admissible in the selection only where $\nabla\cdot v<0$, "to
  address the strong rarefaction waves" (§4.1). The BVD schemes capture contacts in about
  3–4 cells, give more developed Richtmyer–Meshkov structures and resolve vapour bubbles
  created by phase change on $200\times200$ cells, where MUSCL needs $400^2$ or $800^2$
  (stated) (§§4.2–4.4; [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md),
  [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)). On the
  1D cavitation tube MUSCL-THINC-BVD differs from MUSCL by at most $1.49\times10^{-6}$ in
  mass fraction at $\lvert v\rvert=2$ m/s and $6.00\times10^{-5}$ at $500$ m/s, and Adaptive
  THINC-BVD "appropriately selects" THINC with $1.1$ at smooth rarefaction waves (§4.1). Their Appendix A orders the floating-point
  operations so that the BVD scheme keeps mirror symmetry
  ([symmetry preservation](/properties/symmetry-preservation.md)).
- **A volume-fraction switch instead.** [Zhang et al. (2024a)](/sources/zhang-2024.md)
  (§3.3) cite symmetry-preserving BVD but switch their WENO–THINC multiphase hybrid by a
  volume-fraction test, not by boundary variation (see [THINC](/methods/thinc-reconstruction.md)).
- **BVD as a troubled-element test.** [Deng, Jiang & Yan (2025)](/sources/deng-2025.md)
  (§3.3, Eqs. (3.7)–(3.9)) use a relaxed BVD criterion not to select a reconstruction but to
  flag DG elements for [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  extending an indicator of Jiang et al. On each non-uniform subcell they compare the total
  boundary variation of the first-order and of the third-order linear reconstruction,
  $$\mathrm{TBV}^{\mathrm U}_i=\lvert\bar u_i-\bar u_{i-1}\rvert+\lvert\bar u_i-\bar u_{i+1}\rvert,\qquad
  \mathrm{TBV}^{\mathrm P}_i=\lvert[\![u^{\mathrm P}]\!]_{i-1/2}\rvert+\lvert[\![u^{\mathrm P}]\!]_{i+1/2}\rvert$$
  (page-local symbols; P the quadratic reconstruction of the non-uniform
  [normalised-variable diagram](/definitions/normalised-variable-diagram.md)), and call the
  subcell discontinuous when $\mathrm{TBV}^{\mathrm P}_i-\mathrm{TBV}^{\mathrm U}_i>\max\big(10^{-6},10^{-4}(\lvert\bar u_{i-1}\rvert+\lvert\bar u_i\rvert+\lvert\bar u_{i+1}\rvert)\big)$,
  on the rationale, attributed to earlier BVD papers, that high-order linear schemes give the
  smaller boundary variation in smooth regions and the larger one at discontinuities. A 1D element
  is troubled if any subcell is, a 2D element if more than half are; the test runs at every
  Runge–Kutta stage and switches whole elements to the [ROUND](/methods/round-scheme.md) scheme.
  Which variables of the Euler system are tested is not stated, and the threshold makes the
  method scale-dependent (§3.3; [troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
- **A compact BVD inside a DG limiter.** [Huang et al. (2025a)](/sources/huang-2025.md)
  (§3.2.3, Eqs. (22)–(24)) use BVD to choose, in a DG troubled cell, between a TENO and a
  THINC replacement polynomial of the [TENO-THINC limiter](/methods/teno-thinc.md). Let
  $p_i$ denote the DG polynomial of $I_i$ (page-local). The total boundary variation of a
  candidate $p^\Xi_i$, $\Xi\in\{\mathrm{TENO},\mathrm{THINC}\}$, is measured against the
  *unlimited* traces of the neighbours,
  $$\mathrm{TBV}^\Xi_i=\lvert p^\Xi_i(x_{i-1/2})-p_{i-1}(x_{i-1/2})\rvert+\lvert p^\Xi_i(x_{i+1/2})-p_{i+1}(x_{i+1/2})\rvert,$$
  and THINC is taken if $\mathrm{TBV}^{\mathrm{TENO}}_i-\mathrm{TBV}^{\mathrm{THINC}}_i>\max\big(10^{-10},10^{-3}(\mathrm{TBV}^{\mathrm{THINC}}_i+\mathrm{TBV}^{\mathrm{TENO}}_i)\big)$,
  thresholds that the authors take from Jiang et al. (2021). Because the neighbour values
  come from the unlimited DG polynomials and not from their reconstructions, the rule needs
  only the three cells $I_{i-1},I_i,I_{i+1}$; the authors call it "significantly simpler"
  than the BVD of Jiang et al., which "requires the reconstructed values of neighboring
  cells" (§1, §3.2.3). In 2D the same rule is applied direction by direction on trace
  polynomials (Eqs. (34)–(36)). On the $1200\times300$ double Mach reflection it selects THINC
  in 6476 cells, 18.7% of the 34681 troubled cells (§5.5, Fig. 6).
- **A contrast: ROUND.** [Deng (2023)](/sources/deng-2023.md) (Remark 7.2)
  sets BVD against the low-dissipative [ROUND schemes](/methods/round-scheme.md),
  which do not minimize the boundary jump but the *overall* error in a cell, by
  admitting both positive and negative second-order (diffusive and anti-diffusive)
  error terms on the [normalised-variable diagram](/definitions/normalised-variable-diagram.md).

## Qualifications

- The original algorithm of Sun, Inaba and Xiao (2016) is still known here only
  as later sources recall it. Wakimura et al. (2024) print in full the
  minimum-total-boundary-variation selection of Deng et al. (2018) for two
  candidates, which they use; whether it coincides with the 2016 rule, and how
  selections with more than two candidates or several stages work, no ingested
  source states. Hu et al. (2022) give a complete formula for their own
  interface-wise, density-only variant, which is a different rule.
- Wakimura et al.'s $\nabla\cdot v<0$ condition on the steep THINC candidate is
  introduced "to address the strong rarefaction waves" of one test, and no run without
  it is shown (§4.1). Their statement that schemes above third
  order "may introduce spurious oscillation error due to the reconstruction of
  primitive variables" (§1), the reason for their second-order candidates, is given
  without evidence.
- Hu et al. do not give the THINC formula, its steepness or the MUSCL limiter
  used in their BVD candidates.
- "Parameter-free" refers to the selection; the THINC candidate carries its
  steepness $\beta_{\mathrm T}$ (1.6 at discontinuities in the cited BVD
  variants, see [THINC](/methods/thinc-reconstruction.md)). The compact DG variant of
  Huang et al. (2025a) and the relaxed indicator of Deng, Jiang & Yan carry absolute and
  relative thresholds of their own.
- Huang et al. (2025b)'s first-order convergence of MUSCL-THINC-BVD on smooth advection is
  shown in a figure only (Fig. 4), and the paper does not say which selection step causes it.
- deepMTBVD's training cases include the Lax data and the strong Lax data that are also two of
  its 1D tests (Table 6, case 6 and case 2 with $u=0$), so those two tests are not out of the
  training distribution. The text reports accuracy "over 98%" on the training and validation
  sets (§3.3.2), while Table 5 gives 0.975 for the adopted class-weight ratio $1:5$ (0.981 for
  plain binary cross-entropy); the two figures are not reconciled in the paper.
- The time saving of deepMTBVD is stated as "up to 40%" (abstract, conclusion) and "10% to
  40%" (Remark 3). From the printed totals of Table 2 the reductions are $59.0\%$, $46.0\%$
  and $39.2\%$, so two exceed the stated bound; Table 1 gives $18.4\%$, $18.6\%$ and $23.9\%$
  *(compiler check, not in the sources)*. Two printed totals are not the sums of their printed
  parts: Table 3 prints $223.87$ s for deepMTBVD on the double Mach reflection, while its
  reconstruction and selection times sum to $88.25+136.62=224.87$ s; Table 4 prints $242.54$ s
  for MUSCL-THINC-BVD on the Mach 3 step, while $212.22+50.32=262.54$ s
  *(compiler check, not in the sources)*. With the summed value the Mach 3 step saving would be
  $17.9\%$ instead of the $11.1\%$ implied by the printed totals.

# Citations

- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1: BVD recalled; §3: TENO-flag switch as alternative.
- [Fu (2023)](/sources/fu-2023.md) — §3.6, Eq. (29): unified flux, BVD-TENO5-THINC; §3.8: symmetry for BVD.
- [Deng (2023)](/sources/deng-2023.md) — Remark 7.2: BVD versus ROUND.
- [Huang et al. (2026)](/sources/huang-2026.md) — §2.1, Eq. (2.5): unified flux form.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §4.2, Eqs. (4.7)–(4.9); §5, Figs. 5.1–5.7: interface-wise BVD of density in the HLLEM dissipation term.
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §1; §3.2.1, Eq. (26); §3.2.4, Eqs. (35)–(36); §§4.1–4.4; Appendix A: canonical-flux rationale, minimum-total-boundary-variation selection, BVD in a six-equation model with phase change.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.3: volume-fraction switch in place of BVD.
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §3.3, Eqs. (3.7)–(3.9), Remark 3.1: relaxed-BVD troubled-element indicator for DG subcell limiting.
- [Huang et al. (2025a)](/sources/huang-2025.md) — §1; §3.2.3, Eqs. (22)–(24); §4.2, Eqs. (34)–(36); §5.5, Fig. 6: compact BVD against unlimited DG traces in the TENO-THINC limiter.
- [Huang et al. (2025b)](/sources/huang-2025-b.md) — §3.2, Eqs. (24)–(26); §3.3, Eqs. (29)–(32), Algorithms 1–2, Remarks 1–3; §§4.1–4.3; Tables 1–6; Appendices A–E: MUSCL-THINC-BVD as printed, deepMTBVD predictor, normalization invariance, timings.
