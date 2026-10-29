---
type: Method
title: "Weighted compact nonlinear schemes"
description: "The weighted compact nonlinear scheme (WCNS) differences numerical fluxes at cell edges, computed by a Riemann flux from nonlinearly interpolated interface states; the page gives the explicit and the tri-diagonal compact interpolations, the fourth-, sixth- and eighth-order flux differences, and how the nonlinear weights (Z-type, TENO and smooth TENO) set its dissipation in implicit LES and hybrid RANS/LES."
status: established
aliases: [WCNS, weighted compact nonlinear scheme, WCNS-E, WCNS-T, WCNS-L, WCNS-Z, WCNS-JS, WCNS-ST, WCNS-STA, smooth TENO, S-TENO, nonlinear compact interpolation]
tags: [numerical-dissipation, implicit-les, compressible, hybrid-rans-les]
timestamp: 2026-10-29T07:36:00Z
---

# Weighted compact nonlinear schemes

The **weighted compact nonlinear scheme (WCNS)**, of Deng & Zhang as the
sources cite it, is a high-order finite-difference shock-capturing scheme
built from three components: (i) a high-order **flux difference** that
differentiates numerical fluxes defined at cell edges (and, in one form,
physical fluxes at nodes); (ii) a **numerical flux**, an approximate
Riemann solver (Roe in every source here) evaluated from left and right
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
whose WCNS section this page extends. The same group's sixth-order
multi-order-candidate WCNS with an adaptive Roe dissipation
([Wu et al. 2026](/sources/wu-2026-b.md)) runs in PHengLEI-HyOrder.

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

## TENO-type and smooth scale-separating weights

[Wu et al. (2024b)](/sources/wu-2024-b.md) keep the fifth-order explicit
interpolation and the Roe flux but replace the Z-type weights by
TENO-type weights, for SATES hybrid RANS/LES in PHengLEI (§II.B–D,
Eqs. 8–23). Their flux difference is the explicit sixth-order one on
edge fluxes only,

$$E'_j=\frac{75}{64h}\big(E^*_{j+\frac12}-E^*_{j-\frac12}\big)-\frac{25}{384h}\big(E^*_{j+\frac32}-E^*_{j-\frac32}\big)+\frac{3}{640h}\big(E^*_{j+\frac52}-E^*_{j-\frac52}\big)$$

(Eq. 10), exact for a linear flux *(compiler check, not in the sources:
$\tfrac{75}{64}-3\cdot\tfrac{25}{384}+5\cdot\tfrac{3}{640}=1$)*; the
three third-order candidates and the optimal weights
$d_k=(\tfrac1{16},\tfrac{10}{16},\tfrac5{16})$ are those above, applied to
characteristic variables. Citing Nonomura & Fujii, they state that the
flux difference does not affect the resolution and that the nonlinear
interpolation dominates it (§I). Four weightings are compared, with
$\tau_{\mathrm Z}=|\mathrm{IS}_0-\mathrm{IS}_2|$ (page-local) and
$\epsilon_{\mathrm Z}=10^{-40}$ in all of them:

- **WCNS-JS:** $a_k=d_k/(\mathrm{IS}_k+\epsilon_{\mathrm Z})^2$ (Eq. 14).
- **WCNS-Z:** $a_k=d_k\big(1+\tau_{\mathrm Z}/(\mathrm{IS}_k+\epsilon_{\mathrm Z})\big)$,
  first power, chosen "to reduce the numerical dissipation" (Eq. 15).
- **WCNS-T** (TENO weighting in a WCNS, after Fu et al. and Hiejima, as
  cited): the scale-separated measure
  $\gamma^{\mathrm T}_k=\big(1+\tau_{\mathrm Z}/(\mathrm{IS}_k+\epsilon_{\mathrm Z})\big)^6$,
  its normalized form $\chi^{\mathrm T}_k=\gamma^{\mathrm T}_k/\sum_l\gamma^{\mathrm T}_l$,
  the sharp cut-off $\delta^{\mathrm T}_k=0$ for $\chi^{\mathrm T}_k<C_T$ and
  1 otherwise, $C_T=10^{-5}$, and the weights
  $\mathsf w_k=d_k\delta^{\mathrm T}_k/\sum_ld_l\delta^{\mathrm T}_l$
  (Eqs. 16–17, 23). (This WCNS-T is not the tri-diagonal compact WCNS-T of
  Ma et al. above; the two papers use the same label for different
  schemes.)
