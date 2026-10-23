---
type: Definition
title: "Runaway electrons and their generation mechanisms"
description: "Electrons accelerated to relativistic energies when the parallel electric field exceeds the critical field set by collisional drag; in disruptions they form after the thermal quench by primary (Dreicer, hot-tail, tritium decay, Compton) and secondary (avalanche) generation, can carry most of the plasma current as a beam, and are lost when MHD stochastizes the field, apart from a trapped remnant or a confined core remnant that can reseed the beam."
status: established
aliases: [RE, runaway electron beam, RE beam]
tags: [runaway-electrons, disruption]
timestamp: 2026-10-16T18:38:00Z
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
- *Trapped remnant after a flush*: magnetically trapped relativistic
  electrons that survive a stochastic-field expulsion of the beam form a
  seed of 0.1–1% of the beam, orders of magnitude above the nuclear seed of
  "a few ampere" ([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md), p. 4;
  see [runaway reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)).
- *Seed conditions set by injection.* Full-impurity SPI collapses the core
  $T_e$ more than 100 μs before the impurities and density reach the core.
  The resulting hollow density is "unfavourable" for RE suppression
  ([Hu et al. (2021)](/sources/hu-2021.md), §3; stated, not simulated with
  runaways). Dilution cooling before the TQ is the motivation for reducing the
  hot-tail seed ([Hu et al. (2023)](/sources/hu-2023.md), §1, §5). After a
  flush the plasma is so cold ($T_e<20$ eV) that no Dreicer or hot-tail
  source is needed ([Liu et al. (2021)](/sources/liu-2021.md), §6).
- *Nuclear seeds only.* In the EU-DEMO study of
  [Vannini et al. (2025)](/sources/vannini-2025.md) (§4) the seed is tritium
  decay plus Compton scattering, switched on at the end of an artificial
  thermal quench, with no Dreicer or hot-tail source; the avalanche alone
  builds a beam of about 13 MA.

**Secondary (avalanche) generation** multiplies an existing RE population
by close collisions that knock thermal electrons above the critical
momentum. Its growth rate $\Gamma_{\mathrm{av}}$ is proportional to
$E_\parallel-E_c^{\mathrm{eff}}$ and, with partial screening, to the total
(free plus bound) electron density; at high electric field the bound
electrons available for knock-on dominate the impurity effect
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II, Eq. 2.13, after
Hesslow et al. 2017–2019). The formula is on the
[fluid-model page](/methods/runaway-electron-fluid-model.md). M3D-C1 uses
the Rosenbluth–Putvinski avalanche form, with $E_\parallel/E_c\approx10$ in
the post-flush DIII-D plasma ([Liu et al. (2021)](/sources/liu-2021.md),
§5.4). Because the gain is exponential in the available poloidal flux, a
convenient figure of merit is the flux per decade of gain, $\psi_{10}$. Reconstitution
after a flush is bounded by the seed times $10$ raised to the available flux
over that figure of merit ([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md),
Eq. 1).

## Consequences found in MHD simulations

- **Avalanche dominance in ITER.** In the JOREK–DINA ITER case the plateau
  RE current is about 10 MA for seeds of 0.1–1 A and still about 9.5 MA for
  a seed of $10^{-4}$ A, so that moderate seed reduction is ineffective in
  "strong-avalanche-gain machines like ITER"
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.B). In the
  axisymmetric EU-DEMO VDE, raising the neon density from about
  $1.3\times10^{18}$ to $2.4\times10^{19}$ m$^{-3}$ raises the peak runaway
  current from about 9.8 to 13 MA and the beam growth rate from about 180 to
  900 s$^{-1}$ ([Vannini et al. (2025)](/sources/vannini-2025.md), §4,
  Fig. 4, four points read from the figure). Vertical
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
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.4.2). In a 2D
  EU-DEMO VDE the beam keeps the current inside the last closed surface, so
  $q_{95}$ falls instead of rising and the vertical wall force keeps growing
  (≈60 MN), which defeats the
  [vertical-force mitigation](/results/vertical-force-mitigation.md) that
  works without runaways ([Vannini et al. (2025)](/sources/vannini-2025.md),
  §4, Fig. 3). The beam is MHD-unstable at every 3D restart, at
  $q_{95}=2.7$, 2.29 and 2.05, with growth rates of about
  $1$–$8\times10^4$ s$^{-1}$; the authors, citing Bandaru et al. (2024b),
  state that the beam "can become unstable a long time before the value of
  $q_{95}=2.0$" (§5, Fig. 5a).
