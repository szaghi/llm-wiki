---
type: Source
title: "Zhang et al. (2022) — Wall-cooling effects on pressure fluctuations in compressible turbulent boundary layers from subsonic to hypersonic regimes"
description: "DNS of six zero-pressure-gradient boundary layers at Mach 0.5, 2 and 8, adiabatic and cooled: wall cooling lowers wall-pressure fluctuations at subsonic and supersonic speeds but raises them at Mach 8 through near-wall travelling-wave structures, shown by a Poisson decomposition into rapid, slow, viscous and compressible pressure; Laganelli's model is refitted."
resource: "doi:10.1017/jfm.2022.595"
source_kind: paper
authors: [Zhang P.J.Y., Wan Z.H., Liu N.S., Sun D.J., Lu X.Y.]
year: 2022
venue: "J. Fluid Mech. 946:A14"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Fluid_Mechanics_Zhang_Wall-cooling_effects_on_pressure_fluctuations_in_compressibl.pdf"
tags: [dns, compressible, wall-cooling, pressure-fluctuations, hypersonic]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

Zhang et al. (2022) study by [DNS](/definitions/direct-numerical-simulation.md)
how wall cooling changes the pressure fluctuations of spatially developing,
zero-pressure-gradient compressible
[boundary layers](/benchmarks/turbulent-boundary-layer.md) at $M_\infty=0.5$,
2 and 8, each with a quasi-adiabatic wall ($T_w/T_r=1$) and a cooled one
($T_w/T_r=0.25$ at $M_\infty=0.5$, 0.5 otherwise), compared at
$Re_\tau\approx650$. The code is [STREAmS](/software/streams.md): an
eighth-order energy-preserving central flux
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
hybridized at $M_\infty=8$ with seventh-order [WENO](/methods/weno-scheme.md)
by a modified Ducros [sensor](/definitions/shock-sensor.md), and a
recycling–rescaling [inflow](/methods/inflow-turbulence-generation.md).

The statistics are validated through the
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
(van Driest fails for the cooled walls, Trettel–Larsson only in the
viscous sublayer, the total-stress transformation of Griffin et al. 2021
collapses all six cases onto the [law of the wall](/definitions/law-of-the-wall.md)),
the Walz and generalized Reynolds-analogy temperature–velocity relations,
and [Morkovin's](/definitions/morkovin-hypothesis.md) density scaling. Wall
cooling lowers $p'_{\mathrm{rms}}/\tau_w$ at $M_\infty=0.5$ and 2 but raises
it near the wall at $M_\infty=8$ (wall value 3.00 to 3.41), which the
authors attribute to travelling-wave-like alternating positive and
negative structures (APNS) of dilatation and pressure inside cold
low-speed streaks, with streamwise wavelength $\lambda_x^+\approx100$. The
Laganelli et al. (1983) model of wall-pressure fluctuations is refitted on
quasi-adiabatic numerical data, and a linear fit of the free-stream
fluctuations against $M_\infty$ is proposed.

The methodological contribution extends the Poisson decomposition of the
fluctuating pressure, previously applied to
[channels](/benchmarks/turbulent-channel-flow.md), to compressible
boundary layers: $p'=p_r+p_s+p_\tau+p_c+p_h$ (rapid, slow, viscous,
compressible, harmonic), with all far-field pressure assigned to $p_c$.
Cooling suppresses the vorticity mode ($p_r$, $p_s$) at $M_\infty=0.5$ and
2 and enhances the acoustic mode ($p_c$) everywhere, most at $M_\infty=8$,
where $p_c$ dominates near the wall.

# Version read

Version of record (J. Fluid Mech. 946:A14, Cambridge University Press;
received 17 December 2021, accepted 10 July 2022), 33 pages, all read;
pages 9–12, 18 and 20 also read visually for Eqs. (3.1)–(3.3), (5.1),
(6.1)–(6.5). Page-1 title, authors and DOI match the metadata. No identity
problem. Numbering on this page is that of this version.

