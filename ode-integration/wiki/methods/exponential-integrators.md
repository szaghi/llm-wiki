---
type: Method
title: "Exponential integrators and φ-functions"
description: "Exponential integrators treat a stiff linear part exactly through its exponential and the φ-functions; the page records the φ-function conventions, exponential quadrature, Runge–Kutta, Rosenbrock, Adams, general linear, EPIRK and stiffness-resilient families, partial and nondiagonal linear operators, repartitioning, Parareal, multirate infinitesimal structure, kinetic relaxation, structural dynamics, Magnus and trigonometric (Gautschi-type) integrators."
status: established
aliases: [phi-functions, exponential Runge–Kutta, ExpRK, exponential time differencing, ETD, ETD2RK, ETD3RK, ETD4RK, ETDRK4, Cox–Matthews scheme, Krogstad scheme, Strehmel–Weiner scheme, repartitioned exponential integrator, exponential Rosenbrock, ExpRB, EXPRB, exprb32, exprb43, exp4, EPIRK, exponential Euler, exponential Rosenbrock–Euler, exponential quadrature rule, exponential Adams method, exponential multistep method, exponential general linear method, stiffness resilient exponential integrators, SREXP, integrating factor method, Magnus integrator, commutator-free quasi-Magnus, CFQM, exponential midpoint rule, precise integration method, trigonometric integrator, Gautschi-type method, Deuflhard method, impulse method, mollified impulse method]
tags: [exponential, stiff, kinetic, asymptotic-preserving, multirate, order-conditions]
timestamp: 2026-10-29T18:13:00Z
---

# Exponential integrators and φ-functions

An exponential integrator advances a problem with a stiff linear part, typically the
semilinear form $y'=Ly+N(t,y)$ (page-local $N$: the non-stiff remainder), by evaluating
the exponential $e^{hL}$ and related functions of $hL$ exactly, so that the stiffness of $L$
imposes no step-size restriction. The functions involved are the **φ-functions**

$$\phi_0(z)=e^z,\qquad \phi_k(z)=\int_0^1e^{(1-\theta)z}\frac{\theta^{k-1}}{(k-1)!}\,d\theta\quad(k\ge1),$$

which satisfy $\phi_k(0)=1/k!$ and $\phi_{k+1}(z)=\big(\phi_k(z)-1/k!\big)/z$. They arise
from the variation-of-constants (Volterra) formula
$y(t_n+h)=e^{hL}y_n+h\int_0^1e^{(1-\theta)hL}N\big(t_n+\theta h,y(t_n+\theta h)\big)\,d\theta$
when $N$ is replaced by a polynomial in $\theta$. [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md)
state the formula (§1, Eq. (1.5)) and build every method of their survey on it. Their
"basic idea" is "to identify a prototypical differential equation that has stiffness
properties similar to those of the underlying equation (1.1) and that can be solved
exactly", typically a linearization, and to treat the remainder through this formula. They write the problem as $u'+Au=g(t,u)$, so their matrix functions
are evaluated at $-hA$; on this page $L=-A$ and $N=g$ throughout. Their survey covers two
classes of stiff problems: those whose Jacobian has eigenvalues with large negative real
part, typified by semilinear parabolic problems, and highly oscillatory problems with large
purely imaginary eigenvalues (§1). Exponential
Runge–Kutta, exponential Rosenbrock and EPIRK methods are named by Chinomona & Reynolds,
alongside IMEX additive Runge–Kutta methods and general linear methods, as the main
families for problems that couple stiff and non-stiff processes
([Chinomona & Reynolds 2021](/sources/chinomona-2021.md), §1).

**History, as given by Hochbruck & Ostermann (2010, §6).** Exponential integrators "were
first considered by Hersch (1958)"; Certaine (1960) gave exponential multistep methods, Pope
(1963) the exponential Rosenbrock–Euler method, Lawson (1967) and Ehle & Lawson (1975) the
first exponential Runge–Kutta methods, Nørsett (1969) explicit exponential Adams methods,
and Friedli (1978) the first methods with more than one φ-function. "The term 'exponential
integrators' was coined in the seminal paper by Hochbruck, Lubich and Selhofer (1998)." In
the early stiff literature the exponential and $\phi_1$ were replaced by rational (Padé)
approximations, which gave implicit and semi-implicit Runge–Kutta, Rosenbrock and W-methods
(§1; see [Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md)).

Three sources develop the order theory. [Luan (2021)](/sources/luan-2021.md) works with the
stiff order conditions of exponential Runge–Kutta methods and proves a convergence theorem
with one weakened condition. [Luan et al. (2022)](/sources/luan-2022.md) recall the
exponential Rosenbrock conditions to order 6. [Dallerit & Tokman (2025)](/sources/dallerit-2025.md)
introduce φ-order conditions and solve them in closed form. All three are collected at
[stiff order conditions of exponential Runge–Kutta methods](/results/exponential-runge-kutta-stiff-order-conditions.md).
The other sources use the idea in several ways, below. In practice the cost of an
exponential method lies in the actions of φ-functions on vectors, treated at
[evaluating φ-functions](/methods/phi-function-evaluation.md).

## Convention for φ-functions

Chinomona & Reynolds (2021, §3) define $\varphi_k(z)=\int_0^1e^{z(1-t)}t^{k-1}\,dt$ without
the factor $1/(k-1)!$, with the recursion $\varphi_{k+1}(z)=(k\varphi_k(z)-1)/z$. Their
functions are $(k-1)!\,\phi_k$ in the registry normalisation above; the two recursions are
equivalent. These sources use the
registry normalisation:

- Hochbruck & Ostermann (2010, §2.2, Eqs. (2.10)–(2.11)), at argument $-hA=hL$, with the
  tableau shorthand $\varphi_{j,k}=\varphi_j(-c_khA)$, $\varphi_j=\varphi_j(-hA)$, i.e.
  $\phi_{j,k}=\phi_j(c_khL)$, $\phi_j=\phi_j(hL)$ below (in their Rosenbrock tableaux the
  argument is $hJ_n$);
- Luan (2021, Eq. 1.4);
- Luan et al. (2022, Eq. 2.4), in an $h$-scaled integral form;
- [Deka & Einkemmer (2022)](/sources/deka-2022.md) (§2), by the recursion
  $\phi_{k+1}(z)=(\phi_k(z)-1/k!)/z$ (printed for $k\ge1$; it is needed from $k=0$);
- [Caliari et al. (2024)](/sources/caliari-2024.md), with $\phi_1(z)=(e^z-1)/z$ and
  $\phi_2(z)=(\phi_1(z)-1)/z$;
- Dallerit & Tokman (2025, Eqs. 3–4), with $\phi_k(z)=\sum_{m\ge0}z^m/(m+k)!$.

Of the remaining sources, [Buvoli & Minion (2024)](/sources/buvoli-2024.md) print
$\varphi_j(hL)=\int_0^1e^{(1-s)hL}s^j\,ds$ (Eq. 9), which is neither convention. Their
tableaux (App. A), however, need the registry normalisation $\phi_k(0)=1/k!$, so the printed
definition is a slip (see Qualifications). [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md)
(§2, Eqs. 5–9) work with the unnormalised matrices
$\int_0^he^{(h-s)L}s^{k-1}\,ds=(k-1)!\,h^k\phi_k(hL)$ and with $e^{hL}=\phi_0(hL)$
*(compiler translation, by the substitution $s=h\theta$; it agrees with their recurrence (9)
and the leading series term $h^k/k$ of their Eq. A.2)*.

## Exponential quadrature rules (linear problems)

For a linear problem with a time-dependent forcing, $y'=Ly+N(t)$, Hochbruck & Ostermann
(2010, §2.2, Eqs. (2.9), (2.12)) interpolate $N$ at nodes $c_1,\dots,c_s$ inside the step:
$y_{n+1}=e^{h_nL}y_n+h_n\sum_{i=1}^sb_i(h_nL)N(t_n+c_ih_n)$ (variable steps $h_n$). The
collocation choice is $b_i(hL)=\int_0^1e^{(1-\theta)hL}\ell_i(\theta)\,d\theta$ with
$\ell_i$ the Lagrange polynomials of the nodes (page-local $\ell_i$). Their Theorem 2.7: if
the weights are uniformly bounded and
$\sum_ib_i(hL)\,c_i^{j-1}/(j-1)!=\phi_j(hL)$ for $j=1,\dots,p$ (Eqs. (2.17)–(2.18)), the
method converges with order $p$, with error bounded by
$C\sum_jh_j^p\int_{t_j}^{t_{j+1}}\lVert N^{(p)}(\tau)\rVert\,d\tau$ for any step-size
sequence, under only the $C_0$-semigroup bound $\lVert e^{tL}\rVert\le Ce^{\omega t}$
(Assumption 2.2; page-local $C$, $\omega$). The collocation rule has order $s$ (Cor. 2.8).
Examples (Exs. 2.5–2.6): $s=1$,
$y_{n+1}=y_n+h\phi_1(hL)\big(Ly_n+N(t_n+c_1h)\big)$, is the exponential Euler quadrature rule
for $c_1=0$ and the exponential midpoint rule for $c_1=\tfrac12$; $s=2$ with $c_1=0$,
$c_2=1$ is the exponential trapezoidal rule. The bound $\lVert e^{tL}\rVert\le C$ with
$C=1$, $\omega=0$ holds in the Euclidean norm for Hermitian negative semidefinite and for
skew-Hermitian $L$ independently of the dimension, which is what makes the temporal
results mesh-independent (Ex. 2.3).

## Exponential Runge–Kutta methods

**General format** (Hochbruck & Ostermann 2010, §2.3, Eqs. (2.20)–(2.25)). In value form an
$s$-stage exponential Runge–Kutta method is
$Y_i=\chi_i(hL)y_n+h\sum_ja_{ij}(hL)N(t_n+c_jh,Y_j)$,
$y_{n+1}=\chi(hL)y_n+h\sum_ib_i(hL)N(t_n+c_ih,Y_i)$ (page-local $\chi$, $\chi_i$ with
$\chi(0)=\chi_i(0)=1$). The underlying Runge–Kutta method has coefficients $a_{ij}(0)$,
$b_i(0)$, assumed to satisfy $\sum_jb_j(0)=1$, $\sum_ja_{ij}(0)=c_i$. The method preserves
equilibria iff $\sum_jb_j(z)=(\chi(z)-1)/z$ and $\sum_ja_{ij}(z)=(\chi_i(z)-1)/z$
(Eq. (2.21)). The main choice $\chi=e^z$, $\chi_i=e^{c_iz}$ turns these into the
**simplifying assumptions**

