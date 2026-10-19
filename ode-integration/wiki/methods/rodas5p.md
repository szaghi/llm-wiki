---
type: Method
title: "Rodas5P"
description: "Steinebach's 2023 coefficient set for the 8-stage stiffly accurate fifth-order Rosenbrock–Wanner structure of Rodas5: order 5(4) on index-1 DAEs, order reduction limited as in Rodas4P2, index-2 and inexact-Jacobian order 2, A-stable embedded method and an order-4 dense output."
status: established
aliases: [Rodas5P, Rodas5 P]
tags: [stiff, dae, order-reduction, implicit, software]
timestamp: 2026-10-19T00:00:00Z
---

# Rodas5P

**Rodas5P** is an 8-stage, stiffly accurate [Rosenbrock–Wanner method](/methods/rosenbrock-wanner-method.md)
of order 5 for stiff ODEs and index-1 DAEs $My'=f(t,y)$. It comes with a stiffly accurate
7-stage embedded method of order 4 and an order-4 [dense output](/methods/dense-output.md). It
keeps the structure of Di Marzo's Rodas5 (1993) but replaces its coefficients so as to avoid
the severe [order reduction](/definitions/order-reduction.md) of Rodas5
([Steinebach 2023](/sources/steinebach-2023.md), abstract, §3). The paper does not print the
coefficients; they are in OrdinaryDiffEq.jl, part of
[DifferentialEquations.jl](/software/differentialequations-jl.md) (§3, p. 12).

## Motivation: the defects of Rodas5

Steinebach (2023, §1) lists what Rodas5, widely used in DifferentialEquations.jl, gets wrong:

- **Order reduction.** Order 1 on the stiff [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md),
  2 on a semi-discretized parabolic problem, 1 on an index-2 DAE and 1 with an inexact Jacobian,
  although it has order 5(4) on index-1 DAEs (Table 1).
- **Embedded method not A-stable.** This "may cause stepsize reductions" for eigenvalues near
  the imaginary axis (Fig. 1).
- **Degenerate estimator.** For $y'=\cos t$ the main and embedded errors coincide, so
  [step-size control](/methods/step-size-control.md) fails (p. 4).
- **No dense output.** None in the original literature; Julia used Hermite interpolation,
  valid only for ODEs.

## Construction

The structural choices, in the page-local notation of the
[ROW page](/methods/rosenbrock-wanner-method.md) ($\tilde\beta_{ij}=\alpha_{ij}+\gamma_{ij}$,
$\hat b$ the embedded weights), are (Eqs. (3.1)–(3.3)):

$$b_i=\tilde\beta_{8i}\ (i\le7),\quad b_8=\gamma,\quad \alpha_8=1;\qquad
\hat b_i=\tilde\beta_{7i}\ (i\le6),\quad \hat b_7=\gamma,\quad \alpha_7=1;$$

$$\alpha_{8i}=\tilde\beta_{7i}\ (i\le7),\qquad \alpha_{7i}=\tilde\beta_{6i}\ (i\le6),\qquad \alpha_6=1.$$

So both the main and the embedded method are [stiffly accurate](/properties/stiff-accuracy.md),
and the last stage argument equals the embedded solution. Forty coefficients remain free:
$\gamma$, the $\tilde\beta_{ij}$ and the $\alpha_{ij}$ of the first stages (§3, p. 9). The
embedded method is required to satisfy ODE conditions 1–8, DAE conditions 18–22, the index-2
condition 41 and the Prothero–Robinson condition 48.

The coefficients are fixed in nine steps following the author's earlier Rodas4P and Rodas4P2
procedure (§3, steps 1–9):

1. Set $\alpha_{21}=3\gamma$, $\tilde\beta_{21}=0$. This satisfies several DAE and W conditions at
   once and makes the last coefficients of the Scholz Prothero–Robinson polynomials vanish.
2. Solve a sequence of linear (partly underdetermined) systems for the rows
   $\tilde\beta_{3\cdot},\dots,\tilde\beta_{8\cdot}$, each annihilating one more coefficient of
   Scholz's polynomials $C_2(H)$ and $C_3(H)$.
3. Determine the $\alpha_{ij}$, which enter linearly in a further group of conditions; three
   conditions are then satisfied automatically.
4. Satisfy the last 10 nonlinear conditions with 7 remaining degrees of freedom *exactly*, by
   nonlinear least squares with Nelder–Mead in Optim.jl. "Why this is possible and whether there
   are structural reasons for it could not be definitely clarified" (step 9).

The aim is to satisfy all 17 ODE conditions to order 5, all 23 index-1 DAE conditions, the
index-2 conditions 41–44, Jax's W-method conditions 45–47 and Scholz's conditions 48–49.

