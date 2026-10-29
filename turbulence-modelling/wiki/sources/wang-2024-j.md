---
type: Source
title: "Wang et al. (2024c) — Feasible suggestions of scale-adaptive simulation approach based on the high-fidelity large-eddy simulation of supersonic turbulent boundary layer"
description: "Uses wall-resolved LES of a Mach 2 flat-plate boundary layer to locate the RANS/LES interface of Spalart–Allmaras-based hybrids near y+ ≈ 14, shows on the LES fields that DES, DDES and von Kármán-length SAS interfaces move wallward with refinement, and proposes a dissipation-adaptive length scale that caps the wall distance with the von Kármán length through the DDES shielding function."
resource: "doi:10.1063/5.0223264"
source_kind: paper
authors: [Wang B., Xu C.-Y., Lin X.-H., Wang Z., Liu W.-H.]
year: 2024
venue: "Phys. Fluids 36:085158"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Physics_of_Fluids_Wang_Feasible_suggestions_of_scale-adaptive_simulation_approach_b.pdf"
tags: [hybrid-rans-les, scale-adaptive-simulation, compressible, boundary-layer, spalart-allmaras]
timestamp: 2026-10-28T17:07:00Z
---

# Summary

Wang et al. (2024c) run wall-resolved
[large-eddy simulation](/definitions/large-eddy-simulation.md) of a
spatially developing supersonic
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md) on an
adiabatic flat plate at $M_\infty=2.0$, $Re_{\delta_r}\approx13\,500$,
matching the DNS of Pirozzoli, Bernardini & Grasso (2008): a compressible
[Smagorinsky](/methods/smagorinsky-model.md)–Yoshizawa model with
[dynamic](/methods/dynamic-procedure.md) coefficients, seventh-order
[WENO](/methods/weno-scheme.md) convection, sixth-order central viscous
terms and inlet disturbances of the Sandham and Li–Coleman type
([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
Of three grids the finest agrees with the DNS in the van Driest velocity
([compressible velocity transformations](/definitions/compressible-velocity-transformation.md))
and the Reynolds stresses and is used as a database. On the coarse grid,
[Spalart–Allmaras](/methods/spalart-allmaras-model.md)-based
[DES and DDES](/methods/detached-eddy-simulation.md) show the
[log-layer mismatch](/definitions/log-layer-mismatch.md) and too little
Reynolds stress, and the authors' own one-equation SA-based
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md) does
better but under-predicts the stresses below $y^+\approx14$. This SAS
replaces the SA wall distance by $\min(d,L_{\mathrm{vK}}/\kappa)$; it is not
Menter's $k$-$\sqrt kL$ SAS, and the two are kept apart on the SAS page.

From the LES fields the paper reads coherent structures, the joint
distribution of the velocity-gradient invariants by layer, and profiles of
turbulent kinetic energy, its production and its resolved dissipation. It
infers that the change of flow topology occurs in the buffer layer, so
that the "feasible region of switching interface" of
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) lies at $7<y^+<15$, and
recommends $y^+\approx14$, where the resolved dissipation begins to decay
on every grid. Evaluated on the LES fields, the DES, DDES and SAS interfaces all move toward the wall with refinement;
the proposed dissipation-adaptive length
$d_{\mathrm{DSAS}}=d-f_d\max(0,d-L_{\mathrm{vK},3}/\kappa)$ keeps them near
$y^+\approx14$ on all three grids. A coarse-grid run of "the proposed
improvement", which the paper calls its "a posteriori test" (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)), gives larger near-wall Reynolds stresses, a wider $St^{-5/3}$
range of the wall-pressure spectrum and more small-scale structures than
SAS, DES and DDES. Evidence is numerical and largely qualitative; no error
norms are reported.

# Version read

Version of record (AIP; submitted 13 June 2024, accepted 28 July 2024,
online 16 August 2024), 18 PDF pages (an AIP cover page and article pages
085158-1 to -17), all read; the equation pages were checked visually.
Page 1 matches the metadata. The paper does not state that the
coarse-grid "a posteriori test" (Figs. 1–8, Table I) uses Eq. (40); it is
labelled "our modification" and "proposed improvement". Equation, figure
and section numbers are those of this version.

# Key claims

