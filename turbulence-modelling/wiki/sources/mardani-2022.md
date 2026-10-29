---
type: Source
title: "Mardani & Nazari (2022) — Dynamic adjustment of the Eddy Dissipation Concept model for turbulent/combustion interactions in mixed combustion regimes"
description: "RANS study of the Eddy Dissipation Concept for MILD combustion: restates the Magnussen cascade and the validity limits of the default constants, generalizes the cascade frequency ratio, and proposes cell-wise fine-structure constants from the local turbulence Reynolds and Damköhler numbers, tested on jet-in-hot-coflow burners with standard k-ε."
resource: "doi:10.1016/j.combustflame.2021.111873"
source_kind: paper
authors: [Mardani A., Nazari A.]
year: 2022
venue: "Combust. Flame 241:111873"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Combustion_and_Flame_Mardani_Dynamic_adjustment_of_the_Eddy_Dissipation_Concept_model_for.pdf"
tags: [combustion, rans, eddy-viscosity]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Mardani & Nazari (2022) study the Eddy Dissipation Concept (EDC) of
Magnussen, a RANS turbulence–chemistry interaction closure in which
reactions take place in "fine structures" whose length fraction
$\gamma_{\mathrm{fs}}$ and residence time $\tau_{\mathrm{fs}}$ follow from an
energy-cascade model with two constants $C_{D1}$, $C_{D2}$. The target is
MILD (moderate or intense low-oxygen dilution) combustion, where the default
constants are known to fail. The turbulence closure is the standard
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) with
$C_{\varepsilon1}$ raised from 1.4 to 1.6 for the round jet, and the
cascade constant is tied to it through $\tfrac23C_{D1}=C_\mu=0.09$.

The authors first restate the cascade and the validity limits of the default
EDC: the fine structure is smaller than the cell only for $Re_T>20.8$, and
the time-scale fraction $R=\gamma_{\mathrm{fs}}^2/(1-\gamma_{\mathrm{fs}}^3)$
stays below 1 only for $Re_T>64.31$; $\pm10\%$ on $C_{\mathrm{vf}}$ moves the
second limit to 95 and 42. They then generalize the cascade frequency ratio
to $\alpha_{\mathrm c}$ (default 2) and run parametric studies on the
Adelaide jet-in-hot-coflow (JHC) burner HM1: the error trends reverse
between the upstream, low-Damköhler sections and the downstream section,
where entrained air ends the MILD regime, so no single global constant set
fits both.

The contribution is a localized ("dynamic") EDC: identifying the
fine-structure velocity with a turbulent flame speed
$s_{\mathrm L}\sqrt{Re_T+1}$ gives $C_{D2}\approx3/[4(Re_T+1)Da^2]$ and cell-wise
$C_\tau$ and $C_{\mathrm{vf}}$ computed at every iteration from a Damköhler number
built on one reaction or the fastest reaction of the DRM-22 mechanism,
without the pre-calculation step of Parente et al. (2016). The authors note
that their $C_{\mathrm{vf}}$ decreases with $Da$ and $Re_T$, opposite to the
correlations of Parente et al. (2016) and Romero-Anton et al. (2020).
In 2-D axisymmetric RANS of JHC HM1, HM3 and the Delft JHC the local model
improves downstream temperature and species peaks (more than 15% for HM1
at 120 mm, more than 12% for HM3), with upstream accuracy comparable to the
default EDC. The bundle has no EDC page; the work sits beside the
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
page as RANS combustion modelling.

# Version read

Version of record (Combust. Flame 241 (2022) 111873; received 23 Oct 2020,
available online 23 Mar 2022, copyright line "© 2021"), 15 pages, all read;
pages 3–6 read visually because the equations are garbled in the text
extraction. Page-1 title, authors and DOI match the metadata. The
supplementary material (Sandia/TUD flame D, Sydney bluff-body burner, DJHC
velocity and $k$ profiles) is not in the file and was not read. Numbering on
this page is that of this version.

# Key claims

