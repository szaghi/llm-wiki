---
type: Benchmark
title: "Noh implosion problem"
description: "Cold gas at unit speed converging on a point, line or plane forms an infinite-strength shock moving out at speed 1/3 with an exact solution; run in one to three dimensions by shock-capturing, shock-tracking, ALE and adaptive-moving-mesh schemes to test wall heating at the centre, symmetry and positivity."
status: established
aliases: [Noh problem, Noh implosion, Noh shock implosion, 2D Noh, 3D Noh]
tags: [benchmark, positivity, bound-preserving, shock-tracking]
timestamp: 2026-10-23T03:53:00Z
---

# Noh implosion problem

In the Noh problem an ideal gas with $\gamma=5/3$, unit density and
(almost) zero pressure moves towards the origin with unit speed, in
planar, cylindrical or spherical geometry. The gas stagnates at the
centre and an infinitely strong shock runs outwards at speed $1/3$,
leaving behind it a gas at rest of uniform density and pressure. The
exact solution makes the error measurable. The test is known for
**wall heating**: schemes over-heat the gas next to the centre (or the
reflecting wall), so that the density there falls below the exact
plateau while the internal energy rises above it. The sources use the
test for that defect, for the symmetry of the shock, and, because the
pre-shock pressure is near zero, as a positivity test.

## Exact solution

For $\gamma=5/3$ and the shock at $r=t/3$, Fu (2021) prints the 3D
density, $64$ behind the shock and $(1+t/r)^2$ ahead of it, and Ramani
& Shkoller the shock speed $1/3$. In $d$ dimensions the post-shock
density is $\big((\gamma+1)/(\gamma-1)\big)^d$, i.e. 4, 16 and 64 for
$d=1,2,3$, and the pre-shock density is $(1+t/r)^{d-1}$
*(compiler check, not in the sources)*; the post-shock gas is at rest
with specific internal energy $\tfrac12$, the kinetic energy of the
inflow.

## Setups

| Source | Dimension, domain | Initial data | Boundaries | Grid, final time |
|---|---|---|---|---|
| [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) §IV.D | 1D, $(-0.5,0.5)$ in space, $(0,1)$ in time | $(\rho,v,p)=(1,1,10^{-6})$ left, $(1,-1,10^{-6})$ right | — | 4 space–time quadrilaterals, $t=1$ |
| [Fu (2021)](/sources/fu-2021.md) §5.8 | 3D, $[0,0.256]^3$ | $\rho=1$, $v=-x/r$, $p=10^{-6}$ ("to avoid complex eigenvalues") | symmetry on $x_i=0$, supersonic inflow with the analytic density elsewhere | $64^3$, $t=0.6$ |
| [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) §3.5.3 | 2D, $[0,1]^2$ | $\rho=1$, specific internal energy $10^{-14}$, unit velocity towards the origin | reflective left and bottom, free right and top | $35\times35$ moving cells, $t=0.6$ |
| [Ramani & Shkoller (2023)](/sources/ramani-2023.md) §7.1, Eq. (56) | 2D, $[0,1]^2$ | $\rho=1$, $\rho v=(-\cos\theta,-\sin\theta)$ for $r>0$, $0$ at $r=0$, $E=0.5+10^{-6}/(\gamma-1)$ | reflecting left and bottom, exact solution on top and right | $50^2$, $100^2$, $200^2$ uniform; $50^2$ adaptive; $T=2$ |

All four use $\gamma=5/3$. Ramani & Shkoller's total energy is the
kinetic energy $\tfrac12$ plus a pressure of $10^{-6}$, the pressure of
Fu and Luo et al.; Gu et al.'s internal energy $10^{-14}$ gives a
pressure $\tfrac23\times10^{-14}$ *(compiler check, not in the
sources)*. In the 2D runs at $T=2$ the shock reaches $r=2/3$, inside
the unit quarter-square *(compiler check, not in the sources)*.

## Runs and findings

**Very-high-order TENO with a positivity limiter.** Fu (2021) runs
TENO8-AA and TENO10-AA ([adaptive TENO](/methods/adaptive-teno.md))
with Rusanov splitting and the
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
that all the paper's extreme cases use. The spherical shock keeps its
shape and shows no wall heating, compared with a $128^3$ result of an
earlier work; the density overshoot at the origin is smaller than with
WENO-CU6-M1 at the same resolution, and TENO10-AA gives a more accurate
post-shock density than TENO8-AA (Fig. 15).

