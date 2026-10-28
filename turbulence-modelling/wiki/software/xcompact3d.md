---
type: Software
title: "Xcompact3d"
description: "Xcompact3d (successor of Incompact3d) is an open-source Fortran framework for incompressible flow with sixth-order compact finite differences, a spectral Poisson solver and pencil decomposition; this page records its numerics, its implicit spectral vanishing viscosity, the immersed boundaries it hosts, its MHD module and the studies run with it."
status: established
aliases: [Incompact3d, Xcompact3D, Incompact3d/Xcompact3d]
tags: [software, dns, implicit-les, immersed-boundary, mhd]
timestamp: 2026-10-28T17:00:00Z
---

# Xcompact3d

**Xcompact3d** is an open-source (BSD 3-clause) Fortran 90–95 framework,
the successor of Incompact3d, that solves the incompressible
Navier–Stokes equations on Cartesian meshes with sixth-order
[compact finite differences](/methods/compact-finite-difference-scheme.md),
optionally stretched in the wall-normal direction
([Fang et al. 2025](/sources/fang-2025.md), program summary, §2.3). Three
sources of the bundle use it: [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
for explicit against implicit LES of the Taylor–Green vortex and of pipe
flow, [Yan et al. (2024)](/sources/yan-2024.md) for wall-modelled LES on
a diffused-interface immersed boundary, and Fang et al. (2025), who add a
magnetohydrodynamics module for DNS.

## Numerics

As the sources describe the framework:

- **Space.** Sixth-order compact schemes for first and second derivatives
  on a collocated mesh (Lele; Laizet & Lamballais, as Fang et al. cite
  them), with wall-normal stretching (Fang et al. 2025, §2.3). Yan et al.
  (2024, App. A1, Eqs. A1–A3) print the tridiagonal sixth-order first
  derivative with coefficients $1/3$ on the left and $14/9$, $1/9$ on the
  right, the second derivative with $2/11$ and $12/11$, $3/11$, and the
  midpoint interpolation with $3/10$ and $3/4$, $1/20$; Fang et al. (2025,
  Eqs. 15–16) print the staggered sixth-order derivative to the half mesh
  ($9/62$ on the left, $63/62$ and $17/186$ on the right) and the same
  midpoint interpolation. The schemes are on the
  [compact finite-difference](/methods/compact-finite-difference-scheme.md)
  page.
- **Convection** in skew-symmetric form, kinetic-energy conserving up to
  time-integration error (Vicente Cruz & Lamballais 2023, §3; Yan et al.
  2024, Eq. 2; Fang et al. 2025, §2.1, "to reduce aliasing errors"); see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md).
  In truncated-Euler runs the deviation from the initial kinetic energy is
  below 1% over $0\le t\le20$, the loss scaling about as $\Delta t^3$
  (Vicente Cruz & Lamballais 2023, §6.2).
- **Pressure.** Fractional-step projection with a direct Poisson solver in
  spectral space (3D FFTs) on a half-staggered pressure mesh, chosen for
  "numerical stability"; non-periodic conditions through cosine transforms;
  the velocity divergence vanishes "up to machine accuracy" through the
  modified-wavenumber concept (Fang et al. 2025, §2.3; Yan et al. 2024, §II A).
- **Time.** Explicit Adams–Bashforth or Runge–Kutta schemes: third-order
  Runge–Kutta in all MHD benchmarks (Fang et al. 2025, §2.3), third-order
  Adams–Bashforth in the immersed-boundary study (Yan et al. 2024, Eqs. 3–6),
  third-order time stepping in the LES study (Vicente Cruz & Lamballais
  2023, §3).
- **Parallelism.** 2D pencil decomposition through 2DECOMP&FFT, derivatives
  in X, Y and Z pencils with global transposes by MPI all-to-all; prior
  scaling to hundreds of thousands of MPI processes, as Fang et al. (2025,
  §2.3) cite it.

## Implicit LES by spectral vanishing viscosity

