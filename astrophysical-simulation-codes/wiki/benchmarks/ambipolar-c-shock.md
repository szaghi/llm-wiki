---
type: Benchmark
title: "Ambipolar C-shock"
description: "A steady magnetized C-type shock whose structure is set by ambipolar diffusion or by ion–neutral drag; run as single-fluid MHD with ambipolar diffusion (Athena++ oblique adiabatic case, IDEFIX isothermal case with super time stepping) and as two-fluid ion–neutral MHD (AthenaK), each against a semi-analytic steady profile."
status: established
aliases: [C-shock, C-type shock, ambipolar diffusion shock, Mac Low C-shock, Masson C-shock]
tags: [benchmark, mhd, verification, time-integration]
timestamp: 2026-10-12T00:00:00Z
---

# Ambipolar C-shock

A steady magnetized shock whose structure is set by ambipolar diffusion
(in single-fluid MHD) or by the drag between ions and neutrals (in
two-fluid MHD). The sources compare with an analytic steady profile
(Athena++) or an ODE solution (AthenaK). Codes that treat ambipolar
diffusion as a parabolic term test that term and its time integration; a
two-fluid code tests its ion–neutral drag coupling. The three runs below
use three different set-ups.

**Runs.**

* *Oblique adiabatic C-shock, single fluid* (after Masson et al. 2012).
  [Stone et al. (2020)](/sources/stone-2020.md), §3.3.4, Fig. 16, with
  [Athena++](/software/athena-plus-plus.md). Left state
  $(\rho, v_x, v_y, B_x, B_y, p) = (0.5, 5, 0, \sqrt2, \sqrt2, 0.125)$,
  right state $(0.9880, 2.5303, 1.1415, \sqrt2, 3.4327, 1.4075)$;
  ambipolar diffusion coefficient $1/(75\rho)$. 2D domain
  $[-0.5, 0.5]\times[-0.0078125, 0.0078125]$ with $h = 1/128$, the
  interface rotated by $\tan^{-1}(3/4)$ to the grid, shifted-periodic in
  $y$ and outflow in $x$; run to $t = 10$. The code reproduces the
  analytic steady profile at this low resolution. No error norm is given.
* *Isothermal C-shock, single fluid* (after Mac Low et al. 1995).
  [Lesur et al. (2023)](/sources/lesur-2023.md), §4.3, Fig. 14, with
  [IDEFIX](/software/idefix.md). Mach number 50, Alfvénic Mach number 10,
  angle $\pi/4$ (as printed); the C-shock length is the ambipolar diffusivity
  over the Alfvén speed $c_A$. The parabolic terms are integrated either
  explicitly with RK2 or with second-order Runge–Kutta–Legendre
  [super time stepping](/methods/super-time-stepping.md), at 2 points per
  C-shock length (high resolution) and 1 point (low resolution). The
  error is "less than 2 %" with 2 points per length, and the
  super-time-stepping run takes "about 10 %" of the explicit time to
  solution at high resolution. This is the only run of the three with a
  quantitative error.
* *Steady C-shock, two-fluid ion–neutral MHD.*
  [Stone et al. (2026)](/sources/stone-2026.md), §3.4, Fig. 7 (right),
  with [AthenaK](/software/athenak.md). Here the ions (MHD) and neutrals
  (hydrodynamics) are separate fluids coupled by a drag term, so
  ambipolar drift is resolved rather than modelled as a diffusion term.
  The ODE solution is mapped to 200 cells and evolved for 10 flow times
  on one CPU core. Upstream: ion density $10^{-3}$, neutral density 1,
  both velocities 30, transverse field 10 in Gaussian units (printed as
  $B_y/\sqrt{4\pi}$), drag coefficient 1, isothermal sound speed 1; Mach
  30, neutral Alfvén Mach 3. The coupling length is printed as $10^4$
  (as the neutral Alfvén speed over the drag coefficient times the ion
  density, which with the printed values gives $10^3$ times the neutral
  Alfvén speed; recorded as printed). The final profile matches the
  initial one ("excellent correspondence"); visual only, no norm.

**What it shows.** Three codes hold the semi-analytic steady profile,
with two independent single-fluid set-ups and one two-fluid set-up. Only
IDEFIX quantifies the error (under 2 % at 2 points per C-shock length)
and the gain from super time stepping (time to solution about 10 % of
explicit). The Athena++ and IDEFIX runs differ in equation of state
(adiabatic against isothermal) and parameters, so their outcomes are not directly comparable.

# Citations

1. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.4.
2. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.3 (arXiv v1).
3. [Stone et al. (2026)](/sources/stone-2026.md), §3.4 (arXiv v1).
