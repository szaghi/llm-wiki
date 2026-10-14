---
type: Method
title: "Milne's central-difference method"
description: "The two-step recurrence y^{n+1} = y^{n-1} + 2 Delta t F(t^n, y^n) from the central difference, needing a second starting value; on the decay equation with Delta t = 0.5 and exact starting values it is more accurate early but soon oscillates with growing amplitude, which the source attributes to rounding errors exciting the growing solution exp(+t)."
status: established
aliases: [Milne's method, leapfrog method, explicit midpoint rule, central-difference method]
tags: [time-integration, stability, finite-difference]
timestamp: 2026-10-13T00:00:00Z
---

# Milne's central-difference method

Replacing the derivative by the [central difference](/operators/central-difference.md)
$D_0$ in time gives the two-step recurrence
([Riley et al. (2006)](/sources/riley-2006.md), eq. 27.64)
$$y^{n+1} = y^{n-1} + 2\Delta t\,F(t^n, y^n),$$
which the source calls "a more accurate method based on central differences
(Milne's method)" (p. 1022). The aliases *leapfrog* and *explicit midpoint*
are the compiler's identification of the same formula; the source does not
use them. Two starting values are needed. The second "must be estimated by
other means (e.g. by using a Taylor series ...)".

## Behaviour on the decay equation

For the [exponential-decay test equation](/benchmarks/exponential-decay-test-equation.md),
$y^{n+1} = y^{n-1} - 2\Delta t\,y^n$ (eq. 27.65). With $\Delta t = 0.5$ and the
exact starting value $y^{-1} = e^{\Delta t}$, table 27.11 gives

| $t$ | $0.5$ | $1.0$ | $1.5$ | $2.0$ | $2.5$ | $3.0$ |
|---|---|---|---|---|---|---|
| $y^n$ | $0.648$ | $0.352$ | $0.296$ | $0.056$ | $0.240$ | $-0.184$ |
| $e^{-t}$ | $0.607$ | $0.368$ | $0.223$ | $0.135$ | $0.082$ | $0.050$ |

The early values improve on forward Euler at the same step, but "this scheme
soon runs into difficulties". The source's diagnosis (p. 1022): "Some part of
this poor performance is not really attributable to the approximations made
in estimating" the derivative "but to the form of the equation itself".
In its words, "any rounding error occurring in the evaluation effectively
introduces into $y$ some contamination by the solution of"
$\mathrm dy/\mathrm dt = +y$, which, being $e^{t}$, "grows without limit;
ultimately it will dominate". The source states that it has "only illustrated, rather than
analysed" these difficulties (p. 1022).

## Compiler's note (derivation, hypothesis)

Not in the source. The recurrence $y^{n+1} + 2\Delta t\,y^n - y^{n-1} = 0$ has
solutions $y^n = G^n$ with $G^2 + 2\Delta t\,G - 1 = 0$, so
$$G_{1,2} = -\Delta t \pm\sqrt{1 + \Delta t^2}.$$
$G_1 \approx 1 - \Delta t$ follows the decaying solution. The parasitic root
$G_2 = -\Delta t - \sqrt{1+\Delta t^2}$ has $\lvert G_2\rvert > 1$ for **every**
$\Delta t > 0$, and it alternates in sign. At $\Delta t = 0.5$,
$G_1 \approx 0.618$ (against $e^{-0.5} \approx 0.607$) and $G_2 \approx -1.618$.
The growing mode is therefore excited by any departure from the pure $G_1$
solution, the starting and truncation errors included, not only by rounding.
Even the "accurate" starting value $y^{-1} = e^{\Delta t}$ excites it, because
$G_1 \ne e^{-\Delta t}$. This matches the sign-alternating growth of
table 27.11. A source on the stability of multistep methods would confirm
or correct this note.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.6.1 (eqs. 27.64–27.65, table 27.11, pp. 1022–1023).
