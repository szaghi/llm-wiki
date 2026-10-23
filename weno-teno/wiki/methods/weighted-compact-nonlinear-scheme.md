---
type: Method
title: "Weighted compact nonlinear schemes (WCNS)"
description: "WCNS are finite-difference shock-capturing schemes in three steps — nonlinear node-to-interface interpolation, an interface flux, and high-order interface-to-node differencing; the page records explicit, TENO-weighted, spectrally optimized adaptive-dissipation, exponential-weight, multi-resolution, hybrid and mapped members, and an open disagreement on conservation."
status: established
aliases: [WCNS, WCNS-Z, WCNS-JS, TCNS, targeted compact nonlinear scheme, WCNS-T, HWCNS, WCNS-IS, PP-WCNS-IS, explicit WCNS, WCNS-SA, WCNS-opt, WCNS-LD, ONL6, WCNS-MR, WCNS7M, MND scheme, WCNS-EXP, hybrid MR-WCNS]
tags: [compact-scheme, finite-difference, weno, teno, numerical-flux, multiphase]
timestamp: 2026-10-23T23:00:00Z
---

# Weighted compact nonlinear schemes (WCNS)

The **weighted compact nonlinear scheme** of Deng and Zhang (as recalled by Fu 2023, §3.7, and Wong et
al. 2021, §4) is a finite-difference scheme built in three steps:

1. a nonlinear (WENO-weighted) **interpolation** of the variables from the nodes $x_i$ to the
   interfaces ("midpoints") $x_{i+1/2}$, giving $u^\pm_{i+1/2}$;
2. evaluation of an **interface flux** $h(u^-_{i+1/2},u^+_{i+1/2})$, e.g. a Riemann solver;
3. high-order **interface-to-node differencing** of the interface fluxes, compact (spatially
   implicit) in the original scheme, explicit in later ones, to obtain $\partial_xf$ at the nodes.

It shares steps 1 and 2 with the [alternative WENO formulation](/methods/alternative-weno.md), which
reaches high order by explicit even-derivative corrections instead; Ye et al. (2022, §1) state that
AFWENO "is similar to WCNS and is equivalent to the HWCNS scheme under specific parameters" (HWCNS is
cited to a Deng et al. conference paper). For [AFTENO](/methods/afteno.md), Ye et al. (§1, §5) credit
this interpolation-plus-flux structure with the freedom to use any monotone or Riemann-solver flux and
to interpolate conserved, primitive or characteristic variables. Wong et al. (2021, §4.3) make the
same point against flux-split FD-WENO, which they say "degenerates to only second order" with a
Riemann solver, whereas "a WCNS can still maintain high order".

## Explicit WCNS with hybrid differencing (WCNS-IS)

Wong, Angel, Barad & Kiris (2021, §4) build a fifth-order explicit WCNS for the five-equation
two-phase model ([five-equation model](/definitions/five-equation-model.md)).

**Differencing.** Following Nonomura & Fujii's observation that explicit schemes are more efficient,
they use Deng's explicit hybrid cell-midpoint and cell-node scheme (HCS; §4.1, Eq. (77)), with
midpoint fluxes $\tilde f_{i\pm1/2}$ from step 2 and nodal fluxes $f_j=f(u_j)$:

$$\partial_xf\big|_i\approx\frac1{\Delta x}\Big[\Psi\big(\tilde f_{i+1/2}-\tilde f_{i-1/2}\big)-\tfrac{175\Psi-192}{256}\big(f_{i+1}-f_{i-1}\big)+\tfrac{35\Psi-48}{320}\big(f_{i+2}-f_{i-2}\big)-\tfrac{45\Psi-64}{3840}\big(f_{i+3}-f_{i-3}\big)\Big],$$

($\Psi$ the HCS parameter, page-local). With $\Psi=256/175$ the linear scheme is eighth order, leading
error $-\tfrac1{40320}\partial_x^9f\,\Delta x^8$ (Eqs. (78)–(79)), although the family is called
"sixth order". Rewritten in flux-difference form, after Subramaniam, Wong & Lele, it has the implied
interface flux (Eq. (80))

$$\hat f_{i+1/2}=\Psi\tilde f_{i+1/2}-\big(\tfrac{75\Psi}{128}-\tfrac{37}{60}\big)(f_i+f_{i+1})+\big(\tfrac{25\Psi}{256}-\tfrac2{15}\big)(f_{i-1}+f_{i+2})-\big(\tfrac{3\Psi}{256}-\tfrac1{60}\big)(f_{i-2}+f_{i+3}).$$

*(Compiler check, not in the sources: the HCS is exact on polynomials of degree 8, its degree-9
error is $-\tfrac{1}{40320}\partial_x^9f\,\Delta x^8$, and the difference of the implied fluxes
reproduces the bracket above.)* The same formula reconstructs the interface advection velocity, so
that the non-conservative volume-fraction term uses the same differencing as the flux (Eqs. (81)–(82)).

