---
type: Source
title: "Hedayati Nasab et al. (2021) — Optimal Runge-Kutta Stability Polynomials for Multidimensional High-Order Methods"
description: "Computes optimal explicit Runge–Kutta stability polynomials from multidimensional von Neumann eigenspectra of flux-reconstruction DG on six element types, finds gains over 1D-optimized polynomials only on simplex and prism elements, and reports per-stage speedups up to 1.97 over RK4."
resource: "doi:10.1007/s10915-021-01620-x"
source_kind: paper
authors: [Hedayati Nasab S., Pereira C.A., Vermeire B.C.]
year: 2021
venue: "J. Sci. Comput. 89:11"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Scientific_Computing_Hedayati_Optimal_Runge-Kutta_Stability_Polynomials_for_Multidimension.pdf"
tags: [runge-kutta, explicit, stability, method-of-lines, high-order-methods]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper computes [optimal stability polynomials](/methods/optimal-stability-polynomial.md)
for explicit Runge–Kutta methods. An optimal polynomial gives the largest
linearly stable step for a given number of stages $s$ and order $p$. Here the
optimization is done for discontinuous Galerkin discretizations recovered by
the flux reconstruction (FR) approach, on line, quadrilateral, triangular,
hexahedral, prismatic and tetrahedral elements. Earlier such polynomials for
DG/FR had been generated only from 1D eigenspectra.

The pipeline has three steps:

1. A multidimensional von Neumann analysis of upwind FR-DG for linear advection
   gives the semi-discrete eigenvalues over all wavenumbers and advection
   directions.
2. The hull of these eigenvalues defines the target set.
3. The Ketcheson–Ahmadia algorithm finds the polynomial. A convex inner problem
   fixes the free monomial coefficients of the
   [stability polynomial](/definitions/stability-function.md) $P(z)$, and a
   bisection on $h$ wraps it, converged to $10^{-12}$.

Polynomials are produced for spatial degrees $k=1,\dots,6$, orders $p=1,\dots,4$
and up to $s=16$ stages.

The maximal stable step grows about linearly with $s$. The stage-normalized
step $h_{\mathrm{opt}}/s$ saturates for $p=1,2$ but still grows beyond $s=16$
for $p=3,4$. For quadrilaterals and hexahedra, the multidimensional optimum
equals the 1D one. Triangles, prisms and tetrahedra gain up to 1.12, 1.09 and
1.09 respectively, because their spectra protrude towards the negative real
axis. Against RK3,3 and RK4,4 at $s=16$ and $k=4$, the per-stage speedups are
1.46–1.74 for $p=3$ and 1.63–1.97 for $p=4$.

Butcher tableaus are built from the polynomials by least truncation; they are
given in the supplementary material, not in the paper. Manufactured-solution
advection on every element type confirms the design orders. A
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) DNS at
$\mathrm{Re}=1600$ compares the optimal $s=16$, $p=4$ scheme with RK4,4, both
run at 80% of their maximal stable step. It gives step-ratio speedups of 1.68
(hexahedra), 1.64 (prisms) and 1.57 (tetrahedra), with indistinguishable
kinetic-energy dissipation and enstrophy.

# Version read

The file is the Springer version of record (with a "corrected publication 2021"
notice on page 1): 30 pages, received 30 Aug 2020, published online 24 Aug 2021.
Page 1 matches Crossref for title, venue, article number and DOI. The archive
filename shortens the two-word surname "Hedayati Nasab" to "Hedayati". The
supplementary material (tableaus and polynomial coefficients) is not part of the
file.

# Key claims

