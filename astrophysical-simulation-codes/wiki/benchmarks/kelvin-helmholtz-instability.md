---
type: Benchmark
title: "Kelvin–Helmholtz instability"
description: "The shear-layer instability run in several distinct set-ups — a smooth periodic layer with AMR (Athena++, Quokka), the viscous stratified benchmark of Lecoanet et al. against a spectral reference (Athena, Athena++, AthenaK tracers), Galilean-invariance tests with bulk flows (Castro), and relativistic magnetized layers (PLUTO, Athena++); it tests AMR artefacts, convergence to a reference, and resolution requirements."
status: established
aliases: [KHI, Kelvin-Helmholtz test, shear-layer instability]
tags: [benchmark, hydro, mhd, amr, relativity, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Kelvin–Helmholtz instability

A shear layer between two streams is perturbed, rolls up into vortices
and, at late times, develops secondary instabilities. The sources use
several different set-ups, grouped below; results are comparable
only within one set-up. In the inviscid set-ups the late-time small-scale
structure has no converged reference (see Castro below), so most runs are
judged visually; the Lecoanet et al. set-up is viscous and has a
converged spectral reference.

## Smooth periodic layer with AMR (Athena++ set-up)

**Set-up** ([Stone et al. (2020)](/sources/stone-2020.md), §3.4.3,
eq. 26). Periodic $[-0.5, 0.5]^2$,
$\rho = 1.5 - 0.5\tanh(\vert y - 0.25\vert/0.01)$,
$v_x = 0.5\tanh(\vert y - 0.25\vert/0.01)$,
$v_y = 0.01\cos(4\pi x)\exp[-(y - 0.25)^2/0.2^2]$ (layer thickness 0.01,
perturbation amplitude 0.01 and width 0.2, as printed), $p = 2.5$,
$\gamma = 1.4$; the MHD version adds $B_x = 0.1$.

**Runs.**
* [Stone et al. (2020)](/sources/stone-2020.md), §3.4.3, Figs. 21–22,
  Table 1. [Athena++](/software/athena-plus-plus.md), VL2, PLM, HLLC
  (hydro) or HLLD (MHD); uniform $2048^2$ against
  [AMR](/methods/adaptive-mesh-refinement.md) with root $256^2$ and 4
  levels, blocks of $8^2$ or $16^2$, refined on a shear criterion. The
  densities are indistinguishable: maximum density difference 0.70–1.59 %,
  mean 0.044–0.060 %. Sound waves are damped in coarse regions, so AMR
  "cannot be used" where such waves matter. Times on 32 Skylake 6148
  cores: hydro 319 s uniform against 319 s ($8^2$ blocks) and 152 s
  ($16^2$); MHD 883 s against 688 s and 387 s.
* [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.8, Fig. 7,
  eqs. 52–54. [Quokka](/software/quokka.md), the same parameters (layer
  thickness 0.01, perturbation width 0.2 and amplitude 0.01, $p = 2.5$,
  $\gamma = 1.4$) after Stone et al. (2020); hydro only; refinement where
  the relative density gradient exceeds 0.2; 4 levels on a $2048^2$ base,
  peak effective $32{,}768^2$, $128^2$ local grids; $t = 1.5$, CFL 0.4.
  It ran on a single GPU in about 4.5 h and shows no visible artefacts at
  level boundaries. Qualitative only.

## Viscous stratified layer of Lecoanet et al.

**Set-up.** The Lecoanet et al. benchmark with density contrast 1 and
equal viscosity, conductivity and dye diffusivity, so that a converged
reference exists from the spectral code Dedalus. Stone et al. (2020)
cite it as Lecoanet et al. 2015, Stone et al. (2026) as Lecoanet et al.
2016 (as printed).

**Runs.**
* [Stone et al. (2020)](/sources/stone-2020.md), §3.3.6, Fig. 18.
  Viscosity, conductivity and dye diffusivity $2\times10^{-5}$,
  Reynolds number $10^5$, $\nu = 0.4$, primitive reconstruction, HLLC.
  Athena++ with RK3+PPM converges to the Dedalus solution at
  $8192\times16384$, half the linear resolution that
  [Athena](/software/athena.md) (CTU+PPM, operator-split diffusion) needed
  ($16384\times32768$). VL2+PLM at $4096\times8192$ shows an instability of
  the inner vortex at $t = 4$.
* [Stone et al. (2026)](/sources/stone-2026.md), §4.1, Fig. 18.
  [AthenaK](/software/athenak.md), Lecoanet et al. (2016) set-up with
  background pressure 10, shear velocity 1, perturbation width 0.2 and
  amplitude 0.01; LLF, PLM, RK2; $512\times1024$ on
  $[-0.5, 0.5]\times[-1, 1]$. Used to test $10^7$ Lagrangian Monte Carlo
  tracer particles against a passive scalar at $t = 2$ and 3: the tracers
  are "more diffusive". Visual; no comparison with Dedalus.

## Bulk-flow (Galilean-invariance) variants

**Runs.** [Katz et al. (2016)](/sources/katz-2016.md), §4.3.1, Figs. 7–9,
with [Castro](/software/castro.md).
* Robertson et al. (2010) initial conditions A and B: 2D $[0, 1]^2$,
  densities 1 and 2, velocities $-0.5$ and $0.5$, $p = 2.5$,
  $\gamma = 5/3$ (sound speed about 0.7); a bulk velocity of 0, 1, 3, 10,
  30 or 100 (about Mach 70) along $y$; $64^2$ to $512^2$, with stationary
  references at $1024^2$, $2048^2$ and $4096^2$; to $t = 2$. With the
  sharp interface (A, the Springel 2010 test) the instability "completely
  fails to develop" at low resolution and high bulk speed, and the problem
  does not converge even qualitatively. With the smooth ramp (B) the
  disruption "quickly converges away" and the $512^2$ result is nearly
  identical to the one without bulk flow.
* McNally et al. (2012) initial conditions, same resolutions and speeds:
  higher bulk speeds need higher resolution. Run to $t = 10$, the layer
  damps at low resolution and disrupts at high resolution; at
  $1024^2$–$4096^2$ the secondary instabilities appear at different times
  and scales ($t = 3.0$–3.6), so no converged late-time reference exists.
  The authors decline to read this as a deficiency of fixed grids.

## Relativistic magnetized layers

**Runs.**
* [Mignone et al. (2012)](/sources/mignone-2012.md), §6.6, Figs. 31–32.
  [PLUTO](/software/pluto.md), after Bucciantini & Del Zanna (2006) and
  Mignone et al. (2009): $[0, 1]\times[-1, 1]$, $\rho = 1$, $p = 20$, shear
  velocity 1/4, Taub–Mathews equation of state, poloidal and toroidal
  magnetizations 0.01 and 1; base $32\times64$ with 6 levels (effective
  $2048\times4096$), Courant number 0.8, refinement on total energy;
  $t = 5$. AMR is about 40 times faster than the uniform grid; 3 levels
  of ratio 4 do somewhat better than 6 levels of ratio 2; parallel
  scaling degrades below 3–4 blocks per processor.
* [Stone et al. (2020)](/sources/stone-2020.md), §4.3.2, Figs. 38–39.
  Athena++, after Mignone et al. (2012): $\rho = 1$, $p = 20$,
  $B_x = \sqrt{2/5}$, $B_z = 10\sqrt{2/5}$,
  $v_x = \tfrac14\tanh(100y)$,
  $v_y = \tfrac{1}{400}\sin(2\pi x)\exp(-100y^2)$, ideal gas with
  adiabatic index 4/3 (where Mignone et al. used Taub–Mathews); root
  $64\times32$ with $16^2$ blocks and up to 5 levels; VL2+PPM, HLLE or
  HLLD, $\nu = 0.4$, $t = 5$. The choice of
  [Riemann solver](/methods/approximate-riemann-solvers.md) shifts the
  rolls, and many small-scale features are artefacts of fine/coarse
  boundaries, absent from a uniform $4096\times2048$ run with a smooth
  vortex. AMR costs 32.2 core-hours against 251 uniform (×7.8, 2 KNL
  nodes).

**Note.** The two relativistic set-ups differ in domain and equation of
state, so the PLUTO and Athena++ AMR speed-ups (about 40 and 7.8) are not
comparable.

## What it shows

* AMR reproduces the uniform-grid roll-up in the smooth set-ups (Athena++
  to about 1 % in density; Quokka with no visible artefacts) but damps
  sound waves on coarse levels and, in the relativistic magnetized case,
  creates small-scale artefacts at level boundaries (Stone et al. 2020).
* Against a converged spectral reference, a less dissipative scheme
  reaches convergence at half the linear resolution (Athena++ RK3+PPM
  against Athena CTU+PPM).
* With sharp initial interfaces or long run times there is no converged
  reference, and conclusions are qualitative (Katz et al. 2016).

## Later uses (batch 4)

### Shear instabilities in a moving-mesh production run

[Ohlmann et al. (2016)](/sources/ohlmann-2016.md) do not run a
Kelvin–Helmholtz test; they report the instability in an application, the
common-envelope spiral-in computed with the moving-mesh code AREPO, and
attribute its appearance to the code's Galilean invariance.
* **What is observed** (§3, Figs. 1–4). Large-scale Kelvin–Helmholtz
  instabilities develop between adjacent spiral shocks in the envelope.
  Recorded as printed: the abstract places them "after about 20 orbits",
  while §3 places the first instabilities at about 7 orbits (40 d) and the
  large-scale overlap at 90 d. About $1.8\times10^6$ cells at the start and
  $2.7\times10^6$ at the end (§2). No run at a second resolution and no
  resolution study of the instability are presented.
* **The attribution** (§3, last paragraph; §4). "The violation of Galilean
  invariance in conventional grid-based hydrodynamics codes (when altering
  the background velocity at the same resolution) suppresses
  Kelvin-Helmholtz instabilities on a static mesh", illustrated by
  Springel (2010), Fig. 33; AREPO's scheme "is Galilean invariant, thus,
  shear instabilities may also develop on top of background velocities".
  The absence of the instability in the earlier grid simulations of Passy
  et al. (2012) is attributed to their background velocity field, and in
  their SPH simulations to numerical diffusion. Both attributions are
  stated as a suspicion ("We suspect") and are not tested.

**Relation to the bulk-flow runs above — a qualification, not a
contradiction.** Ohlmann et al. restrict their claim to fixed resolution
and support it with the Springel (2010) sharp-interface test, which is
Katz et al.'s IC A; for IC A Katz et al. likewise find that the
instability "completely fails to develop" at low resolution and high bulk
speed. Katz et al.'s finding that the disruption "quickly converges away"
holds for the smooth IC B, and their refusal to call the McNally et al.
behaviour a deficiency of fixed grids concerns the late-time secondary
instabilities. Neither source measures the effect in a common-envelope
configuration, so the two do not make incompatible claims about the same
thing. What remains open is whether the grid runs of Passy et al. (2012)
were in the under-resolved regime where the suppression occurs; Ohlmann
et al. do not show it.

# Citations

1. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.6, §3.4.3, §4.3.2.
2. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.8 (arXiv v2).
3. [Stone et al. (2026)](/sources/stone-2026.md), §4.1 (arXiv v1).
4. [Katz et al. (2016)](/sources/katz-2016.md), §4.3.1 (arXiv v2).
5. [Mignone et al. (2012)](/sources/mignone-2012.md), §6.6.
6. [Ohlmann et al. (2016)](/sources/ohlmann-2016.md), §§2–4, Figs. 1–4 (arXiv v1).
