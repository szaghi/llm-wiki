---
type: Source
title: "Wang et al. (2018) — Analysis and reduction of skin-friction in a rocket-based combined-cycle engine flow path operating from Mach 1.5 to 6.0"
description: "RANS computations of a complete kerosene-fuelled RBCC flow path at 16 flight points from Mach 1.5 to 6 that decompose skin friction by component and relate it to thrust (40.3% of thrust at Mach 6), plus a simplified step-duct computation in which hydrogen boundary-layer combustion lowers the mean wall shear stress by 57.5% at the cost of a local heat-flux rise."
resource: "doi:10.1016/j.actaastro.2018.06.028"
source_kind: paper
authors: [Wang S., He G., Yan D., Huang Z., Qin F.]
year: 2018
venue: "Acta Astronaut. 151:357–367"
local_file: "/home/stefano/papers/mosaic/chemical-airbreathing-propulsion/2018_Crossref_Acta_Astronautica_Wang_Analysis_and_reduction_of_skin-friction_in_a_rocket-based_co.pdf"
tags: [rbcc, skin-friction, boundary-layer-combustion, rans, kerosene, hydrogen, drag-reduction]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper computes, with steady RANS in ANSYS Fluent (SST k–ω, a
Lagrangian kerosene spray and a three-step global kerosene mechanism), the
complete internal and external flow path of a wide-range rocket-based
combined-cycle (RBCC) engine: forebody, inlet, a combustor with struts,
cavities and three embedded rockets, and a variable nozzle. It covers 16
flight points between Mach 1.5 and 6 and angles of attack from −4° to +8°
(Table 1). It decomposes the wall shear stress and the integrated skin
friction by component and relates the skin friction to net thrust: the
ratio reaches 40.3% at Mach 6 (Fig. 4b), the combustor carries 48% of the
engine skin friction at Mach 6 (34% at Mach 1.5), and the inlet has the
highest mean wall shear stress at Mach 6, twice the engine average.
Angle-of-attack effects are tabulated at Mach 1.8, 3 and 6 (Table 3).
Finally, a simplified 3-D rectangular duct with a rearward-facing step at
Mach-6 combustor-entry conditions shows that hydrogen boundary-layer
combustion lowers the mean upper-wall shear stress from 1234 Pa to 525 Pa
(57.5%), with a strong local heat-flux rise near $x=350$ mm.

# Key claims

1. **Skin friction grows with flight Mach number** (§3.2, Fig. 4). The
   integrated skin friction (normalized by an undefined constant) and the
   mean wall shear stress rise with flight Mach number, sharply above
   Mach 3. Skin friction is 40.3% of net thrust at Mach 6; the reader's
   readings of Fig. 4b give about 12–15% at Mach 1.5–3, about 19% at
   Mach 4 and about 26% at Mach 5. Shown.
2. **Halving skin friction** would raise thrust by 20% at Mach 6 (§3.2).
   Stated; an arithmetic consequence of claim 1.
3. **Component shares** (§3.2, Fig. 5). The combustor carries 48% of the
   skin friction at Mach 6 and 34% at Mach 1.5. The inlet's mean wall
   shear stress at Mach 6 is about 640 Pa (figure reading), twice the
   engine average. The rocket inner surfaces are about 4% of the engine
   area; their wall shear peaks at about 490 Pa at Mach 1.8 (figure
   reading) but their contribution is small; the rockets are off from
   Mach 4. Shown.
4. **Shear distribution** (§3.3, Fig. 6). At Mach 1.8 wall shear spans
   0–300 Pa behind the rockets (shear layer between rocket exhaust and
   air); at Mach 6 peaks reach about 2000 Pa, with heat release moved
   forward into the inlet. Shown.
5. **Angle of attack** (§3.3, Fig. 7, Table 3). With rocket state and
   overall equivalence ratio fixed, skin friction grows nearly linearly
   with angle of attack at mid and high speed (larger capture area,
   stronger combustion at fixed kerosene equivalence ratio); at Mach 6 the
   skin-friction-to-thrust ratio first decreases then increases; at low
   speed (poor inlet startability) the ratio fluctuates and rises rapidly
   beyond +4°. Nozzle wall shear barely depends on flight speed, and the
   nozzle dominates the skin friction at low speed. Shown.
6. **Boundary-layer combustion** (§3.4, Figs. 9, 11). Mean upper-wall
   shear stress 1234 Pa (air only), 1214 Pa (hydrogen injection, no
   combustion), 525 Pa (hydrogen combustion): a 57.5% reduction. Shown.
   The mechanism, near-wall density reduction lowering the Reynolds stress,
   is stated after Stalker and Goyne (refs. 11–15).
7. **Heat-flux penalty** (§3.4, Fig. 10). Total heat flux on the upper-wall
   midline is about −2 MW/m² for air only; combustion produces a strong
   exothermic region near $x\approx350$ mm with a peak of about
   −4.9 MW/m² (figure reading; sign convention not stated). Shown.
