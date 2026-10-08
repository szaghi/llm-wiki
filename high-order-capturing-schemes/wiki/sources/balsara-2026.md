---
type: Source
title: "Balsara, Bhoriya & Shu (2026) — An alternative finite difference WENO-like scheme with physical constraint preservation for divergence-preserving hyperbolic systems"
description: "Extends AFD-WENO to systems with a divergence involution (electrodynamics, MHD, relativistic MHD): cell variables by AFD-WENO, face-averaged normal fields updated FV-style by edge electric fields from a multidimensional LLF/HLL Riemann solver, plus a time-explicit PCP hybridization; orders up to nine."
resource: "doi:10.1007/s42967-025-00517-y"
source_kind: paper
authors: [Balsara D.S., Bhoriya D., Shu C.-W.]
year: 2026
venue: "Commun. Appl. Math. Comput. 8:1730-1798"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2026-CAMC-Balsara-101007s42967-025-00517-y.pdf"
tags: [finite-difference, weno, mhd, constrained-transport, positivity, multidimensional-riemann-solver]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

All divergence-preserving sub-systems share the induction-equation
structure, so one mixed FD–FV algorithm covers them. The bulk of the
variables use cheap AFD-WENO, and only the face fields use an FV
update. Published online 9 Dec 2025 in volume 8 (2026). Merged into
the new [constrained transport](/methods/constrained-transport.md)
page, into [AFD-WENO](/methods/alternative-finite-difference-weno.md),
the positivity pages (where it opens the MHD `Contradictions` entry)
and the MHD benchmarks.

# Key claims

1. **Mixed form** (§2): cell-centred point values by AFD-WENO; Yee-type
   face averages $\bar B$ updated by edge averages $\bar{\mathcal E}$
   (eqs. 3–5, checked on the page image), which preserves the divergence
   exactly; no divergence-free volumetric reconstruction.
2. **Multidimensional Riemann solver** (§3): with anti-symmetric
   induction fluxes, the 2D LLF edge field is the four-corner average
   plus $\frac{S}{2}[B_{x,D} - B_{x,U} + B_{y,R} - B_{y,L}]$ (eq. 12, checked);
   the HLL version has a nine-case supersonic stack (eqs. 16–20).
3. **Algorithm** (§4): 2D WENO face reconstruction, 1D WENO
   interpolation to cell centres, 2D WENO interpolation of edge fields,
   AFD-WENO update, and 1D interpolation to edge averages; FV
   reconstruction from point values is possible at any order
   (Appendices B–C).
4. **PCP** (§5): a first-order scheme with HLL/LLF fluxes "will indeed be
   PCP, as was first proved by Gurski"; rare failures from averaging face
   fields are fixed by conservative energy borrowing, or else a
   non-conservative energy source; cell factors $\theta$ lowered
   iteratively, with face and edge minima (following Hu et al.).
5. **Results** (§§6–7): design order 3–9 for CED, MHD and RMHD vortices;
   beam refraction and total internal reflection; Orszag–Tang, rotor,
   two low-β blasts (PCP needed); RMHD blast and shock–cloud.
6. **Speed** (§7.4): FD 7–14× faster than FV in 2D and 5–12× in 3D with
   identical ingredients; FV could close part of the gap with ADER
   (about 2×), which FD "cannot" use.

# Notation map

| Balsara, Bhoriya & Shu (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf E$ (electric field) | $\boldsymbol{\mathcal E}$ | avoids the energy $E$ |
| $\bar B_{x;i+1/2,j,k}$ | $\bar B_{x;i+1/2,j,k}$ | |
| $\bar E^{num}_{z;\dots}$, $e^{num}_z$ | $\bar{\mathcal E}_z$, point value $\mathcal E_z$ | |
| $\Delta x, \Delta y, \Delta z$ | $h_x, h_y, h_z$ | |
| $S_L, S_R, S_D, S_U$, $S$ | $S_L, S_R, S_D, S_U$, $S$ | |
| $\theta_{i,j,k}$ | $\theta$ | PCP blending |
| $\varepsilon$ (total energy) | $E$ | |

# Pages created or updated

* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [MHD blast wave in a low-β medium](/benchmarks/mhd-blast-wave.md).
* Updated [MHD rotor](/benchmarks/mhd-rotor.md).
* Updated [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Updated [Shock–cloud interaction (MHD and relativistic MHD)](/benchmarks/shock-cloud-interaction.md).
* Updated [Alternative finite-difference WENO (AFD-WENO)](/methods/alternative-finite-difference-weno.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Updated [Positivity-preserving flux limiters (high/low-order flux blending)](/methods/positivity-preserving-flux-limiter.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md).
* Updated [Unequal-stencil and adaptive-order WENO (WENO-ZQ, WENO-AO)](/methods/weno-ao.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2026-CAMC-Balsara-101007s42967-025-00517-y.pdf` (doi:10.1007/s42967-025-00517-y; open-access typeset article, 69 pp.): text extraction, all sections; eqs. (3)–(5) and (12)–(15) read from the page images (pp. 1735, 1741). The 2D interpolation coefficients (Appendix A) and the HLL edge-field formulas are not reproduced. Reference list: 91 entries.
