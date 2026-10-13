---
type: Method
title: "Mimetic spectral elements"
description: "Arbitrary-order tensor-product elements whose reduction-reconstruction projection commutes with the exterior derivative, discretizing grad/curl/div exactly on curvilinear meshes."
status: established
aliases: [MMSEM, mimetic spectral element method]
tags: [mimetic, spectral-elements, high-order, divergence-constraint, curvilinear]
timestamp: 2026-10-13T00:00:00Z
---

# Mimetic spectral elements

Arbitrary-order compatible elements on curvilinear quadrilaterals and
hexahedra ([Kreeft & Gerritsma (2013)](/sources/kreeft-gerritsma-2013.md)):
degrees of freedom are integrals over $k$-cells (the cochain data of the
complex, [notation](/notation.md)), reconstructed by tensor products of
nodal and *edge* (histopolation) interpolation functions of arbitrary
degree, with the projection $\pi = \mathcal{I}\circ\mathcal{R}$ satisfying
$$\pi \circ \mathrm d = \mathrm d \circ \pi .$$
The commutation is the whole method: differentiation is performed exactly
in the finite-dimensional space, so for incompressible flow the discrete
velocity is **pointwise divergence-free at every mesh size** — not
converging to solenoidal, *being* solenoidal — while retaining optimal
spectral convergence and LBB stability.

## Position in this bundle

This is the corpus's constructive existence proof that **high order and
the exact algebraic invariant coexist** — realized in the FE/spectral
family on conforming curvilinear meshes. Read against the bundle's central
question, each qualifier is load-bearing: the DOFs are facet-integral
(not collocated point values), the machinery is variational (not
finite-difference stencils), and the meshes are conforming (no 2:1
interfaces treated). It is the higher-order sibling of
[Whitney forms](/definitions/whitney-forms.md) with the commuting
projection of [FEEC](/definitions/finite-element-exterior-calculus.md)
realized concretely — and the natural benchmark any high-order FD
construction with exactness claims must be measured against.

The framework behind the method
([Palha et al. (2014)](/sources/palha-2014.md)): quantities split into
forms and pseudo-forms by orientation, the Hodge-$\star$ is the sole
metric crossing, and two equivalent architectures result — a dual-grid
description resembling staggered finite volumes and a single-grid
description resembling finite elements, proved to deliver equivalent
solutions on the volume-form Poisson problem. The design principle in
their words: the discrete system behaves like the continuous one exactly
when the operators **commute with the projection**.

# Citations

1. [Kreeft & Gerritsma (2013)](/sources/kreeft-gerritsma-2013.md), §§3–5.
2. [Palha et al. (2014)](/sources/palha-2014.md), §§1–6.
