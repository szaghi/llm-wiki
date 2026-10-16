---
type: Definition
title: "Shattered pellet injection and massive material injection"
description: "Massive material injection (MMI) is the deliberate injection of large amounts of deuterium and/or impurities to trigger a controlled disruption; shattered pellet injection (SPI), the basis of the ITER disruption mitigation system, breaks a cryogenic pellet into fragments whose ablation is modelled in MHD codes by per-fragment ablation laws and localized density sources."
status: established
aliases: [SPI, MMI, MGI, massive gas injection, disruption mitigation system, DMS]
tags: [disruption, impurities, runaway-electrons, mhd]
timestamp: 2026-10-16T12:00:00Z
---

# Shattered pellet injection and massive material injection

**Massive material injection (MMI)** is the injection of large quantities of
deuterium and/or impurities (neon, argon) into a tokamak plasma to make a
[disruption](/definitions/disruption.md) controlled: radiate the thermal
energy uniformly, raise the density against
[runaway electrons](/definitions/runaway-electrons.md), and set the
current-quench rate. Its forms in the sources are **massive gas injection
(MGI)**, **shattered pellet injection (SPI)** and dispersive shell pellet
injection ([Hu et al. (2021b)](/sources/hu-2021-b.md), §1). In SPI a
cryogenic pellet is shattered into fragments before entering the plasma;
SPI is the planned basis of the ITER disruption mitigation system (DMS)
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6;
[Bhole et al. (2023)](/sources/bhole-2023.md), §1).

## Models in MHD codes

**Fragment ablation and deposition (JOREK).** Each fragment follows a straight
line at constant velocity and ablates by a neutral-gas-shielding scaling;
the ablated material enters as a density source localized around the
fragment in the poloidal plane and toroidally
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8, Eq. 44). In
[Bhole et al. (2023)](/sources/bhole-2023.md) (§4.1, Eqs. 47–48) the
fragment radius to the power 5/3 decreases at a rate proportional to
$n_e^{1/3}T_e^{5/3}$, fragment sizes follow a statistical fragmentation
model, 100 fragments are launched with spreads in speed and angle, and each
deposits through a Gaussian source in $(R,Z)$ and in $\phi$. Results
converge in the toroidal source width for deuterium pellets, but not
necessarily for impurity pellets, whose radiated power scales inversely
with that width ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8).
KSTAR SPI runs still use an artificially enlarged deposition area for
numerical reasons ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2).
The ablation laws (mixed-pellet coefficient, magnetic reduction factor,
local or flux-averaged evaluation), the fragmentation model and the
deposition widths used by the chunk-2 SPI studies
([Hu et al. (2021)](/sources/hu-2021.md), [Hu et al. (2023)](/sources/hu-2023.md),
[Hu et al. (2024)](/sources/hu-2024.md)) are collected on
[pellet ablation and fragmentation models](/methods/pellet-ablation-models.md).
Narrowing the toroidal width from 0.5 to 0.3 rad raises the radiation of
neon–deuterium SPI in ITER at equal assimilation, but less than
proportionally ([Hu et al. (2023)](/sources/hu-2023.md), §4.2, Fig. 19; see
Contradictions), and a wide toroidal source under-predicts
[plasmoid drift](/definitions/plasmoid-drift.md)
([Kong et al. (2025)](/sources/kong-2025.md), §3.2, §5).

**Gas injection.** MGI is represented by a fixed density source of Gaussian
shape: central argon or neon injection at ≈$4.37\times10^{23}$ atoms/s into
DIII-D in [Hu et al. (2021b)](/sources/hu-2021-b.md) (§2.1, Eq. 18, §3).
Idealized benchmarks replace the injection by an instantaneous uniform
appearance of deuterium and neon inside the plasma
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §III.A, §IV.A).

**Impurity physics.** The injected impurities enter through a
[coronal-equilibrium](/methods/coronal-equilibrium-impurity-model.md) fluid
(charge states in instantaneous ionization–recombination balance, ionization
energy carried as potential energy; [Bhole et al. (2023)](/sources/bhole-2023.md),
Eqs. 11–13; [Bandaru et al. (2024)](/sources/bandaru-2024.md), §II) or a
[collisional-radiative](/methods/collisional-radiative-impurity-model.md)
treatment with charge-state-resolved super-particles
([Hu et al. (2021b)](/sources/hu-2021-b.md), §2;
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2). Coronal equilibrium
underestimates the radiation of weakly ionized states early in the
injection ([Hu et al. (2021b)](/sources/hu-2021-b.md), §1). Neutral
deuterium is carried by a [fluid neutral model](/methods/fluid-neutral-models.md)
in [Bandaru et al. (2024)](/sources/bandaru-2024.md) (§II).