**Interpolation.** An incremental-stencil WENO interpolation adapted from the finite-volume WENO-IS
of Wang, Xiang & Hu (§4.3, Eqs. (84)–(101)): four candidates on $\{i,i+1\}$, $\{i-1,i\}$,
$\{i,i+1,i+2\}$, $\{i-2,i-1,i\}$, with linear weights $\tfrac{15}{32},\tfrac5{32},\tfrac5{16},\tfrac1{16}$
that combine them into the fifth-order interpolant
$\tfrac1{128}(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2})$, WENO-Z-type weights with the TENO
reference indicator, and an extra indicator on $\{i-1,i,i+1\}$ for the two-point stencils
([smoothness indicators](/definitions/smoothness-indicator.md), [WENO-Z](/methods/weno-z.md),
[targeted ENO](/methods/targeted-eno.md)). *(Compiler check: the four candidates with these weights
give exactly the printed interpolant.)* It is applied to primitive variables projected on
characteristic fields of the primitive system (App. A), with HLLC midpoint fluxes
([HLL-family solvers](/methods/hll-riemann-solvers.md)). Appendix B proves fifth order for a scalar
law with $f'>0$ away from critical points, under the sufficient condition $\omega_k-d_k=O(\Delta x^4)$
([accuracy at critical points](/properties/critical-point-accuracy.md)).

**Positivity and boundedness (PP-WCNS-IS).** Two limiter stages blend with first-order quantities:
an interpolation limiter blends the midpoint states with the node state, successively for partial
densities, volume fraction and $\rho e-\bar p_\infty$ (page-local mixture stiffening pressure); a flux
limiter blends the implied flux with the first-order HLLC flux in the same three stages, with a common
blending factor for the two sides of an interface (§5, Algorithms 1–6). The first-order HLLC scheme is
proved positivity- and boundedness-preserving under CFL $\le0.5$, which the SSP-RK3 extension keeps
(§3.3, §5.3) ([bound preservation](/properties/bound-preservation.md),
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)). Because both
limiters act on the implied fluxes, the update stays in flux-difference form and is "discretely
conservative for all conservative equations" of the model (Abstract, §5.2).

**Results.** Fifth order on 2-D volume-fraction advection ($L_2$ from $3.136\times10^{-5}$ at $8^2$ to
$1.714\times10^{-13}$ at $256^2$, orders 4.85–4.97 beyond the first refinement; Table 4); sharp,
oscillation-free interfaces on 1-D advection, gas–liquid shock tube and multi-material Sedov problems;
the unlimited WCNS-IS fails (imaginary sound speed) on a Mach 10 shock/water-column interaction that
PP-WCNS-IS runs (§6.6); a Mach 100 water jet, multiphase version of the Mach 2000 jet (§6.7;
[shock–water column](/benchmarks/shock-water-column.md),
[high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md),
[Sedov blast wave](/benchmarks/sedov-blast-wave.md)).

## Very high-order interpolation with TENO stencils (WCNS-T, WCNS-JS)

Hiejima (2022) builds explicit WCNS-type schemes for the 3-D Euler equations at interpolation orders
5, 7, 9 and 11. Steps 1 and 2 are as above; step 3 is absent: the flux derivative is
$(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$ with AUSMDV interface fluxes, and "the WCNS does not include
a compact procedure for calculating the flux derivative" (§2.2, Eq. (5); the paper says nothing about
conservation). Primitive variables $(\rho,v,p)$ are interpolated componentwise, with no
characteristic projection, and the time integrator is the four-step fourth-order Runge–Kutta of
Jameson, Schmidt & Turkel at CFL 0.8 (§2.2).

