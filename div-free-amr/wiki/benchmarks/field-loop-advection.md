---
type: Benchmark
title: "Field-loop advection"
description: "Passive advection of a weak magnetic loop; the standard detector of divergence-constraint violations and stencil inconsistency in MHD schemes."
status: established
tags: [benchmark, divergence-constraint, mhd, constrained-transport]
timestamp: 2026-07-08T00:00:00Z
---

# Field-loop advection

A weak magnetic field loop (magnetic pressure dynamically negligible) is
advected by a uniform velocity across a periodic domain; the exact
solution is pure translation. Sensitive quantities: preservation of the
loop's shape, decay of magnetic energy, and — the diagnostic that made
the test canonical — spurious growth of field components that should stay
identically zero.

**Origin.** The 2D form was introduced by
[Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) §3.3.1. A loop
with $A_z = A_0(R - r)$ and $\beta = 2\cdot10^6$ is advected along the
diagonal of a periodic $2N\times N$ grid, so the field is effectively a
passive scalar. Its first job there was to discriminate the dissipation of
corner-EMF algorithms: an unbiased EMF goes oscillatory and a
Lax–Friedrichs one diffuses. It also exposes missing multidimensional
source terms in the interface states: without them "the field loop
disintegrates in oscillations before completing a fraction of an orbital
period".

## What it detects, per the compiled sources

* **Stencil inconsistency** (the sharpest use): in 3D, a loop confined to
  the $(x,y)$-plane advected with $v_z \ne 0$ grows spurious $B_z$ unless
  the divergence is held **on the same stencil used to construct the
  $B_z$ fluxes**; round-off-constant $B_z$ certifies consistency
  ([Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), where the
  test motivates the divergence-balanced PPM source terms —
  [exact discrete divergence](/properties/exact-discrete-divergence.md)).
* **EMF-assembly dissipation**: magnetic-energy decay differentiates
  Riemann-solver and EMF-averaging choices
  ([Fromang et al. (2006)](/sources/fromang-2006.md), Roe vs
  Lax–Friedrichs; [Balsara (2004)](/sources/balsara-2004.md) test suite).
* **Constraint machinery on unstructured/hybrid meshes**: 2D and 3D loop
  advection validates the exactly divergence-free hybrid schemes of
  [Zampa (2024)](/sources/zampa-2024.md).
* **A cleaning scheme across 2:1 seams** ([Zaghi (2026)](/sources/zaghi-2026.md),
  hypothesis). Collocated WENO MHD with
  [GLM](/methods/glm-divergence-cleaning.md), with a $v_z$ component so that
  $\partial_t B_z$ measures the divergence error.
  * The generated $\langle|B_z|\rangle$ stays at the cleaning level and
    decreases under refinement.
  * Magnetic energy retained at 64/128 cells: 0.872/0.937 with flux
    splitting, 0.887/0.944 with HLLD on characteristic variables.
  * On a 2:1 grid, the compiler's reading of the captured histories: the
    seam divergence peaks when the loop crosses the seam
    ($9.75\cdot10^{-4}$ at $t \approx 0.38$, 64²), not at the first step as
    the code's docs state. It then decays about 3×, to the uniform-grid
    interior level, by $t = 1$.
  * In a scheme without an exact invariant the test therefore reads the
    seam as one more truncation source, not as a distinct defect.

The test's virtue is that it is *trivial physics with unforgiving
algebra*: any constraint-consistent error channel — wrong stencil, biased
EMF, transfer-operator leakage — shows up as structure the exact solution
forbids.

# Citations

1. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §1, §6.
2. [Fromang et al. (2006)](/sources/fromang-2006.md), §3.
3. [Balsara (2004)](/sources/balsara-2004.md), §7.
4. [Zampa (2024)](/sources/zampa-2024.md), §4.6.4.
5. [Zaghi (2026)](/sources/zaghi-2026.md): FLUME `verification.md` (MV-9, "MHD on weno-riemann" table); captured field-loop div(B) histories.
6. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §§3.1, 3.3.1, 5.1.
