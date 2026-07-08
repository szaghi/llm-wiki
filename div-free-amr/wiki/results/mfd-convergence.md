---
type: Result
title: "MFD convergence on polyhedral meshes"
description: "The mixed-form mimetic finite difference method is stable and converges at optimal rates for scalar and flux variables on general polyhedral meshes, including degenerate elements."
status: established
tags: [mimetic, convergence, polyhedral, stability, amr]
timestamp: 2026-07-08T00:00:00Z
---

# MFD convergence on polyhedral meshes

**Statement**
([Brezzi, Lipnikov & Shashkov (2005)](/sources/brezzi-lipnikov-shashkov-2005.md)).
For the linear diffusion problem in mixed first-order form
($F = -K\,\mathrm{grad}\,p$, $\mathrm{div}\,F = b$), the mimetic finite
difference discretization — face-flux and cell-scalar unknowns, operators
built by the [support-operator](/definitions/support-operator-method.md)
discipline — is **stable and converges at the optimal rates for both
variables** on unstructured polyhedral meshes satisfying mild shape
assumptions (nonconvex and degenerate elements admitted). Proof by a
direct technique (the "lift property"), not via equivalence with mixed
finite elements.

## Consequences

* **The mimetic promises become theorems**: exact local conservation,
  operator symmetry/positivity, and null-space control — previously
  design principles with strong empirical support — now carry a
  convergence guarantee on essentially arbitrary cell shapes.
* **Hanging nodes without special treatment**: because a locally refined
  or nonmatching mesh is a conformal polyhedral mesh with degenerate
  elements (faces meeting at 180°), the 2:1 interface is *inside* the
  proven class — the mimetic route to AMR needs no interface-specific
  operator construction, in sharp contrast to the bespoke transfer
  operators of the staggered-CT
  ([$P_D$](/operators/divergence-free-prolongation.md)) and SBP
  ([$I_{C2F}$](/operators/sbp-preserving-interpolation.md)) branches. The
  price: MFD here is low-order and implicit/elliptic in character, not a
  high-order explicit FD scheme.

**Scope.** Stationary diffusion (elliptic), mixed form, full tensor
coefficients; 3D with 2D analog; says nothing per se about hyperbolic
constraint transport — the relevance to this bundle is the interface
philosophy and the proof that mimetic structure survives degenerate cells.

# Citations

1. [Brezzi, Lipnikov & Shashkov (2005)](/sources/brezzi-lipnikov-shashkov-2005.md), §§2–5, Appendix.
