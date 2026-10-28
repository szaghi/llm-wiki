---
type: Source
title: "Kimmel et al. (2025) — Turbulence and Upstream Shock Wave-Boundary Layer Interaction Effects on Compliant Structures"
description: "Implicit LES with block-structured AMR (PeleC) of a Mach 4, 24-degree compression ramp, used to load a downstream compliant panel: SBLI frequencies reach the panel and could excite its modes, turbulence and structure are one-way coupled, and a thickness–intensity map locates moderate panel deflection."
resource: "doi:10.2514/1.J065095"
source_kind: paper
authors: [Kimmel E.S., Huang D., Sharma V., Singh J., Raman V., Friedmann P.P.]
year: 2025
venue: "AIAA J. 63(9):3641–3653"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_AIAA_Journal_Kimmel_Turbulence_and_Upstream_Shock_Wave-Boundary_Layer_Interactio.pdf"
tags: [shock-boundary-layer-interaction, implicit-les, hypersonic, fluid-structure-interaction, mesh-adaptation]
timestamp: 2026-10-28T17:05:00Z
---

# Summary

Kimmel et al. (2025) ask whether a turbulent shock-wave/boundary-layer
interaction upstream of a compliant control-surface panel changes the
panel's response, and how strongly boundary-layer turbulence and panel
deformation couple. The flow is a Mach 4, $24^\circ$ compression ramp
([shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md))
with a $10\times10$ cm Inconel 718 panel 10 cm downstream of the corner.
It is computed with the AMReX-based PeleC code: second-order finite
volumes, a Godunov-type Riemann solver with slope reconstruction,
embedded-boundary cut cells for the ramp (an
[immersed-boundary](/methods/immersed-boundary-method.md) treatment), and
three levels of block-structured
[adaptive refinement](/methods/mesh-adaptation.md) (130 million cells).
The isotropic cells stop at $\Delta x^+=\Delta y^+=\Delta z^+=11$, the
first cell centre sits at $y^+=5.5$, and there is neither a subgrid nor a
wall model, so the authors call the computation an
[implicit LES](/definitions/implicit-les.md), not a
[DNS](/definitions/direct-numerical-simulation.md). The
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)
grows from a 1 mm laminar parabolic inflow profile with random
$\pm2\%$ velocity perturbations
([inflow generation](/methods/inflow-turbulence-generation.md)). The
structure is a plate finite-element model solved in 20 normal modes and
loaded one way by the computed wall pressure.

Three findings. (1) Wall-pressure spectra evolve from 7–25 kHz upstream
to 1.5–2 kHz at the separation-shock foot, 0.5–2 kHz at reattachment and
a dominant 4 kHz downstream; cross-correlations show the 1.5–2 kHz band
surviving to $x/\delta>8$, and the 4 kHz peak would excite a panel mode,
so the authors state that upstream interactions "must be considered" in
control-surface FSI modelling.
(2) A static 1 mm panel deformation changes the pressure spectra strongly,
but feeding the changed pressure history to an elastic panel changes its
response only marginally: turbulence and structure are one-way coupled.
(3) With the record extended by spectral proper orthogonal decomposition
(SPOD), a map over pressure-fluctuation intensity and panel thickness
shows that moderate deflection needs very high dynamic pressure at the
1% intensity of external flows, while the threshold falls by more than an
order of magnitude at 10%. Evidence is numerical; the solver's accuracy
and mesh convergence are delegated to the authors' conference paper.

# Version read

