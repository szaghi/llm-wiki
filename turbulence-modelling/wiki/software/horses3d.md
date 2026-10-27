---
type: Software
title: "HORSES3D"
description: "HORSES3D is an open-source Fortran DGSEM framework for compressible and incompressible flow with RANS, explicit and implicit LES, shock capturing, multiphase, particles, aeroacoustics and immersed boundaries; this page records its numerics, turbulence options including jump-penalty implicit LES and self-tuning explicit modal filtering, adaptation, solvers and parallel performance."
status: established
aliases: [HORSES3D, High-Order Spectral Element Solver 3D, horses2plt]
tags: [software, dg, les, implicit-les, entropy-stable, mesh-adaptation]
timestamp: 2026-10-26T20:48:00Z
---

# HORSES3D

**HORSES3D** (High-Order Spectral Element Solver 3D) is the open-source
(MIT) discontinuous Galerkin spectral element framework of the NUMATH group
at the Universidad Politécnica de Madrid, described by
[Ferrer et al. (2023)](/sources/ferrer-2023.md). It is an object-oriented
Fortran code (the program summary says Fortran 2008, §3 says Fortran 2003)
with optional METIS, MPI, HDF5, MKL and PETSc, and reads curvilinear,
conforming hexahedral meshes in GMSH, HDF5 and SpecMesh/HOHQMesh formats
(Program summary; §3.1). One executable is compiled per physics module, and a
separately compiled "problem file" library supplies user hooks for initial
and boundary conditions, source terms and monitoring (§3.4). The
post-processor `horses2plt` interpolates to homogeneous nodes, changes the
polynomial degree and extracts vorticity, $Q$-criterion and Reynolds
stresses (§3.1). The paper is a code description: its figures are mostly
taken from the group's earlier papers. The version read is the arXiv v1
preprint, which lists 13 of the 14 authors of the published article.

## Rationale for high order

Ferrer et al. (2023, §1) argue from an error model in which the error decays
as a power of the number of degrees of freedom with the order as exponent:
equal error for a low-order and a high-order method gives
$\mathrm{dof}_{\mathrm{HO}}=\mathrm{dof}_{\mathrm{LO}}^{\,p_{\mathrm{LO}}/p_{\mathrm{HO}}}$
(page-local orders $p$). With $p_{\mathrm{LO}}=2$, $p_{\mathrm{HO}}=5$ and
$10^8$ low-order degrees of freedom this gives about 1600, "a factor of
60000" fewer, which the authors call optimistic because near-wall resolution
is ignored. The printed values are consistent with $10^{8\times0.4}\approx1585$
*(compiler check, not in the sources)*. They put typical low-order aircraft
simulations at 50 to 100 million degrees of freedom.

## Numerics

