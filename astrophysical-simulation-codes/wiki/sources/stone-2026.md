---
type: Source
title: "Stone et al. (2026) — AthenaK: A Performance-Portable Version of the Athena++ AMR Framework"
description: "Method paper of AthenaK, a Kokkos reimplementation of the Athena++ block-based AMR framework with device-resident data and MeshBlockPacks, documenting Newtonian, SR and GR (M)HD, two-fluid MHD, GR radiation and particles, with 1077 Mzone-cycles/s per Grace Hopper device for 3D hydro and 80% weak-scaling efficiency on 65,536 Frontier GCDs."
resource: "doi:10.3847/1538-4365/ae3717"
source_kind: paper
authors: [Stone J.M., Mullen P.D., Fielding D., Grete P., Guo M., Kempski P., Most E.R., White C.J., Wong G.N.]
year: 2026
venue: "Astrophys. J. Suppl. 283:27"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2024-arXiv-Stone-1048550arXiv240916053.pdf"
tags: [software, mhd, hydro, amr, gpu, kokkos, performance-portability, relativity, constrained-transport, riemann-solver, time-integration, performance, scaling, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

AthenaK is a from-scratch reimplementation of the
[Athena++](/software/athena-plus-plus.md) block-based AMR framework
(MeshBlocks in a binary tree, quadtree or octree, Z-ordering, flux
correction at level boundaries, one global time step, task lists) on the
Kokkos C++ performance-portability library, so that one source runs on
CPUs and on NVIDIA, AMD and ARM hardware (abstract, §1–§2). The
GPU-specific changes are the MeshBlockPack (all MeshBlocks of a device in
one aggregate, one kernel launch), Kokkos Views with a MeshBlock index that
keep all field data on the device, a host-side tree with DualViews,
device-side ghost packing with point-to-point MPI of device buffers,
templated algorithm options against register spilling, and Cartesian
coordinates only (§2). The solvers cover Newtonian, SR and GR hydro and
MHD (method of lines with SSP-RK1–RK4; PLM, PPM4, PPMX, WENOZ on
primitives; LLF, HLLE, HLLC, HLLD, Roe; upwind CT; first-order flux
correction; the Kastaun et al. inversion), explicit diffusion, two-fluid
ion–neutral MHD with IMEX, gray GR radiation on a discrete angular grid,
and tracer and charged particles (§3–§4). One Grace Hopper device reaches
1077 Mzone-cycles/s for 3D hydro (Table 1), and weak scaling holds about
80% efficiency on 65,536 MI250X GCDs of Frontier (§5.2). Merged into
[AthenaK](/software/athenak.md).

# Key claims

1. **Programming model** (§1–§2). Kokkos templates abstract memory spaces,
   execution spaces and execution policies. The framework was rewritten,
   not ported, but "very little of the overall design was changed".
2. **MeshBlockPack** (§2): one aggregate of all MeshBlocks per device
   "reduces the number of kernel launches and greatly enhances performance
   when there are a large number of small MeshBlocks on the same device."
3. **Residency** (§2): data are "always stored on the device, and is never
   moved to the host except for outputs"; the tree lives on the host;
   physics always runs on the device.
4. **Communication** (§2): ghost cells loaded in device kernels into device
   buffers sent by point-to-point MPI; prolongation and restriction in
   device kernels; infrastructure "largely re-designed" from Athena++.
   GPU-aware MPI is not stated.
5. **Cartesian only** (§2), partly because virtual functions and
   polymorphism "are not supported by the compilers currently available on
   many GPUs"; no 2D axisymmetric runs.
6. **Templating** (§2) of options such as Riemann solvers "reduces register
   spillage and can greatly improve performance."
7. **Solvers** (§3): reconstruction on primitives only (characteristic
   "not yet been implemented"); LLF, HLLE, HLLC, HLLD, Roe; Ketcheson
   (2010) low-storage SSP-RK1–RK4 with $\Delta t$ from the minimum over
   cells and directions (eq. 3) and "Generally we use CFL ≤ 1/Ndim"; no
   CTU; IMEX for stiff sources; Evans–Hawley CT with Gardiner–Stone upwind
   EMFs.
8. **FOFC** (§3): after Lemaster & Stone (2009), fluxes of a cell that
   would turn negative in density or pressure are recomputed with
   piecewise-constant states and LLF, before the AMR flux correction; it
   "significantly reduces the need for floors" in GRMHD accretion.
9. **Diffusion** (§3.3, eqs. 6–10): explicit, in every Runge–Kutta stage;
   super-time-stepping and implicit solvers "have not been ported from
   Athena++".
10. **Relativity** (§3.5–§3.6): the [Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md)
    inversion "in a departure from Athena++"; GR in Cartesian Kerr–Schild
    or Minkowski only, so "our algorithm does not conserve angular
    momentum to machine precision as HARM".
11. **GR radiation** (§3.7): gray specific-intensity transport on a geodesic
    angular grid (White et al. 2023), operator-split implicit source.
12. **Particles** (§4): Lagrangian Monte Carlo tracers and charged test
    particles; migration by gather–scatter plus non-blocking sends.
13. **Performance** (§5.1, Tables 1–2): per-device throughput from 11
    (Apple M1 pro, MHD) to 1077 (Grace Hopper, hydro) Mzone-cycles/s; MHD
    about 2× hydro; precision and solver configuration not stated.
14. **Block size on GPU** (§5.1): on an A100, 614, 413, 242 and 126
    Mzone-cycles/s for $128^3$, $64^3$, $32^3$ and $16^3$ MeshBlocks.
15. **AMR on GPU** (§5.1, Fig. 20): ≈20% overhead, AMR run 5.4× faster than
    uniform for the same 2D MHD blast.
16. **Weak scaling** (§5.2, Figs. 21–22): ≈70% at 4096 A100s (Perlmutter);
    80% at 65,536 MI250X GCDs (Frontier); AMR weak scaling "nearly
    perfect" with fixed $32^3$ blocks to 4096 GCDs.
17. **Positioning** (§1, §6): "a much smaller and simpler project" than
    Parthenon; most Athena++ features "will not be implemented in AthenaK
    anytime soon"; planned: fourth-order integrator, multigrid self-gravity
    on AMR, non-relativistic radiation and neutrino transport.

**Tests.** Verification mostly on one CPU core, plots only (no tabulated
errors): 1D hydro and MHD [linear waves](/benchmarks/linear-wave-convergence.md)
(fourth order with PPMX/WENOZ + RK3, except the MHD fast wave, second
order; §3.1–§3.2, Figs. 1, 3); Shu–Osher, 200 cells (Fig. 1);
[Brio–Wu](/benchmarks/brio-wu-shock-tube.md), 200 cells, "small amplitude
ringing near the compound wave" (Fig. 3); Gaussian viscous diffusion,
second order (Fig. 5); two-fluid relaxation and steady C-shock (Fig. 7);
SRMHD shock tube with AMR (Fig. 9); Komissarov cylindrical explosions
(Fig. 10); GR Bondi accretion, second order (Fig. 12); Blandford–Znajek
monopole (Fig. 13); EHT SANE torus comparison (Fig. 14);
radiation-modified linear wave and a beam in Schwarzschild (Figs. 15–16);
tracers in Kelvin–Helmholtz (Fig. 18); a 2D
[MHD blast wave](/benchmarks/mhd-blast-wave.md), uniform against AMR on one
A100 (Fig. 20). Performance: Tables 1–2, Figs. 20–22. Details on
[AthenaK](/software/athenak.md).

# Notation map

| Stone et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F$, $S$ (eq. 1) | $u$, $\mathbf f(u)$, $s(u)$ | |
| $W$ (primitive vector) | words | **collision:** registry $W$ is the Lorentz factor |
| $\rho$, $\mathbf v$, $p_g$, $E$ | $\rho$, $\mathbf v$, $p$, $E$ | |
| $u_g$ | $\rho e$ | internal energy density; **collision** with the conserved state $u$ |
| $\gamma$ | $\gamma$ | |
| $C$ (isothermal sound speed) | words | registry $c_s$ is adiabatic |
| $p^* = p_g + p_m$ | $P^*$ | |
| $p_m$ | words | magnetic pressure |
| $B$ | $\mathbf B$ | Heaviside–Lorentz; the C-shock test prints $B_y/\sqrt{4\pi}$ (Gaussian) |
| $E$ (electric field, eq. 2) | $\boldsymbol{\mathcal E}$ | **collision** with total energy $E$ |
| $J = \nabla\times B$ | $\mathbf J$ | |
| $\eta$, $\nu$, $\kappa$, $D_i$ | words | resistivity, viscosity, conductivity, diffusion coefficient; **collisions** with $\eta_1,\eta_2$, the Courant number $\nu$, the opacity $\kappa$ and the Valencia $D$ |
| CFL, CFL$_{\mathrm{diff}}$ | $\nu$; words | eq. 3: minimum over cells and directions |
| $\lambda_{\max,i}$ | $\max_p\vert\lambda^{(p)}\vert$ in direction $i$ | |
| $\Delta x_i$ | $h$ | |
| $N_{\mathrm{dim}}$ | $d$ | |
| $N$ (resolution) | $N$ | |
| MeshBlock size | $N_{\mathrm b}$ | |
| $\alpha$ (drag coefficient, lapse, absorptivity) | words; $\alpha_{\mathrm L}$ for the lapse | **collision:** the paper reuses $\alpha$ three ways |
| $\rho_i$, $\rho_n$, $v_i$, $v_n$ | words | ion and neutral fluids; **collision** with species densities $n_i$ |
| $D$, $M$, $E - D$ (eq. 12) | $D$, $S_i$, $\tau$ | |
| $\Gamma$ (Lorentz factor) | $W$ | |
| $u^\mu$, $\tilde u^i$ | words | four-velocity and normal-frame velocity; **collision** with $u$ |
| $\beta^i$; $\beta$ (plasma beta) | $\beta^i$; words | **collision** |
| $\sigma = b^2/\rho$ | words | magnetization; also a Gaussian width in §3.3, §4.1 |
| $a$ (black-hole spin) | words | **collision:** registry $a$ is the scale factor |
| $M$ | $M_{\mathrm{BH}}$ | units $G = c = 1$ |
| $\psi$, $\zeta$ (angles) | words | **collision:** $\psi$ is the GLM scalar |
| $R^{\mu\nu}$ | related to $E_{\mathrm r}$, $\mathbf F_{\mathrm r}$, $\mathsf P_{\mathrm r}$ | coordinate-frame radiation tensor |
| Mzcps, Mzc/s | words | $10^6$ cell updates per second |

# Pages created or updated

* [AthenaK](/software/athenak.md) (created).
* [Athena++](/software/athena-plus-plus.md), [Super-time-stepping](/methods/super-time-stepping.md).
* [Constrained transport](/methods/constrained-transport.md), [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md), [Primitive-variable recovery](/methods/primitive-variable-recovery.md), [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md).
* [GAMER](/software/gamer.md), [Athena](/software/athena.md), [CASTRO](/software/castro.md), [Cholla](/software/cholla.md).
* [GLM divergence cleaning](/methods/glm-divergence-cleaning.md).
* [Cell-update throughput](/definitions/cell-updates-per-second.md), [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md), [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), [MHD blast wave](/benchmarks/mhd-blast-wave.md), [Shu–Osher shock tube](/benchmarks/shu-osher-shock-tube.md), [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md), [Ambipolar C-shock](/benchmarks/ambipolar-c-shock.md).
* Also cited on (batch 4) [Magnetized Fishbone–Moncrief torus](/benchmarks/magnetized-torus-accretion.md), [Density and pressure floors](/methods/numerical-floors.md), [EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md), [H-AMR](/software/h-amr.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2024-arXiv-Stone-1048550arXiv240916053.pdf`.
   * **Version.** arXiv:2409.16053v1 [astro-ph.IM], 24 Sep 2024 ("Draft
     version September 25, 2024", AASTeX63, 29 pages), **not** the journal
     version. No code version or commit and no Kokkos version are printed.
   * **Identity.** The arXiv DOI 10.48550/arXiv.2409.16053 is a DataCite
     DOI (Crossref returns 404); DataCite resolves it to this title, 2024,
     version 1. The published version was found on Crossref by title:
     doi:10.3847/1538-4365/ae3717, Astrophys. J. Suppl. 283(1), article 27,
     online 2026-02-26, print 2026-03-01, same nine authors in the same
     order, titled "AthenaK: A Performance-portable Version of the Athena++
     Adaptive Mesh Refinement Framework". The slug follows the issue year
     (2026), not the preprint year; the bundle law records the change.
   * **How it was read.** Text extraction of all sections; eq. 27 checked
     on rendered page 16 and Fig. 21 read from rendered page 25 (values
     approximate). Eqs. 12–18 and 20–26 read from the text layer only and
     not reproduced.
   * **Recorded as printed.** The text calls Fig. 9 a relativistic MHD
     "blast wave test" of Athena++ §4.3.1, while the caption calls it an
     "SRMHD shock tube test", and the text refers to "Figure 37 in S08",
     although Athena (S08) has no relativistic MHD. The text and caption of
     Fig. 5 swap its panels. The Fig. 6 caption calls the MRI run
     "axisymmetric", against §2 ("2D axisymmetric calculations are not
     possible with AthenaK"). Table 1 says "AMD MI250", §5.2 "AMD MI250X".
     Figs. 21–22 label the axis "Total performance (Mzcps)" but the
     single-device values match Table 1 only in cell updates per second.
     The text gives "roughly 70% on 4096 GPUs" (Perlmutter) and 80%
     (Frontier); the plotted curves end near $10^3$ GPUs at about
     0.63–0.68 and at about 0.74–0.77. The AMR overhead is "roughly 20%"
     (22% from 181 → 141) and the speed-up "5.4×" (1/0.18 = 5.6). The
     C-shock coupling length is printed as $10^4$; the drag citation as
     "Pareshi & Russo (2005)"; the driving spectrum as "peaking at
     $2\pi k = 2L_{\mathrm{box}}$".
   * **Reference list:** 86 entries in v1 (AAS style, no titles, DOIs for
     most); Crossref lists 91 for the journal version, so the published
     list differs and the bibliography records v1. Guo (2024) is printed
     as "Guo, M. e. a. 2024" with no venue; seven entries are arXiv-only.
     The ingested [Stone et al. (2008)](/sources/stone-2008.md),
     [Stone et al. (2020)](/sources/stone-2020.md),
     [Mignone et al. (2012)](/sources/mignone-2012.md),
     [Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md) and
     [Tomida & Stone (2023)](/sources/tomida-2023.md) are cited.
     [Rossazza et al. (2026)](/sources/rossazza-2026.md) cite this
     paper's preprint as arXiv 2024; that entry is merged into
     `stone-2026`.
