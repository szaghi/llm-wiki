---
type: Property
title: "Positivity preservation in time integration"
description: "A time integrator is positivity preserving if nonnegative data give nonnegative numerical solutions; within SSP theory it holds under $h\\le\\mathcal C h_{\\mathrm{FE}}$, unconditional positivity is limited to first order for Runge–Kutta and multistep methods, and multiderivative, splitting and exponential reformulations obtain higher order, including uniformly in a stiffness parameter."
status: established
aliases: [positivity-preserving time stepping, positivity preserving coefficient, nonnegativity preservation, unconditional positivity]
tags: [positivity, structure-preserving, ssp, stiff, asymptotic-preserving, kinetic]
timestamp: 2026-10-19T12:00:00Z
---

# Positivity preservation in time integration

A time integrator is **positivity preserving** for $y'=f(y)$ if $y_n\ge0$ (or $>0$)
componentwise implies $y_{n+1}\ge0$, either for all $h>0$ (*unconditional*) or under a
step restriction. Densities, concentrations and kinetic distribution functions need
it: a negative value can make the semi-discrete problem ill-posed (for instance a
negative temperature in a Maxwellian) and stops a computation even when the error is
small. In the SSP framework positivity is the special case of a convex functional
(the indicator of the nonnegative cone), so every
[SSP method](/methods/strong-stability-preserving-runge-kutta.md) preserves it under
$h\le\mathcal Ch_{\mathrm{FE}}$ whenever forward Euler preserves it under $h\le
h_{\mathrm{FE}}$ ([Gottlieb et al. 2022](/sources/gottlieb-2022.md), §1, §3.4).

## The first-order barrier

Runge–Kutta and linear multistep methods that preserve positivity **unconditionally**
are at most first order (Bolley & Crouzeix 1978), as recalled by
[Blanes et al. (2024)](/sources/blanes-2024.md) (§9.2.1). The SSP form of the same
fact: implicit methods preserving the forward Euler condition for every $h$ cannot
exceed order 1, backward Euler being the first-order example, as recalled by Gottlieb
et al. (2022, §1, App. A, restating Gottlieb–Shu–Tadmor). For stiff problems this is
the obstacle: the stiff part fixes a small $h_{\mathrm{FE}}$, and a higher-order
implicit method inherits only a bounded multiple of it. Gottlieb et al. illustrate it
on $y'=-10y^2$, $y(0)=10$: the forward Euler bound is $h\le0.1/y_n$, and the second-
and third-order stiffly accurate DIRKs of Kennedy & Carpenter lose positivity for
$h>\frac1{50}$ and $h>\frac1{75}$ and converge to qualitatively wrong solutions (§2.4,
Fig. 1).

## Ways around the barrier

Every route changes the class of methods or adds hypotheses on $f$:

- **Multiderivative methods with a backward derivative condition.** If in addition
  $\lVert y-h^2\dot f(y)\rVert\le\lVert y\rVert$ for $h^2\le\dot kh_{\mathrm{FE}}^2$
  (page-local constant $\dot k>0$), implicit two-derivative methods with nonnegative
  coefficients on $f$ and nonpositive coefficients on $\dot f$ preserve the functional
  for every $h>0$; methods of orders 2, 3 and 4 exist (Gottlieb et al. 2022, Thm. 1,
  §2.3). On $y'=-10y^2$ they stay positive for all steps tested, where the DIRKs fail
  (Fig. 1). See [multiderivative Runge–Kutta methods](/methods/multiderivative-runge-kutta.md).
- **Splitting of a doubled system.** For a problem written as $y'=A(y)y$ (page-local matrix function $A$), the doubled
  system $y'=A(z)y$, $z'=A(y)z$ is split so that each sub-step is a linear problem
  with frozen matrix, solved exactly; the Strang composition yields second-order
  approximations that preserve positivity and mass for every $h>0$, and fail for
  $h<0$ (Blanes et al. 2024, §9.2.1, Eqs. (9.14)–(9.15)). The structural hypothesis on
  $A$ that makes the frozen flows positive is not recorded in the reading notes. See
  [operator splitting](/methods/operator-splitting.md).
- **Exponential reformulation of stiff relaxation.** For a kinetic equation
  $\partial_tF=\frac1\varepsilon\mathcal Q(F)$ penalized by a BGK operator
  $\beta(\mathcal M-F)$, the change of variable
  $\partial_t[(F-\mathcal M)e^{\beta t/\varepsilon}]=\frac{\mathcal Q-\beta(\mathcal M-F)}{\varepsilon}e^{\beta t/\varepsilon}$
  lets any explicit Runge–Kutta method be applied; $\beta$ is chosen as the smallest
  value that keeps $F$ positive, and the inhomogeneous version of Li & Pareschi is
  stated to preserve positivity, high order and the AP property (Dimarco & Pareschi;
  Li & Pareschi; as recalled by [Jin 2022](/sources/jin-2022.md), §5.2, Eqs.
  (5.7)–(5.8); page-local: $F$ distribution, $\mathcal Q$ collision operator,
  $\mathcal M$ local Maxwellian). See
  [exponential integrators](/methods/exponential-integrators.md) and
  [BGK penalization](/methods/bgk-penalization.md).
