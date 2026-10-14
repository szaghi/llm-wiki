---
type: Result
title: "Stokes' theorem"
description: "For a vector field on a two-sided open surface S with perimeter C, ∫_S (∇×v)·dS = ∮_C v·dx; with the corollaries ∫_S dS×∇φ = ∮_C φ dx and ∫_S (dS×∇)×b = ∮_C dx×b, and a tensor form."
status: established
aliases: [Kelvin-Stokes theorem, curl theorem]
tags: [integral-theorems, vector-calculus]
timestamp: 2026-10-14T00:00:00Z
---

# Stokes' theorem

**Statement** ([Riley et al. (2006)](/sources/riley-2006.md), §11.9,
eq. (11.23), p. 406). For a two-sided open surface $S$ bounded by the closed
curve $C$, with $d\mathbf S$ oriented right-handedly with the traversal of
$C$ ([vector area element](/definitions/vector-area-element.md)),

$$\int_S(\nabla\times\mathbf v)\cdot d\mathbf S=\oint_C\mathbf v\cdot d\mathbf x.$$

It holds for simply and multiply connected two-sided open surfaces.
[Arfken et al. (2013)](/sources/arfken-2013.md) state the same theorem (§3.8, eq. (3.92),
p. 167) with the perimeter written $\partial S$; in their forms chapter it
is the case $p=2$, $D=3$ of [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md),
stated there for a simply connected surface (Example 4.7.2, eq. (4.114),
p. 247) — a stronger hypothesis than Riley's, recorded as a qualification on
that page.

**Argument given** (p. 406): divide $S$ into small areas, apply the
circulation definition of the [curl](/definitions/curl.md),
$(\nabla\times\mathbf v)\cdot\hat{\mathbf n}_iS_i\approx\oint_{C_i}\mathbf v\cdot d\mathbf x$
(eq. (11.17)); interior edges are traversed twice in opposite directions and
cancel, leaving $C$. Arfken et al. give the same argument on a network of
small rectangles, using their circulation formula (3.60) for each
(eqs. (3.91)–(3.92), p. 167, fig. 3.16), and note that the sign of the line
integral and the direction of $d\mathbf S$ both follow from the direction of
traversal, "so consistent results will always be obtained".

**Corollaries** (eqs. (11.24)–(11.25), p. 407; by $\mathbf v=\phi\mathbf c$
and $\mathbf v=\mathbf b\times\mathbf c$ with $\mathbf c$ constant):

$$\int_S d\mathbf S\times\nabla\phi=\oint_C\phi\,d\mathbf x,\qquad \int_S(d\mathbf S\times\nabla)\times\mathbf b=\oint_C d\mathbf x\times\mathbf b.$$

The same two corollaries are Arfken eqs. (3.94)–(3.95) (p. 168), by the
same arbitrary-vector technique. Arfken et al. add: for a **closed** surface
there is no perimeter, so $\oint_S(\nabla\times\mathbf v)\cdot d\mathbf S=0$
(eq. (3.93), p. 167); and, worked in spherical coordinates for a disk and a
hemisphere sharing the unit circle as perimeter, both surface integrals
equal the line integral — "Stokes' theorem is indifferent to features of the
surface other than its perimeter", because the curl is solenoidal
(Example 3.10.5, pp. 193–194).

With $\mathbf b=\mathbf x$ the second gives the vector area
$\mathbf S=\frac12\oint_C\mathbf x\times d\mathbf x$ (p. 408;
[closed-surface vector area](/results/closed-surface-vector-area.md)). In the
plane, Stokes' theorem reduces to
[Green's theorem in the plane](/results/greens-theorem-in-the-plane.md)
(p. 407). It is the step (3)⇒(1) in the characterisation of a
[conservative vector field](/definitions/conservative-vector-field.md), and it
converts integral circulation laws into differential ones (§11.9.2,
p. 408). Line singularities are admitted with a delta function
($\nabla\times\mathbf u=2\pi\delta(R)$ for the line vortex, p. 409).

**Tensor form** (§26.13, p. 955; stated by extension):
$\int_S\varepsilon_{ijk}\,\partial v_k/\partial x_j\,\hat n_i\,dS=\oint_Cv_k\,dx_k$,
and with $v_k$ replaced by any Cartesian tensor component carrying the index
$k$ ([Levi-Civita symbol](/definitions/levi-civita-symbol.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §11.9, pp. 406–409; §26.13, p. 955.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.8, pp. 167–168; Example 3.10.5, pp. 193–194; §4.7, p. 247; exercises 3.8.3, 3.8.7, 3.8.8, 3.8.13, pp. 169–170.
