---
type: Result
title: "Solvability of linear systems"
description: "Rank, range and null space of an M x N matrix, the rank-nullity relation rank A + dim N(A) = N, and the resulting existence and uniqueness criteria for Ax = b: the augmented-matrix rank test, the affine solution set, and the square case det A != 0."
status: established
aliases: [rank-nullity theorem, rank, range, null space, nullity, augmented matrix, Rouche-Capelli]
tags: [linear-algebra, linear-system]
timestamp: 2026-10-14T00:00:00Z
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
[Arfken et al. (2013)](/sources/arfken-2013.md) define the rank of a square
matrix as the number of linearly independent linear forms its rows
describe, $N$ for a non-singular matrix, and defer its systematic
determination to their eigenvalue chapter (§2.2, p. 104), where they state
that a matrix with $m$ zero eigenvalues has rank $N-m$ (§6.4, p. 317).

*Compiler's note on the eigenvalue rank criterion (status: hypothesis).*
With $m$ counted as algebraic multiplicity, the statement holds for
diagonalisable matrices — in particular for the Hermitian matrices of that
section — but not in general: $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ has
the eigenvalue $0$ twice and rank $1$. In general $N-\operatorname{rank}A$
is the geometric multiplicity of the eigenvalue $0$ (rank–nullity below).

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
  unique, $\mathbf x=A^{-1}\mathbf b$. Arfken et al. state the same
  criterion, "A square matrix $A$ is singular if and only if $\det(A)=0$"
  (eq. 2.36, p. 103), and for $\det A=0$ distinguish a homogeneous system
  (a family of solutions, arbitrary in scale), equations with the same
  linear form but different right-hand sides (no solution), and the same
  form with equal right-hand sides (a family of solutions) (§2.1,
  p. 90).

Solution methods for the square case:
[Gaussian elimination](/methods/gaussian-elimination.md),
[LU decomposition](/methods/lu-decomposition.md), direct inversion and
[Cramer's rule](/definitions/determinant.md); for any $M$, $N$ the
[singular value decomposition](/methods/singular-value-decomposition.md)
gives orthonormal bases of $\mathcal R(A)$ and $\mathcal N(A)$ and the
minimum-norm least-squares solution. Riley et al. do not discuss
conditioning or the sensitivity of the solution to perturbations of $A$
and $\mathbf b$. Arfken et al. touch it only in exercise statements: the
Hilbert matrix $\left[(i+j-1)^{-1}\right]$ arising from a polynomial
least-squares fit is "becoming ill-conditioned and unstable" at order 5,
where its determinant is $3.7\times10^{-12}$ (exercise 5.1.3, p. 267;
determinants also in exercise 2.1.5, p. 94). No condition number or
perturbation bound appears in either source; a small determinant is used
as the warning sign, which *the compiler notes (hypothesis)* is not a
scale-invariant measure of conditioning.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.11 (pp. 267–268),
  §8.18.1–8.18.2 (pp. 292–295).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §2.1 (pp. 89–90, 94),
  §2.2 (pp. 103–104), §5.1 (p. 267), §6.4 (p. 317).
