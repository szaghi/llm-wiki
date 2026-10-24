---
okf_version: "0.1"
---

# weno-teno — Knowledge Bundle

High-order discretizations of hyperbolic conservation laws and compressible
flows, as collected in a research bibliography of 2021–2026: nonlinear
reconstruction (WENO and its variants, TENO, CWENO, THINC hybrids, compact
and learned schemes), numerical fluxes and central-upwind schemes,
discontinuous Galerkin and its entropy-stable and limited forms, bound
preservation, Active Flux, and the benchmarks they are tested on.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($\bar u_i$ cell averages, $u^\mp_{i+1/2}$ the left and right states,
$\hat f_{i+1/2}$ the numerical flux, $d_k$, $\beta_k$, $\alpha_k$, $\omega_k$ the
linear weights, smoothness indicators and nonlinear weights, $q$ their
exponent, $\tau$ the WENO-Z global indicator, $C_T$ and $\delta_k$ the TENO
cut-off, $N$ the DG degree, $(\eta,F_\eta)$ the entropy pair), and the
[update log](/log.md).

**Corpus:** all 11 chunks ingested (204 of 207 sources; feng-2026, li-2024 and wu-2023
await a re-download, see `INGESTION-ISSUES.md`). Chunk 1, the reviews and the
papers that fix the vocabulary: the TENO review of
[Fu (2023)](/sources/fu-2023.md), the geometric quasilinearization of
[Wu & Shu (2023)](/sources/wu-2023-b.md), the compact-stencil framework of
[Deng (2023)](/sources/deng-2023.md) and its sequel
[Huang et al. (2026)](/sources/huang-2026.md), affine-invariant, alternative,
WENO-Z+ and WENO-ZN weights, very-high-order and alternative-formulation TENO,
TENO-THINC, fluctuation-form finite-difference WENO, central-upwind schemes,
entropy-stable DG and its performance, subcell limiting, OEDG, optimal
cell-average decomposition, WENO-stabilized continuous finite elements,
Active Flux and kinetic-energy-preserving discretizations. Chunk 2 (2021–2022 papers):
multi-resolution and Hermite WENO, WLS-ENO, CWENO interface capturing,
sparse invariant-domain-preserving DG, entropy-stable DGSEM for multicomponent
flows and resistive MHD, TeCNO and moving-mesh entropy-stable finite differences,
implicit shock tracking, Quinpi, semi-Lagrangian WENO, well-balanced and
asymptotic-preserving central schemes, positivity-preserving WCNS and the MFC
multiphase solver. Chunk 3 (2021–2022 papers): flux reconstruction and its
entropy filtering and time-reversibility viscosity, entropy correction terms,
WENO limiters for DG, data-driven shock capturing and WENO3-NN, quasi-spectral
viscosity, entropy-stable moving meshes for relativistic MHD, path-conservative
A-WENO, WCNS-T, kinetic-energy-preserving splittings, bound-preserving DG for
reacting flows, physical-constraint-preserving WENO for relativistic flows, and
multiphase, combustion and immersed-boundary solvers. Chunk 4 (2022–2024 papers):
TENO variants (TENO-M, unstructured, five-point adaptive), RBF-WENO, MDCD and
scale sensors, scale-invariant multi-resolution A-WENO with gravity, Hermite and
positivity-preserving finite-difference WENO for Navier–Stokes, a shock-stable
HLLEM, HOIST shock tracking, immersed boundaries for flux reconstruction,
p-adaptive DG, residual viscosity for MHD, semi-implicit all-Mach IMEX schemes, an
asymptotic-preserving kinetic scheme, divergence-preserving AMR prolongation, and
the IDEFIX code. Chunk 5 (2023 papers): gradient-based reconstruction and
α-damping viscous fluxes, wall-modelled LES with hybrid TENO, pressure-equilibrium-preserving
split forms, entropy filtering for MHD, entropy-stable two-fluid relativistic plasma
schemes, shock-capturing multi-block boundary closures, optimized WCNS, all-Mach MHD,
a polynomial-viscosity-matrix solver for radiation MHD, high-order immersed boundaries and
boundary gradients, and the GPU solvers ADAM, URANOS, STREAmS-2.0 and JAX-Fluids. Chunk 6 (2023
papers): exponential WCNS weights, hybrid multi-resolution WCNS, spatio-temporal MDCD
schemes, IMWENO-P, flux globalization for moving equilibria, HLL-GRP for MHD, gas-kinetic
schemes, asymptotically entropy-conservative and pressure-equilibrium-preserving fluxes,
entropy-stable DG for reacting air and with positivity for Navier–Stokes, hybrid DG–FV,
phase-field, discrete-equations and phase-change interface methods, WENO remapping,
smooth adaptive meshing and Cartesian-grid Active Flux with AMR. Chunk 7 (2023–2024
papers): TENO-AZ, TENO-S and dual-selection TENO, learned WENO5-NN weights, a TENO
limiter for Hermite-WENO DG, relativistic Hermite WENO with positivity, fourth-order
upwind constrained transport, monolithic convex limiting, ADER with reconstruction for
off-site data and quasi-conservative multimaterial schemes, entropy filtering for
multicomponent flows, an evolving artificial-viscosity field (TENET), staggered
well-balanced schemes, singular-source Riemann solvers, a Lagrangian particle WENO-Z+,
an all-Mach THINC, and immersed boundaries, OpenFOAM and overset solvers for hypersonic
and multiphase flows. Chunk 8 (2024 papers): ghost, modified and hybrid multi-resolution WENO
with parameter-free troubled-cell indicators, adaptive linear weights on triangles,
scale-adaptive TENO6, RBF-based TENO, incremental-stencil WENO with THINC for
five-equation multiphase flows, THINC-BVD for cavitating two-phase flows,
oscillation-eliminating Hermite WENO, adaptive-TENO limiting for spectral difference,
hybrid DG limiters, entropy-bounded subcell limiting for DGSEM, GQL bound-preserving
central DG for relativistic MHD, Active Flux by bicharacteristics, cost-efficient
high-order constrained-transport MHD, all-Mach visco-resistive MHD, multi-dimensional
well-balanced shallow water, space-time implicit shock tracking, optimal-transport mesh
adaptation and spectral relaxation against tygers. Chunk 9 (2024–2026 papers): the
PAMPA scheme, tensor-train WENO, AENO reconstruction for ADER, Hermite WENO on a single stencil set,
hybrid reconstruction with a discontinuity feedback factor, adaptive low-dissipation and LCD
path-conservative central-upwind schemes, entropy projection on Gauss and uncollocated nodes,
Bassi–Rebay viscous terms with entropy projection, nonlinearly stable flux reconstruction,
DG as subcell finite volumes with a posteriori correction, positivity and entropy bounds for
reacting Navier–Stokes, OEDG for the five-equation model, divergence-free positivity-preserving
finite volumes for MHD, force-free splitting and resistive relativistic MHD, the ROUND scheme on
non-uniform grids, STREAmS-2.1, an incompressible MHD dynamo code and hypocoercive
relaxation analysis. Chunk 10 (2025–2026 papers): converged ENO for steady
states, TENO with an adaptive cut-off and a variance indicator, learned WCNS weights and learned
MUSCL slopes, deepMTBVD, MR-WENO with spectral analysis against the carbuncle, a TENO-THINC
limiter for DG, sign-preserving WENO for TeCNO, the APEC pressure-equilibrium flux, entropy-stable
and divergence-free DG for MHD with the Godunov–Powell term, a new LDCU, arbitrary-order and
flux-vector-split Active Flux with bound preservation and for Vlasov–Poisson, all-Mach and
low-Mach finite elements, a positivity-preserving immersed-boundary TENO and the MFC 5.0 code.
Chunk 11 (2023–2026 papers): the COS(DG) oscillation suppression, Wang, Don & Wang's AWENO
with adaptive Lax–Friedrichs dissipation, learned entropy-stable fluxes, low-dissipation
high-order AMR with WENO transfers, and the AthenaK code. The [Sources](/sources/index.md)
index lists what is in; a whole-bundle deep lint closed the archive.

