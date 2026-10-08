---
type: Source
title: "Dumbser & Käser (2007) — Arbitrary high order non-oscillatory finite volume schemes on unstructured meshes for linear hyperbolic systems"
description: "ADER finite-volume schemes of arbitrary order on triangles and tetrahedra, built on a reference-element least-squares reconstruction and a WENO that blends whole polynomials of full degree with a dominant central linear weight, so that no negative linear weights arise and one reconstruction per step suffices."
resource: "doi:10.1016/j.jcp.2006.06.043"
source_kind: paper
authors: [Dumbser M., Käser M.]
year: 2007
venue: "J. Comput. Phys. 221:693-723"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2007-JCP-Dumbser-101016jjcp200606043.pdf"
tags: [ader, weno, unstructured, finite-volume]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper builds a reconstruction operator for unstructured 2D and 3D
meshes, taken over from DG technique, and a WENO on top of it that
returns entire polynomials. Combined with the Cauchy–Kowalewski ADER
time integration for linear systems, this gives one-step finite-volume
schemes up to seventh order on triangles and sixth on tetrahedra. Merged
into the new [polynomial WENO](/methods/polynomial-weno.md) and
[ADER](/methods/ader.md) pages.

# Key claims

1. **Reference-element reconstruction** (§2.1): mapping each stencil
   to the target cell's reference element cancels all Jacobians. This
   avoids ill-conditioned reconstruction matrices (Abgrall). The basis is
   hierarchical orthogonal (Dubiner).
2. **Least squares** (§2.2): stencils of $1.5L$ cells in 2D and $2L$ in
   3D, solved with exact conservation in the target cell. No singular
   matrix was met.
3. **WENO of whole polynomials** (§2.3): one central, three primary and
   three reverse sector stencils in 2D (4 + 4 in 3D). Linear weights are
   1 for one-sided stencils and $\lambda_1 = 10^3$ for the central one,
   with $\epsilon = 10^{-5}$ and $r = 4$ (eqs. 19–22). The oscillation indicator
   is a mesh-independent quadratic form with a universal matrix
   (eqs. 23–25). There are no negative weights, because the linear weights
   do not carry accuracy.
4. **ADER-FV for linear systems** (§3): time integration and flux
   evaluation are exchanged. Cauchy–Kowalewski is written in reference
   coordinates (eq. 42), with flux matrices precomputed and an exact
   Riemann solver. The scheme is stable to Courant number 1 in 1D (cited).
5. **Convergence** (§4, Tables 5–8): linearized Euler with orders 2–7
   on irregular triangles and 2–6 on regular tetrahedra, linear and
   WENO. WENO costs at most twice the linear reconstruction.
6. **Non-oscillatory tests** (§5): insensitivity to $\lambda_1$ in
   $[10^2, 10^5]$ (slotted cylinder, smooth vortex), kinematic
   frontogenesis to sixth order, a hollow sphere on 191,933 tetrahedra,
   and the composite profile on 1:20 stretched tetrahedra.
7. **Cost argument** (§6): fifth order on tetrahedra would need 84
   optimal WENO reconstructions per element and step with RK3. ADER with
   polynomial WENO needs one, and gets fifth order in time too. The
   authors claim the first 3D unstructured WENO.

# Notation map

| Dumbser & Käser (2007) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M$ (degree), $M + 1$ (order) | $K$, $K + 1$ | |
| $w^{(m)}$, $\hat w_l$, $\Psi_l$ | $\mathcal{P}_i$, $\hat{\mathbf u}_k$, basis | element $T^{(m)}$ is cell $i$ |
| $\lambda_i$, $\lambda_1$ | $d_k$, $d_{\mathrm c}$ | registry $\lambda$ is an eigenvalue |
| $\tilde\omega_i$, $\omega_i$ | $\tilde\omega_k$, $\omega_k$ | |
| $\sigma_i$, $\Sigma_{lm}$ | $\beta_k$, $\mathsf B$ | registry $\Sigma^2$ is the GP kernel amplitude |
| $\epsilon$, $r$ | $\varepsilon$, $q$ | registry $r$ counts stencils |
| $A^N_{pq}$, $R^N$, $\Lambda^N$ | $A$, $R$, $\Lambda$ along the face normal | |
| $\xi, \eta, \zeta$ | reference coordinates | registry $\xi$ is a wavenumber; not used on concept pages |

# Pages created or updated

* Created [ADER one-step schemes (arbitrary high order using derivatives)](/methods/ader.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Updated [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Order barriers and optimal coefficients of SSP time discretizations](/results/ssp-order-barriers.md).
* Created [Polynomial WENO reconstruction with a dominant central stencil](/methods/polynomial-weno.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [WENO limiters for discontinuous Galerkin schemes](/methods/weno-limited-dg.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Notation registry](/notation.md): batch-4 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2007-JCP-Dumbser-101016jjcp200606043.pdf` (doi:10.1016/j.jcp.2006.06.043, checked on Crossref; typeset JCP article, issue 2007, online 2006): text extraction, all sections; eqs. 19–25 read from the page images (pp. 700–701). The ADER matrices of §3 (eqs. 43–52) are only partly legible in the text layer and are not reproduced. Reference list: 48 entries.
