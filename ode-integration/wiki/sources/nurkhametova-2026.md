---
type: Source
title: "Nurkhametova et al. (2026) — A Patankar predictor-corrector approach for positivity-preserving time integration"
description: "Post-processes stiffly accurate SDIRK steps on graph-Laplacian production–destruction systems with a Patankar-type corrector, one extra linear solve that makes the solution nonnegative and keeps the linear invariants for any step, with a worst-case order min(p, q+1) and observed nominal orders."
resource: "doi:10.1016/j.apnum.2026.08.005"
source_kind: paper
authors: [Nurkhametova K., Gomillion R.J., Subrahmanya A.N., Sandu A.]
year: 2026
venue: "Appl. Numer. Math. 230:503-535"
local_file: "/home/stefano/papers/mosaic/ode-integration/2026_Crossref_Applied_Numerical_Mathematics_Nurkhametova_A_Patankar_predictor-corrector_approach_for_positivity-prese.pdf"
tags: [positivity, structure-preserving, stiff, implicit, step-size-control]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper targets stiff [production–destruction systems](/definitions/production-destruction-system.md). More generally it treats ODEs in graph-Laplacian form $y'=\mathbb G(t,y)\,y$, where $\mathbb G$ has a nonpositive diagonal, nonnegative off-diagonal entries and left null vectors $w_j$ that are linear invariants. Standard [SDIRK](/methods/diagonally-implicit-runge-kutta.md) methods can produce small negative components. Clipping alone destroys conservation. Rejecting steps until the solution is positive makes the step collapse.

The contribution is a Patankar predictor–corrector post-processing for [stiffly accurate](/properties/stiff-accuracy.md) SDIRK methods with nonnegative weights. The predictor is an ordinary SDIRK step. The corrector clips the predicted stages and forms $\bar{\mathbb G}=\sum_jb_j\mathbb G(\breve Y_j)\Sigma_{Y_j/y^{\mathrm p}_{n+1}}$, where the diagonal ratio-scaling matrix $\Sigma$ has entries $\max(Y_{j,\ell},0)/\max(y^{\mathrm p}_{n+1,\ell},\epsilon_{\mathrm c})$. It then solves $y_{n+1}=(I-h\bar{\mathbb G})^{-1}y_n$. Nonnegative combinations of column-scaled graph Laplacians are graph Laplacians, so $I-h\bar{\mathbb G}$ is an M-matrix. The corrected solution is therefore nonnegative and keeps every linear invariant that is a left null vector of $\mathbb G$, for any $h$: this is [positivity preservation](/properties/positivity-preservation.md) at the cost of one extra LU factorization per step. A variant corrects every stage the same way. The authors place the scheme among the [modified Patankar methods](/methods/modified-patankar-methods.md), calling the correction an extra MPRK-type stage.

A proposition bounds the local error of the corrected solution by $\mathcal O(h^{\min(q+2,p+1)})+\mathcal O(\epsilon_{\mathrm c})$. The worst-case order is thus $\min(p,q+1)$, which is 2 for SDIRK with [stage order](/definitions/stage-order.md) $q=1$, a cap of the kind recorded under [order reduction](/definitions/order-reduction.md). The tests use SDIRK21, SDIRK32 and SDIRK43 of Kennedy–Carpenter with [embedded pairs](/methods/embedded-runge-kutta-pair.md) on the [Robertson problem](/benchmarks/robertson-problem.md), a MAPK cascade, the [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md) and a positivity-shifted finite-volume [Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md). Negative values disappear, structurally exact invariants stay at roundoff, and the observed slopes are reported as the nominal orders. Run-time changes for SDIRK43 range from −81 % to +266 %; the extra solve is discussed under [implicit-stage solvers](/methods/implicit-stage-solvers.md). Correcting all stages distorts KdV, so the final-stage correction is recommended there.

# Version read

The author's manuscript distributed as Virginia Tech Computational Science Laboratory technical report CSL-TR-26-1, dated 16 Sep 2026. Its cover page cites the published article (Appl. Numer. Math. 230 (2026) 503–535). The text thanks the reviewers, so it is the accepted post-review text, not the journal-typeset version of record. 61 PDF pages (a cover page and 60 numbered pages), all read; the tableaux (pp. 28–29) and test problems (pp. 22–25) were also checked visually. The title page matches Crossref; no identity problem. Page, section, equation and table numbers cited here are those of the report. The acknowledgement discloses that ChatGPT was used to polish the text.

