---
type: Method
title: "Cures for numerical shock instability"
description: "Sensor-driven fixes that make low-dissipation Riemann solvers stable at strong shocks while keeping contacts and shear: widening the HLL wave speeds only inside the dissipation (selective wave modification), scaling the anti-diffusion near shocks, adding an entropy-control term on the entropy wave, adding dissipation only to the shear wave, or switching to a dissipative flux near shocks; all tested at first or second order only."
status: established
aliases: [carbuncle cure, carbuncle fix, selective wave modification, HLLC-SWM, HLLEM-SWM, anti-diffusion control, entropy control, shear-wave dissipation]
tags: [riemann-solver, shock-instability, robustness, numerical-flux]
timestamp: 2026-10-12T00:00:00Z
---

# Cures for numerical shock instability

Every cure here targets the same failure, the [numerical shock instability](/definitions/numerical-shock-instability.md)
of solvers that resolve contact and shear waves. Each tries to add
dissipation at strong shocks without losing that resolution elsewhere.
Most take one shared view: a low-dissipation solver is HLL plus an
anti-diffusive term. In central form,
$\hat f^{\mathrm{HLL}} = \tfrac12\left(f(u^-) + f(u^+)\right) + \mathbf d^{\mathrm{HLL}}$ with
$$\mathbf d^{\mathrm{HLL}} = \frac{\vert S_R\vert - \vert S_L\vert}{2(S_R - S_L)}\left(f(u^-) - f(u^+)\right) + \frac{\vert S_L\vert S_R - \vert S_R\vert S_L}{2(S_R - S_L)}\left(u^- - u^+\right),$$
and HLLC is $\hat f^{\mathrm{HLL}} + S_L\left(u^{\mathrm{HLLC}}_{*L} - u^{\mathrm{HLL}}_*\right)$
for $S_L \le 0 \le S_M$ (with $R$ for $S_M \le 0 \le S_R$)
([Simon & Mandal (2019)](/sources/simon-2019.md), eqs. 13–16).
[HLLEM](/methods/hllem-riemann-solver.md) is HLL minus anti-diffusion
along the contact and shear waves.

## Selective wave modification (Simon & Mandal)

Only the HLL dissipation sees widened speeds,
$S^{\mathrm w}_L = S_L - \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}$ and
$S^{\mathrm w}_R = S_R + \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}$. The
contact speed $S_M$ and the anti-diffusive term keep the original speeds,
so contacts and shear are still captured by construction.
* **HLLC-SWM.** $\vert S_L\vert$ and $\vert S_R\vert$ in the numerators of
  $\mathbf d^{\mathrm{HLL}}$ become $\vert S^{\mathrm w}_L\vert$ and
  $\vert S^{\mathrm w}_R\vert$. The denominators $S_R - S_L$ and the outer
  factors $S_R$, $S_L$ stay unmodified, so this is not HLL with wider
  speeds, and the authors stress that only this form works. With equal
  increments on both sides of a subsonic face, the change is an extra
  $\tfrac12\alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}(u^- - u^+)$ on the
  state jump. The cure is needed only on faces transverse to the shock
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §5, eqs. 17–22).
* **HLLEM-SWM.** The widened speeds replace $S_L$, $S_R$ throughout
  $\mathbf d^{\mathrm{HLL}}$, denominators included. Only the mass and
  interface-normal momentum fluxes are modified. Transverse faces alone
  turned out "necessary but not sufficient": the cure must act on every
  face near the shock ([Simon & Mandal (2019b)](/sources/simon-2019-b.md), §6.1, eqs. 41–43).
* **Sensors.** Variant E sets $\epsilon_{\mathrm{SWM}}$ to the largest
  $\tfrac12\max_p\vert\lambda^{(p)}(u^+) - \lambda^{(p)}(u^-)\vert$ (the
  entropy-fix size) over the faces transverse to the face: four for HLLC,
  excluding the face itself to spare boundary layers, and five for HLLEM.
  Variant P multiplies it by $1 - \omega_{\mathrm p}$ (HLLC), or uses
  $(1 - \omega_{\mathrm p})\vert S_{L,R}\vert$ (HLLEM), where
  $\omega_{\mathrm p}$ is the minimum over the stencil of
  $\min(p^+/p^-, p^-/p^+)^5$. The pressure sensor separates shock
  detection from the size of the dissipation and stays inactive at
  contacts and in shear layers
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §7;
  [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §6.1).
* **Tuning.** $\alpha_{\mathrm{SWM}} = 3.5$ comes from a matrix stability
  analysis of a steady normal shock at $M_s$ = 3, 7, 10 and 20. At
  $M_s = 7$ the largest real part of the spectrum falls from $+8.156$
  (plain HLLC) to $-0.661$ (variant E) and $-0.593$ (variant P).
  $\alpha_{\mathrm{SWM}} > 1$ is necessary, and in the nonlinear run the
  shock is stable only for $\alpha_{\mathrm{SWM}} \ge 2.5$
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §8;
  [stationary normal shock](/benchmarks/stationary-normal-shock.md)).
