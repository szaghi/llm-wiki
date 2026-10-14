---
type: Method
title: "Singular value decomposition"
description: "Factorisation A = U Sigma V^H of any M x N matrix into unitary factors and non-negative singular values from the eigenproblems of A^H A and A A^H; gives rank, orthonormal bases of range and null space, and the minimum-norm least-squares solution V Sigma^+ U^H b."
status: established
aliases: [SVD, singular values, pseudo-inverse, Moore-Penrose inverse, least squares, minimum-norm solution]
tags: [linear-algebra, decomposition, least-squares]
timestamp: 2026-10-13T00:00:00Z
---

# Singular value decomposition

**Decomposition.** Any $M\times N$ complex $A$ is written
$$A=U\Sigma V^{\mathsf H},$$
$U$ ($M\times M$) and $V$ ($N\times N$) unitary, $\Sigma$ ($M\times N$)
diagonal with entries $\sigma_1\ge\sigma_2\ge\dots\ge\sigma_p\ge0$,
$p=\min(M,N)$ ([Riley et al. (2006)](/sources/riley-2006.md), §8.18.3,
eq. 8.131). Existence is stated, its proof "beyond the scope of this book",
with a reference to Golub & Van Loan (1996) (footnote, p. 302). Riley et
al. call SVD "the method of choice in analysing any set of simultaneous
linear equations" (p. 302).

**Construction.** From
$A^{\mathsf H}A=V\Sigma^{\mathsf H}\Sigma V^{\mathsf H}$ and
$AA^{\mathsf H}=U\Sigma\Sigma^{\mathsf H}U^{\mathsf H}$ (eqs. 8.132–8.133),
the columns $\mathbf v_k$ of $V$ are the orthonormal eigenvectors of
$A^{\mathsf H}A$, the columns $\mathbf u_k$ of $U$ those of
$AA^{\mathsf H}$, and $\sigma_k^2$ are the eigenvalues of the smaller of the
two Hermitian matrices (the larger has the same plus zeros). Then
$$A\mathbf v_k=\sigma_k\mathbf u_k,\qquad A^{\mathsf H}\mathbf u_k=\sigma_k\mathbf v_k\qquad(k\le p)\quad\text{(eqs. 8.134–8.135)},$$
so $\mathbf v_k=A^{\mathsf H}\mathbf u_k/\sigma_k$ for non-zero $\sigma_k$;
remaining null-space columns are completed by
[Gram–Schmidt](/methods/gram-schmidt-orthogonalisation.md) (p. 305).

**Structure.** With $r$ non-zero singular values,
$A=\sum_{k=1}^r\sigma_k\mathbf u_k\mathbf v_k^{\mathsf H}$ (eq. 8.136):
$\operatorname{rank}A=r$; $\mathbf u_1,\dots,\mathbf u_r$ is an orthonormal
basis of $\mathcal R(A)$; $\mathbf v_{r+1},\dots,\mathbf v_N$ is an
orthonormal basis of $\mathcal N(A)$ (pp. 303–304), consistent with
[rank–nullity](/results/solvability-of-linear-systems.md).

## Solving $A\mathbf x=\mathbf b$

Let $\Sigma^{+}$ be $\Sigma^{\mathsf T}$ with each non-zero $\sigma_k$
replaced by $1/\sigma_k$, and
$$\hat{\mathbf x}=V\Sigma^{+}U^{\mathsf H}\mathbf b\quad\text{(eq. 8.141)}.$$

* If $\mathbf b\in\mathcal R(A)$, $\hat{\mathbf x}$ solves the system
  exactly, since $A\hat{\mathbf x}-\mathbf b=U(\Sigma\Sigma^{+}-I)U^{\mathsf H}\mathbf b=\mathbf 0$
  (eq. 8.142); the general solution adds any combination of
  $\mathbf v_{r+1},\dots,\mathbf v_N$, and $\hat{\mathbf x}$ is the one of
  shortest length ("straightforward to show", not shown). It is unique only
  if $r=N$.
* If $\mathbf b\notin\mathcal R(A)$, $\hat{\mathbf x}$ minimises
  $\lVert A\mathbf x-\mathbf b\rVert$: adding $\mathbf x'$ adds
  $A\mathbf x'\in\mathcal R(A)$, whose $U$-components and those of
  $(\Sigma\Sigma^{+}-I)U^{\mathsf H}\mathbf b$ occupy disjoint index sets, so
  the residual is smallest at $A\mathbf x'=\mathbf 0$ (eq. 8.143, p. 306).

The matrix $V\Sigma^{+}U^{\mathsf H}$ is what is usually called the
Moore–Penrose pseudo-inverse $A^{+}$; the book does not use the name.
Neither the conditioning information carried by $\sigma_1/\sigma_r$ nor
truncation of small singular values is discussed.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.18.3 (pp. 301–307).
