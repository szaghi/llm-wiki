---
type: Method
title: "Flux reconstruction"
description: "Flux reconstruction (FR/CPR) builds a degree-N discontinuous flux polynomial per element and corrects it with interface corrections fed by a Riemann solver; with suitable correction functions it recovers nodal DG. This page covers its formulation, its use as implicit LES, explicit SGS models and filter width on it, and its stabilization."
status: established
aliases: [FR, flux reconstruction method, correction procedure via reconstruction, CPR, FR/CPR, lifting collocation penalty, Huynh flux reconstruction]
tags: [flux-reconstruction, dg, implicit-les, numerical-dissipation, les, wmles]
timestamp: 2026-10-26T11:38:00Z
---

# Flux reconstruction

**Flux reconstruction (FR)**, in the form of Huynh, and its variant the
**correction procedure via reconstruction (CPR)** solve the differential
(strong) form of a conservation law
$\partial_tU+\nabla\cdot(F^c(U)-F^v(U,\nabla U))=0$ with a nodal polynomial
of degree $N$ in each element. The flux evaluated at the solution points
gives a *discontinuous* flux polynomial, which a *correction* term makes
continuous in its normal component at the element faces: the correction is
the jump between a common interface flux $f^*$ (from an approximate Riemann
solver) and the discontinuous flux, spread into the element by correction
functions. The choice of correction functions fixes the scheme, and one
choice recovers the nodal [discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
method, which [Dzanic et al. (2022)](/sources/dzanic-2022.md), §2.2, describe
as FR being "a generalization of the nodal discontinuous Galerkin method".
In the turbulence sources FR runs as [implicit LES](/definitions/implicit-les.md)
or under-resolved DNS ([Dzanic et al. 2022](/sources/dzanic-2022.md);
[Wang 2024](/sources/wang-2024-b.md)), with explicit subgrid models in
[wall-modelled LES](/methods/wall-modelled-les.md)
([Duan & Wang 2024](/sources/duan-2024.md)), and with
[PANS](/methods/partially-averaged-navier-stokes.md) as the hybrid closure
(Dzanic et al. 2022).

Page-local symbols: $\boldsymbol g_{f,k}$ the correction function of flux
point $k$ on face $f$; $N_{sp}$ the number of solution points of an element;
$\ell_i$ the nodal Lagrange basis; $c_{q,f,l}$ the CPR lifting coefficients
(the source's $\alpha_{q,f,l}$, renamed because $\alpha$ is the DG/FV blending
factor of the registry); $V_e$ the element volume.

## Formulation

**FR form** (Dzanic et al. 2022, §2.2, Eqs. 18–22; Wang 2024, §2.2,
Eqs. 9–15). In each element, mapped to a reference element, the solution is
$U\approx\sum_{i=1}^{N_{sp}}U_i\,\ell_i(\boldsymbol\xi)$ with
$\ell_i(\boldsymbol\xi_j)=\delta_{ij}$. The flux splits as
$$F=F^D+F^C,\qquad F^D=\sum_{i=1}^{N_{sp}}F(U_i)\,\ell_i(\boldsymbol\xi),\qquad
F^C(\boldsymbol\xi)=\sum_{f}\sum_{k}\Big[(f^*\cdot\boldsymbol n)_{f,k}-(F^D\cdot\boldsymbol n)_{f,k}\Big]\boldsymbol g_{f,k}(\boldsymbol\xi),$$
with the correction functions normalized at the flux points,
$\boldsymbol g_{f,k}\cdot\boldsymbol n_{f_2,k_2}=1$ if $(f,k)=(f_2,k_2)$ and
$0$ otherwise (Wang 2024, Eq. 15). Dzanic et al. (2022, §2.2) add that the
sum of the correction functions lies in the Raviart–Thomas space of order
$N$. The divergence of $F^D$ needs only the derivatives of the Lagrange basis;
that of $F^C$ the divergence of $\boldsymbol g_{f,k}$; FR "solves the
differential form" of the equations (Wang 2024, §2.2).

**CPR form** (Duan & Wang 2024, §3, Eqs. 16–25). The same scheme written at
solution point $q$ of element $k$ as
$$\frac{\partial U_{k,q}}{\partial t}+\Big[\nabla\cdot\hat F^c(U_k)\Big]_q-\Big[\nabla\cdot\hat F^v(U_k,\nabla U_k)\Big]_q+\frac{1}{\mathcal J_{k,q}}\sum_f\sum_l c_{q,f,l}\Big([F^n]_{f,l}-[F^n_v]_{f,l}\Big)A_{f,l}=0,$$
where $\hat F$ are the flux polynomials interpolated from the solution
points, $[F^n]_{f,l}$ and $[F^n_v]_{f,l}$ the jumps between the common and the
interpolated normal fluxes at flux point $l$ of face $f$, $A_{f,l}$ the local
face area, $\mathcal J$ the mapping Jacobian, and the lifting coefficients
$c_{q,f,l}$ depend only on the element shape. Duan & Wang state that the
normal fluxes "must be continuous across element interfaces at the flux
points to ensure conservation".

**Node sets.** The sources place the solution points differently: Gauss
points ("usually", Duan & Wang 2024, §3), Legendre–Gauss–Lobatto points for
both solution and flux points so that nodal DG is recovered (Wang 2024, §2.2,
§3, Fig. 1), Williams–Shunn points on triangles with Gauss–Legendre flux
points (Dzanic et al. 2022, Fig. 1). These are choices within the family,
not disagreements.

**Interface fluxes and time stepping in the sources.**

| Source | code | inviscid flux | viscous flux | time stepping | degrees used |
|---|---|---|---|---|---|
| Dzanic et al. (2022), §2.3 | PyFR | Rusanov-type | BR2 | explicit fourth-order Runge–Kutta | $N=1$, $3$ |
| Duan & Wang (2024), §3 | hpMusic | Roe | common solution and gradients, face gradients by BR2 | explicit SSP-RK3, or optimized BDF2 with (block) LU-SGS | $N=2$–$5$ |
| Wang (2024), §2.2, §3 | ATHOS | Rusanov at no-slip walls, Roe or HLLC inside | LDG, penalty $0$, directional parameter $\pm0.5$ | explicit low-storage five-stage fourth-order Runge–Kutta, CFL $0.85/(2N+1)$ | up to $N=3$ |

Wang (2024, §2.2) reads the Rusanov flux as a central flux with scalar
dissipation (the largest local wave speed) and the Roe flux as a central flux
with matrix dissipation, so that "the choice of Riemann solver can have an
impact on the accuracy and robustness of implicit LES". The LDG penalty on
the solution jump is set to zero, "the minimum dissipation version of LDG"
(§2.2, Eq. 16; see [jump-penalty stabilization](/methods/jump-penalty-stabilization.md)).
Wang's ATHOS is a new in-house C++ FR solver on linear quadrilaterals and
hexahedra, which raises the order by restarts $N=0\to1\to2\to3$ (§3, §4.2).

## FR as implicit LES

Duan & Wang (2024, §3) state that projecting a solution onto the
piecewise-polynomial space "can be considered a space-filtering operation",
so FR/CPR without a subgrid model "becomes ILES", and an explicit model
amounts to extra dissipative flux terms. Evidence in the sources:

- **Well-resolved flows favour no model.** On the viscous
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$
  ($64^3$ elements, $N=4$) the no-model enstrophy lies "almost on top of"
  the DNS, and in a wall-resolved [channel](/benchmarks/turbulent-channel-flow.md)
  at $Re_\tau=180$ ($N=3$, per-degree-of-freedom spacing
  $\Delta x^+=5.7$, $\Delta y^+=0.68$, $\Delta z^+=5.7$) the no-model LES
  agrees very well with DNS (Duan & Wang 2024, §5.2–5.3, Figs. 7, 9–10). Wang
  (2024, §4.1, Figs. 2–3) reproduces the DNS dissipation rate and spectra of
  the Taylor–Green vortex at $Re=1600$ and $5000$ on $64^3$ elements at $N=3$.
- **Under-resolution breaks it.** In a wall-modelled channel at
  $Re_\tau=5200$ on $60\times16\times40$ elements the no-model run was not
  stable (Duan & Wang 2024, §5.4); in decaying isotropic turbulence on
  $32^3$ cells, $N=2$ and $3$ pile up energy at high wavenumbers, which the
  authors attribute to aliasing (§5.2, "we believe"). Dzanic et al. (2022,
  §3.1, Fig. 5) see large oscillations of the wall-normal variance in $N=3$
  under-resolved DNS of the [periodic hill](/benchmarks/periodic-hill.md),
  attributed to aliasing-driven instability and absent with PANS.
- **Order at fixed degrees of freedom.** Dzanic et al. (2022, §2.3, §3)
  compare $N=1$ ("comparable to a finite volume formulation") with $N=3$ at
  equal degrees of freedom, the $N=1$ meshes carrying "approximately 6-8
  times as many elements": fourth order improves first-order statistics of under-resolved
  DNS and PANS about equally, but second-order statistics and the cylinder's
  spectral peaks much more for PANS, which the authors attribute to the
  lower [numerical dissipation](/properties/numerical-dissipation.md) of the
  high-order scheme (details on the [PANS](/methods/partially-averaged-navier-stokes.md)
  page). Their new $N=3$ DNS of the cylinder at $Re_D=3900$ uses about
  55.6 million degrees of freedom (§3.2; see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md)).
