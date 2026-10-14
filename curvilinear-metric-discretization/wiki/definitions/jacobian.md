---
type: Definition
title: "Jacobian of the coordinate mapping"
description: "J = det[∂x^i/∂ξ^j] = a_1·(a_2×a_3), the signed volume of the parallelepiped spanned by the covariant base vectors per unit coordinate volume, with |J| = √g; it carries the volume element dV = √g dξ^1dξ^2dξ^3 and is a relative scalar under changes of curvilinear coordinates."
status: established
aliases: [Jacobian, Jacobian determinant, sqrt g, cell volume factor, inverse Jacobian]
symbol: "$J$"
tags: [metric, jacobian, curvilinear-coordinates]
timestamp: 2026-10-14T00:00:00Z
---

# Jacobian of the coordinate mapping

For the mapping $\xi\mapsto\mathbf x$ of
[general curvilinear coordinates](/definitions/curvilinear-coordinates.md),
this bundle writes

$$J=\det\left[\frac{\partial x^i}{\partial\xi^j}\right]=\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3),\qquad \lvert J\rvert=\sqrt g,$$

where $\mathbf a_i$ are the
[covariant base vectors](/definitions/covariant-and-contravariant-bases.md)
and $g$ the determinant of the [metric tensor](/definitions/metric-tensor.md).

What the source states:

* The volume element is the volume of the parallelepiped spanned by
  $\mathbf a_i\,d\xi^i$ (exercise 26.25; §10.10, p. 366 for orthogonal
  systems), and $dV=\sqrt g\,d\xi^1d\xi^2d\xi^3$ (eq. (26.58), p. 957), with
  $\lvert\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)\rvert=\sqrt g$ (p. 959,
  "it may be shown"; exercise 26.25 asks for the proof)
  ([Riley et al. (2006)](/sources/riley-2006.md)).
* For a change between two general systems $\xi\mapsto\bar\xi$, the book calls
  $\lvert\partial\bar\xi/\partial\xi\rvert$, the determinant of
  $[\partial\bar\xi^i/\partial\xi^j]$, "the Jacobian of the transformation",
  and notes that its reciprocal $\lvert\partial\xi/\partial\bar\xi\rvert$ "is
  often called the Jacobian of the transformation" too (§26.17, p. 964). The
  metric determinant transforms as $\bar g=\lvert\partial\xi/\partial\bar\xi\rvert^2g$
  (worked example, p. 964), so $\sqrt g$ is a relative scalar of weight 1, a
  scalar density ([relative tensor](/definitions/relative-tensor.md)), and
  $dV$ is invariant (exercise 26.25, with hint p. 983).
* For orthogonal systems $\sqrt g=h_1h_2h_3$ (§26.15, p. 957;
  [scale factors](/definitions/scale-factors.md); also Arfken et al., p. 225).

What [Arfken et al. (2013)](/sources/arfken-2013.md) state (§4.4, pp. 227–231):

* **Definition and derivation.** For a change of variables from Cartesian
  $x^i$ to $\xi^i$, $dV=J\,d\xi^1d\xi^2d\xi^3$ with
  $J=\partial(x^1,x^2,\dots)/\partial(\xi^1,\xi^2,\dots)$, the determinant of
  the derivatives $\partial x^i/\partial\xi^j$ (eq. (4.74), p. 229) — this
  bundle's $J$. The volume of the region spanned by the displacements
  $(\partial\mathbf x/\partial\xi^i)\,d\xi^i$ is shown to equal the
  determinant by row operations that change each displacement only along the
  previous ones (Gram–Schmidt-like), valid in any number of dimensions and
  for non-orthogonal systems (pp. 227–229, figs. 4.1–4.2).
* **Triple product.** In three dimensions the determinant "corresponds
  exactly with the formula for the scalar triple product", the volume of the
  parallelepiped of the three displacement vectors; in two dimensions it is
  the $z$-component of the cross product of the two (Example 4.4.1,
  pp. 229–230). This states $J=\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)$,
  listed below as a compiler's identification for Riley.
* **Inverse.** $J^{-1}=\partial(\xi^1,\xi^2,\dots)/\partial(x^1,x^2,\dots)$
  equals $1/J$, proved by the determinant product theorem and the chain rule
  (eqs. (4.75)–(4.76), p. 230); computing $J^{-1}$ first is often easier
  (Example 4.4.2, p. 231).
* **Sign.** "Since $J$ is a determinant, it will have a sign that depends on
  the order in which" the two sets of coordinates "are specified"; this corresponds to
  the freedom of right- or left-handed coordinates, and "in typical
  applications ... it is usual to take its absolute value" (p. 229). With
  differential forms the sign is kept: $dx\wedge dy\wedge dz=J\,d\xi^1\wedge d\xi^2\wedge d\xi^3$
  with the signed $J$, and the oriented volume carries it (§4.7, p. 245;
  [wedge product](/definitions/wedge-product.md)).
* **Two dimensions, orthogonal:** $J=h_1h_2$ (exercise 4.4.2, p. 231).

Compiler's identifications (not stated in this form by Riley; each is one
step from what it states; the first and third are stated by Arfken et al.,
above):

* $\det[\partial x^i/\partial\xi^j]=\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)$,
  because the $j$-th column of the Jacobian matrix holds the Cartesian
  components of $\mathbf a_j$.
* $g=J^2$ follows from the weight-2 law above with the Cartesian system as
  the unbarred one ($g=1$ there).
* $\det[\partial\xi^i/\partial x^j]=1/J$, because the two matrices are
  inverse to each other (reciprocity $\mathbf a_i\cdot\mathbf a^j=\delta^j_i$,
  §10.10, pp. 366–367).
* $J\,\mathbf a^i=\mathbf a_j\times\mathbf a_k$ for $(i,j,k)$ cyclic, from
  the reciprocal-basis formula of p. 959.
* $J>0$ for a mapping that keeps right-handed triads right-handed; Riley
  works with $\lvert J\rvert$ only and does not discuss orientation; Arfken
  et al. tie the sign to handedness (above).

**Naming hazard.** Both $\det[\partial x/\partial\xi]$ and its reciprocal
$\det[\partial\xi/\partial x]$ are called "the Jacobian" in the literature —
the source itself flags the ambiguity for general transformations (p. 964).
This bundle fixes $J=\det[\partial x^i/\partial\xi^j]$; a source that uses the
reciprocal is mapped to $J^{-1}$ in its notation map
([notation registry](/notation.md)). Arfken et al. illustrate the hazard
inside one example: having defined $J=\partial(x)/\partial(u)$ and
$J^{-1}=\partial(u)/\partial(x)$ (eqs. (4.74)–(4.75)), Example 4.4.2 (p. 231)
calls "the Jacobian" $J=\partial(r,\theta,\varphi)/\partial(x,y,z)=1/(r^2\sin\theta)$
and $J^{-1}=\partial(x,y,z)/\partial(r,\theta,\varphi)=r^2\sin\theta$, the
reverse labelling; in this bundle's notation the spherical-polar Jacobian is
$J=r^2\sin\theta$. The book also notes that the "Jacobian matrix" and the
"Jacobian determinant" are both called the Jacobian, and follows the second
usage (p. 229).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.10, pp. 365–367; §26.15, pp. 957–959; §26.17, p. 964; exercise 26.25, p. 981, hint p. 983.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.3, p. 225; §4.4, pp. 227–231; §4.7, pp. 244–245; exercise 4.4.2, p. 231.
