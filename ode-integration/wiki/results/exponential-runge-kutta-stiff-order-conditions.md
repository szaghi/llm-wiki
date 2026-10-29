---
type: Result
title: "Stiff order conditions of exponential Runge–Kutta methods and φ-order conditions"
description: "Stiff order conditions make an exponential Runge–Kutta or Rosenbrock method converge with error constants independent of the stiff operator; the page states the conditions to order 5 (Runge–Kutta) and 6 (Rosenbrock), Luan's one-weakened-condition convergence theorem, and the intermediate φ-order conditions of Dallerit and Tokman with their closed-form solution."
status: established
aliases: [stiff order, stiff order conditions, Hochbruck–Ostermann order conditions, φ-order conditions, phi-order conditions, ϕ-order, stiffness resilience, stiffly accurate exponential integrator]
tags: [exponential, order-conditions, stiff, order-reduction]
timestamp: 2026-10-29T18:13:00Z
---

# Stiff order conditions of exponential Runge–Kutta methods and φ-order conditions

An [exponential integrator](/methods/exponential-integrators.md) has coefficients that are
functions of a stiff matrix, so its order can be defined in two ways. Its **classical
order** comes from expanding every coefficient in a Taylor series in $hL$, and the
resulting error terms carry powers of $L$. Its **stiff order** is the order of a global
error bound whose constant does not depend on $\lVert L\rVert$. The bound holds when $L$
generates an analytic semigroup and the method satisfies the **stiff order conditions**
of Hochbruck and Ostermann, which are identities between matrix functions that must hold
for arbitrary matrices. [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) define
the notion: a method has stiff order $p$ for a class of problems if its global error on
finite intervals is bounded by $Ch^p$ with $C$ depending on the interval and the problem
class "but neither on the stiffness nor on the step size $h$", and "the classical order is
always an upper bound to the stiff order" (§1, p. 212). Their survey states the conditions to
order 4 (Table 2.2) and the Rosenbrock conditions to order 4 (Table 2.3). [Luan (2021)](/sources/luan-2021.md) lists these conditions to
order 5 and proves that one of them can be weakened. [Luan et al. (2022)](/sources/luan-2022.md)
list the much shorter exponential Rosenbrock set to order 6.
[Dallerit & Tokman (2025)](/sources/dallerit-2025.md) propose a third, intermediate
notion, the **φ-order**, whose conditions they solve in closed form at every order.
Luan and Dallerit & Tokman, after Hochbruck–Ostermann, call methods that satisfy the
stiff conditions "stiffly accurate"; the 2010 survey of Hochbruck & Ostermann itself uses
"stiff order" and not that phrase. That use is unrelated to
[stiff accuracy](/properties/stiff-accuracy.md) of a Runge–Kutta tableau ($a_{sj}=b_j$),
and on this page "stiff" always means the matrix-function conditions.

## Setting and method format

The problem is semilinear, $y'=f(t,y)=Ly+N(t,y)$: $L$ is the stiff linear part and $N$ the
non-stiff remainder (page-local, as on [exponential integrators](/methods/exponential-integrators.md)).
Luan (2021, Eqs. 1.2–1.3) writes an $s$-stage explicit exponential Runge–Kutta (ExpRK)
method in the reformulated form

$$\begin{aligned}
Y_i&=y_n+c_ih\,\phi_1(c_ihL)f(t_n,y_n)+h\sum_{j=2}^{i-1}a_{ij}(hL)D_j,\qquad i=2,\dots,s,\\
y_{n+1}&=y_n+h\,\phi_1(hL)f(t_n,y_n)+h\sum_{i=2}^{s}b_i(hL)D_i,\qquad D_i=N(t_n+c_ih,Y_i)-N(t_n,y_n),
\end{aligned}$$

with $Y_1=y_n$, $c_1=0$, and $D_i$ page-local. The coefficients $a_{ij}(z)$ and $b_i(z)$
are linear combinations of the [φ-functions](/methods/exponential-integrators.md)
$\phi_k(c_iz)$ and $\phi_k(z)$, in the registry normalisation $\phi_k(0)=1/k!$, which Luan
also uses (Eq. 1.4). Exponential Euler is the case $s=1$. All sums below run over
$i=2,\dots,s$.

The defect functions (Luan 2021, Eq. 3.3; page-local) are

