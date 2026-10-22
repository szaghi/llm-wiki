---
type: Method
title: "Fluctuation-form finite-difference WENO for non-conservative systems"
description: "Balsara, Bhoriya, Shu and Kumar write point-value FD-WENO as an interior quasilinear term plus HLL or HLLI fluctuations at zone boundaries; it equals Lax–Friedrichs FD-WENO for linear systems, treats non-conservative products, preserves stationary linearly degenerate jumps and needs one reconstruction per zone."
status: established
aliases: [FD-WENO in fluctuation form, path-conservative FD-WENO, FD-WENO with non-conservative products, HLLI FD-WENO]
tags: [finite-difference, weno, riemann-solver, multiphase, well-balanced]
timestamp: 2026-10-22T20:00:00Z
---

# Fluctuation-form finite-difference WENO for non-conservative systems

Classical finite-difference WENO evolves point values $u_i$ through a conservative flux
difference of reconstructed split point fluxes ([conservative finite-difference
scheme](/definitions/conservative-finite-difference-scheme.md)); it has no place for a
non-conservative product. [Balsara et al. (2024)](/sources/balsara-2024.md) extend
point-value FD-WENO to

$$\partial_tu+\partial_xf(u)+\mathcal C(u)\,\partial_xu=0,\qquad \partial_tu+A\,\partial_xu=0,\quad A=\frac{\partial f}{\partial u}+\mathcal C,$$

with $\mathcal C$ (registry §10) the matrix of non-conservative products (§II, Eqs.
(2.4)–(2.5)), by writing the scheme in fluctuation form. To their knowledge this is the
first FD-WENO for nonlinear systems with non-conservative products (Abstract, §I).

## The scheme

In zone $i$ one WENO reconstruction of the point values, in the characteristic variables of
zone $i$, gives the two zone-boundary states $u^-_{i+1/2}$ (right face of zone $i$) and
$u^+_{i-1/2}$ (left face). An [HLL-type](/methods/hll-riemann-solvers.md) Riemann solver at
each boundary gives a left-going fluctuation $\mathcal D^-_{i+1/2}$ and a right-going one
$\mathcal D^+_{i+1/2}$ (page-local symbols). The update is (§IV, Eq. (4.1))

$$\frac{d}{dt}u_i=-A(u_i)\,\frac{u^-_{i+1/2}-u^+_{i-1/2}}{\Delta x}-\frac1{\Delta x}\Big(\mathcal D^-_{i+1/2}+\mathcal D^+_{i-1/2}\Big):$$

an interior term — the quasilinear matrix at the zone centre times the reconstructed jump
across the zone — plus the boundary fluctuations. Ingredients (§IV, §VI steps 1–7):
reconstruction by [WENO-AO](/methods/weno-ao.md) or multi-resolution WENO, with the fixes of
App. D; $s^-_{i+1/2}$ reset to the minimum and $s^+_{i+1/2}$ to the maximum of the signal
speeds over **all** boundaries of the stencils that contribute to $x_{i+1/2}$, which the
authors state is "needed in order to obtain the order property"; the Riemann solver; SSP
Runge–Kutta in time. Multi-D is dimension by dimension.

**Fluctuations** (§III, Eqs. (3.1)–(3.9), from Dumbser & Balsara 2016). The resolved state
$u^{\mathrm{HLL}}_{i+1/2}$ (registry §10) solves

$$u^{\mathrm{HLL}}=\frac{s^+u^+-s^-u^--\big(f(u^+)-f(u^-)\big)}{s^+-s^-}-\frac{\tilde{\mathcal C}(u^-,u^{\mathrm{HLL}})(u^{\mathrm{HLL}}-u^-)+\tilde{\mathcal C}(u^{\mathrm{HLL}},u^+)(u^+-u^{\mathrm{HLL}})}{s^+-s^-},$$

