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

The test's virtue is that it is *trivial physics with unforgiving
algebra*: any constraint-consistent error channel — wrong stencil, biased
EMF, transfer-operator leakage — shows up as structure the exact solution
forbids.

# Citations

1. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §1, §6.
2. [Fromang et al. (2006)](/sources/fromang-2006.md), §3.
3. [Balsara (2004)](/sources/balsara-2004.md), §7.
4. [Zampa (2024)](/sources/zampa-2024.md), §4.6.4.
