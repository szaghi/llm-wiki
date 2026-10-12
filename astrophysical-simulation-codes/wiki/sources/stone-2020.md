---
type: Source
title: "Stone et al. (2020) — The Athena++ adaptive mesh refinement framework: Design and magnetohydrodynamic solvers"
description: "Method paper of Athena++, a C++ rewrite of Athena that abstracts the mesh from the physics: block-based tree AMR of fixed-size MeshBlocks with native face- and edge-centred data for constrained transport, a single global time step, task-list execution, method-of-lines VL2 and SSP Runge–Kutta integrators, curvilinear coordinates, and relativistic MHD, with 84–86% weak-scaling efficiency on 524,288 threads."
resource: "doi:10.3847/1538-4365/ab929b"
source_kind: paper
authors: [Stone J.M., Tomida K., White C.J., Felker K.G.]
year: 2020
venue: "Astrophys. J. Suppl. 249:4"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2020-ApJS-Stone-1038471538-4365ab929b.pdf"
tags: [software, mhd, amr, constrained-transport, time-integration, riemann-solver, performance, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Athena++ is a from-scratch C++ rewrite of Athena
([Stone et al. (2008)](/sources/stone-2008.md)) whose central design
decision is to separate the mesh from the physics (§1, §2). The mesh is a
block-based AMR of identical `MeshBlock`s in a binary tree, quadtree or
octree, carrying cell-, face- and edge-centred variables, so that
upwind CT is native to the AMR; each point is covered by exactly one
level and all levels share one time step (§2.1, §2.1.7). A bit-field
`TaskList` overlaps communication with computation and allows different
physics on different `MeshBlock`s (§2.5). The MHD module keeps Athena's
finite-volume discretization and Gardiner–Stone CT but replaces CTU with
method-of-lines integrators, adds curvilinear PLM/PPM, a general EOS,
explicit or super-time-stepped diffusion, and angular-momentum-conserving
geometric sources (§3). A special- and general-relativistic MHD module is
summarized (§4). Merged into [Athena++](/software/athena-plus-plus.md),
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) and
[constrained transport](/methods/constrained-transport.md).

# Key claims

1. **Mesh abstraction** (§1, §2). Mesh, AMR, boundary conditions and MPI
   decomposition are written "without specific references to any
   particular physics"; classes `Mesh`, `MeshBlock`, `Coordinates`,
   `TaskList`. Public repository
   https://github.com/PrincetonUniversity/athena-public-version, BSD-3
   licence, C++11 (§2.6).
2. **Block-based tree AMR** (§2.1, §2.1.2). All `MeshBlock`s have the same
   cell count; $r_{\mathrm{ref}} = 2$ in all directions at once; $N_{\mathrm b}$
   must be even, and $n_{\mathrm g}$ must be even with AMR; neighbours differ
   by at most one level. Z-ordering of the tree assigns blocks to
   processes.
3. **Ghost zones and buffers** (§2.1.1, §2.1.3). $n_{\mathrm g} = 2$ for
   second-order MHD on a uniform mesh; 3 (hydro) and 4 (MHD) for spatial
   orders up to four. One message buffer per neighbour: up to 8 (2D) / 26
   (3D) on uniform grids and 12 / 56 with AMR. Restricted copies sit in
   "coarse buffers".
4. **Single coverage** (§1). Each position is covered by "one and only one
   mesh level", which removes level-dependent derived quantities (e.g.
   temperature in cooling) of patch-based AMR.
5. **Refluxing and EMF correction** (§2.1.4, Eq. 1, Figs. 6–8). Coarse
   face fluxes are replaced by the area-weighted sum of the fine ones; on
   coarse/fine faces the coarse edge EMF times its length equals the sum of
   fine EMFs times their lengths. EMFs on edges shared by same-level
   `MeshBlock`s are also replaced by their arithmetic average, because
   round-off, nondeterministic MPI ordering or non-ANSI optimizations
   otherwise create divergence errors that CT never removes.
