---
type: Source
title: "Glandon et al. (2022) — Linearly Implicit Multistep Methods for Time Integration"
description: "Introduces linearly implicit multistep methods (Limm, and the W-variant Limm-w), which need one linear solve per step, derives their variable-step order conditions by Taylor and B-series expansion, proves stiff convergence, designs methods of orders 1–5 with larger stability angles than BDF and compares them with BDF in a variable-step code."
resource: "doi:10.1137/20m133748x"
source_kind: paper
authors: [Glandon R., Narayanamurthi M., Sandu A.]
year: 2022
venue: "SIAM J. Sci. Comput. 44:A3437-A3462"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_SIAM_Journal_on_Scientific_Computing_Glandon_Linearly_Implicit_Multistep_Methods_for_Time_Integration.pdf"
tags: [linear-multistep, implicit, stiff, order-conditions, b-series, step-size-control]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

Implicit [linear multistep methods](/methods/linear-multistep-method.md)
such as [BDF](/methods/backward-differentiation-formula.md) need a
nonlinear solve per step. The paper introduces
[linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md)
(Limm), built from multistep methods the way
[Rosenbrock methods](/methods/rosenbrock-wanner-method.md) are built from
implicit Runge–Kutta methods. A $k$-step Limm combines past solutions and
past function values with the single Jacobian $J_n$ applied to a linear
combination of past solutions (and optionally past function values), so
each step costs exactly one linear solve with $I-h_n\kappa_{-1}J_n$.
It has $4k+1$ free coefficients against $2k+1$ for a classical method, at
the same storage. The W-variant Limm-w allows an arbitrary matrix $W_n$ in
place of $J_n$.

Order conditions are derived for variable steps: by Taylor expansion for
Limm-w ($2p+1$ conditions) and by [B-series](/definitions/b-series.md) with
an extra "fat" node for $J_ny$ for the exact-Jacobian Limm ($2p$
conditions). Only the order-two conditions differ, exactly as for
Rosenbrock versus W-methods. Linear stability uses a three-polynomial
characteristic equation and a companion stability matrix;
[zero-stability](/definitions/zero-stability.md) on variable grids is
discussed through products of these matrices. A convergence theorem gives
order $p$ on problems whose stiffness is linear, with a step bound
independent of the stiffness; a remark extends it to index-1
[DAEs](/definitions/differential-algebraic-equation.md). With no
Jacobian–function-value terms, Limm-w is an
[IMEX multistep method](/methods/imex-linear-multistep-methods.md) for the
splitting $f=(f-J_ny)+J_ny$.

Methods of orders 1–5 designed by a genetic algorithm have larger
[A($\alpha$)](/properties/a-stability.md) angles than BDF for $k=3,4,5$.
A self-starting variable-step, variable-order implementation with a
divided-difference [error estimate](/methods/step-size-control.md) runs in
MATLODE. On Lorenz-96 the fixed-step orders are confirmed; on Gray–Scott
(direct LU) and a quasi-geostrophic model (GMRES,
[inexact linear solves](/methods/implicit-stage-solvers.md)) Limm is
slightly faster than an in-house BDF in the same framework and matches or
beats RODAS4 and SDIRK4a on the quasi-geostrophic model.

# Version read

The file is a SIAM-template author manuscript, not the version of record:
every page carries line numbers and the footer "This manuscript is for
review purposes only.", and the title footnote reads "Submitted to the
editors on 5/11/2020." It has 26 pages (main text 1–22, references 22–25,
Table 6.2 on p. 26), all read, paginated 1–26 rather than A3437–A3462.
Whether it is the first submission or a revision cannot be decided.
Several cross-references point into a supplement that is not part of the
file ("Table ??", "Figure ??"); the fixed-step Limm coefficients, the
variable-step coefficient formulas and the Limm stability regions are only
there. Title and authors match Crossref. Numbering cited here is that of
the manuscript.

# Key claims

The paper indexes coefficients by $i=-1,\dots,k-1$, with $i=-1$ the new
point $t_{n+1}$ and $y_{n-i}$ the value at $t_{n-i}=t_n-\delta_ih_n$; the
claims keep this indexing (see the Notation map for the registry form). The
Jacobian coefficients are written $\kappa_i$ and $\xi_i$ as on the
[Limm](/methods/linearly-implicit-multistep-method.md) page (the source's
$\mu_i$, $\nu_i$), and the step fractions satisfy $\delta_i=-\theta_{k-1-i}$
with that page's $\theta_j$.

