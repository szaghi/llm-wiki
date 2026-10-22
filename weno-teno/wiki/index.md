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

**Corpus:** chunks 1–2 of 11 ingested (40 of 207 sources). Chunk 1, the reviews and the
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
multiphase solver. The remaining chunks follow the archive's order; the [Sources](/sources/index.md) index
lists what is in.

## Reading guide

**1. Reconstruction.** Begin with the
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
(point values, flux reconstruction, and its relation to finite volumes) and the
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
[multi-resolution WENO](/methods/multi-resolution-weno.md), [WLS-ENO](/methods/wls-eno.md),
[CWENO](/methods/cweno.md), [Hermite WENO](/methods/hermite-weno.md),
[hybrid central-WENO schemes](/methods/hybrid-weno.md) and
[learned WENO weights](/methods/learned-weno-weights.md). The
[semi-Lagrangian finite-volume WENO](/methods/semi-lagrangian-finite-volume.md)
reconstructs on Lagrangian cells.
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
[Rankine–Hugoniot condition](/definitions/rankine-hugoniot-condition.md) and the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md);
[characteristic decomposition](/methods/characteristic-decomposition.md);
[central-upwind schemes](/methods/central-upwind-scheme.md), their
[LCD variant](/methods/lcd-central-upwind-scheme.md) and the
[adaptive-diffusion Rankine–Hugoniot flux](/methods/adaptive-diffusion-central-upwind-flux.md);
[unstaggered central schemes](/methods/unstaggered-central-scheme.md);
[fluctuation-form finite-difference WENO](/methods/fluctuation-form-fd-weno.md)
for non-conservative systems, with
[stationary contact preservation](/properties/stationary-contact-preservation.md)
[well-balancing](/properties/well-balancing.md) and
[asymptotic preservation](/properties/asymptotic-preservation.md).

**4. Dissipation, dispersion and symmetry.** The
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md),
[numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
and [symmetry preservation](/properties/symmetry-preservation.md).

**5. Discontinuous Galerkin and structure preservation.** The
[discontinuous Galerkin method](/methods/discontinuous-galerkin.md) and
[DGSEM](/methods/dgsem.md) on [summation-by-parts operators](/operators/summation-by-parts-operator.md);
[flux differencing](/methods/flux-differencing.md) with
[entropy-conservative and kinetic-energy-preserving fluxes](/methods/entropy-conservative-flux.md)
(built on the [logarithmic mean](/operators/logarithmic-mean.md)) gives
[entropy stability](/properties/entropy-stability.md), and
[TeCNO schemes](/methods/tecno-scheme.md) carry it to high-order reconstruction; on the
finite-difference side, [split convective forms](/methods/split-convective-forms.md)
give [kinetic energy preservation](/properties/kinetic-energy-preservation.md),
and [local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md).
[Free-stream preservation](/properties/free-stream-preservation.md) on curved
meshes; [adaptive moving meshes](/methods/adaptive-moving-mesh.md),
[hp-adaptation](/methods/hp-adaptation.md) and
[implicit shock tracking](/methods/implicit-shock-tracking.md) move or refine the mesh;
the codes [Trixi.jl](/software/trixi-jl.md) and [FLUXO](/software/fluxo.md).

**6. Limiting and bounds.** [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
decide where to act; [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
[convex limiting](/methods/convex-limiting.md), [OEDG](/methods/oedg.md),
[artificial viscosity](/methods/artificial-viscosity.md) and
[WENO-stabilized continuous finite elements](/methods/weno-stabilized-continuous-galerkin.md)
are the remedies. [Bound preservation](/properties/bound-preservation.md) is
analysed by [geometric quasilinearization](/methods/geometric-quasilinearization.md)
and enforced by the [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
or the [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md),
whose time-step bound the [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
sharpens; MHD adds the [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

**7. Multiphase and multicomponent flows.** The
[five- and six-equation models](/definitions/five-equation-model.md), the
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md) and the
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md);
[level-set and ghost-fluid methods](/methods/level-set-method.md); the solver
[MFC](/software/mfc.md).

**8. Beyond method-of-lines reconstruction.** [Active Flux](/methods/active-flux.md),
the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) behind every
conservative scheme, [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md) and the
implicit CWENO stepping of [Quinpi](/methods/quinpi.md).

**9. Benchmarks.** Scalar: [Burgers equation tests](/benchmarks/burgers-equation-tests.md),
the [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md) and
[solid-body rotation](/benchmarks/solid-body-rotation.md). One-dimensional:
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md), the
[Leblanc shock tube](/benchmarks/leblanc-shock-tube.md), the
[double rarefaction problem](/benchmarks/double-rarefaction-problem.md),
the [Shu–Osher problem](/benchmarks/shu-osher-problem.md), the
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md) and the
[Sedov blast wave](/benchmarks/sedov-blast-wave.md).
Smooth: the [isentropic vortex](/benchmarks/isentropic-vortex.md) and the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md). Two-dimensional
shocks: [two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md), the
[forward-facing step](/benchmarks/forward-facing-step.md),
[shock–vortex](/benchmarks/shock-vortex-interaction.md) and
[shock–bubble](/benchmarks/shock-bubble-interaction.md) interactions, the
[shock–water column](/benchmarks/shock-water-column.md) and
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md), and
[high-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md).
Instabilities: [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
and [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md). Non-convex
and MHD: the [KPP rotating wave](/benchmarks/kpp-rotating-wave.md) and the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) and the
[MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md).

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
