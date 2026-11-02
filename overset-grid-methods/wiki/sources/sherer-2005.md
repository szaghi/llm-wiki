---
type: Source
title: "Sherer & Scott (2005) — High-order compact finite-difference methods on general overset grids"
description: "Extends a sixth-order compact finite-difference solver with high-order Padé filters to general overset grids with holes, analyses explicit, compact, wavenumber-optimized and B-spline inter-grid interpolation by Fourier error measures, and recommends explicit non-optimized Lagrange interpolation of high order."
resource: "doi:10.1016/j.jcp.2005.04.017"
source_kind: paper
authors: [Sherer S.E., Scott J.N.]
year: 2005
venue: "J. Comput. Phys. 210:459-496"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2005_Crossref_Journal_of_Computational_Physics_Sherer_High-order_compact_finite-difference_methods_on_general_over.pdf"
tags: [overset-grid, high-order, interpolation, finite-difference, hole-cutting]
timestamp: 2026-11-02T14:53:00Z
---

# Summary

Sherer & Scott carry a high-order compact (Padé-type) finite-difference solver with low-pass Padé
filters up to tenth order, the Visbal–Gaitonde FDL3DI lineage, from single-block and
coincident-point multi-block grids to general [overset grids](/definitions/overset-grid.md):
overlaps with non-coincident points and holes cut in grids. The result is the
[high-order overset discretization](/methods/high-order-overset-discretization.md) of the paper.
Two capabilities are added.

- **Holes inside implicit operators.** At hole boundaries the tridiagonal difference and filter
  operators switch to one-sided boundary closures, and every hole point gets the row $\{0,1,0\}$
  with zero right side. The system stays tridiagonal and splits into decoupled regions (see
  [hole cutting](/methods/hole-cutting.md) and [point classification](/definitions/point-classification.md)).
- **High-order [inter-grid interpolation](/methods/inter-grid-interpolation.md)** at
  non-coincident overlaps, applied dimension by dimension in donor computational space. The
  offsets come from a Newton iteration on a high-order isoparametric map, started from the
  second-order offsets and stencils of an external assembly code (see
  [donor search](/methods/donor-search.md) and [domain connectivity](/definitions/domain-connectivity.md)).

The interpolation study compares one general 1-D formula in two families: generalized Lagrange
interpolation, either explicit or "compact" (three receivers coupled in a tridiagonal system),
non-optimized or wavenumber-optimized; and B-spline interpolation with natural-spline end
conditions. A 1-D Fourier error analysis finds compact formulas more accurate, optimization prone
to low-wavenumber error pockets, and B-splines poor in outer subintervals. The "compact" coupling
links receivers inside one donor grid, which is not the cross-grid implicit interpolation of
Chesshire & Henshaw (see [explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)).

Tests: grid-to-grid interpolation of analytic functions, an inviscid convecting vortex through an
overset system with a hole, flow past one and two side-by-side cylinders at $Re=100$
([flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)), and acoustic
scattering from one and three cylinders. Second-order interpolation reduces the sixth-order
solver to second order, as the [interpolation-order requirement](/results/interpolation-order-requirement.md)
predicts; sixth-order interpolation nearly recovers the direct-injection result. A two-point
[fringe](/definitions/fringe-point.md) is used throughout. The authors recommend explicit,
non-optimized Lagrange interpolation, and drop compact interpolation (fragile for arbitrary
receiver distributions) and optimization.

# Version read

The Elsevier version of record (J. Comput. Phys. 210:459–496, received 28 September 2004,
online 22 June 2005), 38 pages, all read; equations and figure annotations were checked visually.
Page 1 agrees with the Crossref card in title, authors, volume and pages. The paper rests on
Sherer's 2002 Ohio State thesis (`sherer-2002`), cited for most extended results. Section,
equation and figure numbers below are those of this version.

# Key claims

