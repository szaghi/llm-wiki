---
type: Method
title: "Interpolation-free overset coupling"
description: "Coupling overlapping grids without interpolating at receptors: either by turning the overlap into a patched interface on which fluxes are matched, or by making the two grids share points so that values are copied; both remove the interpolation error and are claimed conservative, at the price of constraining the grids."
status: established
aliases: [point-coincident overset mesh, fully conservative overset mesh]
tags: [conservation, overset-grid, finite-difference, finite-volume]
timestamp: 2026-11-02T15:26:00Z
---

# Interpolation-free overset coupling

Interpolation at [fringe points](/definitions/fringe-point.md) is the source of the conservation defect of overset grids ([conservative overset interface](/methods/conservative-overset-interface.md)). Two sources avoid it altogether.

## Overlap turned into a patched interface

[Wang (1995)](/sources/wang-1995.md) uses one overlapping boundary as a new internal boundary of the other grid, turning the overlapped pair into two [patched](/definitions/patched-grid.md) zones whose common boundary is a zonal interface; fluxes are then matched on it with cut cells, and the scheme is conservative for cell-centred finite volumes (§2). The grids may still be generated independently.

## Shared points, copied values

[Teschner & Mundt (2022)](/sources/teschner-2022.md) remove the metric singularity on the symmetry axis of blunt-body meshes ($J^{-1}=0$ on the axis) with a small hexahedral overset mesh around the axis whose calculation points coincide with points of the body mesh, so values are copied with no interpolation (§3); coincidence is exact in 2-D axisymmetric runs and to $2\times10^{-12}$ in 3-D, where the overset coordinates come from a surface spline (Eqs. (19)–(21)). The overset mesh's metric also supplies the body mesh's metric on the axis (Eq. (22)). The authors call the method "fully conservative" by analogy with point-continuous patched grids; the evidence is total-enthalpy conservation within 0.03 % (2-D) and 0.09 % (3-D) on a supersonic hemisphere cylinder (§4).

## Related flux-based coupling

[Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) also avoid fringe interpolation, with a compact hybrid stencil that lets finite-volume fluxes carry information between the grids ([ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md)).

## Virtual faces between overlapping cells

[Devlin et al. (2023)](/sources/devlin-2023.md) generalize the finite-volume method to overlapping control volumes (a form first derived for a meshless method): cell volume is distributed by a characteristic top-hat weight function normalized to a partition of unity, so overlapping cells share volume, intercell areas emerge, and fluxes pass between overlapping cells through virtual faces of defined area. The scheme is conservative by construction and needs no interpolation, no overset grid assembly and no external library; on 1-D diffusion it converges at second order, on the [lid-driven cavity](/benchmarks/lid-driven-cavity.md) it resolves a tertiary vortex that interpolated overset misses on a coarse grid, and volume-of-fluid cases conserve liquid mass where interpolated overset loses it ([multiphase flow](/methods/multiphase-flow-on-overset-grids.md)).

## Qualifications

- The two meanings of "conservative" differ: Wang (1995) shows a discrete flux balance across the interface (mass imbalance $6\times10^{-6}$ % printed, Table I), while Teschner & Mundt (2022) give no discrete flux-balance argument and rely on shared points and enthalpy conservation; they also state that the solver's mesh adaption interpolates non-conservatively (§3).
- Teschner & Mundt (2022) note that Wang's interface works only for finite volumes, which motivated their finite-difference approach (§1).

# Citations

- [Wang (1995)](/sources/wang-1995.md) — §2, Table I.
- [Teschner & Mundt (2022)](/sources/teschner-2022.md) — §1–§4, Eqs. (19)–(22).
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §1, §4.
- [Devlin et al. (2023)](/sources/devlin-2023.md) — Abstract, §2, §4, Conclusions.