Page-local symbols: $\delta_r$ the inflow boundary-layer thickness (the
source's $\delta_0$, registry §11); $L_{\mathrm{vK},n}$ ($n=1,2,3$) the three
three-dimensional von Kármán lengths of ref. 42, $\kappa$ included;
$d_{\mathrm{DES}}$, $d_{\mathrm{SAS},n}$, $d_{\mathrm{DSAS}}$ the hybrid
lengths replacing the SA wall distance $d$ ($d_{\mathrm{DDES}}$, $f_d$, $r_d$
registry §11); $Re_\Delta=\rho\lvert S\rvert\Delta^2/\mu$ the mesh Reynolds
number; $A_{ij}=\partial_ju_i$, $P_A$, $Q_A$, $R_A$ its invariants (registry
§11) and $Q_A^d$, $R_A^d$ those of its deviatoric part $A^d_{ij}$; FRSI the
feasible region of switching interface.

1. LES at $M_\infty=2.0$, $Re_{\delta_r}\approx13\,500$ with WENO-7 "can provide credible predictions when grid resolution is sufficient"; LES3 (649×201×161) agrees with the DNS of Pirozzoli et al. in the van Driest mean velocity and the Reynolds stresses, while LES1 and LES2 are "not accurate" (Abstract; §III.B, Figs. 1–2). **Shown**
2. In the inner region $y^+<7$ all LES and hybrid results agree with the wall law, so the grid resolution there "nearly has a negligible effect" (§III.B, Fig. 1). **Shown**
3. DES and DDES on the coarse grid exhibit the log-layer mismatch, "the inherent defect of original DES method and its variants" (§III.B, Fig. 1b). **Shown** (mismatch) / **Stated** (inherent defect)
4. SAS on the coarse grid gives "satisfactory predictions with less computational grids", making SAS "a more promising LES-like hybrid method" (§III.B, Fig. 1b). **Shown**
5. Coarse LES (LES1, LES2) over-predicts $R_{11}$ and slightly under-predicts $R_{12}$; the DES and DDES Reynolds stresses are "obviously insufficient"; SAS is acceptable except that the stresses at $y^+<14$ are under-predicted, attributed to insufficient modelled Reynolds stress of the RANS computation in the inner layer (§III.B, Fig. 2). **Shown** (stresses) / **Stated** (attribution)
6. The a posteriori test of the proposed modification enhances the inner-layer Reynolds stresses, confirming that "more small-scale fluctuations exist in the region of $y^+\approx14$" (§III.B, Fig. 2b). **Shown**
7. Wall-pressure spectra in the outer layer: LES2 and LES3 show $St^{-5/3}$ ranges extending to higher frequency with refinement; LES1 shows $St^{-2}$ scaling; DES and DDES show no obvious $-5/3$ slope; the a posteriori test has a larger $St^{-5/3}$ range than SAS (§III.B, Fig. 3). **Shown**
8. Vortical structures depend on grid and method: LES1 shows large "stem" quasi-streamwise structures, LES2 a mix with hairpins, LES3 small-scale hairpins; DES shows only a few stems; SAS more small-scale structures; on the coarse grid the proposed improvement "performs even better than LES" (§III.C, Fig. 4, $Q_A=0.5$). **Shown** (qualitative)
9. The flow is divided into three stages: transition for $x/\delta_r<10$ (triggered by the inflow condition), developing for $10<x/\delta_r<20$, fully developed for $x/\delta_r>20$; the a posteriori run strengthens the growth of compressible eddies, especially in the second stage (§III.C, Figs. 5–6). **Shown** (qualitative)
10. Negative Lamb-vector divergence dominates the viscous sublayer in the first stage; insufficient resolution (LES1) leaves larger regions of negative divergence, tied to depletion of flow energy; quasi-cyclic behaviour appears earlier in the a posteriori test than in DES and SAS (§III.C, Fig. 6). **Shown** (qualitative)
11. At $y^+=15$ the streaks have a characteristic length of O(1000) wall units (cited from ref. 59); outer-layer streaks at $y^+=80$ are captured by all simulations except DES; the a posteriori run has larger spanwise variation and amplitude of $u'$ (§III.C, Figs. 7–8). **Shown** / **Stated** (O(1000))
12. Joint distributions of $Q_A^d$–$R_A^d$ (at $P_A^d=0$) show the teardrop shape; with grid refinement the contours approach S1 (unstable focus/compressing) and S2 (unstable node/saddle/saddle) and S4 (stable focus/stretching) narrows, "indicating that more unstable small-scale structures are successfully captured" (§III.D, Fig. 10). **Shown**
13. The $Q_A^d$–$R_A^d$ contours in the viscous sublayer are little affected by grid resolution, while in the log and wake layers notable differences appear; hence "the transformation process of flow topology occurs mainly in the buffer layer" (§III.D, Fig. 11). **Shown** / **Derived** (inference)
14. The FRSI from the RANS to the LES-like model "probably" lies in the buffer layer, "within the range of $7<y^+<15$" (§III.D, end). **Stated** (inference from Fig. 11 and refs. 59, 79)
15. The peak of turbulent kinetic energy shifts from $y^+\approx20$ to $y^+\approx15$ with grid refinement, and the peaks of the energy and of its streamwise part decrease with refinement (§III.E, Fig. 12). **Shown**
16. The production peak rises with grid resolution (§III.E, Fig. 13). **Shown**
17. Regardless of the grid, the resolved dissipation $\langle\varepsilon\rangle$ "rapidly decays when $y^+>14$" and approaches zero at the boundary-layer edge; the position where it begins to decay is "nearly independent of grid resolution" (§III.E, §III.F, Fig. 14). **Shown**
18. With the $k$-$\varepsilon$ eddy viscosity $\mu_t=C_\mu\rho k^2/\varepsilon$ ($C_\mu=0.09$, ref. 82), $y^+\approx14$ "corresponds to the critical location of modeled Reynolds stresses"; hence $y^+\approx14$ "may be the appropriate RANS/LES interface of SAS method" (§III.E). **Stated** (heuristic argument)
19. The insufficiently resolved dissipation of coarse-grid LES must be "compensated in the inner-layer region" (§III.E, end). **Stated**
20. The three three-dimensional von Kármán lengths $L_{\mathrm{vK},1,2,3}$ reduce to the one-dimensional definition (Eq. 30) "based on the theoretical analysis" of ref. 42 (§III.F). **Stated**
21. Evaluated on the LES fields, all second length scales are strongly grid dependent; the DES length drops sharply with refinement; $L_{\mathrm{vK},2}$ is "evidently larger" than $L_{\mathrm{vK},1}$ and $L_{\mathrm{vK},3}$, which are highly similar; in all hybrids the RANS/LES interface moves toward the wall with refinement (§III.F, Fig. 15). **Shown**
22. $L_{\mathrm{vK},3}$, which "takes into account both compressible and vortex stretching effect", is considered the more reasonable second length scale for SAS (§III.F). **Stated**
23. The appropriate RANS/LES interface should be grid independent and able to distinguish stable from unstable flow states (§III.F, citing ref. 88). **Stated**
24. $r_d$ of DDES "is equivalent to $Re_\Delta^{-1}$", which links $f_d$ to the balance of subgrid and resolved viscous dissipation of ref. 89 (§III.F). **Stated**
25. $d_{\mathrm{DDES}}$ varies more gradually near the interface than $d_{\mathrm{DES}}$ but stays grid sensitive because $C_{\mathrm{DES}}\Delta$ is still used; $d_{\mathrm{DSAS}}$ changes more smoothly than $d_{\mathrm{SAS},3}$, is similar to it around $y^+\approx14$, and the $d_{\mathrm{DSAS}}$ curves of the three grids concentrate around $y^+\approx14$ (§III.F, Fig. 16). **Shown** (from LES fields)
26. The dissipation-adaptive length scale "would improve the grid-independent characteristic of RANS/LES interface" and "may be a feasible optimization of SAS methods" (§III.F, §IV). **Shown** (from LES fields, Fig. 16) / **Stated** (generalisation)
27. Coarse-grid a posteriori comparisons show that the modified method "can achieve more satisfactory predictions" than the other LES-like methods (§IV). **Shown**
28. LES is "about ten times" cheaper than DNS (introduction, on Ducros et al., ref. 26). **Stated**

The hybrids in registry notation (§III.F, Eqs. 29–40), all replacing the
wall distance $d$ of the SA model:
$d_{\mathrm{DES}}=\min(d,C_{\mathrm{DES}}\Delta_{\max})$ with
$\Delta_{\max}=\max(\Delta x,\Delta y,\Delta z)$ and $C_{\mathrm{DES}}=0.65$;
$d_{\mathrm{DDES}}=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta)$,
$f_d=1-\tanh[(8r_d)^3]$,
$r_d=(\mu_t+\mu)/(\rho\kappa^2d^2\sqrt{\partial_ju_i\,\partial_ju_i})$ (which
$\Delta$ enters $d_{\mathrm{DDES}}$ is not stated); the one-dimensional
$L_{\mathrm{vK}}=\kappa\lvert(\partial\langle u\rangle/\partial y)/(\partial^2\langle u\rangle/\partial y^2)\rvert$
and its three-dimensional forms

