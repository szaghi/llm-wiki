---
type: Source
title: "Rajek & Pozorski (2026) — High-fidelity pseudo-spectral simulations of isotropic turbulence: Large eddy simulations with semi-adaptive parametrization of residual flow scales"
description: "Pseudo-spectral LES of forced isotropic turbulence up to a Taylor-scale Reynolds number near 10 000 on 256³ modes shows that the positive low-wavenumber plateau of the Chollet–Lesieur spectral eddy viscosity suppresses the inertial subrange, and proposes an adaptively determined spectral eddy viscosity, zero at low wavenumbers, and the resolution criterion k_cλ ≈ 10."
resource: "doi:10.1063/5.0315239"
source_kind: paper
authors: [Rajek M., Pozorski J.]
year: 2026
venue: "Phys. Fluids 38:035118"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Physics_of_Fluids_Rajek_High-fidelity_pseudo-spectral_simulations_of_isotropic_turbu.pdf"
tags: [spectral-eddy-viscosity, isotropic-turbulence, sgs-model, grid-requirements, les]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Rajek & Pozorski (2026) ask whether Fourier pseudo-spectral LES of forced
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
with a [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) captures
the inertial subrange at Taylor-scale Reynolds numbers up to about 10 000 on a
fixed $256^3$ grid. At $Re_\lambda\approx100$ the Chollet–Lesieur plateau–cusp
model (Domaradzki's fit with $C_K=1.4$) is compared with a $256^3$
[DNS](/definitions/direct-numerical-simulation.md) and with filtered DNS (sharp
cutoff $k_c=30$, which the paper calls "a priori LES";
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
Resolved energy transfer is roughly right but the PDF of $Q$ has shortened
tails; the a priori eddy viscosity of Domaradzki et al. (1987), computed from
the filtered DNS, is negative for $k<0.4k_c$ (close to $-\nu$), which the
authors connect to [backscatter](/definitions/energy-backscatter.md), and used
as a closure it recovers the DNS spectrum. At high $Re_\lambda$ (hypothetical
DNS-to-LES grid ratios 2 to 1024) the standard model gives a $k^{-5/3}$ range,
but the compensated spectrum rises for $k/k_c>0.1$ and $\Pi(k)=\varepsilon$
holds only over the first shells: the authors attribute the suppression of the
inertial subrange to the positive low-wavenumber plateau, and the LES
statistics saturate at $Re_\lambda\approx1000$.

The proposed **adaptively determined spectral eddy viscosity** is driven by a
regulator, after Overholt & Pope's deterministic forcing, toward a prescribed
model spectrum, set to zero in the forcing range and below a transition
wavenumber $k_t$ by a $\tanh$ blending, fitted to a four-parameter form and
corrected for dealiasing; its time average (the "adaptively reconstructed"
viscosity) has no run-time cost. At $Re_\lambda\approx100$ it recovers the
DNS spectrum with $R^2=0.994$ against 0.271 for the standard model; at
$Re_\lambda\approx10\,000$ lowering $k_t$ to $0.1k_c$ helps, but $\Pi=\varepsilon$
needs resolution. The authors propose $k_c\lambda\approx10$
([grid-point requirements](/results/les-grid-point-requirements.md)), side with
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
against the plateau, and contrast their closure with the
[autonomous eddy-viscosity models](/methods/autonomous-eddy-viscosity-model.md)
of Domaradzki.

# Version read

Version of record (AIP; submitted 4 December 2025, accepted 9 February 2026,
online 4 March 2026), 18 PDF pages (AIP cover plus pp. 035118-1 to -17), all
read; Table III checked visually (the text layer drops minus signs). Page 1
matches the Crossref metadata; no identity issue. Numbering is that of this
version.

# Key claims

Page-local symbols (spectral page: $k$ the wavenumber magnitude, $K$ the
turbulent kinetic energy): $\nu_t^+(k\mid k_c)$ the normalized spectral eddy
viscosity, $\nu_t=\nu_t^+[E(k_c)/k_c]^{1/2}$; $\nu^+_{t,s}$, $\nu^+_{t,\mathrm{th}}$,
$\nu^+_{t,a}$, $\nu^+_{t,m}$, $\nu^+_{t,ar}$ its standard, theoretical, adaptive,
fitted and adaptively reconstructed forms; $\nu^+_{\mathrm{pl}}$ the plateau
value; $T(k)$, $T_<(k)$ the transfer spectrum and its resolved-triad
part; $\Pi(k)$ the spectral energy flux; $C_K$ the Kolmogorov constant and
$C_K(k)=E(k)k^{5/3}/\varepsilon^{2/3}$; $E_m(k)$ the model spectrum; $k_0$,
$k_{\max}$, $k_t$, $k_{f,\max}$ the lowest, dealiased maximum, transition and
highest forced wavenumbers; $\varepsilon_f$ the injection rate; $L_B$, $L_t=K^{3/2}/\varepsilon$
the box size and turbulence length; $S_{\partial u}$, $F_{\partial u}$ the
skewness and flatness of the longitudinal velocity derivative.

1. At $Re_\lambda\approx100$ ($N_x$ ratio 4, $k_c=30$ against DNS $k_{\max}=121$) the standard model transfers energy among resolved scales at about the right rate; shell energies are over-estimated by up to 15% for $k\eta<0.1$ and under-estimated by up to 50% over the rest of the range (§III A, Fig. 1). **Shown**
2. The LES holds more than 95% and the filtered DNS more than 98% of the DNS kinetic energy; without eddy viscosity the spectrum is unphysical (§III A, Fig. 1). **Shown**
3. About 85% of the resolved scales of the LES are isotropic, $I(k)\approx1$ (§III A, Fig. 2). **Shown**
4. The PDF of $Q$ with the standard model keeps its non-Gaussian form with much shorter tails than the DNS and only slightly narrower than the filtered DNS; the filtered DNS "establishes the predictive capabilities of LES", so further gain needs structural modelling beyond eddy viscosity (§III A, Fig. 3). **Shown** / **Stated**
5. The theoretical eddy viscosity, $T(k)-T_<(k)=-2\nu_{t,\mathrm{th}}(k\mid k_c)k^2E(k)$ from filtered DNS (Eq. 16), rises steeply near $k_c$; its cutoff value grows almost exponentially up to $k_c\eta=1$ and drops beyond, for $0.15\le k_c\eta\le1.1$ (§III B, Fig. 4). **Shown**
6. At $Re_\lambda\approx100$, $k_c=30$, the theoretical eddy viscosity is negative for $k<0.4k_c$ with magnitude close to $\nu$ and grows by about an order of magnitude from $0.7k_c$ to $k_c$, in agreement with Domaradzki et al. (1987) (§III B, Fig. 5). **Shown**
7. Used as a closure, the theoretical eddy viscosity recovers the DNS spectrum over almost the whole resolved range but leaves the PDF of $Q$ nearly unchanged; it needs DNS data and has no predictive value beyond DNS-attainable Reynolds numbers; the authors state it "has not been applied as a subgrid-scale closure in a true LES to date" (§III B, §V, Figs. 5–6). **Shown** / **Stated**
8. Standard model (Eqs. 13–14): $\nu^+_{t,s}=C_K^{-3/2}(0.441+15.2e^{-3.03k_c/k})$, with $C_K=1.4$ "to approximately match" Métais & Lesieur, i.e. $\nu_{t,s}=(0.267+9.21e^{-3.03k_c/k})[E(k_c)/k_c]^{1/2}$. **Stated**
9. With $\varepsilon=6\times10^{-2}$ m²/s³, $\nu=1.5\times10^{-5}$ m²/s and $256^3$ LES, the hypothetical DNS cases give $Re_\lambda$ from 97 (case 0) to 9825 (case 10, ratio 1024); the measured LES values range from 94 to 10 067 (§III C, Tables II–III). **Shown**
10. On $256^3$, $E(k_c)$ saturates at a grid ratio near 32 ($Re_\lambda\approx1000$); spectra of higher cases become statistically indistinguishable (§III C, Fig. 7). **Shown**
11. $C_K(k)$ approaches a constant for most scales but rises for $k/k_c>0.1$ at $Re_\lambda\gtrsim1000$; it lies in the expected range for about 75% of resolved scales, with differences up to 65% near the cutoff (§III C, Figs. 8–9). **Shown**
12. $\Pi(k)\approx\varepsilon$ holds only in the first shells even at $Re_\lambda\approx10\,000$; the inertial subrange is suppressed by excessive dissipation at intermediate and low wavenumbers, attributed to the positive plateau (§III C, Fig. 9; §IV). **Shown** / **Stated**
13. $S_{\partial u}=-0.52$ (DNS), then $-0.47$, $-0.40$, $-0.35$, $-0.33$, $-0.32$ for cases 1–5 and constant afterwards; $F_{\partial u}$ from 5.29 to 4.47 (Table III); with the standard model on $256^3$ the maximum $Re_\lambda$ for accurate inertial-range dynamics is at most about 1000 (§III C). **Shown**
14. Scales outside the forced band are highly isotropic at $Re_\lambda\approx10\,000$; $L_1/L_2$ ranges from 1.881 to 2.065 (§III C, Figs. 10–11, Table III). **Shown**
15. Proposed: the regulator $\frac{d\nu^+_{t,a}}{dt}=\frac{\mathcal C[F_c]}{\tau_{\mathrm{reg}}(k)}$, $\tau_{\mathrm{reg}}=c_1[k^3E_m(k)]^{-1/2}$, $F_c=c_2\ln(E/E_m)$ ($c_1=1$, $c_2=0.25$, damping constants $c_3=c_4=0$), where the operator $\mathcal C$ applies the blending $B(k;k_t)=\tfrac12+\tfrac12\tanh[\alpha_B(k-k_t)]$ ($\alpha_B=0.75$) and never lets the viscosity go negative (§IV, Eqs. 18–27). **Derived** (definition)
16. The adaptive viscosity is fitted to $\nu^+_{t,m}=a_0+a_1\{1-\tanh[((k_c-k)/(a_2k_c))^{a_3}]\}$ by least squares over $k_t\le k<k_c$ (Eqs. 28–30), under-relaxed (Eq. 31), corrected at $k=k_c$ by $D_{\mathrm{al}}=(4\pi k^2/N_k-1)^{3/2}$ (Eq. 32), and time-averaged into $\nu^+_{t,ar}=\nu^+_{t,m}B\,D_{\mathrm{al}}$ (Eqs. 33–34). **Derived**
17. At $Re_\lambda\approx100$ the adaptive viscosity recovers the DNS spectrum over $k_c/2\le k<k_c$ with $R^2=0.993$ against 0.271 for the standard model (Fig. 14); the adaptively reconstructed one gives $R^2=0.994$ (text, Fig. 15) (§IV). **Shown**
18. The adaptive viscosity drops sharply at $k_c$ because spherical-truncation dealiasing already removes much energy from the last shell; a bump from $k/k_c\approx0.2$ follows a step-like spectral artifact of unclear origin, removed by smoothing (§IV, Figs. 14–15). **Shown**
19. The adaptively reconstructed viscosity slightly enhances the PDF of $Q$ relative to the standard model but does not enrich the resolved scales beyond the theoretical-viscosity LES (§IV, Fig. 16). **Shown**
20. A scale-dependent scaling $\nu_t=\nu_t^+[E(k)/k]^{1/2}$ (Eq. 35) replaces $[E(k_c)/k_c]^{1/2}$, giving a more responsive regulator, better fits and less round-off as $E(k_c)/k_c\to0$ (§IV). **Stated** (tests not shown)
21. At $Re_\lambda\approx10\,000$ with $k_t=0.4k_c$ the reconstructed viscosity drains energy at about the right rate for $k\ge k_c/2$, with a strict $k^{-5/3}$ there, but $\Pi(k)\ne\varepsilon$; raising $k_c$ ($k_c\lambda=0.07$, 0.14, 0.28) widens the $\Pi=\varepsilon$ range while energy accumulates before $k_c/2$ (§IV, Fig. 17). **Shown**
22. At $k_c\lambda=0.28$, lowering $k_t$ improves the spectrum before $k_c/2$; with $k_t=0.1k_c$ the spectrum agrees relatively well with the reference, but at most 15% of resolved scales show $\Pi(k)=\varepsilon$ (§IV, Fig. 18). **Shown**
23. The transition point is first bounded by $k_{f,\max}<k_t\le k_c/2$ (Eq. 19, after Kraichnan's 75% of the subgrid transfer from $k_c/2\le k\le k_c$), then by $k_{f,\max}<k_t\lesssim0.1k_c$ (Eq. 36); with $k_t\sim1/\lambda$ this gives the LES resolution criterion $k_c\lambda\approx10$, the analogue of $k_{\max}\eta>1$ in DNS (§III C, §IV). **Stated**
24. Capturing almost the whole inertial subrange at $Re_\lambda\approx10\,000$ without artificial viscosity would need about $8192^3$ to $16\,384^3$ modes, against about $262\,144^3$ for DNS (§IV, Table II). **Derived** (estimate)
25. The regulator costs $O(\lfloor\sqrt2N_x/3+0.5\rfloor)$ operations, far less than a 3D DFT, and the reconstructed form none (§IV, §V). **Stated**
26. Accurate large-scale modelling of isotropic turbulence does not need increased viscosity at low wavenumbers; the positive plateau is "highly undesirable" and signals insufficient resolution compensated by extra dissipation, contrary to Kraichnan, Chollet & Lesieur, Chollet and Domaradzki and in line with spectral-vanishing-viscosity and numerical-dissipation works (§V). **Stated** on **Shown** evidence
27. Beyond DNS the LES needs one extra input, $C_K$, which could be estimated on the fly from the compensated spectrum, making the LES "fully autonomous" (§V). **Stated**
28. The method is specific to isotropic turbulence; splitting into statistically homogeneous subdomains, as in [Hausmann et al. (2022)](/sources/hausmann-2022.md), is suggested for other flows (§V). **Stated**

The DNS (companion paper) sets the viscosity from the target resolution,
$\nu=[\varepsilon_f(k_{\max}\eta/k_{\max})^4]^{1/3}$ with
$k_{\max}=k_0\lfloor\sqrt2N_x/3+0.5\rfloor$ (Eq. 5), forces
$\sqrt3\le k/k_0\le\sqrt{10}$ by $\boldsymbol f_{\boldsymbol k}=(\varepsilon_f/2E_f)\boldsymbol u_{\boldsymbol k}$
(Eq. 4) and runs at $k_{\max}\eta=1.5$, $Re_\lambda=94$ (Table I).

With the printed $\nu=1.5\times10^{-5}$
m²/s and $\varepsilon=6\times10^{-2}$ m²/s³, $(\nu\varepsilon)^{1/4}\approx3.1\times10^{-2}$
m/s; Table I's $u'=0.15$ m/s and $u'/u_\eta=4.92$ give $u_\eta\approx3.0\times10^{-2}$
m/s. With $L_t/L=0.43$ and $L/L_B=1/8$, $L_t/L_B=0.43/8\approx0.054$, while
$1/(8\times0.43)\approx0.29$ follows from $L/L_t=0.43$ *(compiler check,
not in the sources)*.

# Printed slips

- **§II A:** "$u_\eta\sim0.3\times10^{-2}$ m/s", against Table I ($u'=0.15$ m/s, $u'/u_\eta=4.92$) and the printed $\nu$ and $\varepsilon$ (compiler check above).
- **§III C:** "the ratio of $L_t/L$ asymptotically approaches the value of 0.43. Therefore, assuming $L_B/L=8$, … $L_t/L_B=1/(8\times0.43)\approx0.3$".
- **§IV:** "Using the Heaviside function, Eq. (22) can be rewritten in a more concise form" introduces Eq. (27), which is Eq. (20) with the operator of Eq. (26) applied to $F_c$.
- **§IV against Tables I and III:** "the integral one is $L\sim0.125L_B$"; the tables give $L/L_B=0.107$–0.112.
- **Table III:** $Re_L$ is not defined in the text or the nomenclature.
- **Typos:** "Taylor miscroscale" (nomenclature); "decovolution" in the title of ref. [31]; "J. Fluid. Mech." (ref. [26]); "can be used the determine" (§III C).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ | $k$ | wavenumber magnitude (spectral page) |
| $E_K$ | $K$ | turbulent kinetic energy (spectral page) |
| $\alpha,\beta$ indices | $i,j$ | |
| $\bar u_\alpha$ | $\bar u_i$ | LES filter |
| $\hat u_\alpha$, $\hat{\bar u}_\alpha$ | $u_{i,\boldsymbol k}$, $\bar u_{i,\boldsymbol k}$ | **the source's hat is the Fourier transform**, not a test filter |
| $\tau_{\alpha\beta}=\overline{u_\alpha u_\beta}-\bar u_\alpha\bar u_\beta$ | $\tau_{ij}$ | positive trace |
| $\nu_e(k,t;k_c)$ | $\nu_t(k\mid k_c)$ | spectral eddy viscosity |
| $\nu_e^+$, $\nu_{e,s}$, $\nu_{e,th}$, $\nu_{e,a}$, $\nu_{e,m}$, $\nu_{e,ar}$ | $\nu_t^+$, $\nu_{t,s}$, $\nu_{t,\mathrm{th}}$, $\nu^+_{t,a}$, $\nu^+_{t,m}$, $\nu^+_{t,ar}$ (page-local) | |
| $\mathcal P$ | $\nu^+_{\mathrm{pl}}$ (page-local) | plateau value; **collision** with the pressure jump ratio $\mathcal P$ |
| $P[\cdot]$ | $\mathcal C[\cdot]$ (page-local) | control operator |
| $F_c$, $S$, $D_1$, $D_2$, $R$ | $F_c$ and its source, damping terms, ratio $E/E_m$ (page-local) | $S$ also the derivative skewness |
| $\tau(k)$, $c_1$–$c_4$, $\alpha$, $\gamma$ | $\tau_{\mathrm{reg}}(k)$, $c_1$–$c_4$, $\alpha_B$, under-relaxation factor (page-local) | not $\tau_{ij}$, not the DG $\alpha$, not $\gamma$ |
| $B(k;k_t)$, $H$, $D(k)$ | $B$, $H$, $D_{\mathrm{al}}(k)$ (page-local) | blending, Heaviside, dealiasing correction |
| $T(k)$, $T_{<k_c}$, $T_{>k_c}$ | $T(k)$, $T_<$, $T_>$ (page-local) | transfer spectra; not the temperature |
| $\Pi(k)$ | $\Pi(k)$ (page-local) | spectral flux; **collision** with the local SGS flux $\Pi$ |
| $C_K$, $C_K(k)$ | page-local | 1.4 in the standard model, 1.85 in the model spectrum |
| $N$, $N_{DNS}$, $N_{LES}$, $N_k$ | $N_x$, (DNS and LES $N_x$), modes per shell | **not** the polynomial degree $N$ |
| $\lambda$, $Re_\lambda$, $\eta$, $\tau_\eta$, $u_\eta$ | same | $\lambda=(15\nu u'^2/\varepsilon)^{1/2}$ |
| $L$, $L_1$, $L_2$, $L_t$, $L_B$ | $L$, page-local | spectral integral scale; longitudinal and transverse; $K^{3/2}/\varepsilon$; box |
| $T_e=L/u'$, $T_t$, $T_f$ | $T_E$, page-local | large-eddy turnover; turbulence time $K/\varepsilon$; fitting interval |
| $S$, $F$ | $S_{\partial u}$, $F_{\partial u}$ (page-local) | **collision** with the strain rate |
| $I(k)$ | page-local | isotropy spectrum |
| $Q$ | $Q$ | second invariant of the velocity gradient |
| FDNS ("a priori LES") | filtered DNS | not an a priori test of a model |

# Reference list

40 printed references, numbered (AIP superscript style). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ingested works among them: ref. [1]
[Yeung et al. (2025b)](/sources/yeung-2025-b.md) (printed under the same
author-year as the ingested Yeung et al. (2025)), [21]
[Domaradzki (2024)](/sources/domaradzki-2024.md) and [40]
[Hausmann et al. (2022)](/sources/hausmann-2022.md). Refs. [8] and [9]
(Rajek & Pozorski, Int. J. Multiphase Flow 197, 2026) and [10] (the companion
DNS paper, printed "submitted", no year) share the author-year of this source and are keyed `rajek-2026-b`, `rajek-2026-c` and `rajek-2026-d`. Ref. [23] prints "Patterson, Jr."; ref. [28]
is a chapter of *Turbulent Shear Flows IV* without pages. No item is
unparseable.

# Pages created or updated

Chunk 16 (2026-10-29). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
- [Spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
