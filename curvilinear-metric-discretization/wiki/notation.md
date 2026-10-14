---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-13T00:00:00Z
---

# Notation registry

This registry is normative for every concept page of the bundle. Source pages
translate each source's native symbols into these in their `# Notation map`.
It was seeded on 2026-10-13 from the tensor-calculus conventions of
[Riley et al. (2006)](/sources/riley-2006.md) (Chs. 10, 11, 26), adjusted so
that the body-fitted-grid literature of computational fluid dynamics
(computational coordinates $(\xi,\eta,\zeta)$, metric coefficients
$\xi_x,\dots$, Jacobian, covariant and contravariant base vectors) maps onto
it one symbol to one symbol. Symbols marked *reserved* are registered for the
scope of the bundle (metric discretization, moving grids) but no concept page
uses them yet.

## Index and summation conventions

| Symbol | Meaning | Notes |
|---|---|---|
| $i,j,k,l,m,n$ | coordinate indices, each in $\{1,2,3\}$ | three-dimensional Euclidean space unless a page says otherwise |
| $a^i b_i$ | summation convention: an index appearing once as a superscript and once as a subscript in a term is summed over $1,2,3$ | in Cartesian frames, where upper and lower components coincide, a repeated subscript is summed |
| $\delta_{ij}$, $\delta^i_j$ | Kronecker delta (1 if $i=j$, else 0) | $\delta^i_j$ is the mixed form, a tensor under general transformations |
| $\varepsilon_{ijk}$, $\varepsilon^{ijk}$ | Levi-Civita permutation symbol: $+1$ (even permutation of 1,2,3), $-1$ (odd), 0 otherwise | numerically equal; relative tensors of weight $-1$ and $+1$ respectively (see [relative tensor](/definitions/relative-tensor.md)) |
| (no sum) | written explicitly when a repeated index is not summed | e.g. $v^i=\hat v_i/h_i$ (no sum) |

## Coordinates and the coordinate mapping

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathbf x$ | position vector of a point in Euclidean space | |
| $x^i$ | Cartesian coordinates; $(x^1,x^2,x^3)\equiv(x,y,z)$ | Cartesian components may carry lower indices, $x_i=x^i$ |
| $\xi^i$ | general curvilinear (computational) coordinates; $(\xi^1,\xi^2,\xi^3)\equiv(\xi,\eta,\zeta)$ | the mapping $\mathbf x=\mathbf x(\xi^1,\xi^2,\xi^3)$ is assumed one-to-one and differentiable except at isolated points or lines |
| $\bar\xi^i$ | a second general coordinate system, used for transformation laws | $\bar\xi^i=\bar\xi^i(\xi^1,\xi^2,\xi^3)$, invertible |
| $\partial_i$ | $\partial/\partial\xi^i$ | |
| $\partial x^i/\partial\xi^j$ | Jacobian matrix of the mapping $\xi\mapsto\mathbf x$ | shorthand $x_\xi\equiv\partial x/\partial\xi$, $y_\eta$, … for written-out 2D/3D forms |
| $\partial\xi^i/\partial x^j$ | metric coefficients (inverse Jacobian matrix) | shorthand $\xi_x\equiv\partial\xi/\partial x$, $\eta_y$, … for written-out 2D/3D forms |
| $(R,\varphi,z)$ | cylindrical polar coordinates | $R$, not $\rho$, so that $\rho$ stays density |
| $(r,\theta,\varphi)$ | spherical polar coordinates | $\theta$ polar angle, $\varphi$ azimuth |
| $t$ | physical time | |
| $\tau$ | computational time, $\tau=t$ (*reserved*) | for moving grids $\mathbf x=\mathbf x(\xi^1,\xi^2,\xi^3,\tau)$ |
| $\partial\mathbf x/\partial\tau$ | grid-point velocity (*reserved*) | |
| $\partial\xi^i/\partial t$ | time metric of a moving grid (*reserved*) | shorthand $\xi_t$ |

