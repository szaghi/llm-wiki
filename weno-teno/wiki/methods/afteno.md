---
type: Method
title: "AFTENO — alternative-formulation TENO"
description: "AFTENO places a TENO interpolation of point values inside the alternative finite-difference flux formulation, a monotone two-point flux on interpolated states plus even-derivative corrections, so that any Riemann solver and any variable set can be used at arbitrary odd or even order; this page gives its stencils, linear weights, correction coefficients, tested fifth-order performance and cost."
status: established
aliases: [AFTENO, AFTENO5, alternative formulation of targeted ENO, TENO in the AFWENO framework]
tags: [teno, finite-difference, numerical-flux, reconstruction]
timestamp: 2026-10-21T12:00:00Z
---

# AFTENO — alternative-formulation TENO

**AFTENO** ([Ye et al. (2022)](/sources/ye-2022.md)) combines the
[targeted ENO](/methods/targeted-eno.md) stencil selection with the
[alternative formulation of finite-difference WENO](/methods/alternative-weno.md)
(AFWENO, Jiang, Shu and Zhang 2013, as recalled). In that formulation the
conservative flux of the finite-difference scheme
$\frac{d}{dt}u_i=-\frac1{\Delta x}(\hat f_{i+1/2}-\hat f_{i-1/2})$ is not
reconstructed from split point fluxes; it is a two-point flux on interpolated
states plus even-derivative corrections (the Shu–Osher alternative flux
expansion),

$$\hat f_{i+1/2}=h\big(u^-_{i+1/2},u^+_{i+1/2}\big)+\sum_{\ell\ge1}a_{2\ell}\,\Delta x^{2\ell}\Big(\frac{\partial^{2\ell}f}{\partial x^{2\ell}}\Big)_{i+1/2},$$

with $h$ any monotone flux (Lax–Friedrichs, Steger–Warming, HLL, HLLC, Roe)
and $u^\pm_{i+1/2}$ interpolated point values (Ye et al., §3, Eqs. (11)–(13)).
AFTENO replaces the WENO interpolation of $u^\pm_{i+1/2}$ by a TENO
interpolation. [Fu (2023)](/sources/fu-2023.md) (§3.10) lists it among the TENO
variants as the route by which "arbitrary monotone fluxes (Riemann solvers) can be
used".

## Construction

1. **Candidate interpolants** at $x_{i+1/2}$ on the incremental TENO stencils
   ($S_0$ central, $S_1$ downwind, $S_2$ upwind, $S_3=\{i,\dots,i+3\}$,
   $S_4=\{i-3,\dots,i\}$, …). Seventh order (Ye et al., Eq. (14)):
   $u^{(0)}=-\tfrac18u_{i-1}+\tfrac34u_i+\tfrac38u_{i+1}$,
   $u^{(1)}=\tfrac38u_i+\tfrac34u_{i+1}-\tfrac18u_{i+2}$,
   $u^{(2)}=\tfrac38u_{i-2}-\tfrac54u_{i-1}+\tfrac{15}8u_i$,
   $u^{(3)}=\tfrac5{16}u_i+\tfrac{15}{16}u_{i+1}-\tfrac5{16}u_{i+2}+\tfrac1{16}u_{i+3}$,
   $u^{(4)}=-\tfrac5{16}u_{i-3}+\tfrac{21}{16}u_{i-2}-\tfrac{35}{16}u_{i-1}+\tfrac{35}{16}u_i$.
2. **Linear weights** from $\sum_kd_ku^{(k)}=$ the full-stencil interpolant
   (Eqs. (15)–(17), Table 2): $K=3$: $1$; $K=4$: $\tfrac12,\tfrac12$;
   $K=5$: $\tfrac58,\tfrac5{16},\tfrac1{16}$; $K=6$: $\tfrac{15}{32},\tfrac5{16},\tfrac1{32},\tfrac3{16}$;
   $K=7$: $\tfrac{35}{64},\tfrac{35}{128},\tfrac7{128},\tfrac7{64},\tfrac1{64}$;
   $K=8$: $\tfrac{175}{384},\tfrac{35}{128},\tfrac7{192},\tfrac{21}{128},\tfrac1{128},\tfrac1{16}$.
   These are interpolation weights, not the reconstruction weights of TENO
   ($6/10,3/10,1/10$ at fifth order).
3. **Selection** exactly as in TENO: Jiang–Shu indicators of the candidate
   interpolants (Eq. (18)), scale separation
   $\gamma_k=(C+\tau_K/(\beta_k+\epsilon))^q$ with $C=1$, $q=6$ by default,
   normalization, sharp cut-off $C_T$, renormalized weights (Eqs. (6)–(10)). The
   global indicator is $\tau_5=\lvert\beta_2-\beta_1\rvert$ at fifth order and the
   sixth-order WENO-CU6-type $\tau_K$ from sixth order up (Eqs. (24), (28), (39)).
   At fifth order the stencils and weights are those of AFWENO5, relabelled
   $\{S_0,S_1,S_2\}^{\mathrm{AFTENO}}=\{S_1,S_2,S_0\}^{\mathrm{WENO}}$ (§3.3).
