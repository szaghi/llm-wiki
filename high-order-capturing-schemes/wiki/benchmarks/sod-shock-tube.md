---
type: Benchmark
title: "Sod shock tube"
description: "The 1D Riemann problem (1, 0, 1 | 0.125, 0, 0.1): rarefaction, contact and shock with a monotone density profile; the baseline check of shock, contact and rarefaction resolution."
status: established
aliases: [Sod problem, Sod's problem]
tags: [benchmark, euler, riemann-problem, 1d]
timestamp: 2026-10-08T00:00:00Z
---

# Sod shock tube

**Set-up** (Sod 1978): $(\rho, v, p)_L = (1, 0, 1)$,
$(\rho, v, p)_R = (0.125, 0, 0.1)$, $\gamma = 1.4$
([Liu, Osher & Chan (1994)](/sources/liu-1994.md);
[Jiang & Shu (1996)](/sources/jiang-1996.md)). The density profile is
monotone, so intermediate states need not be "built up" — which makes it
an easier test than [Lax's](/benchmarks/lax-shock-tube.md)
([Harten et al. (1987)](/sources/harten-1987.md)).

**Uses.**
* Second- and fourth-order ENO with characteristic reconstruction;
  component-wise fourth-order ENO shows some noise, at a practically
  acceptable level ([Harten et al. (1987)](/sources/harten-1987.md),
  Figs. 9–11).
* With the self-similar Riemann solution, convergence of any scheme is
  limited to first order; comparisons should count time steps to resolved
  intermediate states ([Harten et al. (1987)](/sources/harten-1987.md)).
* Contact sharpening by subcell resolution and artificial compression
  ([Shu & Osher (1989)](/sources/shu-1989.md), Example 6).
* WENO $r = 3$ with Roe flux and characteristic reconstruction
  ([Liu, Osher & Chan (1994)](/sources/liu-1994.md), Example 4);
  WENO5 better than WENO5-PS, better than WENO3; artificial compression
  sharpens the contact most ([Jiang & Shu (1996)](/sources/jiang-1996.md)).
* MP5 resolves contact and shock sharply
  ([Suresh & Huynh (1997)](/sources/suresh-1997.md), Example 1).
* Central WENO: component-wise indicators give irregular weights at the
  contact; global indicators are better
  ([Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 5).
* Run with MPWENO with good results, not shown
  ([Balsara & Shu (2000)](/sources/balsara-2000.md)).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §7.
2. [Shu & Osher (1989)](/sources/shu-1989.md), Example 6.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), Example 4.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.2 Example 1.
5. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.2.
6. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 5.
7. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.b.
