---
type: Method
title: "SBP-SAT technique"
description: "Imposes boundary and interface conditions weakly through penalty terms that preserve the SBP energy estimate, coupling multi-block high-order FD schemes stably and conservatively."
status: established
aliases: [simultaneous approximation term, penalty method]
tags: [sbp, sat, interface-conditions, multi-block, stability]
timestamp: 2026-10-13T00:00:00Z
---

# SBP-SAT technique

The standard companion of [SBP operators](/definitions/summation-by-parts.md):
boundary and interface conditions are imposed **weakly**, by adding to the
semi-discretization a *simultaneous approximation term* — a penalty
proportional to the deviation of the boundary/interface data from the
imposed condition, scaled by $\mathsf{H}^{-1}$ ([notation](/notation.md))
so it acts at the boundary points. The penalty coefficients are chosen so
the SBP energy estimate survives with the boundary terms absorbed:
stability is proved, not observed. (The technique originates with
Carpenter, Gottlieb & Abarbanel — primary source not in this corpus; the
multi-block, curvilinear development compiled here is
[Nordström & Carpenter (1999)](/sources/nordstrom-carpenter-1999.md).)

## Multi-block interfaces

At an interface, both sides receive SATs penalizing the mismatch of the
coupled quantities. Findings of the curvilinear analysis:

* **Conforming interfaces** (matching gridlines, equal tangential metrics)
  admit conservative, strictly and strongly stable couplings — with the
  penalties on *fluxes*, whose normal components are the continuous
  quantities across the interface.
* **Penalize the right continuity**: flux-based coupling degenerates as the
  advective wave speed vanishes; variable-based coupling
  ($u=v$, matched derivatives) does not — the choice of penalized quantity
  is part of the stability design, not a cosmetic one.
* **Metric conditions**: in curvilinear coordinates the norm carries the
  Jacobian, and conservation/strict stability hold only under conditions on
  the discrete metric terms — non-smooth meshes put the metric derivatives
  on the critical path.

## Nonconforming interfaces

The conforming-interface assumptions above were later removed:
[SBP-preserving interpolation operators](/operators/sbp-preserving-interpolation.md)
($I_{C2F}, I_{F2C}$, adjoint in the interface norms and non-amplifying)
couple blocks of different resolution — including the 2:1 compression —
and even different operator orders, keeping strict stability, accuracy,
and conservation
([Mattsson & Carpenter (2010)](/sources/mattsson-carpenter-2010.md)).

## The strong-imposition alternative

SAT is not the only stable interface treatment: **SBP-GP** imposes
conditions strongly through ghost points, and at hanging-node refinement
interfaces the two were connected and compared by
[Wang & Petersson (2019)](/sources/wang-petersson-2019.md) — the improved
one-sided-ghost GP variant achieves fourth order with energy stability and
**no explicit time-step reduction** relative to the periodic problem,
where the SAT coupling pays an interface stiffness penalty. The choice
between weak and strong imposition is therefore a genuine trade
(implementation simplicity and generality vs time-step and system size),
not a settled default.

**Strong imposition in the original construction.** The first SBP
operators were used without penalties:
[Kreiss & Scherer (1974)](/sources/kreiss-scherer-1974.md) (§3, eq. 3.4)
semi-discretize a symmetric hyperbolic system with the boundary
conditions on the ingoing characteristics imposed on the grid function
itself (the grid function "satisfies the boundary conditions"), and
assert that "there is no difficulty in deriving an
energy estimate" without writing it out. They have no penalty terms, which
is consistent with SAT originating later. They also assert that
interpolation between overlapping grids can be built "in such a way that
no stability problem arises" (p. 199), with neither construction nor
reference: an unproved claim, not an interface result.

# Citations

1. [Nordström & Carpenter (1999)](/sources/nordstrom-carpenter-1999.md), §§3–5.
2. [Mattsson & Carpenter (2010)](/sources/mattsson-carpenter-2010.md), §§3–4.
3. [Wang & Petersson (2019)](/sources/wang-petersson-2019.md), §§2–5.
4. [Kozdon, Erickson & Wilcox (2021)](/sources/kozdon-2021.md) — the
   hybridized form: independent trace variables on block faces carry all
   coupling; Schur elimination of volume unknowns leaves a small SPD
   face-only system (elliptic problems, repeated solves).
5. [Kreiss & Scherer (1974)](/sources/kreiss-scherer-1974.md), pp. 198–199, §3, eq. 3.4.
