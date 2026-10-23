---
type: Method
title: "Multirate exponential Runge–Kutta and Rosenbrock methods (MERK, MERB)"
description: "MERK and MERB methods turn the φ-function weights of an exponential Runge–Kutta or Rosenbrock method into polynomial forcings of modified linear fast ODEs that any inner solver integrates; the page gives the construction lemma, the MERB schemes of orders 2–6, the convergence theorem with its inner-solver orders, MERK's order for nonlinear fast parts, and the measured cost."
status: established
aliases: [MERK, MERB, multirate exponential Runge–Kutta, multirate exponential Rosenbrock, MERB2, MERB3, MERB4, MERB5, MERB6]
tags: [multirate, exponential, runge-kutta, order-conditions]
timestamp: 2026-10-20T06:18:00Z
---

# Multirate exponential Runge–Kutta and Rosenbrock methods (MERK, MERB)

Multirate exponential methods are
[multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md) built
from [exponential integrators](/methods/exponential-integrators.md). An exponential
method applies $\phi$-functions of a linear operator to slow nonlinear terms; each
such stage is the exact solution of a **linear** ODE with a polynomial forcing, so
the matrix functions can be replaced by an inner solve of that ODE with any method
and micro step $h=H/m$. The multirate exponential Runge–Kutta (MERK) methods of
Luan, Chinomona & Reynolds (2020) take a fixed linear fast operator,
$y'=Ly+N(t,y)$; the multirate exponential Rosenbrock (MERB) methods of
[Luan et al. (2022)](/sources/luan-2022.md) take the per-step Jacobian as fast
operator. Neither needs matrix functions; MERB pays for its dynamic splitting with a
re-linearization at every macro step (Luan et al. 2022, §1, Remark 2.3).

## Exponential Rosenbrock base (as recalled by Luan et al. 2022, §2.1)

Linearizing at $(t_n,y_n)$,

$$f(t,y)=J_ny+V_nt+N_n(t,y),\qquad J_n=\partial_yf(t_n,y_n),\quad V_n=\partial_tf(t_n,y_n),\quad N_n=f-J_ny-V_nt$$

($V_n$, $N_n$ page-local), gives the explicit exponential Rosenbrock (ExpRB) scheme
with nodes $c_1=0$, $c_i\in[0,1]$:

$$\begin{aligned}
Y_i&=y_n+c_iH\phi_1(c_iHJ_n)f(t_n,y_n)+c_i^2H^2\phi_2(c_iHJ_n)V_n+H\sum_{j=2}^{i-1}a_{ij}(HJ_n)D_j,\\
y_{n+1}&=y_n+H\phi_1(HJ_n)f(t_n,y_n)+H^2\phi_2(HJ_n)V_n+H\sum_{i=2}^{s}b_i(HJ_n)D_i,\qquad D_i=N_n(t_n+c_iH,Y_i)-N_n(t_n,y_n)
\end{aligned}$$

(page-local $D_i$). Because $\partial_yN_n$ and $\partial_tN_n$ vanish at $(t_n,y_n)$,
$D_i=\mathcal O(H^2)$ and every ExpRB method has order at least 2. Luan et al. recall
the stiff ExpRB order conditions of Luan & Ostermann: **seven** conditions up to order
6, against 36 for explicit Runge–Kutta or exponential Runge–Kutta methods of that order
(Table 1, Remark 2.1); for $s=2$ the order-3 condition reads
$b_2c_2^2=2\phi_3$ (scalar arguments $HJ_n$). The stiff order conditions themselves are on
[stiff order conditions of exponential Runge–Kutta methods](/results/exponential-runge-kutta-stiff-order-conditions.md).

## Construction lemma (Luan et al. 2022, Lemma 2.2)

If the weights are linear combinations of $\phi$-functions,
$a_{ij}(HJ_n)=\sum_{k=1}^{\kappa_{ij}}\alpha^{(k)}_{ij}\phi_k(c_iHJ_n)$ and
$b_i(HJ_n)=\sum_{k=1}^{\hat\kappa_i}\beta^{(k)}_i\phi_k(HJ_n)$ (scalar coefficients
$\alpha^{(k)}_{ij},\beta^{(k)}_i$ and term counts $\kappa_{ij},\hat\kappa_i$ page-local, the source's
$\ell_{ij}$, $m_i$; not the Shu–Osher $\alpha_{ij}$), then
$Y_i=v_i(c_iH)$ and $y_{n+1}=v_{n+1}(H)$ for

