---
type: Source
title: "Chinomona & Reynolds (2021) — Implicit-Explicit Multirate Infinitesimal GARK Methods"
description: "Introduces IMEX-MRI-GARK methods, multirate infinitesimal schemes with an implicit-explicit slow scale, proves they are GARK methods, derives internal-consistency and third- and fourth-order conditions and a joint stability region, and constructs methods of orders 3 and 4."
resource: "doi:10.1137/20m1354349"
source_kind: paper
authors: [Chinomona R., Reynolds D.R.]
year: 2021
venue: "SIAM J. Sci. Comput. 43:A3082-A3113"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_SIAM_Journal_on_Scientific_Computing_Chinomona_Implicit-Explicit_Multirate_Infinitesimal_GARK_Methods.pdf"
tags: [multirate, imex, gark, order-conditions, stability]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper introduces [IMEX-MRI-GARK](/methods/imex-mri-gark.md) methods for
three-way additive problems $y'=f^{\mathrm I}(t,y)+f^{\mathrm E}(t,y)+f^{\{\mathrm f\}}(t,y)$.
The slow scale is split into a stiff part $f^{\mathrm I}$, treated implicitly, and a
non-stiff part $f^{\mathrm E}$, treated explicitly, and the fast part is treated
"infinitesimally". Each slow stage is reached by solving a modified fast IVP
$v'(\theta)=\Delta c_i\,f^{\{\mathrm f\}}+g(\theta)$, whose polynomial forcing $g$
combines slow implicit and explicit stage tendencies through coefficient matrices
$\Gamma^{(k)}$ (lower triangular) and $\Omega^{(k)}$ (strictly lower triangular).
This extends Sandu's MRI-GARK ([multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md)),
whose slow scale is either explicit or implicit. Before this work only first-order
Lie–Trotter and second-order Strang–Marchuk [splittings](/methods/operator-splitting.md)
combined an IMEX slow scale with an infinitesimal fast scale.

The theory shows that every IMEX-MRI-GARK method is a
[GARK method](/methods/generalized-additive-runge-kutta.md) built on a base
[IMEX ARK](/methods/imex-runge-kutta.md) written in [stiffly accurate](/properties/stiff-accuracy.md)
form, and gives the GARK tables explicitly. It derives the internal-consistency
conditions, two coupling conditions for order 3 and five families for order 4, and
a linear stability function on a three-eigenvalue test problem, built with
[φ-functions](/methods/exponential-integrators.md). It defines a joint stability
region $\mathcal J_{\alpha,\beta}$ that extends Zharovsky et al. to three components
(see [multirate linear stability](/definitions/multirate-linear-stability.md)).
Three methods are built: IMEX-MRI-GARK3a and 3b (order 3, from ARS(3,4,3) in
solve-decoupled form, 8 slow stages; 3b optimized for stability) and IMEX-MRI-GARK4
(order 4, 12 slow stages, empty joint stability region).

Numerical tests on a nonlinear multirate Kværno–[Prothero–Robinson](/benchmarks/prothero-robinson-problem.md)
problem reach the design orders. A stiff advection–diffusion–reaction
[Brusselator](/benchmarks/brusselator.md), run in the [ARKODE](/software/arkode.md)
infrastructure, shows that the new methods beat the legacy splittings at every
accuracy and that the third-order ones compete with implicit MRI-GARK-ESDIRK34a. It
also shows [order reduction](/definitions/order-reduction.md) on the finer spatial
grid.

# Version read

arXiv:2007.09776v3 [math.NA], 3 May 2021, 31 pages (Appendices A–C and the
references included), with the SIAM macro footnote "Submitted to the editors DATE."
and no statement of acceptance. It is not the SIAM version of record
(pp. A3082–A3113). Title and authors on page 1 match Crossref. Definition, theorem,
equation and page numbers on this page are those of arXiv v3.

# Key claims

