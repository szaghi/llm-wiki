---
type: Source
title: "Bezgin et al. (2023) — JAX-Fluids: A fully-differentiable high-order computational fluid dynamics solver for compressible two-phase flows"
description: "Software paper on JAX-Fluids, a Python/JAX Cartesian finite-volume solver for compressible single- and two-phase (sharp-interface level-set) flows that is differentiable end to end, with WENO/TENO reconstruction, Riemann solvers or characteristic flux splitting, validation tests, single-GPU performance and an end-to-end-trained Rusanov dissipation coefficient."
resource: "doi:10.1016/j.cpc.2022.108527"
source_kind: paper
authors: [Bezgin D.A., Buhendwa A.B., Adams N.A.]
year: 2023
venue: "Comput. Phys. Commun. 282:108527"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computer_Physics_Communications_Bezgin_JAX-Fluids_A_fully-differentiable_high-order_computational_f.pdf"
tags: [software, machine-learning, finite-volume, multiphase, level-set, gpu]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper presents [JAX-Fluids](/software/jax-fluids.md), a three-dimensional
Cartesian finite-volume solver for the compressible Euler and Navier–Stokes
equations, written entirely in Python/JAX. Because it is written in JAX, the whole
solver can be differentiated by automatic differentiation and runs on CPU, GPU
and TPU. The motivation is end-to-end ("online") training of data-driven
submodels with gradients propagated through whole simulation trajectories.

The numerics (§3, Table 2) are taken from the literature:

- cell averages with one-point face quadrature, dimension by dimension;
- a "high-order Godunov" route: WENO reconstruction of primitive or conservative
  variables, optionally in characteristic space, followed by an approximate
  Riemann solver ([Lax–Friedrichs/Rusanov](/methods/lax-friedrichs-flux.md),
  [HLL, HLLC, HLLC-LM](/methods/hll-riemann-solvers.md), AUSM+);
- a flux-splitting route with Roe-averaged
  [characteristic decomposition](/methods/characteristic-decomposition.md);
- reconstructions WENO1 to WENO9-JS, WENO-Z, WENO3-NN, WENO6-CU/CUM and TENO5;
- TVD Runge–Kutta 2/3, ALDM implicit LES, and ideal, stiffened-gas and Tait
  equations of state;
- the Hu et al. (2006) conservative sharp-interface
  [level-set method](/methods/level-set-method.md), with cut-cell apertures, an
  interface Riemann solution with surface tension and conservative mixing of
  small cells. Immersed solids are handled by the same method.

The validation tests are:

- linear advection;
- the [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md) and an
  air–helium two-phase shock tube;
- a lid-driven cavity;
- [decaying compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md);
- bow shocks on an immersed cylinder
  ([flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md));
- an oscillating drop and a sheared drop;
- a Mach 1.22 [shock–helium-bubble interaction](/benchmarks/shock-bubble-interaction.md).

Performance is measured with the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
on one RTX A6000: about $25\times10^{-9}$ s per cell per step for HLLC in single
precision. In §7 automatic-differentiation gradients are checked against finite
differences. A Rusanov flux whose dissipation coefficient is predicted by a
neural network ("Rusanov-NN") is then trained end to end on a coarse-grained 2D
implosion and beats the classical Rusanov flux.

The implosion is a variant: its printed inner state $(\rho,v_1,v_2,p)=(0.14,0,0,0.125)$
on $[0,1]^2$ swaps density and pressure relative to the Liska–Wendroff implosion
recorded on [explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md),
and uses a different domain. The paper does not touch
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md):
its two-phase tests are gas–gas.

# Version read

