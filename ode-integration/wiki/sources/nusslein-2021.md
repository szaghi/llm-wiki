---
type: Source
title: "Nüßlein et al. (2021) — Positivity-preserving adaptive Runge–Kutta methods"
description: "Restores positivity of a Runge–Kutta step after the stages are computed by re-choosing the weights through a linear program under the linear order conditions, preserving every linear invariant, with stability bounds for convex and free adaptation and an error estimate for step-size control."
resource: "doi:10.2140/camcos.2021.16.155"
source_kind: paper
authors: [Nüßlein S., Ranocha H., Ketcheson D.I.]
year: 2021
venue: "Commun. Appl. Math. Comput. Sci. 16:155-179"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Communications_in_Applied_Mathematics_and_Computational_Scie_Nüßlein_Positivity-preserving_adaptive_RungeKutta_methods.pdf"
tags: [positivity, structure-preserving, runge-kutta, embedded-pair, step-size-control]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

An unconditionally positive Runge–Kutta or general linear method has order at most 1 (Bolley–Crouzeix). The paper therefore enforces [positivity](/properties/positivity-preservation.md) per problem and per step. Once the stage derivatives of a step are known, the update $y_{n+1}=y_n+h\sum_ib_if(t_n+c_ih,Y_i)$ is linear in the weights. If it has negative entries, the weights $b$ are replaced by $\tilde b$ from a linear program: minimize $\lVert\tilde b-b\rVert_1$ subject to positivity (or two-sided bounds) and to the order conditions up to a possibly reduced order $\tilde p$, which are linear in $b$ for fixed $A$ and $c$ ("free adaptation"). A variant restricts $\tilde b$ to convex combinations of known weight vectors, such as the [embedded](/methods/embedded-runge-kutta-pair.md) weights or a backward-Euler chain ("convex adaptation"). This is the [adaptive-weight Runge–Kutta method](/methods/adaptive-weight-runge-kutta.md). Every step remains a Runge–Kutta step $(A,\tilde b_n)$, so all linear invariants are preserved, unlike clipping.

Four analytical results back the method. The number of free weights is $s-\operatorname{rank}(G_{\tilde p})$, tabulated for explicit and implicit baselines, and it forces $\tilde p<s$. The error estimate $E_T+\delta$ adds the weight perturbation to the embedded estimate and drives [step-size control](/methods/step-size-control.md). A convex adaptation contains the intersection of its components' [stability regions](/definitions/stability-function.md), so it inherits [A-stability](/properties/a-stability.md). A free adaptation obeys a perturbation bound on $\lvert R(z)\rvert$.

The tests are a $2\times2$ linear [production–destruction system](/definitions/production-destruction-system.md) with [SSP(3,3)](/methods/strong-stability-preserving-runge-kutta.md), a nonlinear four-species system, advection–decay, diffusion, an advection–diffusion–production–destruction PDE and the [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md). With explicit baselines adaptation helps only in a narrow window of steps below the linear-stability limit, where a smaller step is usually cheaper. The authors recommend [diagonally implicit](/methods/diagonally-implicit-runge-kutta.md) baselines and backward-Euler [extrapolation](/methods/extrapolation-methods.md) baselines. For these the linear program is cheap compared with the stage solves, and the step is not stability-limited. [Modified Patankar methods](/methods/modified-patankar-methods.md) appear only as an alternative that escapes the barrier by not being general linear methods. The paper also notes the kinship with [relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md), which also rescale the weights after the stages.

# Version read

arXiv:2005.06268v2 [math.NA], 30 Apr 2021 (title page dated 3 May 2021), the authors' typesetting, 21 pages, all read; pp. 4, 5 and 8 were checked visually. Page 1 matches Crossref; no identity problem. The journal pagination (155–179) differs, and section, equation and figure numbers cited here are those of the arXiv v2. Code and data: reproducibility repository [23] (Zenodo, doi:10.5281/zenodo.3819791).

# Key claims

Notation: the solution is $y$ with $y_n$ at step $n$ (source $u$, $u^n$) and dimension $d$ (source $m$); stage values are $Y_j$ (source $y_j$); $h$ is the step (source $\Delta t$). $\mathsf F\in\mathbb R^{d\times s}$ is the page-local matrix with columns $f(t_n+c_jh,Y_j)$, so $y_{n+1}=y_n+h\mathsf Fb$. $G_p\tilde b=r_p$ collects the order conditions up to order $p$ (page-local; source $Q_p$). $E_T$ is the embedded error estimate (source $\mathrm{err}_T$) and $\mathcal H$ the active set (source $h$). $\tilde b$ are the adapted weights and $\delta=\lVert h\mathsf F(\tilde b-b)\rVert$.

