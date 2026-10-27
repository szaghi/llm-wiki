---
type: Definition
title: "Shock sensors and troubled-cell indicators"
description: "A shock sensor or troubled-cell indicator is the switch that decides where a scheme adds shock-capturing dissipation or changes its discretization; this page defines the pressure, dilatation–vorticity, modal-decay, density-gradient and TENO-type indicators of the sources, and what each flags wrongly in turbulence."
status: established
aliases: [shock sensor, shock indicator, troubled-cell indicator, troubled-cell detector, discontinuity indicator, Ducros sensor, Jameson pressure sensor, Persson–Peraire indicator, KXRCF indicator, TVB minmod indicator, TENO troubled-cell indicator, filtered shock indicator]
tags: [shock-capturing, numerical-dissipation, compressible, dg, implicit-les, boundary-layer]
timestamp: 2026-10-27T06:08:00Z
---

# Shock sensors and troubled-cell indicators

A **shock sensor** (in DG language a **troubled-cell indicator**) is a
pointwise or element-wise function of the discrete solution that marks
where a discontinuity is present, so that the scheme can act there and
only there: switch on an [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md),
replace a DG element by [finite-volume subcells](/methods/subcell-finite-volume-shock-capturing.md),
apply a limiter, or move from a central or linear scheme to a
[WENO or TENO](/methods/weno-scheme.md) reconstruction. In scale-resolving
simulation of compressible turbulence the sensor decides how much
shock-capturing [numerical dissipation](/properties/numerical-dissipation.md)
reaches the resolved turbulence: a sensor that fires on vortical or
under-resolved turbulent structures turns a low-dissipation scheme into a
dissipative one there, a sensor that misses a shock lets the scheme
oscillate. The sources agree on this role and differ on which quantity
separates shocks from turbulence.

Symbols: $\Psi_i$ the Jameson pressure sensor and $\Phi_i$ the Ducros
factor of registry §11; $s_e$ the Persson–Peraire indicator of an element
and $s_0$ its threshold (as on the subcell page);
$\mathrm{IS}_k$ the Jiang–Shu-type smoothness indicator of stencil or
polynomial $k$ (registry §11). Page-local, shared with the
[WENO](/methods/weno-scheme.md) page: $\gamma^{\mathrm T}_k$ the
scale-separated smoothness measure of TENO and
$\chi^{\mathrm T}_k=\gamma^{\mathrm T}_k/\sum_l\gamma^{\mathrm T}_l$ its
normalized form (the sources' $\gamma_k$, $\chi_k$, marked because
$\gamma$ is the ratio of specific heats and $\chi$ the Spalart–Allmaras
ratio), $C_T$ the cut-off threshold; $q$ an exponent, $\epsilon$ a small
regularizer; $U_\infty$ and $\delta_0$ the free-stream velocity and inflow
boundary-layer thickness.

## Pressure-jump sensors

**Jameson–Schmidt–Turkel sensor.** The normalized second difference of
pressure,
$$\Psi_i=\frac{\big|\sum_k(p_i-p_k)\big|}{\sum_k(p_i+p_k)}$$
over the neighbours $k$ of node $i$, switches the second-difference
dissipation of JST-type schemes; in the unstructured LD2C scheme its cap
makes the scheme first-order upwind at shocks
([Carlsson et al. 2023](/sources/carlsson-2023.md), §2.2.3, Eqs. 12–13; see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).
OpenCFD-SCU sums a one-dimensional form,
$|{-p_{i-1}}+2p_i-p_{i+1}|/(p_{i-1}+2p_i+p_{i+1})$, over the three grid
directions and selects by two thresholds (0.02 and 0.1) a linear
seventh-order upwind, a seventh-order WENO or a fifth-order WENO flux
([Dang et al. 2022](/sources/dang-2022.md), §2.2.3, Eqs. 41–43; see
[WENO](/methods/weno-scheme.md)).

