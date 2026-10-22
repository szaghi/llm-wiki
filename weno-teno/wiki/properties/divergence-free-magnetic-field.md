---
type: Property
title: "Divergence-free magnetic field"
description: "The magnetic field of MHD obeys div B = 0; discretizations enforce it exactly, locally, through divergence cleaning or not at all, and Wu and Shu show that bound preservation of high-order MHD schemes requires a discrete divergence-free condition, recovered by a Godunov-symmetrization source term."
status: established
aliases: [div B = 0, solenoidal constraint, discrete divergence-free condition, DDF, divergence cleaning, GLM-MHD, constrained transport, locally divergence-free DG]
tags: [mhd, bound-preserving, positivity, dg]
timestamp: 2026-10-21T12:00:00Z
---

# Divergence-free magnetic field

The ideal MHD equations carry the involution $\nabla\cdot B=0$: it holds for
all time if it holds initially, but the conservative flux form does not
enforce it, and discretizations generally do not preserve any discrete
version of it. The sources of this bundle meet the constraint in three ways:
as a hypothesis that [bound preservation](/properties/bound-preservation.md)
needs ([Wu & Shu (2023)](/sources/wu-2023-b.md)), as a quantity controlled by
generalized-Lagrange-multiplier (GLM) divergence cleaning
([Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)),
and through constrained transport in finite-difference TENO codes
([Fu (2023)](/sources/fu-2023.md)).

## Divergence and bound preservation

[Wu & Shu (2023)](/sources/wu-2023-b.md) (§6) study multicomponent ideal MHD,
whose admissible set requires $0\le Y_k\le1$, $\rho>0$ and $p>0$ (Eq. (6.4)).
Its [geometric quasilinearization](/methods/geometric-quasilinearization.md)
writes the pressure constraint as
$\varphi(u;v_*,B_*)=u\cdot n_*+\tfrac12\lvert B_*\rvert^2>0$ for all auxiliary
velocities $v_*$ and fields $B_*$ (Eq. (6.5); page-local $\varphi$). With it:

- **First order** (Thm 6.1). Under
  $\Delta t\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)\le1$, the 2D
  Lax–Friedrichs update keeps the species and density constraints and
  satisfies
  $$\varphi(\bar u^{n+1}_{ij};v_*,B_*)>-\Delta t\,(v_*\cdot B_*)\,\mathrm{div}_{ij}\bar B,\qquad
  \mathrm{div}_{ij}\bar B=\frac{\bar B_{1,i+1,j}-\bar B_{1,i-1,j}}{2\Delta x}+\frac{\bar B_{2,i,j+1}-\bar B_{2,i,j-1}}{2\Delta y}.$$
  The update is therefore bound-preserving if the discrete divergence
  vanishes, the **discrete divergence-free (DDF) condition**; since
  $v_*\cdot B_*$ takes either sign, a nonzero divergence leaves the
  right-hand side negative for some auxiliary states.
- **High order** (Thm 6.2, proof omitted by analogy with Wu's 2018
  analysis). For finite-volume or DG cell-average schemes of degree $N\ge1$
  with Gauss-quadrature Lax–Friedrichs fluxes, if the point values at the
  mixed Gauss / Gauss–Lobatto points lie in $G$, then under the CFL bound
  with the first Gauss–Lobatto weight the same estimate holds with
  $\mathrm{div}_{ij}B=\tfrac12\big(\mathrm{div}^-_{ij}B+\mathrm{div}^+_{ij}B\big)$,
  built from the interior ($-$) and exterior ($+$) interface traces.
- **Standard schemes do not preserve the DDF condition** (Rem. 6.3).
  Globally divergence-free DG techniques are incompatible with the local
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md), and a locally
  divergence-free DG basis gives only $\mathrm{div}^-_{ij}B=0$. The
  convex-decomposition analyses of the classical Zhang–Shu framework are
  therefore "inapplicable" to multidimensional MHD.

