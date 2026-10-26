---
type: Source
title: "Möller et al. (2024) — Transitional Delayed Detached-Eddy Simulation for a Compressor Cascade: A Critical Assessment"
description: "Assesses DDES-γ, an SST-based delayed detached-eddy simulation coupled to Menter's one-equation γ transition model, on the V103 compressor cascade: transition coupling fixes separation-induced transition, but bypass transition needs synthetic inflow turbulence and a constant 5 % upwind flux blending."
resource: "doi:10.2514/1.b39344"
source_kind: paper
authors: [Möller F.M., Tucker P.G., Wang Z.N., Morsbach C.]
year: 2024
venue: "J. Propuls. Power 40:533–546"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Propulsion_and_Power_Möller_Transitional_Delayed_Detached-Eddy_Simulation_for_a_Compress.pdf"
tags: [hybrid-rans-les, des, transition, turbomachinery, numerical-dissipation]
timestamp: 2026-10-26T15:50:00Z
---

# Summary

Möller et al. (2024) assess DDES-$\gamma$, a transitional
[delayed detached-eddy simulation](/methods/detached-eddy-simulation.md) that
the same authors introduced in an earlier paper. It couples an SST-based DDES
([$k$-$\omega$ SST](/methods/k-omega-sst-model.md) with the shear-layer-adapted
subgrid length of Shur et al. 2015 and $C_{\mathrm{DES}}=0.65$) with the
one-equation $\gamma$ model of Menter et al. (2015), a
[local-correlation-based transition model](/methods/local-correlation-based-transition-model.md).
The coupling multiplies the production of the modelled $k$ by $\gamma$,
multiplies the DDES destruction by $\max(0.1,\gamma)$, and drops the
separation-induced extra production of the RANS $\gamma$ model. The authors
argue that in laminar regions $\gamma=0$ keeps the modelled $k$ and the RANS
length scale near zero. The length-scale test then declares "RANS mode"
where the model behaves like an implicit LES, so the RANS/LES distinction of
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) loses its meaning in
transitional flow.

The test case is the V103 [compressor cascade](/benchmarks/compressor-cascade.md)
at the scaled DNS point of Zaki et al. (2010): $M=0.1$, $Re=138\,500$ on the
axial chord, $Tu=3.25\%$. The suction side has a
[laminar separation bubble](/definitions/laminar-separation-bubble.md) and the
pressure side bypass transition. All runs use DLR's second-order finite-volume
solver [TRACE](/software/trace.md). The references are the DNS, the authors'
own [WALE](/methods/wale-model.md) LES and the DDES of Yin & Durbin (2021).
DDES-$\gamma$ fixes the separation-induced transition that the fully turbulent
DDES misses. On the pressure side it only reproduces RANS-$\gamma$, as it does
on the [ERCOFTAC T3C5 plate](/benchmarks/ercoftac-t3-flat-plate.md). Without
inflow turbulence, the modelled free-stream $Tu$ decays unphysically ahead of
the blade, because the shielding function enables LES mode in the free stream.
The synthetic turbulence generator of Shur et al. (2014)
([inflow turbulence generation](/methods/inflow-turbulence-generation.md))
restores the free-stream $Tu$ and lets bypass transition proceed through
resolved scales. The skin friction then improves only after the dynamic
central/upwind flux blending is replaced by a constant 5 % upwind fraction, a
choice about [numerical dissipation](/properties/numerical-dissipation.md). The
authors then ask whether the model still works as intended or "acts more like
an LES model". The base closure is the
[Boussinesq](/definitions/boussinesq-hypothesis.md) SST model, and the DES
constant was checked on decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
(results not shown).

# Version read

Author-typeset accepted manuscript in the AIAA journal template (PDF created
14 February 2024), 30 pages numbered 2–30, with no journal typesetting and no
preprint-server stamp. All pages were read; pp. 1–13 were checked visually.
A page-1 footnote says the work was presented as AIAA paper 2023-3421 at
AVIATION 2023. Page numbers on this page are those of the manuscript, not the
journal's 533–546. Title and authors match Crossref.

# Key claims

