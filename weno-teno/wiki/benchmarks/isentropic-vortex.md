---
type: Benchmark
title: "Isentropic vortex"
description: "Smooth exact solution of the Euler equations, an isentropic vortex advected by a uniform stream (or held steady) on a periodic box; used for design-order convergence studies, which expose the time-step scaling and multidimensional quadrature high orders need, and, with an amplified vortex strength, as a stress test of entropy-conservative fluxes."
status: established
aliases: [isentropic vortex advection, isentropic vortex evolution, vortex convection, steady isentropic vortex]
tags: [benchmark, weno, dg, entropy-stable, finite-volume]
timestamp: 2026-10-22T12:00:00Z
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
benchmark problem" with an analytical solution. Without the stream the
vortex is steady, and the error is the deviation from the initial data
([Bryngelson et al. (2021)](/sources/bryngelson-2021.md)); a rotated
copy gives a three-dimensional test
([Li, Duan & Tang (2022)](/sources/li-2022-c.md)).

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
| [Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.1 | $[-10,10]^2$, centre $(-2,-2)$, periodic | 5 | $\rho_0=1$, temperature 1 with $c_v=1$, stream $(1,1)$ | $t=4$; $\ell^1$, $\ell^\infty$ errors of $\rho$, $N_x=40$ to $320$, moving mesh |
| Li, Duan & Tang (2022) Ex. 5.5 | $[-10,10]^3$, 2D vortex rotated onto the domain diagonal | 5 | as Ex. 5.1 | $t=0.1$; $N_x=40$ to $320$ |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.1 | $[-10,10]^2$ (enlarged from $[-5,5]^2$), periodic | amplitude not printed | $\rho_0=1$, $p_0=1/\gamma$, stream of Mach $\sqrt{2/\gamma}$ at $45°$ | one cycle; $100^2$ to $500^2$, CFL 0.6 down to 0.00625 |
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §5.4 | steady vortex, no stream; setup deferred to an earlier MFC paper | not printed | not printed | $\lVert\rho(1)-\rho(0)\rVert_\infty$, $1/N\in[10^{-3},10^{-1}]$ |

Wang et al. print $\rho=\big(1-\frac{25(\gamma-1)}{8\gamma\pi^2}e^{1-r^2}\big)^{1/(\gamma-1)}$,
which is the table's form with $\mathcal E=5$, $T_0=1$. Balsara et al.
take the setup of Pao & Salas as described in Balsara & Shu, without
restating its parameters. Wang et al. take theirs from three earlier
papers, Ranocha et al. cite Shu.

The other normalizations reduce to the same vortex *(compiler check, not
in the sources)*. Li et al. write $p=(\gamma-1)\rho T$ with $c_v=1$, so
their temperature perturbation $-\mathcal E^2e^{1-r^2}/(8\gamma\pi^2)$
is the table's $T$-perturbation divided by $\gamma-1$; their velocity
perturbation turns the other way, $\propto(\bar y,-\bar x)$.
Sciacovelli et al. write the perturbations through a Gaussian
$\Omega=A_\Omega e^{-r^2/2}$ with an amplitude $A_\Omega$ they do not print (page-local symbols), $\delta v=\Omega(-\bar y,\bar x)$,
$\rho=(1-\tfrac{\gamma-1}2\Omega^2)^{1/(\gamma-1)}$ and
$p=\rho^\gamma/\gamma$; this is the table's form with
$\mathcal E=2\pi A_\Omega e^{-1/2}$ and $T_0=1/\gamma$, i.e. unit background
sound speed. Sciacovelli et al. enlarge the domain to $[-10,10]^2$ "to
reduce artificial shear layers at boundaries", and Li et al. and
Balsara et al. (orders 7 and 9) use the same box.

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

**Ninth order and the time-integration error.** Sciacovelli et al. run
a ninth-order central-difference scheme with Jameson-type adaptive
[artificial dissipation](/methods/artificial-viscosity.md) and the
third-order TVD Runge–Kutta method of Gottlieb & Shu. At constant CFL
the observed order wanders between 3 and 9: a ninth-order range appears
only for CFL $\le0.2$, and ninth order holds over the whole range
$100^2$–$500^2$ only at CFL $1.25\times10^{-2}$ and
$6.25\times10^{-3}$ (§4.1, Fig. 2). They explain the behaviour by the
error balance: keeping the ratio of temporal to spatial error fixed
needs $\Delta t\propto\Delta x^{9/3}=\Delta x^3$, whereas a constant CFL
gives $\Delta t\propto\Delta x$ (Eq. 40). The same balance is what
Wang et al.'s CFL $\Delta x^{2/3}$ and Li et al.'s
$\Delta t=C_{\mathrm{CFL}}(\min\Delta\xi_k)^{5/3}$ (Li et al., §5) realize
for fifth order with a third-order integrator: across the sources, a
convergence study above third order with SSP-RK3 is only meaningful
with a refined time step or a small CFL. See
[SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md).

**Moving meshes and entropy.** Li et al. advect the vortex on an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) (monitor built
from $\lvert\nabla\rho\rvert$ and $\lvert\Delta\rho\rvert$) with
entropy-stable fluxes whose dissipation uses
[multi-resolution WENO](/methods/multi-resolution-weno.md) and reach
fifth order in $\ell^1$ and $\ell^\infty$ at $t=4$ (Ex. 5.1, Fig. 5.2),
and the expected fifth order in three dimensions at $t=0.1$ (Ex. 5.5,
Fig. 5.6). The same runs check [entropy stability](/properties/entropy-stability.md):
the total entropy stays almost constant with the
[entropy-conservative flux](/methods/entropy-conservative-flux.md) and
decays with the entropy-stable one, to about $-4.2\times10^{-6}$ at
$t=4$ on $160^2$ in 2D and to about $-1\times10^{-7}$ by $t=0.1$ in 3D.

