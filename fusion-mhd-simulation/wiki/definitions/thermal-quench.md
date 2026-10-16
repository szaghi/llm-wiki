---
type: Definition
title: "Thermal quench"
description: "The thermal quench is the disruption phase in which the plasma loses most of its thermal energy, by parallel transport along stochastic field lines opened by MHD modes, by impurity radiation, or both; its duration (0.1 ms in NSTX to about 20 ms predicted for unmitigated ITER) is sensitive to parallel heat conduction, impurity atomic model, boundary conditions and numerical stabilization."
status: established
aliases: [TQ, radiative collapse, thermal collapse]
tags: [disruption, impurities, mhd, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# Thermal quench

The **thermal quench (TQ)** is the phase of a
[disruption](/definitions/disruption.md) in which the thermal energy
$W_{\mathrm{th}}$ collapses on a time short compared with the subsequent
current quench. In the nonlinear-MHD literature of this bundle two loss
channels produce it, often together:

- **Stochastic parallel transport.** MHD modes overlap, the field becomes
  stochastic, field lines connect the core to the wall, and heat is lost
  along them at the rate set by $\kappa_\parallel$.
- **Radiative collapse.** Injected impurities radiate ($P_{\mathrm{rad}}$)
  and absorb ionization energy, cooling the plasma from the outside in.

A TQ is therefore classified by its trigger: an MHD-triggered TQ in an
unmitigated disruption or a [hot VDE](/definitions/vertical-displacement-event.md),
and an injection-triggered TQ in a mitigated disruption
([shattered pellet and massive material injection](/definitions/shattered-pellet-injection.md)).

## MHD-triggered TQ

In the 3D NSTX hot-VDE benchmark the plasma drifts into the wall, the edge
safety factor falls, and when $q_{95}\approx2$ low-$n$ external kinks
(2/1, 4/2, 6/3) grow from the edge, create an ergodic layer, open core
regions to the wall and produce filamentary pressure structures; the TQ
follows in all three codes ([Artola et al. (2021)](/sources/artola-2021.md),
§4.1.2–4.1.3, Figs. 6–7). Its duration is 0.14 ms (JOREK), 0.24 ms (M3D-C1)
and 0.20 ms (NIMROD), consistent with the ≈0.2 ms loss of core confinement
in NSTX disruptions (same source, §4.1.3; also
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8). Once the 3D
instability sets in, the decay rate of $W_{\mathrm{th}}$ is dominated by the
3D dynamics, not by the (raised) perpendicular diffusivities
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.1).

The TQ time depends sublinearly on parallel conduction: multiplying
$\kappa_\parallel$ by 10 shortens the JOREK TQ from 0.14 to 0.043 ms, a
factor ≈3, while the peak wall forces stay similar
([Artola et al. (2021)](/sources/artola-2021.md), §4.3.2, Fig. 13).

For ITER, unmitigated VDE simulations predict a significantly longer TQ, "in
the range of 20 ms" ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1).
In dedicated ASDEX Upgrade VDE experiments, JOREK reproduces the onset point
of the TQ during the vertical motion; the timing is strongly affected by the
SOL heat transport, controlled by the temperature below which the
$T$-dependence of $\kappa_\parallel$ is cropped (same source, §3.1, Fig. 5).
Ports in a 3D volumetric wall advance the TQ of a 3D hot VDE (≈12 ms
against ≈12.5 ms, read from the figure) and move it to a larger $q_{95}$
([Isernia et al. (2023)](/sources/isernia-2023.md), §VI, Fig. 10).

## Injection-triggered TQ

**Tearing cascade.** In JOREK deuterium massive-gas-injection simulations
of JET, the cold front reaches $q=2$, destabilizes a large 2/1 tearing mode
(boosted by helical cooling inside the island), which flattens $j_\phi$
there and steepens it further in; the steep gradient destabilizes 3/2 and
then 4/3 modes, and the combined modes make the field globally stochastic
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.1, Figs. 54–55). See
[tearing mode](/definitions/tearing-mode.md).

