---
type: Source
title: "Steinebach (2023) — Construction of Rosenbrock–Wanner method Rodas5P and numerical benchmarks within the Julia Differential Equations package"
description: "Constructs Rodas5P, a new coefficient set for the 8-stage stiffly accurate fifth-order Rosenbrock–Wanner structure of Rodas5, satisfying index-1 DAE, Prothero–Robinson, index-2 and W-method conditions with an A-stable embedded method and an order-4 dense output, and benchmarks it within the Rodas family in Julia's DifferentialEquations.jl."
resource: "doi:10.1007/s10543-023-00967-x"
source_kind: paper
authors: [Steinebach G.]
year: 2023
venue: "BIT Numer. Math. 63:27"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_BIT_Numerical_Mathematics_Steinebach_Construction_of_RosenbrockWanner_method_Rodas5P_and_numerica.pdf"
tags: [implicit, stiff, dae, order-reduction, order-conditions, software]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper constructs [Rodas5P](/methods/rodas5p.md), a new coefficient set
for the 8-stage, stiffly accurate, fifth-order
[Rosenbrock–Wanner](/methods/rosenbrock-wanner-method.md) structure of
Rodas5 (Di Marzo 1993). The method is meant for stiff ODEs and index-1
[DAEs](/definitions/differential-algebraic-equation.md) $My'=f(t,y)$.
Rodas5 is widely used in
[DifferentialEquations.jl](/software/differentialequations-jl.md) but has
four defects. It shows severe [order reduction](/definitions/order-reduction.md),
down to order 1, on the
[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md), on
semi-discretized parabolic problems, on index-2 DAEs and with inexact
Jacobians. Its embedded method is not
[A-stable](/properties/a-stability.md). On $y'=\cos t$ its main and
embedded errors coincide, which breaks
[step-size control](/methods/step-size-control.md). And it has no
[dense output](/methods/dense-output.md).

The construction follows the author's earlier Rodas4P/Rodas4P2 procedure.
Both the main method and the 7-stage
[embedded method](/methods/embedded-runge-kutta-pair.md) are
[stiffly accurate](/properties/stiff-accuracy.md). That structure leaves
40 free coefficients. They are fixed by satisfying, in order: Scholz's
Prothero–Robinson conditions (equivalent for parabolic problems to the
Ostermann–Roche conditions behind
[weak stage order](/definitions/weak-stage-order.md)); the 17 ODE and 23
index-1 DAE order conditions to order 5; the index-2 conditions 41–44;
and Jax's W-method conditions 45–47. Steps 1–8 are linear systems. The
last 10 nonlinear conditions are solved exactly by Nelder–Mead least
squares with 7 degrees of freedom left. The result is A- and L-stable,
with an A-stable embedded method (see the
[stability function](/definitions/stability-function.md) page). A
degree-4 dense output of order 4 is derived for Rodas5P and Rodas5.

Constant-step convergence tables and work–precision diagrams compare
Rodas5P with Rodas4, Rodas4P, Rodas4P2 and Rodas5. Rodas5P keeps order
5(4) on index-1 DAEs. On the stiff Prothero–Robinson problem it reaches
order 3, about 3.8 on the parabolic problem and 2 on index-2 and
inexact-Jacobian tests, matching Rodas4P2. "For higher accuracy
requirements Rodas5P always belongs to the best methods within the Rodas
family." Its coefficients are not printed; they are in OrdinaryDiffEq.jl.

# Version read

Version of record (Springer, open access CC BY 4.0), 26 pages, article 27
of BIT 63. Received 18 July 2022, accepted 20 March 2023, published online
17 April 2023. The DOI is printed on page 1, and title, venue and article
number match Crossref. Pages 2–12 and 14–22 were read visually because
text extraction garbled the equations, trees and rotated tables. The
paper does not print the Rodas5P coefficients or the new dense-output
coefficients. It refers to the OrdinaryDiffEq.jl repository
(github.com/SciML/OrdinaryDiffEq.jl) for them (§3, p. 12).

# Key claims

Registry notation: $h$ step, $M$ mass matrix, $J=\partial f/\partial y$
evaluated at $(t_n,y_n)$, Rosenbrock coefficients $\alpha_{ij}$,
$\gamma_{ij}$ and diagonal $\gamma$, $\hat p$ embedded order, $z=h\lambda$.
"Order $p(\hat p)$" gives main and embedded orders on a problem class.