**Numerics.** The steep pressure gradients around ablation clouds make
full-MHD SPI runs fail in the linear solver without stabilization;
[shock-capturing artificial viscosity](/methods/shock-capturing-artificial-viscosity.md)
lets them pass through the thermal quench and cuts the GMRES time to
$t\approx1.5$ ms in a 3D neon case from 13.6 h to 5 h
([Bhole et al. (2023)](/sources/bhole-2023.md), §4.2–4.3, Table 1;
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5).

## Dynamics found in simulations

- **SPI regimes.** The ordering of the shard transit time against the
  resistive current-decay time of the cooled region decides whether helical
  cooling and the 1/1 kink (fast shards) or an edge-to-core tearing cascade
  (slow shards) triggers the [thermal quench](/definitions/thermal-quench.md).
  The current-decay time grows like the square of the machine size and the
  transit time linearly, which explains part of the difference between JET
  and ASDEX Upgrade deuterium SPI ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
  §6.2.1).
- **Deuterium dilution.** Pure-deuterium SPI keeps a relatively high
  post-cooling temperature and can dilute the plasma without an immediate
  TQ, which is a candidate route to runaway-electron avoidance; it works in
  JOREK in the absence of pre-existing islands and at low background
  impurity density (same section). The response to massive deuterium
  injection depends on the injection phase relative to a pre-existing island
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2).
- **Assimilation.** Deposited material first expands along field lines at
  the sound speed; SPI assimilates and mixes better than MGI in JET
  simulations because shards penetrate deeper
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.3). Plasmoid drifts
  are essential for assimilation in JET deuterium SPI; ITER neon–deuterium
  SPI shards can reach the core before the edge radiative collapse
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2). The primary
  study of the ITER statement is [Hu et al. (2023)](/sources/hu-2023.md)
  (§3.1–3.2, Fig. 8): in a 15 MA L-mode the fragments reach the core while
  the post-injection region stays at $O(100)$ eV, especially at 500 m/s.
  Assimilation is self-regulated: flux-averaged instead of local ablation,
  or removing the magnetic reduction factor, changes the assimilated neon
  only mildly but the radiated power strongly (§4.1, Figs. 16, 18), and
  background Be and W radiate about $10^3$ times less than the injected
  neon (§4.3, Fig. 20). In an ITER baseline H-mode with 1%-neon pellets
  the opposite ordering holds: plasmoid drift collapses the pedestal and
  loses over 100 MJ before the fragments penetrate, and only ≈20% of the
  neon is assimilated ([Hu et al. (2024)](/sources/hu-2024.md), §3,
  Table 2); the targets differ (L-mode against a 370 MJ pedestal), so this
  is a dependence on the target, recorded under Qualifications.
- **Core penetration and the 1/1 kink.** Material deposited on or inside
  $q=1$ is convected into the core by the 1/1 kink that the fragments
  trigger; mixed hydrogen–neon pellets, which penetrate deeper, give much
  better core neon penetration than pure neon pellets of the same neon
  content ([Hu et al. (2021)](/sources/hu-2021.md), §4.1, Fig. 14). Kink
  convection moves density cells $O(1)$ m in 0.2 ms while the fragments move
  0.1 m, and an axisymmetric twin run stays hollow
  ([Hu et al. (2023)](/sources/hu-2023.md), §3.1, Figs. 6–7). The core
  temperature can collapse more than 100 µs before the material mixes into
  the core, leaving a hollow density (Hu et al. 2021, §3). Transient
  [electron temperature holes](/results/electron-temperature-hole.md) form
  in the fragment plume (Hu et al. 2023, §3.2).
- **Plasmoid drift.** The over-pressured ablation cloud drifts toward the
  low-field side in $\mathbf E\times\mathbf B$; braking by shear Alfvén
  waves and parallel currents, the size of the flow region and the
  toroidal source width set its speed; see
  [plasmoid drift](/definitions/plasmoid-drift.md)
  ([Kong et al. (2025)](/sources/kong-2025.md); [Hu et al. (2024)](/sources/hu-2024.md)).
- **Radiation asymmetry.** With SPI from a single toroidal location the
  toroidal peaking factor of the radiated power can exceed the ITER target
  of 2 during the pre-TQ and early TQ; multiple injection locations reduce it
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.4). The primary
  simulations are [Hu et al. (2021)](/sources/hu-2021.md) (§4.3, §5): a
  peaking factor above 2 with the helicity of the triggering surface, and
  dual injection mitigating it even with a 1 ms delay; the first-wall
  energy impact of ITER H-mode dual SPI is in
  [Hu et al. (2024)](/sources/hu-2024.md). Details on
  [radiation asymmetry](/definitions/radiation-asymmetry.md).
