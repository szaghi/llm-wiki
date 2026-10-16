---
type: Software
title: "HYMAGYC"
description: "Hybrid code coupling linear resistive full MHD (an initial-value derivative of the MARS eigenvalue solver, backward Euler, Fourier × finite elements) to gyrokinetic δf energetic-particle PIC through pressure coupling, with an optional Cartesian (R, Z) stress-tensor grid that filters numerical noise; a reference code of the NLED-AUG benchmarks."
status: established
aliases: [HYMAGYC code]
tags: [code, hybrid-kinetic, energetic-particles, alfven-eigenmode, particles, time-integration, verification]
timestamp: 2026-10-16T23:30:00Z
---

# HYMAGYC

HYMAGYC is a [hybrid kinetic-MHD](/methods/hybrid-kinetic-mhd.md) code in
which the thermal plasma follows **linear**, full, resistive MHD in arbitrary
axisymmetric equilibria and the energetic particles (EPs) follow a nonlinear
gyrokinetic Vlasov equation solved by particle-in-cell
([Vlad et al. (2025)](/sources/vlad-2025.md), §3, Appendix).
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§II) group it with HMGC
and M3D-C1-K as codes that add an explicit EP contribution to an implicit MHD
advance.

## MHD module

From Vlad et al. (2025), §3:
* Derived from the MARS eigenvalue code, converted to an initial-value solver.
* Fully implicit backward-Euler time stepping (see
  [implicit time integration](/methods/implicit-time-integration.md)).
* Fourier series in the poloidal and toroidal angles, generalized finite
  elements with the Tunable Integration Method in the radial direction; an
  equal-arc-length poloidal angle.
* Resistivity and adiabatic index included, no viscosity:
  $S^{-1}=5\times10^{-7}$, $\Gamma=5/3$ in the NLED-AUG case.
* 180 radial points and poloidal modes $m\in[-3,13]$ for $n=-1$.

## Energetic-particle module

From Vlad et al. (2025), §3 and Appendix:
* Nonlinear gyrokinetic equations of motion (Brizard 1990) expanded to second
  order in the ratio of the EP Larmor radius to the density scale length and to
  first order in its ratio to the field scale length (Eqs. A1–A4); standard
  [δf](/methods/delta-f-method.md) (see
  [particle pushers](/methods/particle-pushers.md)).
* PIC grid of $180\times120$ in $(s,\theta)$, gridless finite-size particles in
  $\phi$ with 8 toroidal points, 64 markers per cell, 11 059 200 markers in
  total; FLR by a 32-point gyro-average, FOW-only runs set the average to the
  gyrocentre value.
* EPs crossing the last closed surface are lost and not re-injected.
* **Coupling** through the divergence of the EP pressure tensor in the MHD
  momentum equation ([pressure coupling](/methods/pressure-and-current-coupling.md),
  Park 1992). The tensor divergence is computed either on the $(s,\theta)$ grid
  or on a new Cartesian $(R,Z)$ grid ($121\times121$ by default). The $(s,\theta)$
  evaluation is prone to short-scale perpendicular noise and numerical
  instability in the nonlinear phase, especially with FOW only; the coarser
  Cartesian grid acts as an intrinsic filter that trims the poloidal-spectrum
  tails (§3, Fig. 7).

## Benchmarks

* **[NLED-AUG](/benchmarks/nled-aug-benchmark.md), linear** (Vlad et al. 2025,
  Table 2): FOW-only $\gamma=174\,606$ s$^{-1}$ and $\omega/2\pi=180.02$ kHz with
  the $(s,\theta)$ stress tensor, $231\,090$ s$^{-1}$ and $162.42$ kHz with the
  $(R,Z)$ tensor; with FLR $199\,841$ and $215\,570$ s$^{-1}$, $171.51$ and
  $163.00$ kHz. With the $(s,\theta)$ tensor FLR raises the growth rate, against
  the general statement of §7 that FLR lowers it. HYMAGYC $(R,Z)$ and MEGA
  agree in $\gamma$ within 5.5 % (FOW) and 21 % (FLR) (compiler's ratio).
* **NLED-AUG, nonlinear** (§3, Figs. 2–6, 13): the
  [EPM](/definitions/energetic-particle-mode.md) saturates at
  $t\approx700\,\tau_A$ (0.14 ms; $\tau_A=R_0/v_A$ on axis, $2.0\times10^{-7}$ s) with a few overshoots and chirps downward
  along the lower continuum of the toroidal gap; the core of the hollow EP
  profile fills and the mid-radius peak drops (from about $2.15$ to
  $1.4\times10^{18}$ m$^{-3}$ by 0.36 ms); a non-chirping, counter-rotating
  external [TAE](/definitions/toroidal-alfven-eigenmode.md) ($m=2,3$) later
  dominates. About 15 % of the EPs are first-orbit losses and another 20 % are
  lost after saturation. Power-exchange analysis shows the drive coming
  mainly from co- and counter-passing EPs in the inner half, with a trapped-EP
  outer drive about ten times weaker that the authors link to the late TAE.
* **AUG-NLED with JOREK**: JOREK's growth rate is close to HYMAGYC's and MEGA's,
  but HYMAGYC's frequency rises with the EP gradient (about 150 to 179 kHz)
  where JOREK's falls ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md),
  §IV B, Fig. 9).

## Limitations and benchmark spread

* Linear MHD only, so wave–wave nonlinearity is absent by construction (Vlad
  et al. 2025, §3); the benchmark omits fluid nonlinearities in all codes
  (§1).
* The FOW-only $(s,\theta)$ run is numerically unstable in the long saturated
  phase (§3).
* Saturated energy about 15× higher than MEGA's, EP redistribution much
  stronger, and the TAE onset more than 0.2 ms after the first saturation
  against about 0.1 ms in MEGA; the cause is not identified (§4, §7). Recorded
  on the [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md).

# Citations

1. [Vlad et al. (2025)](/sources/vlad-2025.md) — §1, §§3–4, §7, Appendix, Tables 1–2, Figs. 2–7, 13.
2. [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §II, §IV B, Fig. 9.
