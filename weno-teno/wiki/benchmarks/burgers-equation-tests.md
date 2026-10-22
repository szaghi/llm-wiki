---
type: Benchmark
title: "Burgers equation tests"
description: "The inviscid Burgers equation as test bed: sine data for accuracy before the shock forms and shock capturing after, discontinuous data, a two-dimensional four-quadrant Riemann problem, and special Euler data with gamma = 3 whose solution is a Burgers solution; records setups, breaking times and reported orders."
status: established
aliases: [Burgers equation, inviscid Burgers test, Burgers sine wave, two-dimensional Burgers Riemann problem]
tags: [benchmark, weno, cweno, dg]
timestamp: 2026-10-22T12:00:00Z
---

# Burgers equation tests

The inviscid Burgers equation $\partial_tu+\partial_x(u^2/2)=0$, and its
two-dimensional form $\partial_tu+\partial_x(u^2/2)+\partial_y(u^2/2)=0$,
is the simplest genuinely nonlinear conservation law. Smooth data
steepen and form a shock at the breaking time
$t_{\mathrm b}=-1/\min_xu_0'(x)$ (page-local symbol), so a single
initial profile serves two tests: an accuracy test at $t<t_{\mathrm b}$,
where the exact solution follows from characteristics, and a
shock-capturing test at $t>t_{\mathrm b}$. The sources also use
discontinuous data, a two-dimensional Riemann problem, and Euler data
that reduce exactly to Burgers.

## Sine data: accuracy and shock formation

| Source | Data | Domain | Accuracy time | Shock time |
|---|---|---|---|---|
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.1 | $u_0=0.5+\sin(\pi x)$ | $[0,2]$, periodic | $0.5/\pi$, 10–320 cells | $1.5/\pi$, 200 cells |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.2 | $u_0=0.5+\sin(\pi(x+y)/2)$ | $[0,4]^2$, periodic | $0.5/\pi$, $10^2$–$320^2$ | $1.5/\pi$, $200^2$, cut along $x=y$ |
| [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) §4.1, §4.3.1 | $u_0=0.5-0.25\sin(\pi x)$ | $[0,2]$, periodic | $1$, $\Delta t=h,10h,50h$ | $2$, 256 cells, $\Delta t=3h,5h$ |

For $u_0=0.5+\sin(\pi x)$, $t_{\mathrm b}=1/\pi$; along the diagonal the
two-dimensional data have the same breaking time; for
$u_0=0.5-0.25\sin(\pi x)$, $t_{\mathrm b}=4/\pi\approx1.27$ *(compiler
check, not in the sources)*. The accuracy times thus lie before and
the shock times after breaking.

**Orders.** Li, Shu & Qiu's sixth-order moment-based
[multi-resolution HWENO](/methods/hermite-weno.md), with the first
moments modified only in cells flagged by their indicator (M5-I),
reaches $L^1$ error $3.95\times10^{-13}$ at 320 cells (order 5.96) in
1D and $6.83\times10^{-12}$ at $320^2$ (order 6.36) in 2D; modifying the
moments in every cell (M5-NI) drops the order to five, as they expect
(4.97 and 4.88; Tables 3.1–3.2). On the shocked data the unmodified and
modified schemes both match the exact solution with "not much
difference" (Figs. 3.1–3.2). Puppo et al.'s time-limited implicit
[Quinpi](/methods/quinpi.md) scheme Q3P1 converges at third order even
at time steps of 10 and 50 cell widths: $L^1$ errors
$3.66\times10^{-7}$ ($\Delta t=h$, 2560 cells), $1.29\times10^{-7}$
($\Delta t=10h$, 5120 cells) and $1.41\times10^{-5}$ ($\Delta t=50h$,
5120 cells), with finest-grid rates 2.99, 2.99 and 2.79 (Table 1);
implicit Euler is first order and the unlimited DIRK–CWENO scheme D3P1
third order on the same data (Fig. 1). After the shock forms, Q3P1 is
slightly more diffusive than D3P1 but much less than implicit Euler,
and at $\Delta t=5h$ it reduces D3P1's oscillations (Figs. 4–5).

## Discontinuous data and interacting shocks

[Puppo et al.](/sources/puppo-2023.md) §4.3.2–4.3.3 run, on periodic
$[-1,1]$:

- the top hat $u_0=1$ on $|x|\le0.25$, $0$ otherwise, to $t=0.5$ on 400
  cells with $\Delta t=3h,5h$, which develops a rarefaction and a moving
  shock (Fig. 6). Without their conservative correction Q3P1 loses mass
  and misplaces the shock; with it mass is conserved at all times and
  the shock is correctly placed (Fig. 7). An explicit first-order
  predictor, even at each Runge–Kutta abscissa, does not prevent
  spurious oscillations at $\Delta t=5h$ (Fig. 8);
