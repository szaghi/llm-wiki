---
type: Method
title: "Boundary conditions for Runge–Kutta stages"
description: "How time-dependent Dirichlet data are imposed on the internal stages of Runge–Kutta and IMEX methods in a method-of-lines setting: stage-time values limit accuracy to the stage order, Irksome moved from derivative-of-data to stage-value (DAE-type) conditions, a PDE-based treatment recovers design order 3 and 4, and halo stages need the same care."
status: established
aliases: [stage boundary conditions, boundary treatment of stage values, boundary treatment for IMEX Runge–Kutta, stage Dirichlet data, DAE-type boundary conditions, ODE-type boundary conditions]
tags: [order-reduction, imex, runge-kutta, verification]
timestamp: 2026-10-29T18:13:00Z
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
citing Lubich–Ostermann). The sources treat the problem in three ways: by imposing the
time derivative of the data on stage derivatives
([Farrell et al. 2021](/sources/farrell-2021.md)), by imposing the data on the stage
values and accepting the stage-order limit
([Kirby & MacLachlan 2025](/sources/kirby-2025.md)), and by computing stage boundary
values from the stage equations and the PDE itself (González-Tabernero et al. 2024). The
same consistency question arises at the internal boundaries of a domain decomposition
([Goswami et al. 2023](/sources/goswami-2023.md)).

## Derivative-of-data and stage-value conditions (Irksome)

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

**Change of default to stage values.** Kirby & MacLachlan (2025, §2–2.1), the first a
co-author of the earlier paper, replace this "ODE-type" treatment as Irksome's default by a
"DAE-type" one that treats the Dirichlet condition as an algebraic constraint on the stage
values:

$$Y_i|_\Gamma=g(\cdot,t_n+c_ih)\quad\Longleftrightarrow\quad\sum_ja_{ij}k_j|_\Gamma=\frac{g(\cdot,t_n+c_ih)-u_n|_\Gamma}{h},\qquad i=1,\dots,s$$

(Eqs. (2.15)–(2.17)), solvable for the boundary values of the $k_i$ when $A$ is invertible,
up to the $L^2$ projection error of $g$. They state that it retains (at least) the stage
order of the scheme, matching the convergence theory of stiff ODEs and DAEs, and that for
[stiffly accurate](/properties/stiff-accuracy.md) methods (Lobatto IIIC, Radau IIA)
$u_{n+1}=Y_s$ matches the data at $t_{n+1}$, which other methods do not guarantee. The ODE
type "has proven to have some inherent weaknesses": with incompatible data (1D heat
equation, zero initial value, boundary values 1, three-stage Lobatto IIIC, $h=0.05$) it
sees a zero boundary derivative and stays at the zero solution, while the DAE type captures
the approach to $u\equiv1$ (Fig. 2). "Many practical cases show little difference". Both
treatments remain available (`bc_method='DAE'`, the default, or `'ODE'`). The two papers
thus record a change of default by the software's authors, not a disagreement; see
[Irksome](/software/irksome.md).

The DAE type is the stage-time imposition that the lead of this page describes, with the
error that the stage order governs; Kirby & MacLachlan accept that limit, while
González-Tabernero et al. below aim beyond it *(compiler remark, not in the sources)*. On
their heat-equation tests with DAE-type data, three- and four-stage Radau IIA (stage order
$s$) and the DIRK WSODIRK433 (weak stage order 3) keep optimal accuracy, while backward
Euler, Alexander's DIRK (stage order 1) and, with cubic elements, two-stage Radau IIA
(stage order 2) lose $L^2$ accuracy at large steps (§4.1, Figs. 3–4).

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

## Stage values at subdomain interfaces

In a distributed explicit solver every Runge–Kutta stage needs halo data from neighbouring
processes, so an $s$-stage low-storage method costs $s$ halo exchanges per step
([Goswami et al. 2023](/sources/goswami-2023.md), §2.3). Goswami et al. avoid the
inter-stage exchanges with asynchrony-tolerant finite differences on delayed halo values
and meet the boundary-stage problem at the processor boundaries:

- **Frozen buffer values.** Holding the halo values fixed across the stages breaks the
  cancellation of stage error terms between neighbouring points; their truncation-error
  analysis limits the solution at processor boundaries to second order and the
  domain-averaged error to third order under strong scaling, whatever the orders of the
  spatial and temporal schemes (§3.1–3.2, Eqs. (16)–(24)).
- **Buffer values advanced by the stage recurrence.** The halo points are advanced through
  the same low-storage recurrence, with the unavailable right-hand side replaced by a
  one-sided temporal stencil on the delayed history whose coefficients reproduce the Taylor
  terms that the stages accumulate, not $\partial_tu$ alone (§3.2.1, Eqs. (26)–(37)). This
  restores fourth order with a two-stage method and sixth order with three-stage methods in
  1D advection–diffusion tests, with an asynchrony error that grows linearly with the
  number of processes (§3.4, §4, Figs. 5–6).

