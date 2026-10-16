---
type: Definition
title: "Runaway electrons and their generation mechanisms"
description: "Electrons accelerated to relativistic energies when the parallel electric field exceeds the critical field set by collisional drag; in disruptions they form after the thermal quench by primary (Dreicer, hot-tail, tritium decay, Compton) and secondary (avalanche) generation and can carry most of the plasma current as a beam."
status: established
aliases: [RE, runaway electron beam, RE beam]
tags: [runaway-electrons, disruption]
timestamp: 2026-10-16T00:00:00Z
---

# Runaway electrons and their generation mechanisms

A runaway electron (RE) is an electron whose acceleration by the parallel
electric field $E_\parallel$ exceeds the collisional drag at its momentum,
so that it gains energy up to relativistic values. In a
[disruption](/definitions/disruption.md) the
[thermal quench](/definitions/thermal-quench.md) raises the resistivity;
the decaying current then induces a large $E_\parallel$ during the current
quench, and REs form. Because the number of avalanche e-foldings scales
with the plasma current, REs are a major risk for the ITER first wall
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §I;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.4).

## Critical field

The threshold for runaway of the most energetic electrons is the
Connor–Hastie critical field
$$E_c=\frac{n_ee^3\ln\Lambda_c}{4\pi\varepsilon_0^2m_ec^2},\qquad \tau_c=\frac{m_ec}{eE_c},$$
where $\ln\Lambda_c$ is the relativistic Coulomb logarithm and $\tau_c$
the relativistic collision time
([Bandaru et al. (2024)](/sources/bandaru-2024.md), Eq. 2.14). In plasmas
with partially ionized impurities the bound electrons add drag and
pitch-angle scattering, and synchrotron and bremsstrahlung losses add
further drag. The resulting *effective* critical field
$E_c^{\mathrm{eff}}>E_c$ (Eqs. 2.18–2.19) is the threshold that the
avalanche source of the
[RE fluid model](/methods/runaway-electron-fluid-model.md) uses.

## Generation mechanisms

**Primary (seed) generation** creates REs from the thermal population or
from external sources:

- *Dreicer* generation, diffusion of thermal electrons into the runaway
  region of velocity space. The 2019 JOREK RE fluid model started it when
  $E_\parallel$ exceeded $10^{-2}$ of the Dreicer field
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.7). The 2024
  extension contains no Dreicer source; the GO and ITER studies it follows
  find the Dreicer seed negligible in the ITER scenarios considered
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II.A, §III.A,
  attributing this to Vallhagen et al. (2020) and Martín-Solís et al.
  (2017)).
- *Hot-tail* generation, the survival of the fast tail of the pre-quench
  distribution when the cooling is faster than collisional relaxation.
  It is not implemented in the 2024 JOREK model; the artificial seed of
  the JOREK–DINA benchmark is said to represent Dreicer and hot-tail
  generation "loosely" ([Bandaru et al. (2024)](/sources/bandaru-2024.md),
  §IV.A).
- *Tritium β decay*: β electrons born with energy above the critical
  runaway energy run away. The seed is the tritium decay rate times the
  fraction of the β spectrum (end-point 18.6 keV) above that energy
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), p. 4).
- *Compton scattering* of γ photons from the activated wall: all
  electrons, free and bound, count, since the 0.1–10 MeV photons far exceed
  the binding energies of argon and neon. The source scales with fusion
  power; applying the burning-plasma photon flux during the current quench
  "should be strictly viewed as a conservative or worst-case approach"
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), pp. 4–5).

**Secondary (avalanche) generation** multiplies an existing RE population
by close collisions that knock thermal electrons above the critical
momentum. Its growth rate $\Gamma_{\mathrm{av}}$ is proportional to
$E_\parallel-E_c^{\mathrm{eff}}$ and, with partial screening, to the total
(free plus bound) electron density; at high electric field the bound
electrons available for knock-on dominate the impurity effect
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II, Eq. 2.13, after
Hesslow et al. 2017–2019). The formula is on the
[fluid-model page](/methods/runaway-electron-fluid-model.md).

## Consequences found in MHD simulations

- **Avalanche dominance in ITER.** In the JOREK–DINA ITER case the plateau
  RE current is about 10 MA for seeds of 0.1–1 A and still about 9.5 MA for
  a seed of $10^{-4}$ A, so that moderate seed reduction is ineffective in
  "strong-avalanche-gain machines like ITER"
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.B). Vertical
  plasma motion during the current quench reduces the avalanche gain
  substantially, "although the avalanche gain remains very large"
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.5).
- **Feedback on the thermal plasma.** Conversion of the current to REs
  removes Ohmic heating and lets the plasma cool further, to about 1 eV in
  the pure-neon GO case ([Bandaru et al. (2024)](/sources/bandaru-2024.md),
  §III.B).
- **MHD stability.** An RE fraction of the current recovers the
  $S^{-1/3}$ scaling of the [resistive internal kink](/definitions/resistive-internal-kink.md)
  at large resistivity, because the RE current is not resistively damped
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.7, Fig. 25). An
  off-axis RE current can destabilize a 1/1 internal kink in a plasma that
  would otherwise have a dominant 2/1 mode, and an RE beam slows a
  [vertical displacement event](/definitions/vertical-displacement-event.md)
  when current decay influences the vertical instability
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.4.2).
- **Beam termination.** In the simulated benign termination of a JET RE
  beam, an $n=1$ double tearing mode at two $q=4$ surfaces stochastizes the
  field and the REs are lost in $\le100\,\mu$s, in "very good agreement"
  with the experiment ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
  §6.4.2).
- **Electric-field fluctuations.** Test-electron studies in JOREK
  disruption fields find that parallel electric-field fluctuations of
  about 1 kV/m during the thermal quench broaden the electron energy
  distribution to a few tens of keV within tens of $\mu$s, which promotes
  runaway; axisymmetric lower-dimensional models do not capture this
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.4.1).

## Modelling approaches

- **Fluid**: one RE density coupled to the MHD through the current
  ([RE fluid model](/methods/runaway-electron-fluid-model.md)); similar
  fluid models exist in M3D-C1 and NIMROD and in Matsuyama et al. (2017),
  cited without comparison by [Bandaru et al. (2024)](/sources/bandaru-2024.md)
  (§I).
- **Test particles**: relativistic full-orbit or guiding-centre tracers in
  the MHD fields, without back-reaction
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.10, §6.4.1).
- **Kinetic with back-reaction**: full-$f$ particle-in-cell REs with
  two-way [pressure or current coupling](/methods/pressure-and-current-coupling.md)
  are in development, together with a synthetic synchrotron diagnostic
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.5).
  [Liu et al. (2022)](/sources/liu-2022.md) (§7) name the slow-manifold
  Boris pusher of [M3D-C1-K](/software/m3d-c1-k.md) as a good candidate for
  REs (see [particle pushers](/methods/particle-pushers.md)).

# Citations

- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §I–IV, Eqs. 2.13–2.19.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.10–2.11, §4.7, §6.4.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.5.
- [Liu et al. (2022)](/sources/liu-2022.md) — §7.
