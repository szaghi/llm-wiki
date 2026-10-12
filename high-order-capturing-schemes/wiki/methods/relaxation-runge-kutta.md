---
type: Method
title: "Relaxation Runge–Kutta methods"
description: "Scale the Runge–Kutta update by a relaxation parameter found from one scalar equation per step, so that a convex functional (an entropy) changes by exactly the method's own quadrature of its rate: fully discrete entropy conservation or dissipation for any Runge–Kutta method, order kept when the result is assigned to the relaxed time (RRK) and lost by one when assigned to the full step (IDT)."
status: established
aliases: [RRK, relaxation RK, incremental direction technique, IDT, fully discrete entropy stability]
tags: [time-discretization, runge-kutta, entropy]
timestamp: 2026-10-12T00:00:00Z
---

# Relaxation Runge–Kutta methods

**The problem.** An entropy-stable semi-discretization satisfies
$\frac{d}{dt}\mathcal S(u) \le 0$ for a convex functional $\mathcal S$
(the global entropy). A time integrator need not inherit it. The
[SSP argument](/methods/ssp-runge-kutta.md) transfers an entropy
inequality only when forward Euler satisfies it, and for an
entropy-conservative semi-discretization it does not: by convexity,
$\mathcal S(u + \Delta t\mathcal L(u)) \ge \mathcal S(u) + \Delta t\langle\mathcal S'(u), \mathcal L(u)\rangle = \mathcal S(u)$
(compiler's one-line argument). In the tests of
[Ranocha et al. (2020)](/sources/ranocha-2020.md) every unmodified
method, SSP or not, changes the total entropy of an entropy-conservative
DG/SBP discretization (Fig. 7), and SSPRK(3,3) gains energy on a
pendulum (§3.3).

## The relaxed step

With the stages $Y_j$ of any [Runge–Kutta method](/methods/explicit-runge-kutta.md)
(§2, eqs. 2.1–2.6):
$$u^{n+1}_{\gamma} = u^n + \gamma^n_{\mathrm R}\,\Delta t\sum_{j=1}^{s}\mathsf b_j\,\mathcal L(Y_j),$$
where $\gamma^n_{\mathrm R}$ is the positive root of
$$\Psi^n(\gamma) = \mathcal S\Big(u^n + \gamma\Delta t\sum_j\mathsf b_j\mathcal L(Y_j)\Big) - \mathcal S(u^n) - \gamma\Delta t\sum_j\mathsf b_j\big\langle\mathcal S'(Y_j), \mathcal L(Y_j)\big\rangle .$$
The new value changes $\mathcal S$ by exactly the method's quadrature of
$\frac{d}{dt}\mathcal S$. For $\mathcal S = \tfrac12\Vert u\Vert^2$ this is
Ketcheson's 2019 relaxation, which the paper generalizes to any smooth
convex $\mathcal S$. The two sums are accumulated during the stages, so
a [low-storage](/methods/low-storage-runge-kutta.md) implementation runs
unchanged; the cost is one scalar root-find per step (Brent's method in
the ODE tests, bisection to machine precision in the 3D solver; §§2.4, 4).

**Properties** (§2):
* **Entropy** (Theorem 2.2). The method is entropy conservative; with all
  $\mathsf b_j \ge 0$ and $\gamma^n_{\mathrm R} \ge 0$ it is entropy
  dissipative. The Fehlberg and Dormand–Prince 5(4) pairs have a negative
  weight, so the sufficient condition fails for them (Remark 2.3).
* **Existence** (Theorems 2.8, 2.15). For a method of order
  $p_{\mathrm t} \ge 2$, strictly convex $\mathcal S$, $\mathcal L(u^n) \ne 0$
  and small $\Delta t$, $\Psi^n$ has exactly the roots $0$ and a unique
  positive $\gamma^n_{\mathrm R} = 1 + O(\Delta t^{p_{\mathrm t}-1})$;
  $\Psi^n(1)$, the entropy production of the unmodified method, is
  $O(\Delta t^{p_{\mathrm t}+1})$ (Corollary 2.13).
* **Order depends on where the result is placed** (Theorem 2.11). Read as
  an approximation at $t^n + \Delta t$ (the incremental direction
  technique, IDT, of Calvo et al.), the scheme has order
  $p_{\mathrm t} - 1$. Read at $t^{n+1} = t^n + \gamma^n_{\mathrm R}\Delta t$
  (relaxation Runge–Kutta, RRK), it keeps order $p_{\mathrm t}$. On the
  exponential-entropy ODE IDT also shows "serious convergence issues for
  small time steps" (§3.1).
* **Retained structure.** Linear invariants (total mass on a periodic
  domain) are conserved although $\gamma^n_{\mathrm R}$ is nonlinear.
  Several convex quantities are all dissipated by taking the smallest
  root, when all $\mathsf b_j \ge 0$. SSP properties are retained as long
  as $\gamma^n_{\mathrm R}$ stays close to 1, cited from Ketcheson (2019) with no bound given
  (§2.3).

## Fully discrete entropy-stable CFD

Coupled with entropy-conservative or entropy-stable flux-differencing
SBP–SAT (DG-type collocation) discretizations on unstructured hexahedra,
RRK gives explicit, fully discrete, primary-conservative and
entropy-stable schemes for 3D Euler and Navier–Stokes
([Ranocha et al. (2020)](/sources/ranocha-2020.md), §4, Conclusions).
* **The guarantee is global**, for the integrated entropy; a cell-local
  fully discrete entropy inequality is "currently out of reach".
* **Positivity is not addressed**; combining relaxation with
  [positivity limiters](/properties/positivity-preserving.md) is left
  open (Conclusions). Rescaling the update by $\gamma^n_{\mathrm R}$ is
  not covered by a stage-wise limiter's guarantee.
* **Accuracy.** On a 3D [isentropic vortex](/benchmarks/isentropic-vortex.md)
  the coupled schemes reach $L^2$ rates 4.21, 5.17 and 6.15 for
  polynomial degrees 3, 4 and 5 (Table 1). On random-degree
  nonconforming grids with all interface dissipation off, relaxation
  conserves the total entropy to quadruple precision with all thirteen
  methods tested (Fig. 7).
* **Little effect on shocks.** There is no shock capturing. On the
  [Sod tube](/benchmarks/sod-shock-tube.md) and the
  [Titarev–Toro sine-shock test](/benchmarks/shu-osher-problem.md),
  solutions with and without relaxation are indistinguishable,
  overshoots included, and $\vert\gamma^n_{\mathrm R} - 1\vert < 5\times10^{-4}$
  (Figs. 8–10). On a supersonic turbulent flow past a square rod,
  $\vert\gamma^n_{\mathrm R} - 1\vert \le 2.5\times10^{-7}$ (Fig. 13).

The relaxation idea and the [positivity-adaptive weights](/methods/positivity-preserving-adaptive-runge-kutta.md)
of Nüßlein, Ranocha and Ketcheson both re-choose $\mathsf b$ after the
stages; relaxation rescales it by one scalar, the positivity method
solves a linear program for a new vector
([Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §1).

# Citations

1. [Ranocha et al. (2020)](/sources/ranocha-2020.md), §§1–4, Conclusions (arXiv v4; eqs. 2.1–2.7 checked on the page image).
2. [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §1.
