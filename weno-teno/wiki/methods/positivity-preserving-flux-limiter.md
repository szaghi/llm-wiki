---
type: Method
title: "Positivity-preserving flux limiter (Hu–Adams–Shu)"
description: "A positivity-preserving flux limiter blends, interface by interface, a high-order flux with a first-order admissible flux so that the forward-Euler update stays admissible; the page gives Wong et al.'s HLLC construction, the Hu–Adams–Shu form at every Runge–Kutta stage, a lower-bound Active Flux variant, Xiong–Qiu–Xu's parametrized limiter and the schemes relying on it."
status: established
aliases: [PP flux limiter, Hu–Adams–Shu limiter, positivity-preserving limiter, positivity- and boundedness-preserving flux limiter, parametrized flux limiter]
tags: [positivity, bound-preserving, limiting, finite-difference, numerical-flux]
timestamp: 2026-10-23T20:30:00Z
---

# Positivity-preserving flux limiter (Hu–Adams–Shu)

A **positivity-preserving flux limiter** replaces, at every interface
$x_{i+1/2}$, the high-order numerical flux $\hat f^{\mathrm{HO}}_{i+1/2}$ of
a conservative scheme by the convex combination
$$\hat f_{i+1/2}=\theta_{i+1/2}\,\hat f^{\mathrm{HO}}_{i+1/2}+\big(1-\theta_{i+1/2}\big)\,\hat f^{\mathrm{LO}}_{i+1/2},\qquad 0\le\theta_{i+1/2}\le1,$$
where $\hat f^{\mathrm{LO}}$ is a first-order flux whose scheme is
[bound-preserving](/properties/bound-preservation.md) under a CFL condition,
and $\theta_{i+1/2}$ (page-local; the flux analogue of the registry's
scaling factor $\theta$) is the largest value for which the forward-Euler
update stays in the admissible set $G$. One coefficient per interface,
shared by the two cells it bounds, keeps the scheme conservative. The
limiter acts on fluxes, not on a polynomial, so it fits finite-difference
schemes, where no cell polynomial exists for the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) to
scale. The idea goes back to Hu, Adams and Shu (2013), as recalled by the
sources of this bundle; four sources write a limiter of this kind out:
[Wong et al. (2021)](/sources/wong-2021.md), for HLLC and the
five-equation model, [Fan et al. (2023)](/sources/fan-2023.md), for
the parametrized limiter of Xiong, Qiu and Xu in two dimensions,
[Chen & Chen (2026)](/sources/chen-2026.md), for the Hu–Adams–Shu form in a
TENO finite-difference scheme, and [Kiechle, Chudzik & Helzel (2025)](/sources/kiechle-2025.md),
for the fully discrete Active Flux method. Wong et al. cite Hu et al. among the limiters applied
directly to fluxes (§1) and for the directional split (Eq. (59)), but do
not present their limiter as an extension of it.

## Construction (Wong et al. 2021)

**Half-cell decomposition of the update.** [Wong et al. (2021)](/sources/wong-2021.md)
(§5.2, Eqs. (102)–(103), with the directional split of §3.3, Eq. (59), taken
from Hu et al.) write the 2D forward-Euler step of the conservative scheme
as
$$u^{n+1}_{ij}=\sigma_x\Big(\tfrac12u^{x,(\mathrm l)}_{ij}+\tfrac12u^{x,(\mathrm r)}_{ij}\Big)+\sigma_y\Big(\tfrac12u^{y,(\mathrm l)}_{ij}+\tfrac12u^{y,(\mathrm r)}_{ij}\Big),\qquad \sigma_x=\frac{\Lambda_x}{\Lambda_x+\Lambda_y},\quad\Lambda_x=\frac{\max(\lvert v_1\rvert+c)}{\Delta x},$$
with the half-cell states (page-local, written here for a conservation law)
$$u^{x,(\mathrm l)}_{ij}=u^n_{ij}+\frac{2\Delta t}{\sigma_x\Delta x}\Big(\hat f_{i-1/2,j}-f(u_{ij})\Big),\qquad
u^{x,(\mathrm r)}_{ij}=u^n_{ij}-\frac{2\Delta t}{\sigma_x\Delta x}\Big(\hat f_{i+1/2,j}-f(u_{ij})\Big),$$
and $\sigma_y$, $\Lambda_y$, $u^{y,(\mathrm l,\mathrm r)}$ alike ($\sigma_{x,y}$, $\Lambda_{x,y}$
page-local; the source writes $\tau_x$ for $\Lambda_x$). Adding the two
half-cell states recovers the flux difference, and the physical flux
$f(u_{ij})$ cancels *(compiler check, not in the sources: $\tfrac12(u^{(\mathrm l)}+u^{(\mathrm r)})=u^n-\frac{\Delta t}{\sigma_x\Delta x}(\hat f_{i+1/2}-\hat f_{i-1/2})$)*.
Because $G$ is convex, $u^{n+1}\in G$ whenever the four half-cell states are
in $G$. The time step is $\Delta t=\nu/(\Lambda_x+\Lambda_y)$ (Eq. (60)), so that
$\Delta t/(\sigma_x\Delta x)=\nu/\max(\lvert v_1\rvert+c)$ ($\nu$ the CFL
number). Each half-cell state depends on a single interface flux, which is
what makes an interface-local coefficient possible.

