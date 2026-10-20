---
type: Source
title: "Buvoli et al. (2026) — Multirate Runge–Kutta for Nonlinearly Partitioned Systems"
description: "Defines multirate nonlinearly partitioned Runge–Kutta (MR-NPRK) methods as NPRK methods whose reduced underlying methods have different stage counts, classifies their timescale coupling, proves a sufficient condition for L-stability in the stiff limit, and builds implicitly wrapped IMEX methods of orders 2 and 3 around any explicit Runge–Kutta method."
resource: "doi:10.1137/25m1747373"
source_kind: paper
authors: [Buvoli T., Tran B.K., Southworth B.S.]
year: 2026
venue: "SIAM J. Sci. Comput. 48:A2884-A2909"
local_file: "/home/stefano/papers/mosaic/ode-integration/2026_Crossref_SIAM_Journal_on_Scientific_Computing_Buvoli_Multirate_RungeKutta_for_Nonlinearly_Partitioned_Systems.pdf"
tags: [multirate, imex, runge-kutta, order-conditions, stability]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

Multirate Runge–Kutta (GARK-type) and multirate infinitesimal methods assume that the fast and slow scales separate linearly, additively or by components. In thermal radiation transport and radiation hydrodynamics, material coefficients that interact with stiff processes depend on non-stiff variables, so neither partition is natural. The paper extends multirating to the nonlinear partitions $f(y)=F(y,y)$ of [nonlinearly partitioned Runge–Kutta (NPRK) methods](/methods/nonlinearly-partitioned-runge-kutta.md).

An NPRK method is multirate (MR-NPRK) when its two reduced underlying Runge–Kutta methods, obtained when $F$ depends on one argument only, have different numbers of stages. No new method class is needed. Timescale coupling is classified as fully decoupled, $1\to2$, $2\to1$ or fully coupled through the irreducible stage index sets, each with an implied tensor sparsity. Up to order 3 the [order conditions](/results/runge-kutta-order-conditions.md) are the additive ones plus a single nonlinear coupling condition.

Linear stability uses the partitioned Dahlquist problem and the additive stability function $R(z_1,z_2)$, extending the [joint stability regions of multirate methods](/definitions/multirate-linear-stability.md). Theorem 3.2 gives sufficient conditions for L-stability in the stiff $z_1$ limit: fully decoupled or $1\to2$ coupling, stiff accuracy, and a reduced implicit method that is a DIRK with nonzero diagonal. The authors show that this property loses practical value as the number of explicit stages grows.

Implicitly wrapped IMEX MR-NPRK methods put one or two implicit stages before, and one after, an arbitrary explicit Runge–Kutta method. Order 2 uses an SDIRK with $\gamma=(2\pm\sqrt2)/2$, and order 3 Butcher's L-stable three-stage SDIRK. Apart from the implicit solves, a step is one explicit step of a modified ODE $w'=F(Y_2,w)$, and a base method composed $m$ times gives many explicit stages.

The test is [Burgers](/benchmarks/burgers-equation.md) with nonlinear diffusion and WENO advection, under a semi-implicit partition that needs only linear solves. The methods reach orders 2 and 3, are more accurate than single-rate IMEX-NPRK at a fixed step, stay stable at larger steps than explicit SSP methods, and are about four times faster than single-rate NPRK at moderate precision.

# Version read

arXiv:2504.03257v1 [math.NA], 4 Apr 2025, the SIAM-style submitted manuscript ("Submitted to the editors DATE."), not the version of record. It has 41 PDF pages: 26 of main text (with Appendix A and references) and 15 of supplementary materials (SM1–SM15), all read. No DOI is printed. Page 1 prints "Runge-Kutta" with a hyphen; title and authors otherwise match Crossref. The 26 main pages match the published range A2884–A2909, but the published content was not seen. Section, equation, table and SM numbers cited here are those of arXiv v1.

# Key claims

