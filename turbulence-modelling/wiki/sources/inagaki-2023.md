---
type: Source
title: "Inagaki & Kobayashi (2023) — Analysis of anisotropic subgrid-scale stress for coarse large-eddy simulation"
description: "Splits the filtered-DNS subgrid stress of channel flow at Re_tau 400 into an energy-matching eddy-viscosity part and an energy-transfer-free anisotropic stress, and shows from the resolved Reynolds-stress budgets, physical and spectral, that on coarse grids the anisotropic stress produces spanwise fluctuations no eddy viscosity can supply."
resource: "doi:10.1103/physrevfluids.8.104603"
source_kind: paper
authors: [Inagaki K., Kobayashi H.]
year: 2023
venue: "Phys. Rev. Fluids 8:104603"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Physical_Review_Fluids_Inagaki_Analysis_of_anisotropic_subgrid-scale_stress_for_coarse_larg.pdf"
tags: [les, sgs-model, anisotropy, eddy-viscosity, a-priori-a-posteriori, grid-requirements]
timestamp: 2026-10-26T07:41:00Z
---

# Summary

Inagaki & Kobayashi (2023) ask what the part of the subgrid-scale stress
that transfers no energy between resolved and subgrid scales does in
[LES](/definitions/large-eddy-simulation.md) of wall-bounded flow, and why
it matters most on coarse grids. Following Abe (2019) and their own 2020
paper, they split the deviatoric SGS stress of filtered
[DNS](/definitions/direct-numerical-simulation.md) into an eddy-viscosity
term and an "anisotropic" remainder. The eddy viscosity is chosen to
reproduce the local energy flux $\Pi$ exactly and can be negative
([backscatter](/definitions/energy-backscatter.md)); the remainder
$\tau^{\mathrm{ani}}_{ij}$ satisfies $\tau^{\mathrm{ani}}_{ij}\bar S_{ij}=0$.
In the budget of the resolved Reynolds stress, the split separates the SGS
dissipation into an eddy-viscosity dissipation and an "anisotropic
redistribution". A spectral version of the budget, over streamwise and
spanwise wavenumbers, adds an interscale transfer term.

