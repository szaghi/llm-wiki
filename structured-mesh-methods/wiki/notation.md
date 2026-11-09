---
type: Definition
title: "Notation registry"
description: "Normative symbol registry of the bundle: physical and curvilinear coordinates, the mapping and its Jacobian matrix, covariant and contravariant base vectors, the metric tensor, metric terms and metric identities, moving grids and the geometric conservation law, grid-generation operators and control functions, variational functionals, equidistribution and monitor functions, element Jacobians, targets and quality metrics, and the flow symbols; every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-11-08T20:53:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-11-08 from chunk 1, the founding papers:
Winslow (1966) on the inverse Laplace generator, Gordon and Hall (1973) on
transfinite interpolation, Thompson, Thames and Mastin (1974) on body-fitted
coordinates for multiply connected regions, Thomas and Lombard (1979) on the
geometric conservation law, Steger and Sorenson (1979) on boundary
clustering, Steger and Chaussee (1980) on hyperbolic generation, Brackbill
and Saltzman (1982) on variational adaptive zoning, the review of Thompson,
Warsi and Mastin (1982), Huang, Ren and Russell (1994) on moving mesh PDEs
and Knupp (2001) on algebraic quality metrics. The tensor symbols follow the
review of Thompson et al. (1982); the element symbols follow Knupp (2001).
Extend this registry, and log the extension, before writing a symbol it
lacks.

**Conventions that the sources split on, fixed here.** Physical coordinates
are $\mathbf x$ and curvilinear (computational, logical) coordinates
$\boldsymbol\xi$; in two dimensions $(x,y)$ and $(\xi,\eta)$, in three
$(\xi,\eta,\zeta)$. Gordon and Hall's parameters $(s,t)$ are written
$(\xi,\eta)$, since $t$ is time. Time is $t$ in both frames: a time
derivative at fixed curvilinear coordinates is written
$\partial_t|_{\boldsymbol\xi}$, never $\partial_\tau$, because $\tau$ is the
relaxation time of moving mesh PDEs. The Jacobian *determinant* is $J$ and
the Jacobian *matrix* $\mathsf A$; Thompson et al. write $\sqrt g$ for $J$.
The Winslow coefficients $\alpha,\beta,\gamma$ of the sources are the metric
components $g_{22}$, $g_{12}$, $g_{11}$. The order of accuracy is $r$ and the
polynomial degree $k$.

## Coordinates and the mapping

| symbol | meaning |
|---|---|
| $\mathbf x=(x_1,x_2,x_3)$; $(x,y)$ | physical (Cartesian) coordinates |
| $\boldsymbol\xi=(\xi^1,\xi^2,\xi^3)$; $(\xi,\eta,\zeta)$ | curvilinear (computational) coordinates; the computational domain is a unit square or cube, or a rectangle with unit spacing $\Delta\xi=1$ |
| $\Omega$, $\partial\Omega$; $\hat\Omega$ | physical domain and its boundary; computational (logical, reference) domain |
| $\mathbf x(\boldsymbol\xi,t)$ | the mapping (grid) from $\hat\Omega$ onto $\Omega$; a grid point is $\mathbf x_{\mathbf i}=\mathbf x(\boldsymbol\xi_{\mathbf i})$ with multi-index $\mathbf i=(i,j,k)$ |
| $d$ | space dimension |
| $\mathsf A=\partial\mathbf x/\partial\boldsymbol\xi$ | Jacobian matrix of the mapping (columns $\mathbf a_i$) |
| $J=\det\mathsf A$ | Jacobian determinant, the volume (area) element; $J>0$ for a valid, untangled mapping |
| $h$ | physical mesh width |

## Base vectors, metric tensor and metric terms

| symbol | meaning |
|---|---|
| $\mathbf a_i=\partial\mathbf x/\partial\xi^i$ | covariant base vectors (tangent to the $\xi^i$ coordinate lines) |
| $\mathbf a^i=\nabla\xi^i$ | contravariant base vectors (normal to the $\xi^i$ = const surfaces); $\mathbf a^i\cdot\mathbf a_j=\delta^i_j$ |
| $g_{ij}=\mathbf a_i\cdot\mathbf a_j$, $g^{ij}=\mathbf a^i\cdot\mathbf a^j$ | covariant and contravariant metric tensors; $\det(g_{ij})=J^2$ |
| $J\mathbf a^i$ | **metric terms** (contravariant base vectors scaled by $J$), the coefficients of the conservative (strong) form; in 3-D $J\mathbf a^1=\mathbf a_2\times\mathbf a_3$ and cyclically; in 2-D $J\nabla\xi=(y_\eta,-x_\eta)$, $J\nabla\eta=(-y_\xi,x_\xi)$ |
| $\sum_i\partial(J\mathbf a^i)/\partial\xi^i=0$ | **metric identities** (surface conservation law), exact for any smooth mapping |
| $\theta$ | angle between coordinate lines (skewness); orthogonal grid: $g_{12}=0$ |

