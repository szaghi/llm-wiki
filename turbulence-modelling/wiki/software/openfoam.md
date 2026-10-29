---
type: Software
title: "OpenFOAM"
description: "OpenFOAM is the open-source unstructured finite-volume toolbox that bundle sources use as baseline RANS solver for data-driven closures, as second-order LES solver, as host of in-house compressible, reacting and two-scale solvers and of a wall-model library, and as reference for high-order codes; this page records the solvers, schemes and versions they report."
status: established
aliases: [OpenFOAM, simpleFoam, pimpleFoam, DAFoam, libWallModelledLES, foam-extend, pUCoupledFoam, rhoCentralFoam, detonationFoam]
tags: [software, rans, les, data-driven, numerical-dissipation, combustion]
timestamp: 2026-10-28T17:51:00Z
---

# OpenFOAM

**OpenFOAM** is an open-source C++ toolbox for unstructured, cell-centred
finite-volume solution of the flow equations. Rismondo et al. (2025) cite it
to Weller et al. (1998). In this bundle it is never the subject of a study.
It runs the baseline RANS of several
data-driven closure papers, the second-order LES that high-order codes are
compared against, and the base of in-house and adjoint solvers. Every
source reports its own solver application, schemes and version. None of
these is a default of the code.

## Solvers and schemes as reported

