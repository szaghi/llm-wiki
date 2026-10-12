---
type: Method
title: "Super-time-stepping (Runge–Kutta–Legendre) for parabolic terms"
description: "Explicit Runge–Kutta–Legendre super steps that cover a hyperbolic time step with a number of stages growing as the square root of the ratio of hyperbolic to parabolic step limits, used operator-split for viscosity, conduction, Ohmic and ambipolar diffusion in Athena++ (RKL1/RKL2) and IDEFIX (RKL2), with a stated cost in divergence round-off growth."
status: established
aliases: [STS, RKL, RKL1, RKL2, Runge–Kutta–Legendre, Runge-Kutta-Legendre super-time-stepping]
tags: [time-integration, mhd, constrained-transport, performance]
timestamp: 2026-10-12T00:00:00Z
---

# Super-time-stepping (Runge–Kutta–Legendre)

Explicit diffusion (viscosity, thermal conduction, Ohmic and ambipolar
diffusion) limits the time step in proportion to the square of the cell
width, so at high resolution it can be far smaller than the hyperbolic
limit. Super-time-stepping replaces the many explicit diffusive steps
needed to cover one hyperbolic step by one explicit multi-stage "super
step" whose stage count grows only as the square root of the ratio of the
two limits. The codes in this bundle use the Runge–Kutta–Legendre (RKL)
schemes of Meyer et al. (2012, 2014), operator-split from the hyperbolic
update.

## Stage count and cost

[Lesur et al. (2023)](/sources/lesur-2023.md) (§2.8, eqs. 11–13) give the
relation for RKL2. With $\Delta t_{\mathrm{hyp}}$ the hyperbolic step,
$\Delta t_{\mathrm{par}}$ the explicit parabolic limit and
$s_{\mathrm{RKL}}$ the number of stages,
$$\Delta t_{\mathrm{hyp}} = \Delta t_{\mathrm{par}}\,\frac{s_{\mathrm{RKL}}^2 + s_{\mathrm{RKL}} - 2}{4},$$
so $s_{\mathrm{RKL}} \simeq 2\sqrt{\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}}$
stages replace the $2\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}$
stages of an explicit RK2 integration of the same interval.
[Stone et al. (2020)](/sources/stone-2020.md) (§3.2.5) state the same
scaling for Athena++: a super step of $s_{\mathrm{RKL}}$ stages covers a number of
explicit diffusive steps growing as $s_{\mathrm{RKL}}^2$, so the speed-up is proportional to the
stage count.

## Schemes and splitting in codes

* **[Athena++](/software/athena-plus-plus.md)** offers RKL1 and RKL2,
  operator-split, as an alternative to explicit diffusion added inside each
  integrator stage. An RKL1 super step spans the full (M)HD step; RKL2 uses
  two super steps of half the (M)HD step each per update
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.2.5). The RKL formulae
  are not reproduced in the paper.
* **[IDEFIX](/software/idefix.md)** uses second-order RKL (Meyer et al.
  2014; Vaidya et al. 2017), with first-order RKL kept for debugging, for
  viscosity, thermal diffusion, ambipolar and Ohmic diffusion, but not the
  Hall effect. The RKL stages alternate before and after the main
  integrator to retain second order in time
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.8).
* **[AthenaK](/software/athenak.md)** adds viscous, conductive and Ohmic
  fluxes explicitly in every Runge–Kutta stage, with a step limit of the
  squared cell width over $2d$ times the diffusion coefficient; super
  time stepping and implicit solvers "have not been ported from Athena++"
  ([Stone et al. (2026)](/sources/stone-2026.md), §3.3, eq. 10).

## Effect on the divergence constraint

[Lesur et al. (2023)](/sources/lesur-2023.md) (§2.8) state that with
[constrained transport](/methods/constrained-transport.md) the round-off
error in $\nabla\cdot\mathbf B$ grows as the square root of the number of
cycles with the explicit integrator but linearly with RKL, and recommend
IDEFIX's vector-potential formulation whenever RKL is applied to a
parabolic MHD term. The growth laws are stated without a figure (§2.4,
§2.8).

## Measured gain

In IDEFIX's ambipolar isothermal C-shock (after Mac Low et al. 1995), RKL2
reaches the solution in about 10% of the explicit scheme's time in the
high-resolution runs (2 points per ambipolar length), with an error below
2% at that resolution ([Lesur et al. (2023)](/sources/lesur-2023.md), §4.3,
Fig. 14).

# Citations

1. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.4, §2.8, eqs. 11–13, §4.3, Fig. 14 (arXiv v1).
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.2.5.
3. [Stone et al. (2026)](/sources/stone-2026.md), §3.3, eq. 10 (arXiv v1).
