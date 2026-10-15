---
type: Source
title: "Moradi et al. (2018) — The influence of coolant jet direction on heat reduction on the nose cone with Aerodome at supersonic flow"
description: "RANS-SST study at Mach 5 of front (opposing), back (oblique) and top (lateral) coolant jets from an aerodome on a spiked nose cone, with air, CO2 and helium at two jet pressure ratios, finding the top jet reduces the nose-cone heat load most (about 90%) and the opposing jet least."
resource: "doi:10.1016/j.actaastro.2018.06.026"
source_kind: paper
authors: [Moradi R., Mosavat M., Barzegar Gerdroodbary M., Abdollahi A., Amini Y.]
year: 2018
venue: "Acta Astronaut. 151:487–493"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Moradi_The_influence_of_coolant_jet_direction_on_heat_reduction_on.pdf"
tags: [context, hypersonic, aeroheating, spike, coolant-jet, rans]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A steady RANS (SST k–ω with compressibility correction) study of
coolant injection from an aerodome, a cap at the tip of a spike mounted
ahead of a blunt nose cone, at freestream Mach 5. Following the geometry
of Qin et al. [23], three injector positions are compared: front
(opposing jet), back (oblique jet at the spike–aerodome junction) and
top (lateral jet), at jet-to-freestream total-pressure ratios 0.3 and
0.6, with air, CO₂ and helium. The top (lateral) jet gives the largest
nose-cone heat-load reduction (about 90%, Fig. 9 and Conclusion),
attributed to a steeper bow shock pushed off the nose shoulder and an
enlarged recirculation zone; the front (opposing) jet barely changes the
flow and gives the smallest reduction. The coolant matters little except
at the back position, where helium is clearly better. No validation is
shown; the paper refers to the authors' earlier work [11–15].

# Key claims

All quantitative claims come from the paper's own simulations; Fig. 9
values are approximate readings of an unlabelled bar chart (PR = 0.3,
air / CO₂ / He).

1. **Top (lateral) jet best** (Conclusion, Fig. 9): heat-load reduction
   "up to 90%", about 91 / 92 / 87%. Shown.
2. **Front (opposing) jet ineffective** (§3.1, Figs. 5, 9): it "does not
   change the flow feature" of the recirculation or bow shock; about
   24 / 25 / 34%. Shown.
3. **Back (oblique) jet intermediate** (§§3.1, 3.3, Fig. 9): removes the
   small recirculation behind the aerodome, pushes the bow shock off the
   nose, coolant fills the recirculation; about 58 / 60 / 74%. Shown.
4. **Mechanism** (§§3.1, 3.3, Conclusion; interpretation of Mach and
   streamline contours, Figs. 5–7): the top jet increases the bow-shock
   angle, pushes the reflected shock away from the nose shoulder and
   "noticeably enlarges the circulations"; "circulation strength" is named
   the controlling parameter but never quantified. Stated.
5. **Pressure ratio** (§3.1, Fig. 6): raising it from 0.3 to 0.6
   "significantly augments the effects". Qualitative; heat-load numbers
   exist only for 0.3.
6. **Coolant gas** (§§3.2–3.3, Figs. 7–8): helium spreads more (attributed
   to its higher diffusion coefficient); the CO₂ mass fraction on the nose
   exceeds helium's for the opposing and oblique jets and is similar for
   the lateral jet; gas type makes no significant difference "except for
   the back jet". The abstract's "15%" helium advantage for the lateral
   jet conflicts with Fig. 9 (see Recorded as printed).
7. **Heat capacity** (§3.2): named "the main effective term" for heat
   reduction. Stated, not tested.
8. **Heat flux** (Eq. 12): $q=h_f(T_w-T_f)$, with $h_f$ the fluid-side
   heat-transfer coefficient and $T_f$ the local fluid temperature; how the
   Fig. 9 "heat load reduction" is computed (integration, baseline) is not
   defined.

# Methods

* **Geometry** (§2.1, Figs. 1–3): after Qin et al.; nose-cone diameter
  10 cm, spike length 10 cm, aerodome at the spike tip; treated as
  axisymmetric (half simulated); domain 27 cm × 10 cm.
* **Freestream** (§2.2): Mach 5, 12076 Pa, 216 K, zero incidence;
  Reynolds number not stated.
* **Boundaries**: pressure far field; no-slip isothermal walls at 300 K;
  symmetry planes; pressure outlet; sonic injector with prescribed total
  pressure and temperature (jet total temperature not stated).
* **Solver** (§2.3): unnamed implicit in-house cell-centred finite-volume
  coupled code, second-order upwind, Roe flux-difference splitting;
  steady.
* **Turbulence** (Eqs. 1–11): Menter SST k–ω with dilatation-dissipation
  correction, $\zeta^*=1.5$, $M_{t0}=0.25$, $F(M_t)=M_t^2-M_{t0}^2$ above
  $M_{t0}$, production limiter $\min(G_k,10\rho\beta^*k\omega)$; standard
  formulation restated.
