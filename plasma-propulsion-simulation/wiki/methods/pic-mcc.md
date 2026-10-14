---
type: Method
title: "Particle-in-cell with Monte Carlo collisions (PIC-MCC)"
description: "Kinetic plasma simulation in which macroparticles are pushed in grid fields that their own deposited charge determines, with collisions applied stochastically between pushes; used fully kinetically (electrons and ions as particles) or for heavy species only, in 1D to 3D thruster geometries."
status: established
aliases: [PIC, PIC/MCC, particle-in-cell, explicit electrostatic PIC, fully kinetic PIC]
tags: [pic, mcc, kinetic, hall-thruster, numerics, software]
timestamp: 2026-10-14T00:00:00Z
---

# Particle-in-cell with Monte Carlo collisions (PIC-MCC)

PIC-MCC represents each species by macroparticles, computes the fields on a
grid from the charge the particles deposit, and advances the particles in
those fields; collisions are applied between pushes by a Monte Carlo step
([Taccogna et al. (2023)](/sources/taccogna-2023.md), §II, Fig. 1). In
electric-propulsion modelling it is used in two forms: *fully kinetic*, with
electrons and ions as particles and a Poisson field solve, and
*heavy-species-only*, with ions (and neutrals) as particles and electrons
treated as a fluid or by a prescribed relation (see
[hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md)). The
collision step is described on
[Monte Carlo collisions](/methods/monte-carlo-collisions.md); the grid and
time-step limits on
[resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md).

## The explicit electrostatic cycle

Taccogna et al. (2023, §II, Eqs. 1–6, Fig. 1) give the cycle that the
fully kinetic codes of this bundle share:

1. **Macroparticle representation** (Eq. 1). The distribution function of
   species $s$ is a sum over its $N$ macroparticles,
   $$f_s(\mathbf x,\mathbf v,t)=\sum_{p=1}^{N}W_p\,S(\mathbf x-\mathbf x_p)\,\delta(\mathbf v-\mathbf v_p),$$
   where $W_p$ is the macroparticle weight and $S$ the particle shape,
   normalized to unit integral. A uniform weight per species is common.
   The function that assigns a particle to the grid nodes is $S$
   convolved with a top-hat of one mesh width.
2. **Deposition** (Eq. 5). Charge density and current density at each node
   are sums over particles of $q_sW_p$ (times $\mathbf v_p$ for the
   current) weighted by the assignment function, divided by the cell
   volume.
3. **Field solve** (Eq. 6). Poisson's equation for $\phi$ in electrostatic
   codes; dielectric boundaries are handled by a capacitor-like surface
   condition (Eq. 7) or by a generalized Poisson equation solved through the
   dielectric (Eq. 8).
4. **Gather and push** (Eqs. 2–3). Grid fields are interpolated to the
   particle and the Newton–Lorentz equations
   $$m_s\frac{d\mathbf v_p}{dt}=q_s(\mathbf E+\mathbf v_p\times\mathbf B),\qquad \frac{d\mathbf x_p}{dt}=\mathbf v_p$$
   are advanced, with leapfrog "the most diffuse" choice (see
   [particle pushers](/methods/particle-pushers.md)).
5. **Collisions** (Eq. 4), by [MCC or DSMC](/methods/monte-carlo-collisions.md).

