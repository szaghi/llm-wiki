---
type: Method
title: "Invariant-domain preserving high-order time stepping (explicit and IMEX)"
description: "Ern and Guermond rewrite any explicit or IMEX Runge–Kutta tableau in incremental form, each stage built from the closest earlier stage, and limit every stage against a low-order Euler step, so that any method becomes invariant-domain preserving and conservative under a step bound set by the largest abscissa gap."
status: established
aliases: [IDP time stepping, IDP-ERK, IDP-IMEX, invariant-domain-preserving Runge–Kutta, incremental form of the Butcher tableau, efficiency ratio, Ern–Guermond time stepping]
tags: [positivity, structure-preserving, runge-kutta, imex, explicit, ssp]
timestamp: 2026-10-20T16:00:00Z
---

# Invariant-domain preserving high-order time stepping (explicit and IMEX)

A method-of-lines scheme is **invariant-domain preserving** (IDP) if, whenever the
initial degrees of freedom lie in a convex set $\mathcal A$ of admissible states, every
later step does too; for a conservation law it should also keep the total mass
$\sum_im_iy_i$ (page-local: $\mathcal A$ the invariant domain, $m_i$ the lumped masses)
([Ern & Guermond 2022](/sources/ern-2022.md), §1.1, Eqs. (3)–(4)). The standard route is
the [SSP](/methods/strong-stability-preserving-runge-kutta.md) one: write the
Runge–Kutta step as a convex combination of forward Euler steps. Ern and Guermond replace
it by a construction that turns **every** explicit Runge–Kutta method (Part I) and every
IMEX Runge–Kutta pair with an explicit first implicit stage (Part II,
[Ern & Guermond 2023](/sources/ern-2023.md)) into an IDP and conservative method. Each
stage is rewritten as an increment from the closest earlier stage, a low-order
forward-Euler update over the same abscissa gap is computed beside the high-order one,
and a limiter blends the two. Negative Butcher coefficients are allowed, and the step
bound depends only on the abscissae. The construction is the time-stepping half of
[bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md); invariant
domains generalize the positivity of
[positivity preservation](/properties/positivity-preservation.md).

## Structural assumptions on the space discretization

The method needs two discretizations of $\partial_tu=-\nabla\cdot F(u)$ (page-local $u$,
flux $F$): a low-order one,
$M^{\mathrm L}y'=f^{\mathrm L}(y)$ with a diagonal positive (lumped) mass matrix, and a
high-order one, $M^{\mathrm H}y'=f^{\mathrm H}(y)$ (page-local symbols; Ern & Guermond
2022, Eq. (2)). Two hypotheses are assumed (Eqs. (8)–(9)):

1. **Low-order Euler step.** There is $h_{\mathrm{FE}}>0$ such that
   $y\in\mathcal A^I\Rightarrow y+h(M^{\mathrm L})^{-1}f^{\mathrm L}(y)\in\mathcal A^I$ for
   $0<h\le h_{\mathrm{FE}}$ ($\mathcal A^I$ the product over the $I$ degrees of freedom).
   Graph-viscosity continuous finite elements, first-order finite volumes and DG(0) with
   Riemann-type fluxes provide it (Example 2.1, §5.1, Eq. (54)).
2. **Limiter.** A nonlinear operator $\mathscr L$ (page-local) maps a state, a low-order
   increment and a high-order increment to a state in $\mathcal A^I$ whenever the
   low-order update from the same state is in $\mathcal A^I$.

In the conservative version the limiter is a symmetric matrix of coefficients in
$[0,1]$ acting on skew-symmetric antidiffusive fluxes, the flux-corrected-transport
structure (Def. 3.2, Eqs. (25)–(30)); it then conserves mass (Lemma 3.3). Ern and
Guermond use flux-corrected transport only for affine constraints and convex limiting for
invariant domains $\mathcal A=\bigcap_l\{\Psi_l\ge0\}$ with quasiconcave $\Psi_l$
(page-local; §5.3, Eq. (60)).

## Incremental form of an explicit Runge–Kutta method

