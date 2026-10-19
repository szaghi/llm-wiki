---
type: Benchmark
title: "Linear hyperbolic relaxation system"
description: "Hyperbolic systems with a stiff relaxation source of strength 1/ε, linear or Jin–Xin type, whose ε → 0 limit is a scalar conservation law; the standard test of IMEX, asymptotic-preserving and uniformly accurate time integrators across the kinetic, intermediate and equilibrium regimes."
status: established
aliases: [hyperbolic relaxation system, Jin–Xin relaxation system, linear relaxation system, stiff relaxation system, Chen–Levermore–Liu relaxation system]
tags: [asymptotic-preserving, imex, stiff, verification, kinetic]
timestamp: 2026-10-19T23:00:00Z
---

# Linear hyperbolic relaxation system

A **hyperbolic relaxation system** couples a conservation law to a relaxing variable
that is driven, on the time scale $\varepsilon$, to a local equilibrium. Its method-of-lines
form is the model problem $y'=f^{\mathrm E}(y)+\frac1\varepsilon Q(y)$ of the
[asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) literature, with the
convection nonstiff and the relaxation stiff, and it is the standard test of
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) and
[IMEX multistep](/methods/imex-linear-multistep-methods.md) schemes across the regimes
$\varepsilon=O(1)$, $\varepsilon\sim h$ and $\varepsilon\to0$
([Jin (2022)](/sources/jin-2022.md), §6.1;
[Gottlieb et al. (2022)](/sources/gottlieb-2022.md), §3.4.1;
[Hu & Shu (2025)](/sources/hu-2025.md); [Ma et al. (2026)](/sources/ma-2026.md)).

## Forms in the sources

Page-local symbols: $u$ the conserved variable, $v$ its flux variable, $F$ the
equilibrium flux, $x$ the space variable, and $\kappa$ the equilibrium slope of the
linear case (Hu & Shu write $b$).

**Jin–Xin type, nonlinear** (Gottlieb et al. 2022, Eqs. (33)–(35)):

$$\partial_tu+\partial_xv=0,\qquad \partial_tv+\partial_xu=\frac1\varepsilon\big(F(u)-v\big),$$

with limit $\partial_tu+\partial_xF(u)=0$. The relaxation term $Q=F(u)-v$ satisfies
$Q'(y)Q(y)=-Q(y)$, the structural property behind Gottlieb et al.'s positivity and AP
result (property 5 with constant 1); the system is used there only as an example, without
numerics. Hu & Shu (2025, App. 7.3, Eq. (7.1)) use the same form, with $\lvert F'\rvert<1$,
for their formal AP theorem.

**Linear, Chen–Levermore–Liu** (Hu & Shu 2025, Eqs. (1.1)–(1.3), (2.1)):

$$\partial_tu+\partial_xv=0,\qquad \partial_tv+\partial_xu=\frac1\varepsilon(\kappa u-v),\qquad\lvert\kappa\rvert<1.$$

The formal limit is $\partial_tu+\kappa\,\partial_xu=0$, and with the first correction
$\partial_tu+\kappa\,\partial_xu=\varepsilon(1-\kappa^2)\partial_{xx}u$. The condition
$\lvert\kappa\rvert<1$ is the subcharacteristic condition, which makes the correction
diffusive. With $w=v-\kappa u$ the system becomes
$\partial_tu+\partial_x(\kappa u+w)=0$, $\partial_tw+\partial_x((1-\kappa^2)u-\kappa w)=-\frac1\varepsilon w$,
with equilibrium $w=0$. Jin (2022, §6.1, Eqs. (6.1)–(6.2)) recalls the general form with a
dissipative relaxation term and the Chapman–Enskog limit, parabolic exactly when the
subcharacteristic condition holds (Chen, Levermore & Liu 1994, as recalled).

**General linear class** (Ma et al. 2026, §1–§2.1): $U_t+\mathcal AU_x=\frac1\varepsilon\mathcal QU$
with constant matrices (page-local $\mathcal A$, $\mathcal Q$), under Yong's structural
stability condition (relaxation matrix similar to $\mathrm{diag}(0,\hat S)$, $\hat S$
invertible; a symmetrizer; a dissipative coupling). It covers the Jin–Xin system, the
linearized [Broadwell model](/benchmarks/broadwell-model.md), the linearized
Aw–Rascle–Zhang traffic model and linearized Grad moment systems (§4). After the initial
layer, of length $O(\varepsilon\log(1/\varepsilon))$ per time derivative, the relaxing
components are $O(\varepsilon)$ and all derivatives are bounded uniformly in $\varepsilon$
(Thm. 3.2).

## What it tests and results

- **Uniform order across regimes.** On the linear system with $\kappa=0.6$, Fourier–Galerkin
  with $N=40$ modes, $x\in[0,2\pi]$ periodic, equilibrium data $u=e^{\sin x}$,
  $v=\kappa e^{\sin x}$ evolved exactly to $t=1$, steps $h=\frac8{N^2}2^{-k}$, $k=1,\dots,5$,
  final time 2 and $\varepsilon$ from 1 to $10^{-7}$: ARS(2,2,2) is uniformly second order,
  BHR(5,5,3)* uniformly third order, and ARS(4,4,3) third order at both ends but only
  uniformly second order, with an error peak near $\varepsilon\approx10^{-4}$–$10^{-3}$
  (Hu & Shu 2025, §6, Fig. 1). The theorems behind these rates are on
  [uniform accuracy of IMEX schemes](/results/uniform-accuracy-relaxation-systems.md).
- **IMEX-BDF.** The structurally stable systems of Ma et al. (2026, §4) give orders 2, 3, 4
  for every $\varepsilon\in[10^{-7},1]$ with $N=100$ Fourier modes.
- **AP mechanism.** Gottlieb et al. (2022, Prop. 1) and Hu & Shu (2025, Thm. 7.4) use the
  Jin–Xin form to state when the $\varepsilon\to0$ limit of an IMEX scheme is the explicit
  part applied to the limit conservation law.
- **Survey context.** Jin (2022, §6.1) lists AP schemes for relaxation systems (Jin &
  Levermore; Jin; Caflisch, Jin & Russo), high-order IMEX schemes (Pareschi & Russo;
  Dumbser, Enaux & Toro), AP with positivity (Hu & Shu 2019) and the uniform-accuracy proof
  for IMEX-BDF (Hu & Shu 2021).

## Qualifications

- The convergence studies use spectral discretizations on periodic domains and steps
  proportional to $N^{-2}$, the scaling of the energy proofs; they do not test the
  convective CFL regime.
- The tests start after the initial layer or from equilibrium data. Order reduction caused by
  non-equilibrium data is a different effect, not measured here.
- Hu & Shu reuse $b$ for the equilibrium slope and for the Runge–Kutta weights; this page
  writes $\kappa$ for the slope.

# Citations

- [Hu & Shu (2025)](/sources/hu-2025.md) — Eqs. (1.1)–(1.3), (2.1); §6 (Eq. (6.1), Fig. 1); App. 7.3 (Eq. (7.1), Thm. 7.4); arXiv v1.
- [Ma et al. (2026)](/sources/ma-2026.md) — §1, §2.1, Thm. 3.2, §4; arXiv v1.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §3.4.1 (Eqs. (33)–(35)), Prop. 1.
- [Jin (2022)](/sources/jin-2022.md) — §6.1 (Eqs. (6.1)–(6.2)).
