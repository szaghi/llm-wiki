---
type: Source
title: "Sugaya & Imamura (2021) — Unsteady turbulent flow simulations on moving Cartesian grids using immersed boundary method and high-order scheme"
description: "Extends a hierarchical Cartesian-grid solver to grids moving rigidly with the body: immersed-boundary wall functions including the wall velocity, a Galilean-transformed flux and a fourth-order flux-quadrature correction for the grid motion, validated on a steady and a pitching NACA 0012 and on the Caradonna–Tung rotor with DDES."
resource: "doi:10.1016/j.compfluid.2021.105173"
source_kind: paper
authors: [Sugaya K., Imamura T.]
year: 2021
venue: "Comput. Fluids 231:105173"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Computers_amp_Fluids_Sugaya_Unsteady_turbulent_flow_simulations_on_moving_Cartesian_grid.pdf"
tags: [immersed-boundary, des, spalart-allmaras, wall-model, high-order, compressible]
timestamp: 2026-10-27T15:50:00Z
---

# Summary

Sugaya & Imamura (2021) extend the hierarchical Cartesian-grid solver
UTCart from stationary to moving grids for compressible, high-Reynolds-number
flow around moving bodies such as pitching airfoils and rotor blades. The
whole Cartesian grid moves rigidly with the body. The cell classification
and the [immersed-boundary](/methods/immersed-boundary-method.md) geometry
(image points) are therefore computed once and never change. No cell turns
from body to fluid, so the "fresh-cell" pressure oscillations of fixed-grid
immersed boundaries cannot occur, and the turbulent boundary layer stays in
the same cells. The introduction cites the
[geometric conservation law](/properties/geometric-conservation-law.md)
(Thomas & Lombard) only for deformable grids; the paper does not discuss it
for its rigidly moving grids.

Three ingredients are described. First, the grid-motion flux is folded into
the inviscid flux through a Galilean transformation: the SLAU Riemann solver
acts on grid-relative variables, and the result is transformed back.
Second, the immersed-boundary [wall function](/methods/rans-wall-function.md)
of Tamaki et al. (2017) sets the face-centre values from linear profiles
between the wall and an image point at $d_{\mathrm{IP}}=2h$. It uses the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) wall law and a
Newton–Raphson friction velocity, and the authors extend it with the wall
velocity. Third, the fourth-order (on uniform patches) quadrature-modification
finite-volume scheme of Tamaki & Imamura (2017) is extended to moving grids
with an extra correction for the linear variation of the grid velocity over
a face.

Steady SA RANS of the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at
$Re_c=6\times10^6$, $\alpha=10^\circ$ gives residual histories and profiles
that match to machine zero between a stationary grid in a free stream and a
moving grid in quiescent air, and that agree with a body-fitted code. The
AGARD Case 3 pitching NACA 0012 ($M_\infty=0.6$) reproduces the lift and
moment hysteresis of experiment and of a body-fitted solver. DDES-p, a
[delayed DES](/methods/detached-eddy-simulation.md) variant whose
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) shielding suits Cartesian
grids, is run on the [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md)
in hover with 75 and 149 million cells. The thrust and figure of merit are
nearly independent of grid and scheme, and the blade $C_p$ and tip-vortex
trajectories agree with experiment. The high-order scheme resolves finer
wake vortices than MUSCL: the scheme "greatly affects the prediction of the
wake structure" but barely the loads.

# Version read

Version of record (Elsevier, Comput. Fluids 231:105173; received 1 May
2021, online 6 October 2021); 13 pages, all read, pp. 2–6 and 9–12 checked
visually. Page 1 matches Crossref; no identity problem.

# Key claims

Page-local symbols: $Q_c$, $F$ the conservative variables and inviscid flux,
$\boldsymbol V$ the grid velocity, $V_n$ its normal component,
$\mathcal T_c$ the Galilean transformation, $\breve{(\cdot)}$ a face
average, $h$ the cell size (see the Notation map).

