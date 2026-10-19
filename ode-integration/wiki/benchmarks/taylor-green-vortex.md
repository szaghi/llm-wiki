---
type: Benchmark
title: "Taylor–Green vortex"
description: "Three-dimensional periodic vortex flow used to test time integrators on compressible-flow semidiscretizations: inviscid at low Mach number as a stability-limited test for explicit pairs and step-size controllers, and viscous at Re 1600 for optimized many-stage Runge–Kutta methods."
status: established
aliases: [TGV, Taylor-Green vortex, inviscid Taylor–Green vortex, Taylor–Green vortex at Re 1600]
tags: [explicit, step-size-control, runge-kutta, stability]
timestamp: 2026-10-19T00:00:00Z
---

# Taylor–Green vortex

The **Taylor–Green vortex (TGV)** is a three-dimensional periodic flow whose smooth initial
vortices stretch and break down into turbulence. In the sources it serves as a method-of-lines
test for explicit time integrators: the semi-discrete spectrum of a high-order DG-type
discretization makes the time step **stability-limited** for most of the run, so the benchmark
measures how far a method's stability region and its step-size controller let the step grow
([Ranocha et al. 2022](/sources/ranocha-2022.md), §5.1;
[Hedayati Nasab et al. 2021](/sources/hedayatinasab-2021.md), §7.2).

## Set-up

Page-local symbols: velocity $(v_1,v_2,v_3)$, pressure $\mathcal P$, density $\rho$, temperature
$\Theta$, Mach number $\mathrm{Ma}$, Reynolds number $\mathrm{Re}$.

**Inviscid, nondimensional** (Ranocha et al. 2022, §5.1, Eq. (5.3)). 3D compressible Euler on
the periodic cube $[-\pi,\pi]^3$:

$$\begin{aligned}
v_1&=\sin x_1\cos x_2\cos x_3,\qquad v_2=-\cos x_1\sin x_2\cos x_3,\qquad v_3=0,\\
\mathcal P&=1+\tfrac1{16}\bigl(\cos2x_1+\cos2x_2\bigr)\bigl(\cos2x_3+2\bigr),\qquad \Theta=1,
\end{aligned}$$

- $\mathrm{Ma}=0.1$;
- entropy-dissipative nodal DG spectral-element collocation with 8 elements per direction;
- final time 20, or 8 in the controller optimization.

**Viscous, dimensional** (Hedayati Nasab et al. 2021, §7.2, Eq. (29)). 3D compressible
Navier–Stokes on $[-\pi L,\pi L]^3$:

$$\begin{aligned}
v_1&=U_0\sin\tfrac xL\cos\tfrac yL\cos\tfrac zL,\qquad v_2=-U_0\cos\tfrac xL\sin\tfrac yL\cos\tfrac zL,\qquad v_3=0,\\
\mathcal P&=\mathcal P_0+\frac{\rho_0U_0^2}{16}\Bigl(\cos\tfrac{2x}L+\cos\tfrac{2y}L\Bigr)\Bigl(\cos\tfrac{2z}L+2\Bigr),\qquad \rho=\mathcal P/(R_{\mathrm g}\Theta_0),
\end{aligned}$$

- $\mathrm{Ma}=0.1$, $\mathrm{Re}=1600$ ($R_{\mathrm g}$ the gas constant, page-local);
- final time $20t_c$ with $t_c=L/U_0$;
- flux-reconstruction DG of degree 5 on hexahedra, prisms or tetrahedra, about $256^3$ solution
  points;
- checked against a reference spectral DNS (van Rees et al.).

The two set-ups share the velocity and pressure fields up to scaling; they differ in viscosity
and element types.

## What it tests and results

**Stability-limited explicit pairs and controllers** (Ranocha et al. 2022). The step is mostly
stability-limited and the flow becomes turbulent. At $\mathrm{Ma}=0.1$ the negative real axis
of the stability region matters more than the rest of the advection spectrum; methods covering
more of it do better (§5.5.4). Right-hand-side evaluations at tolerance $10^{-5}$:

- **general-purpose pairs** (§5.5.1, Table 3): BS3(2)3F 5256, BS5(4)7F 7722, DP5(4)6F 8014,
  i.e. the third-order pair is about 50% more efficient when stability-limited;
- **SSP pair** (§5.5.2, Table 4): SSP3(2)4[3S\*$_+$] with controller $(0.55,-0.27,0.05)$ needs
  3438 against 5256/5261 for BS3(2)3F and SSP3(2)3 at loose and medium tolerances, but its cost
  grows sharply at tight tolerances;
- **new low-storage pairs** (§6.2): the third-order pairs are up to 5% better than
  KCL4(3)5[3R$_+$]C with optimized PID, and the fifth-order pairs up to 18% better than
  KCL5(4)9[2R$_+$]S with its prescribed controller;
- **controller tuning**: the TGV is one of the three problems in the brute-force PID search
  (§5.4; see [step-size control](/methods/step-size-control.md)).

**Optimized many-stage methods at Re 1600** (Hedayati Nasab et al. 2021, §7.2). A fourth-order,
16-stage method with an [optimal stability polynomial](/methods/optimal-stability-polynomial.md)
for the multidimensional element spectrum runs at 80% of its bisected maximal stable step.
Against the classical four-stage RK4 at the same fraction, the per-stage step ratios are:

| Elements | hexahedra | prisms | tetrahedra |
|---|---|---|---|
| speedup | 1.68 | 1.64 | 1.57 |

The kinetic-energy dissipation rate and enstrophy histories are visually indistinguishable,
and so are the Q-criterion isosurfaces at $t=15t_c$ (Figs. 8–10). The speedup is a ratio of
stage-normalized step sizes; no wall-clock time or hardware is reported.

[Southworth et al. (2022)](/sources/southworth-2022.md) mention that the Taylor–Green vortex
gave results similar to their double shear layer for implicit Runge–Kutta solvers, without
showing them (§7.2).

## Qualifications

- Both uses measure cost at the linear stability limit of explicit methods on dissipative
  DG-type discretizations; the TGV is not used for accuracy-limited or implicit comparisons in
  these sources.
- Hedayati Nasab et al. write the snapshot time as "$t_c=15$"; $t=15t_c$ is meant (§7.2).

# Citations

- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §5.1 (Eq. (5.3)), §5.4, §5.5.1–5.5.4 (Tables 3–4), §6.2.
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §7.2 (Eq. (29), Figs. 8–10).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §7.2 (results mentioned, not shown).
