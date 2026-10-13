---
type: Method
title: "Recovery discontinuous Galerkin for diffusion"
description: "Van Leer–Nomura DG treatment of diffusion: at each interface, recover the smooth polynomial of degree 2K+1 on the two adjacent cells that has the same Legendre moments as the discrete solution, and take its value and derivative in the twice-integrated weak form; Fourier analysis gives fourth order for K = 1 (confirmed on one steady test) and a good eigenvalue of order eight for K = 2 (unconfirmed), and the scheme lies outside the interior-penalty (σ, μ) family unless a new jump-of-derivative term is added."
status: established
aliases: [recovery DG, recovery-based DG, recovery principle, optimal recovery, RDG diffusion, van Leer–Nomura recovery]
tags: [dg, accuracy, legendre-basis, stability]
timestamp: 2026-10-13T00:00:00Z
---

# Recovery discontinuous Galerkin for diffusion

**The problem** ([van Leer & Nomura (2005)](/sources/vanleer-2005.md),
§§1, 3). A DG scheme for advection takes the discontinuous data "as is"
and borrows upwind interface values (Riemann solvers) from finite
volume. Diffusion has no such guide. The classic DG diffusion terms
(Arnold's interior penalty, the Symmetric and the Baumann bilinear terms,
which van Raalte unified as a two-parameter family) are, in the authors'
reading, *ad hoc* Lagrange-multiplier terms. The recovery principle
replaces them with one rule: diffusion needs an unbiased, smooth
interpretation of the data on both sides of a face, whereas advection
needs an upwind one. The authors hold that the two interpretations of the
same data are not in contradiction (§2, §4.1).

Notation: the model problem is $u_t = \mu u_{xx}$ with diffusion
coefficient $\mu$; the solution in $I_i$ is the polynomial
$\mathcal P_i = \sum_{l=0}^{K}\hat u^{(l)}_i P_l(\zeta)$ of degree $K$
([notation](/notation.md)). At an interface, $[\![q]\!]_{i+1/2}$ is the
jump (right trace minus left trace) and $\{\!\{q\}\!\}_{i+1/2}$ the
average of the two traces.

## The interior-penalty family it is compared with

(§3.3, eq. 32, as printed, with the test function $P_l$ supported in
$I_i$.)
$$\begin{aligned}
\int_{I_i} P_l\,u_t\,dx ={}& -\mu\left(\{\!\{u_x\}\!\}[\![P_l]\!]\big|_{i+1/2} + \{\!\{u_x\}\!\}[\![P_l]\!]\big|_{i-1/2}\right) - \mu\int_{I_i}(P_l)_x\,u_x\,dx \\
&+ \sigma_{\mathrm{DG}}\,\mu\left(\{\!\{(P_l)_x\}\!\}[\![u]\!]\big|_{i+1/2} + \{\!\{(P_l)_x\}\!\}[\![u]\!]\big|_{i-1/2}\right) - \frac{\mu_{\mathrm{IP}}\,\mu}{h}\left([\![P_l]\!][\![u]\!]\big|_{i+1/2} + [\![P_l]\!][\![u]\!]\big|_{i-1/2}\right).
\end{aligned}$$
$\sigma_{\mathrm{DG}} = -1$ is the Symmetric scheme, which needs the
penalty $\mu_{\mathrm{IP}}$; $\sigma_{\mathrm{DG}} = 1$, $\mu_{\mathrm{IP}} = 0$
is Baumann's, stable without penalty and, citing others, dispersive for
basis degree at least 3.
* **$K = 0$** (§3.4, eqs. 33–35). Only the penalty survives, and
  consistency with the three-point Laplacian requires exactly
  $\mu_{\mathrm{IP}} = 1$, giving
  $\frac{d}{dt}\bar u_i = \frac{\mu}{h^2}\,\delta^2\bar u_i$. The weak form
  alone does not fix the penalty, as it does not fix the upwind value for
  $K = 0$ advection (§2.4); the authors read both as a lapse of the
  finite-element doctrine.