$$L_{\mathrm{vK},1}=\frac{\kappa\lvert S\rvert}{\lvert\nabla^2\boldsymbol u\rvert},\qquad L_{\mathrm{vK},2}=\frac{\kappa\lvert\Omega\rvert}{\lvert\nabla\lvert\Omega\rvert\rvert},\qquad L_{\mathrm{vK},3}=\frac{\kappa\lvert\Omega\rvert}{\lvert\nabla^2\boldsymbol u\rvert},$$

with $\lvert\nabla^2\boldsymbol u\rvert^2=(\partial_i\partial_iu_k)(\partial_j\partial_ju_k)$ and
$\kappa=0.41$; $d_{\mathrm{SAS},n}=\min(d,L_{\mathrm{vK},n}/\kappa)$; and the
contribution $d_{\mathrm{DSAS}}=d-f_d\max(0,d-L_{\mathrm{vK},3}/\kappa)$. The
RANS/LES interface is defined as the intersection of the second length
scale with $d$. The LES closes
$\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$ by
$\tau_{ij}=-2C_s^2\Delta^2\bar\rho\lvert\tilde S\rvert\tilde S^d_{ij}-\tfrac23C_I\Delta^2\bar\rho\lvert\tilde S\rvert^2\delta_{ij}$
as printed (Eq. 12; the source's $C_R=C_s^2$; its $\tau^{SGS}_{ij}$ enters
the momentum equation with a minus sign), an eddy-diffusivity heat flux with $Pr_t$,
$C_s^2$, $C_I$ and $Pr_t$ computed dynamically, and $\Delta=V_c^{1/3}$
(Eqs. 6–13). Of the subgrid terms, $D^{SGS}_{ij}$, $Q^{SGS}_i$ and
$\sigma^{SGS}_i$ are neglected and $J^{SGS}_i=\tilde u_j\tau_{ij}$. The
velocity-gradient invariants follow
$\Lambda^3+P_A\Lambda^2+Q_A\Lambda+R_A=0$ with $P_A=-\operatorname{tr}A$,
$R_A=-\det A$, and the deviatoric forms $Q_A^d=Q_A-\tfrac13P_A^2$,
$R_A^d=R_A-\tfrac13P_AQ_A+\tfrac2{27}P_A^3$ normalized by
$\langle Q_\Omega\rangle$ and $\langle Q_\Omega\rangle^{3/2}$, $Q_\Omega=-\Omega_{ij}\Omega_{ji}/2$
(Eqs. 16–25).

