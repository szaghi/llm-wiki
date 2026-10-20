---
type: Source
title: "Vermeire & Hedayati Nasab (2021) — Accelerated implicit-explicit Runge-Kutta schemes for locally stiff systems"
description: "Introduces AIMEXs,2, second-order IMEX Runge–Kutta schemes for mesh-induced local stiffness that add explicit stages to a two-stage SDIRK while keeping two implicit solves per step; the added stages are fixed by an optimized stability polynomial, giving explicit steps over five times larger and speedups up to 23."
resource: "doi:10.1016/j.jcp.2020.110022"
source_kind: paper
authors: [Vermeire B.C., Hedayati Nasab S.]
year: 2021
venue: "J. Comput. Phys. 429:110022"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Computational_Physics_Vermeire_Accelerated_implicit-explicit_Runge-Kutta_schemes_for_locally_stiff_systems.pdf"
tags: [imex, optimal-stability-polynomial, diagonally-implicit, locally-stiff, cfd]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper targets **locally stiff** semi-discretizations, where the
stiffness comes from the mesh. A small set of refined elements is
integrated implicitly and the rest explicitly, so the
[IMEX](/methods/imex-runge-kutta.md) split is spatial (element by element),
not an operator split. A cost model shows that the implicit solver
dominates the cost per unit time, while the explicit stability limit sets
the step. Enlarging the explicit stability region without adding implicit
solves therefore pays.

The construction starts from IMEX3,2 (Ascher–Ruuth–Spiteri ARS(2,3,2)): an
L-stable, stiffly accurate two-stage
[SDIRK](/methods/diagonally-implicit-runge-kutta.md) with
$\gamma=(2-\sqrt2)/2$, paired with a three-stage explicit method. AIMEX$s$,2
("accelerated IMEX") inserts stages between the second and the last. In the
implicit tableau the inserted stages only extrapolate the second stage
derivative, so every step needs exactly two implicit solves and the
implicit region sees the original SDIRK. In the explicit tableau each
inserted stage has two nonzero entries, which makes the scheme low-storage
(three stage derivatives) and leaves one free coefficient per stage. With
shared $b$ and $c$, these coefficients are fixed one after another by the
free coefficients of a second-order explicit
[stability polynomial](/definitions/stability-function.md). The polynomial
is optimized with the Ketcheson–Ahmadia bisection
([optimal stability polynomial](/methods/optimal-stability-polynomial.md))
against [von Neumann](/definitions/von-neumann-stability-analysis.md)
spectra of nodal-DG flux reconstruction for linear advection.

With four stages the explicit step is 1.79–2.01 times that of IMEX3,2, and
the gain grows about linearly with $s$, past five at $s=10$. Second-order
convergence is verified on [linear advection](/benchmarks/linear-advection-equation.md)
over a mesh with element-size ratio about $2.5\times10^5$, and on the
[isentropic vortex](/benchmarks/isentropic-vortex.md) with an implicit
refined strip. On laminar SD7003 airfoil flow AIMEX10,2 is up to 23 times
faster than explicit RK3,3 and at least twice as fast as IMEX3,2, with the
same lift and drag. A stalled NACA 0020 implicit LES agrees reasonably with
DNS.

# Version read

The file is the version of record (Elsevier typeset), 23 pages, received 1
Aug 2019, available online 26 Nov 2020, issue year 2021. Title, authors,
volume, article number and DOI on page 1 match Crossref. The `local_file` is
the full-title archive file; the short-titled sibling file
"…_for_locall.pdf" holds a different paper,
[Al Jahdali et al. (2022)](/sources/aljahdali-2022.md). The electronic
supplement with the complete tableaux for $s=4$–10 is cited but not in the
file.

# Key claims

