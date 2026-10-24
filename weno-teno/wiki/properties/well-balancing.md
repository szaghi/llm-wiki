---
type: Property
title: "Well-balancing"
description: "A scheme for a balance law is well-balanced if it preserves a steady state exactly, such as the lake at rest, moving water, a hydrostatic atmosphere or a stationary wave at a singular source; the sources obtain it from invariant WENO interpolation, stationary-contact-preserving fluctuations, equilibrium variables, flux globalization, hydrostatic reconstruction, deviation evolution and source-aware interface flux pairs."
status: established
aliases: [well-balanced scheme, C-property, lake-at-rest property, exact preservation of still water, hydrostatic reconstruction, subtraction technique, perturbation well-balancing, fully well-balanced scheme, moving-equilibria preservation, stationarity preservation]
tags: [well-balanced, weno, finite-difference, finite-volume, central-scheme, asymptotic-preserving]
timestamp: 2026-10-24T05:59:00Z
---

# Well-balancing

For a balance law $\partial_tu+\partial_xf(u)=S(u)$, a discretization is **well-balanced** for
a given steady state if discrete data equal to that steady state stay unchanged up to
round-off, i.e. the discrete flux divergence and the discrete source cancel exactly. For the
shallow-water equations the steady state of interest is still water, "lake at rest";
[Wang & Don (2022)](/sources/wang-2022-b.md) (§2–§3.3) use "WB-property" and "C-property"
for its exact preservation. Moving-water and discontinuous equilibria are a stronger target,
reached in the bundle by [flux globalization](/methods/flux-globalization.md) (section below);
the equilibria themselves are on [shallow-water equations](/definitions/shallow-water-equations.md).
Below, $h$ is the water depth, $b$ the bottom, $H_{\mathrm s}=h+b$
the free-surface level and $g$ gravity (page-local; $h$ is not a numerical flux here).

## Shallow water: WB from affine invariance

Following Li, Caleffi & Qi (2015) as recalled by Wang & Don (§3.3, Eqs. (26)–(28)), the
equations are written in $(H_{\mathrm s},hv)$,

$$\partial_t\begin{pmatrix}H_{\mathrm s}\\ hv\end{pmatrix}+\partial_x\begin{pmatrix}hv\\ \dfrac{(hv)^2}{H_{\mathrm s}-b}+\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b\end{pmatrix}=\begin{pmatrix}0\\ -gH_{\mathrm s}\,\partial_xb\end{pmatrix},$$

with still water $v=0$, $H_{\mathrm s}=$ const. The scheme is characteristic-wise
finite-difference WENO with global [Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md)
and Roe-averaged eigenvectors. Well-balancing requires that the discrete derivative of
$\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b$ equal the discrete $-gH_{\mathrm s}\partial_xb$ at all
times. With classical WENO weights this needs the "WENO linearization technique" — using the
same nonlinear weights for flux and source (App. B of Li et al., as recalled).

Wang & Don observe that at still water this flux component is an **affine** function of $b$,
with scaling $-gH_{\mathrm s}$ and translation $\tfrac12gH_{\mathrm s}^2$. An
[affine-invariant WENO](/methods/affine-invariant-weno.md) operator commutes with affine maps
(their Thm. 1), so its derivative of the flux equals $-gH_{\mathrm s}$ times its derivative of
$b$, matching the source discretization; and because the characteristic projection is linear,
the property survives [characteristic decomposition](/methods/characteristic-decomposition.md)
(§3.3). Well-balancing is therefore intrinsic, without linearization (contribution).

**Evidence** (§3.3, Figs. 9–10): $x\in[0,10]$, smooth bottom $b_1=5e^{-\frac25(x-5)^2}$ and
discontinuous bottom $b_2=4$ on $[4,8]$, $H_{\mathrm s}=10$, $v=0$, $g=9.812$, $t=50$, up to
1000 points, quadruple precision, no linearization. With $\epsilon=10^{-12}$ the
affine-invariant Z- and D-type schemes keep $\lVert H_{\mathrm s}-10\rVert_\infty$ at round-off
(about $10^{-33}$), while classical and scale-invariant WENO errors fall from about
$10^{-11}$ to $10^{-23}$ with refinement on $b_1$ and stay near $10^{-26}$ on $b_2$. With
$\epsilon=10^{-40}$ all operators are well-balanced except the classical and scale-invariant
D-type ones on $b_1$, whose modifier is not affine invariant. See
[scale and affine invariance](/properties/scale-invariance.md).

## Layered and debris-flow models: WB from stationary contacts

[Balsara et al. (2024)](/sources/balsara-2024.md) link the lake-at-rest property to the
exact preservation of isolated stationary contact discontinuities (§III;
[stationary contact preservation](/properties/stationary-contact-preservation.md)). Their
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md), with the HLLI anti-diffusion
and the bottom carried as a variable with non-conservative products, reproduces perturbed
lake-at-rest tests "without any special modifications for the well-balancing":

- Pitman–Le debris flow: bump $b=0.25(\cos(10\pi(x-\tfrac12))+1)$ for $\lvert x-0.5\rvert\le0.1$,
  equilibrium with constant solid fraction and constant surface, perturbation $10^{-3}$ on
  $[-0.6,-0.5]$, 400 zones on $[-1.2,1.2]$, $t=1.25$ (§VIII.a, Fig. 4);
