---
type: Source
title: "Vermeire (2023) — Embedded paired explicit Runge-Kutta schemes"
description: "Adds to each second-order paired explicit Runge–Kutta member a first-order embedded method with one fewer active stage and a slightly smaller optimized stability region, so that the embedded difference detects the stability limit for a PID controller; speedups of 4.95–7.11 over Bogacki–Shampine 3(2) on Navier–Stokes flows."
resource: "doi:10.1016/j.jcp.2023.112159"
source_kind: paper
authors: [Vermeire B.C.]
year: 2023
venue: "J. Comput. Phys. 487:112159"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Journal_of_Computational_Physics_Vermeire_Embedded_paired_explicit_Runge-Kutta_schemes.pdf"
tags: [runge-kutta, explicit, embedded-pair, step-size-control, stability, method-of-lines]
timestamp: 2026-10-19T20:00:00Z
---

# Summary

[Paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)
(P-ERK) families share $s$, $c$ and $b$ across members that differ in
the number $e$ of active stages, and assign members to mesh elements by
stiffness. Before this paper they had no error estimator and needed an
a-priori maximum stable step. The paper adds to each second-order member
with $e$ active stages a first-order
[embedded method](/methods/embedded-runge-kutta-pair.md) with $e-1$ active
stages: $\hat b_s=0$, $\hat b_i=0$ on the inactive stages and
$\hat b_1=1-\sum_{i=2}^{s-1}\hat b_i$. The base tableau has
$c_i=(i-1)/(2(s-1))$ and $b=(0,\dots,0,1)$.

The embedded stability polynomial $\hat P$ is
[optimized](/methods/optimal-stability-polynomial.md), like the base $P$,
for flux-reconstruction DG spectra, but its region is designed to be
slightly smaller than that of $P$. The embedded solution then departs from
the base solution just before the base scheme goes unstable, and the
embedded difference works as a stability-limit detector, not mainly as an
accuracy estimate. Both polynomials have $e-2$ free coefficients, matching
the free entries of $A$ and $\hat b$, which are obtained sequentially with
no nonlinear solve. The ratio $\hat\nu_{\max}/\nu_{\max}$ of maximum stable
CFL numbers goes from about 60 % at few stages to about 93 % at $e=16$.

A PID [step-size controller](/methods/step-size-control.md) with the
Fekete et al. gains, a maximum growth factor of only 1.2 and tolerances
$10^{-4}$, drives the step towards, without exceeding, the base stability
limit. Adaptive P-ERK ($s=16$, members $e\in\{16,8,3\}$ assigned by
minimum edge length) is compared with the Bogacki–Shampine 3(2) pair in
the flux-reconstruction code HORUS on a laminar cylinder ($\mathrm{Re}=150$),
a heaving and pitching NACA 0012 on a deforming mesh ($\mathrm{Re}=1000$) and
a stalled 3D NACA 0020 ($\mathrm{Re}=20\,000$). Force coefficients agree,
and the speedups are 4.95–7.11. The paper has no theorems; the evidence is
numerical. The embedded solutions are not conservative across members,
which the paper accepts because they never advance the solution.

# Version read

The file is the Elsevier version of record (J. Comput. Phys. 487 (2023)
112159; received 22 August 2022, revised 20 March 2023, accepted 15 April
2023, online 25 April 2023), 16 pages, all read. Page 1 matches Crossref
for title, single author, volume, article number and DOI. The supplementary
data mentioned in the paper are not part of the file.

# Key claims

