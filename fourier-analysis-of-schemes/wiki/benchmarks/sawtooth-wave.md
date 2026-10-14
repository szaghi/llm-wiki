---
type: Benchmark
title: "Sawtooth wave"
description: "The odd, period-L function equal to x on -L/2 < x < L/2, with a jump of size L at the period ends; its sine coefficients alternate in sign and decay only as 1/m, and it tests convergence to the mean at a jump, the persistent overshoot, failed term-by-term differentiation and successful term-by-term integration."
status: established
aliases: [sawtooth wave form, f(x) = x, saw-tooth function]
tags: [fourier-series, discontinuity, benchmark-function]
timestamp: 2026-10-14T00:00:00Z
---

# Sawtooth wave

The **sawtooth wave** of period $L$ is $f(x) = x$ on $-L/2 < x < L/2$,
extended periodically. It is odd and jumps by $L$ at $x = \pm L/2$.
[Arfken et al. (2013)](/sources/arfken-2013.md) use $L = 2\pi$ and write it
on $[0, 2\pi)$ as $x$, then $x - 2\pi$ (eq. 19.8, fig. 19.1), and note that
it is the same as $f(x) = x$ on $-\pi < x < \pi$ with "the discontinuity …
simply … moved to the ends of the interval" (p. 939).
[Riley et al. (2006)](/sources/riley-2006.md) use $L = 4$ (eq. 12.12).

## Fourier series

Only sine terms appear, with
$$b_m = \frac{L}{\pi}\,\frac{(-1)^{m+1}}{m},\qquad \hat f_m = \frac{\mathrm iL\,(-1)^m}{2\pi m}\ (m\ne0),\qquad \hat f_0 = 0.$$
Both printed cases are instances: $f(x) = 2\sum_{m\ge1}(-1)^{m+1}\sin(mx)/m$
for $L = 2\pi$ (eqs. 19.9, 19.19; exercise 19.2.7), and
$\hat f_m = 2\mathrm i(-1)^m/(\pi m)$ for $L = 4$ (Riley et al., eq. 12.12).
The general-$L$ form is the compiler's rescaling of the two. The coefficients
decay only as $1/m$, the rate the source expects of a discontinuous function
(p. 951; see [convergence of Fourier series](/results/fourier-series-convergence.md)).

## What it tests

* **Convergence at the jump.** Partial sums of 4, 6 and 10 terms (fig. 19.2)
  show "a steady increase in the accuracy of the representation", and at
  $x = \pi$, where $f$ jumps from $+\pi$ to $-\pi$, "all the curves pass through
  the average of these two values", $0$ (Arfken et al., p. 938).
* **Overshoot.** "In the vicinity of the discontinuity … there is an overshoot
  that persists and shows no sign of diminishing" (p. 938); see
  [Gibbs phenomenon](/results/gibbs-phenomenon.md).
* **Term-by-term differentiation fails.** Differentiating eq. 19.19 gives
  $1 = 2\sum_{m\ge1}(-1)^{m+1}\cos mx$ (eq. 19.20), "which is not convergent.
  Warning: Check your derivative for convergence" (p. 943).
* **Term-by-term integration succeeds.** Integrating the series gives
  $\pi^2/12 = \sum_{m\ge1}(-1)^{m+1}/m^2$ (exercise 19.1.12, p. 947).
* **A summation.** At $x = \pi/2$ the series gives Leibniz's
  $\pi/4 = 1 - \tfrac13 + \tfrac15 - \cdots$ (pp. 938–939).
* **Choice of extension.** Given only on $[0, \pi]$, $f(x) = x$ has this sine
  series, a cosine series $\frac\pi2 - \frac4\pi\sum_{p\ge0}\frac{\cos(2p+1)x}{(2p+1)^2}$
  (the continuous triangular wave, coefficients $\sim m^{-2}$), and its power
  series. All three represent $f$ on $[0, \pi]$ and differ "strikingly" outside
  it (Example 19.1.2, fig. 19.3). The triangular wave differentiates term by
  term into the [square wave](/benchmarks/square-wave.md) (eqs. 19.21–19.23).

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §19.1 (eqs. 19.8–19.9, 19.18–19.23, Examples 19.1.1–19.1.2, figs. 19.1–19.3, pp. 937–944), §19.2 (p. 951); exercises 19.1.12, 19.2.7.
* [Riley et al. (2006)](/sources/riley-2006.md), §12.7 (eq. 12.12, p. 425).