| Source | Application | Pressure–velocity coupling and schemes | Version |
|---|---|---|---|
| [Rismondo et al. (2025)](/sources/rismondo-2025.md), §2.1 | incompressible LES in a multiple reference frame, [WALE](/methods/wale-model.md) | PISO with two correctors and two non-orthogonal correctors; second-order backward time, Gauss linear (central) space; bi-conjugate gradient for momentum, GAMG for pressure | not printed |
| [Saini et al. (2023)](/sources/saini-2023.md), §2.1 | incompressible LES, WALE ($C_w=0.325$) | `pimpleFoam`, second order | v1712 |
| [Wu et al. (2025)](/sources/wu-2025.md), §2–§3 | steady incompressible RANS, [SST](/methods/k-omega-sst-model.md) | `simpleFoam`; discrete adjoint by DAFoam, Jacobians by automatic differentiation (CoDiPack) | not printed |
| [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §4.1 | steady RANS, SST with blended learned corrections (modified solver) | SIMPLE, linear upwind convection, second-order central viscous terms, Gauss–Seidel smoother | "v23-06" in the text, "Version 10" in the reference list |
| [Tang et al. (2023)](/sources/tang-2023.md), §III | steady RANS, [$k$-$\varepsilon$](/methods/k-epsilon-model.md) with a frozen learned anisotropy | SIMPLE, second-order upwind convection, central otherwise | not printed |
| [McConkey et al. (2022)](/sources/mcconkey-2022.md) | RANS, $k$-$\varepsilon$-$\varphi$-$f$ elliptic relaxation | not printed | v2006 |
| [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md), §3.2 | standard $k$-$\varepsilon$ RANS (`simpleFoam`); WALE LES reference | not printed | not printed |
| [Liu et al. (2024)](/sources/liu-2024.md) | SSG/LRR-$\omega$ [Reynolds-stress model](/methods/reynolds-stress-model.md) coupled to Menter's $\gamma$ model | time-averaged URANS for the 3D cascades, first-order upwind for the turbulence variables and $\gamma$ | not printed |
| [Nuca et al. (2025)](/sources/nuca-2025.md), §VI, App. B | incompressible wall-modelled LES, [$\sigma$ model](/methods/sigma-model.md), libWallModelledLES | `pimpleFoam`, PIMPLE with 1 outer and 4 inner correctors; conjugate gradient for pressure, BiCGStab for velocity; second-order linear convection and diffusion in the turbulent region, blended with second-order upwind convection in laminar and free-stream regions | v2306 |
| [Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §3.1, §3.3 | steady RANS, [SST](/methods/k-omega-sst-model.md), wall value of $\omega$ by `omegaWallFunction` | `simpleFoam` | 12 |
| [Brenner et al. (2022)](/sources/brenner-2022.md), §2.8–2.9, §3.1 | steady incompressible RANS, [$k$-$\varepsilon$](/methods/k-epsilon-model.md) (`kEpsilon`, `nutLowReWallFunction`) with a frozen eddy viscosity scaled by an assimilated field; hand-built discrete adjoint | foam-extend 4.0, block-coupled pressure–velocity solver `pUCoupledFoam` extended with the adjoint; second-order schemes; BiCGStab with Cholesky preconditioning; under-relaxation | foam-extend 4.0 |
| [Cherroud et al. (2022)](/sources/cherroud-2022.md), §3 | steady RANS, SST with learned anisotropy and production corrections (general explicit algebraic stress implementation); BSL-EARSM for comparison | SIMPLE, linear upwind convection, second-order central viscous terms, Gauss–Seidel smoother; grids and settings of Schmelzer et al. (2020a) | not printed |
| [Böttler et al. (2022)](/sources/bottler-2022.md), §2.3 | laminar low-Mach reacting flow with a [flamelet/progress-variable](/methods/flamelet-tabulated-chemistry.md) table (transported H$_2$, O$_2$, H$_2$O and enthalpy); detailed-chemistry reference coupled with Cantera | second order in time and space | not printed |
| [Cheng et al. (2023)](/sources/cheng-2023-b.md), §2 | compressible [implicit LES](/definitions/implicit-les.md) of shock–vortex and shock–turbulence problems (no explicit subgrid model) | AUSM+-up flux; ROUND reconstruction of primitive variables cast as a flux limiter on a compact stencil, against the van Leer and MUSCL limiters; central viscous terms; time integrator not stated | not printed |
| [Fureby & Nilsson (2023)](/sources/fureby-2023.md), §3 | compressible reacting LES, LDKM subgrid model, PaSR finite-rate chemistry | density-based; second-order Kurganov central(-upwind) convective flux, linear diffusive fluxes; operator split, inviscid step explicit, viscous step iterative (Gauss–Seidel); second-order multi-step time integration; Rosenbrock chemistry | not printed |
| [Zhang et al. (2023)](/sources/zhang-2023-c.md), §3.4 | low-Mach reacting LES with flamelet-generated manifolds, presumed-PDF or [thickened-flame](/methods/thickened-flame-model.md) closure, [dynamic Smagorinsky](/methods/dynamic-procedure.md) | PISO; second-order backward time, second-order TVD convection and diffusion; fixed $\Delta t=0.32$ µs (CFL about 0.4) | not printed |
| [Sun et al. (2023)](/sources/sun-2023.md), §2.2 | detonationFoam: compressible multi-component reacting Navier–Stokes or Euler with detailed chemistry, no turbulence model | derived from the density-based `rhoCentralFoam`; HLLC-P flux with second-order MUSCL, central diffusion, first-order implicit Euler for the non-reactive step, operator-split stiff chemistry (seulex); 2D adaptive refinement and dynamic load balancing | not printed |
| [Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §3.4 | P-DNS with a continuous particle method; DPMFoam as Lagrangian reference | PIMPLE; first order in time, second-order FV in space | not printed |
| [Wei et al. (2023)](/sources/wei-2023.md), §II | scramjetFoam: compressible reacting wall-resolved LES, dynamic one-equation [subgrid kinetic-energy model](/methods/subgrid-kinetic-energy-equation-model.md), laminar chemistry closure; `reactingFoam` and `rhoCentralFoam` as comparators | energy-preserving split convective flux with AUSM-type diffusion switched on by a Ducros sensor (threshold 0.05); Jameson-style four-stage Runge–Kutta | 7 |
| [Zhang et al. (2024)](/sources/zhang-2024.md), §2.3 | Spalart–Allmaras-based DDES of a compressor tandem cascade | second-order central convection with least-squares weighting of the flux, second-order backward time, $\Delta t=10^{-6}$ s, mean Courant number 0.65 | not printed |
| [Guo & Wang (2025)](/sources/guo-2025.md), §2.1, §3.1 | SST-based [DDES](/methods/detached-eddy-simulation.md) and the authors' adaptive variants (new classes `kOmegaSSTFDDES`, `adaptiveDelta`), square cylinder, wall functions | first-order implicit Euler; cellLimited Gauss linear gradients (limiter 0.5 on the pressure gradient); linearUpwind convection (limited for $k$, $\omega$); PIMPLE with five outer and two momentum correctors; GAMG for pressure, PBiCGStab for $U$, $k$ | v2306 |
| Guo & Wang (2025), §3.2 | same models, periodic hill, wall functions | second-order backward time; linear upwind convection, limited linear for $k$, $\omega$; Gauss linear corrected diffusion; PIMPLE with one outer and three momentum correctors; GAMG with DIC–Gauss–Seidel smoother | v2306 |
| [De Cosmo et al. (2025)](/sources/decosmo-2025.md), §3.2, §3.4 | incompressible LES references for a compressible implicit-LES code: `pimpleFoam` with [WALE](/methods/wale-model.md) (decaying isotropic turbulence) and with the $k$-equation [subgrid model](/methods/subgrid-kinetic-energy-equation-model.md) (curved-wall channel bump) | Gauss linear gradient, divergence and Laplacian schemes, non-orthogonal correction of the Laplacian; second-order backward time | not printed |

## Roles in the bundle

**Baseline solver of data-driven RANS closures.** The learned corrections
of [field inversion and machine learning](/methods/field-inversion-machine-learning.md),
[symbolic-regression closures](/methods/symbolic-regression-closure.md),
[tensor-basis](/methods/tensor-basis-neural-network.md) and probabilistic
closures are trained and tested in OpenFOAM by several authors:

- Wu et al. (2025) invert a conditioned correction field on the SST
  $\omega$ destruction with DAFoam's discrete adjoint and SLSQP. They then
  test symbolic-regression models in `simpleFoam` on the
  [periodic hill](/benchmarks/periodic-hill.md), the
  [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md), a
  flat plate, the [NACA 0012](/benchmarks/naca-0012-airfoil.md), an SAE
  notchback and the [Ahmed body](/benchmarks/ahmed-body.md). The 3D runs
  use half models of up to $3.3\times10^7$ (notchback) and
  $1.4\times10^7$ (Ahmed) cells (§3, Tables 6–7).
- Oulghelou et al. (2025) blend learned SST corrections inside a modified
  solver ([aggregation of data-driven models](/methods/turbulence-model-aggregation.md)),
  on 2D steady cases including the NASA hump and the NACA 0012. They state
  that the grids are fine enough for the discretization error to be
  negligible against the model effect, and show no grid study (§4.1).
- Tang et al. (2023) and McConkey et al. (2022) inject frozen learned
  anisotropies into the $k$-$\varepsilon$ and $k$-$\varepsilon$-$\varphi$-$f$
  solvers on the periodic hill. Agrawal & Koutsourelakis (2024) train on a
  [backward-facing step](/benchmarks/backward-facing-step.md), with OpenFOAM
  WALE LES as reference data (1,428,920 degrees of freedom).
- [Brenner et al. (2022)](/sources/brenner-2022.md) assimilate sparse
  LES velocity data on the [periodic hill](/benchmarks/periodic-hill.md)
  ($Re=10595$, $180\times130$ cells, first-cell $y^+\approx5$) by
  scaling a frozen $k$-$\varepsilon$ eddy viscosity with a spatial field
  (see [field inversion](/methods/field-inversion-machine-learning.md)).
  Their gradient comes from a discrete adjoint built inside foam-extend
  4.0 rather than by automatic differentiation: the adjoint matrix is the
  transposed converged block-coupled forward matrix, obtained by
  exchanging the lower and upper triangles of the LDU storage, so the
  forward boundary coefficients carry over and no adjoint boundary
  conditions are derived; the parameter Jacobian is assembled with the
  built-in implicit operators from the only field-dependent term, the
  diffusion with the scaled eddy viscosity (§2.1.4, §2.8–2.9). The
  contribution of the pressure residual is dropped because no implicit
  operators are available for it (§2.3). Against finite differences at
  156 cells the gradient differs significantly in some cells and has the
  correct sign for 84% of the field (§3.3, Fig. 8); in their conclusions
  (§4) the authors call the gradients "accurate".
  Each optimization step becomes much cheaper after the first, because the
  forward problem is warm-started (§3.4).
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) run their
  sparse-Bayesian learned SST corrections in a modified OpenFOAM with a
  general explicit algebraic stress implementation (a public repository of
  Schmelzer), on the periodic hill, a converging–diverging channel and a
  curved backward-facing step on the grids of Schmelzer et al. (2020a); the
  solver runs each candidate model for a posteriori cross-validation of the
  sparsity parameter, and propagating the maximum a posteriori model costs
  one run (§2, §3, Conclusions). In App. C the learned single-term models
  are almost as robust and cheap as SST and better than OpenFOAM's
  BSL-EARSM (see
  [explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)).
- Liu et al. (2024) implement the SSG/LRR-$\omega$ model with Menter's
  one-equation $\gamma$ model in OpenFOAM, and test it on the
  [ERCOFTAC T3](/benchmarks/ercoftac-t3-flat-plate.md) plates and on
  [compressor cascades](/benchmarks/compressor-cascade.md) (see
  [local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)).

**Second-order LES and its dissipation.** Saini et al. (2023) give the
sharpest quantitative statement on OpenFOAM's numerical dissipation in
LES. On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) the
discretization supplies 65–75% of the non-viscous dissipation in OpenFOAM,
against 85–95% in [Nektar++](/software/nektar-plus-plus.md), and the
normalized total non-viscous dissipation of the second-order runs is 1–4
times the viscous one. On a
combustor port flow the equivalent numerical viscosity is 10–23 times the
molecular viscosity on 16M cells and 8–15 times on 48M cells, against 2.5–7
for an equal-cost spectral/hp run (§5, Table 2). They attribute the
accuracy-per-cost gap mainly to numerical dissipation, the model playing a
secondary role (see [numerical dissipation](/properties/numerical-dissipation.md)).
Rismondo et al. (2025) run a wall-resolved WALE LES of a model wind turbine
on about 144 million cells. It is the source of a
[Ffowcs Williams–Hawkings](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
noise computation. They claim second-order accuracy "in both space and
time" and give no grid-convergence study. Their maximum Courant number is
about 10 in a few cells near the blade tips, with an average of about 0.017
(§2.1, §2.3).

**Compressible in-house solvers.** Two sources build compressible
scale-resolving solvers inside OpenFOAM.

- [Cheng et al. (2023)](/sources/cheng-2023-b.md) state that OpenFOAM's
  performance on shock–vortex and shock–turbulence problems "is limited by
  the available solvers which are using conventional second-order schemes"
  (§1), and implement the ROUND reconstruction "with rigorously adjusted
  dissipation" (parameter sets ROUND_A and ROUND_A+) with the AUSM+-up
  flux in an implicit-LES solver. To fit OpenFOAM's face-based
  unstructured framework they rewrite the reconstruction as a flux-limiter
  function of a gradient ratio, which avoids the virtual cell values of the
  original form (§2.2, Eqs. 2.12–2.14). Against the van Leer and MUSCL
  limiters, "widely used TVD schemes" in OpenFOAM, ROUND keeps more
  small-scale structure on inviscid shock and vortex tests and, on a
  transonic deep cavity ($M=0.8$, $Re=8.6\times10^5$ on the cavity length,
  10.36 million cells, smallest cell $1/120$ of that length, 60 shedding
  cycles), gives Reynolds stresses closer to experiment; the classical TVD
  limiters under-predict them, while the fifth-order MUSCL implicit LES of
  Thornber & Drikakis, on a different grid, "tends to slightly overestimate
  them" (§3.6, Figs. 11–14). No time integrator, CFL number or timing is
  given. See [implicit LES](/definitions/implicit-les.md) and
  [numerical dissipation](/properties/numerical-dissipation.md).
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) run their
  compressible reacting-flow LES of a cavity-stabilized dual-mode ramjet
  with "the density-based FVM, implemented in openFOAM" (§3.4): the
  localized dynamic $k_{\mathrm{sgs}}$-equation model (see
  [one-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)),
  gradient-diffusion subgrid fluxes, the partially stirred reactor model
  for the filtered reaction rates and a no-slip subgrid wall model, on
  hexahedral grids of 7.3, 24.6 and 57.8 million cells that resolve 90%,
  94% and 96% of the turbulent kinetic energy (§6.2). They name artificial
  diffusivity and hybrid schemes as alternatives for discontinuities and
  use neither (§3.4).

**An energy-preserving supersonic film-cooling solver.**
[Wei et al. (2023)](/sources/wei-2023.md) build scramjetFoam on OpenFOAM 7
for wall-resolved LES of the Burrows–Kurkov supersonic hydrogen film
(Mach 2.44 vitiated mainstream, sonic tangential slot), with an implicit
grid filter $\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$. Its convective flux
is split into a convective and a pressure part, discretized in the
discretely energy-preserving form of Pirozzoli and of Modesti & Pirozzoli
(which they cite), and AUSM-type numerical diffusion is added only where a
Ducros sensor exceeds 0.05 (§II C, Eqs. 16–19; see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
and [shock sensors](/definitions/shock-sensor.md)). The subgrid closure is
the dynamic one-equation $k_{\mathrm{sgs}}$ model with constant subgrid
$Pr_t=0.85$ and $Sc_t=0.7$ (§II B; see
[turbulent Prandtl number](/definitions/turbulent-prandtl-number.md)), and
the inflow uses synthetic eddies on a RANS precursor
([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).

- *Against the shipped solvers.* On the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on a $64^3$
  mesh without subgrid model, scramjetFoam keeps the volume-averaged
  kinetic energy constant "over a long duration", while `reactingFoam` and
  `rhoCentralFoam`, both configured second order, dissipate it "to 65% and
  30% of the initial value"; scramjetFoam "can reasonably track the growth
  trend of enstrophy" of the Brachet et al. solution and the two shipped
  solvers do not (§III A, Fig. 4). The authors call the dissipation of
  these second-order solvers possibly "unacceptable for LES application";
  see [numerical dissipation](/properties/numerical-dissipation.md).
- *Resolution.* About $7.4\times10^6$ structured cells with a first cell at
  $y^+\approx0.6$, $\Delta x^+=120$, $\Delta z^+=40$, $\Delta y^+<60$; 99.5%
  of the cells of a boundary-layer test resolve more than 80% of the
  turbulent kinetic energy by Pope's criterion, the rest lying in the
  viscous sublayer (§II E, §III B, Fig. 6).

**A compressor-cascade DDES.** [Zhang et al. (2024)](/sources/zhang-2024.md)
run Spalart–Allmaras-based
[delayed DES](/methods/detached-eddy-simulation.md) of the tip-leakage flow
of a NACA 65-K48 tandem
[compressor cascade](/benchmarks/compressor-cascade.md) in OpenFOAM, on
about 6.65 million cells over half the span with a mid-span symmetry plane
(§2.2–2.3); the schemes are in the table above.

**Reacting flows: a turbulent-flame LES and a laminar detonation solver.**
Two sources build reacting-flow solvers in OpenFOAM.

- [Zhang et al. (2023)](/sources/zhang-2023-c.md) run an LES of the
  Darmstadt multi-regime burner (stratified methane/air, flame MRB26b) with
  tabulated flamelet-generated manifolds in an OpenFOAM LES-FGM solver, on
  about 3.87 million hexahedra, a mesh coarser than that of the earlier
  LES of Popp et al., who provided it with the boundary conditions, with 20
  flow-through times after ignition and 20 more for statistics (§2, §3.4).
  The cold-flow mesh resolves at least 80% of the turbulent kinetic energy
  by the Pope criterion (§2). Their flame sensor and minor-species
  correction are on the [thickened flame model](/methods/thickened-flame-model.md);
  the chemistry tables on
  [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).
- [Sun et al. (2023)](/sources/sun-2023.md) present detonationFoam, an
  open-source (GPLv3) OpenFOAM solver for gaseous detonation, built on
  `rhoCentralFoam` with five changes: species transport with detailed
  finite-rate chemistry, a mixture-averaged transport model (Wilke and
  Mathur mixing rules, thermal diffusion), the HLLC-P approximate Riemann
  solver with MUSCL reconstruction, two-dimensional adaptive mesh
  refinement and the dynamic load balancing of DLBFoam (§1, §2.2, §4). They
  state that the earlier `rhoCentralFoam`-based detonation solvers use the
  Sutherland law, so that multi-species transport "cannot be accurately
  predicted" (§1), and that OpenFOAM's own adaptive refinement supports only
  hexahedra in 3D and is "not appropriate for 2D detonation simulation";
  their 2D version refines a cell into four on a threshold of the density
  gradient and coarsens with conservative averaging (§2.2.2, Table 1; see
  [mesh adaptation](/methods/mesh-adaptation.md)). On a wedge-stabilized
  oblique detonation the refinement cuts the cell count to about 1/6 and
  refinement with load balancing the CPU time to about 1/5 of a uniform
  mesh without balancing, with nearly identical steady structures (§3.9,
  Figs. 15–16; no hardware or core count printed). The HLLC-P flux is
  shown less dissipative at a shock than the KNP and HLLC fluxes of
  OpenFOAM on a 1D shock tube (§3.3, Fig. 5). All test cases are laminar
  or inviscid; the paper contains no turbulence modelling.

**Wall-modelled LES with libWallModelledLES.** [Nuca et al. (2025)](/sources/nuca-2025.md)
implement their explicit (non-iterative) forms of the Spalding, Reichardt
and equilibrium-ODE wall models in libWallModelledLES, the OpenFOAM
wall-modelling library of Mukha et al. (2019), which they cite, and run
wall-modelled LES of the Aérospatiale A-airfoil near stall in the
configuration of Tamaki & Kawai (2023), which they cite: a structured C-grid of
$18.7\times10^6$ cells, 40 across the span, 10–12 cells across the local
boundary-layer thickness, the wall model on the whole suction side,
statistics over one convective time $c/U_\infty$, which the authors call
insufficient for converged statistics (§VI, App. B). They report, from
their own and the library's users' experience, that the Newton inversion
of Spalding's law "would often sporadically diverge" in complex flows,
particularly when the sampling height exceeds the first off-wall cell
(§I). On the airfoil the iterated count rises near transition; used as
initial guesses, the explicit forms cut the maximum Newton count from 11
to 3 (Reichardt) and 10 to 3 (Spalding), and the equilibrium-ODE
fixed-point maximum from 100 (the iteration cap, i.e. non-convergence) to
6 (Table VIII). Wall modelling takes about 2% of the run time with the
algebraic models, 1.8–1.9% with the explicit ones (a difference the
authors do not call statistically significant over the short averaging)
and 11.9% with the integrated equilibrium ODE (§VI; Shaheen III, no
further hardware detail).
Their a priori channel test uses an OpenFOAM wall-resolved LES at
$Re_\tau\approx1000$ from the same group. See
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[wall-modelled LES](/methods/wall-modelled-les.md).

**Wall-modelled LES, as cited.** [Mukha et al. (2025)](/sources/mukha-2025.md),
§II.C.4, §IV.B, state that the viscosity-based wall-stress condition
(no-slip plus a wall eddy viscosity that reproduces the modelled stress)
"has long been used in OpenFOAM". They cite an earlier OpenFOAM WMLES of
a flat-plate boundary layer, at about 2 cells per boundary-layer thickness,
as less accurate than their spectral-element results. In
[Nek5000](/software/nek5000.md) the same condition fails (see that page and
[wall-modelled LES](/methods/wall-modelled-les.md)).
[Gao et al. (2025)](/sources/gao-2025.md), §III.A.2, Fig. 10, compare the
wall-pressure spectra of their slip-wall WMLES in a fourth-order
dispersion-relation-preserving finite-difference code
($127\times41\times95$ points) with an OpenFOAM WMLES of Fan et al. at
$Re_\tau=1000$ ($127\times101\times127$), which shows "a spurious
spectral peak, larger amplitude discrepancies, and premature decay in the
mid-frequency range"; they attribute the difference to "inherent
limitations of conventional low-order numerical schemes" (their wall
treatment is on [slip-wall models](/methods/slip-wall-model.md)).

**A hybrid RANS/LES model implemented as OpenFOAM classes.**
[Guo & Wang (2025)](/sources/guo-2025.md), §2.1, Fig. 1, implement their
adaptive SST-based DDES variants in OpenFOAM-v2306 as a turbulence-model
class `kOmegaSSTFDDES`, derived from `kOmegaSSTDDES` by modifying
`correctNut()` (eddy-viscosity filtering), and a new `LESdelta` class
`adaptiveDelta` that switches between the largest cell dimension and the
least-squares subgrid length of Trias et al., compiled with `wmake`; they
call the implementation "lightweight and compatible with other hybrid
RANS/LES models in the same framework" (code on request). Their wall
treatment uses OpenFOAM's `kqRWallFunction`, `nutUSpaldingWallFunction`
(Spalding's law) and `omegaWallFunction` (§2.2.2, Eqs. 17–20; see
[wall functions for RANS](/methods/rans-wall-function.md)). Runs: a
[square cylinder](/benchmarks/square-cylinder-flow.md) at $Re=21\,400$ on
about 4.08 million cells (about 288 core-hours on 64 cores) and the
[periodic hill](/benchmarks/periodic-hill.md) at $Re_h=10\,565$ on
$200\times160\times160$ points (about 75 h on 48 cores); the time step is not
given (§3.1–§3.2). The model is on
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

**Incompressible LES as reference for a compressible implicit LES.**
De Cosmo et al. (2025) compare their low-dissipation Roe finite-volume code
Zephyrus, run as [implicit LES](/definitions/implicit-les.md), with
OpenFOAM LES on the same domains: on Comte-Bellot–Corrsin decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
($32^3$ to $128^3$ cells) both reproduce the $-5/3$ range and depart from
it only near the Nyquist limit, with differences "qualitatively negligible"
and OpenFOAM "slightly less dissipative" (§3.2, Fig. 4); on the
curved-wall bump in a [channel](/benchmarks/turbulent-channel-flow.md) of
Banchetti et al. the OpenFOAM pressure coefficient is "practically
coincident" with the DNS, and, with no DNS fluctuations available, the
OpenFOAM Reynolds stresses serve as the guideline for the implicit LES
(§3.4, Figs. 14, 16).

**Finite-volume reference for a high-order RANS code.**
Tomboulides et al. (2025) run OpenFOAM SST beside their spectral element
$k$-$\tau$ and regularized $k$-$\omega$ models in [Nek5000](/software/nek5000.md)
([$k$-$\tau$ model](/methods/k-tau-model.md)). In a channel at
$Re_\tau\approx5200$ (104 cells across) OpenFOAM gives $u_\tau=0.0409$
against 0.0412–0.0415 for the Nek5000 models and 0.0415 from DNS (§3.1,
Table 1). On the Driver–Seegmiller
[backward-facing step](/benchmarks/backward-facing-step.md) (meshes of
10,468, 41,872 and 165,072 cells, the first two matched in degrees of
freedom to Nek5000 at $N=2$ and 4) the fine-mesh reattachment length is
$6.44H$ against $6.48H$ ($k$-$\tau$) and $6.26H$ measured; OpenFOAM SST
under-predicts $C_f$, "a known behavior of the SST model", and the authors
find the Nek5000 $C_f$ profiles more consistent at comparable resolution
(§3.3, Figs. 9–12). The inlet $\omega$ of the OpenFOAM step is the Nek5000
regularized remainder plus the analytical wall part
$6\nu/(\beta_\omega d^2)$ ($\beta_\omega$ the destruction coefficient of
the $\omega$ equation, $d$ the wall distance).

**Other uses.** Steinhausen et al. (2023, §2.1) run DNS of side-wall
flame quenching with an in-house finite-rate chemistry solver, OpenFOAM-based
according to the titles of the works they cite for it, of fourth order in space and second order in time
([direct numerical simulation](/definitions/direct-numerical-simulation.md)).
Domingo & Vervisch (2023, §1) list OpenFOAM among the DNS codes of second
or fourth order. Böttler et al. (2022, §2.3) implement their
flamelet/progress-variable model for laminar hydrogen–air ignition and
flame propagation in an OpenFOAM framework (low-Mach, second order in time
and space). Their 2D counterflow reference with detailed chemistry runs in
OpenFOAM coupled with Cantera. The planar and curved 1D references use
other codes (ULF, A-SURF). They state, without timings, that the tabulated
model cuts the cost "by an order of magnitude" although it only halves the
number of transport equations (§3). None of their cases is turbulent. Goc et al. (2021, §1, §4) quote an OpenFOAM
Spalart–Allmaras RANS of the Third High-Lift Prediction Workshop on 109
million cells at about $60\times10^3$ core-hours, about the cost of their
medium-grid WMLES ([Spalart–Allmaras model](/methods/spalart-allmaras-model.md),
[CharLES](/software/charles.md)).
[Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §3.4, write that "the
P-DNS implementation here presented uses OpenFOAM as the core library"
for their continuous particle method of particle-laden flow, and take the
reference solutions from OpenFOAM's Lagrangian DPMFoam solver so that both
run "in the same platform"; both use PIMPLE pressure–velocity coupling,
first-order time integration and second-order finite volumes in space (see
[pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md)).
The review of conditional source-term estimation by
[Salehi et al. (2024)](/sources/salehi-2024.md) cites a premixed CSE
implementation in OpenFOAM, CSE routines with hash tables, and LES of a
buoyant methane line flame with the fireFoam solver (see
[conditional source-term estimation](/methods/conditional-source-term-estimation.md)).
The AI-in-turbulence review of [Fang et al. (2026)](/sources/fang-2026.md)
cites a mixed-precision study of OpenFOAM among HPC developments and the
curated RANS and DNS/LES dataset of McConkey et al., which ships OpenFOAM
set-ups (as cited there).

## Qualifications

- Oulghelou et al. (2025) give two version labels for the same solver
  (§4.1 against ref. [57]), and do not say how compressibility is handled
  in their near-sonic jet case, which runs in an incompressible-form
  solver.
- Rismondo et al. (2025, Eq. 2.2) write the subgrid term as
  $+\partial_j\tau_{ij}$ without defining $\tau_{ij}$; for Eq. (2.2) to
  hold, their $\tau_{ij}$ is the negative of the registry's positive-trace
  $\tau_{ij}$, as their Source page's Notation map records.
- Brenner et al. (2022) run foam-extend 4.0 and list OpenFOAM among their
  keywords; their adjoint relies on the block-coupled `pUCoupledFoam`
  solver of foam-extend. Their Fig. 8 caption swaps the subscripts of the
  adjoint and finite-difference gradients relative to the axis labels.
- Cheng et al. (2023, §3.6) compare their deep-cavity statistics on
  10.36 million cells (finer mesh following their ref. 47) with the
  fifth-order MUSCL implicit LES of Thornber & Drikakis on that study's
  own grid, and write that some of their mean-velocity results "may
  benefit from the finer grid size"; Fureby & Nilsson (2023) cite the
  Kurganov central scheme to a paper on the semidiscrete central-upwind
  scheme.
- Guo & Wang (2025) give no time step, no grid-convergence study (they
  refer to their earlier paper for the cylinder grid) and no cost
  comparison among their four model variants; their wall-function
  constants $E$, $\kappa$ and $C_\mu$ are not printed.
- Cost and accuracy statements on this page are those of each study's
  set-up (mesh, schemes, model). None isolates OpenFOAM from its
  configuration.

- [Sun et al. (2023)](/sources/sun-2023.md) state, without showing it,
  that second-order time schemes have "little influence on the results
  due to the very small time step in the order of $10^{-9}$ s" (§2.2.1).
  [Zhang et al. (2023)](/sources/zhang-2023-c.md) give no OpenFOAM version
  and no Reynolds number of the burner.
- Wei et al. (2023) attribute part of the enstrophy error of all three
  solvers to grid resolution and add that an enstrophy-conserving scheme is
  harder to implement in finite volume (§III A). Zhang et al. (2024) name
  neither the OpenFOAM solver application nor the version.

# Citations

- [Rismondo et al. (2025)](/sources/rismondo-2025.md) — §2.1, Eqs. (2.1)–(2.2) (LES solver and schemes); §2.3 (mesh, Courant number).
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, Table 1 (pimpleFoam v1712, WALE); §3, Table 2 (costs); §5–6 (dissipation shares).
- [Wu et al. (2025)](/sources/wu-2025.md) — authors' manuscript: §2 (DAFoam discrete adjoint, CoDiPack, SLSQP); §3, Tables 6–7 (simpleFoam test cases).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §4.1 (modified solver, schemes, version); §4 (test cases).
- [Tang et al. (2023)](/sources/tang-2023.md) — §II A, §III, Table I (k-ε baseline, SIMPLE, schemes).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — Eqs. (10)–(16) (k-ε-φ-f model in OpenFOAM v2006).
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §3.2, §3.4 (simpleFoam baseline, WALE LES reference).
- [Liu et al. (2024)](/sources/liu-2024.md) — Eqs. (1)–(21), "Flow solvers" (SSG/LRR-ω with γ in OpenFOAM).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.C.4, §IV.B (viscosity-based wall condition and OpenFOAM WMLES, as cited).
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — §2.1 (OpenFOAM-based DNS solver).
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §1 (OpenFOAM among DNS codes).
- [Goc et al. (2021)](/sources/goc-2021.md) — §1, §4 (OpenFOAM SA RANS cost reference).
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I (Newton divergence in libWallModelledLES practice); §VI, Table VIII, App. B (A-airfoil set-up, iteration counts, cost); §VI (OpenFOAM channel LES data).
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.1, Table 1 (channel, OpenFOAM v12 SST); §3.3, Figs. 9–12 (backward-facing step meshes and results).
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §2.1.3–2.1.4, §2.3, §2.8–2.9 (discrete adjoint in foam-extend 4.0, LDU transposition, built-in operators for the parameter Jacobian, dropped pressure term); §3.1, §3.3–3.4, Fig. 8 (periodic hill set-up, gradient check, warm start); §4.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §2 (a posteriori cross-validation in OpenFOAM); §3 (modified OpenFOAM, schemes, grids); App. C (BSL-EARSM comparison); Conclusions (cost of propagating the MAP model).
- [Böttler et al. (2022)](/sources/bottler-2022.md) — §2.3 (OpenFOAM flamelet/progress-variable solver, OpenFOAM–Cantera reference); §3 (stated cost reduction).
- [Cheng et al. (2023)](/sources/cheng-2023-b.md) — §1 (limits of OpenFOAM's shipped solvers); §2.1–2.2, Eqs. (2.7)–(2.14) (AUSM+-up, ROUND as flux limiter, primitive-variable reconstruction); §3.6, Figs. 9–14 (deep cavity).
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §3.2–3.4, Eqs. (5)–(8) (density-based FVM in OpenFOAM, LDKM, PaSR, Kurganov flux, operator split, Rosenbrock); §6.2 (grids, resolved kinetic energy).
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §3.4 (OpenFOAM as P-DNS core library, DPMFoam reference, PIMPLE, discretization orders).
- [Zhang et al. (2023)](/sources/zhang-2023-c.md) — §2 (mesh, Pope criterion); §3.4 (OpenFOAM LES-FGM solver, schemes, time step, averaging).
- [Sun et al. (2023)](/sources/sun-2023.md) — §1 (rhoCentralFoam-based solvers, OpenFOAM AMR); §2.2, Table 1 (detonationFoam numerics, 2D AMR, load balancing); §3.3, Fig. 5 (HLLC-P against KNP and HLLC); §3.9, Figs. 15–16 (AMR and load-balancing efficiency); §4.
- [Wei et al. (2023)](/sources/wei-2023.md) — §II A–C, Eqs. (12)–(19) (scramjetFoam: subgrid model, split flux, Ducros-switched AUSM diffusion); §II E (grid); §III A, Fig. 4 (inviscid Taylor–Green against reactingFoam and rhoCentralFoam); §III B, Fig. 6 (resolved-energy fraction).
- [Zhang et al. (2024)](/sources/zhang-2024.md) — §2.2–2.3 (OpenFOAM DDES set-up, schemes, time step).
- [Guo & Wang (2025)](/sources/guo-2025.md) — §2.1, Fig. 1 (OpenFOAM-v2306 classes `kOmegaSSTFDDES`, `adaptiveDelta`); §2.2.2, Eqs. (17)–(20) (OpenFOAM wall functions); §3.1–§3.2 (schemes, solvers, meshes, cost).
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) — §3.2, Fig. 4 (pimpleFoam WALE reference in decaying isotropic turbulence); §3.4, Figs. 14, 16 (pimpleFoam $k$-equation LES reference on the curved-wall bump).
- [Salehi et al. (2024)](/sources/salehi-2024.md) — review: OpenFOAM implementations of CSE and fireFoam LES, as cited (passing).
- [Fang et al. (2026)](/sources/fang-2026.md) — review: mixed-precision OpenFOAM and the McConkey et al. dataset with OpenFOAM set-ups, as cited (passing).
- [Gao et al. (2025)](/sources/gao-2025.md) — §III.A.2, Fig. 10 (OpenFOAM WMLES of Fan et al. as a low-order comparison, cited).
