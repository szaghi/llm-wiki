---
type: Method
title: "WENO reconstruction"
description: "Weighted essentially non-oscillatory reconstruction: a convex combination of candidate-stencil interpolants whose nonlinear weights recover the high-order central stencil in smooth regions and drop stencils that cross discontinuities; constraint-agnostic, so every MHD use pairs it with a divergence mechanism."
status: established
aliases: [WENO, WENO-JS, WENO5, weighted ENO]
tags: [weno, reconstruction, high-order, finite-difference, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# WENO reconstruction

A high-order, shock-capturing reconstruction. In its standard form,
fixed by [Jiang & Shu (1996)](/sources/jiang-shu-1996.md), it is a
finite-difference scheme on point values. The primary source contains no
MHD and no divergence constraint: everything this bundle uses it for comes
from later papers (below).

## Definition

For the face $j+1/2$, each candidate stencil $k$ of $k_{\mathrm s}$ points
containing the upwind cell gives a polynomial interpolant and a face value
$w^{(k)}_{j+1/2}$; with $k_{\mathrm s} = 3$ there are three candidates. The
reconstructed value is their convex combination

$$w^-_{j+1/2} = \sum_k \omega_k\, w^{(k)}_{j+1/2},\qquad
\omega_k = \frac{d_k/(\epsilon_{\mathrm W} + \mathrm{IS}_k)^{p_{\mathrm W}}}{\sum_l d_l/(\epsilon_{\mathrm W} + \mathrm{IS}_l)^{p_{\mathrm W}}}.$$

The linear (optimal) weights $d_k$ reproduce the upstream central value on
the union of the stencils: fifth order for $k_{\mathrm s} = 3$, with
$d_k = (1/10, 6/10, 3/10)$, and third order for $k_{\mathrm s} = 2$, with
$d_k = (1/3, 2/3)$ (Table 2). In Jiang & Shu's finite-difference form, $w$
is one component of the split flux at the points $x_j$, and the combined
face value is the numerical flux at $x_{j+1/2}$ (eq. 2.10). Full central order in smooth regions needs
$\omega_k - d_k = O(h^2)$. A stencil crossing a discontinuity has
$\mathrm{IS}_k = O(1)$, so with $p_{\mathrm W} = 2$ its weight falls to
$O(h^4)$, and the scheme behaves like ENO stencil selection there
([Jiang & Shu (1996)](/sources/jiang-shu-1996.md), eqs. 2.10–2.17,
2.26–2.28).

**The WENO-JS indicator** (eq. 3.1). $\mathrm{IS}_k$ is the sum, over the
derivative orders 1 to $k_{\mathrm s}-1$, of the cell integral of the squared
derivative of stencil $k$'s interpolant, scaled by the power of $h$ that
removes the $h$-dependence. It replaced the
Liu–Osher–Chan indicator (squared undivided differences), which gives
only fourth order (three-point stencils) in smooth monotone regions and
third order at critical points. The paper's constants are $\epsilon_{\mathrm W} = 10^{-6}$
and $p_{\mathrm W} = 2$, for $k_{\mathrm s} = 2$ and 3 (§2). The explicit three-point indicators are on the [source page](/sources/jiang-shu-1996.md).

**Accuracy, as claimed.** With the new indicator the three-point scheme is
fifth order in smooth regions, measured on linear advection (orders
4.95–5.07 from 40 to 320 points). From an expansion of the indicator where
the first derivative of the flux vanishes (eq. 3.9) the paper also claims fifth order at critical points.
That claim is the paper's own; no test isolates a critical point, and no
ingested source of this bundle re-tests it or states otherwise. The
convergence theorem for smooth solutions proves only the stencil-size
rate (third order for three-point stencils), not the fifth order of the
design (§6, eq. 6.5).

## Finite-difference against finite-volume form

* **FD-WENO (Jiang–Shu).** The unknowns are point values. The scheme
  reconstructs a numerical flux from point values of the *flux*, through
  the flux primitive whose cell averages are the point fluxes
  (eqs. 2.2–2.3), after a flux splitting. One-dimensional stencils are
  applied direction by direction.
  [Jiang & Wu (1999)](/sources/jiang-1999.md) require a uniform or
  smoothly varying grid for third and higher order.

  **Origin of the flux form.** The point-value flux framework is Shu &
  Osher's. The 1988 paper builds the numerical flux by ENO interpolation
  of each split flux plus fixed Taylor corrections in even derivatives,
  which make the conservative difference of order $2m$ on $2m+1$ points
  ([Shu & Osher (1988)](/sources/shu-osher-1988.md), eqs. 3.5–3.9); it
  introduces no flux primitive. The flux primitive, the primitive of an
  implicit function whose cell averages are the point fluxes, is Lemma 2.1
  of the 1989 sequel, with divided differences taken directly from those
  of the flux ([Shu & Osher (1989)](/sources/shu-osher-1989.md),
  eqs. 2.1–2.5). The two are equivalent in accuracy; the flux-primitive
  form is the one Jiang & Shu restate (eqs. 2.2–2.3). Point-value and
  cell-average ENO coincide for linear 1D equations only (1989, p. 36).
  The stencil must start on the upwind side: a downwind start is unstable
  for Burgers even with ENO selection up to third order (1989, p. 36).
* **FV-WENO.** The unknowns are cell averages; the same weighting is
  applied to reconstruct interface values of the *state* from cell
  averages, and the fluxes come from Riemann solvers. This form is what
  [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
  couples to ([Balsara (2004)](/sources/balsara-2004.md),
  [Balsara (2009)](/sources/balsara-2009.md),
  [Ding & Wu (2024)](/sources/ding-2024.md)). Jiang & Shu do not present
  it.
* **Alternative-FD WENO.** Point-value unknowns with interpolation of
  states rather than of the flux primitive
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md)), which find
  FD-WENO 7 to 14 times faster than FV-WENO in 2D and 5 to 12 times in 3D.
