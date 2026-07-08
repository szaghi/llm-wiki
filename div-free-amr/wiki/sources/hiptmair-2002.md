---
type: Source
title: "Hiptmair (2002) — Finite elements in computational electromagnetism"
description: "Acta Numerica review founding FE electromagnetics on discrete differential forms: Whitney elements, commuting-diagram interpolation, and the discrete de Rham theorem with cohomology."
resource: "doi:10.1017/S0962492902000041"
source_kind: paper
authors: [Hiptmair R.]
year: 2002
venue: "Acta Numerica 11:237-339"
local_file: "~/papers/mosaic/div-free-amr/2002-ActaNum-Hiptmair-101017S0962492902000041.pdf"
tags: [finite-elements, differential-forms, whitney-forms, de-rham, electromagnetics, edge-elements]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

104-page review founding finite-element electromagnetics on **discrete
differential forms**: Maxwell's equations are stated coordinate-free in the
calculus of forms; the *topological* laws live on cochains (incidence
matrices $\mathsf{D}^l$, purely combinatorial, $\mathsf{D}^{l+1}\mathsf{D}^l = 0$);
the *metric* material laws force extension of cochains into cell interiors
via **Whitney maps**, producing the Whitney-form finite elements (nodal /
edge / face / volume elements as discrete 0/1/2/3-forms,
[definition page](/definitions/whitney-forms.md)). Convergence theory is
developed by adapting Lagrangian-FE techniques; schemes *outside* this
framework are shown to be haunted by spurious solutions.

**Coverage of this ingestion (scoped):** §§1–3 read in full (introduction;
Maxwell in forms; discrete differential forms, pp. 237–291). §§4–6 (Maxwell
eigenvalue/source problems, regularized formulations) *not read* — flagged
for a follow-up pass; claims from those sections are not compiled.

# Key claims

1. **Topology/metric split**: the incidence matrices $\mathsf{D}^l$ depend
   only on mesh topology and satisfy $\mathsf{D}^{l+1}\mathsf{D}^l = 0$
   plus a cochain de Rham theorem (Theorem 3.1): the kernel of
   $\mathsf{D}^l$ is the image of $\mathsf{D}^{l-1}$ *plus* a discrete
   cohomology space of dimension equal to the $l$th Betti number of the
   domain — the FE mirror of the mimetic factorization, with the
   multiply-connected case handled explicitly.
2. **Whitney maps, four axioms** (§3.2): extension of cochains
   ($I_l \circ \mathsf{W}^l = \mathrm{Id}$), the commuting diagram
   $d \circ \mathsf{W}^l = \mathsf{W}^{l+1} \circ \mathsf{D}^l$, strict
   locality, and piecewise-polynomial vector proxies. Barycentric formula
   for all degrees on simplices; tensor-product versions on bricks; affine
   equivalence and parametric (curved-cell) versions by pullback.
3. **Commuting-diagram property for interpolation** (eq. 3.12):
   $d \circ \Pi^l = \Pi^{l+1} \circ d$ — nodal interpolation commutes with
   exterior derivative; the de Rham theorem transfers verbatim to Whitney
   forms (Corollary 3.3).
4. **Discrete potentials are computationally available** — and this is
   exceptional: for curl-free *Lagrangian* (componentwise piecewise-linear)
   vector fields, the potential would be a $C^1$ piecewise-quadratic object
   with no localized basis, computationally unusable. Whitney forms are the
   arrangement in which discrete potentials stay in a finite element space.
5. **Higher order**: the exact-sequence property is posed as a necessary
   design condition for higher-order discrete forms —
   $\{u \in W_p^l : du = 0\} = dW_p^{l-1}$ — anticipating the
   arbitrary-order families.

# Notation map

| Hiptmair | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| cochain spaces $C^l(\Omega_h)$ | $V_h^0, V_h^1, V_h^2, V_h^3$ | DOFs = integrals over $l$-facets |
| $\mathsf{D}^l$ (incidence matrices) | combinatorial part of $G_h, C_h, D_h$ | topology only; metric enters via mass matrices |
| $d$ (exterior derivative) | continuous $\mathrm{grad}/\mathrm{curl}/\mathrm{div}$ by degree | |
| $\mathsf{W}^l$ (Whitney map), $\Pi^l$ | — | extension/interpolation; commuting-diagram operators |
| $d\circ\Pi^l = \Pi^{l+1}\circ d$ | the commutation discipline behind $P_D$-type operators | interpolation commutes with the constraint operator |

# Pages created or updated

* Created [Whitney forms (discrete differential forms)](/definitions/whitney-forms.md).
* Updated [Discrete exactness theorems](/results/discrete-exactness-theorems.md) (FE counterpart; cohomology-aware statement).

# Citations

1. `~/papers/mosaic/div-free-amr/2002-ActaNum-Hiptmair-101017S0962492902000041.pdf` (doi:10.1017/S0962492902000041) — text extraction, §§1–3 (pp. 237–291); §§4–6 not read in this pass.
