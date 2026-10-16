---
type: Definition
title: "Edge harmonic oscillation and QH-mode"
description: "The quiescent H-mode is an ELM-free H-mode in which a saturated low-n kink-peeling mode, seen as the edge harmonic oscillation with frequencies at integer multiples of a fundamental, provides the edge transport that holds the pedestal below the ELM limit; JOREK reproduces it for DIII-D, ASDEX Upgrade and, predictively, HL-3, with access in windows of q95 and without torque input."
status: established
aliases: [EHO, edge harmonic oscillation, QH-mode, quiescent H-mode, saturated kink-peeling mode]
tags: [elm, pedestal, edge, kink, reduced-mhd, extended-mhd, tokamak]
timestamp: 2026-10-16T18:00:00Z
---

# Edge harmonic oscillation and QH-mode

The quiescent H-mode (QH-mode) is an H-mode without
[edge-localized modes](/definitions/edge-localized-mode.md). Its pedestal is
held below the ELM stability limit by a quasi-stationary, saturated
low-$n$ kink-peeling mode, the external-kink branch of the peeling–ballooning
family. The mode is seen experimentally as the **edge harmonic oscillation**
(EHO): a coherent, non-sinusoidal edge fluctuation whose toroidal harmonics
$n$ appear at frequencies $n$ times a fundamental, as expected for a rigidly
rotating structure. The kink-peeling mode itself raises the edge transport
in place of the ELM crash
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §5;
[Cathey et al. (2024)](/sources/cathey-2024.md), §3.2;
[Liang et al. (2025)](/sources/liang-2025.md), §I, §IV B).

## Simulated cases

| Device (source) | Model | Linearly unstable | Saturated state | EHO fundamental, simulated vs measured |
|---|---|---|---|---|
| DIII-D (Hoelzl et al. 2021, §5, refs. [244, 245]) | JOREK | not given in the review | saturated kink-peeling mode gives the EHO | not given |
| ASDEX Upgrade #39279 ([Cathey et al. (2024)](/sources/cathey-2024.md), §3.2, Fig. 3) | JOREK reduced MHD, diamagnetic terms, Sauter bootstrap, single temperature, no torque, $n=0$–6 | $n=1$, 2 ($n=2$ faster) | $n=1$ dominant, energy of higher harmonics falling steeply with $n$ | about 27 kHz vs about 10 kHz |
| HL-3, predictive ([Liang et al. (2025)](/sources/liang-2025.md), §III–IV) | same model family, $n=0$–12, Mach-1 sheath targets, no momentum source, ideal wall | $n=2$, 3 | $n=2$ dominant from 19 to 60 ms | 7.5 kHz vs measured fundamentals of about 6 kHz (JET, HL-2A) and 10 kHz (DIII-D, AUG) on other devices |
| ITER 10 MA steady-state scenario ([Becoulet et al. (2022)](/sources/becoulet-2022.md), §3, §5) | JOREK two-fluid with rotation and neoclassical friction | — | $n=3$ saturates and rotates without a crash, "QH-mode-like"; locks to a static $n=3$ RMP | not given |

In the ITER $Q=10$ and AUG QH cases summarized by Hoelzl et al. (2021, §5),
low-$n$ harmonics ($n=1$–3) dominate at an $E\times B$ velocity of about
20 km/s.

## The HL-3 prediction (Liang et al. 2025)

**Setting.** HL-3 ($R_0=1.78$ m, $a=0.65$ m) in lower single null, with
$B_\phi=+2.1$ T on axis, $I_p=-2.0$ MA and $q_{95}=2.5$; no HL-3 discharge is
used as input. An axisymmetric run with ad hoc transport wells and 24 MW of
heating builds the pedestal over 12.72 ms; then $n=1$–12 are started from
noise. The grid has 11 136 $G^1$ Bézier elements (§II–IV A; grid §III, Fig. 1; see
[Bézier finite elements](/methods/bezier-finite-elements.md)).

* **Linear and saturated phase.** Single-$n$ runs give only $n=2$ and 3
  unstable, and the truncation at $n=12$ is justified by diamagnetic
  stabilization of higher $n$. $n=1$ is driven at about 16 ms with
  $\gamma_{n=1}\approx\gamma_{n=2}+\gamma_{n=3}$, the modes saturate at about
  19 ms with $n=2$ dominant, and the kinetic energies stay stationary to
  60 ms (§IV B 1, Fig. 7).
* **Edge transport.** The saturated mode makes the edge stochastic outside
  $\psi_N\approx0.93$, a layer that widens with time, while resilient
  surfaces persist near $q=2$ ($\psi_N\approx0.87$) "despite the fact that
  the KAM surfaces are not enforced in JOREK"; transport rises through
  parallel conduction in the stochastic layer and non-axisymmetric
  $E\times B$ convective cells. The pedestal $p$ and $T_e$ relax slightly at
  saturation, the radial-electric-field well becomes shallower, and the
  thermal energy stops growing, against a steady rise in the axisymmetric
  reference; no density pump-out is visible because the pedestal particle
  source dominates (§IV B 1, Figs. 9–12).
* **EHO spectrum.** The high-field-side density at $\psi_N=0.95$ is
  non-sinusoidal with equally spaced harmonics; $n=2$ at 15 kHz dominates,
  so the fundamental is 7.5 kHz, and $n=3$ sits at 22.5 kHz (§IV B 2,
  Figs. 13–14). Modes with $n>7$ lie above 55 kHz with small amplitude.