1. A second-order P-ERK member with $e$ active stages ($2\le e\le s$) is given a first-order embedded method with $e-1$ active stages (§3; Conclusions). **Derived**
2. In the general embedded P-ERK tableau (Eq. 15), $c_i=\frac{i-1}{2(s-1)}$ (Eq. 16) and $b=(0,\dots,0,1)$ (Eq. 17); together these "ensure that a second-order scheme will be obtained when using the b weights" (§3). **Derived**
3. Setting $a_{i+1,i}=0$ for $2\le i\le s-e+1$ (Eq. 18) leaves $e$ active stages; the embedded weights satisfy $\hat b_i=0$ for $2\le i\le s-e+1$ (Eq. 19), $\hat b_s=0$ and $\hat b_1=1-\sum_{i=2}^{s-1}\hat b_i$ (Eq. 20). This leaves $e-2$ free parameters in $A$ and $e-2$ in $\hat b$ (§3). **Derived**
4. The base stability polynomial has degree $e$ and the embedded one degree $e-1$; each has $e-2$ free coefficients, $\{\theta_3,\dots,\theta_e\}$ and $\{\hat\theta_2,\dots,\hat\theta_{e-1}\}$ (Eqs. 26–27), matching the free tableau parameters (§4). **Derived**
5. All unknowns in $A$ and $\hat b$ follow from the two prescribed stability polynomials "sequentially without requiring any non-linear solvers" (§3, after Eq. 23). **Derived** (shown for the $s=10$, $e=6$ example, Eqs. 22–23)
6. All members with the same $s$ share $c$ and $b$ and so pair seamlessly, "the same property that is exploited when building IMEX schemes"; $\hat b$ differs between members, so "the embedded schemes will not be conservative", which is acceptable because they only estimate the stability limit and never advance the solution (§3). **Stated**
7. Load imbalance from different active-stage counts per element is handled by METIS multi-constraint partitioning (§3). **Stated**
8. For flux-reconstruction DG with $k=1$–$8$ and $e=3$–$16$, the embedded region is always smaller than the base region. For $k=1$ the optimal embedded region coincides with the base region of the member with one fewer active stage, for all $e$; for higher $k$ and few stages this fails, but the trend returns at larger $e$ (§4, Fig. 1). **Shown**
9. Maximum stable CFL numbers for 1D linear advection ($\nu_{\max}$ / $\hat\nu_{\max}$) grow with $e$ for every $k$: $k=1$: $e=3$ 0.59/0.33, $e=8$ 1.71/1.49, $e=16$ 3.43/3.43; $k=4$, $e=16$: 0.75/0.71; $k=8$: $e=3$ 0.04/0.03, $e=16$ 0.30/0.28 (Table 1). The text's claim that "the value of $\hat\sigma_{max}$ is always slightly smaller than $\sigma_{max}$" (§4) is contradicted by two printed $k=1$ entries (see Printed slips). **Shown**
10. $\hat\nu_{\max}/\nu_{\max}$ is about 60 % at low active-stage counts (depending on $k$) and about 93 % at $e=16$ (§4, Fig. 2). **Shown**
11. Error scaling: $\mathrm{sc}=\mathrm{atol}+\max(\lvert y_n\rvert,\lvert y_{n+1}\rvert)\,\mathrm{rtol}$ (Eqs. 29–30) and $\mathrm{err}=\lVert(y_{n+1}-\hat y_{n+1})/\mathrm{sc}\rVert_\infty$ (Eq. 31); a step is accepted iff $\mathrm{err}\le1$ (Eq. 34) (§5). **Stated**
12. Step update $h_{\mathrm{new}}=h\cdot\min(f_{\max},\max(f_{\min},f_\beta\,\beta_{n+1}))$ (Eq. 32, after Fekete et al.) with the PID factor $\beta_{n+1}=\mathrm{err}_n^{-0.58/p}\,\mathrm{err}_{n-1}^{0.21/p}\,\mathrm{err}_{n-2}^{-0.1/p}$, i.e. $(\beta_1,\beta_2,\beta_3)=(0.58,-0.21,0.1)$ in registry form (Eq. 33) (§5). **Stated**
13. For P-ERK, $f_{\min}=0.1$, $f_{\max}=1.2$, $f_\beta=0.9$ and $\mathrm{atol}=\mathrm{rtol}=10^{-4}$ "were found to be a good combination for detecting the stability limit"; for classical embedded pairs, the Fekete et al. coefficients with tolerances $10^{-3}$ likewise ran close to, without exceeding, the stability limit (§5). **Shown** (from experience; no data printed)
14. P, PI and the explicit Gustafsson controller were also tried; the PID controller with these coefficients gave the fewest rejected steps (§5). **Stated** (no numbers printed)
15. Running at the stability limit is justified because, for advection–diffusion with high-order spatial discretizations, the maximum stable step "often introduces little temporal error relative to the error introduced by the spatial discretization" (§2.2, cited). **Stated**
16. The Bogacki–Shampine 3(2) pair (4 stages, FSAL, 3 evaluations per step) is the baseline because the Heun–Euler pair has "poor stability" for high-order spatial discretizations (§6.1). **Stated**
17. Laminar cylinder (Ma 0.2, $\mathrm{Re}=150$, $k=1$–$5$, $\text{P-ERK}_{16,16,2}$ in the boundary layer and $\text{P-ERK}_{16,3,2}$ in the far field): $C_D$ = 1.234, 1.338, 1.346, 1.345, 1.345 for $k=1$–$5$, identical for both integrators; speedups over Bogacki–Shampine 5.25, 6.39, 6.87, 7.00, 6.68 (§6.1, Table 2). **Shown**
18. Heaving and pitching NACA 0012 ($\mathrm{Re}=1000$, Ma 0.1, deforming mesh, $e=16,8,3$): lift and drag histories nearly indistinguishable from the baseline, mean $C_L$/$C_D$ differ in the third significant digit; speedups 4.95, 5.02, 5.66, 6.53, 7.11 for $k=1$–$5$ (§6.2, Table 3, Figs. 7–8). **Shown**
19. Stalled NACA 0020 ($\mathrm{Re}=20\,000$, Ma 0.2, angle of attack $20^\circ$, 3D, $e=16$ and 3): mean $C_L$ 0.67, 0.68, 0.67, 0.66, 0.64 and $C_D$ 0.38, 0.38, 0.37, 0.36, 0.36 for $k=1$–$5$ against Rosti et al. 0.64/0.35; speedups 5.93, 5.80, 5.73, 6.08, 6.23. The baseline ran only about $10t_c$, restarted from P-ERK, to measure the speedup (§6.3, Table 4). **Shown**
20. Abstract: adaptive embedded P-ERK is "up to seven times less computationally expensive than classical embedded pairs for all cases"; Conclusions: "speedup factors in excess of 7 observed for all considered test cases" (overstated, see Printed slips). **Shown** (as printed)
21. Non-embedded P-ERK gives speedups of 5–10 over classical explicit Runge–Kutta, per the earlier P-ERK papers (§1). **Stated**
22. Future work: embedded pairs for third-order P-ERK, whose "primary challenge" is satisfying the larger number of order conditions for both base and embedded schemes (§7). **Stated**

