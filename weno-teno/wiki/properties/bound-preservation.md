---
type: Property
title: "Bound preservation"
description: "A scheme is bound-preserving when its discrete solution stays in the convex admissible set G of the PDE; the page states the definition, the convexity requirement, the cell-average route of Zhang and Shu, the flux- and convex-limiting routes, and the geometric-quasilinearization proofs."
status: established
aliases: [bound-preserving scheme, positivity preservation, invariant-region preservation, invariant-domain preservation, BP, PP, IDP]
tags: [bound-preserving, positivity, limiting, dg, finite-volume]
timestamp: 2026-10-21T12:00:00Z
---

# Bound preservation

Let $G$ be the admissible set (invariant region) of a hyperbolic system: a
set of states, written $G=\{u:g_i(u)>0\ \text{or}\ \ge0,\ i=1,\dots,I\}$
with constraint functions $g_i$, that the exact solution never leaves,
$u(\cdot,0)\in G\Rightarrow u(\cdot,t)\in G$. A numerical scheme is
**bound-preserving** (BP) if the same holds for the discrete solution:
$u_h(\cdot,t^0)\in G\Rightarrow u_h(\cdot,t^n)\in G$ for all $n$
([Wu & Shu (2023)](/sources/wu-2023-b.md), §1, Eq. (1.4)). Positivity
preservation (density and pressure, or density and internal energy, for gas
dynamics) and the maximum principle (scalar laws) are the instances Cui et
al. treat ([Cui, Ding & Wu (2024)](/sources/cui-2024.md), §1, §7).

## Admissible sets used by the sources

| System | $G$ | Source |
|---|---|---|
| scalar law | $[U_{\min},U_{\max}]$ (global maximum principle) | Cui et al. (2024), §1 |
| Euler / Navier–Stokes | $\{\rho>0,\ \rho e>0\}$ | Wu & Shu (2023), Eq. (2.2); Cui et al. (2024), Rem. 8.1 |
| Euler with Tadmor's minimum entropy principle | $\{\rho>0,\ \rho e>0,\ s\ge s_{\min}\}$, i.e. $p\rho^{-\gamma}\ge\exp(s_{\min})$, $s_{\min}$ the initial minimum of $s$ | Wu & Shu (2023), Eq. (2.3), Thm 4.7 |
| special relativistic hydrodynamics | $\{D>0,\ E-\sqrt{D^2+\lvert m\rvert^2}>0\}$ ($D=\rho W$ the relativistic mass density, $m$ the momentum) | Wu & Shu (2023), Thm 4.9; Cui et al. (2024), Ex. 4–5 |
| ten-moment Gaussian closure | positive-definite pressure tensor | Wu & Shu (2023), Thm 4.11 |
| ideal MHD | $\{\rho>0,\ E-\tfrac12\rho\lvert v\rvert^2-\tfrac12\lvert B\rvert^2>0\}$ | Wu & Shu (2023), Thm 4.12 |
| multicomponent MHD | $0\le Y_k\le1$, $\rho>0$, $p>0$ ($Y_k$ the mass fractions) | Wu & Shu (2023), Eq. (6.4) |

Every set in the table is convex. Convexity is not incidental:
[Wu & Shu (2023)](/sources/wu-2023-b.md) take "$G$ convex with nonempty
interior" as the minimal hypothesis of their theory (Assumption 3.4),
because the cell-average arguments below write updated states as convex
combinations of admissible states, and because a set that is an
intersection of halfspaces is necessarily convex (§3). The constraint
functions themselves need not be concave (§3). In the Zhang–Shu limiter
for MHD they replace the non-concave pressure by the concave
$E-\frac12(\lvert\rho v\rvert^2/\rho+\lvert B\rvert^2)$ (App. B).

## Route 1: first-order BP scheme, cell-average decomposition, scaling limiter

The framework recalled by [Cui et al. (2024)](/sources/cui-2024.md) (§1,
Eqs. (1.3)–(1.8), after Zhang and Shu) and used by
[Wu & Shu (2023)](/sources/wu-2023-b.md) (§6, App. B) has three
ingredients.

