---
type: Source
title: "Buvoli & Southworth (2025) — A New Class of Runge–Kutta Methods for Nonlinearly Partitioned Systems"
description: "Introduces nonlinearly partitioned Runge–Kutta (NPRK) methods for a right-hand side written as a two-argument function, which evaluate it at pairs of stages so each argument gets its own implicitness, derives order conditions through an equivalence with partitioned Runge–Kutta methods, defines stability in the coupled stiff limit, and constructs IMEX and IMIM methods of orders 1–3."
resource: "doi:10.1137/24m1638501"
source_kind: paper
authors: [Buvoli T., Southworth B.S.]
year: 2025
venue: "SIAM J. Sci. Comput. 47:A2609-A2635"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_SIAM_Journal_on_Scientific_Computing_Buvoli_A_New_Class_of_RungeKutta_Methods_for_Nonlinearly_Partitione.pdf"
tags: [runge-kutta, imex, order-conditions, stability, stiff]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper introduces [nonlinearly partitioned Runge–Kutta (NPRK) methods](/methods/nonlinearly-partitioned-runge-kutta.md) for $y'=f(y)$ rewritten as $y'=F(y,y)$, where $F(u,v)$ is any two-argument function with $F(y,y)=f(y)$. Stages and update evaluate $F$ at pairs of stage values, $Y_i=y_n+h\sum_{j,k}a_{ijk}F(Y_j,Y_k)$ and $y_{n+1}=y_n+h\sum_{i,j}b_{ij}F(Y_i,Y_j)$, with a rank-3 coefficient tensor and a weight matrix. Each argument can then have its own implicitness. Implicit in $u$ and explicit in $v$, the stage solve is linear whenever $F$ is linear in $u$: the lagged-coefficient (Picard) linearization, lifted to high order. NPRK contains classical Runge–Kutta methods. On an additive $F$ it reduces to an [additive (IMEX) Runge–Kutta method](/methods/imex-runge-kutta.md) with shared abscissae. It contains the [semi-implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md) of Boscarino et al. as $2s$-stage methods with alternating stages. [GARK](/methods/generalized-additive-runge-kutta.md) is said not to address nonlinear partitions. [Explicit–implicit–null](/methods/explicit-implicit-null-method.md) stabilization is recalled as an additive method.

For a diagonally implicit subclass, every method equals a larger sequentially coupled method using only $F(Y_j,Y_{j-1})$. That method is a partitioned Runge–Kutta method with equal weights, so partitioned [order conditions](/results/runge-kutta-order-conditions.md) apply. Linear stability uses $y'=\lambda_1y+\lambda_2y$, whose [stability function](/definitions/stability-function.md) $R(z_1,z_2)$ is the additive one. The paper defines IMEX A- and L-stability in the stiff $z_j$ limit, and a new stability in the coupled stiff $z_2$ limit, $\sup_{\lvert\kappa\rvert\le1}\lim_{\lvert z_1\rvert\to\infty}\lvert R(z_1,\kappa z_1)\rvert\le1$, checked through a cosine series on the unit circle.

IMEX-NPRK methods of orders 1–3 (2–5 stages, 1–4 implicit solves) and two A-stable second-order implicit–implicit (IMIM) methods are derived, with a stage-value implementation. On viscous Burgers, only methods stable in the coupled stiff $z_2$ limit survive large steps on the conservative partition. On gray thermal radiation transport (Marshak wave), second-order NPRK methods are stable at much larger steps than Boscarino-form IMEX schemes. On the coarse mesh every higher-order scheme suffers [order reduction](/definitions/order-reduction.md) to first order under the IMEX partition.

# Version read

arXiv:2401.04859v2 [math.NA], 4 Apr 2025, in the authors' LaTeX layout, not the SIAM version of record. 39 PDF pages: 27 of main text (with Appendix A and references) and 12 of supplementary materials (SM1–SM5), all read, with pages 6, 10–11, 15–17 and 19–21 checked visually. Page 1 prints "Runge-Kutta" with a hyphen; title and authors otherwise match Crossref, and no DOI is printed. Whether the SIAM version carries the supplement is not determinable from this copy. Equation, section and SM numbers cited here are those of arXiv v2. The bibliography's `buvoli-2024-b` (arXiv:2401.04859, 2024), cited by other sources, is this paper's preprint and stays a distinct entry.

