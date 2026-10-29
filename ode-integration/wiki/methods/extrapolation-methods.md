---
type: Method
title: "Extrapolation methods (Richardson extrapolation of a base integrator)"
description: "An extrapolation method combines several solutions of a low-order base method, computed with different substep counts, so that their leading errors cancel; per step it is a Runge–Kutta method with base-method stages and non-convex weights, used for positivity and bound preservation, and global extrapolation of the trapezoidal rule gives an A-stable fourth-order procedure."
status: established
aliases: [Richardson extrapolation, Richardson extrapolation of the trapezoidal rule, Aitken–Neville extrapolation, Euler extrapolation, extrapolated Euler, backward Euler extrapolation, ExE-RK5, BE extrapolation, IEX4, implicit Euler extrapolation]
tags: [runge-kutta, explicit, implicit, positivity, ssp]
timestamp: 2026-10-29T18:00:00Z
---

# Extrapolation methods (Richardson extrapolation of a base integrator)

An **extrapolation method** advances one step $h$ by computing $S$ approximations of
$y(t_n+h)$ with a first-order base method using $1,2,\dots,S$ equal substeps (the
*harmonic sequence*), and combines them with the Aitken–Neville weights that eliminate the
leading error terms, giving order $S$. With forward Euler as the base, every substep is an
explicit Euler step; with backward Euler, a linearly or fully implicit one. The sources
recall the construction from Hairer–Nørsett–Wanner (§II.9 and §IV.9) and write the
result as a [Runge–Kutta method](/definitions/runge-kutta-method.md) whose stages are the
substep values ([Kuzmin et al. 2022](/sources/kuzmin-2022.md), §3.1.2;
[Nüßlein et al. 2021](/sources/nusslein-2021.md), §4.1;
[Quezada de Luna & Ketcheson 2022](/sources/quezadadeluna-2022.md), §7.1).

## Global extrapolation of the trapezoidal rule and A-stability

[Dahlquist (1963)](/sources/dahlquist-1963.md) (§2, p. 33) uses extrapolation over the whole
integration rather than per step. Let $y(t,h)$ and $y(t,2h)$ (page-local) be trapezoidal-rule
solutions with steps $h$ and $2h$. "Without using the extrapolated values in the succeeding
computation", compute at $t=2h,4h,6h,\dots$

$$y^*(t,h)=y(t,h)+\tfrac13\big(y(t,h)-y(t,2h)\big)=\tfrac13\big(4y(t,h)-y(t,2h)\big).$$

He states that "one can prove" that its error is $O(h^4)$ for given $t$ and that the procedure is
A-stable "since it is obtained by subtraction of the results of two A-stable procedures", and
offers it as an A-stable procedure of order 4 outside the class covered by
[his order barrier](/results/dahlquist-second-barrier.md). If the extrapolated values are used in
the succeeding computation, A-stability is destroyed: with $R(z)=(1+z/2)/(1-z/2)$ the factor per
interval $2h$ is $\tfrac13\big(4R(z)^2-R(2z)\big)\to\tfrac53>1$ as $z\to-\infty$. *(Compiler
check, not in the sources: $R(z)\to-1$, so the limit is $\tfrac13(4+1)=\tfrac53$; without feedback
the value after $m$ intervals is $\tfrac13\big(4R(z)^{2m}-R(2z)^m\big)$, which tends to zero for
$\operatorname{Re}z<0$, as the asymptotic definition of
[A-stability](/properties/a-stability.md) requires.)* He names the order 2 of the trapezoidal
rule as one of its two disadvantages and says that it can be partly compensated by Richardson
extrapolation (§3, p. 42).

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
- **Backward Euler extrapolation with bound-preserving limiting.** Quezada de Luna &
  Ketcheson (2022, §7.1, Algorithm 1) write IEX$p$ explicitly: for $k=1,\dots,p$, $k$
  backward Euler substeps $Y_{k,j}=Y_{k,j-1}+\frac hkf(Y_{k,j})$ from $Y_{k,0}=y_n$ give
  $T_{k,1}=Y_{k,k}$, and the Aitken–Neville recursion
  $T_{j,k}=T_{j,k-1}+(T_{j,k-1}-T_{j-1,k-1})/\bigl(\frac j{j-k+1}-1\bigr)$ gives
  $y_{n+1}=T_{p,p}$ (page-local $Y_{k,j}$, $T_{j,k}$). As a Runge–Kutta method IEX4 has 10
  stages in four uncoupled lower-triangular blocks, with abscissae $1$; $\tfrac12,1$;
  $\tfrac13,\tfrac23,1$; $\tfrac14,\tfrac12,\tfrac34,1$, all entries of block $k$ equal to
  $\frac1k$, and weights
  $b=(-\tfrac16;\,2,2;\,-\tfrac92,-\tfrac92,-\tfrac92;\,\tfrac83,\tfrac83,\tfrac83,\tfrac83)$
  (Eq. (33)). These are the Aitken–Neville coefficients $(-\tfrac16,4,-\tfrac{27}2,\tfrac{32}3)$
  divided by the substep counts, the same as for explicit Euler extrapolation of order 4
  except that no first evaluation is shared *(compiler check, not in the sources: the explicit weights above
  are these with the four first-substep contributions summed, $-\tfrac16+2-\tfrac92+\tfrac83=0$)*.
  Every stage is a backward Euler substep, so the method satisfies the stage conditions
  $AX(r)\ge0$, $AX(r)\mathbf 1\le\mathbf 1$ for **every** $r>0$: its stages are
  unconditionally bound preserving when backward Euler is (Eq. (32), §7). The methods are
  A($\alpha$)-stable with $\alpha$ close to $90^\circ$, can have any order and parallelize
  well across the blocks, as recalled from Hairer–Wanner (§7.1). With GMC limiting of the
  final update, IEX4 keeps the global bounds on a linear advection–diffusion test with
  measured rates 3.63, 3.89 and 4.61 (Table 3, §8.1.1); see
  [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md).

## Qualifications

- **Printed slip in Kuzmin et al.** Algorithm 1 prints the outer loop "for $s=1\to S$",
  which would create an extra stage $y_n+hf(y_n)$ that neither Table 1 nor tableau (A.2)
  contains; pass $s$ adds $s-1$ stages, so the stage counts 2, 4, 7, 11 of Table 1 match a
  loop starting at $s=2$ *(compiler check of Algorithm 1, PDF p. 10)*.
- "Internal SSP" is a property of the stages under a forward Euler hypothesis. It is
  unrelated to [internal stability](/definitions/internal-stability.md), the propagation of
  round-off through the stages, despite the shared word.
- Apart from Dahlquist's (1963) global extrapolation of the trapezoidal rule, the sources use
  extrapolation at fixed order inside one step; order and step-size variation by extrapolation
  tableaux is not treated in them.
- Dahlquist (1963) gives no proof of the $O(h^4)$ error or of the A-stability of the passive
  procedure.

# Citations

- [Dahlquist (1963)](/sources/dahlquist-1963.md) — §2, p. 33 (Richardson extrapolation of the trapezoidal rule, with and without feedback); §3, p. 42.

- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §3.1.2 (Algorithm 1, Table 1, Eqs. (36)–(37)), §4, §5.2–5.3 (Tables 3–4), App. A.2 (Eq. (A.2)); arXiv v2.
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §4.1 (Table 2), §5.2–5.4; arXiv v2.
- [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) — §7 (Eq. (32)), §7.1 (Algorithm 1, Eq. (33)), §8.1.1 (Table 3); arXiv v1.
