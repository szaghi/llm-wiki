---
type: Result
title: "Integral definitions of grad, div and curl"
description: "The coordinate-free definitions ∇φ = lim (1/V)∮φ dS, ∇·v = lim (1/V)∮v·dS, ∇×v = lim (1/V)∮dS×v and (∇×v)·n̂ = lim (1/A)∮v·dx as the volume or area shrinks to a point, which the source shows reproduce the differential forms in Cartesian and (for div and curl) orthogonal curvilinear coordinates."
status: established
aliases: [geometric definitions of grad div curl, flux definition of divergence, circulation definition of curl, finite-volume definition]
tags: [integral-theorems, operators, vector-calculus, conservation-form]
timestamp: 2026-10-14T00:00:00Z
---

# Integral definitions of grad, div and curl

At a point $P$, with $V$ a small volume enclosing $P$ and $S$ its closed
boundary ([Riley et al. (2006)](/sources/riley-2006.md), §11.7,
eqs. (11.14)–(11.17), p. 398):

$$\nabla\phi=\lim_{V\to0}\frac1V\oint_S\phi\,d\mathbf S,\qquad \nabla\cdot\mathbf v=\lim_{V\to0}\frac1V\oint_S\mathbf v\cdot d\mathbf S,\qquad \nabla\times\mathbf v=\lim_{V\to0}\frac1V\oint_S d\mathbf S\times\mathbf v,$$

and, with $C$ a plane contour of area $A$ round $P$ and unit normal $\hat{\mathbf n}$,

$$(\nabla\times\mathbf v)\cdot\hat{\mathbf n}=\lim_{A\to0}\frac1A\oint_C\mathbf v\cdot d\mathbf x.$$

The book proposes these as the geometrical *definitions* of the
operators, independent of any coordinate system, and with $\mathbf v=\nabla\phi$
also $\nabla^2\phi=\lim_{V\to0}\frac1V\oint_S\nabla\phi\cdot d\mathbf S$ (p. 400).

**Scope of what is proved** ("it may be shown, in any coordinate system,
that all the above equations are consistent with our definitions", p. 398):

* gradient: shown only in Cartesian coordinates, on a rectangular element
  $\Delta x\,\Delta y\,\Delta z$ (worked example, pp. 398–399); the
  curvilinear proof is stated to need complicated manipulation of the
  base-vector derivatives and is omitted;
* divergence: shown for orthogonal curvilinear coordinates on the element
  $h_1h_2h_3\Delta\xi^1\Delta\xi^2\Delta\xi^3$, whose paired faces
  $\xi^1=$ const contribute $\partial_1(\hat v_1h_2h_3)\Delta\xi^1\Delta\xi^2\Delta\xi^3$
  (p. 399), giving eq. (10.61) ([divergence](/definitions/divergence.md));
* curl: shown for orthogonal coordinates from the circulation round the face
  $h_2h_3\Delta\xi^2\Delta\xi^3$ (p. 400) ([curl](/definitions/curl.md)).

Non-orthogonal coordinates are not treated in this section; there the
book's route is the tensor form of §26.20.

[Arfken et al. (2013)](/sources/arfken-2013.md) do not state the limits as definitions,
but derive the differential forms by the same element-level bookkeeping,
which agrees with the scope above: the Cartesian divergence from the net
outflow through the faces of a parallelepiped $dx\,dy\,dz$ (eq. (3.55),
p. 148), the Cartesian curl from the circulation round a small rectangle
(eq. (3.60), p. 151), and the orthogonal-coordinate divergence and curl from
the outflow of a curvilinear volume element and the circulation round a
curvilinear face element, with scale factors evaluated on the displaced faces
and edges (eqs. (3.140)–(3.143), pp. 185–187). Both books thus obtain the
orthogonal divergence and curl from flux and circulation, and neither does
so for non-orthogonal coordinates, where Arfken too switches to the tensor
forms (§4.3).

These limits are the bridge from the differential operators to the
[divergence theorem](/results/divergence-theorem.md) and
[Stokes' theorem](/results/stokes-theorem.md), whose derivations in the
source sum them over a partition of the domain. Read backwards, the
cell-averaged divergence $\frac{1}{V}\oint_S\mathbf v\cdot d\mathbf S$ of a
finite cell is the quantity a finite-volume scheme evolves (compiler's
remark; the source does not discuss discretization).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §11.7, pp. 398–400; §§11.8–11.9, pp. 401, 406.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.5, pp. 147–151; §3.10, pp. 185–187.
