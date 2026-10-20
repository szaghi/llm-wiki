---
type: Method
title: "Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)"
description: "Patankar-type schemes weight each production and destruction term by a ratio of new to old values, making every stage a linear M-matrix system; they are positive and conservative for every step size on production–destruction systems, up to arbitrary order, but can oscillate around steady states and lose order for vanishing constituents."
status: established
aliases: [Patankar-type methods, Patankar trick, modified Patankar schemes, modified Patankar–Runge–Kutta, MPRK, MPRK22, MPRK22ncs, MPRK43, MPRKSO, SSPMPRK, MPE, modified Patankar–Euler, Patankar–Euler, modified Patankar deferred correction, mPDeC, MPDeC, modified Patankar linear multistep, MPLM, modified Patankar multistep, MPMS2, MPMS3, Patankar predictor–corrector, Patankar weight denominator]
tags: [positivity, structure-preserving, stiff, implicit, deferred-correction, linear-multistep]
timestamp: 2026-10-20T14:00:00Z
---

# Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)

A **Patankar-type method** integrates a
[production–destruction system](/definitions/production-destruction-system.md)
$y_i'=\sum_j(p_{ij}(y)-d_{ij}(y))$ with an explicit or implicit base scheme in which every
destruction term $d_{ij}$ is multiplied by $y^{n+1}_i/\varpi_i$ and, in the *modified*
variants, every production term $p_{ij}$ by $y^{n+1}_j/\varpi_j$, where the
**Patankar weight denominators** $\varpi_i>0$ are computed from known values and are
independent of $y^{n+1}$ (registry §8). The unknown then enters linearly: each stage is one
linear system whose matrix is an M-matrix for every $h$, so the scheme is positive for
every step size, and the modified weighting keeps the production–destruction pairs
balanced, so it is conservative. Here $y^n_i$ is component $i$ of $y_n$ and $Y_{k,i}$
component $i$ of stage $Y_k$ (page-local). The trick originates with Patankar (1980) and
its conservative form with Burchard, Deleersnijder and Meister (2003), as recalled by
[Torlo et al. (2022)](/sources/torlo-2022.md) (§2.1),
[Ciallella et al. (2022)](/sources/ciallella-2022.md) (§4.2),
[Izzo et al. (2025)](/sources/izzo-2025.md) (§1),
[Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) (§2.1) and
[Zhu et al. (2024)](/sources/zhu-2024.md) (§1, Eq. (1.5)). Base schemes in the
sources: Euler, explicit Runge–Kutta (MPRK, MPRKSO), deferred correction (mPDeC), explicit
linear multistep methods (MPMS, MPLM), and a post-processing of SDIRK steps (Patankar
predictor–corrector).

## The Patankar trick and why it gives unconditional positivity

**Patankar–Euler** weights only the destruction:
$y^{n+1}_i=y^n_i+h\sum_j\bigl(p_{ij}(y_n)-d_{ij}(y_n)\,y^{n+1}_i/y^n_i\bigr)$. The system
is diagonal and positive, but production and destruction no longer cancel, so the scheme
is not conservative (Torlo et al. 2022, Eq. (8); Ciallella et al. 2022, Eq. (27)).
**Modified Patankar–Euler** (MPE) weights both:

$$y^{n+1}_i=y^n_i+h\sum_j\Bigl(p_{ij}(y_n)\frac{y^{n+1}_j}{y^n_j}-d_{ij}(y_n)\frac{y^{n+1}_i}{y^n_i}\Bigr),$$

i.e. $\varpi=y_n$ (Torlo et al. 2022, §2.1; Ciallella et al. 2022, Eq. (28); Izzo et al.
2025, Eq. (3.19)). It is first order (Izzo et al. 2025, §3, after Burchard et al.). The
mechanism is the same in every Patankar scheme; Izzo et al. prove it for their multistep
class (Lemma 2.2) and Torlo et al. state it for MPE (§2.1, after Axelsson):

- the step is $My_{n+1}=r$ with a known right-hand side $r>0$;
- $M$ has diagonal $1+h\sum_jd_{ij}/\varpi_i>0$ and off-diagonal entries
  $-hp_{ij}/\varpi_j\le0$; for a conservative system, $p_{ji}=d_{ij}$ makes $M^\top$ strictly
  diagonally dominant;
- a strictly diagonally dominant Z-matrix is an M-matrix, so $M^{-1}\ge0$ and
  $y_{n+1}=M^{-1}r>0$, whatever $h$.

Conservation follows because, with $p_{ij}=d_{ji}$, the weighted terms
$p_{ij}y^{n+1}_j/\varpi_j$ and $d_{ji}y^{n+1}_j/\varpi_j$ cancel in $\sum_i$ (Izzo et al.
2025, Lemma 2.3). On a linear conservative PDS, MPE coincides with implicit Euler (Torlo et
al. 2022, §2.1). All modified Patankar schemes considered by Torlo et al. (MPE,
MPRK(2,2,α), MPRK(4,3,α,β), MPRKSO, mPDeC, MPRK(3,2), and the non-conservative SI-RK) are
**steady-state preserving**: if the right-hand side vanishes at $y^*$ and $y_n=y^*$, then
$y_{n+1}=y^*$, because the stage systems have unique solutions and the Patankar weights
reduce to 1 (Def. 2.2, Prop. 2.3); IMEX modifications of explicit Runge–Kutta methods need
not be (§2, after Chertock et al.).

**Why the first-order barrier does not apply.** Runge–Kutta and general linear methods
that are unconditionally positive for all positive ODEs have order at most 1
(Bolley–Crouzeix, as recalled by [Nüßlein et al. 2021](/sources/nusslein-2021.md), §1,
and by Torlo et al. 2022, §1; see
[positivity preservation](/properties/positivity-preservation.md)). Patankar schemes are
not general linear methods: the weights $y^{n+1}/\varpi$ make the update a nonlinear,
solution-dependent function of the data, and the scheme is defined only on PDS. MPRK
methods "avoid the barrier for the same reason" as unconditionally positive diagonally
split Runge–Kutta methods (Nüßlein et al. 2021, §1). This is why Izzo et al. (2025) can
build unconditionally positive multistep schemes of orders 2 to 6 and Öffner–Torlo
deferred correction reaches arbitrary order: the barrier binds linear methods and is not
contradicted. The price is a different notion of order. Consistency now requires the
Patankar weights to approach 1 at the right rate, and the order theorems assume all
constituents bounded away from zero, which is where the issues below arise.

