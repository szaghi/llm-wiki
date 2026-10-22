---
type: Method
title: "Shock-capturing boundary closure for multi-block finite differences"
description: "Qin, Chen, Lin and Deng close a fifth-order staggered WCNS at block boundaries with nonlinear multi-resolution interpolation on one-sided nested stencils built on 'conservative solution points', so that the multi-block scheme is globally conservative, fifth order and shock-capturing up to the boundary, and slow shocks cross block interfaces."
status: established
aliases: [shock-capturing boundary closure, nonlinear boundary closure, conservative boundary closure, WCNS-MR boundary closure, conservative solution points, semi-uniform grid]
tags: [finite-difference, compact-scheme, weno, reconstruction, limiting]
timestamp: 2026-10-23T16:00:00Z
---

# Shock-capturing boundary closure for multi-block finite differences

A high-order finite-difference stencil is truncated at a domain boundary and at the interface between
two blocks of a multi-block grid. Qin, Chen, Lin & Deng (2023, §1) list what a non-conservative interface
interpolation produces when a discontinuity is near or crosses the interface: spurious oscillations,
phase lag, wrong jumps, stagnation of slow shocks, instability and, for overlapping grids, convergence to
a false solution. Their **shock-capturing boundary closure** applies the nonlinear interior interpolation
of a [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md) on one-sided
nested stencils near the boundary, on a grid whose near-boundary solution points are moved so that the
whole scheme is globally conservative. The authors state that no earlier high-order finite-difference
method had both properties (§1).

## Globally conservative staggered grid

On $[a,b]$ with flux points $x_{i+1/2}=a+i\Delta x$, $i=0,\dots,N$, the solution points are the
midpoints $a+(i-\tfrac12)\Delta x$ except the first two and last two, replaced by the **conservative
solution points** of Deng & Chen (2018), as Qin et al. print them (§2, Eq. (2)):

$$x_{1,2}=a+\frac{12204\mp\sqrt{53326826}}{13420}\,\Delta x,\qquad x_{N-1}=a+b-x_2,\quad x_N=a+b-x_1 .$$

A step of the scheme has the three WCNS steps: interpolation of $u^\mp_{i+1/2}$ from the solution
values, a numerical flux at the flux points (Roe with characteristic interpolation for Euler, global
Lax–Friedrichs splitting otherwise; [Roe solver](/methods/roe-riemann-solver.md),
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md)), and a difference of the interface fluxes only,

$$\partial_xf\big|_i\approx\frac1{\Delta x}\sum_kc_{i,k}\,\hat f_{\cdot},$$

