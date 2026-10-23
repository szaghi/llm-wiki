---
type: Method
title: "ADER schemes"
description: "ADER schemes advance a DG or finite-volume solution in one step: an element-local space–time predictor, solved by fixed-point iteration without neighbour data, feeds a corrector that integrates fluxes in time by quadrature; the page gives the two ADER-DG formulations of the sources, their time-step limits, a posteriori subcell limiting and the uses of the predictor."
status: established
aliases: [ADER, ADER-DG, ADER-FV, ADER predictor–corrector, local space–time predictor, one-step ADER]
tags: [dg, finite-volume, limiting, immersed-boundary, multiphase]
timestamp: 2026-10-23T23:45:00Z
---

# ADER schemes

An ADER scheme is a one-step, explicit time discretization of a high-order
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) or finite-volume
method. In each element and each step it first computes a **predictor**, a
space–time polynomial on $K\times[t^n,t^{n+1}]$ that solves the equations in
a weak sense using only the element's own data at $t^n$. A **corrector** then
updates the solution with the DG (or finite-volume) residual
integrated over the time step, by quadrature in time on the predictor.
Neighbouring elements meet only in the corrector, through numerical fluxes
evaluated on the predictor traces. The two bundle sources run ADER-DG of
degree $N=1$–$3$ on unstructured triangles and polygons, after Dumbser and
co-workers ([Ciallella et al. (2024)](/sources/ciallella-2024.md), §3.3;
[Gaburro et al. (2024)](/sources/gaburro-2024.md), §3.1–3.3; both arXiv v1).
Neither paper presents ADER as a contribution: both use it as the time
discretization on which their contribution, a boundary treatment and a
primitive-variable formulation respectively, is built.

Page-local symbols: $q_h$ the predictor and $\hat q_\ell$ its modal
coefficients; $\mathsf b_\ell(x,t)$ the space–time basis functions;
$\mathcal Q$ their number; $\mathsf r_K$ the spatial DG residual of element
$K$ (all terms of the weak form except the time derivative); $t_q$,
$\mathsf w^t_q$ the nodes and weights of the time quadrature; $h_K$ a length
scale of $K$; $(x_{b},y_{b})$ its barycentre.

## Predictor

**Basis.** Both sources use rescaled Taylor monomials about the barycentre,
with time scaled by the same length (Ciallella et al., Eq. (12); Gaburro et
al., Eqs. (23)–(25)):

$$\mathsf b_\ell(x,y,t)=\Big(\frac{x-x_b}{h_K}\Big)^{p_\ell}\Big(\frac{y-y_b}{h_K}\Big)^{q_\ell}\Big(\frac{t-t^n}{h_K}\Big)^{r_\ell},\qquad 0\le p_\ell+q_\ell+r_\ell\le N,$$

with page-local exponents $p_\ell,q_\ell,r_\ell$. Ciallella et al. divide each
factor by its factorial and take $h_K$ the incircle diameter of the
triangle; Gaburro et al. take $h_K$ the radius of gyration of the polygon.
The predictor has the degree $N$ of the DG solution in space and time, so
$q_h=\sum_{\ell<\mathcal Q}\mathsf b_\ell\,\hat q_\ell$ with
$\mathcal Q=\frac1{(d+1)!}\prod_{m=1}^{d+1}(N+m)$ modes in $d$ space
dimensions (Ciallella et al., Eq. (11)): 10 for $N=2$ and 20 for $N=3$ in 2D,
against 6 and 10 spatial modes *(compiler check, not in the sources)*.

**Local space–time weak form.** Testing the PDE with each $\mathsf b_k$ on
$K\times[t^n,t^{n+1}]$ and integrating by parts in time only gives
(Ciallella et al., Eq. (13))

$$\int_K\mathsf b_k(t^{n+1})\,q_h(t^{n+1})\,dx-\int_K\mathsf b_k(t^n)\,u_h^n\,dx-\int_{t^n}^{t^{n+1}}\!\!\int_K\partial_t\mathsf b_k\,q_h\,dx\,dt+\int_{t^n}^{t^{n+1}}\!\!\int_K\mathsf b_k\,\nabla\cdot f(q_h)\,dx\,dt=\int_{t^n}^{t^{n+1}}\!\!\int_K\mathsf b_k\,S(q_h)\,dx\,dt .$$

The initial data enter weakly at $t^n$ (upwinding in time), and the spatial
divergence is taken inside the element, with no numerical flux, so the
problem is local. It is solved by a discrete Picard (fixed-point) iteration
element by element (Ciallella et al., §3.3). Gaburro et al. write the same
form for a quasilinear system $\partial_t\mathsf V+A_{\mathsf V}\partial_x\mathsf V+B_{\mathsf V}\partial_y\mathsf V=0$
in primitive variables (page-local $\mathsf V$, $A_{\mathsf V}$, $B_{\mathsf V}$),
with the non-conservative product in place of $\nabla\cdot f$, and stop the
iteration when the relative $L_2$ change of the predictor falls below
$10^{-7}$ (Eqs. (27)–(31)).