## Modified Patankar–Runge–Kutta methods

**MPRK(2,2,α)** (Kopecz–Meister; $\alpha=1$ from Burchard et al.), as written by Torlo et
al. (2022, §2.2), is the modified two-stage second-order Runge–Kutta method with
$c_2=\alpha\ge\tfrac12$:

$$\begin{aligned}
Y_1&=y_n,\qquad Y_{2,i}=y^n_i+c_2h\sum_j\Bigl(p_{ij}(Y_1)\frac{Y_{2,j}}{Y_{1,j}}-d_{ij}(Y_1)\frac{Y_{2,i}}{Y_{1,i}}\Bigr),\\
y^{n+1}_i&=y^n_i+h\sum_j\Bigl(\bigl[(1-\tfrac1{2c_2})p_{ij}(Y_1)+\tfrac1{2c_2}p_{ij}(Y_2)\bigr]\frac{y^{n+1}_j}{\varpi_j}-\bigl[(1-\tfrac1{2c_2})d_{ij}(Y_1)+\tfrac1{2c_2}d_{ij}(Y_2)\bigr]\frac{y^{n+1}_i}{\varpi_i}\Bigr),
\end{aligned}$$

with $\varpi_i=Y_{2,i}^{1/c_2}Y_{1,i}^{1-1/c_2}$. For $c_2=1$ it is the modified Heun method
(SSPRK(2,2)) and coincides with mPDeC2. [Izgin et al. (2022)](/sources/izgin-2022.md)
(Eq. (6)) write the Kopecz–Meister family with a switch on the stage: MPRK22(α) is the
scheme above, with $\alpha=c_2$, whose stage is itself conservative, and **MPRK22ncs(α)**
("non-conservative stages") leaves the production term of the stage unweighted,
$Y_{2,i}=y^n_i+\alpha h\sum_j\bigl(p_{ij}(Y_1)-d_{ij}(Y_1)Y_{2,i}/Y_{1,i}\bigr)$, with the
same update. Their stability is analysed below.

