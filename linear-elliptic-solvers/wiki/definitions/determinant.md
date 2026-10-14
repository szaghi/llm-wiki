---
type: Definition
title: "Determinant and Cramer's rule"
description: "Determinant by Laplace cofactor expansion, its properties (transpose, row operations, product rule, triangular case), the adjugate formula for the inverse, and Cramer's rule with its case analysis of singular systems."
status: established
aliases: [determinant, Laplace expansion, cofactor, adjugate, Cramer's rule]
tags: [linear-algebra, direct-solver]
timestamp: 2026-10-13T00:00:00Z
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

## Properties (§8.9.1, stated without proof)

1. $\det A^{\mathsf T}=\det A$; $\det A^{\mathsf H}=\overline{\det A}$ (eqs. 8.49–8.50).
2. Interchanging two rows (columns) changes the sign.
3. A common factor of a row may be taken out; $\det(\lambda A)=\lambda^N\det A$ (eq. 8.51).
4. Two proportional rows (columns) give $\det A=0$.
5. Adding a multiple of one row (column) to another leaves $\det A$ unchanged.
6. $\det(AB)=\det A\,\det B=\det(BA)$ (eq. 8.52).
7. Diagonal and triangular matrices: $\det A=\prod_ia_{ii}$ (eqs. 8.63–8.64).

Property 5 is what makes [LU decomposition](/methods/lu-decomposition.md)
give $\det A=\prod_iu_{ii}$ cheaply (eq. 8.127).

## Inverse via the adjugate

$$\left(A^{-1}\right)_{ik}=\frac{C_{ki}}{\det A},\qquad A^{-1}=\frac{\operatorname{adj}A}{\det A},$$
resting on $\sum_kC_{ki}a_{kj}=\det A\,\delta_{ij}$, proved by replacing
column $i$ with column $j$ (a matrix with two equal columns has zero
determinant) (eqs. 8.55–8.57, pp. 264–265). $A$ is singular iff
$\det A=0$; for $N=2$, $A^{-1}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\begin{pmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{pmatrix}$
(eq. 8.60). Direct inversion $\mathbf x=A^{-1}\mathbf b$ (eq. 8.122) is
"computationally demanding" for large $N$ (p. 296).

## Cramer's rule

For non-singular $A$,
$$x_i=\frac{\det A_i}{\det A},$$
where $A_i$ is $A$ with column $i$ replaced by $\mathbf b$ (eq. 8.130,
derived for $N=3$ by adding multiples of columns; the derivation divides by
$x_1$, and the result is asserted to hold also when some $x_i=0$)
(§8.18.2, pp. 299–300). Reading each equation of a $3\times3$ system as a
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
