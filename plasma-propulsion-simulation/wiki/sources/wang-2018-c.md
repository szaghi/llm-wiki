---
type: Source
title: "Wang et al. (2018) — Analysis and reduction of skin-friction in a rocket-based combined-cycle engine flow path operating from Mach 1.5 to 6.0"
description: "RANS simulations of a full wide-range RBCC flow path at 16 flight points from Mach 1.5 to 6 decompose skin-friction by component (40.3% of net thrust at Mach 6, combustor 48% of the total), tabulate angle-of-attack effects, and show in a simplified step duct that hydrogen boundary-layer combustion cuts the mean wall shear stress by 57.5% at the cost of a local heat-flux rise."
resource: "doi:10.1016/j.actaastro.2018.06.028"
source_kind: paper
authors: [Wang S., He G., Yan D., Huang Z., Qin F.]
year: 2018
venue: "Acta Astronaut. 151:357–367"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Analysis_and_reduction_of_skin-friction_in_a_rocket-based_co.pdf"
tags: [context, rbcc, skin-friction, boundary-layer-combustion, rans, kerosene, hypersonic]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper computes, with steady RANS in ANSYS Fluent (SST k–ω, a
Lagrangian kerosene spray and a three-step global kerosene mechanism), the
full internal-plus-external flow path of a wide-range rocket-based
combined-cycle (RBCC) engine (forebody, inlet, combustor with struts,
cavities and three embedded rockets, variable nozzle) at 16 flight points
between Mach 1.5 and 6 and angles of attack −4° to +8° (Table 1). It
decomposes wall shear stress and integrated skin-friction by component and
relates skin-friction to net thrust: the ratio rises to 40.3% at Mach 6
(Fig. 4b); the combustor carries 48% of the engine skin-friction at Mach 6
(34% at Mach 1.5); the inlet has the highest mean wall shear stress at
Mach 6, twice the engine average. Angle-of-attack effects are tabulated at
Mach 1.8, 3 and 6 (Table 3). A simplified 3D rectangular duct with a
rearward-facing step at Mach-6 combustor-entry conditions then shows that
hydrogen boundary-layer combustion lowers the mean upper-wall shear stress
from 1234 Pa to 525 Pa (57.5%; the abstract says 57.7%), at the price of a
strong local heat-flux increase near 350 mm.

# Key claims

1. **Skin-friction against flight Mach** (§3.2, Fig. 4). Integrated
   skin-friction (normalized by an unstated constant) and mean wall shear
   stress rise with flight Mach, sharply after Mach 3; skin-friction is
   40.3% of net thrust at Mach 6 (Fig. 4b, approximate: about 12–15% at
   Mach 1.5–3, about 19% at 4, about 26% at 5). Shown. Halving it would
   raise Mach-6 thrust by 20% (arithmetic consequence, stated).
2. **Component shares** (§3.2, Fig. 5). Combustor share 48% at Mach 6, 34%
   at Mach 1.5; inlet mean wall shear about 640 Pa at Mach 6 (figure),
   twice the engine average; rocket inner surfaces are about 4% of engine
   area, with wall shear peaking about 490 Pa at Mach 1.8 but a small
   contribution; rockets off from Mach 4. Shown.
3. **Distributions** (§3.3, Fig. 6). At Mach 1.8 wall shear spans 0–300 Pa
   behind the rockets (shear layer between rocket exhaust and air); at Mach
   6 peaks reach about 2000 Pa, with heat release moved forward into the
   inlet. Shown.
4. **Angle of attack** (§3.3, Fig. 7, Table 3), rocket state and overall
   equivalence ratio fixed:

   | AoA [°] | Norm. skin-friction, Mach 1.8 / 3 / 6 | Skin-friction / net thrust [%], Mach 1.8 / 3 / 6 |
   |---|---|---|
   | −4 | 2.30 / 5.59 / 7.52 | 10.95 / 12.51 / 45.90 |
   | 0 | 2.28 / 6.06 / 9.48 | 12.19 / 12.19 / 40.33 |
   | +4 | 2.24 / 6.54 / 10.67 | 10.90 / 12.71 / 39.86 |
   | +8 | 2.52 / 6.67 / 11.35 | 22.33 / 12.81 / 48.42 |

   At mid and high speed skin-friction grows nearly linearly with angle of
   attack; at Mach 6 the thrust ratio first falls then rises; at low speed
   it fluctuates and rises rapidly beyond +4°. Nozzle wall shear barely
   depends on flight speed, and the nozzle dominates at low speed. Shown,
   with interpretation.
