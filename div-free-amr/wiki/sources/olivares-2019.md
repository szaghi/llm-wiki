---
type: Source
title: "Olivares et al. (2019) — Constrained transport and adaptive mesh refinement in the Black Hole Accretion Code"
description: "Staggered upwind-CT on AMR in GRMHD (BHAC), with coordinate-independent divergence-preserving prolongation operators; divergence-control choice shown to change accretion results qualitatively."
resource: "doi:10.1051/0004-6361/201935559"
source_kind: paper
authors: [Olivares H., Porth O., Davelaar J., Most E.R., Fromm C.M., Mizuno Y., Younsi Z., Rezzolla L.]
year: 2019
venue: "Astron. Astrophys. 629:A61"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2019-A&A-Olivares-10105100046361201935559.pdf"
tags: [constrained-transport, amr, grmhd, prolongation, production-code, upwind-emf]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Brings staggered-mesh CT — the Londrillo–Del Zanna upwind-CT line — onto
the AMR hierarchy of BHAC (GRMHD in arbitrary stationary spacetimes), the
code behind Event Horizon Telescope theoretical models. The technical
core: **a general class of divergence-preserving prolongation operators
for face-allocated variables**, derived as a *coordinate-independent
generalization* of the Cartesian constructions
([Tóth & Roe (2002)](/sources/toth-roe-2002.md)) — extending
[$P_D$](/operators/divergence-free-prolongation.md) to curvilinear
coordinates and curved spacetimes. Implementation is documented to
transplant level (ghost exchange, data structures, coarse–fine and
polar-axis treatments).

# Key claims

1. **$P_D$, coordinate-independent**: the prolongation class preserves the
   staggered divergence on faces in general geometry — the third
   published construction after Balsara's polynomial and Tóth–Roe's flux
   formulations, and the first freed from Cartesian metric assumptions.
2. **The constraint-control choice changes the science**: "the choice of
   the divergence-control method can produce qualitative differences in
   the simulation results for scientifically relevant accretion problems"
   — cleaning-based BHAC (its earlier default) vs the new staggered CT
   differ beyond convergence cosmetics on production problems.
3. **Motivation hierarchy stated plainly**: cleaning couples to AMR
   "straightforwardly" (why it was the AMR default across GRMHD codes);
   staggered CT on AMR needs the machinery of this paper — the
   effort-vs-integrity trade the whole field navigates.

# Notation map

| Olivares et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face-allocated $B$, upwind CT EMFs | $B_h \in V_h^2$, $E_h \in V_h^1$ | LDZ/Del Zanna lineage |
| divergence-preserving prolongation | $P_D$, general coordinates | coordinate-independent class |

# Pages created or updated

* Updated [Divergence-space prolongation $P_D$](/operators/divergence-free-prolongation.md) (coordinate-independent generalization).
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md) (production evidence: control-method choice changes results qualitatively).

# Citations

1. `~/papers/mosaic/div-free-amr/2019-A&A-Olivares-10105100046361201935559.pdf` (doi:10.1051/0004-6361/201935559) — text extraction, 21 pp.
