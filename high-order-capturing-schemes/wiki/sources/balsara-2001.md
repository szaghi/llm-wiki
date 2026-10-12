---
type: Source
title: "Balsara (2001) — Divergence-free adaptive mesh refinement for magnetohydrodynamics"
description: "Second-order divergence-free AMR for MHD on a Yee mesh: the first divergence-free reconstruction of face fields inside a zone, a ratio-2 divergence-free prolongation with bilinear face moments, area-weighted restriction of face fields, and an electric-field correction at coarse–fine edges that transposes Berger–Colella refluxing from faces to edges."
resource: "doi:10.1006/jcph.2001.6917"
source_kind: paper
authors: [Balsara D.S.]
year: 2001
venue: "J. Comput. Phys. 174:614-648"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2001-JCP-Balsara-101006jcph20016917.pdf"
tags: [mhd, divergence-free, amr, staggered, reconstruction]
timestamp: 2026-10-09T00:00:00Z
---

# Summary

A complete second-order AMR scheme for MHD on a Yee mesh (face-centred
$\mathbf B$, edge-centred $\boldsymbol{\mathcal E}$), built by analogy with
Berger–Colella's conservative AMR for the Euler equations. Its core tool
is a divergence-free reconstruction of the field inside a zone, which in
1D reduces to MUSCL. Cross terms on the faces and cubic terms inside turn
it into a divergence-free prolongation for refinement ratio 2.
Restriction averages fine face fields, and an electric-field correction
at fine–coarse edges keeps the coarse field divergence-free after
subcycled fine steps. Merged into the
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md),
[CT](/methods/constrained-transport.md) and
[high-order AMR](/methods/high-order-amr.md) pages and the
[shock–cloud](/benchmarks/shock-cloud-interaction.md) benchmark.

# Key claims

1. **Edge fields** (§II, eqs. 2.4–2.10): the Balsara–Spicer average of four
   face Godunov fluxes, using $F_7 = -G_6$ and its analogues; a
   semi-implicit resistive term is sketched. The face update is the
   discrete Stokes law.
2. **Staggered over zone-centred CT** (§III, items 1–3). Tóth's zone-centred
   formulation is "a mere averaging" of Balsara–Spicer; its control volumes
   do not tile the mesh, do not align with refinement patches and do not
   nest for multigrid.
3. **Divergence-free reconstruction** (§III; 2D eqs. 3.1–3.16, 3D eqs.
   3.17–3.39). Quadratic polynomials whose divergence vanishes everywhere
   in the zone, matching minmod-limited linear profiles of the normal
   component on each face; 17 coefficients against 18 face data less one
   (the discrete divergence). The closed forms, including
   $\hat B_{x,x} = (B^+_x - B^-_x)/h_x$ and the zone average
   $\langle B_x\rangle_i = \tfrac12(B^+_x + B^-_x) - \hat B_{x,xx}h_x^2/6$
   (eq. 3.39), are those later restated by Balsara (2004).
4. **1D limit** (eq. 3.40): van Leer's MUSCL, so the fluxes coincide with a
   zone-centred TVD scheme. No multi-D TVD-like property is proved.
5. **Prolongation, ratio 2** (§IV, eqs. 4.1–4.19). Where a coarse face
   overlies four fine faces, its profile gains a bilinear term fitted
   exactly to the four fine values (eqs. 4.4–4.5). The interior gains 12
   terms under three new divergence constraints. The system is
   under-determined, and three coefficients are fixed by a simplifying
   choice so that the prolongation reduces to the reconstruction when the
   cross terms vanish (eqs. 4.12–4.14), not by energy minimization.
   Ratios 4 and 8 follow by recursion; other ratios need new formulas.
6. **Use** (§IV item 2; §VI items 2–3): prolongation initializes new fine
   meshes, after injection from old fine meshes wherever possible; fine
   halos are filled with the plain reconstruction, "spatially and
   temporally second-order accurate". How coarse data are interpolated in
   time inside the RK stages is not stated.
7. **Restriction** (eq. 5.4): the coarse face field is the average of the
   four fine face fields covering it, at synchronization.
8. **Electric-field correction** (§V, eqs. 5.5–5.7, Fig. 3). Restriction
   implicitly replaces the coarse edge fields on the shared face by
   space–time averages of fine edge fields. Coarse faces that only share
   an edge with the fine patch must be corrected by the difference, for
   example
   $B^{n+1}_{y} \leftarrow B^{n+1}_{y} - \frac{\Delta t}{h_x}\left(\tfrac14\sum(\text{two fine edges}\times\text{two half-steps}) - \mathcal E^{n+1/2}_{z}\right)$.
   This is Berger–Colella flux correction moved from faces to edges. That
   it makes the coarse field divergence-free is argued, not proved.
9. **Time stepping** (§VI): unsplit second-order RK at Courant number 0.4
   on all levels, ratio-2 subcycling, proper nesting required.
10. **A divergence-preserving variant** (§IV item 10) prolongs a nonzero
    divergence faithfully. **Refinement does not cure non-solenoidal
    schemes** (§I): their divergence errors have the same relative size on
    every level.

**Tests** (§VI, 3D, two levels, ratio 2). A Mach 10 shock–cloud
interaction ($96\times64\times64$ root grid) and a supernova blast ($64^3$
root grid). The undivided divergence relative to $|\mathbf B|$ stays below
$10^{-14}$ (shock–cloud at $t = 0.0251$) and "well below $10^{-13}$" later.
There is no convergence study, and no run without the electric-field
correction, so its necessity is argued, not shown.

# Notation map

| Balsara (2001) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_{x,i+1/2,j,k}$, $E_{z,i+1/2,j+1/2,k}$ | $\bar B_{x;i+1/2,j,k}$, $\bar{\mathcal E}_{z;i+1/2,j+1/2,k}$ | face and edge values on the Yee mesh |
| $a_0, a_x, a_{xy}, \dots$; $b_\cdot$; $c_\cdot$ | $\hat B_{x,0}, \hat B_{x,x}, \hat B_{x,xy}, \dots$; $\hat B_{y,\cdot}$; $\hat B_{z,\cdot}$ | |
| $\Delta_y B^\pm_x$, $\Delta_{yz} B^\pm_x$ | (words: limited undivided face slopes and bilinear moment) | |
| $\mathbf E$, $c$ | $\boldsymbol{\mathcal E}$; (speed of light dropped) | Gaussian units in the paper |
| $r$ | $r_{\mathrm{AMR}}$ | |
| $\sigma$ | (words: conductivity) | |
| $\Delta x$ | $h_x$ | |

# Pages created or updated

* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md): origin of the second-order formulas; prolongation, restriction and the electric-field correction.
* Updated [Constrained transport](/methods/constrained-transport.md) and [High-order AMR](/methods/high-order-amr.md).
* Updated [Shock–cloud interaction](/benchmarks/shock-cloud-interaction.md).
* Also updated in the same run (list completed at the batch-8 deep lint): [Total variation diminishing](/properties/total-variation-diminishing.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2001-JCP-Balsara-101006jcph20016917.pdf` (doi:10.1006/jcph.2001.6917, printed on page 1, checked on Crossref: J. Comput. Phys. 174(2):614–648, December 2001; typeset publisher version): text extraction; eqs. 3.5–3.40, 4.1–4.19, 5.1–5.7 and Fig. 3 read from the page images; eqs. 2.3, 2.5–2.10 from the text layer only, not reproduced. Printed slips noted: "J. Comput. Phys. 7, 270" for Balsara & Spicer in the abstract; "Section III.3"; "The coarse mesh takes two time steps" (the fine mesh is meant). Reference list: 46 entries.