- two-layer shallow water: bump on $[1.4,1.6]$, interface at $0.65$, surface perturbation
  $0.2$ or $10^{-3}$ on $[1.1,1.2]$, 400 zones on $[0,2]$, $t=0.2$ (§VIII.c, Fig. 9).

## Two-layer shallow water: WB from equilibrium variables

[Chu et al. (2022)](/sources/chu-2022.md) define well-balanced schemes as those "capable of
preserving (several) steady-state solutions of the studied system within a machine accuracy"
(§6.1). For the two-layer shallow-water equations, with upper and lower depths $h_1,h_2$,
discharges $q_k=h_kv_k$, density ratio $r=\rho_1/\rho_2<1$ and bottom $b$ (all page-local; Chu
et al. write $Z$ for the bottom), they follow earlier central-upwind work in replacing $h_2$ by
the interface elevation $w=h_2+b$, so that the unknowns are $(h_1,q_1,w,q_2)$ (Eq. (6.3)):

$$\begin{aligned}
&\partial_th_1+\partial_xq_1=0,\qquad
\partial_tq_1+\partial_x\Big(\frac{q_1^2}{h_1}+\frac g2h_1^2\Big)=-gh_1\,\partial_xw,\\
&\partial_tw+\partial_xq_2=0,\qquad
\partial_tq_2+\partial_x\Big(\frac{q_2^2}{w-b}+\frac g2w^2\Big)=gb\,\partial_xw-gr(w-b)\,\partial_xh_1,
\end{aligned}$$

equivalent to the original form for smooth solutions. The lake at rest is
$v_1=v_2=0$, $h_1=$ const, $w=$ const (Eq. (6.2)). The right-hand sides are non-conservative
products, discretized by the [path-conservative](/methods/path-conservative-scheme.md)
central-upwind scheme inside fifth-order [A-WENO](/methods/alternative-weno.md), with the bottom
interpolated once by the same WENO-Z operator (Remark 6.1). The resulting scheme is stated to
be well-balanced (Abstract, §6.1, §8); no proof is printed. *(compiler check, not in the
sources: at the lake at rest every interpolated state is the constant itself, because WENO-Z
weights sum to one and the characteristic projection is linear; then the jumps $u^+-u^-$, the
built-in anti-diffusion, the path integrals and the cell integrals of $\partial_xw$ and
$\partial_xh_1$ vanish, the point fluxes are constant because $q_1=q_2=0$ removes the only
$b$-dependence, and the A-WENO derivative corrections of constant fluxes are zero, so the right
side vanishes exactly.)* The same paper names flux globalization as the route to moving-water
equilibria, left to future work (§8); the next section records two sources that take it.

**Evidence** (§7.1, Ex. 2, Fig. 7.3): a $10^{-5}$ perturbation of $h_1$ on $0.1<x<0.2$ over the
lake at rest $(h_1,w)=(1,-1)$, $g=10$, $r=0.98$, on $[-0.2,1]$ with $\Delta x=1/100$ to
$t=0.15$, over a smooth bump $b=0.25(\cos(10\pi(x-0.5))+1)-2$ on $0.4<x<0.6$ and over a step
($b=-1.5$ for $x>0.5$, $-2$ otherwise): both the fifth-order and the second-order scheme
propagate the perturbation without spurious oscillations, the fifth-order one with much higher
resolution (reference: $\Delta x=1/1600$).

[Kurganov et al. (2023)](/sources/kurganov-2023.md) state that the original second-order
path-conservative central-upwind scheme preserves only this lake at rest of the two-layer
system (§1, §4).

## Moving and discontinuous equilibria: flux globalization

Writing $\partial_tu+\partial_xK=0$ with a global flux $K=f-\int^xS$ (page-local) makes every steady state a
state of constant $K$ ([flux globalization](/methods/flux-globalization.md)). Three sources build
well-balanced schemes on it, with different discrete notions of the preserved state.

- **Equilibrium variables** ([Kurganov et al. (2023)](/sources/kurganov-2023.md), §4). For
  non-conservative systems whose steady states are $\mathsf E(u)\equiv$ const for algebraic
  equilibrium variables $\mathsf E$ (page-local), the second-order scheme reconstructs
  $\mathsf E$, integrates the non-conservative product along a path linear in $\mathsf E$ with
  trapezoidal quadratures, and lets the global part jump at interfaces; Theorem 4.1 proves that
  discrete data with constant $\mathsf E$ have constant global flux. A further condition is
  needed: the diffusion term of the [central-upwind](/methods/central-upwind-scheme.md) flux
  vanishes at such states only if it is built from modified interface states that coincide
  whenever $\mathsf E^+=\mathsf E^-$ (§4.2). The equilibria covered include discontinuous nozzle
  flows at a jump of the cross-section and two-layer moving-water states over a step; a
  discontinuous nozzle steady state is kept with errors $0$ and $8.88\times10^{-16}$ (Table 7.1).
