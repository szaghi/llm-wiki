---
type: Definition
title: "Finite element exterior calculus (FEEC)"
description: "Finite element spaces of differential forms organized into de Rham subcomplexes with bounded cochain projections; stability and correct convergence follow from the structure."
status: established
aliases: [FEEC]
tags: [feec, finite-elements, de-rham, cohomology, stability]
timestamp: 2026-07-08T00:00:00Z
---

# Finite element exterior calculus (FEEC)

The homological framework for compatible finite elements
([Arnold, Falk & Winther (2006)](/sources/arnold-falk-winther-2006.md)):
discretize with finite element spaces of *differential forms* — the two
families $\mathcal{P}_r\Lambda^k$ and $\mathcal{P}_r^-\Lambda^k$, of which
$\mathcal{P}_1^-\Lambda^k$ are the
[Whitney forms](/definitions/whitney-forms.md) — arranged into
finite-dimensional **subcomplexes of the de Rham complex** ($2^{n-1}$ per
degree in $n$ dimensions) that **reproduce the de Rham cohomology** on
domains of arbitrary Betti numbers, connected to the continuous complex by
**cochain projections**. Well-posedness of the discretization is inherited
from the structure rather than verified case by case; the Hodge Laplacian
$d\delta + \delta d$ unifies the applications (mixed Poisson, Maxwell,
div–curl systems, eigenvalue problems, elasticity via BGG).

## Why structure is not optional

The founding review's motivating failures are categorical, not
quantitative: equal-order continuous elements for the 1D mixed Poisson
problem are *unstable*, and standard energy minimization for the vector
Poisson problem **converges to the wrong solution on nonconvex polygons**
— the discrete spaces, failing to form a subcomplex with bounded
projections, miss part of the continuous solution space (the singular
cohomology-adjacent content). This is the FE-side sharpening of the theme
running through
[discrete exactness](/results/discrete-exactness-theorems.md): the complex
structure is what stands between a scheme and silently wrong limits.

Relation to the discrete-object frameworks (mimetic FD,
[DEC](/definitions/discrete-exterior-calculus.md), FIT): shared
motivation, coincidence at Whitney level — but FEEC elements are genuine
differential forms living in the solution space, carrying full
approximation theory (rates, adaptivity) that the formal frameworks lack.

## The master criterion (2009 form)

The abstract theory
([Arnold, Falk & Winther (2009)](/sources/arnold-falk-winther-2009.md))
distills stability to **two hypotheses on a closed Hilbert complex**: the
discrete spaces form a *subcomplex*, and a *bounded cochain projection*
onto it exists. These alone (plus minor consistency) give inherited
cohomology, harmonic-form isomorphism with error bounds, and stability of
the discrete Hodge Laplacian. In this bundle's language: the pairing of
placement (subcomplex) with a norm-bounded commuting transfer operator
(the projection) is what carries well-posedness across discretization —
the same two-part shape as $D_H R = R D_h$ and the SBP interface adjoint
condition, here elevated to the general theorem.

## Generalization: finite element systems

[Christiansen et al. (2011)](/sources/christiansen-2011.md) §5 extend the
framework to cellular complexes with **general polyhedral cells** and
non-polynomial shape functions: two local compatibility conditions
(face-restriction surjectivity, cellwise exactness) *imply* commuting
interpolators, and smoothing techniques upgrade them to $L^q$-stable
commuting projections — so the bounded-cochain-projection hypothesis is
constructible, not merely assumed, on general shape-regular meshes.

# Citations

1. [Arnold, Falk & Winther (2006)](/sources/arnold-falk-winther-2006.md), §1.
2. [Arnold, Falk & Winther (2009)](/sources/arnold-falk-winther-2009.md), §§1, 3.
3. [Christiansen et al. (2011)](/sources/christiansen-2011.md), §5.
