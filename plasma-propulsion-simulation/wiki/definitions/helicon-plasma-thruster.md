---
type: Definition
title: "Helicon plasma thruster"
description: "An electrodeless, neutralizer-free radiofrequency thruster in which a helicon (whistler) wave sustains a dense plasma that expands through a magnetic nozzle, reaching about 10 mN/kW in laboratory tests and up to 17.8% rf efficiency in a privately communicated result, and whose simulation needs electromagnetic fields, neutral depletion and nozzle physics."
status: established
aliases: [HPT, helicon thruster, helicon double-layer thruster, radiofrequency magnetic-nozzle thruster, electrodeless plasma thruster]
tags: [helicon, magnetic-nozzle, plume, kinetic, hybrid]
timestamp: 2026-10-14T00:00:00Z
---

# Helicon plasma thruster

A helicon plasma thruster produces plasma with a helicon wave launched by an
rf antenna in a dielectric source tube and accelerates it in a
[magnetic nozzle](/definitions/magnetic-nozzle.md). Helicon and ECR waves
are both whistler (R) modes; the helicon has no strict resonance and so
operates over a wide range of $B$, whereas ECR needs 0.0875 T (printed as 875 G) at 2.45 GHz
([Takahashi (2019)](/sources/takahashi-2019.md), §2, Eqs. 3–6, Fig. 3).
Helicon sources reach $10^{18}$–$10^{19}$ m$^{-3}$ (printed as
$10^{12}$–$10^{13}$ cm$^{-3}$) at a few tenths of a pascal (printed as a
few mTorr), with
$T_e\gg T_i$ (§2). The thruster has no electrode in contact with the
plasma and, being current-free, needs no neutralizer (§1, §5.3, §7).
[Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III B,
class it with ICP and ECR thrusters as electromagnetic thrusters, whose
simulation needs Maxwell's equations or a subset.

## Physics a model must capture

* **Thrust generation.** Source electron pressure, the diamagnetic Lorentz
  force in the nozzle and axial momentum lost to the radial wall; see
  [thrust decomposition of a magnetic nozzle](/results/magnetic-nozzle-thrust-decomposition.md).
* **Ion acceleration** by the [current-free double layer](/definitions/current-free-double-layer.md)
  in expanding plasmas ([Takahashi (2019)](/sources/takahashi-2019.md), §5.2–5.4).
* **Mode jump** to the high-density helicon mode, seen in thrusters only at
  low field, about 0.005–0.01 T (printed as 50–100 G), ascribed to the downstream axial boundary
  ([Takahashi (2019)](/sources/takahashi-2019.md), §5.1).
* **Neutral depletion.** In a pulsed helicon thruster about 80% of the
  neutrals are depleted near the exit and the density peak moves upstream in
  time; injecting gas near the exit raised thrust and downstream density by
  25–40% ([Takahashi (2019)](/sources/takahashi-2019.md), §5.6, Fig. 17).
  In Kr and Xe, neutral depletion goes with a measured negative wall force
  (§5.5.3, Fig. 16).
* **Power absorption.** [Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. III B, report a PIC study (their ref. 174) in which helicon-mode
  power is absorbed in the bulk rather than by Trivelpiece–Gould modes, "in
  contrast to a common assumption".
* **Electron cooling and detachment** in the nozzle; see
  [magnetic nozzle](/definitions/magnetic-nozzle.md) and
  [polytropic electron closure](/definitions/polytropic-electron-closure.md).

## Performance

[Takahashi (2019)](/sources/takahashi-2019.md), §6, Table 1, Figs. 22–23,
collects 18 thrust measurements from 0.07 to 6 kW and 0.85 to 67 mN, with rf
efficiency from 0.25% to 17.8% (the efficiency $\eta$ of the
[notation registry](/notation.md) with $P$ the rf power). Most thrusters
reach about 10 mN/kW, with $I_{sp}$ from 100 to 3000 s. The best entry
(Takahashi & Ando 2018, private communication) is 67 mN at 6 kW,
$I_{sp}=3256$ s, 11.2 mN/kW and 17.8%, in argon with a 95 mm source and gas
injection at the exit. The best performers owe their results to a larger
source and a stronger $B$. The first direct thrust measurements (2011) gave
a few mN at several hundred W (§5.5.1).

## Simulation

* **Fully kinetic.** PIC has been applied to double-layer formation, to an
  instability near the nozzle surface (Singh et al. 2013), and, with
  artificially depleted neutrals, to the negative wall force (Takao &
  Takahashi 2015); a PIC simulation coupled with [DSMC](/methods/dsmc.md)
  reproduced neutral depletion qualitatively (Takase et al. 2018)
  ([Takahashi (2019)](/sources/takahashi-2019.md), §5.2, §5.5.2, §5.5.3,
  §5.6). The review gives no numerical parameters for any of them and
  states that the wave and flow models "have not been compared with the
  experiments yet" (§4).
* **Hybrid.** Fluid electrons with PIC ions (ref. 173 of
  [Taccogna et al. (2023)](/sources/taccogna-2023.md)); see
  [hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md). For
  electrodeless thrusters the anomalous coefficient is taken constant
  ([Ahedo (2023)](/sources/ahedo-2023.md), Eq. 18 and following, citing
  ref. 35).
* **Electromagnetic fields.** The explicit electromagnetic CFL limit is
  "typically intractable"; workarounds are quasi-neutral field estimates,
  semi-Lagrangian schemes, implicit and energy-conserving PIC, and
  frequency-domain fields updated about once per rf period, which exclude
  non-linear effects ([Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. III B, Eq. 12). See
  [semi-implicit, implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md).
* **Reduced particle model.** [Gallo et al. (2021)](/sources/gallo-2021.md),
  §4.4, compute $I_{sp}$ and thrust trends of a helicon double-layer thruster
  with a quasi-1D heavy-species model and
  [Boltzmann electrons](/methods/boltzmann-electron-model.md) (about 10 min
  per run); results on the
  [current-free double layer](/definitions/current-free-double-layer.md)
  page.

# Citations

1. [Takahashi (2019)](/sources/takahashi-2019.md), §1, §2, §4, §5.1–5.6, §6, Table 1, Figs. 3, 16–17, 22–23.
2. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III B, Eq. 12 (accepted manuscript).
3. [Gallo et al. (2021)](/sources/gallo-2021.md), §4.4.
4. [Ahedo (2023)](/sources/ahedo-2023.md), Eqs. 18–21.
