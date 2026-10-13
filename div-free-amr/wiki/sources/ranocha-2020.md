---
type: Source
title: "Ranocha, Ostaszewski & Heinisch (2020) — Discrete vector calculus and Helmholtz Hodge decomposition for classical FD SBP operators"
description: "For collocated tensor-product SBP operators, div curl = 0 and curl grad = 0 hold exactly, but the potential-existence converses and the Helmholtz-Hodge decomposition fail by explicitly characterised grid-oscillation modes, removable by an orthogonal filter."
resource: "doi:10.1007/s42967-019-00057-2"
source_kind: paper
authors: [Ranocha H., Ostaszewski K., Heinisch P.]
year: 2020
venue: "Commun. Appl. Math. Comput. 2(4):581-611 (arXiv:1908.08732)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2020-CAMC-Ranocha-101007s42967-019-00057-2.pdf"
tags: [sbp, collocation, discrete-vector-analysis, exactness, hodge-decomposition, grid-oscillations, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper studies discrete vector calculus for the most common SBP
operators: collocated, nodal, diagonal-norm, tensor-product finite
differences. The same results apply to Lobatto–Legendre spectral
collocation. The result is negative but exact.
* **The identities hold.** The composition identities hold everywhere,
  boundaries included, because the 1D derivatives commute.
* **The converses fail.** Potential-existence theorems fail, and so does
  the Helmholtz–Hodge decomposition.
* **The failure is a finite, explicit set of grid-oscillation modes**, the
  kernel of the $\mathsf{H}$-adjoint of the 1D derivative.

This is the collocated counterpart of the staggered and FE
[exactness theorems](/results/discrete-exactness-theorems.md), and the
characterisation that the [Zaghi (2026)](/sources/zaghi-2026.md) record
draws on (cited there as "Ranocha 2019").

The file read is the arXiv v2 preprint. Venue, volume and pages were
verified on Crossref.

# Key claims

1. **Commutation** (Remark 2.8). For tensor-product SBP operators,
   $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$ and $C_h^{\mathrm{c}} G_h = 0$
   ([notation](/notation.md)), since $D_jD_i = D_iD_j$.
2. **Grid oscillations** (Lemma 3.3, Definition 3.4, Examples 3.5–3.6).
   * Take a nullspace-consistent derivative ($\ker\mathsf{D}_1 = \mathrm{span}\{1\}$).
     Then $\dim\ker\mathsf{D}_1^* = 1$. The spanning mode alternates
     $\pm1$ in the interior, with boundary values set by the closure.
   * For Lobatto–Legendre collocation it is the highest Legendre mode on
     the grid.
   * Tensor products give multi-direction modes.
3. **The kernels exceed the images** (Theorems 3.7–3.8, 3.18–3.19). In 3D,
   $\dim\ker C_h^{\mathrm{c}} = \dim\operatorname{im}G_h + 3$ and
   $\dim\ker D_h^{\mathrm{c}} = \dim\operatorname{im}C_h^{\mathrm{c}} + 3$.
   The complements are spanned explicitly:
   * single-direction modes for curl;
   * two-direction modes placed in the remaining component for div.
   
   In 2D the excess is 2 in each case. The kernels equal the images on the
   subspace orthogonal to the grid oscillations.
4. **Filter** (eq. 55, Theorem 3.20). Removing the single-direction
   oscillations is an $\mathsf{H}$-orthogonal projection of norm at most 1.
   The integral-based potential constructions are ill-conditioned and can
   be dominated by roundoff.
5. **Fields that are both divergence-free and curl-free** (Theorem 4.2) are
   exactly discrete gradients of discretely harmonic functions, as in the
   continuum. A discrete Neumann problem recovers the potential.
6. **Helmholtz–Hodge fails** (Theorems 5.1, 5.6).
   * Grid functions carrying the all-direction mode lie outside
     $\operatorname{im}G_h + \operatorname{im}C_h^{\mathrm{c}}$, so a
     remainder $r$ is unavoidable.
   * A divergence-free vector potential cannot always be chosen.
   * Boundary conditions and the divergence of the potential cannot both
     be prescribed.
7. **Numerics** (§6). Least-norm least-squares projections (LSQR, LSMR in
   $\mathsf{H}$-scaled form) give potentials converging at the order
   expected for first-order PDEs, and the remainder vanishes under
   refinement.
   * On MHD wave modes (Alfvén and fast), the decomposition separates the
     current components.
   * Projection order must follow the amplitude ordering, boundary effects
     need several wavelengths in the domain, and large amplitude ratios
     need resolution.

# Notation map

| Ranocha et al. (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M$ (mass/norm matrix) | $\mathsf{H}$ | |
| $D$, $D_i$ | $\mathsf{D}_1$, per direction | |
| $D^* = M^{-1}D^TM$ | $\mathsf{D}_1^*$ | registry extended in this ingestion |
| $\mathrm{osc}$, $\mathrm{osc}_{ij}$, $\mathrm{osc}_{123}$ | grid-oscillation modes | prose; spanning $\ker\mathsf{D}_1^*$ and its tensor products |
| $\operatorname{grad}$, $\operatorname{curl}$, $\operatorname{div}$, $\operatorname{rot}$ | $G_h$, $C_h^{\mathrm{c}}$, $D_h^{\mathrm{c}}$ | collocated; rot is the 2D scalar-to-vector curl |
| $F$ (eq. 55) | grid-oscillation filter | |

# Pages created or updated

* Updated [Discrete exactness theorems](/results/discrete-exactness-theorems.md): the collocated SBP failure, with a revised description.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): the identity holds through the boundary closures, but the kernel exceeds the image.
* Updated [Vector-potential evolution](/methods/vector-potential-evolution.md): the exactness converse is a staggered-complex property.
* Updated [Divergence source at collocated 2:1 seams](/results/collocated-seam-divergence-source.md): the characterisation of the grid-oscillation modes the record invokes.
* Updated [Summation by parts](/definitions/summation-by-parts.md): nullspace consistency and grid oscillations.
* Updated [Notation registry](/notation.md): $\mathsf{D}_1^*$.

# Citations

1. `~/papers/mosaic/div-free-amr/2020-CAMC-Ranocha-101007s42967-019-00057-2.pdf` (doi:10.1007/s42967-019-00057-2): text extraction, all pages including the reference list (60 entries).
