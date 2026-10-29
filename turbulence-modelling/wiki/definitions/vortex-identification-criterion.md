---
type: Definition
title: "Vortex identification criteria"
description: "Scalar or vector fields of the velocity gradient whose iso-surfaces mark vortices: vorticity magnitude, Q, lambda-2, swirling strength, Omega, Rortex, and a symbolic-regression indicator of characteristic speeds; as the sources print them, with their thresholds, shear contamination, use in comparing schemes and closures, and use in mesh adaptation."
status: established
aliases: [vortex criterion, vortex identification, Q-criterion, Q criterion, lambda-2 criterion, λ2 criterion, Omega criterion, Ω criterion, Rortex, Liutex, swirling strength, vortex indicator]
tags: [dns, les, mesh-adaptation, symbolic-regression, benchmark]
timestamp: 2026-10-29T05:13:00Z
---

# Vortex identification criteria

A **vortex identification criterion** is a field computed from the local
velocity-gradient tensor $A_{ij}=\partial_ju_i$, split into the strain-rate
tensor $S_{ij}$ and the rotation-rate tensor $\Omega_{ij}$ (registry §1),
whose iso-surface or sign is taken to mark a vortex. In the sources of this
bundle the criteria serve three purposes: to visualize the resolved
structures of a DNS, LES or hybrid simulation; to compare schemes and
closures by the structures they resolve; and, in one source, to decide where
a mesh is refined. [Li et al. (2024b)](/sources/li-2024-f.md) (§III.D.3),
following a classification they cite to Liu et al., order the Eulerian
criteria in three generations: vorticity magnitude, then the
velocity-gradient invariants such as $Q$, then the rigid-rotation measure
Rortex. [Lv et al. (2025)](/sources/lv-2025.md) (§I), after Epps (cited),
separate Eulerian region-based criteria from Lagrangian ones (ridges of the
finite-time Lyapunov exponent, Lagrangian-averaged strain).

## The criteria as the sources print them

All symbols below except $S_{ij}$, $\Omega_{ij}$, $\omega_i$ and $A_{ij}$
are page-local; $\lambda_2$ and $\lambda_{ci}$ are not the registry's Taylor
microscale $\lambda$.

- **Vorticity magnitude** $\lvert\boldsymbol\omega\rvert$, "first
  generation", whose iso-surface shows the vortex tube (Li et al. 2024b,
  §III.D.3, Eq. 5).
- **$Q$ criterion**, the second invariant of $A_{ij}$ from the
  Cauchy–Helmholtz split, positive where rotation exceeds strain:
  $$Q=\tfrac12\big(\Omega_{ij}\Omega_{ij}-S_{ij}S_{ij}\big)=\tfrac14\big(\lvert\Omega\rvert^2-\lvert S\rvert^2\big),$$
  the second form in the registry's magnitudes with the factor two
  *(compiler check, not in the sources)*. Li et al. (2024b, Eq. 6),
  [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md) (§III F,
  Eqs. 31–32) and [Klose et al. (2025)](/sources/klose-2025.md) (§4)
  print $Q=\tfrac12(\lVert\boldsymbol\Omega\rVert^2-\lVert\mathbf S\rVert^2)$,
  the last without saying which norm; the first form above is that print
  with Frobenius norms. [Wang et al. (2024c)](/sources/wang-2024-j.md)
  (§III.D) use the same invariant as the coefficient $Q_A$ of the
  characteristic polynomial $\Lambda^3+P_A\Lambda^2+Q_A\Lambda+R_A=0$ of
  $A_{ij}$ (registry §11), with $P_A=-\mathrm{tr}A$ and $R_A=-\det A$; for
  divergence-free flow $Q_A=-\tfrac12A_{ij}A_{ji}$, which equals the $Q$
  above *(compiler check, not in the sources)*. As a history,
  [Kim & Leonard (2024)](/sources/kim-2024-b.md) (§4.8) date the first
  report of the $Q$ criterion to the 1988 Summer Program of the Center for
  Turbulence Research (Hunt et al., cited).