- **Constant global-flux averages** ([Ciallella et al. (2023)](/sources/ciallella-2023.md), §3).
  The arbitrary-order WENO finite-volume scheme for single-layer shallow water with friction
  keeps every discrete state with $\bar K_i\equiv K_0$ (Prop. 3.1), and, with a split bottom
  source, shared WENO weights and an interface jump of the global part, the lake at rest
  exactly (Prop. 3.3), at $L^2$ errors of about $10^{-13}$ (Table 1). The discrete steady states
  are not the analytical moving equilibria (Remark 3.2), so the method "is not exactly well
  balanced with respect to all analytically computable equilibria" (§1); on moving equilibria
  its errors are 2 to 5 orders of magnitude below a standard WENO scheme at orders 3 and 5, and
  $q$ and $K$ are kept to about $10^{-9}$ (§5.3).

- **Field-wise diffusion with equilibrium variables** ([Chu et al. (2025b)](/sources/chu-2025-b.md),
  Remark 3.1). The LCD-PCCU scheme keeps the global fluxes, the equilibrium-variable
  reconstruction and the modified states $\check u^\pm$ of Kurganov et al. and replaces the
  scalar diffusion by the field-wise one of the
  [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md). The proof follows
  that of Theorem 2.1 of Cao, Kurganov, Liu and Xin (2022), as the authors state: at discrete data with $\mathsf E_i\equiv$ const,
  $K^+_{i+1/2}=K^-_{i+1/2}=K^+_{i-1/2}$ is a constant $\hat K$ (Eq. (3.4)); with
  $\mathcal P+\mathcal M=I$ and $\check u^+=\check u^-$ the numerical flux is $\hat K$ at every
  interface, so the right-hand side vanishes. In 2D (Remark 4.1, proof omitted) the
  dimension-by-dimension scheme preserves only steady states whose $x$-global flux does not
  depend on $x$ and whose $y$-global flux does not depend on $y$; genuinely 2D steady states are
  not preserved, and the authors add that "to the best of our knowledge, no existing numerical
  method is capable of exactly preserving general 2-D steady states, even the smooth ones". On
  the Ripa (thermal shallow-water) system a discontinuous constant-pressure equilibrium,
  $(h,v,\mathsf b)=(2,0,1)$ for $y<0$ and $(1,0,4)$ otherwise ($h$ the depth, $\mathsf b$ the buoyancy,
  registry §10), is preserved by PCCU and LCD-PCCU with zero errors in $h$ and $\mathsf b$ (§5.2.1,
  Ex. 6) *(compiler check, not in the sources: $\tfrac12\mathsf bh^2=2$ on both sides)*.

Ciallella et al. do not compare with still-water well-balanced WENO schemes, citing earlier
work that such methods "do not provide better performances on moving-water equilibria" (§5).

## Stationarity preservation of Active Flux

For linear acoustics, the analogue of well-balancing is the preservation of all discrete
stationary states *(compiler check, not in the sources: for
$\partial_tp+c\nabla\cdot v=0$, $\partial_tv+c\nabla p=0$ these are the states with
$\nabla\cdot v=0$ and $\nabla p=0$)*. As recalled by
[Calhoun et al. (2023)](/sources/calhoun-2023.md) (§1), Barsukow showed that the Cartesian
[Active Flux](/methods/active-flux.md) method with the evolution operator of Barsukow et al. is
stationarity preserving: it adds no dissipation to discrete representations of all stationary
states. Calhoun et al. find that the property "does not carry over to adaptively refined
meshes" with their approaches: with that operator the solver on
[AMR](/methods/adaptive-mesh-refinement.md) grids becomes unstable, stated as an observation
without analysis (§4.6, Conclusions). Their own Eymann–Roe operator is not stationarity
preserving, yet third order plus AMR keeps a stationary vortex accurate to $t=100$ (§4.6,
Fig. 16).

## Euler with gravity: hydrostatic reconstruction

[Arun et al. (2022)](/sources/arun-2022.md) build a first-order finite-volume
scheme for the barotropic Euler equations with gravity and friction,
$p(\rho)=\rho^\gamma$, $\gamma\ge1$, in a multiscale scaling with page-local
relaxation parameter $\varepsilon$ and exponent $\beta_{\mathrm{ms}}\in[0,1]$
(§2, Eq. (2.6); the scaling and the asymptotic regimes are on
[asymptotic preservation](/properties/asymptotic-preservation.md)). With the
page-local gravitational potential $\phi$, the hydrostatic states are $v=0$,
$\varepsilon^{1-\beta_{\mathrm{ms}}}\partial_xp(\rho)=\rho\,\partial_x\phi$, i.e.
$\rho=C\exp(\varepsilon^{\beta_{\mathrm{ms}}-1}\phi)$ for $\gamma=1$ (§2.1,
Eqs. (2.11)–(2.14)). Following Bouchut, a discrete hydrostatic steady state is
a grid function with zero momentum that satisfies a consistent discrete
equilibrium relation, and a scheme is well-balanced if it maps such states to
themselves (Definition 4.1). The construction (§4):

