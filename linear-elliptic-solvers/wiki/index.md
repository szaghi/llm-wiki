---
okf_version: "0.1"
---

# linear-elliptic-solvers — Knowledge Bundle

Linear algebra for discretized PDEs and the solution of elliptic problems: vector spaces and operators, eigenproblems, Hermitian and Sturm-Liouville theory, direct and iterative solvers (relaxation, Krylov, multigrid, preconditioning), Poisson and Helmholtz problems with Green's functions and isolated boundary conditions.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page, and the [update log](/log.md).

**Corpus:** 2 sources, both scoped reads — [Riley, Hobson & Bence (2006)](/sources/riley-2006.md),
Chs. 8, 17, §21.5, §§27.1–27.3 and §27.8; [Arfken, Weber & Harris (2013)](/sources/arfken-2013.md),
Chs. 2, 5, 6, 8 and 10. Citation record: [bibliography](/bibliography.md).
Where the two books differ, the concept pages record a qualification or a
`Contradictions` entry (one open, on the
[matrix eigenvalue problem](/definitions/eigenvalue-problem.md) page).

## Reading guide

**1. The discrete problem and its solvability.** Start from the
[inner-product space](/definitions/inner-product-space.md) and
[linear operators and matrices](/definitions/linear-operators-and-matrices.md)
(including the normal/Hermitian/unitary classes), then
[solvability of linear systems](/results/solvability-of-linear-systems.md)
(rank–nullity, existence and uniqueness of $A\mathbf x=\mathbf b$).

**2. Spectral structure.** The [matrix eigenvalue problem](/definitions/eigenvalue-problem.md)
(similarity, diagonalisation, the Jacobi eigenvalue method), the
[spectral theorem for normal matrices](/results/spectral-theorem-normal-matrices.md),
[quadratic and Hermitian forms](/definitions/quadratic-and-hermitian-forms.md)
(positive definiteness, Rayleigh quotient and its eigenvalue bounds), the
[variation method](/methods/variation-method.md) for the lowest eigenvalue,
and the
[singular value decomposition](/methods/singular-value-decomposition.md)
(rank, minimum-norm least squares).

**3. Direct solvers.** [Gaussian elimination with interchange](/methods/gaussian-elimination.md),
[LU decomposition](/methods/lu-decomposition.md) (with Cholesky), the
O(N) [tridiagonal solver](/methods/tridiagonal-solver.md); for small
systems the [determinant and Cramer's rule](/definitions/determinant.md).

**4. Iterative solvers.** [Convergence of fixed-point iteration](/results/fixed-point-iteration-convergence.md)
(order of convergence; scalar case only), [Gauss–Seidel iteration](/methods/gauss-seidel-iteration.md)
(with its Jacobi form; no convergence theory yet in the corpus), and
[relaxation for Laplace's equation](/methods/laplace-relaxation.md) on the
[five-point discrete Laplacian](/operators/five-point-laplacian.md).
Scalar root finding: [Newton–Raphson](/methods/newton-raphson-method.md).

**5. Continuum operator theory.** [Adjoint and Hermitian differential operators](/definitions/hermitian-operator.md),
the [Sturm–Liouville problem](/definitions/sturm-liouville-problem.md)
(the two books' sign and weight conventions mapped there),
[eigenfunction expansion](/methods/eigenfunction-expansion.md) and
[Gram–Schmidt orthogonalisation](/methods/gram-schmidt-orthogonalisation.md).

**6. Elliptic problems and Green's functions.** The
[Poisson boundary-value problem](/definitions/poisson-boundary-value-problem.md)
(Dirichlet, Neumann, free space), the [Green's function](/definitions/greens-function.md)
(one-dimensional construction, fundamental solutions of the Laplace,
Helmholtz and modified Helmholtz operators, the sign convention),
[Green's representation formula](/results/greens-representation-formula.md),
and the [method of images](/methods/method-of-images.md).

**Not yet in the corpus:** SOR, Krylov methods, multigrid, preconditioning,
FFT and fast Green's-function solvers, and the convergence theory of
stationary linear iterations. They wait for their sources.
