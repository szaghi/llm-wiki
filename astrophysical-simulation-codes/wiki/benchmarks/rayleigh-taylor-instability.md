---
type: Benchmark
title: "Rayleigh–Taylor instability"
description: "A heavy fluid resting on a light one in a gravitational field, seeded with a single-mode perturbation; it has no unique converged nonlinear solution and is used to compare the fine structure and artefacts of split and unsplit schemes, and, with a magnetic field, the suppression of small scales."
status: established
aliases: [single-mode Rayleigh–Taylor, magnetic Rayleigh–Taylor, RT instability]
tags: [benchmark, hydro, mhd, unsplit, amr, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Rayleigh–Taylor instability

**Set-up.** A dense layer over a light one in hydrostatic equilibrium
under uniform gravity $\mathbf g$, with a small velocity or interface
perturbation of one horizontal mode. Bubbles and spikes grow and roll up
through secondary Kelvin–Helmholtz instabilities. The nonlinear stage has
no unique converged solution
([Stone et al. (2008)](/sources/stone-2008.md), §8.3), so comparisons are
visual. A horizontal magnetic field adds tension that suppresses small
scales.

## Hydrodynamic, single mode

* [Stone et al. (2008)](/sources/stone-2008.md), §8.3, Fig. 18. Liska &
  Wendroff (2003) §4.6: domain $(1/3, 1)$, $|\mathbf g| = 0.1$, densities
  2 over 1, $\gamma = 1.4$, sound speed 1 in the light fluid at the
  interface, vertical velocity perturbation $0.01\sin(6\pi x)$;
  $200\times400$, PPM, HLLC, CTU, $t = 8.5$. Athena shows more fine
  structure than most codes in Liska & Wendroff, but less than
  Lagrange-plus-remap PPM.
* [Almgren et al. (2010)](/sources/almgren-2010.md), §8.3, eqs. 45–47,
  Fig. 9. Densities 2 over 1 g cm⁻³, $|\mathbf g| = 1$ cm s⁻² (downward),
  $\gamma = 1.4$, domain $0.5\times1$ cm, base pressure 5 dyn cm⁻² with
  hydrostatic profile (eq. 45), symmetric cosine interface perturbation of
  amplitude 0.01 cm (eq. 46) smoothed by a tanh of width 0.005 cm
  (eq. 47); $256\times512$, $t = 2.5$ s. Six schemes compared:
  dimensionally split and unsplit, each with PLM, the old PPM limiters and
  the new PPM limiters. All three split variants produce spurious
  secondary instabilities, attributed to alternating compression and
  expansion between sweeps in regions of varying strain. Unsplit PLM and
  unsplit old-limiter PPM show mild anomalies at the bubble and spike
  tips; unsplit new-limiter PPM is cleanest. The unsplit scheme costs about
  twice the CPU time and memory in 2D; in 3D slightly less than twice the
  CPU time and under 10% more memory, thanks to strip-mining.
  Qualitative.

## Magnetic, with AMR

* *2D* ([Stone et al. (2008)](/sources/stone-2008.md), §8.4, Fig. 27).
  Domain $(0.1, 0.2)$, $|\mathbf g| = 0.1$, $\gamma = 5/3$, densities 3
  over 1, a uniform horizontal field at 0.05 times the critical field
  0.14 (the field set by the density jump, gravity and box length), five
  levels on an $8\times16$ base grid (effective $256\times512$), $t = 3$,
  with a passive contaminant. The field suppresses secondary
  Kelvin–Helmholtz instabilities. (The section refers to the hydrodynamic
  test as Fig. 16; it is Fig. 18.)
* *3D* ([Mignone et al. (2012)](/sources/mignone-2012.md), §5.5, eqs. 62–63,
  Figs. 17–18). $x, z \in [-1/2, 1/2]$, $y \in [-3/2, 1/2]$, $\mathbf g = (0, -1, 0)$,
  densities 4 over 1, hydrostatic $p(y) = 100/\gamma - \rho y$ (eq. 62),
  perturbation eq. 63; horizontal field 0, 0.2 and 0.6 times the critical
  field; PPM, Roe, CFL 0.45, characteristic tracing,
  [GLM cleaning](/methods/glm-divergence-cleaning.md); base
  $16\times32\times16$ with 4 levels of ratio 2 or 2 levels of ratio 4
  (effective $256\times512\times256$), density tagging; $t = 3$. Small
  scales are suppressed anisotropically as the field strengthens
  (Fig. 17). Scaling (Fig. 18): the 2-level run is about twice as fast at
  large processor counts; efficiency above 0.8 up to 512 processors, and
  about 0.61 (2 levels) against 0.44 (4 levels) at 1024 cores.

**What it shows.** In hydrodynamics it separates split from unsplit
[integrators](/methods/unsplit-godunov-integrators.md): split sweeps seed
spurious secondary instabilities
([Almgren et al. (2010)](/sources/almgren-2010.md), §8.3). With a field,
both MHD runs show the suppression of small-scale structure, on
[AMR](/methods/adaptive-mesh-refinement.md) meshes.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.3, §8.4.
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §8.3 (arXiv v1).
3. [Mignone et al. (2012)](/sources/mignone-2012.md), §5.5.
