---
type: Source
title: "Baldan & Guardone (2025) — Wall-resolved large eddy simulations of a pitching airfoil in deep dynamic stall"
description: "Wall-resolved WALE LES of a sinusoidally pitching NACA 0012 in deep dynamic stall with spanwise extents of 0.2 to 1.2 chords: a span of at least one chord is needed in the downstroke, and LES, SST-intermittency URANS and SBES share the same offset from experiment."
resource: "doi:10.1063/5.0252828"
source_kind: paper
authors: [Baldan G., Guardone A.]
year: 2025
venue: "Phys. Fluids 37:024112"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Physics_of_Fluids_Baldan_Wall-resolved_large_eddy_simulations_of_a_pitching_airfoil_i.pdf"
tags: [les, airfoil, dynamic-stall, transition, hybrid-rans-les, sgs-model]
timestamp: 2026-10-26T15:50:00Z
---

# Summary

Baldan & Guardone (2025) reproduce the Lee & Gerontakos (2004) experiment, a
[NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md) pitching sinusoidally
between $-5°$ and $25°$ (reduced frequency 0.1, $Re_c=1.35\times10^5$,
14 m/s) into deep dynamic stall. They use wall-resolved
[LES](/definitions/large-eddy-simulation.md) with the
[WALE model](/methods/wale-model.md) in ANSYS Fluent 2023R2: incompressible
second-order upwind finite volumes, SIMPLEC coupling and bounded second-order
implicit time stepping on a rigidly rotating O-grid. The study has two
aims.

The first is the spanwise extent of the periodic domain. Four extrusions,
$L_z/c=0.2$, 0.4, 0.8, 1.2, are run at the same spacing $\Delta z=10^{-3}c$,
from 62.7M to 374.7M nodes, meeting wall-resolved
[grid criteria](/results/les-grid-point-requirements.md). The upstroke, with
attached flow and a [laminar separation bubble](/definitions/laminar-separation-bubble.md),
is insensitive to span: the largest $C_L$ difference is 0.05 up to about
$22°$. Once the bubble bursts and the dynamic-stall vortex forms, the two
short spans force a nearly two-dimensional vortex. This gives spurious
downstroke lift peaks, up to 0.5 above the upstroke $C_L$. The longer spans
develop three-dimensional structures and follow the measured downstroke with
an offset of about 0.25 in $C_L$. The authors conclude that the span must be
at least one chord. The 0.05–0.2 chord spans common in the LES literature are
acceptable only for attached-flow, ramp-up motions.

The second aim is a comparison of the 1.2-chord LES with the authors' earlier
2D URANS, which couples the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
with a $\gamma$ [intermittency transport model](/methods/local-correlation-based-transition-model.md),
and with their 3D stress-blended eddy simulation, a
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) method. The three agree
within 0.1 in $C_L$ in attached flow and all place peak lift at $22°$,
against $24°$ in the experiment. They diverge in the early stalled
downstroke, and a 0.2 $C_L$ offset from experiment persists. The authors
infer that the discrepancies attributed to the turbulence model "as commonly
reported" ([model-form uncertainty](/definitions/model-form-uncertainty.md))
come from other factors, such as wind-tunnel effects and surface roughness.
They cite the [DES](/methods/detached-eddy-simulation.md) best practice of
Shur et al. (1999), a span of at least one chord. Only one pitching cycle is computed.

# Version read

arXiv preprint 2405.12036v2 (15 January 2025), not the typeset version of
record; 14 pages, all read (figures not read for values). The arXiv title is
"Wall-resolved large eddy simulations of a pitching airfoil incurring in deep
dynamic stall", where the published title drops "incurring in"; same work,
same authors. Every page from page 2 carries the running header "A deep
neural network physics-based reduced order model for dynamic stall", left
over from another manuscript. The introduction is unnumbered; sections are 1
(numerical setup), 2 (results), 3 (conclusions).

# Key claims

