---
type: Definition
title: "Toroidal radiation asymmetry and first-wall energy impact"
description: "The toroidal asymmetry of the power radiated during a mitigated thermal quench, measured by the radiation toroidal peaking factor and converted into a first-wall energy impact; in JOREK simulations single-injector SPI gives peaking factors above 2 with a helical structure set by the triggering rational surface and dual injection removes most of it even with a 1 ms delay, while NIMROD multi-valve gas injection in SPARC stays below 1.5 in the thermal quench."
status: established
aliases: [radiation peaking, toroidal peaking factor of radiation, TPF of radiated power, radiation asymmetry, energy impact, heat-flux factor]
tags: [disruption, impurities, wall, mhd, tokamak]
timestamp: 2026-10-16T16:51:00Z
---

# Toroidal radiation asymmetry and first-wall energy impact

A mitigated [disruption](/definitions/disruption.md) is meant to radiate
the thermal energy uniformly onto the first wall. Injection from a few
toroidal locations ([shattered pellet injection](/definitions/shattered-pellet-injection.md),
massive gas injection) makes the radiated power density $P_{\mathrm{rad}}$
toroidally and poloidally non-uniform, and what matters for the wall is the
local, time-integrated heat load that the asymmetry produces.

## Measures

Registry symbols ([notation](/notation.md), §10): $\mathrm{TPF}_{\mathrm{rad}}$
the radiation toroidal peaking factor, $q_w$ the heat flux onto a wall
surface, $\Delta Q$ the energy impact.

- **Radiation toroidal peaking factor.** With
  $P_{\mathrm{rad}}^{\mathrm{tor}}(\phi)$ the radiated power integrated over
  the poloidal plane at toroidal angle $\phi$ (per radian),
  $$\mathrm{TPF}_{\mathrm{rad}}=\frac{\max_\phi P_{\mathrm{rad}}^{\mathrm{tor}}(\phi)}{\frac{1}{2\pi}\oint P_{\mathrm{rad}}^{\mathrm{tor}}\,d\phi},$$
  the same max-over-mean definition that the JOREK review uses
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.4;
  [Hu et al. (2021)](/sources/hu-2021.md), §4.3, which plots the ratio as a
  function of $\phi$). ITER's target for it is 2 (as recorded from Hoelzl
  et al. 2021 on the SPI page). It is distinct from the halo-current
  $\mathrm{TPF}$ of [halo current](/definitions/halo-current.md).
- **Discrete-sector estimate.** An experiment sees $P_{\mathrm{rad}}^{\mathrm{tor}}$
  only at a few bolometer sectors $\phi_i$; the synthetic diagnostic of
  [Tang et al. (2025)](/sources/tang-2025.md) (Fig. 23 caption) replaces the
  toroidal mean by the trapezoidal average over the five AUG foil-bolometer
  sectors,
  $$\mathrm{TPF}_{\mathrm{rad}}\approx\frac{\max_iP_{\mathrm{rad}}^{\mathrm{tor}}(\phi_i)}{\sum_i\frac12\big[P_{\mathrm{rad}}^{\mathrm{tor}}(\phi_i)+P_{\mathrm{rad}}^{\mathrm{tor}}(\phi_{i+1})\big]\frac{\phi_{i+1}-\phi_i}{2\pi}},$$
  which approaches the continuous definition only when the sectors resolve
  the toroidal structure.
- **Phase-integrated and partial-volume factors.**
  [Izzo et al. (2025)](/sources/izzo-2025.md) (§II C–D) tabulate the factor
  of the radiated *energy* integrated over each phase (pre-TQ, TQ, CQ), and
  an "upper TPF" from the radiation of the upper half volume only, which
  separates the local radiation near a row of valves from global peaking.
