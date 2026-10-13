---
type: Benchmark
title: "Field-loop advection"
description: "A weak circular loop of magnetic field is advected by a uniform flow oblique to the grid; the retention of loop shape and magnetic energy, and the out-of-plane field staying zero, test how an MHD scheme keeps the divergence-free constraint and its numerical dissipation."
status: established
aliases: [advection of a field loop, Gardiner–Stone field loop]
tags: [benchmark, mhd, verification, constrained-transport, divergence-cleaning, amr]
timestamp: 2026-10-13T00:00:00Z
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

## Later uses (batch 3)

* *3D, tilted spherical loop, GPU code*
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.3, eq. 36,
  Figs. 4–5; [Cholla](/software/cholla.md)). A new 3D variant: the loop is
  spherical and tilted, from a vector potential whose $y$ and $z$
  components equal $10^{-3}$ times (0.3 minus the distance from the
  centre) inside radius 0.3 and whose $x$ component is zero; $\rho = 1$,
  $p = 1$, $\mathbf v = (1, 1, 2)$; domain $1\times1\times2$ centred at
  the origin, $N\times N\times2N$ with $N = 32$, 64, 128, 256; $t = 2$
  (two periods); VL+CT with HLLD and PPM with characteristic limiting.
  At $t = 2$ the volume-averaged $B^2$ normalized to its initial value is
  about 0.97 at $N = 256$ and about 0.80 at $N = 32$ (read from Fig. 4,
  left); the dissipation rate "improves at approximately first order",
  "comparable" to Stone et al. (2008). The maximum $|\nabla\cdot\mathbf B|$
  stays at about $10^{-17}$–$10^{-15}$, "near round off", for the whole
  run (Fig. 4, right), and the field outside the loop stays near zero.
  The loop images (Fig. 5) use PLM because "PPMC introduced spurious
  oscillations in the direction of advection".

Cholla's "approximately first order" is a qualitative reading of Fig. 4
with no fitted rate, so it qualifies the statement above that none of the
sources reports a convergence order. The divergence result agrees with
the [constrained-transport](/methods/constrained-transport.md) runs above:
round-off level throughout.

## Later uses (batch 6)

* *2D, origin of the test* ([Gardiner & Stone (2005)](/sources/gardiner-2005.md),
  §3.3.1, §5.1, eq. 53, Figs. 1–3, 6–8; arXiv v1). The set-up the runs
  above defer to: domain $[-1,1]\times[-0.5,0.5]$ on $2N\times N$ cells with
  $N = 64$, periodic; $\rho = 1$, $p = 1$; velocity of magnitude $\sqrt5$
  with components $(2, 1, 0)$, one orbit along the grid diagonal by
  $t = 1$, or zero for a pure diffusion test; in-plane field from a $z$
  vector potential $10^{-3}(0.3 - r)$ inside radius 0.3, zero outside;
  plasma beta $2\times10^6$ inside. These agree with the parameters
  Mignone et al. (2012) print above, on a twice finer base grid.
  * *First-order scheme, three corner-EMF variants* (§3.3.1, $t = 2$). A
    stationary loop: the Lax–Friedrichs variant shows "unacceptable"
    diffusion (a central hole by reconnection), $\mathcal E_z^\circ$ and
    $\mathcal E_z^c$ are "essentially identical". An advected loop:
    $\mathcal E_z^\circ$ develops oscillations that dominate by $t = 2$.
    Without the multidimensional terms in the characteristic step, "the
    field loop disintegrates in oscillations before completing a fraction
    of an orbital period". The test thus separates corner-EMF dissipation
    and the treatment of the normal-field derivative; see
    [constrained transport](/methods/constrained-transport.md).
  * *Second-order CTU+CT* (§5.1, $128\times64$, $t = 2$, $\mathcal E_z^c$,
    Roe). Dissipation concentrates at the loop centre and edge, where the
    initial current is singular. The volume-averaged $B^2$ fits
    $3.463\times10^{-8}\left[1 - (t/10{,}614)^{0.2914}\right]$ (Fig. 7),
    falling to about $3.1\times10^{-8}$ by $t = 2$ (plot reading), i.e. to
    about 90 % of its initial value (computed here). Field lines, contours
    of the vector potential rebuilt from the face fields, stay circular;
    the innermost is dissipated by $t = 2$. Diagnostics are magnetic
    pressure, field lines and the $B^2$ history, not the current density.
  * With uniform $v_z$ the out-of-plane field stays at round-off "with an
    incoherent structure", attributed to where the $v_z\,\partial_xB_x$
    term is placed in the integrator (§4.1.2; asserted, no figure). This
    agrees with the round-off result of Stone et al. (2008) above.

The original runs one resolution, and its fit is a decay law in time, not
an order in $h$; the statement above that no source reports a convergence
order is unchanged by it.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.4, §8.6.
2. [Mignone et al. (2012)](/sources/mignone-2012.md), §5.2.
3. [Stone et al. (2020)](/sources/stone-2020.md), §3.5.2.
4. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.3 (arXiv v2).
5. [Gardiner & Stone (2005)](/sources/gardiner-2005.md), §§3.3.1, 4.1.2, 5.1, eq. 53 (arXiv v1).
