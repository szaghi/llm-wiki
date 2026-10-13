---
type: Benchmark
title: "Orszag–Tang vortex (2D MHD)"
description: "Smooth periodic MHD data that steepen into interacting shocks and current sheets; the standard 2D test of shock capturing and divergence control in ideal MHD."
status: established
aliases: [Orszag-Tang problem, Orszag-Tang vortex]
tags: [benchmark, mhd, 2d, divergence-free]
timestamp: 2026-10-13T00:00:00Z
---

# Orszag–Tang vortex

**Set-up.** Doubly periodic; in the normalization of Christlieb et al.
$\rho = \gamma^2$, $\mathbf v = (-\sin y, \sin x, 0)$,
$\mathbf B = (-\sin y, \sin 2x, 0)$, $A_z(0) = \frac12\cos 2x + \cos y$ on
$[0, 2\pi]^2$, $\gamma = 5/3$
([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.3).

**Results.**
* PIF-WENO with unstaggered [constrained transport](/methods/constrained-transport.md)
  agrees with the literature at $t = 0.5, 2, 3, 4$ on $192^2$. Without CT
  non-physical features appear by $t = 1.5$ and the run crashes at
  $t = 1.67$. The positivity limiter, not needed here, changes little
  ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.3, Figs. 4–6).
  Run to $t = 30$, the energy error from the limiter's correction stays
  small and decreases with refinement (§6.7).
* Divergence-preserving AFD-WENO with a Yee-staggered field performs
  well at third to ninth order
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2).

**Later uses (batch 4).** In the $4\pi$-scaled normalization
($\rho = \gamma^2$, $p = \gamma$,
$\mathbf B = \sqrt{4\pi}(-\sin y, \sin 2x)$, $\gamma = 5/3$) with GLM
divergence cleaning:
* third-order ADER-WENO with AMR (equivalent $800^2$) to $t = 5$
  matches the uniform fine grid, Jiang and Wu's fifth-order FD-WENO and
  an unstructured WENO solution, at 1.8 times less CPU ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4);
* ADER-DG with $K = 5$, subcell limiting and AMR (equivalent $270^2$)
  agrees with the uniform grid and the same references ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.2).

**Later uses (batch 5).** Jiang and Wu state the same set-up with
$p = \gamma$ and unscaled $\mathbf B$, "identical to Zachary et al.",
and run fifth-order FD-WENO on $192^2$
([Jiang & Wu (1999)](/sources/jiang-1999.md), §3.4):
* $L^1$ density errors against a $512^2$ reference fall from
  $1.8\times10^{-2}$ ($16^2$) to $6.8\times10^{-7}$ ($256^2$) at
  $t = 0.2$, with orders 2.4, 3.6, 4.3 and 4.4 (Table VI). By $t = 0.5$ the
  global order drops to 2.6–3.4 (Table VII).
* Without a divergence projection the pressure turns negative and the
  run fails at $t \approx 3.9$ or 2.5, depending on the eigensystem.
  With it, the run is stable to $t = 8$
  ([projection](/methods/constrained-transport.md)).
* At $t = 3$ the result agrees with Zachary et al., and a pressure cut at
  $y = 0.625\pi$ is more oscillatory without the projection (Fig. 15).

**Later uses (batch 6).**
* The original unstaggered-CT FD-WENO, same set-up on $192^2$, runs to
  $t = 30$ with no negative pressure anywhere. Its base scheme without CT
  reaches negative pressure at about $t = 4.0$
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.3).
* *On $[0, 1]^2$* ($\mathbf v = (-\sin 2\pi y, \sin 2\pi x)$,
  $\mathbf B = (-\sin 2\pi y, \sin 4\pi x)$) with GLM cleaning on $256^2$: at
  $t = 1$ the fifth-order schemes, MP5 especially, form a central magnetic
  island with a dense spot that third order misses. The authors attribute
  it to lower effective resistivity at the central current sheet
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.5).
* Fourth-order finite volume with upwind CT resolves the central island
  already on $64^2$ with MP5 and HLLD. A relativistic version with halved
  velocity shows several islands on $1024^2$
  ([Berta et al. (2024)](/sources/berta-2024.md), §5.6).