# Key claims

The source's overbar (Reynolds average, thermodynamic variables) is
$\langle\cdot\rangle$, its tilde (Favre average, velocities)
$\langle\cdot\rangle_\rho$; its viscous stress $\tau_{ij}$ is $\sigma_{ij}$;
its dilatation $\theta$ is written $\vartheta_d=\partial_ku_k$ (page-local,
not the momentum thickness); the pressure components $p_r$, $p_s$,
$p_\tau$, $p_c$, $p_h$ are page-local.

1. Wall cooling suppresses $p'_{\mathrm{rms}}/\tau_w$ in the subsonic ($M_\infty=0.5$) and supersonic ($M_\infty=2.0$) cases but enhances it near the wall in the hypersonic ($M_\infty=8.0$) case; wall values 2.56 (M05T100), 2.03 (M05T025), 2.88 (M20T100), 2.60 (M20T050), 3.00 (M80T100), 3.41 (M80T050) (Abstract, §3, §5, Table 3, Fig. 13). **Shown**
2. Travelling-wave-like alternating positive and negative structures of dilatation and pressure are found in the viscous sublayer and buffer layer of the hypersonic cases; wall cooling makes them more prevalent, and they lie within cold low-speed streaks (§4, Fig. 12, plane $y^*=5$). **Shown**
3. For M80T050 the wall value of $p'_{\mathrm{rms}}/\tau_w$ becomes the maximum of the profile ("up to 3.41"), "a consequence of the observed APNS"; away from the wall the profile first decreases, then peaks again at the peak position of M80T100 (§5, Fig. 13b). **Shown**
4. In the quasi-adiabatic cases $p'_{\mathrm{rms}}/\tau_w$ peaks at about $y/\delta=0.04$ irrespective of Mach number; cooling shifts the peak outward to $y/\delta=0.24$ (M05T025) and $0.07$ (M20T050); in semi-local scaling the peaks collapse at about $y^*=30$ (§5, Fig. 13). **Shown**
5. The original Laganelli model (Eq. 5.1, $\sigma=0.006$, $\phi=0.64$) agrees better with uncorrected and corrected measurements but deviates from the extended measurements and the simulation data; the authors attribute this to historical data being "biased low", with a literature range $0.008\leqslant\sigma\leqslant0.01$ (§5, Fig. 14a). **Shown** (comparison) / **Stated** (cause)
6. Refitting on all numerical quasi-adiabatic data gives $\sigma=0.01$, $\phi=0.75$ ("by linear fitting"), which predicts $(p'_{\mathrm{rms}}/q_\infty)_w$ over the whole Mach range, the main improvement being at lower Mach number; Ritos et al.'s $\sigma=0.008$ underestimates for $M_\infty\leqslant2.0$ (§5, Fig. 14a). **Shown**
7. For cooled walls the refitted model gives reasonable values for M20T050 and M80T050; for $T_w/T_r=0.25$ it overestimates M05T025 and underestimates the M6Tw025 case of Zhang et al. (2017), because it accounts neither for the APNS nor for the acoustic mode at high Mach number (§5). **Shown** / **Stated**
8. Free-stream pressure fluctuations grow roughly linearly with Mach number, $(p'_{\mathrm{rms}}/\tau_w)_\infty=0.12M_\infty+0.08$, subsonic cases included, consistent with Laufer (1964); cooling enhances them at $M_\infty=0.5$, suppresses them at $M_\infty=8.0$ and has little influence at $M_\infty=2.0$ (§5, Fig. 14b). **Shown**
9. Wall cooling decreases the shape factor and increases $C_f$ in all regimes; the Reynolds-analogy factors $s_{\mathrm{RA}}=2C_h/C_f$ (registry §11) are 1.16, 1.14, 1.11, "all close to 1.1" as predicted by Hopkins & Inouye (1971) (§3, Table 3). **Shown**
10. The van Driest transformation fails for the cooled cases; Trettel–Larsson collapses the viscous sublayer but is less successful in the log region; the quasi-equilibrium transformation of Griffin et al. gives a common slope $1/\kappa$ but different intercepts; the total-stress transformation of Griffin et al. (2021) "agree[s] well with the wall law and the log law" for adiabatic and cooled cases (§3, Fig. 3). **Shown**
11. The Walz relation (Eq. 3.1) is accurate for the quasi-adiabatic cases but deviates for the cooled ones; the generalized Reynolds analogy of Zhang et al. (2014) (Eq. 3.2) fits both (§3, Fig. 5). **Shown**
12. Cooling enhances $u''_{\mathrm{rms}}/u_\tau$ and $\langle u''v''\rangle_\rho/u_\tau^2$, mainly because $u_\tau$ decreases, and shifts their peaks outward; Morkovin's density scaling improves the collapse and semi-local scaling collapses the peak positions (§3, Fig. 4). **Shown**
13. Cooling raises the turbulent Mach number $M_t$ in all three regimes (lower local sound speed); at $M_\infty=8$ it locally exceeds 0.3 in the buffer and log layers, so "eddy shocklets are expected to emerge" (§3, Eq. 3.3, Fig. 8). **Shown** / **Stated**
14. Cooling restrains the vorticity fluctuations in most regions, except very near the wall for M80T050; dilatation fluctuations grow with Mach number and peak at the wall, and cooling stimulates them strongly at $M_\infty=8.0$ (and at $M_\infty=0.5$ away from the wall) but suppresses them at $M_\infty=2.0$ (§3, Fig. 9). **Shown**
15. The near-wall streak spacing is about 100 in semi-local units for all cases, in accordance with Huang et al. (2022); in outer scaling cooling increases the streak size and streamwise coherence, most visibly for M05T025 (§4, Figs. 10–11). **Shown**
16. The fluctuating pressure is decomposed as $p'=p_r+p_s+p_\tau+p_c+p_h$ from the fluctuating pressure Poisson equation (Eqs. 6.4–6.5), with the boundary conditions of Table 4 (far field: $p_c=p'$, all others zero); the authors state that "the patterns of the pressure components in compressible TBLs have never been reported" (§1, §6.1). **Derived** (equations) / **Stated** (novelty); *(compiler check, not in the sources)* the right-hand sides of Eqs. (6.5a–d) sum to that of Eq. (6.4).
17. For M05T100 the r.m.s. profiles of $p'$, $p_r$, $p_s$, $p_\tau$ normalized by the wall value agree with incompressible channel data at $Re_\tau=550$ (Hoyas & Jiménez 2008) except near the boundary-layer edge; $p_s$ exceeds $p_r$ except very near the wall, consistent with Kim (1989) (§6.2, Fig. 18a). **Shown**
18. $p_r$, $p_s$ and $p_c$ dominate; $p_\tau$ matters only near the wall, and $p_\tau$ and $p_c$ are an order of magnitude weaker than $p_r$ and $p_s$ for M05T100; $p_c$ shows large-scale patterns, attributed to wavepackets induced by hairpin packets, and carries the radiated acoustic waves in the free stream (§6.2, Fig. 16). **Shown** / **Stated** (interpretation)
19. At $M_\infty=0.5$ cooling suppresses $p_r$ and $p_s$ (the vorticity mode), shifts their peaks outward and enhances $p_c$ (attributed to increased density fluctuations); at $M_\infty=2.0$ cooling acts mainly below $y^+=100$, and the suppression of $p_r$, $p_s$ and $p_\tau$ lowers $p'_{\mathrm{rms}}$ (§6.2, Fig. 18b,c). **Shown**
20. At $M_\infty=8.0$ cooling strongly enhances $p_c$ throughout the boundary layer and $p_r$ in the viscous sublayer and buffer layer, weakly affects $p_s$ (suppressed in the buffer and log layers) and strengthens $p_\tau$; in M80T050 $p_c$ has much larger amplitudes than the other components, with near-wall extremes at the APNS (§6.2, Figs. 17, 18d). **Shown**
21. Wall-pressure PDFs: at $M_\infty=0.5$ and 2.0 cooling narrows both tails of $p_w$, $p_{r,w}$, $p_{s,w}$ and $p_{\tau,w}$ but lifts the tails of $p_{c,w}$; at $M_\infty=8.0$ it lifts all tails, especially of $p_{c,w}$; in M80T050 $p_w$ and $p_{c,w}$ are positively skewed and $p_{\tau,w}$ strongly negatively skewed (§6.2, Fig. 19). **Shown**
22. Cross-correlations between components are negligible except in M80T050, where $p_r$–$p_s$, $p_r$–$p_c$ and $p_s$–$p_c$ are significant in the viscous sublayer and buffer layer ($p_s$–$p_c$ positive, $p_r$ negatively correlated with both); interactions with $p_h$ are negligible everywhere (§6.2, Fig. 20). **Shown**
23. Spectra: for M05T100 the premultiplied pressure spectrum peaks in the buffer layer at $\lambda_x^+\approx250$, and $p_c$ is dominated by wavelengths of order $\delta$; cooling lengthens the contributing wavelengths of all components (for $p_c$ up to about $3\delta$ at $M_\infty=0.5$) (§6.2, Figs. 21–22). **Shown**
24. At $M_\infty=8.0$ cooling raises the near-wall pressure fluctuations through a contribution at $\lambda_x^+\approx100$ (the APNS), matching the peak reported by Yu et al. (2020) in a channel at nominal Mach 8; in M80T050 these short wavelengths dominate the $p_c$ spectrum, so "the contributions of the APNS are mainly reflected by compressible pressure $p_c$" (§6.2, Fig. 23, §7). **Shown**
25. The main effects of wall cooling are the suppression of the vorticity mode and the enhancement of the acoustic mode; at $M_\infty=0.5$ and 2.0 the vorticity mode leads within the boundary layer, while in the cooled $M_\infty=8.0$ case the acoustic mode is "essential in both the near-wall region and the free stream, which should be considered when modelling high-Mach-number wall-bounded turbulence" (Abstract, §7). **Shown** / **Stated**
26. For M80T050 the components computed on 1200-point and 1000-point streamwise subdomains agree in instantaneous wall distributions and r.m.s. profiles (Appendix, Fig. 24). **Shown**
27. The spanwise domain is wide enough: the spanwise two-point correlations of $u''$ and $p'$ at $y^+=15$ decay to about zero within the half-span (§2, Fig. 2). **Shown**

# Printed slips

- **§6.1 against Table 4:** the text says "$\partial p/\partial y=0$ is applied for all pressure components in the streamwise direction and on the wall except for the harmonic pressure $p_h$"; Table 4 prints $\partial(\cdot)/\partial x=0$ at the streamwise boundaries and $\partial(\cdot)/\partial y=0$ only at the wall.
- **Fig. 5 caption against §3:** the Zhang et al. (2014) relation is called the "modified strong Reynolds analogy" in the caption and the "generalized Reynolds analogy" in the text and in the reference title.
- **Table 1:** $Re_\tau=623$ for M80T100, while the text places all cases at $Re_\tau\approx650$.
- **Spellings:** "Pirozzolo & Bernardini (2011) TBL2" (Fig. 4b legend), "Lagenelli model" (p. A14-19), "Farve" (p. A14-7), "the turbulent–non-turbulent interface exits" (p. A14-23), "sightly skewed" (p. A14-24).
- **References:** Morkovin (1962) printed "Mécanique de la Turbulence 367 (380), 26".

# Notation map

| Zhang et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f$, $f'$ | $\langle f\rangle$, $f'$ | Reynolds average and fluctuation (thermodynamic variables); **collision:** the overbar is not the LES filter |
| $\tilde f$, $f''$ | $\langle f\rangle_\rho$, $f''$ | Favre average and fluctuation (velocities); **collision:** the tilde is not the Favre filter |
| $\tau_{ij}$, $\tau'_{ij}$ | $\sigma_{ij}$, $\sigma'_{ij}$ | viscous stress; **collision** with the SGS stress |
| $\tau_w$, $u_\tau=\sqrt{\tau_w/\bar\rho_w}$, $\delta_v$ | $\tau_w$, $u_\tau$, $\delta_\nu$ | agree |
| $Re_\tau=\delta/\delta_v$ | $Re_\tau$ | agree |
| $y^*=y/\delta^*_\nu$, $\lambda_z^*$ | $y^*$ (semi-local scaling), (streak spacing in semi-local units) | agree |
| $Re^*_\tau=(\rho_\infty\tau_w)^{1/2}\delta/\mu_\infty$ | (friction Reynolds number with free-stream properties) | **collision:** this star uses free-stream, not local, properties |
| $k$, $C$ | $\kappa$, $B$ | log law $\kappa=0.41$, $B=5.2$ (Fig. 3); **collision:** $k$ is not the kinetic energy |
| $C_h$ | $C_h$ | Stanton number (registry §11), agree |
| $C_f$, $H$, $\delta^*$, $\theta$ | $C_f$, (shape factor), $\delta^*$, $\theta$ | |
| $B_q$ | (non-dimensional wall heat flux) | $-B_q>0$ for cooled walls |
| $T_r$, $r$, $T_{rg}$, $r_g$ | (recovery temperature and factor; generalized ones) | page-local |
| $\delta_i$ | (inlet boundary-layer thickness) | domain lengths in $\delta_i$ |
| $M_t=\sqrt{\overline{u''_iu''_i}}/\bar c$ | $M_t$ | defined with the full trace |
| $\theta'$, $\theta^+_{\mathrm{rms}}$ | $\vartheta_d'$ (page-local dilatation) | **collision** with the momentum thickness $\theta$ |
| $\omega^+_{\mathrm{rms}}$ | (vorticity r.m.s. in wall units) | |
| $p_r$, $p_s$, $p_\tau$, $p_c$, $p_h$ | (rapid, slow, viscous, compressible, harmonic pressure) | page-local |
| $\sigma$, $\phi$ | (Laganelli model constants; page-local $\sigma_L$, $\phi_L$ on [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)) | **collision:** $\sigma$ is not the viscous stress |
| $q_\infty$, $c_0$ | (free-stream dynamic pressure, free-stream sound speed) | |
| $\Theta$ | (Ducros threshold, 0.15) | **collision:** not the temporal filter width $\Theta$ of registry §11 |
| $\lambda_x^+$, $k_xE^+_{pp}$ | (streamwise wavelength in wall units; premultiplied spectrum) | **collision:** $k_x$ is a wavenumber |

# Reference list

61 printed references, author–year (JFM style), alphabetical. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Same-author same-year works take suffixes in printed order
(Bernardini 2011, two works; Pirozzoli 2010, two works). Eight printed
keys (Bernardini 2011, Duan 2011, Griffin 2021, Pirozzoli 2011, Schlatter
2010, Tang 2020, Xu 2021, Yu 2019) name works other than the
bibliography's entries of the same key and are resolved by venue (`bernardini-2011-b`, `bernardini-2011-c`, `duan-2011-b`, `griffin-2021-c`, `pirozzoli-2011-b`, `schlatter-2010-b`, `tang-2020-b`, `xu-2021-c`, and Yu 2019 onto its existing entry); Huang et
al. (2022) is the ingested [huang-2022](/sources/huang-2022.md). No printed
duplicate, no unparseable item.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [STREAmS](/software/streams.md)
