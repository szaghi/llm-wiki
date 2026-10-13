---
type: Result
title: "Nonconvexity of ideal MHD and compound waves"
description: "Ideal MHD is nonconvex: near a vanishing tangential field the fast or the slow characteristic field is neither genuinely nonlinear nor linearly degenerate, so a shock can carry an attached rarefaction (a compound wave containing an intermediate shock); whether such solutions are physical, and so whether the MHD Riemann problem is unique, is unsettled in the corpus."
status: established
aliases: [MHD is not genuinely nonlinear, compound wave, MHD nonconvexity, intermediate shock]
tags: [mhd, riemann-problem, eigenvectors]
timestamp: 2026-10-13T00:00:00Z
---

# Nonconvexity of ideal MHD and compound waves

**Setting.** The 1D ideal-MHD system has seven characteristic fields,
with eigenvalues $v_x \mp c_f$, $v_x \mp c_A$, $v_x \mp c_s$ and $v_x$.
A characteristic field, of index $(p)$ (the bracketed field index,
distinct from the pressure $p$ used below), is genuinely nonlinear if
$\nabla_u\lambda^{(p)}\cdot r^{(p)} \ne 0$ for all states, and linearly
degenerate if $\nabla_u\lambda^{(p)}\cdot r^{(p)} \equiv 0$ (Brio and
Wu's definition, along the shock curve, §VI); a system is called convex
when every field is one or the other.

**Statement** ([Brio & Wu (1988)](/sources/brio-1988.md), §VI). With
the complete, renormalized eigenvectors
([local characteristic decomposition](/methods/characteristic-decomposition.md)),
and $B_z = 0$, $\nabla_u\lambda^{(p)}\cdot r^{(p)}$ is proportional to
$B_y$ near $B_y = 0$
* for the fast fields when $c^2 < c_A^2$, and
* for the slow fields when $c^2 > c_A^2$.

These fields change the sign of $\nabla_u\lambda^{(p)}\cdot r^{(p)}$
where the tangential field changes sign, so they are neither genuinely
nonlinear nor linearly degenerate: ideal MHD is nonconvex. The earlier
conclusion that the fast and slow fields are genuinely nonlinear
(Jeffrey and Taniuti's Theorem E.1) "is not correct, since the set (34)
is not complete": it rested on eigenvectors that degenerate exactly
where the sign change happens.

**Consequence: compound waves** (§VI, eqs. 54–55). An expansion of the
slow shock curve for small tangential field, with the pre-shock state
$\rho = 1$, $v_x = 0$, $B_x = 1$, $p = 1$, $\gamma = 2$, gives both the
slow characteristic speed behind the shock and the shock speed as $-1$
plus terms quadratic in the pre- and post-shock $B_y$. The two curves
cross where the post-shock $B_y$ is $-\tfrac12$ times the pre-shock
$B_y$; there the shock speed is stationary along the shock curve, and a
slow rarefaction can travel attached behind the shock. Because $B_y$
changes sign across this shock, it is an intermediate shock. In the
[Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) the slow compound
wave runs from $B_y = 0.5849$ (the numerical left state Brio and Wu use to solve the jump relations) ahead of the shock to $-0.3073$ at the
point where the shock speed ($-0.2995$) equals the slow characteristic
speed, and to $-0.5341$ at the tail of the rarefaction, where the
analytic and second-order upwind states agree to within 0.005 (Figs.
8–9). Ryu and Jones find the same structure at $\gamma = 5/3$, a "2-4"
intermediate shock followed by a slow rarefaction, and a fast analogue
for planar fields, a "1-3" intermediate shock preceded by a fast
rarefaction ([Ryu & Jones (1995)](/sources/ryu-1995.md), §5;
[Ryu–Jones shock tubes](/benchmarks/ryu-jones-shock-tubes.md), set 5).

**What is not settled.** The nonconvexity is proved; the admissibility
of the intermediate shock it allows is not, and the corpus holds three
positions that are compatible with each other but do not close the
question.
* Brio and Wu: if intermediate shocks were inadmissible, then "all
  numerical schemes tested in Section 5 admit nonphysical shocks". They
  cite Wu (1987), whose resistive-MHD runs form some intermediate shocks,
  this one included, by steepening of a continuous wave (§VI).
* Dai and Woodward exclude intermediate shocks from their nonlinear
  solver and find, for the Brio–Wu states at $\gamma = 2$, a regular
  solution with two slow shocks and a rotational discontinuity of about
  180° instead of the compound wave. A simulation from the post-fast-wave
  states still forms the compound wave, which "will be generated through
  the conservation law … no matter what approximation we use"; they
  conclude that "this Riemann problem does not have a unique solution"
  ([Dai & Woodward (1994)](/sources/dai-1994.md), p. 368, §6).
* Ryu and Jones take no side on the reality of intermediate shocks; their
  code and their solver disagree only at compound waves (§5).

**Consequences for capturing schemes.**
* Because intermediate-shock structure is not unique, a capturing
  scheme's result can depend on its numerical dissipation and may fail
  to converge under refinement ([Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 4).
  Dai and Woodward likewise leave the treatment of degenerate speeds,
  where the solution can depend on the neglected dissipation, to the
  programmer (p. 359).
* [Balsara (2017)](/sources/balsara-2017-d.md), §II.1, citing Ibáñez et
  al. (2015), cautions that in non-convex MHD and relativistic MHD the
  nonlinear wave families "might give rise to their own further
  pathologies" for family-specific limiting.
* Nonconvexity "was first discovered by using the upwind scheme" on the
  Brio–Wu test (Brio & Wu, §VII), and the slow intermediate shock is
  admitted by all four schemes they compared (upwind, Lax–Friedrichs,
  Lax–Wendroff, FCT; §VI). In a variant with right $B_y = -0.4$ an almost
  stationary slow intermediate shock forms, on which Lax–Wendroff could
  not be stabilized "with any value of artificial viscosity" (§V).

**Later uses (batch 16).** *Closed forms and the triple umbilic*
([Roe & Balsara (1996)](/sources/roe-1996.md), §§3–5, eqs. 19–24).
* *Structure coefficients.* With the orthonormal eigenvectors of
  [local characteristic decomposition](/methods/characteristic-decomposition.md)
  (batch 16), $\nabla\lambda^{(p)}\cdot r^{(p)}$ taken in primitive
  variables is, for an ideal gas,
  $$\alpha_f c_f\left[\tfrac{\gamma+1}{2}\alpha_f^2 + \tfrac32\alpha_s^2\right]\ \text{(fast fields)},\qquad \alpha_s c_s\left[\tfrac{\gamma+1}{2}\alpha_s^2 + \tfrac32\alpha_f^2\right]\ \text{(slow fields)}$$
  (eqs. 23–24; for a general equation of
  state $\tfrac{\gamma+1}{2}$ becomes one plus the logarithmic density
  derivative of $c$ at constant entropy). With $\alpha_f = 1$, $\alpha_s = 0$
  (fast) or $\alpha_s = 1$, $\alpha_f = 0$ (slow), the wave in the guise of
  an acoustic wave, they reduce to the acoustic result. Near $B_\perp = 0$ the vanishing factor is
  $\alpha_f$ when $c^2 < c_A^2$ and $\alpha_s$ when $c^2 > c_A^2$, and
  $\alpha_f\alpha_s$ is proportional to $B_\perp$: the same fields and
  conditions as the Brio–Wu statement above, which Roe and Balsara call
  "the 'loss of convexity' first observed in" Brio and Wu. There the wave
  is "neither expansive nor compressive".
* *Wave paths near the triple umbilic* (§3, Fig. 3). Fast and slow
  integral curves near the point where $c_A = c$ and $B_\perp = 0$ have a
  topology of Schaeffer–Shearer type IV, of a shape independent of
  $\gamma$ (integrated for $\gamma = 5/3$). The dissipationless Riemann
  problem is then well posed "if compressive shocks are the only ones
  admitted" (citing Isaacson et al.). Whether a scheme without modelled
  dissipation captures the dissipative internal structure of waves near
  the point is "an open question" (§4). Both statements fit **What is not
  settled** above without closing it.
* *Entropy fixes* (§5). Zachary and Colella add dissipation from the
  structure coefficients, after Bell, Colella and Trangenstein. That extra
  dissipation is needed only at stationary sonic points, as Roe found for
  Euler, "appears to be confirmed" for MHD by Aslan's thesis, "but only
  extensive testing will decide the issue".

# Citations

1. [Brio & Wu (1988)](/sources/brio-1988.md), §§IV.3, V–VII, eqs. 53–55, Figs. 8–9.
2. [Dai & Woodward (1994)](/sources/dai-1994.md), pp. 359–360, 368, §6.
3. [Ryu & Jones (1995)](/sources/ryu-1995.md), §5.
4. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 4.
5. [Balsara (2017)](/sources/balsara-2017-d.md), §II.1.
6. [Roe & Balsara (1996)](/sources/roe-1996.md), §§3–5, eqs. 19–24.
