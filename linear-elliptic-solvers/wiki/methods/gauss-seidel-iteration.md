---
type: Method
title: "Gauss–Seidel iteration"
description: "Stationary iteration for Ax = b that scales each equation by its diagonal entry and updates the unknowns in order, using each new component as soon as it is available; the simultaneous-update predecessor (Jacobi form) and the source's lack of a convergence criterion."
status: established
aliases: [Gauss-Seidel, Gauss-Seidel method, successive displacement, Jacobi iteration, simultaneous displacement]
tags: [linear-algebra, iterative-solver, relaxation]
timestamp: 2026-10-13T00:00:00Z
---

# Gauss–Seidel iteration

**Motivation.** When only an approximate solution of a large system is
needed, an iteration may reach adequate precision with less work than
[elimination](/methods/gaussian-elimination.md)
([Riley et al. (2006)](/sources/riley-2006.md), §27.3.2, pp. 996–997).

**Construction** (steps (i)–(iii), eqs. 27.23–27.28). Divide each equation
by its diagonal coefficient, so that $A\mathbf x=\mathbf b$ becomes a system
with unit diagonal. In the splitting $A=D-E-F$ of the registry this is
$$\left(I-D^{-1}E-D^{-1}F\right)\mathbf x=D^{-1}\mathbf b .$$

* **Simultaneous update** (eq. 27.26):
  $$\mathbf x^{(k+1)}=D^{-1}(E+F)\,\mathbf x^{(k)}+D^{-1}\mathbf b .$$
  This is the form usually called the Jacobi iteration, iteration matrix
  $T_{\mathrm J}=D^{-1}(E+F)$; the book presents it only as step (ii) and
  does not name it.
* **Gauss–Seidel** (eq. 27.28), "to improve the convergence": split
  $D^{-1}(E+F)$ into its strictly lower part $D^{-1}E$ and strictly upper
  part $D^{-1}F$ and use the newest values,
  $$\mathbf x^{(k+1)}=D^{-1}E\,\mathbf x^{(k+1)}+D^{-1}F\,\mathbf x^{(k)}+D^{-1}\mathbf b .$$
  The implicit-looking term is explicit componentwise: component $i$ of
  $D^{-1}E\,\mathbf x^{(k+1)}$ needs only components $1,\dots,i-1$, already
  computed in the current sweep.

**Example.** For the system of eq. 27.29 (the
[elimination](/methods/gaussian-elimination.md) test, exact solution
$(10,1,2)^{\mathsf T}$), starting from $(2,2,2)^{\mathsf T}$, seven sweeps
give $(10.029,1.004,2.004)^{\mathsf T}$ (table 27.6, p. 998).

## What the source does not provide

No convergence criterion is stated for either form, and none of the
standard sufficient conditions (diagonal dominance, positive definiteness)
appears; the claim that Gauss–Seidel improves on the simultaneous update is
made without proof or qualification. The worked system's first row,
$x_1+6x_2-4x_3=8$, is not diagonally dominant, so its convergence is not
covered by a dominance argument either.

*Compiler's derivation (status: hypothesis, not in the source).* Collecting
terms, eq. 27.28 is
$\mathbf x^{(k+1)}=(D-E)^{-1}F\,\mathbf x^{(k)}+(D-E)^{-1}\mathbf b$, and
the error obeys $\mathbf e^{(k+1)}=T_{\mathrm{GS}}\,\mathbf e^{(k)}$ with
$T_{\mathrm{GS}}=(D-E)^{-1}F$; likewise
$\mathbf e^{(k+1)}=T_{\mathrm J}\,\mathbf e^{(k)}$. Convergence for every
starting vector therefore turns on the powers of $T$ — the matrix analogue
of the scalar condition on the
[fixed-point iteration](/results/fixed-point-iteration-convergence.md)
page. The theorem that this holds iff $\rho(T)<1$ awaits a source.

The PDE use of the same idea is [relaxation](/methods/laplace-relaxation.md)
for the [five-point Laplacian](/operators/five-point-laplacian.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.3.2 (pp. 996–998).
