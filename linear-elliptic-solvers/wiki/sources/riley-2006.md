---
type: Source
title: "Riley, Hobson & Bence (2006) — Mathematical Methods for Physics and Engineering, 3rd ed."
description: "Undergraduate-to-graduate textbook of mathematical methods; this bundle reads its chapters on matrices and vector spaces, eigenfunction methods, Green's functions for inhomogeneous PDEs, and the numerical sections on equations, iteration, simultaneous linear equations and PDEs."
resource: "doi:10.1017/CBO9780511810763"
source_kind: book
authors: [Riley K.F., Hobson M.P., Bence S.J.]
year: 2006
venue: "Cambridge University Press (3rd ed.)"
local_file: "/home/stefano/papers/mosaic/linear-elliptic-solvers/2006-CUP-Riley-101017CBO9780511810763.pdf"
tags: [textbook, linear-algebra, operator-theory, greens-function, poisson, direct-solver, iterative-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A comprehensive textbook (over 1300 pages) of mathematical methods for
physicists and engineers. Identity verified from the title and copyright
pages and on Crossref (type monograph, edition 3; hardback ISBN
978-0-521-86153-3, paperback 978-0-521-67971-8). The PDF is a scanned print
with a text layer; PDF page = printed page + 30.

**Scoped read.** Read: the contents, the three prefaces (from p. xx),
Ch. 8 *Matrices and vector spaces* §§8.1–8.18 (pp. 241–307), Ch. 17
*Eigenfunction methods for differential equations* §§17.1–17.6
(pp. 554–573), §21.5 *Inhomogeneous problems – Green's functions*
(pp. 751–767), and Ch. 27 *Numerical methods* introduction and §§27.1–27.3
(pp. 984–1000) and §27.8 (pp. 1030–1032), plus the end of §27.7 (p. 1030),
which shares the first PDF page of §27.8. The exercise sections were not
worked: §8.19–8.20 and §17.7–17.8 were scanned only for citations;
exercise 27.26 was read as a statement because §27.8 points to it. Not
read: all other chapters, including §§21.1–21.4 (separation of variables,
transforms), Ch. 20 (classification and uniqueness of PDEs, cited by §21.5),
Ch. 15 (Green's functions for ODEs), Ch. 22 (variational methods) and
§§27.4–27.7. Results the read sections quote from unread chapters are
recorded as such on the concept pages.

The read chapters are expository: they define the linear-algebra and
operator-theory vocabulary of the bundle, prove the standard spectral
results for normal matrices and Hermitian operators (completeness stated
without proof in both settings), develop Green's functions for Poisson's
equation with Dirichlet and Neumann data by the method of images, and
introduce numerical solution only at the level of Gaussian elimination,
LU, the tridiagonal solver, Gauss–Seidel and point relaxation for the
five-point Laplacian. No convergence theory for linear iterations,
conditioning, Krylov, multigrid or preconditioning appears in the scope.

# Key claims

1. **Vector spaces and inner products** (§8.1, eqs. 8.2–8.22): axioms,
   basis and dimension, inner product conjugate-linear in the first
   argument, Gram matrix, Schwarz, triangle and Bessel inequalities (proved),
   parallelogram equality (stated).
2. **Operators and matrices** (§§8.2–8.12): matrix of an operator in a
   basis; product rules for transpose and Hermitian conjugate (8.39–8.40);
   $\operatorname{tr}AB=\operatorname{tr}BA$ (8.44); the special classes
   through normal matrices.
3. **Determinant and inverse** (§§8.9–8.10): Laplace expansion; seven
   properties stated without proof; $A^{-1}=\operatorname{adj}A/\det A$
   (8.55, proved via 8.57).
4. **Rank** (§8.11): column rank equals row rank (stated, reference to
   Cantrell 2000) and the largest non-singular submatrix.
5. **Spectral theorem for normal matrices** (§8.13): $A^{\mathsf H}$ has
   conjugate eigenvalues (8.69–8.71), eigenvectors of distinct eigenvalues
   orthogonal (8.76), completeness stated without proof (p. 275),
   $A=\sum\lambda_k\mathbf q_k\mathbf q_k^{\mathsf H}$ (8.80); Hermitian
   eigenvalues real; commuting normal matrices share eigenvectors (§8.13.5).
6. **Characteristic equation and invariants** (§§8.14–8.16):
   $\sum\lambda_k=\operatorname{tr}A$ (8.87); similarity invariants
   (8.95–8.98); diagonalisation iff $N$ independent eigenvectors; unitary
   diagonalisation of normal matrices; $\det\exp A=\exp\operatorname{tr}A$
   (8.104).
7. **Forms** (§8.17): reduction to sums of squares (8.110); positive
   definiteness iff all eigenvalues positive; Rayleigh quotient stationary at
   eigenvectors (proved for real symmetric $A$, pp. 290–291).
8. **Solvability** (§8.18.1): rank–nullity (8.119, proved); augmented-matrix
   criterion.
9. **Direct methods** (§8.18.2): inversion (8.122), LU with unit lower
   factor (8.125–8.127), Cholesky $A=LL^{\mathsf H}$ for positive definite
   $A$ (8.128, not developed), Cramer's rule (8.130) with the $3\times3$
   case analysis.
10. **SVD** (§8.18.3): $A=U\Sigma V^{\mathsf H}$ (existence stated, reference
    to Golub & Van Loan 1996); rank and bases of range and null space;
    $V\Sigma^{+}U^{\mathsf H}\mathbf b$ exact when $\mathbf b\in\mathcal R(A)$,
    least-squares minimiser otherwise (8.141–8.143, proved); minimum norm
    stated.
11. **Function spaces** (§17.1): weighted inner product (17.6), Gram–Schmidt
    for functions; "Hilbert space" used for any infinite-dimensional
    inner-product function space.
12. **Adjoint and Hermitian operators** (§§17.2–17.3): formal adjoint by
    integration by parts (17.15); Hermitian = self-adjoint plus vanishing
    boundary terms (17.16); real eigenvalues, orthogonality (17.23–17.24);
    completeness stated, reference to Courant & Hilbert (1953) (p. 560);
    closure relation (17.28).
13. **Sturm–Liouville** (§17.4): Hermitian under (17.37); integrating factor
    (17.39); natural intervals and table 17.1.
14. **Eigenfunction expansion and Green's function** (§§17.5–17.6):
    $G=\sum\phi_n\bar\phi_n/\lambda_n$ (17.51), $G(x,x')=\overline{G(x',x)}$
    (17.52); shifted problem with $\lambda_n-\mu$ and the solvability
    condition at $\mu=\lambda_n$ (p. 573).
15. **Green's functions for PDEs** (§21.5.1): $\mathcal LG=\delta$ (21.77),
    eigenfunction series (21.79) called cumbersome.
16. **Representation formula** (§21.5.2): (21.84) from Green's second
    theorem.
17. **Dirichlet problems** (§21.5.3): $G=0$ on $\partial\Omega$, (21.86);
    fundamental solutions $-1/(4\pi\lvert\mathbf r-\mathbf r'\rvert)$
    (21.90) and $(2\pi)^{-1}\ln\lvert\mathbf r-\mathbf r'\rvert$ (21.93);
    images for half-space, half-plane, quarter-plane, sphere and disc;
    disc Poisson integral (21.104).
18. **Neumann problems** (§21.5.4): consistency (21.105); $\partial_nG=1/\lvert\partial\Omega\rvert$;
    (21.106); disc Neumann solution.
19. **Root finding** (§27.1): rearrangement, linear interpolation, binary
    chopping and Newton–Raphson on $x^5-2x^2-3=0$; a combination recommended.
20. **Convergence of iteration** (§27.2): $\epsilon_{k+1}\approx\Phi'(\xi)\epsilon_k$,
    $\lvert\Phi'(\xi)\rvert<1$ called "necessary (but not sufficient)"
    (27.17; see the compiler's note on the
    [fixed-point](/results/fixed-point-iteration-convergence.md) page);
    order $p$ (27.19); Newton–Raphson second order.
21. **Gaussian elimination with interchange** (§27.3.1): partial pivoting
    motivated without analysis.
22. **Gauss–Seidel** (§27.3.2): diagonal scaling, simultaneous form (27.26),
    Gauss–Seidel form (27.28); no convergence criterion.
23. **Tridiagonal systems** (§27.3.3): recurrences (27.31–27.32), linear
    cost against $\sim N^3$ in general; two-point BVP by central differences
    (§27.7, p. 1030).
24. **PDEs** (§27.8): five-point Laplacian (27.87–27.88), point relaxation
    as "the simplest" relaxation method; nine-point scheme in exercise
    27.26. Out of this bundle's scope and recorded only here: the explicit
    forward-time centred-space scheme for $\partial_t\phi=\kappa\partial_x^2\phi$
    (Riley's symbols, eqs. 27.90–27.92) and the error cancellation at
    $\alpha=\kappa\Delta t/(\Delta x)^2=1/6$ (27.93–27.96).

**Gaps.** No equation in the scope was illegible; garbled text-layer
equations were checked against rendered pages where they matter
(pp. 764, 766). The citation scan of the exercise sections is not a full
reading.

# Notation map

| Riley et al. | Registry | Note |
|---|---|---|
| $\mathcal A$ (script, operator), $\mathsf A$ (matrix) | $\mathcal A$, $A$ | the book distinguishes vector and column matrix; the registry does not |
| $A_{ij}$ | $a_{ij}$ | |
| $N$, $M$ (dimensions) | $N$, $M$ | same |
| $\langle a\vert b\rangle$, $\Vert a\Vert$ | $\langle\mathbf a,\mathbf b\rangle$, $\lVert\mathbf a\rVert$ | same convention (conjugate-linear in first argument) |
| $G_{ij}$ (metric of a basis) | $\Gamma_{ij}$ | $G$ reserved for Green's functions |
| $A^*$, $A^\dagger$ | $\bar A$, $A^{\mathsf H}$ | |
| $\operatorname{Tr}A$, $\lvert A\rvert$ | $\operatorname{tr}A$, $\det A$ | |
| $R(A)$, rank | $\operatorname{rank}A$ | |
| $\Delta_i$ (Cramer determinant) | $\det A_i$ | |
| $\mathbf x^i$, $\lambda_i$ (eigenvectors) | $\mathbf q_k$, $\lambda_k$ | |
| $S$ (similarity), $A'$ | $S$, $A'$ | same; $S$ of eigenvectors written $Q$ |
| $\mathsf S$ (SVD), $s_i$, $\bar{\mathsf S}$ | $\Sigma$, $\sigma_k$, $\Sigma^{+}$ | $U$, $V$, $\mathbf u_k$, $\mathbf v_k$ same |
| $\mathbf b$, residual $\lvert\mathsf A\mathbf x-\mathbf b\rvert$ | $\mathbf b$, $\lVert A\mathbf x-\mathbf b\rVert$ | |
| $\xi$, $x_n$, $\epsilon_n$, $F(x)$ (iteration), $f(x)=0$ | $\xi$, $x_k$, $\epsilon_k$, $\Phi(x)$, $g(x)=0$ | |
| $N$ (order of convergence) | $p$ | |
| $\mathsf C=\mathsf I-\mathsf F$, $\mathbf d$ (Gauss–Seidel) | $D^{-1}A$, $D^{-1}(E+F)$, $D^{-1}\mathbf b$ | Riley's $\mathsf L$, $\mathsf U$ are $D^{-1}E$, $D^{-1}F$ |
| $\mathbf x_n$, $\boldsymbol\xi$ (iterates, solution) | $\mathbf x^{(k)}$, $\mathbf x^\star$ | |
| $a_i$, $b_i$, $c_i$, $y_i$ (tridiagonal) | $a_{i,i-1}$, $a_{ii}$, $a_{i,i+1}$, $b_i$ | |
| $\theta_i$, $\phi_i$ (sweep) | $\theta_i$, $\eta_i$ | |
| $\rho(x)$ (weight function) | $w(x)$ | $\rho$ reserved for the spectral radius |
| $y_i(x)$, $\hat y_n(x)$ (eigenfunctions) | $\phi_n(x)$ (normalised) | |
| $L$, $L^\dagger$ | $\mathcal L$, $\mathcal L^{*}$ | |
| $p$, $q$ in $-(py')'-qy$ | $p$, $-q$ | **sign flip of $q$** |
| $r(x)$ in (17.38), $F(x)$ integrating factor | $p_1(x)$, $\Psi(x)$ | |
| $z$ (ODE Green's-function variable) | $x'$ | |
| $\rho(\mathbf r)$ (source), $V$, $S$ | $f(\mathbf r)$, $\Omega$, $\partial\Omega$ | |
| $\mathbf r_0$ (source point) | $\mathbf r'$ | |
| $f(\mathbf r)$ (boundary data) | $g_{\mathrm D}$ or $g_{\mathrm N}$ | |
| $F(\mathbf r,\mathbf r_0)$, $H$ | $G_0$, $H$ | |
| $A$ (area of $S$) | $\lvert\partial\Omega\rvert$ | |
| $q_n$, $\mathbf r_n$ (images) | $\alpha_m$, $\mathbf r_m$ | |
| $a$ (sphere/disc radius) | $R$ | |
| $(\rho,\phi)$ polar | $(r,\varphi)$ | |
| $k$ (Helmholtz) | $\kappa$ | |
| $\phi_{i,j}$, $\lambda=(\Delta x/\Delta y)^2$ | $u_{i,j}$, $\beta$ | |
| Poisson $\nabla^2u=\rho$, $\nabla^2G=\delta$ | $\nabla^2u=f$, $\nabla^2G=\delta$ | same sign convention |

# Pages created

* Created [Notation registry](/notation.md)
* Created [Inner-product space](/definitions/inner-product-space.md)
* Created [Linear operators and matrices](/definitions/linear-operators-and-matrices.md)
* Created [Determinant and Cramer's rule](/definitions/determinant.md)
* Created [Matrix eigenvalue problem](/definitions/eigenvalue-problem.md)
* Created [Quadratic and Hermitian forms](/definitions/quadratic-and-hermitian-forms.md)
* Created [Adjoint and Hermitian differential operators](/definitions/hermitian-operator.md)
* Created [Sturm–Liouville problem](/definitions/sturm-liouville-problem.md)
* Created [Green's function](/definitions/greens-function.md)
* Created [Poisson boundary-value problem](/definitions/poisson-boundary-value-problem.md)
* Created [Spectral theorem for normal matrices](/results/spectral-theorem-normal-matrices.md)
* Created [Solvability of linear systems](/results/solvability-of-linear-systems.md)
* Created [Convergence of fixed-point iteration](/results/fixed-point-iteration-convergence.md)
* Created [Green's representation formula](/results/greens-representation-formula.md)
* Created [Gram–Schmidt orthogonalisation](/methods/gram-schmidt-orthogonalisation.md)
* Created [Singular value decomposition](/methods/singular-value-decomposition.md)
* Created [LU decomposition](/methods/lu-decomposition.md)
* Created [Gaussian elimination with interchange](/methods/gaussian-elimination.md)
* Created [Tridiagonal solver](/methods/tridiagonal-solver.md)
* Created [Gauss–Seidel iteration](/methods/gauss-seidel-iteration.md)
* Created [Relaxation for Laplace's equation](/methods/laplace-relaxation.md)
* Created [Newton–Raphson method](/methods/newton-raphson-method.md)
* Created [Eigenfunction expansion](/methods/eigenfunction-expansion.md)
* Created [Method of images](/methods/method-of-images.md)
* Created [Five-point discrete Laplacian](/operators/five-point-laplacian.md)

# Citations

* Bibliography entry `riley-2006`; the works cited in the chapters read
  are merged with `citedby = {riley-2006}` (see [bibliography](/bibliography.md)).