* **High- and low-field-side asymmetry.** On the low-field side $n=2$ and 3
  contribute comparably and the amplitude is lower; near $\psi_N=0.95$ $n=3$
  exceeds $n=2$, whose profile has a valley at 0.94. On the high-field side
  $n=2$ dominates except at $\psi_N=0.88$–0.90. The mechanism is "not
  completely understood"; edge gradients and rotation shear are "suspected"
  (§IV B 2–3, Figs. 15–16a).
* **Density versus temperature response.** The density perturbation peaks
  where $E_r$ is locally weak and $|\nabla n|$ is largest; the temperature
  perturbation peaks at the two extrema of $E_r$ ($\psi_N=0.915$ and 0.976)
  and is similar on both sides (§IV B 3, Figs. 16–17). This is a
  correlation, not a tested mechanism.
* **Robustness.** Starting the 3D phase at 3 or 6 ms instead of 12.72 ms
  changes the linear and early nonlinear phases but not the $n=2$-dominated
  saturated state. Without a wall the QH-mode is also reached, with $n=1$
  then linearly unstable (§III, §IV B 3; stated, no figure).
* **Loss of QH-mode.** At $B_\phi=2.0$ T ($q_{95}=2.3$, same shear) $n=2$ is
  linearly stable, an $n=8$ precursor saturates at low amplitude, the
  pedestal keeps building, and an ELM-like burst with $n=2$ and 4 at
  52.1 ms removes about 3% of the thermal energy in about 1 ms (§IV C,
  Figs. 18–20). The authors call it a type-I ELM crash and defer a resolved
  study.

## Access conditions

* **$q_{95}$ windows.** AUG simulations find "$q_{95}$ windows" inside which
  QH-mode exists; inside them external-kink formation prevents the pedestal
  from building up to an ELM, and a nonlinear drop of $q_{95}$ by current
  redistribution, including the self-consistent bootstrap current, lowers
  the growth rates and acts as a saturation mechanism
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §2.1, Abstract;
  Cathey et al. 2024, §3.2, from rigidly raising $q$ at fixed shear). The
  HL-3 runs probe a "much lower edge safety factor" than the AUG study and
  lose the QH-mode between $q_{95}=2.5$ and 2.3 (Liang et al. 2025, §IV C);
  two values do not establish whether 2.5 lies inside a window.
* **Pedestal density.** Raising the particle source in the AUG case gives a
  type-I ELM once the pedestal density exceeds about
  $2.3\times10^{19}$ m$^{-3}$, the threshold seen in the same discharge
  (Cathey et al. 2024, §3.2; Hoelzl et al. 2024, Fig. 2).
* **Torque.** Counter-current torque was once believed necessary;
  QH-mode has since been obtained experimentally with co-current and nearly
  zero torque (Garofalo et al. 2011, as cited by Liang et al. 2025, §I). Both
  JOREK cases reach the QH-mode with no momentum source; Liang et al. (§V)
  state that the self-generated $E\times B$ shear stabilizes the high-$n$
  modes when diamagnetic effects are included, without a separate test.

## Numerics

* **Toroidal resolution.** Doubling the number of toroidal harmonics leaves
  the AUG EHO unchanged (Cathey et al. 2024, fn. 10). The HL-3 runs keep all
  $n\le12$ without periodicity reduction; no convergence study is given
  (Liang et al. 2025, §III).
* **Resistivity.** HL-3 uses $\eta\propto T_e^{-3/2}$ at about 4 times
  Spitzer at $\psi_N=0.95$, a factor of about 3.7 above the neoclassically
  corrected realistic value (§III).

## Qualifications

* **Frequency comparison across devices.** The HL-3 7.5 kHz is compared
  with measured fundamentals on other devices, not with an HL-3 measurement;
  the AUG comparison is with the same discharge.
* **Reviews.** The DIII-D and AUG window results enter through two reviews
  (Hoelzl et al. 2021, 2024); the primary QH paper (Meier et al. 2023) is not
  ingested.
* **Single temperature, no torque.** Both JOREK cases use $T_e=T_i$ and no
  torque source, which affects $E_r$ and the mode frequency (Cathey et al.
  2024, §2.3, §3.2; Liang et al. 2025, §III).

## Contradictions

* **What sets the simulated EHO frequency — qualification.**
  [Cathey et al. (2024)](/sources/cathey-2024.md) (§3.2) attribute the AUG
  mismatch, about 27 kHz simulated against about 10 kHz measured, to the
  missing NBI torque and the single-temperature model ("likely explains").
  [Liang et al. (2025)](/sources/liang-2025.md) use the same model family
  with the same two omissions and obtain 7.5 kHz, "within the range" of
  measured fundamentals (§IV B 2, §V). The two results are not in
  contradiction: the devices, $q_{95}$ (6.8 against 2.5), dominant $n$ (1
  against 2) and pedestals differ, and the HL-3 comparison is with other
  devices. They do show that the two omissions alone do not fix the
  simulated frequency at a value far above experiment, so the AUG
  attribution remains an untested hypothesis (compiler's reading). A run
  with torque and separate temperatures on one of the two cases would test
  it.

# Citations

- [Liang et al. (2025)](/sources/liang-2025.md) — §§I–V, Table I, Figs. 1–20.
- [Cathey et al. (2024)](/sources/cathey-2024.md) — §2.3, §3.2, Table 1, Fig. 3, fn. 10.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.1, Fig. 2.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §5.
- [Becoulet et al. (2022)](/sources/becoulet-2022.md) — §3, §5.
