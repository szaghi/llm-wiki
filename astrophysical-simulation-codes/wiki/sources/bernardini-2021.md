---
type: Source
title: "Bernardini et al. (2021) — STREAmS: A high-fidelity accelerated solver for direct numerical simulation of compressible turbulent flows"
description: "Presents STREAmS, a Cartesian finite-difference DNS solver for compressible wall turbulence (energy-preserving central flux hybridized with Lax–Friedrichs flux-split WENO under a Ducros sensor, low-storage RK3) kept in one Fortran source for CPUs and GPUs through CUDA Fortran kernels and device-resident data, with a 2.2x memory-layout speed-up on one V100, about 97% weak-scaling efficiency on 1024 V100 GPUs, and about 10x lower accuracy-matched time to solution than the flux-reconstruction code ZEFR."
resource: "doi:10.1016/j.cpc.2021.107906"
source_kind: paper
authors: [Bernardini M., Modesti D., Salvadore F., Pirozzoli S.]
year: 2021
venue: "Comput. Phys. Commun. 263:107906"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2021-CPC-Bernardini-101016jcpc2021107906.pdf"
tags: [software, gpu, cuda, performance, scaling, time-integration, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

STREAmS is a Cartesian finite-difference solver for direct numerical
simulation of the compressible Navier–Stokes equations of an ideal
heat-conducting gas, aimed at supersonic channel flow, spatially developing
boundary layers and shock-wave/turbulent boundary-layer interaction. Convective
terms combine, in locally conservative form, the energy-preserving central
flux of Pirozzoli (2010) (orders 2 to 8) with Lax–Friedrichs flux-vector
splitting and WENO reconstruction of characteristic fluxes (orders 1 to 7),
switched by a modified Ducros sensor; time stepping is a three-stage
low-storage RK3 (§2). One Fortran source serves CPU and multi-GPU builds
through CUDA Fortran `cuf` kernels, `#ifdef USE_CUDA` blocks and duplicated
host/device arrays copied only at the start and end of a run (§4.1). A
five-step memory-access optimization gives 2.2× on one V100 (§4.2);
compute–communication overlap, with or without CUDA-aware MPI, keeps weak
scaling above 97% on 1024 V100 GPUs (§4.3); an accuracy-matched comparison
with the flux-reconstruction GPU code ZEFR gives about 10× lower time and about
20× lower memory (§4.4). Merged into [STREAmS](/software/streams.md),
[GPU porting](/methods/gpu-porting.md),
[cell-update throughput](/definitions/cell-updates-per-second.md) and
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).

# Key claims

1. **Equations** (§2, eqs. 1–3). Compressible Navier–Stokes for a perfect
   heat-conducting gas; Sutherland viscosity, Prandtl number 0.72; in channel
   flow a forcing term keeps the mass-flow rate discretely constant and its
   power enters the energy equation.
2. **Central flux** (§2.1, eqs. 4–7). Locally conservative split-form flux
   built from three-factor averages of density, velocity and the transported
   quantity, weighted by the central first-derivative coefficients of order
   $2L$; it conserves total kinetic energy discretely "in the limit case of
   inviscid incompressible flow"; order 2 to 8.
3. **Shock capturing** (§2.1). Lax–Friedrichs flux-vector splitting with WENO
   reconstruction of the characteristic fluxes, order 1 to 7; the locally
   conservative form "allows straightforward hybridization".
4. **Shock sensor** (§2.1, eq. 8). Modified Ducros sensor in $[0,1]$ with fixed
   reference velocity and length scales; threshold 0.05 in the channel test
   (§3.1).
5. **Viscous terms** (§2.1, eq. 9). Laplacian form, central differences up to
   eighth order, to avoid odd–even decoupling.
6. **Time integration** (§2.2, eqs. 10–11). Three-stage third-order
   low-storage RK of Spalart, Moser & Rogers (1991).
7. **Time-step analysis** (§2.2, eqs. 12–14, Fig. 2). At unit Courant number
   the compressible explicit step is always more restrictive than the
   incompressible one, "easily exceeding an order of magnitude" at low Mach
   number.
8. **Wall-normal staggering** (§3.1). The wall sits on an intermediate node
   where convective fluxes vanish: exact mass conservation and twice the
   maximum time step.
9. **Programming model** (§4.1). Fortran 90 + MPI with a 2D pencil
   decomposition; CUDA Fortran `!$cuf kernel do(3)` kernels chosen over
   directives, CUDA C, OpenCL and HIP so that most code stays unaltered.
10. **Memory** (§4.1). Baseline and compute copies of each array; the compute
    copy is device-resident in GPU builds; copies only before and after time
    marching; `move_alloc` in CPU builds. Contrasted with AFiD (module
    aliasing) and CaNS (managed memory with prefetch hints).
11. **Explicit Euler-flux kernels** (§4.2), because the CPU routine's large
    temporaries would go to the kernel stack.
