---
type: Source
title: "Mignone & Tzeferacos (2010) — A second-order unsplit Godunov scheme for cell-centered MHD: the CTU-GLM scheme"
description: "Fully cell-centered unsplit CTU scheme with mixed GLM cleaning, benchmarked head-to-head against eight-wave and staggered CT in PLUTO; competitive and simpler to implement."
resource: "doi:10.1016/j.jcp.2009.11.026"
source_kind: paper
authors: [Mignone A., Tzeferacos P.]
year: 2010
venue: "J. Comput. Phys. 229:2117-2138 (arXiv:0911.3410)"
local_file: "~/papers/mosaic/div-free-amr/2010-JCP-Mignone-101016jjcp200911026.pdf"
tags: [glm, ctu, unsplit, collocation, production-code, comparison, mhd]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The production case for the cell-centered route: a second-order,
dimensionally unsplit CTU scheme with **all variables (including
$\mathbf{B}$) cell-centered** and the constraint handled by
[mixed GLM cleaning](/methods/glm-divergence-cleaning.md) — fully
conservative in mass, momentum, induction, and energy, with no staggered
mesh and no elliptic solve. Verified by a **direct three-way comparison**
inside PLUTO (where both collocations are implemented) against Powell's
[eight-wave](/methods/eight-wave.md) and staggered
[CT](/methods/constrained-transport.md): the verdict is "robust, accurate
and competitive with recent implementations of the constrained transport
method while being considerably easier to implement in existing hydro
codes."

# Key claims

1. **Motivation is architectural**: same-location discretization of all
   primary variables "considerably ease[s] the extension to adaptive
   grids, to more complex physics and to schemes with higher than second
   order accuracy" — the collocated camp's standing argument, stated as
   the design driver.
2. **EGLM variant**: adding Dedner's divergence source terms (momentum and
   energy rows) breaks conservation of those quantities but is "more
   robust … in presence of strong discontinuit[ies] propagating through
   highly magnetized environments" — an explicit robustness/conservation
   trade inside the GLM family itself.
3. **Cleaning parameters made physical**: the damping parameter is
   $\alpha = \Delta t_d / \Delta t_a$, the ratio of diffusive
   ($\Delta h^2/c_p^2$) to advective ($\Delta h/c_h$) time scales.
4. **Head-to-head evidence**: 2D/3D test suite quantifies GLM vs eight-wave
   vs staggered CT under one code, one integrator (CTU), one reconstruction
   — the cleanest same-infrastructure comparison in this corpus.

# Notation map

| Mignone & Tzeferacos | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| cell-centered $\mathbf{B}$, $\psi$ | $B_h$ cell-collocated, $\psi_h$ | no staggering anywhere |
| $c_h$, $c_p$, $\alpha$ | GLM parameters | $\alpha = \Delta t_d/\Delta t_a$ |
| EGLM source terms | Dedner's eq. (4) extension | conservation-breaking variant |

# Pages created or updated

* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) (CTU-GLM production realization; EGLM trade; comparison verdict).

# Citations

1. `~/papers/mosaic/div-free-amr/2010-JCP-Mignone-101016jjcp200911026.pdf` (doi:10.1016/j.jcp.2009.11.026, arXiv:0911.3410) — text extraction, 31 pp.