$$\sum_jb_j(z)=\phi_1(z),\qquad \sum_ja_{ij}(z)=c_i\phi_1(c_iz)\qquad\text{(Eq. (2.23))},$$

which Hochbruck & Ostermann assume throughout their §2.3; they also make the methods
invariant under transformation to autonomous form. Explicit methods have $c_1=0$ and
$a_{ij}=0$ for $j\ge i$. Eliminating $\chi$ gives the difference form below (Eq. (2.25)).
Explicit methods cannot satisfy the stage conditions of order 2 at every stage, so "the
internal stages are of order one only" (p. 226), which "makes the construction of
higher-order methods quite involved". The explicit form goes back to Friedli (1978), whose
"non-stiff order conditions" are "not sufficient to analyse parabolic problems" (p. 221, as
recalled).

For $y'=Ly+N(t,y)$ an explicit exponential Runge–Kutta (ExpRK) method has stages
$Y_i=y_n+c_ih\phi_1(c_ihL)f(t_n,y_n)+h\sum_{j=2}^{i-1}a_{ij}(hL)D_j$ and update
$y_{n+1}=y_n+h\phi_1(hL)f(t_n,y_n)+h\sum_{i=2}^sb_i(hL)D_i$, with
$D_i=N(t_n+c_ih,Y_i)-N(t_n,y_n)$ (page-local) and coefficients that are combinations of
$\phi_k(c_ihL)$ and $\phi_k(hL)$ (Luan 2021, Eqs. 1.2–1.3). The format and its stiff order
conditions are on the [result page](/results/exponential-runge-kutta-stiff-order-conditions.md).
Methods derived from Taylor-expanded ("classical") conditions have error terms that depend
on $\lVert L\rVert$. Methods satisfying the stiff conditions do not, and Luan, after
Hochbruck–Ostermann, calls them "stiffly accurate". That is a different notion from
[stiff accuracy](/properties/stiff-accuracy.md) of a Runge–Kutta tableau (Luan 2021, §1).
The 2010 survey of Hochbruck & Ostermann speaks of the **stiff order** of a method, the
order of a global error bound $Ch^p$ whose constant depends neither on the stiffness nor on
$h$ (§1, p. 212); the phrase "stiffly accurate" does not occur in it.

**Low orders.** In the notation above (Luan 2021, §2.2, Eqs. 2.5–2.6; Caliari et al. 2024,
Appendix):

- exponential Euler, $y_{n+1}=y_n+h\phi_1(hL)f(t_n,y_n)$, is first order in general (Deka &
  Einkemmer 2022, §2; Caliari et al. 2024, Appendix). Hochbruck & Ostermann (2010, Thm. 2.14)
  prove stiff order 1 for semilinear parabolic problems (analytic semigroup, $N$ locally
  Lipschitz from the domain of a fractional power of $-L$, Assumptions 2.9–2.10), with error
  $\le Ch\sup_t\lVert(-L)^{\varsigma-1}\tfrac{d}{dt}N(t,y(t))\rVert$ in that norm (page-local
  regularity index $\varsigma$);
- second order (expRK2s2, the scheme "erk2p2" of Caliari et al.): $Y_2=y_n+c_2h\phi_1(c_2hL)f(t_n,y_n)$ and
  $y_{n+1}=y_n+h\phi_1(hL)f(t_n,y_n)+\tfrac h{c_2}\phi_2(hL)D_2$, $0<c_2\le1$. The variant
  "erk2p1" replaces the last term by $\tfrac h{2c_2}\phi_1(hL)D_2$ and avoids $\phi_2$.
  These are the one-parameter families (2.39) and (2.40) of Hochbruck & Ostermann (2010,
  Ex. 2.18; $b_1=\phi_1-\tfrac1{c_2}\phi_2$, $b_2=\tfrac1{c_2}\phi_2$, resp.
  $b_1=(1-\tfrac1{2c_2})\phi_1$, $b_2=\tfrac1{2c_2}\phi_1$, $a_{21}=c_2\phi_{1,2}$ in value
  form) *(compiler check, not in the sources)*. They state that second order needs at least two stages,
  that (2.40) with $c_2=\tfrac12$ has $b_1=0$, and that both families are B-consistent of
  order one, as recalled from Strehmel & Weiner (1992) (see
  [B-convergence](/definitions/b-convergence.md));
- third order (expRK3s3): $Y_3=y_n+\tfrac23h\phi_1(\tfrac23hL)f(t_n,y_n)+\tfrac{4}{9c_2}h\phi_2(\tfrac23hL)D_2$
  and $y_{n+1}=y_n+h\phi_1(hL)f(t_n,y_n)+\tfrac32h\phi_2(hL)D_3$, with $c_2\ne\tfrac23$.

Luan states without detail that no method improves on these at orders 2 and 3 under his
cost measure (§4).

**Cost model.** A stage whose matrix functions all have the same argument $c_ihL$ is one
linear combination $\sum_k\phi_k(c_ihL)V_k$, and costs one call of a combination routine.
Stages that share their vectors $V_k$, or are mutually independent, can share a call
(Luan 2021, §2.1, Eq. 2.4; see [evaluating φ-functions](/methods/phi-function-evaluation.md)).
The two older methods that are stiffly accurate in Luan's sense fail this test:

- **expRK4s5** (Hochbruck–Ostermann; order 4, nodes $c_2=c_3=c_5=\tfrac12$, $c_4=1$) has a
  last stage that mixes arguments $\tfrac12hL$ and $hL$. It needs 6 sequential evaluations
  per step.
- **expRK5s8** (Luan–Ostermann; order 5) has stages 7 and 8 that mix two and three
  arguments, and none of its stages can be computed simultaneously. It needs 11 evaluations
  (Remark 2.1, §5).

**expRK4s6 and expRK5s10** (Luan 2021, §4, contributions). Both families are built from his
one-weakened-condition theorem. With page-local Lagrange-type coefficient functions

$$\Theta_{j;k}(c)=\frac{-c^2c_k\,\phi_2(chL)+2c^3\phi_3(chL)}{c_j(c_j-c_k)},\qquad
\Theta_{j;k,l}(c)=\frac{c^2c_kc_l\,\phi_2(chL)-2c^3(c_k+c_l)\,\phi_3(chL)+6c^4\phi_4(chL)}{c_j(c_j-c_k)(c_j-c_l)},$$

both families start with $Y_2=y_n+c_2h\phi_1(c_2hL)f(t_n,y_n)$ and $a_{i2}=\tfrac{c_i^2}{c_2}\phi_2(c_ihL)$
for $i=3,4$, and every stage also carries the term $c_ih\phi_1(c_ihL)f(t_n,y_n)$. They
continue as follows:

- **expRK4s6** (order 4, $s=6$; Eqs. 4.4–4.10): $a_{i3}=\Theta_{3;4}(c_i)$, $a_{i4}=\Theta_{4;3}(c_i)$
  for $i=5,6$; $b_5=\Theta_{5;6}(1)$, $b_6=\Theta_{6;5}(1)$; all other coefficients zero. The
  nodes are free except for $c_5=(4c_6-3)/(6c_6-4)$, which is the weakened condition 4. The
  representative is $c_2=c_3=\tfrac12$, $c_4=c_6=\tfrac13$, $c_5=\tfrac56$. Only
  $\phi_1,\phi_2,\phi_3$ appear. The pairs $\{Y_3,Y_4\}$ and $\{Y_5,Y_6\}$ are independent
  within each pair and share one format, so a step costs 4 sequential evaluations: $Y_2$, the
  pair $\{Y_3,Y_4\}$, the pair $\{Y_5,Y_6\}$ and $y_{n+1}$ (Remark 4.1, §5).
- **expRK5s10** (order 5, $s=10$; Eqs. 4.11–4.26): $a_{ij}=\Theta_{j;k}(c_i)$ for $i=5,6,7$ and
  $\{j,k\}=\{3,4\}$; $a_{ij}=\Theta_{j;k,l}(c_i)$ for $i=8,9,10$ and $\{j,k,l\}=\{5,6,7\}$;
  $b_i=\Theta_{i;k,l}(1)$ for $\{i,k,l\}=\{8,9,10\}$; all other coefficients zero. Only
  condition 8 is weakened. The nodes $c_8,c_9,c_{10}$ must be distinct, positive and satisfy
  $\tfrac14(c_8+c_9+c_{10})-\tfrac13(c_8c_9+c_8c_{10}+c_9c_{10})+\tfrac12c_8c_9c_{10}=\tfrac15$
  (Eq. 4.14). The representative is $c_2=c_3=c_5=\tfrac12$, $c_4=c_6=\tfrac13$,
  $c_7=\tfrac14$, $c_8=\tfrac3{10}$, $c_9=\tfrac34$, $c_{10}=1$, which satisfies (4.14).
  The groups $\{Y_3,Y_4\}$, $\{Y_5,Y_6,Y_7\}$ and $\{Y_8,Y_9,Y_{10}\}$ give 5 sequential
  evaluations per step (Remark 4.2).

**Tests** (Luan 2021, §6; MATLAB on one iMac). All four methods are compared on three
problems: a 1D semilinear parabolic problem of Hochbruck–Ostermann (200 points,
$\lVert L\rVert_\infty\approx1.6\times10^5$), a cubic nonlinear Schrödinger equation (128
Fourier modes) and the [Gray–Scott model](/benchmarks/gray-scott-model.md). The new
methods reach orders 4 and 5. At equal step counts they are as accurate as or more accurate
than expRK4s5 and expRK5s8, and they are faster in CPU time. expRK4s6 is the most efficient
at loose tolerances (errors above about $10^{-6}$ on the parabolic problem) and expRK5s10
at tight ones (Figs. 6.1–6.4).

**Cox–Matthews and Krogstad schemes (value format).** Many applications write the stages
with values of $N$ rather than differences:
$Y_i=e^{c_ihL}y_n+h\sum_{j<i}a_{ij}(hL)N(t_n+c_jh,Y_j)$ and
$y_{n+1}=e^{hL}y_n+h\sum_ib_i(hL)N(t_n+c_ih,Y_i)$, with $\phi_k=\phi_k(hL)$ and
$\phi_{k,j}=\phi_k(c_jhL)$ (Buvoli & Minion 2024, Eqs. 10–12, App. A). For $i\ge2$ the weights
$b_i$ are those of the difference format above, and $b_1=\phi_1-\sum_{i\ge2}b_i$ *(compiler
check, not in the sources)*. The named schemes are:

| scheme | $c$ | nonzero $a_{ij}$ | $b$ |
|---|---|---|---|
| exponential Euler (ERK1) | $0$ | — | $\phi_1$ |
| Cox–Matthews ETD2RK (ERK2) | $(0,1)$ | $a_{21}=\phi_1$ | $(\phi_1-\phi_2,\ \phi_2)$ |
| Cox–Matthews ETD3RK (ERK3) | $(0,\tfrac12,1)$ | $a_{21}=\tfrac12\phi_{1,2}$; $a_{31}=-\phi_1$, $a_{32}=2\phi_1$ | $(\phi_1-3\phi_2+4\phi_3,\ 4\phi_2-8\phi_3,\ 4\phi_3-\phi_2)$ |
| Cox–Matthews ETD4RK (ETDRK4) | $(0,\tfrac12,\tfrac12,1)$ | $a_{21}=a_{32}=\tfrac12\phi_{1,2}$; $a_{41}=\tfrac12\phi_{1,2}(\phi_{0,2}-I)$, $a_{43}=\phi_{1,2}$ | $(\phi_1-3\phi_2+4\phi_3,\ 2\phi_2-4\phi_3,\ 2\phi_2-4\phi_3,\ 4\phi_3-\phi_2)$ |
| Krogstad (ERK4) | $(0,\tfrac12,\tfrac12,1)$ | $a_{21}=\tfrac12\phi_{1,2}$; $a_{31}=\tfrac12\phi_{1,2}-\phi_{2,2}$, $a_{32}=\phi_{2,2}$; $a_{41}=\phi_1-2\phi_2$, $a_{43}=2\phi_2$ | as ETD4RK |
| Strehmel–Weiner (1992, Ex. 4.5.5) | $(0,\tfrac12,\tfrac12,1)$ | $a_{21}=\tfrac12\phi_{1,2}$; $a_{31}=\tfrac12\phi_{1,2}-\tfrac12\phi_{2,2}$, $a_{32}=\tfrac12\phi_{2,2}$; $a_{41}=\phi_1-2\phi_2$, $a_{42}=-2\phi_2$, $a_{43}=4\phi_2$ | $(\phi_1-3\phi_2+4\phi_3,\ 0,\ 4\phi_2-8\phi_3,\ 4\phi_3-\phi_2)$ |
| expRK4s5 (Hochbruck–Ostermann 2005) | $(0,\tfrac12,\tfrac12,1,\tfrac12)$ | as Krogstad in rows 2–3; $a_{41}=\phi_1-2\phi_2$, $a_{42}=a_{43}=\phi_2$; $a_{52}=a_{53}=\tfrac12\phi_{2,2}-\phi_3+\tfrac14\phi_2-\tfrac12\phi_{3,2}$, $a_{54}=\tfrac14\phi_{2,2}-a_{52}$, $a_{51}=\tfrac12\phi_{1,2}-2a_{52}-a_{54}$ | $(\phi_1-3\phi_2+4\phi_3,\ 0,\ 0,\ 4\phi_3-\phi_2,\ 4\phi_2-8\phi_3)$ |

The ERK1–ERK3 and Krogstad rows are Buvoli & Minion's tableaux (App. A). Hochbruck &
Ostermann (2010, Eqs. (2.41)–(2.43), p. 229) print the ETD4RK, Krogstad, Strehmel–Weiner and
five-stage rows; their ETD4RK and Krogstad tableaux agree with the rows above once
$\phi_{j,3}=\phi_{j,2}$ ($c_3=c_2$) and $\phi_{j,4}=\phi_j$ ($c_4=1$) are used, and the
Strehmel–Weiner and expRK4s5 rows are theirs written with the same identities
($\phi_{j,5}=\phi_{j,2}$) *(compiler check, not in the sources)*. Against their stiff order conditions,
ETD4RK can drop to order two "in the worst case", Krogstad's and the Strehmel–Weiner scheme to
order three, and the five-stage method has order four (Ex. 2.19, p. 229); the conditions and
these statements are on the
[result page](/results/exponential-runge-kutta-stiff-order-conditions.md). The ETD4RK row is
Permyakova & Goldobin's Eq. (4), the original Cox–Matthews scheme, translated: its last stage
is built from the first internal stage, $Y_4=e^{hL/2}Y_2+\tfrac h2\phi_1(\tfrac12hL)\big(2N(Y_3)-N(y_n)\big)$,
which gives the $a_{41}$ above *(compiler translation)*. Their ETD3RK (Eq. 3) coincides with
Buvoli & Minion's ERK3. ETD4RK and Krogstad's method share their weights and differ in the
third and fourth stages. Permyakova & Goldobin quote the one-step errors
$-h^3\ddot N/12$ for ETD2RK (from Cox and Matthews) and terms proportional to
$h^4\,d^3N/dt^3$ and $h^5\,d^4N/dt^4$ for ETD3RK and ETD4RK, and recall that an ETD scheme of
order $n$ is exact when $N$ is a polynomial of degree $n-1$ in time over the step (§1–2).
These are classical-order statements; how ETD4RK fares against the stiff conditions is on the
[result page](/results/exponential-runge-kutta-stiff-order-conditions.md).

## Exponential Rosenbrock methods

Exponential Rosenbrock (ExpRB) methods linearize at every step:
$f(t,y)=J_ny+V_nt+N_n(t,y)$, with $V_n=\partial_tf(t_n,y_n)$ and the remainder $N_n$
(page-local). They apply the ExpRK format with $L\to J_n$ and $N\to N_n$, plus a term
$c_i^2h^2\phi_2(c_ihJ_n)V_n$ in each stage and $h^2\phi_2(hJ_n)V_n$ in the update
(Luan et al. 2022, §2.1, Eqs. 2.1–2.6). For autonomous problems $V_n=0$ and
$N_n(y)=f(y)-J_ny$. Because $N_n$ has zero derivatives at $(t_n,y_n)$, every $D_i$ is
$\mathcal O(h^2)$:

- every ExpRB method has order at least 2, and the conditions are few, 7 up to order 6
  (Remark 2.1; see the
  [result page](/results/exponential-runge-kutta-stiff-order-conditions.md));
- the exponential Rosenbrock–Euler method $y_{n+1}=y_n+h\phi_1(hJ_n)f(t_n,y_n)+h^2\phi_2(hJ_n)V_n$
  is second order, because it uses the Jacobian (Luan et al. 2022, §2.4.1; Deka & Einkemmer
  2022, §2.1, Eq. 3; Caliari et al. 2024, Appendix). Hochbruck & Ostermann (2010, §2.4)
  prove it second-order convergent as the worked case of their Theorem 2.22 and credit the
  method, in this non-autonomous form, to Pope (1963).

**Original formulation** (Hochbruck & Ostermann 2010, §2.4, Eqs. (2.44)–(2.53)). For
$y'=f(y)$ the method is the explicit ExpRK value format applied to $y'=J_ny+N_n(y)$ at every
step, with arguments $c_ihJ_n$. Under the simplifying assumptions it can be rewritten so that
"each stage of the method consists of a perturbed exponential Rosenbrock–Euler step",
$Y_i=y_n+c_ih\phi_1(c_ihJ_n)f(y_n)+h\sum_{j=2}^{i-1}a_{ij}(hJ_n)D_j$, with
$D_j=N_n(Y_j)-N_n(y_n)$ small in norm, so that only the term with $f(y_n)$ needs an
expensive Krylov approximation (Eq. (2.48); see
[evaluating φ-functions](/methods/phi-function-evaluation.md)). Such methods preserve
equilibria, have small defects and simple stiff order conditions (four up to order 4,
Table 2.3). A non-autonomous problem is made autonomous by adding $t$ as a variable, "standard
for Rosenbrock methods as well", although it "changes a linear non-autonomous problem into a
nonlinear one"; the φ-functions of the augmented Jacobian have the block form
$\begin{pmatrix}\phi_k(0)&0\\h\phi_{k+1}(hJ_n)V_n&\phi_k(hJ_n)\end{pmatrix}$, which yields the
$h^2c_i^2\phi_2(c_ihJ_n)V_n$ terms above (Eqs. (2.50)–(2.52)). Consequences of the order
conditions they draw (§2.4, Ex. 2.25): the weights of every third-order method depend on
$\phi_3$, those of every fourth-order method on $\phi_3$ and $\phi_4$; and the
exponential Rosenbrock-type methods of Hochbruck, Lubich & Selhofer (1998), which use
$\phi_1$ only, "cannot have order larger than two", although their exp4 has classical order
four (three stages, implemented as seven with three function evaluations). Tokman's EPI
methods use the same linearization (§2.4).

- **exprb32** (Ex. 2.23): $c=(0,1)$, $a_{21}=\phi_1$, $b=(\phi_1-2\phi_3,\ 2\phi_3)$, with the
  exponential Rosenbrock–Euler method ($\hat b_1=\phi_1$) as embedded second-order
  estimate; order 3. Its $b_2=2\phi_3$ is the $c_2=1$ case of the weight
  $\tfrac2{c_2^2}\phi_3$ below.
- **exprb43** (Ex. 2.24): $c=(0,\tfrac12,1)$, $a_{21}=\tfrac12\phi_1(\tfrac12hJ_n)$, $a_{31}=0$,
  $a_{32}=\phi_1$, $b=(\phi_1-14\phi_3+36\phi_4,\ 16\phi_3-48\phi_4,\ -2\phi_3+12\phi_4)$,
  embedded $\hat b=(\phi_1-14\phi_3,\ 16\phi_3,\ -2\phi_3)$ of order 3; order 4. In difference
  form this is the EXPRB43 of Deka & Einkemmer below, and it satisfies
  $\sum_ib_ic_i^2=2\phi_3$, $\sum_ib_ic_i^3=6\phi_4$:
  $\tfrac14(16\phi_3-48\phi_4)+(-2\phi_3+12\phi_4)=2\phi_3$ and
  $\tfrac18(16\phi_3-48\phi_4)+(-2\phi_3+12\phi_4)=6\phi_4$ *(compiler check, not in the
  sources)*. "The internal stages of the above methods are just exponential Rosenbrock–Euler
  steps."

**Schemes generalized to non-autonomous form with free nodes** (Luan et al. 2022, §2.4):

