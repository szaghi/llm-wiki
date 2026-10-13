---
type: Benchmark
title: "Double-rarefaction (near-vacuum) Riemann problems"
description: "Two rarefactions moving apart from a symmetric Riemann state, leaving vacuum or near vacuum at the centre (the Einfeldt 1-2-3 type and the Linde–Roe variant); the basic test of positivity and of internal-energy errors at low density."
status: established
aliases: [double rarefaction, 1-2-3 problem, Einfeldt strong rarefaction, vacuum Riemann problem]
tags: [benchmark, euler, positivity, low-density, riemann-problem]
timestamp: 2026-10-13T00:00:00Z
---

# Double-rarefaction (near-vacuum) Riemann problems

**Variants.**
* *Linde–Roe*: $\rho = 7$, $v_x = \mp1$, $p = 0.2$, $\gamma = 1.4$, $t = 0.6$;
  the exact solution contains vacuum
  ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3, in 1D and 2D;
  [Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.2;
  [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 8, $h = 0.005$).
* *Einfeldt type* ([Einfeldt et al. (1991)](/sources/einfeldt-1991.md); data confirmed at the source, batch 16): $\rho = 1$, $v_x = \mp2$.
  Guo et al. use $p = 0.4$, $h = 0.0025$, $t = 0.1$ (Example 6). Hu et al.
  use $p = 0.1$ on the left with $h = 2.5\times10^{-3}$, $t = 0.1$, where a
  vacuum forms ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.1).
  Reyes et al. run it to $t = 0.15$ on 128 cells
  ([Reyes et al. (2018)](/sources/reyes-2018.md), §5.5).

**What it tests.** Positivity of density and pressure, and the internal
energy $p/(\rho(\gamma - 1))$, which is a ratio of two vanishing numbers
and amplifies their errors.

**Results.**
* RKDG with the positivity limiter captures the low density and
  pressure well. Without it the scheme blows up; with a TVB limiter only
  it runs but is poor ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3).
  FD WENO5 with the limiter is comparable
  ([Zhang & Shu (2012)](/sources/zhang-2012.md), Fig. 5.1).
* With the cut-off flux limiter the rarefaction profiles stay accurate
  although the centre, being vacuum, has no physical meaning
  ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.1).
* Compact WENO with HLLC stays positive (minimum density
  $1.8\times10^{-2}$ and $2.1\times10^{-4}$ in the two variants) but shows
  oscillations in velocity and internal energy at the centre. These are
  attributed to the low-dissipation HLLC flux; Lax–Friedrichs removes them
  ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Examples 6, 8).
* GP-WENO's internal-energy error at the centre shrinks as the stencil
  radius grows; GP-R2 is slightly worse than WENO-JS there
  ([Reyes et al. (2018)](/sources/reyes-2018.md), §5.5).

**Later uses (batch 7).**
* A viscous variant ($\rho = 7$, $v_x = \mp1$, $p = 0.2$, $\mathrm{Re} = 1000$) with
  DG of degree 2–5 on 200 and 400 cells: the low density and pressure are
  captured with the positivity-preserving viscous flux ([Zhang (2017)](/sources/zhang-2017.md),
  Example 3).

