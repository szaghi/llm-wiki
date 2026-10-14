---
type: Source
title: "Arfken, Weber & Harris (2013) — Mathematical Methods for Physicists, 7th ed."
description: "Graduate textbook of mathematical methods for physicists; this bundle reads its chapters on determinants and matrices, vector spaces, eigenvalue problems, Sturm–Liouville theory and Green's functions."
resource: "doi:10.1016/C2009-0-30629-7"
source_kind: book
authors: [Arfken G.B., Weber H.J., Harris F.E.]
year: 2013
venue: "Academic Press (7th ed.)"
local_file: "/home/stefano/papers/mosaic/linear-elliptic-solvers/2013-AcademicPress-Arfken-101016C20090306297.pdf"
tags: [textbook, linear-algebra, operator-theory, eigenproblem, sturm-liouville, greens-function]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

*Mathematical Methods for Physicists: A Comprehensive Guide*, seventh
edition (Academic Press, an imprint of Elsevier; © 2013 Elsevier Inc.;
ISBN 978-0-12-384654-9 on the copyright page; doi:10.1016/C2009-0-30629-7
verified on Crossref). Identity checked on the title page (PDF p. 3) and the
copyright page (PDF p. 4). The file is a calibre ebook conversion with a
good text layer; the PDF page exceeds the printed page by a drifting offset
(+13 at Ch. 2, +10 at Ch. 5, +9 at Ch. 6, +9 at Ch. 8, +7 at Ch. 10).
Every locator below is a **printed** page.

**Scoped read.** Read: the preface (pp. xi–xiii); Ch. 2 *Determinants and
Matrices* (pp. 83–121); Ch. 5 *Vector Spaces* (pp. 251–297); Ch. 6
*Eigenvalue Problems* (pp. 299–328); Ch. 8 *Sturm–Liouville Theory*
(pp. 381–399); Ch. 10 *Green's Functions* (pp. 447–467), each with its
"Additional Readings". Exercise sets were read as statements, not worked.
Not read: all other chapters, including Ch. 3 (vector analysis and potential
theory, which holds Green's theorem), Ch. 7 (ODEs, which holds the Wronskian
identity Ch. 10 cites), Chs. 14–16 and 18 (the special functions and the
multipole expansion Ch. 10 quotes), Ch. 20 (integral transforms) and Ch. 21
(integral equations). Results the read chapters quote from unread ones are
recorded as such on the concept pages.

The preface (p. xi) states the book's standard of proof: proofs are
"sketched", are "not what a mathematician would consider rigorous", and no
attempt is made "to minimize the conditions necessary". The read chapters
are expository and physics-oriented (quantum mechanics is the running
application). Their numerical content is limited to Gauss elimination,
Gauss–Jordan inversion and a short description of the Jacobi eigenvalue
method; there is no treatment of iterative linear solvers, conditioning
analysis, Krylov methods, multigrid or preconditioning, and none of the
Poisson representation formula or method of images (those sit in the
unread Ch. 3 and later chapters, if anywhere).

# Key claims

1. **Determinants** (§2.1, pp. 83–93): Leibniz definition through the
   Levi-Civita symbol (eqs. 2.8, 2.10); row/column properties derived from
   it (eqs. 2.11–2.13); Laplace expansion in minors (eq. 2.14); Cramer's
   rule for $n$ equations by column operations (eqs. 2.15–2.18); a
   non-zero determinant iff the forms are linearly independent, and a
   homogeneous system has non-trivial solutions only if the determinant
   vanishes (p. 90).
2. **Gauss elimination** (Example 2.1.4, pp. 91–93): equations reordered
   up front so that "the largest coefficients run along the main diagonal"
   for "optimum numerical accuracy"; elimination reduces the determinant to
   triangular form (eq. 2.24). Reference: Press et al. (1992).
