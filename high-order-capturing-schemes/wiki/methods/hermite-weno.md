---
type: Method
title: "Hermite WENO"
description: "WENO reconstruction or interpolation from more than one datum per cell (cell average and first moment, or point value and first derivative), which reaches a given order on a narrower stencil: a scheme between finite-volume WENO and DG, a stand-alone solver also for Hamilton–Jacobi equations, and above all a more compact WENO limiter for DG; the corpus holds only reviews and citations of it, no formulas."
status: established
aliases: [HWENO, Hermite-type WENO, Hermite WENO limiter, Hermite-type ENO]
tags: [weno, dg, limiter, reconstruction]
timestamp: 2026-10-13T00:00:00Z
---

# Hermite WENO

**Definition** ([Shu (2020)](/sources/shu-2020.md), §3.2.4). When each
cell or point carries more than one piece of information, for example a
cell average together with its first moment, or a point value together
with the first derivative, a high-order Hermite-type ENO or WENO
polynomial can be reconstructed or interpolated on a narrower stencil
than classical [WENO](/methods/weno.md) needs for the same order.

**Place between WENO and DG** ([Shu (2009)](/sources/shu-2009.md),
§5.1). Finite-volume WENO evolves one piece of information per cell; DG
of order $K + 1$ in 1D evolves $K + 1$, the moments $\hat u^{(l)}_i$,
$l = 0, \dots, K$. The Hermite WENO schemes of Qiu and Shu (2003, 2005,
not ingested) sit between them: they evolve a linear function per cell,
two pieces of information in 1D, and reconstruct the point values needed
to higher order. Because each cell holds more than one degree of
freedom, the same order needs a narrower stencil, which Shu presents as
one of two efforts to combine the advantages of WENO and DG.

**Uses named by the reviews.**
* *DG limiter.* In the two-step framework of
  [WENO limiters for DG](/methods/weno-limited-dg.md) (flag troubled
  cells, keep their averages, rebuild the higher moments), either
  classical or Hermite WENO can rebuild the moments; Hermite WENO "is
  more desirable since it involves a narrower stencil"
  ([Shu (2009)](/sources/shu-2009.md), §5.1), and it fits "the more
  compact DG data structure" ([Shu (2020)](/sources/shu-2020.md), §3.2.4).
  Qiu and Shu's 2005 WENO-limiter paper lists Hermite-type reconstruction
  among its planned improvements for more compact stencils
  ([Qiu & Shu (2005)](/sources/qiu-2005.md), §4).
* *Stand-alone solver*, including Hermite WENO schemes for
  Hamilton–Jacobi equations (Qiu and Shu 2005; finite-difference
  versions by Zheng, Shu and Qiu 2017, 2019, the latter on unstructured
  meshes; [Shu (2020)](/sources/shu-2020.md), §§3.2.4, 5).

**How compact is compact.** The two reviews differ in emphasis, not in
substance. In 2009 Shu stresses that the Hermite stencil is narrower than
the classical one. In 2020 he groups the first Qiu–Shu WENO limiters,
the Hermite ones among them (2003b, 2005b in his list), with those that
"used wider stencils than the original communication structure of DG
methods", which troubles parallel codes; limiters using only immediate
neighbours came later (Zhong and Shu 2013; Zhu, Zhong, Shu and Qiu 2017,
whose title calls theirs a "simple and compact Hermite WENO limiter")
([Shu (2020)](/sources/shu-2020.md), §4.3, reference list). Narrower
than classical WENO is therefore not yet DG-compact.

**Seen from a posteriori limiting** ([Dumbser et al. (2014)](/sources/dumbser-2014.md),
§3.1.2). Hermite WENO limiters were designed "to avoid the
non-compactness of the WENO limiters, but they are following a similar
idea": they share the WENO limiter's loss of part of DG's subcell
resolution, because the higher moments are still rebuilt from main-grid
data. Dumbser et al. cite them on 1D meshes (Qiu and Shu), unstructured
grids (Luo, Baum and Löhner 2007; Zhu and Qiu 2009) and in hybrid
RKDG+HWENO schemes with a subcell troubled-zone indicator (Balsara,
Altmann, Munz and Dumbser 2007). The alternative they develop is
[a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md).

**What the corpus lacks.** No ingested source prints a Hermite WENO
stencil, linear weights, smoothness indicator, order statement or test;
every primary paper named above is cited, not ingested. The page records
the definition and the reviewers' assessments only. The compact limiter
written out by [Balsara (2017)](/sources/balsara-2017-d.md) (§VI.2,
Zhong and Shu 2013) is on [WENO limiters for DG](/methods/weno-limited-dg.md);
that source does not call it Hermite WENO.

# Citations

1. [Shu (2020)](/sources/shu-2020.md), §§3.2.4, 4.3, 5.
2. [Shu (2009)](/sources/shu-2009.md), §5.1.
3. [Qiu & Shu (2005)](/sources/qiu-2005.md), §4.
4. [Dumbser, Zanotti, Loubère & Diot (2014)](/sources/dumbser-2014.md), §3.1.2.
5. [Balsara (2017)](/sources/balsara-2017-d.md), §VI.2.