$$\psi_j(hL)=\sum_{i=2}^sb_i(hL)\frac{c_i^{j-1}}{(j-1)!}-\phi_j(hL),\qquad
\psi_{j,i}(hL)=\sum_{k=2}^{i-1}a_{ik}(hL)\frac{c_k^{j-1}}{(j-1)!}-c_i^j\phi_j(c_ihL).$$

The local error of one step started from $y(t_n)$ is
$\sum_{j=2}^5h^j\psi_j(hL)\,\tilde N^{(j-1)}(t_n)$ plus terms in which derivatives of $N$
with respect to $y$ act on the $\psi_{j,i}$, plus $\mathcal O(h^6)$; here
$\tilde N(t)=N(t,y(t))$ is page-local (Luan 2021, Eqs. 3.1–3.2, as recalled from
Hochbruck–Ostermann and Luan–Ostermann).

**Relation to stage order** *(compiler check, not in the sources)*. At $L=0$, with
$\phi_j(0)=1/j!$ and $c_1=0$, $\psi_{j,i}(0)=\tau^{(j)}_i/(j-1)!$, where $\tau^{(j)}$ is the
[stage-order](/definitions/stage-order.md) residual of the underlying Runge–Kutta tableau.
The stage conditions $\psi_{j,i}=0$ are therefore matrix-function versions of stage-order
conditions, imposed stage by stage.

## The stiff order conditions to order 5

Luan (2021, Table 3.1, recalled from Luan–Ostermann) gives the conditions below. $Z$,
$X_1$, $X_2$, $X_3$ are arbitrary square matrices and $\mathcal B$ an arbitrary bilinear
map (page-local; the source writes $J,K,L,B$); $a_{ij}$, $b_i$, $\psi$ are evaluated at $Z$.

| No. | condition | order | H–O 2010 no. |
|---|---|---|---|
| 1 | $\psi_2(Z)=0$, i.e. $\sum_ib_i(Z)c_i=\phi_2(Z)$ | 2 | 2 |
| 2 | $\psi_3(Z)=0$, i.e. $\sum_ib_i(Z)c_i^2/2!=\phi_3(Z)$ | 3 | 4 |
| 3 | $\sum_ib_iX_1\psi_{2,i}=0$ | 3 | 5 |
| 4 | $\psi_4(Z)=0$, i.e. $\sum_ib_i(Z)c_i^3/3!=\phi_4(Z)$ | 4 | 6 |
| 5 | $\sum_ib_iX_1\psi_{3,i}=0$ | 4 | 7 |
| 6 | $\sum_ib_iX_1\sum_ja_{ij}X_1\psi_{2,j}=0$ | 4 | 8 |
| 7 | $\sum_ib_ic_iX_2\psi_{2,i}=0$ | 4 | 9 |
| 8 | $\psi_5(Z)=0$, i.e. $\sum_ib_i(Z)c_i^4/4!=\phi_5(Z)$ | 5 | — |
| 9 | $\sum_ib_iX_1\psi_{4,i}=0$ | 5 | — |
| 10 | $\sum_ib_iX_1\sum_ja_{ij}X_1\psi_{3,j}=0$ | 5 | — |
| 11 | $\sum_ib_iX_1\sum_ja_{ij}X_1\sum_ka_{jk}X_1\psi_{2,k}=0$ | 5 | — |
| 12 | $\sum_ib_iX_1\sum_ja_{ij}c_jX_2\psi_{2,j}=0$ | 5 | — |
| 13 | $\sum_ib_ic_iX_2\psi_{3,i}=0$ | 5 | — |
| 14 | $\sum_ib_ic_iX_2\sum_ja_{ij}X_1\psi_{2,j}=0$ | 5 | — |
| 15 | $\sum_ib_i\,\mathcal B(\psi_{2,i},\psi_{2,i})=0$ | 5 | — |
| 16 | $\sum_ib_ic_i^2X_3\psi_{2,i}=0$ | 5 | — |

Cumulatively there are 1, 3, 7 and 16 conditions for orders 2, 3, 4 and 5. A condition holds
in **strong form** if it holds for arbitrary $Z$, and in **weakened form** if it holds
only with $b_i(Z)$ replaced by $b_i(0)$ (Luan 2021, §3.1). No condition appears for order 1
in Luan's difference format.

