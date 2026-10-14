---
type: Definition
title: "Matrix eigenvalue problem"
description: "Eigenvalues and eigenvectors of a square matrix: characteristic equation, trace and determinant identities, degeneracy and defective matrices, change of basis by similarity transformation with its invariants, and diagonalisation."
status: established
aliases: [eigenvalue, eigenvector, characteristic equation, secular determinant, similarity transformation, diagonalisation, defective matrix, change of basis]
tags: [linear-algebra, eigenproblem]
timestamp: 2026-10-14T00:00:00Z
---

# Matrix eigenvalue problem

**Definition.** A non-zero $\mathbf q$ with $A\mathbf q=\lambda\mathbf q$ is
an eigenvector of the square matrix $A$ and $\lambda$ its eigenvalue
(eqs. 8.67–8.68). Eigenvectors are fixed only up to a factor and are usually
normalised, $\mathbf q^{\mathsf H}\mathbf q=1$
([Riley et al. (2006)](/sources/riley-2006.md), §8.13, pp. 272–273). If
$A$ is non-singular, $A^{-1}$ has the same eigenvectors with eigenvalues
$1/\lambda_k$ (p. 273; also [Arfken et al. (2013)](/sources/arfken-2013.md),
exercise 6.4.5, p. 318).

**Operator eigenproblems as matrix eigenproblems.** Arfken et al. reach the
matrix problem from an operator equation $\mathcal A\psi=\lambda\psi$ on a
Hilbert space: expanding in an orthonormal basis $\phi_i$, with
$a_{ij}=\langle\phi_i,\mathcal A\phi_j\rangle$ and
$x_i=\langle\phi_i,\psi\rangle$, gives $A\mathbf x=\lambda\mathbf x$, which
they call "totally equivalent" to the operator problem (§6.1, eq. 6.2,
pp. 300–301). For an infinite basis the equivalence is asserted, not
proved.

**Characteristic equation.** $(A-\lambda I)\mathbf q=\mathbf 0$ has a
non-trivial solution only if
$$\det(A-\lambda I)=0,$$
a polynomial of degree $N$ whose $N$ roots are the eigenvalues (§8.14,
eqs. 8.85–8.86). The coefficient of $-\lambda^{N-1}$ gives
$$\sum_k\lambda_k=\operatorname{tr}A\quad\text{(eq. 8.87)},\qquad\prod_k\lambda_k=\det A\quad\text{(eq. 8.103)},$$
the first offered as a necessary, not sufficient, check on computed
eigenvalues. The determinant product is derived for diagonalisable $A$
(§8.16). Arfken et al. name the same equation the secular equation (the
determinant the secular determinant) or the characteristic equation, count
$N$ eigenvalues with multiplicity by the fundamental theorem of algebra, and
derive the trace and determinant identities for Hermitian $A$ from their
invariance under unitary transformation (§6.2, eqs. 6.4–6.5, pp. 302–305;
§6.4, p. 313); exercise 6.4.1 extends them to any matrix brought to
diagonal form by a similarity transformation (p. 317).

**Degeneracy.** An eigenvalue with several independent eigenvectors is
degenerate; any combination of those eigenvectors is again an eigenvector
(eqs. 8.77–8.78). A matrix whose eigenvectors are not linearly independent
is **defective**. Stated without proof: a matrix with $N$ distinct
eigenvalues has $N$ independent eigenvectors; with degenerate eigenvalues a
general matrix may or may not (§8.13.4, p. 278). Arfken et al. agree: every
distinct eigenvalue has at least one eigenvector, an eigenvalue of
multiplicity $k>1$ need not have $k$, and
$\begin{pmatrix}1&1\\0&1\end{pmatrix}$ has the double eigenvalue $1$ with a
single eigenvector (§6.5, p. 324). For a non-normal matrix the eigenvalues
of $A^{\mathsf H}$ are still the conjugates of those of $A$, since
$\det(A^{\mathsf H}-\bar\lambda I)=\overline{\det(A-\lambda I)}$, but the
eigenvectors of $A$ are in general neither orthogonal nor shared with
$A^{\mathsf H}$ (p. 322); the eigenvectors of $A$ and of $A^{\mathsf H}$
are biorthogonal: an eigenvector of $A^{\mathsf H}$ belonging to
$\bar\lambda_i$ is orthogonal to the eigenvector $\mathbf q_j$ of $A$
whenever $\lambda_i\neq\lambda_j$ (exercise 6.5.10, p. 325, stated with the
book's labelling of the eigenvalues). For normal matrices the
[spectral theorem](/results/spectral-theorem-normal-matrices.md) settles
the question.

## Similarity transformation

Changing basis by $\mathbf e'_j=\sum_iS_{ij}\mathbf e_i$ ($S$ non-singular)
transforms components as $\mathbf x=S\mathbf x'$ and the operator matrix as
$$A'=S^{-1}AS\quad\text{(eqs. 8.90–8.94)}.$$
Basis-independent properties are invariant (eqs. 8.95–8.98): $I'=I$,
$\det A'=\det A$, the characteristic polynomial and hence the eigenvalues,
and $\operatorname{tr}A'=\operatorname{tr}A$. If $S$ is unitary,
$A'=S^{\mathsf H}AS$, an orthonormal basis stays orthonormal, and
(anti-)Hermitian and unitary matrices keep their class (eqs. 8.99–8.100)
(§8.15, pp. 282–285).

Arfken et al. derive the unitary case from expansions in orthonormal
bases: the coefficient columns transform by a unitary matrix whose entries
are the scalar products of new and old basis vectors, and the matrix of an
operator by the corresponding unitary similarity; in registry form
$\mathbf x'=S^{-1}\mathbf x$, $A'=S^{-1}AS$ with $S$ unitary (§§5.5–5.6,
eqs. 5.67–5.76, pp. 287–292; their transformation matrix is the registry's
$S^{-1}$, see the notation map). Scalar products, the trace and the
determinant are invariant (§5.7, eqs. 5.82–5.83, pp. 294–295). On
non-unitary similarity the two books differ; see **Contradictions** below.

## Diagonalisation

With the eigenvectors as columns, $Q=[\mathbf q_1\ \cdots\ \mathbf q_N]$,
$$Q^{-1}AQ=\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_N),$$
possible iff the $N$ eigenvectors are independent; a defective matrix
cannot be diagonalised (§8.16, pp. 285–286). Normal matrices are
diagonalised by a unitary $Q$. Consequences: $(Q^{-1}AQ)^n=Q^{-1}A^nQ$, and
the trace formula $\det(\exp A)=\exp(\operatorname{tr}A)$ (eq. 8.104),
proved for diagonalisable $A$. Arfken et al. state the trace formula for
Hermitian $A$ and prove it in the eigenvector basis (eq. 2.84, p. 113;
eq. 6.27, p. 316).

