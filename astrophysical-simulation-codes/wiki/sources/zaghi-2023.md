---
type: Source
title: "Zaghi et al. (2023) — Efficient GPU parallelization of adaptive mesh refinement technique for high-order compressible solver with immersed boundary"
description: "Presents ADAM, a Fortran 2003 block-octree AMR library whose compute phase runs entirely on NVIDIA GPUs through CUDA Fortran with a block-index-contiguous device layout and CUDA-aware MPI, the octree being a serial CPU hash map, and its WENO / Lax–Friedrichs / SSP-RK3 Navier–Stokes application NASTO with an immersed boundary; on V100s the compute phase scales near-ideally to 8 GPUs and about 90% at 16, while the serial AMR update dominates at high block counts."
resource: "doi:10.1016/j.compfluid.2023.106040"
source_kind: paper
authors: [Zaghi S., Salvadore F., Di Mascio A., Rossi G.]
year: 2023
venue: "Comput. Fluids 266:106040"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2023-CompFluids-Zaghi-101016jcompfluid2023106040.pdf"
tags: [software, hydro, amr, gpu, cuda, performance, scaling]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper presents ADAM, a Fortran 2003 object-oriented library for
block-based octree AMR on Cartesian grids, built so that the solver runs
entirely on NVIDIA GPUs through a CUDA Fortran back end with CUDA-aware MPI,
and NASTO, a compressible Navier–Stokes application on it with
finite-difference WENO, Lax–Friedrichs (Rusanov) flux-vector splitting, SSP
RK3 and an immersed boundary (§2, §3). Code is split by its dependence on
the equations and on the back end (Fig. 1). The octree is a hash map on the
CPU, replicated on all processes and updated serially; the field is copied
to a transposed GPU array with the block index fastest, used for the whole
compute phase; host–device copies happen only at I/O and AMR updates
(§2.2). Performance is measured on Marconi100 V100s on a 3D Mach 2.89 shock
diffraction by a sphere: the compute phase scales near-ideally to 8 GPUs,
about 90% at 16 and below 60% at 32, while the serial AMR update scales
poorly and reaches 527.97 s per update at 684,258 blocks (§3.2, Table 1).
Validation is qualitative (§3.3, Appendix). Merged into
[ADAM and NASTO](/software/adam.md).

# Key claims

1. **Modules by dependency class** (§2.1, Fig. 1): independent of equations
   and back end (AMR grid, I/O); equation-only; back-end-only (ghost
   updates); both (fluxes), to avoid one variant per equation set per back
   end.
2. **Language** (§2.2): Fortran "following the Fortran 2003 object style",
   derived types with type-bound procedures.
3. **Mesh** (§2.2): identical Cartesian blocks of $N_{\mathrm b}^3$
   cell-centred cells, 26 ghost regions per block, a single root block,
   splitting into 8 children ($r_{\mathrm{ref}} = 2$): "the classical
   octree".
4. **Octree** (§2.2, Fig. 2): hash map with $O(1)$ insertion and deletion,
   64-bit keys linearizing level and block coordinates; shared by all
   processes; operations "essentially serial" (a stated limitation).
5. **Device layout and residency** (§2.2): the device field is transposed so
   the block index is contiguous, "to maximize access data coalescing for
   contiguous CUDA threads"; it is allocated once to fill the GPU memory;
   the compute phase runs on the GPU and copies occur only at I/O and AMR
   updates; only the CUDA Fortran back end exists.
6. **No AMR in the compute core** (§2.2): neighbour and coordinate arrays
   are precomputed at each AMR update; "there is in fact no evidence that
   this is AMR code" in the compute phase.
7. **AMR update** (§2.2, Fig. 3b): marking with a CPU sanitizing pass (full
   sibling sets for recomposition, 2:1 level balance, maximum level);
   refinement or coarsening on the host "by interpolation" (order not
   stated); Morton-curve load balancing; copy back; ghost maps regenerated.
   Thresholds should leave a hysteresis band against "flip-flop".
8. **Ghost update** (§2.2): same-process, other-process (CUDA-aware MPI),
   physical boundaries; "second-order interpolations" across level jumps.
9. **NASTO** (§3.1, eqs. 1–10): non-dimensional Navier–Stokes; conservative
   finite differences with WENO and Lax–Friedrichs flux-vector splitting;
   three-stage SSP RK3; one global time step from local Courant conditions
   (eqs. 8–9); immersed boundary by signed distance and pseudo-time
   extrapolation.
10. **Scaling** (§3.2, Fig. 5): efficient "if each GPU has a mesh portion
    greater than 250 K cells".
11. **AMR cost** (§3.2, Figs. 5, 7): the AMR update time is
    "dramatically high when the number of blocks increases".
12. **Resolution claim** (§3.3, §4): "the finest resolution shown in
    literature for the fully three dimensional diffraction of a strong shock
    wave over a sphere".

**Tests.** (i) *Shock diffraction by a sphere* (§3, Fig. 4, §§3.2–3.3,
Table 1): cube of 20 units, Mach 2.89 shock, post-shock
$\rho = 5.1432014$, $p = 9.0454500$, velocity 2.0451168, pre-shock
$\rho = 1.4$, $p = 1$; refinement on the density-gradient modulus.
Thirteen runs on 1–256 V100s, up to 684,258 blocks and 350.3 M cells;
strong scaling 1.019 to 0.0541 s per iteration from 1 to 32 GPUs; block
size 16 lowers the grind time from 0.28 to 0.16 against 8. Physics compared
visually with one digitized schlieren plate of Bryson & Gross (1961) at
$t = 4$. (ii) *Moving isentropic vortex* (Appendix, Figs. A.16–A.18):
periodic cube, levels 2–5, about 2.4 M cells, WENO3; tracked with some
smearing; strong scaling to 16 GPUs including AMR time. Not printed:
precision, compiler, GPUs per node, Courant number, WENO order of the shock
test, sphere radius, Reynolds number, regrid frequency.