- **exprb32** (order 3): $b_2=\tfrac2{c_2^2}\phi_3(hJ_n)$ with one internal stage at $c_2$. The
  original has $c_2=1$; $c_2=\tfrac12$ is used in the tests.
- **exprb42** (order 4, Luan 2017): the same structure with $c_2=\tfrac34$, so $b_2=\tfrac{32}9\phi_3(hJ_n)$.
- **pexprb54s4** (order 5, Luan–Ostermann 2016; parallel, with an embedded fourth-order method):
  - $a_{32}=\tfrac{2c_3^3}{c_2^2}\phi_3(c_3hJ_n)$ and $a_{42}=\tfrac{2c_4^3}{c_2^2}\phi_3(c_4hJ_n)$;
  - $b_3=\frac{2c_4\phi_3-6\phi_4}{c_3^2(c_4-c_3)}$ and $b_4=\frac{2c_3\phi_3-6\phi_4}{c_4^2(c_3-c_4)}$, at argument $hJ_n$;
  - $c_4=\frac{3(5c_3-4)}{5(4c_3-3)}$;
  - stages 3 and 4 are independent, so the method behaves like a three-stage method.
- **pexprb65s7** (order 6, with an embedded fifth-order method): the stage groups
  $\{Y_2,Y_3\}$ and $\{Y_4,\dots,Y_7\}$ are independent, so it behaves like a three-stage
  method.

Against the first two Rosenbrock conditions $\sum_ib_ic_i^2=2\phi_3$ and
$\sum_ib_ic_i^3=6\phi_4$: exprb32 meets the first; pexprb54s4 meets both for every $c_3$;
exprb42 meets the first, and the second only at $Z=0$ ($b_2(0)c_2^3=\tfrac14=6\phi_4(0)$),
which is what fixes $c_2=\tfrac34$, a weakened condition in the sense of the
[result page](/results/exponential-runge-kutta-stiff-order-conditions.md)
*(compiler check, not in the sources)*. Luan et al. turn these schemes into multirate methods MERB2–MERB6.
Their Lemma 2.2 shows that a stage whose coefficients are combinations of
$\phi_k(c_ihJ_n)$ is the exact solution at $c_ih$ of a linear ODE with polynomial forcing;
see [multirate exponential methods](/methods/multirate-exponential-methods.md).

**EXPRB43 and EXPRB54s4** (as used by Deka & Einkemmer 2022, §2.1, Eqs. 4–7; autonomous,
$D_i=N_n(Y_i)-N_n(y_n)$, $f_n=f(y_n)$):

$$\begin{aligned}
&\text{EXPRB43 (Hochbruck et al. 2009):}\\
&Y_2=y_n+\tfrac12h\phi_1(\tfrac12hJ_n)f_n,\qquad Y_3=y_n+h\phi_1(hJ_n)f_n+h\phi_1(hJ_n)D_2,\\
&y_{n+1}=y_n+h\phi_1(hJ_n)f_n+h\phi_3(hJ_n)(16D_2-2D_3)+h\phi_4(hJ_n)(-48D_2+12D_3),\\
&\text{EXPRB54s4 (Luan–Ostermann 2014):}\\
&Y_2=y_n+\tfrac14h\phi_1(\tfrac14hJ_n)f_n,\qquad Y_3=y_n+\tfrac12h\phi_1(\tfrac12hJ_n)f_n+4h\phi_3(\tfrac12hJ_n)D_2,\\
&Y_4=y_n+\tfrac9{10}h\phi_1(\tfrac9{10}hJ_n)f_n+\tfrac{729}{125}h\phi_3(\tfrac9{10}hJ_n)D_3,\\
&y_{n+1}=y_n+h\phi_1(hJ_n)f_n+h\phi_3(hJ_n)\big(18D_3-\tfrac{250}{81}D_4\big)+h\phi_4(hJ_n)\big(-60D_3+\tfrac{500}{27}D_4\big).
\end{aligned}$$

Deka & Einkemmer print the updates with values $N_n(\cdot)$, whose coefficients sum to zero.
The difference form above follows from that *(compiler rewriting, checked against the order
conditions)*. Their embedded solutions are:

- for EXPRB43, the update without the $\phi_4$ term (order 3), which gives a third-order
  error estimate;
- for EXPRB54s4, $y_n+h\phi_1f_n+h\phi_3(64D_2-8D_3)+h\phi_4\big(-60D_2-\tfrac{285}8D_3+\tfrac{125}8D_4\big)$
  (order 4).

They count 5 matrix-function evaluations per step for EXPRB43 and 10 for EXPRB54s4 (§5.3).
On their resistive-MHD reconnection problem the fifth-order EXPRB54s4 with Leja
interpolation is worse than EXPRB43, despite its higher order (§5.3, Fig. 13).

## Exponential multistep and general linear methods

**Exponential Adams methods** (Hochbruck & Ostermann 2010, §2.5, after Certaine 1960 and
Nørsett 1969, whose aim was A-stable generalizations of the explicit Adams methods). The
nonlinearity is interpolated at the past points $t_{n-k+1},\dots,t_n$, with
$G_j=N(t_j,y_j)$ and backward differences $\nabla^jG_n$ (page-local):

$$y_{n+1}=e^{hL}y_n+h\sum_{j=0}^{k-1}\gamma_j(hL)\nabla^jG_n,\qquad
\gamma_j(z)=(-1)^j\int_0^1e^{(1-\theta)z}\binom{-\theta}{j}d\theta$$

