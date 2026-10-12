---
type: Method
title: "Positivity-preserving adaptive Runge–Kutta methods"
description: "Enforce componentwise positivity (or box bounds) of a Runge–Kutta step after the stages are computed, by solving a linear program for new weights closest in ℓ1 to the original ones subject to the bounds and the order conditions up to a possibly reduced order; conserves every linear invariant, unlike clipping, and pays off mainly for implicit methods."
status: established
aliases: [weight-adaptive Runge-Kutta, LP-adapted Runge-Kutta weights, positivity-adaptive RK]
tags: [time-discretization, runge-kutta, positivity]
timestamp: 2026-10-12T00:00:00Z
---

# Positivity-preserving adaptive Runge–Kutta methods

Once the stages $Y_j$ of a [Runge–Kutta step](/methods/explicit-runge-kutta.md)
are known, the update $u^{n+1} = u^n + \Delta t\sum_j\mathsf b_j\mathcal L(Y_j)$
is linear in the weights, and so are the order conditions for fixed
$\mathsf a_{ij}$, $\mathsf c_i$. [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md)
use this to make the step output nonnegative (§§2–3):
* **Free adaptation** (LP 3.1). Minimize $\Vert\tilde{\mathsf b} - \mathsf b\Vert_1$
  subject to $u^n + \Delta t\sum_j\tilde{\mathsf b}_j\mathcal L(Y_j) \ge 0$
  componentwise and the order conditions up to order
  $\tilde p_{\mathrm t}$. If $u^{n+1}$ is already nonnegative the program
  returns $\mathsf b$.
* **Convex adaptation** (LP 3.2). Take $\tilde{\mathsf b}$ as a convex
  combination of preselected weight vectors (embedded methods; forward or
  backward Euler as a last resort); the order is the lowest among them.
* **Degrees of freedom.** The order conditions must leave room:
  $\tilde p_{\mathrm t} < s$ in effect. Classical RK4 has no free weights
  at order 3; SSP-RK(10,4) keeps four at full order 4; the
  Cash–Karp and Dormand–Prince pairs must drop order (§4.1, Table 1).
* **Algorithm** (§3.4). Lower $\tilde p_{\mathrm t}$ until the program is
  feasible and the perturbation is within tolerance; otherwise reduce
  $\Delta t$ and redo the step. Positivity is imposed only on the
  components that go negative, an active set that converged in at most
  two iterations in the tests (§3.3). The perturbation enters the error
  estimate of [step-size control](/methods/runge-kutta-step-size-control.md) (§4.2).

**What it preserves.** Every adapted step is still a Runge–Kutta step,
so all linear invariants (mass) hold exactly; setting negative values to
zero breaks them (§§1–2). Only $u^{n+1}$ is constrained: stages may go
negative, so $\mathcal L$ must be defined for negative arguments (§5.1).
This differs from the stage-wise limiting of
[positivity preservation](/properties/positivity-preserving.md), which
keeps every stage admissible. The bounds must be linear in
$\tilde{\mathsf b}$, so the method as written covers componentwise bounds
(densities, concentrations), not the pressure of the Euler equations
(compiler's observation; the paper treats only ODEs and scalar
linear PDEs).

**What is proved** (§4.3). A convex combination of weight vectors keeps
the intersection of their stability regions (Theorem 4.1), so A-stable
components give an A-stable method; the stability function changes by at
most $\Vert\tilde{\mathsf b} - \mathsf b\Vert_1$ times a bounded factor
(Lemma 4.2), which motivates the $\ell_1$ objective. Feasibility for
explicit methods, convergence of the adapted sequence and the global
order are observed, not proved.

**Where it pays off.** For explicit methods the useful window is narrow:
on advection with decay, Dormand–Prince stays positive unaided for
$\Delta t \le 0.0082$ and is unstable beyond $0.016$, so adaptation helps
only between (§5.1), and a smaller step is usually cheaper. With
diagonally implicit or backward-Euler extrapolation methods the step is
not stability-limited and a first-order fallback is always feasible; the
heat-equation and production–destruction tests keep positivity and
invariants to round-off (§§5.2–5.4, §6).

Background (§1): no Runge–Kutta or general linear method that is
unconditionally positive for all positive ODEs exceeds first order
(Bolley & Crouzeix, cited, not in the corpus); SSP methods are positive
for $\Delta t \le \mathcal C\,\Delta t_{\mathrm{FE}}$, and this method
targets steps beyond that limit.

# Citations

1. [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §§1–6 (arXiv v2).