1. A $k$-step Limm, $\sum_{i=-1}^{k-1}\alpha_iy_{n-i}=h_n\sum_{i=0}^{k-1}\beta_if_{n-i}+h_nJ_n\big(\sum_{i=-1}^{k-1}\kappa_iy_{n-i}+h_n\sum_{i=0}^{k-1}\xi_if_{n-i}\big)$ with $\alpha_{-1}=1$, needs exactly one linear solve per step with $I-h_n\kappa_{-1}J_n$, has $4k+1$ free coefficients against $2k+1$ for a classical method, and stores $k$ past solutions and $k$ past function values (§2, Def. 2.2, Eq. 2.4). **Stated**
2. Direct linearization of an implicit multistep method about $(t_n,y_n)$ keeps the classical number of degrees of freedom and is expected to degrade accuracy and stability; a variant with past Jacobian–vector products is rejected for its storage (§2, Eqs. 2.2–2.3). **Stated**
3. Limm-w (arbitrary $W_n$, variable steps) has order $p$ iff $\sum_i\alpha_i=0$, $\sum_i\kappa_i=0$, $\sum_{i=-1}^{k-1}\alpha_i\delta_i^\ell+\ell\sum_{i=0}^{k-1}\beta_i\delta_i^{\ell-1}=0$ ($\ell=1,\dots,p$) and $\sum_{i=-1}^{k-1}\kappa_i\delta_i^{\ell-1}-(\ell-1)\sum_{i=0}^{k-1}\xi_i\delta_i^{\ell-2}=0$ ($\ell=2,\dots,p$): $2p+1$ conditions (Thm. 3.3, Eq. 3.3). **Proved**
4. In the stiff case ($\lVert h_nW_n\rVert\not\to0$) the local error is dominated by an $O(h^p)$ term; imposing the $\kappa$/$\xi$ conditions up to order $p+1$ restores $O(h^{p+1})$ (Remark 3.4). **Derived**
5. The pair $\{\alpha_i,\beta_i\}$ of an order-$p$ Limm-w is itself an order-$p$ explicit $k$-step method; the Jacobian terms contribute only at $O(h^{p+1})$ (Remark 3.5). **Derived**
6. For $p\le k$ the order conditions, linear with Vandermonde structure, have solutions with $\alpha_i$, $\kappa_i$ continuous in $\beta_i$, $\xi_i$, the step fractions and $k-p$ free parameters (Remark 3.6). **Derived**
7. The exact-Jacobian Limm has order $p$ under $2p$ conditions, derived by B-series over the trees plus the empty tree and a fat node $\tau_\circ$ with $F(\tau_\circ)(y)=J_ny$; they coincide with the Limm-w conditions except at order two, where the single combined condition $\sum_i\alpha_i\delta_i^2+2\sum_i\big((\beta_i+\kappa_i)\delta_i-\xi_i\big)=0$ replaces the two separate ones (Thm. 3.7, Remark 3.8, Eq. 3.17). **Proved**
8. The Limm order conditions depend only on the tree order $\lvert\tau\rvert$, not on its topology; for $\lvert\tau\rvert\ge3$ both the singly- and multiply-branched-root conditions apply, which forces the separate $\kappa$/$\xi$ condition (§3.2). **Derived**
9. On $y'=\lambda y$ the method gives the characteristic equation $\varrho(\zeta)-z\sigma(\zeta)-z^2\upsilon(\zeta)=0$, where $\sigma$ is built from $\beta_i+\kappa_i$ and $\upsilon$ from $\xi_i$; the boundary locus is $z=\varrho/\sigma$ when all $\xi_i=0$ and a quadratic-root formula otherwise (§4, Eqs. 4.1–4.4). **Derived**
10. For the 2-step Limm as $z\to-\infty$ the stability matrix $\mathcal M_2(r_1,\infty)$ has spectral radius $\le1$ iff $r_1\ge1/3$; computer algebra gives the same condition for every real $z<0$ (§4.1). **Shown**
11. For the 2-step Limm-w a weighted norm of $\mathcal M_2(r,z)$ is $\le1$ for all real $z<0$ and all $r\in[r_{\min},r_{\max}]$ with $r_{\min}=13204873/133414177\approx0.1$ and $r_{\max}=(10262629+\sqrt{484910319930169})/20525258\approx1.57$ (Remark 5.6). **Shown** (computed, no proof)
12. An order-$p$ Limm-w with $\xi_i=0$, under Assumptions 5.1–5.5 (stiffness linear and captured by a local Jacobian, A($\alpha$)-stability, strict stability at the origin and at infinity, $\kappa_{-1}>0$, bounded products of stability matrices), converges with global error $O(h_{\max}^p)$ for $h_j\le h_*$, $h_*$ independent of the stiffness, given $O(h_{\max}^p)$ starting values (Thm. 5.8). **Proved**
13. With $\xi_i=0$, Limm-w is an IMEX multistep method for the splitting $f=(f-J_ny)+J_ny$, with explicit coefficients $\beta_i$ and implicit coefficients $\kappa_i+\beta_i$; its order conditions are equivalent to those of claim 3 (§5, Eq. 5.1). **Derived**
14. The convergence result also holds in the non-stiff case (Remark 5.9). **Stated**
15. Limm with $\xi_i=0$, strictly stable at infinity, applied to semi-explicit index-1 DAEs gives $O(h_{\max}^p)$ errors in both the differential and the algebraic variables (Remark 5.10, Eqs. 5.8–5.9). **Derived** (informal)
16. Design choices: $\xi_i=0$ ($3k+1$ free coefficients), $\sigma(0)=0$ so that the root $\zeta(z)\to0$ as $z\to-\infty$, zero-stability as a nonlinear constraint, objectives "maximize the A($\alpha$) angle" and "minimize the squared residuals of the order-$(p+1)$ conditions", a MATLAB genetic algorithm, free parameters rationalized (§6, Eqs. 6.1–6.4). **Stated**
17. Fixed-step Limm and Limm-w of orders 1 and 2 are A-stable; orders 3–5 are A($\alpha$)-stable (Fig. 6.1, Table 6.1). **Shown**
18. A($\alpha$) angles for $k=1,\dots,5$: BDF 90, 90, 86.03, 73.35, 51.84; Limm 90, 90, 87.7849, 78.0742, 72.9999; Limm-w 90, 90, 87.3899, 77.9101, 70.3168. Error constants: BDF 0.5, 0.333333, 0.25, 0.2, 0.166667; Limm 0.5, 0.222222, 0.167344, 0.204625, 0.217405; Limm-w 0.5, 0.424915, 0.403238, 0.380873, 0.365325 (Table 6.1). **Shown**
19. Exact rational fixed-step Limm-w coefficients for $k=1,\dots,5$ are given in Table 6.2; the 1-step Limm-w is the linearly implicit Euler method $y_{n+1}-y_n=h_nf_n+h_nW_n(y_{n+1}-y_n)$ (Table 6.2). **Stated**
20. Local error estimate for variable step and order: $e^{(k,h)}_{n+1}=(k+1)!\,C_k\,h_n^{k+1}\,\delta^{k+1}y[t_{n+1},\dots,t_{n-k}]$, with $C_k$ the larger of the two order-$(k+1)$ residuals over $(k+1)!$; it may slightly overestimate (Def. 7.1, Eqs. 7.3–7.5). **Derived**
21. Step increases are allowed only after $k$ successful steps at the current step size, because explicit ratio bounds for general multistep methods are not available (Remark 7.3). **Stated**
22. Lorenz-96 ($d=40$, $t\in[0,0.5]$, fixed steps): measured slopes for Limm $k=1,\dots,5$ are $-0.991496$, $-1.949240$, $-2.984357$, $-3.974819$, $-4.925216$ and for Limm-w $-0.991496$, $-2.010821$, $-3.128820$, $-4.018503$, $-5.004428$ (§8.1, Fig. 8.1). **Shown**
23. Gray–Scott ($128\times128$ grid, direct LU): the five multistep integrators reach similar errors with similar step counts; SDIRK4a and RODAS4 need fewer steps; MATLAB ode15s is fastest in CPU time; Limm and Limm-w show a "small performance advantage" over the in-house BDF (§8.2, Fig. 8.2). **Shown**
24. Quasi-geostrophic model ($127\times127$, GMRES at one tenth of the integrator tolerance): error–step curves are jagged at loose tolerances, possibly from inexact GMRES solves; Limm keeps its CPU advantage over BDF and matches or beats RODAS4 and SDIRK4a; ode15s performs very poorly (§8.3, Fig. 8.3). **Shown**
25. Runs use MATLAB 2019a, tolerances $10^{-2}$ to $10^{-10}$ with $\mathrm{rtol}=\mathrm{atol}$, and reference solutions from ode15s or RODAS4 (§8). **Stated**
26. "Our variable stepsize Limm implementation outperforms a comparable BDF implementation for nonlinear problems" (§9). **Shown** (two problems, same framework)

