---
type: Method
title: "Dense output"
description: "Continuous extensions of a one-step method that give the solution between grid points: Hermite interpolants for nonstiff problems, Lagrange interpolation of stored steps for stiff ones, Rosenbrock weight polynomials (Rodas5, Rodas5P), full-order φ-method dense output, collocation and DG-in-time polynomials, and the time-continuous cell states of asynchronous time stepping."
status: established
aliases: [continuous extension, interpolant, continuous Runge–Kutta, dense-output formula, collocation polynomial, local DG solution, subgrid resolution]
tags: [runge-kutta, stiff, software, step-size-control, exponential]
timestamp: 2026-10-20T16:00:00Z
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

## Dense output of exponential integrators

The φ-series of [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) (Thm. 10, Eq. 38)
extends to any point of the step. With $J_n=f'(y_n)$, the exact solution satisfies
$y(t_n+\vartheta h)=y_n+\sum_{k\ge1}\vartheta^k\phi_k(\vartheta hJ_n)G_k$, where
$G_1=hf(y_n)$, $G_2=0$ and $G_k$, $k\ge3$, are the φ-series vectors of
[stiff order conditions of exponential Runge–Kutta methods](/results/exponential-runge-kutta-stiff-order-conditions.md)
(page-local $G_k$). A method of φ-order $p$ with update vectors $v_k$ therefore has the dense output

$$y_n+\vartheta h\,\phi_1(\vartheta hJ_n)f(y_n)+\sum_{k=3}^p\vartheta^k\phi_k(\vartheta hJ_n)\,v_k,$$

which keeps the full φ-order $p$ at every $\vartheta\in[0,1]$ (§5.5). The interpolant uses no
extra right-hand-side evaluations. Adaptive Krylov codes return several values of
$\vartheta$ from one projection at little extra cost (§5.5; see
[evaluating φ-functions](/methods/phi-function-evaluation.md)). The authors use this dense
output inside their methods in two ways:

- **as stages of higher-order methods.** For $p>4$ the stages are computed by the dense
  output of a φ-order-$(p-2)$ method. Their order-6 method takes four stages at
  $\vartheta=\tfrac14,\tfrac12,\tfrac34,1$ from the dense output of the φ-order-4 method
  (§6.1, Eq. 41);
- **as past values of multivalue methods,** taken from the previous step's dense output at
  nodes inside that step (§6.3).

See [exponential integrators](/methods/exponential-integrators.md).

## Collocation and DG-in-time polynomials

Methods that compute a polynomial in time on each step carry their dense output with them.

- **Collocation and SDC.** The collocation solution of a
  [fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md) or spectral deferred
  correction step on $\mathsf M$ nodes is the polynomial of degree $\mathsf M$ through $y_n$ and the
  node values. Evaluated inside the step it is accurate to order $\mathsf M$, against a higher
  order at the step end ([Saupe et al. (2025)](/sources/saupe-2025.md), §2.1, after
  Hairer–Nørsett–Wanner). Saupe et al. use it twice in their adaptive SDC: the error estimate
  of their $\Delta t$-$k$-adaptivity compares the value at node $\mathsf M-1$ with the
  degree-$(\mathsf M-1)$ interpolant through the other nodes, an order-$(\mathsf M-1)$ value
  (Eqs. (16)–(18)), and a rejected step's polynomial, evaluated at the nodes of the shorter
  retry, gives its initial guess (§2.2, §4.1). See
  [step-size control](/methods/step-size-control.md).
