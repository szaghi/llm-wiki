---
type: Method
title: "TASE operators: time-accurate and highly stable explicit operators"
description: "TASE operators precondition the stiff linear(ized) part of a semi-discrete system with a rational operator built by Richardson extrapolation of the implicit-Euler resolvent, so that an unchanged explicit Runge–Kutta method becomes A-stable or nearly so while keeping its order, at the cost of p linear solves per stage."
status: established
aliases: [TASE, TASE preconditioner, time-accurate and highly-stable explicit operators, RK+TASE]
tags: [stiff, explicit, stability, linear-algebra, runge-kutta]
timestamp: 2026-10-19T20:00:00Z
---

# TASE operators: time-accurate and highly stable explicit operators

A **TASE operator** replaces a stiff semi-discrete system $y'=Ly$ by the modified
system $y'=\mathcal P_p(\vartheta,hL)\,L\,y$, where the preconditioner
$\mathcal P_p$ is a rational function of $hL$ with
$\mathcal P_p=I+\mathcal O(h^p)$. Any explicit integrator is then applied,
unchanged, to the modified system. The modified operator $\mathcal P_pL$ has a
bounded spectrum as $h\to\infty$, so the explicit scheme stays stable at step
sizes far beyond its own limit, and its order is kept when $p$ matches it
([Bassenne et al. (2021)](/sources/bassenne-2021.md), §2.1, Eqs. (4)–(6)).
The method needs no additive splitting of the right-hand side into explicit and
implicit parts, which Bassenne et al. present as its advantage over
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) and
[operator splitting](/methods/operator-splitting.md) (§1).

