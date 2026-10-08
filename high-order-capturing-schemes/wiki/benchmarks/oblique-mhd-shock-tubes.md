---
type: Benchmark
title: "Grid-oblique MHD shock tubes"
description: "One-dimensional MHD Riemann problems (Brio–Wu, Ryu–Jones, and others) rotated against a 2D or 3D Cartesian grid, with shifted-periodic boundaries so that the exact 1D solution is the reference: the standard test of how divergence control behaves at discontinuities, where divergence errors show up as oscillations in the normal field."
status: established
aliases: [rotated shock tube, oblique MHD shock tube, rotated Ryu–Jones problem, rotated Brio–Wu problem]
tags: [benchmark, mhd, riemann-problem, divergence-free, 2d, 3d]
timestamp: 2026-10-08T00:00:00Z
---

# Grid-oblique MHD shock tubes

**Why rotate.** A 1D MHD Riemann problem aligned with a grid axis has a
constant normal field, so no divergence error can arise. Rotated against
the grid, the normal field must stay constant across every wave, and any
divergence error appears as oscillation in it. With the rotation chosen
so that the planar symmetry is an integer cell shift, the boundaries can
be shifted-periodic and the run compared with a fine 1D solution.

**Variants and results.**
* *Rotated [Brio–Wu](/benchmarks/brio-wu-shock-tube.md).*
  * 45° on $600^2$, with a divergence projection: matches 1D. Without the
    projection there are oscillations near the slow rarefaction
    ([Jiang & Wu (1999)](/sources/jiang-1999.md), §3.1).
  * 45° on $600\times6$ cells with shifted-periodic boundaries, GLM
    cleaning, $\gamma = 2$: $L^1$ density errors $4.11\times10^{-3}$
    (WENO+3), $3.61\times10^{-3}$ (LimO3), $2.72\times10^{-3}$ (WENO-Z) and
    $2.31\times10^{-3}$ (MP5). MP5 keeps the normal field constant to about
    0.7%. Going from third to fifth order gains only a factor 1.5–2
    ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.1;
    [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
* *Rotated Ryu–Jones problems* (two fast shocks, two slow shocks, two
  rotational discontinuities and a contact).
  * 3D, rotated by $\tan\alpha = -\tfrac12$ and $\tan\gamma = 1/(2\sqrt5)$
    on $768\times8\times8$ cells: $L^1$ density errors from
    $1.82\times10^{-3}$ (WENO+3) to $1.07\times10^{-3}$ (MP5), with no
    prominent overshoots
    ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.2).
  * The same rotation with fourth-order finite volume and upwind CT, for
    MHD and relativistic MHD. It matches a 16384-point reference, with
    normal-field oscillations comparable to Mignone et al.'s and smaller
    than Gardiner and Stone's. The order drops to first at the
    discontinuities ([Berta et al. (2024)](/sources/berta-2024.md), §5.1).
  * 2D at 45° on $256^2$ (the Ryu–Jones–Frank problem): all seven
    discontinuities are correct, shocks span 2–3 cells, and high-order CT
    costs no robustness. Rotational and contact discontinuities are sharper
    than with a second-order TVD code
    ([Seo & Ryu (2023)](/sources/seo-2023.md), §3.5).
* *Helzel–Rossmanith states*, $\gamma = 5/3$, rotated by $\tan^{-1}\tfrac12$
  on $180\times150$: the base FD-WENO scheme without CT oscillates, while
  unstaggered CT matches a 1D reference
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.2;
  [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6;
  [constrained transport](/methods/constrained-transport.md)).

# Citations

1. [Jiang & Wu (1999)](/sources/jiang-1999.md), §3.1.
2. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2 (arXiv v2).
3. [Berta et al. (2024)](/sources/berta-2024.md), §5.1 (arXiv v4).
4. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.5.
5. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.2 (arXiv v2).
6. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.
