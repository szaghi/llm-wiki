---
type: Method
title: "Lawson (integrating-factor) methods"
description: "Lawson methods apply an explicit Runge–Kutta method to the equation transformed by the integrating factor of the stiff linear part, so they need only matrix exponentials; the page gives the first- and second-order schemes, Caliari et al.'s stabilized variants and stability bounds for a partial linear operator, and the integrating-factor form of stiff kinetic relaxation."
status: established
aliases: [Lawson scheme, integrating factor method, integrating-factor Runge–Kutta, IFRK, Lawson–Euler, stabilized Lawson, generalized Runge–Kutta of Lawson, generalized Lawson method, generalized integrating factor method]
tags: [exponential, explicit, stiff, stability, splitting]
timestamp: 2026-10-29T18:13:00Z
---

# Lawson (integrating-factor) methods

A **Lawson method** advances the semilinear problem $y'=Ly+N(t,y)$ ($N$ the non-stiff
remainder, page-local as on [exponential integrators](/methods/exponential-integrators.md))
in three moves. It changes variables with the integrating factor of $L$, applies an explicit
Runge–Kutta method to the transformed equation, and transforms back. With
$y(t_n+\tau)=e^{\tau L}w(\tau)$ the problem becomes
$w'(\tau)=e^{-\tau L}N\big(t_n+\tau,y(t_n+\tau)\big)$, which has no stiff linear term
([Hochbruck & Ostermann 2010](/sources/hochbruck-2010.md), §2.7, Eqs. (2.79)–(2.82) with
$k=0$, in their sign convention $L=-A$). The factor $e^{-\tau L}$ "is not defined for
semigroups", but it is only formal and disappears from the final scheme, provided the nodes
satisfy $c_i\in[0,1]$ (§2.7). The resulting schemes involve the matrix exponential only,
with no φ-functions ([Caliari et al. 2024](/sources/caliari-2024.md), §2, after Lawson 1967).
Hochbruck & Ostermann (§6) credit Lawson (1967) and Ehle & Lawson (1975), who used rational
approximations for higher-order Runge–Kutta bases, with the first exponential Runge–Kutta
methods. That is their
practical advantage: an exponential can be computed in ways that do not extend to
$\phi_k$, for instance as a product of small one-dimensional exponentials when $L$ is a
Kronecker sum (§1, §5.2; see [evaluating φ-functions](/methods/phi-function-evaluation.md)).

## Schemes

With $f=Ly+N$ the full right-hand side, Caliari et al. (2024, §2, Appendix) use these
schemes, written in the registry:

| scheme | stages and update | order |
|---|---|---|
| Lawson–Euler (le) | $y_{n+1}=e^{hL}\big(y_n+hN(t_n,y_n)\big)$ | 1 |
| Lawson2a (l2a), midpoint-based | $Y=e^{hL/2}\big(y_n+\tfrac h2N(t_n,y_n)\big)$, $y_{n+1}=e^{hL}y_n+h\,e^{hL/2}N(t_n+\tfrac h2,Y)$ | 2 |
| Lawson2b (l2b), Heun-based | $Y=e^{hL}\big(y_n+hN(t_n,y_n)\big)$, $y_{n+1}=e^{hL}\big(y_n+\tfrac h2N(t_n,y_n)\big)+\tfrac h2N(t_n+h,Y)$ | 2 |
| stabilized Lawson–Euler (sle), new | $y_{n+1}=y_n+h\,e^{hL}f(t_n,y_n)$ | 1 |
| stabilized Lawson2 (sl2), new | $Y=y_n+c_2h\,e^{c_2hL}f(t_n,y_n)$, $y_{n+1}=y_n+h\,e^{hL/2}f(t_n,y_n)+\frac{h}{2c_2}e^{hL}\big(N(t_n+c_2h,Y)-N(t_n,y_n)\big)$ | 2 |

The sl2 node is $0<c_2\le1$, and $c_2=0.327$ in use. The source calls it $\alpha$.

**Lawson–Euler is a splitting.** For the heat equation split as
$y'=\vartheta\Delta y+(1-\vartheta)\Delta y$ with $L=\vartheta\Delta$ (page-local $\vartheta\in[0,1]$,
the source's $\lambda$), Lawson–Euler equals Lie
[splitting](/methods/operator-splitting.md) with the second sub-flow replaced by explicit
Euler: $e^{h\vartheta\Delta}e^{h(1-\vartheta)\Delta}y_n\approx e^{h\vartheta\Delta}\big(y_n+h(1-\vartheta)\Delta y_n\big)$
(Caliari et al. 2024, §2).

