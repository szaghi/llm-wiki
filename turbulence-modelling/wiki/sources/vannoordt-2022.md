---
type: Source
title: "van Noordt et al. (2022) — An immersed boundary method for wall-modeled large-eddy simulation of turbulent high-Mach-number flows"
description: "Sharp ghost-cell immersed-boundary method coupled to an equilibrium wall model for hypersonic WMLES in a Cartesian finite-difference code: single-ghost-cell WENO boundary closure chosen by pseudospectral stability analysis, least-squares viscous stencils, two-point ray sampling, verified by manufactured solutions and validated on channel, Mach-6 plate, shock interaction and Mach-7.2 ramp."
resource: "doi:10.1016/j.jcp.2022.111583"
source_kind: paper
authors: [van Noordt W., Ganju S., Brehm C.]
year: 2022
venue: "J. Comput. Phys. 470:111583"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_van_An_immersed_boundary_method_for_wall-modeled_large-eddy_simu.pdf"
tags: [immersed-boundary, wmles, wall-model, hypersonic, shock-boundary-layer-interaction, numerical-dissipation]
timestamp: 2026-10-27T15:28:00Z
---

# Summary

van Noordt et al. (2022) couple a sharp ghost-cell
[immersed boundary method](/methods/immersed-boundary-method.md) to
[wall-modelled LES](/methods/wall-modelled-les.md) for compressible,
high-Mach-number turbulent flows in the Cartesian finite-difference solver
CHAMPS (block-structured octree [mesh adaptation](/methods/mesh-adaptation.md)),
and claim the first published hypersonic simulations that combine WMLES
with an IBM. The convective flux blends a fourth-order kinetic-energy- and
entropy-preserving centred flux ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
[entropy conservation](/properties/entropy-conservation.md)) with a
third-order [WENO](/methods/weno-scheme.md) flux-vector-splitting flux,
the blending factor $\alpha$ given by a Ducros-type
[sensor](/definitions/shock-sensor.md) in the interior and prescribed in
the first three irregular cells. Only one ghost cell enters the upwind
reconstruction: new two-candidate boundary stencils, one downwind-biased,
are derived, and their free parameter is fixed by a spectral and
pseudospectral stability analysis of the RK4-discretized advection
operator. Viscous fluxes at irregular faces use overdetermined
least-squares stencils matching the interior truncation error; the wall
shear stress and heat flux of an ODE
[equilibrium wall model](/methods/equilibrium-wall-model.md) (van Driest
damping in Trettel–Larsson semi-local coordinates,
[compressible velocity transformation](/definitions/compressible-velocity-transformation.md))
enter directly as viscous fluxes, an explicit alternative to the dynamic
[slip-wall](/methods/slip-wall-model.md) condition of Bose & Moin, which
the paper contrasts but does not use. The SGS model is the
[WALE model](/methods/wale-model.md) without compressibility correction.