* **$K = 1$, Fourier analysis** (§3.5, eqs. 36–58). In units of
  $\mu/h^2$, with $\xi$ the [scaled wavenumber](/definitions/modified-wavenumber.md),
  the symbol of the scheme acting on $(\bar u_i, \hat u^{(1)}_i)$ is
  $$\begin{pmatrix} -2\mu_{\mathrm{IP}}(1-\cos\xi) & i(1-\mu_{\mathrm{IP}})\sin\xi \\ 12i(\sigma_{\mathrm{DG}}+\mu_{\mathrm{IP}})\sin\xi & -6(1+\sigma_{\mathrm{DG}}+\mu_{\mathrm{IP}}) + 6(1-\sigma_{\mathrm{DG}}-\mu_{\mathrm{IP}})\cos\xi\end{pmatrix}$$
  (eq. 48), to be compared with $-\xi^2$ times the identity.
  - *Baumann:* eigenvalues $-6\left(1 \mp \sqrt{1 - \tfrac13\sin^2\xi}\right)$
    (eq. 52). The good one is $-\xi^2 + O(\xi^4)$, but it vanishes at
    $\xi = \pi$, so the $2h$ mode is undamped: odd–even decoupling (p. 11).
    This is a diffusion-operator null mode, a different mechanism from the
    [numerical shock instability](/definitions/numerical-shock-instability.md)
    of the same name.
  - *Symmetric:* without penalty the eigenvalues have opposite signs
    (unstable, eq. 54). The minimal stabilizing penalty
    $\mu_{\mathrm{IP}} = 1$ decouples averages and slopes, with
    eigenvalues $-2(1-\cos\xi)$ and $-6(1-\cos\xi)$ (eq. 55).
  - Both are second order, because the slope update is not consistent
    with $\partial_t u_x = \mu\,\partial_x^2 u_x$. Consistency needs
    $\sigma_{\mathrm{DG}} + \mu_{\mathrm{IP}} = \tfrac52$ (eq. 57, stated
    "omitting details"); the member $\mu_{\mathrm{IP}} = \tfrac94$,
    $\sigma_{\mathrm{DG}} = \tfrac14$ (eq. 58), "not studied previously",
    has a fourth-order eigenvalue and bad-eigenfunction weight $O(\xi^4)$
    (Appendix A3, no proof).

## Recovery

**Principle** (§4.1, eq. 59). At $x_{i+1/2}$, recover the polynomial
$u^{\mathrm{rec}}_{i+1/2}$ on $I_i \cup I_{i+1}$ that is weakly
indistinguishable from the discrete solution:
$$\int_{I_i} P_l\,u^{\mathrm{rec}}_{i+1/2}\,dx = \int_{I_i} P_l\,\mathcal P_i\,dx,\qquad \int_{I_{i+1}} P_l\,u^{\mathrm{rec}}_{i+1/2}\,dx = \int_{I_{i+1}} P_l\,\mathcal P_{i+1}\,dx,\qquad l = 0,\dots,K,$$
each $P_l$ in its own cell's coordinate. The $2K+2$ conditions fix a
polynomial of degree $2K+1$. The union of the two neighbours is an
unbiased interval: "the proper choice with regard to diffusion – and, in
turn, useless for advection". The update integrates by parts once more
than the usual weak form (eq. 64):
$$\int_{I_i} P_l\,u_t\,dx = \mu\Big[P_l\,\partial_x u^{\mathrm{rec}} - (P_l)_x\,u^{\mathrm{rec}}\Big]_{x_{i-1/2}}^{x_{i+1/2}} + \mu\int_{I_i}(P_l)_{xx}\,\mathcal P_i\,dx,$$
with $u^{\mathrm{rec}}_{i+1/2}$ at the right face and
$u^{\mathrm{rec}}_{i-1/2}$ at the left one, the test function traced from
inside $I_i$.

* **$K = 0$** (§4.2, eqs. 60–66). The recovered derivative is
  $(\bar u_{i+1} - \bar u_i)/h$ and the scheme is the $\mu_{\mathrm{IP}} = 1$
  scheme above, obtained "for the right reason", with no parameter to
  tune. Using the recovered value $\tfrac12(\bar u_i + \bar u_{i+1})$ as an
  *advective* interface value gives the unstable central scheme.
