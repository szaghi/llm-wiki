---
type: Source
title: "Zhou & Bae (2024) — Sensitivity analysis of wall-modeled large-eddy simulation for separated turbulent flow"
description: "WMLES of the Boeing Gaussian bump with the exact DNS mean wall stress imposed through three idealized wall conditions, comparing Vreman, dynamic Smagorinsky, AMD and mixed-similarity models on isotropic and anisotropic meshes: the subgrid model, more than the wall condition, decides the separation bubble and its grid convergence."
resource: "doi:10.1016/j.jcp.2024.112948"
source_kind: paper
authors: [Zhou D., Bae H.J.]
year: 2024
venue: "J. Comput. Phys. 506:112948"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Computational_Physics_Zhou_Sensitivity_analysis_of_wall-modeled_large-eddy_simulation_f.pdf"
tags: [wmles, sgs-model, separated-flow, wall-model, grid-requirements, anisotropy]
timestamp: 2026-10-28T07:04:00Z
---

# Summary

Zhou & Bae (2024) study the sensitivity of
[wall-modelled LES](/methods/wall-modelled-les.md) of smooth-body
separation on the spanwise-periodic
[Gaussian bump](/benchmarks/gaussian-bump.md) at $Re_L=2\times10^6$, with
the set-up of the hybrid DNS–wall-resolved LES of Uzun & Malik (called
"DNS" in the paper, separation length $L_s/L=0.32$). To remove the
wall-stress modelling error, the wall carries the DNS mean wall stress
through three idealized conditions: a time-independent velocity Neumann
condition; an "equilibrium" Dirichlet condition with a wall eddy
viscosity calibrated by a running average from the integrated thin
boundary-layer equations ([equilibrium wall model](/methods/equilibrium-wall-model.md));
and a "non-equilibrium" version that keeps the pressure gradient
([non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).
Five closures are compared: the [Vreman model](/methods/vreman-model.md)
with constants 0.025 and 0.07, dynamic Smagorinsky
([dynamic procedure](/methods/dynamic-procedure.md)), the
[AMD model](/methods/anisotropic-minimum-dissipation-model.md) with
constant 0.3, a [mixed-similarity model](/methods/scale-similarity-model.md)
([Smagorinsky](/methods/smagorinsky-model.md) part with $C_s=0.13$), and
no model. Four isotropic meshes (1.94 M to 993 M cells) and three
anisotropic meshes (4:1:2 at equal cell volume) are run in the
energy-conserving incompressible finite-volume code of You, Ham & Moin
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
with a recycled precursor inflow
([inflow generation](/methods/inflow-turbulence-generation.md)).

The bubble depends mostly on the subgrid model. On the baseline mesh only
AMD, Vreman 0.025 and the mixed model separate; dynamic Smagorinsky never
separates in this code, which the authors restrict to their set-up since
other bump studies (Agrawal et al., see the
[dynamic tensor-coefficient model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md))
did capture separation with it. $L_s$ converges monotonically only with
Vreman 0.025; with AMD and Vreman 0.07 the bubble shrinks spuriously on
refinement; the mixed model over-predicts the bubble but consistently
across meshes. The wall condition matters less, mainly through $C_f$.
Anisotropic cells degrade the models that use the cube-root filter
width, not AMD. The reduced subgrid activity of dynamic Smagorinsky near
the wall inflates the first-cell velocity. Evidence is numerical.

# Version read

Version of record (Elsevier; received 25 September 2023, accepted 14
March 2024, online 20 March 2024), 19 pages, all read (pp. 3–5 also
visually). Page 1 matches the metadata; no identity issue. Equation,
figure, table and section numbers are those of this version.

# Key claims

Page-local symbols: $L$ the bump width (reference length, not the
integral scale), $h_b=0.085L$ and $x_0=0.195L$ the bump height and width
parameter; $L_s$ the horizontal separation length; $\Delta_c=V_c^{1/3}$
the characteristic cell size; $\nu_{t,w}$ the effective wall eddy
viscosity; $\breve u_{1,c}$ the running time average of the first-cell
velocity (the source's overbar); $T_r$ its averaging time; $c_{\mathrm V}$
the Vreman constant; $s_a$ the SGS activity; $\varepsilon_\nu=2\nu\bar S_{ij}\bar S_{ij}$
the resolved viscous dissipation.

1. On the baseline isotropic mesh with the Neumann condition, mean separation occurs only with AMD, Vreman ($c_{\mathrm V}=0.025$) and the mixed model; the Vreman 0.025 bubble is "similar to the DNS", the mixed-model one "significantly larger"; no model, dynamic Smagorinsky and Vreman 0.07 stay attached (§3.1, Fig. 4). **Shown**
2. The mean SGS viscosity in the turbulent boundary layer is of the order of the molecular viscosity; AMD gives the largest and Vreman 0.025 the smallest; the mixed model raises it in the shear layer downstream of the peak (§3.1, Fig. 5). **Shown**
3. Wall $C_p$ agrees upstream of the peak and on the downstream flat wall but differs around the peak and on the leeward side; Vreman 0.025 agrees best with the DNS (§3.1, Fig. 6). **Shown**
4. Because the Neumann condition imposes the DNS mean wall stress, $L_s$ cannot be read from $C_f$; it is measured from the sign of $\langle u_1\rangle$ at the first off-wall cell centre ($x_2/L=2.38\times10^{-4}$ on the baseline mesh) (§3.1, Fig. 7). **Stated** (method choice)
5. The first-cell velocity differs between subgrid models over the whole domain; dynamic Smagorinsky matches the DNS best where the pressure gradient is small, the mixed model gives a lower velocity; hence "the performance of wall models can be sensitive to the choice of the SGS model" (§3.1, Fig. 7). **Shown**
6. The fine mesh ($\Delta_c/L=2.38\times10^{-4}$) approaches grid convergence, especially with AMD and Vreman; the DNS bubble is $L_s/L=0.32$ with a DNS cell size $\approx1.10\times10^{-4}L$ (§3.1, Fig. 8). **Shown**
7. $L_s$ converges to the DNS monotonically for Vreman 0.025 and non-monotonically for AMD and Vreman 0.07, "leading to a spurious diminishment or shrinking of the separation bubble upon mesh refinement", in agreement with [11, 27], which ties non-monotonic WMLES convergence to the subgrid model (§3.1, Fig. 8). **Shown**
8. The mixed model (fixed $C_s=0.13$, not optimized) predicts a larger bubble than the others but sizes consistent across meshes, which the authors read as a possible benefit of SGS-stress anisotropy [47] (§3.1, Fig. 8; Conclusion 2). **Shown** / **Stated** (attribution)
9. WMLES without a subgrid model improves markedly on the fine mesh, where the boundary layer in the separated region is covered by more than 150 cells, approaching wall-resolved resolution (§3.1). **Shown**
10. Upstream of the peak AMD and both Vreman models give profiles closer to the DNS; on the leeward side the mixed model over-predicts and all others under-predict the boundary-layer thickness, Vreman 0.025 the most accurate (§3.1, Fig. 9). **Shown**
11. The SGS dissipation $\Pi=-\tau_{ij}\bar S_{ij}$ rises strongly on the leeward side; the mixed model dissipates most at all stations, AMD most among the eddy-viscosity models (§3.1, Fig. 10). **Shown**
12. SGS activity $s_a=\langle\Pi\rangle/(\langle\Pi\rangle+\langle\varepsilon_\nu\rangle)$: subgrid dissipation dominates across the boundary layer for the mixed model and AMD, and is comparable to the viscous one for Vreman 0.025; dynamic Smagorinsky's activity drops in the near-wall cells, which amplifies the first-cell mean velocity, in line with [15, 49] (§3.1, Fig. 11). **Shown**
13. Dynamic Smagorinsky predicts no bubble on any mesh; the authors restrict this to their solver and set-up, note that Iyer & Malik [12, 50] also found none while [11, 27] found one, and attribute the difference possibly to clipping, filtering, mesh topology and numerics (§3.1). **Shown** / **Stated** (attribution)
14. That the dynamic model's correct near-wall asymptotics in wall-resolved LES without damping carries over to coarse-mesh WMLES is "an open question" (§3.1, §4). **Stated**
15. On the fine mesh the profiles at $x/L=-0.709$ and $-0.025$ agree with each other and the DNS but differ at $x/L=0.2$: the subgrid-model dependence persists without upstream-history effects (§3.1, Fig. 12). **Shown**
16. An inflow generated with AMD instead of dynamic Smagorinsky ($\delta_{\mathrm{in}}/L=0.0062$, $Re_\theta\approx1126$, $Re_\tau\approx630$) changes the bump profiles negligibly (App. A, Fig. A.21). **Shown**
17. With the two $\nu_{t,w}$ conditions $C_f$ differs between models in $x/L\in(0,0.7)$; part of the discrepancy comes from clipping $\nu_{t,w}\ge0$, which occurs only there, "with an average occurrence rate below 13% in each case" (§3.2, Fig. 13). **Shown**
18. With both $\nu_{t,w}$ conditions the subgrid model and the mesh still decide $L_s$; non-monotonic convergence persists with AMD and Vreman 0.07; the mixed model stays consistent; the wall condition has "a negligible impact on the convergence behavior" (§3.2, Fig. 14). **Shown**
19. Measured by $C_f$, the non-equilibrium condition "notably improves" the bubble for eddy-viscosity models; measured by the first-cell velocity the two conditions differ little, and the equilibrium results resemble the Neumann ones (§3.2, Fig. 14). **Shown**
20. The wall condition and the subgrid model interact: for Vreman 0.07 the three conditions agree; for the mixed model and Vreman 0.025 the $\nu_{t,w}$ conditions move reattachment downstream and lengthen the bubble; the Vreman model is sensitive to its constant (§3.2, Figs. 15–16). **Shown**
21. The wall condition "can enhance the prediction of flow separation, it has a less dominant effect on the simulation compared to the SGS model", its influence "mainly limited to the skin friction on the wall" (§3.2, Conclusion 3). **Shown**
22. Anisotropic cells (4:1:2, same cell volume and spanwise spacing) degrade the bubble, especially for Vreman 0.025; for the mixed model the bubble grows on the two coarser anisotropic meshes and shrinks strongly on the baseline one, losing its isotropic-mesh consistency (§3.3, Fig. 17). **Shown**
23. AMD's $C_p$ and first-cell velocity barely change with mesh type, while Vreman 0.025 and the mixed model change over the whole domain and the separated boundary layer at $x/L=0.2$ becomes attached or nearly so on anisotropic meshes (§3.3, Figs. 18–20). **Shown**
24. All models except AMD take the filter width as the cube root of the cell volume, adequate on isotropic cells and error-prone on anisotropic ones; AMD, "specifically designed for anisotropic meshes", mitigates that error (§3.3). **Stated** (interpretation, not isolated by a test)
25. On isotropic meshes Vreman 0.025 is "comparatively robust" (accurate attached layer and bubble, monotonic convergence), but users "should be cautious" because of its sensitivity to mesh anisotropy (§4, Conclusion 5). **Shown**
26. The authors call for subgrid models robust for separation, monotonic convergence and anisotropic meshes, citing the non-Boussinesq model of Agrawal et al. [27], the dynamic nonlinear model of Uzun & Malik [51] and unified subgrid/wall models such as the [building-block flow model](/methods/building-block-flow-wall-model.md) [29, 52] (§4). **Stated**

The closures and wall conditions in registry notation. The mixed model
(Eq. 1) is $\tau_{ij}=-2(C_s\Delta)^2|\bar S|\bar S_{ij}+(\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j)$
with a Gaussian secondary filter (width not printed) and $\Delta$ the
cube root of the cell volume; the Vreman, dynamic and AMD formulas are
not printed. From the thin boundary-layer equations, integrated from the
wall to the first cell centre $h_{\mathrm{wm}}$ (the source's $h_c$),
$\tau_{w,i}\approx\rho(\nu+\nu_{t,w})u_{i,c}/h_{\mathrm{wm}}$ (Eq. 4);
the equilibrium condition sets
$\nu_{t,w}\approx\tau^{\mathrm{DNS}}_{w,1}/(\rho\breve u_{1,c}/h_{\mathrm{wm}})-\nu$
(Eq. 5) with the running average
$\breve u_{1,c}^{n+1}=(\Delta t/T_r)u_{1,c}^{n+1}+(1-\Delta t/T_r)\breve u_{1,c}^n$
(Eq. 6, $T_r=0.3L/U_\infty$, then $6L/U_\infty$), and the wall stress
$\tau_{w,i}=\rho(\nu+\nu_{t,w})\partial_2u_i|_w$ (Eq. 7); the
non-equilibrium condition adds $\tfrac12h_{\mathrm{wm}}\partial_1p$ to the
numerator of Eq. (5) and subtracts $\tfrac12h_{\mathrm{wm}}\partial_ip$
from the wall stress (Eqs. 8–9) *(compiler check, not in the sources:
integrating $\rho(\nu+\nu_{t,w})\partial_2u_1=\tau_{w,1}+x_2\partial_1p$
from 0 to $h_{\mathrm{wm}}$ gives the printed $\tfrac12h_{\mathrm{wm}}\partial_1p$)*.
$\nu_{t,w}$ is clipped at zero. Meshes (Table 1): $\Delta_c/L=1.90\times10^{-3}$,
$9.52\times10^{-4}$, $4.76\times10^{-4}$, $2.38\times10^{-4}$ with
$1050\times44\times42$ to $8400\times352\times336$ cells; the fine mesh
has 10–30 wall units in attached regions. Each run spends 2 flow-through
times on transients and 3 on statistics, at CFL 1.0.

# Printed slips

None found in the equations or tables *(compiler check, not in the
sources: the Table 1 cell counts multiply to the printed totals, e.g.
$8400\times352\times336\approx993$ M, and the 4:1:2 anisotropic counts
keep the cell volume)*. Text: "Whitmore et al. [15] delves" (§1). Ref.
[2] prints the article number "15–00418" as a page range.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde{(\cdot)}$ | $\bar\phi$ | implicit grid filter (incompressible; not Favre); dropped after Eq. (1) |
| $\hat{(\cdot)}$ | $\hat\phi$ | Gaussian secondary filter of the similarity term |
| $\overline{(\cdot)}$ (Eq. 6) | $\breve\phi$ (page-local) | running time average; **collision** with the LES filter |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time and spanwise average |
| $\tau_{ij}$ | $\tau_{ij}$ | positive-trace convention (eddy part $-2\nu_t\bar S_{ij}$) |
| $S_{ij}$, $\lvert S\rvert=(2S_{ij}S_{ij})^{1/2}$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | factor two included |
| $c$ (Vreman) | $c_{\mathrm V}$ (page-local) | 0.025 or 0.07; formula not printed |
| AMD constant | $C_{\mathrm{AMD}}$ | 0.3 |
| $C_s$ | $C_s$ | 0.13 in the mixed model |
| $\Delta$, $\Delta_c=\sqrt[3]{V_c}$, $\Delta_1,\Delta_2,\Delta_3$ | $\Delta$, $\Delta_c$ (page-local), $\Delta_k$ | |
| $x_1,x_2,x_3$; $u_1,u_2,u_3$ | wall-local streamwise, wall-normal, spanwise | the global frame is $x,y,z$ |
| $h_c$, $u_{i,c}$ | $h_{\mathrm{wm}}$, $U_{\mathrm{LES}}$ components | first off-wall cell centre |
| $\nu_{t,w}$ | $\nu_{t,w}$ (page-local) | kinematic counterpart of the wall-model viscosity $\mu^w_{\mathrm{sgs}}$ (§11) |
| $\tau^{\rm DNS}_{w,1}$, $\tau_{w,i}$ | $\tau_w$ (DNS mean), wall-stress components | |
| $T$ (Eq. 6) | $T_r$ (page-local) | **collision** with the temperature $T$ |
| $\epsilon_t=-\tau_{ij}S_{ij}$ | $\Pi$ | SGS energy flux |
| $\epsilon_\nu$, $s_a$ | $\varepsilon_\nu$, $s_a$ (page-local) | activity parameter of Geurts & Fröhlich |
| $f_b=h\exp[-(x/x_0)^2]$, $h$, $L$ | $h_b$, $x_0$, $L$ (page-local) | **collision:** $h$ is the cell size, $L$ the integral length |
| $Re_L$, $L_s$, $C_p$, $C_f$ | $Re_L$, $L_s$ (page-local), $C_p$, $C_f$ | based on $\tfrac12\rho U_\infty^2$ |
| $\delta_{in}$, $Re_\theta$, $Re_\tau$ | $\delta_{\mathrm{in}}$, $Re_\theta$, $Re_\tau$ | precursor inflow boundary layer |
| "DNS" | (hybrid DNS–wall-resolved LES of Uzun & Malik) | |

# Reference list

52 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug.
Same-author same-year works are keyed in printed order (Zhou 2022, Uzun
2022, Gray 2022). Refs. [3], [27] and [47] are the ingested
[bose-2018](/sources/bose-2018.md), [agrawal-2022](/sources/agrawal-2022.md)
and [inagaki-2023](/sources/inagaki-2023.md). Ref. [2] prints an article
number as a page range; [5], [6], [7], [36] print no page or article
number; [37] and [49] are Stanford theses; [47] prints "K. Inagaki, H.
Kobayashi, et al."; [12] prints "ICCFD11 Paper, vol. 204, 2022". No item
is unparseable.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Gaussian (Boeing) bump](/benchmarks/gaussian-bump.md)
- [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
- [Building-block-flow wall model](/methods/building-block-flow-wall-model.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Vreman model](/methods/vreman-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [CharLES](/software/charles.md)
