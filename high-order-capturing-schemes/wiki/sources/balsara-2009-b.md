---
type: Source
title: "Balsara (2009b) — Divergence-free reconstruction of magnetic fields and WENO schemes for magnetohydrodynamics"
description: "Extends divergence-free reconstruction of face-centred magnetic fields to third and fourth order in closed form, fixing free coefficients by minimizing magnetic energy, and builds a Yee-staggered RK-WENO finite-volume MHD scheme that reaches design order to fourth on a magnetized vortex and a 3D torsional Alfvén wave."
resource: "doi:10.1016/j.jcp.2009.03.038"
source_kind: paper
authors: [Balsara D.S.]
year: 2009
venue: "J. Comput. Phys. 228:5040-5056"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2009-JCP-Balsara-101016jjcp200903038.pdf"
tags: [mhd, divergence-free, reconstruction, weno, staggered, amr]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The RK sibling of [Balsara et al. (2009)](/sources/balsara-2009.md), the
ADER-WENO paper, built on the same reconstruction. It is keyed
`balsara-2009-b` because that paper holds the bare key. Merged into the
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
page and the CT, positivity and SSP pages, and the vortex, Alfvén-wave,
rotor and blast benchmarks.

# Key claims

1. **Basis and data** (§2, eqs. 3–6): scaled Legendre polynomials to
   $P_4$ on the unit cube; 3, 6 and 10 face moments per face at orders 2,
   3 and 4. Eq. 6 misprints $P_1(z)$ for $P_1(y)$.
2. **Closed form** (§2, eqs. 7–18): coefficients in a fixed order from
   quartic to constant terms; those the faces leave free minimize the
   zone's magnetic energy (eqs. 11, 13, 15); the only compatibility
   condition is zero net face flux (eq. 18).
3. **Observations** (§2): the face moments fix every needed coefficient;
   ratio-3 AMR by relaxing one moment; the curvilinear transformations of
   Balsara (2004) carry over; possible use in multigrid prolongation.
4. **Scheme** (§3): Legendre modal reconstruction of the conserved state;
   face moments by WENO within faces; a linearized flux with its
   dissipation matrix frozen at the face barycentre, integrated exactly;
   edge fields averaged over four faces; SSP-RK2 and RK3. RK4 "was not
   implemented", so fourth order in space needs a Courant number reduced by
   0.396 per mesh doubling (§3.3), which matches $2^{-4/3}$ for $\Delta t$
   (a compiler's reading).
5. **Accuracy** (§4, Tables I–II): $L^1$ orders 2.00, 2.99, 4.41 on the
   magnetized vortex and 2.48, 2.94, 4.48 on the 3D torsional Alfvén wave.
   The table rows are labelled "ADER" although the runs are RK, and the
   numbers differ from the ADER paper's.
6. **Other tests** (§5): torsional Alfvén-wave decay (dissipation falls
   with order whatever the solver), rotor, low-β blast (pressure stays
   positive, credited to the reconstruction without an ablation run).

# Notation map

| Balsara (2009b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(x, y, z) \in [-\tfrac12, \tfrac12]^3$ | $\zeta$ per direction | |
| $P_0, \dots, P_4$ | $P_l(\zeta)$ | $P_4 = \zeta^4 - \tfrac3{14}\zeta^2 + \tfrac3{560}$ |
| $B^{x\pm}_{yy}, \dots$ (face moments) | Legendre face moments of $B_x$ | words on concept pages |
| $a_\cdot, b_\cdot, c_\cdot$ | $\hat B_{x,\cdot}$, $\hat B_{y,\cdot}$, $\hat B_{z,\cdot}$ | |
| $A(y,z)$ (dissipation matrix) | (words) | registry $A$ is the flux Jacobian |
| $\varepsilon$ (energy; wave amplitude) | $E$; (words) | |
| $U_1, \hat U_2, \dots, \hat U_{20}$ | $\bar u_i$, $\hat u^{(\cdot)}_i$ | |

# Pages created or updated

* Created [Circularly polarized (torsional) Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Created [Divergence-free reconstruction of face-centred magnetic fields](/methods/divergence-free-reconstruction.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [MHD blast wave in a low-β medium](/benchmarks/mhd-blast-wave.md).
* Updated [MHD rotor](/benchmarks/mhd-rotor.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2009-JCP-Balsara-101016jjcp200903038.pdf` (author manuscript, created 13 November 2008, most likely the submitted version, not the version of record; published as J. Comput. Phys. 228(14):5040–5056 (August 2009), doi:10.1016/j.jcp.2009.03.038, checked on Crossref; the manuscript prints 35 references where Crossref lists 41 for the article): text extraction, all sections; eqs. 4–6, 11–18 and Table I read from the page images. Not given: the vortex strengths, the rotor and blast set-ups (deferred to Balsara 2004), and the energy-minimization derivation. Reference list: 35 entries (two share the number [26]).
