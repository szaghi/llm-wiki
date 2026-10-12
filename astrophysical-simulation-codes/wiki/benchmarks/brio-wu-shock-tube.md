---
type: Benchmark
title: "Brio–Wu MHD shock tube"
description: "The one-dimensional MHD Riemann problem of Brio and Wu with normal field 0.75 and adiabatic index 2, whose fast rarefactions, compound wave, contact and slow shock test MHD Riemann solvers and the variables in which states are reconstructed."
status: established
aliases: [Brio-Wu, Brio and Wu shock tube]
tags: [benchmark, mhd, riemann-solver, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Brio–Wu MHD shock tube

**Set-up.** A 1D MHD Riemann problem with normal field $B_x = 0.75$ and
$\gamma = 2$ (Brio & Wu 1988). The left and right states are tabulated in
[Stone et al. (2008)](/sources/stone-2008.md), Table 2, and not reproduced
here. Solutions are compared with high-resolution reference runs.

**Runs.**

* [Stone et al. (2008)](/sources/stone-2008.md), §8.2, Fig. 13. PLM, Roe,
  CTU, $t = 0.08$, reference solution with $10^4$ points. Shocks and
  contacts are captured in 2–3 zones. PPM gives small velocity
  oscillations, and the authors write that "our TVD limiters could be
  improved". The resolution is printed inconsistently: 800 zones in the
  text, 400 in the Fig. 13 caption.
* [Stone et al. (2020)](/sources/stone-2020.md), §3.3.3, Fig. 15.
  $N = 256$, HLLD, characteristic reconstruction, $t = 0.1$, reference
  with $N = 8192$. Reconstruction in primitive
  variables gives significant oscillations behind the right-moving fast
  rarefaction, so characteristic reconstruction is needed; RK3+PPM gives a
  slightly sharper rarefaction head and foot.

The two sources print different output times (0.08 and 0.1).

**What it shows.** Both sources use it to examine oscillations next to
MHD waves: [Stone et al. (2008)](/sources/stone-2008.md) attribute residual
PPM oscillations to the limiters, and
[Stone et al. (2020)](/sources/stone-2020.md) show that the choice of
reconstruction variables decides whether they appear. No error norms are
reported. See also [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.2, Table 2.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.3.
