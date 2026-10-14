# Directory Update Log

## 2026-10-14

* **Ingestion of [arfken-2013](/sources/arfken-2013.md)** (Arfken, Weber &
  Harris, *Mathematical Methods for Physicists*, 7th ed., Academic Press
  2013), second source, merge path. Scoped read: preface, Ch. 2
  (pp. 83–121), Ch. 5 (pp. 251–297), Ch. 6 (pp. 299–328), Ch. 8
  (pp. 381–399), Ch. 10 (pp. 447–467), each with its Additional Readings;
  exercises read as statements only.
  * Created 1 page: methods (1) [variation method](/methods/variation-method.md)
    (Arfken §6.4, §8.4; Riley §8.17.1 cited on it).
  * Updated 16 pages with Arfken citations, extensions and
    qualifications: definitions (9) determinant, eigenvalue problem,
    Green's function, Hermitian operator, inner-product space, linear
    operators and matrices, Poisson BVP, quadratic and Hermitian forms,
    Sturm–Liouville; results (2) spectral theorem, solvability; methods
    (4) eigenfunction expansion, Gaussian elimination, Gram–Schmidt, SVD;
    and the notation registry.
  * Contradictions opened (1): [matrix eigenvalue problem](/definitions/eigenvalue-problem.md)
    — whether a non-unitary similarity transformation is a change of
    basis (Riley §8.15, pp. 282–284, vs Arfken §5.6, p. 293); open, with a
    compiler's reading (hypothesis) that the books define the matrix of an
    operator differently.
  * Qualifications recorded (5): Sturm–Liouville sign and form (Arfken
    $(p_0u')'+p_2u$, eq. 8.11, and $(pu')'+qu$, eq. 10.5, vs registry
    $-(pu')'+qu$; Arfken's weight eq. 8.15 equals Riley's integrating
    factor eq. 17.39); "self-adjoint" vs "Hermitian" terminology (Arfken
    pp. 277, 385 vs Riley pp. 559–560); scope of "Hilbert space" (Arfken
    pp. 255–256 vs Riley p. 557); when the elimination reordering is done
    (Arfken p. 91, once, vs Riley pp. 995–996, every step); the matrix
    "adjoint" of Arfken (eq. 2.41) is the registry's Hermitian conjugate.
  * Agreements confirmed: the Green's-function sign — both books and the
    registry use $\nabla^2G=\delta$, $G_0=-1/(4\pi\lvert\mathbf r-\mathbf r'\rvert)$
    (Arfken eqs. 10.40–10.43, with its remark on the opposite convention,
    p. 462); the weight function $w$ (same symbol in both).
  * Compiler's notes (hypothesis): the eigenvalue rank criterion holds for
    diagonalisable matrices only (solvability page); a small determinant is
    not a scale-invariant conditioning measure (solvability page); the
    Gram–Schmidt matrix gives a Cholesky factor of the Gram matrix
    (Gram–Schmidt page); completeness of Hermitian eigenfunctions is stated
    without hypotheses in both books (Hermitian operator page); the
    weighted Rayleigh quotient on the variation-method page.
  * Registry extended (14 entries, marked "added 2026-10-14, arfken-2013"):
    $[A,B]$, $A\otimes B$, $\varepsilon_{i_1\cdots i_N}$,
    $\mathcal A^{\mathsf H}$, $R_{\mathcal L}(u)$,
    $\lambda_{\min}$/$\lambda_{\max}$, $\tilde u$, $\vartheta$, $\Theta$,
    $u_a$/$u_b$, $\mathcal W$, modified Helmholtz $\nabla^2-\kappa^2$,
    $H_0^{(1)}$/$K_0$, $P_l$/$\chi$/$r_<$/$r_>$.
  * Bibliography: 36 entries (was 4). Arfken's reference list — the
    Additional Readings of Chs. 2, 5, 6, 8, 10 plus the works cited in
    footnotes of those chapters, 47 citations of 33 distinct works — merged
    complete; 31 new entries, 2 existing entries gained `arfken-2013` in
    `citedby` (courant-1953, golub-1996); `@book{arfken-2013}` added.
    DOIs added only for the 5 journal articles, each verified on Crossref.

## 2026-10-13

* **Scaffolding and ingestion of [riley-2006](/sources/riley-2006.md)**
  (Riley, Hobson & Bence, *Mathematical Methods for Physics and
  Engineering*, 3rd ed., CUP 2006). Scoped read: contents, prefaces, Ch. 8
  §§8.1–8.18, Ch. 17 §§17.1–17.6, §21.5, Ch. 27 introduction, §§27.1–27.3,
  §27.8 (with the end of §27.7 on the same page); exercise sections scanned
  for citations only, exercise 27.26 read as a statement.
  * Seeded the [notation registry](/notation.md): vector spaces and inner
    products; matrices and linear operators; eigenproblems, forms and
    decompositions; linear systems and iterations (splitting $A=D-E-F$,
    iteration matrices); scalar nonlinear equations; function spaces and
    differential operators (Sturm–Liouville sign $-(pu')'+qu$, weight $w$);
    elliptic boundary-value problems (Poisson $\nabla^2u=f$, Green's function
    $\nabla^2G=\delta$); discretization. $\rho(A)$ reserved for the spectral
    radius.
  * Created 24 concept pages: definitions (9) inner-product space, linear
    operators and matrices, determinant and Cramer's rule, matrix
    eigenvalue problem, quadratic and Hermitian forms, adjoint and Hermitian
    differential operators, Sturm–Liouville problem, Green's function,
    Poisson boundary-value problem; results (4) spectral theorem for normal
    matrices, solvability of linear systems, convergence of fixed-point
    iteration, Green's representation formula; methods (10) Gram–Schmidt,
    SVD, LU, Gaussian elimination, tridiagonal solver, Gauss–Seidel,
    relaxation for Laplace, Newton–Raphson, eigenfunction expansion, method
    of images; operators (1) five-point discrete Laplacian.
  * Compiler's notes recorded as hypothesis: the Gauss–Seidel error
    recursion, and the necessary-versus-sufficient reading of
    $\lvert\Phi'(\xi)\rvert<1$ on the fixed-point page.
  * Bibliography: 4 entries (riley-2006 plus 3 works cited in footnotes:
    cantrell-2000, courant-1953, golub-1996).

