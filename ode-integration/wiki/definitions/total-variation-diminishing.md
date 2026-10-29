---
type: Definition
title: "Total variation diminishing (TVD) time stepping"
description: "A time discretization of a method-of-lines system is TVD when the total variation of the grid function does not grow over a step; Shu and Osher define r-th order TVD time discretizations relative to one forward Euler step, and Gottlieb, Shu and Tadmor rename them strong stability preserving."
status: established
aliases: [TVD, total variation diminishing, TVD time discretization, TVD Runge–Kutta, total variation bounded, TVB]
tags: [ssp, stability, structure-preserving, explicit]
timestamp: 2026-10-29T18:13:00Z
---

# Total variation diminishing (TVD) time stepping

For a grid function $y=(y_j)$ the total variation is
$\mathrm{TV}(y)=\sum_j\lvert y_{j+1}-y_j\rvert$, with $j$ the spatial index. A scheme
is **total variation diminishing** (TVD) when $\mathrm{TV}(y_{n+1})\le\mathrm{TV}(y_n)$,
and **total variation bounded** (TVB) on $0\le t\le T$ when
$\mathrm{TV}(y_n)\le B$ for a constant $B$ that depends only on $\mathrm{TV}(y_0)$, for all
$n$ and $h$ with $0\le nh\le T$
([Shu & Osher (1988)](/sources/shu-1988.md), §I, Eqs. (1.5)–(1.7), citing Harten). The
setting is the method-of-lines system $y'=f(y)$ obtained from a conservation law: its
right-hand side $f$ is a spatial discretization of order $r$, and forward Euler is
assumed TVD under a CFL restriction. Gottlieb, Shu & Tadmor state the same hypothesis as
$\mathrm{TV}(y_n+hf(y_n))\le\mathrm{TV}(y_n)$ for $h\le h_{\mathrm{FE}}$
([Gottlieb et al. (2001)](/sources/gottlieb-2001.md), §2.1, Eqs. (2.3)–(2.5)).

## TVD time discretizations (Shu & Osher)

Shu & Osher (1988, §II, Eqs. (2.1)–(2.6)) write one forward Euler step as
$T(y)=y+hf(y)$ and seek a one-step map $y_{n+1}=S(y_n)$ with

1. local accuracy $O(\Delta x^{r+1})$ on smooth solutions (2.4), and
2. $\mathrm{TV}(S(y))\le\mathrm{TV}(T(y))$ under a restriction on $h$, or equivalently on
   the CFL number (2.5).

They call such a map an "$r$-th order TVD" time discretization. Condition (2.5)
compares the new total variation with that after **one forward Euler step**, not with
$\mathrm{TV}(y)$. So if $T$ is TVD, $\mathrm{TV}(T(y))\le\mathrm{TV}(y)$ (2.6a), $S$ is TVD,
and if $T$ is only TVB, $\mathrm{TV}(T(y))\le\mathrm{TV}(y)+M'h$ with a bounded
constant $M'\ge0$ (page-local; (2.6b)), $S$ is TVB.