## Moving grids

| symbol | meaning |
|---|---|
| $\dot{\mathbf x}=\partial_t\mathbf x|_{\boldsymbol\xi}$ | grid (mesh) velocity |
| $\xi^i_t=-\dot{\mathbf x}\cdot\mathbf a^i$ | time metric terms |
| $\partial_t J|_{\boldsymbol\xi}+\sum_i\partial(J\xi^i_t)/\partial\xi^i=0$ | **geometric conservation law** (volume conservation law) in differential form |

## Grid generation

| symbol | meaning |
|---|---|
| $\mathcal P_\xi$, $\mathcal P_\eta$; $\mathcal P_\xi\oplus\mathcal P_\eta=\mathcal P_\xi+\mathcal P_\eta-\mathcal P_\xi\mathcal P_\eta$ | univariate interpolation projectors of transfinite interpolation and their Boolean sum |
| $\varphi_0,\varphi_1$ | blending functions (cardinal: $\varphi_m(\xi_n)=\delta_{mn}$) |
| $P$, $Q$ (2-D); $P^i$ | control (source, forcing) functions of the elliptic generator $\nabla^2\xi^i=P^i$ |
| $s$ | arc length along a coordinate line; $\Delta s$ the first spacing off a boundary |
| $V$ | prescribed cell volume (area) of a hyperbolic generator |
| $I_s$, $I_o$, $I_v$ | smoothness, orthogonality and weighted-volume functionals of variational generation |
| $w(\mathbf x)$ | weight function of a variational or adaptive generator |
| $\lambda_o$, $\lambda_v$ | weights of the functionals in a combined variational principle |
| $\sigma(\mathbf x)$, $w_\sigma$ | level-set (implicit geometry) function whose zero isocontour is a target surface; weight of a fitting penalty |

## Adaptation and moving meshes

| symbol | meaning |
|---|---|
| $M(\mathbf x,t)>0$ | monitor function (scalar), e.g. arc length $\sqrt{1+u_x^2}$; $\mathbb M$ a monitor (metric) tensor |
| $\theta_M(t)=\int_\Omega M\,d\mathbf x$ | total monitor |
| $\tau$ | relaxation time of a moving mesh PDE |
| $u$ | a scalar solution driving adaptation |

## Element Jacobians, targets and quality

| symbol | meaning |
|---|---|
| $\mathsf W$ | Jacobian of the ideal (reference, target) element, $\det\mathsf W>0$ |
| $\mathsf T=\mathsf A\mathsf W^{-1}$ | Jacobian of the map from the target to the physical element |
| $|\mathsf T|$ | Frobenius norm $\sqrt{\mathrm{tr}(\mathsf T^{\mathsf T}\mathsf T)}$ |
| $\kappa(\mathsf T)=|\mathsf T||\mathsf T^{-1}|$ | condition number of an element |
| $J_0$ | Jacobian determinant of the straight-sided (linear) element from which a curved element is built |
| $\mathcal D(\boldsymbol\xi)=J/J_0$ | distortion (scaled Jacobian) of a curved high-order element; valid iff $\mathcal D>0$ everywhere |
| $\mu(\mathsf T)$ | a quality (distortion) metric; shape metrics are $1$ for a scaled rotation of the target and $0$ for a degenerate element |

## Discretization and flow

| symbol | meaning |
|---|---|
| $\mathbf q$ | conserved variables; $\hat{\mathbf q}=J\mathbf q$ in curvilinear coordinates |
| $\boldsymbol{\mathcal F}=(\mathbf f_1,\dots,\mathbf f_d)$ | physical flux; contravariant flux $\hat{\mathbf f}^i=J\mathbf a^i\cdot\boldsymbol{\mathcal F}$ (moving grids: plus $J\xi^i_t\,\mathbf q$) |
| $\delta_i$ | the discrete derivative operator applied to the fluxes in direction $\xi^i$ |
| $\delta^{\mathrm o}_i$, $\delta^{\mathrm{in}}_i$ | outer and inner discrete operators of the conservative metric forms (e.g. $J\xi_x=\delta^{\mathrm o}_\zeta(z\,\delta^{\mathrm{in}}_\eta y)-\delta^{\mathrm o}_\eta(z\,\delta^{\mathrm{in}}_\zeta y)$) |
| $\mathcal I_k$ | interpolation onto polynomials of degree $k$ (element-wise) |
| $r$; $k$ | order of accuracy; polynomial degree of a discretization |
| $\rho$, $\mathbf u$, $p$, $E$, $\gamma$ | density, velocity, pressure, total energy per unit volume, ratio of specific heats |

## Clashes kept on purpose

$\theta$ (angle between coordinate lines) and $\theta_M$ (total monitor,
always subscripted). $\mathsf T$ (target-to-physical Jacobian, sans-serif)
and the transpose superscript ${}^{\mathsf T}$. $\varphi$ (blending function)
is not used for any other quantity. $\tau$ is only the relaxation time of
moving mesh PDEs.
