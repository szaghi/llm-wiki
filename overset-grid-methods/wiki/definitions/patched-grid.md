---
type: Definition
title: "Patched (zonal) grids"
description: "Multizone grids whose subdomains meet along common boundaries without overlap: how the founding overset sources define them, contrast them with overset grids (zero-overlap limit, conservation, interface matching, metric discontinuities), and how Wang turns an overlap into a patch to make the overset interface conservative."
status: established
aliases: [patched grid, grid patching, zonal grid, multizone grid, multiblock grid, patched zones]
tags: [overset-grid, conservation, finite-volume, composite-grid]
timestamp: 2026-11-02T11:29:00Z
---

# Patched (zonal) grids

A **patched grid** decomposes the domain into subdomains (zones, blocks) that
are disjoint except for their common boundaries, $\Omega=\bigcup_k\Omega_k$ with
$\Omega_k\cap\Omega_{k'}=\Gamma_{kk'}$ a shared interface, each zone carrying its
own grid; zones communicate by fluxes or boundary data on $\Gamma_{kk'}$, not
through an overlap region. [Benek et al. (1983)](/sources/benek-1983.md),
p. 373, and [Benek et al. (1985)](/sources/benek-1985.md), p. 322, set grid
patching beside grid embedding and grid adapting as the three ways to reduce
grid-generation effort: patched subdomains share common boundaries, embedded
ones need a common overlap region instead. The contrast with
[overset grids](/definitions/overset-grid.md) runs through every founding
source.

## Patched grids in the founding sources

- **Variants recalled by Benek et al.** (1983, p. 373; 1985, p. 322): a global
  mesh with grid lines continuous across patches (Rubbert & Lee; Lee);
  separate solves per patch with patches overlapping by one point and coupled
  by transferring boundary data at coincident boundary points (Lasinski et al.);
  independent patch meshes coupled by conservative interface differencing (Rai).
  Benek et al. (1985), p. 324, decline Berger's generalization of Rai's
  conservative treatment to overlapping 2-D grids because its difference
  stencils would be "even more irregular" in 3-D.
- **Zero-overlap limit.** [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md),
  §2, p. 8: a patched grid "can in some sense be thought of as an overlapping
  grid with exactly zero overlap", and overlapping grids are the more flexible
  of the two.
- **Metric discontinuities.** [Henshaw (1994)](/sources/henshaw-1994.md), §1.2:
  composite overlapping grids avoid the metric discontinuities of multiblock
  patched grids, which makes high-order accuracy easier to obtain.
- **Conservation and matching.** [Wang (1995)](/sources/wang-1995.md), §1,
  list (a)–(b), Fig. 1: patched-grid schemes are fully conservative and need no
  inter-zone interpolation for cell-centred finite-volume schemes, but require a
  "perfect interface match"; overlapped grids allow arbitrary interface matches
  and relative motion, but are not fully conservative and need two-way
  interpolation. A multizone scheme whose interfaces are not treated
  conservatively is "zonally conservative" but "nonconservative globally"
  (p. 97).
- **On the sphere.** [Kageyama & Sato (2004)](/sources/kageyama-2004.md), §I,
  decompose a sphere either by patched grids (no overlap; Rai, as recalled) or
  by overset grids (partial overlap), and choose the overset
  [Yin–Yang grid](/definitions/yin-yang-grid.md). They count the cubed sphere,
  six component grids on the faces of a cube, among overset grids.

## The conservation condition on a patch

For two zones discretized conservatively by finite volumes, Wang (1995), §2,
Eq. (11), shows that the composite scheme is conservative if and only if the
total flux leaving one zone through the common boundary equals the total flux
entering the other:

$$
\sum_{f\in\Gamma_{k'\mid k}}\mathbf F_fS_f=-\sum_{f\in\Gamma_{k\mid k'}}\mathbf F_fS_f ,
$$

each sum taken with the outward normals of its own zone over the faces that
lie on the shared interface. On overlapping zones the corresponding conditions
involve the whole overlap region $\Omega_{kk'}$ — a unique rate of change of the
conserved quantities in it and a flux balance on both overlap boundaries
(Eqs. 8, 10) — and Wang judges enforcing them simultaneously "extremely
difficult, if not impossible" (§3).

## From overlap to patch

Wang's conservative Chimera (§3, Figs. 2–4) uses one overlap boundary, the part
$\Gamma_{k\mid k'}$ of the minor grid $G_k$'s boundary lying inside the major grid
$G_{k'}$, as a new internal patch boundary of $G_{k'}$. The overlapped pair
becomes two patched zones, $\Omega_{k'}\setminus\Omega_{kk'}$ and $\Omega_k$:
major-grid cells inside the minor grid become hole cells, cells cut by
$\Gamma_{k\mid k'}$ become cut cells with retained face fractions $W_f\in[0,1]$,
and the boundary segments of the minor grid are split by the major grid's faces
into "smallest faces", on each of which one Riemann flux is computed from the
adjacent cells of both grids. Conservation then reduces to the patch condition
above, the solution in the former overlap is unique, and no interpolation is
needed. The geometric work (zonal interface generation) costs about one flow
step in 2-D and is done once for static grids. The details are on
[conservative overset interface](/methods/conservative-overset-interface.md).
In the patched zones produced this way the interface coincides geometrically
while the faces of the two zones do not, the mismatch being absorbed by the
smallest faces.

## Qualifications

- Chesshire & Henshaw's zero-overlap reading treats a patch as a limit of the
  overlapping construction; their own interpolation theory needs $d>0$, the
  interpolation system becoming singular when receptors of the two grids
  coincide (§5.3), so the limit is not reached by their interpolation-based
  coupling *(compiler check, not in the sources)*
  ([fringe points](/definitions/fringe-point.md)).
- The classification of the cubed sphere as an overset grid is Kageyama &
  Sato's (§I); no other chunk-1 source classifies it.
- Wang prints Eq. (9) as $\sum_{\Delta V\in G}\frac{\partial Q}{\partial t}\Delta V=\sum_{f\in\Gamma_G}F_f\,dS_f$,
  without the minus sign carried by Eqs. (6)–(7); with $-\sum_{f\in\Gamma_G}$,
  Eqs. (6)–(9) yield Eq. (10) as printed *(compiler check, not in the sources)*.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — Introduction, p. 373 (three categories; patched-grid variants).
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 322 (three categories; Rubbert & Lee, Lasinski et al., Rai); p. 324 (Berger's conservative interface declined).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §2, p. 8 (zero overlap); §5.3 ($d>0$).
- [Henshaw (1994)](/sources/henshaw-1994.md) — §1.2 (metric discontinuities of patched grids).
- [Wang (1995)](/sources/wang-1995.md) — §1, Fig. 1; §2, Eqs. (8)–(11); §3, Figs. 2–4; §6.
- [Kageyama & Sato (2004)](/sources/kageyama-2004.md) — §I (patched vs overset on the sphere; cubed sphere).
