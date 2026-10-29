---
type: Source
title: "Gottlieb et al. (2001) — Strong stability-preserving high-order time discretization methods"
description: "Review with new results that renames TVD time discretizations as strong-stability-preserving (SSP) methods, proves the bound C ≤ 1 for s-stage order-s methods, gives optimal linear SSP methods of every order, SSP multistep barriers and optimal methods, and order barriers for implicit SSP methods without explicit terms."
resource: "doi:10.1137/S003614450036757X"
source_kind: paper
authors: [Gottlieb S., Shu C.-W., Tadmor E.]
year: 2001
venue: "SIAM Rev. 43(1):89-112"
local_file: "/home/stefano/papers/mosaic/ode-integration/2001_Crossref_SIAM_Review_Gottlieb_Strong_Stability-Preserving_High-Order_Time_Discretization_M.pdf"
tags: [ssp, strong-stability, runge-kutta, linear-multistep, explicit, implicit]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

The paper reviews and extends time discretizations of method-of-lines systems
$y'=L(y)$ that keep the strong stability of the forward Euler step. If
$\lVert y+hL(y)\rVert\le\lVert y\rVert$ for $h\le h_{\mathrm{FE}}$ in some
norm or convex functional, the goal is a high-order method with
$\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for $h\le\mathcal C h_{\mathrm{FE}}$
(the paper's "CFL coefficient" $c$). Because the argument uses convexity
only, the authors rename the "TVD time discretizations" of Shu–Osher, Shu
and Gottlieb–Shu as **strong stability-preserving (SSP)** methods
([SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md),
[total variation diminishing](/definitions/total-variation-diminishing.md)).

§2 recalls the convex-combination lemmas: Shu–Osher form with
$\beta_{ij}\ge0$, the downwind operator $\tilde L$ for negative $\beta_{ij}$,
and the multistep analogue. §3 proves that an $s$-stage method of order $s$
has $\mathcal C\le1$, and gives for every $s$ an explicit $s$-stage
order-$s$ linear method with $\mathcal C=1$; since the degree-$s$ Taylor
polynomial is the only [stability polynomial](/definitions/stability-function.md)
of such a method, that polynomial is SSP with coefficient 1. It applies this
to coercive linear time-dependent problems and proves bounded growth of
classical RK4 under $h\le2\eta_{\mathrm c}$, improving the
[energy-method](/methods/runge-kutta-energy-method.md) constant of
Levy–Tadmor ([strong stability](/properties/strong-stability.md)). §4
reviews the optimal SSPRK(2,2) and SSPRK(3,3), the four-stage fourth-order
negative-coefficient result, a fourth-order method with two $\tilde L$
evaluations, a third-order 2N [low-storage](/methods/low-storage-runge-kutta.md)
SSP method, and hybrid two-step methods. §5 gives order barriers and optimal
coefficients for SSP [linear multistep methods](/methods/linear-multistep-method.md)
and a table of 15 methods of orders 2–5. §6 proves that implicit Runge–Kutta
and multistep methods of the restricted forms (6.7) and (6.16), with only
implicit terms, cannot be unconditionally SSP beyond first order. Numerical
evidence uses the [Burgers equation](/benchmarks/burgers-equation.md) and
[linear advection](/benchmarks/linear-advection-equation.md) with step data.

# Version read

Version of record (SIAM typeset, printed pp. 89–112, 24 PDF pages), all
read; born-digital text, with the table, tableau and long-formula pages
(pp. 94–102, 105) also read visually. Page 1 matches the Crossref metadata;
the page prints the title in title case. Received 11 February 2000,
published electronically 2 February 2001.

# Key claims

Registry notation: $h$ is the step (source $\Delta t$), $h_{\mathrm{FE}}$ the
forward-Euler bound (source $\Delta t_{FE}$), $\mathcal C$ the SSP coefficient
(source "CFL coefficient" $c$), $s$ the number of stages (source $m$), $k$
the number of steps of a multistep method (source $m$). Stages are written
in the source's 0-based form $y^{(i)}$, $y^{(0)}=y_n$ (source $u^{(i)}$).
Multistep methods use the backward index of the source,
$y_{n+1}=\sum_{r=1}^k\bigl(\bar\alpha_ry_{n+1-r}+h\bar\beta_rL(y_{n+1-r})\bigr)$
(page-local bars; source $\alpha_i$, $\beta_i$). $\eta_{\mathrm c}(t)$ is the coercivity
constant (source $\eta(t)$; page-local, as on the concept pages that cite it).

1. Lemma 2.1 (from Shu–Osher): if forward Euler is strongly stable for
   $h\le h_{\mathrm{FE}}$, the Shu–Osher form (2.9) with $\beta_{ij}\ge0$ is
   strongly stable for $h\le\mathcal Ch_{\mathrm{FE}}$,
   $\mathcal C=\min\alpha_{ij}/\beta_{ij}$ (2.10): its stages are convex
   combinations of forward Euler steps of size $h\beta_{ij}/\alpha_{ij}$
   (§2.2). **Proved** (recalled)
2. Lemma 2.2 (from Shu–Osher): with $\beta_{ij}<0$ the method is SSP with
   $\mathcal C=\min\alpha_{ij}/|\beta_{ij}|$ (2.13) if $\beta_{ij}L$ is
   replaced by $\beta_{ij}\tilde L$, where $\tilde L$ approximates the same
   spatial derivative and makes $y-h\tilde L(y)$ strongly stable (2.11). For
   conservation laws $\tilde L$ comes from $u_t=f(u)_x$, "the only difference
   is the change of upwind direction"; when both $L(y^{(k)})$ and
   $\tilde L(y^{(k)})$ are needed, cost and storage for that $k$ double
   (§2.2). **Proved** (recalled)
3. Lemma 2.3 (from Shu): the multistep form (2.14) with $\bar\alpha_r\ge0$ is
   SSP with $\mathcal C=\min_r\bar\alpha_r/|\bar\beta_r|$ (2.15) (§2.3).
   **Proved** (recalled)
4. The argument uses convexity only, so "any convex function will be
   preserved", including the total variation, maximum norms, weighted $L^2$
   norms and cell entropies; the TVB hypothesis
   $\lVert y+hL(y)\rVert\le(1+O(h))\lVert y\rVert$ is preserved too. If forward
   Euler is not stable, "the framework in this paper cannot be used" (§2.1).
   **Stated**. Footnote 1 defines strong stability as "no temporal growth".
5. On a Burgers Riemann problem with second-order MUSCL, an SSP second-order
   Runge–Kutta method is non-oscillatory, while a linearly stable non-SSP
   second-order method overshoots (§2.1, Fig. 2.1, reproduced from
   Gottlieb–Shu). **Shown**
6. Prop. 3.1: among $s$-stage order-$s$ methods (2.9) with
   $\alpha_{ij},\beta_{ij}\ge0$ the largest coefficient is $\mathcal C=1$; the
   proof works in the linear case. The bound holds only when stages equal
   order: Shu built an $s$-stage first-order method with $\mathcal C=s$ (§3.1).
   **Proved**
7. Prop. 3.2: the family (3.1)–(3.2), $s-1$ forward Euler stages followed by
   a convex combination with $\alpha_{s,k}=\frac1k\alpha_{s-1,k-1}$,
   $\alpha_{s,s-1}=\frac1{s!}$, $\alpha_{s,0}=1-\sum_{k\ge1}\alpha_{s,k}$, is
   order $s$ on linear problems, SSP with $\mathcal C=1$, with all
   $\alpha_{s,k}\ge0$; as the $s$-stage order-$s$ linear Runge–Kutta
   polynomial is unique, "this unique $m$-stage, $m$th-order linear
   Runge–Kutta method is SSP under CFL coefficient $c=1$". For nonlinear $L$
   the method stays SSP with $\mathcal C=1$ but is "no longer $m$th-order
   accurate" (§3.1). **Proved**
8. The Taylor polynomials of degree 3 and 4 are convex combinations of powers
   of $I+hL$, e.g.
   $\sum_{k=0}^4\frac{(hL)^k}{k!}=\frac38I+\frac13(I+hL)+\frac14(I+hL)^2+\frac1{24}(I+hL)^4$
   (3.4)–(3.5) (§3.1). **Derived**
9. Table 3.1 lists $\alpha_{s,j}$ for $s=1,\dots,8$ (§3.1). **Derived**
10. Assumption 3.1 (coercivity),
    $\eta_{\mathrm c}(t)=\inf_{|y|=1}-\mathrm{Re}\langle L(t)y,y\rangle/|L(t)y|^2>0$:
    then $\lVert I+h_nL(t_n)\rVert\le1$ iff $h_n\le2\eta_{\mathrm c}(t_n)$, and
    $\lVert L(t)\rVert\le1/\eta_{\mathrm c}(t)$ (§3.2, Eqs. (3.7)–(3.8)). **Proved**
11. Prop. 3.3: under coercivity and the Lipschitz bound
    $\lVert L(t)-L(t')\rVert\le\frac{K}{\eta_{\mathrm c}(t)}|t-t'|$ (3.14), classical
    RK4 for $y'=L(t)y$ satisfies $|y_n|\le e^{3Kt_n}|y_0|$ under
    $h_n\le2\eta_{\mathrm c}(t_n)$ (§3.2, Eqs. (3.15)–(3.16)). **Proved** (frozen
    coefficients give $\lVert P_4\rVert\le1$ by the convex form; the
    perturbation adds the factor $1+3Kh_n$)
12. This "improve[s] in both simplicity and generality" on Levy–Tadmor, whose
    bound $C_4=1/31$ becomes "our uniform $C_s=2$" (§3.2, Remark after
    Prop. 3.3). **Stated**. The printed proof is for RK4 (Prop. 3.3); §3.2
    announces the general $s$-stage case and then treats "the fourth-order"
    one "to make one point".
13. Prop. 4.1 (see Gottlieb–Shu): with $\beta_{ij}\ge0$, the second-order
    method (4.1) and the third-order method (4.2), the Shu–Osher methods, are
    optimal with $\mathcal C=1$, "optimal (in the sense of CFL coefficient and
    the cost incurred by $\tilde L$ if it appears)" (§4.1). **Stated** (recalled)
14. Prop. 4.2 (see Gottlieb–Shu): every four-stage fourth-order SSP method
    (2.9) with nonzero coefficient (2.13) has at least one $\beta_{ij}<0$
    (§4.1). **Stated** (recalled)
15. The four-stage fourth-order method (4.3), from Gottlieb–Shu, has
    $\mathcal C=0.936$ with two $\tilde L$ evaluations; its "effective CFL
    coefficient, compared with an ideal case without $\tilde L$'s", is
    $0.936\times\frac46=0.624$. Optimality is not claimed (§4.1). **Shown**
    (search)
16. The best third-order SSP method found in 2N low-storage form (4.4) has
    $B^{\mathrm W}_1=0.924574$ and SSP coefficient $0.32$; no five-stage
    fourth-order Carpenter–Kennedy method with positive coefficients was found;
    a low-storage method with negative $\beta_{ij}$ "cannot be made SSP"
    because $\tilde L$ destroys the low-storage property (§4.2). **Shown**
    (search) / **Stated**
17. In the hybrid two-step two-stage family (4.5)–(4.6), third order leaves a
    three-parameter family (4.7); the best member found (stage parameter
    $0.4043$, $\alpha_{30}=0.0605$, $\alpha_{31}=0.6315$) has coefficient
    $\approx0.473$, against 1 for (4.2) (§4.3). **Shown** (search)
18. Prop. 4.3: no fourth-order hybrid method (4.5) has all
    $\alpha_{ij}\ge0$ (§4.3). **Proved**
19. Prop. 5.1: for $k\ge2$ there is no $k$-step order-$k$ SSP multistep method
    with all $\bar\beta_r\ge0$, and no $k$-step SSP method of order $k+1$
    (§5). **Proved** (test polynomials $x(k-x)^{k-1}$ and
    $\int_0^x\prod_{r=1}^k(r-\tau)\,d\tau$ in the order conditions (5.2))
20. This is "consistent with" Dahlquist: no linearly stable $k$-step methods
    of order $k+1$ for odd $k$, while for even $k$ they "would require
    negative $\alpha_i$" (§5, after Table 5.1). **Stated**
21. Prop. 5.2: two-step second-order SSP methods have optimal
    $\mathcal C=\frac12$, at $\bar\alpha_1=\frac45$ (§5). **Proved**
22. Prop. 5.3: three-step second-order methods with $\bar\beta_r\ge0$ have
    optimal $\mathcal C=\frac12$, attained by
    $y_{n+1}=\frac34y_n+\frac14y_{n-2}+\frac32hL(y_n)$, with "the same
    efficiency" as (4.1) at one evaluation per step and more storage (§5).
    **Proved**
23. Prop. 5.4: four-step third-order methods with $\bar\beta_r\ge0$ have optimal
    $\mathcal C=\frac13$, attained by
    $y_{n+1}=\frac{16}{27}y_n+\frac{11}{27}y_{n-3}+\frac{16}9hL(y_n)+\frac49hL(y_{n-3})$
    (§5). **Proved**
24. More steps raise $\mathcal C$: second order with four steps
    $\frac23$; third order with five steps $\frac12$, six steps $0.567$;
    fourth order with four steps $0.154$ (Shu) and $0.159$ (search), six steps
    $0.245$; fifth order with five steps $0.077$ (Shu) and $0.085$ (search),
    six steps $0.130$ (Shu) (§5, Table 5.1). **Shown** (search)
25. Five-step fourth-order methods with all $\bar\alpha_r,\bar\beta_r\ge0$
    exist with $\mathcal C\le\frac3{88}\approx0.034$; search gives $0.021$
    (scheme 12). This "disproves the belief that SSP schemes of order four or
    higher must have negative $\beta$", though the coefficient is "probably
    too small for the scheme to be of much practical use" (§5). **Shown** /
    **Derived** (bound)
26. Lemma 6.1 (Harten): the implicit scheme (6.1) with incremental
    coefficients $C_{j+\frac12},D_{j-\frac12}\ge0$ is TVD for every $h$
    (§6.1). **Proved**
27. The second-order implicit family (6.3) for linear $L$ has
    $\alpha_{2,1}=\frac1{2\beta_1(1-\beta_1)}\in[4,\infty)\cup(-\infty,0)$, so
    $\alpha_{2,0}$ and $\alpha_{2,1}$ cannot both be nonnegative (§6.1,
    Eq. (6.4)). **Derived**
28. On $u_t=u_x$ with step data, first-order upwinding,
    $h/\Delta x=1.4$ and 100 steps, backward Euler is monotone and (6.3)–(6.4)
    with $\beta_1=2$ oscillates (§6.1, Fig. 6.1). **Shown**
29. Prop. 6.2: an implicit Runge–Kutta method of the form (6.7) — one
    implicit evaluation per stage, $y^{(i)}=\sum_{k<i}\alpha_{i,k}y^{(k)}+h\beta_iL(y^{(i)})$,
    no explicit terms — of order $\ge2$ cannot have all $\alpha_{i,k}\ge0$,
    whatever the signs of $\beta_i$ (with $\tilde L$ for negative $\beta_i$);
    the hypothesis is unconditional strong stability of implicit Euler (6.8)
    (§6.2). **Proved**
30. Prop. 6.3: an implicit multistep method (6.16),
    $y_{n+1}=\sum_r\bar\alpha_ry_{n+1-r}+h\beta_0L(y_{n+1})$, of order $\ge2$
    cannot have all $\bar\alpha_r\ge0$, because second order forces
    $\sum_rr^2\bar\alpha_r=0$ (§6.3, Eq. (6.17)). **Proved**
31. If explicit terms are allowed ($L(y^{(0)})$ in (6.7), explicit $L$ in
    (6.16)), "we would be able to obtain SSP Runge–Kutta [multistep] methods
    under restrictions on $\Delta t$ similar to explicit methods" (§6.2,
    §6.3). **Stated**

