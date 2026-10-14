---
type: Result
title: "Convergence of fixed-point iteration"
description: "For x_{k+1} = Phi(x_k) with root xi = Phi(xi), the error obeys epsilon_{k+1} ~ Phi'(xi) epsilon_k, so |Phi'(xi)| < 1 governs convergence; vanishing of the first p-1 derivatives of Phi at xi gives p-th order convergence, as for Newton-Raphson (p = 2) and Heron's square-root iteration."
status: established
aliases: [fixed-point iteration, order of convergence, rate of convergence, rearrangement method, linear convergence, quadratic convergence, Heron's method]
tags: [iteration-theory, nonlinear-equation]
timestamp: 2026-10-13T00:00:00Z
---

# Convergence of fixed-point iteration

**Setting.** A root $\xi$ of $g(x)=0$ is sought by an iteration
$x_{k+1}=\Phi(x_k)$ with $\xi=\Phi(\xi)$, e.g. by rearranging $g(x)=0$ into
$x=\Phi(x)$ with $\Phi$ slowly varying (§27.1.1, eqs. 27.4–27.5)
([Riley et al. (2006)](/sources/riley-2006.md)). Success means
$x_k\to\xi$, and, in practice, closeness for all $k$ beyond a small index
(eq. 27.2).

**Error recursion** (§27.2, eqs. 27.13–27.17). With
$x_k=\xi+\epsilon_k$ and a Taylor expansion,
$$\epsilon_{k+1}=\epsilon_k\Phi'(\xi)+\tfrac12\epsilon_k^2\Phi''(\xi)+\cdots,\qquad\epsilon_{k+1}\approx\Phi'(\xi)\,\epsilon_k ,$$
and the book concludes that $\lvert\Phi'(\xi)\rvert<1$ is "a necessary (but
not sufficient) condition for convergence". The condition is on $\Phi'$,
not on $g'$.

**Order of convergence** (eqs. 27.18–27.19). If
$\Phi'(\xi)=\dots=\Phi^{(p-1)}(\xi)=0$ then $\epsilon_{k+1}=O(\epsilon_k^p)$,
$p$-th order convergence. Two second-order instances are proved:

* [Newton–Raphson](/methods/newton-raphson-method.md),
  $\Phi=x-g/g'$: $\Phi'=gg''/(g')^2$ vanishes at a simple root,
  $g'(\xi)\neq0$ (p. 993).
* Square root, $x_{k+1}=\tfrac12(x_k+X/x_k)$: $\Phi'(\sqrt X)=0$,
  $\Phi''(\sqrt X)=1/\sqrt X\neq0$, so exactly second order; from
  $x_0=1$ for $X=16$ the error falls from $4.5$ to $6.4\times10^{-7}$ in
  five steps (eq. 27.20, table 27.5, p. 994).

The rearrangement $x=(2x^2+3)^{1/5}$ of $x^5-2x^2-3=0$ is first order,
reducing the error by a factor of about 4 per step (table 27.1, p. 988).

## Compiler's note on the stated condition

*Status: hypothesis (compiler's reading, not a second source).* As a
statement about convergence from starting points close enough to $\xi$,
$\lvert\Phi'(\xi)\rvert<1$ (with $\Phi'$ continuous) is ordinarily a
**sufficient** condition — it makes $\Phi$ a contraction near $\xi$ — while
it is not strictly necessary, since $\lvert\Phi'(\xi)\rvert=1$ is not
decisive and $\lvert\Phi'(\xi)\rvert>1$ excludes convergence except by
landing on $\xi$ exactly. The book's "necessary (but not sufficient)"
reading is consistent only with the global question (convergence from an
arbitrary start). The point should be settled against a numerical-analysis
source before it is relied on. The matrix analogue — convergence of
stationary linear iterations governed by the iteration matrix — is open on
the [Gauss–Seidel](/methods/gauss-seidel-iteration.md) page.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.1.1 (pp. 987–988),
  §27.2 (pp. 992–994).
