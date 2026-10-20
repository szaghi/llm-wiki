---
type: Source
title: "Hedayati Nasab & Vermeire (2022) — Third-order Paired Explicit Runge-Kutta schemes for stiff systems of equations"
description: "Extends paired explicit Runge–Kutta (P-ERK) families to third order with a three-register tableau of shared abscissae and weights, optimizes the members' stability polynomials for flux-reconstruction DG spectra, and reports wall-clock speedups of 4.06–4.51 over RK3,3 on compressible Navier–Stokes problems."
resource: "doi:10.1016/j.jcp.2022.111470"
source_kind: paper
authors: [Hedayati Nasab S., Vermeire B.C.]
year: 2022
venue: "J. Comput. Phys. 468:111470"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Computational_Physics_Hedayati_Third-order_Paired_Explicit_Runge-Kutta_schemes_for_stiff_sy.pdf"
tags: [runge-kutta, explicit, stability, multirate, method-of-lines, low-storage]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

A [paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)
(P-ERK) family is a set of explicit Runge–Kutta tableaux with the same
number of stages $s$, the same abscissae $c$ and the same weights $b$. The
members differ in the number $e$ of *active* stages, the stages whose
right-hand side is evaluated. Members with large $e$ have large stability
regions and are assigned to the stiff (small-element) part of a
method-of-lines mesh; members with small $e$ run elsewhere at lower cost,
all with one global step $h$. Vermeire (2019) built the second-order
family; this paper builds the third-order one, $\text{P-ERK}_{s,e,3}$.

The tableau is nonzero only in the first column and the first subdiagonal
of $A$, and $b$ is nonzero only in its last two entries, so only three
stage derivatives are held in memory whatever $s$ is (a
[low-storage](/methods/low-storage-runge-kutta.md) property). Setting
$a_{i,i-1}=0$ for $2<i<s-e+3$ deactivates stages. With $c_s=1$ the four
third-order [order conditions](/results/runge-kutta-order-conditions.md)
fix $b_{s-1}=3/4$, $b_s=1/4$, $c_{s-1}=1/3$ and
$c_{s-2}=(2-a_{s,s-1})/(9a_{s-1,s-2})$. The $e-3$ free coefficients of each
member's degree-$e$ stability polynomial are chosen by the Ketcheson–Ahmadia
[optimal stability polynomial](/methods/optimal-stability-polynomial.md)
method for 1D flux-reconstruction DG spectra ($k=0$–$8$, $e=3$–$16$). The
paper argues from the partitioned Runge–Kutta conditions that shared $b$
and $c$ keep any spatial mix of members third order and conservative.

Each member $\text{P-ERK}_{16,e,3}$ and a random spatial mix of all
members reach observed order 2.98–3.00 on the
[isentropic vortex](/benchmarks/isentropic-vortex.md). With five members
($e=3,4,8,12,16$), laminar and turbulent SD7003 airfoil flows and the
HiOCFD5 tandem spheres run at 7.28–8.21 times the RK3,3 step, with
wall-clock speedups of 4.06–4.51 and unchanged force coefficients. The
tableau coefficients are not printed, and how $c_{s-2}$ is kept equal
across members is not stated.

# Version read

The file is the Elsevier version of record (J. Comput. Phys. 468 (2022)
111470; received 14 July 2021, revised 5 July 2022, accepted 8 July 2022,
online 18 July 2022), 24 pages, all read. Page 1 matches Crossref for
title, authors, volume, article number and DOI. The archive filename
shortens the surname "Hedayati Nasab" to "Hedayati". The supplementary
material announced in the paper is not part of the file, and the scheme
coefficients are not printed.

# Key claims

