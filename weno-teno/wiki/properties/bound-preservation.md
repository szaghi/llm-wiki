---
type: Property
title: "Bound preservation"
description: "A scheme is bound-preserving when its discrete solution stays in the convex admissible set G of the PDE; the page states the definition and its invariant-domain form, the admissible sets of the sources with their convexity, the Zhang–Shu cell-average route with its viscous, reacting-flow and relativistic extensions, the flux-limiting, convex-limiting, filtering and a posteriori (MOOD) routes, and the geometric-quasilinearization proofs."
status: established
aliases: [bound-preserving scheme, positivity preservation, invariant-region preservation, invariant-domain preservation, physical-constraint preservation, BP, PP, IDP, PCP]
tags: [bound-preserving, positivity, limiting, dg, finite-volume]
timestamp: 2026-10-23T16:00:00Z
---

# Bound preservation

Let $G$ be the admissible set (invariant region) of a hyperbolic system: a
set of states, written $G=\{u:g_i(u)>0\ \text{or}\ \ge0,\ i=1,\dots,I\}$
with constraint functions $g_i$, that the exact solution never leaves,
$u(\cdot,0)\in G\Rightarrow u(\cdot,t)\in G$. A numerical scheme is
**bound-preserving** (BP) if the same holds for the discrete solution:
$u_h(\cdot,t^0)\in G\Rightarrow u_h(\cdot,t^n)\in G$ for all $n$
([Wu & Shu (2023)](/sources/wu-2023-b.md), §1, Eq. (1.4)). Positivity
preservation (density and pressure, or density and internal energy, for gas
dynamics) and the maximum principle (scalar laws) are the instances Cui et
al. treat ([Cui, Ding & Wu (2024)](/sources/cui-2024.md), §1, §7).

**Invariant-domain form.** [Pazner (2021)](/sources/pazner-2021.md)
(§2, Def. 1, after Guermond and Popov) defines the admissible sets through
the Riemann problem: $G$ is an *invariant set* if, for all $u^\pm\in G$ and
every unit direction, the average of the self-similar entropy solution of
the Riemann problem over $[-a_{\max}t,a_{\max}t]$ stays in $G$ for all
$t>0$ ($a_{\max}$ its maximum wave speed, page-local; the source writes $A$
and $\lambda_{\max}$). A scheme is
**invariant-domain preserving** (IDP) if a solution in a convex invariant
set stays there. Pazner presents IDP as a generalization of the discrete
maximum principle that implies bound preservation, positivity preservation
and the absence of oscillations of the low-order scheme (§1, §2).

## Admissible sets used by the sources

| System | $G$ | Source |
|---|---|---|
| scalar law | $[U_{\min},U_{\max}]$ (global maximum principle); any interval is an invariant set | Cui et al. (2024), §1; Pazner (2021), Def. 1 |
| linear transport, Vlasov–Poisson | $u\ge0$ | Zheng et al. (2022), Prop. 3.2 |
| Euler / Navier–Stokes | $\{\rho>0,\ \rho e>0\}$; $\rho e$ is concave in $u$ for $\rho>0$ | Wu & Shu (2023), Eq. (2.2); Cui et al. (2024), Rem. 8.1; Fan et al. (2021), Eqs. (3.7), (3.25) |
| Euler with a minimum principle on the specific entropy | $\{\rho>0,\ \rho e>0,\ s\ge s_{\min}\}$, i.e. $p\rho^{-\gamma}\ge\exp(s_{\min})$; Pazner writes the specific entropy as $\ln(e^{1/(\gamma-1)}\rho^{-1})$ | Wu & Shu (2023), Eq. (2.3), Thm 4.7; Pazner (2021), Eq. (65) |
| Euler with a local minimum of $\rho s$ at the solution nodes | $\{\rho\ge\rho_{\min},\ p\ge p_{\min},\ \rho s\ge(\rho s)^K_{\min}\}$, floors $10^{-8}$, bound over the element and its face neighbours | Dzanic & Witherden (2022), §3.2, §4.1 |
| multicomponent Euler (mixture of $n_c$ ideal gases) | $\{0\le Y_k\le1,\ \rho>0,\ e>0\}$ ($Y_k$ mass fractions) | Renac (2021), Eq. (9) |
| reacting multicomponent Navier–Stokes, calorically perfect species | $\{\rho\ge0,\ P(u)\ge0,\ \rho Y_k\ge0\}$, $P=E-\sum_k\rho Y_kh_k(0)-\tfrac12\rho\lvert v\rvert^2=p/(\gamma(u)-1)$ ($h_k(0)$ formation enthalpies, page-local); $Y_k\le1$ is not in $G$ | Du & Yang (2022), §4.1, Eq. (4.1) |
| five-equation two-phase model, stiffened gases | $\{0\le\phi_1\le1,\ \phi_k\rho_k\ge0,\ \rho e-\bar p_\infty>0\}$ ($\phi_k$ volume fractions, $\bar p_\infty$ mixture stiffness, page-local) | Wong et al. (2021), Eqs. (10), (12) |
| special relativistic hydrodynamics | $\{D>0,\ E-\sqrt{D^2+\lvert m\rvert^2}>0\}=\{\rho>0,\ p>0,\ \lvert v\rvert<1\}$ ($D=\rho W$ the relativistic mass density, $m$ the momentum, $E$ the relativistic energy) | Wu & Shu (2023), Thm 4.9; Chen & Wu (2022), Lemmas 2.1–2.2; Cui et al. (2024), Ex. 4–5 |
| ten-moment Gaussian closure | positive-definite pressure tensor | Wu & Shu (2023), Thm 4.11 |
| ideal MHD | $\{\rho>0,\ E-\tfrac12\rho\lvert v\rvert^2-\tfrac12\lvert B\rvert^2>0\}$ | Wu & Shu (2023), Thm 4.12; Liu et al. (2021), §3.3.4 |
| ideal MHD with a local minimum of $p\rho^{-\gamma}$ at the solution nodes | $\{\rho>\epsilon_{\mathrm f},\ p>\epsilon_{\mathrm f},\ p\rho^{-\gamma}>(p\rho^{-\gamma})^K_{\min}+\epsilon_{\mathrm f}\}$, tolerance $\epsilon_{\mathrm f}=10^{-8}$ (page-local), bound over the element and its face neighbours from the previous stage | Dzanic & Witherden (2023), Eqs. (21)–(22), §4 |
| multicomponent MHD | $0\le Y_k\le1$, $\rho>0$, $p>0$ | Wu & Shu (2023), Eq. (6.4) |

