---
type: Benchmark
title: "Field-loop advection"
description: "A weak circular loop of magnetic field is advected by a uniform flow oblique to the grid; the retention of loop shape and magnetic energy, and the out-of-plane field staying zero, test how an MHD scheme keeps the divergence-free constraint and its numerical dissipation."
status: established
aliases: [advection of a field loop, Gardiner–Stone field loop]
tags: [benchmark, mhd, verification, constrained-transport, divergence-cleaning, amr]
timestamp: 2026-10-12T00:00:00Z
---

# Field-loop advection

**Set-up.** After Gardiner & Stone (2005): a circular loop of weak
magnetic field, initialized from a vector potential, in a uniform gas
moving at constant velocity oblique to the grid on a periodic domain. The
field is dynamically negligible, so the exact solution is pure
translation. Diagnostics are the loop shape (often through the current
density), the decay of the volume-averaged magnetic energy, and the
out-of-plane field, which must stay zero.

**Runs.**

* *2D, single grid* ([Stone et al. (2008)](/sources/stone-2008.md), §8.4,
  Fig. 21). Parameters deferred to GS05. $256\times128$, PLM, Roe, CTU with
  [constrained transport](/methods/constrained-transport.md), advected twice
  around the domain. The current density $J_z$ is shown and the loop shape
  is "preserved extremely well". With a uniform $v_z \neq 0$, $B_z$ stays
  zero to round-off.
* *3D, two versions* ([Stone et al. (2008)](/sources/stone-2008.md), §8.6).
  (i) A cylindrical loop with $B_z = 0$ and velocity along the grid
  diagonal ($v_z \neq 0$): the $x$–$y$ slice is identical to the 2D result,
  and $B_z = 0$ is kept to round-off. (ii) A loop inclined to the grid and
  advected along a perpendicular diagonal (after Gardiner & Stone 2008),
  domain $(1, 1, 1)$, $128^3$, HLLD, PLM and PPM (Fig. 34): the axial field
  component is zero to truncation error.
* *2D, with AMR and GLM cleaning* ([Mignone et al. (2012)](/sources/mignone-2012.md),
  §5.2, Fig. 11). Domain $[-1,1]\times[-0.5,0.5]$, base $64\times32$;
  $\rho = p = 1$; flow speed $\sqrt5$ at an angle whose sine is
  $1/\sqrt5$; vector potential $10^{-3}$ times (0.3 minus the distance from
  the loop centre) inside radius 0.3 (eq. 57); $t = 2$. Two, three or four
  levels of refinement ratio 2 (effective resolution up to
  $1024\times512$), tagging on the in-plane magnetic energy; WENO
  reconstruction, Roe, CFL 0.4, characteristic tracing,
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) (the only
  divergence control of the AMR version). The volume-averaged $B^2$
  retained rises from about 94% to about 98% of its initial value as
  levels are added (Fig. 11, top); the speed-up over a uniform grid is
  shown only graphically (Fig. 11, bottom).
* *3D through the polar axis* ([Stone et al. (2020)](/sources/stone-2020.md),
  §3.5.2, Fig. 29). A curvilinear variant: spherical-polar mesh
  $0.1 < r < 2$, $0 < \theta < \pi/2$, $0 < \phi < 2\pi$,
  $160\times80\times160$ with logarithmic radial spacing; Cartesian
  advection $v_x = 1$ of a loop centred at $(-\sqrt2/2, 0, \sqrt2/2)$,
  radius 0.5, Gaussian vertical width 0.2 (eq. 29); plasma beta $10^5$;
  PLM, HLLD, $\gamma = 5/3$, $t = 2$. Numerical diffusion appears at the
  loop centre, but the structure is well preserved through the coordinate
  singularity.

**What it shows.** The test isolates divergence control: with
[constrained transport](/methods/constrained-transport.md) the
out-of-plane field stays zero to round-off (or truncation for the
inclined 3D loop) ([Stone et al. (2008)](/sources/stone-2008.md), §8.4,
§8.6); with [GLM cleaning](/methods/glm-divergence-cleaning.md) on
[AMR](/methods/adaptive-mesh-refinement.md), magnetic-energy retention
improves with refinement ([Mignone et al. (2012)](/sources/mignone-2012.md),
§5.2). None of the sources reports a convergence order.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.4, §8.6.
2. [Mignone et al. (2012)](/sources/mignone-2012.md), §5.2.
3. [Stone et al. (2020)](/sources/stone-2020.md), §3.5.2.