- **Energy impact.** For a semi-infinite wall under a constant surface flux
  $q_w$ applied for $\Delta t$, the surface temperature rise is
  $\frac{2}{\sqrt\pi\,b}\,q_w\sqrt{\Delta t}$, with $b$ the thermal
  effusivity of the material (square root of conductivity times density
  times specific heat); the energy impact $\Delta Q=q_w\sqrt{\Delta t}$ is
  therefore the quantity compared with melt limits. For a time-varying
  flux the half-space heat kernel gives
  $$\Delta Q(t)=\frac12\int_{t_0}^{t}\frac{q_w(t')}{\sqrt{t-t'}}\,dt',$$
  which reduces to $q_w\sqrt{t-t_0}$ for constant flux
  ([Hu et al. (2024)](/sources/hu-2024.md), §2.2, Eqs. 2–4; the compiler
  checked the constant-flux limit). Limits quoted: stainless steel 13,
  beryllium 28, tungsten 38 MJ s$^{-1/2}$ m$^{-2}$ (§1, §4–5, citing Pitts
  et al. 2015 and Herrmann 2002). [Izzo et al. (2025)](/sources/izzo-2025.md)
  (§II D) use the continuous form "from [Hu 2024]" and give 50 MJ
  s$^{-1/2}$ m$^{-2}$ for melting of pure tungsten (see Contradictions).

## Single-injector SPI: peaking and helical structure

[Hu et al. (2021)](/sources/hu-2021.md) (JOREK reduced MHD,
[coronal-equilibrium impurities](/methods/coronal-equilibrium-impurity-model.md))
give the primary simulation evidence:

- **ITER L-mode, neon–hydrogen mono-SPI.** $\mathrm{TPF}_{\mathrm{rad}}$ is
  "larger than 2 during the TQ when the radiation power is strongest", with
  values read from Fig. 18a of ≈5.7 at 2.32 ms (low absolute power), ≈4.5 at
  3.80 ms and ≈2.4 in the early TQ (4.24 ms), relaxing to ≈1.2 at 4.67 ms;
  the peak lies near the injection angle (§4.3, §5.1, Figs. 16, 18).
- **Helical structure.** The asymmetry is poloidal as well as toroidal and
  has the helicity of the surface that triggers the thermal quench: 1/1 in
  the ITER case, 2/1 in a JET-like argon case, where the injection plane
  radiates an order of magnitude more than the plane at $\pi$ (§3, Fig. 9;
  §4.3, Fig. 16). The radiation peak does not necessarily coincide with the
  fragments or the impurity-density peak: an unrelaxed impurity density
  from strong ablation as the outward heat flux rises, and an asymmetric
  outgoing heat flux, set it (§4.3).
- **Relaxation.** The asymmetry relaxes by the end of the TQ; the current
  quench radiates more energy but "much more relaxed", so the TQ is the
  critical phase (§1, §5.2).
- **SPI against MGI.** The peak lies near the injector in these runs and in
  NIMROD SPI, but at $\pi$ from it in Izzo's MGI simulation; the authors
  attribute the difference to toroidally localized (SPI) against uniform
  (MGI) impurity density, with the MGI peak set by where the 1/1 X-point
  heat flux emerges (§6). This is a physical difference between injection
  schemes, not a disagreement between codes; no MGI run is made. The
  NIMROD SPARC MGI runs below agree that the TQ peak is not at the
  injector: it lies in a single helical flux tube at mid-radius
  ([Izzo et al. (2025)](/sources/izzo-2025.md), §II D, Fig. 7).

## Dual injection

- **Synchronized.** Two injectors at toroidally opposite ports, same total
  quantity: peaking at $\phi=0,\pi$ before the TQ (≈2.4 at 2.52 ms, read),
  falling steadily to ≈1 at 4.16 ms, near TQ onset; the peak per-radian
  power does not rise although total radiation does
  ([Hu et al. (2021)](/sources/hu-2021.md), §5.1, Fig. 18b,d).
- **Delayed by 1 ms.** Similar pre-TQ peaking, stronger at the first
  injector, "mostly flattened" shortly after the TQ; "good mitigation of
  toroidal peaking can be maintained with $\mathcal O(1\,\mathrm{ms})$ time
  delay" (§5.2, Fig. 21). For a delay comparable with the whole mitigation
  time the result tends to mono-SPI (stated trend).
- **MHD parity follows the injection symmetry.** Synchronized dual SPI
  makes even-$n$ modes dominate, replaces the 2/1 island by a 4/2 and
  removes the 1/1 kink motion; a delay restores $n=1$ dominance (§5,
  Figs. 17, 19, 20). The review states the same conclusion, single SPI above
  2 and dual SPI mitigating ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
  §6.2.4).

## ASDEX Upgrade SPI: early peaking against experiment

