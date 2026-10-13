---
type: Source
title: "Balsara & Shu (2000) — Monotonicity preserving weighted essentially non-oscillatory schemes with increasingly high order of accuracy"
description: "WENO of orders 7–13 (r = 4–7) with tabulated coefficients and indicators, made robust by the Suresh–Huynh bounds (MPWENO); convergence, flat-extremum degradation, artificial-compression tuning by order, and 1D/2D Euler and MHD tests."
resource: "doi:10.1006/jcph.2000.6443"
source_kind: paper
authors: [Balsara D.S., Shu C.-W.]
year: 2000
venue: "J. Comput. Phys. 160:405-452"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2000-JCP-Balsara-101006jcph20006443.pdf"
tags: [weno, monotonicity, very-high-order, mhd, benchmark]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Extends finite-difference WENO beyond fifth order and pairs it with the
monotonicity-preserving bounds of [Suresh & Huynh (1997)](/sources/suresh-1997.md).
The resulting MPWENO schemes are almost spectrally accurate on smooth
problems at modest extra cost and robust at shocks; the paper also
tests whether the MP bounds keep the order (they do not on flat
extrema), tunes artificial compression for very high order, and argues
for very high order in compressible DNS/LES. Merged into
[WENO](/methods/weno.md),
[monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)
(opening a `Contradictions` entry), [PPM](/methods/ppm.md) (comparisons),
[contact sharpening](/methods/contact-sharpening.md) and the benchmarks.

# Key claims

1. **Uniform order at critical points** (§I): states that Jiang–Shu
   proved uniform third and fifth order for $r = 2, 3$ including at
   critical points, and that Mathematica (proofs omitted) extends uniform
   $(2r-1)$-th order to $r = 4$–$7$.
2. **Fluxes** (§II): characteristic flux components; LLF with $\chi$
   times the stencil maximum of $\vert\lambda\vert$ ($\chi = 1.1$–$1.3$);
   RF variants; LLF for linearly degenerate and RF for genuinely
   nonlinear fields; $\varepsilon = 10^{-10}$, $q = 2$.
3. **Coefficients** (§III): candidate coefficients, indicators and
   optimal weights for $r = 4, 5, 6$; linear-weights-only formulas for
   smooth flows; cost $r^3 + 4r^2 + 2r$ flops; $r = 5$ only 35–50 %
   dearer than $r = 3$.
4. **Unbounded high-order WENO is not monotonicity preserving**; $r = 5$
   with RK3 non-oscillatory at CFL 0.2, slightly oscillatory at 0.4;
   linear stability CFL 1.43 to 0.99 for $r = 3$–$7$.
5. **MP bounds** (§III.d): $\kappa = 2$ (CFL 0.6), large-curvature factor
   4; three curvature measures (MM, M4, M4X); results insensitive to the
   heuristics.
6. **Convergence** (§IV): design order on $\sin(\pi x)$, $\exp(\sin\pi x)$,
   Burgers, 2D advection; on $\sin^4$ every MP bound degrades the order
   ("do not live up to the full extent of the claim made in Suresh and
   Huynh"), yet errors stay far below TVD; $r = 5$ optimal there; 45°
   supersonic vortex: $r = 5$ MPWENO on $50^2$ ≈ $r = 3$ WENO on $100^2$,
   both far better than PPMDE.
7. **Artificial compression** (§V): smaller coefficients at higher order;
   none for $r = 7$; $r \ge 5$ carry contacts over about seven zones.
8. **Tests** (§§VI–VII): composite advection (10 periods), blast waves,
   Brio–Wu and a Ryu–Jones MHD Riemann problem (slow shocks crisp; 400
   zones ≈ TVD with 800), Shu–Osher, forward step, double Mach reflection
   (carbuncle with RF, cured by LLF near shocks), oblique shock–vortex
   interaction. Conclusion: test problems should not be grid-aligned.

# Notation map

| Balsara & Shu (2000) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F$ | $u$, $\mathbf{f}$ | |
| $\hat F_{j+1/2}$ | $\hat f_{i+1/2}$ | |
| $r_{s;j+1/2}$, $l_{s;j+1/2}$, $\lambda_{s;j+1/2}$ | $r^{(p)}$, $\ell^{(p)}$, $\lambda^{(p)}$ | |
| $\hat\lambda_{s;j+1/2}$, $\chi$ | $\alpha_{i+1/2}$ per field, safety factor | |
| $S_{j;k}$, $q^{\pm r}_{s;j;k}$ | $S_k$, $q_k$ | |
| $C^r_k$, $IS^r_k$, $\omega^r_k$ | $d_k$, $\beta_k$, $\omega_k$ | |
| $u^L_{j+1/2}$ | $u^-_{i+1/2}$ | |
| $\alpha$ (MP) | $\kappa$ | |
| $\beta$ (MP) | large-curvature factor | renamed: registry $\beta_k$ is the indicator |
| $d^{\mathrm{MD}}, d^{\mathrm{LC}}$ choices (MM, M4, M4X) | variants of $\mathcal{D}^{\mathrm{M4}}$ | |

# Pages created or updated

* Updated [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Contact-discontinuity sharpening (subcell resolution, artificial compression, steepening)](/methods/contact-sharpening.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [Monotonicity-preserving (MP) limiting](/methods/monotonicity-preserving-limiter.md).
* Updated [Piecewise parabolic method (PPM)](/methods/ppm.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Total variation diminishing (TVD) and bounded (TVB)](/properties/total-variation-diminishing.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2000-JCP-Balsara-101006jcph20006443.pdf` (doi:10.1006/jcph.2000.6443): text extraction, all sections and figure captions; Tables I–IX (coefficients and convergence data) were not transcribed. Reference list: 50 entries.
