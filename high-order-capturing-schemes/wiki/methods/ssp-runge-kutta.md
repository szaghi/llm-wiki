---
type: Method
title: "TVD / strong-stability-preserving Runge–Kutta methods"
description: "Explicit Runge–Kutta methods written as convex combinations of forward-Euler steps, so any norm or convex-functional stability of forward Euler (TVD, maximum norm, positivity, entropy) carries over under a scaled time step."
status: established
aliases: [TVD Runge-Kutta, SSP Runge-Kutta, Shu-Osher Runge-Kutta, SSP-RK3]
tags: [time-discretization, ssp, tvd, method-of-lines]
timestamp: 2026-10-09T00:00:00Z
---

# TVD / strong-stability-preserving Runge–Kutta methods

**The idea** ([Shu & Osher (1988)](/sources/shu-1988.md), §II). Suppose
the forward-Euler step $u + \Delta t\,\mathcal{L}(u)$ is TVD (or TVB)
for $\Delta t \le \Delta t_{\mathrm{FE}}$. Write an explicit RK method in
the Shu–Osher form
$$u^{(i)} = \sum_{k=0}^{i-1}\left(a_{ik}\,u^{(k)} + b_{ik}\,\Delta t\,\mathcal{L}(u^{(k)})\right),\qquad a_{ik} \ge 0,\ \ \sum_k a_{ik} = 1 .$$
If also $b_{ik} \ge 0$, every stage is a convex combination of forward
Euler steps with step $(b_{ik}/a_{ik})\Delta t$, hence TVD for
$\Delta t \le \mathcal{C}\,\Delta t_{\mathrm{FE}}$ with
$\mathcal{C} = \min a_{ik}/b_{ik}$. Where some $b_{ik} < 0$, the
operator is replaced by the downwind operator $\tilde{\mathcal{L}}$
(Proposition 2.1). The total variation may be replaced by any convex
functional (Remark 2.1): the methods preserve maximum-norm stability,
entropy inequalities, and so on ([Shu (1998)](/sources/shu-1998.md),
§4.2.1).

**Optimal low-order methods** ([Shu & Osher (1988)](/sources/shu-1988.md),
eqs. 2.15–2.19; [Shu (1998)](/sources/shu-1998.md), eqs. 4.10–4.11):
* second order (Heun), $\mathcal{C} = 1$:
  $u^{(1)} = u^n + \Delta t\,\mathcal{L}(u^n)$,
  $u^{n+1} = u^n + \tfrac12\Delta t\,\mathcal{L}(u^n) + \tfrac12\Delta t\,\mathcal{L}(u^{(1)})$;
* third order, $\mathcal{C} = 1$:
$$\begin{aligned}
u^{(1)} &= u^n + \Delta t\,\mathcal{L}(u^n),\\
u^{(2)} &= \tfrac34 u^n + \tfrac14 u^{(1)} + \tfrac14\Delta t\,\mathcal{L}(u^{(1)}),\\
u^{n+1} &= \tfrac13 u^n + \tfrac23 u^{(2)} + \tfrac23\Delta t\,\mathcal{L}(u^{(2)}).
\end{aligned}$$
  Each stage needs only the previous stage's $\mathcal{L}$, which lowers
  storage. Classical third-order methods rewritten in this form have
  negative $b_{ik}$ and smaller $\mathcal{C}$.

**Fourth order and above.** No four-stage, fourth-order method with
nonnegative coefficients exists (proved by Gottlieb and Shu, cited in
[Shu (1998)](/sources/shu-1998.md)). Their preferred four-stage
fourth-order method uses $\tilde{\mathcal{L}}$, has $\mathcal{C} = 0.936$,
and costs two operator evaluations at one stage, an effective
$\mathcal{C}$ of $0.624$. A fifth-order method with $\tilde{\mathcal{L}}$
is given by [Shu & Osher (1988)](/sources/shu-1988.md). Third-order
low-storage methods (two registers) reach $\mathcal{C} \approx 0.32$.
TVD multistep methods exist to third order with $\mathcal{C} = 0.5$
per evaluation; none of fourth order without negative coefficients was
found ([Shu (1998)](/sources/shu-1998.md), §4.2.2).

