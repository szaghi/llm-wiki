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
smoothness. The velocity analog $D_h u_h = 0$ (incompressibility) is the
older sibling: the [MAC method](/methods/mac-method.md)
([Harlow & Welch (1965)](/sources/harlow-welch-1965.md)) already enforced
the face-difference stencil $D_h^{\mathrm{f}} u_h = 0$ cell-by-cell — though
by elliptic solve (tolerance-level), not algebraically.

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
  it is the face-flux difference over a cell, $D_h^{\mathrm{f}}$
  (Evans & Hawley eq. 4.9, the discrete Gauss theorem). A field exactly
  solenoidal in one discretization is generally not solenoidal in another.
  [Tóth (2000)](/sources/toth-2000.md) makes the stencil-dependence
  systematic: the collocated recast of the CT variants conserves the
  corner-centered $D_h^{\mathrm{k}}$ but *not* the natural cell-centered
  $D_h^{\mathrm{c}}$
  ([CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md));
  central-difference schemes conserve $D_h^{\mathrm{c}}$ to roundoff; the
  [projection method](/methods/projection-method.md) enforces
  $D_h^{\mathrm{c}}$ to solver tolerance;
  [eight-wave](/methods/eight-wave.md) bounds it by truncation error only.
* **No stencil choice is physically privileged.** For conservative
  shock-capturing schemes, no discrete divergence constraint eliminates all
  unphysical Lorentz-force effects — exact orthogonality of the discrete
  acceleration to $B_h$ in every cell is incompatible with momentum
  conservation
  ([conservation–orthogonality incompatibility](/results/conservation-orthogonality-incompatibility.md));
  Tóth: the choice of discretization "is always somewhat arbitrary."
* **Roundoff behavior.** The invariant is exact in exact arithmetic; in
  floating point it accumulates roundoff at a problem-dependent rate
  (Evans & Hawley observe drift from $10^{-15}$ to $10^{-10}$ in single
  precision over one run; double-precision field evolution holds
  $10^{-15}$–$10^{-14}$).

* **Stencil consistency is testable.** The 3D field-loop advection test
  ($(x,y)$-plane loop, $v_z \ne 0$) detects mismatch operationally: if the
  constraint is held on a stencil different from the one used to build the
  $B_z$ fluxes, $B_z$ grows unphysically; round-off-constant $B_z$
  certifies preservation on the *consistent* stencil
  ([Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md)).

## Why it matters

Nonzero numerical divergence produces an anomalous force component parallel
to the magnetic field, corrupting dynamics (Brackbill & Barnes 1980, as
reviewed in [Evans & Hawley (1988)](/sources/evans-hawley-1988.md) §III —
primary source not yet ingested).

# Citations

1. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §III–IV, eq. (4.7)–(4.9), (5.6).
2. [Tóth (2000)](/sources/toth-2000.md), §1.1, §4.4, §7, Appendix A.
3. [Harlow & Welch (1965)](/sources/harlow-welch-1965.md), eqs. (6)–(10).
4. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §1, §6.