1. Rodas5 reduces to order 1 on stiff Prothero–Robinson, order 2 on the
   parabolic problem, order 1 on index-2 DAEs and order 1 with an inexact
   Jacobian, while having order 5(4) on index-1 DAEs (Table 1,
   constant-step numerics). **Shown**
2. Table 1, stages $s$ and orders on (DAE-1, Prothero–Robinson, parabolic,
   DAE-2, inexact Jacobian): ROS3P $s=3$: 3(2), 2(2), 3(2), 2(1), 1(1);
   Ros3prl2 $s=4$: 3(2), 3(2), 3(2), 2(1), 1(1); Rodas3 $s=4$: 3(2), 1(2),
   2(2), 1(2), 2(1); Rodas4 $s=6$: 4(3), 1(1), 2(2), 1(1), 1(1); Rodas4PR2
   $s=6$: 4(3), 4(3), 4(3), 2(2), 1(1); Rodas4P2 $s=6$: 4(3), 3(3), 4(3),
   2(2), 2(1); Rodas5 $s=8$: 5(4), 1(1), 2(2), 1(1), 1(1) (§1). **Shown**
3. For $y'=\cos t$, $y(0)=0$, Rodas5 and its embedded scheme give exactly
   the same error, so step-size control fails (§1, p. 4). **Stated**
4. The embedded method of Rodas5 is not A-stable (Fig. 1), which "may cause
   stepsize reductions for problems with eigenvalues near the imaginary
   axis" (§1, p. 4). **Shown** (plot)
5. The original Rodas5 literature has no dense-output coefficients. Julia
   used Hermite interpolation, "only applicable to ODE problems" (§1, p. 4).
   **Stated**
6. Scholz's error-constant estimate for Prothero–Robinson is not sharp: for
   L-stable methods it behaves like $C_1/z$. So for fixed $h$ the results
   are asymptotically exact as $\lvert\lambda\rvert\to\infty$, but for fixed
   large $\lvert\lambda\rvert$ only order $p-1$ is observed. Hence Rodas4P
   and Rodas4P2 satisfy conditions 48–49 yet show order 3, while Rodas4PR2
   reaches full order (§2, p. 8, citing Steinebach 2020 and Rang). **Stated**
   (supported by Table 6)
7. Condition 41, $\sum b_iw_{ij}w_{jk}\alpha_k^2=2$, guarantees order 2 for
   index-2 DAEs $y'=f(y,z)$, $0=g(y)$ with $g_yf_z$ nonsingular. Conditions
   42–44 add order 3 in $y$ and 2 in $z$ (§2, Table 4, from Lubich–Roche).
   **Stated**
8. Jax's conditions 45–47 give at least order 2 for index-1 problems with
   an inexact Jacobian, provided the derivative of the algebraic equation
   with respect to the algebraic variable is exact (§2, §4 problem 5).
   **Stated**
9. Rodas5P has $s=8$ and is stiffly accurate ($b_i=\beta_{8i}$,
   $b_8=\gamma$, $\alpha_8=1$). Its stiffly accurate embedded method has
   $\hat s=7$ stages and order $\hat p=4$ and satisfies conditions 1–8,
   18–22, 41 and 48 (§3, Eqs. (3.1)–(3.2)). **Derived**
10. Exactly 40 coefficients remain after the structural choices
    (3.1)–(3.3) (§3, p. 9). **Derived**
11. The final 10 nonlinear conditions (Nos. 9, 11, 15, 24, 25, 26, 29, 44,
    45, 46), with 7 degrees of freedom, were satisfied exactly by
    nonlinear least squares (Nelder–Mead, Optim.jl). "Why this is possible
    and whether there are structural reasons for it could not be
    definitely clarified" (§3, step 9). **Shown** (computationally)
12. Rodas5P is A-stable and, being stiffly accurate, L-stable; its embedded
    method is A-stable (Fig. 2, §3, p. 11). **Shown** (plot of
    $\lvert R(z)\rvert=1$)
13. An order-4 dense output with degree-4 weight polynomials $b_i(\theta)$
    requires $3\cdot13=39$ linear equations in $3s=24$ unknowns. The system
    is nevertheless solvable for both Rodas5P and Rodas5 (§3, p. 12).
    **Shown** (computationally)
