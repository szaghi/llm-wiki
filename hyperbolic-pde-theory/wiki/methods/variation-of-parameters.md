---
type: Method
title: "Variation of parameters"
description: "A particular integral of an nth-order linear ODE with known complementary function y_c = sum c_j y_j is sum k_j(x) y_j with the k_j' fixed by n linear equations whose determinant is the Wronskian: the first n-1 combinations of derivatives vanish and the last equals psi/a_n."
status: established
aliases: [variation of constants, Lagrange's method]
tags: [ode, particular-integral]
timestamp: 2026-10-13T00:00:00Z
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

The method needs the whole complementary function. Reduction of order needs
only one solution (p. 508; [structure of linear ODE
solutions](/results/linear-ode-solution-structure.md)). The book
recommends it as the most straightforward general method when
undetermined coefficients do not apply (p. 495).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §15.2.4 (pp. 508–510).
