---
type: Source
title: "Sabnis & Babinsky (2023) — A review of three-dimensional shock wave–boundary-layer interactions"
description: "Review of the physics of turbulent, steady, three-dimensional shock wave–boundary-layer interactions below Mach 5: canonical swept and fin geometries, cylindrical and conical symmetry, regimes by surface topology, and the sidewall corner-wave mechanism in rectangular ducts; turbulence modelling enters only through RANS remarks."
resource: "doi:10.1016/j.paerosci.2023.100953"
source_kind: paper
authors: [Sabnis K., Babinsky H.]
year: 2023
venue: "Prog. Aerosp. Sci. 143:100953"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Progress_in_Aerospace_Sciences_Sabnis_A_review_of_three-dimensional_shock_waveboundary-layer_inter.pdf"
tags: [review, shock-boundary-layer-interaction, compressible, separated-flow, rans]
timestamp: 2026-10-29T10:05:00Z
---

# Summary

Sabnis & Babinsky (2023) review three-dimensional
[shock wave–boundary-layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
(SBLIs), restricted to turbulent, uncontrolled, predominantly steady
interactions in the transonic and supersonic range ($M<5$); hypersonic
interactions are left out, and unsteadiness and control are treated only
briefly. The paper presents no data of its own.

The two-dimensional background (§2) is the feedback loop between upstream
pressure transmission through the subsonic near-wall layer, the displacement
of the [boundary layer](/benchmarks/turbulent-boundary-layer.md) and the
shock, for normal shocks, oblique reflections and compression corners.
Separation onset is governed by the adverse pressure gradient rather than the
incoming shape factor. The three-dimensional part (§3) surveys swept
compression corners, sharp, double, swept and blunt fins, cylinders, swept
reflections, flares and semi-cones. Outside an inception region the
interactions become cylindrically or conically symmetric, and in the plane
normal to the shock (or hinge line) they resemble the two-dimensional
interaction; regimes are classified by the critical-point topology of the
skin-friction lines. Sweep suppresses the low-frequency unsteadiness of the
unswept interaction.

The review's own synthesis (§4) is the sidewall effect in rectangular ducts:
corner separations, made early by low-momentum corner flow, emit compression
and expansion waves that cross the span and change the centre-span adverse
pressure gradient. This explains the facility scatter of normal-shock
separation onset through the viscous aspect ratio $\delta^*/W$, and three
regimes of centre-span separation length for oblique reflections and
compression corners. A strip theory predicts the spanwise variation of
separation. Corner and centre separations are usually not dynamically coupled,
compression corners excepted, and curing corner separation can worsen centre
separation. The concluding remarks attribute RANS failures in such flows to a
mispredicted displacement of the corner separation, and point to RANS that
reproduces the stress-induced corner vortices (the quadratic constitutive
relation is cited; see the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
and [Reynolds-stress models](/methods/reynolds-stress-model.md)). The
[LES](/definitions/large-eddy-simulation.md), [implicit LES](/definitions/implicit-les.md),
[DES](/methods/detached-eddy-simulation.md) and
[DNS](/definitions/direct-numerical-simulation.md) studies of these
interactions are cited by configuration, without method content.

# Version read

Version of record (Elsevier, open access CC BY; received 10 February 2023,
online 24 October 2023), 27 pages, all read, pages 24–27 the reference list.
Page 1 matches Crossref; no identity problem.

# Key claims

1. Separation onset in a turbulent SBLI is almost insensitive to the incoming shape factor: a low shape factor resists separation but also gives a thinner subsonic layer, a shorter interaction and a steeper adverse pressure gradient; onset is governed by shock strength, more precisely the adverse pressure gradient seen by the boundary layer (§2, citing [2], [20]). **Stated**
2. For normal shocks weaker than about $M=1.3$ the boundary layer stays attached, and the smeared pressure rise can extend "up to 70 boundary-layer thicknesses downstream of the inviscid shock location" ([21]); separation is typically seen above shock Mach "roughly 1.30 to 1.35" ([2, 21, 22]) (§2.1). **Stated**
3. In a separated normal-shock interaction the incompressible shape factor $H_i$ rises strongly in the separation and recovers to an equilibrium profile 20–30 incoming boundary-layer thicknesses after reattachment (§2.1, Fig. 4b). **Stated**
4. In an attached oblique reflection the upstream pressure transmission is "typically on the order of a boundary-layer thickness"; in an attached compression corner the pressure rise is smeared over about one $\delta$ ([26]) (§2.2–2.3). **Stated**
5. In compression corners the separation length tends to zero at zero deflection, so a small separation may always exist; onset is then the smallest separation the measurement detects, and five regimes with increasing deflection are distinguished ([19, 27–31]) (§2.3). **Stated**
6. SBLI unsteadiness bands: low frequency $St_\delta<0.01$, mid $0.01<St_\delta<0.1$, high $St_\delta>0.1$, $St_\delta$ based on the incoming boundary-layer thickness ([34]); in two dimensions high frequencies follow the incoming turbulence and low frequencies are driven by separated-region instabilities ([35]) (§3). **Stated**
7. Sweep breaks the dynamic link between separation and reattachment lines: swept-wing normal-shock interactions lose the large-amplitude low-frequency unsteadiness and keep only high-frequency shock rippling ([36, 37]); LES of swept compression corners ([34]) show low-frequency unsteadiness suppressed against the two-dimensional corner (§3, §3.1). **Stated**
8. Swept compression corners fall into regimes A (attached), B (cylindrical symmetry), C (conical symmetry, detached stand-off shock, lines converging to a virtual conical origin) and D (reattachment line moving from ramp to floor) (§3.1, Figs. 6–7; [44–47]). **Stated**
9. Vanstone et al. [51] (PIV, $M=2$) find conical symmetry in the streamwise velocity while the spanwise component reaches its asymptote much farther downstream, and hypothesise that regime B is a conical flow not yet at its far field; "to date, this hypothesis has not been investigated in detail" (§3.1). **Stated**
10. Settles and Dolling [7] state that the plateau-to-incoming pressure ratio of separated swept interactions equals the two-dimensional one at the same Mach number; the authors call this an order-of-magnitude statement because plateaus are smeared (§3.1). **Stated**
11. The unswept sharp-fin interaction is characterised by $M_n=M_\infty\sin\beta_0$; incipient separation occurs at a pressure-rise ratio near 1.5, i.e. $M_n=1.2$, below the two-dimensional critical value 1.3 ([65, 66]), so cross-flow promotes earlier separation in swept flows (§3.2). **Stated**
12. Sharp-fin regimes number five for Korkegi [63] and six for Zheltovodov [57]; the sequence is attached, separated, secondary separation appearing (laminar reversed flow), disappearing (transitional or turbulent reversed flow, supersonic jet) and reappearing (terminating normal shock in the supersonic reversed flow) (§3.2, Figs. 9–10). **Stated**
13. Secondary separation under a sharp fin is set by the adverse pressure gradient on the reversed flow, its laminar or turbulent state, and its acceleration to supersonic speed ([57, 68]) (§3.2). **Stated**
14. Swept fins are conically symmetric for all sweepback angles and follow unswept scaling: as functions of $M_n$, plateau pressures and critical normal Mach numbers for primary and secondary separation coincide with unswept fins; shock curvature lowers the reattachment peak and plateau ([61, 104, 105]) (§3.3, Fig. 12). **Stated**
15. Blunt fins always separate the incoming boundary layer through a strong normal shock, even at small fin angles ([108]); the horseshoe-vortex extent depends only weakly on incoming thickness or Reynolds number (RANS of Hung and Buning [110]) (§3.3). **Stated**
16. Swept compression corner, sharp fin and semi-cone at $M=2.95$ with similar inviscid strength collapse in surface topology and shock-normal pressure ratio (Settles and Kimmel [44], Fig. 17) (§3.4). **Stated**
17. Bruce et al. [135] found normal-shock separation onset scattered from shock Mach 1.29 to 1.59 over many facilities, attributed to rectangular test sections; the viscous aspect ratio $\delta^*/W$ collapses the onset better (Fig. 18) (§4, §4.1). **Stated**
18. Corners are "generally more prone to separation" because they hold low-momentum flow; stress-anisotropy-driven counter-rotating corner vortices ([139]) depend on nozzle history ([140]) and must be captured for a quantitatively correct corner separation ([141, 142]), but they change momentum little, so corners can be treated as low-momentum regions (§4). **Stated**
19. In normal-shock duct flows the corner compression waves (idealized as a weak conical corner shock) merge with the lambda shock near the sidewall, lengthen the interaction, reduce the adverse pressure gradient and delay separation there; larger corner separation gives a more benign centre-span interaction; at $M=1.4$ suction that reduces corner separation causes centre-span separation ([135], Fig. 20) (§4.1). **Stated**
20. In oblique reflections in ducts the corner waves cross the shock system; centre-span separation length against the crossing location of the corner shocks shows regimes A (quasi-two-dimensional), B (corner shocks intersect within the interaction, longer separation) and C (corner shocks intersect ahead, expansion waves shorten it, possibly below regime A) (Xiang and Babinsky [154], $M=2.5$, 8°; Figs. 22–23) (§4.2). **Stated**
21. Lusher and Sandham [165] reproduce the three regimes in laminar $M=2$ computations but attribute the corner waves to the sharp-fin footprint of the shock generator rather than to corner-separation displacement (§4.2). **Stated**
22. The strip theory of Williams and Babinsky [167] (corner-wave pressure profile added, strip by strip, to the overall pressure rise) predicts the spanwise variation of separation length of [154] over most of the span but fails near the sidewalls (§4.2); it also predicts corrugated separation in compression corners with imposed conical shocks ([182]) (§4.3). **Stated**
23. Full-span compression corners in ducts show the same A–B–C sequence (Williams and Babinsky [171], 20° ramp, $M=2.5$, Fig. 24); a highly confined duct ([181]) gives a narrower, shorter central separation than the less confined case of [179] (§4.3). **Stated**
24. Computations with boundary-layer fences give a larger central separation than equivalent spanwise-periodic ones ([176, 177]); fences do not isolate the interaction from sidewall effects (§4.3). **Stated**
25. Corner and central separations are usually not dynamically coupled ([160, 178, 183, 188]), though corners set the low-frequency central unsteadiness through the mean central separation size ([189], [171]); the exception is the compression corner, where asymmetric modes appear to couple them ([180, 186, 187]), and the corner influence extends to 35% of the span ([180]) (§4.4, §5). **Stated**
26. Corner control (suction, micro-vortex generators, fences, chamfers, fillets) reduces corner separation but can aggravate centre-span separation through the corner-wave mechanism ([191], [153]); vortex generators work only when they produce downwash at the corner; control on one wall can worsen the others ([197, 198]); combined corner and centre control performs best ([191, 193]) (§4.5). **Stated**
27. "When RANS simulations are unable to predict interactions with corner effects, it is usually not because the flow is inherently three dimensional but because an accurate simulation of the wider flow field requires the displacement effect of the corner separation to be correctly captured"; current RANS effort aims at reproducing the stress-generated streamwise corner vortices (§5). **Stated**

Disagreements the review records between its cited works: the number of
sharp-fin regimes ([63] against [57]); whether sharp-fin regime C has a true
secondary separation ([58] against [57, 69]); cylindrical regime B ([45])
against the unfinished-conical hypothesis ([51]); whether swept-corner
high-frequency content follows the incoming turbulence (LES [34]) or is
uncorrelated with it (PIV POD [55]), "not been adequately resolved"; and the
origin of the corner waves ([145, 154] against [165]).

# Printed slips

- §3.2, p. 10: "Further RANS simulations at Mach 3 conducted by Yang et al. [84] at Mach 2.95 studied …": two Mach numbers for one study.
- Bisek [179] is "large-eddy simulations of a 24 degree ramp at Mach 2.25" (§4.3, p. 19) and "large-eddy simulations on a 24 degree compression corner at Mach 2.5" (§4.4, p. 20).
- §4.4: "Large-eddy simulations of an oblique shock interaction … performed by Garnier [160]"; the printed title of [160] is "Stimulated detached eddy simulation of three-dimensional shock/boundary layer interaction".
- Deshpande and Poggie [180] are "Experiments on highly-confined compression ramp interactions" (§4.4), and the Fig. 26 caption reads "Unsteady behaviour from experiments of a 24 degree compression corner at Mach 2.25"; §5 states that the compression-corner coupling "has been observed in both high-fidelity computations and in experiment". Both are recorded as printed.
- §1: sidewall mechanisms cause "the onset of ‘‘buzz’’ behaviour which precludes unstart"; §2.1: "enhances the upstream transfer of pressure information upstream".
- Reference typos as printed: [101] "Passive flow cntrol"; [119] "K. Ktamura"; [65] "glancing inter-action".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y$, $u$ | $y$, $\langle u\rangle$ | wall-normal coordinate; the mean is implied, no averaging symbol printed |
| $u_e$ | $u_e$ (edge velocity, page-local) | |
| $\delta$, $\delta^*$ | $\delta$, $\delta^*$ | $\delta^*$ in $\delta^*/W$ not said to be compressible or incompressible |
| $H_i=\delta_i^*/\theta_i$ (Eq. 1) | $H_i$, $\delta_i^*$, $\theta_i$ (incompressible shape factor and thicknesses, page-local) | integrals to $\delta$ with $1-u/u_e$ and $(u/u_e)(1-u/u_e)$ |
| $W$ | $W$ (duct width, page-local) | viscous aspect ratio $\delta^*/W$ |
| $St_\delta$ | $St$ based on $\delta$ | velocity scale not stated |
| $M_\infty$, $M_n=M_\infty\sin\beta_0$ | $M_\infty$, $M_n$ (shock-normal Mach number, page-local) | |
| $\beta_0$ | $\beta_0$ (glancing-shock angle, page-local) | **collision** with $\beta(\boldsymbol x)$ and $\beta^*$ |
| $p$, $p_0$ | $p$, $p_0$ (wall and stagnation pressure, page-local) | Figs. 3–4 plot $p/p_0$ |
| regimes A–D, A–E, A–C | (page-local labels) | the letters are reused for swept corners, sharp fins and duct corner effects |

No turbulence-model, averaging or SGS symbols are printed.

# Reference list

204 printed references, numbered style, no DOIs printed. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Same-author same-year works are keyed in printed order. Refs. [12], [34],
[120], [165] and [183] print no pages or article number, [98] no volume or
pages; [7] is printed as a journal-style item ("Tactical Missile Aero-dyn.
104 (1986) 297–379") and kept as printed. Ref. [11] is a chapter of the
book [4] and is a separate entry. Two printed keys collide with the keys of
ingested sources or other entries for different works (ref. [79], Liu T. et al., Shock Waves
32:665–678, keyed `liu-2022-m`; ref. [13], Wang Z.-Y. et al., AIAA J. 61:37–47, keyed `wang-2023-j`).
All items parsed.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