Page-local symbols: $\gamma_{\mathrm{fs}}$ the fine-structure length fraction
$u^*/u'$ and $\gamma^*_{\mathrm{fs}}$ the volume fraction (the source's
$\gamma$, $\gamma^*$; the registry's $\gamma$ is the ratio of specific
heats); $\tau_{\mathrm{fs}}$ the fine-structure residence time (the source's
$\tau$); $C_{D1}$–$C_{D4}$, $C_{\mathrm{vf}}$ (the source's $C_\gamma$, as on [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)), $C_\tau$ the EDC constants;
$Re_T$ the turbulence Reynolds number; $Da$ the Damköhler number;
$\alpha_{\mathrm c}$ the cascade frequency ratio and
$\beta_{\mathrm c}=\varepsilon/q^*$ (the source's $\alpha$, $\beta$);
$u^*$, $L^*$ the fine-structure velocity and length; $s_{\mathrm L}$ (registry §11)
and $s_{\mathrm T}$ the laminar and turbulent flame speeds.

1. The EDC is "not a unique model, but a set of variants" (citing Li et al.); its constants need tuning for MILD combustion (§2). **Stated**
2. In the Magnussen cascade with frequency doubling, $\varepsilon/q^*\to4/3$: "75% of the total dissipation of turbulent kinetic energy would be dissipated in the fine structures" (§2, Eqs. 7–8). **Derived**
3. Matching the cascade eddy viscosity to the $k$-$\varepsilon$ model, $\tfrac23C_{D1}=C_\mu=0.09$, gives $C_{D1}=0.135$; $C_{D2}=0.5$ is Magnussen's experimental value (§2). **Derived** ($C_{D1}$) / **Stated** ($C_{D2}$)
4. The fine-structure Reynolds number is $u^*L^*/\nu=2C_{D2}/(3C_{D1})$, so the fine structure depends on the combustion constants and, through $C_{D1}$, on the turbulence model (§2). **Derived**
5. The default EDC is physically meaningful only for $Re_T>20.8$ (fine structure smaller than the cell, Eq. 18) and, more restrictively, for $Re_T>64.31$ (time-scale fraction $R<1$, printed $\gamma_{\mathrm{fs}}<0.7568$, Eqs. 19–20) (§4). **Derived**
6. Numerical studies show the standard EDC cannot be applied below $Re_T=64.31$; the critical value varies between constant sets (§4). **Stated**
7. A 10% decrease of $C_{\mathrm{vf}}$ moves the validity limit to $Re_T>42$, a 10% increase (2.1377 → 2.3515) to $Re_T>95$ (§4, Fig. 2). **Derived**
8. With $\omega_n=\alpha_{\mathrm c}\omega_{n-1}$ the dissipation ratio becomes $\varepsilon/q^*=1/(1-\alpha_{\mathrm c}^{-2})=\beta_{\mathrm c}$; $\alpha_{\mathrm c}$ must exceed unity (§4.1, Eqs. 22–23). **Derived**
9. $\alpha_{\mathrm c}$ acts on the EDC cascade only, not on the turbulence field or mixing time scale; it changes the chemical time scale directly and the velocity only through temperature and composition (§4.1). **Stated**
10. For JHC-HM1, increasing $\alpha_{\mathrm c}$ raises $\gamma_{\mathrm{fs}}$, lowers $\tau_{\mathrm{fs}}$ and raises the peak temperature; lowering it reduces the error at $Z=120$ mm, raising it reduces the error at $Z=30$ and 60 mm (§6.1, Fig. 4, Table 3). **Shown**
11. Higher $\alpha_{\mathrm c}$ is better upstream (low $Da$), lower downstream (high $Da$), so "finding an optimum α for all regions seems to be impossible" (§6.1, Fig. 4d). **Shown**
12. Increasing the fine-structure to Kolmogorov time-scale ratio increases the error at $Z=30$ and 60 mm and decreases it at 120 mm, attributed to wind-tunnel air entrainment raising the oxygen level downstream (§6.2, Fig. 5). **Shown**
13. If only the MILD region is targeted, a smaller $C_{D2}$ (fine-structure to Kolmogorov scale ratios below 1) is applicable (§6.2). **Stated**
14. Approximating the fine-structure velocity by $s_{\mathrm T}=s_{\mathrm L}\sqrt{Re_T+1}$ yields $C_{D2}\approx3/[4(Re_T+1)Da^2]$ (§4.2, Eqs. 26–31). **Derived**
15. The local constants are $C_\tau=C_{D3}/(2Da\sqrt{Re_T+1})$ and $C_{\mathrm{vf}}=C_{D4}[9/(16C_{D1}^2(Re_T+1)Da^2)]^{1/4}$ with $C_{D3}=1.0$, $C_{D4}=0.65$; $C_{D4}$ was varied from 0.2 to 1.0 and 0.65 chosen against temperature and species measurements (§4.2, Eqs. 32–33). **Derived** (form) / **Stated** (values; the parametric study is not displayed)
16. A non-unity $C_{D4}$ limits the reacting part of the fine structure as a reacting fraction below 1 does, consistent with Lewandowski & Ertesvåg (§4.2). **Stated**
17. In the new correlation $C_{\mathrm{vf}}$ decreases with $Da$ and $Re_T$, opposite to Parente et al. ($C_{\mathrm{vf}}\propto Da^{1/2}(Re_T+1)^{1/2}$) and Romero-Anton et al. ($C_{\mathrm{vf}}\propto Da^{3/4}(Re_T+1)^{1/2}$); the model thus gives a smaller fine structure for fast burning or highly mixed conditions (§4.2). **Derived**
18. Unlike Parente et al., the local constants are computed during the solution at every iteration, with no pre-calculation using a global mechanism (§1, §4.2). **Stated**
19. For JHC-HM1 the local model gives $C_{\mathrm{vf}}$ in 0.6–3.5, $C_\tau$ in 0.2–3, $Da<8.5$ (growing downstream), $Re_T$ in 200–2400 and $\gamma_{\mathrm{fs}}<0.75$, within the physical limits; $\gamma_{\mathrm{fs}}$ is also clipped at 0.7548 in the code (§6.3, Fig. 6). **Shown**
20. Combustion lowers $Re_T$ against the non-reacting case, more strongly downstream: "combustion has suppressed the turbulence and relaminared the turbulent flow" (§6.3, Fig. 7). **Shown**
21. Damköhler numbers from reaction no. 49 of DRM-22 ($Da_I$) and from the maximum local rate ($Da_{II}$) give similar predictions, both somewhat better than reaction no. 58 (§6.3, Fig. 8). **Shown**
22. At $Z=120$ mm the local model improves temperature, OH and CO$_2$ by more than 15% for HM1 and more than 12% for HM3; at 30 and 60 mm the deviations are about 10% or less for HM3 and, for HM1, about 3% for temperature and CO$_2$ and 37% for OH (§6.3, Fig. 12). **Shown**
23. On JHC-HM1 the local model's accuracy is near that of Parente et al.'s local approach (§6.3, Fig. 9). **Shown**
24. For DJHC-I (Re 4100) the local model improves temperature at $Z=90$, 120 and 150 mm against the standard EDC and De et al.; upstream results are similar, attributed to low heat release under high dilution (§6.3, Fig. 11). **Shown**
25. For Sandia/TUD flame D and the Sydney bluff-body burner predictions improve "in a range of higher than 10%" and "few to 50 percent" (§6.3). **Stated** (shown only in the supplementary material, not read)
26. The CPU time per iteration of the standard model and of the local model with $Da_I$ is "relatively the same", lower than with $Da_{II}$ (§6.3). **Stated** (no timings given)
27. The average deviation from measurements falls by more than 10% (abstract), more than 13% in high-$Da$ regions (conclusions), and more as the oxidizer oxygen level decreases (abstract, §7). **Shown**

# Printed slips

- **Eq. (20):** printed "$R<1\rightarrow\gamma<0.7568\rightarrow Re_T>64.31$".
  *(compiler check, not in the sources)* $R=\gamma^2/(1-\gamma^3)=1$ (Eq. 19)
  has the root $\gamma=0.75488$, and $(2.1377/0.75488)^4=64.31$ reproduces
  the printed $Re_T$ limit; $\gamma=0.7568$ gives $(2.1377/0.7568)^4=63.66$.
  The code clipping value printed in §6.3 is 0.7548. The text repeats "the
  limit value of 0.7568 for γ".
- **§4:** "the standard EDC model setting (i.e., $C_{D1}$ = 2.137; $C_{D2}$ =
  0.5)"; the paper gives $C_{D1}=0.135$ (§2), and 2.1377 is the default
  $C_{\mathrm{vf}}$.
- **Table 3, $\alpha=1.2$:** printed $C_\tau=0.6369$. *(compiler check, not
  in the sources)* Eq. (24) with $C_{D2}=0.5$ and
  $\beta_{\mathrm c}=1/(1-1/1.44)$ gives 0.6396; the other rows match Eq. (24)
  to four digits.
- **Eq. (25) against Table 3:** Eq. (25) prints
  $\gamma=(C_{D2}/(\beta C_{D1}^2))^{1/2}(\nu\varepsilon/k^2)^{1/2}$.
  *(compiler check, not in the sources)* The $C_{\mathrm{vf}}$ column of Table 3 is
  reproduced by $(C_{D2}/(\beta_{\mathrm c}C_{D1}^2))^{1/4}$ with
  $C_{D2}=0.5$ and $C_{D1}\approx0.134$ (1.4827 at $\alpha=1.1$, 2.1377 at
  $\alpha=2$); the printed exponent 1/2 gives about 2.2 at $\alpha=1.1$. The
  default $C_{\mathrm{vf}}=2.1377=(3C_{D2}/(4C_{D1}^2))^{1/4}$ likewise implies
  $C_{D1}=0.1340$, while the text gives 0.135.
- **$Re_T$:** defined as $k^2/(\nu\varepsilon)$ (Eqs. 11, 18, 34) and as
  $\nu_T/\nu$ (before Eq. 27); with $\nu_t=C_\mu k^2/\varepsilon$ the two
  differ by the factor $C_\mu$. The derivation of Eqs. (27)–(33) uses the
  second, Eq. (34) evaluates the first.
- **Eq. (8):** the series is printed
  $1+\frac1{2^2}+\frac1{2^4}+\cdots+\frac1{2^n}$, with the sum $\to4/3$.
- **Eq. (29):** the first expression prints $\frac43C_{D2}\nu\,u^{*2}/L^*$,
  the second $(Re_T+1)s_{\mathrm L}^2/L^{*2}$.
- **§4.2:** "the Damköhler number is defined as the ratio … (i.e.,
  $a=\tau_\eta/\tau_c$)".
