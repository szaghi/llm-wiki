---
type: Operator
title: "Divergence-space prolongation $P_D$"
description: "Prolongation of face magnetic fields constructed so the prolonged fine field is exactly divergence-free whenever the coarse field is."
status: established
symbol: "$P_D$"
aliases: [divergence-free prolongation]
tags: [amr, prolongation, divergence-constraint, coarse-fine-interface]
timestamp: 2026-07-08T00:00:00Z
---

# Divergence-space prolongation $P_D$

The transfer operator $P_D : V_H^2 \to V_h^2$ ([notation](/notation.md))
carrying coarse face-field data to fine faces such that the divergence
constraint survives the transfer:
$$D_H B_H = 0 \;\Rightarrow\; D_h (P_D B_H) = 0,$$
the prolongation half of the commutation requirement $D_h P = P_D D_H$.

## The Balsara construction

[Balsara (2001)](/sources/balsara-2001.md) §IV instantiates $P_D$ at second
order on the staggered ($D_h^{\mathrm{f}}$) formulation:

1. From the six coarse-zone face averages, build the
   [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
   — limited linear face profiles plus interior quadratic polynomials
   constrained to be divergence-free *pointwise in the whole zone*.
2. **Prolong by area-weighted integration** of those polynomials over each
   fine face (his eq. 4.19). Because the underlying vector field is
   divergence-free in the continuous sense, every fine control volume
   inherits $D_h^{\mathrm{f}}$-exactness to machine precision.

Properties of the construction, per the source: reduces to the plain
reconstruction when face cross-terms vanish; extends to any integer
refinement ratio (recursion for $2^k$, new formulas otherwise), to
orthogonal curvilinear geometries, and to triangular/tetrahedral meshes;
used to initialize newly refined patches, while ghost (halo) filling during
subcycling uses the reconstruction directly.

**Higher order and refinement ratio 3**
([Balsara (2009)](/sources/balsara-2009.md) §2). The fourth-order
[reconstruction](/methods/divergence-free-reconstruction.md) carries 10
face moments, one more than the 9 that a ratio-3 prolongation must fix
per face. Ratio 3 is therefore available, and recursion with the ratio-2
formulas reaches any ratio built from factors 2 and 3. The claim is made
in the source without an AMR demonstration.

## Structural remarks

* The construction is *integral*, not algebraic: exactness comes from
  prolonging an exactly solenoidal continuous field, not from tuning
  stencil coefficients — the reason it generalizes across ratios and
  geometries.
* It presumes **nested staggered control volumes**: fine face unions tile
  coarse faces. This is the property
  [Balsara (2001)](/sources/balsara-2001.md) claims zone-centered
  formulations lack
  ([CT–finite-volume equivalence, Contradictions](/results/ct-finite-volume-equivalence.md)).
* $P_D$ alone handles refinement; keeping the invariant through *time* on a
  subcycled hierarchy additionally needs the
  [electric-field correction](/methods/electric-field-correction.md) and
  area-weighted restriction $R$.
* **Production caveat — the premise fails mid-subcycle**: $P_D$'s
  exactness guarantee is conditional on divergence-free *input*, but ghost
  filling during subcycling interpolates the coarse field **in time**
  (first-order), producing data that is not divergence-free — at which
  point $P_D$-class schemes degrade to ordinary interpolation.
  [Miniati & Martin (2011)](/sources/miniati-martin-2011.md) accordingly
  found divergence-free ghost interpolation "neither practical nor
  necessary," reserving exactness machinery for the synchronization points
  where its premise actually holds.

## The coordinate-independent generalization

[Olivares et al. (2019)](/sources/olivares-2019.md) derive a general class
of divergence-preserving prolongation operators for face-allocated
variables valid in **arbitrary coordinates and stationary curved
spacetimes** — generalizing the Cartesian constructions below — with the
full AMR implementation (ghost exchange, coarse–fine and polar-axis
treatment) documented in the production GRMHD code BHAC.

## The Tóth–Roe construction

[Tóth & Roe (2002)](/sources/toth-roe-2002.md) give an independent
second-order construction in flux variables: limited linear interpolation
on the coarse faces, with the interior fine components determined by
requiring all eight fine-cell divergences to equal $\tfrac18$ of the coarse
divergence — plus variants that preserve the discrete *curl* as well. They
also supply the restriction half ($D_H R = R\, D_h$ by flux summation) and
prove the locality trichotomy across storage choices —
[locality limits](/results/transfer-operator-locality-limits.md): the pair
(local $P_D$, local $R$) exists only for face-staggered data.

# Citations

1. [Balsara (2001)](/sources/balsara-2001.md), §III–IV.
2. [Tóth & Roe (2002)](/sources/toth-roe-2002.md), §3.
3. [Miniati & Martin (2011)](/sources/miniati-martin-2011.md), §3.
4. [Etienne, Liu & Shapiro (2010)](/sources/etienne-2010.md) — the [vector-potential route](/methods/vector-potential-evolution.md) that dissolves the transfer problem instead of solving it.
5. [Olivares et al. (2019)](/sources/olivares-2019.md), §§3–4.
6. [Balsara (2009)](/sources/balsara-2009.md), §2 (observations 2–3).
