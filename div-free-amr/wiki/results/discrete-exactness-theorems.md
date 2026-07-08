---
type: Result
title: "Discrete exactness theorems"
description: "On logically rectangular grids the natural discrete operators satisfy the vector-analysis theorems with converses: solenoidal iff a discrete curl, irrotational iff a discrete gradient."
status: established
tags: [mimetic, exactness, discrete-vector-analysis, divergence-constraint]
timestamp: 2026-07-08T00:00:00Z
---

# Discrete exactness theorems

**Statement** ([Hyman & Shashkov (1997)](/sources/hyman-shashkov-1997.md)).
For the natural discrete operators
$G_h : V_h^0 \to V_h^1$, $C_h : V_h^1 \to V_h^2$, $D_h : V_h^2 \to V_h^3$
([notation](/notation.md)) on logically rectangular — including
nonorthogonal and nonsmooth — grids:

1. $D_h \vec A = 0$ **if and only if** $\vec A = C_h \vec B$ for some
   $\vec B \in V_h^1$;
2. $C_h \vec A = 0$ **if and only if** $\vec A = G_h \varphi$ for some
   $\varphi \in V_h^0$;
3. discrete line integrals of $G_h \varphi$ are path-independent, equal to
   endpoint differences;
4. zero circulation over every closed discrete path implies gradient form.

## Why the converses matter

The composition identities $D_h C_h = 0$, $C_h G_h = 0$ are cheap — any CT
scheme embodies the first. The **converses** are the discrete Poincaré
lemma: the kernel of $D_h$ is *exactly* the image of $C_h$, so the space of
discretely solenoidal fields is completely parametrized by discrete vector
potentials. Consequences visible elsewhere in this bundle:

* Initializing $B_h$ from an edge vector potential loses nothing: *every*
  constraint-satisfying field is reachable
  ([exact discrete divergence](/properties/exact-discrete-divergence.md);
  Evans & Hawley's eq. 4.17 is the CT special case).
* Any divergence-preserving transfer operator (e.g.
  [$P_D$](/operators/divergence-free-prolongation.md)) can equivalently be
  built as "prolong the potential, then take $C_h$" — exactness guarantees
  the two routes span the same targets.
* The theorems hold on *distorted* grids: exactness is combinatorial
  (topology of the complex), with the metric entering only through the
  operator coefficients — the topology–metric factorization of the source.

**Scope.** Proved for the natural operators on logically rectangular grids
in 2D (with 3D formulations); simply connected domains implicit in the
potential constructions (the paper does not treat cohomological
obstructions of multiply connected domains).

## The finite-element counterpart

The same exactness holds for
[Whitney forms](/definitions/whitney-forms.md), with topology handled in
full ([Hiptmair (2002)](/sources/hiptmair-2002.md), Thm. 3.1 and Cor. 3.3):
the kernel of the discrete derivative equals the image of the previous one
**plus a discrete cohomology space whose dimension is the corresponding
Betti number** — on a ball-like domain the sequences are exact and the
statements above are recovered; on multiply connected domains the
obstruction is quantified rather than ignored. Two structural additions
from the FE side: the interpolation operators commute with the derivative
($d\,\Pi^l = \Pi^{l+1} d$), and the discrete potentials guaranteed by
exactness live *inside the finite element family* — a property Hiptmair
shows fails for componentwise Lagrangian elements, where the potential
escapes to a non-local $C^1$ space.

# Citations

1. [Hyman & Shashkov (1997)](/sources/hyman-shashkov-1997.md), §§4–5, conclusions.
2. [Hiptmair (2002)](/sources/hiptmair-2002.md), §3.
