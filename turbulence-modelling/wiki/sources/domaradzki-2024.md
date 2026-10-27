---
type: Source
title: "Domaradzki (2024) — Autonomous large-eddy simulations of turbulence using eddy viscosity derived from the subgrid-scale similarity stress tensor"
description: "Carries the autonomous spectral LES method into physical space: an eddy viscosity with no adjustable constant is computed each step from the filtered energy transfer of a similarity-type stress, and reproduces the inertial range of forced isotropic turbulence and Comte-Bellot–Corrsin decay."
resource: "doi:10.1017/jfm.2024.212"
source_kind: paper
authors: [Domaradzki J.A.]
year: 2024
venue: "J. Fluid Mech. 985:A48"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Fluid_Mechanics_Domaradzki_Autonomous_large-eddy_simulations_of_turbulence_using_eddy_v.pdf"
tags: [sgs-model, eddy-viscosity, scale-similarity, spectral-eddy-viscosity, backscatter, isotropic-turbulence]
timestamp: 2026-10-26T20:44:00Z
---

# Summary

Domaradzki (2024) carries the author's spectral "autonomous" LES over to physical
space, giving the [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md).
In the spectral version the subgrid energy transfer across a test cutoff
$k_c/2$ is computed from the LES field at each step. It is converted into a
Kraichnan-type [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md),
rescaled to the real cutoff $k_c$, and scaled by an ultraviolet-flux relation.
In physical space the role of the resolved transfer is taken by the local energy
flux of a [similarity-type stress](/methods/scale-similarity-model.md) built from
the LES velocity with a graded (Gaussian or box) filter of width $\hat\Delta=2\Delta x$.
Inverting this flux pointwise into an eddy viscosity is unstable. Filtering the
flux once more replaces the spectral shell average, and the resulting viscosity
enters a [Boussinesq](/definitions/boussinesq-hypothesis.md) model of the
[subgrid-scale stress](/definitions/large-eddy-simulation.md). No adjustable
constant enters. A variant with a constant $C_{\mathrm A}\approx0.8$ enforces the
global transfer constraint.

The tests use a de-aliased pseudo-spectral code, in which
[numerical dissipation](/properties/numerical-dissipation.md) is said to be
negligible, on [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
Forced turbulence at nominal $Re_\lambda>10^4$ on $64^3$ and $32^3$ grids
recovers a $-5/3$ range. The decaying grid turbulence of Comte-Bellot &
Corrsin is predicted without adjustment, where an under-resolved
[DNS](/definitions/direct-numerical-simulation.md) fails. The subgrid transfer of
the model correlates with that of the similarity stress at 0.81, against about
0.4 quoted for the [Smagorinsky model](/methods/smagorinsky-model.md). The model
carries local [backscatter](/definitions/energy-backscatter.md) without
instability. With $C_{\mathrm A}=0.8$ it acts as a nearly wavenumber-independent
viscosity. A [dynamic](/methods/dynamic-procedure.md) determination of the
constant fails. The paper also restates why similarity models correlate well
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) but fail a
posteriori.

# Version read

Version of record (J. Fluid Mech., Cambridge University Press, open access
CC BY 4.0; received 23 September 2023, revised 16 January 2024, accepted 26
February 2024), 28 pages (985 A48-1 to A48-28), all read; the equations of
§§1–3 were checked visually. Locators are the journal's sections, equations,
figures and tables. Single author, printed "J.A. Domaradzki" (Crossref gives
"Domaradzki J."); no identity problem.

# Key claims

