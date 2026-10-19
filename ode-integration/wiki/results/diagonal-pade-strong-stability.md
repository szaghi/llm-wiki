---
type: Result
title: "Unconditional strong stability of diagonal Padé schemes and its energy law"
description: "Sun, Wei and Wu prove that every diagonal $(m,m)$ Padé approximation, the stability function of the $m$-stage Gauss method, obeys on linear seminegative problems an exact energy law that truncates the continuous one with the same weights, giving unconditional strong stability and energy-dissipation error $O(h^{2m})$."
status: established
aliases: [unified energy law for diagonal Padé approximations, energy law of Gauss methods on linear problems, Sun–Wei–Wu theorem]
tags: [stability, strong-stability, implicit, structure-preserving, runge-kutta]
timestamp: 2026-10-19T12:00:00Z
---

# Unconditional strong stability of diagonal Padé schemes and its energy law

Consider $y'=Ly$ with $L$ bounded, seminegative ($\langle Lv,v\rangle\le0$) and
possibly non-normal on a real Hilbert space, the dissipation semi-norm $\lvert
v\rvert_L^2=-2\langle Lv,v\rangle$, and the $(m,m)$ diagonal Padé approximation of
$e^z$ as one-step map $y_{n+1}=D(hL)^{-1}N(hL)y_n$ (page-local: $m$ the degree, $N$ and
$D$ numerator and denominator). Its coefficients are

$$N(z)=\sum_{i=0}^m\theta_iz^i,\quad D(z)=\sum_{i=0}^m(-1)^i\theta_iz^i,\qquad \theta_i=\frac{m!}{(2m)!}\,\frac{(2m-i)!}{i!\,(m-i)!}$$

([Sun et al. 2022](/sources/sun-2022.md), Eq. (5.1)). These are the stability
functions of the $m$-stage Gauss collocation methods, of order $2m$ (Sun et al. 2022,
§1, citing Hairer–Wanner II, Table 5.13; see
[fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)).

## Statement

Let $d_k=\frac{(k!)^2}{(2k)!\,(2k+1)!}$ (page-local). In the notation of the
[energy method](/methods/runge-kutta-energy-method.md), for the diagonal Padé
approximation the diagonal coefficients all vanish, $\eta_k=0$, and

**Theorem 5.1 (Sun et al. 2022).** For every $m\in\mathbb Z^+$ the quadratic-form
matrix $\Upsilon\in\mathbb R^{m\times m}$ is negative **definite**, with the explicit
factorization $\Upsilon=-U^\top\mathrm{diag}(d_0,\dots,d_{m-1})\,U$, $U=(u_{ij})$ upper
triangular,

$$u_{ij}=\frac{m!}{(2m)!}\,\frac{(2i+1)!}{i!\,(i+j+1)!}\,\frac{(2m+i-j)!}{(m-1-j)!}\,\frac{\bigl(m-1-\frac{i+j}2\bigr)!\,\bigl(\frac{i+j}2\bigr)!}{\bigl(m-\frac{j-i}2\bigr)!\,\bigl(\frac{j-i}2\bigr)!}\quad(i\le j,\ i\equiv j\ \mathrm{mod}\ 2),$$

and $u_{ij}=0$ otherwise.

**Theorem 5.2 (Sun et al. 2022), unified energy law.**

$$\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2=-\sum_{k=0}^{m-1}d_k\,h^{2k+1}\,\bigl\lvert L^ky^{(k)}\bigr\rvert_L^2,\qquad y^{(k)}=\sum_{j=k}^{m-1}u_{kj}(hL)^{j-k}D(hL)^{-1}y_n.$$

Hence every diagonal Padé scheme is **unconditionally strongly stable**,
$\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for all $h\ge0$, for general linear
seminegative systems, normal or not (Sun et al. 2022, §5.2, Eqs. (5.6)–(5.7)). The
operator form is
$R(hL)^\top R(hL)-I=\sum_{k=0}^{m-1}d_kh^{2k+1}U_k^\top(L^\top+L)U_k\le0$ (Remark 5.7,
Eq. (5.9)).

The cases $m=1$ (implicit midpoint and Crank–Nicolson, law $-h\lvert
w_n\rvert_L^2$ with $w_n=(I-\frac h2L)^{-1}y_n$) are the first instance (Ex. 4.2).

## The discrete law truncates the continuous one

