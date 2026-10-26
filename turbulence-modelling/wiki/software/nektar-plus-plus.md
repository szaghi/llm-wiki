---
type: Software
title: "Nektar++"
description: "Nektar++ is an open-source spectral/hp element framework with continuous and discontinuous Galerkin solvers; this page records the incompressible and acoustic solvers, stabilizations (spectral vanishing viscosity, gradient-jump penalisation), meshing and costs used by the scale-resolving and aeroacoustic studies of the bundle."
status: established
aliases: [Nektar, NektarPlusPlus, IncNavierStokesSolver, AcousticSolver, NekMesh, FieldConvert]
tags: [software, spectral-element, les, implicit-les, aeroacoustics]
timestamp: 2026-10-26T07:42:00Z
---

# Nektar++

**Nektar++** is an open-source spectral/hp element framework (cited by the
sources to Cantwell et al. 2015 and Moxey et al. 2020) whose solvers
discretize the domain into elements carrying high-order polynomial
expansions, with continuous (CG) or discontinuous (DG) Galerkin coupling.
Two solvers appear in the bundle: the incompressible Navier–Stokes solver
`IncNavierStokesSolver`, used for [implicit LES](/definitions/implicit-les.md)
of a combustor flow by [Saini et al. (2023)](/sources/saini-2023.md) and of
a multi-element wing by [Slaughter et al. (2023)](/sources/slaughter-2023.md);
and the `AcousticSolver`, used to propagate jet noise by
[Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md). The tools
`NekMesh` (high-order meshing) and `FieldConvert` (post-processing) also
appear. Nektar++ is a relative of the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) codes of
the bundle; its incompressible solver is continuous, like
[Nek5000](/software/nek5000.md).

## Incompressible solver

- **Discretization.** Continuous Galerkin spectral/hp elements on
  unstructured hybrid meshes with a Jacobi-polynomial basis; velocity one
  order higher than pressure, "to satisfy the inf-sup condition" (Saini et
  al. 2023, §2.1, Table 1: orders 4 and 3) or as Taylor–Hood-type
  expansions (Slaughter et al. 2023, §3.1, §3.3: orders 6 and 5).
  Slaughter et al. state that orders 3 to 8 are typical for industrial
  problems in Nektar++.
- **Quasi-three-dimensional option.** Spectral/hp elements in the $x$–$y$
  plane combined with a Fourier expansion in a homogeneous spanwise direction
  (the "Fourier spectral/hp" method; Slaughter et al. 2023, §3.1: 64 Fourier
  modes over a span of $0.16c$, $c$ the main-element chord).
- **Splitting and time stepping.** Velocity-correction (operator-splitting)
  scheme of Guermond and Shen, decoupling pressure and velocity;
  second-order implicit–explicit time integration, convection explicit and
  diffusion implicit (Slaughter et al. 2023, §3.1); second-order backward
  differencing in Saini et al. (2023, Table 1), whose convection term is
  upwinded (§2.1).
- **Linear solver.** Direct solver with multi-level static condensation
  (recursive boundary/interior decomposition and Schur complements)
  (Slaughter et al. 2023, §3.1).
- **Boundary conditions.** High-order Neumann pressure condition on walls and
  a high-order convective outflow condition (Slaughter et al. 2023, §3).

## Stabilization and subgrid dissipation

Neither study adds an explicit subgrid model to the Nektar++ runs.

- **[Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).**
  Saini et al. (2023, §2.2, §2.3, Eqs. 14–15) use the power-kernel SVV of
  Moura et al., with amplitude $\epsilon_{\mathrm{SVV}}=\epsilon_0U_lh/N$ and
  modal kernel $\hat Q(m)=(m/N)^{P_{\mathrm{SVV}}}$ (page-local: $\epsilon_0$ a
  fixed parameter, $U_l$ a local advection speed, $h$ the element size, $m$
  the mode index, $P_{\mathrm{SVV}}$ the activation exponent; values not
  printed). Slaughter et al. (2023, §3.1) use SVV with an exponential kernel
  only in the Fourier direction, active on modes above the product of a
  cut-off ratio and the polynomial order (values not printed).
- **[Gradient-jump penalisation](/methods/jump-penalty-stabilization.md)**
  (GJP of Moura et al.) stabilizes the in-plane discretization of Slaughter
  et al. (2023, §3.1), who relay that SVV at low polynomial order "can be
  overly diffusive" and that GJP "has out-performed the SVV approach on
  canonical cases but has yet to be applied to more complex geometries".

