---
type: Method
title: "Rosenbrock–Wanner (ROW) and W-methods"
description: "Linearly implicit one-step methods that replace the nonlinear stage solves of implicit Runge–Kutta methods by s linear solves with the single matrix M - h gamma J: the scheme, its ODE, index-1 and index-2 DAE, W-method and Prothero–Robinson order conditions, stiff accuracy, order reduction, and the Rodas family."
status: established
aliases: [ROW method, Rosenbrock method, linearly implicit Runge–Kutta, W-method, Rodas, ROS3P]
tags: [stiff, implicit, dae, order-reduction, order-conditions]
timestamp: 2026-10-20T16:00:00Z
---

# Rosenbrock–Wanner (ROW) and W-methods

A **Rosenbrock–Wanner (ROW) method** is a linearly implicit one-step method for stiff ODEs and
index-1 DAEs $My'=f(t,y)$. Each step solves $s$ *linear* systems, all with the same matrix
$M-h\gamma J_n$, instead of the nonlinear stage equations of an implicit
[Runge–Kutta method](/definitions/runge-kutta-method.md). A **W-method** is a ROW method whose
order does not depend on $J_n$ being the exact Jacobian. The description follows
[Steinebach (2023)](/sources/steinebach-2023.md), §1–2, who recalls the scheme from
Hairer–Wanner and Lang.

## The scheme

