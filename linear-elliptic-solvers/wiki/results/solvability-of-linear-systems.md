---
type: Result
title: "Solvability of linear systems"
description: "Rank, range and null space of an M x N matrix, the rank-nullity relation rank A + dim N(A) = N, and the resulting existence and uniqueness criteria for Ax = b: the augmented-matrix rank test, the affine solution set, and the square case det A != 0."
status: established
aliases: [rank-nullity theorem, rank, range, null space, nullity, augmented matrix, Rouche-Capelli]
tags: [linear-algebra, linear-system]
timestamp: 2026-10-13T00:00:00Z
---

# Solvability of linear systems

**Rank.** Two equivalent definitions (§8.11, pp. 267–268): the number of
linearly independent columns of $A$ (the dimension of their span), equal to
the number of independent rows (the row–column equality is stated, with a
reference to Cantrell (2000), ch. 6); or the order of the largest square
submatrix with non-zero determinant. Row or column exchanges, scaling and
adding multiples of one row to another leave the rank unchanged;
$\operatorname{rank}A\le\min(M,N)$, and a square $A$ is singular unless
$\operatorname{rank}A=N$ ([Riley et al. (2006)](/sources/riley-2006.md)).

**Range and null space.** For $A:V\to W$ ($\dim V=N$), the range
$\mathcal R(A)$ is the image subspace, of dimension $\operatorname{rank}A$;
the null space $\mathcal N(A)$ is the subspace mapped to $\mathbf 0$, of
dimension the nullity (§8.18.1, p. 293).

## Rank–nullity

$$\operatorname{rank}A+\dim\mathcal N(A)=N\quad\text{(eq. 8.119)},$$
proved by writing $A\mathbf x=\sum_jx_j\mathbf c_j$ over the columns
$\mathbf c_j$: $\mathcal R(A)$ is their span, and with $r$ independent
columns the remaining $N-r$ coefficients of a null vector are free
(pp. 293–294).

## Existence and uniqueness for $A\mathbf x=\mathbf b$ (pp. 294–295)

* **No solution** unless $\mathbf b\in\mathcal R(A)$, i.e. unless $A$ and
  the augmented matrix $[A\ \mathbf b]$ have the same rank.
* **Unique solution** if $\mathbf b\in\mathcal R(A)$ and
  $\operatorname{rank}A=N$.
* **Infinitely many** if $\mathbf b\in\mathcal R(A)$ and
  $\operatorname{rank}A<N$: any particular solution plus any element of
  $\mathcal N(A)$, an $(N-r)$-dimensional family.
* **Homogeneous** $\mathbf b=\mathbf 0$: only $\mathbf x=\mathbf 0$ if
  $r=N$; otherwise $\mathcal N(A)$. Fewer equations than unknowns ($M<N$)
  always gives infinitely many solutions.
* **Square** $M=N$ (§8.18.2): $r=N$ iff $\det A\neq0$; then the solution is
  unique, $\mathbf x=A^{-1}\mathbf b$.

Solution methods for the square case:
[Gaussian elimination](/methods/gaussian-elimination.md),
[LU decomposition](/methods/lu-decomposition.md), direct inversion and
[Cramer's rule](/definitions/determinant.md); for any $M$, $N$ the
[singular value decomposition](/methods/singular-value-decomposition.md)
gives orthonormal bases of $\mathcal R(A)$ and $\mathcal N(A)$ and the
minimum-norm least-squares solution. The book does not discuss
conditioning or the sensitivity of the solution to perturbations of $A$
and $\mathbf b$.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.11 (pp. 267–268),
  §8.18.1–8.18.2 (pp. 292–295).
