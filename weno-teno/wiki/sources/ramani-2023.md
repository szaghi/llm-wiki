---
type: Source
title: "Ramani & Shkoller (2023) — A fast dynamic smooth adaptive meshing scheme with applications to compressible flow"
description: "Smooth adaptive meshing (SAM): an r-adaptive mesh map with prescribed Jacobian built by a Poisson solve and a pseudo-time transport (a version of the deformation method), made O(N) per step by a perturbation formulation, and coupled to a GCL-augmented FD WENO ALE scheme with C-method artificial viscosity."
resource: "doi:10.1016/j.jcp.2023.112280"
source_kind: paper
authors: [Ramani R., Shkoller S.]
year: 2023
venue: "J. Comput. Phys. 490:112280"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Ramani_A_fast_dynamic_smooth_adaptive_meshing_scheme_with_applicati.pdf"
tags: [moving-mesh, finite-difference, artificial-viscosity, free-stream-preservation, weno]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper addresses r-adaptivity (mesh redistribution) for multi-D
compressible flow, and argues that the bottleneck of
[moving-mesh](/methods/adaptive-moving-mesh.md) hydrodynamics is the cost of
generating the mesh, not the discretization of the PDE. A mesh map $\mathsf X$
from a uniform reference mesh is built by prescribing its Jacobian
determinant, $\det\nabla\mathsf X=\mathsf G\circ\mathsf X$, with slip
boundary conditions. Instead of the optimal-transport (Monge–Kantorovich,
MK) solution, the authors use a new version of the Dacorogna–Moser
deformation method: one Neumann Poisson solve (FFT on a doubled domain) and
one transport solve in pseudo-time (fifth-order linear upwind differences
and RK4). This is static SAM (smooth adaptive meshing). When the target meets
a Neumann condition, the Jacobian error converges at fourth order. On the MK
benchmark of Delzanno et al., SAM is reported to run about 190 times faster
than MK, after a correction for the machine.

For moving meshes the paper introduces a perturbation formulation,
$\mathsf X_{k+1}=\mathsf X_k\circ\delta\mathsf X_{k+1}$, where the
near-identity map $\delta\mathsf X_{k+1}$ solves a problem of the same form on
the fixed reference domain (dynamic SAM). The physical CFL condition keeps
the pseudo-time step $O(1)$, so the work is $O(N_{\mathrm c})$ per step. A
restarted variant recomputes the map by static SAM when a grid-distortion
measure grows too much.

SAM is then coupled to a simplified finite-difference WENO ALE Euler solver:
[conservative finite differences](/definitions/conservative-finite-difference-scheme.md)
with fifth-order [WENO-JS](/methods/weno-js-reconstruction.md) reconstruction
of the variables, the C-method space–time smooth
[artificial viscosity](/methods/artificial-viscosity.md) of the authors'
earlier work, the geometric conservation law appended as an extra conserved
equation for [free-stream preservation](/properties/free-stream-preservation.md),
and a new ALE interface tracking. On the 2D
[Noh implosion](/benchmarks/noh-implosion-problem.md), a $50\times50$ SAM-ALE
run has a smaller $L^2$ density error than a $200\times200$ uniform run and
is about 6 times faster. On a
[Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md),
$64\times128$ SAM-ALE is comparable to $256\times512$ uniform and 10 times
faster. The authors contrast SAM with dyadic
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md), whose
resolution jumps they say corrupt both problems.

# Version read

The arXiv preprint arXiv:2205.09463v2 [physics.comp-ph], stamped 8 Jun 2023
and dated "June 12, 2023" on page 1, not the version of record; 50 pages.
The file prints no DOI; the published identity comes from Crossref. Title and
authors match the card. Section, equation, table and page numbers are those
of the arXiv v2.

# Key claims

Notation of the Notation map: $\mathsf X$ is the mesh map from the reference
domain $\Omega_{\mathrm{ref}}$ to the physical domain $\Omega$, $\mathsf G$ the
target Jacobian, $\mathsf F=1/\mathsf G$, $\tau_{\mathrm p}$ the pseudo-time,
$\mathsf Y(\cdot,\tau_{\mathrm p})$ the flowmap, $N_{\mathrm c}$ the number of
cells, $J$ and $Ja$ the Jacobian and cofactor matrix of $\mathsf X$.

