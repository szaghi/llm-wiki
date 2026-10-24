---
type: Benchmark
title: "Oscillating droplet"
description: "A two-dimensional elliptic drop at rest relaxes under surface tension and oscillates about the circle of equal area; the measured period, compared with the linear two-phase (Rayleigh mode-2) formula, and the mean pressure jump, compared with Laplace's law, test the surface-tension model of compressible interface-capturing schemes."
status: established
aliases: [oscillating ellipsoidal drop, oscillating elliptic droplet, droplet oscillation test, Rayleigh drop oscillation]
tags: [benchmark, multiphase, interface-capturing, surface-tension]
timestamp: 2026-10-23T20:05:00Z
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
| [Zhang et al. (2024a)](/sources/zhang-2024.md) §4.10 | water ellipse in air, nondimensional parameters of a cited work (water $p_\infty=6000$), uniform $p=1$ | ratio about 1000 | semi-axes 1.25 and 0.8, $\sigma_{\mathrm{st}}=1$ | $[0,4]^2$, extrapolation boundaries, to $t=120$ | Rayleigh, $T=2\pi\sqrt{(\rho_1+\rho_2)R_0^3/(6\sigma_{\mathrm{st}})}$, $R_0=\sqrt{a'b'}=1$; $T/2=40.56$ printed |
| [Long et al. (2023)](/sources/long-2023.md) §4.3, Eq. (36) | water drop in vapour, $p=1.3\times10^5$ Pa, 380 K | 1073.55 and 0.74 | semi-axes 0.6 and 0.4 mm, 20 N/m | $5\times5$ mm, quarter computed, multiresolution $256^2$ effective | two-phase Rayleigh, $\omega^2=(o^3-o)\sigma_{\mathrm{st}}/((\rho_{\mathrm{liq}}+\rho_{\mathrm{vap}})R^3)$, mode $o=2$, $R=0.4899$ mm (Eq. (37)) |

The three reference formulas are the same; Zhang et al. (2024a) print
Long et al.'s mode-2 form directly, and Jiao et al.'s agrees with it: with Jiao et al.'s full axes $a=2a'$, $b=2b'$ one has
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

**Steepness of the THINC profile.** Zhang et al. (2024a) run the ellipse
with their hybrid WENO5IS-THINC five-equation scheme (continuum surface
force, THINC on the volume fraction in interface cells; see
[THINC reconstruction](/methods/thinc-reconstruction.md)) and compare
THINC steepness parameters, schemes and resolutions by the history of
the kinetic energy. A larger steepness damps the kinetic energy more
and shifts the period; steepness 1.3 preserves most of the kinetic
energy and matches the analytical period, and MUSCL-THINC decays most
and has the largest period discrepancy (§4.10, Fig. 19).

**Laplace law.** The static companion of the test, a circular drop at
its Laplace pressure, is run by Zhang et al. (2024a) §4.9 with the
same cited nondimensional parameters: a water cylinder of
diameter 2 in $[0,4]^2$, pressure 2 inside and 1 outside (jump
$\sigma_{\mathrm{st}}/R_0=1$), smoothed initial volume fraction, to $t=10$.
On $128^2$ the steepness 1.3, 1.8, 2.3 leaves the volume fraction nearly
unchanged, but 1.8 and 2.3 add a spurious extra pressure jump: $L_1$
pressure errors $0.99$, $1.66$, $1.81$ and volume-fraction errors
$0.81$, $0.78$, $0.72$ (both $\times10^{-2}$; Table 11). They recommend a
moderate steepness when surface tension is present, and with 1.3 on
$64^2$–$256^2$ find the THINC schemes roughly first order in the
pressure error, plain WENO5IS below first order (Figs. 17–18). Their
parasitic currents at Laplace number $10^{11}$ give capillary numbers
$10^{-6}$–$10^{-7}$, comparable for the three schemes and decreasing with
resolution (§4.11, Fig. 20).

[Wilfong et al. (2026)](/sources/wilfong-2026.md) §4.1.8 run the same
static test with the surface-tension model of their
[six-equation model](/definitions/six-equation-model.md) in
[MFC](/software/mfc.md): a water column in air of nondimensional radius
$R^*=1$ and surface-tension coefficient $\sigma^*_{\mathrm{st}}=7.2\times10^{-4}$
on $128\times128$ cells, the capillary stress
$-\sigma_{\mathrm{st}}\big(\lVert\nabla\mathsf c\rVert I-\nabla\mathsf c\otimes\nabla\mathsf c/\lVert\nabla\mathsf c\rVert\big)$
of an advected colour function $\mathsf c$ (page-local) entering momentum and
total energy. The pressure jump settles at $\sigma_{\mathrm{st}}/R_0$, which
they call resolved "exactly", and the relative change of the pressure
between steps, $\max\lvert p^{n}-p^{n-1}\rvert/p^n$, falls to about
$10^{-9}$ by $t^*\approx40$ (Fig. 9). They state that the model is
conservative except for the pressure-relaxation terms.

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

- Zhang et al.'s (2024a) printed $T/2=40.56$ corresponds to $\rho_1+\rho_2=1000$;
  with $\rho_1=1000$ and $\rho_2=1$ the formula gives
  $\pi\sqrt{1001/6}=40.58$, a negligible difference *(compiler check,
  not in the sources)*.

# Citations

- [Jiao et al. (2024)](/sources/jiao-2024.md) — §3.5, §4.4, Eqs. (4–2)–(4–4), Table 4.6, Figs. 4.11–4.12.
- [Long et al. (2023)](/sources/long-2023.md) — §4.3, Eqs. (36)–(37), Fig. 13.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §4.9–4.11, Table 10–11, Figs. 17–20.
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §4.1.8, Fig. 9.
