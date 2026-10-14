---
type: Result
title: "Stokes' theorem for differential forms"
description: "For a (p−1)-form α on an oriented p-dimensional region Ω with boundary ∂Ω, ∫_Ω dα = ∫_∂Ω α; one theorem whose cases are the fundamental theorem of calculus for exact 1-forms, Green's theorem in the plane, the classical Stokes theorem and the divergence theorem."
status: established
aliases: [generalized Stokes theorem, Stokes-Cartan theorem, fundamental theorem of exterior calculus, Stokes theorem for forms]
tags: [integral-theorems, differential-forms, exterior-calculus]
timestamp: 2026-10-14T00:00:00Z
---

# Stokes' theorem for differential forms

**Statement** ([Arfken et al. (2013)](/sources/arfken-2013.md), §4.7,
eq. (4.106), p. 245). If $\Omega$ is a simply connected ("no holes") region
of a $p$-dimensional differentiable manifold in a $D$-dimensional space
($D\ge p$), with $(p-1)$-dimensional boundary $\partial\Omega$, and $\alpha$
is a $(p-1)$-form defined on $\Omega$ and its boundary, then

$$\int_\Omega d\alpha=\int_{\partial\Omega}\alpha ,$$

with $d$ the [exterior derivative](/definitions/exterior-derivative.md). The
book calls it "the generalization, to $p$ dimensions" of
$\int_C d\phi=\phi(\mathbf x_1)-\phi(\mathbf x_0)$ along any curve $C$ from $\mathbf x_0$ to $\mathbf x_1$ (eq. (4.101)). Signs: the differentials of
$d\alpha$ are those of $\alpha$ in the same order, preceded by the one
produced by the differentiation; this fixes the relative orientation of
$\Omega$ and $\partial\Omega$ (p. 245).

**Argument given** (eqs. (4.107)–(4.108), p. 246; "a rigorous proof ... is
somewhat complicated, but an indication of its validity is not too
involved"): for a monomial $\alpha=a\,dx^2\wedge\cdots\wedge dx^p$, cover the
part of $\Omega$ next to the boundary with thin parallelepipeds of thickness
$\delta$ in $x^1$; integrating $d\alpha=(\partial a/\partial x^1)\,dx^1\wedge\cdots\wedge dx^p$
across each gives the difference of $\int a\,dx^2\wedge\cdots\wedge dx^p$ on
its two faces of constant $x^1$; repeating the construction inwards collapses
the inner boundary to zero volume.

## Cases in two and three dimensions

Different cases of this single theorem were "originally identified as
distinct theorems" (p. 246):

| $p$ | $\alpha$ | result | source |
|---|---|---|---|
| 1 | $\phi$ (exact 1-form $d\phi$) | $\int_C d\phi=\phi(\mathbf x_1)-\phi(\mathbf x_0)$ | eq. (4.101), p. 244 |
| 2, $D=2$ | $P\,dx+Q\,dy$ | [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md), $\oint_C(P\,dx+Q\,dy)=\int_S(\partial_xQ-\partial_yP)\,dS$ | Example 4.7.1, eqs. (4.109)–(4.111), pp. 246–247 |
| 2, $D=3$ | $v_k\,dx^k$ | [Stokes' theorem](/results/stokes-theorem.md), $\oint_C\mathbf v\cdot d\mathbf x=\int_S(\nabla\times\mathbf v)\cdot d\mathbf S$ | Example 4.7.2, eqs. (4.112)–(4.114), p. 247 |
| 3, $D=3$ | $b_1\,dx^2\wedge dx^3+b_2\,dx^3\wedge dx^1+b_3\,dx^1\wedge dx^2$ | [divergence theorem](/results/divergence-theorem.md), $\int_V\nabla\cdot\mathbf b\,dV=\oint_S\mathbf b\cdot d\mathbf S$ | Example 4.7.3, eqs. (4.115)–(4.117), p. 248 |

The identifications $dy\wedge dz\mapsto dS_x$, $dz\wedge dx\mapsto dS_y$,
$dx\wedge dy\mapsto dS_z$ and $dx\wedge dy\wedge dz\mapsto dV$, as well as
counterclockwise traversal in the plane, are choices made to match
right-handed Cartesian computation; "the differential forms calculus does
not know whether we intend to use a right-handed coordinate system" and the
user carries the responsibility for these correspondences (pp. 247–248). In
the planar case the calculus by itself fixes $\oint_Cx\,dy=A$ and
$\oint_Cy\,dx=-A$ for counterclockwise traversal (p. 247).

## Qualification: simple connectivity

The book states the theorem for simply connected $\Omega$ ("one with no
holes"). The founding source states the vector-calculus cases for multiply
connected regions too, with every boundary component included and
oriented: the divergence theorem "for both simply and multiply connected
closed surfaces" and Stokes' theorem for simply and multiply connected
two-sided open surfaces ([Riley et al. (2006)](/sources/riley-2006.md),
pp. 401, 406). The two statements differ in hypothesis, not in conclusion:
Arfken assumes more than Riley needs and does not claim failure without the
assumption (its own Gauss's-law example joins a cavity to the outer boundary
by a thin tube to stay inside its hypothesis, §3.9, pp. 175–176). Recorded
as a qualification, not a contradiction.

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.7, pp. 243–248; §3.9, pp. 175–176.
* [Riley et al. (2006)](/sources/riley-2006.md), §11.8, p. 401; §11.9, p. 406 (multiply connected cases).
