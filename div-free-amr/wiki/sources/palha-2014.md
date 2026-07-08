---
type: Source
title: "Palha, Rebelo, Hiemstra, Kreeft & Gerritsma (2014) — Physics-compatible discretization techniques on single and dual grids, with application to the Poisson equation of volume forms"
description: "The framework paper of the Delft mimetic school: forms vs pseudo-forms with Hodge-star as the switch, dual-grid (staggered-FV-like) vs single-grid (FE-like) methods proved equivalent."
resource: "doi:10.1016/j.jcp.2013.08.005"
source_kind: paper
authors: [Palha A., Rebelo P.P., Hiemstra R., Kreeft J., Gerritsma M.]
year: 2014
venue: "J. Comput. Phys. 257:1394-1422 (arXiv:1304.6908)"
local_file: "~/papers/mosaic/div-free-amr/2014-JCP-Palha-101016jjcp201308005.pdf"
tags: [mimetic, differential-forms, dual-grid, hodge, spectral-elements]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The conceptual framework behind the Delft mimetic spectral line
([mimetic spectral elements](/methods/mimetic-spectral-elements.md)):
physical quantities split into **forms and pseudo-forms** (inner vs outer
orientation — work changes sign under curve reversal, mass does not), with
the Hodge-$\star$ as the only operator crossing between them. Two
architectures follow: the **dual-grid** description ("resembles a
staggered finite volume method") keeps forms and pseudo-forms on primal
and dual meshes; the **single-grid** description ("strong resemblance with
a finite element method") keeps everything on one mesh and moves the
Hodge into the inner product. Both are worked out for the Poisson
equation of volume forms and **shown to give equivalent solutions**.

# Key claims

1. **The boxed principle**: a discrete system "will display the same
   structure/dynamics" as the continuous one exactly when the discrete and
   continuous operators **commute with the projection** — the Delft
   statement of the commuting-diagram criterion running through
   [FEEC](/definitions/finite-element-exterior-calculus.md) and this
   bundle.
2. **Orientation forces the architecture**: the forms/pseudo-forms
   distinction (Tonti/Bossavit lineage) is what generates dual grids —
   independently confirming the CDO orientation analysis
   ([Bonelle & Ern (2014)](/sources/bonelle-ern-2014.md)) from the
   spectral side.
3. **Staggered-FV and FE are the same physics, different Hodge placement**:
   the proved single/dual equivalence on the model problem makes the
   architectural choice a matter of where the metric sits, not which
   structure is preserved.
4. **Metric-free topology, metric-bearing closure**: integration of forms
   is metric-free, so all topological laws discretize exactly; grad, curl,
   div (vector versions) are metric-dependent, the exterior derivative is
   not — switching orthogonal ↔ curvilinear grids touches only the Hodge.

# Notation map

| Palha et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| forms / pseudo-forms | inner-/outer-oriented cochains | orientation types |
| Hodge-$\star$ | metric closure operator | single crossing point |
| mimetic projection | commuting $\pi$ | as in MMSEM |

# Pages created or updated

* Updated [Mimetic spectral elements](/methods/mimetic-spectral-elements.md) (framework: orientation split; single/dual equivalence).

# Citations

1. `~/papers/mosaic/div-free-amr/2014-JCP-Palha-101016jjcp201308005.pdf` (doi:10.1016/j.jcp.2013.08.005) — text extraction, 27 pp.
