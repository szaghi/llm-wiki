---
type: Source
title: "Rossazza et al. (2026) — The PLUTO Code on GPUs: A First Look at Eulerian MHD Methods"
description: "First description of gPLUTO, a C++ rewrite of PLUTO that runs the whole ideal-MHD time step on NVIDIA GPUs through OpenACC, with flat coalesced arrays, Unified Memory, device-side halo packing, weak and strong scaling to 256–512 nodes, a node-to-node GPU/CPU ratio of about 9, and GPU-frequency energy savings of 8–11 %."
resource: "doi:10.1016/j.ascom.2026.101076"
source_kind: paper
authors: [Rossazza M., Mignone A., Bugli M., Truzzi S., Riha L., Panoc T., Vysocky O., Shukla N., Romeo A., Berta V.]
year: 2026
venue: "Astron. Comput. 55:101076"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2026-AstronComput-Rossazza-101016jascom2026101076.pdf"
tags: [software, mhd, gpu, openacc, constrained-transport, divergence-cleaning, performance, scaling]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper is a first description of [gPLUTO](/software/gpluto.md), a
complete C++ rewrite of [PLUTO](/software/pluto.md) that runs the whole
time step on NVIDIA GPUs through OpenACC directives (abstract, §1, §3).
Only the classical ideal-MHD, uniform-Cartesian, finite-volume path is
covered: SSP-RK3 method of lines, WENOZ or parabolic reconstruction of
primitive variables, HLLD fluxes, and either upwind constrained transport
(UCT-HLLD of Mignone & Del Zanna 2021) or GLM cleaning (§2). The
implementation sections describe collapsed `parallel loop` kernels with a
sequential loop over variables, flat `Ary` arrays ordered for coalesced
access, direction-templated kernels that keep small arrays in registers,
CUDA Unified Memory plus explicit data directives, and an MPI halo exchange
packed and unpacked on the device with up to 26 neighbours in 3D (§3).
Weak and strong scaling of a 3D Orszag–Tang vortex and a 3D circularly
polarized Alfvén wave are measured on MareNostrum 5 ACC, Leonardo Booster,
MeluXina and Leonardo DCGP (CPU); efficiency stays near 0.9 to 256–512
nodes, and a GPU node is about 9× faster than a CPU node (§4.1–§4.2). A
GPU clock study on Karolina finds 8 % (Orszag–Tang) and 11 % (Alfvén wave)
energy savings for at most about 6 % longer runtime (§4.3). AMR,
relativistic and non-ideal physics, particles and other coordinates are
deferred to a forthcoming paper.

# Key claims

1. **Rewrite and programming model** (abstract, §1, §3.1): C++ for
   templates, classes and polymorphism; OpenACC as simpler than CUDA and
   "interchangeable" (the same source runs on CPUs without the directives).
   OpenMP for AMD is future work (§5).
2. **Device residency** (§3.1): "The entire computational workload is
   handled by the GPUs"; the CPU does the OS, system memory and I/O, with no
   host–device transfers during computation.
3. **Kernels** (§3.2, Fig. 1): `parallel loop collapse(3) present(...)`;
   the variable loop is `loop seq`.
4. **Memory** (§3.3): `-gpu=managed` Unified Memory plus `enter data` /
   `exit data` directives for deep copies.
5. **Layout** (§3.3, Fig. 2): flat arrays in `Ary` classes, $x$ index
   fastest and variable index slowest for coalescing; sweep buffers viewed
   as per-row 2D slices, reordered for the $y$ sweep.
6. **Templates** (§3.3, Fig. 3): direction-templated kernels keep local
   arrays in registers.
7. **MPI** (§3.4, Fig. 4): ArrayLib replaced by plain buffers and
   non-blocking messages to up to 26 neighbours; device-side packing on two
   `async` queues; buffers from `acc_malloc`. CUDA-aware MPI not stated.
8. **Numerics** (§2, eqs. 1–8): ideal MHD, SSP-RK3, primitive
   reconstruction, generic upwind flux, Powell / cleaning / CT (Mignone &
   Del Zanna 2021 form).
9. **GLM for memory** (§4.1): strong scaling uses cleaning "because this
   algorithm requires less device memory than the constrained transport
   method"; no numbers.
