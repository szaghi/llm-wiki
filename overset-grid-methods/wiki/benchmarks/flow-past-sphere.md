---
type: Benchmark
title: "Flow past a sphere"
description: "The sphere as the three-dimensional overset test body: Henshaw's fourth-order incompressible flow in a channel on two pole-free sphere patches plus a Cartesian grid (1994), fourth-order Maxwell convergence and Mie scattering on a sphere grid (2006), and Horne and Mahesh's GPU unstructured solver at Re 3700 and a freely falling sphere (2021)."
status: established
aliases: [sphere in a channel, flow over a sphere, sphere at Re 3700, freely falling sphere]
tags: [benchmark, incompressible, high-order, gpu, unstructured, moving-grid]
timestamp: 2026-11-02T14:54:00Z
---

# Flow past a sphere

A sphere cannot be covered by one smooth logically rectangular grid without
coordinate singularities at the poles; an overlapping grid covers it with
two or more patches, each free of singularities, plus a background grid
([Henshaw 1994](/sources/henshaw-1994.md), §1.2). It plays in three
dimensions the role of the
[circular cylinder](/benchmarks/flow-past-circular-cylinder.md): a smooth
body and one hole in the background grid. The flow sources use it to
demonstrate solvers and to time them, and none of them reports a
convergence rate measured on the sphere; the only rates on a sphere grid
are those of the Maxwell tests of Henshaw (2006) (below).

## Cases

**Sphere in a channel, fourth-order incompressible flow (Henshaw 1994,
§5.2, Fig. 6, Table VIII).** [Henshaw (1994)](/sources/henshaw-1994.md),
with the CGINS solver on [CMPGRD](/software/cmpgrd.md) grids:
- *Geometry and flow.* Sphere of radius 1 at the origin in the channel
  $[-2.2,2.2]^3$; $\nu=0.05$; inflow $\mathbf u=(1,0,0)$, slip side walls,
  an outflow condition mixing $p$ and $\partial_np$, no-slip sphere.
- *Grids.* Three component grids, $(35^3)\cup(25^2\times9)\cup(25^2\times9)$:
  a Cartesian background and two sphere patches; fourth-order
  discretization with width-$q=5$ (triquartic) interpolation and two
  receptor lines; 10,728 interpolation points. The timing table labels the
  sphere's interpolation "implicit" (the cylinder's "explicit") without
  defining the terms there (see
  [explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)).
- *Cost.* 45.0 s per step on an IBM RS/6000-530: GMRES pressure solve 42%,
  implicit interpolation 17%, Adams predictor–corrector 28%, boundary
  conditions 9%. Henshaw attributes the interpolation share to the high
  fraction of receptors.
- Only contours at $t=2$ are shown; no drag or wake data. The solver is on
  [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

**Sphere at $Re=3700$, GPU unstructured overset solver (Horne & Mahesh 2021,
§4.2.2, Figs. 15–18, Table).** [Horne & Mahesh (2021)](/sources/horne-2021.md):
- *Setup.* Domain as in the DNS of Rodriguez et al. (2011); a hexahedral
  unstructured overset mesh around the sphere over an unstructured
  background mesh, assembled by their GPU bounding-volume-hierarchy method
  (see [parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md));
  collocated kinetic-energy-preserving finite volume, Crank–Nicolson, with
  receptor values injected into the linear systems. Accuracy run:
  $12\times10^6$ control volumes, spacing $0.015D$, near-wake spacing
  $0.014D$, patch-edge resolution matched to the background,
  $\Delta t=5\times10^{-4}$ (in units of $D/U_\infty$), statistics over
  $t\in[175,300]$.
- *Results against references:*

  | Quantity | Horne & Mahesh | Rodriguez et al. (DNS) | Experiment, as cited |
  |---|---|---|---|
  | drag coefficient $C_d$ | 0.392 | 0.394 | 0.39 (Schlichting & Gersten) |
  | recirculation length $L_w$ | $2.2D$ | $2.2D$ | — |
  | Strouhal number $St$ | 0.22 | 0.215 | 0.225 (Kim & Durbin) |

  A 1–5% match on every quantity, as the authors summarize; the surface
  pressure coefficient is compared with Kim & Durbin (1988) and the wake
  spectrum at a probe ($x=5D$, $y=1.5D$) shows roughly a $-5/3$ slope. No
  vortex distortion is seen at the overset boundary.
- *Speed-up.* On one node (4 NVIDIA V100 GPUs and a 24-core Xeon Gold 6126),
  100 steps at loadings from 150,000 to about 23 million cells, the new code
  runs 8 to 56 times faster than the authors' earlier CPU method, the gain
  growing with cell loading; the algorithmic changes alone give about a
  factor 2 on CPUs, and the production run would have taken about 35 times
  as long with the earlier method on the same nodes (Fig. 16). The
  comparison is not like-for-like by the authors' own account (different
  algorithms, a non-threaded CPU baseline).