How much of the total dissipation these stabilizations carry is measured by
Saini et al. (2023, §5): over turbulent subdomains of a combustor port flow,
SVV supplies 15–44% of the non-viscous dissipation and the numerical
dissipation of the discretization the rest (see
[numerical dissipation](/properties/numerical-dissipation.md)).

## Meshing and post-processing

`NekMesh` projects a linear mesh onto the CAD geometry to make it
curvilinear and splits a single prismatic boundary-layer layer
isoparametrically into a geometric series of thinner layers (Slaughter et
al. 2023, §3.2: 10 layers at growth rate 1.4 around the wing elements, 5 on
the floor). `FieldConvert` computes derivatives at solution order for the
dissipation budgets of Saini et al. (2023, §2.3), who evaluate the SVV
convolution by FFT on a three-times-finer uniform grid with a Tukey window
and call that procedure "less general and non-exact".

## Acoustic solver

The `AcousticSolver` used by Moratilla-Vega et al. (2024, §2.2) solves the
acoustic perturbation equations (APE-4) with a DG spectral/hp method on a
fifth-order ($N=5$) Gauss–Lobatto–Legendre nodal basis, a Lax–Friedrichs
flux, an absorbing forcing layer near the outer boundaries and classical
fourth-order Runge–Kutta, at $\mathrm{CFL}=1/(2N+1)$ (Eq. 12). The source
terms (the Lamb-vector perturbation) come from a second-order
finite-volume LES with the $\sigma$ model through one-way, in-memory
coupling by the CWIPI library over a shared MPI communicator (§2.3). The
grid of about $10^6$ elements carries $216\times10^6$ solution points
(Table 1). The authors quote 5 points per wavelength for this scheme against
22 for second-order methods (§4.4).

## Studies run with it

| Study | Solver | Case | Resolution | Cost |
|---|---|---|---|---|
| Saini et al. (2023), §3 | incompressible CG, $N=4/3$, SVV (v4.5.0) | [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), $Re=1600$ and 3000 | $8^3$ and $16^3$ elements | $16^3$: 1.3 times the cost of a $64^3$ second-order finite-volume run, about ten times more accurate (relayed from the authors' earlier study) |
| Saini et al. (2023), §3.2 | same | combustor port flow, $Re_p=2.25\times10^4$ | 130 000 elements, $8.4\times10^6$ points | 1.03 times a 16-million-point second-order run (178 h on 336 cores) |
| Slaughter et al. (2023), §3 | Fourier spectral/hp, $N=6/5$, GJP + SVV | [Imperial front wing](/benchmarks/imperial-front-wing.md), $Re=2.2\times10^5$ | 64 Fourier modes; first quadrature point at $y^+\lesssim1$ except two small regions | not stated (ARCHER2 and CSD3) |
| Moratilla-Vega et al. (2024), §3 | acoustic DG, $N=5$ | installed and isolated subsonic jet | about $10^6$ elements | not stated |

Saini et al. (2023, §6) attribute the accuracy-per-cost advantage of the
Nektar++ runs over second-order OpenFOAM runs primarily to lower numerical
dissipation, the model playing a secondary role. Slaughter et al. (2023)
obtain $C_L=-8.33$, $C_D=0.17$ and resolve laminar separation bubbles on the
wing; no grid-convergence study or experimental comparison of that slice
case is shown.

## Qualifications

- Ferrer et al. (2023, §2, Table 1) list Nektar++ among the high-order codes
  they compare with HORSES3D (see [HORSES3D](/software/horses3d.md)).
- The version of Slaughter et al. read is the Research Square preprint
  (v1); its reference to
  the Nektar++ paper prints a Mendeley Data DOI prefix.
- The polynomial orders are written $P$ (Saini et al.) and "polynomial
  order" or $p$ (Slaughter et al., Moratilla-Vega et al.); they are $N$ here.

# Citations

- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, Table 1 (solver set-up); §2.2–2.3, Eqs. (6)–(15) (SVV, FieldConvert, FFT convolution); §3, Table 2 (cases, costs); §5–6 (dissipation shares, conclusion).
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — Research Square preprint v1: §3, §3.1 (Fourier spectral/hp, velocity correction, static condensation, IMEX, GJP, SVV); §3.2 (NekMesh); §3.3 (orders, boundary conditions); §3.6, §4.
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §2.2, Eqs. (11)–(12) (AcousticSolver); §2.3 (CWIPI coupling); §3, Table 1; §4.4.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §2, Table 1.
