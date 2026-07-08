---
type: Operator
title: "SBP-preserving interpolation $I_{C2F}, I_{F2C}$"
description: "Interface interpolation pair between nonconforming SBP blocks that is adjoint in the interface norms and non-amplifying, preserving stability, accuracy, and conservation."
status: established
symbol: "$I_{C2F}, I_{F2C}$"
aliases: [SBP interpolation operators, glue operators]
tags: [sbp, interpolation, 2-1-interface, nonconforming, conservation]
timestamp: 2026-07-08T00:00:00Z
---

# SBP-preserving interpolation $I_{C2F}, I_{F2C}$

The pair of trace-space transfer operators coupling SBP blocks of
different resolution (canonically a 2:1 compression) or different operator
order, introduced by
[Mattsson & Carpenter (2010)](/sources/mattsson-carpenter-2010.md).
Interface data moves coarse→fine by $I_{C2F}$ and fine→coarse by
$I_{F2C}$ inside the SAT penalties; the base scheme's guarantees survive
iff ([notation](/notation.md)):

1. **Adjointness in the interface norms**:
   $$\mathsf{H}_F\, I_{C2F} = I_{F2C}^{\,T}\, \mathsf{H}_C ,$$
   the exact condition under which the SAT interface terms telescope in
   the energy estimate — conservation and strict stability inherit from
   the single-block proofs.
2. **Non-amplification**: $\mathsf{H}_C(I - I_{F2C} I_{C2F}) \ge 0$ and
   $\mathsf{H}_F(I - I_{C2F} I_{F2C}) \ge 0$ — the coarse–fine round trip
   is a contraction in energy.
3. **Accuracy with a boundary sacrifice**: exactness on polynomials to
   degree $p{-}1$ interior but only $\sim (p{-}1)/2$ near the interface
   ends — the trace analog of SBP boundary closures; in practice
   $p$th-order interpolation preserves the $p$th-order scheme.

## Structural remarks

* The adjoint condition is the same discipline as the mimetic
  [support-operator method](/definitions/support-operator-method.md)
  (derived operator := adjoint of prime in the discrete inner products)
  and the same shape as the volume commutation
  $D_H R = R\,D_h$: in each case the *pairing*, not the individual
  stencil, carries the invariant.
* These operators preserve the **energy** structure across 2:1 interfaces.
  Whether an analogous pair can preserve an **algebraic divergence**
  structure for collocated high-order FD at 2:1 interfaces is precisely
  the open question this bundle orbits — here the SBP branch delivers its
  strongest interface tool, and it is a stability/conservation tool, not a
  constraint-invariant one.

## Glue-space generalization

[Kozdon & Wilcox (2015)](/sources/kozdon-wilcox-2015.md) replace the
pairwise operators with **projections onto an interface glue space** of
discontinuous piecewise polynomials, each projection compatible with its
own block's $\mathsf{H}$-norm. Coupling factors through the intermediary,
so operators are built once per SBP operator regardless of the far side —
extending provably stable coupling to curved interfaces, non-matching
block corners, and SBP–DG hybrids (the Mattsson–Carpenter pairs required
matching corners; Nissen et al. removed that at fixed refinement ratio —
corpus paper, pending).

# Citations

1. [Mattsson & Carpenter (2010)](/sources/mattsson-carpenter-2010.md), §§2–4, Lemma 3.4.
2. [Kozdon & Wilcox (2015)](/sources/kozdon-wilcox-2015.md), §§2–4.