The codes in this bundle implement the same loop: Cartesian cloud-in-cell
(linear) weighting with a leapfrog–Boris push
([Reza et al. (2022)](/sources/reza-2022.md), §2;
[Troyetsky et al. (2026)](/sources/troyetsky-2026.md), PIC-MCC model
section); a Boris push with a centred-difference field
([Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Eq. 6); and in
[WarpX](/software/warpx.md) a relativistic Boris push with the
energy-conserving gather of Lewis (1970) on a staggered grid, gather and
push fused into one GPU kernel, linear shape functions, field solve in
double and particles in single precision
([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods).

Field solvers named by the review are finite-difference or finite-volume
discretizations, sometimes with AMR, with direct (PARDISO, MUMPS) or
iterative (PETSc, preferred in 3D) linear solvers (Taccogna et al. 2023,
§III A); [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md) (App. 3)
list HYPRE, FISHPACK, SuperLU, PETSc and WSMP. Troyetsky et al. (2026) use
HYPRE GMRES with a PFMG preconditioner; WarpX uses geometric multigrid,
warm-started from the previous step (Marks & Gorodetsky 2025, Methods);
Reza et al. (2022, §2) solve two 1D Poisson problems by the Thomas
algorithm in their [reduced-order scheme](/methods/reduced-order-pic.md).

## Fully kinetic and heavy-species-only variants

**Fully kinetic.** Electrons and singly charged ions are macroparticles in
the axial–azimuthal runs of [Charoy et al. (2020)](/sources/charoy-2020.md)
(§II A), Marks & Gorodetsky (2025) and
[Miranda et al. (2026)](/sources/miranda-2026.md) (§2.1), in the
axial–radial run of Troyetsky et al. (2026), and in all planes of Reza et
al. (2022). Neutrals are then either an imposed background — a 1D Euler
solution (Charoy et al. 2020, §V, Eq. 30), a $\tanh$ axial profile
(Miranda et al. 2026, eq. 2), a quasi-steady 1D depletion law chosen to
suppress the [breathing mode](/definitions/breathing-mode.md) (Troyetsky
et al. 2026, Eqs. 42–43), a fixed density (Reza et al. 2022, §4.2) — or
macroparticles too (Reza et al. 2022, §5.1; Muñoz Tejeda et al. 2025,
where electrons, ions and neutrals are all pushed). Where ionization is
replaced by an imposed source of electron–ion pairs (Charoy et al. 2020;
Marks & Gorodetsky 2025; Reza et al. 2022, §3), the breathing mode and
probably ion transit-time oscillations are excluded (Charoy et al. 2020,
p. 10).

**Heavy species only.** In the standard electric-propulsion hybrid that
[Boyd (2005)](/sources/boyd-2005.md) describes (§2.2.2), ions are PIC
particles pushed by $m_i\,d\mathbf v/dt=q_i\mathbf E$ (Eq. 2.4), electrons
are a quasi-neutral fluid whose momentum equation gives $\phi$, and DSMC
collisions follow the move step; Boyd states that quasi-neutrality holds
for several-eV electrons down to about $10^{14}$ m$^{-3}$, except between
the grids of ion thrusters. [Gallo et al. (2021)](/sources/gallo-2021.md)
push only ions and neutrals: $\phi$ and $T_e$ are prescribed in the
Hall-thruster channel and electrons follow a
[Boltzmann relation](/methods/boltzmann-electron-model.md) with a nonlinear
1D Poisson solve in the helicon case (§2, §3). Taccogna et al. (2023,
§III A c, §IV A) list Boltzmann-electron gridded-ion-engine models,
fluid-electron Hall models with particle ions and neutrals, polytropic
plume models and fluid-electron helicon models as hybrid variants.

## Closing the circuit in planar domains

Planar axial–azimuthal and axial–radial domains have no physical cathode,
so the codes inject electrons at a cathode plane to balance the current:
the number emitted per step is set by the anode electron and ion currents
(Charoy et al. 2020, p. 4, emission plane 1 mm inside the boundary,
potential rescaled to zero there); ions minus electrons crossing the anode
plane, with a potential correction that subtracts from the raw Poisson
solution a ramp growing linearly in $z$ from zero at the anode to the
solution's azimuthal mean at the cathode plane, which keeps the 200 V drop
(Marks & Gorodetsky 2025, Eqs. 7–8); emitted current equal to the
anode-collected current after a start-up phase (Miranda et al. 2026, §3);
cathode current equal to anode current (Troyetsky et al. 2026); a variable current that keeps the cells next to the cathode
quasi-neutral (Muñoz Tejeda et al. 2025, Table 2).

## Dimensionality

Taccogna & Garrigues (2019, §3) survey fully kinetic Hall-thruster PIC by
geometry, attributing each result to its authors:

- **1D radial, 3V**, explicit cylindrical (Taccogna et al.) and implicit
  Cartesian (Sydorenko et al.), with imposed $E_z$ of 5–20 kV/m (printed as 50–200 V/cm) and
  $B_r$ of about 0.01–0.02 T (printed as 100–200 G), for the sheath and
  [secondary-emission](/definitions/secondary-electron-emission.md) physics
  (§3.2).
- **2D $r$–$z$**, with a Bohm-type anomalous collision
  $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\,\omega_{ce}/16$ that only scatters
  velocity; fitted $\alpha_{\mathrm B}=0.032$–$0.32$, axially dependent
  (the source's native form is converted on its Source page). The review
  states that these models predict thrust and discharge current within
  20 % and capture breathing and ion-transit-time oscillations (§3.3,
  Fig. 15).
- **1D $\theta$** with re-injection across virtual axial boundaries, which
  the review says gives a cross-field mobility about ten times too large
  with fixed $E_z$; **2D $r$–$\theta$** and **2D $\theta$–$z$**, for the
  [electron drift instability](/definitions/electron-drift-instability.md)
  (§3.4).
- **3D**: an SPT-50 with small ion mass and large $\varepsilon_0$
  (Hirakawa & Arakawa 1995, 1996), miniaturized thrusters, and one
  azimuthal sector of $\pi/20$ (§3.5).

Taccogna et al. (2023, §III A d, §V B a) add that ECDI work exists in 1D
azimuthal, 2D axial–azimuthal, 2D radial–azimuthal and 3D, that
gridded-ion-engine work runs in 3D and inductive and ECR source work in
1D–3D, and that plumes are run 2D-axisymmetric, planar or 3D. A 3D
SPT-100 channel at $n=10^{18}$ m$^{-3}$ and $T_e\sim10$ eV ($\lambda_D\approx20$ µm)
would need about $10^{10}$ cells, "hundreds of billions of particles" and
about 10 TB of memory.
[Adamovich et al. (2017)](/sources/adamovich-2017.md) (§4) call 3D MC/PIC
with adaptive mesh and transient non-isotropic electrons "required for
high-fidelity modeling predictions", and (§17) name Poisson's equation,
"due to its nonlocal nature", as still a major obstacle to parallelization.

The runs of this bundle's sources: 2D-3V axial–azimuthal (Charoy et al.
2020; Marks & Gorodetsky 2025; Miranda et al. 2026, 256 × 256 cells);
2D-3V axial–radial (Troyetsky et al. 2026); pseudo-2D in the axial–azimuthal,
azimuthal–radial and axial–radial planes (Reza et al. 2022); pseudo-2D
axial–radial plus a one-cell 0D model (Muñoz Tejeda et al. 2025); 2D
axial–radial and quasi-1D heavy-species runs (Gallo et al. 2021).

## Codes and cost

| Code | Source | Model | Parallelism | Cost stated |
|---|---|---|---|---|
| LPPic ([benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md)) | Charoy et al. (2020) | 2D-3V electrostatic PIC-MCC, axial–azimuthal | not stated | not stated |
| [WarpX](/software/warpx.md) | Marks & Gorodetsky (2025) | explicit or semi-implicit electrostatic PIC, Python callbacks | GPU, MPI one rank per GPU | 20 µs of the axial–azimuthal benchmark in 1.81 days on one H100, 3.81 days on one V100 |
| XOOPIC | Miranda et al. (2026) | 2D3V electrostatic PIC-MCC | Poisson solver not parallelized | "extremely long execution time", not quantified |
| IPPL code (Julia) | Reza et al. (2022) | explicit electrostatic PIC-MCC, pseudo-2D | not stated | not stated |
| PlasmaSim (C++/Unreal Engine) | Muñoz Tejeda et al. (2025) | fully kinetic electrostatic PIC, 0D and pseudo-2D | OpenMP, ParallelFor | several weeks for 10 µs of a 2D run |
| in-house | Troyetsky et al. (2026) | 2D3V PIC-MCC, axial–radial | MPI particle decomposition | about 5 weeks on 100 cores for 50 µs |
| in-house (MATLAB, CUDA kernel) | Gallo et al. (2021) | ions and neutrals only | one GPU | 55.75 min (GPU) vs 101.2 min (multicore CPU) for the Hall case |

Marks & Gorodetsky (2025, Results) report, from Charoy et al. (2019), that
the best CPU code of that benchmark needed 2.5 days on 112 CPUs for the
same case. Taccogna et al. (2023, §V B) name further codes: ECCOPIC /
ECCOPIC2S-M (implicit, energy-conserving, CUDA), LTP-PIC (OpenACC), EDIPIC,
LSP and Warp (direct implicit), VORPAL, CHAOS (octree PIC-DSMC, MPI-CUDA)
and JET2D (hybrid plume). GPU strategies are on
[GPU acceleration of particle codes](/methods/gpu-acceleration-of-pic.md);
the axial–azimuthal benchmark these codes share is on
[axial–azimuthal Hall-thruster PIC benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md).

## Accuracy against experiment

Boyd (2005, §3.4) attributes to Blateau et al. and Irishkov et al. fully
kinetic Hall-thruster PIC, run with an increased electron-to-ion mass ratio
and an increased vacuum permittivity, that over-predicts thrust by about
10 % and efficiency by about 50 %; he calls fully kinetic modelling
"clearly the direction for future research". The effect of these scalings
is on [permittivity, ion-mass and geometric scaling](/methods/pic-acceleration-scaling.md).
Muñoz Tejeda et al. (2025) compare a water-vapour PIC run at 300 V and
1 mg/s (12.4 mN, 933 s) with a WET-HET measurement (11.2 mN, 1142 s) and
call the agreement "reasonable".

# Citations

1. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §§II, III A, III A d, IV A, V B (accepted manuscript).
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§3.2–3.5, App. 3 (accepted manuscript).
3. [Boyd (2005)](/sources/boyd-2005.md), §§2.2.2, 3.4.
4. [Charoy et al. (2020)](/sources/charoy-2020.md), §§II A, V, p. 4, p. 10 (accepted manuscript).
5. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods, Results, Eqs. 7–8.
6. [Miranda et al. (2026)](/sources/miranda-2026.md), §§2.1, 3, eq. 2.
7. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), "PlasmaSim 2D", Eq. 6, Table 2, performance section.
8. [Reza et al. (2022)](/sources/reza-2022.md), §§2, 3, 4.2, 5.1 (preprint).
9. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), PIC-MCC model section, Eqs. 42–43.
10. [Gallo et al. (2021)](/sources/gallo-2021.md), §§2, 3, 4.3.
11. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §§4, 17.