Notation, as on [high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md):
$q$ donor points per direction, $b$ receivers coupled per interpolation equation (page-local; the
source's $BW$), $\varpi_k$ receiver coefficients and $\alpha_j$ donor weights, $\bar s_k$ receiver
offsets from the stencil base point in units of donor spacing, $\theta$ the wavenumber (unit
spacing), $r_{\mathrm o}\pi$ and $\theta_{\max}$ the upper limits of the optimization and
error-integration ranges (the source's $r\pi$ and $R\pi$), and $p$ the formal order (the source's
$\sigma$).

1. Delfs showed that linear interpolation, typical of second-order overset solvers, eventually
   corrupts the whole domain when coupled with high-order schemes; Chesshire & Henshaw showed
   that linear interpolation cannot keep global accuracy at the level of a high-order
   discretization. (§1) **Stated**
2. The general 1-D interpolation formula is $\sum_{k=1}^{b}\varpi_k\hat u(\bar s_k)=\sum_{j=0}^{q-1}\alpha_ju_j$
   (Eq. (1)): $b=1$ explicit, $3$ tridiagonal ("compact"), $5$ pentadiagonal; only
   $b\le3$ is considered. (§2) **Stated** (definition)
3. The maximum formal order of a $b$-wide formula on a $q$-point stencil is
   $p_{\max}=q+b-1$ (Eq. (4)); classical Lagrange interpolation has $p=q$. (§2.1)
   **Stated**
4. Optimized coefficients minimize $E_{\mathrm{opt}}=\int_0^{r_{\mathrm o}\pi}\bigl|\sum_k\varpi_ke^{\mathrm i\bar s_k\theta}-\sum_j\alpha_je^{\mathrm ij\theta}\bigr|^2d\theta$
   (Eq. (5)) under $p$ order constraints (A.1) and the normalization $\varpi_{k_c}=1$ (A.2), by a
   Lagrange-multiplier linear system (A.3)–(A.8); $p=p_{\max}$ is non-optimized, $p=1$ fully
   optimized. (§2.1, App. A) **Derived**
5. Closed-form non-optimized coefficients are given for $b=1$ (Eqs. (A.9)–(A.10),
   the classical Lagrange weights) and $b=3$ (Eqs. (A.11)–(A.13)). **Derived**
6. Compact Lagrange interpolation lowers the local error by over an order of magnitude at low
   wavenumbers against an explicit formula on the same stencil. (§3.1, Fig. 2) **Shown** (1-D
   Fourier analysis)
7. Optimization ($r_{\mathrm o}$ from 0.2 to 0.5) lowers the local error for $\theta>1$ but
   produces non-monotone local-error pockets for $\theta\le1$ that widen and grow with
   $r_{\mathrm o}$; Tam and Kurbatskii observed the same for explicit formulas. (§3.1,
   Fig. 2) **Shown**
8. The integrated error vanishes when the receiver coincides with a donor (direct injection) and
   peaks near subinterval midpoints; for $q=6$ the peak rises by an order of magnitude from the
   central to the outermost subinterval. (§3.2, Fig. 4a) **Shown**
9. Raising the order by adding two points on one side only still lowers the integrated error for
   all $q$ considered (up to $q=10$ in the thesis); the trend reverses only at very high
   wavenumbers ($\theta_{\max}>0.5\pi$, about 4 points per wavelength) for explicit formulas
   up to sixth order, and higher for compact ones. (§3.2, Fig. 4b) **Shown** / **Stated** for the
   thesis
10. With $\theta_{\max}=1$ ($2\pi$ points per wavelength) and $q=6$, the
    $r_{\mathrm o}=0.3$ optimized formula has integrated error two to three orders of
    magnitude below the non-optimized one; compact optimization helps for all
    $r_{\mathrm o}\le0.5$; explicit optimization at $r_{\mathrm o}=0.5$ is worse
    than none. (§3.2, Fig. 5) **Shown**
11. The error reduction factor $\log_{10}(E^{\mathrm{opt}}_{\mathrm{int}}/E^{\mathrm{non\text{-}opt}}_{\mathrm{int}})$
    (Eq. (8)) reaches about two orders of magnitude along $\theta_{\max}=r_{\mathrm o}\pi$;
    the breakeven curve is $\theta_{\max}/\pi=1.504\,r_{\mathrm o}+0.005$ for explicit
    $q=6$, valid for $r_{\mathrm o}<0.6$ (Eq. (9), Fig. 6); below it the optimized error can
    be orders of magnitude higher. **Shown** (fit)
12. The B-spline (natural spline) error in the outermost subinterval saturates at a value
    independent of $q$ and several orders above the central value; at the stencil centre the
    order-4 B-spline error becomes $q$-independent for $q\ge10$, order 6 at $q=24$, order 8 not
    yet at $q=30$ (thesis). (§3.2, Fig. 7) **Shown**
13. With $\theta_{\max}=1$ the sixth-order B-spline at the stencil centre has
    integrated error comparable to the optimized compact formula on a four-point stencil. (§3.2,
    Fig. 8) **Shown**
14. Five-point block-to-block (coincident) overlaps suffice to recover interior high-order
    differencing and filtering; a two-point fringe ($n_f=2$) is used at all interpolation
    boundaries. (§4.2) **Stated**
15. Interpolation boundary conditions are applied $T+1$ times per time step ($T$ Runge–Kutta
    stages or subiterations, plus once after filtering). (§4.2) **Stated**
16. Compact interpolation in several dimensions (dimension by dimension, coupled along lines) is
    less robust than explicit or B-spline interpolation: arbitrary receiver distributions
    (clustered or stacked points, too few points, near-coincidence with donors) give singular or
    ill-conditioned systems. (§4.2) **Stated**
17. Points within two points of a hole boundary use boundary difference formulas (five-point
    interior stencil), within five points boundary filters (11-point filter); hole points get rows
    $\{0,1,0\}$ and zero right side, so the system stays tridiagonal and splits into three
    decoupled regions. (§4.4, Fig. 10) **Stated**
18. In grid-to-grid interpolation of four analytic functions the measured orders of non-optimized
    explicit and compact formulas closely match the formal order; compact formulas give 0.5–1 order
    of magnitude less error than explicit ones of the same order, an optimal scenario since every
    foreground point is a receiver. (§5.1, Fig. 12) **Shown**
19. B-spline interpolation does not converge at a consistent rate: the order-4 B-spline beats the
    same-order Lagrange formula on the coarsest grid and matches or beats it on the finest; the
    order-6 B-spline has the largest error on the finest grid. (§5.1, Fig. 12) **Shown**
20. Optimized explicit ($q=6$) interpolation lowers the error on the coarse grid, but the
    non-optimized formula wins under refinement; on the finest grid the error grows with
    $r_{\mathrm o}$ for all functions; optimization is dropped. (§5.1, Fig. 13) **Shown**
21. Convecting vortex on a direct-injection multi-block grid: the 44444 scheme is limited by its
    order, 66666 is unstable on both grids with boundary filters of order 8, 45654 is stable with
    them and matches single-block sixth-order accuracy and is adopted as "C6". A second-order
    boundary filter (the "low-order centered" approach of Gaitonde and Visbal) limits accuracy
    for all schemes. (§5.2, Fig. 15) **Shown**
22. Second-order interpolation makes the whole overset computation second order even with the
    sixth-order compact solver; sixth-order interpolation approaches direct injection. Annotated
    rates: $\sigma=2.01$ for $q=2$, $5.33$ for $q=6$, $6.36$ direct injection, $7.47$ single grid.
    (§5.2, Fig. 16a) **Shown**
23. Preliminary fourth-order B-spline and sixth-order compact interpolation were only marginally
    better, or slightly worse, than non-optimized explicit interpolation in the vortex case
    (thesis). (§5.2) **Stated**
24. Cell-volume ratios of 4 and 16 between inner and outer grids in the overlap cause no
    degradation of the vortex; the filter removes the spurious waves generated by the volume jump.
    (§5.2, Fig. 18) **Shown**
25. Single cylinder, $Re_D=100$: fourth- and sixth-order explicit interpolation match the
    direct-injection drag history; the fourth-order B-spline is worse because of the small overlap
    (receivers in outer subintervals); second order is worst. (§5.3, Fig. 19) **Shown**
26. Two side-by-side cylinders (centres $1.3D$ apart): the computed fundamental Strouhal number
    $\approx0.09$ matches experiment, and the asymmetric gap flow is reproduced. (§5.3,
    Figs. 21–22) **Shown** (against experiment)
27. Acoustic scattering from one cylinder: a second-order boundary filter gives spikes at block
    boundaries; all one-sided filters of order $\ge4$ perform well at this resolution, with no
    instability up to order 8. (§5.4, Fig. 24) **Shown**
28. Fourth- and sixth-order interpolation nearly reproduce the single-grid result; fourth order is
    slightly better than sixth, which the authors attribute to minimal overlap and more one-sided
    stencils for the higher order. (§5.4, Fig. 25; §6) **Shown** (attribution **Stated**)
29. Three-cylinder scattering: the compact C6 solver with sixth-order interpolation is nearly
    indistinguishable from the analytic solution, while the explicit E4F8 scheme with the same
    five-point stencil and fourth-order interpolation shows considerable error. (§5.4, Fig. 26)
    **Shown**
30. Explicit non-optimized Lagrange interpolation offers the best combination of accuracy,
    robustness and ease of use; optimized coefficients need a dense solve, a concern if they must
    be recomputed on the fly for moving grids. (§6) **Stated**

# Printed slips

- **Eq. (14)** is labelled "F1" (p. 476), while the Fig. 12(b) caption calls it "Function F2
  (Eq. (14))" and Eq. (15) is F3: the label should read F2.
- **Eq. (17)** prints the vortex pressure as $p_\infty-p=\frac{\rho C^2}{2R^2}\exp(-r_2)$. Radial
  balance of the printed velocity field gives $\frac{\rho C^2}{2R^2}e^{-r^2}$ in the incompressible
  approximation, so "$r_2$" stands for $r^2$ *(compiler check, not in the sources)*.
- **(B.3)** prints "$B_j^\sigma(x)=0$ for $x\in[t_j,t_{j+\sigma-1}]$", followed by "non-zero only
  over σ contiguous subintervals". From (B.1)–(B.2) the support is $[t_j,t_{j+\sigma})$: the
  statement needs "$\notin$" and the upper index $j+\sigma$.
- **App. B:** "I is the subinterval number ranging from 1 to N" (p. 493), while p. 492 numbers the
  $N-1$ subintervals "from 1 to N − 1".
- §2.2 gives B-spline matrices a "bandwidth of BW = σ − 1", reusing $BW$ of Eq. (1); "BW" also
  abbreviates Beam–Warming. Eq. (6) writes $B_{i,\sigma}$ and (B.19) "$L_K=1$" against
  $B_i^\sigma$ and $L_1=1$ elsewhere.
- §4.4 says Fig. 10(c) shows "a coefficient matrix corresponding to a compact differencing
  operator"; the caption calls (c) and (d) the "one-dimensional implicit filter operator".
- §5.4 cites "Figs. 24(c) and 24(d)"; Fig. 24 has only panels (a) and (b).
- **Fig. 25:** the caption reads "(a) over entire top half of cylinder, (b) close-up of backscatter
  region", while the printed panel "a" is the close-up and "b" the full half.
- Eqs. (13) and (16) use $IL$, $JL$, $KL$, $L_x$, $L_y$, $L_z$, which the text never defines.
- Fig. 16 caption prints "course grid" for "coarse grid".

# Notation map

| Sherer & Scott (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N$ (donor points of a 1-D stencil) | $q$ | **$N$ is reserved for the polynomial degree** |
| $\sigma$, $\sigma_{\max}$ (formal order) | $p$ (scheme), order $q$ (explicit interpolation), $p_{\max}=q+b-1$ | **$\sigma$ is the observed convergence rate in the registry**; also the B-spline order (degree $+1$) |
| order annotations 2.01, 5.33, … (Fig. 16a) | $\sigma$ | observed rates |
| $BW$ | $b$ (page-local) | receivers coupled per equation; reused for B-spline bandwidth and Beam–Warming |
| $R_j$ | $\alpha_j$ | donor weights |
| $L_k$ | $\varpi_k$ (page-local) | receiver coefficients, $\varpi_{k_c}=1$ |
| $x_j=j$, $\hat x_k=\delta_k$, $\vec\delta=(\delta_\xi,\delta_\eta,\delta_\zeta)$ | donor points, receiver offsets $\bar s_k$ (in donor spacings from the base point) | generalizes $\mathbf s$ to $[0,q-1]$; **$\delta$ is the Yin–Yang buffer angle in the registry** |
| $J$ (receiver count) | — | **clashes with the Jacobian $J$**, which the paper also uses (Eq. (10)) |
| $\alpha$ (wavenumber), $\alpha_j$ (Lagrange factor in (A.10)) | $\theta$ (page-local); weights $\alpha_{\mathbf j}$ | **$\alpha$ is the angle of attack / interpolation weight in the registry** |
| $r$, $R$ | $r_{\mathrm o}$, $\theta_{\max}/\pi$ (page-local) | $R$ is also the vortex core radius in §5.2 |
| $E_{local}$, $E_{int}$, $E_{opt}$, $\epsilon$, $\delta_C$ | $E_{\mathrm{loc}}$, $E_{\mathrm{int}}$, $E_{\mathrm{opt}}$: local, integrated, optimization error; error reduction factor; stencil centring | page-local |
| receiver, interpolation point; donor | $\mathcal R_k$; donor stencil $\mathcal S_{\mathbf i}$ | |
| two-point fringe | $n_f=2$ | |
| hole points "blanked out" | $\mathcal H_k$ | no mask values printed |
| $(\xi,\eta,\zeta)$, $J$, $\vec U/J$, $\hat F_I$, $\hat F_v$ | $\boldsymbol\xi$, $J$, $\hat{\mathbf q}$, $\hat{\mathbf F}^{\mathrm i}$, $\hat{\mathbf F}^{\mathrm v}$ | strong conservation form, time-invariant mapping |
| $\rho E$ | $E$ | total energy per unit volume |
| $\beta$ | minimum order of the one-sided boundary filters | page-local; **reserved for WENO in the registry** |
| $\alpha_f$ | Padé filter coefficient | page-local |
| $T$ | stages or subiterations per step | also the B-spline knot sequence in App. B |
| 45654, C6, E4F8, $F10_b^{\alpha_f}$ | scheme and filter labels of Gaitonde and Visbal | boundary-to-interior order digits |
| $\Delta$ | nominal grid spacing $h$ | §5 |

# Reference list

48 printed references, numbered [1]–[48], all merged complete into the
[bibliography](/bibliography.md) with `citedby` sherer-2005. Three Sherer works of 2004 take
suffixes in printed order: [23] `sherer-2004`, [44] `sherer-2004-b`, [46] `sherer-2004-c`; [46]
prints no year apart from its report number NASA/CP-2004-212954, from which the year is taken.
Ref. [4] prints the author as "R. Hirsch"; ref. [40] prints "AIAA 32th Fluid Dynamics Meeting".
Both are entered as printed. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-11-02), cited further in chunk 3. This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Isentropic vortex convection](/benchmarks/isentropic-vortex.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Patched (zonal) grids](/definitions/patched-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Donor search](/methods/donor-search.md)
- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