* $200^2$, fifth-order FV-WENO: without divergence projection and
  positivity limiter the code fails at $t = 3.11$, and without the
  projection alone it oscillates severely by $t = 4$. With the projection
  the discrete divergence of the traces stays near $10^{-14}$
  ([Ding & Wu (2024)](/sources/ding-2024.md), Example 4.2).

**Later uses (batch 7).**
* *Divergence history on block AMR* (to $256^2$, $t = 0.5$): without
  cleaning the integrated divergence grows to about 1.07, with
  entropy-stable GLM it stays at 0.17–0.19, and density and pressure lose
  the oscillations of the uncleaned run ([Derigs et al. (2018)](/sources/derigs-2018.md), §5.4).
* *Relativistic Orszag–Tang* on $1000^2$ to $t = 0.8$ with fourth-order
  ADER-WENO ([Balsara (2017)](/sources/balsara-2017-d.md), §IX.7).

**Later uses (batch 11, Balsara & Nkonga; merged at the 2026-10-13 deep
lint).** *Relativistic Orszag–Tang* on the unit square with $1000^2$
cells to $t = 0.8$, fourth-order ADER–WENO with the multidimensional HLLI
(MuSIC) solver; the result is shown qualitatively
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.6;
[multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).
Same grid, order and end time as the review's run in the batch-7 entry
above.

**Later uses (batch 17).** *Seven divergence treatments, one code*
([Tóth (2000)](/sources/toth-2000.md), §6.4, Table VII, Fig. 16). On
$[0, 2\pi]^2$ with $\rho = 25/9 = \gamma^2$, $p = 5/3 = \gamma$,
$\mathbf v = (-\sin y, \sin x)$, $\mathbf B = (-\sin y, \sin 2x)$ (the
unscaled normalization of Jiang and Wu above), $\gamma = 5/3$, $N = 50$,
100, 200, with errors averaged against two $400^2$ references (projection
and field-CT):
* at $t = 1$, the averaged relative $L^1$ error on $200^2$ runs from 0.0026 (field-CD) and 0.0029
  (field-CT) to 0.0045 (transport-flux-CT), a rate of about 1.6;
* at $t = 3.14$, from 0.0300 (field-CD) and 0.0340 (projection) to 0.0478
  (eight-wave) and 0.0705 (the base scheme, which needed the minmod
  limiter at $N = 200$: with MC it fails), a rate of about 1;
* field-CT and field-CD look sharpest, but field-CT has spurious features.

* *What Zachary et al. state.* $192^2$, periodic, $\mathbf v = (-\sin y, \sin x)$, $\mathbf B = (-\sin y, \sin 2x)$ (unscaled), Mach number 1 and plasma beta 10/3. $\gamma$, the base density and pressure, and the domain are not stated, and the printed definitions of the Mach number and beta are garbled. One time is shown, "after 300 timesteps (approximately 2 Alfvén transit times)", with a pressure cut at grid row 60. No $t = 3$ is printed ([Zachary, Malagoli & Colella (1994)](/sources/zachary-1994.md), §3.2.2, Fig. 9). Jiang and Wu's "identical to Zachary et al." and their agreement "at $t = 3$" are their statements; this paper alone cannot confirm $p = \gamma$ or the time.
* *A $[0,1]^2$ normalization.* $\mathbf v = (-\sin 2\pi y, \sin 2\pi x)$, $\mathbf B = (-\sin 2\pi y, \sin 4\pi x)$, Gaussian plasma beta 10/3 and Mach number 1, $128^2$–$512^2$, $t = 0.5$, qualitative only, attributed to Dahlburg and Picone (1989) and Picone and Dahlburg (1991) ([Dai & Woodward (1998)](/sources/dai-1998.md), Figs. 6–7).

