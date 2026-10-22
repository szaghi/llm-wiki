---
type: Source
title: "Matsushita & Aoki (2021) — Gas-liquid two-phase flows simulation based on weakly compressible scheme with interface-adapted AMR method"
description: "Fully explicit weakly compressible solver for low-Mach gas–liquid flows on GPUs: an artificial-sound-speed pressure equation instead of the Poisson solve, a conservative phase field coupled with a level set, WENO3 blended with first-order upwind near the density jump, and interface-adapted tree-based block AMR scaling to 128 GPUs."
resource: "doi:10.1016/j.jcp.2021.110605"
source_kind: paper
authors: [Matsushita S., Aoki T.]
year: 2021
venue: "J. Comput. Phys. 445:110605"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Journal_of_Computational_Physics_Matsushita_Gas-liquid_two-phase_flows_simulation_based_on_weakly_compre.pdf"
tags: [multiphase, interface-capturing, weno, finite-difference, software]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper targets large, high-resolution simulations of low-Mach,
incompressible-like gas–liquid flows on GPUs without the pressure-Poisson solve
of semi-implicit solvers, whose iterative convergence degrades for density
ratios near $10^3$. Incompressibility is replaced by an isothermal **weakly
compressible** model: the non-conservative velocity equation plus the explicit
pressure equation $\partial_tp=-\rho c_{\mathrm a}^2\nabla\cdot v$, obtained from $p=\rho c_{\mathrm a}^2$
with the pressure advection dropped and no pressure diffusion. The sound speed
$c_{\mathrm a}$ is artificial, equal in both phases and set from a target Mach number
($M=0.03$ typically). Everything is explicit, with three-stage
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stepping and an acoustic time-step
bound.

Interfaces are carried by the conservative phase-field equation of Chiu & Lin,
solved by finite volumes (MUSCL3 with minmod) for exact mass conservation and
coupled to a [level set](/methods/level-set-method.md) $\Phi$ that supplies the
normal of the anti-diffusion flux and the curvature; $\Phi$ is rebuilt from
the phase field and reinitialized. Momentum is discretized on a staggered grid
in a density-weighted advection form, with the third-order Jiang–Peng
Hamilton–Jacobi version of [WENO](/methods/weno-js-reconstruction.md) blended
with first-order upwind through a minmod-limited slope ratio, a limiter-type
[hybrid](/methods/hybrid-weno.md) that the paper calls a
"[smoothness indicator](/definitions/smoothness-indicator.md)" although it is a
TVD slope ratio, not a $\beta_k$. A level-set quality test replaces bad
curvatures in thin films.

The second contribution is a GPU tree-based block AMR adapted to the interface:
$4^2$ or $4^3$ leaves mapped to CUDA blocks, 2:1 balance, Morton ordering, a GPU
memory pool with CPU-side defragmentation and Morton-curve domain decomposition.
Weak scaling reaches 81% efficiency on 128 V100 GPUs (95% for the fluid part).
Tests: the 2D rising bubble of Hysing et al., 3D bubbles against Grace's
diagram, dam breaks on dry and wet floors, liquid-jet breakup (11 h on one GPU),
soap-bubble growth, and appendices on volume error, manufactured-solution order,
convergence to incompressible flow (rate about 2 in $M$) and the single-vortex
test.

# Version read

Version of record (Elsevier typeset), 33 pages, all read; equations on pp. 4–9
and 29–30, garbled in the text layer, read visually. Page 1 matches Crossref
(title, both authors in this order, venue, DOI). Equation, table and figure
numbers cited here are those of this version.

# Key claims

Registry notation (see the notation map): velocity $v$, Mach number $M$, slope
ratio $r_{i-1/2}$ and TVD limiter $\psi$. Page-local symbols follow the
[level-set page](/methods/level-set-method.md): artificial sound speed
$c_{\mathrm a}$, level set $\Phi$ (the source's $\psi$), phase field (liquid
volume fraction) $\phi_{\mathrm l}$, interface-width parameter $\ell$, mobility
$M_{\mathrm{pf}}$ and curvature $\kappa_{\mathrm c}$.

