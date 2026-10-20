---
type: Definition
title: "Order reduction"
description: "Order reduction is the drop of the observed convergence rate of a time integrator below its classical order $p$ on stiff problems, method-of-lines PDEs with boundary data, DAEs or split operators; this page collects its mechanisms, the reduced rates the sources predict and observe, and the remedies."
status: established
aliases: [stiff order reduction, stiff order]
tags: [order-reduction, stiff, runge-kutta, stage-order, dae]
timestamp: 2026-10-20T08:00:00Z
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

**Stage boundary values (IMEX).** [González-Tabernero et al. (2024)](/sources/gonzaleztabernero-2024.md)
(§1, §5) observe the layer directly for IMEX Runge–Kutta methods with explicit convection
and implicit diffusion: imposing time-dependent Dirichlet data at the stage times,
$Y_i|_\Gamma=g(t_n+c_ih)$, gives errors concentrated at the boundaries (Figs. 1, 4) and
observed rates of about 2.5, 2.25 and 2.0 in $L^1$, $L^2$ and $L^\infty$ for a third-order
scheme and for the fourth-order ARK4(3)6L[2]SA alike, on linear and nonlinear
convection–diffusion problems in one and two dimensions (Tables 1–4). They recall that the
same reduction occurs for non-IMEX Runge–Kutta methods (§1). See
[boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md).

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
to its stage order (Southworth et al. 2022, §2.1; [Abu-Labdeh et al. 2023](/sources/abulabdeh-2023.md),
§2, §3.1); see
[differential-algebraic equations](/definitions/differential-algebraic-equation.md).
On an incompressible fluid–structure DAE, [Taddei et al. (2026)](/sources/taddei-2026.md)
(§5.1.1, Table 1) observe fitted rates of about 2.1, 2.4 and 3.5 for Radau IIA with
$s=2,3,4$, against the formal $3,5,7$, and attribute them to "the differential algebraic
structure" together with the spatial discretization, the ALE mesh motion and the
iterative interface coupling; their rates are measured against an $s=4$,
$h=0.001$ reference, and the three-stage errors are not monotone in $h$.

**Splitting with boundary conditions.** In an [operator splitting](/methods/operator-splitting.md)
the boundary conditions hold for $f$ but not for the sub-operators; for
reaction–diffusion with Dirichlet or Neumann data this reduces the order, by one
in the maximum norm for Strang splitting, as recalled by
[Blanes et al. (2024)](/sources/blanes-2024.md), §6.1, from Hansen–Ostermann and
Hundsdorfer–Verwer. [Southworth et al. (2024)](/sources/southworth-2024.md) (§1–2) cite
the order reduction of Strang splitting on stiff problems as one reason to replace the
Lie–Trotter split of radiation hydrodynamics by IMEX Runge–Kutta methods.

**Intermediate stiffness in multiscale problems.** For asymptotic-preserving IMEX
schemes on $u'=T(u)+\varepsilon^{-1}Q(u)$, [Gottlieb et al. (2022)](/sources/gottlieb-2022.md),
Remark 4 and §3.5, observe design order for $\varepsilon=\mathcal O(1)$ and for
$\varepsilon\ll1$ and reduced order in between; their errors plateau at
$\mathcal O(\varepsilon)$ rather than converging at $\mathcal O(h)$, which they
distinguish from the usual asymptotic-preserving order reduction.
[Hu & Shu (2025)](/sources/hu-2025.md) prove where the intermediate regime bites and how
to avoid it for the linear hyperbolic relaxation system with Fourier–Galerkin
discretization: ARS(4,4,3), third order by design, is third order for
$\varepsilon=\mathcal O(1)$ and for $\varepsilon\to0$ but only second order uniformly in
$\varepsilon$, with an error peak near $\varepsilon\approx10^{-4}$–$10^{-3}$ (§1, §6,
Fig. 1). The cause is the low stage order of the intermediate stages: a second-order IMEX
scheme can have intermediate stages of stage order 1, which their uniform second-order
theorem must accommodate (Remark 4.4, Lemma 4.5), while uniform third order needs, in
addition, stage-order conditions $\tfrac12c_i^2=\sum_ja^{\mathrm E}_{ij}c_j=\sum_ja^{\mathrm I}_{ij}c_j$
for $i\ge3$ and a vanishing-coefficient condition, which only their modified BHR(5,5,3)*
satisfies (Thm. 5.1). See
[uniform accuracy of IMEX schemes for relaxation systems](/results/uniform-accuracy-relaxation-systems.md).
[Orlando et al. (2025)](/sources/orlando-2025-b.md) (§4.2) name stiff order reduction,
after DG low-Mach inaccuracy and round-off, as a possible cause of the error saturation of
their IMEX schemes for the Euler equations at Mach $10^{-4}$; their fourth-order IMEX
scheme drops to rate 1.0 at Mach $10^{-2}$ (Table 12).

