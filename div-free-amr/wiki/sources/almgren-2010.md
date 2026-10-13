---
type: Source
title: "Almgren et al. (2010) — CASTRO: A new compressible astrophysical solver. I. Hydrodynamics and self-gravity"
description: "Code paper for CASTRO on BoxLib: unsplit PPM on subcycled block-structured AMR (ratio 2 or 4, proper nesting without parent–child links, refluxing), and a multilevel self-gravity synchronization — level Poisson solves, a lagged composite correction and a flux-register-driven two-level correction solve; no divergence constraint."
resource: "doi:10.1088/0004-637X/715/2/1221"
source_kind: paper
authors: [Almgren A.S., Beckner V.E., Bell J.B., Day M.S., Howell L.H., Joggerst C.C., Lijewski M.J., Nonaka A., Singer M., Zingale M.]
year: 2010
venue: "Astrophys. J. 715:1221-1238"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2010-ApJ-Almgren-1010880004-637X7152-1221.pdf"
tags: [amr, block-structured, subcycling, self-gravity, production-code]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

[CASTRO](/software/castro.md) is a compressible astrophysical code on
BoxLib, the predecessor of [AMReX](/software/amrex.md): unsplit PPM,
general equation of state, reactions and self-gravity on a subcycled
block-structured hierarchy. Its contribution to this bundle is the AMR
synchronization of an elliptically coupled field, the gravitational
potential $\phi_{\mathrm g}$. The code has no MHD and no divergence
constraint.

# Key claims

1. **Hierarchy** (§§1, 6.1). Arbitrary-size logically rectangular grids,
   $r \in \{2, 4\}$, even cell counts.
   * Proper nesting of unions with no parent–child relation, and a buffer
     of 2 cells ($r = 2$) or 1 ($r = 4$), because PPM needs four ghost
     cells.
   * Regridding by error tagging and Berger–Rigoutsos clustering.
   * The code is placed against FLASH, ENZO and RAGE on parent–child
     nesting and time stepping.
2. **Subcycled advance** (§6.2.1). Level $l$ advances first, then $r$
   steps of level $l+1$, then synchronization by volume averaging and
   Berger–Colella refluxing. The time step is set by the most restrictive
   level. The ghost-fill interpolation orders in space and time are not
   stated.
3. **Level against composite solves** (§6.2.3). Separate level solves
   generate a mismatch in the normal gradient of $\phi_{\mathrm g}$ at
   level boundaries, even without density changes. A lagged correction
   (after Miniati & Colella 2007) makes the end-of-step potential exact
   when the density is unchanged.
4. **Two-level synchronization** (§6.2.3, eqs. 36–40, from the page images).
   * A flux register of the normal-gradient mismatch (coarse minus
     area-weighted fine) and the refluxing-only density change form a
     composite residual.
   * A two-level composite solve gives a potential correction, from which
     momentum and energy sync sources follow (time-centred, factor
     $\tfrac12$).
   * The correction is added to the next-coarser register (eq. 40).
5. **Hydro** (§5). Unsplit PPM with corner coupling and an
   accuracy-preserving limiter, "formally second-order in both space and
   time". Gravity is time-centred by a predictor–corrector.
6. **Performance** (§7).
   * Weak scaling without gravity from 8 to 64 000 processors; Poisson to
     13 824.
   * One level of refinement costs 5–19 % over its ideal factor of 3.
   * Grids are distributed by a knapsack heuristic or a Morton curve.

**Tests** (§8): Sod, double rarefaction, a strong shock, Sedov–Taylor,
single-mode Rayleigh–Taylor, a hydrostatic white dwarf (second-order
convergence of the velocity), homologous dust collapse and reacting
bubbles. The self-gravity tests run without refinement, so the multilevel
gravity synchronization is not exercised.

# Notation map

| Almgren et al. (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\ell$, $r_\ell$ | $l$, $r$ | |
| $R_{\ell'}$ | $r^{(0\to l)}$ (words) | collides with the restriction $R$ |
| $R^{\mathrm{comp}}$ | composite residual (words) | collides with $R$ |
| $\phi$ (gravitational potential) | $\phi_{\mathrm g}$ | $\phi_h$ is the projection potential |
| volume average onto coarse | $R$ | |
| ghost and new-grid interpolation | $\Gamma$, $P$ | orders not stated |
| $\nabla\phi$, $\nabla\cdot$ | $G_h$, $D_h$ | |
| $\Gamma_1$ | words | collides with the ghost-fill $\Gamma$ |
| $\delta F_\phi$ | register (as on [refluxing](/methods/refluxing.md)) | |

# Pages created or updated

* Created [CASTRO](/software/castro.md).
* Updated [Refluxing](/methods/refluxing.md), [AMR projection method](/methods/amr-projection-method.md), [Block-structured AMR](/definitions/block-structured-amr.md).
* Created [AMReX](/software/amrex.md) and [Space-filling curve](/definitions/space-filling-curve.md) (cited).
* Updated [Notation registry](/notation.md): $\phi_{\mathrm g}$.

# Citations

1. `~/papers/mosaic/div-free-amr/2010-ApJ-Almgren-1010880004-637X7152-1221.pdf`.
   * **Version.** arXiv:1005.0114v1 (1 May 2010), 52 pages. It is not the
     typeset article.
   * **Identity.** doi:10.1088/0004-637X/715/2/1221, checked on Crossref:
     Astrophys. J. 715(2):1221–1238, June 2010, ten authors.
   * **How it was read.** Text extraction, all sections. Eqs. 36–40 and the
     sync formulas were read from the page images.
   * **Recorded as printed.** The strong-shock "six orders of magnitude"
     against $p_L/p_R = 10^5$.
   * **Reference list:** 51 entries.
