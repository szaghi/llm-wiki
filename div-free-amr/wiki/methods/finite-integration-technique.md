---
type: Method
title: "Finite integration technique (FIT)"
description: "Discretizes Maxwell's integral equations exactly as topological matrix equations on a primal-dual grid pair, confining all error and material content to discrete Hodge matrices."
status: established
aliases: [FIT, Maxwell-Grid-Equations]
tags: [fit, electromagnetics, dual-grid, hodge, maxwell]
timestamp: 2026-07-08T00:00:00Z
---

# Finite integration technique (FIT)

Weiland's discretization of Maxwell's equations in **integral form** on a
primal–dual grid doublet $\{G, \tilde G\}$, reviewed by
[Clemens & Weiland (2001)](/sources/clemens-weiland-2001.md). Degrees of
freedom are integral quantities — edge voltages $\hat e$, facet fluxes
$\hat b$ on the primal complex; magnetomotive forces and
dielectric/current fluxes on the dual — and the **Maxwell-Grid-Equations**
$$\mathsf{C}\hat e = -\frac{d}{dt}\hat b, \quad \mathsf{S}\hat b = 0,
\qquad \tilde{\mathsf{C}}\hat h = \frac{d}{dt}\hat d + \hat j, \quad
\tilde{\mathsf{S}}\hat d = q,$$
use only incidence matrices ($\{-1,0,1\}$ entries) and hold **exactly**:
$\mathsf{S}\hat b = 0$ is an algebraic invariant of the update, conserved
by $\mathsf{S}\mathsf{C} = 0$ — the electromagnetic twin of
[exact discrete divergence](/properties/exact-discrete-divergence.md) via
$D_h C_h = 0$.

## Structure

* **All error in the Hodge matrices.** Constitutive laws couple primal and
  dual DOFs through material matrices — discrete Hodge operators carrying
  every bit of metric and material information; the topological equations
  are error-free. Approximation quality, symmetry, and conditioning are
  therefore properties of the Hodge matrices alone (diagonal on orthogonal
  doublets; symmetric non-diagonal in nonorthogonal N-FIT; identical in
  role to edge-FE mass matrices built from
  [Whitney forms](/definitions/whitney-forms.md)).
* **Provable-before-computing conservation**: charge and energy
  conservation follow algebraically from the operator identities,
  explaining long-term-stable time stepping and spurious-mode-free
  eigenproblems.
* **Placement**: the grid doublet is the electromagnetic realization of
  the primal–dual complex — the same placement discipline as the
  [staggered grid](/definitions/staggered-grid.md) and the
  [Yee scheme](/methods/yee-scheme.md). Within FIT, the explicit leapfrog
  FDTD scheme appears as the standard time integrator (with a
  dual-staggered time axis), and discrete energy conservation is proved
  for it algebraically.

# Citations

1. [Clemens & Weiland (2001)](/sources/clemens-weiland-2001.md), §§1–4.
