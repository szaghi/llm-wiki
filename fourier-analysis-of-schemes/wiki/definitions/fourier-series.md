---
type: Definition
title: "Fourier series"
description: "Expansion of a periodic function of period L in the mutually orthogonal modes cos and sin of k_m x (real form) or exp(i k_m x) (complex form), with coefficients given by integrals over one period; symmetry of the function removes coefficient families, and a function on a finite range is expanded through a chosen periodic extension."
status: established
aliases: [trigonometric series, complex Fourier series, Fourier coefficients, half-range series, periodic extension]
tags: [fourier-series]
timestamp: 2026-10-13T00:00:00Z
---

# Fourier series

The **Fourier series** of a function $f(x)$ of period $L$ is its expansion in
sines and cosines of the wavenumbers $k_m = 2\pi m/L$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 12.4):
$$f(x) = \frac{a_0}{2} + \sum_{m=1}^{\infty}\bigl[a_m\cos k_m x + b_m\sin k_m x\bigr],$$
with the **Fourier coefficients** (eqs. 12.5–12.6)
$$a_m = \frac2L\int_{x_0}^{x_0+L} f(x)\cos k_m x\,\mathrm dx,\qquad b_m = \frac2L\int_{x_0}^{x_0+L} f(x)\sin k_m x\,\mathrm dx,$$
where $x_0$ is arbitrary (often $0$ or $-L/2$). The factor $\tfrac12$ on $a_0$
makes the formula for $a_m$ hold at $m = 0$ as well. A function that may be
expanded this way is one satisfying the
[Dirichlet conditions](/definitions/dirichlet-conditions.md).

## Orthogonality

The coefficient formulas follow from the orthogonality of the modes over one
period (eqs. 12.1–12.3), for integers $m, p \ge 0$:
$$\int_{x_0}^{x_0+L}\sin k_m x\cos k_p x\,\mathrm dx = 0,\qquad
\int_{x_0}^{x_0+L}\cos k_m x\cos k_p x\,\mathrm dx = \begin{cases}L & m=p=0\\ \tfrac12 L & m=p>0\\ 0 & m\ne p\end{cases},$$
and the same for $\sin\sin$ except that it vanishes for $m = p = 0$.
Multiplying the series by $\cos k_p x$ (or $\sin k_p x$), integrating over a
period and exchanging sum and integral isolates one coefficient (eq. 12.7);
the source does not discuss the legitimacy of that exchange.

## Complex form

With $e^{\mathrm i u} = \cos u + \mathrm i\sin u$ the series is
(eqs. 12.9–12.10)
$$f(x) = \sum_{m=-\infty}^{\infty}\hat f_m\,e^{\mathrm i k_m x},\qquad \hat f_m = \frac1L\int_{x_0}^{x_0+L} f(x)\,e^{-\mathrm i k_m x}\,\mathrm dx,$$
derived from the orthogonality relation: $\int_{x_0}^{x_0+L} e^{-\mathrm i k_p x}e^{\mathrm i k_m x}\,\mathrm dx$
equals $L$ for $m = p$ and $0$ for $m \ne p$. The two forms are related by (eq. 12.11)
$$\hat f_m = \tfrac12(a_m - \mathrm i b_m),\qquad \hat f_{-m} = \tfrac12(a_m + \mathrm i b_m),$$
so that a real $f$ has $\hat f_{-m} = \hat f_m^{*}$ (§12.7, p. 425).

## Symmetry

(§12.3, pp. 419–420.)

* $f$ odd: all $a_m = 0$ (sine series). $f$ even: all $b_m = 0$ (cosine series).
* $f$ even about $L/4$, i.e. $f(L/4 - x) = f(x - L/4)$: $a_{2p+1} = 0$ and $b_{2p} = 0$.
* $f$ odd about $L/4$: $a_{2p} = 0$ and $b_{2p+1} = 0$.

The source calls the quarter-period results "less obvious" and less used; it
derives them from the substitution $s = x - L/4$.

## Non-periodic functions: periodic extension

A function wanted only on a finite range is first continued outside it to a
periodic function, whose series then represents it on that range only (§12.5,
pp. 422–424). The continuation is a choice. Continuing $f$ given on $0 < x \le L/2$
as an odd or an even function gives a sine-only or cosine-only series of
period $L$ (fig. 12.4). The source adds a constraint: the continuation
"must not be discontinuous at the end-points of the interval of interest; if
it is the series will not converge to the required value there" (p. 422).
Example: $f(x) = x^2$ on $0 < x \le 2$, continued evenly to period 4, gives
$$x^2 = \frac43 + 16\sum_{m=1}^\infty\frac{(-1)^m}{\pi^2 m^2}\cos\frac{\pi m x}{2},$$
whereas the odd continuation gives a sine series that converges to $0$, not to
$f(\pm 2) = \pm 4$, at $x = \pm 2$ (pp. 423–424; exercise 12.18). The choice of
continuation also sets the decay rate of the coefficients. Exercise 12.8 asks
for the faster-converging of the even and odd series of $x\sin x$ on
$[0,\pi]$ and states that it converges as $m^{-3}$. Exercise 12.6 asks which
of the sine and cosine series of $1 - x$ on $[0, 1]$ "would be better for
numerical evaluation", relating the answer to the continuations.

# Examples

* Square wave: see [square wave](/benchmarks/square-wave.md) (eq. 12.8).
* $f(x) = x$ on $-2 < x < 2$: $\hat f_m = \frac{2\mathrm i(-1)^m}{\pi m}$ for $m \ne 0$, $\hat f_0 = 0$ (eq. 12.12).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§12.1–12.3, 12.5, 12.7 (pp. 415–425); exercises 12.6, 12.8, 12.18.
