---
type: Benchmark
title: "Schardin's problem (shock over a triangular wedge)"
description: "A weak planar shock (Mach about 1.3) passes an equilateral-triangle wedge on a grid that does not fit it: reflected shock, diffraction at the rear corners, Mach stems, triple points and shed vortices, compared with Chang & Chang's shadowgraphs; a qualitative test of immersed and embedded boundaries, also run with the wedge moving."
status: established
aliases: [Schardin problem, shock–wedge interaction, shock over a triangle]
tags: [benchmark, euler, immersed-boundary, embedded-boundary, mach-reflection]
timestamp: 2026-10-12T00:00:00Z
---

# Schardin's problem (shock over a triangular wedge)

**Set-up.** A planar shock of Mach about 1.3 runs over an equilateral
triangle pointing upstream. It reflects from the front faces, diffracts
around the rear corners into expansion fans and shed vortices, and forms
Mach stems, triple points and slip lines behind the body. The reference
is the shadowgraph series of Chang and Chang. Comparisons are
qualitative (feature positions and trajectories). It differs from the
backward-corner [shock diffraction](/benchmarks/shock-diffraction.md).

**Variants.**
* *Stationary wedge, ghost-cell immersed boundary.* Mach 1.3 into gas at
  rest at 0.05 MPa and 300 K, domain 200 mm × 150 mm on 1170 × 850
  nodes; the numerical schlieren at 147.78 µs matches the
  shadowgraph at 151.0 µs, and the triple-point and vortex-centre
  trajectories agree with the experiment and with Chaudhuri et al.
  ([Seshadri & De (2020)](/sources/seshadri-2020.md), §8.1.6,
  Figs. 19–21; [immersed-boundary methods](/methods/immersed-boundary-method.md)).
* *Moving wedge, cut cells.* A triangle of side 0.02 m moves at the
  pre-shock flow speed (459.54 m/s) into a stationary Mach 1.34 shock,
  domain 0.09 m × 0.09 m, $32^2$ base grid with four AMR levels; the
  reflected shock, expansion, vortices, decelerated shock, two Mach stems,
  two triple points and slip lines appear as in Chang and Chang
  ([Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.4, Figs. 7–8;
  [cut-cell finite volume](/methods/cut-cell-finite-volume.md)). A 3D
  analogue with a cone is run the same way (§3.7).

# Citations

1. [Seshadri & De (2020)](/sources/seshadri-2020.md), §8.1.6 (author manuscript).
2. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §§3.4, 3.7 (arXiv v1).
