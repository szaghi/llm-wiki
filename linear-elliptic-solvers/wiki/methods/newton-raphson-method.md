---
type: Method
title: "Newton–Raphson method"
description: "Root-finding iteration x_{k+1} = x_k - g(x_k)/g'(x_k) from the tangent line, second-order convergent at a simple root, with its failure modes near stationary points; compared on one test equation with rearrangement, linear interpolation (false position) and binary chopping (bisection)."
status: established
aliases: [Newton's method, Newton-Raphson, bisection, binary chopping, false position, regula falsi, linear interpolation]
tags: [nonlinear-equation, iteration-theory]
timestamp: 2026-10-13T00:00:00Z
---

# Newton–Raphson method

**Method.** The tangent to $g$ at $x_k$, $y=(x-x_k)g'(x_k)+g(x_k)$, cuts
the axis at
$$x_{k+1}=x_k-\frac{g(x_k)}{g'(x_k)}\quad\text{(eqs. 27.10–27.11)}$$
([Riley et al. (2006)](/sources/riley-2006.md), §27.1.4, pp. 990–991). It
is second-order convergent at a simple root
([fixed-point convergence](/results/fixed-point-iteration-convergence.md)).
Near a stationary point of $g$ ($g'\approx0$) it works badly, and a nearby
maximum or minimum can make the iterates oscillate across the root instead
of homing in. On $x^5-2x^2-3=0$ ($\xi=1.49510640$) from $x_1=1.7$ the
residual falls to $2.6\times10^{-8}$ by the fifth iterate (table 27.4).

## Comparison methods (§27.1, same test equation)

| Method | Iteration | Behaviour in the source |
|---|---|---|
| rearrangement | $x_{k+1}=\Phi(x_k)$ | first order, error factor $\approx4$ per step (table 27.1) |
| linear interpolation (false position) | chord root $x_k=\frac{A_kg(B_k)-B_kg(A_k)}{g(B_k)-g(A_k)}$ between bracketing $A_k<B_k$, replacing the endpoint of the same sign (eq. 27.8) | factor $\approx3$ per step; one endpoint tends to stay fixed when the curvature keeps its sign; approaches monotonically, so no error bracket (table 27.2) |
| binary chopping (bisection) | $x_k=\tfrac12(A_k+B_k)$ (eq. 27.9) | error halves per step, predictable in advance; a safe bracket $A_k<\xi<B_k$ at every stage (table 27.3) |
| Newton–Raphson | eq. 27.11 | accuracy improves dramatically near the root; less satisfactory far from it |

No single method is ideal; the recommended practice is some combination of
the first three followed by Newton–Raphson when high accuracy is needed
(p. 992). The extension to systems of nonlinear equations is not treated.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.1 (pp. 985–992), §27.2
  (p. 993).
