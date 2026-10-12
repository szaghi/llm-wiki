---
type: Benchmark
title: "Double-rarefaction (near-vacuum) Riemann problems"
description: "Two rarefactions moving apart from a symmetric Riemann state, leaving vacuum or near vacuum at the centre (the Einfeldt 1-2-3 type and the Linde–Roe variant); the basic test of positivity and of internal-energy errors at low density."
status: established
aliases: [double rarefaction, 1-2-3 problem, Einfeldt strong rarefaction, vacuum Riemann problem]
tags: [benchmark, euler, positivity, low-density, riemann-problem]
timestamp: 2026-10-12T00:00:00Z
---

# Double-rarefaction (near-vacuum) Riemann problems

**Variants.**
* *Linde–Roe*: $\rho = 7$, $v_x = \mp1$, $p = 0.2$, $\gamma = 1.4$, $t = 0.6$;
  the exact solution contains vacuum
  ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3, in 1D and 2D;
  [Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.2;
  [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 8, $h = 0.005$).
* *Einfeldt type* (Einfeldt et al. 1991): $\rho = 1$, $v_x = \mp2$.
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

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.2.
3. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.1.
4. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Examples 6, 8.
5. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.5.
6. [Zhang (2017)](/sources/zhang-2017.md), Example 3.
7. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.1.
8. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.6.1.
