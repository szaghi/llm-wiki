---
type: Source
title: "Chandar & Sitaraman (2022) — A flux correction approach for the pressure equation in incompressible flows on overset meshes"
description: "Derives the discrete global mass-conservation condition of the pressure equation of a pressure-correction finite-volume solver on overset meshes and imposes it implicitly at one flux-balance cell, recovering machine-level conservation, second order in 1-D and lower errors in 2-D for inverse-distance, polynomial and RBF interpolation."
resource: "doi:10.1016/j.cpc.2021.108279"
source_kind: paper
authors: [Chandar D.D.J., Sitaraman J.]
year: 2022
venue: "Comput. Phys. Commun. 273:108279"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_Computer_Physics_Communications_Chandar_A_flux_correction_approach_for_the_pressure_equation_in_inco.pdf"
tags: [incompressible, conservation, finite-volume, interpolation, overset-grid]
timestamp: 2026-11-02T15:02:00Z
---

# Summary

In a pressure-correction (SIMPLE/PISO-type) incompressible solver the pressure equation alone decides mass conservation. On overset meshes the interpolation at receptors does not make the fluxes on the two sides of the overlap match, so a global mass defect appears. Chandar & Sitaraman isolate the simplified Poisson problem $\nabla^2p=\nabla\cdot\mathbf u^*$, derive the discrete global conservation condition over all overset interfaces, and impose it implicitly by replacing the interpolation row of one receptor, the **flux-balance cell**, with that condition. The result is a [conservative overset interface](/methods/conservative-overset-interface.md) for the pressure equation of [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md), tested with inverse-distance, polynomial and radial-basis-function [inter-grid interpolation](/methods/inter-grid-interpolation.md) in OpenFOAM ([OpenFOAM](/software/openfoam.md)), on manufactured Poisson problems, a rotating inner mesh ([moving overset grids](/methods/moving-overset-grid.md)) and a Stokes [lid-driven cavity](/benchmarks/lid-driven-cavity.md).

# Version read

Version of record (Elsevier typeset), 20 pages, all read. Page 1 matches the Crossref record.

# Key claims

1. Distance-weighted or least-squares interpolation between overset finite-volume meshes is non-conservative; the global flux imbalance acts as a source or sink and appears as reduced order or as pressure oscillations on moving meshes (Abstract, §1). **Stated**
2. Summing the 1-D finite-volume Poisson discretization over the field cells of both meshes gives a balance that holds for any interpolation; equating it with the single-mesh balance requires $\nabla p_{O1}-\nabla p_{O2}=f(L_1+L_2-L)$ at the overset interfaces (§3.1, Eqs. (17)–(20)). **Derived**
3. Imposing that condition while interpolating at every receptor over-determines the system; interpolating at all receptors but one and imposing the condition at the remaining **flux-balance cell** closes it (§3.1, Eqs. (21)–(30)). **Derived**
4. In several dimensions the condition is $\sum_O\nabla p\cdot d\mathbf S=\sum_O\mathbf u^*\cdot d\mathbf S$ over all overset interfaces (Eq. (37)); for the full momentum-weighted pressure equation it is Eq. (38). Imposing $\sum_O\mathbf u^*\cdot d\mathbf S=0$ instead is incorrect, $\mathbf u^*$ being an intermediate field (§3.3–3.4). **Derived**
5. The constraint row is dense; it is assembled in compressed row storage and solved with BiCGStab (ITSOL), because the OpenFOAM matrix format cannot hold it (§3). **Stated**
6. 1-D manufactured problem ($k=3$): inverse-distance interpolation degrades the global order to 1 and the correction restores 2; quadratic (polynomial) interpolation gives order 2 with or without it (§3.6, Figs. 8–9). **Shown**
7. 2-D static inner mesh ($k=7/2$): the correction lowers the finest-mesh error about 6× (inverse distance) and 3× (polynomial) but improves the order only marginally; RBF interpolation keeps second order either way (§3.7.1, Figs. 14–16). **Shown**
8. The authors attribute the 1-D/2-D difference to the number of overset interfaces, fixed in 1-D but growing with refinement in 2-D (§3.7.1). **Stated** (hypothesis)
9. Global mass error on the coarse RBF mesh: uncorrected overset stalls near $-9.5\times10^{-5}$ for solver tolerances from $10^{-15}$ to $10^{-8}$; corrected overset tracks the tolerance ($-1.48\times10^{-16}$ at $10^{-15}$), as a single mesh does (§3.7.2, Table 3). **Shown**
10. Wider overlap reduces the number of receptors and the $L_2$ error; the corrected variant is lower at every overlap width (§3.7.3, Fig. 20). **Shown**
11. The choice of the flux-balance cell changes the error strongly for inverse distance and hardly for polynomial and RBF interpolation (§3.7.5, Fig. 24). **Shown**
12. Rotating inner mesh ($\omega=4\pi$ rad/s): the force error oscillates with the number of receptors, as cells switch status; RBF has two orders of magnitude lower force error than inverse distance, and the correction reduces the oscillation magnitude (§3.7.6, Figs. 25–27). **Shown**
13. BiCGStab iterations to $10^{-15}$ are essentially unchanged by the dense row (Table 4); in the Stokes cavity the time per cell per iteration is 0.198 ms (single mesh), 0.318 and 0.319 ms (overset RBF without and with the correction) (§3.7.7, §3.8, Table 5). **Shown**
14. Stokes long cavity: the result depends on where the flux-balance cell is placed; on a low-velocity interface the upper inner streamlines change, on a higher-velocity interface the single-mesh result is reproduced; the authors do not fully explain why (§3.8, Figs. 32–34). **Shown**
15. RBF interpolation needs at least 9 donor cells in 2-D; a quadratic interpolant needs 3 donors in 1-D and its Vandermonde system can become singular in more dimensions (§3.5.2, §3.7.1). **Stated**

# Printed slips

- §3.8: the cavity is described as of height 5 and width 1, while the background mesh is printed as $0\le x\le5$, $0\le y\le1$ and the refinement mesh as $0.3\le x\le0.6$, $3\le y\le4$, outside the printed background in $y$; one set of coordinates is transposed *(compiler check, not in the sources)*.
- The size of the RBF system is printed $(N+K,N)$ in the text and $(N,N+K)$ in Eq. (49).
- Eq. (58) lacks brackets and the $\cdot d\mathbf S$ factor.
- The meshes are numbered 1/2 in §3.1 and 0/1 in §3.6 and Fig. 4.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overset interface $O$ | face between a field cell and a receptor | |
| interpolation cell, $g_1$, $g_2$ | receptor ($\mathcal R_k$) | |
| flux balance cell | one receptor whose row carries the conservation constraint | |
| $\mathbf u^*$ | predicted velocity of the fractional step | |
| $\mathbf H$, $a_O$ | off-diagonal momentum operator and diagonal coefficient | pressure-correction notation |

# Reference list

43 printed references, numbered, merged complete into the [bibliography](/bibliography.md) with `citedby` chandar-2022. Ref. [9], printed with given names first, is `mader-2020` (ADflow; authors from Crossref, DOI 10.2514/1.I010796). Chesshire & Henshaw (1990) is cited as ref. [40]. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-11-02). This source is cited on:

- [Lid-driven cavity](/benchmarks/lid-driven-cavity.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [OpenFOAM (overset)](/software/openfoam.md)