**Higher order.** MPRK(4,3,α,β) (MPRK43 in Kopecz–Meister's notation) is a four-stage
third-order family built on three-stage third-order Runge–Kutta tableaux with
$c=(0,\alpha,\beta)$; its Patankar denominators combine stage values with fractional
exponents and an auxiliary linear solve, and its coefficients are nonnegative only in a
region of the $(\alpha,\beta)$ plane (Torlo et al. 2022, App. A, Eq. (72)). Nurkhametova et
al. (2026, §2.1) recall the surrounding theory: order conditions and the MPRK22 family,
the result that no three-stage third-order MPRK exists with standard Patankar weights, the
necessary and sufficient conditions for MPRK43, arbitrary-order MPRK order conditions, and
Lyapunov stability of MPRK22 (Izgin, Kopecz and Meister). Torlo et al. (Remark 2.1) note
that higher-order MPRK need more stages than the classical method of the same order.
Izzo et al. (2025, §4) compare with the third-order MPRK of Kopecz–Meister with
$\gamma=0.5$ as "MPRK3".

**MPRKSO** (Huang and Shu; Huang, Zhao and Shu) builds the Patankar weights into the Shu–Osher form of a
[SSP](/methods/strong-stability-preserving-runge-kutta.md) method: MPRKSO(2,2,α,β) with
weight exponent $\frac{1-\alpha\beta+\alpha\beta^2}{\beta(1-\alpha\beta)}$ (Shu–Osher
parameters $\alpha\in[0,1]$, $\beta>0$, $\alpha\beta+\frac1{2\beta}\le1$), and a
four-stage third-order MPRKSO(4,3) with optimized SSP coefficients (Torlo et al. 2022,
Eq. (9), App. A). Zhu et al. (2024, §2.1, Eqs. (2.2)–(2.3)) recall the same second-order
parameters and the third-order MPRKSO of Huang, Zhao and Shu, whose coefficients they do
not reprint. SSP-MPRK schemes are positive and conservative under the convective CFL
condition independently of the stiffness of the sources (Nurkhametova et al. 2026, §2.1,
recalled).

**MPRK(3,2)** is a new three-stage second-order scheme of Torlo et al. (2022, §2.5) on the
SSPRK(3,3) abscissae $c=(0,1,\tfrac12)$:

$$\begin{aligned}
Y_2&:\ \text{one MPE step from }y_n,\\
Y_{3,i}&=y^n_i+\tfrac h4\sum_j\Bigl(\bigl[p_{ij}(Y_1)+p_{ij}(Y_2)\bigr]\frac{Y_{3,j}}{Y_{2,j}}-\bigl[d_{ij}(Y_1)+d_{ij}(Y_2)\bigr]\frac{Y_{3,i}}{Y_{2,i}}\Bigr),\\
y^{n+1}_i&=y^n_i+\tfrac h6\sum_j\Bigl(\bigl[p_{ij}(Y_1)+p_{ij}(Y_2)+4p_{ij}(Y_3)\bigr]\frac{y^{n+1}_j}{Y_{2,j}}-\bigl[d_{ij}(Y_1)+d_{ij}(Y_2)+4d_{ij}(Y_3)\bigr]\frac{y^{n+1}_i}{Y_{2,i}}\Bigr).
\end{aligned}$$

Its second order rests on a heuristic argument ($Y_2$, $Y_3$ first order, Simpson's rule
in the update, $y^{n+1}/Y_2=1+\mathcal O(h^2)$) and on symbolic expansions on the linear
test, "no formal proof" (§2.5, Suppl. §2.2).

**SI-RK2 and SI-RK3** (Chertock, Cui, Kurganov and Wu) are semi-implicit SSP Runge–Kutta
methods that put a Patankar weight on the destruction terms of each Euler substep and add
a final correction restoring the order; they are positive but **not conservative**, and
Torlo et al. were the first to read them as Patankar methods (§1, Eq. (10)).

**Negative coefficients.** A negative Runge–Kutta or quadrature coefficient would turn a
production term into a destruction one and break the M-matrix sign pattern; the schemes
swap the production and destruction weights of such terms (Torlo et al. 2022, App. A,
§2.3; the mPDeC selector below).

## Modified Patankar deferred correction (mPDeC)

Öffner and Torlo apply the trick to explicit [deferred correction](/methods/deferred-correction.md)
in Abgrall's form (Torlo et al. 2022, §2.3; Ciallella et al. 2022, §4.3, Eq. (29)). On
subnodes $t_{n,m}$, $m=0,\dots,\mathsf M$, with the interpolation weights $\omega_{mr}$ of
[deferred correction](/methods/deferred-correction.md) ($h\omega_{mr}$ integrates the Lagrange
basis polynomial of node $r$ over $[t_n,t_{n,m}]$) and iterates $y^{(k)}_m$ (page-local, $y^{(k)}_0=y_n$),
correction $k=1,\dots,K$ solves for every node

$$y^{(k)}_{m,i}-y^n_i-h\sum_{r=0}^{\mathsf M}\omega_{mr}\sum_j\Bigl(p_{ij}(y^{(k-1)}_r)\frac{y^{(k)}_{m,\varsigma(j,i)}}{y^{(k-1)}_{m,\varsigma(j,i)}}-d_{ij}(y^{(k-1)}_r)\frac{y^{(k)}_{m,\varsigma(i,j)}}{y^{(k-1)}_{m,\varsigma(i,j)}}\Bigr)=0,$$

where the index selector $\varsigma(j,i)=j$ if $\omega_{mr}>0$ and $i$ otherwise
(page-local) swaps production and destruction for negative weights, so positivity
survives negative quadrature weights. Then $y_{n+1}=y^{(K)}_{\mathsf M}$. Order $d$ uses
$\mathsf M=d-1$ equispaced subintervals and $K=d$ corrections; equispaced and
Gauss–Lobatto nodes coincide up to order 3; mPDeC1 is MPE and mPDeC2 is MPRK(2,2,1)
(Torlo et al. 2022, §2.3). The scheme is conservative, unconditionally positive and of
arbitrary order (Ciallella et al. 2022, §4.3, recalled). With Gauss–Lobatto nodes
$\mathsf M$ subintervals give a collocation operator of order $2\mathsf M$, and Ciallella
et al. use $\mathsf M=3$, $K=5$ for fifth order (§4.1, Remark 4.3).

**mPDeC in a PDE solver** (Ciallella et al. 2022). The finite-volume WENO5 update of the
water height of the shallow-water equations is rewritten as a conservative PDS (the
positive and negative parts of the face fluxes, Eq. (33)), advanced by mPDeC, while the
momenta are advanced by explicit DeC with the same subnodes and corrections (Algorithms
4–5). Each correction and subnode needs one sparse linear system
$\mathbb M(y^{(k-1)}_m)\,y^{(k)}_m=y_n$ with at most five nonzeros per row (page-local
$\mathbb M$; Eqs. (30)–(31)). By construction its diagonal is at least 1 and its
off-diagonal entries are nonpositive, so Jacobi iteration from the right-hand side keeps
every iterate positive, whereas Krylov methods in general do not (§5.1, Remark 5.1). Jacobi
needs "usually 10-20 iterations" at machine tolerance, at worst 40, almost independently
of the mesh and growing with the CFL number (§5.1, Figs. 6c, 15). The whole procedure
costs about 18% more than explicit DeC5 at equal CFL number (§5.1, §6.6), about 10% on the
vortex test (§6.1). Positivity of the water height then holds for every $h$; the step is
limited only by the explicit DeC of the momenta, whose stability in this combination is
"simply assumed" (Remark 5.5). In tests the scheme converges at fifth order, runs a dry
dam break at CFL 1.5 with positive heights, and keeps order near five on an almost-dry
lake at rest where SSPRK(6,4) with a positivity limiter plateaus near $10^{-6}$
(§6.1–6.6, Tables 1–2). They present it as the first application of mPDeC to a PDE and
note that earlier Patankar methods in fluid codes were Runge–Kutta-based and at most third
order (§1).

## Modified Patankar linear multistep methods (MPMS, MPLM)

**MPMS2 and MPMS3** (Zhu et al. 2024, §2.2). The first modified Patankar multistep
schemes in the sources, presented as the first in the literature (§5), weight the explicit
[SSP](/methods/strong-stability-preserving-runge-kutta.md) multistep methods of
Gottlieb–Shu–Tadmor, $y_{n+1}=\tfrac14y_{n-2}+\tfrac34y_n+\tfrac32hf(y_n)$ (order 2) and
$y_{n+1}=\tfrac{11}{27}y_{n-3}+\tfrac49hf(y_{n-3})+\tfrac{16}{27}y_n+\tfrac{16}9hf(y_n)$
(order 3), whose SSP coefficients are $\tfrac12$ and $\tfrac13$ (Eqs. (2.5)–(2.6), §3.3):

$$\begin{aligned}
\text{MPMS2:}\quad y^{n+1}_i&=\tfrac14y^{n-2}_i+\tfrac34y^n_i+\tfrac32h\sum_j\Bigl(p_{ij}(y_n)\frac{y^{n+1}_j}{\varpi_j}-d_{ij}(y_n)\frac{y^{n+1}_i}{\varpi_i}\Bigr),\\
\text{MPMS3:}\quad y^{n+1}_i&=\tfrac{11}{27}y^{n-3}_i+\tfrac{16}{27}y^n_i+h\sum_j\Bigl(\bigl[\tfrac49p_{ij}(y_{n-3})+\tfrac{16}9p_{ij}(y_n)\bigr]\frac{y^{n+1}_j}{\varpi_j}-\bigl[\tfrac49d_{ij}(y_{n-3})+\tfrac{16}9d_{ij}(y_n)\bigr]\frac{y^{n+1}_i}{\varpi_i}\Bigr)
\end{aligned}$$

(Eqs. (2.8), (2.15)). The denominators are **weighted geometric means of past values**,
$\varpi_i=\prod_{r\ge0}(y^{n-r}_i)^{e_r}$ with exponents $e_r$, $\sum_re_r=1$ (page-local),
over three past levels for MPMS2 and four for MPMS3 (Eqs. (2.10), (2.17)). The sufficient
order condition is $\varpi_i=y_i(t_{n+1})+O(h^p)$, since the weights are then
$1+O(h^p)$ and the scheme differs from its base by $O(h^{p+1})$ (Eqs. (2.9), (2.16)). A
Taylor expansion gives one-parameter families: in Zhu et al.'s exponent names $(s,r)$ for
$y^n$, $y^{n-1}$ (and $p$ for $y^{n-2}$), the conditions are $r+2s-3=0$ for MPMS2 and
$r=-3s+6$, $p=3s-8$ for MPMS3 (Eqs. (2.14), (2.21)). Equivalently
$\sum_r(r+1)e_r=0$ for MPMS2 and additionally $\sum_r(r+1)^2e_r=0$ for MPMS3: $\log\varpi_i$
is the polynomial extrapolation of $\log y_i$ to $t_{n+1}$, exact for linear (MPMS2) or
quadratic (MPMS3) functions, with one redundant node, and some exponents are negative;
for example $\varpi_i=(y^n_i)^2/y^{n-1}_i$ for MPMS2 *(compiler restatement of Eqs. (2.14)
and (2.21), not in the source)*. The schemes are conservative (Lemma 2.1) and stated to
be unconditionally positive, with the proof skipped as "similar to Lemma 2.7" of
Kopecz–Meister (Lemma 2.2, Thms. 2.3–2.4). On a linear two-species exchange and a
three-species nonlinear test they show orders 1.98–2.07 and 2.96–3.32 (Tables 1–2). The
error at fixed $h$ depends on the free exponent and has a minimum, left to future work
(Remark 4.1, Fig. 1). With explicit DG convection the fully discrete schemes are positive
under $h\le\tfrac12h_{\mathrm{FE}}$ and $h\le\tfrac13h_{\mathrm{FE}}$ (§3.3, Eqs.
(3.8)–(3.9)), implemented as an explicit convective step, a positivity limiter at Gauss
points, the Patankar source step and a second limiter at the interface points, because
the Patankar step keeps positivity only at the points it acts on (§3.5, Remark 3.1); they
are applied to multispecies reacting Euler flows with detonations (§4.2–4.3). Zhu et al.
state, without cost data, that multistep schemes "work better" than Runge–Kutta ones
unless characteristic speeds change wildly (§5).

**General MPLM.** Izzo et al. (2025) apply the trick to explicit $k$-step
[linear multistep methods](/methods/linear-multistep-method.md) with nonnegative
coefficients. Write the base method in the backward form
$y_n=\sum_{r=1}^k\bar\alpha_ry_{n-r}+h\sum_{r=1}^k\bar\beta_rf(y_{n-r})$ ($\bar\alpha_r$,
$\bar\beta_r$ page-local; in the registry form with $\alpha_k=1$, $\beta_k=0$ these are
$\bar\alpha_r=-\alpha_{k-r}$, $\bar\beta_r=\beta_{k-r}$), with order conditions
$\sum_r\bar\alpha_r=1$ and $\sum_r(r^q\bar\alpha_r-qr^{q-1}\bar\beta_r)=0$, $q\le p$
(Eq. (2.7)). The MPLM-$k$ scheme (Def. 2.1, Eq. (2.8)) is

$$y^n_i=\sum_{r=1}^k\bar\alpha_ry^{n-r}_i+h\sum_{r=1}^k\bar\beta_r\sum_j\Bigl(p_{ij}(y_{n-r})\frac{y^n_j}{\varpi^n_j}-d_{ij}(y_{n-r})\frac{y^n_i}{\varpi^n_i}\Bigr),\qquad\bar\alpha_r,\bar\beta_r\ge0,$$

with denominators $\varpi^n=\varpi^n(y_{n-1},\dots,y_{n-k})$ that are positive and
independent of $y_n$; one linear system of size $d$ per level.

- **Positivity and conservation for every $h$** (Lemmas 2.2–2.3), by the M-matrix argument
  above, for a fully conservative PDS and positive starting values.
- **Order** (Thms. 3.1–3.2): MPLM-$k$ is consistent of order $p$ iff
  $\varpi^n_i(y(t_{n-1}),\dots,y(t_{n-k}))=y_i(t_n)+\mathcal O(h^p)$ (Eq. (3.12)), given an
  order-$p$ base method. Sufficiency follows from $y_i(t_n)/\varpi_i=1+\mathcal O(h^p)$;
  necessity is shown on a special one-pair linear PDS (App. A).
- **Convergence** (Thm. 3.5): order $p$ if the data are $C^p$, the starting errors
  $\mathcal O(h^p)$, the denominators $C^1$ and (3.12) holds, on a set where every component
  stays above some $\mu>0$ (page-local); the proof is a discrete Gronwall argument that uses
  $\bar\alpha_r\ge0$ (Lemma 3.4).
- **$\varpi$-embedding** (§3.1, Eq. (3.20), Thm. 3.6): the denominators of the order-$p$
  scheme are one step of an order-$(p-1)$ MPLM-$\tilde k$, $\tilde k\le k$, evaluated on
  the past values of the order-$p$ scheme, whose own denominators come recursively from a
  lower-order MPLM, down to MPE. This yields convergence of every order $p$. MPE as
  denominator already gives $y(t_n)+\mathcal O(h^2)$, hence a second-order MPLM.
- **Methods** (Table 1, MPLM-$k(p)$, coefficients of $y_{n-1},\dots,y_{n-k}$):
  MPLM-2(2) $\bar\alpha=(0,1)$, $\bar\beta=(2,0)$ (leapfrog); MPLM-4(3)
  $\bar\alpha=(\tfrac14,0,\tfrac34,0)$, $\bar\beta=(\tfrac{35}{18},\tfrac13,0,\tfrac29)$;
  MPLM-5(4), MPLM-7(5) and MPLM-10(6) with $\bar\alpha_k=1$ and the other $\bar\alpha_r=0$.
  Every printed set satisfies (2.7) exactly to its stated order. For MPLM-2(2), -5(4),
  -7(5) and -10(6) all roots of the first generating polynomial lie on the unit circle, so
  these base methods are only weakly stable; MPLM-4(3) has the root 1 and roots of modulus
  $\sqrt3/2$ and 0, so it is strongly stable *(compiler check of Table 1)*. For $k=4$,
  $\bar\alpha=(\tfrac{16}{27},0,0,\tfrac{11}{27})$, $\bar\beta=(\tfrac{16}9,0,0,\tfrac49)$
  reproduces a third-order modified Patankar multistep scheme of Zhu, Huang and Yang (§2),
  the MPMS3 base above.
- **Relation to MPMS.** Zhu et al. (2024) introduced MPMS2 and MPMS3 with a sufficient
  order condition, a formal Taylor argument and no convergence proof or starting
  procedure; Izzo et al. (2025) prove the condition necessary and sufficient for their
  class, prove convergence and give the $\varpi$-embedding. The two agree; Izzo et al.
  extend Zhu et al. in rigour and in order. Zhu et al.'s geometric means of past values and
  Izzo et al.'s embedded lower-order MPLM steps are two different choices of $\varpi$
  satisfying the same condition.
- **Numerics** (§4): observed orders 1–6 on a linear exchange, the algal bloom, the
  original six-species [Brusselator](/benchmarks/brusselator.md), a SACEIRQD COVID-19 model
  and a finite-volume heterogeneous diffusion (Tables 2–6); for instance 1.00–6.26 on the
  linear test (Table 2). Against MPRK3, MPLM is more efficient for $p\ge3$ or $p\ge4$
  (Figs. 4, 9, 13). Against the Julia mPDeC code of Öffner–Torlo, mPDeC is more efficient
  on the two small tests and MPLM on the Brusselator, the COVID model and the PDE (Figs.
  5, 14, 19–20, Table 6); the authors attribute this to mPDeC's several linear solves per
  step against MPLM's denominator computation, more favourable as $d$ grows (§4.3,
  stated, not measured). On the PDE at $h=2^{-9}$ MPLM-4(3) takes $9.71\cdot10^2$ against
  $2.85\cdot10^3$ CPU units for mPDeC(3), with errors $2.73\cdot10^{-8}$ against
  $7.97\cdot10^{-9}$ (Table 6).
