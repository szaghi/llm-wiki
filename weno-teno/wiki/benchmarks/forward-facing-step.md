---
type: Benchmark
title: "Mach 3 forward-facing step"
description: "Two-dimensional Euler benchmark of Mach 3 flow in a wind tunnel with a step, run to t=4; it tests robustness at the expansion corner and the resolution of the Kelvin–Helmholtz roll-up of the vortex sheet from the triple point."
status: established
aliases: [forward-facing step, wind tunnel with a step, Mach 3 wind tunnel]
tags: [benchmark, low-dissipation, weno]
timestamp: 2026-10-22T20:00:00Z
---

# Mach 3 forward-facing step

A uniform Mach 3 flow of ideal gas enters a wind tunnel of unit height
containing a step of height $0.2$ whose corner sits at $(0.6,0.2)$. A bow
shock forms ahead of the step, reflects from the upper wall and the step
top, and a triple point forms on the upper wall from which a vortex
sheet trails downstream. The expansion corner of the step is a
singularity that strains robustness, and the vortex sheet is
Kelvin–Helmholtz unstable, so the benchmark measures both whether a
scheme survives and how much small-scale structure it resolves. Eight
sources of the bundle run it, two of them on unstructured triangles and
one in a relativistic version; those that name an origin attribute it
to Woodward & Colella.

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
plot 30 density contours from 0.32 to 6.15, as do
[Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.5, who describe a
right-moving Mach 3 initial flow in the same tunnel with reflecting
walls and inflow/outflow boundaries and no corner treatment beyond
local mesh refinement. [Yu & Hesthaven (2022)](/sources/yu-2022.md)
§5.4.5 run the Mach 3 step to $t=3$ on fully unstructured triangles,
without special treatment of the corner, and compare with Chaudhuri et
al.

**Relativistic version.** [Chen & Wu (2022)](/sources/chen-2022-b.md)
Ex. 4.9 (arXiv v1) run the same tunnel and step for the
[relativistic](/definitions/relativistic-hydrodynamics.md) Euler
equations with $\gamma=1.4$ and $\rho=1.4$ at a "Newtonian" Mach number
3, with inflow speeds $v_1=0.9$, $0.99$ and $0.999$ to $t=6$, $4.45$ and
$4$, on 149,436 triangles ($h=1/160$), reflecting walls and no entropy
fix at the corner.

| Source | Scheme | Grid | CFL |
|---|---|---|---|
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.4 | [WENO-Z+M](/methods/weno-z-plus.md) vs WENO-Z, WENO-Z+, WENO-IS-I, WENO-Z7, WENO-Z9 | $481\times161$ | 0.5 |
| [Li et al. (2022)](/sources/li-2022-b.md) §4.4.3 | seventh-order [WENO-ZN](/methods/weno-zn.md) vs WENO-JS, WENO-Z | $600\times200$ | not restated for 2D |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §IX.g | seventh-order [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md), HLL-based (Fig. 17 caption) | $1440\times480$ | 0.4 |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.10 | sixth-order moment-based [multi-resolution HWENO](/methods/hermite-weno.md), HLLC: HWENO6 vs HWENO6-M5-I | $600\times200$ | 0.6 |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.8 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5, original WENO5-MR) vs WENO-JS5, WENO-AO5 | $1200\times400$ | 0.6 |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.5 | RKDG $P^1$, $P^2$ with the improved vs the original [simple WENO limiter](/methods/weno-limiter-dg.md), KXRCF $C_k=0.01$ | triangles, $h=1/400$ near the corner, $1/100$ elsewhere | 0.3 ($P^1$), 0.18 ($P^2$) |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.4.5 | nodal DG, ANN-predicted [artificial viscosity](/methods/artificial-viscosity.md) with decay-rate threshold $\mathfrak a_0=2.5$ (page-local) and their min-rule (4.8) | unstructured triangles, $h=1/80$ | — |
| [Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.9 | third-order FV WENO on triangles, physical-constraint-preserving limiter, HLL (relativistic) | triangles, $h=1/160$ | 0.5 |

## What the benchmark measures

**Robustness of very-high-order WENO.** Luo & Wu report that both the
seventh- and the ninth-order WENO-Z schemes fail on this problem at CFL
0.5, while WENO-Z+M runs and resolves the shear layer "significantly
better" than WENO-IS-I (§5.3.4, Fig. 16). The same paper needs CFL 0.1 for
WENO-Z9 on the [double Mach reflection](/benchmarks/double-mach-reflection.md),
so the two problems together expose a stability margin that design
order alone does not show.

**The corner without a fix.** Three sources describe no
Woodward–Colella corner treatment: Yu & Hesthaven and Chen & Wu say
so, Du et al. mention only local mesh refinement. Du et al. see a spurious Mach stem at
the bottom wall, caused by the corner, in the $P^2$ result with the
original limiter, which "decreases when using the improved limiter";
the improved limiter saves 9.35 % ($P^1$) and 33.96 % ($P^2$) of the
CPU time (Ex. 4.5, Fig. 4.9, Table 4.9). Yu & Hesthaven stabilize the
shocks without special treatment of the corner; an entropy layer along
the step wall, triggered by the corner (where their Lobatto edge nodes
put a zero velocity), decreases with the polynomial degree, and the
results agree with Chaudhuri et al. The run needs the tuned setting
$\mathfrak a_0=2.5$ (the threshold of the modal decay rate
in their viscosity switch, page-local; default 2) with the min-rule
(§5.4.5, Figs. 21–23). In Chen & Wu's
relativistic runs the physical-constraint-preserving limiter is needed
to keep the scheme running at every inflow speed (Ex. 4.9, Fig. 13).

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
- The Cartesian grids differ by a factor of three in each direction
  ($481\times161$ to $1440\times480$), the triangular meshes are
  locally refined or unstructured, and the time steppers and fluxes
  differ, so the roll-up seen in the papers is not comparable across
  them.
- Yu & Hesthaven stop at $t=3$, the other non-relativistic runs at
  $t=4$.
- Li et al. write that the problem "is also originally from the paper
  of [30]", with no preceding mention of that paper.

# Citations

- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.4, Fig. 16.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.4.3, Fig. 9.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.g, Fig. 17.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §1; Ex. 3.10, Fig. 3.8; comment p. 31 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.8, Fig. 5.14.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — Ex. 4.5, Figs. 4.8–4.9, Table 4.9.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.4.5, Figs. 21–23.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.9, Fig. 13 (arXiv v1).
