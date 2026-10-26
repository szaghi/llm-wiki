---
type: Source
title: "Blind et al. (2023) — Residual estimation for grid modification in wall-modeled large eddy simulation using unstructured high-order methods"
description: "Transfers the Toosi–Larsson LES modelling-residual estimator and its optimal-spacing equidistribution to the DGSEM code FLEXI, with an element-local modal test filter and element-averaged residuals, and uses it to adapt hexahedral meshes with 2-to-1 mortars for wall-resolved and wall-modelled channels and a transonic airfoil."
resource: "doi:10.1016/j.compfluid.2023.105796"
source_kind: paper
authors: [Blind M.P., Kahraman A.B., Larsson J., Beck A.]
year: 2023
venue: "Comput. Fluids 254:105796"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Computers_amp_Fluids_Blind_Residual_estimation_for_grid_modification_in_wall-modeled_la.pdf"
tags: [les, wmles, mesh-adaptation, dg, grid-requirements]
timestamp: 2026-10-26T05:09:00Z
---

# Summary

Blind et al. (2023) carry the grid-adaptation method of Toosi and Larsson,
developed for finite-difference and finite-volume codes, over to the
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
in [FLEXI](/software/flexi.md), with $N=5$, Pirozzoli's split-form fluxes
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md))
and the [Vreman model](/methods/vreman-model.md). The method is a
[mesh adaptation](/methods/mesh-adaptation.md) driven by an a posteriori
estimate of the [LES](/definitions/large-eddy-simulation.md) modelling
residual. The LES solution is test-filtered to an imagined coarser
resolution $\hat\Delta$, and the residual is the difference between the
operator applied to the filtered solution and the filtered operator. For
[implicit LES](/definitions/implicit-les.md) the subgrid terms of the
estimate vanish. In DG the test filter is a one-directional modal cut-off
inside each element; only the Vreman length scale changes at the test level.
The squared residual is evaluated exactly on a degree-$2N$ representation and
averaged over each element, which removes spurious peaks at element
boundaries. The optimal spacing equidistributes the element-integrated
residual in space and direction.