1. A span-to-chord ratio of at least one is required to capture the dynamic-stall vortex physics in the downstroke of deep dynamic stall (Abstract, §2.1, §3). **Shown**
2. Span has no effect on loads or structures during the attached upstroke: from $-5°$ to about $22°$ the largest $C_L$ difference among the four spans is 0.05 (§2.1, Figs. 3–4). **Shown**
3. The $0.2c$ and $0.4c$ spans diverge from the larger ones when the separation bubble detaches and induces the dynamic-stall vortex at about $22°$; their first downstroke lift peak is higher (§2.1, Fig. 3). **Shown**
4. Lower in the downstroke, the trailing-edge-vortex–dynamic-stall-vortex interaction on the short spans gives a lift peak 0.5 above the upstroke $C_L$, and 0.3 above in $C_D$ (§2.1, Fig. 3). **Shown**
5. The larger spans follow the measured downstroke trend with a $C_L$ offset of about 0.25 (§2.1, Fig. 3). **Shown**
6. For $L_z/c=0.2$ and 0.4 the periodic conditions enforce a mainly two-dimensional flow at maximum incidence, with a more defined vortex core and higher peak velocity; larger spans show smaller turbulent structures from spanwise interactions (§2.1, Fig. 4). **Shown**
7. At $10°$ in the downstroke, $L_z=1.2c$ is fully stalled while $L_z=0.8c$ still shows oscillatory wake patterns (§2.1, Fig. 4). **Shown**
8. Negative-$C_f$ regions agree across spans in the upstroke; the largest differences are at maximum incidence and at $20°$ and $10°$ in the downstroke; at $22°$ the $C_f$ trends are very similar for all spans (§2.1, Fig. 5). **Shown**
9. Span-averaged space–time maps: transition starts at the trailing edge around $2°$ and moves towards the bubble by $10°$; the vortex develops beyond $15°$ and reaches the trailing edge at $22°$, interacting with the trailing-edge vortex; short spans show two trailing-edge $C_p$ peaks plus a weaker third and a vortex shed from mid-chord, long spans one lower peak, a weaker second, then full stall (§2.1, Fig. 6). **Shown**
10. The wall-resolved criteria $\Delta x^+<40$, $\Delta y^+<5$, $\Delta z^+<20$ (Piomelli & Balaras 2002; Georgiadis et al. 2010) hold on all grids, including the instant at which the near-wall velocity exceeds twice the free stream; at $25°$ on the 1.2c grid $\Delta y^+$ is close to 1, finer than LES needs, to suit the RANS initialization (§1.1, §2.1, Fig. 7). **Shown**
11. WALE gives the right near-wall eddy-viscosity behaviour without a damping function, $\mu_t/\mu\sim O(y^{+3})$ at the wall (Chapman & Kuhn 1986) (§1.2). **Stated** (no formula or constant printed)
12. The cycle is discretized in 144 000 steps, $\Delta t=2.337\times10^{-6}$ s or $2.181\times10^{-4}$ convective times, keeping the CFL number close to one (§1.2). **Stated**
13. Q-criterion views (1.2c): hairpin structures mark transition at $10°$ upstroke; the vortex near $20°$ is mainly two-dimensional; at maximum incidence the flow is fully three-dimensional; it stays stalled and three-dimensional at $20°$ and $10°$ downstroke and relaminarizes near $0°$ (§2.1, Fig. 8). **Shown**
14. The downstroke, not simulated in ramp-up studies, is critical for dynamic stall and is where span matters most (§2.1, §3). **Shown** (span sensitivity) / **Stated** (literature)
15. LES, SST-intermittency URANS and SBES agree in attached flow within 0.1 in $C_L$ (§2.2, Fig. 9). **Shown**
16. Peak lift is at $22°$ in all three models against $24°$ in the experiment: all simulations, wall-resolved LES included, anticipate the angle at which the vortex convects downstream (§2.2, Fig. 9). **Shown**
17. In the early stalled downstroke ($24°$–$18°$) the three models diverge somewhat, then converge as incidence falls; a 0.2 $C_L$ offset from experiment persists (§2.2, Fig. 9). **Shown**
18. The key numerical–experimental discrepancies "are not primarily due to turbulence models, as commonly reported", but seem linked to wind-tunnel effects or the unreproduced surface roughness of the model (§3, Introduction). **Stated** (inferred from claims 15–17, not tested)
19. Most URANS and hybrid dynamic-stall studies attribute the discrepancies to the turbulence model (Introduction). **Stated**
20. Much of the LES literature on dynamic stall uses spans of 5–20% of the chord (Introduction). **Stated**
21. DES best practice (Shur et al. 1999) requires a span of at least one chord to reproduce the dynamic-stall vortex, whose size is of chord order in deep stall (McCroskey 1981) (Introduction). **Stated**
22. Cycle-to-cycle variation in the stalled part is not considered because of the LES cost; one cycle is recorded after discarding a quarter cycle (§1.2, §2.2). **Stated**
23. An O-grid is used to avoid the non-physical patterns that highly anisotropic C-grid cells produce near the trailing edge (§1.1). **Stated**

The motion (Eq. 1): $\alpha_a(t)=10°+15°\sin(\omega_{\mathrm p}t)$, with reduced frequency $k_{\mathrm{red}}=\omega_{\mathrm p}c/(2U_\infty)=0.1$, imposed by rigid rotation of the grid at the rate $\dot\alpha_a=\omega_{\mathrm p}\,15°\cos(\omega_{\mathrm p}t)$.