Version of record (AIAA typeset; received 7 November 2024, accepted 7
March 2025, open access online 23 June 2025), 13 pages, all read; the
equations, Figs. 2–5 and 11–12 and Appendix A were checked visually.
Page 1 matches the metadata. One identity point: the first-page footnote
says the article was "Presented as Paper 2024-2735 at the AIAA SciTech
Forum", and Ref. [23] is AIAA Paper 2024-2735 by the same group under a
different title ("Evaluation of Shock Wave-Boundary Layer Interaction
Modeling Capabilities for Use in a Hypersonic Aerothermoelastic
Framework"), cited as the evidence for PeleC's accuracy and mesh
convergence. Numbering on this page is that of the version read.

# Key claims

Page-local symbols: $I_P=\langle\lvert p'\rvert\rangle/\langle p\rangle$
the pressure-fluctuation intensity (a mean absolute fluctuation, not an
rms); $t_p$ the panel thickness; $\lambda_{\mathrm{fl}}$ the
non-dimensional dynamic pressure of panel flutter; $w_{\mathrm p}$ the
panel transverse displacement; $\theta_r$ the ramp angle. Coordinates are
the registry's: $x$ streamwise, $y$ wall-normal, $z$ spanwise.

1. PeleC solves the compressible Navier–Stokes equations (Eqs. 1–4) "with second-order spatiotemporal accuracy" by a finite-volume method of lines with characteristic extrapolation, a second-order explicit Runge–Kutta scheme, a Godunov-type Riemann solver with slope reconstruction, adaptive mesh refinement and an embedded-boundary method (§II.A). **Stated**
2. PeleC "generates statistically accurate turbulent boundary layers and models compression ramp SBLI with sufficient accuracy", citing Ref. [23] (§II.A). **Stated**
3. Mesh: base $512\times64\times256$, three refinement levels each halving the cell size, 130 million cells; about 40 million level-2 cells over 7.5% of the domain and 75 million level-3 cells over 1.75%; refinement tagged on the boundary layer, the interaction region and the shock path, plus cut cells and cells with $\lvert\nabla\rho\rvert\ge10^{-6}$ (§III.A, Fig. 3). **Stated**
4. Time step $\Delta t=4.7\times10^{-7}$ s (CFL 0.3) with subcycling per refinement level; 2500 samples at 425 kHz (§III.A). **Stated**
5. DNS would need $y^+\le1$ at the first point (Eq. 7), which the isotropic-cell constraint $\Delta x^+=\Delta y^+=\Delta z^+$ of block-structured refinement makes "computationally prohibitive"; the finest cell is $\Delta x^+=\Delta y^+=\Delta z^+=11$, the first evaluation point is at $y^+=5.5$, and with no wall model and no subgrid model the simulations are implicit LES (§III.A). **Stated**
6. Mesh-convergence studies in Ref. [23] gave similar beam FSI responses with three and four refinement levels, so three levels suffice (§III.A). **Stated** (evidence in the cited work)
7. Upstream of the interaction ($x/\delta\le-2.5$) the pressure fluctuations span 7–25 kHz with no low-frequency content, so the interaction begins at $x/\delta=-2.5$; 1.5–2 kHz appear for $-2.5\le x/\delta\le-1$ (separation-shock foot oscillation); 5–10 kHz in the recirculation bubble; 0.5–2 kHz from reattachment ($x/\delta=0$) to $x/\delta=1.5$; beyond that a dominant 4 kHz with moderate 1.5–2, 2.7 and 6 kHz components (§IV.A, Fig. 5b). **Shown**
8. The reattachment region contains 0.5–1 kHz content absent from the separation region; since Dupont et al. [15] find near-identical separation and reattachment spectra for impinging shocks, the difference is attributed to the ramp geometry, where large upstream eddies collide with the ramp surface (Fig. 6), giving two peaks at $x/\delta=0$ and $x/\delta=1.25$ (§IV.A). **Shown** (attribution **Stated**)
9. Power spectra of the cross-correlation (Eq. 8) with reference station $x/\delta=-2$ show strong low-frequency correlation in the shock-oscillation region, 1.5–2 kHz correlation near reattachment, decreasing correlation downstream and 1.5–2 kHz bands again for $x/\delta>8$: low interaction frequencies propagate into the downstream boundary layer (§IV.A, Fig. 7). **Shown**
10. The evolution (high frequencies upstream, low in the interaction, intermediate downstream) matches impinging-shock configurations [15, 31], with greater similarity between interaction-region and downstream frequencies for the ramp (§IV.A). **Shown** (comparison with cited works)
11. The 4 kHz downstream peak would excite the (5,1) mode of a $10\times10\times0.1$ cm Inconel 718 panel; since the post-interaction boundary layer contains frequencies low enough for resonance and an undisturbed one does not, the upstream interaction "must be considered" in downstream FSI modelling (§IV.A; Conclusion 1). **Stated** (mode identification not shown)
12. The fluid time scale (a particle crossing the panel, 0.15 ms) is far below the structural one (one (1,1) oscillation, 2 ms), which justifies representing the deformation by a static shape when assessing its effect on turbulence (§III.B). **Stated**
13. Flat rigid panel: dominant 4 kHz near the leading edge with 2–3 and 6 kHz secondary peaks; spectral levels fall downstream but the peak frequencies persist over the chord (§IV.B.1, Figs. 8a,b). **Shown**
14. Panel with a static mode-(2,1) shape of 1 mm amplitude: strong 2, 4 and 7 kHz content at the leading edge, which acts as a compression ramp; fluctuations collapse past the quarter chord, low frequencies appear between quarter and mid chord after the expansion, and fluctuations rise again at the trailing edge; the dominant frequencies vary strongly along the chord, so structural deformation changes turbulence properties, consistent with Ref. [20] (§IV.B.1, Figs. 8c,d). **Shown**
15. Frequency responses (Eq. 10) of a 1 mm elastic panel: under the flat-panel pressure history the (1,1) mode is about three times stronger than (2,1) and (1,2); under the deformed-panel history these are about equal; the peak (1,1) response of the flat history is about double that of the deformed one; modes beyond (1,3) and (3,1) are an order of magnitude weaker or at too high frequency (§IV.B.2, Fig. 9). **Shown**
16. Time-domain panel-centre responses to the two histories differ slightly in amplitude and frequency content (0.5 kHz, the first natural frequency, dominates both; content near 1 kHz is stronger under the deformed history), with differences "on the order of $0.0001t_p$" (§IV.B.2, Fig. 10). **Shown**
17. A 1 mm deformation (100% of $t_p$) changed the turbulence such that the FSI response changed by 0.05%: deformations affect turbulence, but the changed turbulence barely affects the structural response (one-way coupling) (§IV.B.2; Conclusion 2). **Shown**
18. Proposed consequence: a framework in which the quasi-steady flow is two-way coupled with the structure and the turbulent component one-way coupled; reduced-order models can exploit this; turbulence may still matter for high-frequency fatigue (§III.B, §V). **Stated**
19. The simulated boundary layer has $I_P=1.04\%$; the 0.047 s record (40 flow-throughs, 4000 samples) is too short for low-frequency structural response, so SPOD with 4 modes and 1001 frequencies reconstructs a 0.25 s history "while maintaining the spatiotemporal properties" (citing [29]), followed by a 1 kHz high-pass filter that removes reconstruction artefacts (§III.C, Eq. 13). **Stated**
20. At $I_P=1\%$ the $t_p=0.1$ mm panel's deflection grows continually and exceeds $0.07t_p$ by 0.25 s, mostly in the first mode; by linearity $I_P=2\%$ would exceed the $0.1t_p$ moderate-deformation threshold, but 2% is "unrealistic for the current Mach 4 flow" (§IV.C, Fig. 11a). **Shown**
21. The $t_p=1$ mm panel at $I_P=1\%$ has non-dimensional displacements of order $10^{-4}$, multi-modal and not growing; even at $I_P=10\%$ displacements stay small (§IV.C, Fig. 11b). **Shown** (the 10% statement by linearity)
22. Threshold map (Fig. 12): the $0.1t_p$ threshold lies at high $\lambda_{\mathrm{fl}}$, especially at low $I_P$; for $t_p<0.1$ mm moderate deformations occur at 1%; the threshold $\lambda_{\mathrm{fl}}$ falls by more than an order of magnitude as $I_P$ reaches 10% (§IV.C; Conclusion 3). **Shown**
23. Configurations such as scramjet inlets "routinely experience pressure fluctuation intensities beyond 10%", so turbulence may matter for FSI in high-speed internal flows (§IV.C). **Stated**
24. "Traditional methods for modeling flat panels in hypersonic flows cannot be extended to control surface analysis" (Conclusion 1; the methods of Ref. [14], §I). **Stated**
25. For FSI the pressure, not the velocity fluctuation, is the relevant turbulence statistic, and $I_P$ (Eq. 12) is used as the measure of turbulence strength (§IV.C). **Stated**

Method details in registry notation. The cross-correlation of Eq. (8) is
normalized by the zero-lag auto-correlations of the two wall-pressure
signals and its power spectrum identifies the most correlated frequencies.
The pressure history of the deformed panel is rescaled pointwise by the
ratio of flat to deformed mean absolute fluctuation (Eq. 9) before it is
applied to the elastic panel. The flutter parameter is
$\lambda_{\mathrm{fl}}=2qL^3/(\sqrt{M^2-1}\,D_{\mathrm p})$ with
$D_{\mathrm p}=E_Yt_p^3/[12(1-\nu_{\mathrm P}^2)]$ (Eq. 14), $q$ the
dynamic pressure, $L$ the panel length. The structural model is a 16-DOF
Bogner–Fox–Schmit plate element (Eqs. 5–6, 11) with 2% modal damping;
Appendix A gives the POD and SPOD formulation with the Welch estimator.

# Printed slips

- **§IV.A:** "higher frequencies between 5 and 10 kHz emerged in the recirculation bubble located within 1 ≤ x∕δ ≤ 0" (an empty interval as printed).
- **§IV.A:** "In the shock oscillation region, −2.5 ≤ x∕δ ≤ 1", where the same section earlier gives the shock-foot region as "−2.5 ≤ x∕δ ≤ −1".
- **Eqs. (2) and (4):** the momentum equation is printed $\partial_t(\rho\mathbf u)+\nabla\cdot(\rho\mathbf u\otimes\mathbf u+\boldsymbol\Pi)+\nabla P=\mathbf 0$ with $\boldsymbol\Pi=\mu(\nabla\mathbf u+(\nabla\mathbf u)^T)+(\kappa-\frac23\mu)\mathbf I\,\nabla\cdot\mathbf u$. *(Compiler check, not in the sources: with these two printed forms, for constant $\mu$ and $\nabla\cdot\mathbf u=0$, the viscous contribution to $\partial_t(\rho\mathbf u)$ is $-\mu\nabla^2\mathbf u$, a negative diffusion; the system is consistent only if $\boldsymbol\Pi$ carries a leading minus sign.)*
- **Appendix A, before Eq. (A13):** "$\Phi(x,t)=\Psi(x,\omega')e^{2\pi\omega't}$", without the imaginary unit carried by Eqs. (A12) and (13).
- **§IV.B.2:** the differences between the two response histories are "on the order of 0.0001$t_p$", while two paragraphs later "the 100% structural deformation only caused a 0.05% deformation in the FSI response"; 0.05% is $5\times10^{-4}$, five times $10^{-4}$ *(compiler check, not in the sources)*.
- **§III.C:** "4000 panel data samples were collected" and "The duration of the simulation was 0.047 s, or 40 flows through the domain". *(Compiler check, not in the sources: at the 425 kHz sampling rate of §III.A, 4000 samples span $4000/425\,000\approx9.4$ ms, not 0.047 s; the sampling rate of this record is not stated.)*
- **Eq. (9):** the full pressure $P_{\mathrm{def}}$, not its fluctuation, is multiplied by the ratio of fluctuation magnitudes, while the text says the scaling enforces "a local pressure fluctuation magnitude distribution similar to the undeformed panel".
- **Eq. (14):** Young's modulus is printed $E$, where the nomenclature and §III.B write $E_Y$.
- **Footnote and Ref. [23]:** the article is "Presented as Paper 2024-2735", and Ref. [23], AIAA Paper 2024-2735, carries a different title and is cited as separate supporting evidence (see Version read).
- **References:** [8] prints a truncated title ("… Boundary Layer Interactions at Mach,"); [24] prints "Stiffnes"; [20] prints the journal "European Journal of Mechanics".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $x$, $z$, $y$ | **collision:** the source's $z$ is wall-normal and $y$ spanwise |
| $x^+$, $y^+$, $z^+$ | $\Delta x^+$, $\Delta z^+$, $\Delta y^+$ | grid spacings in wall units, all 11 |
| $z_w^+$ | $y^+$ of the first cell centre | 5.5 |
| $z^+=z\sqrt{(\rho_w/\mu_w)\,du/dz\rvert_w}$ (Eq. 7) | $y^+=y/\delta_\nu$ | |
| $\rho$, $\mathbf u$, $P$, $E_T$ | $\rho$, $\boldsymbol u$, $p$, $E$ | $\rho$ also the panel density |
| $P'$, $\bar P$ | $p'$, $\langle p\rangle$ | **collision:** the source's overbar is a time average, the registry's the LES filter |
| $\boldsymbol\Pi$ | viscous stress, sign as printed (registry $\sigma_{ij}$ is $+2\mu S^d_{ij}$) | **collision** with the SGS energy flux $\Pi$ |
| $\mu$, $\kappa$ | $\mu$, $\mu_b$ | **collision:** $\kappa$ (bulk viscosity) is the von Kármán constant in the registry; reused in (A17) as the Welch normalization |
| $\mathcal Q$ | conduction heat flux | sign convention not stated |
| $\delta$ | $\delta$ | boundary-layer thickness upstream of the corner, 8 mm |
| $\theta$ | $\theta_r$ (page-local) | ramp angle $24^\circ$; **collision** with the momentum thickness |
| $M$, $U_\infty$, $Re_x$ | $M$, $U_\infty$, unit Reynolds number | $Re_x=8.661\times10^6$ m$^{-1}$ |
| $I_P=\overline{\lvert P'\rvert}/\bar P$ | $I_P$ (page-local) | mean absolute fluctuation over mean pressure |
| $t_p$, $L$, $w$ | $t_p$, $L$, $w_{\mathrm p}$ (page-local) | **collision:** $w$ is the spanwise velocity in the registry; $L$ here the panel length |
| $\lambda$ | $\lambda_{\mathrm{fl}}$ (page-local) | **collision** with the Taylor microscale |
| $E$ (Eq. 14), $E_Y$, $\nu$, $D$ | $E_Y$, $\nu_{\mathrm P}$, $D_{\mathrm p}$ (page-local) | **collisions:** total energy $E$, kinematic viscosity $\nu$ |
| $\omega$, $\omega_i$ | frequency, natural frequency $i$ | ordinary frequency in $e^{2i\pi\omega t}$ (Eqs. 13, A12), angular in Eq. (10); **collision** with the specific dissipation rate |
| $\eta_i$, $\zeta_i$, $\boldsymbol\phi_i$, $\Lambda_i=\omega_i^2$ | modal coordinate, damping ratio (0.02), eigenvector, eigenvalue | page-local, structural model |
| $\Phi$, $\Psi$, $\Lambda$, $N_{mode}$, $N_\omega$ | POD/SPOD modes, eigenvalues, modes kept (4), frequencies per block (1001) | page-local, Appendix A; $\Phi$ also the structural mode-shape matrix of Eq. (11) |
| $R_{P_{x_{ref}},P_x}(m)$ | normalized wall-pressure cross-correlation at lag $m$ | Eq. (8) |
| ILES | [implicit LES](/definitions/implicit-les.md) | second-order Godunov finite volumes, no SGS or wall model |

# Reference list

32 printed references, numbered style (AIAA), DOIs printed for most
(none for [12], [24], [25], [27]). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Two printed
works fall on keys already held by different works in the bundle
bibliography (Huang & Friedmann 2020, J. Fluids Struct. 94:102927, and
Shinde et al. 2021, Eur. J. Mech. B/Fluids 89:485–500) and are keyed `huang-2020-d` and `shinde-2021-b`. Ref. [23] is the authors' AIAA SciTech 2024 paper (see
Version read). Ref. [8] has a truncated title as printed. No item is
unparseable and no item is printed twice.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
