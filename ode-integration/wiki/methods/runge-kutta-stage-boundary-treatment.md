---
type: Method
title: "Boundary conditions for Runge–Kutta stages"
description: "How time-dependent Dirichlet data are imposed on the internal stages of Runge–Kutta and IMEX methods in a method-of-lines setting: naive stage-time values create numerical boundary layers and order reduction, Irksome imposes the data's time derivative on stage derivatives, and a PDE-based boundary treatment recovers design order 3 and 4."
status: established
aliases: [stage boundary conditions, boundary treatment of stage values, boundary treatment for IMEX Runge–Kutta, stage Dirichlet data]
tags: [order-reduction, imex, runge-kutta, verification]
timestamp: 2026-10-19T23:00:00Z
---

# Boundary conditions for Runge–Kutta stages

A Runge–Kutta step for a method-of-lines semi-discretization of an
initial-boundary-value problem needs boundary values not only at $t_n$ and $t_{n+1}$
but at every internal stage. With time-dependent Dirichlet data $u=g(x,t)$ on the
boundary $\Gamma$ (page-local: $u(x,t)$ the PDE solution, $g$ the data), the stage
value $Y_i$ is not an approximation of $u(\cdot,t_n+c_ih)$ to the method's order (its
error is governed by the [stage order](/definitions/stage-order.md)), so imposing
$Y_i|_\Gamma=g(\cdot,t_n+c_ih)$ makes the boundary values inconsistent with the
interior stages. The result is a **numerical boundary layer** and
[order reduction](/definitions/order-reduction.md)
([González-Tabernero et al. 2024](/sources/gonzaleztabernero-2024.md), §1, Fig. 1,
citing Lubich–Ostermann). The sources treat the problem in two ways: by imposing the
time derivative of the data on stage derivatives
([Farrell et al. 2021](/sources/farrell-2021.md)), and by computing stage boundary
values from the stage equations and the PDE itself (González-Tabernero et al. 2024).

## Derivative-of-data stage conditions (Irksome)

[Irksome](/software/irksome.md) works with stage derivatives $k_i\approx u_t(t_n+c_ih)$.
Strongly imposed Dirichlet data $u|_\Gamma=g$ become

$$k_i|_\Gamma=\partial_tg(\cdot,t_n+c_ih),\qquad i=1,\dots,s,$$

while weakly imposed data need only the data at stage times (Farrell et al. 2021, §2.2.1,
Eq. (18)). Translated to stage values, this imposes
$Y_i|_\Gamma=u_n|_\Gamma+h\sum_ja_{ij}\,\partial_tg(\cdot,t_n+c_jh)$, the stage of the same
Runge–Kutta method applied to the boundary ODE $u'=\partial_tg$, not the data at the stage
time *(compiler translation, not in the source)*. Farrell et al. observe order reduction
of two-stage Gauss–Legendre on a manufactured heat solution with Dirichlet data
(§4.1, Figs. 1–2) and do not discuss the role of the stage condition in it.

## Boundary treatment from the stage equations (IMEX)

González-Tabernero et al. (2024) consider convection–diffusion–reaction
$u_t+\nabla\cdot F(u)=\nabla\cdot G(\nabla u)+r(u)$ on Cartesian domains (page-local
fluxes $F$, $G$ — $G$ linear — and reaction $r$), discretized by local discontinuous
Galerkin in space and by an [IMEX Runge–Kutta method](/methods/imex-runge-kutta.md) in
time, with convection and reaction explicit, $f^{\mathrm E}=-\nabla\cdot F+r$, and
diffusion implicit, $f^{\mathrm I}=\nabla\cdot G$, so that $h=\mathcal O(\Delta x)$
(§1–2). The IMEX scheme is written with a stage $0$ equal to $y_n$,

$$Y_i=y_n+h\sum_{j=0}^{i-1}a^{\mathrm E}_{ij}f^{\mathrm E}_j+h\sum_{j=0}^{i}a^{\mathrm I}_{ij}f^{\mathrm I}_j,\qquad i=1,\dots,s,$$

with shared abscissae $c_i=\sum_ja^{\mathrm E}_{ij}=\sum_ja^{\mathrm I}_{ij}$
(Eq. (2.16)). The treatment computes the boundary value of each stage "in the same way
as the interior points", in four steps (§3):