1. Any Runge–Kutta method, or more generally any general linear method, that is unconditionally positivity preserving for all positive ODEs has order $\le1$. (§1, citing Bolley & Crouzeix [3]) **Stated**
2. For ODEs satisfying (1.4) ($y_i=0\Rightarrow f_i(t,y)\ge0$ for all $y\ge0$), backward Euler preserves positivity for any step and forward Euler for small enough $h$. (§1, citing [12]) **Stated**
3. If forward Euler is positive for $h\le h_{\mathrm{FE}}$, any SSP Runge–Kutta method is positive for $h\le\mathcal Ch_{\mathrm{FE}}$. (§1, citing [8]) **Stated**
4. Unconditionally positive diagonally split RK methods exceed order 1 because they are not general linear methods, but are less accurate than backward Euler at large steps; MPRK methods avoid the barrier for the same reason and need a linear solve. (§1, citing [11, 21, 18]) **Stated**
5. Replacing $b$ by $\tilde b$ after the stages turns positivity into the linear constraint $y_n+h\mathsf F\tilde b\ge0$; since the order conditions are linear in $\tilde b$ for fixed $A$, $c$, weight selection with a linear objective is a linear program. (§2, Eqs. (2.4)–(2.7), LP (3.1)) **Derived**
6. Every step is a Runge–Kutta step $(A,\tilde b_n)$, so all linear invariants of the ODE are preserved automatically, unlike orthogonal projection onto the positive orthant [29]. (§§1–2) **Derived** (and shown in §§5.3–5.4: invariants conserved to roundoff)
7. Minimizing the weight deviation $\lVert\tilde b-b\rVert_1$ instead of the solution deviation (projection methods [28, 29]) is computationally much cheaper for large systems. (§2.1) **Stated** (not timed)
8. Example I: SSP(3,3) on $y'=Ly$, $L=\begin{pmatrix}-5&1\\5&-1\end{pmatrix}$, $y_0=(1,0)^\top$, $h=1/3$, gives $y_1=(-1/9,10/9)^\top$; the second-order family $\tilde b=b+\alpha(1/2,1/2,-1)^\top$ is printed as reaching every positive, mass-conserving $y_1$ for $\alpha\in[1/45,2/9]$. (§2.1, Eqs. (2.11)–(2.13)) **Derived** (the printed (2.13) drops the factor $h$; see Printed slips)
9. Example II: Cash–Karp RK5 with $h=0.005$ on the reaction system (2.14) first produces a negative $y_1$ at $t=1.905$, after which the solution diverges; with weights adapted at order 4 it stays positive and qualitatively correct, adaptation being active only for $1.905\le t\le2.63$. (§2.2, Fig. 1) **Shown**
10. Feasibility needs $\operatorname{rank}(G_{\tilde p})<s$; since the quadrature conditions give $\operatorname{rank}(G_p)\ge p$, the reduced order must satisfy $\tilde p<s$. (§3.1; printed "$\tilde p\le s$" there, "$\tilde p<s$" in §4.1 and §6) **Derived**
11. The objective $\lVert\tilde b-b\rVert_1$ returns the original weights when no negative value occurs and penalizes large-magnitude weights. (§3.2) **Derived**
12. Convex adaptation needs no explicit order conditions, since each component method satisfies them; the adapted method has the lowest order among the components. (§3.2, LP (3.2)) **Derived**
13. Active-set reduction: impose positivity only on the components negative in $y_{n+1}$ and enlarge the set with newly negative components; this converged in at most 2 iterations in the authors' examples. (§3.3) **Shown** (asserted from experience)
14. Free weights $s-\operatorname{rank}(G_{\tilde p})$ for $\tilde p=1,2,\dots$ (Table 1): RK4 3/2/0/0; SSPRK(10,4) 9/8/6/4, so 4 at full order; Cash–Karp RK5(4)6 5/4/2/1/0; Dormand–Prince RK5(4)7 6/5/3/1/0. (§4.1, Table 1) **Derived**
15. Table 2: backward Euler 0; Lobatto IIIC4 3/2/1/0/0/0; Radau IIA3 2/1/0/0/0; SDIRK(5,4) 4/3/1/0; TR-BDF2 2/1; BE extrapolation of order 2, 3, 4: 2/1, 5/4/2, 9/8/6/3. Fully implicit methods need a drastic order reduction, SDIRK(5,4) one order, TR-BDF2 and the extrapolation methods none. (§4.1, Table 2) **Derived**
16. For DIRK methods whose first stage is a scaled backward-Euler step, allowing $\tilde p=1$ guarantees feasibility, because backward Euler is unconditionally positive; for explicit methods $\tilde p=1$ guarantees it only for small enough $h$. (§4.1) **Derived**
17. Local error estimate: $\mathrm{err}\le\lVert y(t_{n+1})-y_{n+1}\rVert+\lVert h\mathsf F(\tilde b-b)\rVert\approx E_T+\delta$, with $E_T$ the embedded estimate; a step is rejected if $\delta>\mathrm{tol}_\delta$. (§4.2, Eqs. (4.1)–(4.2), Algorithm 1) **Derived**
18. Theorem 4.1: if $\tilde b=\sum_ig_ib^{i}$ is a convex combination, the stability region of $(A,\tilde b)$ contains the intersection of those of $(A,b^{1}),\dots,(A,b^{m})$; A-stable components give an A-stable adapted method. (§4.3.1) **Proved** (from $R$ being affine in $b$)
19. Lemma 4.2: $\lvert R_{\tilde b}(z)\rvert\le\lvert R_b(z)\rvert+\lVert\tilde b-b\rVert_1\lVert z(I-zA)^{-1}\mathbf 1\rVert_\infty$, which justifies the $\ell^1$ objective as a control on the change of the stability region, particularly for explicit methods. (§4.3.2) **Proved**
20. Advection–decay with Dormand–Prince RK5, $N=100$: the unaltered method is positive for $h\le0.0082$, weights are altered above, and the baseline is unstable for $h>0.016$; at $h=0.015$ adaptation is active for $t\le0.375$; adapted runs (order $\ge4$ or $\ge3$) have errors close to the unaltered fifth-order method. (§5.1, Figs. 4–5) **Shown**
21. For that explicit, cheap-right-hand-side problem a smaller step is generally more efficient than adaptation with the current unoptimized implementation; for the implicit tests adaptation is more efficient than reducing the step. (§5.1) **Shown**/**Stated** (no timings printed)
22. On problems whose exact solution is positive for some data but which violate (1.4), tests "did not show promising results". (§5 intro) **Stated**
23. Diffusion with BE 3 extrapolation, $h=10^{-3}$, discrete-delta data: free adaptation (still order 3) is positive but shows a nonphysical dip at $x=0$ after the first step; convex adaptation with an added first-order embedded method gives a physical solution, at order 1 in the adapted step. Only the first step needs adaptation. (§5.2, Fig. 6) **Shown**
24. Convergence on the diffusion problem: no adaptation is needed for $h<3\times10^{-5}$; free adaptation converges like the unaltered method; convex adaptation has larger errors (slope marked $p=2.3$) but still beats backward Euler at equal cost. (§5.2, Fig. 7) **Shown**
25. Advection–diffusion–production–destruction PDE, BE 3 extrapolation with free adaptation, PI control [10], error (4.2), tolerance $0.01$, $t_{\mathrm{end}}=50$: 264 steps, 72 adapted, all adapted weights still of order 3; $\delta$ is of the size of $E_T$; total mass is conserved to roundoff. (§5.3, Figs. 8–9) **Shown**
26. Stratospheric reaction problem, BE 3 extrapolation with free adaptation and step control, $t\in[12,84]$ h, normalized data: 249 steps, 2 rejected by the error bound, 25 with negative values, $\min y=-1.59\times10^{-11}$; both linear invariants preserved to roundoff. (§5.4, Figs. 10–11) **Shown**
27. Conclusion: the method is mainly of interest for diagonally implicit methods, where the step is not stability-limited and the linear program is cheap; with explicit methods it helps only on a small interval of steps. (§6) **Stated**
28. As $h\to0$ with a positive exact solution, eventually no modification is needed and the unmodified convergence is observed; expected and seen in the examples, not proved. (§4.2) **Shown**

*(Compiler checks, not in the sources.)* With an explicit baseline the right-hand side must be evaluated at possibly negative stage values (the authors suggest $\sqrt{\max(y,0)}$-type guards), which Patankar-type schemes avoid. "Unconditional positivity" here is problem- and data-dependent, since the method changes every step; it is not the fixed-scheme sense of the Patankar literature. No convergence or stability theory covers the sequence of varying methods (admitted in §4.2).

# Printed slips

- **Eq. (2.13) drops the factor $\Delta t$:** printed "$u^1=u^0+\Delta t(f_1,f_2,f_3)\tilde b=\binom{-1/9}{10/9}+\alpha\binom{5}{-5}$". With $h=1/3$ the increment is $\frac{5\alpha}3\binom{1}{-1}$; the printed interval $\alpha\in[1/45,2/9]$ follows the printed formula, while the corrected one gives $[1/15,2/3]$ *(compiler check, not in the sources; checked visually, p. 4)*.
- Eq. (3.3) prints "$u_i^n+\Delta t\sum_{j=0}^{s}F_{i,j}b_j\ge0$": the sum starts at $j=1$ and the weights are $\tilde b_j$.
- Eq. (2.14d) prints "$u_4'=0.05u_2+0.02u_3+0.003u_4$" while (5.5d) prints "$-0.003u_4$"; mass conservation ($u_1'$ contains $+0.003u_4$) requires the minus sign.
- §3.1: "we must take $\tilde p\le s$", where the argument gives $\tilde p<s$ (as §4.1 and §6 state).
- §4.2: $\mathrm{err}_T=\lVert u^n_b-u^n_{\hat b}\rVert$ uses superscript $n$ where $n+1$ is meant.
- Eq. (1.4) uses $n$ for the dimension, (1.1) uses $m$; Theorem 4.1 reuses $m$ for the number of weight vectors.
- §5.2: the semi-discretization writes $d/\Delta x^2$ for the coefficient $D=1$; §5.3 writes "at T = 27" for a time.
- Typos: "shwon" (§5.4), "yield to positive results" (§§5.1–5.2), "Outside of this regions" (§5.3).

# Notation map

| Nüßlein et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u^n$, $t^n$ | $y$, $y_n$, $t_n$ | |
| $m$ | $d$ | dimension; (1.4) writes $n$, Thm. 4.1 reuses $m$ for the number of weight vectors |
| $\Delta t$ | $h$ | |
| $A$, $b$, $c$, $s$ | $A$, $b$, $c$, $s$ | non-autonomous form |
| $y_j$ | $Y_j$ | **stage values; the source's $y$ is not the solution** |
| $f_j$, $F$, $F_{i,j}$ | $f(t_n+c_jh,Y_j)$, $\mathsf F$ (page-local) | **sans-serif, as on the concept page: the registry $F(\tau)$ is the elementary differential** |
| $\tilde b$, $\tilde b_n$, $\tilde u^{n+1}$ | kept | adapted weights and solution |
| $p$, $\tilde p$, $p_{start}$, $p_{min}$ | $p$, kept | design order, reduced order and the loop limits of Algorithm 1 |
| $Q_p$, $r_p$, $v$ | $G_p$, $r_p$, $v$ (page-local) | order-condition matrix and right-hand side; renamed as on the concept page: **$Q$ is the registry SDC collocation matrix** |
| $B=[b^1,\dots,b^K]$, $g$, $K$ | kept, page-local | convex adaptation; **$K$ collides with the registry iteration count** |
| $h$, $h_a$ | $\mathcal H$, $\mathcal H_a$ (page-local) | **active set of constrained components; collides with the registry step $h$** |
| $\alpha$, $\beta$ | kept, page-local | lower and upper bounds; $\alpha$ also the Example I parameter; **not Shu–Osher or multistep coefficients** |
| $\delta$, $\mathrm{err}_T$, $\mathrm{err}$ | $\delta$, $E_T$ (page-local, as on the concept page), $\mathrm{err}_n$ | weight perturbation, embedded estimate, total estimate |
| $\mathrm{tol}_\delta$, $\mathrm{tol}_{error}$, $Tol$ | kept; $\mathrm{rtol}$/$\mathrm{atol}$ | tolerances |
| $R_b(z)=1+zb^T(I-zA)^{-1}e$ | $R(z)$ for weights $b$ | $z=h\lambda$ |
| $e$ | $\mathbf 1$ | |
| "positive" | nonnegative | stated in §1 |
| BE $k$ extrapolation | backward-Euler extrapolation of order $k$ | harmonic step sequence, $s=3,6,10$ stages for $k=2,3,4$ |

# Reference list

32 printed references, numbered [1]–[32]. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` nusslein-2021. [3] is Bolley & Crouzeix (1978), the order barrier for unconditional positivity. [22] is the MOSEK software (2020). [23] is the authors' reproducibility repository with a Zenodo DOI. [17] (NodePy) is a JOSS paper with a URL, and [12] prints a URL with a visit date. arXiv numbers printed beside DOIs ([15], [25], [26], [27], [32]) are recorded as eprints of the published works. [32] (SciPy 1.0) includes the corporate author "SciPy 1.0 Contributors", and its "Vand erPlas" is a kerning artefact for VanderPlas. No printed duplicates; no unparseable item.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Adaptive-weight (positivity-preserving) Runge–Kutta methods](/methods/adaptive-weight-runge-kutta.md)
* [Dormand–Prince 5(4) pair](/methods/dormand-prince-5-4.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Extrapolation methods (Richardson extrapolation of a base integrator)](/methods/extrapolation-methods.md)
* [Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)](/methods/modified-patankar-methods.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Production–destruction systems](/definitions/production-destruction-system.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
