---
type: Source
title: "Zhang et al. (2023) — Large-eddy simulation of the Darmstadt multi-regime turbulent flame using flamelet-generated manifolds"
description: "LES of the stratified Darmstadt multi-regime burner flame MRB26b with flamelet-generated manifolds in OpenFOAM: premixed and counter-flow databases, presumed-PDF and dynamically thickened closures, a piecewise flame sensor, and a minor-species correction for thickening and wrinkling loss."
resource: "doi:10.1016/j.combustflame.2023.113001"
source_kind: paper
authors: [Zhang W., Han W., Wang J., Huang Z., Jin W., van Oijen J.]
year: 2023
venue: "Combust. Flame 257:113001"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Combustion_and_Flame_Zhang_Large-eddy_simulation_of_the_Darmstadt_multi-regime_turbulen.pdf"
tags: [combustion, les, tabulated-chemistry, dynamic-procedure]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Zhang et al. (2023) simulate the Darmstadt multi-regime burner flame
MRB26b (stratified CH$_4$/air, a TNF-workshop target; rich central jet,
air slot, lean slot, air coflow) by
[large-eddy simulation](/definitions/large-eddy-simulation.md) with
flamelet-generated manifolds ([flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md))
in [OpenFOAM](/software/openfoam.md). Mixture fraction $Z$ and progress
variable $Y_c=Y_{\mathrm{CO_2}}+Y_{\mathrm{H_2O}}$ are transported at unit
Lewis number; three databases are built with CHEM1D and GRI-Mech 3.0:
free-propagating premixed flamelets (FP), counter-flow diffusion
flamelets (CF-Diff) and counter-flow flamelets against a rich premixed
mixture (CF-PaPre). The subgrid viscosity is the dynamic
[Smagorinsky model](/methods/smagorinsky-model.md)
([dynamic procedure](/methods/dynamic-procedure.md)); the mesh is
qualified on cold flow by the Pope criterion; inlet turbulence comes from
precursor pipe and annular-pipe flows
([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
Two combustion closures are compared: a presumed PDF ($\beta$-PDF in $Z$,
top-hat in $Y_c$, gradient-model variances) and the dynamically
[thickened flame model](/methods/thickened-flame-model.md) with a new
piecewise flame sensor.

All databases and closures give similar mean velocity, temperature,
mixture fraction and major species, in agreement with experiment. CO and
H$_2$ are over-predicted in the inner multi-regime zone with the premixed
database and improved by the counter-flow ones, which the authors
attribute to species diffusion along $Z$ and to strain in the tabulation;
transporting CO and H$_2$ with a linearized consumption source also
repairs the premixed database. The thickened flame over-predicts CO and
H$_2$ in the outer premixed zone, with a lower rms of $Y_c$ than the
presumed PDF; the authors attribute it to thickening combined with loss
of resolved wrinkling, and derive from species-mass conservation the
correction $Y^{\mathrm c}_{\mathrm{CO}}=Y_{\mathrm{CO}}\,\Xi_\Delta/F$,
the Gruhlke et al. form with $a=1$, $b=0$, which brings the thickened
results close to the presumed PDF. Regime statistics (flame index) and
propagation directions are similar for all databases; downstream the
premixed share is over-predicted against experiment.

# Version read

Version of record (Combust. Flame 257:113001, Elsevier; received 16 Sep
2022, revised and accepted 3 Aug 2023, online 18 Aug 2023), 16 pages,
all read; equations on pp. 3, 5, 11 and 14 checked visually. Page-1
title, six authors, venue and DOI match the metadata; no identity
problem. Numbering on this page is that of this version.

# Key claims

The source's $\mathcal Y$ is $Y_c$; its flame sensor $\Omega$ is
$\Omega_{\mathrm{fs}}$; $\delta_L^0$ and $s_L^0$ are $l^0_{\mathrm F}$ and
$s_{\mathrm L}$; $\Delta_{mesh}$ (cube root of the cell volume) is
$\Delta$; $\tilde Z_v$, $\tilde{\mathcal Y}_v$ are the subgrid variances
$Z_v$, $Y_{c,v}$; $\langle\cdot\rangle$ is a time average.

1. The cold-flow mesh (about 3.87 million hexahedra) satisfies the Pope criterion: $M_E=\langle k_{\mathrm{sgs}}/(k_{\mathrm{sgs}}+k_{\mathrm{res}})\rangle$ is generally below 0.2 within $0<x<100$ mm, $|r|<40$ mm, so at least 80% of the turbulent kinetic energy is resolved, $k_{\mathrm{sgs}}$ coming from the dynamic Smagorinsky model (§2, Eqs. 1–2, Fig. 2b). **Shown**
2. The databases (FP, CF-Diff, CF-PaPre) and closures (presumed PDF, thickened flame) give very similar mean axial velocity, temperature, mixture fraction and CH$_4$, O$_2$, CO$_2$, H$_2$O, in good agreement with experiment (§4.1.1, Fig. 6). **Shown**
3. In the recirculation zone between the two slots (especially $x=6$ mm) O$_2$ is slightly over-predicted and CO$_2$, H$_2$O and $\tilde Z$ under-predicted, attributed to the unit-Lewis-number assumption with reference to the authors' earlier work (§4.1.1, Fig. 6). **Stated** (attribution not tested here)
4. With the FP database and the thickened flame, reactants are over-consumed around the outer reaction zone at $x=30$ and 60 mm (higher temperature, over-predicted CO$_2$, H$_2$O), attributed to an over-predicted turbulent flame speed; Popp et al. observed a similar over-prediction (§4.1.1, Fig. 6). **Shown** (cause **Stated**)
5. CF-Diff and CF-PaPre results are very close because both have pure air on one side and a mixture far beyond the rich limit on the other (§4.1.1). **Stated**
6. Even the outer premixed zone ($\phi_{\mathrm{eq}}=0.8$) is well predicted with the counter-flow databases, because steady plus unsteady counter-flow flamelets give control-variable bounds similar to FP and local combustion at low strain is close to premixed (§4.1.1, Fig. 6). **Shown** / **Stated**
7. With the FP database CO and H$_2$ are over-predicted in the inner reaction zone, especially downstream; the counter-flow databases improve them (§4.1.2, Fig. 7). **Shown**
8. Scatter plots of $\tilde Z$ against $\tilde Y_c$ at $x=15$, 30, 60 mm are similar for FP and CF-PaPre while the conditional means of CO and H$_2$ differ (FP much higher at larger $\tilde Z$ in the inner zone): the tabulation, not the control-variable field, is responsible (§4.1.2, Figs. 8–10). **Shown**
9. In the counter-flow databases species diffusion along $Z$ lowers CO and H$_2$ in the richer region compared to FP (Fig. 11); strain further reduces their production, as shown by Han et al. (§4.1.2). **Shown** (databases) / **Stated** (strain)
10. Transporting CO and H$_2$ with the FP database and a linearized, locally adaptive consumption source (Eq. 7) brings their conditional means close to the counter-flow database (§4.1.2, Figs. 7, 9, 10, 12). **Shown**
11. In the outer premixed zone ($\phi_{\mathrm{eq}}=0.8$, $Z\approx0.0446$) minor-species distributions are nearly the same in the FP and counter-flow databases, and both predict CO and H$_2$ well there (§4.1.2, Fig. 11). **Shown**
12. H$_2$ behaves like CO for MRB26b; H$_2$ had not been reported for this flame before (§4.1.2). **Shown**
13. The thickened flame over-predicts CO and H$_2$ near the outer premixed zone, as Popp et al. also observed (§4.2.1, Fig. 12). **Shown**
14. Mean and rms $\tilde Z$ and mean $\tilde Y_c$ are well predicted by both closures at $x=6$, 15, 22.5 mm around the outer zone; the rms of $\tilde Y_c$ is lower with the thickened flame (§4.2.1, Fig. 13). **Shown**
15. The lower rms of $\tilde Y_c$ indicates wrinkling loss from artificial thickening; instantaneous reaction layers are more wrinkled with the presumed PDF (§4.2.1, Fig. 14). **Shown**
16. Downstream (especially $x=60$ mm) the thickened-flame rms of $\tilde Y_c$ approaches the presumed-PDF one and the CO, H$_2$ deviations shrink, which the authors take as support for the wrinkling-loss explanation (§4.2.1, Figs. 12, 14). **Shown**
17. The thickened flame under-predicts the rms of major species and temperature at $x=6$ mm in the outer zone while their means are unaffected, because major species sit mainly in unburned and burned gas and intermediates in the reaction zone (§4.2.1, Fig. 15). **Shown** / **Stated** (reason)
18. The minor-species over-prediction of the thickened flame is a combined effect of thickening and wrinkling loss, whereas earlier studies addressed only one of the two (§4.2.2). **Stated**
19. Species-mass conservation between the thickened resolved front (thickness $Fl^0_{\mathrm F}$, area $A_{\mathrm{res}}$) and the thin wrinkled laminar front (thickness $l^0_{\mathrm F}$, area $\Xi_\Delta A_{\mathrm{res}}$), with the front-mean $Y^*_{\mathrm{CO}}$ of Eq. (17), gives $Y^{\mathrm c}_{\mathrm{CO}}=Y_{\mathrm{CO}}\,\Xi_\Delta/F$ (Eqs. 17–19), and likewise for H$_2$. **Derived**
20. Eq. (19) is the Gruhlke et al. correction $Y^{\mathrm c}_{\mathrm{CO}}=Y_{\mathrm{CO}}(a\Xi_\Delta+b)/F$ with $a=1$, $b=0$, called "properly acceptable" (§4.2.2). **Derived**
21. Corrected thickened-flame CO and H$_2$ in the outer premixed region are much improved and very close to the presumed PDF; the inner-zone improvement is slight because the correction is premixed-based (§4.2.2, Fig. 17). **Shown**
22. The correction is not needed for major species; Gruhlke et al. showed theirs influences major species little; not tested further (§4.2.2). **Stated**
23. The three databases give similar regime distributions by the flame index $G_{\mathrm{FO}}=\nabla\tilde Y_{\mathrm{CH_4}}\cdot\nabla\tilde Y_{\mathrm{O_2}}/(|\nabla\tilde Y_{\mathrm{CH_4}}||\nabla\tilde Y_{\mathrm{O_2}}|)$ (Eq. 20, Table 2) in the inner zone: non-premixed combustion is rare, multi-regime combustion dominates, and the premixed share grows downstream and decreases for $x>75$ mm (§4.3, Fig. 18). **Shown**
24. Downstream the simulations predict more premixed than multi-regime combustion, unlike the experiment, seemingly through faster dilution of the rich mixture (§4.3). **Shown**
25. Back-supported flames (alignment angle of $\nabla\tilde Z$ and $\nabla\tilde Y_c$ below 90°) prevail upstream and front-supported flames downstream, as in experiment (§4.3, Fig. 19). **Shown**
26. Adding the $\beta$-PDF variance dimension (11 points in $Z_v$) increases the database size "10 times (to about 591 Mb)" (§3.3). **Stated**
27. Time step 0.32 μs, CFL about 0.4; 20 flow-through times after ignition, then 20 of statistics (§3.4). **Stated**

# Printed slips

- **§3.2:** the FP flamelets span "0.4⩽ φ ⩽ φslot1 =2.6", with "Zslot1 ≈0.132", and the CF-PaPre fuel side is a "premixed CH4/air mixture at φslot1=2.6", while §2 defines $\phi_{\mathrm{slot1}}=0$ and $\phi_{\mathrm{jet}}=2.6$; §4.1.2 prints $Z\approx0.0446$ at $\phi_{\mathrm{slot2}}=0.8$. The paper prints no relation between $Z$ and $\phi_{\mathrm{eq}}$.
- **§3.3:** "11 grid points were assigned to $\tilde Z_v$" and "the database size is increased 10 times".
- **§3.3:** the gradient variance model is printed $\tilde Z_v=\alpha\Delta_{mesh}(\nabla\tilde Z)^2$ (likewise for $\mathcal Y$), with $\Delta_{mesh}$ to the first power. *(compiler check, not in the sources)* $Z$ is dimensionless and $\Delta_{mesh}$ a length, so the printed right-hand side has the dimension of an inverse length; a dimensionless variance needs $\Delta^2$.
- **App. A:** the constants $C_k$ and $b$ of Eqs. (A.1)–(A.4) are given no value anywhere in the paper.
- **References:** ref. [29] is printed with the placeholder volume "0 0 0 (2020) 1–10"; ref. [5] title "Liminar"; ref. [32] a stray "1" in the author list; ref. [11] no volume.
- **Typos:** "a pr ior analysis" (§4.1.1, §4.1.2), "winkling factor" (§4.1.1, §4.2.2), "staining rate" (§4.1.1), "Imaging that" (§4.2.2), "As a results" (§4.1.2).

# Notation map

| Zhang et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\cdot$, $\tilde\cdot$ | $\bar\cdot$, $\tilde\cdot$ | spatial filter and Favre filter, agree |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time average, agree |
| $k_{sgs}$, $k_{res}$, $M_E$ | $k_{\mathrm{sgs}}$, $k_{\mathrm{res}}$, (Pope-criterion ratio) | $M_E$ page-local |
| $\mathcal Y$ | $Y_c$ | unnormalized progress variable, as on the tabulated-chemistry page |
| $Z$, $\tilde Z_v$, $\tilde{\mathcal Y}_v$ | $Z$, $Z_v$, $Y_{c,v}$ | Bilger mixture fraction; subgrid variances |
| $D_{th}$ | $\bar D_{\mathrm{th}}$ (page-local) | "thermal diffusion rate", unit-Lewis diffusivity, printed without a density factor |
| $\mu_t$, $Sc_t$ | $\mu_t$, $Sc_t$ | subgrid eddy viscosity (dynamic Smagorinsky); turbulent Schmidt number 0.7 |
| $\Delta_{mesh}$ | $\Delta$ | cube root of the cell volume |
| $\Delta=F\delta_L^0$ | $\Delta_{\mathrm c}$ (page-local) | combustion filter width of the efficiency function; **collision** with the registry $\Delta$ |
| $\alpha$ (variance model, 1/12) | $\alpha_{\mathrm v}$ (page-local) | **collision** with the DG blending factor $\alpha$ |
| $\alpha$ (Eq. 21) | $\alpha_{\mathrm{fp}}$ (page-local) | alignment angle of $\nabla\tilde Z$ and $\nabla\tilde Y_c$; second meaning of $\alpha$ in the source |
| $F$, $F_{max}$, $n$ | $F$, $F_{\max}$, $n$ | thickening factor (registry §11), its maximum, points across the front (5) |
| $\Xi_\Delta$ | $\Xi_\Delta$ (registry §11) | subgrid wrinkling factor, as on the thickened-flame page |
| $\beta$ (Eq. 12) | $\beta_{\mathrm{Ch}}$ (page-local) | wrinkling exponent 0.5; **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $\Omega$, $\Omega_1$, $\Omega_2$, $\Omega_3$ | $\Omega_{\mathrm{fs}}$ (registry §11), $\Omega_1$, $\Omega_2$, $\Omega_3$ (page-local) | flame sensors; **collision** with the rotation-rate tensor $\Omega_{ij}$ |
| $\Gamma_\Delta$, $f_u$, $f_\Delta$, $f_{Re}$, $Re_\Delta$ | (efficiency function and its parts, subgrid Reynolds number) | page-local |
| $u'_\Delta$ | $u'_\Delta$ | subgrid velocity scale (registry §11) |
| $C_k$, $a$, $b$ (App. A) | (efficiency-function constants) | page-local; **collision** with the DES length factor $C_k$; Gruhlke's $a$, $b$ are other constants |
| $s_L^0$, $\delta_L^0$ | $s_{\mathrm L}$, $l^0_{\mathrm F}$ | laminar flame speed and thermal thickness, functions of $Z$ |
| $K_s$, $K_s^{ext}$ | $a_{\mathrm{cf}}$, $a^{\mathrm{ext}}_{\mathrm{cf}}$ | counter-flow strain rate (registry §11) and its extinction value |
| $\phi$ | $\phi_{\mathrm{eq}}$ | equivalence ratio |
| $Y^*_{CO}$, $Y^c_{CO}$, $\delta_{res}$, $A_{res}$, $A_{total}$ | $Y^*_{\mathrm{CO}}$, $Y^{\mathrm c}_{\mathrm{CO}}$, $Fl^0_{\mathrm F}$, $A_{\mathrm{res}}$, $\Xi_\Delta A_{\mathrm{res}}$ | page-local; $Y^*$ is a front mean, not semi-local scaling |
| $G_{FO}$ | $G_{\mathrm{FO}}$ (page-local) | Takeno-type flame index |
| $x$, $r$ | (axial and radial coordinates) | $x$ is also the 1D flamelet coordinate in Eq. (16) |

# Reference list

62 printed references, numbered style ([1]–[62]), with a single printed
DOI (ref. [52]). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Several cited
works share a first-author-year key with different works already in the
bibliography (Wang 2011, Zhang 2021, Zhang 2017, Ma 2017, Wu 2019, Hartl
2019) and are keyed `wang-2011-e`, `zhang-2021-e`, `zhang-2017-f`, `ma-2017-b`, `wu-2019-f` and `hartl-2019-b`; Nambully et al. (2014) Parts I
and II take suffixes in printed order, resolved against the existing
entry by volume and page. Ref. [29] carries a placeholder volume, ref.
[11] no volume, ref. [12] is a web item; no printed duplicate, no
unparseable item.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Thickened flame model](/methods/thickened-flame-model.md)
- [OpenFOAM](/software/openfoam.md)
