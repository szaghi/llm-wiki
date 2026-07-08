---
type: Method
title: "Eight-wave formulation"
description: "Powell's non-conservative source-term formulation: advects divergence errors with the flow, holding the constraint to truncation error only."
status: established
aliases: [Powell source terms, 8-wave]
tags: [eight-wave, source-terms, divergence-constraint, shock-capturing]
timestamp: 2026-07-08T00:00:00Z
---

# Eight-wave formulation

Powell's modification of the conservative MHD system: source terms
proportional to $\nabla\cdot\mathbf{B}$ are added (derivable from physical
principles when the $\nabla\cdot\mathbf{B}=0$ Maxwell equation is not
invoked), plus a matching eighth wave in the Riemann solver. Divergence
errors are not eliminated but *advected with the flow*, preventing local
accumulation; the constraint holds to truncation error only — the weakest
guarantee among the families compared by
[Tóth (2000)](/sources/toth-2000.md) (Powell's primary reports are not yet
ingested).

## Properties, per [Tóth (2000)](/sources/toth-2000.md)

* **Non-conservative — with consequences.** By the Lax–Wendroff theorem only
  conservative schemes are guaranteed correct jump conditions; Tóth's rotated
  shock-tube test demonstrates the failure concretely: across strong
  discontinuities the source terms produce **incorrect jumps that do not
  converge away with resolution**, even though the solution appears to
  converge normally.
* **Grid-agnostic and simple:** no staggering, no elliptic solve; usable on
  any grid type; requires only source terms and a Riemann-solver
  modification of the base scheme.
* **Usually adequate:** in most of the ten test problems it "works
  correctly" with small divergence errors and competitive accuracy — the
  failure mode is occasional, not generic.
* Initial/boundary data must satisfy the constraint to second-order accuracy
  (contrast the roundoff-exact compatibility CT requires:
  [exact discrete divergence](/properties/exact-discrete-divergence.md)).

# Citations

1. [Tóth (2000)](/sources/toth-2000.md), §§2–3, 6.3, 7.