# Printed slips

- §4.2, $A_2$ of the low-storage method: "$-z_1(6c2-4c+1)+3z_3$" lacks the
  superscript ($6c^2$), and "$z1$" lacks the subscript in several places of
  $A_2$, $B_2$, $B_3$ (p. 102).
- §4.2: "with $c=0.924574$, resulting in a CFL coefficient $c=0.32$" uses one
  letter for two quantities in one sentence; §4.3 does the same with
  $c=0.4043$ and "CFL coefficient $c\approx0.473$".
- (3.4)–(3.5): the constant terms are printed as $\frac13$ and $\frac38$
  without $I$; the proof of Prop. 3.3 writes $\frac38I$.
- Proof of Prop. 3.3: $P_4(\Delta t_nL^n):=\frac38I+\frac13(I+\Delta tL)+\dots$
  mixes $\Delta t_nL^n$ and $\Delta tL$ (p. 99); the text after (3.29) reads
  "$j^3$ does not exceed $|j^3|<\dots$".
- Table 3.1: $\alpha_{7,3}$ printed unreduced as $\frac3{48}$.
- The hybrid stage is named $u^{n+\frac12}$ although it sits at
  $t_n+0.4043h$ in the best method (§4.3).
- "Courant–Friedrichs–Levy" (p. 90), "Cauchy–Schwartz" (p. 98),
  "Crank–Nicholson" (p. 108).