- **Cost against finite volumes**, as relayed by
  [Saini et al. (2023)](/sources/saini-2023.md), §1, from earlier studies:
  fifth-order PyFR was more accurate than a commercial finite-volume code but
  about 2 and 6 times more expensive on two cases, and third-order FR was more
  accurate at one third of the cost of a second-order run on a 64 times larger
  mesh.

## Explicit subgrid models on FR: element averaging and filter width

Duan & Wang (2024) calibrate the [Smagorinsky](/methods/smagorinsky-model.md),
[WALE](/methods/wale-model.md) and [Vreman](/methods/vreman-model.md) models in
hpMusic for high-order WMLES, where they argue ILES "often runs into
robustness and accuracy issues due to the low dissipation embedded in these
methods" (Abstract, §1). Their implementation choices (§3):

- **Element-averaged eddy viscosity**, to make the model "less oscillatory":
  $$\nu_t=\frac{1}{V_e}\sum_q w_q\,\nu_{t,q},$$
  with $\nu_{t,q}$ the pointwise value at solution point $q$ (Eq. 26).
- **No interface subgrid flux**: the common flux of the subgrid stress is set
  to zero on every face, "to guarantee the conservation and minimize data
  communication", on the ground that model stresses are poorly correlated
  with the physical ones and serve only to drain energy (Eq. 27).
