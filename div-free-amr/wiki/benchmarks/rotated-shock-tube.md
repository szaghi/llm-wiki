---
type: Benchmark
title: "Rotated shock tube"
description: "1D MHD Riemann problems rotated obliquely to the grid; the exactly constant normal field makes its deviation a direct measure of divergence errors and of non-conservative jump defects."
status: established
aliases: [oblique shock tube]
tags: [benchmark, divergence-constraint, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Rotated shock tube

A one-dimensional MHD Riemann problem whose discontinuities are rotated by
an angle $\alpha$ against the Cartesian grid. In the exact solution the
normal field component $B_n$ is constant, so its numerical deviation
measures the error the divergence constraint should have prevented.
Comparing a cut through the 2D run with a high-resolution 1D reference
also measures the jump conditions.

## Setup

* **Narrow strip** ([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md),
  credited to Tóth): a domain $[0,1]\times[0, 2/N]$ on an $N\times2$ grid
  with shifted periodic boundaries, $\alpha = \tan^{-1}2 \approx 63.4°$. It
  is compared with a 1024-cell 1D run.
* **Choose the angle with care.** If the initial field is uniform, or the
  fronts run along cell sides or diagonals (for example $\alpha = 45°$), every
  discrete divergence stays exactly zero and the test cannot discriminate
  between schemes. At a generic angle the fronts are discretized with unequal
  $x$ and $y$ jumps, so $B_n$ is constant only approximately, even for a
  scheme that holds its divergence exactly.

## What it has shown

* **Non-conservative source terms give wrong jumps.** The
  [eight-wave](/methods/eight-wave.md) scheme produces incorrect jump
  conditions across strong shocks, and they do not converge away with
  resolution ([Tóth (2000)](/sources/toth-2000.md)).
* **Monopoles from collocated fluxes.** Between upwind CT and its collocated
  base scheme with the same solver, the $B_n$ error drops 2.7–21×. The
  central divergence of the interpolated cell-centered field remains
  $O(10$–$100)$ at fronts in both schemes, while the staggered invariant
  stays at round-off
  ([UCT](/methods/upwind-constrained-transport.md);
  [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md)).
* **A cleaning scheme for scale** ([Zaghi (2026)](/sources/zaghi-2026.md),
  hypothesis). Fifth-order WENO with GLM gives
  $\delta B_\parallel = 2.79\cdot10^{-3}$ at 63.4° and $4.17\cdot10^{-3}$ at
  45° (256 cells), first order. The record quotes $3.7\cdot10^{-3}$ at 63.4°
  for Tóth's second-order base scheme. At discontinuities the scheme order
  barely matters for this measure.

# Citations

1. [Tóth (2000)](/sources/toth-2000.md): the rotated shock-tube test and the eight-wave failure.
2. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §4.2, Tables 2–3, Figs. 4–7.
3. [Zaghi (2026)](/sources/zaghi-2026.md): FLUME `verification.md` (MV-8).