- **Discretization.** [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
  on curvilinear hexahedra with Gauss or Gauss–Lobatto nodes; Gauss nodes
  are "more accurate", Gauss–Lobatto nodes allow energy- or entropy-stable
  formulations through the summation-by-parts property (§3.3, §3.5);
  [Ranjbar et al. (2026)](/sources/ranjbar-2026.md), §II.A, repeat the
  preference for Gauss–Lobatto nodes in energy- or entropy-stable schemes.
- **Fluxes.** Convective: central, Lax–Friedrichs, Rusanov, Roe,
  low-dissipation Roe, Roe–Pike, matrix dissipation. Viscous: BR1, BR2,
  symmetric interior penalty (§3.3).
- **Split forms.** Morinishi, Ducros, Kennedy–Gruber, Pirozzoli, entropy
  conserving and Chandrashekar, on Gauss–Lobatto nodes; the group has
  extended entropy stability to the Spalart–Allmaras equations and to a
  Navier–Stokes/Cahn–Hilliard multiphase model (§3.5; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
- **Adaptation.** Anisotropic $p$-adaptation (a degree per element and
  direction) driven by $\tau$-estimation of the truncation error, which the
  authors prefer because it "targets the source of the discretisation
  error" and is a by-product of a multigrid cycle; the threshold, which "does
  not have any direct physical or engineering meaning", has been tied to a
  flow functional. $p$-non-conforming faces are coupled by mortars, "which
  does not retain entropy stability" (§3.6). Feature-based adaptation tracks
  multiphase interfaces. See [mesh adaptation](/methods/mesh-adaptation.md).
- **Time integration.** Low-storage explicit third-order Runge–Kutta by
  default, fourth-order Runge–Kutta; nonlinear $p$-multigrid (FAS) with
  explicit or semi-implicit smoothers (BIRK, LU-SGS, ILU(0)) for steady
  problems; BDF of orders 1–5 and a sixth-order Rosenbrock scheme for
  unsteady ones, with analytical or colour-based numerical Jacobians,
  Jacobian-free GMRES, PETSc and dual time stepping (§3.7).
- **Parallelism.** Hybrid MPI+OpenMP. On a $64^3$ Taylor–Green vortex the
  hybrid code reaches "86% of the ideal performance for 600 cores and $P=6$"
  (degree $N=6$), pure MPI scaling worse (§3.8). The abstract states "good
  scalability for up to 1000 processors" and §3.8 "up to a thousand cores";
  the quantified efficiency in the text is the one at 600 cores.

## Turbulence options

Ferrer et al. (2023, §4.1) define DNS as solving "the Navier-Stokes
equations without additional modelling", restricted to moderate Reynolds
numbers, and list the closures available:

- **RANS:** the negative [Spalart–Allmaras model](/methods/spalart-allmaras-model.md);
  the NASA Common Research Model at $M=0.85$, $Re=5\times10^6$, 2.3° with
  $N=2$ and split-form inviscid fluxes is shown as pressure contours only.
- **Explicit LES:** [Smagorinsky](/methods/smagorinsky-model.md), WALE,
  [Vreman](/methods/vreman-model.md) and the group's SVV-Smagorinsky model,
  which "was capable of maintaining low dissipation levels for laminar
  flows, while providing the correct dissipation for all wave-number ranges
  in turbulent regimes" (see [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md));
  no model formulas or constants are printed.
- **Implicit LES:** because DG dissipation and dispersion errors sit at high
  wavenumbers, the authors call DG "very suitable for ILES" and offer three
  routes: dissipative Riemann solvers, an interior-penalty parameter raised
  above its coercivity minimum, and energy-stable split forms combined with
  SVV ([implicit LES](/definitions/implicit-les.md)). An implicit LES of the
  NACA 0012 at $Re=10^6$ on 18,000 hexahedra with $N=4$ (2.2 million degrees
  of freedom) is reported in "very good agreement" with experimental lift and
  drag polars (Fig. 7, from an earlier paper; the experiment is not cited).
- **Shock capturing** by an entropy-stable, SVV-filtered artificial viscosity
  with a density-gradient troubled-element sensor (§4.4), the method of
  [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) described on the
  DGSEM page; HORSES3D does not use [subcell finite volumes](/methods/subcell-finite-volume-shock-capturing.md).

The program summary and §1 mention wall models, but none is described in the
text.

**Jump penalties as implicit LES.** [Kou et al. (2023)](/sources/kou-2023.md)
implement two face penalties in HORSES3D, on the solution jump (the
symmetric-interior-penalty viscous flux with an enlarged parameter, the
second implicit-LES route above) and on the gradient jump, with a Roe flux,
SIP viscous flux, no over-integration and the penalties scaled by $1/Re$ and
applied to a selected subset of the equations (momentum only at low Mach
number, all equations for compressible cases) (§2.2). On the Taylor–Green
vortex at $Re=1600$, $M=0.1$, $32^3$ elements, $N=3$, the unpenalized code
diverges and both penalties remove a spurious second peak of the
dissipation rate and beat the Smagorinsky and Vreman models adapted to DG;
on a Kelvin–Helmholtz instability only the solution penalty completes the
run (§4.2–4.3). Details are on
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md).

**Self-tuning explicit modal filtering.** Ranjbar et al. (2026) implement
in HORSES3D their self-tuning dynamic explicit modal filter (STDEMF), an LES
closure that filters the solution itself in modal space instead of adding
an SVV flux: nodal values on Gauss–Lobatto points are mapped to Legendre
modes by precomputed matrices, mode groups above an element-wise,
time-dependent cut-off are attenuated by a tanh kernel, and the result is
blended back with weight 0.01 at every step, only in elements whose local
Kolmogorov length is smaller than the mean grid spacing (§II.B–C; details
on [explicit modal filtering](/methods/explicit-modal-filtering.md)). They
describe HORSES3D as an object-oriented Fortran DG code with explicit time
marching, extended to incompressible, multiphase, acoustic and particle
flows, shock capturing, turbulence models, energy- and entropy-stable
schemes, polynomial adaptation and immersed boundaries, available under
MIT on GitHub (§II.C). Their settings: Williamson's low-storage third-order
Runge–Kutta, MPI+OpenMP on CPUs; the low-dissipation Roe flux with BR1 and
zero penalty (interface averaging) for the periodic boxes, the "standard
form" (no split form) for decaying isotropic turbulence and the split form with Chandrashekar
averaging for the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md);
for the [channel](/benchmarks/turbulent-channel-flow.md) the split form
with BR2 and penalty 1.5, because "the presence of walls in channel flow
necessitates BR2" (§II.A, §III). Test cases, all a posteriori on coarse
unmodelled meshes ("coarse DNS"): decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at
$Re=450$ on $6^3$ elements with $N=7$ (DNS $12^3$, $N=8$, validated against
the DSEM code of Ranjbar et al. (2024c, as recalled)); the Taylor–Green vortex at
$Re=200$ on $11^3$ elements, $N=4$, and at $Re=800$ on $7^3$, $N=10$; and the
compressible channel at $Re_\tau=395$, $M=0.3$, on
$14\times12\times16$ elements with $N=6$. The filter, with constant 0.65,
0.25 and 0.5 respectively, comes closest to the reference DNS in all three,
while the [Smagorinsky model](/methods/smagorinsky-model.md) with
$C_s=0.12$ over-dissipates late in the decay, is called "not a suitable
option" for the Taylor–Green vortex, and in the channel crashes for
$C_s<0.15$ and deviates "significantly" at $C_s=0.2$ (results not shown).
The filter costs 1.31% extra wall time on the $Re=800$ Taylor–Green case
and 0.96–2.5% on the channel, depending on the averaging used by its sensor,
with the same number of processors (§III.D.3; hardware not stated). The
unmodelled channel run keeps non-zero velocity fluctuations at the wall,
which the authors attribute to the weak imposition of the boundary
condition, and filtering drives them to zero (§III.C).

