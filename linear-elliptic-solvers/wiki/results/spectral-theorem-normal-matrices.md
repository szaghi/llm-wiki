---
type: Result
title: "Spectral theorem for normal matrices"
description: "A normal matrix has an orthonormal basis of eigenvectors and is unitarily diagonalisable, A = sum lambda_k q_k q_k^H; Hermitian eigenvalues are real, anti-Hermitian imaginary, unitary of unit modulus; two normal matrices share an eigenbasis iff they commute."
status: established
aliases: [spectral decomposition, unitary diagonalisation, simultaneous eigenvectors, commuting matrices]
tags: [linear-algebra, eigenproblem, matrix-class]
timestamp: 2026-10-13T00:00:00Z
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

**Special classes** (§§8.13.2–8.13.3, pp. 276–278):

* Hermitian $A$: eigenvalues real (also proved directly), eigenvectors of
  distinct eigenvalues orthogonal; likewise for real symmetric $A$.
* anti-Hermitian $A$: eigenvalues pure imaginary or zero.
* unitary $A$: $\lvert\lambda\rvert=1$.

A non-normal matrix has in general no orthogonal eigenvectors and may be
defective (§8.13.4); see the [eigenvalue problem](/definitions/eigenvalue-problem.md).

## Simultaneous eigenvectors

Two normal matrices have a common set of eigenvectors iff they commute,
$AB=BA$ (§8.13.5, pp. 278–279). The proof is given for distinct
eigenvalues of $A$; for degenerate eigenvalues the book asserts the result
still holds provided one joint set can be formed by linear combination.

The function-space analogue — real eigenvalues, orthogonal and complete
eigenfunctions — is on the [Hermitian operator](/definitions/hermitian-operator.md)
page.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.13 (pp. 272–279),
  §8.16 (p. 286).
