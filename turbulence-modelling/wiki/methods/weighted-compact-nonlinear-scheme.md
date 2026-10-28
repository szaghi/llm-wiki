---
type: Method
title: "Weighted compact nonlinear schemes"
description: "The weighted compact nonlinear scheme (WCNS) differences numerical fluxes at cell edges, computed by a Riemann flux from nonlinearly interpolated interface states; the page gives the explicit and the tri-diagonal compact interpolations, the fourth- and eighth-order flux differences, and how the nonlinear weights set its dissipation in implicit LES and hybrid RANS/LES."
status: established
aliases: [WCNS, weighted compact nonlinear scheme, WCNS-E, WCNS-T, WCNS-L, WCNS-Z, nonlinear compact interpolation]
tags: [numerical-dissipation, implicit-les, compressible, hybrid-rans-les]
timestamp: 2026-10-28T07:03:00Z
---

# Weighted compact nonlinear schemes

The **weighted compact nonlinear scheme (WCNS)**, of Deng & Zhang as the
sources cite it, is a high-order finite-difference shock-capturing scheme
built from three components: (i) a high-order **flux difference** that
differentiates numerical fluxes defined at cell edges (and, in one form,
physical fluxes at nodes); (ii) a **numerical flux**, an approximate
Riemann solver (Roe in all three sources) evaluated from left and right
interface states; (iii) a **weighted nonlinear interpolation** that
produces those interface states from the nodal values, with WENO-type
weights. Unlike a WENO finite-difference scheme, which reconstructs split
fluxes, the WCNS interpolates the variables and leaves the upwinding to the
Riemann flux ([Ma et al. 2022](/sources/ma-2022.md), §2.1;
[Wu et al. 2023](/sources/wu-2023-b.md), §2.2.1;
[Wu et al. 2024](/sources/wu-2024.md), §2.3). In this bundle the
scheme appears in two roles: as the discretization of
[implicit LES](/definitions/implicit-les.md), where its dissipation is the
subgrid dissipation (Ma et al.), and as the low-dissipation convective
scheme under explicit and hybrid closures (Wu et al. 2023, 2024), in the
CARDC solver [PHengLEI](/software/phenglei.md). Its relation to
WENO and TENO is on [WENO and hybrid schemes](/methods/weno-scheme.md),
whose WCNS section this page extends.

Notation (page-local unless registered): the model equation
$\partial_tU+\partial_xE=0$ on nodes $x_j=jh$ ($h$ the spacing, registry
§6), semi-discretized as $(\partial_tU)_j=-E'_j$; $E^*_{j+1/2}$ the
numerical flux (registry $f^*$) from interface states
$U^{\mathrm L}_{j+1/2}$, $U^{\mathrm R}_{j+1/2}$; $u_j$ one component of
the interpolated variable and $u_{j+1/2}$ its interface value;
$d_k$ the optimal (linear) weights, $a_k$ and $\mathsf w_k$ the
unnormalized and normalized nonlinear weights, $\mathrm{IS}_k$ the
smoothness indicators (registry §11); $\alpha_{\mathrm W}$, $b_{\mathrm W}$
the flux-difference coefficients (not the DG blending factor $\alpha$);
$\epsilon_{\mathrm Z}$ the regularizer of the weights (registry §11).

## Flux differences

**Eighth order, edge and node fluxes** (Ma et al. 2022, §2.1, Eq. 9,
from Deng, cited):

$$E'_j=\frac{\alpha_{\mathrm W}}{h}\big(E^*_{j+\frac12}-E^*_{j-\frac12}\big)+\frac{192-175\alpha_{\mathrm W}}{256h}(E_{j+1}-E_{j-1})+\frac{35\alpha_{\mathrm W}-48}{320h}(E_{j+2}-E_{j-2})+\frac{64-45\alpha_{\mathrm W}}{3840h}(E_{j+3}-E_{j-3}),$$

sixth order in general and eighth order for $\alpha_{\mathrm W}=256/175$,
the value used; it mixes numerical fluxes at edges with physical fluxes
$E_j$ at nodes.

**Fourth order, edge fluxes only** (Wu et al. 2023, §2.2.1, Eq. 12):

$$E'_j=\frac{\alpha_{\mathrm W}}{h}\big(E^*_{j+\frac12}-E^*_{j-\frac12}\big)+\frac{b_{\mathrm W}}{h}\big(E^*_{j+\frac32}-E^*_{j-\frac32}\big),\qquad \alpha_{\mathrm W}=\tfrac98,\ b_{\mathrm W}=-\tfrac1{24}.$$