## Corrector

The corrector is the DG update integrated in time. In Ciallella et al.
(Eqs. (9)–(10)), with $M$ the element mass matrix,

$$\hat u^{n+1}=\hat u^n-M^{-1}\int_{t^n}^{t^{n+1}}\mathsf r_K(q_h)\,dt\approx\hat u^n-M^{-1}\Delta t\sum_q\mathsf w^t_q\,\mathsf r_K\big(q_h(t_q)\big),$$

where $\mathsf r_K$ contains the volume integral and the face integrals of a
two-point flux, here the Rusanov flux
([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)) evaluated on the
predictor traces of $K$ and its neighbours. Gaburro et al. keep the
corrector in primitive variables. The face term becomes a path-integral
fluctuation along the segment path,
$\mathcal D^-_n(\tilde{\mathsf v}^+_h-\tilde{\mathsf v}^-_h)$ with the negative part
of the averaged normal matrix computed by eigendecomposition, and the volume
term integrates the non-conservative product over the open element
(Eqs. (32)–(34); [path-conservative schemes](/methods/path-conservative-scheme.md)).
This extends Zanotti & Dumbser, who used primitive variables only in the
predictor, as the authors state (§1).

## Time step

Both sources bound the step by a $1/(2N+1)$ factor:

- Ciallella et al.: $\Delta t<\nu\,h_{\min}/\big((2N+1)\,a\big)$ with $\nu<1/d$
  for DG on unstructured meshes (Eq. (14), Remark 1, citing the literature);
- Gaburro et al.: $\Delta t<\nu\,\lvert K\rvert/\big((2N+1)\,d\,a_K\,\lvert\partial K\rvert\big)$
  with $\nu\le1$, run at $\nu=0.1$ for the first ten steps and $0.5$ after
  (Eq. (21), §5).

Here $a$, $a_K$ are maximum wave speeds and $\lvert K\rvert$, $\lvert\partial K\rvert$ the
element area and perimeter. The one-step update means the residual is
evaluated once per step on the time-quadrature nodes, instead of once per
Runge–Kutta stage.

## A posteriori subcell limiting

Both ADER-DG schemes are stabilized by the a posteriori subcell
finite-volume limiter of Dumbser and co-workers
([MOOD-type a posteriori limiting](/methods/mood-a-posteriori-limiting.md)):
the unlimited ADER-DG candidate is checked for admissibility, and flagged
elements are recomputed on subcells by a second-order
[MUSCL–Hancock](/methods/muscl-hancock.md) scheme, which Gaburro et al.
call "equivalent to a second order ADER-FV scheme" (§3.4). The subcell
counts differ:

- Ciallella et al. split each troubled triangle into $(2N+1)^d$
  sub-triangles, so that the step bound above holds on the subcells with
  $N=0$ and limiting needs no smaller step (Remark 1);
- Gaburro et al. split each polygon into its barycentric triangles and each
  of these into $N^2$ sub-triangles (§3.4).

Gaburro et al. add a third, shock-triggered criterion and switch the
subcell corrector to the conservative variables in shock cells, which
removes the conservation defect of the primitive scheme there (§4.4; see
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)).

## Uses of the space–time predictor

The predictor is a space–time polynomial available before any flux is
computed, and the sources use it in three ways.

- **One boundary reconstruction per step.** Ciallella et al. impose
  boundary conditions on a curved true boundary by a constrained
  least-squares reconstruction in each boundary element
  ([immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)).
  Done in space only, it needs one constrained solve per sub-time node of
  the time integrator, ADER corrector nodes or Runge–Kutta stages (§5.2,
  Fig. 3a). Writing the reconstruction in the predictor's own space–time
  basis makes the least-squares functional $\tfrac12\lvert\mathsf y-\hat q\rvert^2$
  in the coefficients $\mathsf y$ (page-local), so the normal matrix is the
  identity and a single saddle-point system per space–time boundary element
  remains (Eqs. (30)–(33)). With constraints $\mathsf C\mathsf y=\mathsf g$
  (page-local) its solution is the orthogonal projection
  $\mathsf y=\hat q-\mathsf C^\top(\mathsf C\mathsf C^\top)^{-1}(\mathsf C\hat q-\mathsf g)$
  *(compiler check, not in the sources)*. The authors report about 10 %
  lower cost for $N=3$ than the space-only version at near-identical errors
  (§6.1); no timings, hardware or mesh are printed.
