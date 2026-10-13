---
type: Benchmark
title: "MHD blast wave in a low-β medium"
description: "An over-pressured region expanding into a strongly magnetized, low-pressure background; strong anisotropic shocks against tiny thermal pressure make it the standard positivity stress test for MHD, also run in relativistic MHD."
status: established
aliases: [magnetized blast wave, MHD blast problem, RMHD blast wave]
tags: [benchmark, mhd, positivity, low-beta, 2d, 3d]
timestamp: 2026-10-13T00:00:00Z
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

**Later uses (batch 11).** The origin, [Balsara & Spicer (1999)](/sources/balsara-1999.md),
§3.2, Fig. 4, is 2D only. In Gaussian units: unit square (position not
stated), $200^2$; $\rho = 1$; $p = 1000$ inside radius 0.1 and 0.1 outside;
$\gamma = 1.4$; at rest; $B = 100$ along $x$ (ambient plasma beta
$2.51\times10^{-4}$); $t = 0.01$, given only in the figure caption. It is
called a "more stringent variant" of Balsara's earlier blast.
* *Corrections of attribution.* The batch-4 line places the origin's blast
  on $[-0.5, 0.5]^2$; that is the coordinate choice of Balsara et al.
  (2009), not of the origin. Its "stricter 3D version on $151^3$" belongs
  to Balsara et al. (2009) alone: the 1999 paper has no 3D run. Ding &
  Wu's field-along-$x$ case (batch 6) is the origin set-up in
  Heaviside–Lorentz units ($100/\sqrt{4\pi}$). The oblique lead set-up
  ($B_x = B_y = 100/\sqrt{8\pi}$) is a later variant with the same field
  magnitude, rotated by 45°.
* *Findings.* Balsara–Spicer CT and the zone-centred Godunov scheme with
  cleaning are "extraordinarily similar", and even the zone-centred scheme
  without cleaning is "very similar": fast strong shocks do not expose
  divergence errors, unlike the [rotor](/benchmarks/mhd-rotor.md). The
  pressure-switch variant gives the same result; forcing its weight to one
  direction everywhere degrades shock propagation only slightly in the
  other direction. Whether the energy correction was used is not stated
  ([constrained transport](/methods/constrained-transport.md)).

**Later uses (batch 11, Balsara & Nkonga; merged at the 2026-10-13 deep
lint).** *The 3D "extreme" blast again* (§5.4): $\gamma = 1.4$,
$\rho = 1$, $p = 0.1$ with $p = 1000$ inside radius 0.1,
$B_x = B_y = B_z = 150/\sqrt3$, unit cube, $257^3$ cells, plasma beta
$1.117\times10^{-4}$, CFL 0.4, $t = 0.0075$, third-order ADER–WENO with
the multidimensional HLLI (MuSIC) solver. Density and pressure stay
"positive as expected"; which positivity safeguards were active is not
stated ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.4;
[multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).
The set-up is that of the review's run in the batch-7 entry above.

**Later uses (batch 18).** *The 1998 blasts and the 2012 3D blast.*
* *Balsara's 1998 blasts* ([Balsara (1998)](/sources/balsara-1998-b.md),
  §6.2.2, Figs. 9–11). Unit square, $200^2$, uniform $B_x = 10$ G,
  second-order TVD. Adiabatic: $\rho = 1$, $p = 1000$ inside radius 0.05
  and 1 outside, $\gamma = 1.4$, $t = 0.02$, Strang-split with the spectral
  projection; ambient plasma beta about 0.25 (reader's arithmetic,
  $8\pi p/B^2$); more symmetric than the isothermal case, and splitting
  "does not seem to have affected the quality". Isothermal: $\rho = 100$
  inside radius 0.05 and 1 outside, isothermal sound speed 1, $t = 0.09$;
  without cleaning (and split) the magnetic pressure shows "a great deal of
  small-scale fluctuations especially in the center", unlike the unsplit
  cleaned run. By its parameters the adiabatic case is very likely the
  "earlier blast" of which the batch-11 origin is a "more stringent
  variant": the 1999 set-up raises the field to 100, the radius to 0.1 and
  lowers the ambient pressure to 0.1 (reader's identification; the
  batch-11 record does not name the reference). The adiabatic run is
  cleaned, so it is no test of divergence errors; Balsara's evidence that
  cleaning matters is the isothermal case, which changes splitting and
  cleaning together, and so does not conflict with the batch-11 finding
  that the uncleaned zone-centred scheme is "very similar" on the strong
  adiabatic blast.
* *The 2012 3D blast* ([Balsara (2012)](/sources/balsara-2012.md), §3.3,
  Figs. 5–6). $\gamma = 1.4$, $\rho = 1$, $p = 0.1$ and 1000 inside radius
  0.1 (centre not stated), $B_x = B_y = B_z = 50/\sqrt3$ (Gaussian,
  $\vert\mathbf B\vert = 50$), plasma beta $1.005\times10^{-3}$, unit cube,
  $129^3$, CFL 0.3, $t = 0.012$; third-order ADER-WENO with a linearized
  solver and the [self-adjusting positivity limiter](/methods/self-adjusting-positivity-limiter.md),
  also run at second and fourth order. Mid-plane ranges:
  $\rho \in [0.115, 2.53]$, $p \in [0.0135, 88.3]$,
  $\vert\mathbf v\vert \le 8.94$, $\vert\mathbf B\vert \in [13.7, 64.1]$.
  With floors only ($p \ge 10^{-8}$) the pressure reaches the floor and is
  "totally corrupted… scientifically unusable", with peak
  $\vert\mathbf v\vert$ 9.6 and $\vert\mathbf B\vert$ 67.2. Called the 3D
  variant of Balsara and Spicer's 2D blast; it is milder than the batch-7
  "extreme" blast ($\vert\mathbf B\vert = 150$, beta $1.117\times10^{-4}$,
  $257^3$), which uses the same method.

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
12. [Balsara & Spicer (1999)](/sources/balsara-1999.md), §3.2.
13. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.4.
14. [Balsara (1998)](/sources/balsara-1998-b.md), §6.2.2, Figs. 9–11.
15. [Balsara (2012)](/sources/balsara-2012.md), §3.3, Figs. 5–6.
