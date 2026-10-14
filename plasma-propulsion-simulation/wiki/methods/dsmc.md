---
type: Method
title: "Direct simulation Monte Carlo (DSMC)"
description: "Particle solution of the Boltzmann equation for rarefied gas in which simulated molecules move collisionlessly over a time step and then collide in randomly chosen pairs within each cell, used in electric propulsion for resisto-jet and arcjet nozzles, heavy-species collisions in PIC-DSMC plume and ion-optics codes, and neutral flows."
status: established
aliases: [DSMC, direct simulation Monte Carlo, PIC-DSMC, sophisticated DSMC]
tags: [dsmc, kinetic, hybrid, plume, numerics]
timestamp: 2026-10-14T00:00:00Z
---

# Direct simulation Monte Carlo (DSMC)

DSMC represents a gas by simulated molecules, each standing for $W$ real
molecules, and solves the Boltzmann equation statistically. In the
satellite-aerodynamics runs of
[Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md), §3, each
simulated molecule represents $10^9$–$10^{10}$ real ones. The method
decouples molecular motion from collisions: molecules first move, then
collision partners are chosen at random within a cell, with a collision
probability proportional to the cross section times the relative speed
([Boyd (2005)](/sources/boyd-2005.md), §2.2.1, attributing the method to
Bird). The collision types Boyd lists are momentum exchange, charge
exchange, internal-energy exchange and chemistry (§2.2.1).

## Regime of use

* Continuum descriptions fail for $\mathrm{Kn}>0.01$, where collisions can
  no longer keep the velocity distributions near Maxwellian
  ([Boyd (2005)](/sources/boyd-2005.md), §2.2.1). A resisto-jet goes from
  continuum at the throat to $\mathrm{Kn}\approx0.1$ at the exit (exit
  density $10^{21}$ m$^{-3}$, a few cm exit diameter; §3.1).
* At the other end, [Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md),
  §4, state, citing Moss, that free-molecular flow starts at
  $\mathrm{Kn}=50$. Their satellite at 150 km has $\mathrm{Kn}\approx31$
  (mean free path about 32 m over a 1.04 m body), so they use DSMC rather
  than free-molecular formulas, to capture interactions between free-stream
  and re-emitted molecules.

## Validity conditions

* **Time step and cell size.** $\Delta t$ must be much smaller than the mean
  collision time, and random pairing is accurate only when the cell size is
  of order $\lambda_{\mathrm{mfp}}$ ([Boyd (2005)](/sources/boyd-2005.md),
  §2.2.1).
* **Applied in a PIC-DSMC plume code.** [Cai et al. (2018)](/sources/cai-2018.md),
  §2.3, require cells larger than $\lambda_D$ (about $10^{-5}$ m) and of
  order $\lambda_{\mathrm{mfp}}$ (about 0.1 m). This is the reverse of the
  explicit-PIC requirement $\Delta x\lesssim\lambda_D$ of
  [explicit PIC](/definitions/explicit-pic-resolution-constraints.md); it is
  consistent only because the code solves no Poisson equation (its
  electrons follow the [Boltzmann relation](/methods/boltzmann-electron-model.md)).
  The run uses about 2 million tetrahedral cells (1, 2 and 4 million
  tested; the axial current density converges beyond 0.3 m from the exit),
  $\Delta t=1\times10^{-7}$ s and $W=2\times10^8$.
* **Collision-separation check.** [Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md),
  §3, report that the DS3V program displays, per collision cell, the ratio
  of the mean collision separation to $\lambda_{\mathrm{mfp}}$. It must stay
  below 1 everywhere, and Bird suggests 0.2 for an optimal-quality run. Their
  runs give 0.003–0.062 (Tables 2a–2d). Steady state is judged when the time
  history of the number of simulated molecules becomes "jagged" within a
  standard-deviation band; the ratio of simulated time to fluid-dynamic
  time was 72–309 in their runs (Tables 2a–2d) against a stated rule of
  thumb of order 10 (§4).
* **"Sophisticated" DSMC.** The same paper (§3) lists, attributing them to
  Bird (2006), Bird et al. (2009) and Gallis et al. (2009): separate
  collision and sampling cells with cell adaptation, promotion of
  nearest-neighbour collisions, automatic setting of the numbers of cells
  and molecules from the memory budget and free-stream density, radial
  weighting for axisymmetric flows, an "optimal time step", and no
  repeated collisions of the same pair. No formula or criterion value is
  given there.

