---
type: Source
title: "Conte et al. (2024) — Stability Theory of TASE-Runge-Kutta Methods with Inexact Jacobian"
description: "Linear stability theory of TASE-Runge–Kutta methods when the matrix inside the TASE operator is an approximation of the Jacobian: stability diagrams in the generalized-eigenvalue plane, conditions for conditional and unconditional stability through generalized eigenvalues and weighted fields of values, and efficiency against Rosenbrock methods."
resource: "doi:10.1137/24m1631869"
source_kind: paper
authors: [Conte D., Martín-Vaquero J., Pagano G., Paternoster B.]
year: 2024
venue: "SIAM J. Sci. Comput. 46:A3628-A3657"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_SIAM_Journal_on_Scientific_Computing_Conte_Stability_Theory_of_TASERungeKutta_Methods_with_Inexact_Jaco.pdf"
tags: [stiff, stability, explicit, linear-algebra, runge-kutta]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

TASE-Runge–Kutta (TASE-RK) methods precondition the right-hand side of a stiff ODE with a [TASE operator](/methods/tase-operators.md) $\mathcal P_p(hJ)=\sum_j\mathsf w_j(I-\vartheta_jhJ)^{-1}=I+O(h^p)$ and then apply an explicit $p$-stage Runge–Kutta method of order $p$. The order is kept for any matrix in place of the Jacobian $J$. In practice $J$ is therefore replaced by a cheap matrix $\tilde J$, constant, symmetric negative definite and factorized once. All earlier stability results assumed $\tilde J=J$. The paper analyses linear stability for an arbitrary $\tilde J$. It writes $J=\tilde J+E$ and borrows the technique of Rosales, Seibold, Shirokoff and Zhou for unconditional stability of IMEX multistep methods ([IMEX splitting](/methods/imex-runge-kutta.md) of the test problem).

On the scalar test $y'=(\lambda+\lambda_E)y$ with $\mu=\lambda_E/\lambda$ and $x=h\lambda<0$, the [stability function](/definitions/stability-function.md) becomes $P\big(\hat{\mathcal P}_p(x)(1+\mu)\big)$. Here $P$ is the stability polynomial of the explicit method and $\hat{\mathcal P}_p(z)=z\mathcal P_p(z)$. The authors define stability diagrams $\mathcal D_{x,p}$ in the $\mu$-plane. Each diagram is a scaled, reflected and shifted copy of the explicit stability region. The diagrams are nested and shrink, as $h\to\infty$, to the unconditional diagram $\mathcal D_{\infty,p}$. When $\tilde J$ and $E$ are simultaneously diagonalizable, stability is decided eigenvalue by eigenvalue, and unconditional stability holds iff all generalized eigenvalues lie in $\mathcal D_{\infty,p}$. In the general case a weighted field of values gives sufficient conditions. A mean-value linearization extends the analysis heuristically to reaction terms.

Matlab experiments use a $3\times3$ linear test, the Fisher–Kolmogorov equation, the viscous [Burgers equation](/benchmarks/burgers-equation.md) and the [FitzHugh–Nagumo model](/benchmarks/fitzhugh-nagumo-model.md). They confirm the predictions and show TASE-RK with a constant $\tilde J$ more efficient than [Rosenbrock methods](/methods/rosenbrock-wanner-method.md) ROS2, ROS3 and ROS4 of the same order that use the exact Jacobian. The paper also records, from González-Pinto et al. (2023), that TASE-RK methods are a subclass of W-methods. The [A-stability](/properties/a-stability.md) data of the exact-Jacobian case are recalled from Calvo, Montijano and Rández.

# Version read

arXiv:2401.10088v1 [math.NA], 18 January 2024 (SIAM review template, "Submitted to the editors DATE", footer "This manuscript is for review purposes only"), 26 pages, all read; pp. 13, 14, 18 and 19 were checked visually. This is not the version of record (SIAM J. Sci. Comput. 46:A3628–A3657, 2024), whose pagination cannot be checked against this file. Section, equation and page numbers on this page are those of arXiv v1. Page 1 matches Crossref (title, authors; the arXiv page prints "MARTIN-VAQUERO" without the accent), and the DOI is not printed.

