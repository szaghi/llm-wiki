---
type: Benchmark
title: "Rayleigh–Taylor mixing"
description: "Buoyancy-driven mixing of a heavy fluid placed above a light one: a transient flow that passes from linear laminar growth through bubbles, spikes and Kelvin–Helmholtz transition to turbulent mixing, here at Atwood number 0.5 as a test that RANS fails and partially-averaged Navier–Stokes recovers at a fraction of the resolution."
status: established
aliases: [Rayleigh-Taylor instability, RT mixing layer, Rayleigh–Taylor flow, variable-density mixing layer]
tags: [benchmark, pans, hybrid-rans-les, rans]
timestamp: 2026-10-27T15:37:00Z
---

# Rayleigh–Taylor mixing

A heavy fluid of density $\rho_h$ rests above a light fluid of density
$\rho_l$ under gravity $g$, and the perturbed interface is unstable: the
misalignment of the density gradient and the pressure gradient generates
vorticity, light fluid rises in bubbles and heavy fluid falls in spikes, and
Kelvin–Helmholtz instability on their flanks triggers turbulence. The
density contrast is measured by the Atwood number
$At=(\rho_h-\rho_l)/(\rho_h+\rho_l)$. A mixing layer of height $h$ grows,
late in time as $h\propto At\,g\,t^2$. The flow is transient and passes
through laminar, transitional and turbulent stages, and turbulent kinetic
energy is produced both by shear and by buoyancy, which one-point RANS
closures are not designed to represent. In this bundle it tests how much of
the spectrum a bridging model must resolve.

## Set-up in the source

[Pereira et al. (2021)](/sources/pereira-2021.md), §II, App. A, Table I:

- prism of square section $L=2\pi$ cm and height $3L$; periodic lateral
  boundaries, reflective top and bottom;
- $At=0.5$, viscosities 0.002 and 0.006 g/(cm s) (light, heavy), $\gamma=1.4$,
  Schmidt and Prandtl numbers 1, $g=-980$ cm/s$^2$, Mach number below 0.1;
  the Reynolds number $\dot hh/\nu$ reaches about 500;
- initial interface perturbation: a band of modes $30\le\sqrt{n^2+m^2}\le34$
  with random phases and standard deviation up to $0.04L$, containing the
  most unstable linear mode, of wavelength $h_o=2\pi/32$ (Eq. 2);
- compressible multi-material finite-volume code xRAGE (HLLC Riemann
  solver, parabolic reconstruction, low-Mach correction, Heun time
  stepping, maximum CFL 0.5), $256^2\times768$ cells; time in units of
  $\sqrt{h_o/(g\,At)}$, run to $t=25$;
- diagnostics: $h$ between the 5% and 95% levels of the mixture fraction,
  a growth coefficient $\alpha_b=\dot h^2/(4g\,h\,At)$ averaged over the
  last ten time units, the molecular-mixing parameter $\theta_m$ (page-local;
  0 unmixed, 1 fully mixed), and resolved spectra at the centre plane.

The reference is the same code with no closure ($f_k=0$), not an external
DNS; its growth coefficient $\alpha_b\approx0.025$ matches the DNS of
Livescu et al. that the authors cite (§IV.2). A grid study at $f_k=0$ with
$64^2\times192$ to $512^2\times1536$ cells shows the $256^2\times768$ and
$512^2\times1536$ results nearly identical, while the coarsest grid misses
the shape of $h(t)$ (App. B, Fig. 18).

## Regimes

The flow is linear and laminar until $t\approx2.5$, then nonlinear: mushroom
bubbles and spikes form, fine-scale turbulence is visible from $t\ge5$, and
the layer grows quadratically late in time (§IV.1). Shear and buoyancy
contribute similarly to the production at first (§IV.3.3).

## What the case tests

