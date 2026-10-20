---
type: Property
title: "Strong stability (monotonicity) of Runge–Kutta methods for linear seminegative problems"
description: "A one-step method is strongly stable on $y'=Ly$ with $\\langle Lv,v\\rangle\\le0$ if $\\lVert y_{n+1}\\rVert\\le\\lVert y_n\\rVert$; for non-normal $L$ eigenvalue analysis cannot decide it, energy-method criteria can, explicit Taylor-type methods fail for $p\\equiv1,2\\pmod4$, and the property differs from SSP."
status: established
aliases: [monotonicity, monotonicity-preserving, monotonicity stability, contractivity in an inner-product norm, L2 stability, weak(kappa) stability]
tags: [stability, strong-stability, runge-kutta, structure-preserving, explicit, implicit]
timestamp: 2026-10-20T16:00:00Z
---

# Strong stability (monotonicity) of Runge–Kutta methods for linear seminegative problems

Let $V$ be a real Hilbert space with inner product $\langle\cdot,\cdot\rangle$ and
norm $\lVert\cdot\rVert$, and let $L$ be a bounded linear operator on $V$, not
necessarily normal, that is **seminegative**: $\langle Lv,v\rangle\le0$ for all $v$.
The solution of $y'=Ly$ then satisfies the energy law

$$\frac{d}{dt}\lVert y\rVert^2=-\lvert y\rvert_L^2\le0,\qquad [v,w]_L:=-\langle Lv,w\rangle-\langle v,Lw\rangle,\quad \lvert v\rvert_L:=\sqrt{[v,v]_L},$$

with $[\cdot,\cdot]_L$ a semi-inner product and $\lvert\cdot\rvert_L$ the dissipation
semi-norm (page-local symbols; [Sun et al. 2022](/sources/sun-2022.md), §1, Eqs.
(1.2)–(1.3)). A Runge–Kutta method, applied as $y_{n+1}=R(hL)y_n$ with $R$ its
[stability function](/definitions/stability-function.md), is **strongly stable** if

$$\lVert y_{n+1}\rVert\le\lVert y_n\rVert,$$

possibly under a step restriction $h\lVert L\rVert\le c_0$, and **unconditionally
strongly stable** if this holds for all $h\ge0$ (Sun et al. 2022, §1, Eq. (3.12);
[Sun & Shu 2021](/sources/sun-2021.md), §1, Eq. (1.3)). The ODE literature calls the
same property monotonicity, monotonicity-preserving or contractivity; Xu and
coauthors call it monotonicity stability (Sun et al. 2022, §1). Strong stability is
the discrete form of the entropy inequality for the square entropy (Sun & Shu 2021,
§1). Weaker notions:

- **weak stability**, $\lVert y_{n+1}\rVert\le(1+Ch)\lVert y_n\rVert$, which only gives
  $\lVert y_n\rVert\le e^{Ct_n}\lVert y_0\rVert$ (Sun & Shu 2021, §1);
- **weak($\kappa$) stability**,
  $\lVert y_{n+1}\rVert^2\le\bigl(1+C(h\lVert L\rVert)^\kappa\bigr)\lVert y_n\rVert^2$
  for $h\lVert L\rVert\le c_0$, which yields the exponential bound only if
  $h\lVert L\rVert^{1+1/(\kappa-1)}\le c_0$ (Sun et al. 2022, Thm. 3.7(1)).

## Why eigenvalues are not enough

For normal $L$, strong stability on $y'=Ly$ reduces to $\lvert R(h\lambda)\rvert\le1$
on the spectrum. For non-normal $L$, eigenvalue (test-equation) analysis is only
necessary: it "may sometimes give misleading conclusions on the time step constraint
or the stability property" (Sun et al. 2022, §1; Sun & Shu 2021, §1). A-stability does
suffice in the unconditional case: an [A-stable](/properties/a-stability.md) method is
strongly stable for every seminegative $L$ in an inner-product norm, by von Neumann's
lemma, as recalled by Sun et al. (2022, §1, citing Hairer–Wanner II §IV.11); so are the
stability functions of algebraically stable methods. The conditional case, which is
the case of every explicit method, needs the
[energy method](/methods/runge-kutta-energy-method.md).