*(Compiler checks, not in the sources.)* Table 6.1 lists BDF error constants as $1/(k+1)$,
a normalization the caption does not state, while the Limm constants are
not divided by $\sigma(1)$, so the rows may mix normalizations. The
abstract's "error constants comparable to BDF" holds for Limm, not for
Limm-w, whose constants exceed BDF's for every $k\ge2$. Remark 3.4 (stiff
order loss unless the conditions are imposed one order higher) and
Theorem 5.8 (full order under linear stiffness) concern different settings,
and the paper does not relate them. The condition $\sigma(0)=0$ gives
damping at infinity, which the paper calls "a condition for L-stability",
although orders 3–5 are only A($\alpha$)-stable.

# Printed slips

- Unresolved references "Table ??" (p. 10, l. 306; p. 12, l. 382; p. 16, l. 499), "Figure ??" (l. 499) and "Sections ?? and ??" (l. 501), all to the missing supplement.
- Proof of Thm. 3.3 (p. 5, l. 156): "Subtracting (3.5) from (3.10)"; (3.10) is the exact-Jacobian equation of §3.2, and (3.4) is meant.
- Remark 3.4 (p. 5, l. 165): "which recovers Theorem 3.1"; there is no Theorem 3.1, Theorem 3.3 is meant.
- Eqs. 3.6–3.7 (p. 5): the local-error factor is printed $(I-h_nA_n)^{-1}$; by (3.4) it should be $(I-h_n\mu_{-1}A_n)^{-1}$.
- Eqs. 3.14 and 3.17b (pp. 8–9): "$\sum_{i=-1}^{k}\mu_i=0$" with upper limit $k$; everywhere else the coefficients run to $k-1$.
- Remark 3.8 (p. 9): (3.17d) "is the sum of Limm-w conditions (3.3c) and (3.3d) for ℓ=2"; it is (3.3c) plus twice (3.3d).
- Eq. 7.7 (p. 18): the $\hat\mu$ term carries $h\,J_n$ instead of $h_nJ_n$.
- Assumption 5.2 (p. 11): "A(α) stable, for 0 ≤ α ≤ π/2" reuses $\alpha$ and admits the trivial $\alpha=0$.
- Thm. 5.8 (p. 12): "$\|\Delta y_n\|=O(h^p_{\max})$ for $i=1,\dots,k$"; the index should be $\Delta y_i$.
- Proof of Thm. 5.8 (p. 13, l. 421): "$h_*<(C_TL\mu_{-1})^{-1}$" uses $L$ where $L_*$ was defined.
- Remark 5.10 (p. 14, l. 441): "satisfying (3.3b) up to order p", where (3.3) is meant; "LIMM" in capitals (l. 452).
- §8.2 (p. 20, l. 622): "chemical reactions with retirement".
- Remark 7.2 (p. 18): the start-up formula $\delta^3y[t_1,t_0]\approx(\delta^2y[t_1,t_0]-J_0f_0)/(3h_0)$ subtracts $y''(t_0)$ from a divided difference of size $y''/2$; printed so.
- §4.1 uses the 2-step Limm coefficients "from Table ??" and Remark 5.6 the 2-step Limm-w, two different methods.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y\in\mathbb R^N$ | $y\in\mathbb R^d$ | dimension |
| $f_n$, $J_n$ | $f(y_n)$, $J_n$ | agree; autonomous form from Remark 2.1 |
| $h_n=t_{n+1}-t_n$ | $h_n$ | agree |
| $k$ | $k$ | number of steps; agree |
| $\sum_{i=-1}^{k-1}\alpha_iy_{n-i}$ | $\sum_{j=0}^k\alpha_jy_{n+1-k+j}$ | registry index $j=k-1-i$; the source's $i=-1$ is the new point; normalization $\alpha_{-1}=1$ |
| $\alpha_i$, $\beta_i$ | $\alpha_j$, $\beta_j$ | multistep coefficients, reversed index; $\beta_{-1}=0$ in Limm |
| $\mu_i$ | $\kappa_i$ (page-local, as on the [Limm](/methods/linearly-implicit-multistep-method.md) page) | coefficients of $J_ny_{n-i}$; $\kappa_{-1}$ plays the Rosenbrock $\gamma$; renamed: **collision** with the registry multipliers $\mu_j$ |
| $\nu_i$ | $\xi_i$ (page-local, as on the Limm page) | coefficients of $h_nJ_nf_{n-i}$; **collision** with the Courant number $\nu$; zero in all designed methods |
| $A_n$ | $W_n$ | arbitrary matrix of Limm-w; **collision** with the Butcher matrix $A$ |
| $\omega_n=h_n/h_{n-1}$ | $r_n$ | step ratio; $\omega_{\min}$, $\omega_{\max}$ written $r_{\min}$, $r_{\max}$ |
| $c_i$ | $\delta_i$ (page-local) | step fractions, $t_{n-i}=t_n-c_ih_n$, $c_{-1}=-1$, $c_0=0$; the Limm page writes $\theta_j=-\delta_{k-1-j}$; **collision** with the Runge–Kutta abscissae |
| $T$, $T_1$, $\varnothing$, $\tau_\circ$ | $T$, —, $\varnothing$, $\tau_\circ$ | trees, extended tree set, empty tree, fat node with $F(\tau_\circ)(y)=J_ny$ |
| $t$, $\lvert t\rvert$, $\sigma(t)$, $\gamma(t)$, $F(t)$ | $\tau$, $\lvert\tau\rvert$, $\sigma(\tau)$, $\gamma(\tau)$, $F(\tau)$ | tree notation |
| $\theta$ | — | B-series coefficients of the numerical solution |
| $\varrho(\zeta)$, $\sigma(\zeta)$, $\upsilon(\zeta)$ | $\varrho(\zeta)$, $\sigma(\zeta)$, $\upsilon(\zeta)$ | agree in name; the source's $\sigma$ is built from $\beta_i+\mu_i$, not from $\beta_i$ alone; $\upsilon$ is local |
| $z=h\lambda$, $\mathcal S$ | $z$, $\mathcal S$ | stability region by the root condition |
| $M(\omega_{i-k:i-1},z)$ | $\mathcal M(r,z)$ | companion stability matrix; **collision** with the mass matrix $M$ |
| $\rho(\cdot)$, $\rho_\infty$ | — | spectral radius; $\rho(\mathcal M(\mathbf 1,\infty))$ |
| $\phi$ (also $\alpha$ in Assumption 5.2) | A($\alpha$) angle | |
| $\rho_{p+1,a}$, $\rho_{p+1,b}$, $\Phi_1$, $\Phi_2$ | — | order-$(p+1)$ residuals and design objectives |
| $C_k(c)$, $e^{(k,h)}_{n+1}$, $h^{(k)}_{\mathrm{opt}}$ | $C_k$, —, — | error constant, local error estimate, optimal step |
| $\delta^iy[\cdot]$, $\hat\alpha_i$, $\hat\mu_i$, $\hat\beta_i$ | — | divided differences and transformed coefficients; distinct from the step fractions $\delta_i$ |
| $J_\tau$, $r_\tau$, $L_\tau$, $J_*$, $L_*$ | — | local linear stiff part, nonlinear remainder and Lipschitz constants (Assumption 5.1) |
| $T_n=I-h_n\mu_{-1}J_*$, $C_T$, $C_M$ | — | solve matrix and its bounds |