**Failure of RANS in a transitional flow.** With the variable-density
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
closure (a scale-aware form of the Besnard–Harlow–Rauenzahn linear
eddy-viscosity model) run as RANS ($f_k=1$), the mixing is over-predicted:
$\alpha_b=0.043$ against 0.025, linear mixture-fraction profiles, $\theta_m$
near 0.95 before $t=5$ and tending to one, against 0.8 at $t\approx25$ in
the reference; the maximum ratio of effective to molecular viscosity is
20,737 at $t=25$ (§IV.2–IV.3.1, Table II, Figs. 8–11). The closure already
alters the laminar linear stage, where the turbulent stress should vanish,
and puts the peaks of the turbulent mass flux and of the density–specific-volume
correlation on the heavy side, against the DNS literature (§IV.2, §IV.3.2).

**Convergence of a bridging model with resolution.** Lowering $f_k$, the
ratio of unresolved to total kinetic energy, moves the solution toward the
reference. Of three ways of setting the other resolution ratios, setting the
mass-flux ratio to $\sqrt{f_k}$ (strategy S2) is best: at $f_k=0.25$ it
gives $\alpha_b=0.024$ and an effective-viscosity ratio of 408, and S2 needs
$f_k\le0.35$ to reproduce the reference. The strategy derived from a priori
filtering of fully developed variable-density turbulence (S3) does not
converge as $f_k$ decreases and produces a nonphysical overshoot at
$t=2.5$, which the authors attribute to assuming developed turbulence in a
transitional flow (§IV.2, §IV.3.2, Table II). Coherent structures at
$t=2.5$ are indistinguishable from the reference for $f_k\le0.35$ and are
dissipated above it; the resolution needed is set by the bubbles and spikes
that trigger turbulence (§IV.3.4, Fig. 16). See
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

**Spread in the literature.** The authors' survey (§I, Fig. 1) finds
experimental growth coefficients significantly larger than simulated ones,
small variability among DNS and a broad range among
[implicit LES](/definitions/implicit-les.md) runs, attributed beyond initial
conditions to inviscid or one- and two-dimensional modelling assumptions.

## Shock-driven counterpart

[Davidovits et al. (2022)](/sources/davidovits-2022.md), §III, adapt the linear
analysis of the Richtmyer–Meshkov instability to scale the turbulence a
strong shock generates in a medium with order-one density fluctuations
($\sigma_v\propto A_\sigma U_s$, page-local symbols defined there). For a
continuous density field they use a pre-shock average Atwood number built
from the normalized density standard deviation, which is not the two-fluid
$At$ of this page; the scaling and the turbulent jump relations are on
[shock-generated turbulence](/results/shock-generated-turbulence.md). No
ingested source compares the two configurations.

## Single-mode inviscid instability as a shock-capturing test

[Takagi et al. (2022)](/sources/takagi-2022.md), §4.7,
[Liang & Fu (2024)](/sources/liang-2024.md), §4.7,
[Huang et al. (2025)](/sources/huang-2025.md), §5.7, and
[Kumar & Ghosh (2022)](/sources/kumar-2022-b.md), §3.1.7, run the inviscid
two-dimensional single-mode instability (densities 2 and 1, $\gamma=5/3$,
$At=1/3$ *(compiler check, not in the sources)*, grids $64\times256$ to
$300\times1200$, $t=1.95$; Kumar & Ghosh on $[0,1/4]\times[0,1]$ with
spacings $1/480$ and $1/960$, initial perturbation
$v=-0.025\,c\cos(8\pi x)$, $c$ the sound speed) only as a small-scale
resolution test of [WENO and TENO schemes](/methods/weno-scheme.md), where
its results are; it has no viscosity, mixing statistics or turbulence and
is not the mixing-layer flow of this page. Kumar & Ghosh find that the
less dissipative schemes resolve more roll-up and are the ones that lose
the left–right symmetry of the single mode (their four-point
bandwidth-optimized scheme on the coarser grid, the three-point one only
marginally on the finer), which they call consistent with an earlier
finding of Fu et al. (Figs. 19–22).