**Later uses (batch 8).**
* *Einfeldt data in 2D.* $(\rho, v_x, v_y, p) = (1, \mp2, 0, 0.4)$ on
  $100\times50$ to $t = 0.1$ at first order. A sheared variant,
  $(1, \mp1, \mp2, 5)$, runs to $t = 0.11$ (the caption says 0.1). HLLC
  with selective wave modification runs without failure. The authors
  suggest it is positivity-preserving from these runs, without proof
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.1).
* The 1D Einfeldt problem (Toro's RP2) is robust with HLLEM at second
  order, at very low density ([Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.6.1).

**Later uses (batch 12).**
* *Toro's Test 2, "the 123 problem"* ([Toro (1997)](/sources/toro-1997.md),
  Tables 4.1, 4.3, 6.2). $(\rho, v_x, p) = (1, -2, 0.4)$ on the left and
  $(1, 2, 0.4)$ on the right, $\gamma = 1.4$; the scheme runs put the
  diaphragm at $x = 0.5$ on $[0, 1]$, with 100 cells and $t = 0.15$, the
  time Reyes et al. use above. Exact star values: $p_* = 0.00189$,
  $v_{n*} = 0$, $\rho_{*L} = \rho_{*R} = 0.02185$. This is near vacuum, not
  vacuum: the data satisfy the pressure-positivity
  (no-vacuum) condition of the
  [exact Riemann solver](/methods/exact-riemann-solver.md) (eq. 4.40), and since both
  waves are rarefactions the two-rarefaction pressure is exact.
* *Which first-order solvers fail* (§§6.4, 10.8, 11.5, 12.4). Exact
  Godunov is good in $\rho$, $v_x$ and $p$ but poor in the specific internal
  energy; Lax–Friedrichs is inaccurate in internal energy; HLLC does not
  fail but is less accurate in velocity and internal energy
  ([HLLC Riemann solver](/methods/hllc-riemann-solver.md)). Roe's solver
  "does actually fail" and needs Einfeldt et al.'s modification; Osher's
  solver fails with O-ordering and runs with P-ordering; the
  second-order Richtmyer scheme fails
  ([approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* *Attribution, a qualification of the "Einfeldt type" line above.* That
  line attributes the $\rho = 1$, $v_x = \mp2$ data with $p = 0.4$ to
  Einfeldt et al. (1991). Toro, who names the problem "the 123 problem",
  does not attribute the data to them: he cites them only as background,
  "Test 2 is also useful in assessing the performance of numerical
  methods for low density flows, see Einfeldt et al." (p. 129). The
  batch-8 label "Toro's RP2" and this page's alias "1-2-3 problem" fit
  Toro. Einfeldt et al. (1991) were not ingested at batch 12; the batch-16
  block below settles whether their paper contains the same data; the
  attribution line stays as written.

**Later uses (batch 16).** *The Einfeldt attribution, settled*
([Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §6, Figs. 6.1–6.3).
The paper contains the data, in conserved variables: the "1–2–0–3
problem", $(\rho, \rho v_x, \rho v_y, E) = (1, \mp2, 0, 3)$, i.e.
$\rho = 1$, $v_x = \mp2$, $p = 0.4$ at $\gamma = 1.4$ (reader's
conversion; $\gamma$ is not stated for the runs), on spacing 0.01 with
output at $t = 0.05$ and $0.1$, not Toro's $t = 0.15$. The left momentum is
printed $+2$, a misprint for $-2$ (the text describes two rarefactions
moving apart). This resolves the batch-12 "open" remark for the data;
neither source says that Toro's "123" name derives from the label.
First-order results: Roe "explodes after a few time-steps", and with the
Harten–Hyman or Harten (1983) entropy fixes it oscillates or fails; HLLE
with bounding speeds runs "without any difficulties". The data lie in the
non-linearizable range of Proposition 3.1, so no linearized solver can keep
them positive ([positivity preservation](/properties/positivity-preserving.md)).
*The sheared variant.* Einfeldt et al.'s "1–1–2–5 problem" is
$(\rho, \rho v_x, \rho v_y, E) = (1, \mp1, \mp2, 5)$ (the printed equal
transverse momenta are probably a misprint for $\mp2$): the 5 is the total
energy, giving $p = 1.0$ at $\gamma = 1.4$ (reader's arithmetic), not
$p = 5$. Whether Simon & Mandal's $(1, \mp1, \mp2, 5)$ above is in
$(\rho, v_x, v_y, p)$ as labelled, or relabels Einfeldt's conserved data,
is not checkable from the bundle; recorded as a qualification.

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.2.
3. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.1.
4. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Examples 6, 8.
5. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.5.
6. [Zhang (2017)](/sources/zhang-2017.md), Example 3.
7. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.1.
8. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.6.1.
9. [Toro (1997)](/sources/toro-1997.md), §§4.3, 6.4, 10.8, 11.5, 12.4, Tables 4.1, 4.3, 6.2.
10. [Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §§3, 6, Figs. 6.1–6.6.
