---
type: Method
title: "TASE operators: time-accurate and highly stable explicit operators"
description: "TASE operators precondition the stiff linear(ized) part of a semi-discrete system with a rational operator, a weighted sum of shifted implicit-Euler resolvents, so that an unchanged explicit Runge–Kutta method becomes A-stable or nearly so while keeping its order; with an inexact Jacobian its linear stability is decided by stability diagrams and generalized eigenvalues."
status: established
aliases: [TASE, TASE preconditioner, time-accurate and highly-stable explicit operators, RK+TASE, TASE-RK, TRK]
tags: [stiff, explicit, stability, linear-algebra, runge-kutta]
timestamp: 2026-10-19T23:00:00Z
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

## Other operator families and inexact Jacobians

**The Calvo–Montijano–Rández family.** [Conte et al. (2024)](/sources/conte-2024.md)
use the TASE operators of Calvo, Montijano and Rández,

$$\mathcal P_p(\boldsymbol\vartheta,hL)=\sum_{j=1}^p\varpi_j\,(I-\vartheta_jhL)^{-1},\qquad
\varpi_j=\frac{\vartheta_j^{-(p-1)}}{\prod_{l\ne j}\big(\vartheta_j^{-1}-\vartheta_l^{-1}\big)},$$

with free shifts $\vartheta_j>0$ and weights $\varpi_j$ fixed by
$\mathcal P_p=I+\mathcal O(h^p)$ (page-local $\vartheta_j$, $\varpi_j$; the source's
$\omega_j$, $\beta_j$; §2, Eqs. (2.1)–(2.2)). Bassenne et al.'s operator above is the
special case $\vartheta_j=\vartheta/2^{j-1}$, $\varpi_j=\omega_{p,j-1}/2^{j-1}$ (reader's
check on Conte et al., verified for $p=2$, where $(\vartheta,\vartheta/2)$ gives
$\varpi=(-1,2)$). The shifts used (Table 1, from Calvo et al.) are $(3,\,1.5)$ for $p=2$,
$(2.3147,\,1.8796,\,1.5822)$ for $p=3$ and $(3.9396,\,2.4506,\,2.2271,\,2.0612)$ for
$p=4$. The $p=2$ choice is Bassenne's family with $\vartheta=3$, twice the
$\vartheta_{\min}=1.5$ of RK2 in the table above *(compiler check, not in the
sources)*. With these shifts and the exact Jacobian, the $p$-stage, order-$p$ methods
TRK$p$ are, as recalled by Conte et al. from Calvo et al.: TRK2 strongly A-stable with
$R(\infty)=0.5$; TRK3 L($\theta$)-stable with $\theta=89.02^\circ$; TRK4 strongly
A($\theta$)-stable with $\theta=87.34^\circ$ and $R(\infty)=0.27$ (§2, Table 1). The
value $R(\infty)=0.5$ for TRK2 agrees with the large-step limit
$h\,\mathcal P_2\lambda\to-1$ and $P(-1)=\tfrac12$ *(compiler check)*.

**TASE–Runge–Kutta with an arbitrary matrix.** In practice the Jacobian $J$ inside
$\mathcal P_p$ is replaced by a cheap matrix $\tilde J$ (page-local; constant, symmetric
negative definite, factorized once). Conte et al. write the method as

$$Y_i=y_n+h\sum_{j<i}a_{ij}\,\mathcal P_p(h\tilde J)\,f(t_n+c_jh,Y_j),\qquad
y_{n+1}=y_n+h\sum_ib_i\,\mathcal P_p(h\tilde J)\,f(t_n+c_ih,Y_i)$$

(Eq. (2.3); the source calls the Butcher matrix $\alpha$ because $A$ is its inexact
Jacobian). The order $p$ is kept for any $\tilde J$, because
$\mathcal P_p=I+\mathcal O(h^p)$ holds for any matrix (§1, Remark 2.1). Stability is
another matter: every earlier analysis assumed $\tilde J=J$, and an arbitrary $\tilde J$
carries "a concrete risk of running into instability issues" (§1).

