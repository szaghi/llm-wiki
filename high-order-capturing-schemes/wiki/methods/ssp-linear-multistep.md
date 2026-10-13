---
type: Method
title: "SSP linear multistep methods"
description: "Explicit linear multistep methods written as convex combinations of forward-Euler steps from past states, with one operator evaluation per step; the fixed-step optimal coefficients, a sharp bound on the SSP coefficient in terms of the step history and closed-form optimal formulae for variable steps, greedy CFL-following step selection, and why they are recommended with positivity limiters."
status: established
aliases: [SSP LMM, SSP multistep, TVD multistep, variable-step SSP multistep, SSPMSV]
tags: [time-discretization, ssp, multistep]
timestamp: 2026-10-13T00:00:00Z
---

# SSP linear multistep methods

An explicit $m$-step method
$u^{n+1} = \sum_{i=1}^{m}\left(a_i u^{n+1-i} + \Delta t\,b_i\,\mathcal L(u^{n+1-i})\right)$,
with $a_i \ge 0$, $\sum_i a_i = 1$ and $b_i \ge 0$, is a convex combination
of forward-Euler steps from past states. It therefore keeps any convex
functional bound of forward Euler for $\Delta t \le \mathcal C\,\Delta t_{\mathrm{FE}}$,
$\mathcal C = \min_i a_i/b_i$, at one evaluation of $\mathcal L$ per step
([Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §5;
[Shu (1998)](/sources/shu-1998.md), §4.2.2). The fixed-step optimal
values and barriers are on
[SSP order barriers](/results/ssp-order-barriers.md): with all
$b_i \ge 0$, three-step second order $1/2$, four-step second order $2/3$,
four-step third order $1/3$ and five-step third order $1/2$; no $m$-step
method of order $m$ has all $b_i \ge 0$. The optimal two-step
second-order method, also $\mathcal C = 1/2$, has a negative $b_2$ and
needs the downwind operator $\tilde{\mathcal L}$ (Gottlieb, Shu &
Tadmor, Proposition 5.2: $a_1 = 4/5$, $a_2 = 1/5$, $b_1 = 8/5$,
$b_2 = -2/5$, so $\min(a_1/b_1, a_2/\vert b_2\vert) = 1/2$; the
coefficients were checked against the printed one-parameter family).

## Fixed-step bound

For $m \ge p_{\mathrm t}$, $\mathcal C \le (m - p_{\mathrm t})/(m - 1)$
(Lenferink, as cited by [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §3.1).
It gives $\mathcal C \le 0$ for $m = p_{\mathrm t}$, the barrier above, and
is attained by the optimal second-order methods,
$\mathcal C = (m-2)/(m-1)$, and by the four- and five-step third-order
methods, $1/3$ and $1/2$ (Remark 3, Proposition 1). These agree with the
values of Gottlieb, Shu and Tadmor.

## Variable step size

A multistep method's coefficients assume equal steps, but a CFL-limited
step changes with the solution. [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md)
build the first explicit SSP multistep methods whose coefficients follow
the step history:
* **SSP condition** (Theorem 1, eqs. 11–14). With nonnegative
  coefficients $a_{i,n}$, $b_{i,n}$ that now depend on the step history,
  the step must satisfy
  $\Delta t^n \le \min_i \frac{a_{i,n}}{b_{i,n}}\,\Delta t_{\mathrm{FE}}(u^{n+1-i})$
  over every past state used, not only the last one (Remark 2). The bound
  is also necessary (Remark 1). The sufficient form uses the smallest
  past forward-Euler limit, $\min_i\Delta t_{\mathrm{FE}}(u^{n+1-i})$.
* **Sharp bound** (Theorem 2, eq. 18). With the step-history sum
  $\Omega_{\Delta t}$ (equal to $m$ for fixed steps),
  $$\mathcal C \le \frac{\Omega_{\Delta t} - p_{\mathrm t}}{\Omega_{\Delta t} - 1}\quad(\Omega_{\Delta t} > p_{\mathrm t}),\qquad \mathcal C \le 0\quad(\Omega_{\Delta t} \le p_{\mathrm t}),$$
  which reduces to Lenferink's bound. It is attained at second order
  (Theorem 3, closed-form optimal formulae for every $m$) and at third
  order for $m = 4, 5$ when the step history stays in a window
  (Proposition 1, eqs. 26–28). The optimal formula's sparsity pattern can
  change with the history (Remark 4). Methods of any order exist for
  bounded step ratios, with enough steps (Theorem 5, existence only).
* **Greedy step selection** (§4, eqs. 36, 39). Since $\mathcal C$ depends on
  the new step, the condition is implicit. Solved in closed form at
  second order, the new step is the smallest past forward-Euler limit
  multiplied by a ratio: the sum of the last $m - 1$ steps, divided by
  that sum plus the limit; at third order the limit enters the
  denominator twice. The step tends to the fixed-step SSP step
  $\frac{m - p_{\mathrm t}}{m - 1}\Delta t_{\mathrm{FE}}$ (Theorems 6–7;
  third order needs a slow-variation assumption). This is CFL following,
  not [error control](/methods/runge-kutta-step-size-control.md).
* **Convergence** (Theorems 8–10). Nonnegative $a_{i,n}$ give
  zero-stability, and the methods converge at orders 2 and 3. Starting
  steps use the two-stage SSP Runge–Kutta method.
* **Tests** (§6). Variable-coefficient advection reaches orders 2 and 3.
  On Burgers' equation the Courant number settles at $\mathcal C$ times
  the forward-Euler limit $1/2$, i.e. at $1/4$ and $1/6$. On the
  [Woodward–Colella blast waves](/benchmarks/interacting-blast-waves.md),
  run to $t = 0.04$, the step follows the maximum wave speed. The
  forward-Euler limit $1/2$ is proved for the TVD scheme only and is used
  with WENO5 without proof; the total variation of the WENO runs grows by
  at most $10^{-4}$ per step.

## Why multistep with positivity limiters

Two reasons appear in the corpus for preferring SSP multistep methods
when a [positivity limiter](/properties/positivity-preserving.md)
enforces bounds:
* the stage wave speeds of a Runge–Kutta step are unknown at $t^n$, so
  the CFL bound for the stages is uncertain; a multistep method has no
  stages ([Zhang & Shu (2010)](/sources/zhang-2010.md), Remark 2.7);
* Runge–Kutta methods "in conjunction with the limiter can lead to order
  reduction" ([Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md),
  §1, citing Gottlieb, Ketcheson & Shu 2011 and the Zhang–Shu
  maximum-principle paper). This second reason is an open entry
  ([positivity preservation](/properties/positivity-preserving.md),
  Contradictions: "Does positivity limiting inside Runge–Kutta stages
  reduce the order?").

The variable-step condition shows the multistep method's price: it
avoids unknown future stage speeds but must take the minimum of the
forward-Euler limits over all past states it uses.

**Later uses (batch 16).** *The origin: TVD multistep methods* ([Shu (1988b)](/sources/shu-1988-b.md), §3).
* *Form and proof* (eqs. 3.7–3.16, Proposition 3.1). The $m$-step method
  above, with $\tilde{\mathcal L}$ in place of $\mathcal L$ where
  $b_i < 0$, $a_i \ge 0$, $a_i = 0$ only if $b_i = 0$, and
  $\sum_i a_i = 1$, is a convex combination of forward-Euler steps from
  the past levels, hence TVD for
  $\Delta t \le \min_i(a_i/\vert b_i\vert)\,\Delta t_{\mathrm{FE}}$. This is
  the convexity argument of the later SSP framework, proved here for the
  total variation. The paper counts *past* levels, so its $m$ is this
  page's $m - 1$.
* *Order conditions* (eq. 3.11, re-indexed by the compiler and checked on
  every row below): order $p_{\mathrm t}$ if, besides $\sum_i a_i = 1$,
  $$\sum_{i=1}^{m}\left[(i-1)^{l}a_i - l\,(i-1)^{l-1}b_i\right] = (-1)^{l},\qquad l = 1,\dots,p_{\mathrm t}\quad(0^0 = 1).$$
* *Every order is reachable* (Corollary 3.1). For a TVD space
  discretization of a given order, an $m$-step method of the same order,
  $p_{\mathrm t} = m$, with positive $\mathcal C$ exists for given $a_i$
  (e.g. all $1/m$): the
  $b_i$ solve a nonsingular linear system. Existence only; the $b_i$ may
  be negative.
* *Cost and choice* (Remarks 3.1–3.3). More steps give a larger
  $\mathcal C$; requiring $b_i \ge 0$ avoids $\tilde{\mathcal L}$, which
  "will reduce the work of each timestep by one half". A negative $b_i$
  without $\tilde{\mathcal L}$ runs the upwind scheme backward in time,
  "unstable in any sense". Runge–Kutta methods are self-starting and need
  less storage, but "for very high-order methods (order $\ge 5$)
  multilevel methods may be simpler".
* *Table 1* (p. 1079), in this page's indexing ($a_1$, $b_1$ act on
  $u^n$), with the printed $\mathcal C$; "by no means exhaustive, nor …
  the optimal of the corresponding order":

  | $m$ | $p_{\mathrm t}$ | $\mathcal C$ | $a_1,\dots,a_m$ | $b_1,\dots,b_m$ |
  |---|---|---|---|---|
  | 2 | 2 | 0.5 | 4/5, 1/5 | 8/5, −2/5 |
  | 3 | 2 | 0.5 | 3/4, 0, 1/4 | 3/2, 0, 0 |
  | 4 | 2 | 0.67 | 8/9, 0, 0, 1/9 | 4/3, 0, 0, 0 |
  | 4 | 2 | 0.75 | 16/17, 0, 0, 1/17 | 64/51, 0, 0, −4/51 |
  | 3 | 3 | 0.27 | 4/7, 2/7, 1/7 | 25/12, −20/21, 37/84 |
  | 4 | 3 | 0.33 | 16/27, 0, 0, 11/27 | 16/9, 0, 0, 44/27 (as printed; see below) |
  | 5 | 3 | 0.5 | 25/32, 0, 0, 0, 7/32 | 25/16, 0, 0, 0, 5/16 |
  | 6 | 3 | 0.57 | 108/125, 0, 0, 0, 0, 17/125 | 36/25, 0, 0, 0, 0, 6/25 |
  | 4 | 4 | 0.15 | 29/72, 7/24, 1/4, 1/18 | 481/192, −1055/576, 937/576, −197/576 |
  | 6 | 4 | 0.245 | 747/1280, 0, 0, 0, 81/256, 1/10 | 237/128, 0, 0, 0, 165/128, −3/8 |
  | 5 | 5 | 0.077 | 1/4, 1/4, 7/24, 1/6, 1/24 | 185/64, −851/288, 91/24, −151/96, 199/576 |
  | 6 | 5 | 0.1298 | 7/20, 3/10, 4/15, 0, 7/120, 1/40 | 291201/108000, −198401/86400, 88063/43200, 0, −17969/43200, 73061/432000 |

  In exact arithmetic eleven rows satisfy the order conditions to the
  stated order and not the next, and $\min a_i/\vert b_i\vert$ reproduces
  the printed $\mathcal C$. The four-step third-order row does not: the
  printed $b_4 = 44/27$ fails the first condition. With $b_2 = b_3 = 0$ the
  conditions fix $b_4 = 4/9$, which gives third order and
  $\min a_i/\vert b_i\vert = 1/3$, the printed $\mathcal C$ (compiler's
  derivation, recorded beside the printed value). The first row is the
  optimal two-step method quoted above, in its first appearance; the
  three-step, four-step second-order, four-step third-order and five-step
  third-order rows are the fixed-step values above.
* *Source terms and several dimensions* (Propositions 3.2–3.4). With a
  source Lipschitz in $u$ and $x$ the methods are TVB of the same order.
  Applied dimension by dimension they keep their order, and they are
  bounded in the maximum norm for
  $\Delta t \le \frac{1}{2d}\min_i(a_i/\vert b_i\vert)\,\Delta t_{\mathrm{FE}}$
  with the one-dimensional $\Delta t_{\mathrm{FE}}$, a bound the
  conservation form doubles (Remark 3.4).
* No time-dependent test of these methods is in the paper; results are
  referred to Shu's TVB paper (p. 1079).

# Citations

1. [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §§1–6 (arXiv v2).
2. [Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §5.
3. [Shu (1998)](/sources/shu-1998.md), §4.2.2.
4. [Zhang & Shu (2010)](/sources/zhang-2010.md), Remark 2.7.
5. [Shu (1988b)](/sources/shu-1988-b.md), §3, Propositions 3.1–3.4, Corollary 3.1, Remarks 3.1–3.4, Table 1 (read from the page images).