# Key claims

Notation: $y\in\mathbb R^d$ (the source writes $d$ and $N$ interchangeably); stage values $Y_i$; $y^{\mathrm p}_{n+1}$, $Y^{\mathrm p}_i$ the predicted (uncorrected) solution and stages; $\breve Y=\max(Y,0)$ componentwise; $\mathbb G(t,y)$ the page-local graph-Laplacian factor with $f=\mathbb G(t,y)y$; $w_j$ its left null vectors; $\Sigma_{Y/Z}=\operatorname{diag}_\ell\max(Y_\ell,0)/\max(Z_\ell,\epsilon_{\mathrm c})$ with a page-local threshold $\epsilon_{\mathrm c}>0$. The Patankar weight denominator of the corrector is thus $\varpi_\ell=\max(y^{\mathrm p}_{n+1,\ell},\epsilon_{\mathrm c})$ *(compiler check, not in the sources)*. $p$ and $q$ are the classical order and stage order of the base method.

1. Standard explicit and implicit integrators can produce negative concentrations or artificial mass gain or loss on PDS with large steps; naive clipping destroys mass conservation. (§§1–2) **Stated**
2. For $\mathbb G$ satisfying Assumptions 3.1–3.2, $I-h\mathbb G$ is an M-matrix and $(I-h\mathbb G)^{-1}\ge0$ for every $h\ge0$. (Remark 3.6; proven in [2] for one invariant $w_1=\mathbf 1$) **Stated**
3. Right-multiplying a graph Laplacian by a nonnegative diagonal matrix keeps its sign structure and its left null vectors, and nonnegative combinations of such matrices are graph Laplacians with the same left kernel. (Remarks 3.7–3.9, Eqs. (8)–(10)) **Proved** (elementary, inline)
4. A conservative PDS with $d_{ij}=\ell_{ij}(y)y_i$, $\ell_{ij}\ge0$, can be written $y'=\mathbb G(y)y$ with $\mathbb G=\mathcal L^\top-\operatorname{diag}(\mathcal L\mathbf 1)$, $\mathcal L=(\ell_{ij})$, which has the graph-Laplacian sign structure and zero column sums. (§3.2, Eqs. (11)–(14)) **Derived**
5. Not every linear invariant of $y'=\mathbb G(t,y)y$ is a left null vector of $\mathbb G$; invariants that are not may be lost by the methods of the paper. (Remark 3.11) **Stated**
6. Lemma 3.14: in any monotone norm, clipping the negative entries of SDIRK stages and solution does not increase their local errors, which are $\mathcal O(h^{q+1})$ ($q=1$) and $\mathcal O(h^{p+1})$. (Eq. (19), Fig. 1) **Proved**
7. The corrector (24) gives $y_n\ge0\Rightarrow y_{n+1}\ge0$ and $y_n>0\Rightarrow y_{n+1}>0$, and preserves every linear invariant $w_j$ with $w_j^\top \mathbb G\equiv0$, for any step. (Eqs. (24d)–(24e)) **Proved** (M-matrix argument; see the compiler checks)
8. Under the strong sign Assumption 3.3 (sign structure for all $y\in\mathbb R^d$) the stages need not be clipped: $\bar{\mathbb G}=\sum_jb_j\mathbb G(Y_j)\Sigma_{Y_j/y^{\mathrm p}_{n+1}}$. (Remark 3.18, Eq. (25)) **Stated**
9. For adaptive stepping the embedded estimate uses the uncorrected predictor, $y^{\mathrm p}_{n+1}-\hat y_{n+1}$, so the controller is unaffected by the correction; a more conservative estimate adds $\lVert y_{n+1}-y^{\mathrm p}_{n+1}\rVert$. (Remarks 3.20–3.21) **Stated**
10. The stage-corrected DIRK (Eq. (27)) makes every stage nonnegative and conservative; it requires a stiffly accurate method with $a_{ij}\ge0$ and $b_i\ge0$. (§3.4) **Derived**
11. The correction costs one extra LU factorization per step, different from the nonlinear solver's, viewed as an extra MPRK-type stage; MPRK starts from an explicit Runge–Kutta method and uses one LU per stage. (Remark 3.22) **Stated**
12. Proposition 3.23: from exact $y_n$, the corrected solution has local error $\mathcal O(h^{\min(q+2,p+1)})+\mathcal O(\epsilon_{\mathrm c})$; with $\epsilon_{\mathrm c}=Ch^{\min(q+2,p+1)}$ the order is $\min(p,q+1)$. (Eqs. (32)–(33)) **Proved** (short, somewhat formal proof)
13. On Robertson, uncorrected SDIRK21 gives negative values of species $B$ (insets at $10^{-10}$ and $10^{-15}$); final-stage and all-stage corrections give nonnegative trajectories. (Figs. 2–4) **Shown**
14. On the stratospheric problem, uncorrected SDIRK21 gives negative $\mathrm O^{1D}$ and $\mathrm O$; both corrections remove them. (Figs. 5–7) **Shown**
15. MAPK showed no negative concentrations with the uncorrected methods. (§5.1.1) **Shown**
16. Enforcing positivity by rejecting steps with negative components and halving $h$ drives the step to the "step size too small" floor in stiff regimes. (Stratospheric, Fig. 8a vs 8b) **Shown**
17. For KdV, all-stage correction "exhibited severely distorted dynamics" (not displayed); final-stage correction removes undershoots of order $10^{-4}$ at $t=0.35$ without visible distortion. (§5.1.4, Figs. 9–10) **Shown**
18. Invariant errors on Robertson, $[0,10^4]$: baseline $2.44\times10^{-15}$, final-stage $2.22\times10^{-15}$, all-stage $3.99\times10^{-15}$. (§5.2.1, Figs. 11–13) **Shown**
19. MAPK on $[0,200]$, baseline / final-stage / all-stage: factorization $\alpha=0$: $E_{C_1}=9.14$, $9.26$, $9.26\times10^{-15}$ and $E_{C_2}=5.40$, $5.39$, $5.73\times10^{-4}$; $\alpha=1$: $E_{C_1}=9.48$, $9.47$, $9.21\times10^{-4}$ and $E_{C_2}=3.11\times10^{-15}$ for all three. (Tables 1–2) **Shown**
20. Stratospheric over one day: $E_{M_O}=4.89\times10^{-14}$, $4.89\times10^{-14}$, $1.49\times10^{-12}$ and $E_{M_N}=7.18$, $7.39$, $7.18\times10^{-15}$; the all-stage oxygen increase is attributed to accumulated roundoff. (Table 3) **Shown**
21. KdV mass deviation: baseline $8.88\times10^{-16}$, final-stage $7.40\times10^{-16}$. (§5.2.4, Figs. 23–24) **Shown**
22. Empirical orders, final-stage correction, SDIRK21 / SDIRK32 / SDIRK43: stratospheric 2.07 / 4.27 / 4.70; MAPK 1.98 / 2.76 / 3.81; Robertson 1.51 / 3.47 / 5.47; KdV 1.72 / 3.37 / 3.85. (Table 4; slopes printed negative) **Shown**
23. Empirical orders, all-stage correction: stratospheric 2.07 / 4.28 / 4.62; MAPK 1.98 / 2.75 / 3.86; Robertson 1.95 / 2.84 / 3.76; the paper concludes that the correction "preserves, in practice, the formal order". (Table 5, §5.3.5) **Shown**
24. Wall-clock, SDIRK43, $\mathrm{rtol}=\mathrm{atol}=10^{-7}$, mean of 5 runs, MATLAB R2023b on an AMD Ryzen 7 5825U laptop: stratospheric (3 days) 30.2 s → 110.5 s (+266 %); MAPK 0.560 → 0.516 s (−7.9 %); Robertson 0.485 → 0.090 s (−81.4 %); KdV 10.9 → 21.2 s (+94.5 %). The Robertson speed-up is attributed to avoiding stiff dynamics in non-physical negative regimes. (Table 6, Remark 3.22) **Shown**
25. For explicit Runge–Kutta methods the correction reduces convergence to first order; it applies in principle, but the linear solve removes the advantage of explicit computation. (§§1, 6) **Stated** (no data)
26. The overhead could be reduced by reusing $\bar{\mathbb G}$ as an approximate Jacobian for the next step's nonlinear solve. (§6, future work) **Stated**
27. The framework "generalizes to SSP SDIRK methods and higher-order schemes [19]". (§4.2.4) **Stated**

