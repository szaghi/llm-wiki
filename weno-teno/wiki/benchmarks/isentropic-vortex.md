---
type: Benchmark
title: "Isentropic vortex"
description: "Smooth exact solution of the two-dimensional Euler equations, an isentropic vortex advected by a uniform stream on a periodic box; used for design-order convergence studies and, with an amplified vortex strength, as a stress test of entropy-conservative flux implementations."
status: established
aliases: [isentropic vortex advection, isentropic vortex evolution, vortex convection]
tags: [benchmark, weno, dg, entropy-stable]
timestamp: 2026-10-21T12:00:00Z
---

# Isentropic vortex

The isentropic vortex is a smooth, exact, time-dependent solution of the
compressible Euler equations: a vortex with Gaussian-type velocity and
temperature perturbations, at constant specific entropy $s$, superposed
on a uniform stream $(v_1,v_2)=(1,1)$ on a periodic square. Since the
exact solution is the initial data translated along the diagonal, the
error after any number of periods is measurable; Wang et al. and
Balsara et al. use it as their two-dimensional order-of-accuracy check
for the Euler equations, and Ranocha et al. call it "a widely used
benchmark problem" with an analytical solution.

## Setup

Let $T=p/\rho$ be the temperature, $\mathcal E$ the vortex strength
and $r$ the distance from the vortex centre (page-local symbols). The
form printed by [Wang et al. (2023)](/sources/wang-2023-b.md) Example 3
and, in three dimensions, by
[Ranocha et al. (2023)](/sources/ranocha-2023.md) §4.1, Eq. (4.1) is,
in two dimensions,

$$
\begin{aligned}
T&=T_0-\frac{(\gamma-1)\mathcal E^2}{8\gamma\pi^2}\,e^{\,1-r^2},\qquad
\rho=\rho_0\Big(\frac{T}{T_0}\Big)^{1/(\gamma-1)},\qquad p=\rho T,\\
(v_1,v_2)&=(1,1)+\frac{\mathcal E}{2\pi}\,e^{(1-r^2)/2}\,(-\bar y,\ \bar x),
\end{aligned}
$$

with $(\bar x,\bar y)$ the position relative to the centre and
$\gamma=1.4$. The sources differ in normalization and strength:

| Source | Domain | $\mathcal E$ | Background | Final time / use |
|---|---|---|---|---|
| [Wang et al. (2023)](/sources/wang-2023-b.md) Example 3 | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=T_0=1$ | $t=1$; $L^2$ error of $\rho$ on $\Delta x=1/2,\dots,1/64$ |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §VII.a | square periodic box; $[-10,10]^2$ and doubled time for orders 7 and 9 | not restated | not restated | design order, $64^2$ to $512^2$ |
| [Ranocha et al. (2023)](/sources/ranocha-2023.md) §4.1 | $[-5,5]^d$, $d=2,3$, periodic | 20 | $\rho_0=1$, $p_0=10$, $v_0=(1,1,0)$ | timing only, 8 elements per direction |

Wang et al. print $\rho=\big(1-\frac{25(\gamma-1)}{8\gamma\pi^2}e^{1-r^2}\big)^{1/(\gamma-1)}$,
which is the table's form with $\mathcal E=5$, $T_0=1$. Balsara et al.
take the setup of Pao & Salas as described in Balsara & Shu, without
restating its parameters. Wang et al. take theirs from three earlier
papers, Ranocha et al. cite Shu.

## Uses in the sources

**Design-order verification.** Balsara et al. use it to show that
their [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md)
reaches design order for conservation laws with
[WENO-AO](/methods/weno-ao.md) and multi-resolution WENO weights of
orders 3, 5, 7 and 9, LLF flux, CFL 0.3. Density $L_1$ rates at the
finest grid: WENO-AO-3 2.59 ($512^2$), AO-(5,3) 4.97, AO-(7,3) 6.93
($L_1$ error $5.18406\times10^{-10}$ at $512^2$), AO-(9,3) 8.78
($1.01355\times10^{-10}$ at $384^2$); multi-resolution WENO 2.74, 4.68,
6.93, 8.78 (Table I). The domain and the final time are doubled for
orders 7 and 9.

**Fifth-order A-WENO with the time-step tied to the grid.** Wang et
al. run their [A-WENO](/methods/alternative-weno.md) schemes with the
adaptive-diffusion central-upwind flux (NEW) and the earlier central flux
(OLD) with CFL number $\Delta x^{2/3}$. Then $\Delta t\propto\Delta x^{5/3}$
and the third-order SSP-RK error scales like $\Delta x^5$, the spatial
design order *(compiler check, not in the sources)*. Both reach fifth
order, with irregular rates: OLD 3.27, 2.39, 6.38, 4.99, 6.20; NEW
3.24, 2.36, 6.37, 4.98, 6.22. The $L^2$ density errors at
$\Delta x=1/64$ are $3.45\times10^{-9}$ (OLD) and $3.62\times10^{-9}$
(NEW); the NEW errors are slightly larger on every grid (Table 1).

**Implementation stress test.** Ranocha et al. raise the strength to
$\mathcal E=20$ "to make sure that all possible paths in the logarithmic
mean are followed" in the [entropy-conservative fluxes](/methods/entropy-conservative-flux.md)
of [flux-differencing DG](/methods/flux-differencing.md). They report
no errors: the vortex is used to time
[Trixi.jl](/software/trixi-jl.md) against [FLUXO](/software/fluxo.md)
(Trixi.jl: 50 steps of a 9-stage fourth-order RK with error-based step
control; FLUXO: 90 steps of a 5-stage fourth-order RK; the same number
of right-hand-side evaluations) and in single-element microbenchmarks.
Precomputing $\ln\rho$ and $\ln p$ speeds the volume terms up by about
10 % on this vortex, against 25–55 % on sinusoidal and 60–75 % on random
data, because near-constant states take the Taylor branch of the
logarithmic mean (§7.2, Fig. 6).

## Qualifications

- Wang et al. print "$r=(x-5)^2+(y-5)^2$" while the formulas use
  $e^{1-r^2}$; the formulas are consistent only with
  $r^2=(x-5)^2+(y-5)^2$, i.e. with $r$ the distance from the centre as
  Ranocha et al. define it.
- The irregular rate sequence of Wang et al. (2.36–2.39 on the third
  refinement) is printed without comment.
- Ranocha et al. report timings only; their strengthened vortex
  carries no accuracy result.

# Citations

- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 3, Table 1.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VII.a, Table I.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §4.1, Eq. (4.1); §7.2, Fig. 6 (arXiv v2).
