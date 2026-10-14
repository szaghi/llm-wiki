---
type: Definition
title: "Charge-exchange ions"
description: "Slow ions created when a fast ion takes an electron from a slow neutral, which carry little momentum but populate the plume wings and the backflow, erode ion-optics accel grids, and are modelled as DSMC or MCC collisions or as a separate low-energy ion fluid."
status: established
aliases: [CEX ions, charge exchange, charge-exchange collisions, CEX]
tags: [plume, ion-thruster, hall-thruster, dsmc, mcc, fluid]
timestamp: 2026-10-14T00:00:00Z
---

# Charge-exchange ions

In a charge-exchange (CEX) collision a fast ion takes an electron from a
slow neutral. The products are a fast neutral and a slow ion, the CEX ion,
which the local electric field then accelerates in a direction set by the
field rather than by the beam. [Cai et al. (2018)](/sources/cai-2018.md),
§2.1, eqs. 5–6, write the single and double reactions for xenon:
$\mathrm{Xe}^+_{\mathrm{fast}}+\mathrm{Xe}_{\mathrm{slow}}\to\mathrm{Xe}_{\mathrm{fast}}+\mathrm{Xe}^+_{\mathrm{slow}}$
and
$\mathrm{Xe}^{2+}_{\mathrm{fast}}+\mathrm{Xe}_{\mathrm{slow}}\to\mathrm{Xe}_{\mathrm{fast}}+\mathrm{Xe}^{2+}_{\mathrm{slow}}$.

## Why they matter

* **Grid erosion.** CEX ions drive the erosion of gridded-ion-thruster
  accel grids ([Boyd (2005)](/sources/boyd-2005.md), §3.3.3). Boyd reports
  PIC with Monte Carlo CEX giving erosion depths over 1000 h (Peng et al.),
  and a 3D code reproducing the pits-and-grooves erosion of the NSTAR
  8200 h life test, which needed a long downstream domain to capture the
  CEX ions flowing back to the grid (Wang et al.; Figs. 11–12).
* **Plume wings and backflow.** In the 3D ion-thruster plume of
  [Cai et al. (2018)](/sources/cai-2018.md), §4.2, Figs. 13–14, the CEX ion
  density forms a "wing" near the exit, enlarged and densified in front of
  an impinged plate and decaying behind it; higher-energy single CEX ions
  are produced in the annular wing region within about 0.5 m of the exit,
  and denser CEX regions have lower mean energy. The hybrid plume model
  around a spacecraft reported by [Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. IV A, Fig. 9 (Cichocki et al., $\gamma=1.1$, with CEX), finds that
  adding non-neutral regions raises the ion backflow current by about 20%.
* **Small momentum share.** On a plate 0.6–1.0 m downstream of the LIPS-200
  ion thruster, single and double CEX ions together carry less than 0.1% of
  the momentum, against about 85% for Xe$^+$
  ([Cai et al. (2018)](/sources/cai-2018.md), §4.1, Table 3).
* **Thrust of magnetic nozzles.** [Takahashi (2019)](/sources/takahashi-2019.md),
  §4 and §5.6, reports that CEX conserves total momentum and that the
  momentum gain of an expanding plasma increases when the CEX mean free
  path is shorter than the scale of the potential drop (Makrinich &
  Fruchtman 2009; Fruchtman 2011, 2014).

## How codes represent them

* **DSMC between macroparticles.** [EX-PWS](/software/ex-pws.md) tracks CEX
  ions as separate macroparticle species and handles the reactions, and the
  elastic CEX-ion–Xe collision, by [DSMC](/methods/dsmc.md), with cross
  sections from an earlier paper of the group
  ([Cai et al. (2018)](/sources/cai-2018.md), §2.1, eqs. 1–6). Boyd lists
  charge exchange among the DSMC collision types
  ([Boyd (2005)](/sources/boyd-2005.md), §2.2.1).
* **MCC against a neutral background.** The PIC-MCC code of
  [Troyetsky et al. (2026)](/sources/troyetsky-2026.md) evaluates CEX at the
  relative energy $\tfrac12m_i|\mathbf v_i-\mathbf v_n|^2$, samples the
  neutral from a drifting Maxwellian at 0.1 eV, and swaps the ion and
  neutral velocities (§PIC-MCC model). See
  [Monte Carlo collisions](/methods/monte-carlo-collisions.md).
* **A second ion fluid.** The same paper's
  [five-moment fluid model](/methods/five-moment-fluid-model.md) carries
  high-energy and low-energy Xe$^+$ fluids (Eqs. 14–26). CEX converts
  high-energy ions to low-energy ones at the frequency
  $\nu_{in}=n_n\,\sigma_{in}\,g$, with $\sigma_{in}$ the CEX cross section
  of Miller et al. evaluated at the relative speed $g$ of the high-energy
  ions (Eq. 21). Ionization feeds a fraction of its new ions to the
  high-energy fluid and the rest to the low-energy one, and CEX moves
  high-energy ions to the low-energy fluid at a rate weighted by one minus
  that fraction; the fraction ramps linearly in the local potential, from 0
  below 30 V to 0.999 above 60 V (the value below 1 is for stability).

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §2.2.1, §3.3.3, Figs. 11–12.
2. [Cai et al. (2018)](/sources/cai-2018.md), §2.1, eqs. 1–6, §4.1, Table 3, §4.2, Figs. 13–14.
3. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. IV A, Fig. 9 (accepted manuscript).
4. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), Eqs. 14–26, §PIC-MCC model.
5. [Takahashi (2019)](/sources/takahashi-2019.md), §4, §5.6.