- **§6.2:** "parametric study was done on the new variables $L^*/\eta_k$ and
  $t^*/\eta_k$", while Eq. (37) is $t^*/\tau_k$; the equation number (36) is
  used twice (error metric in §6, $L^*/\eta_k$ in §6.2).
- **§4:** "De et al. [24] defined the time scale fraction, R, by Eq. (17)";
  the relation is Eq. (19), Eq. (17) is the source term.
- **§6.2:** "The author, recently [28], has also reported…"; ref. [28] is
  Parente et al., the sole-author work is Mardani [29].
- **§5 against Fig. 3:** the text uses 40,000 cells for JHC after the grid
  study; the Fig. 3 caption calls 60,000 cells "fine" and 40,000 "coarse".
- **§7:** "Bluff-body Sydney burner (HM1)"; HM1 is a JHC case label.
- **Table 2:** the second row (Re 8800) carries no case label.

# Notation map

| Mardani & Nazari | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\epsilon$, $k$ | $\varepsilon$, $k$ | RANS dissipation and turbulent kinetic energy; $k=\tfrac32u'^2$ in the cascade |
| $\nu$, $\nu_T$ ($\nu_t$) | $\nu$, $\nu_t$ | |
| $C_\mu$, $C_{\epsilon1}$ | $C_\mu$, $C_{\varepsilon1}$ | standard $k$-$\varepsilon$; $C_{\varepsilon1}=1.6$ |
| $\gamma$, $\gamma^*$ | $\gamma_{\mathrm{fs}}$, $\gamma^*_{\mathrm{fs}}$ (page-local) | **collision** with $\gamma$, ratio of specific heats; the source also writes $\gamma$ for the volume-type fraction in Eqs. (15), (18), (25) |
| $\tau$ | $\tau_{\mathrm{fs}}$ (page-local) | fine-structure residence time; **collision** with the SGS stress $\tau_{ij}$ |
| $C_{D1}$, $C_{D2}$, $C_{D3}$, $C_{D4}$, $C_\tau$ | same (page-local) | EDC constants; default $C_{D2}=0.5$ |
| $C_\gamma$ | $C_{\mathrm{vf}}$ (page-local, as on [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)) | fine-structure constant, default 2.1377 |
| $Re_T$, $Re_t$ | $Re_T$ (page-local) | turbulence Reynolds number; two printed definitions (Printed slips) |
| $\alpha$ | $\alpha_{\mathrm c}$ (page-local) | cascade frequency ratio; **collision** with the DG blending factor $\alpha$; $\alpha_T$, $\alpha_L$ in Eq. (26) are thermal diffusivities |
| $\beta$ | $\beta_{\mathrm c}$ (page-local) | $\varepsilon/q^*$; **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $u^*$, $L^*$, $\omega^*$, $t^*$ | (fine-structure velocity, length, frequency, time) | $\omega_n$ is a cascade frequency, not the specific dissipation rate $\omega$ |
| $q_n$, $q^*$, $w_n$ | (cascade dissipation at step $n$ and at the fine structure; energy transfer) | |
| $\tau_\eta$, $\tau_k$; $\eta_k$ | $\tau_\eta$; $\eta$ | Kolmogorov time and length |
| $Da$, $Da_I$, $Da_{II}$, $\tau_c$, $c_r$ | (page-local) | Damköhler number $\tau_\eta/\tau_c$; chemical time; rate over $\rho$ |
| $S_L$, $S_T$ | $s_{\mathrm L}$ (registry §11), $s_{\mathrm T}$ (page-local) | laminar and turbulent flame speeds; **collision:** the registry's $S_L$ is the Lundquist number |
| $\chi$ | $\chi_{\mathrm{fs}}$ (page-local reacting fraction of the fine structure) | **collision** with the SA ratio $\chi$ |
| $R$, $\tau_{mix}$ | (time-scale fraction, mixing time) | $R$ is not a Reynolds stress |
| $Y_i^*$, $Y_i^0$, $\overline{Y_i}$, $R_{EDC}$ | $Y_k^*$, (surrounding-state mass fraction), $\langle Y_k\rangle$, $\bar R_k$ (page-local) | the overbar is the RANS cell mean, not an LES filter |
| $Z$ | (axial distance from the jet exit, mm) | |

# Reference list

66 printed references, numbered in order of first citation. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Same-author same-year works take suffixes in printed order
(Sorrentino 2017, 2018; Mardani 2010). Printed defects: ref. [5] has a
garbled author list; ref. [15] has no journal or pages; ref. [36] has no
venue; ref. [45] prints the authors as initials only; ref. [50] prints a
scrambled author order; ref. [60] prints Warnatz twice; ref. [65] (DRM-22)
is a web resource; refs. [42], [49] carry online-first placeholders
("0 (0)", "000"). Three printed keys (`lee-2015`, `ihme-2012`, `li-2017`)
name works other than the bibliography entries of those keys and are keyed `lee-2015-c`, `ihme-2012-b` and `li-2017-d`. No printed duplicates.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [k-ε models](/methods/k-epsilon-model.md)
