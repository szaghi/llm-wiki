---
type: Source
title: "De Vanna et al. (2023) — Effect of convective schemes in wall-resolved and wall-modeled LES of compressible wall turbulence"
description: "Parametric study, in the URANOS solver, of how WENO-Z (orders 3, 5, 7), TENO5, TENO-A5, a sixth-order energy-preserving central scheme and their Ducros-switched hybrids change wall-resolved and wall-modelled LES of Mach 2 and Mach 5.86 turbulent boundary layers; recommends a hybridization threshold of about 0.2."
resource: "doi:10.1016/j.compfluid.2022.105710"
source_kind: paper
authors: [De Vanna F., Baldan G., Picano F., Benini E.]
year: 2023
venue: "Comput. Fluids 250:105710"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_De_Effect_of_convective_schemes_in_wall-resolved_and_wall-model.pdf"
tags: [turbulence, numerical-dissipation, weno, teno, kinetic-energy-preserving]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

A numerical study of how the discretization of the convective terms changes
wall-resolved LES (WRLES) and [wall-modelled LES](/methods/wall-modeled-les.md)
(WMLES) of compressible turbulent boundary layers. All runs use the authors'
finite-difference solver [URANOS](/software/uranos.md) with an equilibrium
wall-stress model that keeps no-slip and isothermal walls and imposes the
modelled stress and heat flux through an effective wall viscosity and
diffusivity. Six convective schemes are compared: a sixth-order fully split
central energy-preserving (EP) scheme of Pirozzoli
([split convective forms](/methods/split-convective-forms.md)),
[WENO-Z](/methods/weno-z.md) of orders 3, 5 and 7 with $\epsilon=10^{-12}$,
[TENO5](/methods/targeted-eno.md) with $C_T=10^{-7}$ and
[TENO-A5](/methods/adaptive-teno.md) with $C_T$ between $10^{-10}$ and
$10^{-7}$. The shock-capturing schemes run everywhere ("pure") or in a
[hybrid](/methods/hybrid-weno.md) with the EP scheme switched by a modified
[Ducros sensor](/definitions/ducros-shock-sensor.md) at thresholds 0.1, 0.2
and 0.4. The 69 cases cover a spatially developing
[supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
at Mach 2 (WRLES at $\mathrm{Re}_\tau=250$; WMLES at $\mathrm{Re}_\tau=900$ on
three grids) and at Mach 5.86 (WMLES, $\mathrm{Re}_\tau=1200$), compared with
DNS.

In WRLES, upwind [numerical dissipation](/definitions/numerical-dissipation.md)
underestimates friction, raises the log layer and the TKE peak, less so at
higher WENO order and with TENO; the EP scheme matches the DNS. In WMLES the
effect is much stronger: pure WENO/TENO, WENO-Z3 above all, fail to sustain
wall turbulence, and hybridization with even the 0.1 threshold restores
realistic statistics. At Mach 5.86 a pure EP run diverges because of
shocklets, and 0.2 is the largest stable threshold; the authors recommend
about 0.2. Hybrid runs cost the same as pure EP or slightly less, pure
WENO/TENO up to 32 % more. The subgrid model matters little provided its
eddy viscosity vanishes at the wall. A momentum-balance argument is offered
for the change in drag.

# Version read

Version of record (Elsevier typeset, Computers and Fluids 250 (2023) 105710),
17 pages, all read; page 1 matches Crossref (title, four authors in this
order, venue, DOI printed). Equation, table and figure numbers on this page
are those of this version.

# Key claims

Registry notation (see the notation map): the source's Ducros sensor
$\theta$ and threshold $\bar\theta$ are written $\Psi_{\mathrm D}$ and
$\Psi^*$ (page-local; $\theta$ is the Zhang–Shu factor in the
registry); its WENO regularization $\varepsilon$ is $\epsilon$.

1. The grid points needed to resolve near-wall eddies scale as $N_{\mathrm{DNS}}\sim\mathrm{Re}^{37/14}$ for DNS and $N_{\mathrm{WR}}\sim\mathrm{Re}^{13/7}$ for WRLES, after Choi and Moin (§1). **Stated**
2. The wall model imposes the modelled wall stress and heat flux through $\mu_{\mathrm{eff}}=\frac{\tau_{w,\mathrm{wm}}}{\tau^{\mathrm{LES}}_w}\mu_w$ and $\lambda_{\mathrm{eff}}=\frac{q_{w,\mathrm{wm}}}{q^{\mathrm{LES}}_w}\lambda_w$, keeping no-slip and isothermal/adiabatic walls, and falls back to WRLES when the wall is resolved (§2.2, Eqs. 6–8, from the authors' earlier work). **Stated**
3. The EP scheme is a sixth-order fully split central scheme preserving total kinetic energy semi-discretely in the incompressible inviscid limit, with "theoretically zero numerical dissipation" in shock-free conditions, but it cannot stably evolve shocks or shocklets (§3.1). **Stated**
4. WENO-Z is used at orders 3, 5 and 7 with $\epsilon=10^{-12}$ "to reduce the dissipation" (§3.1). **Stated**
5. TENO5 uses $C_T=10^{-7}$; TENO-A5 lets $C_T$ range in $[10^{-10},10^{-7}]$ with constants $10.5$, $3.5$, $C_r=0.25$ and $10^{-3}$ taken from Fu et al. (§3.1). **Stated**
6. The modified Ducros sensor $\Psi_{\mathrm D}=\max\big(-\nabla\!\cdot v/\sqrt{(\nabla\!\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}},0\big)$, $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ (Eq. 9), flags an interface when $\Psi_{\mathrm D,i+1/2}>\Psi^*$; WENO/TENO is then used there and in two, three or four neighbouring cells depending on the order, EP elsewhere (§3.2). **Stated**
7. In low-resolution settings such as WMLES, shock detectors read numerical noise, oscillations and physical turbulent fluctuations as shocks, so shock capturing is activated in nominally smooth regions (§3.2, §4.3.3). **Stated**
8. WRLES at Mach 2 ($\Delta x^+\times\Delta y^+_w\times\Delta z^+=29.3\times0.54\times11.7$, implicit LES): WENO-Z3 gives a much shorter $\mathrm{Re}_\tau$ range and an extended transition; agreement with DNS improves with WENO order and with TENO; the EP scheme "perfectly fits" the DNS $c_f$ (§4.2.1, Fig. 1a). **Shown**
9. In WRLES, adding the WALE model changes $c_f$ only marginally (WENO-Z7 and EP), because its eddy viscosity vanishes at the wall and the scale separation is small (§4.2.1–4.2.2, Figs. 1b, 3). **Shown**
10. In WRLES, the shock-capturing schemes underestimate wall friction, overestimate the log-layer velocity and raise the TKE peak at $\mathrm{Re}_\tau=250$; the error shrinks with order and with TENO (§4.2.2, Fig. 2). **Shown**
11. In pure-shock-capturing WMLES at Mach 2, near-wall velocity contours show only wide transitional-like structures with WENO-Z3; streaks improve with order and the EP scheme is the most realistic (§4.3, Fig. 4). **Shown**
12. Coarse WMLES grid ($675\times64\times108$, $\Delta^+=120\times70\times50$): pure WENO/TENO give a very narrow $\mathrm{Re}_\tau$ range, turbulence not developed; the 0.1 hybrid recovers a decreasing $c_f$ over a wider range but not a fully turbulent shape (§4.3.1, Figs. 5a–b). **Shown**
13. Medium grid ($960\times128\times160$): all pure schemes except WENO-Z3 give reasonable $c_f$ but damped turbulence; the 0.1 hybrid aligns WMLES with DNS and with EP, TENO closer to EP than WENO (§4.3.1, Figs. 5c–d). **Shown**
14. Fine grid ($1350\times225\times270$): pure WENO/TENO "dramatically" overestimate wall friction, WENO-Z3 stays far from all others, and the 0.1 hybrid collapses the results near DNS (§4.3.1, Figs. 5e–f). **Shown**
15. No WENO/TENO scheme of any order collapses on the EP solution in WMLES; EP remains the best approximation of DNS in shock-free supersonic WMLES (§4.3.1). **Shown**
16. Wall time per iteration normalized by EP (Table 2): hybrids 0.90–1.00, pure variants 0.95–1.32 (maximum TENO-A5 on the fine grid); hardware TGCC Joliot-Curie KNL partition, 13 nodes of Intel KNL 7250 (§4.3.1). **Shown**
17. At $\mathrm{Re}_\tau=900$ with the 0.1 hybrid: the coarse grid underestimates the log-region velocity and overestimates fluctuations (TENO-A5 and EP best); on the medium grid TENO5/TENO-A5 suit DNS very well; on the fine grid they recover DNS "almost as the EP scheme, at the evident penalty of a roughly doubled computing cost [33,40]" (§4.3.2, Fig. 6). **Shown** (cost **Stated**, cited)
18. Pure schemes on the medium grid: WENO-Z5/Z7 give a bulge-like log region and low fluctuations, while TENO5 approximates DNS "quite accurately" (§4.3.3, Figs. 7a–b). **Shown**
19. With threshold 0.1 even WENO-Z3 reproduces the physics; at 0.2 the order dependence persists without affecting global accuracy; at 0.4 all WENO and TENO profiles collapse, since EP solves most of the flow; hybrids always leave a mild drag reduction and overestimated fluctuations relative to pure EP (§4.3.3, Figs. 7c–d, 8). **Shown**
20. At Mach 5.86 a pure centred scheme, EP included, diverges because of shocklets in the nominally shock-free flow, and 0.2 is "the highest limit that ensures the current arrangement's numerical stability" (§4.4). **Shown** (no figure of the divergence)
21. At Mach 5.86, pure schemes give a bulge-like log region and order-dependent overestimated TKE; 0.1 reduces both; at 0.2 all TENO variants capture the mean velocity precisely, WENO gives a mild drag reduction, and the temperature is nearly scheme-independent (§4.4.1, Fig. 9). **Shown**
22. Recommended threshold $\Psi^*\simeq0.2$, an upper bound for hypersonic regimes; in supersonic shock-free conditions it can range from 0 (pure shock capturing) to 1 (in effect pure EP) (§6). **Stated**
23. In WRLES, upwind numerical viscosity damps the small scales and freezes the Reynolds stress; by momentum conservation the mean wall velocity gradient must change, giving an effective drag reduction seen as a positive log-layer mismatch, analogous to polymer drag reduction (§5, §6). **Derived** (qualitative; see Printed slips)
24. In WMLES the Reynolds stresses reach the wall stress only through the wall model, which knows only the instantaneous velocity and temperature at the exchange point, so with predominant shock capturing or poor resolution turbulence can be wholly destroyed (§5). **Derived** (qualitative)
25. Pure WENO/TENO without hybridization are "ineffective for describing wall dynamics in a WMLES framework"; pure WENO-Z3 mispredicts the wall flow at any resolution (§6). **Shown**
26. Smagorinsky ($C_s=0.12$) deviates because its eddy viscosity does not vanish at the wall; WALE, Sigma and Mixed Time Scale give similar results matching DNS (Appendix, Fig. 10, Table A.5). **Shown**

# Printed slips

- Mach 5.86 resolution: Table 4 and §4.4 print $\Delta x^+=90$ for $N_x=1400$; assuming the $L_x=90\delta_0$ of §4.1 also holds at Mach 5.86 and $\Delta^+$ is taken at the statistics station ($\mathrm{Re}_\tau=1200$), $\Delta x^+=90\times1200/1400=77.1$, and the printed 90 corresponds to $N_x=1200$. The same computation reproduces the other printed spacings of Tables 1–4 (e.g. $768\to29.3$ at $\mathrm{Re}_\tau=250$; $675\to120$, $960\to84.4$, $1350\to60$ at 900). *(compiler check, not in the sources.)*
- Drag wording: §5 says frozen Reynolds stress makes "the average wall velocity gradient … increase with a consequent effect in terms of an effective drag reduction", and §4.3.2 that underestimating the log-region velocity "corresponds to significant drag reduction if observed in inner scaling"; a larger wall velocity gradient is a larger wall stress, and §4.2 reports friction underestimation; with $\tau_w$ proportional to the mean wall velocity gradient, the mechanism as worded has the sign opposite to the reported friction *(compiler check, not in the sources)*.
- §4.3.1: "pure schemes increase the computational time of about 5÷30%", but the coarse-grid pure WENO-Z3/Z5/Z7 values are 0.95, 0.98, 0.99 (Table 2).
- "around seventy" / "seventy different setups" for cases numbered 1–69.
- §4.3.1 "$\theta=0.1$" (bar missing); §4.4.1 "WENO 3" for WENO-Z3; "not worth mentioning" (§4.1) and "not worthless to remind" (§4.3.3) for "worth".
- $\varepsilon$ denotes both the WENO regularization and the sensor regularization; $y^*$ both the semi-local wall distance (§2.2) and $y/\delta$ (§4.2.2).
- The cost "roughly doubled" for TENO against EP (§4.3.2) is attributed to refs. [33,40]; this paper's own Table 2 gives 1.03–1.32 pure and 0.91–0.99 hybrid.

# Notation map

| De Vanna et al. (2023a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\phi$, $\tilde\phi$ | kept | Reynolds and Favre filtering (LES), not cell averages |
| $\tilde u_i$ | $v$ | velocity; **$u$ is the conserved vector in the registry** |
| $\varepsilon$ (§3.1) | $\epsilon$ | WENO regularization $10^{-12}$ |
| $\theta$, $\bar\theta$ | $\Psi_{\mathrm D}$, $\Psi^*$ (page-local on [Ducros shock sensor](/definitions/ducros-shock-sensor.md)) | sensor and threshold; **$\theta$ is the Zhang–Shu factor in the registry** |
| $\varepsilon$ (§3.2) | $\epsilon_{\mathrm D}$ | sensor regularization $(u_\infty/\delta_0)^2$; **same letter as the WENO $\varepsilon$** |
| $C_T$ | $C_T$ | agrees |
| $\alpha_1$, $\alpha_2$, $C_r$, $\xi$ | $b_1$, $b_2$, $C_r$, $\xi_{\mathrm A}$ | TENO-A constants as on [adaptive TENO](/methods/adaptive-teno.md); **$\alpha_{1,2}$ collide with $\alpha_k$** |
| $\alpha$ (Eq. 10) | kept, page-local | grid stretching |
| $\mu_{\mathrm{eff}}$, $\lambda_{\mathrm{eff}}$, $\tau_{w}$, $q_w$ | kept, page-local on [wall-modelled LES](/methods/wall-modeled-les.md) | |
| $Ma_\infty$, $Re_\tau$ | $M_\infty$, $\mathrm{Re}_\tau$ | |
| $y^*$ | kept | semi-local wall distance (§2.2) and $y/\delta$ (§4.2.2) — **collision in the source** |
| EP 6, WENO-Z 3/5/7, TENO 5, TENO-A 5 | kept | formal orders |

# Reference list

54 printed references in numbered Elsevier style ([1]–[54]), merged complete
into the [bibliography](/bibliography.md) with `citedby` `devanna-2023`. Ref.
[44] prints "Lelef SK" (Lele), kept as printed; [14] prints an article number
in the page field; [43] prints no page or article number; [52] is a CTR
Summer Program proceedings entry. No unparseable items and no printed
duplicates.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–12 (2026-10-23/30). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [URANOS](/software/uranos.md)
* [Wall-modelled large-eddy simulation](/methods/wall-modeled-les.md)
* [WENO-Z weights](/methods/weno-z.md)
