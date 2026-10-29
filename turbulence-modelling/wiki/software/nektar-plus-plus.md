---
type: Software
title: "Nektar++"
description: "Nektar++ is an open-source spectral/hp element framework with continuous and discontinuous Galerkin solvers; this page records the incompressible and acoustic solvers, stabilizations (spectral vanishing viscosity, gradient-jump penalisation), the wall-modelled SVV implicit LES, meshing and costs used by the scale-resolving and aeroacoustic studies of the bundle."
status: established
aliases: [Nektar, NektarPlusPlus, IncNavierStokesSolver, AcousticSolver, NekMesh, FieldConvert]
tags: [software, spectral-element, les, implicit-les, wmles, aeroacoustics]
timestamp: 2026-10-29T07:38:00Z
---

# Nektar++

**Nektar++** is an open-source spectral/hp element framework (cited by the
sources to Cantwell et al. 2015 and Moxey et al. 2020) whose solvers
discretize the domain into elements carrying high-order polynomial
expansions, with continuous (CG) or discontinuous (DG) Galerkin coupling.
Two solvers appear in the bundle: the incompressible Navier–Stokes solver
`IncNavierStokesSolver`, used for [implicit LES](/definitions/implicit-les.md)
of a combustor flow by [Saini et al. (2023)](/sources/saini-2023.md) and of
a multi-element wing by [Slaughter et al. (2023)](/sources/slaughter-2023.md),
and coupled to a wall-stress model for the wall-modelled implicit LES of
channel flow of [Huang et al. (2022c)](/sources/huang-2022-c.md);
and the `AcousticSolver`, used to propagate jet noise by
[Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md). The tools
`NekMesh` (high-order meshing) and `FieldConvert` (post-processing) also
appear. Its DG coupling is shared with the
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
  problems in Nektar++. Huang et al. (2022c, §II A) use hexahedra with
  tensor-product Lagrange interpolants on Gauss–Lobatto–Legendre points for
  velocity and pressure, "of order $N_p$" (as printed; see Qualifications).
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

Neither study adds an explicit subgrid model to the Nektar++ runs, and neither does Huang et al. (2022c), whose spectral-vanishing-viscosity implicit LES is described below.

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

## Wall-modelled SVV implicit LES

Huang et al. (2022c) couple an algebraic
[equilibrium wall model](/methods/equilibrium-wall-model.md) to the
spectral-vanishing-viscosity implicit LES (SVV-iLES) of the incompressible
solver, and claim it as "the first to construct the wall model of SVV-iLES
based on the spectral/hp element method" (Abstract, §I). They write the SVV
term in the Kirby–Sherwin form, with an effective strength and a kernel
acting on the high modes (Eqs. 12–13), and cite the "DG kernel" of Moura
et al.; the kernel, strength and cut-off of their own runs are not stated
(§II B; see [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)).
Time stepping is the second-order velocity-correction (stiffly stable)
scheme: explicit non-linear terms, a pressure Poisson solve, then Helmholtz
solves for the viscous terms (§II A). The code-specific points:

- **Free sampling height.** The resolved velocity is interpolated at any
  wall distance $h_{\mathrm{wm}}$ by evaluating the elemental high-order expansion after
  locating the element and its reference coordinates (Eqs. 15–16); the runs
  sample at the top of the first wall-adjacent element, $0.224\delta$
  (§II C, §III A).
- **Neumann condition.** $u_\tau$ is found from the log law
  ($\kappa=0.41$, $B=5.2$, Eq. 14) by Newton–Raphson and the wall stress is
  imposed as a Neumann condition on the streamwise velocity, with zero
  wall-normal and spanwise velocity at the wall (Eq. 20). The authors choose
  the Neumann type so that no mixing-length eddy viscosity enters the
  equations at the interface and, with the velocity-correction scheme, the
  Helmholtz problems keep a constant viscosity coefficient (§I).
