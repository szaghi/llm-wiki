---
type: Benchmark
title: "Square wave"
description: "The odd, period-T function equal to -1 on the first half-period and +1 on the second; its Fourier series contains only odd sine harmonics with amplitudes 4/(pi m), and it serves as the test function for convergence at a jump (to 0), the Gibbs overshoot, and Parseval's power partition."
status: established
aliases: [square-wave function, square-wave signal]
tags: [fourier-series, discontinuity, benchmark-function]
timestamp: 2026-10-13T00:00:00Z
---

# Square wave

The **square wave** of period $T$ is
$$f(t) = \begin{cases}-1, & -\tfrac12T \le t < 0,\\ +1, & 0 \le t < \tfrac12T,\end{cases}$$
extended periodically ([Riley et al. (2006)](/sources/riley-2006.md), §12.2,
fig. 12.2, p. 418). It models a circuit input switching between two states.

## Fourier series

It is odd, so all $a_m = 0$, and even about $t = T/4$, so $b_{2p} = 0$
(§12.3, p. 420). Only odd sine harmonics remain:
$b_m = \frac{2}{\pi m}[1 - (-1)^m]$, i.e. $4/(\pi m)$ for odd $m$, and
(eq. 12.8)
$$f(t) = \frac4\pi\left(\sin\omega_1 t + \frac{\sin 3\omega_1 t}{3} + \frac{\sin 5\omega_1 t}{5} + \cdots\right),\qquad \omega_1 = \frac{2\pi}{T}.$$
The coefficients decay only as $1/m$.

## What it tests

* **Convergence at a jump.** At $t = 0$ every term vanishes, so the series
  gives $0$, the mean of $\pm1$, as the
  [midpoint rule](/results/fourier-series-convergence.md) predicts (p. 421).
* **Gibbs phenomenon.** Partial sums with 1, 2, 3 and 20 terms show an
  overshoot that narrows towards the jump but persists (fig. 12.3; see
  [Gibbs phenomenon](/results/gibbs-phenomenon.md)).
* **Parseval.** With $\hat f_{\pm m} = \mp 2\mathrm i/(\pi m)$ for odd $m$
  and $\sum_{p\ge0}(2p+1)^{-2} = \pi^2/8$, the coefficients carry the full
  mean square $1$. The modes $m = \pm1, \pm3$ alone carry more than 90% of
  it (exercise 12.19 and answer, pp. 429, 431; see
  [Parseval's theorem](/results/parseval-theorem.md)).
* **Cosine form.** Shifting the origin by $T/4$ turns it into a cosine series
  (exercise 12.4).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§12.2–12.4 (pp. 418–421), fig. 12.3; exercises 12.4, 12.19.