# Key claims

Notation: $f(y)=F(y,y)$ (source $G$). The additive pieces are $f^{\{1\}}$, $f^{\{2\}}$ (source $G^{\{1\}}$, $G^{\{2\}}$), and the underlying tableaux $(A^{\{1\}},b^{\{1\}},c^{\{1\}})$, $(A^{\{2\}},b^{\{2\}},c^{\{2\}})$. In the IMEX class the first argument $u$ is implicit and the second $v$ explicit. $z_j=h\lambda_j$. As on the [NPRK page](/methods/nonlinearly-partitioned-runge-kutta.md), the ratio $\kappa=z_2/z_1$ (source $\epsilon$), the limit $R_\infty(\kappa)$ (source $\beta_\infty(\epsilon)$) and the cosine series $\Upsilon(\theta)$ (source $\gamma(\theta)$) are page-local.

1. An NPRK method (4.2) is a classical Runge–Kutta method iff $a_{ijk}=0$ for $j\ne k$ and $b_{ij}=0$ for $i\ne j$ (sufficiency stated). (§4.1) **Stated**
2. Every NPRK method has two underlying Runge–Kutta methods (Def. 4.1): with $F(u,v)=f(u)$, $a^{\{1\}}_{ij}=\sum_ka_{ijk}$, $b^{\{1\}}_i=\sum_jb_{ij}$; with $F(u,v)=f(v)$, $a^{\{2\}}_{ik}=\sum_ja_{ijk}$, $b^{\{2\}}_j=\sum_ib_{ij}$; the abscissae coincide, $c^{\{1\}}=c^{\{2\}}$. (Eqs. 4.3–4.4) **Derived**
3. On an additive $F(u,v)=f^{\{1\}}(u)+f^{\{2\}}(v)$ NPRK reduces to the additive method built from its underlying methods. An order-$p$ NPRK method therefore needs underlying methods satisfying the additive order conditions to order $p$. Shared abscissae remove none of the NPRK conditions, which must hold for nonlinear partitions. (§4.1, Eq. 4.5) **Derived**
4. Any $s$-stage semi-implicit (SIRK) method with tableaux $(A^{\mathrm I},b)$, $(A^{\mathrm E},b)$ is a $2s$-stage NPRK method with $a_{2i-1,2j,2j-1}=A^{\mathrm E}_{ij}$, $a_{2i,2j,2j-1}=A^{\mathrm I}_{ij}$, $b_{2i,2i-1}=b_i$, all else zero (Eq. 4.6). NPRK needs no alternation of explicit and implicit stages and can reach high order with fewer stages. (§4.2) **Derived** / **Stated**
5. The sparsity of $a_{ijk}$ fixes the implicitness: DIRK–DIRK $a_{ijk}=0$ for $j>i$, $k>i$; explicit–explicit $a_{ijk}=0$ for $j\ge i$, $k\ge i$; DIRK–explicit (IMEX) $a_{ijk}=0$ for $j>i$, $k\ge i$. (Table 4.1) **Stated**
6. Proposition 4.3 / A.1: any $s$-stage method of form (4.7) is equivalent to an $\hat s$-stage sequentially coupled method (4.8), $\hat s\ge s$; the inductive proof appends $2\sigma-2$ stages per original stage $\sigma$. (App. A) **Proved**
7. Proposition 4.4: an $s$-stage sequentially coupled method is an $(s-1)$-stage partitioned Runge–Kutta method with $a_{ij}=a_{i+1,j+1,j}$, $\hat a_{ij}=a_{i,j+1,j}$, $b_i=\hat b_i=b_{i+1,i}$, applied to $z'=F(z,w)$, $w'=F(z,w)$, $z_n=w_n=y_n$, with $Z_i=Y_{i-1}$, $W_i=Y_i$. (Eqs. 4.9–4.10) **Proved**
8. For sequentially coupled NPRK, second order needs only both partitioned tableaux of second order; third order adds three coupling conditions. (Table 4.3, Eqs. 4.13–4.15) **Derived** (from partitioned Runge–Kutta theory [19, 25, 27])
9. On $y'=\lambda_1y+\lambda_2y$ the NPRK stability function is the additive one, $R(z_1,z_2)=\det(I-z_1A^{\{1\}}-z_2A^{\{2\}}+\mathbf 1(z_1b^{\{1\}}+z_2b^{\{2\}})^\top)/\det(I-z_1A^{\{1\}}-z_2A^{\{2\}})$ (Eq. 4.18). A nonlinear partitioned system reduces locally to decoupled test equations if linearized and the two partial Jacobians are simultaneously diagonalizable (SM2). **Derived**
10. NPRK methods implicit in only one argument cannot be A-stable, since one of $R(0,z_2)$, $R(z_1,0)$ is an explicit stability polynomial. (§4.5.2) **Stated** (immediate)
11. For a diagonally implicit IMEX additive method with nonzero implicit diagonal, $R_\infty(\kappa)=\lim_{\lvert z_1\rvert\to\infty}R(z_1,\kappa z_1)$ is a polynomial in $\kappa$ (Prop. SM3.1) and $\Upsilon(\theta)=\lvert R_\infty(e^{i\theta})\rvert^2$ is a cosine series for real coefficients (Prop. SM3.2); by the maximum modulus principle, stability in the coupled stiff $z_2$ limit is equivalent to $\Upsilon(\theta)\le1$ on $[0,2\pi)$. (Remark 2, Eq. 4.27) **Proved**
12. IMEX-NPRK1[21] (Euler, $y_{n+1}=y_n+hF(y_{n+1},y_n)$) is L-stable in $z_1$ and stable in the coupled stiff $z_2$ limit: $R=(1+z_2)/(1-z_1)$, $R_\infty(\kappa)=\kappa$ as printed. (Eq. 5.2) **Derived**
13. IMEX-NPRK2[31] (one solve; underlying implicit and explicit midpoint) is not L-stable in $z_1$: $\lim_{\lvert z_1\rvert\to\infty}R=-(z_2+1)$, stable only while $\lvert z_2+1\rvert\le1$; it should be used only when $F$ is non-stiff in its second argument. Its third-order residual is $\lVert r^{(3)}\rVert_2=\sqrt{13}/12\approx0.300463$. (Eq. 5.4, SM4.8, SM4.10) **Derived**
14. The three-stage two-solve second-order family L-stable in stiff $z_1$ has one parameter (Eq. 5.5). For it $\Upsilon(\theta;b_{32})=c_0+c_1\cos\theta$ with $\Upsilon(\pi;b_{32})=1$ for all $b_{32}$. Optimizing $\Upsilon(0)$ gives $b_{32}=1-1/\sqrt2$ (global optimum, NPRK2[32]a, stable in the coupled stiff $z_2$ limit) and $b_{32}=1+1/\sqrt2$ (local, NPRK2[32]b, not stable). (SM4.17–SM4.21) **Derived**
15. Error constants: $\lVert r^{(3)}\rVert_2\approx4.15904$ for NPRK2[32]a and $\approx0.302179$ for NPRK2[32]b. The four-stage two-solve NPRK2[42]a/b have the same stability regions, with $\approx1.69593$ and $0.191112$, i.e. 40% and 63% of the three-stage values, at the cost of one more stored stage. (SM4.22–23, SM4.36–37, §5.1.3) **Derived**
16. Stiffly accurate four-stage three-solve second-order IMEX-NPRK methods form a three-parameter family (SM4.43), L-stable in $z_1$ with $R_\infty(\kappa)=-\kappa^3$, hence stable in the coupled stiff $z_2$ limit. (§5.1.3) **Derived**
17. With singly implicit and stiffly accurate structure, $\gamma=0.386585$ minimizes $\lVert r^{(3)}\rVert_2$ and gives IMEX-NPRK2[43]-SiSa (Eq. 5.13), objective $0.500262$; the sibling family (SM4.45) gives $\gamma=0.325754$, objective $0.286004$ ("IMEX-NPRK2[43]b-SiSa", not used in the experiments). **Derived** (numerical optimization)
18. At least five stages are needed for third order in the sequentially coupled IMEX ansatz (5.1); with stiff accuracy exactly two solutions exist, the rational IMEX-NPRK3[54]-Sa (5.14) and one with a diagonal coefficient $\approx4.55$ (SM4.51). (§5.1.4) **Stated** (Mathematica solve; minimality not proved)
19. IMEX-NPRK3[54]-Si ($\gamma=0.54$) is not stable in the coupled stiff $z_2$ limit. (§5.1.4) **Stated**
20. The IMIM ansatz (5.16) has a one-parameter family with bounded $R$ as $z_1$ or $z_2\to\infty$ (5.17). For $b_{23}\in\{1/2,1\}$ the stability function separates, $R(z_1,z_2)=f(z_1)g(z_2)$ with $f(z)=g(z)=(z+2)/(z-2)$, so the methods are A-stable in both variables. The underlying methods are implicit midpoint twice ($b_{23}=1$), or implicit midpoint and Crank–Nicolson ($b_{23}=1/2$). (Eqs. 5.18–5.19, SM5.7–SM5.12) **Derived**
21. For IMIM methods the arguments of $F$ can be swapped without changing accuracy or linear stability. (Remark 3) **Stated**
22. Burgers with viscosity $1/200$ and $1/10000$, $x\in[-2,2]$, 1000 points, $t=0.6$: the nonlinearly partitioned IMEX Euler step (3.1) matches implicit and Rosenbrock Euler in accuracy and stability with one linear solve and no exact Jacobian. Additive IMEX Euler degrades to explicit Euler as the viscosity $\to0$. (§3, Fig. 3.1) **Shown**
23. Burgers, $x\in[-8,8]$, 1000 points, $t=20$. On the non-conservative partition (7.2) all seven IMEX-NPRK methods are stable at all step sizes. On the conservative partition (7.3) only the methods stable in the coupled stiff $z_2$ limit (1[21], 2[42]a, 2[43]-SiSa, 3[54]-Sa) are stable at large steps, and "the degree of instability is proportional to the maximum value of $\gamma(\theta)$" (that is, of $\Upsilon$). All methods converge at their design order. (§7.1, Fig. 7.1) **Shown**
24. Gray thermal radiation transport, Marshak wave, fine mesh (1000 cells, S8): second-order accuracy at reasonable physical steps. H-LDIRK2(2,2,2) and SSP-LDIRK2(3,3,2) in Boscarino (duplicated-equation) form are stable only at smaller steps. All second-order NPRK methods tested are stable at much larger steps with comparable accuracy at small steps. The three-implicit-stage NPRK methods need less memory than SSP-LDIRK2(3,3,2). (§7.2, Fig. 7.3a) **Shown**
25. On radiation transport NPRK3[54]-Si mostly develops too many temperature negativities (NaNs); in the semi-implicit case at large steps where it is stable it converges at third order; "no other 3rd order schemes we have tested from [27, 33, 42] offer stability for these problems either". (§7.2) **Shown** / **Stated**
26. Coarse mesh (128 cells): the IMEX partitioning suffers complete order reduction to first order for all higher-order schemes, so higher order needs the semi-implicit partition. All schemes converge at all steps there, and NPRK2[43]-SiSa has the largest basin of convergence and stays second order even at the largest steps. (§7.2, Fig. 7.3b) **Shown**
27. The standard first-order time-lagging of opacities in radiation transport (Larsen [30]) is exactly a nonlinear partition with the NPRK Euler step (3.1); NPRK extends it to higher order. (§7.2) **Stated**
28. Rosenbrock methods impose the same linearly implicit treatment on the whole problem and do not allow mixed explicit, implicit and linearly implicit treatment of variables inside nonlinear terms. (§2.3) **Stated**

