---
type: Definition
title: "Pulsed plasma thruster"
description: "An electric thruster that ablates a solid propellant (usually PTFE) in a microsecond discharge and accelerates the products, with low efficiency, dense continuum-to-kinetic plasma, a spark-plug ignition phase and late-time ablation that fluid models miss; laser ablation variants separate ablation from acceleration."
status: established
aliases: [PPT, ablative pulsed plasma thruster, APPT, micro-PPT, laser ablation plasma thruster, LA-PPT]
tags: [pulsed-plasma-thruster, fluid, plume, dsmc]
timestamp: 2026-10-14T00:00:00Z
---

# Pulsed plasma thruster

A pulsed plasma thruster (PPT) ablates a solid propellant, usually
Teflon (PTFE, C$_2$F$_4$), in a discharge of a few µs and accelerates the
ablated material ([Boyd (2005)](/sources/boyd-2005.md), §3.5). Each pulse
delivers an impulse bit $I_{\mathrm{bit}}$.

## Operating range

* [Boyd (2005)](/sources/boyd-2005.md), Table 1: thrust 0.05–10 mN,
  $I_{sp}$ 500–2000 s, number density $10^{20}$–$10^{22}$ m$^{-3}$, regime
  continuum/kinetic; efficiency 10–20%, one spacecraft in operation in 2005
  (§3.5). [Zhang et al. (2018)](/sources/zhang-2018.md), §1, give the
  efficiency of classic PPTs as "often around 10–15%".
* [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A, class
  pulsed-arc thrusters (PAT) among electrostatic thrusters, which need only
  Poisson's equation, and estimate the cost of explicit PIC for them: density
  peaks of $10^{22}$ m$^{-3}$ give $\lambda_D$ of order $10^{-7}$ m and, with
  $T_e\approx10$ eV, $\Delta t$ of order $10^{-13}$ s, hence about $10^8$
  steps for "at least a few µs"; enlarged permittivity, reduced ion mass
  and size scaling are still used for them. See
  [resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
  and [permittivity, ion-mass and geometric scaling](/methods/pic-acceleration-scaling.md).
* [Adamovich et al. (2017)](/sources/adamovich-2017.md), §12, cite the
  liquid-fed PPT and the vacuum-arc thruster among cathode-less options for
  small satellites.

## Modelling

* **MHD and late-time ablation.** [Boyd (2005)](/sources/boyd-2005.md),
  §3.5, describes the unsteady ALE MHD code MACH2 with equilibrium vapour
  pressure of Teflon and chemical equilibrium. It sometimes predicts
  performance well, but the agreement is "almost certainly fortuitous"
  because the predicted ablated mass is an order of magnitude below the
  measured one. The missing mass motivated the concept of late-time
  ablation: neutral mass ablated after the current pulse.
* **Chained micro-PPT model.** For the AFRL micro-PPT (6.35 mm diameter) an
  ablation model, a Knudsen-layer fluid model and a DSMC-PIC plume model
  are chained ([Boyd (2005)](/sources/boyd-2005.md), §3.5, Fig. 20). See
  [DSMC](/methods/dsmc.md).
* **Accuracy.** Boyd places PPT performance prediction within 10–20%, with
  arcjets and Hall thrusters (§4).

## Ignition by a spark plug

[Sun & Wu (2018)](/sources/sun-2018.md) fired a parallel-plate PTFE PPT
(electrodes 25 mm long, 12 mm wide, 25 mm gap; coaxial semiconductor spark
plug; 1130 and 1430 V) with a normal propellant face, an inclined face and
no propellant. This is an experiment with an algebraic ionization criterion,
no simulation.

* Without propellant the thruster still discharges with near-identical
  voltage and current waveforms; the light is confined to the side ceramics
  at the start of the channel, which the authors read as a surface flashover
  (§3, Figs. 4–6).
* The spark-plug voltage lasts about 15 µs against a discharge of about
  5.5 µs (§3, Fig. 7).
* Proposed mechanism with propellant (not proved): spark-plug electrons form
  an initial conductive path, the initial current of about 500 A ablates
  neutral gas, and the gas is ionized if an electron gains more energy over
  one $\lambda_{\mathrm{mfp}}$ in a uniform field than a weighted ionization
  energy of C and F (§3, Eqs. 1–4). This gives a minimum discharge voltage
  of about 468 V; the inputs of the estimate are not printed.
* Measured success rate over 2000 ignitions falls from 85% at 600 V to 39%
  at 450 V (§3). At 1430 V, inclining the propellant face lowers the mass
  shot and the success rate, from 4.23 µg / 99% (normal) to 3.01 µg / 72%
  (inclined 5/25) (Table 2).

## Laser ablation plasma thruster

The laser ablation plasma thruster of
[Zhang et al. (2018)](/sources/zhang-2018.md) separates laser ablation of a
metal target, inside a ceramic tube, from electromagnetic acceleration. Its
experiments (their ref. 1, attributed, not shown) give $I_{sp}\approx8000$ s
and thrust efficiency about 90% with metallic propellant (§1). Zhang et al.
model only the ablation and plume stage; see the
[laser-ablation plume model](/methods/laser-ablation-plume-model.md). At a
fluence of $10^5$ J/m$^2$ (printed as 10 J/cm$^2$) the computed thrust peaks at 175 N with a pulse
width below 0.3 µs, and $I_{\mathrm{bit}}\approx14$ µN·s at 1.5 µs (§3.5,
Fig. 14).

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), Table 1, §3.5, §4, Fig. 20.
2. [Sun & Wu (2018)](/sources/sun-2018.md), §2, §3, Eqs. 1–4, Figs. 4–7, Table 2.
3. [Zhang et al. (2018)](/sources/zhang-2018.md), §1, §3.5, Fig. 14.
4. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A (accepted manuscript).
5. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §12.