- **P-reconstruction** of the interface states, in the pressure (4.14):
  $\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho^-_{i+1/2})=\big[\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho_i)+\{\!\{\rho\}\!\}_{i+1/2}\big(\min(\phi_i,\phi_{i+1})-\phi_i\big)\big]_+$,
  and $\rho^+_{i+1/2}$ likewise from cell $i+1$, with $[X]_+=\max(0,X)$ keeping
  the density non-negative and $\{\!\{\rho\}\!\}_{i+1/2}=\tfrac12(\rho_i+\rho_{i+1})$;
- a Rusanov-type flux ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md))
  on these states, with the gravity source of cell $i$ split into upwinded
  interface contributions proportional to $p(\rho^-_{i+1/2})-p(\rho_i)$ and
  $p(\rho_i)-p(\rho^+_{i-1/2})$ (Eq. (4.6), after Audusse et al. and
  Natalini–Ribot–Twarogowska);
- in the mass update, which in their semi-implicit time discretization carries
  second-derivative terms, a central difference of $p$ and the averaged potential
  flux $\big[\{\!\{\rho\}\!\}_{i+1/2}(\phi_{i+1}-\phi_i)-\{\!\{\rho\}\!\}_{i-1/2}(\phi_i-\phi_{i-1})\big]/\Delta x^2$,
  which cancel exactly on the discrete equilibrium
  $\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho_{i+1})-\{\!\{\rho\}\!\}_{i+1/2}\phi_{i+1}=\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho_i)-\{\!\{\rho\}\!\}_{i+1/2}\phi_i$
  (Eq. (4.16)).

Theorem 4.3(ii) states well-balancing for this discrete state: there
$u^-_{i+1/2}=u^+_{i+1/2}$, the flux differences cancel the upwinded sources, and
the central terms of the mass update cancel. *(compiler check, not in the
sources: inserting (4.16) into (4.14) gives equal arguments of $[\cdot]_+$ for
$\rho^-_{i+1/2}$ and $\rho^+_{i+1/2}$, so the two reconstructed states indeed
coincide.)* The well-balancing must hold in the mass equation too, which a
hydrostatic reconstruction alone does not give. Arun et al. discard the
alternative E-reconstruction, in the enthalpy $\frac{\gamma}{\gamma-1}\rho^{\gamma-1}$,
because, citing Natalini, Ribot and Twarogowska, it gives a wrong diffusion
coefficient in the parabolic limit and so loses asymptotic preservation
(Remark 4.2).

**Evidence** (§5.2, Tables 1–2, Figs. 3–10). Isothermal and isentropic
equilibria with $\phi=x,\ x^2/2,\ \sin(2\pi x)$, $T=2$: for $\phi=x$, $\gamma=1$,
$\varepsilon=1$, the $L^1$ density errors are $2.6815\times10^{-6}$ ($N_x=100$)
and $2.7018\times10^{-8}$ ($N_x=1000$); for $\sin(2\pi x)$ about
$2.2\times10^{-4}$ and $2.1\times10^{-6}$ for all $\varepsilon$. A Gaussian
perturbation of amplitude $10^{-3}$ or $10^{-5}$ is resolved by the WB scheme
and not by the non-well-balanced (NWB) one at $\varepsilon=1$; at
$\varepsilon=10^{-3}$ the NWB scheme gives similar results, which the authors
explain by the limit equation sharing the steady state and by the NWB scheme
being asymptotic preserving; in long runs ($T=100$) the NWB scheme drifts at
$\varepsilon=1$ and oscillates at $\varepsilon=0.1,0.01$.

## Staggered grids: hydrostatic reconstruction with dry areas

[Goudon & Minjeaud (2024)](/sources/goudon-2024.md) carry hydrostatic reconstruction to an
explicit **staggered** finite-volume scheme for the barotropic Euler equations with a potential
source, $\partial_t\rho+\partial_x(\rho v)=0$, $\partial_t(\rho v)+\partial_x(\rho v^2+p(\rho))=-\rho\,\partial_xz$
(page-local potential or topography $z$; shallow water is $p=\rho^2/2$). Densities live on
primal cells, $\rho_{j+1/2}$, velocities at the nodes, $v_j$ (page-local: in this paragraph a
half index is a density cell, an integer index a velocity node). With the enthalpy-like
potential $\mathcal E(\rho)=p(\rho)/\rho+\int_0^\rho p(s)s^{-2}ds$ (page-local, not the vortex strength; $\mathcal E(\rho)=\rho$
for shallow water), the rest states including dry shores are
$v=0$, $\mathcal E(\rho)+z=\max(\eta_{\mathrm l},z)$ for a level $\eta_{\mathrm l}$ (page-local; Eq. (2)).
The construction (§2.2, Eqs. (14)–(18)):

- $z_j=\max(z_{j+1/2},z_{j-1/2})$ and reconstructed densities at the node,
  $\mathcal E(\rho^r_j)=[\mathcal E(\rho_{j+1/2})+z_{j+1/2}-z_j]_+$,
  $\mathcal E(\rho^\ell_j)=[\mathcal E(\rho_{j-1/2})+z_{j-1/2}-z_j]_+$, fed into the kinetic-type split
  mass fluxes and the upwinded momentum fluxes;