**Coefficient.** The flux at $x_{i+1/2}$ enters $u^{(\mathrm r)}_i$ and
$u^{(\mathrm l)}_{i+1}$. For a constraint quantity $g(u)\ge\epsilon_g$
($\epsilon_g$ a floor, page-local), Wong et al. compute a candidate
coefficient from each of the two half-cell states with a three-case rule
(Algorithms 4–6): $\theta=0$ if the first-order half-cell state already
violates the floor; otherwise, if the high-order one violates it, $\theta$
solves $(1-\theta)\,g(u^{\mathrm{LO}})+\theta\,g(u^{\mathrm{HO}})=\epsilon_g$;
otherwise $\theta=1$. The interface takes the minimum of the two candidates,
$\theta_{i+1/2}=\min(\theta^+,\theta^-)$, and the flux is blended. The
authors state that the intention is to blend $(\hat f-f(u_i))$, in which the
nodal flux cancels (§5.2).

**Successive constraints.** For the
[five-equation model](/definitions/five-equation-model.md) the blending is
done three times in sequence, each stage starting from the flux of the
previous one: partial densities $\phi_k\rho_k\ge\epsilon$, volume
fraction $\epsilon\le\phi_1\le1-\epsilon$, and
$\rho e-\bar p_\infty\ge\epsilon$, a quantity that is concave in the
conserved variables when the phase with $p_{\infty,k}=0$ has the smaller
$\gamma_k$ (Lemma 1, Theorem 1; $\phi_k$, $\rho_k$ are the volume fractions
and phasic densities of registry §10, $\bar p_\infty$ the mixture stiffness of the
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
page, page-local). For the concave quantity the convex combination is
justified by Jensen's inequality, as the algorithms state. Floors are $10^{-10}$, $10^{-10}$ and
$10^{-8}$; a hard switch to the first-order flux acts below $10^{-11}$,
$10^{-11}$ and $10^{-9}$ to absorb round-off (§5.1–§5.2). The user must pick
floors below the minima of the initial fields.

