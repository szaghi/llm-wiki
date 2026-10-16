---
type: Definition
title: "Massive gas injection"
description: "Massive gas injection (MGI) is the disruption-mitigation scheme that puffs a large quantity of deuterium and noble gas through fast valves into the plasma edge; MHD codes represent it by a localized neutral or density source outside or near the separatrix, and its simulated thermal quench proceeds by a tearing-mode cascade from q = 2 inward or by a 1/1 mode that pulls the gas into the core, with toroidal radiation peaking set by the number and arrangement of the valves."
status: established
aliases: [MGI, gas injection, massive gas puff, multi-valve MGI]
tags: [disruption, impurities, neutrals, mhd, tokamak]
timestamp: 2026-10-16T18:00:00Z
---

# Massive gas injection

**Massive gas injection (MGI)** is one form of massive material injection:
a fast valve releases a large quantity of gas (deuterium, a noble gas such
as neon or argon, or a mixture) which reaches the plasma edge, is ionized
there, and makes the [disruption](/definitions/disruption.md) controlled by
radiating the thermal energy and raising the density
([Hu et al. (2021b)](/sources/hu-2021-b.md), §1). The pellet-based
alternatives, [shattered pellet injection](/definitions/shattered-pellet-injection.md)
and dispersive shell pellets, deliver the material deeper; SPI
"assimilates and mixes better than MGI" in JET simulations because the
shards penetrate further ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§6.2.3).

**Why MGI or SPI.** ITER chose SPI because its long injection line would
make gas delivery too slow; on a compact device such as SPARC the short
tube removes that obstacle, and MGI is the simpler and more robust choice
([Izzo et al. (2025)](/sources/izzo-2025.md), §I, citing Baylor et al.
2015).

## Source models in MHD codes

- **Fixed Gaussian density source (JOREK).** Axisymmetric JOREK runs of the
  DIII-D argon and neon injection deposit about $4.37\times10^{23}$
  atoms/s through a Gaussian source centred on the magnetic axis, with a
  toroidal width taken large ([Hu et al. (2021b)](/sources/hu-2021-b.md),
  §3, Eq. 18). This is the
  [DIII-D gas-injection impurity benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md)
  of Lyons et al. (2019), the axisymmetric code-to-code reference for MGI
  impurity physics.
- **Edge neutral source per valve (NIMROD).**
  [Izzo et al. (2025)](/sources/izzo-2025.md) (§II A, Fig. 1) deposit all
  neutrals between the equilibrium separatrix and the simulation boundary,
  radially flat with a sharp tanh drop at the separatrix, Gaussian in
  poloidal angle (half-width 6.4°) and von Mises in toroidal angle, one
  lobe per valve. The neutrals are cold, "do nothing except diffuse and
  ionize", with a diffusivity of 10 m²/s, and equilibrate instantly with
  the background once ionized. Each neon charge state has its own
  continuity equation, advected with the single fluid velocity
  ([NIMROD](/software/nimrod.md);
  [collisional-radiative impurity model](/methods/collisional-radiative-impurity-model.md)).
  A 4 eV floor temperature, which is also the initial temperature outside
  the separatrix, holds the deposited gas until it diffuses across the
  separatrix, since no energy is available for ionization at the floor.
- **Deuterium in the source.** The SPARC injection is $10^{23}$ D$_2$
  molecules and $1.11\times10^{22}$ Ne atoms over 2 ms. The low-resolution
  runs take 10% of the deuterium as assimilated and spread over the plasma
  at $t=0$, discard the rest, and inject pure neon; the high-resolution
  runs put 20% of the deuterium back into the localized source, which
  multiplies the localized injection by almost 5. The largest numerically
  tractable deuterium source was not established (Izzo et al. 2025, §II A).

## Thermal-quench dynamics

**Tearing cascade (JET).** In JOREK deuterium MGI into JET, the
cold front reaches $q=2$ and destabilizes a large 2/1 tearing mode
boosted by helical cooling inside the island; the flattened current
steepens the profile further in and destabilizes 3/2 and 4/3 modes, until
the field is globally stochastic ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§6.2.1; see [thermal quench](/definitions/thermal-quench.md)). In these
MGI runs $n>1$ modes are destabilized by a current-profile effect, whereas
in the island-locking cases of the same review they are destabilized by
mode beating, a difference the review leaves "to be clarified" (§6.2.1).
JOREK argon MGI into JET pulse 85943 at realistically low resistivity gives
an $I_p$ spike of experimental magnitude, but the stochasticity decays
before the current profile has flattened, so the relaxation is incomplete
(§6.2.2; see [disruption](/definitions/disruption.md)).