# Printed slips

- **Eq. (18):** "$Q=\frac12([\mathrm{tr}(\boldsymbol A)]^2-\mathrm{tr}(\boldsymbol A))$", while the right-hand side of the same equation, $\frac12(P^2-S_{ij}S_{ji}-W_{ij}W_{ji})$, corresponds to $\mathrm{tr}(\boldsymbol A^2)$ in the second term.
- **Eq. (25):** "$R^*=\dots=-\Lambda^*_1\Lambda^*_2\Lambda^*_2$" repeats $\Lambda^*_2$, against $R=-\det\boldsymbol A$ (Eq. 19).
- **Eq. (13):** $q^{SGS}_i=\dots\partial\tilde T/\partial x_j$, free index $i$ on the left and $j$ on the right.
- **§III.D:** "$A^*_{ij}=A_{ij}-\frac13\theta$" lacks the $\delta_{ij}$ that $S^*_{ij}=S_{ij}-\frac13S_{kk}\delta_{ij}$, printed just below Eq. (25), carries.
- **Layer names:** §III.B "In the inner-layer region (i.e., buffer region) of $y^+<7$", while §III.D places the buffer layer at $7<y^+<15$; §III.E puts the energy peak at "the outer edge of the logarithmic-law region" and then at $y^+\approx20$ to $15$.
- **§III.D:** "The $Q^*$-$R^*$ contours in the viscous sublayer is little affected by grid resolution (see)." — "(see)" has no target.
- **Citations:** §I cites "scale-adaptive simulation (SAS),6" where ref. 6 is Spalart et al. (1997, DES), and the "zone-determined method of DES,8,9" with ref. 8 Menter et al. (2003, SAS).
- **Figures:** the slopes of Fig. 3 are labelled "$St^{2}$" and "$St^{5/3}$" while the text says $St^{-2}$, $St^{-5/3}$; the legend of Fig. 1 reads "DNS form Pirozzoli et al.".
- **References:** ref. 49 "privative equations", ref. 11 "artifical", ref. 62 "Spring-Verlag Press" (kept as printed).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f$, $\tilde f=\overline{\rho f}/\bar\rho$ | $\bar f$, $\tilde f$ | LES and Favre filters; dropped "for neatness" after §III.A |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time and spanwise average |
| $\{f\}$, $u''_i$ | $\langle f\rangle_\rho$, $u''_i$ | Favre average and fluctuation |
| $\tau^{SGS}_{ij}$ | $\tau_{ij}$ (compressible, with $\bar\rho$) | full tensor, positive trace |
| $\tilde\tau_{ij}$ | $\sigma_{ij}$ | resolved viscous stress |
| $\tilde S=(2\tilde S_{ij}\tilde S_{ij})^{1/2}$, $S$ | $\lvert\tilde S\rvert$, $\lvert S\rvert$ | factor two included |
| $C_R$, $C_I$, $Pr_T$ | $C_s^2$, $C_I$, $Pr_t$ | dynamic; no values printed |
| $\bar\Delta=(V_c)^{1/3}$ | $\Delta$ | cube root of the cell volume |
| $\max\{\Delta x,\Delta y,\Delta z\}$ | $\Delta_{\max}$ (page-local) | DES length |
| $\mu_T$ | $\mu_t$ | |
| $L_{vk}$, $L_{vk1,2,3}$ | $L_{\mathrm{vK}}$, $L_{\mathrm{vK},1,2,3}$ | $\kappa$ included, then divided by $\kappa$ in $d_{\mathrm{SAS},n}$ |
| $\Omega$ (Eqs. 31–33) | $\lvert\Omega\rvert$ | vorticity magnitude; **collision** with the tensor $\boldsymbol\Omega$ of Eq. (14) |
| $U_{i,j}$ | $\partial_ju_i$ | in $r_d$ |
| $d_{DES}$, $d_{DDES}$, $d_{SASn}$, $d_{DSAS}$ | $d_{\mathrm{DES}}$, $d_{\mathrm{DDES}}$, $d_{\mathrm{SAS},n}$, $d_{\mathrm{DSAS}}$ | |
| $Re_{\bar\Delta}=\rho S\bar\Delta^2/\mu$ | $Re_\Delta$ (page-local) | mesh Reynolds number |
| $\boldsymbol A$, $P$, $Q$, $R$ | $A_{ij}$, $P_A$, $Q_A$, $R_A$ | $\Lambda^3+P\Lambda^2+Q\Lambda+R=0$; $Q$ also the Q criterion (Eq. 14) |
| $A^*_{ij}$, $Q^*$, $R^*$, $S^*_{ij}$ | $A^d_{ij}$, $Q_A^d$, $R_A^d$, $S^d_{ij}$ | **collision:** the registry's $(\cdot)^*$ is semi-local scaling |
| $W_{ij}$, $Q_W$ | $\Omega_{ij}$, $Q_\Omega$ (page-local) | |
| $\theta=S_{ii}$ | $\nabla\cdot\boldsymbol u$ | **collision** with the momentum thickness $\theta$ |
| $\Delta$ (Eq. 20) | (discriminant of the characteristic equation) | **collision** with the filter width |
| $\langle k\rangle$, $\langle k_x\rangle$, … | $2k/U_\infty^2$ and its parts | Eq. (26) sums the normal stresses without the factor $\tfrac12$ |
| $\langle P\rangle$, $\langle\varepsilon\rangle$ | $P_k$, $\varepsilon$ (density-weighted, resolved) | **collision** of $P$ with the invariant |
| $R_{ij}$ | $(\langle\rho\rangle/\rho_w)\langle u''_iu''_j\rangle_\rho$ | plotted over $u_\tau^2$ |
| $\delta_0$, $Re_\delta$ | $\delta_r$, $Re_{\delta_r}$ | inflow thickness |
| $\Delta y^+_w$ | $\Delta y^+$ | first cell, 0.8 on all grids |
| $\boldsymbol l=\boldsymbol\omega\times\boldsymbol u$ | (Lamb vector, page-local) | |
| $NS$, $C_1$, $C_2$ | (numerical schlieren, page-local) | |
| $St=f\delta_0/U_\infty$ | $St$ | |

# Reference list

89 printed references, numbered AIP style with titles. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. 56 (Wang B. et al., "Scale-adaptive simulation of the separated
flow past a 90°-inclined prolate spheroid", Phys. Fluids 36:045101) takes
the key of the ingested [wang-2024](/sources/wang-2024.md), a different work, and is keyed `wang-2024-n`. Same-author same-year works are keyed
in printed order (Wu 2007: refs. 13, 63; Xu 2010: refs. 1, 85). Refs. 2,
8, 51, 53 and 55 are reports or conference papers; printed typographic
slips in titles are kept. No item is unparseable.

# Pages created or updated

Chunk 14 (2026-10-28), cited further in chunk 15. This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Vortex identification criteria](/definitions/vortex-identification-criterion.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
