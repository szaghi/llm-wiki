---
type: Operator
title: "SBP-preserving interpolation $I_{C2F}, I_{F2C}$"
description: "Interface interpolation pair between nonconforming SBP blocks that is adjoint in the interface norms and non-amplifying, preserving stability, accuracy, and conservation."
status: established
symbol: "$I_{C2F}, I_{F2C}$"
aliases: [SBP interpolation operators, glue operators]
tags: [sbp, interpolation, coarse-fine-interface, nonconforming, conservation]
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

## The accuracy bound and its circumvention

For second-derivative PDEs the interface truncation error was later shown
to cost **one full order of global convergence**, and the cause is a
theorem, not an implementation defect: interpolation accuracy is capped by
the quadrature order of the SBP norm — for interior order $2p$,
$q_{C2F} + q_{F2C} \le 2p+1$. The **order-preserving (OP) remedy**
([Almquist, Wang & Werpers (2019)](/sources/almquist-2018.md)): use *two*
interpolation pairs, each obeying the bound but with the accuracy budget
split oppositely, placed asymmetrically in the SATs so the accurate
direction covers the error that matters — full conforming-interface
convergence restored, with existence proved for any two diagonal-norm SBP
schemes and any interface point distribution.

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
* **Partial answer, hypothesis-grade** ([Zaghi (2026)](/sources/zaghi-2026.md)).
  A sixth-order collocated FD code tested the question at its 2:1 seams.
  Two findings point to *no*:
  * The energy-stable route targets the wrong invariant. On the failing run
    the field energy stays flat (−3%) while the seam divergence grows 145×,
    so an SBP–SAT coupling would bound what is already bounded. The record
    cites Koley et al. for the absence of a discrete divergence bound in that
    framework.
  * A matched seam operator that does carry the divergence structure,
    telescoping $D_h^{\mathrm{c}} C_h^{\mathrm{c}}$ to order 6 across the
    jump, is eigenvalue-unstable. It lacks exactly the adjointness that
    condition 1 above supplies.

  So, in the tested constructions, the energy structure and the divergence
  structure each impose their own interface condition, and no single
  operator met both ([seam divergence source](/results/collocated-seam-divergence-source.md)).
  This is the pattern of the nonlinear caveat below, now for the
  divergence.

## Glue-space generalization

[Kozdon & Wilcox (2015)](/sources/kozdon-wilcox-2015.md) replace the
pairwise operators with **projections onto an interface glue space** of
discontinuous piecewise polynomials, each projection compatible with its
own block's $\mathsf{H}$-norm. Coupling factors through the intermediary,
so operators are built once per SBP operator regardless of the far side —
extending provably stable coupling to curved interfaces, non-matching
block corners, and SBP–DG hybrids. On the adaptive-grid side,
[Nissen et al. (2014)](/sources/nissen-2014.md) take the pairs into
genuine block-AMR: stable **junction (corner) operators** where interfaces
of different refinement meet — the configuration two-block analyses never
see — plus interior-stencil coupling across same-level block boundaries,
paying a local accuracy tax at junctions that numerically does not
dominate the global error.

## The nonlinear caveat

Interface machinery certified in the $L_2$ energy norm does **not**
automatically preserve nonlinear invariants: at h/p nonconforming DG
interfaces, the standard mortar projection "does not guarantee entropy
stability for non-linear problems, which can lead to instabilities" — a
targeted modification of the coupling restores provable entropy stability
at unchanged cost
([Friedrich et al. (2018)](/sources/friedrich-2018.md)). The pattern
mirrors the accuracy story above: each additional property (conservation,
accuracy order, entropy) imposes its own condition on the transfer
operators, and none is implied by the others.

# Citations

1. [Mattsson & Carpenter (2010)](/sources/mattsson-carpenter-2010.md), §§2–4, Lemma 3.4.
2. [Kozdon & Wilcox (2015)](/sources/kozdon-wilcox-2015.md), §§2–4.
3. [Nissen et al. (2014)](/sources/nissen-2014.md), §§3–5.
4. [Almquist, Wang & Werpers (2019)](/sources/almquist-2018.md), §§3–4, 7.
5. [Lundquist, Malan & Nordström (2018)](/sources/lundquist-2018.md) — general-mesh hybrid extension: the coupling conditions posed on arbitrary node sets, enabling stable high-order-FD-to-unstructured-FV interfaces.
6. [Friedrich et al. (2018)](/sources/friedrich-2018.md), §§3–4.
7. [Zaghi (2026)](/sources/zaghi-2026.md): issue #29 (E3, fix-class A, the energy diagnostic).