**The original table** (Hochbruck & Ostermann 2010, §2.3, Table 2.2). Hochbruck & Ostermann
list nine conditions up to order 4 for the value format of
[exponential integrators](/methods/exponential-integrators.md), with $J$, $K$ arbitrary
bounded operators (the $X_1$, $X_2$ above). The last column gives their numbering. Their two
further conditions are $\psi_1=0$ (no. 1, order 1) and the stage conditions $\psi_{1,i}=0$
(no. 3, order 2); these are the simplifying assumptions
$\sum_jb_j(Z)=\phi_1(Z)$, $\sum_ja_{ij}(Z)=c_i\phi_1(c_iZ)$ (their Eq. (2.23)), which Luan's
difference format satisfies by construction. Cumulatively their table has 1, 3, 5 and 9
conditions for orders 1–4 *(compiler check, not in the sources: $1$; $1+2$; $3+2$; $5+4$ from
the order column of their Table 2.2)*. They define the defects
with the opposite sign, $\phi_j(Z)-\sum_ib_ic_i^{j-1}/(j-1)!$ and
$\phi_j(c_iZ)c_i^j-\sum_{k=1}^{i-1}a_{ik}c_k^{j-1}/(j-1)!$ (Eqs. (2.17), (2.37)), with the
stage sum from $k=1$ because they work with values rather than differences; their condition 8
has the inner sum from $j=2$. The sign is immaterial for conditions of the form "$=0$"
*(compiler check, not in the sources)*. They state
that explicit methods cannot achieve $\psi_{2,i}=0$ for all $i$, so "the internal stages are of
order one only" (p. 226). The stiff
conditions are indexed by trees in the exponential B-series of Luan–Ostermann, which
Luan (2021) cites as the systematic route to any order; see [B-series](/definitions/b-series.md).

## Convergence with one weakened condition

**Hypotheses** (Luan 2021, §3, after Hochbruck–Ostermann). (1) $L$ generates an analytic
semigroup on a Banach space, so $\lVert e^{tL}\rVert\le C$ and the coefficients
$\phi_k(hL)$, $a_{ij}(hL)$ and $b_i(hL)$ are bounded. Parabolic smoothing then gives
$\big\lVert hL\sum_{j=1}^ne^{jhL}\big\rVert\le C$ uniformly for $0<nh\le T-t_0$ (Eq. 3.5).
(2) The solution is smooth, and $N$ is Fréchet-differentiable often enough in a strip
around it, with uniformly bounded derivatives.

**Earlier framework.** The fourth-order expRK4s5 of Hochbruck–Ostermann and the
fifth-order expRK5s8 of Luan–Ostermann were built from a convergence result that allows
many conditions in weakened form. At order 4 these are conditions 4–7, and at order 5,
nine of the sixteen (Luan 2021, §2, Remark 2.2, §4.2).

**Theorem** (Hochbruck & Ostermann 2010, Thm. 2.17, quoted from their 2005 work, proof not
reproduced). Let $L$ generate an analytic semigroup, let the solution and $N$ be smooth
(Assumptions 2.9 and 2.16, with $N$ Lipschitz on the whole space), and let the explicit method
satisfy the simplifying assumptions (2.23). For $2\le p\le4$, if the conditions of their
Table 2.2 hold up to order $p-1$, $\psi_p(0)=0$, and the remaining order-$p$ conditions hold
"in a weaker form with $b_i(0)$ instead of $b_i(-hA)$", then
$\lVert y_n-y(t_n)\rVert\le Ch^p$ uniformly on $0\le nh\le T$. This is the earlier framework
Luan describes: at order 4, Luan's conditions 4–7 (theirs 6–9) in weakened form. For
exponential general linear methods they state the analogous Theorem 2.31, after Ostermann,
Thalhammer & Wright (2006), in which only the order-$p$ quadrature condition is weakened, to
its value at $z=0$ (Eq. (2.78)); see
[exponential integrators](/methods/exponential-integrators.md).

**Theorem** (Luan 2021, Thm. 3.1). Let $2\le p\le5$. Suppose an explicit ExpRK method
satisfies the conditions of the table up to order $p$ in strong form, except the single
condition $\psi_p(Z)=0$, which holds only as $\psi_p(0)=0$. Then
$\lVert y_n-y(t_n)\rVert\le Ch^p$ uniformly on $t_0\le t_n\le T$, with $C$ independent of
$n$ and $h$.

