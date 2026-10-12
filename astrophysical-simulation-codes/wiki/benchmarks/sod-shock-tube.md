---
type: Benchmark
title: "Sod shock tube"
description: "The one-dimensional Riemann problem of Sod, density and pressure 1 | 0.125 and 1 | 0.1 at rest with adiabatic index 1.4, producing a rarefaction, contact and shock; a basic check of shock capturing, including across AMR levels."
status: established
aliases: [Sod problem, Sod's shock tube]
tags: [benchmark, hydro, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Sod shock tube

**Set-up.** Gas at rest with $(\rho, p) = (1, 1)$ on the left and
$(0.125, 0.1)$ on the right of a diaphragm, $\gamma = 1.4$. The exact
solution (a left rarefaction, a contact and a right shock) is known.

**Runs.**

* [Stone et al. (2008)](/sources/stone-2008.md), §8.1, Fig. 8, Table 2.
  100 cells on $-0.5 < x < 0.5$, $t = 0.25$, PPM, HLLC. Shocks and contacts
  are resolved in 2–3 zones. The authors write that the test "should no
  longer be considered a discriminating test".
* [Almgren et al. (2010)](/sources/almgren-2010.md), §8.1.1, eq. 41,
  Fig. 3. Domain $[0, 1]$, interface at 0.5, $t = 0.2$; base grid of 32
  cells with two [AMR](/methods/adaptive-mesh-refinement.md) levels of
  ratio 2 (effective 128), refined on density and velocity gradients; the
  new PPM limiters, CFL 0.9. "Excellent agreement" with the exact solution
  of Toro (1997); qualitative, no error norm. Identical results are
  reported in 2D and 3D with the interface aligned with an axis.
* [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.1, Fig. 4.
  Interface at $x = 0.5$, 100 root cells, $t = 0.25$; PPM, ZEUS and MUSCL
  solvers, on a uniform grid and with 2 AMR levels (ratio 2, refining where
  the normalized density slope exceeds 10%). L1 errors (cell-width-weighted
  sum of absolute deviations from the exact solution):

  | solver | uniform | AMR |
  |---|---|---|
  | PPM | $2.8\times10^{-3}$ | $9.6\times10^{-4}$ |
  | ZEUS | $9.3\times10^{-3}$ | $3.8\times10^{-3}$ |
  | MUSCL | $7.9\times10^{-3}$ | $2.4\times10^{-3}$ |

  PPM is best in both cases.

The Liska–Wendroff implosion uses the Sod states
across a diagonal discontinuity in 2D; it is a symmetry test, not this
benchmark ([Stone et al. (2008)](/sources/stone-2008.md), §8.3;
[Stone et al. (2020)](/sources/stone-2020.md), §3.3.5).

**What it shows.** Stone et al. regard it as no longer discriminating.
Its remaining uses here are solver comparison on equal grids and the
check that AMR across the waves reduces the error (by factors of about
2.4 to 3.3 in the Bryan et al. table).

## Later uses (batch 3)

* [Lesur et al. (2023)](/sources/lesur-2023.md), §4.1, Fig. 2;
  [IDEFIX](/software/idefix.md). $\gamma = 1.4$, $t = 0.2$; Roe, PLM, RK2,
  500 points, against the analytic solution; visual only. Recorded as
  printed: the text gives the left pressure as 0.1, but Fig. 2 shows 1.0,
  the standard Sod value; the right state is printed as
  $(\rho, p) = (0.125, 0.1)$.
* [Caddy & Schneider (2024)](/sources/caddy-2024.md), §4.2.1;
  [Cholla](/software/cholla.md). Not a validation run but a calibration of
  the test suite: Sod results differ by about $5\times10^{-15}$ across
  hardware and compilers, which set the absolute tolerance of $10^{-14}$
  in the code's floating-point comparisons (a comparison passes if either
  this absolute check or a check of at most 4 units in the last place
  passes).

The new run adds nothing beyond the visual agreement already recorded
above, consistent with Stone et al.'s judgement that the test no longer
discriminates. Cholla's use is a different one: a reproducibility
reference for automated testing.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.1.
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §8.1.1 (arXiv v1).
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.1 (arXiv v1).
4. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.1 (arXiv v1).
5. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §4.2.1 (arXiv v2).
