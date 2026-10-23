---
type: Software
title: "ADAM"
description: "ADAM is a Fortran 2003 object-oriented library for block-based octree adaptive mesh refinement with immersed boundaries on GPU clusters (CUDA Fortran, CUDA-aware MPI), with NASTO, its compressible Navier–Stokes application using conservative finite-difference WENO with Lax–Friedrichs splitting; it is measured on 3D shock diffraction by a sphere on up to 256 V100 GPUs."
status: established
aliases: [ADAM AMR library, NASTO]
tags: [software, gpu, finite-difference, weno, immersed-boundary, amr]
timestamp: 2026-10-22T19:46:00Z
---

# ADAM

ADAM is a library for block-based octree
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) (AMR)
coupled with an [immersed boundary](/methods/immersed-boundary-method.md)
method, written in object-oriented Fortran 2003 for GPU-accelerated
supercomputers; NASTO is the compressible Navier–Stokes application
built on it. The bundle's account is
[Zaghi, Salvadore, Di Mascio & Rossi (2023)](/sources/zaghi-2023.md),
which describes the software design, the GPU data layout and the AMR
algorithm, and measures them on the three-dimensional diffraction of a
strong shock by a sphere on the Marconi100 cluster (CINECA, NVIDIA V100).

## Software design

The code is divided by its dependence on the equations and on the
computing back-end, so that $N_{\mathrm{equations}}\times N_{\mathrm{backends}}$
replicated versions are avoided (§2.1, Fig. 1):

1. independent of both: the AMR grid, the tree, input/output;
2. dependent on the equations only: field and method initialization;
3. dependent on the back-end only: ghost-cell updates and MPI buffers;
4. dependent on both: convective and viscous fluxes.

The components are derived types with type-bound procedures (`grid`,
`tree`, `field`, `adam`, a back-end field `base_<backend>`, and the
equation-specific objects). The only back-end implemented is CUDA
Fortran, mostly through `!$cuf` kernels with some explicit kernels, and
CUDA-aware MPI (§2.2).

## Grid and data layout

- **Blocks.** The domain is a single parallelepiped root block; refinement
  splits a block into eight identical children and eight siblings rejoin
  their parent, so the blocks form an octree indexed by level and block
  coordinates. Every block has the same $N_{xyz}^3$ (page-local)
  equispaced, cell-centred cells and full three-dimensional ghost layers,
  26 ghost regions (6 faces, 12 edges, 8 corners) (§2.2).
- **Hash map.** The octree is stored in a hash map with O(1) insertion
  and deletion, keyed by a 64-bit integer that linearizes (level, block
  coordinates) (§2.2, Fig. 2).
- **Field arrays.** The CPU field is a five-index array (three space
  indices, variable, block); the GPU copy is transposed so that the
  block index is contiguous, for coalesced access by contiguous CUDA
  threads, and is allocated once to fill the GPU memory (§2.2).
- **Residency.** The whole computation runs on the GPU; CPU–GPU copies,
  with transposition, occur only at input/output and at AMR updates.
  Output is HDF5, one file per process, indexed by XDMF (§2.2).

## AMR update

Three phases (§2.2, Fig. 3):

1. **Marking.** A back-end routine marks each block for splitting,
   recomposition or neither from a criterion (the density-gradient
   modulus in the shock test, the enthalpy gradient in the vortex test);
   the CPU then sanitizes the marks: eight siblings recompose only if
   all exist and are all marked, neighbouring blocks differ by at most
   one level (2:1 balance), and levels are capped.
2. **Refinement and coarsening.** The hash map and the maps are
   updated, the field is copied to the CPU and refined or coarsened by
   interpolation there.
3. **Load balancing.** Blocks are reassigned to processes along a Morton
   space-filling curve, the field is redistributed and copied back, and
   the ghost maps are regenerated.

Splitting and recomposition use hysteresis, a split threshold above the
recomposition one, against flip-flop. Ghost cells between blocks of
different levels are filled by second-order interpolation. The octree
is held by every process and its operations are essentially serial, a
limitation the authors acknowledge (§2.2, §3.2, §4).

## NASTO: the compressible solver

- **Equations.** Compressible Navier–Stokes for a perfect gas,
  nondimensionalized by Reynolds and Prandtl numbers (§3.1, Eqs. 1–4).
