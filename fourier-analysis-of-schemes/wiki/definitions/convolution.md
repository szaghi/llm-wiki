---
type: Definition
title: "Convolution"
description: "The integral of f(x) g(z - x) over all x (Fourier form) or over 0 to t (Laplace form), commutative, associative and distributive; it smooths and broadens, models a measurement through a resolution function, and is inverted (deconvolution) by division of transforms."
status: established
aliases: [convolution integral, deconvolution, resolution function]
tags: [fourier-transform, laplace-transform, convolution]
timestamp: 2026-10-14T00:00:00Z
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

**Qualification: Arfken et al.'s normalized convolution.**
[Arfken et al. (2013)](/sources/arfken-2013.md) define the Fourier
convolution with the transform's constant inside,
$\frac{1}{\sqrt{2\pi}}\int g(u)\,f(x-u)\,\mathrm du = \frac{1}{\sqrt{2\pi}}(f*g)(x)$,
and with $(2\pi)^{-3/2}$ in three dimensions (eqs. 20.68–20.69). Their
convolution theorem then carries no constant. This is a difference of
convention, not of claim, and concept pages use the unnormalized $f*g$ above.
Their Laplace convolution $\int_0^t f(t-u)\,g(u)\,\mathrm du$ (eq. 20.187) is
Riley et al.'s one-sided form, which they state "can be shown" to be
symmetric (eq. 20.188). They write both with the same symbol $*$, and they
note the German name *Faltung* ("folding"): as a function of $u$, $f(x - u)$
is $f(u)$ folded about $u = x/2$ (fig. 20.7, p. 986). For multiple convolutions the order does not
matter (p. 991), consistent with commutativity and associativity. The
discrete, cyclic analogue is on the
[discrete Fourier transform](/definitions/discrete-fourier-transform.md) page.

## Interpretation

The source motivates convolution by measurement. A true distribution $f$
observed through an apparatus whose resolution function $g(y)\,\mathrm dy$
is the probability that a true value is recorded displaced by $y$ gives the
observed distribution $q = f * g$, "broader and smoother than the true one".
A biased $g$ displaces the maxima, and $g = \delta$ gives $q = f$ (§13.1.7,
pp. 446–447). Convolving with $\delta(x+a) + \delta(x-a)$ places a copy of $g$
at each delta: $q(z) = g(z+a) + g(z-a)$ (worked example, p. 447).

Arfken et al. give two further readings. The potential of a charge
distribution is the convolution of the density with $1/r$, which "suggests
that convolutions will arise in a wide variety of problems in which there is
a distributed source of almost any kind and an effect therefrom that depends
on relative position" (Example 20.4.1, p. 989). A linear device that multiplies
each frequency component of its input by a **transfer function** produces an
output that is the convolution of the input with the device's response in
time. Causality, a response that vanishes for negative time lag, makes the real
and imaginary parts of the transfer function mutually dependent (§20.5,
eqs. 20.102–20.113, pp. 998–1001). A compiler remark: Riley et al.'s resolution
function plays the role of that response.

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
* [Arfken et al. (2013)](/sources/arfken-2013.md), §20.4 (eqs. 20.68–20.69, 20.79, 20.83, pp. 986–991), §20.5 (pp. 997–1001), §20.9 (eqs. 20.187–20.188, p. 1035).
