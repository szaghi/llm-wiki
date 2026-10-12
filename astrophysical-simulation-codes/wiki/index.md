---
okf_version: "0.1"
---

# astrophysical-simulation-codes — Knowledge Bundle

How production simulation codes for astrophysical and compressible flows
are built and what they are shown to do: (magneto)hydrodynamics
frameworks and their solvers, meshes and AMR; physics modules treated as
numerical methods (self-gravity, sink particles, cooling and chemistry,
radiation moments, equations of state, relativistic primitive recovery);
code comparisons; and GPU and performance-portable frameworks, astro or
not.
**Corpus: 10 of 35 archived sources compiled** (see the [update log](/log.md)).

**Start here:** the [Notation registry](/notation.md), which is normative
for every page.

## Reading guide

1. **The codes.** Start with [Athena](/software/athena.md) and its rewrite
   [Athena++](/software/athena-plus-plus.md), then the other frameworks:
   [PLUTO](/software/pluto.md) (Chombo AMR), [Castro](/software/castro.md)
   (BoxLib AMR, general EOS), [Enzo](/software/enzo.md) (cosmological patch
   AMR), [GAMER](/software/gamer.md) (GPU octree AMR) and
   [RAMSES-RT](/software/ramses-rt.md) (cell-based AMR with radiation).
2. **How they integrate (M)HD.** [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md)
   (CTU, VL2, SSP Runge–Kutta), the [Riemann solvers](/methods/approximate-riemann-solvers.md)
   they offer, and the two ways of controlling the magnetic divergence:
   [constrained transport](/methods/constrained-transport.md) and
   [GLM cleaning](/methods/glm-divergence-cleaning.md). Where kinetic energy
   dominates, the [dual-energy formalism](/methods/dual-energy-formalism.md).
3. **Meshes.** [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md):
   cell, patch and block hierarchies; subcycled against global time steps;
   refluxing and EMF correction.
4. **Physics modules as numerics.** Self-gravity:
   [Poisson solvers on adaptive meshes](/methods/multigrid-self-gravity.md)
   and [conservative self-gravity](/methods/conservative-self-gravity.md).
   Radiation: [M1 two-moment transport](/methods/m1-radiation-transport.md)
   and the [reduced speed of light](/definitions/reduced-speed-of-light.md).
5. **Verification.** [Linear wave convergence](/benchmarks/linear-wave-convergence.md),
   [Sod](/benchmarks/sod-shock-tube.md), [Brio–Wu](/benchmarks/brio-wu-shock-tube.md),
   [Orszag–Tang](/benchmarks/orszag-tang-vortex.md),
   [field-loop advection](/benchmarks/field-loop-advection.md),
   [MHD blast wave](/benchmarks/mhd-blast-wave.md),
   [Sedov–Taylor](/benchmarks/sedov-taylor-blast-wave.md),
   [double Mach reflection](/benchmarks/double-mach-reflection.md),
   [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md),
   [Jeans wave](/benchmarks/jeans-wave.md).

Folder indexes: [Software](/software/index.md) · [Methods](/methods/index.md) ·
[Definitions](/definitions/index.md) · [Operators](/operators/index.md) ·
[Properties](/properties/index.md) · [Results](/results/index.md) ·
[Benchmarks](/benchmarks/index.md) · [Sources](/sources/index.md) ·
[Bibliography](/bibliography.md)