- the discrete source $S_j=p(\rho^r_j)-p(\rho_{j+1/2})-p(\rho^\ell_j)+p(\rho_{j-1/2})$, so that
  centred pressure plus source collapse to $p(\rho^r_j)-p(\rho^\ell_j)$.

At a discrete rest state $\mathcal E(\rho^r_j)=\mathcal E(\rho^\ell_j)=[\eta_{\mathrm l}-z_j]_+$, so
$\rho^r_j=\rho^\ell_j$, and all mass fluxes, momentum fluxes and pressure-plus-source vanish,
dry areas included; the positive part is what makes the dry case work (§2.2, proved). The scheme
is first-order consistent, also near dry cells when $\lim_{\rho\to0}p''\ne0$ (Remark 2.1), keeps
the density non-negative under a CFL condition, and satisfies a **semi-discrete** entropy
inequality; a fully discrete one is left open, the authors noting that for collocated
hydrostatic-reconstruction schemes it holds only up to a vanishing error or with added
viscosity (pp. 1272–1275; [entropy stability](/properties/entropy-stability.md)). For shallow
water far from dry areas, $S_j=\tfrac12(\rho_{j+1/2}+\rho_{j-1/2})\,\delta z_j-\tfrac12(\rho^r_j-\rho^\ell_j)\lvert\delta z_j\rvert$
with $\delta z_j=z_{j+1/2}-z_{j-1/2}$ (Eq. (19)).

The **second-order** version reconstructs $\rho$ and $\mathcal E(\rho)+z$ linearly
([MUSCL](/methods/muscl-hancock.md)), derives interface topographies from the two
reconstructions, and adds $+\tfrac12(\rho^r_j-\rho^\ell_j)\lvert\delta z_j\rvert$ to the source to remove
the first-order defect of Eq. (19) (Eq. (36)); for shallow water away from dry areas the source
then reduces to the centred $\tfrac12(\rho_{j+1/2}+\rho_{j-1/2})\,\delta z_j$. Rest states with and
without dry areas are still preserved, by limiter properties and a four-case argument (§2.3).
Moving-water steady states are not preserved: the error is proportional to the mesh size,
visible on the discharge (§3.3).

**Evidence** (§3): lake at rest without and with a dry zone for $\gamma\in\{1.4,2,3,4\}$ kept at
machine precision up to $T=1500$ and $T=1000$; convergence to the rest state from constant data;
LeVeque's perturbed lake at rest for $\gamma=1.4,2,3$; flow over a bump in four regimes and two
tests of Castro et al., with second-order $L^1$ convergence on the smooth ones; a wet/dry front
over a step; and the 2D Thacker paraboloid, observed order 1.8
([flow over a bump and lake at rest](/benchmarks/flow-over-a-bump.md)).

## Singular sources: an interface flux pair

