---
type: Source
title: "Moradi et al. (2018) — The influence of coolant jet direction on heat reduction on the nose cone with Aerodome at supersonic flow"
description: "RANS (SST k–ω) study of sonic coolant injection from the front, back or top of an aerodome on a spiked nose cone at Mach 5, finding that top (lateral) injection reduces the nose-cone heat load by about 90%, front (opposing) injection the least, and that the coolant gas matters mainly at the back position."
resource: "doi:10.1016/j.actaastro.2018.06.026"
source_kind: paper
authors: [Moradi R., Mosavat M., Barzegar Gerdroodbary M., Abdollahi A., Amini Y.]
year: 2018
venue: "Acta Astronaut. 151:487–493"
local_file: "/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Moradi_The_influence_of_coolant_jet_direction_on_heat_reduction_on.pdf"
tags: [aeroheating, spike, aerodome, coolant-jet, rans, sst]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper is a steady RANS (SST k–ω) study of coolant injection from an
aerodome (a cap on a forward spike) mounted ahead of a blunt nose cone at
$\mathrm{Ma}_\infty=5$. Following Qin et al. (ref. [23]), three injector
positions are compared: front (opposing jet), back (oblique jet, at the
spike–aerodome junction) and top (lateral jet), at two jet-to-freestream
total-pressure ratios (0.3 and 0.6) and with three coolants (air, CO$_2$,
He). The top (lateral) jet gives the largest nose-cone heat-load reduction,
about 90% (Fig. 9 and Conclusion). The paper attributes this to a steeper
bow shock pushed off the nose shoulder and an enlarged recirculation zone.
The front jet barely changes the flow and gives the smallest reduction. The
coolant gas matters little except at the back position, where helium is
clearly better. The geometry comes from Qin's experiment, but the paper shows
no validation of its own; it refers to the authors' earlier papers
(refs. [11–15]).

# Key claims

1. **Top (lateral) injection is best** (Conclusion, Fig. 9). Heat-load
   reduction "up to 90%"; Fig. 9 at pressure ratio 0.3 reads about 91% (air),
   92% (CO$_2$) and 87% (He) (approximate bar readings). Shown, own
   simulation.
2. **Front (opposing) injection is ineffective** (§3.1, Fig. 5, Fig. 9). The
   front jet "does not change the flow feature" of the recirculation region
   or the bow shock; reduction about 24% (air), 25% (CO$_2$), 34% (He).
   Shown.
3. **Back (oblique) injection is intermediate** (§3.1, §3.3, Fig. 9). It
   removes the small recirculation behind the aerodome, pushes the bow shock
   off the nose, and its coolant fills the recirculation; reduction about 58%
   (air), 60% (CO$_2$), 74% (He). Shown.
4. **Mechanism** (§3.1, §3.3, Conclusion). The top jet raises the bow-shock
   angle, pushes the reflected shock away from the nose shoulder and
   "noticeably enlarges the circulations", which the paper calls the main
   reason for its better cooling. "Circulation strength" is named as the
   controlling parameter but never quantified. Stated, interpreted from Mach
   and streamline contours (Figs. 5–7).
5. **Pressure ratio** (§3.1, Fig. 6). Raising the jet-to-freestream
   total-pressure ratio from 0.3 to 0.6 "significantly augments the effects";
   the top jet has "the most effective influence on the main stream".
   Qualitative only; heat-load numbers are given only at 0.3.
6. **Coolant gas** (§3.2–3.3, Figs. 7–8). Helium spreads more than CO$_2$,
   attributed to its higher diffusion coefficient; on the nose cone the CO$_2$
   mass fraction exceeds the helium one for the opposing and oblique jets and
   is similar for the lateral jet. Gas type makes no significant difference
   "except for the back jet". The abstract's claim that helium as the lateral
   jet performs 15% better contradicts Fig. 9 (see below).
7. **Heat capacity** (§3.2). The coolant's specific heat is named "the main
   effective term". Stated, not tested.
8. **Heat flux** (Eq. 12). Wall heat flux = local fluid-side heat-transfer
   coefficient × (wall temperature − local fluid temperature). How the
   "heat load reduction" of Fig. 9 is computed from it (integration area,
   no-jet baseline) is not defined.

# Methods

* Geometry (§2.1, Figs. 1–3), from Qin's experiment: nose-cone diameter
  10 cm; spike length equal to the nose diameter; aerodome at the spike tip;
  domain 27 cm × 10 cm; half model, described as axisymmetric.
* Freestream (§2.2): $\mathrm{Ma}_\infty=5$, $p_\infty=12076$ Pa,
  $T_\infty=216$ K, zero angle of attack. Reynolds number not stated.
* Boundary conditions: pressure far field; no-slip isothermal walls at 300 K;
  symmetry planes; pressure outlet at ambient pressure; injector at total
  pressure and temperature, sonic. Jet total temperature not stated.
* Solver (§2.3): implicit in-house cell-centred finite-volume coupled code,
  "second-order upwind" for momentum and continuity, Roe flux-difference
  splitting; steady.
* Turbulence (Eqs. 1–11): Menter SST k–ω with a dilatation-dissipation
  compressibility correction (correction factor 1.5, threshold turbulent Mach
  number 0.25, production limiter 10). The standard formulation, restated.
