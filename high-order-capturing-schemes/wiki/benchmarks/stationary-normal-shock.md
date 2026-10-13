---
type: Benchmark
title: "Stationary normal shock test (one-dimensional carbuncle)"
description: "A steady normal shock captured with one interior cell, whose state lies on the Hugoniot curve at a chosen sub-cell position, in 1D, in a thin 2D strip, as a small 2D grid for a matrix stability analysis, or inclined to the grid: the most direct test of whether a numerical flux keeps a strong steady shock stable."
status: established
aliases: [steady shock test, one-dimensional carbuncle test, matrix stability analysis of a shock, inclined stationary shock]
tags: [benchmark, euler, shock-instability, steady]
timestamp: 2026-10-13T00:00:00Z
---

# Stationary normal shock test

**One-dimensional and 1.5-dimensional versions**
([Xie et al. (2021)](/sources/xie-2021.md), §§3.1, 3.4–3.5, after Kitamura, Roe & Ismail).
* **Set-up.** 50 cells, Rankine–Hugoniot states left and right. Cell 13
  holds an intermediate state on the Hugoniot curve, placed by the
  sub-cell shock position $\epsilon_{\mathrm{sh}} \in \{0, 0.1, \dots, 0.9\}$.
  The outflow mass flux is fixed, and $M_s$ runs up to beyond 20. The
  scheme is first order with a three-stage first-order Runge–Kutta step,
  CFL 0.5, 40 000 steps. The 1.5D version has $50\times25$ cells.
* **1D results.** HLLE and HLLEM are unstable for
  $\epsilon_{\mathrm{sh}} = 0$–$0.3$ in Table 1. The text says 0.1–0.3,
  an inconsistency recorded as printed. The intermediate state oscillates
  and enters "an approximate limit cycle involving the shedding of
  spurious waves", and the residual does not converge.
* **Stabilizing with entropy control.** At $M_s = 6$ and
  $\epsilon_{\mathrm{sh}} = 0.3$, applying the entropy control in cell 13
  only stabilizes the shock once $\varphi_{\mathrm p}$ falls below a
  threshold of about 0.73–0.76 over $M_s \approx 4$–22 (read from plots).
  The 1.5D version needs much smaller factors: 0.33 at $M_s = 6$, and
  about 0.16–0.34 over the range. Once stable, the residual falls to about
  $10^{-25}$ ([cures](/methods/shock-instability-cures.md)).

**Matrix stability analysis** ([Simon & Mandal (2019)](/sources/simon-2019.md), §8,
after Dumbser, Moschetta & Gressier).
* **Set-up.** A thin shock between cells 6 and 7 of an $11\times11$ grid
  on $[0,1]^2$, periodic in $y$. At $M_s = 7$ the upstream state is
  $(\rho, v_x, v_y, p) = (1, 1, 0, 0.01457)$, with the Rankine–Hugoniot
  state downstream. The spectrum of the linearized first-order spatial
  operator is computed. The method also covers $M_s$ = 3, 10 and 20.
* **Spectrum.** The largest real part is $+8.15562$ for HLLC at
  $M_s = 7$. It falls with the selective-wave-modification coefficient,
  through $+0.55869$ at 1.0, to $-0.66053$ at 3.5. Higher $M_s$ raises the
  growth rate at every coefficient, reaching about 17 for HLLC at
  $M_s = 20$.
* **Nonlinear run** ($t = 20$). Plain HLLC develops a saw-tooth
  post-shock density. The modified scheme is stable only for a
  coefficient of at least 2.5, so the linear and nonlinear thresholds
  differ.

**Shock-speed map.** The stationary shock is the $M_{\mathrm{prop}} = 0$
row of Kitamura & Shima's map on Quirk's grid, with the shock on a cell
interface. There grid perturbations have no influence, since the shock
does not cross cells. Each flux has its own "comfortable" shock location.
Stationary shocks are "either more or less stable than moving ones,
depending on the flux functions"
([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§IV.B, V;
[Quirk's test](/benchmarks/quirk-odd-even-test.md)).

**Inclined stationary shock** (after Ohwada et al.).
* **Set-up.** A Mach 7 shock along $y = 2(x - 12)$, at 63.43° to the
  grid, on $50\times30$ cells over $[0,50]\times[0,30]$, run to $t = 5$
  at first order. The states are
  $(\rho, v_x, v_y, p) = (1, 447.26, -223.50, 3644.31)$ and
  $(5.444, 82.15, -41.05, 207725.94)$
  ([Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.6).
* **Results.** HLLC and HLLEM show a saw-tooth density behind the shock.
  Selective wave modification and anti-diffusion control keep it clean,
  and the pressure-sensor HLLC variant comes "close to exact". The
  shear-only control of Xie et al. (2017) fails
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.3;
  [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.6).

See [numerical shock instability](/definitions/numerical-shock-instability.md).

**Later uses (batch 11).** *A perturbed-column variant at Mach 20, at
second order* ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III F, eq. 25).
* **Set-up.** $51\times26$ cells, a steady normal shock at $M_s = 20$, with
  Rankine–Hugoniot states in columns $i \le 39$ and $i \ge 41$. In the
  intermediate column $i = 40$ the density is 0.2 times the left-state
  density plus 0.8 times the right-state density in odd rows, and 0.4
  plus 0.6 in even rows, with "other variables calculated based on" it. CFL 0.5; MUSCL reconstruction; output after $10^4$
  and $4\times10^4$ steps. The domain size, upstream state and boundary
  conditions are not printed.
* **Results.** With HLLC the odd–even decoupling is "clearly visible",
  and the paper says the steady shock "dies out after $4\times10^4$ time
  steps". HLL and HLL-BVD are "free from carbuncle instability"
  (Figs. 10–11).
* **Attribution.** The paper calls this the "odd–even perturbation
  problem" proposed by Quirk. The perturbation sits in the shock-cell
  state of a stationary shock, not in the grid of a moving one, so it is
  filed here; the attribution is recorded as printed on the
  [Quirk test](/benchmarks/quirk-odd-even-test.md) page.

**Later uses (batch 14).** *An early one-dimensional version*
([Harten (1983)](/sources/harten-1983.md), §7.I, eq. 7.9, Figs. 4–5).
* **Set-up.** Two states related by the Rankine–Hugoniot conditions of
  the $v_x - c$ field with zero shock speed, upstream $\rho = p = 1$,
  $\gamma = 1.4$; upstream Mach number 4 (pressure ratio 18.5) and 10
  (ratio 116.5); 100 cells, 50 steps, $\nu = 0.95$; Harten's simplified
  second-order TVD scheme (ULT2); pressure profiles only.
* **Results.** At Mach 4 the entropy-fix parameter is set to 0.1 and
  0.25, at Mach 10 to 0.1 "for robustness". The inverted, inadmissible
  Mach 4 discontinuity is broken up with parameter 0.1, while with 0 it
  is "an entropy-violating stationary solution for ULT2" (Fig. 5). This
  is a one-dimensional test of entropy enforcement, not of the
  multidimensional instability the tests above probe.

# Citations

1. [Xie et al. (2021)](/sources/xie-2021.md), §§3.1, 3.4–3.5.
2. [Simon & Mandal (2019)](/sources/simon-2019.md), §§8, 9.3.
3. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.6.
4. [Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§IV.B, V.
5. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III F.
6. [Harten (1983)](/sources/harten-1983.md), §7.I, eq. 7.9, Figs. 4–5.
