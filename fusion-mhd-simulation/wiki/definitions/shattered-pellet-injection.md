---
type: Definition
title: "Shattered pellet injection and massive material injection"
description: "Massive material injection (MMI) is the deliberate injection of large amounts of deuterium and/or impurities to trigger a controlled disruption; shattered pellet injection (SPI), the basis of the ITER disruption mitigation system, breaks a cryogenic pellet into fragments whose ablation is modelled in MHD codes by per-fragment ablation laws and localized density sources."
status: established
aliases: [SPI, MMI, MGI, massive gas injection, disruption mitigation system, DMS]
tags: [disruption, impurities, runaway-electrons, mhd]
timestamp: 2026-10-16T00:00:00Z
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
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2).
- **Radiation asymmetry.** With SPI from a single toroidal location the
  toroidal peaking factor of the radiated power can exceed the ITER target
  of 2 during the pre-TQ and early TQ; multiple injection locations reduce it
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.4).
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

## Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8, §6, §6.2.1–6.2.4.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2, §5.
- [Bhole et al. (2023)](/sources/bhole-2023.md), §1, §4.
- [Hu et al. (2021b)](/sources/hu-2021-b.md), §1–3.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §II–V.
