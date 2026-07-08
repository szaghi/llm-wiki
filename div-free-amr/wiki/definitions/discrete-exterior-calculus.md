---
type: Definition
title: "Discrete exterior calculus (DEC)"
description: "Calculus built directly on simplicial complexes: forms as cochains, exterior derivative as coboundary, diagonal Hodge star from circumcentric primal-dual volume ratios."
status: established
aliases: [DEC]
tags: [dec, differential-forms, simplicial, dual-grid, hodge]
timestamp: 2026-07-08T00:00:00Z
---

# Discrete exterior calculus (DEC)

An *ab initio* calculus on simplicial complexes
([Desbrun, Hirani, Leok & Marsden (2005)](/sources/desbrun-hirani-2005.md)):
discrete $k$-forms are cochains (values on $k$-simplices), the exterior
derivative is the coboundary — so the generalized Stokes theorem
$\langle d\alpha, c\rangle = \langle\alpha, \partial c\rangle$ and
$dd = 0$ hold **by definition** — and the metric enters through a
**diagonal Hodge star** built from the volume ratios of primal simplices
and their **circumcentric (Voronoi) dual** cells. From $d$ and $*$ the
rest follows: codifferential $\delta$, Laplace–deRham
$\Delta = d\delta + \delta d$, and — DEC's distinctive extension —
discrete *vector fields* with flat/sharp, contraction, and Lie
derivatives, which is what forces circumcentric rather than barycentric
duals.

## Position among the placement frameworks

DEC is the simplicial member of the family this bundle keeps meeting: the
[staggered grid](/definitions/staggered-grid.md) (FD/FV — named by the DEC
authors as where primal–dual pairs "arise most often"),
[Whitney forms](/definitions/whitney-forms.md) (FE),
[FIT](/methods/finite-integration-technique.md) (EM integral form), and
the [mimetic natural operators](/definitions/support-operator-method.md)
(logically rectangular FD). All five put degree-$k$ data on
$k$-dimensional mesh objects and split topology (exact, combinatorial)
from metric (the Hodge/mass/material matrices). DEC's trade: structural
identities and a discrete Poincaré lemma hold exactly on unstructured
simplicial meshes of any dimension
([discrete exactness theorems](/results/discrete-exactness-theorems.md)),
but the theory is *formal* — convergence to the smooth counterparts is,
by the authors' own statement, mostly not proved.

The lineage runs to production: DEC-family operators, rebuilt VEM-style
with mimetic stabilization for arbitrary (even non-planar) polygons, are
the numerical layer of modern geometry-processing pipelines
([de Goes, Butts & Desbrun (2020)](/sources/degoes-2020.md)).

# Citations

Two thesis-level points sharpen the picture
([Hirani (2003)](/sources/hirani-2003.md)): DEC is built **discrete-first**
— the mesh is "the only given thing," objects but never the mesh are
interpolated, as opposed to truncating smooth operators on an approximated
manifold — and the primal/dual pairing makes operators *proliferate*
(primal–primal, primal–dual, …): one continuous operator corresponds to a
discrete family, and choosing among them is scheme design.

# Citations

Pointwise values require leaving pure cochain calculus: the DEC school's
own reconstruction operator is the **Whitney bridge** — Whitney $k$-forms
interpolating cochains into fields
([Desbrun, Kanso & Tong (2008)](/sources/desbrun-kanso-tong-2008.md)) —
making DEC-plus-Whitney and FEEC two descriptions of one junction. The
machinery is now standard curriculum
([Crane (2025)](/sources/crane-2025.md)), whose running *no-free-lunch
principle* — every discrete definition preserves a different subset of
continuous properties, and none preserves all — is the pedagogical form of
the operator-proliferation fact above.

# Citations

1. [Desbrun, Hirani, Leok & Marsden (2005)](/sources/desbrun-hirani-2005.md), §§3–9, 11.
2. [de Goes, Butts & Desbrun (2020)](/sources/degoes-2020.md).
3. [Hirani (2003)](/sources/hirani-2003.md), abstract.
4. [Desbrun, Kanso & Tong (2008)](/sources/desbrun-kanso-tong-2008.md), §6.
5. [Crane (2025)](/sources/crane-2025.md).
