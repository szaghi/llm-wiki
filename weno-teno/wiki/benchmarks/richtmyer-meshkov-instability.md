---
type: Benchmark
title: "Richtmyer–Meshkov instability"
description: "A planar shock crossing a sinusoidally perturbed interface between two gases or a metal and a gas: the single-mode air–SF6 case at Mach 1.2 against front-tracking and growth models, a heavy-to-light copper–gas case with phase reversal, and the Brouillette–Sturtevant air–acetone/SF6 case with re-shock; it tests interface sharpness, growth rates and the resolution of the mixing zone."
status: established
aliases: [RMI, Richtmyer–Meshkov, shock-accelerated interface, reshocked Richtmyer–Meshkov instability, single-mode Richtmyer–Meshkov instability]
tags: [benchmark, multiphase, interface-capturing, dg]
timestamp: 2026-10-22T18:00:00Z
---

# Richtmyer–Meshkov instability

A planar shock crosses an interface between two materials of different
density whose position carries a small single-mode perturbation,
$x=x_{\mathrm I}+a_0\cos(2\pi y/\lambda)$ with amplitude $a_0$ and
wavelength $\lambda$ (page-local symbols). The impulsive acceleration
makes the perturbation grow: the light fluid penetrates the heavy one as
bubbles, the heavy fluid the light one as spikes, and the interface
rolls up. When the shock reflects from an end wall and crosses the
interface again (re-shock), the mixing zone breaks into fine structures.
The benchmark tests whether a scheme keeps the material interface sharp
and resolves its roll-up, and, where the sources measure it, whether
the perturbation amplitude and growth rate agree with front-tracking
computations and with growth models. The density contrast is given by
the Atwood number $A=(\rho_{\mathrm h}-\rho_{\mathrm l})/(\rho_{\mathrm h}+\rho_{\mathrm l})$
(page-local; heavy and light densities).

## Setups in the sources

All three setups are two-dimensional and single-mode.

**Air–SF$_6$, Mach 1.2.** [Bai & Li (2022)](/sources/bai-2022.md)
§3.3.1, Table 2: domain $[-28,32]\times[-1.875,1.875]$ cm, symmetry
conditions in $y$ and outgoing ones in $x$; interface at $x_{\mathrm I}=0$
with $\lambda=3.75$ cm and $a_0=0.24$ cm; air $\rho=0.95$ kg/m³,
$\gamma=1.4$, and SF$_6$ $\rho=4.84$ kg/m³, $\gamma=1.09$, at
$p=0.8$ bar; a Mach 1.2 shock starts at $x=-1.0$ cm in the air. The
pre-shock Atwood number is $A\approx0.67$ *(compiler check, not in the
sources)*. Their sharp-interface discontinuous Galerkin solver (degree
2, level set, ghost fluid in cut cells; see
[level-set methods](/methods/level-set-method.md)) runs on three
adaptive levels with 80 elements per wavelength on the background
mesh; snapshots from $-30.1$ to $1118\,\mu$s.

**Copper–gas, Mach 2.5, heavy to light.** Bai & Li §3.3.2, Table 3:
domain $[-10,10]\times[-2,2]$ cm, $\lambda=4.0$ cm, $a_0=0.16$ cm; a
Mach 2.5 shock starts at $x=-0.28$ cm inside a copper-like
[stiffened gas](/definitions/stiffened-gas-equation-of-state.md)
($\rho=8930$ kg/m³, $\gamma=3.0$, $C_p=2587$, $p_\infty=4.62\times10^{10}$)
and passes into a gas ($\rho=1.22$ kg/m³, $\gamma=1.67$, $C_p=683$) at
$p=1.0$ bar; four levels, 32 elements per wavelength; time zero when
the shock reaches the bottom of the interface, snapshots to
$81.8\,\mu$s. The shock goes from heavy to light, so the perturbation
first reverses its phase.

**Air–acetone/SF$_6$ with re-shock, Mach 1.21.**
[Renac (2021)](/sources/renac-2021.md) §7.4, after Brouillette &
Sturtevant's experiment: a Mach 1.21 shock in a mixture of air and
acetone vapour ($\gamma=1.24815$, $C_v=3.2286$) hits a single-mode
interface with SF$_6$ ($\gamma=1.0984$, $C_v=2.0019$), $A=0.6053$; data
non-dimensional with a length of 1 cm and the pre-shock pressure,
temperature and sound speed of the mixture; domain
$[0,80.1]\times[0,5.9]$, periodic top and bottom, non-reflecting on the
left and reflecting on the right, so that the shock returns and
re-shocks the interface. The
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
are solved by entropy-stable [DGSEM](/methods/dgsem.md) of degree
$N=3$ on $1601\times118$ Cartesian elements, 118 per wavelength, which
Renac calls coarse compared with earlier computations; snapshots
labelled 4, 6 and 6.6 µs before and 7 µs after re-shock (Fig. 7).

## Findings

**Growth against models and other computations.** On air–SF$_6$, Bai &
Li's amplitude and growth-rate histories are consistent with Holmes's
front-tracking results, with Ullah et al.'s and with an earlier
computation of their group, and agree with the Zhang–Sohn nonlinear
model; they also plot linear theory and Richtmyer's impulsive model
(Figs. 16–17). On copper–gas, the transmitted rarefaction decompresses
the metal from 8930 to a release density of 7570 kg/m³, the asymptotic
bubble velocity is almost equal to the velocity of the unperturbed
interface, and the spike velocity falls after its peak (Figs. 18–19).

**Resolution of the re-shocked mixing zone.** Renac reports "a good
resolution of the shock and material interface and the associated
vortical structures" before and after re-shock, with spike roll-up
after the first passage and "complex fine flow field structures and a
low Mach number flow field" after the second (§7.4, Fig. 7). The
evidence is contour plots; no growth rate or mixing width is measured.

**Also in the bundle.** [Huang et al. (2026)](/sources/huang-2026.md)
§6.9 run a Richtmyer–Meshkov problem at $\Delta x=1/200$ to $t=2$ and
find [ROUND](/methods/round-scheme.md) comparable to a learned
third-order WENO and its low-dissipation variant finer than WENO5-JS
(Fig. 14), again by visual comparison.

## Qualifications

- The three setups share only the geometry: the Atwood numbers
  (about 0.67, 0.61 and a metal–gas contrast), the shock strengths
  (Mach 1.2, 1.21, 2.5), the direction (light to heavy, heavy to light)
  and the presence of re-shock all differ, and only Bai & Li measure a
  growth rate.
- Bai & Li print the copper stiffening constant with the unit "bar";
  with bar the sound speed of their metal would be about 1250 km/s, with
  pascal about 3.9 km/s, so pascal is meant *(compiler check, not in the
  sources)*. Their Table 3 labels the gas density "$\rho_{\mathrm{air}}$"
  although the gas has $\gamma=1.67$.
- Renac defines the Atwood number with "$\rho_2=\gamma_2$ taken as the
  pre-shock density of the mixture", but component 1 is the mixture:
  with his non-dimensionalization the mixture density is
  $\gamma_1=1.24815$, and $A=0.6053$ then gives an SF$_6$ density of
  about 5.08 *(compiler check, not in the sources)*.
- Renac's figure labels the snapshots in microseconds for a
  non-dimensional computation.

# Citations

- [Bai & Li (2022)](/sources/bai-2022.md) — §3.3.1–3.3.2, Tables 2–3, Figs. 16–19.
- [Renac (2021)](/sources/renac-2021.md) — §7.4, Fig. 7 (arXiv v3).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.9, Fig. 14.