Notation: $f(y)=F(y,y)$ (source $G$). The first argument of $F$ is implicit and the second explicit. $(A^{\{r\}},b^{\{r\}},c^{\{r\}})$, $r=1,2$, are the underlying methods, and $(\hat a^{\{r\}},\hat b^{\{r\}},\hat c^{\{r\}})$ their reduced tableaux (source hats kept). $\mathcal S^{\{r\}}$ are the irreducible stage index sets with sizes $s^{\{r\}}$. $z_r=h\lambda_r$, and $\gamma$ is an SDIRK diagonal (source $\lambda$ in §3.2.2).

1. Existing multirate methods (multirate GARK and multirate infinitesimal) target additive or component partitions and assume a linear separation of scales. This fails for radiation transport and radiation hydrodynamics, where coefficients interacting with stiff processes depend on non-stiff variables and energy balance prohibits component partitioning. (Introduction, pp. 1–2) **Stated**
2. $F(u,v)$ is a nonlinear partition of $f$ if $F(y,y)=f(y)$ for all $y$; NPRK methods (1.5) replace $a_{ij}$, $b_j$ by a third-order tensor $a_{ijk}$ and a weight matrix $b_{ij}$. (§1, Eqs. (1.2), (1.5)) **Stated** (background from [7, 35])
3. Every NPRK method has two underlying methods, $a^{\{1\}}_{ij}=\sum_ka_{ijk}$, $b^{\{1\}}_i=\sum_jb_{ij}$ and $a^{\{2\}}_{ik}=\sum_ja_{ijk}$, $b^{\{2\}}_j=\sum_ib_{ij}$, with $c^{\{1\}}=c^{\{2\}}$. (Def. 1.1, Eqs. (1.6)–(1.7)) **Derived**
4. NPRK reduces to an additive method for $F(u,v)=f^{\{1\}}(u)+f^{\{2\}}(v)$ and to a partitioned method for a component partition (1.9), so every MR-NPRK method is also a multirate additive and a multirate partitioned method. (§1.2) **Derived**
5. An irreducible NPRK method can have reducible underlying methods (Remark 2.2); MR-NPRK means an NPRK method whose reduced underlying methods have $s^{\{1\}}\ne s^{\{2\}}$. (Defs. 2.3, 2.6) **Stated** (definition)
6. Example 2.4: a four-stage first-order IMEX MR-NPRK method reduces to one backward Euler step for $F=f(u)$ and to three forward Euler steps of size $h/3$ for $F=f(v)$, with $\mathcal S^{\{1\}}=\{4\}$, $\mathcal S^{\{2\}}=\{1,2,3\}$; it is fully coupled. (Eqs. (2.2)–(2.3), Examples 2.7, 2.9) **Derived**
7. The four timescale couplings (fully decoupled, $1\to2$, $2\to1$, fully coupled) are characterized by their allowed argument evaluations (Fig. 1) and imply tensor sparsity (Table 1; proof SM A.2). If $\mathcal S^{\{1\}}\cap\mathcal S^{\{2\}}\ne\emptyset$ the method is fully coupled (Prop. SM A.2), so methods that are not fully coupled have disjoint stage sets (Cor. SM A.3). **Proved**
8. The order conditions of MR-NPRK are those of NPRK (edge-colored rooted trees [35]), with summation sets reduced by sparsity. Up to order 3 they are the additive conditions plus one nonlinear coupling condition for the tree $F_{12}[F,F]$ ($\gamma(\tau)=3$), which is "not possible" to write in terms of the underlying methods. (§2.2, Table 2, App. B) **Derived**
9. A NPRK method is second order iff both underlying methods are second order (from [35]). (SM C.1, before (C.5)) **Stated**
10. On the partitioned Dahlquist problem $y'=F(y,y)$, $F(u,v)=\lambda_1u+\lambda_2v$, the NPRK stability function is the additive one, $R(z_1,z_2)=\det(I-z_1A^{\{1\}}-z_2A^{\{2\}}+\mathbf 1(z_1b^{\{1\}}+z_2b^{\{2\}})^\top)/\det(I-z_1A^{\{1\}}-z_2A^{\{2\}})$. (§2.3.2, Eq. (2.7)) **Derived**
11. Because spectra of real discretizations are conjugate-symmetric, the relevant region is $\mathcal P=\{(z_1,z_2):\max(\lvert R(z_1,z_2)\rvert,\lvert R(\bar z_1,z_2)\rvert)\le1\}$, shown as slices $\mathcal P(z_1)$; $\arg z_1=\pi/2$ models skew-symmetric advection and $\arg z_1=\pi$ symmetric positive definite diffusion. (Eqs. (2.8)–(2.10)) **Stated**
12. No IMEX NPRK method can be A-stable, since $R(0,z_2)$ is the stability function of an explicit Runge–Kutta method. (§3.1) **Derived**
13. Theorem 3.2: an IMEX MR-NPRK method is L-stable in the stiff $z_1$ limit, $\lim_{\lvert z_1\rvert\to\infty}R(z_1,z_2)=0$, if it is (i) fully decoupled or $1\to2$ coupled, (ii) stiffly accurate, and (iii) its reduced implicit method is a DIRK with nonzero diagonal. The denominator is $\prod_{i=1}^{s^{\{1\}}}(1-z_1\hat a^{\{1\}}_{ii})$, of degree $s^{\{1\}}$; a permutation and block-determinant argument bounds the numerator degree in $z_1$ by $s^{\{1\}}-1$. (Thm 3.2, App. A.2, Props. A.3–A.4, Lemma A.5) **Proved**
14. Numerator degree bounds (Prop. A.4): the degree in $z_1$ is at most $s^{\{1\}}$ (fully decoupled, $1\to2$) or $s$ ($2\to1$, fully coupled); in $z_2$ at most $s^{\{2\}}$ (fully decoupled, $2\to1$) or $s$ ($1\to2$, fully coupled). **Proved**
15. Lemma A.5: a diagonally implicit, stiffly accurate IMEX MR-NPRK method has its last stage index $s\in\mathcal S^{\{1\}}$. **Proved**
16. The practical value of L-stability in the stiff $z_1$ limit decreases as $s^{\{2\}}$ grows: damping occurs asymptotically only if $\lvert z_1\rvert\gg\lvert z_2\rvert^{s^{\{2\}}/s^{\{1\}}}$, and methods with $s^{\{2\}}\gg s^{\{1\}}$ must still step within the explicit stability region, which grows only linearly in $s^{\{2\}}$. (§3.1.1) **Derived**
17. The fully coupled first-order method (3.3) ($s^{\{2\}}$ forward Euler substeps and backward Euler) is "mildly unstable" in the stiff $z_1$ limit: $\lim_{z_1\to\infty}R=\sum_{j=1}^{s^{\{2\}}}c_jz_2^j$, unbounded as $z_2\to\infty$. The fully decoupled method (3.5), whose implicit part is a two-stage L-stable DIRK with final implicit weight $3/4$, is L-stable in that limit. (Eqs. (3.3)–(3.5)) **Derived**
18. For $s^{\{2\}}=4$ method (3.5) has much larger slices $\mathcal P(z_1)$ than (3.3), but for $s^{\{2\}}=32$ and $z_1=-10000$ the improvement is minor, although $z_1$ is more than 100 times stiffer than the explicit component; the explicit region $\mathcal P(0)$ grows linearly with $s^{\{2\}}$. (§3.1.1, Fig. 2) **Shown**
19. The second-order implicitly wrapped MR-NPRK method (3.6) has $s=s^{\{2\}}+2$ stages, implicit stages 2 and $s$ only, and any explicit method of order $\ge2$. An SDIRK implicit part requires $a_{2,2,1}=a_{s,s,s-1}=(2\pm\sqrt2)/2$; the minus sign gives the smaller error and the plus sign more damping. The method is fully decoupled and stiffly accurate. (§3.2.1, Eqs. (3.6)–(3.7), App. C.1) **Derived**
20. The third-order implicitly wrapped MR-NPRK method (3.9)/Table 3 has $s=s^{\{2\}}+3$ stages and implicit stages 2, 3 and $s$. Its implicit underlying method is the L-stable three-stage stiffly accurate SDIRK (3.8) with $\gamma=0.43586652150845899941601945119356$. The coupling coefficient is $a_{3,2,2}\approx0.18253672044687517980951745313830$ ($\omega=1$) or $\approx-0.2533298010615838196065019980553$ ($\omega=2$). The method is $1\to2$ coupled and stiffly accurate. (§3.2.2, Table 3, App. C.2) **Derived**
21. Given third-order underlying implicit and explicit methods, exactly three order conditions remain for the third-order ansatz (C.18), each solvable by one free parameter: $a_{3,2,2}$, one coefficient in the explicit stages, one in the final stage. (App. C.2, (C.18)–(C.19)) **Derived**
22. Remark 3.3: for any explicit method with $\lim_{s^{\{2\}}\to\infty}\lvert\hat b^{\{2\}}_{s^{\{2\}}}\rvert=0$, such as any composite tableau (3.13), the coefficient $a_{s^{\{2\}}+2,3,s^{\{2\}}+1}=(1-3\hat c^{\{1\}}_1)/(6\hat b^{\{2\}}_{s^{\{2\}}}(\hat c^{\{1\}}_2-\hat c^{\{1\}}_1))$ becomes unbounded. An alternative third-order method with bounded coefficients (C.46, Table SM4) costs twice the explicit function evaluations. (Remark 3.3, App. C.3–C.4) **Derived**
23. Composing an $s$-stage explicit method $m$ times gives an $sm$-stage explicit method (3.13) with the storage of the base method. (§3.2.3) **Stated**
24. Implicitly wrapped methods need only implicit solves in the first argument of $F$ and explicit integration of $w'=f(c,w)$ for fixed $c$; apart from the solves, a step is one explicit step of a modified ODE, and the low storage of the explicit method is kept. (§3.2) **Derived**
25. For Burgers with nonlinear diffusion (4.1), the nonlinear partition (4.3) treats advection explicitly and nonlinear diffusion semi-implicitly, with its coefficient frozen at $v$, so only linear solves are needed; an additive partition would need nonlinear solves and a component partition an implicit WENO. (§4.1) **Stated**
26. MR-NPRK methods converge at their expected orders (2 and 3) and are more efficient than both single-rate IMEX-NPRK and explicit SSP methods. (§4.4, Fig. 4) **Shown**
27. With an implicit solve four times as expensive as a function evaluation, MR-NPRK at a fixed step is consistently more accurate than single-rate NPRK and stays stable at much larger steps; explicit SSP methods are unstable at coarse steps because of the diffusion stiffness. (§4.4) **Shown** (no hardware stated)
28. With two Gaussian pulses all implicitly wrapped MR-NPRK methods reach almost exactly the accuracy of the underlying explicit integrator; with three, one inside the diffusive region, multirating improves the error much less, because diffusion is still stepped with the full step. (§4.4) **Shown**
29. At moderate precision MR-NPRK3-1[ssp3-8x] and MR-NPRK2m[ssp2-16x] obtain a stable solution about four times faster than single-rate NPRK. (§4.4) **Shown**

