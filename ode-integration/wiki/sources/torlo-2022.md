---
type: Source
title: "Torlo et al. (2022) — Issues with positivity-preserving Patankar-type schemes"
description: "Analyses modified Patankar Runge–Kutta and deferred-correction schemes on a linear two-species production–destruction system, proving they preserve steady states but oscillate above order-one step bounds and lose order when an initial constituent vanishes, and proposes a three-stage second-order MPRK(3,2)."
resource: "doi:10.1016/j.apnum.2022.07.014"
source_kind: paper
authors: [Torlo D., Öffner P., Ranocha H.]
year: 2022
venue: "Appl. Numer. Math. 182:117-147"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Applied_Numerical_Mathematics_Torlo_Issues_with_positivity-preserving_Patankar-type_schemes.pdf"
tags: [positivity, structure-preserving, stiff, order-reduction, stability]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

[Modified Patankar methods](/methods/modified-patankar-methods.md) are linearly implicit modifications of explicit Runge–Kutta or [deferred-correction](/methods/deferred-correction.md) schemes for [production–destruction systems](/definitions/production-destruction-system.md). They are unconditionally positive and, in the "modified" variants, conservative. The paper studies MPE, MPRK(2,2,$\alpha$), MPRK(4,3,$\alpha,\beta$), MPRKSO(2,2) and (4,3), mPDeC and the semi-implicit SI-RK2/3. It first proves that all of them preserve steady states exactly. It then names two failure modes and analyses both on the conservative linear system $y_1'=-\theta y_1+(1-\theta)y_2$, $y_2'=\theta y_1-(1-\theta)y_2$ with $y_0=(1-\varepsilon,\varepsilon)$.

**Spurious oscillations.** For a linear method, not overshooting the steady state is equivalent to $R(-h)>0$ for the [stability function](/definitions/stability-function.md), and a table gives this bound for many implicit methods. Patankar schemes are nonlinear, so [positivity](/properties/positivity-preservation.md) does not make them oscillation-free. For MPRK(2,2,1), which equals mPDeC2, the sharp bound $h\le2$ is proved; numerical scans give the bounds of all other schemes. Most bounds are close to 1, and Gauss–Lobatto mPDeC has bound 1 from order 6 on.

**Order loss for vanishing data.** When $\varepsilon\to0$ with $\varepsilon/h\to0$, Patankar weights built from fractional powers of stage values degenerate. This is a new kind of [order reduction](/definitions/order-reduction.md), and the limits $h\to0$ and $\varepsilon\to0$ do not commute. MPRK(2,2,$\alpha>1$) makes the initial state a spurious steady state and drops to first order. Several third-order schemes drop to order 1 or 2. mPDeC drops to order 2, or to order 1 when a final correction weight is negative.

The paper also proposes MPRK(3,2), built on [SSPRK(3,3)](/methods/strong-stability-preserving-runge-kutta.md). It has the largest oscillation-free bound found, about 16.56, keeps second order for vanishing data and moves in the correct direction. The linear predictions are checked on the [Robertson problem](/benchmarks/robertson-problem.md), on HIRES and, in the supplement, on a scalar nonlinear ODE. The evidence mixes proofs (MPRK(2,2,1), the Runge–Kutta bounds, steady-state preservation), symbolic Mathematica expansions and numerical scans.

# Version read

arXiv:2108.07347v5 [math.NA], 8 Aug 2022 (title page dated 9 Aug 2022), not the version of record. The file holds the main text (pp. 1–39, refs [1]–[47]) and the Supplementary Material (pp. 40–69, numbered S1–S30, with its own sections, equations, figures and refs [S1]–[S12]); all 69 pages read, the late supplement pages being mostly HIRES figure panels. Page 1 matches Crossref; no identity problem. Numbering cited here is that of the arXiv v5.

# Key claims

