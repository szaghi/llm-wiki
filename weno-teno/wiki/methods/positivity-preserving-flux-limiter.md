---
type: Method
title: "Positivity-preserving flux limiter (Hu–Adams–Shu)"
description: "A positivity-preserving flux limiter blends, interface by interface, a high-order flux with a first-order admissible flux so that the forward-Euler update stays admissible; the page gives Wong et al.'s HLLC-based construction for the five-equation model, Xiong–Qiu–Xu's parametrized limiter on the Runge–Kutta-combined flux of a Hermite WENO scheme, and the finite-difference papers relying on it."
status: established
aliases: [PP flux limiter, Hu–Adams–Shu limiter, positivity-preserving limiter, positivity- and boundedness-preserving flux limiter, parametrized flux limiter]
tags: [positivity, bound-preserving, limiting, finite-difference, numerical-flux]
timestamp: 2026-10-23T10:00:00Z
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
sources of this bundle; two sources write a limiter of this kind out:
[Wong et al. (2021)](/sources/wong-2021.md), for HLLC and the
five-equation model, and [Fan et al. (2023)](/sources/fan-2023.md), for
the parametrized limiter of Xiong, Qiu and Xu in two dimensions. Wong et al. cite Hu et al. among the limiters applied
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
- **Scale-invariant MR-AWENO** ([Li et al. (2023)](/sources/li-2023.md),
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
- [Li et al. (2023)](/sources/li-2023.md) — §3.3, §3.6 (limiter used; pressure stage active at the jet front).