- **Limits** (§5): reduced efficiency on stiff problems such as Robertson (no data shown);
  no stability analysis; constant steps only.

## Patankar predictor–corrector for SDIRK methods

Nurkhametova et al. (2026, §3.3) post-process a stiffly accurate
[SDIRK](/methods/diagonally-implicit-runge-kutta.md) step on a system written in the
graph Laplacian form $y'=\mathbb G(t,y)y$ of the
[production–destruction page](/definitions/production-destruction-system.md):

1. **Predictor:** an ordinary SDIRK step gives stages $Y_k$ and $y^{\mathrm p}_{n+1}$
   (page-local), possibly with negative entries.
2. **Clipping:** $\breve Y_k=\max(Y_k,0)$ componentwise (Def. 3.13). In a monotone norm
   clipping does not increase the local errors, $\mathcal O(h^{q+1})$ for the stages and
   $\mathcal O(h^{p+1})$ for the solution (Lemma 3.14).
3. **Ratio scaling:** $\Sigma_{Y/Z}=\operatorname{diag}_l\bigl(\max(Y_l,0)/\max(Z_l,\epsilon_{\mathrm c})\bigr)$
   with a small threshold $\epsilon_{\mathrm c}>0$ (page-local symbols; Def. 3.15).
4. **Corrector:** one linear solve,
   $$\bar{\mathbb G}=\sum_{k=1}^sb_k\,\mathbb G(\breve Y_k)\,\Sigma_{Y_k/y^{\mathrm p}_{n+1}},\qquad y_{n+1}=(I-h\bar{\mathbb G})^{-1}y_n\qquad\text{(Eq. (24))}.$$