- **Positive coefficients in splitting.** For parabolic problems splitting
  coefficients must themselves be nonnegative (a negative sub-step runs a diffusion
  backwards); real splittings of order $\ge3$ need negative coefficients, so real
  positive splittings stop at order 2 unless commutators or complex coefficients are
  used (Blanes et al. 2024, §2.6, §6.4). This is positivity of the *method
  coefficients*, a precondition for well-posed sub-steps, not positivity of the
  solution; see the [negative-coefficient barrier](/results/negative-coefficient-barrier.md).

## Positivity uniformly in a stiffness parameter

For the stiff relaxation form $y'=T(y)+\frac1\varepsilon Q(y)$ (page-local: $T$
transport, $Q$ collision or relaxation), a scheme should stay positive under a step
restriction independent of $\varepsilon$ and be
[asymptotic preserving](/definitions/asymptotic-preserving-scheme.md). Ordinary
higher-order IMEX schemes generally violate positivity unless $h$ is restricted in
terms of $\varepsilon$ (Higueras et al., as recalled by Gottlieb et al. 2022, §3.4).
Gottlieb et al. assume (§3.4.1): forward Euler on $T$ preserves positivity for
$h\le h_{\mathrm{FE}}$; backward Euler on $Q$ preserves it for every $h\ge0$ (which
forward Euler positivity does not imply, Remark 1); conservation $\mathcal RQ=0$ for
a linear map $\mathcal R$; equilibria $Q(y)=0\iff y=E(\mathcal Ry)$; and the key,
non-generic property $Q'(y)Q(y)=-C_{\mathcal Ry}Q(y)$ with $C_{\mathcal Ry}>0$
(page-local symbols). Under these, their multiderivative IMEX scheme preserves
positivity for $h\le rh_{\mathrm{FE}}$, $r$ the SSP coefficient of the explicit part,
for **every** $\varepsilon$, because each implicit stage collapses to a backward Euler
step on $Q$ with the nonnegative effective step
$\frac h\varepsilon d_{ii}-\frac{h^2}{\varepsilon^2}\dot d_{ii}C_{\mathcal RY_i}$,
where $d_{ii}\ge0$ and $\dot d_{ii}\le0$ are the stage's diagonal coefficients on the
stiff term and on its time derivative (Prop. 1, Eq. (51)). BGK, Broadwell and hyperbolic relaxation systems satisfy the
property ($C=1$, $\rho$, $1$). In a mixed-regime BGK test ($\varepsilon$ from $10^{-5}$
to $O(1)$) no negative cell average appeared at $h=\frac1{24}\Delta x/v_{\max}$
(§3.5.3, Fig. 8). They present the third-order scheme as the first positivity- and
AP-preserving IMEX method of order three, earlier final-stage derivative corrections
of Hu, Shu & Zhang having stopped at order 2 (§3.4). Hu & Shu (2019) give a
second-order AP and positivity-preserving exponential Runge–Kutta method, as recalled
by Jin (2022, §6.1).

## Qualifications

- The multiderivative route needs $\dot f=f'f$ and a structural condition on it; the
  condition $Q'Q=-CQ$ is special to relaxation-type operators (Gottlieb et al. 2022,
  §3.4.1, "non-generic").
- The exponential-RK claims are recalled by Jin without proof; whether high order
  holds *uniformly* in $\varepsilon$ is not claimed there, and the reader of that
  source flags reported order reduction in intermediate regimes.
- Positivity of a fully discrete scheme also depends on the spatial discretization
  (limiters, as in the WENO positivity limiter used in Gottlieb et al. 2022, §3.5.3).
- Patankar-type methods, also aimed at unconditional positivity, are not covered by
  the sources of this page.

# Citations

- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §1, Thm. 1, §2.3–2.4 (Fig. 1), §3.4 (Properties 1–5, Prop. 1, Eq. 51, Remark 1), §3.5.3 (Fig. 8), App. A.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §2.6, §6.4, §9.2.1 (Bolley–Crouzeix barrier, doubled-system splitting, Eqs. 9.14–9.15).
- [Jin (2022)](/sources/jin-2022.md) — §5.2 (Eqs. 5.7–5.8, exponential reformulation and positivity), §6.1 (Hu & Shu 2019).