14. Index-1 DAE test: all methods reach their theoretical order. Rodas5P
    gives 5.1/5.0/5.0 (embedded 4.1/4.0/4.0) and Rodas5 5.2/5.1/5.0
    (Table 5). Rodas5P errors are about 3–4 times larger than Rodas5's
    (at $h=0.015625$: 8.01e−13 against 2.16e−13). **Shown**
15. Prothero–Robinson with stiffness $10^5$: Rodas5P 3.1/3.0/3.0 (embedded
    the same), like Rodas4P2; Rodas5 1.3/1.2/1.1; Rodas4 −3.4/0.5/0.8;
    Rodas4PR2 about 4 (Table 6). Over stiffness $10^0$–$10^5$ only Ros3prl2
    converges independently of $\lambda$, and Rodas4PR2 drops to order 3 in
    mildly stiff regimes (§4 problem 2). **Shown**
16. Parabolic problem ($n_x=1000$): no method reaches the full parabolic
    order of Table 1, because the theory assumes linear problems with
    vanishing boundary data. A linear parabolic test gave full orders (not
    shown). Rodas5P 3.7/3.8/3.9 (embedded 3.6/3.7/3.8), Rodas5 1.9/1.9/2.0
    (Table 7). **Shown** (the linear test **Stated**)
17. GRK4T and Rodas4 with boundary-corrected stages (Alonso-Mallo & Cano)
    have exactly order 4 on the parabolic problem. Rodas5P is more
    efficient "because it has a lower error constant" (Fig. 3, constant and
    adaptive steps). **Shown**
18. Index-2 DAE: Rodas3, Rodas4 and Rodas5 reduce to order 1. All other
    methods, Rodas5P included (1.9/2.0), reach order 2 (Table 8). **Shown**
19. Inexact Jacobian $\begin{pmatrix}0&0\\0&2y_2\end{pmatrix}$: Rodas5P
    behaves like Rodas4P2, order 2 (§4 problem 5, no table). **Shown**
20. Dense output: the 4th-order methods (Rodas4, Rodas4P, Rodas4P2) have
    dense output of order 3. Rodas5 and Rodas5P interpolate with order 4
    (Table 9: $t^4$ reproduced to about 5e−14). **Shown**
21. Work–precision: parabolic — Rodas5P and Rodas4P2 best; hyperbolic —
    Rodas5P best in both $l_2$ and $L_2$; pendulum index-1 — Rodas5 and
    Rodas5P best; index-2 — Rodas4 and Rodas5 reduce most; transistor
    amplifier — "Rodas5P cannot beat Rodas5"; water tube — Rodas5P slightly
    better than Rodas5; pollution — fifth-order methods preferable; PV
    network — Rodas4 and Rodas5P most suitable (§4, Figs. 4–7). **Shown**
22. "For higher accuracy requirements Rodas5P always belongs to the best
    methods within the Rodas family" (abstract). It is recommended as "a
    standard method for stiff problems and index-1 DAEs for medium to high
    accuracy requirements" in DifferentialEquations.jl (§5). **Shown**
    (benchmark-based recommendation)
23. With automatic differentiation for the Jacobian, the per-step Jacobian
    requirement of ROW methods "becomes more and more obsolete" (abstract,
    §1). **Stated**

# Printed slips

- §3, p. 11: the dense output replaces "equation (1.3)", but the update
  $y_1=y_0+\sum b_ik_i$ is in (1.2); (1.3) defines $f_y$ and $f_t$.
- §3, step 9: "optimization package Otim.jl" (Optim.jl).
- §3, step 7: stray "ss" after "by solving" (p. 10). Step 1: "Form No. 48,
  49 we obtain" ("From").
- §4 problem 3: "shown in Tabel 1".
- Typos: "fullfilled/fullfill" (passim), "satiesfied" (p. 3),
  "additonal/Additonal" (pp. 7, 15), "stabilty" (Fig. 2 caption),
  "intruduced" and "intervall" (p. 18), "form the Julia package" (p. 15),
  "eqautions" (title of ref. 22), "The author declare" (p. 24).
- Prothero–Robinson sign convention switches: Eq. (1.4) has
  $y'=\lambda(y-g)+g'$ with $\Re\lambda\ll0$; §4 problem 2 has
  $y'=-\lambda(y-g)+g'$ with $\lambda=10^5$.
