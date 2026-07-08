---
type: Source
title: "Desbrun, Kanso & Tong (2008) — Discrete differential forms for computational modeling"
description: "Pedagogical DEC chapter whose distinctive content is the Whitney bridge: interpolating cochains to pointwise forms via Whitney k-forms, joining the DEC and FE-forms branches."
resource: "doi:10.1007/978-3-7643-8621-4_16"
source_kind: paper
authors: [Desbrun M., Kanso E., Tong Y.]
year: 2008
venue: "Oberwolfach Seminars 38 (Discrete Differential Geometry), Birkhäuser, pp. 287-323"
local_file: "~/papers/mosaic/div-free-amr/2008-Birkhauser-Desbrun-1010079783764386214_16.pdf"
tags: [dec, whitney-forms, differential-forms, pedagogy]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The pedagogical companion to
[DEC](/definitions/discrete-exterior-calculus.md), written for
computational modeling. Its distinctive contribution to this bundle is the
**explicit Whitney bridge** (§6): cochains suffice for the calculus, but
pointwise field values require interpolation — supplied by hat functions
for 0-forms, the Whitney 1-form
$\varphi_{ij} = \varphi_i\, d\varphi_j - \varphi_j\, d\varphi_i$ on edges,
and general Whitney $k$-forms — i.e. exactly the
[Whitney elements](/definitions/whitney-forms.md) of the FE branch,
adopted from inside DEC as *its own* reconstruction operator.

# Key claims

1. **DEC and Whitney/FEEC are two halves of one machine**: cochain
   calculus (combinatorial, exact) plus Whitney interpolation (pointwise,
   metric-bearing) — the chapter states from the DEC side the same
   junction the FE literature states from theirs.
2. **Cochains alone can't answer pointwise questions** — a candid
   limitation statement complementing the 2005 paper's formality caveat.

# Notation map

| Desbrun, Kanso & Tong | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\varphi_{i_0 \dots i_k}$ Whitney $k$-forms | Whitney reconstruction of $V_h^k$ | shared with FE branch |

# Pages created or updated

* Updated [Discrete exterior calculus (DEC)](/definitions/discrete-exterior-calculus.md) (Whitney bridge).

# Citations

1. `~/papers/mosaic/div-free-amr/2008-Birkhauser-Desbrun-1010079783764386214_16.pdf` (doi:10.1007/978-3-7643-8621-4_16) — text extraction, pp. 287–323.
