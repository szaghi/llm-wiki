---
type: Result
title: "Gibbs phenomenon"
description: "At a jump discontinuity the partial sums of a Fourier series overshoot the function; as more terms are added the overshoot moves arbitrarily close to the discontinuity but never disappears, and its size is proportional to the magnitude of the jump (stated without proof or numerical value)."
status: established
aliases: [Gibbs' phenomenon, Gibbs overshoot, Gibbs oscillations]
tags: [fourier-series, discontinuity, convergence]
timestamp: 2026-10-13T00:00:00Z
---

# Gibbs phenomenon

At a point of finite discontinuity, the partial sums $S_M f$ of a
[Fourier series](/definitions/fourier-series.md) overshoot the function. "Although as more
terms are included the overshoot moves in position arbitrarily close to the
discontinuity, it never disappears even in the limit of an infinite number of
terms. This behaviour is known as Gibbs' phenomenon"
([Riley et al. (2006)](/sources/riley-2006.md), §12.4, pp. 420–421).

The source states one quantitative property: "the size of the overshoot is
proportional to the magnitude of the discontinuity".

## Scope

* No proof and no value of the overshoot are given ("A full discussion is not
  pursued here", p. 421). In particular the source does not state the
  overshoot as a fraction of the jump. That figure waits for a source that
  derives it.
* The statement concerns partial sums. It coexists with
  [pointwise convergence](/results/fourier-series-convergence.md) to the
  midpoint *at* the jump: the overshoot is not at a fixed point but moves
  towards the jump as $M$ grows.
* The phenomenon is illustrated on the [square wave](/benchmarks/square-wave.md)
  with 1, 2, 3 and 20 terms (fig. 12.3). The overshoot marked in panel (d)
  (labelled delta there) is not quantified.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §12.4 (pp. 420–421), fig. 12.3.
