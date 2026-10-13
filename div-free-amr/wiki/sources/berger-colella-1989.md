---
type: Source
title: "Berger & Colella (1989) — Local adaptive mesh refinement for shock hydrodynamics"
description: "Defines block-structured AMR: properly nested rectangular patch hierarchies refined in space and time, with conservative averaging and flux correction at coarse-fine interfaces."
resource: "doi:10.1016/0021-9991(89)90035-1"
source_kind: paper
authors: [Berger M.J., Colella P.]
year: 1989
venue: "J. Comput. Phys. 82:64-84"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1989-JCP-Berger.pdf"
tags: [amr, block-structured, refluxing, conservation, shock-capturing]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The defining paper of **block-structured AMR** for hyperbolic conservation
laws: the refined region is a hierarchy of rectangular grid patches, properly
nested, with boundaries coinciding with coarse grid lines, refined by the
same ratio $r$ in space *and* time (subcycling), integrated by an unmodified
"off-the-shelf" conservative scheme on every patch. Because the target is
unsteady shock flow, **maintaining global conservation form is a primary
consideration** — met by two coupling operations at coarse–fine boundaries:
conservative averaging of covered coarse cells, and a flux-correction
("refluxing") pass at interface cells. Grid generation is automatic:
Richardson-type error estimation flags cells, buffer zones absorb feature
motion between regriddings, clustering produces new patches. Demonstrated on
2D Euler multiple-Mach-reflection problems on a Cray. (The paper carries no
printed DOI — the retroactive Elsevier DOI above was verified via Crossref
against title/authors/volume/pages.)

# Key claims

1. **Hierarchy discipline** ([definition page](/definitions/block-structured-amr.md)):
   patches start/end on coarse cell corners; a level-$l$ cell is separated
   from level-$l{-}2$ by at least one level-$l{-}1$ cell ("proper nesting");
   refinement ratio $r$ (even) applies to $\Delta t$ as well as $\Delta x$,
   so the same explicit scheme is stable on every level; the solution at a
   point is *defined* as the finest-grid value there.
2. **Covered coarse cells are overwritten by the conservative average** of
   the $r^2$ fine cells (the restriction $R$); the coarse integration result
   there is discarded.
3. **Refluxing** ([method page](/methods/refluxing.md)): at a coarse cell
   abutting a fine patch but not covered, conservation across the interface
   requires the coarse flux to equal the time-and-space sum of fine fluxes
   on that edge; implemented as a correction pass with a saved edge array
   $\delta F$ initialized to minus the provisional coarse flux and
   accumulated with fine fluxes over the $r$ fine steps.
4. **Ghost filling**: fine-patch boundary values come from adjacent
   same-level grids where available, else bilinear interpolation in space
   and linear interpolation in time from the coarser level — the concrete
   ancestral instance of the ghost-fill operator $\Gamma$.
5. **Regridding**: error estimation (justified for smooth solutions;
   variants discussed for shocks) flags cells; a two-cell buffer zone
   exploits finite propagation speed; level-$l$ cells under level-$l{+}2$
   interiors are force-flagged to preserve nesting; clustering heuristics
   emit large, low-overlap rectangles.

# Notation map

| Berger & Colella | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| refinement ratio $r = \Delta x_{l-1}/\Delta x_l$ | $H/h$ at one interface | $r=2$ is the 2:1 case; they allow any even $r$ |
| conservative average of covered cells | $R$ (restriction) | cell-volume averaging |
| bilinear + linear-in-time boundary interpolation | $\Gamma$ (ghost fill) | acts level $l{-}1 \to l$ patch borders |
| $\delta F$ correction pass | refluxing | no registry symbol; named operation |
| $u$, $F$, $G$ | conserved state and fluxes | generic hyperbolic system |

# Pages created or updated

* Created [Block-structured AMR](/definitions/block-structured-amr.md).
* Created [Refluxing (coarse-fine flux correction)](/methods/refluxing.md).

# Citations

1. `~/papers/mosaic/div-free-amr/1989-JCP-Berger.pdf` (doi:10.1016/0021-9991(89)90035-1, Crossref-verified) — text extraction, pp. 64–84.