# Printed slips

1. Eq. 21 prints $\hat b_1=1-\hat b_7-\hat b_8-\hat b_9$, but $\hat b_6$ is a free nonzero weight (it appears in the $z^2$ coefficient $0.2777\hat b_6$ of Eq. 23), so by Eq. 20 $\hat b_1=1-\hat b_6-\hat b_7-\hat b_8-\hat b_9$.
2. Table 1, $k=1$: $e=15$ prints $\sigma_{max}=\hat\sigma_{max}=3.22$ and $e=16$ prints 3.43/3.43, contradicting "the value of $\hat\sigma_{max}$ is always slightly smaller than $\sigma_{max}$" (§4) and Fig. 1. The pattern $\hat\sigma_{max}(e)=\sigma_{max}(e-1)$ stated for $k=1$ would give 3.00 and 3.22, so the last two $k=1$ embedded entries appear shifted.
3. The caption of Table 2 copies that of Table 1 ("Maximum stable time step sizes, σmax and σ̂max for all considered solution polynomial degrees from k = 1 to k = 8 …"), whereas Table 2 holds cylinder $C_D$ and speedups for $k=1$–$5$.
4. Speedup overclaims: the Conclusions' "in excess of 7 … for all considered test cases" against table maxima of 7.00 (Table 2), 7.11 (Table 3) and 6.23 (Table 4). §6.3 quotes "up to 7.11 relative to RKBS" in the NACA 0020 discussion, but 7.11 is the NACA 0012 value.
5. Fig. 2 caption: "active stages ranging from e = 2 to 16", whereas Table 1, Fig. 1 and §4 cover $e=3$ to 16.
6. Tables print the baseline as RKBS$_{4,3,2}$ in the $RK_{s,e,p}$ notation where $p$ is the order (§2.1), but the text calls it a third/second-order pair, higher order than P-ERK; it should be RKBS$_{4,3,3}$.
7. Ref. [7] prints "E. Hairer, H. Wanner"; the second author is G. Wanner.
8. Eq. 33: the exponent normalizer $p$ is not defined in §5 (base order 2 or embedded order 1, a factor 2 apart).
9. Eq. 23: the numerical $z^3$–$z^5$ coefficients depend on values of $a_{7,6},\dots,a_{10,9}$ that are not printed, and the $k$ they belong to is not stated.
10. Typos: "advancemets", "an general formulation", "the based and embedded schemes", "conovective", "solution was them time averaged", "qualatitively", "Quantitive", "Quantiative", "qudrilateral", "Ghoresishi" next to "Ghoreishi", "mesh induced stiff"; the Table 3 $k=1$ baseline row lacks the "-" in the speedup column; stability conditions written as $\Delta t\omega\subseteq S$ for a point.
11. "Re = 1000 with the airfoil chord length c as the reference length number" is garbled; $c$ also denotes the speed of sound (Eq. 35), the chord and the abscissae.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u^n$, $u^{n+1}$, $\hat u^{n+1}$ | $y_n$, $y_{n+1}$, $\hat y_{n+1}$ | |
| $\Delta t$ | $h$ | step size; the source's $h$ is the element size, here $\Delta x$ |
| $u'=\omega u$, $\omega$ | $y'=\lambda y$, $\lambda$ | |
| $z=\omega\Delta t$ | $z=h\lambda$ | |
| $e$ (number of active stages) | $e$ | page-local, not in the registry; as on the [P-ERK](/methods/paired-explicit-runge-kutta.md) page; **collision**: the source also writes $e$ for the vector of ones (Eqs. 9–10), registry $\mathbf 1$ |
| $s$, $A$, $b$, $c$, $\hat b$ | $s$, $A$, $b$, $c$, $\hat b$ | agree; $c=A\mathbf 1$ assumed (Eq. 3) |
| $p$ | $p$ | order (agree); also the undefined normalizer of Eq. 33 |
| $P(z)$, $\hat P(z)$; $P_{e,p}$, $\hat P_{e-1,p}$ | $P(z)$, $\hat P(z)$ | stability polynomials of base and embedded method; subscripts are (degree, order) |
| $\gamma_j$, $\hat\gamma_j$ | $\theta_j$, $\hat\theta_j$ | monomial coefficients; **collision**: registry $\gamma$ is the tree density |
| $S$, $\hat S$ | $\mathcal S$, $\hat{\mathcal S}$ | regions of absolute stability |
| $\sigma_{max}$, $\hat\sigma_{max}$ | $\nu_{\max}$, $\hat\nu_{\max}$ | maximum stable CFL numbers |
| $\alpha$ | — | advection speed; also angle of attack (§6.3) |
| $k$ | $k$ | flux-reconstruction solution degree; page-local; **collision**: the source's PID gains $k_1,k_2,k_3$ are registry $\beta_1,\beta_2,\beta_3$ |
| $A_{tol}$, $R_{tol}$, $sc$ | $\mathrm{atol}$, $\mathrm{rtol}$, — | |
| $err_{n+1}$, $err_n$, $err_{n-1}$ | $\mathrm{err}_n$, $\mathrm{err}_{n-1}$, $\mathrm{err}_{n-2}$ | max norm, not $\lVert\cdot\rVert_{\mathrm{WRMS}}$; index shifted by one |
| $k_1,k_2,k_3=0.58,0.21,0.1$ | $\beta_1,\beta_2,\beta_3=0.58,-0.21,0.1$ | the source writes the middle exponent with a plus sign |
| $f_{min}$, $f_{max}$, $f_\beta$, $\beta_{n+1}$ | — | step-factor limits, safety factor, controller output |
| RKBS | — | Bogacki–Shampine 3(2) pair |

# Reference list

The paper prints 30 references in numbered style ([1]–[30]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. No printed duplicates. Ref. [7] prints the second Hairer–Wanner
author as "H. Wanner" (entered with a note); [18] and [27] print an article
number together with a page range, recorded as article numbers; [1]
Stetter (Springer 1973) is entered as printed ("2 edition"). Same-author
same-year pairs are Vermeire 2019 ([14], [23]) and Pereira 2020 ([18],
[27]). Ref. [6], whose PID gains the paper adopts, is the ingested
[Fekete et al. (2022)](/sources/fekete-2022.md). All items parsed.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Paired explicit Runge–Kutta (P-ERK) methods](/methods/paired-explicit-runge-kutta.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
