---
type: Method
title: "Multiderivative Runge–Kutta methods and the backward derivative condition"
description: "Runge–Kutta methods that also use higher time derivatives of the solution ($\\dot f=f'f$ and beyond): implicit two-derivative ones with nonpositive $\\dot f$ coefficients are SSP for every step at orders 2–4, explicit $r$-derivative ones are made Jacobian-free for conservation laws by approximate Taylor fluxes, and implicit Hermite–Birkhoff ones are discretized with an auxiliary variable."
status: established
aliases: [two-derivative Runge–Kutta, MDRK, SSP-iMDRK, implicit Taylor method, SSP IMEX multiderivative Runge–Kutta, explicit multiderivative Runge–Kutta, rDRKq-s, MDRKCAT, Jacobian-free multiderivative Runge–Kutta, compact approximate Taylor method, CAT, Taylor method, two-derivative Hermite–Birkhoff Runge–Kutta, HBRK, two-point Hermite rule, Obreshkov rule]
tags: [multiderivative, ssp, implicit, imex, asymptotic-preserving, order-conditions, lax-wendroff]
timestamp: 2026-10-20T16:00:00Z
---

# Multiderivative Runge–Kutta methods and the backward derivative condition

A **two-derivative Runge–Kutta method** for the autonomous problem $y'=f(y)$ uses, besides
$f$, the second time derivative of the solution $\dot f(y)=f'(y)f(y)$:

$$Y_i=y_n+h\sum_{j=1}^{i}a_{ij}f(Y_j)+h^2\sum_{j=1}^{i}\dot a_{ij}\dot f(Y_j),\quad i=1,\dots,s,\qquad y_{n+1}=Y_s,$$

so the weights are the last rows, $b_j=a_{sj}$, $\dot b_j=\dot a_{sj}$, and the
method is stiffly accurate by construction; $c=A\mathbf 1$ and, page-local,
$\dot c=\dot A\mathbf 1$ ([Gottlieb et al. 2022](/sources/gottlieb-2022.md), §2.1,
Eqs. (8)–(9), the class of Christlieb–Gottlieb–Grant–Seal). Gottlieb, Grant, Hu &
Shu use the lower-triangular (diagonally implicit) case. The page records their
contribution: strong stability preservation without a step restriction from the
implicit operator, which no implicit [Runge–Kutta method](/definitions/runge-kutta-method.md)
achieves beyond first order.

Three further strands use the class. Explicit methods with up to four derivatives are made
practical for conservation laws by replacing exact flux derivatives with finite
differences in time ([Chouchoulis et al. 2022](/sources/chouchoulis-2022.md)); implicit
two-derivative Hermite–Birkhoff methods, reached by
[deferred correction](/methods/deferred-correction.md), are coupled to DG with an auxiliary
variable for $\dot f$ ([Zeifang & Schütz 2022](/sources/zeifang-2022.md)); and the
one-stage Taylor member is the time discretization of
[Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)
([Babbar et al. 2022](/sources/babbar-2022.md)). The sections below take them in turn.

## Order conditions

Through order 4 (Gottlieb et al. 2022, §2.1; recalled up to order 6 from Christlieb
et al.), with products of vectors componentwise:

| $p$ | conditions |
|---|---|
| 1 | $b^\top\mathbf 1=1$ |
| 2 | $b^\top c+\dot b^\top\mathbf 1=\frac12$ |
| 3 | $b^\top c^2+2\dot b^\top c=\frac13$; $\ b^\top Ac+b^\top\dot c+\dot b^\top c=\frac16$ |
| 4 | $b^\top c^3+3\dot b^\top c^2=\frac14$; $\ b^\top(c\,Ac)+b^\top(c\,\dot c)+\dot b^\top c^2+\dot b^\top Ac+\dot b^\top\dot c=\frac18$; $\ b^\top Ac^2+2b^\top\dot Ac+\dot b^\top c^2=\frac1{12}$; $\ b^\top A^2c+b^\top A\dot c+b^\top\dot Ac+\dot b^\top Ac+\dot b^\top\dot c=\frac1{24}$ |

## SSP conditions on the second derivative

