---
type: Source
title: "Cheng et al. (2018) — Performance evaluation and comparison of electricity generation systems based on single- and two-stage thermoelectric generator for hypersonic vehicles"
description: "Builds steady quasi-one-dimensional models of single- and two-stage SiGe thermoelectric generators placed between hot and cold hydrogen-fuel channels of a regeneratively cooled hypersonic vehicle, finding the single stage gives the higher maximum power density (16.53 kW/m² at 1200 K) and the two stage the higher efficiency at maximum power (10.78%)."
resource: "doi:10.1016/j.actaastro.2018.05.033"
source_kind: paper
authors: [Cheng K., Zhang D., Qin J., Zhang S., Bao W.]
year: 2018
venue: "Acta Astronaut. 151:15–21"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Cheng_Performance_evaluation_and_comparison_of_electricity_generat.pdf"
tags: [context, power-generation, thermoelectric, hypersonic, thermal-management]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper builds steady, quasi-one-dimensional models of single-stage and
two-stage SiGe thermoelectric generators (TEGs) on a hypersonic vehicle.
Hot hydrogen fuel, already heated in the engine-wall cooling channels, is
the heat source; cold hydrogen fuel, before it enters the wall channels,
is the heat sink; the two channels run in counter-flow. A nodal energy
balance at each streamwise element (walls, junctions and, for two stages,
an intermediate junction) is solved as a linear system (Eqs. 9 and 23)
and coupled iteratively to 1-D finite-difference channel equations
(Eqs. 24–27) closed by the Dittus–Boelter correlation (Eqs. 30–31). At
heating-channel inlet temperatures of 800, 1000 and 1200 K, the
single-stage TEG gives the higher maximum power density, 16.53 kW/m² at
1200 K (Table 3), and the two-stage TEG the higher conversion efficiency
at maximum power, 10.78% at 1200 K (Table 4). The authors attribute the
two-stage gain to less parasitic conduction from the hot to the cold
channel and argue for a lower-temperature material in the second stage
(AgPb$_m$SbTe$_{2+m}$). The paper is about onboard power generation and
thermal management; it has no external-flow content.

# Key claims

Symbols are the paper's own (see the notation map). All quantitative
claims come from the paper's own model; there is no experiment.

1. **Power density** (§4.4, Table 3): single stage 4.22 / 9.35 / 16.53
   kW/m², two stage 3.38 / 7.43 / 12.94 kW/m² at 800 / 1000 / 1200 K;
   attributed to the single stage's lower internal resistance. Shown.
2. **Efficiency at maximum power** (§4.4, Table 4): single stage 4.63 /
   6.85 / 8.96%, two stage 5.79 / 8.45 / 10.78%; attributed to less heat
   conducted "in vain" through the taller module. Shown.
3. Both quantities increase monotonically with the heating inlet
   temperature (Tables 3–4). Shown.
4. **Single-stage temperature budget** at 1200 K (§4.2, Fig. 5): the
   heating fuel drops by about 390 K, the cooling fuel rises by 360 K, so
   most of the heat passes to the cold fuel; the drop across the 0.2 mm
   β-Si₃N₄ plate is negligible. Shown.
5. **Two-stage temperature budget** at 1200 K (§4.3, Fig. 7): heating fuel
   drops 250 K, cooling fuel rises 220 K, the two stages carry nearly equal
   temperature differences. Shown.
6. **Figure of merit** (Figs. 6, 8): single-stage ZT rises from about 0.45
   to 1.11 along $x$; in the two-stage TEG about 0.94–1.24 (stage 1) and
   0.34–0.77 (stage 2), read from Fig. 8. The recommendation of a
   different second-stage material is argued, not computed.
7. **Matched load is approximate** (§3.1, after Eq. 13): since junction
   temperatures depend on current, maximum power does not occur exactly at
   $R_L=R_{in}$; $R_L=R_{in}$ is used as an approximation. Stated, citing
   the authors' multi-stage paper.
8. **Fuel as the only heat sink** (§§1, 2.4; stated): in hypersonic flight
   the air is too hot to cool, so onboard fuel is the only cold source;
   hydrogen avoids hydrocarbon coking.
9. **Element relations** (§3.1), read cleanly: $\alpha=\alpha_p-\alpha_n$
   (Eq. 1); $R=l_p/(\sigma_pA_p)+l_n/(\sigma_nA_n)$ (Eq. 2);
   $K_{ele}=\lambda_pA_p/l_p+\lambda_nA_n/l_n$ (Eq. 3); hot-junction balance
   $K^i_{cph}[T_{wh}(i)-T_{jh}(i)]=\alpha_iIT_{jh}(i)-0.5I^2R_i+K^i_{ele}[T_{jh}(i)-T_{jc}(i)]$
   (Eq. 6); $P=U_LI=U_o^2R_L/(R_L+R_{in})^2$ (Eq. 13);
   $P_D=P/(W_{ch}L_{ch})$ (Eq. 14); $\eta=P/Q_{inp}$ (Eq. 16);
   $Nu=0.023\,\mathrm{Re}^{0.8}\mathrm{Pr}^{0.4}$ (Eq. 31). The reader checked
   that the matrices of Eqs. 9 and 23 follow from Eqs. 5–8 and 17–22.
10. **Conclusion** (§5, stated): thermoelectric generation is feasible as
    an auxiliary electricity source on hypersonic vehicles; no system-level
    mass or power budget is given.

# Methods

* Purely numerical, steady, quasi-1-D; no validation against measured TEG
  data.
* **Nodal model**: per-element thermal-resistance network (convection, hot
  wall, ceramic plate, hot junction with Peltier, half-Joule and leg
  conduction terms, cold junction, ceramic, cold wall, convection), a 4×4
  linear system (Eq. 9) for the single stage and 6×6 (Eq. 23) for the two
  stage; all elements in series electrically (Eqs. 10–11).