**Freely falling sphere (Horne & Mahesh 2021, §4.2.3, Figs. 19–20).** A
sphere falling in quiescent fluid under six-degree-of-freedom rigid-body
motion, Galileo number $Ga=291$, density ratio $m^*=7.8$, domain
$10D\times10D\times50D$ (figure label), so the overset mesh and its
connectivity move every step. On 2 nodes with 2 V100 each, 100 steps at
65,000 to 500,000 cells per core run 12 to 20 times faster than the
earlier method, with better gains at low loadings than in the static case,
which the authors attribute to accelerated matrix assembly, overset
assembly and mesh motion. Timing only; no trajectory is validated in this
paper. See [moving overset grids](/methods/moving-overset-grid.md).

**Other physics.** [Henshaw (2006, §10.1–10.2)](/sources/henshaw-2006-b.md)
runs the fourth-order Maxwell scheme on a sphere of radius $1/2$ in the
box $[-2,2]^3$ ($41^3$ points) covered by two orthographic patches of
$33\times33\times13$ points: a manufactured solution gives max-norm rates
4.12, 4.26, 4.11 for $E_x$, $E_y$, $E_z$ and 3.47 for the divergence
(Table 2), and plane-wave scattering by a perfectly conducting sphere,
compared with the Mie series at $t=3$, gives 3.86, 3.86, 3.85 and 3.09
(Table 3). That case is on
[Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md).

## What the cases measure

| Source | Reynolds number | Grids | Measured | Reference data |
|---|---|---|---|---|
| Henshaw (1994) | based on radius 1, $\nu=0.05$ | 3 structured, two sphere patches | cost breakdown, contours | none |
| Horne & Mahesh (2021) | 3700 | 2 unstructured | $C_d$, $L_w$, $St$, $C_p$, spectrum; speed-up | DNS, experiment |
| Horne & Mahesh (2021) | $Ga=291$ | 2 unstructured, moving | speed-up | none |
| Henshaw (2006) | Maxwell, no flow | 3 structured, two orthographic patches | max-norm rates 3.1–4.3 | manufactured solution; Mie series |

## Qualifications

- Henshaw (1994) gives the sphere case "47,550 active grid points" in the
  text (§5.2) and "17,550" in Table VIII; the three grids hold
  $35^3+2\cdot25^2\cdot9=54{,}125$ points including unused and ghost points
  *(compiler check, not in the sources)*, which does not decide the slip.
- Horne & Mahesh print the near-wake spacing as "$D=0.014D$" (§4.2.2),
  with no spacing symbol on the left side. Their speed-up ranges differ across
  the paper: "upwards of 50 times" (abstract), 8–56× (§4.2.2), 12–20×
  (§4.2.3) and "15x to 50x" (§5); the last matches neither end of §4.2.2.
- Horne & Mahesh's Fig. 16 abscissa labels read 150000, 6480000, 12000000,
  2304000, a non-monotone sequence; the text gives "about 23 million" as
  the top loading.

# Citations

- [Henshaw (1994)](/sources/henshaw-1994.md) — §1.2 (sphere covered by overlapping patches without pole singularities); §4.1 (width-5 interpolation, two receptor lines); §5.2, Fig. 6, Table VIII (sphere in a channel, timings, receptor count).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §2 (GPU assembly); §3 (solver); §4.2.2, Figs. 15–18 and results table (sphere at $Re=3700$, speed-up); §4.2.3, Figs. 19–20 (freely falling sphere); §5 (speed-up summary).
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §10.1, Table 2 (manufactured Maxwell solution on the sphere-in-a-box grid); §10.2, Table 3 (PEC sphere scattering against the Mie series).
