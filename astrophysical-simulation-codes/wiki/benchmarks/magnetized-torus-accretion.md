---
type: Benchmark
title: "Magnetized Fishbone–Moncrief torus"
description: "A Fishbone–Moncrief equilibrium torus around a Kerr black hole, threaded by a weak single poloidal field loop and perturbed, which develops MRI turbulence and accretes in the SANE state; the EHT code comparison runs nine GRMHD codes on it at three resolutions, AthenaK overlays its run on that data set, and Athena++ runs a variant with different torus and spin as a demonstration."
status: established
aliases: [Fishbone-Moncrief torus, FM torus, SANE torus, magnetized torus accretion, GR torus, EHT torus]
tags: [benchmark, mhd, relativity, verification, amr]
timestamp: 2026-10-13T00:00:00Z
---

# Magnetized Fishbone–Moncrief torus

**Set-up** (the EHT code comparison,
[Porth et al. (2019)](/sources/porth-2019.md), §4, eqs. 8–9; units
$G = c = 1$, lengths in $r_{\mathrm g}$). A Kerr black hole of dimensionless
spin 0.9375. A Fishbone–Moncrief torus with constant specific angular
momentum, inner edge at $6r_{\mathrm g}$ and pressure maximum at
$12r_{\mathrm g}$; $\gamma = 4/3$. A single poloidal loop from a vector
potential proportional to the larger of the density relative to its
maximum minus 0.2 and zero, scaled so that twice the maximum gas pressure
over the maximum squared field is 100. The pressure is perturbed by 4 %
white noise (multiplied by one plus a uniform random number in
$[-0.02, 0.02]$). Domain of
interest from the horizon to $50r_{\mathrm g}$, full polar and azimuthal
range; nominal resolutions $N = 96$, 128 and 192 in that domain; run to
$t = 10^4$ (in $r_{\mathrm g}/c$), averages over $5000$–$10^4$. The
initial data were validated with a stand-alone Fortran 90 program and
equatorial radial cuts from every group. Coordinates, boundaries and floors
are left to each code (logarithmically stretched Kerr–Schild with optional
polar warping suggested).

The weak loop develops MRI turbulence and accretes in the SANE state.
There is no exact solution; codes are compared with each other through
horizon fluxes, disk profiles, averaged maps, an emission proxy and MRI
quality factors (§5.1).

## Runs

* *Nine GRMHD codes, three resolutions*
  ([Porth et al. (2019)](/sources/porth-2019.md), §4–§6, Tables 1–2).
  Athena++, BHAC, Cosmos++, ECHO, [H-AMR](/software/h-amr.md),
  HARM-Noble, iharm3D, IllinoisGRMHD and KORAL, all second-order
  conservative with machine-precision $\nabla\cdot\mathbf B$; plus BHAC
  Cartesian (8 AMR levels, Löhner estimator on magnetization and density)
  and IllinoisGRMHD (Cartesian fixed mesh refinement, finest
  $h \approx r_{\mathrm g}/4.388571$, six factor-2 de-refinements); plus
  BHAC at $256\times256\times128$ and $384^3$ and H-AMR at
  $1608\times1056\times1024$. Accretion-rate max/min across codes falls
  from 3.903 ($N = 96$) to 1.772 ($N = 192$), normalized horizon flux from
  17.408 to 2.777. The full results and their attribution are on
  [EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md).
* *[Athena++](/software/athena-plus-plus.md) in the comparison* (§4.1.1,
  Table 1): VL2, PPM, HLL, Gardiner–Stone CT, radial domain
  $1.152$–$50r_{\mathrm g}$, de-refinement by factors of 2 toward the
  poles. Its outer boundary near the torus edge produces a smaller torus
  and visible kinks (§5.3–§5.4); with PLM its accretion rate falls well
  below the PPM value (App. A).
* *[AthenaK](/software/athenak.md)*
  ([Stone et al. (2026)](/sources/stone-2026.md), §3.6, Fig. 14). Same
  torus (inner edge $6r_{\mathrm g}$, pressure maximum $12r_{\mathrm g}$,
  spin $15/16$, $\gamma = 4/3$, 4 % pressure perturbation) to
  $t = 10^4$, in Cartesian Kerr–Schild coordinates; $\dot M$ and the
  normalized horizon flux are overlaid on the $128^3$ data sets of Porth et
  al. (2019). Visual comparison only: Cartesian against logarithmic grids
  makes a one-to-one comparison "less straightforward". The resolution of this run is
  not stated with Fig. 14.
* *Variant: Athena++ demonstration*
  ([Stone et al. (2020)](/sources/stone-2020.md), §4.3.4, Fig. 42).
  Spin 0.9, inner edge $15r_{\mathrm g}$, pressure maximum
  $25r_{\mathrm g}$, single poloidal loop with mass-weighted inverse plasma
  beta 0.01; spherical Kerr–Schild, root grid $56\times32\times44$,
  logarithmic in radius from $1.329$ to $100r_{\mathrm g}$, static mesh
  refinement with 3 levels away from the axis, effective
  $448\times256\times352$ within $50.625^\circ$ of the midplane; to
  $t = 10^4$. Demonstration only: MRI turbulence saturates and the inner
  disk reaches inflow equilibrium, with reference to the Porth et al.
  (2019) comparison. Different torus and spin, so not comparable number
  for number with the runs above.

## What the test shows

The comparison finds that differences between codes are dominated by
resolution of the MRI, by the treatment of the polar axis and outer
boundary, by floors and by reconstruction (PPM against PLM), and that
"convergence in the strict sense cannot be achieved for ideal MHD
simulations of turbulence" ([Porth et al. (2019)](/sources/porth-2019.md),
§6.1). Only the highest standard resolution ($N = 192$) keeps the MRI
turbulence alive to $t = 10^4$ (§5.6–§5.7). The MRI quality factor, the
wavelength of the fastest-growing MRI mode over the cell width in one
direction (eqs. 25–26), is the resolution diagnostic.

## Later uses (batch 10)

**Athena++ in 2016** ([White et al. (2016)](/sources/white-2016.md), §5, Figs. 13–16). The 2D hydro torus (spin 0.95, $\gamma = 13/9$, HLLC) converges at second order; over three orbits at $64\times32$ the error is 0.030 with HLLE and 0.021 with HLLC. The 3D MRI torus has spin 0.9375, inner edge 6 and pressure maximum 12, outer radius 40, $\gamma = 13/9$, LLF, and runs to $t = 12{,}000$ with static derefinement at the poles. It is compared with Shiokawa et al. (2012), not with another code: plasma beta about 200 in the outer region (against below 60), and larger azimuthal correlation lengths that shrink with resolution.

# Citations

1. [Porth et al. (2019)](/sources/porth-2019.md), §4, §4.1.1, §5.1–§6.1, Tables 1–2, App. A (arXiv v2).
2. [Stone et al. (2026)](/sources/stone-2026.md), §3.6, Fig. 14 (arXiv v1).
3. [Stone et al. (2020)](/sources/stone-2020.md), §4.3.4, Fig. 42.
4. [White et al. (2016)](/sources/white-2016.md), §5, Figs. 13–16.
