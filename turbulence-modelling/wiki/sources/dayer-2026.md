---
type: Source
title: "D'Ayer et al. (2026) — Immersed boundary conditions using the spectral difference method applied to turbulent flows over rough surfaces"
description: "Volume-penalization immersed boundaries in the high-order spectral difference solver JAGUAR, with the stiff penalization term split off by Strang splitting and integrated analytically; validated on a laminar cylinder and on a DNS of a heated rough-wall minimal channel at Re_tau=400 against body-fitted and reference DNS."
resource: "doi:10.1016/j.compfluid.2026.106998"
source_kind: paper
authors: [D'ayer É., Colombié A., Chedevergne F.]
year: 2026
venue: "Comput. Fluids 309:106998"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Computers_amp_Fluids_Dayer_Immersed_boundary_conditions_using_the_spectral_difference_m.pdf"
tags: [immersed-boundary, high-order, dns, boundary-layer, compressible]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

D'Ayer et al. (2026) implement a continuous
[immersed boundary method](/methods/immersed-boundary-method.md), volume
(Brinkman) penalization, in JAGUAR, a compressible Navier–Stokes solver of
CERFACS and ONERA based on the
[spectral difference method](/methods/spectral-difference-method.md) on
hexahedral meshes. The aim is DNS databases of turbulent flow over rough,
heated walls in minimal channels, to support roughness closures for RANS such as
the corrections of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md).

The penalization source term relaxes velocity and energy in the solid towards
target values with a permeability $\eta_p$; it is stiff as
$\eta_p\to0$ and would restrict an explicit time step. The authors
split it from the convective and viscous fluxes with Strang splitting: an
analytical half step of the penalization (exponential relaxation), a full
spectral-difference step with a five-stage fourth-order SSP Runge–Kutta
scheme, and a second analytical half step. The time step is then set by the
CFL condition alone, and $\eta_p=10^{-10}$ s in all runs.