The [method of manufactured solutions](/methods/method-of-manufactured-solutions.md)
on a sphere shows the boundary treatment at least second order. Validation:
a [channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=5200$ (the
interior [numerical dissipation](/properties/numerical-dissipation.md)
matters far more than the irregular-cell one; the log-region deviation,
cf. [log-layer mismatch](/definitions/log-layer-mismatch.md), vanishes with
refinement), a Mach-6 transitional flat-plate
[boundary layer](/benchmarks/turbulent-boundary-layer.md), a Mach-6
transitional [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
aligned with and rotated against the grid (0–12°), and a Mach-7.2 8°
compression ramp against DNS, at under 5% of the DNS cell count
([grid requirements](/results/les-grid-point-requirements.md)). Heat
transfer is very sensitive to the dissipation added at the immersed
boundary; separation and post-shock adjustment on the ramp, and acoustic
reflections at coarse–fine interfaces, are the remaining discrepancies.

# Version read

Version of record (J. Comput. Phys. 470:111583, Elsevier typeset, open
access CC BY; received 15 Nov 2021, online 5 Sep 2022), 30 pages, all read;
the equation pages whose text extraction failed (pp. 4–6, 9, 13–14, 18–19)
were read visually. Page-1 title, authors and DOI match the metadata. No
identity problem. Numbering on this page is that of this version.

# Key claims

The blending factor of the convective flux is written $\alpha$ as the
registry's blending factor ($\alpha=1$ pure upwind WENO); the WENO
smoothness indicators, weights and ideal weights are $\mathrm{IS}_k$,
$\mathsf w_k$, $d_k$; the source's reference boundary-layer thickness
$\delta_0$ (and $\delta_{ref}$ of the ramp) is $\delta_r$; the cell size
$\Delta x_{min}$ is $h$; the Stanton number is $C_h$.

1. To the authors' knowledge, this is the first published work containing hypersonic turbulent flow simulations employing WMLES and an IBM (§1). **Stated**
2. Distinguishing features against other IBM-WMLES studies: third-order flux reconstruction at the boundary through a ghost-cell method that uses a single ghost cell, and a ghost-cell filling algorithm with a second interpolation point in addition to the usual one (§1). **Stated**
3. The convective flux is the convex blend $\hat{\mathbf f}_{conv}=(1-\alpha)\hat{\mathbf f}_{cent}+\alpha\hat{\mathbf f}_{diss}$ of a fourth-order KE/EP centred flux (Kuya et al.; Totani et al.) and an upwind-biased third-order WENO flux (Eq. 8), with $\alpha$ in the volume from a Ducros-type sensor (Eq. 9) whose $u_\infty/\delta_r$ term "shields the boundary layer"; at the faces $i-1/2$, $i+1/2$, $i+3/2$ next to the immersed boundary $\alpha$ is prescribed (§2.3). **Stated**
4. The second ghost layer is excluded from the upwind reconstruction because it "introduces large numerical errors as it is essentially extrapolated", so $\hat f^+_{m,i-1/2}$ must be biased downwind (§2.3). **Stated**; the two-ghost-cell case T2G "does not yield accurate results" (§3.2, Fig. 16). **Shown**
5. The boundary candidate stencils (Eqs. 21–22) with smooth-flow weights $\mathsf w_1^+=\mathsf w_2^+=1/2$, $\mathsf w_1^-=2/3$, $\mathsf w_2^-=1/3$ (Eq. 23) give third-order face values, but the flux derivative at the first irregular point is only second order because the truncation errors of the left and right faces do not cancel (§2.3, §2.7). **Derived** and **Shown** (Table 2)
6. Robustness improves when the ghost value is removed from the stencil of $\hat f^-_{m,j-1/2}$, although a linearly stable scheme can be obtained with it (§2.3). **Stated**
7. Irregular viscous stencils match the interior order and leading truncation-error coefficients: $k_1=-1/24$, $k_2=0$ for $\partial/\partial x$; $k_1=1/8$, $k_2=0$ for the mid-point average; $k_1=1/8$, $k_2=1/6$ for $\partial/\partial y$ (Eq. 29 and text, §2.4). **Derived**
8. The wall-adjacent viscous flux derivative uses an overdetermined four-point system (Eq. 31) solved with the pseudo-inverse, which removes the singularity as the wall distance tends to zero (§2.4). **Derived**
9. Manufactured solution on a unit sphere (Eq. 44): interpolation orders $L_2/L_\infty$ between 2.30 and 3.00 (P 2.658/2.300; U 2.998/2.771; V 2.994/2.831; W 2.997/2.712; T 2.659/2.298); ghost-cell filling $L_2$ 2.84–2.96, $L_\infty$ 1.86–1.99 (Table 1); "boundary conditions are applied with second-order accuracy at a minimum" (§2.7). **Shown**
10. Operators with boundary (Table 2): convective $L_2/L_\infty$ continuity 2.686/1.967, $x$-momentum 2.727/2.107, $y$-momentum 2.725/2.117, $z$-momentum 2.981/2.023, energy 2.650/2.044 (with $\alpha=1$ everywhere); viscous $x$-momentum 2.014/2.377, $y$-momentum 2.320/2.118, $z$-momentum 2.301/2.082, energy 2.101/2.049; the convective scheme is third order in the volume and second order at the boundary (§2.7). **Shown**
11. For the parameter $t$ of the boundary stencil $C^+(t)$ (Eq. 54) the spectral radius of $\mathbf D_1^+$ grows exponentially for $t<0.25$ and saturates near $t\approx0.5$; $t=1/2$ is chosen so the boundary eigenvalue is as large as possible while smaller than at least one other eigenvalue, giving $C^+=\{1/6,7/6,-1/3\}$ (Eq. 55, Fig. 8); for $C^-(t)$ (Eq. 56) the spectrum depends weakly on $t$, and $t=1/3$ is chosen (§2.8). **Shown** (numerical eigenvalues)
12. Pseudospectra ($N_x=130$, five random perturbations per $\lVert\mathbf M\rVert=\varepsilon_p\in\{10^{-3},\dots,10^{-10}\}$): the three operators for $a>0$ lie inside the unit disk; the three for $a<0$ breach it for some $\varepsilon_p$ but lie inside for approximately $\varepsilon_p<10^{-4}$; the operator is "linearly finite-time stable for a range of configurations" (§2.8, Figs. 9–10). **Shown**
13. Channel at $Re_\tau=5200$: $\alpha<0.0125$ generates significant noise; larger $\alpha$ and $\alpha_{irreg}$ accelerate the centreline flow and retard the near-wall flow; the best values are $\alpha=0.0125$, $\alpha_{irreg}=(0.05,0.025,0.0125)$; doubling $\alpha_{irreg}$ makes no significant difference, so the interior dissipation matters much more than the irregular-cell dissipation (§3.1, Fig. 12). **Shown**
14. Moving the wall-model exchange point $Q_2$ ($3$, $3.5$, $4\,h$) and the near point $Q_1$ ($0.5$–$1.5\,h$) has no significant effect on the mean velocity or the Reynolds stresses; $Q_1$ has a slightly larger effect on the near-wall Reynolds stresses (§3.1, Fig. 13). **Shown**
15. With grid refinement the log-region deviation of the mean velocity from DNS "has almost completely vanished"; the Reynolds stresses agree with a reference WMLES but poorly with DNS in the inner region, especially $R_{11}$ (§3.1, Fig. 14). **Shown**
16. Mach-6 transitional flat plate: the wall-model transition sensor is tuned to the reference transition location (not a prediction); the baseline TB agrees reasonably with Mettu & Subbareddy, heat transfer slightly above the DNS; results are not insensitive to near-wall dissipation (TH, with more dissipation, erodes the turbulent structures); laminar surface quantities are not accurately predicted by the wall model (§3.2, Fig. 16). **Shown**
17. Grid refinement on the flat plate changes the peak $C_f$ less than the dissipation configurations do, and delays transition because the inflow forcing was tuned on the coarse grid (§3.2, Fig. 17). **Shown**
18. Mach-6 SWBLI aligned with the grid: on the fine mesh the surface heat transfer agrees well with the DNS, marginally over-predicted near the downstream end of the separation bubble; the coarse mesh is less favourable (§3.3.1, Fig. 19). **Shown**
19. Inclined SWBLI (0°, 3°, 6°, 9°, 12°): the peak transitional heat transfer agrees among all angles within approximately 5%; the separation bubble grows slightly with inclination, attributed to the sudden appearance of irregular points in the streamwise direction, which varies the streamwise dissipation (§3.3.2, Figs. 21–24). **Shown** (attribution **Stated**)
20. Coarse–fine grid interfaces ($h$ to $2h$) partly reflect the acoustic radiation of the transition region back towards the boundary layer, visible in $R_{22}$ for cases C1–C4: negligible on the means, not on higher-order statistics (§3.3.2, Fig. 24). **Shown** (cause **Stated**)
21. Mach-7.2 8° ramp: the fine grid captures the surface pressure; the coarse grid over-predicts the pressure upstream of the corner and the instantaneous separation; the minimum $C_f$ is notably higher than in the DNS; the post-shock adjustment length is about $4\delta_r$ on the coarse mesh and much smaller on the fine one; a possible cause is the imbalance between tangential pressure gradient and convective terms that the equilibrium wall model does not capture (§3.4, Figs. 26–27). **Shown** (cause **Stated**)
22. The coarse ramp grid (11M cells) costs less than 5% of the reference DNS (96M cells for the ramp plus 138M upstream) "considering only the spatial requirement" (§3.4). **Stated**; *(compiler check, not in the sources)* $11/(96+138)=4.7\%$, consistent.
23. Surface heat transfer is very sensitive to the artificial dissipation added at the immersed boundary, and a less sensitive method needs further work (§4). **Stated**
24. Even with the original incompressible WALE model the results show no significant deviation from experiment and DNS (§2.2). **Stated**

# Printed slips

- **Eq. (17):** printed "$\omega_k^\pm=\frac{c_k}{(\varepsilon+\beta_k)^l}$, and $\beta_k=\frac{\alpha_k}{\alpha_1+\alpha_2}$", while the text states $\omega_1\approx c_1=1/3$, $\omega_2\approx c_2=2/3$ in smooth flow. *(compiler check, not in the sources)* As printed the normalization acts on the smoothness indicators $\alpha_k$ of Eq. (18), not on the weights: $\omega_1+\omega_2\ne1$ in general, and for $\alpha_1\approx\alpha_2$ the weights tend to $c_k/(\varepsilon+1/2)^2$, not to $c_k$.
- **Eq. (9):** printed $\alpha|_{volume}=\frac{(\nabla\cdot\mathbf u)^2+|\nabla\times\mathbf u|^2}{(\nabla\cdot\mathbf u)^2+(u_\infty/\delta_0)^2}$, described as following Ducros et al. and as shielding the boundary layer. *(compiler check, not in the sources)* As printed, where $\nabla\cdot\mathbf u=0$ the expression is $|\nabla\times\mathbf u|^2/(u_\infty/\delta_0)^2$, which exceeds 1 wherever the vorticity magnitude exceeds $u_\infty/\delta_0$, so the printed formula alone does not keep the blend of Eq. (8) in $[0,1]$. The results report constant interior factors ($\alpha=0.0125$ channel, $\alpha=0.02$ hypersonic cases); how these combine with Eq. (9) is not stated.
- **§2.8:** the text calls $\mathbf A$ "a 4th-order approximation of $\exp(\gamma\mathbf D)$", while Eq. (48) prints "$e^{-\gamma\mathbf D}\approx\mathbf A=\mathbf I-\gamma\mathbf D+\dots$".
- **Eq. (60), §3.2:** "$C_p=\gamma R/\gamma-1$" without parentheses; Eq. (5) prints $\frac{\gamma R}{\gamma-1}$.
- **Table 5, coarse channel grid:** $\Delta x=\delta/20$, $\Delta y=\delta/80$ printed with $\Delta x^+=270$, $\Delta y^+=68$. *(compiler check, not in the sources)* At $Re_\tau=5200$ these spacings give $260$ and $65$; the printed values correspond to $Re_\tau\approx5400$. The fine-grid row ($\delta/30\to173.3$, $\delta/128\to40.6$, $3\delta/100\to156$) is consistent with 5200.
- **§3.3 against Table 10:** the text says the aligned SWBLI "was run ... on two grids, one coarse (≈2.1M cells) and one fine (≈4.6M cells)"; Table 10 lists three, "2.1M (coarse)", "4.6M (medium)", "16M (fine)". Which grid is the "fine mesh" of Fig. 19 is not stated.
- **§3.3.2 against Table 11:** "The domain height was expanded to be 50% larger than the domain described in the previous case"; Table 11 gives $L_y=91\delta_0$ against $26\delta_0$ in §3.3. *(compiler check, not in the sources)* 50% larger would be $39\delta_0$.
- **§3.3.1:** "separation bubble thickness of approximately $50\delta_0$", with a domain height of $26\delta_0$ in §3.3.
- **Figure references:** §3.2 "Instantaneous skin friction and Stanton number results are shown in Fig. 16" (Fig. 16 shows spanwise averages; the snapshots are Fig. 15); §3.3.2 "as seen in Fig. 20(i)" (the schematic is Fig. 20(a), (i) labels the incoming shock); §3.4 "Fig. 25(ii)" for the visualization of Fig. 25(b).
- **Table 9 against Table 13:** $u_\infty=969.6$ against 969 m/s, $P_\infty=498.72$ against 498 Pa.
- **Symbols overloaded:** $\alpha$ is the blending factor (Eq. 8) and the smoothness indicators (Eqs. 18, 24); $\beta$ the bulk viscosity (Eq. 6) and the normalized smoothness (Eq. 17); $\gamma$ the ratio of specific heats and the Courant number (Eq. 48); $c_k$ the ideal weights and the stencil and extrapolation coefficients.
- **References:** [46] and [67] are the same work (McQuaid et al., AIAA SciTech 2021) printed twice; [62] printed with year 2015 and a DOI string reading 10.1016/j.jcp.2013.01.027; [14] title ends with a stray "cite"; [25] booktitle contains "(Llm)"; [41] "no. January 2020, 2021"; [58] pages "15–418"; [6] "Collela"; §2.5 cites "Larsson [58]" for a four-author paper; §2.4 "Penrose pseudo-inverse".

# Notation map

| van Noordt et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$; $u$, $v$, $w$ | same | $y$ wall-normal, agree |
| $u_i$, $\rho$, $p$, $T$ (no bars) | $\tilde u_i$, $\bar\rho$, $\bar p$, $\tilde T$ | the source calls its equations "Favre-averaged" and drops filter marks |
| $\mu$, $\mu_t$, $\nu_t=\mu_t/\rho$ | $\mu$, $\mu_t$, $\nu_t$ | $\mu_t$ is the SGS viscosity in the LES and the mixing-length viscosity in the wall model |
| $\tau_{i,j}$ | $\sigma_{ij}$ plus the modelled stress | total viscous-plus-SGS stress with $\mu+\mu_t$; **collision** with the SGS stress $\tau_{ij}$ |
| $\beta$ (Eq. 6) | $\mu_b$ | bulk viscosity, set to 0; **collision** with $\beta_k$ of Eq. 17 |
| $\bar S_{ij}$, $\mathcal S^d_{ij}$, $C_w$, $\Delta\approx3h$ | $\bar S_{ij}$, $\mathcal S_{ij}$ of the [WALE page](/methods/wale-model.md), $C_w$, $\Delta$ | $C_w=0.55$ |
| $\alpha$ (Eq. 8), $\alpha_{irreg}$ | $\alpha$ (blending factor), $\alpha_{irreg}$ (page-local: prescribed values in the first three irregular cells) | $\alpha=1$ pure upwind WENO, as the registry's $\alpha=1$ pure finite volume |
| $\alpha_k$ (Eqs. 18, 24) | $\mathrm{IS}_k$ | WENO smoothness indicators; **collision** with $\alpha$ |
| $\omega_k^\pm$, $c_k$ | $\mathsf w_k$, $d_k$ | WENO weights and ideal weights; $\omega$ is not the specific dissipation rate |
| $\hat{\mathbf f}^\pm$, $\sigma$ | (split fluxes, spectral radius of the flux Jacobian) | **collision:** the hat is not a test filter; $\sigma$ is not the viscous stress |
| $\Delta x_{min}$ | $h$ | minimum cell size |
| $\delta_0$, $\delta_{ref}$ | $\delta_r$ | reference boundary-layer thickness (inflow; ramp) |
| $Q_2$, $r_2$ | $h_{\mathrm{wm}}$ | wall-model exchange point, fixed in outer units |
| $Q_1$, $r_1$ | (near sampling point, in grid units) | page-local |
| $y^*=y\sqrt{\rho\tau_w}/\mu$ | $y^*$ (semi-local scaling) | agree |
| $\kappa=0.41$, $A^+=17$ | $\kappa$, $A^+$ | agree |
| $\tau_w$, $q_w$ | $\tau_w$, (wall heat flux) | agree |
| $St$ | $C_h$ | Stanton number; **collision** with the registry's Strouhal number |
| $Tr$, $Tr_0$ | (transition sensor of the wall model and threshold 5/3) | page-local; the hat filter in $Tr$ is not defined by the source |
| $\gamma$ (§2.8), $\mathbf A$, $\mathbf D$, $\Lambda_\varepsilon$, $\varepsilon$ | (Courant number, RK4 update matrix, discrete operator, $\varepsilon_p$-pseudospectrum, perturbation size $\varepsilon_p$) | **collision:** $\gamma$ is the ratio of specific heats elsewhere; $\varepsilon$ is not the dissipation rate |
| $C^\pm(t)$ | (one-parameter boundary stencils) | page-local |
| $N_x$ | $N_x$ | grid points of the stability analysis, agree |
| $\langle u'u'\rangle$, $\langle v'v'\rangle$ | $R_{11}$, $R_{22}$ | positive, agree |
| $Re_b=U_b\delta/\nu$ | $Re_b$ | $\delta$ channel half-height, agree |

# Reference list

69 printed references, numbered [1]–[69]. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. [46] and
[67] print the same work (McQuaid et al., AIAA SciTech 2021) and fold into
one entry. Ref. [21] (Zangeneh, AIAA SciTech 2021 Forum) is not the
ingested [zangeneh-2021](/sources/zangeneh-2021.md) (Phys. Fluids) and is keyed `zangeneh-2021-d`; ref. [50] is the ingested [kuya-2018](/sources/kuya-2018.md).
Same-author same-year works take suffixes in printed order (Brehm 2015,
three works; McQuaid 2021). Items [26], [41], [46], [60] and [63] are
partially printed (missing venue, year or book title).

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Method of manufactured solutions](/methods/method-of-manufactured-solutions.md)
- [Non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [WALE model](/methods/wale-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
