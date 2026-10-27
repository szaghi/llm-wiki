---
type: Property
title: "Geometric conservation law and free-stream preservation"
description: "On curvilinear grids a discretization preserves a uniform flow only if its discrete metric terms satisfy the metric identities; the sources obtain this geometric conservation law with curl-form metrics in DGSEM codes and with a symmetric conservative metric form in a curvilinear gas-kinetic finite-volume scheme."
status: established
aliases: [GCL, geometric conservation law, free-stream preservation, freestream preservation, metric identities, discrete metric identities]
tags: [dg, gas-kinetic, high-order, compressible]
timestamp: 2026-10-26T20:44:00Z
---

# Geometric conservation law and free-stream preservation

When a conservation law $\partial_tU+\nabla\cdot F=0$ is solved on a
curvilinear grid, each element or cell is the image of a reference
(computational) element under a map $\boldsymbol x(\boldsymbol\xi)$ with
Jacobian determinant $\mathcal J$ (page-local), and the equation is
transformed to
$$\mathcal J\,\partial_tU+\sum_{i=1}^{3}\frac{\partial}{\partial\xi^i}\big(\mathcal J\boldsymbol a^i\cdot F\big)=0,$$
with $\mathcal J\boldsymbol a^i$ the contravariant (metric) vectors (Krais et
al. 2021, §3.1, Eqs. 5–7; [Kurz et al. 2025](/sources/kurz-2025.md), §2.2,
Eqs. 11–13; page-local symbols, the registry's $\xi$, $\xi_i$ are reference
coordinates and nodes). A uniform state $U=\mathrm{const}$ has a constant
physical flux, so it remains a solution of the transformed equation only if
$$\sum_{i=1}^{3}\frac{\partial(\mathcal J a^i_n)}{\partial\xi^i}=0,\qquad n=1,2,3,$$
the **metric identities** *(compiler check, not in the sources: with $F$
constant the flux term reduces to $\sum_n F_n\sum_i\partial(\mathcal J a^i_n)/\partial\xi^i$;
the sources state only the requirement)*. A discretization in which the discrete metric terms
satisfy the discrete version of these identities is **free-stream
preserving**; the requirement is called the **geometric conservation law
(GCL)**. The sources below meet it in high-order
[LES](/definitions/large-eddy-simulation.md) and
[DNS](/definitions/direct-numerical-simulation.md) codes on curved and
stretched grids.

## DGSEM: curl-form metric terms

For the [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md),
[Krais et al. (2021)](/sources/krais-2021.md), §3.1, Eq. (4), compute the
metric terms in the **curl form**
$$\mathcal J a^i_n=-\hat{\boldsymbol x}_i\cdot\nabla_\xi\times\big(x_l\nabla_\xi x_m\big),\qquad i,n=1,2,3,\quad (n,m,l)\ \text{cyclic},$$
($\hat{\boldsymbol x}_i$ the Cartesian unit vector, page-local) and state,
citing Kopriva, that it satisfies the metric identities discretely, which
free-stream preservation on curved meshes requires. The same curl form is
Eq. (11) of the GPU code [GALÆXI](/software/galaexi.md) (Kurz et al. 2025,
§2.2), which keeps [FLEXI](/software/flexi.md)'s discretization.
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §3, use the
conservative Kopriva form for the same reason, and
[Morsbach et al. (2024)](/sources/morsbach-2024.md), §2, obtain free-stream
preservation in DLR's TRACE DGSEM by mapping the equations to the reference
element following Kopriva and Gassner (2016).

## Finite volumes from discrete grid points: the curvilinear gas-kinetic scheme

[Cao et al. (2024)](/sources/cao-2024.md) extend the
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md) to
meshes given only by discrete points (HGKS-cur). Their metric terms are the
Jacobian-scaled cofactors of the map, e.g. for the first computational
direction (§2.1, Eq. 5; $(\xi,\eta,\zeta)$ the computational coordinates,
page-local, not the Kolmogorov length or input features; subscripts
derivatives; the hat marks a metric term, not the test filter)
$$\hat\xi_x=y_\eta z_\zeta-z_\eta y_\zeta,\qquad \hat\xi_y=z_\eta x_\zeta-x_\eta z_\zeta,\qquad \hat\xi_z=x_\eta y_\zeta-y_\eta x_\zeta,$$
and cyclically for $\eta$ and $\zeta$. To satisfy the GCL they (§2.3):

