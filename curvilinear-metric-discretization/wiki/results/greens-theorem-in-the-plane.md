---
type: Result
title: "Green's theorem in the plane"
description: "For P(x,y), Q(x,y) with continuous derivatives on a plane region R bounded by C traversed with R on the left, ∮_C (P dx + Q dy) = ∬_R (∂Q/∂x − ∂P/∂y) dx dy; the two-dimensional divergence theorem, valid for multiply connected regions with every boundary traversed positively."
status: established
aliases: [Green's theorem, two-dimensional divergence theorem, planar Stokes theorem, shoelace area formula]
tags: [integral-theorems, vector-calculus, two-dimensional]
timestamp: 2026-10-14T00:00:00Z
---

# Green's theorem in the plane

**Statement** ([Riley et al. (2006)](/sources/riley-2006.md), §11.3,
eq. (11.4), p. 384). If $P(x,y)$, $Q(x,y)$ and their partial derivatives are
single-valued, finite and continuous inside and on the boundary $C$ of a
simply connected plane region $R$,

$$\oint_C(P\,dx+Q\,dy)=\iint_R\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dx\,dy,$$

with $C$ traversed so that $R$ lies on the left (anticlockwise).

* **Proof** (pp. 384–385): integrate $\partial P/\partial y$ in $y$ between
  the lower and upper boundary curves and $\partial Q/\partial x$ in $x$
  between the left and right ones; this assumes a region that each line
  parallel to an axis cuts at most twice (fig. 11.3).
* **Multiply connected regions** (p. 385): valid if the line integral is
  taken over all boundaries, each traversed with $R$ on the left.
* **Area** (worked example, p. 385): $P=-y$, $Q=x$ give
  $A=\frac12\oint_C(x\,dy-y\,dx)=\oint_Cx\,dy=-\oint_Cy\,dx$.
* **Path independence** (p. 386): $\partial P/\partial y=\partial Q/\partial x$
  throughout a simply connected region is sufficient, and necessary, for
  $\int_A^B(P\,dx+Q\,dy)$ to be path-independent, i.e. for $P\,dx+Q\,dy$ to be
  exact (eq. (11.5); [conservative vector field](/definitions/conservative-vector-field.md)).
* It is both the two-dimensional [divergence theorem](/results/divergence-theorem.md)
  (with $P=-v_y$, $Q=v_x$, p. 402) and the planar case of
  [Stokes' theorem](/results/stokes-theorem.md) (with $P=v_x$, $Q=v_y$, p. 407).
  The book calls it "sometimes called the divergence theorem in two
  dimensions" (p. 384).

[Arfken et al. (2013)](/sources/arfken-2013.md) obtain the theorem as the case $p=D=2$ of
[Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md):
for the 1-form $P\,dx+Q\,dy$, $d(P\,dx+Q\,dy)=(\partial_xQ-\partial_yP)\,dx\wedge dy$,
and with the orientation $dx\wedge dy\mapsto dx\,dy$ the same formula
follows (Example 4.7.1, eqs. (4.109)–(4.111), pp. 246–247). They derive the
area formulas $\oint_Cx\,dy=A$ and $\oint_Cy\,dx=-A$ for counterclockwise
traversal, and $\frac12\oint_C(x\,dy-y\,dx)=A$ via Stokes' theorem
(exercise 3.8.6, p. 169), and stress that the counterclockwise convention
and $dx\wedge dy\mapsto+dx\,dy$ are the user's choices, "not dictated by the
theory of differential forms" (p. 247). Their statement assumes a simply
connected region (via eq. (4.106)); Riley's covers multiply connected
regions with every boundary positively traversed — a difference of
hypothesis (see the [qualification](/results/generalized-stokes-theorem.md)).

Exercise 11.8 (p. 410) asks the reader to find the flaw in a "proof" that
$\pi=0$ obtained by applying the theorem to $\tan^{-1}(y/x)$ and
$\tan^{-1}(x/y)$, functions that violate the continuity hypothesis in $R$.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §11.3, pp. 384–387; §11.8, p. 402; §11.9, p. 407; exercise 11.8, p. 410.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.7, pp. 245–247; exercise 3.8.6, p. 169.
