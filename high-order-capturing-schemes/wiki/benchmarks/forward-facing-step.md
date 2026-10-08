---
type: Benchmark
title: "Mach 3 wind tunnel with a forward-facing step"
description: "Woodward–Colella Mach 3 inflow over a step (0.2 high at x = 0.6 in a [0,3]×[0,1] tunnel): reflected shocks, a Mach stem and a vortex sheet from it, plus a corner singularity."
status: established
aliases: [forward facing step, Mach 3 step]
tags: [benchmark, euler, 2d, vortex-sheet]
timestamp: 2026-10-08T00:00:00Z
---

# Mach 3 wind tunnel with a forward-facing step

**Set-up** (Woodward & Colella). A tunnel 1 wide and 3 long; a step
0.2 high with its corner at $(0.6, 0.2)$; Mach 3 inflow
($\rho = 1.4$, $p = 1$, $\gamma = 1.4$) at the left, outflow at the
right, reflecting walls; the corner singularity treated as Woodward and
Colella did ([Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3
Example 2; [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.a).

**Results.**
* WENO-LF-4 and WENO-LF-5 on $122\times 39$ and $242\times 79$ resolve the
  contact from the Mach stem slightly better than ENO-LF-4, with fewer
  small bumps; the pressure–entropy-weight version fails at the strong
  reflected waves ([Jiang & Shu (1996)](/sources/jiang-1996.md)).
* $r = 5$ MPWENO with RF fluxes and no compression on $240\times 80$ to
  $t = 4$ gives sharp shocks and a vortex sheet a few zones wide, with
  little spreading along the domain
  ([Balsara & Shu (2000)](/sources/balsara-2000.md), Fig. 6).

**Later uses (batch 2).** WENO-AO(7,5,3) on $600 \times 200$ shows a
crisp vortex-sheet roll-up at $t = 3$, compared with WENO-ZQ
([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)); WENO-ZQ and
WENO-JS at $600 \times 200$, $t = 4$ ([Zhu & Qiu (2016)](/sources/zhu-2016.md)).

**Later uses (batch 3).** Fifth-order HLL-based AFD-WENO on
$1440\times480$ to $t = 0.4$, with the corner singularity treated as by
Woodward–Colella and with flattening, gives sharp profiles and a
pronounced roll-up of the vortex sheet
([Balsara et al. (2025)](/sources/balsara-2025.md), §VIII.a).

**Later uses (batch 4).**
* Fourth-order ADER-WENO at $240\times80$, $480\times160$ and
  $960\times320$ to $t = 4$. Roll-up of the vortex sheet starts at
  $480\times160$. The authors judge that an exceptionally good second-order
  scheme would need $960\times320$ to show it ([Balsara et al. (2009)](/sources/balsara-2009.md), §6.3).
* Third-order ADER-WENO on AMR (equivalent $2400\times800$, $t = 2.5$)
  rolls up the slip line much better than a second-order AMR run
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4; [high-order AMR](/methods/high-order-amr.md)).
* ADER-DG with $K = 5$ and subcell limiting on $300\times100$ to $t = 4$.
  Kelvin–Helmholtz vortices along the upper shear layer emit acoustic
  waves visible in the isolines, and limiting is confined to the
  shocks ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.5). With AMR, on a $150\times50$ base and
  $r_{\mathrm{AMR}} = 4$, the instability is well resolved
  ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.4).

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 2.
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.a.
3. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.6.
4. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Example 3.9.
5. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VIII.a.
6. [Balsara et al. (2009)](/sources/balsara-2009.md), §6.3.
7. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
8. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.5.
9. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.4.
