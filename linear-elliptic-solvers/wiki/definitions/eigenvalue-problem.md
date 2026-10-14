---
type: Definition
title: "Matrix eigenvalue problem"
description: "Eigenvalues and eigenvectors of a square matrix: characteristic equation, trace and determinant identities, degeneracy and defective matrices, change of basis by similarity transformation with its invariants, and diagonalisation."
status: established
aliases: [eigenvalue, eigenvector, characteristic equation, secular determinant, similarity transformation, diagonalisation, defective matrix, change of basis]
tags: [linear-algebra, eigenproblem]
timestamp: 2026-10-13T00:00:00Z
---

# Matrix eigenvalue problem

**Definition.** A non-zero $\mathbf q$ with $A\mathbf q=\lambda\mathbf q$ is
an eigenvector of the square matrix $A$ and $\lambda$ its eigenvalue
(eqs. 8.67–8.68). Eigenvectors are fixed only up to a factor and are usually
normalised, $\mathbf q^{\mathsf H}\mathbf q=1$
([Riley et al. (2006)](/sources/riley-2006.md), §8.13, pp. 272–273). If
$A$ is non-singular, $A^{-1}$ has the same eigenvectors with eigenvalues
$1/\lambda_k$ (p. 273).

**Characteristic equation.** $(A-\lambda I)\mathbf q=\mathbf 0$ has a
non-trivial solution only if
$$\det(A-\lambda I)=0,$$
a polynomial of degree $N$ whose $N$ roots are the eigenvalues (§8.14,
eqs. 8.85–8.86). The coefficient of $-\lambda^{N-1}$ gives
$$\sum_k\lambda_k=\operatorname{tr}A\quad\text{(eq. 8.87)},\qquad\prod_k\lambda_k=\det A\quad\text{(eq. 8.103)},$$
the first offered as a necessary, not sufficient, check on computed
eigenvalues. The determinant product is derived for diagonalisable $A$
(§8.16).

**Degeneracy.** An eigenvalue with several independent eigenvectors is
degenerate; any combination of those eigenvectors is again an eigenvector
(eqs. 8.77–8.78). A matrix whose eigenvectors are not linearly independent
is **defective**. Stated without proof: a matrix with $N$ distinct
eigenvalues has $N$ independent eigenvectors; with degenerate eigenvalues a
general matrix may or may not (§8.13.4, p. 278). For normal matrices the
[spectral theorem](/results/spectral-theorem-normal-matrices.md) settles
the question.

## Similarity transformation

Changing basis by $\mathbf e'_j=\sum_iS_{ij}\mathbf e_i$ ($S$ non-singular)
transforms components as $\mathbf x=S\mathbf x'$ and the operator matrix as
$$A'=S^{-1}AS\quad\text{(eqs. 8.90–8.94)}.$$
Basis-independent properties are invariant (eqs. 8.95–8.98): $I'=I$,
$\det A'=\det A$, the characteristic polynomial and hence the eigenvalues,
and $\operatorname{tr}A'=\operatorname{tr}A$. If $S$ is unitary,
$A'=S^{\mathsf H}AS$, an orthonormal basis stays orthonormal, and
(anti-)Hermitian and unitary matrices keep their class (eqs. 8.99–8.100)
(§8.15, pp. 282–285).

## Diagonalisation

With the eigenvectors as columns, $Q=[\mathbf q_1\ \cdots\ \mathbf q_N]$,
$$Q^{-1}AQ=\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_N),$$
possible iff the $N$ eigenvectors are independent; a defective matrix
cannot be diagonalised (§8.16, pp. 285–286). Normal matrices are
diagonalised by a unitary $Q$. Consequences: $(Q^{-1}AQ)^n=Q^{-1}A^nQ$, and
the trace formula $\det(\exp A)=\exp(\operatorname{tr}A)$ (eq. 8.104),
proved for diagonalisable $A$.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.13 (pp. 272–279),
  §8.14 (pp. 280–282), §§8.15–8.16 (pp. 282–288).
