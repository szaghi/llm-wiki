---
type: Method
title: "Gram–Schmidt orthogonalisation"
description: "Sequential construction of an orthonormal set from linearly independent vectors or functions by subtracting projections onto the already-normalised predecessors; used for degenerate eigenspaces of normal matrices and Hermitian operators and to build orthonormal polynomial bases."
status: established
aliases: [Gram-Schmidt, Gram-Schmidt process, classical Gram-Schmidt]
tags: [linear-algebra, orthogonalisation, function-space]
timestamp: 2026-10-13T00:00:00Z
---

# Gram–Schmidt orthogonalisation

**Method.** Given linearly independent $\mathbf y_1,\dots,\mathbf y_k$ in an
[inner-product space](/definitions/inner-product-space.md), set
$$\mathbf z_1=\mathbf y_1,\qquad\mathbf z_m=\mathbf y_m-\sum_{l=1}^{m-1}\langle\hat{\mathbf z}_l,\mathbf y_m\rangle\,\hat{\mathbf z}_l,\qquad\hat{\mathbf z}_m=\frac{\mathbf z_m}{\lVert\mathbf z_m\rVert},$$
normalising each $\mathbf z_m$ before the next is formed. Each
$\mathbf z_m$ is orthogonal to all its predecessors
([Riley et al. (2006)](/sources/riley-2006.md), §8.13.1, p. 275). The same
recursion with $\langle\cdot,\cdot\rangle_w$ orthogonalises functions
(§17.1, p. 557); if the normalisation is skipped, the projection
coefficients must be divided by $\lVert\mathbf z_l\rVert^2$.

**Uses in the source.**

* Degenerate eigenspace of a normal matrix: the $\mathbf z_m$ are
  combinations of eigenvectors of one eigenvalue, hence eigenvectors
  themselves, so an orthonormal eigenbasis always exists (§8.13.1;
  [spectral theorem](/results/spectral-theorem-normal-matrices.md)). Riley
  et al. call it "laborious" and prefer, in examples, choosing a simple
  vector in the eigenspace and completing by a cross product (§8.14.1).
* Degenerate eigenvalues of a
  [Hermitian operator](/definitions/hermitian-operator.md) (§17.3.2,
  p. 562), and the null-space columns of $V$ in the
  [SVD](/methods/singular-value-decomposition.md) (p. 305).
* Applied to $1,x,x^2$ on $[-1,1]$ with $w=1$ it yields multiples of the
  first three Legendre polynomials (p. 558).

The source treats the process in exact arithmetic only; its loss of
orthogonality in floating point, and the modified variant, are not
discussed.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.13.1 (p. 275), §17.1
  (pp. 557–558), §17.3.2 (p. 562).
