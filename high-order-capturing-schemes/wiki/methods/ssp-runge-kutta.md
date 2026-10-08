---
type: Method
title: "TVD / strong-stability-preserving Runge–Kutta methods"
description: "Explicit Runge–Kutta methods written as convex combinations of forward-Euler steps, so any norm or convex-functional stability of forward Euler (TVD, maximum norm, positivity, entropy) carries over under a scaled time step."
status: established
aliases: [TVD Runge-Kutta, SSP Runge-Kutta, Shu-Osher Runge-Kutta, SSP-RK3]
tags: [time-discretization, ssp, tvd, method-of-lines]
timestamp: 2026-10-08T00:00:00Z
---

# TVD / strong-stability-preserving Runge–Kutta methods

**The idea** ([Shu & Osher (1988)](/sources/shu-1988.md), §II). Suppose
the forward-Euler step $u + \Delta t\,\mathcal{L}(u)$ is TVD (or TVB)
for $\Delta t \le \Delta t_{\mathrm{FE}}$. Write an explicit RK method in
the Shu–Osher form
$$u^{(i)} = \sum_{k=0}^{i-1}\left(a_{ik}\,u^{(k)} + b_{ik}\,\Delta t\,\mathcal{L}(u^{(k)})\right),\qquad a_{ik} \ge 0,\ \ \sum_k a_{ik} = 1 .$$
If also $b_{ik} \ge 0$, every stage is a convex combination of forward
Euler steps with step $(b_{ik}/a_{ik})\Delta t$, hence TVD for
$\Delta t \le \mathcal{C}\,\Delta t_{\mathrm{FE}}$ with
$\mathcal{C} = \min a_{ik}/b_{ik}$. Where some $b_{ik} < 0$, the
operator is replaced by the downwind operator $\tilde{\mathcal{L}}$
(Proposition 2.1). The total variation may be replaced by any convex
functional (Remark 2.1): the methods preserve maximum-norm stability,
entropy inequalities, and so on ([Shu (1998)](/sources/shu-1998.md),
§4.2.1).

**Optimal low-order methods** ([Shu & Osher (1988)](/sources/shu-1988.md),
eqs. 2.15–2.19; [Shu (1998)](/sources/shu-1998.md), eqs. 4.10–4.11):
* second order (Heun), $\mathcal{C} = 1$:
  $u^{(1)} = u^n + \Delta t\,\mathcal{L}(u^n)$,
  $u^{n+1} = u^n + \tfrac12\Delta t\,\mathcal{L}(u^n) + \tfrac12\Delta t\,\mathcal{L}(u^{(1)})$;
* third order, $\mathcal{C} = 1$:
$$\begin{aligned}
u^{(1)} &= u^n + \Delta t\,\mathcal{L}(u^n),\\
u^{(2)} &= \tfrac34 u^n + \tfrac14 u^{(1)} + \tfrac14\Delta t\,\mathcal{L}(u^{(1)}),\\
u^{n+1} &= \tfrac13 u^n + \tfrac23 u^{(2)} + \tfrac23\Delta t\,\mathcal{L}(u^{(2)}).
\end{aligned}$$
  Each stage needs only the previous stage's $\mathcal{L}$, which lowers
  storage. Classical third-order methods rewritten in this form have
  negative $b_{ik}$ and smaller $\mathcal{C}$.

**Fourth order and above.** No four-stage, fourth-order method with
nonnegative coefficients exists (proved by Gottlieb and Shu, cited in
[Shu (1998)](/sources/shu-1998.md)). Their preferred four-stage
fourth-order method uses $\tilde{\mathcal{L}}$, has $\mathcal{C} = 0.936$,
and costs two operator evaluations at one stage, an effective
$\mathcal{C}$ of $0.624$. A fifth-order method with $\tilde{\mathcal{L}}$
is given by [Shu & Osher (1988)](/sources/shu-1988.md). Third-order
low-storage methods (two registers) reach $\mathcal{C} \approx 0.32$.
TVD multistep methods exist to third order with $\mathcal{C} = 0.5$
per evaluation; none of fourth order without negative coefficients was
found ([Shu (1998)](/sources/shu-1998.md), §4.2.2).

**Why nonlinear stability matters.** Linear stability of the ODE solver
does not suffice for discontinuous solutions, and does not apply to
adaptive-stencil schemes at all ([Shu & Osher (1988)](/sources/shu-1988.md)).
A second-order MUSCL scheme that is TVD under forward Euler produces an
overshoot at a shock when integrated with a linearly stable but non-TVD
second-order RK method, and larger oscillations in the intermediate
stages; the TVD method does not ([Shu (1998)](/sources/shu-1998.md),
Fig. 4.1).

## Use in this corpus

* ENO and WENO in the method-of-lines form use the third-order method
  ([Shu & Osher (1989)](/sources/shu-1989.md);
  [Liu, Osher & Chan (1994)](/sources/liu-1994.md), which also prints a
  fourth-order variant; [Jiang & Shu (1996)](/sources/jiang-1996.md),
  "RK-3", together with the classical non-TVD fourth-order "RK-4" and
  $\Delta t \propto \Delta x^{5/4}$ in accuracy tests so that RK-4 acts
  as fifth order).
* [Harten et al. (1987)](/sources/harten-1987.md) (Remark C2) found the
  semi-discrete ENO with Runge–Kutta time stepping non-oscillatory for
  CFL up to 0.5, with oscillations beyond, and less efficient than their
  fully discrete Cauchy–Kowalewski scheme.
* [Suresh & Huynh (1997)](/sources/suresh-1997.md) design the MP5
  constraint for the stage structure: since each RK3 stage is a
  forward-Euler step and the next stage a positive combination,
  monotonicity of one stage implies monotonicity of the full step
  ([monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).
* [Balsara & Shu (2000)](/sources/balsara-2000.md): WENO of $r = 3$ to
  $7$ with RK3 is linearly stable for CFL between 1.43 and 0.99, but
  non-oscillatory shock capturing needs much smaller CFL ($r = 5$ WENO:
  clean at 0.2, slightly oscillatory at 0.4); convergence tests use
  $\Delta t \propto \Delta x^{(2r-1)/3}$.
* The alternative is the Lax–Wendroff (Taylor) time discretization,
  compact and fully one-step, but algebraically heavy in multi-D and
  hard to analyze ([Shu (1998)](/sources/shu-1998.md), §4.2.3).
  [Levy, Puppo & Russo (1999)](/sources/levy-1999.md) use Runge–Kutta
  with natural continuous extensions to supply the time quadrature of
  a staggered central scheme ([central WENO](/methods/central-weno.md)).

# Citations

1. [Shu & Osher (1988)](/sources/shu-1988.md), §II (eqs. 2.12–2.19 read from the page images).
2. [Shu (1998)](/sources/shu-1998.md), §4.2.
3. [Harten et al. (1987)](/sources/harten-1987.md), Remark C2.
4. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §2.
5. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§1, 6.
6. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §§1–2.
7. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§I, IV.
8. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), §2.1.