- **Candidates.** For interpolation order $K$ on the full stencil of $K$ points
  $i-\tfrac{K-1}2,\dots,i+\tfrac{K-1}2$ ($K=2r-1$ in the source's order parameter $r$), $K-2$
  substencils: the central $\{i-1,i,i+1\}$ and the pairs $\{i,\dots,i+s+1\}$, $\{i-s-1,\dots,i\}$,
  $s=1,\dots,\tfrac{K-3}2$,
  the "pyramid" taken from the original TENO (§2.3, Fig. 1; see
  [targeted ENO](/methods/targeted-eno.md)). Each candidate is a Taylor expansion about $x_i$ with
  the derivatives replaced by one-sided or central differences on the substencil (Eqs. (6)–(12),
  coefficients in Tables 1, 3, 5); the seventh-order case is written out with its truncation terms
  (Eqs. (19)–(24)). *(Compiler check, not in the sources: with the derivative orders each substencil
  supports, a candidate equals the Lagrange interpolant of the substencil at $x_{i+1/2}$.)*
- **Linear weights** (Tables 2, 4, 6), for the order central, downwind, upwind, …: $K=7$:
  $(\tfrac{35}{64},\tfrac{35}{128},\tfrac7{128},\tfrac7{64},\tfrac1{64})$; $K=9$:
  $(\tfrac{525}{1024},\tfrac{525}{2048},\tfrac{105}{2048},\tfrac{63}{512},\tfrac9{512},\tfrac9{256},\tfrac1{256})$;
  $K=11$: $(\tfrac{8085}{16384},\tfrac{8085}{32768},\tfrac{1617}{32768},\tfrac{2079}{16384},\tfrac{297}{16384},\tfrac{99}{2048},\tfrac{11}{2048},\tfrac{11}{1024},\tfrac1{1024})$;
  the right state uses the mirrored weights. $K=5$ "is consistent with" Deng & Zhang's fifth-order
  WCNS. *(Compiler check, not in the sources: the $K=7$ set combines the five candidates into the
  seven-point interpolant at $x_{i+1/2}$ exactly; for $K=5$ the weights are
  $(\tfrac58,\tfrac5{16},\tfrac1{16})$, the fifth-order interpolation weights printed by Chu et al. 2022
  on the [alternative WENO](/methods/alternative-weno.md) page in the upwind-first order.)* The
  nonlinear value is written $u^{\mathrm{opt}}_{i+1/2}+\sum_k(\omega_k-d_k)u^{(k)}_{i+1/2}$, with
  $u^{\mathrm{opt}}_{i+1/2}$ the optimal linear interpolation (page-local; Eq. (25)).
- **Indicators.** The Deng–Zhang form, unweighted squares of the difference derivatives on each
  substencil (Eq. (14); [smoothness indicators](/definitions/smoothness-indicator.md)).
- **WCNS-JS:** $\alpha_k=d_k/(\epsilon+\beta_k)^2$, $\epsilon=10^{-40}$ (Eq. (15);
  [WENO-JS](/methods/weno-js-reconstruction.md)). **WCNS-T:** $\gamma_k=1/(\epsilon+\beta_k)^6$, no
  constant and no global indicator, normalized $\chi_k$, cut-off $C_T=10^{-5}$ on every candidate,
  $\omega_k=d_k\delta_k/\sum_ld_l\delta_l$ (Eqs. (16)–(18)).
- **Positivity fallback.** In double Mach reflection, where an interpolated $\rho$ or $p$ is
  negative a first-order interpolation is used instead (§3.4, after Kamiya et al.); which variables
  and sides is not stated ([bound preservation](/properties/bound-preservation.md)).

**Evidence** (qualitative; no convergence test; Hiejima 2022, §3, App.): on Sod and Lax at 101 points
WCNS-JS is oscillation-free at every order and WCNS-T shows slight under- and overshoots growing with
order; all schemes overshoot the Lax velocity where the solution is "continuous but not
differentiable" ([Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)). On the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md) (201 and 401 points) WCNS-JS shows "no
difference based on the accuracy" and misses the small waves, which the author attributes to the
dissipation of the Jiang–Shu weights; WCNS-T resolves them, its 11th order equal to its 9th. On
[double Mach reflection](/benchmarks/double-mach-reflection.md) at $1024\times256\times5$ WCNS-JS shows no
Kelvin–Helmholtz roll-up of the slip line at any order, WCNS-T increasingly more with order up to the
9th; at 11th order the wavy structures vanish, "probably caused by the first-order interpolation" of
the fallback; at $2048\times512\times5$ the small scales grow with order up to the 11th (Figs. 7–9). In
Pirozzoli's [approximate dispersion relation](/definitions/approximate-dispersion-relation.md), WCNS-T
is better than WCNS-JS but "not so different", and orders 5 to 11 nearly coincide (Fig. A.1), which the
author reads as an open question of the weight formulation. The conclusion: high order works "on the
premise that a suitable grid resolution is being satisfied", and $q$ and $C_T$ need tuning, as in
[adaptive TENO](/methods/adaptive-teno.md) (§4).

## Optimized dispersion and adaptive dissipation (WCNS-SA)

Zhou, Ding, Huang & Luo (2023) build an explicit six-point WCNS for single- and two-species Euler
flows whose spectral properties are optimized with the nonlinear weights included.

**Differencing.** Deng et al.'s sixth-order explicit midpoint-and-node-to-node (MND) scheme (§2.2,
Eq. (5)),

$$\partial_xf\big|_i\approx\frac{64}{45\Delta x}\big(\tilde f_{i+1/2}-\tilde f_{i-1/2}\big)-\frac2{9\Delta x}\big(f_{i+1}-f_{i-1}\big)+\frac1{180\Delta x}\big(f_{i+2}-f_{i-2}\big),$$

with HLLC midpoint fluxes $\tilde f_{i\pm1/2}$ and nodal fluxes $f_j$. *(Compiler check, not in the
sources: this is the HCS of the WCNS-IS section with $\Psi=\tfrac{64}{45}$, for which the
$f_{i\pm3}$ coefficient vanishes.)* Citing Deng et al. and Nonomura & Fujii, the authors state that for
fifth- or higher-order differencing its type has weak influence on resolution, and that the spectral
properties of a WCNS are "mainly determined by the interpolation scheme" (§2.2), so only the
interpolation is optimized.

