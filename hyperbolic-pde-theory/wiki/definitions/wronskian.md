---
type: Definition
title: "Wronskian"
description: "The determinant of n functions and their first n-1 derivatives; a non-zero Wronskian on an interval proves linear independence (the converse fails for general functions), and it is the determinant that variation of parameters and the two-point ODE Green's function divide by."
status: established
aliases: [Wronskian determinant]
tags: [ode, linear-independence]
timestamp: 2026-10-13T00:00:00Z
---

# Wronskian

Functions $y_1, \dots, y_n$ are linearly independent on an interval if no
constants other than $c_1 = \dots = c_n = 0$ make
$c_1y_1 + \dots + c_ny_n = 0$ there. Differentiating that relation $n-1$
times gives $n$ linear equations for the $c_j$, whose determinant is the
**Wronskian**
$$W(y_1, \dots, y_n) = \begin{vmatrix} y_1 & y_2 & \cdots & y_n \\ y_1' & y_2' & \cdots & y_n' \\ \vdots & \vdots & & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & \cdots & y_n^{(n-1)} \end{vmatrix}$$
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 15.4–15.6, p. 491).
If $W \ne 0$ on the interval the functions are linearly independent. "The
vanishing of the Wronskian does not guarantee that the functions are
linearly dependent" (p. 491).

## Uses in the chapters read

* **Constant-coefficient ODEs.** The exponentials $e^{\nu_j x}$ of distinct
  auxiliary roots have non-zero Wronskian. For a repeated root the
  Wronskian has identical columns and vanishes, which signals the missing
  solutions $x e^{\nu x}, \dots$ (p. 493; see
  [structure of linear ODE solutions](/results/linear-ode-solution-structure.md)).
* **Variation of parameters.** The linear system for the $k_j'$ has the
  Wronskian as its determinant, "which is non-zero since the solutions
  $y_m(x)$ are linearly independent" (p. 509; see
  [variation of parameters](/methods/variation-of-parameters.md)).
* **Green's function of a two-point problem.** For
  $y'' + a_1(x)y' + a_0(x)y = 0$ with independent solutions $y_1(0) = 0$,
  $y_2(1) = 0$, the Green's function with $G(0,x') = G(1,x') = 0$ is
  $G = y_1(x)y_2(x')/W(x')$ for $x < x'$ and $y_2(x)y_1(x')/W(x')$ for
  $x > x'$ (Exercise 15.27, p. 527; set as an exercise, not proved in the
  text; see [Green's functions for linear ODEs](/methods/greens-functions-for-linear-odes.md)).

## Gap

The variation-of-parameters step uses the converse direction
(independence implies $W \ne 0$), which p. 491 warns fails for general
functions. It does hold for solutions of a linear ODE with non-vanishing
leading coefficient, but that theorem is not in the chapters read
(compiler's remark).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §15 introduction
  (pp. 490–492), §15.1.1 (p. 493), §15.2.4 (p. 509), Exercise 15.27
  (p. 527).