Sources: [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md),
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md),
[Dzanic & Witherden (2023)](/sources/dzanic-2023.md),
[Du & Yang (2022)](/sources/du-2022-b.md),
[Chen & Wu (2022)](/sources/chen-2022-b.md),
[Renac (2021)](/sources/renac-2021.md),
[Wong et al. (2021)](/sources/wong-2021.md),
[Liu et al. (2021)](/sources/liu-2021.md),
[Zheng et al. (2022)](/sources/zheng-2022.md). The multicomponent and
two-phase models are on the
[multicomponent Euler](/definitions/multicomponent-euler-equations.md) and
[five-equation model](/definitions/five-equation-model.md) pages, the
relativistic one on
[relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md).
Chen & Wu call bound preservation for that set *physical-constraint
preservation* (PCP).

**Convexity.** Every set in the table is convex, and convexity is not
incidental: [Wu & Shu (2023)](/sources/wu-2023-b.md) take "$G$ convex with
nonempty interior" as the minimal hypothesis of their theory
(Assumption 3.4), because the cell-average arguments below write updated
states as convex combinations of admissible states, and because a set that
is an intersection of halfspaces is necessarily convex (§3). The constraint
functions themselves need not be concave (§3). In the Zhang–Shu limiter for
MHD they replace the non-concave pressure by the concave
$E-\frac12(\lvert\rho v\rvert^2/\rho+\lvert B\rvert^2)$ (App. B). For gas
dynamics convexity follows from the concavity of $\rho e$, which
[Fan et al. (2021)](/sources/fan-2021.md) call straightforward to check
(Eq. (3.8)). For two-phase flows it is a theorem with a hypothesis:
[Wong et al. (2021)](/sources/wong-2021.md) prove that $\rho e-\bar p_\infty$
is concave, hence $G$ convex, if one phase has $p_{\infty,k}=0$ and the smaller
ratio of specific heats, and that it cannot be concave otherwise (Lemma 1,
Theorem 1); they call the hypothesis mild for gas–liquid pairs (water
$\gamma$ 4–7 against 1.4 for air, §2). Fan et al. also note that
$p>0\Leftrightarrow e>0$ holds for the ideal gas and fails for other
equations of state such as JWL (§3.1). For reacting mixtures
[Du & Yang (2022)](/sources/du-2022-b.md) use that the mixture
$\gamma(u)-1=\sum_kY_kR_u/W_k\big/\sum_kY_kc_{v,k}$ is positive for
$Y_k\ge0$, so $p\ge0\Leftrightarrow P(u)\ge0$, and that $P$ is concave,
hence $G$ convex (§4.1; $R_u$, $W_k$, $c_{v,k}$ the gas constant, molar
masses and specific heats, page-local). For relativistic hydrodynamics
$g(u)=E-\sqrt{D^2+\lvert m\rvert^2}$ is concave (Chen & Wu, Lemma 2.1,
recalled from Wu & Tang).

## Route 1: first-order BP scheme, cell-average decomposition, scaling limiter

The framework recalled by [Cui et al. (2024)](/sources/cui-2024.md) (§1,
Eqs. (1.3)–(1.8), after Zhang and Shu) and used by
[Wu & Shu (2023)](/sources/wu-2023-b.md) (§6, App. B),
[Fan et al. (2021)](/sources/fan-2021.md) (§3),
[Renac (2021)](/sources/renac-2021.md) (§6) and
[Liu et al. (2021)](/sources/liu-2021.md) (§3.3.4) has three ingredients.