- **Injection symmetry and MHD.** Synchronized dual SPI makes even-$n$
  modes dominate and removes the 1/1 kink motion; mono-SPI "can be seen as
  an asymmetric dual-SPI with extremely long delay"
  ([Hu et al. (2021)](/sources/hu-2021.md), §5, Figs. 17, 19–20).
- **Injection speed.** Slower fragments (200 against 500 m/s) give stronger
  radiative cooling at equal penetration and a larger MHD amplitude at core
  relaxation, with comparable neon assimilation
  ([Hu et al. (2023)](/sources/hu-2023.md), §3.1–3.2, Figs. 4, 8–9).
- **Full MHD.** Neon SPI into a JET-like plasma (pulse 85943) gives a
  thermal quench 2–3 ms after injection with 3/1, 2/1 and later 1/1
  structures and an $I_p$ spike, qualitatively like the earlier reduced-MHD
  SPI runs ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.3.1, §5).
- **Forces.** Impurity injection during a VDE reduces the vertical wall force
  ([vertical-force mitigation](/results/vertical-force-mitigation.md)).
- **Validation.** JET deuterium and mixed SPI simulations reproduce key
  radiation observations; ASDEX Upgrade SPI reproduces the double radiation
  peak qualitatively; KSTAR SPI gives good density agreement and
  qualitative bolometry agreement ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md),
  §3.2). The DIII-D argon and neon gas-injection case is the axisymmetric
  code-to-code reference ([DIII-D gas-injection impurity benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md)).
- **Runaway electrons.** Coupling the runaway-electron fluid model with the
  SPI model in 3D is possible in principle, but the effect of runaways on
  pellet ablation is not yet included ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §V).

## Qualifications

**Plasmoid drift: essential or detrimental.** "Plasmoid drifts are
essential for assimilation" in JET deuterium and mixed SPI simulations
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2), while in an ITER
baseline H-mode with LFS injection of 1%-neon pellets the drift expels
material and reduces assimilation ([Hu et al. (2024)](/sources/hu-2024.md),
§3). Machine, pellet composition and target differ; a higher neon
fraction or a degraded pedestal suppresses the drift (Hu et al. 2024).
Context-dependent, not contradictory; conditions on
[plasmoid drift](/definitions/plasmoid-drift.md).

**Core before edge.** The statement that ITER neon–deuterium shards reach
the core before the edge radiative collapse (Hoelzl et al. 2024, §3.2;
Hu et al. 2023) holds for L-mode targets; in the ITER baseline H-mode with
low-neon pellets the edge stochastizes and the pedestal collapses first
(Hu et al. 2024, §3).

**Convergence in the toroidal source width.** Hoelzl et al. (2021, §2.8)
state that results converge in the toroidal width for deuterium pellets.
The plasmoid drift of a deuterium source does not: a wider source brings
Pégourié braking in earlier and slows the drift
([Kong et al. (2025)](/sources/kong-2025.md), §3.2). Convergence of
assimilated quantities does not imply converged drift.

## Contradictions

**Scaling of impurity radiation with the toroidal source width — Open.**
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§2.8) state that for
impurity pellets the radiated power is proportional to the inverse of the
toroidal source width. [Hu et al. (2023)](/sources/hu-2023.md) (§4.2,
Fig. 19) find that narrowing the width from 0.5 to 0.3 rad raises the
radiation of ITER neon–deuterium SPI at equal assimilation "less than
proportional" to the width change, and attribute the weaker dependence to
parallel relaxation and the merging of plasmoids into a "plasmoid
conglomerate". Both agree on the direction and on the conclusion that
elongated sources under-estimate radiation. They disagree on the
exponent, unless the review's proportionality is meant loosely or refers
to a single isolated source. A width scan over more than two values in a
single setup would settle it.

## Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8, §6, §6.2.1–6.2.4.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2, §5.
- [Bhole et al. (2023)](/sources/bhole-2023.md), §1, §4.
- [Hu et al. (2021b)](/sources/hu-2021-b.md), §1–3.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §II–V.
- [Hu et al. (2021)](/sources/hu-2021.md), §2.2, §3–6.
- [Hu et al. (2023)](/sources/hu-2023.md), §2–5.
- [Hu et al. (2024)](/sources/hu-2024.md), §2–5.
- [Kong et al. (2025)](/sources/kong-2025.md), §3.2, §5.
