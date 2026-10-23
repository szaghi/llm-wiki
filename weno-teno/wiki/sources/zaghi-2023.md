---
type: Source
title: "Zaghi et al. (2023) — Efficient GPU parallelization of adaptive mesh refinement technique for high-order compressible solver with immersed boundary"
description: "Presents ADAM, a Fortran 2003 CUDA-Fortran and MPI library for block-octree adaptive mesh refinement with an immersed boundary, and its WENO finite-difference Navier–Stokes solver, measured on up to 256 V100 GPUs for the three-dimensional diffraction of a strong shock by a sphere."
resource: "doi:10.1016/j.compfluid.2023.106040"
source_kind: paper
authors: [Zaghi S., Salvadore F., Di Mascio A., Rossi G.]
year: 2023
venue: "Comput. Fluids 266:106040"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_Zaghi_Efficient_GPU_parallelization_of_adaptive_mesh_refinement_te.pdf"
tags: [software, amr, gpu, immersed-boundary, finite-difference, weno]
timestamp: 2026-10-23T16:00:00Z
---

# Summary

The paper presents [ADAM](/software/adam.md), an object-oriented Fortran 2003
library for block-based octree [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
on GPU-accelerated clusters, coupled with the
[immersed-boundary method](/methods/immersed-boundary-method.md) of Di Mascio &
Zaghi (2021), and NASTO, a compressible Navier–Stokes solver built on it. The
code is split by its dependence on the equations and on the computing back-end,
so that $N_{\text{equations}}\times N_{\text{back-ends}}$ copies are avoided. The
grid is a set of identical Cartesian blocks of $N_{xyz}^3$ cells with 26 ghost
regions each; the octree lives in a hash map keyed by a 64-bit integer that
linearizes (level, $b_x$, $b_y$, $b_z$); the GPU copy of the field is transposed
so that the block index is contiguous. The only back-end is CUDA Fortran with
CUDA-aware MPI. The tree is kept serially on the CPU and replicated on every
process; load balancing follows a Morton space-filling curve.

NASTO discretizes with a [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
with [WENO reconstruction](/methods/weno-js-reconstruction.md),
[Lax–Friedrichs (Rusanov) flux-vector splitting](/methods/lax-friedrichs-flux.md)
and three-stage third-order [SSP Runge–Kutta](/methods/ssp-runge-kutta.md).
The immersed boundary extrapolates the solution into the body along the normal
of a signed-distance function, by marching a transport equation in pseudo-time.

The test is the three-dimensional [diffraction](/benchmarks/shock-diffraction.md)
of a planar shock, stated as Mach 2.89, by a sphere, after the experiment of
Bryson & Gross (1961), on NVIDIA V100 GPUs (Marconi100, CINECA). Strong scaling
on 3.6M cells is superlinear up to 8 GPUs and about 90% efficient at 16. Larger
blocks lower the grind time. Raising the fine/coarse resolution ratio from 2 to
32 reaches 684,258 blocks and 350.3M cells on 256 GPUs with less than a
threefold rise in grind time, but the serial AMR update then takes 528 s. An
appendix runs an [isentropic vortex](/benchmarks/isentropic-vortex.md) with
WENO3.

# Version read

Version of record (Elsevier typeset, open access; received 29 Dec 2022, accepted
20 Aug 2023, online 9 Sep 2023), 16 pages, all read; pages 6, 13 and 14 also
read visually. Page 1 matches Crossref (title, four authors in this order,
venue, DOI). Equation, table and figure numbers are those of this version.

# Key claims

Registry notation: conserved variables $u=(\rho,\rho v,E)$, sound speed $c$,
grid spacing $\Delta x$; the source's required coarsest and finest cell sizes
$\delta_C$, $\delta_F$ and their ratio $R_\delta=\delta_C/\delta_F$ are kept
(page-local).

1. ADAM is a new AMR library with an immersed boundary for compressible Navier–Stokes flows, designed for GPU-accelerated exascale machines and modular in equations and back-end (Abstract, §2.1, Fig. 1). **Stated**
2. The code falls into four categories: independent of equations and back-end (AMR grid, I/O); equation-dependent only (field and method initialization); back-end-dependent only (ghost updates); dependent on both (convective and viscous fluxes) (§2.1). **Stated**
3. Every block holds the same number of equispaced, cell-centred cells and full 3D ghost layers: 26 ghost regions (6 faces, 12 edges, 8 corners) (§2.2). **Stated**
4. Refinement splits a block into 8 identical children and coarsening rejoins 8 siblings into their parent; a block is indexed by its level and $(b_x,b_y,b_z)$, which forms an octree (§2.2). **Stated**
5. The octree is stored in a hash map with $O(1)$ insertion and deletion, keyed by 64-bit integers that linearize (level, $b_x$, $b_y$, $b_z$) (§2.2). **Stated**
6. The field is a 5-index array (three space indices, variable, block) with the block index contiguous, plus a map between hash-map and field-block indices; the GPU array is transposed with the block index first, to coalesce memory access of contiguous CUDA threads (§2.2). **Stated**
7. The whole computation runs on the GPU without CPU–GPU copies; copies (with transposition) occur only at I/O and at AMR updates (§2.2). **Stated**
8. The octree is shared by all processes and the tree operations are essentially serial, a limitation of the current implementation (§2.2, §3.2, §4). **Stated**
9. An AMR update has three phases: block marking on the back-end plus CPU sanitizing (coarsening only if all 8 siblings exist and are marked, adjacent blocks differ by at most one level, a maximum level); hash-map update and refinement/coarsening by interpolation on the CPU; Morton-curve load balancing, redistribution and regeneration of the ghost maps (§2.2, Fig. 3). **Stated**
10. Refinement uses hysteresis: split above a threshold $S_{\text{split}}$, recompose below $S_{\text{recompose}}<S_{\text{split}}$, to avoid flip-flop (§2.2). **Stated**
11. Ghost cells between levels are filled by second-order interpolation; exchange between processes uses CUDA-aware MPI; output is HDF5, one file per process, with an XDMF index (§2.2). **Stated**
12. NASTO uses the conservative finite-difference form (Eq. 5) with WENO reconstruction, Lax–Friedrichs (Rusanov) flux-vector splitting and three-stage third-order SSP Runge–Kutta, with a global time step from the local condition of Eqs. (8)–(9) (§3.1). The WENO order of the shock–sphere runs is not given in the main text; the appendix vortex uses WENO3. **Stated**
13. The immersed boundary extrapolates the solution into the body by marching $\partial_\tau u+n\cdot\nabla u=0$ (Eq. 10, pseudo-time $\tau$, $n$ the normal of the signed distance) to steady state; one propagation step at CFL close to 1 per Runge–Kutta stage suffices (§3.1.1, citing Di Mascio & Zaghi 2021). **Stated**
14. Strong scaling (runs 1–6: 3.6M cells, 7008 blocks of $8^3$): speed-up close to ideal, even superlinear, up to 8 GPUs; about 90% efficiency at 16 GPUs (about 225K cells per GPU); below 60% at 32 GPUs; the code is efficient above about 250K cells per V100. Iteration time $T=1.019$ s on 1 GPU, 0.114 s on 8 (speed-up 8.94), 0.0716 s on 16 (14.23), 0.0541 s on 32 (18.84) (§3.2, Fig. 5, Table 1). **Shown**
15. The AMR update time scales poorly: 4.25 s on 1 GPU, 1.84 s on 32 GPUs (Table 1, Fig. 5). **Shown**
16. Larger blocks lower the grind time $T_g=T\,N_{\text{GPUs}}/N_{\text{cells}}$: 0.28 ($8^3$, 1 GPU), 0.16 ($16^3$, 8 GPUs), 0.21 ($32^3$, 64 GPUs); with $32^3$ blocks the ghost exchange between nodes becomes significant (§3.2, Fig. 6, runs 7–8). **Shown**
17. With fixed $\delta_C=0.5$ and $R_\delta=2,4,8,16,32$ (runs 9–13 on 1, 4, 16, 64, 256 GPUs) the cell count grows by a factor of 4 to 5 per halving of $\delta_F$ instead of 8; the finest grid has 350.3M cells "instead of the 8 billions it would have with uniform refinement" (§3.2, Table 1). **Shown** (see Printed slips)
18. $T_g$ grows with $R_\delta$ by less than a factor 3 (0.20 to 0.49), attributed to ghost communication among more blocks and processes (§3.2, Fig. 7). **Shown**
19. The AMR update becomes very costly with many blocks: 527.97 s for 684,258 blocks (run 13), acceptable for statistically stationary runs, problematic for transient ones (§3.2). **Shown**
20. Largest run: 684,258 blocks, 350.3M cells, 256 V100 GPUs, 25.21 h elapsed (Table 1, run 13). **Shown**
21. The results have the finest resolution in the literature for the fully 3D diffraction of a strong shock by a sphere (§3.3, §4). **Stated**
22. The computed flow agrees qualitatively with Bryson & Gross's plate 5; the main discrepancy is the curved reflected shock, slightly ahead in the digitized experiment, whose digitization carries a large error (§3.3, Fig. 11). **Shown** (qualitative)
23. For a fixed finest size, a larger coarsest size uses more levels (a more adapted grid) and a smaller one a more uniform grid; the better choice depends on whether time-to-solution or finest resolution matters (§3.3, Figs. 13–15). **Shown** (qualitative)
24. Appendix vortex: 4768 blocks, about 2.4M cells, maximum level 5 (finest size 0.0625), refinement on the enthalpy gradient; smearing comes from WENO3 dissipation, level jumps "seem to not pollute the solution", and strong scaling up to 16 GPUs is comparable with §3.2 (Appendix, Figs. A.17–A.18). **Shown**

# Printed slips

- **Shock Mach number.** §3 states "a plane shock (the incident shock) at Mach 2.89" with pre-shock $\rho=1.4$, $p=1$ ($c=1$) and post-shock $\rho=5.1432014$, $p=9.0454500$, $v_1=2.0451168$ (Fig. 4). With $\gamma=1.4$ the Rankine–Hugoniot relations give $\rho=5.2544$, $p=9.5775$, $v_1=2.1200$ at Mach 2.89, and $\rho=5.1432$, $p=9.0455$, $v_1=2.0451$ at Mach 2.81: the printed state is a Mach 2.81 shock. *(compiler check, not in the sources: $\rho_2/\rho_1=(\gamma+1)M^2/((\gamma-1)M^2+2)$, $p_2/p_1=1+\tfrac{2\gamma}{\gamma+1}(M^2-1)$, $v_2=Mc_1(1-\rho_1/\rho_2)$.)*
- **Grind-time unit.** Table 1 gives $T_g$ in s with $T_g=T\,N_{\text{GPUs}}/N_{\text{cells}}$, but $1.019/3.6\times10^6=2.83\times10^{-7}$ s; the printed 0.28 is in µs per cell per GPU, the cell count being in millions. *(compiler check, not in the sources)*
- **"8 billions" (§3.2).** The cube of side 20 at $\delta_F=0.015625$ has $1280^3\approx2.10\times10^9$ cells under uniform refinement. *(compiler check, not in the sources)*
- §3.2: "$R_\delta$ increases by a factor of 32"; runs 9–13 go from $R_\delta=2$ to $32$, a factor 16.
- §3.2: cells "increase by a factor of between 4 and 5"; the Table 1 ratios are 4.5, 4.6, 5.05 and 4.18.
- §3.2, weak scaling in $N_{xyz}$: the reference is called "the strong scaling reference case" with GPUs "increased to 8 and 64", but run 4 ($8^3$) and run 7 ($16^3$) both use 8 GPUs; the eightfold progression holds only from run 1.
- Figs. 11, 14, 15 number grids #3, #4, #6, #7, which are Table 1 runs 11, 12, 7, 8; Fig. 14 and Fig. 15 give different level ranges for the same grids (e.g. grid #3: [3,6] and [4,6]).
- Eq. (7): the stage sum runs over $l=1,\dots,N_s-1$ with coefficients $a_l$, so every stage would use all stages; an explicit stage $k$ needs $l<k$ and $a_{k,l}$.
- Eq. (5) uses $h$ for both the grid spacing and the numerical flux function; Eq. (9) takes the minimum of local CFL numbers where the minimum of the admissible time steps is meant.
- Appendix vortex: Eq. (A.5) gives $v_2$ with $Y-Y_v$, as Eq. (A.4) does for $v_1$; a rotating vortex needs $X-X_v$ in $v_2$. Eq. (A.2) puts $e^{(1-r^2)/2}$ in the density, while radial equilibrium with the printed velocity amplitude $\propto r\,e^{(1-r^2)/2}$ gives $T/T_0=1-\tfrac{\gamma-1}2M_v^2e^{1-r^2}$, so the initial data are not an exact steady vortex. *(compiler check, not in the sources: $c_p\,dT/dr=v_\theta^2/r$ with $c_0^2=(\gamma-1)c_pT_0$.)*
- Appendix: "$p,\rho,u,v,w$ are the density, pressure, …" swaps $p$ and $\rho$; the Fig. A.16 caption repeats "Shock wave diffraction simulation setup"; Fig. 4(b) calls $k$ "thermal diffusivity [m²/s]" while §3.1 defines it as the thermal conductivity.
- §3.3: "experimental results of the simulated shock diffraction is not available in literature", while the set-up reproduces the Bryson & Gross experiment.
- §3.2: AMR update times of the $N_{xyz}$ runs are said to vary "around 3.5 s"; Table 1 gives 4.25 or 2.1, 2.96 and 4.3 s.
- Typos: "refinemend", "syncrhonize", "ARM grid", "entalpy", "aerodinamics" (ref. [5]).

# Notation map

| Zaghi et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\vec U=[\rho,\rho\vec v,\rho E]$ | $u=(\rho,\rho v,E)$ | the source's $E$ is specific (per unit mass); the registry's is per unit volume |
| $\vec v=(u,v,w)$ | $v=(v_1,v_2,v_3)$ | |
| $a$ | $c$ | sound speed; **$a$ is the maximum wave speed in the registry** |
| $Re$, $Pr$, $\gamma$ | $\mathrm{Re}$, $\mathrm{Pr}$, $\gamma$ | agrees |
| $h$ (spacing), $h(x)$ (Eq. 5) | $\Delta x$, $\hat f_{i\pm1/2}$ | **one symbol for two quantities** |
| $N_s$, $b_k$, $a_l$, $K_{i,k}$, $R$, $Dt$ | kept, $\mathcal L$, $\Delta t$ | Runge–Kutta stages and coefficients; the residual is $\mathcal L$ |
| $CFL_i$, $\Delta t_i$ | $\nu$, $\Delta t$ | local CFL number |
| $\phi$ | $\phi_{\mathrm d}$ (page-local) | signed distance, positive in the body; **$\phi_k$ is a volume fraction in the registry** |
| $\mathbf n=\nabla\phi/\lvert\nabla\phi\rvert$ | $n$ | normal pointing into the body |
| $\tau$ (Eq. 10), $\bar\tau$ | $\tau$ (page-local), kept | pseudo-time and viscous stress; **$\tau$ is the WENO-Z global indicator in the registry** |
| $\mathbf q$ | $u$ | solution vector of the extrapolation |
| $N_{xyz}$, $\delta_C$, $\delta_F$ ($\Delta_{coarse}$, $\Delta_{fine}$), $R_\delta$ | kept | block size, coarsest and finest cell sizes (two notations in the source), their ratio |
| $T$, $T_g$, $T_{AMR}$, $T_{TET}$ | kept | iteration time, grind time, AMR update time, total elapsed time |
| $S_{split}$, $S_{recompose}$ | kept | refinement thresholds |
| $M_0$, $M_v$, $R_v$, $X_v$, $Y_v$ | kept | vortex parameters (appendix) |

# Reference list

70 printed references in Elsevier numbered style ([1]–[70], with titles), all
merged complete into the [bibliography](/bibliography.md) with `citedby`
`zaghi-2023`. Ref. [30] prints a garbled author string ("Paul F. Fischer JWL,
Kerkemeier SG"), parsed as Fischer, Lottes and Kerkemeier; ref. [21] mixes a
corporate author (NVIDIA) with personal authors; refs. [17] and [42] print no
volume or pages; ref. [61] is kept with its year as printed. Refs. [2] (Berger
& LeVeque, AIAA 1989) and [3] (Berger & Colella, JCP 1989) share first author
and year, and the latter is the bundle's existing `berger-1989`. No printed
duplicates.

# Pages created or updated

Chunk 5 (2026-10-23), cited further in chunk 6 (2026-10-23). This source is cited on:

* [ADAM](/software/adam.md)
* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [PyFR](/software/pyfr.md)
* [Shock diffraction](/benchmarks/shock-diffraction.md)
* [STREAmS](/software/streams.md)
