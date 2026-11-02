---
type: Definition
title: "Composite overlapping grid"
description: "Chesshire and Henshaw's formal definition of an overlapping grid: logically rectangular component grids mapped from the unit square or cube, a valid composite grid in which every point is a discretization, interpolation or unused point, the parameters it depends on, and the mapping method of discretizing on it."
status: established
aliases: [composite grid, composite mesh, overlapping grid, overlaid grid, composite overlapping mesh]
tags: [composite-grid, overset-grid, domain-connectivity, finite-difference]
timestamp: 2026-11-02T11:29:00Z
---

# Composite overlapping grid

A **composite overlapping grid** is a set $\mathcal G=\{G_k\}_{k=1}^{n_g}$ of
logically rectangular, curvilinear component grids; each $G_k$ is the image of
a uniform grid on the unit square (unit cube in 3-D) under a smooth mapping
$\mathbf x=\mathbf d_k(\mathbf r)$, $\mathbf r\in[0,1]^{n_d}$, onto a subdomain
$\Omega_k$; the subdomains cover $\Omega$ and overlap where they meet, and the
solutions on different components are matched by interpolation equations
([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §1, §3.1;
[Henshaw (1994)](/sources/henshaw-1994.md), §2). It is the formal,
Kreiss-school statement of what the Chimera papers call an
[overset grid](/definitions/overset-grid.md); a point is labelled $(\mathbf i,k)$
with position $\mathbf x^k_{\mathbf i}$ and parameter coordinates
$\mathbf r_{\mathbf i}$. [Benek et al. (1985)](/sources/benek-1985.md), p. 323,
use "composite mesh" for the output of PEGSUS in the same sense.

## Validity and point classification

Chesshire & Henshaw (1990), §3.2, p. 16, call a composite grid **valid** when
every point $(\mathbf i,k)$ is one of:

1. a **discretization point** — an *interior* point, which can be discretized
   to the required order by a centred stencil of user-given width $q_{\mathrm d}$
   whose points are discretization or interpolation points of $G_k$, or a
   *boundary* point on the true boundary $\partial\Omega$ that can be
   discretized in the same sense (the boundary-condition stencil may differ);
2. an **interpolation point** — a point that can be interpolated, to the
   required order and with a "sufficiently centred" stencil, from discretization
   or interpolation points of another grid $G_{k'}$, $k'\neq k$;
3. an **exterior or unused point** — neither.

In registry terms these are $\mathcal D_k$, $\mathcal R_k$ and $\mathcal H_k$
([point classification](/definitions/point-classification.md)); CMPGRD stores
them in the signed flag translated here as $\iota_k$. The categories can
overlap (a discretization point may also be interpolable); CMPGRD seeks the
valid grid with the fewest interpolation points. A **null grid**, in which
every point is unused, is valid but useless; enough overlap avoids it.

The composite grid built from given components is not unique. It depends on
four parameters (§3.2, p. 14; Fig. 9): the interpolation width $q$ (per
direction and grid pair, CMPGRD's `iw`), the discretization width
$q_{\mathrm d}$, the minimum allowable overlap, and the **ordering** of the
component grids, higher-numbered grids covering lower ones
([grid hierarchy and priority](/definitions/grid-hierarchy.md)). Changing the
order changes which points are removed; all grids, even the top one, lose
points (Fig. 9). A centred three-point discretization needs one line of
interpolation points at an interpolation boundary, a five-point one two lines
(§3.2, p. 14); Henshaw (1994) uses two lines with $q=5$ for his fourth-order
scheme. The overlap $d$ and width $q$ needed for a given accuracy are the
subject of the [interpolation-order
requirement](/results/interpolation-order-requirement.md); explicit and implicit
use of interpolation points as donors is defined on
[explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md).
The algorithm that turns component grids into a valid composite grid is
described on [domain connectivity](/definitions/domain-connectivity.md) and
[CMPGRD](/software/cmpgrd.md).

## Why overlapping components

Chesshire & Henshaw (1990), §2, p. 7, list the limits of a single mapping:
forced non-uniform point density (a "narrow-waist" region), the global effect
of any local change, and a necessary singularity for regions that are not the
smooth image of a square — the Jacobian of any map of the unit square onto a
disc is singular at some corners. Composite grids lift these limits: each
component can be generated almost independently, and "it is wise to have about
equal grid spacings where grids overlap" (§3.1, p. 11). The layout they describe fits
thin boundary-conforming grids along each boundary, built by marching along
normals (valid while the grid width is small against the boundary's radius of
curvature), and covers the interior with a Cartesian grid (§3.1; §5.4, where
smoothed-corner polygonal boundary grids are built). Henshaw (1994), §1.2,
adds that composite grids avoid coordinate singularities — a sphere's poles are
covered by two or more patches, as in his two-grid spherical-shell test
(Table VII) — and the metric discontinuities of multiblock patched grids, which
eases high-order accuracy.

## Discretizing on a composite grid: the mapping method

On each component the PDE is written in the parameter coordinates by the
chain rule (Chesshire & Henshaw 1990, §5.1, Eq. 5.2), with the metric
$\partial r_m/\partial x_n$ supplied by CMPGRD at the grid points:

$$
\frac{\partial u}{\partial x_n}=\sum_{m=1}^{n_d}\frac{\partial r_m}{\partial x_n}\frac{\partial u}{\partial r_m},\qquad
\frac{\partial^2u}{\partial x_n^2}=\sum_{m,m'}\frac{\partial r_m}{\partial x_n}\frac{\partial r_{m'}}{\partial x_n}\frac{\partial^2u}{\partial r_m\partial r_{m'}}+\sum_m\frac{\partial^2r_m}{\partial x_n^2}\frac{\partial u}{\partial r_m},
$$

and the $r$-derivatives are replaced by centred differences on the uniform
parameter grid ($\Delta r_m$), the second metric derivatives being differenced
from the first. This non-conservative form needs smoother mappings than a
finite-volume method, which the authors say composite grids make easy to
obtain. Henshaw (1994), §2, uses the same form with fourth-order differences
$\nabla_4$, $\nabla_4^2$ and two ghost lines.

As a method of lines (Chesshire & Henshaw 1990, §5.6, Eq. 5.9) the composite
system is: $\mathrm d\mathbf u^k_{\mathbf i}/\mathrm dt=\mathbf f^k_{\mathbf i}(\mathbf U,t)$
at interior points, boundary conditions at boundary points, and the
interpolation equations
$\mathbf u^k_{\mathbf i}=\sum_{\mathbf j\in\mathcal S_{\mathbf i}}\alpha_{\mathbf j}\mathbf u^{k'}_{\mathbf j}$
at receptors. An explicit step advances the interior and then refreshes boundary
and interpolation points; an implicit step solves the stepping equations
together with the interpolation equations. Different time-stepping on different
component grids is natural; their IMEX scheme (trapezoidal implicit part,
second-order Adams–Bashforth explicit part) is chosen per grid in the CGNVT
runs (§6.3).

## Cost of the composite structure

For explicit time stepping the storage overhead over a single-grid code is
essentially the flag array ($N_{\mathrm{pts}}$ integers) plus the interpolation
arrays; for the implicit CGNVT run on the coarsest cylinder grid the sparse
solver takes 2,673,907 of 2,802,678 words (Chesshire & Henshaw 1990, Table IX,
whose printed sparse-solver subtotal is 100 words below the sum of its rows,
72,241 + 2,601,766 = 2,674,007 *(compiler check, not in the sources)*).
Interpolation cost depends on how it is done: 2% of a step for explicit
interpolation in Henshaw's cylinder run, 17% for implicit interpolation in his
sphere run, where the 10,728 interpolation points are a large fraction of all
points (Henshaw 1994, Tables V, VIII). Multigrid on composite grids (CGMG)
reaches convergence rates "almost as good" as on a single grid; CMPGRD builds
the coarse composite levels, which are not simply the fine grids with lines
removed (Chesshire & Henshaw 1990, §5.5, as reported there).

## Lineage

Chesshire & Henshaw (1990), §1, recall Starius (1977, Schwarz alternating
procedure for elliptic problems on two overlapping meshes; 1980, Lax–Wendroff
stability on a 1-D overlapping mesh), Reyna (method-of-lines stability), B.
Kreiss (1983, grid construction and hyperbolic problems, the origin of
CMPGRD), Pärt (finite-volume adaptation), and the theses of Henshaw and
Chesshire; they cite the Chimera scheme of Benek, Steger and Buning as the
parallel approach and contrast Berger's overlapping rectangular grids, which
serve adaptivity rather than geometry.

## Qualifications

- **Ordering independence is a conjecture.** Chesshire & Henshaw (1990), §3.2,
  p. 16, state that if a valid composite grid exists for some ordering, a valid
  grid "should result for all orderings", and say explicitly that this is not
  proved.
- **Non-conservative.** Neither the mapping-method discretization nor the
  interpolation conserves; the authors leave conservation at interpolation
  boundaries to future work (§6.4, §7); see
  [conservative overset interface](/methods/conservative-overset-interface.md).
- Chesshire & Henshaw print the method-of-lines interpolation equation (5.9c)
  with donor values on grid $k$ instead of $k'$; their Eq. (5.3) has the correct
  donor index.

# Citations

- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §1 (definition, lineage); §2, p. 7 (single-mapping limits); §3.1, p. 11 (component grids); §3.2, pp. 14–16, Fig. 9 (valid grid, point types, parameters, ordering conjecture); §5.1, Eq. (5.2); §5.5; §5.6, Eq. (5.9); Table IX.
- [Henshaw (1994)](/sources/henshaw-1994.md) — §1.2 (singularities avoided); §2 (components $\mathbf d_k$ from the unit cube, fourth-order mapping method); Tables V, VII, VIII.
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 323 (composite mesh as PEGSUS output).
