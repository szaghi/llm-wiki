---
type: Source
title: "Christiansen, Munthe-Kaas & Owren (2011) — Topics in structure-preserving discretization"
description: "Acta Numerica review; its finite-element-systems part generalizes FEEC to polyhedral cellular complexes, with compatibility conditions yielding commuting interpolators and smoothed stable projections."
resource: "doi:10.1017/S096249291100002X"
source_kind: paper
authors: [Christiansen S.H., Munthe-Kaas H.Z., Owren B.]
year: 2011
venue: "Acta Numerica 20:1-119"
local_file: "~/papers/mosaic/div-free-amr/2011-ActaNum-Christiansen-101017S096249291100002X.pdf"
tags: [feec, finite-element-systems, polyhedral, cochain-projection, structure-preserving]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Broad structure-preservation review; the part compiled here is **§5,
finite element systems (FES)** — Christiansen's generalization of
[FEEC](/definitions/finite-element-exterior-calculus.md) to **cellular
complexes with general (polyhedral) cells and possibly non-polynomial
shape functions**. Two local *compatibility* conditions — surjectivity
under restriction to faces, and sequence exactness under $d$ on each cell
— **imply** the existence of interpolation operators commuting with the
exterior derivative; degrees of freedom are *deduced*, not postulated.
Combining interpolators with smoothing yields commuting projections
uniformly stable in $L^q$, delivering eigenpair approximation for the
mixed Hodge Laplacian plus discrete Sobolev injections and translation
estimates.

**Coverage of this ingestion (scoped):** abstract + §5 (pp. 65–108) at
claim level; §§2–4 (Lie-group integrators, first-integral preservation,
group-theoretic algorithms — temporal structure preservation) *not
compiled*: outside this bundle's domain.

# Key claims

1. **Compatibility ⟹ commuting interpolators**: locality does the work —
   cellwise surjectivity + exactness produce the commuting-diagram
   property and, via algebraic topology, the global cohomology; DOFs
   become comparable choices rather than definitional commitments.
2. **The bounded projection is constructible**: the smoothing lineage
   (Schöberl's grid-perturbation averaging; convolution on macro-elements;
   Christiansen–Winther space-dependent smoothing for general
   shape-regular meshes, with commuting extension operators) upgrades
   interpolators to $L^q$-stable commuting projections — making the second
   FEEC hypothesis (bounded cochain projection) a *construction*, not an
   assumption, including on general meshes.
3. **Trimmed families recovered and repositioned**: the Koszul-trimmed
   $\Lambda_p^k$ system reproduces Whitney ($p=1$), Nédélec, and
   Hiptmair's arbitrary-order forms, with $p$-indexing chosen so the wedge
   product maps between orders.
4. **The FE method's differentia** (vs mimetic FD, covolume, FV): "its
   emphasis on defining fields inside cells … in such a way that the main
   discrete differential operators … are obtained simply by restriction of
   the continuous ones."

# Notation map

| Christiansen et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| FE system $A^k(T)$ over cellular complex | generalized $V_h^k$ on polyhedral cells | non-polynomial admitted |
| $\kappa$ (Koszul operator) | — | trimming; named inline |
| smoothed commuting projections | bounded cochain projections | FEEC hypothesis (ii), constructed |

# Pages created or updated

* Updated [FEEC](/definitions/finite-element-exterior-calculus.md) (FES generalization; projections constructible on polyhedral meshes).

# Citations

1. `~/papers/mosaic/div-free-amr/2011-ActaNum-Christiansen-101017S096249291100002X.pdf` (doi:10.1017/S096249291100002X) — scoped read: §5 at claim level; §§2–4 not compiled.