1. DDES-$\gamma$ sets $P_{k,\mathrm{trans}}=\gamma P_k$ and $D_{k,\mathrm{trans}}=\max(0.1,\gamma)\,\rho k_{\mathrm{sgs}}^{3/2}/l_{\mathrm{DDES}}$ in the SST $k$ equation, and drops the separation-induced production $P_k^{\lim}$ of the RANS $\gamma$ model; the removal is justified in the authors' earlier paper (§II.B.3, Eqs. 24–25). **Stated**
2. DDES uses $C_{\mathrm{DES}}=0.65$; the calibration of the implementation was verified on decaying isotropic turbulence (§II.B.1, p. 6). **Stated** (results not shown)
3. Shielding constants $C_{d2}=3$ (Spalart et al.) and $C_{d1}=20$ (Gritskevich et al.) (§II.B.1, Eq. 19). **Stated**
4. $f_d$ is an "enabler" of LES mode, not an activator: LES mode needs both $l_{\mathrm{RANS}}>C_{\mathrm{DES}}\Delta_{\mathrm{SLA}}$ and $f_d\neq0$ (§II.B.1, p. 7). **Stated**
5. In a laminar region $\gamma=0$ gives zero production and 10 % of the original destruction, so $k_{\mathrm{sgs}}$ stays minimal, $l_{\mathrm{RANS}}\approx0$, and the region is classified as RANS mode although it is "more a laminar mode"; LES mode there would need extremely fine meshes (§II.D, p. 10, Fig. 1b). **Derived** (qualitative, from Eq. 27)
6. "In laminar regions, the DDES-$\gamma$ acts more like an implicit LES model": the subgrid viscosity is minimal and the model tries to resolve turbulent scales, hence the demand for finer meshes (§II.D, p. 10). **Stated**
7. The dynamic solver blending of Travin et al. was designed for fully turbulent flows that need a clear RANS/LES distinction (§II.D, p. 10). **Stated**
8. On the ERCOFTAC T3C5 flat plate (bypass transition at a comparable free-stream $Tu$), DDES-$\gamma$ gave results identical to RANS-$\gamma$ (§II.F, p. 10). **Stated** (results not shown)
9. Mesh study (675 720, 1 079 440 and 4 317 760 cells, 40 spanwise cells, $y^+<1$): the integral total-pressure loss converges towards the LES; the medium mesh is chosen, comparable to Yin & Durbin's 1 474 560 cells (§III.A, Tables 2–3, Fig. 3). **Shown**
10. Fully turbulent DDES (no transition model) misses the suction-side bubble, produces modelled TKE too early, ends in an open separation near the trailing edge, and "transitions" right behind the leading edge on the pressure side (§III.B.1, Figs. 5–8). **Shown**
11. Baseline DDES-$\gamma$ agrees well with LES and DNS in $C_p$ and the suction-side bubble; $C_f$ is almost identical to DNS up to $x/c_{\mathrm{ax}}\approx0.65$ but too low after reattachment, because $\gamma$ suppresses near-wall production and the resolved TKE is slightly low (§III.B.1, Figs. 5–9). **Shown**
12. For bypass transition the baseline DDES-$\gamma$ follows RANS-$\gamma$, not DNS or Yin & Durbin; $l_{\mathrm{ratio}}$ rarely exceeds one on the pressure side, and a slight rise at 0.4–0.6 axial chords from the wall removes modelled TKE and delays the onset slightly (§III.B.1, Fig. 10). **Shown**
13. Without inflow turbulence both DDES variants show a rapid, unphysical drop of the free-stream $Tu$ near the leading-edge plane, unlike DNS, LES and RANS-$\gamma$; the cause is $f_d=1$ in the free stream together with a very small $\Delta_{\mathrm{SLA}}$ (§III.B.1, Figs. 11–12). **Shown**
14. With the synthetic turbulence generator the bubble closes slightly earlier, closer to DNS, through a minor overprediction of resolved TKE (§III.B.2, Figs. 13–14). **Shown**
15. With the generator the pressure-side $C_f$ barely changes, since $f_d=0$ near the wall enforces RANS mode; but the maximum-TKE extraction shows bypass transition now carried by resolved scales ($x=0.3$–$0.55\,c_{\mathrm{ax}}$, slightly delayed against LES), against modelled TKE ($0.5$–$0.65\,c_{\mathrm{ax}}$) without it (§III.B.2, Figs. 13b, 15, 16). **Shown**
16. "Assessing the transition process by surface values such as $c_f$ only may lead to wrong conclusions" (§III.B.2, p. 21). **Shown** (Fig. 13b against Fig. 16)
17. If resolved scales are supplied at the inflow, the near-wall mesh is "most likely" fine enough that boundary-layer shielding "might not be required" (§III.B.2, p. 21). **Stated**
18. The generator restores the free-stream turbulence intensity: the total $Tu$ agrees with DNS (slight overprediction of $k_{\mathrm{sgs}}+k_{\mathrm{res}}$), and with resolved free-stream content $f_d=1$ there is acceptable (§III.B.2, Figs. 17–18). **Shown**
19. Upwind-fraction scan with inflow turbulence: 0 % (pure central) oscillates and suppresses the suction-side separation; 25 % (Yin & Durbin's value) damps the synthetic turbulence, delays bypass transition and overpredicts the bubble; a constant 5 % agrees best with DNS (§III.B.3, Fig. 19). **Shown**
20. The dynamic blending is close to fully upwind in the boundary layers on both sides and damps the near-wall resolved scales (§III.B.3, Fig. 20). **Shown**
21. DDES-$\gamma$ with constant 5 % blending and inflow turbulence predicts both transitions better than the dynamic variant, agreeing with Yin & Durbin and closer to DNS on the pressure side; the resolved TKE follows the LES (§III.B.3, Figs. 21–22). **Shown**
22. Varying the blending without inflow turbulence gave results like the dynamic variant (not shown), which the authors read as an interdependence of resolved inflow scales and numerical dissipation (§III.B.3, p. 25). **Stated**
23. Caveat: bypass-transition prediction now relies on resolved scales; it is "questionable" whether the model stays in its intended range or "acts more like an LES model", and the 5 % blending is a further parameter that may need re-tuning for other cases or meshes (§III.B.3, pp. 25–26). **Stated**
24. Baseline DDES-$\gamma$ cannot be expected to beat RANS-$\gamma$ for bypass transition, since attached layers without resolved content stay in RANS mode (§IV). **Derived**

The hybrid length and the coupled destruction (Eqs. 18, 25, 27), with
$l_{\mathrm{RANS}}=\sqrt{k_{\mathrm{sgs}}}/(\beta^*\omega)$, $\beta^*=0.09$:

$$\begin{aligned}
l_{\mathrm{DDES}}&=l_{\mathrm{RANS}}-f_d\max\big(0,\;l_{\mathrm{RANS}}-C_{\mathrm{DES}}\Delta_{\mathrm{SLA}}\big),\qquad l_{\mathrm{ratio}}=l_{\mathrm{RANS}}/l_{\mathrm{DDES}},\\
D_{k,\mathrm{trans}}&=\max(0.1,\gamma)\,\frac{\rho\,k_{\mathrm{sgs}}^{3/2}}{l_{\mathrm{DDES}}},\qquad f_d=1-\tanh\big[(C_{d1}r_d)^{C_{d2}}\big].
\end{aligned}$$

# Printed slips

- **§II.B.1, p. 7:** "Values of $l_{\mathrm{ratio}}<0$ are not possible for the DDES model." By Eq. 18, $l_{\mathrm{DDES}}\le l_{\mathrm{RANS}}$, so $l_{\mathrm{ratio}}\ge1$ whenever $l_{\mathrm{DDES}}>0$; the statement is true but weaker than the bound the surrounding text uses ("$=1$ in RANS regions, $>1$ in LES regions") *(compiler check, not in the sources)*.
- **Symbol $\kappa$:** the ratio of specific heats ($\kappa=1.4$, §II.A) and the von Kármán constant in Eq. 20, whose value is not printed.
- **Symbol $\omega$:** the nomenclature calls it "turbulent dissipation rate, s⁻¹"; the text calls it the specific dissipation rate.
- **Fig. 1b:** the progressive-transition region ($0<\gamma<1$) is labelled "Still: production of $k_{\mathrm{mod}}$ prevented", while Eq. 24 gives production $\gamma P_k$, reduced but not zero.
- **Ref. [12]:** printed "https://doi.org/10.2514/6.2013-995, AIAA 2023-0995" for a 2013 conference paper; the paper number conflicts with the printed year and DOI.
- **Ref. [5]:** title printed "Feasability".
- Typos: "transitition" (p. 23), "another trend is can be observed" (p. 19), "DDES-FTis", "RANS-$\gamma$are" (p. 17).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overbar $\bar\square$ | $\langle\cdot\rangle$ (Reynolds average) | **collision:** not an LES filter |
| tilde $\tilde\square$, $\square''$ | $\langle\cdot\rangle_\rho$, $\phi''$ (Favre average, fluctuation) | **collision:** not a Favre filter |
| $-\overline{\rho u_i''u_j''}$ (Eq. 13) | $-\langle\rho u_i''u_j''\rangle$, i.e. $-\langle\rho\rangle R_{ij}$ in Favre form | negative convention; Eq. 13 is the Boussinesq closure with $-\tfrac23\rho k\delta_{ij}$ |
| $\tilde S_{ij}$ | $S_{ij}$ of the Favre-averaged velocity | |
| $\Omega$ (Eq. 14) | $\lvert\Omega\rvert$ (vorticity magnitude) | SST limiter |
| $k_{\mathrm{mod}}$, $k_{\mathrm{res}}$, $k_{\mathrm{tot}}$ | $k_{\mathrm{sgs}}$ (modelled, RANS or subgrid), $k_{\mathrm{res}}$, $k_{\mathrm{tot}}$ | |
| $\omega$ | $\omega$ (specific dissipation rate) | printed as "turbulent dissipation rate" in the nomenclature |
| $\beta_k=0.09$ | $\beta^*$ | |
| $a_1=0.31$, $\sigma_k$, $\sigma_\omega$, $\alpha$, $\beta$, $\sigma_{\omega2}$, $F_1$, $F_2$ | SST constants and blending functions | values of the $F_1$-blended constants not printed; **collision:** $\alpha$ is not the DG/FV blending factor |
| $l_{\mathrm{RANS}}$, $l_{\mathrm{DDES}}$, $l_{\mathrm{ratio}}$ | same (DES length scales, as on the DES page) | |
| $C_{\mathrm{DES}}$, $f_d$, $r_d$, $C_{d1}$, $C_{d2}$ | same | |
| $\Delta_{\mathrm{SLS}}=\Delta_{\mathrm{SLA}}$ | $\Delta$ (filter width), shear-layer-adapted definition | |
| $\kappa$ | $\gamma$ (Eqs. 10–11) and $\kappa$ (Eq. 20) | **collision:** two meanings in the source |
| $\gamma$ | $\gamma$ (intermittency) | transition-page meaning |
| $P_k^{\lim}$ | (separation-induced extra production of the $\gamma$ model) | set to zero in DDES-$\gamma$ |
| $\sigma_b$ | (upwind fraction of the inviscid flux, page-local) | **collision:** $\sigma$ is not the viscous stress |
| $c_{\mathrm{ax}}$ | (axial chord, 0.204 m) | Reynolds-number length |
| $TI$, FSTI | $Tu$ | |
| $l_t$ | $L$ (inlet turbulent length scale) | |
| $c_p$, $c_f$ | $C_p$, $C_f$ | definitions not printed |
| $c_P$, $c_V$ | $c_p$, (specific heat at constant volume) | |
| $\zeta$, $\zeta_{\mathrm{int}}$ | (total-pressure loss, local and pitch-integrated) | |
| $d$, $\eta$ (plots) | $d$ (wall distance) | **collision:** $\eta$ is not the Kolmogorov length |

# Reference list

36 printed references, AIAA numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [16] is
the authors' own 2023 paper that introduced DDES-$\gamma$, a different work
(key `moller-2023`). Ref. [12] carries the "AIAA 2023-0995" inconsistency,
kept in a note. All references parsed; no printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Compressor cascades](/benchmarks/compressor-cascade.md)
- [ERCOFTAC T3 flat-plate transition cases](/benchmarks/ercoftac-t3-flat-plate.md)
- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [WALE model](/methods/wale-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [TRACE](/software/trace.md)
