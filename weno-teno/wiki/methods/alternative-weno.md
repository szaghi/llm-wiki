---
type: Method
title: "Alternative WENO (A-WENO)"
description: "The alternative formulation of finite-difference WENO evaluates a two-point finite-volume flux on WENO-interpolated interface states and adds a Taylor series of even-order flux derivatives, so that any monotone, Riemann-solver or central-upwind flux and any set of variables can be used while keeping the high order of the conservative finite-difference scheme."
status: established
aliases: [A-WENO, AFWENO, alternative formulation of WENO, alternative flux formulation, Jiang–Shu–Zhang scheme]
tags: [weno, finite-difference, numerical-flux, reconstruction]
timestamp: 2026-10-21T12:00:00Z
---

# Alternative WENO (A-WENO)

The alternative formulation of finite-difference WENO (Jiang, Shu & Zhang 2013, built on the
alternative flux expansion of Shu & Osher 1988, as recalled by Ye et al. 2022, §3.1, and Wang et al.
2023, §2) keeps the [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
on point values $u_i$ but constructs the flux differently. Instead of reconstructing split point
fluxes, it **interpolates** left and right states $u^\mp_{i+1/2}$ at $x_{i+1/2}$ with WENO and writes

$$\hat f_{i+1/2}=h\big(u^-_{i+1/2},u^+_{i+1/2}\big)+\sum_{\ell=1}^{\lfloor(\mathcal K-1)/2\rfloor}b_{2\ell}\,\Delta x^{2\ell}\Big(\frac{\partial^{2\ell}f}{\partial x^{2\ell}}\Big)_{i+1/2},$$

with $h$ a two-point numerical flux, $\mathcal K$ the target order and $b_{2\ell}$ the correction
coefficients (page-local; Ye et al.'s $a_{2\ell}$) (Ye et al. 2022,
Eqs. (12)–(13)). The two names in the bundle, "A-WENO" (Wang et al. 2023) and "AFWENO" (Ye et al.
2022), denote this same scheme.

## Correction coefficients

The coefficients come from the requirement that $\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)/\Delta x$
equal $\partial_xf$ at $x_i$: Ye et al. (2022, App., Eqs. (A.15)–(A.17)) derive

$$b_2=-\tfrac1{24},\quad b_4=\tfrac{7}{5760},\quad b_6=-\tfrac{31}{967680},\quad b_8=\tfrac{127}{154828800},\quad b_{10}=-\tfrac{73}{3503554560}.$$

*(Compiler check, not in the sources: these are the Taylor coefficients of
$\tfrac{z/2}{\sinh(z/2)}$, the inverse of the cell-averaging symbol, and were confirmed by series
expansion.)* The fifth-order scheme keeps $b_2$ and $b_4$, with central differences of the point
fluxes $f_j=f(u_j)$ on the six points $i-2,\dots,i+3$ (Wang et al. 2023, Eq. (4)):

$$\begin{aligned}
(\partial_x^2f)_{i+1/2}&\approx\frac{-5f_{i-2}+39f_{i-1}-34f_i-34f_{i+1}+39f_{i+2}-5f_{i+3}}{48\,\Delta x^2},\\
(\partial_x^4f)_{i+1/2}&\approx\frac{f_{i-2}-3f_{i-1}+2f_i+2f_{i+1}-3f_{i+2}+f_{i+3}}{2\,\Delta x^4}.
\end{aligned}$$

*(Compiler check: both formulas are exact on polynomials up to degree 5, i.e. fourth- and
second-order accurate, which is what $\Delta x^2$ and $\Delta x^4$ prefactors need for an
$O(\Delta x^6)$ flux.)* Ye et al. (2022, Tables 3–6; App. Eq. (A.25)) tabulate central coefficients up
to tenth order.

Ye et al. (2022, §3.2) recall from Jiang et al. that the corrections carry at least $\Delta x^2$ and
contribute little to oscillations, so low-order central differences of the physical fluxes, without
characteristic projection or nonlinear weighting, suffice. A purely central approximation "can be
unstable in some problems"; an upwind (flux-split) approximation as in Liu (2017) fixes this but
"increases the computational cost significantly" (Eqs. (19)–(23)).

## The interface flux

Because the leading term is an ordinary two-point flux on interpolated states, A-WENO can use any
monotone flux or (approximate) Riemann solver. In a finite-difference context a standard
finite-volume flux is limited to second order; the high order comes from the corrections (Wang et
al. 2023, §1). The fluxes used in the bundle:

