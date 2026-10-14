---
type: Method
title: "Variation of parameters"
description: "A particular integral of an nth-order linear ODE with known complementary function y_c = sum c_j y_j is sum k_j(x) y_j with the k_j' fixed by n linear equations whose determinant is the Wronskian: the first n-1 combinations of derivatives vanish and the last equals psi/a_n."
status: established
aliases: [variation of constants, Lagrange's method]
tags: [ode, particular-integral]
timestamp: 2026-10-14T00:00:00Z
---

# Variation of parameters

Given the complementary function $y_c = \sum_{j=1}^n c_jy_j$ of
$a_n(x)y^{(n)} + \dots + a_0(x)y = \psi(x)$, seek
$$y_p = \sum_{j=1}^n k_j(x)\,y_j(x)$$
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 15.53–15.54,
p. 508). The ODE imposes one condition on $n$ functions, so $n - 1$ more
may be chosen. The convenient choice is
$$\sum_j k_j'\,y_j^{(m)} = 0 \quad (m = 0, \dots, n-2), \qquad \sum_j k_j'\,y_j^{(n-1)} = \frac{\psi(x)}{a_n(x)}$$
(eq. 15.55). The first $n-1$ equations make each derivative
$y_p^{(m)}$, $m < n$, look like a derivative of $y_c$. The last is then
forced by the ODE, not chosen (pp. 508–509). The determinant of the
system is the [Wronskian](/definitions/wronskian.md), non-zero for
independent solutions. Solving for the $k_j'$ and integrating, with the
constants set to zero, gives $y_p$; keeping the constants redefines the
$c_j$ (pp. 509–510).

**Worked case** (pp. 510): $y'' + y = \operatorname{cosec}x$ with
$y_1 = \sin x$, $y_2 = \cos x$ gives $k_1' = \cot x$, $k_2' = -1$, so
$y = (c_1 + \ln\sin x)\sin x + (c_2 - x)\cos x$. With $y(0) = y(\pi/2) = 0$
this gives $y = \sin x\ln\sin x - x\cos x$, the same as reduction of order
and the [Green's function](/methods/greens-functions-for-linear-odes.md).

[Arfken et al. (2013)](/sources/arfken-2013.md) derive the same scheme for
second order (§7.7, eqs. 7.95–7.98, pp. 375–376): with
$y_p = k_1y_1 + k_2y_2$ for $y'' + a_1y' + a_0y = \psi$, they impose
$k_1'y_1 + k_2'y_2 = 0$, and the ODE then gives
$k_1'y_1' + k_2'y_2' = \psi$. The determinant is the Wronskian of the
independent solutions, non-zero, so the choice is consistent (p. 376).
Exercise 7.7.1 writes the closed form
$$y_p(x) = y_2(x)\int^x\frac{y_1(q)\psi(q)}{W(q)}\,\mathrm dq - y_1(x)\int^x\frac{y_2(q)\psi(q)}{W(q)}\,\mathrm dq$$
(p. 377). Example 7.7.1: $(1 - x)y'' + xy' - y = (1 - x)^2$, with
$y_1 = x$, $y_2 = e^x$, must first be divided by $1 - x$; it gives
$y_p = x^2 + 1$ after a multiple of $y_1$ is dropped (pp. 376–377). For a
first-order linear equation the same idea is "variation of the constant":
replacing $C$ by $C(x)$ in the homogeneous solution reproduces the
integrating-factor solution (§7.2, pp. 338–339; see
[first-order ODE methods](/methods/first-order-ode-solution-methods.md)).

The method needs the whole complementary function. Reduction of order needs
only one solution (p. 508; [structure of linear ODE
solutions](/results/linear-ode-solution-structure.md)). The book
recommends it as the most straightforward general method when
undetermined coefficients do not apply (p. 495).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §15.2.4 (pp. 508–510).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §7.2 (pp. 338–339),
  §7.7 (pp. 375–377).