All conditions refer to a convex functional $\lVert\cdot\rVert$ and the
forward Euler condition $\lVert y+hf(y)\rVert\le\lVert y\rVert$ for $h\le
h_{\mathrm{FE}}$ (see [SSP methods](/methods/strong-stability-preserving-runge-kutta.md)).
Three conditions on $\dot f$ appear in Gottlieb et al. (2022, §1), with page-local
positive constants:

- **second derivative condition** (earlier work, explicit methods):
  $\lVert y+h^2\dot f(y)\rVert\le\lVert y\rVert$ for $h^2\le\tilde kh_{\mathrm{FE}}^2$
  (Eq. (4));
- **Taylor series condition** (earlier work):
  $\lVert y+hf(y)+\frac12h^2\dot f(y)\rVert\le\lVert y\rVert$ for $h\le\hat kh_{\mathrm{FE}}$
  (Eq. (5));
- **backward derivative condition** (new):
  $\lVert y-h^2\dot f(y)\rVert\le\lVert y\rVert$ for $h^2\le\dot kh_{\mathrm{FE}}^2$
  (Eq. (6)), the analogue for $\dot f$ of the downwind condition used by Ketcheson for
  second-order unconditionally SSP methods, and inspired by the derivative-correction
  schemes of Hu, Shu & Zhang (§4).

## Implicit Shu–Osher form and unconditional SSP

Gottlieb et al. write the method with only diagonal (implicit) evaluations,

$$Y_i=r_iy_n+\sum_{j<i}p_{ij}Y_j+hd_{ii}f(Y_i)+h^2\dot d_{ii}\dot f(Y_i),\qquad y_{n+1}=Y_s,$$

with page-local matrices $\mathbf P=(p_{ij})$, $\mathbf R=I-\mathbf P$ ($r_i$ its row
sums), $\mathbf D=\mathrm{diag}(d_{ii})$, $\dot{\mathbf D}=\mathrm{diag}(\dot d_{ii})$;
the Butcher form follows from $A=\mathbf R^{-1}\mathbf D$, $\dot A=\mathbf R^{-1}\dot{\mathbf D}$,
while the converse is not always possible (§2.2, Eqs. (10)–(11)). This form is
necessary but not sufficient for an unrestricted step.

**Theorem 1 (Gottlieb et al. 2022, §2.2).** Under the forward Euler condition and the
backward derivative condition, a method of this form with $r_i\ge0$, $p_{ij}\ge0$,
$d_{ii}\ge0$ and $\dot d_{ii}\le0$ satisfies $\lVert y_{n+1}\rVert\le\lVert
y_n\rVert$ for **every** $h>0$ (Eq. (12)). *Proof idea:* add $(\alpha+\beta)Y_i$ to a
stage and divide, so that $Y_i$ becomes a convex combination of the previous stages,
a forward Euler step $Y_i+\frac{hd_{ii}}{\alpha}f(Y_i)$ and a backward derivative step
$Y_i-\frac{h^2\lvert\dot d_{ii}\rvert}{\beta}\dot f(Y_i)$; $\alpha$ and $\beta$ can be
taken as large as needed, so no restriction on $h$ remains.

**Why the sign matters (App. A).** If instead $\dot d_{ii}\ge0$, as the second
derivative and Taylor series conditions require, the recursion for $A\mathbf 1$ and
$Ac$ gives $b^\top\mathbf 1-b^\top c\le k_s<\frac12$ with $k_1=\frac14$,
$k_i=1/(4(1-k_{i-1}))$; first order then forces $b^\top c>\frac12$, and the
second-order condition $b^\top c+\dot b^\top\mathbf 1=\frac12$ forces a negative entry
in $\dot b$. Hence no implicit two-derivative method of order 2 is unconditionally SSP
under those conditions, an extension of the Gottlieb–Shu–Tadmor barrier for implicit
Runge–Kutta methods (Gottlieb et al. 2022, App. A, Eq. (62)).

## Unconditionally SSP methods (SSP-iMDRK)

From Gottlieb et al. (2022, §2.3):

- **Order 2, one stage, the implicit Taylor method:**
  $y_{n+1}=y_n+hf(y_{n+1})-\frac12h^2\dot f(y_{n+1})$.