For the 1D Euler equations with a Dirac-delta source at $x=0$,
$\partial_tu+\partial_xf(u)=\delta_{\mathrm D}(x)\,S$ with $S=\mathrm{diag}(k_1,k_2,k_3)f(u(0^\mp))$
taken upwind (page-local symbols), the equilibria are single **stationary waves**, jumps fixed at
$x=0$ with $f(u^-)+S=f(u^+)$, $u^\mp=u(0^\mp)$, $u^+$ on a subsonic or supersonic branch of a
stationary-wave curve of $u^-$ and the one-sided Mach numbers in admissible sets
([Yu, Liu & Feng (2023)](/sources/yu-2023.md), §2.1, Table 1; the admissibility criterion and the
classification of Riemann solutions are taken from the authors' companion preprint). They
define a scheme as well-balanced if it keeps every such stationary wave, placed on a cell
interface, unchanged (Def. 3.1; also "C-property").

- **Splitting fails.** Convection followed by an exact source step is not well-balanced for any
  $\Delta t>0$ (Thm. 3.1; [operator splitting](/methods/operator-splitting.md)).
- **Sufficient condition.** An unsplit conservative scheme with two one-sided fluxes at the
  source interface $x_{i_0+1/2}=0$, $\hat f_{i_0+1/2,-}$ for the left cell and $\hat f_{i_0+1/2,+}$
  for the right one, whose difference approximates the time-integrated source, is well-balanced if
  $\hat f_-(u^-,u^+)=f(u^-)$ and $\hat f_+(u^-,u^+)=f(u^+)$ for every admissible stationary pair,
  ordinary consistency holding elsewhere (Eqs. (3.18)–(3.23), Thm. 3.2).
- **Kröner–Thanh flux.** Two classical Riemann problems, each with one side mapped across the
  stationary wave, satisfy the condition (Thm. 4.1), but their fluxes are "unavailable" when a
  one-sided Mach number leaves its admissible set (Thm. 4.2, stated without proof), and the two
  fluxes may use different branches of the discontinuous stationary-wave curve. In choked cases
  (a sonic state next to the stationary wave) the scheme runs only with ad hoc corrections and
  oscillates or gives wrong solutions (§4.1, §5, Tests 4–7).
- **Solution-structure based solver.** Predicting the structure of the Riemann solution (five of
  seven types; the two limit types are left out) and computing the states $\tilde u^\mp$ (page-local) at
  $x/t=0^\mp$, by bisection on a pressure function for the non-choked type with a subsonic left
  state, gives a solver that is exact on any single stationary wave (Lemma 4.1), hence fluxes
  $f(\tilde u^\mp)$ that make the scheme well-balanced (Thm. 4.3), with both fluxes on the same
  branch by construction (§4.2).

**Evidence** (§5; third-order RKDG with a characteristic TVD limiter, local Lax–Friedrichs away
from the source, $\gamma=1.4$, $\Delta x=0.05$): the single stationary wave is kept by the Kröner–Thanh
and the present scheme, not by splitting; on Riemann problems of the seven types the present
scheme agrees with the exact solutions, including the choked ones where Kröner–Thanh fails. No
round-off magnitude, error table or convergence study is printed.

## Euler with gravity: WB from scale invariance

[Li et al. (2023a)](/sources/li-2023.md) (§4, after the methodology of Li and Gao) make a
characteristic-wise fifth-order [A-WENO](/methods/alternative-weno.md) scheme well-balanced for
the Euler equations with gravity, $S=(0,-\rho\,\partial_x\phi,-\rho v\,\partial_x\phi)$, and a
known hydrostatic equilibrium $v=0$, $\partial_xp_{\mathrm e}=-\rho_{\mathrm e}\partial_x\phi$
(page-local $\rho_{\mathrm e}$, $p_{\mathrm e}$; isothermal
$\rho_{\mathrm e}=\rho_0e^{-\phi/(RT_0)}$ or polytropic, Eqs. (57)–(60)). Three ingredients
(§4.1, Eqs. (61)–(64)):

1. the [Lax–Friedrichs](/methods/lax-friedrichs-flux.md) dissipation acts on the interpolated
   deviation $u-u_{\mathrm e}$ instead of $u$;
2. the momentum source is rewritten as $(\rho/\rho_{\mathrm e})\,\partial_xp_{\mathrm e}$, with
   $\partial_xp_{\mathrm e}$ discretized by the same interpolation and A-WENO derivative
   correction as the flux;
3. the interpolation operator is **scale invariant**, $\mathcal W[\lambda q]=\lambda\mathcal W[q]$
   (page-local operator $\mathcal W$; [scale invariance](/properties/scale-invariance.md)).

**Theorem 5** (§4.2, Eqs. (65)–(71), App. A; 1D): with these, the hydrostatic equilibrium is
preserved exactly. At equilibrium the Roe-averaged velocity vanishes and the local
characteristic variables are multiples of $p_{\mathrm e}$ by one interface constant
([characteristic decomposition](/methods/characteristic-decomposition.md)), so the sufficient
condition is the scale invariance of the interpolation applied to $p_{\mathrm e}$; the authors
call this "the crucial novel idea". It is the Euler-with-gravity counterpart of Wang & Don's
affine-invariance argument above, which Wang & Don state but do not test for Euler.

**Evidence** (§5, Tables 4–8, Figs. 9–14). Isothermal steady states in 1D ($\phi=x$, $t=2$,
$N_x=10$–$160$) and 2D ($\phi=x+y$, $t=1$): the well-balanced scheme stays at $O(10^{-16})$ in
double and $O(10^{-34})$ in quadruple precision, while the unmodified scheme starts at
$O(10^{-10})$ on 10 points and reaches only $O(10^{-19})$ at $N_x=160$ in quadruple precision.
Polytropic states (1D $\phi=3.15x$ to $t=10$; 2D Lane–Emden polytrope, $\gamma=2$, to $t=14.8$):
same picture. Perturbations of amplitude $10^{-10}$ to $10^{-12}$ are resolved only by the
well-balanced scheme, and in a Sod problem under gravity the unmodified scheme oscillates near
the shock and the contact. The accuracy is fifth order for both versions; with the polytropic
equilibrium the error on 32 points is $7.49\times10^{-4}$ and then coincides with the
unmodified scheme (order 12.55 on the first refinement), which the authors call
"super-convergence behavior like the spectral method" (Table 6).

## Known equilibria: evolving the deviation

[Kanbar et al. (2022)](/sources/kanbar-2022.md) make an
[unstaggered central scheme](/methods/unstaggered-central-scheme.md)
well-balanced for 2D ideal MHD with gravity by a "subtraction technique", after
Berberich, Chandrashekar and Klingenberg and their own Euler version. Given a
stationary solution $u_{\mathrm e}$ (analytic or numerical; page-local), the
scheme evolves the deviation $\delta u=u-u_{\mathrm e}$ by

$$\partial_t\delta u+\partial_x\big[f(\delta u+u_{\mathrm e})-f(u_{\mathrm e})\big]+\partial_y\big[g(\delta u+u_{\mathrm e})-g(u_{\mathrm e})\big]=S(\delta u),$$

which uses that the gravity source $S$ is linear in $u$ (§3, Eqs. (4)–(7)), and
recovers $u=\delta u+u_{\mathrm e}$. If $\delta u^n=0$, the predictor gives
$\delta u^{n+1/2}=0$ (proved, Eq. (17)), and the staggered and back-projected
updates stay zero (called "straight forward"), so the reference state is
preserved "up to machine precision". *(compiler check, not in the sources: the
cancellation uses that $f(u_{\mathrm e})$ is subtracted with the same discrete
operator, that the limited slopes of $u^n$ and $u_{\mathrm e}$ coincide when
$u^n=u_{\mathrm e}$, and that $S(0)=0$.)*

**Evidence** (§§5.3–5.5, Figs. 6–12): a stationary MHD vortex with
$u_{\mathrm e}$ the vortex itself ($32^2$–$128^2$), an isothermal stratified
atmosphere $\rho=\rho_0e^{-y/H}$, $p=p_0e^{-y/H}$ ($H=0.158$, $p_0=1.13$, $g=2.74$)
unchanged at $t=1.8$, and its magnetized version $B=(0,\mu_B,0)$ (page-local
field strength $\mu_B$); small and large piston perturbations of the atmosphere are compared
visually with Fuchs et al. No error norm is printed. The method is
well-balanced for the supplied $u_{\mathrm e}$; the concluding claim that it
"is capable of preserving any type of known equilibrium states" holds in that
sense only.

## Unstructured grids: well-balancing inside the Riemann solver

[Del Grosso et al. (2024)](/sources/delgrosso-2024.md) (HAL preprint; §3.5.1, §4.5, §4.6) build the
lake-at-rest property into the approximate Riemann solver of a first-order cell-centred finite
volume for 2D shallow water on polygonal grids, whose subface fluxes depend on a nodal velocity
$v_{\mathsf p}$ solved from a $2\times2$ system per node (construction on
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)). The interface source enters the
Godunov acoustic velocity of each subface through
$$\overline{gh\Delta b}=g\,\frac{h^-+h^+}2\,(b^+-b^-)$$
(Eq. (34)), chosen so that a lake-at-rest pair gives zero intermediate normal velocity. Then the
right side of the nodal system vanishes, $v_{\mathsf p}=0$, the intermediate states equal the
data, and the cell update cancels by the geometric identity $\sum l_fn_f=0$ around each cell
(Eq. (48)), so the multi-point scheme preserves the lake at rest "without further modification"
(§4.5). *(compiler check, not in the sources: with $p=\tfrac12gh^2$,
$p^+-p^-=g\tfrac{h^-+h^+}2(h^+-h^-)$, and at the lake at rest $h^+-h^-=-(b^+-b^-)$, so
$p^+-p^-+\overline{gh\Delta b}=0$ exactly.)* The same source term appears in the energy balance,
multiplied by the intermediate velocity, so that the entropy (energy) inequality holds with the
topography (§3.5.3).

