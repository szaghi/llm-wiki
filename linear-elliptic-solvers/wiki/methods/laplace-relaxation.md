---
type: Method
title: "Relaxation for Laplace's equation"
description: "Point relaxation for the five-point discretization of Laplace's equation: guess all interior values, recompute each as the mean of its four current neighbours, and sweep until no value changes significantly; the simplest relaxation method, with a nine-point refinement as an exercise."
status: established
aliases: [relaxation method, point relaxation, iterative Laplace solver]
tags: [iterative-solver, relaxation, poisson, finite-difference]
timestamp: 2026-10-13T00:00:00Z
---

# Relaxation for Laplace's equation

**Method.** For the [five-point discretization](/operators/five-point-laplacian.md)
of $\nabla^2u=0$ with Dirichlet values on the perimeter:

1. guess a complete set of $u_{i,j}$, the boundary values held fixed;
2. with $\beta=1$, recompute each interior $u_{i,j}$ as the mean of the four
   current neighbouring values, i.e. solve eq. 27.88 for $u_{i,j}$;
3. repeat full sweeps over $i,j$ until no value changes significantly.

Riley et al. call it "the simplest of such 'relaxation' methods" and refer
to "specialist books" for faster and more accurate variants
([Riley et al. (2006)](/sources/riley-2006.md), §27.8, p. 1031); no work
is named. A "slightly more sophisticated" scheme is the nine-point
weighted mean of exercise 27.26.

**Which iteration is this?** The text says "the four current values at
neighbouring grid-points" without saying whether values updated earlier in
the same sweep are used. Updated in place, it is the
[Gauss–Seidel iteration](/methods/gauss-seidel-iteration.md) applied to the
five-point system; with all four values from the previous sweep, it is the
simultaneous (Jacobi) form. The text does not decide, and gives no
convergence rate, stopping tolerance or over-relaxation parameter; SOR is
not mentioned.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.8 (p. 1031),
  exercise 27.26 (p. 1038).
