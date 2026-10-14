---
type: Definition
title: "Convolution"
description: "The integral of f(x) g(z - x) over all x (Fourier form) or over 0 to t (Laplace form), commutative, associative and distributive; it smooths and broadens, models a measurement through a resolution function, and is inverted (deconvolution) by division of transforms."
status: established
aliases: [convolution integral, deconvolution, resolution function]
tags: [fourier-transform, laplace-transform, convolution]
timestamp: 2026-10-13T00:00:00Z
---

# Convolution

## Definition

The **convolution** of $f$ and $g$ is
([Riley et al. (2006)](/sources/riley-2006.md), eq. 13.37)
$$(f * g)(z) = \int_{-\infty}^{\infty} f(x)\,g(z - x)\,\mathrm dx.$$
It is commutative, associative and distributive (p. 447). For functions
defined on $t \ge 0$, as with the [Laplace transform](/definitions/laplace-transform.md),
the source uses the one-sided form (eq. 13.64)
$$(f * g)(t) = \int_0^t f(u)\,g(t - u)\,\mathrm du,$$
also commutative, associative and distributive (p. 458). The two coincide
when $f$ and $g$ vanish for negative argument (a compiler remark, not stated
in the source).

## Interpretation

The source motivates convolution by measurement. A true distribution $f$
observed through an apparatus whose resolution function $g(y)\,\mathrm dy$
is the probability that a true value is recorded displaced by $y$ gives the
observed distribution $q = f * g$, "broader and smoother than the true one".
A biased $g$ displaces the maxima, and $g = \delta$ gives $q = f$ (§13.1.7,
pp. 446–447). Convolving with $\delta(x+a) + \delta(x-a)$ places a copy of $g$
at each delta: $q(z) = g(z+a) + g(z-a)$ (worked example, p. 447).

## Deconvolution

By the [convolution theorem](/results/convolution-theorem.md),
$\hat q = \sqrt{2\pi}\,\hat f\hat g$, so
$$f(x) = \frac{1}{\sqrt{2\pi}}\,\mathcal F^{-1}\!\left[\frac{\hat q(k)}{\hat g(k)}\right]$$
(p. 449). The source warns that in practice this is "often not very precise"
because of experimental and statistical uncertainty, data over a limited
range, and three numerical transforms each needing in principle an infinite
integral. It does not discuss the division where $\hat g$ is small or zero.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.1.7 (pp. 446–449), §13.2.2 (eq. 13.64, p. 458).