* Species: air, CO$_2$, He; the multispecies transport model is not stated.
* Grids (§2.1, Fig. 4): three structured grids, 10800 (180 × 60), 14600
  (220 × 68) and 18400 (250 × 75) cells; first-cell height < 0.1 mm. The
  nose-cone static-to-total pressure ratio agrees between fine and very fine
  (peak about 0.016 near arc length 0.5 nose radii); the fine grid is used.
* Convergence: residuals and a mass fraction on a monitoring plane; density
  change ≤ $10^{-4}$.
* Validation: none shown; agreement with experiment is asserted for the
  authors' earlier studies (refs. [11–15]). No comparison with Qin's
  experiment.

# Tests and results

| Case | Section / figure | Conditions | Findings |
|---|---|---|---|
| Grid study | §2.1, Fig. 4 | Mach 5 | fine ≈ very fine |
| Air jets | §3.1, Fig. 5 | ratio 0.3 | front: no change; back: removes rear recirculation; top: bow-shock angle "significantly increases" |
| Air jets | §3.1, Fig. 6 | ratio 0.6 | effects stronger; qualitative |
| CO$_2$ vs He | §3.2, Figs. 7–8 | ratio 0.6 (Fig. 8 not stated) | He spreads more; CO$_2$ fraction higher on the nose for front and back |
| Heat-load reduction | §3.3, Fig. 9 | ratio 0.3 | back 58/60/74%, front 24/25/34%, top 91/92/87% (air/CO$_2$/He, approximate) |

Panels of Figs. 5–8 are not labelled by injector position.

# Notation map

| Moradi et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M$, $M_\infty$ | $\mathrm{Ma}$, $\mathrm{Ma}_\infty$ | |
| PR | words (jet-to-freestream total-pressure ratio) | not $\sigma_0$ |
| $\rho$, $T$, $\gamma$, $R$ | $\rho$, $T$, $\gamma$, $R$ | |
| $\alpha=\sqrt{\gamma RT}$ | $a$ | **collision** with $\alpha$ (angle of attack) |
| $k$, $\omega$ | words (turbulent kinetic energy, specific dissipation rate) | **collision:** registry $k$ |
| $M_t$, $M_{t0}$ | words (turbulent Mach number) | |
| $\beta$, $\beta^*$, $\beta_i$, $\beta_i^*$, $\zeta^*$ | words (SST constants) | **collision** with $\beta_s$ |
| $q$ | $q_w$ | |
| $h_f$ | words (heat-transfer coefficient) | **collision:** registry $h$ |
| $T_w$, $T_f$ | $T_w$; words | |
| $C_p$ (heat capacity) | words | **collision:** registry $C_p$ |
| $P_s/P_T$ | $p/p_0$ | reference total pressure not defined |
| $S/R$ | words (arc length over nose radius) | |

# Pages created or updated

* [Aeroheating reduction by spikes and coolant jets](/methods/aeroheating-reduction-spikes-and-jets.md)
* [SST k–ω turbulence model in high-speed flow](/methods/sst-k-omega-model.md)

# Citations

1. `/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Moradi_The_influence_of_coolant_jet_direction_on_heat_reduction_on.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier, 7 pages).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.026, printed on page 1 and
     checked on Crossref: Acta Astronaut. 151, 487–493, five authors as
     above, issue 2018-10 (no online date in Crossref). Received 27 May 2018,
     accepted 10 Jun 2018, online 15 Jun 2018 (page 1). Page-1 title matches
     the filename.
   * **How it was read.** Full text layer plus rendered pp. 488–491;
     Eqs. 1–12 read cleanly. Fig. 9 has no axis label or units; its bar
     values are approximate readings (±1%).
   * **Recorded as printed.**
     * The abstract says helium as the lateral jet cools 15% better than the
       other gases; in Fig. 9 the top (lateral) position has He below air
       and CO$_2$, and helium is about 15 points better only at the back
       (oblique) position, as §3.3 says.
     * §3.3: "injection of the top jet could significantly enhance the heat
       load", contradicted by the next sentence and Fig. 9.
     * §3: "the applied approach is inconsistent with experimental data and
       obtained results agree well", where "consistent" is meant.
     * Grid counts: 220 × 68 = 14960 and 250 × 75 = 18750, not the printed
       14600 and 18400.
     * The convergence monitor is placed "5 mm downstream of the cavity"; the
       geometry has no cavity.
     * "Our previous studies [20–26]" points to other groups' papers.
     * Ref. [41], cited for Roe splitting, is an aerodisk drag/heat paper
       and a verbatim duplicate of ref. [21].
     * The model is called axisymmetric (half simulated), the boundary
       conditions list "lateral sides and top plane" as symmetry planes, and
       the abstract calls it two-dimensional.
     * The title says supersonic; the abstract and introduction say
       hypersonic, at Mach 5.
   * **Reference list.** 50 printed entries (Crossref count 50); ref. [41]
     duplicates ref. [21]. The corresponding author appears as
     "M. Barzegar Gerdroodbary" and "M.B. Gerdroodbary". Ref. [23] (Qin et
     al.) is printed as J. Spacecr. Rockets 55 (2) (2017), while volume 55
     is the 2018 volume (not verified). Ref. [42] (Menter et al. 2003) is
     printed as a journal but is a conference proceedings volume.
