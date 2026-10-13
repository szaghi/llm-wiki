---
type: Benchmark
title: "MHD rotor"
description: "A dense, rapidly spinning disc in a magnetized ambient medium launches torsional Alfvén waves; low-pressure regions make it a positivity test, especially in its very-low-β version."
status: established
aliases: [rotor problem, Balsara-Spicer rotor]
tags: [benchmark, mhd, 2d, positivity, low-beta]
timestamp: 2026-10-13T00:00:00Z
---

# MHD rotor

**Set-up** (Balsara and Spicer). On $[0,1]^2$ a disc of radius 0.1 with
density 10 rotates rigidly in a unit-density ambient. Density and
velocity taper linearly between radii 0.1 and 0.115 (Christlieb et al.,
the very-low-β version of Waagan, cited) or 0.13 (Balsara et al.)
([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4;
[Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2).

**Results.**
* PIF-WENO with CT on $400^2$ to $t = 0.27$ matches the reference; the
  positivity-preserving [flux limiter](/methods/positivity-preserving-flux-limiter.md)
  is required, otherwise the code fails
  ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4).
* Seventh-order divergence-preserving AFD-WENO on $256^2$ to $t = 0.29$
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2, Fig. 13).

**Later uses (batch 4).** Variants differ in taper and $\gamma$.
* Balsara et al.: $[-0.5, 0.5]^2$, $200^2$, $\mathbf B = (2.5, 0)$,
  $p = 1$, taper 0.1–0.13 (six zones, to be kept under refinement),
  $\gamma = 5/3$. Fourth-order ADER-WENO with a linearized solver to
  $t = 0.29$ agrees with Balsara and Spicer ([Balsara et al. (2009)](/sources/balsara-2009.md), §7.3).
* Dumbser et al. and Zanotti et al.: $[-0.6, 0.6]^2$, taper only
  0.1–0.105, $\gamma = 1.4$, GLM cleaning, $t = 0.25$. Third-order
  ADER-WENO with AMR (equivalent $960^2$) uses more than five times
  fewer elements. Thanks to the cleaning, it shows no spurious
  oscillations in density or magnetic pressure ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4, Table 6).
  ADER-DG with $K = 5$ and subcell limiting on AMR (equivalent $800^2$)
  matches the uniform grid ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.1).

**Later uses (batch 6).**
* *Second order.* Unit square, $200^2$, $B = 2.5$, $p = 1$, taper 0.1–0.13,
  $\gamma = 5/3$, $t = 0.29$, with divergence-free reconstruction and HLLE:
  consistent with Balsara and Spicer ([Balsara (2004)](/sources/balsara-2004.md), §7.2).
  The RK-WENO fourth-order sibling of the ADER run gives the same picture
  ([Balsara (2009b)](/sources/balsara-2009-b.md), §5.2).
* *Tóth's first rotor.* $[-0.5, 0.5]^2$, angular velocity 20, taper width
  0.015, $\gamma = 1.4$, $\mathbf B = 5/\sqrt{4\pi}\,\hat x$, $400^2$, with
  no positivity treatment: symmetric, no spurious oscillations, and the
  order of the CT makes no visible difference. The output time is 0.15 in
  the text and 0.125 in the caption ([Seo & Ryu (2023)](/sources/seo-2023.md), §3.6).
* *Another normalization.* $[0, 1]^2$, $B_x = 2.5/\sqrt{4\pi}$, $p = 0.5$,
  taper 0.1–0.115, $\gamma = 5/3$, $400^2$, $t = 0.295$. Without the
  divergence projection the fifth-order Mach number shows instability and
  nonphysical structure ([Ding & Wu (2024)](/sources/ding-2024.md), Example 4.3).
* *Relativistic.* With a maximum Lorentz factor of 10 or 30, the usual $400^2$ mesh
  has no zone within 10% of the nominal Lorentz factor. The fraction levels
  off only from $1200^2$ (Lorentz factor 10) and $3500^2$ (30), a
  resolution caveat for this benchmark. Runs on $2500^2$ and $4700^2$ at
  third order ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.1).

**Later uses (batch 7).**
* *GLM vs CT at second order* (Tóth's first rotor, $400^2$, $t = 0.15$):
  "extremely similar" Mach contours ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.6).
* *Entropy-stable GLM on block AMR* up to $512^2$: much smaller divergence
  artifacts than without cleaning, close to staggered CT; density and
  pressure minima that the CT run shows only at $2048^2$
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §5.3).
* *Fourth-order ADER-WENO on $1000^2$* with a multidimensional Riemann
  solver, taper kept at six zones; and a relativistic rotor with Lorentz
  factor 30, which needs at least $3500^2$ and was run at $4700^2$
  ([Balsara (2017)](/sources/balsara-2017-d.md), §§IX.3, IX.6).

**Later uses (batch 11).** The origin, [Balsara & Spicer (1999)](/sources/balsara-1999.md),
§3.1, prints in Gaussian units (field strength $B$ becomes
$B/\sqrt{4\pi}$ in Heaviside–Lorentz units): unit square, $400^2$; ambient
$\rho = 1$, $p = 1$, at rest; disc $\rho = 10$ inside $r = 0.1$, density and
rotation tapering linearly to the ambient at $r = 0.115$ (six zones); rotation
speed 2 at $r = 0.1$; $\gamma = 1.4$; $B_x = 5$; Courant number 0.8;
$t = 0.295$; boundary conditions not printed.
* *Erratum.* An "Update" (J. Comput. Phys. 153:671, 1999) states that the
  paper's Figs. 2–3 were run with $p = 0.5$, $\gamma = 5/3$, speed 1 at
  $r = 0.1$ and $B = 2.5$, densities and taper as printed; the printed set
  "also produce[s] an interesting rotor problem but at earlier times".