The stabilized schemes are not Lawson methods in the strict sense, since they apply the
exponential to $f$ rather than transform the variable. They are **not exact for linear
problems** ($N=0$), and they are not [A-stable](/properties/a-stability.md). Their
stability regions do contain the whole negative real axis (Remark 2.2, Fig. 1).

## Generalized Lawson methods and their stiff order

Hochbruck & Ostermann (2010, §2.7, after Krogstad 2005, who called them "(generalized)
integrated factor methods") subtract from $N$, before transforming, the polynomial that
interpolates it at the $k$ past points $t_{n-k+1},\dots,t_n$, and treat that polynomial
exactly with the exponential Adams weights of
[exponential integrators](/methods/exponential-integrators.md). For $k=0$ this is the Lawson
method above. With a Runge–Kutta base the result is an exponential general linear method:
stages $Y_i=e^{c_ihL}y_n+h\sum_ja_{ij}(hL)N_j+h\,w_{i1}(hL)N(t_{n-1},y_{n-1})$ and update
$y_{n+1}=e^{hL}y_n+h\sum_ib_i(hL)N_i+h\,v_1(hL)N(t_{n-1},y_{n-1})$, with
$N_j=N(t_n+c_jh,Y_j)$ and $\phi_{k,j}=\phi_k(c_jhL)$ (page-local $w_{i1}$, $v_1$, $N_j$). Their
examples, all on Runge's (midpoint) method $c=(0,\tfrac12)$ unless stated (Exs. 2.32–2.34):

| $k$ | coefficients | order they state |
|---|---|---|
| 0 (Lawson 1967) | $a_{21}=\tfrac12e^{hL/2}$; $b=(0,\ e^{hL/2})$ | "first-order accurate by Theorem 2.17" |
| 1 | $a_{21}=\tfrac12\phi_{1,2}$; $b=(\phi_1-e^{hL/2},\ e^{hL/2})$ | 2, by Thm. 2.17 |
| 2 | $a_{21}=\tfrac12(\phi_{1,2}+\phi_{2,2})$, $w_{21}=-\tfrac12\phi_{2,2}$; $b=(\phi_1+\phi_2-\tfrac32e^{hL/2},\ e^{hL/2})$, $v_1=-\phi_2+\tfrac12e^{hL/2}$ | 2, by Thm. 2.31 |
| 2, classical RK4 base (Krogstad 2005), $c=(0,\tfrac12,\tfrac12,1)$ | $a_{21}=\tfrac12\phi_{1,2}+\tfrac14\phi_{2,2}$, $w_{21}=-\tfrac14\phi_{2,2}$; $a_{31}=\tfrac12\phi_{1,2}+\tfrac14\phi_{2,2}-\tfrac34I$, $a_{32}=\tfrac12I$, $w_{31}=-\tfrac14\phi_{2,2}+\tfrac14I$; $a_{41}=\phi_1+\phi_2-\tfrac32e^{hL/2}$, $a_{43}=e^{hL/2}$, $w_{41}=-\phi_2+\tfrac12e^{hL/2}$; $b=(\phi_1+\phi_2-e^{hL/2}-\tfrac13I,\ \tfrac13e^{hL/2},\ \tfrac13e^{hL/2},\ \tfrac16I)$, $v_1=-\phi_2+\tfrac13e^{hL/2}+\tfrac16I$ | 3, by Thm. 2.31 |

The $k=0$ row is Lawson2a of the table above: $Y=e^{hL/2}\big(y_n+\tfrac h2N(t_n,y_n)\big)$,
$y_{n+1}=e^{hL}y_n+h\,e^{hL/2}N(t_n+\tfrac h2,Y)$ *(compiler check, not in the sources: their tableau with $L=-A$)*.
The orders in the last column are stiff orders in the sense of
[stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md), for
semilinear parabolic problems; Krogstad's RK4-based scheme satisfies the stage and quadrature
conditions for $m=1,2$ and the weakened quadrature condition for $p=3$ (p. 243).

## Linear stability with a partial linear operator

Caliari et al. (2024, §2) put only a fraction $\vartheta$ of the diffusion in $L$ and treat
the rest explicitly. On $y'=\Delta y$ with periodic boundary conditions, a Fourier mode
$k$ has $z=-hk^2\in(-\infty,0]$, and each scheme has a two-argument amplification factor
$R(z;\vartheta)$ (the source writes $\Phi(z,\lambda)$). The scheme is called **unconditionally
stable** if $\lvert R(z;\vartheta)\rvert\le1$ on the whole negative real axis. The
amplification factors are:

- le: $R=e^{\vartheta z}\big(1+(1-\vartheta)z\big)$;
- l2a: $R=e^{\vartheta z}\big(1+w+\tfrac12w^2\big)$, with $w=(1-\vartheta)z$ page-local;
- l2b: the source prints $e^{\vartheta z}\big(1+\tfrac z2(1-\vartheta)+\tfrac z2(1-\vartheta)(1+z(1-\vartheta))\big)$,
  which expands to the same function as l2a;
- sle: $R=1+z\,e^{\vartheta z}$;
- sl2: $R=1+z\,e^{\vartheta z/2}+\tfrac{z^2}2(1-\vartheta)\,e^{(1+c_2)\vartheta z}$.

In general a Lawson method built on an explicit method with stability polynomial $P$ has
$R(z;\vartheta)=e^{\vartheta z}P((1-\vartheta)z)$ *(compiler check, consistent with the le, l2a
and l2b formulas above; the stabilized schemes are not of this form)*. The lower bounds on $\vartheta$ for unconditional stability (Thms. 2.1–2.7, Table 1;
[stability function](/definitions/stability-function.md)) are:

| scheme | order | bound on $\vartheta$ |
|---|---|---|
| IMEX backward–forward Euler | 1 | $1/2$ (Wang–Zhang–Wang–Shu, as recalled) |
| IMEX imex2 | 2 | $1/2$ (as recalled) |
| exponential Euler | 1 | $1/2$ |
| ExpRK2 with $\phi_2$, $c_2=1$ | 2 | $1/(1+c_2)=1/2$ |
| ExpRK2 with $\phi_1$ only, $c_2=1$ | 2 | $1/(1+2c_2)=1/3$ |
| Lawson2a, Lawson2b | 2 | $0.301$ |
| Lawson–Euler | 1 | $0.218$ |
| stabilized Lawson–Euler | 1 | $1/(2e)\approx0.184$ |
| stabilized Lawson2, $c_2=0.327$ | 2 | $0.183$ |

Lawson schemes therefore stay stable with a smaller implicit fraction than the
exponential Runge–Kutta schemes, and these with a smaller one than the two IMEX schemes. The
stabilized variants go furthest, and the node $c_2$ of sl2 is chosen to minimize its bound
(Thm. 2.7). Some bounds are proved in closed form: for le, the condition is
$1-1/\vartheta+e^{1/(1-\vartheta)}\ge0$, evaluated numerically, and for sle, $1/(2e)$. The
l2a/l2b and sl2 bounds are numerical. The IMEX comparison is the exponential counterpart of
the [explicit–implicit–null method](/methods/explicit-implicit-null-method.md), which adds
and subtracts a constant-coefficient operator.

**Sharpness and choice of $\vartheta$.** On 1D variable-coefficient diffusion
$\partial_ty=a(x)\partial_{xx}y$ with $a=1+10\sin^2x$ (page-local $a$), the bounds are
sharp. At $\vartheta=1/3$ exponential Euler and ExpRK2 with $\phi_2$ blow up, and at
$\vartheta=0.17$ every scheme loses unconditional stability (§4.1, Figs. 2–3). On a nonlinear
diffusion–reaction problem every method grows more accurate as $\vartheta$ decreases, and sle
and sl2 are the most accurate first- and second-order methods (§4.2, Fig. 4). The most
accurate stable $\vartheta$ is not always the smallest one. The authors therefore choose
$\vartheta$ by a parameter scan on a coarse grid. Their selections are le 0.22, sle 0.23,
l2a 0.53 and sl2 0.57 in 2D (Table 2). In 3D they are le 0.36, sle 0.27, l2a 0.62 and
sl2 0.53 at advection speed $-0.01$, and 0.60, 0.50, 0.50 and 0.57 at speed $-1$ (§3, §5,
Table 3).

## Performance

Caliari et al. (2024, §5) take a constant-coefficient $L$: $\vartheta$ times the maximal
diffusion, plus a mean advection. Its exponential is then evaluated pointwise in Fourier
space (2D, periodic) or by μ-mode products of small exponentials (3D, finite differences,
mixed Dirichlet–Neumann). The comparison is against the same integrators applied to the
full variable-coefficient operator with the Krylov code kiops or with BiCGStab. Results, in
MATLAB on one Intel i7-10750H:

- in 3D at advection speed $-0.01$, μ-mode Lawson–Euler and stabilized Lawson–Euler beat
  their original-formulation counterparts in error and wall-clock time, and Lawson2a is the
  best second-order method "with a considerable advantage" (Fig. 8);
- at speed $-1$ the stabilized schemes keep or lower their errors in the reformulation,
  while le and l2a lose accuracy but stay fastest (Fig. 9);
- overall the gain is "up to a factor of roughly 15 in the three dimensional case" (§6).

## Integrating factor for stiff kinetic relaxation

For the space-homogeneous kinetic equation $\partial_tF=\varepsilon^{-1}Q(F)$, the
reformulation of Dimarco & Pareschi (2011) multiplies $F-\mathcal M$ by $e^{\beta t/\varepsilon}$
and applies an explicit Runge–Kutta method to the transformed variable. As recalled by
[Jin (2022)](/sources/jin-2022.md) (§5.2, Eq. 5.7), the resulting schemes are high order,
asymptotic-preserving and, for suitable $\beta$, positivity preserving. Structurally this
is an integrating-factor (Lawson-type) method with the scalar linear part $-\beta/\varepsilon$
*(compiler classification, not in the source)*. The symbols and the inhomogeneous extension
are on [exponential integrators](/methods/exponential-integrators.md); see also
[asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md).

## Qualifications

- "Unconditional stability" in Caliari et al. (2024) means stability on the negative real
  axis only, which is weaker than A-stability: sle and sl2 are explicitly not A-stable. Their
  Fig. 1 calls the stability regions "A-stability regions".
- The analysis is per Fourier mode for the constant-coefficient heat equation, where $L$ and
  the explicit part commute. The variable-coefficient tests support it numerically, but no
  proof covers non-commuting parts.
- The claim that exponential and Lawson schemes have better stability than "similarly
  constructed" IMEX schemes rests on two IMEX schemes, both with bound $1/2$.
- **Order of Lawson2a.** Caliari et al. (2024, Appendix) list Lawson2a as a second-order
  scheme; Hochbruck & Ostermann (2010, Ex. 2.32) call the same scheme "first-order accurate by
  Theorem 2.17", and every order in their survey is a stiff order for the problem class at hand,
  here semilinear parabolic problems (§1, p. 212). The Lawson tableau has $\sum_jb_j=e^{hL/2}$, not $\phi_1(hL)$, so it does not
  satisfy the simplifying assumptions (2.23) under which their §2.3, including Theorem 2.17
  (stated for $2\le p\le4$), is formulated *(compiler check, not in the sources)*.
- l2a and l2b have identical amplification factors, so their equal bound is no coincidence
  *(compiler check)*. The sl2 bound 0.183 is rounded up from about 0.1820 *(compiler
  check)*. Their Fig. 4 labels the second-order ExpRK2 with $\phi_1$ "ERK1P1" (printed slip).

# Citations

- [Caliari et al. (2024)](/sources/caliari-2024.md) — §1–2 (Lawson schemes, Lie-splitting interpretation, Thms. 2.1–2.7, Remarks 2.1–2.2, Table 1, Fig. 1), §3 (choice of $\vartheta$), §4.1–4.2 (Figs. 2–4), §5.1–5.2 (Tables 2–3, Figs. 6–9), §6, Appendix; arXiv v2.
- [Jin (2022)](/sources/jin-2022.md) — §5.2, Eq. 5.7 (exponential reformulation of kinetic relaxation, Dimarco & Pareschi 2011, as recalled).
- [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) — §2.7 Eqs. (2.75)–(2.82), Exs. 2.32–2.34 (Lawson and generalized Lawson methods, tableaux, stiff orders), §6 (history); version of record.