* **Price.** The saw-tooth analysis gives all three amplification factors
  below 1, under the tighter bound
  $\nu_y \le 1/\left(1 + \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}/\sqrt\gamma\right)$
  ([Simon & Mandal (2019)](/sources/simon-2019.md), eq. 27;
  [Simon & Mandal (2019b)](/sources/simon-2019-b.md), eq. 49). On a
  Mach 0.1 flat plate, variant P matches the Blasius profile, while E is
  slightly dissipative inside the boundary layer. A low-Mach switch
  $\sin\left(\tfrac{\pi}{2}\,\mathrm{Ma}/0.3\right)$ on the increment, for
  $\mathrm{Ma} \le 0.3$, repairs E. Positivity of the modified schemes is
  suggested by tests, not proved
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §§9.1, 9.9).

## Anti-diffusion control (HLLEM-ADC)

On the faces transverse to the shock only, the mass and normal-momentum
fluxes take $\omega_{\mathrm p}$ times the HLLEM anti-diffusion
($\omega_{\mathrm p} \to 0$ gives HLLE). The amplification factors become
$1 - 2\nu_y(1 - \omega_{\mathrm p})$ for density and normal velocity, and
$1 - 2\nu_y$ for pressure. It is the cheapest cure, but the most
dissipative on the flat plate, because the sensor fires where pressure
varies along the wall. The same analysis for the shear-only control of
Xie et al. (2017), HLLEMS, leaves the density factor at 1. That variant
fails on the Mach 20 blunt body and on the inclined stationary shock.
Simon & Mandal take this to contradict Xie et al.'s claim that
controlling the shear anti-diffusion suffices. The 2017 paper is not
ingested here, and its successor moved to entropy control
([Simon & Mandal (2019b)](/sources/simon-2019-b.md), §§6.2, 7.3, 7.6, 7.7).

## Entropy control (Xie et al.)

An additive term acts only along the entropy wave. Its strength contains
$(\rho^+ - \rho^-) - (p^+ - p^-)/c^2$, and the term scales the pressure part by
$\varphi_{\mathrm p}$:
$$\hat f^{\mathrm X+} = \hat f^{\mathrm X} + (\varphi_{\mathrm p} - 1)\,\frac{S_L^- S_R^+}{S_R^+ - S_L^-}\,\delta_2\,\frac{p^+ - p^-}{c^2}\,r^{(2)},$$
where $r^{(2)}$, $c$ and $\delta_2 = c/(c + \vert v_n\vert)$ are taken at
the Roe state. The base flux X may be Godunov's exact flux, Roe, HLLEM or
HLLC. The factor is
$\varphi_{\mathrm p} = \left(\min\, \min(p_a/p_b, p_b/p_a)\right)^3$ over
the face and the four normal-direction faces of its two neighbour cells.
It tends to 1 in smooth flow, where the term vanishes
([Xie et al. (2021)](/sources/xie-2021.md), §5, eqs. 77–80).
* The term adds no dissipation on the linearly degenerate waves. It
  leaves a laminar boundary layer and Elling's "physical carbuncle" (a
  vortex filament through a Mach 20 shock) intact. Plain HLLE and Quirk's
  Roe–HLLE hybrid smear that physical carbuncle (§§6.5–6.6).
* The derivation rests on a modified equation in characteristic
  variables. HLL over-dissipates the entropy wave, and the HLLEM
  anti-diffusion coefficient is already at its stability bound. Lowering
  the pressure part ($\varphi_{\mathrm p} < 1$) or raising the density
  part of the entropy-wave strength raises the entropy of the intermediate
  cell. The density version violates the contact stability condition and
  is discarded (§3.3).
* With the term, Godunov, Roe, HLLEM and HLLC pass Quirk's test, the
  Mach 20 cylinder, the double Mach reflection with "barely noticeable"
  kinks, and the shock diffraction. Roe with the term gets the correct
  stagnation-line pressure with one interior shock point (§6).

## Dissipation only on the shear wave (shallow water)

For the augmented Roe solver of the shallow-water equations, two fixes
replace only the shear-momentum flux. In the first, the star normal mass
flux upwinds it, which transports the tangential momentum as a passive
scalar. In the second, it comes from the two-wave HLLS solver. Either
can be applied only in shock cells, which keeps shear resolution
elsewhere. Both remove the carbuncle from a supercritical bow shock and
from a Mach-stem reflection; the first smears the slip line least
([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§5.3–5.4, 6.2, 6.4).

## Switching to a dissipative flux near shocks

At high order, Balsara & Shu cure a mild carbuncle of Roe-type fluxes by
using local Lax–Friedrichs near shocks
([conservative finite difference](/methods/conservative-finite-difference.md);
[Balsara & Shu (2000)](/sources/balsara-2000.md)). Hybrid solvers of this
kind lose shear resolution wherever the switch fires
([Xie et al. (2021)](/sources/xie-2021.md), §6.6). Kitamura & Shima find
fluxes that spread the shock over a few cells, or carry a
multidimensional dissipation term, insensitive to shock speed. They
recommend SLAU2 with a minmod limiter at second order, citing earlier
work ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§IV.B, V).

## Status at high order

All these cures are tested at first order, some also at second order
with limited linear reconstruction. None is tested with WENO or another
high-order reconstruction. The entropy-control term is a flux add-on and
so formally independent of the reconstruction; its authors name high
order as future work ([Xie et al. (2021)](/sources/xie-2021.md), §7).

# Citations

1. [Simon & Mandal (2019)](/sources/simon-2019.md), §§5–9.
2. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §§6–7.
3. [Xie et al. (2021)](/sources/xie-2021.md), §§3.3, 5–7.
4. [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§5.3–5.4, 6.2, 6.4.
5. [Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§IV.B, V.
6. [Balsara & Shu (2000)](/sources/balsara-2000.md).