12. **Single-GPU optimization** (§4.2, Tables 1–2): see Tests.
13. **Communication** (§4.3, Fig. 12). One MPI process per GPU; host-staged or
    CUDA-aware MPI at compile time; optional overlap of interior-flux
    computation with the ghost exchange, using `cudaMemcpyAsync` in a separate
    stream when MPI is not CUDA-aware.
14. **Scaling** (§4.3, Fig. 13): see Tests.
15. **Accuracy-matched comparison with ZEFR** (§4.4, Table 3, eq. 15): see
    Tests.
16. **CPU against GPU generations** (§4.2, Fig. 11): see Tests; node against
    single card, without power or cost normalization.

# Tests

All physics tests are DNS of wall turbulence, compared graphically; there is
no shock-tube or convergence-order test.
* **Supersonic channel** (§3.1, Figs. 3–5): bulk Mach 1.5, bulk Reynolds number
  15241, friction Reynolds number 502; $6\pi\times2\times2\pi$ half-heights;
  $1032\times256\times512$. Sixth-order energy-conserving runs agree with
  earlier DNS; fourth- and sixth-order central and the hybrid run (sixth-order
  central, fifth-order WENO, threshold 0.05) are "undistinguishable"; WENO3 and
  WENO5 everywhere show "excessive numerical dissipation".
* **Supersonic boundary layer** (§3.2, Figs. 6–7): Mach 2, friction Reynolds
  number about 600, $4096\times256\times512$; characteristic non-reflecting
  boundaries, digital-filter inflow; "near collapse" with incompressible DNS
  at friction Reynolds number about 580.
* **Hypersonic boundary layer** (§3.2, Fig. 8): Mach 5.86, wall-to-recovery
  temperature 0.76, hybrid scheme, $2048\times384\times800$; "excellent
  agreement" with earlier DNS.
* **Shock-wave/boundary-layer interaction** (§3.3, Figs. 9–10): Mach 2.28, 8°
  shock generator, $4096\times384\times288$; wall pressure and streamwise
  fluctuations against the experiment of Dupont et al. (2006).
* **Single-V100 optimization** (§4.2, Tables 1–2; channel,
  energy-conserving, $360\times240\times360$). Times in ms for steps A/B/C/D/E:
  Euler-x 76/330/36/24/24; Euler-y 18/22/22/16/14; Euler-z 20/22/22/15/15;
  Viscous-I 45/54/54/11/11; Viscous-II 10/7.5/7.5/6.6/6.6; RK-I 20/5/5/5/5;
  total 656/1396/515/311/297 (factor 2.2). Load/store efficiencies (%, base to
  optimized): Euler-x 25→63/25→90, Euler-y 28→90/25→94, Euler-z 28→90/25→94,
  Viscous-I 30→86/25→97, Viscous-II 27→80/25→100, RK-I 25→54/25→100.
* **Hardware generations** (Fig. 11; same mesh; time per step): Broadwell
  node (36 cores) 2.87 s, K40 2.42 s, P100 0.66 s, Skylake node (48 cores)
  1.68 s, V100 0.3 s.
* **Weak scaling** (Fig. 13; Marconi100, 4 V100 per Power9 node, NVLink,
  NVIDIA HPC-SDK; $360\times240\times360$ per GPU; sixth-order central):
  asynchronous efficiency "about 97% on 1024 GPUs". The reader's approximate
  plot readings: synchronous time ratio up to about 1.35 at 512 GPUs and about
  1.19 at 1024; asynchronous near 1.05 throughout.