10. **Weak scaling, Orszag–Tang, CT** (§4.1, Fig. 5, Table 2): above 95 %
    at 256 nodes (MareNostrum 5), 88 % at 512 nodes (Leonardo Booster),
    91 % at 32 nodes (MeluXina), above 95 % to 64 nodes and 84 % at 128
    (Leonardo DCGP).
11. **GPU against CPU node** (Table 3): ratios 8.98–9.24 from 1 to 64
    nodes, 10.24 at 128; "a factor ≈ 9 acceleration (per node usage)".
12. **Strong scaling** (§4.1–§4.2, Tables 4–5): Orszag–Tang 0.90 and 0.89;
    Alfvén wave 0.97 and 0.93 as printed.
13. **Energy** (§4.3, Table 6, Figs. 10–12): up to 8 % and 11 % savings at
    ≤ 6 % longer runtime.

# Tests

Performance only; no accuracy is shown (§4). Hardware (Table 1):
MareNostrum 5 ACC (4 NVIDIA Hopper GPUs of 64 GB per node), Leonardo
Booster (4 A100 per node), MeluXina (4 A100 of 40 GB per node), Leonardo
DCGP (2 × 56-core Xeon 8480+ per node); all runs FP64, HLLD, WENOZ,
SSP-RK3.
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), 3D variant
  (§4.1, eq. 9): periodic unit cube, $\rho = 25/9$, $p = 5/3$, the 2D
  velocity and field of the classic problem with a $z$-modulation of the
  in-plane velocity by $1 + \sin(2\pi z)/5$ and $v_z = 0.2\sin(2\pi z)$,
  "similar to" Helzel et al. (2011), $t = 0.5$. Weak scaling with CT on
  per-node grids $704\times704\times352$ ($704\times704\times350$ on DCGP,
  $512^3$ on MeluXina); strong scaling with GLM in six groups from
  $832\times832\times416$ on 1 node to $3328\times1664\times1664$ on 32
  nodes, each spanning 8× in nodes.
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
  3D (§4.2, eq. 10): unit cube, $\rho = 1$, $p = 0.1$, $\gamma = 5/3$,
  amplitude 0.1; Leonardo Booster and MareNostrum 5; weak (CT) 0.97 and
  0.95 at 256 nodes; strong (GLM) as above.
* Energy (§4.3): both tests, strong scaling over 1–32 Karolina nodes
  (8 A100 each), SM clock 1410 down to 990 MHz in 60 MHz steps; problem
  sizes not stated. Default runs: Orszag–Tang 129 s and 365 kJ on 1 node,
  11.2 s and 719 kJ on 32; Alfvén wave 189 s and 524 kJ, 13.2 s and 885 kJ.

# Notation map

| Rossazza et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal U$, $\langle\mathcal U\rangle_{\mathbf c}$ | $u$, cell average | |
| $\mathsf T$ (flux tensor), $\mathcal S$ | $\mathbf f(u)$, $s(u)$ | |
| $\rho$, $\mathbf v$, $\mathbf B$, $p$ | same | no $4\pi$ in $p_t$: registry default units |
| $\mathcal E$ | $E$ | total energy density |
| $p_t$ | $P^*$ | |
| $\Gamma$ | $\gamma$ | **collision:** registry $\Gamma_1$ is the generalized adiabatic index |
| $\Delta x$, $\Delta y$, $\Delta z$ | $h$ per direction | |
| $\mathbf c = (i,j,k)$ | cell multi-index | **collision:** registry $c$ is the speed of light |
| $\hat F$, $\hat G$, $\hat H$ | $\hat f_{i+1/2}$ per direction | |
| $\mathcal L$ | $\Delta t\,\mathcal L(u)$ | **caveat:** the paper's operator contains $\Delta t$ |
| $\langle\mathcal U\rangle^*$, $\langle\mathcal U\rangle^{**}$ | $u^*$, $u^{**}$ | RK stage values, defined on the gPLUTO page |
| $\mathcal V_c$, $\mathcal V^L_{i+1/2}$, $\mathcal V^R_{i-1/2}$ | primitive variables (words); minus/plus interface sides | registry $-$ = left, $+$ = right |
| $\mathcal R^\pm_x$ | words (reconstruction operator) | the paper's $\pm$ is a direction, opposite in meaning to the registry's sides |
| $D_{i+1/2}$ | words (dissipation matrix) | |
| $\epsilon$, $\phi$, $\mathbf k$, $\zeta(z)$, $L_x$ | words | benchmark-local |
| $N_t$ | words (total grid points) | **collision:** registry $N$ is cells per dimension |
| $T_1$, $T_N$ | words (wall-clock times) | **collision:** registry $T$ is temperature; the paper's $N$ is a node count |

