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

* **Read through macro-cells.** At a generic angle the discrete solution
  varies on the grid scale along the fronts, so even an exact-CT scheme
  shows a roughly 10% oscillation of the cell-centered $B_n$ at fast shocks.
  Averaged conservatively onto macro-cells, which are the grid's symmetry
  period ($2\times1$ cells for $\tan^{-1}2$), $B_n$ is constant to
  round-off. Schemes that create a true *jump* in $B_n$ cannot pass this
  test. Removing the cell-level oscillation would need a viscosity stencil
  at least macro-cell-wide
  ([Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) §5.3).

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
* **High-order cleaning at 45° and in 3D**
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md)).
  * 2D Brio–Wu on a $600\times6$ strip. The authors choose $\alpha = 45°$
    because it minimizes the $B_n$ error, which is the configuration the
    angle caveat above calls least discriminating.
  * 3D Ryu–Jones on $768\times8\times8$, rotated by $\tan\alpha = -1/2$,
    $\tan\beta = 1/4$, so that planar symmetry is an integer cell shift.
  * Third- and fifth-order schemes reach $\epsilon_1(B_1) \approx
    2$–$9\cdot10^{-5}$, with a peak $B_n$ oscillation of about 0.7% for
    MP5. Going from third to fifth order gains only a factor 1.5–2 at
    discontinuities.
  * Their divergence monitor is built from reconstructed interface values
    ([GLM](/methods/glm-divergence-cleaning.md)), so its
    $\approx 10^{-2}$ level is not comparable with the monitors above.

* **Base scheme against collocated CT**
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md)). At
  $\alpha = \tan^{-1}0.5$ on $180\times150$, fifth-order FD-WENO without
  CT shows spurious oscillations in density, $B_\perp$ and $B_\parallel$.
  The authors attribute them to divergence errors. With potential-based
  CT the cuts agree with a 5000-cell 1D reference. No divergence norm is
  reported.

# Citations

1. [Tóth (2000)](/sources/toth-2000.md): the rotated shock-tube test and the eight-wave failure.
2. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §4.2, Tables 2–3, Figs. 4–7.
3. [Zaghi (2026)](/sources/zaghi-2026.md): FLUME `verification.md` (MV-8).
4. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §5.3, Fig. 10.
5. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md), §§4.2.1–4.2.2, Table 2, Fig. A.7.
6. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.2, Figs. 2–4.
