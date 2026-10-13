---
type: Source
title: "Londrillo & Del Zanna (2000) — High-order upwind schemes for multidimensional magnetohydrodynamics"
description: "Derives staggered collocation from consistency arguments and constructs high-order divergence-free reconstruction and upwind EMFs for CT schemes."
resource: "doi:10.1086/308344"
source_kind: paper
authors: [Londrillo P., Del Zanna L.]
year: 2000
venue: "Astrophys. J. 530:508-524"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2000-ApJ-Londrillo-101086308344.pdf"
tags: [constrained-transport, high-order, eno, divergence-free-reconstruction, upwind-emf]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Constructs high-order (third-order, ENO-based) upwind MHD schemes with the
divergence-free constraint as a **built-in condition**, from consistency
arguments about the operator structure of the MHD system relative to Euler.
Three structural results: (i) staggered collocation of the magnetic field is
*derived*, not assumed — time-split consistency forces the induction
equation to be discretized with a unique EMF flux function at common
collocation points; (ii) the cell-averaged constraint is exact only at
second order, and high-order schemes need **divergence-free reconstruction**
— independent 1D reconstructions of the field components generate spurious
divergence; (iii) the EMF at cell corners is a genuinely two-dimensional
*four-state* Riemann flux, upwinded in both directions.

# Key claims

1. **Staggering from consistency** (their §3): a unique flux function
   $\Omega$ at common points "entails necessarily a staggered collocation of
   the magnetic field scalar components"; the staggered placement "is by no
   means a numerical trick but arises in a consistent way" from the discrete
   curl structure. (Tension with Tóth's elimination result — recorded at
   [staggered grid](/definitions/staggered-grid.md) `Contradictions`.)
2. **Second-order ceiling of naive CT**: the staggered cell-averaged
   condition $D_h^{\mathrm{f}} B_h = 0$ is an exact law *for second-order
   schemes*; beyond that, point values and cell averages separate, and
   reconstructing $B_x, B_y$ independently yields "a numerical
   $\nabla\cdot\mathbf{B}$ of any size."
3. **High-order divergence-free reconstruction**
   ([method page](/methods/divergence-free-reconstruction.md)): general
   prescriptions such that an $r$th-order-accurate interpolated field
   satisfies an $(r{+}1)$th-order-accurate divergence relation, with normal
   components continuous along their longitudinal coordinates.
4. **Upwind EMF as a four-state 2D Riemann flux** (their eq. 26): the corner
   EMF combines the four reconstructed states with dissipation terms from
   *both* $x$- and $y$-eigenspaces — replacing the plain averaging of
   [flux-CT](/methods/flux-ct.md)-type schemes with genuine two-dimensional
   upwinding, and "assuring the exact conservation in time of the
   divergence-free condition."
5. **Vector-potential equivalence**: a divergence-free field is fully
   equivalent to its numerical vector potential representation; the
   staggered induction update can always be integrated via the scalar
   $A_z$ equation.

# Notation map

| Londrillo & Del Zanna | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $b_x, b_y$ staggered / $B$ centered | $B_h$ face- / cell-collocated | same convention as Tóth |
| $\Omega$ (corner EMF flux function) | $E_h \in V_h^1$ | four-state upwind evaluation |
| $\oint_{\partial C} B_n\, dl = 0$ (eq. 12) | integral form of $D_h^{\mathrm{f}} B_h = 0$ | kinematical constraint |
| $\Delta_x, \Delta_y$ commuting difference operators | components of $D_h, C_h$; preservation via commutativity | their §3 argument = $D_h C_h = 0$ |
| $r$, $(r{+}1)$ | reconstruction / divergence accuracy orders | |

# Pages created or updated

* Created [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md).
* Updated [Constrained transport](/methods/constrained-transport.md) (high-order extension; upwind EMF).
* Updated [Staggered grid](/definitions/staggered-grid.md) (`Contradictions`: necessity vs eliminability of staggering).

# Citations

1. `~/papers/mosaic/div-free-amr/2000-ApJ-Londrillo-101086308344.pdf` (doi:10.1086/308344) — text extraction, pp. 508–524.