## Other physics

Artificial-compressibility incompressible solver with dual time stepping;
entropy-stable Navier–Stokes/Cahn–Hilliard multiphase solver; two-way
coupled Lagrangian point particles with radiative heating;
[Ffowcs Williams–Hawkings](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
acoustics (convective form, solid or permeable surfaces,
quadrupoles neglected; about 7% amplitude error for a monopole in a
$M=0.5$ stream); and a volume-penalization
[immersed boundary method](/methods/immersed-boundary-method.md) with STL
ray tracing, shown on a wind turbine (§4.2–4.7).

## Comparison with other high-order codes

Table 1 of Ferrer et al. (2023, §2) ticks twelve capabilities for HORSES3D,
Nek5000, Nektar++, Semtex, deal.II, Flexi/Fluxo, Trixi and PyFR as judged by
the authors in June 2022; HORSES3D is the only one ticked for RANS and has
all twelve, from which the authors conclude it "provides a unique set of
capabilities". For [FLEXI](/software/flexi.md) see its page;
[Nek5000](/software/nek5000.md) is a continuous spectral element code.
[Kurz et al. (2025)](/sources/kurz-2025.md), §1, introducing the GPU code
[GALÆXI](/software/galaexi.md), name HORSES3D and
[Nektar++](/software/nektar-plus-plus.md) as the spectral element codes that
solve both the compressible and the incompressible Navier–Stokes equations.
They do not say whether either runs on GPUs.

## Reproducibility

Test cases (manufactured solutions, Taylor–Green vortex, cylinder, NACA
0012, forward-facing step and others) run on GitHub workflows at every pull
request, and a fuller suite runs monthly across compilers in serial and
parallel (§5.1–5.2).

## Qualifications

- The version read (arXiv v1, June 2022) leaves the program-summary links
  unfilled and lists a private repository; the published version may differ.
  Ranjbar et al. (2026, §II.C) give a public GitHub repository under the MIT
  licence.
- Printed slips: Eq. (2) has $\rho u_3$ where the other entries use $v$;
  §3.2 mixes $e$ and $E$ for the total energy; §4.6 swaps "loading" and
  "thickness" relative to the paper's own Eqs. (25)–(26); the reference list
  prints one Gassner–Winters–Kopriva paper twice.

# Citations

- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — Program summary; §1 (degree-of-freedom estimate); §2, Table 1; §3.1–3.8, Figs. 1–5 (numerics, split forms, adaptation, solvers, scaling); §4.1, Figs. 6–7 (turbulence closures); §4.2–4.7, Figs. 8–14 (other physics); §5.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §5–§6 (the SVV-filtered artificial viscosity used for shock capturing).
- [Kou et al. (2023)](/sources/kou-2023.md) — §2.2, Eqs. (15)–(25) (jump penalties in HORSES3D); §4.2–4.3 (Taylor–Green vortex, Kelvin–Helmholtz instability).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §1 (HORSES3D among high-order solvers).
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §II.A (DGSEM settings, Gauss–Lobatto preference, time integration, MPI+OpenMP); §II.B (modal filter); §II.C (HORSES3D description, licence); §III.A–C, Figs. 3, 13–15 (isotropic turbulence, Taylor–Green vortex, channel, Smagorinsky comparison); §III.D.3 (cost overhead).