8. **Literature** (§1, attributed). Skin friction exceeds 50% of total drag
   on hypersonic vehicles (ref. 9); inlet, combustor and nozzle exceed 60%
   of total skin friction (ref. 10); passive methods such as riblets give
   at most about 10% (ref. 16); arc discharge 18.5% (air) and 27.4%
   (argon) (ref. 18); boundary-layer combustion above 70% (ref. 11); about
   50% with hydrogen and negligible with JP-10 (ref. 20).

# Methods

* **Solver.** ANSYS Fluent (ref. 23), steady RANS, "steady state implicit
  backward Euler time scheme" and "second-order accuracy total variation
  diminishing spatial scheme" (§2.2.2). Pressure- or density-based solver
  and flux scheme not stated.
* **Equations.** Compressible multispecies RANS with spray source terms,
  Eqs. 1-1 to 1-11; ideal-gas mixture; Sutherland viscosity; turbulent
  Schmidt number 0.9.
* **Turbulence.** Menter SST k–ω (refs. 24, 25), Eqs. 2-1 to 2-10, with the
  Fluent constants listed in §2.2.2. No wall treatment or $y^+$ stated.
* **Spray.** Liquid kerosene C₁₂H₂₃, solid-cone injection, Lagrangian
  tracking of a dilute spray without collisions, TAB secondary breakup (no
  primary breakup), initial mean droplet diameter 0.04 mm, Rosin–Rammler
  distribution, non-equilibrium evaporation and a boiling law (Eqs. 3-1 to
  3-9).
* **Chemistry.** Three-step irreversible global mechanism (Table 2) with
  laminar finite-rate closure (Eq. 4-1); no turbulence–chemistry
  interaction stated. The mechanism of the hydrogen case is not stated.
* **Engine geometry** (Fig. 1). Forebody with three compression ramps,
  rectangular inlet, combustor with two struts, two cavities, three
  circumferential embedded rockets, three struts behind the rockets and a
  rear cavity, variable nozzle, far-field domains fore and aft. Grid size,
  grid independence, boundary conditions, trajectory, equivalence ratios
  and rocket flow rates are not stated.
* **Simplified duct** (§3.4, Fig. 8). Length 900 mm; entry 250 mm long,
  54 mm × 29 mm; a 3 mm rearward-facing step with three 3 mm × 3 mm
  injection holes. Inflow total temperature 1850 K, total pressure
  2.4 MPa, Mach 2.3 (Mach-6 combustor conditions); hydrogen at 1 MPa total
  pressure and 300 K; overall equivalence ratio 0.2. Cell count not stated.
* **Validation.** (i) Tsuru et al. (ref. 44) direct skin-friction duct
  (Mach 2.5 vitiated air): measured mean lower-wall shear 1072 Pa ± 5% and
  1060 Pa ± 10% by two approaches; computed 950 Pa, called "acceptable in
  engineering calculations". (ii) The authors' own direct-connect test of
  the RBCC combustor in ramjet mode at Mach 3: normalized axial wall
  pressure agrees "for most part" (Fig. 3); test conditions not given.

# Tests and results