1. The authors present the method as "the first study that combines immersed boundary methods and wall functions on Cartesian grids with moving grid methods to simulate the unsteady turbulent flow around moving bodies" (§1). **Stated**
2. Because the grid moves with the body, the fresh-cell pressure oscillations do not occur and the position of the turbulent boundary layer relative to the near-wall cells is unchanged, so application to high-Reynolds-number flow is "straightforward" (§2.2, Conclusion). **Stated** (argued from the construction)
3. The moving-grid inviscid flux satisfies $F(Q_c,\boldsymbol n)-Q_cV_n=\mathcal T_c^{-1}F(\mathcal T_cQ_c,\boldsymbol n)$, $\mathcal T_cQ_c$ being the conservative variables relative to the moving boundary (Eqs. 4–6, after Nishikawa and Muffo et al.). **Derived**
4. The image point lies on the wall normal through the face centre at $d_{\mathrm{IP}}=2h$ from the wall; its values are linearly interpolated with the gradient of the cell containing it, and its location is computed once at the start (§2.2). **Stated**
5. The wall-velocity extension of the wall condition of Tamaki et al. — $V_{n,\mathrm{wall}}$ in the linear non-penetration profile, $V_{t,\mathrm{wall}}$ in the Newton–Raphson residual $g(u_\tau)=u_\tau f(y^+_{\mathrm{IP}})-(u_{t,\mathrm{IP}}-V_{t,\mathrm{wall}})$ — reduces to the original condition when $V_{t,\mathrm{wall}}=0$ (§2.2, Eqs. 11–15). **Derived**
6. Taking the face-centre pressure from the adjacent fluid cell instead of the image point gives "a small improvement … in the simple test cases" (§2.2, Table 1); the improvement is not shown. **Stated**
7. The scheme is fourth-order where the grid is uniform and second-order at faces where the cell size changes, because the least-squares first derivative is first-order there; hence "high-order scheme" rather than fourth-order. Only the inviscid flux is high-order, and no convergence study is given in this paper (§2.3). **Stated**
8. For a rigid grid velocity $\boldsymbol V=\boldsymbol V_{\mathrm{trans}}+\boldsymbol\Omega_{\mathrm{rot}}\times\boldsymbol r$, $V_n$ varies linearly over a face and $\breve{(Q_cV_n)}=\breve Q_cV_{n,\mathrm{FC}}+\frac{h^2}{12}\,\partial_YV_n\,\partial_YQ_c+O(h^4)$, $Y$ the face-tangential coordinate (Eq. 22). **Derived**
9. The moving-grid quadrature modification flux is that of the grid-relative flux evaluated at $\boldsymbol V=\boldsymbol V_{\mathrm{FC}}$ minus $\frac{h^2}{12}\partial_YV_n\,\partial_YQ_c$, which gives the face-averaged flux to $O(h^4)$ (Eqs. 24–26). **Derived**
10. Steady NACA 0012 (SA RANS, $Re_c=6.0\times10^6$, relative Mach 0.15, $\alpha=10^\circ$): density $L_2$ norms of $4.85717\times10^{-11}$ (stationary grid) and $4.85718\times10^{-11}$ (moving grid) at step 15,000, and $4.20906\times10^{-16}$ and $4.49798\times10^{-16}$ at 30,000, differences "in the order of machine zero" (§3.1, Table 3, Fig. 5). **Shown**
11. The two cases give identical $C_p$, $C_f$, relative-velocity and eddy-viscosity profiles at $x/c\sim0.3$, in agreement with the body-fitted code FaSTAR on the Turbulence Modeling Resource grid (§3.1, Figs. 6–8). **Shown**
12. $y^+_{\mathrm{IP}}\approx230$ at $x/c=0.5$ in the steady case; immersed boundaries with wall functions agree with body-fitted grids for surface pressure "when $y^+$ is approximately 500 or less" (§3.1, Fig. 4, citing four studies). **Stated** (cited)
13. AGARD Case 3 ($M_\infty=0.6$, $Re_c=4.8\times10^6$, $\alpha=4.86^\circ+2.44^\circ\sin\varpi_{\mathrm p}t$, reduced frequency 0.081, pivot at quarter chord): shock and suction-peak positions at $\alpha=5.92^\circ$ pitching up agree with FUN3D on a body-fitted grid and with experiment (§3.2, Figs. 10–11). **Shown**
14. The $C_L$–$\alpha$ hysteresis loop and the inversion of the lift trajectory near $\alpha\sim6^\circ$ are reproduced, consistent with experiment and FUN3D (§3.2, Fig. 12). **Shown**
15. The pitching-moment difference from experiment is "around 0.005, which is almost the same as with the simulation using the body-fitted grid" (§3.2, Fig. 13). **Shown**
16. Since immersed boundaries do not strictly conserve, the pitching results are compared with a body-fitted conservative simulation; the agreement is offered as evidence that non-conservation does not spoil the unsteady aerodynamics (§3.2). **Shown** (indirectly)
17. Caradonna–Tung rotor in hover, time-averaged thrust coefficient and figure of merit: MUSCL Grid 1 0.00514, 0.594; MUSCL Grid 2 0.00518, 0.611; high-order Grid 1 0.00519, 0.606; high-order Grid 2 0.00521, 0.618; grid size and scheme "have a small effect" (§4.5, Table 7). **Shown**
18. Time-averaged $C_p$ at $r/R=0.50$, 0.68, 0.80, 0.89, 0.96 agrees with experiment and is almost grid-independent (§4.5, Fig. 17). **Shown**
19. Tip-vortex trajectories agree with experiment "both qualitatively and quantitatively"; between 300° and 400° vortex age the radial position changes rapidly with MUSCL and stays almost constant with the high-order scheme (§4.5, Fig. 18). **Shown**
20. The high-order scheme resolves finer wake vortices than MUSCL, including secondary braid structures between two helical vortices reported earlier in simulations and experiments; "the numerical scheme greatly affects the prediction of the wake structure" (§4.5, Fig. 19). **Shown**
21. Cost: 896 cores (Grid 1) and 1792 cores (Grid 2); 11 h for the first 10 revolutions; 63 h (MUSCL) against 99 h (high-order) for the remaining ones on both grids (§4.5, Table 6). **Shown**
22. A one-order-of-magnitude drop of the inner residual per physical step is "widely used as a convergence criterion" and sufficient (§4.3, citing three studies). **Stated**