# Pages created or updated

* Created [gPLUTO](/software/gpluto.md),
  [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Constrained transport](/methods/constrained-transport.md),
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md).
* Per the batch plan, also cited on: [PLUTO](/software/pluto.md),
  [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md),
  [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md),
  [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md).
* Also cited on (batch 3) [Adaptive mesh refinement in astrophysical codes](/methods/adaptive-mesh-refinement.md), [GAMER (GPU-accelerated octree AMR code), MHD extension](/software/gamer.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2026-AstronComput-Rossazza-101016jascom2026101076.pdf`.
   * **Version.** arXiv:2511.20337v1 [physics.plasm-ph], 25 Nov 2025, 14
     pages; not the journal typeset version. No code version, repository
     URL or compiler is printed.
   * **Identity.** doi:10.1016/j.ascom.2026.101076, checked on Crossref
     (title and the ten authors in order match page 1): Astron. Comput.
     55:101076, issued 2026-04.
   * **How it was read.** Text extraction of all sections; eq. 4 checked on
     the rendered page 2 and eq. 10 on page 8. Throughput values (Fig. 6)
     are read from a log-scale plot; the paper prints none.
   * **Recorded as printed.**
     * Eq. 4 is dimensionally inconsistent: the time derivative of the cell
       average is set to $-\frac{\Delta t}{\Delta x}$ times the flux
       difference; eq. 5 is consistent with an operator that already
       contains $\Delta t$.
     * Eq. 5 prints the last SSP-RK3 stage as one third of
       $u^n + 2u^{**} + \mathcal L(u^{**})$; the Shu–Osher scheme needs
       twice the operator term. The concept pages write the standard form.
     * Eq. 10 prints the $y$ unit vector twice in the velocity; the field
       line implies the second is $z$.
     * The Table 3 caption swaps the partitions (DCGP with 4 A100 GPUs,
       Booster with 112 CPU cores); Table 1 and the text are correct. The
       Table 6 caption says "990 GHz" for MHz.
     * The §4.2 strong-scaling averages (0.97 Leonardo, 0.93 MareNostrum 5)
       are not reproducible from Table 5: the last-row means are 0.95 and
       0.817, the means over all non-base entries 0.967 and 0.91. The Table
       4 averages (0.902, 0.888) reproduce.
     * Table 1 names the GPUs only "NVIDIA Ampere" and "NVIDIA Hopper"; A100
       appears only in the Table 3 caption and H100 nowhere.
     * §1 claims the tests highlight the code's "effectiveness in
       reproducing them"; §4 shows no accuracy evidence.
     * Not stated: global weak-scaling grids, CFL number, CUDA-aware MPI,
       compiler, energy-test problem sizes, the CPU build of the DCGP
       comparison, I/O implementation.
   * **Reference list:** 66 printed entries, 65 distinct ([44] repeats
     [26], Mignone et al. 2010, MNRAS 402:7), merged complete. The AthenaK
     preprint (arXiv:2409.16053, 2024) is merged into
     [stone-2026](/sources/stone-2026.md). Powell et al. (1999) is printed
     correctly as J. Comput. Phys. 154:284. Remapped by vol:page:
     Mignone, Tzeferacos & Bodo (2010) to `mignone-2010-c` and Mignone,
     Plewa & Bodo (2005) to `mignone-2005-b`. Seven A&A papers printed as
     "Journal of Computational Physics" were entered under A&A with a note,
     and "Fluidika" as Fluids 7:87, each from its printed DOI on Crossref.
     D. Zhang (2018, Galaxies 6:114) is a different work from the ingested
     [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md) and is keyed
     `zhang-2018-c`. The bibliography holds 1509 entries after this batch.
