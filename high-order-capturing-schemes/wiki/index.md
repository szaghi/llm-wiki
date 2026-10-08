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
**Corpus: 20 sources compiled**: 20 published works, four of them read
in a report or preprint version (see the [update log](/log.md)).

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
   [WENO weight accuracy conditions](/results/weno-weight-accuracy-conditions.md).
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
   [SSP Runge–Kutta](/methods/ssp-runge-kutta.md), and
   [contact sharpening](/methods/contact-sharpening.md).
8. **Tests.** [Sod](/benchmarks/sod-shock-tube.md),
   [Lax](/benchmarks/lax-shock-tube.md),
   [Shu–Osher](/benchmarks/shu-osher-problem.md),
   [interacting blast waves](/benchmarks/interacting-blast-waves.md),
   [composite advection](/benchmarks/composite-advection-profile.md),
   [double Mach reflection](/benchmarks/double-mach-reflection.md),
   [forward step](/benchmarks/forward-facing-step.md),
   [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).

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
