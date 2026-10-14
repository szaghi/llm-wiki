---
type: Result
title: "d'Alembert's formula"
description: "The solution of the one-dimensional wave equation on the whole line with initial displacement u0 and velocity u1 is the mean of u0 at x - ct and x + ct plus 1/(2c) times the integral of u1 over [x - ct, x + ct]: half of each initial disturbance travels each way along the characteristics."
status: established
aliases: [d'Alembert's solution, D'Alembert solution]
tags: [hyperbolic, wave-equation, cauchy-problem, characteristics]
timestamp: 2026-10-13T00:00:00Z
---

# d'Alembert's formula

**Statement.** For $\partial_x^2u = c^{-2}\partial_t^2u$ on
$-\infty < x < \infty$ with Cauchy data $u(x,0) = u_0(x)$ and
$\partial_tu(x,0) = u_1(x)$,
$$u(x,t) = \tfrac12\left[u_0(x - ct) + u_0(x + ct)\right] + \frac{1}{2c}\int_{x-ct}^{x+ct}u_1(q)\,\mathrm dq$$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.31, p. 694).

**Derivation** (pp. 694). Insert the general solution
$u = F(x - ct) + G(x + ct)$ of the [wave equation](/definitions/wave-equation.md)
into the data: $F + G = u_0$ and $-cF' + cG' = u_1$ at $t = 0$
(eqs. 20.27–20.28). Integrating the second from an arbitrary lower limit
gives $F$ and $G$ separately (eqs. 20.29–20.30). Adding them at
$x \mp ct$ removes the arbitrary limit and the integration constant.

**Interpretation** (pp. 694–695). The factor $\tfrac12$ reflects that half
of a displacement profile starting at any point travels towards $x$ and
half away. $\tfrac12u_0(x - ct)$ is the initial displacement at distance
$ct$ to the left, arriving at time $t$, and likewise from the right. The
integral is the accumulated displacement from "all parts of the initial
motion whose effects can reach $x$ within a time $t$", in both directions.
Equivalently, $u(x,t)$ depends only on the data in $[x - ct, x + ct]$, the
interval cut out of $t = 0$ by the two [characteristics](/definitions/characteristic-curve.md)
through $(x,t)$. The term "domain of dependence" is not the book's.

**Scope.** Infinite string, no boundaries. The book states no regularity
requirements on $u_0$, $u_1$; the derivation differentiates $F$, $G$ and
$u_0$ and integrates $u_1$. Bounded strings are left to [separation of
variables](/methods/separation-of-variables.md) (p. 693). Exercise 20.16
(p. 709) applies the formula to a string released from rest with a
compactly supported sinusoidal displacement written with Heaviside
functions.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.4 (pp. 693–695),
  Exercise 20.16 (p. 709).
