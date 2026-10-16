---
type: Definition
title: "Toroidal radiation asymmetry and first-wall energy impact"
description: "The toroidal asymmetry of the power radiated during a mitigated thermal quench, measured by the radiation toroidal peaking factor and converted into a first-wall energy impact; in JOREK simulations single-injector SPI gives peaking factors above 2 with a helical structure set by the triggering rational surface, and dual injection removes most of it even with a 1 ms delay."
status: established
aliases: [radiation peaking, toroidal peaking factor of radiation, TPF of radiated power, radiation asymmetry, energy impact, heat-flux factor]
tags: [disruption, impurities, wall, mhd, tokamak]
timestamp: 2026-10-16T12:00:00Z
---

# Toroidal radiation asymmetry and first-wall energy impact

A mitigated [disruption](/definitions/disruption.md) is meant to radiate
the thermal energy uniformly onto the first wall. Injection from a few
toroidal locations ([shattered pellet injection](/definitions/shattered-pellet-injection.md),
massive gas injection) makes the radiated power density $P_{\mathrm{rad}}$
toroidally and poloidally non-uniform, and what matters for the wall is the
local, time-integrated heat load that the asymmetry produces.

## Measures

Page-local symbols, pending registry entries: $\mathrm{TPF}_{\mathrm{rad}}$
the radiation toroidal peaking factor, $q_s$ the heat flux onto a wall
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
- **Energy impact.** For a semi-infinite wall under a constant surface flux
  $q_s$ applied for $\Delta t$, the surface temperature rise is
  $\frac{2}{\sqrt\pi\,b}\,q_s\sqrt{\Delta t}$, with $b$ the thermal
  effusivity of the material (square root of conductivity times density
  times specific heat); the energy impact $\Delta Q=q_s\sqrt{\Delta t}$ is
  therefore the quantity compared with melt limits. For a time-varying
  flux the half-space heat kernel gives
  $$\Delta Q(t)=\frac12\int_{t_0}^{t}\frac{q_s(t')}{\sqrt{t-t'}}\,dt',$$
  which reduces to $q_s\sqrt{t-t_0}$ for constant flux
  ([Hu et al. (2024)](/sources/hu-2024.md), §2.2, Eqs. 2–4; the compiler
  checked the constant-flux limit). Limits quoted: stainless steel 13,
  beryllium 28, tungsten 38 MJ s$^{-1/2}$ m$^{-2}$ (§1, §4–5, citing Pitts
  et al. 2015 and Herrmann 2002).

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
  schemes, not a disagreement between codes; no MGI run is made.

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
  artificially mitigated toroidal peaking". Hu et al. (2023) find that
  narrowing the width from 0.5 to 0.3 rad raises radiation less than
  proportionally and conclude that radiation from elongated sources "should
  be considered as a lower estimation" ([Hu et al. (2023)](/sources/hu-2023.md),
  §4.2, §5). The quantitative dependence on the width is contested; see
  [shattered pellet injection](/definitions/shattered-pellet-injection.md).
- **Opacity.** All runs assume an optically thin plasma; near the fragments
  this is questionable (Hu et al. 2021, §2.2), and neglected opacity
  overestimates the peak radiation (Hu et al. 2024, §5).
- **Resolution.** Neither study reports a convergence test of
  $\mathrm{TPF}_{\mathrm{rad}}$ or $\Delta Q$.

## Citations

- [Hu et al. (2021)](/sources/hu-2021.md), §1–6, Figs. 9, 16–21.
- [Hu et al. (2024)](/sources/hu-2024.md), §1–5, Eqs. 2–4, Table 2, Figs. 6, 12–15.
- [Hu et al. (2023)](/sources/hu-2023.md), §4.2, §5.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.4.
