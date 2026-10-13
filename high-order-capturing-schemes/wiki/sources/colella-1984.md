---
type: Source
title: "Colella & Woodward (1984) — The piecewise parabolic method (PPM) for gas-dynamical simulations"
description: "PPM: fourth-order edge interpolation with monotonized parabolas, Lagrangian and single-step Eulerian Riemann states from characteristic domains of dependence, contact steepening, shock flattening and extra dissipation for slow strong shocks."
resource: "doi:10.1016/0021-9991(84)90143-8"
source_kind: paper
authors: [Colella P., Woodward P.R.]
year: 1984
venue: "J. Comput. Phys. 54:174-201"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1984-JCP-Colella-1010160021-99918490143-8.pdf"
tags: [ppm, godunov, reconstruction, limiter, contact-discontinuity]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The detailed description of the piecewise parabolic method, the most
accurate scheme in the authors' comparison of shock-hydrodynamics
methods (their refs. [1], [2]). It is a MUSCL-type higher-order Godunov
method with three new elements: parabolic interpolants (steeper
discontinuities, especially contacts), a simpler and more robust
treatment of the nonlinear wave interactions used for the fluxes, and
dissipation added where any higher-order Godunov scheme of this type
needs it. Merged into [PPM](/methods/ppm.md).

# Key claims

1. **Advection scheme** (§1): edge values from the quartic interpolant
   of the primitive, monotonized slopes, parabolas reset to monotone
   profiles; third order in general, fourth for small $\Delta t$ on a
   uniform grid; variable meshes handled (needed for Lagrange + remap).
2. **Contact steepening** ("discontinuity detection", eqs. 1.14–1.17),
   only for density and only at contacts (eq. 3.2).
3. **Lagrangian gas dynamics** (§2): interpolate $\tau, v, p$ in mass
   coordinate; Riemann states are averages over the domain of dependence
   of each interface; second order in the nonlinear wave interaction
   (after van Leer), with "very little accuracy lost" on strong shocks.
4. **Single-step Eulerian scheme** (§3): first guess from extreme
   characteristic speeds, corrected per characteristic family.
5. **Dissipation** (§4, Appendix): flattening near strong, steep shocks
   (reduces post-shock oscillations in the Riemann invariants crossing
   the shock); extra dissipation (diffusive flux or alternating grid
   motion) for slowly moving strong shocks, where even first-order
   Godunov has a 3 % post-shock entropy error. The algorithms are "the
   minimal ones": any simplification degraded the results.

# Notation map

| Colella & Woodward (1984) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $a_j$, $a_{L,j}$, $a_{R,j}$ | $\bar u_i$, $u^+_{i-1/2}$, $u^-_{i+1/2}$ | zone average and edge values |
| $\Delta a_j$, $a_{6,j}$ | $\Delta u_i$, $u_{6,i}$ | parabola coefficients |
| $A(\xi)$ | $\mathcal{U}(x)$ | indefinite integral of $a$ |
| $\delta_m a_j$ | limited slope | no registry symbol |
| $\tilde f_j$ | $\phi_i$ | flattening coefficient |
| $\xi$, $\Delta\xi_j$ | $x$, $h_i$ | |

# Pages created or updated

* Created [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Created [Contact-discontinuity sharpening (subcell resolution, artificial compression, steepening)](/methods/contact-sharpening.md).
* Created [Piecewise parabolic method (PPM)](/methods/ppm.md).
* Updated [Notation registry](/notation.md): batch-1 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1984-JCP-Colella-1010160021-99918490143-8.pdf` (doi:10.1016/0021-9991(84)90143-8): text extraction (OCR layer; many equations garbled), all 28 pages read, including the Appendix and the reference list (12 entries). Equations reproduced only where legible: the uniform-grid edge formula (1.9) and the parabola (1.4)–(1.5). The detection, flattening and dissipation formulas of §4 and the Appendix are described in words, not reproduced.
