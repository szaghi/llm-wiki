---
type: Source
title: "Balsara, Bhoriya & Shu (2026) — An alternative finite difference WENO-like scheme with physical constraint preservation for divergence-preserving hyperbolic systems"
description: "Hybrid scheme to ninth order: zone-centred point values by alternative-FD WENO, face-averaged fields by a Yee-type Stokes update with edge EMFs from a 2D LLF/HLL Riemann solver, plus a time-explicit positivity (PCP) strategy, for CED, MHD and RMHD."
resource: "doi:10.1007/s42967-025-00517-y"
source_kind: paper
authors: [Balsara D.S., Bhoriya D., Shu C.-W.]
year: 2026
venue: "Commun. Appl. Math. Comput. 8:1730-1798"
local_file: "~/papers/mosaic/div-free-amr/2026-CAMC-Balsara-101007s42967-025-00517-y.pdf"
tags: [constrained-transport, upwind-emf, multidimensional-riemann-solver, finite-difference, weno, high-order, positivity, mhd, relativistic, electrodynamics]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper gives one algorithm for any PDE system that contains an
induction-type subsystem $\partial_t B + \nabla\times E = 0$:
computational electrodynamics, MHD and relativistic MHD. The rest of the
system is advanced as zone-centred point values with alternative
finite-difference (AFD) WENO, which is cheap. Only the face-averaged
normal fields keep an FV, Stokes-law update, on a Yee-type collocation.

It is merged into
[upwind constrained transport](/methods/upwind-constrained-transport.md)
and [positivity–divergence coupling](/results/positivity-divergence-coupling.md),
where it opens a `Contradictions` entry.

Received September 2024 and published in CAMC volume 8 (2026). The slug
follows the printed year.

# Key claims

1. **Why a hybrid** (§§1–2). FD-WENO is much cheaper than FV-WENO, but a
   divergence-preserving field needs face-averaged values and edge-averaged
   EMFs for Stokes' law to hold. Only the induction subsystem is kept in FV
   form. No volumetric divergence-free reconstruction is built.
2. **The edge EMF from the structure alone** (§3). The induction flux is
   antisymmetric across directions, so a 2D Riemann solver at an edge needs
   only two kinds of input: the four zone-centred $E$ values and the four
   face-normal fields, which are continuous across faces.
   * The 2D LLF EMF (eq. 12) is the average of the four $E$ values plus
     $S/2$ times the jumps of the facially reconstructed normal fields at
     the edge.
   * The 2D HLL version (eqs. 18–20) averages two resolved expressions and
     has a ninefold stack of supersonic and subsonic cases.
   * No constitutive relation between $E$ and $B$ is assumed.
3. **Algorithm** (§4).
   * 2D FV-WENO reconstruction of each face field within its face.
   * 1D WENO interpolation of face point values to zone centres.
   * 2D WENO interpolation of zone-centred $E$ to edges; Appendix A gives
     the formulas at orders 3, 5 and 7.
   * Normal-field jumps at the edges supply the dissipation.
   * AFD-WENO fluxes for the zone variables.
   * 1D WENO interpolation turns edge point values into edge averages.
4. **Positivity** (§5).
   * The low-order scheme is a first-order zone update with HLL or LLF
     fluxes. The authors call it positive "as was first proved by
     Gurski" (2004).
   * Averaging the exact face fields to zone centres can still break
     positivity in a few zones. Those are repaired by borrowing thermal
     energy from neighbours, after Abgrall, or by a low-order energy
     source.
   * A flag $\theta$ per zone then blends high- and low-order fluxes and
     EMFs, iterated until every zone is admissible.
5. **Accuracy and tests** (§§6–7).
   * Design orders 3, 5, 7 and 9 are met on a 3D plane electromagnetic
     wave, 2D MHD and 2D RMHD, with SSP-RK3 or the five-stage SSP-RK4
     with a shrinking time step.
   * Stringent tests, including low-$\beta$ blasts and strongly magnetized
     jets with $\beta$ down to $10^{-4}$, need the positivity strategy.
   * Electrodynamics in dielectric media, RMHD blasts and a shock–cloud
     problem are also shown.
6. **Speed** (§7.4, one core, same SSP-RK). FD-WENO is 7 to 14 times
   faster than FV-WENO in 2D and 5 to 12 times in 3D at third and fifth
   order. The authors note that ADER and flux-count economies could narrow
   the gap for FV.
7. **Related high-order FD CT.** The authors place Seo & Ryu (2023) as a
   case-by-case precursor for MHD. They state that their approach keeps
   the solved problem of high-order divergence-preserving AMR available.

# Notation map

| Balsara et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar B_x, \bar B_y, \bar B_z$ (face averages) | $B_h \in V_h^2$ | primal |
| $\bar E^{\mathrm{num}}$ (edge averages) | $E_h \in V_h^1$ | from the 2D Riemann solver |
| eqs. 3–5 | $\partial_t B_h = -C_h E_h$ | |
| $S$ (signal speed) | LLF wave-speed estimate | no registry symbol |
| PCP | positivity of density and pressure, i.e. data in $\mathcal G$ | |
| $\theta_{i,j,k}$ | high/low-order blending flag | |

# Pages created or updated

* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): the finite-difference realization up to ninth order.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): the staggered high-order positivity repair, and an open `Contradictions` entry on the multi-D positivity of the first-order update.

# Citations

1. `~/papers/mosaic/div-free-amr/2026-CAMC-Balsara-101007s42967-025-00517-y.pdf` (doi:10.1007/s42967-025-00517-y): text extraction, all pages including the appendices and the reference list (91 entries). The interpolation formulas of Appendices A–C and the PCP derivations of §5 were read in outline, and no equation from them is reproduced beyond the LLF EMF structure. Figures and tables were read from their captions and the text.