1. Semi-implicit incompressible two-phase solvers become costly at scale because the pressure-Poisson iteration converges slowly, notably for density contrasts of about three orders of magnitude that make the matrix "extremely stiff" (§1). **Stated**
2. Under isothermal and low-Mach assumptions, mass conservation with $p=\rho c_{\mathrm a}^2$ gives $\partial_tp+(v\cdot\nabla)p=-\rho c_{\mathrm a}^2\nabla\cdot v$; the advection term is dropped "because the acoustic waves are much faster than the advection velocity", and no pressure-diffusion term is added, giving Eqs. (7)–(8) (§2.1). **Derived**
3. The sound speed is equal in both phases because "we do not solve the real compressibility" (§2.1). **Stated**
4. The phase-field normal $\nabla\phi_{\mathrm l}/\lvert\nabla\phi_{\mathrm l}\rvert$ is replaced by the level-set normal $\nabla\Phi/\lvert\nabla\Phi\rvert$, to improve geometric accuracy and reduce the "compression effect" of the weakly compressible velocity on $\phi_{\mathrm l}$; the right-hand side acts only where $\lvert\Phi\rvert<5\delta$ (§2.2, Eqs. 12–13). **Stated**
5. The phase field is solved in flux form and the density computed from it, so total mass is conserved to about $10^{-16}$ in double precision on uniform and AMR grids (2D rising bubble, case A) (§5.1, Fig. 21). **Shown**
6. The volume of each phase is not conserved by weakly compressible schemes; for the 2D rising bubble case B the gas-area error "remain[s] within 1.5%" and decreases with refinement (App. 8.1, Fig. 37). **Shown** (see Printed slips)
7. The blend $f_x=f_x^{\mathrm{1st}}+\psi(r_{i-1/2})\big(f_x^{\mathrm{WENO}}-f_x^{\mathrm{1st}}\big)$ with the minmod limiter prevents instabilities from the steep density change at the interface (§3.1, Eqs. 26–27). **Stated**
8. The time step is $\Delta t=\min\big(\nu\Delta x/(\max\sum_l\lvert v_l\rvert+c_{\mathrm a}),\ k_{\mathrm{visc}}\Delta x^2/(2N_d\max(\mu_l/\rho_l,\mu_g/\rho_g)),\ k_{\mathrm{sf}}\sqrt{(\rho_l+\rho_g)\Delta x^3/(4\pi\sigma)},\ k_{\mathrm{pf}}\Delta x^2/(2N_dM_{\mathrm{pf}}\ell)\big)$ with $\nu=0.4$, $k_{\mathrm{visc}}=k_{\mathrm{pf}}=0.6$, $k_{\mathrm{sf}}=0.2$, $N_d$ the space dimension (§3.3, Eq. 38). **Stated**
9. The level-set quality $Q=\lvert1-\lvert\nabla\Phi\rvert\rvert$ with threshold $0.05$ detects the "valley" singularity of $\Phi$ in thin films; there the curvature is replaced by that of the face neighbour with the smallest $Q$ (§3.4, Eqs. 39–41, Fig. 3). **Stated** (illustrated)
10. The mesh is adapted every $n_{\mathrm{AMR}}$ steps, chosen so that the interface moves $2\Delta x_{\min}$ for $4^3$ leaves; a leaf is refined when $\min\lvert\Phi\rvert<\sqrt3\,\Delta x_{n+1}b$, $b$ cells per leaf direction (§3.5, Eq. 42; §4, Eq. 47). **Stated**
11. Tree management on the CPU takes 70% of the AMR time, but AMR is not dominant (remeshing every hundred or so steps): about 90% of the run time is GPU computation (§4.2, Figs. 13–14). **Shown**
12. Weak scaling (wet-floor dam break, 458,765 leaves or 29,360,960 cells per GPU, remeshing every 128 steps, 4 V100 per node): 81% efficiency overall and 95% for the fluid computation at 128 GPUs; the tree structure is not yet parallelized (§4.3, Figs. 16–17). **Shown**
13. 2D rising bubble ($M=0.03$, $c_{\mathrm a}\approx16.67$): case A agrees with the TP2D, FreeLIFE and MooNMD reference codes at $t=3$; case B differs slightly at the skirt, attributed to the diffuse interface rather than to weak compressibility (§5.1, Fig. 18). **Shown**
14. Without a consistent initial pressure, gravity-imbalanced pressure launches strong, weakly damped acoustic waves that perturb the rise velocity; solving $\nabla\cdot(\rho^{-1}\nabla p)=\nabla\cdot v/\Delta t$ by red-black SOR (tolerance $10^{-7}$) for the first few steps removes them (§5.1, Eq. 50, Fig. 19). **Shown**
15. The density compression ratio is $\Delta\rho/\rho\simeq-\nabla\cdot v\,\Delta t\sim10^{-5}$ (§5.1, Eq. 51, Fig. 20). **Shown**
16. Linear (gradient-based) interpolation at refinement reproduces the uniform-mesh bubble position better than direct copying (§5.1, Fig. 22). **Shown**
17. 2D soap bubble: 9-level AMR, finest cell 0.0195 mm (equivalent to $8192\times8192$ uniform), about 0.9 million cells, $\mathrm{Re}=1181$; the radius grows 7.5 times by $t=5$ s and the pressure jump is about 0.66 against the Laplace estimate 0.667 (Abstract, §5.2, Fig. 28). **Shown**
18. 3D rising bubbles in four Grace regimes (density and viscosity ratios 100): Reynolds numbers 1.5/1.5, 4.6/4.6, 19.2/18.9, 1.76/1.70 (uniform/AMR) against Grace 1.7, 4.6, 20, 1.5 and van Sint Annaland 1.6, 4.3, 18, 1.7, with the relative error stated as "less than 7%" (§6.1, Table 3). **Shown** (see Printed slips)
19. Dam break on a dry floor: the water height matches Martin & Moyce and Hu & Sueyoshi; the surge front is slightly fast, as in other codes, attributed to the unmodelled gate (§6.2, Figs. 32–33). **Shown**
20. Dam break on a wet floor: uniform $768\times128\times384$ and AMR runs give similar interfaces, agreeing with an incompressible solver and "sharper than that of filtered CLBM" (§6.2, Fig. 34). **Shown**
21. Liquid-jet breakup (7-level AMR, $\Delta x=D/256$): the mushroom tip is reproduced; the run stops at $t^*=13.6$ when GPU memory runs out; 11 h on one V100 against an estimated 501,840 core-hours for the incompressible reference (explicitly not a fair comparison) (§6.3, Fig. 36). **Shown**
22. Manufactured solution (density ratio $10^3$, viscosity ratio $10^2$): the velocity $L_1$ error converges at third order for $\Delta x>1/128$ and $M=0.03,0.01,0.003$, and flattens on finer grids as "the compressibility effect becomes larger"; the error barely depends on the CFL number at $\Delta x=1/128$ (App. 8.2, Figs. 38–39). **Shown**
23. The weakly compressible solution converges to an incompressible one at rate about 2 in $M$ for $M\ge0.01$, saturating at $M=0.003$ (2D rising bubble case A, $128\times256$) (App. 8.3, Fig. 40). **Shown**
24. Single-vortex test ($T=8$): $L_1$ errors $9.09\times10^{-2}$ to $4.01\times10^{-4}$ from $32^2$ to $512^2$, rates 2.06, 1.40, 2.29, 2.04 (App. 8.4, Table 4). **Shown**