Notation: $(A,b,c)$ explicit and $(\hat A,\hat b,\hat c)$ implicit tableaux
(the registry's $A^{\mathrm E}$, $A^{\mathrm I}$); $\gamma$ the SDIRK
diagonal; $P_{s,2}(z)=\sum_j\theta_jz^j$ the explicit stability polynomial;
$\eta$ the implicit fraction of elements.

1. An IMEX pair with an $s$-stage order-$p$ explicit part and an $\hat s$-stage order-$\hat p$ implicit part is written IMEX$s,p$; coupling at the interface needs $\hat b=b$ and $\hat c=c$ (§2.1, Eqs. 9–10). **Stated**
2. Cost model: with $e$ explicit and $\hat e$ implicit stage evaluations per step, cost $c$, $\hat c$ per element and evaluation, and implicit fraction $\eta=\hat n/(n+\hat n)$, the cost per unit time and element is $\tilde C=[(1-\eta)ec+\eta\hat e\hat c]/h\approx\eta\hat e\hat c/h$ since $\hat c\gg c$ (§2.2, Eqs. 16–18). **Derived**
3. Adding explicit stages to enlarge the stability region without raising $\hat e$ lowers the total cost, provided the implicit solver cost does not grow faster than $h$; its iteration count tends to grow with $h$ (§2.2). **Stated**
4. AIMEX$s$,2 pads the SDIRK with stages between stage 2 and the last and sets $\hat a_{ij}=0$ for $3\le j\le s-1$: only two implicit stage derivatives are computed ($\hat e=2$), and the implicit region recovers the original SDIRK exactly (§3.1, Eqs. 23–25). **Derived**
5. The inserted abscissae are equidistant, $\hat c_i=(1-\gamma)(i-2)/(s-2)+\gamma$ for $3\le i\le s-1$; optimizing them is left to future work (§3.1, Eq. 26). **Stated**
6. The explicit part allows only $a_{i,1}$ and $a_{i,i-1}$ in rows $i\ge4$ and has $c=\hat c$, giving one new unknown per added stage (§3.1, Eqs. 27–29). **Derived**
7. AIMEX schemes are low-storage: three stage derivatives at a time, whatever $s$ (§3.1). **Stated** (follows from the sparsity)
8. Every AIMEX$s$,2 scheme is uniquely determined by a suitable explicit stability polynomial, and its unknowns can be solved for sequentially (§3.1–3.1.1, Eqs. 32–34; Appendix 1 for $s=5$–10). **Derived** (explicit formulas for $s=4$; asserted in general)
9. AIMEX4,2: $P_{4,2}(z)=1+z+\tfrac12z^2+\tfrac12a_{4,3}(\gamma^2+\gamma)z^3+a_{3,2}a_{4,3}\gamma^2z^4$, so $a_{4,3}=2\theta_3/(\gamma+\gamma^2)$ and $a_{3,2}=\theta_4/(a_{4,3}\gamma^2)$ (§3.1.1, Eqs. 32–34). **Derived**; $P_{4,2}$ recomputed from the tableau as $1+zb^\top(I-zA)^{-1}\mathbf 1$ *(compiler check)*
10. Second order follows from the tableau: the $z^2$ coefficient is $2\gamma-\gamma^2=\tfrac12$ for $\gamma=(2-\sqrt2)/2$ (Appendix 1; §3.1.1). **Derived**
11. Maximizing $h$ over $\theta_3,\dots,\theta_s$ is nonconvex for $s>2$; the Ketcheson–Ahmadia form has a convex inner problem and a bisection on $h$, converged to $10^{-12}$ with CVX in Matlab (§3.2, Eqs. 37–39, Algorithm 1). **Stated**
12. For flux reconstruction recovering nodal DG with degree 1–8, the optimal four-stage polynomials give $h_{\mathrm{opt}}=0.8256,0.3756,0.2352,0.1630,0.1206,0.0934,0.0748,0.0614$ (unit element width), 2.01 to 1.84 times the IMEX3,2 maximum step (§4.3, Table 1). **Shown**
13. $h_{\mathrm{opt}}$ grows about linearly with $s$ for every degree, and at $s=10$ the ratio to IMEX3,2 exceeds 5; for large $s$ the gain is larger at higher degree (§4.3, Fig. 1). **Shown**
14. Arbitrarily large steps may be reachable by raising $s$ while keeping two implicit stages (§4.3). **Stated** (extrapolation)
15. 1D linear advection with element-size ratio about $2.5\times10^5$: AIMEX$s$,2, $s=4$–10, converge at second order (observed 1.96–2.00), with errors almost independent of $s$; IMEX3,2 shows orders 3.55, 2.47, 2.19 and smaller errors at small $h$ ($2.80\times10^{-8}$ against $1.03\times10^{-7}$ for AIMEX4,2 at $h=1.25\times10^{-4}$) (§5.1, Table 2). **Shown**
16. Isentropic vortex (Euler), AIMEX10,2 optimized for degree 6, refined strip implicit (edge ratio about 240): $L_2$ density errors $1.86\times10^{-6}$ to $3.02\times10^{-8}$ for $h=1/100$ to $1/800$, orders 1.97, 1.99, 1.98 (§5.2, Table 3). **Shown**
17. SD7003 airfoil ($Re_c=10{,}000$, Ma 0.2): AIMEX10,2 reaches speedups up to 23 over explicit RK3,3 and beats IMEX3,2 by at least a factor two for degrees 1–4 (§5.3, Fig. 6). **Shown**
18. Raising the implicit fraction beyond $\eta\approx0.2$ lowers the peak speedup, because the implicit solver cost grows faster than the step gain (§5.3, Fig. 6). **Shown**
19. At $\eta\approx0.1$ and 75% of the maximum stable step, AIMEX10,2 and IMEX3,2 give the same $C_D$, $C_L$ to the printed digits except $C_D$ at degree 2 (0.0492 against 0.0493), in agreement with the literature; no degradation is visible at the implicit/explicit interface (§5.3, Table 4, Fig. 5). **Shown**
20. Stalled NACA 0020 implicit LES ($Re_c=20{,}000$, $20^\circ$), AIMEX10,2, degrees 1–3: $C_D=0.34,0.34,0.33$ and $C_L=0.59,0.61,0.59$ against DNS 0.35 and 0.64, with under 3% of the DNS degrees of freedom (§5.4, Table 5). **Shown**
21. With more than three stages AIMEX needs fewer implicit solves than a conventional IMEX scheme with as many stages (§1). **Stated**
22. Future work: higher-order AIMEX, comparison with IMEX-BDF, embedded AIMEX pairs for error estimation (§6). **Stated**

The design treats only the explicit polynomial on the explicit-region
spectrum. Linear stability of the coupled scheme at the implicit/explicit
interface is not analyzed; claim 19's "no degradation" is visual. No
hardware, core counts or wall-clock times are printed; speedups are ratios.

# Printed slips

- Eq. 26: range printed "$i\le 3\le s-1$" for $3\le i\le s-1$.
- §3.2: "we converge the bisection method in Algorithm 2"; there is only Algorithm 1, which tests $r_{p,s}$ while Eqs. 38–39 define $r_{s,p}$.
- §1 announces "In Sect. 4 we optimize AIMEX schemes", but §4 and §5 are both headed "Numerical results"; §3.1 says "Chapter 2" for Section 2.
- $\omega$ is the test-equation eigenvalue in Eq. 11 but the temporal frequency of $u\propto e^{I(\theta x-\omega t)}$ in Eq. 53, so the semi-discrete eigenvalue is $-I\omega^\delta$; Eq. 37 and §4.2 still place $\omega^\delta$ directly in $P_{s,p}(\Delta t\,\omega^\delta)$. The rotation is not shown.
- The abstract says "over a factor of 20", §5.3 "up to 23".
- Ref. [2] prints the second author of Hairer–Wanner as "H. Wanner"; ref. [20] is cited as "Lopez et al." (§5.3) and "Lopez-Morales et al." (Table 4), while the list prints "M.R. López".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf A$, $\mathbf b$, $\mathbf c$ | $A^{\mathrm E}$, $b^{\mathrm E}$, $c^{\mathrm E}$ | explicit tableau |
| $\hat{\mathbf A}$, $\hat{\mathbf b}$, $\hat{\mathbf c}$ | $A^{\mathrm I}$, $b^{\mathrm I}$, $c^{\mathrm I}$ | implicit tableau; **collision** with the embedded $\hat b$, $\hat p$ |
| $\mathbf e$ | $\mathbf 1$ | vector of ones; **collision** with the evaluation counts $e$, $\hat e$ |
| $u^n$, $\Delta t$ | $y_n$, $h$ | |
| $u'=\omega u$, $z=\omega\Delta t$ | $y'=\lambda y$, $z=h\lambda$ | $\omega$ also the frequency of the von Neumann ansatz |
| $P_{s,p}(z)$, $\gamma_j$ | $P(z)$, $\theta_j$ | stability polynomial and its coefficients |
| $\gamma$ | same (page-local) | SDIRK diagonal $(2-\sqrt2)/2$; **collision** with the polynomial coefficients $\gamma_j$ and the ratio of specific heats 1.4 in the source, and with the registry tree density |
| $S$ | $\mathcal S$ | stability region |
| $\boldsymbol\omega^\delta$, $\omega^\delta$ | $\lambda$ (set of semi-discrete eigenvalues) | |
| $s$, $\hat s$, $p$, $\hat p$ | same | explicit/implicit stages and orders |
| $e$, $\hat e$, $c$, $\hat c$, $n$, $\hat n$, $C$, $\tilde C$ | same (page-local) | evaluation counts, costs, element counts; **collision**: scalar $c$ also the abscissae and the chord |
| $\eta$ | same (page-local) | implicit fraction of elements; **collision** with the entropy $\eta(y)$ |
| $k$ | same (page-local) | flux-reconstruction polynomial degree; **collision** with the multistep $k$ |
| $\sigma$ | same (page-local) | $L_2$ error; **collision** with the tree symmetry |
| $I$ | $i$ | imaginary unit |

# Reference list

The paper prints 29 references in numbered style ([1]–[29]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. Same-author same-year works are told apart by suffix: [22]/[23]
(Balay et al. 2018, PETSc web page and users manual revision 3.9) are
`balay-2018-b` and `balay-2018-c`, because `balay-2018` holds revision 3.10,
and [7]/[25] (Vermeire 2015) are `vermeire-2015` and `vermeire-2015-b`. [10]
(Matlab) has a corporate author (`mathworks-2016`); [11] is CVX, dated March
2014, merged into the existing version-2.1 entry `grant-2014` and distinct
from the CVX 2013 entry `grant-2013`. [9] prints no
conference name and [26] no institution. No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Von Neumann (Fourier) stability analysis of fully discrete schemes](/definitions/von-neumann-stability-analysis.md)