# Reference list

The paper prints 56 references in SIAM numbered style ([1]–[56]), with DOIs
or URLs for most. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. Ref. [36]
(Roberts et al., "Implicit multirate GARK methods", printed as a Virginia
Tech report "in print" in J. Sci. Comput., 2020, with arXiv 1910.14079) is
the pre-publication form of the ingested
[Roberts et al. (2021)](/sources/roberts-2021.md); it is merged into the
existing arXiv-preprint entry `roberts-2019-b`, distinct from the published
work. Ref. [3] (MATLODE) is printed as submitted, and [38] (Roberts, Sarshar
& Sandu, "in print" without volume or pages) is `roberts-2020-c`. Ref. [28]
(Lorenz) prints the book title only; [42] prints no pages; [5] (Butcher) is
printed with year 2009 and keyed `butcher-2009-b`; [24] prints the DOI
"10.1007/s211-001-8010-0", kept unverified; [19] and [29] carry JSTOR URLs.
Same-author same-year pairs follow the keys already in the bibliography, not
the printed order: [12]/[13] are `cardone-2014-b`/`cardone-2014`,
[49]/[50] `tranquilli-2014-b`/`tranquilli-2014`, [53]/[54]
`zhang-2014-b`/`zhang-2014`, and [2] is `akrivis-2015-b`. No printed
duplicates; all items parsed.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [B-series, composition and substitution laws](/definitions/b-series.md)
* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [CVODE](/software/cvode.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Gray–Scott model](/benchmarks/gray-scott-model.md)
* [IMEX linear multistep and IMEX-BDF methods](/methods/imex-linear-multistep-methods.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Linearly implicit multistep methods (Limm, Limm-W)](/methods/linearly-implicit-multistep-method.md)
* [Order reduction](/definitions/order-reduction.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Zero-stability](/definitions/zero-stability.md)
