---
type: Source
title: "Teschner & Mundt (2022) — Fully conservative overset mesh to overcome the blunt body metric singularity"
description: "Removes the axis metric singularity of a curvilinear finite-difference blunt-body solver by a small hexahedral overset mesh around the symmetry line whose calculation points coincide with those of the body mesh, so that values are copied rather than interpolated, tested on a supersonic hemisphere cylinder in two and three dimensions."
resource: "doi:10.1007/s00193-022-01078-2"
source_kind: paper
authors: [Teschner F., Mundt C.]
year: 2022
venue: "Shock Waves 32:295-312"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_Shock_Waves_Teschner_Fully_conservative_overset_mesh_to_overcome_the_blunt_body_m.pdf"
tags: [finite-difference, compressible, conservation, overset-grid]
timestamp: 2026-11-02T15:05:00Z
---

# Summary

A body-orientated mesh of a blunt body, built by rotating a meridian plane, collapses all circumferential lines onto the symmetry axis, where $J^{-1}=0$ and the conservative curvilinear equations cannot be solved. Teschner & Mundt place a small hexahedral overset mesh around the axis whose calculation points coincide with points of the body mesh, so the two meshes exchange values by direct copy; the overset mesh also supplies the body mesh's metric on the axis. The authors call it fully conservative, borrowing the point-continuous patched-grid argument ([patched grids](/definitions/patched-grid.md)). It is the main example of [interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md) here, alongside the [conservative overset interface](/methods/conservative-overset-interface.md) of Wang (1995), which the authors note works only for finite volumes. Tested in CONSST3D on a supersonic hemisphere cylinder ([shock capturing](/methods/shock-capturing-on-overset-grids.md)).

# Version read

Version of record (Springer typeset, open access), 18 pages, all read. Page 1 matches the Crossref record.

# Key claims

1. On the symmetry axis $x_{1\eta}=x_{2\eta}=x_{3\eta}=0$ and $J^{-1}=0$, so the conservative variables and fluxes, all carrying $J^{-1}$, vanish there (§2). **Derived**
2. Earlier fixes modify the equations or exclude the axis and fill it by averaging or extrapolation, which is not conservative; interpolation-coupled overset meshes are not conservative either; Wang's conservative overlapped-grid interface works only for finite volumes (§1). **Stated**
3. The overset mesh's calculation points coincide with body-mesh points, so variables are copied with no interpolation; in 2-D axisymmetric runs the coincident points come from rotating the median plane, in 3-D from a Harder–Desmarais surface spline on each $\zeta$ surface, with coordinate mismatch $2\times10^{-12}$ (§3, Eqs. (19)–(21)). **Stated**
4. The overset-mesh metric supplies the body mesh's metric on the axis, so the half-point flux at $i=1/2$ can be formed (§3, Eq. (22)). **Derived**
5. The method is called "fully conservative" because the meshes share points; the evidence is the conservation of total enthalpy within 0.03 % (2-D) and 0.09 % (3-D, angle of attack $-5^\circ$) and a stagnation temperature 2.72878 deviating $2.199\times10^{-3}$ % from the inviscid value; no discrete flux balance is given (§4). **Shown** / **Stated**
6. Hemisphere cylinder at $M_\infty=2.94$, $Re_\infty=2.2\times10^5$: wall pressure and temperature agree with Esfahanian et al.; small oscillations on the axis in 3-D at $-5^\circ$ vanish at $-10^\circ$ (§4). **Shown**
7. Mesh adaption in the solver interpolates non-conservatively (§3). **Stated**

# Printed slips

- Eq. (18) uses $i$ for the circumferential index, which elsewhere is the tangential index with $i=0$ on the axis.
- Typos "point-discontinues", "gird surface", "needs to be build"; ref. [16] prints the publisher as "RC Press".
- The paper's $J^{-1}$ has the opposite sign to $\det(\partial\mathbf x/\partial\boldsymbol\xi)$; this is a sign convention, consistent within the paper.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| body-orientated mesh, overset mesh | $G_k$, the axis grid $G_{k'}$ | |
| $J^{-1}$ | cell volume (registry $J=\det(\partial\boldsymbol\xi/\partial\mathbf x)$) | opposite sign convention |
| calculation points, metric points | grid points; auxiliary points for the metric | |

# Reference list

35 printed references, numbered, merged complete into the [bibliography](/bibliography.md) with `citedby` teschner-2022. [Wang (1995)](/sources/wang-1995.md) is cited, and also Wang's AIAA Paper 95-0077 (`wang-1995-b`). No printed duplicates.

# Pages created or updated

Chunk 3 (2026-11-02). This source is cited on:

- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Patched (zonal) grids](/definitions/patched-grid.md)
- [Adaptive mesh refinement on overlapping grids](/methods/amr-on-overset-grids.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
