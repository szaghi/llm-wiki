---
type: Method
title: "LU decomposition"
description: "Factorisation A = LU into unit lower and upper triangular factors by equating entries in row-column order, solution of Ax = b by forward and back substitution for many right-hand sides, determinant as the product of the u_ii, and the Cholesky factorisation A = L L^H for positive definite A."
status: established
aliases: [LU factorisation, Doolittle factorisation, forward substitution, back substitution, Cholesky decomposition, Cholesky factorisation]
tags: [linear-algebra, direct-solver, decomposition]
timestamp: 2026-10-13T00:00:00Z
---

# LU decomposition

**Factorisation.** A square $A$ is written
$$A=LU,$$
$L$ lower triangular with unit diagonal, $U$ upper triangular (eq. 8.125).
Writing out the product for $N=3$ (eq. 8.126), the unknown entries are found
by equating with $A$ in the order: row 1 of $U$, column 1 of $L$, row 2 of
$U$, column 2 of $L$, and so on
([Riley et al. (2006)](/sources/riley-2006.md), §8.18.2, pp. 296–297).
Riley et al. say it is "always possible" to take the diagonal of $L$ as
unity; that a non-singular $A$ can need row interchanges for the
factorisation to exist is not stated here (interchange appears only with
[Gaussian elimination](/methods/gaussian-elimination.md)).

**Solve.** $LU\mathbf x=\mathbf b$ splits into two triangular systems,
$$L\mathbf y=\mathbf b\ \text{(forward)},\qquad U\mathbf x=\mathbf y\ \text{(backward)}.$$
Once the factors are known, further right-hand sides cost little; this,
not inversion, is the economical route, since computing $A^{-1}$ is
"computationally demanding, especially when $N$ is large" (p. 296).

**By-products** (p. 298). $A^{-1}$ column by column from
$A\mathbf x=\mathbf e_i$, $i=1,\dots,N$; and
$$\det A=\det L\,\det U=\prod_{i=1}^Nu_{ii}\quad\text{(eq. 8.127)}.$$

## Cholesky decomposition

If $A$ is Hermitian (the book writes "symmetric") and positive
semi-definite, $A=LL^{\mathsf H}$ with $L$ lower triangular whose diagonal
is not in general unity (eq. 8.128; $A=LL^{\mathsf T}$ for real $A$). The
diagonal cannot be fixed because $L$ must carry as many independent entries
as $A$. Necessity of semi-definiteness follows from
$\mathbf x^{\mathsf H}A\mathbf x=\lVert L^{\mathsf H}\mathbf x\rVert^2\ge0$;
a non-singular $A$ must be positive definite, and failure to find $L$ shows
$A$ is not (pp. 298–299; see
[Hermitian forms](/definitions/quadratic-and-hermitian-forms.md)). The
book does not develop the algorithm ("we shall not explore it further").

Operation counts are not given for LU; the general statement that solving
$A\mathbf x=\mathbf b$ costs roughly $N^3$ operations appears in §27.3.3
(p. 998), against linear cost for the
[tridiagonal solver](/methods/tridiagonal-solver.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.18.2 (pp. 296–299),
  §27.3.3 (p. 998).