**Later uses (batch 18).** *The origin, and an isothermal variant.*
* *Origin* ([Orszag & Tang (1979)](/sources/orszag-1979.md), §§2–3,
  eq. 7). The 1979 problem is **incompressible, viscous and resistive** 2D
  MHD in vorticity–vector-potential form, solved by a Fourier
  pseudospectral method on a $2\pi$-periodic square, as a study of
  small-scale structure and possible finite-time singularities in 2D MHD
  turbulence. Its initial condition is $\mathbf v = (-\sin y, \sin x)$,
  $A_z = \cos y + \tfrac12\cos 2x$, hence $\mathbf B = (-\sin y, \sin 2x)$,
  the velocity and field of the set-up above. It has no density, pressure,
  $\gamma$, sound speed, Mach number or plasma beta, so no shocks can form;
  the field is the curl of $A_z$, so $\nabla\cdot\mathbf B = 0$ holds by
  construction. Runs use viscosity = diffusivity from 0.08 down to 0.005
  (up to $256^2$ modes), field plots at $t = 1$ only (an S-shaped central
  current structure, Fig. 7) and integral diagnostics to $t = 2$ and 4.5.
* *A qualification of the description.* "Smooth periodic MHD data that
  steepen into interacting shocks" describes the compressible adaptation,
  not the 1979 problem: the density, pressure, $\gamma = 5/3$, Mach number
  1 and plasma beta 10/3 of the sections above are later additions,
  attributed by Dai and Woodward to Dahlburg and Picone (1989) and Picone
  and Dahlburg (1991). The magnetic island and central current sheet
  discussed in the batch-6 entries sit where the original shows its
  central current structure, under different equations (historical
  context only).
* *Isothermal Orszag–Tang* ([Balsara (1998)](/sources/balsara-1998-b.md),
  §6.2.1, Figs. 7–8). $(0, 2\pi)^2$, $200^2$, $\rho = 1$,
  $\mathbf v = v_0(-\sin y, \sin x)$, $\mathbf B = B_0(-\sin y, \sin 2x)$,
  $v_0$ equal to the isothermal sound speed, $B_0$ set by gas pressure over
  rms magnetic pressure $= 10/3$, $t = 3.0$, second-order TVD. A
  Strang-split run without cleaning and an unsplit run with a spectral
  projection every step give "reasonably similar" density and total
  pressure; the split, uncleaned kinetic energy shows "two tiny
  concentrations at the center that dominate the entire flow field". Since
  splitting and cleaning change together, the difference cannot be
  attributed to cleaning alone (reader's observation); the paper presents
  it as evidence that cleaning matters
  ([constrained transport](/methods/constrained-transport.md)).

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§6.3, 6.7.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2.
3. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4, Table 5.
4. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.2.
5. [Jiang & Wu (1999)](/sources/jiang-1999.md), §3.4, Tables VI–VII.
6. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.3 (arXiv v2).
7. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.5 (arXiv v2).
8. [Berta et al. (2024)](/sources/berta-2024.md), §5.6 (arXiv v4).
9. [Ding & Wu (2024)](/sources/ding-2024.md), Example 4.2 (arXiv v1).
10. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.4.
11. [Balsara (2017)](/sources/balsara-2017-d.md), §IX.7.
12. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.6.
13. [Tóth (2000)](/sources/toth-2000.md), §6.4, Table VII.
14. [Zachary, Malagoli & Colella (1994)](/sources/zachary-1994.md), §3.2.2, Fig. 9.
15. [Dai & Woodward (1998)](/sources/dai-1998.md), §3, Figs. 6–7.
16. [Orszag & Tang (1979)](/sources/orszag-1979.md), §§2–3, eq. 7, Figs. 1–12.
17. [Balsara (1998)](/sources/balsara-1998-b.md), §6.2.1, Figs. 7–8.