The exact flow satisfies
$\lVert y(t_n+h)\rVert^2-\lVert y(t_n)\rVert^2=-\sum_{k\ge0}d_kh^{2k+1}\lvert
L^k\hat y^{(k)}\rvert_L^2$ with the **same** weights $d_k$ (Sun et al. 2022, Thm. 2.1;
see the [energy method](/methods/runge-kutta-energy-method.md)). Moreover, when the
continuous vectors $\hat y^{(k)}$ are re-expanded in $D(hL)^{-1}y(t_n)$, their
coefficients coincide with the discrete $u_{kj}$ for $k\le j\le m-1$ (Thm. 5.4), and
$y^{(k)}=\sum_{j=k}^{m-1}\hat u_{kj}(hL)^{j-k}D_j(hL)D(hL)^{-1}y_n$ with $D_j$ the
truncation of $D$ to degree $m-1-j$ (Thm. 5.5). The diagonal Padé law is thus a
truncation of the continuous law. Consequence (Remark 5.6): the energy-dissipation
error is $O(h^{2m+1})$ per step and, for fixed $T=nh$,
$\Delta E:=(\lVert y(t_n)\rVert^2-\lVert y(t_0)\rVert^2)-(\lVert y_n\rVert^2-\lVert
y_0\rVert^2)=O(h^{2m})$, the order of the scheme. No explicit remainder bound is
written.

## Proof structure

The entries of $F(m):=\Upsilon+U^\top\mathrm{diag}(d_k)U$ are rewritten as rational
functions of a continuous parameter replacing $m$; they are shown to vanish on the
uncountable set of reals $x$ with $2x\notin\mathbb Z$, hence identically (Sun et al.
2022, §5.3–5.5, Observations 5.8–5.9, Prop. 5.10). The tools are Pochhammer
identities, telescoping sequences, and a combinatorial identity (Lemma 5.3) proved by
Watson's $_3F_2$ summation formula (App. D).

## Numerical confirmation

On the non-normal matrix $L=-\begin{pmatrix}1&2&2\\0&1&2\\0&0&1\end{pmatrix}$ with
$y(0)=(0.9134,0.2785,0.5469)^\top$, $t=8$ and $h\in\{1.6,0.8,0.4,0.2\}$, the $(3,3)$ and
$(4,4)$ schemes converge at orders $\approx6$ and $\approx8$ both in the $\ell^2$ error
and in $\Delta E$ (e.g. $m=4$: $\Delta E$ from $1.07\times10^{-9}$ to
$6.36\times10^{-17}$), and the per-step dissipation $\lVert y_n\rVert^2-\lVert
y_{n+1}\rVert^2$ is positive and matches the law (Sun et al. 2022, Ex. 6.1, Table 1,
Fig. 1a). The $(2,2)$ scheme runs at $h=0.1$ for P1-DG advection and P0-LDG dispersion
($\psi_t+\psi_{xxx}=0$) with $\Delta x=0.05$, where an explicit method would need
$h\le C\Delta x^3$ in the dispersive case (Exs. 6.2–6.3, Fig. 1b–c).

For skew $L$ ($L^\top=-L$) the right-hand side vanishes and the norm is conserved
exactly *(compiler check: immediate from Thm. 5.2)*. This is what Farrell, Kirby &
Marchena-Menéndez observe for Gauss–Legendre with one and two stages on an
energy-conserving mixed wave semi-discretization, $E(10)/E(0)=1$ at $h=0.1,0.5,1.0$,
while Radau IIA and Lobatto IIIC damp it, at the largest steps to ratios as small as $10^{-20}$
([Farrell et al. 2021](/sources/farrell-2021.md), §4.3, Table 1). The non-Padé
Qin–Zhang DIRK has the same conservative behaviour (Farrell et al. 2021, §4.3), as its
own energy law predicts (Sun et al. 2022, Ex. 4.3).

## Qualifications

- **What is new.** Unconditional strong stability of diagonal Padé schemes on linear
  seminegative problems already follows from their A-stability via von Neumann's lemma,
  and from the algebraic stability of the Gauss methods; Sun et al. say so themselves
  (§1). The contribution of Thms. 5.1–5.2 is the explicit identity, its definiteness
  for every $m$ and its agreement with the continuous law, not the stability
  conclusion.
- The result concerns autonomous linear problems; "order" here is the order of the
  rational approximation. Nonlinear energy behaviour of Gauss methods is a different
  matter (they preserve quadratic invariants; see
  [symplecticity](/properties/symplecticity.md)).
- Sun et al. use $s$ for the Padé degree; $m$ is used here because $s$ denotes the
  stage count in this bundle (the two coincide for Gauss methods).

# Citations

- [Sun et al. (2022)](/sources/sun-2022.md) — §1, Thm. 2.1, Ex. 4.2, Eq. (5.1), Thms. 5.1–5.2, Lemma 5.3, Thms. 5.4–5.5, Remarks 5.6–5.7, §5.3–5.5 and App. D, §6 (Exs. 6.1–6.3, Table 1, Fig. 1).
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §4.3, Table 1 (energy conservation of Gauss–Legendre on a mixed wave equation).