1. **A BP first-order scheme.** With a monotone or otherwise BP two-point
   flux $h$, the three-point update
   $\bar u_i^{n+1}=\bar u_i^n-\frac{\Delta t}{\Delta x}\big(h(\bar u_i,\bar u_{i+1})-h(\bar u_{i-1},\bar u_i)\big)$
   stays in $G$ under $a\Delta t/\Delta x\le c_0$. Cui et al. give $c_0=1$
   for the [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) and
   $c_0=1/2$ for [HLL and HLLC](/methods/hll-riemann-solvers.md)
   (§7, after Eq. (7.5)); let $c_0$ denote this first-order BP CFL
   constant (page-local). Wu & Shu prove the Lax–Friedrichs case for Euler
   by geometric quasilinearization: the scheme is BP under $\nu\le1$ with
   $a$ the global maximum of $\lvert v\rvert+c$ (§5.1, Ex. 1.1).
2. **A cell-average decomposition.** The cell average of the
   high-order polynomial is written as a convex combination of point
   values that includes the interface traces. The high-order cell-average
   update then becomes a convex combination of first-order updates, and
   is BP under a CFL condition proportional to the smallest boundary
   weight $\varpi$ of the decomposition
   ([optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
3. **A limiter** that brings the point values used by the decomposition
   back into $G$ without changing the cell average
   ([Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).

The property that results is called *weak* bound preservation in the
literature these sources recall: the cell average is guaranteed in $G$
when the point values are, and the limiter supplies the point values
([Wu & Shu (2023)](/sources/wu-2023-b.md), concepts recalled in §1 and
§6.2). The BP CFL number of the standard Gauss–Lobatto decomposition is
$\mathsf w_0^{\mathrm{GL}}=1/(L(L-1))$ with $L=\lceil(N+3)/2\rceil$ in 1D
and on Cartesian $\mathbb Q^N$ cells; Cui et al. prove it optimal there and,
for $\mathbb P^N$ at zero anisotropy, improve it by a factor between 1.5
($N=2,3$) and about 1.74 ($N=6,7$) (Thms 2.3, 4.1; Table 1; the ratios
are the compiler's, from the tabulated values).

**Time stepping.** Both sources extend the forward-Euler result to
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) and SSP multistep methods,
because SSP methods are convex combinations of forward-Euler steps
([Wu & Shu (2023)](/sources/wu-2023-b.md), §6.2 after Thm 6.4;
[Cui et al. (2024)](/sources/cui-2024.md), footnote 2, Rem. 7.9). The
limiter must then be applied at every stage.

## Route 2: proofs for nonlinear constraints — geometric quasilinearization

For nonlinear $g_i$ (pressure as a function of conservative variables,
implicit pressure in relativistic hydrodynamics, positive-definite
tensors), checking that a convex combination stays in $G$ is the hard
step. [Wu & Shu (2023)](/sources/wu-2023-b.md) replace each nonlinear
constraint by a family of constraints affine in $u$, indexed by free
auxiliary variables: for convex $G$ with piecewise-$C^1$ boundary,
$G=\{u:(u-u_*)\cdot n_*\succ0\ \forall u_*\in\partial G\}$ (Thms 3.9,
3.10). The method page is
[geometric quasilinearization](/methods/geometric-quasilinearization.md).
Its use for BP is that linearity commutes with the convex-combination and
flux-difference structure of the update: Wu & Shu give short BP proofs for
first-order Lax–Friedrichs and gas-kinetic schemes for Euler, a
Navier–Stokes scheme without convex splitting of convection and diffusion,
and a ten-moment Lax–Friedrichs scheme (§5).

## Route 3: limiting against a low-order BP scheme

A high-order update can be blended with a low-order BP update, in fluxes
or in residuals, with a blending factor chosen so that the result meets
the bounds: [convex limiting](/methods/convex-limiting.md) and
flux-corrected transport. [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
blend a DGSEM with a compatible subcell finite-volume scheme and enforce
positivity of $\rho$ and $p$ either relative to the finite-volume solution
($\rho\ge0.1\rho^{\mathrm{FV}}$, $p\ge0.1p^{\mathrm{FV}}$, Eq. (43)) or
through invariant-domain bounds built from Guermond–Popov bar states
(Eqs. (47)–(48))
([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
Several finite-difference papers of the corpus obtain positivity this way
from an external flux limiter (Hu, Adams & Shu 2013, as recalled by them)
rather than from the reconstruction: TENO-AA for near-vacuum and Mach 2000
jet cases ([Fu (2021)](/sources/fu-2021.md), §5.7, claim "with the
assistant of a positivity-preserving flux limiter"), TENO-THINC for the
Mach 80 and 2000 jets ([Takagi et al. (2022)](/sources/takagi-2022.md),
§4.9), and affine-invariant WENO, which "is not positivity preserving in
general" and needs the limiter on the Mach 2000 jet, where it activates
only near the jet front and inlet corners
([Wang & Don (2022)](/sources/wang-2022-b.md), §3.2.4, Fig. 8).

## Bound preservation and the divergence of the magnetic field

For ideal and multicomponent MHD the BP property of the cell-average
update is tied to a discrete divergence-free condition on $B$: the
first-order Lax–Friedrichs update satisfies the GQL constraint only up to
a term proportional to a discrete $\nabla\cdot B$ ([Wu & Shu (2023)](/sources/wu-2023-b.md),
Thms 6.1–6.2). The details are on
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Qualifications

- **Local versus global bounds.** [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)
  state that schemes of order above two cannot be *locally* bound
  preserving in general, so that local discrete maximum principles impose
  a second-order barrier, whereas global bounds (as in the Zhang–Shu
  framework) impose none (§1, §3, citing Zhang and Shu). The claim is
  stated, not proved there. The invariant-domain bounds of Rueda-Ramírez
  et al. are local (bar states of neighbouring nodes); that paper reports
  no convergence-order study, so the corpus contains no test of what such
  local bounds cost in accuracy.
- **Guarantees that are not guarantees.** When Rueda-Ramírez et al. use
  HLLE or second-order subcell reconstruction as the low-order scheme,
  the bar-state bounds are no longer guaranteed to be attainable, and the
  blending returns the solution "closest to the restrictions" (§5.2.3).
  Those variants are not provably invariant-domain preserving.
- **No BP claim for OEDG.** The oscillation-eliminating DG method computes
  the Mach 2000 jet and double Mach reflection without mentioning a
  positivity limiter and claims no bound preservation
  ([Peng, Sun & Wu (2024)](/sources/peng-2024.md), Ex. 5.17–5.18;
  [OEDG](/methods/oedg.md)).
- **Accuracy of the limiter.** That the scaling limiter keeps high-order
  accuracy is cited, not shown, in Wu & Shu (2023) (App. B); Cui et al.
  (2024) show it numerically for $\mathbb P^2$, $\mathbb P^4$, $\mathbb P^6$
  and $\mathbb P^8$ DG (Ex. 1, Tables 3–6).

# Citations

- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §1 (definition, Eq. (1.4)); §3 (Assumption 3.4, Thms 3.9–3.10); §4.2 (admissible sets); §5 (first-order BP proofs); §6 (MHD, Thms 6.1–6.4); App. B (limiter).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §1 (Zhang–Shu framework, Eqs. (1.3)–(1.15)); §7 (Thms 7.1, 7.5, 7.6; $c_0$ values); Table 1; Rem. 8.1.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.4 (Eqs. (23)–(29)); §5.2 (Eqs. (43), (47)–(48)); §5.2.3.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §1, §3 (order barrier of local bounds, stated).
- [Fu (2021)](/sources/fu-2021.md) — arXiv v1: Abstract, §5.7 (external positivity-preserving flux limiter).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.9 (positivity-preserving flux limiter for the jets).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.4, Fig. 8 (limiter needed by affine-invariant WENO).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: Ex. 5.17–5.18 (no positivity limiter mentioned).
