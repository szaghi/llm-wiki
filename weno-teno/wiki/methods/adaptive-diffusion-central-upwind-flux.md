---
type: Method
title: "Adaptive-diffusion central-upwind Rankine–Hugoniot flux"
description: "Wang, Don, Kurganov and Liu tighten the one-sided speeds of the anti-diffused central-upwind flux with regularized discrete Rankine–Hugoniot speeds, replace them by fluid-velocity speeds where a relative-jump detector flags smoothness, and damp acoustic speeds near contacts in 2D; used inside fifth-order A-WENO."
status: established
aliases: [adaptive diffusion CURH flux, CURH flux, central-upwind Rankine–Hugoniot flux, NEW A-WENO flux]
tags: [central-scheme, numerical-flux, alternative-weno, low-dissipation]
timestamp: 2026-10-21T12:00:00Z
---

# Adaptive-diffusion central-upwind Rankine–Hugoniot flux

The adaptive-diffusion central-upwind Rankine–Hugoniot (CURH) flux of
[Wang et al. (2023)](/sources/wang-2023-b.md) is the two-point finite-volume flux
$h(u^-,u^+)$ of a fifth-order [alternative WENO](/methods/alternative-weno.md) scheme for the
Euler equations. It is a [central-upwind](/methods/central-upwind-scheme.md) flux in three
layers: a built-in minmod anti-diffusion (Garg, Kurganov & Liu 2021, as recalled); one-sided
speeds sharpened by discrete Rankine–Hugoniot quantities (same origin); and, new in the paper,
a further reduction of the speeds where the solution is smooth, plus the
numerical-dissipation switch of Kurganov, Liu & Zeitlin in 2D. Chertock et al. list the
Rankine–Hugoniot speeds and the dissipation switch among the existing routes for reducing CU
dissipation ([Chertock et al. (2023)](/sources/chertock-2023.md), §1).

## Embedding in A-WENO

The scheme evolves point values,
$\frac{d}{dt}u_i=-\frac1{\Delta x}(\hat f_{i+1/2}-\hat f_{i-1/2})$, with

$$\hat f_{i+1/2}=h\big(u^-_{i+1/2},u^+_{i+1/2}\big)-\frac{1}{24}\Delta x^2\,(f_{xx})_{i+1/2}+\frac{7}{5760}\Delta x^4\,(f_{xxxx})_{i+1/2},$$

where $u^\pm_{i+1/2}$ come from fifth-order characteristic-wise WENO-Z **interpolation** and
the derivatives are central differences of the point fluxes $f_i=f(u_i)$ on
$i-2,\dots,i+3$ (§2, Eqs. (2)–(4)):

$$(f_{xx})_{i+1/2}=\frac{-5f_{i-2}+39f_{i-1}-34f_i-34f_{i+1}+39f_{i+2}-5f_{i+3}}{48\,\Delta x^2},\qquad (f_{xxxx})_{i+1/2}=\frac{f_{i-2}-3f_{i-1}+2f_i+2f_{i+1}-3f_{i+2}+f_{i+3}}{2\,\Delta x^4}.$$

Wang et al. state that in finite differences a standard finite-volume flux is limited to
second order, the high order coming from this Taylor correction (§1), and that A-WENO
schemes had so far used the Rusanov flux or its lower-dissipation adaptive-diffusion central
variant (§1).

## The flux

$h$ is the anti-diffused CU flux of the
[central-upwind page](/methods/central-upwind-scheme.md) (Eq. (5)), with the one-sided speeds
$a^\pm_{i+1/2}$ computed in three steps (§3.1; page-local symbols noted).

1. **Eigenvalue bounds** (Eq. (6)):
   $\tilde a^+=\max\{\lambda_m(A(u^+)),\lambda_m(A(u^-)),0\}$,
   $\tilde a^-=\min\{\lambda_1(A(u^+)),\lambda_1(A(u^-)),0\}$.
2. **Rankine–Hugoniot tightening** (Eqs. (7)–(9)). Per component $l$,
   $\hat\sigma^{(l)}=2[\![f^{(l)}]\!]/\big([\![u^{(l)}]\!]+[\![u^{(l)}]\!]^{\epsilon}\big)$, where
   $[\![u^{(l)}]\!]^{\epsilon}$ is the jump floored to $\pm10^{-10}$ with its sign; so
   $\hat\sigma^{(l)}=[\![f^{(l)}]\!]/[\![u^{(l)}]\!]$ when the jump is not tiny. With
   $\hat\sigma_{\max}=\max_l\hat\sigma^{(l)}$ and $\hat\sigma_{\min}=\min_l\hat\sigma^{(l)}$
   (page-local): if $\hat\sigma_{\max}>10^{-10}$, $\hat a^+=\min\{\tilde a^+,\hat\sigma_{\max}\}$
   and $\hat a^-=\max\{\tilde a^-,-\hat\sigma_{\max}\}$; if $\hat\sigma_{\min}<-10^{-10}$,
   $\hat a^+=\min\{\tilde a^+,-\hat\sigma_{\min}\}$ and $\hat a^-=\max\{\tilde a^-,\hat\sigma_{\min}\}$;
   otherwise $\hat a^\pm=\tilde a^\pm$.