The coefficients satisfy $\alpha_{\mathrm W}+3b_{\mathrm W}=1$ and
$\alpha_{\mathrm W}+27b_{\mathrm W}=0$, the conditions for fourth order
*(compiler check, not in the sources)*. Wu et al. state that the scheme
satisfies the [geometric conservation law](/properties/geometric-conservation-law.md)
and can capture shocks (§1, citing earlier work); Ma et al. compute the
grid metrics with the same scheme as the flux derivatives for that purpose
(§2). Viscous terms are differenced by fourth-order central differences
in Wu et al.

## Interpolation of the interface states

**Explicit fifth-order interpolation (WCNS-E).** The left state at
$j+\tfrac12$ is a weighted combination of three third-order candidates on
the five-point stencil (Ma et al. 2022, Eqs. 10–15; Wu et al. 2023,
Eqs. 13–14):

$$u^{\mathrm L}_{j+\frac12}=\sum_{k=0}^{2}\mathsf w_k\,u^{(k)}_{j+\frac12},\qquad u^{(0)}=\tfrac18(3u_{j-2}-10u_{j-1}+15u_j),\quad u^{(1)}=\tfrac18(-u_{j-1}+6u_j+3u_{j+1}),\quad u^{(2)}=\tfrac18(3u_j+6u_{j+1}-u_{j+2}),$$

with Z-type weights (Borges et al., cited)

$$\mathsf w_k=\frac{a_k}{\sum_la_l},\qquad a_k=d_k\Big(1+\frac{|\mathrm{IS}_0-\mathrm{IS}_2|}{\mathrm{IS}_k+\epsilon_{\mathrm Z}}\Big),\qquad d_k=\big(\tfrac1{16},\tfrac{10}{16},\tfrac5{16}\big),$$

and indicators $\mathrm{IS}_k=(hf^{(k)})^2+(h^2s^{(k)})^2$ built from
one-sided first- and second-derivative estimates on each candidate
stencil (Ma et al., Eqs. 13–15; page-local $f^{(k)}$, $s^{(k)}$). With
$\mathsf w_k=d_k$ the interpolation is the linear fifth-order one,
$u^{\mathrm L}_{j+1/2}=\tfrac1{128}(3u_{j-2}-20u_{j-1}+90u_j+60u_{j+1}-5u_{j+2})$
(Ma et al., Eq. 10). Wu et al. print the same weight formula but not the
optimal weights or indicators. Ma et al. interpolate component by
component and mention no characteristic projection.

**Nonlinear tri-diagonal compact interpolation (WCNS-T).** Ma et al.
(2022, §2.2) replace the explicit interpolation, on the same five-point
stencil, by the seventh-order linear compact interpolation (Eq. 16)

$$\tfrac12u_{j-\frac12}+u_{j+\frac12}+\tfrac3{14}u_{j+\frac32}=-\tfrac1{224}u_{j-2}+\tfrac18u_{j-1}+\tfrac{15}{16}u_j+\tfrac58u_{j+1}+\tfrac1{32}u_{j+2},$$

written as a convex combination of four fourth-order compact
sub-interpolations, each containing interface unknowns (Eq. 18), with
optimal weights $d_k=(1,18,30,7)/56$, which then become Z-type nonlinear
weights (Eq. 21):

$$a_k=d_k\Big(1+\frac{|\mathrm{IS}_0+3\mathrm{IS}_1-3\mathrm{IS}_2-\mathrm{IS}_3|}{\mathrm{IS}_k+\epsilon_{\mathrm Z}}\Big),\qquad \epsilon_{\mathrm Z}=10^{-6},$$

with indicators that add a third-derivative term,
$\mathrm{IS}_k=(hf^{(k)})^2+(h^2s^{(k)})^2+(h^3t^{(k)})^2$, on the
four-point stencil $\{x_{j-3+k},\dots,x_{j+k}\}$ (Eqs. 22–25). The result
is a solution-dependent tri-diagonal system for the interface values
(Eq. 26), one solve per variable, grid line and direction. With
idealized weights (zero on candidates whose indicator stencil crosses a
jump in $[x_j,x_{j+1}]$, optimal elsewhere) the rows next to the jump lose
their off-diagonal coupling and the system splits into two independent
systems, one on each side; the authors call this the shock-capturing
mechanism and note that no switch between compact and explicit
interpolation families is needed (Eqs. 27–29). The decoupling role of the
weights is also recorded on [shock sensors](/definitions/shock-sensor.md).

## Order, resolution and cost