(Eq. (2.69); page-local $\gamma_j$, with $\gamma_0=\phi_1$ and the recurrence
$z\gamma_k(z)+1=\sum_{j=0}^{k-1}\frac1{k-j}\gamma_j(z)$ of Nørsett). For $L=0$ this is the
explicit Adams method (see [linear multistep methods](/methods/linear-multistep-method.md)).
In the implementation form (2.70) a step is a corrected exponential Euler step; since
$\lVert\nabla^jG_n\rVert=\mathcal O(h^j)$, the Krylov approximations become cheaper with $j$.
For $k=2$: $y_{n+1}=y_n+h\phi_1(hL)(Ly_n+G_n)+h\phi_2(hL)(G_n-G_{n-1})$ (Eq. (2.71)).
Theorem 2.27: under Assumptions 2.9–2.10, a $k$-th-order smooth forcing and starting errors
$\le c_0h^k$, the $k$-step method converges with order $k$ (proved for $k=2$, "the proof for
$k>2$ is analogous"). Related schemes they list: Cox–Matthews (2002) in the same class;
Calvo–Palencia (2006), with variation of constants over $kh$ and all parasitic roots on the unit
circle; Beylkin–Keiser–Vozovoi (1998).

**Linearized exponential multistep methods** (§2.6). With the per-step Jacobian $J_n$ and
$N_n(y)=f(y)-J_ny$ (autonomous case), Tokman's (2006) two-step method is
$y_{n+1}=y_n+h\phi_1(hJ_n)f(y_n)-\tfrac23h\phi_2(hJ_n)\big(N_n(y_n)-N_n(y_{n-1})\big)$, and
Hochbruck & Ostermann propose the variant

$$y_{n+1}=y_n+h\phi_1(hJ_n)f(y_n)-2h\phi_3(hJ_n)\big(N_n(y_n)-N_n(y_{n-1})\big)\qquad\text{(Eq. (2.72))},$$

which coincides with Tokman's for $J_n=0$ and "has better convergence properties": it is
third-order convergent (Thm. 2.29; no counterexample for Tokman's method is given).
Since $N_n(y_n)-N_n(y_{n-1})=-r_n(y_{n-1})$ with the remainder $r_n$ of the
stiffness-resilient section below, (2.72) is the order-3 method SREXP_MS3 of Dallerit &
Tokman (2025) *(compiler check, not in the sources)*.

**Exponential general linear methods** (§2.7, after Ostermann, Thalhammer & Wright 2006)
combine $s$ stages with $k-1$ past values $N(t_{n-\ell},y_{n-\ell})$, weighted by further
matrix functions (Eq. (2.75)); $k=1$ gives exponential Runge–Kutta and $s=1$ exponential Adams
methods. A method has *stage order* $q$ if its stage defects are $\mathcal O(h^{q+1})$ and
*quadrature order* $p$ if its step defect is $\mathcal O(h^{p+1})$; both are expressed by
matrix-function conditions (2.77). Theorem 2.31: conditions (2.77) up to $p-1$ plus the
order-$p$ quadrature condition at $z=0$ only (Eq. (2.78), a weakened condition) give the
error bound
$Ch^{p-\alpha+\varsigma}\sup\lVert(-L)^\varsigma\tilde N^{(p-1)}\rVert+Ch^p\sup\lVert\tilde N^{(p)}\rVert$
plus starting errors, with $\tilde N(t)=N(t,y(t))$, $\alpha\in[0,1)$ the fractional-power
index of the space on which $N$ is Lipschitz and $\varsigma$ a regularity index (page-local
$\tilde N$, $\alpha$, $\varsigma$). [Lawson methods](/methods/lawson-methods.md)
with past values are of this class.

## EPIRK methods

Exponential propagation iterative Runge–Kutta (EPIRK) methods (Tokman) place a separate
scaling inside every matrix-function argument. EPIRK5P1 (Tokman et al. 2012), as given by
Deka & Einkemmer (2022, §2.2, Eq. 8, Table 1), reads

$$\begin{aligned}
Y_2&=y_n+\hat a_{11}h\phi_1(g_{11}hJ_n)f_n,\qquad
Y_3=y_n+\hat a_{21}h\phi_1(g_{21}hJ_n)f_n+\hat a_{22}h\phi_1(g_{22}hJ_n)D_2,\\
y_{n+1}&=y_n+\hat b_1h\phi_1(g_{31}hJ_n)f_n+\hat b_2h\phi_1(g_{32}hJ_n)D_2+\hat b_3h\phi_3(g_{33}hJ_n)(D_3-2D_2),
\end{aligned}$$

with page-local EPIRK coefficients $\hat a$, $\hat b$, $g$. To six digits they are
$\hat a_{11}=g_{11}=0.351296$, $\hat a_{21}=g_{21}=0.844055$, $\hat a_{22}=1.690589$,
$g_{22}=0.5$, $\hat b_1=g_{31}=1$, $\hat b_2=1.272713$, $\hat b_3=2.271460$,
$g_{32}=0.711111$ and $g_{33}=0.623781$; Table 1 prints 20 digits. The scheme is fifth order.
Setting $g_{32}=0.5$, $g_{33}=1$ gives an embedded fourth-order solution (Loffeld & Tokman
2013). It needs 8 matrix-function evaluations per step, error estimate included. EPIRK
methods are designed to be "Krylov-friendly" (§5.3; see
[evaluating φ-functions](/methods/phi-function-evaluation.md)).

## Stiffness-resilient exponential integrators

Dallerit & Tokman (2025, §6) build a family on their φ-order conditions. The update is
$y_{n+1}=y_n+h\phi_1(hJ_n)f(y_n)+\sum_{k=3}^p\phi_k(hJ_n)\sum_{j=1}^{p-2}\kappa_{k,j}\,h\,r_n(Y_j)$,
with $r_n(y)=f(y)-f(y_n)-J_n(y-y_n)$ and $p-2$ stage values $Y_j$ of classical order $p-2$
at nodes $c_j$ (page-local $r_n$, $\kappa_{k,j}$). The coefficients $\kappa_{k,j}$ follow in
closed form from the nodes (Thm. 6, on the
[result page](/results/exponential-runge-kutta-stiff-order-conditions.md)). The update is a
single φ-combination, evaluated with one Krylov projection per step. The choice of nodes
selects the family:

- **Exponential Runge–Kutta (SREXP_RK$p$), nodes in $(0,1]$** (§6.1, Table 1).
  - *SREXP_RK3*: $Y_1=y_n+\tfrac34h\phi_1(\tfrac34hJ_n)f(y_n)$ and
    $y_{n+1}=y_n+h\phi_1(hJ_n)f(y_n)+\tfrac{32}9h\phi_3(hJ_n)r_n(Y_1)$. Every node
    $0<c_1\le1$ gives φ-order 3. The node $\tfrac34$ is claimed to raise the classical order to
    4, which Fig. 3 shows.
  - *SREXP_RK4*: nodes $c_{1,2}=(10\mp\sqrt{10})/15$, both stages by exponential Euler, and
    $\kappa_{3,1}=\tfrac{155+65\sqrt{10}}{18}$, $\kappa_{3,2}=\tfrac{155-65\sqrt{10}}{18}$,
    $\kappa_{4,1}=\tfrac{-100-55\sqrt{10}}4$, $\kappa_{4,2}=\tfrac{-100+55\sqrt{10}}4$ (Eq. 40).
  - *Higher orders.* For $p>4$ the stages are computed by the
    [dense output](/methods/dense-output.md) of a φ-order-$(p-2)$ method, since exponential
    Euler is no longer accurate enough. An order-6 example uses the SREXP_RK4 stages plus
    four stages at $c=\tfrac14,\tfrac12,\tfrac34,1$ (Eq. 41).
  - *Jacobi nodes.* Nodes at the roots of the shifted Jacobi polynomial
    $P^{(0,2)}_{p-2}(2x-1)$ "in some cases" raise the classical order: SREXP_RK3 and
    SREXP_RK5 converge at orders 4 and 6 (Fig. 3). Methods "of order up to 8" were built this
    way but are not printed, and no theory explains the gain.
  - The nodes $(\tfrac12,\tfrac23)$ and $(\tfrac18,\tfrac19)$ re-derive methods of Rainwater &
    Tokman (§6.1).
- **Exponential multistep (SREXP_MS$p$), nodes $c_j=-j$, stages $Y_j=y_{n-j}$** (§6.2,
  Table 2). The order-3 method is $y_{n+1}=y_n+h\phi_1(hJ_n)f(y_n)+2h\phi_3(hJ_n)r_n(y_{n-1})$.
  The authors state, without showing it, that these methods are identical to the exponential
  Adams methods of Hochbruck & Ostermann. They need $p-2$ past values, so they are hard to
  start, and the distant nodes cost accuracy.
- **Exponential multivalue (SREXP_MV$p$), nodes $c_j=-j/(p-2)$ inside the last step** (§6.3,
  Table 3). The past values come from the previous step's dense output, "for little to no
  extra cost".

All methods of orders 3–6 converge at their design order or better on two
Hochbruck–Ostermann semilinear parabolic problems and on a 2D advection–diffusion–reaction
problem, with no order reduction. At order 5, the exponential Rosenbrock EXPRB_5s4 of
Luan–Ostermann shows "a slight order reduction" on the advection–diffusion problem. At least
two stiffness-resilient schemes beat it in CPU time against error on all three problems
(§7, Figs. 1–4); no hardware or implementation details are given. Higher order pays on the
cheap semilinear problems, while on the advection–diffusion problem lower orders "can
perform better for certain parameter regimes" (§7).

## Partial linear operators

The linear part need not be the whole stiff operator. Caliari et al. (2024, §3, Eq. 11)
treat an advection–diffusion–reaction equation with variable diffusion $a(x)$ and velocity
$b(x)$ (page-local). In $L$ they keep only a constant-coefficient operator: a fraction
$\vartheta\in[0,1]$ (page-local, as on [Lawson methods](/methods/lawson-methods.md)) of the maximal diffusion plus a mean effective velocity. The
variable-coefficient rest goes into the explicitly treated $N$. The matrix functions of $L$
are then cheap, by FFT or by μ-mode products (see
[evaluating φ-functions](/methods/phi-function-evaluation.md)). Stability requires $\vartheta$
above a scheme-dependent bound. The bound is $1/2$ for exponential Euler and for the
second-order expRK2s2 with $c_2=1$, and $1/3$ for "erk2p1" with $c_2=1$ (Thms. 2.1, 2.4,
2.5). The [Lawson methods](/methods/lawson-methods.md) need less (Table 1). The construction
is the exponential counterpart of the
[explicit–implicit–null method](/methods/explicit-implicit-null-method.md). In 2D tests the
reformulated schemes beat the same integrators applied to the full operator with kiops,
and up to a factor of roughly 15 in 3D (§5–6). The exponential Rosenbrock–Euler method
applied to the original formulation is cheaper than Lawson2a and erk2p1 there, but the
reformulation is still superior overall (§5.1).

## Nondiagonal linear parts with precomputed matrix functions

Caliari et al. choose $L$ so that its matrix functions are cheap. Permyakova & Goldobin (2025)
take the opposite route for problems whose constant $L$ is **nondiagonal** and has no cheap
structure: finite differences with variable coefficients, spatially heterogeneous ("frozen
disorder") parameters, or a non-Fourier basis. All "dominating sources of numerical
instability" go into $L$ (§2). Before the run they compute, once, the dense matrices
$e^{hL}$, $e^{hL/2}$, $\tfrac h2\phi_1(\tfrac12hL)$ and $(k-1)!\,h^k\phi_k(hL)$ for $k=1,2,3$, by
integrating auxiliary linear problems (see
[evaluating φ-functions](/methods/phi-function-evaluation.md)). Each step of ETD2RK, ETD3RK or
ETD4RK above is then a few dense matrix–vector products (Eqs. 10–12): ETD2RK needs
$e^{hL}$, $\phi_1(hL)$ and $\phi_2(hL)$, ETD3RK and ETD4RK also $e^{hL/2}$, $\phi_1(\tfrac12hL)$
and $\phi_3(hL)$. Zero eigenvalues of $L$ (conservation laws) are harmless, because the
expressions with $L^{-k}$ are shorthands for power series (§2, App. A).

Their tests (Fortran on an Intel i7-4790K; §3, Figs. 3–8, Table 1) compare against Heun's
predictor–corrector and the Runge–Kutta–Merson method at their explicit stability limits:

- **1D convective Cahn–Hilliard equation** (fourth derivative; 200 points,
  $\Delta x=0.05$, $t\in[0,50]$): an error rate of $10^{-6}$ is reached with $h\approx0.005$
  (ETD2RK), $0.02$ (ETD3RK) and $0.04$ (ETD4RK); the gain in CPU time exceeds a factor 100 for
  all three, largest for ETD4RK, and grows when the grid is refined;
- **1D Matthews–Cox equation** (sixth derivative): a gain of about three orders of
  magnitude;
- **Fokker–Planck chain of a noisy network of quadratic integrate-and-fire neurons**
  (complex, non-banded $L$ that cannot practically be diagonalized; 200–400 modes): gains of
  3–10 for short runs ($h=5\times10^{-4}$) and up to about 100 for long runs
  ($h=5\times10^{-3}$); for example ETD4RK at $h=5\times10^{-3}$ needs 12.5 s of preparation and
  0.397 s of integration for a relative error $4.2\times10^{-10}$, against 13.8 s for the
  predictor–corrector at its maximal stable step $1.2\times10^{-6}$ (Table 1).

The preparation cost grows linearly with $h$, so for short runs the best $h$ balances
preparation and integration and ETD2RK is somewhat more efficient, while for long runs
(spatiotemporal chaos, frozen disorder) the preparation is negligible and ETD4RK gives the
largest gain (§3.1.2, §4). They state, from a scaling argument, that the gain over explicit
schemes grows like $\Delta x^{m-2}$ for a highest spatial derivative of order $m$ (§3.2.2, §4).
The extension to several dimensions is called straightforward but memory-demanding, since
the matrices are $N\times N$ with $N$ the total number of unknowns; their entries decay
rapidly off the diagonal, and zeroing those below about $10^{-16}$ gives a further, smaller
speedup (§3.2.2, §4; page-local $N$).

## Purely imaginary spectra: repartitioning

For non-diffusive problems (dispersive or hyperbolic, with $L$ of purely imaginary spectrum)
exponential integrators have stability regions of a size similar to explicit methods, but the
growth rate of the instability is very small, so their solutions stay usable as long as the
number of steps is not too large (Buvoli & Minion 2024, §3.2, as recalled from Buvoli &
Minion 2022). **Repartitioning** moves a damping term between the two parts. With
$L=U\Lambda U^{-1}$ and an angle $0<\rho<\pi/2$ (page-local $U$, $\Lambda$, $\rho$), the
integrator exponentiates

$$\hat L=L-\tan\rho\;U\lvert\Lambda\rvert U^{-1}\qquad\text{and treats}\qquad
\hat N(t,y)=N(t,y)+\tan\rho\;U\lvert\Lambda\rvert U^{-1}y$$

explicitly (Eqs. 13–15; the source writes $\hat L=L+\epsilon D$ with
$D=-U\lvert\Lambda\rvert U^{-1}$ and $\epsilon=\tan\rho$). The ODE is unchanged, but every
eigenvalue of the exponentiated operator is rotated by $\rho$ into the left half-plane, which
gives a large stability region for a continuous range of small $\rho$. Other damping
operators, such as low-order even spatial derivatives, are possible; for the Fourier-discretized
[nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md) they take
$\operatorname{diag}(-\xi^2)$ ($\xi$ the wavenumbers, page-local) and $\rho=\pi/128$
(Eq. 18). On the partitioned Dahlquist equation $y'=\lambda_1y+\lambda_2y$ ($\lambda_1$
exponentiated, $\lambda_2$ explicit, both imaginary; page-local) repartitioning replaces
$\lambda_1$ by $\lambda_1-\tan\rho\,\lvert\lambda_1\rvert$ and $\lambda_2$ by
$\lambda_2+\tan\rho\,\lvert\lambda_1\rvert$ (§5.1). With $\rho=0$ the exponential integrator
is exact for $\lambda_2=0$; any repartitioning destroys this exactness, and larger $\rho$ costs
accuracy, so the authors advise the smallest $\rho$ that ensures stability (§5.6, Fig. 10).
Repartitioning is the mirror image of the partial linear operators above, which move part of
the stiff operator out of $L$ *(compiler remark, not in the sources)*.

## Exponential integrators as Parareal propagators

Buvoli & Minion (2024) use exponential Runge–Kutta methods as both the coarse and the fine
propagator of [Parareal](/methods/parareal.md), because they resolve fast linear waves exactly
at coarse steps, and claim to be the first to put ETD Runge–Kutta methods inside Parareal (§7).
Fine propagator: Krogstad's fourth-order method; coarse: ETD3RK. Their findings (§4–6):

- **Parareal magnifies the mild instability.** Serial ERK4 is stable over the whole range of
  their parameter rectangle with growth rates below 1.01, yet Parareal with classical
  exponential integrators diverges on the nonlinear Schrödinger equation, and its linear
  stability region shrinks as the iteration count grows; repartitioned propagators are stable,
  so repartitioning is essential for Parareal even on time scales where serial integration does
  not need it (§4, §5.3, Fig. 5).
- **Stiffness must sit in $L$.** Even with repartitioning the iteration is stable only when the
  linear part carries most of the stiffness ($\lvert h\lambda_2\rvert\ll\lvert h\lambda_1\rvert$)
  (§5.3).
- **Only low-frequency modes converge.** A convergence bound on the partitioned Dahlquist
  equation predicts monotone convergence exactly for modes with $\lvert h\lambda\rvert$ below a
  computable width, and higher-order coarse propagators or more coarse steps widen it (§5.4–5.6,
  Remark 1).
- **Speedups.** Against serial ERK4 with the fine step: 10.4 measured (38.5 theoretical) on
  1D NLS with 2048 cores; 9.09, 10.15 and 11.71 times on the 2D Kadomtsev–Petviashvili equation
  (errors $2.7\times10^{-7}$, $1.3\times10^{-8}$, $1.8\times10^{-9}$, partly extrapolated from a
  shortened run); 24 times on the Vlasov–Poisson bump-on-tail problem (error
  $6.6\times10^{-8}$, three coarse steps per slice) (§4, §6.2–6.3; see
  [Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md) and
  [Vlasov–Poisson equation](/benchmarks/vlasov-poisson-equation.md)).

All their experiments use diagonal $L$, where the φ-functions are elementwise; nondiagonal $L$
is left to future work (§7). The Parareal iteration, its speedup model and its convergence
analysis are on the [Parareal](/methods/parareal.md) page.

## Multirate infinitesimal methods as exponential integrators

In a [multirate infinitesimal method](/methods/multirate-infinitesimal-methods.md) each
slow stage is reached by solving a modified fast problem whose forcing is a polynomial in
time built from slow stage values. If the fast part is linear and solved exactly, every
stage is an exponential-integrator stage. Chinomona & Reynolds (2021, §3, Eqs. 3.1–3.3)
use this to obtain the linear stability function of
[IMEX-MRI-GARK](/methods/imex-mri-gark.md) methods on
$y'=(\lambda^{\{\mathrm f\}}+\lambda^{\mathrm E}+\lambda^{\mathrm I})y$ (page-local
eigenvalues of the fast, slow-explicit and slow-implicit parts;
$z^{\{\cdot\}}=H\lambda^{\{\cdot\}}$ with macro step $H$). With page-local $\Delta c_i$ the
stage increments of the slow abscissae and $\omega^{(k)}_{ij}$, $\gamma^{(k)}_{ij}$ the
entries of the registry's explicit and implicit coupling matrices $\Omega^{(k)}$,
$\Gamma^{(k)}$ (the source writes $\omega^{\{k\}}_{ij}$, $\gamma^{\{k\}}_{ij}$), variation of constants gives,
in registry normalisation,

$$\begin{aligned}
Y_i&=e^{\Delta c_iz^{\{\mathrm f\}}}Y_{i-1}+z^{\mathrm E}\sum_{j<i}\eta_{ij}Y_j+z^{\mathrm I}\sum_{j\le i}\mu_{ij}Y_j,\\
\eta_{ij}&=\sum_k\omega^{(k)}_{ij}\,k!\,\phi_{k+1}\big(\Delta c_iz^{\{\mathrm f\}}\big),\qquad
\mu_{ij}=\sum_k\gamma^{(k)}_{ij}\,k!\,\phi_{k+1}\big(\Delta c_iz^{\{\mathrm f\}}\big)
\end{aligned}$$

(page-local $\eta_{ij},\mu_{ij}$; the source writes $\varphi_{k+1}$ without the $k!$). The
stability function $R(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})$ is the last component
of the solution of this lower-triangular linear system with $Y_1=1$ (Eq. 3.3), and
defines the joint stability region of
[multirate linear stability](/definitions/multirate-linear-stability.md).

