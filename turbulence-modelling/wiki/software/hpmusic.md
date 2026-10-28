---
type: Software
title: "hpMusic"
description: "hpMusic is the University of Kansas high-order flux-reconstruction (FR/CPR) solver for unstructured meshes; this page records its numerics as the sources configure them, its use for implicit LES with adaptive h-refinement of turbine cascades, for subgrid-model calibration in wall-modelled LES, and its HLPW-4 high-lift submission."
status: established
aliases: [hpMusic solver, Kansas hpMusic, W-047]
tags: [software, flux-reconstruction, implicit-les, wmles, mesh-adaptation, turbomachinery]
timestamp: 2026-10-28T02:13:00Z
---

# hpMusic

**hpMusic** is a high-order solver of the compressible Navier–Stokes
equations by the flux reconstruction / correction procedure via
reconstruction (FR/CPR) method, developed at the University of Kansas in
the group of Z.J. Wang. [Ims & Wang (2023)](/sources/ims-2023.md), §2, run
all their LES with it and name it as the solver of the cascade DNS they
take as reference. [Duan & Wang (2024)](/sources/duan-2024.md), §3, use it
to calibrate eddy-viscosity models for high-order
[wall-modelled LES](/methods/wall-modelled-les.md). In the workshop summary of
[Kiris et al. (2023)](/sources/kiris-2023.md) it is submission W-047 of the
4th AIAA High-Lift Prediction Workshop. The code is never the subject of a
study in the bundle; this page collects what the sources print about it.
The method itself is on [flux reconstruction](/methods/flux-reconstruction.md).

## Numerics as reported

| Item | [Ims & Wang (2023)](/sources/ims-2023.md), §2, §4 | [Duan & Wang (2024)](/sources/duan-2024.md), §3–§4 | [Kiris et al. (2023)](/sources/kiris-2023.md), Tables 1–2 (W-047) |
|---|---|---|---|
| Spatial scheme | FR/CPR on unstructured curved cells, correction field lifted from the normal flux jumps (Eqs. 3–6) | FR/CPR, degree $N=2$–5 | "p2 Flux reconstruction", $N=2$ |
| Interface flux | common flux from a local Riemann problem (solver not named) | Roe | not stated |
| Viscous terms | BR2 gradients | common solution and gradients, face gradients by BR2 | not stated |
| Time integration | three-stage SSP Runge–Kutta (explicit) or BDF2OPT (implicit, A-stable, second order) | explicit SSP-RK3, or optimized BDF2 with (block) LU-SGS | implicit BDF2, non-dimensional $\Delta t=9.7\times10^{-5}$ |
| Stabilization | an accuracy-preserving limiter in severely under-resolved regions | element-averaged eddy viscosity (when a model is used) | none stated |
| Turbulence closure | implicit LES, "we apply no subgrid scale model" | implicit LES or Smagorinsky, WALE, Vreman models | implicit LES with an equilibrium wall model |
| Mesh | h-adapted curved meshes with hanging nodes | hexahedral channel and box meshes | committee unstructured grid, 13M degrees of freedom |

The implicit LES of the first and third columns rely on the dissipation of
the discretization alone; see [implicit LES](/definitions/implicit-les.md)
and [numerical dissipation](/properties/numerical-dissipation.md).
Kiris et al. (2023, §II.2, §II.4) state that W-047 solves the compressible
equations with flux reconstruction and no subgrid model, "relying on
artificial dissipation of the inviscid flux discretization".

## Explicit subgrid models in hpMusic

Duan & Wang (2024) add the [Smagorinsky](/methods/smagorinsky-model.md),
[WALE](/methods/wale-model.md) and [Vreman](/methods/vreman-model.md) models
to hpMusic with an eddy viscosity averaged over each element by quadrature
and a zero common interface flux of the subgrid stress (§3, Eqs. 26–27),
and recalibrate the filter width rather than the coefficients: d1
$\Delta=V^{1/3}$, d2 $\Delta=V^{1/3}/\sqrt{N+1}$, d3 $\Delta=V^{1/3}/(N+1)$,
$V$ the element volume (Eqs. 28–30). Implicit LES agrees best with DNS in
the wall-resolved channel at $Re_\tau=180$; in the wall-modelled channel at
$Re_\tau=5200$ on $60\times16\times40$ elements implicit LES "was not
stable", and the Vreman model with d2 is the recommended combination from
$N=2$ to 5 (§5.3–§6). The results are on the
[Vreman model](/methods/vreman-model.md) and
[flux reconstruction](/methods/flux-reconstruction.md) pages. The wall
model reads the LES at the interface between the first and second elements
off the wall, with data from the second element, because the scales of the
first element are always under-resolved (§4, Fig. 4); see
[equilibrium wall model](/methods/equilibrium-wall-model.md). Kiris et al.
(2023, Table 2) print the same exchange location for W-047, "interface
between the 1st and 2nd elements".

## Adaptive h-refinement for implicit LES

Ims & Wang (2023) add to hpMusic three per-cell error indicators that drive
isotropic h-refinement at fixed degree (see
[mesh adaptation](/methods/mesh-adaptation.md) for the indicators and their
ranking):

- the unsteady residual of the solution evaluated at degree $N+1$, which
  they call "freely available" in an hp-aware solver (§3.1, §5.3);
