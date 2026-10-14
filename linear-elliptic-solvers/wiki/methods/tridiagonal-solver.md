---
type: Method
title: "Tridiagonal solver"
description: "Two-sweep elimination for tridiagonal systems: the ansatz x_{i-1} = theta_{i-1} x_i + eta_{i-1} gives forward recurrences for theta_i and eta_i and a backward substitution, at cost linear in N; applied to the central-difference discretization of a two-point boundary-value problem."
status: established
aliases: [Thomas algorithm, tridiagonal matrix algorithm, TDMA, tridiagonal matrix]
tags: [linear-algebra, direct-solver, banded-matrix]
timestamp: 2026-10-13T00:00:00Z
---

# Tridiagonal solver

**Setting.** A tridiagonal matrix has non-zero entries only on the
diagonal $a_{ii}$, the subdiagonal $a_{i,i-1}$ and the superdiagonal
$a_{i,i+1}$. It arises when the members of an ordered set interact only
with nearest neighbours, and from difference approximations of
differential equations. For most systems the work grows roughly as $N^3$;
for tridiagonal systems it grows linearly
([Riley et al. (2006)](/sources/riley-2006.md), §27.3.3, pp. 998–999).

**Method.** Row $i$ reads
$a_{i,i-1}x_{i-1}+a_{ii}x_i+a_{i,i+1}x_{i+1}=b_i$. With the ansatz
$x_{i-1}=\theta_{i-1}x_i+\eta_{i-1}$ (eq. 27.31), substitution keeps the
same form one index up, giving
$$\theta_i=\frac{-a_{i,i+1}}{a_{i,i-1}\theta_{i-1}+a_{ii}},\qquad\eta_i=\frac{b_i-a_{i,i-1}\eta_{i-1}}{a_{i,i-1}\theta_{i-1}+a_{ii}}\quad\text{(eq. 27.32)},$$
started from $\theta_1=-a_{12}/a_{11}$, $\eta_1=b_1/a_{11}$, "provided the
denominator does not vanish for any $i$". A forward sweep computes all
$\theta_i,\eta_i$; then $x_N=\eta_N$ and the backward sweep applies
eq. 27.31 (p. 999; worked $6\times6$ example, table 27.7, p. 1000).

The book gives no condition guaranteeing non-vanishing denominators (such
as diagonal dominance) and no stability analysis. The alternative of
shooting with $x_1$ unknown is dismissed as "very cumbersome" for large
matrices (p. 999).

## Application: two-point boundary-value problem

For a second-order linear equation with constant coefficients on $[0,1]$
and prescribed $u(0)$ and $u(1)$, central differences for $u''$ and $u'$ on
$N$ points with $h=1/(N-1)$ give, at each interior point, a relation among
$u_{i-1}$, $u_i$, $u_{i+1}$ with right-hand side $h^2f(x_i)$: a
tridiagonal system whose boundary rows are $a_{11}=a_{NN}=1$ with the
boundary values on the right (§27.7, eq. 27.85 and the recurrence below it,
p. 1030). The multidimensional analogue, the
[five-point Laplacian](/operators/five-point-laplacian.md), is not
tridiagonal and is treated by [relaxation](/methods/laplace-relaxation.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.3.3 (pp. 998–1000),
  §27.7 (p. 1030).
