---
type: Benchmark
title: "Shock diffraction at a backward-facing corner"
description: "A Mach 5.09 shock diffracting around a 90° corner: the strong expansion behind the corner drives density and pressure towards zero, so unlimited high-order schemes need ad hoc fixes, and the diffracted normal shock exposes the shock instability of low-dissipation Riemann solvers."
status: established
aliases: [shock diffraction, backward-facing step diffraction]
tags: [benchmark, euler, positivity, 2d, shock-instability]
timestamp: 2026-10-13T00:00:00Z
---

# Shock diffraction at a backward-facing corner

**Set-up.** Domain $[0,1]\times[6,11]\cup[1,13]\times[0,11]$. A
right-moving Mach 5.09 shock starts at $x = 0.5$, $6 \le y \le 11$, into
gas with $\rho = 1.4$, $p = 1$, $\gamma = 1.4$. Inflow at $x = 0$, outflow
on the far boundaries, reflecting walls along the step; $t = 2.3$
([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.5;
[Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.3).

**Results.** Negative density or pressure arises below and to the right
of the corner. Cockburn and Shu's DG needed an ad hoc positivity
correction. With the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md),
RKDG (TVB $M = 100$) and FD WENO5 ($h = 1/80$) never produce negative
values, and their results match the published ones. A reactive variant —
detonation diffraction at a 90° corner — is run with the same limiter
([Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.5).

**Later uses (batch 7).**
* *DG with only the positivity limiter* at $h = 1/64$, degree 2–3 on
  rectangles: the Euler run is highly oscillatory and at degree 3 the
  oscillations shift the shock; the Navier–Stokes run at $\mathrm{Re} = 200$
  is clean ([Zhang (2017)](/sources/zhang-2017.md), Example 7).

**Later uses (batch 8).**
* *A 90° corner in the unit square, as a shock-instability test.* A Mach
  5.09 shock on $[0,1]^2$ with $400\times400$ cells and the corner at
  $(0.05, 0.45)$, run to $t = 0.1561$ at second order. HLLC and HLLEM
  partly distort the diffracted normal shock. Selective wave modification
  and anti-diffusion control keep it, the latter most cleanly
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.6; [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.4).
* With the corner at the middle of the left boundary, $t = 0.15$, second
  order: Godunov, Roe, HLLEM and HLLC all show post-shock oscillations,
  which the entropy-control term removes ([Xie et al. (2021)](/sources/xie-2021.md), §6.2).
* The failure in both is [numerical shock instability](/definitions/numerical-shock-instability.md),
  not positivity.

**Later uses (batch 12).** The experimental background of the 90°
corner, from shock-tube studies at low $M_s$.
* *Regimes.* Behind a shock moving into gas at rest the flow becomes
  supersonic in the laboratory frame above $M_s^* \approx 2.07$
  ($\gamma = 7/5$). Above $M_s^*$, and for corner angles above 75°, the
  pattern is well understood and depends only mildly on $M_s$; for corner
  angles above 75° it does not depend on the angle, so $M_s$ is the only
  parameter at fixed $\gamma$. The transition regime $1.3 < M_s < M_s^*$
  has subsonic post-shock flow but secondary shock systems: a terminator, a
  second shock and shocks on the vortex periphery. A recompression shock
  on the wall side of the vortex appears from $M_s = 1.45$ and becomes an
  almost straight wall-normal shock above $M_s^*$, and all records show a
  density minimum inside the slipstream, so these two are not confined to
  the transition regime ([Kleine et al. (1995)](/sources/kleine-1995.md), §§1, 4).
  The Mach 5.09 runs above lie in the regime above $M_s^*$.
* *Experiment against a second-order Euler run.* Nitrogen, $M_s$ from 1.05
  to 3.0, in a 54.5 mm square shock tube, recorded by shadowgraphy, colour
  schlieren and holographic interferometry. The computation is a
  Godunov-type scheme after Colella & Glaz: piecewise-linear primitive
  variables with the superbee limiter, Roe's
  [approximate Riemann solver](/methods/approximate-riemann-solvers.md),
  Strang splitting in 2D, on a uniform Cartesian grid aligned with the
  corner walls (grid size not stated). Density and density-gradient
  contours "coincide almost perfectly" with the interferograms and
  schlieren records wherever the Euler equations apply ($M_s$ = 1.35/1.34,
  1.58, 1.60, 1.80/1.78), including the vortex. The agreement is visual;
  no data are tabulated. Discrepancies: at $M_s = 1.6$ a shock almost
  parallel to the terminator is seen only in the experiment (also absent
  from Hillier's 1991 simulations, unexplained); the computation shows
  fewer wavelet systems at $M_s = 1.45$ and stronger kinks on the vortex
  periphery, which the authors attribute to the missing friction
  ([Kleine et al. (1995)](/sources/kleine-1995.md), §4, Figs. 2–5).
* *Self-similarity is only approximate.* The Euler pattern is self-similar
  about the corner, but the finite cell size gives the computation a
  length scale, with the strongest effect at early times; viscosity and
  the mean free path do the same in the experiment
  ([Kleine et al. (1995)](/sources/kleine-1995.md), §3).
* *Shock-free supersonic pockets.* The computation shows local supersonic
  regions ($\mathrm{Ma} \ge 1$) for $M_s \ge 1.33$, with no secondary
  shocks. A nozzle analogy requires the ratio of the total pressure behind
  the incident shock to the static pressure ahead of it to reach
  $((\gamma+1)/2)^{\gamma/(\gamma-1)} = 1.893$ for $\gamma = 7/5$, printed
  as $M_s \ge 1.31$; a reader check with the normal-shock relations gives
  about 1.27, and the paper does not print the expression it used, so the
  printed value stands with that caveat. The authors leave open whether
  the pockets are physical ([Kleine et al. (1995)](/sources/kleine-1995.md),
  §4, Eq. 1, Fig. 6).
* *The corner vortex at $M_s = 1.6$ recorded four ways* (shadowgram,
  magnitude and direction colour schlieren, holographic interferogram) in
  nitrogen. The interferogram barely shows the slipstream roll-up and the
  secondary shocks that schlieren resolves. The figure is qualitative; the
  quantitative study it comes from (Kleine, Ritzerfeld & Grönig 2003) is
  not ingested ([Kleine et al. (2006)](/sources/kleine-2006.md), §2.3,
  Fig. 2).
* *A related variant: weak shocks over splitter tips.* $M_s$ = 1.31 and
  1.59 diffracting over a sharp ramp, a sharp symmetric wedge and a rounded
  tip (radius 2.8 mm) leaving a 24.8 mm square tube, recorded by
  schlieren at fixed times. Lambda shocklets on the shear layer appear only
  at 1.59; the rounded tip moves separation downstream, damps the
  Kelvin–Helmholtz instability and keeps the contact surface from rolling
  up. The data are qualitative, and the confining walls of the small test
  section reflect the diffracted shock back onto the vortex, so a
  simulation must include them ([Gnani et al. (2014)](/sources/gnani-2014.md),
  §§2–4).

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.5.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Examples 5.3, 5.5.
3. [Zhang (2017)](/sources/zhang-2017.md), Example 7.
4. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.6.
5. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.4.
6. [Xie et al. (2021)](/sources/xie-2021.md), §6.2.
7. [Kleine et al. (1995)](/sources/kleine-1995.md), §§1–4, Eq. 1, Figs. 1–6.
8. [Kleine et al. (2006)](/sources/kleine-2006.md), §2.3, Fig. 2.
9. [Gnani et al. (2014)](/sources/gnani-2014.md), §§1–4.
