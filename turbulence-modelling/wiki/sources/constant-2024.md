---
type: Source
title: "Constant et al. (2024) — An improved immersed boundary method for turbulent flow simulations on Cartesian grids: extension of a global geometric approach for thin boundary layers and strong flow incidence"
description: "Extends a ghost-cell immersed boundary method with a wall function for steady Spalart–Allmaras RANS on octree Cartesian grids by a locally adapted modelling height and a higher-order wall-pressure reconstruction from a second image-point layer, cutting drag errors on NACA 0012, a multi-element airfoil and the NASA CRM high-lift model."
resource: "doi:10.1016/j.jcp.2024.113441"
source_kind: paper
authors: [Constant B., Péron S., Beaugendre H., Benoit C.]
year: 2024
venue: "J. Comput. Phys. 519:113441"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Computational_Physics_Constant_An_improved_immersed_boundary_method_for_turbulent_flow_simu.pdf"
tags: [immersed-boundary, wall-model, rans, moving-grids, high-lift]
timestamp: 2026-10-27T15:54:00Z
---

# Summary

Constant et al. (2024) extend their ghost-cell direct-forcing
[immersed boundary method](/methods/immersed-boundary-method.md) for steady
RANS at high Reynolds number on octree Cartesian grids (ONERA's Cassiopee and
the second-order finite-volume solver FastS), closed with the standard
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) and Musker's
algebraic [equilibrium wall function](/methods/equilibrium-wall-model.md).
Their earlier "F42" method places every forcing (target) point below a global
*modelling height*, estimated a priori from a flat-plate skin-friction
correlation and a user target $y^+$ of the first computed cells, which removes
the near-wall oscillations of immersed-boundary wall-function coupling. Two
shortcomings motivate the paper. At strong incidence the flat-plate estimate
leads to "strong over-predictions of the $y^+$ distribution": the suction-side
$y^+$ at the image points exceeds the target, by close to 300% at the leading
edge at $15^\circ$ on NACA 0012 (§4.1), so the [wall law](/definitions/law-of-the-wall.md) is applied where
the boundary layer is thin and not in equilibrium. And the wall pressure is
copied from the image point, a zero normal-pressure-gradient assumption that
misplaces the suction peak and corrupts the near-field pressure drag.

