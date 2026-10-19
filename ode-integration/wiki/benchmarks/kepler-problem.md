---
type: Benchmark
title: "Kepler problem"
description: "The planar two-body problem with three invariants (energy, angular momentum, Laplace–Runge–Lenz vector), and its perturbed variant with a precessing orbit, used to test invariant-preserving relaxation methods and the modified equation of Störmer–Verlet."
status: established
aliases: [two-body problem, Kepler two-body problem, perturbed Kepler problem]
tags: [geometric-integration, structure-preserving, verification]
timestamp: 2026-10-19T20:00:00Z
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

* **Multiple relaxation.** Biswas & Ketcheson (2023) conserve all three
  invariants with multiple-relaxation versions of SSPRK(3,3) ($h=0.05$), RKF45
  ($h=0.05$) and DOPRI5 ($h=0.1$), each with two extra embedded methods, for
  $e=0.5$ to $t=200$: the invariants hold "almost to machine precision"
  against about four decimal places for the baselines, and the error grows
  linearly instead of quadratically (§5.3.1, Figs. 6–7). On the perturbed
  problem the relaxed methods conserve $H$ and $L$ to round-off and reproduce
  the precession; the third-order baseline gets the orbit visibly wrong, and
  the higher-order baselines look right but their position error grows
  quadratically to 100% (§5.3.2, Figs. 8–10). See
  [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md).
* **Backward error analysis.** [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md)
  (§3.1.2) write Störmer–Verlet, split as $f^{[1]}=(p,0)$, $f^{[2]}=(0,\text{force})$,
  as a two-part additive Runge–Kutta method and compute its modified equation
  through $h^7$: it has no odd powers of $h$, as symmetry predicts. Its order-4
  modifying integrator puts $q$ in the right-hand side of $q'$ and is no longer
  explicit (Eq. (47)). See
  [backward error analysis](/methods/backward-error-analysis.md) and
  [symplecticity](/properties/symplecticity.md).

## Qualifications

* Ketcheson & Ranocha (2023, Eq. (43)) print the force as $+q/\lvert q\rvert^3$
  (repulsive); the Kepler problem is attractive, as Biswas & Ketcheson (2023)
  write it. The structure of their modified equation does not depend on the
  sign, but its coefficients do; no numerical solution is shown there.

# Citations

- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §5.3.1 (Eqs. (27)–(29), Figs. 6–7), §5.3.2 (Eqs. (30)–(31), Figs. 8–10).
- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §3.1.2 (Eqs. (43)–(47)).
