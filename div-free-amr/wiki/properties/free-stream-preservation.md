---
type: Property
title: "Free-stream preservation"
description: "A constant (free-stream) state remains exactly constant under the scheme, independent of grid refinement pattern, mesh distortion, or velocity field."
status: established
tags: [free-stream, invariant, amr, conservation]
timestamp: 2026-07-08T00:00:00Z
---

# Free-stream preservation

The property that a spatially constant state — a scalar field without
sources, a uniform flow — is an exact fixed point of the discrete scheme:
no refinement pattern, interface, mesh distortion, or advecting velocity
manufactures variation from constancy. Like the
[exact discrete divergence](/properties/exact-discrete-divergence.md), it
is an *algebraic* property of the scheme's stencils rather than an accuracy
statement: violations are not truncation error decaying with $h$ but
spurious source terms at special locations (interfaces, metric
discontinuities) that persist under refinement of the feature causing them.

In [Almgren et al. (1998)](/sources/almgren-1998.md) it is an explicit
design requirement of the
[AMR projection method](/methods/amr-projection-method.md): advected
scalars remain constant "independent of grid refinement patterns and the
velocity field," engineered by building all advective fluxes from a single
MAC-projected (discretely divergence-free) velocity — a constant $c$ then
advects with flux $c\,u_h$ whose divergence vanishes exactly — together
with the interface synchronization suite.

Structural kinship: free-stream preservation is to the *state* what the
divergence constraint is to the *field* — both demand exact cancellation in
the scheme's algebra, both are threatened at exactly the same places (2:1
interfaces, transfer operators), and a transfer operator that breaks one
typically breaks the other.

# Citations

1. [Almgren et al. (1998)](/sources/almgren-1998.md), §1, §3.