The second-order version reconstructs $h$, $hv$ and $h+b$ by limited least squares, so the bottom
is $(h+b)$ minus $h$ cell by cell, and adds an in-cell correction
$g\tfrac12(\hat h_f+h)(\hat b_f-b)$ between the reconstructed face values $\hat h_f$, $\hat b_f$ and the
cell values (page-local; Eq. (60)) to keep the lake at rest; positivity and entropy stability of
the second-order scheme are stated, not proved (§4.6).

**Evidence** (§5.2, Figs. 5–6): the lake at rest over three mounds with $h+b=4$ on
$[0,40]^2$ m, $100\times100$ squares, kept to $t=200$ s "up to a machine error of order $10^{-15}$"
by the first-order multi-point, the second-order and the two-point schemes; a $10^{-3}$
perturbation of the free surface leaves the domain, the run stopping at $t\approx55.45$ s when the
residuals fall below $10^{-10}$. Only wet states and only zero-velocity steady states are targeted;
the authors call preservation of all steady states "fully well-balanced" and leave it aside (§2).

## Qualifications

- Chu et al. (2025b)'s claim that no existing method preserves general 2D steady states exactly
  (Remark 4.1) is a belief "to the best of our knowledge", made for their balance laws; the
  stationarity preservation of Active Flux recalled above (Calhoun et al. (2023)) preserves discrete
  representations of all stationary states of linear acoustics, a different system and a
  discrete notion, so the two statements do not collide as printed.
- Wang & Don's "well-balanced for any $\epsilon$" rests on two values of $\epsilon$; it follows
  from their Thm. 1 in exact arithmetic. The claim that characteristic-wise WB WENO is also
  well-balanced for the Euler equations under gravity without linearization is stated but not
  tested in their paper (Abstract, §3.3). The linearization is still required when the WENO
  operator acts on sums or products of functions, e.g. two-$\gamma$ multicomponent
  equilibria (Introduction).
- Balsara et al. write "We don't consider well-balancing in this paper" (§III) and later
  call the method well-balanced (§VIII.c); their evidence is visual agreement with the
  reference results of Dumbser & Balsara (2016), not a round-off equilibrium measurement.
