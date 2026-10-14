---
type: Result
title: "Convergence of Fourier series"
description: "Under the Dirichlet conditions the Fourier series converges to f at points of continuity and to the mean of the one-sided limits at a finite discontinuity (stated without proof); term-by-term integration converges to the integral, and term-by-term differentiation converges to f' when f is continuous and periodic and f' satisfies the Dirichlet conditions."
status: established
aliases: [pointwise convergence of Fourier series, term-by-term differentiation, term-by-term integration, midpoint convergence at a jump]
tags: [fourier-series, convergence, discontinuity]
timestamp: 2026-10-13T00:00:00Z
---

# Convergence of Fourier series

## Pointwise convergence

If $f$ satisfies the [Dirichlet conditions](/definitions/dirichlet-conditions.md),
its [Fourier series](/definitions/fourier-series.md) converges to $f(x)$ at
every point where $f$ is continuous
([Riley et al. (2006)](/sources/riley-2006.md), §12.1, p. 416). At a point
$x_d$ of finite discontinuity it converges to the mean of the one-sided limits
(§12.4, p. 420):
$$\frac12\lim_{\epsilon\to0}\bigl[f(x_d + \epsilon) + f(x_d - \epsilon)\bigr].$$
Both statements are made **without proof**; the second is introduced with "we
state without proof". The series "itself does not produce a discontinuous
function". Near the jump the partial sums overshoot: see
[Gibbs phenomenon](/results/gibbs-phenomenon.md).

Consequence for periodic extensions: if the extension of a function given on a
finite range jumps at an end-point, the series converges there to the mean,
not to the end value. The odd extension of $x^2$ on $(0,2]$ converges to $0$
at $x = \pm 2$ (§12.5, pp. 423–424; exercise 12.18).

## Term-by-term integration and differentiation

(§12.6, p. 424, stated without proof.)

* The series of $f$ integrated term by term converges to the integral of $f$,
  up to a constant of integration to be determined separately.
* If $f$ is continuous for all $x$ and periodic, the series differentiated
  term by term converges to $f'$, **provided** $f'$ itself satisfies the
  Dirichlet conditions.

The continuity requirement matters: exercise 12.10 asks why the series of
$e^x$ on $(-1,1)$ cannot be differentiated term by term to recover $e^x$. Its
periodic extension is discontinuous at $x = \pm1$. Exercise 12.7 shows the
sine series of $1 - x$ on $[0,1]$ differentiated term by term "does not
converge" (answer, p. 431).

## Rate of decay of coefficients

The chapter states no general theorem linking smoothness to the decay rate of
$a_m, b_m$. The link appears only in exercises: 12.8 asks the reader to pick,
"by sketching the function and considering its derivative", the
faster-converging extension of $x\sin x$, and states a convergence
$\sim m^{-3}$ for it.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§12.1, 12.4–12.6 (pp. 416–424); exercises 12.7, 12.8, 12.10, 12.18 and answers (pp. 428–431).
