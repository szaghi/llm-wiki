---
type: Definition
title: "Order reduction"
description: "Order reduction is the drop of the observed convergence rate of a time integrator below its classical order $p$ on stiff problems, method-of-lines PDEs with boundary data, DAEs or split operators; this page collects its mechanisms, the reduced rates the sources predict and observe, and the remedies."
status: established
aliases: [stiff order reduction, stiff order]
tags: [order-reduction, stiff, runge-kutta, stage-order, dae]
timestamp: 2026-10-19T20:00:00Z
---

# Order reduction

A one-step method of classical order $p$ has local error $\mathcal O(h^{p+1})$ with
a constant that grows with the stiffness of the problem. **Order reduction** is the
regime in which that constant dominates: for $|z|=|h\lambda|\gg1$ (stiff ODEs),
for method-of-lines discretizations of initial-boundary-value problems with
non-trivial boundary data, for DAEs of index 2, or for splittings whose
sub-problems do not respect the boundary conditions, the observed rate falls
below $p$, often to roughly the [stage order](/definitions/stage-order.md) $q$
([Biswas et al. 2023](/sources/biswas-2023.md), §1–2;
[Biswas et al. 2024](/sources/biswas-2024.md), §1, §2;
[Southworth et al. 2022](/sources/southworth-2022.md), §2.1). It is a property of
the method–problem pair, not of the method alone: the same scheme converges at
order $p$ once $h$ is small enough to resolve the stiffness (Biswas et al. 2023,
§6.1, Fig. 2). The order a method keeps uniformly in the stiffness, for problems
with a one-sided Lipschitz bound, is its [B-convergence](/definitions/b-convergence.md)
order.

**Not the same as precision-induced loss of order.**
[Croci & Rosilho de Souza (2022)](/sources/croci-2022.md), §3, call the stagnation or
loss of convergence order of a Runge–Kutta method evaluated partly in low-precision
arithmetic "an order-reduction phenomenon". That effect comes from rounding errors of
size proportional to the unit roundoff, not from stiffness or boundary data, and is
treated at [mixed-precision Runge–Kutta methods](/methods/mixed-precision-runge-kutta.md);
this page does not cover it.

## Mechanisms

**Stage defects amplified by stiffness (Runge–Kutta).** On the
[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)
$y'=\lambda(y-g)+g'$ the stages carry local defects proportional to the
stage-order residuals $\tau^{(k)}=Ac^{k-1}-c^k/k$, and the step propagates them
through $z\,b^\top(I-zA)^{-1}$. In the stiff limit $z\to-\infty$ the expansion of
$(I-zA)^{-1}$ produces $b^\top A^{-j}\tau^{(k)}$, $j\ge1$, which the classical
order conditions do not annihilate (Biswas et al. 2023, §2, Eq. (8)). Stage order
removes the defects; [weak stage order](/definitions/weak-stage-order.md) makes them
invisible to the weights.

**Numerical boundary layers (method of lines).** For PDEs with time-dependent
boundary data the reduced accuracy concentrates near the boundary, in a layer whose
width scales with the step (Biswas et al. 2023, §6, after Rosales et al.):
$\mathcal O(h^{1/2})$ for the heat equation (half an order lost in $u_x$ when
$q_{\mathrm w}<p$), $\mathcal O(h)$ for linear advection (a full order lost in
$u_x$), $\mathcal O(h^{1/4})$ for $u_t=-u_{xxxx}$. [Biswas et al. (2025)](/sources/biswas-2025.md),
§1.3 and §5.1, attribute the reduction of explicit methods on hyperbolic
initial-boundary-value problems to the same $\mathcal O(h)$ layers: weak stage
order shrinks their amplitude but does not remove them.

**Rosenbrock methods.** [Steinebach (2023)](/sources/steinebach-2023.md), Table 1,
measures with constant steps the orders of the Rodas family on five problem classes
(stages; order of main(embedded) method):

| method | $s$ | index-1 DAE | Prothero–Robinson | parabolic | index-2 DAE | inexact Jacobian |
|---|---|---|---|---|---|---|
| ROS3P | 3 | 3(2) | 2(2) | 3(2) | 2(1) | 1(1) |
| Ros3prl2 | 4 | 3(2) | 3(2) | 3(2) | 2(1) | 1(1) |
| Rodas3 | 4 | 3(2) | 1(2) | 2(2) | 1(2) | 2(1) |
| Rodas4 | 6 | 4(3) | 1(1) | 2(2) | 1(1) | 1(1) |
| Rodas4PR2 | 6 | 4(3) | 4(3) | 4(3) | 2(2) | 1(1) |
| Rodas4P2 | 6 | 4(3) | 3(3) | 4(3) | 2(2) | 2(1) |
| Rodas5 | 8 | 5(4) | 1(1) | 2(2) | 1(1) | 1(1) |

