---
type: Result
title: "Laplace transform properties"
description: "Operational rules of the Laplace transform: the transform of the p-th derivative is s^p times the transform minus a polynomial in s carrying the initial values, integration divides by s, multiplication by exp(a t) shifts s, multiplication of the transform by exp(-b s) delays f, plus scaling, multiplication by t^p, division by t, and (exercises) the limits s L[f] -> A as s -> 0 and s L[f] -> f(+0) as s -> infinity."
status: established
aliases: [Laplace transform of derivatives, s-shift theorem, t-shift theorem, final value theorem]
tags: [laplace-transform, initial-value-problem]
timestamp: 2026-10-14T00:00:00Z
---

# Laplace transform properties

Rules for the [Laplace transform](/definitions/laplace-transform.md)
$\mathcal L\{f\}(s) = \int_0^\infty f(t)e^{-st}\,\mathrm dt$
([Riley et al. (2006)](/sources/riley-2006.md), §§13.2.1–13.2.2, pp. 455–459).

## Derivatives and integrals

Integration by parts gives (eqs. 13.57–13.58)
$$\mathcal L\{f'\} = s\,\mathcal L\{f\} - f(0),\qquad
\mathcal L\!\left[f^{(p)}\right] = s^p\,\mathcal L\{f\} - s^{p-1}f(0) - s^{p-2}f'(0) - \dots - f^{(p-1)}(0),$$
and (eq. 13.59)
$$\mathcal L\!\left[\int_0^t f(u)\,\mathrm du\right] = \frac1s\,\mathcal L\{f\}.$$
The initial values enter the transformed equation directly, which is why the
source introduces the transform for initial-value problems. The derivative
rules are printed "for $s > 0$" (eqs. 13.57–13.58), not for $s > s_0$. A
compiler remark: the boundary term $f(t)e^{-st}\to0$ as $t\to\infty$ needs $s$
above the growth rate of $f$, so the printed $s > 0$ is the condition for
bounded $f$.

[Arfken et al. (2013)](/sources/arfken-2013.md) print the same rules
(eqs. 20.147–20.149) with the initial values taken as one-sided limits,
$f(+0)$, $f'(+0)$, …. They require $f'$ "at least piecewise continuous", and $f$ and $f'$
to be such that "the integrals do not diverge" (p. 1016). They state no fixed bound on $s$. This is a qualification
of the printed "$s > 0$", consistent with the compiler remark above. The
integral rule follows from the convolution theorem (their exercise 20.9.1).

## Shifts and other rules

| Rule | Statement | Eq. |
|---|---|---|
| $s$-shift | $\mathcal L\{e^{at}f(t)\} = \mathcal L\{f\}(s - a)$ | 13.60 |
| $t$-shift (delay) | $e^{-bs}\mathcal L\{f\}(s)$, $b > 0$, is the transform of $f(t - b)$ for $t > b$, zero for $0 < t \le b$ | p. 457 |
| Scaling | $\mathcal L\{f(at)\} = \frac1a\,\mathcal L\{f\}(s/a)$ | 13.61 |
| Multiplication by $t^p$ | $\mathcal L\{t^pf(t)\} = (-1)^p\frac{\mathrm d^p}{\mathrm ds^p}\mathcal L\{f\}(s)$, $p = 1, 2, \dots$ | 13.62 |
| Division by $t$ | $\mathcal L\{f(t)/t\} = \int_s^\infty\mathcal L\{f\}(u)\,\mathrm du$, provided $\lim_{t\to0}f(t)/t$ exists | 13.63 |
| Convolution | $\mathcal L\{f * g\} = \mathcal L\{f\}\,\mathcal L\{g\}$ (one-sided convolution) | 13.64 |

Arfken et al. print every rule of this table (table 20.2; eqs. 20.156
scaling, 20.157 substitution, 20.166 translation, 20.174 derivative of a
transform, 20.184 integral of a transform, 20.186 convolution), and they agree
with it. They call the delay rule the **Heaviside shifting theorem**
(p. 1023). Their condition for the division rule is weaker than Riley et
al.'s: $f(t)/t$ "finite at $t = 0$ or diverges less strongly than $t^{-1}$"
(p. 1027), against "$\lim_{t\to0}f(t)/t$ exists". The two do not conflict.
They also give the complex-variable inversion (the Bromwich integral, see
[Laplace transform](/definitions/laplace-transform.md)).

The convolution rule is on the [convolution theorem](/results/convolution-theorem.md)
page.

## Exercises

* **Limit $s\to0$** (exercise 13.25a). If $f = A + g$, $A$ constant, with
  $\int^t g$ bounded as $t\to\infty$, then $\lim_{s\to0}s\,\mathcal L\{f\}(s) = A$.
  Part (b) applies it to a damped, driven second-order equation and reads the
  limit as the long-time mean of $y$. The source does not name it the final
  value theorem.
* **Periodic functions** (exercise 13.28). For $g$ of period $T$,
  $\mathcal L\{g\}(s) = \frac{1}{1 - e^{-sT}}\int_0^T e^{-st}g(t)\,\mathrm dt$.
  Arfken et al.'s exercise 20.8.20 states the same.
* **Limit $s\to\infty$** (Arfken et al., exercise 20.7.1). If $f$ has a power
  series in $t$, $\lim_{s\to\infty}s\,\mathcal L\{f\}(s) = \lim_{t\to+0}f(t)$.
  The source does not name it the initial value theorem.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§13.2.1–13.2.2 (pp. 455–459); exercises 13.25, 13.28 (pp. 465–466).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §20.8 (eqs. 20.147–20.184, table 20.2, pp. 1016–1028), §20.9 (p. 1035); exercises 20.7.1, 20.8.20, 20.9.1.