* **$K = 1$ ("Optimal Recovery")** (§4.3, eqs. 67–80). The recovery is
  cubic, with face values (eqs. 71–72)
  $$u^{\mathrm{rec}}_{i+1/2}(x_{i+1/2}) = \tfrac12(\bar u_i + \bar u_{i+1}) - \tfrac16\left(\hat u^{(1)}_{i+1} - \hat u^{(1)}_i\right),\qquad \partial_x u^{\mathrm{rec}}_{i+1/2}(x_{i+1/2}) = \frac1h\left\{\tfrac94(\bar u_{i+1} - \bar u_i) - \tfrac58\left(\hat u^{(1)}_i + \hat u^{(1)}_{i+1}\right)\right\},$$
  and third derivative $-15\,[\![u]\!]_{i+1/2}/h^3$ (eq. 74). The scheme
  (eq. 77) is
  $$\begin{aligned}
  \frac{d}{dt}\bar u_i &= \frac{\mu}{h^2}\left\{\tfrac94\,\delta^2\bar u_i - \tfrac58\left(\hat u^{(1)}_{i+1} - \hat u^{(1)}_{i-1}\right)\right\},\\
  \frac{d}{dt}\hat u^{(1)}_i &= \frac{\mu}{h^2}\left\{\tfrac{15}{2}\left(\bar u_{i+1} - \bar u_{i-1}\right) + 2\left(\hat u^{(1)}_{i+1} - 2\hat u^{(1)}_i + \hat u^{(1)}_{i-1}\right) - \tfrac{15}{4}\left(\hat u^{(1)}_{i+1} + 2\hat u^{(1)}_i + \hat u^{(1)}_{i-1}\right)\right\}.
  \end{aligned}$$
  Its eigenvalues, in units of $\mu/h^2$ (eq. 79),
  $$-\tfrac{15}{2} - \tfrac12(1-\cos\xi) \pm \tfrac{15}{2}\sqrt{1 - \tfrac25(1-\cos\xi) - \tfrac{11}{225}(1-\cos\xi)^2},$$
  are real and negative (stable). The bad one lies in $[-15, -9]$; the
  good one is $-\xi^2 + O(\xi^6)$ (eq. 80), and the bad eigenfunction
  enters the projected initial data with amplitude $O(\xi^6)$ (eq. 118).
  The authors conclude the scheme is "truly fourth-order accurate" (p. 16,
  Appendix A2).
* **$K = 2$** (§4.4, eqs. 81–85; Appendix A4). All three eigenvalues are
  real and negative; the good one is $-\xi^2 + O(\xi^{10})$ (eq. 85), and
  the bad-eigenfunction amplitudes are $O(\xi^8)$. This suggests eighth
  order, "at least when regarding only the cell averages", against the
  $2K+2 = 6$ the principle promises. The test errors sat at round-off
  already on a 4-cell grid, so neither order is confirmed (§6). The
  scheme matrix for $K = 2$ is not printed.

**What is claimed, and how.** The abstract claims order "at least
$2K+2$". Every order statement rests on Fourier eigenvalue and
eigenvector analysis of the periodic problem, not on a proof. Stability
for $K = 1, 2$ is no guarantee for higher $K$: "a general proof remains
to be found" (p. 16).

**Order needs two things** (Appendix A1). A DG scheme's formal accuracy
combines the accuracy of its best eigenvalue (the operator error, which
governs steady solutions) and the weight of the bad eigenfunctions in the
projected initial data (the starting error). The two need not agree:
Baumann's scheme has a fourth-order starting error and a second-order
operator error (Appendix A3). For a nonlinear scheme the starting error
recurs every step, because the bad eigenfunction is regenerated
(footnote 8). This extends the first-derivative
[modified-wavenumber](/definitions/modified-wavenumber.md) analysis to a
second-derivative operator with two unknowns per cell.

## Relation to the penalty family

* **Recovery is outside it** (§5.1). With $\mu_{\mathrm{IP}} = \tfrac94$,
  $\sigma_{\mathrm{DG}} = -1$, every entry of the $K = 1$ family matrix
  matches recovery except the second-difference part of the slope
  equation: coefficient 3 in the family, for any parameters, against 2
  in recovery.
* **Suboptimal recovery** (§5.2, eqs. 86–92). Averaging the recovered
  value and derivative over the staggered cell
  $[x_i, x_{i+1}]$ (adding $\tfrac{h^2}{24}$ times the second and third
  derivatives) gives eigenvalues $-2(1-\cos\xi) = -\xi^2 + O(\xi^4)$ and
  $-7 - \tfrac12\cos\xi$ (eqs. 90–91): second order, with the same good
  eigenvalue as the $K = 0$ scheme and the stabilized Symmetric scheme.
  It is offered as a fall-back if optimal recovery turns out unstable at
  some $K$ (p. 16).
