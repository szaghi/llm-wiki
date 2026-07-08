---
type: Definition
title: "Orientation (inner/outer)"
description: "The two orientation types of geometric quantities — circulation-like (inner) vs flux-like (outer) — which force primal-dual mesh pairs, with the Hodge operator as the only crossing."
status: established
aliases: [inner and outer orientation, forms and pseudo-forms, ordinary and twisted forms]
tags: [orientation, differential-forms, dual-grid, hodge]
timestamp: 2026-07-08T00:00:00Z
---

# Orientation (inner/outer)

Geometric quantities carry one of two orientation types. **Inner** (internal)
orientation is orientation *of* the object itself — a direction along a
curve, a rotation sense in a surface: circulations and work change sign
when it flips. **Outer** (external) orientation is orientation of the
object's *complement* — a crossing direction through a surface, a screw
sense around a curve: fluxes change sign when *it* flips, while mass in a
volume changes sign under neither.

Three communities found the same distinction independently, in three
vocabularies now unified on this page:

* *inner/outer orientation* — the CDO analysis
  ([Bonelle & Ern (2014)](/sources/bonelle-ern-2014.md)): discrete
  differential operators act only between entities of the *same*
  orientation type; the discrete Hodge alone crosses types;
* *forms/pseudo-forms* — the Delft school
  ([Palha et al. (2014)](/sources/palha-2014.md)): the split generates the
  dual-grid (staggered-FV-like) and single-grid (FE-like) architectures;
* *ordinary/twisted forms* — lattice field theory
  ([Teixeira (2013)](/sources/teixeira-2013.md)): Maxwell's $F$ is
  ordinary, $G = \star F$ twisted, hence $E, B$ on the primal lattice and
  $D, H$ on the dual.

## Why it matters here

Orientation is the *reason* primal–dual (staggered) structure exists: the
two orientation types cannot share one mesh without breaking the exactness
of the topological laws, and every framework in this bundle — the
[staggered grid](/definitions/staggered-grid.md),
[FIT](/methods/finite-integration-technique.md)'s grid doublet,
[DEC](/definitions/discrete-exterior-calculus.md)'s circumcentric duals,
[Whitney/FEEC](/definitions/whitney-forms.md) with its single-grid Hodge in
the mass matrix — is one answer to where the orientation crossing is paid.
The registry's complex $V_h^0 \to V_h^1 \to V_h^2 \to V_h^3$
([notation](/notation.md)) implicitly fixes one orientation type per
degree; its dual complex carries the other.

# Citations

1. [Bonelle & Ern (2014)](/sources/bonelle-ern-2014.md), §1.
2. [Palha et al. (2014)](/sources/palha-2014.md), §§1, 3.
3. [Teixeira (2013)](/sources/teixeira-2013.md), §3.