## Bases and scale factors

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathbf e_k$ | constant orthonormal Cartesian basis | $(\mathbf e_1,\mathbf e_2,\mathbf e_3)\equiv(\mathbf i,\mathbf j,\mathbf k)$ |
| $\mathbf a_i$ | covariant base vectors, $\mathbf a_i=\partial\mathbf x/\partial\xi^i$, tangent to the $\xi^i$ coordinate curve | see [covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md) |
| $\mathbf a^i$ | contravariant base vectors, $\mathbf a^i=\nabla\xi^i$, normal to the surface $\xi^i=$ const | $\mathbf a_i\cdot\mathbf a^j=\delta^j_i$ |
| $\hat{\mathbf a}_i$ | unit tangent basis, $\hat{\mathbf a}_i=\mathbf a_i/h_i$ | |
| $\hat{\mathbf a}^i$ | unit normal basis, $\hat{\mathbf a}^i=\mathbf a^i/\lvert\mathbf a^i\rvert$ | coincides with $\hat{\mathbf a}_i$ in orthogonal systems |
| $h_i$ | scale factors, $h_i=\lvert\mathbf a_i\rvert$ | see [scale factors](/definitions/scale-factors.md) |
| $\hat{\mathbf a}_R,\hat{\mathbf a}_\varphi,\hat{\mathbf a}_z$; $\hat{\mathbf a}_r,\hat{\mathbf a}_\theta,\hat{\mathbf a}_\varphi$ | unit bases of cylindrical and spherical polars | |

## Metric

| Symbol | Meaning | Notes |
|---|---|---|
| $g_{ij}$ | covariant metric tensor, $g_{ij}=\mathbf a_i\cdot\mathbf a_j$ | see [metric tensor](/definitions/metric-tensor.md) |
| $g^{ij}$ | contravariant metric tensor, $g^{ij}=\mathbf a^i\cdot\mathbf a^j$; $[g^{ij}]=[g_{ij}]^{-1}$ | |
| $g$ | $\det[g_{ij}]$ | relative scalar of weight 2 |
| $J$ | Jacobian of the mapping, $J=\det[\partial x^i/\partial\xi^j]=\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)$ | $\lvert J\rvert=\sqrt g$; see [Jacobian](/definitions/jacobian.md). A source whose "Jacobian" is the reciprocal $\det[\partial\xi^i/\partial x^j]$ is mapped to $J^{-1}$ in its notation map. The Jacobian between two general systems is written in full, $\lvert\partial\bar\xi/\partial\xi\rvert$ |
| $s$, $ds$ | arc length and its element, $(ds)^2=g_{ij}\,d\xi^i d\xi^j$ | |
| $dV$ | volume element, $dV=\sqrt g\,d\xi^1d\xi^2d\xi^3$ | |

## Fields, components and tensors

| Symbol | Meaning | Notes |
|---|---|---|
| $\phi,\psi$ | scalar fields | the azimuth is $\varphi$, never $\phi$ |
| $\mathbf v,\mathbf w$ | generic vector fields | |
| $v^i$, $v_i$ | contravariant and covariant components, $\mathbf v=v^i\mathbf a_i=v_i\mathbf a^i$ | |
| $\hat v_i$ | physical components on the unit basis, $\mathbf v=\sum_i\hat v_i\hat{\mathbf a}_i$ | for orthogonal systems $v^i=\hat v_i/h_i$ (no sum) |
| $\mathbf T$ | second-order tensor; $T^{ij}$, $T^i{}_j$, $T_{ij}$ its contravariant, mixed, covariant components | $\mathbf T=T^{ij}\mathbf a_i\otimes\mathbf a_j$ |
| $\otimes$ | outer (tensor) product | |
| $L_{ij}$ | orthogonal matrix of a rotation of Cartesian axes, $x'_i=L_{ij}x_j$ | Cartesian-tensor pages only; primes there denote the rotated frame |
| $w$ | weight of a relative tensor | |
| $\mathbf c$ | an arbitrary constant vector (proof device) | |
| $\rho$ | mass density | |
| $\mathbf u$ | fluid velocity | |

## Differential operators

