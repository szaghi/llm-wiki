---
type: Benchmark
title: "Interacting blast waves"
description: "The Woodward–Colella problem of two strong blast waves between reflecting walls in a gamma = 1.4 gas, compared with a fine reference at t = 0.038 by the L1 density error; its discontinuities limit every scheme to at most first-order convergence, which only PPM reached in the original comparison and FLASH's AMR PPM reaches again."
status: established
aliases: [Woodward–Colella blast waves, two interacting blast waves, Woodward–Colella interacting blast waves, WC blast waves]
tags: [benchmark, hydro, verification, amr]
timestamp: 2026-10-13T00:00:00Z
---

# Interacting blast waves

**Set-up.** Introduced by [Woodward & Colella (1984)](/sources/woodward-1984.md)
(§IVa, p. 125), who credit its first appearance to Woodward (1982). A
$\gamma = 1.4$ gas at rest between **reflecting walls** a unit apart,
density 1 everywhere, pressure 1000 for $x < 0.1$, 0.01 in the middle and
100 for $x > 0.9$. Two strong blast waves and their rarefactions form,
reflect from the walls and collide at about $t = 0.028$, leaving several
contacts and shocks. The comparison time is **$t = 0.038$** (p. 129; p. 142
prints "0.38", a misprint). There is no exact solution: results are
measured against a fine-grid reference.

**Reference and error measure** (Woodward & Colella 1984, pp. 129, 142).
The reference is a special Lagrange-plus-remap PPM run that tracks three
distinct fluids, computes the early non-interacting phase exactly, and
refines by 8 in space and time near each discontinuity and both walls:
3096 zones of width 1/2400, with widths 1/4800 and 1/9600 in the collision
region. The error is the mean, over the $N$ zones of the coarse grid, of
the absolute difference between computed and reference zone-averaged
densities; the convergence rate is the one-sided slope of its logarithm
against $\log h$.

**Runs.**

* *Seven schemes, uniform grids* ([Woodward & Colella (1984)](/sources/woodward-1984.md),
  §VIa, Table I, Fig. 6). 100 to 2400 zones; Courant number 0.8 (0.4 for
  ETBFCT); CRAY-1 timings. Error at 200 → 1200 zones (finest-pair rate):

  | Scheme | 200 zones | 1200 zones | rate |
  |---|---|---|---|
  | MacCormack + Lapidus | 0.261 | 0.0862 | 0.72 |
  | BBC | 0.196 | 0.0717 | 0.64 |
  | ETBFCT | 0.227 | 0.0606 | 0.76 |
  | Godunov (first order) | 0.330 | 0.182 | 0.40 |
  | MUSCL | 0.162 | 0.0401 | 0.85 |
  | PPMDE | 0.0990 | 0.0144 | 1.07 |
  | PPMLR | 0.0760 | 0.0133 | 0.98 |

  "Only the error of the PPM scheme converges to zero as fast as
  [the zone width $h$]"; since the error concentrates at discontinuities it can
  converge "no faster than [$h$]" (p. 146). Matching the 200-zone
  PPMLR accuracy costs 1.6 (PPMDE) to 13.5 (ETBFCT) times the CPU time, and
  Godunov cannot match it "even if it is given twelve times as many zones".
  Most of the error sits at the left and central contacts; only PPM is
  "essentially converged" at 1200 zones. As printed, Godunov's error at 600
  zones (0.241) exceeds that at 400 (0.214).
* *PPM on AMR, FLASH* ([Fryxell et al. (2000)](/sources/fryxell-2000.md),
  §7.5, Figs. 32–33; [FLASH](/software/flash.md)). Reflecting walls,
  reference at 10 levels, $t = 0.038$; L1 self-convergence for 2 to 9 levels
  ($h = 1/16$ to 1/2048) is "only linear", and the authors recall that
  "Woodward & Colella (1984) found that only PPM achieved even linear
  convergence".
* *Athena* ([Stone et al. (2008)](/sources/stone-2008.md), §8). Listed among
  the 1D hydrodynamic tests of the CTU+CT code; no parameters or results
  are recorded in this bundle.

**What it shows.** The problem is a stress test of strong-shock and
contact capturing, not an order-of-accuracy test: with discontinuities
dominating the error, first order in $h$ is the ceiling, and schemes differ
in how close they get. Contact smearing decides the ranking (Godunov
smears contacts badly; PPM keeps the outer contacts one zone wide even at
200 zones). FLASH's linear rate agrees with the original's finding for PPM.

# Citations

1. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§IVa, VIa, Table I, Figs. 1–2, 6, pp. 125–146.
2. [Fryxell et al. (2000)](/sources/fryxell-2000.md), §7.5, Figs. 32–33.
3. [Stone et al. (2008)](/sources/stone-2008.md), §8.