1. No multirate method allowed IMEX treatment of the slow scale with order 3 or more; the only IMEX-slow, infinitesimal-fast schemes were Lie–Trotter (order 1) and a Strang–Marchuk variant (order 2), both of low accuracy and poor stability (§1, Eqs. (1.3)–(1.4)). **Stated** ("to our knowledge", scoped to infinitesimal fast treatment)
2. IMEX-MRI-GARK methods (Def. 2.1, Eq. (2.3)) are GARK methods: with $\bar\gamma_{ij}=\sum_k\gamma^{(k)}_{ij}/(k+1)$ and $\bar\omega_{ij}=\sum_k\omega^{(k)}_{ij}/(k+1)$, the slow tables are $A^{\{\mathrm I,\mathrm I\}}=E\bar\Gamma$, $A^{\{\mathrm E,\mathrm E\}}=E\bar\Omega$, and the coupling and fast tables have closed Kronecker forms (§2.1, Eqs. (2.5)–(2.26)). **Derived** (assuming one step of an $s^{\{\mathrm f\}}$-stage fast Runge–Kutta method with $b^{\{\mathrm f\}\top}(c^{\{\mathrm f\}})^k=1/(k+1)$)
3. Consistency with the base IMEX ARK when $f^{\{\mathrm f\}}\equiv0$ is ensured by $E\bar\Gamma=A^{\mathrm I}$ and $E\bar\Omega=A^{\mathrm E}$ (Eq. (2.11)). **Derived**
4. The slow implicit and slow explicit partitions share one slow–fast coupling matrix $A^{\{\mathrm s,\mathrm f\}}=\Delta C\otimes b^{\{\mathrm f\}\top}$, whose row sums automatically equal the slow abscissae $c$ (Eqs. (2.12)–(2.18)). **Derived**
5. Internal consistency (Thm. 2.2) holds for every fast method if and only if $\Gamma^{(0)}\mathbf 1=\Omega^{(0)}\mathbf 1=\Delta c$ and $\Gamma^{(k)}\mathbf 1=\Omega^{(k)}\mathbf 1=0$ for all $k\ge1$ (Eq. (2.29)). **Proved**
6. An internally consistent IMEX-MRI-GARK method whose component tables have order at least 2 is at least second order (§2.1.1, citing Sandu–Günther GARK theory). **Stated**
7. An internally consistent IMEX-MRI-GARK method has order 3 if and only if the base IMEX ARK has order at least 3 and $\Delta c^\top\mathcal A^{\{\mathrm I,\zeta\}}c=\tfrac16$, $\Delta c^\top\mathcal A^{\{\mathrm E,\zeta\}}c=\tfrac16$ (Thm. 2.3, Eq. (2.40)). **Proved** (using the simplifying formulas of Sandu's Lemma 3.8)
8. Given Thm. 2.3, order 4 holds if and only if the base IMEX ARK has order at least 4 and conditions (2.41a)–(2.41e) hold for all pairs of slow partitions; of the 26 order-4 GARK coupling conditions, ten hold automatically and the other 16 reduce to (2.41) (Thm. 2.4, Eqs. (2.41)–(2.49)). **Proved**
9. Assuming $b^{\mathrm E}=b^{\mathrm I}$ in the base method simplifies the order-4 conditions only slightly: only (2.41c) benefits, four conditions collapsing to two (Remark 2.5). **Derived**
10. For solve-decoupled third-order methods with $\bar\Gamma=\Gamma^{(0)}$, $\bar\Omega=\Omega^{(0)}$, the conditions (2.40) are equivalent to $\Delta c^\top(L_{\mathrm s}+\tfrac12E^{-1})A^{\mathrm E}c=\tfrac16$ and the same with $A^{\mathrm I}$, each the MIS third-order condition of Knoth & Wolke (Remark 4.1, Eq. (4.1)). **Stated** (equivalence asserted, not proved in detail)
11. On $y'=(\lambda^{\{\mathrm f\}}+\lambda^{\mathrm E}+\lambda^{\mathrm I})y$ with commuting parts and an exact fast solve, $R(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})=e_{s}^\top\big(I-\operatorname{diag}(e^{\Delta c\,z^{\{\mathrm f\}}})L_{\mathrm s}-z^{\mathrm E}\eta(z^{\{\mathrm f\}})-z^{\mathrm I}\mu(z^{\{\mathrm f\}})\big)^{-1}e_1$, $z^{\{\cdot\}}=H\lambda^{\{\cdot\}}$, where $\eta=\sum_k k!\,\operatorname{diag}(\phi_{k+1}(\Delta c\,z^{\{\mathrm f\}}))\,\Omega^{(k)}$ and $\mu$ likewise with $\Gamma^{(k)}$ (§3, Eq. (3.3)). **Derived**
12. The joint stability region $\mathcal J_{\alpha,\beta}$ (the explicit slow region valid for every $z^{\{\mathrm f\}}$ in a sector of half-angle $\alpha$ and every $z^{\mathrm I}$ in a sector of half-angle $\beta$) extends Zharovsky et al. to a three-part splitting; it is "artificially restrictive", since $f^{\mathrm I}$ and $f^{\{\mathrm f\}}$ are not infinitely stiffer than $f^{\mathrm E}$ (§3). **Stated**
13. IMEX-MRI-GARK3a is built from ARS(3,4,3), padded to stiffly accurate form and converted to solve-decoupled form (8 slow stages); its 54 unknowns (10 free table entries, 24 in $\Gamma^{(0)}$, 20 in $\Omega^{(0)}$) against 50 independent linear conditions are fixed by a minimum-norm least-squares solution (§4.1, App. A). **Shown** (construction)
14. IMEX-MRI-GARK3b uses the four remaining free parameters to extend the joint stability region along the negative real axis; its $\mathcal J_{\alpha,\beta}$ is "significantly larger" than that of 3a, covering most of the base IMEX ARK region for $\alpha=10^\circ,45^\circ$ and $\beta\le60^\circ$, while that of 3a shrinks as $\beta$ grows (§4.1, Fig. 1, App. B). **Shown**
15. IMEX-MRI-GARK4 (order 4, polynomial coupling of degree 1, 12 slow stages) satisfies (2.11), (2.29), (2.40) and (2.41), but even with $z^{\mathrm E}=0$ its stability region is very small and $\mathcal J_{\alpha,\beta}$ is empty; the authors "do not promote its widespread use" (§4.2, App. C). **Shown**
16. No fourth-order IMEX ARK with sorted abscissae $0=c_1\le\dots\le c_s\le1$ was known to the authors, who therefore designed their own base method (§4.2). **Stated**
17. Solve-decoupled multirate methods are easier to implement but less stable than solve-coupled ones (§4.1, citing Roberts et al.). **Stated**
18. On the multirate Kværno–Prothero–Robinson problem the measured orders are 0.99 (Lie–Trotter), 1.98 (Strang–Marchuk), 3.10 (IMEX-MRI-GARK3a), 3.14 (3b), 3.06 (MRI-GARK-ESDIRK34a), 4.15 (IMEX-MRI-GARK4) and 3.93 (MRI-GARK-ESDIRK46a), with $H=\pi/2^k$ and $m=20$ (§5.1, Fig. 2). **Shown**
19. On the Brusselator the best-fit orders are 0.91, 1.92, 2.86, 2.92, 2.94, 3.12, 2.94 on 201 points and 0.90, 1.87, 2.41, 2.47, 3.02, 2.69, 2.42 on 801 points (same order of methods as claim 18); the higher-order methods lose order when the grid is refined (§5.2, Fig. 3). **Shown**
20. On the Brusselator IMEX-MRI-GARK4 is unstable for $H>1/80$ (201 points) and $H>1/160$ (801 points), MRI-GARK-ESDIRK46a for $H>1/40$ and $H>1/80$; all other methods are stable at every $H=0.1\cdot2^{-k}$, $k=0,\dots,10$ (§5.2). **Shown**
21. IMEX-MRI-GARK and implicit MRI-GARK methods are more efficient (error against run time) than Lie–Trotter and Strang–Marchuk at every accuracy shown (§5.2, Fig. 3). **Shown**
22. The third-order IMEX-MRI-GARK methods beat IMEX-MRI-GARK4 on the Brusselator because they need fewer slow implicit solves per step (3 against 5), a cheaper fast implicit method (2 against 5 implicit stages), and suffer less order reduction (§5.2). **Shown** / attribution **Stated**
23. MRI-GARK-ESDIRK46a is the most efficient below errors of $10^{-8}$; all third-order methods are comparable at looser accuracies, with no visible run-time difference between IMEX-MRI-GARK3a/b and MRI-GARK-ESDIRK34a on 201 points, while the latter is more efficient on 801 points (§5.2). **Shown**
24. The linear-advection Brusselator is a "best case" for implicit MRI-GARK; for reacting compressible flow with nonlinear shock-capturing advection, IMEX-MRI-GARK3a/b are expected to be "significantly more efficient" (§5.2). **Stated** (expectation, not shown)
25. Order-5 conditions, embedded methods for adaptivity, optimized fourth-order methods and solve-coupled IMEX-MRI-GARK methods are left to future work (§6). **Stated**

# Printed slips

- §5.1 (pp. 20–21), Kværno–Prothero–Robinson splitting: the problem's forcing is printed as $-[\beta\sin(\beta t)/(2u);\ \sin(t)/(2v)]$, but the split part is printed "$f^{\{E\}}=[0;\ \sin(t)/(2v)]$" with a plus sign; since $v=\sqrt{2+\cos t}$ gives $v'=-\sin t/(2v)$, it should be $[0;\ -\sin(t)/(2v)]$ (checked visually, p. 21).
- §2.1 (p. 6): "$b^{\{F\}T}c^{\{F\}\times k}=1/(k+1)$ for $k=1,\dots,q$": the quadrature conditions of an order-$q$ method hold for $k=0,\dots,q-1$; (2.8) is also cited before it is defined.
- §3 (p. 16): the definition uses $z^{\{F\}}\in S^{\{F\}}_\alpha$, $z^{\{I\}}\in S^{\{I\}}_\beta$, but the explanation says "$z^{\{I\}}$ can range throughout an entire infinitely long sector $S^{\{I\}}_\alpha$ … $z^{\{F\}}$ … $S^{\{F\}}_\beta$": the sector angles are swapped.
- §4 (p. 17): "IMEX-MRI-GARK methods of the form (2.1)": should be (2.3).
- Proof of Thm. 2.4 (p. 14): "$=\tfrac12\Delta c^{\{S\}}\mathcal A^{\{\sigma,\zeta\}}c^{\{S\}\times2}$": transpose missing on $\Delta c^{\{S\}}$.
- Reference [11] prints "pp. 207–207"; reference [2] prints a doubled "https://doi.org/https://doi.org/" prefix and no volume.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f^{\{I\}}$, $f^{\{E\}}$ | $f^{\mathrm I}$, $f^{\mathrm E}$ | slow stiff and slow non-stiff parts |
| $f^{\{F\}}$, $\{S\}$ | $f^{\{\mathrm f\}}$, $\{\mathrm s\}$ | fast part, slow label |
| $H$, $h$ | $H$, $h$, $m=H/h$ | $h=H/20$ (Prothero–Robinson), $H/5$ (Brusselator) |
| $Y_i^{\{S\}}$ | $Y_i$ | slow stage values |
| $c^{\{S\}}$, $\Delta c_i^{\{S\}}$ | $c$, $\Delta c_i=c_i-c_{i-1}$ | slow abscissae, sorted |
| $A^{\{E,E\}}$, $A^{\{I,I\}}$, $b^{\{E\}}$, $b^{\{I\}}$ | $A^{\mathrm E}$, $A^{\mathrm I}$, $b^{\mathrm E}$, $b^{\mathrm I}$ | base IMEX ARK in stiffly accurate (padded) form |
| $\mathbf A^{\{\sigma,\nu\}}$, $\mathbf b^{\{\sigma\}}$, $\mathbf c^{\{\sigma,\nu\}}$ | $A^{\{q,r\}}$, $b^{\{q\}}$ | GARK tables; agrees in form |
| $A^{\{F,F\}}$, $b^{\{F\}}$, $c^{\{F\}}$, $s^{\{F\}}$ | fast tableau | kept with $\{\mathrm f\}$ |
| $\Gamma^{\{k\}}$, $\Omega^{\{k\}}$, $\gamma^{\{k\}}_{i,j}$, $\omega^{\{k\}}_{i,j}$ | $\Gamma^{(k)}$, $\Omega^{(k)}$, $\gamma^{(k)}_{ij}$, $\omega^{(k)}_{ij}$ | registry MRI coupling matrices (implicit and explicit slow parts); $\gamma$ clashes with the registry tree density and Rosenbrock $\gamma$ |
| $\gamma_{i,j}(\tau)$, $\omega_{i,j}(\tau)$, $\tau=\theta/H$, $k_{\max}$ | $\gamma_{ij}(\theta/H)$, $\omega_{ij}(\theta/H)$, $k_{\max}$ | coupling polynomials in the normalized inner time; the source's $\tau$ collides with a tree $\tau$ |
| $\theta$, $v(\theta)$, $g(\theta)$ | kept | fast-IVP variable, fast solution, slow forcing |
| $\mathbb 1$, $e_j$ | $\mathbf 1$, $e_j$ | |
| $E$, $D$ | kept | lower and upper triangular all-ones matrices; **$D$ is not** the simplifying assumption $D(\zeta)$ |
| **$L$** | $L_{\mathrm s}$ on this page | sub-diagonal shift $L_{ij}=\delta_{i,j+1}$; **collides** with the registry linear operator $L$ |
| $\Delta C^{\{S\}}$ | $\Delta C$ | lower triangular, column $j$ equal to $\Delta c_j$ |
| $a\times b$, $c^{\times k}$, $\otimes$ | componentwise product and power, Kronecker product | |
| **$\varphi_k(z)=\int_0^1e^{z(1-t)}t^{k-1}\,dt$** | $\phi_k$, with $\varphi_k=(k-1)!\,\phi_k$ | **collision:** the source omits the $1/(k-1)!$ factor, so its recursion is $\varphi_{k+1}=(k\varphi_k-1)/z$ |
| $z^{\{\sigma\}}=H\lambda^{\{\sigma\}}$, $R$ | $z=h\lambda$ with $H$, $R$ | stability function |
| $\eta(z)$, $\mu(z)$ | kept | explicit and implicit stability matrices; $\eta$ is also an ARS(3,4,3) parameter |
| $S^\sigma_\alpha$, $\mathcal J_{\alpha,\beta}$ | kept | sectors and joint stability region; **$\alpha$ clashes** with the registry A($\alpha$) angle and Shu–Osher $\alpha_{ij}$ |
| **$\zeta_k$, $\beta_k$, $\xi_k$** | kept | moments of the fast method; collide with $D(\zeta)$, the PID $\beta$, $B(\xi)$ |
| $q$ | $p$ | order of the base IMEX ARK; **registry $q$ is the stage order** |
| $\varepsilon$, $\Lambda$ (Prothero–Robinson) | $\varepsilon$ | coupling parameter of the test problem |

# Reference list

44 printed references, numbered [1]–[44] in SIAM style. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` chinomona-2021.
Pre-publication citations (Gardner et al. arXiv:2011.10073, Roberts et al.
arXiv:1910.14079 and arXiv:2002.00868, Sexton arXiv:1808.03718) are separate
entries, and [7] is a GitHub repository holding the coefficients. Same-key pairs take
suffixes in printed order (Luan 2014 ×2, Roberts 2020 ×2). [2] has no volume and a
doubled DOI prefix, [5] has no volume, [11] prints "pp. 207–207", and [26] (Marchuk)
has an EuDML URL and no DOI. No printed duplicates and no unparseable items.

# Pages created or updated

Chunk 1 (2026-10-19). This source is cited on:

* [A-stability barriers for decoupled and internally consistent multirate methods](/results/multirate-a-stability-barriers.md)
* [ARKODE](/software/arkode.md)
* [Brusselator](/benchmarks/brusselator.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Exponential integrators and φ-functions](/methods/exponential-integrators.md)
* [Generalized additive Runge–Kutta (GARK) methods and internal consistency](/methods/generalized-additive-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [IMEX multirate infinitesimal GARK methods](/methods/imex-mri-gark.md)
* [Linear stability of multirate methods and joint stability regions](/definitions/multirate-linear-stability.md)
* [Multirate infinitesimal methods (MIS, MRI-GARK)](/methods/multirate-infinitesimal-methods.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Order reduction](/definitions/order-reduction.md)
* [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