**The first-order flux.** The limiter needs a first-order scheme that is
admissible on its own. Wong et al. prove that the first-order
[HLLC](/methods/hll-riemann-solvers.md) scheme with Einfeldt wave speeds,
Batten's contact speed, and the contact speed as the interface advection
velocity of $\phi_1$, is positivity- and boundedness-preserving for
stiffened-gas mixtures under $\nu\le0.5$ in the directional split above
(§3.3, Eqs. (46)–(70)): the needed bound
$s^-<v_{1}-(p+\bar p_\infty)/\sqrt{2\rho(\rho e-\bar p_\infty)}$ on the left
wave speed is implied by Einfeldt's $s^-\le v_1-c$ (Eq. (57)). The flux
limiter then makes the high-order update admissible under the same
$\nu\le0.5$, and [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stages
inherit it as convex combinations of forward-Euler steps (§5.3).

**Two limiters, not one.** In Wong et al.'s
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
the Riemann solver acts on interpolated midpoint states, which must
themselves be admissible for the HLLC flux to be defined. A first
*interpolation limiter* (Algorithms 1–3) therefore blends each interpolated
midpoint state convexly with the adjacent node state, through the same
three successive constraints; the *flux limiter* then acts on the implied
interface fluxes of the compact differencing (§5.1–§5.2). The interpolation
limiter is a convex blend of the kind of the scaling limiter, which Wong et
al. cite as motivation (§1), but toward a node value, not toward a cell
average.

**The interpolation limiter alone, in a finite-volume scheme.**
[Zhang et al. (2024a)](/sources/zhang-2024.md) (§3.3, Eqs. (47)–(49),
Algorithm 1) use only the first of Wong et al.'s two limiters, in the
finite-volume five-equation solver of ALPACA with HLLC fluxes. After the
reconstruction of the primitive variables (incremental-stencil WENO, with
THINC for the volume fraction and phase densities in interface cells;
[THINC](/methods/thinc-reconstruction.md),
[incremental-stencil WENO](/methods/incremental-stencil-weno.md)), each
face state $\tilde q$ is blended with the cell value $q_i$,
$\tilde q^*=(1-\theta)q_i+\theta\tilde q$, in three successive loops: the
partial densities $\phi_k\rho_k$ and the volume fractions $\phi_k$, each with the floor
$10^{-11}$, and then $\rho c^2$ with the floor $10^{-9}$, $\theta=0$ when
the cell value itself is below the floor and otherwise the root of the
linear interpolation to the floor ($10^{-8}$ is added to the initial
fields). The whole primitive vector is blended, so a limited face drops to
first order. They measure how often the limiter acts in a Mach 10
shock-induced bubble collapse at $1920\times960$: above 1 % of the cells
with WENO-JS5 as base reconstruction, much less with TENO5 and least with
the incremental-stencil WENO, never above 0.04 %, which is why they choose
the last (§4.8, Fig. 16b). No flux limiter follows, and no positivity
theorem is stated for the scheme.

## The Hu–Adams–Shu form at every Runge–Kutta stage (Chen & Chen 2026)

[Chen & Chen (2026)](/sources/chen-2026.md) (§2.4, Eqs. (27)–(32)) write the
limiter out for their [adaptive TENO](/methods/adaptive-teno.md)
finite-difference scheme with Lax–Friedrichs flux splitting and a sharp-interface
[immersed boundary](/methods/immersed-boundary-method.md). Each stage of the
five-stage third-order SSP Runge–Kutta method is written as a forward-Euler step
with $\lambda_s=\Delta t\sum_k\beta_{sk}/\Delta x$ ($\beta_{sk}$ the Shu–Osher
coefficients, page-local), and the step is split into two half-cell states,
$$u^{s+1}_i=\tfrac12u^-_i+\tfrac12u^+_i,\qquad u^-_i=u^s_i+2\lambda_s\hat f_{i-1/2},\qquad u^+_i=u^s_i-2\lambda_s\hat f_{i+1/2}$$
(page-local $u^\pm_i$), the 1D form of Wong et al.'s split above. The low-order flux is
the global [Lax–Friedrichs](/methods/lax-friedrichs-flux.md) flux with
$a=\max(\lvert v\rvert+c)$, positivity preserving for CFL numbers below $\tfrac12$,
as the authors recall from Zhang & Shu. The coefficients are found in two passes:
for density, $\theta^+_{i+1/2}$ solves
$(1-\theta)\rho(u^{\mathrm{LF},+}_i)+\theta\rho(u^+_i)=\epsilon_\rho$ if $\rho(u^+_i)<\epsilon_\rho$,
$\theta^-_{i+1/2}$ the same on $u^-_{i+1}$, and $\theta_{i+1/2}=\min(\theta^+,\theta^-)$;
then the same for pressure on the density-limited flux, with floors
$\epsilon_\rho=\min(10^{-13},\min\rho^0)$, $\epsilon_p=\min(10^{-13},\min p^0)$. The
limiter runs at every stage. The pressure pass relies on the concavity of $p$ in the
conserved variables, which the abstract states and their "Theorem 1", cited without
proof, prints as "convexity" (§2.4); the conclusion they draw, positivity under convex
combinations and a convex admissible set, needs concavity. No CFL number is printed for
any test. The positivity claim of the abstract, "at every grid point for all time",
also involves the immersed-boundary interpolation: the bilinear interpolation at body
intercepts is two successive convex combinations and keeps positivity, a general
bilinear fit near the wall is blended by bisection with it when it fails, and the
ghost values come from a mirror extrapolation, not a convex combination, with the rules
for ghost density and pressure not printed (§2.5, Eqs. (35)–(40)). With the adaptive
cut-off $C_T\in[10^{-9},10^{-1}]$ the limiter is rarely activated on a Mach 3
cylinder; with smaller cut-off ranges its activations spread from the bow shock into the
wake (§3.1, Fig. 8, maps only).

## Active Flux: lower bound from a four-way split (Kiechle et al. 2025)

[Kiechle, Chudzik & Helzel (2025)](/sources/kiechle-2025.md) (§3.2, Eqs.
(12)–(24), Remark 3.1) build a limiter of this kind for the fully discrete
[Active Flux](/methods/active-flux.md) method, whose fluxes are Simpson averages
of point values in space and time, for a scalar quantity $u\ge0$ in 2D. The
low-order flux is global Lax–Friedrichs, $\hat f^{\mathrm{LF}}_{i-1/2,j}=\tfrac12\big(f(\bar u_{i-1,j})+f(\bar u_{i,j})-a^{(1)}(\bar u_{i,j}-\bar u_{i-1,j})\big)$,
$a^{(1)}=\max\lvert f'\rvert$. The update is split into four one-sided states,
$$\bar u^{n+1}_{i,j}=\tfrac{\mathsf s_x}2u^-_i+\tfrac{\mathsf s_x}2u^+_i+\tfrac{\mathsf s_y}2u^-_j+\tfrac{\mathsf s_y}2u^+_j,\qquad
u^\mp_i=\bar u^n_{i,j}\pm\frac{2\Delta t}{\mathsf s_x\Delta x}\hat f_{i\mp1/2,j},$$
$\mathsf s_x+\mathsf s_y=1$ (page-local $\mathsf s_{x,y}$, $u^\pm_{i,j}$; the source's
$\alpha_x$, $\alpha_y$, $Q^\pm$), so the average is nonnegative when the four states
are. With $\mathsf s_x=\mathsf s_y=\tfrac12$ the Lax–Friedrichs states are nonnegative
for CFL numbers up to $\tfrac14$, half the $\tfrac12$ of the plain Lax–Friedrichs scheme.
Each face of a cell gives a candidate, $\theta^-_{i-1/2,j}=(\epsilon-u^{\mathrm{LF},-}_i)/(u^-_i-u^{\mathrm{LF},-}_i)$
if $u^-_i<\epsilon$ and 1 otherwise, the other cell gives $\theta^+$ through its right
face, and $\theta_{i-1/2,j}=\min(\theta^-,\theta^+)$, with
$\epsilon=\max\{10^{-13},\min u_0\}$ (Eqs. (22)–(24)); the implementation subtracts
$10^{-16}$ and clips to $[0,1]$ against round-off (Remark 3.1). Only the lower bound is
enforced: oscillations near the upper value 1 of their advected indicator function
remain (Fig. 4). The authors cite Zhang & Shu and Hu, Adams & Shu for the idea, state,
after Hu et al.'s finite-volume result, that the limiter does not reduce the order on
smooth solutions, and confirm it on the Vlasov–Poisson two-stream instability, where the
limited scheme at CFL $0.25$ converges with order $2.9722$ against $2.9730$ unlimited at
CFL $0.5$ (Table 1). The limiter needs no bound-preserving reconstruction, which avoids
the cell-wise minima and maxima of the reconstruction (§3.1.1; no timing). They compare
it with the two-sided flux limiter of the bound-preserving
[PAMPA scheme](/methods/pampa-scheme.md), which needs admissible point values and keeps
both bounds (Remark 3.2).

## Parametrized limiter on the Runge–Kutta flux (Fan et al. 2023)

[Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) (Remark 2.3,
Appendix, Eqs. (A.4)–(A.10), Algorithm A.1) give a 2D finite-difference
implementation of the parametrized positivity-preserving flux limiter of
Xiong, Qiu and Xu (as recalled) for their fifth-order
[Hermite WENO](/methods/hermite-weno.md) scheme. It is applied once per
time step, at the final stage, to the convex combination of the stage
fluxes that SSP-RK3 implies, written as
$u^{n+1}_{ij}=u^n_{ij}-\frac{\Delta t}{\Delta x}(\hat f^{\mathrm{RK}}_{i+1/2,j}-\hat f^{\mathrm{RK}}_{i-1/2,j})-\frac{\Delta t}{\Delta y}(\hat g^{\mathrm{RK}}_{i,j+1/2}-\hat g^{\mathrm{RK}}_{i,j-1/2})$
(page-local $\hat f^{\mathrm{RK}}$, $\hat g^{\mathrm{RK}}$). Each interface
flux is replaced by
$\theta(\hat f^{\mathrm{RK}}-\hat f^{\mathrm{LF}})+\hat f^{\mathrm{LF}}$, with
$\hat f^{\mathrm{LF}}$ the first-order
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) with
$a=\lVert\lvert v_1\rvert+c\rVert_\infty$, whose first-order update is
positive. The floors are $\epsilon_\rho=\min\{\hat\rho^{n+1}_{ij},10^{-13}\}$
and likewise for the pressure, with $\hat\rho^{n+1}$ the first-order
update. Step I turns the density floor, which is linear in the four
$\theta$'s of a cell, into upper bounds on them (left, right, down, up)
from the signs of the four flux differences. Step II tests the 16
vertices of the box of these bounds for the pressure floor, scales any
failing vertex toward the origin by the root of a quadratic, and keeps
the largest box whose vertices pass. Step III takes, at each interface,
the smaller of the bounds of its two cells. The procedure is sufficient
only, so it may act where no negative state would appear, and its
preservation of high order "relies on numerical verification" (as
recalled). The authors choose it over polynomial scaling because it
"allows larger time steps in practice and is more convenient for FD
schemes" (§1, Remark 2.3). It is needed, for their scheme and for the
WENO-ZQ comparison, only on the Mach 2000 jet (active in 0.0146 % of the
cells) and on a Mach 10 reflection–diffraction problem (0.0012 %); the
1D and 2D Sedov, double-rarefaction and Leblanc problems run without it
(Ex. 3.5–3.7, 3.10–3.12, Remark 3.2).

