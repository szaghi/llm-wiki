---
type: Source
title: "Chambers et al. (2022) — Spontaneous runaway of fast turbulent flames for turbulence-induced deflagration-to-detonation transition"
description: "Turbulent-shock-tube experiment (schlieren, high-speed PIV, OH chemiluminescence, pressure) on hydrogen–air flames in shock-generated turbulence: at equivalence ratio 0.89 the turbulent flame speed exceeds the Chapman–Jouguet deflagration speed globally and locally, confirming the runaway criterion of turbulence-induced deflagration-to-detonation transition."
resource: "doi:10.1063/5.0078556"
source_kind: paper
authors: [Chambers J., Chin H.M., Poludnenko A.Y., Gamezo V.N., Ahmed K.A.]
year: 2022
venue: "Phys. Fluids 34:015114"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Chambers_Spontaneous_runaway_of_fast_turbulent_flames_for_turbulence-.pdf"
tags: [combustion, detonation, experiment, compressible]
timestamp: 2026-10-27T20:37:00Z
---

# Summary

Chambers et al. (2022) test experimentally the runaway criterion of
turbulence-induced deflagration-to-detonation transition (tDDT), proposed by
Poludnenko and co-workers from
[DNS](/definitions/direct-numerical-simulation.md) of premixed flames in
spectrally forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md):
a turbulent flame whose speed $S_T$ relative to the reactants immediately
ahead exceeds the Chapman–Jouguet (CJ) deflagration speed
$S_{\mathrm{CJ}}=c_{s,p}/\alpha_\rho$ cannot stay a steady deflagration; it
builds a compressed region and shocks ahead of itself and accelerates,
without confinement or obstacles. The turbulent shock tube is a 1.5 m
semi-confined $45\times45$ mm² channel filled with hydrogen–air (equivalence
ratio 0.78–1.1), ignited at the closed end; six perforated plates accelerate
the flame and produce a leading shock (Mach 2–3) whose passage through the
last plate forms choked jets and intense, nominally isotropic turbulence in
the optical test section. This turbulence comes from post-shock jets, a
mechanism other than the shock–fluctuation interaction of
[shock-generated turbulence](/results/shock-generated-turbulence.md).
Schlieren (100 kHz), high-speed PIV (20 kHz), OH chemiluminescence (40 kHz)
and pressure transducers (250 kHz) run simultaneously.

The equivalence ratio separates four regimes (slow and fast deflagration,
shock–flame complex, detonation). In the runaway case (0.89) the flame moves
at 763 m/s in the laboratory into compressed reactants moving at 377 m/s,
giving $S_T=386\pm11$ m/s above $S_{\mathrm{CJ}}=292.4$ m/s for the compressed
state: the flame is "super-CJ", which the authors call a direct confirmation
of the tDDT criterion. Local values from 128 PIV rows (250–650 m/s, mean
420 m/s) all exceed $S_{\mathrm{CJ}}$; the local turbulent Mach number spans
0.1–0.44, and the flame sits in the thin-reaction-zone regime with
$u'\approx17S_L$, inside the DNS runaway range. The authors also report
vorticity rising across the flame (flame-generated turbulence) and a
stagnation-pressure rise ahead of the flame before any detonation. The paper
contains no model or simulation of its own.

# Version read

Version of record (Phys. Fluids 34:015114, AIP, CC BY; submitted 13 November
2021, accepted 23 December 2021, online 13 January 2022), 13 PDF pages (an AIP
download cover and article pages 015114-1 to -12), all read. Page-1 title,
five authors and DOI match the metadata. No identity problem. Numbering on
this page is that of this version.

# Key claims

$S_T$, $S_f$, $U_f$, $S_L$, $S_{\mathrm{CJ}}$, $D_{\mathrm{CJ}}$,
$c_{s,f}$, $c_{s,p}$ and $\alpha_\rho=\rho_f/\rho_p$ are page-local (see the
Notation map); $u'$ is the r.m.s. of a single PIV field after subtracting a
local window mean (spatial, not Reynolds, statistics).