6. **Restriction and prolongation** (§2.1.5, Eqs. 2–5). Volume-weighted
   restriction of cell data, area-weighted of face data. Cell-centred
   prolongation is minmod-limited linear reconstruction; ghost cells use
   primitive variables, new blocks use conserved variables with a pressure
   floor. Face fields use the Tóth & Roe (2002) divergence-preserving
   prolongation, extended to nonuniform and curvilinear meshes.
7. **Load balancing** (§2.1.6). Per-block cost, user-set or timed;
   at least one block per process; block order cannot be shuffled.
8. **No subcycling** (§2.1.7, §2.2). One global $\Delta t$: the largest
   signal speed is often on the root level, temporal interpolation adds
   error (especially with self-gravity), complexity hurts optimization and
   load balance, and the saving is only about $N/2$ for $N$ levels of equal
   cell count. It is less efficient beyond 10 levels covering ≤1% of the
   volume.
9. **AMR taxonomy** (§2.2). Cell-by-cell (RAMSES, ART); patch-based
   Berger–Oliger/Berger–Colella (Enzo, PLUTO, AMRVAC; Chombo, AMReX);
   block-based (FLASH/PARAMESH, NIRVANA, DISPATCH, Athena++).
10. **Coordinates** (§2.3). Uniform, logarithmic or user spacing;
    Cartesian, cylindrical, spherical-polar; GR metrics (Minkowski,
    Schwarzschild, spherical Kerr–Schild, user stationary). A "polar"
    boundary averages EMFs on radial edges touching the pole.
11. **Parallelism** (§2.4, §2.5). Coarse-grained OpenMP (one thread per
    `MeshBlock`, `MPI_THREAD_MULTIPLE`); loop-level OpenMP was found
    inefficient. GPU only through the Kokkos port K-Athena. Tasks carry a
    bit `task_id` and a bit-field dependency; nonblocking receives are
    posted before execution.
12. **Discretization** (§3.1–§3.2). Nonideal MHD (viscosity, Ohmic and
    ambipolar diffusion, conduction; Eqs. 6–9) with permeability 1, general
    EOS. Upwind CT of Gardiner & Stone (2005, 2008); the EMF recipe is not
    restated. Reconstruction DC, PLM or PPM in primitive or characteristic
    variables; PLM with the van Leer (1974) limiter or Mignone (2014) on
    nonuniform/curvilinear meshes; PPM with the McCorquodale et al. (2015) /
    Colella & Sekora (2008) limiter on Cartesian meshes. The default CT is
    second order, so accuracy stays $\mathcal O(h^2)$ with PPM.
13. **Riemann solvers** (§3.2.2, §4.2.2). HLLE, HLLC, HLLD, Roe; no exact
    solver; HLLE/HLLC/HLLD extended to a general EOS. The H-correction is
    not implemented. Relativistic HLLE, HLLC and HLLD.
14. **Time integrators** (§3.2.3, Eqs. 11–15). Method of lines in the
    Ketcheson (2010) 2S low-storage form; CTU is not implemented. RK1, VL2
    (default; predictor with first-order fluxes), SSPRK(2,2), SSPRK(3,3).
    $\nu = 1$ for RK2/RK3; VL2 has $\nu = 1$ in 1D and $\nu = 1/2$ in 2D/3D,
    positive-definite for $\nu \le 1/3$ with first-order fluxes in both
    stages.
15. **Curvilinear angular momentum** (§3.2.4, Eqs. 16–19). Geometric source
    terms built from Riemann face stresses are algebraically identical to
    the conservative angular-momentum update, so angular momentum is
    conserved to machine precision.
16. **Diffusion and physics** (§3.2.5–§3.2.6, §5). Unsplit explicit
    diffusion or RKL1/RKL2 super-time-stepping; passive scalars; shearing
    box and orbital advection. FFT self-gravity is public; full-multigrid
    self-gravity is being extended to AMR; implicit radiation transport
    implemented.
17. **Relativistic MHD** (§4). Normal-frame four-velocity primitives,
    Newman & Hamlin (2014) inversion, $\sqrt{-g}$-weighted CT, energy and
    $z$-angular momentum conserved to machine precision for ignorable
    coordinates.