*Mechanism* (proof, Eq. 3.8). The remaining leading defect is
$h^p(\psi_p(hL)-\psi_p(0))\tilde N^{(p-1)}(t_n)$. Write
$\psi_p(hL)-\psi_p(0)=\tilde\psi_p(hL)\,hL$ with $\tilde\psi_p$ bounded (page-local).
Parabolic smoothing absorbs the factor $hL$ when the local errors accumulate, and a discrete
Gronwall lemma closes the argument. Luan calls the result "stronger" than those of
Hochbruck–Ostermann and Luan–Ostermann. It asks more conditions to hold strongly, and in
return it admits stage structures in which groups of stages are independent and share one
φ-combination format, so that a step needs fewer sequential evaluations (§3.2, §4).

**Stage-count findings** (Luan 2021, §4). These are derived along the author's construction
path and are not proved as general lower bounds:

- order 4 cannot be reached with $s=5$ under the theorem's hypotheses; Luan recalls that
  Hochbruck–Ostermann showed that $s=5$ is minimal for their weakened set. Hochbruck &
  Ostermann (2010, §2.3, p. 229) state that the question "whether it is possible to modify
  the coefficients of the above four-stage methods" (ETD4RK, Krogstad's and
  Strehmel–Weiner's) "in such a way that they have order four for semilinear parabolic
  problems was answered in the negative" in their 2005 work, which constructed the
  five-stage method;
- the six-stage family expRK4s6 reaches order 4 with 4 sequential evaluations per step,
  against 6 for expRK4s5;
- order 5 needs $s\ge9$. With $s=9$, condition 11 cannot hold in strong form, because the
  requirements it places on $a_{j2}$, $a_{j3}$ conflict with $\psi_{2,j}=\psi_{3,j}=0$
  (Eq. 4.29);
- the ten-stage family expRK5s10 weakens only condition 8 and needs 5 sequential
  evaluations, against 11 for expRK5s8;
- an eleven-stage scheme meeting all 16 conditions in strong form can be built the same way,
  at the same cost of 5 evaluations, but is not given (Remark 4.2).

The families and their coefficients are on [exponential integrators](/methods/exponential-integrators.md).
Dallerit & Tokman (2025, §1, §3) recall that exponential Runge–Kutta methods satisfying the
stiff conditions are known only up to order 5. That is consistent with Luan (2021).

## A classical-order scheme measured against the stiff conditions: Cox–Matthews ETD4RK

The ETD Runge–Kutta schemes of Cox and Matthews were derived from classical, Taylor-expanded
conditions. [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md) use ETD2RK, ETD3RK and
ETD4RK with classical error terms only ($\propto h^5\,d^4N/dt^4$ for ETD4RK, §2) and make no
stiff-order claim; their tests (fourth- and sixth-order parabolic-type problems and a
Fokker–Planck chain) report error rates without convergence slopes. Written in Luan's
difference format, ETD4RK (tableau on
[exponential integrators](/methods/exponential-integrators.md)) has $c=(0,\tfrac12,\tfrac12,1)$,
$a_{32}=\tfrac12\phi_1(\tfrac12Z)$, $a_{42}=0$, $a_{43}=\phi_1(\tfrac12Z)$,
$b_2=b_3=2\phi_2-4\phi_3$, $b_4=4\phi_3-\phi_2$, and the table above gives *(compiler check,
not in the sources)*:

- conditions 1 and 2 hold in strong form ($\sum_ib_ic_i=\phi_2$,
  $\sum_ib_ic_i^2/2=\phi_3$);
- condition 4 holds only in weakened form: $\sum_ib_ic_i^3/3!=\tfrac12\phi_3-\tfrac1{12}\phi_2$,
  which equals $\phi_4$ at $Z=0$ but differs from it at first order in $Z$;
- condition 3 holds in neither form: with $b_i(0)$,
  $\sum_ib_i(0)\psi_{2,i}(Z)=\tfrac16\big(\phi_1(\tfrac12Z)-\phi_2(\tfrac12Z)-\phi_2(Z)\big)$,
  which vanishes at $Z=0$ and to first order but has the $Z^2$ coefficient $-\tfrac1{576}$;
  with $b_i(Z)$ (strong form, scalar case) the $Z^2$ coefficient is $+\tfrac1{576}$.

Luan's theorem therefore guarantees stiff order 2 for ETD4RK and no more. Whether its order
drops on a given stiff problem is not tested by any ingested source.

**Hochbruck & Ostermann's analysis of the four-stage schemes** (2010, Ex. 2.19, p. 228; their
numbering of Table 2.2, no numerical tests). For ETD4RK (their Eq. (2.41)) they state:

- conditions 1–4 hold, and condition 6 in "the weakened but sufficient" form $\psi_4(0)=0$;
- conditions 5, 7, 8 and 9 do not hold; conditions 5 and 9 hold in "a weakened form"
  because the stage defects satisfy $\psi_{2,2}(0)+\psi_{2,3}(0)=0$ and $\psi_{2,4}(0)=0$, and
  conditions 7 and 8 only in "a very weak form (where all arguments are evaluated for
  $A=0$)";
- "In the worst case, this leads to an order reduction to order two only."

Their worst-case order agrees with the compiler check above. Their "weakened form" of
condition 5 rests on stage defects at $A=0$, whereas the check above replaces $b_i(Z)$ by
$b_i(0)$ and keeps $\psi_{2,i}(Z)$; the two statements concern different reductions of the
same condition. For **Krogstad's scheme** (2.42) conditions 1–5 and 9 hold, condition 6 in
the weakened form $\psi_4(0)=0$, and conditions 7 and 8 only in the very weak form: "In the
worst case, this leads to an order reduction to order three." The **Strehmel–Weiner scheme**
(2.43) "satisfies the conditions of Table 2.2 in exactly the same way as Krogstad's method",
so it converges "with order three in the worst case"; Strehmel & Weiner (1992) proved it
B-consistent of order two (as recalled; see [B-convergence](/definitions/b-convergence.md)).
The **five-stage method** (expRK4s5, p. 229) has order four under Thm. 2.17. The tableaux are
on [exponential integrators](/methods/exponential-integrators.md); see also
[order reduction](/definitions/order-reduction.md).

## Exponential Rosenbrock methods: a shorter set

An exponential Rosenbrock method linearizes at every step,
$f(t,y)=J_ny+V_nt+N_n(t,y)$, with $V_n=\partial_tf(t_n,y_n)$ and the remainder $N_n$
(page-local). The method is the ExpRK format above with $L$ replaced by $J_n$, $N$ by $N_n$,
and an added $c_i^2h^2\phi_2(c_ihJ_n)V_n$ term ([Luan et al. 2022](/sources/luan-2022.md),
Eqs. 2.1–2.6). Because $\partial_yN_n$ and $\partial_tN_n$ vanish at $(t_n,y_n)$, every
$D_i=\mathcal O(h^2)$, and every such method has order at least 2 (Eq. 2.7, Remark 2.1). The
stiff conditions to order 6 (Table 1, recalled from Luan–Ostermann 2013) are listed below,
with $Z$, $X_1$, $X_2$ arbitrary matrices (page-local; the source writes $Z,K,M$):

| No. | condition | order |
|---|---|---|
| 1 | $\sum_ib_i(Z)c_i^2=2\phi_3(Z)$ | 3 |
| 2 | $\sum_ib_i(Z)c_i^3=6\phi_4(Z)$ | 4 |
| 3 | $\sum_ib_i(Z)c_i^4=24\phi_5(Z)$ | 5 |
| 4 | $\sum_ib_i(Z)c_iX_1\big(\sum_ka_{ik}(Z)\tfrac{c_k^2}{2!}-c_i^3\phi_3(c_iZ)\big)=0$ | 5 |
| 5 | $\sum_ib_i(Z)c_i^5=120\phi_6(Z)$ | 6 |
| 6 | $\sum_ib_i(Z)c_i^2X_2\big(\sum_ka_{ik}(Z)\tfrac{c_k^2}{2!}-c_i^3\phi_3(c_iZ)\big)=0$ | 6 |
| 7 | $\sum_ib_i(Z)c_iX_1\big(\sum_ka_{ik}(Z)\tfrac{c_k^3}{3!}-c_i^4\phi_4(c_iZ)\big)=0$ | 6 |

Seven conditions give order 6, "much less than the 36 conditions needed for explicit
Runge–Kutta or exponential Runge–Kutta methods of the same order" (Remark 2.1). The
brackets in conditions 4, 6 and 7 are exactly the stage defects $\psi_{3,i}$, $\psi_{3,i}$
and $\psi_{4,i}$ above, at $Z$ *(compiler check, not in the sources)*.