The file is the arXiv preprint arXiv:2203.13760v1 [physics.flu-dyn] of 25 Mar
2022 (footer "Preprint submitted to Elsevier, March 28, 2022"), not the CPC
version of record, although the archive filename says "Crossref Computer Physics
Communications". It has 53 pages (text with figures to p. 40, Appendix A
pp. 40–42, references pp. 44–53), all read. The title and authors match Crossref;
page 1 prints "JAX-FLUIDS" where the journal writes "JAX-Fluids". Section,
equation, table and reference numbers here are those of the preprint, and the CPC
version was revised (for example, the acknowledgements section is empty in v1).
The code is at github.com/tumaer/JAXFLUIDS (MIT licence).

# Key claims

Registry notation: velocity $v$, the Rusanov dissipation coefficient $a$, and
interface states $u^\mp_{i+1/2}$ (see the notation map).

1. To the authors' knowledge no comprehensive mesh-based differentiable CFD package in the Eulerian frame existed before. JAX-Fluids is presented as the first fully-differentiable framework for 3D compressible two-phase flows with high-order methods (§1). **Stated**
2. Offline-trained ML models suffer from a mismatch between the training and test data distributions. End-to-end training through a differentiable solver alleviates it, because the model sees its own outputs (§1, §7.2). **Stated**
3. Convective fluxes are computed either by the high-order Godunov approach, $\hat f_{i+1/2}=h(u^-_{i+1/2},u^+_{i+1/2})$ after WENO reconstruction in physical or characteristic space (Eq. 10), or by the flux-splitting approach. The latter projects with $L_{i+1/2}$, splits the characteristic fluxes as $\tfrac12(L f\pm\bar\Lambda L u)$ with componentwise local LF or Roe eigenvalues $\bar\Lambda$, applies WENO to the split fluxes, sums and projects back with $R_{i+1/2}$ (§3.3). **Stated** (method description)
4. Reconstruction in physical (component) space can produce spurious oscillations from interacting discontinuities in different fields (citing Qiu & Shu). The slightly oscillatory HLLC/primitive-WENO5-JS Sod and Lax solutions are attributed to this (§3.3; §5.1.2, Figs. 9–10). **Shown** (qualitatively)
5. Face fluxes are evaluated with one-point Gaussian quadrature; higher-order quadrature is possible (§3.1). **Stated**
6. Normal viscous face derivatives use 2nd/4th-order central differences at the face (Eq. 11). Tangential derivatives are computed at cell centres (Eq. 12) and then interpolated to the face (Eq. 13) (§3.4). **Stated**
7. In the two-phase sharp-interface level-set method of Hu et al., each phase is solved separately with volume-fraction-weighted cell averages, aperture-weighted face fluxes and interface fluxes (Eq. 17). Conservation holds because the opposite interface normals make the two interface fluxes equal and opposite (§3.6). **Stated**
8. The interface velocity and the phase-specific interface pressures come from a linearized two-material Riemann problem with surface tension (Eq. 22). The interface pressure jumps when surface tension and curvature are non-zero (§3.6). **Stated**
9. Cut-face apertures are computed analytically from trilinearly interpolated corner level-set values ($2^4$ sign combinations). The volume fraction is computed from seven pyramids (Eq. 24) and the interface segment from aperture differences (Eq. 23) (§3.6). **Stated**
10. Small, newly created and vanished cut cells are handled by conservative mixing with threshold $\alpha_{\mathrm{mix}}=0.6$, using seven target cells in 3D with weights from Eq. (28) and the mixing flux of Eq. (29) (§3.6). **Stated**
11. JIT compilation in JAX requires pure functions and control flow on static arguments only. So the time loop is not jitted (only the time-step, integration-step and forcing routines are), and element-wise conditionals are written as masks (§4.3). **Stated**
12. The `feed_forward` interface (fixed number of steps and fixed $\Delta t$, batched with `jax.vmap`) is jit-compilable and differentiable with `jax.grad`; `simulate` is not differentiable (§4.5). **Stated**
13. For linear advection of $\rho=1.5+\sin(2\pi x)$, $v=p=1$, on 10 to 1000 points to $t=1$ with $\Delta t=10^{-4}$, WENO1, WENO3-JS and WENO5-JS reach orders 1, 2 and 5 in $l_1$, $l_2$ and $l_\infty$. WENO3-JS is said to drop to second order at extrema (§5.1.1, Fig. 8). **Shown**
14. The Sod ($t=0.2$) and Lax ($t=0.14$) tubes on 100 cells: the HLLC and Roe setups agree "very well" with the exact solution (§5.1.2, Figs. 9–10). **Shown**
15. The lid-driven cavity at $\mathrm{Re}=5000$ on $500\times500$ with HLLC gives centre-line velocities that agree with Ghia et al. (§5.1.3, Fig. 11). **Shown**
16. For decaying compressible isotropic turbulence (Spyropoulos & Blaisdell cases 1–3, $M_t=0.2,0.4,0.6$), HLLC on $128^3$ recovers the DNS $\rho_{\mathrm{rms}}(t)$. On $32^3$ ALDM agrees with the DNS and plain HLLC does not (§5.1.4, Fig. 12). **Shown**
17. In the two-phase air ($\gamma=1.4$)–helium ($\gamma=1.667$) shock tube (200 cells, $t=0.15$), the interface position, shock speed and strength are correct. Slight density oscillations at the interface are consistent with Hu et al., since no isobaric fix is used (§5.2.1, Fig. 13). **Shown**
18. The bow shock on an immersed cylinder at Mach 3 and 20 ($480\times1280$, HLLC) reaches a steady state that compares well with the literature (§5.2.2, Fig. 14). **Shown** (qualitative)
19. For the oscillating drop the computed period is $T=1.16336$ against the analytical $T_{\mathrm{ref}}=1.16943$ (Rayleigh, Eq. 35) (§5.2.3, Fig. 15). **Shown**. The printed $T_{\mathrm{ref}}$ is consistent with $R=\sqrt{0.2\cdot0.15}$, $\sigma=0.05$ and unit densities. *(compiler check, not in the sources)*
20. The shear-drop deformation $D(Ca)$ agrees well with Taylor's small-deformation relation, Eq. (37) (§5.2.4, Fig. 16). **Shown**
21. For the Mach 1.22 shock–helium bubble, agreement with Haas & Sturtevant and ALPACA is qualitative. The space–time positions of the upstream, jet and downstream interface points are in "very good quantitative agreement" with Terashima & Tryggvason (§5.2.5, Figs. 17–18). **Shown**
22. Single-GPU performance (RTX A6000, 48 GB; Taylor–Green vortex at Mach 0.1; TVD-RK3), as mean wall time per cell per step in $10^{-9}$ s over $32^3/64^3/128^3/256^3/384^3$ (§6, Table 3). **Shown**
    - HLLC, single precision: 64.41 / 24.39 / 25.09 / 28.36 / 28.11.
    - HLLC, double precision: 98.20 / 93.94 / 92.55 / 92.76 / –.
    - Roe, single precision: 241.71 / 302.20 / 304.55 / 301.78 / –.
    - Roe, double precision: 703.40 / 746.78 / 759.36 / 760.09 / –.
