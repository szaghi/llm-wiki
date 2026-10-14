---
type: Definition
title: "Determinant and Cramer's rule"
description: "Determinant by Laplace cofactor expansion, its properties (transpose, row operations, product rule, triangular case), the adjugate formula for the inverse, and Cramer's rule with its case analysis of singular systems."
status: established
aliases: [determinant, Laplace expansion, cofactor, adjugate, Cramer's rule]
tags: [linear-algebra, direct-solver]
timestamp: 2026-10-14T00:00:00Z
---

# Determinant and Cramer's rule

**Definition.** For a square $A$, the cofactor of $a_{ij}$ is
$C_{ij}=(-1)^{i+j}$ times the determinant of the matrix left after deleting
row $i$ and column $j$ (the minor). The determinant is the Laplace
expansion along any row or column, e.g. $\det A=\sum_ja_{ij}C_{ij}$ for
fixed $i$; Riley et al. assert that the value is independent of the row or
column chosen and check it for order 3 by rearrangement (eqs. 8.45–8.47)
([Riley et al. (2006)](/sources/riley-2006.md), §8.9, pp. 259–261). For
$N=3$ with rows $\mathbf a,\mathbf b,\mathbf c$, $\det A=\mathbf a\cdot(\mathbf b\times\mathbf c)$,
the parallelepiped volume (eq. 8.48). For any $N$, $\det A=0$ when the rows
(or columns) are linearly dependent.

**Leibniz form.** [Arfken et al. (2013)](/sources/arfken-2013.md) take the
permutation sum as the definition,
$$\det A=\sum_{i_1,\dots,i_N}\varepsilon_{i_1i_2\cdots i_N}\,a_{1i_1}a_{2i_2}\cdots a_{Ni_N}$$
($N!$ signed products, one entry from each row and column; §2.1, eqs. 2.8,
2.10, pp. 85–86), and obtain the Laplace expansion in cofactors (eq. 2.14,
p. 88) and the row and column properties from it. The two books agree on
the expansion; Arfken et al. supply the derivation that Riley et al.
replace by assertion. Arfken et al. stress that "a determinant of large
elements" can have a very small value (p. 86), and pose the Hilbert
determinants $\det\left[(i+j-1)^{-1}\right]$, of order $10^{-18}$ at
$N=6$, as an exercise (exercise 2.1.5, p. 94).

**Linear dependence** (pp. 89–90). The $N$ rows of $A$ are linearly
independent iff $\det A\neq0$; a homogeneous system has solutions other
than $\mathbf x=\mathbf 0$ only if $\det A=0$, and then they are
"arbitrary as to scale". This is the general-$N$ form of cases 2 and 5
below.

## Properties (§8.9.1, stated without proof)

Riley et al. state the list below without proof; Arfken et al. derive
properties 2–5 from the Leibniz form, assert property 1 (eqs. 2.11–2.13,
p. 87; the conjugate case on p. 107) and prove
property 6, the product theorem, by expanding the columns of $AB$ and
collecting a Levi-Civita symbol (eqs. 2.37–2.38, pp. 103–104), with
$\det A^{-1}=1/\det A$ as a corollary (eq. 2.39).

1. $\det A^{\mathsf T}=\det A$; $\det A^{\mathsf H}=\overline{\det A}$ (eqs. 8.49–8.50).
2. Interchanging two rows (columns) changes the sign.
3. A common factor of a row may be taken out; $\det(\lambda A)=\lambda^N\det A$ (eq. 8.51).
4. Two proportional rows (columns) give $\det A=0$.
5. Adding a multiple of one row (column) to another leaves $\det A$ unchanged.
6. $\det(AB)=\det A\,\det B=\det(BA)$ (eq. 8.52).
7. Diagonal and triangular matrices: $\det A=\prod_ia_{ii}$ (eqs. 8.63–8.64).

Property 5 is what makes [LU decomposition](/methods/lu-decomposition.md)
give $\det A=\prod_iu_{ii}$ cheaply (eq. 8.127). Arfken et al. make the
same point for [Gauss elimination](/methods/gaussian-elimination.md): the
elimination brings the determinant to triangular form, so $\det A$ is the
product of the pivots times the factors divided out on the way (eq. 2.24,
p. 93).

**Derivative of a determinant.** For $A$ depending on a parameter $x$,
$$\frac{\mathrm d\det A}{\mathrm dx}=\det A\sum_{i,j}\left(A^{-1}\right)_{ji}\frac{\mathrm da_{ij}}{\mathrm dx}=\det A\,\operatorname{tr}\!\left(A^{-1}\frac{\mathrm dA}{\mathrm dx}\right),$$
from $\partial\det A/\partial a_{ij}=C_{ij}$ ([Arfken et al. (2013)](/sources/arfken-2013.md),
eq. 2.35, p. 102; the trace form is the compiler's rewriting).

## Inverse via the adjugate

$$\left(A^{-1}\right)_{ik}=\frac{C_{ki}}{\det A},\qquad A^{-1}=\frac{\operatorname{adj}A}{\det A},$$
resting on $\sum_kC_{ki}a_{kj}=\det A\,\delta_{ij}$, proved by replacing
column $i$ with column $j$ (a matrix with two equal columns has zero
determinant) (eqs. 8.55–8.57, pp. 264–265). Arfken et al. give the same formula,
$(A^{-1})_{ij}=C_{ji}/\det A$ (eq. 2.34, p. 100), call it "closed, but
cumbersome", and prefer Gauss–Jordan elimination (see
[Gaussian elimination](/methods/gaussian-elimination.md)). $A$ is singular iff
$\det A=0$ (also Arfken et al., eq. 2.36, with the converse proved from
eq. 2.39, p. 104); for $N=2$, $A^{-1}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\begin{pmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{pmatrix}$
(eq. 8.60). Direct inversion $\mathbf x=A^{-1}\mathbf b$ (eq. 8.122) is
"computationally demanding" for large $N$ (p. 296).

## Cramer's rule

For non-singular $A$,
$$x_i=\frac{\det A_i}{\det A},$$
where $A_i$ is $A$ with column $i$ replaced by $\mathbf b$ (eq. 8.130,
derived for $N=3$ by adding multiples of columns; the derivation divides by
$x_1$, and the result is asserted to hold also when some $x_i=0$)
(§8.18.2, pp. 299–300). Arfken et al. derive the rule for any $N$ without
that division: multiply column $i$ of $\det A$ by $x_i$, add $x_j$ times
every other column $j$ (which leaves the value unchanged), and the column
becomes $\mathbf b$, so $x_i\det A=\det A_i$ (eqs. 2.15–2.18,
pp. 88–89). This removes the restriction left open by Riley's derivation.
Reading each equation of a $3\times3$ system as a
plane, Riley et al. classify (p. 301):

1. $\det A\neq0$, $\mathbf b\neq\mathbf 0$: one non-trivial solution.
2. $\det A\neq0$, $\mathbf b=\mathbf 0$: only $\mathbf x=\mathbf 0$.
3. $\det A=0$, $\mathbf b\neq\mathbf 0$, all $\det A_i=0$: infinitely many
   solutions, on a line (rank 2) or a plane (rank 1).
4. $\det A=0$, $\mathbf b\neq\mathbf 0$, some $\det A_i\neq0$: no solution.
5. $\det A=0$, $\mathbf b=\mathbf 0$: a line of solutions through the origin.

The case analysis is stated for $N=3$ only; the general-$N$ criterion is
the rank test on the [solvability](/results/solvability-of-linear-systems.md)
page.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §8.9 (pp. 259–263), §8.10
  (pp. 263–266), §8.18.2 (pp. 295–301).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §2.1 (pp. 83–94), §2.2
  (pp. 100–104).
