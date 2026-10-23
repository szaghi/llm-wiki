---
type: Source
title: "Doehring et al. (2024) — Many-Stage Optimal Stabilized Runge–Kutta Methods for Hyperbolic Partial Differential Equations"
description: "Parametrizes explicit stability polynomials by the roots of (P−1)/z, which lie on the stability boundary, and optimizes them from an equal-arc-length guess on the spectrum's convex hull, reaching degree 128; builds 2N-storage many-stage methods and analyses their internal stability and missing SSP property."
resource: "doi:10.1007/s10915-024-02478-5"
source_kind: paper
authors: [Doehring D., Gassner G.J., Torrilhon M.]
year: 2024
venue: "J. Sci. Comput. 99:28"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Journal_of_Scientific_Computing_Doehring_Many-Stage_Optimal_Stabilized_RungeKutta_Methods_for_Hyperbo.pdf"
tags: [runge-kutta, explicit, stability, low-storage, ssp, method-of-lines]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper builds [optimal stability polynomials](/methods/optimal-stability-polynomial.md)
of degree above 100 for explicit
[stabilized Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md)
applied to method-of-lines discretizations of hyperbolic PDEs, whose
Jacobian spectra fill a two-dimensional region of the left half-plane. The
Ketcheson–Ahmadia convex formulation optimizes the monomial coefficients
$\theta_j\sim1/j!$ and so stalls at about 16–20 stages in double precision.
The authors instead write every polynomial of linear order at least 1 as
$P(z)=1+z\prod_{j=1}^{s-1}(1-z/\tilde r_j)$ and optimize the roots
$\tilde r_j$, the *pseudo-extrema*, which lie on the stability boundary
$\lvert P\rvert=1$. For the proven optimal first- and second-order disk
polynomials the pseudo-extrema are the Chebyshev extreme points projected
onto the circle, equally spaced in arc length (Theorems 1–2).

Assuming approximately equal arc-length spacing on the convex hull of the
spectrum for strictly convex spectra gives the initial guess. Algorithm 1
scales the Ketcheson–Ahmadia step at $s=16$ linearly in $s$, parametrizes
each pseudo-extremum by its real part on a piecewise-linear hull
interpolant, then adds small imaginary corrections. Degree-$s/2$ solutions
seed degree-$s$ problems. Feasibility problems solved with Ipopt and
algorithmic derivatives give polynomials up to degree 128 (orders 1–3) in
seconds to minutes for DGSEM spectra of Burgers, shallow water, ideal MHD
and 2D Euler, and nonconvex spectra are handled through their convex hull.

The factorized polynomial yields 2N-storage
([low-storage](/methods/low-storage-runge-kutta.md)) many-stage methods in
modified Shu–Osher form, built from forward Euler steps and two-stage
submethods. [Internal stability](/definitions/internal-stability.md), the
growth of round-off through the stages, is the main obstacle; minimizing
$\lVert\beta\rVert_1$, allowing negative $\beta$ and grouping near-imaginary
roots with the most negative ones lowers the internal amplification measure
from $10^{22}$ to $10^{9}$. The methods have SSP coefficient $\mathcal C=0$
(see [SSP methods](/methods/strong-stability-preserving-runge-kutta.md)).
Linear tests reach design order at the full scaled step except the largest
$s$; nonlinear tests need CFL fractions 0.28–0.79, which the authors
attribute to the missing SSP property.

# Version read

