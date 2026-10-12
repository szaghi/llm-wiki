---
type: Benchmark
title: "Liska–Wendroff implosion"
description: "A 2D hydrodynamic implosion in a square box with reflecting walls, low-pressure gas in the corner below a diagonal; a jet forms along the diagonal only if the scheme preserves exact x–y symmetry, which needs unsplit integration, direction-unbiased stencils and floating point without fused multiply–add contraction, on CPUs and on GPUs."
status: established
aliases: [LW03 implosion, Liska-Wendroff implosion test, diagonal implosion]
tags: [benchmark, hydro, verification, unsplit, gpu]
timestamp: 2026-10-12T00:00:00Z
---

# Liska–Wendroff implosion

**Set-up.** The implosion test of Liska & Wendroff (§4.7 of their
comparison): the square $[0, 0.3]^2$ with reflecting walls, a
discontinuity along the diagonal $x + y = 0.15$, and $\gamma = 1.4$. The
gas in the corner below the diagonal has the lower density and pressure.
A correct solution develops a jet along the diagonal $x = y$. The problem is symmetric about that diagonal, so any
asymmetry in the solution is a defect of the discretization.

The states are described differently:
* [Stone et al. (2008)](/sources/stone-2008.md) (§8.3) and
  [Stone et al. (2020)](/sources/stone-2020.md) (§3.3.5) describe them as
  the [Sod](/benchmarks/sod-shock-tube.md) states across the 45°
  discontinuity (Stone et al. 2020 refer to Table 1 of Stone et al. 2008);
* [Wibking & Krumholz (2022)](/sources/wibking-2022.md) (§3.1.9) print
  $\rho = 0.125$, $p = 0.14$ for $x + y \le 0.15$ and $\rho = 1$, $p = 1$
  outside.

The inner pressure 0.14 differs from Sod's right-state 0.1. The Athena
and Athena++ pressures are not given numerically in the evidence read, so
whether those runs used 0.1 or 0.14 is not recorded. This is a difference
in what is printed, not a recorded contradiction.

**Runs.**

* [Stone et al. (2008)](/sources/stone-2008.md), §8.3, Fig. 17.
  [Athena](/software/athena.md), $400\times400$, PPM, HLLC, shown at
  $t = 0.045$ and $2.5$. The diagonal jet forms with the unsplit
  integrator but not with dimensionally split ones; the authors conclude
  that the jet is correct and that the problem is a sensitive test of
  symmetry.
* [Stone et al. (2020)](/sources/stone-2020.md), §3.3.5, Fig. 17.
  [Athena++](/software/athena-plus-plus.md), $512^2$, $t = 2.5$,
  characteristic PPM, HLLC, RK3. The solution is symmetric to
  double-precision machine epsilon in all variables, at all resolutions
  and for all solver permutations tried. This requires direction-unbiased
  stencils and value-safe floating point (with the Intel compiler: no
  reassociation and no fused multiply–add contraction). The symmetry is
  also preserved with [AMR](/methods/adaptive-mesh-refinement.md)
  (§3.3.5).
* [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.9, Fig. 8.
  [Quokka](/software/quokka.md) on NVIDIA GPUs, $1024^2$, CFL 0.4,
  $t = 2.5$. The diagonal jet is recovered and the solution is "exactly
  symmetric" only when the RK2-SSP flux sums are coded symmetrically and
  `nvcc` is run with `fmad=false`, since fused multiply–add contraction
  breaks the source-level symmetry (§3.1.9). The PPM interface formula is
  regrouped symmetrically about the interface, after Stone et al. (2020),
  for the same reason (§2.2.1, eq. 22). Qualitative only.

**What it shows.** The three runs agree: the jet is a property of a
discretization that is exactly symmetric under exchange of $x$ and $y$.
Stone et al. (2008) tie it to unsplit integration (see
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md));
Stone et al. (2020) and Wibking & Krumholz (2022) show that exact symmetry
also depends on the order of floating-point operations, so that compiler
contraction into fused multiply–add instructions must be disabled, on
Intel CPUs and on NVIDIA GPUs alike. No source reports an error norm.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.3.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.5.
3. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1, §3.1.9 (arXiv v2).