**Why nonlinear stability matters.** Linear stability of the ODE solver
does not suffice for discontinuous solutions, and does not apply to
adaptive-stencil schemes at all ([Shu & Osher (1988)](/sources/shu-1988.md)).
A second-order MUSCL scheme that is TVD under forward Euler produces an
overshoot at a shock when integrated with a linearly stable but non-TVD
second-order RK method, and larger oscillations in the intermediate
stages; the TVD method does not ([Shu (1998)](/sources/shu-1998.md),
Fig. 4.1).

## Use in this corpus

* ENO and WENO in the method-of-lines form use the third-order method
  ([Shu & Osher (1989)](/sources/shu-1989.md);
  [Liu, Osher & Chan (1994)](/sources/liu-1994.md), which also prints a
  fourth-order variant; [Jiang & Shu (1996)](/sources/jiang-1996.md),
  "RK-3", together with the classical non-TVD fourth-order "RK-4" and
  $\Delta t \propto h^{5/4}$ in accuracy tests so that RK-4 acts
  as fifth order).
* [Harten et al. (1987)](/sources/harten-1987.md) (Remark C2) found the
  semi-discrete ENO with Runge–Kutta time stepping non-oscillatory for
  CFL up to 0.5, with oscillations beyond, and less efficient than their
  fully discrete Cauchy–Kowalewski scheme.
