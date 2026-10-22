---
type: Method
title: "Alternative WENO (A-WENO)"
description: "The alternative formulation of finite-difference WENO evaluates a two-point finite-volume flux on WENO-interpolated interface states and adds a Taylor series of even-order flux derivatives, so that any monotone, Riemann-solver or central-upwind flux and any set of variables can be used while keeping the high order of the conservative finite-difference scheme."
status: established
aliases: [A-WENO, AFWENO, alternative formulation of WENO, alternative flux formulation, Jiang–Shu–Zhang scheme]
tags: [weno, finite-difference, numerical-flux, reconstruction, multiphase]
timestamp: 2026-10-22T20:00:00Z
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

Ye et al. (2022, §3.2) and Zheng, Shu & Qiu (2021, §2.1) recall from Jiang et al. that the
corrections carry at least $\Delta x^2$ and contribute little to oscillations, so low-order central differences of the physical fluxes, without
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

## Two-medium flows: interpolating primitive variables

The freedom to interpolate any variables is the point of Zheng, Shu & Qiu (2021), who build a
fifth-order conservative finite-difference scheme for compressible two-medium flows (gas–gas,
gas–water with a stiffened-gas law) on this formulation:

- **Why this formulation.** Reconstructing fluxes or conserved variables across a material interface
  puts jumps in every component and spoils the continuity of $v$ and $p$; classical flux-reconstruction
  FD cannot interpolate primitive variables, and the alternative formulation can (§1). They also state
  that finite-volume schemes above second order cannot, a claim limited in the Qualifications below.
- **Interpolation.** Fifth-order WENO interpolation with position-dependent linear weights of the
  primitive variables $(\rho,v,p)$, in the local characteristic fields of the primitive quasilinear
  system, with explicit $R$ and $L$ (§2.2.4, §3.1.3;
  [characteristic decomposition](/methods/characteristic-decomposition.md),
  [WENO-JS](/methods/weno-js-reconstruction.md)); each fluid keeps its own nodal values and stencils
  take those of the fluid where the flux is evaluated.
- **Flux.** Global [Lax–Friedrichs](/methods/lax-friedrichs-flux.md) $h$ plus the two corrections,
  multiplied near the interface by a smooth discontinuity indicator $\varphi_{i+1/2}\in[0,1]$
  (page-local; Eq. (6)):
  $\hat f^{\mathrm H}_{i+1/2}=h(u^-_{i+1/2},u^+_{i+1/2})-\varphi_{i+1/2}\big(\tfrac1{24}\Delta x^2(\partial^2_xf)_{i+1/2}-\tfrac{7}{5760}\Delta x^4(\partial^4_xf)_{i+1/2}\big)$.
  Proposition 2.1: the flux difference is fifth order if $\varphi=1+O(\Delta x^3)$; with the
  interface treatment, $\varphi=1+O(\Delta x^5)$ and $\Delta t=O(\Delta x^r)$, $r\le2$, are needed
  (Propositions 2.2–2.3), and the indicator, built from WENO-Z-type differences of
  [smoothness indicators](/definitions/smoothness-indicator.md), satisfies $\varphi=1+O(\Delta x^6)$ on
  smooth data and $O(\Delta x^4)$ near a jump (App. B;
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
- **Interface.** A [level set](/methods/level-set-method.md) locates the interface; cells next to it
  are merged, a low-order interface flux from an ALE-type space–time balance with the interface flux
  $(0,p,vp)$ is blended with the high-order one by $\varphi$, and the updated mixed-cell value is
  redistributed to the two fluids, again blended by $\varphi$. The final update is a single
  flux difference from $u^n$, hence conservative
  ([conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)).

Results: fifth order on 1-D and 2-D Burgers-reducible artificial-interface tests ($L_1$ order 5.14 at
$N=320$, 5.06 at $320^2$; Tables 2, 4), sixth-order convergence of $\varphi$ (Table 3), velocity and
pressure deviations near $10^{-11}$–$10^{-10}$ on a moving contact against $10^{-4}$–$10^{-3}$ for
conservative-variable WENO-JS (Fig. 6), correct wave positions where a finite-difference WENO
ghost-fluid method misplaces them (Fig. 8), and no spurious interface jump on a gas–water Riemann
problem where WENO-JS produces one (Fig. 11) ([gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md),
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)). CFL 0.5, SSP-RK3 assembled so that
each stage is one conservative update from $u^n$ ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## Non-conservative systems: path-conservative central-upwind A-WENO

Chu, Kurganov & Na (2022) extend A-WENO to systems with non-conservative products,
$\partial_tu+\partial_xf(u)+\mathcal C(u)\partial_xu=0$ (they write $+B(u)\partial_xu$ on the
right-hand side, $B=-\mathcal C$), with the second-order finite-volume path-conservative
central-upwind (PCCU) scheme of Castro Díaz, Kurganov & Morales de Luna (2019) as the two-point part
([path-conservative schemes](/methods/path-conservative-scheme.md),
[central-upwind schemes](/methods/central-upwind-scheme.md)).

