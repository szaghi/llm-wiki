---
type: Result
title: "Restriction-compatibility bound for point-value prolongation"
description: "For point-value DOFs with the conservation-consistent mean restriction, exact round-trip compatibility R P = I is incompatible with reproducing quadratics: compatible ghost fills are at most second-order."
status: hypothesis
aliases: [R P = I wall, point-value Guzik constraint]
tags: [amr, prolongation, restriction, ghost-fill, collocation]
timestamp: 2026-10-12T00:00:00Z
---

# Restriction-compatibility bound for point-value prolongation

**Setting.** A collocated scheme stores **point values** at cell centers. At
a 2:1 interface each coarse cell of width $H$ covers $2^d$ fine cells whose
centers sit at offsets $\pm H/4$ along each axis. Let the restriction $R$ be
the mean of the $2^d$ fine values. In a point-value scheme this is the
restriction consistent with discrete conservation, because the conserved
total is the cell sum. Let the prolongation $P$, which fills fine ghosts
from coarse data ($\Gamma$, [notation](/notation.md)), be linear.

**Statement** ([Zaghi (2026)](/sources/zaghi-2026.md), issue #21;
`status: hypothesis` per bundle law, though the proof below is complete).
If $P$ reproduces quadratics exactly, then $R P \ne I$. Equivalently, a
prolongation with exact round-trip compatibility $R P = I$ has ghost
accuracy at most $q = 2$.

**Proof.** Take $u = x_1^2$ around the coarse anchor $x_1 = 0$, so the
coarse point value is $0$. A $P$ exact on quadratics returns $u$ at every
fine center, $(\pm H/4)^2 = H^2/16$, so
$$R P\, u = \frac{H^2}{16} \ne 0 = u(0).$$
Hence $R P = I$ forces $P$ to be inexact on $x_1^2$. Exactness on linear
functions is still available: the symmetric three-node pair
$[-1, 8, 1]/8$ and $[1, 8, -1]/8$ satisfies $R P = I$ for arbitrary data. $\blacksquare$

## Why it matters

* **The cell-average constraint does not carry over to point values.** In
  high-order finite-volume AMR, the conservation constraint on ghost
  interpolation (fine averages summing to the coarse average) is compatible
  with high order. Exact polynomial cell averages satisfy it automatically,
  by additivity of the integral. Point values have no such additivity, so
  the same constraint destroys order. This sharpens the asymmetry between
  averaged and pointwise DOFs at refinement interfaces, already visible in
  the [transfer locality limits](/results/transfer-operator-locality-limits.md).
* **Order, not compatibility, is load-bearing for the seam divergence.** In
  the record's A/B test on a source-free 2:1 seam, the compatible $q = 2$
  fill lowered the seam divergence by a constant factor (about 2×) with zero
  convergence slope. The plain tricubic $q = 4$ fill (with $R P \ne I$)
  converged at $p_{\mathrm{obs}} \approx 1.1$–$1.6$
  ([seam divergence source](/results/collocated-seam-divergence-source.md)).
* **Scope.** The bound concerns the *mean* restriction only. Whether some
  other restriction admits exact $R P = I$ together with a high-order $P$
  is not addressed. Any such restriction would not be the
  conservation-consistent one, so the theorem is a statement about
  conservation-consistent round trips for point values, not about transfer
  operators in general.

**Data points from a GPU lattice-Boltzmann AMR** (point values at cell
centres, mean restriction, linear or cubic ghost fill;
[Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §§3.4, 5.3). The paper does not test $R P = I$.
* Cubic ghost fill, which reproduces quadratics and so is not
  restriction-compatible, gives a drag coefficient on a square cylinder
  that matches the finest uniform grid. Linear fill "is seen to degrade
  accuracy". This is consistent with order, not compatibility, being
  load-bearing.
* The authors' attempt at a cubic fine-to-coarse restriction was unstable
  "even when the root grid was refined and the mesh adaptivity was
  disabled", so they kept the mean. This is single-source and given
  without analysis.

# Citations

1. [Zaghi (2026)](/sources/zaghi-2026.md): issue #21, comment N0 (proof and amended design), N3 (A/B measurement), closing summary item 2.
2. [Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §§3.4.3, 5.3, Table 7.