*(Compiler checks, not in the sources.)* For Euler the limit of $R(z_1,\kappa z_1)=(1+\kappa z_1)/(1-z_1)$ is $-\kappa$, not $\kappa$ (claim 12); the modulus is unaffected. Recomputing from SM4.17–SM4.19 gives $\Upsilon(0;1-1/\sqrt2)=57-40\sqrt2\approx0.431$ and $\Upsilon(0;1+1/\sqrt2)=57+40\sqrt2\approx113.6$, confirming claim 14 against the swapped Fig. SM4.1 caption. In (5.18) the implicit-midpoint stability function is $(2+z)/(2-z)=-(z+2)/(z-2)$; the sign cancels in the product, so claim 20 stands.

# Printed slips

- Eq. (2.4), output: "$z_{n+1}=z_n+h\sum_j b_jH^{\{1\}}(Z_j,Y_j)$"; $Y_j$ should be $W_j$.
- §2.2: "upper triangular $A^{\{1\}}=A^I$"; the implicit DIRK tableau is lower triangular.
- §3: "diffusion requires that $h=O(\epsilon/h_x^2)$"; it should be $O(h_x^2/\epsilon)$.
- Eq. (4.17): "$z_1=hz_1,\ z_2=hz_2$" for $z_j=h\lambda_j$. After (4.18): "$b^{\{1\}}=[b^{\{2\}}_i]$" for $b^{\{2\}}$.
- Eq. (4.22) lacks the modulus; (4.25) defines $\beta_\infty$ with a modulus, while Remark 2 and SM3.7 treat it as a polynomial; Eq. (5.2) gives $\beta_\infty(\epsilon)=\epsilon$ where the limit is $-\epsilon$; §5.1.3 calls $\beta_\infty=-\epsilon^3$ a "stability function $\beta(\epsilon)$".
- Fig. 5.1: the middle column heading prints $\arg(z_1)=3\pi/2$ where the caption gives $3\pi/4$.
- Eq. (5.7): "$b_{23}=0$" for $b_{32}=0$. §5.1.4: the stiff-accuracy condition is printed "$b_{i,i+1}=a_{s,i,i+1}$" for $b_{i,i-1}=a_{s,i,i-1}$. §5.2 after (5.18): "$b_{32}$" for $b_{23}$.
- Eq. (5.18): $f(z)=g(z)=(z+2)/(z-2)$ carries a sign slip (see above).
- Eqs. (6.2)–(6.3): $a_{i,j,j-1}$ in (6.3) where the implicit coefficient is $a_{i,i,i-1}$.
- Algorithm 6.1, lines 15–17: the update "$y_{(n+1)}\mathrel{+}=b_{i,i-1}\delta$" sits inside the loop over $i=j+1,\dots,s$, so it adds $\delta_j$ once per later stage and never adds the last stage's $\delta_s$; the intended update is $y_{n+1}\mathrel{+}=b_{j,j-1}\delta$ once per stage $j$. Lines 3/17 write $y_{(n+1)}$, line 18 $y_{n+1}$.
- §7.2: Fig. 7.2 is said to show "three time snapshots" but shows four; "$\sigma(0.025)\approx10^{16}$" where $10^{12}/0.025^3=6.4\times10^{16}$.
- Fig. SM4.1 caption swaps the global and local minima of $\gamma(0;b_{32})$ (values $57\mp40\sqrt2$); SM4.21, (5.6) and the main text are right. The text and the caption call panel (a) "$\gamma(\pi;b_{32})$" or "$\gamma(\theta;b_{32})$" where it is $\gamma(0;b_{32})$.
- SM4.4: "$a_{221}=\frac1{2ab_{32}}$", stray "a"; SM4.5–SM4.6 rename the weight $b_{32}$ as $b_{23}$. SM4.47 names "IMEX-NPRK2[43]a-SiSa" against "IMEX-NPRK2[43]-SiSa" in (5.13), and prints "$c(386585)=0.500262$". SM4.51 uses an index labelling ($a_{110},a_{210},\dots$) inconsistent with $a_{i,j,j-1}$. SM5.1 omits $h$ in the update.
- Ref. [42] prints "Boscarino Sebastiano" (name order inverted); ref. [19] prints "Hairer, Wanner, Nørsett". Typos: "Tablaue" (Table 4.2), "anstaz", "Denomenator", "feely", "tabaleau"; "Burger's", "Burgers'" and "Burgers" alternate.