Validation has two levels. A steady laminar
[circular-cylinder](/benchmarks/circular-cylinder-wake.md) flow at $Re_D=40$,
$M=0.2$, $N=2$, matches a body-fitted run and the volume-penalization
[flux-reconstruction](/methods/flux-reconstruction.md) results of Kou et al.
(2022): recirculation length, separation angle and drag differ by less than
1%, while the wall vorticity oscillates in partially immersed cells. A heated
[turbulent channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=400$
over staggered hemispheres (the Wu et al. geometry RH400-20-4), cropped to a
minimal channel and run as a
[direct numerical simulation](/definitions/direct-numerical-simulation.md)
with $N=3$, agrees with body-fitted JAGUAR, a finite-volume AVBP run and the
reference DNS in mean velocity and temperature below the minimal-channel
critical height; Reynolds stresses and heat fluxes differ by at most about 5%.

# Version read

HAL preprint hal-05075852v1 ("Preprint submitted on 20 May 2025"), the
manuscript submitted to Computers and Fluids (Editorial Manager cover,
manuscript CAF-D-25-00529, footer dated 19 May 2025), not the version of
record; 15 PDF pages (HAL cover, Editorial Manager cover, 12 manuscript pages,
declaration of interest), all read; Eqs. 12, 14–23, 26–28 and Figs. 1, 4–6
checked visually. **Author list:** the manuscript prints four authors
(D'Ayer, Colombié, Dounia, Chedevergne; Dounia also appears in the CRediT
statement), Crossref lists three (no Dounia); the frontmatter follows
Crossref, and the file cannot tell which record is complete. The surname is
printed "D'Ayer" in the manuscript, "d'Ayer" on the HAL cover and "D'ayer" by
Crossref. The title matches Crossref. Venue and DOI are not printed in the
file. Locators are those of the manuscript.

# Key claims

1. Volume penalization is a continuous immersed boundary method that can only impose Dirichlet conditions on velocity and temperature; in practice $\boldsymbol u_\Omega=0$ and $e_\Omega=c_vT_\Omega$ in the solid (§2.3, Eqs. 12–13). **Stated**
2. Continuous immersed boundary methods are "usually restricted to first-order accuracy near the boundary", though simpler to implement than discrete ones (§1, citing Mittal & Iaccarino). **Stated**
3. The $L^2$ norm of the penalization modelling error is known a priori (Angot et al.) and printed as $|\boldsymbol U-\boldsymbol U_\eta|=O(\eta_p^{-1/2})$ (§2.3, Eq. 14; see Printed slips). **Stated**
4. The total error splits as $|\boldsymbol U-\boldsymbol U_\eta^{[n]}|\le|\boldsymbol U-\boldsymbol U_\eta|+|\boldsymbol U_\eta-\boldsymbol U_\eta^{[n]}|$; lowering $\eta_p$ lowers the modelling error but not necessarily the total error, since the discretization error can depend on $\eta_p$ (§2.3, Eq. 15, citing Engels et al.). **Stated**
5. With the source term added directly to an explicit scheme, very small $\eta_p$ causes instability; known limits are $\Delta t_{\max}=\eta_p$ (pseudo-spectral with AB2) and $\frac{6}{11}\eta_p$ (with AB3); when unknown, "a good starting point is to set $\Delta t=\eta$" (§2.4). **Stated**
6. Two-part Strang splitting with the penalization term solved analytically (Eq. 23) "makes possible the use of any value of $\eta$ without limiting the time step" (§2.4). **Derived**
7. The Strang splitting error is $O(\Delta t^3)$ in the $L^2$ norm (Eq. 21, Strang); here $\Delta t_{\max}$ is set by the CFL condition, not by this error (§2.4). **Stated**
8. $\eta_p=10^{-10}$ s in all computations (§2.4). **Stated**
9. The analytical treatment of the source term does not increase the computational cost (§4). **Stated** (no timings)
10. Legendre–Gauss interior flux points make the 1-D spectral difference scheme linearly stable for any degree $N$ (§2.2, citing Jameson). **Stated**
11. Spectral difference is as fast as flux reconstruction under favourable conditions or slightly slower in some circumstances (§1, cited). **Stated**
12. Cylinder ($Re_D=40$, $M=0.2$, $N=2$): $C_p(\theta)$ of the immersed-boundary run agrees with the body-fitted run and with Kou et al.; both immersed-boundary results show very small pressure oscillations near $90°$ and $180°$ (§3.1, Fig. 3). **Shown**
13. Cylinder: the wall vorticity of the immersed-boundary run differs slightly from the body-fitted one, with oscillations confined near the cylinder; the vorticity away from the wall agrees; the error is similar to that of the flux-reconstruction penalization of Kou et al. (§3.1, Figs. 4–5). **Shown**
14. Table 2: recirculation length $L_r/D$ = 2.27 (Kou et al.), 2.27 (Choi et al.), 2.27 (JAGUAR body-fitted), 2.25 (JAGUAR immersed); separation angle 52.0, 52.0, 52.2, 52.1; $C_D$ 1.52, 1.52, 1.55, 1.54; each differs by "less than 1%" between body-fitted and immersed runs (§3.1). **Shown**
15. The drag of the immersed run is the volume integral of the penalization term, $C_D=\frac{1}{\frac12\rho_\infty u_\infty^2D}\int_\Omega\frac{\rho}{\eta_p}(\boldsymbol u_\Omega-\boldsymbol u)\,dV$ (§3.1, Eq. 26). **Stated**
16. The vorticity oscillation comes from partially immersed cells: the discontinuous solution inside such a cell produces a Runge phenomenon (§3.1). **Stated** (mesh study not shown)
17. Immersed-boundary results are more sensitive to mesh resolution than body-fitted ones; a refinement study confirmed the body-fitted mesh (§3.1). **Stated** (not shown)
18. Refinement near the interface "may improve the accuracy" but is avoided to limit cost (§3.1). **Stated**
19. In the fully rough regime the drag increase is mainly pressure drag, so the immersed-boundary errors, concentrated in near-wall gradients, should leave the roughness drag effect well predicted (§3.1). **Stated**
20. Minimal-channel requirements (MacDonald et al.): $L_x^+\gtrsim\max(1000,3L_z^+,\lambda^+_{k,x})$, $L_z^+\gtrsim\max(100,k_r^+/0.4,\lambda^+_{k,z})$ (§3.2, Eq. 28); 8 streamwise and 3 spanwise roughness patterns give $L_x^+\approx1009$, $L_z^+\approx240$ (see Printed slips). **Stated**
21. The minimal channel preserves the roughness sublayer and the inner region; the mean flow is non-physical above the critical height $y_c^+=0.4L_z^+$ (§3.2, Fig. 7). **Stated**
22. Rough channel: no significant differences in $u^+(y^+)$ among JAGUAR body-fitted, JAGUAR immersed, AVBP and Wu et al. below $y_c^+$; above it all minimal-channel profiles overestimate the mean velocity (§3.2, Fig. 7). **Shown**
23. The mean temperature of AVBP and of both JAGUAR runs agree "excellent[ly]": the immersed boundary reproduces the isothermal wall (§3.2, Fig. 8). **Shown**
24. $R_{11}^+$ peaks near $y^+=25$, just above the roughness; the three computations differ from the reference by "no more than 5%" (§3.2, Fig. 9a). **Shown**
25. All three minimal-channel computations overestimate $R_{22}^+$ and underestimate $R_{33}^+$, attributed to the minimal channel (MacDonald et al.); $R_{12}^+$ agrees well (§3.2, Fig. 9b–d). **Shown**
26. Turbulent heat fluxes $\langle u'\theta'\rangle^+$, $\langle v'\theta'\rangle^+$ of AVBP and JAGUAR agree; the immersed run slightly overestimates the streamwise flux, by less than 5% (§3.2, Fig. 10). **Shown**
27. Grids (Table 3): Wu et al. body-fitted 859M DOF, $\Delta x^+=9.97$, $\Delta z^+=5.61$, first-point $\Delta y^+=0.15$; JAGUAR body-fitted 17M, 2.04, 1.11, 0.92; AVBP 14M, 1.03, 1.03, 0.21; JAGUAR immersed 25M, 1.73, 1.50, 0.51. Cylinder (Table 1): body-fitted 182k cells (1.63M solution points), immersed 263k (2.37M). **Shown**
28. Conclusion: spectral difference with volume penalization "was proved to be suitable to elaborate accurate DNS database of turbulent flows over rough surfaces"; future work is automatic $hp$-refinement near the interface (§4). **Stated**

# Printed slips

- Eq. 14 prints $|\mathbf U-\mathbf U_\eta|=O(\eta^{-1/2})$, a bound that diverges as $\eta\to0$, against the surrounding text, which says $\mathbf U_\eta\to\mathbf U$ and that lowering $\eta$ lowers the modelling error.
- §3.2: "$L_x^+\approx1009$"; with 8 patterns of length $\sqrt3\,d$, $d=4k_r$, $k_r=H/20$, $L_x=2.771H$ and $L_x^+\approx1109$ at $Re_\tau=400$ ($L_z^+=240$ checks) *(compiler check, not in the sources)*.
- §3.2: "We choose $N_x=8$, and $N_y=3$" for the spanwise count $N_z$.
- §3.2: "$\overline{v'v'}^+$, as shown in Figure 9d"; it is Fig. 9b.
- Fig. 10b caption "Spanwise turbulent heat flux" for the wall-normal flux $\overline{v'\theta'}^+$.
- Fig. 9b–d legends "JAGUAR (IBC)" for "JAGUAR (IBM)".
- §3.1: "the angle of separation $\theta$" while Table 2 uses $\alpha$ ($\theta$ is the surface angle).
- Eq. 2 prints the trace term as "$\frac23\nabla\mathbf u\cdot\mathbf I$" for $\frac23(\nabla\cdot\mathbf u)\mathbf I$.
- Eqs. 1c and 5: with $\mathbf q=-\lambda\nabla T$ printed, both give $\partial_t(\rho e)=\dots-\nabla\cdot(\lambda\nabla T)$, the anti-diffusive sign *(compiler check, not in the sources)*; the two equations agree with each other.
- Eq. 23 with $\mathbf A=\mathrm{diag}(0,\mathbf I_d,1)$ makes the density in the solid decay as $\delta\rho_0$, whereas the penalization sub-problem has no density source and keeps $\rho_0$ *(compiler check, not in the sources)*.
- Eq. 25, $\omega_z=\frac{1}{u_\infty D}(\partial_xv-\partial_yu)$, is not dimensionless; a reduced vorticity carries $D/u_\infty$ *(compiler check, not in the sources)*.
- Typography: "gaz turbine", "Discontinuous Galerking", "Raviar-Thomas", "preformed", "dy dividing", "Langrange", "François Chedeverne".

# Notation map

| D'Ayer et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$ | $N$ | polynomial degree; $N+1$ solution points, $N+2$ flux points per direction |
| $P$ | $p$ | pressure |
| $e$ | $E/\rho$ | total energy per unit mass |
| $\boldsymbol\tau$ | $\sigma_{ij}$ | viscous stress |
| $\lambda$ | (thermal conductivity) | |
| $\xi,\eta$ (§2.2) | $\xi$ (reference coordinates) | **collision:** $\eta$ is also the permeability |
| $\eta$ (§2.3) | $\eta_p$ (penalization permeability, s; registry §11, as on [immersed boundary methods](/methods/immersed-boundary-method.md)) | **collision:** $\eta$ is the Kolmogorov length in the registry |
| $\chi$, $\mathbf S$, $\mathbf u_\Omega$, $e_\Omega$, $T_\Omega$ | $\chi$, $\boldsymbol s_p$, $\boldsymbol u_\Omega$, $e_\Omega$, $T_\Omega$ (solid mask, penalization source, target velocity, energy, temperature; page-local, as on [immersed boundary methods](/methods/immersed-boundary-method.md)) | **collision:** $\mathbf S$ is not the strain-rate tensor |
| $\mathbf U_S$, $\delta(t)$, $\mathbf A$, $\mathbf B$ | (Strang-split solution), $r_p=e^{-t/\eta_p}$ (relaxation factor), $\mathsf A$, $\mathsf B$ (selector matrices), page-local as on [immersed boundary methods](/methods/immersed-boundary-method.md) | |
| $L/D$ | $L_r/D$ | recirculation length |
| $\alpha$, $\theta$ (§3.1) | (separation angle, surface angle) | **collision:** not the DG/FV blending factor, not a momentum thickness |
| $C_d$, $C_p$ | $C_D$, $C_p$ | **collision:** $C_p$ is also the specific heat (Eq. 27) |
| $H$, $k$, $d$ | $\delta$, $k_r$ (page-local roughness height), (hemisphere spacing) | **collision:** $k$ is the turbulent kinetic energy in the registry |
| $\overline{u'u'}^+$, $\overline{v'v'}^+$, $\overline{w'w'}^+$, $\overline{u'v'}^+$ | $R_{11}^+$, $R_{22}^+$, $R_{33}^+$, $R_{12}^+$ | **collision:** overbar is a time and $x$–$z$ average, not the LES filter |
| $\theta^+=T^+-T_\Omega^+$, $T_\tau$ | (temperature difference in wall units, friction temperature) | **collision:** $\theta$ is the momentum thickness in the registry |
| $u_\tau$, $Re_\tau$, $y^+$ | $u_\tau$, $Re_\tau$, $y^+$ | agree; the definition of $Re_\tau$ is not printed |
| $L_x^+$, $L_z^+$, $y_c^+$ | (minimal-channel lengths, critical height) | |
| $\Delta y_0^+$ | $\Delta y^+$ at the first point | |

# Reference list

68 printed references, numbered. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Refs [12] (Yang et
al., J. Fluid Mech. 941:A47) and [66] (Wu et al., J. Fluid Mech. 863) print no
year and no journal name: years come from their DOIs, and their natural keys
collide with other works already in the bibliography, so they take the
keys `yang-2022-c` and `wu-2018-f`. [36] (Wang, Witherden & Jameson, GPU $h$-adaptation for flux
reconstruction) is not the ingested source wang-2024 and takes the key `wang-2024-g`.
Kou et al. are cited as kou-2022 (J. Comput. Phys. 448), not the ingested
kou-2023. Ref [4] carries database residue ("Cited by: 419"); [59] prints an
ISBN and chapter DOI without a book title. No printed duplicates.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