1. The resolved subgrid stress $\tau^{res}_{ij}=L_{ij}$ (Eq. 2.36), a similarity-type stress computed from the velocity on the LES mesh, contains enough information to build an autonomous, dissipative eddy-viscosity model, although similarity models used directly fail in LES (§1, §2.4). **Shown**
2. Pure similarity models used directly in LES are not dissipative enough a posteriori (citing Bardina et al. 1983; Liu et al. 1994), because they lack the information on the true subgrid scales $k>k_c$ carried by $\tau^{phy}_{ij}$ (Eq. 2.37) (§1; §2.3). **Stated**
3. Pointwise inversion (Eq. 2.46), $\nu_t=\Pi_L/\lvert\hat{\bar S}\rvert^2$, "will cause numerical instabilities", because $\Pi_L$ has regions of forward and inverse transfer that give a negative viscosity (§2.4). **Stated** (as "well known")
4. Filtering the resolved flux once more with the same filter (Eq. 2.47) "was found to be sufficient" as the physical-space substitute for spectral shell averaging (§2.4). **Shown** (by the stable runs of §3)
5. The eddy viscosity is computed from the filtered field and applied unchanged to the unfiltered LES field; no rescaling to the mesh cutoff is needed because a graded filter keeps the spectral support (§2.4). **Stated** (modelling assumption: "for two similar fields … the eddy viscosities are similar, here assumed to be the same")
6. With a sharp spectral filter at $k_c/2$, the domain average of the resolved flux equals the integrated resolved spectral transfer, $\langle\Pi_L\rangle=-T^{res}_{\mathrm{SGS}}(k_c/2)$ (Eq. 2.41). **Stated**
7. The total subgrid transfer across $k_c$ follows from the resolved transfer at the test cutoff $ak_c$, $T_{\mathrm{SGS}}(k_c)=T^{res}_{\mathrm{SGS}}(ak_c)/(1-a^{4/3})$, a factor $1.66$ for $a=1/2$ (Eq. 2.26, derived in Domaradzki 2021b from Kraichnan's ultraviolet-flux scaling, Eq. 2.27). **Stated** (derived in earlier work)
8. Forced LES ($64^3$, Gaussian filter, $k^{-5/3}$ initial spectrum, about 10 large-eddy turnover times) give late-time slopes in good agreement with $-5/3$ and a compensated Kolmogorov function $C_K(k)$ within 1.4–2.1 outside the forcing band, with minor departures near $k_c$ (§3.1, Fig. 1). **Shown**
9. Halving the resolution to $32^3$ causes "no visible deterioration" of the inertial range (§3.1, Fig. 2a). **Shown**
10. The top-hat filter instead of the Gaussian slightly overdamps the highest wavenumbers and raises intermediate-wavenumber energy; the author speculates that the more non-local Gaussian stencil is the reason (§3.1, Fig. 2b). **Shown** (the reason is speculation)
11. With a pulse initial spectrum ($E(k)=0$ for $k>4$) the steady spectrum settles at a higher energy level but the Kolmogorov function changes very little (§3.1, Fig. 3). **Shown**
12. The method assumes neither the inertial-range exponent nor the Kolmogorov constant; both are predictions, unlike the Smagorinsky or Chollet–Lesieur models, which assume them (§3.1; end of §3.3). **Stated**
13. For the Comte-Bellot & Corrsin decay ($64^3$, $k_c=30$) an under-resolved DNS without model fails, while the autonomous LES predicts the spectrum evolution "quite well" over $U_0t/M\in[42,98]$ and $[98,171]$ (§3.1, Figs. 4b, 5). **Shown**
14. LES against experiment (in parentheses) at $U_0t/M=98$: $u_{\mathrm{rms}}=1.21$ (1.28), $\varepsilon=5.58$ (6.33), $\lambda=0.0774$ (0.0764), $L=0.41$ (0.345), $Re_\lambda=63.0$ (65.3); at 171: $u_{\mathrm{rms}}=0.865$ (0.895), $\varepsilon=1.73$ (1.74), $\eta=0.0066$ (0.0066), $\lambda=0.099$ (0.102), $L=0.48$ (0.490), $Re_\lambda=57.2$ (60.7) (Table 2). **Shown**
15. The planar correlation coefficient between the subgrid transfer of the similarity stress and that of the eddy-viscosity model (Eqs. 2.42–2.47) is 0.81, "also in excess of 0.8" in 3-D, "much higher" than "the value around 0.4 found for the standard Smagorinsky model" (§3.1, Fig. 6). **Shown** (the Smagorinsky value **Stated**)
16. The model's subgrid flux contains backscatter (regions of negative $\nu_t$), yet no simulation showed "any hints of instability"; the total forward transfer exceeded backscatter by at least an order of magnitude, which the author suspects explains the stability (§3.1). **Shown** (explanation **Stated**)
17. With sharp spectral filters, forward and inverse subgrid transfers are of the same order and the net forward transfer is much smaller than either (citing Piomelli et al. 1991; Domaradzki, Liu & Brachet 1993); the correlation conclusions hold for graded filters (§3.1). **Stated**
18. In the spectral method, under-predicting the total transfer (step ix, Eq. 2.26) led to a gradual but significant loss of accuracy, reminiscent of the similarity model (citing Domaradzki 2021a) (§3.2). **Stated**
19. For graded filters no scaling result fixes the total transfer, so $C_{\mathrm A}$ in Eq. (3.3) is an adjustable constant that depends on filter and spectrum; comparing $\langle\Pi_L\rangle$ with the spectral $T_{\mathrm{SGS}}(k_c)$ for the Gaussian filter with $\hat\Delta=2\Delta x$ gives $C_{\mathrm A}\approx0.8$ for both the inertial-range and the Comte-Bellot–Corrsin fields (§3.2). **Shown**
20. With $C_{\mathrm A}=0.8$ the spectra still follow $-5/3$ with $C_K$ in 1.4–2.1 outside forcing, but $C_K$ rises steeply near $k_c$, consistent with insufficient subgrid dissipation there; the author attributes this "more likely" to the scale distribution of the transfer than to its lower total (§3.2, Figs. 7–8). **Shown**
21. For Comte-Bellot–Corrsin with $C_{\mathrm A}=0.8$ the LES at $U_0t/M=98$ over-predicts experiment at higher $k$ and under-predicts the peak at 171; the physical-space method dissipates less near the mesh cutoff than the spectral one (§3.2, Fig. 9). **Shown**
22. Against three spectral eddy viscosities (Chollet–Lesieur, Eq. 2.25; an LES-derived cusp with plateau $p_{\mathrm{pl}}=0.37$ of the cusp value; a $k$-independent viscosity matched to Eq. 2.26), the $C_{\mathrm A}=0.8$ model practically overlaps the $k$-independent one, acting as a time-dependent, spatially near-uniform viscosity; the plateau–cusp viscosity agrees best with the inertial range up to $k_c$ (§3.3, Fig. 10). **Shown**
23. Thiry, Winckelmans & Duponcheel (2019) found the spectral viscosity of the dynamic Smagorinsky model "essentially uniform over all wavenumbers", and Siegel & Domaradzki (1994) found Smagorinsky spectra approximately uniform in wavenumber (§3.3). **Stated**
24. The dynamic procedure is not useful for this method: it selects a model first and fits its coefficient, so its subgrid transfer depends on the model chosen; the local $C_{\mathrm A}(\boldsymbol x)$ from Eq. (3.5) fluctuated wildly, and the domain average gave $C_{\mathrm A}=-3.9$ with standard deviation $O(10^3)$ (§3.3). **Shown**
25. In the domain-averaged form (Eq. 3.7) the two terms involving the resolved flux are comparable in value (confirmed by direct calculation), so a large $C_{\mathrm A}$ would be needed, with excessive dissipation (§3.3, Eq. 3.7). **Derived**/**Shown**
26. The actual subgrid transfer at $k_c$ is at most a factor 1.66 larger than the resolved transfer at $k_c/2$ (citing Domaradzki 2021a), so a model's subgrid dissipation cannot differ much from the resolved transfer (§3.3). **Stated**
27. The de-aliased spectral code makes numerical dissipation negligible, so the observed effects are due entirely to the model; many finite-difference and finite-volume methods have numerical dissipation comparable to the model dissipation (§3.3). **Stated**
28. The physical-space method is unlikely to be universal: it must depend on filter type and width, unlike the sharp-spectral method, whose constants follow from LES data and theory (§4). **Stated**
29. Channel-flow results up to $Re_\tau=2000$ are announced as future work (§3.3). **Stated**

The physical-space model (Eqs. 2.36, 2.40, 2.42, 2.47, 3.3) in registry
notation, aligned with the [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
page: $\bar u_i$ is the LES velocity on the mesh and the hat the graded filter
of width $\hat\Delta=2\Delta x$ applied to it:
$$L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j,\qquad \Pi_L=-L_{ij}\hat{\bar S}_{ij},\qquad \nu_t(\boldsymbol x)=C_{\mathrm A}\,\frac{\widehat{\Pi_L}(\boldsymbol x)}{\lvert\hat{\bar S}(\boldsymbol x)\rvert^2},\qquad \tau_{ij}=-2\nu_t\bar S_{ij},$$
with $C_{\mathrm A}=1$ for the autonomous model and $\lvert\hat{\bar S}\rvert^2=2\hat{\bar S}_{ij}\hat{\bar S}_{ij}$; the trace of the model stress is ignored.

# Printed slips

- **Table 2 caption:** "after conversion using a length unit [L] = 0.1 cm", while the text (p. A48-17) sets 1 cm $=k^{min}_eL$ with $k^{min}_e=0.1$, i.e. $L=10$ cm, consistent with the printed conversions $k=10k_e$, $\nu=0.1^2\nu_e$, $E=0.1^3E_e$ and $k_c=30\leftrightarrow k_e=3$ cm$^{-1}$; the caption's unit is inverted *(compiler check, not in the sources)*.
- **Table 1:** the printed $\lambda$ does not follow from the printed definition $\lambda=(15u_{\mathrm{rms}}^2\nu/\varepsilon)^{1/2}$ with $\nu=2.5\times10^{-7}$ and the tabulated $u_{\mathrm{rms}}^2$, $\varepsilon$: recomputed 0.00338, 0.00278, 0.00262, 0.00319, 0.00261, 0.00238 against printed 0.00359, 0.00274, 0.00268, 0.00321, 0.00271, 0.00241 (deviations up to about 6%), while the printed $Re_\lambda$ follows from the printed $\lambda$ *(compiler check, not in the sources)*.
- **Table 2, first LES row ($U_0t/M=51$):** the same definition with $u_{\mathrm{rms}}=1.93$, $\varepsilon=17.7$, $\nu=0.0015$ gives $\lambda\approx0.0688$ against printed 0.0643 *(compiler check, not in the sources)*.
- **Reference list:** "Heilderberg" (Chollet 1984); "Phys. Fluids 3" (Germano et al. 1991) and "Phys. Fluids 4" (Lilly 1992) without the series letter.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u^<$ (LES field, projection on the mesh, sharp cutoff $k_c=\pi/\Delta x$) | $\bar u$ | as on the concept page; the source's $<$ marks the *resolved* field, the opposite of the registry's $\phi^<$ |
| $u^>$ (true subgrid scales, $k>k_c$) | $u^<$ | unresolved part |
| $\bar f$ (graded Gaussian or box filter, $\Delta=2\Delta x$) | $\bar f$ on the full field (Eqs. 1.1–1.2); $\hat f$, $\hat\Delta=2\Delta x$, when applied to the LES field | so $\bar u^<\to\hat{\bar u}$ |
| $\hat f$ (Liu et al. test filter, Eq. 1.4) | $\hat f$ | used only in the recalled Eq. (1.4) |
| $u'_i=u_i-\bar u_i$ | subfilter velocity | **collision:** the prime is the registry's Reynolds fluctuation |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | positive trace, full tensor |
| $\tau^{res}_{ij}$ | $L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j$ | resolved (similarity-like) stress |
| $\tau^{full}_{ij}$, $\tau^{phy}_{ij}$, $\tau^{sim}_{ij}$ | same, page-local | full, true-subgrid and Bardina stresses |
| $S^<_{ij}$, $\bar S^<_{ij}$; $(\bar S^<_{ij})^2$ | $\bar S_{ij}$, $\hat{\bar S}_{ij}$; $\tfrac12\lvert\hat{\bar S}\rvert^2$ | the source's square has no factor two |
| $\epsilon_{SGS}=\tau_{ij}\bar S_{ij}$, $\epsilon^{res}_{SGS}$, $\bar\epsilon^{res}_{SGS}$ | $-\Pi$, $-\Pi_L$, $-\widehat{\Pi_L}$ | **sign collision:** the source's flux is negative for forward transfer; $\Pi_L$ page-local |
| $\nu_{eddy}(\boldsymbol x)$, $\nu^{(C)}_{eddy}$ | $\nu_t$ | |
| $C$ (Eq. 3.3) | $C_{\mathrm A}$ | page-local; not the Smagorinsky $C_s$ |
| $\nu_{eddy}(k\mid k_c)$ | $\nu_t(k\mid k_c)$ | spectral eddy viscosity |
| $T_{SGS}(k\mid k_c)$, $T_{SGS}(k_c)$, $T^{res}_{SGS}$ | same, page-local | spectral subgrid transfer (negative for a drain) |
| $C_K$, $C_K(k)$ | same, page-local | Kolmogorov constant; compensated spectrum $E(k)/(\varepsilon^{2/3}k^{-5/3})$ |
| $C_m$, $f_1$, $a$, $D$, $p$ | same; $p_{\mathrm{pl}}$ for $p$ | spectral-model coefficient and shape, test-cutoff ratio $1/2$, $D=1/(1-a^{4/3})$, plateau fraction |
| $N$ | $N_x$ | **collision** with the polynomial degree |
| $u'$ (rms velocity), $L_{int}$, $T_e$ | $u_{\mathrm{rms}}$, $L$, $T_E$ | page-local $u_{\mathrm{rms}}$; $T_E$ the large-eddy turnover time of registry §11 |
| $\varepsilon$, $\lambda$, $Re_\lambda$, $\eta$ | same | |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | shell average or average over all mesh points |

# Reference list

47 printed references in JFM author–year style, alphabetical, merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works are keyed in printed order (Domaradzki 2021a/b; Domaradzki &
Adams 2002 and Domaradzki, Loh & Yee 2002; Ghosal et al. 1995 and Ghosal & Moin
1995; Kraichnan 1971a/b). Rogallo (1981) is printed without a title (NASA TM
81315). No cited work is an ingested source; all items parsed.

# Pages created or updated

Chunk 5 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