- **Global flux.** The system is read as $\partial_tu+\partial_xK(u)=0$ with
  $K(u)=f(u)+\int^x\mathcal C(u)\,\partial_\xi u\,d\xi$ (page-local $K$; §4), and the A-WENO flux
  of $K$ is assembled from the PCCU flux and the corrections of $K$. In the registry's sign convention the
  fifth-order scheme reads (Eq. (4.1); page-local $\mathcal B_i$, $\mathcal B_{\Psi,i+1/2}$)
  $$\begin{aligned}\frac{du_i}{dt}=&-\frac1{\Delta x}\Big[h_{i+1/2}-h_{i-1/2}+\mathcal B_i+\frac{a^+_{i-1/2}}{a^+_{i-1/2}-a^-_{i-1/2}}\mathcal B_{\Psi,i-1/2}-\frac{a^-_{i+1/2}}{a^+_{i+1/2}-a^-_{i+1/2}}\mathcal B_{\Psi,i+1/2}\Big]\\&+\frac{\Delta x}{24}\big[(\partial_x^2K)_{i+1/2}-(\partial_x^2K)_{i-1/2}\big]-\frac{7\Delta x^3}{5760}\big[(\partial_x^4K)_{i+1/2}-(\partial_x^4K)_{i-1/2}\big],\end{aligned}$$
  where $h$ is the central-upwind flux of $f$ with one-sided speeds $a^\pm_{i+1/2}$ and the built-in
  anti-diffusion term (a minmod of the differences between $u^\pm_{i+1/2}$ and $u^{\mathrm{HLL}}$),
  $\mathcal B_i=\int_{I_i}\mathcal C(u)\partial_xu\,dx$ is the cell integral and
  $\mathcal B_{\Psi,i+1/2}=\int_0^1\mathcal C(\Psi(s))\Psi'(s)\,ds$ the path integral along the linear
  segment $\Psi$ from $u^-_{i+1/2}$ to $u^+_{i+1/2}$ (Eqs. (2.1)–(2.9), (4.2)). The anti-diffusion term,
  switched off in the 2019 scheme, is kept (§2).
- **Corrections.** $(\partial_x^2K)=(\partial_x^2f)+[\partial_x(\mathcal C\partial_xu)]$ and
  $(\partial_x^4K)=(\partial_x^4f)+[\partial_x^3(\mathcal C\partial_xu)]$, with the six-point formulas
  above for $f$ and, for $g_m=\mathcal C(u_m)(\partial_xu)_m$ (page-local),
  $[\partial_xg]_{i+1/2}=\frac{-g_{i+2}+27g_{i+1}-27g_i+g_{i-1}}{24\Delta x}$ and
  $[\partial_x^3g]_{i+1/2}=\frac{g_{i+2}-3g_{i+1}+3g_i-g_{i-1}}{\Delta x^3}$, the nodal derivatives
  $(\partial_xu)_m$ by five-point one-sided or central differences on $i-2,\dots,i+3$ (§4).
  *(Compiler check, not in the sources: the nodal derivative formulas and $[\partial_xg]$ are exact on
  polynomials up to degree 4, $[\partial_x^3g]$ likewise, i.e. fourth- and second-order accurate.)*
- **Cell integral.** A finite-difference scheme has no piecewise polynomial in $I_i$ on which to
  integrate $\mathcal B_i$, so a new five-point quadrature integrates the product of quartic
  interpolants through $x_{i-1/2},x_{i-1/4},x_i,x_{i+1/4},x_{i+1/2}$ (Eqs. (4.3)–(4.4)); the
  quarter-point values come from fifth-order WENO-Z interpolation with the same three candidates
  and indicators and new linear weights $d_0=\tfrac{15}{64}$, $d_1=\tfrac{21}{32}$, $d_2=\tfrac7{64}$
  at $x_{i-1/4}$ (mirrored at $x_{i+1/4}$). Its fifth order is stated as "easy to show", without
  proof (Remark 4.1). *(Compiler check, not in the sources: these weights combine the three printed
  parabolic values at $x_{i-1/4}$ into the five-point Lagrange interpolant exactly.)*
- **Interpolation.** Fifth-order WENO-Z point-value interpolation with $d=(\tfrac1{16},\tfrac58,\tfrac5{16})$,
  $q=2$, $\epsilon=10^{-12}$ (Eqs. (3.4)–(3.7)), in local characteristic variables of the Roe-averaged
  matrix $A(\hat u)+\mathcal C(\hat u)$, eigenvectors computed numerically (Remarks 6.2–6.3;
  [WENO-Z](/methods/weno-z.md), [characteristic decomposition](/methods/characteristic-decomposition.md)).
  The 2-D scheme is dimension by dimension (Eq. (5.2)).

