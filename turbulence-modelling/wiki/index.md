---
okf_version: "0.1"
---

# turbulence-modelling — Knowledge Bundle

The modelling and simulation of turbulent flows, as collected in a
turbulence-modelling bibliography of 2017–2026: Reynolds-averaged closures
and transition models, large-eddy simulation and its subgrid-scale models,
wall models, hybrid RANS/LES, data-driven and learned closures, the
high-order discretizations and codes used for scale-resolving simulation,
direct numerical simulation, turbulent combustion, and MHD turbulence.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($\langle\cdot\rangle$ the Reynolds average, $\bar\cdot$ the LES
filter of width $\Delta$, $\tilde\cdot$ the Favre filter, $\hat\cdot$ the test
filter, $R_{ij}$ and $\tau_{ij}$ the Reynolds and subgrid stresses with positive
trace, $\nu_t$ the eddy viscosity, $\lvert S\rvert=\sqrt{2S_{ij}S_{ij}}$,
$u_\tau$, $y^+$ and $h_{\mathrm{wm}}$ the wall quantities, $N$ the polynomial
degree of element methods, $\boldsymbol Z^\pm$ the Elsasser fields), and the
[update log](/log.md).

**Corpus:** chunks 1–12 ingested (240 of the 307 sources planned in 16
chunks; the archive is still growing). Chunk 1 holds the reviews and the
papers that fix the vocabulary: the data-driven modelling reviews of
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md) and
[Duraisamy (2021)](/sources/duraisamy-2021.md), the MHD turbulence review of
[Schekochihin (2022)](/sources/schekochihin-2022.md), the survey of
machine-learning wall models of [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md),
wall-modelled LES of a high-lift aircraft ([Goc et al. 2021](/sources/goc-2021.md))
and of the NASA Juncture Flow ([Lozano-Durán et al. 2022](/sources/lozanoduran-2022.md)),
DNS of turbulent combustion ([Domingo & Vervisch 2023](/sources/domingo-2023.md)),
explicit against implicit subgrid modelling
([Vicente Cruz & Lamballais 2023](/sources/vicentecruz-2023.md)),
backscatter ([Vela-Martín 2022](/sources/velamartin-2022.md)), an algebraic
transition model ([Menter et al. 2022](/sources/menter-2022.md)), active model
split and PANS hybrids ([Haering et al. 2022](/sources/haering-2022.md),
[Dzanic et al. 2022](/sources/dzanic-2022.md)), kinetic-energy-preserving DG
for LES and FLEXI ([Flad & Gassner 2017](/sources/flad-2017.md),
[Krais et al. 2021](/sources/krais-2021.md)), the LaRTE and
inverse-velocity-transformation wall models
([Fowler et al. 2022](/sources/fowler-2022.md),
[Griffin et al. 2023](/sources/griffin-2023.md)), a tensor-coefficient
dynamic SGS model ([Agrawal et al. 2022](/sources/agrawal-2022.md)),
discretization- and divergence-consistent learned closures
([Beck & Kurz 2023](/sources/beck-2023.md),
[Agdestein & Sanderse 2025](/sources/agdestein-2025.md)) and
Spalart–Allmaras corrections ([Li & Liu 2022](/sources/li-2022.md)).
Chunk 2 (2021–2023 papers): SGS models on anisotropic grids and the
clipping of structural models, PANS for Rayleigh–Taylor mixing, adaptive
and adjoint-based mesh adaptation, hybrid RANS/LES and zonal DES of jets
and turbomachinery, transition at low Reynolds number, wall models in
Nek5000 and adverse pressure gradient, data-driven SA corrections,
high-order gas-kinetic schemes, entropy-stable SVV for DG, DNS of
supersonic and hypersonic boundary layers, reinforcement-learning wall
models, and turbulent dynamos in galaxy and interstellar-medium
simulations. Chunk 3 (2022–2023 papers): a fractional SGS model, learned
SGS models trained by reinforcement learning, the optimal eddy viscosity
and the conditioning of data-driven RANS, physics-informed networks,
variational data assimilation, residual-based grid adaptation for
wall-modelled LES, immersed boundaries with lattice Boltzmann and
constrained LES, low-dissipation and WENO-based schemes and the GPU codes
STREAmS, OpenCFD-SCU, NekRS and HORSES3D, shock–boundary-layer
interaction at hypersonic speeds, shock-generated turbulence, and plasma,
Hall-MHD and wave turbulence. Chunk 4 (2023–2024 papers): learned SGS
models (supervised, adjoint-trained, reinforcement learning), symbolic
regression for RANS, the anisotropic part of the SGS stress, the WALE,
σ and anisotropic minimum-dissipation models, the building-block-flow wall
model, hybrid RANS/LES of cars and turbomachinery, separation-bubble
transition, kinetic-energy- and pressure-equilibrium-preserving schemes,
jump-penalty and upwind stabilization of high-order methods, gas-kinetic
schemes on GPUs, lattice Boltzmann methods, and Hall-MHD turbulence.
Chunk 5 (2023–2025 papers): an autonomous eddy-viscosity model,
filter-width recalibration for high-order LES, ensemble-Kalman and
Bayesian calibration of closures, energy-conserving and fusion neural
SGS models, a reinforcement-learning wall model, Reynolds-stress and
laminar-kinetic-energy transition models, the compressible Baldwin–Lomax
model, immersed-boundary and lattice-Boltzmann wall treatments, flux
reconstruction and modal filtering, stabilized finite elements as implicit
LES, tabulated chemistry for flame–wall interaction, and turbulence in a
solar flare. Chunk 6 (2024–2026 papers): transitional DDES of a compressor
cascade and shock buffet in a transonic cascade, conditioned field
inversion, adjoint data assimilation and blending of data-driven RANS
models, neural-operator and super-resolution LES, a residual-based dynamic
SGS model, artificial viscosity and shock-capturing comparisons for the
supersonic Taylor–Green vortex, the GPU code GALÆXI, wall-modelled LES with
spectral elements, LES of dynamic stall, canopy flow and wind-turbine noise,
exascale DNS of isotropic turbulence, and bulk viscosity in compressible
MHD turbulence. Chunk 7 (2021–2026 papers): the Wilcox $k$-$\omega$ model and
wall functions in high-order RANS, RSM-based IDDES, continuous eddy
simulation and PITM, tip-leakage vortices, supersonic combustion with
flamelets, explicit modal filtering, numerically induced filters and
approximate deconvolution, higher-order gradient models and multi-filter
training of neural closures, the sigma model, volume-filtered immersed
boundaries with slip-wall models, spectral difference and nonlinearly
stable flux reconstruction, entropy-conservative schemes for thermally
perfect gases, DG error estimation and anisotropic mesh adaptation, and
shock-capturing schemes for real gases and kinetic equations. Chunk 8
(2022–2026 papers): high-order RANS and transition solvers (COOLFluiD flux
reconstruction, entropy-stable Spalart–Allmaras DGSEM, the $k$-$	au$ model,
laminar-kinetic-energy onset correlations), DES of a pump, ZDES in a
lattice-Boltzmann solver, scale-adaptive simulation, LES of dynamic stall
and of a shock/boundary-layer interaction with subcell shock capturing,
explicit wall-model fits, a priori deconvolution models, relaxation
filtering, solar-wind turbulence transport and TENO-based schemes.
Chunk 9 (2013–2022 papers): the High-Order CFD Workshop summary, the
wall-modelled LES and hybrid RANS/LES reviews of Bose & Park and Heinz,
the turbomachinery review of Sandberg & Michelassi, kinetic-energy- and
entropy-preserving schemes, gene-expression programming and random-forest
closures, wall-model-integrated LES, gas-kinetic LES, immersed boundaries
on moving Cartesian grids, the thickened flame model and thermodiffusive
DNS. Chunk 10 (2022 papers): variational multiscale LES and immersed
boundaries, explicit algebraic Reynolds-stress models learned by sparse
regression and CFD-driven training, discrete-adjoint field inversion and
SHAP explanations of RANS corrections, output-based mesh adaptation,
Rosenbrock time integration for DG, optimized modal filters, temporal LES
with lattice Boltzmann, entropy-stable weak solutions, BVD and compact
nonlinear schemes, wall-modelled LES of hypersonic and shock-dominated
flows, pressure dilatation and bulk viscosity in compressible DNS, wall
cooling and pressure fluctuations in hypersonic boundary layers, and the
eddy dissipation concept for MILD combustion. Chunk 11 (2022–2024 papers):
one-equation subgrid kinetic-energy models, subgrid velocity enrichment,
pseudo-DNS from fine-scale databases, the spatial gradient model, a priori
and a posteriori tests of compressible and real-gas SGS models, the
filtered actuator line in implicit LES and wind-farm LES over hills, a
dynamic RSM-based IDDES of transonic buffet, self-adaptive turbulence eddy
simulation with weighted compact nonlinear schemes on the 30P30N airfoil,
wall-modelled LES with spectral vanishing viscosity, a review of turbulent
boundary layers, machine learning in combustion and industrial CFD,
neural-network RANS closures, numerical subgrid stress in implicit LES,
ROUND schemes in OpenFOAM, hypersonic swept-ramp DNS, scramjet combustion
LES, premixed-flame DNS and turbulent deflagration-to-detonation transition.
Chunk 12 (2023–2024 papers): the HLPW-4 wall-modelled LES summary on the
CRM high-lift configuration, wall-modelled LES with semi-local scaling
including the SGS viscosity, neural-network nonlinear algebraic SGS models,
van Cittert deconvolution with differential filters, field inversion for
compressible channel RANS, eigensolution analysis of spectral difference
and flux reconstruction, mesh-refinement indicators for implicit LES,
shock capturing by subcell, positivity-preserving and a posteriori
limiters, skin-friction decomposition and mixing-layer analysis of a
shock/boundary-layer interaction, hypersonic inflow generation and the
generalized Reynolds analogy, scale-resolving hybrid RANS/LES of cylinder
flow, fluid–structure interaction with shock-induced panel loading,
dynamically thickened flames, principal-component transport, and
detonation codes and detonation–turbulence DNS.

