---
type: Definition
title: "Inner-product space"
description: "Linear vector space with basis, components and an inner product: axioms, orthonormal bases and the Gram matrix, the function space with a weighted inner product, and the Schwarz, triangle, Bessel and parallelogram relations."
status: established
aliases: [linear vector space, vector space, Hilbert space, inner product, scalar product, Schwarz inequality, Cauchy-Schwarz inequality, Bessel's inequality, Parseval's identity, resolution of the identity, overlap matrix]
tags: [linear-algebra, function-space]
timestamp: 2026-10-14T00:00:00Z
---

# Inner-product space

**Vector space.** A set $V$ is a (linear) vector space if it is closed
under commutative, associative addition and under multiplication by
scalars (distributive and associative), contains a null vector
$\mathbf 0$ with $\mathbf a+\mathbf 0=\mathbf a$, satisfies
$1\cdot\mathbf a=\mathbf a$, and contains a negative $-\mathbf a$ for every
$\mathbf a$ ([Riley et al. (2006)](/sources/riley-2006.md), §8.1,
eqs. 8.2–8.6). Real scalars give a real space, complex scalars a complex
space.

* **Span, dependence.** The span of a set is all its linear combinations.
  The set is linearly dependent if a non-trivial combination vanishes,
  linearly independent otherwise (eqs. 8.7–8.8).
* **Dimension and basis.** $V$ is $N$-dimensional if it holds $N$, but not
  $N+1$, linearly independent vectors. Any $N$ independent vectors
  $\mathbf e_1,\dots,\mathbf e_N$ form a basis, and every $\mathbf x$ has
  unique components, $\mathbf x=\sum_i x_i\mathbf e_i$ (§8.1.1,
  eqs. 8.9–8.11). The vector is basis-independent; only its components
  change with the basis.

## Inner product

An inner product $\langle\mathbf a,\mathbf b\rangle$ is a scalar function
with $\langle\mathbf a,\mathbf b\rangle=\overline{\langle\mathbf b,\mathbf a\rangle}$
and linearity in the second argument; it follows that it is
conjugate-linear in the first (§8.1.2, eqs. 8.13–8.14). Orthogonality is
$\langle\mathbf a,\mathbf b\rangle=0$, the norm is
$\lVert\mathbf a\rVert=\langle\mathbf a,\mathbf a\rangle^{1/2}$. Riley et al.
restrict themselves to spaces with $\langle\mathbf a,\mathbf a\rangle\ge0$,
where $\langle\mathbf a,\mathbf a\rangle=0$ implies $\mathbf a=\mathbf 0$.
[Arfken et al. (2013)](/sources/arfken-2013.md) list the same axioms — the
"scalar product" is conjugate-linear in the first argument, linear in the
second, and $\langle f,f\rangle>0$ unless $f=0$ — and add that for
functions "zero" must be read as "zero except on a set of measure zero"
(§5.1, p. 256 and footnote 2).

* In an orthonormal basis, $\langle\mathbf e_i,\mathbf e_j\rangle=\delta_{ij}$,
  the components are $x_i=\langle\mathbf e_i,\mathbf x\rangle$ and
  $\langle\mathbf a,\mathbf b\rangle=\sum_i\bar a_ib_i=\mathbf a^{\mathsf H}\mathbf b$
  (eqs. 8.15–8.16, 8.42). The component formula fails in a non-orthonormal
  basis.
* In a general basis, with the Gram matrix $\Gamma_{ij}=\langle\mathbf e_i,\mathbf e_j\rangle$,
  $$\langle\mathbf a,\mathbf b\rangle=\sum_{i,j}\bar a_i\Gamma_{ij}b_j=\mathbf a^{\mathsf H}\Gamma\mathbf b,$$
  and $\Gamma_{ij}=\bar\Gamma_{ji}$ makes $\langle\mathbf a,\mathbf a\rangle$
  real (eq. 8.18, §8.7). Arfken et al., who call $\Gamma$ the overlap
  matrix, add that it is positive definite for a linearly independent basis,
  since $\mathbf x^{\mathsf H}\Gamma\mathbf x=\lVert\sum_ix_i\mathbf e_i\rVert^2>0$
  (Example 6.4.2, p. 317).
