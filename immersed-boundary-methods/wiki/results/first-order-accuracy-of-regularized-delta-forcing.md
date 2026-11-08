---
type: Result
title: "First-order accuracy of regularized-delta forcing at interfaces"
description: "A singular interface force represented with a regularized delta function of width O(h) smears the jump in the normal derivative of the solution across the interface, so the method converges at first order near and, for the solution, everywhere, even though the delta function interpolates smooth fields to second order."
status: established
aliases: [first-order accuracy of the immersed boundary method, smearing error of discrete delta functions]
tags: [accuracy, delta-function, diffuse-interface, immersed-interface]
timestamp: 2026-11-08T17:31:00Z
---

# First-order accuracy of regularized-delta forcing at interfaces

**Statement.** Let a singular source or force be concentrated on an
interface $\Gamma$, so that the solution is continuous but its normal
derivative jumps across $\Gamma$. If the source is spread to a uniform grid of
width $h$ with a [regularized delta function](/operators/regularized-delta-function.md)
$\delta_h$ of support $O(h)$, the computed solution converges at first order in
$h$ in two or more dimensions, whatever the order of the interior scheme.

**Evidence.**

- *Measured.* [LeVeque & Li (1994)](/sources/leveque-1994.md), §5 Example 1,
  solve $\Delta u=\int\sigma\,\delta(\mathbf x-\mathbf X(s))\,ds$ with a circular
  $\Gamma$ and $[\partial_n u]=2$, using Peskin's cosine kernel (and a hat
  kernel, with "almost the same" results) and as many Lagrangian points as
  grid points per direction: the maximum error falls by about 2 per
  refinement (first order), against about 4 (second order) for the
  [immersed interface method](/methods/immersed-interface-method.md) (Table 1).
  "The discrete delta function approach smears the jump."
- *Argued.* LeVeque & Li (1994, §1): in 2-D "it does not appear to be
  possible to achieve second-order accuracy at all grid points using a
  right-hand side" of discrete-delta form; in 1-D the hat kernel is exact
  for $u''=c\,\delta(x-x_\Gamma)$ (citing Beyer and LeVeque 1992), so the
  limitation is multi-dimensional.
- *Stated.* [Peskin (2002)](/sources/peskin-2002.md), §6 and §8: the unit-sum
  and first-moment conditions make $\delta_h$ interpolate smooth functions to
  second order, but at a true immersed boundary the velocity "suffers a jump in
  its normal derivative" and the interpolation "is only first-order
  accurate"; the method, second order in space for smooth problems, is
  limited to first order for problems with immersed boundaries, the boundary
  being smeared over a thickness of order $h$.

**Scope.** The result concerns diffuse representations
([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md)).
Sharp treatments — jump-corrected stencils
([LeVeque & Li 1994](/sources/leveque-1994.md)), cut cells
([Ye et al. 1999](/sources/ye-1999.md)) and linear reconstruction in
[direct forcing](/methods/direct-forcing.md) ([Fadlun et al. 2000](/sources/fadlun-2000.md),
§2.3, where volume-fraction weighting is first order and reconstruction
second order) — recover second order.

# Citations

- [LeVeque & Li (1994)](/sources/leveque-1994.md) — §1, §5 Example 1, Table 1.
- [Ye et al. (1999)](/sources/ye-1999.md) — §1, §3.
- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §2.3.
- [Peskin (2002)](/sources/peskin-2002.md) — §6, §8.