* [Suresh & Huynh (1997)](/sources/suresh-1997.md) design the MP5
  constraint for the stage structure: since each RK3 stage is a
  forward-Euler step and the next stage a positive combination,
  monotonicity of one stage implies monotonicity of the full step
  ([monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).
* [Balsara & Shu (2000)](/sources/balsara-2000.md): WENO of $r = 3$ to
  $7$ with RK3 is linearly stable for CFL between 1.43 and 0.99, but
  non-oscillatory shock capturing needs much smaller CFL ($r = 5$ WENO:
  clean at 0.2, slightly oscillatory at 0.4); convergence tests use
  $\Delta t \propto h^{(2r-1)/3}$.
* The alternative is the Lax–Wendroff (Taylor) time discretization,
  compact and fully one-step, but algebraically heavy in multi-D and
  hard to analyze ([Shu (1998)](/sources/shu-1998.md), §4.2.3).
  [Levy, Puppo & Russo (1999)](/sources/levy-1999.md) use Runge–Kutta
  with natural continuous extensions to supply the time quadrature of
  a staggered central scheme ([central WENO](/methods/central-weno.md)).

**Later uses (batch 2).** RK3 is the default time stepping of every
batch-2 scheme; to measure spatial order, time steps are shrunk
($\Delta t \propto h^{5/3}$ in [Henrick et al. (2005)](/sources/henrick-2005.md);
reduced, grid-dependent steps also in [Borges et al. (2008)](/sources/borges-2008.md)
and [Castro et al. (2011)](/sources/castro-2011.md), whose exact scalings
are not legible in the copies read). Seventh-order tests use
an $m$-stage linear SSP method for linear problems and the five-stage
fourth-order SSP(5,4) for nonlinear ones ([Rathan & Naga Raju (2017)](/sources/rathan-2017.md));
WENO-AO cites the Spiteri–Ruuth SSP methods ([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md));
[Pirozzoli (2002)](/sources/pirozzoli-2002.md) uses non-TVD RK4 and a
von Neumann analysis of the full discretization.

**Later uses (batch 3).**
* *Terminology and theory.* Gottlieb, Shu and Tadmor rename "TVD time
  discretization" to *strong stability preserving*: the argument uses
  only convexity, so any norm or convex functional is preserved, and a
  weakened forward-Euler bound $\Vert u + \Delta t\mathcal{L}u\Vert \le (1 + O(\Delta t))\Vert u\Vert$
  (TVB) carries over too. They give optimal linear methods of every
  order with $\mathcal{C} = 1$, multistep methods, and the barriers
  collected in [SSP order barriers](/results/ssp-order-barriers.md)
  ([Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md)).
  Their Fig. 2.1 reproduces Gottlieb and Shu's Burgers example: a
  TVD MUSCL scheme overshoots at the shock with a non-SSP second-order
  Runge–Kutta method and not with the SSP one.
* *Positivity.* Because an SSP step is a convex combination of
  forward-Euler steps, it keeps a convex admissible set, and the
  positivity limiters are applied at every stage
  ([positivity preservation](/properties/positivity-preserving.md)).
  The stage wave speeds needed for the CFL bound are unknown at
  $t^n$; a safety factor of 2–3 works in practice, and SSP multistep
  methods avoid the issue ([Zhang & Shu (2010)](/sources/zhang-2010.md), Remark 2.7).
* *Stability limits in multi-D.* With RK3, FV-WENO is stated stable for
  Courant numbers up to 1 in 1D and 1/2 in 2D — the limits of the
  unsplit Godunov scheme — and, from numerical experiments, 1/3 in 3D.
  Accuracy tests are run at a fixed Courant number (0.45 in 2D, 0.27 in
  3D) rather than with $\Delta t \propto h^{5/3}$, which for $r = 4$
  becomes $\Delta t \propto h^{7/3}$, stricter than a parabolic limit
  ([Titarev & Toro (2004)](/sources/titarev-2004.md), §§2, 5). The 1D
  value is below the linear-stability CFL of 1.43 reported for $r = 3$
  by [Balsara & Shu (2000)](/sources/balsara-2000.md); Titarev and Toro
  call theirs the "optimal" condition without derivation, so it is read
  here as a working bound, not a competing stability limit.
* *Accuracy tests at high order* use SSP-RK3 for third order and the
  five-stage fourth-order SSP method of Spiteri–Ruuth for orders 5–9,
  with $\Delta t$ scaled by $(1/2)^{5/4}$ or $(1/2)^{7/4}$ per mesh doubling
  ([Balsara et al. (2025)](/sources/balsara-2025.md), §VI;
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §6). GP-WENO
  uses a fourth-order TVD Runge–Kutta method
  ([Reyes et al. (2018)](/sources/reyes-2018.md), §5). IMEX Runge–Kutta
  is recommended for stiff relaxation sources
  ([Balsara et al. (2025)](/sources/balsara-2025.md), §V).
* *The single-step alternative* for AMR and storage:
  [Lax–Wendroff (Taylor) time discretization](/methods/taylor-time-discretization.md)
  ([Christlieb et al. (2016)](/sources/christlieb-2016.md)).

**Later uses (batch 4).**
* *Linear stability limits.* For the linear upwind-biased schemes of
  orders 3, 5, 7, 9, 11 and 13 with SSP-RK3, the largest stable Courant
  numbers are 1.62, 1.43, 1.24, 1.12, 1.04 and 0.99 ([Li, Shu & Zhang (2016)](/sources/li-2016.md), Table 3.1).
  The values for orders 5 to 13 agree with Balsara and Shu's range,
  1.43 to 0.99 for $r = 3$–$7$.
* *Boundary data inside stages.* Imposing $g(t^n + \Delta t)$ and
  $g(t^n + \Delta t/2)$ in the two inner RK3 stages reduces accuracy to
  second order. The stages must instead receive $g + \Delta t\,g'$ and
  $g + \tfrac12\Delta t\,g' + \tfrac14\Delta t^2 g''$ at $t^n$
  (Carpenter et al.; [Li, Shu & Zhang (2016)](/sources/li-2016.md), §2.2; [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.1;
  [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)).
* *RKDG* uses SSP-RK3 with the limiter after each stage ([Qiu & Shu (2005)](/sources/qiu-2005.md), §1).
  The barriers are also the argument for one-step [ADER](/methods/ader.md):
  explicit RK needs more stages than order beyond four, and in practice
  RKDG stops at third order ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.1; [Zanotti et al. (2015)](/sources/zanotti-2015.md), §1). On AMR grids,
  intermediate stages need consistent ghost data on every level, which
  a one-step method avoids ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §1).

