---
type: Benchmark
title: "Oscillating droplet"
description: "A two-dimensional elliptic drop at rest relaxes under surface tension and oscillates about the circle of equal area; the measured period, compared with the linear two-phase (Rayleigh mode-2) formula, and the mean pressure jump, compared with Laplace's law, test the surface-tension model of compressible interface-capturing schemes."
status: established
aliases: [oscillating ellipsoidal drop, oscillating elliptic droplet, droplet oscillation test, Rayleigh drop oscillation]
tags: [benchmark, multiphase, interface-capturing, surface-tension]
timestamp: 2026-10-23T23:45:00Z
---

# Oscillating droplet

A drop of one fluid in another, both at rest and at the same pressure, is given an elliptic
initial shape with semi-axes $a'$ and $b'$ (page-local). Surface tension with coefficient
$\sigma_{\mathrm{st}}$ (registry §10) pulls it towards the circle of equal area, radius
$R_0=\sqrt{a'b'}$, which it overshoots: the drop oscillates between the two elliptic
orientations, passing through the circle twice per period, and the oscillation decays only by
numerical (or physical) dissipation. For small amplitude the period of the second mode in two
dimensions follows from the linear two-phase theory, and after the transient the pressure
jump across the interface tends to Laplace's value $\sigma_{\mathrm{st}}/R_0$ in 2D. The test
checks the curvature computation and the force discretization of a capillary model in a
compressible scheme, separately from shocks and phase change.

## Setups

| Source | Drop / ambient | $\rho$ (kg m$^{-3}$) | Shape, $\sigma_{\mathrm{st}}$ | Domain, grid | Reference period |
|---|---|---|---|---|---|
| [Jiao et al. (2024)](/sources/jiao-2024.md) §4.4 | two ideal gases at $p_0=10^7$ Pa, 300 K (Table 4.6) | 117.647 and 4.444 | $(10^4x-7.9)^2/4^2+(10^4y-7.9)^2/3^2=1$ (semi-axes 0.4 and 0.3 mm), 80 N/m | $(1.58\times10^{-3})^2$ m$^2$, $158\times158$, non-reflective | Fyfe et al., $T=2\pi\sqrt{(\rho_1+\rho_2)(ab)^{3/2}/(48\sigma_{\mathrm{st}})}$ with $a=6\times10^{-4}$, $b=8\times10^{-4}$ m |
| [Long et al. (2023)](/sources/long-2023.md) §4.3, Eq. (36) | water drop in vapour, $p=1.3\times10^5$ Pa, 380 K | 1073.55 and 0.74 | semi-axes 0.6 and 0.4 mm, 20 N/m | $5\times5$ mm, quarter computed, multiresolution $256^2$ effective | two-phase Rayleigh, $\omega^2=(o^3-o)\sigma_{\mathrm{st}}/((\rho_{\mathrm{liq}}+\rho_{\mathrm{vap}})R^3)$, mode $o=2$, $R=0.4899$ mm (Eq. (37)) |

The two reference formulas are the same: with Jiao et al.'s full axes $a=2a'$, $b=2b'$ one has
$(ab)^{3/2}=8R_0^3$, so Fyfe et al.'s period is $2\pi\sqrt{(\rho_1+\rho_2)R_0^3/(6\sigma_{\mathrm{st}})}$,
which is Long et al.'s mode-2 Rayleigh period ($o^3-o=6$) *(compiler check, not in the
sources)*. Both sources take $R_0$ as the radius of the circle of equal area: Long et al.'s
$R=0.4899$ mm is $\sqrt{0.6\times0.4}$ mm, and Jiao et al.'s "equivalent radius" 0.346 mm is
$\sqrt{0.4\times0.3}$ mm *(compiler check, not in the sources)*.

## Findings across sources

**Period.** Jiao et al. obtain a period of $2\times10^{-5}$ s from the semi-length of the minor
axis, "in accordance to the analytic expression" (Fig. 4.12); the formula with their data gives
$2.04\times10^{-5}$ s *(compiler check, not in the sources)*. Long et al. compute 0.207 ms
against the theoretical 0.204 ms, an error of about 1.47%, and find that phase change
(evaporation and condensation coefficients 1.0) alters the amplitude but not the frequency of
the oscillation (§4.3, Fig. 13).

**Pressure jump.** Jiao et al. average the pressure inside and outside after the transient and
obtain a jump of 241017 Pa against Laplace's $\sigma_{\mathrm{st}}/R_0\approx231214$ Pa, a 4.24%
error which they call acceptable at their resolution (§4.4, Eq. (4–4)). Their surface-tension
model is the continuum surface force with a curvature computed from a Gaussian-filtered
indicator, decoupled from the gradient of the Heaviside function (§3.5); Long et al.'s
surface tension enters the jump conditions of their phase-change Riemann solver
([phase-change Riemann solver](/methods/phase-change-riemann-solver.md)) in a conservative
sharp-interface [level-set method](/methods/level-set-method.md).

## Qualifications

- Jiao et al. call the ellipse "drop" in the section title and "bubble" in Fig. 4.11 and in the
  text of §4.4, print the gas
  constant in kJ/(kg K) and the density in kJ/m$^3$ in Table 4.6 (the printed $\rho=p_0/(RT)$
  values hold with $R$ in J/(kg K)), and call $\sigma_{\mathrm{st}}/R_0$ "the theoretical value of
  the pressure jump for a spherical bubble", whereas $\sigma_{\mathrm{st}}/R_0$ is the
  two-dimensional (circular) value *(compiler check, not in the sources: the units)*.
- Jiao et al.'s densities 117.647 and 4.444 kg m$^{-3}$ give a density ratio of about 26, two
  ideal gases; Long et al.'s ratio is about 1450 *(compiler check, not in the sources: both
  ratios)*. The two runs therefore test different regimes of the same model problem.

# Citations

- [Jiao et al. (2024)](/sources/jiao-2024.md) — §3.5, §4.4, Eqs. (4–2)–(4–4), Table 4.6, Figs. 4.11–4.12.
- [Long et al. (2023)](/sources/long-2023.md) — §4.3, Eqs. (36)–(37), Fig. 13.