23. Roe characteristic flux splitting costs about an order of magnitude more than HLLC because of the eigen-decomposition. Single precision is 2.5–3× faster than double (§6). **Shown**
24. GPU memory (Table 4) grows to 29849.2 MB for HLLC in single precision at $384^3$, the only configuration that fits in 48 GB at that size (§6). **Shown**
25. The automatic-differentiation gradient of the integral entropy increase after 5 steps with respect to the shock Mach number ($M_S=2$) matches central finite differences, whose error converges at second order, for single-phase and two-phase (full level-set) setups (§7.3, Fig. 19). **Shown**
26. A Rusanov flux whose dissipation coefficient is predicted by a network, $a^{\mathrm{NN}}=\mathrm{NN}(\lvert\Delta v\rvert,v_M,c_M,\lvert\Delta s\rvert)$ (an MLP with three layers of 32 nodes and an exponential output, so $a^{\mathrm{NN}}\ge0$), is trained end to end on 15-step unrolls of a coarse-grained ($32\times32$) implosion. It is less dissipative than Rusanov, stays stable over the full 2501-step trajectory and "consistently outperforms" Rusanov in relative $L_1$ errors of density and pressure, also beyond the 1000-step training horizon (§7.4, Figs. 20–21). **Shown**
27. JAX-Fluids scales "out of the box" to roughly 400 million degrees of freedom on a single GPU, with GPU memory the main limitation. Adaptive multiresolution is problematic under jit because the compute graph must be static, and multi-GPU parallelization is future work (§8). **Stated**
28. Combustion, fluid–structure interaction and cavitation cannot yet be modelled (§8). **Stated**