- **Beam termination.** In the simulated benign termination of a JET RE
  beam, an $n=1$ double tearing mode at two $q=4$ surfaces stochastizes the
  field and the REs are lost in $\le100\,\mu$s, in "very good agreement"
  with the experiment ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
  §6.4.2). In M3D-C1 the final loss of a DIII-D plateau is a (2,1) resistive
  kink at $q_a\to2$. With nonlinearly excited $n>1$ harmonics it stochastizes
  the outer plasma, and more than 95% of the REs reach the lower
  high-field-side wall within about 0.06 ms with an $n=1$ footprint. The
  current converts to Ohmic current with a small spike, and a (1,1) kink
  flattens the residual core. The loss fraction converges only with at least
  16 toroidal planes ([Liu et al. (2021)](/sources/liu-2021.md), §5.3,
  Figs. 12–14). [Nardon et al. (2023b)](/sources/nardon-2023-b.md) (§V)
  hypothesize that D$_2$ injection terminates beams benignly because the
  colder, more resistive background lets the
  [double tearing mode](/definitions/double-tearing-mode.md) grow larger
  before stochasticity sets in. A trapped remnant can survive the flush and
  reseed the beam, at the cost of a 2–3 MA current drop in an ITER-like case
  ([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md); see
  [runaway reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)).
  In 3D JOREK runs of the EU-DEMO beam at $q_{95}\approx2.3$ with $n\le7$,
  edge $(8,4)$ and $(9,4)$ modes dominate first, then a $(2,1)$ mode
  saturates at $\sqrt{\psi_N}=0.6$; the stochastic region grows inward and
  the runaway current falls from 12.3 to 2.8 MA in 1.12 ms. The remnant
  stays in the core inside closed surfaces and re-avalanches to about 10 MA,
  then partly decays again after a new MHD burst
  ([Vannini et al. (2025)](/sources/vannini-2025.md), §5, Figs. 6–9). Two
  harmonics ($n=0$ and one $n>0$) misplace or overestimate the growth
  rates; all $n\le4$ are needed for the linear phase (§5, Fig. 5b). The
  energy that the lost runaways deposit, and the effect of sacrificial
  limiters, are on
  [runaway-electron wall loads](/definitions/runaway-electron-wall-loads.md).
- **Deconfinement by a passive coil.** A passive $n=1$
  [runaway-electron mitigation coil](/definitions/runaway-electron-mitigation-coil.md),
  driven by the current-quench loop voltage, keeps the post-TQ field
  stochastic while $q_0<2$; for SPARC, 1.5 ms of such deconfinement at
  1.75 MA/ms "could result in a $10^3$ reduction in the overall avalanche
  gain" ([Izzo et al. (2025)](/sources/izzo-2025.md), §III C, §IV; estimate
  without derivation).
- **Kink with RE current.** The RE current gives the (2,1) resistive kink a
  real frequency. Growth rate and frequency both "follow the 3/5 power law" of
  the resistivity, and both are insensitive to the convection speed of the
  fluid model above $4v_A$ (about 11% change from 4 to $16v_A$)
  ([Liu et al. (2021)](/sources/liu-2021.md), §5.2, Figs. 5, 9).