**Shock tracking without overheating.** Luo et al.'s
[MDG+ICE implicit shock tracking](/methods/implicit-shock-tracking.md)
with $\mathbb P^1$ elements fits the two shocks as element faces in
space–time. During the nonlinear iterations one element collapses and
is removed, and density and pressure turn negative without affecting
the result; the PDE and geometry residuals reach about
$10^{-8}$–$10^{-9}$ in about 50 iterations, and the final solution is
"virtually identical to the exact solution" with no overheating
(Figs. 22–24). They state, citing Liou, that Eulerian, Lagrangian and
ALE methods all produce the overheating; the claim is not tested in the
paper. The same authors treat the
[double rarefaction](/benchmarks/double-rarefaction-problem.md) the same
way.

**Lagrangian failure and ALE with positivity-preserving remapping.**
Gu et al. compare the third-order positivity-preserving ENO Lagrangian
scheme of Cheng & Shu with an indirect ALE method that rezones and
remaps every 20 steps with their positivity-preserving multi-resolution
WENO [conservative remapping](/methods/conservative-remapping.md). The
pure Lagrangian run fails after $t=0.54$; the ALE run reaches $t=0.6$
(grid, density and internal energy in Fig. 17, density against radius
in Fig. 18). The positivity limiter of the remap is needed: without it
negative internal energy and pressure stop the code, which they state
and mark through the limited cells of Fig. 17 rather than by a run
without the limiter. They note that other Lagrangian schemes "may
produce better or more robust results" on this test.

**Adaptive moving mesh against uniform meshes.** Ramani & Shkoller run
a simplified finite-difference WENO ALE scheme with smooth C-method
[artificial viscosity](/methods/artificial-viscosity.md), on uniform
grids at CFL about 0.2 and on a $50\times50$ dynamic
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) (SAM-ALE)
whose target, built from the exact solution, concentrates cells at the
shock. On uniform grids the solution is non-oscillatory and radially
symmetric, and the artificial viscosity "almost entirely removes" the
wall heating at the higher resolutions (Fig. 13). The adaptive run has
a very small wall-heating error, the smallest of all runs, preserved
symmetry, and a shock as sharp as on the $200^2$ uniform grid
(Fig. 14). Table 6:

| Run | $L^2$ density error | CPU time (s) | Memory (MB) |
|---|---|---|---|
| $50^2$ uniform | $1.019$ | 4.3 | 7.5 |
| $100^2$ uniform | $6.917\times10^{-1}$ | 35.3 | 14.6 |
| $200^2$ uniform | $5.406\times10^{-1}$ | 289 | 43.7 |
| $50^2$ adaptive | $4.897\times10^{-1}$ | 45.6 | 7.8 |

The adaptive run is more accurate than the finest uniform one, about 6
times faster and with 18 % of its memory ($289/45.6=6.3$,
$7.8/43.7=0.18$; *compiler check, not in the sources*). They attribute
the symmetry to the artificial viscosity together with the alignment of
the grid with the shock, and recall from the literature that dyadic
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
produces Noh anomalies, from spurious wave reflection at refinement
jumps, that persist or worsen under refinement (§7.1). See
[symmetry preservation](/properties/symmetry-preservation.md).

## Qualifications

- Evidence is visual for three sources (density profiles and scatter
  plots against the exact solution); only Ramani & Shkoller print an
  error norm.
- Fu prints the 3D initial condition as $(\rho,u,v,p)=(1,-x/r,-y/r,10^{-6})$,
  without the third velocity component $-z/r$ that the 3D test needs.
- Ramani & Shkoller print the mesh target as
  $C_\psi=\exp[-400(r^2-t^2/9)]$, without a square or absolute value of
  the bracket; as printed it grows without bound inside the shock
  radius and peaks at the origin, not at the shock $r=t/3$ it is
  "designed ... to track", while their analogous targets elsewhere in
  the paper square the bracket *(compiler check, not in the sources)*.
  They are read as arXiv v2.
- Luo et al.'s run uses four space–time elements; their statement on
  other methods is a literature claim, and no capturing scheme is run
  for comparison.
- The four setups differ in dimension, so post-shock densities (4, 16,
  64) and wall-heating levels are not comparable across them.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.8, Fig. 15 (arXiv v1).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §IV.D, Figs. 22–24 (author manuscript).
- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §3.5, §3.5.3, Figs. 17–18.
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) — §1.1, §7.1, Eqs. (56)–(57), Table 6, Figs. 13–14 (arXiv v2).
