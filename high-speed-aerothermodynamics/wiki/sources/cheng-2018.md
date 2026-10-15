---
type: Source
title: "Cheng et al. (2018) — Performance evaluation and comparison of electricity generation systems based on single- and two-stage thermoelectric generator for hypersonic vehicles"
description: "Quasi-one-dimensional models of single- and two-stage SiGe thermoelectric generators heated by hydrogen fuel leaving the engine-wall cooling channels and cooled by fresh fuel, showing that the single stage gives the higher power density (16.53 kW/m² at 1200 K) and the two-stage the higher efficiency at maximum power (10.78%)."
resource: "doi:10.1016/j.actaastro.2018.05.033"
source_kind: paper
authors: [Cheng K., Zhang D., Qin J., Zhang S., Bao W.]
year: 2018
venue: "Acta Astronaut. 151:15–21"
local_file: "/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Cheng_Performance_evaluation_and_comparison_of_electricity_generat.pdf"
tags: [thermoelectric, power-generation, thermal-management, fuel-cooling, hypersonic-vehicle]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper builds steady, quasi-one-dimensional models of single-stage and
two-stage SiGe thermoelectric generators (TEGs) on a hypersonic vehicle.
Hydrogen fuel already heated in the engine-wall cooling channels is the heat
source; cold hydrogen fuel, before it enters the wall channels, is the heat
sink; the two channels run in counter-flow. A nodal energy balance at each
streamwise element (walls, junctions and, for two stages, an intermediate
junction) is solved as a linear system (Eqs. 9 and 23) and coupled
iteratively to one-dimensional finite-difference channel equations
(Eqs. 24–27) closed by the Dittus–Boelter correlation (Eqs. 30–31). At
heating-channel inlet temperatures of 800, 1000 and 1200 K, the single-stage
TEG gives the highest maximum power density, 16.53 kW/m² at 1200 K
(Table 3); the two-stage TEG gives the highest conversion efficiency at
maximum power, 10.78% at 1200 K (Table 4). The authors attribute the
two-stage gain to less parasitic conduction from the hot to the cold channel
and argue that the second stage should use a lower-temperature material
(AgPb$_m$SbTe$_{2+m}$).

# Key claims

1. **Single stage wins on power density** (§4.4, Table 3). Maximum power
   density 4.22 / 9.35 / 16.53 kW/m² at 800 / 1000 / 1200 K, against 3.38 /
   7.43 / 12.94 kW/m² for two stages; attributed to the lower total internal
   resistance. Shown (own model).
2. **Two stages win on efficiency at maximum power** (§4.4, Table 4). Single
   stage 4.63 / 6.85 / 8.96%; two stages 5.79 / 8.45 / 10.78%; attributed to
   less heat conducted "in vain" to the cooling channel through the taller
   module. Shown.
3. Both quantities rise monotonically with the heating-channel inlet
   temperature (Tables 3–4). Shown.
4. **Single-stage temperature budget at 1200 K** (§4.2, Fig. 5). The heating
   fuel drops by about 390 K and the cooling fuel rises by 360 K, so most of
   the heat passes to the cold fuel instead of being converted; the drop
   across the 0.2 mm β-Si$_3$N$_4$ plate is negligible. Shown.
5. **Two-stage temperature budget at 1200 K** (§4.3, Fig. 7). Heating fuel
   −250 K, cooling fuel +220 K; the two stages carry almost equal temperature
   differences. Shown.
6. **Figure of merit along the module** (Figs. 6, 8). Single stage: $ZT$
   rises from about 0.45 to 1.11 along $x$. Two stages: about 0.94–1.24 in
   the first stage and about 0.34–0.77 in the second (figure readings). SiGe
   is argued to be ill-suited to the second stage; a different material per
   stage is recommended (ref. [32]). Recommendation, not computed.