The LES closure of two of the studies is the implicit
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
built into the second-derivative scheme of the viscous term, with a single
parameter $\nu_0/\nu$ (the numerical viscosity at the cutoff over the
molecular one): Vicente Cruz & Lamballais (2023, §5) and Yan et al. (2024,
App. B1, Eqs. B1–B8), the latter printing the closed-form coefficients of
the 3–9-point compact scheme as functions of $\nu_0/\nu$. Values used are
$\nu_0/\nu=234$ and $756$ in the pipe (Vicente Cruz & Lamballais 2023,
§7) and 15 to 300 on bluff bodies (Yan et al. 2024). Yan et al. (2024, §III A)
measure 15.04 h wall clock per $10^5$ steps on 96 cores for the sixth-order
scheme with implicit spectral vanishing viscosity, against 18.16 h for a
second-order central scheme with the
[Smagorinsky model](/methods/smagorinsky-model.md) on the same mesh,
because the implicit model computes no SGS terms; see
[implicit LES](/definitions/implicit-les.md).

## Immersed boundaries

- **Reconstruction inside the solid.** Vicente Cruz & Lamballais (2023, §3)
  reconstruct the solution inside the solid so that the compact schemes can
  differentiate across the domain as if it were periodic; the no-slip
  condition is soft and the treatment is not kinetic-energy conserving (see
  [immersed boundary methods](/methods/immersed-boundary-method.md)).
- **Diffused-interface direct forcing with a wall model.** Yan et al. (2024,
  §II B–C) add Lagrangian markers with a 3-point smoothed delta kernel, an
  explicit diagonal approximation of the marker system, and a wall model
  that replaces the no-slip target velocity by a slip target from explicit
  wall functions with a pressure-gradient correction (see
  [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md) and
  [wall-modelled LES](/methods/wall-modelled-les.md)). They state that the
  strong scaling of Xcompact3d is kept with the wall-modelled immersed
  boundary from about 10 to about 1000 cores (Fig. 4), and present the
  coupling as the first of a wall-modelled diffused-interface immersed
  boundary with high-order compact finite differences (Table I).

## MHD module

Fang et al. (2025, §2, Fig. 1, Table 1) add two MHD systems to the
incompressible solver, selected by the input `mhd_equation`, with the
Lorentz force $N_{\mathrm{St}}(\boldsymbol J\times\boldsymbol B)$ added to
the momentum equation; $N_{\mathrm{St}}=\sigma B_0^2L/(\rho U)$ is the
Stuart number (interaction parameter), $\boldsymbol J$ the current density
and $\sigma$ the electrical conductivity (page-local symbols; all
quantities nondimensional as in the source):

- **Induction solver** (finite $Rm$): the induction equation in
  skew-symmetric form with diffusion $Rm^{-1}\nabla^2\boldsymbol B$ and
  $\boldsymbol J=Rm^{-1}\nabla\times\boldsymbol B$. After the predictor
  $\boldsymbol B^*$, a "magnetic pressure" $\psi_B$ (page-local) is obtained
  from $\nabla^2\psi_B=\nabla\cdot\boldsymbol B^*$ by the same spectral
  Poisson solver and the field is corrected to
  $\boldsymbol B=\boldsymbol B^*-\nabla\psi_B$ (Eqs. 11–13); the authors
  attribute the step to the divergence cleaning of Dedner et al. After the
  correction the magnetic divergence in the 2D Orszag–Tang vortex is noise
  of order $10^{-13}$ (§3.1, Fig. 4).
- **Potential solver** (quasi-static limit $Rm\ll1$, imposed field
  $\boldsymbol B_0$): one Poisson equation
  $\nabla^2\varphi=\nabla\cdot(\boldsymbol u\times\boldsymbol B_0)$ for the
  electric potential $\varphi$ (page-local) and Ohm's law
  $\boldsymbol J=-\nabla\varphi+\boldsymbol u\times\boldsymbol B_0$
  (Eqs. 7–8). It is cheaper and avoids the stiffness of the induction
  equation at very low $Rm$ (§2.1).

**Cost and scaling on ARCHER2** (AMD EPYC 7742, §3.5, Table 7, Figs. 16–17):
with 262 144 mesh nodes per core, a time step costs 0.54, 0.92 and 1.43 s
(Navier–Stokes, with the potential solver, with the induction solver) on
8 cores and $128^3$, and 2.41, 3.56 and 6.33 s on 4096 cores and $1024^3$;
the authors summarize the overheads as about 1.5 (potential) and 2.6
(induction) times the Navier–Stokes cost. Strong scaling to 32 768 cores
is called excellent up to 1024 cores for $256^3$ and up to 16 384 cores
for $1024^3$, and the MHD solvers "do not alter the strong scaling of
Xcompact3d".