The motivation: when all stages are nonnegative and $y^{\mathrm p}_{n+1}\ge\epsilon_{\mathrm c}$,
the predictor itself can be written in this form (Remark 3.17), so the corrector is the
predictor with Patankar-type weights $Y_k/y^{\mathrm p}_{n+1}$. Since $b\ge0$ makes
$\bar{\mathbb G}$ a nonnegative combination of scaled graph Laplacians, $I-h\bar{\mathbb G}$
is an M-matrix: $y_n\ge0$ gives $y_{n+1}\ge0$, $y_n>0$ gives $y_{n+1}>0$, and every linear
invariant that is a left null vector of $\mathbb G$ is preserved, for every $h$ (Eqs.
(24d)–(24e)). Under the strong sign assumption the stages need not be clipped (Remark
3.18). A **stage variant** corrects every stage in the same way and needs $a_{ij}\ge0$ as
well (§3.4, Eq. (27)). The cost is one extra LU factorization per step, "an extra MPRK type
stage", against one per stage for MPRK (Remark 3.22).

**Proven versus observed order.** Started from exact data, the corrected solution has
local error $\mathcal O(h^{\min(q+2,p+1)})+\mathcal O(\epsilon_{\mathrm c})$; with
$\epsilon_{\mathrm c}=Ch^{\min(q+2,p+1)}$ the method has order $\min(p,q+1)$
(Prop. 3.23). With stage order $q=1$ this proves order 2 for every SDIRK base. The
experiments (SDIRK21, SDIRK32, SDIRK43 of Kennedy–Carpenter on Robertson, MAPK, the
stratospheric problem and KdV) report observed slopes close to the nominal 2, 3 and 4, for
example 2.07, 4.27, 4.70 on the stratospheric problem and 1.51, 3.47, 5.47 on Robertson
with the final-stage correction (Table 4), and 1.95, 2.84, 3.76 on Robertson with all
stages corrected (Table 5); the paper concludes the correction "preserves, in practice, the
formal order" (§5.3.5). The proven bound is an upper bound on the error, so higher observed
slopes are compatible with it; nominal order beyond 2 remains an observation on four
problems, with $\epsilon_{\mathrm c}$ unstated.

**Positivity hypothesis versus the tested methods.** The guarantee requires
$b_i\ge0$ (§3.3: "only non-negative weights") and, for the stage variant, $a_{ij}\ge0$
(§3.4). The printed tableaux (§4.2.2–4.2.3) have $b_3=-\tfrac{723}{9272}$ for SDIRK32 and
$b_2=-\tfrac{400}{819}$, $b_4=-\tfrac{575}{252}$ for SDIRK43, and negative $a_{ij}$ in both;
only SDIRK21 satisfies the hypotheses *(compiler check of the printed tableaux, PDF pp.
28–29; not discussed in the source)*. With a negative $b_k$, $\bar{\mathbb G}$ need not
have the graph Laplacian sign pattern, so the unconditional positivity statement does not
cover two of the three tested methods; the positivity figures use SDIRK21 (§5.1).