The data are an in-house DNS of [channel flow](/benchmarks/turbulent-channel-flow.md)
at $Re_\tau=400$, filtered with a sharp cutoff in $x$ and $z$ at a
"medium" and a "coarse" resolution. For the medium filter the anisotropic
stress is negligible in the mean shear stress and in the kinetic-energy
budget, so an eddy viscosity suffices
([Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). For the
coarse filter the anisotropic stress is comparable to the eddy-viscosity
part, and its redistribution is productive near the wall. The spanwise
component is productive everywhere and peaks at the streak spacing, from
which the authors infer a role in generating streamwise vortices. An
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) test of
three energy-transfer-free models favours the
[scale-similarity](/methods/scale-similarity-model.md) form of the
stabilized mixed model over the [Clark gradient model](/methods/gradient-model.md);
a quadratic strain–rotation model gives the wrong sign. An a posteriori
[dynamic](/methods/dynamic-procedure.md)
[Smagorinsky](/methods/smagorinsky-model.md) LES confirms that the medium
grid predicts the mean velocity and the coarse one does not
([grid-point requirements](/results/les-grid-point-requirements.md)).
The [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
of Agrawal et al. (2022) is cited among the anisotropic models that improve
statistics.

# Version read

arXiv preprint arXiv:2301.12672v3 [physics.flu-dyn], 5 September 2023
("Dated: September 6, 2023"), single-column layout, 40 pages, all read;
the equations on pp. 6–8, 10–11 and 27–28 were also checked visually. Not
the APS version of record. Page-1 title and authors match the metadata; no
identity problem. Equation, figure, table and section numbers on this page
are those of this version.

# Key claims

The decomposition (Eqs. 3–5) reads, in registry notation,
$\tau^d_{ij}=-2\nu_t\bar S_{ij}+\tau^{\mathrm{ani}}_{ij}$ with
$\nu_t=-\tau_{ij}\bar S_{ij}/(2\bar S_{kl}\bar S_{kl})=\Pi/\lvert\bar S\rvert^2$,
and the SGS dissipation tensor of the resolved Reynolds-stress budget
splits as $\varepsilon^{\mathrm{SGS}}_{ij}=\varepsilon^{\mathrm{EV}}_{ij}-\xi^{\mathrm{AR}}_{ij}$,
$\xi^{\mathrm{AR}}_{ij}=\langle\tau^{\mathrm{ani}}_{il}\partial_l\bar u'_j+\tau^{\mathrm{ani}}_{jl}\partial_l\bar u'_i\rangle$
(Eqs. 8–9), where $\bar u'_i=\bar u_i-\langle\bar u_i\rangle$ and
$\bar S'_{ij}$ is its strain rate.

1. The anisotropic term does not contribute to the local resolved–subgrid energy transfer, $\tau^{\mathrm{ani}}_{ij}\bar S_{ij}=0$, and the eddy viscosity of Eq. (4) can be negative (local backscatter) (§II A). **Derived**
2. Unlike the pressure redistribution, the anisotropic redistribution is not traceless: $\xi^{\mathrm{AR}}_{ii}=2\langle\tau^{\mathrm{ani}}_{ij}\bar S'_{ij}\rangle\neq0$, and $\langle\tau^{\mathrm{ani}}_{ij}\bar S_{ij}\rangle=0$ gives $\xi^{\mathrm{AR}}_{ii}=-\langle\tau^{\mathrm{ani}}_{ij}\rangle\langle S_{ij}\rangle$; with $\partial_y\langle u\rangle>0$, $\langle\tau^{\mathrm{ani}}_{12}\rangle<0$ makes the trace productive and $\langle\tau^{\mathrm{ani}}_{12}\rangle>0$ dissipative (§II C, Eq. 10). **Derived**
3. A stochastic forcing $a_i$ added to the filtered momentum equation contributes nothing to the resolved Reynolds-stress budget, $\langle\bar u'_ia_j\rangle=0$, so a deterministic model is needed to reproduce the productive contribution (§IV B). **Derived**
4. For the medium filter $k_{\mathrm{res}}/k_{\mathrm{tot}}\gtrsim0.9$ across the channel; for the coarse filter $k_{\mathrm{res}}/k_{\mathrm{tot}}<0.8$ for $y^+<100$ (§III B, Fig. 1). **Shown**
5. For the medium filter the resolved wall-normal fluctuation is less than 80% of the unfiltered one for $y^+<50$; the authors suggest that $\Delta z^+<20$ may be needed to predict the near-wall anisotropy (§III B, Fig. 2). **Shown** (ratio) / **Stated** (requirement)
6. For the coarse filter half of the peak of the streamwise spectrum at $y^+\approx15$ is filtered out, and most of the wall-normal and shear spectra lie in the subgrid scales (§III B, Fig. 2). **Shown**
7. For the medium filter the anisotropic part of the mean SGS shear stress is negligible, so eddy-viscosity models can predict both the energy transfer and the mean SGS shear stress; for the coarse filter the anisotropic stress is comparable to the eddy-viscosity term (§III C, Fig. 3). **Shown**
8. In the resolved kinetic-energy budget $\xi^{\mathrm{AR}}$ is negligible for the medium filter and positive near the wall for the coarse filter; for the coarse filter the total SGS dissipation is productive (averaged backscatter) at $y^+\approx12$ and the eddy-viscosity dissipation at $y^+\approx10$ (§III D, Fig. 4). **Shown**
9. For the medium filter the wall-normal and spanwise components of $\xi^{\mathrm{AR}}_{ij}$ almost cancel; for the coarse filter the streamwise and spanwise components contribute positively around $y^+\approx20$ and the spanwise one dominates in $50<y^+<100$; $\xi^{\mathrm{AR}}_{33}$ is positive everywhere for both filters (§III D, Fig. 5). **Shown**
10. In the budget of $R^{\mathrm{res}}_{22}$, $\xi^{\mathrm{AR}}_{22}$ is a large negative contribution, compared with the viscous and eddy-viscosity dissipations, for $y^+<50$; the SGS diffusion balances pressure and turbulent diffusion for $y^+<100$ (§III E 2, Fig. 7). **Shown**
11. In the budget of $R^{\mathrm{res}}_{33}$, which has no production, the SGS dissipation is productive near $y^+\approx20$ for both filters; for the coarse filter $\xi^{\mathrm{AR}}_{33}$ is comparable to the pressure redistribution for $y^+<100$ and is called "indispensable" for the resolved spanwise fluctuation; for the medium filter its absence is inferred to cause the underestimated spanwise fluctuation (§III E 3, Fig. 8). **Shown** (budget) / **Stated** (inference)
12. In the spectral streamwise budget at $y^+\approx15$ for the coarse filter, $\xi^{\mathrm{AR}}_{11}$ is positive for $k_x^+>0.01$ ($\lambda_x^+\lesssim600$) and feeds $k_x^+>0.015$, where the interscale transfer moves energy from $k_x^+<0.01$, $0.02<k_z^+<0.06$ to $k_z^+<0.03$; for $k_x^+>0.015$, $k_z^+>0.04$ it slightly exceeds the interscale transfer, which the authors read as a streak-breakdown-like contribution (§IV A 1, Figs. 9–10). **Shown** / interpretation **Stated**
13. In the spectral spanwise budget at $y^+\approx15$ the interscale transfer of the spanwise spectrum is negative at $k_z^+=0.04$ and positive for $k_z^+<0.02$ (inverse transfer in spanwise scale) for both filters; for the medium filter it changes sign at $k_z^+\approx0.08$ ($\lambda_z^+\approx80$), larger than the critical $r_z^+\approx20$ of Cimarelli & De Angelis and of Hamba (with $\lambda_z=2r_z$), a shift attributed to the filtered-out small scales; for the coarse filter the forward cascade of the spanwise spectrum is unresolved (§IV A 2, Fig. 11). **Shown**
14. For both filters the positive spectral $\xi^{\mathrm{AR}}_{33}$ exceeds the eddy-viscosity dissipation at all wavenumbers (§IV A 2, Fig. 11). **Shown**
15. The spectral pressure redistribution of the spanwise component is negative for $k_x^+<0.005$, $k_z^+>0.04$ ($\lambda_x^+\gtrsim1200$, $\lambda_z^+\lesssim160$), the scale of streamwise vortices, where $\xi^{\mathrm{AR}}_{33}$ is positive and peaks at $k_z^+\approx0.05$ ($\lambda_z^+\approx130$), the streak spacing. The authors infer that the anisotropic SGS stress takes part in generating streamwise vortices, a mechanism lost with a pure eddy-viscosity model, and that the spanwise filter is more critical than the streamwise one (§IV A 2, Fig. 12). **Shown** / inference **Stated**
16. A priori for the coarse filter, all three anisotropic-stress models give a positive $\xi^{\mathrm{AR}}_{11}$ but miss the near-wall negative filtered-DNS value; the scale-similarity ("SGS-Reynolds") model is closest, the Clark model differs, and the variants without the energy-removing viscosity $\nu^{\mathrm a}$ are strongly negative (§IV B, Fig. 13a). **Shown**
17. With the dynamic Smagorinsky eddy viscosity (Eq. 22) in place of Eq. (4) ("AR-DSM"), the anisotropic contribution at $y^+\approx40$ is about $-0.02$, half the filtered-DNS eddy-viscosity dissipation there, so the total SGS dissipation of $R^{\mathrm{res}}_{11}$ is twice the dynamic-Smagorinsky estimate: the dynamic model is less dissipative than the ideal eddy viscosity (§IV B). **Shown**
18. All models predict $\xi^{\mathrm{AR}}_{22}$ well, with or without $\nu^{\mathrm a}$; for $\xi^{\mathrm{AR}}_{33}$ the quadratic strain–rotation ("SW") model has the opposite sign to filtered DNS, and the scale-similarity and Clark models have the right sign but a small magnitude; the scale-similarity model stays positive even without $\nu^{\mathrm a}$ (§IV B, Fig. 13b,c). **Shown**
19. Whatever the eddy-viscosity model, the anisotropic stress contributes significantly to the budgets of coarse-grid LES, and models with the $\nu^{\mathrm a}$ correction generally do better (§IV B). **Shown** (a priori) / **Stated** (generalization)
20. In a posteriori dynamic-Smagorinsky LES at $Re_\tau=400$, the fine $(\Delta x^+,\Delta z^+)=(26.2,13.1)$ and medium $(52.4,26.2)$ grids predict the DNS mean velocity and the coarse $(105,52.4)$ grid overestimates it; the medium grid overestimates $R^{\mathrm{res}}_{11}$ and $R^{\mathrm{res}}_{12}$ and underestimates the wall-normal and spanwise components, trends stronger on the coarse grid (App. C, Figs. 16–17, Table I). **Shown**
21. The wall-normal component of the SGS diffusion is set by the anisotropic-stress diffusion (its eddy-viscosity part is negligible); for the spanwise component the eddy-viscosity diffusion has the opposite sign (App. A, Fig. 14). **Shown**
22. From the literature: Cimarelli & De Angelis require filter lengths $\Delta_x^+<100$, $\Delta_z^+<20$ for eddy-viscosity models to resolve the interscale interaction including the spanwise inverse cascade; typical eddy-viscosity LES uses $\Delta_x^+<130$, $\Delta_z^+<30$ (refs [27–29]) (§II D). **Stated**

# Printed slips

1. Eq. (7d) prints the pressure diffusion as $-\partial_\ell\langle\overline p^{\rm total}\overline u'_j\delta_{i\ell}+\overline p^{\rm total}\overline u'_j\delta_{i\ell}\rangle$: the second term repeats the first instead of the $i\leftrightarrow j$ counterpart. The spectral form (14d) repeats the duplication.
2. Eq. (7f) prints $\langle\overline s'_{i\ell}\overline u'_j+\overline s'_{j\ell}\overline u'_j\rangle$, the second term with $\overline u'_j$ instead of $\overline u'_i$; Eq. (14f) repeats it and writes the derivative "$\partial/\partial x_y$".
3. Eq. (12) prints $E^{\rm GS}_{ij}=\Re\langle\tilde{\overline u}'_i\tilde{\overline u}'^*_i\rangle$, with index $i$ twice; the Fig. 2 caption has the $j$.
4. Eq. (14h): the second term prints $\tilde\tau^{\rm sgs}_{j\ell}$ where the first has $\tilde\tau^{\rm sgs}_{iy}$ under $\partial/\partial y$.
5. Eqs. (18a,b) are printed without the real part that Eq. (14g) carries; Eq. (16) writes $\check T_{ij}$ without the GS superscript.
6. §II C, after Eq. (10): "For unidirectional turbulent shear flows as channel flows, it reads $\langle\tau^{\rm ani}_{xy}\rangle\partial U_x/\partial y/2$". With $S_{xy}=S_{yx}=\tfrac12\partial U_x/\partial y$ the contraction $\langle\tau^{\rm ani}_{ij}\rangle S_{ij}$ is $\langle\tau^{\rm ani}_{xy}\rangle\partial U_x/\partial y$, without the factor $\tfrac12$; the sign conclusions are unaffected *(compiler check, not in the sources)*.
7. §V refers to "Appendix B" for the LES showing that the eddy-viscosity model fails on the coarse grid; the LES is in Appendix C.
8. The Fig. 17(d) legend reads "fine DNS / medium DNS / coarse DNS" where panels (a)–(c) read "fDNS".

# Notation map

| Inagaki & Kobayashi (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline{(\cdot)}$, $\overline\Delta_\alpha$ | $\bar\phi$, $\Delta_\alpha$ (directional filter length) | sharp cutoff in $x$ and $z$ only; cutoff wavelength $2\Delta$ |
| $\widehat{(\cdot)}$, $\widehat{\overline\Delta}/\overline\Delta=2$ | $\hat\phi$, $\hat\Delta/\Delta=2$ | test filter |
| $\langle\cdot\rangle$, $\langle\cdot\rangle_{\mathrm S}$ | $\langle\cdot\rangle$ | plane and time average; $x$–$z$ plane average in the dynamic procedure |
| $U_i$, $Q=\langle\overline q\rangle$ | $\langle u_i\rangle$ | with this filter $\langle\bar q\rangle=\langle q\rangle$ |
| $\overline q'=\overline q-Q$ | $\bar u'_i=\bar u_i-\langle\bar u_i\rangle$ (resolved fluctuation) | |
| $\tau^{\mathrm{sgs}}_{ij}=\overline{u_iu_j}-\overline u_i\overline u_j$ | $\tau_{ij}$ | positive trace, full tensor |
| $\tau^{\mathrm{sgs}}_{ij}\vert_{\mathrm{tl}}$ | $\tau^d_{ij}$ | traceless part |
| $\overline p^{\mathrm{total}}=\overline p+\tau^{\mathrm{sgs}}_{mm}/3$ | (modified pressure) | kinematic |
| $\overline s_{ij}$, $\overline s^2=\overline s_{ij}\overline s_{ij}$ | $\bar S_{ij}$, $\lvert\bar S\rvert^2/2$ | the source's $\overline s^2$ has no factor two; $\sqrt{2\overline s^2}=\lvert\bar S\rvert$ |
| $\overline w_{ij}$ | $\bar\Omega_{ij}$ | |
| $S_{ij}$ | $\langle S_{ij}\rangle$ | mean strain rate |
| $\nu^{\mathrm{sgs}}$ | $\nu_t$ | the energy-matching ("ideal") eddy viscosity of Eq. (4), or the dynamic one in AR-DSM |
| $\tau^{\mathrm{ani}}_{ij}$, $\tau^{\mathrm a}_{ij}$, $\nu^{\mathrm a}$ | (anisotropic SGS stress, model base tensor and its energy-removing viscosity; page-local) | |
| $R^{\mathrm{GS}}_{ij}=\langle\overline u'_i\overline u'_j\rangle$ | $R^{\mathrm{res}}_{ij}$ | positive trace |
| $K^{\mathrm{GS}}$, $K$ | $k_{\mathrm{res}}$, $k_{\mathrm{tot}}$ | $k_{\mathrm{tot}}=k_{\mathrm{res}}+\langle\tau_{ii}\rangle/2$ |
| $P^{\mathrm{GS}}_{ij}$, $\varepsilon^{\mathrm{GS}}_{ij}$, $\Phi^{\mathrm{GS}}_{ij}$, $D^{\mathrm{p,t,v,GS}}_{ij}$ | (production, dissipation, pressure redistribution, pressure, turbulent and viscous diffusion of $R^{\mathrm{res}}_{ij}$) | **collision:** $\Phi$ is not a filter |
| $\varepsilon^{\mathrm{SGS}}_{ij}$, $\varepsilon^{\mathrm{EV}}_{ij}$, $D^{\mathrm{SGS}}_{ij}$, $D^{\mathrm{EV}}_{ij}$, $D^{\mathrm{AS}}_{ij}$ | (SGS dissipation and its eddy-viscosity part; SGS, eddy-viscosity and anisotropic-stress diffusion; page-local) | $\varepsilon^{\mathrm{SGS}}>0$ is a sink |
| $\xi^{\mathrm{AR}}_{ij}$ | $\xi^{\mathrm{AR}}_{ij}$ (anisotropic redistribution, page-local) | **collision:** not a reference coordinate; positive = productive |
| $\tilde q$, $^*$, $\Re$ | $q_{\boldsymbol k}$, complex conjugate, real part | **collision:** the tilde is a Fourier coefficient, not a Favre filter |
| $\check A_{ij}$, $E^{\mathrm{GS}}_{ij}(k_x,y,k_z)$, $\check T^{\mathrm{GS}}_{ij}$ | (spectral density of a budget term, resolved Reynolds-stress spectrum, interscale transfer; page-local) | $\sum\check T_{ij}=0$ |
| $k_x$, $k_z$, $\lambda_\alpha=2\pi/k_\alpha$ | (streamwise and spanwise wavenumbers and wavelengths) | **collision:** $k$ is not the kinetic energy |
| $h$, $Re_\tau=u_\tau h/\nu$ | $\delta$, $Re_\tau$ | channel half-width |
| $C$ | $C_s^2$ | dynamic coefficient, $\nu_t=C\Delta^2\lvert\bar S\rvert$, clipped at zero |
| $a_i$ | (stochastic forcing, §IV B) | |
| $r_z$ | (spanwise separation of structure-function analyses) | $\lambda_z=2r_z$ |

# Reference list

50 printed references, numbered style, all parsed; no DOIs are printed. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. No printed duplicates and no same-author same-year
pairs. Ref. [9] is the bundle's Source
[agrawal-2022](/sources/agrawal-2022.md). Ref. [23] (Bardina et al. 1983,
Stanford report TF-19) is a technical report, refs. [32] and [34] are
books, and ref. [49] prints the title "Direct numerical simulation of
turbulent channel up to Reτ = 590" without "flow", recorded as printed.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunk 6. This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Super-resolution subgrid-scale models](/methods/super-resolution-sgs-model.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