* *What this means for the batch-6 entries.* "Tóth's first rotor" above
  (angular velocity 20, i.e. speed 2 at $r = 0.1$; taper width 0.015;
  $\gamma = 1.4$; $5/\sqrt{4\pi}$) is the printed Balsara–Spicer set, and its
  earlier output time (0.15 or 0.125) is consistent with the erratum's remark.
  Ding & Wu's "another normalization" ($2.5/\sqrt{4\pi}$, $p = 0.5$, taper
  0.1–0.115, $\gamma = 5/3$, $400^2$, $t = 0.295$) is the erratum-corrected
  set, the one the origin's figures show. In every parameter this page
  lists, neither is a separate normalization. The runs "consistent with
  Balsara and Spicer" by Balsara (2004) and Balsara et al. (2009) use
  $p = 1$ and a 0.13 taper, so they are a variant of the corrected set;
  the agreement they report is with the figures' morphology.
* *Why the test exists.* Without CT or cleaning, the zone-centred Godunov
  scheme develops "magnetic monopoles" at the rotor edge, where the field
  lines are most sheared ($2h\,\nabla\cdot\mathbf B/|\mathbf B|$ between
  $-0.66$ and $0.66$ at $t = 0.317$), and a spurious solution; with a
  cleaning step it matches the CT result. This is the origin of the
  report cited by Dumbser et al. in batch 4. Balsara–Spicer CT and its
  pressure-switch variant give identical results at $t = 0.295$
  ([constrained transport](/methods/constrained-transport.md)).

**Later uses (batch 11, Balsara & Nkonga; merged at the 2026-10-13 deep
lint).** Fourth-order ADER–WENO with the multidimensional HLLI (MuSIC)
solver at the vertices, on $[-0.5, 0.5]^2$ with $1000^2$ cells, rotor
radius 0.1, $t = 0.29$; the states are not printed and the result is
shown qualitatively ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.3;
[multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).
It is the same resolution and order as the review's run in the batch-7
entry above.

**Later uses (batch 17).** *Tóth's two rotors*
([Tóth (2000)](/sources/toth-2000.md), §6.6, Table VIII, Figs. 19–20).
* *First rotor:* speed 2 at $r = 0.1$, taper to $r = 0.115$, $p = 1$,
  $B_x = 5/\sqrt{4\pi}$, $\gamma = 1.4$, $t = 0.15$, unsplit TVD-MUSCL
  with the MC limiter, $\nu \le 0.6$. This is the "Tóth's first rotor" of
  the batch-6 and batch-7 entries; the paper's domain is $[0, 1]^2$, so the
  $[-0.5, 0.5]^2$ listed there is Seo and Ryu's shift.
* *Second rotor*, "used to obtain the plots in BS": speed 1, $p = 0.5$,
  $B_x = 2.5/\sqrt{4\pi}$, $\gamma = 5/3$, taper 0.1–0.115, $t = 0.295$,
  one-step TVD with MC. "By mistake the final time and the plots in BS do
  not correspond to the initial condition described in the text (BS,
  private communication)." This agrees with the erratum reading of the
  batch-11 entry.
* *Errors.* Relative $L^1$ errors $\bar\delta_{50,100,200}$ fall at first
  order. First rotor: projection 0.1145/0.0603/0.0276 (best), eight-wave
  0.1152/0.0621/0.0285, flux-CT 0.1191/0.0624/0.0298, field-CT
  0.1537/0.0893/0.0488 (worst). Second rotor: projection
  0.1146/0.0625/0.0324 (best), field-CT 0.1404/0.0777/0.0453.
* *Pressure undershoots.* Many schemes undershoot in pressure, seen as
  spurious Mach-number peaks; an energy correction that holds the
  thermal energy fixed removes them, at a total-energy error below 0.4%,
  and was used for every second-rotor run.
* *The velocity distortion and $\nabla\cdot\mathbf B$ (a qualification of
  the batch-11 "Why the test exists").* The base scheme and field-CT
  distort the rotating velocity field in the centre, an error that "looks
  similar to the one shown by BS in Fig. 3 for their dimensionally split
  base scheme". Field-CT keeps its discrete divergence at round-off and
  shows "very distorted velocity contours", while the eight-wave scheme,
  with finite divergence errors, does not; so Balsara and Spicer's
  explanation of the error by the divergence is "not support[ed]" by these
  simulations (Fig. 20). The two papers ran different schemes: Balsara and
  Spicer's evidence is their own zone-centred scheme with and without
  cleaning, Tóth's a comparison across seven treatments in one code. Each
  claim stands on its own runs, so this is recorded as a qualification of
  the explanation, not as a contradiction.

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §7.3.
4. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
5. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.1.
6. [Balsara (2004)](/sources/balsara-2004.md), §7.2.
7. [Balsara (2009b)](/sources/balsara-2009-b.md), §5.2 (author manuscript).
8. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.6.
9. [Ding & Wu (2024)](/sources/ding-2024.md), Example 4.3 (arXiv v1).
10. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.1.
11. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.6.
12. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.3.
13. [Balsara (2017)](/sources/balsara-2017-d.md), §§IX.3, IX.6.
14. [Balsara & Spicer (1999)](/sources/balsara-1999.md), §3.1 and the erratum (J. Comput. Phys. 153:671).
15. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.3.
16. [Tóth (2000)](/sources/toth-2000.md), §6.6, Table VIII, Figs. 19–20.
