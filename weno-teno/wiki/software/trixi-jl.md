---
type: Software
title: "Trixi.jl"
description: "Trixi.jl is an open-source Julia framework for DGSEM on Cartesian, structured and unstructured curved meshes; the sources use it for entropy-stable and kinetic-energy-preserving flux-differencing schemes, measure its serial performance against FLUXO, and run the KPP subcell-limiting test with it."
status: established
aliases: [Trixi, Trixi.jl framework]
tags: [software, dg, entropy-stable, kinetic-energy-preserving]
timestamp: 2026-10-21T12:00:00Z
---

# Trixi.jl

Trixi.jl is an open-source framework, written in Julia, for the
[DGSEM](/methods/dgsem.md) and its [flux-differencing](/methods/flux-differencing.md)
(split-form, entropy-stable, kinetic-energy-preserving) variants on
quadrilateral and hexahedral elements
([Ranocha et al. (2023)](/sources/ranocha-2023.md), §1, §4). It is one of the
two codes in which Ranocha et al. implement and measure every optimization
of their paper. The other is the Fortran code [FLUXO](/software/fluxo.md).

## Design as reported

**Meshes.** Ranocha et al. (2023), §4.1, report the following costs:

- `TreeMesh` (Cartesian, tree-based) is the fastest, by up to 33 % with the
  cheap flux and up to 20 % with the entropy-conservative flux. The margin is
  about ten percentage points smaller in 2D.
- `StructuredMesh` (curvilinear, structured) is the baseline for the other
  two.
- `P4estMesh` (curvilinear, unstructured) costs about the same as
  `StructuredMesh` in 2D and about 5 % more in 3D.

**Time integration.** Time integration comes from OrdinaryDiffEq.jl. The
benchmarks use 50 steps of a 9-stage, fourth-order FSAL Runge–Kutta method
with error-based step control at tolerance $10^{-8}$ (§4.1).

**Volume fluxes.** The directional Shima et al. flux and the
entropy-conservative Ranocha flux are implemented directly in directional
form, not through rotations. This is the authors' recommendation from
their microbenchmarks (§3.2, §4.2;
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)).

**Inlining.** Marking the volume fluxes `@inline` helps cheap fluxes and
curved meshes most. It gives up to about 2× lower PID on curved meshes,
against about 25 % on `TreeMesh` (§7.3, Fig. 8). PID is the time per
right-hand-side evaluation per DG node.

**Precomputation.** Primitive variables are precomputed per element through
LoopVectorization.jl, which gives 5–25 % on the volume terms (§7.1).

**SIMD.** An explicitly vectorized volume-term kernel uses a per-element
array-of-structures-of-arrays layout, a triangular outer loop exploiting
the skew-symmetry of $M\widetilde D$, and precomputed logarithms. It reaches
vectorization ratios above 98 % and 20–29 % of the FMA peak at $N=3$ on an
Intel Core i7-8700K. Because LLVM's preferred vector width is 256 bits, it
is limited to AVX2 (§4, §8, Table 3).

**Gauss collocation.** The entropy-stable Legendre–Gauss variant is
implemented in the hybridized form (6.1). The solution is stored at LGL
nodes and interpolated to Gauss nodes before each right-hand-side
evaluation, and surface fluxes are computed twice per face (§6).

## Performance relative to FLUXO

With Julia 1.7.0 and bounds checking disabled, serial performance per
degree of freedom is similar to FLUXO's (Ranocha et al. (2023), §4.1,
Fig. 1). The best 3D PIDs at $N=3$ are $2.6\times10^{-8}$ s (Cartesian) and
$4.3\times10^{-8}$ s (curved unstructured) for the Shima et al. flux, and
$4.2\times10^{-8}$ s and $6.5\times10^{-8}$ s for the Ranocha flux (§9). All
timings are single-core.

## Use in the sources

[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) run
the [KPP rotating wave](/benchmarks/kpp-rotating-wave.md) with Trixi.jl. They
compare the standard and the entropy-stable split-form DGSEM with
element-wise shock capturing, at $N=3$ on $32^2$ to $256^2$ elements (§5.1).
Their other tests use FLUXO.

## Qualifications

- PID counts one DG node as one degree of freedom, not node times variable
  (Ranocha et al. (2023), Def. 4.1). Trixi.jl timings are therefore not
  directly comparable with codes that count per variable *(compiler check,
  not in the sources)*.
- MPI parallel performance is not measured in the source. The authors
  expect sublinear scaling up to a full node and close-to-ideal scaling
  across nodes, citing other work (§9).

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §1, §3.2, §4–4.2 Fig. 1 Table 2, Def. 4.1, §6, §7.1–7.3 Fig. 8, §8 Table 3, §9.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5, §5.1.
