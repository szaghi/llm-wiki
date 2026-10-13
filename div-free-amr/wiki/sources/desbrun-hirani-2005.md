---
type: Source
title: "Desbrun, Hirani, Leok & Marsden (2005) — Discrete exterior calculus"
description: "Ab initio calculus on simplicial complexes: discrete forms and vector fields with d, Hodge star, codifferential, wedge, Lie derivative on circumcentric primal-dual meshes; Stokes true by definition."
resource: "arXiv:math/0508341"
source_kind: paper
authors: [Desbrun M., Hirani A.N., Leok M., Marsden J.E.]
year: 2005
venue: "arXiv:math/0508341v2 [math.DG]"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2005-arXiv-Desbrun-1048550arXivmath0508341.pdf"
tags: [dec, differential-forms, simplicial, dual-grid, hodge, discrete-vector-analysis]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The canonical reference for **discrete exterior calculus (DEC)**
([definition page](/definitions/discrete-exterior-calculus.md)): a
self-contained calculus on simplicial complexes of arbitrary finite
dimension, covering not only discrete differential forms (cochains) but
**discrete vector fields** and the operators connecting them — exterior
derivative $d$, Hodge star $*$, codifferential $\delta$, wedge, flat/sharp,
contraction, Lie derivative, divergence, Laplace–deRham. The distinctive
technical commitment is the **circumcentric (Voronoi) dual** complex —
barycentric duals, standard in the EM-forms community, are argued
insufficient once vector fields enter the theory.

# Key claims

1. **Forms are cochains; Stokes is true by definition**:
   $\langle d\alpha, c\rangle = \langle \alpha, \partial c\rangle$ — $d$
   is the coboundary operator, so $d_{k+1} d_k = 0$ follows immediately;
   dual forms live on the dual complex with a carefully defined dual
   boundary.
2. **Diagonal Hodge from volume ratios**: primal $k$-simplices pair
   one-to-one with dual $(n{-}k)$-cells sharing the same support volume;
   the discrete Hodge star scales by the corresponding volume ratio —
   giving e.g. $\operatorname{div}(X) = -\delta X^\flat = *d*X^\flat$
   evaluated as a sum of dual-edge fluxes over $|{\star}\sigma^0|$: the
   finite-volume divergence, rederived from the calculus.
3. **Discrete Poincaré lemma** proved via an explicit homotopy operator on
   simplicial meshes — the DEC form of the exactness converses
   ([discrete exactness theorems](/results/discrete-exactness-theorems.md)).
4. **Staggered meshes named as the ancestor**: "the use of primal and dual
   meshes arises most often as staggered meshes in finite volume and
   finite difference methods" — cell-centered densities as duals of
   0-cells, face fluxes as 2-cells or their normal 1-cells.
5. **Formality caveat, the authors' own**: definitions are chosen to make
   the key theorems hold exactly; "for the most part, we do not prove that
   these definitions converge to the smooth counterparts" — DEC here is a
   structurally exact but not convergence-proved theory (checked to match
   variationally derived operators where available).

# Notation map

| DEC | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| cochains $\Omega_d^k(K)$ | $V_h^k$ | simplicial rather than cubical |
| $d$ (coboundary) | combinatorial $G_h, C_h, D_h$ by degree | $dd = 0$ |
| $*$ (volume-ratio Hodge) | diagonal metric operator | circumcentric duals make it diagonal |
| $\delta = \pm * d\, *$, $\Delta = d\delta + \delta d$ | codifferential, Laplace–deRham | |
| $\flat, \sharp$ | — | vector-field/1-form bridges; DEC-specific |
| $\star\sigma^k$ (circumcentric dual) | dual complex | Voronoi, not barycentric |

# Pages created or updated

* Created [Discrete exterior calculus (DEC)](/definitions/discrete-exterior-calculus.md).
* Updated [Discrete exactness theorems](/results/discrete-exactness-theorems.md) (simplicial/DEC counterpart via homotopy operator).

# Citations

1. `~/papers/mosaic/div-free-amr/2005-arXiv-Desbrun-1048550arXivmath0508341.pdf` (arXiv:math/0508341) — text extraction, 53 pp.