- **WCNS-ST** (smooth TENO, the contribution): the step is replaced by
  $\delta^{\mathrm T}_k=\tanh\big((\chi^{\mathrm T}_k/C_T)^{2}\big)$ for
  $\chi^{\mathrm T}_k<10C_T$ and $\delta^{\mathrm T}_k=1$ above, to save the
  hyperbolic tangent (Eqs. 18–19; Fig. 2 compares the exponents 1, 2, 3,
  5, 7 and 20 with the step). The weights become continuous functions of
  the data. **WCNS-STA** adds an adaptive threshold
  $C_T=10^{-\lfloor\beta_{\mathrm A}\rfloor}$,
  $\beta_{\mathrm A}=10-5\,(1-g)$, $g=(1-m_{\mathrm R})^4(1+4m_{\mathrm R})$,
  driven by the discontinuity indicator $m_{\mathrm R}$ of Ren et al. as
  cited (page-local $\beta_{\mathrm A}$, $m_{\mathrm R}$; formula on
  [shock sensors](/definitions/shock-sensor.md)), so that $C_T=10^{-5}$
  near discontinuities ($m_{\mathrm R}\approx1$) and $10^{-10}$ in smooth
  regions ($m_{\mathrm R}\approx0$) (Eqs. 20–22).

**The argument against the sharp cut-off.** Wu et al. (2024b) hold that
marginally resolved high-wavenumber turbulence has no true
discontinuity, and that the discontinuous switch of the sharp cut-off
between "resolved" and "non-resolved" scales makes the weights
discontinuous, which "would lead to numerical instability or bad
convergence" of the Newton-like sub-iterations of their implicit
dual-time integration (second-order backward differences with LU-SGS)
(§I, §II.D). They also state that the stencil-selecting TCNS of Zhang et
al. "struggles to maintain the continuity of the interpolation variable
near discontinuities" (§II.D). The evidence:

- **Spectral properties.** By Pirozzoli's approximate dispersion relation,
  WCNS-T keeps the linear-scheme properties over a wide wavenumber range,
  WCNS-ST stays close to WCNS-T and WCNS-STA approaches the linear scheme
  (§IV.A, Fig. 4; qualitative only).
- **Two-dimensional Riemann problem** (configuration 3 of Lax & Liu,
  $401\times401$, $t=0.8$): the TENO-type weightings resolve
  "significantly more small-scale structures" than JS and Z, with sharp
  and stable shocks; WCNS-ST matches WCNS-T and WCNS-STA resolves more
  (§IV.B, Fig. 5).
- **30P30N airfoil** (SATES, $Re=1.71\times10^6$, $M=0.17$, $5.5^\circ$,
  about 27 million cells): WCNS-JS suppresses the slat-cove shear-layer
  instability and its mean $C_p$ deviates mostly on the flap; WCNS-Z does
  better; WCNS-T, -ST and -STA agree with the experiment and with the
  linear fifth-order WCNS; sub-iteration residuals converge worse with
  WCNS-T than with WCNS-ST or -STA, and WCNS-ST matches the measured
  slat-cove vorticity better than WCNS-T, which the authors relate to the
  convergence (§IV.C.1, Figs. 7–10; see
  [30P30N high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md)).
- **Supersonic base flow** (Herrin & Dutton, $M_\infty=2.46$, 7 and 42
  million cells): within a time step the residual falls by about one
  order with WCNS-T, three with WCNS-ST and two with WCNS-STA; on the
  coarse grid the resolved turbulent kinetic energy peak is predicted
  best by WCNS-STA, then WCNS-ST, then WCNS-T, with JS and Z poor (the
  fine-grid reference is WCNS-JS) (§IV.C.2, Figs. 13–14).
- **Cost** (Table I, CPU hours over WCNS-JS): 30P30N — linear 0.97, Z
  1.03, T 1.51, ST 1.52, STA 1.68; base flow — Z 1.02, T 1.58, ST 1.55,
  STA 1.54.