**Interpolation.** Freeing the first and last coefficients of the sixth-order central interpolant on
$\{i-2,\dots,i+3\}$ gives a fourth-order interpolation with a dispersion parameter $\eta_{\mathrm Z}$ and
a dissipation parameter $\xi_{\mathrm Z}$ (page-local; the source's $\eta$, $\xi$; Eq. (20)):

$$u_{i+1/2}=\tfrac{\eta_{\mathrm Z}+\xi_{\mathrm Z}}2u_{i-2}-\big(\tfrac32\eta_{\mathrm Z}+\tfrac52\xi_{\mathrm Z}+\tfrac1{16}\big)u_{i-1}+\big(\eta_{\mathrm Z}+5\xi_{\mathrm Z}+\tfrac9{16}\big)u_i+\big(\eta_{\mathrm Z}-5\xi_{\mathrm Z}+\tfrac9{16}\big)u_{i+1}-\big(\tfrac32\eta_{\mathrm Z}-\tfrac52\xi_{\mathrm Z}+\tfrac1{16}\big)u_{i+2}+\tfrac{\eta_{\mathrm Z}-\xi_{\mathrm Z}}2u_{i+3},$$

sixth-order central for $(\eta_{\mathrm Z},\xi_{\mathrm Z})=(\tfrac3{128},0)$ and fifth-order upwind for
$\eta_{\mathrm Z}=\xi_{\mathrm Z}=\tfrac3{128}$. With MND differencing the dispersion depends on
$\eta_{\mathrm Z}$ only and the dissipation on $\xi_{\mathrm Z}$ only (Eq. (24)). *(Compiler check, not
in the sources: the printed modified wavenumber is exactly that of the
[MDCD scheme](/methods/mdcd-scheme.md) with $c_{\mathrm{disp}}=\tfrac{64}{45}\eta_{\mathrm Z}$,
$c_{\mathrm{diss}}=\tfrac{64}{45}\xi_{\mathrm Z}$.)* The interpolation is split into the three-point
candidates on $\{i-2,i-1,i\}$, $\{i-1,i,i+1\}$, $\{i,i+1,i+2\}$ and the downwind $\{i+1,i+2,i+3\}$ with
parameter-dependent linear weights (Eq. (27))

$$d_0=\tfrac43(\xi_{\mathrm Z}+\eta_{\mathrm Z}),\quad d_1=\tfrac{20}3\xi_{\mathrm Z}-\tfrac43\eta_{\mathrm Z}+\tfrac12,\quad d_2=-\tfrac{20}3\xi_{\mathrm Z}-\tfrac43\eta_{\mathrm Z}+\tfrac12,\quad d_3=\tfrac43(\eta_{\mathrm Z}-\xi_{\mathrm Z}),$$

and Wong & Lele's localized-dissipation weights $\alpha_k=d_k\big(C+(\tau_6/(\beta_k+\epsilon))^q\big)$,
$\epsilon=10^{-40}$, Jiang–Shu indicators of the interpolation polynomials, the six-point
[WENO-CU6](/methods/weno-cu6.md) indicator for the downwind candidate and
$\tau_6=|\beta_3-\tfrac18(\beta_0+6\beta_1+\beta_2)|$ (§2.3, Eqs. (12)–(18);
[smoothness indicators](/definitions/smoothness-indicator.md)). Characteristic-wise primitive variables
are interpolated, with a first-order fallback where an interpolated density or pressure could be
negative (§2.2–2.3).

**Two-step optimization** (§4):

1. $\eta_{\mathrm Z}$ minimizes Sun et al.'s weighted dispersion error
   $\int_0^\pi e^{-\nu_{\mathrm w}\vartheta}(\tilde\vartheta_r-\vartheta)^2d\vartheta$ (page-local weight
   exponent $\nu_{\mathrm w}$), evaluated not by linear Fourier analysis but by the
   [approximate dispersion relation](/definitions/approximate-dispersion-relation.md) of the full
   nonlinear scheme. The optimum depends on $(C,\xi_{\mathrm Z})$ for small $C$ (0.0675 and 0.0539 at
   $C=10$ for $\xi_{\mathrm Z}=0$ and $\tfrac3{128}$) and becomes independent of $\xi_{\mathrm Z}$ near
   $C=10^9$, where $\eta_{\mathrm Z}=0.0385$ (Table 2). The resulting WCNS-opt keeps the linear
   dispersion up to $\vartheta\approx1.6$, against about 1.25 for WCNS-LD (Wong & Lele) and ONL6 (Jin et
   al.), which the authors read as "completely" remedying the dispersion loss of the nonlinear mechanism
   (§4.1, Figs. 4–5). For the linear scheme the optimal values for $\nu_{\mathrm w}=4,\dots,8$ are
   $0.0502$, $0.0432$, $0.0384$, $0.0350$, $0.0326$ (Table 1). *(Compiler check, not in the sources:
   $\nu_{\mathrm w}=8$ gives $c_{\mathrm{disp}}=\tfrac{64}{45}\cdot0.0326=0.0464$, the MDCD value 0.0463783
   of Sun et al.)*
2. $C$ and $\xi_{\mathrm Z}$ follow Li et al.'s second-derivative [scale sensor](/definitions/scale-sensor.md):
   $C=2\times10^{10}$ and $\xi_{\mathrm Z}=0.0002$ where the sensor is below 0.5; $C=2\times10^8$ and
   $\xi_{\mathrm Z}$ from 0.0075 rising to 0.028 above it (Eqs. (31)–(32), Table 3). The design target is
   an "idealized" dissipation curve, zero below the critical wavenumber and rising steeply beyond it; the
   authors argue that Hu et al.'s dispersion–dissipation condition gives "insufficient dissipation at the
   high-wavenumber region" (§4.2–4.3, Fig. 7; [numerical dissipation](/definitions/numerical-dissipation.md)).

For two species the scheme is combined with Abgrall & Karni's double-flux algorithm, each interface flux
computed twice with the frozen $\gamma$ of the two neighbouring cells (Eq. (33);
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).

**Evidence** (all numerical and comparative, no convergence-order test; §5): on Sod, two-species Sod,
Lax and [Shu–Osher](/benchmarks/shu-osher-problem.md), WCNS-SA gives the thinnest discontinuities
(measured by $\Delta\rho/\max_j|\rho_{j+1}-\rho_j|$), with WCNS-LD overshooting at the Lax contact and
near Shu–Osher shocklets and ONL6 damping the post-shock waves; on the
[2-D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) WCNS-LD and WCNS-SA give more
vortices but more post-shock noise than ONL6; on [double Mach reflection](/benchmarks/double-mach-reflection.md)
($960\times240$), [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) WCNS-SA resolves more small
structure. In the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) WCNS-SA on $64^3$ preserves
kinetic energy better than ONL6 and WCNS-LD on $128^3$, is "nearly identical" to TENO8 at $128^3$, and
alone matches Brachet's dissipation rate at $\mathrm{Re}=100$–400. One thousand steps of the supersonic
Taylor–Green vortex on 32 MPI cores (Xeon Gold 6154) cost 4592 s, 4630 s and 4713 s for ONL6, WCNS-LD and
WCNS-SA (Table 4).