with $\tilde{\mathcal C}(u_{\mathrm a},u_{\mathrm b})=\int_0^1\mathcal C\big(u_{\mathrm a}+\mathsf s(u_{\mathrm b}-u_{\mathrm a})\big)\,d\mathsf s$
along a straight-line path (page-local path parameter $\mathsf s$), computed by a
few fixed-point iterations started from the single-path state; four-point Gauss–Lobatto
quadrature is "often sufficient". In the subsonic case $\mathcal D^-=s^-(u^{\mathrm{HLL}}-u^-)$,
$\mathcal D^+=s^+(u^+-u^{\mathrm{HLL}})$; if $s^-\ge0$, $\mathcal D^-=0$ and $\mathcal D^+$ is the
full jump term, and conversely if $s^+\le0$ (Eq. (3.6)). With $\mathcal C=0$ these are the
fluctuations of the standard HLL solver.

**HLLI anti-diffusion** (Eqs. (3.7)–(3.9)). The anti-diffusive flux

$$\Phi^{\mathrm{AD}}_{i+1/2}=-\varphi_{i+1/2}\,\frac{s^+s^-}{s^+-s^-}\,R(u^{\mathrm{HLL}})\,\Delta_{\mathrm{AD}}\,L(u^{\mathrm{HLL}})\big(u^+-u^-\big)$$

is added to $\mathcal D^-$ and subtracted from $\mathcal D^+$, so it is conservative.
$\Delta_{\mathrm{AD}}$ is diagonal and gives each field more anti-diffusion the slower its wave,
the most to stationary waves; $\varphi\in[0,1]$ is a flattener, $0$ at shocks (page-local
$\Phi^{\mathrm{AD}}$, $\Delta_{\mathrm{AD}}$, $\varphi$). Only the eigenvectors of linearly
degenerate fields are needed — the others may be zeroed — and all results of the paper avoid
genuinely nonlinear eigenvectors, which for the debris-flow model exist only numerically
(§III).

## Equivalence with Lax–Friedrichs FD-WENO for linear systems

For constant $A$ the high-order upwind scheme

$$\frac{d}{dt}u_i=-A^+\frac{u^-_{i+1/2}-u^-_{i-1/2}}{\Delta x}-A^-\frac{u^+_{i+1/2}-u^+_{i-1/2}}{\Delta x},\qquad A^\pm=\tfrac12(A\pm aI),$$

is stated to reduce identically to the Lax–Friedrichs FD-WENO of Shu–Osher / Jiang–Shu
when the flux is linear (§II, Eq. (2.3)). Adding and subtracting
$A(u^-_{i+1/2}-u^+_{i-1/2})/\Delta x$ and inserting the Lax–Friedrichs limit $s^\pm\to\pm a$
of the fluctuations shows that Eq. (4.1) **is** Eq. (2.3) for linear systems (§V, Eqs.
(5.1)–(5.5)). The authors stress that the equivalence holds only for linear PDEs with the
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md) limit; the accuracy for nonlinear smooth
flow is argued from including all nonlinearity in the Riemann solver and shown numerically.
Eq. (4.1) itself appears, "with slight modification", as a second-order scheme in Dumbser &
Balsara (2016); the claim is that it is genuinely high order (§V).

The naive upgrade with $A_i^\pm=\tfrac12(A(u_i)\pm a_iI)$ (Eq. (2.6)) may keep high order for
mild nonlinearity but, like Eq. (2.3), cannot preserve a stationary contact and is declared
"unacceptable" (§II).

## Claimed advantages

1. **Exact stationary linearly degenerate discontinuities**, from the HLLI anti-diffusion
   ([stationary contact preservation](/properties/stationary-contact-preservation.md)); with
   it the lake-at-rest tests are passed without special modification
   ([well-balancing](/properties/well-balancing.md)).
2. **One reconstruction per zone** instead of two (for the right- and left-going split
   fluxes of Lax–Friedrichs FD-WENO): "half as computationally expensive" if reconstruction
   dominates (§VI, §XI). No timing is reported.
