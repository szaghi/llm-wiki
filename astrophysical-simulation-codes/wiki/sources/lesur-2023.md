---
type: Source
title: "Lesur et al. (2023) — IDEFIX: a versatile performance-portable Godunov code for astrophysical flows"
description: "Method paper of IDEFIX, a Kokkos C++ finite-volume Godunov code for non-relativistic HD and MHD with PLUTO-compatible inputs, vector-potential-capable constrained transport, RKL2 super-time-stepping, non-ideal MHD and orbital advection on non-AMR curvilinear grids, run fully on the device, with 1240 Mcell/s per MI250X node and above 95% weak-scaling efficiency on 1024 GPUs."
resource: "doi:10.1051/0004-6361/202346005"
source_kind: paper
authors: [Lesur G.R.J., Baghdadi S., Wafflard-Fernandez G., Mauxion J., Robert C.M.T., Van den Bossche M.]
year: 2023
venue: "Astron. Astrophys. 677:A9"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2023-A&A-Lesur-10105100046361202346005.pdf"
tags: [software, mhd, hydro, gpu, kokkos, performance-portability, constrained-transport, riemann-solver, time-integration, performance, scaling, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

IDEFIX is a new C++ finite-volume Godunov code for non-relativistic HD and
MHD, written from scratch rather than by porting
[PLUTO](/software/pluto.md), on the Kokkos library, so that one source
compiles for CPUs and NVIDIA and AMD GPUs (§1, §3.1). Its algorithm
reconstructs primitive variables (flat, PLM, LimO3, PPM), solves Rusanov,
HLL, HLLC, HLLD or Roe Riemann problems, evolves face-centred fields by
constrained transport with an optional vector-potential form, integrates
by method-of-lines Euler, RK2 or RK3, super-time-steps parabolic terms by
RKL2, and carries Ohmic, ambipolar and Hall terms and conservative
FARGO-type orbital advection on Cartesian, cylindrical and spherical
stretched grids without AMR (§2). All data and loops live on the device;
the host does I/O, initial conditions and exception handling; MPI packs on
the device and exchanges ghosts dimension by dimension (§3). Thirteen
standard tests validate it (§4), and it reaches 1240 Mcell/s per 4×MI250X
node and $3\times10^{11}$ cell/s on 1024 GPUs at above 95% weak-scaling
efficiency (§5). Merged into [IDEFIX](/software/idefix.md) and
[super-time-stepping](/methods/super-time-stepping.md).

# Key claims

1. **Equations** (§2.1, eqs. 1–4): dimensionless non-relativistic MHD with
   viscosity, thermal diffusion, Ohmic, Hall and ambipolar terms,
   $\mathbf J = \nabla\times\mathbf B$ without $4\pi$.
2. **Pressure in the flux** (§2.3): unlike PLUTO, which treats pressure
   gradients as a momentum source, so results "are expected to differ,
   even if the same algorithm combination is chosen" in curvilinear
   geometry.
3. **Reconstruction** (§2.3) of primitives without characteristic
   decomposition; LimO3 "up to 4th order", PPM "4th order accurate on
   regularly spaced grids", but the code is "at most globally second
   order" (footnote 1).
4. **Riemann solvers** (§2.3): Rusanov, HLL, HLLC/HLLD, Roe, run-time
   selectable.
5. **Vector-potential CT** (§2.4, eqs. 6–8): "mathematically equivalent to
   the original CT algorithm" but prevents round-off accumulation in
   $\nabla\cdot\mathbf B$; costs memory and may overflow under a constant
   large-scale EMF (periodic gauge transformation).
6. **EMFs** (§2.4): arithmetic, $\boldsymbol{\mathcal E}^0$,
   $\boldsymbol{\mathcal E}^c$ (default, "similar to Athena"), 2D HLL and
   HLLD Riemann EMFs.
7. **Hall MHD** (§2.5, §4.3): whistler speed in the HLL fan for the field
   fluxes only, arithmetic Hall EMF; HLL is "our only solver compatible
   with the Hall effect".
8. **Integrator** (§2.7, eq. 9, Table 1): Euler, RK2, RK3 (Gottlieb & Shu
   1998) as a method of lines.
9. **Time step** (§2.7, eq. 10): point-wise sum of hyperbolic and parabolic
   rates, Courant number below 1, no dimension prefactor; equal to the
   number of dimensions times PLUTO's Courant number, and "somewhat
   larger" than PLUTO's step.
10. **RKL** (§2.8, eqs. 11–13): RKL2 for viscosity, conduction, Ohmic and
    ambipolar diffusion; stage count about twice the square root of the
    hyperbolic-to-parabolic step ratio; stated round-off growth of
    $\nabla\cdot\mathbf B$ as the square root of the cycle count with
    explicit integration and linearly with RKL.
11. **Orbital advection** (§2.9): conservative scheme of Mignone et al.
    (2012, A&A 545:152), fully parallel in 3D.
12. **Grids** (§2.6): Cartesian, polar/cylindrical, spherical, stretched;
    no AMR; angular momentum conserved to machine precision.
13. **Kokkos design** (§3.1): `IdefixArrayND` (Kokkos Views, after
    K-Athena) and `idefix_for`; the algorithm runs "exclusively on the
    device".
14. **MPI** (§3.4): device-side packing, persistent communications,
    CUDA-aware MPI; sequential per-dimension exchange measured "generally
    faster, especially on NVidia GPUs" than Athena++'s 26-neighbour
    exchange; unsuitable for AMR.
15. **PLUTO compatibility** (§3.2–§3.3): same input format, keywords,
    variable names, several macros and VTK conventions.
16. **Performance** (§5, Tables 3–4): double precision, 3D Orszag–Tang,
    HLLD + PLM + $\boldsymbol{\mathcal E}^c$ + RK2; per node 41.3 (2×EPYC
    7H12), 25.0 (2×Cascade Lake 6248), 484 (4×V100) and 1240 (4×MI250X)
    Mcell/s; node-to-node speed-ups 19.3 and 49.6 against the Cascade Lake
    node; TDP-based energy efficiency up to 6× the CPUs at $256^3$ cells
    per GPU.
17. **Weak scaling** (§5, Fig. 18): above 80% to 131 072 Rome cores, "very
    close to Pluto's"; above 80% to 512 V100; above 95% to 1024 MI250X;
    about $3\times10^{11}$ cell/s peak.
18. **Related codes** (§6): K-Athena "quantitatively similar"; Parthenon
    "similar to Idefix" in hydro and has AMR.

**Tests** (§4). Visual unless noted:
[Sod](/benchmarks/sod-shock-tube.md) (500 points, Roe + PLM + RK2);
[double Mach reflection](/benchmarks/double-mach-reflection.md)
($1920\times480$); [Sedov–Taylor](/benchmarks/sedov-taylor-blast-wave.md)
in Cartesian $512^3$ and spherical $256\times256\times512$ across the axis;
[Brio–Wu](/benchmarks/brio-wu-shock-tube.md) with $\gamma = 5/3$ against
PLUTO 4.3; oblique MHD [linear waves](/benchmarks/linear-wave-convergence.md)
(quantitative: second order for four solvers with PLM; PPM stalls at high
resolution, also in Athena++ with primitive reconstruction; LimO3
recommended); magnetized rotor in Cartesian and polar grids;
[Orszag–Tang](/benchmarks/orszag-tang-vortex.md) with
$\vert\nabla\cdot\mathbf B\vert \ll 10^{-12}$; planet–disc interaction
against FARGO3D; ambipolar C-shock (quantitative: error below 2% at 2
points per ambipolar length; RKL2 at about 10% of the explicit time); a
Hall-dominated shock (quantitative: slightly below second order); hydro and
MHD shearing waves. A 3D Orszag–Tang variant is the performance workload
(§5).

# Notation map

| Lesur et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F$, $S$ | $u$, $\mathbf f(u)$, $s(u)$ | |
| $\rho$, $v$, $E$ | $\rho$, $\mathbf v$, $E$ | |
| $P$ | $p$ | |
| $\mathcal P \equiv P + B^2/2$ | $P^*$ | |
| $e$ | $\rho e$ | **collision:** the paper's $e$ is internal energy per volume |
| $\psi$ (gravitational potential) | $\Phi$ | **collision:** registry $\psi$ is the GLM scalar |
| $\psi_p$ (planet potential) | words | point-mass Plummer potential, not a Poisson solution |
| $\eta_1$, $\eta_2$ (viscosities) | words | **collision:** registry $\eta_1$, $\eta_2$ are dual-energy thresholds |
| $\Pi$ | words | viscous stress tensor |
| $\kappa$ | words | **collision:** thermal diffusion coefficient, registry $\kappa$ is the opacity |
| $\eta_O$, $x_H$, $x_{AD}$, $\eta_{AD}$ | words | Ohmic, Hall and ambipolar coefficients |
| $J$ | $\mathbf J$ | no $4\pi$ |
| $\mathcal E$, $\mathcal E^0$, $\mathcal E^c$ | $\boldsymbol{\mathcal E}$, $\boldsymbol{\mathcal E}^0$, $\boldsymbol{\mathcal E}^c$ | edge EMFs; Gardiner–Stone variant names kept |
| $A$ (vector potential) | words | **collision:** registry $A(u)$ is the flux Jacobian |
| $c_s$ (§4.2, slow speed; §4.3, sound speed) | words; $c_s$ | **collision** in §4.2 |
| $v_A$ | $c_A$ | |
| $dt$, $dt_{\rm hyp}$, $dt_{\rm par}$ | $\Delta t$, $\Delta t_{\mathrm{hyp}}$, $\Delta t_{\mathrm{par}}$ | subscripted steps proposed for the registry |
| $s_{\rm RKL}$ | $s_{\mathrm{RKL}}$ | RKL stage count, proposed for the registry |
| $\sigma_{\rm CFL}$ | $\nu$ | IDEFIX definition, no dimension prefactor |
| $C_{a,\rm PLUTO}$ | $\nu$ (PLUTO definition) | $\sigma_{\rm CFL} = D\,C_{a,\rm PLUTO}$ |
| $D$ (dimensions) | $d$ | |
| $d$ (direction index), $d\ell_d$ | words, $h$ | **collision:** registry $d$ is the number of dimensions |
| $n$ (cycle index) | $n$ | time level |
| $U_s$, $U^*$, $\mathcal S_{dt}$, $w_s$, $w_s^0$ | words | stage states and weights; $\mathcal S_{dt}$ is a full Euler step $u + \Delta t\,\mathcal L(u)$ plus CT |
| $U$ (orbital velocity), $\delta v$ | words | **collision** with the conserved state |
| $q$, $a$ (planet mass ratio, smoothing length) | words | **collision:** registry $a$ is the scale factor |
| $N$ (in $2N\times N\times N$) | $N$ | |
| $\epsilon$, $\Omega$, $A_R$, $n_R$, $n_\phi$, $n_z$, $M$, $A$, $L$ | words | test parameters |

# Pages created or updated

* [IDEFIX](/software/idefix.md) and [Super-time-stepping](/methods/super-time-stepping.md) (created).
* [Athena++](/software/athena-plus-plus.md), [PLUTO](/software/pluto.md), [GAMER](/software/gamer.md), [Athena](/software/athena.md).
* [GLM divergence cleaning](/methods/glm-divergence-cleaning.md).
* [Constrained transport](/methods/constrained-transport.md), [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md), [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md).
* [Cell-update throughput](/definitions/cell-updates-per-second.md), [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* [Sod shock tube](/benchmarks/sod-shock-tube.md), [Double Mach reflection](/benchmarks/double-mach-reflection.md), [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), [Linear wave convergence](/benchmarks/linear-wave-convergence.md), [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), [Ambipolar C-shock](/benchmarks/ambipolar-c-shock.md), [Relativistic magnetic rotor](/benchmarks/relativistic-magnetic-rotor.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2023-A&A-Lesur-10105100046361202346005.pdf`.
   * **Version.** arXiv:2304.13746v1 [astro-ph.IM], 26 Apr 2023, an A&A
     preprint ("A&A proofs: manuscript no. idefix", April 28, 2023; 18
     pages), not the journal version. Its "Received September 15, 1996;
     accepted March 16, 1997" line is the unedited A&A template. No code
     version is printed.
   * **Identity.** The DOI is not printed in the arXiv PDF; doi:10.1051/0004-6361/202346005
     (from the filename) checked on Crossref: "IDEFIX: A versatile
     performance-portable Godunov code for astrophysical flows", Astron.
     Astrophys. 677, article A9, online 2023-08-25, issue 2023-09, same six
     authors in the same order.
   * **How it was read.** Text extraction of all sections; eqs. 1–4, 9–14
     and Table 1, garbled in the text layer, read from rendered pages 2, 4,
     5 and 7.
   * **Recorded as printed.** The Sod test prints a left pressure of 0.1;
     Fig. 2 shows the standard 1.0. The Orszag–Tang resolution is "$128^3$,
     plus a reference case at $512^3$" in the text but $128^2$ and $1024^2$
     in Figs. 10–11. For linear waves, the text says LimO3 shows "proper
     second order convergence", the Fig. 8 caption "slightly larger than
     second order". The Brio–Wu states are not
     printed (deferred to Mignone et al. 2007), so the $\gamma = 5/3$ choice
     cannot be checked here. The text says "Mi250", Table 3 "Mi250X", and
     the interconnect is called "AMD Slingshot". `IdefixArrayND` is
     described with "1 < N < 4" though `IdefixArray1D` is used. Footnote 6
     reports a typo in González-Morales et al. (2018) eq. 50a. The
     Sedov injection radius is not printed.
   * **Reference list:** 58 entries (A&A style, titles mostly absent). The
     printed "Mignone et al. 2012" is the A&A orbital-advection paper
     (A&A 545:152), merged as `mignone-2012-b`, not the ingested
     [Mignone et al. (2012)](/sources/mignone-2012.md). Stone et al. (2020)
     is printed "ApJ, 249, 4" (it is the ApJS paper,
     [Stone et al. (2020)](/sources/stone-2020.md)); Masset (2000) is
     printed "A&A, 141, 165" (A&A Suppl. Ser.). K-Athena (Grete et al.
     2021) and Parthenon (Grete et al. 2023) are cited but not ingested.