1. An explicit RK method applied to $y'=\lambda y$ advances by $y_{n+1}=P(z)y_n$, $z=h\lambda$. Linear stability requires $\lvert P\rvert\le1$. Order $p$ requires $\theta_j=1/j!$ for $0\le j\le p$, which leaves $s-p$ free coefficients (§2, eqs. 1–3). **Stated**
2. $p=s$ is possible up to order 4 for nonlinear equations (§2, citing Butcher). **Stated**
3. Maximizing $h$ subject to $\lvert P(h\lambda)\rvert\le1$ over all semi-discrete eigenvalues (eq. 6) is nonconvex for $s>2$ and has sub-optimal local minima. The Ketcheson–Ahmadia reformulation makes the inner problem convex and the outer one a scalar bisection (§3.1, eqs. 7–8, Alg. 1). **Stated**
4. The bisection is converged to $10^{-12}$ in Matlab 2016a, and the inner problem is solved with CVX at "best" precision (§3.1). **Stated**
5. Semi-discrete eigenvalues computed in double precision can show spurious positive real parts at machine-precision level. These were removed before optimization (§5). **Stated**
6. Optimal polynomials are generated for 1D, quadrilateral, triangle, hexahedron, prism and tetrahedron elements with $k=1,\dots,6$, $p=1,\dots,4$ and $s\le16$. A hull of the eigenspectrum replaces the full eigenvalue set to reduce cost (§6.1–6.3). **Shown**
7. $h_{\mathrm{opt}}$ grows about linearly with $s$ for all element types (§6, Figs. 4, 11, 13, 15, 17, 19). **Shown**
8. For $k=0$, higher temporal order carries a roughly constant penalty in $h_{\mathrm{opt}}$. For high-order spatial discretizations, $p=2$ nearly matches the $h_{\mathrm{opt}}$ of $p=1$ at large $s$ (§6.1, Fig. 4). **Shown**
9. The stage-normalized step $h_{\mathrm{opt}}/s$ grows with $s$. It saturates for $p=1,2$, while $p=3,4$ "continue to benefit beyond $s=16$ stages" (§6, Fig. 6, $k=4$). **Shown**
10. At small $s$, the stability regions of higher-order schemes protrude well beyond the scaled eigenspectrum. As $s$ grows they conform to its shape (§6.1, Fig. 5). **Shown**
11. Quadrilateral and hexahedral eigenspectrum hulls and stability regions are visually indistinguishable from the 1D ones. Triangles, prisms and tetrahedra differ because their spectra protrude towards the negative real axis (§6.2–6.3). **Shown**
12. For $k=4$, optimizing for quadrilaterals or hexahedra gives no gain over the 1D-optimal polynomial: the ratio is 1.00 at every $s$ and $p$ (Tables 1, 3). **Shown**
13. For $k=4$, the gain in $h_{\mathrm{opt}}$ over the 1D-optimal polynomial reaches 1.12 on triangles (Table 2), 1.09 on prisms (Table 4) and 1.09 on tetrahedra (Table 5) (§6.4). **Shown**
14. $h_{\mathrm{opt}}/h_{\mathrm{RK3,3}}$ at $s=16$, $k=4$: hexahedron 8.31, prism 9.07, tetrahedron 7.77, quadrilateral 8.31, triangle 9.29, line 8.32 (Table 6). **Shown**
15. The speedup over RK3,3, $(h_{\mathrm{opt}}/s)/(h_{\mathrm{RK3,3}}/3)$, at $s=16$, $k=4$ is 1.46–1.74 (§6.5, Table 7). **Shown**
16. $h_{\mathrm{opt}}/h_{\mathrm{RK4,4}}$ at $s=16$, $k=4$: hexahedron 6.99, prism 7.67, tetrahedron 6.52, quadrilateral 7.00, triangle 7.88, line 7.00 (Table 8). **Shown**
17. The speedup over RK4,4, $(h_{\mathrm{opt}}/s)/(h_{\mathrm{RK4,4}}/4)$, at $s=16$, $k=4$ is 1.63–1.97. This is the abstract's "up to 1.97" (§6.5, Table 9). **Shown**
18. Butcher tableaus realizing each polynomial are built with the Ketcheson–Ahmadia least-truncation method and given in the supplementary material (§7.1, §8). **Stated**
19. In manufactured-solution linear advection ($s=16$, $p=1,\dots,4$, $k=6$, all five multidimensional element types), "all schemes achieve their designed order of accuracy" (§7.1, Fig. 7). **Shown**
20. In the Taylor–Green vortex DNS ($\mathrm{Re}=1600$, Mach 0.1, $k=5$, about $256^3$ solution points), both schemes run at 80% of their maximal stable step. The optimal $p=4$, $s=16$ scheme gives speedups over RK4,4 of 1.68 (hexahedra), 1.64 (prisms) and 1.57 (tetrahedra). These are step and stage ratios; no wall-clock timings are reported (§7.2). **Shown**
21. The speedups come "with negligible code modification, simply the substitution of the coefficients in the Butcher tableau" (§7.2). **Stated**
22. Taylor–Green Q-criterion isosurfaces at $t=15t_c$, the kinetic-energy dissipation rate and the enstrophy of the classical and optimized schemes are visually indistinguishable (§7.2, Figs. 8–10). **Shown**
23. Pereira and Vermeire showed that, away from the stability limit, the dispersion and dissipation properties of optimal RK schemes are similar to those of conventional ones (§5). **Stated**

