---
type: Source
title: "Davidovits et al. (2022) — Turbulence generation by shock interaction with a highly nonuniform medium"
description: "Simulates strong shocks crossing media with order-unity density fluctuations in an idealized laser-driven shock tube, and fits the post-shock velocity dispersion and turbulent Mach number with Richtmyer–Meshkov-inspired scalings and Favre-averaged turbulent shock-jump relations that predict reduced post-shock pressure and density."
resource: "doi:10.1103/physreve.105.065206"
source_kind: paper
authors: [Davidovits S., Federrath C., Teyssier R., Raman K.S., Collins D.C., Nagel S.R.]
year: 2022
venue: "Phys. Rev. E 105:065206"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physical_Review_E_Davidovits_Turbulence_generation_by_shock_interaction_with_a_highly_non.pdf"
tags: [compressible, implicit-les, anisotropy, astrophysics]
timestamp: 2026-10-26T20:51:00Z
---

# Summary

Davidovits et al. (2022) study numerically how a strong, initially planar
shock crossing a medium of highly non-uniform density, with normalized
density standard deviation $(\sigma_\rho/\langle\rho\rangle)_0\sim1$,
generates post-shock turbulence. That amplitude lies outside the
small-perturbation regime of most linear theories of shock–turbulence and
shock–inhomogeneity interaction. The motivation is controlled generation
of compressible turbulence in a laser-driven high-energy-density shock
tube. The simulations use the radiation-hydrodynamics code HYDRA with
arbitrary Lagrangian–Eulerian hydrodynamics: radiation only launches the
shock, after which the working material is an ideal gas with $\gamma=5/3$,
no physical viscosity or heat conduction, and artificial viscosity for the
shock. The authors therefore say the runs "should not be regarded as
[direct numerical simulation](/definitions/direct-numerical-simulation.md)"
but are "in the spirit of [implicit large eddy simulations](/definitions/implicit-les.md)",
and they analyse only large-scale averages, which they expect to depend
least on [numerical dissipation](/properties/numerical-dissipation.md). The
non-uniformity is built from low-density voids (and, at the highest
variance, dense beads) on a randomly perturbed close-packed lattice. A 2D
suite varies the shock Mach number, the density variance and the void
radius; six 3D runs supplement it.

The results are collected on
[shock-generated turbulence](/results/shock-generated-turbulence.md). The
post-shock velocity dispersion follows a scaling inspired by linear
Richtmyer–Meshkov theory, $\sigma_v\propto A_\sigma U_s$ with a pre-shock
"average Atwood number" $A_\sigma$, times a dimensional-analysis factor
$r_v^{1/3}$ in the void radius. The turbulent Mach number obeys the same
law with the shock speed replaced by the shock Mach number relative to the
post-shock sound speed, which saturates at $4/\sqrt5\approx1.79$ for
$\gamma=5/3$, so stronger drives give diminishing returns. Favre-averaged
jump conditions for a single average normal shock with a Reynolds-stress
term, expanded to first order, predict post-shock pressure and density
reductions that match the runs fairly; the pressure can fall below half
its unperturbed value. The paper is peripheral to closure modelling: it
proposes scalings and jump relations, not a turbulence model.

# Version read

arXiv preprint arXiv:2205.15998v1 [physics.plasm-ph], 31 May 2022, 15
pages, all read (main text pp. 1–11, Appendices A–B pp. 12–13, references
pp. 13–15). The preprint prints the title "Turbulence Generation by Shock
Interaction with a Highly Non-Uniform Medium", the Crossref record of the
version of record (Phys. Rev. E 105:065206) "Turbulence generation by
shock interaction with a highly nonuniform medium": the same work, with the
same six authors in the same order. Locators are those of the preprint;
the Fig. 6 caption inconsistency below may have been corrected in print.

# Key claims