## Use in the corpus

Several finite-difference schemes of the bundle are not
positivity-preserving by themselves and run their extreme cases with the
Hu–Adams–Shu limiter, without describing it:

- **TENO-AA** ([Fu (2021)](/sources/fu-2021.md), §5.7): double rarefaction,
  [Leblanc](/benchmarks/leblanc-shock-tube.md),
  [Sedov](/benchmarks/sedov-blast-wave.md), and Mach 80 and Mach 2000
  [jets](/benchmarks/high-mach-astrophysical-jet.md), with a local
  Lax–Friedrichs flux; positivity is achieved "with the assistant of a
  positivity-preserving flux limiter", and the reconstruction alone is not
  claimed positivity-preserving (Abstract).
- **TENO-THINC** ([Takagi et al. (2022)](/sources/takagi-2022.md), §4.9):
  Mach 80 and Mach 2000 jets on $800\times400$ points at CFL 0.35.
- **Affine-invariant WENO** ([Wang & Don (2022)](/sources/wang-2022-b.md),
  §3.2.4, Fig. 8): "not positivity preserving in general"; on the Mach 2000
  jet the limiter (Hu–Adams–Shu, and Li et al. 2018, as cited) activates
  only near the jet front and the two inlet corners at the final time.
- **Improved TENO-THINC** ([Liang et al. (2022)](/sources/liang-2022.md),
  §4.11): the Hu–Adams–Shu limiter for the Mach 80 and Mach 2000 jets on
  $800\times400$ points at CFL 0.35; every compared scheme is stable with
  it ([TENO-THINC](/methods/teno-thinc.md)).
