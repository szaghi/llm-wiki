---
type: Benchmark
title: "Square wave"
description: "The odd, period-T function equal to -1 on the first half-period and +1 on the second; its Fourier series contains only odd sine harmonics with amplitudes 4/(pi m), and it serves as the test function for convergence at a jump (to 0), the Gibbs overshoot (quantified on it as about 18% of the half-jump), and Parseval's power partition."
status: established
aliases: [square-wave function, square-wave signal]
tags: [fourier-series, discontinuity, benchmark-function]
timestamp: 2026-10-14T00:00:00Z
---

# Square wave

The **square wave** of period $T$ is
$$f(t) = \begin{cases}-1, & -\tfrac12T \le t < 0,\\ +1, & 0 \le t < \tfrac12T,\end{cases}$$
extended periodically ([Riley et al. (2006)](/sources/riley-2006.md), §12.2,
fig. 12.2, p. 418). It models a circuit input switching between two states.
[Arfken et al. (2013)](/sources/arfken-2013.md) use period $2\pi$ and two
offsets. Example 19.2.1 takes values $0$ and $h$ (eqs. 19.25–19.26), and §19.3
takes $\pm h/2$ (eqs. 19.32–19.33). The second with $h = 2$ and $T = 2\pi$ is
Riley et al.'s wave. Arfken et al. place it in "electronic circuits designed to
handle sharply rising pulses" (p. 949).

## Fourier series

It is odd, so all $a_m = 0$, and even about $t = T/4$, so $b_{2p} = 0$
(§12.3, p. 420). Only odd sine harmonics remain:
$b_m = \frac{2}{\pi m}[1 - (-1)^m]$, i.e. $4/(\pi m)$ for odd $m$, and
(eq. 12.8)
$$f(t) = \frac4\pi\left(\sin\omega_1 t + \frac{\sin 3\omega_1 t}{3} + \frac{\sin 5\omega_1 t}{5} + \cdots\right),\qquad \omega_1 = \frac{2\pi}{T}.$$
The coefficients decay only as $1/m$. Arfken et al. print the same series
(eqs. 19.26, 19.33). They note that the odd terms "fall only as $n^{-1}$", a
conditional convergence. "Physically this means that our square wave contains
a lot of high-frequency components. If the electronic apparatus will not pass
these components, our square-wave input will emerge more or less rounded off"
(p. 950).

## What it tests

* **Convergence at a jump.** At $t = 0$ every term vanishes, so the series
  gives $0$, the mean of $\pm1$, as the
  [midpoint rule](/results/fourier-series-convergence.md) predicts (p. 421).
* **Gibbs phenomenon.** Partial sums with 1, 2, 3 and 20 terms show an
  overshoot that narrows towards the jump but persists (fig. 12.3; see
  [Gibbs phenomenon](/results/gibbs-phenomenon.md)). Arfken et al. derive the
  overshoot on this wave. With $M$ terms the peak lies near $x \approx \pi/M$,
  and its height is $1.1789797\ldots$ times the corner value, "some 18%" above
  it (eqs. 19.37–19.43, fig. 19.11 with 20 to 100 terms, pp. 959–961).
* **Parseval.** With $\hat f_{\pm m} = \mp 2\mathrm i/(\pi m)$ for odd $m$
  and $\sum_{p\ge0}(2p+1)^{-2} = \pi^2/8$, the coefficients carry the full
  mean square $1$. The modes $m = \pm1, \pm3$ alone carry more than 90% of
  it (exercise 12.19 and answer, pp. 429, 431; see
  [Parseval's theorem](/results/parseval-theorem.md)). Arfken et al.'s
  exercise 19.1.13(c) uses this wave to show that Parseval's identity does not
  need the uniform convergence assumed in their derivation.
* **Derivative of a continuous wave.** The term-by-term derivative of the
  triangular wave's series is this series (Arfken et al., eqs. 19.21–19.23;
  see [convergence of Fourier series](/results/fourier-series-convergence.md)),
  and integrating the series of $\delta$ on $(-\pi, \pi)$ gives it as well
  (exercise 19.2.4).
* **Cosine form.** Shifting the origin by $T/4$ turns it into a cosine series
  (exercise 12.4).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§12.2–12.4 (pp. 418–421), fig. 12.3; exercises 12.4, 12.19.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §19.2 (Example 19.2.1, pp. 949–950), §19.3 (eqs. 19.32–19.43, pp. 958–961), §19.1 (eqs. 19.21–19.23, p. 943); exercises 19.1.13, 19.2.4.