**Properties.** Rodas5P is A-stable and, being stiffly accurate, L-stable; its embedded method is
A-stable too. In Fig. 2 the $|R(z)|=1$ curves of both lie in the right half-plane (§3, p. 11).

**Dense output.** Degree-4 weight polynomials of order 4, obtained by solving 39 linear equations
in 24 unknowns; the same construction gives a new order-4 dense output for Rodas5 (§3, p. 12;
details on the [dense-output page](/methods/dense-output.md)).

## Observed orders (constant steps)

| Problem class | Rodas5P | Rodas5 | Source |
|---|---|---|---|
| index-1 DAE | 5.1 / 5.0 / 5.0 (embedded 4) | 5.2 / 5.1 / 5.0 | Table 5 |
| Prothero–Robinson, $\lambda=10^5$ | 3.1 / 3.0 / 3.0 | 1.3 / 1.2 / 1.1 | Table 6 |
| parabolic, $u_t=u_{xx}+u^2+$ source, $n_x=1000$ | 3.7 / 3.8 / 3.9 | 1.9 / 1.9 / 2.0 | Table 7 |
| index-2 DAE | 1.9 / 2.0 | 1 | Table 8 |
| index-1 with inexact Jacobian | 2 (like Rodas4P2) | 1 | §4 problem 5, no table |

Rodas5P thus reproduces the order-reduction behaviour of Rodas4P2 (order 3 on stiff
Prothero–Robinson, order 2 on index-2 and with an inexact Jacobian) at fifth classical order.
Its index-1 DAE errors are about 3–4 times larger than those of Rodas5 at equal step, e.g.
$8.01\times10^{-13}$ against $2.16\times10^{-13}$ at $h=0.015625$ (Table 5).

## Benchmarks

Steinebach (2023) compares Rodas4, Rodas4P, Rodas4P2, Rodas5 and Rodas5P in work–precision
diagrams (DiffEqDevTools.jl, errors over all steps and at 100 interpolated points; §4,
Figs. 4–7):

- **parabolic problem**: Rodas5P and Rodas4P2 best, with the order reduction of Rodas4 and
  Rodas5 visible;
- **hyperbolic problem**: Rodas5P best in both error measures;
- **pendulum (index 1)**: Rodas5 and Rodas5P best and similar; in the index-2 formulation Rodas4
  and Rodas5 suffer the largest order reduction;
- **transistor amplifier**: "Rodas5P cannot beat Rodas5";
- **water tube**: Rodas5P slightly ahead of Rodas5;
- **pollution**: fifth-order methods preferable;
- **photovoltaic network**: Rodas4 and Rodas5P most suitable.

**Versus boundary correction** (Fig. 3). The boundary-corrected GRK4T and Rodas4 of
Alonso-Mallo and Cano reach exactly order 4 on the parabolic problem, but Rodas5P is more
efficient "because it has a lower error constant", with constant and adaptive steps.

**Recommendation.** Steinebach proposes Rodas5P "as a standard method for stiff problems and
index-1 DAEs for medium to high accuracy requirements" in DifferentialEquations.jl. The abstract
says that "for higher accuracy requirements Rodas5P always belongs to the best methods within
the Rodas family" (§5).

## Context

[Biswas et al. (2025)](/sources/biswas-2025.md) cite Rosenbrock DAE methods of order 5 (their
ref. [37], Rodas5P) among the methods whose design conditions are weak-stage-order-type
conditions avoiding order reduction (§1.3); see [weak stage order](/definitions/weak-stage-order.md).

## Qualifications

- **The recommendation is family-level and benchmark-based.** Rodas5P has larger index-1 error
  constants than Rodas5 and does not beat it on the transistor amplifier, so "always belongs to
  the best" means "is among the best Rodas methods", not "dominates".
- **Degree-of-freedom bookkeeping.** Steps 2 and 6 of the construction appear to leave eight
  free parameters, but step 9 speaks of seven; the source does not explain the difference.
  Several conditions (ODE 14, 16, 17; DAE 31–40; index-2 43) are not shown being satisfied,
  although the stated aim is to satisfy all of them.
- **Printed slips.** The optimizer is printed "Otim.jl" (step 9), and "equation (1.3)" is cited
  where the weight formula (1.2) is meant (p. 11).

# Citations

- [Steinebach (2023)](/sources/steinebach-2023.md) — abstract; §1 (Table 1, Fig. 1); §2 (Tables 2–4); §3 (Eqs. (3.1)–(3.6), steps 1–9, Fig. 2); §4 (Tables 5–9, Figs. 3–7); §5.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1.3 (Rosenbrock DAE methods of order 5 among WSO-type constructions).
