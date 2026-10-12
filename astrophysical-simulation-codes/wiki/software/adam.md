---
type: Software
title: "ADAM (GPU block-octree AMR library) and NASTO"
description: "Fortran 2003 object-oriented library for block-based octree AMR on Cartesian grids whose compute phase runs entirely on NVIDIA GPUs through CUDA Fortran with CUDA-aware MPI, with the octree kept serially on the CPU in a hash map; its NASTO application solves the compressible Navier–Stokes equations with WENO finite differences, Lax–Friedrichs flux splitting, SSP RK3 and an immersed boundary."
status: established
aliases: [ADAM, NASTO, ADAM-NASTO]
tags: [software, hydro, amr, gpu, cuda, time-integration, performance, scaling]
timestamp: 2026-10-12T00:00:00Z
---

# ADAM and NASTO

ADAM is a library for block-based octree AMR on Cartesian grids, designed so
that the solver runs entirely on NVIDIA GPUs; NASTO is the compressible
Navier–Stokes application built on it
([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2, §3). The paper is a
CFD (not astrophysical) code paper; its contribution here is the GPU-resident
AMR design and its measured costs.

## Code

From [Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.
* Fortran, "following the Fortran 2003 object style": each component is a
  derived type with type-bound procedures (§2.2). No version number,
  repository URL or licence is printed; data "will be made available on
  request".
* **Modules by dependency class** (§2.1, Fig. 1): code independent of both
  the equations and the back end (AMR grid, I/O); equation-dependent only
  (field and method initialization); back-end-dependent only (ghost-region
  updates); dependent on both (convective and viscous fluxes). The aim is to
  avoid writing one variant per equation set and per back end. Components:
  `parameters`, `grid`, `tree`, `field`, `adam`, `base_<backend>`,
  `<equation>/equation_base`, `<equation>/equation_<backend>`,
  `<equation>/main_<backend>`.
* **Back ends**: only CUDA Fortran exists; kernels are mostly CUDA Fortran
  "cuf" kernels, with some explicit kernels; other back ends are "under
  development" (§2.2), OpenMP and OpenACC named as targets (§4).
* **I/O**: HDF5, one file per process, coordinated by an XDMF file (§2.2).

## Mesh and AMR

From [Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2; see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Blocks**: identical rectilinear Cartesian blocks of equispaced
  cell-centred cells, $N_{\mathrm b}$ per side; ghost layers cover all 26
  neighbour regions (6 faces, 12 edges, 8 corners). The initial mesh is one
  block covering the domain; a block splits into 8 children
  ($r_{\mathrm{ref}} = 2$) and 8 siblings can rejoin: "the classical
  octree".
* **Octree storage** (Fig. 2): a hash map with $O(1)$ insertion and deletion,
  keys being 64-bit integers that linearize the level and the three block
  coordinates. The octree "is shared among all processes" and its operations
  are "essentially serial", stated as a limitation.
* **Update in three steps** (Fig. 3b). (i) *Marking* by a back-end routine
  (for example a gradient criterion), then a CPU pass that allows
  recomposition only when all 8 siblings exist unsplit and are all marked,
  keeps the levels of contiguous blocks within one of each other (2:1), and
  caps the level. (ii) *Refinement and coarsening*: the hash map is updated,
  the GPU field is copied to the host, and the host field is refined or
  coarsened "by interpolation" (order and conservation not stated).
  (iii) *Load balancing* along Morton space-filling curves, redistribution
  locally and over MPI, copy back to the GPU, regeneration of the ghost
  maps.
* **Hysteresis**: refinement criteria should avoid "flip-flop", splitting
  above one threshold and recomposing below a smaller one.
* **Ghost update**: same-process blocks, other-process blocks, physical
  boundaries, with "second-order interpolations" across level jumps.
* **Time step**: one global $\Delta t$, the minimum over cells of local
  Courant conditions (§3.1, eqs. 8–9); no subcycling is described. The
  Courant number used is not printed.
* **Conservation across level jumps** (refluxing) is not discussed.

## GPU design

From [Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2; see
[porting compressible-flow codes to GPUs](/methods/gpu-porting.md).
* **Field layout**: the host field is a 5-index array (three spatial
  indices, variable, block); the device copy uses **transposed ordering with
  the block index contiguous** (first, in Fortran) "to maximize access data
  coalescing for contiguous CUDA threads". The device array is "generally"
  allocated once "so that it occupies the entire GPU memory", and the host
  array with the same size.
* **Residency**: the whole compute phase runs on the GPU; host–device copies,
  with transposition, occur only at I/O and AMR updates. This is the reverse
  of [GAMER](/software/gamer.md), which keeps data on the host and streams
  patch groups, while both keep AMR operations on the CPU.
* **Precomputed neighbour arrays**: block coordinates and ghost-exchange
  neighbour indices are prepared during the AMR update, so the compute phase
  never queries the hash map; "there is in fact no evidence that this is AMR
  code" in the compute core.
* **MPI**: inter-process ghost exchange with CUDA-aware MPI.

## NASTO solver

From [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1.
* **Equations**: non-dimensional compressible Navier–Stokes, Newtonian
  viscous stress with Stokes' hypothesis, Fourier conduction, perfect gas
  (eqs. 1–3).
* **Space**: conservative finite differences, the derivative of the flux
  being the difference of high-order numerical fluxes at
  $x_{i\pm1/2}$ divided by $h$ (eq. 5, after Jiang & Shu 1996), with WENO
  reconstruction and Lax–Friedrichs (Rusanov) flux-vector splitting; see
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
  The WENO order of the shock test is not stated; the vortex test uses
  WENO3.
* **Time**: method of lines with explicit three-stage, third-order SSP
  Runge–Kutta in Butcher form (eqs. 6–7); see
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **Immersed boundary** (§3.1.1): a signed distance to the body (positive
  inside); the solution is extrapolated into the body by marching a
  pseudo-time advection along the distance gradient (eq. 10), "a single
  propagation step with CFL close to 1 per Runge–Kutta sub-stage" being
  sufficient (citing Di Mascio & Zaghi 2021). Per time step: AMR update if
  needed and distance recomputation; per RK stage: ghost update,
  extrapolation steps each followed by a ghost update, boundary conditions
  where the distance vanishes, residuals, stage update.

## Performance

From [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2, Table 1, Figs. 5–7.
NVIDIA V100 GPUs of Marconi100 (CINECA). Not printed: floating-point
precision, compiler, GPUs per node, ranks per GPU. All baselines are the same
code on one V100; there is no CPU or cross-code comparison. Problem: 3D
Mach 2.89 shock diffraction by a sphere (below). Times are per iteration at
$t = 5$, excluding AMR; the grind time is the iteration time divided by
cells per GPU. Table 1 labels the grind time in seconds, but its values are
seconds per $10^6$ cells per GPU (run 1: 1.019/3.6 = 0.28); whether an
iteration is a full three-stage step is not stated. See
[cell-update throughput](/definitions/cell-updates-per-second.md) and
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).

* **Strong scaling** (runs 1–6, 3.6 M cells, 7008 blocks, $N_{\mathrm b} = 8$):
  1.019, 0.477, 0.221, 0.114, 0.0716, 0.0541 s per iteration on 1, 2, 4, 8,
  16, 32 GPUs. Near-ideal ("even superlinear") to 8 GPUs, "close to 90 %" at
  16 (about 225 K cells per GPU), "below 60 %" at 32. Conclusion: efficient
  "if each GPU has a mesh portion greater than 250 K cells".
* **AMR update cost**: falls only from 4.25 s (1 GPU) to 1.84 s (32 GPUs);
  across the resolution series it rises from 0.74 s (1562 blocks) to
  527.97 s (684,258 blocks), "dramatically high when the number of blocks
  increases", attributed to the serial octree update and redistribution.
* **Block size** (runs 1, 7, 8, roughly constant load per GPU): $N_{\mathrm b}
  = 16$ lowers the grind time from 0.28 to 0.16 against $N_{\mathrm b} = 8$,
  by speeding up the compute part (at equal GPU count, runs 4 and 7 on 8
  GPUs, 0.25 against 0.16; run 1 is on 1 GPU); $N_{\mathrm b} = 32$ on 64 GPUs keeps the
  compute time but inter-node ghost time grows (grind time 0.21) (Fig. 6).
* **AMR against uniform** (runs 9–13, 1 to 256 GPUs): halving the finest
  target cell size multiplies the cell count by "between 4 and 5" instead
  of 8; the finest run has 350.3 M cells "instead of the 8 billions it would
  have with uniform refinement" (a cell-count ratio, not a measured time).
  The grind time grows from 0.20 to 0.49 while the coarse-to-fine ratio
  grows 32×.

## Verification

From [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.3 and the Appendix;
validation is qualitative only, with no error norm or convergence study.
* **Shock diffraction by a sphere** (§3, Fig. 4, §3.3, Figs. 8–15). Cube of
  20 non-dimensional units, sphere (immersed boundary) at the centre, plane
  Mach 2.89 shock; refinement on the density-gradient modulus with target
  coarse and fine cell sizes. Grid #4 (finest target cell 0.03125) at
  $t = 4$ is compared with a digitized schlieren plate of Bryson & Gross
  (1961): "very good agreement", the main discrepancy being the reflected
  curved shock, "slightly anticipated" in the experiment; "only qualitative
  conclusions can be taken". The authors claim "the finest resolution shown
  in literature" for this 3D problem (§3.3, §4).
* **Moving isentropic vortex** (Appendix, Figs. A.16–A.18, after Poinsot &
  Lele 1992). Periodic cube, levels 2 to 5, about 2.4 M cells, WENO3: the
  vortex is "well tracked, although some smearing is visible", attributed to
  WENO3; "AMR grid refinements jumps seem to not pollute the solution"
  (visual). Strong scaling to 16 GPUs including AMR time is called
  "comparable" with §3.2, although the plotted speed-ups (about 4.5, 6.4,
  7.6 at 4, 8, 16 GPUs, read from the figure) are well below §3.2's.

# Citations

1. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §§2–4, eqs. 1–10,
   Table 1, Figs. 1–15, Appendix (version of record).
