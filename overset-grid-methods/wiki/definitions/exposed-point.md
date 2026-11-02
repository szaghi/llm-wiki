---
type: Definition
title: "Exposed points"
description: "Points of a moving overlapping grid that were inactive (unused or receptors) at the old time level but whose old-time values the new-time stencils need, because an overlying grid has moved away: Henshaw and Schwendeman's definition, detection test and old-time interpolation remedy, and Meakin and Suhs's earlier rule that forbids them by limiting hole motion."
status: established
aliases: [exposed point, uncovered point, newly uncovered point, hole-to-field transition]
tags: [moving-grid, domain-connectivity, overset-grid, composite-grid]
timestamp: 2026-11-02T14:53:00Z
---

# Exposed points

When a component grid of an [overset grid](/definitions/overset-grid.md)
moves, the [point classification](/definitions/point-classification.md) of
the grids it overlaps changes: points that were hole (unused) points at time
level $n$ can become discretization points at level $n+1$, and points next to
them can need their old values. An **exposed point** is an inactive point at
level $n$, unused ($\mathcal H_k$) or a receptor ($\mathcal R_k$), that becomes
active when an overlying grid moves away; values at the previous time levels are
then needed there "so that all values used in the approximation of the PDE are
valid" ([Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md), §3.2,
Figs. 3–4, who name these points). The critical case is a point
$(\mathbf i,k)\in\mathcal H_k$ whose value $u^{k,n}_{\mathbf i}$ is used by
the discretization stencil of a point of $\mathcal D_k$ at level $n+1$: the
solver never updated it, so it carries no valid value. The issue arises only for
[moving overset grids](/methods/moving-overset-grid.md); a static assembly
never uncovers points.

## Detection

Henshaw & Schwendeman (2006), §3.2, test each point unused at level $n$
against the discretization points of the same grid at level $n+1$: with
$q_{\mathrm d}$ the width of the discretization stencil, $(\mathbf i,k)$ is
exposed if some new discretization point $(\mathbf j,k)$ satisfies

$$
\max_{1\le m\le n_d}\lvert i_m-j_m\rvert<\frac{q_{\mathrm d}-1}{2}
$$

(as printed; see Qualifications). Their slope-limited Godunov scheme has
$q_{\mathrm d}=5$ (§5). The test runs after the connectivity of the
predicted grid positions has been recomputed by Ogen and before the time step
is taken (`updateExposedPoints` in the PDEsolve algorithm, Fig. 6).

## Remedies

**Interpolate the old values (Henshaw & Schwendeman 2006).** An exposed point
is given values at the *previous* time level(s) by interpolation from the
other grids that cover it at that time; in the 1-D example of their Fig. 4,
the exposed $u^{k,n}_1$ is interpolated from two points of the overlapping
grid at level $n$. The scheme then advances as if the point had always been
active. The authors set aside the alternative of assigning *new*-time values to
the newly created discretization points (from neighbouring new values of both
grids, or by extrapolation), which "appears to be more difficult to implement
since it involves an implicit coupling between unknown values at the new time
level" (§3.2). The cost is negligible: 0.024 s
of 17.8 s per step (0.13%) on a moving grid and 0.0064 s of 3.81 s (0.17%) with
adaptive refinement (Table 6, 2.2 GHz Xeon).

**Forbid them by limiting the motion (Meakin & Suhs 1989).**
[Meakin & Suhs (1989)](/sources/meakin-1989.md), §II, Fig. 3, state the
underlying hazard for Chimera holes: a hole point must never become a field
point "without ever being updated through interpolation as a hole boundary
point", or undefined values enter the field computation. In their 1-D
illustration a hole moving one point per step is valid, because the uncovered
point was an interpolated hole-boundary point at the previous level; a hole
moving two points is invalid. Their restricted donor search, limited to the
points on either side of the old hole boundaries, therefore bounds the hole
motion to one point per step, a bound they state is far looser than the time
step the physics requires in all their moving-body cases
([hole cutting](/methods/hole-cutting.md); [donor search](/methods/donor-search.md)).

The two sources address the same failure from opposite sides: Meakin & Suhs
keep the receptor layer between hole and field thick enough in time that no
point is uncovered without a value; Henshaw & Schwendeman allow the uncovering
and repair the old values. Neither source compares the two.

## Relation to other point types

An exposed point is not an [orphan](/definitions/orphan-point.md): an orphan
is a receptor without a donor at the current level, an exposed point a former
hole point without a value at the previous level
([Meakin & Suhs (1989)](/sources/meakin-1989.md), §II; Henshaw & Schwendeman
2006, §3.2). Lee & Baeder's argument for updating hole points like other
points ([implicit hole cutting](/methods/implicit-hole-cutting.md)) does not
address uncovering, as recorded on [point
classification](/definitions/point-classification.md).

## Qualifications

- **Strict inequality.** Henshaw & Schwendeman print the test with a strict
  "$<$". In their own Fig. 4 example the stencil has width $q_{\mathrm d}=3$, so
  $(q_{\mathrm d}-1)/2=1$; the unused $u^{k,n}_1$ neighbours the new
  discretization point $u^{k,n+1}_2$ with $\lvert1-2\rvert=1\not<1$, yet the text
  declares it exposed. The non-strict "$\le$" reproduces the example; the paper
  prints no other form *(compiler check, not in the sources)*.
- Meakin & Suhs print the time-step remark twice with opposite literal
  meaning (§II, p. 646); the first statement, that the physics needs much
  smaller steps than the search restriction allows, is the one their context
  supports.
- Meakin & Suhs's term is not "exposed point"; the identification of their
  hole-to-field transition with Henshaw & Schwendeman's exposed point is made
  here *(compiler check, not in the sources)*.

# Citations

- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §3.2, Figs. 3–4 (definition, detection, old-time interpolation, alternative set aside); §5 (stencil width 5); Fig. 6 (PDEsolve); Table 6 (cost).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II DCF, Fig. 3 (hole-motion rule, undefined values, time-step remark).
