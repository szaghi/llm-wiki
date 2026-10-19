---
type: Source
title: "Gottlieb et al. (2022) — High Order Strong Stability Preserving MultiDerivative Implicit and IMEX Runge–Kutta Methods with Asymptotic Preserving Properties"
description: "Introduces the backward derivative condition and builds two-derivative implicit Runge–Kutta methods of orders 2–4 that are SSP for any step size, plus SSP IMEX multiderivative methods of orders 2 and 3 that are positivity- and asymptotic-preserving for stiff kinetic relaxation systems."
resource: "doi:10.1137/21m1403175"
source_kind: paper
authors: [Gottlieb S., Grant Z.J., Hu J., Shu R.]
year: 2022
venue: "SIAM J. Numer. Anal. 60:423-449"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_SIAM_Journal_on_Numerical_Analysis_Gottlieb_High_Order_Strong_Stability_Preserving_MultiDerivative_Impli.pdf"
tags: [ssp, multiderivative, imex, positivity, asymptotic-preserving]
timestamp: 2026-10-19T00:00:00Z
---

# Summary

Implicit [SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
of order above one have a bounded SSP coefficient $\mathcal C$, so the stiff operator
always restricts the step. The paper removes this restriction with a
[two-derivative Runge–Kutta](/methods/multiderivative-runge-kutta.md) formulation that
uses both $f$ and $\dot f=f'f$, and a new **backward derivative condition**
$\lVert y-h^2\dot f(y)\rVert\le\lVert y\rVert$ for $h^2\le\dot k\,h_{\mathrm{FE}}^2$.
A method written in an implicit-only Shu–Osher form, with non-negative convex
coefficients, non-negative diagonal coefficients $d_{ii}$ on $f$ and non-positive
diagonal coefficients $\dot d_{ii}$ on $\dot f$, satisfies
$\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for every $h>0$ (Theorem 1). Such methods are
found for orders 2 (one stage, the implicit Taylor method), 3 (two stages) and 4
(five stages); the search found none of order 5. Appendix A shows why the earlier
second-derivative and Taylor-series conditions cannot give unconditional SSP beyond
first order.

The construction is extended to [IMEX](/methods/imex-runge-kutta.md) multiderivative
methods for $y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$: explicit SSP treatment of
$f^{\mathrm E}$, implicit $f^{\mathrm I}$ and $\dot f^{\mathrm I}$ on the diagonal.
Theorem 2 gives strong stability for $h\le r\,h_{\mathrm{FE}}$, independent of
$f^{\mathrm I}$. New order conditions up to order 3 for this three-tableau class
(see [order conditions](/results/runge-kutta-order-conditions.md)) yield a 3-stage
second-order method with $r=1$ and a 6-stage third-order method with
$r\approx0.9044$. For stiff kinetic relaxation systems
$y'=f^{\mathrm E}(y)+\frac1\varepsilon Q(y)$ with $\dot Q=-C_{\mathcal Ry}Q$,
Proposition 1 proves [positivity](/properties/positivity-preservation.md) for
$h\le r\,h_{\mathrm{FE}}$ independent of $\varepsilon$, and the
[asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) property when
every stage contains $Q$ or $\dot Q$. Numerical tests (a scalar ODE against
[DIRK](/methods/diagonally-implicit-runge-kutta.md) methods, a stiff ODE model,
Broadwell, BGK) confirm positivity and AP behaviour and show
[order reduction](/definitions/order-reduction.md) at intermediate $\varepsilon$.

# Version read

arXiv:2102.11939v3 [math.NA], 9 Aug 2021, 27 pages (24 main text, Appendix A on
pp. 25–26, references on pp. 26–27), with revised passages typeset in blue. It is not
the SIAM version of record (pp. 423–449). Page 1 prints "MULTI-DERIVATIVE" where
Crossref has "MultiDerivative", and Crossref's "Runge--Kutta" is the TeX form of the
printed "Runge–Kutta". These are the same work, with the same authors in the same
order. Theorem, equation, section and page numbers on this page are those of the
arXiv v3.

# Key claims

1. Under the forward Euler condition on $f$ and the backward derivative condition on $\dot f$, a two-derivative method in the implicit Shu–Osher form (11) with $r_i\ge0$, $p_{ij}\ge0$, $d_{ii}\ge0$, $\dot d_{ii}\le0$ satisfies $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for any $h>0$ (§2.2, Thm. 1, Eq. (12)). **Proved**
2. Form (11), with only implicit (diagonal) evaluations of $f$ and $\dot f$, is necessary but not sufficient for having no SSP step restriction (§2.2, citing [10]). **Stated**
3. Every method of form (11) has a Butcher form (9) with $A=\mathbf R^{-1}\mathbf D$, $\dot A=\mathbf R^{-1}\dot{\mathbf D}$; the converse with diagonal $\mathbf D$, $\dot{\mathbf D}$ is not always possible (§2.2). **Stated**
4. The one-stage implicit Taylor method $y_{n+1}=y_n+hf(y_{n+1})-\tfrac12h^2\dot f(y_{n+1})$ is second order and unconditionally SSP (§2.3). **Proved** (via Thm. 1)
5. A two-stage third-order unconditionally SSP implicit two-derivative method exists, with $A=\begin{bmatrix}0&0\\0&1\end{bmatrix}$, $\dot A=\begin{bmatrix}-\tfrac16&0\\-\tfrac16&-\tfrac13\end{bmatrix}$ (§2.3). **Proved** (coefficients satisfy Thm. 1 and the order conditions; the reader checked them numerically)
6. A five-stage fourth-order unconditionally SSP implicit two-derivative method exists, with 15-digit coefficients (§2.3). **Shown** (optimization output; the reader checked that the Shu–Osher coefficients satisfy all eight order conditions to about $10^{-15}$)
7. The authors "were unable to find any fifth order methods that satisfy the conditions in Theorem 1" (§2.3). **Stated** (a failed search, not a proved barrier)
8. Under the earlier conditions (forward Euler plus the second-derivative condition (4), or plus the Taylor-series condition (5)), which need $\dot d_{ii}\ge0$, a method of form (10) cannot be second order, so no unconditionally SSP implicit two-derivative method exists in those senses (App. A, Eq. (62), adapting [11]). **Proved**
9. For $y'=-10y^2$, $y(0)=10$: forward Euler positivity needs $h\le0.1/y_n$ and the backward derivative step needs $h^2\le0.005/y_n^2$; the new methods stay positive for every $h$ tested, while the second-order DIRK loses positivity for $h>1/50$ and the third-order DIRK for $h>1/75$ (§2.4, Fig. 1). **Shown**
10. For general convex functionals, IMEX Runge–Kutta does not remove the step restriction caused by the stiff operator $f^{\mathrm I}$ (§3, citing [13, 7]). **Stated**
11. The multiderivative IMEX method (14) with $r>0$ and $r_i,p_{ij},w_{ij},d_{ii}\ge0$, $\dot d_{ii}\le0$ is strongly stable for $h\le r\,h_{\mathrm{FE}}$, with no restriction from $f^{\mathrm I}$ or $\dot f^{\mathrm I}$, under Conditions 1–3 (§3.1, Thm. 2, Eq. (15)). **Proved**
12. The order conditions of the IMEX multiderivative class (16) up to order 3 (22 conditions, table on p. 11) "have not appeared previously" (Abstract, §3.2). **Derived**
13. A three-stage second-order SSP IMEX multiderivative method has $r=1$, against $r=0.8125$ for the method of [16] §2.6.2, a 23% larger allowable step; both need three implicit stage solves (§3.3.1, §3.4). **Proved** (coefficients) / ratio **Stated** ($1/0.8125=1.2308$, consistent)
14. A six-stage third-order SSP IMEX multiderivative method has $r=0.904402174130635$; "To achieve a third order method we required six stages" (§3.3.2). **Shown** (optimization output; the reader checked all 22 order conditions and the Butcher conversion numerically)
15. Positivity- and AP-preserving IMEX schemes beyond first order generally violate positivity unless $h$ is restricted by $\varepsilon$ [13, 14]; earlier second-order schemes with both properties [17, 16] used a derivative correction at the final stage and did not reach order 3 (§3.4). **Stated**
16. Under Properties 1–5, scheme (13) with (49) preserves positivity for $h\le r\,h_{\mathrm{FE}}$ for every $\varepsilon$. If also $d_{ii}+\lvert\dot d_{ii}\rvert>0$ for all $i$ (50), it is AP: as $\varepsilon\to0$ with $h$ fixed it reduces to the explicit part of (13) applied to the limiting system (21), "with the same order as the original scheme" (§3.4.2, Prop. 1). **Proved**
17. The new IMEX schemes are type A and globally stiffly accurate in the classification of Boscarino–Pareschi–Russo [2], and any initial condition is allowed for AP (Remark 2). **Stated** (here $A^{\mathrm I}$ alone is singular for both new methods; "type A" is meant in the combined sense $d_{ii}+\lvert\dot d_{ii}\rvert>0$, an extension of [2]'s invertibility criterion)
18. For Broadwell and BGK with first-order upwind transport, Theorem 2 with the discrete entropy as convex functional gives entropy decay $S[f^{n+1}]\le S[f^n]$ (Remark 3, Eqs. (53)–(56)). **Stated** (verification deferred to [16])
19. The order conditions do not exclude order reduction: some is seen at intermediate $\varepsilon$, and the AP property restores full accuracy as $\varepsilon\to0$ (Remark 4, §3.5). **Shown**
20. On the stiff ODE model (29) with $f=1+y_1^2$, $g=\sin y_1$, design orders 2 and 3 appear in the kinetic ($\varepsilon=O(1)$, small $h$) and fluid ($\varepsilon\ll1$) regimes, with order reduction between them; round-off makes the error grow for $h<5\times10^{-5}$ at $\varepsilon=1$ (third order) (§3.5.1, Figs. 2–3). **Shown**
21. The intermediate error plateaus at $O(\varepsilon)$ in Figs. 2–3 are not the usual AP order reduction and not round-off, and step-doubling self-convergence still shows the design order; the explanation is "likely" in higher-order asymptotic expansions (§3.5.1). **Shown** / explanation **Stated**
22. Broadwell with WENO5 finite volumes, $h=\tfrac12\Delta x$, $T=0.1$, behaves like the ODE model (§3.5.2, Figs. 4–5). **Shown**
23. On 1D BGK, second order is seen for small $h$ at $\varepsilon=O(1)$ and $\varepsilon\ll1$, with order reduction between; the third-order scheme converges faster than expected because spatial error dominates, but its error is much smaller than the second-order one at the same $h$ (§3.5.3, Figs. 6–7). **Shown**
24. Mixed-regime BGK ($\varepsilon(x)$ from $10^{-5}$ to $O(1)$), WENO5 with a positivity-preserving limiter, $N_x=40$, $h=\frac1{24}\Delta x/v_{\max}$: no negative cell average appears, and the solution agrees with an explicit SSPRK2 reference ($N_x=80$, $h=\frac1{240}\Delta x/v_{\max}$) (§3.5.3, Fig. 8). **Shown**
25. Unconditionally SSP methods of order $p>2$ are new, "unique among SSP methods" (Abstract, §4); Ketcheson's downwind-based unconditionally SSP implicit methods [20] are second order (§1). **Stated**

# Printed slips

- §2.3, fourth-order Butcher coefficients: the subscripts are transposed against the lower-triangular convention of (8) ("$a_{12}=a_{13}=a_{11}$, $a_{14}=a_{15}=0.060653001401867$, … $a_{45}=a_{44}$" denote entries (2,1), (3,1), (4,1), (5,1), …, (5,4)); confirmed by reconstructing $A=\mathbf R^{-1}\mathbf D$ from the Shu–Osher coefficients.
- §2.3: "$\dot a_{12}=a_{13}=\dot a_{11}$": the middle term should be $\dot a_{13}$.
- §2.3: $a_{14}=0.060653001401867$ against the reconstructed $0.060653001401868$ (last-digit rounding).
- Proof of Thm. 2 (p. 9): "$u^{(1)}=u^n+\Delta t d_{11}G(u^{(i)})+\Delta t^2\dot d_{11}\dot G(u^{(i)})$": the arguments should be $u^{(1)}$.
- Proof of Thm. 2 (p. 10): "Given the non-negativity of all the coefficients (12)": should cite (15), since (12) lacks $\mathbf W$.
- Proof of Thm. 2: "from the condition $R+W+P=I$": the fact needed is the row-sum identity $r_i+\sum_j(p_{ij}+w_{ij})=1$.
- Eq. (61), mixed-regime $\varepsilon(x)=\varepsilon_0+(\tanh(1-11(x-1))+\tanh(1+11(x-1)))$, printed without a factor $\tfrac12$ (peak $\approx2\tanh1\approx1.52$); compare with [16] §5.3 before reusing it.
- Typos: "coeffiicients" (§3.3.2), "the the CFL number" (§3.5.2, §3.5.3), "equilbrium" (§3.5.1).
- Figs. 2–7: the abscissa is labelled "t" where $\Delta t$ is meant (as extracted).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u^n$, $u_t=G(u)$ | $y$, $y_n$, $y'=f(y)$ | autonomous throughout |
| $\Delta t$, $\Delta t_{FE}$ | $h$, $h_{\mathrm{FE}}$ | |
| $\dot G=G'(u)G(u)$ | $\dot f=f'(y)f(y)$ | agrees with the multiderivative entry |
| $u^{(i)}$, $U$ | $Y_i$ | stage values; the last stage is $y_{n+1}$ (stiffly accurate by construction) |
| $\mathbf A$, $\dot{\mathbf A}$ | $A$ (or $A^{\mathrm I}$ in the IMEX case), $\dot A=(\dot a_{ij})$ | |
| **$\hat{\mathbf A}$, $\hat{\mathbf b}$, $\hat{\mathbf c}$** | $A^{\mathrm E}$, $b^{\mathrm E}$, $c^{\mathrm E}$ | **collision:** the source hat marks the explicit tableau; the registry hat marks embedded weights |
| $\mathbf b$, $\dot{\mathbf b}$, $\mathbf c=\mathbf A\mathbf e$, $\dot{\mathbf c}$ | $b$, $\dot b$, $c$, $\dot c=\dot A\mathbf 1$ | |
| $\mathbf e$ | $\mathbf 1$ | |
| $F$, $G$ (IMEX) | $f^{\mathrm E}$, $f^{\mathrm I}$ | |
| $T(u)$, $\frac1\varepsilon Q(u)$ | $f^{\mathrm E}(y)$, $f^{\mathrm I}=\frac1\varepsilon Q(y)$ | **$T$ collides** with the registry set of rooted trees; written $f^{\mathrm E}$ here |
| $\varepsilon$ | $\varepsilon$ | agrees (Knudsen / relaxation parameter) |
| $C$ | $\mathcal C$ | SSP coefficient, not divided by $s$ |
| $r$ | SSP coefficient of the explicit part | kept; no registry symbol |
| $\mathbf P$, $\mathbf W$, $\mathbf{Re}$, $r_i$ | Shu–Osher coefficients | kept; with $\alpha_{ij}=p_{ij}+w_{ij}$ and $\beta_{ij}=w_{ij}/r$ on the explicit part |
| **$\mathbf R=\mathbf I-\mathbf P-\mathbf W$** | kept | **not** the stability function $R(z)$ |
| **$\mathbf D$, $\dot{\mathbf D}$**, $d_{ii}$, $\dot d_{ii}$ | kept | diagonal implicit coefficients; **not** the simplifying assumption $D(\zeta)$ |
| $\tilde k$, $\hat k$, $\dot k$, $k$ | kept | constants of the conditions (4), (5), (6), Condition 2 |
| $\lVert\cdot\rVert$ | $\lVert\cdot\rVert$ | here any convex functional (norm, semi-norm, positivity) |
| $\mathcal R$, $E$, $\omega$, $C_{\mathcal Ru}$ | kept | conservation projection, equilibrium map, macroscopic variable, Property 5 factor |
| **$M$** | kept on this page | Maxwellian of the BGK model; **collides** with the registry mass matrix |
| $p$ | $p$ | classical order; stage order is not discussed |

# Reference list

24 printed references, numbered [1]–[24] in SIAM style, alphabetical by first author,
with no DOIs printed. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` gottlieb-2022. Two same-key pairs
take suffixes in printed order (Higueras 2006 / Higueras & Roldán 2006; Shu 1988 /
Shu & Osher 1988). [9] is printed with an author dash (same authors as [8]), [19] is
a NASA technical memorandum, and [5] prints its volume in Roman numerals (XLVII). No
printed duplicates and no unparseable items.

# Pages created or updated

Chunk 1 (2026-10-19). This source is cited on:

* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Multiderivative Runge–Kutta methods and the backward derivative condition](/methods/multiderivative-runge-kutta.md)
* [Order reduction](/definitions/order-reduction.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