## Staggered multi-resolution WCNS with conservative closures (WCNS-MR)

Qin, Chen, Lin & Deng (2023) use a fifth-order WCNS whose interior interpolation is multi-resolution
(nested 1-, 3- and 5-point stencils, Z-type weights, scaled derivative-sum indicators) and whose
differencing uses only interface fluxes, six-point sixth order inside and five-point fourth order at the
first and last two solution points, on a grid with moved "conservative solution points"; one-sided
nested stencils close the interpolation at block boundaries. They choose WCNS for its free-stream
preservation and its freedom in the flux function (§1). The construction and its tests are on
[shock-capturing boundary closure](/methods/shock-capturing-boundary-closure.md) and
[multi-resolution WENO](/methods/multi-resolution-weno.md).

## Staggered WCNS with exponential weights (WCNS-EXP)

Chen & Deng (2023, §2) use a fifth-order WCNS on a staggered layout: solution points at the cell
centres, flux points at the interfaces, with the domain ends at flux points, which the authors say
avoids special treatment at a corner such as that of the forward-facing step. The interpolation is the
point-value one with weights $(\tfrac1{16},\tfrac58,\tfrac5{16})$ and point-value indicators (Eqs. (14)–(16)); the
interface flux is Roe's; variables are interpolated characteristic-wise; SSP-RK3 at CFL 0.6. The
differencing, after Nonomura & Fujii, mixes interface fluxes $\hat f_{i\pm1/2}$, $\hat f_{i\pm3/2}$ and
nodal fluxes $f_{i\pm1}$ (Eqs. (5)–(6)):

$$\partial_xf\big|_i\approx\frac1{\Delta x}\Big[\tfrac32\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)-\tfrac3{10}\big(f_{i+1}-f_{i-1}\big)+\tfrac1{30}\big(\hat f_{i+3/2}-\hat f_{i-3/2}\big)\Big],$$

sixth order with error $\tfrac1{8960}\partial_x^7f\,\Delta x^6$ *(compiler check, not in the sources: a
Taylor expansion confirms it)*, and "more robust" than the scheme with interface fluxes only because of
its lower resolution. Their new weights, $d_k\exp(-\beta_k^{\lambda_{\mathrm E}}/\lambda_{\mathrm E})$ with a
stencil-local exponent, keep fifth-order interpolation at critical points of any order; with them the
scheme is WCNS-EXP, about 1.2–1.34 times WCNS-JS in cost and much cheaper than WCNS-MR; it needs a
first-order fallback on negative density or pressure in double Mach reflection and the forward-facing
step ([exponential weights](/methods/exponential-nonlinear-weights.md)). They credit WCNS with an easier
free-stream preservation on curvilinear grids when the metrics are discretized by the symmetric
conservative metric method, and with more choices of numerical flux (§1;
[free-stream preservation](/properties/free-stream-preservation.md)).

