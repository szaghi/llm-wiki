---
type: Definition
title: "Wronskian"
description: "The determinant of n functions and their first n-1 derivatives; a non-zero Wronskian on an interval proves linear independence (the converse fails for general functions), for solutions of a second-order linear ODE it obeys Abel's formula and is identically zero or never zero, and it is the determinant that variation of parameters and the two-point ODE Green's function divide by."
status: established
aliases: [Wronskian determinant, Abel's formula]
tags: [ode, linear-independence]
timestamp: 2026-10-14T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) derive the same determinant
the same way (§7.6, eq. 7.55, pp. 359–360) and agree on the sufficient
condition: a non-zero Wronskian proves independence, and zeros at isolated
points prove nothing. Their Exercise 7.6.6 is an example: $\sin x$, $e^x$,
$e^{-x}$ are independent, with $W = 4\sin x$ vanishing at $x = n\pi$
(p. 370).

**Qualification: the converse.** Arfken et al. state in the text that "if
the Wronskian is zero over the entire range of the variable, the functions
… are linearly dependent over this range" (p. 360). A footnote attaches the
conditions: continuous derivatives, and at least one minor of the bottom
row of the determinant non-vanishing on the interval (citing Lass 1957,
p. 187). Their Exercise 7.6.7 shows why the conditions matter: $x$ and
$\lvert x\rvert$ have $W \equiv 0$ on $[-1, 1]$ and are independent
(p. 370). This is Riley et al.'s warning. The two books therefore agree:
the converse fails for general functions and holds under extra hypotheses,
which only Arfken et al. state. Read without its footnote, Arfken's
sentence would contradict Riley's (compiler's reading).

## Solutions of a second-order linear ODE

For two solutions of $y'' + a_1(x)y' + a_0(x)y = 0$, Arfken et al. show
$W' = -a_1W$ (eq. 7.57, p. 361), hence **Abel's formula**
$$W(x) = W(x_0)\exp\left(-\int_{x_0}^{x}a_1(q)\,\mathrm dq\right)$$
(eq. 7.63, p. 362; the name is not the book's). If $a_1$ stays finite on
the interval, the Wronskian of two solutions is "either identically zero or
never zero" (footnote 7, p. 362). With $a_1 = 0$ it is constant, and the
solutions can be scaled to $W = 1$ (eq. 7.62).

The same identity proves that the equation has at most two independent
solutions: the $3 \times 3$ Wronskian of any three solutions, expanded by
minors and reduced with $W' = -a_1W$, has two equal rows and vanishes
(pp. 361–362; asserted for order $n$ without proof). Abel's formula also
yields the second solution from a first one ([series solutions of linear
ODEs](/methods/frobenius-series-solutions.md); eq. 7.67).

## Uses in the chapters read

* **Constant-coefficient ODEs.** The exponentials $e^{\nu_j x}$ of distinct
  auxiliary roots have non-zero Wronskian. For a repeated root the
  Wronskian has identical columns and vanishes, which signals the missing
  solutions $x e^{\nu x}, \dots$ (p. 493; see
  [structure of linear ODE solutions](/results/linear-ode-solution-structure.md)).
* **Variation of parameters.** The linear system for the $k_j'$ has the
  Wronskian as its determinant, "which is non-zero since the solutions
  $y_m(x)$ are linearly independent" (p. 509; see
  [variation of parameters](/methods/variation-of-parameters.md)). Arfken et
  al. make the same step for second order (§7.7, p. 376).
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

**Narrowed by arfken-2013, not closed.** Arfken et al. supply two of the
ingredients for second order: Abel's dichotomy (zero everywhere or
nowhere), and $W \equiv 0 \Rightarrow$ dependence when one of the two
functions does not vanish on the interval (Exercise 7.6.4, p. 370). On an
interval where $y_1 \ne 0$ and $a_1$ is finite, two solutions independent
on that interval therefore have a Wronskian that is not identically zero,
hence nowhere zero. Carrying
this to an interval on which every solution has zeros requires the
uniqueness of the initial-value problem, which Arfken et al. pose only as
an exercise under a Taylor-expansion hypothesis (Exercise 7.5.1, p. 356).
The assembly is the compiler's; the step remains a compiler's remark.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §15 introduction
  (pp. 490–492), §15.1.1 (p. 493), §15.2.4 (p. 509), Exercise 15.27
  (p. 527).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §7.6 (pp. 359–362),
  Exercises 7.6.4–7.6.7, 7.6.10 (p. 370), §7.7 (p. 376).