- **$\lambda_2$ criterion** of Jeong & Hussain (cited): vortex cores are
  the regions where $\lambda_2$, the second eigenvalue of
  $\mathsf J=S_{ik}S_{kj}+\Omega_{ik}\Omega_{kj}$ (page-local), is negative.
  [Luckring & Rizzi (2024)](/sources/luckring-2024.md) (nomenclature;
  Fig. 43, a DNS of a wing section with hairpin vortices after a trip)
  define it as the "second eigenvalue of the tensor $J=[\Omega^2+S^2]$";
  [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) (§5.1.2,
  Fig. 9) take "the second largest eigenvalue in absolute value" in their
  text and "the second largest eigenvalue" in the figure caption, for a
  visualization of filtered forced turbulence;
  [Pereira et al. (2021)](/sources/pereira-2021.md) (Fig. 7) plot
  iso-surfaces $-\lambda_2=2.5$, 5.0 and $10.0\times10^4$ in a
  Rayleigh–Taylor mixing layer; [Fureby & Nilsson (2023)](/sources/fureby-2023.md)
  (their ref. [74]) plot $\lambda_2$ iso-surfaces of a ramjet LES and
  call $\lambda_2$ "the second invariant of the velocity gradient".
- **$\Delta$ and swirling-strength ($\lambda_{ci}$) criteria**, which Lv
  et al. (2025, §I) list, after Chong et al. and Zhou et al. (cited), as
  criteria representing local streamline patterns, without a formula.
- **$\Omega$ criterion** of Liu et al. (cited), the share of rotation in
  the velocity-gradient norm, printed by [Zhang et al. (2024)](/sources/zhang-2024.md)
  (§3.2, Eq. 14) with the small positive number $\epsilon_\Omega$ of Dong
  et al. (cited):
  $$\Omega_{\mathrm v}=\frac{\Omega_{ij}\Omega_{ij}}{S_{ij}S_{ij}+\Omega_{ij}\Omega_{ij}+\epsilon_\Omega}\in[0,1),$$
  translated from $\lVert B\rVert_F^2/(\lVert A\rVert_F^2+\lVert B\rVert_F^2+\varepsilon)$
  with $A$, $B$ the symmetric and antisymmetric parts. Both Zhang et al.
  (2024) and Lv et al. (2025, §V) use the iso-value or threshold 0.52; Lv
  et al. describe the criterion as representing "vortical vorticity" and
  print no formula for it.
- **Rortex**, "third generation" (Li et al. 2024b, §III.D.3, Eq. 7): the
  rigid-rotation strength $R_{\mathrm x}$ about the unit vortex-axis vector
  $\boldsymbol r_{\mathrm x}$, plotted as iso-surfaces of
  $\lVert R_{\mathrm x}\boldsymbol r_{\mathrm x}\rVert$. Its integral
  curves, Rortex lines, give the rotation axis and the core "independently
  of any threshold", an advantage the authors state over scalar criteria.

## Shear contamination and thresholds

