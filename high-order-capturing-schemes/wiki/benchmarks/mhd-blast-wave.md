---
type: Benchmark
title: "MHD blast wave in a low-β medium"
description: "An over-pressured region expanding into a strongly magnetized, low-pressure background; strong anisotropic shocks against tiny thermal pressure make it the standard positivity stress test for MHD, also run in relativistic MHD."
status: established
aliases: [magnetized blast wave, MHD blast problem, RMHD blast wave]
tags: [benchmark, mhd, positivity, low-beta, 2d, 3d]
timestamp: 2026-10-09T00:00:00Z
---

# MHD blast wave in a low-β medium

**Set-up.** A piecewise-constant pressure — high inside a small
sphere, low outside — with constant density, zero velocity and a
uniform oblique field $B_x = B_y = 100/\sqrt{8\pi}$
([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.6). Wu and
Shu's two variants, BLAST-I and BLAST-II, differ in field and pressure
strengths ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2).
The relativistic version follows Komissarov and Mignone–Bodo: domain
$[-6,6]^2$, explosion density $10^{-2}$ and pressure 1 within radius
0.8, ambient $10^{-4}$ and $5\times10^{-4}$ beyond radius 1, field 0.1,
$\gamma = 4/3$, $t = 4$ (§7.3).

**Results.**
* PIF-WENO with CT: negative pressure appears at the first (2D, $256^2$)
  or second (3D, $150^3$) step without the positivity limiter. With it
  the results match the literature at $t = 0.01$, and the limiter's
  energy error stays below 1% except on the coarsest meshes
  ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §§6.6–6.7).
* Divergence-preserving AFD-WENO needs its PCP variant for both
  variants (3D $300^3$; 2D $400^2$, fifth order, $t = 0.01$), and runs
  the RMHD blast at fifth order on $512^2$
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§7.2–7.3;
  [flux limiter](/methods/positivity-preserving-flux-limiter.md)).

**Later uses (batch 4).** Balsara and Spicer's 2D blast on
$[-0.5, 0.5]^2$, $200^2$, ambient plasma beta $2.51\times10^{-4}$,
$t = 0.01$, and a stricter 3D version on $151^3$ with $\gamma = 1.4$.
Fourth-order ADER-WENO with HLL captures the nearly circular, then
nearly spherical, fast shock crisply, without oscillations, and keeps
the pressure positive. The authors credit the divergence-free
reconstruction of the zone-centred field
([Balsara et al. (2009)](/sources/balsara-2009.md), §§7.4–7.5; [constrained transport](/methods/constrained-transport.md)).

**Later uses (batch 6).**
* *Second order, $200^2$, $t = 0.01$, ambient beta $2.51\times10^{-4}$.*
  Pressure stays positive with fast TVD slopes, and with $r = 3$ WENO
  slopes held by a multidimensional limiter. The limiter alone gives a
  small pressure drop at oblique shock segments. One Riemann problem per
  face with averaged edge fields does not evolve the pressure properly
  ([Balsara (2004)](/sources/balsara-2004.md), §7.3;
  [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
  Fourth-order RK-WENO captures the fast shock crisply with positive
  pressure ([Balsara (2009b)](/sources/balsara-2009-b.md), §5.3).
* *Field along $x$*, $B = 100/\sqrt{4\pi}$, $p = 10^3$ inside $\varrho = 0.1$ and
  0.1 outside, $200^2$: with the positivity limiter off the code fails from
  negative pressure, and without the divergence projection it oscillates.
  The final time is not printed; 0.01 is inferred from a figure axis
  ([Ding & Wu (2024)](/sources/ding-2024.md), Example 4.4).
* *3D, three cases on $192^3$*: Felker and Stone's case at three times
  their field, the largest the scheme affords without an energy
  correction; the Balsara–Spicer case with the correction; and a
  relativistic case. Point symmetry is kept, and the fallback to lower
  order "played an essential role" ([Berta et al. (2024)](/sources/berta-2024.md), §5.7, Table 3).
* *3D, milder.* $B_0 = 10$ diagonal, pressure 100 inside $\varrho = 0.125$
  (printed swapped in eq. 47), $200^3$, $t = 0.02$, no positivity
  treatment mentioned ([Seo & Ryu (2023)](/sources/seo-2023.md), §3.7).
* *Relativistic*, $400^2$, the set-up above: stable "near-infinite
  shocks". The paper states both third and fourth order for this run
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.2).

**Later uses (batch 7).**
* *Two 3D blasts at second order* on $200^3$. At plasma beta $2\times10^{-2}$
  ($B_0 = 10$, $p = 100 \mid 1$, $\varrho = 0.125$, $t = 0.02$, printed in the right
  order) GLM, EGLM and CT are indistinguishable. At $2\times10^{-4}$
  ($B_0 = 100$, $p = 10^4 \mid 1$, $t = 2.5\times10^{-3}$) only EGLM runs; CT fails
  even with a minmod limiter ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.7).
* *A 3D "extreme" blast* on $257^3$: $|\mathbf B| = 150$ along the diagonal,
  $p = 1000 \mid 0.1$, plasma beta $1.117\times10^{-4}$, $t = 0.0075$, third-order
  ADER-WENO with a multidimensional Riemann solver and Balsara's
  self-adjusting positivity method; density and pressure stay positive
  ([Balsara (2017)](/sources/balsara-2017-d.md), §IX.4).

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§6.6–6.7.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§7.2–7.3.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §§7.4–7.5.
4. [Balsara (2004)](/sources/balsara-2004.md), §7.3.
5. [Balsara (2009b)](/sources/balsara-2009-b.md), §5.3 (author manuscript).
6. [Ding & Wu (2024)](/sources/ding-2024.md), Example 4.4 (arXiv v1).
7. [Berta et al. (2024)](/sources/berta-2024.md), §5.7 (arXiv v4).
8. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.7.
9. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.2.
10. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.7.
11. [Balsara (2017)](/sources/balsara-2017-d.md), §IX.4.
