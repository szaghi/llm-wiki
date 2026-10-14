---
type: Benchmark
title: "Exponential-decay test equation"
description: "The initial-value problem dy/dt = -y, y(0) = 1, with exact solution exp(-t), used to compare forward Euler at several steps and Milne's two-step method against the exact values and to exhibit oscillation, divergence and parasitic growth of difference schemes."
status: established
aliases: [decay equation, dy/dt = -y, linear test equation]
tags: [time-integration, stability, benchmark-function]
timestamp: 2026-10-13T00:00:00Z
---

# Exponential-decay test equation

$$\frac{\mathrm dy}{\mathrm dt} = -y,\qquad y(0) = 1,\qquad y(t) = e^{-t}$$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 27.61). It is the linear
test equation $\mathrm dy/\mathrm dt = \lambda y$ with $\lambda = -1$. The
source uses it because comparing against the exact solution is then easy
(§27.6, p. 1020).

## Results printed for it

* [Forward Euler](/methods/forward-euler-method.md), table 27.10, with
  $\Delta t = 0.01, 0.1, 0.5, 1, 1.5, 2, 3$ up to $t = 3$. Accuracy needs very
  small steps. $\Delta t = 1$ gives $y^n = 0$ after one step; for
  $\Delta t > 1$ the solution oscillates and for $\Delta t > 2$ it diverges
  (p. 1021). At $t = 3$ the printed values are $0.049$ ($\Delta t = 0.01$),
  $0.042$ ($0.1$) and $0.016$ ($0.5$), against $0.050$.
* [Milne's central-difference method](/methods/milne-central-difference-method.md),
  table 27.11, $\Delta t = 0.5$ with the exact second starting value. The
  values are better early but go negative by $t = 3$ ($-0.184$ against
  $0.050$).

## Why it is a stability test

The source points out that the companion equation $\mathrm dy/\mathrm dt = +y$
has the growing solution $e^{t}$, and that rounding errors "effectively
introduce" it into the computed solution, where it ultimately dominates
(p. 1022). The test equation thus separates a scheme's accuracy from its
tendency to amplify perturbations, though the source illustrates this and
does not analyse it.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.6.1 (eq. 27.61, tables 27.10–27.11, pp. 1020–1023).