## Hybrid multi-resolution WCNS

Wang, Zhu, Wang & Zhao (2023c, §3) build a fifth-order explicit WCNS for Euler and Navier–Stokes flows
with interface-only differencing,

$$\partial_xf\big|_i\approx\frac1{\Delta x}\Big[\tfrac{75}{64}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)-\tfrac{25}{384}\big(\hat f_{i+3/2}-\hat f_{i-3/2}\big)+\tfrac3{640}\big(\hat f_{i+5/2}-\hat f_{i-5/2}\big)\Big]$$

(Eq. (3.4), the explicit member, with compact coefficient zero, of a compact family; they prefer it to the tridiagonal implicit
member for cost), Lax–Friedrichs midpoint fluxes "from the perspective of stability and computational
efficiency", characteristic-wise interpolation and TVD-RK3 at CFL 0.6. *(Compiler check, not in the
sources: the formula is sixth order, leading error $\tfrac5{7168}\partial_x^7f\,\Delta x^6$.)* The
interpolation is a simplified multi-resolution one on nested 5-, 3- and 1-point stencils
([multi-resolution WENO](/methods/multi-resolution-weno.md)), and a parameter-free switch uses the linear
five-point value wherever the derivative of the five-point interpolant has no extreme point inside the
stencil ([hybrid schemes](/methods/hybrid-weno.md)). The scheme costs 0.81–1.07 times WENO-JS, against
1.50–2.31 for the MR-WCNS of Zhang, Wang & Zhang (Table 5.1). The authors recall that the
node-to-midpoint interpolation "dominates" the resolution of WCNS (§1, §3), the view also stated by
Zhou et al. above.

## Members recalled in the sources

- **WCNS-JS and WCNS-Z**: interpolation weighted with Jiang–Shu or WENO-Z weights; WCNS-Z beats
  WCNS-JS (Fu 2023, §3.7).
- **TCNS** (targeted compact nonlinear schemes): WCNS with the [TENO](/methods/targeted-eno.md)
  weighting (incremental stencils, sharp cut-off). TCNS "clearly beat" WCNS-Z; TCNS6 is better than
  seventh- and ninth-order WCNS-Z on the Shu–Osher problem, and TCNS is insensitive to the definition of
  the global indicator $\tau_K$, which mainly affects cost; a TCNS with adaptive dissipation exists
  (Fu 2023, §3.7, §4.1; [adaptive TENO](/methods/adaptive-teno.md)).
- **WCNS-T** (Hiejima): fifth-, seventh-, ninth- and eleventh-order WCNS with TENO weighting (Fu 2023,
  §3.7; also cited by Ye et al., §1); described in the section above.
- **Further members** recalled by Hiejima (2022, §1, §2.3): Nonomura & Fujii's robust explicit
  formulation with ninth-order interpolation, Yan et al.'s seventh-order scheme with Y-type weights
  on the fifth-order stencil, the compact high-resolution interpolation of Subramaniam, Wong & Lele
  (lower dispersion error), and the TCNS of Zhang, Zhang & Xu, TENO stencil selection in fifth-order
  WCNS for optimal linear interpolation in smooth regions; and Hiejima's own earlier interpolation on
  uniform substencils, which "requires strong suppression of numerical oscillations".
- **WCNS-LD and ONL6**: Wong & Lele's localized-dissipation WCNS and Jin et al.'s optimized nonlinear
  six-point WCNS, the comparators of WCNS-SA on the same six-point stencil; Zhou et al. (2023, §1, §4)
  fault ONL6 for a linear optimization that ignores the nonlinear weights, and WCNS-LD for a
  dissipation that "decreases evidently when $\vartheta>2.4$" (Fig. 7b).
- **WCNS7M**: the seventh-order explicit WCNS of Chamarthi (2023b, §3, Eqs. (42)–(49)), the comparator
  of [gradient-based reconstruction](/methods/gradient-based-reconstruction.md): four four-point
  candidates with linear weights $(\tfrac1{64},\tfrac{21}{64},\tfrac{35}{64},\tfrac7{64})$, Jiang–Shu-type
  weights with exponent 2 passed through the Henrick mapping ([mapped WENO](/methods/mapped-weno.md)),
  conservative-variable interpolation, HLLC, and eighth-order midpoint-to-node differencing
  $\frac1{\Delta x}\big[\tfrac{1225}{1024}(\tilde f_{i+1/2}-\tilde f_{i-1/2})-\tfrac{245}{3072}(\tilde f_{i+3/2}-\tilde f_{i-3/2})+\tfrac{49}{5120}(\tilde f_{i+5/2}-\tilde f_{i-5/2})-\tfrac5{7168}(\tilde f_{i+7/2}-\tilde f_{i-7/2})\big]$.
  It fails on the 1-D [Sedov](/benchmarks/sedov-blast-wave.md) problem and costs 1.38–1.97 times
  MEG7-prim (Ex. 3.3, Table 2). *(Compiler check, not in the sources: the four candidates with these
  weights give the seven-point interpolant $\tfrac1{1024}(-5,42,-175,700,525,-70,7)$ once the third
  candidate is corrected as in the Qualifications.)*
