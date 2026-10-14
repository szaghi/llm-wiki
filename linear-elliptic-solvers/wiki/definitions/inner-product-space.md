---
type: Definition
title: "Inner-product space"
description: "Linear vector space with basis, components and an inner product: axioms, orthonormal bases and the Gram matrix, the function space with a weighted inner product, and the Schwarz, triangle, Bessel and parallelogram relations."
status: established
aliases: [linear vector space, vector space, Hilbert space, inner product, Schwarz inequality, Cauchy-Schwarz inequality, Bessel's inequality]
tags: [linear-algebra, function-space]
timestamp: 2026-10-13T00:00:00Z
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

* In an orthonormal basis, $\langle\mathbf e_i,\mathbf e_j\rangle=\delta_{ij}$,
  the components are $x_i=\langle\mathbf e_i,\mathbf x\rangle$ and
  $\langle\mathbf a,\mathbf b\rangle=\sum_i\bar a_ib_i=\mathbf a^{\mathsf H}\mathbf b$
  (eqs. 8.15–8.16, 8.42). The component formula fails in a non-orthonormal
  basis.
* In a general basis, with the Gram matrix $\Gamma_{ij}=\langle\mathbf e_i,\mathbf e_j\rangle$,
  $$\langle\mathbf a,\mathbf b\rangle=\sum_{i,j}\bar a_i\Gamma_{ij}b_j=\mathbf a^{\mathsf H}\Gamma\mathbf b,$$
  and $\Gamma_{ij}=\bar\Gamma_{ji}$ makes $\langle\mathbf a,\mathbf a\rangle$
  real (eq. 8.18, §8.7).

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

## Standard inequalities

For $\langle\mathbf a,\mathbf a\rangle\ge0$ (§8.1.3; repeated for functions
in §17.1.1, eqs. 17.12–17.14):

* **Schwarz:** $\lvert\langle\mathbf a,\mathbf b\rangle\rvert\le\lVert\mathbf a\rVert\,\lVert\mathbf b\rVert$,
  with equality when $\mathbf a$ is a multiple of $\mathbf b$ (eq. 8.19;
  proved from $\lVert\mathbf a+\lambda\mathbf b\rVert^2\ge0$ with a
  discriminant argument).
* **Triangle:** $\lVert\mathbf a+\mathbf b\rVert\le\lVert\mathbf a\rVert+\lVert\mathbf b\rVert$
  (eq. 8.20, from Schwarz).
* **Bessel:** for an orthonormal set $\mathbf e_i$,
  $\lVert\mathbf a\rVert^2\ge\sum_i\lvert\langle\mathbf e_i,\mathbf a\rangle\rvert^2$,
  with equality when the sum runs over a whole basis (eq. 8.21).
* **Parallelogram equality:**
  $\lVert\mathbf a+\mathbf b\rVert^2+\lVert\mathbf a-\mathbf b\rVert^2=2(\lVert\mathbf a\rVert^2+\lVert\mathbf b\rVert^2)$
  (eq. 8.22, stated without proof).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.1 (pp. 242–247), §8.7
  (p. 258), §17.1 (pp. 556–559).