The DDES-p shielding function is not printed (it is referred to Tamaki,
Imamura & Kawai 2018 and Imamura & Tamaki 2020), nor are the SA wall law
$f(y^+)$ and the near-wall SA modification of Tamaki et al.

# Printed slips

- §1: "Posa et al. [14] proposed the coupling of the immersed boundary method with the overset grid method"; ref. [14] is De Vanna, Picano & Benini (2020), the Posa & Broglia paper is ref. [9].
- References [4] and [41] are the same work (Abras & Hariharan, J. Aircr. 55(1) 2018, 12–22).
- §4.3 is followed by §4.5 (no §4.4); cross-references read "section III-A", "section II/III/IV/V" while the headings are numbered 2, 3, 3.1, 4.
- Eq. (6): stray comma, "$\rho(w-V_z,)$"; Eq. (16): a stray "$v=$" opens the third line.
- Eq. (22): the prefactor is printed $1/\Delta x$ with integration limits $\pm\Delta X/2$, and the expansion of $Q_c$ omits the $1/2!$ of Eq. (16). The final line is unaffected: the $\eta^2$ term of $Q_c$ multiplies the constant $V_{n,\mathrm{FC}}$ and stays inside $\breve Q_cV_{n,\mathrm{FC}}$, and the cross term $\partial_YV_n\,\partial_YQ_c\,\eta^2$ averages to $\frac{h^2}{12}\partial_YV_n\,\partial_YQ_c$ *(compiler check, not in the sources)*.
- Ref. [35] is printed "AIAA J 2020;(11):4893–907 … Col. 11." without volume; refs. [20] and [29] print "(in Japansese)".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Q_c=[\rho,\rho u,\rho v,\rho w,E]^T$, $Q_p$, $F$, $F_v$ | same (page-local) | conservative and primitive variables, inviscid and viscous fluxes |
| $\tilde F$, $\tilde Q_c$ | $\breve F$, $\breve Q_c$ (face averages, page-local) | **collision:** the source's tilde is a face average, not a Favre filter |
| $\overline Q_{c,i}$ | (cell average, page-local) | **collision:** the source's overbar is a cell average, not the LES filter |
| $V=[V_x,V_y,V_z]^T$, $V_n$, $V_{trans}$ | $\boldsymbol V$, $V_n$, $\boldsymbol V_{\mathrm{trans}}$ (grid velocity, page-local) | |
| $\omega$ (rigid rotation), $\Omega$ (rotor) | $\boldsymbol\Omega_{\mathrm{rot}}$ | **collision** with $\omega$ and $\Omega_{ij}$ |
| $\omega$ (pitching) | $\varpi_{\mathrm p}$ (page-local, as on [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)) | **collision** with $\omega$ |
| $\mathcal T_c$, $\mathcal T_p$ | same (Galilean transformations, page-local) | |
| $\Delta X=\Delta Y$, $\Delta x$ | $h$ | cell size; not the filter width $\Delta$ |
| $X$, $Y$, $\eta$ | same (face-normal, face-tangential coordinates; tangential offset, page-local) | **collision** with the Kolmogorov length $\eta$ |
| $F_{mod}$, $F'_{mod}$ | same (quadrature modification fluxes, page-local) | |
| FC, IP, $d_{IP}$, $d_{FC}$ | same; $d_{\mathrm{IP}}$ (registry §11) | face centre, image point |
| $f_{wall}$ | $f(y^+)$ | SA wall law, registry §11 |
| $u_\tau$, $y^+$, $y^+_{IP}$ | $u_\tau$, $y^+$, $y^+_{\mathrm{IP}}$ | |
| $u_{n}$, $u_{t}$, $V_{n,wall}$, $V_{t,wall}$ | same (page-local) | normal and tangential fluid and wall velocities |
| $\alpha$, $\alpha_m$, $\alpha_0$, $k_r$ | same (angle of attack, mean, amplitude, reduced frequency, page-local) | **collision** with the DG blending factor $\alpha$ and with $k$ |
| $C_l$, $C_m$ | $C_L$, $C_m$ | |
| $C_T$, $C_Q$, FM, $M_{tip}$, $R$, $\theta_c$ | $C_{\mathrm{Th}}$, $C_Q$, FM, $M_{\mathrm{tip}}$, $R_{\mathrm r}$, $\theta_c$ (rotor thrust and torque coefficients, figure of merit, tip Mach number, radius, collective, page-local) | **collision:** the registry $C_T$ is the TENO cut-off threshold |
| $Re$ | $Re_c$ | rotor: chord and **sonic speed** ($4.44\times10^6$); airfoils: chord and relative velocity |

# Reference list

46 printed references, numbered style ([1]–[46]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Refs. [4] and [41] are one work printed twice (folded into one entry).
Ref. [20] (the authors' JAXA-SP-20-008 paper of 2021 on the 30P30N
high-lift airfoil) is a different work from this paper and is keyed `sugaya-2021-b`. Four web items ([2], [23], [28], [44]) are included; all
items parsed.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Dynamic stall](/definitions/dynamic-stall.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