## Exponential reformulation of stiff kinetic relaxation

For the space-homogeneous kinetic equation $\partial_tF=\varepsilon^{-1}Q(F)$ (page-local,
as on [BGK penalization](/methods/bgk-penalization.md): $F$ the distribution function, $Q$
the collision operator, $\mathcal M$ its local equilibrium, which is constant in time in the
homogeneous case, and $\beta>0$ a penalization constant), Dimarco & Pareschi (2011) rewrite
the equation exactly as

$$\partial_t\Big[(F-\mathcal M)e^{\beta t/\varepsilon}\Big]=\frac{Q(F)-\beta(\mathcal M-F)}{\varepsilon}\,e^{\beta t/\varepsilon},$$

as recalled by [Jin (2022)](/sources/jin-2022.md) (§5.2, Eq. 5.7). The factor
$e^{-\beta t/\varepsilon}$ "removes the stiffness and numerically forces the convergence
between $F$ and $\mathcal M$"; applying any explicit Runge–Kutta method to the transformed
variable gives schemes that are "not only of high order but also satisfy the AP property
automatically", and $\beta$ is chosen as the smallest value that preserves the positivity of
$F$ (p. 451). Li & Pareschi (2014) extend it to the inhomogeneous equation, with the
Maxwellian evolving inside the step through its moments (Eqs. 5.8–5.10), and claim
positivity, high-order accuracy and "strong AP properties" (p. 452). The penalization by
$\beta(\mathcal M-F)$ is the same device as in [BGK penalization](/methods/bgk-penalization.md);
see also [asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md) and
[positivity preservation](/properties/positivity-preservation.md). Hu & Shu (2019) give a
second-order AP and positivity-preserving exponential Runge–Kutta method for relaxation
systems (as recalled by Jin 2022, §6.1). Structurally this is an integrating-factor
([Lawson-type](/methods/lawson-methods.md)) transformation with the scalar linear part $-\beta/\varepsilon$ *(compiler
classification, not in the source)*.

## Magnus and commutator-free quasi-Magnus methods

For linear non-autonomous problems $y'=L(t)y$ the exact solution is
$y(t_n+h)=e^{\Upsilon(h)}y_n$, with $\Upsilon$ a series of iterated integrals of nested
commutators (the Magnus expansion). Truncating it and using two-point Gauss quadrature
$c_{1,2}=\tfrac12\mp\tfrac{\sqrt3}6$ gives the fourth-order Magnus integrator

$$y_{n+1}=\exp\Big(\tfrac h2(L_1+L_2)+\tfrac{\sqrt3}{12}h^2[L_2,L_1]\Big)y_n,\qquad L_j=L(t_n+c_jh)$$

([Blanes et al. 2024](/sources/blanes-2024.md), §6.3, Eqs. 6.32–6.33; page-local $L_j$ and
$\Upsilon$, the source's $\Omega$, renamed because $\Omega^{(k)}$ is the registry's MRI coupling
matrix used above). For the Schrödinger equation with a smooth time-dependent potential, Magnus
integrators keep their full order uniformly in the space discretization (as recalled from
Hochbruck & Lubich 2003). Their drawback is the cost of the commutators, acute in two and
three space dimensions. **Commutator-free quasi-Magnus (CFQM)** methods, "a different class
of exponential integrators", replace the single exponential by a product
$y_{n+1}=e^{hB_J}\cdots e^{hB_1}y_n$ of exponentials of linear combinations
$B_j=\sum_ka_{jk}L(t_n+c_kh)$ (page-local $B_j$, $a_{jk}$, $c_k$). Examples are the
exponential midpoint rule $y_{n+1}=e^{hL(t_n+h/2)}y_n$ (order 2, Eq. 6.34) and the
fourth-order method with $c_{1,2}=\tfrac12\mp\tfrac{\sqrt3}6$,
$a_{11}=a_{22}=\tfrac14+\tfrac{\sqrt3}6$, $a_{12}=a_{21}=\tfrac14-\tfrac{\sqrt3}6$,
$y_{n+1}=e^{hB_2}e^{hB_1}y_n$ (Eq. 6.35). CFQM methods are unconditionally stable with
full order under low regularity; schemes up to order 6 and 8 exist (§6.3, as recalled
from Blanes et al. 2017, 2018, 2021 and Alvermann & Fehske 2011).