$$v'=J_nv+p_i(\theta),\quad v(0)=y_n,\qquad p_i(\theta)=N_n(t_n,y_n)+(t_n+\theta)V_n+\sum_{j=2}^{i-1}\Big(\sum_{k=1}^{\kappa_{ij}}\frac{\alpha^{(k)}_{ij}\,\theta^{k-1}}{c_i^kH^{k-1}(k-1)!}\Big)D_j,$$

and the analogous final ODE on $[0,H]$ with $\beta^{(k)}_i/(H^{k-1}(k-1)!)$; $\theta$ is the inner
time (page-local; the source writes $\tau$). The proof
inserts the integral form of $\phi_k$ and recognizes variation of constants. This is
the bridge from exponential to infinitesimal multirate methods: the polynomial
forcing plays the role of the MRI coupling polynomials $\gamma_{ij}(\theta)$.

## MERB (Luan et al. 2022, §2.2, Algorithm 2.1)

Linearize at the MERB solution, solve each stage ODE
$v_i'=J_nv_i+p_i(\theta)$ on $[0,c_iH]$ and the final ODE on $[0,H]$ with an inner
method of micro step $h=H/m$, all from $v(0)=y_n$. The fast operator is
$f^{\{\mathrm f\}}=J_ny$ and the slow one $V_nt+N_n(t,y)$. Stages that share a forcing
polynomial are read off one fast trajectory at the intermediate times (nested
stages), which sets the **fast traversal** per macro step (in units of $H$).

| Method | Base ExpRB | Modified ODEs per step | Slow stages | Fast traversal | Free nodes in experiments |
|---|---|---|---|---|---|
| MERB2 | exponential Rosenbrock–Euler | 1 | 1 | 1 | — |
| MERB3 | exprb32, generalized | 2 | 2 | 1.5 | $c_2=\tfrac12$ |
| MERB4 | exprb42, $c_2=\tfrac34$ | 2 | 2 | 1.75 | — |
| MERB5 | pexprb54s4, generalized, $c_4=\frac{3(5c_3-4)}{5(4c_3-3)}$ | 3 | 4 | 2.075 | $c_2=c_4=\tfrac14$, $c_3=\tfrac{33}{40}$ |
| MERB6 | pexprb65s7, generalized | 3 | 7 | 1.253 | $c_3=c_5=\tfrac1{10}$, $c_2=c_6=\tfrac19$, $c_7=\tfrac18$, $c_4=\tfrac17$ |

For comparison (Table 2): MERK3 needs 3 ODEs (traversal 2.166), MERK4 4 (2.833), MERK5
5 (3.2); MRI-GARK33a 3 and MRI-GARK45a 5, both with traversal 1. MERB3 has
$y_{n+1}=\dots+H\frac2{c_2^2}\phi_3(HJ_n)D_2$, hence the final forcing
$p_{n+1}(\theta)=N_n(t_n,y_n)+(t_n+\theta)V_n+\frac{\theta^2}{c_2^2H^2}D_2$. Luan et al. call
MERB6 "the first-ever sixth-order infinitesimal multirate method" (§2.4.5); before it no
partitioned-RK-based infinitesimal method (MIS, RMIS, MRI-GARK, IMEX-MRI-GARK) exceeded
order four (§1).

## Convergence (Luan et al. 2022, Thms. 2.4, 2.12)