## Reading guide

**1. Averaging, filtering and the closure problem.**
[Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md) →
[large-eddy simulation](/definitions/large-eddy-simulation.md) →
[direct numerical simulation](/definitions/direct-numerical-simulation.md) →
[grid-point requirements](/results/les-grid-point-requirements.md).

**2. RANS and transition.**
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md),
[Wilcox k-ω model](/methods/k-omega-model.md),
[k-ω SST model](/methods/k-omega-sst-model.md),
[k-ε models](/methods/k-epsilon-model.md),
[k-τ model](/methods/k-tau-model.md),
[differential Reynolds-stress models](/methods/reynolds-stress-model.md),
[barycentric anisotropy map](/definitions/barycentric-anisotropy-map.md),
[explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md),
[Baldwin–Lomax model](/methods/baldwin-lomax-model.md),
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
[laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md),
[laminar separation bubble](/definitions/laminar-separation-bubble.md),
[dynamic stall](/definitions/dynamic-stall.md),
[model-form uncertainty](/definitions/model-form-uncertainty.md).

**3. Subgrid-scale models and implicit LES.**
[Smagorinsky model](/methods/smagorinsky-model.md) →
[dynamic procedure](/methods/dynamic-procedure.md) →
[dynamic tensor-coefficient model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md);
[Vreman model](/methods/vreman-model.md),
[scale-similarity and mixed models](/methods/scale-similarity-model.md),
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md),
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
[fractional SGS model](/methods/fractional-sgs-model.md),
[WALE model](/methods/wale-model.md),
[residual-based dynamic SGS model](/methods/residual-based-dynamic-sgs-model.md),
[sigma model](/methods/sigma-model.md),
[explicit modal filtering](/methods/explicit-modal-filtering.md),
[autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md),
[anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md),
[variational multiscale method](/methods/variational-multiscale-method.md),
[one-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md),
[subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md),
[pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md);
[energy backscatter](/definitions/energy-backscatter.md),
[bottleneck effect](/definitions/bottleneck-effect.md);
[gradient model and clipping](/methods/gradient-model.md);
[implicit LES](/definitions/implicit-les.md) and
[numerical dissipation](/properties/numerical-dissipation.md).