**Error bounds for large $h\lVert L\rVert$** (Hochbruck & Ostermann 2010, §3.1, after
Hochbruck & Lubich 1999, 2003). They write the same Magnus expansion (Eq. (3.6)), the
exponential midpoint rule (Eq. (3.8)) and the fourth-order two-point Gauss method (Eq. (3.10)),
which agrees with the formula above. The Magnus series "is not at all useful for studying the
convergence of Magnus integrators in the case of large $h\lVert A(t)\rVert$" (their $A(t)$ is
$L(t)$ here), since it need
not converge there (as recalled from Moan & Niesen 2008), yet the integrators "work
extremely well" at such steps. For skew-Hermitian $L(t)$ with bounded derivatives the
exponential midpoint rule has error $\le Ch$, with $C$ depending only on the derivative
bounds and $T$, and a higher power of $h$ under the extra regularity conditions (3.11)–(3.12)
(Thm. 3.4). For
$L(t)=-i(D^2+V(t))$ with $D$ symmetric positive definite and the commutator bound
$\lVert[L(\tau),L(\tau')]v\rVert\le Kh\lVert Dv\rVert$ for $\lvert\tau-\tau'\rvert\le h$
(page-local $D$, $V$, $K$; Assumption 3.6), the exponential midpoint rule satisfies
$\lVert y_n-y(t_n)\rVert\le Ch^2t_n\max_t\lVert Dy(t)\rVert$ with $C$ independent of $n$,
$h$ and $D$ (Thm. 3.9), and $p$-th-order interpolatory Magnus integrators satisfy
$\le Ch^pt_n\max_t\lVert D^{p-1}y(t)\rVert$ for $h\lVert D\rVert\le c$ (Thm. 3.10). For the
linear Schrödinger equation on a torus, $D^2=-\Delta+I$, $\lVert Dv\rVert$ is the $H^1$
norm and the commutator bound holds uniformly for spectral discretizations (Ex. 3.7); see
[nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md). For
parabolic $y'=L(t)y+b(t)$ the Magnus integrator
$y_{n+1}=e^{hL(t_{n+1/2})}y_n+h\phi_1(hL(t_{n+1/2}))b(t_{n+1/2})$ is second order
(Eq. (2.84), as recalled from González, Ostermann & Thalhammer 2006; page-local $b$). For
singularly perturbed problems $y'=\varepsilon^{-1}L(t)y$ they recall adiabatic integrators,
which integrate in the eigenbasis of $L(t)$; the averaged adiabatic exponential midpoint rule
has error $\mathcal O(\min\{\varepsilon,h\})$ only (§3.1, Eq. (3.34)).

## Trigonometric (Gautschi-type) integrators for oscillatory second-order problems

For $\ddot q=-W^2q+N(q)$ with $W$ symmetric positive semidefinite and $\lVert W\rVert\gg1$
(page-local $q$, velocity $v=\dot q$, frequency matrix $W$; Hochbruck & Ostermann 2010,
§3.2, Eq. (3.36)), "Taylor series expansion of the exact solution is not a viable option"
(§1), and the exact propagator of the linear oscillator is used instead. With $\operatorname{sinc}\xi=\sin\xi/\xi$ the two-step class is

$$q_{n+1}-2\cos(hW)\,q_n+q_{n-1}=h^2\,\sigma(hW)\,N\big(\varpi(hW)q_n\big)\qquad\text{(Eq. (3.41))},$$

with an outer filter $\sigma$ and an inner filter $\varpi$ (page-local; the source's $\psi$,
$\phi$), and a one-step form (3.42) that also updates $v$. Named members (Ex. 3.12, Eq. (3.50)):

| method | inner filter $\varpi(\xi)$ | outer filter $\sigma(\xi)$ |
|---|---|---|
| Gautschi (1961) | $1$ | $\operatorname{sinc}^2(\xi/2)$ |
| Deuflhard (1979) | $1$ | $\operatorname{sinc}\xi$ |
| García-Archilla, Sanz-Serna & Skeel (1998) | $\operatorname{sinc}\xi$ | $\operatorname{sinc}^2\xi$ |
| Grimm & Hochbruck (2006) | $\operatorname{sinc}\xi$ | $\operatorname{sinc}^3\xi$ |
| Hochbruck & Lubich (1999), two-step | $\big(1+\tfrac13\operatorname{sinc}^2\tfrac\xi2\big)\operatorname{sinc}\xi$ | $\operatorname{sinc}^2(\xi/2)$ |

**Theorem 3.15** (after Grimm & Hochbruck 2006). If the solution has finite energy,
$\tfrac12\lVert v\rVert^2+\tfrac12\lVert Wq\rVert^2\le\mathcal E^2$ (page-local $\mathcal E$), and the filters
satisfy the boundedness and smallness conditions (3.45)–(3.48), the one-step method has
position error $\le Ch^2$; under (3.49) also velocity error $\le Ch$; the constants are
independent of $\lVert W\rVert$. The proof bounds sums of oscillatory defects by summation by
parts "as long as no resonances occur", and the filters remove the resonances. Gautschi's and
Deuflhard's methods "do not use an inner filter $\phi$, and thus suffer from resonances" (their $\phi$ is $\varpi$ here)
(Ex. 3.14). Symmetric one-step methods of the class are symplectic iff
$\sigma(\xi)=\operatorname{sinc}(\xi)\varpi(\xi)$; the long-time near energy conservation proved by
Hairer & Lubich (2000) for linear problems needs $\sigma=\operatorname{sinc}^2\varpi$, "which
cannot be satisfied by a symplectic method" (Remark 3.18; see
[symplecticity](/properties/symplecticity.md)).

**Impulse and multiple time stepping.** The impulse method (Grubmüller et al. 1991; Tuckerman,
Berne & Martyna 1992) is a Strang [splitting](/methods/operator-splitting.md) into fast and
slow forces: a half kick with the slow force, the fast oscillation over $h$, a half kick. For
linear fast forces it "is then precisely the scheme of Deuflhard (1979)", and it shows
resonances when eigenvalues of $hW$ are integer multiples of $\pi$ (Biesiadecki & Skeel 1993,
as recalled). The mollified impulse method of García-Archilla et al. (1998) replaces the slow
force by an averaged one and, for linear fast forces, is the one-step method with the
García-Archilla filters, so Theorem 3.15 covers it (§3.2, Eq. (3.52)).

## Exact linear flows inside splittings

[Operator splitting](/methods/operator-splitting.md) uses exact exponentials of a linear
part in another way: the split-step Fourier and time-splitting spectral methods solve the
free Schrödinger flow exactly in Fourier space (Jin 2022, §3.1; Blanes et al. 2024, §1.6),
and rotation–kick splittings integrate the quadratic part of a Hamiltonian exactly
(Blanes et al. 2024, §4.2, §5). Jin (2022, §3.3) shows that exact sub-flows are what lets
the time-splitting spectral method stay asymptotic-preserving in time for semiclassical
observables.

## Exact exponential map of linear structural dynamics

For linear second-order systems $M\ddot u+C\dot u+Ku=f(t)$ (page-local $u$, $C$, $K$,
$f$), [Song & Eisenträger (2022)](/sources/song-2022.md) (§2.1, Eqs. (12)–(21)) write the
state-space form $x'=\mathcal Ax+F$ in step-local time, with $x=[h\dot u;u]$ and
$\mathcal A$ containing the step (page-local; see
[Padé time integration](/methods/pade-time-integration.md)). If the load is a polynomial
of degree $p_{\mathrm f}$ in each step, expanded about the midpoint with coefficients
$\mathcal F_k$, the one-step map is exact:

$$x_{n+1}=e^{\mathcal A}x_n+\sum_{k=0}^{p_{\mathrm f}}\mathcal B_k\mathcal F_k,\qquad
\mathcal B_k=\int_0^1(\theta-\tfrac12)^ke^{(1-\theta)\mathcal A}\,d\theta,$$

with $\mathcal B_0=\mathcal A^{-1}(e^{\mathcal A}-I)$ and
$\mathcal B_k=\mathcal A^{-1}\big(k\mathcal B_{k-1}+(-\tfrac12)^k(e^{\mathcal A}-(-1)^kI)\big)$
(page-local $\mathcal B_k$, $\mathcal F_k$, $p_{\mathrm f}$). In registry normalisation
$\mathcal B_0=\phi_1(\mathcal A)$, and each $\mathcal B_k$ is a combination of
$\phi_1,\dots,\phi_{k+1}$ because the midpoint-centred monomials are combinations of
$\theta^j$ *(compiler check, not in the source)*. The authors trace the approach to the
precise integration method of Zhong and Williams and its successors (Fung, Wang and Au)
and to an exponential Runge–Kutta method of Luan (§2.1), as recalled. They do not
evaluate the exponential: with a consistent mass matrix $M^{-1}K$ and $e^{\mathcal A}$
are full, so they replace $e^{\mathcal A}$ by its diagonal Padé approximant, an implicit
rational scheme, rather than by a Taylor polynomial, which would give an explicit,
conditionally stable scheme (§2.1–2.2).

## Multirate exponential Runge–Kutta and Rosenbrock methods

The bridge also runs the other way. Luan et al. (2022, Lemma 2.2) show that an ExpRB stage
whose coefficients are combinations $\sum_k\alpha^{(k)}_{ij}\phi_k(c_ihJ_n)$ is the exact
value at $\tau=c_ih$ of the linear ODE $v'=J_nv+p_i(\tau)$, $v(0)=y_n$, whose forcing $p_i$
is a polynomial in $\tau$ built from the $D_j$ (page-local $v$, $\tau$, $p_i$,
$\alpha^{(k)}_{ij}$). Solving these ODEs with an inner integrator on a micro step, instead of
evaluating the φ-functions, gives the multirate exponential Rosenbrock (MERB) methods. Their
predecessors, the MERK methods, require a fixed linear fast operator. Both are treated at
[multirate exponential methods](/methods/multirate-exponential-methods.md).

## Preservation of linear invariants

Exponential integrators preserve every linear invariant and equilibrium of the original
system (Theorem 2 of Einkemmer & Ostermann 2015, as recalled by Deka & Einkemmer 2022,
§1, §3.1). For resistive MHD Deka & Einkemmer need a finite-difference Jacobian, and both the
Jacobian and the remainder $f(y)-J_ny$ satisfy the discrete solenoidal condition. A
polynomial approximation of a φ-function applied to such a vector therefore keeps it, so
$\nabla\cdot B=0$ holds without divergence cleaning. Their runs keep $\nabla\cdot B$ between
about $10^{-10}$ and $10^{-9}$ up to $t=100$ for EXPRB43 and EPIRK5P1 (Fig. 12). They assert,
without proof, that the finite-difference Jacobian preserves the constraint.

## Application: matrix-free integration of resistive MHD

Deka & Einkemmer (2022) run EXPRB43 and EPIRK5P1 matrix-free on 2.5-D resistive MHD,
with Leja interpolation, the cost-based step-size controller and wall-clock comparisons;
the hardware is not stated. The results (§4.3, Figs. 7–8, §5.2–5.3):

- **Against explicit pairs.** EXPRB43 with Leja beats the explicit embedded pairs RK43 and
  DOPRI54 by factors 3.6 and 2.4 against error (3.7 and 4.8 against tolerance) in the
  diffusion-dominated Kelvin–Helmholtz case I. In case II the factors are 6.3 and 8.4
  against error (9.8 and 13 against tolerance). RK43 fails to converge at tolerance
  $10^{-2}$, and DOPRI54 at $10^{-2}$ and $10^{-3}$.
- **Against BDF.** In the low-diffusion cases III and IV, EXPRB43 with Leja beats
  [CVODE](/software/cvode.md)'s variable-order BDF by up to a factor 3 and 2.3, and is "more
  stable in terms of the error incurred as a function of the computational cost".

The Leja-versus-Krylov comparison is at [evaluating φ-functions](/methods/phi-function-evaluation.md),
the controller at [step-size control](/methods/step-size-control.md), and the test at
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md). The authors state
without evidence that exponential integrators "can take large time steps (often
significantly larger than even fully implicit methods)" (§1).