# Printed slips

- §2.1, after Eq. (3): "mass conservation (2) and momentum conservation (1)"; the numbers are swapped.
- §2.2, p. 4: "We compute the mobility as $\bar\lambda=M_\phi\lvert u_l\rvert_{max}$"; the mobility is $\bar\gamma$ in Eqs. (9), (12) and (38). Also "the center pf the profile".
- Eq. (27): the $u_{i-1/2}\le0$ branch is the reciprocal of the $u_{i-1/2}>0$ branch on the same left-biased points (checked visually, p. 6); an upwind ratio for $u\le0$ would use $f_{i+3/2}-f_{i+1/2}$ *(compiler check, not in the sources)*.
- Eq. (28) omits the $-\tfrac23\delta_{ij}\nabla\cdot v$ term of Eq. (3) without comment.
- Eq. (39): the curvature is written with continuous derivatives over a denominator $4\Delta x^2$; as printed it is dimensionally inconsistent unless the derivatives are undivided differences *(compiler check, not in the sources)*.
- §5.1: "four cases, Case A and Case B with a uniform 128 × 256 cells and a uniform 256 × 512 cells" (two cases on two grids).
- §5.2: with the printed data ($\rho_l=1045.9$, $\bar U=0.125$, $2R=0.016$, $\sigma=0.02$) the printed definition $We=\rho_l\bar U^22R/\sigma$ gives about 13.1, not the printed $We=0.26$, which is the value before division by $\sigma$; "expanding in the x-direction and the x-direction alternatively". *(compiler check, not in the sources: $1045.9\times0.125^2\times0.016=0.2615$, divided by $0.02$.)*
- §6.1: the stated "less than 7%" error holds only against van Sint Annaland's computations; against Grace, case A is 1.5 vs 1.7 and case D 1.76 vs 1.5 (about −12% and +17%). *(compiler check, not in the sources: relative differences from Table 3.)*
- §6.2, Eq. (64): $U=\sqrt{gL_z}\simeq1.83$ m/s, but Fig. 31(b) gives $L_z=0.36$ m and $\sqrt{9.8\times0.36}\approx1.88$ m/s. *(compiler check, not in the sources.)*
- App. 8.1: the text says case-B volume errors "remain within 1.5%", while the axis of Fig. 37 spans −0.0002 to 0.0016 (at most 0.16%).
- Eq. (75): $u=-\partial\Psi/\partial x$, $v=\partial\Psi/\partial y$ is not divergence-free; the single-vortex field needs $u=-\partial\Psi/\partial y$, $v=\partial\Psi/\partial x$ *(compiler check, not in the sources: $\partial_xu+\partial_yv=-\Psi_{xx}+\Psi_{yy}\neq0$ as printed)*.
- §6.3 "Shinjo and Umehara [59]" (Umemura); "with an ARM grid" (§5.1); Figs. 38–39 captions "Velocity L1 errors of as a function of".
- References: [25] Berger & Oliger (1984) is printed with the DOI 10.1016/0021-9991(92)90307-K; [46] and [51] have garbled author lists; [52] (Bazilevs et al., wind-turbine FSI) is cited for bubble shapes from incompressible solvers and its DOI is truncated.