- **Model stress** added to the viscous stress with the viscous sign, built
  on the full strain rate, $\tau_{ij}=-2\nu_t\bar S_{ij}$ (no deviatoric
  projection printed), with the subgrid heat flux, pressure work and
  turbulent diffusion dropped "for the low Mach number flows considered"
  (§2.1–2.2).

**Filter width.** The model coefficients are kept and the length scale is
recalibrated, with three choices (Eqs. 28–30):
$$\text{d1: }\Delta=V_e^{1/3},\qquad \text{d2: }\Delta=\frac{V_e^{1/3}}{\sqrt{N+1}},\qquad \text{d3: }\Delta=\frac{V_e^{1/3}}{N+1}.$$
d1 is the finite-volume convention (one degree of freedom per element), d3
the "natural" choice with $N+1$ degrees of freedom per direction, and d2 is
introduced because the models "have been mostly calibrated and used for
2nd-order methods" and high-order methods have much less numerical
dissipation, so d3 is expected to under-dissipate (§3). Findings (§5–6):

- dissipation ranks WALE < Vreman < Smagorinsky; on the inviscid
  Taylor–Green vortex ($16^3$ elements, $N=4$) every model and length scale
  dissipates far more than the Riemann-solver dissipation of the scheme, and
  d2, d3 much less than d1 (Figs. 5–6);
- in isotropic turbulence d1 shrinks the resolved wavenumber range, d3 is
  close to no model, d2 is a "good balance" (Fig. 8);
- in the wall-resolved channel Smagorinsky fails at every length scale,
  WALE and Vreman match DNS with d2 and d3 (Figs. 9–10);
- in the wall-modelled channel at $Re_\tau=5200$ ($N=2$–$5$, element sizes
  $\Delta x^+=1088$, $\Delta y^+=650$, $\Delta z^+=544$) and at
  $Re_\tau=544$ ($N=3$), Vreman gives the same ranking at every degree, d1
  too dissipative, d3 too little, d2 best; WALE is best with d1 for $N=2$–$4$
  and with d2 at $N=5$, where the trend with length scale reverses
  (Figs. 11–15).