* **Point-value reconstruction from cell-centre point values**, inside a
  fourth-order FV scheme ([Berta et al. (2024)](/sources/berta-2024.md)).
  Its point-value optimal weights for WENO-Z, $(1/16, 5/8, 5/16)$, differ
  from the $(1/10, 6/10, 3/10)$ above because the target differs; this is
  an extension, not a disagreement.

## Systems and splitting

Jiang & Shu compute fluxes in local characteristic fields of the
interface Jacobian, evaluated at the arithmetic mean of the two adjacent
states (or Roe's matrix for Euler), with the weights computed field by
field, then project back (§4, eqs. 4.1–4.4). The projections dominate the
cost. The splitting tested is **global** Lax–Friedrichs, with
$\alpha^{\mathrm{LF}}$ the maximum wave speed over the whole range, per
direction (eq. 2.5); local splitting is allowed in words but not tested.
A cheaper variant takes the weights from pressure and entropy; it fails
at reflective walls, where those variables cannot see jumps in the normal
velocity, and the density goes negative (§8.3).

**Splittings in the ENO lineage.** The 1988 Shu–Osher scheme uses global
Lax–Friedrichs splitting, one constant $\alpha^{\mathrm{LF}}$ bounding the
characteristic speed, and for systems a frozen-state matrix built from
bounds on $|\lambda_k|$ ([Shu & Osher (1988)](/sources/shu-osher-1988.md),
eq. 3.1, p. 22). The 1989 paper adds three variants that keep high order
at sonic points ([Shu & Osher (1989)](/sources/shu-osher-1989.md),
Algs. 2.1–2.3):
* **ENO-Roe**: the stencil starts on the side given by the sign of the
  Roe speed; one divided-difference table, half the cost; it admits
  entropy-violating expansion shocks;
* **ENO-LLF**: local Lax–Friedrichs splitting, with $\alpha^{\mathrm{LF}}$
  per interface the maximum of the characteristic speed between the two
  adjacent states (eq. 2.12), and for systems the maximum of $|\lambda_k|$
  at the two states, field by field (eqs. 4.3–4.4);
* **ENO-RF**: ENO-Roe where the characteristic speed keeps its sign
  across the interface, ENO-LLF where it changes sign. Observed, not
  proved, to give the entropy solution even for nonconvex fluxes (p. 40);
  the authors' preferred scheme (§VI).

Numerical viscosity, hence shock smearing, decreases from global LF to
LLF to Roe (Remark 2.2d). The local characteristic decomposition at the
arithmetic-mean or Roe-averaged state that Jiang & Shu use is Algorithm 4.1
of the same paper. The "RF" splitting that Jiang & Shu reference to Shu &
Osher is this ENO-RF construction.

**Time integration.** The third-order TVD Runge–Kutta of Shu & Osher,
later called SSP-RK3, and the classical fourth-order RK, which is not TVD
(eqs. 1.3–1.4). Linear-stability CFL numbers for three-point stencils: 1.434 (RK3),
1.731 (RK4) (Table 5).

**Origin and TVD status of the integrators.** The third-order scheme is
eq. 2.18 of [Shu & Osher (1988)](/sources/shu-osher-1988.md), TVD under
the forward-Euler CFL limit times a coefficient of 1; the 1989 paper only
re-lists it (Table I). Classical RK4 is TVD there too, at coefficient
$\frac23$, but only if a downwinded spatial operator replaces the plain one
at the stages with negative weights (eq. 2.20); used with the plain
operator, as Jiang & Shu use it, it is not TVD. The TVD coefficient and
the linear-stability limits above are different quantities
([SSP Runge–Kutta methods](/methods/ssp-runge-kutta.md)).

## Uses and variants in this bundle

* **The MHD extension.** [Jiang & Wu (1999)](/sources/jiang-1999.md) keep
  the Jiang–Shu ingredients as their paper states them: point-value
  fluxes, characteristic decomposition at the arithmetic-mean state,
  global LF splitting, the WENO-JS weights with constant $10^{-6}$, RK4.
  Their CFL 0.8 for MHD is their own choice. Jiang & Shu's Euler runs use
  CFL 0.6 (Figs. 4, 7, 10–13) or $\Delta t = 0.6\Delta x$ (Figs. 5–6
  and the 2D tests of §8.3); 0.8 appears only on the scalar
  Buckley–Leverett figure (Fig. 3, §8.1 Ex. 2). Jiang & Wu's page
  records no power.
* **Local LF splitting** in HOW-MHD's fifth-order FD-WENO
  ([Seo & Ryu (2023)](/sources/seo-2023.md)) is that code's choice; the
  scheme is attributed to Jiang & Shu and Jiang & Wu there, but Jiang &
  Shu test only global splitting.
  **Origin of local splitting.** Local Lax–Friedrichs splitting in the
  point-value flux ENO framework predates HOW-MHD: it is ENO-LLF of
  [Shu & Osher (1989)](/sources/shu-osher-1989.md) (Alg. 2.2, eq. 2.12;
  for systems eqs. 4.3–4.4). HOW-MHD's choice is to use it inside
  Jiang–Shu WENO, which Jiang & Shu allow in words but do not test.
* **Other weights and indicators.** WENO-Z and WENO+3 in PLUTO
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md);
  [Berta et al. (2024)](/sources/berta-2024.md), with a WENO3 fallback);
  Borges indicators in Flash-X's Spark
  ([Couch et al. (2021)](/sources/couch-2021.md)); WENO-3 to WENO-9 and
  TENO-5 in ALPACA ([Hoppe et al. (2022)](/sources/hoppe-2022.md)).
  WENO-Z and WENO3 are variants of the WENO-JS weighting.