**Inexact Jacobians in linearly implicit methods.** For the linearly implicit multistep
W-methods of [Glandon et al. (2022)](/sources/glandon-2022.md) (Remark 3.4), the local
error splits into a part annihilated by the classical order conditions and a part
multiplied by the step's Jacobian approximation; when $\lVert hA_n\rVert\not\to0$ (page-local
$A_n$ the approximate Jacobian) the second part, only $\mathcal O(h^p)$, dominates, and the
Jacobian-related order conditions must be imposed one order higher. They suggest that
inexact GMRES solves "possibly" caused the jagged error curves of their variable-order
runs on a quasi-geostrophic model, by degrading stability or by order reduction
(§8.3). See [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md);
the Rosenbrock analogue is the "inexact Jacobian" column of the table above.

**Unbounded operators in exponential integrators.** An exponential method derived from
classical order conditions, with all φ-functions Taylor-expanded, keeps terms
$J^kF(\tau)$ in its leading error. These suffer order reduction when the Jacobian is
unbounded (recalled from Hochbruck & Ostermann by
[Dallerit & Tokman 2025](/sources/dallerit-2025.md), §1, §3). The stiff order conditions
avoid it under analytic-semigroup assumptions, and methods of φ-order $p$ remove every
term $J^kF(\tau)$ with $\lvert\tau\rvert\le p$ from the local error (Thm. 7). That is an
exact statement tree by tree; no error bound uniform in an unbounded $J$ is proved. See
[stiff order conditions of exponential Runge–Kutta methods](/results/exponential-runge-kutta-stiff-order-conditions.md).
In their tests, two semilinear parabolic problems of Hochbruck–Ostermann (designed to
expose order reduction) and a 2D advection–diffusion–reaction problem with Neumann data,
the φ-order methods of orders 3–6 show no order reduction. The stiffly accurate (in the
exponential sense) Rosenbrock method EXPRB_5s4 shows "a slight order reduction" on the
advection–diffusion problem (§7, Fig. 4e).