* **Extended family** (§5.3, eqs. 93–101). A new term
  $\omega_{\mathrm{DG}}\,\mu h\left([\![(P_l)_x]\!][\![u_x]\!]\big|_{i+1/2} + [\![(P_l)_x]\!][\![u_x]\!]\big|_{i-1/2}\right)$
  has no effect at $K = 0$ and adds $-12\,\omega_{\mathrm{DG}}$ times the
  second difference to the slope equation. Optimal recovery is
  $(\mu_{\mathrm{IP}}, \sigma_{\mathrm{DG}}, \omega_{\mathrm{DG}}) = (\tfrac94, -1, \tfrac1{12})$
  and suboptimal recovery $(\tfrac{13}{8}, -1, \tfrac16)$. Both have the
  Symmetric $\sigma_{\mathrm{DG}} = -1$; Baumann's $+1$ "appears to be an
  odd choice, unconnected to the recovery principle". More terms are
  expected for $K \ge 2$.

## Evidence

One test (§6, eqs. 102–106; $K = 1$ only): the steady state of
$u_t = \mu u_{xx} + 4\pi^2\mu\sin(2\pi x)$ on $(0, 1)$, with $u(0) = 1$
and $u_x(1) = 2\pi - 1$, exact solution $\sin(2\pi x) + 1 - x$, measured
on cell averages. The paper does not print $\mu$, the time integrator or
the grid sizes; the Fig. 5 axis shows four grids of roughly 8 to 64 cells
(read from the axis). $L_2$ slopes read from Fig. 5:

| scheme | slope |
|---|---|
| Optimal Recovery | 3.967 |
| $(\sigma_{\mathrm{DG}}, \mu_{\mathrm{IP}}) = (\tfrac14, \tfrac94)$ | 3.497 (from 4 in $L_1$ to 3 in $L_\infty$, attributed to a third-order boundary error) |
| Suboptimal Recovery, stabilized Symmetric | 2.002 (equal errors) |
| Baumann | 2.078 (largest error) |

* Recovery and the $(\tfrac14, \tfrac94)$ scheme end about 3.5 decades
  below the second-order schemes.
* Baumann with Dirichlet conditions at both ends shows visible
  odd–even decoupling on 32 cells (Fig. 6); with the Neumann end, the
  $2h$ mode was damped.
* **The boundary sets the order.** Recovery at the boundary uses the
  boundary condition plus one or two interior cells. In $L_\infty$,
  Optimal Recovery gives 2.882 with a quadratic boundary fit and 3.922
  with a quartic one (Fig. 7). The same lesson, that a boundary closure
  can cap an interior scheme, recurs for capturing schemes in
  [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md).
* Not tested: time accuracy, advection–diffusion, multi-D, nonlinear
  problems, shocks.

## Context in this bundle

* The hyperbolic DG of [WENO-limited DG](/methods/weno-limited-dg.md)
  has this paper's history behind it: Reed and Hill (1973) for steady
  transport, and van Leer's 1977 Schemes III (linear) and VI (quadratic)
  as unsteady DG with exact-shift time stepping. Scheme III has one
  eigenfunction advected at third order (superconvergence) and one quickly
  damped; its extension to nonlinear systems failed because the exact
  shift no longer applies, hence today's method-of-lines decoupling (§2.3).
  The $K = 1$ recovery eigenfunctions and the 1977 advection
  eigenfunctions are "indistinguishable within the eyeball norm" at
  $\xi = \pi/5$, which the authors take to suggest the two fit together
  for convection–diffusion DG (Appendix A2).
* Finite volume (§3.2): the usual face gradient
  $(\bar u_{i+1} - \bar u_i)/h$ treats averages as point values, that is,
  differentiates the continuous piecewise-linear interpolant, which does
  not conserve cell averages; a short-time exact diffusion solution at
  each jump is not consistent, because its time-averaged flux scales as
  $(\mu\Delta t)^{-1/2}$. The [fourth-order finite-volume](/methods/fourth-order-finite-volume.md)
  scheme likewise takes face gradients from a smooth reconstruction across
  the face.
* A penalty on the interface jump appears elsewhere with another goal:
  the Lax–Friedrichs-type viscous flux of [positivity preservation](/properties/positivity-preserving.md)
  chooses its penalty for positivity, whereas van Leer and Nomura reject
  penalties as unmotivated for accuracy and consistency (compiler's
  contrast; the papers do not discuss each other).
* Explicit time stepping (§3.1). Forward-time centred diffusion is stable
  for $\mu\Delta t/h^2 \le \tfrac12$; Richardson's leap-frog version and a
  one-sided version are unconditionally unstable, and "advection and
  diffusion operators are opposites". The paper gives no step bound for
  the recovery schemes; it notes only that the bad eigenfunction "may be
  strongly damped by a suitable time-integrator" (p. 11).

# Citations

1. [van Leer & Nomura (2005)](/sources/vanleer-2005.md), §§1–6, Appendices A1–A4 (all equations read from the page images; figure values read off the plots).
