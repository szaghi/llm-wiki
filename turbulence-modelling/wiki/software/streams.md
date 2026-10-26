---
type: Software
title: "STREAmS"
description: "STREAmS is an open-source multi-GPU finite-difference solver for compressible wall-bounded flows on Cartesian grids, combining energy-preserving central schemes with WENO shock capturing; this page records its numerics and its use for supersonic and hypersonic boundary-layer DNS and for implicit LES of a capsule wake with immersed boundaries."
status: established
aliases: [STREAmS-2.0, STREAMS]
tags: [software, gpu, dns, compressible, implicit-les, immersed-boundary]
timestamp: 2026-10-26T11:08:00Z
---

# STREAmS

**STREAmS** is an open-source, GPU-accelerated finite-difference solver of
the compressible Navier–Stokes equations on Cartesian grids for canonical
wall-bounded flows, by Bernardini and co-workers (Bernardini et al. 2021,
and STREAmS-2.0, Bernardini et al. 2023, as recalled by
[Placco et al. 2023](/sources/placco-2023.md), §2). It runs on multiple GPUs
through CUDA Fortran ([Cogo et al. 2022](/sources/cogo-2022.md), §2). Both
studies of this bundle that use it ran on the Marconi100 system of CINECA.

## Numerics

- **Convective terms.** Cogo et al. (2022, §2) describe "consolidated,
  high-order, energy-preserving schemes" in shock-free regions, "free of
  numerical dissipation", and WENO shock capturing applied locally where the
  Ducros sensor flags shocks (see [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
  and [WENO and hybrid schemes](/methods/weno-scheme.md)). Placco et al.
  (2023, §2) describe fifth-order WENO for the convective terms, "to account
  for flow discontinuities", and do not mention the central part.
- **Viscous terms.** A locally conservative formulation "expanded to
  Laplacian for ensuring finite molecular dissipation at all resolved
  wavelengths" (Cogo et al. 2022, §2); sixth-order central differences
  (Placco et al. 2023, §2).
- **Time.** Third-order explicit Runge–Kutta of Wray (Placco et al. 2023,
  §2).
- **Immersed boundaries.** Placco et al. (2023, §2) represent a capsule with
  a ghost-point-forcing [immersed boundary method](/methods/immersed-boundary-method.md)
  that imposes no-slip and no-penetration through ghost nodes filled from the
  fluid.

Neither source gives orders of accuracy for the central schemes or
performance figures of the code.

## Applications in the sources

- **DNS of zero-pressure-gradient boundary layers** (Cogo et al. 2022, §2,
  Table 1): four spatially developing [boundary layers](/benchmarks/turbulent-boundary-layer.md)
  over a cold isothermal wall ($T_w/T_r=0.76$), $M_\infty=2$ and 5.86, at
  $Re_\tau\approx450$ and $\approx2000$; recycling–rescaling inflow with the
  recycling station at $80\delta_{\mathrm{in}}$; wall-normal "natural"
  stretching of Pirozzoli & Orlandi (constant resolution in units of the
  local Kolmogorov length in the outer layer); grids up to
  $16384\times832\times2048$ points with $\Delta x^+\le7.9$, $\Delta z^+\le4.8$;
  runs of $200\,\delta_{\mathrm{in}}/u_\infty$. The database tests
  [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md) and the
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md);
  resolution details are on [direct numerical simulation](/definitions/direct-numerical-simulation.md).
- **Implicit LES of a Mars entry capsule** (Placco et al. 2023, §2–§3):
  ExoMars-shaped capsule at $M_\infty=2$, $Re=10^6$ on the diameter
  $D=3.8$ m, CO$_2$ ideal gas ($\gamma=1.3$, $Pr=0.72$), angles of attack
  $0^\circ$ to $15^\circ$; $2048\times672\times672$ nodes on a
  $20D\times10D\times10D$ box, 32 GPUs; no subgrid model, the numerical
  dissipation of the discretization acting "as artificial viscosity at small
  scales" ([implicit LES](/definitions/implicit-les.md)). The drag
  coefficient falls from 1.5685 at $0^\circ$ to 1.5349 at $15^\circ$ and the lift spectrum peaks at
  $St=fD/U_\infty\approx0.2$–$0.3$ (Table 3, Fig. 11). The resolution in wall
  units is not reported and no reference data are compared.

## Qualifications

- [Kurz et al. (2025)](/sources/kurz-2025.md), §1, describe STREAmS (citing
  both releases) as a solver of "high-order finite difference methods with
  WENO-type shock capturing", contrasting it with DG and flux
  reconstruction codes. The description agrees with Cogo et al. and Placco
  et al. and adds no figures.
- The two sources describe the convective discretization differently
  (energy-preserving central plus Ducros-switched WENO; fifth-order WENO
  only). Whether the central part was active in the capsule runs is not
  stated; this is a gap in the description, not a contradiction.

# Citations

- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2, Table 1 (STREAmS numerics, CUDA Fortran, boundary-layer DNS set-up).
- [Placco et al. (2023)](/sources/placco-2023.md) — §2 (STREAmS and STREAmS-2.0, WENO, central viscous terms, Wray Runge–Kutta, ghost-point immersed boundary, implicit LES); §3, Table 1 (grid, 32 GPUs); §4, Table 3, Fig. 11.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §1 (STREAmS as a high-order finite-difference WENO code).