**Later uses (batch 5).**
* *Classical RK4, not SSP.* Fifth-order FD-WENO for MHD uses it in every
  test, with $\Delta t \sim h^{5/4}$ in accuracy runs
  ([Jiang & Wu (1999)](/sources/jiang-1999.md), §§2.2, 3.2). Fourth-order
  finite volume uses it with a linear stability limit of 1.3925 for the
  sum of directional Courant numbers, from RK4 with first-order upwinding
  ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), eq. 57;
  [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §3.1;
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md)).
* *Dense output for AMR subcycling.* Coarse-step stages give a cubic
  (RK4) or quadratic (SSP-RK3) interpolant in time. Fine-level ghost
  values must match the fine intermediate stages, not just the stage
  times, or limiters fire on smooth data
  ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §3.1;
  [Wang et al. (2025)](/sources/wang-2025.md), §4.2.3;
  [high-order AMR](/methods/high-order-amr.md)).
* *Conservation through the stages.* Exact boundary conservation is
  imposed only on the RK-averaged flux of the last stage,
  $\tfrac16(\hat f^n + \hat f^{(1)} + 4\hat f^{(2)})$ for SSP-RK3
  ([Ding, Shu & Zhang (2020)](/sources/ding-2020.md), eq. 2.10). Refluxing
  accumulates the stage fluxes with the Butcher weights
  ([Wang et al. (2025)](/sources/wang-2025.md), §4.3).
* *Moving boundaries and interfaces.* SSP-RK3 stage data at a moving
  boundary are taken with the boundary frozen at $t^n$
  ([Liu et al. (2023)](/sources/liu-2023.md), §2;
  [Liu et al. (2022)](/sources/liu-2022.md), eq. 29). A fluid FD solver
  and a DG solid solver share one SSP-RK3, so they exchange data at every
  stage ([Liu et al. (2025)](/sources/liu-2025.md), §3.1).

**Later uses (batch 6).**
* *Many stages, large steps.* Ketcheson's 10-stage, fourth-order,
  low-storage SSP-RK(10,4) keeps FD-WENO5 essentially non-oscillatory up to
  CFL 3.07 (Gottlieb et al., cited). It runs at CFL 3.0 and beats non-SSP
  RK4 at CFL 0.8. The many stages enlarge ghost regions under AMR
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3).
* *SSP(5,4).* Its SSP coefficient, $1.50818004975927$, is used directly
  as the CFL number for WENO5 MHD, about 50% cheaper than RK4 at CFL 0.8
  with identical results ([Seo & Ryu (2023)](/sources/seo-2023.md), §§2.3, 3.5).
  Equating the SSP coefficient with the admissible CFL assumes forward
  Euler is stable at CFL 1, which the paper does not show. A five-stage
  fourth-order variant with all coefficients printed drives fourth-order
  finite volume ([Berta et al. (2024)](/sources/berta-2024.md), §3.3, eq. 31).
* *Von Neumann limits* for mimetic edge schemes: 0.7071, 1.1507 and 1.3040
  for orders 2, 3 and 4 with SSP-RK2, SSP-RK3 and SSP-RK(5,4). SSP-RK3's
  own dissipation keeps third-order damping at the level of second order
  ([Balsara et al. (2023)](/sources/balsara-2023.md), §4).
* *Not SSP.* The low-storage RK3 of Spalart, Moser and Rogers (one
  negative coefficient) in a production hybrid WENO DNS code
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.2;
  [STREAmS](/software/streams.md)). A second-order scheme labelled "TVD
  Runge–Kutta … simply the Heun scheme" but printed as the explicit
  midpoint rule, which is not SSP ([Balsara (2004)](/sources/balsara-2004.md),
  eq. 2.5; recorded as printed).
