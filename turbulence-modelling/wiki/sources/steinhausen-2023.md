---
type: Source
title: "Steinhausen et al. (2023) — Flame-vortex interaction during turbulent side-wall quenching and its implications for flamelet manifolds"
description: "A fully resolved detailed-chemistry simulation of a methane-air V-flame quenching at the wall of a turbulent channel verifies that near-wall vortices recirculate cold exhaust gas into the fresh mixture, and an extended quenching flamelet manifold with an exhaust-gas-recirculation dimension removes the tabulation errors this causes, tested a priori."
resource: "doi:10.1016/j.proci.2022.09.026"
source_kind: paper
authors: [Steinhausen M., Zirwes T., Ferraro F., Scholtissek A., Bockhorn H., Hasse C.]
year: 2023
venue: "Proc. Combust. Inst. 39:2149-2158"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Proceedings_of_the_Combustion_Institute_Steinhausen_Flame-vortex_interaction_during_turbulent_side-wall_quenchin.pdf"
tags: [combustion, tabulated-chemistry, flame-wall-interaction, dns, a-priori-a-posteriori, boundary-layer]
timestamp: 2026-10-26T10:27:00Z
---

# Summary

Steinhausen et al. (2023) study flame–wall interaction in turbulent
combustion. A premixed stoichiometric methane–air V-flame, anchored in a
fully developed [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
(bulk velocity 4.4 m/s, $Re_b=U_b\delta/\nu\approx2770$ on the half-width,
wall and inflow at 300 K), quenches at the cold side wall. The authors call
the computation a "fully resolved simulation with detailed chemistry": a
reduced 24-species, 165-reaction mechanism with unit Lewis number, 200
million cells with a first-cell height of $\Delta y^+=0.14$, an in-house
OpenFOAM-based solver of fourth order in space and second order (implicit) in
time, previously validated for "DNS-like" simulations (§2.1; see
[direct numerical simulation](/definitions/direct-numerical-simulation.md)). The inflow comes from a separate periodic
non-reactive channel ([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).

The simulation verifies numerically the flame–vortex interaction mechanism
proposed from experiments by Zentgraf et al.: near-wall vortices carry cold
burnt gas into the fresh mixture between the flame branch and the wall near
the quenching point, then push the flame onto the wall in a head-on-quenching
event, and the cycle repeats. The mixed states lie below the lowest CO mass
fraction (at given CO$_2$) of the laminar side-wall-quenching flame, so laminar
flamelets cannot represent them; more than 80% of lateral locations show such
an event over 5 ms.

The authors then extend the quenching flamelet-generated manifold of Efimov
et al. with an exhaust-gas-recirculation dimension (QFM-EGR): 63 transient
one-dimensional head-on-quenching flames with recirculated-gas mass fraction
0 to 0.3, plus preheated flames from 300 to 750 K, tabulated in
$(c,c_2,h_{\mathrm{norm}})$
([flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)).
In an [a priori test](/definitions/a-priori-and-a-posteriori-testing.md) the
two-dimensional manifold without recirculation errs by up to 70% inside the
interaction region, while QFM-EGR agrees with the reference everywhere. The
coupled LES test is left to future work.

# Version read

arXiv preprint arXiv:2212.03762v1 [physics.flu-dyn], 7 December 2022, 12
pages (10 of text, 2 of references), all read; pp. 1–3 and 8–10 also read as
images to check Eqs. 3–9 and the Fig. 7 schematic. The metadata above are
those of the published article (Proc. Combust. Inst. 39:2149–2158); the DOI
is not printed on the preprint. Page 1 title and authors match the published
record. Figure and equation numbers on this page are those of the arXiv file;
the supplementary videos are not part of it.

# Key claims

Coordinates translated to the registry: the source's wall-normal $z$ is $y$
here, its lateral $y$ is $z$.

1. In the turbulent side-wall quenching, the minimum of $Y_{\mathrm{CO}}$ at given $Y_{\mathrm{CO_2}}$ is lower than in the laminar case, "showing values comparable to the unburnt and burnt gas state over the whole range of $Y_{CO2}$"; in the $T$–$Y_{\mathrm{CO_2}}$ plane the turbulent states are covered by the laminar ones, and in $T$–$Y_{\mathrm{CO}}$ only at low temperature does the turbulent case show higher $Y_{\mathrm{CO}}$ (§3, Fig. 2). **Shown**
2. In the laminar side-wall quenching, the conditional maximum of $Y_{\mathrm{CO}}$ at given $Y_{\mathrm{CO_2}}$ equals the freely propagating flame's value and the conditional minimum equals the wall value (§3, Eqs. 1–2). **Shown**
3. The flame–vortex interaction mechanism of Zentgraf et al. [18] is verified numerically: a vortex downstream of the flame tip is pushed streamwise by the propagating tip, and together with the entrainment of hot exhaust gas at the wall this mixes cold burnt products and fresh gas below the reaction zone, between flame branch and wall ($t=0.55$–$1.1$ ms) (§3, Figs. 3–4). **Shown**
4. The mixing changes the flame-tip velocity and lowers the heat release at the tip ($t=1.65$ ms); the vortex above the front then pushes the flame against the wall, giving a head-on-quenching-like region parallel to the wall ($t=2.2$ ms); the sequence repeats (§3). **Shown**
5. The turbulent side-wall quenching shows both head-on- and side-wall-quenching-like behaviour that strongly affects near-wall CO formation, in accordance with Palulli et al. [17] and Zentgraf et al. [18] (Abstract, §3). **Shown**
6. The interaction "is mainly driven by the interaction of the flame with the near-wall vortical structures. It is not restricted to the equivalence ratio or even fuel" (§3). **Stated** (one stoichiometric methane case; the generalization rests on the comparison with dimethyl-ether experiments [18])
7. At $y/l_{\mathrm F}=0.2$, $t=1.1$ ms, the interaction region covers most of the reaction zone, and it shrinks with wall distance (Figs. 5, 9). **Shown**
8. Counting an event per time step and lateral position when $Y_{\mathrm{CO}}$ at given $Y_{\mathrm{CO_2}}$ falls below the laminar value at more than one streamwise location, over twenty time steps in 5 ms, "more than 80 % of the lateral locations are prone to exhaust gas recirculation" (§3). **Shown**
9. Earlier laminar flame–wall studies showed that one-dimensional flamelets from burner-stabilized flames cannot capture the near-wall flame structure, whereas transient head-on-quenching flames can (§1, citing [11–16]). **Stated**
10. Jiang et al. [6] found good agreement with diluted freely propagating flames and strained opposed-flow flames in the core flow of a three-dimensional DNS of diluted methane–air side-wall quenching, but not near the wall (§1). **Stated**
11. QFM-EGR is built from 63 head-on-quenching flames with recirculation levels 0 to 0.3, each initialized by a freely propagating flame diluted with cold exhaust gas at inflow temperature and quenched at a 300 K wall; preheated flames from 300 to 750 K extend the upper boundary; the ensemble spans a three-dimensional manifold in flamelet coordinate, time and recirculated mass fraction (§4). **Derived** (construction)
12. The diluted flamelets reach lower $Y_{\mathrm{CO}}$ at given $Y_{\mathrm{CO_2}}$ and "can cover the complete thermochemical state of the turbulent SWQ configuration" (§4, Fig. 6). **Shown**
13. The manifold is tabulated in $(c,c_2,h_{\mathrm{norm}})$ at resolution $150\times201\times101$, with $c$ from $Y_{\mathrm{CO_2}}$, $c_2$ from $Y_{\mathrm{CO}}$ conditioned on $c$, and the normalized enthalpy conditioned on both, looked up in that order (§4, Eqs. 3–5). **Derived**
14. A priori (control variables taken from the reference): both manifolds agree well outside the interaction region; inside it the two-dimensional manifold errs "of up to 70 % for all species studied", so the near-wall mixture is inconsistent with its states for all species, not only CO (§5, Fig. 8, $t=1.10$ ms). **Shown**
15. The added dimension $c_2$ accounts for the recirculation-induced mixture shift and gives "very good agreement" with the reference (§5, Fig. 8). **Shown**
16. Mean relative errors (Eq. 7) over the reaction zone $c^*\in[0.3,0.7]$ and twenty time steps: the two-dimensional manifold deteriorates in the interaction region; for $y/l_{\mathrm F}>2$ it is very good with slight deviations in $Y_{\mathrm{CO}}$ and $Y_{\mathrm{H_2O}}$; QFM-EGR shows "excellent agreement" (§5, Fig. 9). **Shown**
17. The near-wall increase of the relative error of $Y_{\mathrm{OH}}$ and of the CO$_2$ reaction rate is not an increase of the absolute error but follows from these quantities tending to zero under strong wall heat losses (§5). **Stated**
18. An a priori test isolates the tabulation error from the errors of the transport equations of the control variables in a coupled (a posteriori) simulation (§5, Fig. 7). **Stated**
19. The solver was previously validated for DNS-like simulations against several DNS reference cases (§2.1, citing [22]). **Stated**
20. Resolution: reactive-mesh wall spacing 12 µm ($\Delta y^+=0.14$), Kolmogorov length $\eta>45$ µm, laminar flame thickness $l_{\mathrm F}\approx0.5$ mm; the flame approaches the wall to 100 µm (§2.1). **Stated**
21. The reactive simulation ran on 32678 CPU cores (as printed) for more than 18 million core-hours (§2.1). **Stated**
22. QFM-EGR "constitutes a significant advance for the modeling of turbulent SWQ"; its evaluation in coupled LES is future work (§6). **Stated**

# Printed slips

- **Page 1:** Ferraro carries the affiliation superscript "A", which matches none of the numbered affiliations 1–3.
- **§2.1:** the laminar flame thickness is printed $\delta_L=(T_{burnt}-T_{unburnt})/|\delta T/\delta x|_{max}$, with $\delta$ for the derivative.
- **Fig. 4 caption:** "The vertical structures are shown in grey", where the text and Fig. 3 speak of vortical structures.
- **Fig. 2 caption:** "colored by wall distance z", whereas the colour bar and the text use $z/\delta_L$ (printed symbols).
- **Eq. 8:** "$z=z$" uses one symbol for the sample coordinate and the fixed wall distance.
- **Eq. 7** *(compiler check, not in the sources)*: $\epsilon_q(z)=\frac1N\sum|q_{i,ref}-q_{i,Manifold}|/\sum|q_{i,ref}|$; the ratio of the two sums is already independent of the sample count, so the extra $1/N$ makes $\epsilon_q$ scale with $1/N$.
- **Ref. [24]:** title printed "Eddies, Steams, and Convergence Zones in Turbulent Flows".

# Notation map

| Steinhausen et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $x$, $z$, $y$ | **source $z$ is wall-normal and $y$ lateral**; translated |
| $y^+$ (first cell) | $\Delta y^+$ | first-cell height in wall units |
| $H$ | $\delta$ | channel half-width, 10 mm |
| $Re=U_{bulk}H/\nu$ | $Re_b$ | on the bulk velocity and the half-width |
| $\eta$ | $\eta$ | Kolmogorov length; agrees |
| $\delta_L$ | $l_{\mathrm F}$ (page-local) | laminar (thermal) flame thickness, as on [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md); **collision:** $\delta$ is the boundary-layer thickness |
| $\Phi$, Le | (equivalence ratio, Lewis number) | |
| $Y_k$, $Y_c=Y_{CO2}$, $Y_{c,2}=Y_{CO}$ | $Y_k$, $Y_c$, $Y_{c,2}$ (page-local) | species mass fraction, progress variables |
| $c$, $c_2$, $h_{norm}$, $c^*$ | page-local | normalized progress variables (Eqs. 3–4), normalized enthalpy (Eq. 5), enthalpy-conditioned progress variable (Eq. 9) |
| $h$ | $h_t$ (page-local) | **collision:** total enthalpy, not the element size |
| $(Y_{CO}\vert Y_{CO2})$ | (value of $Y_{\mathrm{CO}}$ at given $Y_{\mathrm{CO_2}}$) | a conditional value, not an expectation |
| $\dot\omega_{CO2}$ | (reaction rate) | **collision:** not the vorticity or specific dissipation |
| $Y_{EGR}$ | (mass fraction of recirculated cold burnt gas) | 0 to 0.3 |
| $Q$ | (Q-criterion) | |
| $\epsilon_q$, $\Delta q$, $\Omega(z)$, $N$ | (mean and signed relative errors, sample set, sample count) | **collisions:** $\Omega$ (rotation rate), $N$ (polynomial degree) |
| $\psi_{ref}$ | (reference thermochemical state) | |

# Reference list

24 printed references, numbered ([1]–[24]), DOIs printed for most. The list
is merged complete into the [bibliography](/bibliography.md) with `citedby`
steinhausen-2023. Zirwes et al. 2018 [22] and [23] take suffixes in printed
order; [21] (Ranzi et al.) prints no venue and is a miscellaneous entry;
[18] prints no volume. No cited work is an ingested source. No printed
duplicates or unparseable items.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunk 6. This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [OpenFOAM](/software/openfoam.md)