The contributions are a one-pass, a posteriori adaptation of the modelling
height (F42-A), which turns target points into computed points from the
converged $y^+$ without changing the mesh, unlike
[mesh adaptation](/methods/mesh-adaptation.md); and a second layer of image
points from which the wall pressure is reconstructed to first or second order
in post-processing. On the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at
$15^\circ$ the near-field drag error against a body-fitted wall-resolved
reference falls from 94% to 17%; on a two-dimensional multi-element airfoil
both corrections are needed at every mesh; on the
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md) half model
(2.4 billion cells) the drag error falls from 9.1% to 1.5% and the lift error
from 13% to 8.4%. A drag error of almost 20% remains at $15^\circ$, which
the authors compare with the deviations of Berger & Aftosmis and the
test-case sensitivity reported by Diskin et al. (as cited) and which could be
removed only by applying the wall model in the viscous sublayer at the
leading edge (§6.1, lines 747–757); on the multi-element airfoil they trace
the residual lift error of the coarsest mesh to the inability of their wall
model to represent a boundary layer without an established logarithmic
region (§6.2, lines 876–879). Strong adverse and favourable tangential gradients
occur where the solutions differ, and a
[pressure-gradient-aware wall law](/definitions/adverse-pressure-gradient-wall-law.md)
"would certainly improve the solution". The authors list the
[wall-modelled LES](/methods/wall-modelled-les.md) uses of immersed-boundary
wall functions and plan a [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
extension with a non-equilibrium wall model.

# Version read

HAL deposit hal-04731107v1 (10 October 2024, CC BY 4.0), the author
manuscript in preprint layout with line numbers, footer "Preprint submitted to
Journal of Computational Physics, October 3, 2024"; not the typeset version
of record. 69 PDF pages (a HAL cover page and 68 manuscript pages, references
on pp. 62–68), all read; Eqs. 5–11 were checked visually. Section, equation,
table and line numbers are those of the manuscript. Page 1 matches the
published identity.

# Key claims

1. The steady RANS–SA immersed boundary method F42 of Constant et al. (2021) is extended by an a posteriori local modelling height and by a higher-order post-processing reconstruction of the wall pressure; both act in pre- or post-processing only, not in the solver (Abstract, §1, §7). **Stated**
2. Most recent immersed-boundary literature for high-Reynolds-number flow assumes a constant wall-normal pressure across the whole turbulent boundary layer, which "can ultimately lead to significant errors" in direct force integration (§1, lines 44–47). **Stated**
3. The flat-plate estimate (Eq. 5, with the skin-friction correlation $0.058Re^{-0.2}$, printed $f(Re)$) is satisfactory at $0^\circ$, but at high incidence the suction-side image-point $y^+$ differs strongly from the target; the relative error between the target 300 and the leading-edge maximum is "close to 300% at AoA=15°" (NACA 0012, $M=0.15$, $Re_c=6\times10^6$) (§4.1, Fig. 10). **Shown**
4. The adaptation converts target points into computed points according to the $y^+$ one layer below in the wall-normal direction (a safety rule where $y^+$ varies strongly); the first two rows of target points are never changed; the procedure is static and converges in one pass, unlike the dynamic relocation of Xu & Liu (2021) (§4.2, Fig. 11). **Stated** (design) / **Shown** (one-pass convergence, Fig. 18)
5. The adaptation re-runs only the interpolation-data part of pre-processing, without mesh modification or recomputation of the wall distance, and restarts from the converged solution without mesh-to-mesh interpolation (§4.2). **Stated**
6. On NACA 0012 at $15^\circ$ (IBM6 mesh, target $y^+=100$) adaptation lowers the maximum suction-side image-point $y^+$ from 435 to 243; the leading-edge maximum still exceeds 100 because of the safety rule (§6.1, Fig. 18). **Shown**
7. Over the first 10% of chord at $15^\circ$ the equilibrium wall function cannot represent the velocity profile; beyond it the log region is established; non-adapted solutions carry the leading-edge error downstream, visible in eddy-viscosity profiles near the trailing edge (§6.1, Figs. 19–21). **Shown**
8. Pressure gradients at the first image points oscillate strongly, especially at the leading edge, and are unusable for a higher-order reconstruction; at the second image points they are smooth "without any spatial smoothing"; iso-distance and stair-step fronts for the second layer give no significant difference, and the stair-step front is kept (§6.1, Fig. 22). **Shown**
9. Strong adverse ($\partial_tp>0$) and favourable tangential pressure gradients occur on the suction side and near the leading edge, where the immersed-boundary and reference solutions disagree, so a pressure-gradient-aware wall model "would certainly improve the solution" (§6.1, Fig. 22b). **Stated** (from shown gradients)
10. A body-fitted wall-modelled study (NACA 0012, $10^\circ$) shows the errors on pressure drag, stagnation point and peak pressure growing with the target $y^+$ from 50 to 300; refining the immersed-boundary mesh at fixed target 100 changes the error little although the maximum distance over which zero normal pressure gradient is assumed is divided by four, so a better reconstruction during the simulation would have little impact, which supports a post-processing correction (§5.1, Figs. 12–13). **Shown**
11. The authors agree with Cai et al. (2021) that far-field integration gives a better pressure drag than near-field integration, but locate the error in the post-processing reconstruction of the wall pressure, not in the field solution (§5.1, lines 434–442). **Shown** (Figs. 23–25) / **Stated** (attribution)
12. On NACA 0012 at $15^\circ$ the linear reconstruction corrects the position and level of the suction peak and smooths $C_p$; first- and second-order results superimpose on the IBM6 mesh (§6.1, Figs. 23a, 24). **Shown**
13. Without pressure correction the near-field drag is overestimated, the error dominated by pressure drag while friction drag stays close to the reference; with first- or second-order reconstruction near- and far-field drag agree (§6.1, Fig. 25). **Shown**
14. Table 3 (NACA 0012, $15^\circ$): body-fitted $C_D=20.85\times10^{-3}$, $C_L=1.516$; F42 zeroth order $C_D=40.44\times10^{-3}$ (error 94%); F42-A zeroth order $30.57\times10^{-3}$ (47%); F42-A second order $24.51\times10^{-3}$ (17%), $C_L=1.476$ (2.6%) (§6.1). **Shown**
15. The remaining drag error of about 20% at $15^\circ$ matches deviations reported by Berger & Aftosmis with a cut-cell method and advanced wall models, explained after Diskin et al. as a sensitivity of the test case; removing it would require the wall model to act only in the viscous sublayer at the leading edge (§6.1, lines 747–757). **Stated**
16. Lift is insensitive to the integration method and the reconstruction order; only the adapted solution keeps the lift error below 3% at every incidence, the non-adapted one reaching "almost 10%" at $15^\circ$ (§6.1, Fig. 25). **Shown**
17. On the multi-element airfoil the first non-adapted run on IBM7 needs four times as many iterations as on IBM4, convergence being "quasi-proportional to the near-wall resolution"; a warm restart after adaptation costs about a third of the initial run, a cold start would double the process, and both reach the same $C_L$ (§6.2, Fig. 28). **Shown**
18. Non-adapted solutions on the multi-element airfoil overestimate the boundary-layer thickness of slat and main element; the slat-wake error falls from almost 80% (coarsest mesh) to a little over 20% (finest) before adaptation, and after adaptation even the coarsest mesh comes close to the finest non-adapted one (§6.2, Fig. 29). **Shown**
19. Table 6 (multi-element airfoil, F42-A, second order): drag error 42%, 27%, 23%, 22% on IBM4–IBM7 against the FUN3D body-fitted $C_D=6.22\times10^{-2}$, $C_L=3.779$; the lift error is "divided by two for each new Cartesian mesh" (§6.2). **Shown**
20. On coarse meshes (target $y^+=200$, 400) the quadratic reconstruction "can still halve the relative error" on drag; at 200 the second-order adapted solution practically matches the target-100 ones; on fine meshes the linear reconstruction suffices (§6.2, Fig. 30). **Shown**
21. Both the adaptation and the higher-order wall pressure are needed to bring the aerodynamic coefficients to an acceptable error, whatever the mesh resolution (§6.2, lines 852–856). **Shown**
22. CRM high-lift (HLPW-4, $17.05^\circ$): the IBM4 Cartesian mesh (minimum spacing 3.5 mm, target $y^+=500$) has 2.4 billion cells, four times the LAVA reference grid D (550M), but was pre-processed in under seven hours from the surface mesh alone, against weeks for a comparable curvilinear grid and months to calibrate one for WMLES (§6.3, Table 8). **Stated**
23. The CRM run used 20×28 Broadwell CPUs on ONERA's SATOR cluster, five runs of 15 000 iterations, with adaptation after the third (§6.3). **Stated**
24. Table 9 (CRM high-lift): F42 zeroth order $C_D=0.3767$, $C_L=2.2118$ (errors 9.1%, 13%); F42-A zeroth order 0.3783, 2.2940 (9.5%, 9.5%); F42-A second order 0.3405, 2.3205 (1.5%, 8.4%); LAVA body-fitted 0.3455, 2.5341; the higher-order reconstruction "divides the error made on the drag coefficient by six" (§6.3). **Shown**
25. FastS updates up to 10 million cells per second on one Broadwell core (as stated in earlier work), and its Cartesian solver is 2.5 times cheaper than the curvilinear one in memory and CPU (§2.2). **Stated**
26. With the blanking step of F42 there is "little to no difference" in CPU cost between the original and the improved method, as stated in Constant et al. (2021) (§3.1). **Stated**
27. For a far-field integration box of side greater than the chord the results do not depend strongly on its size; a side of two chords is imposed and the viscous stresses on it are neglected (§3.3.2). **Stated**
28. Future work: a hybrid RANS/LES transposition and a non-equilibrium wall model, since the equilibrium formulation limits the usable target $y^+$ range (§7). **Stated**

The wall-function reconstruction at a target point A from the image point B (Eqs. 6–11), with $f(y^+)$ Musker's law, $u_t$ and $u_n$ the tangential and normal velocities and $u_\tau$ constant along the normal:
$$u_{t,A}=u_\tau f(y_A^+),\qquad u_{n,A}=\frac{y_A}{y_B}u_{n,B},\qquad \tilde\nu_A^4-\nu_{t,A}\tilde\nu_A^3-\nu_{t,A}\nu^3c_{v1}^3=0,\quad \nu_{t,A}=\kappa u_\tau y_A\left[1-e^{-y_A^+/19}\right],\qquad p_A=p_B,$$
with $\kappa=0.41$ and the temperature from Crocco–Busemann on adiabatic walls; $\nu_t=\kappa u_\tau yD$ is called "valid in the log layer and down to the wall". The wall pressure (Eqs. 21–24), with $B_2$ the second image point at wall distance $h_{\mathrm{wm}}+2\sqrt{d_s}\,h$ ($d_s$ the space dimension) and $\ell_2=\lVert\overrightarrow{WB_2}\rVert$:
$$p_{w}^{(0)}=p_{B_1},\qquad p_w^{(1)}=p_{B_2}-\partial_np\big|_{B_2}\ell_2,\qquad p_w^{(2)}=p_w^{(1)}+\tfrac12\partial_{nn}p\big|_{B_2}\ell_2^2.$$
**Stated**
The adaptation criterion estimates the $y^+$ one layer below as $y^+_{n-1}\approx y^+_n(1-h/y_n)$ (Eq. 19), for a mesh aligned with the wall. **Stated**

# Printed slips

- **§3.1, line 200:** "$y_0$ is the height of the first cell on a flat plate for which $y^+=0$"; the right-hand side of Eq. 5, $\sqrt2L/(Re\sqrt{f(Re)})$, is the first-cell height for $y^+=1$ *(compiler check, not in the sources)*.
- **§3.2, lines 220–221:** "$u=\mathbf u\cdot t$ and $v=\mathbf u\cdot n$ as the normal and tangential components" (the words are swapped; Eqs. 6–7 use $u$ tangential, $v$ normal).
- **Table 3:** lift error printed 5.6% for F42 zeroth order ($C_L=1.416$ against the reference 1.516, both printed), while $(1.516-1.416)/1.516=6.6\%$ *(compiler check, not in the sources)*; the text says the non-adapted lift error reaches "almost 10%" at $15^\circ$ (line 762). The F42-A second-order drag error, $(24.51-20.85)/20.85=17.6\%$, is printed 17% *(compiler check, not in the sources)*.
- **Table 9:** drag error printed 9.1% for F42 zeroth order, while $(0.3767-0.3455)/0.3455=9.0\%$ *(compiler check, not in the sources)*.
- **§6.2, line 811:** "the modeling height adaptation described in Section 3" (it is Section 4).
- **Names:** "Person et al. [36]" (§5.2, line 482) for Péron; "The 2DMA profile" (line 773); "Thomson's simplified approach [29]" for Thompson; Eq. 8 writes $C_{v1}$ for Eq. 2's $c_{v1}$; Fig. 29 legends "(Y+-400 MUSKER)" with a stray minus; "simulation paramaters" (Tables 1, 4, 7); "NASA CRM-HL" in Tables 7–9 against "HL-CRM" in the text.
- **Table 5 against §6, line 552:** IBM7 halves the spacing of IBM6 but keeps the target $y^+=100$, whereas "each $y^+_{target}$ is given as a function of the near-wall resolution".
- **Reference list:** [10] and [41] printed as *AIAA Journal* with conference-paper DOIs; [20] prints "J.-M. L. Gouez" and "C. andreolli".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u_i$, $p$, $E$, $T$ | $\langle\rho\rangle$, $\langle u_i\rangle$, … | RANS means, no averaging symbol printed |
| $\tau_{ij}$ | $\sigma_{ij}$ | **collision:** viscous stress (Eq. 1) and the wall stress tensor $\tau_w(t_in_j+t_jn_i)$ (Eq. 16), not the SGS stress |
| $\tilde\nu$, $\chi$, $f_{v1}$, $c_{v1}=7.1$ | $\tilde\nu$, $\chi$, $f_{v1}$, $c_{v1}$ | Eq. 8 prints $C_{v1}$ |
| $\nu$, $\nu_t$ | $\nu$, $\nu_t$ | |
| $\kappa=0.41$, $u_\tau$, $y^+$ | $\kappa$, $u_\tau$, $y^+$ | |
| $D=1-\exp(-y^+_A/19)$ | van Driest damping with $A^+=19$ | to the first power, not squared as in the mixing length of the [equilibrium wall model](/methods/equilibrium-wall-model.md) |
| $M(y^+)$ | $f(y^+)$ | Musker's law (registry §11); its form is not printed |
| $H_{mod}$ | $h_{\mathrm{wm}}$ | modelling height: wall distance below which points are target (modelled) points |
| $y^+_{target}$ | (target $y^+$ of the first computed cells, page-local) | 50–500 (§3.1) |
| $y_0$, $f(Re)=0.058Re^{-0.2}$ | (flat-plate first-cell height, skin-friction correlation) | **collision:** $f$ is the wall-law profile $f(y^+)$ in the registry; the correlation is not given a symbol here |
| $u$, $v$ (§3.2) | $u_t$, $u_n$ (tangential and normal velocity, page-local) | **collision** with the velocity components $u$, $v$ |
| $n$, $t$ | (wall normal and tangent) | |
| A, B ($B_1$), $B_2$, W | (target, first image, second image, wall point) | W is also the primitive vector $(\rho,u_i,T,\tilde\nu)$ |
| $h$, $h_{min}$ | $h$ | minimum near-wall cell size |
| $\epsilon=2\sqrt{dim}\,h$ | (offset of the second image layer) | **collision** with $\varepsilon$; $dim$ written $d_s$ here |
| $p_{w,o0}$, $p_{w,o1}$, $p_{w,o2}$ | $p_w^{(0)}$, $p_w^{(1)}$, $p_w^{(2)}$ | |
| $\partial_np$, $\partial_{nn}p$, $\partial_tp$ | (normal first and second, tangential pressure derivatives) | $\partial_tp>0$ adverse |
| $C_p$, $C_f$, $C_D$, $C_L$ | $C_p$, $C_f$, $C_D$, $C_L$ | free-stream dynamic pressure |
| $\delta$ (§3.3.2) | (side of the far-field integration box, $2c$) | **collision** with the boundary-layer thickness |
| $c$, $L$ | (chord, reference length) | |
| $Re$ | $Re_c$ (chord; mean aerodynamic chord 7.005 m on the CRM) | |
| cellN | (cell nature: 0 blanked, 1 computed, 2 interpolated) | |

# Reference list

62 printed references, numbered style in order of citation. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Journal items print journal and year with a DOI but no volume or pages,
recorded as printed. Five undated web items (the Fast and Cassiopee pages of
ONERA, the NASA Turbulence Modeling Resource, FUN3D, the AIAA High-Lift
Prediction Workshop) take the citing year 2024 with a note. References [10]
and [41] print *AIAA Journal* with conference DOIs. The authors' earlier paper
[1] is keyed `constant-2021`, distinct from this source. No printed duplicates
and no unparseable item.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunk 7. This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
- [Wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
