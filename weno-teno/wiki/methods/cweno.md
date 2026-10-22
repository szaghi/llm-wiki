---
type: Method
title: "Central WENO (CWENO)"
description: "Central WENO schemes combine candidate polynomials of unequal size, including a central high-order one, with linear weights that may be any positive numbers summing to one, independent of the stencil geometry; the bundle's sources recall them as the stability-oriented branch of WENO from which WENO-AO and WENO-ZQ descend."
status: established
aliases: [CWENO, central WENO, compact central WENO, CWENO3]
tags: [weno, cweno, reconstruction, finite-volume]
timestamp: 2026-10-21T12:00:00Z
---

# Central WENO (CWENO)

Central WENO schemes (Levy, Puppo & Russo, with later work by Cravero, Semplice, Coco, Russo and
Visconti, as recalled by Balsara et al. 2024, §I, Fu 2021, §1 and Deng 2023, §1) are WENO
reconstructions in which the candidate set contains stencils of **unequal size**, typically a large
central stencil carrying the design order and smaller stencils for shock capturing. Their defining
freedom, in Fu's words (2021, §1), is that "the optimal linear weights can be arbitrary positive
numbers provided that the sum equals one"; Fu (2023, §1) says they "can be arbitrary as long as their
sum equals one". Deng (2023, §1) gives the
consequence: because the linear weights are determined independently of the reconstruction stencil,
CWENO extends more easily to non-uniform grids.

## Position in the WENO family

- **Stability before accuracy.** Balsara et al. (2024, §I) place CWENO in a recent trend of scheme
  design that "has also begun to emphasize stability": CWENO schemes "emphasize the central, and most
  stable, stencil over and above all the other stencils". Fu (2023, §1) groups CWENO with its cognate
  variants WENO-AO and WENO-ZQ as alternatives "which emphasize more on numerical stability by
  introducing the unequal-size candidate stencils and the tailored weighting strategy", and Fu (2021,
  §1) speaks of "a tailored stencil selection procedure".
- **Unstructured meshes.** Balsara et al. (2024, §I) recall extensions to unstructured meshes
  (Friedrichs; Käser & Iske; Dumbser & Käser).
- **Descendants.** [WENO-AO](/methods/weno-ao.md) hybridizes large central high-order stencils with
  an $r=3$ WENO for stability; WENO-ZQ (Zhu & Qiu) hybridizes a central stencil with an
  extrema-clipping van Albada limiter; multi-resolution WENO (Zhu & Shu) uses a hierarchy of nested
  central stencils (Balsara et al. 2024, §I). Balsara et al. claim for WENO-AO, against WENO-ZQ, that
  it preserves local extrema.
- **Third order.** Deng (2023, §1) recalls third-order compact CWENO schemes on the three-cell stencil
  and their refinements, and judges that their performance "is usually dependent on parameters in an
  ad hoc way"; with the other third-order WENO schemes they are said to seek a trade-off between
  accuracy and oscillations that is "not necessarily optimal". Deng's own answer is the
  [ROUND](/methods/round-scheme.md) family.

## Relation to TENO

TENO also uses candidate stencils of unequal width, but it keeps or discards each stencil with a
sharp cut-off and renormalized linear weights; its incremental stencils make the linear combination
"always work" on uniform and non-uniform Cartesian meshes because each stencil contains the
evaluation point, whereas negative or non-existent linear weights appear on unstructured meshes (Fu
2023, §2.5; [targeted ENO](/methods/targeted-eno.md)). Fu (2021, §1) cites CWENO, WENO-AO and
WENO-ZQ as the cognate unequal-stencil approaches when he introduces TENO-AA, which tests nested
large symmetric stencils before falling back on three small ones
([adaptive TENO](/methods/adaptive-teno.md)).

## Qualifications

- No ingested source of chunk 1 prints a CWENO reconstruction formula; the content above is what the
  sources state about the family. The formulas of the AO variant are on the
  [WENO-AO](/methods/weno-ao.md) page.

# Citations

- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Deng (2023)](/sources/deng-2023.md) — §1.
- [Fu (2023)](/sources/fu-2023.md) — §1; §2.5.
- [Fu (2021)](/sources/fu-2021.md) — §1.
