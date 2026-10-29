---
type: Source
title: "Tonicello et al. (2022) — Turbulence kinetic energy transfers in direct numerical simulation of shock-wave–turbulence interaction in a compression/expansion ramp"
description: "Spectral-difference DNS of a Mach-2.91 boundary layer over a 24° compression ramp followed by an expansion, with bulk artificial viscosity; an a priori budget of resolved kinetic energy shows that mean backscatter near the expansion and the dilatation–transfer correlation come from the spherical part of the subgrid or Reynolds stress."
resource: "doi:10.1017/jfm.2022.22"
source_kind: paper
authors: [Tonicello N., Lodato G., Vervisch L.]
year: 2022
venue: "J. Fluid Mech. 935:A31"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Fluid_Mechanics_Tonicello_Turbulence_kinetic_energy_transfers_in_direct_numerical_simu.pdf"
tags: [dns, shock-boundary-layer-interaction, backscatter, a-priori-a-posteriori, compressible, spectral-difference]
timestamp: 2026-10-29T10:05:00Z
---

# Summary

Tonicello et al. (2022) run a [DNS](/definitions/direct-numerical-simulation.md)
of a Mach-2.91 [boundary layer](/benchmarks/turbulent-boundary-layer.md)
($Re_\theta=2900$, $Re_\tau=340$) over a 24° compression ramp followed by
an expansion corner, at the conditions of Priebe & Martín (2012)
([shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
The discretization is the sixth-order
[spectral difference method](/methods/spectral-difference-method.md)
($N=5$), with [artificial bulk viscosity](/methods/artificial-viscosity-shock-capturing.md)
([bulk viscosity](/definitions/bulk-viscosity.md)) switched by a modal
[sensor](/definitions/shock-sensor.md) multiplied by a Ducros-type
compression/vorticity factor that turns it off at walls and in vortical
regions, and a Zhang–Shu positivity limiter; the inflow is a digital filter
([inflow turbulence generation](/methods/inflow-turbulence-generation.md))
with van Driest [transformed](/definitions/compressible-velocity-transformation.md)
mean profiles. Validation against DNS and experiment covers wall friction
and pressure, velocity profiles and Reynolds stresses; the spectra show an
inertial range lengthened after the shock
([shock-generated turbulence](/results/shock-generated-turbulence.md)),
and the authors note that most compression-ramp DNS use
[WENO](/methods/weno-scheme.md) schemes.

The DNS then serves [a priori](/definitions/a-priori-and-a-posteriori-testing.md):
the budget of resolved kinetic energy is evaluated with Favre time–span
averaging (RANS sense) and with an explicit differential filter of widths
$2h$, $4h$, $8h$ ([LES](/definitions/large-eddy-simulation.md) sense); the
budget closes to nearly zero, read as negligible
[numerical dissipation](/properties/numerical-dissipation.md). The
subgrid (or turbulent) transfer is mostly forward, but large
[backscatter](/definitions/energy-backscatter.md) appears even in the mean
near the expansion corner; compression correlates with forward transfer
and expansion with backscatter, and the correlation with the
[pressure dilatation](/definitions/pressure-dilatation.md) grows with the
filter width. Splitting the stress into deviatoric and spherical parts, the
mean deviatoric transfer is forward everywhere: the mean backscatter and
most of the dilatation–transfer correlation come from the spherical part
($k_{\mathrm{sgs}}$). An eddy viscosity ([Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md))
therefore suits the deviatoric part, while the authors propose a
bulk-viscosity-type model for the trace (untested). Preliminary LES with
the spectral-element [dynamic model](/methods/dynamic-procedure.md) of
Chapelier & Lodato is mentioned.

# Version read

Version of record (J. Fluid Mech. 935:A31, Cambridge University Press;
received 18 June 2021, accepted 31 December 2021), 43 pages, all read;
equations on pp. 9, 17, 18, 28 and the Fig. 7 caption checked visually.
Page 1 prints the first author "Niccolò Tonicello": the surname is
"Tonicello", without accent (a citing list in the bibliography spelled it
"Tonicellò"). Page-1 title, authors and DOI match the metadata. Numbering on
this page is that of this version.

# Key claims

The source's stress $\tau_{ij}=\bar\rho\tilde u_i\tilde u_j-\overline{\rho u_iu_j}$
is minus the registry's $\tau_{ij}$; its transfer term $K_3$ is the
registry's $-\Pi$ ($K_3<0$ forward transfer, $K_3>0$ backscatter); its
spherical transfer is $\Lambda=-\tfrac23\bar\rho k_{\mathrm{sgs}}\,\partial_l\tilde u_l$;
its order-$N$ SD scheme has degree $N-1$, so its $N=6$ is the registry's
$N=5$. The resolved pressure-dilatation work is $K_1=\bar p\,\partial_j\tilde u_j$.

1. A DNS of a 24° compression/expansion ramp at the Priebe & Martín (2012) conditions ($M=2.91$, $Re_\theta=2900$, $Re_\tau=340$, $u_\infty=610$ m/s, $\delta=7.1$ mm) is run with a sixth-order SD scheme ($N=5$), $(120+120+120)\times28\times27$ elements, 54M DoF as printed (Table 2); to the authors' knowledge the first spectral-element simulation of this interaction (§2). **Stated**
2. Resolution: first solution point at $y^+\approx0.3$, first element within $y^+<10$, $\Delta x^+=4.75$–$15$, $\Delta y^+=0.3$–$9$, $\Delta z^+=4.2$; the ratio of the effective spacing $(\Delta x\Delta y\Delta z)^{1/3}$ to the a posteriori Kolmogorov length is about 1 upstream of the shock and never above 6 downstream (§2.1). **Shown**
3. "Direct numerical simulation" is restricted to the scales of turbulence: shocks remain under-resolved and are regularized by artificial terms (§2.2). **Stated**
4. Multiplying the modal sensor by a Ducros-type factor (Eq. 2.10), nonzero only in compression, prevents the artificial viscosity from acting at walls and in strongly vortical regions with negligible compression (§2.2). **Stated**; the mean artificial viscosity is nonzero only near the shock (Fig. 12). **Shown**
5. The time- and span-averaged activation flag of the positivity limiter peaks at about $10^{-4}$: the limiter acts in a very small region and is mostly inactive in time (§3.2, Fig. 13). **Shown**
6. Upstream skin friction is slightly higher than in Priebe & Martín (2012) and lower than in Zhu et al. (2017); the experimental separation point is better predicted by the present DNS and Zhu et al. than by Priebe & Martín; the wall pressure follows Zhu et al. and departs from Priebe & Martín in $-3<x/\delta<0$ (§3.1, Fig. 3). **Shown**
7. Downstream of the interaction the mean velocity agrees better with the Ringuette et al. (2009) experiment than with the Wu & Martín (2007) DNS; similar results in the detached region were reported only by Kokkinakis et al. (2020) with a ninth-order WENO scheme (§3.1, Fig. 4). **Shown** / **Stated**
8. Incoming boundary layer at $x=-8\delta$: $Re_\theta=2873$, $\delta=7.43$ mm, $Re_\tau=355$, $\delta^*=2.72$ mm, $\theta=0.47$ mm, $H=5.86$, $C_f\times10^3=2.17$, against reference values 2900, 7.10, 340, 2.58, 0.47, 5.49, 2.16 (Table 3). **Shown**
9. Spectra (Taylor hypothesis and spanwise) show an inertial range, no energy accumulation near the Nyquist wavenumber, and an inertial range lengthened after the shock interaction (§3.2, Figs. 7–8). **Shown**
10. The monotonically decreasing spectra are not due to spanwise confinement: the Tong et al. (2017a,b) autocorrelations drop to zero at about $0.2\delta$ upstream with a span of about $2\delta$ (§3.2). **Stated** (argument from cited data)
11. Downstream of the interaction, conditioned on $M>1$, the density PDF extends to larger values while the pressure PDFs are insensitive to the sonic regime, attributed partly to shocklets (§3.2, Fig. 11). **Shown**
12. The resolved kinetic-energy balance (Eq. 4.8) evaluated at $y^+\approx30$ closes to nearly zero, indicating negligible numerical dissipation (§4.1, Fig. 17). **Shown**
13. The artificial-viscosity budget term $K_5=K_5^f+K_5^s$ (Eq. 4.13) is small against the other terms and dominated by its flux part; the sink part is negative by construction and much smaller (§4.1, Fig. 18). **Shown**
14. Even in the mean (RANS sense) a large region near the expansion corner shows inverse transfer ($\Pi<0$) from the fluctuating field to the mean flow; the correlation of compression and expansion with forward and inverse transfer reported by O'Brien et al. (2014) and Wang et al. (2018a, 2020) is "confirmed also on average" (§4.1, Fig. 14). **Shown**
15. PDFs of the transfer: averaged fields are dominated by forward transfer; filtered fields have many more values of both signs but a similar mean, consistent with eddy-viscosity models reproducing the mean but not the local transfer; the PDF narrows for $\Delta=8h$, and those for $2h$ and $4h$ differ negligibly (§4.2, Fig. 19). **Shown**
16. The subgrid Mach number $M_{\mathrm{sgs}}=\sqrt{2\bar\rho k_{\mathrm{sgs}}/(3\gamma\bar p)}$ (Eq. 4.14) reaches about 0.32 in the mean and larger values in the filtered fields; non-negligible compressibility effects are expected above about 0.3 (§4.2, Figs. 20–22). **Shown**
17. Joint PDFs of $K_3$ and $K_1$: compression enhances forward transfer and expansion backscatter, more strongly as the filter widens (§4.2, Figs. 23–24). **Shown**
18. $K_1$–$K_3$ correlation coefficients (Table 4): full field 0.2775 (average), 0.1936 ($4h$), 0.2682 ($8h$); quadrant I 0.8781, 0.5252, 0.6062; quadrant III 0.070, 0.3278, 0.3269; the correlation is stronger in expansion regions with backscatter than in compression with forward transfer. **Shown**
19. "The importance of compressibility in the modelling is imposed not entirely by the physics of the problem, but … strongly influenced by the filter width": a coarse LES feels compressibility more than a well-resolved one (§4.2). **Shown** (from the trend of Table 4)
20. Larger $M_{\mathrm{sgs}}$ correlates with stronger forward transfer in the mean, and with both forward transfer and backscatter in filtered fields (§4.2, Figs. 25–26). **Shown**
21. Splitting the transfer into deviatoric and spherical parts (Eq. 5.1) gives the equivalent eddy viscosity $\nu_t=(K_3+\Lambda)/(-2\bar\rho\tilde S^d_{ij}\partial_j\tilde u_i)$ (Eq. 5.3) (§5). **Derived**; *(compiler check, not in the sources)* with the source's $\tau_{kk}=-2\bar\rho k_{\mathrm{sgs}}$, the term $\tfrac13\tau_{kk}\,\partial_l\tilde u_l$ of Eq. (5.2) equals $\Lambda$, consistent with Eqs. (4.4), (4.7) and (4.10).
22. With non-spectral filters $k_{\mathrm{sgs}}>0$ (Vreman et al. 1994), so $\Lambda<0$ in expansions and $\Lambda>0$ in compressions, opposite to $K_3$ (§5). **Derived** / **Stated**
23. In the mean, the $\Lambda$–$K_3$ joint PDF lies almost entirely on the $\nu_t>0$ side: a positive eddy viscosity is "fairly accurate" on average even with backscatter, since $\Lambda$ compensates it; filtered fields show a large share of negative $\nu_t$ (§5, Fig. 27). **Shown**
24. $\Lambda$–$K_3$ correlation (Table 5): full field $-0.4755$ (average), $-0.2636$ ($4h$), $-0.3268$ ($8h$); quadrant II dominant, $-0.8990$, $-0.7392$, $-0.7922$ (§5). **Shown**
25. The averaged deviatoric transfer $K_3+\Lambda$ is negative (forward) in the whole domain: the deviatoric part of the stress is essentially dissipative on average, and the trace is directly responsible for the backscatter near the expansion corner (§5, Fig. 28). **Shown**
26. The $K_1$–$(K_3+\Lambda)$ correlation (Table 6) drops to 0.1081 (average), 0.0370 ($4h$), 0.0889 ($8h$): the dilatation–transfer correlation comes mainly from the spherical part; in filtered fields a mild correlation persists (§5, Fig. 29). **Shown**
27. Near shocks a bulk-viscosity term mirrors the spherical subgrid part, $\tfrac23\bar\rho k_{\mathrm{sgs}}\sim-\mu_b\,\partial_k\tilde u_k$ (Eq. 5.5); a bulk-viscosity SGS model for the trace, paralleling the shear eddy viscosity for the deviatoric part, is proposed as future work (§5, §6). **Stated** (not tested)
28. Preliminary LES of a similar configuration with the spectral-element dynamic model (Chapelier & Lodato 2016) gave "promising results" (Tonicello et al. 2021) (§5). **Stated**

# Printed slips

- **§2.1:** "$\varepsilon=2\nu S^d_{ij}(\partial u_i/\partial u_j)$": the derivative is printed with respect to $u_j$; $K_2$ of Eq. (4.10) uses $\partial\tilde u_i/\partial x_j$.
- **Table 2:** 54M DoF. *(compiler check, not in the sources)* $(120+120+120)\times28\times27$ elements with $6^3$ solution points each give $58\,786\,560\approx58.8$M; what the printed 54M counts is not stated.
- **§4.2, p. 26:** "Similar trends are observed for filtered data too (figure 23a,b)": the filtered data are Fig. 23(b,c); 23(a) is the averaged field.
- **Table 6:** quadrant I is printed 0.3829 for both $\Delta=4h$ and $\Delta=8h$.
- **Fig. 8 axis label:** printed $\mathbb E(\kappa_z\delta)\kappa_z^{5/3}/(\bar\varepsilon)^{3/2}$, compared with a Kolmogorov constant of 1.5. *(compiler check, not in the sources)* The compensated form printed by [Yeung et al. (2025)](/sources/yeung-2025.md), §3, $E(k)\langle\varepsilon\rangle^{-2/3}k^{5/3}$, divides by $\varepsilon^{2/3}$, not $\varepsilon^{3/2}$; the two exponents give different dimensions.
- **§2.1:** statistics "every $0.025\delta/u_\infty$ s for approximatively $1000\delta/u_\infty$ s" (unit appended to a dimensional time).
- **References:** Fernandez, Nguyen & Peraire (2018b) is printed "43rd AIAA Aerospace Sciences Meeting … AIAA Paper 2018-0062", while Bookey et al. (2005) is printed "43rd AIAA Aerospace Sciences Meeting and Exhibit. AIAA Paper 2005-309".
- **Typos:** "entropy overshot", "beexplained", "sucha", "artificialspanwise", "the the main flow features".

# Notation map

| Tonicello et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau_{ij}=\bar\rho\tilde u_i\tilde u_j-\overline{\rho u_iu_j}$ | $-\tau_{ij}$ | **sign collision:** negative of the registry stress (compressible form, with $\bar\rho$); $\tau_{kk}=-2\bar\rho k$ |
| $\tau^d_{ij}$ | $-\tau^d_{ij}$ | deviatoric part, same sign flip |
| $\tau^v_{ij}$ | (unclosed viscous term) | page-local |
| $k$ | $k_{\mathrm{sgs}}$ (filtered fields) or $k$ (averaged fields) | unresolved kinetic energy per unit mass |
| $K_0,\dots,K_5$ | (resolved kinetic-energy budget terms) | page-local; $K_3=-\Pi$, $K_1$ the resolved pressure-dilatation work |
| $\Lambda$ | (spherical-part transfer, $-\tfrac23\bar\rho k_{\mathrm{sgs}}\partial_l\tilde u_l$) | page-local |
| $Ma_{SGS}$ | $M_{\mathrm{sgs}}$ | subgrid Mach number (registry §11) |
| $Ma$ | $M$ | |
| $N$ (order of approximation) | $N+1$ | the source's solution polynomial has degree $N-1$; its $N=6$ is the registry's $N=5$ |
| $h$ | $h$ | DNS resolution; element size in App. B |
| $\Delta$ | $\Delta$ | filter width (§4.2); also the effective spacing $(\Delta x\Delta y\Delta z)^{1/3}$ (§2.1) |
| $\bar\phi$ | $\bar\phi$ or $\langle\phi\rangle$ | filter (LES sense) or time–span average (RANS sense) |
| $\tilde\phi$ | $\tilde\phi$ or $\langle\phi\rangle_\rho$ | Favre filter or Favre average |
| $\langle\cdot\rangle$ (Eq. 2.10) | $\{\cdot\}_e$ (element average) | **collision** with the Reynolds average |
| $S^d_{ij}$, $\tilde S^d_{ij}$ | $S^d_{ij}$, $\tilde S^d_{ij}$ | agree |
| $\sigma_{ij}$ | $\sigma_{ij}$ plus the artificial bulk term | |
| $\beta_{AV}$ | $\mu_{b,\mathrm{AV}}$ (artificial bulk viscosity, registry §11) | elementwise constant |
| $\beta$ (Eqs. 5.4–5.5) | $\mu_b$ | generic bulk viscosity |
| $\kappa$, $\kappa_{AV}$ | (thermal conductivity, artificial conductivity) | **collision** with the von Kármán constant; $\kappa$ is also the wavenumber in Fig. 7 |
| $Pr_\beta$, $Ma_{thr}$ | $Pr_{\mathrm{AV}}$ (artificial Prandtl number, registry §11), (threshold Mach number 3) | |
| $s_{modal}$, $s_e$, $s_0$, $l$, $\varepsilon_0$, $C_\varepsilon$ | (modal sensor, Ducros-modified sensor, threshold, width, maximum artificial viscosity, its constant) | page-local |
| $\omega_i$ | $\omega_i$ | vorticity, agree |
| $\delta^+=\delta u_\tau/\nu_w$ | $Re_\tau$ | Kármán number |
| $\delta$, $\delta^*$, $\theta$, $H$ | $\delta_{99}$, $\delta^*$, $\theta$, (shape factor) | |
| $c_f$ | $C_f$ | |
| $u^+_{VD}$ | (van Driest transformed velocity) | see [compressible velocity transformations](/definitions/compressible-velocity-transformation.md) |
| $\eta$ | $\eta$ | Kolmogorov length, agree |

# Reference list

126 printed references, author–year (JFM style), alphabetical. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Same-author same-year works take suffixes in printed order. The
cited Tonicello, Lodato & Vervisch (2022, Flow Turbul. Combust. 108:77) is
a different work from this paper and keeps its existing key
`tonicello-2022-b`. Fernandez et al. (2018a) is an arXiv preprint and stays
its own entry. Johnsen et al. (2010) is printed with ten authors and "et
al.". No printed duplicate, no unparseable item.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