# Notation map

| Buvoli & Southworth | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y'=G(y)$ | $y'=f(y)$ | autonomous throughout |
| $F(u,v)$, $F(y,y)=G(y)$ | $F(u,v)$, $f(y)=F(y,y)$ | **the source's IMEX class is implicit in the first argument $u$ and explicit in $v$** |
| $G^{\{1\}}$, $G^{\{2\}}$ | $f^{\{1\}}$, $f^{\{2\}}$ | additive pieces |
| $h$; $\Delta t$ (Algorithm 6.1, Eqs. 6.2–6.3) | $h$ | |
| $Y_i$ | $Y_i$ | stage values |
| $a_{ijk}$, $b_{ij}$ | kept | NPRK coefficient tensor and weight matrix |
| $a^{\{q\}}_{ij}$, $b^{\{q\}}$, $c^{\{q\}}$ | $A^{\{q\}}$, $b^{\{q\}}$, $c^{\{q\}}$ | underlying methods $M^{\{1\}}$, $M^{\{2\}}$ |
| $(a,b,c)$, $(\hat a,\hat b,\hat c)$ | kept, page-local | partitioned tableaux of a sequentially coupled method; **the hat is not the registry embedded weight** |
| $A^I$, $A^E$ | $A^{\mathrm I}$, $A^{\mathrm E}$ | SIRK tableaux |
| $\lambda_1$, $\lambda_2$; $z_j=h\lambda_j$ | same | partitioned Dahlquist problem |
| $R(z_1,z_2)$ | $R(z_1,z_2)$ | two-variable stability function |
| $\epsilon=z_2/z_1$ | $\kappa$, page-local | as on the NPRK page; **$\epsilon$ collides with the registry stiffness parameter $\varepsilon$ and is also the Burgers viscosity in Eq. (3.2)** |
| $\beta(z_1,\epsilon)=R(z_1,\epsilon z_1)$, $\beta_\infty(\epsilon)$ ($B_\infty$ in SM3) | $R(z_1,\kappa z_1)$, $R_\infty(\kappa)$, page-local | **$\beta$ is not the PID or multistep $\beta$** |
| $\gamma(\theta)=\lvert\beta_\infty(e^{i\theta})\rvert^2$ | $\Upsilon(\theta)$, page-local | as on the NPRK page; **$\gamma$ collides with the singly implicit diagonal $\gamma$ (kept) and the adiabatic index $\gamma=5/3$ of the same paper** |
| $r^{(3)}$ | kept | third-order residual vector, $\lVert r^{(3)}\rVert_2$ the error constant |
| $F_E(v)$, $F_I(u,v)$ | kept | explicit and implicit parts in Algorithm 6.1 |
| $D$, $A$ | kept, page-local | Burgers diffusion and advection matrices; **$A$ is not a Butcher matrix here** |

# Reference list

51 printed references, numbered [1]–[51], alphabetical; the supplement has no separate list. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` buvoli-2025. [43] is printed "(in review), 2024" with the authors in the order Southworth, Park, Olivier, Buvoli; it is the one-sweep semi-implicit radiation-transport paper, merged into its preprint entry `southworth-2024-b` (arXiv:2401.04285), and is not the ingested [Southworth et al. (2024)](/sources/southworth-2024.md). [44] (arXiv:2305.05452) is the preprint of that ingested source and stays its own preprint entry, `southworth-2023`. [47] is the companion order-condition preprint of Tran, Southworth & Buvoli (arXiv:2401.12427). [17] prints pages without a volume, [15] a book without publisher, [29] "Mathematics Online First Collections, pages 1–17". No DOIs are printed.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Explicit–implicit–null (EIN) time marching](/methods/explicit-implicit-null-method.md)
* [Generalized additive Runge–Kutta (GARK) methods and internal consistency](/methods/generalized-additive-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Nonlinearly partitioned Runge–Kutta (NPRK) methods](/methods/nonlinearly-partitioned-runge-kutta.md)
* [Order reduction](/definitions/order-reduction.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