*(Compiler checks, not in the sources.)* SDIRK32 has $b_3=-723/9272<0$ and SDIRK43 has $b_2=-400/819<0$ and $b_4=-575/252<0$, with negative $a_{ij}$ as well. Both therefore violate the $b_i\ge0$ hypothesis of §3.3 and the $a_{ij}\ge0$ hypothesis of §3.4, so the unconditional positivity guarantee does not cover two of the three tested methods. The positivity figures use SDIRK21, whose coefficients are nonnegative. The corrector argument invokes Assumption 3.1 for $\bar{\mathbb G}$, but Remark 3.9 transfers only the sign structure and left kernel. The M-matrix property follows for zero-column-sum $\mathbb G$; it is not established for MAPK, whose $\mathbb G$ "does not always have column sums equal to zero". Prop. 3.23 proves order 2 for SDIRK; the higher observed slopes do not contradict this upper bound, but rest on four problems with $\epsilon_{\mathrm c}$ unstated. The Robertson SDIRK21 slope of 1.51 and the KdV slope of 1.72 fall short of the text's "no order degradation". The MAPK sentence "for $\alpha\in(0,1)$ … two independent linear conservation laws given by the left kernel vectors" is wrong as printed. From the printed $\mathbb G$, $w_1$ is a left null vector only for $\alpha=0$ and $w_2$ only for $\alpha=1$, although both are invariants of the ODE for every $\alpha$; the paper's own bullets and tables agree with this. The overhead is called "only modest" against Table 6's +266 % and +94.5 %.