# Notation map

| Matsushita & Aoki (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $p$ | $\rho$, $p$ | agrees; $p$ is evolved, not $\rho$ |
| $u$ (vector), $u_l$ (component) | $v$, $v_l$ | velocity |
| $c_s$ | $c_{\mathrm a}$ (local) | artificial sound speed, $p=\rho c_{\mathrm a}^2$, equal in both phases; not the physical $c$ |
| $Ma=U/c_s$ | $M$ | Mach number |
| $\tau$, $\mu$ | kept | viscous stress and viscosity; **$\tau$ is also the reinitialization pseudo-time and a normalized time** |
| $\phi$ | $\phi_{\mathrm l}$ (local) | phase field (liquid volume fraction, the registry's §10 $\phi_k$ with $k$ the liquid), 1 liquid, 0 gas (finite-volume cell average) |
| $\psi$ | $\Phi$ (local) | level set (signed distance); **$\psi$ is the entropy flux potential and the TVD limiter in the registry** |
| $\epsilon$ | $\ell$ (local) | interface-width parameter; **collides with the WENO $\epsilon$** |
| $\delta$, $\lambda$ | kept | interface thickness ($3\Delta x$) and sharpness (0.05); **$\delta$ collides with the TENO flag $\delta_k$** |
| $\bar\gamma$, $M_\phi$ | $M_{\mathrm{pf}}$ (local), $M_\phi$ kept | mobility and its coefficient; **$\bar\gamma$ is not the ratio of specific heats** |
| $\delta_\psi$, $b$ | $\delta_b$ (local), $b$ kept | band indicator of half-width $5\delta$; $b$ is also the number of cells per leaf direction in Eq. (47) |
| $\sigma$ | kept | surface-tension coefficient |
| $\kappa$ | $\kappa_{\mathrm c}$ (local) | interface curvature; **$\kappa$ is the kinetic energy in the registry** |
| $Q(\psi)$, $\eta$ | $Q$, kept | level-set quality and its threshold; **$Q$ collides with the SBP matrix, $\eta$ with the entropy** |
| $r_{i-1/2}$, $\Psi(r)$ | $r_{i-1/2}$, $\psi(r_{i-1/2})$ | slope ratio and minmod limiter; the source calls $r$ a "smoothness indicator", not a $\beta_k$ |
| $f_x^{WENO}$, $f_x^{1st}$ | kept | third-order Jiang–Peng WENO and first-order upwind derivatives |
| $L(q)$ | $\mathcal L$ | semi-discrete operator of SSP-RK3 |
| CFL | $\nu$ | 0.4, defined by Eq. (38) |
| $k_{visc}$, $k_{sf}$, $k_{pf}$, $N_d$ | kept | time-step coefficients, space dimension |
| $dh_n$, $m$ | $\Delta x_n$, kept | cell size at tree depth $n$, leaf index |
| $Re$, $We$, $Mo$, $Eo$ | $\mathrm{Re}$, kept | Reynolds, Weber, Morton, Eötvös numbers |

# Reference list

61 printed references in numbered Elsevier style ([1]–[61]), all parsed and
merged complete into the [bibliography](/bibliography.md) with `citedby`
`matsushita-2021`. Same-author same-year works take suffixes in printed order
(Matsushita & Aoki 2019 [19]/[27]). [24] is a CTR research brief, [29]
(Basilisk) a website, [40] a technical report with no printed year (keyed with
the citing year); [31] and [60] print arXiv identifiers. Garbled author lists
([46], [51]), the second author "Y.-T. Liu" of [22] and the truncated DOI of
[52] (omitted) are recorded as printed with notes. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–5 (2026-10-22/23). This source is cited on:

* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Level-set and ghost-fluid interface methods](/methods/level-set-method.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