1. **Write the stage equation at the boundary** and replace the implicit diffusive term
   through the PDE, which holds at the stage time:
   $f^{\mathrm I}_j|_\Gamma=\partial_tg(t_n+c_jh)-f^{\mathrm E}_j|_\Gamma$. For the first
   stage of their third-order scheme ($a^{\mathrm I}_{11}=a^{\mathrm E}_{10}=c_1$) this
   gives
   $$Y_1|_\Gamma=y_n+c_1h\big(f^{\mathrm E}_0+\partial_tg(t_n+c_1h)-f^{\mathrm E}_1\big)$$
   (Eq. (3.4)), and in general
   $Y_i|_\Gamma=y_n+h\sum_ja^{\mathrm E}_{ij}f^{\mathrm E}_j+h\sum_ja^{\mathrm I}_{ij}\big(\partial_tg(t_n+c_jh)-f^{\mathrm E}_j\big)$
   (Algorithm 4.1, step 9).
2. **Differentiate the stage equations in space** to obtain the boundary derivatives
   $\partial_xY_i$ that $f^{\mathrm E}_j|_\Gamma$ needs. Theorem 3.5 gives them for any
   stage of any IMEX tableau, in terms of $\partial_xY_1$, the tableaux and Taylor-shifted
   values of $\partial_xf^{\mathrm E}$, $\partial_xf^{\mathrm I}$ at $t_n$
   (proof by differentiating Eq. (2.16) and using $\sum_ja^{\mathrm E}_{ij}=\sum_ja^{\mathrm I}_{ij}=c_i$).
3. **Taylor shifts and Lax–Wendroff (Cauchy–Kovalevskaya) substitution.** Quantities at
   stage times are expanded about $t_n$ (Prop. 3.1:
   $H(z(x,t+h),t+h)=H(z(x,t),t)+\mathcal O(h)$ for $C^2$ functions of $z=u,u_x$, extended
   to higher order by more Taylor terms), and time derivatives are converted into space
   derivatives through the PDE. The stage value inside the explicit term can either be
   found by solving the resulting nonlinear boundary equation or be Taylor-expanded; for
   order $p$ only $p-1$ time derivatives of $y_n$ are needed (Eq. (3.6)), and the two
   approaches give no substantial difference (§5).
4. **Approximate the boundary space derivatives** from the local polynomial of the
   numerical solution. They multiply $h^2$, so with $h=\mathcal O(\Delta x)$ accuracy
   $\mathcal O(\Delta x^{p-2})$ suffices (Remark 3.4, Remark 3.6); the first and second
   derivatives come from the local polynomial, the third is rebuilt by a one-sided second
   difference of $\hat u_x$ over neighbouring cells, and for fourth order the fourth and
   fifth derivatives by first-order differences (Remark 3.4, §5.4).

Algorithms 4.1–4.3 need only the two tableaux. Algorithm 4.2 evaluates the explicit
terms at their own stage times and Taylor-shifts the implicit derivative only from the
previous stage; Algorithm 4.3 extends it to two dimensions on structured meshes (§4).
For second- and third-order schemes the correction sums of Theorem 3.5 vanish and a
first-order Taylor shift suffices (Remark 3.6). The authors present the procedure as an
extension and simplification of Wang, Zhang and Shu (2018), who treated one third-order
IMEX scheme on a 1D linear problem, to nonlinear convection, source terms, arbitrary
order and several dimensions; they cite Wang–Zhang–Shu and Zhao–Huang (finite
differences with inverse Lax–Wendroff ghost points) as the only prior IMEX boundary
treatments (§1). They state that the procedure applies to explicit Runge–Kutta methods
as a special case and to implicit stiff sources, without testing either (§1, §6).

## Numerical evidence

Observed rates in $L^1$, $L^2$, $L^\infty$ at the finest meshes, with $h=\mathrm{CFL}\,\Delta x$
refined together (González-Tabernero et al. 2024, §5, Tables 1–4):

