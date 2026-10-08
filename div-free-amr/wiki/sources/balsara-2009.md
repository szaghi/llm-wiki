---
type: Source
title: "Balsara (2009) — Divergence-free reconstruction of magnetic fields and WENO schemes for MHD"
description: "Extends divergence-free reconstruction to third and fourth order in a Legendre-moment basis (face moments fix the interior; free constraints set by magnetic-energy minimization), giving finite-volume divergence-free WENO schemes that meet design order."
resource: "doi:10.1016/j.jcp.2009.03.038"
source_kind: paper
authors: [Balsara D.S.]
year: 2009
venue: "J. Comput. Phys. 228(14):5040-5056"
local_file: "~/papers/mosaic/div-free-amr/2009-JCP-Balsara-101016jjcp200903038.pdf"
tags: [divergence-free-reconstruction, high-order, weno, constrained-transport, amr]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Takes the [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
of [Balsara (2001)](/sources/balsara-2001.md) and [Balsara (2004)](/sources/balsara-2004.md),
which is second order, to third and fourth order. The result is a
finite-volume, face-staggered, divergence-free WENO scheme for MHD with SSP
Runge–Kutta time stepping. The author motivates the finite-volume route by
non-uniform and adaptive meshes, where the finite-difference high-order
lines (Jiang–Wu; [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md))
are less suited. The scheme meets its design order on 2D and 3D smooth
problems and stays positive on a $\beta = 2.5\cdot10^{-4}$ blast.

The file read is the author preprint; venue and pages were verified on
Crossref.

# Key claims

1. **Moment formulation** (§2, eqs. 3–9). On a zone mapped to the unit cube:
   * each face component is expanded in tensor Legendre polynomials of the
     face coordinates: 3 moments at second order, 6 at third, 10 at fourth;
   * the interior components are complete polynomial expansions of one
     order higher in their own direction, with the cyclic structure of
     the 2001 construction.
   The formulas are closed-form and must be evaluated in a set order:
   quartic, cubic, quadratic, linear, constant.
2. **The faces determine the interior** (observation 1). Specifying all face
   moments to order $r$ fixes every interior coefficient needed at order
   $r$. The remaining interior terms only match the faces exactly. So an
   $r$th-order divergence-free field inside a zone needs nothing beyond
   $r$th-order face data.
3. **Constraint closure by energy minimization** (eqs. 11, 13). The
   divergence-free constraint does not fix every coefficient. The free ones
   are chosen by an SVD minimization of the integrated magnetic energy over
   the zone. The author credits this with helping keep the pressure
   positive on stringent problems. The constant-term relation is equivalent
   to the integral (Gauss) form of the constraint, so the reconstruction is
   consistent with the exactly held $D_h^{\mathrm{f}} B_h = 0$
   ([notation](/notation.md)).
4. **Refinement ratio 3** (observations 2–3). Ratio 3 needs 9 degrees of
   freedom per face, and the fourth-order reconstruction has 10, so one can
   be relinquished. With the ratio-2 formulas of the 2001 paper, recursion
   gives any ratio that is a product of 2s and 3s for
   [divergence-free prolongation](/operators/divergence-free-prolongation.md).
   The author also claims transparent extension to curvilinear meshes with
   diagonal metrics, and to divergence-free prolongation for multigrid in
   resistive or Hall MHD. Neither is demonstrated here.
5. **Fluxes and EMFs** (§3.2). Fluxes are linear in four vectors (left and
   right states and fluxes), with the dissipation matrix frozen at the
   face barycenter, after Dumbser–Enaux–Toro, and integrated analytically.
   Four EMF contributions per edge, one from each adjacent face, are
   *averaged* as in Balsara (2004).
6. **Measured order** (§4, Tables I–II).
   * Magnetized vortex in 2D, $L_1$ orders: 2.00, 2.99, 4.41.
   * Torsional Alfvén wave in 3D: 2.48, 2.94, 4.48.
   * At fourth order the time stepping is third-order SSP-RK, so the Courant
     number is cut by 0.396 per mesh doubling to keep temporal error in step.
   * **Record inconsistency:** the tables label the schemes "2nd/3rd/4th order
     ADER", while the text describes RK-WENO.
7. **Dissipation** (§5.1). Torsional Alfvén waves at 9.46° decay much more
   slowly as the order rises. The linearized Riemann solver's advantage over
   HLL shrinks with order, so "higher order schemes allow us to get by with
   less expensive Riemann solvers". The rotor and the low-$\beta$ blast are
   captured with positive pressure and no grid artifacts.

# Notation map

| Balsara (2009) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_0^{x\pm}, B_y^{x\pm}, \dots$ (face moments) | moments of $B_h \in V_h^2$ on each face | Legendre basis, eqs. 4–6 |
| $a_\cdot, b_\cdot, c_\cdot$ (interior coefficients) | coefficients of the reconstructed field | eqs. 7–9 |
| eq. (18)/(19) | integral form of $D_h^{\mathrm{f}} B_h = 0$ | |
| $P_k(x)$ | scaled Legendre polynomials | no registry symbol |
| $E$ at edges | $E_h \in V_h^1$ | averaged from four faces |

# Pages created or updated

* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md): the high-order extension.
* Updated [Divergence-space prolongation $P_D$](/operators/divergence-free-prolongation.md): ratio 3 and recursive ratios.

# Citations

1. `~/papers/mosaic/div-free-amr/2009-JCP-Balsara-101016jjcp200903038.pdf` (doi:10.1016/j.jcp.2009.03.038): text extraction, all 34 pp., including the reference list (35 entries; two are numbered [26]).