3. Stiff sources are collocated with the point values, so IMEX Runge–Kutta applies directly;
   the paper uses IMEX-SSP3(4,3,3) of Pareschi & Russo (§X; see
   [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## Numerical evidence

- Design orders 3, 5, 7, 9 (WENO-AO-3, (5,3), (7,3), (9,3) and multi-resolution WENO,
  Lax–Friedrichs limit, base CFL 0.3) on the 2D Euler
  [isentropic vortex](/benchmarks/isentropic-vortex.md) (e.g. AO-(9,3): $L_1$ error
  $1.01355\times10^{-10}$ at $384^2$, rate 8.78) and on vortex tests for Baer–Nunziato,
  Pitman–Le debris flow and two-layer shallow water (§VII, Tables I–V).
- Debris-flow Riemann problem 1 (three superposed stationary jumps): preserved "at all
  orders", HLL and Lax–Friedrichs identical, velocity fluctuations below $1.4\times10^{-14}$
  (§VIII.a, Fig. 2). Abgrall test for Baer–Nunziato: pressure deviation below
  $9\times10^{-13}$, velocities below $2\times10^{-13}$ (§VIII.b, Fig. 5).
- [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md) (1000 zones,
  orders 3–7), [forward-facing step](/benchmarks/forward-facing-step.md) ($1440\times480$,
  seventh order) and [double Mach reflection](/benchmarks/double-mach-reflection.md)
  ($1920\times480$); new 2D [shock–bubble](/benchmarks/shock-bubble-interaction.md) and
  [shock–vortex](/benchmarks/shock-vortex-interaction.md) problems for the three
  non-conservative systems (§§VIII.d, IX).

## Relation to the A-WENO path-conservative central-upwind scheme

The priority claim above is the authors' own. In the same corpus
[Chu et al. (2022)](/sources/chu-2022.md) build a fifth-order point-value scheme for
$\partial_tu+\partial_xf(u)=-\mathcal C(u)\partial_xu$ (their $B=-\mathcal C$) by a different
route: the system is written with a global flux $f+\int^x\mathcal C\,\partial_\xi u\,d\xi$, the
[path-conservative](/methods/path-conservative-scheme.md) central-upwind flux of that global flux
is inserted in [A-WENO](/methods/alternative-weno.md), and the cell integral of the
non-conservative product is evaluated by a new five-point quadrature (§4, Eqs. (4.1)–(4.4)).
Both schemes reconstruct (Chu et al.: interpolate) point values in local characteristic
variables — per interface with a Roe-type matrix in Chu et al. (Remarks 6.2–6.3), per zone here —
and use the straight-line path; Chu et al.'s is Riemann-solver-free (only
one-sided speeds) and does not claim stationary-contact preservation, while the HLLI
anti-diffusion here does. Chu et al. motivate A-WENO by stating that the original FD-WENO
"relies on flux splitting, which is quite diffusive" (§1); the present scheme avoids flux
splitting as well. The two papers share the two-layer shallow-water system as a test case.

## Qualifications

- No truncation-error analysis of the nonlinear fluctuation form is given, and discrete
  conservation for nonlinear conservative $f$ is not proved (the interior term is
  non-conservative by itself); mass conservation is shown numerically for Baer–Nunziato
  (Fig. 6g).
- In the Baer–Nunziato Riemann problems the anti-diffusion is switched off, since no good
  flattener exists for that system; the text also says "$\varphi=1$" in the same place, which
  would mean full anti-diffusion — an internal inconsistency of the accepted manuscript
  (§VIII.b).
- Eq. (3.7) uses a speed $S_{i+1/2}$ never defined in the text; the anti-diffusion matrix is
  therefore given here only in words.

# Citations

- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I, §II (Eqs. (2.2)–(2.6)), §III (Eqs. (3.1)–(3.9)), §IV (Eq. (4.1)), §V (Eqs. (5.1)–(5.5)), §VI, §§VII–X, App. D (accepted manuscript).
- [Chu et al. (2022)](/sources/chu-2022.md) — §1, §4 (Eqs. (4.1)–(4.4)), §6; the A-WENO PCCU scheme used for the comparison.