3. **Matrix algebra** (§2.2, pp. 95–114): product, commutator (eqs.
   2.26–2.27), uniqueness of the inverse, matrices form a ring (p. 100);
   inverse by minors (eq. 2.34) and Gauss–Jordan inversion, "computationally
   more efficient" (Example 2.2.3, pp. 100–102); derivative of a
   determinant (eq. 2.35); singular iff $\det=0$ (eq. 2.36); product theorem
   proved (eqs. 2.37–2.38); rank as the number of independent forms
   (p. 104); transpose, "adjoint" (conjugate transpose), trace and their
   product rules (eqs. 2.40–2.47); orthogonal, unitary, Hermitian matrices
   (eqs. 2.49–2.53); direct product (eqs. 2.55–2.58); functions of matrices,
   $\exp(\mathrm iH)$ unitary, trace formula (eqs. 2.77–2.84).
4. **Function spaces** (§5.1, pp. 251–269): weighted scalar product
   (eq. 5.4), "Hilbert space" defined by a spanning basis and a scalar
   product (pp. 255–256); Schwarz inequality proved (eqs. 5.8–5.10);
   orthonormal and orthogonal expansions (eqs. 5.12–5.13, 5.18–5.20);
   Bessel's inequality and convergence in the mean (eqs. 5.21–5.22);
   completeness of power, trigonometric and Hermitian-eigenfunction sets
   stated, citing Courant & Hilbert (1953) (p. 262); closure relation
   (eq. 5.27); resolution of the identity (eqs. 5.31–5.32).
5. **Gram–Schmidt** (§5.2, pp. 269–273): eqs. 5.33–5.39; order dependence;
   orthogonal polynomials generated from powers (eq. 5.41, table 5.1); as an
   upper-triangular, non-similarity transformation with
   $T^\dagger ST=1$ (Example 5.6.1, eqs. 5.79–5.81, p. 293).
6. **Operators** (§§5.3–5.4, pp. 275–286): adjoint by $\langle f|Ag\rangle=\langle A^\dagger f|g\rangle$
   (eq. 5.47); "self-adjoint, or equivalently, Hermitian" (eq. 5.48); the
   adjoint depends on the scalar product and the interval (Examples
   5.3.2–5.3.3); matrix of an operator (eqs. 5.50–5.57); adjoint operator
   ↔ adjoint matrix (eq. 5.60); Hermitian operator ↔ Hermitian matrix
   (eq. 5.62).
7. **Basis transformations** (§§5.5–5.7, pp. 287–295): unitary
   transformation between orthonormal bases, $\mathbf c'=U\mathbf c$,
   $A'=UAU^{-1}$ (eqs. 5.67–5.76); a non-unitary similarity transformation
   "do[es] not describe the same quantity in a different basis" (p. 293);
   invariance of scalar products, trace and determinant (eqs. 5.82–5.83).
8. **Matrix eigenproblems** (§§6.1–6.2, pp. 299–308): basis expansion turns
   an operator eigenproblem into $A\mathbf c=\lambda\mathbf c$ (eq. 6.2),
   called "totally equivalent" (p. 300); secular equation (eqs. 6.4–6.5);
   degeneracy (Example 6.2.3).
9. **Hermitian eigenproblems** (§§6.3–6.4, pp. 310–318): real eigenvalues,
   orthogonal eigenvectors (eqs. 6.17–6.21); completeness asserted
   (p. 311); unitary diagonalisation with eigenvectors as the columns of
   $U^{-1}$ (eqs. 6.23–6.24); Jacobi eigenvalue method (p. 314, exercise
   6.4.9); simultaneous diagonalisation iff commuting (pp. 314–315);
   spectral decomposition and functions of $H$ (eqs. 6.25–6.27); expectation
   value bounded by the extreme eigenvalues (eqs. 6.28–6.31, p. 316);
   positive definiteness, overlap matrices, rank $n-m$ from $m$ zero
   eigenvalues (p. 317).