## Rayleigh–Taylor fingers in a solar-flare simulation

[Ruan et al. (2023)](/sources/ruan-2023.md) run a three-dimensional
resistive MHD simulation of a solar flare (MPI-AMRVAC, effective $1024^3$
by adaptive refinement, cells below 100 km) in which reconnection downflows
hit the flare arcade below a termination shock. Rayleigh–Taylor and
Richtmyer–Meshkov fingers form at the interface, as in the earlier
simulation of Shen et al. that the authors cite, which attributed the
turbulence there to them; in this run the fingers appear later than the
analysed phase and below the region of largest nonthermal velocity, where
the velocity at the upper border of the loops stays below 50 km/s. The
authors find the turbulent zone "most likely driven by" the
Kelvin–Helmholtz instability of the shear between downflows and reflected
upflows, which is unstable in planes perpendicular to the guide field
(§1, §3.1, §3.3, Fig. 3). The run has no subgrid closure, and the paper
reports no resolution study; see
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md) and
[mesh adaptation](/methods/mesh-adaptation.md). It is a buoyancy-driven
interface in a magnetized, stratified plasma, not the two-fluid mixing
layer of this page.

## Qualifications

- Only one ingested source runs the turbulent mixing case; the page
  records its set-up and findings, not a cross-source consensus.
- [Pereira et al. (2021)](/sources/pereira-2021.md) (read in arXiv v2) call
  $\alpha_b$ the growth rate of the mixing-layer half-width (and, in §I,
  "of the lower interface") while computing it from the full height $h$:
  for $h=\alpha At\,g\,t^2$, $\dot h^2/(4ghAt)=\alpha$, the coefficient of
  the full height *(compiler check, not in the sources)*.
- They set the maximum CFL number to 0.5 for all runs in §II, yet report
  that strategy S3 at $f_k<0.5$ required "a CFL number not exceeding 0.5"
  (§IV.2), and use 0.8 on the finest grid of App. B.
- The text calls the accuracy of strategy S1 monotonic in $f_k$ (on $h(t)$,
  Fig. 8a), while the S1 growth coefficients of Table II (0.027, 0.012,
  0.016 at $f_k=0.50$, 0.35, 0.25, reference 0.025) are not monotonic in
  error.
- The reference run is under-resolved at the initial interface
  ($\theta_m\approx0.26$ at $t=0$, §IV.2), although the authors call it a
  simulation resolving all flow scales.
- **An announced test that is not in the paper.** The abstract of
  [Svärd (2022)](/sources/svard-2022.md) lists "a turbulent
  Rayleigh-Taylor problem" among the tests of its entropy-stable implicit
  LES scheme, but the paper runs a Kelvin–Helmholtz instability and the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) instead (§1,
  §5); it contains no Rayleigh–Taylor result.

# Citations

- [Pereira et al. (2021)](/sources/pereira-2021.md) — §I, Fig. 1; §II, Eqs. (1)–(3), Table I; §III; §IV.1–IV.3, Table II, Figs. 8–17; App. A–B, Fig. 18.
- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §III, §IV (Richtmyer–Meshkov scaling with a pre-shock Atwood number).
- [Ruan et al. (2023)](/sources/ruan-2023.md) — §1, §2, §3.1, §3.3, Fig. 3 (Rayleigh–Taylor fingers against Kelvin–Helmholtz turbulence in a flare).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.7, Eq. (32) (single-mode inviscid instability, numerics test).
- [Liang & Fu (2024)](/sources/liang-2024.md) — §4.7, Eq. (60), Fig. 14 (same).
- [Huang et al. (2025)](/sources/huang-2025.md) — §5.7, Fig. 8 (same).
- [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) — §3.1.7, Figs. 19–22 (same, bandwidth-optimized WENO against WENO-JS, WENO-BS, TENO6 and TENO8).
- [Svärd (2022)](/sources/svard-2022.md) — Abstract; §1, §5 (Rayleigh–Taylor test announced in the abstract, not run).
