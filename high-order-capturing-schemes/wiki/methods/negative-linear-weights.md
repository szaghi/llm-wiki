---
type: Method
title: "Negative linear weights in WENO and their treatment"
description: "When accuracy fixes the linear weights, some can be negative or fail to exist (at some target points, for derivatives and integrals, on unstructured meshes); the WENO convex combination then loses its non-oscillatory property. The remedies are the Shi–Hu–Shu splitting into two positive-weight sums, or giving up the big-stencil order for freely chosen positive weights."
status: established
aliases: [negative weights, Shi–Hu–Shu technique, positive linear weights]
tags: [weno, linear-weights, unstructured, nonlinear-weights]
timestamp: 2026-10-13T00:00:00Z
---

# Negative linear weights in WENO and their treatment

**The problem** ([Shu (2009)](/sources/shu-2009.md), §§2.3.3, 3.5.5;
[Shu (2020)](/sources/shu-2020.md), §3.2.2). The linear weights $d_k$ of
[WENO](/methods/weno.md) are fixed uniquely by requiring the combination
of candidates to reproduce the big-stencil value. Depending on the target
point, the weights can be negative, or not exist at all. A combination of
monotone approximations with negative coefficients need not be monotone,
so unmodified WENO then oscillates or becomes unstable.
* For WENO *interpolation* of point values the linear weights always exist
  and are positive, wherever the target lies in the cell (Carlini,
  Ferretti and Russo, as cited by Shu 2020, §3.2.2). The big-stencil
  interpolant is a combination of the candidate interpolants with
  polynomial weights that are non-negative on the common interval (cited
  by Shu 2009, §2.3.1).
* *Reconstruction* weights can be negative at some points. At fifth
  order the linear weights for the midpoint node of three-point Gauss
  quadrature are negative, which is why 4-point Gauss–Lobatto nodes are
  used for 2D FV-WENO edges
  ([Ding & Wu (2024)](/sources/ding-2024.md), §2.2.2). The two Gauss points
  of fourth-order quadrature happen to have positive weights at $r = 3$
  ([finite-volume reconstruction](/methods/finite-volume-reconstruction.md)).
* *Derivatives and integrals* often have negative weights. A cell integral
  from point values has $d = (-\tfrac{17}{240}, \tfrac{137}{120}, -\tfrac{17}{240})$
  (Shu 2009, §2.3.4).
* On *unstructured meshes* the optimal weights depend on the local mesh,
  are hard to build, and can be negative (Shu 2009, §3.5.5).

**Remedy 1: split.** Shi, Hu and Shu write the combination as the
difference of two combinations with positive weights and apply WENO
weights to each. This is used for central WENO, staggered finite
differences, non-conservative systems and well-balanced schemes (Shu
2009, §2.3.3; Shu 2020, §3.2.2).

**Remedy 2: give up order.** Any set of positive linear weights can be
used if one accepts the order of the small stencils, e.g. equal weights or
the largest on the most central stencil. This suits moving and
unstructured meshes (Shu 2009, §2.3.3; Shu 2020, §§3.2.2–3.3). Two
designs avoid the loss:
* [polynomial WENO](/methods/polynomial-weno.md) blends whole candidates of
  the full degree $K$, each on a stencil wide enough for it, so each is
  already of full order. Shu lists Dumbser and Käser among the
  order-sacrificing schemes (Shu 2020, p. 722); the two statements agree,
  because the order given up is only that of the union of the candidate
  stencils, never the degree-$K$ order of each candidate;
* [unequal-stencil WENO](/methods/weno-ao.md) blends one large polynomial
  with small ones through a weight-adjusted subtraction, so any positive
  weights keep the large stencil's order. Shu traces this device to
  central WENO (Levy, Puppo and Russo) and advocates its multi-resolution
  form for unstructured meshes, derivatives and integrals (Shu 2020,
  §3.2.3; [multi-resolution WENO](/methods/multi-resolution-weno.md)).

# Citations

1. [Shu (2009)](/sources/shu-2009.md), §§2.3.1, 2.3.3, 2.3.4, 3.5.5.
2. [Shu (2020)](/sources/shu-2020.md), §§3.2.2–3.3.
3. [Ding & Wu (2024)](/sources/ding-2024.md), §2.2.2 (arXiv v1).
