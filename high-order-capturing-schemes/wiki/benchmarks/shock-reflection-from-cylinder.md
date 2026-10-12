---
type: Benchmark
title: "Shock reflection from a cylinder"
description: "A planar shock (Mach 2 to 2.8) hits a circular cylinder on a Cartesian grid that does not fit it, producing a reflected bow shock, Mach stems, triple points and slip lines; compared with the Bryson–Gross schlieren photographs, it tests cut-cell small-cell stabilization, AMR interfaces crossing the body, and moving embedded boundaries."
status: established
aliases: [shock diffraction by a cylinder, Bryson–Gross cylinder, shock–cylinder interaction]
tags: [benchmark, euler, embedded-boundary, mach-reflection]
timestamp: 2026-10-12T00:00:00Z
---

# Shock reflection from a cylinder

**Set-up.** A planar shock moving into gas at rest strikes a circular
cylinder. The incident shock reflects into a detached bow shock, Mach
stems form on the cylinder with triple points and slip lines, and the
diffracted shocks meet behind the body. The reference is the schlieren
series of Bryson and Gross (1961). The body is not grid-fitted. It is
distinct from the steady [supersonic cylinder flow](/benchmarks/supersonic-cylinder-flow.md)
and from the free body of [shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md).

**Variants.**
* *Mach 2, stationary cylinder.* Radius 0.15 centred at $(0.5, 0.5)$ in
  $[0, 1.00001]\times[0, 1]$, shock at $x = 0.2$, $302\times302$ cells, run
  to $t = 0.25$. Of 416 cut cells, 160 are below half a cell and the
  smallest volume fraction is $1.17\times10^{-4}$. Second-order MUSCL
  (CFL 0.85) and method of lines (CFL 1), both with a local Lax–Friedrichs
  flux and [state redistribution](/methods/state-redistribution.md), run
  robustly; MUSCL is better in the subsonic region ahead of the body, the
  method of lines smoother along the wall, and both place the wall shocks
  alike ([Berger & Giuliani (2021)](/sources/berger-2021.md), §5.2,
  Figs. 10–11).
* *Mach 2.81, AMR crossing the body.* $[0, 1]^2$, cylinder centred at
  $(0.5, 0.5)$ (radius not printed), shock at $x = 0.2$, upstream density
  1, outflow in $x$ and walls in $y$, base grid $256^2$ with two levels.
  Refining only the upper half of the cylinder, so that coarse–fine
  boundaries cross cut cells, gives the same solution in the refined
  region as refining all of it, with re-redistribution; the reflected
  shock, primary Mach stem, contact and triple point match Bryson and
  Gross at $t = 0.068$ and $0.088$ ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md),
  §4.3, Figs. 5–7). The upstream pressure is printed ambiguously.
* *Moving cylinder.* A cylinder of diameter 0.04 m moves at the
  pre-shock flow speed into a stationary shock of Mach 1.34 or 2.82, with
  [moving cut cells](/methods/cut-cell-finite-volume.md) and four AMR
  levels (114 points per diameter); before the shock arrives no waves
  appear, and the Mach 2.82 run reproduces the Bryson–Gross features
  qualitatively ([Natarajan et al. (2022)](/sources/natarajan-2022.md),
  §3.3, Fig. 6). Its printed post-shock density does not match its stated
  density ratio.

All comparisons are qualitative; no error norms are reported.

# Citations

1. [Berger & Giuliani (2021)](/sources/berger-2021.md), §5.2 (arXiv v1).
2. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4.3 (arXiv v1).
3. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.3 (arXiv v1).
