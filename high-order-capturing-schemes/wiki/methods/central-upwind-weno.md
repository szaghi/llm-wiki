---
type: Method
title: "Central-upwind WENO (WENO-CU6)"
description: "Hu–Wang–Adams sixth-order WENO: a downwind candidate stencil completes a symmetric six-point set whose linear weights give the sixth-order central scheme; WENO-Z-type weights with a large constant and a six-point indicator switch smoothly between central and upwind."
status: established
aliases: [WENO-CU6, adaptive central-upwind WENO]
tags: [weno, low-dissipation, central-scheme, turbulence]
timestamp: 2026-10-13T00:00:00Z
---

# Central-upwind WENO (WENO-CU6)

**Construction** ([Hu, Wang & Adams (2010)](/sources/hu-2010.md)). The
three upwind three-point candidates of WENO5 are joined by a downwind one,
$\hat f_{3,i+1/2} = \tfrac16(11 f_{i+1} - 7 f_{i+2} + 2 f_{i+3})$. With
linear weights $d = (\tfrac{1}{20}, \tfrac{9}{20}, \tfrac{9}{20}, \tfrac{1}{20})$
they reproduce the sixth-order central flux
$\tfrac{1}{60}(f_{i-2} - 8 f_{i-1} + 37 f_i + 37 f_{i+1} - 8 f_{i+2} + f_{i+3})$,
whose difference is a non-dissipative sixth-order derivative; sixth
order holds if $\omega_k - d_k = O(h^4)$. Weights:
$$\tilde\omega_k = d_k\left(C_w + \frac{\tau_6}{\beta_k + \varepsilon}\right),\qquad \tau_6 = \beta_6 - \tfrac16\left(\beta_0 + \beta_2 + 4\beta_1\right),$$
$C_w = 20$, $\varepsilon = 10^{-40}$ (eqs. 24–26, read from the page
image). For the downwind stencil the three-point indicator is replaced by
$\beta_6$, the indicator of the whole six-point stencil (from
[Balsara & Shu (2000)](/sources/balsara-2000.md)); a discontinuity
anywhere in the six points makes $\beta_6$ large and the downwind weight
vanish. $\tau_6 = O(h^6)$ in smooth regions, so the condition holds
independently of $C_w$; the large $C_w$ pulls the weights to optimal when
the indicators are comparable. At critical points the scheme degenerates
like WENO5; the authors decline the Borges et al. fix because it adds
dissipation.

**Results.** Sixth order on a Gaussian pulse; Sod, Lax and the 123
problem with less dissipation than WENO5 and WENO-M near
discontinuities, small velocity overshoots at strong waves that vanish
under refinement; no instability at contacts, unlike the order-optimized
symmetric scheme of [Martín et al. (2006)](/sources/martin-2006.md)
([bandwidth-optimized WENO](/methods/bandwidth-optimized-weno.md)). Blast
waves, Shu–Osher (better than WENO5, WENO-M and the WENO-SYM schemes),
isentropic vortex, Mach 8 shock/vorticity interaction, double Mach
reflection (vortical structure comparable to WENO5 at twice the
resolution), and an equipartition spectrum test (23 % of the kinetic
energy kept after 10 steps against 13 % for WENO-Z). $C_w$ of order 10
changes dissipation only slightly; much larger values risk instability
with strong shocks.

**Later.** [Fu, Hu & Adams (2016)](/sources/fu-2016.md) list the
drawback that spurious waves can appear at marginally resolved
wavenumbers because the central background scheme cannot suppress
accumulated dispersion error; a variant WENO-CU6-M ($C_w = 1000$, $q = 4$)
acts as an implicit subgrid model but fails their blast-wave and double
Mach tests. TENO generalizes the idea ([targeted ENO](/methods/teno.md)).

# Citations

1. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §§2–3.
2. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §§1, 2.3, 5.
3. [Balsara & Shu (2000)](/sources/balsara-2000.md), §III.
4. [Martín et al. (2006)](/sources/martin-2006.md), §§4–5.