On isentropic-vortex advection WCNS-E reaches order 4.98 and WCNS-T 7.01
at the finest grid (grid size printed as 2802, whose meaning the paper
does not state; Ma et al., §2.3.2, Table 2). Per grid, WCNS-T is 5 to 7
times more expensive ($1.26\times10^4$ against $1.83\times10^3$ CPU time
units on that grid, hardware not named), cheaper at equal error
(Fig. 3). By Fourier and approximate-dispersion-relation analyses the
resolving ratio (fraction of resolvable wavenumbers) rises from 30.2% to
49.3% and from 28.6% to 39.7%, and on the shock–entropy-wave interaction
WCNS-T on 200 points matches WCNS-E on 300 (§2.3, Table 1, Figs. 1–2;
detail on [low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).
Wu et al. report no order, resolution or cost figures for their
fourth-order scheme.

## Dissipation in turbulence: the weights decide

Ma et al. (2022) and Wu et al. (2023) locate the dissipation that matters
in turbulence in the interpolation step, and both report a nonlinear weighting that costs
accuracy in shock-free flow:

- **Implicit LES.** Ma et al. (§1, §2.2) state, citing Ishiko & Shimada and
  Matsukawa, that WCNS-E behaves like a strongly dissipative subgrid model,
  which makes WCNS-based implicit LES ineffective, and that the explicit
  interpolation dominates its dissipation. With WCNS-T and no subgrid
  model they run the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
  the [circular cylinder](/benchmarks/circular-cylinder-wake.md) at
  $Re_D=3900$ ($180\times180\times45$), the T106A
  [turbine cascade](/benchmarks/turbine-cascade.md) at $Re\approx60\,000$
  (about 12 million points) and the transonic M219 open cavity, and
  conclude that WCNS-T "is not over-dissipative anymore for ILES" (§3–4;
  results on [implicit LES](/definitions/implicit-les.md)). In the T106A
  cascade the *linear* WCNS-E ($\mathsf w_k=d_k$) captures the
  leading-edge separation that the nonlinear WCNS-E misses (§3.3,
  Fig. 12).
- **Hybrid RANS/LES and explicit LES.** Wu et al. (§2.2.1, §3.3) run the
  fourth-order WCNS-E-type interpolation with two regularizers: $\epsilon_{\mathrm Z}=100$,
  chosen "to neglect the nonlinear weight and approach the linear scheme"
  (WCNS-L), and $\epsilon_{\mathrm Z}=10^{-6}$ (WCNS-Z). In SATES hybrid RANS/LES of
  the [30P30N high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
  ($Re=1.71\times10^6$, $M=0.17$, 27 million cells) the lift coefficient
  deviates from the measured mean 2.83 by $-0.4\%$ (WCNS-L), $-6.7\%$
  (WCNS-Z) and $-11.0\%$ (a second-order blended central/upwind scheme
  with 2% upwinding) (Table 2). The authors attribute the WCNS-Z deficit to
  the Z-type weights, which reach optimal order at first-order critical
  points but "still suffered a loss in accuracy near high-order critical
  points", adding dissipation that delays the instability of the slat-cove
  shear layer, and recommend linear interpolation for shock-free low-Mach
  flow; they expect the Z-type weights to cause "considerable numerical
  dissipation in supersonic turbulent flows" and leave it to future work
  (§3.3, §4). The same WCNS-L carries their comparison of SATES with
  Smagorinsky LES and IDDES (see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
  and [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

Ma et al. lower the dissipation by changing the interpolation family
while keeping nonlinear weights, Wu et al. by switching the weights off
in a shock-free flow. No source runs both remedies on one case.

**Linear WCNS-E-4 against MUSCL under SATES-σ.** In the same group's
later paper, [Wu et al. (2024)](/sources/wu-2024.md), §2.3, Eqs. (12)–(15),
the convective scheme of PHengLEI is the fourth-order flux difference
above ($\alpha_{\mathrm W}=9/8$, $b_{\mathrm W}=-1/24$) with the Roe flux
and the linear fifth-order interpolation
$u^{\mathrm L}_{j+1/2}=\tfrac1{128}(3u_{j-2}-20u_{j-1}+90u_j+60u_{j+1}-5u_{j+2})$
and its mirror image for $u^{\mathrm R}_{j+1/2}$, i.e. the linear weights
are used "to reduce the numerical dissipation in the original WCNS-E-4",
with fourth-order central viscous terms. The comparison scheme is a MUSCL
interpolation with a smooth rational limiter (its own parameter $\approx10^{-6}$) and a second-order
flux difference (§2.4, Eqs. 16–17). On the supercritical
[circular cylinder](/benchmarks/circular-cylinder-wake.md) at
$Re_D=3\times10^6$, $M=0.2$ (about 6.7 million cells, $y^+<1$), with the
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md)
variant SATES-σ, the Strouhal number, base pressure, recirculation length
and drag are $0.24$, $-0.34$, $0.79D$, $0.55$ with WCNS and $0.19$,
$-1.32$, $0.61D$, $1.26$ with MUSCL (Table 3; the measured
$C_D$ of Shih et al. that they cite is $0.24$ at $Re_D=1\times10^6$).
The authors conclude that WCNS is "more accurate and necessary": with
MUSCL the separation is not delayed (a subcritical-like pressure
distribution and higher drag), the Kelvin–Helmholtz instability of the
shear layer is damped, the recirculation is shorter and the
moderate-frequency content of the wake spectrum is suppressed (§3.2,
Figs. 13–17; §4). The same linear WCNS-E-4 carries their
stall sweep of the [30P30N high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
at $Re_c=9\times10^6$. As in Wu et al. (2023), the scheme is stated to
capture shocks and to satisfy the
[geometric conservation law](/properties/geometric-conservation-law.md),
by citation (§2.3).

## Qualifications

- **Evidence.** Ma et al. give no error norms for the implicit-LES cases,
  and print neither the Taylor–Green Reynolds number and grid nor the
  cavity Mach number; Wu et al.'s scheme comparison is one airfoil on one
  grid with one closure (SATES), against integrated lift and measured
  profiles.
- **Idealized decoupling.** The splitting of the WCNS-T system at a jump
  assumes weights exactly zero on crossing stencils; with $\epsilon_{\mathrm Z}=10^{-6}$
  they are small but not zero, which the authors acknowledge by calling
  the argument "a theoretical analysis" (§2.2).
- **What $\epsilon_{\mathrm Z}=100$ does.** Wu et al. state that the large regularizer
  makes the weights near linear. With indicators of the form printed by
  Ma et al. (Eqs. 13–15), quadratic in the differences of the
  interpolated variable, the effect of a fixed $\epsilon_{\mathrm Z}$ depends on the
  scaling of that variable *(compiler check, not in the sources)*; Wu et
  al. state neither their indicators nor the scaling.
- **Printed slips (Ma et al. 2022).** The boundary rows of the
  right-hand-side matrix of the WCNS-T system are printed
  $(3/128,\,-5/32,\,-19/64,\,15/32,\,-5/128)$, whose sum is zero, so as
  printed the boundary interpolation would not reproduce a constant
  *(compiler check, not in the sources)*; the closure is not stated
  elsewhere. The second-derivative indicator of candidate 2 (Eq. 24) is
  printed identical to that of candidate 1, while the first- and
  third-derivative indicators of candidate 2 use the shifted stencil.
- **Printed slips (Wu et al. 2023).** The sentence giving the order of
  Eq. (12) is garbled ("and equation) is 4th order in accuracy"); the
  scheme comparison of §3.4 refers to groups "B" and "C" where Table 2
  labels them A and B.
- **Printed slips (Wu et al. 2024).** The MUSCL interpolation is called
  "third-order" in §2.4 and once in §3.2, "second-order" elsewhere in
  §3.2 and in §4, beside a
  second-order flux difference; the cylinder comparison is one grid and
  one closure, against references at other Reynolds numbers for part of
  the data.
- **Cost of WCNS-T.** Ma et al. state that the nonlinear compact
  interpolation needs "no extra computation" (§2.2, §4) and that one
  solution-dependent tri-diagonal system is solved per variable, grid
  line and direction; their Table 2 prints 5 to 7 times the CPU time of
  WCNS-E on the same grid.

# Citations

- [Ma et al. (2022)](/sources/ma-2022.md) — §1 (WCNS over-dissipative for implicit LES, cited); §2, Eqs. (1)–(2) (curvilinear form, metrics with the flux scheme); §2.1, Eqs. (7)–(15) (three components, eighth-order flux difference, WCNS-E, Z-type weights, indicators); §2.2, Eqs. (16)–(29) (compact interpolation, WCNS-T, decoupling at discontinuities, boundary rows); §2.3, Tables 1–2, Figs. 1–3 (resolution, order, cost); §3.1–3.4, Figs. 4–16 (implicit LES; linear against nonlinear WCNS-E in T106A); §4.
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1 (GCL and shock capturing of WCNS, cited); §2.2.1, Eqs. (10)–(14) (fourth-order flux difference, Roe flux, Z-type weights, WCNS-L and WCNS-Z); §2.2.2, Eq. (15) (blended comparison scheme); §3.3, Table 2, Figs. 11–16 (scheme dissipation on the 30P30N airfoil); §3.4; §4.
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.3, Eqs. (12)–(15) (linear WCNS-E-4 in PHengLEI, Roe flux, GCL by citation); §2.4, Eqs. (16)–(17) (MUSCL comparison scheme); §3.2, Table 3, Figs. 13–17 (WCNS against MUSCL on the supercritical cylinder); §4.