4. **Derivative corrections**, the same as in AFWENO: low-order central
   differences of the physical point fluxes over the TENO global stencil, without
   characteristic projection or weighting, on the argument that their coefficients
   carry at least $\Delta x^2$ (§3.2). The coefficients are
   $a_2=-\tfrac1{24}$, $a_4=\tfrac7{5760}$, $a_6=-\tfrac{31}{967680}$,
   $a_8=\tfrac{127}{154828800}$, $a_{10}=-\tfrac{73}{3503554560}$
   (Appendix, Eqs. (A.15)–(A.17)), with central difference coefficients up to
   order 10 in Tables 3–6. A purely central approximation "can be unstable in
   some problems"; the upwind, flux-split approximation of Liu (2017) fixes this
   but "increases the computational cost significantly" (§3.2, Eqs. (19)–(23)).

## Claimed advantages

Over classical TENO: interpolation of conserved, primitive or characteristic
variables and any monotone flux, where classical TENO reconstructs a smooth
flux-splitting function only; better free-stream preservation (asserted, not
tested in the paper; see [free-stream preservation](/properties/free-stream-preservation.md)).
Over AFWENO: robustness with several discontinuities in the global stencil, and
arbitrary odd or even order, where AFWENO "only has odd order accuracy" (Ye et
al., Abstract, §1, §5). Coefficients are given up to $K=8$; only fifth order is
tested.

## Evidence (fifth order)

([Ye et al. (2022)](/sources/ye-2022.md), §4.) Linear advection of
$\sin(\pi x)$ to $t=2$: fifth order, $L_1$ error $6.95\times10^{-12}$ at
$N_x=640$ against $6.31\times10^{-11}$ for AFWENO5-LF, $9.72\times10^{-12}$ for
TENO5 and $7.94\times10^{-11}$ for WENO5-JS (Tables 7–8). 2D Euler density wave:
smallest $L_1$ errors ($5.60\times10^{-11}$ at $320^2$, against
$2.90\times10^{-10}$ for AFWENO5-JS), but larger $L_\infty$ errors than
AFWENO5-JS on every mesh and an observed order falling to 4.70 (Tables 11–12).
On Sod, shock–density wave, blast waves, Rayleigh–Taylor ($\Delta x=1/480$, HLLC,
resolution comparable to fifth-order WENO-JS at $\Delta x=1/1920$, matching ninth-order
references at $C_T=10^{-8}$), double Mach reflection ($\Delta x=1/256$) and the viscous
Taylor–Green vortex at $\mathrm{Re}=1600$ on $256^3$ (best dissipation-rate peak
with HLLC), AFTENO5 is the least dissipative of AFWENO-JS, AFWENO-Z and TENO5.
On the shock–entropy wave, the exponent $q$ matters more than $C_T$, and $q=2$
is closer to the reference than $q=6$ (§4.5, Fig. 5).

**Cost** (2D Euler, 500 steps, Intel Xeon E5-2680v3, global Lax–Friedrichs;
Table 13): on $160\times160$ AFTENO takes 269.85 s against 176.86 s for AFWENO
(+52.6%) and 90.94 s for TENO (+196.7%); on $320\times320$, 2119.94 s against
1348.72 s (+57.2%) and 731.51 s (+189.8%). The extra cost over AFWENO is
attributed to scale separation and selection, the factor of about three over
TENO to the interpolation-based flux plus derivative terms (§4.2).

## Qualifications

- The text claims the smallest errors on the 2D density wave (§4.1), which its
  own $L_\infty$ table contradicts; the claim holds for $L_1$ only.
- Printed slips in the coefficient tables: Table 1 rows $K=5$ and $K=7$ have
  misprinted or swapped entries (Eq. (14) is correct); Table 3 rows "5∼6" and
  "9∼10" and two rows of Table 5 have inverted signs (Eq. (A.25) is correct).
  Eq. (13) and Eq. (A.19) give the arguments of $h$ in opposite orders.
- Tables 9–10 report observed orders 6.1–7.0 on the finest meshes of the 1D
  density wave for fifth-order schemes, with no time step or CFL stated; the
  domain is printed $[0,1\pi]$ with periodic $\sin x$ data, probably a slip for
  $[0,2\pi]$.
- "AFWENO has odd order only" is a property of the Jiang–Shu–Zhang construction,
  not of interpolation-based flux formulations in general.

# Citations

- [Ye et al. (2022)](/sources/ye-2022.md) — §§2–4, Eqs. (1)–(39), Tables 1–13, Appendix Eqs. (A.15)–(A.26).
- [Fu (2023)](/sources/fu-2023.md) — §3.10: AFTENO among the TENO variants.