- References: [5] "K. Dekker and and J. G. Verwer"; [9] Kurganov precedes
  [10] Jackiewicz; [10] and [14] print "SIAM J. Numer. Anal" without the final
  period.

# Notation map

| Gottlieb et al. (2001) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u^n$, $u^n_j$ | $y$, $y_n$ (component $j$) | |
| $L(u)$, $L$ | $L$ | semi-discrete operator; a matrix in §3 |
| $\tilde L$ | $\tilde L$ | downwind operator: $u-\Delta t\tilde L(u)$ strongly stable (2.11) |
| $\Delta t$, $\Delta t_n$ | $h$, $h_n$ | |
| $\Delta t_{FE}$ | $h_{\mathrm{FE}}$ | |
| $c$ ("CFL coefficient") | $\mathcal C$ | **also** the low-storage parameter $B_1=c$ (§4.2) and the hybrid stage parameter (§4.3) |
| effective CFL coefficient | — | $c\cdot\frac4{4+i}$, $i$ the number of $\tilde L$ evaluations (§4.1); **not the registry $\mathcal C_{\mathrm{eff}}=\mathcal C/s$** |
| $\alpha_{i,k}$, $\beta_{i,k}$ | $\alpha_{ij}$, $\beta_{ij}$ | Shu–Osher coefficients, 0-based stages |
| $u^{(i)}$ | $y^{(i)}$ (page-local), $y^{(i)}=Y_{i+1}$ | stage values, $u^{(0)}=u^n$ |
| $m$ | $s$ (stages) or $k$ (steps) | |
| $\alpha_i$, $\beta_i$ (multistep) | $\bar\alpha_r$, $\bar\beta_r$ (page-local) | backward index on $y_{n+1-r}$; $\bar\alpha_r=-\alpha_{k-r}$, $\bar\beta_r=\beta_{k-r}$ with registry $\alpha_k=1$ |
| $\beta_0$ | $\beta_k$ | implicit multistep coefficient (6.16) |
| $\beta_i$ (§6.2) | — | single implicit coefficient of stage $i$ of (6.7) |
| $A_i$, $B_i$, $du$ | $A^{\mathrm W}_i$, $B^{\mathrm W}_i$ | 2N low-storage (Williamson) coefficients and register (4.4); **$A$ is the Butcher matrix** |
| $A_{i,k}$ | — | coefficient of $(\Delta tL)^{k+1}$ in stage $i$ (proof of Prop. 3.1); **collides with the Butcher $A$** |
| $\eta(t)$ | $\eta_{\mathrm c}(t)$ (page-local) | coercivity constant (3.7); **$\eta$ is the registry entropy** |
| $K$ | — | Lipschitz constant of (3.14); **$K$ is the registry iteration count** |
| $k^i$, $j^i$ | — | RK4 stage derivatives with true and frozen $L$; **$k$ is the registry step count** |
| $P_4$ | $P(z)$ at $z=hL$ | RK4 stability polynomial in convex form |
| $TV$ | $\mathrm{TV}$ | (2.5) |
| $r$ | $p$ | order of a multistep method (Table 5.1) |
| $C_{j+\frac12}$, $D_{j-\frac12}$ | — | Harten incremental coefficients (6.1) |
| $X_m$, $Y_m$, $c_m$ | — | proof sequences of Prop. 6.2; **$c_m$ is not $\mathcal C$** |

