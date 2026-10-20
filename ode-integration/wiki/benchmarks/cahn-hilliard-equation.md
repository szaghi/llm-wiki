---
type: Benchmark
title: "Cahn–Hilliard equation"
description: "The fourth-order Cahn–Hilliard phase-field equation, whose free energy decays and whose biharmonic term limits explicit steps to O(Δx^4); the sources use a 2D finite-element problem to compare Radau IIA and DIRK methods in Irksome and a 1D convective variant to measure ETD speed-ups over explicit schemes."
status: established
aliases: [Cahn-Hilliard equation, convective Cahn–Hilliard equation, CHE]
tags: [stiff, verification, implicit, exponential, structure-preserving]
timestamp: 2026-10-20T14:00:00Z
---

# Cahn–Hilliard equation

The **Cahn–Hilliard equation** is the conservative fourth-order phase-field model of phase
separation. With unit mobility (page-local symbols on this page: phase field $u$, double-well
potential $\Psi$, gradient-energy coefficient $\kappa$, chemical potential $w$, free energy
$\mathcal E$),

$$\partial_tu=\Delta w,\qquad w=\Psi'(u)-\kappa\,\Delta u,\qquad
\mathcal E(u)=\int_\Omega\Bigl(\Psi(u)+\frac\kappa2\lvert\nabla u\rvert^2\Bigr)\,dx .$$

With no-flux boundary data the free energy does not increase in time, and the integral of $u$
is conserved, since the right-hand side is a divergence *(compiler remark, not in the
sources)*. For time integration the point is the term $-\kappa\Delta^2u$: its spectrum grows like
$\Delta x^{-4}$, so explicit methods need steps of order $\Delta x^4$. Permyakova & Goldobin
state that explicit Euler and Heun's predictor–corrector are unstable unless
$h<\Delta x^4/8$ for their second-order finite differences
([Permyakova & Goldobin 2025](/sources/permyakova-2025.md), §3.1.1), which matches the largest
eigenvalue $16/\Delta x^4$ of the discrete fourth derivative and the real stability interval
$[-2,0]$ of both methods *(compiler check, not in the source)*. The nonlinear potential makes
the implicit stages nonlinear. Compare the second-order
[Allen–Cahn equation](/benchmarks/allen-cahn-equation.md), which is not conservative and has a
$\Delta x^{-2}$ spectrum.

## Set-ups

| source | equation | data and parameters | discretization | use |
|---|---|---|---|---|
| [Kirby & MacLachlan (2025)](/sources/kirby-2025.md), §4.3, Eqs. (4.3)–(4.5) | 2D, $\Psi(u)=50(u^2-1)^2$, $\kappa=10^{-2}$, unit mobility, no-flux | $u_0=0.42$ on $[0.3,0.7]^2$ and $0.38$ elsewhere; steps $5\times10^{-6}$ down to $3.125\times10^{-7}$; Fig. 13 ends at $t=2.5\times10^{-4}$ | $C^1$ quintic Bell elements on $32\times32$ squares cut into right triangles, boundary terms by Nitsche's method (penalty 250); Newton to $10^{-10}$, FGMRES with stage-coupled monolithic geometric multigrid | Radau IIA with 1–5 stages, Alexander's DIRK, WSODIRK433 and WSODIRK744 in [Irksome](/software/irksome.md) |
| [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md), §3.1, Eqs. (13)–(15) | 1D convective form $\partial_tu=-v\,\partial_xu-\partial_x^2\bigl[\chi(x)u+\partial_x^2u-u^3\bigr]$ (page-local advection speed $v$, "excitability" $\chi$) | $x\in(0,10)$, $u=\partial_xu=0$ at both ends, $\chi=2.5$ on $(3,7)$ and $-3$ elsewhere, $v=1$ (an oscillatory solution), $t\in(0,50)$ | second-order central differences, 200 points ($\Delta x=0.05$) or 400 ($\Delta x=0.025$) | [exponential time differencing](/methods/exponential-integrators.md) with precomputed matrix functions against explicit schemes |

The convective form is the equation above with $\kappa=1$,
$\Psi(u)=\tfrac14u^4-\tfrac12\chi(x)u^2$ and an added advection term
($-\partial_x^2[\chi u+\partial_x^2u-u^3]=\partial_x^2[u^3-\chi u-\partial_x^2u]$): a double well where
$\chi>0$ and a single well where $\chi<0$ *(compiler check, not in the source)*. The
two set-ups share the fourth-order structure, not the parameters: they differ in dimension,
potential, boundary conditions and advection.

## What it tests and results