- **Learned variants**: WCNS3-NN and WCNS3-MR-NN, to which Huang et al. (2026, §7) claim their
  diagram-fitting method applies ([learned WENO weights](/methods/learned-weno-weights.md)).
- **Earlier multiphase use**: Wong & Lele applied WCNS to the five-equation model for mixtures of ideal
  gases only (as recalled by Wong et al. 2021, §1).

## Stated weaknesses and neighbours

- Fu (2023, §3.7) names "the lack of conservation" as "the main flaw of WCNS family schemes", although
  their "spectral property is typically better than the WENO counterpart"; see Contradictions.
- Hiejima (2022, §1) states, without citation or test, that WCNS can use any numerical flux, is
  "easy to apply … to general coordinates, in contrast to the WENO scheme", and "slightly outperforms
  the WENO scheme with the same order of accuracy" in resolution, but "is less robust than the WENO
  because the results of the former can sometimes blow up, i.e., the interpolated pressure or density
  becomes negative"; and that "almost all methods with multipoint interpolation above the seventh
  order of accuracy cause spurious oscillations near strong discontinuities".
- **CRWENO** (Ghosh and Baeder, as recalled by Fu 2023, §3.7): compact reconstruction WENO, with lower
  dissipation than WENO at low and moderate wavenumbers and higher dissipation at aliased wavenumbers;
  a TENO variant exists.
- **Cost against finite volumes.** Wong et al. (2021, §4.3), citing Sebastian & Shu, state that
  explicit FD-WENO and WCNS are "four times cheaper in 2D and nine times cheaper in 3D" than
  finite-volume WENO, because they avoid multi-dimensional reconstruction; the factor is relayed, and
  the paper prints no timing for it.

- Zhou et al. (2023, §1–§2.2) state that interpolation-based schemes such as WCNS can use both flux-vector
  and flux-difference splitting "while reconstruction-based schemes can only take the flux vector
  splitting technique", that flux-vector splitting in curvilinear coordinates "contains grid metrics and
  cannot be split into two upwind parts, violating the geometric conservation law", that traditional WCNS
  "may yield negative density or pressure during the nonlinear interpolation process, and thus shows less
  robustness than WENO", and that WCNS is "still too dissipative to resolve full-scale turbulence";
  Chamarthi (2023b, §3) that WCNS, "unlike the WENO schemes", admits any approximate Riemann solver; Qin
  et al. (2023, §1) that it is free-stream preserving. These agree with Wong et al. and Hiejima above on the
  freedom of the flux; the alternative formulation is interpolation-based in Zhou's sense
  ([alternative WENO](/methods/alternative-weno.md)).

## Qualifications

- The equivalence of AFWENO and HWCNS is relayed from a cited conference paper, not derived in an
  ingested source.
- Wong et al. (2021) read is the arXiv v1 preprint; the value of $\epsilon$ in the WCNS-IS weights is
  not printed.
- Wong et al.'s statement about Riemann solvers in FD-WENO does not cover the alternative
  formulation; see the Qualifications of [alternative WENO](/methods/alternative-weno.md).
- **Order of Hiejima's schemes.** The orders 5 to 11 are interpolation orders. *(Compiler check, not
  in the sources: with no step 3, the plain difference of exact interface fluxes is
  $\partial_xf(x_i)+\tfrac{\Delta x^2}{24}\partial_x^3f(x_i)+O(\Delta x^4)$, so the spatial operator is
  formally second order for point values, the limit Wang et al. 2023b state for an uncorrected
  two-point flux in finite differences; see
  [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md).)*
  The paper shows no convergence test that could confirm or refute the higher order.
- Chamarthi (2023b, Eq. (42)) prints the third WCNS7M candidate as
  $-\tfrac1{16}u_{i-1}+\tfrac9{16}u_i+\tfrac9{16}u_{i+1}+\tfrac1{16}u_{i+2}$, whose coefficients sum to
  $\tfrac{18}{16}$; the four-point Lagrange interpolant has $-\tfrac1{16}$ on $u_{i+2}$ *(compiler check, not in
  the sources)*. The other three candidates are printed correctly. Chamarthi's $IS_k$ (Eq. (46)) lacks the square of
  the inner sum, and its coefficients are not given; the mapping slip is recorded on
  [mapped WENO](/methods/mapped-weno.md).
