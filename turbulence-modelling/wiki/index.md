---
okf_version: "0.1"
---

# turbulence-modelling — Knowledge Bundle

The modelling and simulation of turbulent flows, as collected in a
turbulence-modelling bibliography of 2017–2026: Reynolds-averaged closures
and transition models, large-eddy simulation and its subgrid-scale models,
wall models, hybrid RANS/LES, data-driven and learned closures, the
high-order discretizations and codes used for scale-resolving simulation,
direct numerical simulation, and MHD turbulence.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($\langle\cdot\rangle$ the Reynolds average, $\bar\cdot$ the LES
filter of width $\Delta$, $\tilde\cdot$ the Favre filter, $\hat\cdot$ the test
filter, $R_{ij}$ and $\tau_{ij}$ the Reynolds and subgrid stresses with positive
trace, $\nu_t$ the eddy viscosity, $\lvert S\rvert=\sqrt{2S_{ij}S_{ij}}$,
$u_\tau$, $y^+$ and $h_{\mathrm{wm}}$ the wall quantities, $N$ the polynomial
degree of element methods, $\boldsymbol Z^\pm$ the Elsasser fields), and the
[update log](/log.md).

**Corpus:** chunks 1–3 of 7 ingested (60 of the 134 sources planned; the
archive is still growing). Chunk 1 holds the reviews and the
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
Hall-MHD and wave turbulence.

## Reading guide

**1. Averaging, filtering and the closure problem.**
[Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md) →
[large-eddy simulation](/definitions/large-eddy-simulation.md) →
[direct numerical simulation](/definitions/direct-numerical-simulation.md) →
[grid-point requirements](/results/les-grid-point-requirements.md).

**2. RANS and transition.**
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md),
[k-ω SST model](/methods/k-omega-sst-model.md),
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
[model-form uncertainty](/definitions/model-form-uncertainty.md).

**3. Subgrid-scale models and implicit LES.**
[Smagorinsky model](/methods/smagorinsky-model.md) →
[dynamic procedure](/methods/dynamic-procedure.md) →
[dynamic tensor-coefficient model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md);
[Vreman model](/methods/vreman-model.md),
[scale-similarity and mixed models](/methods/scale-similarity-model.md),
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md),
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
[fractional SGS model](/methods/fractional-sgs-model.md);
[energy backscatter](/definitions/energy-backscatter.md);
[gradient model and clipping](/methods/gradient-model.md);
[implicit LES](/definitions/implicit-les.md) and
[numerical dissipation](/properties/numerical-dissipation.md).

**4. Walls.**
[Law of the wall](/definitions/law-of-the-wall.md) →
[wall-modelled LES](/methods/wall-modelled-les.md) →
[equilibrium wall model](/methods/equilibrium-wall-model.md),
[LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md),
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md) and the
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md),
[machine-learning wall models](/methods/machine-learning-wall-model.md);
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md),
[log-layer mismatch](/definitions/log-layer-mismatch.md),
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md).

**5. Hybrid RANS/LES.**
[Hybrid RANS/LES](/definitions/hybrid-rans-les.md) →
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md),
[active model split](/methods/active-model-split.md),
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

**6. Data-driven closures.**
[A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md) →
[field inversion and machine learning](/methods/field-inversion-machine-learning.md),
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
[model-consistent training](/methods/model-consistent-training.md),
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md),
[physics-informed neural networks](/methods/physics-informed-neural-network.md);
[discretization-consistent closure](/definitions/discretization-consistent-closure.md),
[divergence-consistent LES](/methods/divergence-consistent-les.md);
[mesh adaptation](/methods/mesh-adaptation.md).

**7. Discretizations and codes for scale-resolving simulation.**
[Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md),
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md),
[high-order gas-kinetic schemes](/methods/high-order-gas-kinetic-scheme.md),
[WENO and hybrid shock-capturing schemes](/methods/weno-scheme.md),
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md),
[immersed boundary methods](/methods/immersed-boundary-method.md);
codes [FLEXI](/software/flexi.md), [CharLES](/software/charles.md),
[LESGO](/software/lesgo.md), [elsA](/software/elsa.md),
[RAMSES](/software/ramses.md), [STREAmS](/software/streams.md),
[OpenCFD-SCU](/software/opencfd-scu.md), [Nek5000 and NekRS](/software/nek5000.md),
[HORSES3D](/software/horses3d.md). Compressible wall turbulence:
[Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md),
[attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md).

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
[shock-generated turbulence](/results/shock-generated-turbulence.md).

**9. MHD, plasma and wave turbulence.**
[Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md) →
[critical balance](/properties/critical-balance.md) →
[dynamic alignment](/properties/dynamic-alignment.md) →
[tearing-mediated turbulence](/results/tearing-mediated-mhd-turbulence.md);
[decaying MHD turbulence](/results/decaying-mhd-turbulence.md),
[small-scale dynamo](/results/small-scale-dynamo.md),
[subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md);
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md),
[exact laws of (Hall-)MHD turbulence](/results/turbulence-exact-laws.md),
[weak wave turbulence](/results/weak-wave-turbulence.md),
[cross-scale interaction in plasma turbulence](/results/cross-scale-interaction.md),
[STITCH helicity-condensation model](/methods/stitch-helicity-condensation-model.md).

## Catalog

- [Definitions](/definitions/index.md) — precise domain terms.
- [Methods](/methods/index.md) — models, algorithms and schemes.
- [Properties](/properties/index.md) — constraints and invariants a method or flow can hold.
- [Results](/results/index.md) — scalings, theories and proved properties.
- [Benchmarks](/benchmarks/index.md) — standard test flows.
- [Software](/software/index.md) — codes embodying methods.
- [Sources](/sources/index.md) — one page per ingested source.
- [Bibliography](/bibliography.md) — every work cited by an ingested source.
