---
type: Source
title: "Roberts et al. (2021) — Implicit Multirate GARK Methods"
description: "Casts implicit–implicit multirate Runge–Kutta methods as GARK schemes, builds a scalar and 2D linear stability theory with two A-stability barriers, analyses Newton solves, and derives compound-fast MrGARK methods of orders two to four."
resource: "doi:10.1007/s10915-020-01400-z"
source_kind: paper
authors: [Roberts S., Loffeld J., Sarshar A., Woodward C.S., Sandu A.]
year: 2021
venue: "J. Sci. Comput. 87:4"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Scientific_Computing_Roberts_Implicit_Multirate_GARK_Methods.pdf"
tags: [multirate, implicit, stability, order-conditions, linear-algebra]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper develops multirate Runge–Kutta methods for stiff problems $y'=f^{\{\mathrm f\}}(y)+f^{\{\mathrm s\}}(y)$ in which both the fast and the slow partitions are treated implicitly, inside the [GARK framework](/methods/generalized-additive-runge-kutta.md). Two families are written as GARK schemes: standard [MrGARK](/methods/multirate-gark.md) and compound-fast MrGARK, which takes one compound macro step $H$ on the whole of $f$ and then re-integrates the fast part over $m$ micro steps $h=H/m$. For the compound-fast family the paper proves the fourth-order coupling conditions.

The core is a [linear stability theory for multirate methods](/definitions/multirate-linear-stability.md). It uses a scalar test problem with stability function $R_1(z^{\{\mathrm f\}},z^{\{\mathrm s\}})$ and the 2D Gear test problem in real and complex variants. It defines scalar [A-, L-, A($\alpha$)- and L($\alpha$)-stability](/properties/a-stability.md), gives an imaginary-axis criterion for scalar A-stability, and orders the notions in a hierarchy. Two impossibility results follow ([multirate A-stability barriers](/results/multirate-a-stability-barriers.md)): no consistent decoupled GARK method is A-stable for the real 2D test problem, and an internally consistent MrGARK method of order exactly one is scalar A-stable for only finitely many ratios $m$.

Section 4 analyses the Newton iterations of the coupled stage systems: cost, Jacobian reuse, "stage reducibility" and Woodbury-type reductions ([implicit stage solvers](/methods/implicit-stage-solvers.md)). Section 5 derives new methods on [SDIRK](/methods/diagonally-implicit-runge-kutta.md) bases: multirate backward Euler and implicit midpoint, two internally consistent SDIRK2 methods with poor stability, and compound-fast SDIRK2, SDIRK3 and a new five-stage [stiffly accurate](/properties/stiff-accuracy.md) SDIRK4. The compound-fast methods have scalar L($\alpha$) angles of about 83°, 86.8° and 81.2° that hardly change with $m$. On a 500-inverter MOSFET chain the compound-fast methods run 4–6 times faster than single-rate SDIRK at orders 2–3, are slightly better than [IMEX ARK](/methods/imex-runge-kutta.md), and run about 3 times faster than single rate at order 4.

# Version read

arXiv:1910.14079v3 [math.NA], 1 Dec 2020: a cover sheet (Virginia Tech Computational Science Laboratory Report CSL-TR-19-5, 2 Dec 2020) followed by the author manuscript in the Springer "Noname manuscript" template, not the typeset version of record. The file has 36 PDF pages (cover, main text, appendices A–C, references); PDF page = printed page + 1. Title and the five authors match Crossref. Page, equation and theorem numbers on this page are those of the arXiv v3 and may differ from the journal article. The displayed mathematics was checked visually because text extraction scrambled it; nothing was illegible.

# Key claims

Notation: $f^{\{\mathrm f\}}$, $f^{\{\mathrm s\}}$ fast and slow parts, $H$ macro step, $h=H/m$ micro step, $m$ multirate ratio, $\ell=1,\dots,m$ micro-step index, $(A,b,c)$ base method, $A^{\{\mathrm f,\mathrm s,\ell\}}$ slow-to-fast coupling of micro step $\ell$ (see the notation map).