*(Compiler checks, not in the sources.)* L-stability in the stiff $z_1$ limit is weaker than [L-stability](/properties/a-stability.md): it requires no A-stability, only the limit at fixed $z_2$. §3.1.1 says the numerator has degree "at least" $s^{\{2\}}$ in $z_2$ "(See Proposition A.4)", but Prop. A.4 gives only upper bounds. (C.15) calls (3.8) "The only L-stable, three-stage, stiffly-accurate SDIRK method", which holds only once order 3 is imposed. The partitioned test problem represents a nonlinear system only when the two partial Jacobians are simultaneously diagonalizable, a strong assumption that the paper states.

# Printed slips

- §2.3.1 heading "The partitioned Dalqhuist equation".
- §2.1 (ii)/(iii): "$a_{iuv}$ for $\mu,\nu\in\mathcal S^{\{1\}}$" ($u$ for $\mu$).
- Table 2, row $F_1[F_1[F]]$: "$k\in I_1(1)$" for $I_1(i)$. After (2.7): "$\mathbf b^{\{1\}}=[b^{\{2\}}_i]$" for $\mathbf b^{\{2\}}$.
- §2.3.3: spectra "symmetric about the imaginary axis"; conjugate symmetry is about the real axis, as region (2.9) uses.
- App. A.1 calls (2.8) "the stability function" (it is the region; the function is (2.7)), and App. A's introduction says it proves results "stated in Subsection 2.3" (Thm 3.2 is in §3.1). The Table 1 caption cites "Appendix A.2" for a proof that is in supplementary Appendix A.2.
- Eq. (3.3): the subtracted term $-\frac{h(s^{\{2\}}-1)}{s^{\{2\}}}F(Y_1,Y_j)$ has a free index $j$ outside the sum. Eq. (3.4): "$\lim_{z_2\to\infty}p(z_2)=\infty$" with $p$ undefined. Eq. (3.5): "$y_{n+1}=Y_s$" with $s$ undefined.
- Pseudocode for (3.6): "Select $\gamma=(\sqrt2\pm2)/2$" against $(2\pm\sqrt2)/2$ in (3.7); the minus cases differ in sign.
- Implementation of (3.9): step 3 writes the explicit tableau unhatted; (3.11) writes $a_{s^{\{2\}}+2,3,k}$ for $a_{s^{\{2\}}+2,3,s^{\{2\}}+1}$; "Solve $Y_s=\xi+hF(Y_s,Y_{s-1})$" omits $\hat a^{\{1\}}_{33}$; (3.12) writes $b_{s^{\{2\}}}$ unhatted. Table 3, $Y_{s^{\{2\}}+2}$: the sum uses an undefined index $i$.
- Eq. (4.2): "$q_{i+1/2}=k_{i+1/2}(u_{i+1}-u_{i+1})/\Delta x$" for $u_{i+1}-u_i$; (4.4) has a stray leading "$\cdot$".
- Final time: §4 and Fig. 4 give $t=5$, §4.4 "the final time $t=6$".
- Method names vary: §4.2 lists MR-NPRK2-[ssp2-$m$x], NPRK2[32]b and NPRK3[54]-Sa, while Fig. 4 and §4.4 use MR-NPRK2m-[ssp2-…], IMEX-NPRK2[42]b and IMEX-NPRK3[54]-Sa, and §4.4 writes "MR-NPRK3-1[ssp-8x]".
- Prop. A.3 writes $R(z_1,z_2)$ for the denominator $Q$ and $I$ for 1. (A.13) has $A^{\{2\}}$ for $A^{\{1\}}$, and the proof ends "$\lim S(z_1,z_2)=0$". "couplied" (App. A.2).
- (C.3): "$G(Y_2,Y_0)$" with $Y_0$ undefined. Remark C.1: "$\sum_k a_{2,3,k}$" for $a_{s,3,k}$. (C.22): "$\widehat M^{\{2\}}$" for $\widehat M^{\{1\}}$. (C.39), (C.43): index slips $a_{3,s,\alpha}$, $\hat A^{\{1\}}_{3,3}$. App. C.4 title "MP-NPRK". Typos "coefficeints", "proposng", "entires"; duplicate citation "[36, 36, 32, …]".
- Ref. [7] (arXiv:2401.04859) is printed with year 2023; the arXiv number dates it to January 2024.