The recommendation is Vreman with d2 for high-order WMLES (§6). The DG
sources of this bundle use d3 as the DG filter width (see
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md), "Filter
width"); Duan & Wang's d2 is calibrated with their element-averaged eddy
viscosity and zero interface subgrid flux, in wall-modelled channels and
the other cases of §5.

**Wall model on FR.** Duan & Wang (2024, §4, Fig. 4) impose the
[equilibrium wall model](/methods/equilibrium-wall-model.md) weakly at the
wall flux points and take its input at the interface between the first and
second element off the wall, from the second element, because "the
turbulent eddies at the first element are always under-resolved", so the
matching height equals the first element height; they call a near-wall
aspect ratio of one desirable.

## Stabilization of FR implicit LES

Under-resolved FR needs an added dissipation mechanism. Duan & Wang (2024,
§1, Fig. 2) show, for a fourth-order discontinuous method in a channel at
$Re_\tau=5200$, that the outcome of solution limiting depends on its amount:
too little damping over-predicts the wall friction and under-predicts the
velocity, too much does the reverse, which they call "very ad hoc" (§5.4)
and replace by explicit models.

Wang (2024) keeps implicit LES and stabilizes it by **solution filtering**:
a local modal filter switched on in elements whose Persson–Peraire
smoothness indicator exceeds a threshold, or the positivity-preserving
entropy filter of Dzanic and Witherden; both are described, with their
thresholds, costs and turbine results, on
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
("Indicator-switched modal and entropy filters"). The author states that
filtering adds local dissipation to the total numerical dissipation that
ILES relies on, and that solution filtering may cause time inconsistency
(§2.3, §5). Further findings on the interface flux (§2.4.2, §4.3.2, Tables
7–8):

- at no-slip walls the convective flux is computed from ghost states with a
  Riemann solver; of Rusanov, Roe and HLLC the most dissipative, Rusanov,
  is the most robust there, consistent with Mengaldo et al. as cited;
- inside the domain HLLC is more robust than Roe (stable with less
  filtering) on the VKI LS89 vane, which the author explains by Roe's known
  failure near vacuum states, citing Toro; when both are stable, mean-flow
  results are nearly identical, and the predicted heat-transfer coefficient
  depends more on the filter threshold than on the Riemann solver.

**Wall units on high-order grids.** Wang (2024, §4.2, Eq. 26, after Jia et
al.) divides the first-cell $y^+$ computed from the cell height by $N+1$;
the [PANS](/methods/partially-averaged-navier-stokes.md) wall value of
Dzanic et al. (2022, Eq. 26) likewise uses the element height over $N+1$ as
first-point distance.

## Applications in the sources

- **Turbomachinery** (Wang 2024, §4.2–4.4): the T106C low-pressure-turbine
  cascade at exit $Re=80{,}000$ ($N=3$, 7.87 million degrees of freedom per
  equation) and the VKI LS89 high-pressure-turbine vane at
  $Re=1.13\times10^6$ with heat transfer (6.6 to 31.3 million degrees of
  freedom), see [turbine cascades](/benchmarks/turbine-cascade.md). Raising
  $N$ from 2 to 3, then refining the span, moves the heat-transfer
  coefficient towards experiment, and a spanwise spacing
  $\Delta z^+\approx45$–$60$ suffices for the mean heat transfer (§4.3.1).