## Numerical diagonalisation

Riley et al. do not discuss how eigenvalues are computed. Arfken et al.
note that no closed formula solves secular equations of high degree, so
practical programs approach diagonal form by successive approximation, and
cite a computation of some eigenpairs of a matrix of dimension above $10^9$
(Olsen et al. 1990) (§6.4, pp. 313–314). As an illustration they describe
the **Jacobi eigenvalue method**, "supplanted by more efficient (but less
transparent) methods": for Hermitian $A$, a unitary transformation acting
only on rows and columns $i$, $j$ annihilates $a_{ij}$ and $a_{ji}$; other
zeros may be destroyed, but the sum of the squared moduli of the
off-diagonal entries decreases, and the rotations are repeated until every
off-diagonal entry is below a tolerance; the product of the rotations is
the diagonalising matrix (p. 314). For real symmetric $A$ the rotation
angle satisfies $\tan2\vartheta=2a_{ij}/(a_{jj}-a_{ii})$, the trace is
unchanged, and the off-diagonal sum of squares falls by exactly $2a_{ij}^2$
(exercise 6.4.9, statement only, p. 318). No convergence rate is given.

## Contradictions

**What a non-unitary similarity transformation represents.** *Open.*

* [Riley et al. (2006)](/sources/riley-2006.md), §8.15 (pp. 282–284):
  changing to **any** new basis $\mathbf e'_j=\sum_iS_{ij}\mathbf e_i$ with
  $S$ merely non-singular transforms the components by $\mathbf x=S\mathbf x'$
  and the matrix of the operator by $A'=S^{-1}AS$; $A'$ is the matrix of the
  same operator in the new basis, and the unitary case is the special case
  of orthonormal bases.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §5.6 (p. 293): a
  transformation $GAG^{-1}$ with $G$ non-singular but not unitary, called a
  similarity transformation, "preserves the original operator equation" but
  its "corresponding items do not describe the same quantity in a different
  basis. Instead, they describe quantities that have been systematically
  (but consistently) altered by the transformation." Example 5.6.1 adds that
  passing from a non-orthogonal basis to the Gram–Schmidt orthonormal one
  transforms the matrix of scalar products $\langle\mathbf y_i,\mathcal A\mathbf y_j\rangle$
  by $\Theta^{\mathsf H}(\cdot)\Theta$, which is "not even" a similarity
  transformation.

Read literally, the two statements disagree on whether a non-unitary
similarity transformation is a change of basis.

*Compiler's reading (status: hypothesis, not a source).* The books define
"the matrix of an operator in a basis" differently. Riley et al. use
expansion coefficients, $\mathcal A\mathbf e_j=\sum_ia_{ij}\mathbf e_i$,
which are defined in any basis and transform by similarity under any
non-singular change of basis. Arfken et al. work with orthonormal bases
throughout Ch. 5, where the expansion coefficients coincide with the scalar
products $\langle\phi_i,\mathcal A\phi_j\rangle$; in a non-orthonormal
basis the scalar-product matrix transforms by congruence, not by
similarity. On that reading both statements hold within their own
definition, and the disagreement is one of scope. The reading is the
compiler's; the entry stays open until a source settles it or the human
closes it.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.13 (pp. 272–279),
  §8.14 (pp. 280–282), §§8.15–8.16 (pp. 282–288).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §2.2 (p. 113), §§5.5–5.7
  (pp. 287–295), §§6.1–6.2 (pp. 299–308), §6.4 (pp. 311–318), §6.5
  (pp. 322–325).