**Results** (§5). Uncorrected SDIRK21 produces negative values on Robertson (species $y_2$,
magnitudes $10^{-10}$–$10^{-15}$) and on the stratospheric problem ($O(^1D)$ and $O$); both
corrections remove them (Figs. 2–7). Invariant errors stay at roundoff, e.g.
$2.22\times10^{-15}$ on Robertson (§5.2). Enforcing positivity by rejecting steps with
negative entries makes the step collapse to the minimum step on the stratospheric problem
(Fig. 8). Wall-clock changes for SDIRK43 at tolerance $10^{-7}$ (MATLAB, laptop): $-81.4\%$
on Robertson, which the authors attribute to avoiding stiff dynamics in non-physical
negative states, $-7.9\%$ on MAPK, $+94.5\%$ on KdV and $+266\%$ on the stratospheric
problem (Table 6). On KdV the all-stage correction "exhibited severely distorted
dynamics" (not shown), so only the final-stage correction is recommended there (§5.1.4).
For step-size control the embedded estimate uses the uncorrected predictor, optionally
augmented by $\lVert y_{n+1}-y^{\mathrm p}_{n+1}\rVert$ (Remarks 3.20–3.21; see
[embedded pairs](/methods/embedded-runge-kutta-pair.md)). For explicit Runge–Kutta bases the
correction reduced convergence to first order (§1; no data shown).

## Issues: oscillations, steady states and vanishing constituents

Torlo et al. (2022) analyse the failure modes on the linear exchange
$y_1'=-\theta y_1+(1-\theta)y_2$, $y_2'=\theta y_1-(1-\theta)y_2$, $0\le\theta\le1$, from
$(1-\varepsilon,\varepsilon)$ (page-local $\theta$; time rescaled so that the nonzero
eigenvalue is $-1$; a general exchange with rates $\kappa_1,\kappa_2$ rescales $h$ by
$\kappa_1+\kappa_2$). Its steady state is $(1-\theta,\theta)$ and
$v=\theta y_1-(1-\theta)y_2$ obeys $v'=-v$ (§3, Eqs. (11)–(18)).

**Oscillations around the steady state.** A one-step method is *not overshooting* if
$y^1_2$ stays on the same side of $\theta$ as $\varepsilon$ (Property 4.1) and moves in the
*correct direction* if $y^1_2$ moves from $\varepsilon$ towards $\theta$ (Property 4.2);
both together mean oscillation-free. For a Runge–Kutta method the diagonalization commutes
with the scheme, so Property 4.1 holds iff $R(-h)>0$ and Property 4.2 iff $R(-h)<1$, which
every A-stable method satisfies (Props. 4.3–4.6; see
[stability function](/definitions/stability-function.md)). Table 1 lists the conditions:
always for Radau IA5, Radau IIA5, Lobatto IIIA4 and IIIB4, Lobatto IIIC2, Gauss–Legendre 4,
implicit Euler and the Kraaijevanger–Spijker DIRK; $h<3$ for Radau IA3 and IIA3; $h<2$ for
implicit midpoint and trapezoid; $h<1+\sqrt2$ for TR-BDF2. Patankar schemes are nonlinear,
so this equivalence fails, and **unconditional positivity does not imply absence of
oscillations**. For MPRK(2,2,1) = mPDeC2, Thm. 4.7 proves both properties for $h\le2$
(i.e. $h\le2/(\kappa_1+\kappa_2)$), sharp as $\theta,\varepsilon\to0$. For the others a
numerical scan gives the largest oscillation-free step (§6, Fig. 6): MPRK(3,2) 16.56,
MPRKSO(4,3) 1.31, SI-RK2 1.41, SI-RK3 1.27; equispaced mPDeC of orders 2–8 between 1.04 and
2.0; Gauss–Lobatto mPDeC 1.0 from order 6 on; against implicit midpoint and trapezoid 2.0,
TR-BDF2 2.4, Radau IIA3 3.0 and Radau IIA5 $\infty$. MPRK(2,2,α) has bound 1 for $\alpha<1$,
2 for $\alpha=1$, and larger bounds for $\alpha>1$ (Fig. 5b). On the scalar nonlinear
problem $y'=-k\lvert y\rvert y+1$ the linear bounds "can mostly be transferred", except for
second-order schemes (Suppl. §4.1). Torlo et al. present the Lyapunov stability of MPRK22
for all $h>0$ shown by Izgin, Kopecz and Meister as a different notion (stability of the
fixed point, not monotone approach), not as a conflict (Remark 1.4).

**Lyapunov stability of steady states.** Since a Patankar scheme cannot be applied to
$y'=\lambda y$, Izgin et al. (2022) test on the general positive conservative linear
$2\times2$ system $y_1'=-ay_1+by_2$, $y_2'=ay_1-by_2$, whose steady states form a line
(page-local $a,b\ge0$). Their centre-manifold theorem for positive conservative maps makes
a steady state Lyapunov stable when the non-unit Jacobian eigenvalue $R$ of the map has
$\lvert R\rvert<1$ (Thm. 2.9). For MPRK22(α), $R_1(z)=\frac{2-2\alpha z-z^2}{2(1-z)(1-\alpha z)}$
with $z=-h(a+b)$, and $\lvert R_1\rvert<1$ for every $z<0$ and $\alpha\ge\tfrac12$: the
scheme is **unconditionally stable** in this sense (Lemma 3.8, Cor. 3.9). MPRK22ncs(α) has
a two-variable $R_0(-ha,-hb)$; it is unconditionally stable for $\alpha\ge1$ and stable
only below a critical step for $\tfrac12\le\alpha<1$, e.g. $h^*\approx0.14$ for
$\alpha=0.5$ and $h^*\approx0.38$ for $\alpha=0.8$ when $a=b=25$ (Lemma 3.10, Cor. 3.11,
§4). On the degenerate system $b=0$ both families contract monotonically, so that test
cannot separate them (§3.1). Details on
[Lyapunov stability of positive, conservative schemes](/results/lyapunov-stability-positive-conservative-schemes.md).
"Unconditionally stable" here is Lyapunov stability of the fixed point at every $h$, not
freedom from oscillations: MPRK22(1) oscillates at $h=4$ in their Fig. 4, and Torlo et
al. bound its oscillation-free step by 2. The two results are consistent, as Torlo et al.
(Remark 1.4) already say.

