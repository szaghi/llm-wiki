---
type: Source
title: "Etienne, Liu & Shapiro (2010) — Relativistic magnetohydrodynamics in dynamical spacetimes: a new AMR implementation"
description: "GRMHD with the induction equation recast as vector-potential evolution: B = curl A is divergence-free on any grid, and the unconstrained A admits arbitrary AMR interpolation."
resource: "doi:10.1103/PhysRevD.82.084031"
source_kind: paper
authors: [Etienne Z.B., Liu Y.T., Shapiro S.L.]
year: 2010
venue: "Phys. Rev. D 82:084031 (arXiv:1007.2848)"
local_file: "~/papers/mosaic/div-free-amr/2010-PRD-Etienne-101103PhysRevD82084031.pdf"
tags: [vector-potential, amr, grmhd, constrained-transport, general-relativity, production-code]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

GRMHD in dynamical spacetimes (BSSN metric evolution + conservative HRSC
matter) with the induction equation recast as an **evolution equation for
the magnetic vector potential** $A_i$
([method page](/methods/vector-potential-evolution.md)): $A_i$ lives on
edges (staggered against hydro/metric variables), the field is computed as
$\tilde B^i = \tilde\epsilon^{ijk}\partial_j A_k$, and the constraint
holds **by construction on any grid**. On uniform grids the scheme is
"numerically equivalent to a commonly used, staggered-mesh
constrained-transport scheme"; on AMR it is the reason for the design:
"unlike the magnetic field, the vector potential is not constrained, and
so **any interpolation scheme can be used during prolongation and
restriction**, thus enabling its use with any AMR algorithm." Validated on
magnetized shocks, Alfvén waves, cylindrical explosions/disks, magnetized
Bondi flow, and magnetized rotating-star collapse — including black-hole
spacetimes with moving punctures (interior errors stay inside the
horizon).

# Key claims

1. **The transfer problem dissolved at the potential level**: AMR
   prolongation/restriction act on unconstrained $A$; taking the curl
   afterwards yields exactly solenoidal $B_h$ at every level and interface
   — the constructive use of the exactness converse
   ([discrete exactness theorems](/results/discrete-exactness-theorems.md)):
   transfer the potential, then differentiate.
2. **Uniform-grid equivalence to staggered CT** (after Del Zanna et al.):
   the A-evolution is CT by another parametrization; the AMR behavior is
   where the two part ways.
3. **Staggering retained**: $A_i$ on edges, $B^i$ on faces — the same
   $V_h^1$/$V_h^2$ placement as CT; the reformulation changes *which*
   object is evolved and transferred, not the collocation discipline.
4. **Scope note**: gauge dynamics of $A$ under AMR (zero-speed gauge modes
   at refinement boundaries) are not yet addressed here — taken up in the
   authors' later work (corpus papers, pending ingestion).

# Notation map

| Etienne et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $A_i$ on edges (Table I) | $V_h^1$ DOFs | vector potential |
| $\tilde B^i = \tilde\epsilon^{ijk}\partial_j A_k$ | $B_h = C_h A_h$ | densitized field, face-collocated |
| prolongation/restriction of $A$ | plain $P, R$ on $V_h^1$ | unconstrained — no $P_D$ needed |

# Pages created or updated

* Created [Vector-potential evolution](/methods/vector-potential-evolution.md).
* Updated [Divergence-space prolongation $P_D$](/operators/divergence-free-prolongation.md) (the potential route as alternative).

# Citations

1. `~/papers/mosaic/div-free-amr/2010-PRD-Etienne-101103PhysRevD82084031.pdf` (doi:10.1103/PhysRevD.82.084031) — text extraction, 23 pp.