18. **Performance** (§3.6, Tables 2–3). One Skylake 6148 core, 3D MHD,
    HLLD+PLM, VL2, $64^3$ block: 2.924 Mzone-cycles/s; PPM halves it.
    Claimed per-core lead over the public FLASH, PLUTO and Enzo "in some
    cases by as much as a factor of 10". About 85% of the MHD code
    vectorized; full-node per-core throughput is about 2× lower
    ("cache-limited"). K-Athena on a Volta GPU ≈5× one 20-core Skylake.
19. **Scaling** (§3.6.3, Figs. 33–35). Cray XC50, $64^3$ per block, one
    block per process, 8 → 250 nodes: ≈97% (hydro, HLLC) and ≈95% (MHD,
    HLLD). Oakforest-PACS KNL, 2048 nodes = 524,288 threads: 86% (hydro)
    and 84% (MHD) against 8 nodes. With AMR, $16^3$ blocks halve throughput
    but cut time to solution ≈5×.
20. **Block-size cost model** (§3.6.5, Eq. 30). Cost
    $A + b/x + c/x^3$ for $x$ cells per block side; $8^3$–$16^3$ blocks are
    recommended for AMR, the largest possible for uniform grids. The AMR
    linear-wave run shows ≈20% AMR overhead (132.5 → 106.0 Mzone-cycles/s,
    §3.4.1).

**Tests.** [Linear waves](/benchmarks/linear-wave-convergence.md) in 3D
along the grid diagonal, $N = 16$–256 (§3.3.1, Fig. 11): strictly second
order with VL2 or PLM, RK3+PPM ≥10× lower errors; the same with AMR, still
second order (§3.4.1, Fig. 19). Nonideal fast-wave decay (§3.3.2); Shu–Osher
(§3.3.3); [Brio–Wu](/benchmarks/brio-wu-shock-tube.md) with 256 cells
(§3.3.3, Fig. 15: characteristic reconstruction needed); oblique C-shock
(§3.3.4); Liska–Wendroff implosion symmetric to machine epsilon (§3.3.5);
Kelvin–Helmholtz against Dedalus (§3.3.6); [double Mach reflection](/benchmarks/double-mach-reflection.md)
with AMR, ×4.4 faster than uniform (§3.4.2, Fig. 20); KHI with AMR (§3.4.3);
3D hydro and MHD [Sedov–Taylor blast](/benchmarks/sedov-taylor-blast-wave.md)
with AMR (§3.4.4, Figs. 23–25); curvilinear advection (§3.5.1);
[field-loop advection](/benchmarks/field-loop-advection.md) through the pole
of a spherical-polar grid (§3.5.2, Fig. 29); spherical-polar blast with AMR
(§3.5.3); relativistic shock tube, magnetized KHI, magnetized blast in 2D
and 3D, and a GR torus (§4.3). The paper has no Sod shock tube.

# Notation map