**Energy decay and accuracy of fully implicit against diagonally implicit methods.** All
methods of Kirby & MacLachlan (2025) produce a monotonically decreasing free energy; backward
Euler is qualitatively different from the others even at $h=6.25\times10^{-7}$ (§4.3,
Fig. 13). Some methods' Newton iterations failed at the larger steps. Run time depends mainly on
the number of stages, and here a Radau IIA method costs slightly more than a DIRK with the same
number of stages; Newton needs about 4 iterations per step as $h$ decreases (Fig. 14). In the
error of the final energy against a Radau IIA(5) reference at $h=3.125\times10^{-7}$, Radau
IIA(3) and (4) are the most accurate, then WSODIRK744; Radau IIA(2) beats Alexander's DIRK and
WSODIRK433 at much lower cost. Few schemes attain their formal order, which the authors
attribute to stiffness and stage order (Fig. 15). Monolithic multigrid is faster at small steps
and the Rana-type $LD$ stage preconditioner at large ones (no data shown). See
[fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md),
[diagonally implicit Runge–Kutta](/methods/diagonally-implicit-runge-kutta.md),
[DIRK methods with high weak stage order](/methods/dirk-high-weak-stage-order.md),
[order reduction](/definitions/order-reduction.md) and
[implicit stage solvers](/methods/implicit-stage-solvers.md).

**Exponential time differencing against explicit stepping.** Permyakova & Goldobin (2025,
§3.1.2, Figs. 3–4) advance the semi-discrete system $y'=Ly+N(y)$, with $L$ the nondiagonal
finite-difference matrix of the linear terms, by the Cox–Matthews schemes ETD2RK, ETD3RK and
ETD4RK. The matrices $e^{hL}$ and $(k-1)!\,h^k\phi_k(hL)$ are computed once, before the run, by
integrating auxiliary linear problems with Heun's method at step $0.1\Delta x^4$ (see
[evaluating φ-functions](/methods/phi-function-evaluation.md)). For an error rate of $10^{-6}$
per unit time the steps can be $h\approx0.005$ (ETD2RK), $0.02$ (ETD3RK) and $0.04$ (ETD4RK);
the gain in CPU time over the predictor–corrector at its stability limit exceeds a factor 100
for all three, largest for ETD4RK, and grows when the grid is refined to 400 points. The
preparation cost grows linearly with $h$, so for short runs the best $h$ balances preparation
and integration. The authors argue from a scaling argument that the gain over explicit schemes
grows like $\Delta x^{m-2}$ for a highest spatial derivative of order $m$, here $\Delta x^2$
(§3.2.2, §4).

## Other mentions in the bundle

The equation also appears without a run: [Tan et al. (2022)](/sources/tan-2022.md) (§1) recall
that the [explicit–implicit–null method](/methods/explicit-implicit-null-method.md) had been
applied to Cahn–Hilliard problems at low order, and
[García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) (§1) cite a variable-step BDF2
analysis for it.

## Qualifications

- **Energy as printed by Kirby & MacLachlan (2025).** Their energy carries the mobility inside
  the integral, $\int_\Omega Mf(c)+\frac{M\lambda}2\lvert\nabla c\rvert^2$ in their symbols; with
  unit mobility it is the free energy above. They state the final time only through the axis of
  Fig. 13, and the mobility symbol $M$ also denotes their mass matrix and a step ratio elsewhere
  in the paper.
- **Order of the exponential schemes.** Permyakova & Goldobin state classical error terms
  ($\propto h^{p+1}$ times a derivative of the nonlinear term) for ETD3RK and ETD4RK, without a
  stiff-order analysis, and their error curves are not slope-annotated, so they neither confirm
  nor refute order 4 for ETD4RK (see
  [stiff order conditions of exponential Runge–Kutta methods](/results/exponential-runge-kutta-stiff-order-conditions.md)).
  Their gains are measured against explicit schemes at their stability limit, not against
  implicit, IMEX or Krylov-based exponential methods. They were read as arXiv v2.
- **Dense matrices.** The precomputed matrices of Permyakova & Goldobin are $N\times N$ with
  rapidly decaying off-diagonal entries; memory grows with the square of the number of unknowns,
  which the authors call the obstacle in several dimensions (§4).

# Citations

- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §4.3 (Eqs. (4.3)–(4.5), Figs. 12–15).
- [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md) — §2 (Eqs. (10)–(12)), §3.1 (Eqs. (13)–(16), Figs. 1–4), §3.2.2, §4; arXiv v2.
- [Tan et al. (2022)](/sources/tan-2022.md) — §1 (mention only).
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §1 (mention only).
