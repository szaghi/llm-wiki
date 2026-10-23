---
type: Software
title: "PyFR"
description: "PyFR is an unstructured high-order flux-reconstruction solver for CPUs and GPUs; four papers of Dzanic and co-authors implement in it a time-reversibility artificial viscosity and a positivity- and entropy-bounded adaptive modal filter, later extended to ideal MHD and multi-species flows, run nodal DG through FR from degree 2 to 14 on mixed meshes, and report filter costs on V100 GPUs."
status: established
aliases: [PyFR solver, Py-FR]
tags: [software, flux-reconstruction, dg, gpu]
timestamp: 2026-10-23T23:30:00Z
---

# PyFR

PyFR is an open-source solver for unstructured meshes based on the
[flux reconstruction](/methods/flux-reconstruction.md) (FR) approach, which
runs on CPUs and GPUs, as recalled by two of the bundle sources that use it
([Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md), §4.2;
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md), §4.2). Neither
source is a paper about PyFR itself; both use it as the host of a new
shock-capturing method, and what follows is the configuration they report.

## Discretization as reported

| ingredient | Dzanic, Trojak & Witherden (2022) | Dzanic & Witherden (2022) |
|---|---|---|
| scheme | FR with correction functions that recover nodal DG, after Huynh | FR with DG correction functions |
| solution points | not stated beyond nodal DG | Gauss–Lobatto on tensor-product elements, $\alpha$-optimized on simplices |
| inviscid flux | Rusanov with Davis wave speeds | HLLC |
| viscous flux | BR1 | BR2 |
| time stepping | explicit RK4; viscous terms implicit in 1D | SSP-RK3 |
| shock capturing | [artificial viscosity](/methods/artificial-viscosity.md) from a time-reversibility defect, element-wise constant | [entropy filtering](/methods/entropy-filtering.md): adaptive exponential modal filter after each stage |
| modal basis | — | orthonormal Legendre, Proriol–Koornwinder–Dubiner–Owens on triangles |

Both formulations are written in matrix form: the divergence at solution
point $x_j$ is a fixed linear combination of the nodal fluxes and of the
common interface fluxes, with the correction-function divergences as
coefficients (Dzanic & Witherden, Eqs. (25)–(26); Dzanic et al., Eqs.
(31)–(38)). Dzanic et al. obtain the reverse-time, downwind divergence of
their sensor by flipping the sign of the dissipative part of the Rusanov
flux, so the sensor reuses the solver's own residual evaluation (§4.2).

## Use in the sources

- **Orders and meshes.** Dzanic et al. run $\mathbb P^2$ to $\mathbb P^{14}$:
  1D Burgers with $\mathbb P^{14}$ on five elements, KPP with $\mathbb P^9$, a
  partially confined explosion on $8\times10^5$ second-order triangles,
  the inviscid ONERA M6 wing on tetrahedra with an extruded surface layer,
  and the MHD rotor and Orszag–Tang vortex with a Powell source (§5).
  Dzanic & Witherden run $\mathbb P^2$–$\mathbb P^7$ on 1D and 2D Euler
  problems, the Taylor–Green vortex at $\mathrm{Re}=1600$, the Daru–Tenaud
  viscous shock tube and an LES of the transonic VFE-2 delta wing with
  $4.1\times10^6$ mixed prism and tetrahedral elements at $\mathbb P^3$,
  $1.04\times10^8$ degrees of freedom per component, compared with
  pressure-sensitive-paint data (§5.2.3).
- **Cost on a GPU.** On an NVIDIA V100, the entropy filter adds 1.1 %,
  1.7 % and 2.0 % to the time to solution with 5, 10 and 20 bisection
  iterations, for a smooth isentropic-vortex run ($40\times40$ elements,
  $\mathbb P^3$, $\Delta t=2\times10^{-4}$, five flow-throughs) (Dzanic &
  Witherden, §5.1.3). Dzanic et al. give no timing for their viscosity;
  its extra forward and backward residual evaluations at every Runge–Kutta
  stage are not costed.