**Order reduction for vanishing initial data.** The classical order proofs fix
$\varepsilon>0$. In the coupled limit $h\to0$ with $\varepsilon/h\to0$, which models a
constituent absent at $t=0$, denominators of size $\mathcal O(\varepsilon)$ or
$1/\mathcal O(\varepsilon)$ degrade the stages (Lemmas 5.2–5.3; §5, Eq. (40)), and "the limits
$\Delta t\to0$ and $\varepsilon\to0$ are not interchangeable" (Suppl. Remark 2.4). First-step
and final errors (Table 2, Thm. 5.4):

| scheme | first step | final time |
|---|---|---|
| MPRK(2,2,α), $\alpha>1$ | $\Theta(h)$ | $\Theta(h)$ (initial state a spurious steady state) |
| MPRK(2,2,1) = mPDeC2 | $\Theta(h^3)$ | $\Theta(h^2)$ |
| MPRK(2,2,α), $\tfrac12\le\alpha<1$ | $\Theta(h^2)$ | $\Theta(h^2)$ |
| MPRK(4,3,α,β), depending on the weight exponents | $\Theta(h)$ to $\Theta(h^4)$ | $\Theta(h)$ to $\Theta(h^3)$ |
| MPRKSO(4,3) | $\Theta(h^2)$ | $\Theta(h^2)$ |
| MPRK(3,2), SI-RK2, SI-RK3 | $\Theta(h^3)$ | $\Theta(h^2)$ |
| mPDeC, Gauss–Lobatto any order, or equispaced with $\omega_{\mathsf Mr}\ge0$ | $\Theta(h^2)$ | $\Theta(h^2)$ |
| mPDeC equispaced with some $\omega_{\mathsf Mr}<0$ (orders 9 and $\ge11$) | $\Theta(h)$ | $\Theta(h)$ |

So every third- and higher-order Patankar scheme analysed falls to global order 1 or 2
when a constituent vanishes (Thm. 5.5 for mPDeC: a negative weight carries the vanishing
state through the iterations, Prop. 5.6). The schemes with the largest oscillation-free
bounds, MPRK(2,2,α>1) and MPRK(4,3) near the boundary of their nonnegative-coefficient
region, are exactly those that drop to first order (§6). MPRK(3,2) combines the largest
bound with second order for vanishing data and the correct direction, "maybe the best
conditions of all the schemes" (§6). On the [Robertson problem](/benchmarks/robertson-problem.md)
with zeros replaced by $10^{-180}$ and 20 exponentially growing steps, the schemes that
fall to first order miss the evolution of $y_2$ and sometimes $y_3$, and the
non-conservative SI-RK blow up (§7.1, Fig. 7). On the HIRES problem ($10^3$ uniform steps,
zeros replaced by $10^{-35}$) MPRK(2,2,5) misses several species while MPRK(2,2,1) is
accurate, MPRKSO(2,2,0,8) shows the spurious steady state, and sixth-order Gauss–Lobatto
mPDeC captures a late reaction (§7.2, Fig. 8). See
[order reduction](/definitions/order-reduction.md).

Nurkhametova et al. (2026, §1) summarize the same picture from outside: MPRK and related
nonstandard schemes "often suffer from order reduction, additional computational cost, or
difficulty achieving high orders of accuracy, particularly for stiff systems". Izzo et al.
(2025) obtain their observed orders 1–6 with zero components replaced by about
$2.2\times10^{-308}$ on the Brusselator and COVID tests, outside the hypothesis $\mu>0$ of
their convergence theorem; their tests do not explore the vanishing-data limit
systematically.

## Relation to other positivity-preserving approaches

[Adaptive-weight Runge–Kutta methods](/methods/adaptive-weight-runge-kutta.md) obtain
positivity by changing the weights of an ordinary Runge–Kutta step after the stages,
problem by problem and step by step; their "unconditional" positivity is data-dependent,
whereas Patankar schemes are a fixed nonlinear scheme positive for all $h$ on the PDS
class (Nüßlein et al. 2021, §1). [Bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)
and SSP methods with positivity limiters give positivity under a CFL restriction
(Ciallella et al. 2022, Remark 3.1). Nurkhametova et al. (2026, §2) also recall GeCo
schemes (explicit, positive, conservative, bounded stability), exponential and Magnus
integrators for graph Laplacian systems at orders 2–3, and Sandu's projection onto the
nonnegative states that satisfy the linear invariants. The overview is on
[positivity preservation](/properties/positivity-preservation.md).

## Qualifications

- **Scope of "unconditional".** In Ciallella et al. (2022) positivity is unconditional for
  the water height only; the scheme is CFL-limited by the explicit DeC of the momenta, the
  WENO positivity limiter is still applied, and near dry states a regularized division
  (Remark 4.5, Eq. (32)) replaces the exact one on which the mPDeC proofs rest. Torlo et al.
  (2022) show that positivity for every $h$ coexists with oscillation-free bounds of order
  one. Neither is a stability result for the combined or nonlinear scheme.
- **Scope of Izzo et al.'s theorems.** The necessity half of Thm. 3.2 is proved on one
  special linear PDS, so it shows that order $p$ for all PDS forces (3.12), not that (3.12)
  holds for a given problem; Thm. 3.5 needs all components above $\mu>0$ *(compiler reading of the
  proofs, Thm. 3.5 and App. A; not stated by the authors)*.
- **MPDeC robustness in Izzo et al.** The mPDeC code of Öffner–Torlo returns "several NAN"
  on the COVID model with zero initial components (Izzo et al. 2025, §4.4); mPDeC was run
  there with data modified to $10^{-10}$ while MPLM received the $2.2\times10^{-308}$
  replacement, so the comparison concerns that code and data, not the method. It does not
  contradict Torlo et al. or Ciallella et al., who make no claim about that problem.
