---
type: Definition
title: "Linear operators and matrices"
description: "Linear operator and its matrix in a basis, matrix algebra, transpose and Hermitian conjugate, trace, inverse, functions of a matrix, and the special square classes: diagonal, triangular, symmetric, orthogonal, Hermitian, unitary and normal."
status: established
aliases: [matrix, Hermitian matrix, unitary matrix, normal matrix, orthogonal matrix, triangular matrix, symmetric matrix, Hermitian conjugate, adjoint matrix, trace, inverse matrix, commutator, Kronecker product, direct product]
tags: [linear-algebra, matrix-class]
timestamp: 2026-10-14T00:00:00Z
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
[Arfken et al. (2013)](/sources/arfken-2013.md) build the same matrix for an
operator on a function space: in an orthonormal basis $\phi_j$,
$\mathcal A\phi_j=\sum_ia_{ij}\phi_i$ with $a_{ij}=\langle\phi_i,\mathcal A\phi_j\rangle$,
and $\mathcal Af=g$ becomes $A\mathbf x=\mathbf y$ for the coefficient
columns, so that the operator is "completely defined by its matrix
elements" (§5.3, eqs. 5.50–5.57, pp. 279–280).

**Algebra** (§8.4, eqs. 8.26–8.37). Sums and scalar multiples act
elementwise; the product is $(AB)_{ij}=\sum_ka_{ik}b_{kj}$, defined when
the column count of $A$ equals the row count of $B$. Multiplication is
associative and distributive but not commutative. The $M\times N$ matrices
themselves form an $MN$-dimensional vector space. Arfken et al. add the
commutator $[A,B]=AB-BA$ (eq. 2.27), the uniqueness of the inverse, and the
remark that square matrices form a ring, not a field, since non-zero
singular matrices exist ($AB=0$ with $A$, $B\neq0$) (§2.2, pp. 97–100).

**Terminology.** Arfken et al. call $A^{\mathsf H}$ the **adjoint** of $A$
(eq. 2.41, p. 105) and write it $A^\dagger$; it is the registry's Hermitian
conjugate, not the adjugate $\operatorname{adj}A$ of the
[determinant](/definitions/determinant.md) page.

**Derived matrices and scalars.**

* Transpose and Hermitian conjugate: $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$,
  $(A_1A_2\cdots A_m)^{\mathsf H}=A_m^{\mathsf H}\cdots A_2^{\mathsf H}A_1^{\mathsf H}$
  (eqs. 8.39–8.40; Arfken et al., eqs. 2.45–2.47, p. 106, with
  $(AB)^{-1}=B^{-1}A^{-1}$).
* Trace: $\operatorname{tr}A=\sum_ia_{ii}$, linear, with
  $\operatorname{tr}AB=\operatorname{tr}BA$ for any $A$, $B$ whether or not
  they commute, hence invariance under cyclic permutation (eqs. 8.43–8.44;
  Arfken et al., eqs. 2.43–2.44, p. 105, who add that every commutator is
  traceless and that non-cyclic permutations change the trace in general).
* Inverse: $AA^{-1}=A^{-1}A=I$, existing iff $\det A\neq0$ (non-singular);
  $(AB)^{-1}=B^{-1}A^{-1}$, $(A^{\mathsf T})^{-1}=(A^{-1})^{\mathsf T}$,
  $(A^{\mathsf H})^{-1}=(A^{-1})^{\mathsf H}$, $\det A^{-1}=1/\det A$
  (§8.10, eqs. 8.53–8.62). The cofactor formula for $A^{-1}$ is on the
  [determinant](/definitions/determinant.md) page.
* Functions of a square matrix: power series $\sum_na_nA^n$, meaningful
  when convergent, e.g. $\exp A=\sum_{n\ge0}A^n/n!$ (§8.5, eq. 8.38;
  Arfken et al. add $\sin A$, $\cos A$, eqs. 2.77–2.79, p. 113). For
  Hermitian $H$, $\exp(\mathrm iH)$ is unitary (Arfken et al., eq. 2.83).
* Direct (Kronecker) product: $A\otimes B$ is the block matrix $(a_{ij}B)$,
  of size $MM'\times NN'$; it is associative, not commutative,
  distributive over addition, and obeys
  $(A\otimes B)(A'\otimes B')=(AA')\otimes(BB')$ (Arfken et al., eqs.
  2.55–2.58, pp. 108–109). Its use for separable discrete operators is not
  discussed.

## Special square matrices (§8.12)

| Class | Defining property | Consequences stated |
|---|---|---|
| diagonal | $a_{ij}=0$ for $i\neq j$ | $\det A=\prod_ia_{ii}$; inverse diagonal; diagonal matrices commute (eq. 8.63) |
| lower/upper triangular | zeros above/below the diagonal | $\det A=\prod_ia_{ii}$ (eq. 8.64); inverse of the same type (stated) |
| symmetric / antisymmetric | $A=\pm A^{\mathsf T}$ | every $A$ splits into symmetric plus antisymmetric parts; antisymmetric of odd order is singular |
| orthogonal | $A^{\mathsf T}=A^{-1}$ (real $A$) | $\det A=\pm1$; preserves the norm of real vectors (eq. 8.65); products of orthogonal matrices are orthogonal (Arfken et al., eqs. 2.49–2.50) |
| Hermitian / anti-Hermitian | $A=\pm A^{\mathsf H}$ | every $A=\tfrac12(A+A^{\mathsf H})+\tfrac12(A-A^{\mathsf H})$; inverse of the same type; real diagonal (Hermitian); for Hermitian $A$, $B$: $AB+BA$ Hermitian, $AB-BA$ anti-Hermitian, $AB$ Hermitian iff $[A,B]=0$ (Arfken et al., eq. 2.53, p. 108; exercise 2.2.37) |
| unitary | $A^{\mathsf H}=A^{-1}$ | $\lvert\det A\rvert=1$; preserves the norm of complex vectors (eq. 8.66); products of unitary matrices are unitary (Arfken et al., eqs. 2.51–2.52, p. 107) |
| normal | $AA^{\mathsf H}=A^{\mathsf H}A$ | includes Hermitian, anti-Hermitian and unitary matrices; inverse normal; Arfken et al. note that normal matrices outside these three classes exist (§6.5, p. 319) |

Normality is the class for which the
[spectral theorem](/results/spectral-theorem-normal-matrices.md) holds;
positive definiteness of a Hermitian matrix is defined by its
[Hermitian form](/definitions/quadratic-and-hermitian-forms.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§8.2–8.8 (pp. 247–259),
  §8.10 (pp. 263–266), §8.12 (pp. 268–272).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §2.2 (pp. 95–114), §5.3
  (pp. 279–282), §6.5 (p. 319).