**4. Walls.**
[Law of the wall](/definitions/law-of-the-wall.md) →
[wall-modelled LES](/methods/wall-modelled-les.md) →
[equilibrium wall model](/methods/equilibrium-wall-model.md),
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md),
[slip-wall models](/methods/slip-wall-model.md),
[LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md),
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md) and the
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md),
[machine-learning wall models](/methods/machine-learning-wall-model.md),
[building-block-flow wall model](/methods/building-block-flow-wall-model.md),
[wall functions for RANS](/methods/rans-wall-function.md);
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md),
[log-layer mismatch](/definitions/log-layer-mismatch.md),
[skin-friction decomposition](/definitions/skin-friction-decomposition.md),
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md).

**5. Hybrid RANS/LES.**
[Hybrid RANS/LES](/definitions/hybrid-rans-les.md) →
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md),
[active model split](/methods/active-model-split.md),
[continuous eddy simulation](/methods/continuous-eddy-simulation.md),
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md),
[detached-eddy simulation](/methods/detached-eddy-simulation.md);
[spectral gap](/definitions/spectral-gap.md).

**6. Data-driven closures.**
[A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md) →
[field inversion and machine learning](/methods/field-inversion-machine-learning.md),
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
[model-consistent training](/methods/model-consistent-training.md),
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md),
[physics-informed neural networks](/methods/physics-informed-neural-network.md),
[neural-network SGS models](/methods/neural-network-sgs-model.md),
[symbolic-regression closures](/methods/symbolic-regression-closure.md),
[Relexi](/software/relexi.md),
[ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md),
[blending of data-driven models](/methods/turbulence-model-aggregation.md),
[super-resolution SGS models](/methods/super-resolution-sgs-model.md),
[neural-operator LES surrogates](/methods/neural-operator-les-surrogate.md);
[discretization-consistent closure](/definitions/discretization-consistent-closure.md),
[divergence-consistent LES](/methods/divergence-consistent-les.md);
[mesh adaptation](/methods/mesh-adaptation.md).