- **Three kinds of evidence.** Wang & Don and Li et al. (2023a) measure round-off
  ($\approx10^{-33}$ to $10^{-34}$ in quadruple precision); Arun et al. state that the challenge is to resolve perturbations
  "up to machine precision" (§1) but report $L^1$ errors of $10^{-6}$ to $10^{-4}$ on 100
  cells; they interpolate the exact equilibrium onto the grid (§5.2.1); Kanbar et al. print
  no magnitude; Chu et al. (2022) print no lake-at-rest round-off test either, only the
  perturbation plots. *(compiler check, not in the sources: the errors fall by about 100 per
  tenfold refinement, i.e. second order; and for $\gamma=1$, $\varepsilon=1$, $\phi=x$ the
  interpolated state $\rho_i=e^{x_i}$ misses the discrete equilibrium (4.16) by
  $\rho_{i+1}-\rho_i-\{\!\{\rho\}\!\}_{i+1/2}(\phi_{i+1}-\phi_i)=-\tfrac1{12}e^{x_i}\Delta x^3+O(\Delta x^4)$,
  so the tests start from a state that Theorem 4.3(ii) does not cover, consistent with
  truncation-level rather than round-off errors.)*
- Arun et al.'s scheme is first order in space and time; the deviation formulation of
  Kanbar et al. is applied to a second-order scheme whose order is not measured.
- **Which equilibrium is preserved.** "Well-balanced" ranges in the bundle from the lake at rest
  or a supplied hydrostatic state (Wang & Don, Li et al. (2023a), Arun et al., Kanbar et al.) to
  every discrete state of constant equilibrium variables (Kurganov et al.) or of constant
  global-flux averages (Ciallella et al.); the last two are fully discrete notions, and
  Ciallella et al. say explicitly that theirs differ from the analytical equilibria. Goudon &
  Minjeaud preserve the lake at rest including dry areas, not moving water; Yu et al. preserve
  single stationary waves at a singular source, discontinuous equilibria by construction; Del
  Grosso et al. preserve the lake at rest on unstructured grids, wet states only. Claims
  are comparable only within one notion.
- Goudon & Minjeaud print the shallow-water relation as $\rho^r_j=\rho_{j+1/2}-[\delta z_j]_-$
  (p. 1269), with $[a]_-=\min(0,a)$. From their Eqs. (14)–(15) with $\mathcal E(\rho)=\rho$, the case
  $\delta z_j\le0$ gives $z_j=z_{j-1/2}$ and $\rho^r_j=\rho_{j+1/2}+\delta z_j$, so the sign should be
  $+$; their Eq. (19) holds with $+$ in both sign cases *(compiler check, not in the sources)*.
  They also print the second-order source correction with a minus on p. 1277 where Eq. (36) and
  the subsequent expansions carry a plus.
- Yu et al. (arXiv v1) print the singleton and empty cases of their stationary-wave curve
  (Property 2.1) on Mach ranges that are the complements of the admissible sets of their
  Table 1; their Algorithm 1 tests the left state with the ranges of Table 1 (Eq. (4.4)).

# Citations

- [Wang & Don (2022)](/sources/wang-2022-b.md) — Introduction, §2.3 (Thm. 1), §3.3 (Eqs. (26)–(30), Figs. 9–10).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §III, §VIII.a (Fig. 4), §VIII.c (Fig. 9) (accepted manuscript).
- [Arun et al. (2022)](/sources/arun-2022.md) — §1, §2.1, §4 (Def. 4.1, Eqs. (4.6), (4.14), (4.16), Thm. 4.3, Remark 4.2), §5.2 (Tables 1–2, Figs. 3–10) (arXiv v1).
- [Chu et al. (2022)](/sources/chu-2022.md) — §6.1 (Eqs. (6.1)–(6.4), Remark 6.1), §7.1 (Ex. 2, Fig. 7.3), §8.
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §3 (Eqs. (4)–(7), (17)), §§5.3–5.5, §6 (arXiv v1).
- [Li et al. (2023a)](/sources/li-2023.md) — §4 (Eqs. (57)–(71), Thm. 5), App. A, §5 (Tables 3–8, Figs. 9–14).
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §1, §4 (Theorem 4.1, Eqs. (4.13)–(4.16)), §7 (Table 7.1).
- [Ciallella et al. (2023)](/sources/ciallella-2023.md) — §1, §3 (Props. 3.1, 3.3, Remark 3.2), §5 (Table 1, §5.3) (author manuscript).
- [Calhoun et al. (2023)](/sources/calhoun-2023.md) — §1, §4.6 (Fig. 16), Conclusions (arXiv v2).
- [Goudon & Minjeaud (2024)](/sources/goudon-2024.md) — §2.1–2.3 (Eqs. (2), (14)–(19), (26)–(36), Remark 2.1), §3 (Figs. 3–24) (HAL wrap of the version of record).
- [Yu, Liu & Feng (2023)](/sources/yu-2023.md) — §2.1 (Table 1, Property 2.1), §3 (Def. 3.1, Thms. 3.1–3.2, Eqs. (3.18)–(3.23)), §4 (Thms. 4.1–4.3, Lemma 4.1, Alg. 1), §5 (arXiv v1).
- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §2, §3.5.1 (Eq. (34)), §3.5.3, §4.5 (Eq. (48)), §4.6 (Eq. (60)), §5.2 (Figs. 5–6) (HAL preprint).
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — Remark 3.1 (Eq. (3.4)), Remark 4.1, §5.2.1 (Ex. 6).
