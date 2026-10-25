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

**Corpus:** chunk 1 of 7 ingested (20 of the 131 sources present on
2026-10-25; the archive is still growing). Chunk 1 holds the reviews and the
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
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md);
[energy backscatter](/definitions/energy-backscatter.md);
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
[log-layer mismatch](/definitions/log-layer-mismatch.md),
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md).

**5. Hybrid RANS/LES.**
[Hybrid RANS/LES](/definitions/hybrid-rans-les.md) →
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md),
[active model split](/methods/active-model-split.md).

**6. Data-driven closures.**
[A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md) →
[field inversion and machine learning](/methods/field-inversion-machine-learning.md),
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
[model-consistent training](/methods/model-consistent-training.md),
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md);
[discretization-consistent closure](/definitions/discretization-consistent-closure.md),
[divergence-consistent LES](/methods/divergence-consistent-les.md).

**7. Discretizations and codes for scale-resolving simulation.**
[Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md),
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md);
codes [FLEXI](/software/flexi.md), [CharLES](/software/charles.md),
[LESGO](/software/lesgo.md).

**8. Benchmarks.**
[Turbulent channel flow](/benchmarks/turbulent-channel-flow.md),
[periodic hill](/benchmarks/periodic-hill.md),
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[JAXA Standard Model](/benchmarks/jaxa-standard-model.md),
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md).

**9. MHD turbulence.**
[Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md) →
[critical balance](/properties/critical-balance.md) →
[dynamic alignment](/properties/dynamic-alignment.md) →
[tearing-mediated turbulence](/results/tearing-mediated-mhd-turbulence.md);
[decaying MHD turbulence](/results/decaying-mhd-turbulence.md),
[small-scale dynamo](/results/small-scale-dynamo.md).

## Catalog

- [Definitions](/definitions/index.md) — precise domain terms.
- [Methods](/methods/index.md) — models, algorithms and schemes.
- [Properties](/properties/index.md) — constraints and invariants a method or flow can hold.
- [Results](/results/index.md) — scalings, theories and proved properties.
- [Benchmarks](/benchmarks/index.md) — standard test flows.
- [Software](/software/index.md) — codes embodying methods.
- [Sources](/sources/index.md) — one page per ingested source.
- [Bibliography](/bibliography.md) — every work cited by an ingested source.
