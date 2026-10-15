---
type: Method
title: "Aeroheating reduction by spikes and coolant jets"
description: "Reduction of the heat load on a blunt nose by a forward spike carrying an aerodisk or aerodome, combined with coolant injection from the cap; at Mach 5 a lateral jet from the top of the aerodome is computed to cut the nose-cone heat load by about 90%, an opposing jet the least."
status: established
aliases: [spiked blunt body, aerospike, aerodisk, aerodome, coolant jet, combined spike and jet]
tags: [aeroheating, thermal-protection, spike, aerodome, coolant-jet, rans]
timestamp: 2026-10-14T00:00:00Z
---

# Aeroheating reduction by spikes and coolant jets

A forward spike ahead of a blunt nose carries a cap at its tip (an aerodisk
or, in the source below, an aerodome); coolant can be injected from the cap.
In the configuration below, the flow over the spiked body shows a bow shock,
recirculation regions around the aerodome and over the nose, and a
reflected shock near the nose shoulder, and the injection acts on these
features ([Moradi et al. (2018)](/sources/moradi-2018.md), §3.1, §3.3). [Moradi et al. (2018)](/sources/moradi-2018.md) compare three
injector positions on an aerodome at $\mathrm{Ma}_\infty=5$, after the
configuration of Qin et al.: front (an opposing jet), back (an oblique jet
at the spike–aerodome junction) and top (a lateral jet).

## Computed effect of injector position

All from [Moradi et al. (2018)](/sources/moradi-2018.md), steady RANS with
[SST k–ω](/methods/sst-k-omega-model.md), sonic jets at a jet-to-freestream
total-pressure ratio of 0.3; nose-cone heat-load reduction read from the
bar chart of Fig. 9 (approximate, unlabelled axis, no stated baseline or
integration area):

| Injector position | Air | CO$_2$ | He | Flow change (§3.1, Fig. 5) |
|---|---|---|---|---|
| Front (opposing) | about 24% | about 25% | about 34% | "does not change the flow feature" of recirculation or bow shock |
| Back (oblique) | about 58% | about 60% | about 74% | removes the small recirculation behind the aerodome; pushes the bow shock off the nose; coolant fills the recirculation (§3.3) |
| Top (lateral) | about 91% | about 92% | about 87% | bow-shock angle "significantly increases"; reflected shock pushed off the nose shoulder |

* **Ranking.** Top > back > front for every gas; the paper's conclusion
  quotes a reduction "up to 90%" for the top jet.
* **Mechanism (interpretive).** The authors attribute the top jet's
  advantage to the steeper bow shock, the reflected shock moved away from
  the nose shoulder and "noticeably" enlarged circulations, naming
  circulation strength as the controlling parameter without quantifying it
  (§3.1, §3.3, Conclusion). Interpreted from Mach and streamline contours.
* **Pressure ratio.** Raising the ratio from 0.3 to 0.6 "significantly
  augments the effects" (§3.1, Fig. 6); no heat-load numbers at 0.6.
* **Coolant gas.** Gas type matters little except at the back position, where
  helium is about 15 points better (§3.3, Fig. 9). Helium spreads more than
  CO$_2$, attributed to its higher diffusion coefficient; CO$_2$ covers more
  of the nose for the front and back jets, similarly for the top jet (§3.2,
  Figs. 7–8). The coolant's specific heat is named "the main effective term"
  without a test (§3.2). The abstract's statement that helium is 15% better
  as the *lateral* jet disagrees with the paper's own Fig. 9 and §3.3.

## Limits of the evidence

The configuration (nose diameter 10 cm, spike length equal to the diameter,
$p_\infty$ = 12076 Pa, $T_\infty$ = 216 K, isothermal walls at 300 K) is
taken from Qin's experiment, but the paper shows no comparison with it; it
asserts agreement with experiment only for the authors' earlier studies.
The heat flux is defined as heat-transfer coefficient times the difference
between wall and local fluid temperature (Eq. 12), but no heat-flux
distribution is shown, and the jet total temperature and the species
transport model are not stated ([Moradi et al. (2018)](/sources/moradi-2018.md),
§2–3). The ranking is therefore a single unvalidated RANS study.

# Citations

1. [Moradi et al. (2018)](/sources/moradi-2018.md) — §2.1–2.3 (Eqs. 1–12, Figs. 1–4), §3.1–3.3 (Figs. 5–9), Conclusion.
