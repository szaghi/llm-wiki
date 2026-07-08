---
type: Method
title: "Divergence-free reconstruction"
description: "Reconstructs point values of the magnetic field from face data so that the interpolated field itself satisfies the divergence constraint to high order."
status: established
tags: [high-order, reconstruction, divergence-constraint, constrained-transport]
timestamp: 2026-07-08T00:00:00Z
---

# Divergence-free reconstruction

The reconstruction step that lets a
[constrained-transport](/methods/constrained-transport.md)-type scheme keep
its divergence guarantee **above second order**. Introduced by
[Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md) from the
observation that the staggered cell-averaged constraint
$D_h^{\mathrm{f}} B_h = 0$ ([notation](/notation.md)) is an exact statement
about *cell averages*: at second order, averages and point values coincide
to $O(h^2)$ and the constraint is inherited pointwise, but for higher-order
schemes the two separate — and reconstructing each field component by
independent one-dimensional interpolations produces "a numerical
$\nabla\cdot\mathbf{B}$ of any size."

**Requirement**: the multidimensional interpolant of the field must be
built so that, for reconstruction accuracy of order $r$, the divergence of
the interpolated field vanishes to order $r{+}1$, with each normal
component continuous along its own longitudinal coordinate (discontinuities
admitted only transversally, where the characteristic modes live). The
reconstruction is therefore a *constrained, genuinely multidimensional*
interpolation of face data — the high-order generalization of the
prolongation problem: any operator producing point/fine values from face
averages must commute with the divergence to the scheme's order, or the
built-in invariant is silently destroyed at the reconstruction stage.

## The Balsara TVD construction

[Balsara (2001)](/sources/balsara-2001.md) §III gives a concrete
second-order realization: minmod-limited linear profiles for each face
field, completed by zone-interior quadratic vector polynomials
($a_{yy} = b_{xx} = 0$; coefficients bound by the continuous divergence-free
constraint) — the reconstructed field is divergence-free **at every point
of the zone**, reduces exactly to standard TVD reconstruction under 1D
variation, and supplies left/right Riemann states on faces. Its
area-weighted integration over fine faces is precisely the
[$P_D$ prolongation](/operators/divergence-free-prolongation.md), which is
why reconstruction quality governs AMR transfer quality.

# Citations

1. [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md), §3–4.
2. [Balsara (2001)](/sources/balsara-2001.md), §III.
