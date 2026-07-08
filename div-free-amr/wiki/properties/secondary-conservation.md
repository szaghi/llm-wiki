---
type: Property
title: "Secondary conservation"
description: "Discrete conservation of derived quantities — kinetic energy, entropy, vorticity, divergence relations — not among the scheme's unknowns; harder than primary conservation and decisive for fidelity."
status: established
tags: [conservation, secondary-conservation, invariant]
timestamp: 2026-07-08T00:00:00Z
---

# Secondary conservation

[Perot (2011)](/sources/perot-2011.md)'s taxonomy: **primary**
conservation concerns the scheme's own unknowns (mass, momentum, energy) —
flux-form methods get it locally almost for free, whatever the flux
approximation. **Secondary** conservation concerns *derived* quantities —
kinetic energy, entropy, vorticity, dilatation — which no flux form
guarantees; it is "typically much harder to achieve," and its absence has
named pathologies (carbuncles ↔ entropy violation; wrong turbulent
cascades ↔ kinetic-energy drift).

## Position in this bundle

The divergence constraint is the archetypal secondary invariant of this
corpus: $D_h B_h$ is not an unknown, and holding it exactly
([exact discrete divergence](/properties/exact-discrete-divergence.md))
requires structure beyond flux-form conservation — the once-per-edge EMF
assembly, the complex identity $D_h C_h = 0$. Two of Perot's observations
generalize across everything compiled here:

* **Sub-family phenomenon**: every discretization family (FD, FV, FE,
  spectral) contains a structure-preserving subset — the staggered/CT,
  mimetic, Whitney/FEEC, SBP branches of this wiki are exactly those
  subsets, one per language.
* **Formulation over discretization**: secondary conservation attaches to
  *how the problem is written* (fluxes vs potentials, which variables are
  fundamental) more than to the discretization family — compare the
  [vector-potential route](/methods/vector-potential-evolution.md), where
  reformulating makes the invariant automatic, at the price of a new
  secondary problem (gauge).

# Citations

1. [Perot (2011)](/sources/perot-2011.md), §§1–3, 5.
