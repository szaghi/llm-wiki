---
type: Definition
title: "Sharp and diffuse interface representations"
description: "The classification of immersed boundary methods by whether the boundary is smeared over a band of grid cells (diffuse: regularized delta functions, Gaussian spreading, penalization masks) or kept a codimension-one set that the discrete equations see exactly (sharp: jump-corrected stencils, ghost values, cut cells, reconstruction at forcing points)."
status: established
aliases: [sharp interface, diffuse interface, smeared boundary, sharp-interface method, diffused-interface method]
tags: [immersed-boundary, classification, accuracy]
timestamp: 2026-11-08T18:22:00Z
---

# Sharp and diffuse interface representations

An [immersed boundary method](/definitions/immersed-boundary-method.md) is
**diffuse** when the boundary $\Gamma$ acts on the grid through a band of
cells of width $O(h)$ around it, and **sharp** when the discrete equations
distinguish the two sides of $\Gamma$ at the grid scale, so that no grid value
mixes information from both sides through a smoothing kernel.

- **Diffuse.** The [classical method](/methods/classical-immersed-boundary-method.md)
  spreads the singular force with a [regularized delta function](/operators/regularized-delta-function.md)
  of support $4h$ ([Peskin 1972](/sources/peskin-1972.md), §III.B;
  [Peskin 2002](/sources/peskin-2002.md), §6). [Goldstein et al. (1993)](/sources/goldstein-1993.md)
  spread their feedback force with a narrow Gaussian because point forces in
  a spectral method produce global oscillations. [Volume penalization](/methods/volume-penalization.md)
  marks the body with the mask $\chi_s$, which on a grid is a staircase or a
  smoothed indicator ([Angot et al. 1999](/sources/angot-1999.md)).
- **Sharp.** The [immersed interface method](/methods/immersed-interface-method.md)
  builds the jumps $[u]$ and $[\beta\partial_n u]$ into the stencil
  ([LeVeque & Li 1994](/sources/leveque-1994.md)); the
  [ghost fluid method](/methods/ghost-fluid-method.md) gives each fluid its
  own ghost values across the level set and keeps the density profile a
  Heaviside step ([Fedkiw et al. 1999](/sources/fedkiw-1999.md)); the
  [cut-cell method](/methods/cut-cell-method.md) clips the control volumes
  at $\Gamma$ ([Pember et al. 1995](/sources/pember-1995.md);
  [Ye et al. 1999](/sources/ye-1999.md)); and [direct forcing](/methods/direct-forcing.md)
  with linear reconstruction imposes the boundary value at the grid point
  nearest to $\Gamma$ ([Fadlun et al. 2000](/sources/fadlun-2000.md), §2.3;
  [Kim et al. 2001](/sources/kim-2001.md), §2.2).

## Why the distinction matters

1. **Accuracy.** Across a true interface the velocity is continuous but its
   normal derivative jumps; smoothing the jump over $O(h)$ limits a diffuse
   method to first order ([first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)).
2. **Coupled dynamics.** Ye et al. (1999, §1) argue, citing Udaykumar et al.,
   that smearing "can adversely impact the dynamics of flows where the
   boundary motion is closely coupled with the evolution of surrounding fluid
   field", and that a sharp representation suits high-Reynolds-number flows
   with thin boundary layers.
3. **Material interfaces.** In multimaterial compressible flow a smeared
   density with a different equation of state on each side produces spurious
   pressure oscillations ([Fedkiw et al. 1999](/sources/fedkiw-1999.md), §1).

## Qualifications

- Fadlun et al. (2000, §2.3) show that the *interpolation* of the forcing,
  not the forcing law, sets the accuracy: a stepwise boundary is less than
  first order, volume-fraction weighting first order, linear reconstruction
  second order. The same forcing law can therefore be diffuse or sharp.
- Peskin (2002, §6) notes that the smoothing is what lets an elastic boundary
  move through the grid without jumps in the interpolated velocity or the
  applied force as Lagrangian points cross grid lines.

## Tracking versus representation

[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) separate how a method
*tracks* the boundary from how it *represents* its effect: Peskin's method
tracks a sharp Lagrangian boundary but represents it diffusely; cut-cell and
ghost-cell methods are sharp in both; volume-of-fluid is diffuse in both. In
their account the smoothing of continuous forcing prevents a sharp boundary,
"especially undesirable for high Reynolds number flows", while discrete forcing
with direct imposition keeps it sharp and decouples the solid nodes from the
fluid. [Ghias et al. (2007)](/sources/ghias-2007.md), §1, and
[Mittal et al. (2008)](/sources/mittal-2008.md), §1, define a diffuse boundary
as one where the condition "is not precisely satisfied at its actual location
but within a localized region around the boundary". Smearing also has a
benefit: diffuse methods have no [fresh-cell problem](/definitions/fresh-cell-problem.md).

## Later statements

[Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md), §3, build their
review on the diffused/sharp split; in their account the reconstruction of
sharp methods enters the intermediate velocity, so a mass-conservation
correction is needed in the projection. [Griffith & Patankar (2020)](/sources/griffith-2020.md)
show what smearing does physically: for a cylinder at $Re=200$ a regularized-delta
immersed boundary generates spurious fluid motion *inside* the body, because the
interface moves with a local average of the velocity, so the exterior flow
drives a counter-rotating interior flow; an immersed interface computation,
which reconstructs the velocity-derivative jump, removes it.

## Compressible evidence

[Ménez et al. (2023)](/sources/menez-2023.md) find that a continuous-forcing
immersed boundary method "is not able to properly reproduce the downstream part
of a supersonic flow past a wedge" because the artificial flow inside the
boundary contaminates the external flow, the compressible analogue of the
spurious interior flow noted by Griffith and Patankar.

# Citations

- [Peskin (1972)](/sources/peskin-1972.md) — §III.B.
- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — spectral implementation (Gaussian spreading, spectral oscillations).
- [LeVeque & Li (1994)](/sources/leveque-1994.md) — §1, §5 Example 1.
- [Pember et al. (1995)](/sources/pember-1995.md) — §2.
- [Fedkiw et al. (1999)](/sources/fedkiw-1999.md) — §1, §3.
- [Ye et al. (1999)](/sources/ye-1999.md) — §1.
- [Angot et al. (1999)](/sources/angot-1999.md) — §3.
- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §2.3.
- [Kim et al. (2001)](/sources/kim-2001.md) — §2.2.
- [Peskin (2002)](/sources/peskin-2002.md) — §6.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — continuous- and discrete-forcing sections, moving boundaries.
- [Ghias et al. (2007)](/sources/ghias-2007.md) — §1.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §1.
- [Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md) — §3.
- [Griffith & Patankar (2020)](/sources/griffith-2020.md) — benchmarks.
- [Ménez et al. (2023)](/sources/menez-2023.md) — conclusions.
