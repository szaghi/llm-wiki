---
type: Definition
title: "Dirichlet conditions"
description: "The four conditions (periodicity, single-valuedness with finitely many finite discontinuities, finitely many extrema per period, absolutely integrable over a period) under which a function may be expanded as a Fourier series; stated without proof as sufficient for convergence to the function at its points of continuity."
status: established
aliases: [Dirichlet conditions for Fourier series]
tags: [fourier-series, convergence]
timestamp: 2026-10-14T00:00:00Z
---

# Dirichlet conditions

A function $f(x)$ satisfies the **Dirichlet conditions** when
([Riley et al. (2006)](/sources/riley-2006.md), §12.1, p. 415):

1. it is periodic;
2. it is single-valued and continuous, except possibly at a finite number of
   finite discontinuities;
3. it has only a finite number of maxima and minima within one period;
4. the integral of $\lvert f(x)\rvert$ over one period converges.

These are the conditions under which $f$ "may be expanded as a
[Fourier series](/definitions/fourier-series.md)". If they hold, the series
converges to $f(x)$ at every point where $f$ is continuous; the behaviour at a
discontinuity is the subject of
[convergence of Fourier series](/results/fourier-series-convergence.md)
(§12.1, p. 416).

[Arfken et al. (2013)](/sources/arfken-2013.md) state the conditions for a
function expanded on $[0, 2\pi]$ as "only a finite number of finite
discontinuities and only a finite number of extreme values (maxima and
minima)" in the interval, with the coefficient integrals "subject to the
requirement that the integrals exist". They call such functions **piecewise
regular** (§19.1, pp. 935–936). At a point of discontinuity they give the same
mean-value limit (eq. 19.7).

## Scope

* The source states the sufficiency **without proof** ("We have stated without
  proof that any function that satisfies the Dirichlet conditions may be
  represented as a Fourier series", p. 416) and offers only a plausibility
  argument: every function is the sum of an even part and an odd part, the
  even part representable by cosines and the odd part by sines.
* The conditions are presented as sufficient. The source does not claim they
  are necessary. Arfken et al. say so explicitly: "These conditions are
  sufficient but not necessary" (footnote 1, p. 935).
* **Qualification (difference of statement, not of claim).** Arfken et al.
  list only the discontinuity and extremum conditions. Periodicity enters
  through the expansion interval, and integrability through the requirement
  that the coefficient integrals exist; that reading of their wording is the
  compiler's. Functions that violate the conditions "can be considered
  pathological for purposes of Fourier expansions" (p. 936).
* In §20.10 Arfken et al. also use "the Dirichlet conditions" loosely for
  Fourier-transformable functions, requiring there that the transform vanish
  at infinite frequency (eq. 20.199, p. 1038; see
  [Fourier transform](/definitions/fourier-transform.md)).
* Conditions 2–4 "are almost always met in real applications"; Arfken et al.
  agree: "In the vast majority of physical problems involving a Fourier series,
  the Dirichlet conditions will be satisfied" (p. 936). Condition 1 is
  the one that fails in practice, and a non-periodic function on a finite range
  is handled by a periodic extension (§12.5; see
  [Fourier series](/definitions/fourier-series.md)).

# Examples

Exercise 12.3 classifies five functions on stated ranges; the answer
(§12.10, p. 431) is that only $\lvert\sin x\rvert^{-1/2}$ on $-\infty<x<\infty$
can be represented, the others failing as follows: $\tanh^{-1}x$ fails
condition 1, $\tan x$ and $\cos^{-1}(\sin 2x)$ fail condition 2, and
$x\sin(1/x)$ repeated cyclically on $(-\pi^{-1},\pi^{-1}]$ fails condition 3.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §12.1 (pp. 415–416), exercise 12.3 and its answer (pp. 427, 431).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §19.1 (pp. 935–937), §20.10 (p. 1038).
