---
type: Source
title: "Balsara, Rumpf, Dumbser & Munz (2009) — Efficient, high accuracy ADER-WENO schemes for hydrodynamics and divergence-free magnetohydrodynamics"
description: "Structured-mesh finite-volume ADER-WENO schemes to fourth order for Euler and divergence-free MHD: modal Legendre WENO with a dominant central stencil and cheap cross-term stencils, divergence-free reconstruction of face fields, and the continuous-Galerkin ADER-CG predictor, with point-by-point implementation recipes."
resource: "doi:10.1016/j.jcp.2008.12.003"
source_kind: paper
authors: [Balsara D.S., Rumpf T., Dumbser M., Munz C.-D.]
year: 2009
venue: "J. Comput. Phys. 228:2480-2516"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2009-JCP-Balsara-101016jjcp200812003.pdf"
tags: [ader, weno, mhd, constrained-transport, legendre-basis, finite-volume]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A practical catalogue of one-step finite-volume schemes of second to
fourth order on structured meshes, implemented in Balsara's RIEMANN
code. The WENO reconstruction is modal and gives the central stencil
100 times the linear weight of the others. The predictor is ADER-CG, and
MHD keeps a face-centred, divergence-free field. The scheme is tested
on stringent Euler and MHD problems. Merged into the new
[ADER](/methods/ader.md) and [polynomial WENO](/methods/polynomial-weno.md)
pages and into the constrained-transport, Riemann-solver and positivity
pages.

# Key claims

1. **Why one-step FV** (§1): finite-difference WENO does not take well
   to non-uniform or hierarchical meshes. One-step schemes are the right
   AMR building block (Colella), and RK lacks a one-step structure.
2. **Modal WENO** (§2.1): explicit 1D formulas at third, fourth and
   fifth order. The indicators are sums of squares,
   $u_x^2 + \frac{13}{3}u_{xx}^2$ at third order (eqs. 6–9, 11–15, 17–22).
   The central stencil gets 100 times the one-sided weight, and the
   power is 4, after Dumbser and Käser.
3. **Cross terms** (§2.2): third order uses four diagonal stencils.
   Fourth order uses five stencils for the $xy$-type moments and eight
   for $xyz$, which is cheaper than Balsara et al.'s earlier strategy.
4. **Divergence-free reconstruction** (§2.3): facial moments
   (eqs. 43–45) plus $\nabla\cdot\mathbf B = 0$ fix interior polynomials
   (eqs. 46–48). Some terms are "non-evolutionary".
5. **ADER-CG** (§3): a continuous-in-time Galerkin predictor in modal
   space, with explicit third-order formulas (second and fourth in the
   appendices). It uses $K + 1$ iterations for order $K + 1$ ("we used
   two, three and four ADER iterations for the second, third and fourth
   order schemes … the minimum permissible number", §4.2 step 5, p. 2494)
   and cannot handle stiff sources.
6. **Fluxes and electric fields** (§4.1): HLL speeds are frozen at the
   space–time barycentre. Edge electric fields are averaged over four
   faces. The HLL dissipation bracket is doubled for the electric field.
7. **Cost** (§4.2): second-order MHD runs at 31,000 zones/s in 3D on one
   core. Third order costs 2.5 times second, and fourth 3 times third.
8. **Accuracy** (§5): design order on isentropic and magnetized
   vortices, 3D torsional Alfvén waves and density waves. Fourth order
   on $16^3$ is as accurate as second order on $48^3$, which takes 12
   times longer.
9. **Tests** (§§6–7): interacting blasts, Shu–Osher, forward step, double
   Mach reflection, MHD Riemann problems (Ryu–Jones, Dai–Woodward),
   Alfvén-wave decay, rotor, and 2D/3D low-β blast. Pressure stays
   positive, credited to the divergence-free reconstruction. A
   flattening algorithm is given in Appendix A, not reviewed here.

# Notation map

| Balsara et al. (2009) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_0$, $u_x$, $u_{xx}$, $u_{xxx}$, $u_{xy}$, … | $\bar u_i$, $\hat u^{(1)}_i$, $\hat u^{(2)}_i$, $\hat u^{(3)}_i$, $\hat u^{(11)}_i$, … | Legendre moments |
| $P_l(x)$ on $[-\tfrac12, \tfrac12]$ | $P_l(\zeta)$ | |
| $IS$ | $\beta_k$ | |
| $\lambda_L$, $\lambda_R$ | $S_L$, $S_R$ | HLL speeds |
| $E$ (electric field), $e$ (energy) | $\boldsymbol{\mathcal E}$, $E$ | |
| $\Delta x$ | $h$ | |

# Pages created or updated

* Created [ADER one-step schemes (arbitrary high order using derivatives)](/methods/ader.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Created [High-order adaptive mesh refinement for capturing schemes](/methods/high-order-amr.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [MHD blast wave in a low-β medium](/benchmarks/mhd-blast-wave.md).
* Updated [MHD rotor](/benchmarks/mhd-rotor.md).
* Created [Polynomial WENO reconstruction with a dominant central stencil](/methods/polynomial-weno.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Notation registry](/notation.md): batch-4 registry extensions.
* Also cited on [Circularly polarized (torsional) Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md), [Ryu–Jones and Dai–Woodward one-dimensional MHD shock tubes](/benchmarks/ryu-jones-shock-tubes.md), [Divergence-free reconstruction of face-centred magnetic fields](/methods/divergence-free-reconstruction.md), [Multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2009-JCP-Balsara-101016jjcp200812003.pdf` (doi:10.1016/j.jcp.2008.12.003, checked on Crossref; typeset JCP article; `pdftotext` reports a damaged xref table but extracts all pages): text extraction, all sections; eqs. 6–15 read from the page image (p. 2483). The ADER-CG matrices (eqs. 53–65) and the vortex and wave initial data are only partly legible in the text layer and are not reproduced. Reference list: 60 entries.