- **Order 3, two stages:** $\mathbf D=\mathrm{diag}(0,1)$,
  $\dot{\mathbf D}=\mathrm{diag}(-\frac16,-\frac13)$, $p_{21}=1$, $r=(1,0)$; i.e.
  $Y_1=y_n-\frac16h^2\dot f(Y_1)$ (implicit in $\dot f$ only) and
  $y_{n+1}=Y_1+hf(y_{n+1})-\frac13h^2\dot f(y_{n+1})$. It is exactly of order 3 (the
  first fourth-order condition gives $0\ne\frac14$, a check made during ingestion).
- **Order 4, five stages:** 15-digit Shu–Osher coefficients, e.g.
  $\mathrm{diag}(\mathbf D)=(0.6609\dots,0.2422\dots,1.1375\dots,0.1914\dots,0.6253\dots)$,
  $\mathrm{diag}(\dot{\mathbf D})=(-0.1778\dots,-0.3547\dots,-0.4040\dots,-0.1616\dots,-0.2189\dots)$;
  the printed coefficients satisfy all eight order conditions to about $10^{-15}$
  (checked during ingestion).
- No fifth-order method satisfying Theorem 1 was found: a search failure, not a
  proved barrier.

On $y'=-10y^2$, $y(0)=10$ ($\dot f=200y^3$; forward Euler positivity needs $h\le
0.1/y_n$, the backward derivative step $h^2\le0.005/y_n^2$) the second- and
third-order methods remain positive for every step tested, while stiffly accurate
DIRKs of orders 2 and 3 lose positivity for $h>\frac1{50}$ and $h>\frac1{75}$ (§2.4,
Fig. 1). The authors call unconditional SSP at order $p>2$ "unique among SSP methods";
Ketcheson's downwind-based methods reach order 2 (Abstract, §1, §4).

## IMEX multiderivative methods