**The remedy: a discretized Godunov-symmetrization source** (§6.2). The
symmetrizable form $\partial_tu+\nabla\cdot f(u)+(\nabla\cdot B)\,S_B(u)=0$,
$S_B=(0,B,v,v\cdot B)^\top$ (Godunov 1972, as recalled; page-local $S_B$),
is discretized by a source built only from the jumps of the normal magnetic
field at the interface Gauss points (Eq. (6.22)). With a locally
divergence-free DG basis, $\mathrm{div}_{ij}B$ reduces to those jumps
(Eq. (6.19)), the source cancels the offending term, and the scheme is
provably bound-preserving under $(1+\varepsilon_B)\nu\le\varpi$
(Thm 6.4), where $\nu=\Delta t(a^{(1)}/\Delta x+a^{(2)}/\Delta y)$ is the 2D
CFL number of this page, $\varpi=\mathsf w^{\mathrm{GL}}_0$ the first
Gauss–Lobatto weight (the source writes $\lambda$ and $\widehat\omega_1$) and $\varepsilon_B$ a
correction proportional to the normal-field jumps divided by the wave speeds
(page-local; the source's $\varepsilon$). The CFL penalty vanishes when the
normal field is continuous.

**Evidence** (§7). A third-order locally divergence-free DG method with the
source term, a locally divergence-free WENO limiter in KXRCF-flagged cells,
the scaling limiter and SSP-RK3 at CFL 0.15 keeps the admissible set
throughout a two-species MHD blast ($400^2$ cells, $t=0.01$, Fig. 5), and
computes a two-species MHD jet with inflow speed 800 and
$B=(0,\sqrt{4000},0)$ (Fig. 6). On the jet the run "fails quickly" without
any one of the three ingredients — scaling limiter, locally divergence-free
basis, source term — even with the WENO limiter; this is stated, no failure
figure is shown.

## Divergence cleaning (GLM-MHD)

[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§5.3, Eqs.
(51)–(52)) solve GLM-MHD in conservative form: an extra field
$\psi_{\mathrm{GLM}}$ transports divergence errors away at a cleaning speed
$c_h$, recomputed every step as the largest value compatible with CFL
stability; $\nabla\cdot B=0$ is not enforced exactly. They use the conservative
form although the non-conservative form is needed to prove entropy stability,
because the conservative form fits their subcell-limiting framework (§5.3).
On the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
($N=3$, $256^2$ elements, $t=1$) subcell-wise density limiting with
second-order subcell finite volumes limits less and develops more turbulent
structure than with first-order ones (§5.3.1;
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).

## Constrained transport with TENO

[Fu (2023)](/sources/fu-2023.md) reviews TENO-A for MHD with unstaggered
constrained transport (§5.3, recalled from earlier work): in 1D the cost of
TENO5-A is similar to WENO5-JS and WENO5-Z, and even the eight-point TENO8-A
adds a "negligible" cost; Orszag–Tang results at $200^2$ are compared with a
WENO5-JS reference at $512^2$ (Fig. 19). The review gives no formulas for
the transport step.

## Qualifications

- The Godunov-symmetrization source is non-conservative; Wu & Shu do not
  discuss the resulting conservation error. The source vanishes only where
  the normal field is continuous.
- The extension of Thm 6.4 to SSP time stepping requires the point-value
  hypothesis and the locally divergence-free property at every stage; it is
  stated without a stage-wise argument (§6.2).
- arXiv v1 of Wu & Shu prints the jump coefficient of $\varepsilon_B$ with
  $(\rho^\pm)^{1/2}$ where a Cauchy–Schwarz and AM–GM bound of Eq. (6.21)
  gives $(\rho^\pm)^{-1/2}$ *(compiler check, not in the sources; worked out
  on [geometric quasilinearization](/methods/geometric-quasilinearization.md))*;
  the version of record should decide.

# Citations

- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §6 (Eqs. (6.3)–(6.5), (6.17)–(6.22); Thms 6.1, 6.2, 6.4; Rem. 6.3); §7 (Ex. 7.1–7.2, Figs. 5–6).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §5.3 (Eqs. (51)–(52)); §5.3.1 (Figs. 10–11).
- [Fu (2023)](/sources/fu-2023.md) — §5.3, Fig. 19.