**The original table** (Hochbruck & Ostermann 2010, §2.4, Table 2.3). To order 4 they list
four conditions: $\sum_ib_i(Z)=\phi_1(Z)$ (order 1), $\sum_{j<i}a_{ij}(Z)=c_i\phi_1(c_iZ)$ for
$2\le i\le s$ (order 2), $\sum_{i\ge2}b_i(Z)c_i^2=2\phi_3(Z)$ (order 3) and
$\sum_{i\ge2}b_i(Z)c_i^3=6\phi_4(Z)$ (order 4). The first two are the simplifying assumptions
of the value format; the last two are conditions 1 and 2 above. Hence the weights of every
third-order method involve $\phi_3$ and of every fourth-order method $\phi_3$ and $\phi_4$,
and methods that use $\phi_1$ only, such as exp4, "cannot have order larger than two"
(p. 235, Ex. 2.25). **Theorem 2.22**: if $L$ (their $-A$) generates only a strongly
continuous semigroup (Assumption 2.2, no analyticity), the solution and $N$ are smooth with
$N$ Lipschitz on the whole space, the Jacobian is Lipschitz (Eq. (2.56)), and the step sizes
satisfy $\sum_{k=1}^{n-1}\sum_{j=0}^{k-1}h_j^{p+1}\le C_H$ with $C_H$ small (Eq. (2.57);
page-local $C_H$), then a method satisfying Table 2.3 up to order $p$, $2\le p\le4$, has
$\lVert y_n-y(t_n)\rVert\le C\sum_{j=0}^{n-1}h_j^{p+1}$ (Eq. (2.58)). The proof is given for the
exponential Rosenbrock–Euler method, which is therefore second-order convergent; the general
case is referred to Hochbruck, Ostermann & Schweitzer (2009). The convergence theorem of
Luan et al. (2022, §2.3) likewise assumes that the Jacobian generates a strongly continuous
semigroup with $\lVert e^{tJ}\rVert\le Ce^{\omega t}$ (page-local $\omega$), together with a
uniform stability bound for products of $e^{hJ_n}$ (Eq. 2.20).

## φ-order conditions

Dallerit & Tokman (2025) take the autonomous problem $y'=f(y)$, the full Jacobian
$J_n=f'(y_n)$, recomputed every step, and the remainder
$r_n(y)=f(y)-f(y_n)-J_n(y-y_n)$ (page-local). They expand in [B-series](/definitions/b-series.md)
with the registry normalisation $h^{\lvert\tau\rvert}/\sigma(\tau)$. Trees are split into
$T_S$, those with exactly one branch at the root, and $T_M=T\setminus T_S$, which holds
$\bullet$ and the trees with at least two root branches (page-local). Every tree of $T_S$
is uniquely $[\tau]_k$, the $k$-fold rooting of a tree $\tau\in T_M$, and
$F([\tau]_k)(y_n)=J_n^kF(\tau)(y_n)$ (Lemma 1).

**Theorem** (φ-series of the exact solution; Dallerit & Tokman 2025, Thm. 5, Eqs. 11–12):

$$y(t_n+h)=y_n+h\phi_1(hJ_n)f(y_n)+\sum_{k=3}^{\infty}\phi_k(hJ_n)\,G_k,\qquad
G_k=B(g_k,y_n),\quad g_k(\tau)=\begin{cases}k!/\gamma(\tau)&\tau\in T_M,\ \lvert\tau\rvert=k,\\0&\text{otherwise},\end{cases}$$

with $G_k=\mathcal O(h^k)$ and no $k=2$ term (page-local $G_k$, $g_k$). The proof inserts
the B-series of the remainder into the variation-of-constants formula. That series vanishes on
$\varnothing$, on $\bullet$ and on $T_S$, and equals $\prod_iz(\tau_i)$ on
$\tau=[\tau_1,\dots,\tau_m]\in T_M\setminus\{\bullet\}$ (Thm. 4, Eq. 10; $z$ the coefficient
map of the point of evaluation, page-local).

**Definition** (φ-order; Def. 4). A method
$y_{n+1}=y_n+h\phi_1(hJ_n)f(y_n)+\sum_{k\ge3}\phi_k(hJ_n)v_k$, with $v_k=B(\hat g_k,y_n)$,
has **φ-order $p$** if $\hat g_k(\tau)=g_k(\tau)$ for all $k\ge3$ and all
$\lvert\tau\rvert\le p$. Then $v_k=0$ may be taken for $k>p$ (page-local $v_k$, $\hat g_k$).

**Ansatz and closed-form solution** (§3, Thm. 6, Eq. 19). Take
$v_k=\sum_{j=1}^{p-2}\kappa_{k,j}\,h\,r_n(Y_j)$, $3\le k\le p$, with stage values $Y_j$ at
distinct nonzero nodes $c_j$ (page-local $\kappa_{k,j}$). At least $p-2$ remainder
evaluations are needed, because the $v_k$ must be linearly independent. With exactly $p-2$
of them the method has φ-order $p$ if and only if
(i) each $Y_j$ is a classical order-$(p-2)$ approximation of $y(t_n+c_jh)$, and
(ii)