1. An internally consistent compound-fast MrGARK method has order four iff its base method $(A,b,c)$ has order four and the coupling conditions (2.7a)–(2.7f) hold: $mA^{\{\mathrm f,\mathrm s,\ell\}}\mathbf 1=(\ell-1)\mathbf 1+c$; $\tfrac m6=\sum_\ell b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c$; $\tfrac{m^2}8=\sum_\ell(\ell-1)b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c+\sum_\ell(b\times c)^\top A^{\{\mathrm f,\mathrm s,\ell\}}c$; $\tfrac m{12}=\sum_\ell b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c^2$; $\tfrac{m^2}{24}=\sum_\ell b^\top AA^{\{\mathrm f,\mathrm s,\ell\}}c+\sum_\ell(m-\ell)b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c$; $\tfrac m{24}=\sum_\ell b^\top A^{\{\mathrm f,\mathrm s,\ell\}}Ac$ ($\times$ and $c^2$ componentwise). Of the GARK conditions 3a–4j, 3b, 4b, 4d and 4h–4j reduce to base-method conditions and 4g coincides with 4f. (Thm 2.1, §2.2, pp. 6–8) **Proved**
2. The compound-fast family is telescopic, coupled only in the compound macro step (2.6a) and decoupled in the fast micro steps (2.6b). Order is preserved if the interpolant behind $A^{\{\mathrm f,\mathrm s,\ell\}}$ is accurate enough; that is sufficient, not necessary. (§2.2, p. 6) **Stated**
3. Unlike single-rate Runge–Kutta, multirate and partitioned linear stability depends on the basis, so a scalar test equation is not enough (after Gear). (§3, p. 9) **Stated**
4. A GARK method is scalar A-stable iff $\lvert R_1(iy^{\{\mathrm f\}},iy^{\{\mathrm s\}})\rvert\le1$ for all real $y^{\{\mathrm f\}},y^{\{\mathrm s\}}$ and $R_1$ is analytic on $\mathbb C^-\times\mathbb C^-$; this reduces the check from four real dimensions to two. (Thm 3.1, eq. 3.6, p. 10) **Proved** (by the multivariate maximum principle)
5. The two-variable E-polynomial $E_1(y^{\{\mathrm f\}},y^{\{\mathrm s\}})=Q_1(iy^{\{\mathrm f\}},iy^{\{\mathrm s\}})Q_1(-iy^{\{\mathrm f\}},-iy^{\{\mathrm s\}})-P_1(iy^{\{\mathrm f\}},iy^{\{\mathrm s\}})P_1(-iy^{\{\mathrm f\}},-iy^{\{\mathrm s\}})$, with $R_1=P_1/Q_1$, is nonnegative on $\mathbb R^2$ iff the scalar stability region contains the imaginary axes. (Thm 3.2, p. 10) **Proved**
6. The GARK method with tableau $\frac{1|0}{1|1}$, weights $(1|1)$, is scalar L-stable and algebraically stable, yet $\rho\big(R_2\big(\begin{smallmatrix}-1&1\\-10&-1\end{smallmatrix}\big)\big)=\frac{\sqrt5+3}{4}>1$; it is therefore only conditionally stable for the real and complex 2D test problems. (§3.3, pp. 12–13) **Proved** (explicit computation)
7. A GARK method whose base method is only A(45°)-stable has $\lvert R_1(-4+8i,0)\rvert=\sqrt{17}/4>1$, yet is A-stable for the real 2D test problem. Real-2D A-stability therefore does not imply scalar A-stability: the real 2D test cannot detect base-method instabilities off the real axis. (eq. 3.12, p. 13) **Proved** for the scalar value; the real-2D A-stability is asserted, so **Stated**
8. Complex-2D A-stability implies scalar A-stability. (Thm 3.3, pp. 13–14, via identity (3.13b)) **Proved**
9. Hierarchy (Fig. 3.1): complex 2D A ⇒ real 2D A; complex 2D A ⇒ scalar A; algebraic stability ⇒ scalar A; scalar L ⇒ scalar A; scalar A ⇒ scalar A($\alpha$); scalar L ⇒ scalar L($\alpha$) ⇒ scalar A($\alpha$). "In general, no implication arrows are reversible." (Fig. 3.1, p. 14) **Stated**/**Proved** in parts
10. For a decoupled GARK method the off-diagonal coupling matrix $\begin{bmatrix}0&\mathbf A^{\{\mathrm f,\mathrm s\}}\\\mathbf A^{\{\mathrm s,\mathrm f\}}&0\end{bmatrix}$ is nilpotent. (Lemma 3.1, p. 14) **Proved** (graph argument)
11. No decoupled GARK method consistent with (1.1) (first-order accurate) is A-stable for the real 2D test problem: on $y'=\begin{bmatrix}0&\eta\\-\eta&0\end{bmatrix}y$, $\det R_2(w)=1+w^2+\mathcal O(w^4)$, $w=H\eta$, grows without bound. (Thm 3.4, pp. 14–15) **Proved**
12. The 2D stability matrix on the skew test problem (3.9) depends only on the coupling coefficients $\mathbf A^{\{\mathrm f,\mathrm s\}},\mathbf A^{\{\mathrm s,\mathrm f\}}$, not on the base methods. (eq. 3.10, p. 12) **Derived**
13. The scalar stability of compound-fast MrGARK is computable with $s\times s$ matrices only (eqs. 3.16–3.17 and the formula for $R_1$, pp. 15–16). If $A$ is invertible, $\lim_{z^{\{\mathrm f\}}\to-\infty}R_1=R(-\infty)^m$; under (3.18), $A^{\{\mathrm f,\mathrm s,\ell\}}A^{-1}\mathbf 1=\mathbf 1$ for $\ell=1,\dots,m$, $\lim_{z^{\{\mathrm s\}}\to-\infty}R_1=R(-\infty)$. (§3.4, pp. 15–17) **Derived**
14. Newton cost, assuming direct solves dominate: decoupled DIRK-based methods cost $\mathcal O(\mathbf sd^3)$ per step ($\mathbf s$ the total GARK stage count), reduced to $\mathcal O(md^3)$ when the slow factorization is reused per macro step and the fast one per micro step; compound-fast methods cost $\mathcal O(md^3)$, or $\mathcal O(d^3+m(d^{\{\mathrm f\}})^3)$ for component-partitioned systems. (§4.1–4.2, p. 18) **Derived**
15. Stage reducibility: when a GARK coefficient row is repeated across partitions, the Newton system collapses; e.g. the ARK tableau $(\tfrac12|1;\tfrac12|1;1|1)$ gives $(I-\tfrac H2J_1^{\{\mathrm f\}}-HJ_1^{\{\mathrm s\}})\delta=\dots$ (eq. 4.5). Matrices $I-h\gamma J^{\{\mathrm f\}}-H\gamma J^{\{\mathrm s\}}$ can be much better conditioned than $I-H\gamma J$ when $m$ matches the stiffness ratio. (§4.3, p. 19) **Derived** (conditioning argued, not measured)
16. An internally consistent MrGARK method of order exactly one is scalar A-stable for only a finite number of multirate ratios $m$. The proof is a Hessian/saddle argument on $\lvert R_1(i\omega^{\{\mathrm f\}}y,i\omega^{\{\mathrm s\}}y)\rvert^2=1+y^2p+\mathcal O(y^4)$ with $\det H=-4(r^{\{\mathrm f\}}-r^{\{\mathrm s\}})^2$ (here $p$ is a coefficient and $H$ the Hessian, as printed). (Thm 5.1, pp. 20–21) **Proved**
17. The new coupled multirate backward Euler (5.2) is internally inconsistent and scalar L- and algebraically stable for all $m$; its one coupled stage is cheap by stage reducibility. (§5.1, p. 21) **Stated** (no proof shown)
18. The decoupled multirate backward Euler (5.3) is internally inconsistent, has no second-order coupling error when $m$ is even, is scalar L- and algebraically stable for all $m$, and equals subcycled Strang splitting $\varphi_H=(\varphi^{\{\mathrm f\}}_h)^{m/2}\circ\varphi^{\{\mathrm s\}}_H\circ(\varphi^{\{\mathrm f\}}_h)^{m/2}+\mathcal O(H^2)$ with each flow replaced by one backward Euler step. (§5.1, p. 21) **Stated**
19. The coupled multirate midpoint ($m$ odd) and decoupled multirate midpoint ($m$ even, couplings (5.3)) keep the algebraic stability, symmetry and symplecticity of the implicit midpoint rule; only odd-order terms appear in the error expansion, so they suit multirate extrapolation. (§5.2, p. 22) **Stated**
20. With the L-stable SDIRK2 base (5.4), any internally consistent standard MrGARK method needs at least one coupled stage; enforcing stiff accuracy in both partitions uniquely determines the lightly coupled method (5.5). (§5.2, p. 22) **Stated**
21. Methods (5.5) and the Kværnø–Rentrop-type method (5.6) have identical scalar stability functions for all $m$; they are only scalar L(69.2°)-stable at $m=2$ and not even L(0°)-stable by $m=6$. The authors "cannot recommend them as general-purpose multirate methods" and conclude "it appears that internal consistency negatively affects the stability". (§5.2, p. 23) **Shown** (computed angles)
22. Kværnø–Rentrop coupling on the algebraically stable two-stage order-3 base (5.8) gives coupling coefficients that grow without bound in $m$ at third order; no A(0°)-stable method satisfying (5.10)–(5.11) was found. (§5.3, p. 24) **Stated** (negative search result)
23. Scalar L($\alpha$) angles of the new compound-fast methods, for $m=2,3,4,8,16,32$: SDIRK2 (5.7) 84.6°, 83.5°, 83.2°, 83.0°, 83.0°, 83.0°; SDIRK3 (A.2) 88.6°, 87.8°, 87.3°, 86.9°, 86.8°, 86.8°; SDIRK4 (B.2) 81.7°, 81.2°, 81.2°, 81.2°, 81.2°, 81.2° — "just a few degrees short of scalar L-stability", falling by less than 2° as $m$ grows. (Table 5.1, p. 24) **Shown**
24. CUSP convergence for $m=2,4,6$: observed orders closely match the nominal ones for decoupled midpoint and compound-fast SDIRK2/3; for SDIRK4 the observed rate is "slightly higher than the nominal order"; for a fixed number of steps the error decreases as $m$ increases. (Fig. 6.1, §6.1, pp. 25–26) **Shown**
25. Inverter chain (500 inverters, $\Gamma=100$, $t\in[0,120]$, serial C code on the Virginia Tech ARC "Cascades" cluster): at orders 2 and 3 compound-fast MrGARK ($m=14$, $m=10$) reaches a fixed accuracy "four to six times faster than the single rate methods" and is "slightly more efficient than the IMEX methods"; at order 4 ($m=6$) multirate and IMEX perform alike, both about 3 times faster than single-rate SDIRK4. (Fig. 6.2, §6.2, p. 27) **Shown**
26. Largest stable/Newton-convergent step sizes on the inverter chain (single-rate implicit / single-rate explicit / IMEX / compound-fast): order 2: $7.1\times10^{-2}$ / $3.1\times10^{-3}$ / $3.2\times10^{-3}$ / $7.1\times10^{-2}$; order 3: $5.2\times10^{-2}$ / $3.2\times10^{-3}$ / $3.5\times10^{-3}$ / $5.2\times10^{-2}$; order 4: $6.0\times10^{-2}$ / $3.4\times10^{-3}$ / $5.2\times10^{-3}$ / $6.0\times10^{-2}$. IMEX has "an explicit-like stepsize restriction"; compound-fast matches implicit single rate, so stiffness in the slow partition limits the step. (Table 6.1, p. 29) **Shown**
27. Conclusions: forgoing internal consistency can improve stability but increases the number of order conditions and "limits the stage order to zero"; the compound-fast methods up to order four are, to the authors' knowledge, "the highest of this type"; for base methods with more than one stage no standard MrGARK method with satisfactory stability was found, so extrapolation "may be the most practical way to achieve high-order". (§7, p. 29) **Stated**
28. A general GARK method does not preserve linear invariants $\zeta^\top y$. It does if each partition separately satisfies $\zeta^\top f^{\{\cdot\}}=0$, or if $A^{\{\mathrm f,\mathrm f\}}=A^{\{\mathrm s,\mathrm f\}}$, $A^{\{\mathrm f,\mathrm s\}}=A^{\{\mathrm s,\mathrm s\}}$, $b^{\{\mathrm f\}}=b^{\{\mathrm s\}}$ (C.3), in which case the method is a partitioned Runge–Kutta method known to preserve linear invariants. (App. C, p. 33) **Derived**

# Printed slips

- p. 2: "Jacobain of f" for "Jacobian".
- p. 5: "has been use in [31, 28]" for "used"; the same sentence cites "[32, 39] for multirate infinitesimal step methods", but [32] is the GARK paper (Sandu & Günther 2015), not an MIS paper ([31] was likely meant).
- p. 7, proof of Thm 2.1: "has order four if and only the base methods" is missing "if"; in condition 4a, line 2, the last factor is printed $c^{\{s\}}$ where the base-method $c$ is meant (line 3 uses $c$).
- p. 9: "when eq. (2.4) is applied to eq. (3.3)" — $R_1$ (3.4) is the general GARK function, so (2.1) is the natural reference. Minor.
- pp. 16–17 (§3.4): the stage vectors are named $Y^{\{f,\lambda\}}$ in the recurrence but $Y^{\{f,s,\lambda\}}$ in the $R_1$ formulas.
- p. 20: "based on single singly diagonally implicit" (doubled word).
- p. 22, eq. (5.5): the second row of $A^{\{s,f,\lambda\}}$ ($1-\gamma$, $\gamma$) carries no $\lambda$ condition while the first row is zero for $\lambda\ne1$; as printed it applies to all $\lambda$. Ambiguous; to be checked against the version of record.
- p. 24: equation numbering jumps from (5.8) to (5.10); the unnumbered display defining $A^{\{f,s,\lambda+1\}}$ and $F(\lambda)$ is presumably (5.9).
- p. 25: the inverter gate function is printed $g(U_g,U_D,U_S)$ but uses $U_G$ in its body; p. 27 "though the chain" for "through".
- p. 33, App. C: "where is is possible" for "where it is possible".
- References: [7] "Journal on Scientific Computing" for "Journal of Scientific Computing"; [20] prints "Applied Numerical Mathematics 28(327–341)" with the page range in the issue slot; [21] and [22] print CiteSeerX identifiers ("DOI 10.1.1.40.8965", "DOI 10.1.1.9.3084") as DOIs; [26] names "Journal of Research of the National Institute of Standards and Technology" for a 1960 paper (then the NBS journal) and gives no pages; [23] prints the institution truncated ("Universitet I"); [9] and [15] print no volume.
- The Strang-splitting identity (claim 18) is printed with remainder $+\mathcal O(H^2)$, whereas Strang splitting has local error $\mathcal O(H^3)$; the remainder is loose or refers to something else.

No numerical inconsistency was found between Table 5.1, Table 6.1 and the text.

# Notation map

| Roberts et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f^{\{f\}}$, $f^{\{s\}}$ | $f^{\{\mathrm f\}}$, $f^{\{\mathrm s\}}$ | additive partition (1.1); component partition (1.2) is a special case |
| $H$, $h=H/M$ | $H$, $h=H/m$ | macro and micro step |
| $M$ (multirate ratio) | $m$ | **$M$ is the mass matrix in the registry** |
| $\lambda$ (micro-step index $1..M$) | $\ell$ | **collision: the source also uses $\lambda$, $\lambda^{\{f\}}$, $\lambda^{\{s\}}$ for test-problem eigenvalues**, which keep $\lambda$; the source counts $\ell=1,\dots,m$, the registry $\ell=0,\dots,m-1$, so this page keeps the source range |
| $\mathbf A^{\{\sigma,\nu\}},\mathbf b^{\{\sigma\}},\mathbf c^{\{\sigma\}}$ (bold) | $A^{\{q,r\}}$, $b^{\{q\}}$ of the full GARK method | bold kept on this page to separate full GARK from base coefficients |
| $(A,b,c)$, $A^{\{f,f\}}$ | base method | |
| $A^{\{f,s,\lambda\}}$, $A^{\{s,f,\lambda\}}$ | $A^{\{\mathrm f,\mathrm s,\ell\}}$, $A^{\{\mathrm s,\mathrm f,\ell\}}$ | per-micro-step couplings |
| $\mathbb 1_s$ | $\mathbf 1$ | |
| $Y_i^{\{f\}}$, $Y^{\{f,\lambda\}}_i$ | $Y_i^{\{\mathrm f\}}$, $Y^{\{\mathrm f,\ell\}}_i$ | stage values |
| $z^{\{f\}}=H\lambda^{\{f\}}$, $z^{\{s\}}=H\lambda^{\{s\}}$ | same | **both scaled by the macro step $H$**: the fast base method sees $z^{\{\mathrm f\}}/m$ |
| $R(z)$, $R_1$, $P_1/Q_1$, $R_{\rm int}(z)=(I-zA)^{-1}\mathbf 1$ | $R(z)$; $R_1$, $R_{\rm int}$ kept | multirate stability function, internal stability vector |
| $R_2(Z)$, $Z=H\Lambda$ | kept | 2D stability matrix; power boundedness required |
| $S_1$, $S_2$, $\hat S_2$, $W(\alpha)$ | kept | scalar, complex-2D, real-2D stability regions; wedge $\lvert\arg(-z)\rvert<\alpha$ |
| $\gamma$ | $\gamma$ (SDIRK diagonal) | value per method: $1-1/\sqrt2$ (5.4), $(3+\sqrt3)/6$ (5.8), $\approx0.44$ (A.1), $1/4$ (B.1) |
| $\varphi^g_t$ | $\varphi_t$ of the indicated part | exact flow |
| $J_i^{\{\sigma\}}$, $\hat J$, $\hat Y$ | $J$ of each partition | stacked Newton quantities |
| $r^{\{f\}},r^{\{s\}}$ | kept | second-order residuals $\mathbf b^\top\mathbf c-\tfrac12$ |
| $m$ (number of inverters, §6.2) | — | **collides with the registry $m$; written out as "500 inverters"** |
| $\sigma$, $\varepsilon$ (CUSP model) | kept | diffusion coefficient $1/144$ (**$\sigma$ collides with tree symmetry $\sigma(\tau)$**); stiffness $10^{-4}$ |
| $\Gamma$ (inverter chain, §6.2) | kept | model parameter $\Gamma=100$; **not** the MRI-GARK coupling matrices $\Gamma^{(k)}$ |

# Reference list

47 printed references, numbered [1]–[47] in alphabetical order (Springer numbered style). The list is merged complete into the [bibliography](/bibliography.md) with `citedby` roberts-2021. Two Verhoeven 2006 works ([42], [43]) take same-key suffixes in printed order. The two Kværnø items [21], [22] have no venue and print CiteSeerX identifiers as "DOI"s; they are entered without a DOI. [6], [27], [39] and [46] are arXiv preprints ([39] "Submitted to J. Comput. Appl. Math.") and stay distinct entries. All references parsed; [23] prints its institution truncated.

# Pages created or updated

Chunk 1 (2026-10-19); updated in chunk 2 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [A-stability barriers for decoupled and internally consistent multirate methods](/results/multirate-a-stability-barriers.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Generalized additive Runge–Kutta (GARK) methods and internal consistency](/methods/generalized-additive-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Internal stability of explicit Runge–Kutta methods](/definitions/internal-stability.md)
* [Linear stability of multirate methods and joint stability regions](/definitions/multirate-linear-stability.md)
* [Multirate GARK methods (MrGARK, compound-fast, multirate backward Euler)](/methods/multirate-gark.md)
* [Multirate infinitesimal methods (MIS, MRI-GARK)](/methods/multirate-infinitesimal-methods.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stage order](/definitions/stage-order.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