With $J_n=\partial f/\partial y(t_n,y_n)$, $f_t=\partial f/\partial t(t_n,y_n)$ and
$h$-scaled stage increments $U_i$ (page-local; the source's $k_i$), an $s$-stage ROW step is

$$\begin{aligned}
(M-h\gamma J_n)\,U_i&=hf\Bigl(t_n+\alpha_ih,\;y_n+\sum_{j=1}^{i-1}\alpha_{ij}U_j\Bigr)+hJ_n\sum_{j=1}^{i-1}\gamma_{ij}U_j+h^2\gamma_i f_t,\quad i=1,\dots,s,\\
y_{n+1}&=y_n+\sum_{i=1}^s b_iU_i,
\end{aligned}$$

with $\alpha_i=\sum_{j<i}\alpha_{ij}$ and $\gamma_i=\gamma+\sum_{j<i}\gamma_{ij}$ (Eqs. (1.1)–(1.3)).
All stages share one matrix, so one LU factorization per step suffices; index 1 guarantees that
$M-h\gamma J_n$ is regular for small $h>0$. The price, compared with implicit Runge–Kutta
methods, is an exact Jacobian at every step. Steinebach argues that automatic differentiation in
[DifferentialEquations.jl](/software/differentialequations-jl.md) makes this requirement
"more and more obsolete" (abstract, §1); for the Newton-based alternative see
[implicit stage solvers](/methods/implicit-stage-solvers.md).

## Order conditions

Steinebach (2023) writes the conditions with $\tilde\beta_{ij}=\alpha_{ij}+\gamma_{ij}$,
$\tilde\beta_{ii}=\gamma$, $\tilde\beta_i=\sum_{j\le i}\tilde\beta_{ij}$, the lower-triangular
matrix $\tilde B=(\tilde\beta_{ij})$ and $W=\tilde B^{-1}=(w_{ij})$ (page-local symbols,
distinct from the Shu–Osher $\beta_{ij}$; Eqs. (2.1)–(2.2)). They follow Roche and Hairer–Wanner
and are indexed by rooted trees (black nodes for differential, white for algebraic components).

**ODE conditions** (Table 2): 17 conditions up to order 5. The first four:

$$\sum_ib_i=1,\qquad \sum_ib_i\tilde\beta_i=\tfrac12,\qquad \sum_ib_i\alpha_i^2=\tfrac13,\qquad \sum_{i,j}b_i\tilde\beta_{ij}\tilde\beta_j=\tfrac16.$$

**Index-1 DAE conditions** (Table 3): 23 further conditions up to order 5, for 40 in total. The
first is $\sum_{i,j}b_iw_{ij}\alpha_j^2=1$ (order 3).

**Index-2 conditions** (Table 4, from Lubich–Roche), for $y'=f(y,w)$, $0=g(y)$ with $g_yf_w$
nonsingular ($w$ the algebraic variable, page-local):

- $\sum b_iw_{ij}w_{jk}\alpha_k^2=2$ gives order 2;
- three more conditions give order 3 in $y$ and 2 in $w$.

**W-method conditions** (Table 4, from Jax): with an inexact Jacobian, provided the derivative of
the algebraic equation with respect to the algebraic variable is exact,

$$\sum_{i,j}b_i\gamma_{ij}=0,\qquad\sum b_i\alpha_{ij}w_{jk}\alpha_k=\tfrac12,\qquad\sum b_iw_{ij}\alpha_j=1$$

give at least order 2 for index-1 problems.

**Prothero–Robinson conditions** (Scholz): two polynomial conditions $C_2(H)=C_3(H)=0$ in
$H=z/(1-\gamma z)$, for orders 3 and 4 on the
[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md) (Table 4, Eqs. (2.5)–(2.13);
$C_2,C_3,H$ page-local). Ostermann and Roche showed that the same conditions govern
semi-discretized parabolic problems (§2). The letter "P" in Rodas4P, Rodas4P2 and Rodas5P stands
for both "Prothero–Robinson" and "parabolic".

**Stability function.** It is rational in $H$, with all poles at $z=1/\gamma$ (Eq. (2.14)).

**B-series.** [BSeries.jl](/software/bseries-jl.md) lists B-series of ROW methods among its
features ([Ketcheson & Ranocha 2023](/sources/ketcheson-2023.md), §1), although the paper gives
no ROW example and its conclusion lists Rosenbrock methods as a future extension (§5).

## Stiff accuracy and L-stability

A ROW method is [stiffly accurate](/properties/stiff-accuracy.md) when $b_i=\tilde\beta_{si}$
($i<s$), $b_s=\gamma$ and $\alpha_s=1$, so that $y_{n+1}$ equals the argument of the last
stage. With A-stability this gives $R(\infty)=0$, i.e. L-stability (Steinebach 2023, §1, §3,
Eqs. (3.1)–(3.3)). Rodas5P also makes its embedded solution stiffly accurate by the same device
one stage earlier (§3).

## Order reduction and the WSO connection

A ROW method's classical order is reached on nonstiff ODEs, and the index-1 DAE conditions secure
it on index-1 DAEs. On stiff and PDE problems the order can collapse, which is
[order reduction](/definitions/order-reduction.md). Steinebach (2023, Table 1) measures the
observed constant-step orders of the Rodas family (embedded order in brackets):

| Method | $s$ | index-1 DAE | Prothero–Robinson | parabolic | index-2 DAE | inexact $J$ |
|---|---|---|---|---|---|---|
| ROS3P | 3 | 3(2) | 2(2) | 3(2) | 2(1) | 1(1) |
| Ros3prl2 | 4 | 3(2) | 3(2) | 3(2) | 2(1) | 1(1) |
| Rodas3 | 4 | 3(2) | 1(2) | 2(2) | 1(2) | 2(1) |
| Rodas4 | 6 | 4(3) | 1(1) | 2(2) | 1(1) | 1(1) |
| Rodas4PR2 | 6 | 4(3) | 4(3) | 4(3) | 2(2) | 1(1) |
| Rodas4P2 | 6 | 4(3) | 3(3) | 4(3) | 2(2) | 2(1) |
| Rodas5 | 8 | 5(4) | 1(1) | 2(2) | 1(1) | 1(1) |

[Rodas5P](/methods/rodas5p.md) was built to remove the Rodas5 failures in this table.

**Remedies.** Two routes appear in the sources:

- **More order conditions.** Impose the Prothero–Robinson/parabolic, index-2 and W conditions,
  as in Rodas4P, Rodas4P2 and Rodas5P (Steinebach 2023, §2–3).
- **Modified boundary data.** Use adapted boundary conditions in each stage (Alonso-Mallo and
  Cano). This works for any ROW method but needs problem information inside the stage
  evaluation; Steinebach compares it numerically in Fig. 3 (see [Rodas5P](/methods/rodas5p.md)).

**WSO lineage.** The Scholz and Ostermann–Roche conditions are the ROW origin of
[weak stage order](/definitions/weak-stage-order.md):

- [Biswas et al. (2024)](/sources/biswas-2024.md) trace the WSO conditions to the "parabolic
  order conditions" that Ostermann and Roche derived for ROW methods, and to Scholz's conditions
  for SDIRK and ROW methods (§1, Def. 1.1, §2.3);
- [Biswas et al. (2025)](/sources/biswas-2025.md) list the same works, Rang's
  "BPR-consistency" and Rosenbrock DAE methods of order 5 (their ref. [37]) among earlier
  appearances of WSO-type conditions (§1.3).

**Limits of the theory.** Scholz's error-constant estimate is not sharp: for L-stable methods
the error constant behaves like $C_1/z$. At fixed large $|\lambda|$, methods satisfying both
Scholz conditions (Rodas4P, Rodas4P2) therefore show only order $p-1=3$, while Rodas4PR2 reaches
full order (Steinebach 2023, §2, p. 8, citing Steinebach and Rang). The parabolic orders of
Ostermann–Roche assume linear problems with vanishing boundary data. They are not reached on
Steinebach's nonlinear test with non-vanishing Dirichlet data, while a linear problem gives the
full orders (§4 problem 3; the linear test is not shown).

## W-methods

W-methods are ROW methods that do not require the exact Jacobian (Steinebach 2023, citing
Rang). Jax extended them to DAEs with "a huge amount of additional order conditions". Rodas4P2 and Rodas5P satisfy Jax's three conditions, so they keep order 2 for index-1
problems with an inexact Jacobian. Rodas4 and Rodas5 drop to order 1 (Table 1; §4 problem 5).

[Conte et al. (2024)](/sources/conte-2024.md) (§7) state that Rosenbrock methods used with an
inexact Jacobian become W-methods, "for which the order of convergence is generally lower, and
furthermore there is no study on the related stability properties". They present their analysis
of TASE–Runge–Kutta methods with an arbitrary matrix in place of $J$ as the first in-depth
stability study of a subclass of W-methods with an inexact Jacobian "using the techniques that we
employ" (§1.1). The technique splits $J=W+(J-W)$, with $W$ the matrix used in the linear solves
(page-local), and works with the generalized eigenvalues and weighted fields of values of the
pair. It is borrowed from unconditional-stability analyses of IMEX multistep methods; see
[TASE operators](/methods/tase-operators.md).

## Multistep analogue: Limm and Limm-W

[Glandon et al. (2022)](/sources/glandon-2022.md) build
[linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md) from linear
multistep methods in the way Rosenbrock methods are built from implicit Runge–Kutta methods
(§1–2). The correspondence is close:

- **One linear solve per step.** Each step solves one linear system with $I-h\kappa J$, and the
  diagonal coefficient $\kappa$ (page-local there) plays the role of $\gamma$ (§2).
- **Limm-W mirrors W-methods.** It allows an arbitrary matrix in place of $J$, with order
  conditions independent of it.
- **The exact Jacobian saves conditions.** The exact-Jacobian Limm has one order condition
  fewer than Limm-W, exactly as Rosenbrock methods need fewer conditions than W-methods (Thms.
  3.3, 3.7, Remark 3.8).
- **Stiff order loss.** With a generic matrix and $hJ$ not small, the local error of Limm-W
  drops one order unless the Jacobian-related conditions are imposed one order higher (Remark
  3.4). This is the multistep analogue of the Prothero–Robinson-type conditions above.

RODAS4 is one of their baselines. On a 2D Gray–Scott problem with direct solves RODAS4 needed
fewer steps than the multistep methods. On a quasi-geostrophic model with GMRES, the Limm
implementation matched or beat RODAS4 and SDIRK4a at similar errors (§8.2–8.3, Figs. 8.2–8.3).

## Related linearly implicit schemes: TASE

[TASE operators](/methods/tase-operators.md) ([Bassenne et al. (2021)](/sources/bassenne-2021.md))
make an explicit Runge–Kutta method stable on stiff problems by preconditioning the
right-hand side with $\sum_{k=0}^{p-1}\omega_{p,k}(2^kI-\vartheta hJ)^{-1}$ (coefficients
$\omega_{p,k}$ and parameter $\vartheta$ page-local, defined there), with $J$ the Jacobian at the current
state (§4.4.1, Eqs. (42)–(43)). Each stage then solves linear systems with shifted
Jacobians and no nonlinear system, which places the resulting scheme in the linearly
implicit family of this page, with $p$ distinct matrices $2^kI-\vartheta hJ$ per stage, i.e.
diagonal coefficients $\vartheta/2^k$, instead of the single matrix $M-h\gamma J_n$. Because the preconditioner equals
$I+\mathcal O(h^p)$ for any bounded $J$, its nonstiff order does not require the exact
Jacobian, as for a W-method. Bassenne et al. do not make this connection, and cite Rosenbrock–Krylov
methods only as solvers for split reaction steps (§1). Conte et al. (2024, §1–2, Remark 2.1) do:
citing González-Pinto et al. (2023), they state that TASE–Runge–Kutta methods are a subclass of
W-methods whose order $p$ is kept for any matrix in place of $J$. Its stiff order conditions, in the sense of the Prothero–Robinson and
parabolic conditions above, have not been studied in the sources.

## The Rodas family (as characterized by Steinebach 2023)

- **ROS3P** (Lang–Verwer): 3 stages, designed for parabolic problems.
- **Ros3prl2** and **Rodas4PR2** (Rang): successors of ROS3PL and Rodas4P. Ros3prl2 is the only
  method whose Prothero–Robinson convergence is independent of $\lambda\in[10^0,10^5]$.
- **Rodas3** (Sandu et al.).
- **Rodas4** (Hairer–Wanner), "the best known method".
- **Rodas4P** and **Rodas4P2** (Steinebach): Rodas4P2 satisfies the W conditions to order 2
  and the Prothero–Robinson conditions.
- **Rodas5** (Di Marzo 1993): 8 stages, order 5(4), no dense output in the original literature.
- **GRK4T** (Kaps–Rentrop): 4 stages, order 4 for ODEs with only three right-hand-side
  evaluations; order 2 on semi-discretized parabolic problems unless the stage boundary data are
  modified.

## Qualifications

- Steinebach (2023) uses "stiffly stable" for $R(\infty)=0$ (§1). That is not Gear's classical
  definition of stiff stability, which is a region condition; the property he means is the one
  this bundle calls L-stability together with A-stability (see [A-stability](/properties/a-stability.md)).
- The Prothero–Robinson problem appears in two sign conventions in Steinebach (2023):
  $y'=\lambda(y-g)+g'$ with $\operatorname{Re}\lambda\ll0$ (Eq. (1.4)) and $y'=-\lambda(y-g)+g'$ with
  $\lambda=10^5$ (§4 problem 2); both describe the same stiff decay.
- Table 1 orders are observed with constant steps on one problem per class; they are not
  theorems.
- **Comparisons with Rosenbrock methods are not like-for-like.** Conte et al. (2024, §7.1–7.2,
  Figs. 7, 9) find TASE–Runge–Kutta methods with a constant, cheap matrix "much more efficient"
  in error against CPU time than the A-stable Rosenbrock methods ROS2, ROS3 and ROS4 of the same
  order with the exact Jacobian, on viscous Burgers and FitzHugh–Nagumo in MATLAB on a laptop.
  The Rosenbrock methods could also freeze their matrix as W-methods, which was not tested.
- **Conte et al.'s claim about W-method stability is not settled here.** It is likely
  overstated: the classical W-method literature, which Conte et al. themselves cite
  (Steihaug–Wolfbrandt, Hairer–Wanner §IV.7 and two AMF-W papers), contains stability analyses
  with approximate Jacobians *(compiler remark, not in the ingested sources)*. No ingested source settles the question.

# Citations

- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Eqs. (1.1)–(1.4), Table 1, Fig. 1), §2 (Eqs. (2.1)–(2.14), Tables 2–4), §3 (Eqs. (3.1)–(3.3)), §4 (problems 2–5, Fig. 3).
- [Biswas et al. (2024)](/sources/biswas-2024.md) — §1, Def. 1.1, §2.3 (origin of the WSO conditions in ROW theory).
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1.3 (earlier names of WSO-type conditions, Rosenbrock DAE methods).
- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §1, §5 (ROW B-series in BSeries.jl).
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §1; §2.5; §4.4.1 (Eqs. (42)–(43); TASE as a linearly implicit scheme).
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §1–2, Thms. 3.3, 3.7, Remarks 3.4, 3.8, §8.2–8.3 (Limm as the multistep analogue; RODAS4 baseline).
- [Conte et al. (2024)](/sources/conte-2024.md) — §1, §1.1, §2 (Remark 2.1), §7 (W-methods, ROS2/3/4 comparisons, Figs. 7, 9).
