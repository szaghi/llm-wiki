---
type: Benchmark
title: "Sod shock tube"
description: "The one-dimensional Euler Riemann problem of Sod, whose solution has a rarefaction, a contact and a shock; the sources use it to check that asynchronous, adaptive, semi-implicit, IMEX and single-stage Lax–Wendroff time integrators stay non-oscillatory at shocks, with qualitative comparisons against reference runs."
status: established
aliases: [Sod problem, Sod's shock tube, Sod Riemann problem]
tags: [verification, ssp, imex, step-size-control]
timestamp: 2026-10-20T06:18:00Z
---

# Sod shock tube

The Sod problem is the Riemann problem for the one-dimensional Euler equations of an
ideal gas with $\gamma=1.4$ (here $\gamma$ is the ratio of specific heats, page-local)
and the data

$$(\rho,u,p)=\begin{cases}(1,\ 0,\ 1),& x<x_0,\\ (0.125,\ 0,\ 0.1),& x>x_0,\end{cases}$$

(page-local density $\rho$, velocity $u$, pressure $p$), integrated to $t=0.2$. Its
solution has a left rarefaction, a contact discontinuity and a right shock. The sources
use it to check that a time integrator stays non-oscillatory at a shock, not to measure
temporal order: all comparisons are qualitative, against a reference run or the exact
Riemann solution.

## Configurations in the sources

| Source | Domain, discontinuity | Space | Time integrator | Resolution |
|---|---|---|---|---|
| [Unfer (2021)](/sources/unfer-2021.md), §4.2 | unspecified, $t=0.2$ | multi-slope MUSCL, third-order limiter with smoothness sensor | asynchronous ARK3 vs synchronous SSPRK(3,3), CFL 0.4 | 200 cells |
| [Fekete et al. (2022)](/sources/fekete-2022.md), Eq. (27) | $[0,1]$, $x_0=0.5$ | WENO5 | embedded SSP and classical pairs, PID step-size controller | not given |
| [Birke et al. (2024)](/sources/birke-2024.md), §4.1 | with gravity $g_x=-1$, $t=0.2$ | finite volumes | semi-implicit IMEX | 100 cells, reference on 20,000 |
| [Orlando et al. (2025b)](/sources/orlando-2025-b.md), §4.3 (Eq. (81)) | $(-0.5,0.5)$, $x_0=0$, Dirichlet data | DG, degree $r=0$ | IMEX-RK(2,2,2) and its semi-implicit form | 500 elements, $h\approx1.33\times10^{-3}$ |
| [Babbar et al. (2022)](/sources/babbar-2022.md), §9 (Eq. 14) | $[0,1]$, $t=0.2$ | flux reconstruction with TVB limiter (parameter 10) | single-stage Lax–Wendroff against SSP Runge–Kutta | 100 cells |

Orlando et al. (2025b) replace the ideal gas by a Peng–Robinson equation of state
($c_v=1$, $R_g=0.4$, $b=0.5$, $a(T)=0.5/\sqrt T$, page-local symbols of that source).
Their step corresponds to an acoustic Courant number of about 1.23 and a material Courant
number of about 0.47.

## What it shows

* **Asynchronous local time stepping matches the synchronous scheme.** Unfer (2021,
  §4.2, Fig. 5) finds "very little difference" between the cell-wise asynchronous ARK3
  and synchronous SSPRK(3,3). His smoothness sensor exceeds its threshold only near the
  shock and the end of the rarefaction; with sensor parameter 1 small oscillations
  appear near the contact, and a smaller parameter removes them at the cost of local
  order loss. See [local time stepping](/methods/local-time-stepping.md) and
  [SSP methods](/methods/strong-stability-preserving-runge-kutta.md).
* **Step-size control at shocks.** Fekete et al. (2022) use the problem in
  work-precision diagrams for their embedded SSP pairs. The fourth-order SSPERK(10,4)
  pairs beat Dormand–Prince on the hyperbolic tests for tolerances $\ge10^{-4}$ (Figs.
  11d–13d); see [step-size control](/methods/step-size-control.md).
* **Semi-implicit and IMEX schemes at high Mach number.** Birke et al. (2024, Fig. 1)
  use it to show that their low-Mach semi-implicit scheme also captures shocks outside
  the low-Mach regime. Orlando et al. (2025b, Fig. 7) find that the IMEX scheme with a
  Picard-iterated pressure and the semi-implicit scheme agree "excellently" with each
  other and well with an SSPRK(3,3) reference on 32,000 elements. See
  [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).

* **Single-stage Lax–Wendroff time stepping.** Babbar et al. (2022, §9, Figs. 23–29) run
  Sod together with the harder 1D Riemann and shock problems of the same family: Lax's problem
  on $[-5,5]$ to $t=1.3$, the Shu–Osher shock–entropy-wave interaction on $[-5,5]$ to $t=1.8$
  (400 cells), the Woodward–Colella blast wave (400 cells, with a positivity limiter), a
  stationary contact and Toro's test 5. Their Lax–Wendroff flux reconstruction needs the
  limiter once per step instead of once per Runge–Kutta stage (§7). HLLC and Roe fluxes keep a
  stationary contact exact, while Rusanov, Lax–Friedrichs and HLL smear it over two cells; the
  $g_2$ correction function fails on Shu–Osher at degree 1 with the Fourier CFL number
  (negative pressure) and needs CFL 0.44, one reason they recommend Radau correction (§9.6–9.7).
  See [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md).

## Qualifications

* Babbar et al. (2022) state 100 cells for Lax's problem in the text (§9.3) and 200 in the
  Fig. 24 caption (printed inconsistency).

* No source reports a temporal convergence rate on this problem. The shock limits the
  observed order to one in $L^1$, so the test checks robustness, not order *(compiler
  remark, not in the sources)*.
* Fekete et al. (2022) do not state the grid resolution, and Unfer (2021) does not
  state the domain; the Mach number of the Orlando et al. (2025b) run is not printed.

# Citations

- [Unfer (2021)](/sources/unfer-2021.md) — §4.2, Fig. 5.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — Eq. (27), Figs. 11d–13d.
- [Birke et al. (2024)](/sources/birke-2024.md) — §4.1, Fig. 1.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §4.3, Eq. (81), Fig. 7.
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §7, §9 (Eqs. 14–16, Figs. 23–29), §9.6–9.7; arXiv v1.