**7. Discretizations and codes for scale-resolving simulation.**
[Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md),
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md),
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md),
[shock sensors and troubled-cell indicators](/definitions/shock-sensor.md),
[continuous-Galerkin spectral elements](/methods/spectral-element-method.md),
[geometric conservation law](/properties/geometric-conservation-law.md),
[entropy conservation](/properties/entropy-conservation.md),
[spectral difference method](/methods/spectral-difference-method.md),
[eigensolution analysis](/methods/eigensolution-analysis.md),
[method of manufactured solutions](/methods/method-of-manufactured-solutions.md),
[multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md),
[high-order gas-kinetic schemes](/methods/high-order-gas-kinetic-scheme.md),
[WENO and hybrid shock-capturing schemes](/methods/weno-scheme.md),
[weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md),
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md),
[immersed boundary methods](/methods/immersed-boundary-method.md),
[lattice Boltzmann methods](/methods/lattice-boltzmann-method.md),
[flux reconstruction](/methods/flux-reconstruction.md),
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md),
[thickened flame model](/methods/thickened-flame-model.md),
[actuator line and actuator disk models](/methods/actuator-line-model.md),
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md),
[high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md),
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md);
codes [FLEXI](/software/flexi.md), [CharLES](/software/charles.md),
[LESGO](/software/lesgo.md), [elsA](/software/elsa.md),
[RAMSES](/software/ramses.md), [STREAmS](/software/streams.md),
[OpenCFD-SCU](/software/opencfd-scu.md), [Nek5000 and NekRS](/software/nek5000.md),
[HORSES3D](/software/horses3d.md), [Nektar++](/software/nektar-plus-plus.md),
[ProLB](/software/prolb.md), [GALÆXI](/software/galaexi.md),
[TRACE](/software/trace.md), [OpenFOAM](/software/openfoam.md),
[COOLFluiD](/software/coolfluid.md), [hpMusic](/software/hpmusic.md),
[ANSYS Fluent](/software/ansys-fluent.md);
[Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md). Compressible wall turbulence:
[Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md),
[attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md),
[pressure dilatation](/definitions/pressure-dilatation.md).

