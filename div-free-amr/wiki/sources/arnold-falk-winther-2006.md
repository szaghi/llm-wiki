---
type: Source
title: "Arnold, Falk & Winther (2006) — Finite element exterior calculus, homological techniques, and applications"
description: "The FEEC founding review: two families of finite element differential forms arranged into de Rham subcomplexes reproducing cohomology, with stability tied to cochain projections."
resource: "doi:10.1017/S0962492906210018"
source_kind: paper
authors: [Arnold D.N., Falk R.S., Winther R.]
year: 2006
venue: "Acta Numerica 15:1-155"
local_file: "~/papers/mosaic/div-free-amr/2006-ActaNum-Arnold-FEEC-homological.pdf"
tags: [feec, finite-elements, de-rham, cohomology, stability, hodge-laplacian]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The founding review of **finite element exterior calculus**
([definition page](/definitions/finite-element-exterior-calculus.md)):
discretizations designed to be "compatible with the geometric, topological,
and algebraic structures which underlie well-posedness." Two families of
finite element differential forms, $\mathcal{P}_r\Lambda^k$ and
$\mathcal{P}_r^-\Lambda^k$ (the latter generated via the Koszul complex;
$\mathcal{P}_1^-\Lambda^k$ *are* the Whitney forms), organized into
$2^{n-1}$ de Rham subcomplexes per polynomial degree — all **reproducing
the de Rham cohomology on domains of arbitrary Betti numbers**. Unified
treatment of the Hodge Laplacian, Maxwell, eigenvalue problems,
preconditioning, and the four-decades-open stable-elasticity-element
problem (resolved via weakly imposed symmetry and the BGG resolution).

**Coverage of this ingestion (scoped):** §1 (introduction, pp. 1–9) read
in full together with the structural claims it states for Parts 1–2;
technical sections (§§2–11) *not* read — flagged for follow-up passes;
claims below are compiled only at the level the introduction asserts them.

# Key claims

1. **Structure or wrong answers**: two canonical failures motivate the
   framework — continuous piecewise-linears for *both* variables of the 1D
   mixed Poisson problem are unstable; and energy minimization for the
   vector Poisson problem over standard piecewise-polynomial subspaces
   "will inevitably converge to the **wrong solution** on some domains,
   e.g., nonconvex polygons" — structure-blind discretization fails not by
   inaccuracy but by convergence to the wrong limit.
2. **Stability ↔ cochain projections**: "the strong connection between
   numerical stability and cochain projections of elliptic complexes,"
   emphasized since Arnold's 2002 ICM address — developed into the master
   criterion in the 2009 sequel.
3. **Beyond Whitney**: FEEC is "much more than the Whitney forms" — the
   full two-family hierarchy with unified bases and degrees of freedom;
   the two families are shown by representation theory to be essentially
   the only affinely invariant choices.
4. **Relation to the discrete-object frameworks**: mimetic FD, covolume,
   and [DEC](/definitions/discrete-exterior-calculus.md) share motivation,
   and coincide with the Whitney complex in simple cases — but FEEC
   realizes its elements as *true differential forms in the solution
   space* (so exact-vs-discrete comparison is natural), which the authors
   argue is "highly desirable" over objects that mimic forms.

# Notation map

| AFW | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal{P}_r\Lambda^k, \mathcal{P}_r^-\Lambda^k$ | — | FE form families; named inline |
| $\mathcal{P}_1^-\Lambda^k$ | [Whitney forms](/definitions/whitney-forms.md) | isomorphic to simplicial cochains |
| $d$, $\delta$, $d\delta + \delta d$ | exterior derivative, adjoint, Hodge Laplacian | |
| de Rham subcomplex | discrete complex $V_h^0 \to \dots \to V_h^3$ | cohomology-reproducing |

# Pages created or updated

* Created [Finite element exterior calculus (FEEC)](/definitions/finite-element-exterior-calculus.md).
* Updated [Whitney forms](/definitions/whitney-forms.md) (position inside the two FEEC families).

# Citations

1. `~/papers/mosaic/div-free-amr/2006-ActaNum-Arnold-FEEC-homological.pdf` (doi:10.1017/S0962492906210018) — scoped read: §1 in full; §§2–11 not read in this pass.
