---
type: Method
title: "Reconstruction from cell averages"
description: "Recovering point values (or polynomials) of $r$-th order accuracy from the cell averages of an $r$-cell stencil via interpolation of the primitive function; the building block of finite-volume ENO/WENO/PPM schemes."
status: established
aliases: [reconstruction via primitive function, finite-volume reconstruction]
tags: [reconstruction, finite-volume]
timestamp: 2026-10-13T00:00:00Z
---

# Reconstruction from cell averages

**The problem** ([Shu (1998)](/sources/shu-1998.md), Problem 2.1): given
cell averages $\bar u_i$, find in each cell a polynomial $\mathcal P_i$
of degree at most $K = r-1$ with $\mathcal P_i(x) = u(x) + O(h^r)$ in
$I_i$. The interface values $u^-_{i+1/2} = \mathcal P_i(x_{i+1/2})$ and
$u^+_{i-1/2} = \mathcal P_i(x_{i-1/2})$ are then $r$-th order accurate.

**Via the primitive** ([Harten et al. (1987)](/sources/harten-1987.md),
"RP"). The primitive $\mathcal{U}$ is known exactly at interfaces from
the averages. Interpolate it at the $r+1$ interface points of an
$r$-cell stencil by a polynomial of degree $r$ and take its derivative
as $\mathcal P_i$. Then $\mathcal P_i$ reproduces every cell average in
the stencil, and $\mathcal P_i = u + O(h^r)$ where $u$ is smooth there. The procedure needs no
uniform grid. Because the map from averages to interface values is
linear, each stencil position relative to $x_{i+1/2}$ gives fixed
constants that express $u_{i+1/2}$ as a linear combination of the
stencil's averages; they depend on the local spacings but not on the
data, and are tabulated for uniform grids up to seventh order
([Shu (1998)](/sources/shu-1998.md), Table 2.1).

**Via deconvolution** ([Harten et al. (1987)](/sources/harten-1987.md),
"RD"). On a uniform grid the averages are point values of the sliding
average of $u$. Taylor-expanding the sliding average gives a triangular,
diagonally dominant linear system between derivatives of the averaged
function and of $u$. Interpolating the averages and inverting the system
(back substitution) recovers $u$ and its derivatives to $O(h^r)$.