**Partitioning of stiff nonlinear coupling.** [Buvoli & Southworth (2025)](/sources/buvoli-2025.md)
(§7.2, Fig. 7.3) integrate gray thermal radiation transport (a thick Marshak wave) with
second- and third-order schemes in two formulations. On a coarse 128-cell mesh the
implicit–explicit partitioning shows complete order reduction to first order for every
higher-order scheme. The semi-implicit nonlinear partition, with lagged opacities and the
rest implicit, keeps higher order: their IMEX-NPRK2[43]-SiSa converges at second order even
at the largest steps. On the fine 1000-cell mesh second order is reached at reasonable
steps. The authors attribute it to the partitioning ("order reduction due to stiff nonlinear
behavior, … due to partitionings"), not to the methods themselves. See
[nonlinearly partitioned Runge–Kutta methods](/methods/nonlinearly-partitioned-runge-kutta.md).

**Vanishing initial constituents in Patankar schemes.** For the
[modified Patankar methods](/methods/modified-patankar-methods.md) that keep
production–destruction systems positive, [Torlo et al. (2022)](/sources/torlo-2022.md)
identify a two-parameter limit analogous to stiff order reduction: a constituent of size
$\varepsilon$ at $t=0$ with $h\to0$ and $\varepsilon/h\to0$ (§5, Eq. (40)). Patankar weight
denominators of size $\mathcal O(\varepsilon)$ or $1/\mathcal O(\varepsilon)$ then spoil the
stages (Lemmas 5.2–5.3), and the classical order proofs, which fix $\varepsilon>0$, do not
apply, since "the limits $\Delta t\to0$ and $\varepsilon\to0$ are not interchangeable"
(Suppl. Remark 2.4). Every third- and higher-order scheme analysed drops to global order 2
or 1, and MPRK(2,2,α) with $\alpha>1$ to order 1 with the initial state acting as a spurious
steady state (Thm. 5.4, Table 2; Thm. 5.5 for deferred correction with negative final
weights). On Robertson and HIRES the order-1 schemes miss whole species (§7).

**Post-processing corrections.** For the Patankar predictor–corrector applied to SDIRK steps,
[Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) prove only the worst-case order
$\min(p,q+1)$, i.e. 2 for SDIRK bases with stage order 1, once the threshold of the
correction is $\mathcal O(h^{\min(q+2,p+1)})$ (Prop. 3.23), while observing slopes near the
nominal 3 and 4 on four problems (Tables 4–5). They also report that the same correction
applied to explicit Runge–Kutta bases reduced convergence to first order (§1; no data).

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
| observed $\approx2.5$, $2.25$, $2.0$ in $L^1$, $L^2$, $L^\infty$ for 3rd- and 4th-order IMEX with stage-time Dirichlet data | convection–diffusion(–reaction), time-dependent Dirichlet data | González-Tabernero et al. 2024, Tables 1–4 |
| uniform order 2 for ARS(4,4,3) (design 3); uniform design order under stage-order and vanishing-coefficient conditions | linear hyperbolic relaxation, all $\varepsilon$ | Hu & Shu 2025, Thms. 4.3, 5.1, §6 |
| observed $\approx2.1$, $2.4$, $3.5$ for Radau IIA $s=2,3,4$ | incompressible fluid–structure DAE | Taddei et al. 2026, Table 1 |
| global order 1 or 2 for third- and higher-order Patankar schemes (order 1 for MPRK(2,2,α), $\alpha>1$) | production–destruction systems with a vanishing initial constituent, $\varepsilon/h\to0$ | Torlo et al. 2022, Thm. 5.4, Table 2 |
| proven $\min(p,q+1)$ (2 for SDIRK); observed near nominal 3, 4 | Patankar predictor–corrector on SDIRK | Nurkhametova et al. 2026, Prop. 3.23, Tables 4–5 |
| no order reduction observed for φ-order 3–6 exponential methods; slight reduction for EXPRB_5s4 | semilinear parabolic and advection–diffusion–reaction | Dallerit & Tokman 2025, §7, Figs. 1–4 |
| first order for all higher-order schemes with the implicit–explicit partition; second order with the nonlinear partition | gray radiation transport, coarse mesh | Buvoli & Southworth 2025, §7.2, Fig. 7.3b |

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
5. **Stage boundary values from the PDE.** Computing the boundary values of the internal
   IMEX stages from the stage equations, the PDE (to replace the implicit diffusive term by
   $\partial_tg$ minus the explicit terms) and boundary derivatives of the numerical solution
   restores observed orders 3 and 4 at negligible cost (González-Tabernero et al. 2024,
   §3–5, Tables 1–4); Irksome instead imposes $\partial_tg$ on the stage derivatives
   ([Farrell et al. 2021](/sources/farrell-2021.md), Eq. (18)). See
   [boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md).
6. **Uniform-accuracy conditions for IMEX schemes.** For relaxation systems, extra
   stage-order and vanishing-coefficient conditions on the IMEX tableaux give design order
   uniformly in $\varepsilon$ (Hu & Shu 2025, Thm. 5.1).
7. **Positive coefficients for parabolic splittings.** A splitting of order $r$
   with all coefficients non-negative keeps order $r$ for $u'=(A+B)u$ with $A$, $B$
   generating $C_0$-semigroups (Blanes et al. 2024, §6.4, recalling
   Hansen–Ostermann); see [negative-coefficient barrier](/results/negative-coefficient-barrier.md).

8. **Stiff or φ-order conditions for exponential integrators.** Conditions holding for
   arbitrary matrices give stiffness-independent error constants; φ-order conditions remove the
   $J^kF(\tau)$ terms (Dallerit & Tokman 2025, Thm. 7; see the result page above).
9. **A nonlinear partition of the stiff coupling.** Treating the stiff variables implicitly
   inside the nonlinear terms, rather than splitting the terms additively, keeps second
   order where the implicit–explicit partition reduces to first (Buvoli & Southworth 2025,
   §7.2).

## Qualifications

- **Losses of order that are not stiff order reduction.** Several sources report reduced
  rates from other causes. A bound-preserving flux limiter without relaxation lowers the
  rates of fifth- and sixth-order Runge–Kutta methods with WENO5 to about 2.7 on smooth
  advection ([Kuzmin et al. 2022](/sources/kuzmin-2022.md), Table 3; see
  [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)).
  [Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md) call the observed
  $\mathcal O(\Delta T^{k})$ instead of $\mathcal O(\Delta T^{2k})$ convergence of Parareal
  iterates on a Penning trap "order reduction"; it concerns the iteration, not a
  time integrator, and its cause is unknown (§6.2.3, Fig. 3; see [Parareal](/methods/parareal.md)).
  [Popov (2024)](/sources/popov-2024.md) observes orders saturating near 8 and 4, independent
  of the polynomial degree, on the stiff flame problem $y'=y^2-y^3$ and attributes them to the
  sharp front, without using the term (§2.2, Table 7).
- **Parallel and adaptive SDC.** [Čaklović et al. (2025)](/sources/caklovic-2025.md) observe
  an error plateau of parallel SDC variants on the
  [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md) with
  $\varepsilon=10^{-3}$, which they relate to known order reduction and which more sweeps
  lower (§4.3, Figs. 14–15). [Saupe et al. (2025)](/sources/saupe-2025.md) recall that order
  reduction can affect their increment-based SDC error estimate on very stiff problems and
  that IMEX-SDC can lose order (§2.1–2.2).

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
- Not every observed shortfall is order reduction of the method.
  [Southworth et al. (2024)](/sources/southworth-2024.md) (§5.2) observe reduced orders of
  IMEX schemes on Mach-3 and Mach-45 radiation-hydrodynamics shocks and attribute them to
  the implicit-solve tolerance and to the 10-digit coefficients of the published I-IMEX(3,4,3)
  tableau, not to the methods. Abu-Labdeh et al. (2023, §5.1) refine space and time together
  on Stokes, so their rates mix both errors. The attributions of Taddei et al. (2026) and
  Orlando et al. (2025) above are likewise stated, not demonstrated.
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
- [González-Tabernero et al. (2024)](/sources/gonzaleztabernero-2024.md) — §1; §3–4; §5 Tables 1–4, Figs. 1, 4.
- [Hu & Shu (2025)](/sources/hu-2025.md) — §1; Remark 4.4, Lemma 4.5; Thms. 4.3, 5.1; §6 Fig. 1.
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §5.1.1, Table 1.
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §2, §3.1; §5.1 Tables 1–2.
- [Glandon et al. (2022)](/sources/glandon-2022.md) — Remark 3.4; §8.3.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §1–2 (Strang splitting); §5.2 (observed reductions attributed to tolerances and coefficients).
- [Orlando et al. (2025)](/sources/orlando-2025-b.md) — §4.2, Table 12.
- [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) — §1, §3 (classical vs stiff order conditions), Thm. 7, §7 Figs. 1–4.
- [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) — §7.2, Fig. 7.3 (order reduction of the implicit–explicit partition on the coarse mesh); arXiv v2.
- [Torlo et al. (2022)](/sources/torlo-2022.md) — §5 (Eq. (40), Lemmas 5.2–5.3, Thms. 5.4–5.5, Table 2), §7, Suppl. Remark 2.4; arXiv v5.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §1, Prop. 3.23, Tables 4–5.
- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §5.2, Table 3; arXiv v2.
- [Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md) — §6.2.3, Fig. 3 (Penning trap); arXiv v2.
- [Popov (2024)](/sources/popov-2024.md) — §2.2, Table 7; arXiv v1.
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — §4.3, Figs. 14–15; arXiv v2.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — §2.1–2.2; arXiv v2.