* **Table 1.** Cases 1–16: Mach 1.5 (0°), 1.8 (−4, 0, +4, +8°), 2 (0°),
  3 (−4, 0, +4, +8°), 4 (0°), 5 (0°), 6 (−4, 0, +4, +8°). Rockets on for
  cases 1–10 (Mach ≤ 3), off for 11–16 (Mach ≥ 4). Low speed Mach 1.5–2,
  mid speed Mach 3, high speed Mach 4–6. Inlet designed to start at about
  Mach 1.8; ejector-to-ramjet transition at Mach 3 (also "between 3 Ma and
  4 Ma"); cruise above Mach 6.
* **Table 3** (normalized skin friction; skin friction as % of thrust):

| Angle of attack | Mach 1.8 | Mach 3 | Mach 6 | % Mach 1.8 | % Mach 3 | % Mach 6 |
|---|---|---|---|---|---|---|
| −4° | 2.30 | 5.59 | 7.52 | 10.95 | 12.51 | 45.90 |
| 0° | 2.28 | 6.06 | 9.48 | 12.19 | 12.19 | 40.33 |
| +4° | 2.24 | 6.54 | 10.67 | 10.90 | 12.71 | 39.86 |
| +8° | 2.52 | 6.67 | 11.35 | 22.33 | 12.81 | 48.42 |

* **Fig. 4a** (reader's readings): normalized skin friction about 1.9 at
  Mach 1.5 to about 9.5 at Mach 6; mean wall shear about 70 Pa to about
  310 Pa.
* **Fig. 9a** (reader's readings, combustion case): wall shear near zero
  just behind the step, a peak of about 730 Pa near $x\approx0.4$ m, a
  minimum of about 270 Pa at $x\approx0.57$ m, about 850 Pa at the exit;
  negative wall shear behind the step (recirculation, Fig. 11).

# Notation map

| Wang et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| Ma (flight) | $\mathrm{Ma}_\infty$ | freestream subscript per the registry preamble |
| $\rho$, $u_i$, $p$, $T$ | $\rho$, $\mathbf u$, $p$, $T$ | |
| $Y_s$ | $Y_k$ | |
| $R_s$ | $\dot\omega_k$ | species production rate |
| ER | $\phi$ | |
| $F_N$ | $F$ | net thrust |
| $F_D$ | words (integrated skin-friction force) | **collision:** registry $D$ is the detonation speed |
| $F_0$ | words | normalizing constant, value not stated |
| $\tau_{ij}$, wall shear stress | words | |
| $k$, $\omega$, $\mu_t$, $Sc_t$ | words | turbulence quantities; **collision:** $k$ also used for rate constants |
| $D$, $D_{s,m}$ | words (diffusion coefficient) | **collision** with registry $D$ |
| $A_r$, $\beta_r$, $E_r$ | words, words, $E_a$ | **collision:** registry $E$ is Young's modulus |
| $\eta_F$, $\eta_O$ | words (reaction orders) | **collision** with registry $\eta_c$ |
| $q$ (Fig. 10) | words (wall heat flux) | registry $\dot q$ is volumetric heat release |
| $d_p$ | words (droplet diameter) | |

# Pages created or updated

Chunk 2 (2026-10-14) founded the bundle. This source is cited on:

* [Rocket-based combined-cycle engine](/definitions/rbcc-engine.md)
* [Boundary-layer combustion for skin-friction reduction](/methods/boundary-layer-combustion.md)
* [Global kinetic mechanisms for kerosene](/methods/global-kerosene-mechanisms.md)

# Citations

1. `/home/stefano/papers/mosaic/chemical-airbreathing-propulsion/2018_Crossref_Acta_Astronautica_Wang_Analysis_and_reduction_of_skin-friction_in_a_rocket-based_co.pdf`.
   * **Version.** Published Elsevier typeset version, 11 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.028, printed on page 1
     and checked on Crossref (2026-10-14): Acta Astronaut. 151, pp.
     357–367, issued 2018-10 (print); Crossref returns no online date;
     page 1 gives received 29 May 2018, accepted 10 June 2018, available
     online 15 June 2018. Page 1 matches the filename. The file was
     collected in the plasma-propulsion archive; the paper is an RBCC
     skin-friction study.
   * **How it was read.** Full text layer plus rendered pages 3–8 for
     equations, tables and figures. Plot values are the reader's
     approximate readings. Eq. 1-10 was read but not reproduced; the SST
     blending functions are only referenced.
   * **Recorded as printed.**
     * Abstract: 57.7% reduction; §3.4 and Conclusions: 57.5%, which the
       printed shear stresses give ((1234 − 525)/1234 = 57.46%).
     * Conclusions: "total drag can be reduced by 57.5%"; the computed
       quantity is the mean upper-wall shear stress in the simplified duct.
     * §3.2 cites "Fig. 3(b)" for the 40.3% value; Fig. 3 is the pressure
       validation and the value is in Fig. 4b.
     * §3.3: Mach-6 wall shear "several orders of magnitude higher" than
       at Mach 1.8; Fig. 6 maxima are about 300 Pa and about 2000 Pa.
     * §3.2 and Conclusions: "almost 4 times"; Fig. 4a gives about 5× for
       the normalized skin friction and about 4.4× for the mean wall shear
       (plot readings).
     * Fig. 8 shows heights 54 mm (entry) and 60 mm (downstream), a 6 mm
       difference, against the 3 mm step of the text.
     * Mode transition at "3 Ma" and "between 3 Ma and 4 Ma" (§3.3).
     * Table 2 caption cites refs. 35, 36 (droplet evaporation) while the
       text cites refs. 38, 39 for the mechanism; "Clark, R.J. [19]" is
       ref. 20 (ref. 19 is Davide/Quadrio); "equations (3)–(8)" means
       Eq. 3-8; the SST blending functions are referred to ref. 30, a
       hybrid-rocket heat-transfer paper.
     * Table 2 pre-exponential units printed as
       "(kmol/m3)^{1−η_F−η_O}/S".
     * Validation: computed 950 Pa against 1060–1072 Pa measured (about
       11% low, outside both stated uncertainties), called "acceptable".
     * Normalizing constant $F_0$ never given; heat-flux sign convention
       not stated.
   * **Reference list.** 45 printed entries (Crossref reference count 45).
     Printed slips flagged by the reader, not corrected: ref. 2 Acta
     Astronaut. 63 dated 2006; ref. 24 "AIAA Paper 1598–1605, 1994"
     (journal pages printed as a paper number); ref. 25 "C.W. David"
     (Wilcox); ref. 27 "AIAA Paper 2890–2906, 2015"; ref. 29 first author
     "D.A. Y"; ref. 33 Acta Astronaut. 20 (2012); ref. 38 garbled authors;
     ref. 41 Acta Astronaut. 114 (2018); ref. 19 "G. Davide" (name order
     apparently inverted). Pudsey 2015 appears twice (refs. 27, 42).