| Stone et al. (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P$ (§3), $p$ (§3.4), $p_g$ (§4) | $p$ | gas pressure |
| $P^* = P + B^2/2$ | $P^*$ | |
| $E$ | $E$ | total energy density; in §4 the SR conserved energy, which includes $D$ and so is not the Valencia $\tau$ |
| $e$ | $\rho e$ | **collision:** the paper's $e$ is internal energy per volume |
| $\mathbf B$ | $\mathbf B$ | permeability 1 (§3.1) |
| $C_f$, $c_f$; $c_A$ | $c_f$; $c_A$ | |
| $c_s$ (§3.1); $a$ | words; $c_s$ | **collision:** the paper's $c_s$ is isothermal, its $a$ adiabatic |
| $\gamma$ (§3); $\Gamma$ (§4) | $\gamma$ | adiabatic index |
| $\gamma$ (§4) | $W$ | **collision:** Lorentz factor |
| $\gamma_{s0}$, $\gamma_{s1}$, $\beta_{s,s-1}$, $\delta_s$ | words | low-storage RK coefficients; collide with $\gamma$ and $\beta^i$ |
| $F(u)$ (Eq. 11) | $\mathcal L(u)$ | flux-divergence operator, not the physical flux |
| $C_0$ | $\nu$ | Courant number |
| $\nu$ | words | **collision:** kinematic viscosity |
| $\kappa$ | words | **collision:** thermal conductivity, not opacity |
| $\mathbf J$ | $\mathbf J$ | |
| $\varepsilon$ (Eq. 1) | $\boldsymbol{\mathcal E}$ | edge EMF |
| $N_G$ | $n_{\mathrm g}$ | |
| cells per block side ($x$ in Eq. 30) | $N_{\mathrm b}$ | |
| refinement factor 2 | $r_{\mathrm{ref}} = 2$ | |
| $\Delta x$ | $h$, $h_l$ | |
| $n$ (dimensions, §2.1.2) | $d$ | **collision:** registry $n$ is the time level |
| $W = (\rho, \mathbf v, P, \mathbf B)$ | words | **collision:** registry $W$ is the Lorentz factor; the paper's $W(x)$ is also the cost (Eq. 30) |
| $U$ | $u$ | |
| $\alpha$, $\beta^i$, $\gamma_{ij}$ | $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$ | |
| $D$, $\mathbf M$ | $D$, $S_i$ | **collision:** the paper's $\mathbf S$ is a stress tensor |
| $\beta = 2p/B^2$, $\sigma = 2p_m/\rho$ | words | plasma beta and magnetization |

# Pages created or updated

* [Athena++](/software/athena-plus-plus.md).
* [Constrained transport](/methods/constrained-transport.md), [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md), [Field-loop advection](/benchmarks/field-loop-advection.md), [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), [MHD blast wave](/benchmarks/mhd-blast-wave.md), [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Also cited on [Sod shock tube](/benchmarks/sod-shock-tube.md), [Athena (astrophysical MHD code)](/software/athena.md), [Enzo (AMR code for cosmological and astrophysical fluid flow)](/software/enzo.md), [PLUTO (multiphysics code for astrophysical gas dynamics, with Chombo AMR)](/software/pluto.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2020-ApJS-Stone-1038471538-4365ab929b.pdf`.
   * **Version.** The publisher's version of record (40 pages, © AAS
     2020), not a preprint. No numbered code version is printed.
   * **Identity.** doi:10.3847/1538-4365/ab929b, checked on Crossref:
     Astrophys. J. Suppl. 249(1), article 4; online 2020-06-25, print
     2020-07-01; authors Stone, Tomida, White, Felker; 102 references.
   * **How it was read.** Text extraction, all sections; Eq. 1 and the
     relativistic KHI set-up checked on rendered pages.
   * **Recorded as printed.** Eq. 7 prints $\partial v_j/\partial x_j$ in the
     viscous stress where $\partial v_j/\partial x_i$ is presumably meant;
     Eq. 9 prints the heat flux as $+\kappa\nabla T$; the refinement
     indicators of Eqs. 27–28 use an undefined $h$; §3.4.1 calls its set-up
     "identical to … Section 3.3.2" (the ideal linear wave test is §3.3.1);
     §3.3.3 shows VL2+PPM and RK3+PPM but says RK3+PPM "outperforms the
     VL2+PLM method". CFL numbers of the ideal linear wave, DMR, KHI-AMR and
     Sedov tests are not printed.
   * **Reference list:** 102 entries, titles not printed (AAS style); DOIs
     printed only for Stout et al. (1997) and Turk (2013). In printed order
     the key `mignone-2012` falls to Mignone, Flock et al. (A&A 545:A152)
     and the PLUTO AMR paper (ApJS 198:7, the ingested
     [Mignone et al. (2012)](/sources/mignone-2012.md)) to `mignone-2012-b`;
     the merge must swap them. Grete et al. is printed as "2009,
     arXiv:1905.04341" (cited as 2019 in the text); Lamberts et al. as
     "2012, A&A, 560, A79"; Burns et al. as "PhRvD, 2, 023068"; Stout et al.
     as "Proc. EEE Conf." — all kept as printed, unverified.
