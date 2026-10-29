---
type: Source
title: "Alberti et al. (2025) — A systematic study on hybrid RANS/LES models for a high-order discontinuous Galerkin scheme"
description: "Systematically compares Spalart–Allmaras DDES and IDDES variants (subgrid length scales, low-Reynolds correction, shielding and elevating functions) in an incompressible high-order modal DG solver, with length scales normalized by the polynomial degree and equivalent-hexahedron grid lengths, on channels, a backward-facing step and a stalled NACA 0012."
resource: "doi:10.1016/j.compfluid.2025.106686"
source_kind: paper
authors: [Alberti L., Carnevali E., Crivellini A., Noventa G.]
year: 2025
venue: "Comput. Fluids 299:106686"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Computers_amp_Fluids_Alberti_A_systematic_study_on_hybrid_RANSLES_models_for_a_high-order.pdf"
tags: [des, hybrid-rans-les, dg, spalart-allmaras, log-layer-mismatch, high-order]
timestamp: 2026-10-29T07:42:00Z
---

# Summary

Alberti et al. (2025) test non-zonal
[detached-eddy simulation](/methods/detached-eddy-simulation.md) models, all
built on the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md),
inside an incompressible high-order modal
[discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
solver (Bassi–Rebay: artificial-compressibility Godunov flux, BR2 viscous
flux, orthonormal hierarchical basis of complete polynomials of degree
$N$, linearly implicit Rosenbrock ROS3Pw time stepping). DES-type models
were built for low-order finite volumes, and the authors find no earlier DG
work that compares several hybrid variants. They compare DDES and IDDES
with four subgrid length scales ($\Delta_{\max}$, the IDDES $\Delta_{dw}$,
Reddy et al.'s $\Delta_{\mathrm{llm}}$, Mockett et al.'s $\Delta_\omega$),
the low-Reynolds-number correction $\Psi$, the IDDES elevating function
$f_e$, modified IDDES grid variables, and three normalizations $s_\Delta$
of the length scales by the polynomial degree ($N+1$, $N$,
$N_{\mathrm{dof}}^{1/3}$). Grid lengths of arbitrary elements come from an
"equivalent hexahedron" with the element's principal moments of inertia,
rescaled to the element volume.

The cases are the [channel](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=400$ and 5200, the
[backward-facing step](/benchmarks/backward-facing-step.md) at
$Re_H=28\,000$ and the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at
$\alpha=45^\circ$, $Re_c=10^5$. $\Psi$ is detrimental in DG: without it the
LES branch settles by itself at an equivalent
[Smagorinsky](/methods/smagorinsky-model.md) constant of about 0.2 on
coarse grids and about 0.01 on fine ones, where the solver behaves as an
[implicit LES](/definitions/implicit-les.md) and the numerics outweigh the
model ([numerical dissipation](/properties/numerical-dissipation.md)); the
authors call the self-adjusting branch a "dynamic Smagorinsky model",
without a [test-filter procedure](/methods/dynamic-procedure.md).
$\Delta_{\max}$ gives too much eddy viscosity and delays Kelvin–Helmholtz
instabilities; $\Delta_{dw}$ drops the eddy viscosity too sharply in the
grey area and produces [log-layer mismatch](/definitions/log-layer-mismatch.md)
at $Re_\tau=5200$; $\Delta_{\mathrm{llm}}$ and $\Delta_\omega$ perform best.
On very fine grids $f_d$ shields weakly and the IDDES $f_B$ gives a safer
shield, while $f_e$ can corrupt the RANS branch. $s_\Delta=N+1$ is the best
normalization, and raising $N$ on a fixed mesh or at equal degrees of
freedom improves accuracy. The paper calls fine-grid high-order DG "more
like a wall-modeled ILES rather than a simple WMLES"
([wall-modelled LES](/methods/wall-modelled-les.md),
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)). Evidence is numerical.

# Version read

Version of record (Elsevier, open access CC BY-NC-ND; received 25 January
2025, accepted 13 May 2025, online 2 June 2025), 23 pages, all read,
pp. 2–5 checked visually for the equations. Page 1 matches the metadata; no
identity issue. Equation, figure, table and section numbers are those of
this version.

# Key claims

Page-local symbols (following the
[DES page](/methods/detached-eddy-simulation.md)): $d_{\mathrm{DES}}$ the
hybrid length replacing $d$ (the source's $\tilde d$); $C_{\mathrm{DES}}$;
$\Delta_{\max}$, $\Delta_{\mathrm{vol}}=V^{1/3}$, $\Delta_\omega$ (the source's
$\tilde\Delta_\omega$), $\Delta_{\mathrm{llm}}$, and the IDDES length
$\Delta_{dw}$ with constant $C_{dw}$ and wall-normal step $\Delta_{wn}$ (the
source's $\Delta_{hwn}$, $C_w$, $h_{wn}$); $\hat f_d$, $f_{dt}$, $f_B$, $f_e$ the
IDDES blending, shielding, grid and elevating functions (the source's
$\tilde f_d$ for $\hat f_d$); $\alpha_{\mathrm{ID}}=0.25-d/\Delta_{\max}$ the IDDES
grid variable; $\Psi$ the low-Reynolds-number correction; $s_\Delta$ the
length-scale normalization and $N_{\mathrm{dof}}$ the degrees of freedom per
element (both registry §11); $C_{S,\mathrm{eq}}=\sqrt{\nu_t/(\Delta_{\mathrm{vol}}^2|\Omega|)}$ the
equivalent Smagorinsky constant (the source's $\tilde C_S$, Eq. 25); $H$ the
step height.

1. In the authors' reading, the DG literature on DES-type models is thin and gives no breakdown of the modifications a high-order solver needs; no earlier DG work compares several hybrid variants against modelled-stress depletion, log-layer mismatch and the grey area (§1). **Stated**
2. In DG the SA source term uses only the positive part of $\tilde\nu$ ($\tilde\nu=0$ imposed otherwise), and $r$ is limited to $r_{\max}=10$ for stability, following Crivellini et al. [16] (§2.1, Eq. 6). **Stated**
3. $C_{\mathrm{DES}}=0.65$ is kept; it was calibrated in decaying isotropic turbulence with a high-order finite-difference scheme [17] and "recently found confirmation for a modal DG scheme applied to the Taylor–Green vortex flow [12]" (§2.1). **Stated**
4. All length scales are divided by $s_\Delta\in\{N+1,\,N,\,N_{\mathrm{dof}}^{1/3}\}$, the last suited to complete (non-tensor) bases; Table 1 gives $N/N_{\mathrm{dof}}^{1/3}$ and $(N+1)/N_{\mathrm{dof}}^{1/3}$ for $N=1$–6, with the common limit 1.82 as $N\to\infty$ (§2.3, Table 1). **Derived**
5. For unstructured elements $\Delta_x$, $\Delta_y$, $\Delta_z$ come from an equivalent hexahedron with the element's principal moments of inertia, rescaled to the element volume $V$ (Eq. 23); on Cartesian grids it reproduces the cell sides exactly; it was used here for distorted and curved hexahedra only, tetrahedra and prisms being left to future work (§2.3, Fig. 1). **Derived**
6. Channel $Re_\tau=400$, $N=6$: the hybrid models have a "sensible effect" on $u^+$ compared with an ILES at equal resolution; IDDES is the best class for $u^+$, "even surpassing an ILES carried out on a much finer grid", attributed to the fixed protection of $f_B$ overshadowing the solution-dependent $f_d$ (§3.1.1, Figs. 2–3). **Shown**
7. At $Re_\tau=400$ $f_d$ protects weakly because the fine grid gives very low eddy viscosity; sporadic unshielded wall patches cause slight modelled-stress depletion in DDES, with systematic underestimation of the mean Reynolds stresses, while IDDES ($f_B$) stays in RANS mode near the wall and systematically overestimates them; the first cell extends to $y^+=28.7$ (§3.1.1, Fig. 4). **Shown**
8. The low-Reynolds correction $\Psi$ forces $C_{S,\mathrm{eq}}=0.2$, in line with Lilly's 0.18; without it the models still reach a constant $C_{S,\mathrm{eq}}$ in LES mode but at much lower eddy viscosity, close to ILES, a plateau ascribed to $f_{v1}$ and $f_{v2}$; the authors recommend letting $\tilde\nu$ evolve freely in this high-order framework, without any a posteriori correction (§3.1.1, Fig. 5, Eq. 25). **Shown**
9. In DDES, $\Delta_{\max}$ gives too much eddy viscosity in the grey area, overestimating the total Reynolds stress and shifting $u^+$ upward; $\Delta_{\mathrm{llm}}$ "behaves much better" and closes the gap with DNS; $\Delta_\omega$ gives slightly more production than $\Delta_{\mathrm{llm}}$ and shifts $u^+$ up; in IDDES the length-scale differences disappear at $Re_\tau=400$ (§3.1.1, Figs. 2, 4, 6). **Shown**
10. Normalization at $Re_\tau=400$: the smaller $s_\Delta$, the more shielded the boundary layer, because $s_\Delta$ also enters $f_B$ through $\alpha_{\mathrm{ID}}$; $N$ against $N+1$ has almost no effect; $N_{\mathrm{dof}}^{1/3}$ is closer to DNS in the first part of the log layer; halving further ($0.5N_{\mathrm{dof}}^{1/3}$) is negative; "a rather delicate balance in the amount of eddy viscosity" (§3.1.1, Fig. 7). **Shown**
11. Modified IDDES grid variables $0.25-d/(\xi\Delta_{\max})$ and Han et al.'s $1.35-d/\Delta_{\max}$ (Eq. 26): enlarging the protection helps while the RANS/LES interface stays in the buffer layer or the first part of the log layer ($\xi=2$) and hurts once it is pushed well outside the inner layer; Han et al.'s form departs from standard IDDES already in the viscous sublayer, because $f_e$ becomes active inside a shielded zone and corrupts the RANS branch; combining $\xi=2$ with $s_\Delta=N_{\mathrm{dof}}^{1/3}$, each beneficial alone, worsens the solution (§3.1.1, Fig. 8). **Shown**
12. Channel $Re_\tau=5200$ on the $8\times12\times4$ mesh ($N=6$): all variants agree well with DNS except standard IDDES, which shows visible log-layer mismatch, caused by the very small $\Delta_{dw}$ in the RANS/LES transition, which weakens the solution-dependent shielding that $f_B$ does not compensate here; the resolution is formally comparable to the UMD wall-modelled-LES grids, but "almost five times coarser than their least refined mesh" in true degrees of freedom (§3.1.2, Fig. 9). **Shown**
13. At $Re_\tau=5200$ $\Psi$ is ineffective (practically 1 for $\tilde\nu/\nu>20$) and is left out; all variants settle by themselves at $C_{S,\mathrm{eq}}\approx0.2$ in the core, behaving like a standard Smagorinsky model, which the authors read as the LES branch acting as a dynamic Smagorinsky model whose equilibrium level adjusts case by case (§3.1.2, Fig. 10). **Shown**
14. At $Re_\tau=5200$ $f_d$ dominates the shielding over $f_B$, so DDES and IDDES nearly overlap for the same length scale; "the shielding function and the SLS are the two key aspects determining the final solution" (§3.1.2, Fig. 11). **Shown**
15. In the authors' reading, $\Delta_{dw}$ fails in DG because it was designed for finite-volume grid practice: DG meshes need higher wall-normal growth rates to compensate for the uniform spacing of the degrees of freedom inside each element, which produces a "staircase progression" of $\Delta_{dw}$ (§3.1.2, Fig. 12). **Stated** (backed by Fig. 12)
16. Both DDES and IDDES are resilient to leaving the RANS state: mean-flow perturbations of about 10% in the channels decay back to the steady RANS solution "almost instantly" (§3.1.2). **Shown** (no figure)
17. Raising $N$ on the fixed $Re_\tau=5200$ mesh lowers the eddy viscosity, moves the RANS/LES interface inward and squeezes the modelled stress toward the wall, giving a much better centreline $u^+$ (§3.1.3, Fig. 13). **Shown**
18. At roughly equal degrees of freedom for $Re_\tau=400$ (IDDES with $\Delta_{\mathrm{llm}}$: C $N=6$, M $N=4$, F $N=2$) the mean $u^+$ profiles are "spaced far apart": the numerics outweigh the model, the solver running in ILES fashion ($C_{S,\mathrm{eq}}\approx0.01$ in the bulk, not shown); M matches C $N=6$ only at $N=5$, and F approaches it only at $N=4$, "despite having more than three times as many DOFs" (§3.1.3, Table 4, Fig. 14). **Shown**
19. At $Re_\tau=5200$ (DDES with $\Delta_{\mathrm{llm}}$) equal-DOF configurations with $s_\Delta=N+1$ give close results and the highest $N$ is best; VF $N=2$ with twice the DOFs is slightly less accurate; $s_\Delta=N_{\mathrm{dof}}^{1/3}$ on C $N=6$ almost doubles the peak eddy viscosity of $s_\Delta=N+1$; F $N=2$ with $s_\Delta=N$ goes fully RANS, the shielded interface crossing the centreline (Table 5, $y^+=5200.0$) (§3.1.3, Fig. 14). **Shown**
20. $s_\Delta=N+1$ is the most suitable scaling, with the best performance across all polynomial degrees investigated (§3.1.3, §4). **Shown**
21. Backward-facing step ($N=3$): with a non-turbulent inflow the hybrid models stay RANS everywhere except downstream of the step on the lower wall; $\Delta_{\max}$ (standard DDES, and IDDES away from walls where $\Delta_{dw}\approx\Delta_{\max}$) delays or suppresses the Kelvin–Helmholtz instabilities, while $\Delta_{\mathrm{llm}}$ and $\Delta_\omega$ "unlock the complete development" of the rolls into 3D streaks (§3.2, Figs. 16–18). **Shown**
22. Step skin friction: all hybrid models except standard DDES and IDDES clearly improve on RANS, which misses the detachment right after the step, shows a corner bubble up to $x/H\approx0.9$, anticipates and magnifies the negative $C_f$ peak and underpredicts $C_f$ after reattachment; standard DDES massively delays reattachment although its negative peak "seems to match" the Adams experiment; the $\Delta_{\mathrm{llm}}$ variants predict the location of the maximum negative wall Reynolds stress and the reattachment section, with a slight overestimate of the negative $C_f$ peak; $N=4$ moves the results closer to experiment (§3.2, Figs. 19–20). **Shown**
23. Step velocity and $u_{\mathrm{rms}}$ profiles: the $\Delta_{\mathrm{llm}}$ and $\Delta_\omega$ variants nearly overlap and slightly overpredict $u$ near the wall in the recovery; at $N=4$ the discrepancies "almost entirely disappear"; the cross-plotted Reynolds stress is resolved only, because the SA modelled stress lacks the kinetic-energy contribution, absorbed into the pressure (§3.2, Figs. 21–22). **Shown**
24. NACA 0012 at $\alpha=45^\circ$, $Re_c=10^5$ ($N=3$): hybrid $C_p$ agrees with the DES of Shur et al. [17], while 2D RANS overestimates it, especially aft; Table 6 gives $C_L/C_D$ = 1.576/1.635 (2D SA), 1.144/1.169 (DDES, $\Delta_{\mathrm{llm}}$), 1.168/1.196 (the same at $N=4$), 1.209/1.235 (IDDES, $\Delta_{\mathrm{llm}}$), against 0.98/1.06 in the experiment [34] (digitized) (§3.3, Table 6, Fig. 24). **Shown**
25. On the NACA 0012 raising $N$ has an "imperceptible effect on average"; the small DDES–IDDES difference is attributed to the constant-thickness shield of $f_B$ and to $f_e$ being active inside the shielded region, which alters the wall distance, "which may be doubled in the extreme case", and corrupts the background RANS; the authors suggest recalibrating or eliminating $f_e$, which, they write, was likely conceived for the excessive eddy-viscosity decay seen only with $\Delta_{dw}$ (§3.3, Figs. 25–26). **Shown** / **Stated** (proposal)
26. SA-DDES and SA-IDDES work well in high-order DG with minor adjustments; on fine grids high-order DG behaves "more like a wall-modeled ILES rather than a simple WMLES", with an eddy-viscosity production that adapts to the resolution without ad hoc corrections; high order reaches accurate solutions "at a fraction of the DOFs employed at low order" (§4). **Shown** / **Stated** (the last not quantified against a low-order code)

The models in registry and DES-page notation (Eqs. 2–18): the SA
equation with $C_{b1}=0.1355$, $C_{b2}=0.622$, $C_{v1}=7.1$, $\kappa=0.41$,
$\sigma=2/3$, $C_{w2}=0.3$, $C_{w3}=2$, no trip terms, $\tilde S=|\Omega|+\tilde\nu f_{v2}/(\kappa^2d^2)$;
DES $d_{\mathrm{DES}}=\min(d,C_{\mathrm{DES}}\Delta)$; DDES
$d_{\mathrm{DES}}=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta)$,
$f_d=1-\tanh[(8r_d)^3]$, $r_d=(\nu_t+\nu)/(\sqrt{\partial_ju_i\partial_ju_i}\,\kappa^2d^2)$;
IDDES $d_{\mathrm{DES}}=\hat f_d(1+f_e)d+(1-\hat f_d)C_{\mathrm{DES}}\Delta$,
$\hat f_d=\max(1-f_{dt},f_B)$, $f_B=\min(2\exp(-9\alpha_{\mathrm{ID}}^2),1)$,
$\Delta_{dw}=\min(\max[C_{dw}d,C_{dw}\Delta_{\max},\Delta_{wn}],\Delta_{\max})$
($C_{dw}$ not printed); the correction $\Psi=\min\{10,[(1-\tfrac{C_{b1}}{C_{w1}\kappa^2f_w^*}f_{v2})/f_{v1}]^{1/2}\}$,
$f_w^*=0.424$, multiplies $C_{\mathrm{DES}}\Delta$;
$\Delta_{\mathrm{llm}}=f_d\Delta_{\mathrm{vol}}+(1-f_d)\Delta_{\max}$ (with
$f_d\to1-\hat f_d$ in IDDES). The shielded interface is plotted at
$f_d=0.1$ (DDES) and $\hat f_d=0.9$ (IDDES). Order of accuracy $N+1$ for
velocity and $\tilde\nu$, $N$ for pressure; $N_{\mathrm{dof}}=(N+1)(N+2)(N+3)/6$
in 3D.

# Printed slips

- **Table 3, $Re_\tau=5200$, mesh M:** $11\times17\times5$ is printed with 985 elements. *(Compiler check, not in the sources: $11\cdot17\cdot5=935$, and Table 5's 32 725 degrees of freedom for M, $N=4$, equal $935\times35$.)*
- **Eq. (24):** the stretching law is printed with the base $[(b+1)(b-1)]$. *(Compiler check, not in the sources: with the printed $a=0.5$, $b=1.05$ this maps $h=0$ to $y=0.927$ and $h=1$ to $y=0.073$, not the walls; the same formula with $(b+1)/(b-1)$ maps $h=0,0.5,1$ to $0,0.5,1$.)*
- **Table 1:** $(N+1)/N_{\mathrm{dof}}^{1/3}$ printed 1.40 at $N=2$ and 1.48 at $N=3$. *(Compiler check, not in the sources: $3/10^{1/3}=1.3925$ and $4/20^{1/3}=1.4736$.)*
- **Table 5, F grid:** spacings printed 681.2 ($s_\Delta=N+1$) and 1021.8 ($s_\Delta=N$). *(Compiler check, not in the sources: $2\pi\cdot5200/(16\cdot3)=680.7$ and $2\pi\cdot5200/(16\cdot2)=1021.0$, while the C-grid entries reproduce.)*
- **§2.1.2:** "cubic square of the cell volume" for $V^{1/3}$; **§3.1.3:** "$f_D$ function" for $f_d$.
- **Eq. (6):** the limiter cases are written on $r$ ("$r<0$ or $r\ge r_{max}$") instead of $r^*$.
- **Abstract:** "$Re_h=28\,000$", §3.2 "$Re_H$".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ | $N$ | polynomial degree; **collision** with the turbulent kinetic energy $k$ |
| $N_{dof}$ | $N_{\mathrm{dof}}$ (registry §11) | complete (Pascal) basis |
| $s_\Delta$ | $s_\Delta$ (registry §11) | default $N+1$ |
| $\mathbf w=[p,u_i,\tilde\nu]$, $p=P/\rho$ | $p$ kinematic, $u_i$, $\tilde\nu$ | |
| $d_w$, $\tilde d$ | $d$, $d_{\mathrm{DES}}$ | |
| $\Omega=\sqrt{2\Omega_{ij}\Omega_{ij}}$ | $\lvert\Omega\rvert$ | factor two included |
| $U_{ij}=\partial u_i/\partial x_j$ | $\partial_ju_i$ | in $r_d$, $r_{dt}$, $r_{dl}$ |
| $h_{max}$, $\Delta_{vol}$ | $\Delta_{\max}$, $\Delta_{\mathrm{vol}}$ | |
| $\Delta_{hwn}$, $C_w$, $h_{wn}$ | $\Delta_{dw}$, $C_{dw}$, $\Delta_{wn}$ | IDDES length, as on the DES page |
| $\tilde\Delta_\omega$, $\Delta_{llm}$ | $\Delta_\omega$, $\Delta_{\mathrm{llm}}$ | Mockett et al., Reddy et al. |
| $\tilde f_d$ | $\hat f_d$ | IDDES blending, as on the DES page; **opposite convention to $f_d$** ($\hat f_d=1$ RANS, $f_d=1$ LES) |
| $\alpha=0.25-d_w/h_{max}$, $\alpha_\xi$, $\alpha_{mod}$ | $\alpha_{\mathrm{ID}}$ (page-local) | **collision** with the DG blending factor $\alpha$ and the angle of attack |
| $\Psi$ | $\Psi$ (page-local) | not the Jameson sensor $\Psi_i$ |
| $\tilde C_S$ | $C_{S,\mathrm{eq}}$ (page-local) | equivalent Smagorinsky constant, Eq. 25; the tilde is not a Favre filter |
| $H$ (channel), $Re_\tau$ | $\delta$, $Re_\tau$ | channel half-width |
| $H$, $Re_H$ (step) | $H$ (page-local), $Re_H$ | step height |
| $\Delta^+_{/\!/,x}$, $\Delta^+_{/\!/,z}$, $\Delta^+_{y,w}$ | $\Delta x^+$, $\Delta z^+$, $y_1^+$ | scaled by $s_\Delta$ |
| $[\![\circ]\!]=\circ^+-\circ^-$ | $[\![\cdot]\!]$ | interface jump |
| $u_{rms}$ | $\langle u'^2\rangle^{1/2}$ (resolved) | modelled part excluded |
| LLM, MSD, gray area | log-layer mismatch, modelled-stress depletion, grey area | |

# Reference list

36 printed references, numbered style, DOIs printed as URLs for most. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. [28] (Flad & Gassner 2017) is the ingested
[flad-2017](/sources/flad-2017.md). The two UMD wall-modelled-LES web
resources [30], [32] are keyed under the corporate author in printed order;
[22] is a book, [33] (Adams 1984, Stanford) a thesis or report, [25] a
proceedings paper. The cited works under the keys `menter-2010`,
`krank-2019-b`, `bassi-2006`, `dewiart-2015`, `han-2020`, `lee-2020`,
`yang-2016` and `wang-2021` are different works from the bibliography
entries already holding those keys and are keyed `menter-2010-b`, `krank-2019-c`, `bassi-2006-b`, `cartondewiart-2015`, `han-2020-b`, `lee-2020-b`, `yang-2016-g` and `wang-2021-z`. No item
is unparseable.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