**SPI regimes.** For shattered pellets the pre-TQ dynamics depend on the
ordering of the shard transit time and the resistive current-decay time in
the cooled region ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.1).
Fast shards cause helical cooling at low-order rational surfaces and, for
$q_0<1$, excite the 1/1 internal kink when they reach $q=1$ (JET deuterium
SPI). Slow shards let the current profile contract, tearing modes cascade
from edge to core, and the TQ is usually triggered when shards reach $q=2$
(ASDEX Upgrade deuterium SPI, and any impurity SPI). Predictive ITER
neon–deuterium SPI shows the opposite ordering of edge and core: shards can
reach the core before the edge radiative collapse, and a transport barrier
of the stochastic field outside $q=1$ can persist in the early TQ until the
edge collapses ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2,
Fig. 8). In full-MHD neon SPI into a JET-like plasma the core temperature
drops from ≈3.5 keV to below 1 keV between 2 and 3 ms after injection,
with ergodization by 3/1 and 2/1 and later 1/1 structures as fragments
cross $q=2$ ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.3.1,
Figs. 13–14).

**Radiative collapse.** In axisymmetric JOREK argon and neon gas injection
into DIII-D, the collapse proceeds from the inside out with a hollow $T_e$
and a thin current and temperature halo, followed by re-concentration of
the current near a new axis ([Hu et al. (2021b)](/sources/hu-2021-b.md),
§6.2, Figs. 15–16). Idealized benchmarks impose the TQ instead of computing
it: [Bandaru et al. (2024)](/sources/bandaru-2024.md) (§III.A) cool the
plasma by a prescribed exponential with 1 ms time constant to ≈100 eV in
the core before letting radiation, Ohmic heating and ionization take over;
$T_e$ then settles at 6–9 eV and drops to ≈1 eV once runaway electrons carry
the current (§III.B).

## Sensitivities

- **Impurity atomic model.** Coronal equilibrium underestimates the line
  radiation of weakly ionized states early in an injection. Compared with
  the collisional-radiative model, it delays the balance of cooling and
  Ohmic power ([Hu et al. (2021b)](/sources/hu-2021-b.md), §1, §4, Fig. 2).
  In the axisymmetric DIII-D benchmark of
  [the DIII-D gas-injection impurity benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md),
  JOREK's coronal-equilibrium model gives a collapse ≈2× slower than the
  charge-state-resolved M3D-C1 and NIMROD ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7);
  with the collisional-radiative model JOREK agrees with NIMROD in shape and
  peak of the cooling power, with the argon peak 0.15 ms later
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §6.1, Fig. 11). The two
  observations point the same way. See
  [coronal-equilibrium](/methods/coronal-equilibrium-impurity-model.md) and
  [collisional-radiative](/methods/collisional-radiative-impurity-model.md)
  impurity models.
- **Temperature model.** A two-temperature model cools electrons faster
  than a single-temperature model, more markedly for neon
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §5, Figs. 7–8).
- **Numerical stabilization.** Shock capturing lets full-MHD SPI runs pass
  through the TQ with unchanged $W_{\mathrm{th}}$ and $I_p$ traces at moderate
  coefficients, but too strong a setting smears the dynamics, and the
  stronger sensor at low resistivity suppresses the TQ altogether
  ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.3, Figs. 11, 19); see
  [shock-capturing artificial viscosity](/methods/shock-capturing-artificial-viscosity.md).

## Citations

- [Artola et al. (2021)](/sources/artola-2021.md), §4.1.1–4.1.3, §4.3.2.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7, §4.8, §6.2.1.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1, §3.2.
- [Bhole et al. (2023)](/sources/bhole-2023.md), §4.3.
- [Hu et al. (2021b)](/sources/hu-2021-b.md), §1, §4–6.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §III.
- [Isernia et al. (2023)](/sources/isernia-2023.md), §VI.