## Reading guide

**1. Reconstruction.** Begin with the
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
(point values, flux reconstruction, and its relation to finite volumes; the
[cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)
bridges the two) and the
[WENO-JS reconstruction](/methods/weno-js-reconstruction.md), with its
[smoothness indicators](/definitions/smoothness-indicator.md), the
[ENO property](/definitions/eno-property.md) and
[accuracy at critical points](/properties/critical-point-accuracy.md). The
weight families follow: [WENO-Z](/methods/weno-z.md),
[WENO-Z+ and WENO-Z+M](/methods/weno-z-plus.md),
[WENO-ZN](/methods/weno-zn.md), [mapped WENO](/methods/mapped-weno.md),
[affine-invariant weights](/methods/affine-invariant-weno.md) (with
[scale and affine invariance](/properties/scale-invariance.md)),
[WENO-CU6](/methods/weno-cu6.md), [WENO-AO](/methods/weno-ao.md),
[multi-resolution WENO](/methods/multi-resolution-weno.md), [incremental-stencil WENO](/methods/incremental-stencil-weno.md), [WLS-ENO](/methods/wls-eno.md),
[CWENO](/methods/cweno.md), [Hermite WENO](/methods/hermite-weno.md),
[hybrid central-WENO schemes](/methods/hybrid-weno.md) and
[learned WENO weights](/methods/learned-weno-weights.md), with
[RBF-based WENO](/methods/rbf-weno.md), [AENO reconstruction](/methods/aeno-reconstruction.md),
[tensor-train WENO](/methods/tensor-train-weno.md), [converged ENO](/methods/converged-eno.md),
[sign-preserving WENO](/methods/sign-preserving-weno.md) and the
[MDCD schemes](/methods/mdcd-scheme.md) driven by
[scale sensors](/definitions/scale-sensor.md). The
[semi-Lagrangian finite-volume WENO](/methods/semi-lagrangian-finite-volume.md)
reconstructs on Lagrangian cells, and
[gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)
builds second-order finite volumes.
[Gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
reuses compact-scheme gradients for the interface states, with the
[monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md)
at discontinuities, and the
[shock-capturing boundary closure](/methods/shock-capturing-boundary-closure.md)
keeps multi-block finite differences globally conservative.
[Exponential nonlinear weights](/methods/exponential-nonlinear-weights.md) are designed for
optimal order at critical points, and
[RBF differential-quadrature finite volumes](/methods/rbf-differential-quadrature.md)
reconstruct on unstructured meshes.
The [alternative WENO](/methods/alternative-weno.md) formulation interpolates
values instead of reconstructing fluxes, as do the
[weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md).

**2. TENO and interface sharpening.** [Targeted ENO](/methods/targeted-eno.md)
replaces weighting by a sharp cut-off; [adaptive TENO](/methods/adaptive-teno.md)
and [AFTENO](/methods/afteno.md) extend it.
[THINC reconstruction](/methods/thinc-reconstruction.md) and the
[boundary variation diminishing](/definitions/boundary-variation-diminishing.md)
principle lead to [TENO-THINC](/methods/teno-thinc.md). The compact-stencil view
of [Deng (2023)](/sources/deng-2023.md) organises reconstructions on the
[normalised-variable diagram](/definitions/normalised-variable-diagram.md),
against [TVD limiters](/definitions/total-variation-diminishing.md), and
yields the [ROUND schemes](/methods/round-scheme.md).

**3. Fluxes and characteristic projection.** The
[Lax–Friedrichs flux and flux splitting](/methods/lax-friedrichs-flux.md), the
[HLL-family Riemann solvers](/methods/hll-riemann-solvers.md), the
[Roe solver](/methods/roe-riemann-solver.md), the
[polynomial viscosity matrix solvers](/methods/polynomial-viscosity-matrix-solver.md),
[generalized Riemann problem solvers](/methods/generalized-riemann-problem.md),
[gas-kinetic schemes](/methods/gas-kinetic-scheme.md),
[Riemann solvers with phase change](/methods/phase-change-riemann-solver.md), the
[α-damping viscous flux](/methods/alpha-damping-viscous-flux.md), the
[Rankine–Hugoniot condition](/definitions/rankine-hugoniot-condition.md) and the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md), probed by
[matrix stability analysis](/methods/matrix-stability-analysis.md);
[flux vector splitting](/methods/flux-vector-splitting.md);
[characteristic decomposition](/methods/characteristic-decomposition.md);
[central-upwind schemes](/methods/central-upwind-scheme.md), their
[LCD variant](/methods/lcd-central-upwind-scheme.md), the
[low-dissipation central-upwind schemes](/methods/low-dissipation-central-upwind-scheme.md) and the
[adaptive-diffusion Rankine–Hugoniot flux](/methods/adaptive-diffusion-central-upwind-flux.md);
[unstaggered central schemes](/methods/unstaggered-central-scheme.md);
[MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md) and the
[piecewise parabolic method](/methods/piecewise-parabolic-method.md);
[fluctuation-form finite-difference WENO](/methods/fluctuation-form-fd-weno.md)
and [path-conservative schemes](/methods/path-conservative-scheme.md) for
non-conservative systems, with
[stationary contact preservation](/properties/stationary-contact-preservation.md),
[flux globalization](/methods/flux-globalization.md) for the
[shallow-water equations](/definitions/shallow-water-equations.md) and other balance laws,
[well-balancing](/properties/well-balancing.md) and
[asymptotic preservation](/properties/asymptotic-preservation.md).

