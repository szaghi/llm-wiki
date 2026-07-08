---
type: Source
title: "Del Rey Fernández, Hicken & Zingg (2014) — Review of summation-by-parts operators with simultaneous approximation terms for the numerical solution of partial differential equations"
description: "SBP-SAT consolidation review: the norm as a 2p-accurate quadrature, dual consistency and functional superconvergence, and the generalized-SBP unification with pseudo-spectral and DG operators."
resource: "doi:10.1016/j.compfluid.2014.02.016"
source_kind: paper
authors: [Del Rey Fernández D.C., Hicken J.E., Zingg D.W.]
year: 2014
venue: "Computers & Fluids 95:171-196"
local_file: "~/papers/mosaic/div-free-amr/2014-CompFluids-DelReyFernandez-101016jcompfluid20140216.pdf"
tags: [sbp, sat, quadrature, dual-consistency, superconvergence, review]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The consolidation review of the [SBP](/definitions/summation-by-parts.md)-
[SAT](/methods/sbp-sat.md) methodology: forty years of theory (from
Kreiss–Scherer) and application (Euler/Navier–Stokes), operator-derivation
procedures for first and variable-coefficient second derivatives, SAT
construction, artificial dissipation, curvilinear transformation — and the
modern structural results: the variational/DG connection, dual
consistency, functional superconvergence, and the **generalized SBP
concept** built on the quadrature connection.

# Key claims

1. **The norm is a quadrature**: the diagonal $\mathsf{H}$ of a $2p$
   interior-order SBP operator represents a $2p$-accurate quadrature rule
   — the identity underlying both functional superconvergence and the
   interface-interpolation accuracy cap compiled at
   [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md).
2. **Dual consistency buys back the boundary loss**: diagonal-norm schemes
   are $p{+}1$ accurate in the solution (boundary closures of order $p$),
   but **dual-consistent** discretizations deliver functionals
   superconvergent at order $2p$ (Hicken–Zingg) — accuracy lives where
   the discrete adjoint is respected.
3. **Generalized SBP**: defining SBP through the quadrature property
   unifies classical FD-SBP with nodal pseudo-spectral and some
   discontinuous Galerkin operators — one umbrella, with SATs rigorously
   derivable across the family; the SBP-SAT interface theory of this
   bundle thus speaks for a much wider class than FD.
4. **Positioning of SAT virtues**: weak coupling relaxes continuity
   requirements of *both mesh and solution* across block interfaces with
   low communication overhead — the property set that makes SBP-SAT the
   FD community's interface framework.

# Notation map

| Del Rey Fernández et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $H$, $Q$, $D = H^{-1}Q$ | $\mathsf{H}, \mathsf{Q}, \mathsf{D}_1$ | |
| $u^T H v \approx \int UV$ | $\mathsf{H}$ as quadrature | the load-bearing identity |
| generalized SBP | quadrature-defined operator class | includes DG/pseudo-spectral |

# Pages created or updated

* Updated [Summation by parts (SBP)](/definitions/summation-by-parts.md) (quadrature identity; dual consistency; generalized SBP).

# Citations

1. `~/papers/mosaic/div-free-amr/2014-CompFluids-DelReyFernandez-101016jcompfluid20140216.pdf` (doi:10.1016/j.compfluid.2014.02.016) — text extraction, pp. 171–196.
