---
type: Source
title: "Kokkinakis et al. (2023) — High-speed shock–boundary-layer interaction over deformed surfaces"
description: "Implicit LES with an 11th-order WENO finite-volume code of a Mach 1.94 oblique-shock/turbulent-boundary-layer interaction over a planar panel and six static buckled-panel shapes: wall-pressure changes of about 10%, bent anisotropy topology on the barycentric map, and deformation rate as influential as amplitude."
resource: "doi:10.1063/5.0172475"
source_kind: paper
authors: [Kokkinakis I.W., Drikakis D., Spottswood S.M., Brouwer K.R., Riley Z.B.]
year: 2023
venue: "Phys. Fluids 35:106109"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Physics_of_Fluids_Kokkinakis_High-speed_shockboundary-layer_interaction_over_deformed_sur.pdf"
tags: [shock-boundary-layer-interaction, implicit-les, weno, fluid-structure-interaction, anisotropy, compressible]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

Kokkinakis et al. (2023) study how static buckled-panel deformations alter
an oblique [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
in the configuration of the AFRL Research Cell 19 wind tunnel: Mach 1.94
inflow, a $12^\circ$ shock-generator wedge, and a thin compliant panel
($254\times127\times0.635$ mm) where the shock impinges. Instead of a
coupled fluid–structure simulation, six static shapes (modes $\pm1$,
$\pm2$, $\pm3$, products of sines) with amplitudes taken from the
experimental panel response are compared with the planar panel. The solver
is the authors' block-structured finite-volume code CNS3D run as
[implicit LES](/definitions/implicit-les.md) ("coarse-grained simulation"
in the paper's terms, an umbrella for [LES](/definitions/large-eddy-simulation.md)
with explicit or implicit subgrid modelling): HLLC fluxes, an augmented
11th-order [WENO](/methods/weno-scheme.md) reconstruction of primitive
variables, a five-stage SSP Runge–Kutta, and digital-filter
[inflow turbulence](/methods/inflow-turbulence-generation.md). The
[numerical dissipation](/properties/numerical-dissipation.md) of the
scheme is the only subgrid model. A four-mesh study selects a 9.4 M-cell
mesh with $\Delta x^+=717$, $\Delta z^+=634$, $y^+=4.8$; the paper also
quotes the wall-resolved [LES grid guidance](/results/les-grid-point-requirements.md)
$\Delta x^+\approx50$–130, $\Delta z^+\approx15$–30.

Along the midspan the mean and RMS wall pressure change by about 10%
relative to the planar case; where a mode raises the interaction's peak
pressure it lowers the post-interaction pressure, and vice versa. Near-wall
pressure contours bend spanwise, concave or convex by mode. The
[barycentric anisotropy map](/definitions/barycentric-anisotropy-map.md)
of the Reynolds stress, in the colour-weight form of Emory and Iaccarino,
keeps its componentality state but its topology bends spanwise; the effect
is gone at $y^+=2063$, where the [boundary layer](/benchmarks/turbulent-boundary-layer.md)
has recovered. Mode 3, with about a quarter of the mode-1 amplitude, gives
a comparable response, from which the authors infer that the deformation
rate matters as much as the amplitude. No experimental pressure data are
compared in the paper.

# Version read

Version of record (AIP, special topic "Shock Waves"; received 16 August
2023, published online 18 October 2023); 16 PDF pages (cover sheet plus
pages 106109-1 to 106109-15), all read, with equations and signed
statements checked visually on pages 3–6 and 8–11. Page 1 matches
Crossref.

# Key claims

1. Six static deformation modes of the clamped panel are modelled by $d_{n_M}(x,z)\simeq a_{n_M}\sin(n_M\pi x/L_{x,p})\sin(\pi z/L_{z,p})$, $0\le|n_M|\le3$; positive modes start with a bump into the flow, negative ones with a trough (§II A, Eq. 1, Fig. 2). **Stated**
2. Modes $\pm1$ to $\pm3$ were the dominant panel responses for the $12^\circ$ wedge; the mode-1 amplitude reproduces the measured extreme deformation (refs 32, 37), and the mode-2 and mode-3 amplitudes are scaled to give a similar surface curvature (§II A). **Stated**
3. Peak deformation heights $\max|y|/\delta_0=0.402$ ($y^+=1017$), 0.17 (428), 0.114 (290) for modes $\pm1$, $\pm2$, $\pm3$, where the undisturbed Mach number is 1.55, 1.35, 1.23 (Table II). **Stated**
4. The inlet boundary-layer thickness is $\delta_0\approx4.7$ mm, from laminar growth $\delta\simeq5x/Re_x^{1/2}$ up to $Re_{x}\approx0.5\times10^6$ and turbulent growth $\delta\simeq0.37x/Re_x^{1/5}$ (Schlichting–Gersten) at $x=402$ mm (§III B 1). **Derived**
5. Digital-filter inflow turbulence needs about $5\delta_0$ to develop (ref. 25); the wedge sits about $21.1\delta_0$ from the inlet, "sufficiently far" (§III B 1). **Stated**
6. Wall-resolved LES needs $\Delta x^+\approx50$–130, $\Delta z^+\approx15$–30 and 10–30 points across the boundary layer with the first point at $y^+\lesssim1$ (refs 67–69) (§III B 2). **Stated**
7. On the planar panel (Table III; 1 048 576 to 39 726 720 cells) the mean and RMS pressure "converge gradually"; the medium-2 mesh (9 437 184 cells, full 152 mm span, $\Delta x^+=717$, $\Delta z^+=634$, $y^+=4.8$) agrees reasonably with the fine one ($\Delta x^+=268$, $\Delta z^+=100$, $y^+=2.7$, 33 mm span) and is selected (§IV A, Fig. 4). **Shown**
8. A fine wall-resolved ILES would need $x$ and $z$ cells reduced to a third ("almost an order of magnitude") and the full 152 mm span instead of 33 mm ($\sim4.6\times$), a cost "$\sim175$ times greater compared to the medium 2 mesh" (§III B 2). **Stated**
9. Along the midspan the mean and RMS pressure differences relative to the planar case are about 10% and affect the whole panel length, diminishing toward the spanwise edges (§IV B, Figs. 5–6; Conclusion 1). **Shown**
10. Before the interaction the mean pressure rises for positive and falls for negative modes; at the interaction (about 110 mm) modes $\pm2$ and $\pm3$ give the extreme amplification, mode 1 responds opposite to modes 2 and 3, and modes $\pm1$ do not give the largest mean-pressure response despite the largest amplitude (§IV B 1, Fig. 5). **Shown**
11. Downstream (130–190 mm) the mean-pressure response is opposite to that at the interaction, except for modes $\pm2$, which converge to the planar case (§IV B 1). **Shown**
12. The RMS pressure peaks at about 87 mm, ahead of the mean peak; a secondary RMS peak at about 110 mm is shifted about 5 mm upstream by mode +1 and is largest for mode $-2$ (§IV B 2, Fig. 6). **Shown**
13. The RMS-pressure change is of similar percentage across modes despite different amplitudes, suggesting the deformation rate matters as much as the amplitude (§IV B 2). **Shown** (inference **Stated**)
14. Near-wall ($y^+=5$) mean-pressure maps are symmetric about the midspan, taken as showing no mean-flow asymmetry and a sufficient averaging sample (§IV C, Fig. 7). **Shown**
15. Modes +1, $-2$, $-3$ have a positive streamwise deformation gradient at the interaction (surface moving toward the flow) and raise its peak mean pressure by about 10%; the mirror modes lower it (§IV C, Fig. 7). **Shown**
16. The mean-pressure contours acquire a spanwise curvature, concave or convex by mode and position; the frontal interaction region is less affected, by a mechanism "not evident" (§IV C; Conclusion 3). **Shown**
17. The mean wall-normal velocity at $y^+\simeq5$ alternates sign 3–4 times for modes $\pm1$ and 2 and 5–6 times for modes $\pm3$ (§IV C, Fig. 8). **Shown**
18. The mean spanwise velocity changes sign streamwise and spanwise; the number of spanwise sign changes follows the number of inclined surfaces (two, three, four for modes 1, 2, 3) (§IV C, Fig. 9). **Shown**
19. Near the wall the mean streamwise velocity lies in $[-20,35]$ m/s, the wall-normal and spanwise maxima are about 1.75% and 15% of it, so their effect on the mean boundary layer and interaction is small (§IV C). **Shown**
20. The Reynolds-stress anisotropy is analysed on the barycentric map of Banerjee et al. (ref 71) with the colour weights of Emory and Iaccarino (ref 72), $X_{ic}=(C_{ic}+C_{\mathrm{off}})^{C_{\exp}}$, $C_{1c}=\lambda^b_1-\lambda^b_2$, $C_{2c}=2(\lambda^b_2-\lambda^b_3)$, $C_{3c}=3\lambda^b_3+1$, $C_{\mathrm{off}}=0.65$, $C_{\exp}=5$, $\lambda^b_i$ the ordered eigenvalues of $b_{ij}$ built from the Favre-averaged $R_{ij}$ (§IV D, Eqs. 4–5). **Stated** (method), applied **Shown**
21. The deformations do not change the anisotropy state but change its topology: contour lines bend symmetrically about the midspan (§IV D, Figs. 10–13). **Shown**
22. Because even the mode-3 deformation varies slowly compared with the boundary-layer thickness, the boundary layer can adjust gradually to the curvature (§IV D). **Stated**
23. At $y^+=4.8$ the turbulence is mostly two-component; shock and expansion impingement drive it toward one-component; positive modes strengthen this shift near the midspan (most for mode +3), negative modes hamper it (§IV D, Fig. 10). **Shown**
24. At $y^+=24$ and 192 the componentality bends concave where the surface moves toward the flow and convex where it moves away, most in the recovery region (§IV D, Figs. 11–12). **Shown**
25. At $y^+=2063$ the deformations have little to no effect: "the TBL quickly recovers" (§IV D, Fig. 13; Conclusion 4). **Shown**
26. Although the mode-3 amplitude is "almost a quarter" of mode 1's, the overall response is equivalent, so the deformation rate plays "just as important a role" as the amplitude (§V). **Shown** (inference **Stated**)
27. Earlier reduced-order aeroelastic modelling with quasi-steady enriched piston theory (refs 37–38) captures flutter onset for the $12^\circ$ wedge but mispredicts the modal and frequency content of the post-flutter response, attributed to omitted unsteady interactions (§I). **Stated**

The viscous stress is written (§III A)
$\mathbf T=\lambda_{\mathrm v}(\nabla\cdot\boldsymbol u)\mathbf I+\mu[\nabla\otimes\boldsymbol u+(\nabla\otimes\boldsymbol u)^{\mathsf T}]$,
with $\lambda_{\mathrm v}$ printed as the "bulk viscosity" and set to
$-4\mu/3$ "according to Stokes' hypothesis" (see Printed slips). The paper
cites the [spectral gap](/definitions/spectral-gap.md) between integral and
viscous scales (ref. 55) as the basis of coarse-grained simulation (§I).

# Printed slips

- §III A: "bulk viscosity $\lambda_b=-4\mu/3$ according to Stokes' hypothesis" for the stress tensor above. The trace of that tensor is $(3\lambda_{\mathrm v}+2\mu)\nabla\cdot\boldsymbol u$, which vanishes for $\lambda_{\mathrm v}=-2\mu/3$, not $-4\mu/3$; the coefficient is the second viscosity, the [bulk viscosity](/definitions/bulk-viscosity.md) being $\lambda_{\mathrm v}+2\mu/3$ by the relation that [Beattie et al. (2025)](/sources/beattie-2025.md), footnote 2, print *(compiler check, not in the sources)*. The paper does not say which value the code uses.
- Eq. (1) is printed "for $x\in[0,L_{z,p}]$ and $z\in[0,L_{z_p}]$", while its sine argument is $x/L_{x,p}$; "clumped thin panel" (§II A).
- §III B 1: "In the case of modes 2 and 3, the surface deformation reaches … at about 300 and 430, respectively"; Table II prints $y^+=428$ for mode $\pm2$ and 290 for mode $\pm3$.
- Abstract: "The deformation amplitudes we examined were at least half the height of the incoming turbulent boundary layer thickness"; Table II prints $\max|y|/\delta_0=0.402$, 0.17, 0.114, and §III B 1 says the amplitudes "are below $\approx0.4\delta_0$".
- §III B 2: the factors printed are "almost an order of magnitude" and "$\sim4.6$", and the total "$\sim175$ times greater compared to the medium 2 mesh"; a third of the cell size in both $x$ and $z$ is $3\times3=9$ times the cells, $152/33\approx4.6$, $9\times4.6\approx41$, and the medium-2 mesh already spans the full 152 mm *(compiler check, not in the sources)*. No further factor is stated.
- The first anisotropy plane is "$y^+=4.8$" in §IV D and "$y^+=5$" in the caption of Fig. 10; Conclusion 4 names the outer layer "at heights of $y^+\simeq1000$", while the outer plane analysed is $y^+=2063$ (Fig. 13).
- §III B: "The DNS compression ramp data used here were obtained using an augmented 11th-order WENO scheme"; the paper uses no compression-ramp DNS data.
- Ref. 72 prints the page range "213–138"; ref. 48 ends "2021.."; the acknowledgments print "PA#" without a number.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline{(\cdot)}$, $\widetilde{(\cdot)}$, $u''_i$ | $\langle\cdot\rangle$, $\langle\cdot\rangle_\rho$, $u''_i$ | **collision:** the source's overbar is a Reynolds average, its tilde a Favre average |
| $R_{ij}=\widetilde{u''_iu''_j}$ | $R_{ij}=\langle u''_iu''_j\rangle_\rho$ | positive trace, Favre form |
| $a_{ij}=R_{ij}/(2k)-\delta_{ij}/3$ | $b_{ij}$ | |
| $\lambda_1\ge\lambda_2\ge\lambda_3$ | $\lambda^b_1\ge\lambda^b_2\ge\lambda^b_3$ (eigenvalues of $b_{ij}$, registry §11) | **collision** with the Taylor microscale $\lambda$ |
| $X_{1c}$, $X_{2c}$, $X_{3c}$, $C_{ic}$, $C_{off}$, $C_{exp}$ | $X_{ic}$, $C_{ic}$ (registry §11), $C_{\mathrm{off}}$, $C_{\mathrm{exp}}$ (page-local) | the source uses $X_{ic}$ both for the limiting states and for the colour weights of Eq. (5) |
| $\lambda_b$ | $\lambda_{\mathrm v}$ (second viscosity, page-local, as on the bulk-viscosity page) | **collision:** printed as "bulk viscosity", not the registry's $\mu_b$ |
| $u_\tau$, $\tau_w$, $\rho_w$, $\nu_w$, $y^+$, $\Delta x^+$, $\Delta z^+$ | same | |
| $\delta_0$, $\delta_{turb}$, $\delta_{lam}$ | $\delta$ at the inlet; turbulent and laminar estimates | |
| $n_y^w$, $N_c$ | (points across the boundary layer; total cells, page-local) | |
| $d_{n_M}$, $a_{n_M}$, $n_M$, $L_{x,p}$, $L_{z,p}$ | (deformation, amplitude, mode number, panel length and width, page-local) | |
| $\theta$ | (wedge angle, page-local) | **collision** with the momentum thickness $\theta$ |
| $\kappa$ | (heat conductivity, page-local) | **collision** with the von Kármán constant |
| $e_t$, $e_i$ | $E$, (internal energy per unit volume) | |
| $\tilde u_x$, $\tilde u_y$, $\tilde u_z$ | $\langle u\rangle_\rho$, $\langle v\rangle_\rho$, $\langle w\rangle_\rho$ | $y$ wall-normal (toward the upper panel positive) |
| $L_p$, $p_0$ | (sound pressure level, 20 µPa reference) | |

# Reference list

72 printed references, numbered (superscript) AIP style, titles printed
for all, no DOIs printed, all parsed. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works are suffixed in printed order (Brouwer 2021, Brouwer 2023,
Ritos 2018); ref. 54 is an edited volume without author; ref. 72 carries
the printed page range "213–138". No printed duplicates.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Barycentric anisotropy map](/definitions/barycentric-anisotropy-map.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Spectral gap](/definitions/spectral-gap.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