1. DDT has three stages: preconditioning, initiation (a shock strong enough to ignite the reactants directly, giving an overdriven detonation), relaxation to a freely propagating detonation; the first is highly system-dependent, the second more universal (§I). **Stated**
2. tDDT mechanism (Refs. 12, 29, 30): when $S_T$ reaches $S_{\mathrm{CJ}}=c_s/\alpha_\rho$, the flame generates shocks that grow quickly; the compression accelerates burning, which amplifies the shocks (§I). **Stated**
3. The runaway depends only on flame–turbulence interaction, not on kinetics or flame structure, needs no confinement, is independent of the origin of the turbulence, and appears in chemical and thermonuclear flames (§I). **Stated**
4. The CJ deflagration is the fastest steady deflagration allowed by the conservation laws; for $S_T>S_{\mathrm{CJ}}$ the flow must develop a leading shock, ending in a pulsating regime or a CJ detonation (§I). **Stated**
5. Four regimes by laboratory flame speed $S_f$: slow quasi-isobaric deflagration, fast compressible deflagration, shock–flame complex and detonation, bounded by the reactant and product sound speeds and $D_{\mathrm{CJ}}$ of the quiescent mixture at 300 K and 1 atm (§III A, Fig. 4). **Shown**
6. Deflagrations faster than the reactant sound speed form a secondary shock between flame and leading shock; at the product sound speed it merges with the leading shock and the complex propagates supersonically while the flame speed relative to the compressed reactants stays subsonic; the detonation forms overdriven and relaxes to $D_{\mathrm{CJ}}$ (§III A, Fig. 4). **Shown**
7. Necessary condition for tDDT: flame speed exceeding the CJ deflagration speed, with a sonic plane and choked flow in the products; sufficient condition (Ref. 12): a flame-brush burn-out time long enough for the shocks to reach detonation strength (§III A). **Stated**
8. At equivalence ratio 0.89 the flame enters the test section at 760 m/s with a broad compressed region ahead, and successive schlieren frames show growing pressure waves and a quickly accelerating flame (§III A, Figs. 5–6). **Shown**
9. The leading shock moves at Mach 2.2; ahead of the flame the streamwise velocity reaches 450 m/s with transverse fluctuations $\pm80$ m/s and vorticity $\pm80\,000$ s⁻¹ (§III B, Fig. 7). **Shown**
10. Vorticity increases from the compressed region into the products (flame-generated turbulence), and the post-shock turbulence alone no longer sustains the burning (§III B, Fig. 7d). **Shown** (one run)
11. Centreline: behind the leading shock 330 m/s, 4.9 atm, 550 K; in the post-shock region 2.96 atm and 200 m/s; in the compressed region 400 m/s and 6.1 atm (§III B, Fig. 8). **Shown**
12. The simultaneous velocity and pressure rise ahead of the flame is a stagnation-pressure rise (pressure gain) from a turbulent deflagration before detonation, "not demonstrated previously in other experimental studies of turbulent combustion" (§III B). **Shown**/**Stated**
13. Compressed state (Table I): $P_f=6.1$ atm, $T_f=627$ K, $c_{s,f}=575.1$ m/s, $c_{s,p}=999.7$ m/s, $S_L=4.68$ m/s, $S_{\mathrm{CJ}}=292.4$ m/s, $S_T=385$ m/s (computed with CEA and CHEMKIN from the measurements). **Shown**
14. Global test: $S_f=763\pm3$ m/s, $U_f=377\pm4.9$ m/s, $S_T=S_f-U_f=386\pm11$ m/s $>S_{\mathrm{CJ}}$; "This directly confirms the criterion and mechanism of tDDT described in Refs. 12, 29, and 30" (§III C, Eqs. 1–2, Fig. 9). **Shown**
15. The DNS (Refs. 29, 30; volumetric spectral forcing, Ref. 41) gave $S_T=356$ m/s against $S_{\mathrm{CJ}}=194$ m/s in quiescent uncompressed reactants; the shock-preconditioned reactants here raise $S_L$ and $S_{\mathrm{CJ}}$; both show a compressed region ahead of the flame (§III C). **Stated** (DNS values) / **Shown** (experiment)
16. In these regimes $S_T$ is set mainly by the turbulent velocities, two orders of magnitude above $S_L$ (§III C). **Stated**
17. Local $S_T$ from 128 PIV rows ranges 250–650 m/s with mean 420 m/s, "which differs by 9.1% from the global value given in Table I" (§III D, Fig. 10a). **Shown**
18. Probability densities of $u'$ and $v'$ behind the leading shock confirm isotropy; local flame speeds lie within the integral scales ($L_{11}/l_f=100$) (§III D, Figs. 10b, 11). **Shown**
19. The local turbulent Mach number $M_t=u'/c_{s,f}$ ranges 0.1–0.44; local $S_T$ exceeds $u'$ and $S_{\mathrm{CJ}}$ everywhere in the flame brush, so the flame is super-CJ locally as well as globally (§III D, Fig. 12). **Shown**
20. The regime is the thin reaction zone of the Borghi–Peters diagram with mean $u'\approx17S_L$ (uncertainty 5.5% on $u'$, 13% on the integral scale) (§III D, Fig. 13). **Shown**
21. In the DNS, runaway occurred for $u'=12.5$–$24S_L$ and detonation at $u'=39.2S_L$, also in the thin-reaction-zone regime (§III D). **Stated**
22. The runaway onset condition is $S_T>S_{\mathrm{CJ}}$, independent of how the turbulence is generated and without confinement or obstructions (§IV). **Shown** (one equivalence ratio) / **Stated**
23. PIV measurement scale 168 µm, half the laminar flame thickness (320 µm), and 20–100 times a Kolmogorov scale estimated from the Peters correlation (§II D). **Stated**

# Printed slips

- **$S_T$:** "386 $\pm$ 11 m/s" (§III C) against 385 m/s in Table I. *(compiler check, not in the sources)* $763-377=386$; Table I's $M_T=0.671$ fits 386 ($386/575.1=0.671$; $385/575.1=0.669$), while the "9.1%" of §III D fits 385 ($420/385=1.091$; $420/386=1.088$).
- **Uncertainty of $S_T$:** *(compiler check, not in the sources)* the printed $\pm11$ m/s follows from $\pm3$ and $\pm4.9$ m/s neither by linear sum (7.9) nor by root sum of squares (5.7).
- **PIV uncertainty (§II D):** "<5 m/s ($\pm0.026\,S_T/S_{CJ}$)". *(compiler check, not in the sources)* $5/292.4=0.017$; 0.026 corresponds to $S_{CJ}\approx192$ m/s.
- **CJ speed:** printed $S_{CJ}=c_s/\alpha$ (§I), $c_{s,p0}/\alpha$ (§II E) and $c_{s,p}/\alpha$ (Eq. 1); *(compiler check, not in the sources)* Table I's 292.4 m/s follows from the compressed-state $c_{s,p}=999.7$ m/s and $\alpha=2.873/0.8402$.
- **Eq. (1):** "$c_{s,p}=(\partial P/\partial\rho)_s$ is the sound speed", printed without square root; *(compiler check, not in the sources)* the printed quantity has units of a velocity squared.
- **Local-mean window** for $u'$: "$4\times4$ grid-domain" (§II E) against "$5\times5$ grid domain" (§III D).
- **$M_T$:** the turbulent Mach number $u'/c_{s,f}$ in §III D, but the Mach number of the turbulent flame speed ($0.671=S_T/c_{s,f}$, which §III D calls $M_f$) in Table I.

# Notation map

| Chambers et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $S_T$, $S_f$, $U_f$ | (turbulent flame speed $S_f-U_f$, laboratory flame speed, velocity of the reactants just ahead) | page-local; the source's "flame displacement speed" is the laboratory-frame speed |
| $S_L$, $S_{CJ}$, $D_{CJ}$ | (laminar flame speed, CJ deflagration speed, CJ detonation speed) | page-local |
| $c_{s,f}$, $c_{s,p}$ ($c_{s,f0}$, $c_{s,p0}$) | (reactant and product sound speeds, compressed and quiescent states) | page-local |
| $\alpha=\rho_f/\rho_p$ | $\alpha_\rho$ | page-local density ratio; **collision** with the DG blending factor $\alpha$ |
| $\phi$ | (equivalence ratio) | page-local |
| $u'$, $v'$ | (r.m.s. of one PIV field about a local window mean) | spatial statistics, not $\langle\cdot\rangle$ fluctuations |
| $M_T=u'/c_{s,f}$ | $M_t$ | turbulent Mach number; **collision** inside the source (Table I) |
| $M_f$, $M_L$, $M_{CJ}$ | (flame-speed Mach numbers) | page-local |
| $l$, $L_{11}$, $l_f$ | $L$, (laminar flame thickness) | integral scale |
| $\lambda_m$, $\lambda_k$ | (PIV measurement scale), $\eta$ | **collision**: $\lambda$ is the Taylor microscale in the registry |

# Reference list

44 printed references, numbered (AIP style, order of first citation). The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. 11 is a corporate web item and Ref. 39 a NASA
corporate entry; Ref. 12 prints the issue number 6465 in the page slot.
Same-author same-year works take suffixes in printed order (Khokhlov 1999,
Poludnenko 2011). No printed duplicate, no unparseable item.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