1. **A BP first-order scheme.** With a monotone or otherwise BP two-point
   flux $h$, the three-point update
   $\bar u_i^{n+1}=\bar u_i^n-\frac{\Delta t}{\Delta x}\big(h(\bar u_i,\bar u_{i+1})-h(\bar u_{i-1},\bar u_i)\big)$
   stays in $G$ under $a\Delta t/\Delta x\le c_0$. Cui et al. give $c_0=1$
   for the [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) and
   $c_0=1/2$ for [HLL and HLLC](/methods/hll-riemann-solvers.md)
   (§7, after Eq. (7.5)); let $c_0$ denote this first-order BP CFL
   constant (page-local). Wu & Shu prove the Lax–Friedrichs case for Euler
   by geometric quasilinearization: the scheme is BP under $\nu\le1$ with
   $a$ the global maximum of $\lvert v\rvert+c$ (§5.1, Ex. 1.1). Renac's
   entropy-stable relaxation solver for multicomponent Euler is positive
   under $\frac{\Delta t}{\Delta x}\max(\lvert v\cdot n\rvert+a_{\mathrm L}/\rho)<\frac12$,
   $n$ the interface normal and $a_{\mathrm L}$ the relaxation (Lagrangian)
   sound speed (page-local) (§4.3–§4.4, Eq. (52)); Wong et al.'s HLLC scheme for the five-equation model is
   positive and bounded under CFL $\le0.5$ (§3.3).
