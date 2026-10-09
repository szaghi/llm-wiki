---
okf_version: "0.1"
---

# high-order-capturing-schemes — Knowledge Bundle

High-order shock-capturing schemes for hyperbolic conservation laws:
ENO and WENO and their variants (mapped, Z, adaptive-order, targeted
ENO, central WENO, compact hybrids), monotonicity-preserving and PPM
reconstruction, ADER and space–time predictors, a posteriori limiting,
positivity-preserving limiters, SSP time discretization, numerical
boundary treatment (inverse Lax–Wendroff, weighted extrapolation),
high-order AMR, and their extension to MHD.
**Corpus: 62 sources compiled (the whole archive)**: 61 published works,
eighteen of them read in a report, preprint or author-manuscript version,
and one unpublished preprint (see the [update log](/log.md)). Two
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
   alternative and its finite-volume/DG branch, one-step
   [ADER](/methods/ader.md) (one reconstruction per step, equal order in
   space and time), the interface [Riemann solvers](/methods/approximate-riemann-solvers.md),
   and [contact sharpening](/methods/contact-sharpening.md).
8. **Other routes to high order.** Three-dimensional
   [finite-volume reconstruction](/methods/finite-volume-reconstruction.md),
   the [alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md)
   (WENO interpolation, any Riemann solver, even-derivative corrections),
   [compact-reconstruction WENO](/methods/compact-reconstruction-weno.md),
   non-polynomial [GP-WENO](/methods/gp-weno.md),
   [polynomial WENO](/methods/polynomial-weno.md) (whole candidate
   polynomials with a dominant central stencil, for unstructured meshes
   and ADER), and the [fourth-order finite volume](/methods/fourth-order-finite-volume.md)
   of the Colella group (average–point conversions instead of Gauss
   points).
9. **Staying physical.** [Positivity preservation](/properties/positivity-preserving.md)
   — convex admissible set, positive first-order flux, SSP time
   stepping — enforced by the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
   or by [flux limiters](/methods/positivity-preserving-flux-limiter.md).
   Open `Contradictions` entry: is the first-order Lax–Friedrichs MHD scheme
   provably positive? For MHD the divergence constraint is kept by
   [constrained transport](/methods/constrained-transport.md) (staggered
   and unstaggered designs both valid, each for its own discrete
   divergence; closed by fiat), by
   [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
   of staggered fields, by [GLM cleaning](/methods/hyperbolic-divergence-cleaning.md)
   (open `Contradictions` entry: should the cleaning speed follow the time
   step? Time-step changes and AMR break the cleaning's assumptions)
   or by projection; without it high-order MHD runs fail. Curl constraints
   have their dual: [curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md). On curvilinear grids,
   uniform flow must stay uniform:
   [free-stream preservation](/properties/free-stream-preservation.md).
10. **Limiting high-order DG.** A priori:
   [WENO limiters](/methods/weno-limited-dg.md) rebuild troubled cells from
   neighbouring averages. A posteriori:
   [subcell limiting](/methods/a-posteriori-subcell-limiting.md) (MOOD)
   recomputes cells that fail positivity or a relaxed maximum principle,
   using ADER-WENO on $2K+1$ subcells.
11. **Boundaries and adaptive meshes.** Ghost values on Cartesian grids cut
   by the boundary come from [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)
   expansions (stable for any cut-cell distance) or from
   [weighted extrapolation](/methods/weighted-extrapolation.md); the ILW
   line extends to sign-changing wind, exact conservation, moving bodies
   and fluid–structure interfaces. Provably stable closures come from
   summation by parts: [energy-stable WENO](/methods/energy-stable-weno.md).
   [High-order AMR](/methods/high-order-amr.md): one-step updates for
   local time stepping on trees, or Runge–Kutta subcycling on
   block-structured hierarchies, where ghost values must match the stages
   and refluxing costs finite differences their order.
12. **Codes.** [PLUTO](/software/pluto.md), [HOW-MHD](/software/how-mhd.md)
   and the GPU DNS code [STREAmS](/software/streams.md).
13. **Tests.** [Sod](/benchmarks/sod-shock-tube.md),
   [Lax](/benchmarks/lax-shock-tube.md),
   [Shu–Osher](/benchmarks/shu-osher-problem.md),
   [interacting blast waves](/benchmarks/interacting-blast-waves.md),
   [composite advection](/benchmarks/composite-advection-profile.md),
   [double Mach reflection](/benchmarks/double-mach-reflection.md),
   [forward step](/benchmarks/forward-facing-step.md),
   [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md),
   [isentropic vortex](/benchmarks/isentropic-vortex.md),
   [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
   [cylindrical and spherical explosion](/benchmarks/multidimensional-explosion.md). Embedded
   boundaries: [supersonic cylinder](/benchmarks/supersonic-cylinder-flow.md),
   [shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md). Positivity:
   [double rarefaction](/benchmarks/double-rarefaction.md),
   [Sedov](/benchmarks/sedov-blast-wave.md),
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
