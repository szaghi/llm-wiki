---
type: Software
title: "HORSES3D"
description: "HORSES3D is an open-source Fortran DGSEM framework for compressible and incompressible flow with RANS, explicit and implicit LES, shock capturing, multiphase, particles, aeroacoustics and immersed boundaries; this page records its numerics, turbulence options, adaptation, solvers and parallel performance as its developers describe them."
status: established
aliases: [HORSES3D, High-Order Spectral Element Solver 3D, horses2plt]
tags: [software, dg, les, implicit-les, entropy-stable, mesh-adaptation]
timestamp: 2026-10-25T20:42:00Z
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
  formulations through the summation-by-parts property (§3.3, §3.5).
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

## Other physics

Artificial-compressibility incompressible solver with dual time stepping;
entropy-stable Navier–Stokes/Cahn–Hilliard multiphase solver; two-way
coupled Lagrangian point particles with radiative heating; Ffowcs
Williams–Hawkings acoustics (convective form, solid or permeable surfaces,
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

## Reproducibility

Test cases (manufactured solutions, Taylor–Green vortex, cylinder, NACA
0012, forward-facing step and others) run on GitHub workflows at every pull
request, and a fuller suite runs monthly across compilers in serial and
parallel (§5.1–5.2).

## Qualifications

- The version read (arXiv v1, June 2022) leaves the program-summary links
  unfilled and lists a private repository; the published version may differ.
- Printed slips: Eq. (2) has $\rho u_3$ where the other entries use $v$;
  §3.2 mixes $e$ and $E$ for the total energy; §4.6 swaps "loading" and
  "thickness" relative to the paper's own Eqs. (25)–(26); the reference list
  prints one Gassner–Winters–Kopriva paper twice.

# Citations

- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — Program summary; §1 (degree-of-freedom estimate); §2, Table 1; §3.1–3.8, Figs. 1–5 (numerics, split forms, adaptation, solvers, scaling); §4.1, Figs. 6–7 (turbulence closures); §4.2–4.7, Figs. 8–14 (other physics); §5.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §5–§6 (the SVV-filtered artificial viscosity used for shock capturing).