**Splitting test equation and stability diagrams** (§3). Write $J=\tilde J+E$
(page-local remainder $E$; the source's $B$) and test on $y'=(\lambda+\lambda_E)y$ with
$\lambda<0$ an eigenvalue of $\tilde J$ and $\lambda_E$ one of $E$. With $\mu=\lambda_E/\lambda$,
$x=h\lambda<0$ and the scalar map $\hat{\mathcal P}_p(x)=x\,\mathcal P_p(x)$ (page-local
symbols), the stability function of TRK$p$, $p\le4$, is

$$\tilde R(x,\mu)=P\big(\hat{\mathcal P}_p(x)\,(1+\mu)\big),\qquad P(z)=\sum_{j=0}^p\frac{z^j}{j!}$$

(Eq. (3.4)). $\hat{\mathcal P}_p$ increases on $x<0$ from its limit
$\hat{\mathcal P}_p^*$ to 0, with $\hat{\mathcal P}_2^*\approx-1$ and
$\hat{\mathcal P}_3^*\approx\hat{\mathcal P}_4^*\approx-1.5961$ (Fig. 1). The
**stability diagram** $\mathcal D_{x,p}=\{\mu\in\mathbb C:\lvert\tilde R(x,\mu)\rvert\le1,\ \operatorname{Re}\mu\ge-1\}$
(page-local; Def. 3.2) satisfies

$$\mathcal D_{x,p}=-1+\hat{\mathcal P}_p(x)^{-1}\,\mathcal S_p$$

(Lemma 3.4), with $\mathcal S_p$ the explicit method's
[stability region](/definitions/stability-function.md) restricted to
$\operatorname{Re}z\le0$: a homothety by a negative factor, hence a rotation by
$180^\circ$, followed by a shift. The diagrams are nested,
$\mathcal D_{x_1,p}\subseteq\mathcal D_{x_2,p}$ for $x_1<x_2<0$, so the limit
$\mathcal D_{\infty,p}$ is the smallest one, the **unconditional diagram** (Thm. 3.6,
Rem. 3.7; proof by star-shapedness of $\mathcal S_p$).

**Conditions for stability** (§4–5). Let $\mu(\tilde J,E)$ denote the generalized
eigenvalues, the spectrum of $\tilde J^{-1}E$ (page-local), and $\lambda_1$ the most
negative eigenvalue of $\tilde J$.

- *$\tilde J$, $E$ simultaneously diagonalizable.* Stable at step $h$ iff each paired
  ratio $\mu_i\in\mathcal D_{h\lambda_i,p}$ (Prop. 4.1); sufficient, without pairing:
  $\mu(\tilde J,E)\subseteq\mathcal D_{h\lambda_1,p}$ (Thm. 4.3); unconditionally stable iff
  $\mu(\tilde J,E)\subseteq\mathcal D_{\infty,p}$ (Thm. 4.5). On the real axis the
  thresholds are $\mu\le1$ for $p=2$ (with a closed-form step bound beyond it),
  $\mu\le0.5743$ for $p=3$ and $\mu\le0.7445$ for $p=4$ (Rem. 4.2).
- *General case, $\tilde J$ symmetric negative definite.* Stable iff the spectrum of
  $h\,\mathcal P_p(h\tilde J)(\tilde J+E)$ lies in $\mathcal S_p$ (Thm. 5.3). Sufficient:
  some weighted field of values
  $\mathcal W_r(-\tilde J,E)=\{\langle v,(-\tilde J)^{r-1}Ev\rangle:\langle v,(-\tilde J)^rv\rangle=1\}$,
  $r\in\mathbb R$ (page-local; the technique of Rosales, Seibold, Shirokoff and Zhou for
  IMEX multistep methods), lies in $-\mathcal D_{h\lambda_1,p}$ (Thm. 5.5), or in
  $-\mathcal D_{\infty,p}$ for unconditional stability; conversely, unconditional
  stability requires $\mu(\tilde J,E)\subseteq\mathcal D_{\infty,p}$, so one generalized
  eigenvalue outside the unconditional diagram rules it out (Thm. 5.6).
- *Scaling.* Replacing $\tilde J$ by $\kappa\tilde J$ (page-local $\kappa>0$) maps
  $\mu(\kappa\tilde J,J-\kappa\tilde J)=-1+\kappa^{-1}\mu(\tilde J,J)$, so a suitable
  $\kappa$ can restore unconditional stability (Rem. 5.7, after Seibold et al.).

**Evidence** (Matlab, §4–7). On a $3\times3$ commuting test with
$\operatorname{spec}\tilde J=\{-100,-10,-1\}$ and $\mu=(\tfrac12,\tfrac65,\tfrac32)$ the
sharp step bounds are $0.78390$ (TRK2) and $0.28428$ (TRK3), set by the eigenvalue
$-10$ rather than the most negative one; above them the errors blow up (TRK3:
$1.39\times10^{16}$ at $h=0.46875$), while with the exact Jacobian both methods are
stable at every step tried (Table 2, Fig. 4). Theorem 4.3 alone would force a step ten
times smaller (Rem. 4.4). On viscous [Burgers](/benchmarks/burgers-equation.md) with
$\tilde J=\kappa(\epsilon L_\Delta-2I)$ (page-local $\epsilon$ viscosity, $L_\Delta$ the
discrete second derivative): for $\epsilon=0.1$, $\kappa=1$ all TRK$p$ are unconditionally
stable; for $\epsilon=0.01$, $\kappa=1$ the generalized eigenvalues
$-0.4875\pm3.4130\,\mathrm i$ fall outside $\mathcal D_{\infty,p}$ and TRK2 is unstable at
$h=0.5$, while $\kappa=3$ restores unconditional stability (§7.1, Figs. 7–8). On the
[FitzHugh–Nagumo model](/benchmarks/fitzhugh-nagumo-model.md) with $\kappa=1.2$ all
TRK$p$ are unconditionally stable (§7.2, Fig. 9). In error against CPU time, TASE–RK with
a constant matrix is "much more efficient" than Rosenbrock ROS2–ROS4 of the same order
with the exact Jacobian on both PDEs. For nonlinear reactions a mean-value linearization
gives only a heuristic criterion; for a Fisher–Kolmogorov equation the weighted field of
values is bounded explicitly and all TRK$p$ are unconditionally stable (§6, Prop. 6.1).

## Relation to other methods

RK with TASE on a linear or linearized problem is a linearly implicit one-step
method: every stage solves linear systems with shifted Jacobians, and the
nonlinear version freezes the Jacobian at the step start. It thus belongs to the
same family as [Rosenbrock–Wanner and W-methods](/methods/rosenbrock-wanner-method.md),
with $p$ distinct matrices $2^kI-\vartheta hL$, i.e. diagonal coefficients
$\vartheta/2^k$, instead of one diagonal coefficient $\gamma$. Since $\mathcal P_p=I+\mathcal O(h^p)$ for any bounded $L$, its
nonstiff order does not depend on $L$ being the exact Jacobian, as for a
W-method *(compiler remark; Bassenne et al. make neither connection)*. Conte et al.
(2024) state the connection, citing González-Pinto et al. (2023): TASE–RK methods are a
subclass of W-methods, whose order holds for any matrix in place of the Jacobian (§1,
Remark 2.1). They claim theirs is the first in-depth stability study of a subclass of
W-methods with an inexact Jacobian "using the techniques that we employ" (§1.1).

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
- **Spectral radius as stability criterion** (Conte et al. 2024). Their Definition 3.1
  asks for $\lVert y_n\rVert$ bounded independently of $h$ and $n$, while Theorem 5.3
  equates it with a spectral-radius condition; for non-normal amplification matrices
  $\rho\le1$ does not bound the powers uniformly (reader's check on the source; Remark 6.2
  of the source concedes a norm-dependent statement).
- **W-method literature** (Conte et al. 2024, §7): the statement that inexact-Jacobian
  Rosenbrock methods have "no study on the related stability properties" is unqualified;
  their own reference list includes W-method and approximate-factorization papers that
  analyse stability with approximate Jacobians (reader's note on the source).
- **Printed values** (Conte et al. 2024, arXiv v1): the reader of the source computes
  $\mu^*_4=0.7451$ from the printed formula against the printed $0.7445$ ($\mu^*_3=0.5743$
  reproduces); Eq. (5.3) raises the amplification matrix to the power $n+1$ and applies it
  to $y_n$ instead of $y_0$. The analysis covers only $s=p\le4$ and the tabulated shifts.
- **Printed slips** (arXiv v2): the proof of Thm. 3.2 cites a nonexistent
  "lemma 3.2" for Lemma 3.3; §4.5 names RK4 as the baseline while the caption of
  Fig. 12 says RK2; §4.4.3 calls the scalar ODE a PDE.

# Citations

- [Conte et al. (2024)](/sources/conte-2024.md) — §1–1.1, §2 (Eqs. (2.1)–(2.4), Table 1, Remark 2.1), §3 (Def. 3.2, Eq. (3.4), Lemma 3.4, Thm. 3.6, Fig. 1), §4 (Prop. 4.1, Rem. 4.2, Thms. 4.3, 4.5, Table 2, Fig. 4), §5 (Thms. 5.3, 5.5, 5.6, Rem. 5.7), §6 (Prop. 6.1, Remark 6.2), §7 (Figs. 7–9).
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §1; §2.1–2.6 (Eqs. (4)–(15), Thm. 2.1, Tables 1–3, Figs. 1–3); §3 (Def. 3.1, Lemmas 3.3–3.4, Thm. 3.2, Eqs. (16)–(27), Fig. 4); §4.1–4.5 (Figs. 5–12, Tables 4–5); §5.
