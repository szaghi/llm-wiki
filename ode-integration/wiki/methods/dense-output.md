---
type: Method
title: "Dense output"
description: "Continuous extensions of a one-step method that give the solution between grid points: Hermite interpolants for nonstiff problems, Lagrange interpolation of stored steps for stiff ones, and weight polynomials of Rosenbrock methods, with the order-4 dense output of Rodas5 and Rodas5P."
status: established
aliases: [continuous extension, interpolant, continuous Runge–Kutta, dense-output formula]
tags: [runge-kutta, stiff, software, step-size-control]
timestamp: 2026-10-19T12:00:00Z
---

# Dense output

**Dense output** is an approximation $y(t_n+\vartheta h_n)$, $\vartheta\in[0,1]$, of the
solution inside a step, produced without stopping the integrator at every requested time
($\vartheta$ is the page-local dense-output fraction). Integrators need it for output at user
times past which they have stepped, event location, predictors for implicit stages and
error measurement between steps. The sources describe two constructions: **interpolation** of
values (and derivatives) at grid points, and **weight polynomials** that replace the constant
weights $b_i$ of the step by polynomials in $\vartheta$
([Reynolds et al. 2023](/sources/reynolds-2023.md), §3.3;
[Steinebach 2023](/sources/steinebach-2023.md), §3).

## Hermite interpolation (nonstiff problems)

[ARKODE](/software/arkode.md) builds, for nonstiff problems, Hermite interpolants
$\mathcal I_k$ of degree $k\le5$ on $[t_n,t_{n+1}]$ from $y_n$, $y_{n+1}$ and $f_n=f(t_n,y_n)$,
$f_{n+1}$ ($\mathcal I_k$ page-local). The recipe follows Hairer–Nørsett–Wanner, as recalled by
Reynolds et al. (2023), §3.3.1:

| Degree | Conditions | Extra $f$ evaluations |
|---|---|---|
| 0 | $\mathcal I_0=\tfrac12(y_n+y_{n+1})$ | 0 |
| 1 | values at both ends | 0 |
| 2 | values at both ends, derivative $f_{n+1}$ at the right end | 0 |
| 3 | values and derivatives at both ends | 0 |
| 4 | degree-3 conditions plus $\mathcal I_4'=f(\cdot,\mathcal I_3(\cdot))$ at $t_{n+1}-h_n/3$ | 1 |
| 5 | degree-3 conditions plus $\mathcal I_5'=f(\cdot,\mathcal I_4(\cdot))$ at $t_{n+1}-h_n/3$ and $t_{n+1}-2h_n/3$ | 4 (as printed) |

## Lagrange interpolation (stiff problems)

For stiff problems ARKODE instead interpolates stored solution values,

$$\mathcal I_\xi(t)=\sum_{j=0}^{\xi}y_{n+1-j}\,\ell_j(t),\qquad
\ell_j(t)=\prod_{i=0,\,i\ne j}^{\xi}\frac{t-t_{n+1-i}}{t_{n+1-j}-t_{n+1-i}},$$

with derivatives up to third order available, and uses the highest degree the history allows
during the first steps (§3.3.2; $\xi$ and the Lagrange basis $\ell_j$ page-local, the latter
unrelated to the registry's multirate micro-step index $\ell$). The stated reason is that
"interpolants that use derivative values $f=y'$ can result in order reduction" on stiff
problems (§3.3.2); see [order reduction](/definitions/order-reduction.md). Steinebach (2023)
makes the parallel point for DAEs: before Rodas5P, Julia's
[DifferentialEquations.jl](/software/differentialequations-jl.md) used Hermite interpolation for
Rodas5, which is "only applicable to ODE problems" (§1, p. 4).

## Weight polynomials for Rosenbrock methods

For a [Rosenbrock–Wanner method](/methods/rosenbrock-wanner-method.md) with $h$-scaled stage
increments $U_i$ (page-local) and update $y_{n+1}=y_n+\sum_ib_iU_i$, the dense output is
$y_n(\vartheta)=y_n+\sum_ib_i(\vartheta)U_i$ with polynomials $b_i(0)=0$, $b_i(1)=b_i$
(Steinebach 2023, §3, Eqs. (3.4)–(3.6), following Hairer–Wanner). For Rodas5 and
[Rodas5P](/methods/rodas5p.md) Steinebach takes degree-4 polynomials

$$b_i(\vartheta)=\vartheta b_i+\vartheta(\vartheta-1)\bigl(d^{(1)}_i+\vartheta d^{(2)}_i+\vartheta^2d^{(3)}_i\bigr)$$

($d^{(1)}_i,d^{(2)}_i,d^{(3)}_i$ page-local; the source writes $c_i,d_i,e_i$). Order 4 of the
interpolant requires the order conditions 1–8 (ODE) and 18–22 (index-1 DAE) of the Rosenbrock
theory with each right-hand side multiplied by $\vartheta^m$, $m$ the number of solid nodes of
the corresponding tree. That gives $3\cdot13=39$ linear equations in the $3s=24$ unknowns; the
system is overdetermined but solvable for both Rodas5 and Rodas5P (§3, p. 12).

**Verification.** On $y_1'=kt^{k-1}$, $0=y_1-y_2$ (exact solution $t^k$, page-local integer $k$), one step of size 2
followed by interpolation (Steinebach 2023, §4 problem 6, Table 9):

- Rodas5 and Rodas5P reproduce $t^4$ to about $5\times10^{-14}$ at every interpolation point,
  i.e. their dense output has order 4;
- the dense outputs of the fourth-order Rodas4, Rodas4P and Rodas4P2 have order 3.

In work–precision diagrams with errors measured at 100 interpolated points, the new Rodas5 dense
output is visibly better than Rodas4's on a hyperbolic problem (§4, Fig. 4).

## Dense output inside an integrator

- **Output modes.** ARKODE's NORMAL mode steps past the output time and interpolates; the
  TSTOP modes shorten the last step so that $t_n$ hits the output time and no interpolation
  error enters (Reynolds et al. 2023, §4).
- **Implicit-stage predictors.** ARKODE's predictors for implicit stages are dense-output
  extrapolants from the previous step; the "maximum order" predictor uses degree
  $\le\min\{p-1,\ \text{user cap},\ 5\}$ (§3.4.2; see
  [implicit stage solvers](/methods/implicit-stage-solvers.md)).

## Qualifications

- Reynolds et al. state that $\mathcal I_5$ costs four extra evaluations in total, although its
  construction needs $\mathcal I_4$, which costs one; the count is as printed (§3.3.1). They use
  the symbol of the degree-0 Hermite interpolant also for the trivial predictor $y_n$, a
  different object (§3.3.1 versus §3.4.2).
- Reynolds et al. print the Lagrange nodes as $t_i$, $t_j$ while the data are the stored values
  $y_{n-j}$; the formula above uses the stored times (index-convention slip in the source).
- The claim that derivative-based interpolants cause order reduction on stiff problems is stated,
  not demonstrated, in Reynolds et al. (2023).
- Steinebach (2023) refers to replacing "equation (1.3)" by the dense formula; the weight
  formula is his Eq. (1.2) (printed slip).

# Citations

- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §3.3.1 (Hermite), §3.3.2 (Lagrange), §3.4.2 (predictors), §4 (usage modes).
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Hermite interpolation for Rodas5 in Julia), §3 (Eqs. (3.4)–(3.6)), §4 problem 6 (Table 9), Fig. 4.