- **Hybrid RANS/LES**: PANS with the [$k$-$\omega$ SST](/methods/k-omega-sst-model.md)
  closure on the periodic hill and the circular cylinder (Dzanic et al.
  2022; see [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).
- **Canonical LES**: Taylor–Green vortex, Comte-Bellot–Corrsin decaying
  [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
  wall-resolved and wall-modelled channels (Duan & Wang 2024, §5).

## Low-order FR and the spectral-difference relative in a shock–turbulence comparison

In the multi-code comparison of [Chapelier et al. (2024)](/sources/chapelier-2024.md)
on the supersonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
($Re=1600$, $M_0=1.25$), the FR code H3AMR (HySonic Technology) runs on
unstructured meshes in a block-spectral form with $N+1$ Gauss–Legendre
points per direction and element, correction functions averaged over Radau
polynomials of different orders, a Rusanov interface flux and third-order
Runge–Kutta (§III.B.g). Its shock capturing is the "Block Spectral
Stresses" model, which computes sub-filter stresses, heat flux and pressure
work from the spectra of the velocity gradient, is activated by the energy
of the highest polynomial mode of momentum, and is meant to capture shocks
and model turbulence at once (see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).
Run at second order ($N=1$, $32^3$ to $256^3$ elements, Table II), it
under-estimates the kinetic energy at $64^3$ degrees of freedom and gives
the lowest solenoidal dissipation of all solvers on every grid, the excess
numerical dissipation "typical of second-order upwind schemes" (§IV.A,
Figs. 5, 7); in the subsonic verification case it runs at fourth order and
agrees with the other codes (App. A). The comparison also includes
SD3DvisP, a fourth-order spectral-difference code on unstructured hexahedra
(Roe flux with entropy fix, centred viscous flux, subcell artificial
viscosity), which captures small scales well on coarse grids but whose
strong shock capturing "probably" hinders them on the finer ones (§III.B.e,
§IV.A, §V). High-order element methods resolve both large and small scales
better than second order in this compressible setting (§V). The PyFR
compressible FR code is named by [Kurz et al. (2025)](/sources/kurz-2025.md),
§1, among the GPU high-order solvers.

## Qualifications

- Chapelier et al. (2024) print H3AMR's order as the number of points per
  direction ("$N$ = spatial order of accuracy", §III.B.g), here translated
  to the registry's degree $N$ (order $N+1$).
- Duan & Wang (2024) do not print the coefficient values used in the runs;
  only the "often estimated" $C_s=0.16$, WALE constant $0.325$ and the
  relation $c_v\approx\sqrt{2.5}\,C_s$ for the Vreman constant (§2.2–2.4).
  Their evidence is comparison of profiles and spectra; no error norms are
  tabulated.
- Duan & Wang (2024, §5.3) print $Re_\tau=u_\tau L/\nu$ for a channel they
  describe as based on $\delta$, with no $L$ defined.
- Wang (2024) is the arXiv v2 preprint of the Computers & Fluids paper; the
  robustness ranking of Riemann solvers is shown for this FR solver and
  filter only. The author's statement that the entropy filter needs no
  tuning (§4.3.2, §5) is qualified in §4.4.3, where the entropy tolerance is
  called a parameter.
- Dzanic et al. (2022) is the arXiv v1 preprint; it reports no
  de-aliasing test for its attribution of the $N=3$ oscillations to
  aliasing, and prints no timings for its statement that the high order
  comes "without a significant increase in computational effort" (§4).

# Citations

- [Duan & Wang (2024)](/sources/duan-2024.md) — Abstract; §1, Fig. 2 (limiting amount); §2.1–2.4 (governing equations, SGS models); §3, Eqs. (16)–(30) (FR/CPR, element-averaged eddy viscosity, zero interface SGS flux, filter widths d1–d3); §4, Fig. 4 (wall model on FR); §5.1–5.4, Figs. 5–15; §6.
- [Wang (2024)](/sources/wang-2024-b.md) — arXiv v2: §2.2, Eqs. (9)–(16) (FR with DG-recovering correction, Riemann solvers, LDG); §2.3 (solution filtering); §2.4.2 (wall flux); §3 (ATHOS); §4.1, Figs. 2–3; §4.2, Eq. (26); §4.3, Tables 5–8; §4.4.3; §5.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — arXiv v1: §2.2, Eqs. (18)–(22) (Huynh FR, correction functions, generalization of nodal DG); §2.3 (PyFR, Rusanov, BR2, RK4, equal degrees of freedom); Eq. (26); §3.1–3.2, Figs. 3–5, 11–13; §4.
- [Saini et al. (2023)](/sources/saini-2023.md) — §1 (relayed cost and accuracy comparisons of FR against finite volumes).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.e, g, Tables I–II (H3AMR flux reconstruction, Block Spectral Stresses, SD3DvisP spectral difference); §IV.A, Figs. 5, 7; §V; App. A.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv 2404.12703v2: §1 (PyFR among GPU high-order codes).