The remedy has the shape of the boundary treatment above: stage boundary data computed
consistently with the stage equations instead of frozen or naive values *(compiler
analogy, not drawn by the source)*. The method is on
[low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md).

## Numerical evidence

Observed rates in $L^1$, $L^2$, $L^\infty$ at the finest meshes, with $h=\mathrm{CFL}\,\Delta x$
refined together (González-Tabernero et al. 2024, §5, Tables 1–4):

| test | scheme | without treatment | with treatment |
|---|---|---|---|
| 1D convection–diffusion, $u=e^{-t}\sin(x+0.1t)$ | 3rd-order IMEX (Calvo–de Frutos–Novo type) | 2.52 / 2.25 / 2.00 | 2.97 / 2.99 / 2.98 |
| 1D viscous [Burgers](/benchmarks/burgers-equation.md) with source, $u=e^{-t}\sin x$ | 3rd order | 2.65 / 2.26 / 1.98 | 3.01 / 3.00 / 3.00 |
| 2D convection–diffusion | 3rd order | 2.53 / 2.26 / 1.96 | 3.00 / 2.99 / 3.00 |
| 1D convection–diffusion | [ARK4(3)6L[2]SA](/methods/kennedy-carpenter-ark-methods.md) (Kennedy–Carpenter) | 2.50 / 2.26 / 2.02 | 3.98 / 3.98 / 3.95 |

The third-order scheme is a four-row IMEX pair whose implicit part is an SDIRK with a
zero first column, last row equal to $b$, and $c_1=0.4358665\ldots$, the middle root of
$6x^3-18x^2+9x-1$ (p. A3290). Without treatment the pointwise error at $t=h$ peaks at
about $1.1\times10^{-5}$ at both boundaries ($N=160$); with treatment the peaks vanish
(Fig. 4). Work–precision diagrams of a C++ code show the cost of the treatment to be
negligible; the untreated fourth-order curve lies close to the treated third-order one
(§5.5, Fig. 6).

## Relation to other remedies

Among the earlier sources, [Ascher et al. (1997)](/sources/ascher-1997.md) (§1)
list among the drawbacks of Runge–Kutta schemes for time-dependent PDEs "a loss of accuracy
order when time-dependent inflow boundary conditions are prescribed", citing Carpenter,
Gottlieb, Abarbanel and Don (1995), and a remedy by Abarbanel, Gottlieb and Carpenter (1996).
The [order-reduction](/definitions/order-reduction.md) page lists the alternatives:
high [stage order](/definitions/stage-order.md), high
[weak stage order](/definitions/weak-stage-order.md), and modified boundary data in the
style of Alonso-Mallo and Cano, as recalled by Steinebach (2023) and Biswas et al.
(2025). Biswas et al. (2025, §1) list the drawbacks of boundary modifications for
explicit methods: they need derivatives of the boundary data, introduce parameters, are
intrusive, and had been studied only in one dimension. The treatment of
González-Tabernero et al. needs $\partial_tg$ at stage times (or a Cauchy–Kovalevskaya
reconstruction, or interpolation of the data, Remark 3.3), is intrusive in the same sense,
and works in two dimensions on Cartesian meshes. A single-stage scheme avoids stage boundary values altogether.
[Babbar et al. (2022)](/sources/babbar-2022.md) (§8.1.1, Remark 4, Fig. 6b) impose inflow
data in [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)
as the time-averaged boundary flux $\frac1h\int_{t_n}^{t_{n+1}}g(u_b(t))\,dt$ by
$(N+1)$-point Gauss quadrature in time ($g$ the physical flux, $u_b$ the inflow data and $N$
the polynomial degree, page-local). On linear
advection with Dirichlet inflow, SSP Runge–Kutta flux reconstruction at its own CFL number
shows slightly larger errors than the Lax–Wendroff scheme at degrees 3 and 4, which the
authors attribute, citing Carpenter et al., to the treatment of Dirichlet data inside the
Runge–Kutta stages; they do not test a stage boundary correction. For
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
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §2, §2.1 (Eqs. (2.15)–(2.17), Fig. 2); §4.1 (Figs. 3–4).
- [Goswami et al. (2023)](/sources/goswami-2023.md) — §2.3; §3.1–3.4 (Eqs. (16)–(43)); §4 (Figs. 5–6).
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1 (drawbacks of boundary modifications).
- [Steinebach (2023)](/sources/steinebach-2023.md) — Fig. 3 (modified boundary data, as listed on the order-reduction page).
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §4.2 (boundary sources under TASE preconditioning).
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §8.1.1 (Fig. 6b), Remark 4 (time-averaged inflow flux; Runge–Kutta stage data).
- [Ascher et al. (1997)](/sources/ascher-1997.md) — §1 (order loss with time-dependent inflow data, refs. [1], [4]).