**Page-local notation.** $\mathcal P_p(\vartheta,hL)$ is the TASE preconditioner of
order $p$ (the source's $T^{(p)}_L(\alpha,\Delta t)$). $\vartheta>0$ is its free
parameter (the source's $\alpha$, renamed because the registry's $\alpha_{ij}$ are
the Shu–Osher coefficients used below). $\omega_{p,k}$ are the closed-form
coefficients (the source's $\beta_{p,k}$). $\rho$ is the length of the
negative-real-axis segment $[-\rho,0]$ contained in the stability region of the
explicit method (the source's $C$). In this page $p$ is the TASE order, not the
order of the Runge–Kutta method.

## Construction

**First order.** Implicit Euler on $y'=Ly$ can be rewritten with the identity
$\big((I-hL)^{-1}-I\big)/h=(I-hL)^{-1}L$ as
$y_{n+1}=y_n+h\,(I-hL)^{-1}Ly_n$, which is explicit Euler applied to
$y'=(I-hL)^{-1}Ly$ (Bassenne et al. (2021), §2.2, Eqs. (7)–(9)). With a parameter
this gives $\mathcal P_1(\vartheta,hL)=(I-\vartheta hL)^{-1}$, of first order
because $(I-\vartheta hL)^{-1}=I+\vartheta hL+\mathcal O(h^2)$.

**Higher order by Richardson extrapolation in $\vartheta$.** Halving the
parameter and extrapolating cancels the leading error term (§2.3, Eq. (10)):

$$\mathcal P_p(\vartheta,hL)=\frac{2^{p-1}\,\mathcal P_{p-1}(\vartheta/2,hL)-\mathcal P_{p-1}(\vartheta,hL)}{2^{p-1}-1},\qquad p\ge2 .$$

The closed forms are (§2.5, Eqs. (14)–(15), Tables 2–3)

$$\begin{aligned}
\mathcal P_p(\vartheta,hL)&=\sum_{k=0}^{p-1}\omega_{p,k}\,\big(2^kI-\vartheta hL\big)^{-1},\\
\mathcal P_p(\vartheta,hL)\,L&=\frac{1}{\vartheta h}\Big[-(2^p-1)I+\sum_{k=0}^{p-1}2^k\omega_{p,k}\,\big(2^kI-\vartheta hL\big)^{-1}\Big],
\end{aligned}$$

with

| $p$ | $\omega_{p,0}$ | $\omega_{p,1}$ | $\omega_{p,2}$ | $\omega_{p,3}$ |
|---|---|---|---|---|
| 1 | $1$ | | | |
| 2 | $-1$ | $4$ | | |
| 3 | $1/3$ | $-4$ | $32/3$ | |
| 4 | $-1/21$ | $4/3$ | $-32/3$ | $512/21$ |

The source tabulates the second set of coefficients separately; they equal
$2^k\omega_{p,k}$. The coefficients satisfy $\sum_k\omega_{p,k}2^{-k}=1$
($\mathcal P_p=I$ at $h=0$) and $\sum_k\omega_{p,k}=2^p-1$, which fixes the
large-step limit below *(compiler check of the printed tables, not stated as
identities in the source)*.

**Cost.** Each evaluation of the modified right-hand side needs $p$ linear solves
with the shifted matrices $2^kI-\vartheta hL$, which are banded for local
spatial operators. $\mathcal P_p$ itself is generally full and is never formed.
For a linear problem the operator form avoids one matrix–vector product; for a
nonlinear one only the preconditioner form applies. The cost per stage is
therefore "at least comparable" to an implicit scheme's, and the gain must come
from larger steps (§2.5).

## Choice of $\vartheta$ and linear stability

Let $R(z)$, $z=h\lambda$, be the [stability function](/definitions/stability-function.md)
of the preconditioned scheme in terms of the *original* eigenvalue $\lambda$.

**Necessary condition (Thm. 2.1).** As $h\to\infty$,
$h\,\mathcal P_p(\vartheta,h\lambda)\lambda=-(2^p-1)/\vartheta+\mathcal O(h^{-1})$
(Eq. (12)). The modified scaled eigenvalue thus tends to a negative real number,
which lies in the explicit method's stability region iff

$$\vartheta\ge\vartheta_{\min}=\frac{2^p-1}{\rho}\qquad\text{(Eq. (11))}.$$

Explicit methods whose stability region meets the real axis only at the origin
are incompatible with a real $\vartheta$ (§2.4). Table 1 of the source gives
$\vartheta_{\min}$ for the $s$-stage, order-$s$ explicit methods:

| explicit method | $\rho$ (printed) | $p=1$ | $p=2$ | $p=3$ | $p=4$ |
|---|---|---|---|---|---|
| RK1 | 2.00 | 0.50 | | | |
| RK2 | 2.00 | 0.50 | 1.50 | | |
| RK3 | 2.50 | 0.40 | 1.20 | 2.80 | |
| RK4 | 2.79 | 0.36 | 1.08 | 2.51 | 5.38 |

The leading error term of $\mathcal P_p$ grows with $\vartheta$, so
$\vartheta=\vartheta_{\min}$ is the recommended choice (§2.3; Fig. 7(b)).

**First-order TASE: proofs.** Explicit Euler on $y'=\mathcal P_1(\vartheta,h\lambda)\lambda y$
is the $\theta$-method with $\theta=\vartheta$,
$R(z)=\big(1+(1-\vartheta)z\big)/(1-\vartheta z)$, which is
[A-stable](/properties/a-stability.md) iff $\vartheta\ge\tfrac12$ (Lemma 3.3,
Eqs. (17)–(18)). Theorem 3.2 transfers this to any explicit Runge–Kutta method
written in Shu–Osher form with $\alpha_{ij}\ge0$, $\beta_{ij}\ge0$: each stage is a
convex combination of TASE–Euler steps with rescaled parameter and eigenvalue
(Lemma 3.4, Eq. (20)), so the method is unconditionally stable if

$$\vartheta\ge\tfrac12\max_{i,j}\frac{\beta_{ij}}{\alpha_{ij}} .$$

This is the convex-combination argument of
[SSP methods](/methods/strong-stability-preserving-runge-kutta.md) with the
TASE–Euler step as building block. For the linear SSP methods up to order 4 the
maximum ratio is 1, so the sufficient value is $\vartheta=0.5$, larger than the
necessary values 0.40 (RK3) and 0.36 (RK4); the authors report that the
necessary value "works well in practice" (§3.1).

**Arbitrary order: analyticity proved, imaginary axis sampled.** For an $s$-stage
method and TASE order $p$, $R=N/D$ with $D(z)=\prod_{i=0}^{p-1}(2^i-\vartheta z)^s$
($N$ page-local), so all poles lie at $z=2^i/\vartheta>0$ and $R$ is analytic in
$\mathbb C^-$ (§3.2, Eqs. (24)–(27)). The second half of the maximum-modulus test,
$\lvert R(iy)\rvert\le1$, is checked by dense sampling only (Fig. 4). Equivalently,
$R(z)=P\big(z\,\mathcal P_p(\vartheta,z)\big)$ with $P$ the explicit method's
stability polynomial, and A-stability holds iff the map
$z\mapsto z\,\mathcal P_p(\vartheta,z)$ sends $\mathbb C^-$ into the stability region
of the explicit method *(compiler reformulation, not in the source)*.

**Results at $\vartheta=\vartheta_{\min}$** (§2.6, §3.2, Figs. 1–4). For
$s$-stage, order-$s$ explicit methods, $s\le4$:

- $p\le2$, $p\le s$: unconditionally stable (A-stable). This is proved for $p=1$
  only under the sufficient condition above and rests on the numerical
  imaginary-axis check for $p=2$.
- $p>2$: "nearly unconditionally stable". Small unstable regions remain near the
  imaginary axis, at eigenvalues whose imaginary part is about a hundred times
  their real part, with $\max\lvert R(iy)\rvert\approx1.02$.
- $\vartheta<\vartheta_{\min}$ (0.25 and 0.5 times the value) opens large unstable
  regions in $\mathbb C^-$ for RK4 with TASE orders 1–4; $\vartheta>\vartheta_{\min}$
  (2 and 4 times) shrinks the residual regions (Fig. 3).

## Using TASE in practice

**Sources and boundary data.** For $y'=Ly+r(t)$ with a source $r$ (page-local;
e.g. inhomogeneous Dirichlet data), the source must be preconditioned with the
operator, $y'=\mathcal P_p(Ly+r)$, so that the steady state $Ly+r=0$ is kept.
Preconditioning only $Ly$ keeps the order but produces large errors that start at
the boundaries (§4.2, Eq. (32), Fig. 8).

**Several stiff operators.** For $L=L_1+L_2$ the combined form
$\mathcal P_p(\vartheta,h(L_1+L_2))(L_1+L_2)y$ is always safe. The split form
$\mathcal P_p(\vartheta,hL_1)L_1y+\mathcal P_p(\vartheta,hL_2)L_2y$ is acceptable only
when the operators are not in a quasi-steady balance at the same location, a
criterion borrowed from splitting practice (§4.3, Eqs. (34)–(35)). In a
two-species advection–diffusion–reaction test with RK3 and third-order TASE, the
split form is accurate when the reaction dies out at the boundary and wrong near
$x=1$ when incompatible boundary data keep it active (Fig. 9).

**Nonlinear problems.** For $y'=f(y)$ the preconditioner is built on the Jacobian
at the current state, $y'=\mathcal P_p(\vartheta,hJ)f(y)$ (Eqs. (42)–(43)), which
is equivalent to applying the source rule above to $f(y)=Jy+(f(y)-Jy)$. Each
stage then needs only linear solves, no nonlinear system. The source says the
Jacobian is evaluated "at every time-step using the current value" of $y$; it
does not say whether it is refreshed at every stage (§4.4.1).

## Numerical evidence

All tests are in Matlab; the order observed is the classical one (§4).

- **Heat equation, over-resolution** (RK2 with second-order TASE, 600 points):
  steps $6.08\times10^3$ times the explicit stability limit, profiles
  indistinguishable to plotting accuracy, second order kept; the error is slightly
  larger than explicit RK2 and larger than SDIRK2 (§4.1.1, Fig. 5).
- **Steady state and quasi-steady stiff physics:** RK4 with fourth-order TASE
  accurate up to 8.07 times the limit; RK2 with second-order TASE captures a slow
  source at 75 times the limit (§4.1.2–4.1.3, Figs. 6–7).
- **Nonlinear power-law diffusion** ($\partial_tu=\partial_x(\tfrac12u^\beta\partial_xu)$,
  $\beta$ page-local, up to 4): RK4 with fourth-order TASE stable and accurate at 9.56
  times the limit (Fig. 10).
- **Scalar decay** $y'=-y^{10}$ to $t=2\times10^4$: RK2 with second-order TASE at
  $10^3$ and $10^4$ times the limit cuts $10^5$ steps to $10^2$ and $10$, stable
  and second order (§4.4.3, Fig. 11).
- **Polar-coordinate diffusion:** TASE applied to the azimuthal operator alone
  removes the pole-induced step restriction (50 times the azimuthal limit) where
  the explicit solution blows up (§4.5, Fig. 12; qualitative only).

**Cost per step** (Tables 4–5; hardware not stated). With precomputed inverses,
RK with TASE is "in general slightly better" than SDIRK of the same order; with
on-the-fly sparse solves it is more expensive, since TASE needs $p$ solves per
stage against one for SDIRK. On nonlinear diffusion ($\beta=4$), RK with TASE costs
2.1–40 ms per step, SDIRK with Matlab's nonlinear solver 237–1303 ms, plain RK
0.6–1.5 ms. See [DIRK methods](/methods/diagonally-implicit-runge-kutta.md) and
[implicit stage solvers](/methods/implicit-stage-solvers.md).

## Relation to other methods

RK with TASE on a linear or linearized problem is a linearly implicit one-step
method: every stage solves linear systems with shifted Jacobians, and the
nonlinear version freezes the Jacobian at the step start. It thus belongs to the
same family as [Rosenbrock–Wanner and W-methods](/methods/rosenbrock-wanner-method.md),
with $p$ distinct matrices $2^kI-\vartheta hL$, i.e. diagonal coefficients
$\vartheta/2^k$, instead of one diagonal coefficient $\gamma$. Since $\mathcal P_p=I+\mathcal O(h^p)$ for any bounded $L$, its
nonstiff order does not depend on $L$ being the exact Jacobian, as for a
W-method *(compiler remark; Bassenne et al. make neither connection)*.

## Qualifications

- **Order under stiffness is not analysed.** The order claim rests on
  $\mathcal P_p=I+\mathcal O(h^p)$, a nonstiff expansion whose constant grows with
  powers of $\lVert hL\rVert$, while TASE is used exactly where
  $\lVert hL\rVert\gg1$. The source states it as "straightforward" without proof
  and does not study [order reduction](/definitions/order-reduction.md); its
  tests show the expected slopes in the asymptotic range *(compiler check, not in the sources)*.
- **Stability analysis by eigenvalues.** §3 assumes diagonalizable $L$. For
  non-normal $L$ (advection, boundary closures) A-stability does not by itself
  bound $\lVert R(hL)\rVert$; see [strong stability](/properties/strong-stability.md)
  *(compiler check, not in the sources)*.
- **Theorem 3.2 for RK4.** No four-stage fourth-order Runge–Kutta method has a
  non-negative Shu–Osher form for nonlinear problems. The argument uses a
  linear-SSP realization of the stability polynomial $\sum_{j\le4}z^j/j!$, valid
  only for linear constant-coefficient problems; the phrase "the case for most RK
  methods including $s$-stages $s$th-order with $s\le4$" glosses over this
  *(compiler check, not in the sources)*.
- **Rounded $\rho$.** The negative-real intercepts are $\rho\approx2.5127$ (RK3)
  and $\rho\approx2.7853$ (RK4). The printed 2.79 for RK4 is rounded up, so the
  printed $\vartheta_{\min}$ for $p=3,4$ (2.51, 5.38) lie slightly below the exact
  thresholds 2.513 and 5.385 *(compiler check, not in the sources)*. Whether this contributes to the
  $\max\lvert R(iy)\rvert\approx1.02$ reported for RK4 with $p=3,4$ is not known.
- **Printed slips** (arXiv v2): the proof of Thm. 3.2 cites a nonexistent
  "lemma 3.2" for Lemma 3.3; §4.5 names RK4 as the baseline while the caption of
  Fig. 12 says RK2; §4.4.3 calls the scalar ODE a PDE.

# Citations

- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §1; §2.1–2.6 (Eqs. (4)–(15), Thm. 2.1, Tables 1–3, Figs. 1–3); §3 (Def. 3.1, Lemmas 3.3–3.4, Thm. 3.2, Eqs. (16)–(27), Fig. 4); §4.1–4.5 (Figs. 5–12, Tables 4–5); §5.