# Notation map

| Buvoli et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\dot y=G(y)$ | $y'=f(y)$ | autonomous throughout |
| $F(u,v)$, $F(y,y)=G(y)$ | $F(u,v)$, $f(y)=F(y,y)$ | **the source's IMEX methods are implicit in the first argument and explicit in the second** |
| $G^{\{1\}}$, $G^{\{2\}}$ | $f^{\{1\}}$, $f^{\{2\}}$ | additive pieces |
| $h$ | $h$ | the step; the explicit part substeps through the composed method, not through a separate micro step |
| $Y_i$ | $Y_i$ | stage values |
| $a_{ijk}$, $b_{ij}$ | kept | NPRK tensor and weight matrix |
| $M^{\{r\}}=(a^{\{r\}}_{ij},b^{\{r\}}_i,c^{\{r\}}_i)$ | $(A^{\{r\}},b^{\{r\}},c^{\{r\}})$ | underlying methods |
| $\widehat M^{\{r\}}=(\hat a^{\{r\}},\hat b^{\{r\}},\hat c^{\{r\}})$ | kept, page-local | reduced underlying methods; **the hat is not the registry embedded weight** |
| $\mathcal S$, $\mathcal S^{\{r\}}$, $s^{\{r\}}$ | kept | stage index sets and their sizes |
| $\Phi(\tau)$, $\gamma(\tau)$ | $\Phi(\tau)$, $\gamma(\tau)$ | elementary weight and density |
| $\lambda_1$, $\lambda_2$; $z_r=h\lambda_r$ | same | partitioned Dahlquist problem |
| $R(z_1,z_2)=P/Q$, $e$ | $R(z_1,z_2)$, $\mathbf 1$ | |
| $\Gamma$, $\mathcal P$, $\mathcal P(z_1)$ | kept | stability region, conjugate-symmetrized region, slice; **$\Gamma$ is not the MRI-GARK $\Gamma^{(k)}$** |
| $\lambda$ (§3.2.2) | $\gamma$ | SDIRK diagonal; **source $\lambda$ collides with the Dahlquist eigenvalue** |
| $\gamma$ | kept by context | SDIRK coefficient (§3.2.1), elements of $\mathcal S^{\{2\}}$ (Table 1), tree density; **overloaded** |
| $\nu$ | kept, page-local | elements of $\mathcal S^{\{1\}}$ and free indices of App. C; **not the registry Courant number** |
| $\omega$, $\delta$ | kept | stage choice in $Y_3$; convex weight $\delta\approx-0.3635$ of option 3 |
| $w$, $W_k$, $H(w)=F(Y_3,w)-F(Y_2,w)$ | kept | explicit sub-integration state and stages; correction function; **$H$ is not the registry macro step** |
| $m$ | kept | number of compositions of the base explicit method; $s^{\{2\}}=2m$ (SSP2) or $3m$ (SSP3) |
| $P$ (App. A) | kept, page-local | permutation matrix; also the numerator of $R$; **not the registry stability polynomial** |