[Tang et al. (2025)](/sources/tang-2025.md) (§3.5, Figs. 23–24) compare
JOREK neon–deuterium SPI with AUG bolometry. The simulated radiation shows
two peaks in the $P_{\mathrm{rad}}$–$\mathrm{TPF}_{\mathrm{rad}}$ plane.
The first, with $\mathrm{TPF}_{\mathrm{rad}}$ up to about 2.4–2.6, comes
from the outward heat flux and the sharp ablation at fragment arrival; it is
stronger for smaller fragments and "is overestimated in simulations and not
observed in experiments". The factor at the TQ peak is small, as in
experiment. Across the five sectors the measured radiation is more
toroidally uniform than the simulated one (except one sector). The authors
name optical opacity and the missing equilibrium toroidal flow as causes
(stated). This is an *over*estimate of peaking with a toroidal source width
of 0.8 rad, between the 1 rad of Hu et al. (2021) and the 0.3–0.5 rad of
Hu et al. (2023, 2024), widths that those papers associate with artificial
mitigation of peaking (see Numerical caveats).

## Multi-valve gas injection in SPARC

[Izzo et al. (2025)](/sources/izzo-2025.md) compare four NIMROD
[massive gas injection](/definitions/massive-gas-injection.md) layouts with
the same 90/10 D$_2$/neon inventory. The low-resolution runs ($n\le10$,
toroidally broad source) give these factors of the phase-integrated
radiated energy (Table II):

| Layout | pre-TQ | TQ | CQ |
|---|---|---|---|
| 6 valves, non-resonant | 1.07 | 1.21 | 1.11 |
| 6 valves, resonant | 1.09 | 1.26 | 1.41 |
| 4 valves, non-resonant | 1.39 | 1.33 | 1.51 |
| 4 valves, resonant | 1.28 | 1.33 | 1.47 |

All four radiate more than 95% of the lost energy, and the 6-valve
non-resonant layout is lowest in every phase; it was chosen for SPARC
(§II C, §IV). The broad source underpredicts the factor, especially
pre-TQ, so the table is a relative comparison (§II C). At high resolution
($n\le21$, a source four times narrower toroidally, more deuterium in it):

- The total-neon peaking mostly reflects the source, since most neon stays
  neutral outside the separatrix: about 4.5 for the resonant (three
  toroidal locations) and 2.3 for the non-resonant (six locations) layout.
  The "upper TPF" is nearly identical for the two up to 0.25 ms, so fewer
  locations do not mean more local radiation near each valve. Ionized neon
  has a factor near 1 within 0.5 ms (§II D, Fig. 6).
- The radiation factor falls from about 3–4 early to 1–1.5; it upticks at
  the TQ but stays at or below 1.5. The resonant layout shows an $n=3$
  pattern with an $n=1$ overlay at the TQ from the large 1/1 mode, the
  non-resonant one a slight $n=6$ variation early and $n=1$ at the TQ
  (§II D, Fig. 6).
- Ray tracing with Cherab gives a peak first-wall flux $q_w$ above
  1 GW/m² for about 100 µs near an upper injector, and $\Delta Q\approx20$
  MJ s$^{-1/2}$ m$^{-2}$, "near-to but below the critical value" of the
  tungsten heavy alloy of the SPARC limiters (value not printed); melting of
  pure tungsten is "unlikely in any SPARC mitigated disruption" (§II D,
  Fig. 8).

## First-wall energy impact in ITER H-mode dual SPI

[Hu et al. (2024)](/sources/hu-2024.md) ray-trace the JOREK
$P_{\mathrm{rad}}$ onto the real ITER first-wall tiles and the stainless-steel
armour of the equatorial ports with Raysect/CHERAB in IMAS, and integrate
$\Delta Q$ (§2.2, §4):

| Case | max $\Delta Q$ (MJ s$^{-1/2}$ m$^{-2}$) | outcome |
|---|---|---|
| baseline H-mode, 1% Ne, synchronized | 25.4 | port armour melts (above 13), tungsten safe (below 38) |
| degraded H-mode, 5% Ne, synchronized | 5.7 | well below stainless-steel limit |
| degraded H-mode, 5% Ne, 1 ms delay | 14.9 | slightly above stainless-steel limit |