$$\kappa_{k,j}=(-1)^{p-k}(k-1)!\,\frac{E_{p-k}\big(\{c_1,\dots,c_{p-2}\}\setminus\{c_j\}\big)}{c_j^2\prod_{l\ne j}(c_j-c_l)},$$

with $E_m$ the $m$-th elementary symmetric polynomial (page-local). For $p=4$:
$\kappa_{3,1}=\frac{2c_2}{c_1^2(c_2-c_1)}$, $\kappa_{3,2}=\frac{2c_1}{c_2^2(c_1-c_2)}$,
$\kappa_{4,1}=\frac{6}{c_1^2(c_1-c_2)}$, $\kappa_{4,2}=\frac{6}{c_2^2(c_2-c_1)}$ (p. 12, p. 23).
Under the ansatz, φ-order 4 reduces to six tree conditions: $\hat g_3=2,0,0$ and
$\hat g_4=0,6,3$ on the trees $[\bullet,\bullet]$, $[\bullet,\bullet,\bullet]$ and
$[[\bullet],\bullet]$ (p. 11). The proof first solves the bushy trees, which give a
Vandermonde system with a unique solution iff the nodes are distinct and nonzero. The trees
$[\tau,\bullet]$ then force classical order $p-2$ of the stages, and every remaining tree
reduces to the bushy system.

**Theorem** (stiffness resilience; Thm. 7). For a method of this form, φ-order $p$ holds iff
the method matches the exact B-series on all trees with $\lvert\tau\rvert\le p$ **and** on
all trees $[\tau]_k$ with $\lvert\tau\rvert\le p$ and any $k\ge1$. The local error therefore
contains no term $J_n^kF(\tau)$ with $\lvert\tau\rvert\le p$, whatever $k$. Since stiffness
amplifies exactly these terms, the authors call the property **stiffness resilience** and
say it "can alleviate" loss of accuracy on stiff problems (§5.1).

**Further consequences.**

- *Interpolation* (Thm. 8). A φ-order-$p$ method is the variation-of-constants formula with
  the remainder $h\,r_n(y(t_n+\theta h))$ replaced by the unique polynomial $P$ of degree
  $p-1$ with $P(0)=P'(0)=0$ and $P(c_j)=h\,r_n(Y_j)$ (page-local $P$).
- *Embedding* (Thm. 9). Truncating the sum at $q<p$ gives φ-order $q$. An adaptive step
  then needs two Krylov (KIOPS) calls, one for the truncated solution and one for the
  remaining terms, which are the error estimate (§5.4).
- *Dense output* (Thm. 10). The formula keeps φ-order $p$ at every point of the step; see
  [dense output](/methods/dense-output.md).

The methods built on these conditions (exponential Runge–Kutta, multistep and multivalue)
are on [exponential integrators](/methods/exponential-integrators.md).

## Three notions of order compared

| notion | defined by | what it guarantees | sources |
|---|---|---|---|
| classical order $p$ | Taylor or B-series matching with all $\phi_k$ expanded | local error $\mathcal O(h^{p+1})$ with constants depending on $J$ or $L$; order reduction possible for unbounded operators | Dallerit & Tokman 2025, §2–3; Luan 2021, §1 |
| φ-order $p$ | Def. 4: match $G_k$ on trees up to order $p$ | classical order $p$, plus no $J_n^kF(\tau)$ terms with $\lvert\tau\rvert\le p$ (Thm. 7); no stiffness-uniform bound proved | Dallerit & Tokman 2025 |
| stiff order $p$ | conditions holding for arbitrary matrices | error bound $Ch^p$ uniform in the stiffness under analytic-semigroup hypotheses ($C_0$-semigroup for Rosenbrock) | Hochbruck & Ostermann 2010, §1, Thms. 2.17, 2.22; Luan 2021, Thm. 3.1; Luan et al. 2022, Thm. 2.12 |

Dallerit & Tokman call φ-order conditions stronger than the classical ones and weaker, or
easier to solve, than the stiff ones (§3, p. 8). Thm. 7 proves the first half. The second
half is a statement about solvability, not a proved implication, and the authors ask openly
whether the stiff conditions are "too strict" (§1). In practice: Dallerit & Tokman observe no
[order reduction](/definitions/order-reduction.md) for their methods of φ-order 3–6 on two
Hochbruck–Ostermann parabolic problems and on a 2D advection–diffusion–reaction problem.
Under the same tests, the fifth-order exponential Rosenbrock method EXPRB_5s4 of
Luan–Ostermann, which satisfies the stiff conditions, shows "a slight order reduction" on the
advection–diffusion problem (§7, Figs. 1–4).