- **Precision.** Dzanic & Witherden set the upper end of the filter
  bracket from $\varepsilon=10^{-8}$, labelled "machine precision (FP32)"
  (Alg. 2). The FP32 unit roundoff is $2^{-24}\approx6\times10^{-8}$, so the
  label is inexact; as a bracket end it is harmless *(compiler check, not
  in the sources)*. The sources do not state which precision the runs use.

- **Ideal MHD and a faster filter.** [Dzanic & Witherden (2023)](/sources/dzanic-2023.md)
  extend the entropy filter in PyFR to ideal MHD with Powell's source term,
  using FR with DG correction functions, Gauss–Lobatto nodes on tensor
  elements and $\alpha$-optimized nodes on simplices, HLLC with Davis wave
  speeds (HLL for an extreme blast wave) and SSP-RK3 (§4). Their nodewise
  Illinois solve for the filter strength cuts a weakly magnetized 3D
  Rayleigh–Taylor run on 16 NVIDIA V100 GPUs from 61.4 to 25.3 GPU hours at
  $\mathbb P^3$ and from 257 to 39.8 at $\mathbb P^4$, with an example
  implementation in their supplementary material (§4.1, §5.6, Fig. 17;
  [entropy filtering](/methods/entropy-filtering.md)).
- **Multi-species flows.** [Trojak & Dzanic (2024)](/sources/trojak-2024.md)
  run the entropy filter in PyFR on the conservative multi-species Euler
  and Navier–Stokes equations, with solution and flux points at
  Gauss–Lobatto points on tensor-product elements and $\alpha$-optimized
  points on simplices, HLLC inviscid and BR2 viscous fluxes, and SSP-RK3
  with a fixed step (§4, arXiv v1). The runs go up to $\mathbb P^5$ on a
  near-vacuum density wave, $\mathbb P^3$ on $2800\times1200$ quadrilaterals
  for a triple-point problem and on $32\times32\times64$ hexahedra for a
  3D Rayleigh–Taylor instability, on up to 40 NVIDIA V100 GPUs; with the
  structured filter matrices of Dzanic & Witherden (2023) the filter is
  stated to be "only a small portion of the total compute time", with no
  timing printed (§4–5; [entropy filtering](/methods/entropy-filtering.md)).
- **As seen from other GPU codes.** [Bielawski et al. (2023)](/sources/bielawski-2023.md)
  cite PyFR as a GPU-accelerated unstructured high-order FR solver whose
  dominant cost is sparse and dense matrix multiplication handled by BLAS
  libraries, in contrast with the low arithmetic intensity of their
  second-order finite-volume fluxes (§1).
  [Zaghi et al. (2023)](/sources/zaghi-2023.md) group it with STREAmS and
  nek5000 as GPU-performant codes with limited algorithmic flexibility
  (§2.1), and [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) list
  it among the existing GPU solvers they position URANOS against (§1).

The benchmark results are on the pages of the two methods and on
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md),
[isentropic vortex](/benchmarks/isentropic-vortex.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[KPP rotating wave](/benchmarks/kpp-rotating-wave.md),
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) and
[high-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md).

## Qualifications

- Everything on this page is the configuration of four papers by the same
  group, not a description of the code's full capabilities; the PyFR
  paper itself is cited by them, not ingested.

# Citations

- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §4.1 Eqs. (31)–(38), §4.2, §5 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §4.2 Eqs. (25)–(26), §5.1.3, §5.2.3, Alg. 2 (arXiv v3).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §4, §4.1, §5.6 Fig. 17 (arXiv v2).
- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §4, §5 (arXiv v1).
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §1 (accepted manuscript).
- [Zaghi et al. (2023)](/sources/zaghi-2023.md) — §2.1.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §1.
