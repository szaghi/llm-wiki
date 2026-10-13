---
type: Method
title: "Strong-stability-preserving (TVD) Runge–Kutta methods"
description: "Explicit Runge–Kutta methods written as convex combinations of forward-Euler steps, so that any convex stability property of the Euler step (total variation, positivity) carries over under a reduced CFL number; the time integrator of most high-order MHD sources of this bundle, and the stage structure that AMR ghost refresh and refluxing must follow."
status: established
aliases: [SSP-RK, TVD Runge–Kutta, SSP-RK3, Shu–Osher Runge–Kutta, SSPRK]
tags: [time-integration, tvd, stability, high-order, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Strong-stability-preserving (TVD) Runge–Kutta methods

A family of explicit Runge–Kutta methods introduced by
[Shu & Osher (1988)](/sources/shu-osher-1988.md) as "TVD Runge–Kutta"
time discretizations for method-of-lines shock-capturing schemes. The
later name, strong-stability-preserving (SSP), describes the property the
paper already states for any convex functional (Remark 2.1). The method
has no divergence content of its own; it enters this bundle as the time
integrator of its high-order MHD sources and through its stage structure.

## Definition

Write the semi-discrete scheme for the conserved state $U$ as an ODE
system driven by a spatial operator, and assume that one forward-Euler
step of that operator, $U$ plus $\Delta t$ times the operator applied to
$U$, is total-variation diminishing (or bounded) for CFL numbers up to a
forward-Euler limit.

**Convex (Shu–Osher) form** (eq. 2.12). Each stage is a sum over the
earlier stages of a convex weight times the earlier stage plus a step
weight times $\Delta t$ times the operator applied to that stage. The
convex weights are non-negative and sum to one per stage. Written this
way, each stage is a convex combination of forward-Euler steps of length
(step weight / convex weight) $\Delta t$.

**Proposition 2.1** ([Shu & Osher (1988)](/sources/shu-osher-1988.md),
eq. 2.13). The Runge–Kutta scheme is TVD for CFL numbers up to the
forward-Euler limit times the **CFL coefficient**, the smallest ratio of
a convex weight to the modulus of its step weight, provided that wherever
a step weight is negative the operator is replaced by a downwinded
operator that is TVD for the backward-in-time problem (eqs. 2.7–2.9).
Remark 2.1 replaces total variation by any convex functional, which is
the general strong-stability statement.

## The schemes

* **Second order** (eq. 2.15): a forward-Euler step, then the average of
  $U^n$ and a forward-Euler step from the first stage. CFL coefficient 1;
  optimal among two-stage second-order schemes; it is Heun's method
  (eq. 2.16).
* **Third order, SSP-RK3** (eq. 2.18): the first stage is a forward-Euler
  step from $U^n$; the second is $\frac34 U^n$ plus $\frac14$ of a
  forward-Euler step from the first stage; $U^{n+1}$ is $\frac13 U^n$
  plus $\frac23$ of a forward-Euler step from the second stage. CFL
  coefficient 1, no downwinded operator, and each stage needs only the
  operator at the previous stage, which saves storage. Found by
  "extensive searching"; its Butcher weights are $\frac16, \frac16,
  \frac23$ (eq. 2.19). The coefficients agree with
  [Jiang & Shu (1996)](/sources/jiang-shu-1996.md) (eqs. 1.2–1.3) and
  with Table I of [Shu & Osher (1989)](/sources/shu-osher-1989.md).
* **Fourth order with four stages** (eqs. 2.20–2.22). "Extensive
  searching seems to indicate" that negative step weights cannot be
  avoided (stated, not proved). Classical RK4 in convex form has CFL
  coefficient $\frac23$ and needs the downwinded operator at the first
  two stages; re-weightings reach $\frac{137}{200}$ (eq. 2.21) and 0.87
  (eq. 2.22). So classical RK4 is TVD only with the downwinded operator;
  used with the plain operator, as [Jiang & Shu (1996)](/sources/jiang-shu-1996.md)
  use it, it is not TVD ([WENO reconstruction](/methods/weno.md)).
* **Fifth order** (eq. 2.23): Lambert's method in convex form, CFL
  coefficient $\frac{7}{30}$, downwinded operator at three stages; Table I
  of the 1989 paper lists it with six stages.

The five-stage fourth-order SSP schemes and the many-stage low-storage
ones used by later sources of this bundle (below) are not in Shu &
Osher; their primary sources are not ingested here.

**Two CFL quantities, not to be conflated.** The CFL coefficient above is
a TVD (strong-stability) bound relative to the forward-Euler limit. Linear
(von Neumann) stability limits of a specific spatial operator are a
different quantity: 1.434 with SSP-RK3 and 1.731 with classical RK4 for
three-point-stencil WENO ([Jiang & Shu (1996)](/sources/jiang-shu-1996.md),
Table 5); 1.1507 at third order with SSP-RK3 and 1.3040 at fourth order
with SSP-RK(5,4) for the scheme of
[Balsara et al. (2023)](/sources/balsara-2023.md) (§4).

## Multidimensional time step

Applied dimension by dimension, the CFL number is "shrunk by a factor
$(d)^{-1}$" in $d$ dimensions
([Shu & Osher (1988)](/sources/shu-osher-1988.md), p. 22); the 1989 paper
writes the condition as $\Delta t$ times the maximum over states of the
sum over directions of $|\lambda_k|/h$ in each direction, bounded by the
forward-Euler limit ([Shu & Osher (1989)](/sources/shu-osher-1989.md),
p. 42). The 1988 rotated-square advection test was stable at half the 1D
CFL number and blew up ("instability-overflow") at the 1D value (§IV
Ex. 3).

## Positivity by convexity

Remark 2.1 covers any convex functional. Admissibility (positive density
and pressure, the set $\mathcal G$) is a convex constraint, and sources of
this bundle carry forward-Euler positivity to the full scheme on that
ground: [Ding & Wu (2024)](/sources/ding-2024.md) ("SSP-RK3 inherits this
by convexity", §3) and [Wu & Shu (2018)](/sources/wu-shu-2018.md), with
SSP time stepping
([positivity–divergence coupling](/results/positivity-divergence-coupling.md)).
Shu & Osher state the convex-functional generalisation, not positivity.

## Stage structure, AMR and the divergence invariant

Every SSP stage is a linear combination of forward-Euler updates.
*Compiler reading:* a linear invariant that each forward-Euler update
preserves, such as $D_h B_h = 0$ under a CT update, is therefore preserved
by every stage and by the step, whatever the weights; convexity is needed
for the TVD and positivity statements, not for this one. It holds only if
every stage is a complete update of the scheme, including ghost data:

* [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md) apply their
  EMF update at each stage of a "multi-stage (Shu–Osher)" scheme (p. 276).
* At a seam between independently stepped blocks the invariant holds
  exactly only if seam ghosts are refreshed at every Runge–Kutta stage
  ([exact discrete divergence](/properties/exact-discrete-divergence.md);
  [Zaghi (2026)](/sources/zaghi-2026.md), hypothesis); ADAM refreshes
  ghosts at every stage ([Zaghi et al. (2023)](/sources/zaghi-2023.md),
  §3.1.1).
* Conservation at coarse–fine interfaces needs flux registers that hold
  the stage-weighted combination of fluxes, applied at the end of the step
  ([refluxing](/methods/refluxing.md);
  [Couch et al. (2021)](/sources/couch-2021.md)); ALPACA corrects at the
  last stage ([Hoppe et al. (2022)](/sources/hoppe-2022.md)).
* Many-stage schemes enlarge AMR ghost regions and inter-patch traffic
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md)),
  and multistage methods need intermediate-stage ghost values that
  time-interpolated ghosts cannot supply to high order, which is why
  [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md)
  choose a single-stage, single-step integrator.