- Zhou et al. (2023) never print the exponent $q$ of their weights, nor the weight exponent of the
  optimization behind Table 2 and WCNS-opt (the large-$C$ value 0.0384 matches the linear optimum at
  exponent 6), nor the variable fed to the sensor; they reuse $r$ for the stencil half-width and the
  parameter of Hu et al.'s condition. Optimizing $\eta_{\mathrm Z}\ne\tfrac3{128}$ makes the interpolation
  fourth order; the scheme is a six-point, not a sixth-order, WCNS.
- Hiejima (2022) prints "$c^{(k)}_{2,i+54}$" for $c^{(k)}_{2,i+5}$ in a header of Table 5, and the
  index ranges of Eqs. (11)–(12) and (24) hold only for the widest substencils or for $K=7$. In the
  double Mach reflection the text calls the at-rest state $(1.4,0,0,0,1)$ "post-shock" and imposes it
  at the inflow, while Eq. (29) assigns it to the region ahead of the right-moving shock and the
  compressed state $(8,\dots,116.5)$ to the region behind it; the consistent set-up has the latter as
  the post-shock and inflow state.

## Contradictions

**Conservation of WCNS.** *Open.* [Fu (2023)](/sources/fu-2023.md) (§3.7) states that "the main flaw
of WCNS family schemes is the lack of conservation". [Wong et al. (2021)](/sources/wong-2021.md)
(§4.1, citing Subramaniam, Wong & Lele 2019) state that "any central explicit or compact finite
difference scheme can be rewritten into the flux-difference forms", give the implied interface flux of
their explicit WCNS (Eq. (80)), and call the resulting scheme and its limiters "discretely
conservative for all conservative equations" (Abstract, §5.2). The two statements meet on the compact
form: Fu's sentence closes a passage that describes WCNS as "the WENO-like nonlinear node-to-interface
variable interpolation and the high-order compact scheme for interface-to-node differencing" (Deng &
Zhang 2000), and Wong et al.'s sentence covers "any central explicit or compact" scheme. The conflict is
therefore genuine and is not a difference between an explicit and a compact WCNS. Fu gives no
mechanism and cites no specific scheme in that sentence; Wong et al. derive the implied flux only for
their explicit HCS and relay the compact case from the uningested Subramaniam et al. [Qin, Chen, Lin & Deng (2023)](/sources/qin-2023.md) (§1–§2, Eqs. (3)–(5), §4) add a third
statement: their staggered fifth-order WCNS, with explicit interface-to-node differencing on interface
fluxes only and moved "conservative solution points", "is globally conservative" and satisfies a discrete
identity whose quadrature weights differ from 1 at the first and last two points, as proved by Deng & Chen
(2018, not ingested). The statement concerns explicit differencing and a weighted rather than plain sum; Qin et al.
say nothing about compact differencing or about Fu's claim. What would
decide it: a derivation, for the original compact (implicit) interface-to-node differencing with its
boundary closures, of whether a local telescoping interface flux exists, or the identification of the
WCNS variants Fu's statement refers to. *(Compiler check, not in the sources, and not a resolution: Coppola & Veldman 2023,
Lemma A.1, show on the [local conservation](/results/local-conservation-flux-form.md) page that a
globally conservative periodic discretization always factors as a flux difference, which supports Wong
et al. for periodic grids only.)*

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.7: three-step WCNS, WCNS-Z, TCNS, WCNS-T, CRWENO, conservation remark; §4.1.
- [Wong et al. (2021)](/sources/wong-2021.md) — Abstract; §1; §3.3; §4.1, Eqs. (73)–(82); §4.2; §4.3, Eqs. (84)–(101); §5, Algorithms 1–6; §6, Table 4; Apps. A–B.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1, §5: AFWENO similar to WCNS, equivalent to HWCNS; WCNS-T cited.
- [Huang et al. (2026)](/sources/huang-2026.md) — §7: WCNS3-NN, WCNS3-MR-NN.
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — App. A.1, Lemma A.1 (compiler check only).
- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — §1; §2.2–2.3, Eqs. (5)–(18); §3, Eqs. (19)–(26), Table 1; §4, Eqs. (27)–(33), Tables 2–3, Figs. 4–7; §5, Table 4.
- [Qin, Chen, Lin & Deng (2023)](/sources/qin-2023.md) — §1; §2, Eqs. (3)–(5); §4: staggered WCNS-MR, global conservation.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §3, Eqs. (42)–(49), Table 2; Ex. 3.3: WCNS7M.
- [Chen & Deng (2023)](/sources/chen-2023.md) — §1; §2, Eqs. (1)–(16); §4, Table 1: staggered WCNS-EXP.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §1; §3, Eqs. (3.2)–(3.24); §5, Table 5.1: hybrid MR-WCNS.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1; §2.2, Eq. (5); §§2.3–2.6, Eqs. (6)–(25), Tables 1–6, Fig. 1; §3, Figs. 2–9; §4; App., Fig. A.1: WCNS-T and WCNS-JS at orders 5–11.
