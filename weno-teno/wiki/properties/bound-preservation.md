---
type: Property
title: "Bound preservation"
description: "A scheme is bound-preserving when its discrete solution stays in the convex admissible set G of the PDE; the page states the definition and its invariant-domain form, the admissible sets of the sources with their convexity, the cell-average route of Zhang and Shu, the flux-limiting and convex-limiting routes, and the geometric-quasilinearization proofs."
status: established
aliases: [bound-preserving scheme, positivity preservation, invariant-region preservation, invariant-domain preservation, BP, PP, IDP]
tags: [bound-preserving, positivity, limiting, dg, finite-volume]
timestamp: 2026-10-22T12:00:00Z
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
| multicomponent Euler (mixture of $n_c$ ideal gases) | $\{0\le Y_k\le1,\ \rho>0,\ e>0\}$ ($Y_k$ mass fractions) | Renac (2021), Eq. (9) |
| five-equation two-phase model, stiffened gases | $\{0\le\phi_1\le1,\ \phi_k\rho_k\ge0,\ \rho e-\bar p_\infty>0\}$ ($\phi_k$ volume fractions, $\bar p_\infty$ mixture stiffness, page-local) | Wong et al. (2021), Eqs. (10), (12) |
| special relativistic hydrodynamics | $\{D>0,\ E-\sqrt{D^2+\lvert m\rvert^2}>0\}$ ($D=\rho W$ the relativistic mass density, $m$ the momentum) | Wu & Shu (2023), Thm 4.9; Cui et al. (2024), Ex. 4–5 |
| ten-moment Gaussian closure | positive-definite pressure tensor | Wu & Shu (2023), Thm 4.11 |
| ideal MHD | $\{\rho>0,\ E-\tfrac12\rho\lvert v\rvert^2-\tfrac12\lvert B\rvert^2>0\}$ | Wu & Shu (2023), Thm 4.12; Liu et al. (2021), §3.3.4 |
| multicomponent MHD | $0\le Y_k\le1$, $\rho>0$, $p>0$ | Wu & Shu (2023), Eq. (6.4) |

Sources: [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md),
[Renac (2021)](/sources/renac-2021.md),
[Wong et al. (2021)](/sources/wong-2021.md),
[Liu et al. (2021)](/sources/liu-2021.md),
[Zheng et al. (2022)](/sources/zheng-2022.md). The multicomponent and
two-phase models are on the
[multicomponent Euler](/definitions/multicomponent-euler-equations.md) and
[five-equation model](/definitions/five-equation-model.md) pages.

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
equations of state such as JWL (§3.1).

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
$\mathsf w_0^{\mathrm{GL}}=1/(L(L-1))$ with $L=\lceil(N+3)/2\rceil$ in 1D
and on Cartesian $\mathbb Q^N$ cells; Cui et al. prove it optimal there and,
for $\mathbb P^N$ at zero anisotropy, improve it by a factor between 1.5
($N=2,3$) and about 1.74 ($N=6,7$) (Thms 2.3, 4.1; Table 1; the ratios
are the compiler's, from the tabulated values).

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
  $\frac{\Delta t}{\Delta x}\max a^{\mathrm{NS}}\le\varpi=1/(L(L-1))$, $L$ the
  number of Gauss–Lobatto points (Theorem 1, Eq. (3.12); the 2D condition
  (3.30) is strict). The condition is $\Delta t=O(\Delta x)$ and does not
  replace the explicit viscous restriction $\Delta t=O(\mathrm{Re}\,\Delta x^2)$;
  the authors take $\Delta t=\min\{\Delta x/(12a),\ 0.001\,\mathrm{Re}\,\Delta x^2\}$
  and halve the step and restart whenever a stage cell average leaves $G$,
  which terminates by the theorems (§3.3, Eq. (3.33)).
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
third" of the forward-Euler bound (§3.3); see Qualifications.

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
and a ten-moment Lax–Friedrichs scheme (§5). The Navier–Stokes flux of
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
The details are on
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Qualifications

- **Local versus global bounds.** [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)
  state that schemes of order above two cannot be *locally* bound
  preserving in general, so that local discrete maximum principles impose
  a second-order barrier, whereas global bounds (as in the Zhang–Shu
  framework) impose none (§1, §3, citing Zhang and Shu). The claim is
  stated, not proved there. [Pazner (2021)](/sources/pazner-2021.md)
  measures the cost: with strictly enforced local bar-state bounds his
  subcell IDP DGSEM converges at first order on smooth advection (rates
  1.00, 1.04, 1.29 for $N=3,4,5$), and recovers $N+1$ for $N\ge3$ only when
  a modal indicator relaxes the bounds to global ones in smooth cells
  (§4.4, §5.1, Table 1); he calls the first-order behaviour consistent with
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
  polynomials of density and thermal pressure", without saying how the
  pressure polynomial relates to the reconstructed conservative variables
  on which Route 1 guarantees the cell average *(compiler remark, not in the
  sources)*.
- **Clipping is not bound preservation.** MFC clips volume fractions to
  $[0,1]$ and renormalises them only when it evaluates mixture properties,
  so as not to pollute conservation, and claims no positivity
  ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md), §4.2.1,
  Eq. (33)). [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md)
  truncate the reconstructed interface density with $[\cdot]_+=\max(0,\cdot)$
  in their hydrostatic reconstructions and prove no positivity theorem for
  the update (§4.1, Eqs. (4.13)–(4.14)).
- **SSP time stepping.** Fan et al.'s "one third of the CFL" for SSP-RK3
  (§3.3) is stricter than the statement of Wong et al. that the bound is
  unchanged (§5.3). Each stage of the Shu–Osher form that Fan et al. print
  (Eq. (2.6)) is a convex combination of earlier stages and a forward-Euler
  step of size $\Delta t$, so the convexity argument gives the forward-Euler
  bound unchanged, and Fan et al.'s condition is sufficient but not
  required *(compiler check, not in the sources)*; see
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md).
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
