---
type: Benchmark
title: "Mach 3 forward-facing step"
description: "Two-dimensional Euler benchmark of Mach 3 flow in a wind tunnel with a step, run to t=4; it tests robustness at the expansion corner and the resolution of the Kelvin–Helmholtz roll-up of the vortex sheet from the triple point."
status: established
aliases: [forward-facing step, wind tunnel with a step, Mach 3 wind tunnel]
tags: [benchmark, low-dissipation, weno]
timestamp: 2026-10-22T00:00:00Z
---

# Mach 3 forward-facing step

A uniform Mach 3 flow of ideal gas enters a wind tunnel of unit height
containing a step of height $0.2$ whose corner sits at $(0.6,0.2)$. A bow
shock forms ahead of the step, reflects from the upper wall and the step
top, and a triple point forms on the upper wall from which a vortex
sheet trails downstream. The expansion corner of the step is a
singularity that strains robustness, and the vortex sheet is
Kelvin–Helmholtz unstable, so the benchmark measures both whether a
scheme survives and how much small-scale structure it resolves. Five
sources of the bundle run it; the three that name an origin attribute
it to Woodward & Colella.

## Setup

[Balsara et al. (2024)](/sources/balsara-2024.md) §IX.g and
[Li et al. (2022)](/sources/li-2022-b.md) §4.4.3 print the same data:
domain $[0,3]\times[0,1]$, step corner at $(0.6,0.2)$, Mach 3 inflow
with $\rho=1.4$, $p=1$, $\gamma=1.4$, final time $t=4$. The sound speed
of that state is $c=\sqrt{1.4\cdot1/1.4}=1$, so the inflow velocity is
$(v_1,v_2)=(3,0)$ *(compiler check, not in the sources)*.
Walls are reflecting, the left boundary is inflow and the right one
outflow. Balsara et al. treat the corner singularity "in the same manner
as Woodward and Colella"; Li et al. do not mention a corner
treatment. [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.4 refer the
setup to Woodward & Colella without reprinting it and run to $t=4$.
[Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.10 and
[Wang et al. (2021)](/sources/wang-2021.md) Example 5.8 print the
tunnel ($3\times1$, step of height 0.2 at $x=0.6$) and $t=4$, and both
plot 30 density contours from 0.32 to 6.15.

| Source | Scheme | Grid | CFL |
|---|---|---|---|
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.4 | [WENO-Z+M](/methods/weno-z-plus.md) vs WENO-Z, WENO-Z+, WENO-IS-I, WENO-Z7, WENO-Z9 | $481\times161$ | 0.5 |
| [Li et al. (2022)](/sources/li-2022-b.md) §4.4.3 | seventh-order [WENO-ZN](/methods/weno-zn.md) vs WENO-JS, WENO-Z | $600\times200$ | not restated for 2D |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §IX.g | seventh-order [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md), HLL-based (Fig. 17 caption) | $1440\times480$ | 0.4 |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.10 | sixth-order moment-based [multi-resolution HWENO](/methods/hermite-weno.md), HLLC: HWENO6 vs HWENO6-M5-I | $600\times200$ | 0.6 |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.8 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5, original WENO5-MR) vs WENO-JS5, WENO-AO5 | $1200\times400$ | 0.6 |

## What the benchmark measures

**Robustness of very-high-order WENO.** Luo & Wu report that both the
seventh- and the ninth-order WENO-Z schemes fail on this problem at CFL
0.5, while WENO-Z+M runs and resolves the shear layer "significantly
better" than WENO-IS-I (§5.3.4, Fig. 16). The same paper needs CFL 0.1 for
WENO-Z9 on the [double Mach reflection](/benchmarks/double-mach-reflection.md),
so the two problems together expose a stability margin that design
order alone does not show.

**Vortex-sheet roll-up.** Li et al. find that all schemes capture the
shocks and that WENO-ZN gives the clearest Kelvin–Helmholtz roll-up of
the vortex sheet (§4.4.3, Fig. 9). Balsara et al. show "pronounced"
vortex-sheet roll-up at seventh order on $1440\times480$ (Fig. 17).
Luo & Wu plot 60 density contours from 0.2568 to 6.607. Wang et al.
(2021) find the multi-resolution schemes resolving the roll-up better
than WENO-JS5 (Fig. 5.14).

**Hermite WENO and its first moments.** Li, Shu & Qiu recall that the
original Hermite WENO schemes are "not stable enough" for the forward
step, because first-derivative values grow large near discontinuities
(§1). Their sixth-order scheme runs both without and with the
modification of the first moments in troubled cells; the modified one
gives "much better resolutions and sharper shock transitions", and the
troubled cells flagged by their modified KXRCF indicator are plotted
(Fig. 3.8, comment p. 31). See
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

## Qualifications

- Evidence is visual (contour plots); no source reports an error norm
  or a reference solution.
- The grids differ by a factor of three in each direction
  ($481\times161$ to $1440\times480$) and the time steppers and fluxes
  differ, so the roll-up seen in the five papers is not comparable
  across them.
- Li et al. write that the problem "is also originally from the paper
  of [30]", with no preceding mention of that paper.

# Citations

- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.4, Fig. 16.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.4.3, Fig. 9.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.g, Fig. 17.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §1; Ex. 3.10, Fig. 3.8; comment p. 31 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.8, Fig. 5.14.