5. **Boundary-layer combustion** (§3.4, Figs. 9, 11). With H2 injected at a
   3 mm rearward-facing step, mean upper-wall shear stress is 1234 Pa (air
   only), 1214 Pa (injection, no combustion) and 525 Pa (combustion), a
   57.5% reduction. Shown. Mechanism stated after Stalker and Goyne:
   near-wall density reduction lowers the Reynolds stress; downstream
   mixing raises density and shear again; injection without combustion can
   raise downstream shear.
6. **Heat-flux penalty** (§3.4, Fig. 10). Upper-wall heat flux about
   −2 MW/m² for air only; cold-H2 injection lowers it near the step;
   combustion produces a strong region near 350 mm peaking about
   −4.9 MW/m² (sign convention not stated). Shown.
7. **Literature** (§1), attributed: skin-friction over 50% of total drag on
   hypersonic vehicles; inlet, combustor and nozzle over 60% of total
   skin-friction; passive devices at most about 10% reduction; arc
   discharge 18.5% (air) and 27.4% (argon); boundary-layer combustion over
   70%; about 50% with H2 and negligible with JP-10.

# Methods

* **Solver**: ANSYS Fluent, steady RANS, implicit backward-Euler pseudo-time
  and a second-order TVD spatial scheme (§2.2.2); compressible multispecies
  equations with spray sources, Sutherland viscosity, turbulent Schmidt
  number 0.9.
* **Turbulence**: Menter SST k–ω with the Fluent constants listed (§2.2.2);
  wall treatment and wall-unit resolution not stated.
* **Spray**: liquid kerosene C12H23, solid-cone injection, dilute
  Lagrangian tracking, TAB secondary breakup (no primary breakup), initial
  mean droplet diameter 0.04 mm, Rosin–Rammler distribution,
  non-equilibrium evaporation and boiling law.
* **Chemistry**: three-step irreversible global mechanism (Table 2),
  finite rate without turbulence–chemistry interaction:
  C12H23 + O2 → CO + H2O ($A$ = 1.60e+15, $E$ = 2.20e+08 J/kmol, orders
  0.5 and 1.0), CO oxidation ($A$ = 1.92e+10, $E$ = 1.03e+08 J/kmol),
  H2 oxidation ($A$ = 9.87e+08, $E$ = 3.10e+07 J/kmol); temperature
  exponents zero.
* **Engine grid and conditions**: grid size, grid independence, boundary
  conditions, trajectory, fuel equivalence ratios and rocket flows not
  stated.
* **Step duct** (§3.4, Fig. 8): 900 mm long; entry 250 mm, 54 × 29 mm;
  3 mm step with three 3 × 3 mm injection holes; inflow total temperature
  1850 K, total pressure 2.4 MPa, Mach 2.3; H2 at 1 MPa and 300 K total;
  overall equivalence ratio 0.2.
* **Validation**: Tsuru et al. direct skin-friction duct (Mach 2.5,
  vitiated air): measured 1072 Pa ± 5% and 1060 Pa ± 10%, computed 950 Pa
  (about 11% low, called acceptable); the authors' own Mach-3 ramjet-mode
  direct-connect test, axial wall pressure agreeing "for most part"
  (conditions not given).

# Tests and results

* Table 1: 16 cases (Mach 1.5, 1.8, 2, 3, 4, 5, 6; angles of attack −4,
  0, +4, +8° at 1.8, 3 and 6); rockets on to Mach 3, off from Mach 4.
* Fig. 4a (approximate): normalized skin-friction about 1.9 to 9.5 and mean
  wall shear about 70 to 310 Pa from Mach 1.5 to 6.
* Fig. 5 (approximate, Mach 6): mean shear inlet 640, forebody 340,
  combustor 320, nozzle 210 Pa.