* **Channel model**: finite-difference mass, momentum (friction factor,
  hydraulic diameter), energy with heat source, ideal-gas state (Eqs.
  24–27); Newton cooling (Eqs. 28–29) with Dittus–Boelter (Eqs. 30–31,
  attributed). The friction-factor correlation, number of elements,
  convergence tolerance and grid independence are not stated.
* **Materials**: SiGe legs with ZT(T) from Wang et al. (Fig. 2, about 0.15
  at 300 K to 1.3 at 1200 K); β-Si₃N₄ conductivity from Hirosaki et al.
  (about 122 W/(m·K) at 300 K, 28 W/(m·K) at 1400 K); hydrogen properties
  from CHEMKIN-II.
* **Geometry** (Table 1): element section 2 × 2 mm, height 8 mm, gap 0.4 mm
  (air), connector 0.1 mm, ceramic plate 0.2 mm. Channel dimensions and
  counts, element count and the two-stage leg heights are not stated.
* **Conditions** (Table 2): mass flow 0.3 g/s; cooling inlet 300 K and
  3 MPa; heating inlet 1200 K (also 800 and 1000 K); counter-flow; load
  $R_L=R_{in}$; no heat loss to ambient; no uncertainty reported.

# Tests and results

| Case | Section | Finding |
|---|---|---|
| Single stage, temperatures, 1200 K | §4.2, Fig. 5 | heating 1200 → about 810 K, cooling 300 → about 670 K |
| Single stage, ZT | §4.2, Fig. 6 | 0.45 → 1.11 |
| Two stage, temperatures, 1200 K | §4.3, Fig. 7 | drops of 250 K and 220 K; intermediate junction about 670–900 K (approximate) |
| Two stage, ZT | §4.3, Fig. 8 | 0.94–1.24 and 0.34–0.77 (approximate) |
| Maximum power density | Table 3 | claim 1 |
| Efficiency at maximum power | Table 4 | claim 2 |

# Notation map

| Cheng et al. (2018) | Registry | Note |
|---|---|---|
| $P$ | $P$ | electric power |
| $m$ | $\dot m$ | mass flow rate; the paper drops the dot |
| $T_{wh}$, $T_{wc}$ | $T_w$ | hot- and cold-side wall temperatures |
| $T_{fh0}$, $T_{fh}$, $T_{fc}$, $T_{jh}$, $T_{jc}$ | words | fuel inlet, fuel and junction temperatures |
| $\eta$ | words (conversion efficiency) | **collision:** registry $\eta$ is thrust efficiency |
| $\alpha$ | words (Seebeck coefficient) | |
| $\sigma$ | words (electrical conductivity) | **collision:** registry $\sigma_{sk}$ is a cross section |
| $\lambda$ | words (thermal conductivity) | **collision:** registry $\lambda_D$, $\lambda_w$ |
| $I$, $U_o$, $U_L$, $R$, $R_L$, $R_{in}$ | words (current, voltages, resistances) | |
| $ZT$ | words (thermoelectric figure of merit) | |
| $h$, $Nu$, $Re$, $Pr$, $D_h$ | words | |
| $f$ | words (friction factor) | **collision:** registry $f_s$ is a distribution function |
| $\theta_{cp}$ | words (ceramic thickness) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $\rho$, $u$, $p$ | words | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Cheng_Performance_evaluation_and_comparison_of_electricity_generat.pdf`.
   * **Version.** Final published typeset version, 7 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.033, printed on page 1
     and checked on Crossref: title, five authors in printed order, Acta
     Astronaut. 151:15–21 match; issue October 2018 (no online date on
     Crossref); page 1 gives received 2 Nov 2017, revised 10 May 2018,
     accepted 16 May 2018, online 17 May 2018. Page 1 matches the filename
     title.
   * **How it was read.** Text layer plus rendered pages 17–20 for the
     equations, Figs. 2, 5–8 and Tables 1–4; all equations legible. Values
     read from Figs. 5, 7, 8 are approximate.
   * **Recorded as printed.**
     * §2.3 calls the β-Si₃N₄ conductivity of ref. [27] "experimental
       results", but [27] is titled "Molecular dynamics calculation of the
       ideal thermal conductivity…".
     * Eqs. 28–29 use junction temperatures $T_j(i,1)$, $T_j(i,n)$ that are
       never defined, where Eqs. 5, 8, 15 write the same exchange with the
       wall temperatures.
     * "Conversion coefficients" (§4.2) for convection coefficients.
     * The cooling-fuel rises of 360 K and 220 K in the text read as about
       370 K and 230 K on Figs. 5 and 7 (within reading error).
     * The abstract calls 10.78% the "optimal conversion efficiency"; §4.4
       gives it as the efficiency at maximum power output.
     * Fig. 2 data end near 1175 K at about 1.32, while the text says ZT
       reaches about 1.3 at 1200 K.
     * Ref. [25] (Wang et al.) covers n-type SiGe only; the p-leg data
       source is not stated.
   * **Reference list.** 32 printed entries, matching the Crossref
     reference count. Printed slips: "Applied Thermal Engieering" (ref.
     [30]), "Conferenc" ([4]), "heat-electricty" ([15]); ref. [26] has no
     venue, ref. [27] no pages; ref. [31] cites Dittus–Boelter to an AIAA
     uncertainty paper. Ref. [30] (Cheng et al., Appl. Therm. Eng. 130
     (2018) 1598–1609) is a different work by the same first author and
     year, keyed `cheng-2018-b` to avoid colliding with this source.
