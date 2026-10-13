---
type: Source
title: "Li & Shu (2005) — Locally divergence-free discontinuous Galerkin methods for MHD equations"
description: "DG with element-local exactly divergence-free polynomial bases for the magnetic field: cheaper than standard DG, same accuracy, improved stability — with interelement jumps unconstrained."
resource: "doi:10.1007/s10915-004-4146-4"
source_kind: paper
authors: [Li F., Shu C.-W.]
year: 2005
venue: "J. Sci. Comput. 22-23:413-442"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2005-JSC-Li-101007s10915-004-4146-4.pdf"
tags: [dg, divergence-constraint, mhd, high-order]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Extends the locally divergence-free DG method (introduced with Cockburn
for linear Maxwell) to nonlinear ideal MHD: the magnetic field is
approximated in **piecewise polynomial spaces that are exactly
divergence-free inside each element** — the solenoidal constraint is built
into the local basis. Because the local space is smaller than full
piecewise polynomials, the method **costs less** than standard DG while
maintaining the same accuracy for smooth solutions, and the numerical
experiments (1D/2D, smooth and discontinuous) show enhanced stability and
reduction of "certain nonphysical features."

# Key claims

1. **Constraint by basis restriction**: exactness is achieved by choosing
   the approximation space inside the constraint's kernel — no staggering,
   no cleaning field, no potential; RKDG machinery otherwise unchanged.
2. **"Locally" is the honest qualifier**: the divergence vanishes
   *within* elements; across element interfaces the normal component may
   jump, so the *global* (distributional) divergence is not controlled —
   the constraint lives at whatever strength the interelement jumps allow.
   The family therefore sits between exact and controlled in the
   constraint taxonomy of
   [exact discrete divergence](/properties/exact-discrete-divergence.md).
3. **Cheaper, not costlier**: unusual among constraint devices — the
   solenoidal basis is a *smaller* space, so exactness (locally) reduces
   cost rather than adding machinery.

# Notation map

| Li & Shu | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| locally divergence-free polynomial spaces | element-local kernel of $\nabla\cdot$ | basis-level constraint |
| RKDG | TVD-RK DG base scheme | unchanged |

# Pages created or updated

* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md) (the local-only variant: constraint by basis restriction, jumps uncontrolled).

# Citations

1. `~/papers/mosaic/div-free-amr/2005-JSC-Li-101007s10915-004-4146-4.pdf` (doi:10.1007/s10915-004-4146-4) — text extraction, pp. 413–442.
