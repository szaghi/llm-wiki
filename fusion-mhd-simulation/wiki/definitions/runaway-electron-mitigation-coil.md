---
type: Definition
title: "Runaway-electron mitigation coil"
description: "A passive non-axisymmetric (n = 1) coil driven by the loop voltage of the current quench, whose resonant field keeps the post-thermal-quench field stochastic so that runaway electrons are deconfined before the avalanche grows; NIMROD simulations for SPARC model it by a time-dependent normal-field boundary condition and find it effective only while q0 < 2, a condition sensitive to the treatment of the region between limiter and vessel."
status: established
aliases: [REMC, runaway electron mitigation coil, passive runaway coil, passive 3D coil]
tags: [runaway-electrons, disruption, wall, free-boundary, mhd]
timestamp: 2026-10-16T18:00:00Z
---

# Runaway-electron mitigation coil

A **runaway-electron mitigation coil (REMC)** is a passive conductor with
an $n=1$ non-axisymmetric geometry. During the current quench the loop
voltage of the decaying $I_p$ drives a current in it, so it applies a resonant 3D field exactly when
[runaway electrons](/definitions/runaway-electrons.md) would otherwise
avalanche; the field keeps the magnetic field stochastic and deconfines the
runaways before the beam grows ([Izzo et al. (2025)](/sources/izzo-2025.md),
§I, after Boozer 2011 and Smith, Boozer & Helander 2013). It is planned for
SPARC. [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md) (Discussion)
call a passive runaway coil "a more reliable alternative" to relying on an
uncontrolled long open-surface phase for preventing reconstitution after a
flush (see
[runaway reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)).

The REMC differs from a [resonant magnetic perturbation](/definitions/resonant-magnetic-perturbation.md)
coil set in its drive: its current is induced by the current quench itself,
not programmed (compiler's contrast; the source models the amplitude as
growing with the decay of $I_p$, below).

## Model in NIMROD

[Izzo et al. (2025)](/sources/izzo-2025.md) (§II C, §III A) represent the
coil without meshing it:

- **Normal-field boundary condition.** A time-dependent normal field on the
  computational boundary reproduces the coil's perturbation at the last
  closed flux surface. The resistive wall is transparent to this external
  perturbation but resistive to the plasma response
  ([resistive-wall coupling](/methods/resistive-wall-coupling.md)).
- **Amplitude.** The coil current is not prescribed in time. It grows in
  proportion to the decay of $I_p$, as a proxy for the loop voltage,
  through a coil-current versus plasma-current mapping computed with
  ThinCurr (Battey et al., as cited). ThinCurr assumes a self-similar
  current decay; NIMROD lets the current profile redistribute, which is why
  the mapping is in $I_p$ rather than in time.
- **Operating modes.** *Closed-circuit*: current allowed from $t=0$, so the
  coil also acts during the thermal quench. *Switch-activated*: zero until
  the $I_p$ spike.
- **Geometry.** An $n=0$ ideal wall suppresses vertical motion; SPARC is
  expected to be passively vertically stable with a wall time of about
  50 ms, and the coupling to the coil would first increase if the plasma
  moved, with a maximum 35 cm off the midplane (Battey, as cited; §II C,
  §III A).

## Findings

Earlier NIMROD + ASCOT5 + DREAM modelling of the coil alone predicted full
suppression of an otherwise more than 5 MA runaway beam in SPARC (Tinguely
et al. 2021, as cited); a realistic TQ was found to lose much of the seed
itself while the current rearrangement raised $q$ and reduced the coil
resonance (Izzo et al. 2022, as cited); resistive-wall boundary conditions
made the coil more effective than ideal ones and showed that it needs
$q_0<2$ (Izzo et al. 2024, as cited) (Izzo et al. 2025, §I, §III A).
The 2025 study adds, with massive gas injection
([massive gas injection](/definitions/massive-gas-injection.md)):

- **Coil field during the TQ.** A closed-circuit coil produces small $n=1$
  perturbations in the pre-TQ, smaller than the gas-driven $n=3$, which
  nevertheless make the large unstable $n=1$ mode grow and saturate earlier.
  The TQ comes earlier with a similar peak amplitude, the brief radiation
  peaking at the flash is more pronounced, and the radiated fraction at the
  end of the TQ rises from 95% to 99% (§III B, Figs. 10–11).
- **Switch at the spike.** Activated at the $I_p$ spike, the coil first lets
  the large $n=1$ and higher-$n$ modes decay; they grow again from about
  4 ms under the applied field (§III B, Fig. 10).
- **The $q_0<2$ condition.** The field is fully stochastic during the TQ in
  every case. Once $q_0$ exceeds 2, two islands appear and coalesce into a
  core of good flux surfaces. Up to 4.6 ms the coil prevents the good-surface
  core that forms without it (§III C, Fig. 13). The coil is effective only
  while $q_0<2$, supporting the earlier finding.
- **Sensitivity to the ex-limiter region.** When $q_0$ crosses 2 depends on
  how the region between limiter and vessel is parametrized: plasma-like
  parameters pause the inward motion of $q=2$ at $\psi_N=0.25$ and $q_0$
  exceeds 2 only about 1.5 ms after the $I_p$ spike; a resistivity raised
  1000-fold gives $q_0>2$ almost at the spike; raising mass density by 1000
  as well restores the plasma-like timing. The mechanism is "not
  immediately clear" (§III C, Fig. 12). The authors present this as a model
  sensitivity that calls for a better treatment of the plasma surroundings.
- **Avalanche estimate.** At a current-quench rate of 1.75 MA/ms, even
  1.5 ms of coil-driven deconfinement "could result in a $10^3$ reduction in
  the overall avalanche gain" (§IV; estimate, no derivation printed).

No runaway electrons are evolved in these runs; the effect on runaways is
inferred from the field topology (Poincaré plots, connection lengths up to
$2\times10^4$ transits, Fig. 13).

## Citations

- [Izzo et al. (2025)](/sources/izzo-2025.md), §I–IV, Figs. 9–13.
- [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md), Discussion.