## Qualifications

- Jin's claim that explicit Runge–Kutta methods on the exponential reformulation are "of
  high order" refers to order at fixed $\varepsilon$; uniform-in-$\varepsilon$ high order is
  not claimed in the source (Jin 2022, §5.2).
- The function $P$ in the inhomogeneous reformulation (Jin 2022, Eq. 5.8) is used without
  definition in the source (printed slip).
- **Printed slips in Luan (2021), §5 implementation listings and p. 15.** The formulas
  above are the consistent ones; the slips are recorded here only.
  - For expRK4s5 the $\phi_2$ vector of the update is printed with coefficient 5 on $D_5$
    ("5d5") where his Eq. (2.7) has 4.
  - For expRK4s6 the $\phi_3$ entry of the call for $\{Y_5,Y_6\}$ lacks the factor 2 of
    Eq. (4.10c).
  - For expRK5s10 the $\phi_3$ bracket of stages 8–10 is printed with a plus sign on the
    $D_5$ term and minus signs on $D_6$, $D_7$ (p. 15 and §5). Eq. (4.20) requires a minus
    sign on all three, which is the $\Theta_{j;k,l}$ form above. The
    update's $\phi_3$ vector is printed without its minus sign, and one call lists its
    scalings in non-increasing order.
  - The expRK5s8 listing drops the prefactors $\tfrac12$, $\tfrac18$, $\tfrac12$,
    $\tfrac1{25}$ and $\tfrac1{125}$ of its Eq. (2.7).
- **Printed slips in Luan et al. (2022).** Eq. (2.62) gives the exprb42 weight as
  $\tfrac{16}9\phi_3$. The first Rosenbrock condition, and the forcing of their own
  Eq. (2.63), require $\tfrac{32}9$. Eq. (2.64) prints $b_3$ of pexprb54s4 with $c_4\phi_3$
  for $2c_4\phi_3$; their forcing (2.65) is consistent with the factor 2.
- **Printed slips in Deka & Einkemmer (2022).** The remainder is printed $f(u)-\mathcal J(u)$
  for $f(y)-J_ny$ (§2.1). The exact solution of the linear problem is printed with the
  operator order reversed (§2).
- Luan (2021, §2.2) calls expRK4s5 and expRK5s8 "the only existing" fourth- and fifth-order
  stiffly accurate ExpRK methods. That holds within the format above. Exponential methods
  of order 4 and 5 of other types exist: the Rosenbrock and EPIRK schemes on this page.
- Dallerit & Tokman's claim that their multistep methods coincide with Hochbruck–Ostermann's
  exponential Adams methods is asserted, not shown (§6.2). Hochbruck & Ostermann (2010) define
  exponential Adams methods (2.69) with a fixed linear part and the linearized two-step method
  (2.72) with the per-step Jacobian; SREXP_MS3, which uses the per-step Jacobian, coincides with
  the latter (compiler check in the multistep section above).
- Hochbruck & Ostermann (2010) give no numerical experiments; their order statements for
  ETD4RK, Krogstad's and the Strehmel–Weiner scheme are worst-case statements derived from the
  stiff order conditions (Ex. 2.19).
- Permyakova & Goldobin (2025) state only classical error terms for ETD2RK–ETD4RK and do not
  discuss stiff order; against the stiff conditions, ETD4RK satisfies the order-2 hypotheses of
  Luan's theorem but not those of order 3 *(compiler check on the
  [result page](/results/exponential-runge-kutta-stiff-order-conditions.md))*. Their error
  curves carry no slopes, so they neither confirm nor refute order 4; they make no stiff-order
  claim.
- Permyakova & Goldobin's gains are measured against explicit schemes at their stability
  limits, not against implicit, IMEX or Krylov-based exponential integrators; storing dense
  $N\times N$ matrices costs $O(N^2)$ memory, and the advantage over Krylov and contour-integral
  evaluation is argued, not measured (§2, §4).
- **Printed slips in Buvoli & Minion (2024), arXiv v2.** Eq. (9) defines the φ-functions
  without the factor $1/(j-1)!$ and with $s^j$ for $s^{j-1}$, so that as printed
  $\varphi_1(0)=\tfrac12$, which contradicts their exponential Euler (Eq. 10) and their own
  tableaux; the tableaux are the consistent statement. Eq. (11) writes $e^{c_jhL}$ for
  $e^{c_ihL}$, and Eqs. (11)–(12) omit the factor $h$ and write $N(c_j,Y_j)$ for
  $N(t_n+c_jh,Y_j)$. Eq. (13) drops the $y$ in $\hat N=N-\epsilon Dy$, and Eq. (25) writes the
  repartitioned stability function with signs opposite to those of their §5.1 table, whose
  signs are the ones above. Table 4a swaps the fine (ERK4) and coarse (ERK3) integrators of the
  KP runs.
- Buvoli & Minion's speedups are against serial ERK4 with the fine step, not against the best
  serial method at equal error, and the KP speedups are extrapolated from a shortened parallel
  run (§6.1–6.2).

# Citations

- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §1 (ExpRK, ExpRB, EPIRK as method families), §3, Eqs. 3.1–3.3 (exact fast solve, φ-functions, stability function; unnormalised convention).
- [Jin (2022)](/sources/jin-2022.md) — §5.2, Eqs. 5.6–5.10 (exponential reformulation of kinetic relaxation, Dimarco & Pareschi 2011, Li & Pareschi 2014), §6.1 (Hu & Shu 2019), §3.1–3.3 (exact sub-flows in time splitting).
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.3, Eqs. 6.32–6.35 (Magnus and CFQM integrators), §1.6, §4.2, §5 (exact linear flows in splittings).
- [Song & Eisenträger (2022)](/sources/song-2022.md) — §2.1, Eqs. (12)–(21) (exact exponential map of linear structural dynamics with polynomial load; precise integration method as recalled), §2.2 (rational instead of polynomial approximation).
- [Luan (2021)](/sources/luan-2021.md) — §1 (classical vs stiff, terminology), §2.1–2.2 Eqs. 1.2–1.4, 2.4–2.7 (format, cost model, expRK2s2–expRK5s8), Remark 2.1, §4.1–4.2 Eqs. 4.4–4.26 (expRK4s6, expRK5s10), Remarks 4.1–4.2, §5–6 (implementation, tests, Figs. 6.1–6.4); arXiv v1.
- [Luan et al. (2022)](/sources/luan-2022.md) — §2.1 Eqs. 2.1–2.7, Remark 2.1 (ExpRB format, order ≥ 2), Lemma 2.2, §2.4 Eqs. 2.59–2.66 (exprb32, exprb42, pexprb54s4, pexprb65s7 generalized); arXiv v2.
- [Deka & Einkemmer (2022)](/sources/deka-2022.md) — §1, §2–2.2 Eqs. 3–8, Table 1 (exponential Euler, Rosenbrock–Euler, EXPRB43, EXPRB54s4, EPIRK5P1), §3.1 Eq. 11, Fig. 12 (linear invariants), §4.3 Figs. 7–8, §5.2–5.3 Fig. 13 (performance, evaluation counts); author manuscript.
- [Caliari et al. (2024)](/sources/caliari-2024.md) — §2 Thms. 2.1, 2.4, 2.5, Table 1, §3 Eq. 11 (partial linear operator), §5–6, Appendix (schemes); arXiv v2.
- [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) — §1, §3 (order notions), §5.3 (single projection), §6.1–6.3 Eqs. 40–41, Tables 1–3 (SREXP_RK, MS, MV), §7 Figs. 1–4.
- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — §3.1–3.2 Eqs. 7–15, App. A (ERK1–ERK4 tableaux, φ convention, repartitioning), §4 (NLS), §5.1–5.7 (partitioned Dahlquist analysis, Fig. 5, Fig. 10), §6.2–6.3 (KP, Vlasov–Poisson), §7; arXiv v2.
- [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md) — §1–2 Eqs. 1–12 (ETD2RK–ETD4RK, matrix form), §3.1–3.3 (Figs. 3–8, Table 1), §4, App. A; arXiv v2.
- [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) — §1 Eqs. (1.1)–(1.6) (idea, two problem classes, stiff order, rational approximations); §2.1–2.2 Assumption 2.2, Exs. 2.3, 2.5–2.6, Eqs. (2.9)–(2.18), Thm. 2.7, Cor. 2.8 (φ-functions, exponential quadrature); §2.3 Eqs. (2.20)–(2.25), Thm. 2.14, Exs. 2.18–2.19, Eqs. (2.39)–(2.43), p. 229 (ExpRK format, simplifying assumptions, named tableaux); §2.4 Eqs. (2.44)–(2.53), Thm. 2.22, Exs. 2.23–2.25 (exponential Rosenbrock, exprb32, exprb43, exp4); §2.5–2.7 Eqs. (2.69)–(2.78), Thms. 2.27, 2.29, 2.31 (exponential Adams, linearized multistep, general linear methods); §2.8 Eq. (2.84), §3.1 Eqs. (3.6)–(3.10), (3.34), Thms. 3.4, 3.9, 3.10, Ex. 3.7 (Magnus, adiabatic); §3.2 Eqs. (3.36)–(3.52), Exs. 3.12, 3.14, Thm. 3.15, Remark 3.18 (trigonometric, impulse methods); §6 (history); version of record.
