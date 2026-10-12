---
type: Benchmark
title: "Relativistic magnetic rotor"
description: "The Del Zanna et al. (2003) special-relativistic MHD rotor: a dense disk spinning at up to 0.995 c in a uniform magnetized medium, whose maximum Lorentz factor drops from about 10 to about 2 by t = 0.4; run with AMR and GLM cleaning in PLUTO and on a uniform GPU grid with constrained transport in GRaM-X, with visual comparison only."
status: established
aliases: [relativistic rotor, RMHD rotor, Del Zanna rotor]
tags: [benchmark, mhd, relativity, verification, amr, constrained-transport, divergence-cleaning]
timestamp: 2026-10-12T00:00:00Z
---

# Relativistic magnetic rotor

**Set-up** (Del Zanna et al. 2003, as printed by both sources). Two
dimensions, $c = 1$. A disk of radius 0.1 with $\rho = 10$ rotates rigidly
with angular velocity 9.95, so its edge moves at 0.995 and the maximum
Lorentz factor is $W \approx 10$; the ambient medium has $\rho = 1$; the
pressure is $p = 1$ and the field $\mathbf B = (1, 0, 0)$ everywhere; the
end time is $t = 0.4$
([Mignone et al. (2012)](/sources/mignone-2012.md), §6.3;
[Shankar et al. (2023)](/sources/shankar-2023.md), §IV C). Both print
$\gamma = 5/3$; Shankar et al. also print the domain $[-0.5, 0.5]^2$ and
no smoothing at the disk edge. There is no exact solution; both sources compare figures.

The non-relativistic rotor (Balsara & Spicer 1999), run by
[Athena](/software/athena.md) ([Stone et al. (2008)](/sources/stone-2008.md),
Figs. 25–26) and [IDEFIX](/software/idefix.md)
([Lesur et al. (2023)](/sources/lesur-2023.md), §4.2, Fig. 9), is a
different test.

## Runs

* *PLUTO-CHOMBO, AMR* ([Mignone et al. (2012)](/sources/mignone-2012.md),
  §6.3, Figs. 26–27). Base $64^2$ with 6 levels (effective $4096^2$),
  HLL, $\nu = 0.5$, refinement tagged on the ratio of the total energy to
  $D$ with threshold 0.15;
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) with
  divergence errors "transported out of the domain at the speed of
  light". The maximum Lorentz factor falls from 10 to about 2.2; the mean
  $|\nabla\cdot\mathbf B|$ grows only to the levels of van der Holst et al.
  (2008). Strong scaling on 8–512 CPUs with maximum box size 16 or 32
  (11,921 and 6735 blocks): AMR 5–10 times faster than a uniform grid,
  efficiency above 0.7 below 256 processors.
* *GRaM-X, uniform grid, GPU* ([Shankar et al. (2023)](/sources/shankar-2023.md),
  §IV C, Fig. 5). $400\times400\times8$ cells ($h = 0.0025$), static flat
  spacetime, [constrained transport](/methods/constrained-transport.md),
  TVD minmod, HLLE, RK4, $\nu = 0.25$ as $\Delta t/h$
  ($\Delta t = 6.25\times10^{-4}$). The maximum $W$ falls to about 1.85,
  the central density to about 0.4, and the field lines rotate by about
  90°. Agreement with Del Zanna et al., GRHydro and a further code is
  visual. 640 iterations took 97 s on one NVIDIA RTX A6000.

The two final maximum Lorentz factors (about 2.2 and 1.85) come from runs
that differ in effective resolution ($4096^2$ with AMR against $400^2$
uniform), integrator, reconstruction and divergence control, and neither
source reports a convergence study; the difference is not evidence against
either code.

**Recorded as printed.** For the 1D cuts Shankar et al.'s text cites
Fig. 8 of the GRHydro paper, while the caption of their Fig. 5 cites
Fig. 6 (§IV C).

# Citations

1. [Mignone et al. (2012)](/sources/mignone-2012.md), §6.3, Figs. 26–27.
2. [Shankar et al. (2023)](/sources/shankar-2023.md), §IV C, Fig. 5 (arXiv v2).
3. [Stone et al. (2008)](/sources/stone-2008.md), Figs. 25–26 (non-relativistic rotor only).
4. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.2, Fig. 9 (non-relativistic rotor only).
