---
type: Software
title: "HOW-MHD (high-order WENO MHD code with high-order constrained transport)"
description: "Public Cartesian ideal-MHD code (adiabatic and isothermal) built on Jiang–Wu fifth-order finite-difference WENO, five-stage fourth-order SSP Runge–Kutta at CFL 1.5, and a fourth- or sixth-order staggered constrained transport that lifts the code's convergence on multi-D MHD waves from second to fifth order."
status: established
aliases: [HOW-MHD]
tags: [software, mhd, weno, constrained-transport, finite-difference]
timestamp: 2026-10-08T00:00:00Z
---

# HOW-MHD

**Identity** ([Seo & Ryu (2023)](/sources/seo-2023.md)). A Cartesian code
for ideal MHD, in adiabatic and isothermal versions, with a public
version linked from the paper (footnote 1). Cylindrical and spherical
geometry is left for future work (§4).

**Numerics** (§2).
* Fifth-order FD-WENO in the Jiang–Wu form: the fourth-order central flux
  plus nonlinear corrections in characteristic fields, with Jiang–Shu
  weights at $\varepsilon = 10^{-8}$ and a local Lax–Friedrichs speed over
  the six-point stencil. The eigenvectors are Ryu–Jones (adiabatic, seven
  waves) and Kim et al. (isothermal, six waves, no entropy mode)
  ([WENO](/methods/weno.md); [characteristic decomposition](/methods/characteristic-decomposition.md)).
  The authors tried several WENO variants and kept Jiang–Shu, without
  showing data (§1).
* Time: SSPRK(5,4) of Spiteri and Ruuth at CFL 1.508, its SSP coefficient,
  about 50% cheaper than classical RK4 at CFL 0.8 with the same results
  ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).
* **High-order constrained transport.** Face values of the normal field
  are updated by fourth- or sixth-order staggered differences of edge
  electric fields. Those fields are built from the upwinded parts of the
  WENO fluxes of the induction equation and corrected by
  $\frac{1}{24}$ second differences across the edge's transverse plane.
  The zone-centred field comes from sixth-order interpolation
  ([constrained transport](/methods/constrained-transport.md)).

**Results** (§3). On 3D oblique linear waves and the
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
the code converges at fifth order with the new CT, against second order
with the original second-order CT. Loops and reconnection show less
numerical diffusion ([field-loop advection](/benchmarks/field-loop-advection.md)).
The oblique Ryu–Jones–Frank shock tube, the rotor and a 3D blast run
without loss of robustness, and the discrete divergence stays at round-off
([grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md);
[MHD rotor](/benchmarks/mhd-rotor.md); [MHD blast wave](/benchmarks/mhd-blast-wave.md)).
In driven turbulence a $128^3$ HOW-MHD run resembles a $256^3$ run of a
second-order TVD code.

# Citations

1. [Seo & Ryu (2023)](/sources/seo-2023.md), §§1–4.
