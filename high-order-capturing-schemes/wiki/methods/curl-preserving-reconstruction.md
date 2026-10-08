---
type: Method
title: "Edge-centred curl-preserving (ECCP) reconstruction and schemes"
description: "The curl analogue of constrained transport: a vector field that must stay curl-free (or keep its curl tied to a divergence-free field) lives on mesh edges, a potential lives at vertices and is upwinded by a multidimensional Riemann solver, and closed-form reconstructions built from 1D WENO edge moments keep the curl exactly; orders 1–4 in 2D and 1–3 in 3D."
status: established
aliases: [ECCP, curl-free reconstruction, curl constraint-preserving reconstruction, mimetic curl-preserving scheme]
tags: [involution, reconstruction, staggered, multidimensional-riemann-solver, weno]
timestamp: 2026-10-08T00:00:00Z
---

# Edge-centred curl-preserving reconstruction and schemes

**Involution and collocation** ([Balsara et al. (2023)](/sources/balsara-2023.md), §§1–1.1).
Several hyperbolic systems carry a field $\mathbf J$ whose evolution
includes $\partial_t\mathbf J + \nabla(\ldots) + \ldots = 0$, with a
gradient term that keeps $\nabla\times\mathbf J$ zero, or tied to the
divergence-free field $\boldsymbol\Omega = \nabla\times\mathbf J$. Examples
are the Godunov–Peshkov–Romenski model of heat conduction,
hyperelasticity, first-order formulations of relativity, and a
hyperbolic Schrödinger system. The circulation of $\mathbf J$ around
every mesh face stays zero only if the components of $\mathbf J$ sit on
the mesh edges and the potential under the gradient sits at the vertices,
with a multidimensionally upwinded value there. This is the dual of the
face/edge placement of [constrained transport](/methods/constrained-transport.md).

**Reconstruction** (§§2–3). A component-wise reconstruction from edge
values fails: independent edge slopes leave a curl with linear terms
(eqs. 3–6). Adding terms that vanish on the edges, $(1 - 4y^2)$ in $J_x$
and $(1 - 4x^2)$ in $J_y$ at second order, with coefficients fixed by the
constraint, restores an exactly curl-free field. Curl-free and
curl-preserving reconstruction differ only in the target curl (eqs. 7–11).
* The edge moments come from 1D TVD or WENO reconstruction along each
  edge, so the multidimensional field inherits the nonlinear limiting of
  Godunov schemes (§2.2).
* Modes that exist only to satisfy the constraint are part of the field,
  as in [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
  (§2.3).
* At fourth order, edge data no longer suffice: some modes must be
  zone-centred. Five parameters are left free and are fixed by least
  squares against a standard zone-centred WENO reconstruction, whose
  averages depend only on edge data (§2.4, eqs. 16–23).
* In 3D, five of a zone's six face circulations are independent. The
  face circulations are reconstructed by 2D WENO, and the curl is matched
  to a divergence-free reconstruction of $\boldsymbol\Omega$, so curl
  reconstruction contains divergence-free reconstruction as a sub-step
  (§§3.1–3.3).

**Upwinding and stability** (§§2.5, 3.4, 4). At first order, an LLF
multidimensional Riemann solver for the vertex potential turns the edge
update into a centred difference plus $\frac{|v_d|}{2h_d}$ times a
second difference in each direction. That is a properly upwinded scheme
on an edge-centred control volume (eqs. 31–32, 63–64;
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
The paper concludes from this that higher-order versions will be stable;
that is an argument, not a proof. A 2D von Neumann analysis gives maximum
Courant numbers:

| order | 2 | 3 | 4 |
|---|---|---|---|
| time integrator | SSP-RK2 | SSP-RK3 | SSP-RK(5,4) |
| largest stable $\nu$ | 0.7071 | 1.1507 | 1.3040 |

Third order improves phase errors strongly but damps only about as much
as second order, which the authors attribute to SSP-RK3. Fourth order
cuts both dissipation and dispersion errors by about an order of
magnitude at 10 or more cells per wavelength
([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

**Results** (§§5–6).
* A stationary curl-free equilibrium on $[-5, 5]^2$ converges at the
  design order. Its curl error stays at machine precision to $t = 50$, and
  the quadratic energy decays least at fourth order. A second-order
  vertex-staggered competitor dissipates most. Without a curl-preserving
  scheme the equilibrium breaks up and the code eventually fails.
* With a curl source, a zone-centred third-order Godunov scheme with a
  finite-differenced curl has curl errors 2–4 orders of magnitude larger.
* On a heat-conducting blast, the curl of $\mathbf J$ is controlled by the
  relaxation source under ECCP and grows with discretization error under
  the zone-centred scheme.

**Against alternatives** (§5). GLM curl cleaning needs fast cleaning
speeds and many extra fields ([hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
A semi-implicit vertex-staggered scheme is exactly curl-free but second
order and interpolates often, which complicates AMR. ECCP keeps one
control volume for all variables.

# Citations

1. [Balsara et al. (2023)](/sources/balsara-2023.md), §§1–7 (eqs. 3–11, 26–27, 31–32, 61–64 and Table 1 read from the page images).
