---
type: Method
title: "IMEX and additive Runge–Kutta methods"
description: "Additive Runge–Kutta methods integrate y' = fE + fI with an explicit tableau for the nonstiff part and a diagonally implicit tableau for the stiff part on shared stages; the page gives the scheme, its GARK and splitting views, SSP and asymptotic-preserving variants, solver costs and software practice."
status: established
aliases: [IMEX, ImEx, IMEX-RK, ImEx-ARK, ARK, additive Runge–Kutta, implicit-explicit Runge–Kutta]
tags: [imex, runge-kutta, stiff, implicit, explicit, asymptotic-preserving]
timestamp: 2026-10-19T12:00:00Z
---

# IMEX and additive Runge–Kutta methods

An implicit–explicit (IMEX) or additive Runge–Kutta (ARK) method integrates
$y'=f^{\mathrm E}(t,y)+f^{\mathrm I}(t,y)$, with $f^{\mathrm E}$ nonstiff and
$f^{\mathrm I}$ stiff, by applying an explicit tableau
$(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ to $f^{\mathrm E}$ and a diagonally
implicit tableau $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ to $f^{\mathrm I}$, on one
shared set of $s$ stage values. Each stage then needs one implicit solve in
$f^{\mathrm I}$ only, while $f^{\mathrm E}$ is evaluated explicitly. The sources use
IMEX methods as production integrators
([Reynolds et al. 2023](/sources/reynolds-2023.md);
[Gardner et al. 2022](/sources/gardner-2022.md)), as the base of IMEX multirate
methods ([Chinomona & Reynolds 2021](/sources/chinomona-2021.md)), as comparison
baselines ([Roberts et al. 2021](/sources/roberts-2021.md)), as compositions of
Euler steps ([Blanes et al. 2024](/sources/blanes-2024.md)) and as the time
discretization of stiff relaxation and kinetic problems
([Gottlieb et al. 2022](/sources/gottlieb-2022.md); [Jin 2022](/sources/jin-2022.md)).

## The scheme

With step $h_n$ and stage values $Y_i$ (Reynolds et al. 2023, eq. 7; Gardner et al.
2022, §2.3):

$$\begin{aligned}
Y_i&=y_n+h_n\sum_{j=1}^{i-1}a^{\mathrm E}_{ij}f^{\mathrm E}\big(t_n+c^{\mathrm E}_jh_n,Y_j\big)+h_n\sum_{j=1}^{i}a^{\mathrm I}_{ij}f^{\mathrm I}\big(t_n+c^{\mathrm I}_jh_n,Y_j\big),\qquad i=1,\dots,s,\\
y_{n+1}&=y_n+h_n\sum_{i=1}^{s}\Big(b^{\mathrm E}_if^{\mathrm E}\big(t_n+c^{\mathrm E}_ih_n,Y_i\big)+b^{\mathrm I}_if^{\mathrm I}\big(t_n+c^{\mathrm I}_ih_n,Y_i\big)\Big),
\end{aligned}$$

and an embedded solution $\hat y_{n+1}$ uses $\hat b^{\mathrm E}$, $\hat b^{\mathrm I}$
([embedded pairs](/methods/embedded-runge-kutta-pair.md)). $A^{\mathrm E}$ is strictly
lower triangular and $A^{\mathrm I}$ lower triangular, i.e. a
[DIRK](/methods/diagonally-implicit-runge-kutta.md); stage $i$ solves
$Y_i-h_na^{\mathrm I}_{ii}f^{\mathrm I}(t_n+c^{\mathrm I}_ih_n,Y_i)=\text{known data}$.
With a mass matrix, $My'=f^{\mathrm E}+f^{\mathrm I}$ is treated through
$M^{-1}f^{\mathrm E}$ and $M^{-1}f^{\mathrm I}$ with $M$ nonsingular and independent
of $y$ (Reynolds et al. 2023, eqs. 5–6).

**Shared or distinct abscissae.** ARKODE requires the two tables to share $s$ but
allows $c^{\mathrm E}\ne c^{\mathrm I}$, which some SSP IMEX methods need
(Reynolds et al. 2023, §2.2). The base IMEX-ARK of an
[IMEX-MRI-GARK](/methods/imex-mri-gark.md) method must instead be internally
consistent, $c^{\mathrm E}=c^{\mathrm I}$, have an explicit first stage and be
stiffly accurate, a form obtained by padding (Chinomona & Reynolds 2021, §2.1).

## Structural views

- **As a GARK method.** An ARK method is the
  [GARK method](/methods/generalized-additive-runge-kutta.md) with
  $A^{\{\mathrm I,\mathrm E\}}=A^{\{\mathrm E,\mathrm E\}}=A^{\mathrm E}$ and
  $A^{\{\mathrm E,\mathrm I\}}=A^{\{\mathrm I,\mathrm I\}}=A^{\mathrm I}$ (Chinomona &
  Reynolds 2021, §2.1, citing Sandu & Günther). Its order conditions are those of
  the two tables plus the coupling conditions in which both tableaux appear along
  one tree.
- **As a composition of Euler steps.** The one-step IMEX Euler method of Ascher
  et al. is the composition of an explicit Euler step on $f^{\mathrm E}$ and an
  implicit Euler step on $f^{\mathrm I}$, and many second-order IMEX schemes have the
  symmetric form implicit half step ∘ explicit step ∘ explicit half step (Blanes
  et al. 2024, §6.1, eq. 6.14). The IMEX trapezoidal Runge–Kutta method is Strang
  splitting of a doubled system (eqs. 6.18–6.21); without restarting the
  auxiliary variable it is symmetric and can be extrapolated. A splitting variant
  of IMEX Crank–Nicolson leapfrog with an explicit midpoint step halves the implicit
  work (eq. 6.17). See [operator splitting](/methods/operator-splitting.md).
- **Linearly implicit use.** When $f^{\mathrm I}$ is linear in $y$, ARKODE performs
  one Newton iteration per implicit stage (Reynolds et al. 2023, §2.2).

## Named methods in the sources

- **Kennedy–Carpenter ARK methods**, the ARKODE defaults: ARK3(2)4L[2]SA,
  ARK4(3)6L[2]SA and ARK5(4)8L[2]SA, of orders 3, 4, 5 with embeddings 2, 3, 4,
  and ARK4(3)7L[2]SA1 (Reynolds et al. 2023, §2.2). The ESDIRK part of
  ARK5(4)8L[2]SA is ARKODE's default fifth-order DIRK, used for reference
  solutions.
- **ARS(3,4,3)** of Ascher, Ruuth & Spiteri, printed to 40 digits by Chinomona &
  Reynolds (2021, §4.1): with $\gamma_{\mathrm{ARS}}=0.4358665215\ldots$ and
  $\alpha_{\mathrm{ARS}}=0.5529291480\ldots$ (page-local names; the source writes $\eta$,
  $\alpha$), the implicit table is
  $c=(0,\gamma_{\mathrm{ARS}},\tfrac{1+\gamma_{\mathrm{ARS}}}2,1)$ with rows $(0)$,
  $(0,\gamma_{\mathrm{ARS}})$, $(0,\tfrac{1-\gamma_{\mathrm{ARS}}}2,\gamma_{\mathrm{ARS}})$,
  $(0,b_2,b_3,\gamma_{\mathrm{ARS}})$, where $b_2=-\tfrac32\gamma_{\mathrm{ARS}}^2+4\gamma_{\mathrm{ARS}}-\tfrac14$ and
  $b_3=\tfrac32\gamma_{\mathrm{ARS}}^2-5\gamma_{\mathrm{ARS}}+\tfrac54$; both tables share
  $b=(0,b_2,b_3,\gamma_{\mathrm{ARS}})$. It is the base of IMEX-MRI-GARK3a/3b.
- **ARS(2,3,2), ARS(3,4,3), ARK4(3)6L[2]SA** are the IMEX baselines of Roberts et
  al. (2021, §6.2).

## Strong stability and positivity

For a general convex functional, standard IMEX Runge–Kutta methods do not remove
the step restriction coming from the stiff operator (Gottlieb et al. 2022, §3,
citing earlier work). Gottlieb et al. lift it by adding the second
derivative $\dot f^{\mathrm I}=f^{\mathrm I\prime}f^{\mathrm I}$ on the implicit diagonal,
an IMEX [multiderivative](/methods/multiderivative-runge-kutta.md) method:

$$Y_i=y_n+h\sum_{j<i}a^{\mathrm E}_{ij}f^{\mathrm E}(Y_j)+h\sum_{j\le i}a^{\mathrm I}_{ij}f^{\mathrm I}(Y_j)+h^2\sum_{j\le i}\dot a_{ij}\dot f^{\mathrm I}(Y_j),\qquad y_{n+1}=Y_s.$$

**Theorem (Gottlieb et al. 2022, Thm. 2).** Assume forward-Euler conditions on
$f^{\mathrm E}$ (step $h_{\mathrm{FE}}$) and on $f^{\mathrm I}$, and the *backward
derivative condition* $\lVert y-h^2\dot f^{\mathrm I}(y)\rVert\le\lVert y\rVert$ for
$h^2\le\dot\kappa\,h_{\mathrm{FE}}^2$ ($\dot\kappa>0$, page-local). If the method has a
Shu–Osher form with non-negative convex-combination and explicit coefficients,
non-negative diagonal coefficients on $f^{\mathrm I}$ and **non-positive** diagonal
coefficients on $\dot f^{\mathrm I}$, then $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for
$h\le\mathcal C h_{\mathrm{FE}}$, with $\mathcal C$ the
[SSP coefficient](/methods/strong-stability-preserving-runge-kutta.md) of the explicit
part, independently of $f^{\mathrm I}$.

Gottlieb et al. derive the 22 order conditions of this three-tableau class up to
order 3 (§3.2) and give a 3-stage second-order method with $\mathcal C=1$ (explicit
part Heun/SSPRK(2,2), against $\mathcal C=0.8125$ for an earlier method of Hu, Shu
& Zhang: a 23% larger step) and a 6-stage third-order method with
$\mathcal C=0.904402174130635$ (§3.3). For stiff kinetic systems with the
structural property $\dot Q=-C\,Q$ they prove positivity for $h\le\mathcal C h_{\mathrm{FE}}$
uniformly in $\varepsilon$ (Prop. 1); see
[positivity preservation](/properties/positivity-preservation.md).

## Asymptotic-preserving IMEX schemes

For $y'=T(y)+\frac1\varepsilon Q(y)$ with relaxation term $Q$ ($T$, $Q$ page-local),
an IMEX scheme with $Q$ implicit is
[asymptotic preserving](/definitions/asymptotic-preserving-scheme.md) when its
$\varepsilon\to0$ limit at fixed $h$ is a consistent scheme for the limit system.

- Gottlieb et al. (2022, Prop. 1) prove the AP property of their IMEX
  multiderivative methods when every stage carries $Q$ or $\dot Q$
  ($a^{\mathrm I}_{ii}+\lvert\dot a_{ii}\rvert>0$): the limit is the explicit part applied
  to the limit system, with the order of the explicit part. They call their
  schemes "type A" and globally stiffly accurate in the Boscarino–Pareschi–Russo
  classification (Remark 2), although $A^{\mathrm I}$ alone is singular for both
  methods; the classification is extended to the pair $(A^{\mathrm I},\dot A)$.
- Jin (2022, §5.1) reviews the first-order IMEX scheme of
  [BGK penalization](/methods/bgk-penalization.md), whose implicit BGK term is
  inverted explicitly through conservation, and (p. 457) the Boscarino–Pareschi–Russo
  reformulation of the diffusive limit that turns the limiting scheme into an
  implicit diffusion discretization with $h=\mathcal O(\Delta x)$ instead of
  $\mathcal O(\Delta x^2)$. He points to high-order IMEX schemes for hyperbolic
  relaxation (Pareschi & Russo; Dumbser et al.) and to a uniform-accuracy proof
  for IMEX-BDF (Hu & Shu) (§6.1), and to an all-speed low-Mach splitting with the
  stiff pressure gradient implicit (§6.5).
- Order reduction in the intermediate regime $\varepsilon\sim h$ is observed by
  Gottlieb et al. (2022, Remark 4, §3.5); see
  [order reduction](/definitions/order-reduction.md).

## Cost and solver practice

- **Evaluation counts.** $f^{\mathrm E}$ is evaluated once per stage, $f^{\mathrm I}$
  once per nonlinear iteration, so an expensive nonstiff term favours IMEX over a
  fully implicit DIRK (Reynolds et al. 2023, §5.1.2, Table 1). On a
  [Brusselator](/benchmarks/brusselator.md) with $10^{-4}$/$10^{-9}$ tolerances, the
  maximum-order implicit predictor reduces all integrator statistics by at least
  32% against the trivial one for DIRK and for IMEX with implicit reactions; with
  explicit reactions and one Newton iteration the cutoff predictor gains up to 20%
  ([dense output](/methods/dense-output.md),
  [implicit stage solvers](/methods/implicit-stage-solvers.md)).
- **Task-local nonlinear solves.** When the implicit part is pointwise local (e.g.
  reactions), a custom nonlinear solver can solve each MPI task's block
  independently. On a stiff advection–reaction Brusselator with ARKODE's default
  third-order IMEX method it is 4.2–7.9× faster than a global Newton–GMRES solve
  on 40–10,240 MPI tasks (Gardner et al. 2022, §6.1, Fig. 3).
- **Step-size limits.** IMEX keeps an explicit-like step restriction from the
  explicit part: on the 500-inverter chain its largest stable step is
  $3.2$–$5.2\times10^{-3}$ against $5.2$–$7.1\times10^{-2}$ for implicit single-rate
  and compound-fast multirate methods (Roberts et al. 2021, Table 6.1). At orders
  2–3 compound-fast [multirate GARK](/methods/multirate-gark.md) is slightly more
  efficient than the IMEX baselines; at order 4 they are similar.
- **IMEX versus multirate at scale.** In a 3D reacting-flow weak-scaling test the
  IMEX ARK4(3)7L[2]SA1 run is far slower than an explicit-MIS multirate run,
  because every rank-local linear solve inside each Newton iteration triggers a
  global synchronization (Reynolds et al. 2023, §5.2;
  [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md)).

## Qualifications

- Blanes et al. (2024, §6.2, §6.4) note that splitting methods with real positive
  coefficients are limited to order 2 on parabolic problems; this barrier concerns
  splittings of exact sub-flows, not additive Runge–Kutta methods, for which
  higher orders are routine (the Kennedy–Carpenter methods above reach order 5).
- Gardner et al. print the abscissa index of the update and of the stage equation
  as $c_j$ inside sums over $i$ (§2.3, §2.5); the formulas above use the intended
  index.

# Citations

- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.2 (eqs. 5–7), §3.4, §5.1.2 (Table 1), §5.2 (Fig. 3).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.3, §2.5, §6.1 (Fig. 3).
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §2.1, §4.1 (ARS(3,4,3)).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §6.2 (Fig. 6.2, Table 6.1).
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §3 (Thm. 2, order conditions p. 11, §3.3 methods, Prop. 1, Remarks 2 and 4).
- [Jin (2022)](/sources/jin-2022.md) — §5.1 (eq. 5.2), p. 457 (eqs. 5.37–5.38), §6.1, §6.5.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.1 (eqs. 6.14–6.21), §6.2, §6.4.