3. **Smooth-area reduction (the contribution, Eqs. (12)–(13)).** The detector is the
   largest relative interface jump of the conserved components,
   $\Theta_{i+1/2}=\max_l\dfrac{\lvert[\![u^{(l)}]\!]\rvert}{\max\big(\lvert u^{(l)+}\rvert,\lvert u^{(l)-}\rvert,10^{-10}\big)}$
   (page-local $\Theta$). Where $\Theta_{i+1/2}\le\Delta x^2$,
   $$\varsigma^+=\min\big\{\max(v^+,v^-,0),c_{\varsigma}\hat a^+\big\},\quad \varsigma^-=\max\big\{\min(v^+,v^-,0),c_{\varsigma}\hat a^-\big\},\quad a^\pm=\pm\max\{\varsigma^+,-\varsigma^-\},$$
   with $v^\pm$ the one-sided velocities and $c_{\varsigma}=0.1$ (page-local $\varsigma$,
   $c_{\varsigma}$); elsewhere $a^\pm=\hat a^\pm$. In smooth regions the speeds are therefore
   symmetric and bounded by the fluid speed and by $0.1\hat a^\pm$: the acoustic part is
   dropped.

**2D dissipation switch** (§3.2, Eqs. (16)–(18)). At $x_{i+1/2,j}$, let
$\Delta^{(1)}=\big\lvert[\![p]\!]/(\gamma-1)+[\![\rho v_1^2]\!]/2\big\rvert$ (internal plus normal
kinetic energy jump) and $\Delta^{(2)}=\big\lvert[\![\rho v_2^2]\!]/2\big\rvert$ (tangential kinetic
energy jump); the switch is $\Psi=\Delta^{(1)}/\sqrt{(\Delta^{(1)})^2+(\Delta^{(2)})^2}\in[0,1]$
(zero when the denominator is below $10^{-10}$; page-local $\Delta^{(1,2)}$, $\Psi$), and step 1
becomes $\tilde a^+=\max\{v_1^-+\Psi c^-,v_1^++\Psi c^+,0\}$,
$\tilde a^-=\min\{v_1^--\Psi c^-,v_1^+-\Psi c^+,0\}$. Near contacts and shear layers, where
the tangential velocity jump dominates, the acoustic speed is damped; $\Psi\equiv1$ recovers
the direct extension of (6). Steps 2–3 then follow direction by direction.

The baseline ("OLD") scheme is the same A-WENO with the adaptive-diffusion central flux of
Wang, Don, Garg & Kurganov: a Rusanov-type flux
$\tfrac12(f(u^-)+f(u^+))-\tfrac12a_{i+1/2}[\![u]\!]$ with a single adaptive coefficient that
equals $\min\{\min\lvert v^\pm\rvert,0.1\max(\lvert v^\pm\rvert+c^\pm)\}$ in smooth areas and, elsewhere,
an energy-component Rankine–Hugoniot speed clipped between $\min\lvert v^\pm\rvert$ and
$\max(\lvert v^\pm\rvert+c^\pm)$ (App. A,
Eqs. (A1)–(A3)); see [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md).

## Numerical evidence

Euler, $\gamma=1.4$ (Examples 1–8) or $5/3$ (Example 9), SSP-RK3 at CFL 0.45, all
regularizations $10^{-10}$, $c_{\varsigma}=0.1$ (§4).

- Isentropic vortex ([isentropic vortex](/benchmarks/isentropic-vortex.md), $[0,10]^2$,
  $t=1$, CFL $=\Delta x^{2/3}$): both schemes reach fifth order; at $\Delta x=1/64$ the
  $L^2$ density errors are $3.45\times10^{-9}$ (OLD) and $3.62\times10^{-9}$ (NEW), the NEW
  errors being slightly larger on every grid, with irregular rates (Table 1).
  *Compiler check, not in the sources:* CFL $\propto\Delta x^{2/3}$ gives
  $\Delta t\propto\Delta x^{5/3}$, so the third-order time error is $\mathcal O(\Delta x^5)$.
- [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
  ($\Delta x=1/400$) and [Shu–Osher](/benchmarks/shu-osher-problem.md) (200 cells): slightly
  sharper, less dissipation in the post-shock waves (Exs. 1–2; the 1D dissipation switch is
  inactive).
- [Double Mach reflection](/benchmarks/double-mach-reflection.md) ($1/480$), 2D Riemann
  configuration 3, explosion, implosion, [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md),
  [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md): better slip-line roll-up,
  curlier contacts, longer implosion jet, richer instabilities (Exs. 4–9, Figs. 3–9).

## Qualifications

- No theorem is given. Whether the non-smooth switches (minmod, max/min, the $\Theta$ test)
  preserve the formal fifth order of A-WENO rests on Table 1 alone; no positivity or entropy
  claim is made.
- The two "if" branches of step 2 can both hold; the paper does not state their precedence
  (Eq. (9)).
- "Outperforms existing fifth-order A-WENO schemes" is shown against one scheme (OLD) and by
  visual comparison on under-resolved problems; on the smooth vortex the NEW errors are larger.

# Citations

- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1, §2 (Eqs. (2)–(4)), §3.1 (Eqs. (5)–(13)), §3.2 (Eqs. (14)–(18)), §4 (Exs. 1–9, Table 1), App. A.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §1 (Rankine–Hugoniot speeds and dissipation switch as dissipation-reduction routes).
