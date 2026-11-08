---
type: Operator
title: "Spreading and interpolation operators $\\mathcal S$, $\\mathcal J$"
description: "The two coupling operators of the classical immersed boundary method built on the same regularized delta function: spreading maps Lagrangian densities to Eulerian densities, interpolation maps Eulerian values to Lagrangian points, and spreading is the adjoint of interpolation, which makes force, torque, momentum and power identical in the two descriptions."
status: established
symbol: "$\\mathcal S$, $\\mathcal J$"
aliases: [force spreading, velocity interpolation, interaction equations, Lagrangian–Eulerian transfer]
tags: [immersed-boundary, coupling-operator, conservation, delta-function]
timestamp: 2026-11-08T17:31:00Z
---

# Spreading and interpolation operators $\mathcal S$, $\mathcal J$

The interaction equations of the [classical immersed boundary method](/methods/classical-immersed-boundary-method.md)
become, on an Eulerian grid of width $h$ and a Lagrangian grid of points
$\mathbf X_\ell$ with measure $\Delta s_\ell$
([Peskin 2002](/sources/peskin-2002.md), §4; [Peskin 1972](/sources/peskin-1972.md), eqs. 3.21–3.22):

$$\begin{aligned}
\mathbf f_{\mathbf i}=(\mathcal S\mathbf F)_{\mathbf i}&=\sum_\ell \mathbf F_\ell\,\delta_h(\mathbf x_{\mathbf i}-\mathbf X_\ell)\,\Delta s_\ell ,\\
\mathbf U_\ell=(\mathcal J\mathbf u)_\ell&=\sum_{\mathbf i}\mathbf u_{\mathbf i}\,\delta_h(\mathbf x_{\mathbf i}-\mathbf X_\ell)\,h^d ,\qquad \frac{d\mathbf X_\ell}{dt}=\mathbf U_\ell ,
\end{aligned}$$

with the [regularized delta function](/operators/regularized-delta-function.md)
$\delta_h$. The same formula with the Lagrangian mass density in place of
$\mathbf F$ spreads mass. Spreading relates **densities** (the values of
$\mathbf f$ and $\mathbf F$ differ at corresponding points), interpolation
relates **values** (the boundary moves at the interpolated fluid velocity);
Peskin (2002, §2) traces the difference to the map $\mathbf s\mapsto\mathbf X$
inside the delta's argument.

## Identities

**Adjointness.** For any $\delta_h$, with $\langle\mathbf f,\mathbf u\rangle_h=\sum_{\mathbf i}\mathbf f_{\mathbf i}\cdot\mathbf u_{\mathbf i}h^d$
and $\langle\mathbf F,\mathbf U\rangle_\Gamma=\sum_\ell\mathbf F_\ell\cdot\mathbf U_\ell\Delta s_\ell$,

$$\langle\mathcal S\mathbf F,\mathbf u\rangle_h=\langle\mathbf F,\mathcal J\mathbf u\rangle_\Gamma ,\qquad \mathcal S=\mathcal J^{*}.$$

It follows that the power delivered to the fluid equals the power done by
the structure and that the Eulerian and Lagrangian momenta agree. The
argument "only works because the same kernel $\delta_h(\mathbf x-\mathbf X)$
is used in the spreading step and in the interpolation step" (Peskin 2002, §5).

**Force and torque.** If $\sum_{\mathbf i}\delta_h(\mathbf x_{\mathbf i}-\mathbf X)h^d=1$
and $\sum_{\mathbf i}(\mathbf x_{\mathbf i}-\mathbf X)\delta_h(\mathbf x_{\mathbf i}-\mathbf X)h^d=\mathbf 0$
for every real shift $\mathbf X$, then
$\sum_{\mathbf i}\mathbf f_{\mathbf i}h^d=\sum_\ell\mathbf F_\ell\Delta s_\ell$
(total force), the same for mass, and
$\sum_{\mathbf i}\mathbf x_{\mathbf i}\times\mathbf f_{\mathbf i}h^d=\sum_\ell\mathbf X_\ell\times\mathbf F_\ell\Delta s_\ell$
(total torque) (Peskin 2002, §5). The interaction equations therefore
neither create nor destroy momentum, angular momentum or energy; whether the
whole scheme conserves them depends on the fluid solver
([discrete conservation](/properties/discrete-conservation.md)).

## Qualifications

- No analogous identities hold for angular momentum or kinetic energy
  themselves (Peskin 2002, §5).
- The interpolated velocity field is not discretely divergence-free, so the
  enclosed volume of a closed boundary drifts (Peskin 2002, §8, citing Peskin
  and Printz 1993).
- Peskin (1972, §III.B) uses $\mathbf X^n$ as the argument of $\delta_h$ in
  both operators and notes that the implicit choice $\mathbf X^{n+1}$ is
  equally consistent; the fixed-point iteration converges when
  $u_{\max}\Delta t<h/4$, which he takes as a necessary accuracy condition.

# Citations

- [Peskin (1972)](/sources/peskin-1972.md) — §III.B, §III.D, eqs. (3.21)–(3.26).
- [Peskin (2002)](/sources/peskin-2002.md) — §2, §4, §5, §8.