| test | scheme | without treatment | with treatment |
|---|---|---|---|
| 1D convection–diffusion, $u=e^{-t}\sin(x+0.1t)$ | 3rd-order IMEX (Calvo–de Frutos–Novo type) | 2.52 / 2.25 / 2.00 | 2.97 / 2.99 / 2.98 |
| 1D viscous [Burgers](/benchmarks/burgers-equation.md) with source, $u=e^{-t}\sin x$ | 3rd order | 2.65 / 2.26 / 1.98 | 3.01 / 3.00 / 3.00 |
| 2D convection–diffusion | 3rd order | 2.53 / 2.26 / 1.96 | 3.00 / 2.99 / 3.00 |
| 1D convection–diffusion | ARK4(3)6L[2]SA (Kennedy–Carpenter) | 2.50 / 2.26 / 2.02 | 3.98 / 3.98 / 3.95 |

The third-order scheme is a four-row IMEX pair whose implicit part is an SDIRK with a
zero first column, last row equal to $b$, and $c_1=0.4358665\ldots$, the middle root of
$6x^3-18x^2+9x-1$ (p. A3290). Without treatment the pointwise error at $t=h$ peaks at
about $1.1\times10^{-5}$ at both boundaries ($N=160$); with treatment the peaks vanish
(Fig. 4). Work–precision diagrams of a C++ code show the cost of the treatment to be
negligible; the untreated fourth-order curve lies close to the treated third-order one
(§5.5, Fig. 6).

## Relation to other remedies

The [order-reduction](/definitions/order-reduction.md) page lists the alternatives:
high [stage order](/definitions/stage-order.md), high
[weak stage order](/definitions/weak-stage-order.md), and modified boundary data in the
style of Alonso-Mallo and Cano, as recalled by Steinebach (2023) and Biswas et al.
(2025). Biswas et al. (2025, §1) list the drawbacks of boundary modifications for
explicit methods: they need derivatives of the boundary data, introduce parameters, are
intrusive, and had been studied only in one dimension. The treatment of
González-Tabernero et al. needs $\partial_tg$ at stage times (or a Cauchy–Kovalevskaya
reconstruction, or interpolation of the data, Remark 3.3), is intrusive in the same sense,
and works in two dimensions on Cartesian meshes. For
[TASE operators](/methods/tase-operators.md), Bassenne et al. (2021) find that boundary
source terms must be preconditioned together with the operator to avoid errors that start
at the boundaries.

## Qualifications

- **No theory.** Only Prop. 3.1 (a Taylor expansion) and Theorem 3.5 (an algebraic
  identity) are proved; recovery of the design order is shown numerically, on Cartesian
  meshes, with time and space refined together, so the time order is not isolated
  (González-Tabernero et al. 2024, §5). The LDG degree is not stated explicitly.
- **Stage order not mentioned.** The paper does not relate the untreated rates to stage
  order. They are consistent with the boundary-layer picture on the order-reduction
  page: about $q+1=2$ in the maximum norm for methods of stage order 1, with fractional
  gains in $L^2$ and $L^1$ *(compiler remark, not in the source)*.
- **Printed slips** (version of record): the second line of the display after Eq. (3.10)
  prints an undefined $\beta_3$ and $\alpha_2+\beta_2-1$ where Eq. (3.11) has
  $\alpha_2+\beta_1-1$; Algorithms 4.2–4.3 drop the factor $h$ in front of the last implicit
  term of the boundary-derivative update; §5.3 prints the 2D exact solution with a factor
  $D$ that the Table 3 caption omits; Prop. 3.1 gives $H$ the codomain $\Omega$.

# Citations

- [González-Tabernero et al. (2024)](/sources/gonzaleztabernero-2024.md) — §1; §2.2 Eq. (2.16), p. A3290 (third-order tableau); §3 Prop. 3.1, Eqs. (3.3)–(3.12), Remarks 3.3–3.6, Thm. 3.5; §4 Algorithms 4.1–4.3; §5 Tables 1–4, Figs. 1, 4–6; §6.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.2.1 Eq. (18); §4.1 Figs. 1–2.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1 (drawbacks of boundary modifications).
- [Steinebach (2023)](/sources/steinebach-2023.md) — Fig. 3 (modified boundary data, as listed on the order-reduction page).
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §4.2 (boundary sources under TASE preconditioning).
