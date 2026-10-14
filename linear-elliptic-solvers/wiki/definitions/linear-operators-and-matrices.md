---
type: Definition
title: "Linear operators and matrices"
description: "Linear operator and its matrix in a basis, matrix algebra, transpose and Hermitian conjugate, trace, inverse, functions of a matrix, and the special square classes: diagonal, triangular, symmetric, orthogonal, Hermitian, unitary and normal."
status: established
aliases: [matrix, Hermitian matrix, unitary matrix, normal matrix, orthogonal matrix, triangular matrix, symmetric matrix, Hermitian conjugate, trace, inverse matrix]
tags: [linear-algebra, matrix-class]
timestamp: 2026-10-13T00:00:00Z
---

# Linear operators and matrices

**Linear operator.** $\mathcal A$ maps each vector $\mathbf x$ to a vector
$\mathcal A\mathbf x$ with
$\mathcal A(\lambda\mathbf a+\mu\mathbf b)=\lambda\mathcal A\mathbf a+\mu\mathcal A\mathbf b$
([Riley et al. (2006)](/sources/riley-2006.md), §8.2). In a basis
$\mathbf e_j$, $\mathcal A\mathbf e_j=\sum_ia_{ij}\mathbf e_i$, and
$\mathbf y=\mathcal A\mathbf x$ reads $y_i=\sum_ja_{ij}x_j$ (eqs. 8.23–8.24).
For $\mathcal A:V\to W$ with $\dim V=N$, $\dim W=M$ the array $A=(a_{ij})$
is $M\times N$ (eq. 8.25). The same operator has different matrices in
different bases; the transformation law is a
[similarity transformation](/definitions/eigenvalue-problem.md).

**Algebra** (§8.4, eqs. 8.26–8.37). Sums and scalar multiples act
elementwise; the product is $(AB)_{ij}=\sum_ka_{ik}b_{kj}$, defined when
the column count of $A$ equals the row count of $B$. Multiplication is
associative and distributive but not commutative. The $M\times N$ matrices
themselves form an $MN$-dimensional vector space.

**Derived matrices and scalars.**

* Transpose and Hermitian conjugate: $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$,
  $(A_1A_2\cdots A_m)^{\mathsf H}=A_m^{\mathsf H}\cdots A_2^{\mathsf H}A_1^{\mathsf H}$
  (eqs. 8.39–8.40).
* Trace: $\operatorname{tr}A=\sum_ia_{ii}$, linear, with
  $\operatorname{tr}AB=\operatorname{tr}BA$ for any $A$, $B$ whether or not
  they commute, hence invariance under cyclic permutation (eqs. 8.43–8.44).
* Inverse: $AA^{-1}=A^{-1}A=I$, existing iff $\det A\neq0$ (non-singular);
  $(AB)^{-1}=B^{-1}A^{-1}$, $(A^{\mathsf T})^{-1}=(A^{-1})^{\mathsf T}$,
  $(A^{\mathsf H})^{-1}=(A^{-1})^{\mathsf H}$, $\det A^{-1}=1/\det A$
  (§8.10, eqs. 8.53–8.62). The cofactor formula for $A^{-1}$ is on the
  [determinant](/definitions/determinant.md) page.
* Functions of a square matrix: power series $\sum_na_nA^n$, meaningful
  when convergent, e.g. $\exp A=\sum_{n\ge0}A^n/n!$ (§8.5, eq. 8.38).

## Special square matrices (§8.12)

| Class | Defining property | Consequences stated |
|---|---|---|
| diagonal | $a_{ij}=0$ for $i\neq j$ | $\det A=\prod_ia_{ii}$; inverse diagonal; diagonal matrices commute (eq. 8.63) |
| lower/upper triangular | zeros above/below the diagonal | $\det A=\prod_ia_{ii}$ (eq. 8.64); inverse of the same type (stated) |
| symmetric / antisymmetric | $A=\pm A^{\mathsf T}$ | every $A$ splits into symmetric plus antisymmetric parts; antisymmetric of odd order is singular |
| orthogonal | $A^{\mathsf T}=A^{-1}$ | $\det A=\pm1$; preserves the norm of real vectors (eq. 8.65) |
| Hermitian / anti-Hermitian | $A=\pm A^{\mathsf H}$ | every $A=\tfrac12(A+A^{\mathsf H})+\tfrac12(A-A^{\mathsf H})$; inverse of the same type |
| unitary | $A^{\mathsf H}=A^{-1}$ | $\lvert\det A\rvert=1$; preserves the norm of complex vectors (eq. 8.66) |
| normal | $AA^{\mathsf H}=A^{\mathsf H}A$ | includes Hermitian, anti-Hermitian and unitary matrices; inverse normal |

Normality is the class for which the
[spectral theorem](/results/spectral-theorem-normal-matrices.md) holds;
positive definiteness of a Hermitian matrix is defined by its
[Hermitian form](/definitions/quadratic-and-hermitian-forms.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§8.2–8.8 (pp. 247–259),
  §8.10 (pp. 263–266), §8.12 (pp. 268–272).