# Printed slips

- Eq. (13): the interpolation "to the cell face $x_{i+1/2,j,k}$" is printed as $\tfrac12(\cdot_{i-1}+\cdot_{i+1})$ and $\tfrac1{16}(-\cdot_{i-2}+9\cdot_{i-1}+9\cdot_{i+1}-\cdot_{i+2})$. These stencils are symmetric about $x_i$, not $x_{i+1/2}$; the midpoint interpolants are $\tfrac12(\cdot_i+\cdot_{i+1})$ and $\tfrac1{16}(-\cdot_{i-1}+9\cdot_i+9\cdot_{i+1}-\cdot_{i+2})$. *(compiler check, not in the sources)*
- Eq. (12), second-order formula: $\partial_y\psi\vert_{i,j,k}=(-\psi_{j-1}+\psi_{j+1})/\Delta y$. The centred difference needs $2\Delta y$ in the denominator; the fourth-order formula with $12\Delta y$ is correct. *(compiler check, not in the sources)*
- Eq. (23): $\Delta\Gamma=[(\Delta A_x)^2\Delta y\Delta z+(\Delta A_y)^2\Delta x\Delta z+(\Delta A_z)^2\Delta x\Delta y]^{1/2}$ is a length, while in Eq. (24) $\Delta\Gamma\,\phi_{i,j,k}$ must be a volume like the other terms. The consistent form is $[(\Delta A_x\Delta y\Delta z)^2+\dots]^{1/2}$. *(compiler check, not in the sources: dimensional analysis)*
- Sign of the dissipative fluxes: Eq. (9) adds $+\frac1{\Delta x}(F^d_{i+1/2}-F^d_{i-1/2})$, while Eq. (17) puts $F+F^d$ in one bracket with a minus sign.
- Flux-splitting step 3: "$V_j=R^{-1}_{i+1/2}U_i$, $G_j=R^{-1}_{i+1/2}F_i$", with subscript $j$ on the left and $i$ on the right.
- Bow shock (§5.2.2): the state $(\rho,v_1,v_2,p)=(1,\sqrt{1.4}\,Ma,0,1)$ is called the "post shock" state. With $c=\sqrt{1.4}$ it is the undisturbed free stream at Mach $Ma$.
- Shear drop (§5.2.4): "$\mu_b$ and $\mu_d$ the viscosities of the drop and bulk fluid, respectively" reverses the subscript convention of §5.2.3 ($\rho_b$ bulk, $\rho_d$ drop) and of $Ca=\mu_bR\dot s/\sigma$.
- §6: "around 25 μs per time step" for HLLC in single precision, while Table 3 gives about $25\times10^{-9}$ s per cell per step.
- §6: the text lists Taylor–Green runs on $64^3$ to $384^3$, while Tables 3–4 also have a $32^3$ column.
- §8: "roughly 400 million" degrees of freedom. The largest case that fits, $384^3$ cells × 5 variables, is $2.83\times10^8$. *(compiler check, not in the sources)*
- §3.6: "level-set values at the edges of a computational cell" means corners, as the next sentence says.
- Ref. [80] is cited for Pope's turbulence material, but it is printed as Vinet & Zhedanov (2011), "A 'missing' family of classical orthogonal polynomials", with a URL querying "turbulent flows pope". The acknowledgements heading is empty.
- Table 2: "WENO3-JS/Z/N/F3+/NN [45, 62, 63, 37]" lists five schemes with four references.