- **Channel results.** On one $12\times6\times10$-element mesh at
  $Re_\tau=550$, 950 and 2000 (body-force driven, at least 250 flow-through
  times of transient and more than 45 of averaging), the mean velocity is
  "almost not distinguishable" from DNS at 550 and over-predicted by at most
  2% at 950 and 5.4% at 2000; r.m.s. fluctuations and Reynolds shear stress
  show a "parabolic" error near the matching interface, which the authors
  attribute to the Neumann condition (§III B, Figs. 4–6). Reichardt's law in
  place of the log law, and an exponential moving average of the sampled
  velocity, change the results only slightly, so the instantaneous velocity
  is recommended (§III C–D). See [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
  and [wall-modelled LES](/methods/wall-modelled-les.md).
- **h against p.** At similar resolution in wall units, a mesh of
  $14\times8\times12$ elements at $N_p=6$ gives worse fluctuations and shear
  stress than the $12\times6\times10$ mesh at $N_p=7$, with the same mean
  velocity (§III E, Fig. 9); the conclusions call this "p-type refinement"
  and §III E "h-type refinement".
- **Cost.** With the same element mesh and polynomial order in the resolved
  region, the wall-modelled run is up to seven times cheaper than the
  wall-resolved SVV-iLES at $Re_\tau=550$; no wall-clock or hardware figures
  are given (§III A).

Huang et al. (§II B) cite an earlier wall-resolved SVV-iLES by Wang, Wu, Xu &
Sherwin (2021), "well validated for turbulent separated flows", whose
optimized SVV-iLES performs "at least as well as" a subgrid model (the
cited title, ref. 14, names channel flow), and set their work apart from the Nek5000
wall-modelling framework of Pal et al. (see [Nek5000](/software/nek5000.md)).

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
| Huang et al. (2022c), §III | incompressible CG, "$N_p=7$" and 6, SVV, log-law wall model | [channel flow](/benchmarks/turbulent-channel-flow.md), $Re_\tau=550$–2000 | $12\times6\times10$ and $14\times8\times12$ elements | wall-modelled up to 7 times cheaper than wall-resolved (no timings) |
| Moratilla-Vega et al. (2024), §3 | acoustic DG, $N=5$ | installed and isolated subsonic jet | about $10^6$ elements | not stated |

A further Nektar++ study is known in the bundle only through a citation: in
their literature survey of the [periodic hill](/benchmarks/periodic-hill.md)
at $Re_h=10\,600$, [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md),
§2.4, Table 2, list an implicit LES with Nektar++ by Wang et al. (hp
spectral elements of degree 4 and 7 on meshes of 246 000 and 500 000 cells,
140 flow-throughs, time step 0.001), one of the two earlier
finite-element implicit LES of that case they name, the other being the DG
study of Krank et al. (§1). Prieto Saavedra et al. themselves use the
stabilized finite-element code Lethe, not Nektar++; see
[implicit LES](/definitions/implicit-les.md).

[Witherden et al. (2025)](/sources/witherden-2025.md), §1, name Nektar++
(citing Cantwell et al. 2015 and Moxey et al. 2020) and
[hpMusic](/software/hpmusic.md) as high-order spectral element efforts
"similar to PyFR" among the international efforts to bring scale-resolving
simulation into industry; see [PyFR](/software/pyfr.md).

Saini et al. (2023, §6) attribute the accuracy-per-cost advantage of the
Nektar++ runs over second-order OpenFOAM runs primarily to lower numerical
dissipation, the model playing a secondary role. Slaughter et al. (2023)
obtain $C_L=-8.33$, $C_D=0.17$ and resolve laminar separation bubbles on the
wing; no grid-convergence study or experimental comparison of that slice
case is shown.

## Qualifications

- Ferrer et al. (2023, §2, Table 1) list Nektar++ among the high-order codes
  they compare with HORSES3D (see [HORSES3D](/software/horses3d.md)).
- [Kurz et al. (2025)](/sources/kurz-2025.md), §1, list Nektar++ with
  HORSES3D as spectral element codes that "can solve both the compressible
  and incompressible" Navier–Stokes equations. No study in the bundle runs
  its compressible solver; the solvers recorded here are the incompressible
  and the acoustic one.
- The version of Slaughter et al. read is the Research Square preprint
  (v1); its reference to
  the Nektar++ paper prints a Mendeley Data DOI prefix.
- The polynomial orders are written $P$ (Saini et al.) and "polynomial
  order" or $p$ (Slaughter et al., Moratilla-Vega et al.); they are $N$ here.
  Huang et al. (2022c) print "polynomial order $N_p=7$" and write the
  elemental expansion with $P+1$ GLL points per direction (Eq. 16) without
  relating $P$ to $N_p$; their Table I spacings ($\Delta x\simeq0.087\delta$,
  $\Delta z\simeq0.052\delta$, $\Delta y_1\simeq0.037\delta$) equal the element
  sizes $2\pi\delta/12$, $\pi\delta/10$ and $0.224\delta$ divided by
  $N_p-1=6$, i.e. they match $N=N_p-1$ *(compiler check, not in the
  sources)*. $N_p$ is therefore quoted as printed.
- Huang et al. (2022c, Eqs. 20 and 22) print the wall condition as
  $\partial u/\partial y|_w=\tau_w/(\rho v)$ and "$v_t|_w=0$", with the
  glyph of the wall-normal velocity where the kinematic and eddy viscosities
  stand elsewhere in the paper.

# Citations

- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, Table 1 (solver set-up); §2.2–2.3, Eqs. (6)–(15) (SVV, FieldConvert, FFT convolution); §3, Table 2 (cases, costs); §5–6 (dissipation shares, conclusion).
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — Research Square preprint v1: §3, §3.1 (Fourier spectral/hp, velocity correction, static condensation, IMEX, GJP, SVV); §3.2 (NekMesh); §3.3 (orders, boundary conditions); §3.6, §4.
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §2.2, Eqs. (11)–(12) (AcousticSolver); §2.3 (CWIPI coupling); §3, Table 1; §4.4.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §2, Table 1.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §1, §2.4, Table 2 (Nektar++ implicit LES of the periodic hill by Wang et al., as cited).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §1 (Nektar++ among high-order solvers).
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §I (claim of priority, Neumann choice, Pal et al. as cited); §II A–C, Eqs. (12)–(16), (20) (discretization, SVV, Wang et al. as cited, sampling, wall condition); §III A–E, Table I, Figs. 3–9 (channel set-up, results, cost); §IV.
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §1 (Nektar++ among industrial scale-resolving efforts; passing).