# Printed slips

- Eq. 1 prints "$18.67\,[\mathrm{Hz}]$" for $\omega_{\mathrm p}$. The printed step count and step size give a period of $144\,000\times2.337\times10^{-6}\,\mathrm s=0.3365$ s, a frequency of 2.97 Hz, and $2\pi\times2.97=18.67$: the value is an angular frequency in rad/s *(compiler check, not in the sources)*.
- Table 1 prints 311 622 quadrilaterals with $N_\xi=934$, $N_\eta=334$ nodes; $933\times334=311\,622$, while the hexahedra of Table 2 (62.1M for 200 layers, up to 372.8M) correspond to $933\times333=310\,689$ quadrilaterals per layer *(compiler check, not in the sources)*.
- Spans quoted as "from only 5% to 20% of the chord size" (Introduction, while citing 0.02c, 0.25c and 0.5c cases) and as "from 0.1 up to 0.2" (Conclusions).
- $C_L$ offset "≈ 0.25" (§2.1) and "equal to 0.2" (§2.2), in different contexts, not reconciled.
- Introduction, phase (b): transition "initiating at the trailing edge and progressing downstream"; §2.1 has it progress "towards the LSB", that is upstream.
- Running header of pages 2–14 carries another paper's title.
- Typos: "mean angle of attach" (§1), "dumping function" (§1.2), "are can be accepted" (§3), "in its entirely" (§2.1).
- Reference "Marilyn J. et al., 2020": given and family names transposed in the author list ("S. Marilyn J., … P. David"), inherited by the in-text citation.
- Baldan & Guardone (2024b) printed with year 2024 and the DOI 10.1007/s00707-025-04232-w; Menter et al. (2004) printed without volume.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha$, $\alpha_0$, $\alpha_s$ | $\alpha_a$ (angle of attack, page-local), mean $10°$, amplitude $15°$ | **collision:** $\alpha$ is the DG/FV blending factor in the registry |
| $\omega$ | $\omega_{\mathrm p}$ (pitching angular frequency, page-local) | **collision** with the specific dissipation rate $\omega$; printed in "Hz" (Printed slips) |
| $k$ | $k_{\mathrm{red}}=\omega_{\mathrm p}c/(2U_\infty)$ (page-local) | **collision:** not the turbulent kinetic energy |
| $Re$ | $Re_c$ | chord-based |
| $V_\infty$, $P_\infty$ | $U_\infty$, (reference pressure) | |
| $c$, $L_z$ | (chord), (span of the periodic domain) | the chord length is not printed |
| $\xi$, $\eta$, $z$ | $x$ (along the profile), $y$ (wall-normal), $z$ | **collision:** $\xi$ is the reference coordinate and $\eta$ the Kolmogorov length in the registry |
| $\xi^+$, $\eta^+$, $z^+$ | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ | grid spacings in wall units |
| $y^+$ | $y^+$ | |
| $\mu_{SGS}$, $\mu$ | $\mu_t$, $\mu$ | |
| $C_L$, $C_D$, $C_p$, $C_f$ | $C_L$, $C_D$, $C_p$, $C_f$ | $C_f$ signed: positive along the leading-to-trailing-edge direction |
| $\gamma$ | $\gamma$ (intermittency) | transition pages only |
| iSST | SST with $\gamma$ intermittency transport | authors' label |
| DSV, TEV, LSB | dynamic-stall vortex, trailing-edge vortex, laminar separation bubble | |
| span-averaged | average over $z$ of an instantaneous field | not a phase or Reynolds average |

# Reference list

51 printed references, author–year style, ordered by first citation. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Same-author same-year works take suffixes in printed
order (Baldan et al. 2024 and Baldan & Guardone 2024a/b; Zanotti 2014a/b;
Benton & Visbal 2019a/b; Visbal 2018; Lee 2024). The "Marilyn J. et al.
(2020)" entry prints a garbled author list; the merge identified it on Crossref
as Smith et al. (2020, VFS 76th Forum) and keys it `smith-2020`, noting the printed form;
Spalart et al. (1997) has no venue; Kasibhotla & Tafti (2014) a paper number
only; Baldan & Guardone (2023) the venue "Aeronautics and Astronautics" only.
No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-26), cited further in chunks 8, 12. This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Dynamic stall](/definitions/dynamic-stall.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [WALE model](/methods/wale-model.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [ANSYS Fluent](/software/ansys-fluent.md)