For $y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$ with non-stiff $f^{\mathrm E}$ and stiff
$f^{\mathrm I}$ (page-local $\dot f^{\mathrm I}=(f^{\mathrm I})'f^{\mathrm I}$):

$$Y_i=r_iy_n+\sum_{j<i}p_{ij}Y_j+\sum_{j<i}w_{ij}\Bigl(Y_j+\frac hr f^{\mathrm E}(Y_j)\Bigr)+hd_{ii}f^{\mathrm I}(Y_i)+h^2\dot d_{ii}\dot f^{\mathrm I}(Y_i),\qquad y_{n+1}=Y_s,$$

with $r>0$ the SSP coefficient of the explicit part (Gottlieb et al. 2022, §3, Eqs.
(13)–(14)). The Butcher tableaux are $A^{\mathrm E}=\frac1r\mathbf R^{-1}\mathbf W$,
$A^{\mathrm I}=\mathbf R^{-1}\mathbf D$, $\dot A=\mathbf R^{-1}\dot{\mathbf D}$ with
$\mathbf R=I-\mathbf P-\mathbf W$ (Eqs. (16)–(18)).

**Theorem 2.** If forward Euler on $f^{\mathrm E}$ is contractive for $h\le
h_{\mathrm{FE}}$, forward Euler on $f^{\mathrm I}$ for $h\le kh_{\mathrm{FE}}$ ($k>0$
possibly tiny), and the backward derivative condition holds for $\dot f^{\mathrm I}$,
then nonnegative $r_i,p_{ij},w_{ij},d_{ii}$ and nonpositive $\dot d_{ii}$ give
$\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for $h\le rh_{\mathrm{FE}}$, a bound
independent of the stiff term (§3.1, Eq. (15)). Ordinary
[IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md) cannot do this for general
convex functionals (§3, recalled).

**Order conditions** for this three-tableau class through order 3, "not previously
appeared", are 22: $b^{\mathrm I\top}\mathbf 1=b^{\mathrm E\top}\mathbf 1=1$; at order 2
$b^{\mathrm I\top}c^{\mathrm I}+\dot b^\top\mathbf 1=\frac12$ and
$b^{\mathrm I\top}c^{\mathrm E}=b^{\mathrm E\top}c^{\mathrm I}=b^{\mathrm E\top}c^{\mathrm E}=\frac12$;
at order 3 sixteen conditions, e.g.
$b^{\mathrm I\top}A^{\mathrm I}c^{\mathrm I}+\dot b^\top c^{\mathrm I}+b^{\mathrm I\top}\dot c=\frac16$,
$b^{\mathrm I\top}(c^{\mathrm I})^2+2\dot b^\top c^{\mathrm I}=\frac13$,
$b^{\mathrm E\top}A^{\mathrm I}c^{\mathrm I}+b^{\mathrm E\top}\dot c=\frac16$ (§3.2,
table p. 11). The explicit weights couple to $\dot f^{\mathrm I}$ only through
$b^{\mathrm E\top}\dot c$.

**Methods** (§3.3): a three-stage second-order method with $r=1$, whose explicit part
is SSPRK(2,2) ($A^{\mathrm E}$ rows $(0)$, $(1)$, $(\frac12,\frac12)$; $A^{\mathrm I}$ rows
$(\frac12)$, $(\frac12,0)$, $(\frac12,0,\frac12)$; $\dot A$ with
$\dot a_{22}=-\frac12$, $\dot a_{32}=-\frac14$), against $r=0.8125$ for the
corresponding scheme of Hu, Shu & Zhang, a 23% larger step at the same three implicit
solves; and a six-stage third-order method with $r=0.904402174130635$ ("to achieve a
third order method we required six stages"). Coefficients were verified against all
22 conditions during ingestion.

## Asymptotic-preserving use

For $y'=T(y)+\frac1\varepsilon Q(y)$ with the relaxation structure
$Q'(y)Q(y)=-C_{\mathcal Ry}Q(y)$ ($T$, $Q$ and the positive factor $C_{\mathcal Ry}$, which
depends only on $\mathcal Ry$, are page-local), the IMEX scheme with $f^{\mathrm E}=T$,
$f^{\mathrm I}=Q/\varepsilon$ is positivity preserving for $h\le rh_{\mathrm{FE}}$
independently of $\varepsilon$, and, if $d_{ii}+\lvert\dot d_{ii}\rvert>0$ at every
stage, [asymptotic preserving](/definitions/asymptotic-preserving-scheme.md): as
$\varepsilon\to0$ at fixed $h$ it becomes the explicit part applied to the limit
system (Gottlieb et al. 2022, §3.4.2, Prop. 1). Details, including the hypotheses, are
on [positivity preservation](/properties/positivity-preservation.md). On a stiff ODE
model, Broadwell and BGK, design orders appear in the kinetic and fluid limits with
[order reduction](/definitions/order-reduction.md) in between (Remark 4, §3.5).

## Explicit methods with $r$ derivatives

**Page-local notation.** $f^{[k]}(y)=\frac{d^{k-1}}{dt^{k-1}}f(y(t))$ is the $(k-1)$-th total
time derivative of the right-hand side along the solution, computed recursively by the
chain rule, so $f^{[1]}=f$ and $f^{[2]}=\dot f$. The coefficients of derivative $k$ are
$a^{(k)}_{lj}$, $b^{(k)}_l$, with $a^{(1)}=A$, $a^{(2)}=\dot A$ in registry terms.

An explicit $r$-derivative, $s$-stage method of order $p$, written $r$DRK$p$-$s$, is
(Chouchoulis et al. 2022, Def. 1, after Seal, Güçlü & Christlieb)

$$Y_l=y_n+\sum_{k=1}^{r}h^k\sum_{j=1}^{l-1}a^{(k)}_{lj}\,f^{[k]}(Y_j),\qquad y_{n+1}=y_n+\sum_{k=1}^{r}h^k\sum_{l=1}^{s}b^{(k)}_l\,f^{[k]}(Y_l),$$

with strictly lower-triangular blocks. The coefficient of $h^2\dot f$ is $a^{(2)}$ itself,
with no factor $\frac12$. The **Taylor method** of order $r$ is the case $s=1$,
$b^{(k)}_1=1/k!$ (Remark 2). The schemes Chouchoulis et al. use all have the
"Taylor-plus-last-derivative" form: every stage is the Taylor polynomial of degree $r-1$
about $y_n$ plus one correction in the highest derivative evaluated at earlier stages,
$Y_l=y_n+\sum_{k<r}\frac{(c_lh)^k}{k!}f^{[k]}(y_n)+h^r\sum_{j<l}a^{(r)}_{lj}f^{[r]}(Y_j)$
(App. A). For example, the two-derivative fourth-order method of Chan & Tsai is

$$Y_2=y_n+\tfrac h2f(y_n)+\tfrac{h^2}8\dot f(y_n),\qquad y_{n+1}=y_n+hf(y_n)+h^2\Big(\tfrac16\dot f(y_n)+\tfrac13\dot f(Y_2)\Big).$$

Their six schemes and stability functions (Fig. 1, App. A; from Chan & Tsai and from
Ökten Turacı & Öziş, except the new 4DRK6-2):

| scheme | $c$ | $R(z)-\sum_{k\le p}z^k/k!$ |
|---|---|---|
| 2DRK3-2 | $(0,1)$ | 0 |
| 2DRK4-2 | $(0,\frac12)$ | 0 |
| 2DRK5-3 | $(0,\frac25,1)$ | $z^6/600$ |
| 3DRK5-2 | $(0,\frac25)$ | $z^6/900$ |
| 3DRK7-3 | $(0,\frac{3-\sqrt2}7,\frac{3+\sqrt2}7)$ | $c_8z^8+c_9z^9$, $c_8=\frac1{23520}-\frac{\sqrt2}{70560}$, $c_9=\frac{11}{1481760}-\frac{\sqrt2}{246960}$ |
| 4DRK6-2 (new) | $(0,\frac13)$ | $z^7/6480+z^8/77760$ |

The new four-derivative, two-stage, sixth-order 4DRK6-2 has
$a^{(k)}_{21}=\frac{(1/3)^k}{k!}$ for $k=1,\dots,4$, $b^{(k)}=(1/k!,0)$ for $k\le3$ and
$b^{(4)}=(\frac1{60},\frac1{40})$ (Table 8); no derivation or order verification is
printed. Its printed stability function follows from the tableau *(compiler check,
symbolic, not in the source)*. Except 3DRK5-2 and 4DRK6-2, all six regions contain part of the imaginary axis
(Remark 3). Multiderivative methods have two free parameters, derivatives and stages,
against one for Taylor methods, and both move stability (§5).

## Jacobian-free coupling to conservation laws (MDRKCAT)

For a conservation law $u_t+g(u)_x=0$ ($g$ the physical flux, page-local) the derivatives
$f^{[k]}$ become nested space derivatives involving $g'$, $g''$, …; already
$u_{tt}=(g'(u)g(u)_x)_x$ is "very tedious" for systems, which Chouchoulis et al. (2022, §1)
give as the likely reason multiderivative schemes were "rarely used in practice". They
convert only one time derivative into a space derivative and approximate the remaining
$\partial_t^{k-1}g(u)$ by the **compact approximate Taylor (CAT)** procedure of Carrillo &
Parés, built on the approximate Lax–Wendroff procedure of Zorío, Baeza & Mulet: at each
interface, finite differences in time of $g$ evaluated at Taylor-predicted states on the centred
stencil of cells $i-\mathsf p,\dots,i+\mathsf p$ ($\mathsf p$ the stencil half-width,
page-local), using
only flux evaluations (§3, Alg. 1). Inserting these into the stage and update fluxes gives
the conservative family $r$DRKCAT$p$-$s$ (Eqs. (17)–(18), Def. 4). The same device drives
the single-stage [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md).

- **Consistency (Thm. 1).** Under smoothness and $h=\mathcal O(\Delta x)$ the consistency
  order is $\min(2\mathsf p,p)$, so $\mathsf p=\lceil p/2\rceil$ is the efficient choice
  (Remark 6). Proved through lemmas on the CAT recursion.
- **Not multistep.** The CAT recursion has "a multistep flavour" but is local to one step,
  so variable steps are admissible; the tests use $h^n=\nu\Delta x/\max\lvert\lambda^n\rvert$
  (Remark 1, §6).
- **Fully discrete stability (§5, Table 2).** For linear advection MDRKCAT reduces to an
  MDRK–Lax–Wendroff scheme with centred derivative stencils (Thm. 2, proof omitted as
  "similar" to Carrillo & Parés). A [von Neumann analysis](/definitions/von-neumann-stability-analysis.md)
  gives the critical Courant numbers

  | 2DRKCAT3-2 | 2DRKCAT4-2 | 2DRKCAT5-3 | 3DRKCAT5-2 | 3DRKCAT7-3 | 4DRKCAT6-2 |
  |---|---|---|---|---|---|
  | 1.2954 | 1.4718 | 1.0619 | 0.4275 | 0.2300 | 0.8563 |

  against 1 for the original CAT method. Two-derivative schemes improve on CAT, three- and
  four-derivative ones lose; even numbers of derivatives are better, as observed for CAT.
  The ODE stability regions predict this ranking wrongly ("a method of lines (MOL)
  viewpoint is inadequate"): 3DRK7-3 has the largest region in Fig. 1 and the smallest
  critical number.
- **Numerics (§6).** Smooth [Burgers](/benchmarks/burgers-equation.md) data, a
  Buckley–Leverett problem, 1-D Euler density advection and a smooth nonlinear Euler case
  reach the design orders. CAT-$\mathsf p$ with $\mathsf p=4,5,6$ diverges on Burgers at
  $\nu=0.5$ before shocks form, and the MDRKCAT schemes do not. Accuracy per cell is
  comparable to DG-$P^3$/$P^4$ with four-stage SSP Runge–Kutta, which reaches design order
  on coarser meshes because it uses exact fluxes at interfaces and several quadrature points
  per cell. No timings are given.

## Implicit two-derivative Hermite–Birkhoff methods for DG

Zeifang & Schütz (2022, §2, App. A) use implicit two-derivative Hermite–Birkhoff
Runge–Kutta (HBRK) methods of order $p=4,6,8$ on $s=2,3,4$ equispaced nodes in $[0,1]$
with an explicit first stage. The $p=4$ member is the two-point Hermite (Obreshkov) rule

$$y_{n+1}=y_n+\frac h2\big(f(y_n)+f(y_{n+1})\big)+\frac{h^2}{12}\big(\dot f(y_n)-\dot f(y_{n+1})\big);$$

the $p=6$ and $p=8$ tableaux are printed in App. A (their rows of $A$ sum to $c$;
*compiler check, not in the source*). They do not solve the HBRK system directly but approximate it by a
predictor–corrector with $K$ corrections of order $\min(4+K,p)$, described on
[deferred correction](/methods/deferred-correction.md). Two-derivative methods reach high
order "with fewer temporal quadrature nodes" than one-derivative ones (§1).

The PDE coupling decides stability. A direct discretization of $\dot f$ (an implicit
Lax–Wendroff approach) gave "a severe timestep restriction" despite the A-stability of the
ODE method, as Zeifang & Schütz recall from Jaust, Schütz & Seal (§1). Following Schütz,
Seal & Jaust they introduce the auxiliary variable $\sigma=f_h(y)$ and discretize the time
derivative of the weak form, so that $\dot f_h(y,\sigma)$ is a DG operator with a
differentiated Lax–Friedrichs flux; for a linear PDE this preserves the stability of the
ODE solver (§3.2). Each stage becomes a Newton problem for $(Y,\sigma)$, twice the size of
an implicit-Euler step, with $\partial\dot f_h/\partial\sigma=\partial f_h/\partial y$ and
no Hessian term for linear fluxes; the solver and its closed-form element-block
preconditioner are on [implicit stage solvers](/methods/implicit-stage-solvers.md). With
steps 200–500 times the explicit limit the scheme reproduces the cylinder Strouhal number
and the 3D [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) dissipation rate
(§5.3).

## The one-stage limit

Babbar et al. (2022) do not use the multiderivative framing, but their single-step
Lax–Wendroff time discretization is the Taylor method of order $N+1$ (the $s=1$ case
above) with the flux derivatives approximated Jacobian-free and evaluated element-locally;
see [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)
*(compiler remark, not in the sources)*. They motivate it by the Runge–Kutta stage barriers, which a one-stage
method avoids (§1).

## Qualifications

- **"Type A".** Gottlieb et al. (Remark 2) call the IMEX schemes type A and globally
  stiffly accurate in the Boscarino–Pareschi–Russo classification, but $A^{\mathrm I}$
  alone is singular for both new methods; the claim rests on $d_{ii}+\lvert\dot
  d_{ii}\rvert>0$, i.e. invertibility of the combined implicit part. The
  classification is extended, not literal.
- **Printed slips** (arXiv v3): in the fourth-order Butcher list the indices are
  transposed relative to the lower-triangular convention ("$a_{14}$" denotes row 4,
  column 1), and "$\dot a_{12}=a_{13}=\dot a_{11}$" misses a dot; reconstruction from
  the Shu–Osher coefficients confirms the intended values.
- Each implicit stage needs $\dot f$ and its Jacobian; the cost of evaluating and
  solving with $\dot f$ is not discussed in the source.
- Order conditions are classical; stiff order is addressed only numerically.
- **3DRK7-3, row 3 of the third-derivative block.** Chouchoulis et al. (2022, Table 7)
  print the entry $a^{(3)}_{31}=c_2^3/6-a^{(3)}_{32}$. The Taylor-plus-last-derivative
  form requires the row sum $c_3^3/6$. With $c_3^3/6-a^{(3)}_{32}$ the printed tableau
  reproduces the paper's own stability function (Fig. 1) exactly; with the printed
  $c_2^3/6$ the $z^6$ coefficient of $R$ differs from $1/720$, so even linear sixth order
  fails (the $z^6$ coefficient becomes $\frac1{343}-\frac{29\sqrt2}{15435}$) *(compiler check,
  symbolic, not in the sources)*. The printed entry is therefore a slip against the paper's
  own Fig. 1; whether the original tableau of Ökten Turacı & Öziş carries $c_3^3/6$ has not
  been verified, since that paper is not ingested.
- **Tests above the linear limit.** Chouchoulis et al. run all smooth tests except the
  nonlinear Euler convergence study at $\nu=0.5$, above their own critical numbers for
  3DRKCAT5-2 (0.4275) and 3DRKCAT7-3 (0.2300), and both converge; the paper does not
  comment. Only 3DRKCAT7-3 with $\mathsf p=4$ diverges, on the nonlinear Euler case at
  $\nu=0.5$ on the coarse meshes (§6.3). Their $\nu$ in §6 uses the maximal eigenvalue of
  the flux Jacobian, not a constant advection speed, so Table 2 is not a sharp practical
  limit.
- The verdict that odd-derivative schemes "seem less adequate" with CAT (§7) rests on two
  three-derivative schemes, both of Taylor-plus-last-derivative form. The comparison with
  DG is accuracy per cell, with different degrees of freedom and no cost measure.
- Zeifang & Schütz (2022) prove no stability or convergence theorem; the order
  $\min(4+K,p)$ is quoted from Schütz, Seal & Zeifang and confirmed numerically up to 8.

# Citations

- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §1 (Eqs. 2–6), §2.1 (Eqs. 8–9, order conditions), §2.2 (Eqs. 10–12, Thm. 1), §2.3–2.4 (methods, Fig. 1), §3 (Eqs. 13–18), §3.1 (Thm. 2), §3.2 (order conditions), §3.3 (methods), §3.4 (Prop. 1, Remark 2), §3.5, §4, App. A (Eq. 62).
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — §1 (Eq. (4)); §2 (Def. 1, Remarks 1–2); §3 (Eqs. (6)–(18), Alg. 1, Def. 4); §4 (Thm. 1, Remark 6); §5 (Thm. 2, Prop. 1, Table 2, Fig. 1, Remark 3); §6.1–6.3 (Figs. 2–7); §7; App. A (Tables 3–8).
- [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) — §1; §2 (Eqs. (4)–(6), Remark 2); §3.2 (Eqs. (14)–(18)); §5.3; App. A (Eqs. (A.1)–(A.3)).
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §1, §4 (single-step Taylor time discretization).