**1/1 mode and the radiation flash (SPARC).** In NIMROD MGI into a SPARC
target with $q_{\min}=1.05$, where no $q=1$ surface exists, a pre-TQ of
about 2 ms radiates 5–15 GW; a large 1/1 mode then grows, its flows pull
blobs of neon from the edge into a single helical flux tube at mid-radius,
and the TQ flash peaks there at 40–55 GW (low resolution) or about 70 GW
(high resolution), "at the very start of the inward radial mixing of Ne and
not when the Ne is well mixed or has reached the axis"
([Izzo et al. (2025)](/sources/izzo-2025.md), §II C–D, Figs. 4–7; see
[resistive internal kink](/definitions/resistive-internal-kink.md)). The
radiated energy fraction, cumulative radiated plus ionization energy over
cumulative thermal plus magnetic energy lost, exceeds 95% in all four valve
layouts and reaches 98–99% at high resolution (§II C–D, Figs. 4d, 5b).

**Valve layout and MHD parity.** Of four layouts (6 and 4 valves, each
"resonant" or "non-resonant"), the up-down symmetric 4-valve resonant one
suppresses the large $n=1$ mode at the end of the TQ: its $n=1$ magnetic
energy stays more than an order of magnitude smaller, even symmetry is
preserved until the current quench, and there is no $I_p$ spike (Izzo et
al. 2025, §II C, Fig. 4c–e). This parallels the dual-SPI finding that
synchronized opposite injection makes even-$n$ modes dominate and removes
the 1/1 motion ([Hu et al. (2021)](/sources/hu-2021.md), §5); two codes and
two injection schemes give the same parity rule.

## Radiation asymmetry

- **Peak location.** In SPI the toroidal radiation peak lies near the
  injector; in an earlier NIMROD MGI simulation (Izzo 2013, as cited) it lay
  at $\pi$ from it, which [Hu et al. (2021)](/sources/hu-2021.md) (§6)
  attribute to toroidally uniform impurities in MGI, where the peak sits
  where the 1/1 X-point heat flux emerges. The SPARC runs place the TQ peak
  in a mid-radius flux tube, neither at a valve nor on axis
  ([Izzo et al. (2025)](/sources/izzo-2025.md), §II D, Fig. 7).
- **Multi-valve peaking.** The radiation toroidal peaking factor
  $\mathrm{TPF}_{\mathrm{rad}}$ of the SPARC layouts stays at or below 1.33
  in the TQ at low resolution and below 1.5 at high resolution; the 6-valve
  non-resonant layout is lowest in every phase and was selected for the
  SPARC disruption mitigation system, together with M3D-C1 runs, port
  allocation and engineering constraints (Izzo et al. 2025, §II C, §IV,
  Table II). Values and the first-wall energy impact are on
  [radiation asymmetry](/definitions/radiation-asymmetry.md).
- **Code-to-code.** NIMROD and M3D-C1 SPARC MGI runs, with different
  approximations, show "very similar levels of peak radiated power in the
  TQ and comparably high radiated energy fractions" for 6-valve cases; no
  M3D-C1 numbers are printed (Izzo et al. 2025, §II C, §IV).

## Combination with a runaway-electron mitigation coil

MGI and the passive [runaway-electron mitigation coil](/definitions/runaway-electron-mitigation-coil.md)
were simulated together for the first time by
[Izzo et al. (2025)](/sources/izzo-2025.md) (§III): a coil that carries
current from $t=0$ seeds the $n=1$ mode, which grows and saturates earlier,
so the TQ comes earlier and the radiated fraction at the end of the TQ rises
from 95% to 99% (§III B, Figs. 10–11).

## Model sensitivities

- **Viscosity and parallel conduction.** Izzo et al. (2025, §IV) rank the
  high viscosity ($\nu=500$ m²/s) and the constant parallel conduction
  ($\kappa_\parallel=10^8$ m²/s), both needed for convergence and stability,
  as their most significant approximations: lower viscosity would likely
  give faster impurity mixing and less peaked radiation, and a constant
  $\kappa_\parallel$ overestimates transport in cold regions against a
  $T^{5/2}$ closure, which tends to underpredict
  $\mathrm{TPF}_{\mathrm{rad}}$ and overestimate the conducted wall energy
  (stated, not tested).
- **Source width and deuterium content.** The low-resolution source is four
  times broader toroidally than the high-resolution one and underpredicts
  $\mathrm{TPF}_{\mathrm{rad}}$, especially pre-TQ, so those runs serve only
  for relative comparison of layouts (Izzo et al. 2025, §II C). The low/high
  resolution comparison changes the source width and its deuterium content
  together with $N_{\mathrm{tor}}$, so it is not a convergence test
  (compiler's remark).
- **Impurity model.** Coronal equilibrium underestimates the line radiation
  of weakly ionized states early in the injection; in the DIII-D benchmark
  JOREK's coronal model collapses about 2× slower than M3D-C1 and NIMROD,
  and its collisional-radiative model agrees with NIMROD
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §1, §6;
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7).

## Citations

- [Izzo et al. (2025)](/sources/izzo-2025.md), §I–IV, Figs. 1, 4–7, 10–11, Table II.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7, §6.2.1–6.2.3.
- [Hu et al. (2021b)](/sources/hu-2021-b.md), §1, §3, §6, Eq. 18.
- [Hu et al. (2021)](/sources/hu-2021.md), §5, §6.
