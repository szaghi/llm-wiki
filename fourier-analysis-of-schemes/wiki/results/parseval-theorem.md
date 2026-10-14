---
type: Result
title: "Parseval's theorem"
description: "The mean of |f|^2 over a period equals the sum of |f-hat_m|^2 over the Fourier-series coefficients, and for the unitary Fourier transform the integral of |f|^2 equals the integral of |f-hat|^2; both follow from the general multiplication theorem, and the series form is a special case of the transform form."
status: established
aliases: [Parseval's identity, Parseval relation, multiplication theorem, Plancherel theorem]
tags: [fourier-series, fourier-transform, spectrum, energy]
timestamp: 2026-10-13T00:00:00Z
---

# Parseval's theorem

## Fourier series

For $f$ of period $L$ with complex coefficients $\hat f_m$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 12.13):
$$\frac1L\int_{x_0}^{x_0+L}\lvert f(x)\rvert^2\,\mathrm dx = \sum_{m=-\infty}^{\infty}\lvert\hat f_m\rvert^2 = \left(\tfrac12 a_0\right)^2 + \tfrac12\sum_{m=1}^{\infty}\bigl(a_m^2 + b_m^2\bigr).$$
In words, the average of $\lvert f\rvert^2$ over a period equals the sum of
the squared moduli of the complex coefficients. The source calls it
"essentially a conservation law". It is proved through the more general form,
for $f$ and $g$ of the same period with coefficients $\hat f_m$ and $\hat g_m$
(§12.8, p. 426):
$$\frac1L\int_{x_0}^{x_0+L} f(x)\,g^*(x)\,\mathrm dx = \sum_{m=-\infty}^{\infty}\hat f_m\,\hat g_m^{*},$$
whose real-coefficient form is the subject of exercise 12.25. The proof
exchanges sum and integral without comment.

## Fourier transform

With the unitary [Fourier transform](/definitions/fourier-transform.md), setting
$z = 0$ in the [Wiener–Khinchin](/results/wiener-khinchin-theorem.md) form of
the cross-correlation gives the **multiplication theorem** (eq. 13.45) and,
for $g = f$, the common form (eq. 13.46):
$$\int_{-\infty}^{\infty} f^*(x)\,g(x)\,\mathrm dx = \int_{-\infty}^{\infty}\hat f^*(k)\,\hat g(k)\,\mathrm dk,\qquad
\int_{-\infty}^{\infty}\lvert f(x)\rvert^2\,\mathrm dx = \int_{-\infty}^{\infty}\lvert\hat f(k)\rvert^2\,\mathrm dk.$$
No constant appears because of the symmetric normalization. The source states
that the series form "is in fact a special case of (13.46)" (§13.1.9, p. 451),
without showing the reduction.

## Uses and interpretation

* **Energy.** When $f$ is a physical amplitude both sides are a total
  intensity. For a damped oscillator, $\lvert\hat f(\omega)\rvert^2$ is the
  energy per unit frequency interval, and the theorem equates two
  specifications of the total energy "to within a constant" (p. 451).
  The printed transform in that example omits the factor $1/\sqrt{2\pi}$ of
  the definition (13.5), although it says "Using the usual definition"; the
  hedge "to within a constant" absorbs the discrepancy.
* **Summing series.** From the series of $x^2$ on $(-2, 2]$ it gives
  $\sum_{m\ge1} m^{-4} = \pi^4/90$ (p. 427). The source notes that useful
  summations "are nearly always found serendipitously".
* **Spectral content of a truncated signal.** Exercise 12.19: for the
  [square wave](/benchmarks/square-wave.md), the modes $m = \pm1, \pm3$ (a
  filter passing frequencies up to $8\pi/T$) carry more than 90% of the power
  (answer, p. 431).
* **Best approximation.** Exercise 12.26 asks for the sine coefficients that
  minimize the squared deviation
  $\int_{-\pi}^{\pi}\bigl[f - \sum_{m=1}^{M} b_m\sin mx\bigr]^2\,\mathrm dx$ of
  a truncated series. The source leaves the result to the reader.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §12.8 (pp. 426–427), §13.1.9 (pp. 450–451); exercises 12.19, 12.25, 12.26.