1. Static SAM (Algorithm 1) solves the prescribed-Jacobian problem (7) by the Poisson problem $\Delta\Phi_{\mathrm S}=\mathsf F-1$, $\nabla\Phi_{\mathrm S}\cdot n=0$ (11), and the transport $\partial_{\tau_{\mathrm p}}\mathsf Y+\mathsf w\cdot\nabla\mathsf Y=0$ with $\mathsf w=\nabla\Phi_{\mathrm S}/\big(\tau_{\mathrm p}+(1-\tau_{\mathrm p})\mathsf F\big)$ (13)–(14); then $\mathsf X=\mathsf Y(\cdot,1)$. The proof shows that $\mathcal R=J_\xi\,[\tau_{\mathrm p}+(1-\tau_{\mathrm p})\mathsf F]\circ\xi$, with $\xi=\mathsf Y^{-1}$, is constant in $\tau_{\mathrm p}$ (§3.2.1). **Proved** (formal; existence on rectangles is **Stated** to follow from Dacorogna–Moser with polygonal-domain elliptic estimates, §3.2.2)
2. If the target satisfies $D\mathsf G\cdot n=0$ on $\partial\Omega$, the map, its Jacobian and its cofactors converge at least at fourth order. Otherwise the potential, its gradient and the map converge at second order, and the Jacobian and cofactors only at order 1.5, because the symmetric extension of $\mathsf G$ is only Lipschitz (§3.3.2). **Stated** (fourth order **Shown** in Table 1)
3. Table 1 (circular target (19), $\delta_{\mathrm G}=0.75$, $\sigma_{\mathrm G}=64$, $r_{\mathrm G}=0.2$): the $L^2$ Jacobian errors fall from $2.85\times10^{-2}$ ($32^2$) to $9.89\times10^{-8}$ ($1024^2$), with orders 2.5, 3.1, 4.0, 4.3, 4.2. **Shown**
4. "To the best of our knowledge, all other grid generation schemes are at best 2nd order accurate" (§3.4.2); other deformation methods "only yield second-order accurate solutions, at best" (§3.2.2). **Stated**
5. On the MK benchmark $\bar{\mathsf G}=2+\cos(8\pi r)$, SAM with the boundary-smoothed target has smaller errors than MK at every resolution from $16^2$ to $256^2$ ($3.25\times10^{-4}$ against $3.67\times10^{-4}$ at $256^2$); with the unsmoothed target its order drops to about 1.75 (Table 2). **Shown**
6. The $L^2$ mesh displacement $\lVert\mathsf X(x)-x\rVert_{L^2}\approx0.0178$ of SAM is comparable to the 0.0174 of MK, the $L^2$-optimal map (§3.4.3). **Shown**
7. Static SAM is "almost 200 times faster" than MK at $256^2$, 0.042 s against 8.636 s, with printed speed-up factors 47, 131, 160, 174 and 190 from $16^2$ to $256^2$ (Table 3). The MK times are taken from Delzanno et al. and divided by 2.2, a machine factor obtained by rerunning the Liao–Anderson method on both machines (Appendix C.1, Table 8). Serial Fortran 90 with gfortran on an Apple M1 Pro (§2.4). **Shown** (see Printed slips)
8. Static SAM costs $O(N_{\mathrm c}^{3/2})$ per mesh in 2D, because the stability condition (16) forces $\Delta\tau_{\mathrm p}=O(N_{\mathrm c}^{-1/2})$ when $\lVert1/\mathsf G-1\rVert_{L^\infty}\gg1$ (§4.1.2). **Derived**
9. Perturbation formulation: $\mathsf X_{k+1}=\mathsf X_k\circ\delta\mathsf X_{k+1}$ with $\det\nabla\delta\mathsf X_{k+1}=\mathsf P_{k+1}\circ\delta\mathsf X_{k+1}$ and $\mathsf P_{k+1}=(\mathsf G_{k+1}/\mathsf G_k)\circ\mathsf X_k$, a problem of the same form as (7), so the static solver on $\Omega_{\mathrm{ref}}$ is reused (§4.2.1, Eqs. (25)–(27)). **Derived**
10. Under an Eulerian CFL condition $\Delta t\sim N_{\mathrm c}^{-1/2}$, $1-1/\mathsf P_{k+1}=\Delta t\,\partial_t\mathsf G/\mathsf G+O(\Delta t^2)$, so $\lVert1-1/\mathsf P\rVert_{L^\infty}$ and $\lVert\mathsf w\rVert_{L^\infty}$ are $O(N_{\mathrm c}^{-1/2})$ and $\Delta\tau_{\mathrm p}=O(1)$ at all resolutions: dynamic SAM has "optimal complexity", $O(N_{\mathrm c})$ per time step (§4.2.2, Eq. (29)). **Derived**
11. The formulation differs from Semper–Liao and Grajewski et al., who compose in the other order on the deformed mesh and must rebuild mass and stiffness matrices every step; the scheme of Grajewski et al. has order 1.5 and an $O(N_{\mathrm c}^{1.5})$ interpolation search, against fourth order and $O(N_{\mathrm c})$ here (§4.2.2). **Stated** (the SAM side **Shown** in Table 4)
12. Propagating circular front (32): static and dynamic SAM both reach fourth order; dynamic SAM has smaller errors ($1.33\times10^{-7}$ against $2.65\times10^{-7}$ at $1024^2$). It is slower at low resolution because of the interpolation, breaks even at $256^2$, and is 2.86 times faster at $1024^2$ (582 s against 1663 s). Over the run, static SAM costs $O(N_{\mathrm c}^2)$ and dynamic SAM $O(N_{\mathrm c}^{3/2})$ (§5.2.3, Table 4). **Shown**
13. For the propagating front $\lVert1-1/\mathsf G\rVert_{L^\infty}\approx2.43$ while $\lVert1-1/\mathsf P\rVert_{L^\infty}\approx0.3$ (§5.2.2). **Shown**
14. Large zoom-in: static SAM folds the $64^2$ grid at $\delta_{\mathrm G}=0.97$, whereas dynamic SAM along the homotopy $\mathsf G(\cdot,s)=(1-s)+s\mathsf G_\delta$ with $\Delta s=0.05$ gives a smooth $64^2$ mesh at $\delta_{\mathrm G}=0.996$, a zoom-in factor of about 100 (§5.1, Fig. 4). **Shown**
15. Rotating patch ($N_{\mathrm c}=40^2$, $\Delta t=0.01$): the SAM fidelity errors are an order of magnitude below those of the parabolic MK scheme of Sulman et al., and static SAM takes 0.179 s against 75 s ("more than 400 times faster"). Dynamic SAM accumulates distortion (measure from 1.251 to 2.311); restarted SAM with threshold 1.01 keeps it at most 1.259 (Table 5). **Shown** (the competitor's numbers are taken from its paper)
16. At $N_{\mathrm c}=400^2$ on the rotating patch, the runs take 1414 s (static), 184 s (dynamic) and 194 s (restarted) (§5.3.2). **Shown**
17. Differential rotation ($128^2$, $0\le t\le90$): all three variants give untangled grids; restarted SAM resets twice, and static and restarted grids are of similar quality to the MK grids of Chacón et al. (§5.4, Figs. 7–8). **Shown**
18. 3D helical swirl, $32^3$ to $256^3$: fourth-order convergence for all variants. Over the run, static SAM costs $O(N_{\mathrm c}^{5/3})$ and dynamic and restarted SAM $O(N_{\mathrm c}^{4/3})$; restarted SAM is estimated to beat static SAM for $N_{\mathrm c}>735^3$ (§5.5.3, Fig. 12). **Shown** (the crossover is extrapolated)
19. The FD WENO ALE scheme preserves free streams to machine precision when the cofactors are computed with the fourth-order central difference (51), $J$ is evolved by the appended geometric conservation law $\partial_tJ-\partial_j(Ja^{(j)}_i\partial_t\mathsf X^i)=0$ (44), and the interface velocity uses the linear fourth-order average (49), which makes the scheme linear for constant data. On the moving mesh (52), $\lVert\rho(\cdot,T)-1\rVert_{L^\infty}=9.10\times10^{-14}$ at $T=80$ on $50\times50$ (§6.2.1). **Shown** (the linearity argument is **Derived**)
20. "Many standard schemes (including WENO [43]) fail to preserve the free-stream" on dynamic adaptive meshes (§6.1.3). **Stated**
21. Noh implosion ($\gamma=5/3$, $T=2$): $50\times50$ SAM-ALE has $L^2$ density error $4.897\times10^{-1}$ against $5.406\times10^{-1}$ for $200\times200$ uniform, at 45.6 s against 289 s and 7.8 MB against 43.7 MB (Table 6): "approximately 6 times faster" with "only 18% as much memory", very small wall heating and preserved symmetry (§7.1.3). **Shown**
22. Rayleigh–Taylor: $64\times128$ SAM-ALE ($\delta_{\mathrm G}=0.97$) is comparable to $256\times512$ uniform at 138 s against 1370 s, and 88 times faster than $512\times1024$ (12 100 s) (Table 7). Up to $t=1.75$ the vorticity norms follow the $512\times1024$ run (§7.2.4, Fig. 18). **Shown**
23. In the Rayleigh–Taylor run, generating the mesh costs about as much as the ALE solve. Since SAM is 100–200 times faster than MK, "an MK-ALE scheme cannot provide a speed-up over uniform mesh simulations" (§7.2.4). **Derived** (by cost extrapolation, not run)
24. Dynamic SAM gives non-convex elements on the $64\times128$ Rayleigh–Taylor mesh for $\delta_{\mathrm G}\gtrsim0.85$. The large zoom-in homotopy (25 sub-steps), applied at restarts only, gives a convex mesh at $\delta_{\mathrm G}=0.97$ with cells about 13 times smaller than uniform (§7.2.3, Fig. 16). **Shown**
25. The dyadic refinement of AMR causes spurious reflection, refraction and scattering at refinement jumps, which corrupt Noh and Rayleigh–Taylor solutions and persist or worsen under refinement (§1.1, §7.1, cited). **Stated**
26. Footnote 6: "FV schemes are 4 times more expensive than FD schemes in 2D, and 9 times more expensive in 3D" (cited). **Stated**
27. The simplified WENO flux, reconstructed variables times an averaged transport velocity, resembles [alternative-flux WENO](/methods/alternative-weno.md) but has no characteristic decomposition or Riemann solver; it is cheaper and less robust, oscillates on hard problems and needs the C-method viscosity (Remark 1). **Stated**

# Printed slips

- Table 3: the printed speed-up factors (47, 131, 160, 174, 190) do not follow from the printed times. The ratios MK/SAM of the printed rows are $0.045/0.0012=37.5$, $0.182/0.0017=107$, $0.591/0.004=148$, $2.227/0.013=171$ and $8.636/0.042=206$ *(compiler check, not in the sources)*. The caption says the MK row is already divided by 2.2, so the factors cannot be explained by that scaling either.
- Eq. (43) prints the ALE wave speeds $\lambda^{j,\pm}=\frac1{J}(v^j\pm c)$, $\lambda^{j,0}=\frac1Jv^j$, while $v^j=J^{-1}Ja^{(j)}_i(u^i-\partial_t\mathsf X^i)$ already carries $1/J$. In 1D ($Q=Jq$, $F=f(q)-\partial_t\mathsf X\,q$) the eigenvalues of $\partial F/\partial Q$ are $(v_1-\partial_t\mathsf X\pm c)/J=v\pm c/J$, not $(v\pm c)/J$ *(compiler check, not in the sources)*.
- Eq. (57), the Noh target $C_\psi=\exp[-400(r^2-t^2/9)]$, has no square or absolute value: inside the shock radius $r<t/3$ it grows instead of peaking at the shock, e.g. to $e^{177.8}$ at $r=0$, $t=2$ *(compiler check, not in the sources)*. The analogous targets (19) and (32) carry $\lvert\cdot\rvert^2$.
- Appendix B: $I^{(3)}$ carries only the cutoff $\varphi_1$. Then $D_2G^*=\varphi_2(y^2)D_2G(x^1_{\mathrm{mid}},y^2)+\int\varphi_1D_{12}G\,d\xi$, whose second term need not vanish on the boundaries $y^2=\mathrm{const}$ where $\varphi_2=0$, so the claimed $DG^*\cdot\nu=0$ needs $\varphi_1\varphi_2$ in $I^{(3)}$ *(compiler check, not in the sources)*.
- §3.4.3: "does not satisfy the Neumann condition $D\mathsf G\cdot\nu\neq0$" (double negative; the condition is $D\mathsf G\cdot\nu=0$).
- §5.2.3 says the resolution study runs "from $N=32^2$ to $N=512^2$", but Table 4 has a $1024\times1024$ column.
- Table 4 speed-up at $32^2$: printed 0.33, while $0.006/0.017=0.35$ *(compiler check, not in the sources)*.
- §5.2.1 calls the step (33), $\Delta t=0.64/(2\sqrt N)$, a CFL number of 0.64; with $\Delta x=1/\sqrt N$ and front speed 1 the ratio $\Delta t/\Delta x$ is 0.32, and 0.64 is the summed two-component form of (16) *(compiler check, not in the sources)*.
- §6.2.1: "initial data is uniform $U_0\equiv1$" uses a symbol not defined elsewhere.
- Typos: "psuedo-time" (§4.2.2), "contract tracking" (§7.1.3), "when when" (§5.1), "lying in ether" (§5.5.1), "implictly" (§4.2.1).

# Notation map

| Ramani & Shkoller 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$, $\phi=\psi^{-1}$ | $\mathsf X$, $\mathsf X^{-1}$ (local) | mesh map; **collision**: registry $\psi$ is the entropy-flux potential; letters as on the [moving-mesh page](/methods/adaptive-moving-mesh.md) |
| $\Omega_{\rm ref}$ ($x$), $\Omega$ ($y$) | kept | reference and physical domains |
| $N$ | $N_{\mathrm c}$ (local) | total number of cells; **collision** with the DG degree $N$ |
| $\mathsf G$, $\bar{\mathsf G}$, $\mathsf F$ | kept | target Jacobian, unnormalized target, reciprocal; **not the admissible set $G$** |
| $\Phi$, $\overline w$, $w$ | $\Phi_{\mathrm S}$, $\nabla\Phi_{\mathrm S}$, $\mathsf w$ (local) | Poisson potential, its gradient, transport velocity (14) |
| $\eta$, $\xi=\eta^{-1}$ | $\mathsf Y$, $\xi$ (local) | flowmap and back-to-labels map; **collision** with the entropy $\eta$ and the nodes $\xi_j$ |
| $\tau$ | $\tau_{\mathrm p}$ | pseudo-time; **collision** with the WENO-Z $\tau$; $\tau=(\tau^1,\tau^2)$ in Appendix A is the C-method contact tangent |
| $\delta\psi_{k+1}$, $P_{k+1}$ | $\delta\mathsf X_{k+1}$, $\mathsf P_{k+1}$ (local) | perturbation map and target |
| $\mathcal J$, $A$, $a=\mathcal JA$ | $J$, $A$ (kept), $Ja^{(j)}_i$ | Jacobian, inverse deformation tensor and cofactor (contravariant metric) terms; **$A$ is the flux Jacobian in the registry** |
| $\psi_t$ | $\partial_t\mathsf X$ | mesh velocity |
| $\lambda_k$, $\Lambda$ | $\lambda^{\mathrm d}_k$, $\Lambda$ | $L^1$ grid distortion and restart threshold; **$\lambda$ are eigenvalues in the registry** |
| $\delta$, $\sigma$, $r$ | $\delta_{\mathrm G}$, $\sigma_{\mathrm G}$, $r_{\mathrm G}$ | target parameters; **collisions** with the TENO flag, the affine scaling and the stencil size |
| $Q=(\rho,\rho u^1,\rho u^2,E)$; $u^i$ | $u$; $v_i$ | conserved variables; **the source's $u$ is the velocity** |
| $v^j$ | $v^j$ (local) | ALE transport velocity $J^{-1}Ja^{(j)}_i(u^i-\partial_t\mathsf X^i)$ |
| $c$, $\gamma$, $p$, $E$ | agree | |
| $x_{r,s}$, $r+\tfrac12$ | $x_{i,j}$, $i+\tfrac12$ | point values on the uniform reference grid |
| $q_{r+\frac12,s}$ | $u^{(\cdot)}_{i+1/2}$ | WENO5 value at the half point, upwinded on the transport velocity |
| $C$, $\beta$, $\beta_u$, $\beta_E$, $\mu$, $\kappa$, $S$, $\varepsilon$ | kept (C-method) | artificial-viscosity and C-equation parameters; **$\beta$, $\kappa$, $\mu$, $S$ collide with registry symbols** |
| $\mathsf z$, $z$ | kept | physical and ALE interface parametrizations |
| $\Upsilon$ | kept | zoom-in factor $1/\min J$ |

# Reference list

The paper prints 85 references, numbered [1]–[85] in alphabetical order. The
list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `ramani-2023`. [7] is a habilitation thesis; [76] prints
no venue; [66] prints an issue but no article number; [23] and [55] print
pages without a volume; [77] ends with "et al."; [10] prints a truncated last
author ("Y. L. and"), entered with a note. Ref. [26] is the ingested source
[Duan & Tang (2022)](/sources/duan-2022.md). Ref. [49] is the arXiv preprint
(arXiv:2202.07989) of [Li et al. (2022c)](/sources/li-2022-c.md); it is
kept as a separate preprint entry and needs a key distinct from the bundle's
`li-2022`. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–9 (2026-10-23). This source is cited on:

* [Adaptive moving mesh finite differences](/methods/adaptive-moving-mesh.md)
* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Conservative remapping for ALE schemes](/methods/conservative-remapping.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Noh implosion problem](/benchmarks/noh-implosion-problem.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
