---
type: Source
title: "Mattsson & Carpenter (2010) — Stable and accurate interpolation operators for high-order multiblock finite difference methods"
description: "Constructs SBP-preserving interface interpolation operators for nonconforming (2:1) multiblock grids, keeping strict stability, accuracy, and conservation of the base scheme."
resource: "doi:10.1137/090750068"
source_kind: paper
authors: [Mattsson K., Carpenter M.H.]
year: 2010
venue: "SIAM J. Sci. Comput. 32(4):2298-2320"
local_file: "~/papers/mosaic/div-free-amr/2010-SISC-Mattsson-101137090750068.pdf"
tags: [sbp, sat, interpolation, nonconforming, 2-1-interface, multi-block, conservation]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Removes the two standing impediments of multiblock
[SBP-SAT](/methods/sbp-sat.md) — matching collocation points and identical
operators across interfaces (ironically, the very assumptions the original
stability proofs needed): a systematic methodology for coupling arbitrary
SBP schemes across **nonconforming interfaces**, by identifying the
conditions interface interpolation operators must satisfy to preserve
strict stability, accuracy, and conservation
([operator page](/operators/sbp-preserving-interpolation.md)). Concrete
operators are constructed for a **2:1 grid compression** coupling
2nd–2nd, 4th–4th, 6th–6th, 8th–8th-order SBP operators, and for
dissimilar-order couplings (2–4, 4–8) — "the first time such interpolation
operators have been presented in the literature." Verified by eigenvalue
analysis and 2D Euler vortex simulations; parabolic extension in an
appendix.

# Key claims

1. **The SBP-preserving conditions** (their eqs. 15–16): the two interface
   interpolants must be adjoints in the interface norms,
   $\mathsf{H}_R\, I_{C2F} = I_{F2C}^T\, \mathsf{H}_L$, together with the
   contractive conditions
   $\mathsf{H}_L(I - I_{F2C} I_{C2F}) \ge 0$ and
   $\mathsf{H}_R(I - I_{C2F} I_{F2C}) \ge 0$ — the round trip must not
   amplify in the energy norms.
2. **Stability and conservation** (Lemma 3.4): with SAT penalties tuned as
   $2\Sigma_L = A$, $2\Sigma_R = -A$ and the conditions above, the
   nonconforming coupling is energy-stable *and* conservative to the order
   of accuracy — the telescoping-flux argument survives interpolation
   precisely because of the adjoint condition.
3. **Accuracy definition and cost** (Def. 2.4): $p$th-order interpolation =
   exact on $x^k$, $k \le p{-}1$ in the interior but only
   $k \le (p{-}1)/2$ **near interface boundaries** — a boundary-accuracy
   sacrifice mirroring SBP boundary closures; numerically, $p$th-order
   interpolation preserves the accuracy of the $p$th-order narrow-diagonal
   SBP scheme.
4. **Scope**: hyperbolic systems in 2D (curvilinear multiblock), parabolic
   in appendix; the interface remains *conforming in geometry* (shared
   line, matched endpoints) — nonconformity is in resolution and operator
   order, the SBP analog of the 2:1 refinement interface.

# Notation map

| Mattsson & Carpenter | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $I_{F2C}, I_{C2F}$ | $I_{F2C}, I_{C2F}$ | adopted into registry this ingestion |
| $H_L, H_R$ (interface norms) | $\mathsf{H}_C, \mathsf{H}_F$ | 1D trace norms |
| $\Sigma_{L,R}$ penalty matrices | SAT coefficients | |
| 2:1 grid compression | the 2:1 interface, trace version | resolution nonconformity |

# Pages created or updated

* Created [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md).
* Updated [SBP-SAT technique](/methods/sbp-sat.md) (nonconforming extension now ingested).
* Extended [Notation registry](/notation.md) (interface interpolation block).

# Citations

1. `~/papers/mosaic/div-free-amr/2010-SISC-Mattsson-101137090750068.pdf` (doi:10.1137/090750068) — text extraction, pp. 2298–2320.