- **Printed slips in Torlo et al. (2022)** *(compiler checks of the PDF)*.
  Eq. (6) prints the initial value $(0.1,0)$ of the motivating example, while the Fig. 1
  caption gives $(1,10^{-250})$ and the plotted $y_2$ reaches about 0.5, consistent with
  unit mass. "MPRK(3,4,2,0.5)" in §5 is MPRK(4,3,2,0.5), the scheme of Fig. 2; its first
  weight exponent $p=3a_{21}(a_{31}+a_{32})b_3$ (App. A) is $8/3\approx2.67$ for $c_2=2$,
  $c_3=\tfrac12$ and third-order weights, not the printed 3, which
  does not change the conclusion. The MPRKSO(4,3) coefficient "$\eta_3$" is printed twice, the
  second value being the otherwise missing $\eta_4$. §6 says Gauss–Lobatto mPDeC has bound one
  "for orders four and higher", while Fig. 6a gives 1.07 and 1.04 at orders 4 and 5 and 1.0
  from order 6. The supplement says the order of MPRK(2,2,α), $\alpha\in[\tfrac12,1)$, "reduces
  to 1" for vanishing data, where the main text gives a final error $\Theta(h^2)$: the
  supplement means the local order of the first step.
- **Printed slips in Izzo et al. (2025)** *(compiler checks of the PDF, p. 4 and Table 4)*. The $k=3$ scheme of Zhu, Huang
  and Yang is printed as $\bar\alpha=(\tfrac34,0,\tfrac14)$, $\bar\beta=(0,\tfrac32,0)$ and
  called second order; these coefficients satisfy (2.7) only for $q=1$, while
  $\bar\beta=(\tfrac32,0,0)$ gives second order, the classical three-step SSP multistep scheme.
  Zhu et al. (2024) themselves print the latter, $\tfrac32hf(y_n)$ with $y_n$ the most
  recent level (Eqs. (2.5), (2.7)–(2.8)), so the slip is Izzo et al.'s *(compiler check of
  Zhu et al., arXiv v1, p. 6)*.
  In Table 4 the MPE error at the finest step is printed $2.21\cdot10^{-4}$ with observed
  order 1.00 after $4.42\cdot10^{-2}$; order 1 needs $2.21\cdot10^{-2}$.
- **Scope of Zhu et al.'s claims (2024).** Unconditional positivity of MPMS2 and MPMS3 is
  stated with the proof omitted (Lemma 2.2), and Thms. 2.3–2.4 state it for nonnegative
  data, where a geometric mean with negative exponents is undefined at a zero past value,
  while Lemma 2.2 assumes strictly positive data. "Order" is formal consistency by Taylor
  expansion; the starting procedure for the multistep levels is not stated. The abstract's
  claim that the schemes handle stiff sources "with relatively large time steps" has no
  supporting step sizes, and the conclusions say "we take appropriately small time step"
  (§5). The second accuracy test prints "$p_{ij}=d_{ij}=1$ for other sets of $i,j$", which
  does not reproduce the stated ODE; 0 is meant (Example 2).
- **Scope of Izgin et al. (2022).** The stability result is local, for $2\times2$ linear
  test systems with positive steady states; higher dimensions, nonlinear systems and
  global stability are open (§5).
- **Printed slips in Nurkhametova et al. (2026)** *(compiler checks of the PDF, pp. 19, 28,
  and §5.3)*. The embedded weights of
  SDIRK32 sum to about 0.379, so the printed $\hat b$ is not consistent; the main weights are
  correct to order 3. The stage corrector (27) carries a spurious inner factor $h$, absent
  from the worked example (30). §4.2 says the experiments use fixed steps, while §5.3 uses
  adaptive steps for the ODE tests. The threshold $\epsilon_{\mathrm c}$ used in the
  experiments is never stated, although Prop. 3.23 makes the order depend on it.

# Citations

- [Torlo et al. (2022)](/sources/torlo-2022.md) — §1 (Remark 1.4), §2.1–2.5 (Eqs. (8)–(10), Def. 2.2, Prop. 2.3, Remark 2.1), §3 (Eqs. (11)–(18)), §4 (Props. 4.3–4.6, Table 1, Thm. 4.7), §5 (Lemmas 5.2–5.3, Thms. 5.4–5.5, Prop. 5.6, Table 2), §6 (Figs. 5–6), §7 (Figs. 7–8), App. A–B, Suppl. §2.2, §4.1; arXiv v5.
- [Ciallella et al. (2022)](/sources/ciallella-2022.md) — §1, Remark 3.1, §4.1–4.3 (Eqs. (27)–(31), Remarks 4.3–4.5), §5.1 (Eq. (33), Remarks 5.1, 5.5, Algorithms 1–5), §6 (Tables 1–2, Figs. 5–16); arXiv v3.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §1, §2 (Def. 2.1, Eqs. (2.7)–(2.10), Lemmas 2.2–2.3), §3 (Thms. 3.1–3.6, Eqs. (3.12), (3.19)–(3.20), Lemma 3.4), §4 (Tables 1–6, Figs. 4–20), §5, App. A; arXiv v1.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §1, §2.1, §3.3–3.4 (Defs. 3.13, 3.15, Lemma 3.14, Remarks 3.17–3.22, Eqs. (24)–(27), Prop. 3.23), §4.2 (tableaux), §5 (Figs. 2–8, Tables 4–6), §6.
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §1 (Bolley–Crouzeix barrier, MPRK and DSRK); arXiv v2.
- [Zhu et al. (2024)](/sources/zhu-2024.md) — §1 (Eq. (1.5)), §2.1 (Eqs. (2.2)–(2.3)), §2.2 (Eqs. (2.5)–(2.21), Lemmas 2.1–2.2, Thms. 2.3–2.4), §3.3–3.5 (Eqs. (3.8)–(3.9), Remark 3.1, Thm. 3.3), §4.1 (Tables 1–2, Fig. 1, Remark 4.1), §4.2–4.3, §5; arXiv v1.
- [Izgin et al. (2022)](/sources/izgin-2022.md) — §1, Eq. (6), Thm. 2.9, §3 (Lemmas 3.6, 3.8, 3.10, Cors. 3.9, 3.11), §3.1, §4 (Fig. 4), §5; arXiv v1.
