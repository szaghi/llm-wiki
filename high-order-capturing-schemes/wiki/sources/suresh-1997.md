---
type: Source
title: "Suresh & Huynh (1997) — Accurate monotonicity-preserving schemes with Runge–Kutta time stepping"
description: "MP5: a fifth-order five-point interface value limited by a geometric monotonicity-preserving bound designed for RK3, with intervals enlarged near smooth extrema to keep accuracy and a cheap test that skips limiting in smooth cells."
resource: "doi:10.1006/jcph.1997.5745"
source_kind: paper
authors: [Suresh A., Huynh H.T.]
year: 1997
venue: "J. Comput. Phys. 136:83-99"
local_file: "~/papers/mosaic/high-order-capturing-schemes/1997-JCP-Suresh-101006jcph19975745.pdf"
tags: [limiter, monotonicity, high-order, mp5]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Takes the limiting route (PPM, Leonard) rather than ENO/WENO adaptivity:
compute an accurate interface value from five cell averages, then bring
it into an interval that guarantees monotonicity under RK3 but is wide
enough near smooth extrema to leave an accurate value untouched. The
geometric framework uses minmod and median. Merged into
[monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md),
where its accuracy claim is disputed by
[Balsara & Shu (2000)](/sources/balsara-2000.md).

# Key claims

1. **Five points needed** to distinguish an extremum from a discontinuity
   (Fig. 2.1); three-point TVD stencils cannot.
2. **Original value** (2.1), fifth order; fourth-order low-phase-error
   and implicit fifth-order alternatives; $2m-1$ orders from wider
   stencils (seventh and ninth given).
3. **First-order MP constraint** (2.12–2.14) keeps monotone data monotone
   per stage for CFL $\le 1/(1+\kappa)$; $\kappa = 4$ for RK; first order
   at extrema.
4. **Accuracy-preserving constraint** (2.15–2.26): intervals enlarged by
   $u^{\mathrm{MD}}$, $u^{\mathrm{LC}}$ with the M4 curvature (2.27);
   proof of monotonicity on monotone data; continuous dependence on data.
5. **Economy** (2.30): limiting bypassed in most smooth cells.
6. **Systems and multi-D** (§3): characteristic variables frozen at the
   cell centre; Roe flux with Huynh's entropy fix; 2D through the
   Shu–Osher FD (ENO-LLF) framework.
7. **Experiments** (§4): $\sin^4$ advection (MP5 ≈ unlimited quartic,
   approaching fifth order at CFL 0.05), composite profile, Sod, Lax,
   Shu's problem, oblique shock reflection, double Mach reflection;
   favourable against WENO5 and ENO3 in accuracy and CPU time.

# Notation map

| Suresh & Huynh (1997) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $v_j$ | $\bar u_i$ | cell averages |
| $v^L_{j+1/2}$, $v^R_{j+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| original $v^L_{j+1/2}$ | $u^{\mathrm{or}}_{i+1/2}$ | |
| $v^{\mathrm{MP}}$, $v^{\mathrm{MD}}$, $v^{\mathrm{LC}}$, $v^{\min}$, $v^{\max}$ | $u^{\mathrm{MP}}$, $u^{\mathrm{MD}}$, $u^{\mathrm{LC}}$, $u^{\min}$, $u^{\max}$ | |
| $\alpha$ | $\kappa$ | renamed: registry $\alpha$ is the LF speed |
| $d_j$ | $\delta^2 \bar u_i$ | |
| $d^{\mathrm{M4}}_{j+1/2}$ | $\mathcal{D}^{\mathrm{M4}}_{i+1/2}$ | |
| $\sigma$ | CFL number $\nu$ | |
| $\epsilon = 10^{-10}$ | round-off tolerance | |

# Pages created or updated

* Updated [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [ENO reconstruction and schemes](/methods/eno-reconstruction.md).
* Created [Monotonicity-preserving (MP) limiting](/methods/monotonicity-preserving-limiter.md).
* Updated [Piecewise parabolic method (PPM)](/methods/ppm.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Total variation diminishing (TVD) and bounded (TVB)](/properties/total-variation-diminishing.md).
* Updated [Notation registry](/notation.md): batch-1 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1997-JCP-Suresh-101006jcph19975745.pdf` (doi:10.1006/jcph.1997.5745): text extraction, all sections, Appendix (FORTRAN listings skimmed) and the reference list (25 entries). Formulas (2.22), (2.29) for $u^{\mathrm{LC}}$ and $u^{\mathrm{MD}}$ are illegible in the text layer and are described, not reproduced.