The file is the arXiv preprint arXiv:2402.12140v4 [math.NA], 18 March 2024
(footer: "Preprint submitted to Springer Journal of Scientific Computing,
March 19, 2024"), 37 pages, all read. It points to the published DOI. The
archive filename says "Crossref_Journal_of_Scientific_Computing" but the
file is not the typeset version of record. Page 1 prints "Runge-Kutta"
with a hyphen where the published title has an en dash; authors match
Crossref. Page, equation and table numbers cited here are those of arXiv
v4. Code: OSPREI (Zenodo 10.5281/zenodo.8009493); spectra from Trixi.jl.

# Key claims

1. The monomial-coefficient convex formulation of Ketcheson–Ahmadia is limited in double precision to about 16–20 stages for general spectra, because $\theta_j\sim1/j!$; earlier monomial-based optimizations reached degrees 14, 7 and 8 (§1, §2.1.1). **Stated**
2. Every polynomial of at least first linear order can be written $P(z)=1+z\tilde P_{s-1}(z)$ with $\tilde P_{s-1}=\prod_{j=1}^{s-1}(1-z/\tilde r_j)$; the roots $\tilde r_j$ (pseudo-extrema) all lie on $\partial\mathcal S$, since $\lvert P(\tilde r_j)\rvert=1$ (§2.2, Eqs. 2.10–2.11). **Proved** (one-line argument)
3. Theorem 1: the $s-1$ pseudo-extrema of the optimal first-order disk polynomial $(1+z/s)^s$ are the positive Chebyshev extreme points ($x_j\ne0$) of $T_s(1+z/s)$ projected onto the circle of radius $s$ centred at $-s$ (§3.1.1, Eqs. 3.4–3.10). **Proved**
4. Theorem 2: the same holds for the optimal second-order disk polynomial $\frac{s-1}{s}\big(1+\frac{z}{s-1}\big)^s+\frac1s$ (Eq. 3.11), with the circle of radius $s-1$ centred at $-(s-1)$ (§3.1.2). **Proved** ("analogous to proof of Theorem 1")
5. The second-order disk polynomial equals second-order RKC with infinite damping; it can be written as a sequence of forward Euler steps and so is SSP with optimal SSP coefficient (§3.1.2). **Stated**
6. For even $s$ there is one real pseudo-extremum and $s-2$ complex-conjugate ones; for odd $s$ all $s-1$ are complex-conjugate (Remarks 1–2). The same pattern is observed for every strictly convex spectrum tried (§4.1, Fig. 2). **Proved** for the disk, **Shown** for the others
7. Central assumption: for strictly convex spectra the pseudo-extrema of optimal polynomials are spaced approximately equally in arc length on the convex hull of the spectrum, supported by degree-16, order-2 polynomials optimized with Ketcheson–Ahmadia for DGSEM spectra of Burgers, 1D shallow water, 1D ideal MHD and 2D Euler (§3.2, Fig. 2). **Shown** (heuristic)
8. Even-degree polynomials always (in every spectrum considered) select the left real endpoint of the spectrum as a pseudo-extremum, and doubling $s$ reproduces every second pseudo-extremum, $\tilde r^{(2s)}_{2j-1}\approx2\tilde r^{(s)}_j$ after linear step scaling (§4.5, Fig. 3). **Shown**
9. The linear order conditions in the pseudo-extrema follow from Vieta's formulas; order 2 requires $\tfrac12=-\sum_j1/\tilde r_j$, and in general there are $p-1$ equality constraints (Eq. 4.3) (§4.4). **Derived**
10. Step scaling: real-axis (parabolic) inclusion grows like $s^2$; one-sided imaginary-axis inclusion with real coefficients is bounded by $s-1$, with the tighter limit $\sqrt{(s-1)^2-1}$ conjectured and proved for special cases; optimal disks scale linearly. The paper assumes $h_{s,p}=(s/s_{\mathrm{Ref}})\,h_{s_{\mathrm{Ref}},p}$ for general spectra, which gives no per-stage gain once reached (§4.3, Eq. 4.1). **Stated**
11. Algorithm 1 costs linear time in the number of constraints and quadratic time in the number of unknowns $s/2$ (even $s$) (§5.3). Section 6 item 4 instead speaks of "quadratic scaling in the number of constraints" (see Printed slips). **Stated**
12. Supplying the convex hull plus a small subset of eigenvalues usually suffices; the constraints must outnumber the pseudo-extrema, or roots can sit exactly on eigenvalues and allow unbounded steps (§5.3). **Stated**
13. Finite-difference derivatives (Matlab fmincon) failed to find the optimum; Ipopt with exact algorithmic derivatives (dco/c++) succeeded, with constraint-violation tolerance $10^{-16}$ (§5.3). **Stated**
14. Burgers spectrum (129 constraints): degrees 32, 64 and 128, orders 1–3, obtained; the $s=128$ feasibility runtimes are 9.383 s / 8.845 s / 8.549 s (orders 1/2/3), against 15.5 s for $s=16$ with Ketcheson–Ahmadia; cumulative times 26.9 / 27.9 / 27.1 s on an Intel i7-12800H laptop (§6, Table 1). **Shown**
15. Shallow water (117 constraints): $s=30,60,120$, totals 30.687 s (order 1) and 28.726 s (order 2). 1D MHD (252 constraints): $s=28,56,112$, the $s=112$ runs taking 94.433 s and 98.377 s. 2D Euler (717 constraints): $s=26,52,104$, totals 2.456 min and 8.55 min (§6). **Shown**
16. With the convex-hull ansatz on nonconvex spectra, Burgers with Riemann data reaches the linearly scaled optimal step for $s=30,60,120$; the isentropic-vortex Euler spectrum reaches 97.9 % of it for $s=28$ and the full value for $s=56,112$ (§8, Figs. 6–7). **Shown**
17. Many-stage methods are built in modified Shu–Osher form as products of forward Euler steps (real roots) and two-stage low-storage submethods (conjugate pairs), with real time steps only (§9, Eqs. 9.1–9.8). **Derived**
18. Internal stability "seems to be the major difficulty in realizing the maximum timestep" for many-stage methods. The measure is $\widetilde{\mathcal M}=\max_{z\in\mathcal S}\sum_{k=2}^{s+1}\lvert Q_k(z)\rvert$, and $\widetilde{\mathcal M}\cdot10^{-15}$ is compared with $h^{p+1}$ (§9, §9.1, Eqs. 9.10–9.12). **Stated** (estimate from Ketcheson–Lóczi–Parsani)
19. Heuristic: minimize $\lVert\beta^{(j)}_k\rVert_1$ of each two-stage submethod, allow negative $\beta$, and group near-imaginary pseudo-extrema ($\operatorname{Re}\tilde r_j>-0.5$) with those of largest $\lvert\operatorname{Re}\tilde r_j\rvert$ (the "generalized Lebedev idea"). For the degree-104 advection polynomial, $\widetilde{\mathcal M}$ is $2.39\cdot10^{22}$ (no grouping, $\beta\ge0$), $2.19\cdot10^{22}$ (no grouping, $\beta\in\mathbb R$), $7.54\cdot10^{16}$ (grouping, $\beta\ge0$) and $1.63\cdot10^{9}$ (grouping, $\beta\in\mathbb R$) (§9.2–9.3, Table 2). **Shown**
20. The constructed methods have SSP coefficient $\mathcal C=\min\alpha_{k,l}/\beta_{k,l}=0$, because $\alpha_{s+1,s}=0$ and $\beta_{s+1,s}=1$; no $h>0$ guarantees monotonicity, and negative $\beta$ would need special treatment. Many-stage SSP construction is left open (§9.4). **Derived**
21. 1D advection, DGSEM degree 3, 512 cells, $t_f=100$: third-order methods with $s=26,52,104$ run at the full scaled step ($h=5.72\cdot10^{-2},1.14\cdot10^{-1},2.29\cdot10^{-1}$; 1748, 874, 437 steps), with $\widetilde{\mathcal M}\cdot10^{-15}=3.59\cdot10^{-12},1.46\cdot10^{-9},5.39\cdot10^{-5}$ below $h^4=1.07\cdot10^{-5},1.72\cdot10^{-4},2.75\cdot10^{-3}$. Third order is observed in $L^\infty$ and weighted $L^1$; the error constant grows with $s$ (§10.1.1, Table 3, Fig. 8). **Shown**
22. 2D linearized Euler with a manufactured solution, DGSEM degree 4, $64^2$ elements, $t_f=10.5$ (reference step $h_{16,2}\approx4.53\cdot10^{-2}$ from an $8^2$ mesh): $s=32,64,128$ need CFL fractions 1.0, 0.96, 0.81. At CFL 1 the $s=128$ run is unstable with $\widetilde{\mathcal M}\cdot10^{-15}\approx7.60\cdot10^{-2}$ above $h^3$, attributed to internal stability; the $s=64$ reduction is attributed to the coarse-mesh spectrum. Second order in $L^\infty$ (§10.1.2, Table 4, Fig. 9). **Shown**
23. Burgers with a source term (manufactured $u=2+\sin2\pi(x-t)$), DGSEM degree 3, 256 elements, $t_f=5$: $s=28,56,112$ need CFL fractions 0.72, 0.69, 0.28, and the total variation grows ($e_{\mathrm{TV}}=1.30\cdot10^{-2},5.18\cdot10^{-2},6.09\cdot10^{-3}$). Since $\widetilde{\mathcal M}\cdot10^{-15}$ is four orders below $h^3$ for $s=28$, the restriction is attributed to the missing SSP property, not to round-off (§10.2.1, Table 5). **Shown** (attribution argued)
24. Ketcheson's third-order SSP method with $s=n^2=225$ stages has a similar $\widetilde{\mathcal M}\cdot10^{-15}\approx2.13\cdot10^{-13}$ against $h^4\approx5.42\cdot10^{-8}$ but $e_{\mathrm{TV}}\equiv0$. Spurious oscillations of the non-SSP schemes can create amplifying modes: at $t=0.5$, for $s=28$, an eigenvalue has $\operatorname{Re}\lambda=8.57\cdot10^{-12}$ (§10.2.1). **Shown**
25. Burgers converges at second order in $L^\infty$ once oscillations vanish ($h\le\tfrac14h_{s,2}$), and in weighted $L^1$ for every step (Fig. 10). **Shown**
26. Isentropic vortex, DGSEM degree 6, $64^2$ elements, HLLC, $t_f=20$: $s=30,60,120$ need CFL fractions 0.79, 0.65, 0.40 ($h=5.92\cdot10^{-2},9.75\cdot10^{-2},1.20\cdot10^{-1}$), again attributed to the missing SSP property; second order in $L^\infty$ of density until the spatial error dominates (§10.2.2, Table 6, Fig. 11). **Shown**
27. Conclusion: for nonlinear problems the missing SSP property "spoils the effectiveness of the very high-stage methods"; methods with up to about 64 stages are promising and "allow an increase of the characteristic speeds in a simulation by a factor of four at a constant timestep compared to schemes constructed using a monomials-based approach" (§11). **Stated**
28. The intended main use is many-stage members of paired explicit Runge–Kutta (P-ERK) families, partitioned methods with consistency and conservation that "are not trivially satisfied by other classical multirate methods", previously limited to 16 stages by the monomial approach; the application is left for future work (§1, §4.3, §9). **Stated**

# Printed slips

- Table 5, $s=112$ row: the printed $h=3.99\cdot10^{-3}$ conflicts with the same row's 876 steps and $h^3=1.86\cdot10^{-7}$ (both give $h\approx5.71\cdot10^{-3}$) and with CFL 0.28 (from the $s=28$ row, $h_{112,2}=2.04\cdot10^{-2}$, and $0.28$ times it is $5.71\cdot10^{-3}$). Three entries agree on $\approx5.71\cdot10^{-3}$.
- §10.1.2, p. 24: "128 stage method with CFL = 1.0 … $\widetilde{\mathcal M}\cdot10^{-15}\approx7.60\cdot10^{-2}$ while $\Delta t^3\approx9.29\cdot10^{-4}$". At CFL 1, $h=4.53\cdot10^{-2}$ and $h^3=9.30\cdot10^{-5}$, consistent with Table 4; the printed value is one decade off. The conclusion holds either way.
- Eq. 9.5 prints $\beta_{S+1}=(0\ \dots\ 0\ z)$ with the variable $z$ as a coefficient; §9.4 states $\beta_{S+1,S}=1$.
- Eq. 9.6a lacks the factor $\Delta t$, which Eq. 9.6b has; Eq. 9.6b evaluates $F(U_{k-1})$ where $F(Y_{k-1})$ is meant.
- Eq. 9.9 uses $\alpha_{j,l}$ inside a sum over $l$ for stage $k$ (should be $\alpha_{k,l}$); Eq. 9.10 writes $\lVert Q_j(z)\rVert$ with summation index $k$.
- §9.2–9.3 and Table 2 use "the 104 degree, second order accurate stability polynomial optimized for the scalar advection equation (see Section 10.1.1)", but §10.1.1 uses third-order methods; which polynomial Table 2 refers to is unclear.
- §10.1.1: "$\Delta_{16,3}\approx3.53\cdot10^{-2}$" lacks the $t$.
- §8 item 1: Riemann data printed as $u_0=1.5$ for $x<0.5$ and $0.5$ for $x\ge0$; the conditions overlap, and the jump is presumably at 0.5.
- Appendix A, p. 29: "the 'outer' roots $\tilde r_0=-2S^2$ and $\tilde r_{S/2}=0$"; by Eq. A.5, $\tilde r_0=0$ and $\tilde r_{S/2}=-2S^2$, labels swapped.
- The Fig. 7 caption ("Collection of strictly convex spectra …") is copied, while Fig. 7 shows the nonconvex spectra of §8; the Fig. 6 caption says "nonconvex convex spectra".
- §9.2 says "values of $\mathcal M$" while Table 2 reports $\widetilde{\mathcal M}$.
- §6 item 4 ("quadratic scaling in the number of constraints") contradicts §5.3 (linear in constraints, quadratic in unknowns).
- Ref. [35] (Ketcheson–Ahmadia) prints year 2013 with a DOI encoding 2012 (CAMCoS vol. 7 is 2012).
- Refs. [37] and [65] are the same work (Schlottke-Lakemper et al., J. Comput. Phys. 442:110467, 2021), printed twice.
- Ref. [89] has a truncated title; ref. [6] prints the Hairer–Wanner authors in reversed order.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U'=F(U)$, $U_n$ | $y'=f(y)$, $y_n$ | method-of-lines system |
| $J=\partial F/\partial U$, $\sigma(J)$, $\lambda^{(m)}$ | $J$, its spectrum, $\lambda$ | agree |
| $\Delta t$ | $h$ | |
| $S$ | $s$ | number of stages = polynomial degree |
| $p$ | $p$ | **linear** order ($\theta_j=1/j!$, $j\le p$); nonlinear order 2 is automatic for $p=2$ |
| $R(z)$, $P_S(z;\alpha)$, $P_{S,p}$ | $R(z)$, $P(z)$ | |
| $\alpha_j$ | $\theta_j$ | monomial coefficients; **collision** with the Shu–Osher $\alpha_{k,l}$ in the source |
| $\mathcal S$, $\partial\mathcal S$ | $\mathcal S$, $\partial\mathcal S$ | agree |
| $\tilde r_j$, $\tilde P_{S-1}$ | — | pseudo-extrema and the factor $(P-1)/z$; page-local |
| $T_S$ | $T_s$ | Chebyshev polynomial of the first kind; page-local; **collides** with the tree set $T$ and the time slices $T_j$ |
| $\Delta t_{S,p}$, $\Delta t^\star_{S,p}$, $S_{\mathrm{Ref}}$ | $h_{s,p}$, $h^\star_{s,p}$, $s_{\mathrm{Ref}}$ | linearly scaled and optimal steps; $s_{\mathrm{Ref}}=16$ |
| $\widetilde M$ | — | number of stability constraints; **collision** with the registry mass matrix $M$ |
| $\varepsilon$ | — | imaginary-correction bound (0.02); **collision** with the registry stiffness parameter $\varepsilon$ |
| $\alpha_{k,l}$, $\beta_{k,l}$, $v_k$, $Y_k$ | $\alpha_{ij}$, $\beta_{ij}$, —, $Y_i$ | modified Shu–Osher form, $k=1,\dots,S+1$ |
| $c$ (§9.4, Eq. 9.14) | $\mathcal C$ | SSP coefficient; **collision**: the source's $c$ is also the abscissa vector in §9 |
| $Q_k(z)$, $\widetilde{\mathcal M}$ | — | internal stability polynomials and summed internal amplification; page-local |
| $e_k$ | — | round-off perturbation of stage $k$ |
| CFL | — | fraction of the scaled step $h_{s,p}$ actually used, not the Courant number $\nu$ |
| $e_{\mathrm{TV}}$ | — | total-variation increase |

# Reference list

The paper prints 98 references in numbered style ([1]–[98]), ordered by
first citation. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. Refs. [37] and
[65] are a printed duplicate of one work (Schlottke-Lakemper et al. 2021)
and are folded into one entry, so the 98 printed items give 97 entries.
Ref. [34] prints the first author as "S. H. Nasab" (Hedayati Nasab; an
AIAA SciTech 2022 paper keyed `hedayatinasab-2022-b`); [35] (Ketcheson &
Ahmadia) prints year 2013 with a 2012 DOI and is merged into
`ketcheson-2012`; [6] prints the Hairer–Wanner authors reversed and is
merged into `hairer-1996`; [44] is the ingested
[Vermeire (2023)](/sources/vermeire-2023.md); [46] is a chapter with no book title;
[89] has a truncated title; [4] and [11] print irregular Russian venues;
several items print a URL in an "arXiv:" field; [66] Trixi.jl, [75] an
Ipopt issue and [77] OSPREI are software or web items. All items parsed.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Internal stability of explicit Runge–Kutta methods](/definitions/internal-stability.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Paired explicit Runge–Kutta (P-ERK) methods](/methods/paired-explicit-runge-kutta.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping](/methods/stabilized-explicit-runge-kutta.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Trixi.jl](/software/trixi-jl.md)