* Fig. 9a (approximate): with combustion the shear drops near zero after
  the step, peaks about 730 Pa near 0.4 m, dips to about 270 Pa near
  0.57 m and rises to about 850 Pa at the exit; negative shear behind the
  step (Fig. 11).

# Notation map

The paper is outside the plasma-propulsion domain; the registry column
gives a [notation](/notation.md) symbol only where its registry meaning
fits, otherwise "words".

| Wang et al. (2018) | Registry | Note |
|---|---|---|
| Ma | words (flight Mach number) | |
| $\rho$, $p$, $T$ | words | registry $p_s$, $T_s$ are species quantities |
| $u_i$ | words (fluid velocity) | |
| $Y_s$, $R_s$ | words (mass fraction, production rate) | species index $s$ as in the registry |
| ER | words (equivalence ratio) | |
| $F_N$ | $F$ | net thrust |
| $F_D$, $F_0$ | words (integrated skin-friction, normalizing constant) | |
| $\tau_{ij}$ | words (stress tensor) | |
| $k$, $\omega$, $\mu$, $\mu_t$, $Sc_t$ | words | **collision** with $k$, $\omega$ (wave), $\mu_\perp$ |
| $D$, $D_{s,m}$ | words (diffusion coefficients) | |
| $A_r$, $\beta_r$, $E_r$, $\eta_F$, $\eta_O$ | words | **collision** with $\mathbf E$, $\eta$ |
| $q$ | words (wall heat flux) | **collision risk** with $\mathbf q_s$ |
| $d_p$ | words (droplet diameter) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Analysis_and_reduction_of_skin-friction_in_a_rocket-based_co.pdf`.
   * **Version.** Published Elsevier typeset PDF, 11 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.028, printed on page 1
     and checked on Crossref (title, five authors, vol. 151, pp. 357–367
     match); issued and published-print 2018-10; Crossref has no online
     date, page 1 gives 15 June 2018 (received 29 May, accepted 10 June
     2018). Page 1 matches the filename title.
   * **How it was read.** Full text; formulas from the rendered pages;
     plot values approximate. Eq. 1-10 and the SST blending functions not
     reproduced.
   * **Recorded as printed.**
     * Reduction 57.7% in the abstract, 57.5% in §3.4 and the conclusions;
       (1234 − 525)/1234 = 57.5%.
     * The conclusions call it a 57.5% reduction of "total drag"; the
       computed quantity is the mean upper-wall shear stress of the duct.
     * §3.2 cites "Fig. 3(b)" for the 40.3%; it is in Fig. 4(b).
     * §3.3: Mach-6 wall shear "several orders of magnitude higher" than
       at Mach 1.8, while Fig. 6 shows about 2000 against 300 Pa.
     * "Almost 4 times" (§3.2, conclusions), while Fig. 4a shows about 5×
       (normalized skin-friction) and about 4.4× (mean shear).
     * Step geometry: 54 mm entry height and a 3 mm step in the text, while
       Fig. 8 shows 54 and 60 mm heights.
     * Ejector-to-ramjet transition "at 3 Ma", later "between 3 Ma and
       4 Ma" (§3.3).
     * Table 2 caption cites refs. 35–36 (droplet evaporation) while the
       text cites 38–39 for the mechanism; "Clark [19]" is ref. 20;
       "equations (3)–(8)" means Eq. 3-8; the SST blending functions are
       referred to ref. 30, a hybrid-rocket heat-transfer paper.
     * Validation within neither stated experimental uncertainty is called
       acceptable.
     * The printed SST $\alpha_\infty=0.25$ and the Table 2 pre-exponential
       unit form are reproduced as printed; the normalizing constant $F_0$
       and the Fig. 10 heat-flux sign convention are never given.
   * **Reference list.** 45 printed entries (Crossref reference-count 45).
     Printed slips: ref. 2 Acta Astronaut. vol. 63 dated 2006; refs. 24 and
     27 print journal pages as AIAA paper numbers; ref. 25 "C.W. David" for
     Wilcox; ref. 29 first author "D.A. Y"; ref. 33 vol. 20 dated 2012;
     ref. 41 vol. 114 dated 2018; ref. 38 names garbled; ref. 19 given
     name and surname apparently inverted.