10. **Normal and non-normal matrices** (§6.5, pp. 319–324): normal matrices
    the largest unitarily diagonalisable class (footnote citing Macklin
    1984); $A$ and $A^\dagger$ share eigenvectors (eqs. 6.32–6.33);
    non-normal and defective matrices (pp. 322–324).
11. **Sturm–Liouville** (§8.2, pp. 384–387): ODE-sense self-adjointness
    $p_0'=p_1$ (eqs. 8.8–8.11), "weaker" than Hilbert-space self-adjointness
    (p. 385); boundary terms (eqs. 8.12–8.13) killed by Dirichlet, Neumann
    or periodic conditions; weight $w=p_0^{-1}\exp\int p_1/p_0$
    (eq. 8.15) making any second-order operator Hermitian under the weighted
    scalar product (eqs. 8.18–8.20); classical weights (Example 8.2.1,
    exercises 8.2.1–8.2.4).
12. **ODE eigenproblems** (§8.3, pp. 389–391): Legendre and Hermite
    eigenvalues from series termination, boundedness or finite norm acting
    as the boundary condition.
13. **Variation method** (§8.4, pp. 395–397): $\langle\psi|H|\psi\rangle\ge\lambda_{\min}$
    minimised over a parametrised trial family; summary of eigenproblem
    facts (§8.5, pp. 398–399).
14. **One-dimensional Green's functions** (§10.1, pp. 448–456): $\mathcal LG=\delta$
    (eq. 10.6); continuity of $G$ and jump of $\partial_xG$ (eq. 10.9);
    eigenfunction series and symmetry (eqs. 10.14–10.15); two-solution
    construction with the Wronskian (eqs. 10.18–10.19); non-homogeneous
    and initial conditions (pp. 452–454); integral-equation form of an
    eigenproblem (eqs. 10.29–10.31).
15. **Green's functions in two and three dimensions** (§10.2, pp. 459–464):
    general properties (pp. 459–460); symmetry from Hermiticity
    (eqs. 10.34–10.36); shifted expansion (eq. 10.39); fundamental solutions
    of the Laplacian (eqs. 10.40–10.44) and table 10.1 (Laplace, Helmholtz,
    modified Helmholtz in 1–3 D); the sign convention remark (p. 462);
    spherical and cylindrical expansions (pp. 463–464); adding homogeneous
    solutions to meet boundary conditions (Example 10.2.1).

**Out of the bundle's scope, recorded only here:** the Pauli and Dirac
matrices and Clifford algebras (pp. 98, 109–113), spin spaces (§5.1), the
normal modes of the CO$_2$ model (Example 6.5.2), the deuteron model
(Example 8.3.3), the helium variational example (Example 8.4.1), the
Lippmann–Schwinger equation and Born approximation (Example 10.2.2).

**Gaps.** No equation in the scope was illegible. The text layer flattens
displayed fractions; table 10.1 and eqs. 8.12–8.15 were checked against
rendered pages (pp. 463, 385). Exercise statements were read; their
solutions were not worked.

# Notation map

