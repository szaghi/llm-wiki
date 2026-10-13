---
type: Source
title: "Seshadri & De (2020) — A novel sharp interface immersed boundary framework for viscous flow simulations at arbitrary Mach number involving complex and moving boundaries"
description: "Sharp-interface ghost-cell immersed boundary on structured grids with LDFSS flux splitting, TVD or WENO5 and low-Mach preconditioning: ray-tracing node classification, pseudo-normal reconstruction directions at sharp edges, quadratic boundary interpolation replaced by inverse-distance weighting near shocks, and three ghost layers for moving bodies; validated graphically from Mach 0.001 to 2."
resource: "doi:10.1016/j.compfluid.2020.104579"
source_kind: paper
authors: [Seshadri P.K., De A.]
year: 2020
venue: "Comput. Fluids 206:104579"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2020-CompFluids-Seshadri-101016jcompfluid2020104579.pdf"
tags: [immersed-boundary, moving-boundary, boundary-treatment]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

A sharp-interface immersed-boundary method with direct imposition of the
wall condition, a hybrid of the hybrid-Cartesian and ghost-cell
approaches, for flows from nearly incompressible to supersonic, with
fixed and moving bodies described by surface triangulations. The paper's
emphasis is geometric: robust node classification and the direction of
the reconstruction at sharp edges. It is not a cut-cell method and is not
conservative at the wall. Merged into
[immersed-boundary methods](/methods/immersed-boundary-method.md).

# Key claims

1. **Classification** (§§1, 3.2, 5): boundary nodes on the fluid side are
   overwritten by interpolation; ghost nodes inside the body get values
   at image points. No forcing, no cut cells, no small-cell problem.
2. **Ray tracing** (§3.2): node classification by counting ray–triangle
   intersections, since signed distance misclassifies points near edges.
3. **Pseudo-normals** (§§4.1–4.3, eqs. 1–3): the reconstruction direction
   follows angle-weighted vertex and edge normals; the authors argue this
   matters as much as the order of the boundary formula.
4. **Boundary conditions** (§4.4, eqs. 4–8): no-slip, a pressure Neumann
   condition with the wall acceleration (a normal force balance for
   supersonic moving bodies), adiabatic temperature.
5. **Interpolation** (§§4.5–4.6): quadratic for low-Mach flows (second
   order per the authors' earlier work); near shocks it gives negative
   pressure and density, so inverse-distance weighting is used, with no
   stated order.
6. **Moving bodies** (§5): field extension into the body, linear
   image-point interpolation, three ghost layers for WENO5 and one for
   TVD; mass conservation claimed qualitatively.
7. **Base scheme** (§2): cell-centred finite volume, Edwards' LDFSS,
   TVD or WENO5, dual time stepping with low-Mach preconditioning.

**Tests** (§§7–8, all graphical; no order study): NACA 0012 at Mach 0.8
and pitching at Mach 0.006; an impulsively started cylinder;
[Schardin's problem](/benchmarks/schardin-problem.md) at Mach 1.3;
oscillating cylinders; a viscous cylinder moving at Mach 1.2 and 2
(Galilean check, not the inviscid [supersonic cylinder](/benchmarks/supersonic-cylinder-flow.md));
a Mach 1.5 shock-driven free cylinder after Henshaw and Schwendeman (a
different set-up from [lift-off](/benchmarks/shock-cylinder-lift-off.md)).

# Notation map

| Seshadri & De (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $[p, u, v, w, T]$ | $p$, $\mathbf v$, $T$ | primitive variables |
| $\hat n_v$, $\hat n_e$, $\hat n_s$ | words | pseudo-normals |
| $\alpha_i$ (face angle) | words | $\alpha$ is the Lax–Friedrichs speed |
| $u, v, w$ (barycentric) | words | collide with velocity |
| $M_\infty$, $M_D$ | $\mathrm{Ma}$ | |

# Pages created or updated

* Contributed to [Immersed-boundary methods](/methods/immersed-boundary-method.md), [Schardin's problem](/benchmarks/schardin-problem.md).
* Updated [Inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md), [Weighted extrapolation](/methods/weighted-extrapolation.md), [Positivity preservation](/properties/positivity-preserving.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2020-CompFluids-Seshadri-101016jcompfluid2020104579.pdf`.
   * **Version.** The 62-page author manuscript, not the typeset article;
     no arXiv version; the supplementary material was not available.
   * **Identity.** doi:10.1016/j.compfluid.2020.104579, checked on
     Crossref: Comput. Fluids 206:104579, June 2020.
   * **How it was read.** Text extraction, all sections; eqs. 1–8 and 10
     checked on the page images.
   * **Recorded as printed.** The position update of eq. 10 lacks a factor
     $\tfrac12$; in the shock-driven cylinder the post-shock density does
     not satisfy the Mach 1.5 jump conditions (about 2.20 expected, 1.56549
     printed) and the initial shock lies outside the domain; Table 1's lift
     and drag columns appear swapped for the zero-incidence case.
   * **Reference list:** 96 numbers printed, one an invalid placeholder
     ("!!! INVALID CITATION !!!"), so 95 entries, matching Crossref. An
     undated conference paper takes the citing year (bundle rule).