# Printed slips

- §3.4 and Eq. (27): "$Y_i=y_n+h\big(\sum_{j=1}^{i-1}a_{i,j}G(Y_j)\Sigma_{Y_j/Y^{\{p\}}_i}+h\,a_{i,i}G(\breve Y^{\{p\}}_i)\big)Y_i$"; the inner $h$ is spurious (Example (30) has none).
- Remark 3.17 cites "Corollary 3.9", which is a Remark; Prop. 3.23 cites "(3.15)" for Definition 3.15; Remark 3.20 cites Lemma 3.14 (clipping) for the size of the full correction.
- §4.2: "we carry out experiments with fixed step sizes", while §5.3 uses the adaptive mode for the ODE tests and §5.4 tolerances $10^{-7}$.
- SDIRK32 embedded weights (p. 28): the printed $\hat b=(20/51,-410011317313/22571052756900,-2075562131/281561189810,29595333/2429345900)$ sums to $0.3788$, so it is not a consistent method as printed *(compiler check)*; the main weights are correct to order 3.
- §4.2.4 describes the corrections in two-stage language ("correct only $y_{n+1}=Y_2$ … both $Y_1$ and $y_{n+1}=Y_2$") for all three methods.
- §5.1.3 says "one-day simulation", the axes of Figs. 5–7 run 15–35 h, and §4.1.3 says typically three days.
- p. 22: the Robertson reaction scheme "$A\to B$, $B+B\to B+C\to A+C$" conflates $B+B\to C+B$ and $B+C\to A+C$.
- Fig. 28 caption: "positivity correction applied only to all stages".
- The value of $\varepsilon$ used in the experiments is never stated, although Prop. 3.23 makes the order depend on it; the KdV coefficients, mesh and shift are not given either.
- Ref. [27] prints an ISBN in the DOI field. Typos: "appy" (p. 15), "loose" (p. 16), "Roberston's" and "it's own" (p. 20), "Assesment" (§5.3), "absolute ans relative" (§5.3.2).

# Notation map

