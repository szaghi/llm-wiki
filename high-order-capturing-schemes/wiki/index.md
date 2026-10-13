---
okf_version: "0.1"
---

# high-order-capturing-schemes — Knowledge Bundle

High-order shock-capturing schemes for hyperbolic conservation laws:
ENO and WENO and their variants (mapped, Z, adaptive-order, targeted
ENO, central WENO, compact hybrids), monotonicity-preserving and PPM
reconstruction, ADER and space–time predictors, a posteriori limiting,
positivity-preserving limiters, SSP time discretization, numerical
boundary treatment (inverse Lax–Wendroff, weighted extrapolation,
immersed boundaries, cut cells),
high-order AMR, and their extension to MHD.
**Corpus: 116 sources compiled (the whole archive)**: 115 published works,
many of them read in a report, preprint or author-manuscript version (each
Source page records which), and one unpublished preprint (see the
[update log](/log.md)). Two
surveys by Shu ([2009](/sources/shu-2009.md), [2020](/sources/shu-2020.md))
are the best overviews of the field.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page.

## Reading guide

1. **What a capturing scheme must reconcile.** High order in smooth
   regions against no Gibbs oscillation at jumps. The stability notions
   that frame the trade:
   [total variation diminishing](/properties/total-variation-diminishing.md)
   (and why it forces first order at extrema), and its weakening,
   [essentially non-oscillatory](/definitions/essentially-non-oscillatory.md).
   Why the schemes must be nonlinear at all:
   [Godunov's order barrier](/results/godunov-order-barrier.md) (no
   monotone linear scheme is second order). The first-order base they all
   build on is [Godunov's method](/methods/godunov-method.md), and its
   first second-order sequel, with limited slopes, is
   [MUSCL](/methods/muscl.md).
2. **The two approximation problems.**
   [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md)
   (finite volume, any mesh) and the
   [conservative finite-difference formulation](/methods/conservative-finite-difference.md)
   (point values, uniform or mapped grids, cheap in multi-D), joined by the
   primitive-function identity; the interface flux is a
   [monotone flux](/definitions/monotone-flux.md) or a flux splitting.
3. **Adaptive and weighted stencils.**
   [ENO](/methods/eno-reconstruction.md) → [WENO](/methods/weno.md)
   (orders $r+1$, then $2r-1$, then up to 13), governed by the
   [smoothness indicator](/definitions/smoothness-indicator.md);
   a centred, Riemann-free variant: [central WENO](/methods/central-weno.md).
   The conditions any weights must meet are collected in
   [WENO weight accuracy conditions](/results/weno-weight-accuracy-conditions.md);
   when accuracy forces [negative linear weights](/methods/negative-linear-weights.md)
   they need special treatment. A design principle behind the indicators:
   [self-similarity](/properties/self-similarity.md).
4. **The family after WENO-JS.** Restoring order and lowering dissipation:
   [mapped WENO](/methods/mapped-weno.md), [WENO-Z](/methods/weno-z.md),
   [central-upwind WENO](/methods/central-upwind-weno.md),
   [targeted ENO](/methods/teno.md), and the adaptive-order
   [WENO-AO / WENO-ZQ](/methods/weno-ao.md) (open `Contradictions` entry on
   WENO-ZQ's non-oscillation claim). Resolving turbulence:
   [bandwidth-optimized WENO](/methods/bandwidth-optimized-weno.md),
   [hybrid compact-WENO](/methods/hybrid-compact-weno.md), measured by the
   [modified wavenumber](/definitions/modified-wavenumber.md).
5. **Limiting instead of adapting.** [PPM](/methods/ppm.md) and the
   [monotonicity-preserving bounds](/methods/monotonicity-preserving-limiter.md)
   of MP5/MPWENO — the flat-extremum dispute closed by human fiat in
   favour of Balsara–Shu.
6. **Where order is lost.** [Accuracy at critical points](/properties/accuracy-at-critical-points.md)
   collects every family's claim; Henrick et al. supersede WENO-JS's
   critical-point claim (closed `Contradictions` entry).
7. **Making it work on systems and in time.**
   [Local characteristic decomposition](/methods/characteristic-decomposition.md),
   [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) with its
   [order barriers](/results/ssp-order-barriers.md), the single-step
   [Lax–Wendroff (Taylor)](/methods/taylor-time-discretization.md)
   alternative and its finite-volume/DG branch. Beyond SSP:
   [explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md) from
   Runge (1895) on, their [low-storage](/methods/low-storage-runge-kutta.md)
   forms, [SSP multistep methods](/methods/ssp-linear-multistep.md) with
   variable steps, [step-size control](/methods/runge-kutta-step-size-control.md)
   by embedded pairs, and two ways to re-choose the weights after the
   stages: [relaxation](/methods/relaxation-runge-kutta.md) for fully
   discrete entropy stability and
   [positivity adaptation](/methods/positivity-preserving-adaptive-runge-kutta.md).
   Diffusion terms in DG: [recovery DG](/methods/recovery-dg-diffusion.md).
   Then one-step
   [ADER](/methods/ader.md) (one reconstruction per step, equal order in
   space and time; open `Contradictions` entry on how many Picard
   iterations its predictor needs), the interface [Riemann solvers](/methods/approximate-riemann-solvers.md),
   built on the [exact Riemann solver](/methods/exact-riemann-solver.md) of
   the Euler equations, on the two-wave [HLL solver](/methods/hll-riemann-solver.md)
   with its wave-speed estimates, or on the three-wave [HLLC solver](/methods/hllc-riemann-solver.md),
   and [contact sharpening](/methods/contact-sharpening.md).
   **Riemann-solver design.** The [HLLEM (HLLI) solver](/methods/hllem-riemann-solver.md)
   keeps contacts and shear; [multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)
   resolve the strongly interacting state at cell edges and corners. For
   MHD, [nonconvexity](/results/mhd-nonconvexity.md) admits compound waves
   that a solver must handle. Solvers that do suffer
   [numerical shock instability](/definitions/numerical-shock-instability.md)
   (carbuncle, odd–even decoupling, kinked Mach stem), which
   [sensor-driven cures](/methods/shock-instability-cures.md) remove. An
   open `Contradictions` entry asks whether HLLE is carbuncle-free. Related
   anomalies: the [slowly moving shock](/definitions/slowly-moving-shock-anomaly.md)
   (open entry: is it independent of the Riemann solver?)
   and the loss of accuracy of upwind fluxes at
   [low Mach number](/methods/low-mach-number-fluxes.md). This literature
   works mostly at first and second order; the higher-order evidence is
   Balsara & Shu's switch to Lax–Friedrichs fluxes near shocks with
   MPWENO, and Woodward & Colella's PPM, which suppresses the 2D
   instability their Godunov and MUSCL runs show.
8. **Other routes to high order.** Three-dimensional
   [finite-volume reconstruction](/methods/finite-volume-reconstruction.md),
   the [alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md)
   (WENO interpolation, any Riemann solver, even-derivative corrections),
   [compact-reconstruction WENO](/methods/compact-reconstruction-weno.md),
   non-polynomial [GP-WENO](/methods/gp-weno.md),
   [polynomial WENO](/methods/polynomial-weno.md), [multi-resolution WENO](/methods/multi-resolution-weno.md) (nested central stencils), [Hermite WENO](/methods/hermite-weno.md) (averages and derivatives; review-level only) (whole candidate
   polynomials with a dominant central stencil, for unstructured meshes
   and ADER), and the [fourth-order finite volume](/methods/fourth-order-finite-volume.md)
   of the Colella group (average–point conversions instead of Gauss
   points).
9. **Staying physical.** [Positivity preservation](/properties/positivity-preserving.md)
   — convex admissible set, positive first-order flux, SSP time
   stepping — enforced by the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
   or by [flux limiters](/methods/positivity-preserving-flux-limiter.md).
   Open `Contradictions` entries: is the first-order Lax–Friedrichs MHD
   scheme provably positive? Does positivity limiting inside Runge–Kutta
   stages reduce the order? For MHD the divergence constraint is kept by
   [constrained transport](/methods/constrained-transport.md) (staggered
   and unstaggered designs both valid, each for its own discrete
   divergence; closed by fiat), by
   [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
   of staggered fields, by [GLM cleaning](/methods/hyperbolic-divergence-cleaning.md)
   (open `Contradictions` entries: should the cleaning speed follow the
   time step? Time-step changes and AMR break the cleaning's assumptions;
   and is constrained transport or cleaning the more robust?)
   or by projection; without it high-order MHD runs fail. Curl constraints
   have their dual: [curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md). On curvilinear grids,
   uniform flow must stay uniform:
   [free-stream preservation](/properties/free-stream-preservation.md); with
   source terms, equilibria must stay steady:
   [well-balanced schemes](/properties/well-balanced.md).
10. **Limiting high-order DG.** A priori:
   [WENO limiters](/methods/weno-limited-dg.md) rebuild troubled cells from
   neighbouring averages. A posteriori:
   [subcell limiting](/methods/a-posteriori-subcell-limiting.md) (MOOD)
   recomputes cells that fail positivity or a relaxed maximum principle,
   using ADER-WENO on $2K+1$ subcells.
11. **Boundaries and adaptive meshes.** Ghost values on Cartesian grids cut
   by the boundary come from [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)
   expansions (stable for any cut-cell distance, shown for 1D linear
   advection when enough boundary derivatives come from the ILW procedure)
   or from
   [weighted extrapolation](/methods/weighted-extrapolation.md), against which
   [Navier–Stokes characteristic boundary conditions](/methods/characteristic-boundary-conditions.md)
   argue that extrapolation over-specifies outflow (open entry); the ILW
   line extends to sign-changing wind, exact conservation, moving bodies
   and fluid–structure interfaces. Provably stable closures come from
   summation by parts: [energy-stable WENO](/methods/energy-stable-weno.md).
   Bodies that do not fit the grid: [immersed-boundary methods](/methods/immersed-boundary-method.md)
   (Peskin's forcing; ghost cells, not conservative at the wall) and
   conservative [cut-cell finite volume](/methods/cut-cell-finite-volume.md)
   (open entry: what order does flux redistribution give?),
   whose small-cell problem [flux redistribution](/methods/flux-redistribution.md) and [state redistribution](/methods/state-redistribution.md)
   solve, with re-redistribution at AMR interfaces.
   [High-order AMR](/methods/high-order-amr.md): one-step updates for
   local time stepping on trees, or Runge–Kutta time stepping on
   block-structured hierarchies (subcycled or with one global step), where ghost values must match the stages
   and refluxing costs finite differences their order.
12. **Codes.** [PLUTO](/software/pluto.md), [HOW-MHD](/software/how-mhd.md), the [AMReX framework and PeleC](/software/amrex.md)
   and the GPU DNS code [STREAmS](/software/streams.md).
13. **Tests.** [Burgers shock formation](/benchmarks/burgers-shock-formation.md), [Sod](/benchmarks/sod-shock-tube.md),
   [Lax](/benchmarks/lax-shock-tube.md),
   [Shu–Osher](/benchmarks/shu-osher-problem.md),
   [interacting blast waves](/benchmarks/interacting-blast-waves.md),
   [composite advection](/benchmarks/composite-advection-profile.md),
   [double Mach reflection](/benchmarks/double-mach-reflection.md),
   [forward step](/benchmarks/forward-facing-step.md),
   [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md),
   [isentropic vortex](/benchmarks/isentropic-vortex.md),
   [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md),
   [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
   [cylindrical and spherical explosion](/benchmarks/multidimensional-explosion.md). Embedded
   boundaries: [supersonic cylinder](/benchmarks/supersonic-cylinder-flow.md),
   [shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md),
   [supersonic vortex in a quarter annulus](/benchmarks/supersonic-vortex-annulus.md),
   [shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md),
   [Schardin's problem](/benchmarks/schardin-problem.md). Shock
   reflection and diffraction, with experiments to compare against (the
   vocabulary: [regular and Mach reflection](/definitions/mach-reflection.md)):
   [shock passing a sphere](/benchmarks/shock-sphere-interaction.md),
   [double concave wedges](/benchmarks/double-concave-shock-reflection.md),
   and the corner experiments behind [shock diffraction](/benchmarks/shock-diffraction.md). Shock
   instability: [Quirk's odd–even test](/benchmarks/quirk-odd-even-test.md),
   [stationary normal shock](/benchmarks/stationary-normal-shock.md),
   [Mach 20 blunt body](/benchmarks/hypersonic-blunt-body.md). Positivity:
   [double rarefaction](/benchmarks/double-rarefaction.md),
   [Sedov](/benchmarks/sedov-blast-wave.md) (open entry: does
   positivity-limited DG survive it without a TVB limiter?),
   [Leblanc](/benchmarks/leblanc-shock-tube.md),
   [Mach 2000 jet](/benchmarks/high-mach-astrophysical-jet.md),
   [shock diffraction](/benchmarks/shock-diffraction.md). MHD:
   [Brio–Wu](/benchmarks/brio-wu-shock-tube.md),
   [Ryu–Jones shock tubes](/benchmarks/ryu-jones-shock-tubes.md),
   [grid-oblique shock tubes](/benchmarks/oblique-mhd-shock-tubes.md),
   [Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md),
   [field loop](/benchmarks/field-loop-advection.md),
   [Orszag–Tang](/benchmarks/orszag-tang-vortex.md),
   [rotor](/benchmarks/mhd-rotor.md),
   [low-β blast](/benchmarks/mhd-blast-wave.md),
   [shock–cloud](/benchmarks/shock-cloud-interaction.md).

## Folders

* [Definitions](/definitions/index.md)
* [Methods](/methods/index.md)
* [Operators](/operators/index.md)
* [Properties](/properties/index.md)
* [Results](/results/index.md)
* [Benchmarks](/benchmarks/index.md)
* [Software](/software/index.md)
* [Sources](/sources/index.md)
* [Bibliography](/bibliography.md)
