---
type: Property
title: "Exact discrete divergence"
description: "The algebraic invariant $D_h B_h = 0$: a specific discrete divergence of the evolved field vanishes identically, up to machine roundoff."
status: established
tags: [divergence-constraint, invariant, mhd]
timestamp: 2026-07-08T00:00:00Z
---

# Exact discrete divergence

The property that a scheme's evolved magnetic field satisfies
$$D_h B_h = 0$$
*algebraically* — the discrete divergence operator
$D_h : V_h^2 \to V_h^3$ ([notation](/notation.md)) annihilates the evolved
field by construction of the update, so the constraint holds to machine
roundoff at every step, independent of resolution, time step, or solution
smoothness.

Key structural facts, per [Evans & Hawley (1988)](/sources/evans-hawley-1988.md):

* **The constraint is initial data, not dynamics.** Analytically,
  $\nabla\cdot\mathbf{B}=0$ is preserved by the induction equation but not
  enforced by it; discretely the same holds — a scheme with this property
  preserves divergence *changes* at zero, so initial data must satisfy the
  constraint (edge-differencing a vector potential yields exactly
  divergence-free initial fields in the matching discrete sense), and
  boundary inflow can still inject violation.
* **The operator is scheme-specific.** "Exact" is always relative to one
  particular $D_h$ — for [constrained transport](/methods/constrained-transport.md)
  it is the face-flux difference over a cell (Evans & Hawley eq. 4.9, the
  discrete Gauss theorem). A field exactly solenoidal in one discretization
  is generally not solenoidal in another.
* **Roundoff behavior.** The invariant is exact in exact arithmetic; in
  floating point it accumulates roundoff at a problem-dependent rate
  (Evans & Hawley observe drift from $10^{-15}$ to $10^{-10}$ in single
  precision over one run; double-precision field evolution holds
  $10^{-15}$–$10^{-14}$).

## Why it matters

Nonzero numerical divergence produces an anomalous force component parallel
to the magnetic field, corrupting dynamics (Brackbill & Barnes 1980, as
reviewed in [Evans & Hawley (1988)](/sources/evans-hawley-1988.md) §III —
primary source not yet ingested).

# Citations

1. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §III–IV, eq. (4.7)–(4.9), (5.6).