The standard counterexample is the non-normal matrix

$$L=-\begin{pmatrix}1&2&2\\0&1&2\\0&0&1\end{pmatrix},$$

whose eigenvalues are all $-1$, yet on which the $p$-stage, order-$p$ explicit methods
with $p=1,2,4$ increase the norm for every small $h$ tested (Sun & Shu 2021, §6.1.1,
Table 6.3); Sun et al. (2022, Ex. 6.1) use the same matrix.

## Criteria from the energy identity

The energy method writes $\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2$ as a diagonal part
$\sum_k\eta_kh^{2k}\lVert L^kw_n\rVert^2$ plus a quadratic form with matrix
$\Upsilon=(\upsilon_{ij})$ in the semi-inner products $[L^iw_n,L^jw_n]_L$, with
$w_n=D(hL)^{-1}y_n$ for $R=N/D$ (page-local; derivation on
[energy method](/methods/runge-kutta-energy-method.md)). Let $\zeta$ be the index of the
first nonzero $\eta_k$ (Sun & Shu's *leading index* $k^*$) and $\rho$ the largest order
of a negative-semidefinite leading principal submatrix of $\Upsilon$ (page-local). Sun,
Wei & Wu prove (Sun et al. 2022, Thms. 3.5, 3.7):

1. if $\mathrm{diag}(\eta_k)\le0$ and $\Upsilon\le0$ (negative semidefinite), the
   method is **unconditionally** strongly stable;
2. with $\kappa=\min\{2\zeta,2\rho+1\}$, the method is weakly($\kappa$) stable;
3. if $\zeta\le\rho$ and $\eta_\zeta<0$, it is strongly stable for
   $h\lVert L\rVert\le c_0$;
4. if $\eta_\zeta>0$, it is **not** strongly stable in general: a skew $L$
   ($L^\top=-L$) exists with $\lVert R(hL)\rVert>1$ for all $h\lVert L\rVert\in(0,c_0]$.

The constants depend only on the coefficients of $R$. Part 4 works because a skew
operator makes $[\cdot,\cdot]_L$ vanish, so only the diagonal part survives (Sun et
al. 2022, Thm. 3.7(3); the same device proves Sun & Shu 2021, Thm. 3.2). For
semi-discrete hyperbolic problems $\lVert L\rVert=O(\Delta x^{-1})$: strong stability
then needs $h\le C\Delta x$, and weak($\kappa$) stability with an exponential bound
needs $h\le C\Delta x^{1+1/(\kappa-1)}$ (Sun et al. 2022, Remark 3.8).

## Explicit methods

For the $p$-stage, order-$p$ linear methods $R(z)=\sum_{j=0}^pz^j/j!$, Sun & Shu's
earlier energy analysis gives: **not strongly stable if $p\equiv1$ or $2\pmod4$,
strongly stable if $p\equiv3\pmod4$**, as recalled by both Sun & Shu (2021, §1) and Sun
et al. (2022, §1). For odd $p$ the leading index is $\zeta=(p+1)/2$ and the leading
$\zeta\times\zeta$ block of $\Upsilon$ is negative definite; for even $p$,
$\zeta=p/2+1$ and the block of order $p/2$ is negative definite (Sun & Shu 2021, Prop.
2.2). The leading coefficients are $\eta_\zeta=1,\frac14,
-\frac1{12},-\frac1{72},\frac1{360},\frac1{2880}$ for $p=1,\dots,6$: they equal
$-2\mu_2^0$ for the critical diffusive coefficients $\mu_2^0$ of Sun & Shu's Table 6.1
(page-local, as on [superviscosity](/methods/superviscosity-stabilized-runge-kutta.md)), and the lowest
coefficient of $\lvert R(\mathrm iy)\rvert^2-1$ *(compiler check, not in the sources;
see Qualifications)*. Hence forward Euler ($p=1$), $p=2$, $p=5$ and $p=6$ fail by part 4.
Classical RK4 ($p=4$) has $\eta_\zeta<0$ but still fails on the non-normal test matrix
(Sun & Shu 2021, Table 6.3): its failure comes from the quadratic form, which is why
the remedy of Sun & Shu needs a positive dispersive correction for even $p$ (critical
value $\frac1{144}>0$ at $p=4$; Sun & Shu 2021, Thm. 3.1, Table 6.1). RK4 is thus
not strongly stable in general, although the recalled mod-4 statement leaves
$p\equiv0\pmod4$ open.

## Implicit methods

Sun et al. (2022, §4–5) apply the criteria to rational stability functions directly:

| Method | Outcome | Locator |
|---|---|---|
| Backward Euler | unconditional: $-h^2\lVert Ly_{n+1}\rVert^2-h\lvert y_{n+1}\rvert_L^2$ | Ex. 4.1 |
| Crank–Nicolson / implicit midpoint | unconditional: $-h\lvert w_n\rvert_L^2$ | Ex. 4.2 |
| Qin–Zhang two-stage symplectic DIRK | unconditional: $-h\lvert w_n\rvert_L^2-\frac1{16}h^3\lvert Lw_n\rvert_L^2$ | Ex. 4.3 |
| Kraaijevanger–Spijker two-stage DIRK | unconditional | Ex. 4.4 |
| (0,3) Padé approximation (A($\alpha$)-stable) | $\zeta=\rho=2$, $\eta_2=\frac1{12}>0$: weakly(4) stable, not strongly stable | Ex. 4.5 |
| (4,1) Padé approximation | $\zeta=\rho=3$, $\eta_3=-\frac1{1800}<0$: conditionally strongly stable | Ex. 4.6 |
| all diagonal $(m,m)$ Padé approximations | unconditional, with an explicit energy law | Thms. 5.1–5.2 |

The diagonal Padé result, which covers the [Gauss methods](/methods/fully-implicit-runge-kutta.md),
is on [diagonal Padé strong stability](/results/diagonal-pade-strong-stability.md).

## Restoring strong stability

Two families of remedies modify an explicit method that is not strongly stable:
[superviscosity](/methods/superviscosity-stabilized-runge-kutta.md), which adds a
high-order dissipative (and, for even $p$, dispersive) term to the operator or as a
post-step filter (Sun & Shu 2021), and relaxation Runge–Kutta, which rescales the
update to enforce the energy law and is cited by both sources as the alternative
(Sun & Shu 2021, §1, §5; Sun et al. 2022, §1). Sun & Shu's adaptive filter of §5 is
modelled on the relaxation procedure.

## Nonlinear problems: third-order RKDG on Burgers

The theory above is linear. [Wei & Shu (2026)](/sources/wei-2026.md) obtain
$\lVert u^{n+1}\rVert\le\lVert u^n\rVert$ for a **nonlinear** problem, explicit
discontinuous Galerkin for Burgers' equation, as the sum of a cell-by-cell square-entropy
inequality, under $h\le C\Delta x$ and for periodic or compactly supported data (§1, §3).
It holds for $P^2$ and $P^3$ elements and the explicit three-stage third-order methods with
$c_3=a_{31}+a_{32}=1$ and positive weights, Kutta's method among them, and for $P^1$ and any
strictly convex flux extending to an entire function (Thms. 3, 5, A.2). The proof starts
from the same Runge–Kutta energy identity as the [energy method](/methods/runge-kutta-energy-method.md),
$\lVert u^{n+1}\rVert^2-\lVert u^n\rVert^2=2h\sum_ib_i\langle Y_i,f(Y_i)\rangle+h^2\sum_{i,l}b_i(b_l-2a_{il})\langle f(Y_i),f(Y_l)\rangle$,
and splits the quadratic form exactly into two negative squares of first temporal
differences and a positive square of a second difference (Thm. 1). On linear problems all
three-stage third-order methods coincide and give the inequality for every $P^k$
(Remark 1), in line with the strong stability of the third-order Taylor polynomial
recalled above. The class excludes SSP-RK3, and the authors' companion counterexample shows
that RKDG with $P^2$ and a class of third-order methods including SSP-RK3 is not $L^2$ stable
on Burgers under $h\sim\Delta x$ (§1). See
[fully discrete cell entropy inequality](/results/fully-discrete-cell-entropy-inequality.md).

## Relation to SSP

The two notions share the words "strong stability" and are distinct.
[Strong stability preservation](/methods/strong-stability-preserving-runge-kutta.md)
assumes that forward Euler is contractive for a convex functional up to
$h_{\mathrm{FE}}$ and proves $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for
$h\le\mathcal Ch_{\mathrm{FE}}$, for nonlinear $f$ and any convex functional. Strong
stability, as here, is a property of the method on linear seminegative operators in
an inner-product norm, with no forward Euler hypothesis. For coercive $L$ the forward
Euler hypothesis holds and SSP theory proves that every linear Runge–Kutta method is
strongly stable (Gottlieb–Shu–Tadmor, as recalled by Sun & Shu 2021, §1). For merely
seminegative $L$ (energy-conserving or weakly dissipative semi-discretizations such as
central or skew operators) forward Euler is never contractive, SSP theory says
nothing, and strong stability must be checked by the energy method (Sun et al. 2022,
§1). Sun & Shu (2021, §1) and the SSP literature also use "contractivity" for this
property, which in the implicit setting connects to B- and
[algebraic stability](/properties/a-stability.md).

## Qualifications

- **Printed $\eta_\zeta$ formulas.** Sun & Shu (2021, arXiv v1, Prop. 2.2(3)) print
  $\eta_\zeta=(-1)^{(p+1)/2}/(p+1)!$ for odd $p$ and
  $(-1)^{p/2+1}/(p!(p+2))$ for even $p$. These disagree with the paper's own Table 6.1
  and with the critical diffusive coefficient $-\eta_\zeta/2$ of Thm. 3.1; the values consistent with Table 6.1
  are $2(-1)^{(p-1)/2}/(p+1)!$ (odd $p$) and $2(-1)^{p/2+1}/(p!(p+2))$ (even $p$)
  *(compiler check, not in the sources: symbolic expansion of
  $\lvert R(\mathrm iy)\rvert^2-1$ for $p\le6$)*. A printed slip, not a disagreement.
- The criteria of Sun et al. (2022) are sufficient conditions stated through the
  coefficients of $R$; they cover autonomous linear problems with bounded $L$ only.
- Sun et al. (2022, §1) recall the explicit-method result as "strongly stable if
  $p\equiv3\pmod4$, not strongly stable if $p\equiv1,2\pmod4$", silent on
  $p\equiv0\pmod4$; the RK4 failure above is shown numerically by Sun & Shu (2021),
  not proved in either source.

# Citations

- [Sun et al. (2022)](/sources/sun-2022.md) — §1 (definitions, von Neumann lemma, A-stability, SSP contrast), Lemma 3.6, Thms. 3.5, 3.7, Remark 3.8, §4 Exs. 4.1–4.6, Thms. 5.1–5.2, Ex. 6.1.
- [Sun & Shu (2021)](/sources/sun-2021.md) — §1 (Eq. 1.3, weak stability, recalled explicit results, coercive case), Def. 2.1, Props. 2.1–2.2, Thms. 3.1–3.2, §5, §6.1.1 (Tables 6.1, 6.3).
- [Wei & Shu (2026)](/sources/wei-2026.md) — §1, §2 (Eq. (13)), §3 (Thm. 1, Remark 1, Thms. 3, 5), App. A (Thm. A.2); author manuscript.