* **Species**: air, CO₂, He; the multispecies transport model is not
  stated.
* **Grids** (§2.1, Fig. 4): structured, 10800 (180 × 60), 14600
  (220 × 68), 18400 (250 × 75); first cell below 0.1 mm; fine and very
  fine agree on the nose pressure (peak about 0.016 of total pressure near
  arc length 0.5 nose radii); fine adopted.
* **Convergence**: residuals and a monitored mass fraction; density change
  at most $10^{-4}$.
* **Validation**: none shown against Qin's experiment.

# Tests and results

| Case | Section/Fig. | Finding |
|---|---|---|
| Grid study | §3, Fig. 4 | fine ≈ very fine; fine adopted |
| Air, three positions, PR 0.3 | §3.1, Fig. 5 | opposing: no change; oblique: recirculation removed; top: bow-shock angle increases most |
| Air, PR 0.6 | §3.1, Fig. 6 | all effects stronger, top most influential |
| CO₂ vs He | §3.2, Figs. 7–8 | helium spreads more; mass fractions as in claim 6 |
| Heat-load reduction | §3.3, Fig. 9 | back 58/60/74%, front 24/25/34%, top 91/92/87% (air/CO₂/He, approximate) |

# Notation map

| Moradi et al. (2018) | Registry | Note |
|---|---|---|
| $M$, $M_\infty$, $M_t$, $M_{t0}$ | words (Mach and turbulent Mach numbers) | |
| PR | words (jet-to-freestream total-pressure ratio) | |
| $\rho$, $T$, $R$ | words | **collision risk:** registry $\rho_c$ is charge density |
| $\gamma$ | $\gamma$ | ratio of specific heats |
| $\alpha=\sqrt{\gamma RT}$ | words (speed of sound) | |
| $k$, $\omega$ (SST) | words | **collision:** registry $k$, $\omega$ are wavenumber and angular frequency |
| $\beta$, $\beta^*$, $\beta_i$, $\zeta^*$ | words (model constants) | |
| $q$, $h_f$, $T_f$ | words (wall heat flux, heat-transfer coefficient, fluid temperature) | not the heat-flux vector $\mathbf q_s$ |
| $T_w$ | $T_w$ | wall temperature |
| $C_p$ (§3.2) | words (heat capacity) | |
| $P_s/P_T$, $S/R$ | words | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Moradi_The_influence_of_coolant_jet_direction_on_heat_reduction_on.pdf`.
   * **Version.** Publisher's final typeset PDF, 7 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.026, printed on page 1
     and checked on Crossref: title, five authors, Acta Astronaut.
     151:487–493 match; issue October 2018 (no online date on Crossref);
     page 1 gives received 27 May 2018, accepted 10 Jun 2018, online 15 Jun
     2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer plus renders of pp. 488–491;
     Eqs. 1–12 read cleanly. Fig. 9 has no y-axis label; its values are
     read to about ±1 point. Panels of Figs. 5–8 are not labelled by
     injector position. Not stated: jet total temperature, Reynolds number,
     $y^+$, CFL, species model, the pressure ratio of Fig. 8.
   * **Recorded as printed.**
     * The abstract credits helium as the lateral jet with 15% better
       cooling than the other gases; Fig. 9 has helium below air and CO₂ at
       the top (lateral) position, and about 15 points better only at the
       back (oblique) position, as §3.3 says.
     * §3.3: the top jet "could significantly enhance the heat load", while
       the next sentence and Fig. 9 show a reduction.
     * §3: "the applied approach is inconsistent with experimental data and
       obtained results agree well", evidently "consistent".
     * Grid counts: 220 × 68 = 14960, not 14600; 250 × 75 = 18750, not
       18400.
     * The convergence monitor sits "5 mm at the downstream of the cavity";
       the geometry has no cavity.
     * "Our previous studies [20–26]" points to other groups' papers; the
       authors' own are [11–15] and [28–40].
     * The Roe scheme is cited to [41], an aerodisk paper identical to [21].
     * "Axisymmetric … half simulated" (§2.1) against "both lateral sides
       and top plane" as symmetry planes (§2.2) and "two-dimensional" in the
       abstract: axisymmetric vs planar 2-D is not unambiguous.
     * Title "supersonic", text "hypersonic", at Mach 5.
     * Ref. [23] printed J. Spacecr. Rockets 55 (2017); volume 55 is
       2018 per the reader, not verified on Crossref.
   * **Reference list.** 50 printed entries, matching the Crossref
     reference count. Ref. [41] is a verbatim duplicate of ref. [21]
     (Huang et al., Acta Astronaut. 138 (2017) 168–175). The corresponding
     author appears both as "M. Barzegar Gerdroodbary" and as "M.B.
     Gerdroodbary". Ref. [40] has a garbled author string; ref. [42]
     (Menter et al. 2003) is printed as a journal but is the *Turbulence,
     Heat and Mass Transfer 4* proceedings.
