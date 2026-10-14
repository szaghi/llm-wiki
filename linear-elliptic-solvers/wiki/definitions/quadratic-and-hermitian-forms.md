---
type: Definition
title: "Quadratic and Hermitian forms"
description: "Quadratic form x^T A x and Hermitian form x^H A x, reduction to a sum of squares by the eigenvector basis, positive definite and semi-definite matrices, stationarity of the Rayleigh quotient at eigenvectors, and quadratic surfaces."
status: established
aliases: [positive definite matrix, positive semi-definite, SPD, Rayleigh quotient, quadratic form, Hermitian form, principal axes]
tags: [linear-algebra, eigenproblem, positive-definite]
timestamp: 2026-10-14T00:00:00Z
---

# Quadratic and Hermitian forms

**Definition.** A quadratic form is the real scalar
$\mathbf x^{\mathsf T}A\mathbf x$ of a real vector; only the symmetric part
of $A$ contributes, since $\mathbf x^{\mathsf T}B\mathbf x=0$ for
antisymmetric $B$, so $A=A^{\mathsf T}$ may be assumed (eqs. 8.105–8.109).
The complex analogue is the Hermitian form $\mathbf x^{\mathsf H}A\mathbf x$
with $A=A^{\mathsf H}$, which is real (eq. 8.112)
([Riley et al. (2006)](/sources/riley-2006.md), §8.17, pp. 288–290).

**Sum of squares.** In the orthonormal eigenvector basis of symmetric $A$
($\mathbf x=Q\mathbf x'$, $Q$ orthogonal),
$$\mathbf x^{\mathsf T}A\mathbf x=\sum_k\lambda_k\,(x'_k)^2,$$
with no cross terms (eq. 8.110).

## Positive definiteness

$A=A^{\mathsf H}$ is **positive definite** if $\mathbf x^{\mathsf H}A\mathbf x>0$
for all $\mathbf x\neq\mathbf 0$, equivalently all its eigenvalues are
positive; **positive semi-definite** if $\mathbf x^{\mathsf H}A\mathbf x\ge0$,
allowing zero eigenvalues (p. 290). A non-singular positive semi-definite
matrix is positive definite, since a zero eigenvalue makes $\det A=0$
(pp. 298–299). [Arfken et al. (2013)](/sources/arfken-2013.md) define
positive definiteness by the eigenvalues ("If all the eigenvalues of an
operator $\mathcal A$ are positive, it is termed positive definite") and
derive the form criterion from the bound below (§6.4, p. 317); they add
that a Gram (overlap) matrix of independent vectors is positive definite
(Example 6.4.2) and that $m$ zero eigenvalues of a singular matrix signal
rank $N-m$ (p. 317; see the compiler's note on the
[solvability](/results/solvability-of-linear-systems.md) page). Positive definiteness is the condition under which the
Cholesky factorisation $A=LL^{\mathsf H}$ of the
[LU decomposition](/methods/lu-decomposition.md) page exists.

## Rayleigh quotient

Stationarising $\mathbf x^{\mathsf T}A\mathbf x$ under
$\mathbf x^{\mathsf T}\mathbf x=1$ by a Lagrange multiplier gives
$A\mathbf x=\lambda\mathbf x$, and the stationary value is $\lambda$
(eqs. 8.113–8.115). Equivalently, the Rayleigh quotient
$$R_A(\mathbf x)=\frac{\mathbf x^{\mathsf T}A\mathbf x}{\mathbf x^{\mathsf T}\mathbf x}$$
has variation
$\Delta R_A=\frac{2}{\mathbf x^{\mathsf T}\mathbf x}\,\Delta\mathbf x^{\mathsf T}\left[A\mathbf x-R_A(\mathbf x)\,\mathbf x\right]$,
so $R_A$ is stationary exactly at eigenvectors, where it equals the
eigenvalue (§8.17.1, pp. 290–291). Proved for real symmetric $A$; "similar
results hold for Hermitian matrices" is stated. Riley et al. do not state
the min–max characterisation (extreme eigenvalues as the extrema of $R_A$).

**Bounds** (Arfken et al., §6.4, eqs. 6.28–6.31, p. 316). Expanding
$\mathbf x=\sum_kc_k\mathbf q_k$ in the orthonormal eigenvectors of
Hermitian $A$,
$$R_A(\mathbf x)=\frac{\sum_k\lvert c_k\rvert^2\lambda_k}{\sum_k\lvert c_k\rvert^2},$$
a weighted mean of the eigenvalues with non-negative weights, hence
$\lambda_{\min}\le R_A(\mathbf x)\le\lambda_{\max}$ (also exercise 6.5.5,
p. 325), with $R_A(\mathbf x)=\lambda_{\min}$ only for an eigenvector of
$\lambda_{\min}$. This is the extremal half of min–max — the extreme
eigenvalues are the minimum and maximum of $R_A$ — not the full
characterisation of the intermediate eigenvalues, which neither source
states. An approximate eigenvector whose components along the other
eigenvectors are small gives an error in the Rayleigh quotient of the
order of their squares (exercise 6.5.18, statement,
p. 327); the same bound for operators is the
[variation method](/methods/variation-method.md).

**Quadratic surfaces.** $\mathbf x^{\mathsf T}A\mathbf x=1$ has principal
axes along the eigenvectors, with squared principal radii $1/\lambda_k$; all
$\lambda_k>0$ gives an ellipsoid (§8.17.2, p. 292).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.17 (pp. 288–292),
  §8.18.2 (pp. 298–299).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §6.4 (pp. 316–317),
  §6.5 (exercises 6.5.5, 6.5.18, pp. 325–327).
