---
type: Method
title: "Unstaggered central schemes"
description: "Unstaggered central schemes evolve a piecewise-linear solution on a single grid without Riemann solvers by passing through implicit staggered dual cells — forward projection, Nessyahu–Tadmor predictor–corrector on the dual cells, back projection — and, in the source of this bundle, carry a deviation-based well-balancing and a constrained-transport correction for ideal MHD with gravity."
status: established
aliases: [UC scheme, unstaggered Nessyahu–Tadmor scheme, Jiang–Levy–Lin–Osher–Tadmor scheme, ghost staggered cells, Riemann-solver-free central scheme]
tags: [central-scheme, finite-volume, well-balanced, mhd]
timestamp: 2026-10-22T00:00:00Z
---

# Unstaggered central schemes

An **unstaggered central (UC) scheme** is a second-order, Riemann-solver-free
finite-volume scheme that keeps the solution on one grid while evolving it, as the
staggered scheme of Nessyahu and Tadmor does, on dual cells centred at the vertices of
the primary cells; the dual cells are "ghost" cells used only inside a time step. It is
the base scheme of [Kanbar et al. (2022)](/sources/kanbar-2022.md), who recall it from
Jiang, Levy, Lin, Osher and Tadmor and from Touma, and apply it to
$\partial_tu+\partial_xf(u)+\partial_yg(u)=S(u)$, 2D ideal MHD with gravity (§1, §3). It
belongs to a different family from the [central-upwind schemes](/methods/central-upwind-scheme.md):
it uses no local speeds at all, only flux values at cell centres and a staggered
average.

## One time step

Primary cells $C_{i,j}=[x_{i-1/2},x_{i+1/2}]\times[y_{j-1/2},y_{j+1/2}]$, dual cells
$D_{i+1/2,j+1/2}=[x_i,x_{i+1}]\times[y_j,y_{j+1}]$; cell averages are identified with
the values at the centres (§3, Fig. 1). The undivided slopes $u'^x_{i,j}$, $u'^y_{i,j}$
(page-local) are limited componentwise by the three-argument MC limiter with parameter
$1.5$ (Eq. (8); see [TVD](/definitions/total-variation-diminishing.md)). With
$A^{(d)}$ the flux Jacobians, the step reads (§3, Eqs. (12)–(16)):

1. **Forward projection** onto the dual cell, the 2D Nessyahu–Tadmor staggered
   average:
   $$u^n_{i+\frac12,j+\frac12}=\tfrac14\big(u_{i,j}+u_{i+1,j}+u_{i,j+1}+u_{i+1,j+1}\big)^n-\tfrac1{16}\big([\![u'^x]\!]_{i+\frac12,j}+[\![u'^x]\!]_{i+\frac12,j+1}+[\![u'^y]\!]_{i,j+\frac12}+[\![u'^y]\!]_{i+1,j+\frac12}\big)^n,$$
   with $[\![\cdot]\!]$ the jump between the two neighbouring centres.
2. **Predictor** at $t^{n+1/2}$ at the primary centres, by a first-order Taylor step:
   $u^{n+1/2}_{i,j}=u^n_{i,j}-\frac{\Delta t}{2}\Big(\frac{A^{(1)}u'^x_{i,j}}{\Delta x}+\frac{A^{(2)}u'^y_{i,j}}{\Delta y}\Big)+\frac{\Delta t}{2}S_{i,j}$.
3. **Corrector** on the dual cell, integrating over the space–time box with the
   midpoint rule; the fluxes are evaluated at the four primary centres that bound it, so
   there is no Riemann problem:
   $$\begin{aligned}u^{n+1}_{i+\frac12,j+\frac12}=u^n_{i+\frac12,j+\frac12}&-\tfrac{\Delta t}{2\Delta x}\big[f_{i+1,j}-f_{i,j}+f_{i+1,j+1}-f_{i,j+1}\big]^{n+\frac12}\\&-\tfrac{\Delta t}{2\Delta y}\big[g_{i,j+1}-g_{i,j}+g_{i+1,j+1}-g_{i+1,j}\big]^{n+\frac12}+\Delta t\,\bar S^{n+\frac12},\end{aligned}$$
   with $\bar S$ the average of $S$ at the four centres (Eq. (12)).
4. **Back projection** to the primary cells by the same staggered average with the
   dual-cell slopes, again MC-limited (Eq. (16)).

*(Compiler check, not in the sources: the source writes these steps for the
deviation $\delta u$ of the next section; with $u_{\mathrm e}=0$ they reduce to the form
above.)*

## Well-balancing and constrained transport

- **Deviation formulation.** Kanbar et al. apply the four steps to the deviation
  $\delta u=u-u_{\mathrm e}$ from a known stationary state $u_{\mathrm e}$, with every flux
  replaced by $f(\delta u+u_{\mathrm e})-f(u_{\mathrm e})$, and prove that $\delta u^n=0$
  gives $\delta u^{n+1/2}=0$ (Eq. (17)). The details and the tests (hydrostatic and
  magnetohydrostatic atmospheres, a stationary MHD vortex) are on
  [well-balancing](/properties/well-balancing.md).
- **Constrained transport for UC schemes** (Touma, as recalled; §4, Eqs. (18)–(21)). At
  the end of a step the magnetic field is re-updated on the dual cells from the discrete
  induction equation with $\Omega=-v_1B_2+v_2B_1$ (page-local) at $t^{n+1/2}$, then
  averaged back to the centres; this keeps the wide centred-difference divergence
  $\frac{B_{1,i+1,j}-B_{1,i-1,j}}{2\Delta x}+\frac{B_{2,i,j+1}-B_{2,i,j-1}}{2\Delta y}$ at zero
  if it was zero. On a four-state MHD Riemann problem ($400^2$, $t=0.8$) the divergence
  stays at $O(10^{-14})$ with the correction and reaches $O(1)$ without it (§5.2,
  Fig. 5). The correction is applied "whenever needed", with no criterion given (§6).
  See [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Evidence and parameters

All tests use CFL 0.485 and MC parameter 1.5 (§5). The Brio–Wu tube on a 2D domain
(200, 400, 800 points, with and without constrained transport, which smears slightly),
the MHD Riemann problem above, the stationary MHD vortex, and hydrodynamic and MHD wave
propagation in stratified atmospheres, compared visually with the third-order schemes
of Fuchs et al. (§5.4–5.5, Figs. 8–12), which the authors describe as matching "the most
accurate (third order)" of them.

## Qualifications

- Second order is the formal order of the scheme; the paper prints no convergence table
  or error norm (§5.1 calls a three-grid overlay a "convergence study").
- The preserved divergence is the collocated centred one, not the face-centred one of
  staggered constrained transport, and it is zero only in the steps where the
  correction is applied.
- Printed slips in the version read: the second bracket of the corrector (Eq. (14))
  prints one $D^y_+F$ where $D^y_+G$ is meant; the space–time box is printed
  $[x_i,x_{i+1}]\times[y_i,y_{i+1}]$ for $[y_j,y_{j+1}]$.

# Citations

- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §1, §3 (Eqs. (8)–(17), Fig. 1), §4 (Eqs. (18)–(21)), §5 (Figs. 3–12), §6 (arXiv v1).
