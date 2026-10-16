---
type: Definition
title: "General curvilinear coordinates"
description: "Three functions ξ^i of position that label points of space one-to-one through a differentiable, invertible mapping x(ξ), with coordinate surfaces ξ^i = const and coordinate curves; orthogonal when the three surfaces meet at right angles."
status: established
aliases: [curvilinear coordinate system, general coordinates, body-fitted coordinates, computational coordinates]
tags: [curvilinear-coordinates, coordinate-transformation]
timestamp: 2026-10-16T00:00:00Z
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
[Arfken et al. (2013)](/sources/arfken-2013.md) (§3.10, pp. 182–184) introduce the same
mapping, $x^i=x^i(\xi^1,\xi^2,\xi^3)$ with $dx^i=(\partial x^i/\partial\xi^j)\,d\xi^j$
(eq. (3.127)), from the example of spherical polars, and draw four
observations: coordinates need not be lengths; a coordinate surface can have
a position-dependent normal; surfaces of different constant values of one
coordinate need not be parallel; a change of one coordinate moves the point
by an amount and in a direction that depend on position (pp. 182–183).

* The **coordinate surfaces** are $\xi^1=c_1$, $\xi^2=c_2$, $\xi^3=c_3$; each
  pair of them intersects in a **coordinate curve** (line), along which only
  one coordinate varies (§10.10, p. 364, fig. 10.11).
* The system is **orthogonal** if at every point the three coordinate surfaces
  through it meet at right angles; cylindrical and spherical polars are
  orthogonal (§10.10, p. 364). Arfken et al. state the same condition as
  mutual perpendicularity of the unit normals to the three coordinate
  surfaces (p. 183); in an orthogonal system these coincide with the unit
  tangents, see [bases](/definitions/covariant-and-contravariant-bases.md).
* **Components are local.** A vector field is decomposed on the unit vectors
  *at the point where it is evaluated*; algebra between two fields is
  componentwise only at the same point, and the position vector is not
  $r\hat{\mathbf a}_r+\theta\hat{\mathbf a}_\theta+\varphi\hat{\mathbf a}_\varphi$
  (Arfken et al., p. 183); differential and integral operators must
  include the derivatives of the unit vectors (pp. 183, 189, 191).
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
are the tensor forms of §26.20, which Arfken et al. derive in §4.3
(pp. 218–225) ([gradient](/definitions/gradient.md),
[divergence](/definitions/divergence.md), [curl](/definitions/curl.md),
[Laplacian](/definitions/laplacian.md)). That advice is the book's, given for
analytic work; body-fitted grids are in general non-orthogonal, which is why
the general tensor forms are the ones this bundle needs. Arfken et al.
likewise develop the vector operators in Ch. 3 for orthogonal systems only
and remark that, of "at least 11 coordinate systems" useful in physics, the
"evolution of computers and efficient programming techniques" has reduced
the need for most, so they treat only Cartesian, cylindrical and spherical
coordinates in the text (p. 187).

## Coordinates adapted to a vector field

Three application papers of the bundle compute in coordinates adapted to a
magnetic field: [magnetic flux coordinates](/definitions/magnetic-flux-coordinates.md)
$(\Psi,\vartheta,\varphi)$, whose first coordinate labels the surfaces the
field lines lie on, and [field-aligned coordinates](/definitions/field-aligned-coordinates.md),
obtained from them by shifting the toroidal angle along the field lines so
that one coordinate curve is a field line
([Jiang et al. (2024)](/sources/jiang-2024.md), §III, pp. 3–4;
[Liu et al. (2024)](/sources/liu-2024.md), §II B, p. 3;
[Seto et al. (2023)](/sources/seto-2023.md), §2, pp. 2–4). The second
system is non-orthogonal by construction, a case against the book's
advice above: the codes accept the non-orthogonality to put the parallel
derivative on one coordinate, and they need the general tensor forms of the
operators. Both have singular or periodic structure that ordinary
body-fitted grids lack: a coordinate singularity on the magnetic axis
(excluded from the domain) and a twist-shift periodicity in place of plain
periodicity in $\vartheta$.

## Standard orthogonal examples

| System | Mapping | Scale factors |
|---|---|---|
| cylindrical $(R,\varphi,z)$ | $x=R\cos\varphi$, $y=R\sin\varphi$, $z=z$; $R\ge0$, $0\le\varphi<2\pi$ | $h_R=1$, $h_\varphi=R$, $h_z=1$ |
| spherical $(r,\theta,\varphi)$ | $x=r\sin\theta\cos\varphi$, $y=r\sin\theta\sin\varphi$, $z=r\cos\theta$; $0\le\theta\le\pi$ | $h_r=1$, $h_\theta=r$, $h_\varphi=r\sin\theta$ |

(§10.9, eqs. (10.44), (10.53), pp. 357–365; Arfken et al., eqs. (3.144),
(3.145), (3.152), (3.153), pp. 188–191, with the same ranges and the remark
that $\varphi$ is undefined on the axis and $\theta,\varphi$ at the origin.)
The exercises add paraboloidal, hyperbolic and a non-orthogonal
direction-cosine system (Riley, exercises 10.21–10.24, pp. 374–375), and the
orthogonal $(u,v,z)$ system $xy=u$, $x^2-y^2=v$ and elliptic cylindrical
coordinates (Arfken, exercises 3.10.1–3.10.2, p. 196).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§10.9–10.10, pp. 357–369; §26.14, p. 955.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.10, pp. 182–191; §4.3, pp. 218–225; exercises 3.10.1–3.10.2, p. 196.
* [Jiang et al. (2024)](/sources/jiang-2024.md), §III, pp. 3–4.
* [Liu et al. (2024)](/sources/liu-2024.md), §II B, p. 3.
* [Seto et al. (2023)](/sources/seto-2023.md), §2, pp. 2–4.
