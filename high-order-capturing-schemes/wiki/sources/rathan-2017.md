---
type: Source
title: "Rathan & Naga Raju (2017) — An improved non-linear weights for seventh-order weighted essentially non-oscillatory scheme"
description: "Seventh-order WENO (WENO-NS7) with L¹-type local smoothness indicators from generalized undivided differences (fourth-order accurate derivative approximations) and a global indicator, with a power s that keeps seventh order at critical points of order one and two."
resource: "doi:10.1016/j.compfluid.2017.08.023"
source_kind: paper
authors: [Rathan S., Naga Raju G.]
year: 2017
venue: "Comput. Fluids 156:496-514 (read as arXiv:1611.06755v1, 2016)"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2016-arXiv-Rathan-1048550arXiv161106755.pdf"
tags: [weno, nonlinear-weights, critical-points, very-high-order]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Extends the fifth-order $L^1$-indicator approach of Ha et al. to seventh
order. The archived file is arXiv:1611.06755v1; the slug follows the
Computers & Fluids version (verified on Crossref), and the reference list
is the preprint's. Merged into
[smoothness indicator](/definitions/smoothness-indicator.md),
[weight accuracy conditions](/results/weno-weight-accuracy-conditions.md),
[accuracy at critical points](/properties/accuracy-at-critical-points.md)
and benchmark pages.

# Key claims

1. **Review** (§1) of WENO-JS, WENO-M, WENO-Z, Castro, Arandiga et al.
   ($\varepsilon \propto h^2$), Don–Borges, Fan, Ha et al., Kim et al.
2. **Indicators** (§3): $\beta_k = \xi_1\vert L_{1,k}f\vert + \xi_2\vert L_{2,k}f\vert + \vert L_{3,k}f\vert$
   with generalized undivided differences (eq. 11), fourth-order accurate
   at $x_{i+1/2}$ (Theorem); balancing $\xi_1, \xi_2 \in (0,1]$ tuned per
   problem class (0.1/1, 0.1/0.3, 0.3/0.3).
3. **Weights** (eqs. 13–14, 19) with a global indicator and power $s$;
   sufficient condition met at $n_{\mathrm{cp}} \le 2$ for $s \ge 2$.
4. **Tests**: linear advection with jumps and with critical points of order
   1 and 2, composite advection, Burgers, Sod-type, Lax, Shu–Osher, a 2D
   Riemann problem; compared against WENO-BS7 and WENO-Z7; linear
   $m$-stage SSP and SSP(5,4) time stepping.

# Notation map

| Rathan & Naga Raju (2017) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $L_{s,k}f$ | generalized undivided differences | no registry symbol |
| $\xi_1$, $\xi_2$ | balancing parameters | renamed in prose: registry $\xi$ is the wavenumber |
| $\zeta$ | global indicator ($\tau$ role) | |
| $s$ | exponent on the weight ratio | |
| $d_k = (1, 12, 18, 4)/35$ | $d_k$ | seventh order |
| $\Delta x$ | $h$ | |

# Pages created or updated

* Updated [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO-Z](/methods/weno-z.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Accuracy conditions on WENO nonlinear weights](/results/weno-weight-accuracy-conditions.md).
* Updated [Notation registry](/notation.md): batch-2 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-arXiv-Rathan-1048550arXiv161106755.pdf` (arXiv:1611.06755v1; published as doi:10.1016/j.compfluid.2017.08.023): text extraction, all sections; the weight formulas (13), (14), (19) and the error tables are illegible in the text layer and described, not reproduced. Reference list: 34 entries.