- Degree-of-freedom bookkeeping is unexplained. Step 2 lists 7 free
  parameters and step 6 keeps one more, yet step 9 says "7 degrees of
  freedom are left" for the last 10 conditions. Conditions 14, 16, 17,
  31–40 and 43 are never listed as satisfied or remaining, although the aim
  is to fulfil all conditions of Tables 2–4.
- §1, p. 2: "Stiffly stable methods guarantee $R(\infty)=0$". This is not
  Gear's definition of stiff stability; $R(\infty)=0$ with A-stability is
  L-stability.

# Notation map

| Steinebach (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $My'=f(t,y)$, $M$ | $My'=f(t,y)$, $M$ | agrees; singular $M$ means a DAE, index $\le1$ assumed |
| $h$ | $h$ | agrees |
| $t_0,y_0\to y_1$ | $t_n,y_n\to y_{n+1}$ | one step |
| $f_y$ | $J$ | Jacobian at the step start |
| $f_t$ | $\partial f/\partial t$ | |
| $\alpha_{ij}$, $\gamma_{ij}$, $\gamma$ | $\alpha_{ij}$, $\gamma_{ij}$, $\gamma$ | agrees |
| $\alpha_i=\sum_{j<i}\alpha_{ij}$ | — | Rosenbrock analogue of $c_i$ |
| $\gamma_i=\gamma+\sum_{j<i}\gamma_{ij}$ | — | multiplies $h^2\partial f/\partial t$ |
| $k_i$ | — | $h$-scaled stage increments: neither $Y_i$ nor $f(t_n+c_ih,Y_i)$ |
| $b_i$, $\hat b_i$, $s$, $\hat s$, $p$, $\hat p$ | $b_i$, $\hat b_i$, $s$, $p$, $\hat p$ | agrees |
| **$\beta_{ij}=\alpha_{ij}+\gamma_{ij}$** | — | **collision with Shu–Osher $\beta_{ij}$**; Rosenbrock pages only |
| $\beta_i$, $\beta_i'$, $\beta'_{ij}$ | — | row sums with and without the diagonal; strictly lower part |
| **$B=(\beta_{ij})$**, $W=B^{-1}=(w_{ij})$ | — | **$B$ collides with $B(\xi)$** |
| $R(z)$, $z=\lambda h$ | $R(z)$, $z=h\lambda$ | agrees |
| $H=z/(1-\gamma z)$ | — | variable of Scholz's polynomials; **collides with the registry macro step $H$** (multirate pages), page-local |
| $A_i$, $B_i$, $C_2(H)$, $C_3(H)$ | — | Scholz's Prothero–Robinson coefficients; $A_i$, $B_i$ scalars, not the Butcher $A$ |
| **$M(\nu)$, $M_i(\nu)$, $N^{(\sigma)}(\nu)$** | — | **$M(\nu)$ collides with the mass matrix $M$; $\sigma$ in $N^{(\sigma)}$ collides with tree symmetry** |
| $\lambda$ (Prothero–Robinson) | $\lambda$ | **sign flips inside the source** (see Printed slips) |
| **$\lambda(t)$ (pendulum)** | — | **collision**: Lagrange multiplier |
| **$\tau\in[0,1]$**, $b_i(\tau)$ | $\theta$, $b_i(\theta)$ | **collision with tree $\tau$ and $\tau^{(k)}$**; dense-output fraction, page-local |
| **$c_i$, $d_i$, $e_i$ (dense output)** | — | **$c_i$ collides with abscissae**; dense-output coefficients |
| "stiffly stable" | L-stable ($R(\infty)=0$) | non-standard usage in the source |

# Reference list

The paper prints 27 references in numbered style, alphabetical by first
author. All are merged complete into the [bibliography](/bibliography.md)
with `citedby` steinebach-2023. Printed DOIs are on refs. 2, 8, 10, 11, 21
and 25; ref. 13 has a URL and ref. 2 an article number (Mathematics 9(16),
1970). Ref. 3 is an MSc thesis (Geneva 1993), ref. 5 a dissertation
(Wuppertal 2019), ref. 24 a preprint (TH Darmstadt 1995), the last kept as
its own entry. No printed duplicates, and no same-key suffixes needed.

# Pages created or updated

Chunk 1 (2026-10-19); updated in chunk 2 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [B-convergence](/definitions/b-convergence.md)
* [Dense output](/methods/dense-output.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Order reduction](/definitions/order-reduction.md)
* [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)
* [Rodas5P](/methods/rodas5p.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Weak stage order](/definitions/weak-stage-order.md)