## Applications in the sources

- **Explicit against implicit LES** (Vicente Cruz & Lamballais 2023): the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=40\,000$
  (reference DNS on $5400^3$ nodes) and pipe flow at $Re_\tau=1000$ and
  2000 on a Cartesian mesh with an immersed boundary; implicit spectral
  vanishing viscosity at $\Delta x^+=\Delta y^+\approx9$ predicts $u_\tau$
  within 1.8% (pipe cross-section spacings), but fails at $\Delta x^+=18$.
  Results are on [implicit LES](/definitions/implicit-les.md) and
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md).
- **Wall-modelled LES of bluff bodies** (Yan et al. 2024, §III): the
  [circular cylinder](/benchmarks/circular-cylinder-wake.md) at
  $Re_D=3.9\times10^3$ and $1.4\times10^5$, the
  [square cylinder](/benchmarks/square-cylinder-flow.md) at
  $Re_D=2.2\times10^4$ (13.2 h CPU time per shedding cycle as printed,
  against about 1058 and 676 h that the authors infer for two wall-resolved
  LES, Table V) and a
  large-span flat roof in forced vibration.
- **MHD DNS** (Fang et al. 2025, §3–§4): 2D and 3D Orszag–Tang vortices
  (see [decaying MHD turbulence](/results/decaying-mhd-turbulence.md)),
  laminar Hartmann flow against the analytical profile, the turbulent MHD
  [channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=150$ with a
  wall-normal field, which relaminarizes at Hartmann number 8, and a new
  MHD variant of the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  with an imposed uniform field; see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md).

## Qualifications

- Fang et al. (2025, §3.5) summarize the overheads as about 1.5 and 2.6;
  at 64 cores the printed Table 7 times give $2.31/1.44=1.60$ (potential)
  and $3.0/1.44=2.08$ (induction), and at 8, 512 and 4096 cores 1.48–1.70
  and 2.63–2.66 *(compiler check, not in the sources)*.
- Yan et al. (2024, App. B2) print the comparison Smagorinsky model as
  $\nu_t=C_s\Delta^2\lvert\bar S\rvert$ with $C_s=0.12$, the constant to the
  first power; mapped on the [Smagorinsky model](/methods/smagorinsky-model.md)
  page, no verdict.
- Printed slips (Fang et al. 2025): §3.3 prints the Hartmann number as
  $B_0L\sqrt{\sigma\rho_0/\nu}=\sqrt{Re\,N_{\mathrm{St}}}$, whereas the
  printed definitions of $Re$ and $N_{\mathrm{St}}$ give
  $\sqrt{Re\,N_{\mathrm{St}}}=B_0L\sqrt{\sigma/(\rho_0\nu)}$ *(compiler
  check, not in the sources)*; "Dellar [16]" names the reference that the
  list prints as Dedner et al. (2002), and "Orszag and Tang [5]" the one
  printed as Orszag (1969), Orszag & Tang (1979) being ref. [22]. Yan et
  al. (2024) write "six-order" for "sixth-order" throughout.

# Citations

- [Fang et al. (2025)](/sources/fang-2025.md) — program summary; §2.1, Eqs. (1)–(8) (MHD systems, skew-symmetric convection); §2.2, Eqs. (9)–(13), Fig. 1 (induction and potential solvers, magnetic correction); §2.3, Eqs. (14)–(16), Table 1 (compact schemes, spectral Poisson solver, half-staggered mesh, 2DECOMP&FFT, input variables); §3.1–§3.5, Table 7, Figs. 4, 16–17 (validations, cost, scaling); §4 (MHD Taylor–Green vortex).
- [Yan et al. (2024)](/sources/yan-2024.md) — §I, Table I; §II A–C, Eqs. (1)–(32) (filtered equations, Adams–Bashforth, diffused-interface immersed boundary with wall model); §III A–C, Fig. 4, Table V (cost, scaling, applications); App. A1, Eqs. (A1)–(A3); App. B1–B2, Eqs. (B1)–(B11).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — HAL manuscript: §3 (Incompact3d/Xcompact3d, skew-symmetric convection, immersed boundary); §5 (implicit spectral vanishing viscosity); §6.2; §7 (pipe flow).
