---
type: Source
title: "Etienne, Paschalidis, Liu & Shapiro (2012) — Relativistic MHD in dynamical spacetimes: improved EM gauge condition for AMR grids"
description: "Diagnoses spurious magnetic fields at refinement boundaries as zero-speed gauge modes of the algebraic gauge; the Lorenz gauge has only propagating modes and cures them."
resource: "doi:10.1103/PhysRevD.85.024013"
source_kind: paper
authors: [Etienne Z.B., Paschalidis V., Liu Y.T., Shapiro S.L.]
year: 2012
venue: "Phys. Rev. D 85:024013 (arXiv:1110.4633)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2012-PRD-Etienne-101103PhysRevD85024013.pdf"
tags: [vector-potential, gauge, amr, grmhd, stability]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The gauge bill for
[vector-potential evolution](/methods/vector-potential-evolution.md) on
AMR, diagnosed and paid. In the simple "algebraic" gauge, magnetized
black-hole–neutron-star runs show **spurious strong magnetic fields
appearing at refinement level boundaries**, worsening as matter crosses
them during tidal disruption. Eigenvalue analysis identifies the cause:
the algebraic gauge is strongly hyperbolic but possesses a **static
(zero-speed) gauge mode**; excited modes sit where they were generated,
and interpolation errors at refinement boundaries (with their frequency
filtering) convert them into spurious $B$ that propagates inward and grows
until the run breaks down. Kreiss–Oliger dissipation on $A_i$ only
weakens the effect, "with undesired consequences." The **Lorenz gauge has
no zero-speed modes** — all EM modes propagate — so interface-generated
noise leaves the grid; BHNS comparisons confirm long-term stable
evolutions.

# Key claims

1. **Unigrid is immune, AMR is not**: on a single grid the $A$-scheme is
   equivalent to staggered CT and gauge modes never matter; it is
   *interlevel interpolation* that couples gauge dynamics to the physical
   field — the gauge cost is specifically an AMR cost.
2. **Static modes + interpolation = spurious fields**: the mechanism is
   spectral, not truncation-order; no amount of interpolation accuracy
   fixes a mode that cannot leave.
3. **Gauge freedom as a design variable**: "the EM gauge degree of freedom
   can be chosen to one's advantage" — for magnetized BHNS the Lorenz
   gauge is "a major improvement."

# Notation map

| Etienne et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| algebraic gauge / Lorenz gauge | gauge conditions on $A_h$ evolution | zero-speed vs all-propagating |
| spurious $B^i$ at boundaries | interface-generated constraint-consistent error | divergence-free but wrong |

# Pages created or updated

* Updated [Vector-potential evolution](/methods/vector-potential-evolution.md) (gauge-mode diagnosis and cure).

# Citations

1. `~/papers/mosaic/div-free-amr/2012-PRD-Etienne-101103PhysRevD85024013.pdf` (doi:10.1103/PhysRevD.85.024013) — text extraction, 10 pp.