2. **A cell-average decomposition.** The cell average of the
   high-order polynomial is written as a convex combination of point
   values that includes the interface traces. The high-order cell-average
   update then becomes a convex combination of first-order updates, and
   is BP under a CFL condition proportional to the smallest boundary
   weight $\varpi$ of the decomposition
   ([optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
3. **A limiter** that brings the point values used by the decomposition
   back into $G$ without changing the cell average
   ([Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).

The property that results is called *weak* bound preservation in the
literature these sources recall: the cell average is guaranteed in $G$
when the point values are, and the limiter supplies the point values
([Wu & Shu (2023)](/sources/wu-2023-b.md), concepts recalled in §1 and
§6.2). The BP CFL number of the standard Gauss–Lobatto decomposition is
$\mathsf w_0^{\mathrm{GL}}=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ with $N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$ in 1D
and on Cartesian $\mathbb Q^N$ cells; Cui et al. prove it optimal there and,
for $\mathbb P^N$ at zero anisotropy, improve it by a factor between 1.5
($N=2,3$) and about 1.74 ($N=6,7$) (Thms 2.3, 4.1; Table 1) *(compiler
check, not in the sources: ratios of the tabulated weights)*.

**Extensions of the route in the sources.**

- *Viscous fluxes* ([Fan et al. (2021)](/sources/fan-2021.md), §3,
  Theorems 1–2, after Zhang 2017). For the compressible Navier–Stokes
  equations the numerical flux is a Lax–Friedrichs flux of the *total*
  (advective minus diffusive) flux, with a coefficient (page-local
  $a^{\mathrm{NS}}_{i+1/2}$; the source writes $\beta$)
  $$a^{\mathrm{NS}}_{i+1/2}>\max\Big[\lvert v\rvert+\frac{1}{2\rho^2e}\Big(\sqrt{\rho^2q_{\mathrm h}^2+2\rho^2e\,\lvert\tau_{\mathrm v}-p\rvert^2}+\rho\lvert q_{\mathrm h}\rvert\Big)\Big]$$
  over the two interface states ($\tau_{\mathrm v}$ the viscous stress,
  $q_{\mathrm h}$ the heat flux, page-local), which guarantees
  $u\pm f(u,\nabla u)/a^{\mathrm{NS}}\in G$ for every gradient (Lemma 6 of
  Zhang 2017, as recalled; Eqs. (3.4)–(3.5)). With it, the forward-Euler
  finite-volume HWENO update keeps the cell averages in $G$ if the
  interface states and the decomposition residual are in $G$ and
  $\frac{\Delta t}{\Delta x}\max a^{\mathrm{NS}}\le\varpi=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$, $N_{\mathrm{GL}}$ the
  number of Gauss–Lobatto points (Theorem 1, Eq. (3.12); the 2D condition
  (3.30) is strict). The condition is $\Delta t=O(\Delta x)$ and does not
  replace the explicit viscous restriction $\Delta t=O(\mathrm{Re}\,\Delta x^2)$;
  the authors take $\Delta t=\min\{\Delta x/(12a),\ 0.001\,\mathrm{Re}\,\Delta x^2\}$
  and halve the step and restart whenever a stage cell average leaves $G$,
  which terminates by the theorems (§3.3, Eq. (3.33)).
- *Viscous fluxes in finite differences* ([Fan, Zhang & Qiu (2022)](/sources/fan-2022.md),
  §3–§4, Theorems 1–2). With no cell polynomial, they split the total
  flux with the same coefficient, $\tfrac12(u\pm F/a^{\mathrm{NS}})$, read
  the finite-difference WENO scheme as a formal finite-volume scheme for
  the auxiliary functions of the split variables, and obtain a weak
  positivity result under $\frac{\Delta t}{\Delta x}\max a^{\mathrm{NS}}\le\frac1{2N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}$,
  $N_{\mathrm{GL}}=\lceil(2r+3)/2\rceil$, enforced by a scaling limiter on the
  reconstructed split values and the same halve-and-restart stepping
  ($\Delta t=\min\{0.6\Delta x/\max(\lvert v\rvert+c),\ 0.001\,\mathrm{Re}\,\Delta x^2\}$,
  Algorithm 2). They state that without the flux and limiter WENO-JS5,
  WENO-JS7 and WENO-ZQ5 blow up on every 1D and 2D test of the paper
  (§5; not shown). Both viscous constructions are on
  [positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md).
- *Unstructured quadrilaterals* ([Renac (2021)](/sources/renac-2021.md),
  Lemma 3.2, Thm 6.1, App. A). Extending Perthame–Shu from triangles, a
  positive three-point scheme gives a positive scheme on quadrilateral (and
  star-shaped polygonal) meshes; with it, the entropy-stable DGSEM keeps
  cell averages admissible on straight-sided unstructured quadrilaterals
  under a CFL condition with right-hand side $1/(2N(N+1))$, which carries
  the Gauss–Lobatto endpoint weight $\mathsf w_0=2/(N(N+1))$ on $[-1,1]$
  (Eq. (66), Rem. 6.1). Stationary material interfaces are preserved
  exactly at the nodes ([stationary contact preservation](/properties/stationary-contact-preservation.md)).
- *Semi-Lagrangian schemes* ([Zheng et al. (2022)](/sources/zheng-2022.md),
  Prop. 3.2). In a conservative
  [semi-Lagrangian finite-volume](/methods/semi-lagrangian-finite-volume.md)
  scheme the new cell average is the integral of the reconstruction over
  the upstream cell, so a non-negative reconstruction gives a non-negative
  average without any CFL bound (CFL 10.2 in the tests); the guarantee is
  conditional on exact evaluation of the line integrals, and the limiter
  needs the exact minimum of the polynomial over the cell (Rem. 2.1).
- *Viscous reacting flows* ([Du & Yang (2022)](/sources/du-2022-b.md),
  §3–§5). For local DG on the reacting multicomponent Navier–Stokes
  equations, the total flux $f^{\mathrm a}-f^{\mathrm d}$ (advective minus
  diffusive) is treated as one flux, as in Zhang (2017), with a
  Lax–Friedrichs penalty $a^{\mathrm R}$ (page-local; the source's $\beta$)
  that Lemma 4.1 extends to species: $u\pm f/a^{\mathrm R}\in G$ **iff**
  $a^{\mathrm R}\ge\max\big\{\lvert v+\frac{b}{2\rho P}\rvert+\frac{\sqrt{\mathfrak D}}{2\rho P},\ \lvert v+v_k\rvert\big\}$,
  with $v_k$ the species diffusion velocities and $b$, $\mathfrak D$ built
  from the heat flux, the viscous stress and the pressure (Eq. (3.5);
  page-local). The upper bound $Y_k\le1$ is not limited but follows from
  conservation: with the constant vector $\mathsf v=(1,0,0,0,-1,\dots,-1)$
  (page-local), $u\cdot\mathsf v=\rho-\sum_k\rho Y_k$, and a numerical flux
  with $\hat f\cdot\mathsf v=0$ ("consistent") makes the semi-discrete and
  the fully discrete schemes preserve $\sum_kY_k=1$ exactly (Defs. 2.1, 3.1,
  Thms 3.1–3.2), so non-negative partial densities give $Y_k\le1$. Stiff
  chemistry is integrated by the authors' third-order conservative
  modified exponential Runge–Kutta method, which adds a linear damping
  $\mu_{\mathrm R}u$ (page-local) and writes each stage as a convex
  combination of a convective update and a source update
  $\bar s/\mu_{\mathrm R}+\bar u$; the cell averages stay in $G$ under the
  Gauss–Lobatto CFL bound times $\min\alpha_{jl}/\beta_{jl}$ over the method's
  Shu–Osher coefficients and a lower bound on $\mu_{\mathrm R}$ from the
  production rates (Thms 4.1–4.3, 2D Thms 5.4–5.6). The factor is about
  0.793 *(compiler check, not in the sources: from the printed
  coefficients)*. A four-step
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md) supplies the
  point values. On a stiff accuracy test (source coefficient $10^6$) the
  scheme converges at third order where SSP-RK3 with the same step returns
  NaN (Table 6.2); without the limiter the He/N$_2$ and H$_2$/O$_2$/Ar
  shock tubes blow up (Figs. 6.2–6.3).
- *Relativistic hydrodynamics on triangles* ([Chen & Wu (2022)](/sources/chen-2022-b.md),
  §3). Third-order finite-volume WENO with the HLL flux is PCP under
  $\Delta t\,\hat a\,\lvert e\rvert/\lvert K\rvert\le\frac23\mathsf w^{\mathrm{GL}}_0$
  on every edge (Thm 3.1), from the triangle decomposition of
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md),
  a two-step scaling limiter and the GQL proof of Route 2. Because every
  flux evaluation needs the pressure from a nonlinear equation, the route
  also needs a primitive recovery that is guaranteed to converge to a
  positive pressure for admissible states; Chen & Wu provide three
  (bisection, a contractive fixed point and a hybrid) and note that
  Newton's method can return a negative pressure (§3.4, Rem. 3.6). Without
  the limiter their code fails on most tests (§4).

**Time stepping.** The sources extend the forward-Euler result to
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) and SSP multistep methods,
because SSP methods are convex combinations of forward-Euler steps
([Wu & Shu (2023)](/sources/wu-2023-b.md), §6.2 after Thm 6.4;
[Cui et al. (2024)](/sources/cui-2024.md), footnote 2, Rem. 7.9;
[Renac (2021)](/sources/renac-2021.md), §6.2;
[Pazner (2021)](/sources/pazner-2021.md), §3;
[Wong et al. (2021)](/sources/wong-2021.md), §5.3, "the CFL upper limit is
still 0.5"). The limiter must then be applied at every stage. Fan et al.
state instead that their theorems hold for SSP-RK3 "if the CFL is one
third" of the forward-Euler bound (§3.3); see Qualifications. Du & Yang
replace SSP stepping by an exponential method whose stages are convex
combinations as well, with the CFL factor above (Thm 4.3).

## Route 2: proofs for nonlinear constraints — geometric quasilinearization

For nonlinear $g_i$ (pressure as a function of conservative variables,
implicit pressure in relativistic hydrodynamics, positive-definite
tensors), checking that a convex combination stays in $G$ is the hard
step. [Wu & Shu (2023)](/sources/wu-2023-b.md) replace each nonlinear
constraint by a family of constraints affine in $u$, indexed by free
auxiliary variables: for convex $G$ with piecewise-$C^1$ boundary,
$G=\{u:(u-u_*)\cdot n_*\succ0\ \forall u_*\in\partial G\}$ (Thms 3.9,
3.10). The method page is
[geometric quasilinearization](/methods/geometric-quasilinearization.md).
Its use for BP is that linearity commutes with the convex-combination and
flux-difference structure of the update: Wu & Shu give short BP proofs for
first-order Lax–Friedrichs and gas-kinetic schemes for Euler, a
Navier–Stokes scheme without convex splitting of convection and diffusion,
and a ten-moment Lax–Friedrichs scheme (§5).
[Chen & Wu (2022)](/sources/chen-2022-b.md) use the 2D GQL form of the
relativistic admissible set to prove the HLL flux PCP; the difficulty the
linear form removes is that pressure and velocity are implicit functions
of the conserved variables (§1, §3.5). The Navier–Stokes flux of
Fan et al. above obtains the same guarantee by a different route, a
Lax–Friedrichs coefficient large enough to absorb the viscous flux.

## Route 3: limiting against a low-order BP scheme

A high-order update can be blended with a low-order BP update, in fluxes
or in residuals, with a blending factor chosen so that the result meets
the bounds.

- **Convex limiting with invariant-domain bounds.**
  [Pazner (2021)](/sources/pazner-2021.md) builds a low-order graph-viscosity
  scheme on the Gauss–Lobatto subgrid whose forward-Euler update is a
  convex combination of Guermond–Popov bar states, hence IDP under a CFL
  condition (Props. 6–7), and blends the DGSEM with it node by node or
  subcell face by subcell face (Props. 10–11).
  [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
  blend a DGSEM with a compatible subcell finite-volume scheme and enforce
  positivity of $\rho$ and $p$ either relative to the finite-volume solution
  ($\rho\ge0.1\rho^{\mathrm{FV}}$, $p\ge0.1p^{\mathrm{FV}}$, Eq. (43)) or
  through invariant-domain bounds built from bar states (Eqs. (47)–(48)).
  Details on [convex limiting](/methods/convex-limiting.md) and
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).
- **Flux limiting in finite differences.** The
  [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
  blends, interface by interface, a high-order flux with an admissible
  first-order flux so that the half-cell states of the update stay in $G$.
  [Wong et al. (2021)](/sources/wong-2021.md) write it out for the
  five-equation model with a first-order HLLC flux and prove the
  ingredients (§3.3, §5). Several finite-difference papers obtain
  positivity from the Hu–Adams–Shu version of it rather than from the
  reconstruction: TENO-AA for near-vacuum and Mach 2000 jet cases
  ([Fu (2021)](/sources/fu-2021.md), §5.7, "with the assistant of a
  positivity-preserving flux limiter"), TENO-THINC for the Mach 80 and 2000
  jets ([Takagi et al. (2022)](/sources/takagi-2022.md), §4.9), and
  affine-invariant WENO, which "is not positivity preserving in general"
  and needs the limiter on the Mach 2000 jet, where it activates only near
  the jet front and inlet corners
  ([Wang & Don (2022)](/sources/wang-2022-b.md), §3.2.4, Fig. 8).
  [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) write out the
  parametrized limiter of Xiong, Qiu and Xu for 2D finite differences,
  applied to the Runge–Kutta-combined flux at the final stage, with a
  density step and a pressure step over the 16 vertices of a box of
  limiter parameters (Appendix). Their fifth-order Hermite WENO runs the
  1D and 2D Sedov, double-rarefaction and Leblanc problems without it and
  needs it only on the Mach 2000 jet (0.0146 % of cells limited) and a
  Mach 10 reflection–diffraction problem (0.0012 %) (Ex. 3.5–3.12,
  Remark 3.2); the limiter is sufficient only, and its accuracy rests on
  numerical verification.

## Route 4: a posteriori recomputation (MOOD)

[Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) (§3.2.2)
compute the fourth-order update of their explicit kinetic scheme first,
flag grid points where the recovered density or pressure is non-positive
or NaN, flag the quadrilaterals touching them, and recompute their vertex
residuals with the first-order scheme, which is global Lax–Friedrichs
([MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)).
Done at each deferred-correction cycle this would make the scheme
domain-invariant preserving, they state; in the tests it is done once per
time step. On a radial shock with pressure ratio 1000 it is required, and
the flagged elements are few and at the discontinuities (§5.2.3,
Fig. 10). [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
use MOOD positivity enforcement for their fourth-order DeC radial Sod
runs (Fig. 5).

## Route 5: constraint-driven filtering

[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) assume that the
element mean of nodal DG or flux reconstruction stays admissible under SSP
stepping, a CFL condition and a positivity-preserving Riemann solver (§2.2,
attributed to Zhang & Shu and others "without presenting a comprehensive
proof"), and after every stage filter each violating element with an
exponential modal filter whose strength is the smallest that brings every
nodal value into $G$, including a local minimum of $\rho s$
([entropy filtering](/methods/entropy-filtering.md)). The guarantee is
nodal: between nodes the filtered polynomial may leave $G$. The linear
scaling limiter is the special case of a degenerate filter (§3.1).

[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) extend the filter
to ideal MHD with Powell's non-conservative source term, for which the
standard argument no longer covers the element mean. They split each
forward-Euler step (and each SSP-RK3 stage, Eq. (34)): the conservative
update $u^n+\Delta t\,\mathcal L_1(u^n)$ is filtered by a filter $H_e$
that enforces positivity and the local entropy minimum, the explicit
source contribution $\Delta t\,\mathcal L_2(u^n)$ is then added, and a
second filter $H_p$ re-enforces positivity only (§3.2, Eqs. (32)–(33);
$\mathcal L_1$, $\mathcal L_2$, $H_e$, $H_p$ page-local: flux and source
parts of $\mathcal L$, and the two filters). The justification is that the
source-free mean update lies in $G$ (after Bouchut et al. and the
Zhang–Shu equivalence) and that Wu & Shu proved positivity of the mean
for a locally divergence-free $B$; for a $B$ that is not exactly
divergence-free, positivity of the element mean of nodal DG "remains to
be proven", so the existence of a positivity-preserving filter strength
is not guaranteed (§3.2). $H_p$ is "very rarely" needed, they state.
Without the filter their shock–cloud run diverges with negative
pressure, and the extreme [MHD blast wave](/benchmarks/mhd-blast-wave.md)
(pressure ratio $10^5$) "would diverge almost instantly" (§5.4–5.5).

## Bound preservation and the divergence of the magnetic field

For ideal and multicomponent MHD the BP property of the cell-average
update is tied to a discrete divergence-free condition on $B$: the
first-order Lax–Friedrichs update satisfies the GQL constraint only up to
a term proportional to a discrete $\nabla\cdot B$ ([Wu & Shu (2023)](/sources/wu-2023-b.md),
Thms 6.1–6.2). [Liu et al. (2021)](/sources/liu-2021.md) place a locally
divergence-free [WLS-ENO](/methods/wls-eno.md) reconstruction in the
positivity-preserving finite-volume framework of Wu & Shu (2019, as
recalled: HLL flux, upwind Godunov–Powell source, scaling limiter) and keep
$\rho$ and $p$ positive down to plasma $\beta=10^{-4}$ on the
[MHD blast wave](/benchmarks/mhd-blast-wave.md) and a Mach 800 jet (§4.4–§4.5).
Dzanic & Witherden (2023) state the converse gap for nodal DG with a
Powell source: the BP argument for the element mean needs a divergence-free
field, which their discretization does not have, and their positivity is
therefore observed, not proved (§3.2; Route 5).
The details are on
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Qualifications

- **Local versus global bounds.** [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)
  state that schemes of order above two cannot be *locally* bound
  preserving in general, so that local discrete maximum principles impose
  a second-order barrier, whereas global bounds (as in the Zhang–Shu
  framework) impose none (§1, §3, citing Zhang and Shu). The claim is
  stated, not proved there. [Pazner (2021)](/sources/pazner-2021.md)
  measures the cost: with strictly enforced local bar-state bounds Pazner's
  subcell IDP DGSEM converges at first order on smooth advection (rates
  1.00, 1.04, 1.29 for $N=3,4,5$), and recovers $N+1$ for $N\ge3$ only when
  a modal indicator relaxes the bounds to global ones in smooth cells
  (§4.4, §5.1, Table 1); Pazner calls the first-order behaviour consistent with
  the literature. The invariant-domain bounds of Rueda-Ramírez et al. are
  local as well; that paper reports no convergence-order study.
- **Guarantees that are not guarantees.** When Rueda-Ramírez et al. use
  HLLE or second-order subcell reconstruction as the low-order scheme,
  the bar-state bounds are no longer guaranteed to be attainable, and the
  blending returns the solution "closest to the restrictions" (§5.2.3).
  Those variants are not provably invariant-domain preserving. Renac's
  runs use a practical step bound of 0.4 (§7) that the proved condition
  (66) does not cover; positivity there is observed. Liu et al. print no
  CFL number and report a failure (negative pressure at $t=4.45\times10^{-4}$
  on the Mach 800 jet with degree-2 reconstruction), attributed to the
  ill-conditioning of the least-squares solve and removed by a looser SVD
  truncation (§4.5); they state that their limiter acts on "reconstructed
  polynomials of density and thermal pressure", and do not state how the
  pressure polynomial is obtained from the reconstructed conservative
  variables (§3.3.4).
- **Proved and practised steps differ.** Du & Yang's runs use
  $\Delta t=\min\{a_\Delta\Delta x/a^*,\ b_\Delta\Delta x^2/\eta^*\}$ with a wave speed $a^*$
  that omits the viscous and heat-flux terms of the proved penalty, compute
  the damping rate from $u^n$ only although the theorem needs it at every
  stage, and restart a step with doubled damping and halved $\Delta t$
  whenever a cell average leaves $G$, which Theorem 4.3 guarantees to
  terminate ("very few recomputations are observed", §6, Eqs. (6.1)–(6.2);
  $a_\Delta$, $b_\Delta$, $a^*$, $\eta^*$ page-local, $\eta^*$ the largest viscosity,
  not an entropy). Their 2D detonation runs at $N=1$, because higher
  order needs a further oscillation limiter (§6.6).
- **Entropy control is not positivity.** [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
  find that central DG and SBP finite differences with entropy and
  kinetic-energy [correction terms](/methods/entropy-correction-term.md)
  still blow up on the inviscid Taylor–Green vortex, from negative nodal
  densities or pressures, after which entropy variables cannot be formed
  (§4.2.2, §6); their high-order radial Sod runs use MOOD for positivity
  (Fig. 5).
- **Shock capturing without a bound guarantee.** [Dao & Nazarov (2022)](/sources/dao-2022.md)
  leave positivity and invariant-domain preservation out of scope for
  their residual-viscosity finite elements for MHD (§1, §6); their MHD
  rotor runs with a minimum pressure of $3.86\times10^{-2}$ (§5.5), a
  numerical observation ([artificial viscosity](/methods/artificial-viscosity.md)).
  The robustness that [Fan et al. (2023)](/sources/fan-2023.md) claim for
  their Hermite WENO without limiters is likewise numerical: their
  unlimited isentropic-vortex runs report negative minimum pressures on
  coarse meshes (Table 3.3).
- **Admissible set for general equations of state.**
  [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) note that
  $G=\{\rho>0,\ \rho e>0\}$ is convex for any equation of state, since
  $\rho e(u)$ is concave for $\rho>0$, but that for laws other than the
  ideal gas (e.g. JWL) it no longer ensures positive pressure; positivity
  of $\rho$ and $e$ then suffices for robustness, they state (§1).
- **Clipping is not bound preservation.** MFC clips volume fractions to
  $[0,1]$ and renormalises them only when it evaluates mixture properties,
  so as not to pollute conservation, and claims no positivity
  ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md), §4.2.1,
  Eq. (33)). [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md)
  truncate the reconstructed interface density with $[\cdot]_+=\max(0,\cdot)$
  in their hydrostatic reconstructions and prove no positivity theorem for
  the update (§4.1, Eqs. (4.13)–(4.14)). [Hiejima (2022)](/sources/hiejima-2022.md)
  falls back to first-order interpolation wherever an interpolated density
  or pressure of Hiejima's WCNS is negative, on the double Mach reflection only,
  after Kamiya et al.; the paper does not say on which side or for which
  variables (§3.4), and its 11th-order slip line loses its wavy structure,
  "probably caused by" this fallback.
- **SSP time stepping.** Fan et al.'s "one third of the CFL" for SSP-RK3
  (§3.3) is stricter than the statement of Wong et al. that the bound is
  unchanged (§5.3). Each stage of the Shu–Osher form that Fan et al. print
  (Eq. (2.6)) is a convex combination of earlier stages and a forward-Euler
  step of size $\Delta t$, so the convexity argument gives the forward-Euler
  bound unchanged, and Fan et al.'s condition is sufficient but not
  required *(compiler check, not in the sources)*; see
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md).
- **Entropy functional and tolerance of entropy filtering.** Dzanic &
  Witherden bound different functionals with different tolerances in
  their two papers, and the two numbers $10^{-8}$ and $10^{-4}$ are not
  the same quantity. In the Euler paper (2022, §4.3, Alg. 2;
  [entropy filtering](/methods/entropy-filtering.md)) $10^{-8}$ is the
  positivity floor, $\rho\ge\rho_{\min}$, $p\ge p_{\min}$ with
  $\rho_{\min}=p_{\min}=10^{-8}$, and $10^{-4}$ is a separate absolute
  tolerance on the entropy constraint, a local minimum of
  $\rho s=\rho\ln(p\rho^{-\gamma})$. In the MHD paper (2023, Eqs.
  (21)–(22), §4) one margin $\epsilon_{\mathrm f}=10^{-8}$ is
  subtracted in all three constraints, on $\rho$, $p$ and
  $p\rho^{-\gamma}-(p\rho^{-\gamma})^K_{\min}$ (the entropy constraint is
  printed $\Gamma_3=\sigma-\sigma_{\min}-\epsilon>0$), so the entropy
  bound must be exceeded by $10^{-8}$, where the 2022 tolerance let $\rho s$
  fall $10^{-4}$ below its minimum, and it acts on $p\rho^{-\gamma}$
  instead of $\rho s$. The 2023 paper presents the method as the 2022 one
  without flagging either change, and calls its minimum principle on
  $p\rho^{-\gamma}$ identical to Tadmor's (§2.1, Eq. (5)). These are two
  papers' design choices, not incompatible claims; an absolute tolerance
  on $p\rho^{-\gamma}$ depends on the scaling of the variables *(compiler
  check, not in the sources)*.
- **Strict-interior floors.** Limiters enforce $g(u)\ge\epsilon$ with
  floors such as $10^{-13}$ (Fan et al., Liu et al.) or $10^{-10}$ (Renac,
  who also lets mass fractions go slightly negative, down to a bound set by
  the gas constants, §6.3), not the closed set; Wong et al. bound the volume
  fraction in $[\epsilon,1-\epsilon]$.
- **No BP claim for OEDG.** The oscillation-eliminating DG method computes
  the Mach 2000 jet and double Mach reflection without mentioning a
  positivity limiter and claims no bound preservation
  ([Peng, Sun & Wu (2024)](/sources/peng-2024.md), Ex. 5.17–5.18;
  [OEDG](/methods/oedg.md)).
- **Accuracy of the limiter.** That the scaling limiter keeps high-order
  accuracy is cited, not shown, in Wu & Shu (2023) (App. B) and Fan et al.
  (2021) (Rems. 3.2, 3.4); Cui et al. (2024) show it numerically for
  $\mathbb P^2$, $\mathbb P^4$, $\mathbb P^6$ and $\mathbb P^8$ DG (Ex. 1,
  Tables 3–6), Fan et al. observe fifth order in 1D and fourth in 2D at
  $\mathrm{Re}=100$ with the limiter in the scheme (Table 4.1; how often it
  triggers there is not reported), and Renac reports
  the design order $N+1$ for $N\le3$ with the limiter (Table 1).

# Citations

- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §1 (definition, Eq. (1.4)); §3 (Assumption 3.4, Thms 3.9–3.10); §4.2 (admissible sets); §5 (first-order BP proofs); §6 (MHD, Thms 6.1–6.4); App. B (limiter).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §1 (Zhang–Shu framework, Eqs. (1.3)–(1.15)); §7 (Thms 7.1, 7.5, 7.6; $c_0$ values); Table 1; Rem. 8.1.
- [Pazner (2021)](/sources/pazner-2021.md) — arXiv v1: §1–§2 (Def. 1); §3 (Props. 6–7); §4 (Props. 10–11, Eq. (65)); §4.4; §5.1 (Table 1).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §3.1 (Eqs. (3.4)–(3.8), Theorem 1); §3.2 (Theorem 2, Eq. (3.30)); §3.3 (Eq. (3.33)); Rems. 3.2, 3.4; Table 4.1.
- [Renac (2021)](/sources/renac-2021.md) — arXiv v3: §2 (Eq. (9)); §4.3–§4.4 (Eq. (52)); Lemma 3.2, App. A; §6.2 (Thm 6.1, Eq. (66), Rem. 6.1); §6.3; §7 (Table 1).
- [Wong et al. (2021)](/sources/wong-2021.md) — arXiv v1: §2 (Eqs. (10), (12), Lemma 1, Theorem 1); §3.3; §5; §5.3.
- [Liu et al. (2021)](/sources/liu-2021.md) — §3.3.4 (Eqs. (36)–(38)); §4.4–§4.5.
- [Zheng et al. (2022)](/sources/zheng-2022.md) — Prop. 3.2; Rem. 2.1; §4.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.4 (Eqs. (23)–(29)); §5.2 (Eqs. (43), (47)–(48)); §5.2.3.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §1, §3 (order barrier of local bounds, stated).
- [Fu (2021)](/sources/fu-2021.md) — arXiv v1: Abstract, §5.7 (external positivity-preserving flux limiter).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.9 (positivity-preserving flux limiter for the jets).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.4, Fig. 8 (limiter needed by affine-invariant WENO).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — arXiv v1: §4.2.1, Eq. (33) (clipping only).
- [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md) — arXiv v1: §4.1, Eqs. (4.13)–(4.14) (truncation only).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: Ex. 5.17–5.18 (no positivity limiter mentioned).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — arXiv v1: §1; §2 (Lemmas 2.1–2.2); §3 (Thm 3.1); §3.4 (Rem. 3.6); §3.5; §4.
- [Du & Yang (2022)](/sources/du-2022-b.md) — §2.4 (Def. 2.1); §3 (Def. 3.1, Thms 3.1–3.2, Eq. (3.5)); §4 (Eq. (4.1), Lemma 4.1, Thms 4.1–4.3); §5 (Thms 5.4–5.6); §6 (Eqs. (6.1)–(6.2), Tables 6.1–6.2, Figs. 6.2–6.3, §6.6).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — arXiv v3: §2.2; §3.1–§3.2; §4.1.
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — arXiv v2: §2.1, Eq. (5); §3.1–3.2, Eqs. (21)–(22), (29)–(34); §4; §5.4–5.5.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — arXiv v4: Fig. 5 (MOOD); §4.2.2; §6.
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §3.2.2; §5.2.2–5.2.3, Figs. 9–10.
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — arXiv v1: §1; §5.5; §6.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §1, Eqs. (1.2)–(1.3); §3–§4, Theorems 1–2, Algorithm 2; §5.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Remark 2.3; Ex. 3.3, Table 3.3; Ex. 3.5–3.12, Remark 3.2; Appendix.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §3.4 (first-order fallback).