- the Persson–Peraire smoothness indicator (see
  [shock sensors](/definitions/shock-sensor.md)) (§3.2);
- a variant of the Toosi–Larsson small-scale-energy indicator written in
  the computational coordinates of curved cells (§3.3).

Each round marks the 20% of cells with the largest indicator, plus the
cells forced by a one-level size constraint and by a clumping constraint (a
cell at least 50% flanked by marked neighbours is marked); marked cells are
split into equal children that follow the parent's high-order curvature,
and a utility splits the mesh and interpolates the saved fields so that
hpMusic restarts (§4, Fig. 2). Hanging nodes are handled by mortar faces:
data are copied from the fine side and interpolated from the coarse side,
and results are returned by copy (fine side) and $L_2$ projection (coarse
side). In 3D the geometry vectors (normal and area) of a mortar face must be
taken from the coarse side when its flow polynomial is linear and from the
fine side otherwise ("possible and advisable"); otherwise the computation
is unstable because the coarse side is under-integrated (§4). The authors
report this as an implementation observation, without data. They find the
smoothness indicator the simplest to implement and the small-scale-energy
indicator, a double-projected Hessian of a derived velocity, the hardest to
make efficient across MPI, threads and SIMD (§5.3, §6); no timings are
given.

The test cases are the T106c and T106a low-pressure
[turbine cascades](/benchmarks/turbine-cascade.md) of the HiOCFD4/5
workshops at $N=2$ and $N=1$. The T106c reference is a DNS of Alhawwary &
Wang run with hpMusic, which Ims & Wang cite as ref. [26] (§5.1).

## The HLPW-4 high-lift submission

As summarized by Kiris et al. (2023) for the
[NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
(free air, $Re=5.5\times10^6$ on the mean aerodynamic chord, Mach 0.2):

- W-047 is the only flux-reconstruction submission and, with 13M degrees
  of freedom, the smallest after the 3M inviscid one; the best-practice
  grids of the other wall-modelled and lattice-Boltzmann submissions
  range from 273M to 11.3B (Tables 1–2, Fig. 3); its wall-normal spacing is printed as
  "7.2 mm (21.5/3 mm)" at full scale (7 m mean aerodynamic chord) and its
  cell aspect ratio ranges from 1 to 71 (Table 2);
- it obtained "reasonably accurate" integrated loads at $C_{L,\max}$ but
  lacked the outboard slat-bracket-wake separation (§VI.1a);
- its solutions "switched between vastly different states", with
  transients lasting more than 40 convective time units (§III, Fig. 5);
- it falls in stall topology A, inboard stall growing from the
  wing–body juncture (§IV.3);
- W-021 ([CharLES](/software/charles.md)) and W-047 showed a substantial
  reduction of wall-clock hours on GPUs (§VI.4); no figures are given.

## As cited in other sources

[Wang (2024)](/sources/wang-2024-b.md), §4.3.2, compares the pressure
spectra of the VKI LS89 vane computed with the flux-reconstruction solver
ATHOS against the CPR $N=3$ results of Jia et al.: the two agree in the
inertial subrange, the CPR run decays faster at high frequency, and the
author attributes the extra dissipation to "the hpMusic limiter". On the
T106C cascade Wang (2024, §4.2) also compares with the CPR $N=3$ results of
Alhawwary & Wang without naming the solver.

## Qualifications

- Kiris et al. (2023, §VI.1c) write that the implicit codes used time steps
  "only about 10× larger" than the explicit ones. From their Table 2, the
  W-047 step ($9.7\times10^{-5}$) is 1.7–3.3 times the explicit steps
  ($2.9\times10^{-5}$–$5.7\times10^{-5}$), while those of W-031 and W-050
  are about 9–20 times larger *(compiler check, not in the sources)*.
- Kiris et al. print the same size threshold as ">250 M spatial degrees
  of freedom" (abstract), "at least 250M grid cells" (§VI.1a) and "grids
  with >250 M points" (§IV).
- None of the three sources gives the Riemann solver, the limiter or the
  hardware of the W-047 and Ims & Wang runs; Duan & Wang name Roe and BR2.
- Ims & Wang (2023) and Duan & Wang (2024) are by the code's group;
  Kiris et al. summarize the group's workshop submission, and Wang (2024)
  is an outside comparison through a cited result.

# Citations

- [Ims & Wang (2023)](/sources/ims-2023.md) — §2, Eqs. (1)–(6) (FR/CPR, BR2, limiter, SSP-RK3, BDF2OPT, implicit LES, hpMusic); §3.1–3.3 (indicators); §4, Fig. 2 (marking, splitting, restart, mortar faces); §5.1 (T106c, hpMusic DNS reference); §5.3, §6 (implementation cost).
- [Duan & Wang (2024)](/sources/duan-2024.md) — §3, Eqs. (26)–(30) (subgrid models in hpMusic, filter widths); §4, Fig. 4 (wall-model exchange location); §5.3–§6.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — Tables 1–2 (W-047 configuration); §II.2, §II.4 (implicit LES with flux reconstruction); §III, Fig. 5 (transients); §IV.3 (topology A); §VI.1a, §VI.1c, §VI.4 (loads, time steps, GPUs).
- [Wang (2024)](/sources/wang-2024-b.md) — §4.2 (CPR results of Alhawwary & Wang on T106C); §4.3.2, Fig. 16 (hpMusic limiter dissipation, as attributed).