| Nurkhametova et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol y$, $N$, $d$ | $y$, $d$ | |
| $P_i$, $D_i$, $p_{i,j}$, $d_{i,j}$ | $p_{ij}$, $d_{ij}$; row sums kept | $p_{ij}=d_{ji}$; $d_{ij}$ the rate from $i$ to $j$ |
| $\ell_{i,j}$, $L$ | $\ell_{ij}$, $\mathcal L$ (page-local) | **transition-rate matrix renamed: the registry $L$ is the linear operator** |
| $G(t,y)$, $\bar G$, $\bar G_i$ | $\mathbb G(t,y)$, $\bar{\mathbb G}$, $\bar{\mathbb G}_i$ (page-local) | graph-Laplacian factor and its corrected averages; renamed as on [modified Patankar methods](/methods/modified-patankar-methods.md): **$G$ is the registry G-norm matrix** |
| $H(y)$, $D(y)$ | kept, page-local | form $y'=H(y)\mathbf 1$; **$H$ is not the multirate macro step** |
| $w_j$, $M$ | $w_j$, kept | left null vectors and their number; **$M$ collides with the registry mass matrix** |
| $\mathbf 1_d$ | $\mathbf 1$ | |
| $\succeq0$, $\succ0$ | $\ge0$, $>0$ componentwise | |
| $h$, $n$, $s$, $a_{i,j}$, $b_j$, $c_i$, $\gamma$ | $h$, $n$, $s$, $a_{ij}$, $b_j$, $c_i$, $\gamma$ | SDIRK diagonal $\gamma$; stiffly accurate $b_j=a_{sj}$ |
| $Y_i$ | $Y_i$ | stage values |
| $y^{\{p\}}_{n+1}$, $Y^{\{p\}}_i$ | $y^{\mathrm p}_{n+1}$, $Y^{\mathrm p}_i$ (page-local) | predicted solution and stage; **the superscript is not the order $p$** |
| $\breve Y$, $\Sigma_{Y/Z}$ | kept, page-local | clipping and ratio scaling |
| $\max(Z_\ell,\varepsilon)$ in $\Sigma$ | $\varpi_\ell$ | Patankar weight denominator of the corrector |
| $\varepsilon$ | $\epsilon_{\mathrm c}$ (page-local) | scaling threshold; **renamed: $\varepsilon$ is the registry stiffness parameter** |
| $p$, $q$ | $p$, $q$ | classical order and stage order (not weak stage order) |
| $\hat y_{n+1}$, $LTE$ | $\hat y_{n+1}$, $\mathrm{err}_n$ before scaling | embedded solution and local error estimate |
| RelTol, AbsTol | $\mathrm{rtol}$, $\mathrm{atol}$ | |
| $E_I$ | kept | maximum relative invariant deviation (47) |
| $\alpha$ (MAPK) | kept, page-local | factorization parameter in $[0,1]$; **not a Shu–Osher or multistep coefficient** |
| $\alpha$, $\rho$, $\nu$ (KdV) | kept, page-local | advection, transport and dispersion coefficients; **$\nu$ is not the Courant number** |
| $\sigma(t)$, $\gamma$ (stratospheric) | kept, page-local | diurnal photolysis factor and a rate sum; **not the tree symmetry or the SDIRK $\gamma$** |

# Reference list

28 printed references, numbered [1]–[28] and ordered alphabetically by first author. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` nurkhametova-2026. [15] is Izgin, Kopecz & Meister's ESAIM M2AN 56 (2022) paper on Lyapunov stability of MPRK schemes (key `izgin-2022`); [16] is the same authors' different SIAM J. Numer. Anal. 60 (2022) paper (key `izgin-2022-d`). [8] and [9] are the two Hairer–Nørsett–Wanner and Hairer–Wanner volumes (`hairer-1993`, `hairer-1996`). [5] is an arXiv preprint (De Jager 2006). [7], [12] and [17] print "et al." author lists. [13] is cited as chapter 1 of Hundsdorfer–Verwer with the printed reprint year 2013. [27] prints an ISBN in its DOI field, kept in a note. DOIs are printed for [1], [5], [24], [25], [26] and [28]. No printed duplicates; no unparseable item.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md)
* [Lyapunov stability of steady states of positive, conservative time integrators](/results/lyapunov-stability-positive-conservative-schemes.md)
* [Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)](/methods/modified-patankar-methods.md)
* [Order reduction](/definitions/order-reduction.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Production–destruction systems](/definitions/production-destruction-system.md)
* [Robertson problem](/benchmarks/robertson-problem.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md)
