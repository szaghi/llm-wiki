---
type: Benchmark
title: "Burgers equation: shock formation"
description: "Inviscid Burgers equation with smooth sinusoidal data (periodic, or with an inflow boundary), run before the breaking time to measure the design order and after it to check a non-oscillatory shock and the order away from it; set-ups, breaking times and measured orders as printed in fifteen sources, from ENO (1987) to boundary treatments (2021)."
status: established
aliases: [Burgers shock formation, nonlinear Burgers accuracy test, Burgers equation with sine data, scalar Burgers test]
tags: [benchmark, 1d, 2d, accuracy, eno, weno, boundary-treatment]
timestamp: 2026-10-13T00:00:00Z
---

# Burgers equation: shock formation

**The problem.** The scalar conservation law $u_t + \left(\tfrac12 u^2\right)_x = 0$,
$f(u) = \tfrac12 u^2$, with smooth sinusoidal data. The solution stays
smooth up to the breaking time, the reciprocal of the steepest negative
slope of the data (where the slope is $-\max\vert u'(x,0)\vert$), then
a shock forms and runs into the rarefaction that follows it. The exact
solution is computed by a Newton iteration on the characteristic
relation ([Harten et al. (1987)](/sources/harten-1987.md), §7, eqs.
7.2–7.3; [Shu & Osher (1988)](/sources/shu-1988.md), §IV). One problem
gives two tests: before breaking, the order of a nonlinear smooth
problem; after it, a clean shock and the accuracy of the smooth part.
When the data contain a sonic point ($f'(u) = 0$), the test also probes
the building-block flux there ([Shu & Osher (1988)](/sources/shu-1988.md),
§IV; [accuracy at critical points](/properties/accuracy-at-critical-points.md)).
No source proves anything about it; every order below is observed.

## Set-ups as printed

Breaking times marked "printed" are the sources'; the others are the
compiler's, by the rule above.

| Data $u(x,0)$ | Domain and boundaries | Breaking | Times run | Sources |
|---|---|---|---|---|
| $\tfrac14 + \tfrac12\sin\pi x$ | $[-1, 1]$, periodic | $2/\pi$ (printed) | 0.3; $2/\pi$ and 1.1 | [Shu & Osher (1988)](/sources/shu-1988.md), Ex. 1 |
| same | same | $2/\pi$ | $1/\pi$ only | [Balsara & Shu (2000)](/sources/balsara-2000.md), §IV.a (domain not printed); [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §4.2 |
| same | $(-1, 1)$, inflow at $x = -1$ with the exact periodic solution, outflow at $x = 1$ | $2/\pi$ | 0.3 or 0.5; 1.1, 8, 12 | [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.1.2; [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Ex. 3 |
| $1 + \tfrac12\sin\pi x$ | $[-1, 1]$, periodic, or inflow–outflow | $2/\pi$ (printed) | 0.3; about $2/\pi$ | [Harten et al. (1987)](/sources/harten-1987.md), §7 A1 |
| same | $[-1, 1]$, periodic | $2/\pi$ (printed) | 0.33; 0.5 and 1.5 | [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), §5, Test 3 |
| $\tfrac12 + \sin\pi x$ | period 2 | $1/\pi$ (printed by Liu et al.) | 0.15; $1/\pi$ and 0.55 | [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §4.1, Ex. 2 |
| same | 2-periodic, randomly perturbed cells | $1/\pi$ | $0.5/\pi$; $1.5/\pi$ | [Qiu & Shu (2005)](/sources/qiu-2005.md), Exs. 3.1, 3.4 |
| same | $(0, 2)$, periodic | $1/\pi$ | $0.5/\pi$ only | [Zhu & Qiu (2016)](/sources/zhu-2016.md), Ex. 3.1 |
| same | $[-1, 1]$, periodic | $1/\pi$ | 0.55 (output time, not stated as such) | [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §4.1.3, case 2 |
| $0.3 + 0.7\sin\pi(x+1)$ | $[-1, 1]$, periodic | $1/(0.7\pi)$ (printed) | $2/\pi$ | [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §5.1 |
| $-\sin\pi x$ (steady shock at $x = 0$) | $[-1, 1]$, periodic | $1/\pi$ | to 1.5 | [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §4.1.3, case 1 |
| same, as $\sin(\pi x + \pi)$ | inflow $u(-1, t) = 0$ | $1/\pi$ (printed) | 0.6 | [Harten et al. (1987)](/sources/harten-1987.md), Fig. 4 |
| $1 + 2\sin\pi x$ | $(0, \tfrac32)$, each end inflow or outflow by the sign of $u$ | $1/(2\pi)$ | 0.12; 1.5 | [Lu et al. (2021)](/sources/lu-2021.md), Ex. 3.2 |
| $1 + \tfrac12\sin x$, $1 + 0.2\sin x$ | $[0, 2\pi]$, inflow at $x = 0$ | 2 and 5 | 1 only | [Li, Shu & Zhang (2016)](/sources/li-2016.md), §4.2 |
| $\tfrac12 + \sin 2\pi x$ | $[0, 1]$, periodic, 256 cells | $1/(2\pi)$ | 0.8 | [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §6.5 |

**Two dimensions.** $u_t + \left(\tfrac12u^2\right)_x + \left(\tfrac12u^2\right)_y = 0$
with data depending on $x + y$, so the exact solution is the 1D one
along the diagonal:
* $\tfrac14 + \tfrac12\sin\tfrac{\pi(x+y)}{2}$ on $[-2, 2]^2$, at 0.3,
  $2/\pi$ and 1.1 ([Shu & Osher (1988)](/sources/shu-1988.md), Ex. 2);
* $\tfrac12 + \sin\tfrac{\pi(x+y)}{2}$, 4-periodic, at $0.5/\pi$
  ([Qiu & Shu (2005)](/sources/qiu-2005.md), Ex. 3.2;
  [Zhu & Qiu (2016)](/sources/zhu-2016.md), Ex. 3.2);
* $0.75 + 0.5\sin\pi(x+y)$ with the exact solution as inflow data, on
  $(-1, 1)^2$ and on a domain cut by the line $y = -x/\sqrt3 - 1$, at
  0.15, 0.55, 4 and 6 ([Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Ex. 8);
* $1 + 0.5\sin\pi(x+y)$ on $(-1, 1)^2$ and on the unit disk, at 0.2 and
  1.2 ([Lu et al. (2021)](/sources/lu-2021.md), Ex. 3.7).

A steady 2D analogue, $u_t + \left(\tfrac12u^2\right)_x + u_y = 0$ on
$[0, 2\pi)\times[0, 1]$ with $u = 5\sin x$ or $2 + 5\sin x$ at $y = 0$,
is 1D Burgers with $y$ as time; it is shown only as level curves
([Shu & Osher (1989)](/sources/shu-1989.md), §5, Ex. 4).

## Before breaking: measured orders

Finest-grid orders as printed ($L^1$, then $L^\infty$).

| Source | Scheme | Grid | Orders |
|---|---|---|---|
| [Harten et al. (1987)](/sources/harten-1987.md), Tables IA–IB | [ENO](/methods/eno-reconstruction.md) $r = 4$, 5 with a [Taylor](/methods/taylor-time-discretization.md) step, Roe flux, CFL 0.6 | 128 cells | reconstruction via primitive: $L^\infty$ 3.02 ($r = 4$) and 4.50 ($r = 5$); via deconvolution: $L^1$ 4.53 and 5.53, $L^\infty$ 4.76 and 5.36 |
| [Shu & Osher (1988)](/sources/shu-1988.md), Table 1 | flux ENO, Lax–Friedrichs building block, [TVD Runge–Kutta](/methods/ssp-runge-kutta.md), orders 3 and 4 | $h = 1/40$ | 3.13 and 2.89 (third); 4.76 and 4.35 (fourth) |
| [Liu, Osher & Chan (1994)](/sources/liu-1994.md), Table III | [WENO](/methods/weno.md) $r = 3$, Roe flux with entropy fix | 320 | 4.79 and 6.21; the $L^\infty$ order is 3.41 between 80 and 160 |
| [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Table 5.3 | [central WENO](/methods/central-weno.md), orders 3 and 4 (Levy et al.'s $m$) | 640 | 3.11 and 3.53 (order 3, above 4 on middle grids); 4.19 and 4.18 (order 4) |
| [Balsara & Shu (2000)](/sources/balsara-2000.md), Table VI | ninth-order [MPWENO](/methods/monotonicity-preserving-limiter.md), LLF flux, RK3 with $\Delta t \propto h^{3}$ | 160 | 8.52 and 8.53 |
| [Qiu & Shu (2005)](/sources/qiu-2005.md), Table 1 | [WENO-limited RKDG](/methods/weno-limited-dg.md), $P^1$–$P^3$, perturbed meshes | 320 | $P^3$: 3.98 and 4.22 limited, 4.00 and 4.22 unlimited; $P^2$: 2.81 and 2.75 limited, 2.81 and 2.60 unlimited |
| [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), Table 2 | [WENO-ZQ and WENO-AO](/methods/weno-ao.md), RK4 with a step shrunk to expose spatial order | 80–160 | ZQ 5.37 and 4.88; AO(7,5,3) 7.30 and 6.98; AO(9,5,3) 8.87 and 8.57 |
| [Zhu & Qiu (2016)](/sources/zhu-2016.md), Table 3.1 | WENO-ZQ against WENO-JS, RK3, CFL 0.6 | 320 | ZQ 5.07 and 5.06; JS 5.11 and 4.25 |
| [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), Tables 9–11 | FD-WENO5 with three ghost-value treatments | 1280 | 5.09 and 5.06 (Lagrange); 5.55 and 5.13 ([weighted extrapolation](/methods/weighted-extrapolation.md)) |
| [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Tables 2.6, 2.15 | FD-WENO5 with [ILW](/methods/inverse-lax-wendroff.md), conservative modification | 2560 (1D), $640^2$ (2D) | 5.06 and 5.03 (1D); 5.37 and 4.97 (2D square) |
| [Lu et al. (2021)](/sources/lu-2021.md), Tables 3.2, 3.6 | FD-WENO5 with ILW and WENO-type extrapolation | 512 (1D), $256\times320$ (2D) | 4.97 and 4.96 (1D); 5.10 and 4.81 (square); $L^1$ 5.11 and irregular $L^\infty$ orders on the disk |
| [Li, Shu & Zhang (2016)](/sources/li-2016.md), Tables 4.3–4.4 | fifth-order scheme with simplified ILW ($k_{\mathrm{ILW}} = 2$), RK3 | 1280 | $L^2$ 3.00 and $L^\infty$ 2.99 with $\Delta t \propto h$; 4.989 and 4.987 with $\Delta t \propto h^{5/3}$; the paper's question is the stability of the boundary treatment |

**What it showed.** Every scheme reaches about its design order on the
finest grids, with three recurring departures, all printed and none
explained by a proof. The $L^\infty$ order lags the $L^1$ order on some
grids (Harten et al.'s primitive reconstruction; Liu et al.'s 3.41;
WENO-JS's 4.25 against WENO-ZQ's 5.06 in Zhu and Qiu's Table 3.1).
Qiu and Shu's $P^2$ runs reach about 2.8 with and without the limiter,
uncommented. Li, Shu and Zhang find the nonlinear problem more stable
under ILW than their linear analysis predicts: $k_{\mathrm{ILW}} = 2$ is
stable for the fifth-order scheme where 3 is predicted, for $1 + \tfrac12\sin x$ (§4.2.1).

## After breaking

* **Errors away from the shock.** Shu and Osher exclude a band of 0.1
  around the shock: at $h = 1/40$, the $L^1$ errors at $2/\pi$ are
  3.5e-5 (third order) and 8.6e-6 (fourth), "of the same magnitude as in
  the smooth case" (Table 2; 2D in Table 4). Liu, Osher and Chan do the
  same at $t = 0.55$ and find fifth order, $L^1$ 6.70 and $L^\infty$
  5.72 between 160 and 320 points, and conclude that "error propagation
  of the schemes is still very local" (Table IV). Pirozzoli's $L^1$
  error outside $\pm 0.1$ of the shock scales overall as the inverse fifth
  power of the number of points; on coarse grids the shock dominates, and
  from 320 points the
  [hybrid compact-WENO](/methods/hybrid-compact-weno.md) schemes are 2–3
  times more accurate than WENO of the same order (Fig. 9, graph only).
* **The shock itself.** Shu and Osher print the pointwise errors at ten
  points across the shock: the largest is about 0.12, next to it, with no
  oscillation. Levy, Puppo and Russo show the central-WENO weights giving
  almost zero weight to oscillatory stencils after breaking, with the
  shock spread over two cells (Fig. 5.1). Qiu and Shu report "good
  nonoscillatory shock transitions" for $P^1$–$P^3$ (Fig. 1).
* **Comparison by plots only.** Rathan and Naga Raju (seventh-order
  WENO-NS against WENO-BS and WENO-Z, 200 cells, figures without time
  labels) say WENO-NS "captures the shock better"; Harten et al. plot
  $r = 2$ and 4 on 16 cells. The boundary-treatment papers judge by eye
  that the shock is "well captured" as it leaves and re-enters through
  the boundary (Baeza et al., Fig. 6; Ding et al., Figs. 2.2–2.3,
  2.9–2.10; Lu et al., Figs. 3, 6). None of these gives a post-shock norm.
* **Time step.** With a variable-step SSP multistep method the step stays
  constant until the shock forms and then grows; the Courant number
  settles at the theoretical TVD maxima, 1/4 and 1/6
  ([Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §6.5;
  [SSP linear multistep](/methods/ssp-linear-multistep.md)).

**As printed.** Shu and Osher's Table 1 gives the fourth-order
$L^\infty$ error at $h = 1/40$ as 5.4e-5, which does not match its order
4.35 (5.4e-6 would). Balsara, Garain and Shu print the same 80-zone
$L^\infty$ entry (1.2158e-5, order 4.88) for WENO-ZQ and WENO-AO(5,3).
Baeza et al.'s Table 10 prints 9.45e-6 for the $L^\infty$ error at both
160 and 320 points, against orders 8.70 and 5.37. Ding et al.'s 2D
captions print $h_x = h_y = 1/80$ against $h_x$ = 2 over the number of cells in $x$
in their tables. Balsara and Shu's run time $1/\pi$ is before breaking
by a factor of two. These are compiler's checks.

**Related.** An "isentropic Euler–Burgers" problem sets the Euler
velocity to a Burgers wave that breaks at a printed time $t = 1$, with
density and pressure from isentropic relations, and runs to four times
the breaking time to
pass the shock through AMR interfaces
([Wang et al. (2025)](/sources/wang-2025.md), §6.2; preprint;
[high-order AMR](/methods/high-order-amr.md)). Burgers Riemann problems
(discontinuous data) are a different test, used for example to show the
overshoot of a non-SSP Runge–Kutta method
([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §7 A1, Tables IA–IIB, Figs. 2–4.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §IV, Exs. 1–2, Tables 1–4 (ICASE report).
3. [Shu & Osher (1989)](/sources/shu-1989.md), §5, Ex. 4.
4. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §4.1, Ex. 2, Tables III–IV.
5. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), §5, Test 3, Table 5.3, Fig. 5.1.
6. [Balsara & Shu (2000)](/sources/balsara-2000.md), §IV.a, Table VI.
7. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §5.1, Figs. 7–9.
8. [Qiu & Shu (2005)](/sources/qiu-2005.md), Exs. 3.1, 3.2, 3.4, Tables 1–2, Fig. 1.
9. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §4.2, Table 2.
10. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Exs. 3.1–3.2, Tables 3.1–3.2.
11. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §4.1.3, Figs. 5–6.
12. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.1.2, Tables 9–11, Fig. 6.
13. [Li, Shu & Zhang (2016)](/sources/li-2016.md), §4.2, Tables 4.3–4.6.
14. [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §6.5, Fig. 1a.
15. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Exs. 3 and 8, Tables 2.6–2.7, 2.15–2.16.
16. [Lu et al. (2021)](/sources/lu-2021.md), Exs. 3.2 and 3.7, Tables 3.2, 3.6.
17. [Wang et al. (2025)](/sources/wang-2025.md), §6.2 (arXiv preprint).