Grids are built by hand to follow the target spacing, with 2-to-1 mortar
interfaces that coarsen the wall-parallel spacing away from the wall. On the
[channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=550$ the method
reproduces the Toosi–Larsson spacing sequence and converges to a grid of about
$(18,1,8)$ wall units per degree of freedom
([grid requirements](/results/les-grid-point-requirements.md)). At
$Re_\tau=2000$ the mortars save about half the elements. For
[wall-modelled LES](/methods/wall-modelled-les.md) (Spalding's
[law of the wall](/definitions/law-of-the-wall.md) as an algebraic
[equilibrium wall model](/methods/equilibrium-wall-model.md), $h_{\mathrm{wm}}=0.1\delta$)
the target spacing below $h_{\mathrm{wm}}$ is clamped to its value at
$h_{\mathrm{wm}}$. A wall-modelled transonic NACA 64A-110 airfoil, started
from six elements per chord, converges to a wall-resolved reference in four
meshes, with element savings of about 50% against meshes without mortars.

# Version read

arXiv preprint 2301.03199v1 [physics.flu-dyn], 9 January 2023 ("Preprint
submitted to arXiv, January 10, 2023"), 31 pages, all read. Its printed
title is "Grid-Adaptation for Wall-Modeled Large Eddy Simulation Using
Unstructured High-Order Methods"; the version of record (Comput. Fluids
254:105796, 2023) carries the title of the metadata above. Same four
authors in the same order and the same abstract content, so the file is
taken as the same manuscript retitled at publication; the journal text,
tables and numbers were not seen. Section, equation, table and figure
numbers on this page are those of arXiv v1.

# Key claims

Page-local symbols, as on the [mesh adaptation](/methods/mesh-adaptation.md) page: $\mathcal E_{\hat\Delta}$ is the estimated modelling residual (the source's $\mathcal F_{\hat\Delta}$), $\mathcal G=\varrho_r h^{a}$ the averaged residual norm, its density and exponent (the source's $G=g\Delta^\alpha$), $N_f$ the highest mode kept by the test filter (the source's $M$), $\Lambda$ the equidistribution constant.

1. The Toosi–Larsson residual-based adaptation transfers to DGSEM, and to any DG or related scheme "with minimal changes, as long as an element-local filter operation can be specified" (§2.1). **Stated**
2. Classical residual estimation (leading Taylor terms, or interpolation onto a finer mesh) fails for LES: a finer grid resolves smaller scales, and LES is far from the asymptotic range (§2.2). **Stated**
3. The modelling residual is estimated as $\mathcal E_{\hat\Delta}=\mathcal R_{\hat\Delta}(\hat{\boldsymbol w}_\Delta)-\widehat{\mathcal R_\Delta(\boldsymbol w_\Delta)}$, with $\mathcal R_\Delta$ the discrete right-hand-side operator, assuming that the test filter commutes with the time derivative (§2.2, Eq. 2, after [1,7]). **Derived** (background)
4. The residual must be defined at the coarser resolution $\hat\Delta$; defining it at $\Delta$ would count again the scales the subgrid model already represents (§2.2). **Stated**
5. The subgrid term of the residual uses the length scale of $\hat\Delta$; for implicit LES without an explicit model the subgrid terms are zero in the estimate (§2.2). **Stated**
6. The DG test filter is an element-local, one-directional modal cut-off: with $N=5$ the coefficients of degrees 4 and 5 are set to zero in one direction only; it works equally on unstructured hexahedral grids (§2.3). **Stated**
7. Only the subgrid length scale is changed when evaluating $\mathcal R_{\hat\Delta}$, so the estimate holds the modelling residual and excludes the numerical error; evaluation at a lower degree is left for future work (§2.3). **Stated**
8. With $\Delta=V_e^{1/3}/(N+1)$ ($V_e$ the element volume) and $N_f=3$, the test-level length is $\hat\Delta=[(N+1)/(N_f+1)]^{1/3}\Delta$ and the test-level eddy viscosity is "a factor of $[(P+1)/(M+1)]^{2/3}\approx1.59$ larger" (§2.3; see Printed slips). **Stated**
9. The square of the residual is computed exactly by mapping $\mathcal E_{\hat\Delta}$ from degree $N$ to degree $2N$ (§2.3). **Stated**
10. Without element averaging the estimator flags element boundaries, an artefact of DG discontinuities and overshooting gradients in under-resolved flow; averaging $\mathcal E_i\mathcal E_i$ over each element before time and homogeneous averaging removes it; the estimator is "most efficient when applied elementwise and not per collocation point" (§§2.3, 5). **Stated** (the unaveraged field is not shown)
11. With $\mathcal G=\varrho_rh^{a}$ the exponent comes from the spectral behaviour of turbulence near the cutoff, not from numerical analysis; the constant $a=2$ used is "almost certainly larger than the 'correct' value in most flow scenarios", which damps variations of the optimal spacing (§2.4, after [18]). **Stated**
12. Minimizing the residual at fixed element count equidistributes the element-integrated residual in space and direction, $\varrho_{r,i}h_{i,\mathrm{opt}}^{a}V_{\mathrm{opt}}=\Lambda$, independently of the norm exponent of the cost functional (§2.4, Eq. 6, after [1]). **Derived** (background)
13. The residual does not tell whether a grid is converged; convergence is judged by the user on quantities of interest (§2.5). **Stated**
14. Wall-resolved channel at $Re_\tau=550$: from $(10,2,3)$ elements, the spacing sequence resembles the finite-difference results of Toosi and Larsson; at iteration $l=4$ ($50\times9\times36=16\,200$ elements, 3 499 200 dof) $\Delta^+\approx(18,1,8)$ per degree of freedom at the wall, "acceptable (albeit a bit fine)", computed $Re_\tau=556.57$ (§3.1, Table 1). **Shown**
15. The suggested $x$ and $z$ spacings are larger in the viscous sublayer than in the buffer layer, which the authors call correct because wall-parallel length scales grow in the viscous sublayer [21] (§3.1, Fig. 1). **Shown**
16. At $Re_\tau=550$ the mean velocity converges to the DNS of Lee and Moser at $l=4$ and the Reynolds stresses already at $l=3$; at $l=0$ element boundaries show in $R_{12}$ with overshoots and a failing weakly imposed no-slip condition (§3.1, Figs. 2–3). **Shown**
17. Mortar rule (FLEXI mortars are 2-to-1 only): keep the smallest required spacing until the optimal spacing has at least doubled, then insert an interface; $x$ and $z$ interfaces may sit at different wall distances (§3.2). **Stated**
18. Wall-resolved channel at $Re_\tau=2000$ with mortars converges at $l=5$ ($Re_\tau=1967.37$, 142 662 elements, 30 814 992 dof, 128 154 elements saved); mortars save "up to approx. 50%" of the elements of a structured mesh of equal spacing; the time step, set by the smallest cell, is unchanged, so the saving is in processors (§3.2, Tables 2–3). **Shown**
19. With mortars $R_{22}$ lags the other stresses; small mortar signatures remain at $l=5$ (§3.2, Fig. 8). **Shown**
20. Wall-modelled adaptation: the estimator sees the strongest under-resolution near the wall, but under-resolution below $h_{\mathrm{wm}}$ is a choice, so the target spacing of cells between the wall and $h_{\mathrm{wm}}$ is reset to its value at $h_{\mathrm{wm}}$ in all directions (§3.3, credited to Toosi, personal communication). **Stated**
21. Wall-modelled channel at $Re_\tau=2000$: Vreman constant raised to 0.11 from "previous experience" (0.03 in the wall-resolved cases, as in [1]), Spalding's law solved by Newton's method, $h_{\mathrm{wm}}=0.1\delta$ ($h^+_{\mathrm{wm}}=200$); the mean velocity agrees with DNS above $h_{\mathrm{wm}}$ at $l=3$, the stresses need $l=4$, and $R_{11}$ does not converge exactly, attributed to wall-modelled LES itself, not to the adaptation (§3.3, Figs. 10–11, Table 4). **Shown**
22. The wall-model exchange point need not lie in the first cell; at $l=4$ it lies in the second (§3.3). **Shown**
23. NACA 64A-110 ($M=0.72$, $Re_c=930\,000$, $0^\circ$), started from an "extremely cheap" mesh of six elements per chord: the indicator refines most in the wall-normal, then the spanwise, then the wall-tangential direction, asks for coarse spanwise spacing at the laminar leading edge, and refines the turbulent wake (§4, Fig. 12). **Shown**
24. Against a wall-resolved reference, $C_p$ converges first, $C_f$ after $l=2$, and $\delta_{99}$, the most sensitive, needs four meshes; the largest discrepancy for $l\le2$ is at the trailing edge, where the algorithm refines (§4, Fig. 13). **Shown**
25. Spanwise mortar zones save up to about 50% of the airfoil elements ($l=3$: 222 426 elements, 214 902 saved), "which directly translates to the same amount of savings in compute time" (§4, Table 6). **Shown**
26. The method is robust, gives solutions at up to 50% lower cost at comparable accuracy compared with human-generated grids, and applies to arbitrary geometries without prior knowledge of the flow (Abstract, §5). **Stated** (the 50% is measured against structured meshes of equal near-wall spacing)

# Printed slips

- **§2.3, factor 1.59.** "a factor of $[(P+1)/(M+1)]^{2/3}\approx1.59$ larger". *(compiler check, not in the sources)* With the printed $P=5$, $M=3$, $(6/4)^{2/3}\approx1.31$; either the number or the exponent is wrong.
- **Table 4 caption** reads "wall-modeled $Re_\tau = 550$ channel" for the wall-modelled $Re_\tau=2000$ case of §3.3, whose tabulated wall spacings (333.33 = 2000/6) belong to $Re_\tau=2000$.
- **Airfoil polynomial degree.** §2.3 states "Throughout this work we used 5th order polynomials, i.e. $P=5$". *(compiler check, not in the sources)* Table 6 gives 512 = $8^3$ dof per element in every row (e.g. 404 480/790), which corresponds to degree 7, whereas the channel tables give $216=6^3$.
- **Table 2, $l=2$.** *(compiler check, not in the sources)* For $l=3$–5 the element totals plus savings equal $N_{1,\max}N_2N_{3,\max}$, but for $l=2$, $20\cdot4\cdot12=960$ against $1320+120=1440$. The text also says the $l=2$ interfaces in $x$ and $z$ lie at the same wall distance so that mesh $l=3$ "will contain one mortar interface", while the $l=2$ row already lists two $N_1$ zones and Table 3 lists 120 saved elements at $l=2$.
- **Wall-normal element counts.** §3.1 speaks of "2 cells along the channel half-width $h$" and Table 1 prints $\Delta_2(y=h)/h=0.50$ with $N_2=2$, while the domain is $(10h,2h,3h)$ and the element total is $N_1N_2N_3=60$; the counts per half-height and per full height are not reconciled (same pattern in Tables 2 and 4).
- **Symbol clash.** $\alpha$ is both the residual exponent (§2.4) and the airfoil angle of attack (§4).
- **Typos.** "The ration" (§3.1), "introduces by Schlatter" (§4), "cordlength", "the use iterative root-finding" (§2.5), "lack behind".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $q_\Delta$, $R$, $R_\Delta$, $\mathcal N_\Delta$ | $\boldsymbol w$, $\boldsymbol w_\Delta$, $\mathcal R$, $\mathcal R_\Delta$ (page-local), (discrete residual operator) | conserved variables; exact and discrete solution, right-hand-side operator |
| $\mathcal F$, $\mathcal F_{\hat\Delta}$, $\mathcal F_{i,\hat\Delta}$ | $\mathcal E$, $\mathcal E_{\hat\Delta}$, $\mathcal E_{i,\hat\Delta}$ (page-local) | **collision:** the registry's $\mathcal F_h$ is the numerically induced filter |
| $\widehat{(\cdot)}$, $\hat\Delta$ | $\hat\phi$, $\hat\Delta$ | agree: test filter; applied to conserved variables, so the filtered velocity is Favre-weighted |
| $\Delta=\mathcal V^{1/3}/(P+1)$ | $\Delta$ | agrees (element size over $N+1$); also used for the grid spacing |
| $P$ | $N$ | polynomial degree, $P=5$ |
| $M$ | $N_f$ (page-local) | **collision:** the registry's $M$ is the Mach number |
| $\tau^{\mathrm{mod}}_{ij}(\rho,u_i,\Delta)$ | $\tau_{ij}$ (modelled) | enters the momentum flux with $+$ beside $p\delta_{ij}$: positive-trace convention, agrees |
| $\sigma_{ij}$ | $\sigma_{ij}$ | agrees |
| $G(\vec x,\vec n)$, $g$, $\alpha$ | $\mathcal G$, $\varrho_r$, $a$ (page-local) | **collision:** $G$ is the filter kernel, $\alpha$ the DG/FV blending factor in the registry |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time, homogeneous-direction and here element average |
| $\lambda$, $\Lambda$, $\beta$, $\mathcal J$ | (Lagrange multiplier, equidistribution constant, norm exponent, cost functional) | **collision:** $\lambda$ is not the Taylor microscale, $\beta$ not the field-inversion correction |
| $\mathcal V$ | $V_e$ (page-local, element volume) | |
| $h$ | $\delta$ | channel half-height |
| $u'u'$, $v'v'$, $w'w'$, $u'v'$ | $R_{11}$, $R_{22}$, $R_{33}$, $R_{12}$ | |
| $C$ | (Vreman constant) | 0.03 wall-resolved, 0.11 wall-modelled |
| $h_{wm}$ | $h_{\mathrm{wm}}$ | agrees |
| $c_p$, $c_f$, $\tau_w$, $\delta_{99}$ | $C_p$, $C_f$, $\tau_w$, $\delta_{99}$ | |
| $Ma$, $Re_c$ | $M$, $Re_c$ | |
| $l$ | (adaptation iteration) | |

# Reference list

24 printed references, numbered style ([1]–[24]). The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [8]
is the ingested [krais-2021](/sources/krais-2021.md) and ref. [14] the
ingested [flad-2017](/sources/flad-2017.md). Refs. [1] and [7] (Toosi &
Larsson) and [24] (Kahraman & Larsson, online first) print no volume; refs.
[19], [20] (Park et al.) print no venue. No printed duplicates or unparseable
items.

# Pages created or updated

Chunk 3 (2026-10-25). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Vreman model](/methods/vreman-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [FLEXI](/software/flexi.md)
