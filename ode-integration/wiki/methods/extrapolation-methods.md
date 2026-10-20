---
type: Method
title: "Extrapolation methods (Richardson extrapolation of a base integrator)"
description: "An extrapolation method combines several solutions of a low-order base method over one step, computed with different substep counts, so that their leading errors cancel; written as a Runge–Kutta method it has stages that are base-method steps and non-convex final weights, which the sources exploit for positivity and bound preservation."
status: established
aliases: [Richardson extrapolation, Aitken–Neville extrapolation, Euler extrapolation, extrapolated Euler, backward Euler extrapolation, ExE-RK5, BE extrapolation]
tags: [runge-kutta, explicit, implicit, positivity, ssp]
timestamp: 2026-10-20T10:00:00Z
---

# Extrapolation methods (Richardson extrapolation of a base integrator)

An **extrapolation method** advances one step $h$ by computing $S$ approximations of
$y(t_n+h)$ with a first-order base method using $1,2,\dots,S$ equal substeps (the
*harmonic sequence*), and combines them with the Aitken–Neville weights that eliminate the
leading error terms, giving order $S$. With forward Euler as the base, every substep is an
explicit Euler step; with backward Euler, a linearly or fully implicit one. Both sources
recall the construction from Hairer–Nørsett–Wanner (§II.9 and §IV.9) and write the
result as a [Runge–Kutta method](/definitions/runge-kutta-method.md) whose stages are the
substep values ([Kuzmin et al. 2022](/sources/kuzmin-2022.md), §3.1.2;
[Nüßlein et al. 2021](/sources/nusslein-2021.md), §4.1).

## Explicit Euler extrapolation as a Runge–Kutta method

Kuzmin et al. (2022, §3.1.2, Algorithm 1, Table 1, App. A.2) give the Butcher form. The
sequence with $s$ substeps of size $h/s$ shares the first evaluation $f(y_n)$, so order $S$
needs $1+S(S-1)/2$ stages: 2, 4, 7 and 11 for orders 2–5 *(compiler count, not in the
sources)*. The weights, in the order in which the substeps are generated, are

| order | stages | $b$ |
|---|---|---|
| 2 | 2 | $(0,1)$ (explicit midpoint) |
| 3 | 4 | $(0,-2,\tfrac32,\tfrac32)$ |
| 4 | 7 | $(0,2,-\tfrac92,-\tfrac92,\tfrac83,\tfrac83,\tfrac83)$ |
| 5 | 11 | $(0,-\tfrac43,\tfrac{27}4,\tfrac{27}4,-\tfrac{32}3,-\tfrac{32}3,-\tfrac{32}3,\tfrac{125}{24},\tfrac{125}{24},\tfrac{125}{24},\tfrac{125}{24})$ |

For the fifth-order method ExE-RK5 the abscissae are
$c=(0,\tfrac12,\tfrac13,\tfrac23,\tfrac14,\tfrac12,\tfrac34,\tfrac15,\tfrac25,\tfrac35,\tfrac45)$
and every stage is one Euler substep from $y_n$ or from the previous stage of its sequence
(Eq. (A.2)); the final value is the Aitken–Neville combination
$\tfrac1{24}T_1-\tfrac83T_2+\tfrac{81}4T_3-\tfrac{128}3T_4+\tfrac{625}{24}T_5$ of the five
end values $T_s$ (page-local), whose coefficients sum to 1 and reproduce the weights above
*(compiler check, not in the sources: the Aitken–Neville coefficient of $T_j$ is
$\prod_{l\ne j}j/(j-l)$, and stage weights are these divided by $s$, summed over the shared
first stage)*.

## Positivity and bound preservation

The structure splits the method into a positive part and a non-convex combination:

- **Stages.** Every stage is a forward Euler step of size $h/s$ from a stage that is
  itself such a step, so if forward Euler preserves a convex bound for steps up to
  $h_{\mathrm{FE}}$, all stages preserve it for $h$ up to a multiple of $h_{\mathrm{FE}}$.
  Kuzmin et al. call such methods **internal SSP**: they satisfy the stage half of the SSP
  conditions, $AX\ge0$ and $AX\mathbf 1\le\mathbf 1$ with $X=(I+rA)^{-1}$ for some $r>0$,
  but possibly not the weight half (§3.1.2, Eqs. (36)–(37); see
  [SSP methods](/methods/strong-stability-preserving-runge-kutta.md)). Euler extrapolation
  "can be constructed to have any desired order", so the class has no order barrier.
- **Final combination.** The Aitken–Neville weights have mixed signs (table above), so the
  update is not a convex combination and need not preserve bounds. Kuzmin et al. limit only
  that final update, and the intermediate stages with GMC bounds, with their
  [bound-preserving flux limiter](/methods/bound-preserving-flux-limiting.md) (ExE-RK5-GMC,
  §4). On smooth linear advection with WENO5, unlimited ExE-RK5 converges at order 5.00 on
  the finest grid, against 4.29 for the fourth-order SSP54 (Table 3); the limited version
  keeps the rate with relaxation parameter 1 and falls to 2.66 without relaxation; on
  Burgers it needs a larger relaxation (2) than the other methods (Table 4).
- **Backward Euler extrapolation.** Nüßlein et al. (2021) use backward-Euler extrapolation
  of orders 2, 3 and 4 (harmonic sequence, $s=3,6,10$ stages) as their preferred bases for
  [adaptive-weight Runge–Kutta methods](/methods/adaptive-weight-runge-kutta.md). All stages
  are backward Euler steps, hence nonnegative for every $h$ when the ODE satisfies
  $y_i=0\Rightarrow f_i\ge0$; the chain of substeps is an embedded first-order solution that
  is always nonnegative; and the weights have 2, 5 and 9 free directions at first order and
  1, 2 and 3 at full order, so they can be adapted without order loss (§4.1, Table 2). They
  integrate a heat equation, an advection–diffusion–production–destruction problem and the
  [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md) with the
  third-order variant (§5.2–5.4).

## Qualifications

- **Printed slip in Kuzmin et al.** Algorithm 1 prints the outer loop "for $s=1\to S$",
  which would create an extra stage $y_n+hf(y_n)$ that neither Table 1 nor tableau (A.2)
  contains; pass $s$ adds $s-1$ stages, so the stage counts 2, 4, 7, 11 of Table 1 match a
  loop starting at $s=2$ *(compiler check of Algorithm 1, PDF p. 10)*.
- "Internal SSP" is a property of the stages under a forward Euler hypothesis. It is
  unrelated to [internal stability](/definitions/internal-stability.md), the propagation of
  round-off through the stages, despite the shared word.
- The sources use extrapolation at fixed order inside one step; order and step-size
  variation by extrapolation tableaux, the classical use of the method, is not treated in
  them.

# Citations

- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §3.1.2 (Algorithm 1, Table 1, Eqs. (36)–(37)), §4, §5.2–5.3 (Tables 3–4), App. A.2 (Eq. (A.2)); arXiv v2.
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §4.1 (Table 2), §5.2–5.4; arXiv v2.