- **Local DG solution.** The ADER solver with a local discontinuous Galerkin predictor of
  [Popov (2024)](/sources/popov-2024.md) stores on each step a polynomial of degree $\mathsf M$
  (the source's $N$) on the $\mathsf M+1$ Gauss–Legendre nodes, which he presents as "precisely
  the representation of the solution in the form of a finite element", not a reconstruction
  (§1.3, Eq. (16)). It is discontinuous at the grid points and observed to have order
  $\mathsf M+1$ inside the step against $2\mathsf M+1$ at the grid points, up to $\mathsf M=60$
  in 500-digit arithmetic (§2.1, Tables 1–6). Evaluating it at many sub-points is one matrix
  product of precomputed basis values with the coefficients (§1.3). On a harmonic oscillator
  with $h=100\pi/96$, more than half a period, in double precision, $\mathsf M=8$ brings the
  grid values to round-off with a very accurate in-step polynomial, and $\mathsf M=16$ brings
  both to round-off; Popov calls this "subgrid resolution" (§1.3, Fig. 3). See
  [ADER time integration](/methods/ader-time-integration.md).

## Time-continuous states in asynchronous time stepping

In the asynchronous (cell-wise [local time stepping](/methods/local-time-stepping.md))
finite-volume scheme of [Unfer (2021)](/sources/unfer-2021.md) (§3.2, §3.5), each cell keeps
a polynomial in time rather than a value. A neighbour can then evaluate it at any face
refresh time between the cell's own steps. Each cell $i$ carries two time-continuous
representations, with $u_i$ page-local:

- an *extrapolated* state, updated only at the cell's own refresh and used to compute fluxes
  and sources. It is linear in time in the first-order scheme and parabolic in the
  third-order "ARK3";
- a *conservative* state, integrated whenever the cell or a neighbour is refreshed. In ARK3
  it is the cubic Taylor polynomial
  $u_i(t)=u_i(t_q)+\partial_tu_i\,(t-t_q)+\tfrac12\partial_t^2u_i\,(t-t_q)^2+\tfrac16\partial_t^3u_i\,(t-t_q)^3$
  between its integration times $t_q$ (Eq. 111).

The ARK3 derivatives are assembled from fluxes evaluated at three face times (start, end and
midpoint of a face's refresh interval), following the SSPRK(3,3) tableau with abscissae
$(0,1,\tfrac12)$ (Eqs. 103–110). Under a global step the scheme reverts to that
[SSP Runge–Kutta method](/methods/strong-stability-preserving-runge-kutta.md) (§3.5). The
quadratic flux polynomial implied by Eqs. 108–110 integrates over a step to the SSPRK3
weights $(\tfrac16,\tfrac16,\tfrac23)$ *(compiler check, not in the source)*. These
polynomials are a dense-output device in the sense of this page. They are not an
interpolant of computed values: they are Taylor extrapolations whose coefficients come from
the stage fluxes.

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
- Saupe et al. (2025, §2.1) give the step-end order of the collocation solution as "up to
  $2\mathsf M$" for Gauss–Legendre, Lobatto and Radau nodes alike; only Gauss nodes reach $2\mathsf M$,
  Radau IIA $2\mathsf M-1$ and Lobatto $2\mathsf M-2$ (see
  [fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)). The in-step
  order $\mathsf M$ is not affected.
- Popov's (2024) in-step and grid-point orders are observed, not proved for his nodal variant;
  he expects them from Baccouch's proofs for modal DG (Introduction).

- In Unfer (2021, §3.5) the text says that the third extrapolated stage evolves linearly
  from the first with slope $\partial_tu_i+\partial_t^2u_i(\Delta_3-\Delta_1)$. His Eq. (105)
  corresponds to the slope $\partial_tu_i+\partial_t^2u_i\Delta_3$, the true slope at the
  midpoint ($\Delta_1$, $\Delta_3$ page-local: the offsets of the first and third stage times
  from the cell's last refresh). The two agree under a global step, where $\Delta_1=0$
  *(compiler check, not in the source)*.

# Citations

- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §3.3.1 (Hermite), §3.3.2 (Lagrange), §3.4.2 (predictors), §4 (usage modes).
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Hermite interpolation for Rodas5 in Julia), §3 (Eqs. (3.4)–(3.6)), §4 problem 6 (Table 9), Fig. 4.
- [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) — Thm. 10, Eq. 38, §5.5 (φ-order dense output), §6.1 Eq. 41, §6.3 (use for stages and multivalue nodes).
- [Unfer (2021)](/sources/unfer-2021.md) — §3.2 Eqs. 54–56, §3.5 Eqs. 103–111 (time-continuous extrapolated and conservative states, reduction to SSPRK3).
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §2.1 (dense output of the collocation solution), §2.2 (Eqs. (16)–(18), restarts), §4.1.
- [Popov (2024)](/sources/popov-2024.md) — arXiv v1: Introduction, §1.3 (Eq. (16), Fig. 3), §2.1 (Tables 1–6).