- **Confinement in current-quench fields.** In 3D ITER current-quench
  simulations the field is almost completely ergodic at 13 ms and core flux
  surfaces re-form by 23 ms. A companion study cited by
  [Artola et al. (2022)](/sources/artola-2022.md) (§4.1) finds that the REs
  are quickly depleted at 13 ms and could re-appear inside the re-formed
  surfaces.
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
- **Fluid in full MHD**: [M3D-C1](/software/m3d-c1.md) couples an RE
  density to full MHD and solves its continuity equation by
  [advection along characteristics](/methods/runaway-electron-advection-by-characteristics.md)
  ([Liu et al. (2021)](/sources/liu-2021.md), §2–4).
- **Reduced kinetic**: a drift-kinetic Monte Carlo RE solver in 1D flux
  geometry with an imposed stochastic diffusivity stands in for the 3D MHD
  ([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md)).
- **Test particles**: relativistic full-orbit or guiding-centre tracers in
  the MHD fields, without back-reaction
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.10, §6.4.1), also
  seeded from the fluid density to estimate wall loads
  ([Vannini et al. (2025)](/sources/vannini-2025.md), §6).
- **Kinetic with back-reaction**: full-$f$ particle-in-cell REs with
  two-way [pressure or current coupling](/methods/pressure-and-current-coupling.md)
  are in development, together with a synthetic synchrotron diagnostic
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.5).
  [Liu et al. (2022)](/sources/liu-2022.md) (§7) name the slow-manifold
  Boris pusher of [M3D-C1-K](/software/m3d-c1-k.md) as a good candidate for
  REs (see [particle pushers](/methods/particle-pushers.md)).

## Qualifications

**Complete loss versus trapped survivors in beam termination**
(qualification, downgraded from Contradictions by human decision, 2026-10-16). [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§6.4.2)
report that in the JET benign-termination simulation "the REs are lost" in
$\le100\,\mu$s, and [Liu et al. (2021)](/sources/liu-2021.md) (§5.3) find
more than 95% loss in DIII-D. [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md)
(pp. 1–4) state that the expulsion "is not complete": magnetically trapped
relativistic electrons survive the stochastic field as a 0.1–1% seed that
avalanches back. The statements need not conflict on the observed beam loss.
The 3D simulations use fluid RE models with no pitch variable, which cannot
represent a trapped population (compiler's remark). McDevitt & Tang impose
the stochastic transport instead of computing it. A simulation that follows
pitch-resolved (kinetic or particle) REs through a self-consistent 3D flush
and its rehealing would settle whether the trapped remnant survives at the
predicted level.

A third 3D case qualifies the compiler's remark above that fluid runs give
near-complete loss: in EU-DEMO the JOREK fluid model loses 77% of the
runaway current (12.3 to 2.8 MA) and the core remnant, which never reached
the stochastic region, reforms a beam of about 10 MA
([Vannini et al. (2025)](/sources/vannini-2025.md), §5, Fig. 6a). Survival
there is through closed surfaces that persist or reheal in the core, not
through trapping, so complete loss is not a property of fluid models; it
depends on whether the stochastic region reaches the core. The trapped
channel remains untested in 3D.

# Citations

- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §I–IV, Eqs. 2.13–2.19.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.10–2.11, §4.7, §6.4.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.5.
- [Liu et al. (2022)](/sources/liu-2022.md) — §7.
- [Liu et al. (2021)](/sources/liu-2021.md) — §2–6, Figs. 5, 9, 12–15.
- [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md) — Eq. 1, Figs. 1–5, Discussion.
- [Nardon et al. (2023b)](/sources/nardon-2023-b.md) — §V.
- [Artola et al. (2022)](/sources/artola-2022.md) — §4.1.
- [Hu et al. (2021)](/sources/hu-2021.md) — §3, §6.
- [Hu et al. (2023)](/sources/hu-2023.md) — §1, §5.
- [Vannini et al. (2025)](/sources/vannini-2025.md) — §4–6, Figs. 3–9.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §I, §III C, §IV.
