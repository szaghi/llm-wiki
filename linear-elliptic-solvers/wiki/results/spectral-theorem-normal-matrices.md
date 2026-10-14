---
type: Result
title: "Spectral theorem for normal matrices"
description: "A normal matrix has an orthonormal basis of eigenvectors and is unitarily diagonalisable, A = sum lambda_k q_k q_k^H; Hermitian eigenvalues are real, anti-Hermitian imaginary, unitary of unit modulus; two normal matrices share an eigenbasis iff they commute."
status: established
aliases: [spectral decomposition, unitary diagonalisation, simultaneous eigenvectors, simultaneous diagonalisation, commuting matrices, functions of a Hermitian matrix]
tags: [linear-algebra, eigenproblem, matrix-class]
timestamp: 2026-10-14T00:00:00Z
---

# Spectral theorem for normal matrices

**Statement.** Let $A$ be normal, $AA^{\mathsf H}=A^{\mathsf H}A$ (see
[matrix classes](/definitions/linear-operators-and-matrices.md)).

1. If $A\mathbf q=\lambda\mathbf q$ then $A^{\mathsf H}\mathbf q=\bar\lambda\mathbf q$
   (proof: $B=A-\lambda I$ is normal, so $\lVert B\mathbf q\rVert=\lVert B^{\mathsf H}\mathbf q\rVert$)
   (eqs. 8.69–8.71).
2. Eigenvectors of distinct eigenvalues are orthogonal,
   $(\lambda_i-\lambda_j)\,\mathbf q_i^{\mathsf H}\mathbf q_j=0$ (eq. 8.76);
   within a degenerate eigenspace an orthogonal set is built by
   [Gram–Schmidt](/methods/gram-schmidt-orthogonalisation.md).
3. These $N$ orthonormal eigenvectors are **complete** — stated, the proof
   being "beyond the scope of this book" (p. 275) — so any
   $\mathbf y=\sum_k(\mathbf q_k^{\mathsf H}\mathbf y)\,\mathbf q_k$ (eq. 8.79), and
   $$A=\sum_{k=1}^N\lambda_k\,\mathbf q_k\mathbf q_k^{\mathsf H}\quad\text{(eq. 8.80)},\qquad Q^{\mathsf H}AQ=\Lambda,\ Q\text{ unitary}\quad\text{(§8.16)}.$$

([Riley et al. (2006)](/sources/riley-2006.md), §8.13.1, pp. 273–276.)

[Arfken et al. (2013)](/sources/arfken-2013.md) prove items 1 and 2 by the
same argument — $(A-\lambda I)\mathbf q=\mathbf 0$ and normality give
$\lVert(A^{\mathsf H}-\bar\lambda I)\mathbf q\rVert^2=0$ — and call normal
matrices "the largest class of matrices that can be diagonalized by unitary
transformations", citing Macklin (1984) (§6.5, eqs. 6.32–6.33, pp. 319–320,
footnote 2). For the Hermitian case they assert item 3 as "the total number
of eigenvectors of a Hermitian matrix is equal to its dimension", likewise
without proof, and state the diagonalisation as: there is a unitary $Q$
with $Q^{\mathsf H}AQ=\Lambda$, the columns of $Q$ being the normalised
eigenvectors, unique up to their order and, within a degenerate
eigenspace, up to a unitary mixing (§§6.3–6.4, eqs. 6.23–6.24,
pp. 311–313; their $U$ is $Q^{\mathsf H}$). The spectral decomposition
extends to functions with a power series,
$f(A)=\sum_kf(\lambda_k)\,\mathbf q_k\mathbf q_k^{\mathsf H}$, and to
negative powers when $A$ is non-singular (eqs. 6.25–6.26, p. 315).

**Special classes** (§§8.13.2–8.13.3, pp. 276–278):

* Hermitian $A$: eigenvalues real (also proved directly), eigenvectors of
  distinct eigenvalues orthogonal; likewise for real symmetric $A$.
* anti-Hermitian $A$: eigenvalues pure imaginary or zero.
* unitary $A$: $\lvert\lambda\rvert=1$.

Arfken et al. derive the same three statements from
$A^{\mathsf H}\mathbf q=\bar\lambda\mathbf q$ (§6.3, eqs. 6.17–6.21;
§6.5, p. 320) and add the converse: real eigenvalues with an orthonormal
set of eigenvectors make a matrix Hermitian (exercise 6.4.2, p. 317). A
real non-symmetric matrix cannot be diagonalised by an orthogonal or
unitary transformation (exercise 6.4.3, p. 318); for a non-normal matrix
see the [eigenvalue problem](/definitions/eigenvalue-problem.md).

A non-normal matrix has in general no orthogonal eigenvectors and may be
defective (§8.13.4); see the [eigenvalue problem](/definitions/eigenvalue-problem.md).

## Simultaneous eigenvectors

Two normal matrices have a common set of eigenvectors iff they commute,
$AB=BA$ (§8.13.5, pp. 278–279). The proof is given for distinct
eigenvalues of $A$; for degenerate eigenvalues the book asserts the result
still holds provided one joint set can be formed by linear combination.
Arfken et al. state the result for Hermitian matrices — "a complete set of
eigenvectors in common if and only if they commute" — with the same proof
for a non-degenerate eigenvalue and the same assertion for the degenerate
case; with three matrices, $[A,B]=[A,C]=0$ but $[B,C]\neq0$, one can share
an eigenbasis with $B$ or with $C$, not both (§6.4, pp. 314–315).

The function-space analogue — real eigenvalues, orthogonal and complete
eigenfunctions — is on the [Hermitian operator](/definitions/hermitian-operator.md)
page.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.13 (pp. 272–279),
  §8.16 (p. 286).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §6.3 (pp. 310–311), §6.4
  (pp. 311–318), §6.5 (pp. 319–320).