* In an orthonormal basis, $\langle f,g\rangle=\sum_n\bar c_n\langle\phi_n,g\rangle$
  for $f=\sum c_n\phi_n$, and $\lVert f\rVert^2=\sum_n\lvert c_n\rvert^2$
  (Arfken et al., eqs. 5.18–5.20, p. 260; with an infinite sum this is
  Parseval's identity, exercise 5.1.5, p. 268). If the basis is orthogonal
  but not normalised, $c_n=\langle\phi_n,f\rangle/\langle\phi_n,\phi_n\rangle$
  (eq. 5.13, p. 258).
* **Resolution of the identity.** For a complete orthonormal set,
  $\sum_n\phi_n\langle\phi_n,\cdot\rangle$ is the identity operator;
  Arfken et al. write it in Dirac's bra–ket notation and use it to derive
  expansion, change-of-basis and operator-matrix formulas (eqs. 5.31–5.32,
  p. 266).

An orthonormal basis can be built from any basis by
[Gram–Schmidt orthogonalisation](/methods/gram-schmidt-orthogonalisation.md).

## Function spaces

The reasonably well-behaved functions on $[a,b]$ form an
infinite-dimensional vector space (§17.1). With a real, non-negative weight
$w(x)$ the inner product is
$$\langle f,g\rangle_w=\int_a^b\bar f(x)g(x)w(x)\,\mathrm dx,$$
with orthogonality, norm $\lVert f\rVert_w$ and normalisation defined as
above (eqs. 17.6–17.8). Riley et al. call an infinite-dimensional function
space with an inner product a Hilbert space (p. 557); completeness of the
space, which the standard definition requires, is not discussed. In an
orthonormal basis $\phi_n$, $f=\sum_nc_n\phi_n$ with
$c_n=\langle\phi_n,f\rangle_w$ (eqs. 17.10–17.11). The eigenfunctions of a
[Hermitian operator](/definitions/hermitian-operator.md) supply such bases.

*Qualification (scope of "Hilbert space"), Arfken et al.* Arfken et al.
use the same weighted scalar product (eq. 5.4, p. 254), with $w$ positive
"except possibly for zeros at isolated points", and also call the space a
Hilbert space, but by a different loose definition: a space closed under
addition and scalar multiplication, with a scalar product for every pair,
and spanned by a finite or denumerable basis of linearly independent
functions — the spanning property being what they call "completeness"
(pp. 255–256). Neither book requires completeness in the metric
(Cauchy-sequence) sense that the standard definition demands. Arfken et al.
add that power series and trigonometric series are proved complete for the
square-integrable functions, as are the eigenfunctions of Hermitian
eigenproblems (p. 262, citing Courant & Hilbert 1953), and that the
truncated orthonormal expansion with $c_n=\langle\phi_n,f\rangle_w$
minimises the weighted mean-square error, the coefficients not depending
on the number of terms (exercise 5.1.4, p. 267). The analogous
least-squares fit in powers of $x$ on $[0,1]$ leads to the Hilbert matrix
$\left[(i+j-1)^{-1}\right]_{i,j=1}^{N}$, whose equations they call "ill-conditioned and unstable"
already at order 5 (exercise 5.1.3, p. 267).

## Standard inequalities

For $\langle\mathbf a,\mathbf a\rangle\ge0$ (§8.1.3; repeated for functions
in §17.1.1, eqs. 17.12–17.14):

* **Schwarz:** $\lvert\langle\mathbf a,\mathbf b\rangle\rvert\le\lVert\mathbf a\rVert\,\lVert\mathbf b\rVert$,
  with equality when $\mathbf a$ is a multiple of $\mathbf b$ (eq. 8.19;
  proved from $\lVert\mathbf a+\lambda\mathbf b\rVert^2\ge0$ with a
  discriminant argument). Arfken et al. prove it from the same quantity by
  choosing the minimising $\lambda=-\langle\mathbf b,\mathbf a\rangle/\lVert\mathbf b\rVert^2$
  (their $f-\lambda g$ form, eqs. 5.8–5.10, p. 257).
* **Triangle:** $\lVert\mathbf a+\mathbf b\rVert\le\lVert\mathbf a\rVert+\lVert\mathbf b\rVert$
  (eq. 8.20, from Schwarz).
* **Bessel:** for an orthonormal set $\mathbf e_i$,
  $\lVert\mathbf a\rVert^2\ge\sum_i\lvert\langle\mathbf e_i,\mathbf a\rangle\rvert^2$,
  with equality when the sum runs over a whole basis (eq. 8.21). Arfken et
  al. prove the function version from
  $\lVert f-\sum_ic_i\phi_i\rVert^2\ge0$, identify equality with
  convergence in the mean — weaker than uniform convergence, permitting
  deviations at isolated points — and call it "a not too practical test
  for completeness" since it must hold for every $f$ (eqs. 5.21–5.22,
  p. 262).
* **Parallelogram equality:**
  $\lVert\mathbf a+\mathbf b\rVert^2+\lVert\mathbf a-\mathbf b\rVert^2=2(\lVert\mathbf a\rVert^2+\lVert\mathbf b\rVert^2)$
  (eq. 8.22, stated without proof).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.1 (pp. 242–247), §8.7
  (p. 258), §17.1 (pp. 556–559).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §5.1 (pp. 251–268),
  §6.4 (p. 317).
