---
type: Definition
title: "Jacobian of the coordinate mapping"
description: "J = det[∂x^i/∂ξ^j] = a_1·(a_2×a_3), the signed volume of the parallelepiped spanned by the covariant base vectors per unit coordinate volume, with |J| = √g; it carries the volume element dV = √g dξ^1dξ^2dξ^3 and is a relative scalar under changes of curvilinear coordinates."
status: established
aliases: [Jacobian, Jacobian determinant, sqrt g, cell volume factor, inverse Jacobian]
symbol: "$J$"
tags: [metric, jacobian, curvilinear-coordinates]
timestamp: 2026-10-13T00:00:00Z
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
  [scale factors](/definitions/scale-factors.md)).

Compiler's identifications (not stated in this form by the source; each is
one step from what it states):

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
* $J>0$ for a mapping that keeps right-handed triads right-handed; the
  source works with $\lvert J\rvert$ only and does not discuss orientation.

**Naming hazard.** Both $\det[\partial x/\partial\xi]$ and its reciprocal
$\det[\partial\xi/\partial x]$ are called "the Jacobian" in the literature —
the source itself flags the ambiguity for general transformations (p. 964).
This bundle fixes $J=\det[\partial x^i/\partial\xi^j]$; a source that uses the
reciprocal is mapped to $J^{-1}$ in its notation map
([notation registry](/notation.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.10, pp. 365–367; §26.15, pp. 957–959; §26.17, p. 964; exercise 26.25, p. 981, hint p. 983.
