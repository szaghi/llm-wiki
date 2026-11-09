---
type: Method
title: "Hyperbolic grid generation"
description: "Body-fitted grids marched outward from a boundary by solving a hyperbolic system made of an orthogonality condition plus a prescribed arc-length increment or cell volume; fast (about one relaxation sweep of an elliptic generator) with good spacing control near the body, for problems whose outer boundary is free."
status: established
aliases: [hyperbolic grid generator, marching grid generation]
tags: [hyperbolic-generation, grid-generation, orthogonality]
timestamp: 2026-11-08T20:24:00Z
---

# Hyperbolic grid generation

[Steger & Chaussee (1980)](/sources/steger-1980.md) reinterpret the
constructive orthogonal-grid procedure of McNally and Graves (normals marched
from the body between prescribed level lines) as an initial-value problem for
two nonlinear partial differential equations. Marching the Cauchy–Riemann
equations would be ill posed, but the constraints make the system
**hyperbolic** in the marching direction $\eta$, so it is well posed for data
given on the body ($\eta=0$).

- **Arc-length scheme:** orthogonality $\mathbf x_\xi\cdot\mathbf x_\eta=0$ plus
  a prescribed increment $\Delta s^2=\mathbf x_\eta\cdot\mathbf x_\eta$.
- **Cell-volume scheme:** orthogonality plus a prescribed cell area,
  $x_\xi y_\eta-x_\eta y_\xi=V$. Because $J=V$ stays positive and finite the
  grid stays nonsingular, except where severe concavity makes lines coalesce
  like a shock.

Local linearization shows real distinct eigenvalues (for the cell-volume
scheme a symmetric coefficient matrix) whenever $J\ne0$. The authors use a
noniterative implicit scheme, central in $\xi$ and first order in the
marching direction, unconditionally stable, with added smoothing in concave
regions; the cost is about one sweep of a line-relaxation elliptic
generator.

The outer boundary is not prescribed, which suits external aerodynamics but
not closed domains: only elliptic systems take data on an entire closed
boundary ([Thompson, Thames & Mastin 1974](/sources/thompson-1974.md);
[elliptic grid generation](/methods/elliptic-grid-generation.md)).
Thompson, Warsi and Mastin (1982) note that, like all hyperbolic systems, the
generator propagates boundary discontinuities into the field.

# Citations

- [Steger & Chaussee (1980)](/sources/steger-1980.md) — whole paper.
- [Thompson, Thames & Mastin (1974)](/sources/thompson-1974.md) — introduction.
- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Section E.