Runge–Kutta methods written as convex combinations of forward Euler steps satisfy (2.5):
this is Shu & Osher's Prop. 2.1, which Gottlieb et al. (2001, §2.2, Lemmas 2.1–2.2) recall
for [strong-stability-preserving Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
(the CFL number of such a method is $\min\alpha_{ij}/\lvert\beta_{ij}\rvert$ times the forward
Euler bound, with the downwind operator $\tilde L$ in the terms with $\beta_{ij}<0$). Remark 2.1 of the same
paper already replaces $\mathrm{TV}$ by "any convex mapping into the non-negative real line"
on a Banach space of grid functions, with the conclusion that this functional does not grow
from step to step and the formal order stays $r$ (§II, p. 10).

## From TVD to SSP

Gottlieb et al. (2001, abstract, §1, §2.1) rename these methods: "Previously termed TVD
(total variation diminishing) time discretizations", they are now **strong stability
preserving** (SSP), because the proof rests only on convexity and so "any convex function
will be preserved", including the total variation, maximum norms, weighted $L^2$ norms and
cell entropies. The TVB-type hypothesis $\lVert y+hf(y)\rVert\le(1+O(h))\lVert y\rVert$ is
preserved as well. If forward Euler is not strongly stable, "the framework in this paper
cannot be used" (§2.1). The older name survives in later sources: Southworth et al.
(2024, §5.2) compare with a split scheme whose hydrodynamics step is TVD-RK3 (see the
[SSP page](/methods/strong-stability-preserving-runge-kutta.md)). The three-stage
third-order method of Shu & Osher is their Eq. (2.18).

## Why total variation and not linear stability

Shu & Osher (1988, §I, p. 5) state that linear stability analysis is "certainly not enough"
for shock problems, because "linear stability does not imply convergence if shocks or other
discontinuities are present", and that it does not apply to ENO schemes at all, whose
stencils move. They also state that for Lax–Wendroff (Taylor-series) time discretizations
"only second order in time TVD or TVB schemes exist", and that TVD or TVB is "not easy to
prove" for them even when the semi-discrete system and its forward Euler step are TVD or TVB
(§I, pp. 4–5); see [ADER time integration](/methods/ader-time-integration.md) for the
Taylor-series route. For the ENO spatial operators they use, there is no proof that forward
Euler is TVB; analysis and experiments "strongly support that the total variation increase
at each step is $O(\Delta x^r)$" (§II, pp. 14–15).

Gottlieb et al. (2001, §2.1, Fig. 2.1, reproduced from Gottlieb–Shu) show the consequence
on a [Burgers](/benchmarks/burgers-equation.md) Riemann problem with a second-order TVD MUSCL
discretization: an SSP second-order Runge–Kutta method gives a non-oscillatory shock, while a
second-order method that is linearly stable but not SSP produces an overshoot.

## Implicit time stepping

Backward Euler is TVD for every step size when the spatial scheme has Harten's incremental
form: Gottlieb et al. (2001, §6.1, Lemma 6.1) prove that
$y_{n+1,j}=y_{n,j}+h\bigl(C_{j+\frac12}(y_{n+1,j+1}-y_{n+1,j})-D_{j-\frac12}(y_{n+1,j}-y_{n+1,j-1})\bigr)$
with nonnegative coefficients $C_{j+\frac12},D_{j-\frac12}$ (page-local; functions of
$y_n$ and/or $y_{n+1}$) is TVD for arbitrary $h$. Beyond first order the property is lost in
the classes they analyse: implicit Runge–Kutta methods with one implicit evaluation per
stage and no explicit terms (their form (6.7)), and implicit multistep methods with only
the implicit term (form (6.16)), cannot have all $\alpha\ge0$ at order $\ge2$ (Props.
6.2–6.3). With explicit terms admitted, SSP methods exist under step restrictions similar
to those of explicit methods (§6.2–6.3). On step data for
[linear advection](/benchmarks/linear-advection-equation.md) with first-order upwinding at
$h/\Delta x=1.4$, backward Euler stays monotone while a second-order implicit method of the
analysed family oscillates (§6.1, Fig. 6.1).
[Orlando & Bonaventura (2025)](/sources/orlando-2025.md) (§3) recall that implicit
methods of order above one cannot be unconditionally TVD for hyperbolic problems, and that
the same holds for IMEX methods.

## Qualifications

- Shu & Osher's TVD condition (2.5) is stated relative to $\mathrm{TV}(T(y))$, and they
  draw $\mathrm{TV}(S(y))\le\mathrm{TV}(y)$ from it when $T$ is TVD (2.6a); Gottlieb et al.
  (2001, §2.1) state the conclusion directly as $\mathrm{TV}(y_{n+1})\le\mathrm{TV}(y_n)$
  under the forward Euler hypothesis.
- In both papers the TVD property of the time discretization is conditional on the spatial
  operator: on a TVD forward Euler step (Shu & Osher 1988, Eqs. (2.6)–(2.7); Gottlieb et al.
  2001, §2.1) or, for implicit methods, on a TVD backward Euler step (Gottlieb et al. 2001,
  §6).

# Citations

- [Shu & Osher (1988)](/sources/shu-1988.md) — §I (Eqs. (1.5)–(1.7), pp. 4–5), §II (Eqs. (2.1)–(2.6), Prop. 2.1, Remark 2.1, Eq. (2.18), pp. 14–15); read as ICASE Report 87-33.
- [Gottlieb et al. (2001)](/sources/gottlieb-2001.md) — abstract, §1, §2.1 (Eqs. (2.3)–(2.5), Fig. 2.1), §6.1 (Lemma 6.1, Fig. 6.1), §6.2–6.3 (Props. 6.2–6.3).
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §5.2 (TVD-RK3 hydrodynamics step).
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §3 (implicit and IMEX methods not unconditionally TVD beyond first order); HAL v2.