* **MP5**, used alongside them in PLUTO
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md);
  [Berta et al. (2024)](/sources/berta-2024.md)), is not a WENO variant:
  it is a limiter-based alternative (monotonicity-preserving bounds on a
  fifth-order linear interpolant).
* **Hamilton–Jacobi WENO** for the vector potential, with weights on
  derivatives of the potential so that the field is limited
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md);
  [vector-potential evolution](/methods/vector-potential-evolution.md)).
* **WENO finite differences with LF splitting and SSP-RK3** in ADAM
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md);
  [ADAM](/software/adam.md)).

## Role in divergence-preserving schemes

WENO is **constraint-agnostic**. Collocated FD-WENO evolves cell-centred
point values of $B_h$ and holds no $D_h B_h = 0$ invariant. Every MHD
source of this bundle that uses it adds a divergence mechanism:
* a Poisson [projection](/methods/projection-method.md), found necessary
  for stability ([Jiang & Wu (1999)](/sources/jiang-1999.md));
* [GLM cleaning](/methods/glm-divergence-cleaning.md)
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md);
  [Zaghi (2026)](/sources/zaghi-2026.md));
* high-order staggered [CT](/methods/constrained-transport.md), whose
  second-order version caps a fifth-order WENO code at second order
  ([Seo & Ryu (2023)](/sources/seo-2023.md));
* unstaggered CT through a potential
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md));
* [UCT](/methods/upwind-constrained-transport.md) and
  [divergence-free reconstruction](/methods/divergence-free-reconstruction.md),
  where WENO reconstructs face and edge data inside a scheme that holds the
  invariant on its own stencil
  ([Balsara (2009)](/sources/balsara-2009.md);
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md)).

The pressure-positivity loss of uncontrolled FD-WENO MHD on Orszag–Tang
([positivity–divergence coupling](/results/positivity-divergence-coupling.md))
is an MHD finding of Jiang & Wu. The only positivity failure in Jiang &
Shu is hydrodynamic and comes from the pressure/entropy weights at
reflective walls; it has no divergence content.

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-shu-1996.md), §§1–4, 6, 8, eqs. 1.3–1.4, 2.2–2.17, 2.26–2.28, 3.1–3.9, 4.1–4.4, Tables 2–3, 5.
2. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1–2, 3.4, 4.
3. [Seo & Ryu (2023)](/sources/seo-2023.md), §§1–2.
4. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md), §1.
5. [Berta et al. (2024)](/sources/berta-2024.md), §3.
6. [Couch et al. (2021)](/sources/couch-2021.md).
7. [Hoppe et al. (2022)](/sources/hoppe-2022.md), §4, Table 2.
8. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §§3, 5.1.
9. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1.
10. [Zaghi (2026)](/sources/zaghi-2026.md).
11. [Balsara (2004)](/sources/balsara-2004.md), §§3–4.
12. [Balsara (2009)](/sources/balsara-2009.md), §§2–4.
13. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–3, 7.4.
14. [Ding & Wu (2024)](/sources/ding-2024.md), §2.3.
15. [Shu & Osher (1988)](/sources/shu-osher-1988.md), §§II–III, eqs. 2.18, 2.20, 3.1, 3.5–3.9, p. 22 (read as ICASE Report 87-33).
16. [Shu & Osher (1989)](/sources/shu-osher-1989.md), §§I–II, IV, VI, Lemma 2.1, Algs. 2.1–2.3, 4.1, eqs. 2.12, 4.3–4.4, Table I.