- **Primitive variables throughout.** Gaburro et al. evolve
  $\mathsf V=(\rho,v_1,v_2,p,\chi)$ (page-local material marker $\chi$) in
  both predictor and corrector, which avoids evaluating the thermodynamics
  of a mixture across material interfaces (§1, §3;
  [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
- **Ghost data on refined meshes.** In a sub-cycled two-level
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) step for
  a Faraday-type update, [Balsara et al. (2023)](/sources/balsara-2023.md)
  fill fine ghost zones at $t^{n+1/2}$ from the stored coarse ADER
  predictor, but state that it "can never be used to re-initialize a fine
  mesh" because it is only approximately divergence-preserving (§7).

## Evidence

| test | scheme | result |
|---|---|---|
| steady manufactured Euler solution on a curved domain, conformal linear triangles, levels 0–3 | ADER-DG with space–time boundary reconstruction, $N=1$–$3$ | $\rho$ errors at level 3 $1.2295\times10^{-5}$, $2.0771\times10^{-7}$, $1.4723\times10^{-10}$; final rates 2.01, 2.81, 4.07 (Ciallella et al., Table 6; [method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)) |
| same, fully embedded meshes $5^2$–$35^2$ | same | non-monotone rates, e.g. $N=3$: 3.76, 4.17, 1.53, 4.47 (Table 7) |
| [isentropic vortex](/benchmarks/isentropic-vortex.md), polygonal meshes, $t=1$ | primitive-variable ADER-DG, $N=1$–$3$ | final rates on $\rho$/$p$ 2.2/2.2, 2.7/2.7, 3.8/3.6; limiter never active (Gaburro et al., Table 1) |
| circular Sod explosion, $h=1/50$ and $1/215$ | primitive-variable ADER-DG with and without the conservative shock correction | without it the shock speed is wrong; with it the shock is placed correctly (§5.1.4, Fig. 3; [explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)) |
| [double Mach reflection](/benchmarks/double-mach-reflection.md), $N=2$, $h=1/220$ | same | conservative variables used only in shock cells; shear-layer roll-up visible (§5.1.7, Fig. 6) |
| air–helium [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md), $N=2$, $h=1/150$ | same | no spurious pressure waves, against a conservative second-order ENO finite-volume run at $h=1/750$ that produces them (§5.2.2, Fig. 8) |

Gaburro et al.'s abstract states "up to fourth order of accuracy in space
and time"; their printed finest $N=3$ rates are 3.6–3.8 on meshes with
$h\approx0.9$–$1.9$ (Table 1).

## Qualifications

- **Printed counts.** Gaburro et al. print the number of space–time basis
  functions as $\mathrm{dof}(N+1,d)$ (§3.1). For monomials of total degree
  $\le N$ in $(x,y,t)$ the count is $\mathrm{dof}(N,d+1)$, 4 for $N=1$ in 2D,
  whereas $\mathrm{dof}(N+1,2)=6$ *(compiler check, not in the sources)*.
  Ciallella et al. print the index range of their basis in Eq. (12) up to
  $\mathcal Q$, one more than the sum of Eq. (11), which stops at $\mathcal Q-1$.
- **Printed rates.** In Gaburro et al.'s Table 1 the last $N=3$ rates
  printed as 3.8 ($\rho$) and 3.6 ($p$) are 3.53 and 3.40 when recomputed from
  the printed errors and $h=1.15\to0.92$; every other rate of the table is
  reproduced to within 0.05. Rounding of the printed $h$ to two decimals
  moves the recomputed rates to at most 3.69 and 3.56, so it does not
  explain the printed 3.8 for $\rho$ *(compiler check, not in the sources)*.
- **Order claims on embedded meshes.** Ciallella et al. write that "in all
  cases, the expected convergence of $M+1$ is achieved" (§6.1, their $M$ the
  degree); their $N=2$ rates on conformal meshes stay at 2.60–2.97 (Table 6)
  and the embedded rates oscillate (Table 7), which they attribute to the
  way the surrogate boundary cuts the background mesh.
- **Scope.** Both sources are 2D, explicit and on unstructured triangles or
  polygons; neither compares ADER with Runge–Kutta time stepping at equal
  cost, and the cost statement above concerns the boundary treatment, not
  the time discretization.

# Citations

- [Ciallella et al. (2024)](/sources/ciallella-2024.md) — arXiv v1: §3.2–3.4 Eqs. (6)–(14), Remark 1; §5.2 Eqs. (30)–(33), Fig. 3; §6.1 Tables 6–7.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — arXiv v1: §1; §3.1–3.4 Eqs. (19)–(41); §4.4; §5 Table 1, Figs. 3, 6, 8.
- [Balsara et al. (2023)](/sources/balsara-2023.md) — §7.