7. **Matched load is approximate** (§3.1, after Eq. 13). Since junction
   temperatures depend on the current, the open-circuit voltage depends on
   the load, and maximum power does not occur exactly at load resistance =
   internal resistance; the paper uses that equality as an approximation.
   Stated, citing ref. [30] (the authors' multi-stage paper).
8. **Fuel as the only heat sink** (§1, §2.4). In hypersonic flight the air is
   too hot to act as coolant, so on-board fuel is the only cold source;
   hydrogen avoids hydrocarbon coking. Stated.
9. **Element relations** (§3.1, Eqs. 1–16). Seebeck coefficient of a couple
   = p-leg − n-leg; electrical resistance and thermal conductance of the
   legs and ceramic plates; hot-junction balance with Peltier, half-Joule and
   conduction terms (Eq. 6); load power from open-circuit voltage and
   resistances (Eq. 13); power density per channel area (Eq. 14); efficiency
   = power / input heat (Eq. 16); Dittus–Boelter
   $\mathrm{Nu}=0.023\,\mathrm{Re}^{0.8}\mathrm{Pr}^{0.4}$ (Eq. 31). The
   reader checked the matrix rows of Eqs. 9 and 23 against Eqs. 5–8 and
   17–22.
10. **Conclusion** (§5). Thermoelectric generation is feasible as an
    auxiliary electricity source on hypersonic vehicles. Stated as an
    inference; no system-level mass or power budget.

# Methods

* Purely numerical, steady, quasi-1D in the streamwise direction; no
  experiment and no validation against measured TEG data.
* TEG nodal model: thermal-resistance network per element (fuel → convection
  → hot wall → ceramic plate → hot junction → legs → cold junction → ceramic
  → cold wall → convection → cold fuel), a 4 × 4 linear system per element
  for one stage (Eq. 9), 6 × 6 with an inter-stage plate for two (Eqs.
  17–23). Elements in electrical series (Eqs. 10–11).
* Channel model: first-order finite-difference mass, momentum (friction
  factor and hydraulic diameter), energy with heat source, and ideal-gas
  state (Eqs. 24–27); Newton cooling (Eqs. 28–29); Dittus–Boelter (attributed
  to ref. [31]). Friction-factor correlation not stated.
* Coupling: fuel temperatures feed the TEG system, TEG heat rates feed the
  channel energy equation, iterated to convergence (§3.3); tolerance and
  element count not stated.
* Materials: SiGe legs with $ZT(T)$ from Wang et al. (ref. [25]; about 0.15
  at 300 K to about 1.3 at 1200 K, Fig. 2); β-Si$_3$N$_4$ plate conductivity
  from Hirosaki et al. (ref. [27]; about 122 W/(m·K) at 300 K, about
  28 W/(m·K) at 1400 K); hydrogen as ideal gas with CHEMKIN-II properties.
* Geometry (Table 1): element section 2 × 2 mm, height 8 mm, gap 0.4 mm
  (air), connector 0.1 mm, ceramic plate 0.2 mm. Channel dimensions, channel
  and element counts, and two-stage leg heights not stated.
* Operating point (Table 2): mass flow 0.3 g/s (split by an unstated channel
  number); cooling inlet 300 K; heating inlet 1200 K (also 800 and 1000 K);
  cooling inlet pressure 3 MPa; counter-flow; load = internal resistance.
  Heat loss to ambient not modelled. No uncertainty reported.

# Tests and results

| Case | Section | Conditions | Findings |
|---|---|---|---|
| Single stage, temperatures | §4.2, Fig. 5 | 1200 K | heating 1200 → about 810 K; cooling 300 → about 670 K |
| Single stage, $ZT$ | §4.2, Fig. 6 | 1200 K | 0.45 → 1.11 |
| Two stages, temperatures | §4.3, Fig. 7 | 1200 K | heating −250 K; cooling +220 K; intermediate junction about 670–900 K (figure) |
| Two stages, $ZT$ | §4.3, Fig. 8 | 1200 K | stage 1 about 0.94–1.24; stage 2 about 0.34–0.77 (figure) |
| Maximum power density | §4.4, Table 3 | 800 / 1000 / 1200 K | single 4.22 / 9.35 / 16.53; two-stage 3.38 / 7.43 / 12.94 kW/m² |
| Efficiency at maximum power | §4.4, Table 4 | same | single 4.63 / 6.85 / 8.96%; two-stage 5.79 / 8.45 / 10.78% |

# Notation map

| Cheng et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $T$, $\rho$, $u$, $p$ | $T$, $\rho$, $u$, $p$ | |
| $T_{fh0}$ | words (heating-channel inlet temperature) | **collision:** subscript 0 means inlet, not total |
| $T_{wh}$, $T_{wc}$ | $T_w$ | hot and cold side |
| $T_{jh}$, $T_{jc}$ | words (junction temperatures) | |
| $h$ | words (convection coefficient) | **collision:** registry $h$ |
| $\lambda$ | $k$ | thermal conductivity |
| $\sigma$ | words (electrical conductivity) | **collision** with $\sigma_0$ |
| $\alpha$ | words (Seebeck coefficient) | **collision** with $\alpha$ (angle of attack) |
| $ZT$ | $ZT$ | |
| $\eta$ | words (conversion efficiency) | |
| $f$, $D_h$ | words | friction factor (type not specified), hydraulic diameter |
| $m$ | words (mass flow rate) | |
| $Nu$, $Re$, $Pr$ | words (Nusselt); $\mathrm{Re}$, $\mathrm{Pr}$ | Re on hydraulic diameter |
| $\theta_{cp}$ | words (plate thickness) | |
| $P$, $P_D$, $Q$ | words (power, power density, heat rate) | not the registry $Q$ (integrated heat load) |

# Pages created or updated

* [Fuel-cooled thermoelectric generators for hypersonic vehicles](/methods/thermoelectric-generator-for-hypersonic-vehicles.md)

# Citations

1. `/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Cheng_Performance_evaluation_and_comparison_of_electricity_generat.pdf`.
   * **Version.** Final published Elsevier typeset version (7 pages).
   * **Identity.** doi:10.1016/j.actaastro.2018.05.033, printed on page 1 and
     checked on Crossref (2026-10-14): Acta Astronaut. 151, 15–21, five
     authors in printed order, issue 2018-10 (no online date in Crossref).
     Received 2 Nov 2017, revised 10 May 2018, accepted 16 May 2018, online
     17 May 2018 (page 1). Page-1 title matches the filename.
   * **How it was read.** Text layer plus rendered pp. 17–20 (equations,
     Figs. 2, 5–8, Tables 1–4); no equation illegible. Figure values are
     approximate readings.
   * **Scope.** The paper has no external aerothermodynamics; its link to
     this bundle is on-board energy conversion from heat on hypersonic
     vehicles (bundle law).
   * **Recorded as printed.**
     * §2.3 calls the β-Si$_3$N$_4$ conductivity "experimental results" of
       Hirosaki et al. (ref. [27]), whose title is a molecular-dynamics
       calculation.
     * Eqs. 28–29 use junction temperatures $T_j(i,1)$, $T_j(i,n)$ never
       defined; Eqs. 5, 8, 15 write the same exchange with wall
       temperatures.
     * §4.2 "conversion coefficients" for convection coefficients.
     * Cooling-fuel rise: text 360 K and 220 K; Figs. 5 and 7 read about
       370 K and 230 K (within reading error).
     * The abstract calls 10.78% the "optimal conversion efficiency"; §4.4
       gives it as the efficiency at maximum power output.
     * Fig. 2 data end near 1175 K at about 1.32, while the text says 1.3 at
       1200 K.
     * Ref. [25] covers n-type SiGe only; the p-leg data source is not
       stated.
   * **Reference list.** 32 printed entries (Crossref count 32). Printed ref.
     [30] (Cheng et al., Appl. Therm. Eng. 130 (2018) 1598–1609) shares this
     source's natural key and is a different work (`cheng-2018-b`). Slips:
     [30] "Engieering", [4] "Conferenc", [15] "heat-electricty", [26] no
     venue, [27] no pages, [31] attributes Dittus–Boelter to an AIAA
     uncertainty paper.