- **Space.** A [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md),
  $\partial_xf\approx(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$ (Eq. 5),
  with [WENO](/methods/weno-js-reconstruction.md) reconstruction of the
  fluxes and [Lax–Friedrichs (Rusanov) flux-vector splitting](/methods/lax-friedrichs-flux.md)
  for upwinding (§3.1). No stencil, weight, regularization, splitting
  speed or characteristic projection is printed, and the WENO order of
  the shock runs is not stated; the appendix vortex uses WENO3.
- **Time.** The three-stage third-order [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)
  method, with a global time step from the local convective condition
  (Eqs. 6–9); the CFL number used is not reported.
- **Immersed boundary** (after Di Mascio & Zaghi 2021). A signed distance
  $\phi$ (page-local), positive inside the body, defines the wall
  $\phi=0$ and the normal $n=\nabla\phi/\lvert\nabla\phi\rvert$. The
  solution $q$ (page-local) is extended into the body by marching
  $\partial_\tau q+n\cdot\nabla q=0$ in a pseudo-time $\tau$ (page-local)
  toward steady state, one propagation step at CFL close to 1 per
  Runge–Kutta stage being enough; fluxes in cells cut by $\phi=0$ then
  carry the wall condition (§3.1.1, Eq. 10). $\phi$ is recomputed after
  each AMR update, and the extrapolation steps interleave with the ghost
  updates in a fixed order within each stage (§3.1.1). The signed
  distance is likened to the [level sets](/methods/level-set-method.md)
  of Sethian and Smereka.

## Performance

The test is the [diffraction of a plane shock by a sphere](/benchmarks/shock-diffraction.md)
in a cube of side 20, after the Bryson & Gross (1961) experiment;
timings are taken at $t=5$, when the number of blocks is largest. The
grind time is $T_g=T\,N_{\mathrm{GPU}}/N_{\mathrm{cells}}$, with $T$ the
time of one iteration without AMR update (page-local symbols) (§3.2,
Table 1).

**Strong scaling** (3.6 M cells, 7008 blocks of $8^3$; Table 1, runs 1–6,
Fig. 5):

| GPUs | 1 | 2 | 4 | 8 | 16 | 32 |
|---|---|---|---|---|---|---|
| $T$ [s] | 1.019 | 0.477 | 0.221 | 0.114 | 0.0716 | 0.0541 |
| AMR update [s] | 4.25 | 3.11 | 2.36 | 2.1 | 1.91 | 1.84 |

The speed-up is close to ideal, even superlinear, up to 8 GPUs, about
90 % efficient at 16 GPUs (about 225 K cells per GPU) and below 60 % at
32; the authors conclude that a V100 needs more than about 250 K cells.
The AMR update scales poorly.

**Block size.** Grind time falls from 0.28 ($8^3$, 1 GPU) to 0.16
($16^3$, 8 GPUs) and rises to 0.21 ($32^3$, 64 GPUs, 279 M cells), where
the MPI ghost exchange between nodes becomes significant (runs 7–8,
Fig. 6).

**Resolution ratio.** With the coarsest required spacing fixed at 0.5
and the finest halved from 0.25 to 0.015625 (ratio 2 to 32, on 1 to 256
GPUs), the cell count grows by a factor of about 4–5 per halving instead
of 8, up to 684,258 blocks and 350.3 M cells on 256 GPUs; the grind time
grows from 0.20 to 0.49, less than a factor 3, but the serial AMR update
reaches 527.97 s, acceptable for statistically stationary runs and
problematic for transient ones. The largest run took 25.21 h (runs 9–13,
Fig. 7).

**Physics.** The authors compare the flow with a digitized Bryson &
Gross schlieren photograph: the main discrepancy is the curved reflected
shock, slightly ahead in the experiment, whose digitization carries a
large error (§3.3, Fig. 11). They claim the finest resolution published
for the fully three-dimensional strong-shock diffraction by a sphere.
An appendix [isentropic vortex](/benchmarks/isentropic-vortex.md) at
Mach 0.1 with WENO3 (about 2.4 M cells, five levels) shows smearing from
WENO3 dissipation, no visible pollution at level jumps, and strong
scaling to 16 GPUs comparable with the shock test (Appendix,
Figs. A.17–A.18).

## Qualifications

- The text states a Mach 2.89 incident shock, but the printed post-shock
  state ($\rho=5.1432014$, $p=9.04545$, $v_1=2.0451168$ ahead of
  $\rho=1.4$, $p=1$ at rest, $\gamma=1.4$) is the
  [Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md) state of
  a Mach 2.81 shock; Mach 2.89 gives $\rho=5.254$, $p=9.577$,
  $v_1=2.120$ *(compiler check, not in the sources)* (§3, Fig. 4).
- Table 1 labels $T_g$ in seconds, but with $N_{\mathrm{cells}}$ in
  millions the printed values are microseconds per cell and iteration
  per GPU ($1.019/3.6\times10^6=2.8\times10^{-7}$ s for run 1)
  *(compiler check, not in the sources)*.
- The "8 billions" cells a uniform grid would need at the finest spacing
  are $(20/0.015625)^3\approx2.1\times10^9$ *(compiler check, not in the
  sources)*, and the resolution ratio of runs 9–13 grows by a factor 16,
  not the 32 the text states (§3.2).
- The printed vortex of the appendix uses $Y-Y_v$ in both velocity
  components (Eqs. A.4–A.5), so as printed it is not a rotating vortex *(compiler check, not in the sources)*.
- Zaghi et al. contrast ADAM with general codes that lack GPU
  exploitation and with GPU-performant codes of "limited algorithmic
  flexibility" ([STREAmS](/software/streams.md), [PyFR](/software/pyfr.md),
  Nek5000) (§2.1); this is the authors' characterization.

# Citations

- [Zaghi, Salvadore, Di Mascio & Rossi (2023)](/sources/zaghi-2023.md) — §2.1, Fig. 1; §2.2, Figs. 2–3; §3, Fig. 4; §3.1, Eqs. (1)–(9); §3.1.1, Eq. (10); §3.2, Table 1, Figs. 5–7; §3.3, Figs. 9–15; §4; Appendix, Eqs. (A.1)–(A.6), Figs. A.16–A.18.