**The same sensor in a DG element.** [Gao et al. (2022)](/sources/gao-2022.md),
§3.2, Eqs. (12)–(13), adapt it to the DGSEM: at each node, with
$p_{\min}$ and $p_{\max}$ the smallest and largest neighbouring nodal
pressures,
$$\Psi_{ijk}=\frac{|p_{\min}-2p_{ijk}+p_{\max}|}{|p_{\min}+2p_{ijk}+p_{\max}|},$$
averaged over the element with the volumes of the $(N+1)^3$ finite-volume
subcells as weights; an element above the threshold (value not printed)
becomes finite volume. The JST-type indicator is also one of the a priori
indicators of the FLEXI switching scheme of
[Krais et al. (2021)](/sources/krais-2021.md), §4.3, §7.2.

**Pressure ratio of a Riemann solver.** In a real-gas hybrid,
[Xu et al. (2026)](/sources/xu-2026.md), Eq. (18), flag a compressive jump
when the interface pressure ratio given by the primitive-variable Riemann
solver exceeds 0.05 with a compressive wave speed; flagged cells take the
conservative WENO update (see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).

## Dilatation–vorticity sensors (Ducros type)

**The Ducros factor.** The ratio of squared dilatation to squared
dilatation plus squared vorticity,
$$\Phi_i=\frac{(\nabla\cdot\boldsymbol u)^2}{(\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2+\epsilon},$$
is near 0 where vorticity dominates (turbulence away from shocks) and near
1 at inviscid shocks (Carlsson et al. 2023, Eq. 14; Gao et al. 2022,
Eqs. 14–15, with the element value again a volume-weighted mean). Its
uses in the sources:

- as the switch between energy-preserving central schemes and WENO in
  [STREAmS](/software/streams.md) ([Cogo et al. 2022](/sources/cogo-2022.md), §2);
- as the homotopy parameter that blends an eighth-order kinetic-energy-
  and entropy-preserving central scheme with a third-order upwind flux in
  SPADE, and as a multiplier of the Persson–Peraire-driven artificial
  diffusivity in the modal DG code CODA
  ([Chapelier et al. 2024](/sources/chapelier-2024.md), §III.B.a–b, h);
- as the switch of a KGP/HLLC hybrid for real-gas flow, where it is
  "mostly activated by the oscillations" of the central scheme rather than
  by a physical jump ([Bernades et al. 2023](/sources/bernades-2023.md),
  §4.1.1);
- multiplied with the pressure sensor, $\Psi_i\Phi_i$, in LD2C, because
  $\Phi_i$ alone "cannot separate shocks from small dilatations" and fires
  wherever vorticity is negligible; the authors state that the product
  distinguishes shocks from compressible turbulence (Carlsson et al. 2023,
  §2.2.3, Eqs. 14–15);
- in the modified Jameson dissipation of the EDGE solver used for implicit
  LES of supersonic twin jets, where the second-difference coefficient is
  $1.5\,\Phi$ times a pressure-jump ratio and the fourth-difference
  coefficient carries the factor
  $\tfrac12+\tfrac12\min(\max\Phi,\max\Theta)$, with
  $\Theta=|\nabla\times\boldsymbol u|^2/((\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2)$
  the vortical complement (page-local)
  ([Ahn et al. 2023](/sources/ahn-2023.md), §III, Eqs. 1–6; formulas on
  [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).

A dilatation–vorticity sensor of Fernandez et al., with time and space
relaxation factors 0.7, selects the elements of the DG/FV blend of
[Klose et al. (2025)](/sources/klose-2025.md), §2 (formula not printed).

**Regularized and signed variants.** Gao et al. (2022, §3.2) recall
Pirozzoli's choice $\epsilon=(U_\infty/\delta_0)^2$, which filters
small-amplitude dilatation outside the boundary layer, and write two
variants that flag compressions only (Eqs. 16–17, idea credited to Larsson
et al. and Lusher & Sandham):
$$\Phi^{\mathrm s}=\frac{-\nabla\cdot\boldsymbol u}{|\nabla\cdot\boldsymbol u|+|\nabla\times\boldsymbol u|+U_\infty/\delta_0},\qquad
\Phi^{\mathrm s}_{a}=\frac{-\nabla\cdot\boldsymbol u}{|\nabla\cdot\boldsymbol u|+a_\omega|\nabla\times\boldsymbol u|+U_\infty/\delta_0},$$
($\Phi^{\mathrm s}$, $\Phi^{\mathrm s}_a$, $a_\omega$ page-local; $a_\omega$
the source's case-dependent vorticity scaling $\alpha$). The positive
dilatation of an expansion fan then gives negative values, whereas the
squared form flags expansion fans as it flags weak shocks; the scaled
variant is "not easy to be generalized for different cases". Neither is
used in their final runs.

## Modal-decay and gradient sensors in element methods

**Persson–Peraire.** The share of the element's solution norm carried by
its highest modes,
$s_e=\log_{10}\big[(\rho-\rho_{N-1},\rho-\rho_{N-1})_e/(\rho,\rho)_e\big]$
with $\rho_{N-1}$ the truncation of the density to degree $N-1$, gates a
local modal filter in the flux-reconstruction code ATHOS, with recommended
$s_0\in[-3.7,-2.7]$ at $N=2$ and $[-5.3,-4.3]$ at $N=3$
([Wang 2024](/sources/wang-2024-b.md), §2.3, Eq. 19, Table 2b; values and
results on [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).
The same sensor, with the calibration of Glaubitz et al., drives the
Laplacian artificial viscosity of CODA (Chapelier et al. 2024, §III.B.a;
[Schotte et al. 2026](/sources/schotte-2026.md), §2.2). FLEXI's subcell
switching in the code comparison of Chapelier et al. (§III.B.f) uses
instead the exponential decay rate of the modal coefficients of the
**pressure**. [Jiang et al. (2025)](/sources/jiang-2025.md), §3.1, flag
oscillating cells of the turbulent kinetic energy $k$ at the
under-resolved edge of a boundary layer with an element-resolution
indicator (Persson–Peraire cited) and replace their polynomial by a
Hermite-WENO reconstruction: the indicator here targets a turbulence
variable, not a shock.

**Density gradient.** The entropy-stable artificial viscosity of
[HORSES3D](/software/horses3d.md) is switched by an element-wise
density-gradient sensor, $\int_{\mathrm{el}}\mathcal J|\nabla_\xi\rho|^2$
([Ferrer et al. 2023](/sources/ferrer-2023.md), §4.4, Eq. 19;
[Mateo-Gabín et al. 2022](/sources/mateogabin-2022.md), §6.2–6.3,
Eqs. 127–128, where the Shu–Osher run sets the SVV exponent to zero where
the sensor exceeds 10).

**Hysteresis.** Krais et al. (2021, §4.3) switch an element to finite
volumes above an upper threshold and back below a lower one, which they
state prevents back-and-forth switching and reduces the sensitivity to the
user value (no data shown).

## Troubled-cell indicators of modal RKDG

[Huang & Fu (2024)](/sources/huang-2024.md) and
[Huang et al. (2025)](/sources/huang-2025.md) work with third-order modal
(Legendre) Runge–Kutta DG on uniform Cartesian grids ($N=2$; the sources
write $k$), inviscid Euler tests only. They recall two classical
indicators (Huang & Fu 2024, §4.1–4.2, Eqs. 27–31):

- **TVB minmod.** The cell's interface deviations from its mean are
  compared with the neighbouring mean differences through the modified
  minmod function, which returns its first argument if that is below
  $M_{\mathrm{TVB}}\Delta x^2$ ($M_{\mathrm{TVB}}$ page-local, the source's
  $M$) and the minmod otherwise; the cell is troubled if the modification
  changes anything. A larger $M_{\mathrm{TVB}}$ flags fewer cells, too large
  a value misses genuine troubled cells.
- **KXRCF** (Krivodonova et al.), the normalized jump across the inflow
  boundary $\partial I_i^-$ towards the neighbour $I_l$,
  $$I^{\mathrm{KXRCF}}_i=\frac{\big|\int_{\partial I_i^-}(u^h|_{I_i}-u^h|_{I_l})\,ds\big|}{h^{(N+1)/2}\,|\partial I_i^-|\,\big\|u^h|_{I_i}\big\|},$$
  troubled above 1 ($h$ the radius of the circumscribed circle, the norm
  the maximum over the cell).

They state that both need a critical parameter tied to the solution and
tuned case by case (§1).

**TENO-based troubled-cell indicator.** Huang & Fu (2024, §4.3, Eqs. 32–35)
transfer the stencil selection of TENO to the DG polynomials $p_{i-1}$,
$p_i$, $p_{i+1}$ of a cell and its two neighbours, $k\in\{i-1,i,i+1\}$:
$$\mathrm{IS}_k=\sum_{l=1}^{2}\int\Delta x^{2l-1}\Big(\frac{\partial^lp_k}{\partial x^l}\Big)^2dx,\qquad
\gamma^{\mathrm T}_k=\frac{1}{(\mathrm{IS}_k+\epsilon)^q},\qquad
\chi^{\mathrm T}_k=\frac{\gamma^{\mathrm T}_k}{\sum_{l=i-1}^{i+1}\gamma^{\mathrm T}_l},$$
and cell $i$ is troubled iff its own $\chi^{\mathrm T}_i<C_T$, with
$\epsilon=10^{-3}$, $q=6$, $C_T=10^{-4}$ for every case, without tuning.
In two dimensions the one-dimensional test is applied in $x$ and $y$ and
a cell flagged in either direction is troubled (§5.1). The idea comes from
Fu's TENO discontinuity indicator for hybrid finite differences, which
needs four candidate stencils and six points; the novelty is the compact
three-cell form. Huang et al. (2025, §3.1, §4.1, Eqs. 11–14) reuse it with
the same parameters in their TENO-THINC limiter, applied to each
characteristic variable, and in two dimensions limit a cell troubled
along $x$ only along $x$.

Reported behaviour, all on inviscid Euler problems:

- on smooth one- and two-dimensional advection the indicator never fires,
  so the limited and unlimited schemes give identical third-order errors
  (Huang & Fu 2024, §6.1, Tables 1, 3; Huang et al. 2025, §5.1, Tables 1, 3),
  whereas the TVB indicator "may activate limiters" at smooth extrema and
  is therefore used to force limiting in the accuracy test (Huang & Fu
  2024, §6.1.1);
- KXRCF misses the under-resolved high-wavenumber part of the Shu–Osher
  problem ($x\approx5.6$ to 7.2), which the TENO indicator flags, and
  marks more than 50% of the cells of the two-dimensional Riemann problem
  (configuration 3), while the TENO indicator places troubled cells "much
  more precisely" with "less noise" on the shock tubes and the double Mach
  reflection (Huang & Fu 2024, §6.2–6.6, Figs. 4–15; visual evidence only);
- in the double Mach reflection at $1200\times300$ the indicator flags 34681
  cells, 9.63% of the domain, of which the boundary-variation selector of
  the TENO-THINC limiter sends 6476 (1.8% of the domain) to the jump
  reconstruction (Huang et al. 2025, §5.5, Fig. 6).

## Indicators built from TENO stencil flags (finite differences)

**Eight-point TENO-S indicator.** [Liang & Fu (2024)](/sources/liang-2024.md),
§3.1, Eqs. (31)–(34), cover the points $x_{i-3},\dots,x_{i+4}$ with six
**equal-sized** three-point stencils, compute their Jiang–Shu indicators
(the three not used by TENO given in Eq. 31), and set
$\gamma^{\mathrm T}_k=1/(\mathrm{IS}_k+\epsilon)^6$, $k=0,\dots,5$, with
$\epsilon=10^{-4}$ in one dimension and $10^{-2}$ in several (it also acts as
a cut-off of the smoothness measurement). A cell is smooth if
$\chi^{\mathrm T}_k>C_{T2}$ for every $k$, with the built-in $C_{T2}=10^{-6}$,
troubled otherwise; it is evaluated on conserved variables in physical
space (density and total energy in one dimension, density only in
several), dimension by dimension. Smooth cells take a non-dissipative
skew-symmetric flux, troubled ones an eight-point TENO flux (see
[WENO](/methods/weno-scheme.md) and
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
Equal stencils keep the indicator cheap, and the authors state that it
separates smooth from non-smooth scales "in the wavenumber space", hence
"more universal for general conservation laws" than physical-variable
sensors such as the Ducros sensor (§3.1). In the double Mach reflection
more than 90% of the cells use the skew-symmetric flux (§4.6, no count
printed).

**Discontinuity-strength measure.** Liang & Fu (2024, §3.3.2,
Eqs. 47–49) and [Li & Fu (2024)](/sources/li-2024-c.md), §3.2.1,
Eqs. (44)–(47), grade rather than flag: a first-order measure $m\in[0,1]$
built from neighbouring undivided differences (after Ren et al.) is near 1
at a discontinuity and near 0 for high-wavenumber fluctuations, and maps
the TENO cut-off between about $10^{-7}$ (Liang & Fu; $10^{-5}$ for Li &
Fu) and $10^{-10}$; formulas on [WENO](/methods/weno-scheme.md).

**Pattern of TENO flags.** [Takagi et al. (2022)](/sources/takagi-2022.md),
§3.1–3.2, Eqs. (19)–(20), read the 0/1 flags that fifth-order TENO already
computes for its two biased stencils, classify each cell by which of them
is non-smooth, and declare a discontinuity in cell $i$ when a cell on its
left has a non-smooth right stencil, a cell on its right a non-smooth left
stencil (within three cells), and cell $i$ itself neither; the pattern
comes from TENO's flags on a one-cell step (Table 1). It adds no parameter
to TENO and sends the flagged cells to a THINC jump reconstruction; under-
resolved smooth fluctuations, which also turn flags off, do not show the
pattern and stay with TENO. Li & Fu (2024, §3.2.3, Eqs. 59–61) reuse the
same pattern for five- to seven-point adaptive TENO in compressible
multiphase flow.

## Filtering the field before sensing

[Gao et al. (2022)](/sources/gao-2022.md), §3.2, a FLEXI implicit LES of
an oblique shock reflecting on a Mach 2 turbulent boundary layer, report
the failure of both families in that configuration:

- the Jameson indicator evaluated on the instantaneous pressure marks large
  parts of the under-resolved turbulent boundary layer as troubled (Fig. 2),
  so it "cannot be used" for this interaction unmodified;
- the Ducros indicator, because dilatation and vorticity have similar
  magnitudes in the interaction region, either detects almost no shock
  inside the boundary layer (large threshold) or marks too many cells
  (small threshold); most authors, they state, take the large threshold
  and refine the mesh (§1, §3.2, citing Fang et al., Jammalamadaka et al.;
  stated, not run).

Their remedy is to evaluate a jump-detecting indicator on a **filtered**
field from which the turbulent structures are removed while shock jumps
remain. They reject temporal filters (no real-time update; a moving
average made sharp shocks and stability hard to reconcile) and use the
Jameson indicator on the **spanwise-averaged pressure**, the mean over all
spanwise nodes, which confines the subcells to the shocks, including
inside the boundary layer, with "a negligible number" of finite-volume
subcells near the interaction (Fig. 7 against Fig. 2). The global average
needs a quasi-two-dimensional configuration (oblique reflections,
compression ramps); an element-local spanwise average serves some
three-dimensional cases; complex geometries are left open. The authors
state that the filtering applies to any jump-detecting indicator, e.g.
Persson's, and that its parallel cost fits within the 15–20% overhead of
the hybrid scheme (§3.2, §5.3.1). The resulting interaction is on
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

## Qualifications

- **What separates a shock from turbulence.** Carlsson et al. (2023) state
  that the product $\Psi_i\Phi_i$ separates shocks from compressible
  turbulence and support it with channel and base-flow runs in which the
  dissipation coefficient and face extrapolation also change (see the LD2
  page); Gao et al. (2022) state that Ducros-type sensors fail for shocks
  that penetrate a turbulent boundary layer, citing others, and test the
  Jameson indicator alone; Liang & Fu (2024) call their indicator more
  universal than the Ducros sensor without running the Ducros sensor.
  The claims concern different flows (shocks inside or outside the
  boundary layer) and none of the three compares the sensors on one case,
  so no contradiction is recorded.
- **"Parameter-free" indicators.** Huang & Fu (2024) and Huang et al.
  (2025) use one parameter set ($\epsilon=10^{-3}$, $q=6$, $C_T=10^{-4}$)
  for eight and nine Euler tests on uniform grids at $N=2$; the limiters
  they drive keep their own cut-offs and constants. Liang & Fu (2024)
  print "no case-by-case tuning" (abstract) while using
  $\epsilon=10^{-4}$ in one dimension and $10^{-2}$ in several, different
  indicator variables in one and several dimensions, and a Roe instead of
  a Rusanov splitting "to obtain a stable result" in the blast-wave case
  (§4.4). Takagi et al. (2022) call their pattern indicator parameter-free;
  it inherits TENO's $C_T$, whose value changes their blast-wave
  convergence (§4.5, Fig. 9). No source tests these indicators on a
  turbulent flow with shocks.
- **Two printed forms of the TENO indicator.** Huang & Fu (2024, Eq. 32)
  integrate each neighbour polynomial over its own cell $I_k$; Huang et al.
  (2025, Eq. 11), restating the same indicator, integrate all three over
  the target cell $I_i$. For a neighbour quadratic the first-derivative
  term differs in general between the two (the second-derivative term,
  a constant integrand, does not) *(compiler check, not in the sources)*.
- **Printed form in EDGE.** Ahn et al. (2023, Eq. 6) print the pressure
  ratio of the second-difference coefficient as
  $|\sum_kp_k-p_0|/(\sum_kp_k+p_0)$ and write the vortical factor with the
  subscript $j$ and the dilatation of node 0. For more than one neighbour
  the printed ratio is not the normalized sum of differences
  $|\sum_k(p_k-p_0)|/\sum_k(p_k+p_0)$ of the JST sensor above
  *(compiler check, not in the sources)*.
- The Jameson threshold of Gao et al. (2022) is not printed, nor is
  Fernandez et al.'s sensor formula in Klose et al. (2025).

# Citations

- [Gao et al. (2022)](/sources/gao-2022.md) — §1; §3.2, Eqs. (12)–(17), Figs. 2, 5–7 (Jameson and Ducros indicators in DGSEM, signed variants, filtered-field indicator); §5.3.1 (cost of the filtering).
- [Liang & Fu (2024)](/sources/liang-2024.md) — §3.1, Eqs. (31)–(34), Fig. 2 (eight-point indicator); §3.2, Eq. (35); §3.3.2, Eqs. (47)–(49) (discontinuity strength); §4.4, §4.6.
- [Huang & Fu (2024)](/sources/huang-2024.md) — §1; §4.1–4.3, Eqs. (27)–(35) (TVB, KXRCF, TENO indicator); §5.1; §6.1–6.6, Tables 1–4, Figs. 4–15.
- [Huang et al. (2025)](/sources/huang-2025.md) — §3.1, §3.3, §4.1, Eqs. (11)–(14) (TENO indicator restated, characteristic and directional use); §5.1, Tables 1, 3; §5.5, Fig. 6 (troubled-cell and BVD fractions).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §3.1–3.2, Eqs. (19)–(20), Table 1 (TENO-flag pattern indicator); §4.5, Fig. 9.
- [Li & Fu (2024)](/sources/li-2024-c.md) — §3.2.1, Eqs. (44)–(47) (discontinuity strength $m$); §3.2.3, Eqs. (59)–(61) (pattern indicator for TENOA).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2.2.3, Eqs. (12)–(15) (Jameson sensor, Ducros factor, product).
- [Dang et al. (2022)](/sources/dang-2022.md) — §2.2.3, Eqs. (41)–(43) (modified Jameson sensor, thresholds).
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §III, Eqs. (1)–(6) (Ducros-weighted Jameson dissipation in EDGE).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2 (Ducros-switched WENO in STREAmS).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.a, b, f, h (Persson–Peraire with Ducros weighting, Ducros homotopy, pressure modal-decay indicator).
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §4.1.1, Fig. 1 (Ducros sensor activated by oscillations).
- [Krais et al. (2021)](/sources/krais-2021.md) — §4.3 (indicators, hysteresis); §7.2 (JST-type indicator).
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2 (dilatation–vorticity sensor of Fernandez et al.).
- [Wang (2024)](/sources/wang-2024-b.md) — arXiv v2: §2.3, Eq. (19), Table 2 (Persson–Peraire indicator and thresholds).
- [Schotte et al. (2026)](/sources/schotte-2026.md) — §2.2 (Persson–Peraire sensor with Glaubitz calibration).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.4, Eq. (19) (density-gradient sensor).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §6.2–6.3, Eqs. (127)–(128) (density-gradient sensors).
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §3.1 (element-resolution indicator for HWENO limiting of $k$).
- [Xu et al. (2026)](/sources/xu-2026.md) — arXiv 2508.21599v1: §3, Eq. (18) (pressure-ratio sensor).