# Reference list

36 printed references, numbered [1]–[36] in SIAM style; the supplement cites the same list. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` buvoli-2026. [7] is the arXiv preprint (2401.04859, printed 2023) of the ingested [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) and stays a preprint entry, `buvoli-2024-b`, distinct from it. [35] is Tran, Southworth & Buvoli, ETNA 63 (2025) 171–198, whose DOI is printed with the underscore lost ("10.1553/etna vol63s171") and is recorded as `10.1553/etna_vol63s171`. [8] is the GitHub code repository of the paper and [32] an arXiv preprint of 2018. [29] prints the first author "Scäfers". [33] and [34] print no DOI, and [34] no volume. Two Southworth 2024 works take distinct keys: [34] (IMEX-RK for radiation hydrodynamics I) is the ingested [Southworth et al. (2024)](/sources/southworth-2024.md), and [33], the published one-sweep paper (J. Comput. Phys. 517), is `southworth-2024-c`, distinct from its preprint `southworth-2024-b`. [8] is keyed `buvoli-2025-b`. DOIs are printed for 30 of the 36 references.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Burgers equation](/benchmarks/burgers-equation.md)
* [Linear stability of multirate methods and joint stability regions](/definitions/multirate-linear-stability.md)
* [Nonlinearly partitioned Runge–Kutta (NPRK) methods](/methods/nonlinearly-partitioned-runge-kutta.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