so order reduction also arises from an index-2 constraint and from an inexact
Jacobian in a [Rosenbrock–Wanner method](/methods/rosenbrock-wanner-method.md).
[Rodas5P](/methods/rodas5p.md) reaches 3 on Prothero–Robinson, about 3.9 on the
parabolic problem and 2 on index 2 (Steinebach 2023, Tables 6–8).

**DAEs.** For index-2 DAEs the order of a Runge–Kutta method is formally limited
to its stage order (Southworth et al. 2022, §2.1); see
[differential-algebraic equations](/definitions/differential-algebraic-equation.md).

**Splitting with boundary conditions.** In an [operator splitting](/methods/operator-splitting.md)
the boundary conditions hold for $f$ but not for the sub-operators; for
reaction–diffusion with Dirichlet or Neumann data this reduces the order, by one
in the maximum norm for Strang splitting, as recalled by
[Blanes et al. (2024)](/sources/blanes-2024.md), §6.1, from Hansen–Ostermann and
Hundsdorfer–Verwer.

**Intermediate stiffness in multiscale problems.** For asymptotic-preserving IMEX
schemes on $u'=T(u)+\varepsilon^{-1}Q(u)$, [Gottlieb et al. (2022)](/sources/gottlieb-2022.md),
Remark 4 and §3.5, observe design order for $\varepsilon=\mathcal O(1)$ and for
$\varepsilon\ll1$ and reduced order in between; their errors plateau at
$\mathcal O(\varepsilon)$ rather than converging at $\mathcal O(h)$, which they
distinguish from the usual asymptotic-preserving order reduction.

**Spatial refinement.** Refining the grid makes a semi-discretization stiffer and
can expose order reduction at fixed temporal method:
[Chinomona and Reynolds (2021)](/sources/chinomona-2021.md), §5.2, measure on the
stiff [brusselator](/benchmarks/brusselator.md) rates 2.86–3.12 on 201 points and
2.41–3.02 on 801 points for third- and fourth-order multirate methods.

**Pre-asymptotic regime of a B-convergent method.** The deferred-correction schemes
DC$2j$ of [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) are proved
to have order $2j$ with stiffness-independent constants (Cor. 4.1), yet they observe the
design order only when the step resolves the Jacobian, $h\Lambda<2$ with $\Lambda$ the
largest Jacobian norm along the solution (page-local), while larger steps are accurate
but converge slowly (§6.7). On the Bernoulli equation DC4 shows orders 3.33–3.79; on the
[Robertson problem](/benchmarks/robertson-problem.md) convergence is slow for $h>1/300$;
on the [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md) ($\mu=1000$) DC2 and
DC4 show order 0 down to $h=7.5\times10^{-6}$ (Tables 6.1, 6.5, 6.6).
[Deferred correction](/methods/deferred-correction.md) gives the scheme.

## Reduced rates stated in the sources

| statement | problem class | source |
|---|---|---|
| worst case: the stage order $q$ | stiff ODEs and PDEs | Biswas et al. 2024, §1 |
| rate $\approx q_{\mathrm w}$ (=1) in the stiff regime, $p$ for small $h$ | Prothero–Robinson, $\lambda=-10^4$ | Biswas et al. 2023, §6.1 |
| $\approx\min\{p,q+1\}$ | stiff PDEs | Southworth et al. 2022, §2.1 |
| $\min(p,q+1)$ with stage order $q$, after Hundsdorfer–Verwer; observed also with $q_{\mathrm w}$ in place of $q$ | linear PDEs with time-dependent boundary data | Biswas et al. 2025, §1.3, §3, §5 |
| $\min(p,q_{\mathrm w})$ | ODEs | Biswas et al. 2025, §3 (unexplained) |
| $\min\{p,r+2+\bar\nu\}$ under the Ostermann–Roche conditions | linear parabolic PDEs | Biswas et al. 2024, §2.3 |
| collocation methods reduce to their stage order, $s$ for $s$-stage Gauss | stiff problems | Farrell et al. 2021, §4.1 |
| $p-1$ for L-stable Rosenbrock methods satisfying Scholz's conditions at fixed large $\lvert\lambda\rvert$ | Prothero–Robinson | Steinebach 2023, §2 |
| design order $2j$ observed only for $h\Lambda<2$; order 0 for DC2 and DC4 on Van der Pol at practical steps | stiff nonlinear ODEs | Koyaguerebo-Imé & Bourgault 2022, §6 |

In the Ostermann–Roche row $r$ is the number of satisfied conditions and $\bar\nu$ a
problem-dependent number (both page-local). [Farrell et al. (2021)](/sources/farrell-2021.md),
§4.1, Figs. 1–2, observe on a manufactured heat-equation solution that two-stage
Gauss–Legendre falls from 4 to "stiff order" 2 in $L^2$, two-stage Radau IIA reduces
in $L^2$ only, and three-stage Radau IIA keeps full accuracy in both $L^2$ and $H^1$.

## Remedies

1. **High stage order.** [Fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md)
   have $q=s$, which is why Southworth et al. (2022, §2.1) and Farrell et al. (2021,
   §1) argue for them; [DIRK methods](/methods/diagonally-implicit-runge-kutta.md)
   cannot exceed $q=2$.