## Uses in this bundle

* **SSP-RK3:** FD-WENO in ADAM's compressible Navier–Stokes application
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md); [ADAM](/software/adam.md)); PLUTO's high-order GLM schemes
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md));
  third-order SSP-RK at fourth spatial order, with the Courant number cut
  by 0.396 per mesh doubling ([Balsara (2009)](/sources/balsara-2009.md));
  [Ding & Wu (2024)](/sources/ding-2024.md);
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md).
* **Second-order SSP:** SSPRK(2,2) in the resistive CT solver of
  [Jones et al. (2026)](/sources/jones-2026.md); second- or third-order
  SSP-RK in Flash-X's Spark ([Couch et al. (2021)](/sources/couch-2021.md)).
  *Compiler reading:* the optimal two-stage second-order SSP scheme is
  eq. 2.15 of Shu & Osher; the sources do not print their coefficients.
* **Five-stage fourth order:** HOW-MHD at CFL about 1.5
  ([Seo & Ryu (2023)](/sources/seo-2023.md)); the fourth-order UCT scheme
  of [Felker & Stone (2018)](/sources/felker-2018.md); eSSPRK(5,4) in
  [Berta et al. (2024)](/sources/berta-2024.md); with a shrinking time step
  in [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md).
* **Low-storage 10-stage SSP-RK4** at CFL 3.0 for the vector-potential
  scheme ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md);
  [vector-potential evolution](/methods/vector-potential-evolution.md)).
* **Athena++** replaces CTU by SSP and low-storage RK integrators, unsplit
  at every substep to keep the constraint
  ([Stone et al. (2020)](/sources/stone-2020.md)); Runge–Kutta stepping
  avoids the CTU interface-state source terms
  ([Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §6.1).

# Citations

1. [Shu & Osher (1988)](/sources/shu-osher-1988.md), §II (eqs. 2.1–2.23, Proposition 2.1, Remark 2.1), §III p. 22, §IV Ex. 3.
2. [Shu & Osher (1989)](/sources/shu-osher-1989.md), §I (eqs. 1.6–1.7, Table I), p. 42.
3. [Jiang & Shu (1996)](/sources/jiang-shu-1996.md), §1 (eqs. 1.2–1.4), Table 5.
4. [Balsara et al. (2023)](/sources/balsara-2023.md), §4.
5. [Ding & Wu (2024)](/sources/ding-2024.md), §3.
6. [Wu & Shu (2018)](/sources/wu-shu-2018.md).
7. [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md), p. 276.
8. [Zaghi (2026)](/sources/zaghi-2026.md).
9. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1.
10. [Couch et al. (2021)](/sources/couch-2021.md).
11. [Hoppe et al. (2022)](/sources/hoppe-2022.md).
12. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3.
13. [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md).
14. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md).
15. [Balsara (2009)](/sources/balsara-2009.md), §4.
16. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§6–7.
17. [Jones et al. (2026)](/sources/jones-2026.md).
18. [Seo & Ryu (2023)](/sources/seo-2023.md).
19. [Felker & Stone (2018)](/sources/felker-2018.md).
20. [Berta et al. (2024)](/sources/berta-2024.md).
21. [Stone et al. (2020)](/sources/stone-2020.md).
22. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §6.1.
