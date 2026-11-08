---
type: Method
title: "Wall models for immersed boundaries"
description: "Near-wall models that let immersed boundary methods compute high-Reynolds-number turbulent flows without resolving the wall layer: all apply a thin-boundary-layer approximation (law of the wall, Reichardt profile, integral relations) between the boundary and a point in the flow, combined in RANS with anisotropic local refinement and in LES mostly without; why the Cartesian grid makes them necessary."
status: established
aliases: [IB wall model, wall-modelled immersed boundary, wall functions for immersed boundaries]
tags: [turbulence, high-reynolds, wall-model, les, rans]
timestamp: 2026-11-08T18:22:00Z
---

# Wall models for immersed boundaries

A Cartesian immersed-boundary grid cannot cluster points in the wall-normal
direction of an arbitrarily oriented surface, so the thin shear layers of
high-Reynolds-number flows are unresolved. [Verzicco (2023)](/sources/verzicco-2023.md)
names this "the main limitation of immersed boundary methods" (summary point 2),
and [Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md), §7, the
inability "to selectively cluster grid nodes in the vicinity of solid
boundaries". The remedies are local grid refinement and wall models; the
grid-size scaling behind the problem is on the
[immersed boundary method](/definitions/immersed-boundary-method.md) page.

## Approaches reviewed by Verzicco (2023)

- All IB-compliant wall models derive from the **thin-boundary-layer
  approximation at the wall**: the velocity at a point at some distance from
  the boundary is related to the wall shear stress by the logarithmic law, a
  composite profile such as Reichardt's, or an integral relation, and the
  result sets the velocity or shear imposed at the boundary.
- Variants cited: Chen et al. (2014); the integral wall model of Yang et al.
  (2015); Bernardini et al. (2016), applied to a rudimentary landing gear;
  Dhamankar et al. (2016), valid only for attached boundary layers; de Tullio
  et al. (2007) with semi-structured local refinement (Durbin and Iaccarino);
  lattice Boltzmann solvers with local refinement next to the boundary.
- **RANS** wall models are almost always combined with anisotropic local
  refinement, which simplifies the near-wall treatment; **LES** wall models
  seldom are. Implementation details, coupling with the numerical method and
  consistency with the outer-layer turbulence model change the quality of the
  results (summary point 3).

Sotiropoulos and Yang (2014, §7) list wall models with LES as having opened
industrial high-Reynolds-number flows to immersed boundaries, and call for
coupling with adaptive mesh refinement.

## Where the limitation does not bite

Microfluidic and miniaturized devices, active interfaces, heat and mass
transfer, phase change and electrolysis have small dimensions and velocities,
so the high-Reynolds-number limitation disappears and the available forcing
schemes apply to the scalar equations as well (Verzicco 2023, summary point 4).

# Citations

- [Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md) — §7.
- [Verzicco (2023)](/sources/verzicco-2023.md) — wall-model and multiphysics sections, summary points.