- **Scale-invariant MR-AWENO** ([Li et al. (2023a)](/sources/li-2023.md),
  §3.3, §3.6): the limiter of Hu–Adams–Shu and of Li, Don, Wang and Gao
  (as cited) on the Sedov blast wave, with ambient pressure
  $4\times10^{-13}$, and on the Mach 2000 jet, where only its pressure
  stage is active, at the jet front, and the density stays positive
  ([multi-resolution WENO](/methods/multi-resolution-weno.md)).
- **PP-WCNS-IS** ([Wong et al. (2021)](/sources/wong-2021.md), §6.6–§6.7):
  on the Mach 10 shock–water-column interaction the unlimited scheme fails
  with an imaginary sound speed at the incident shock, inside the column
  and in the vortices, while the limited scheme runs and keeps $\phi_1$
  within its floors; the Mach 100 water jet, a multiphase version of the
  Mach 2000 jet, runs with both schemes
  ([shock–water-column interaction](/benchmarks/shock-water-column.md)).

- **WENO5IS-THINC** ([Zhang et al. (2024a)](/sources/zhang-2024.md),
  §4.5–4.8): the interpolation limiter above, without a flux limiter, on
  Mach 2.4, 6 and 10 shock–water-cylinder interactions and a 100 GPa
  bubble collapse ([shock–water-column interaction](/benchmarks/shock-water-column.md),
  [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).

## Relation to other limiters

- **Convex limiting and FCT.** The blend of a high-order and a
  bound-preserving low-order flux with a factor chosen from target bounds is
  the structure of [convex limiting](/methods/convex-limiting.md); there the
  low-order weight is written $\alpha=1-\theta$. Wong et al.'s coefficients
  are computed from half-cell states and floors on $g(u)$ (positivity and
  boundedness), not from local minimum and maximum bounds, so the limiter is
  inactive away from near-vacuum or near-pure-phase states *(compiler
  check, not in the sources: $\theta=1$ unless a high-order half-cell state
  falls below a floor, Algorithms 4–6)*. [Wu & Shu (2023)](/sources/wu-2023-b.md)
  recall the Xu and Hu–Adams–Shu limiters, together with the Guermond–Popov
  framework, as background of bound-preserving schemes (§1).
- **No first-order flux for viscous terms.** [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md)
  state that the positivity-preserving finite-difference methods for the
  Euler equations (Hu–Adams–Shu, Xiong–Qiu–Xu, Seal et al., Guo et al., as
  cited) rely on a first-order positivity-preserving scheme, and that the
  compressible Navier–Stokes diffusion operator has no standard one, "the
  key difficulty"; they therefore use a positivity-preserving splitting of
  the total flux and a scaling limiter instead of a flux limiter (§1.1;
  [positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md)).
- **Flux limiters for convection–diffusion DG.** [Du & Yang (2022)](/sources/du-2022-b.md)
  name flux limiters as "another direction" for high-order
  maximum-principle- and positivity-preserving schemes for
  convection–diffusion equations, citing Xiong, Qiu & Xu and Guo & Yang
  "as an incomplete list" (§1). Their own reacting-flow DG does not use
  one: it takes the cell-average route with a Lax–Friedrichs penalty on the
  total flux and a scaling limiter
  ([bound preservation](/properties/bound-preservation.md)).
- **Scaling limiter.** The [Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md)
  acts on the reconstructed polynomial of a cell before the flux is
  computed; the flux limiter acts after it, on the flux. Both reduce to
  convex combinations with an admissible first-order object.
- **Accuracy-driven flux blending.** Two sources use the same algebraic
  form $\hat f^{\mathrm{LO}}+\theta(\hat f^{\mathrm{HO}}-\hat f^{\mathrm{LO}})$
  with a factor chosen for other ends: [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) blend a
  low-order interface flux with the high-order one through a smooth
  [discontinuity indicator](/definitions/troubled-cell-indicator.md) near
  material interfaces (Eqs. (15)–(16)), and MFC blends a first-order and a
  WENO Riemann flux with a TVD limiter of a volume-fraction ratio
  ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md), §4.2.2,
  Eq. (34); [MFC](/software/mfc.md),
  [TVD limiters](/definitions/total-variation-diminishing.md)). Neither
  makes a positivity claim.

