---
type: Definition
title: "Vector area element"
description: "The oriented surface element dS = n̂ dS, outward for closed surfaces and right-handed with the perimeter for open ones; for a parametrised surface x(u,v) it is (∂x/∂u × ∂x/∂v) du dv, and on a coordinate surface ξ^i = const it is the cross product of the two in-surface base vectors."
status: established
aliases: [vector surface element, oriented area element, area vector, surface element, face area vector]
tags: [vector-calculus, integral-theorems, surfaces, metric]
timestamp: 2026-10-14T00:00:00Z
---

# Vector area element

The **vector area element** of a surface $S$ is $d\mathbf S=\hat{\mathbf n}\,dS$,
with $\hat{\mathbf n}$ the unit normal and $dS$ the scalar area
([Riley et al. (2006)](/sources/riley-2006.md), §11.5, p. 390).
Orientation convention (p. 390; [Arfken et al. (2013)](/sources/arfken-2013.md), §3.7,
p. 161, with the same two rules):

* closed surface (enclosing a volume $V$, not necessarily simply connected):
  $\hat{\mathbf n}$ points **outward**;
* open surface spanning a perimeter $C$: $\hat{\mathbf n}$ follows the
  right-hand screw rule with the direction in which $C$ is traversed. The
  surface must be two-sided (a Möbius strip is excluded). Arfken et al. make
  the rule local: at a perimeter point take $\mathbf u$ along the direction of
  travel and $\mathbf w$ tangent to and lying on the surface, and use
  $\mathbf u\times\mathbf w$ as positive normal; this handles surfaces such as
  a sphere with a hole (fig. 3.13, p. 161).

The flux form $\int_S\mathbf v\cdot d\mathbf S$ "is by far the most commonly
encountered surface integral" (Arfken et al., p. 161; worked flux through
the four faces of a tetrahedron, Example 3.7.2, pp. 161–162).

Surface integrals are defined as limits of sums over elements,
$\int_S\mathbf v\cdot d\mathbf S=\lim_{N\to\infty}\sum_p\mathbf v(\mathbf x_p)\cdot\hat{\mathbf n}_p\,\Delta S_p$
with all $\Delta S_p\to0$ (p. 390); $\int_S\mathbf v\cdot d\mathbf S$ is the
**flux** of $\mathbf v$ through $S$ (p. 395).

## Parametrised surfaces

For $S$ given by $\mathbf x(u,v)$ (§10.5, eqs. (10.21)–(10.24), pp. 345–346),
the tangents $\partial\mathbf x/\partial u$, $\partial\mathbf x/\partial v$ to
the coordinate curves span the tangent plane, a normal is
$\mathbf n=\partial\mathbf x/\partial u\times\partial\mathbf x/\partial v$, and

$$dS=\left\lvert\frac{\partial\mathbf x}{\partial u}\times\frac{\partial\mathbf x}{\partial v}\right\rvert du\,dv,\qquad A=\iint_R\left\lvert\frac{\partial\mathbf x}{\partial u}\times\frac{\partial\mathbf x}{\partial v}\right\rvert du\,dv.$$

Example: the sphere of radius $a$ has $dS=a^2\sin\theta\,d\theta\,d\varphi$
(p. 347). For a surface $f(x,y,z)=0$ projected on the $xy$-plane,
$dS=\lvert\nabla f\rvert\,dA/(\partial f/\partial z)$ (eq. (11.10), p. 391),
valid where each line parallel to the $z$-axis cuts $S$ once.

## Coordinate surfaces of a curvilinear system

For an orthogonal system the face $\xi^1=$ const of the coordinate volume
element is $\Delta\mathbf S=\pm h_2h_3\,\Delta\xi^2\Delta\xi^3\,\hat{\mathbf a}_1$
(§11.7, worked example, p. 399), which yields the divergence formula of the
[integral definitions](/results/integral-definitions-of-grad-div-curl.md).
Arfken et al. write the full element
$d\mathbf S=h_2h_3\,d\xi^2d\xi^3\,\hat{\mathbf a}_1+h_3h_1\,d\xi^3d\xi^1\,\hat{\mathbf a}_2+h_1h_2\,d\xi^1d\xi^2\,\hat{\mathbf a}_3$
(eq. (3.135), p. 185), with the cylindrical and spherical cases
$R\,d\varphi\,dz\,\hat{\mathbf a}_R+dR\,dz\,\hat{\mathbf a}_\varphi+R\,dR\,d\varphi\,\hat{\mathbf a}_z$
and $r^2\sin\theta\,d\theta\,d\varphi\,\hat{\mathbf a}_r+r\sin\theta\,dr\,d\varphi\,\hat{\mathbf a}_\theta+r\,dr\,d\theta\,\hat{\mathbf a}_\varphi$
(eqs. (3.146), (3.154), pp. 189, 191). As a form, the oriented area element
is a 2-form, $dx^2\wedge dx^3\mapsto dS_1$ etc. (Arfken et al., p. 247;
[differential form](/definitions/differential-form.md)).

*Compiler's derivation (hypothesis-grade; not stated in this form by the
source).* Applying eq. (10.22) with $(u,v)=(\xi^2,\xi^3)$ on the surface
$\xi^1=$ const and the reciprocal-basis formula of §26.15 (p. 959;
[covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md)),
for any (also non-orthogonal) system

$$d\mathbf S=\mathbf a_2\times\mathbf a_3\,d\xi^2d\xi^3=J\,\mathbf a^1\,d\xi^2d\xi^3=J\,\nabla\xi^1\,d\xi^2d\xi^3,$$

up to orientation, with $J$ the [Jacobian](/definitions/jacobian.md); and
cyclically for the other two families. The face-normal area vector of a
coordinate surface is thus $J\nabla\xi^i$ per unit coordinate area.

The integrated vector area $\mathbf S=\int_S d\mathbf S$ vanishes for every
closed surface ([closed-surface vector area](/results/closed-surface-vector-area.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.5, pp. 345–347; §§11.5, 11.7, pp. 389–399; §26.15, p. 959.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.7, pp. 161–162; §3.10, pp. 185, 189, 191; §4.7, p. 247.
