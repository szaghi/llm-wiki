---
type: Source
title: "Wu & Shu (2019) — Provably positive high-order schemes for ideal MHD: analysis on general meshes"
description: "Extends the MHD positivity analysis to HLL-type fluxes on polytopal meshes in any dimension: generalized discrete divergence, explicit PP wave speeds, upwind penalty discretization of the Godunov-Powell source, and a proof that smooth solutions of the symmetrizable system stay positive for any div B."
resource: "doi:10.1007/s00211-019-01042-w"
source_kind: paper
authors: [Wu K., Shu C.-W.]
year: 2019
venue: "Numer. Math. 142(4):995-1047 (arXiv:1807.11467)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2019-NumerMath-Wu-101007s00211-019-01042-w.pdf"
tags: [positivity, dg, finite-volume, eight-wave, locally-divergence-free, hll, unstructured, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

This is the third paper of the Wu / Wu–Shu positivity series, after
[Wu (2018)](/sources/wu-2018.md) and
[Wu & Shu (2018)](/sources/wu-shu-2018.md). Those two were restricted to
the global LF flux on uniform Cartesian meshes. This paper redoes the
analysis for **HLL-type fluxes on arbitrary polytopal meshes in any
dimension**. LF is the special case of symmetric wave speeds. The paper
also turns the PDE-level motive of the previous paper into a theorem on
the symmetrizable side. All of this is merged into the
[positivity–divergence coupling](/results/positivity-divergence-coupling.md).

The file read is the arXiv v1 preprint. Volume, issue and pages were
verified on Crossref.

# Key claims

1. **General-mesh key inequality** (Theorem 2.1, Corollaries 2.1–2.2).
   * The two-state inequality of Wu (2018) generalizes to $N$ states with
     arbitrary unit normals.
   * Its extra term is a discrete divergence $\sum_j s_j\langle\xi^{(j)}, B^{(j)}\rangle$.
     The inequality is false without it (Remark 2.2).
2. **HLL wave speeds that guarantee positivity** (Theorem 2.2, Remarks
   2.4–2.5).
   * Under explicit bounds $\sigma_r \ge \alpha_r$ and $\sigma_l \le \alpha_l$,
     the HLL intermediate state is admissible up to a term in the jump of
     $B_n$. It is fully admissible when $B_n$ is continuous.
   * The standard Davis and Einfeldt speeds are not guaranteed to work.
     The recommended speeds take the min/max of both.
3. **1D** (Theorems 3.1–3.2). Standard FV and DG schemes with this HLL flux
   are positivity-preserving under a limiter-accessible condition.
4. **Conservative schemes on general meshes** (eq. 4.9, Corollary 4.1,
   Theorem 4.3).
   * The DDF condition generalizes to a wave-speed-weighted face
     divergence. Under it the conservative scheme is positivity-preserving.
   * Only the Cartesian global-LF scheme is known to preserve it. On
     general meshes it does not, so the scheme is not
     positivity-preserving in general.
5. **The symmetrizable scheme** (Theorems 4.1–4.2, Remarks 4.1, 4.3).
   * The source term is discretized as a penalty
     $-\Delta t\,\mathrm{div}_K\bar B\,S(\bar U)$, *upwinded* with the
     local HLL speeds. For LF it reduces to the Cartesian divergence of
     the earlier papers.
   * Together with locally divergence-free DG elements this gives provable
     positivity with no DDF condition.
   * Remark 4.3 splits the discrete divergence into a cell-interior part
     and a face-jump part. The basis zeroes the first, and the penalty
     supplies exactly the second, which a standard DG scheme lacks.
6. **PDE-level theorem** (Proposition A.1). Any $C^1$ solution of the
   symmetrizable system with positive initial density and pressure stays
   positive for any $\nabla\cdot B$. Along particle paths
   $D_t\rho = -\rho\nabla\cdot v$ and $D_t p = -\gamma p\nabla\cdot v$. The
   same holds for Janhunen's modified system (Remark A.1). The authors
   *hope* it extends to weak entropy solutions; that is not proved.
7. **Numerics** (§5, third-order DG, 1D and 2D rectangles only).
   * The HLL flux resolves features better than the global LF flux of the
     earlier papers.
   * Dropping the penalty term breaks the shock–cloud run at
     $t \approx 0.014$, which is the ablation evidence for item 5.
   * Turning off the positivity limiter leads to failure on extreme
     problems.
   * Triangular-mesh implementations are announced, not shown.

# Notation map

| Wu & Shu (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $G$, $G^*$ | $\mathcal{G}$ | |
| $\mathrm{div}_K\bar B$ (eq. 4.2) | wave-speed-weighted face divergence | reduces to $D_h^{\mathrm{c}}\bar B_h$ for Cartesian LF |
| $\sigma^\pm_{K,j}$, $\sigma_l$, $\sigma_r$ | HLL wave speeds | no registry symbol |
| $S(U)$ | eight-wave source vector | |
| $\alpha^{\mathrm{LF}}$ | $\alpha^{\mathrm{LF}}$ | LF as the symmetric HLL case |
| $\xi^{(j)}_K$, $E_K^j$ | face normals and faces of a polytopal cell | |

# Pages created or updated

* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): general meshes and HLL, the Cartesian-only preservation of the DDF condition, the PDE-level theorem, the scope, and a compiler reading on 2:1 seams.
* Updated [Eight-wave formulation](/methods/eight-wave.md): PDE-level positivity of the symmetrizable system.

# Citations

1. `~/papers/mosaic/div-free-amr/2019-NumerMath-Wu-101007s00211-019-01042-w.pdf` (doi:10.1007/s00211-019-01042-w): text extraction. Theorem statements, remarks, §§1, 4.1, 5, 6 and Appendix A were read in full. The technical proofs of §2 and §4.2 were read in outline only, and no equation from them is reproduced. The reference list has 66 entries.