Li et al. (2024b, §III.D.3, Fig. 7) compare the three generations on the
IDDES field of the [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
at five thresholds (0.05, 0.2, 0.5, 5.0, 10.0, made dimensionless with the
free-stream sound speed and the mean aerodynamic chord). Vorticity and $Q$
iso-surfaces "surround the walls" in the boundary layer: both mark shear
as vortex. Raising the $Q$ threshold reduces this contamination at the
cost of weak vortices, and may not remove it under strong shear. Rortex is
contaminated at 0.05 and 0.2, but at 0.5 the contamination is "well
eliminated" while weak vortices are kept, and that value is used for the
rest of the paper. The authors state that Rortex "theoretically" performs
better because it defines the vortex by the rigid rotation of the fluid
element. Lv et al. (2025, §I) add that criteria such as $Q$ need case- and
grid-sensitive thresholds, and that some "might fail to capture dissipative
vortices with scales smaller than the grid scale", which leaves small
vortices under-resolved when a criterion drives refinement.

The sources normalize their thresholds differently, so the printed values
are not comparable across flows:

| Criterion and value | Normalization | Flow | Source |
|---|---|---|---|
| $Q=0.5$ | not stated on the Source page | gas-kinetic channel LES | [Zhao et al. (2021)](/sources/zhao-2021-c.md), §V D, Figs. 16–19 |
| $Q=0.05$ | not given on the Source page | helicopter-rotor tip vortex | [Han et al. (2022)](/sources/han-2022-c.md), §4.1, Fig. 13 |
| $Q_A=0.5$ | not stated on the Source page | supersonic boundary layer, LES, DES and SAS | Wang et al. (2024c), §III.C, Fig. 4 |
| $Q=5\ \mathrm{s^{-2}}$ | dimensional | cylinder wake, hybrid RANS/LES | [Guo & Wang (2025)](/sources/guo-2025.md), §3.1, Figs. 12–15 |
| $Q=0.02u_0^2/r_0$ ($u_0$, $r_0$ the jet inflow velocity and radius) | jet inflow | compressible [round jets](/benchmarks/turbulent-round-jet.md) | [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md), §III B 1, Fig. 9 |
| $Q=20$ | dimensionless Taylor–Green units | [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) | [Sun et al. (2026)](/sources/sun-2026.md), §7.2 |
| $-\lambda_2=2.5$, 5.0, $10.0\times10^4$ | not stated on the Source page | Rayleigh–Taylor mixing layer | Pereira et al. (2021), Fig. 7 |
| $\Omega_{\mathrm v}=0.52$ | dimensionless by construction | compressor tandem cascade, DDES | Zhang et al. (2024), §3.2, Fig. 19 |
| Rortex 0.5 | free-stream sound speed and mean aerodynamic chord | NASA CRM-HL, IDDES | Li et al. (2024b), §III.D.3, Fig. 7 |

## Use as a diagnostic of schemes and closures

In these sources the criterion is the visual evidence of a comparison of
discretizations or closures:

- **Implicit against explicit LES.** Zhao et al. (2021, §V D, Figs. 16–19)
  find that their gas-kinetic implicit LES and one explicit model resolve
  more structures than the other explicit models on $96^3$, and the
  implicit LES more than all explicit models on $128^3$ (see
  [implicit LES](/definitions/implicit-les.md)).
- **Reconstruction schemes.** Han et al. (2022, §4.1, Fig. 13) capture the
  rotor tip vortex to a wake age of $900^\circ$ with WENO-K, $630^\circ$
  with WENO-JS and $150^\circ$ with MUSCL;
  [Wang et al. (2024b)](/sources/wang-2024-i.md) (Fig. 4) find that WENO-JS
  loses small structures of the inviscid Taylor–Green vortex at $t=10$ and
  that two interpolation-based WENO variants do slightly better than a
  reconstruction-based one (see [WENO schemes](/methods/weno-scheme.md)).
  [Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md) (§VII,
  Fig. 6) judge low-Mach corrections of a WENO implicit LES of channel flow
  by the $Q$ structures: one correction produces "fuzzy", dispersed
  vortices near mid-height, and the NEHA variant gives the closest visual
  agreement with a $128^3$ solution (see [CNS3D](/software/cns3d.md)).
- **Subgrid closures.** [Wang et al. (2023c)](/sources/wang-2023-c.md)
  (§IV, Fig. 17) find in the temporal mixing layer that dynamic models give
  larger structures than filtered DNS, the gradient model much smaller
  ones, and their ensemble-calibrated mixed model the closest; in
  [Li et al. (2024)](/sources/li-2024.md) (§V B 2, Fig. 20) both LES models
  give larger structures than filtered DNS, a Fourier neural operator
  becomes unreliable after about 650 time units, and the transformer
  operator reconstructs the small structures better (see
  [neural-operator surrogates](/methods/neural-operator-les-surrogate.md)).
- **Hybrid RANS/LES.** Li et al. (2024b, §III.D.3, Figs. 8–11) report that
  RANS captures only the strongly swirling tip vortices while IDDES
  captures the fine vortices of wall turbulence, free shear layers and
  wakes; Guo & Wang (2025, §3.1) find that filtering and an added length
  scale in their hybrid model restore small vortices in the mid and far
  wake; Wang et al. (2024c, §III.C, Fig. 4) find quasi-streamwise "stem"
  structures on the coarse LES, hairpins on the fine one, few stems with
  DES and more small structures with their modified scale-adaptive model
  (see [detached-eddy simulation](/methods/detached-eddy-simulation.md) and
  [scale-adaptive simulation](/methods/scale-adaptive-simulation.md)).
- **Turbomachinery.** Zhang et al. (2024, §3.2, Fig. 19) identify the
  horseshoe, tip-leakage, tip-separation, passage, trailing-edge-shedding
  and hairpin vortices of a tandem cascade with the $\Omega$ criterion (see
  [compressor cascade](/benchmarks/compressor-cascade.md)).

Wang et al. (2024c, §III.D, Figs. 10–11) go beyond iso-surfaces: joint
distributions of the deviatoric invariants $Q_A^d$ and $R_A^d$ show the
teardrop shape and approach the unstable-focus and unstable-node regions
of the topology chart as the grid is refined.

## Driving mesh adaptation

[Lv et al. (2025)](/sources/lv-2025.md) refine and coarsen a
$P^2$ (degree $N=2$) direct discontinuous Galerkin discretization of
two-dimensional compressible flow every time step by a vortex indicator
that the same group found with symbolic regression (Feng et al., an SSRN
preprint cited as their ref. 13; see
[symbolic-regression closures](/methods/symbolic-regression-closure.md)
for the tool, used here for classification, not closure). The features are
the $x$- and $y$-gradients of two characteristic speeds $\Lambda_1$ (an
eigenvalue $u\pm c_{\mathrm s}$ of the $x$-direction flux Jacobian) and
$\Lambda_2$ ($v\pm c_{\mathrm s}$, $y$-direction), with $c_{\mathrm s}$ the
sound speed, and the grid scale $h$; the labels are vortex and non-vortex;
the regression used 10 000 samples and PySR with $+$, $-$, $\times$ and
squaring (§IV A 1, Eqs. 17–23). Writing $\mathsf G_\Lambda$ for the matrix
of gradients, $(\mathsf G_\Lambda)_{ab}=\partial_b\Lambda_a$ (page-local,
as are $\Lambda_a$, $c_{\mathrm s}$ and the indicator $I_{\mathrm{SR}}$),
the post-processed indicator is (Eq. 25)

$$I_{\mathrm{SR}}=\tanh\Big(-\Big[\underbrace{(\partial_x\Lambda_1-\partial_y\Lambda_2)^2+4\,\partial_y\Lambda_1\,\partial_x\Lambda_2}_{\text{base term}}+\underbrace{h^2\big(\partial_x\Lambda_1\,\partial_y\Lambda_2-\partial_y\Lambda_1\,\partial_x\Lambda_2\big)}_{\text{activation term}}\Big]\Big).$$

The authors read a negative base term as rotation of the local
characteristics, a vortex core, and the activation term as their
"departure", a vortex boundary, which on coarse grids helps to detect
incipient, small or dissipated vortices (§IV A 1). The base term is the
discriminant $(\mathrm{tr}\,\mathsf G_\Lambda)^2-4\det\mathsf G_\Lambda$ and
the activation term $h^2\det\mathsf G_\Lambda$, so a negative base term
means complex eigenvalues of $\mathsf G_\Lambda$ *(compiler check, not in
the sources)*. The
contribution of the paper is the evaluation of the indicator on
quadrilateral grids with hanging nodes, by direction- and area-weighted
averages of neighbour cell averages (§IV A 2, Eqs. 26–31), with
refinement where $I_{\mathrm{SR}}>0.04$, coarsening elsewhere, at most two
or three levels, $L^2$-projection transfer and fine-side face quadrature for
conservation (§IV B, Algorithm 1; see
[mesh adaptation](/methods/mesh-adaptation.md)).

Results, against refinement by the $\Omega$ criterion (threshold 0.52) and
uniform coarse and fine grids, with no turbulence model and laminar or
under-resolved two-dimensional flows (§V, Tables I–III):

| Case | coarse uniform | fine uniform | $\Omega$-driven | $I_{\mathrm{SR}}$-driven | serial CPU time, min |
|---|---|---|---|---|---|
| [square cylinder](/benchmarks/square-cylinder-flow.md), $M=0.3$, $Re=150$ | 12.05 | 230.37 | 40.88 | 43.58 | Table I |
| Kelvin–Helmholtz double shear layer, inviscid | 2.73 | 8.37 | 12.53 | 26.03 | Table II |
| [NACA 0012](/benchmarks/naca-0012-airfoil.md), $M=0.3$, $15^\circ$ | 60.83 | 415.01 | 62.27 | 65.40 | Table III |

On the cylinder and the airfoil the adaptive runs save 81–85% of the
fine-grid time. On the Kelvin–Helmholtz case the indicator gives "the
highest vortex resolution" (Figs. 8–9); on the airfoil the $\Omega$-driven
run "exhibits quantifiable deviations in both the morphology and size of
the vortices", which the authors attribute to the $\Omega$ criterion being
less able to capture dissipative vortices (§V C); no quantity is given.

## Qualifications

- **Lv et al. (2025): cost statements side by side.** The abstract and
  conclusion claim high vortex resolution "with slight increase in
  computational overhead"; Table II prints 26.03 min for the indicator-driven
  run against 8.37 min on the fine uniform grid and 2.73 min on the coarse
  one, and §V B calls it "relatively costly but still acceptable". With
  three refinement levels on the $40\times40$ base grid the finest
  adaptive cell is $1/320$ of the domain, finer than the $100\times100$
  fine grid *(compiler check, not in the sources)*.
- **Lv et al. (2025): printed forms.** The raw regression result (Eq. 24)
  carries a factor $8.316^2$ inside the tanh, a coefficient 4.2945 on
  $\partial_y\Lambda_1\,\partial_x\Lambda_2$ and only the term
  $-h^2\,\partial_x\Lambda_1\,\partial_y\Lambda_2$, so it is not
  algebraically equal to the post-processed Eq. (25) that the algorithm
  uses *(compiler check, not in the sources)*; the post-processing step is
  not shown. The subsection on time integration is headed "Implicit
  temporal discretization" and describes the explicit SSP-RK3 scheme
  (§III B). The airfoil Reynolds number is $10^6$ in the text and $10^5$ in
  the captions of Figs. 12–13.
- **$\lambda_2$ described two ways.** Luckring & Rizzi (2024) and
  Agdestein & Sanderse (2025) print $\lambda_2$ as an eigenvalue of
  $\mathsf J$; Fureby & Nilsson (2023) call it "the second invariant of
  the velocity gradient". Agdestein & Sanderse print "second largest
  eigenvalue in absolute value" (text) and "second largest eigenvalue"
  (caption).
- **Printed forms of $Q$.** Luckring & Rizzi (2024, nomenclature) print
  $Q=\tfrac12(\lVert\Omega\rVert-\lVert S\rVert)$ without squares on the
  norms. [Kang & Lee (2024)](/sources/kang-2024.md) print the threshold of
  one figure as "$Q=2u_\infty/\delta_0$" in §III and as
  $Q=2u_\infty^2/\delta_0^2$ in the caption of Fig. 8.

# Citations

- [Li et al. (2024b)](/sources/li-2024-f.md) — §III.D.3, Eqs. (5)–(7), Figs. 7–13 (three generations, shear contamination, thresholds, Rortex lines, RANS against IDDES).
- [Lv et al. (2025)](/sources/lv-2025.md) — §I (classification, threshold dependence); §III B; §IV A 1, Eqs. (17)–(25); §IV A 2, Eqs. (26)–(31); §IV B, Algorithm 1; §V, Tables I–III, Figs. 5–13.
- [Zhang et al. (2024)](/sources/zhang-2024.md) — §3.2, Eq. (14), Fig. 19 ($\Omega$ criterion).
- [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md) — §III F, Eqs. (31)–(32) ($Q$ printed).
- [Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md) — §VII, Fig. 6 ($Q$ structures of low-Mach corrections).
- [Klose et al. (2025)](/sources/klose-2025.md) — §4 ($Q$ printed, norms unspecified).
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — §III.C, Fig. 4; §III.D, Figs. 10–11 (invariants of the velocity gradient).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §4.8 (first report of $Q$, cited).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — nomenclature; Fig. 43 ($\lambda_2$ of a cited DNS). Review.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §5.1.2, Fig. 9 ($\lambda_2$).
- [Pereira et al. (2021)](/sources/pereira-2021.md) — Fig. 7 ($\lambda_2$ iso-surfaces).
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — $\lambda_2$ iso-surfaces, described as an invariant (their ref. [74]).
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §V D, Figs. 16–19.
- [Han et al. (2022)](/sources/han-2022-c.md) — §4.1, Fig. 13.
- [Wang et al. (2024b)](/sources/wang-2024-i.md) — Fig. 4.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §IV, Fig. 17.
- [Li et al. (2024)](/sources/li-2024.md) — §V B 2, Fig. 20.
- [Guo & Wang (2025)](/sources/guo-2025.md) — §3.1, Figs. 12–15.
- [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md) — §III B 1, Fig. 9.
- [Sun et al. (2026)](/sources/sun-2026.md) — §7.2 ($Q=20$ iso-surfaces).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §III, Fig. 8 (threshold printed two ways).
