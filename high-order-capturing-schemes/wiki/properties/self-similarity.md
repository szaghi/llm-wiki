---
type: Property
title: "Self-similarity (scale invariance) of capturing schemes"
description: "A scheme is self-similar if its result does not change when the solution is rescaled, or when the grid spacing and time step are scaled together at fixed ratio — no thresholds tied to the mesh size or to the solution's units; WENO keeps it through scaled smoothness indicators, and mesh-dependent regularizations or extrapolation weights break it."
status: established
aliases: [scale invariance, self-similar scheme, dimensionless weights]
tags: [weno, nonlinear-weights, design-principle, boundary-treatment]
timestamp: 2026-10-08T00:00:00Z
---

# Self-similarity (scale invariance) of capturing schemes

**Definition** ([Shu (2009)](/sources/shu-2009.md), §3.5.1). If ε is a
small fraction of the typical size of $u$, the WENO reconstruction is
unchanged by rescaling $u$ or changing $h$. A FV or FD WENO scheme is then
self-similar: its solution does not change when $h$ and $\Delta t$ are
scaled together at fixed $\Delta t/h$. No mesh-dependent thresholds are
needed, and Shu calls this "very important". He discourages modifications
made only to allow analysis, "especially … if the modification destroys
the self-similarity property" (§7).

**How WENO keeps it.** The factor $h^{2l-1}$ in the
[smoothness indicator](/definitions/smoothness-indicator.md) removes the
dependence on $h$ ([Jiang & Shu (1996)](/sources/jiang-1996.md), §2).

**Where it is broken or contested.**
* *Mesh-dependent regularization.* $\varepsilon = h^{r-1}$
  ([Castro, Costa & Don (2011)](/sources/castro-2011.md), §4), $\varepsilon$
  between $O(h^3)$ and $O(h^2)$ for energy-stable WENO
  ([Fisher et al. (2011)](/sources/fisher-2011.md)), and $\varepsilon = h^2$
  for third-order WENO ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md),
  §3.2.1) are chosen for accuracy at critical points. Henrick et al. call ε
  dimensional: a fixed value decides the observed order on fine grids
  ([Henrick et al. (2005)](/sources/henrick-2005.md), §4.3;
  [weight accuracy conditions](/results/weno-weight-accuracy-conditions.md)).
  This is a conflict of design principle with Shu's requirement, not a
  factual contradiction.
* *Human note (2026-10-08), `status: hypothesis`.* ε is not a
  non-dimensional parameter, and its dependence on the mesh and on the
  flow (the solution's scale) is a real concern. Neither a fixed ε nor a
  mesh-scaled ε is free of it. The human's judgment, recorded on request,
  not a claim of any source.
* *Boundary extrapolation weights.* Tan and Shu's WENO extrapolation for
  inverse Lax–Wendroff takes its linear weights as powers of $h$. Lu et al.
  (2021) call this a loss of self-similarity and use constant weights.
  Baeza et al. (2016) build weights that are dimensionless and
  scale-independent by construction. A 3D moving-body variant still uses
  weights in $h_x^2 + h_y^2 + h_z^2$
  ([Lu et al. (2021)](/sources/lu-2021.md), §2.1;
  [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §4;
  [Liu et al. (2022)](/sources/liu-2022.md), Appendix C;
  [weighted extrapolation](/methods/weighted-extrapolation.md)).

# Citations

1. [Shu (2009)](/sources/shu-2009.md), §§3.5.1, 7.
2. [Jiang & Shu (1996)](/sources/jiang-1996.md), §2.
3. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §4.
4. [Fisher et al. (2011)](/sources/fisher-2011.md), §§2.2, 5.2.
5. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §3.2.1 (arXiv v2).
6. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §4.3.
7. [Lu et al. (2021)](/sources/lu-2021.md), §2.1.
8. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §4.
9. [Liu et al. (2022)](/sources/liu-2022.md), Appendix C.