## Qualifications

- **Guarantees under unstated or reduced time steps.** Chen & Chen (2026) state no
  time-step result beyond the recalled Lax–Friedrichs condition, print no CFL number,
  and print the Lax–Friedrichs flux with the states of $t^n$ although the limiter runs
  at every stage (Eq. (27)). Kiechle et al.'s guarantee needs CFL $\le\tfrac14$, while
  their unlimited runs use up to $0.75$; they state that limited and unlimited methods
  coincide "as long as no negative cell averages arise" (§4.4.2). By Eqs. (22)–(24) the
  coefficient is 1 exactly when all one-sided states are at least $\epsilon$, a
  condition on the split states rather than on the averages *(compiler check, not in
  the sources)*.
- **No guarantee is stated where the limiter is only used.** Fu (2021),
  Takagi et al. (2022), Wang & Don (2022), Liang et al. (2022) and Li et
  al. (2023) print no limiter formulas, no
  low-order flux of the limiter and no statement of the CFL condition it
  needs; their positivity claims are therefore numerical.
- **Printed slips in Fan et al.'s appendix.** The density box of Step II
  is printed $[0,\Lambda^\rho_L]\times[0,\Lambda^\rho_R]\times[0,\Lambda^\rho_L]\times[0,\Lambda^\rho_D]$,
  while its vertices are built with the down and up bounds; the third and
  fourth factors are meant to be the down and up bounds. Line 15 of
  Algorithm A.1 tests "$f(k)=1$" for the flag set on line 12. Their
  isentropic-vortex runs without the limiter report negative minimum
  pressures on coarse meshes (Table 3.3), so "robust without limiters"
  holds for their shock tests, not for that case.