(Table 2; the text calls the 14.9 case "approaches" in the abstract and
§4–5 and "only exceeds … slightly" in §1, and the table supports the
latter.) Radiation concentrates around the injecting port early and becomes
nearly uniform late, with peak wall flux an order of magnitude lower at
5.74 ms despite high total power (§4, Fig. 12). The radiation hot spot
shifts away from the fragments, as in Hu et al. (2021) (§4, Fig. 12b).
Synchronization lowers the maximum impact (5.7 against 14.9). In the
baseline case the conductive and convective flux after
[plasmoid drift](/definitions/plasmoid-drift.md) dominates the load; the
source's estimate of its impact is printed as "$10^8$ MJ s$^{-1/2}$/m²",
which is inconsistent with its own Fig. 6 by $10^6$ (very likely J for MJ);
the conclusion that it exceeds the tungsten limit stands either way (§5).

## Numerical caveats

- **Toroidal source width.** The density sources are toroidally elongated
  for resolution reasons (1 rad in Hu et al. 2021; 0.3 rad in Hu et al.
  2024). Hu et al. (2021, §2.2, §6) state that this "may result in
  artificially mitigated toroidal peaking". Izzo et al. (2025, §II C)
  agree for gas injection: their four-times-broader source underpredicts
  $\mathrm{TPF}_{\mathrm{rad}}$. The AUG runs of Tang et al. (2025) at
  0.8 rad nevertheless overestimate early peaking relative to experiment
  (above), so a broad source is not a sufficient condition for an
  underestimate when the peaking comes from the ablation burst itself. Hu et al. (2023) find that
  narrowing the width from 0.5 to 0.3 rad raises radiation less than
  proportionally and conclude that radiation from elongated sources "should
  be considered as a lower estimation" ([Hu et al. (2023)](/sources/hu-2023.md),
  §4.2, §5). The quantitative dependence on the width is contested; see
  [shattered pellet injection](/definitions/shattered-pellet-injection.md).
- **Opacity.** All runs assume an optically thin plasma; near the fragments
  this is questionable (Hu et al. 2021, §2.2), and neglected opacity
  overestimates the peak radiation (Hu et al. 2024, §5); Tang et al. (2025,
  §3.5, §4) name it for their overestimated early peaking.
- **Transport closures.** A constant $\kappa_\parallel$ tends to
  underpredict $\mathrm{TPF}_{\mathrm{rad}}$, and the high viscosity needed
  for stability likely makes radiation more peaked than a lower one would
  ([Izzo et al. (2025)](/sources/izzo-2025.md), §IV, stated).
- **Resolution.** None of the studies reports a convergence test of
  $\mathrm{TPF}_{\mathrm{rad}}$ or $\Delta Q$; the low/high-resolution pair
  of Izzo et al. (2025) changes source width and deuterium content together
  with $N_{\mathrm{tor}}$.
- **Line spectrum.** Post-processing the SPARC TQ peak with OPEN-ADAS
  photon-emissivity coefficients gives 96 non-negligible neon lines summing
  to 70.1 GW against NIMROD's 65 GW, with over 75% of the power between 16
  and 35 eV (Izzo et al. 2025, Appendix, Table III).

## Contradictions

**Melt limit of tungsten in energy-impact units — Open.**
[Hu et al. (2024)](/sources/hu-2024.md) (§1, §4–5) compare their energy
impacts with 38 MJ s$^{-1/2}$ m$^{-2}$ for tungsten (citing Herrmann 2002).
[Izzo et al. (2025)](/sources/izzo-2025.md) (§II D), who take their
$\Delta Q$ formula from Hu et al. (2024), give 50 MJ s$^{-1/2}$ m$^{-2}$
for melting of pure tungsten, without a reference for the number. Neither
states the initial surface temperature or the damage criterion (melting
from room temperature, from an operating temperature, or another
threshold), which can account for a 30% difference. The basis of the 50
value would settle it; the SPARC conclusion holds against either number
($\Delta Q\approx20$).

## Citations

- [Hu et al. (2021)](/sources/hu-2021.md), §1–6, Figs. 9, 16–21.
- [Hu et al. (2024)](/sources/hu-2024.md), §1–5, Eqs. 2–4, Table 2, Figs. 6, 12–15.
- [Hu et al. (2023)](/sources/hu-2023.md), §4.2, §5.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.4.
- [Tang et al. (2025)](/sources/tang-2025.md), §3.5, §4, Figs. 23–24.
- [Izzo et al. (2025)](/sources/izzo-2025.md), §II C–D, §IV, Appendix, Figs. 6–8, Tables II–III.