1. P-ERK schemes, second order in Vermeire (2019), are extended to a third-order family $\text{P-ERK}_{s,e,3}$ with $s>3$ stages and $3\le e\le s$ active stages per member (§3.1, Abstract). **Derived**
2. The sparsity $a_{ij}=0$ for $j>1$, $i>j+1$, and $b_i=0$ for $i<s-1$ (Eqs. 19–20) means only three stage derivatives must be stored at once, regardless of $s$ (§3.1, Eq. 21). **Derived**
3. Setting $a_{i,i-1}=0$ for $2<i<s-e+3$ (Eq. 22) reduces a member to $e$ right-hand-side evaluations (§3.1, Eqs. 22–23). **Derived**
4. With $c_s=1$, the conditions $b^\top\mathbf 1=1$, $b^\top c=1/2$, $b^\top c^2=1/3$ give $b_{s-1}=3/4$, $b_s=1/4$, $c_{s-1}=1/3$; the condition $b^\top Ac=1/6$ gives $c_{s-2}=\dfrac{2-a_{s,s-1}}{9a_{s-1,s-2}}$ (§3.1, Eqs. 26–28). **Derived**
5. The general $\text{P-ERK}_{s,e,3}$ tableau is Eq. 29. Its stability polynomial (Eq. 30) has degree $e$, and its $z^3$ coefficient equals $1/6$ by Eq. 28 (§3.1). **Derived**
6. Because all members share $c$ (Eq. 38) and $b$ (Eq. 39), the third-order partitioned Runge–Kutta conditions (31)–(37) reduce to the four classical conditions per member, so any combination of members is third order (§3.2). **Derived** (by this reduction only)
7. Equal $b$ and $c$ are said to make P-ERK schemes "consistent and conservative", citing Hundsdorfer, Ketcheson & Savostianov (§3.2). **Stated**
8. The $e-3$ free coefficients $\theta_4,\dots,\theta_e$ of $P(z)$ are optimized by the Ketcheson–Ahmadia formulation: bisection on $h$ (Algorithm 1) around a convex minimax subproblem (Problem 2), solved with CVX in Matlab (§3.3). **Stated**
9. For flux-reconstruction DG with $k=0$–$8$, $h_{\mathrm{opt}}$ grows about linearly with $e$ (Fig. 2a), and $h_{\mathrm{opt}}/e$ increases monotonically up to $e=16$ for every $k$ (Table 1). Examples: $k=0$, 0.418806 ($e=3$) to 0.853547 ($e=16$); $k=4$, 0.029895 to 0.046618; $k=8$, 0.011122 to 0.018364 (§4.2, Table 1). **Shown**
10. For each member of the $s=16$ family, the optimal polynomial together with Eq. 28 forms a nonlinear system whose solution gives the tableau coefficients (§4.2). **Stated** (coefficients not printed)
11. Each member $\text{P-ERK}_{16,e,3}$, $e=3,\dots,16$ (14 schemes), attains observed order 2.98–3.00 on the isentropic vortex (§5.1, Fig. 4, Table 2). **Shown**
12. A random spatial distribution of all members (Fig. 3b) also attains third order, observed 2.98–3.00 (§5.1, Table 2). **Shown**
13. Members with more active stages have lower error at a given $h$: at $h=2.5\times10^{-3}$, $e=3$ gives $6.7526\times10^{-8}$, $e=4$ gives $3.6012\times10^{-8}$ and $e=10$ gives $5.0295\times10^{-10}$ (§5.1, Table 2). **Shown**
14. Laminar SD7003 ($\mathrm{Re}_c=10\,000$, Ma 0.2, $\alpha=4^\circ$, 17 602 quadratic quadrilaterals, five members, on average 4.89 active stages per element): step ratios to RK3,3 of 7.59/7.99/7.78/8.02 and speedups of 4.43/4.51/4.39/4.47 for $k=1/2/3/4$; $C_L$ and $C_D$ nearly identical to RK3,3 (§5.2, Table 3). **Shown**
15. No artefacts appear at the interfaces between P-ERK levels in the vorticity contours (§5.2, Fig. 7; §5.3, Fig. 10). **Shown** (qualitative)
16. Turbulent SD7003 ($\mathrm{Re}_c=60\,000$, Ma 0.1, $\alpha=8^\circ$, 60 720 quadratic hexahedra, on average 4.77 active stages): step ratios 7.48/7.35/7.28 and speedups 4.25/4.09/4.15 for $k=1/2/3$ (§5.3, Table 4). **Shown**
17. Tandem spheres (HiOCFD5, $\mathrm{Re}_D=3900$, Ma 0.1, 237 748 quadratic hexahedra, $k=4$, on average 5.28 active stages): step ratio 8.21, speedup 4.06; front/back sphere $C_D$ 0.382/0.411 (§5.4, Tables 5–6). **Shown**
18. Right-hand-side evaluations drop by a factor of about 4.6–4.8, e.g. laminar $k=2$ from $8.7759\times10^{10}$ to $1.7903\times10^{10}$, and tandem spheres from $1.8304\times10^{13}$ to $3.9240\times10^{12}$ (Tables 3–5). **Shown**
19. The stable step is found empirically: the largest $h$ that completes 1000 iterations without negative density or pressure (§5.2–5.4). **Shown** (protocol)
20. Members are assigned to elements by minimum element edge length (§5.3, §5.4). **Stated**
21. "In general, for the scheme to be of order $p$ we must satisfy $2^{p-1}$ constraints" (§2.1). **Stated** (true only for $p\le4$; the count is the number of rooted trees with at most $p$ vertices, 1, 2, 4, 8, 17, 37, …)
22. Problem 1 (maximize $h$ subject to $\lvert P\rvert\le1$ on the spectrum) is nonconvex for $e>2$ with suboptimal local minima; Problem 2 is convex because $P$ is linear in the $\theta_j$ (§3.3, citing Ketcheson–Ahmadia). **Stated**
23. The flux-reconstruction semi-discrete eigenvalues must have non-positive imaginary part, with the plane-wave convention $e^{i(\theta x-\omega t)}$, for boundedness (§4.2). **Stated**
24. Conclusion: speedups "in excess of four" over classical third-order Runge–Kutta for compressible Navier–Stokes, with negligible effect on the results; future work on higher orders and adaptive steps via embedded pairs (§6). **Stated**