| Arfken et al. | Registry | Note |
|---|---|---|
| $\langle f\vert g\rangle$, $\Vert f\Vert$ | $\langle f,g\rangle$ (or $\langle f,g\rangle_w$), $\lVert f\rVert$ | same convention: conjugate-linear in the first argument (p. 256) |
| $s$ (function-space variable), $w(s)$ | $x$, $w(x)$ | same weight symbol |
| $\mathsf A$, $a_{ij}$; $1$, $O$ | $A$, $a_{ij}$; $I$, $0$ | |
| $\tilde A$ or $A^T$; $A^*$ | $A^{\mathsf T}$; $\bar A$ | |
| $A^\dagger$, called the **adjoint** of a matrix (eq. 2.41) | $A^{\mathsf H}$, Hermitian conjugate | **terminology**: the book's matrix "adjoint" is not the adjugate $\operatorname{adj}A$ |
| $A^\dagger$, adjoint of an operator (eq. 5.47) | $\mathcal A^{\mathsf H}$ | Hilbert-space adjoint (registry addition) |
| $M_{ij}$ (minor), $(-1)^{i+j}M_{ij}$ (cofactor) | minor, $C_{ij}$ | |
| $\det(A)$, $D_n$, $\vert A\vert$; trace$(A)$ | $\det A$; $\operatorname{tr}A$ | |
| $\varepsilon_{ij\ldots}$, $A\otimes B$, $[A,B]$ | $\varepsilon_{i_1\cdots i_N}$, $A\otimes B$, $[A,B]$ | registry additions |
| $h_i$, $\mathbf h$ (right-hand side) | $b_i$, $\mathbf b$ | |
| $\mathbf c$, $a_\mu$ (expansion coefficients) | $\mathbf x$ (coefficient column), $c_n$ | |
| $U$ with $\mathbf c'=U\mathbf c$, $A'=UAU^{-1}$ | $S^{-1}$: $\mathbf x'=S^{-1}\mathbf x$, $A'=S^{-1}AS$ | **direction**: the book's transformation matrix is the inverse of the registry's change-of-basis matrix |
| $UHU^{-1}$ diagonal, columns of $U^{-1}$ = eigenvectors | $Q^{\mathsf H}AQ=\Lambda$, $Q=U^{-1}$ | |
| $G$ (non-unitary similarity, eq. 5.78) | $S^{-1}$ | $G$ reserved for Green's functions |
| $S$, $s_{\nu\mu}=\langle\chi_\nu\vert\chi_\mu\rangle$ (overlap matrix) | $\Gamma$, $\Gamma_{ij}$ (Gram matrix) | $S$ reserved for similarity |
| $T$ (Gram–Schmidt, upper triangular), $\chi_\mu$, $\psi_n$, $\varphi_n$ | $\Theta$, $\mathbf y_m$, $\mathbf z_m$, $\hat{\mathbf z}_m$ | $T$ reserved for iteration matrices |
| $H$, $\lambda$, $\mathbf c_i$ (Hermitian eigenproblem) | $A$, $\lambda_k$, $\mathbf q_k$ | |
| $\langle H\rangle=\langle\psi\vert H\vert\psi\rangle$, $\Vert\psi\Vert=1$ | $R_{\mathcal L}(u)$ | registry addition |
| $\theta$ (Jacobi rotation) | $\vartheta$ | |
| $\mathcal L=p_0\,\mathrm d^2/\mathrm dx^2+p_1\,\mathrm d/\mathrm dx+p_2$, $\mathcal L\psi=\lambda\psi$ (eqs. 8.7–8.8) | general equation $pu''+p_1u'-qu+\lambda wu=0$ with $p=-p_0$, $p_1=-p_1^{\text{book}}$, $q=p_2$, $w=1$, $\lambda$ unchanged; after multiplication by the weight, $-(pu')'+qu=\lambda wu$ with $p=-wp_0$, $q=wp_2$ | **Sturm–Liouville sign**: the book's self-adjoint form $(p_0u')'+p_2u$ carries no minus; its examples write it in ($-(1-x^2)y''+2xy'$, $p_0=-(1-x^2)$; $-y''+2xy'$), which is the registry sign |
| "self-adjoint" (ODE sense, $p_0'=p_1$) | formally self-adjoint, $\mathcal L^{*}=\mathcal L$ | |
| "self-adjoint" = "Hermitian" (operator sense, eq. 5.48) | Hermitian | see the [Hermitian operator](/definitions/hermitian-operator.md) page |
| $w(x)=p_0^{-1}\exp\int p_1/p_0$ (eq. 8.15) | $-\Psi(x)$, used as the weight $w$ of an unweighted starting equation | the book's weight is the registry's integrating factor up to the constant factor $-1$ |
| Ch. 10: $\mathcal Ly=(py')'+qy$ (eq. 10.5) | $\mathcal Lu=-(pu')'+qu$ with $p\to-p$, $q\to q$ | the jump of $\partial_xG$ reads $+1/p$ in the book, $-1/p$ in registry form |
| $y$, $f$, $G(x,t)$, $y_1$, $y_2$, Wronskian | $u$, $f$, $G(x,x')$, $u_a$, $u_b$, $\mathcal W$ | |
| $G(\mathbf r_1,\mathbf r_2)$ (field $\mathbf r_1$, source $\mathbf r_2$) | $G(\mathbf r,\mathbf r')$ | |
| $\nabla^2G=\delta$ (eq. 10.40), $G=-1/(4\pi\vert\mathbf r_1-\mathbf r_2\vert)$ (eq. 10.43) | $\nabla^2G_0=\delta$, $G_0=-1/(4\pi\lvert\mathbf r-\mathbf r'\rvert)$ | **Green's-function sign: same as the registry**; the book notes that its previous editions and other texts use $-\delta$ (p. 462) |
| opening example: $-\nabla^2\psi=\rho/\varepsilon_0$, $G=1/(4\pi\varepsilon_0\vert\mathbf r_1-\mathbf r_2\vert)$ (eqs. 10.1–10.3) | $\nabla^2u=f$ with $u=\psi$, $f=-\rho/\varepsilon_0$ | the book's eq. 10.3 is the Green's function of $-\varepsilon_0\nabla^2$, hence positive |
| $\lambda$ in $\mathcal L\psi-\lambda\psi=\delta$ (eqs. 10.38–10.39) | $\mu$ | shift parameter |
| $k$ (Helmholtz), $\nabla^2-k^2$ | $\kappa$, $\nabla^2-\kappa^2$ | |
| $\boldsymbol\rho=(\rho,\varphi)$ (plane) | $\mathbf r$, $(r,\varphi)$ | |
| $H_0^{(1)}$, $K_0$, $P_l$, $\chi$ | same | registry additions |
| $\varphi_n$ (eigenfunctions, unit weight in Ch. 10) | $\phi_n$ with $w\equiv1$ | |

# Pages touched

* Created [Variation method](/methods/variation-method.md)
* Updated [Notation registry](/notation.md) (14 additions)
* Updated [Determinant and Cramer's rule](/definitions/determinant.md)
* Updated [Matrix eigenvalue problem](/definitions/eigenvalue-problem.md) (Contradictions entry opened)
* Updated [Green's function](/definitions/greens-function.md)
* Updated [Adjoint and Hermitian differential operators](/definitions/hermitian-operator.md)
* Updated [Inner-product space](/definitions/inner-product-space.md)
* Updated [Linear operators and matrices](/definitions/linear-operators-and-matrices.md)
* Updated [Poisson boundary-value problem](/definitions/poisson-boundary-value-problem.md)
* Updated [Quadratic and Hermitian forms](/definitions/quadratic-and-hermitian-forms.md)
* Updated [Sturm–Liouville problem](/definitions/sturm-liouville-problem.md)
* Updated [Spectral theorem for normal matrices](/results/spectral-theorem-normal-matrices.md)
* Updated [Solvability of linear systems](/results/solvability-of-linear-systems.md)
* Updated [Eigenfunction expansion](/methods/eigenfunction-expansion.md)
* Updated [Gaussian elimination with interchange](/methods/gaussian-elimination.md)
* Updated [Gram–Schmidt orthogonalisation](/methods/gram-schmidt-orthogonalisation.md)
* Updated [Singular value decomposition](/methods/singular-value-decomposition.md)

# Citations

* Bibliography entry `arfken-2013`. The "Additional Readings" of Chs. 2, 5,
  6, 8 and 10 and the works cited in footnotes of those chapters are merged
  with `citedby = {arfken-2013}` (see [bibliography](/bibliography.md)).