**Adaptive stencils.** Fixed-stencil reconstruction of degree two or
higher oscillates at discontinuities, with an $O(1)$ Gibbs-like
overshoot that does not decay with refinement
([Shu (1998)](/sources/shu-1998.md), Fig. 2.1). The stencil is therefore
chosen adaptively ([ENO](/methods/eno-reconstruction.md)) or the
candidate reconstructions are blended ([WENO](/methods/weno.md),
[central WENO](/methods/central-weno.md)), or a higher-order value is
limited ([PPM](/methods/ppm.md),
[monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).

## In a finite-volume scheme

The semi-discrete scheme is
$\frac{d}{dt}\bar u_i = -\frac{1}{h_i}\left(\hat f_{i+1/2} - \hat f_{i-1/2}\right)$
with $\hat f_{i+1/2} = \hat f(u^-_{i+1/2}, u^+_{i+1/2})$ a
[monotone flux](/definitions/monotone-flux.md) or a Riemann solver
([Shu (1998)](/sources/shu-1998.md), §2.3.1). It applies on arbitrary
meshes ([Liu, Osher & Chan (1994)](/sources/liu-1994.md) use this form
for WENO).

**Multi-D cost.** On Cartesian grids, the reconstruction uses tensor
products: two successive one-dimensional reconstructions per point in 2D
($n$ in $n$ dimensions). Above second order the face fluxes also need
Gaussian quadrature, and for WENO the linear weights differ at each
quadrature point. At fourth order there is an alternative: one flux
evaluation at the face centre plus a transverse-Laplacian correction
([fourth-order finite volume](/methods/fourth-order-finite-volume.md);
[McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §2.2). [Shu (1998)](/sources/shu-1998.md) (§3.3) concludes
that multi-D finite-volume schemes above second order are rarely used,
and that the finite-difference version costs about a factor of four less
in 2D ([conservative finite difference](/methods/conservative-finite-difference.md)).
[Balsara & Shu (2000)](/sources/balsara-2000.md) give the same cost
argument against high-order finite-volume ENO.

**Three dimensions, dimension by dimension** ([Titarev & Toro (2004)](/sources/titarev-2004.md), §3;
weights checked on the page images). Each face flux is a tensor
$N$-point Gauss rule over Riemann solutions at the face Gauss points
([approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
Values there come from three 1D WENO sweeps: normal to the face, to get
face averages; then along $y$, to get line averages at the Gauss
abscissae; then along $z$, to get point values. The second and third
sweeps need linear weights for the Gauss points
$x_i \pm h/(2\sqrt3)$, which had not been published. For $r = 3$ at
$x_i - h/(2\sqrt3)$, with the candidates on cells $\{i, i+1, i+2\}$,
$\{i-1, i, i+1\}$ and $\{i-2, i-1, i\}$, they are
$$\tfrac{210 - \sqrt3}{1080},\quad \tfrac{11}{18},\quad \tfrac{210 + \sqrt3}{1080},$$
mirrored at the other point. All are positive, so no negative-weight
treatment is needed here, unlike other target points. Weights for
$r = 4$ are given too; the nonlinear weights are computed separately at
each point. The two-point (fourth-order) rule gave the best
accuracy/cost for $r = 3, 4$, and convergence still exceeded fourth
order on the vortex test ([isentropic vortex](/benchmarks/isentropic-vortex.md)).
Reconstruction is always in characteristic variables. If two close
discontinuities leave no smooth stencil, the scheme lowers $r$ until the
interface density and pressure stay within 90% of the cell values,
ending at a minmod-limited MUSCL slope (adapted from Harten et al.).
In 2D the FV scheme costs about the same as Shi–Hu–Shu's; FV-WENO is
about three times slower than FD-WENO in 2D, but it works on
unstructured meshes and, with MUSTA, without eigenvectors (§5.5).

**Reconstruction versus interpolation** ([Balsara et al. (2025)](/sources/balsara-2025.md), §I).
Interpolation matches point values on the stencil; reconstruction
matches cell averages. On the same stencil they give polynomials of the
same degree with different coefficients, while linear weights,
indicators and normalization carry over. Interpolation is the basis of
[AFD-WENO](/methods/alternative-finite-difference-weno.md).
Non-polynomial reconstructions from averages are also possible:
[Gaussian-process reconstruction](/methods/gp-weno.md) integrates a
covariance kernel over the cells ([Reyes et al. (2018)](/sources/reyes-2018.md), §2.3).
For positivity limiting, FV-WENO, which delivers only point values, must
supply a polynomial with the right mean — for fifth order the degree-four
interpolant of the two interface values and three neighbouring means
([Zhang & Shu (2012)](/sources/zhang-2012.md), §2.1;
[scaling limiter](/methods/positivity-preserving-scaling-limiter.md)).

**Entire polynomials and unstructured meshes** ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §2). A
high-order reconstruction on triangles or tetrahedra maps every stencil
cell to the reference element of the target cell. The Jacobians cancel
from the conservation equations, which avoids the ill-conditioning of
physical-space reconstruction noted by Abgrall. The basis is a
hierarchical orthogonal one, as in DG. Stencils carry 50–100% more cells
than unknowns and are solved by constrained least squares that conserve
exactly in the target cell, a choice made for robustness on general
meshes. The output is the whole polynomial, not point values at face
quadrature points, which is what [ADER](/methods/ader.md) needs
([polynomial WENO](/methods/polynomial-weno.md)). On Cartesian meshes the
same object is built modally: Legendre moments along each axis come
from 1D reconstructions, and the cross moments of finite-volume
reconstruction (absent from pointwise WENO) come from small diagonal
stencils ([Balsara et al. (2009)](/sources/balsara-2009.md), §2). Subcell averages of a DG polynomial and their
inverse, the subcell reconstruction $\mathcal{R}$, are the same
recovery problem ([a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)).

**Later uses (batch 5).** Fourth-order finite volume can be built from
two identities instead of quadrature. Point values and cell averages
differ by $\frac{h^2}{24}\Delta_h$, and face averages and face centres by
$\frac{h^2}{24}\Delta^\perp_h$. A product rule handles nonlinear
functions of averaged data. Applying each correction to a lower-order
argument keeps the stencil small at an $O(h^4)$ cost
([fourth-order finite volume](/methods/fourth-order-finite-volume.md);
[McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §2.2;
[Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §3). Coarse-to-fine
AMR interpolation uses a constrained least-squares cubic that matches the
coarse average exactly and the neighbouring averages in the
least-squares sense, the same device as polynomial WENO's constrained
reconstruction ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §3.2;
[high-order AMR](/methods/high-order-amr.md)).

**Later uses (batch 6).**
* *Interpolation inside finite volume.* After the $\frac{h^2}{24}$
  deconvolution, point values can be interpolated to faces with
  finite-difference formulas and point-value linear weights:
  $\tfrac1{16}, \tfrac58, \tfrac5{16}$ for fifth order and $\tfrac34, \tfrac14$
  for third, against $\tfrac1{10}, \tfrac6{10}, \tfrac3{10}$ and $\tfrac23, \tfrac13$
  from averages ([Berta et al. (2024)](/sources/berta-2024.md), §3.2;
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md)).
  Two-point Gauss quadrature would need 4 Riemann problems per 3D face.
* *Flexibility and cost.* FV reconstruction needs no uniform or smooth
  mesh, since coefficients and weights become local constants
  ([Shu (2009)](/sources/shu-2009.md), §2.3.2). In 2D it costs two to five times the FD scheme above
  second order, a range that refines Shu's 1998 factor of four
  ([Shu (2009)](/sources/shu-2009.md), §3.4; [conservative finite difference](/methods/conservative-finite-difference.md)).
  On unstructured meshes the optimal weights depend on the local mesh and
  can be negative ([negative linear weights](/methods/negative-linear-weights.md)).
* *Gauss–Lobatto edge nodes.* Fifth-order 2D FV-WENO uses 4-point
  Gauss–Lobatto nodes instead of 3-point Gauss, because the latter gives a
  negative linear weight at the midpoint (Shi, Hu & Shu). The same nodes
  serve the positivity limiter ([Ding & Wu (2024)](/sources/ding-2024.md), §2.2.2).
* *Constrained vector reconstruction.* Magnetic fields can be rebuilt from
  face moments under a divergence constraint
  ([divergence-free reconstruction](/methods/divergence-free-reconstruction.md)),
  and curl-constrained fields from edge moments, with zone-centred WENO
  only as least-squares targets at fourth order
  ([curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md)).

**Later uses (batch 14).** *The origin of second-order reconstruction*
([van Leer (1979)](/sources/vanleer-1979.md); [MUSCL](/methods/muscl.md)).
* *Stored slopes.* Van Leer's cells carry $\mathcal P_i = \bar u_i + \hat u^{(1)}_i\zeta$,
  the $K = 1$ case of the problem above, but the slope is "independent of
  the slab averages; [it] can not be derived from the latter and must be
  stored separately" (§2.2, eqs. 39–41, p. 107). The cell thus holds its
  first Legendre moment as an unknown, as the modal and DG polynomials of
  the "entire polynomials" paragraph do, rather than recovering it from
  neighbours. With every slope zero the scheme is Godunov's, "This
  accounts for the first-order accuracy of Godunov's scheme" (p. 107).
* *Three ways to get the slope* (App. B). Central differencing of the
  averages, $\hat u^{(1)}_i = \tfrac12(\bar u_{i+1} - \bar u_{i-1})$
  (eq. B1); differencing of the two interface values after a step (used in
  MUSCL's Lagrangean step, eq. 51.5); and least-squares fitting of the
  zeroth and first moments (used in its remap). By the linear analysis
  quoted there, moment fitting is "vastly superior", with a convective
  error smaller "by two orders" of the mesh size.
* *The limiters, as printed.* At the start of each Lagrangean step
  (§3.3, eq. 101)
  $$\hat u^{(1)}_i \leftarrow \operatorname{minmod}\left(2\Delta^1\bar u_{i-1},\ \hat u^{(1)}_i,\ 2\Delta^1\bar u_i\right),$$
  so the linear profile stays within the neighbouring averages and is flat
  at their extrema; with the B1 slope this is $\delta^{\mathrm{MC}}\bar u_i$.
  The harmonic-mean alternative is
  $\hat u^{(1)}_i = 2\Delta^1\bar u_{i-1}\Delta^1\bar u_i/(\Delta^1\bar u_{i-1} + \Delta^1\bar u_i)$
  when the two differences share a sign, else 0 (eq. B2). The factors 2 may
  be lowered, but not below 1 plus a term of the order of the data jump,
  "lest the scheme lose its second-order accuracy" (p. 118), and both limiters "clip real peaks to
  the same degree as a first-order method would do" (p. 119).
* *Time integration is part of the reconstruction step.* Van Leer reaches
  second order in time in one step: the characteristic equations at each
  interface discontinuity, with the cell slopes as space derivatives, give
  time-centred interface values (§§2.3–2.4, eqs. 64–90). This differs
  from the semi-discrete form above, where the reconstruction supplies
  only $u^\pm_{i+1/2}$ and a Runge–Kutta method supplies the time
  accuracy.

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1, 3 and Appendix.
2. [Shu (1998)](/sources/shu-1998.md), §§2.1.1, 2.3.1, 3.1.1, 3.3.1.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §§2–3.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §I.
5. [Titarev & Toro (2004)](/sources/titarev-2004.md), §§2–3, 5.5 (eqs. 9–12 and 24–31 read from the page images).
6. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §I.
7. [Reyes et al. (2018)](/sources/reyes-2018.md), §2.3.
8. [Zhang & Shu (2012)](/sources/zhang-2012.md), §2.1.
9. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §2.
10. [Balsara et al. (2009)](/sources/balsara-2009.md), §2.
11. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§2.2, 3.2.
12. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §3 (accepted manuscript).
13. [Berta et al. (2024)](/sources/berta-2024.md), §3.2 (arXiv v4).
14. [Ding & Wu (2024)](/sources/ding-2024.md), §2.2.2 (arXiv v1).
15. [Shu (2009)](/sources/shu-2009.md), §§2.3.2, 3.4.
16. [van Leer (1979)](/sources/vanleer-1979.md), §§2.2–2.4, 3.3, App. B.