- **Strict-interior bounds.** Wong et al.'s bounds are floors
  ($\epsilon\le\phi_1\le1-\epsilon$, $\rho e-\bar p_\infty\ge\epsilon$),
  not the closed admissible set, and the hard switches are tolerances, not
  part of the proof.
- **Scope of the convexity proof.** The concavity of $\rho e-\bar p_\infty$,
  and with it the convexity of $G$, holds only if one phase has
  $p_{\infty,k}=0$ and the smaller $\gamma_k$; Wong et al. show that it cannot be
  concave otherwise (Lemma 1), and call the assumption mild for water–air
  pairs (§2).

- **Zhang et al.'s sound-speed quantity.** The text limits
  "$\rho c^2=\frac{p+P_\infty}{\gamma-1}$" (their $P_\infty$ the mixture
  stiffened-gas constant, written $p_\infty$ below, page-local); with their
  frozen sound speed $c^2=\gamma(p+p_\infty)/\rho$ (Eq. (16)),
  $\rho c^2=\gamma(p+p_\infty)$. Both are positive exactly when
  $p+p_\infty>0$, so the constraint is the same, but the identity as
  printed is not *(compiler check, not in the sources)*.

# Citations

- [Wong et al. (2021)](/sources/wong-2021.md) — arXiv v1: §2 (Lemma 1, Theorem 1); §3.3 (Eqs. (46)–(70)); §5.1 (Algorithms 1–3); §5.2 (Eqs. (102)–(107), Algorithms 4–6); §5.3; §6.6–§6.7.
- [Fu (2021)](/sources/fu-2021.md) — arXiv v1: Abstract; §5.7 (limiter used for extreme cases).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.9 (limiter used for the jets).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.4, Fig. 8 (limiter needed; activation region).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §1 (flux limiters recalled).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — Eqs. (15)–(16) (indicator-blended fluxes).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — arXiv v1: §4.2.2, Eq. (34) (TVD flux blending in MFC).
- [Du & Yang (2022)](/sources/du-2022-b.md) — §1 (flux limiters for convection–diffusion recalled).
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — §1; Remark 2.3; Ex. 3.5–3.12, Remark 3.2; Appendix, Eqs. (A.4)–(A.10), Algorithm A.1.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §1.1 (first-order fluxes for Euler, none for diffusion).
- [Liang et al. (2022)](/sources/liang-2022.md) — §4.11 (limiter used for the jets).
- [Li et al. (2023a)](/sources/li-2023.md) — §3.3, §3.6 (limiter used; pressure stage active at the jet front).
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §2.3, Eq. (16); §3.3, Eqs. (47)–(49), Algorithm 1; §4.5–4.8, Fig. 16b.
- [Chen & Chen (2026)](/sources/chen-2026.md) — Abstract; §2.4, Eqs. (27)–(34); §2.5, Eqs. (35)–(40); §3.1, Fig. 8.
- [Kiechle, Chudzik & Helzel (2025)](/sources/kiechle-2025.md) — §3.1.1; §3.2, Eqs. (12)–(24), Remarks 3.1–3.2, Fig. 4; §4.3; §4.4.1–4.4.2, Table 1.
