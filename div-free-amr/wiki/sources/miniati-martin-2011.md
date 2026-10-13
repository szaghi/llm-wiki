---
type: Source
title: "Miniati & Martin (2011) — Constrained-transport magnetohydrodynamics with adaptive mesh refinement in CHARM"
description: "12-solve CTU+CT MHD on Chombo patch AMR with a reflux-curl synchronization; divergence-free ghost interpolation found neither practical nor necessary under subcycling."
resource: "doi:10.1088/0067-0049/195/1/5"
source_kind: paper
authors: [Miniati F., Martin D.F.]
year: 2011
venue: "Astrophys. J. Suppl. Ser. 195:5"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2011-ApJS-Miniati-1010880067004919515.pdf"
tags: [constrained-transport, amr, ctu, refluxing, production-code, cosmology]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

CT-MHD in the cosmological AMR code CHARM (Chombo patch hierarchy):
full 12-solve unsplit [CTU](/sources/gardiner-stone-2008.md) with PPM for
cell-centered fluid variables, face-centered field evolved by Stokes on
edges, simplified 3D multidimensional MHD source terms. Level
synchronization: face-centered restriction and prolongation plus a
**reflux-curl operation** — edge EMF registers on coarse–fine interfaces,
coarse faces incremented by the curl of the EMF mismatch — maintaining
the solenoidal field across refinement boundaries (Balsara's
[electric-field correction](/methods/electric-field-correction.md), under
Chombo's refluxing vocabulary). Any even refinement ratio. Extensive
tests through full cosmological cluster formation;
$|\Delta x\,\nabla\cdot B|/|B| \sim$ few$\times 10^{-13}$ throughout.

# Key claims

1. **Reflux-curl = EMF correction, productionized**: implemented in
   analogy to Chombo's face-centered flux registers; the near-roundoff
   multilevel divergence demonstrates the interface operators' correctness
   at scale.
2. **Divergence-free ghost interpolation rejected in practice**: "neither
   practical nor necessary." The reason is structural, not lazy: the
   Balsara-2001 / Tóth–Roe schemes preserve solenoidality *of already
   divergence-free input*, but under subcycling the coarse field at
   intermediate times is only a **first-order time interpolation** — not
   divergence-free — so the exactness premise fails exactly when ghost
   filling happens, and the schemes' advantage degrades to that of plain
   interpolation ([$P_D$ page](/operators/divergence-free-prolongation.md)).
3. **Simplified MHD source terms**: the multidimensional predictor terms
   (cf. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md)) applied
   in a reduced 3D form "without loss of accuracy or robustness."

**CTU.** The integrator is Colella's [corner transport upwind](/methods/corner-transport-upwind.md); the 12-solve count is printed first in [Colella (1990)](/sources/colella-1990.md) §6.

# Notation map

| Miniati & Martin | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face $B$, edge $E$ | $B_h \in V_h^2$, $E_h \in V_h^1$ | CT standard |
| reflux-curl operator | EMF correction on $V_h^1$ registers | Balsara (2001) §V operation |
| face-centered restriction/prolongation | $R$, $P$ on face data | plain (non-$P_D$) for ghosts |

# Pages created or updated

* Updated [Electric-field correction](/methods/electric-field-correction.md) (reflux-curl production naming and validation).
* Updated [Divergence-space prolongation $P_D$](/operators/divergence-free-prolongation.md) (subcycling caveat: time interpolation breaks the divergence-free premise for ghost filling).

# Citations

1. `~/papers/mosaic/div-free-amr/2011-ApJS-Miniati-1010880067004919515.pdf` (doi:10.1088/0067-0049/195/1/5) — text extraction, 21 pp.
