---
type: Benchmark
title: "Supersonic vortex in a quarter annulus"
description: "Steady isentropic supersonic flow between two concentric circular walls, with an exact solution, computed on a Cartesian grid cut by both walls: the standard accuracy test of cut-cell schemes, which measures the error separately in the volume and on the boundary cells."
status: established
aliases: [supersonic vortex, Aftosmis supersonic vortex, quarter-annulus vortex]
tags: [benchmark, euler, embedded-boundary, accuracy, steady]
timestamp: 2026-10-12T00:00:00Z
---

# Supersonic vortex in a quarter annulus

**Set-up** (after Aftosmis et al., as used by the papers below). Steady,
isentropic, inviscid flow turning between two concentric arcs of radii
$\varrho_i = 1$ and $\varrho_o = 1.384$ in the first quadrant. The
velocity is tangential, with $\vert\mathbf v\vert \propto 1/\varrho$ and Mach
number 2.25 at the inner wall, density 1 there, $\gamma = 1.4$, and
$p = \rho^\gamma/\gamma$, so that
$\rho = \left(1 + \tfrac{\gamma-1}{2}\,2.25^2\left(1 - \varrho_i^2/\varrho^2\right)\right)^{1/(\gamma-1)}$.
The domain is $[0, 1.43]\times[0, 1.4301]$, with the exact solution in
the inflow and outflow ghost cells and reflecting curved walls cut through
the Cartesian grid. The run is marched to steady state. Errors are
measured in $L^1$ separately over the volume, $\sum_i\vert I_i\vert\,\vert e_i\vert$,
and over the cut cells, weighted by their wall-face areas
([Berger & Giuliani (2021)](/sources/berger-2021.md), §5.1, eq. 56;
[Giuliani et al. (2022)](/sources/giuliani-2022.md), §3.2, eq. 14).
It is distinct from the advected [isentropic vortex](/benchmarks/isentropic-vortex.md).

**Results.**
* Second-order method of lines with [state redistribution](/methods/state-redistribution.md),
  grids $27^2$ to $864^2$, no limiter: the volume error falls by factors
  3.8–5.6 per refinement (order about 2) and the boundary error at rates
  1.38–1.5. Local time stepping without redistribution gives essentially
  the same errors ($2.59$ against $2.68\times10^{-6}$ in the volume on
  $864^2$), so the boundary rate is set by the irregular cut
  cells, not by the stabilization. Treating cell averages as point values
  in the least-squares gradients halves the error on coarse grids
  ([Berger & Giuliani (2021)](/sources/berger-2021.md), Tables 1–2, Fig. 9).
* Weighted state redistribution: second order in the volume and about
  1.4 on the boundary; 2–3 times smaller errors than the original with
  centred merging ([Giuliani et al. (2022)](/sources/giuliani-2022.md),
  Fig. 6b).

# Citations

1. [Berger & Giuliani (2021)](/sources/berger-2021.md), §5.1 (arXiv v1).
2. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §3.2 (arXiv v2).