# Key claims

Notation, page-local and aligned with the [TASE page](/methods/tase-operators.md): $h$ the step (the source's $k$); $\tilde J$ the matrix used inside the TASE operator (the source's $A$); $E=J-\tilde J$; $\mathcal P_p(h\tilde J)=\sum_j\mathsf w_j(I-\vartheta_jh\tilde J)^{-1}$ (the source's $T_p(kA;\vec\omega)$ with weights $\beta_j$ and shifts $\omega_j$); $\lambda<0$ an eigenvalue of $\tilde J$ and $\lambda_E$ one of $E$ (the source's $\lambda$, $\gamma$); $\mu=\lambda_E/\lambda$; $x=h\lambda$; $\hat{\mathcal P}_p(x)=x\mathcal P_p(x)$ (the source's $\hat T_p$); $P(z)=\sum_{j\le p}z^j/j!$ and $\mathcal S_p$ its stability region restricted to $\operatorname{Re}z\le0$ (the source's $R_p$, $\mathcal R_p$); $\mathcal W_r$ the weighted field of values (the source's $\mathcal W_q$); $\rho_p$ the length of the negative real interval of $\mathcal S_p$ (the source's $c_p$). See the notation map.

1. TASE-RK methods are a subclass of W-methods (citing González-Pinto et al. 2023); their order $p$ is kept when $J$ is replaced by any matrix $\tilde J$ in $\mathcal P_p$, because $\mathcal P_p=I+O(h^p)$ still holds (§1, §2, Remark 2.1). **Stated**
2. Until this paper TASE-RK stability had been studied only with $\tilde J=J$. With the shifts of Calvo et al. (Table 1), TRK2 is strongly A-stable ($R(\infty)=0.5$), TRK3 is L($\alpha$)-stable with $\alpha=89.02^\circ$, and TRK4 is strongly A($\alpha$)-stable with $\alpha=87.34^\circ$, $R(\infty)=0.27$ (§2, Table 1). **Stated** (from Calvo et al.)
3. With the splitting $J=\tilde J+E$, the stability function of a TASE-RK method with $s=p\le4$ is $\tilde R(x,\mu)=\sum_{j=0}^p\frac1{j!}\hat{\mathcal P}_p(x)^j(1+\mu)^j$ (§3, Eq. (3.4)). **Derived**
4. $\hat{\mathcal P}_p(z)$ is increasing on $z<0$ with values in $[\hat{\mathcal P}_p^*,0]$, $\hat{\mathcal P}_2^*\approx-1$, $\hat{\mathcal P}_3^*\approx-1.5961$, $\hat{\mathcal P}_4^*\approx-1.5961$ (Fig. 1 caption). **Shown** (plot only)
5. Lemma 3.4: $\mathcal D_{x,p}=-1+\hat{\mathcal P}_p(x)^{-1}\mathcal S_p$ — the stability diagram is the explicit stability region scaled by the negative factor $1/\hat{\mathcal P}_p(x)$ (hence rotated by $180^\circ$) and shifted by $-1$ (§3, Lemma 3.4, Fig. 2). **Proved**
6. Thm 3.6: for $z_1<z_2<0$ and $p=2,3,4$, $\mathcal D_{z_1,p}\subseteq\mathcal D_{z_2,p}$, so $\mathcal D_{\infty,p}$ is the smallest diagram (Remark 3.7, Fig. 3). The proof uses explicit boundary parametrizations and the star-shapedness of $\mathcal S_p$ with respect to 0. **Proved**
7. Prop. 4.1: if $\tilde J$ and $E$ are simultaneously diagonalizable with paired eigenvalues $(\lambda_i,\lambda_{E,i})$, the method is stable with step $h$ iff $\mu_i\in\mathcal D_{h\lambda_i,p}$ for all $i$ (proof in App. A.1). **Proved**
8. Remark 4.2: the real-axis endpoints of $\partial\mathcal D_{x,p}$ are $-1$ and $\mu_r(x)$. For $p=2$, $\mu_r=-1-2/\hat{\mathcal P}_2(x)\ge1$, so the method is unconditionally stable if all real $\mu_i\le1$; otherwise $h^*=\min_i\frac{-8+\mu_i-\sqrt{28+20\mu_i+\mu_i^2}}{9\lambda_i(\mu_i-1)}$ over $\mu_i>1$ (closed form specific to the shifts $(3,1.5)$). Unconditional stability holds for $p=3$ if $\mu_i\le\mu_3^*\approx0.5743$ and for $p=4$ if $\mu_i\le\mu_4^*\approx0.7445$. **Derived**
9. Test 1 ($3\times3$, simultaneously diagonalizable): $h^*\approx7.8390\times10^{-1}$ for TRK2 and $h^*\approx2.8428\times10^{-1}$ for TRK3; the binding eigenvalue is $\lambda=-10$, not the most negative one (§4, Fig. 4, Remark 4.4). **Derived** and **Shown** (Table 2)
10. Table 2: with $\tilde J$ in place of $J$, TRK2 errors at $t=30$ are $2.6260\times10^3$, $1.1609\times10^3$, $2.5721\times10^{-1}$, $1.5684\times10^{-15}$ for $h=1.875$, $0.9375$, $0.46875$, $0.234375$; TRK3 blows up to $1.3881\times10^{16}$ at $h=0.46875$ and is accurate ($9.5785\times10^{-13}$) only at $h=0.234375$; with the exact $J$ both are stable at every $h$ (§4, Table 2). **Shown**
11. Thm 4.3: with $\lambda_1$ the most negative eigenvalue of $\tilde J$, $\mu(\tilde J,E)\subseteq\mathcal D_{h\lambda_1,p}$ is sufficient for stability without pairing eigenvalues; it is more restrictive, forcing $h=h^*/10$ in Test 1 (Remark 4.4). **Proved**
12. Thm 4.5 (simultaneously diagonalizable case): unconditionally stable iff $\mu(\tilde J,E)\subseteq\mathcal D_{\infty,p}$. **Proved**
13. Thm 5.3 (general case): stable with step $h$ iff $\sigma(Z)\subseteq\mathcal S_p$, $Z:=h\mathcal P_p(h\tilde J)(\tilde J+E)$, the stability condition being read as $\rho\big(\tilde R(h\tilde J,hE)\big)\le1$ (Eq. (5.4)). **Proved** (as a spectral-radius criterion; see the caution below)
14. Thm 5.5 (general case, $\tilde J$ symmetric negative definite): stable if there is $r\in\mathbb R$ with $\mathcal W_r(-\tilde J,E)\subseteq-\mathcal D_{h\lambda_1,p}$; this is the field-of-values analogue of Thm 4.3 and more restrictive, since $-\mu(\tilde J,E)\subseteq\mathcal W_r(-\tilde J,E)$ for all $r$. **Proved**
15. Thm 5.6: unconditionally stable if there is $r$ with $\mathcal W_r(-\tilde J,E)\subseteq-\mathcal D_{\infty,p}$; conversely, unconditional stability implies $\mu(\tilde J,E)\subseteq\mathcal D_{\infty,p}$, so one generalized eigenvalue outside $\mathcal D_{\infty,p}$ rules it out. **Proved**
16. Remark 5.7: scaling $\tilde J\to\kappa\tilde J$ with $E=J-\kappa\tilde J$ gives $\mu(\kappa\tilde J,E)=-1+\kappa^{-1}\mu(\tilde J,J)$ and $\mathcal W_r(-\kappa\tilde J,E)=1+\kappa^{-1}\mathcal W_r(-\tilde J,J)$ (from Seibold et al.); a suitable $\kappa>0$ can make the method unconditionally stable. **Stated** / **Derived**
17. Test 2 (not simultaneously diagonalizable but block-diagonalizable): Thm 5.5 applied to the $2\times2$ block with $\lambda_1=-10$ gives the safe steps $h=0.21$ (TRK2) and $h=0.145$ (TRK3); numerically TRK2 and TRK3 are stable for $h<1$. Using the block structure is presented as plausible but unproved (§5, Fig. 5). **Derived** and **Shown**
18. Nonlinear stability (§6) is only heuristic: the mean-value theorem rewrites $y'=\lambda y+g(y)$ as $y'=(\lambda+g'(\xi))y+k_g$; requiring $g'(\upsilon_{\mathrm{UB}})\ge-\rho_p/(h\mathcal P_p(h\lambda))-\lambda$ "leads to stability", with $\rho_2=2$, $\rho_3\approx2.5127$, $\rho_4\approx2.7853$. Remark 6.2 concedes that this is no global proof without checking $\lVert y_n\rVert_\infty\le3/2$ at every step. **Derived**
19. Prop. 6.1: for the second-order finite-difference Fisher–Kolmogorov semi-discretization, $\mathcal W_1(-\tilde J,E)$ is real and $\frac\epsilon\ell(1-2\upsilon_{\mathrm{UB}})\le\mathcal W_1(-\tilde J,E)\le\frac\epsilon\ell(1-2\upsilon_{\mathrm{LB}})$ with $\ell\in\big[\frac{2D}{\Delta x^2}(1+\cos\frac{(M_x-1)\pi}{M_x}),\frac{2D}{\Delta x^2}(1+\cos\frac\pi{M_x})\big]$ (App. A.3). With $\upsilon_{\mathrm{LB}}=0$, $\upsilon_{\mathrm{UB}}=3/2$ and $M_x=100$ every TASE-RK method is unconditionally stable (Fig. 6, TRK3 at $h=0.5$). **Proved** (proposition) and **Shown**
20. Burgers ($\epsilon=10^{-1}$), $\tilde J=\kappa(\epsilon L_1-2I)$ with $\kappa=1$: $\mathcal W_1(-\tilde J,E)\subseteq-\mathcal D_{\infty,p}$ for $p=2,3,4$, so every TRK method is unconditionally stable; TRK2 is stable at $h=0.5$ (§7.1, Fig. 7). **Shown**
21. Burgers ($\epsilon=10^{-2}$), $\kappa=1$: $-0.4875\pm3.4130i\in\mu(\tilde J,E)$ lies outside $\mathcal D_{\infty,p}$, so the methods are not unconditionally stable and TRK2 is unstable at $h=0.5$; with $\kappa=3$ they are unconditionally stable and TRK2 is stable at $h=0.5$ (§7.1, Figs. 7–8). **Shown**
22. FitzHugh–Nagumo, $\tilde J=\kappa\operatorname{blkdiag}(DL_1-I,-(b/\tau)I)$, $\kappa=1.2$: $\mathcal W_{1/3}(-\tilde J,E)\subseteq-\mathcal D_{\infty,p}$, so every TRK method is unconditionally stable; TRK4 at $h=0.5$ is stable on $[0,200]$ (§7.2, Fig. 9). **Shown**
23. Efficiency: TASE-RK with a constant inexact $\tilde J$ is "much more efficient than the ROS of the same order" in error against CPU time on Burgers ($\epsilon=10^{-1}$, final time 4) and FitzHugh–Nagumo (final time 50); Matlab R2023b on a laptop with an AMD Ryzen 7 3700U at 2.30 GHz and 8 GB RAM; reference solutions by ode15s with AbsTol = RelTol = eps (§7.1–7.2, Figs. 7, 9). **Shown**
24. Rosenbrock methods with an inexact Jacobian become W-methods, "for which the order of convergence is generally lower, and furthermore there is no study on the related stability properties" (§7). **Stated**
25. This is "the first manuscript where the stability of a subclass of W-methods is in-depth studied with an inexact Jacobian, using the techniques that we employ" (§1.1). **Stated**
26. Choosing $\tilde J$ symmetric negative definite is "not restrictive", because $E:=J-\tilde J$ absorbs the rest (§3). **Stated**

*(Compiler checks, not in the sources.)* Def. 3.1 asks for $\lVert y_n\rVert\le C$ with $C$ independent of $h$ and $n$, while Thm 5.3 equates this with a spectral-radius bound; for non-normal amplification matrices $\rho\le1$ does not bound powers uniformly, so the "iff" holds only up to that caveat. The claim in item 24 that W-method stability with $\tilde J\ne J$ is unstudied overlooks the classical W-method and AMF-W literature, which analyses stability with approximate Jacobians. The efficiency comparison pits a constant cheap $\tilde J$ against Rosenbrock methods with the exact Jacobian, not against W-methods with a frozen matrix.

# Printed slips

1. p. 13, Eq. (5.3): "$\vec u_{n+1}=(R_{T_p}(kA,kB))^{n+1}\vec u_n$" — the exponent $n+1$ requires $\vec u_0$ on the right (or the exponent should be 1); the same in App. A.1, Eq. (A.1).
2. p. 14, Eq. (5.6): "$\lvert\sigma(I+Z+\dots)\rvert\le1$" — the modulus of a set, meaning $\rho(\cdot)\le1$.
3. p. 15, proof of Thm 5.5: "W(M) = co(σ(M)), as M is a normal matrix (see Remark 5.1, item 4)" — the normal-matrix property is item 5.
4. p. 10, Remark 4.2 ($p=4$): $\mu_4^*\approx0.7445$; a compiler check, not in the sources, gives $-1+2.785294/1.596063=0.74510$ from the printed formula and the Table 1 shifts, so the printed value is off in the fourth digit ($\mu_3^*=0.5743$ reproduces exactly).
5. Sign of $c_p$: §6, Test 3 uses $c_p>0$ ($c_2=2$, $-c_p\le z\le0$), while §6.1 states "$c_p<0$" in the same role (p. 19, before (6.10)).
6. Eq. (6.7): $\vec g(\vec u)=(g_1(u_1),\dots,g_d(u_d))^T\in\mathbb R^{M-1}$ mixes $d$ and $M-1$.
7. The final time of the Fisher–Kolmogorov test is not stated (Fig. 6 shows $t\in[0,2]$).
8. Ref. [9] prints a non-DOI as a DOI ("https://doi.org/www.chebfun.org/docs/guide/"); Ref. [20] prints a doubled prefix ("https://doi.org/doi.org/10.1007/b98868").

*(Compiler checks, not in the sources.)* The Test 1 data were verified ($\sigma(\tilde J)=\{-100,-10,-1\}$, $\sigma(E)=\{-50,-12,-1.5\}$, $\mu=\{0.5,1.2,1.5\}$, commuting matrices), the step bounds $h^*$ of claim 9, and the Table 1 values of $R(\infty)$.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ | $h$ | step |
| **$h$** | $\Delta x$ | mesh width in §6–7; **collides** with the registry step |
| $\vec u$, $\vec f(t,\vec u)$ | $y$, $f(t,y)$ | |
| $J$ | $J$ | agrees (exact Jacobian) |
| **$A$** | $\tilde J$ | inexact Jacobian inside the TASE operator; **collides** with the Butcher matrix |
| $B:=J-A$ | $E$ (page-local) | remainder, renamed as on the TASE page; $B$ would collide with the B-series $B(a,y)$ and $B(\xi)$ |
| **$\alpha_{ij}$**, $b_j$, $c_j$ | $a_{ij}$ (matrix $A$), $b_j$, $c_j$ | explicit Runge–Kutta coefficients; **$\alpha_{ij}$ collides** with the Shu–Osher coefficients |
| $T_p(kA;\vec\omega)$ | $\mathcal P_p(h\tilde J)$ | TASE operator, as on the [TASE page](/methods/tase-operators.md) |
| **$\omega_j$** | $\vartheta_j$ | shifts of the Calvo–Montijano–Rández family; **collide** with the TASE page's weights $\omega_{p,k}$; Bassenne's family is $\vartheta_j=\vartheta/2^{j-1}$ |
| $\beta_j$ | $\mathsf w_j$ | weights fixed by $\mathcal P_p=I+O(h^p)$, as on the TASE page; **$\beta_j$ collides** with the multistep coefficients |
| $\eta$ | — | eigenvalue of $J$, not used on this page; **$\eta$ collides** with the registry entropy |
| $\lambda$, $\gamma$ | $\lambda$, $\lambda_E$ | eigenvalues of $\tilde J$ and $E$; **$\gamma$ collides** with the Rosenbrock $\gamma$ |
| $\mu=\gamma/\lambda$, $\mu(A,B)=\sigma(A^{-1}B)$ | $\mu$, $\mu(\tilde J,E)$ | generalized eigenvalue; not the Nevanlinna–Odeh multipliers |
| $y=k\lambda$ | $x=h\lambda$ | **$y$ collides** with the registry solution |
| $\hat T_p(y)=yT_p(y)$ | $\hat{\mathcal P}_p(x)$ | **the hat collides** with the registry embedded weights |
| $R_p(z)$, $\mathcal R_p$ | $P(z)$, $\mathcal S_p$ | stability polynomial and region (restricted to $\operatorname{Re}z\le0$) |
| $R_{T_p}$, $\tilde R_{T_p}(y,\mu)$ | $R$, $\tilde R(x,\mu)$ | stability function |
| $\mathcal D_{y,p}$, $\mathcal D_{\infty,p}$ | $\mathcal D_{x,p}$, $\mathcal D_{\infty,p}$ | stability diagrams |
| $\mathcal W(X)$, **$\mathcal W_q(-A,B)$** | $\mathcal W(X)$, $\mathcal W_r(-\tilde J,E)$ | field of values; **$q$ collides** with the registry stage order |
| $c_p$ | $\rho_p$ | negative-real interval of $\mathcal S_p$, as on the TASE page; the source flips its sign in §6.1 |
| $\theta$ in A($\theta$) | $\alpha$ | A($\alpha$)-stability angle |
| $M$ | $M_x$ | number of grid intervals; **collides** with the registry mass matrix |
| $\kappa$, $k^*$, $\upsilon_{LB}$, $\upsilon_{UB}$, $\ell$, $\epsilon$, $D$ | $\kappa$, $h^*$, kept | scaling of $\tilde J$, maximal stable step, solution bounds, element of $\mathcal W(-\tilde J)$, PDE coefficients |

# Reference list

25 printed references, numbered [1]–[25] in SIAM style, with DOIs printed as URLs. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` conte-2024. Ref. [9] (Chebfun Guide) prints a malformed DOI URL and is recorded without a DOI. The doubled prefix of [20] is reduced to 10.1007/b98868, and the DOI of [24] is kept as printed (10.1137/1.9780898719574.fm). Ref. [1] prints no volume or pages. Conte et al. 2023 ([7], [8]) take suffixes in printed order. Refs. [17] (Hundsdorfer & Verwer 2003) and [21] (Rosales et al. 2017) are `hundsdorfer-2003-b` and `rosales-2017-b`, because the bibliography already held other works under the plain keys; the JSTOR DOI printed for [23] (Steihaug & Wolfbrandt 1979) is an alternate registration of the work keyed `steihaug-1979`. Several J. Comput. Phys. and Appl. Numer. Math. entries print no article number. There are no printed duplicates and no unparseable items.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [FitzHugh–Nagumo model](/benchmarks/fitzhugh-nagumo-model.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [TASE operators: time-accurate and highly stable explicit operators](/methods/tase-operators.md)