## Qualifications

- Luan (2021, Remark 2.2) says that "4 out of 9" conditions are relaxed at order 4, but his
  Table 3.1 has 7 conditions up to order 4, and §4.1 speaks of weakening conditions 4–7. The
  "9" is a printed slip. His Eq. (3.8) writes the leading defect with the Fréchet derivative
  $G_{p-1,n}$ where (3.1) has the time derivative of $N$ along the solution (slip).
- The count "36 conditions" for explicit Runge–Kutta methods of order 6 (Luan et al. 2022,
  Remark 2.1) is as printed; the rooted trees with at most 6 vertices number 37
  *(compiler count)*.
- Luan's theorem needs an analytic semigroup and parabolic smoothing. His second test, a
  cubic nonlinear Schrödinger equation with Fourier discretization, has a skew-Hermitian $L$
  that generates a unitary group, not an analytic semigroup. The observed orders there
  (Luan 2021, §6, Ex. 6.2) are numerical evidence outside the theorem *(compiler remark)*.
- The exponential Rosenbrock convergence proof of Luan et al. (2022, Thm. 2.12) also uses a
  bound on $\lVert J_n\rVert$ when it bounds the inner-solver errors (proof, Eq. 2.57), so
  that part of the bound is not uniform in the stiffness *(compiler remark, not stated by the
  authors)*; see
  [multirate exponential methods](/methods/multirate-exponential-methods.md)).
- Dallerit & Tokman do not discuss the order reduction of EXPRB_5s4. Their advection–diffusion
  test has Neumann boundary conditions and a strong advection term, and these may violate the
  semigroup and regularity hypotheses of the stiff theory *(compiler remark)*. The observation
  therefore does not contradict that theory.
- Permyakova & Goldobin (2025) call ETD4RK fourth order on the strength of its classical error
  term; by the check above the stiff theory recorded here covers only order 2. They claim no
  stiff order.
- Printed slips in Dallerit & Tokman (2025): the product in Eq. (19) runs over $l\ne i$ for
  $l\ne j$. The worked $p=4$ example prints the stage coefficient (their $w_j$) of
$[[\bullet],\bullet]$ as $c_j/2$ for $c_j^3/2$;
  only the latter satisfies their Eq. (22). Thm. 7 is stated "for all $k>1$", but the proof
  and the consequence for $J_nF(\tau)$ need $k\ge1$. Thm. 9 says "order $q$" for φ-order $q$.

# Citations

- [Luan (2021)](/sources/luan-2021.md) — §1–2 (format, classical vs stiff, Remarks 2.1–2.2), §3.1 Table 3.1, Eqs. 3.1–3.3 (defects, conditions to order 5), §3.2 Thm. 3.1, Eqs. 3.4–3.8 (convergence), §4.1–4.2 (stage-count findings, Eq. 4.29, Remark 4.2), §6 (tests); arXiv v1.
- [Luan et al. (2022)](/sources/luan-2022.md) — §2.1 Eqs. 2.1–2.7, Remark 2.1, Table 1 (exponential Rosenbrock conditions to order 6), §2.3 (semigroup assumptions, Thm. 2.12); arXiv v2.
- [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md) — §2 Eqs. 2–4, 10–12 (Cox–Matthews ETD schemes, classical error terms), §3 (tests without convergence slopes); arXiv v2.
- [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) — §1, p. 212 (definition of stiff order); §2.3 Table 2.2, Eqs. (2.17), (2.23), (2.36)–(2.37), Thm. 2.17, Ex. 2.19, p. 229 (original conditions, convergence, four- and five-stage schemes); §2.4 Table 2.3, Thm. 2.22, Eqs. (2.56)–(2.58), Ex. 2.25 (exponential Rosenbrock conditions and convergence); §2.7 Thm. 2.31, Eq. (2.78); version of record.
- [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) — §1–3 (classical vs stiff, Lemma 1, Thms. 4–5, Def. 4, Eqs. 10–17), Thm. 6 Eq. 19 and pp. 11–17, Thm. 7 (§5.1), Thms. 8–10, §7 Figs. 1–4.
