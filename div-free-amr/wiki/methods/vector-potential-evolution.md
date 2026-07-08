---
type: Method
title: "Vector-potential evolution"
description: "Evolves the magnetic vector potential instead of the field; B = curl A is exactly divergence-free on any grid, and AMR transfer acts on the unconstrained potential."
status: established
aliases: [A-method, potential-based CT]
tags: [vector-potential, constrained-transport, amr, grmhd]
timestamp: 2026-07-08T00:00:00Z
---

# Vector-potential evolution

Evolve $A_h \in V_h^1$ (edge-collocated) by the uncurled induction
equation and *define* the field as
$$B_h = C_h A_h,$$
so $D_h B_h = 0$ holds identically by $D_h C_h = 0$
([notation](/notation.md)) — on every grid, level, and interface, with no
constraint machinery at all. The modern AMR form is
[Etienne, Liu & Shapiro (2010)](/sources/etienne-2010.md) for GRMHD; on
uniform grids it is numerically equivalent to staggered
[constrained transport](/methods/constrained-transport.md), of which it is
the potential-level parametrization.

## Why it wins at AMR — and what it costs

* **Transfer without $P_D$**: the potential is unconstrained, so
  prolongation and restriction can use *any* interpolation — the entire
  divergence-preserving-transfer problem
  ([$P_D$](/operators/divergence-free-prolongation.md),
  [locality limits](/results/transfer-operator-locality-limits.md)) is
  dissolved rather than solved, by the exactness converse: every
  solenoidal field is a curl, so transfer the preimage.
* **The historical costs return**: evolving $A$ was the *original* CT-era
  alternative, and [Evans & Hawley (1988)](/sources/evans-hawley-1988.md)
  rejected it on uniform grids because the Lorentz force needs *second*
  differences of $A$, generating anomalous currents under limited
  reconstruction. The modern HRSC formulations evolve $A$ with the same
  shock-capturing machinery as the fluid, mitigating but not erasing the
  extra-derivative concern.
* **Gauge dynamics is the new constraint — diagnosed and priced**: in the
  simple algebraic gauge the $A$-system carries a **static (zero-speed)
  gauge mode**; interpolation errors at refinement boundaries excite it in
  place, and the result is *spurious magnetic fields at interfaces* —
  divergence-free by construction, and wrong — that grow until the run
  fails. The cure is spectral, not accuracy: the **Lorenz gauge** has only
  propagating modes, so interface noise leaves the grid
  ([Etienne et al. (2012)](/sources/etienne-2012.md)). Note the moral for
  this bundle: exact constraint satisfaction does not certify a correct
  field — the constraint-consistent error channel simply moves elsewhere.

The trade is precise: CT holds the invariant on the *field* and pays at
interfaces (EMF corrections, $P_D$); the potential route holds it by
*construction* and pays in derivative count and gauge control.

# Citations

1. [Etienne, Liu & Shapiro (2010)](/sources/etienne-2010.md), §§I–III.
2. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §III (the second-derivative objection).
3. [Etienne et al. (2012)](/sources/etienne-2012.md), §§I–III, V.
4. [Etienne et al. (2015)](/sources/etienne-2015.md) — production form: damped generalized Lorenz gauge $\nabla_\mu A^\mu = \xi n_\mu A^\mu$ (transport *and* damping for the gauge sector, mirroring GLM's design).
