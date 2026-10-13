---
type: Source
title: "Jiang & Wu (1999) — A high-order WENO finite difference scheme for the equations of ideal magnetohydrodynamics"
description: "Fifth-order finite-difference WENO for ideal MHD in 1D–3D, with characteristic decomposition on Brio–Wu normalized eigenvectors (seven- and eight-wave), classical RK4 and a Brackbill–Barnes divergence projection, which the Orszag–Tang vortex shows to be necessary for stability."
resource: "doi:10.1006/jcph.1999.6207"
source_kind: paper
authors: [Jiang G.-S., Wu C.-C.]
year: 1999
venue: "J. Comput. Phys. 150:561-594"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1999-JCP-Jiang-101006jcph19996207.pdf"
tags: [weno, mhd, finite-difference, divergence-free, eigenvectors]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The Jiang–Shu fifth-order FD-WENO scheme (Shu–Osher flux form,
Lax–Friedrichs splitting, local characteristic decomposition) is carried
over to ideal MHD, dimension by dimension. Most of the new material is
the MHD eigensystem and the divergence treatment. Merged into the WENO,
characteristic-decomposition, constrained-transport and
conservative-finite-difference pages, the Orszag–Tang page, and the new
[Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) page.

# Key claims

1. **Scheme** (§2.1–2.2, eq. 2.3, checked on the page image). The WENO5
   flux is written as the fourth-order central flux minus a nonlinear
   correction. Jiang–Shu weights with $q = 2$ and $\varepsilon = 10^{-6}$,
   insensitive for $\varepsilon \in [10^{-7}, 10^{-5}]$. Global or local
   Lax–Friedrichs per characteristic field; at high order the splitting
   matters much less than at low order (p. 567).
2. **Time stepping** (p. 570). Third-order TVD RK and a classical,
   non-TVD RK4 are given. All tests use RK4, with $\Delta t \sim h^{5/4}$
   in accuracy runs.
3. **Eigensystem** (§2.3, eqs. 2.25–2.27, page image p. 571). Brio–Wu
   normalization keeps the eigenvectors complete where fast, Alfvén and
   slow speeds coincide. Degeneracy tests are relaxed by about
   $10^{-12}$. Arithmetic-mean interface states differ little from Roe
   averages, which exist as one state only for $\gamma = 2$ (p. 572).
4. **Multi-D** (pp. 572–573). A seven-wave system (normal field dropped)
   and Powell's eight-wave system give the same flux except in the
   normal-field component. Powell's source term is not used.
5. **Divergence projection** (§§1, 3). Solve a Poisson equation by
   relaxation and subtract the gradient. Without it the Orszag–Tang run
   fails at $t \approx 3.9$ (eight-wave) or 2.5 (seven-wave) with negative
   pressure; with it both run to $t = 8$ (§3.4).
6. **Efficiency** (§3.3, Table V). WENO5 costs about 4 times a
   second-order scheme per point update. Extrapolated to 3D at equal
   accuracy, ENO3 needs 2.5 times and the second-order Liu–Lax scheme 20
   times its CPU time.
7. **Caveat** (§§1, 4). MHD is not genuinely nonlinear. Intermediate-shock
   structure is non-unique, so a capturing scheme may depend on its
   dissipation and fail to converge under refinement.
8. **Tests** (§3). Brio–Wu problems 1 and 2, also rotated 45° on a 2D
   grid; intermediate-shock formation from a slow simple wave ($L^1$
   order up to 4.8, Table I); periodic and convective MHD
   Kelvin–Helmholtz; Orszag–Tang ($L^1$ order 4.4 at $t = 0.2$, Table VI).

# Notation map

| Jiang & Wu (1999) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h(x)$, $\bar h_k$ | $\mathcal H$, $f(u_j)$ | registry $h$ is the spacing |
| $\alpha_0, \alpha_1, \alpha_2$ | $\tilde\omega_k$ | registry $\alpha$ is the LF speed |
| $IS_k$, $\epsilon$ | $\beta_k$, $\varepsilon$ | |
| $\varepsilon$ (energy) | $E$ | |
| $L_s$, $R_s$, $\lambda^s$ | $\ell^{(p)}$, $r^{(p)}$, $\lambda^{(p)}$ | |
| $a$ (sound speed) | $c$ | |
| $c_a$, $c_f$, $c_s$, $\alpha_f$, $\alpha_s$, $\beta_y$, $\beta_z$ | (words) | Alfvén, fast, slow speeds and Brio–Wu normalization factors |
| $\phi$ (projection potential) | $\Phi$ | registry $\phi_i$ is the PPM flattening |
| $p^*$ | (words: total pressure) | |
| $L(U)$, $U^{(k)}$ | $\mathcal L(u)$, $u^{(i)}$ | |

# Pages created or updated

* Created [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Notation registry](/notation.md): batch-5 registry extensions.
* Also cited on [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md), [Nonconvexity of ideal MHD and compound waves](/results/mhd-nonconvexity.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1999-JCP-Jiang-101006jcph19996207.pdf` (doi:10.1006/jcph.1999.6207, checked on Crossref: J. Comput. Phys. 150(2):561–594, April 1999; typeset journal article): text extraction, all sections; eqs. 2.3 and 2.25–2.27 read from the page images. The full eigenvector matrices (pp. 571–572) are legible but not transcribed. Internal misprint: p. 572 writes $B_x^2 + B_y^2$ for the $B_y^2 + B_z^2$ of eq. 2.25. Reference list: 36 entries.