1. Most theories of shocks through non-uniform media and of shock–turbulence interaction [1, 6, 7, 19–27] hold formally only for small upstream perturbations and a single passage of material through the shock; the present cases with $\sigma_\rho/\langle\rho\rangle\sim1$ violate these assumptions, and the shock front can break into several fronts (§I). **Stated**
2. Without physical viscosity and heat conduction and with artificial viscosity, the simulations "should not be regarded as direct numerical simulation (DNS), but are rather in the spirit of implicit large eddy simulations [31]"; only large-scale quantities, expected to be least influenced by numerical dissipation, are analysed (§II A). **Stated**
3. Doubling the resolution in each direction for a subset of 2D cases leaves the reported scalings unchanged; for $r_v\approx45\ \mu$m, $(\sigma_\rho/\langle\rho\rangle)_0\sim1.05$, $M_s\sim18$ the analysis-region averages change by 0.6%–2.9% depending on the quantity (§II A). **Shown**
4. In a 3D run ($r_v=90\ \mu$m, $(\sigma_\rho/\langle\rho\rangle)_0\sim0.9$, $M_s\sim18$) the PDF of the fluctuating speed is close to a Maxwell–Boltzmann distribution set by $\langle\sigma_v\rangle_{\mathrm{AR}}$, "the velocity distribution observed for fully-developed turbulent flows, even at high Mach number" (Fig. 3b, citing Federrath [34]). **Shown** / **Stated**
5. The transverse velocity spectra are broad, with a peak at the mode number set by the void diameter, $n_\perp\approx11$ for $r_v=90\ \mu$m and $\approx8$ for $r_v=120\ \mu$m (Fig. 3c). **Shown**
6. The post-shock velocity dispersion follows the linear-Richtmyer–Meshkov-inspired proportionality $\sigma_v\propto A_\sigma U_s$, with $A_\sigma=(\sigma_\rho/\langle\rho\rangle)_0/[1+(\sigma_\rho/\langle\rho\rangle)_0]$, as Inoue et al. [4] observed for young supernova remnants (§III, Fig. 4). **Shown**
7. The void radius affects the dispersion; a dimensional argument (energy injection rate $\sim u^3/l$, comparable injection, forcing scale $\propto r_v$) suggests $\sigma_v\propto r_v^{1/3}$, and the 2D suite is fitted by $\langle\sigma_{v,2D}\rangle_{\mathrm{AR}}=0.52(r_v/45)^{1/3}A_\sigma U_s$ (Eq. 2; $r_v$ in microns, velocities in km/s). The coefficient is "chosen to approximately fit the data" and depends on set-up choices such as the averaging window; "it is possible there is some alternate explanation" (§III). **Shown** (fit) / **Derived** (dimensional hypothesis)
8. For a given drive the shock speed is relatively insensitive to $r_v$, consistent with Kim et al. [35] (§III). **Shown**
9. The 3D runs follow the scalings of Eq. 2 with a coefficient $\sim0.6$; the authors cannot firmly attribute the difference to geometry rather than statistical variation (§III). **Shown**
10. The scatter of $\langle\sigma_v\rangle_{\mathrm{AR}}$ grows with $r_v$ because fewer voids fall in the fixed averaging window; repeats with different random void shifts show the most spread at $r_v=90\ \mu$m (§III). **Shown**
11. Inoue et al. [4], in 3D with an isotropic $k^{-5/3}$ density spectrum peaked at the box size, find a coefficient of 1 ($\sigma_v=A_\sigma U_s$) (§III, §IV). **Stated**
12. The turbulent Mach number $M_t=\langle\sigma_v\rangle_{\mathrm{AR}}/\langle c\rangle_{\mathrm{AR}}$ fits $M_t=0.52(r_v/45)^{1/3}A_\sigma\,\mathcal M_s$ (Eq. 3), with $\mathcal M_s=U_s/\langle c\rangle_{\mathrm{AR}}$; points with equal $A_\sigma$ and different $U_s$ cluster because $\mathcal M_s$ saturates (Fig. 5). **Shown**
13. From the Rankine–Hugoniot relations, $\mathcal M_s=(\gamma+1)M_s^2/\sqrt{(2\gamma M_s^2-\gamma+1)((\gamma-1)M_s^2+2)}$ (Eq. 4), which tends to $(\gamma+1)/\sqrt{2\gamma(\gamma-1)}=4/\sqrt5\approx1.79$ for strong shocks at $\gamma=5/3$; hence "a rapidly diminishing return to driving with higher-Mach shocks", a constraint that relaxes as $\gamma\to1$ (§III). **Derived**
14. No feedback of turbulence generation on the volume-averaged post-shock temperature is discernible: it clusters by drive strength and is insensitive to $\langle R_{xx}\rangle_{\mathrm{AR}}/U_s^2$ (Fig. 6). **Shown**
15. Treating the broken-up transition as one average normal shock, the Favre-averaged jump conditions with the Reynolds stress (Eqs. 5–7, after [23, 33]; triple and temperature–velocity correlations and the pre-shock pressure dropped, no pre-shock turbulence),
$$[\![\langle\rho\rangle\langle u\rangle_\rho]\!]=0,\qquad[\![\langle\rho\rangle\langle u\rangle_\rho^2+\langle p\rangle+\langle\rho\rangle R_{xx}]\!]=0,$$
$$\Big[\!\Big[\tfrac12\langle\rho\rangle\langle u\rangle_\rho^3+\tfrac{\gamma}{\gamma-1}\langle p\rangle\langle u\rangle_\rho+\langle\rho\rangle\langle u\rangle_\rho\big(R_{xx}+\tfrac12R_{ii}\big)\Big]\!\Big]\approx0,$$
with $R_{ii}=R_{xx}\big(1+(n_d-1)/\Theta\big)$, give to first order in $R_{xx}/U_s^2$ (Eqs. 8–9)
$$\frac{\langle\rho\rangle_1}{\langle\rho\rangle_{1,0}}\approx1-\frac{2\Theta(3-\gamma)-2(n_d-1)(\gamma-1)}{4\Theta}\,\frac{\gamma+1}{\gamma-1}\,\frac{R_{xx}}{U_s^2},\qquad\frac{\langle p\rangle_1}{\langle p\rangle_{1,0}}\approx1+\frac{(n_d-1)(\gamma-1)^2+\Theta(1-6\gamma+\gamma^2)}{4\Theta}\,\frac{\gamma+1}{\gamma-1}\,\frac{R_{xx}}{U_s^2},$$
and, at $\gamma=5/3$ (Eqs. 10–11), $\langle\rho\rangle_1/\langle\rho\rangle_{1,0}\approx1-\tfrac83\big(1-\tfrac{n_d-1}{2\Theta}\big)R_{xx}/U_s^2$ and $\langle p\rangle_1/\langle p\rangle_{1,0}\approx1-\tfrac89\big(7-\tfrac{n_d-1}{2\Theta}\big)R_{xx}/U_s^2$ (§III). **Derived**
16. The simulations agree "fair[ly]" with Eqs. 10–11; for the largest $\langle R_{xx}\rangle_{\mathrm{AR}}/U_s^2$ the post-shock pressure is "more than halved" relative to the unperturbed case (Fig. 7, plotted with $n_d=3$, $\Theta=1$). **Shown**
17. The pressure jump is relatively insensitive to the anisotropy (for $\Theta\gtrsim1$) and to the dimension, the density jump more sensitive; the simulated pressures collapse on one line even when $n_d$ and $\Theta$ are ignored (Figs. 7, 8). **Derived** + **Shown**
18. The unperturbed runs give analysis-region density jumps of about 3.3–3.8 (Fig. 8 caption), below the strong-shock limit 4 for $\gamma=5/3$ (§IV). **Shown**
19. Eq. 2 also fits the mass-weighted dispersion $\langle\sqrt{R_{ii}}\rangle_{\mathrm{AR}}$ reasonably well; with the anisotropy this can "close" the jump relations (§III). **Shown** / **Stated**
20. The anisotropy $\Theta=\langle R_{xx}\rangle_{\mathrm{AR}}/\langle R_{yy}\rangle_{\mathrm{AR}}$ grows with $\langle R_{xx}\rangle_{\mathrm{AR}}/U_s^2$, with trend lines $\Theta\sim1+13(\langle R_{xx}\rangle_{\mathrm{AR}}/U_s^2-1/40)$ in 2D and $\Theta\sim1+26\langle R_{xx}\rangle_{\mathrm{AR}}/U_s^2$ in 3D; the slope ratio 2 follows from $R_{ii}=R_{xx}(1+(n_d-1)/\Theta)$ with comparable $R_{ii}$ in 2D and 3D (Fig. 9, §III). **Shown** (fit) / **Derived** (factor 2)
21. Moving the analysis region downstream lowers the anisotropy towards equilibrium ("not shown"), as in wind-tunnel shock–turbulence experiments [38] (§III). **Stated**
22. An equipartition estimate (post-shock densities $\gtrsim0.1$ g/cm³, fluctuating velocities $\lesssim40$ km/s) gives magnetic fields of $\sim10$–100 T and magnetic $\beta_p\gtrsim2$; the authors "do not claim such fields would necessarily be present" (§IV). **Derived** (order of magnitude)
23. The coefficient $0.52(r_v/45)^{1/3}$ must have a maximum by momentum and energy conservation, and the $r_v$ scaling must saturate at or before the domain size; $A_\sigma\le1$ by definition (§IV). **Stated**
24. Runs with a tabular carbon equation of state give unperturbed compression ratios that "well exceed" the $\gamma=5/3$ limit of 4, suggesting a lower effective $\gamma$ when the material ionizes (§IV). **Stated** (not shown)
25. Linear Richtmyer–Meshkov theory fits better with the post-shock Atwood number [29, 43]; the paper uses pre-shock quantities for predictive purposes (§IV). **Stated**

