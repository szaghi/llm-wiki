---
type: Source
title: "Harlow & Welch (1965) — Numerical calculation of time-dependent viscous incompressible flow with free surface"
description: "Introduces the MAC method: the original staggered grid and pressure-Poisson enforcement of a face-difference discrete divergence of velocity."
resource: "doi:10.1063/1.1761178"
source_kind: paper
authors: [Harlow F.H., Welch J.E.]
year: 1965
venue: "Phys. Fluids 8(12):2182-2189"
local_file: "~/papers/mosaic/div-free-amr/1965-PhysFluids-Harlow-101063_11761178.pdf"
tags: [mac, staggered, incompressible, pressure-poisson, free-surface]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Introduces the **marker-and-cell (MAC) method** for 2D time-dependent viscous
incompressible flow with a free surface: primitive variables (pressure and
velocity — explicitly *not* vorticity/stream function), explicit
finite-difference time advancement, and the original **staggered
arrangement** — normal velocities on cell faces, pressure at cell centers
(their Fig. 2). The pressure field is computed each cycle by a Poisson
equation constructed so that the face-difference discrete divergence of the
new velocity vanishes in every cell. Marker particles track the free surface
and visualize the flow; they do not enter the dynamics. Validated on
broken-dam and sluice-gate problems against Martin & Moyce experiments (IBM
7030).

The PDF is a text-poor scan (AIP cover page plus imaged article pages); read
visually, all 8 article pages. No illegible ranges.

# Key claims

1. **Staggered placement** (Fig. 2): $u$ at vertical faces
   $(i{+}\tfrac12, j)$, $v$ at horizontal faces $(i, j{+}\tfrac12)$,
   pressure $\varphi = p/\rho$ at centers — the arrangement later called the
   [staggered grid](/definitions/staggered-grid.md); off-center values where
   needed are two-point averages.
2. **The discrete constraint** (their eq. 6):
   $D_{i,j} = (u_{i+\frac12,j}-u_{i-\frac12,j})/\delta x + (v_{i,j+\frac12}-v_{i,j-\frac12})/\delta y = 0$
   — the face-difference divergence, enforced *in every cell*.
3. **Pressure from a divergence-evolution Poisson equation** (eqs. 7, 9–10):
   substituting the momentum updates into the divergence gives an evolution
   equation for $D$; demanding $D^{n+1}_{i,j}=0$ yields a discrete Poisson
   equation for $\varphi$. The source term $R_{i,j}$ retains the $D_{i,j}/\delta t$
   and viscous-$D$ terms, making the iteration **self-correcting**: residual
   divergence from an imperfect previous solve is driven back toward zero
   rather than accumulating ("the use of $R_{i,j}$ … keeps the accumulation
   of compressional discrepancy to a sufficiently low level"). The constraint
   is held to the accuracy of the iterative Poisson solve
   ([MAC method](/methods/mac-method.md)).
4. **Boundary conditions are constraint-derived**: exterior ghost velocities
   at walls are chosen precisely so $D$ vanishes in exterior cells, and
   free-surface velocities are set from $D \equiv 0$ in surface cells — the
   discrete constraint, not physics alone, dictates the boundary recipe.
5. **Stability without artificial viscosity**; necessary conditions
   $4\nu\,\delta t/\delta x^2 < 1$ and $g\,d\,\delta t^2/\delta x^2 < 1$
   observed; a marker-count integral-geometry formula (via Santaló) serves as
   a global incompressibility accuracy check.

# Notation map

| Harlow & Welch | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u, v$ on faces | $u_h$, face-collocated ($V_h^2$ in 2D flux sense) | |
| $\varphi = p/\rho$ at centers | $\phi_h$, cell-collocated | they call it "pressure" |
| $D_{i,j}$ (eq. 6) | $D_h^{\mathrm{f}} u_h$ | face-difference stencil, velocity case |
| eq. (9) left-hand operator | $D_h^{\mathrm{f}} G_h$ | five-point discrete Laplacian |
| eq. (7) | evolution of $D_h^{\mathrm{f}} u_h$ | the constraint-transport identity for velocity |

# Pages created or updated

* Created [MAC method](/methods/mac-method.md).
* Updated [Staggered grid](/definitions/staggered-grid.md) (MAC as the original staggering, 1965).
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md) (velocity/incompressibility ancestry).

# Citations

1. `~/papers/mosaic/div-free-amr/1965-PhysFluids-Harlow-101063_11761178.pdf` (doi:10.1063/1.1761178) — read visually, pp. 2182–2189.
