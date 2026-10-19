---
type: Method
title: "Multiderivative Runge–Kutta methods and the backward derivative condition"
description: "Two-derivative Runge–Kutta methods use $f$ and $\\dot f=f'f$; under the forward Euler and backward derivative conditions, implicit ones with nonpositive $\\dot f$ coefficients are SSP for every step size at orders 2–4, and their IMEX extension is SSP, positivity preserving and asymptotic preserving uniformly in a stiffness parameter."
status: established
aliases: [two-derivative Runge–Kutta, MDRK, SSP-iMDRK, implicit Taylor method, SSP IMEX multiderivative Runge–Kutta]
tags: [ssp, implicit, imex, asymptotic-preserving, order-conditions]
timestamp: 2026-10-19T12:00:00Z
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

# Citations

- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §1 (Eqs. 2–6), §2.1 (Eqs. 8–9, order conditions), §2.2 (Eqs. 10–12, Thm. 1), §2.3–2.4 (methods, Fig. 1), §3 (Eqs. 13–18), §3.1 (Thm. 2), §3.2 (order conditions), §3.3 (methods), §3.4 (Prop. 1, Remark 2), §3.5, §4, App. A (Eq. 62).