**Multidimensional finite-volume quadrature.** Bryngelson et al. use
the steady vortex to verify the finite-volume WENO5 scheme of
[MFC](/software/mfc.md): the $L^\infty$ density error converges at
second order when face fluxes are evaluated at face midpoints and at
fifth order with a $2\times2$ Gauss rule on each face, so "the
4th-order-accurate cell averaging we employ is required to achieve
5th-order accuracy associated with the WENO reconstructions" in
multiple dimensions (§5.4, Fig. 5a).

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
- Bryngelson et al. call the $2\times2$ Gauss rule fourth-order accurate
  and observe fifth order. A face-average error of order
  $\Delta x^4$ bounds the formal order of the scheme at four *(compiler
  check, not in the sources)*; the paper does not comment on the
  observed slope of five. They also print the Gauss points as
  $y_j+(2l+1)\Delta y_j/(2\sqrt3)$, $l=1,2$, which lie outside the face;
  the two-point Gauss points are $y_j\pm\Delta y_j/(2\sqrt3)$.
- Bryngelson et al.'s vortex is steady, so it tests the spatial operator
  without transport across the grid; it is not the advected benchmark
  of the other sources.
- Sciacovelli et al. do not print the amplitude $A_\Omega$, so their
  error levels cannot be reproduced from the paper; their scheme is a
  central scheme with artificial dissipation, not a WENO scheme.

# Citations

- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 3, Table 1.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VII.a, Table I.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §4.1, Eq. (4.1); §7.2, Fig. 6 (arXiv v2).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §5, Eq. (5.1), Ex. 5.1, Fig. 5.2; Ex. 5.5, Fig. 5.6 (arXiv v1).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §4.1, Eqs. (37)–(40), Fig. 2 (arXiv v1).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.1, Eqs. (29)–(30); §5.4, Fig. 5a (arXiv v1).