# Printed slips

- Hull terminology is inconsistent. §6.2–6.3 and the captions of Figs. 12, 14, 16, 18 and 20 say "concave hull", while the same paragraphs speak of "their resulting convex hull".
- §3.1 (p. 4) says "$|P_{s,q}(z)|$ is linear in $\gamma_j$. Therefore, Equation 7 is convex". The polynomial is affine in its coefficients; its modulus is convex, not linear.
- §7.1, eqs. 25–26: the exact solution is printed as $e^{\kappa|\mathbf x-\boldsymbol\alpha t|^2}$ (positive exponent), while the initial condition is $e^{-\kappa|\mathbf x|^2}$.
- §6.2 and §6.3 refer to "the multi-dimensional Von Neumann analysis presented in Sect. 4". It is in Sect. 5.
- §5 says "rewrite Equation 14 at the discrete level", but the semi-discrete equation is Eq. 13.
- Polynomials are said to be generated for $p=1,\dots,6$ (spatial degree), but the figures also show degree 0.
- The captions of Tables 6 and 8 print the stage-normalized ratio that defines Tables 7 and 9. The tables themselves report plain step ratios.
- §7.2: "at a non-dimensional simulation time of $t_c=15$" should read $t=15t_c$. The paper also uses $\epsilon$ for both the bisection tolerance and the dissipation rate, and misspells "enstropy".
- Reference list: [4] reverses the author order of HW-II and calls it "I"; [17] has pages "1753–1751"; [2] has "Willy" as publisher; [5] has "intergration"; [30] gives the Castonguay thesis as "Stanford University Press (2012)".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u'=\omega u$, $\omega$ | $y'=\lambda y$, $\lambda$ | test equation; $\omega$ is a semi-discrete eigenvalue |
| $\Delta t$ | $h$ | step size; the source's $h$ is the element edge length |
| $z=\omega\Delta t$ | $z=h\lambda$ | |
| $P_{s,q}(z)$ | $P(z)$ | stability polynomial with $s$ stages and order $p$ |
| $\gamma_j$ | $\theta_j$ | monomial coefficients; **collision**: registry $\gamma$ is tree density |
| $q$ | $p$ | **collision**: the source's $q$ is the temporal order, registry $q$ is stage order |
| $p$ | $k$ (spatial degree) | **collision**: the source's $p$ is the FR/DG solution degree, registry $p$ is the order; $k$ is page-local (not in the registry) |
| $s$ | $s$ | stages (agrees) |
| $S$ | $\mathcal S$ | region of absolute stability |
| $\Delta t_{max}$, $\Delta t_{opt}$, $P_{opt}$ | $h_{\max}$, $h_{\mathrm{opt}}$, optimal $P$ | $\Delta t_{max}$ is also the bisection upper bound (overloaded) |
| $\boldsymbol\omega^\delta$ | eigenvalue set of $L$ | $L$ is the semi-discrete operator (agrees) |
| $RK_{s,q}$ | RK$s$,$p$ | classical baselines RK3,3 and RK4,4 |
| $\epsilon$ | — | bisection tolerance in Alg. 1; kinetic-energy dissipation rate in §7.2 |

# Reference list

The paper prints 32 references in numbered style ([1]–[32]). The list is merged
complete into the [bibliography](/bibliography.md), with `citedby` this slug.
No printed duplicates. Items printed irregularly were entered as printed: [30]
Castonguay is given as a "Stanford University Press" book (likely the PhD
thesis); [1] Huynh is an AIAA conference paper without pages; [19] is
Matlab 2016a software and [20] is the CVX software. All items parsed.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [Internal stability of explicit Runge–Kutta methods](/definitions/internal-stability.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Paired explicit Runge–Kutta (P-ERK) methods](/methods/paired-explicit-runge-kutta.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
