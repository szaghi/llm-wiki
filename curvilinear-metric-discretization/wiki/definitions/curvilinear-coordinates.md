---
type: Definition
title: "General curvilinear coordinates"
description: "Three functions ξ^i of position that label points of space one-to-one through a differentiable, invertible mapping x(ξ), with coordinate surfaces ξ^i = const and coordinate curves; orthogonal when the three surfaces meet at right angles."
status: established
aliases: [curvilinear coordinate system, general coordinates, body-fitted coordinates, computational coordinates]
tags: [curvilinear-coordinates, coordinate-transformation]
timestamp: 2026-10-13T00:00:00Z
---

# General curvilinear coordinates

A system of **general curvilinear coordinates** labels each point of
three-dimensional Euclidean space by three numbers $\xi^1,\xi^2,\xi^3$ through
a mapping

$$x^i=x^i(\xi^1,\xi^2,\xi^3),\qquad \xi^i=\xi^i(x^1,x^2,x^3),\qquad i=1,2,3,$$

where all these functions are assumed continuous, differentiable and with a
single-valued inverse, "except perhaps at or on certain isolated points or
lines", so that the correspondence between $(x^1,x^2,x^3)$ and
$(\xi^1,\xi^2,\xi^3)$ is one-to-one
([Riley et al. (2006)](/sources/riley-2006.md), §10.10, p. 364). Cartesian,
cylindrical polar and spherical polar coordinates are special cases.

* The **coordinate surfaces** are $\xi^1=c_1$, $\xi^2=c_2$, $\xi^3=c_3$; each
  pair of them intersects in a **coordinate curve** (line), along which only
  one coordinate varies (§10.10, p. 364, fig. 10.11).
* The system is **orthogonal** if at every point the three coordinate surfaces
  through it meet at right angles; cylindrical and spherical polars are
  orthogonal (§10.10, p. 364).
* At each point two natural bases exist: the tangents
  $\mathbf a_i=\partial\mathbf x/\partial\xi^i$ to the coordinate curves and
  the normals $\mathbf a^i=\nabla\xi^i$ to the coordinate surfaces
  ([covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md)).
  Their lengths define the [scale factors](/definitions/scale-factors.md),
  their inner products the [metric tensor](/definitions/metric-tensor.md),
  and their triple product the [Jacobian](/definitions/jacobian.md).

The book develops the vector operators first for orthogonal systems only,
through scale factors (§10.10), and remarks that "non-orthogonal curvilinear
coordinates are difficult to work with and should be avoided if at all
possible" (exercise 10.22, p. 374); the forms valid for non-orthogonal systems
are the tensor forms of §26.20 ([gradient](/definitions/gradient.md),
[divergence](/definitions/divergence.md), [curl](/definitions/curl.md),
[Laplacian](/definitions/laplacian.md)). That advice is the book's, given for
analytic work; body-fitted grids are in general non-orthogonal, which is why
the general tensor forms are the ones this bundle needs.

## Standard orthogonal examples

| System | Mapping | Scale factors |
|---|---|---|
| cylindrical $(R,\varphi,z)$ | $x=R\cos\varphi$, $y=R\sin\varphi$, $z=z$; $R\ge0$, $0\le\varphi<2\pi$ | $h_R=1$, $h_\varphi=R$, $h_z=1$ |
| spherical $(r,\theta,\varphi)$ | $x=r\sin\theta\cos\varphi$, $y=r\sin\theta\sin\varphi$, $z=r\cos\theta$; $0\le\theta\le\pi$ | $h_r=1$, $h_\theta=r$, $h_\varphi=r\sin\theta$ |

(§10.9, eqs. (10.44), (10.53), pp. 357–365.) The exercises add paraboloidal,
hyperbolic and a non-orthogonal direction-cosine system (exercises 10.21–10.24,
pp. 374–375).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§10.9–10.10, pp. 357–369; §26.14, p. 955.
