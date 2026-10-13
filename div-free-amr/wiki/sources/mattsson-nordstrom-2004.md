---
type: Source
title: "Mattsson & Nordström (2004) — Summation by parts operators for finite difference approximations of second derivatives"
description: "Constructs narrow-stencil second-derivative SBP operators sharing the first-derivative norm, with boundary closures two orders lower preserving design accuracy."
resource: "doi:10.1016/j.jcp.2004.03.001"
source_kind: paper
authors: [Mattsson K., Nordström J.]
year: 2004
venue: "J. Comput. Phys. 199:503-540"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2004-JCP-Mattsson-101016jjcp20040301.pdf"
tags: [sbp, second-derivative, parabolic, high-order, boundary-closure]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Extends the [SBP](/definitions/summation-by-parts.md) toolkit from first to
**second derivatives**: operators
$\mathsf{D}_2 = \mathsf{H}^{-1}(A + \mathsf{B}S)$ with $A + A^T \le 0$
(so the energy method closes), $S$ a boundary first-derivative
approximation, and — decisively — **the same norm $\mathsf{H}$ as the
first-derivative operator**, so mixed hyperbolic–parabolic problems get one
coherent energy estimate. Fourth-, sixth-, and eighth-order diagonal- and
full-norm operators are derived with Maple.

# Key claims

1. **Two design routes**: apply $\mathsf{D}_1$ twice — the "complete"
   operator $A = -\mathsf{D}_1^T \mathsf{H} \mathsf{D}_1$ fully mimics
   integration by parts but doubles the stencil width and leaves the
   highest-frequency ($\pi$-)mode undamped (an upwind-split damped variant
   is given that kills it) — or build **minimal-width** operators with the
   first-derivative's interior width, which is the paper's main product.
2. **Boundary-closure economy**: internal order $2p$ survives a
   second-derivative boundary closure of order $2p{-}2$ with a
   $(2p{-}1)$-order boundary derivative $S$ — one order *less* restrictive
   than naive counting, proved by the error analysis and confirmed
   numerically.
3. **Energy estimate without full mimicry**: $A + A^T \le 0$ suffices —
   exact discrete integration by parts is not necessary for stability,
   only semiboundedness; full mimicry buys the exact identity at the cost
   of width.

# Notation map

| Mattsson & Nordström | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $H$, $D_1 = H^{-1}Q$ | $\mathsf{H}$, $\mathsf{D}_1$ | registry renaming |
| $D_2 = H^{-1}(A + BS)$ | $\mathsf{D}_2$ (second-derivative SBP) | narrow form; sign convention theirs |
| $B = \mathrm{diag}(-1,0,\dots,1)$ | $\mathsf{B}$ boundary matrix | |
| $2p$ | interior design order | |

# Pages created or updated

* Updated [Summation by parts (SBP)](/definitions/summation-by-parts.md) (second-derivative operators; shared norm; closure economy).

# Citations

1. `~/papers/mosaic/div-free-amr/2004-JCP-Mattsson-101016jjcp20040301.pdf` (doi:10.1016/j.jcp.2004.03.001) — text extraction, pp. 503–540.