- global Lax–Friedrichs, Steger–Warming and HLLC (Ye et al. 2022, §4; HLLC outperforms Steger–Warming
  in the viscous [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), §4.9)
  ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md), [HLL-family solvers](/methods/hll-riemann-solvers.md));
- Rusanov and the adaptive-diffusion central flux of earlier A-WENO papers, and the adaptive-diffusion
  central-upwind Rankine–Hugoniot flux of Wang et al. (2023, §3), which lowers the numerical
  dissipation in smooth regions and near contacts
  ([adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md),
  [central-upwind schemes](/methods/central-upwind-scheme.md)).

The interpolated variables can be conserved, primitive or characteristic (Ye et al. 2022, Abstract,
§5). Wang et al. (2023, §2) use fifth-order [WENO-Z](/methods/weno-z.md) interpolation, applied
characteristic-wise with a local characteristic decomposition
([characteristic decomposition](/methods/characteristic-decomposition.md)), SSP-RK3 at CFL 0.45, and
add source terms pointwise for balance laws (Remarks 1–2).

## Relation to other schemes

- Ye et al. (2022, §1) state that AFWENO "is similar to WCNS and is equivalent to the HWCNS scheme
  under specific parameters" ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)).
- Ye et al. (2022) replace the WENO interpolation by a TENO interpolation and obtain
  [AFTENO](/methods/afteno.md); they argue that AFWENO is odd-order only and loses every smooth
  candidate when two discontinuities fall in the global stencil, whereas incremental TENO stencils
  keep a smooth third-order candidate (§2.1, Figs. 1–2).

## Measured accuracy and cost

- On $u_t+u_x=0$, $u_0=\sin\pi x$, $t=2$, AFWENO5-LF has $L_1$ error $6.31\times10^{-11}$ at $N_x=640$
  (fifth order), against $7.94\times10^{-11}$ for FD WENO5-JS (Ye et al. 2022, Tables 7–8).
- On the 2-D isentropic vortex Wang et al. (2023, Table 1) report $L^2$ density errors at $\Delta x=1/64$
  of $3.45\times10^{-9}$ (Rusanov-type adaptive central flux) and $3.62\times10^{-9}$ (CURH flux), with
  irregular observed rates (2.36–6.38) that trend to fifth order
  ([isentropic vortex](/benchmarks/isentropic-vortex.md)).
- Cost: on a 2-D Euler density wave, 500 steps, $160\times160$, AFWENO takes 176.86 s against 90.94 s
  for FD TENO5 (Ye et al. 2022, Table 13), i.e. about 1.9 times. Ye et al. (§4.2) attribute the
  extra cost of the interpolation-based family to the two-point flux and the derivative terms, and say
  it buys better free-stream preservation.

## Qualifications

- The free-stream preservation advantage is asserted, never tested, in Ye et al. (2022, §1, §4.2, §5)
  ([free-stream preservation](/properties/free-stream-preservation.md)).
- "Odd order only" is a property of the Jiang–Shu–Zhang WENO interpolation, not of the alternative
  formulation: Ye et al.'s own AFTENO uses the same flux expansion and reaches even orders through
  its incremental stencils (coefficients up to eighth order, Tables 1–2; only fifth order is tested).
- Wang et al. (2023) give no proof that the non-smooth switches (minmod, max/min, smoothness
  detector) inside their two-point flux preserve the formal order; only Table 1 supports it.
- Ye et al. (2022) print sign errors in rows of their central-coefficient Tables 3 and 5: the
  six-point second-derivative row of Table 3 reads $(34,-39,5)/48$ for the pairs
  $(c_i,c_{i+1}),(c_{i-1},c_{i+2}),(c_{i-2},c_{i+3})$, the negative of the exact coefficients given
  above. They also print $F'(x_{i+1/2})$ for $\partial_xf$ at $x_i$ in Eq. (11). Their Appendix
  Eq. (A.25) carries correct signs.

# Citations

- [Ye et al. (2022)](/sources/ye-2022.md) — §1; §2.1; §3.1–3.2, Eqs. (11)–(23), Tables 3–6; §4, Tables 7–8, 13; §4.9; App., Eqs. (A.1)–(A.26).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1; §2, Eqs. (2)–(4), Remarks 1–3; §3; §4.4, Table 1.
