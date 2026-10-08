---
type: Source
title: "Wu & Shu (2018) — A provably positive discontinuous Galerkin method for multidimensional ideal MHD"
description: "Provably positivity-preserving high-order DG for multidimensional MHD via the symmetrizable (Godunov-Powell) form: locally divergence-free basis plus penalty terms from the source term remove the need for a discrete divergence-free condition, at the price of exact conservation."
resource: "doi:10.1137/18M1168042"
source_kind: paper
authors: [Wu K., Shu C.-W.]
year: 2018
venue: "SIAM J. Sci. Comput. 40(5):B1302-B1329 (arXiv:1807.00246)"
local_file: "~/papers/mosaic/div-free-amr/2018-SISC-Wu-10113718m1168042.pdf"
tags: [positivity, dg, eight-wave, locally-divergence-free, admissibility, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

This is the companion of [Wu (2018)](/sources/wu-2018.md). That paper
showed that conservative LF-type schemes need a discrete divergence-free
(DDF) condition to be provably positive, and that a locally
divergence-free basis cannot supply it. Here the authors change the PDE.
They discretize Godunov's symmetrizable form, the
[eight-wave](/methods/eight-wave.md) system with source
$-(\nabla\cdot B)\,S(U)$, and prove positivity *without* any DDF
condition. The result is the non-conservative branch of the
[positivity–divergence coupling](/results/positivity-divergence-coupling.md).

The file read is the arXiv v1 preprint, titled "Provably positive
discontinuous Galerkin methods …". The published title, volume and pages
were verified on Crossref.

# Key claims

1. **The admissible-set machinery** (§2, Lemmas 2.2–2.5) is that of Wu
   (2018). The key inequality's extra term, in
   $(B_i - \tilde B_i)(v^*\cdot B^*)$, is here absorbed by the discretized
   source term instead of being cancelled by a DDF condition (Remark 2.6).
2. **First order** (Theorem 3.1, Remarks 3.2–3.3).
   * The LF scheme plus the penalty
     $-\Delta t\,(D_h^{\mathrm{c}}\bar B_h)\,S(\bar U)$, with the same
     central divergence as Wu (2018) eq. 45, is positivity-preserving.
   * The CFL-type condition carries an extra term $\vartheta$, a bound on
     $|B|/\sqrt\rho$.
   * The required viscosity is at most twice the standard one, and equal to
     it up to $O(h)$ on smooth problems.
   * Without the penalty the scheme reverts to the conservative LF scheme,
     which is not positivity-preserving in general.
3. **High order** (§3.2, Theorem 3.4).
   * $P^K$ DG in the *locally* divergence-free space of Li & Shu.
   * Face terms add $\tfrac12[\![B_n]\!]\,S(U^\mp)$ at each side, a
     discretization of the source term from the jump in the normal field.
   * The Cheng et al. scaling limiter enforces admissibility at
     Gauss–Lobatto points. Time stepping is SSP-RK.
   * Positivity holds under $\Delta t\sum_\ell\alpha_\ell^{\mathrm{LF}}/\Delta x_\ell \le \theta\,\hat\omega_1$,
     with $\theta = 1/(1+\max_\ell \vartheta_\ell/\alpha_\ell^{\mathrm{LF}})$.
   * Remark 3.7 gives a version for FV schemes that reconstruct only
     interface values.
4. **The two features divide the work** (Remark 3.6). The local basis
   makes the divergence zero inside each cell. The penalty controls the
   divergence error across faces.
5. **PDE-level motive** (Appendix A, marked by the authors as evidence, not
   proof). For smooth 3D data with a small $\nabla\cdot B \ne 0$, the
   initial pressure derivative of the *conservative* system can drive the
   pressure negative. The symmetrizable form appears to avoid this. This
   matches Janhunen's 1D observation for jumps in $B_n$.
6. **Numerics** (§4, third-order DG, CFL 0.15).
   * Design order on smooth problems, including a vortex with extremely
     low pressure.
   * Shock–cloud, rotated shock tube, blasts and jets at very low $\beta$:
     without the positivity limiter the DG code breaks down on the
     shock–cloud ($t \approx 0.0367$), the blast ($t \approx 2.85\cdot10^{-4}$)
     and the jets.
   * $\vartheta_\ell/\alpha_\ell^{\mathrm{LF}}$ stays small and
     $\theta \approx 1$ throughout.
7. **Stated cost** (§5): "a conflict between the requirement of the
   non-conservative source term, and the conservation property". No
   jump-condition convergence test is reported.

# Notation map

| Wu & Shu (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $G$, $G^*$ | $\mathcal{G}$ | admissible set, and its linearized form |
| $\mathrm{div}_{ij}\bar B$ (eq. 18) | $D_h^{\mathrm{c}}\bar B_h$ | central over $2\Delta x$ |
| $S(U) = (0, B, v, v\cdot B)$ | eight-wave source vector | |
| $[\![B_1]\!]_{i+1/2}$ | jump of the normal component of $B_h$ across a face | |
| $W_h^K$ | locally divergence-free DG space | no registry symbol |
| $\alpha_{\ell,n}^{\mathrm{LF}}$ | $\alpha^{\mathrm{LF}}$ | |
| $\vartheta_\ell$, $\theta$ | CFL correction factors | no registry symbol |

# Pages created or updated

* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): the non-conservative escape, and the scope sentence.
* Updated [Eight-wave formulation](/methods/eight-wave.md): positivity as a second argument for the source term, weighed against Tóth's wrong-jump result.

# Citations

1. `~/papers/mosaic/div-free-amr/2018-SISC-Wu-10113718m1168042.pdf` (doi:10.1137/18M1168042): text extraction. Theorem statements, remarks, §§1, 3.2.1, 4, 5 and Appendix A were read in full. The proofs of Lemma 2.5 and Theorems 3.1 and 3.4 were read in outline only, and no equation from them is reproduced. The reference list has 58 entries.
