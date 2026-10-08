---
type: Method
title: "Reconstruction from cell averages"
description: "Recovering point values (or polynomials) of $k$-th order accuracy from cell averages via interpolation of the primitive function; the building block of finite-volume ENO/WENO/PPM schemes."
status: established
aliases: [reconstruction via primitive function, finite-volume reconstruction]
tags: [reconstruction, finite-volume]
timestamp: 2026-10-08T00:00:00Z
---

# Reconstruction from cell averages

**The problem** ([Shu (1998)](/sources/shu-1998.md), Problem 2.1): given
cell averages $\bar u_i$, find in each cell a polynomial $p_i$ of degree
at most $k-1$ with $p_i(x) = u(x) + O(h^k)$ in $I_i$. The interface values
$u^-_{i+1/2} = p_i(x_{i+1/2})$ and $u^+_{i-1/2} = p_i(x_{i-1/2})$ are then
$k$-th order accurate.

**Via the primitive** ([Harten et al. (1987)](/sources/harten-1987.md),
"RP"). The primitive $\mathcal{U}$ is known exactly at interfaces from
the averages. Interpolate it at the $k+1$ interface points of a
$k$-cell stencil by a polynomial $P$ of degree $k$ and set $p = P'$.
Then $p$ reproduces every cell average in the stencil, and
$p = u + O(h^k)$ where $u$ is smooth there. The procedure needs no
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
(back substitution) recovers $u$ and its derivatives to $O(h^k)$.

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
quadrature point. [Shu (1998)](/sources/shu-1998.md) (§3.3) concludes
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

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1, 3 and Appendix.
2. [Shu (1998)](/sources/shu-1998.md), §§2.1.1, 2.3.1, 3.1.1, 3.3.1.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §§2–3.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §I.
5. [Titarev & Toro (2004)](/sources/titarev-2004.md), §§2–3, 5.5 (eqs. 9–12 and 24–31 read from the page images).
6. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §I.
7. [Reyes et al. (2018)](/sources/reyes-2018.md), §2.3.
8. [Zhang & Shu (2012)](/sources/zhang-2012.md), §2.1.
