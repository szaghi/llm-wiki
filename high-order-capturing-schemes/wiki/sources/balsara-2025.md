---
type: Source
title: "Balsara, Bhoriya, Shu & Kumar (2025) — Efficient alternative finite difference WENO schemes for hyperbolic conservation laws"
description: "Makes the alternative finite-difference WENO formulation general-purpose up to ninth order: a derivation of the even-derivative flux corrections, WENO-AO pointwise interpolation formulas, and a boundary-centred WENO interpolation of A∂u that suppresses the corrections at shocks, with any Riemann solver at the cost of classical FD-WENO."
resource: "doi:10.1007/s42967-023-00360-z"
source_kind: paper
authors: [Balsara D.S., Bhoriya D., Shu C.-W., Kumar H.]
year: 2025
venue: "Commun. Appl. Math. Comput. 7:2189-2242 (online 2024; read as the 100-page author manuscript)"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2024-CAMC-Balsara-101007s42967-023-00360-z.pdf"
tags: [finite-difference, weno, interpolation, adaptive-order, riemann-solver]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Revives Shu and Osher's alternative FD formulation by removing three
obstacles: an opaque derivation, undocumented WENO interpolation
formulas, and Gibbs oscillations from the flux-derivative corrections.
The archived file is an author manuscript (no journal page numbers). The
article appeared online on 6 May 2024 in volume 7 (2025); the slug
carries the issue year (bundle law, decided at this batch), and the
filename's "2024" is the online year. Merged into the new
[AFD-WENO](/methods/alternative-finite-difference-weno.md) page and into
WENO-AO, central WENO, Riemann-solver and benchmark pages.

# Key claims

1. **Second-order trap** (§II.a): differencing pointwise-exact interface
   fluxes is only second order; the $-\frac{h^2}{24}\partial_x^2 f$
   correction gives fourth (eqs. 3–7).
2. **Fluxes up to ninth order** (§II.b, eqs. 9–12): coefficients
   $\frac{1}{24}$, $\frac{7}{5760}$, $\frac{31}{967680}$,
   $\frac{127}{154828800}$; recast with $A\,\partial_x u$ (eqs. 13–14)
   to shrink stencils. Checked on the page image.
3. **WENO-AO interpolation** (§III): AO(3) to AO(9,3) and AO(7,5,3) in a
   Legendre basis; indicators unchanged.
4. **Boundary-centred interpolation** (§IV): two straddling third-order
   stencils (plus centred fourth, sixth and eighth order); sign
   disagreement suppresses the derivative, so it acts as a discontinuity
   indicator. Multiresolution variant equivalent.
5. **Implementation and cost** (§V): two characteristic-projection
   steps, as in classical FD-WENO; HLLI/LLFI Riemann solvers; SSP-RK;
   IMEX for stiff sources. Further claimed advantages: any Riemann
   solver, stationary contacts, curvilinear free stream, positivity.
6. **Results** (§§VI–VIII): orders 3–9 for Euler, RHD and ten-moment
   vortices; shock tubes, blast waves, relativistic Riemann problems and
   shock–bubble interactions, forward step and DMR (with flattening).

# Notation map

| Balsara et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\mathbf F$ | $u$, $f$ | |
| $\hat{\mathbf U}^\mp_{i+1/2}$ | $u^\mp_{i+1/2}$ | interpolated, not reconstructed |
| $\mathbf F^*(\cdot,\cdot)$ | $\hat f(\cdot,\cdot)$ | Riemann-solver flux |
| $\mathbf F^{num}_{i+1/2}$ | $\hat f_{i+1/2}$ | |
| $\Delta x$ | $h$ | |
| $\mathbf A$ | $A(u)$ | flux Jacobian |
| $\gamma^{r5}_3$, $\gamma^{r3}_k$, $\gamma_{Hi}$, $\gamma_{Lo}$ | $d_P$, $d_k$, $\gamma_{\mathrm{Hi}}$, $\gamma_{\mathrm{Lo}}$ | |
| $w$, $\bar w$, $\beta$, $\tau$ | $\tilde\omega$, $\omega$, $\beta_k$, $\tau$ | |

# Pages created or updated

* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Created [Alternative finite-difference WENO (AFD-WENO)](/methods/alternative-finite-difference-weno.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Central WENO (staggered, Levy–Puppo–Russo)](/methods/central-weno.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Unequal-stencil and adaptive-order WENO (WENO-ZQ, WENO-AO)](/methods/weno-ao.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2024-CAMC-Balsara-101007s42967-023-00360-z.pdf` (author manuscript, 100 pp., of doi:10.1007/s42967-023-00360-z): text extraction, all sections; eqs. (2)–(13) read from the page images (pp. 8–11). The interpolation coefficients of §§III–IV and the Appendix A script are not reproduced. Reference list (manuscript): 63 entries.