They recommend smooth scale separation "in TENO-based schemes,
especially in simulating multiscale flows" (§V). The TENO family itself
is on [WENO and hybrid schemes](/methods/weno-scheme.md); the effect of
the weights on shear-layer dissipation on
[numerical dissipation](/properties/numerical-dissipation.md). In the
compressible Taylor–Green comparison of
[Wang et al. (2024b)](/sources/wang-2024-i.md), §I, a WCNS is listed
among the schemes earlier tested on that case, in passing.

## Sixth-order multi-order-candidate interpolation with adaptive Roe dissipation

[Wu et al. (2026)](/sources/wu-2026-b.md) use in PHengLEI-HyOrder a
sixth-order WCNS whose interpolation of the primitive variables follows
the multi-order-candidate (MOC) form that they cite to Ma et al. (2024)
and Bai et al. (2024), which the authors describe as "a simplified equivalent weighting
formulation of WCNS" (§1, §3.1, Eqs. 22–23):

$$u^{\mathrm L}_{j+\frac12}=\sum_{k=0}^{3}\mathsf w_k\,u^{(k)}_{j+\frac12},\qquad d_k=\big(\tfrac1{16},\tfrac{10}{16},\tfrac5{16},100\big),\qquad a_k=\frac{d_k}{\mathrm{IS}_k+\epsilon_{\mathrm Z}},\quad \epsilon_{\mathrm Z}=10^{-40},$$

with $u^{(0)}$, $u^{(1)}$, $u^{(2)}$ the three third-order candidates above
and $u^{(3)}$ a sixth-order optimized linear interpolation on a six-point
stencil; the indicators are "given by Ma et al. (2024)" and not printed.
Their MOC6-STA then replaces these weights by the smooth scale-separating
form of Wu et al. (2024b), now over four candidates,
$\mathsf w_k=d_k\delta^{\mathrm T}_k/\sum_ld_l\delta^{\mathrm T}_l$ with
$\delta^{\mathrm T}_k=\tanh\big((\chi^{\mathrm T}_k/C_T)^{k}\big)$ for
$\chi^{\mathrm T}_k<10C_T$ and 1 above, and $C_T$ adapted after Fu et al.
(as cited) (§3.2, Eqs. 24–25; the exponent is printed with the letter of
the candidate index, where Wu et al. (2024b) print 2; see
Qualifications). The aim stated is central-like stencils at low wavenumbers
and added dissipation at high wavenumbers.

**Tests** (§3.2–§3.3). On the interpolation of $f(x)=x^me^x$ at $x=0$
($m=1$, a regular point; $m=2$, a first-order critical point; $m$
page-local) MOC6-STA gives "nearly identical error levels and convergence
behavior" to MOC6, with errors below those of the fourth-order WCNS-CU4; a
third-order MUSCL is also plotted (Fig. 2). In the approximate dispersion-relation
analysis MOC6 has smaller dispersion and dissipation errors at resolved
scales and more dissipation at high wavenumbers (Fig. 3; see
[eigensolution analysis](/methods/eigensolution-analysis.md)).

**Adaptive Roe dissipation.** The interface flux is the Roe flux with its
upwind term scaled by a coefficient computed for each primitive variable,

$$f^*_{j+\frac12}=\tfrac12\Big[f(U^{\mathrm L})+f(U^{\mathrm R})-\phi_{\mathrm R}\,|\tilde A|\,(U^{\mathrm R}-U^{\mathrm L})\Big],\qquad \phi_{\mathrm R}=\phi_1+\phi_2-\phi_1\phi_2,$$

