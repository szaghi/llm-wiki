---
type: Benchmark
title: "Broadwell model"
description: "Three-velocity discrete kinetic model whose stiff collision term relaxes to a local Maxwellian with relaxation time ε; used nonlinear and linearized to test positivity, asymptotic preservation and uniform accuracy of IMEX time integrators from the kinetic to the fluid regime."
status: established
aliases: [Broadwell system, linearized Broadwell model, Broadwell discrete-velocity model]
tags: [kinetic, asymptotic-preserving, imex, stiff, verification]
timestamp: 2026-10-19T23:00:00Z
---

# Broadwell model

The **Broadwell model** is a discrete-velocity kinetic equation with three densities
$f_+$, $f_0$, $f_-$ moving with velocities $+1$, $0$, $-1$ and colliding with relaxation
time $\varepsilon$ (page-local symbols):

$$\partial_tf_\pm\pm\partial_xf_\pm=-\frac1\varepsilon\big(f_+f_--f_0^2\big),\qquad \partial_tf_0=\frac1\varepsilon\big(f_+f_--f_0^2\big)$$

([Ma et al. (2026)](/sources/ma-2026.md), §4.2;
[Gottlieb et al. (2022)](/sources/gottlieb-2022.md), Eqs. (36)–(40)). In the moments
$\rho=f_++2f_0+f_-$, $m=f_+-f_-$, $z=f_++f_-$ (page-local) it reads

$$\partial_t\rho+\partial_xm=0,\qquad \partial_tm+\partial_xz=0,\qquad \partial_tz+\partial_xm=\frac1{2\varepsilon}\big(\rho^2+m^2-2\rho z\big),$$

so $\rho$ and $m$ are conserved and $z$ relaxes to the Maxwellian value
$z=\frac{\rho^2+m^2}{2\rho}$; the limit $\varepsilon\to0$ is a $2\times2$ system of
conservation laws for $(\rho,m)$. It is the simplest nonlinear kinetic model with a fluid
limit, between the [hyperbolic relaxation system](/benchmarks/hyperbolic-relaxation-system.md)
and the BGK equation.

## Structure used by time integrators

Gottlieb et al. (2022, §3.4.1, Eq. (40)) note that the collision term $Q$ satisfies
$Q'(y)Q(y)=-\rho\,Q(y)$, i.e. their structural property 5 with constant $C=\rho$, with
conserved quantities $(\rho,m)$ and equilibrium map onto the Maxwellian. Under that
property their IMEX [multiderivative](/methods/multiderivative-runge-kutta.md) schemes
preserve positivity for $h\le r\,h_{\mathrm{FE}}$ independently of $\varepsilon$ and are
[asymptotic preserving](/definitions/asymptotic-preserving-scheme.md) (Prop. 1); with
first-order upwind transport the discrete kinetic entropy decreases (Remark 3, Eqs.
(53)–(56); see [entropy stability](/properties/entropy-stability.md)).

Linearized about $\rho^\star=2$, $m^\star=0$, $z^\star=1$, the system becomes
$U_t+\mathcal AU_x=\frac1\varepsilon\mathcal QU$ with
$\mathcal A=\begin{pmatrix}0&1&0\\0&0&1\\0&1&0\end{pmatrix}$,
$\mathcal Q=\begin{pmatrix}0&0&0\\0&0&0\\1&0&-2\end{pmatrix}$ (page-local), which satisfies
Yong's structural stability condition (Ma et al. 2026, §4.2).

## Set-ups and results

**Nonlinear, IMEX multiderivative** (Gottlieb et al. 2022, §3.5.2, Figs. 4–5). $x\in[0,2]$
periodic, non-equilibrium data $f_+=1+0.2\exp(0.3\sin\pi x)$, $f_-=\exp(0.2\cos2\pi x)$,
$f_0=1/(1+0.3\sin\pi x)$; WENO5 finite volumes with $h=\frac12\Delta x$, final time 0.1,
$L^2$ error against a refined mesh, no positivity limiter. The behaviour is like that of
their stiff ODE model: design order in the kinetic and fluid regimes and
[order reduction](/definitions/order-reduction.md) in between.

**Linearized, IMEX-BDF** (Ma et al. 2026, §4.2, Table 4.2). $x\in[-\pi,\pi]$ periodic,
$\rho=1+0.3\sin2x$, $m=\rho(\frac12+0.1\cos2x)$, and $z=\frac12\rho$ ($q=2$),
$\frac12\rho-\frac\varepsilon4\partial_xm$ ($q=3$),
$\frac12\rho-\frac\varepsilon4\partial_xm-\frac{\varepsilon^2}{16}\partial_{xx}\rho$
($q=4$), i.e. data prepared to the order of the scheme; Fourier–Galerkin with $N=100$,
final time 2, $h=5\times10^{-3}$ down to $6.25\times10^{-4}$, starting values from
ARS(4,4,3) at step $h/500$. The $q$-step IMEX-BDF methods show orders 2, 3 and 4 for every
$\varepsilon\in[10^{-7},1]$, the evidence for
[uniform accuracy](/results/uniform-accuracy-relaxation-systems.md).

## Qualifications

- The two set-ups are not comparable: Gottlieb et al. integrate the nonlinear model from
  non-equilibrium data with a finite-volume WENO discretization; Ma et al. integrate the
  linearization from prepared data spectrally. The order reduction of the first and its
  absence in the second are consistent with the data preparation required by the
  uniform-accuracy theorems.
- Ma et al. print the second-order errors at $h=2.5\times10^{-3}$ with exponent $10^{-5}$
  where the neighbouring entries and the printed orders require $10^{-4}$ (Table 4.2;
  arXiv v1).

# Citations

- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §3.4.1 (Eqs. (36)–(40)), Prop. 1, Remark 3 (Eqs. (53)–(56)), §3.5.2 (Figs. 4–5).
- [Ma et al. (2026)](/sources/ma-2026.md) — §4.2 (Table 4.2); arXiv v1.