## DSMC and Monte Carlo collisions

[Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. II step 3, Eq. 4,
write the collision step of a particle code as a fraction $P_c$ of the
distribution being replaced by its post-collision form, and distinguish two
classes: [Monte Carlo collisions](/methods/monte-carlo-collisions.md), where
the target species is a fluid background, and DSMC, where both partners are
macroparticles. [Boyd (2005)](/sources/boyd-2005.md), §2.2.1, names MCC as
the scheme of hybrid particle–fluid codes for heavy-species collisions with
fluid electrons.

The heavy-species code of [Gallo et al. (2021)](/sources/gallo-2021.md),
§2.4, uses neither for its electron-impact ionization: it states that DSMC
does not apply because its electrons are a fluid, and that standard MCC
does not apply because neutrals dominate, the neutral flux falls along the
channel and the ion and neutral masses differ. It transfers mass from
neutral to ion macroparticles cell by cell instead. This concerns
ionization by fluid electrons; [Cai et al. (2018)](/sources/cai-2018.md)
apply DSMC only to heavy–heavy collisions, so the two statements do not
conflict.

## Uses in electric propulsion

* **Nozzle flows.** DSMC of a cold-flow H$_2$ resisto-jet agrees within 5%
  with the measured $I_{sp}$ and did better than a Navier–Stokes solution
  against Pitot data; DSMC of a 1.4 kW H$_2$ arcjet, started from a
  continuum solution at the throat and with kinetic Ohmic heating, gives
  $I_{sp}$ within 10% ([Boyd (2005)](/sources/boyd-2005.md), §3.1–3.2,
  Figs. 3, 7, reproducing the author's earlier work).
* **Heavy-species collisions in PIC-DSMC codes.** Ion-optics DSMC-PIC with
  multiply charged ions gives "excellent" accel-grid current agreement for
  the UK-10 optics; hollow-cathode and micro-PPT plume models couple DSMC
  heavy species with fluid electrons ([Boyd (2005)](/sources/boyd-2005.md),
  §3.3.2, §3.3.3, §3.5, Fig. 10). [EX-PWS](/software/ex-pws.md) treats
  elastic and [charge-exchange](/definitions/charge-exchange-ions.md)
  collisions of Xe, Xe$^+$, Xe$^{2+}$ and charge-exchange ions by DSMC, with
  the facility background gas as temporary particles created in every cell
  at every step, not tracked, whose collisions change only the simulated
  particle's velocity ([Cai et al. (2018)](/sources/cai-2018.md), §2.1,
  eqs. 1–6). See [hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md).
* **Neutral flows.** [Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. III C d, report a DSMC study (Boccelli et al.) in which reversed
  propellant injection raises $\eta_m$ by at most 30%, and name an
  octree PIC-DSMC code with MPI-CUDA parallelism (CHAOS, their ref. 290).
  [Takahashi (2019)](/sources/takahashi-2019.md), §5.6, reports a PIC
  simulation coupled with DSMC (Takase et al. 2018) whose neutral-depletion
  results are qualitatively consistent with experiment in a pulsed
  [helicon thruster](/definitions/helicon-plasma-thruster.md).
* **Codes named.** DS3V version 2.6 (Bird) in
  [Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md), §3;
  [EX-PWS](/software/ex-pws.md) in [Cai et al. (2018)](/sources/cai-2018.md);
  CHAOS in [Taccogna et al. (2023)](/sources/taccogna-2023.md).

Surface boundary conditions of DSMC codes are on
[gas–surface interaction models](/methods/gas-surface-interaction.md).

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §2.2.1, §3.1, §3.2, §3.3.2, §3.3.3, §3.5, Figs. 3, 7, 10.
2. [Cai et al. (2018)](/sources/cai-2018.md), §2.1, §2.3, eqs. 1–6, Fig. 2.
3. [Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md), §3, §4, Tables 2a–2d.
4. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. II (Eq. 4), Sec. III C d (accepted manuscript).
5. [Takahashi (2019)](/sources/takahashi-2019.md), §5.6.
6. [Gallo et al. (2021)](/sources/gallo-2021.md), §2.4.