on five interface fluxes for $i=1,2,N-1,N$ and six, $\hat f_{i-5/2},\dots,\hat f_{i+5/2}$, in the interior
(Eq. (3); page-local coefficients $c_{i,k}$, the source's $\theta_{j,k}$, Table 1). The interior row is
$(-\tfrac3{640},\tfrac{25}{384},-\tfrac{75}{64},\tfrac{75}{64},-\tfrac{25}{384},\tfrac3{640})$, sixth order;
the boundary rows are fourth order and printed to 16 digits. With these, the scheme satisfies the
discrete identity

$$\sum_{i=1}^N\mathsf q_i\,\partial_xf\big|_i\,\Delta x=\hat f_{N+1/2}-\hat f_{1/2},\qquad
\mathsf q_i=1\ (3\le i\le N-2),\quad \mathsf q_{1,N}=1-\tfrac{11237\sqrt{53326826}}{639921912},\quad \mathsf q_{2,N-1}=1+\tfrac{11237\sqrt{53326826}}{639921912}$$

(page-local quadrature weights $\mathsf q_i$; Eqs. (4)–(5), "proved" in Deng & Chen 2018, which is not
ingested). *(Compiler check, not in the sources: $x_1-a=0.365237\Delta x$, $x_2-a=1.453541\Delta x$,
$\mathsf q_1=0.871768$, $\mathsf q_1+\mathsf q_2=2$; the interior row is exact on polynomials up to
degree 6 at the staggered offsets $\pm\tfrac12,\pm\tfrac32,\pm\tfrac52$.)* By Gustafsson's theorem, which Qin et al. cite
(§2), fourth-order closures keep global fifth order with a fifth-order interior, so it suffices that the
interpolation is fifth order everywhere. On the conformal multi-block grid the interface flux point is
shared by the two blocks; the boundary value $u_{1/2}$ comes from the boundary condition or from the
interpolation in the neighbouring block (§2.2). Qin et al. contrast the approach with SBP-SAT closures,
the established route to time-stable globally conservative closures
([summation-by-parts operators](/operators/summation-by-parts-operator.md)), and with Berger's flux
balancing, "seldom implemented due to its complexity" (§1).

## Interior interpolation: WCNS-MR with scaled indicators

The interior scheme is a fifth-order **multi-resolution WCNS** after Zhang, Wang & Zhang (§2.1,
Eqs. (6)–(22); [multi-resolution WENO](/methods/multi-resolution-weno.md)). On the nested stencils
$T_1=\{x_i\}$, $T_2=\{x_{i-1},x_i,x_{i+1}\}$, $T_3=\{x_{i-2},\dots,x_{i+2}\}$ (page-local, as on the
multi-resolution page) the Lagrange interpolants give at $x_{i+1/2}$

$$u^{(1)}=u_i,\quad u^{(2)}=-\tfrac18u_{i-1}+\tfrac34u_i+\tfrac38u_{i+1},\quad
u^{(3)}=\tfrac3{128}u_{i-2}-\tfrac5{32}u_{i-1}+\tfrac{45}{64}u_i+\tfrac{15}{32}u_{i+1}-\tfrac5{128}u_{i+2},$$

combined by the simplified rule of Wang et al. (2021),
$u^-_{i+1/2}=\omega_1u^{(1)}+\omega_2u^{(2)}+\omega_3\big(\tfrac1{d_3}u^{(3)}-\sum_{m\le2}\tfrac{d_m}{d_3}u^{(m)}\big)$,
with $d=(1,10,100)/111$, $\alpha_m=d_m\big(1+\tau/(\beta_m+\epsilon)\big)$, $\epsilon=10^{-10}$ and
$\tau=\big(\tfrac12(|\beta_3-\beta_2|+|\beta_3-\beta_1|)\big)^2$ (Eqs. (10)–(12)). The indicators are
derivative sums at the solution point with a new **scaling parameter** $\lambda_{\mathrm s}>0$
(page-local),

$$\beta_2=\sum_{n=1}^2\big(\lambda_{\mathrm s}^{n-1}\Delta x^n\partial_x^nP_2(x_i)\big)^2,\qquad
\beta_3=\sum_{n=1}^4\big(\lambda_{\mathrm s}^{n-1}\Delta x^n\partial_x^nP_3(x_i)\big)^2,\qquad
\beta_1=\min(\delta_0^2,\delta_1^2),$$

with $P_m$ the interpolant on $T_m$ and $\delta_0$, $\delta_1$ the one-sided divided differences times
$\Delta x$, which accommodate non-uniform points (Eqs. (13)–(22);
[smoothness indicators](/definitions/smoothness-indicator.md)). $\lambda_{\mathrm s}=1$ is the unscaled form,
"slightly" different from Zhang et al.'s; $\lambda_{\mathrm s}=2$ is adopted, which multiplies the squared
$n$th-derivative terms by $1,4,16,64$. The choice is empirical; no analysis is given.

## The closures

For the flux points next to the boundary the same formulas are applied on one-sided nested stencils
(§2.2, Fig. 2):

| point | $T_1$ | $T_2$ | $T_3$ |
|---|---|---|---|
| $i=1$ | $\{u_1\}$ | $\{u_{1/2},u_1,u_2\}$ | $\{u_{1/2},u_1,\dots,u_4\}$ |
| $i=2$ | $\{u_2\}$ | $\{u_1,u_2,u_3\}$ | $\{u_{1/2},u_1,\dots,u_4\}$ |
| $i=N-1$ | $\{u_{N-1}\}$ | $\{u_{N-2},u_{N-1},u_N\}$ | $\{u_{N-4},\dots,u_N\}$ |
| $i=N$ | $\{u_N\}$ | $\{u_{N-2},u_{N-1},u_N\}$ | $\{u_{N-4},\dots,u_N\}$ |

At the left boundary the boundary value $u_{1/2}$ is a stencil node; at $i=N$ the left state at
$x_{N+1/2}$ is extrapolated. Only the interpolation and derivative coefficients change, printed to
17 digits for $i=1,2,N-1,N$ (Tables 6–9) and for the interior points $i=3,4,N-3,N-2$ whose stencils
contain conservative points (Tables 2–5); the interior pattern is uniform for $5\le i\le N-4$. The
extrapolating closure at $i=N$ has coefficients up to about 2.03 in magnitude (Table 7). Time stepping is
SSP-RK3 at CFL 0.4 with stage boundary data after Tan & Shu (Eqs. (23)–(24);
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## Evidence (Qin et al. 2023, §3)

- **Accuracy.** Fifth order with closures active: linear advection with inflow
  $u(0,t)=-0.1\sin\pi t$, $L_2$ from $6.92\times10^{-6}$ ($N=20$) to $6.40\times10^{-12}$ ($N=320$), order
  5.01, identical for $\lambda_{\mathrm s}=1$ and 2 (Table 10); Burgers at $t=0.3$, $L_2$ order 5.16 and
  $L_\infty$ 4.97 at $N=640$, $\lambda_{\mathrm s}=2$ less accurate on coarse grids ($6.92\times10^{-5}$
  against $4.37\times10^{-5}$ at $N=40$; Table 11); 1-D Euler density wave, order 5.01 at $N=320$
  (Table 12).
- **Shocks through boundaries and interfaces.** A Burgers shock crosses a periodic boundary handled by the
  closures ($N=200$, $t=4,7.9,8.1$; [Burgers tests](/benchmarks/burgers-equation-tests.md)); a slow Burgers
  shock (speed 0.01) crosses an interface with a 2:1 spacing jump with "invisible oscillation and phase
  lag" (Fig. 4); [Buckley–Leverett](/benchmarks/buckley-leverett-problem.md) on two blocks converges to the
  reference (Fig. 5); Sod and Lax shocks cross an interface at $x=0.75$ (160 points on $[0,0.75]$, 40 on $(0.75,1]$) at the correct location
  ([Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)); the
  [Shu–Osher problem](/benchmarks/shu-osher-problem.md) on two blocks is smooth across the interface with
  $\lambda_{\mathrm s}=2$, while with $\lambda_{\mathrm s}=1$ "the shock fails to cross the interface" (stated,
  no figure); a 2-D slow shock (speed 0.015) crosses between two $40\times40$ blocks (Fig. 10).
- **The role of $\lambda_{\mathrm s}$.** On the single-domain Lax problem, $\lambda_{\mathrm s}=1$ is more
  oscillatory than characteristic-wise WENO-JS and WENO-MR, which the authors attribute to the wide
  difference stencil of WCNS; $\lambda_{\mathrm s}=2$ removes the oscillations (Fig. 6).
- **Multi-dimensional.** A [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) on four
  blocks of different spacings (contours not exactly symmetric because the spacings differ); Mach 1.4 flow
  over a 4 % bump on three blocks, which avoids the metric singularities of a single block; a transonic
  NACA0012 ($M=0.8$, $1.25^\circ$) with interfaces deliberately cutting both shocks, $C_p$ equal to the
  single-domain result (Figs. 11–17).
- **Cost.** Two zones against one at $N=10^4$: Lax 284.55 s against 283.38 s, Sod 191.42 s against
  189.09 s, Shu–Osher 375.44 s against 376.14 s (serial, AMD Ryzen7-5800H; Table 13).

## Qualifications

- No stability analysis of the nonlinear closures is given, in contrast with SBP-SAT time stability;
  stability is shown numerically. The global conservation identity is recalled from Deng & Chen (2018),
  not re-proved.
- Qin et al. print the 2-D slow-shock data as $(\rho,v_1,v_2,E)=(1.4,0,4.2,8.8)$ and
  $(5.38064,0,4.25971,27.2576)$ (Eq. (40)). *(Compiler check, not in the sources: read as velocities the
  first state has $p=-1.42$; read as $(\rho,\rho v_1,\rho v_2,E)$ it has $v_2=3$, $p=1$, the second
  $v_2=0.79167$, $p=10.2286$, and the mass and energy jump conditions give speeds 0.01500 and 0.014997,
  the stated 0.015.)* They also call $E=p/(\gamma-1)+\tfrac12\rho|v|^2$ the total energy "per unit mass"
  (§3.4–3.5).
- Table 10 prints identical errors for $\lambda_{\mathrm s}=1$ and 2 in every entry, while Tables 11–12 differ
  on coarse grids.
- The method is shown at fifth order only; the authors state that it applies to other orders (§4).

# Citations

- [Qin, Chen, Lin & Deng (2023)](/sources/qin-2023.md) — §1; §2, Eqs. (1)–(5), Table 1; §2.1, Eqs. (6)–(22), Tables 2–5, Fig. 1; §2.2, Tables 6–9, Fig. 2; Eqs. (23)–(24); §3, Tables 10–13, Figs. 3–17; §4.