# Notation map

| Bezgin et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $W$ | $u$; primitive vector $(\rho,v,p)$ | conservative and primitive variables |
| $\bar U_{i,j,k}$ | $\bar u_i$ | cell average (finite volume) |
| $u,v,w$ | $v_1,v_2,v_3$ | velocity components |
| $F,G,H$ | $f^{(1)},f^{(2)},f^{(3)}$; $\hat f_{i+1/2}$ | **the same letters for physical and numerical fluxes** |
| $F^d$ | kept | dissipative flux |
| $U^\pm_{i+1/2}$, $W^\pm_{i+1/2}$ | $u^\mp_{i+1/2}$ | reconstructed face states; Eq. (10) lists $U^-$ then $U^+$ |
| $R_{i+1/2}$, $R^{-1}_{i+1/2}$, $\Lambda_{i+1/2}$ | $R_{i+1/2}$, $L_{i+1/2}$, $\mathrm{diag}(\lambda_l)$ | face eigen-decomposition |
| $V_j$, $G_j$, $\hat G^\pm$ | $\zeta$ (characteristic variables), $Lf$, split characteristic fluxes | **$G$ collides with the $y$-flux and with the admissible set $G$** |
| $\gamma$, $B$ | $\gamma$, $p_\infty$ | stiffened gas $p=(\gamma-1)\rho e-\gamma B$; single-phase use |
| $\phi$ | kept (level set) | page-local on [level-set method](/methods/level-set-method.md) |
| $\alpha$ (two-phase) | $\phi_k$ | volume fraction; **collides with the Rusanov $\alpha$ and with $\alpha_k$** |
| $A_{i\pm1/2}$ | kept (apertures) | **collides with the flux Jacobian $A$** |
| $\beta_{trg}$ | kept (mixing weights) | **not a smoothness indicator $\beta_k$** |
| $\sigma$, $\kappa$ | kept (surface tension, curvature) | **$\kappa$ is the kinetic energy in the registry** |
| $\alpha_{\mathrm{Rusanov}}$, $\alpha^{NN}$ | $a$, $a^{\mathrm{NN}}$ | Rusanov dissipation coefficient |
| $\tau$ | kept per use | fictitious time, eddy-turnover time, trajectory |
| $CFL$ | $\nu$ | 0.9 with TVD-RK3; definition deferred to ALPACA |
| $\Delta S^n$, $s$ | kept, $s$ | integral entropy increase (physical entropy, increasing) |

# Reference list

There are 93 printed references in numbered Elsevier style ([1]–[93]), all
parsed and merged complete into the [bibliography](/bibliography.md) with
`citedby` `bezgin-2023`. Eight items print no year ([2], [33], [34], [35], [39],
[42], [69], [92]). They carry the citing year 2023 with a note, and the closing
duplicate sweep is to resolve them. Ref. [80] is garbled (see Printed slips) and
is kept as printed. Software and conference items (JAX, Haiku, Optax, TensorFlow,
PyTorch, Adam) are recorded in their printed form. Ref. [37] is the ingested
source `bezgin-2022`. Ref. [59] (Fleischmann et al. 2020, JCP 423:109762) is a different work from the
existing `fleischmann-2020` and is entered as `fleischmann-2020-b`. Ref. [63] (Gande &
Bhise, printed 2021, Numer. Algorithms 88:249–279) is merged into the existing
`gande-2020`, with the printed year and coordinates recorded in its note. No printed duplicates
were found.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–11 (2026-10-23/24). This source is cited on:

* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
* [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [JAX-Fluids](/software/jax-fluids.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Level-set and ghost-fluid interface methods](/methods/level-set-method.md)
* [Lid-driven cavity](/benchmarks/lid-driven-cavity.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
