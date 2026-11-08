---
type: Source
title: "Pember et al. (1995) — An adaptive Cartesian grid method for unsteady compressible flow in irregular regions"
description: "Embedded-boundary (cut-cell) method for the time-dependent Euler equations: volume and area fractions describe the body on a Cartesian grid, an unsplit Godunov predictor ignores the body, a conservative but unstable cut-cell correction is replaced by a stable non-conservative update whose deficit is redistributed, mass-weighted, to neighbours; coupled to block-structured adaptive mesh refinement in 2-D, axisymmetric and 3-D."
resource: "doi:10.1006/jcph.1995.1165"
source_kind: paper
authors: [Pember R.B., Bell J.B., Colella P., Crutchfield W.Y., Welcome M.L.]
year: 1995
venue: "J. Comput. Phys. 120(2):278-304"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/1995_Crossref_Journal_of_Computational_Physics_Pember_An_Adaptive_Cartesian_Grid_Method_for_Unsteady_Compressible.pdf"
tags: [cut-cell, embedded-boundary, redistribution, compressible, amr, small-cell]
timestamp: 2026-11-08T17:46:00Z
---

# Summary

Pember, Bell, Colella, Crutchfield and Welcome treat a body as an interface
embedded in a regular Cartesian mesh in a volume-of-fluid manner
([cut-cell method](/methods/cut-cell-method.md)). Each explicit step computes
second-order unsplit Godunov fluxes as if the body were absent, then
corrects the cut cells: the conservative update is unstable in small cells
([small-cell problem](/definitions/small-cell-problem.md)), so a stable
non-conservative update is used and the conservation deficit is
redistributed, mass-weighted, to the 26 neighbours
([redistribution](/methods/redistribution.md)), restoring
[discrete conservation](/properties/discrete-conservation.md) with a
full-cell time step. The scheme is coupled to conservative block-structured
adaptive mesh refinement. Results suggest global second order and first
order at the boundary for smooth flow.

# Version read

Version of record, J. Comput. Phys. 120, 278–304 (1995), 27 pages. The PDF
is an image-only scan, read through OCR (tesseract, 300 dpi): the prose of
§§1–3 and §2.6 in full, §4 (results) in outline; most display equations,
including the preliminary update and the redistribution formulas (2.6)–(2.29),
are illegible in the OCR and are described here in words only. The page-1
title and authors match Crossref, except that Crossref spells the fourth
author "Curtchfield"; page 1 prints **Crutchfield**, used here.

# Key claims

1. Cartesian grid methods avoid metric terms and body-fitted interpolation difficulties, and need geometry only on a set of codimension one (§1). **Stated**
2. The design problem is maintaining accuracy, stability and conservation in irregular cells with a time step set by the regular cells, and coupling to adaptive refinement (§1). **Stated**
3. Literature placement: cell merging (Chiang et al., Bayyuk et al., Quirk; Coirier and Powell found merging more efficient than small-cell time stepping, both globally second order), LeVeque's large-time-step and Berger–LeVeque's rotated schemes (globally second order, between first and second at the boundary) (§1). **Stated** (cited)
4. The geometry is given by volume fractions, face area fractions and an effective surface normal per cut cell; its generation was not automated (§1.4, Figs. 1–2). **Stated**
5. The cut-cell conservative update is "correct and conservative but potentially unstable"; a stable non-conservative update is followed by redistribution of the deficit (§2). **Stated**
6. The wall flux uses the pressure of a 1-D Riemann problem with the normal velocity reflected (§2.5). **Stated**
7. For a stationary reflecting wall the whole deficit is redistributed to the cut and fluid cells among the 26 neighbours; mass-weighted redistribution was superior to volume-weighted redistribution with strong shocks, using the preliminary density (§2.6). **Shown** (numerical experience)
8. Redistribution is equivalent to modifying the edge fluxes, hence fully conservative (§2.6). **Stated**
9. Stability of redistribution is not proved (here or by Chern and Colella); heuristically, only full-cell volumes appear as divisors (§2.6.1). **Stated**
10. Distinct fluid regions must be separated by at least one full body cell, and each cut cell needs enough fluid neighbours (§2.6.1, Fig. 3). **Stated**
11. The axisymmetric version uses a volume-coordinate form that is free-stream preserving (§2.7). **Stated**
12. The AMR coupling keeps the geometry consistent across levels and adds a re-redistribution step for redistribution across coarse–fine boundaries (§3). **Stated**
13. Smooth flows: globally second order, first order at the boundary (Abstract, §1, as numerical suggestion). Shock reflection on a ramp: about first-order $L^1$ convergence, with somewhat larger errors near the Mach stem for the Cartesian representation than for a reflecting-wall boundary (§4.1). **Shown**
14. Further tests: Mach 10 flow past a 30° ramp with an inclined interface, axisymmetric flow past a cone (density undershoot along the cone, attributed to the wall-heating error of shock capturing) and 3-D flow past a cone-cylinder at $M_\infty=2.33$ with AMR (§4). **Shown**

# Notation map

| Pember et al. (1995) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Lambda_{ijk}$ (volume fraction) | $\kappa_{\mathbf i}$ | |
| face area fractions | $a_{\mathbf i+\frac12\mathbf e_m}$ | |
| $\mathbf U$ | $\mathbf q$ | conserved variables |
| $F$, $G$, $H$ | $\boldsymbol{\mathcal F}$ components | fluxes |
| $U^{\mathrm{ref}}$, conservative update | $\mathbf q^{\mathrm{ref}}$, $\mathbf q^{\mathrm c}$ | |
| $\delta M_{ijk}$ | $\delta\mathbf M_{\mathbf i}$ | "mass" = integrated conserved quantities |
| mixed / irregular cells | cut cells, $0<\kappa<1$ | |

# Reference list

69 printed references, merged complete into the [bibliography](/bibliography.md)
from the OCR text (Crossref deposits no reference list). Most journal
references print no title (placeholder title). OCR or printed slips recorded
in notes: ref. 15 (Chern and Colella) is read "I. Chen"; ref. 45 prints the
year 1944 for an AIAA paper of 1994; ref. 65 prints 1993 for the 1983 AIAA
conference; ref. 18 prints 1969 for Math. Comput. 22 (1968); ref. 58 prints
"J. Comput. Phys. 23(1)" for a 1994 Quirk paper.

# Pages created or updated

Chunk 1 (2026-11-08), list updated in chunk 2 (2026-11-08). This source is cited on:

- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Flux redistribution for cut cells](/methods/redistribution.md)
- [Discrete conservation](/properties/discrete-conservation.md)