1. compute the grid derivatives at the grid points with fourth-order central
   differences, e.g.
   $(\boldsymbol x_\xi)_{ijk}=\frac{1}{12\Delta\xi}\big[8(\boldsymbol x_{i+1,j,k}-\boldsymbol x_{i-1,j,k})-(\boldsymbol x_{i+2,j,k}-\boldsymbol x_{i-2,j,k})\big]$
   (Eq. 10);
2. evaluate the metric terms in a **symmetric conservative form**, a
   half-sum of derivatives of products of coordinates and grid derivatives
   (Eq. 11, "to preserve the GCL", citing Deng et al. 2011 and Xu et al.
   2016);
3. interpolate them dimension by dimension to the two Gauss points of each
   face with cubic Lagrange formulae;
4. reconstruct, with fifth-order [WENO](/methods/weno-scheme.md) in
   computational space, the cell-integrated Jacobian and the
   Jacobian-weighted conservative variables, and recover point values as
   $Q=(\mathcal JQ)/\mathcal J$ ($Q$ the conservative variables,
   page-local).

**Test.** A uniform state $\rho=p=u=v=w=1$ on two sinusoidally perturbed
meshes of $10^3$ to $160^3$ cells keeps $L^1$ errors at $O(10^{-15})$ to
$O(10^{-14})$ (6.2119E-15 at $10^3$ to 4.6088E-14 at $160^3$ on mesh 1),
"machine zero", so "the geometric conservation law is well preserved"
(§3.1, Table 3). The same meshes give fourth- to fifth-order convergence for
an advected density wave (orders 4.03 to 4.65, Tables 1–2). The scheme is
then used as [implicit LES](/definitions/implicit-les.md) of a compressible
[channel](/benchmarks/turbulent-channel-flow.md) and of a
[periodic hill](/benchmarks/periodic-hill.md) whose mesh is built from
discrete bottom-wall points (§3.3–3.4).

## Qualifications

- **Printed metric formula (Cao et al. 2024, arXiv v1, Eq. 11).** The
  printed $\hat\xi_x=\tfrac12\big((zy_\eta)_\zeta-(yz_\eta)_\zeta+(zy_\zeta)_\eta-(yz_\zeta)_\eta\big)$
  expands to $z\,y_{\eta\zeta}-y\,z_{\eta\zeta}$, not to the cofactor
  $y_\eta z_\zeta-z_\eta y_\zeta$ of Eq. (5); the combination
  $\tfrac12\big((zy_\eta)_\zeta-(zy_\zeta)_\eta+(yz_\zeta)_\eta-(yz_\eta)_\zeta\big)$
  does reproduce it *(compiler check, not in the sources)*. In the printed
  $\hat\xi_y$ the last two terms are identical and cancel, and $\hat\xi_z$
  has the printed structure of $\hat\xi_x$. The free-stream test of Table 3
  shows that the code preserves the GCL; the version of record may print
  the formula differently.
- The DGSEM sources state free-stream preservation as a property of their
  metric evaluation (Krais et al. 2021; Kurz et al. 2025) and show no
  free-stream test on curved meshes (Krais et al.'s free-stream runs are
  Cartesian scaling tests, §5.8); Cao et al. (2024) test it.

# Citations

- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv 2107.08609v1: §2.1, Eqs. (3)–(6) (transformed BGK equation, metric terms, Jacobian-weighted variables); §2.3, Eqs. (10)–(11) (metric evaluation from discrete points, symmetric conservative form, Gauss-point interpolation, WENO in computational space); §3.1, Tables 1–3 (accuracy, free-stream preservation); §3.3–3.4.
- [Krais et al. (2021)](/sources/krais-2021.md) — §3.1, Eqs. (4)–(7) (curl-form metric terms, metric identities, free-stream preservation).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv 2404.12703v2: §2.2, Eqs. (11)–(13) (curl-form metric terms in GALÆXI).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §3 (conservative Kopriva form of the metric terms).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2 (free-stream preservation in the TRACE DGSEM).