**8. Benchmarks.**
[Turbulent channel flow](/benchmarks/turbulent-channel-flow.md),
[periodic hill](/benchmarks/periodic-hill.md),
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[JAXA Standard Model](/benchmarks/jaxa-standard-model.md),
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md),
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md),
[backward-facing step](/benchmarks/backward-facing-step.md),
[Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md),
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md),
[shock-generated turbulence](/results/shock-generated-turbulence.md),
[Ahmed body](/benchmarks/ahmed-body.md),
[ACAT1 fan stage](/benchmarks/acat1-fan-stage.md),
[Imperial front wing](/benchmarks/imperial-front-wing.md),
[ERCOFTAC T3 flat plates](/benchmarks/ercoftac-t3-flat-plate.md),
[NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md),
[NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md),
[RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md),
[Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md),
[Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md),
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md),
[NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md),
[30P30N three-element high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md),
[hammerhead launch-vehicle buffet](/benchmarks/hammerhead-launch-vehicle-buffet.md),
[turbine cascades](/benchmarks/turbine-cascade.md),
[compressor cascades](/benchmarks/compressor-cascade.md),
[NASA Rotor 37](/benchmarks/nasa-rotor-37.md),
[NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md),
[square cylinder](/benchmarks/square-cylinder-flow.md),
[temporal mixing layer](/benchmarks/temporal-mixing-layer.md);
[inflow turbulence generation](/methods/inflow-turbulence-generation.md).

**9. MHD, plasma and wave turbulence.**
[Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md) →
[critical balance](/properties/critical-balance.md) →
[dynamic alignment](/properties/dynamic-alignment.md) →
[tearing-mediated turbulence](/results/tearing-mediated-mhd-turbulence.md);
[decaying MHD turbulence](/results/decaying-mhd-turbulence.md),
[small-scale dynamo](/results/small-scale-dynamo.md),
[subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md);
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md),
[bulk viscosity](/definitions/bulk-viscosity.md),
[exact laws of (Hall-)MHD turbulence](/results/turbulence-exact-laws.md),
[weak wave turbulence](/results/weak-wave-turbulence.md),
[cross-scale interaction in plasma turbulence](/results/cross-scale-interaction.md),
[STITCH helicity-condensation model](/methods/stitch-helicity-condensation-model.md),
[GHOST](/software/ghost.md).

## Catalog

- [Definitions](/definitions/index.md) — precise domain terms.
- [Methods](/methods/index.md) — models, algorithms and schemes.
- [Properties](/properties/index.md) — constraints and invariants a method or flow can hold.
- [Results](/results/index.md) — scalings, theories and proved properties.
- [Benchmarks](/benchmarks/index.md) — standard test flows.
- [Software](/software/index.md) — codes embodying methods.
- [Sources](/sources/index.md) — one page per ingested source.
- [Bibliography](/bibliography.md) — every work cited by an ingested source.
