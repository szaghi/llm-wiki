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
**Corpus: 43 of 43 archived sources compiled** (see the [update log](/log.md)).

**Start here:** the [Notation registry](/notation.md), which is normative
for every page.

## Reading guide

1. **The codes.** Start with [Athena](/software/athena.md) and its rewrite
   [Athena++](/software/athena-plus-plus.md), then the other frameworks:
   [PLUTO](/software/pluto.md) (Chombo AMR), [Castro](/software/castro.md)
   (BoxLib AMR, general EOS), [Enzo](/software/enzo.md) (cosmological patch
   AMR), [GAMER](/software/gamer.md) (GPU octree AMR) and
   [RAMSES-RT](/software/ramses-rt.md) (cell-based AMR with radiation),
   [FLASH](/software/flash.md) (PARAMESH block AMR, star formation) and
   [TIGRESS](/software/tigress.md) (Athena-based star-forming ISM).
2. **The GPU codes.** How codes are ported:
   [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md), and how
   their speed is reported: [cell-update throughput](/definitions/cell-updates-per-second.md)
   and [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
   The codes: [AthenaK](/software/athenak.md) (Kokkos rewrite of Athena++),
   [IDEFIX](/software/idefix.md) (Kokkos, PLUTO-compatible),
   [gPLUTO](/software/gpluto.md) (OpenACC rewrite of PLUTO),
   [Cholla](/software/cholla.md) (CUDA/HIP MHD and cosmology), [Quokka](/software/quokka.md)
   (AMReX radiation hydrodynamics), [GRaM-X](/software/gram-x.md) (AMReX GRMHD),
   [H-AMR](/software/h-amr.md) (GPU GRMHD with adaptive time stepping),
   and, outside astrophysics, [ADAM](/software/adam.md) (GPU octree AMR),
   [STREAmS](/software/streams.md) (CUDA Fortran DNS) and
   [Neko](/software/neko.md) (spectral elements).
3. **How they integrate (M)HD.** [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md)
   (CTU, VL2, SSP Runge–Kutta), the reconstruction most of them inherit,
   the [piecewise parabolic method](/methods/ppm.md) (open `Contradictions`
   entry: third or fourth order on non-uniform meshes?), the [Riemann solvers](/methods/approximate-riemann-solvers.md)
   they offer, and the two ways of controlling the magnetic divergence:
   [constrained transport](/methods/constrained-transport.md) and
   [GLM cleaning](/methods/glm-divergence-cleaning.md). Where kinetic energy
   dominates, the [dual-energy formalism](/methods/dual-energy-formalism.md);
   for stiff diffusion, [super-time-stepping](/methods/super-time-stepping.md);
   for keeping the state physical, [density and pressure floors](/methods/numerical-floors.md).
4. **Meshes.** [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md):
   cell, patch and block hierarchies; subcycled against global time steps;
   refluxing and EMF correction.
5. **Physics modules as numerics.** Self-gravity:
   [Poisson solvers on adaptive meshes](/methods/multigrid-self-gravity.md)
   and [conservative self-gravity](/methods/conservative-self-gravity.md);
   [particle-mesh N-body](/methods/particle-mesh-gravity.md) for collisionless matter.
   Radiation: [M1 two-moment transport](/methods/m1-radiation-transport.md)
   and the [reduced speed of light](/definitions/reduced-speed-of-light.md).
   Star formation: [sink particles](/methods/sink-particles.md) and the
   [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md).
   Thermodynamics: [cooling and chemistry integration](/methods/radiative-cooling-integration.md)
   (with the [Grackle](/software/grackle.md) library) and
   [general equations of state](/methods/general-equation-of-state.md).
   Relativity: [primitive-variable recovery](/methods/primitive-variable-recovery.md)
   and [pseudo-Newtonian potentials](/methods/pseudo-newtonian-potentials.md).
6. **Verification.** [Linear wave convergence](/benchmarks/linear-wave-convergence.md),
   [Sod](/benchmarks/sod-shock-tube.md), [Brio–Wu](/benchmarks/brio-wu-shock-tube.md),
   [Orszag–Tang](/benchmarks/orszag-tang-vortex.md),
   [field-loop advection](/benchmarks/field-loop-advection.md),
   [MHD blast wave](/benchmarks/mhd-blast-wave.md),
   [Sedov–Taylor](/benchmarks/sedov-taylor-blast-wave.md),
   [double Mach reflection](/benchmarks/double-mach-reflection.md),
   [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md),
   [Jeans wave](/benchmarks/jeans-wave.md),
   [singular isothermal sphere collapse](/benchmarks/singular-isothermal-sphere-collapse.md),
   [self-gravitating polytrope](/benchmarks/self-gravitating-polytrope.md),
   [hydrostatic white dwarf](/benchmarks/hydrostatic-white-dwarf.md),
   [Shu–Osher](/benchmarks/shu-osher-shock-tube.md),
   [Liska–Wendroff implosion](/benchmarks/liska-wendroff-implosion.md),
   [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md),
   [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
   [relativistic magnetic rotor](/benchmarks/relativistic-magnetic-rotor.md),
   [ambipolar C-shock](/benchmarks/ambipolar-c-shock.md),
   [radiation shadow](/benchmarks/radiation-shadow-test.md),
   [subcritical radiative shock](/benchmarks/subcritical-radiative-shock.md),
   [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md),
   [magnetized torus](/benchmarks/magnetized-torus-accretion.md).
7. **Code comparisons.** The [EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md):
   nine codes on one torus, and what their differences are traced to.

Folder indexes: [Software](/software/index.md) · [Methods](/methods/index.md) ·
[Definitions](/definitions/index.md) · [Operators](/operators/index.md) ·
[Properties](/properties/index.md) · [Results](/results/index.md) ·
[Benchmarks](/benchmarks/index.md) · [Sources](/sources/index.md) ·
[Bibliography](/bibliography.md)