- $u_0=0.2-\sin(\pi x)+\sin(2\pi x)$ on 256 cells with $\Delta t=5h$,
  shown at $t=1/(2\pi)$ (shock formation), $0.6$ (before the shocks
  interact) and $1$ (after): Q3P1 is non-oscillatory and sharper than
  implicit Euler (Fig. 9).

## Two-dimensional Riemann problem

[Pazner (2021)](/sources/pazner-2021.md) §5.5 solves
$\partial_tu+\nabla\cdot(\tfrac12u^2(1,1))=0$ on $[0,1]^2$ with quadrant
values $-1$ ($x>0.5$, $y>0.5$), $-0.2$ ($x\le0.5$, $y>0.5$), $0.5$
($x\le0.5$, $y\le0.5$) and $0.8$ ($x>0.5$, $y\le0.5$), the exact solution
imposed on the boundary, to $t=0.5$. With $120^2$ degrees of freedom as
$N=2$, $5$, $11$ on $40^2$, $20^2$, $10^2$ elements, and a reference with
$N=1$ on $512^2$ elements, his subcell
[convex-limited](/methods/convex-limiting.md) DG resolves the solution
well even on the coarsest mesh and captures discontinuities that are
not aligned with element boundaries (Fig. 11). The same quadrant values
and final time are run by [Peng, Sun & Wu (2024)](/sources/peng-2024.md)
Ex. 5.11 on $256^2$ cells, recorded with the Euler configurations on
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md).

## Euler data that reduce to Burgers

For $\gamma=3$ the isentropic data $p=\rho^\gamma$, $v=\sqrt\gamma\,\rho$
make the sound speed $c=\sqrt{\gamma p/\rho}=\sqrt3\,\rho$ equal to $v$.
The Riemann invariant $v-c$ is then identically zero, and the other,
$v+c=2\sqrt3\,\rho$, is transported at its own speed $v+c$, so it obeys
Burgers' equation *(compiler check, not in the sources)*. The sources
use this to obtain exact smooth Euler solutions:

- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 1: $\gamma=3$,
  $\rho=(1+0.2\sin x)/(2\sqrt\gamma)$, $v=\sqrt\gamma\rho$, $p=\rho^\gamma$
  on periodic $[0,2\pi]$; $2\sqrt\gamma\rho$ solves Burgers with data
  $1+0.2\sin x$, smooth until $t=5$, and the run stops at $t=3$. An
  artificial material interface between identical fluids starts at
  $x=\pi$ with their full interface algorithm active; the density
  converges at fifth order, $L^1$ error $1.05\times10^{-5}$ at 80 points to
  $1.07\times10^{-8}$ at 320 (order 5.14; Table 2). Ex. 8 is the 2D
  analogue, $\rho=(1+0.2\sin((x+y)/2))/\sqrt{2\gamma}$,
  $v_1=v_2=\sqrt{\gamma/2}\,\rho$ on $[0,4\pi]^2$ with an artificial
  circular interface, $t=3$: $9.57\times10^{-6}$ at $80^2$ to
  $1.24\times10^{-8}$ at $320^2$ (order 5.06; Table 4).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.3–3.4 use the
  same data with the factors printed as $2\sqrt3$ and $\sqrt6$, which
  equal $2\sqrt\gamma$ and $\sqrt{2\gamma}$ only for $\gamma=3$, a value they
  do not state *(compiler inference)*; exact solution taken from their
  earlier paper; $t=3$. M5-I reaches $1.69\times10^{-12}$ at 320 cells
  (order 6.03) and $4.67\times10^{-11}$ at $320^2$ (6.49), M5-NI again
  about fifth order (Tables 3.3–3.4).

The breaking time of $1+0.2\sin x$ is $1/0.2=5$ *(compiler check, not
in the sources)*, matching Zheng et al.'s statement.

## Qualifications

- Li, Shu & Qiu caption the Burgers figures "density" and call the
  unknown $\mu$, the letter of the velocity in their Euler examples.
- Their M5-I orders 8.85 and 8.72 at 40 and 80 cells (Table 3.1)
  exceed the design order six and are not commented on.
- Puppo et al.'s Table 1 prints a rate on the first row of each
  sub-table, against a coarser grid that is not listed; their Fig. 7
  caption gives $t=5$ for a test that ends at $t=0.5$.
- The accuracy tests of Zheng et al. use $\Delta t=O(\Delta x^{5/3})$;
  the other sources' accuracy runs state CFL 0.6 with a reduced time
  step (Li, Shu & Qiu) or prescribed multiples of $h$ (Puppo et al.).

# Citations

- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.1–3.4, Tables 3.1–3.4, Figs. 3.1–3.2 (arXiv v1).
- [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) — §4.1, §4.3, Table 1, Figs. 1, 4–9 (arXiv v2).
- [Pazner (2021)](/sources/pazner-2021.md) — §5.5, Fig. 11 (arXiv v1).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.11 (arXiv v1).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §4, Ex. 1 and Ex. 8, Tables 2 and 4.
