---
type: Source
title: "Balsara (2017) — Higher-order accurate space-time schemes for computational astrophysics, Part I: finite volume methods"
description: "Pedagogical review of higher-order Godunov finite-volume methods for Euler, MHD, RHD and RMHD with every formula explicit at third order in 2D: TVD, PPM and modal WENO, SSP-RK and ADER predictors, RKDG with compact WENO and MOOD limiters, PNPM, Balsara's self-adjusting positivity method, HLLI, and the finding that Riemann-solver quality matters less as the order rises."
resource: "doi:10.1007/s41115-017-0002-8"
source_kind: paper
authors: [Balsara D.S.]
year: 2017
venue: "Living Rev. Comput. Astrophys. 3:2"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2017-LRCA-Balsara-101007s41115-017-0002-8.pdf"
tags: [review, weno, ader, dg, positivity, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

An implementation-oriented review of structured-mesh higher-order
finite-volume methods, written for astrophysicists. Every scheme is built
at third order in 2D with all formulas explicit and a step-by-step box.
Most of its content restates methods the bundle already holds; it is
merged where it adds formulas, parameters or evidence: the
[WENO](/methods/weno.md), [PPM](/methods/ppm.md), [ADER](/methods/ader.md),
[SSP-RK](/methods/ssp-runge-kutta.md),
[WENO-limited DG](/methods/weno-limited-dg.md),
[subcell limiting](/methods/a-posteriori-subcell-limiting.md),
[characteristic](/methods/characteristic-decomposition.md),
[scaling-limiter](/methods/positivity-preserving-scaling-limiter.md) and
[Riemann-solver](/methods/approximate-riemann-solvers.md) pages and the
Alfvén-wave, blast, rotor and composite-advection benchmarks.

# Key claims

1. **PNPM** (§§I.2, VI): evolve degree $N$, reconstruct degree $M$; P0PM is
   WENO, PMPM is DG. Limiting 1D CFL numbers (from Dumbser et al. 2008):
   1.00 for $N = 0$, about 0.32 for $N = 1$, 0.17 for $N = 2$, 0.10 for
   $N = 3$ and 0.069 for $N = 4$; divided by the dimension in multi-D. "P1PM
   or P2PM schemes often give most of the sought-after accuracy of a PMPM
   scheme."
2. **Characteristic limiting** with the eigensystem of the *zone centre*,
   neighbours projected into it (§II.1, eqs. 9–11).
3. **PPM** (§II.2, eqs. 12–18): fourth-order edge values with MC-limited
   differences inside; the author prefers resetting an overshooting zone to
   its MC linear profile (eq. 17b) rather than to the constant (eq. 17a).
   "The original PPM scheme was restricted to second order accuracy by the
   use of a monotonicity preserving limiter".
4. **Modal WENO** (§III): third-order stencils with indicator
   $\hat u_x^2 + \tfrac{13}{3}\hat u_{xx}^2$. For FV, linear weights 1, 50–400, 1
   with power 4 and $\varepsilon = 10^{-12}$; the author warns against too large
   a central weight for extreme astrophysical flows. The optimal
   $(0.1, 0.6, 0.3)$ with power 2 pays off "only most effective" for FD.
5. **SSP-RK** (§IV): SSP(5,4) at CFL 1.5 with 15-digit coefficients; the
   CFL divides by the dimension. A quadrature-free face flux freezes the
   HLL speeds at the face centre (§IV.3).
6. **ADER-CG** (§V): a 1D third-order toy predictor in six nodes (eqs.
   58–67) and the 2D relations (eq. 77). "For a temporally Nth order scheme,
   one only needs (N-1) steps"; two iterations at third order, three at
   fourth, followed by a flux "polish" (stepwise box, Steps 7–8).
7. **Compact WENO limiter for DG** (§VI.2, eqs. 95–109): neighbour
   polynomials shifted into the zone with the mean replaced; indicator
   $\hat u_x^2 + \hat u_y^2 + \tfrac{13}{3}(\hat u_{xx}^2 + \hat u_{yy}^2) + \tfrac76\hat u_{xy}^2$;
   linear weights 0.96 centre and 0.01 per neighbour, power 2,
   $\varepsilon = 10^{-12}$, attributed to Zhong and Shu (2013).
8. **MOOD for DG** (§VI.3): at least $(K+1)^d$ subcells; NAD with
   $\delta_0 = 10^{-4}$, $\epsilon = 10^{-3}$, attributed to Dumbser et al. (2014);
   "a simple TVD or low order WENO" fallback. MOOD makes a DG code
   "recursive and difficult to implement".
9. **Self-adjusting positivity** (§VII, eqs. 115–126, from Balsara 2012b): a
   flattener from velocity divergence against the neighbour minimum sound
   speed, spread to pre-shock zones; extended neighbour bounds narrowed at
   strong shocks; Barth-type density rescaling; a common pressure factor
   from a per-node quadratic, at the 3×3 Gauss–Lobatto tensor nodes. It is
   "designed to save a code from a rare code crash"; no CFL theorem is
   claimed, and it is not extended to RMHD.
10. **HLLI** (Apps. D–E): HLL plus linear sub-structure in chosen
    intermediate families; "complete" when all are included, while HLLD
    lacks the slow waves. Preserves stationary contacts.
11. **Riemann-solver quality against order** (§§IX.5, IX.8). On torsional
    Alfvén-wave decay, HLL with a MuSIC solver without sub-structure
    dissipates about 6 times more than HLLI with sub-structure at second
    order, 3 times more at third, and "almost negligible" more at fourth.
    "The second order scheme with superior Riemann solvers is less
    dissipative than the third order scheme with inferior Riemann
    solvers!"
12. **Steepening** (§III.1): "the modern trend consists of forgoing
    excessive reliance on such steepening techniques".

**Tests**: composite advection (400 zones, $t = 10$); hydro, MHD, RHD and
RMHD vortices (log–log plots only, design order "met"); forward step
(sixth-order ADER-DG with MOOD); DMR ($1920\times480$); MHD rotor
($1000^2$); a 3D extreme blast at plasma beta $1.117\times10^{-4}$ ($257^3$,
positive with the self-adjusting method); torsional Alfvén decay;
relativistic rotor (Lorentz factor 30, $4700^2$) and Orszag–Tang.

**Later evidence (batch 18).** The primary source [Dumbser et al. (2008)](/sources/dumbser-2008.md), Table 1, gives 0.33 for $N = 1$, $M = 1$ and 0.32 for $M = 2, 3, 4$. The limits depend on $N$ alone, for every $M \ge N$. The analysis is 1D only, and "divided by the dimension in multi-D" is not in the 2008 paper: its 2D and 3D runs use $0.7/(2N+1)$, or $0.5/(2N+1)$ at fifth and sixth order (§5.2.1).

# Notation map

| Balsara (2017) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $\bar U_{i,j}$ | $u$, $\bar u_i$ | |
| $\hat u_x$, $\hat u_{xx}$; $\hat U_{xy}$ | $\hat u^{(1)}_i$, $\hat u^{(2)}_i$; $\hat u^{(11)}$ | basis $x^2 - \tfrac1{12}$ |
| $IS$ | $\beta_k$ | |
| $\gamma_L, \gamma_C, \gamma_R$ | $d_k$ | collide with $\gamma$ |
| $p$ (weight power) | $q$ | collides with pressure |
| $w^m, l^m, r^m$ | $w^{(p)}, \ell^{(p)}, r^{(p)}$ | |
| $\eta_{i,j}$ (flattener) | $\phi_i$ | same convention |
| $\tau$ (positivity factor) | $\theta$ | collides with the WENO-Z $\tau$ |
| $N$, $M$ (PNPM) | $K$, (words) | $M$ collides with the TVB constant |
| $\delta_m$, $\delta_0$ | $\delta_{\mathrm{DMP}}$, $\delta_0$ | |
| $\Delta x$, $\Delta y$ | $h_x$, $h_y$ | |

# Pages created or updated

* Updated [WENO](/methods/weno.md), [PPM](/methods/ppm.md), [ADER](/methods/ader.md), [SSP Runge–Kutta](/methods/ssp-runge-kutta.md), [WENO limiters for DG](/methods/weno-limited-dg.md), [A posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md), [Local characteristic decomposition](/methods/characteristic-decomposition.md), [Zhang–Shu scaling limiter](/methods/positivity-preserving-scaling-limiter.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* Updated [Circularly polarized Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md), [MHD blast wave](/benchmarks/mhd-blast-wave.md), [MHD rotor](/benchmarks/mhd-rotor.md), [Composite advection profile](/benchmarks/composite-advection-profile.md).
* Also updated in the same run (list completed at the batch-8 deep lint): [Double Mach reflection](/benchmarks/double-mach-reflection.md), [Forward-facing step](/benchmarks/forward-facing-step.md), [Isentropic vortex](/benchmarks/isentropic-vortex.md), [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), [Positivity preservation](/properties/positivity-preserving.md).
* Also cited on [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md), [Multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md), [Nonconvexity of ideal MHD and compound waves](/results/mhd-nonconvexity.md).
* Also cited on [Hermite WENO](/methods/hermite-weno.md) (created 2026-10-13).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2017-LRCA-Balsara-101007s41115-017-0002-8.pdf` (NSF PAR author manuscript, 213 pp., created June 2018, revised after review: it has §IX.8 and cites 2017 volumes that arXiv:1703.01241v1, the submitted version, lacks; doi:10.1007/s41115-017-0002-8 checked on Crossref: Living Rev. Comput. Astrophys. 3(1):2, December 2017): text extraction, all of §§I–X; appendices read for prose and the HLL/HLLI formulas; eqs. 64, 67, 115–117, 121–122, 126 and the boost formulas read from the page images. Convergence results are plots only. Errata noted: a $\beta_yv_x$ for $\beta_yv_y$ in the boost formulas (p. 133), "Fig. 5" for Fig. 25, a duplicated eq. (64). Reference list: 314 entries (Crossref counts 292 for the published version).