Applied to the two-layer shallow water equations in the equilibrium variables
$(h_1,q_1,w,q_2)$, $w$ the lower-layer surface (their notation), the scheme is stated to preserve the lake-at-rest
state exactly ([well-balancing](/properties/well-balancing.md)); no proof or round-off test is
given, only perturbation plots (§6.1, Example 2). Observed $L^1$ rates are self-convergence rates
and erratic (7.69, 3.55, 5.01, 5.37 for $h_1+w$; Table 7.1), and at about equal CPU time
(no timings printed) the fifth-order scheme on $\Delta x=1/200$ resolves a 2-D interface problem
better than the second-order PCCU scheme on $1/450$ (Example 6, Fig. 7.10). Chu et al. (§1) motivate
the choice of A-WENO by calling flux-split finite-difference WENO "quite diffusive". Unlike the
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md) of Balsara et al. (2024), the
scheme uses no Riemann solver and claims no stationary-contact preservation.

## Relation to other schemes

- Ye et al. (2022, §1) state that AFWENO "is similar to WCNS and is equivalent to the HWCNS scheme
  under specific parameters" ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)).
- The "WCNS" of Hiejima (2022, §2.2, Eq. (5)) interpolates primitive variables to $x_{i+1/2}$ at
  orders 5 to 11, evaluates an AUSMDV flux on them and takes the plain flux difference, i.e. the
  leading term of the alternative formulation without its corrections; the paper does not cite
  the alternative formulation. *(Compiler check, not in the sources: the plain difference of exact interface fluxes is
  $\partial_xf(x_i)+\tfrac{\Delta x^2}{24}\partial_x^3f(x_i)+O(\Delta x^4)$, so such a scheme is formally
  second order for point values, consistent with Wang et al.'s statement above; Hiejima shows no
  convergence test.)*
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
- **Riemann solvers in finite differences.** Wong et al. (2021, §4.3) write that "a finite difference
  WENO scheme can only be used with flux-vector splitting methods ... when high-order of accuracy is
  desired", since a Riemann solver in an FD WENO scheme "degenerates to only second order", whereas
  a [WCNS](/methods/weighted-compact-nonlinear-scheme.md) keeps high order. Read as a statement about
  flux-reconstruction FD-WENO it agrees with Wang et al. (2023, §1); it does not cover the alternative
  formulation, which they do not cite and which Ye et al. (2022, HLLC) and Zheng, Shu & Qiu (2021,
  Lax–Friedrichs on WENO-interpolated states) run at fifth order.
- Zheng, Shu & Qiu (2021, §1) state that finite-volume methods above second order cannot interpolate
  primitive variables, because only cell averages of conserved variables are available. Finite-volume
  schemes of the bundle above second order do reconstruct primitive or characteristic variables
  (Tsoutsanis et al. 2021, Bryngelson et al. 2021; see [CWENO](/methods/cweno.md) and
  [WENO-JS](/methods/weno-js-reconstruction.md)), and neither establishes its order at material
  interfaces.
- Zheng, Shu & Qiu (2021, App. A) need $\Delta t=O(\Delta x^r)$ with $r\le2$ because the low-order
  interface flux, obtained from a space–time balance over one step, carries an $O(\Delta x^{2-r})$
  error, so very small time steps degrade it; their accuracy tests use $\Delta t=O(\Delta x^{5/3})$.
- Chu et al. (2022) print the convergence rate without the logarithm (p. 12; Table 7.1 gives
  $\log_2$ of the error ratios), label Table 7.1's rows by the finer grid of each pair against their
  printed definition, write $u^-_{j+1/2}$ for $\phi^-_{j+1/2}$ in the derivative of the quartic
  interpolant (p. 7), print two vanishing differences in the $y$-path integral $C^{(6)}$ (p. 11), and
  a positive exponent in the bottom of Example 9.
- Ye et al. (2022) print sign errors in rows of their central-coefficient Tables 3 and 5: the
  six-point second-derivative row of Table 3 reads $(34,-39,5)/48$ for the pairs
  $(c_i,c_{i+1}),(c_{i-1},c_{i+2}),(c_{i-2},c_{i+3})$, the negative of the exact coefficients given
  above. They also print $F'(x_{i+1/2})$ for $\partial_xf$ at $x_i$ in Eq. (11). Their Appendix
  Eq. (A.25) carries correct signs.

# Citations

- [Ye et al. (2022)](/sources/ye-2022.md) — §1; §2.1; §3.1–3.2, Eqs. (11)–(23), Tables 3–6; §4, Tables 7–8, 13; §4.9; App., Eqs. (A.1)–(A.26).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1; §2, Eqs. (2)–(4), Remarks 1–3; §3; §4.4, Table 1.
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §1; §2.1–2.3, Eqs. (1)–(27), Propositions 2.1–2.3; §3; §4, Tables 2–4, Figs. 6–15; Apps. A–B.
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3.
- [Chu, Kurganov & Na (2022)](/sources/chu-2022.md) — §1; §§2–5, Eqs. (2.1)–(5.2), Remark 4.1; §6, Remarks 6.1–6.3; §7, Table 7.1, Figs. 7.3, 7.10.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §2.2, Eq. (5).