# Reference list

The paper prints 23 references in SIAM numbered style ([1]–[23]),
alphabetical by first author except that [9] Kurganov precedes [10]
Jackiewicz and [12] van Leer is filed under L. All are merged complete into
the [bibliography](/bibliography.md) with `citedby` gottlieb-2001. [9]
(Kurganov & Tadmor, UCLA CAM Report No. 99-16) prints no year. [19] Shu,
"Total-variation-diminishing time discretizations" (SIAM J. Sci. Statist.
Comput. 9) and [20] Shu & Osher (J. Comput. Phys. 77) share the key stem
`shu-1988`; they are mapped by venue to the bundle keys `shu-1988-b` and
[`shu-1988`](/sources/shu-1988.md) respectively. No DOIs are printed.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [Burgers equation](/benchmarks/burgers-equation.md)
* [Energy method for Runge–Kutta stability](/methods/runge-kutta-energy-method.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)](/methods/modified-patankar-methods.md)
* [Negative-coefficient barrier for splitting methods](/results/negative-coefficient-barrier.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Strong stability (monotonicity) of Runge–Kutta methods for linear seminegative problems](/properties/strong-stability.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Total variation diminishing (TVD) time stepping](/definitions/total-variation-diminishing.md)
* [Zero-stability](/definitions/zero-stability.md)
