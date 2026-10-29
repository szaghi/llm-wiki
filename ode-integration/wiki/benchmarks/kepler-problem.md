---
type: Benchmark
title: "Kepler problem"
description: "The planar two-body problem with three invariants (energy, angular momentum, Laplace–Runge–Lenz vector), its perturbed variant with a precessing orbit and a three-dimensional variant, used to test step-size control at high eccentricity, invariant-preserving relaxation methods, the modified equation of Störmer–Verlet and symmetry-constrained learned dynamics."
status: established
aliases: [two-body problem, Kepler two-body problem, perturbed Kepler problem, DETEST D5]
tags: [geometric-integration, structure-preserving, verification, step-size-control]
timestamp: 2026-10-29T18:13:00Z
---

# Kepler problem

The planar Kepler (two-body) problem for position $q\in\mathbb R^2$ and
momentum $p\in\mathbb R^2$ (page-local; $p$ is not the order here) is

$$q'=p,\qquad p'=-\frac{q}{\lVert q\rVert^3},$$

([Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md), §5.3.1, Eqs.
(27)–(29)). It has three independent invariants:

* the Hamiltonian $H=\tfrac12\lVert p\rVert^2-1/\lVert q\rVert$,
* the angular momentum $L=q_1p_2-q_2p_1$,
* the squared norm $\lVert V\rVert^2$ of the Laplace–Runge–Lenz vector
  $V=(p_1,p_2,0)^\top\times(0,0,L)^\top-(q_1,q_2,0)^\top/\lVert q\rVert$
  (cited by Biswas & Ketcheson to Hairer–Lubich–Wanner),

all with page-local symbols. With eccentricity $e$ the initial value is
$(q_1,q_2,p_1,p_2)=(1-e,\,0,\,0,\,\sqrt{(1+e)/(1-e)})$; the orbit is a
periodic ellipse. The Hamiltonian is separable, which is what lets
Störmer–Verlet split it into a kinetic and a potential part (below).

## Perturbed Kepler problem

Adding $-\mu_\star q/\lVert q\rVert^5$ to $p'$ (page-local $\mu_\star$) keeps $H$,
modified to $\tfrac12\lVert p\rVert^2-1/\lVert q\rVert-\mu_\star/(2\lVert q\rVert^3)$,
and $L$, but destroys the Laplace–Runge–Lenz invariant: the ellipse precesses
slowly. Biswas & Ketcheson (2023, §5.3.2, Eqs. (30)–(31)) use
$\mu_\star=0.005$, $e=0.6$, with a reference from SciPy's dopri5 dense output at
$\mathrm{rtol}=\mathrm{atol}=10^{-16}$.

## Uses in the sources

* **Step-size control at high eccentricity.** [Dormand & Prince (1980)](/sources/dormand-1980.md)
  (§4(b), Fig. 3) run problem D5 of the DETEST set of Hull et al., the planar two-body problem
  in first-order form with the initial value above, $e=0.9$, on $t\in[0,20]$. They call it "a
  severe test for the step-size control procedure since the step length must vary by about
  two orders of magnitude" over the orbit, and their pair RK5(4)7M is "again" the most efficient in their comparison of function
  evaluations against maximum global error. See
  [Dormand–Prince 5(4)](/methods/dormand-prince-5-4.md) and
  [step-size control](/methods/step-size-control.md).
* **Multiple relaxation.** Biswas & Ketcheson (2023) conserve all three
  invariants with multiple-relaxation versions of SSPRK(3,3) ($h=0.05$), RKF45
  ($h=0.05$) and DOPRI5 ($h=0.1$), each with two extra embedded methods, for
  $e=0.5$ to $t=200$: the invariants hold "almost to machine precision"
  against about four decimal places for the baselines, and the error grows
  linearly instead of quadratically (§5.3.1, Figs. 6–7). On the perturbed
  problem the relaxed methods conserve $H$ and $L$ to round-off and reproduce
  the precession; the third-order baseline's orbit departs visibly from the reference, and
  the higher-order baselines look right but their position error grows
  quadratically to 100% (§5.3.2, Figs. 8–10). See
  [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md).
* **Backward error analysis.** [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md)
  (§3.1.2) write Störmer–Verlet, split as $f^{[1]}=(p,0)$, $f^{[2]}=(0,\text{force})$,
  as a two-part additive Runge–Kutta method and compute its modified equation
  through $h^7$: it has no odd powers of $h$, as symmetry predicts. Its order-4
  modifying integrator puts $q$ in the right-hand side of $q'$ and is no longer
  explicit (Eq. (47)). This is a symbolic use of the problem: the paper runs no numerical
  solution of it. See
  [backward error analysis](/methods/backward-error-analysis.md) and
  [symplecticity](/properties/symplecticity.md).

## Three-dimensional variant for learned dynamics

[Müller (2023)](/sources/muller-2023.md) (§2.3.1, §3.1.1, Eq. (13)) uses the Kepler problem in
three dimensions, written through its Lagrangian $\tfrac12\lVert q'\rVert^2+1/\lVert q\rVert$
(unit mass and coupling; $q\in\mathbb R^3$ page-local as above), with eccentricity $e=0.8$,
motion in the $x$–$y$ plane and angular momentum $L_z=1$. Its rotational symmetry gives the
three components of the angular momentum as invariants. A neural-network Lagrangian is trained
on noisy samples of the exact orbit and the learned equations are advanced by RK4 at $h=10^{-2}$
to $T=128$. Without symmetry constraints the true angular momentum error reaches about 1 by
$t\approx50$ and the orbit then diverges. With an input layer of rotation invariants the learned
angular momentum is an exact invariant of the learned ODE, the true one stays within $10^{-3}$,
and trajectories from initial data perturbed by $10^{-3}$ separate by less than 0.1 over the run
(Figs. 3–5). See [learned time integrators](/methods/learned-time-integrators.md).

## Qualifications

* Ketcheson & Ranocha (2023, Eq. (43)) print the force as $+q/\lvert q\rvert^3$
  (repulsive); the Kepler problem is attractive, as Biswas & Ketcheson (2023)
  write it. The structure of their modified equation does not depend on the
  sign, but its coefficients do; no numerical solution is shown there.

# Citations

- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §5.3.1 (Eqs. (27)–(29), Figs. 6–7), §5.3.2 (Eqs. (30)–(31), Figs. 8–10).
- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §3.1.2 (Eqs. (43)–(47)).
- [Müller (2023)](/sources/muller-2023.md) — §2.3.1 (Eq. (13)), §3.1.1 (Figs. 3–5).
- [Dormand & Prince (1980)](/sources/dormand-1980.md) — §4(b), Fig. 3 (DETEST D5, $e=0.9$).