# Printed slips

- **Fig. 6 caption against Table I and §II A.** The caption lists "$M_s\sim14$ (circle, black), $M_s\sim16$ (down triangle), $M_s\sim20$ (star), $M_s\sim22$ (up triangle), $M_s\sim37$ (x, brightest red)" and 3D runs "for $M_s\sim20$ … and $M_s\sim37$"; Table I and §II A give $M_s\sim12$, 15, 18, 20, 37 and 3D runs at 18 and 37.
- **Fig. 8 caption.** "$y=(\langle\overline\rho_1\rangle/\overline\rho_0)/(\langle\overline\rho_{1,\tau_0}\rangle)/\rho_{0,\tau_0})$" has one closing parenthesis too many.
- **3D density variances.** The Table I caption lists a 3D case [18, 1.07, 120]; Appendix A gives $\sim1.03$ for the single higher-variance 3D case and $\sim0.87$ for the main 3D cases, which Table I lists as 0.9 (the caption calls the values approximate).
- **Direction names (§II B).** "averaged over the shock-normal directions ($y$ or $y,z$) to create average profiles that depend on the shock-parallel coordinate": $y,z$ lie in the plane of the average shock front and $x$ is the propagation direction; the Fig. 3 caption calls the $y$–$z$ slice "perpendicular to the shock propagation direction (in a plane parallel to the average shock front)".
- **Abstract.** "Richtymer-Meshkov"; the abstract calls $\sigma_\rho/\rho$ a "normalized variance", while §II A defines it as the standard deviation divided by the mean.
- **Symbol reuse.** $R$ is both the void radius and the gas constant in $\overline p=\overline\rho R\tilde T$; $\alpha$ is both the anisotropy and a tensor index in $\tau_{\alpha\beta}$.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$; $y$, $z$ | $x$ (propagation, shock moves to $-x$); $y$, $z$ (transverse, homogeneous) | not wall-normal and spanwise |
| $v_x,v_y,v_z$ | $u,v,w$ | |
| $\overline f$ (volume-weighted average over $y$, $z$ in a slab of width 0.01 mm, Eq. 1) | $\langle f\rangle$ (plane average) | **collision:** the source's overbar is not an LES filter |
| $\tilde f$ (mass-weighted slab average) | $\langle f\rangle_\rho$ | **collision:** the source's tilde is a Favre average, not a Favre filter |
| $f'$, $f''$ | $f'$, $f''$ | fluctuations about the volume- and mass-weighted averages |
| $\langle f\rangle$ (second-stage average over the analysis region $x\in[1.1,1.3]$ mm) | $\langle f\rangle_{\mathrm{AR}}$ (page-local) | **collision** with the registry's Reynolds-average brackets |
| $\tau_{\alpha\beta}=\widetilde{v''_\alpha v''_\beta}$ | $R_{ij}=\langle u_i''u_j''\rangle_\rho$ | **collision:** the source's $\tau$ is a Favre Reynolds stress per unit mass (positive trace), not the SGS stress; the registry's Favre form $\langle\rho u_i''u_j''\rangle$ divided by $\langle\rho\rangle$ |
| $\alpha=\tau_{xx}/\tau_{yy}$ | $\Theta$ (page-local anisotropy ratio) | **collision** with the DG blending factor $\alpha$ |
| $d$ | $n_d$ (page-local dimension, 2 or 3) | **collision** with the wall distance $d$ |
| $R$ (void radius, microns) | $r_v$ (page-local) | **collision** with $R_{ij}$ and with the source's own gas constant |
| $\overline A$ | $A_\sigma$ (page-local pre-shock average Atwood number) | not the two-fluid Atwood number $(\rho_2-\rho_1)/(\rho_2+\rho_1)$ |
| $\overline U_s$ | $U_s$ (page-local mean shock speed) | |
| $M_s$, $\overline M_s$ | $M_s$ (page-local pre-shock shock Mach number) | |
| $\mathcal M_s$, $\overline{\mathcal M}_s$ | $\mathcal M_s$ (page-local shock speed over post-shock sound speed) | |
| $\sigma_M$ | $M_t$ | defined with the volume-weighted dispersion and the average sound speed |
| $C_s$, $C_{s,0}$ | $c$, $c_0$ (page-local sound speed, pre-shock value) | $c_1$ the mean post-shock value |
| $\sigma_f$, $\sigma_v$ | $\sigma_f$, $\sigma_v$ (page-local volume-weighted dispersions) | $\sigma_v^2=\sigma_{u}^2+\sigma_{v}^2+\sigma_{w}^2$ |
| subscript $\tau_0$ | subscript $1,0$ on post-shock quantities (page-local unperturbed case) | |
| $[\![f]\!]$ | $[\![f]\!]=f_1-f_0$ | 0 pre-shock, 1 post-shock |
| $\gamma$ | $\gamma$ | ratio of specific heats, 5/3 |
| $n_\perp$ | $n_\perp$ (page-local transverse mode number) | |

# Reference list

46 printed references, numbered (APS) style with titles. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Incomplete printed items are recorded as printed: [37] (Dhawalikar et
al., MNRAS 2021) and [42] (Barbeau et al., Phys. Plasmas 2021) without
volume or pages, [36] (Landau & Lifshitz) without publisher, [1] and [19]
(NASA Lewis reports) without report numbers. Several items print a URL in
place of a DOI field. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 3 (2026-10-26), cited further in chunk 6. This source is cited on:

- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
