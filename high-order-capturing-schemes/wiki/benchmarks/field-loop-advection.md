---
type: Benchmark
title: "Magnetic field-loop advection"
description: "A weak cylindrical current loop (A_z = A_0(R − r) inside radius R) advected obliquely across a periodic box: a pure test of how a scheme transports a discontinuous magnetic field, measured by the loop's shape, its spurious oscillations and the decay of magnetic energy."
status: established
aliases: [field loop, magnetic loop advection, Gardiner–Stone loop]
tags: [benchmark, mhd, divergence-free, dissipation, 2d, 3d]
timestamp: 2026-10-08T00:00:00Z
---

# Magnetic field-loop advection

**Set-up** (Gardiner and Stone, as used by the sources below). On
$[-1, 1]\times[-\tfrac12, \tfrac12]$, periodic, a loop of radius $R = 0.3$
is set from the vector potential $A_z = A_0(R - r)$ for $r \le R$, with
$A_0 = 10^{-3}$, so the magnetic pressure is negligible and the field is
advected passively by a uniform flow of speed $\sqrt5$ at $\tan\theta = 1/2$
to the mesh. The field is discontinuous at the rim and singular at the
centre. Some versions modify $A_z$ for $r \le 0.2R$ to remove the
central singularity.

**Results.**
* With GLM cleaning, $128\times64$ to $t = 2$: third order is more diffusive
  than fifth, and MP5 is the least diffusive. In 3D (a loop rotated by
  $\tan^{-1}\tfrac12$, $128\times128\times256$, $t = 1$) all schemes keep the
  loop circular. The divergence error is smallest for $\alpha_p \gtrsim 0.4$
  at fifth order and $\alpha_p \lesssim 0.2$ at third
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.4;
  [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
* With staggered CT, $256\times128$, $t = 2$ and 20: second-order CT
  distorts the loop, while fourth- and sixth-order CT keep it circular and
  remove the perimeter oscillations almost completely. At $t = 20$ and
  $N = 128$ about 96% of the magnetic energy remains, against 95% for the
  second-order CT. A grazing case ($\tan\theta = 1/100$) shows oscillations
  of a few percent that do not grow, and a tilted 3D cylindrical loop is
  preserved ([Seo & Ryu (2023)](/sources/seo-2023.md), §3.3;
  [constrained transport](/methods/constrained-transport.md)).
* Fourth-order finite volume with upwind CT, $256\times128$, two periods,
  MHD and relativistic MHD: WENO-Z is best. MP5 shows small over- and
  undershoots at the loop's head and tail, and second order loses
  magnetic energy fastest. The choice of Riemann solver matters only
  marginally. Fifth-order FD also loses about 5% of the magnetic energy
  ([Berta et al. (2024)](/sources/berta-2024.md), §5.4).

# Citations

1. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.4 (arXiv v2).
2. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.3.
3. [Berta et al. (2024)](/sources/berta-2024.md), §5.4 (arXiv v4).