# Notation map

| Zaghi et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\vec U$, $\vec Q$ | $u$, $s(u)$ | source zero here |
| $\overline{\overline{F_c}} + \overline{\overline{F_d}}$ | $\mathbf f(u)$ plus a viscous flux in words | the registry flux is inviscid |
| $\rho$, $\vec v$, $p$, $T$, $\gamma$ | $\rho$, $\mathbf v$, $p$, $T$, $\gamma$ | |
| $E$ (specific total energy) | $E/\rho$ | **collision:** registry $E$ is the energy density |
| $a$ (sound speed) | $c_s$ | **collision:** registry $a$ is the scale factor |
| $\tau_{ij}$, $\mu$, $\lambda$, $k$ | words (viscous stress, viscosity, second viscosity, conductivity) | **collisions** with $\tau$, $\mu$, $\lambda^{(p)}$ |
| $c_p$, $c_v$, $R$ | words | **collision:** registry $c_p$ is the GLM damping parameter; the paper's $R$ is also the residual |
| $h$ (grid spacing) | $h$ | |
| $h(x)$, $h_{x\pm h/2}$ (eq. 5) | $\hat f_{i\pm1/2}$ | **collision** with the cell size $h$ |
| $R(\cdot)$ (residual) | $\mathcal L(u)$ | |
| $Dt$, $\Delta t_i$; $CFL_i$, $CFL$ | $\Delta t$; $\nu$ | eq. 8 is a local Courant number, eq. 9 the global minimum |
| $N_s$, $b_k$, $a_l$, $K_k$ | words | Butcher coefficients; $a$ collides with the scale factor |
| $\phi$, $\mathbf n$, $\tau$ (pseudo-time) | words | **collisions** with $\Phi$, $\hat{\mathbf n}$, $\tau$ |
| level, $(b_x, b_y, b_z)$ | $l$, words | |
| $N_{xyz}$ | $N_{\mathrm b}$ | cells per block side |
| $\delta_C$, $\delta_F$, $\Delta_{coarse}$, $\Delta_{fine}$, $R_\delta$ | words | requested coarsest and finest cell sizes and their ratio, not the realized $h_l$ |
| $N_{GPUs}$, $N_{blocks}$, $N_{cells}$ | words | bare $N$ is cells per dimension in the registry |
| $T$, $T_g$, $T_{AMR}$ | words (iteration time, grind time, AMR-update time) | **collision:** $T$ is temperature |

# Pages created or updated

* Created [ADAM and NASTO](/software/adam.md).
* Updated [GAMER](/software/gamer.md).
* Per the batch-3 page plan, also cited on
  [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md),
  [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md),
  [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md),
  [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md) and
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
  (drafted by other drafters; the compiler confirms the final list).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2023-CompFluids-Zaghi-101016jcompfluid2023106040.pdf`.
   * **Version.** The published Elsevier version of record (journal header
     and pagination on every page), 16 pages, open access CC BY-NC-ND;
     received 29 Dec 2022, accepted 20 Aug 2023, online 9 Sep 2023. No code
     version, repository URL or licence is printed; "Data will be made
     available on request".
   * **Identity.** doi:10.1016/j.compfluid.2023.106040, printed on page 1
     and checked on Crossref (title and the four authors match): Comput.
     Fluids 266:106040, issue November 2023; 70 references deposited.
   * **How it was read.** Text extraction of all sections and the
     Appendix; eqs. 1–3 checked on the rendered page 6; Table 1 transcribed
     in full; Fig. A.18 speed-ups read from the plot (approximate).
   * **Recorded as printed.** Table 1 labels the grind time in seconds, but
     its values are seconds per $10^6$ cells per GPU (run 1:
     1.019/3.6 = 0.283). The requested cell sizes (e.g. 0.5, 0.125) cannot
     be realized by a root block of 20 units with 8 cells per side halved
     per level, so they are targets; the stated "8 billions" uniform
     equivalent fits a finest level 8 ($2048^3$ cells), not the requested
     finest size (reader's inference). Figures 11, 14, 15 label grids #3,
     #4, #6, #7, which match Table 1 runs 11, 12, 7, 8 by their parameters.
     §3.2 says AMR update times vary "around 3.5 s" in the block-size
     series; Table 1 gives 4.25, 2.96 and 4.3 s. The Fig. A.16 caption
     reads "Shock wave diffraction simulation setup" but shows the vortex.
     Eq. A.5 prints $Y - Y_v$ in the $v$ component where a rotating vortex
     has $X - X_v$, and eq. 7 prints a single-index Butcher coefficient
     $a_l$; both reproduced as printed. The Appendix strong scaling is
     called "comparable" with §3.2 although its speed-ups (about 7.6 at 16
     GPUs) are lower.
   * **Reference list:** 70 entries, matching Crossref. Same-author-year
     works are disambiguated: Berger & Colella (1989, J. Comput. Phys.) is
     `berger-1989` and Berger & LeVeque (1989, AIAA) is `berger-1989-b`;
     `brahmi-2020` and `brahmi-2020-b`.
