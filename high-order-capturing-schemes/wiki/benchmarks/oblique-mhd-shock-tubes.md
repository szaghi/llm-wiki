---
type: Benchmark
title: "Grid-oblique MHD shock tubes"
description: "One-dimensional MHD Riemann problems (Brio–Wu, Ryu–Jones, and others) rotated against a 2D or 3D Cartesian grid, with shifted-periodic boundaries so that the exact 1D solution is the reference: the standard test of how divergence control behaves at discontinuities, where divergence errors show up as oscillations in the normal field."
status: established
aliases: [rotated shock tube, oblique MHD shock tube, rotated Ryu–Jones problem, rotated Brio–Wu problem]
tags: [benchmark, mhd, riemann-problem, divergence-free, 2d, 3d]
timestamp: 2026-10-13T00:00:00Z
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
  * 3D, rotated by $\tan\theta_{\mathrm{rot}} = -\tfrac12$ and $\tan\phi_{\mathrm{rot}} = 1/(2\sqrt5)$
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

**Later uses (batch 7).**
* *Provenance.* The rotated "Ryu–Jones" problem with two fast shocks, two
  rotational discontinuities, two slow shocks and a contact is Dai and
  Woodward's Table 1a problem, popularized by Ryu and Jones
  ([Ryu & Jones (1995)](/sources/ryu-1995.md), problem 2a;
  [Ryu–Jones shock tubes](/benchmarks/ryu-jones-shock-tubes.md)).
* *Second order, four schemes.* Tóth's 2D tube rotated by $\tan^{-1}2$ with
  $(2, -1)$ shifted boundaries, and the 3D Gardiner–Stone tube on
  $768\times8\times8$: the normal-field $L^1$ error is 9.6 (eight-wave)
  against 0.4 (CT, GLM, EGLM) $\times10^{-2}$ in 2D, and 3.6 against 0.5
  $\times10^{-4}$ in 3D. The eight-wave scheme gives wrong normal-field jumps
  ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.3, Tables 2–3).
* *Entropy-stable GLM* on the Ryu–Jones–Frank colliding-flow tube at
  $\tan^{-1}2$: cleaning cuts the parallel-field error "significantly", and
  the full and Janhunen non-conservative terms are indistinguishable
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §5.5).

**Later uses (batch 17).**
* *Tóth's 2D tube, the source of the batch-7 entry*
  ([Tóth (2000)](/sources/toth-2000.md), §6.3.2, Tables III–V,
  Figs. 10–13). The colliding-flow problem ($\rho = 1$, normal velocity
  $\pm10$, $p = 20$ and 1, parallel and perpendicular field
  $5/\sqrt{4\pi}$, $\gamma = 5/3$), cited to Dai and Woodward and to Ryu,
  Jones and Frank, rotated by $\theta_{\mathrm{rot}} = \tan^{-1}2 \approx 63.4°$
  on $N\times2$ cells. The symmetry runs along $(-2, 1)$, the same line as
  the $(2, -1)$ above, with ghost rows shifted by four cells (Fig. 10);
  minmod, $t = 0.08/\sqrt5$, compared with a 1D run on 1024 cells. On
  $N = 256$ the averaged errors are 0.0231–0.0239 for field-CD, flux-CD,
  projection, flux-CT, the base scheme and transport-flux-CT, 0.0291 for
  field-CT and 0.0307 for the eight-wave scheme, whose normal-field error
  alone is 0.0413 against at most 0.0062 for the others (Table III). The
  eight-wave normal field is wrong by 3–7% between the fast shocks, comes
  from the source terms rather than start-up or splitting, and does not
  converge (Figs. 11–13); at 45° it is wrong by 5–10% (Table V). Each
  conservative scheme keeps only its own discrete divergence at round-off,
  the corner one for CT and the central one for CD, and accuracy shows "no
  straightforward relationship" with either (Table IV).
* *Tóth's 2.5D tube* (§6.3.3, Table VI): the Ryu–Jones problem of the
  batch-7 provenance entry ($\rho = 1.08$, $p = 0.95$ left; $\rho = 1$,
  $p = 1$ right; $B_x = 2/\sqrt{4\pi}$) at 45°, $t = 0.2/\sqrt2$, half of
  Ryu, Miniati, Jones and Frank's. Here the eight-wave scheme is close
  to the best (1.023 times the projection error, Table IX), and field-CT has about 1.5 times the best error.
  The wrong jumps of the eight-wave scheme are therefore problem-dependent.
* *On unstructured triangles* ([Dedner et al. (2002)](/sources/dedner-2002.md),
  §5, Table II, Fig. 4). The same colliding-flow data, $v_x = \pm10$ and
  $\mathbf B = (5, 5, 0)/\sqrt{4\pi}$, run along $x$ on
  $[-0.5, 0.5]\times[-0.25, 0.25]$ on triangles, compared on a cut at
  $y = 0.0424$ with a 1D reference ($h = 0.0002$), first-order Dai–Woodward
  flux. Mixed GLM and EGLM converge at EOC 0.79–1.07 to $L^1$ errors
  0.228 and 0.240 on 1,048,576 elements; Powell's source terms give wrong
  intermediate states, EOC falling 0.880, 0.622, 0.432, divergence errors
  2–3 times larger and negative pressure on the finer grids; uncorrected
  DW fails on all grids
  ([hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).

* *Dai & Woodward's 45° tubes.* Three shock tubes rotated by 45° (chosen so the initial data satisfy the face-flux divergence exactly), $256^2$, parallel field 5, $t = 0.06$, cuts along $y = x$; initial states shown only graphically. Jump conditions are satisfied, which the authors attribute to conserving all eight quantities. In the tube with two fast and two slow shocks, the parallel field dips to about 4.99997 (read from the Fig. 5 axis), "a symptom of truncation errors" ([Dai & Woodward (1998)](/sources/dai-1998.md), §3, Figs. 3–5).

# Citations

1. [Jiang & Wu (1999)](/sources/jiang-1999.md), §3.1.
2. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2 (arXiv v2).
3. [Berta et al. (2024)](/sources/berta-2024.md), §5.1 (arXiv v4).
4. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.5.
5. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.2 (arXiv v2).
6. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.
7. [Ryu & Jones (1995)](/sources/ryu-1995.md), §4.
8. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.3.
9. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.5.
10. [Tóth (2000)](/sources/toth-2000.md), §§6.3.2–6.3.3, Tables III–VI.
11. [Dedner et al. (2002)](/sources/dedner-2002.md), §5, Table II.
12. [Dai & Woodward (1998)](/sources/dai-1998.md), §3, Figs. 3–5.
