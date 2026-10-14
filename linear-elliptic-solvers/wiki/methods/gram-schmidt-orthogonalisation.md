---
type: Method
title: "Gram–Schmidt orthogonalisation"
description: "Sequential construction of an orthonormal set from linearly independent vectors or functions by subtracting projections onto the already-normalised predecessors; used for degenerate eigenspaces of normal matrices and Hermitian operators and to build orthonormal polynomial bases."
status: established
aliases: [Gram-Schmidt, Gram-Schmidt process, classical Gram-Schmidt]
tags: [linear-algebra, orthogonalisation, function-space]
timestamp: 2026-10-14T00:00:00Z
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
[Arfken et al. (2013)](/sources/arfken-2013.md) give the identical
recursion for functions and for column vectors (§5.2, eqs. 5.33–5.39,
pp. 269–270; Example 5.2.2, p. 273) and add that the result depends on the
order in which the input vectors are taken (p. 270).

**As a matrix transformation** (Arfken et al., Example 5.6.1, p. 293).
Because $\hat{\mathbf z}_m$ involves only $\mathbf y_1,\dots,\mathbf y_m$,
$\hat{\mathbf z}_m=\sum_{l\le m}\Theta_{lm}\mathbf y_l$ with $\Theta$ upper
triangular, and orthonormality reads $\Theta^{\mathsf H}\Gamma\Theta=I$
for the Gram matrix $\Gamma_{ij}=\langle\mathbf y_i,\mathbf y_j\rangle$, so
$\Gamma=(\Theta\Theta^{\mathsf H})^{-1}$ (eqs. 5.79–5.80). The matrix of
scalar products $\langle\mathbf y_i,\mathcal A\mathbf y_j\rangle$ of an
operator becomes $\Theta^{\mathsf H}(\cdot)\Theta$ in the orthonormal
basis, which is not a similarity transformation (eq. 5.81; see the
Contradictions entry on the
[eigenvalue problem](/definitions/eigenvalue-problem.md) page).
*Compiler's note (status: hypothesis).* $\Gamma=(\Theta^{-1})^{\mathsf H}\Theta^{-1}$
with $\Theta^{-1}$ upper triangular is a Cholesky factorisation of the
positive definite Gram matrix (see [LU decomposition](/methods/lu-decomposition.md));
neither source makes the connection.

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
  first three Legendre polynomials (p. 558). Arfken et al. carry the same
  example to the normalised $\sqrt{(2n+1)/2}\,P_n$ (eq. 5.41) and tabulate
  the classical families obtained from the powers $x^n$ by changing the
  interval and weight (table 5.1, p. 272), while calling the process "a
  possible but very cumbersome method" for generating them (p. 271);
  Riley et al. call it "laborious".
* Arfken et al. use it, as Riley et al. do, to orthogonalise degenerate
  eigenvectors of a Hermitian matrix (§6.3, p. 311; Example 6.2.3) and of a
  Hermitian operator (§8.5, item 6, p. 398).

Both sources treat the process in exact arithmetic only; its loss of
orthogonality in floating point, and the modified variant, are not
discussed.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.13.1 (p. 275), §17.1
  (pp. 557–558), §17.3.2 (p. 562).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §5.2 (pp. 269–273), §5.6
  (p. 293), §6.2 (p. 308), §6.3 (p. 311).
