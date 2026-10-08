---
type: Source
title: "McCorquodale & Colella (2011) — A high-order finite-volume method for conservation laws on locally refined grids"
description: "Fourth-order finite volume in space and time on Berger–Colella AMR hierarchies with subcycling: average–point conversions with h²/24 corrections, a modified Colella–Sekora PPM limiter, classical RK4, conservative least-squares interpolation, refluxing of the RK4 total flux, and coarse–fine ghost values that match the fine Runge–Kutta stages, without which the limiter fires and the order collapses."
resource: "doi:10.2140/camcos.2011.6.1"
source_kind: paper
authors: [McCorquodale P., Colella P.]
year: 2011
venue: "Commun. Appl. Math. Comput. Sci. 6:1-25"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2011-CAMCoS-McCorquodale-102140camcos201161.pdf"
tags: [amr, finite-volume, fourth-order, ppm, time-discretization]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The single-level fourth-order scheme of Colella et al. (2011) is extended
to nonlinear systems and put on block-structured AMR with refinement in
time. The AMR contribution is the ghost-cell interpolation in space
(constrained least squares) and in time (stage-consistent dense output).
Merged into the new [fourth-order finite volume](/methods/fourth-order-finite-volume.md)
page and into the high-order AMR, PPM, finite-volume reconstruction,
critical-point and SSP pages.

# Key claims

1. **Time** (§2.1, eqs. 5–11). Classical RK4 in conservation form with
   the RK4-weighted total flux, which also feeds the flux registers. Not SSP.
2. **Fluxes** (§2.2, eqs. 12–20). Average-to-point and point-to-average
   conversions with $h^2/24$ Laplacian corrections, applied to
   lower-order arguments to keep the stencil small. The four-point face
   formula of PPM, then a face-centre flux plus a transverse-Laplacian
   correction. No Gauss points.
3. **Boundaries** (§2.3, eqs. 21–22). One-sided fourth-order face formulas.
4. **Limiter** (§2.4). A modified Colella–Sekora limiter in primitive
   variables. It drops PPM's first stage and adds a third-derivative
   test ($C_3 = 0.1$) that restores fourth order at smooth multi-D extrema
   such as those of $x^3 - xy^2$. Flattening and an $O(h^4)$ artificial
   viscosity handle strong shocks (§2.5).
5. **Stability** (§4, eq. 57). About 1.3925 for the summed directional
   Courant number, from RK4 with first-order upwinding.
6. **AMR** (§3, Sidebar 1). Berger–Colella nesting with a buffer
   $\lceil 5/r_{\mathrm{AMR}}\rceil + 2$, recursive subcycling, averaging
   down, refluxing.
7. **Ghost values in time** (§3.1, eqs. 39–49). A Fok–Rosales cubic
   dense output of the coarse step, corrected so that the ghost values
   match the Taylor expansions of the fine stage values.
8. **Ghost values in space** (§3.2, eqs. 50–56). A degree-3 constrained
   least-squares fit, exact on the coarse average, over 12–13 (2D) or
   31–33 (3D) coarse cells. It is also used for regridding.
9. **Accuracy** (§4.2). $O(h^4)$ truncation away from coarse–fine
   boundaries and $O(h^3)$ at them; about $O(h^{15/4})$ observed in the
   max norm.
10. **Tests** (§4). Linear advection of a Gaussian and a square wave
    (Table 1); a Gaussian acoustic pulse on one level, two fixed levels
    and adaptive levels (Tables 2–4); a shear flow where the naive time
    interpolation with the limiter on drops to rates 1.39 and 1.59
    (Table 5); the Woodward–Colella "shock-ramp" (double Mach
    reflection) with ratio 4, no set-up given (§4.4).

# Notation map

| McCorquodale & Colella (2011) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\langle U\rangle_i$, $U_i$ | $\bar u_i$, $u_i$ | |
| $W$, $\langle W\rangle_i$, $\overline W_i$ | $\mathbf W$, $\langle\mathbf W\rangle_i$, $\mathbf W(\bar u_i)$ | the paper's overbar is not an average |
| $\vec u$ | $\mathbf v$ | |
| $\Delta^{(2)}$, $\Delta^{d,2}$ | $\Delta_h$, $\Delta^\perp_h$ | registry $\Delta^l$ is the undivided difference |
| $e^d$ | $\mathbf e_d$ | |
| $\langle F^d\rangle^{\mathrm{tot}}$ | $\hat f^{\mathrm{tot}}_{i+1/2}$ | |
| $k_1, \dots, k_4$, $\chi$ | $k_m$, $\chi$ | |
| $f(\langle U\rangle)$ (right-hand side) | $\mathcal L(u)$ | registry $f$ is the flux |
| $\rho_i$ (limiter ratio) | (words) | collides with density |
| $\eta_i$ (flattening, 1 = none) | $1 - \phi_i$ | opposite convention |
| $\nu^d$, $\alpha$, $\beta$, $\lambda^d$ (viscosity) | (words) | all collide with registry symbols |
| $n^l_{\mathrm{ref}}$ | $r_{\mathrm{AMR}}$ | |

# Pages created or updated

* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Created [Fourth-order finite-volume method with average–point conversions](/methods/fourth-order-finite-volume.md).
* Updated [High-order adaptive mesh refinement for capturing schemes](/methods/high-order-amr.md).
* Updated [Piecewise parabolic method (PPM)](/methods/ppm.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Notation registry](/notation.md): batch-5 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2011-CAMCoS-McCorquodale-102140camcos201161.pdf` (doi:10.2140/camcos.2011.6.1, checked on Crossref: Commun. Appl. Math. Comput. Sci. 6(1):1–25, 2011; typeset journal article): text extraction, all sections; every quoted equation checked on the page images. Not given in the paper: the double-Mach set-up, the Riemann solver, the flattening formula and the explicit stage-matched ghost formulas. Eq. 29 has a probable typo ($\delta^2 w$ for $\delta w$), recorded as printed. Reference list: 15 entries.