In a strongly continuous semigroup setting ($\lVert e^{tJ}\rVert\le Ce^{\omega t}$ on a
Banach space, sufficiently smooth solution, Assumptions 1–2), the MERB global error splits
exactly into four propagated parts: the drift of the linearization, the local errors of
the base ExpRB method, and the inner-solver errors of the final and of the stage ODEs
(Thm. 2.4). **Theorem 2.12.** If the base ExpRB method has order $p$, the stage ODEs are
solved with order $r_{\mathrm s}$ and the final ODE with order $r_{\mathrm f}$ (page-local; the source's $q$, $r$, renamed because $q$ is the registry stage order) at $h=H/m$, then

$$\lVert y_n-y(t_n)\rVert\le CH^p+CHh^{r_{\mathrm s}}+Ch^{r_{\mathrm f}}=CH^p+\frac C{m^{r_{\mathrm s}}}H^{r_{\mathrm s}+1}+\frac C{m^{r_{\mathrm f}}}H^{r_{\mathrm f}},$$

so $r_{\mathrm s}\ge p-1$ and $r_{\mathrm f}\ge p$ suffice; Luan et al. state that MRI-GARK needs $r_{\mathrm s},r_{\mathrm f}\ge p$
(Remark 2.13). The proof bounds the inner-solver errors with a bounded Jacobian,
$\lVert J_n\rVert\le L_J$ (page-local), through $\phi_1(L_JH)$, so the constants are not
uniform in the fast stiffness *(compiler remark, not in the source)*.

## MERK for nonlinear fast partitions

MERK was derived for a linear fast part. [Fish et al. (2024)](/sources/fish-2024.md)
(§5) show that MERK methods are explicit
[IMEX-MRI-SR](/methods/imex-mri-sr.md) methods ($\Gamma=0$), whose order conditions do
not assume linearity, and prove orders 2, 3 and 4 for MERK2, MERK3 and MERK4 (MERK4 under
$c_6=(3-4c_5)/(4-6c_5)$, which its nodes satisfy) and at least 4 for MERK5, for a
**nonlinear** fast partition; this is "the first theoretical justification" of those
orders. On the Kværnø–Prothero–Robinson problem with a nonlinear fast part they measure
2.06, 3.17, 4.25 and 5.32 for MERK2–5 (Fig. 5). Luan et al. (2022) in turn use MERK3–5 with
"dynamic linearization" (MERK applied to the split $f^{\{\mathrm f\}}=J_ny$), which is
outside MERK's original derivation.

## Measured behaviour (Luan et al. 2022, §3)

Inner solvers have the same order as the method (orders 3–6: Butcher's 3-stage method,
RK4, the explicit part of ARK5(4)8L[2]SA, a Verner 8-stage sixth-order method), although
the theory allows order $p-1$ for the stages. Tests: a 1D reaction–diffusion front
(Savcenco et al.) and a new nonautonomous bidirectional-coupling problem with exact
solution, MATLAB, optimal $m$ found by scanning.

- All methods reach their orders: MERB3–6 measure 3.07, 3.66, 4.7, 6.15 (front) and
  3.44, 3.74, 5.11, 5.81 (coupling); MERK4 with fixed linearization converges at 5.25 on
  the front (Figs. 1–6).
- Dynamic linearization gives smaller errors than fixed linearization, by up to $10^3$ at
  equal $H$ for third-order methods on the coupling problem, and larger optimal $m$.
- MERB is "uniformly the most efficient" in slow evaluations and in MATLAB runtime;
  MRI-GARK always wins in total evaluations because of its traversal 1. The authors call
  MATLAB runtime "a poor proxy" for HPC runtime.

## Qualifications

- Luan et al. (2022) print two coefficient slips that their own forcings correct: the
  MERB4 base weight is printed $\frac{16}9\phi_3$ where the order condition and the forcing
  give $\frac{32}9\phi_3$ ($b_2c_2^2=2\phi_3$ with $c_2=\tfrac34$), and the MERB5 base weight $b_3$
  lacks a factor 2 on $c_4\phi_3$ (the conditions $b_3c_3^2+b_4c_4^2=2\phi_3$,
  $b_3c_3^3+b_4c_4^3=6\phi_4$ give $b_3=(2c_4\phi_3-6\phi_4)/(c_3^2(c_4-c_3))$)
  *(compiler check, not in the source)*. The fixed-splitting slow part of the coupling
  problem prints $w-\beta t$ where $w+\beta t$ is meant.
- "The only existing fifth-order multirate method, MERK5" (Luan et al. 2022, §2.4.4) holds
  only for infinitesimal methods; non-infinitesimal multirate and
  [local time stepping](/methods/local-time-stepping.md) schemes of high order exist.
- No embeddings, step adaptivity or implicit slow treatment are given for MERB (§4).
  [Fish & Reynolds (2023)](/sources/fish-2023.md) (§1, §4.2) list MERK and MERB among infinitesimal families without
  embeddings ([multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md)).

# Citations

- [Luan et al. (2022)](/sources/luan-2022.md) — §1, §2.1 (eqs. 2.1–2.7, Table 1, Remark 2.1), §2.2 (Lemma 2.2, eqs. 2.13–2.17, Remark 2.3), §2.3 (Thms. 2.4, 2.12, Remark 2.13), §2.4 (eqs. 2.59–2.66), §2.5 (Algorithm 2.1), §3 (Table 2, Figs. 1–6), §4.
- [Fish et al. (2024)](/sources/fish-2024.md) — §5 (eqs. 5.1–5.2, Apps. D–E), §6.1 (Fig. 5).
- [Fish & Reynolds (2023)](/sources/fish-2023.md) — §1, §4.2 (MERK and MERB as infinitesimal families; only MRI-GARK has embeddings).