# Printed slips

- Eq. 40 prints $P_{e,3}=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\sum_{j=3}^{e}\gamma_jz^j$; the lower limit should be $j=4$, since the text names the free parameters $\gamma_4,\dots,\gamma_e$.
- §3.3: "The solution to Equation (2) is denoted $r_{e,p}$" and "reformulated the problem in Equation (1)" refer to Problems 2 and 1, not to Eqs. (1)–(2) (the ODE and the Butcher tableau). Also "As mentioned in the Chapter 2" for Section 2.
- Eq. 33 prints $\sum b^l_ic^m_i=\sum b^l_ic^m_i=\frac12$, two identical sides (presumably $\sum b^l_ic^m_i=\sum b^m_ic^l_i$).
- Eq. 30: the $z^6$ coefficient prints only the $\frac14$ term; by the pattern of the $z^4$ and $z^5$ terms it should also carry $\frac34a_{s-1,s-2}a_{s-2,s-3}a_{s-3,s-4}a_{s-4,s-5}c_{s-5}$ (the trailing "+ …" may be intended to cover it).
- For $e=3$, Eq. 22 sets $a_{s-1,s-2}=0$ and Eq. 28 divides by zero; the $e=3$ member must instead satisfy $a_{s,s-1}=2$ (from Eq. 27). The paper does not discuss this case.
- §3.2 reads literally as "equal $b$ (39) gives consistency, equal $c$ (38) gives conservation". In the cited theory equal weights give conservation and equal abscissae (internal consistency) give consistency; the attribution appears swapped.
- Eq. 43: $u^h_i=\sum_{j=1}^{k}u_{i,j}\phi_{k,i,j}$ while the text says $k+1$ nodal points; the text names the basis $\phi_{s,i,j}$, and Eq. 47 uses $\phi_{k,i,g}$.
- Eq. 55 (isentropic vortex) is centred at the origin while the domain is $[0,20]^2$; no centre offset is given.
- Table 2, step sizes: for $\text{P-ERK}_{16,5,3}$ to $\text{P-ERK}_{16,10,3}$ the first step is printed $5.000\times10^{-2}$ before $2.500\times10^{-3}$; for $\text{P-ERK}_{16,11,3}$ to $\text{P-ERK}_{16,16,3}$ the second step is printed $5.000\times10^{-2}$ after $1.000\times10^{-2}$. Both are evidently $5.000\times10^{-3}$. The smallest step $3.120\times10^{-4}$ is presumably $3.125\times10^{-4}$. The column is labelled in seconds for a nondimensional problem.
- Table 6: "30.1 DOFs using P-ERK" and "69.4 DOFs Holst et al." lack the "M". §5.4 gives Martinelli et al. "69.5M DOFs", Table 6 69.4M.
- Table 3 cites "Lopez-Morales et al. [42]" while ref. [42] prints the first author as "M.R. López".
- Abstract: "speedup factors up to four"; the results reach 4.51 (Table 3).
- §6: the "Future work will focus on…" sentence is printed twice.
- §5.4 "relative to RK3.3". Ref. [10] publisher "John Willy"; ref. [16] journal "J. Comput. Sci." for a J. Sci. Comput. paper (recorded as printed).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $du/dt=R(u,t)$, $u$ | $y'=f(t,y)$, $y$ | |
| $u_i$ | $Y_i$ | stage values (stage-value form, Eq. 7) |
| $u_n$ | $y_n$ | |
| $\Delta t$ | $h$ | step size; the source's $h$ is the element size, here $\Delta x$ |
| $u'=\omega u$, $\omega$ | $y'=\lambda y$, $\lambda$ | $\omega$ is also the plane-wave frequency |
| $z=\omega\Delta t$ | $z=h\lambda$ | |
| $P_{s,p}$, $P_{e,p}$, $P_{e,3}$ | $P(z)$ | stability polynomial, degree $e$ |
| $\gamma_j$ | $\theta_j$ | monomial coefficients; **collision**: registry $\gamma$ is the tree density; the source also uses $\gamma$ for the ratio of specific heats |
| $e$ | $e$ | number of active stages; page-local, not in the registry; as on the [P-ERK](/methods/paired-explicit-runge-kutta.md) page |
| $s$, $p$ | $s$, $p$ | stages, order (agree) |
| $A=(a_{ij})$, $b$, $c$ | $A$, $b$, $c$ | agree; $c=A\mathbf 1$ assumed (Eqs. 4, 24) |
| $l$, $m$ (superscripts) | member indices $\{r\}$ | coupled tableaux of the partitioned conditions; the source reuses $l$ for an FR basis vector |
| $S$ | $\mathcal S$ | region of absolute stability |
| $\Delta t_{\text{opt}}$, $P_{\text{opt}}$ | $h_{\mathrm{opt}}$, optimal $P$ | |
| $\boldsymbol\omega$ | eigenvalue set of $L$ | |
| $r_{e,p}(\Delta t,\boldsymbol\omega)$ | — | optimal value of Problem 2; page-local |
| $k$ | $k$ | flux-reconstruction solution degree; page-local (**collides** with the registry $k$: multistep step count, PID exponent denominator) |
| $\epsilon$ | — | bisection tolerance |
| RK3,3 | — | classical three-stage third-order method; tableau not stated |

# Reference list

The paper prints 51 references in numbered style ([1]–[51]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. No printed duplicates. Items printed without volume or pages
(refs. [4]–[9], [14], [16], [31], [33]) are entered as printed; [2] prints
the Hairer–Wanner authors in reversed order; [27] (Matlab) has no author
and [26] (CVX) is software. Ref. [22] is the second-order P-ERK paper of
Vermeire (2019) and [18] is the ingested `hedayatinasab-2021`. All items
parsed.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Paired explicit Runge–Kutta (P-ERK) methods](/methods/paired-explicit-runge-kutta.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