with $|\tilde A|$ the Roe-averaged Jacobian, $\phi_1$ a relative jump of
the interface states and $\phi_2$ a Ducros-type dilatation–vorticity ratio
(Eqs. 27–28; page-local $\phi_{\mathrm R}$, $\phi_1$, $\phi_2$; formulas on
[shock sensors](/definitions/shock-sensor.md)). On the two-dimensional
Riemann problem (configuration 3 of Lax & Liu, $400\times400$) the
coefficient stays close to one in most regions, keeping shock capturing,
and decreases near the shear layers (Fig. 4). The scheme carries the
SATES-II and AIDDES runs of the supersonic base flow and the 30P30N
(see [SATES](/methods/self-adaptive-turbulence-eddy-simulation.md)).

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
- **Printed slips (Wu et al. 2024b).** §II.B names the candidate
  stencils $K_1$, $K_2$, $K_3$ where Eq. (12) and Fig. 1 label them $K_0$,
  $K_1$, $K_2$. After Eq. (22) the text says that for $m_{\mathrm R}\approx0$
  "$C_T$ increases to $10^{-\alpha_1}$"; with the printed
  $\alpha_1=10$, $\alpha_2=5$ the threshold goes from $10^{-5}$ to
  $10^{-10}$, i.e. it decreases *(compiler check, not in the sources)*.
  The Appendix states that WCNS-STA costs "a slightly further increase"
  over WCNS-ST, which Table I shows for the 30P30N (1.68 against 1.52) but
  not for the base flow (1.54 against 1.55). §IV.C.1 cites Fig. 6 (the
  airfoil geometry) for the slat-cove structures shown in Fig. 7.
- **Test scope (Wu et al. 2024b).** The paper tests the convergence
  argument against the sharp cut-off with one implicit dual-time
  integration (second-order backward differences with LU-SGS
  sub-iterations); the base-flow ranking uses one coarse grid, with a
  WCNS-JS fine-grid reference.
- **Printed wording (Wu et al. 2026).** §3.2 states that MOC6-STA reaches
  "nearly identical error levels and convergence behavior" to the
  sixth-order MOC6, then that its error "remains consistently lower than
  that of the 4th-order WCNS-CU4 scheme while showing the same first-order
  convergence rate as all other high-order schemes". The cut-off exponent
  of Eq. (24) is printed with the letter of the candidate index ($n$ in the
  paper, $k$ here), the
  text after it writes the cut-off with index $k$, and the scale-separated
  measure of Eq. (24) is not defined in the paper. The coefficient is
  called $\phi$ in Eq. (27) and $\phi_k$ "of kth's variable" in the text.
- **Cost of WCNS-T.** Ma et al. state that the nonlinear compact
  interpolation needs "no extra computation" (§2.2, §4) and that one
  solution-dependent tri-diagonal system is solved per variable, grid
  line and direction; their Table 2 prints 5 to 7 times the CPU time of
  WCNS-E on the same grid.

# Citations

- [Ma et al. (2022)](/sources/ma-2022.md) — §1 (WCNS over-dissipative for implicit LES, cited); §2, Eqs. (1)–(2) (curvilinear form, metrics with the flux scheme); §2.1, Eqs. (7)–(15) (three components, eighth-order flux difference, WCNS-E, Z-type weights, indicators); §2.2, Eqs. (16)–(29) (compact interpolation, WCNS-T, decoupling at discontinuities, boundary rows); §2.3, Tables 1–2, Figs. 1–3 (resolution, order, cost); §3.1–3.4, Figs. 4–16 (implicit LES; linear against nonlinear WCNS-E in T106A); §4.
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1 (GCL and shock capturing of WCNS, cited); §2.2.1, Eqs. (10)–(14) (fourth-order flux difference, Roe flux, Z-type weights, WCNS-L and WCNS-Z); §2.2.2, Eq. (15) (blended comparison scheme); §3.3, Table 2, Figs. 11–16 (scheme dissipation on the 30P30N airfoil); §3.4; §4.
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §I (interpolation dominates resolution, cited); §II.B–D, Eqs. (8)–(23) (sixth-order flux difference, JS, Z, TENO, smooth TENO and adaptive weights); §IV.A–C, Figs. 4–14, Table I (spectral analysis, Riemann problem, 30P30N, supersonic base flow, sub-iteration convergence, cost); §V.
- [Wang et al. (2024b)](/sources/wang-2024-i.md) — §I (WCNS among earlier Taylor–Green schemes; passing).
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §1, §3.1–§3.3, Eqs. (22)–(28), Figs. 2–4 (MOC6 and MOC6-STA interpolation, convergence and dispersion tests, adaptive Roe dissipation, Riemann problem); §3.4 (PHengLEI-HyOrder).
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.3, Eqs. (12)–(15) (linear WCNS-E-4 in PHengLEI, Roe flux, GCL by citation); §2.4, Eqs. (16)–(17) (MUSCL comparison scheme); §3.2, Table 3, Figs. 13–17 (WCNS against MUSCL on the supercritical cylinder); §4.