Take an explicit tableau with $c=A\mathbf 1$ and $c_i\ge0$, and append the row
$a_{s+1,j}:=b_j$, $c_{s+1}:=1$ (Part I, Eqs. (10)–(11)). For each stage $i=2,\dots,s+1$ let
$i'=i'(i)<i$ (page-local) be the earlier stage whose abscissa is closest below:
$c_{i'}\le c_i$ with $c_i-c_{i'}$ minimal; for nondecreasing abscissae $i'=i-1$ (§2.2,
Eq. (12)). Subtracting the stage-$i'$ equation from the stage-$i$ equation, and using
$a_{i'j}=0$ for $j\ge i'$, gives the **incremental form**

$$Y_i=Y_{i'}+h\sum_{j<i}(a_{ij}-a_{i'j})f(Y_j),\qquad \sum_{j<i}(a_{ij}-a_{i'j})=c_i-c_{i'}.$$

**Algorithm (IDP-ERK)** (Algorithm 1, Eqs. (14)–(19)). Set $Y_1=y_n$; for
$i=2,\dots,s+1$:

$$\begin{aligned}
M^{\mathrm L}Y^{\mathrm L}_i&=M^{\mathrm L}Y_{i'}+(c_i-c_{i'})\,h\,f^{\mathrm L}(Y_{i'}),\\
M^{\mathrm H}Y^{\mathrm H}_i&=M^{\mathrm H}Y_{i'}+h\sum_{j<i}(a_{ij}-a_{i'j})\,f^{\mathrm H}(Y_j),\\
Y_i&=\mathscr L\bigl(Y_{i'},\,\text{low-order increment},\,\text{high-order increment}\bigr),
\end{aligned}$$

and $y_{n+1}=Y_{s+1}$ ($Y^{\mathrm L}_i$, $Y^{\mathrm H}_i$ page-local provisional states).
The low-order step is a forward Euler step of length $(c_i-c_{i'})h$ from the already
admissible stage $Y_{i'}$. The high-order fluxes are evaluated at the limited stages. If
the limiter never acts, the replacement of $Y^{\mathrm H}_{i'}$ by $Y_{i'}$ is an
identity and the scheme is the original Runge–Kutta method *(compiler remark from
Eqs. (15)–(17); not stated in the source)*. Per stage the cost is one low-order update,
one high-order update and one limiting, as for an SSP stage (§2.4).

**IDP theorem** (Lemma 2.2, Lemma 3.4). With

$$\Delta c_{\max}:=\max_{2\le i\le s+1}\bigl(c_i-c_{i'(i)}\bigr),\qquad \tfrac1s\le\Delta c_{\max}\le1$$

(page-local), $y_n\in\mathcal A^I$ and $h\,\Delta c_{\max}\le h_{\mathrm{FE}}$ imply
$y_{n+1}\in\mathcal A^I$. The proof is an induction over stages: each low-order step has
length $(c_i-c_{i'})h\le h_{\mathrm{FE}}$, so hypothesis 1 makes it admissible and
hypothesis 2 makes the limited stage admissible. In the conservative version all stages
and $y_{n+1}$ carry the mass of $y_n$ (Lemma 3.4(ii)). Because the sign of
$a_{ij}-a_{i'j}$ is arbitrary, the high-order increment can lose the artificial viscosity
of the fluxes; an optional graph-viscosity term with the nonnegative weight
$(c_i-c_{i'})$ restores it (§3.4, Eqs. (35)–(36)).

## Efficiency ratio

Ern and Guermond measure a method by the **efficiency ratio**
$c_{\mathrm{eff}}:=\tilde h/(s\,h_{\mathrm{FE}})$ (page-local), with $\tilde h$ the
largest step for which the $s$-stage method is IDP: the cost to reach a final time is
about $1/c_{\mathrm{eff}}$ times that of forward Euler at $h_{\mathrm{FE}}$, and
$c_{\mathrm{eff}}\le1$ (Part I, Def. 1.1). For the construction above

$$c_{\mathrm{eff}}\ge\frac1{s\,\Delta c_{\max}},$$

with $c_{\mathrm{eff}}=1$ when the abscissae are equidistributed, $c_i=(i-1)/s$ for
$i=1,\dots,s+1$ (Lemma 2.3). Part II takes $c_{\mathrm{eff}}:=1/(s\Delta c_{\max})$ as the
definition (Eq. (63)). The ratio depends only on the abscissae. No positivity of $A$ or $b$
is required, because admissibility comes from the limiter, not from a convex
decomposition.

**Not the effective SSP coefficient.** The registry's $\mathcal C_{\mathrm{eff}}=\mathcal C/s$
measures how far a method's own convex decomposition into Euler steps reaches;
$c_{\mathrm{eff}}$ measures how far the limited incremental construction reaches. The two
coincide for SSPRK(2,2) ($\tfrac12$) and SSPRK(3,3) ($\tfrac13$), which Part I lists
together with $\tfrac12$ for SSPRK(4,3) and about 0.51 for Kraaijevanger's SSPRK(5,4)
(§2.4, §4.1). For SSPRK(5,4) the 0.51 is $1/(5\Delta c_{\max})$ with
$\Delta c_{\max}\approx0.392$, while its SSP coefficient $\mathcal C\approx1.508$ gives
$\mathcal C_{\mathrm{eff}}\approx0.30$ *(compiler check, not in the sources: abscissae
$\approx(0,0.392,0.586,0.475,0.935)$, $i'=(1,2,2,3,5)$ as Part I reports)*. Numbers of the
two kinds must not be compared, and the "efficiency" of a method quoted on another page in
the SSP sense is not this quantity.

## Methods with optimal efficiency (explicit)

Part I labels methods RK$(s,p;c_{\mathrm{eff}})$ (§4.1):

| method | abscissae | remark |
|---|---|---|
| RK(2,2;1), explicit midpoint | $(0,\tfrac12)$ | not SSP |
| RK(3,3;1), Heun's third-order | $(0,\tfrac13,\tfrac23)$, $b=(\tfrac14,0,\tfrac34)$ | not SSP |
| RK(4,3;1) | $(0,\tfrac14,\tfrac12,\tfrac34)$, rows $(\tfrac14)$, $(0,\tfrac12)$, $(0,\tfrac14,\tfrac12)$, $b=(0,\tfrac23,-\tfrac13,\tfrac23)$ | third order, fourth order on linear problems |
| RK(4,4;1/2), classical RK4 | $(0,\tfrac12,\tfrac12,1)$ | |
| RK(4,4;3/4), 3/8 rule | $(0,\tfrac13,\tfrac23,1)$ | |
| RK(5,4;1), RK(6,4;1) | equidistributed | tableaux in Part II; RK(6,4;1) fifth order on linear problems |
| RK(6,5;2/3), Lawson | $(0,\tfrac14,\tfrac14,\tfrac12,\tfrac34,1)$ | Eq. (39) |
| RK(7,5;1), new | $c_i=(i-1)/7$ | Eq. (40), 16-digit coefficients |

Part I states that RK(4,3;1) is the only four-stage explicit method with equidistributed
abscissae that is fourth order on linear problems, so that no genuinely fourth-order
four-stage method with $c_{\mathrm{eff}}=1$ exists; the computation is not shown (§4.1).
The Lawson class of six-stage fifth-order methods needs $c_6=1$, which caps
$c_{\mathrm{eff}}$ at $\tfrac56$. RK(7,5;1) is a seven-stage fifth-order method: 28
unknowns, 6 row-sum and 17 order conditions, and one condition
$\lvert R(\mathrm i\epsilon)\rvert=1+\rho_6\epsilon^6+O(\epsilon^8)$ with
$\rho_6=-0.009$ (page-local $\epsilon$, $\rho_6$), solved in Julia to $10^{-15}$
(Eq. (40), Fig. 1; see [stability function](/definitions/stability-function.md)). Fifth
order is the point: explicit SSP methods stop at order 4, while the only order barriers
of the incremental construction are those of explicit Runge–Kutta methods (§1.2, §2.4,
§4.5).

## IMEX version

Part II treats $\partial_tu+\nabla\cdot F(u)+g(u,\nabla u)=0$ with a hyperbolic part and a
parabolic part (diffusion and relaxation), semi-discretized as
$M y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$ with $f^{\mathrm E}$ explicit and $f^{\mathrm I}$
implicit (Eqs. (1)–(4)). The implicit term is **quasi-linearized**: a map
$f^{\mathrm I}_{\mathrm{lin}}(w;\cdot)$ (page-local) with
$f^{\mathrm I}_{\mathrm{lin}}(w;w)=f^{\mathrm I}(w)$ whose implicit problems are "easy",
and over a step the system is rewritten as
$My'=f^{\mathrm E}(y)+f^{\mathrm I}(y)-f^{\mathrm I}_{\mathrm{lin}}(y_n;y)+f^{\mathrm I}_{\mathrm{lin}}(y_n;y)$,
explicit plus implicit (Eqs. (9)–(11)). The tableaux are an explicit
$(A^{\mathrm E},b^{\mathrm E},c)$ and an EDIRK $(A^{\mathrm I},b^{\mathrm I},c)$ with
$a^{\mathrm I}_{11}=0$, shared abscissae, $c_1=0$, $c_i\ge0$ and
$A^{\mathrm E}\mathbf 1=A^{\mathrm I}\mathbf 1=c$ (§3.1, Eq. (45)); see
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) and
[diagonally implicit Runge–Kutta](/methods/diagonally-implicit-runge-kutta.md).

Each stage $i$, again written from $i'$, has four steps (Eqs. (50)–(61)):

1. low-order hyperbolic: forward Euler of length $(c_i-c_{i'})h$ from $Y_{i'}$;
2. high-order hyperbolic prediction with the increments $a^{\mathrm E}_{ij}-a^{\mathrm E}_{i'j}$,
   then a hyperbolic limiter (Def. 2.4);
3. low-order parabolic: a quasi-linear backward Euler step of length $(c_i-c_{i'})h$ from
   the limited prediction;
4. high-order parabolic: the implicit stage with diagonal $a^{\mathrm I}_{ii}$ and the
   increments $a^{\mathrm I}_{ij}-a^{\mathrm I}_{i'j}$, then a parabolic limiter that also
   limits a relaxation correction vanishing on the conserved components (Def. 2.5).

**Theorem 3.3.** If forward Euler of the low-order hyperbolic part is IDP for
$h\le h_{\mathrm{FE}}$ and the low-order quasi-linear backward Euler parabolic step is IDP
(Assumption 2.1), and the limiters satisfy Defs. 2.4–2.5, then for
$0<h\le h_{\mathrm{FE}}/\Delta c_{\max}$ the scheme is well defined, IDP and conservative.
The limiters conserve mass because the coefficients are symmetric and the antidiffusive
fluxes skew-symmetric (Lemma 2.6). The parabolic low-order step is often IDP for every
$h$, so the restriction usually comes from the hyperbolic step alone (Remark 2.3). High
order in time requires the high-order quasi-linearization to be frozen at $y_n$ in all
stages (Remark 3.1). A step costs $2s-1$ quasi-linear solves: $s$ low-order and $s-1$
high-order, the last row being explicit (Remark 3.2).

**New IMEX pairs with $c_{\mathrm{eff}}=1$** (§4.3–4.4), labelled
IMEX$(s,p;c_{\mathrm{eff}})$, all with singly diagonal implicit parts and
$b^{\mathrm E}=b^{\mathrm I}$:

| pair | implicit part | remark |
|---|---|---|
| IMEX(2,2;1) | implicit midpoint (EDIRK form) with explicit midpoint | $R(z)=(2+z)/(2-z)$, Eq. (77) |
| IMEX(3,3;1) | three-stage third-order ESDIRK, diagonal $\gamma=\tfrac12+\tfrac1{2\sqrt3}$, with Heun's third-order method | A-stable, not L-stable: $R(-\infty)=1-\sqrt3$; L-stability has no solution in this design (Eq. (81)) |
| IMEX(4,3;1) | L-stable ESDIRK, diagonal $0.4358665215084591$, with RK(4,3;1) | Eq. (82) |
| IMEX(5,4;1) | L-stable ESDIRK, diagonal $0.57281606248213512$ | Eq. (83) |
| IMEX(6,4;1) | L-stable ESDIRK, diagonal $0.2780538411364528$, fifth-order linear conditions | $b_4=0.47$ fixed to make $\rho^{\mathrm E}_6<0$, Eq. (84) |

The coefficients come from order conditions (including the IMEX coupling conditions
$b^\top A^{\mathrm E}A^{\mathrm I}c=b^\top A^{\mathrm I}A^{\mathrm E}c=\tfrac1{24}$), the
L-stability conditions of an EDIRK written in block form, and imaginary-axis expansions
$\rho_6$, solved in Julia (§4.1, Eqs. (64)–(75)). All new tableaux have negative weights
and negative entries, admissible here because positivity comes from limiting (§4). Strang
splitting with explicit and implicit midpoint is a five-stage IMEX scheme with
$c_{\mathrm{eff}}=1$ when only the four flux-evaluating stages are counted (Remark 4.1);
see [operator splitting](/methods/operator-splitting.md).

## Numerical evidence

- **Explicit, linear transport** (Part I, §4.3, Tables 1–6). With fourth-order finite
  differences and $h=\mathrm{CFL}\cdot s\cdot h_{\mathrm{FE}}$ (so that all methods use the
  same number of flux evaluations; Eq. (42)), the methods with $c_{\mathrm{eff}}=1$ keep
  their rates at larger CFL than SSP methods of the same order: at CFL 0.25, SSPRK(2,2)
  leaves the asymptotic regime on the finest mesh (error $5.36\times10^{-5}$) while
  RK(2,2;1) keeps rate 1.99 ($8.73\times10^{-6}$); RK(4,3;1) delivers fourth order
  ($5.39\times10^{-9}$, rate 3.94) where SSPRK(3,3) degrades. RK(7,5;1) and Lawson's
  RK(6,5;2/3) reach the asymptotic range at CFL 0.02 (Table 4). On
  [linear advection](/benchmarks/linear-advection-equation.md) with $\mathbb P_1$ finite
  elements, RK(4,3;1) gives fourth order in $L^\infty$ at CFL 0.2 and is the best method
  overall (Table 6).
- **Explicit, nonsmooth** (§4.4). On the three-solids rotation the explicit midpoint
  rule, "often shun ... for its lack of stability", performs very well with the IDP
  technique ($L^1$ rates about 0.8, Table 7). On a two-dimensional
  [Burgers](/benchmarks/burgers-equation.md) problem with many sonic points, a CFL sweep
  shows SSPRK(2,2) losing accuracy above about 1/2 and stability above about 0.9,
  SSPRK(3,3) above about 1/3 and 0.6, while RK(2,2;1), RK(3,3;1) and RK(4,3;1) behave
  properly over the whole range $[0.05,1]$ (Fig. 4).
- **IMEX, stiff ODE** (Part II, §5.1, Figs. 1–3). On the system
  $y_1'=-2y_1+\varepsilon^{-1}(y_2^2-y_1)$, $y_2'=y_1-y_2-y_2^2$,
  $y_1(0)=y_2(0)=1$, exact $y_2=e^{-t}$, $y_1=y_2^2$, which Part II takes from
  Kennedy–Carpenter, all second-order pairs keep order 2 for $\varepsilon\in\{1,10^{-6}\}$;
  the third- and fourth-order pairs reach design order at $\varepsilon=1$, but the $y_1$
  error falls to second order at $\varepsilon=10^{-6}$, attributed to the pre-asymptotic
  range $\varepsilon<h$ ([order reduction](/definitions/order-reduction.md)). With
  $\mu=1/\varepsilon$ (page-local) this is the system that
  [Fish et al. (2023)](/sources/fish-2023.md) (§4.1.3) call Kaps' problem, there with
  $\mu=100$ *(compiler check, not in the sources: $-2y_1+\varepsilon^{-1}(y_2^2-y_1)=-(\mu+2)y_1+\mu y_2^2$,
  the second equation and the exact solution coincide; Part II does not name it)*.
- **IMEX, viscous scalar law** (§5.2, Tables 1–2). For a travelling viscous wave of
  $\partial_tu+\nabla\cdot(u(1-u),0)-\varepsilon\Delta u=0$ with continuous finite
  elements and flux-corrected-transport limiting, all new pairs give second order with
  $\mathbb P_1$ and fourth order with $\mathbb P_3$ once the mesh resolves the viscous
  layer (e.g. $2.65\times10^{-10}$, rate 3.83, for IMEX(5,4;1) and IMEX(6,4;1) at
  $\varepsilon=2\times10^{-2}$), and first order otherwise.

## Relation to bound-preserving flux limiting and SSP methods

Kuzmin et al. limit the antidiffusive fluxes of the Runge–Kutta update and, where needed,
of the stages, against forward-Euler bounds, for explicit methods of any order
([bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)). Ern and
Guermond write that they became aware of that work "during the revision", that it
"shares the ideas of going beyond the SSP paradigm and applying a limiter after each
stage", and that "the central idea of rewriting the ERK method in incremental form and
maximizing the efficiency of the method appears to be original" (Part I, §1.2). The
difference is the reference state of the stage limiting: Kuzmin et al. limit stage $k$
against a forward-Euler predictor from $y_n$ with bounds scaled by $c_k$; Ern and
Guermond limit against a forward Euler step from the closest earlier limited stage. The
step bound of the first is set by the largest scaled predictor length $c_kh$, that of the
second by the largest abscissa gap *(compiler remark, not stated in either source)*.
[Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) carry the flux
limiting of Kuzmin et al. to DIRK methods with a backward Euler low-order scheme, with no
step restriction, by limiting the time-averaged flux of the whole step; Ern and Guermond's
IMEX version limits stage by stage and keeps the explicit hyperbolic restriction.

Against [SSP methods](/methods/strong-stability-preserving-runge-kutta.md) the claims are:
every explicit method with $c_{\mathrm{eff}}=1$ can be made IDP, whereas SSP excludes such
methods; the explicit order is not limited to 4; and the per-stage cost is the same
(Part I, §2.4). The second claim is the explicit SSP order barrier recalled on the SSP
page. High-order accuracy after limiting rests on the limiter being inactive or nearly so
on smooth solutions, which both papers obtain by relaxing local bounds (Part I, Remark
5.2; Part II, §5.2); neither paper proves that the limited scheme keeps order $p$.

## Qualifications

- **Implicit SSP barrier as stated in Part I.** Part I (§1.2, §2.4) writes that implicit
  SSP Runge–Kutta methods "cannot be more than first-order accurate", citing
  Gottlieb–Shu–Tadmor (Prop. 6.2 of their review, not ingested). As worded it matches the
  barrier for methods SSP for every step size *(compiler reading)*; implicit SSP methods with
  a finite SSP coefficient exist up to order 6, as recalled by
  [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) (§1),
  [Ciallella et al. (2022)](/sources/ciallella-2022.md) (Remark 3.1) and Quezada de Luna &
  Ketcheson (2022, §1). Part I's motivation for an IMEX extension (the step restriction of
  stiff parabolic terms) stands; the barrier as worded overstates it.
- **Efficiency values of earlier IMEX pairs in Part II.** In the version read (the
  pre-review HAL draft hal-03703035v1), Part II prints $c_{\mathrm{eff}}=\tfrac13(1-\gamma)\approx0.24$
  for the ARS pair IMEX(3,2;0.24) with $c=(0,\gamma,1)$, $\gamma=1-1/\sqrt2$;
  $\tfrac13\gamma\approx0.26$ for the Crouzeix–Nørsett pair IMEX(3,3;0.26) with
  $c=(0,\gamma,1-\gamma)$, $\gamma=\tfrac12+\tfrac1{2\sqrt3}$; and $\tfrac1{12}\approx0.08$ for
  the six-stage Calvo–de Frutos–Novo pair IMEX(6,4;0.08) (Eqs. (78)–(80), §4.4.2). Its own
  definition $c_{\mathrm{eff}}=1/(s\Delta c_{\max})$ gives $\Delta c_{\max}=1-\gamma\approx0.707$
  and $c_{\mathrm{eff}}\approx0.471$ for the first; $\Delta c_{\max}=\gamma\approx0.789$ and
  $c_{\mathrm{eff}}\approx0.423$ for the second (Part II gives $i'=(1,1,2)$); and, with the
  abscissae $(0,\tfrac14,\tfrac34,\tfrac{11}{20},\tfrac12,1)$ of the padded Hairer–Wanner
  SDIRK (Hairer–Wanner's Eq. (IV.6.16), which Part II cites but does not print),
  $\Delta c_{\max}=\tfrac12$ and $c_{\mathrm{eff}}=\tfrac13$ for the third. Each
  printed value equals $\Delta c_{\max}/s$ instead of $1/(s\Delta c_{\max})$ *(compiler
  check, not in the sources: the first two from the tableaux printed in Part II, Eqs. (78)
  and (79); the third from the cited tableau)*. The slip is internal to Part II and does not change its
  conclusion: the new pairs have $c_{\mathrm{eff}}=1$ and the older ones less. The
  "$\approx0.46$" and "$\tfrac18$" quoted for two further ARS pairs (Remark 4.2) are not
  checked.
- **Predecessor index as printed.** Both parts print
  $i'(i):=\min\{k\le i-1:c_i-c_k\ge0\}$, which always returns 1 since $c_1=0$; the prose,
  the statement $i'=i-1$ for nondecreasing abscissae and the reported values (e.g.
  $(1,1,2)$ for SSPRK(3,3)) fix the intended definition, the earlier stage minimizing the
  nonnegative gap (Part I, Eq. (12); Part II, Eq. (46)).
- **Theorem 3.3 interval.** Part II prints the admissible steps as
  $(1,h_{\mathrm{FE}}/\Delta c_{\max}]$ (Eq. (62)); the proof, Lemma 2.7 and the text after
  (63) fix $(0,h_{\mathrm{FE}}/\Delta c_{\max}]$.
- **The CFL number of the experiments** is normalized per stage,
  $h=\mathrm{CFL}\cdot s\cdot h_{\mathrm{FE}}$, not the usual Courant number (Part I,
  Eq. (42); Part II, Eq. (91)); the CFL value of Part II's PDE test is not printed.
- **Versions.** Part I was read as the HAL author manuscript of June 2022 and Part II as
  the pre-review HAL draft; equation numbers are those of the versions read.

# Citations

- [Ern & Guermond (2022)](/sources/ern-2022.md) — §1.1–1.2, Def. 1.1, Eqs. (2)–(19), Example 2.1, Lemmas 2.2–2.3, §2.4, §3 (Def. 3.2, Lemmas 3.3–3.4, Eqs. (25)–(36)), §4.1 (Eqs. (39)–(40), Fig. 1), §4.2 (Eq. (42)), §4.3–4.5 (Tables 1–8, Figs. 2–4), §5 (Eqs. (54), (60), Remark 5.2); HAL v2.
- [Ern & Guermond (2023)](/sources/ern-2023.md) — §1, §2 (Assumption 2.1, Defs. 2.4–2.5, Lemmas 2.2, 2.6–2.7, Remark 2.3), §3 (Eqs. (45)–(63), Thm. 3.3, Remarks 3.1–3.2), §4 (Eqs. (64)–(84), Remarks 4.1–4.2), §5 (Eqs. (85)–(91), Figs. 1–3, Tables 1–2); HAL v1.
- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §1, §3.3 (stage limiting); arXiv v2.
- [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) — §1, §4–6; arXiv v1.
- [Ciallella et al. (2022)](/sources/ciallella-2022.md) — Remark 3.1 (implicit SSP order 6); arXiv v3.
- [Fish et al. (2023)](/sources/fish-2023.md) — §4.1.3 (Kaps' problem).