**4. Dissipation, dispersion and symmetry.** The
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md),
[numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
and [symmetry preservation](/properties/symmetry-preservation.md); the
[Ducros shock sensor](/definitions/ducros-shock-sensor.md) switches hybrid schemes,
as in [wall-modelled large-eddy simulation](/methods/wall-modeled-les.md).

**5. Discontinuous Galerkin and structure preservation.** The
[discontinuous Galerkin method](/methods/discontinuous-galerkin.md) and
[DGSEM](/methods/dgsem.md) on [summation-by-parts operators](/operators/summation-by-parts-operator.md),
with [Bassi–Rebay viscous discretizations](/methods/bassi-rebay-viscous-discretization.md),
and [flux reconstruction](/methods/flux-reconstruction.md) with its code
[PyFR](/software/pyfr.md), and the nodal [spectral difference method](/methods/spectral-difference-method.md);
[flux differencing](/methods/flux-differencing.md) with
[entropy-conservative and kinetic-energy-preserving fluxes](/methods/entropy-conservative-flux.md)
(built on the [logarithmic mean](/operators/logarithmic-mean.md)) gives
[entropy stability](/properties/entropy-stability.md), extended to uncollocated nodes by
[entropy projection](/methods/entropy-projection.md), and
[TeCNO schemes](/methods/tecno-scheme.md) carry it to high-order reconstruction;
[entropy correction terms](/methods/entropy-correction-term.md) restore it a
posteriori; on the
finite-difference side, [split convective forms](/methods/split-convective-forms.md)
give [kinetic energy preservation](/properties/kinetic-energy-preservation.md)
and [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
(with the [APEC flux](/methods/apec-scheme.md)),
and [local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md).
[Free-stream preservation](/properties/free-stream-preservation.md) on curved
meshes; [adaptive moving meshes](/methods/adaptive-moving-mesh.md),
[hp-adaptation](/methods/hp-adaptation.md) and
[implicit shock tracking](/methods/implicit-shock-tracking.md) move or refine the mesh;
the codes [Trixi.jl](/software/trixi-jl.md), [FLUXO](/software/fluxo.md) and
[FLEXI](/software/flexi.md).

**6. Limiting and bounds.** [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
decide where to act; [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
[convex limiting](/methods/convex-limiting.md), [OEDG](/methods/oedg.md) and
[COS(DG)](/methods/cos-dg.md),
[artificial viscosity](/methods/artificial-viscosity.md),
[MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md) (with a subcell
correction built on the [equivalence of DG and subcell finite volumes](/results/dg-subcell-finite-volume-equivalence.md)),
[quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md),
[entropy filtering](/methods/entropy-filtering.md),
[WENO limiters for DG](/methods/weno-limiter-dg.md) and
[WENO-stabilized continuous finite elements](/methods/weno-stabilized-continuous-galerkin.md)
are the remedies. [Bound preservation](/properties/bound-preservation.md) is
analysed by [geometric quasilinearization](/methods/geometric-quasilinearization.md)
and enforced by the [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
or the [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
and, for viscous flows, the
[positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md),
whose time-step bound the [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
sharpens; MHD adds the [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
and the [Godunov–Powell source term](/definitions/godunov-powell-source-term.md),
kept exactly by [constrained transport](/methods/constrained-transport.md) or damped by
[GLM divergence cleaning](/methods/glm-divergence-cleaning.md)
(on AMR hierarchies, [divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md)),
and [special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
add the recovery of primitive variables; at high magnetization the
[force-free splitting](/methods/force-free-splitting-rmhd.md) separates the field from the plasma.

**7. Multiphase and multicomponent flows.** The
[five-equation](/definitions/five-equation-model.md) and
[six-equation models](/definitions/six-equation-model.md), the
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md) and the
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md);
[level-set and ghost-fluid methods](/methods/level-set-method.md),
[conservative phase-field methods](/methods/phase-field-method.md), the
[discrete equations method](/methods/discrete-equations-method.md), the
[double-flux method](/methods/double-flux-method.md),
[conservative remapping](/methods/conservative-remapping.md) for ALE schemes and
[immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md);
[block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md);
the solvers [MFC](/software/mfc.md), [AMROC](/software/amroc.md),
[UCNS3D](/software/ucns3d.md), [IDEFIX](/software/idefix.md), [PLUTO](/software/pluto.md), [AthenaK](/software/athenak.md),
[ADAM](/software/adam.md), [URANOS](/software/uranos.md),
[STREAmS](/software/streams.md), [JAX-Fluids](/software/jax-fluids.md),
[TENET](/software/tenet.md), [ForestClaw](/software/forestclaw.md) and the [OpenFOAM-based solvers](/software/openfoam.md);
[operator splitting](/methods/operator-splitting.md) of stiff chemistry; verification
by the [method of manufactured solutions](/definitions/method-of-manufactured-solutions.md).

**8. Beyond method-of-lines reconstruction.** [Active Flux](/methods/active-flux.md)
and its bound-preserving generalization [PAMPA](/methods/pampa-scheme.md),
[ADER schemes](/methods/ader-scheme.md),
the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) behind every
conservative scheme, [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md),
[IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md) and the
[semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md) built on them,
[deferred correction](/methods/deferred-correction.md),
[discrete kinetic relaxation schemes](/methods/discrete-kinetic-relaxation-scheme.md), and the
implicit CWENO stepping of [Quinpi](/methods/quinpi.md).

**9. Benchmarks.** Scalar: [Burgers equation tests](/benchmarks/burgers-equation-tests.md),
the [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md) and
[solid-body rotation](/benchmarks/solid-body-rotation.md), with the
[Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md). One-dimensional:
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md), the
[Leblanc shock tube](/benchmarks/leblanc-shock-tube.md), the
[double rarefaction problem](/benchmarks/double-rarefaction-problem.md),
the [Shu–Osher problem](/benchmarks/shu-osher-problem.md), the
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md) and the
[Sedov blast wave](/benchmarks/sedov-blast-wave.md), the
[Noh implosion](/benchmarks/noh-implosion-problem.md); viscous: the
[viscous shock tube](/benchmarks/viscous-shock-tube.md).
Smooth: [density-wave advection](/benchmarks/density-wave-advection.md),
[material-interface advection](/benchmarks/material-interface-advection.md), the [isentropic vortex](/benchmarks/isentropic-vortex.md), the
[Gresho vortex](/benchmarks/gresho-vortex.md), the
[linear acoustics tests](/benchmarks/linear-acoustics-tests.md), the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), the
[hydrostatic equilibrium tests](/benchmarks/hydrostatic-equilibrium-tests.md) and
[flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md), the
[lid-driven cavity](/benchmarks/lid-driven-cavity.md), the
[NACA 0012 airfoil](/benchmarks/naca0012-airfoil.md) and the
[supersonic vortex between arcs](/benchmarks/supersonic-vortex-between-arcs.md). Two-dimensional
shocks: [two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md), the
[forward-facing step](/benchmarks/forward-facing-step.md),
[steady shock problems](/benchmarks/steady-shock-problems.md),
[shock diffraction](/benchmarks/shock-diffraction.md),
[explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md), the
[triple-point problem](/benchmarks/triple-point-problem.md),
[supersonic flow in a diamond-wedge channel](/benchmarks/supersonic-diamond-wedge-channel.md),
[supersonic flow over a circular-arc bump](/benchmarks/supersonic-bump-channel.md),
[shock–mixing-layer interaction](/benchmarks/shock-mixing-layer-interaction.md),
[shock–vortex](/benchmarks/shock-vortex-interaction.md) and
[shock–bubble](/benchmarks/shock-bubble-interaction.md) interactions, the
[shock–water column](/benchmarks/shock-water-column.md) and
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md),
[bubble collapse near a wall](/benchmarks/bubble-collapse-near-wall.md), the
[oscillating droplet](/benchmarks/oscillating-droplet.md),
[underwater explosions](/benchmarks/underwater-explosion.md),
[shock-induced combustion and detonation](/benchmarks/shock-induced-combustion.md), and
[high-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md).
Instabilities: [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and
[Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md). Non-convex
and MHD: the [KPP rotating wave](/benchmarks/kpp-rotating-wave.md), the
[Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), the
[MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md), the
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
[magnetic field-loop advection](/benchmarks/field-loop-advection.md), the
[magnetized vortex](/benchmarks/magnetized-vortex.md), the
[MHD shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md) and the
[tearing-mode instability](/benchmarks/tearing-mode-instability.md).
Shallow water: [flow over a bump and lake at rest](/benchmarks/flow-over-a-bump.md) and
[dam-break problems](/benchmarks/dam-break-problem.md).
Turbulence: [compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md),
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md) and the
[supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md).

## Catalog

* [Definitions](/definitions/index.md)
* [Methods](/methods/index.md)
* [Operators](/operators/index.md)
* [Results](/results/index.md)
* [Properties](/properties/index.md)
* [Benchmarks](/benchmarks/index.md)
* [Software](/software/index.md)
* [Sources](/sources/index.md)
* [Bibliography](/bibliography.md) — the complete citation record of the ingested sources.