* *Forward Euler and RK2 are linearly unstable with WENO5* and "should
  not be used even if the problem is steady state and no time accuracy is
  needed" (Wang and Spiteri, as cited by [Shu (2009)](/sources/shu-2009.md), §3.1).
* *Stage accuracy with RK3.* To show fourth-order spatial accuracy with
  SSP-RK3, the step must shrink faster than the mesh
  ([Balsara (2009b)](/sources/balsara-2009-b.md), §3.3).

**Later uses (batch 7).**
* The five-stage fourth-order SSP scheme at CFL 1.5 in 1D, printed with
  15-digit coefficients (first stage $0.391752226571890\,\Delta t$); the
  permitted CFL divides by the dimension; boundary values are needed at
  every stage ([Balsara (2017)](/sources/balsara-2017-d.md), §IV.1, eq. 38).
* *Restart on failure with positivity limiting* ([Zhang (2017)](/sources/zhang-2017.md), §5.3).
  SSP-RK3 with the limiter before every stage; the trial step is
  $\min\{a\,h/\alpha^*,\ b\,\mathrm{Re}\,h^2\}$ from the convective speed only,
  since the viscous penalty grows at shocks; a stage average outside the
  admissible set halves the step and restarts it. A bound checked at the
  first stage does not guarantee the second, because the stage speeds are
  unknown in advance.

# Citations

1. [Shu & Osher (1988)](/sources/shu-1988.md), §II (eqs. 2.12–2.19 read from the page images).
2. [Shu (1998)](/sources/shu-1998.md), §4.2.
3. [Harten et al. (1987)](/sources/harten-1987.md), Remark C2.
4. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §2.
5. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§1, 6.
6. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §§1–2.
7. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§I, IV.
8. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), §2.1.
9. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §5.3.
10. [Borges et al. (2008)](/sources/borges-2008.md), §5.
11. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §5.
12. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §4.
13. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §3.
14. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §2.3.
15. [Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §§1–7.
16. [Titarev & Toro (2004)](/sources/titarev-2004.md), §§2, 5.
17. [Zhang & Shu (2010)](/sources/zhang-2010.md), Remarks 2.2, 2.7.
18. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §§V–VI.
19. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §6.
20. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.
21. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §1.
22. [Li, Shu & Zhang (2016)](/sources/li-2016.md), §§2.2, 3.2 (Table 3.1 read from the page image).
23. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.1.
24. [Qiu & Shu (2005)](/sources/qiu-2005.md), §1.
25. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.1.
26. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §1.
27. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §1.
28. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§2.2, 3.2.
29. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§2.1, 3.1, eq. 57.
30. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §3.1 (accepted manuscript).
31. [Wang et al. (2025)](/sources/wang-2025.md), §§4.2.3, 4.3 (arXiv preprint).
32. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), §2.1.
33. [Liu et al. (2023)](/sources/liu-2023.md), §2.
34. [Liu et al. (2022)](/sources/liu-2022.md), §§2.2, 3.1.3.
35. [Liu et al. (2025)](/sources/liu-2025.md), §3.1.
36. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3 (arXiv v2).
37. [Seo & Ryu (2023)](/sources/seo-2023.md), §§2.3, 3.5.
38. [Berta et al. (2024)](/sources/berta-2024.md), §3.3 (arXiv v4).
39. [Balsara et al. (2023)](/sources/balsara-2023.md), §4.
40. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.2.
41. [Balsara (2004)](/sources/balsara-2004.md), §2.
42. [Balsara (2009b)](/sources/balsara-2009-b.md), §3.3 (author manuscript).
43. [Shu (2009)](/sources/shu-2009.md), §3.1.
44. [Balsara (2017)](/sources/balsara-2017-d.md), §IV.1.
45. [Zhang (2017)](/sources/zhang-2017.md), §5.3.
