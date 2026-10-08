---
type: Result
title: "Locality limits of divergence-preserving transfer"
description: "At 2:1 interfaces, local divergence-preserving prolongation and restriction both exist only for face-staggered storage; vertex collocation loses local restriction, cell collocation loses both."
status: established
tags: [amr, prolongation, restriction, collocation, impossibility, divergence-constraint]
timestamp: 2026-07-08T00:00:00Z
---

# Locality limits of divergence-preserving transfer

**Statement** ([Tóth & Roe (2002)](/sources/toth-roe-2002.md)). For
second-order transfer at factor-of-2 resolution changes on Cartesian grids,
the existence of *local* divergence-preserving operators depends on
storage:

| Storage | local $P_D$ | local $R$ with $D_H R = R D_h$ |
|---|---|---|
| face-centered staggered | **yes** | **yes** (flux summation) |
| vertex-based collocated | yes (with tangentially-averaged divergence) | **no** — global only |
| cell-centered collocated | not found | not found (global projection instead) |

**The vertex-restriction obstruction** (their §4.2): coarsening eight fine
cells in place must alter the vector components at the coarse-cell corners —
but each corner is shared by seven *unrefined* neighboring fine cells, whose
divergences would change; keeping corners fixed instead breaks
$D_H = \tfrac18\sum d_h$, since edge- and face-center fine components enter
the fine divergences but not the coarse one. Only a globally applied
restriction (multigrid-style) preserves the constraint — "not in the
adaptive mesh refinement context."

## Consequences

* The verbatim conclusion: face-centered storage is indicated "for AMR
  schemes which require the divergence-free property" — locality of *both*
  transfer directions is a property of the staggered ($V_h^2$) placement,
  not of divergence preservation per se.
* For collocated schemes, the divergence-preserving options at interfaces
  degrade to global operations (projection/cleaning) — connecting the
  transfer problem to the constraint-strength taxonomy of
  [exact discrete divergence](/properties/exact-discrete-divergence.md).
* The result is *constructive* on the negative side for vertex storage (an
  explicit sharing argument) but only *observational* for cell-centered
  storage ("does not seem to lend itself") — the cell-collocated case is an
  open assertion, not a proof.

## Evidence on the cell-collocated row (hypothesis-grade)

[Zaghi (2026)](/sources/zaghi-2026.md), a high-order collocated
finite-difference code with an exact interior divergence, adds three
things. All are `status: hypothesis` (from the human's own record):

* **A narrow theorem.** For point values with the conservation-consistent
  mean restriction, exact $R P = I$ caps the prolongation at second order
  ([point-value restriction bound](/results/point-value-restriction-compatibility.md)).
  A conservation-compatible round trip and high order are mutually
  exclusive at a collocated interface. Face-staggered fluxes escape this
  because flux summation is additive.
* **A constructive negative.** A matched collocated seam operator that makes
  $D_h^{\mathrm{c}} C_h^{\mathrm{c}}$ telescope to sixth order across the
  2:1 jump exists, and it is eigenvalue-unstable. So for this route, too,
  the obstruction is not the existence of a divergence-preserving formula.
  It is the conflict between that formula and stability.
* **An inductive verdict.** Five classes of local fix were ruled out with
  evidence, and the record concludes that "no local collocated-FD fix
  exists" ([seam divergence source](/results/collocated-seam-divergence-source.md)).

Together these strengthen the "not found / not found" row without proving
it: the row stays an assertion, now with a partial theorem and a failed
construction behind it. The record's only exact route is the one this
result recommends, face-staggered storage at the seam.

# Citations

1. [Tóth & Roe (2002)](/sources/toth-roe-2002.md), §§3–4, 7.
2. [Zaghi (2026)](/sources/zaghi-2026.md): issues #21 (N0), #29, #30.