Notation: the solution is $y$, components $y_i$, step $n$ written $y^n_i$ as in the registry's Patankar convention (source $u$); $h$ is the step (source $\Delta t$; on the test system (12) it is measured in units of $1/(a+b)$); stage values are $Y_s$ (source $y^s$); $r_i$ is the source's non-weighted "rest" term; Patankar weight denominators are $\varpi_i$ (source $\sigma_i$). $\theta$ and $\varepsilon$ are the test-system parameter and the small initial constituent (page-local). mPDeC subnode values are $Y^{(k)}_m$ on $\mathsf M$ subintervals with $K$ corrections and weights $\omega_{mr}$ (source $y^{m,(k)}$, $M$, $\theta^m_r$). $\Theta(\cdot)$ is the Landau symbol of exact order.

1. MPE applied to a positive conservative linear PDS coincides with implicit Euler, and Patankar–Euler coincides with implicit Euler on $y'=\lambda y$, $\lambda<0$. (§2.1) **Derived**
2. MPE is positive because its system matrix is an M-matrix (positive diagonal, nonpositive off-diagonal, strictly diagonally dominant) with a positive right-hand side. (§2.1, citing Axelsson [3]) **Stated**
3. All schemes considered (MPE, MPRK(2,2,$\alpha$), MPRK(4,3,$\alpha,\beta$), MPRKSO, mPDeC, MPRK(3,2), SI-RK2/3) are steady-state preserving: $y^n=y^*$ with $f(y^*)=0$ gives $y^{n+1}=y^*$. IMEX modifications of explicit RK are "not necessarily" so [10]. (Def. 2.2, Prop. 2.3) **Proved**
4. For a linear (Runge–Kutta) method on (12) with $\varepsilon<\theta$, not overshooting the steady state is equivalent to positivity of the Dahlquist mode $v_1=\theta y_1-(1-\theta)y_2$, $v_1'=-v_1$. (Prop. 4.3) **Proved**
5. A Runge–Kutta method satisfies Property 4.1 (no overshoot) on (12) for a given $h$ iff $R(-h)>0$, and Property 4.2 (correct direction) iff $1-R(-h)>0\iff b^\top(I+hA)^{-1}\mathbf 1>0$; every A-stable scheme satisfies Property 4.2 for all $h$. (Props. 4.4, 4.6, Eqs. (23), (27), (28)) **Proved**
6. Conditions for $R(-h)>0$ (Table 1): Radau IA3 and IIA3 $h<3$; Radau IA5, IIA5, Lobatto IIIA4 and IIIB4 always; Lobatto IIIA2 and IIIB2 $h<2$; Lobatto IIIC2 always; Lobatto IIIC4 $h<4$; Gauss–Legendre 4 always; Gauss–Legendre 6 $h\lesssim4.32$; implicit Euler always; implicit midpoint and trapezoid $h<2$; Qin–Zhang DIRK2 $h\ne4$; TR-BDF2 $h<1+\sqrt2$; Kraaijevanger–Spijker DIRK2 always. (Table 1, Mathematica notebook [46]) **Shown** (symbolic computation)
7. Among linear schemes only first-order ones can be unconditionally positive in all stages, $(I+hA)^{-1}\ge0$ for all $h$; Radau IIA5 is not positive in all stages but is unconditionally positive in the final update. (Remark 4.5, citing [6, 15]) **Stated**
8. Modified Patankar schemes are nonlinear, so Prop. 4.3 fails for them: they are unconditionally positive but not unconditionally oscillation-free. (§4, end) **Stated**, then **Shown** in §6
9. Theorem 4.7: mPDeC2 = MPRK(2,2,1) satisfies Properties 4.1 and 4.2 on (12) for all $0<\varepsilon<1$, $0\le\theta\le1$ when $h\le2$; for the general system (11) the bound is $h\le2/(a+b)$; it is sharp as $\theta,\varepsilon\to0$. (§4.1, Eqs. (29)–(30)) **Proved** (cubic-root argument; the discriminant sign of Remark 4.8 checked in Mathematica)
10. MPRK(2,2,$\alpha$) with $\alpha\le1$ always moves in the correct direction on (12), for all $h>0$ (Thm. B.2); so do MPE (Thm. B.1) and MPRKSO(2,2,$\alpha,\beta$) with nonnegative coefficients and $\gamma\ge1$ (Thm. B.3). **Proved**
11. For vanishing initial data the relevant limit is $h\to0$ with $\varepsilon/h\to0$, coupling two parameters as in stiff order reduction; the classical order results, which fix $y^0_i\ge\varepsilon>0$, do not hold in it. (§5, Eq. (40)) **Stated**
12. MPRK(2,2,$\alpha$) for vanishing data: $\alpha=1$ gives first-step error $\Theta(h^3)$ and final error $\Theta(h^2)$; $\alpha>1$ gives $\Theta(h)$ at both, the initial state acting as a spurious steady state for some steps; $\tfrac12\le\alpha<1$ gives $\Theta(h^2)$ at both. (Eq. (45), Thm. 5.4, Table 2) **Proved** (asymptotic Landau-symbol argument)
13. Lemma 5.2: if a stage denominator is $\varpi=\Theta(\eta)$ with $\eta/h^2\to0$, the stage value is $\Theta(\eta/h)$, a zeroth-order error $\Theta(h)$. Lemma 5.3: if $1/\varpi=\Theta(\eta)$, the stage is at most first-order accurate, error $\Theta(h^2)$ ($\eta$ a generic small quantity). (§5.1) **Proved**
14. Table 2, first-step / final errors for vanishing data: MPRK(4,3,$\alpha,\beta$) with exponent $q>1$: $\Theta(h)$/$\Theta(h)$; with $p>1$, $q\le1$: $\Theta(h^2)$/$\Theta(h^2)$; with $p\le1$, $q\le1$, $pq\ne1$: $\Theta(h^3)$/$\Theta(h^3)$; with $p=q=1$: $\Theta(h^4)$/$\Theta(h^3)$ (here $p$, $q$ are the Patankar exponents, not orders). MPRKSO(2,2,$\alpha,\beta$): $\gamma<1$ $\Theta(h)$/$\Theta(h)$, $\gamma=1$ $\Theta(h^3)$/$\Theta(h^2)$, $\gamma>1$ $\Theta(h^2)$/$\Theta(h^2)$. MPRKSO(4,3): $\Theta(h^2)$/$\Theta(h^2)$. MPRK(3,2), SI-RK2, SI-RK3: $\Theta(h^3)$/$\Theta(h^2)$. mPDeC equispaced with nonnegative final weights, and Gauss–Lobatto mPDeC of any order: $\Theta(h^2)$/$\Theta(h^2)$; equispaced with a negative final weight (orders above 8 only): $\Theta(h)$/$\Theta(h)$. (Table 2, Thm. 5.4) **Proved**/**Derived**
15. Theorem 5.5: for vanishing data, mPDeC is of order 2 if some correction weight $\omega_{mr}<0$ with $m\in\{1,\dots,\mathsf M-1\}$, and of order 1 if some $\omega_{\mathsf Mr}<0$; a negative weight carries the vanishing state through the iterations (Prop. 5.6). **Proved**
16. mPDeC3 first-step error, $h$-expansion first: $(-\tfrac1{13824\varepsilon^2}-\tfrac5{1152\varepsilon}+\tfrac{1789}{13824}-\dots)h^4+\mathcal O(h^5)$; taking $\varepsilon\to0$ first gives $-h^2/6+\dots$, a first-step error $\mathcal O(h^2)$ and global second order. (§5, end; supplement §2.2) **Shown** (symbolic)
17. Oscillation-free bounds from the scan over $\varepsilon,\theta$ ($h\in[2^{-6},2^6]$, tolerance $5\times$ machine epsilon): mPDeC equispaced, orders 1–16: $\infty$, 2.0, 1.19, 1.11, 1.07, 1.04, 1.04, 1.37, 6.96, 1.0, 15.5, 1.0, 35.51, 1.07, 12.13, 1.80; mPDeC Gauss–Lobatto: $\infty$, 2.0, 1.19, 1.07, 1.04, then 1.0 for orders 6–16; MPRKSO(4,3) 1.31; SI-RK2 1.41; SI-RK3 1.27; MPRK(3,2) 16.56; implicit midpoint 2.0, trapezoid 2.0, TR-BDF2 2.4, Radau IIA3 3.0, Radau IIA5 $\infty$. (Fig. 6a–d) **Shown**
18. MPRK(2,2,$\alpha$): the bound is 1 for $\alpha<1$, 2 for $\alpha=1$, and grows for $\alpha>1$ (labels 0.57 to 16.00); the schemes with large bounds are exactly those that lose accuracy as $\varepsilon\to0$. (§6, Fig. 5b) **Shown**
19. MPRK(4,3,$\alpha,\beta$): the bound is large near the curve $\beta(6\alpha-3)=3\alpha-2$, a boundary of the nonnegative-coefficient region [28], but every scheme on it is only first order for vanishing data. (§6, Figs. 4a, 6c) **Shown**
20. MPRK(3,2) "has maybe the best conditions of all the schemes": bound about 16.56, second order kept for vanishing data, correct direction (checked in a notebook). (§6, App. B.1) **Shown**
21. Equispaced mPDeC reduces to first order for order 9 and orders $\ge11$, where some final weight is negative; Gauss–Lobatto mPDeC reduces only to order 2 at every order, and its bound is 1 at high order. (§6) **Shown**
22. Robertson problem, 20 exponentially growing steps, zero data replaced by $10^{-180}$: MPRK(2,2,$\alpha>1$), MPRK(4,3,10,0.5), MPRKSO(2,2,0.001,10) and equispaced mPDeC11, all first order for vanishing data, miss the evolution of $y_2$ and sometimes $y_3$; SI-RK2 and SI-RK3 "go to infinity" because they are not conservative. (§7.1, Fig. 7) **Shown**
23. HIRES with $10^3$ uniform steps, zeros replaced by $10^{-35}$, reference mPDeC5 with $10^5$ steps: MPRK(2,2,5) misses $y_2,y_3,y_5,y_9$ while MPRK(2,2,1) is accurate; Gauss–Lobatto mPDeC6 captures the late reaction of $y_7,y_8$; MPRKSO(2,2,0,8) shows the spurious steady state; MPRKSO(2,2,0.3,2) oscillates until refined. (§7.2, Fig. 8) **Shown**
24. On $y'=-k\lvert y\rvert y+1$ ($k=10^4$, $h=\nu/(1.1\sqrt k)$) the linear bounds "can mostly be transferred"; exceptions are MPRK(2,2,$\alpha$), oscillating from $\nu=2$, MPRKSO(2,2,0,$\beta$), oscillating despite large linear bounds, and MPRK(3,2), with a small oscillation at $\nu=2$ only. (Supplement §4.1, Tables S1–S6) **Shown**
25. Diagonally split RK methods can be unconditionally positive but are less accurate than implicit Euler at large steps; general linear methods of order $\ge2$ are only conditionally positive [6]. (§1) **Stated**
26. Higher-order MPRK schemes need more stages than classical Runge–Kutta methods of the same order, consistent with Kopecz–Meister [27] on three-stage third-order MPRK. (Remark 2.1) **Stated**

*(Compiler checks, not in the sources.)* The paper qualifies rather than contradicts the classical order proofs of [26, 28, 19, 20, 37], which fix $\varepsilon>0$ (supplement Remark 2.4). Its oscillation bounds concern monotone approach to the steady state, a different notion from the Lyapunov stability of Izgin, Kopecz & Meister [22], by which MPRK22($\alpha$) is stable for all $h>0$ (Remark 1.4). MPRK(3,2) is second order by a heuristic argument and symbolic expansions on one linear problem; no general order proof is given. The word "order" is used both for local first-step order and for global order (see Printed slips).

# Printed slips

- Eq. (6) prints the initial condition "$u(0)=u_0=(0.1,0)^T$", while the Fig. 1 caption says "$u_0=(1,10^{-250})^T$" and the plotted $u_2$ reaches about 0.5, which fits unit mass.
- §5, p. 22: "MPRK(3,4,2,0.5)" is MPRK(4,3,2,0.5), the scheme of Fig. 2; the same sentence's "$p=3$" recomputes from the printed formulas to $p\approx2.67$ (compiler check; the conclusion $p,q>1$ is unaffected).
- Same paragraph: "$\Delta t\lesssim\varepsilon^{1/3}\approx10^{-3.3}$" requires $\varepsilon=10^{-10}$, while Fig. 2 uses $\varepsilon\in\{10^{-2},10^{-16},10^{-250}\}$.
- MPRKSO(4,3) coefficients (App. A and supplement): "$\eta_3$" is printed twice, $0.1868649805549811$ and $2.224876040351123$; the second is evidently $\eta_4$. The supplement's final update prints $b_{32}p_{ij}(y^2)$ where App. A has $y^3$.
- MPRK(4,3) nonnegativity region: App. A prints "$1/2\le\alpha<2/3$" for the first branch, the supplement "$1/3\le\alpha<2/3$".
- Supplement Thm. 2.3 says MPRK(2,2,$\alpha$), $\alpha\in[0.5,1)$, "reduces to 1", while Thm. 5.4 and Table 2 give a global $\Theta(\Delta t^2)$ error; likewise for mPDeC3. The two use "order" in the local and global senses.
- Supplement Eq. (12): the left side "$\lim_{\varepsilon\to0}u_2^1(\varepsilon)$" should be $u_1^1$, whose expansion the right side is.
- Supplement Tables S1–S6: the header lists 7 CFL values, each row has 8 entries.
- §2.3 announces "in the next section … an example of such inversion"; none follows.
- §6: "a time step restriction of unity for orders four and higher" for Gauss–Lobatto mPDeC, but Fig. 6a gives 1.07 and 1.04 at orders 4 and 5.
- Ref. [11] prints this paper's own arXiv URL (2108.07347) beside "arXiv: 2110.13509"; ref. [16] is a garbled catalogue entry for Hairer–Nørsett–Wanner.
- Typos: "introduce" for "introduced" (§1), "Nonparamteric" (Fig. 6b).

# Notation map

| Torlo et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u^n$, $u_i^n$, $t^n$ | $y$, $y_n$, $y^n_i$, $t_n$ | component-and-step superscript as in the registry's Patankar entry |
| $\Delta t$ | $h$ | on (12) in units of $1/(a+b)$ |
| $p_{ij}$, $d_{ij}$, $I$ | $p_{ij}$, $d_{ij}$, kept | production and destruction; $I$ the index set of constituents |
| $r_i$ | kept, page-local | rest (source) term of a PDRS, not Patankar-weighted |
| $\tilde p_{ij}=p_{ij}/u_j$, $\tilde d_{ij}=d_{ij}/u_i$ | kept | rates; constant for a linear PDS |
| $y^s$, $y_i^s$ | $Y_s$, $Y_{s,i}$ | **stage values; the source's $y$ is not the solution**; $Y_1=y_n$ |
| $\sigma_i$, $\sigma_i^j$ | $\varpi_i$ | Patankar weight denominators; $\varrho_i$, $\mu_i$, $\tilde a_i$ of MPRKSO(4,3) kept as auxiliary stages |
| $y^{m,(k)}$, $M$, $K$ | $Y^{(k)}_m$, $\mathsf M$, $K$ | mPDeC subnode values, subintervals, corrections |
| $\theta^m_r$ | $\omega_{mr}$ | DeC weights normalized to the unit interval; **the source's $\theta$ also names the test parameter** |
| $\gamma(j,i,\theta)$ | $\varsigma(j,i)$ (page-local) | index selector swapping production and destruction for negative weights, as on [modified Patankar methods](/methods/modified-patankar-methods.md); **renamed: the registry $\gamma$ is the tree density** |
| $\theta$ | kept, page-local | test parameter, $a=\theta$, $b=1-\theta$, steady state $y_2^*=\theta$ |
| $\varepsilon$ | kept, page-local | small initial constituent $y^0_2$; **not the registry stiffness parameter**, though it plays a comparable role |
| $M$ (§3) | $L$ | **system matrix of (12); the registry $M$ is the mass matrix** |
| $L$, $\Lambda$, $v$ | $V$, $\Lambda$, $v$ (page-local) | **diagonalizer renamed: the registry $L$ is the linear operator**; $v_1$ Dahlquist mode, $v_2$ conserved sum |
| $R(z)$, $A$, $b$, $c$, $\mathbf 1$ | same | evaluated at $z=-h$ |
| $\alpha$ (MPRK(2,2,$\alpha$)) | kept, $=c_2$ | **$\alpha,\beta$ of MPRK(4,3) are $c_2,c_3$, and of MPRKSO Shu–Osher parameters, not the registry $\alpha_{ij}$, $\beta_{ij}$** |
| $p$, $q$ (MPRK(4,3)) | kept, page-local | Patankar exponents $p=3a_{21}(a_{31}+a_{32})b_3$, $q=a_{21}$; **collide with the order $p$, stage order $q$ and $p_{ij}$** |
| $\gamma$ (MPRKSO) | kept, page-local | weight exponent; **not the Rosenbrock $\gamma$** |
| $\eta$ | kept, page-local | generic small quantity; **not the registry entropy** |
| $\Theta(\cdot)$ | kept | exact-order Landau symbol |
| CFL (supplement) | $\nu$ | $h=\nu/C(k)$, $C(k)=1.1\sqrt k$ |

# Reference list

47 printed references in the main text, numbered [1]–[47], and 12 in the supplement, [S1]–[S12]. Eleven supplement items repeat main-list entries; only [S12] (Wolfram Research, Mathematica 12.0, 2019) is new. The 48 distinct works are merged complete into the [bibliography](/bibliography.md) with `citedby` torlo-2022. [36] is the ingested source [Nüßlein et al. (2021)](/sources/nusslein-2021.md). [11] is the arXiv preprint of [Ciallella et al. (2022)](/sources/ciallella-2022.md), kept as its own entry (ciallella-2021), and prints this paper's own arXiv URL beside the right eprint number. [22] and [23] are arXiv preprints by Izgin, Kopecz & Meister, kept as their own entries (izgin-2022-b, izgin-2022-c), distinct from their published versions izgin-2022 (ESAIM: M2AN) and izgin-2022-d (SIAM J. Numer. Anal.). [46] is the authors' reproducibility repository (torlo-2021) and [47] the arXiv preprint of this paper itself, cited for its supplement (torlo-2021-b). [16] is a garbled catalogue entry for the Hairer–Nørsett–Wanner nonstiff volume, merged as printed (hairer-2000, 2000 printing). [25] prints no pages, [27] no volume, [29] neither.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Lyapunov stability of steady states of positive, conservative time integrators](/results/lyapunov-stability-positive-conservative-schemes.md)
* [Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)](/methods/modified-patankar-methods.md)
* [Order reduction](/definitions/order-reduction.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Production–destruction systems](/definitions/production-destruction-system.md)
* [Robertson problem](/benchmarks/robertson-problem.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