2. **Weak stage order.** Extra algebraic conditions on $(A,b)$ that keep DIRK or
   explicit structure: [DIRK schemes](/methods/dirk-high-weak-stage-order.md) and
   [explicit schemes](/methods/explicit-runge-kutta-high-weak-stage-order.md) with
   high $q_{\mathrm w}$, limited by the
   [weak-stage-order barriers](/results/weak-stage-order-barriers.md).
3. **Prothero–Robinson and parabolic conditions for Rosenbrock methods.** Scholz's
   conditions $C_2(H)=C_3(H)=0$ and the W-method conditions, imposed in Rodas4P,
   Rodas4P2 and Rodas5P (Steinebach 2023, §2–3).
4. **Modified boundary data.** Boundary-corrected stages (Alonso-Mallo and Cano)
   give exact order 4 for GRK4T and Rodas4 on Steinebach's parabolic problem, though
   Rodas5P is more efficient there because of a smaller error constant (Steinebach
   2023, Fig. 3). Biswas et al. (2025, §1) list the drawbacks of boundary
   modifications for explicit methods: they need derivatives of the boundary data,
   introduce parameters, are intrusive and have been studied only in one dimension.
   For splittings, boundary correction functions (Einkemmer–Ostermann) play this
   role (Blanes et al. 2024, §6.1).
5. **Positive coefficients for parabolic splittings.** A splitting of order $r$
   with all coefficients non-negative keeps order $r$ for $u'=(A+B)u$ with $A$, $B$
   generating $C_0$-semigroups (Blanes et al. 2024, §6.4, recalling
   Hansen–Ostermann); see [negative-coefficient barrier](/results/negative-coefficient-barrier.md).

## Qualifications

- The reduced rates are problem-, norm- and regime-dependent. Biswas et al. (2023,
  §6.5) observe order 3 instead of the expected 2 for their $q_{\mathrm w}=1$
  reference DIRK schemes on linear advection and have no explanation.
- Steinebach (2023, §4, problem 3) reports that no Rosenbrock method reaches its
  theoretical "parabolic" order on his nonlinear problem with non-vanishing
  Dirichlet data, because the theory assumes linear problems with vanishing boundary
  conditions; a linear test (not shown) gave full orders.
- [TASE operators](/methods/tase-operators.md) claim to keep the order of the explicit
  method they precondition, on the basis of the nonstiff expansion
  $\mathcal P_p=I+\mathcal O(h^p)$ of the TASE preconditioner $\mathcal P_p$ (defined there); [Bassenne et al. (2021)](/sources/bassenne-2021.md)
  (§2.1, §2.3) do not analyse the stiff regime $\lVert hL\rVert\gg1$ in which the
  method is used, so its order there is open *(compiler check, not in the sources)*.
- Weak stage order is a remedy for linear problems; on nonlinear problems it gives
  partial improvement (Burgers: order 3) or none (Van der Pol), as detailed on
  [weak stage order](/definitions/weak-stage-order.md).

## Contradictions

**Reduced order of Gauss methods on stiff PDEs: stage order $q$ or $q+1$.** *Open.*
Farrell et al. (2021, §4.1) state that on stiff problems collocation methods
"reduce to the maximum truncation error per-stage (e.g. $s$ for an $s$-stage
Gauss–Legendre method)" and observe order 2 for two-stage Gauss–Legendre on their
heat problem (Fig. 1). Southworth et al. (2022, §2.1) state that the observed
accuracy of Runge–Kutta methods on stiff PDEs "can be limited to" $\approx\min\{p,q+1\}$,
which is $s+1$ for Gauss methods; Biswas et al. (2025, §1.3) say that stage order $q$
"typically" reduces the rate to $\min(p,q+1)$, after Hundsdorfer–Verwer. Biswas et al.
(2024, §1) give the stage order $q$ as the worst case, which agrees with Farrell et al. Both are general statements
covering the same method class. A source analysing Gauss methods on a parabolic
problem with time-dependent Dirichlet data, in a stated norm (the Ostermann–Roche
theory recalled by Biswas et al. 2024, §2.3, makes the rate norm- and
problem-dependent), would decide it.

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — §1–2 Eq. (8); §6.1–6.8 Figs. 2–9; §7.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — §1; §2.2–2.3.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1, §1.3; §3; §5.1–5.7.
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 Table 1; §2; §4 Tables 5–8, Fig. 3.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1; §4.1 Figs. 1–2.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1.
- [Chinomona and Reynolds (2021)](/sources/chinomona-2021.md) — §5.2 Fig. 3.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.1; §6.4.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — Remark 4; §3.5.1–3.5.3.
- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — Cor. 4.1; §6.1, §6.5–6.7 (Tables 6.1, 6.5, 6.6).
- [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) — §3 (terminology only).
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §2.1, §2.3 (nonstiff order claim).
