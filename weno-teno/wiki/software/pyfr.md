---
type: Software
title: "PyFR"
description: "PyFR is an unstructured high-order flux-reconstruction solver for CPUs and GPUs; two Dzanic et al. papers implement in it a time-reversibility artificial viscosity and a positivity- and entropy-bounded adaptive modal filter, run nodal DG through FR from degree 2 to 14 on mixed meshes, and report a filter overhead of 1–2 % on a V100 GPU."
status: established
aliases: [PyFR solver, Py-FR]
tags: [software, flux-reconstruction, dg, gpu]
timestamp: 2026-10-22T20:00:00Z
---

# PyFR

PyFR is an open-source solver for unstructured meshes based on the
[flux reconstruction](/methods/flux-reconstruction.md) (FR) approach, which
runs on CPUs and GPUs, as recalled by the two bundle sources that use it
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

The benchmark results are on the pages of the two methods and on
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md),
[isentropic vortex](/benchmarks/isentropic-vortex.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[KPP rotating wave](/benchmarks/kpp-rotating-wave.md),
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) and
[high-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md).

## Qualifications

- Everything on this page is the configuration of two papers by the same
  group, not a description of the code's full capabilities; the PyFR
  paper itself is cited by them, not ingested.

# Citations

- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §4.1 Eqs. (31)–(38), §4.2, §5 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §4.2 Eqs. (25)–(26), §5.1.3, §5.2.3, Alg. 2 (arXiv v3).