| Symbol | Meaning | Notes |
|---|---|---|
| $\nabla$ | del; $\nabla=\mathbf e_k\,\partial/\partial x^k$ in Cartesians, $\nabla=\mathbf a^i\partial_i$ in general coordinates | |
| $\nabla\phi$ | gradient | [gradient](/definitions/gradient.md) |
| $\nabla\cdot\mathbf v$ | divergence | [divergence](/definitions/divergence.md) |
| $\nabla\times\mathbf v$ | curl | [curl](/definitions/curl.md) |
| $\nabla^2$ | Laplacian | [Laplacian](/definitions/laplacian.md) |
| $\partial\phi/\partial n$ | normal derivative, $\hat{\mathbf n}\cdot\nabla\phi$ | |
| $v^i{}_{,j}$ | partial derivative $\partial v^i/\partial\xi^j$ | |
| $v^i{}_{;j}$, $v_{i;j}$ | covariant derivative | [covariant derivative](/definitions/covariant-derivative.md) |
| $\delta v^i/\delta t$ | absolute (intrinsic) derivative along a curve $\xi^i(t)$ | |
| $\Gamma^k_{ij}$ | Christoffel symbol of the second kind, $\partial_j\mathbf a_i=\Gamma^k_{ij}\mathbf a_k$ | [Christoffel symbols](/definitions/christoffel-symbols.md) |
| $\Gamma_{kij}$ | Christoffel symbol of the first kind, $\Gamma_{kij}=g_{kl}\Gamma^l_{ij}$ | |
| $R^l{}_{ijk}$ | Riemann curvature tensor | identically zero in Euclidean space |

## Curves, surfaces and volumes

| Symbol | Meaning | Notes |
|---|---|---|
| $V$ | volume (region) | |
| $S$ | surface; for a closed surface, the boundary of $V$ | |
| $C$ | curve; for an open surface, its bounding perimeter | |
| $R$ | region of a plane, with area $A$ | |
| $d\mathbf x$ | vector line element along a curve | |
| $\hat{\mathbf t}$ | unit tangent of a curve | |
| $\hat{\mathbf n}$ | unit normal of a surface; outward for a closed surface, right-handed with the traversal of $C$ for an open one | |
| $dS$, $d\mathbf S$ | scalar and vector area elements, $d\mathbf S=\hat{\mathbf n}\,dS$ | [vector area element](/definitions/vector-area-element.md) |
| $\mathbf S$ | vector area of a surface, $\mathbf S=\int_S d\mathbf S$ | |
| $\oint_C$, $\oint_S$ | integral over a closed curve, closed surface | |
| $P(x,y)$, $Q(x,y)$ | the two functions of Green's theorem in the plane | local to that theorem |

## Auxiliary symbols

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathbf b$ | a further generic vector field (with $\mathbf v,\mathbf w$) | |
| $A$, $A_{ij}$ | a generic $3\times3$ matrix; an antisymmetric second-order tensor | |
| $U$, $G$ | the matrices $[\partial\xi^i/\partial\bar\xi^j]$ and $[g_{ij}]$ | transformation of $g$ |
| $p_i$ | dual pseudovector of an antisymmetric tensor, $p_i=\tfrac12\varepsilon_{ijk}A_{jk}$ | |
| $N$, $M$ | orders of tensors | |
| $\lambda,\eta,\nu$ | coefficients of the general fourth-order isotropic tensor | |
| $\hat{\mathbf s}$ | a unit direction (directional derivative) | |
| $\hat{\mathbf x}$ | radial unit vector $\mathbf x/r$ | |
| $(u,v)$ | parameters of a parametrised surface $\mathbf x(u,v)$ | $\mathbf n=\partial_u\mathbf x\times\partial_v\mathbf x$ unnormalised normal |
| $\boldsymbol\omega$ | angular velocity of a rigid rotation | |
| $\delta(\mathbf x)$, $\delta(R)$ | Dirac delta in three dimensions; two-dimensional delta on the axis $R=0$ | |
| $Q$ | strength of a point source | |
| $\Delta$ | finite increment, e.g. $\Delta\xi^i$, $\Delta V$ | |
| $\phi_P$ | value of $\phi$ at a point $P$ | |