* **Strong scaling** ($512\times230\times360$ in total): above 90% at 8 GPUs,
  70% at 16; plotted speed-up at 16 GPUs about 11.7–11.9 (reader's reading).
* **ZEFR comparison** (§4.4; channel at friction Reynolds number 180, bulk
  Mach 0.2, $4\pi\times2\times2\pi$; meshes M1 = $60\times40\times60$ points
  and M2–M8 scaled by 2–8 per direction; ZEFR $15\times10\times15$ cells of
  degree 4 on M1). Error = maximum deviation of a profile over the maximum of
  the reference (eq. 15). STREAmS (fourth order) has errors at most 3% at M4;
  ZEFR needs M6 (three times the degrees of freedom). Per point or degree of
  freedom and iteration: 9.6 against 28.3 ns; 350 against 2060 bytes;
  accuracy-equivalent time 88 against 880, memory 3.2 against 64.1 ("about
  twenty-one times less"). Single GPU, memory more than 50% allocated; GPU
  model not stated.

Precision (FP32 or FP64) is not stated anywhere in the paper.

# Notation map

| Bernardini et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $p$, $T$, $\gamma$ | $\rho$, $p$, $T$, $\gamma$ | same |
| $u_i$; $u, v, w$ | $\mathbf v$ | **collision:** registry $u$ is the conserved state |
| $\mathbf w = [\rho,\rho u,\rho v,\rho w,\rho E]$ | $u$ | **collision:** paper $w$ is also the $z$-velocity |
| $\mathbf R(\mathbf w)$ | $\mathcal L(u)$ | residual of the semi-discretization |
| $E$ (per unit mass) | $E/\rho$ | **collision:** registry $E$ is an energy density |
| $H = E + p/\rho$ | words (specific total enthalpy) | registry $h$ is the cell size, $h_{\mathrm{rel}}$ relativistic |
| $c$ (sound speed) | $c_s$ | **collision:** registry $c$ is the speed of light |
| $\mu$ (dynamic viscosity) | words | **collision:** registry $\mu$ is the mean molecular weight |
| $k$, $Pr$, $c_p$, $c_v$ | words | conductivity, Prandtl number, specific heats; registry $c_p$ is the GLM damping parameter |
| $\sigma_{ij}$, $q_j$ | words | viscous stress, heat flux |
| $f$ (forcing, eq. 1b) | words | **collision:** registry $f$ is the physical flux |
| $f_x = \rho u\varphi$, $\hat f_{x,i+1/2}$ | $f$, $\hat f_{i+1/2}$ | direction subscript kept |
| $\varphi$ | words | transported quantity |
| $\Delta x$ | $h$ | uniform spacing |
| $L$ (stencil half-width) | words | order $2L$ |
| $a_l$, $b_l$ | words | first- and second-derivative coefficients |
| $\theta$ | words (Ducros sensor) | |
| $u_0$, $L_0$ | words | sensor reference scales |
| $\alpha_\ell$, $\beta_\ell$, $\ell$ | words | RK coefficients and stage; registry $\beta^i$ is the shift, $l$ the level |
| CFL | $\nu$ | unit Courant number in the analysis |
| $M_0$, $M_b$, $M_\infty$; $Re_b$, $Re_\tau$ | words | Mach and Reynolds numbers |
| $\tau_w$, $C_f$, superscript $+$ | words | **collision:** registry $\tau$ is the Valencia energy or optical depth |
| $h$ (channel half-height) | words | **collision:** registry $h$ is the cell size |
| $N_x$, $N_y$, $N_z$ | $N$ per direction | extends the registry $N$ |
| ETP, MPP, ENP | words | ns per point per iteration; bytes per point; equivalent points |

# Pages created or updated

* Created [STREAmS](/software/streams.md).
* Created [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md),
  [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* Also cited on [GAMER](/software/gamer.md) and
  [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* Also cited on (batch 3) [Adaptive mesh refinement in astrophysical codes](/methods/adaptive-mesh-refinement.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2021-CPC-Bernardini-101016jcpc2021107906.pdf`.
   * **Version.** The published journal version (Elsevier typeset, 14 pages,
     © 2021 Elsevier), not a preprint. Code: STREAmS, GPLv3,
     `https://github.com/matteobernardini/STREAmS`, CPC Library
     doi:10.17632/hdcgjpzr3y.1 and a Code Ocean capsule; no version number
     printed.
   * **Identity.** doi:10.1016/j.cpc.2021.107906, printed on page 1 and
     checked on Crossref: Comput. Phys. Commun. 263, article 107906, issued
     2021-06; the four authors as on page 1; 63 references. Received 21 Aug
     2020, online 20 Feb 2021.
   * **How it was read.** Text extraction, all sections; eqs. 8–9 checked on
     the rendered page 3. Figure values beyond the quoted 97%, above 90% and
     70% are approximate readings from plots.
   * **Recorded as printed.**
     - Eq. 8: the third term under the square root is printed as the
       reference velocity squared over the reference length, not
       dimensionally consistent with the other two (presumably the square of
       their ratio); not corrected.
     - Eq. 9: the first sum carries $a_l^2$ for the product of two
       first-derivative stencils, unexplained; not reinterpreted.
     - Eq. 11: the first RK coefficient set is printed $(0, 17/60, -5/12)$;
       the standard scheme has $-17/60$, and with the printed sign the
       weights sum to $94/60$. Not checked against Spalart et al. (1991).
     - Fig. 13(b): the upper axis (4.24 to 0.26 million points per GPU from 1
       to 16 GPUs) is a factor 10 below the stated $512\times230\times360$
       mesh (42.4 million points); the stated per-GPU optimum of "about
       500,000" matches the axis, not the mesh, and is unreliable.
     - Friction Reynolds number of the channel: 502 (text), 490 (Fig. 3
       caption), 500 (Fig. 4 caption); hypersonic boundary layer 268 at the
       inlet (text) and 436 (Fig. 8 caption, presumably another station).
     - Units of Table 3's equivalent time and memory are not printed.
   * **Reference list:** 63 entries (Crossref 63), journal titles not
     printed. Same-author-year suffixes follow printed order:
     `pirozzoli-2011` [24], `-b` [25], `-c` [28], `-d` [46];
     `pirozzoli-2010` [27], `-b` [34]; `bernardini-2014` [30], `-b` [61].
     [21] is printed "M.D. Renzo" (presumably Di Renzo), keyed `renzo-2020`
     for the merge to check; DOIs entered only where printed ([10], [30]).
