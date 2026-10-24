---
type: Source
title: "Huang & Johnsen (2023) — A consistent and conservative Phase-Field method for compressible multiphase flows with shocks"
description: "Adds a generic Phase-Field flux to a compressible N-phase diffuse-interface model so that interfaces keep a fixed thickness against numerical diffusion, derives the physical constraints on that flux, and gives a bound-preserving, equilibrium-preserving finite-volume discretization built on two consistency requirements for mass and volume fraction."
resource: "doi:10.1016/j.jcp.2023.112195"
source_kind: paper
authors: [Huang Z., Johnsen E.]
year: 2023
venue: "J. Comput. Phys. 488:112195"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Huang_A_consistent_and_conservative_Phase-Field_method_for_compres.pdf"
tags: [multiphase, interface-capturing, bound-preserving, finite-volume, positivity]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

Material interfaces are linearly degenerate: unlike shocks, they do not
steepen, so the numerical diffusion of capturing schemes thickens them
without bound, and non-uniformly in non-uniform velocity fields. Huang &
Johnsen build a [phase-field](/methods/phase-field-method.md) mechanism into
a compressible multiphase model to hold the interfaces at a finite, uniform
thickness. They start from the
[five-equation](/definitions/five-equation-model.md) framework for
$N_\phi$ phases and add a generic Phase-Field flux $J_k$ (read as
$\phi_k(v-v_k)$) to each volume-fraction equation. The flux is carried
consistently into the phase masses, the mixture momentum and the total
energy. No form of $J_k$ is assumed. The authors then derive the
conditions $J_k$ must meet: the second law, Galilean invariance,
interface equilibrium and consistency of reduction. The favourable case is
$\sum_kJ_k=0$, and the consistent incompressible phase-field model is
recovered in the incompressible limit.

The discretization splits a hyperbolic step (finite volume, MUSCL with
minmod, HLLC, primitive-variable reconstruction, characteristic
decomposition for velocity and pressure only) from a Phase-Field step. Two
consistency requirements are introduced: mass and volume fraction must be
reconstructed consistently (Def. 1), and their Phase-Field fluxes computed
consistently (Def. 2). A reduction-consistent flux
$\tilde J_1=\phi_1^{\downarrow}(1-\phi_1)^{\uparrow}\nabla \Upsilon$,
with $\Upsilon$ from a linear Poisson-type equation, gives the mass fluxes
without computing the phase densities. It keeps velocity, pressure and
temperature equilibrium ([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
It keeps $\phi_1\in[0,1]$ and the partial densities non-negative under a
CFL-like condition ([bound preservation](/properties/bound-preservation.md)),
and it is TVD at first order. The conservative Allen–Cahn model supplies
$\nabla\cdot J_1$. Phases follow the
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md).

The tests are air–helium and air–water
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md),
the [advection of a water disk](/benchmarks/material-interface-advection.md)
at a density ratio near 1000, and the Haas–Sturtevant
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md).
Without the Phase-Field term the interface keeps thickening. With it the
interface holds at 4–5 cells for $\varepsilon_{\mathrm I}/\Delta x=1$, and
conservation and equilibrium errors stay at round-off. Violating Def. 1 or
Def. 2 produces mass spikes of up to 40 %. The paper does not cite
[THINC](/methods/thinc-reconstruction.md)-type sharpening, the bundle's
other route to bounded interface thickness.

# Version read

Version of record (Elsevier typeset; received 24 Dec 2022, revised 28 Apr
2023, accepted 29 Apr 2023, online 9 May 2023), 29 pages, DOI printed on
page 1. Title, authors and venue match Crossref; no identity problem.
Equation, theorem, section and figure numbers are those of the journal
version.

# Key claims

Registry notation: volume fraction $\phi_k$, phase density $\rho_k$,
velocity $v$, pressure $p$, stiffened-gas constant $p_{\infty,k}$, ratio of
specific heats $\gamma_k$ of phase $k$. Page-local symbols: $N_\phi$ (number
of phases), $J_k$ (Phase-Field flux of phase $k$),
$\tilde J_1$ (its discrete form), $K_k$ (compressibility coefficient
of the volume-fraction source), $\mathsf m$ (consistent mass flux),
$\Upsilon$ (auxiliary potential), $f^{\uparrow}$ and $f^{\downarrow}$ (face
values reconstructed upwind and downwind with respect to $\nabla \Upsilon$),
and $\Gamma_{\mathrm m}$, $\varepsilon_{\mathrm I}$ (Allen–Cahn mobility and
interface-thickness parameter).

1. The numerical diffusion of capturing methods thickens material interfaces without bound because, unlike shocks, they are linearly degenerate with no physical steepening; higher order "would only delay" this (§1, citing Harten [23, 24]). **Stated**
2. The $N_\phi$-phase model (Eqs. (1), (3), (6), (8)) conserves phase mass, mixture momentum and total energy, and keeps $\sum_k\phi_k=1$ for any $J_k$, provided $\sum_k\phi_kK_k=0$ (§2.1–2.4, §2.10). **Derived**
3. Consistency of mass conservation and consistency of mass and momentum transport imply the kinetic-energy balance $\partial_t(\rho\lvert v\rvert^2/2)+\nabla\cdot(\mathsf m\lvert v\rvert^2/2)=v\cdot(\nabla\cdot\sigma)$. Violating either adds the spurious source $-\tfrac{\lvert v\rvert^2}2(\partial_t\rho+\nabla\cdot\mathsf m')$ (Thm 2.1, Remark 2.1.1). **Proved**
4. The model satisfies the second law under inequality (10). An admissible closure is a Newtonian stress, Fourier's law, a zero Phase-Field entropy flux, a Phase-Field energy flux $p\sum_lJ_l$, and $\sum_l(J_l-\mathsf b_l\nabla p)=0$ with $\mathsf b_l\ge0$ (Thm 2.2, Remark 2.2.1, Eq. (14)). **Proved**
5. The model is Galilean invariant if $J_k$, $K_k$, the stress and the heat and Phase-Field energy fluxes are frame indifferent (Thm 2.3). **Proved**
6. Isolated interfaces in interfacial equilibrium in a uniform flow are advected with no errors in phase density, velocity, pressure or temperature (Thm 2.4). If $\sum_lJ_l=0$ or $\sum_l\nabla\cdot J_l=0$, this holds for any initial volume fractions (Remark 2.4.1). **Proved**
7. Local consistency of reduction holds if $J_k=0$ where phase $k$ is locally absent and the other fluxes reduce to those of the $(N_\phi-1)$-phase system (Thm 2.5, Eq. (21)). **Proved**
8. With $K_k=0$ (Allaire et al.) the mixture $\rho c^2$ is a convex combination of the $\rho_kc_k^2$. With $K_k=\rho c^2/(\rho_kc_k^2)-1$ (Kapila et al.) the Wood sound speed results (§2.9, Eq. (25)). **Derived**
9. In the incompressible limit, consistency of the volume-fraction and mass equations requires $K_k=-1$. Kapila's model satisfies this, while Allaire's ($K_k=0$) gives inconsistent equations. The model recovers the consistent incompressible phase-field model of [40] (§5.3). **Derived**
10. Earlier compressible phase-field methods [45–47, 55] are tied to specific forms of $J_1$ and need assumptions on the phase densities: small normal gradients [45, 46], constant densities [47], or $\rho_k$ computed as $(\phi\rho)/\phi$ [55], which is not robust near 0 or 1. They introduce $O(1)$ model errors, do not guarantee boundedness and positivity together ([45, 46] violate mass conservation), and are all second order at most (§3.2). **Stated**
11. Consistent reconstruction of mass and volume fraction (Def. 1) holds if both are reconstructed by the same scheme and the scheme preserves affine relations $g=af+b$. MUSCL with most TVD limiters does this, but characteristic-variable reconstruction does not, so mass and volume fraction are reconstructed again from primitive variables after the characteristic reconstruction (§3.1). **Stated**
12. For consistency of reduction in the hyperbolic step, the face velocity in the $\nabla\cdot v$ source of the volume-fraction equation must come from the Riemann solver (§3.1, Thm A.1). **Proved**
13. The reduction-consistent formulation $\tilde J_1=\phi_1^{\downarrow}(1-\phi_1)^{\uparrow}\nabla \Upsilon$ gives the mass fluxes $(\tilde J_1\rho_k)$ without computing $\rho_k$ and satisfies Def. 2 (Eqs. (29)–(31), §3.2.1). **Derived**
14. After the Phase-Field step, $v=v_0$ and $p=p_0$ are preserved, for any explicit time integrator and finite-volume divergence, and for equation-of-state coefficients that depend on $\rho_k$ and $p$ (Thm 3.1, Remarks 3.1.1–3.1.2). **Proved**
15. With first-order reconstruction and forward Euler, $\phi_1\in[0,1]$ and non-negative partial densities are preserved under Eq. (37). A simpler sufficient condition is $2\Delta t\max_i(\lvert\partial_x\Upsilon\rvert/\Delta x)\le1$ (Eq. (41)) (Thm 3.2, Remark 3.2.1). **Proved**
16. High-order extension: with a Gauss–Lobatto decomposition of the cell averages ($N_q$ points, $2N_q-3$ at least the polynomial degree), positivity of the reconstructions at the Gauss–Lobatto points and the step condition (B.9) give bound and positivity preservation. A sufficient condition is $\frac{\Delta t}{\mathsf w_{\mathrm{GL}}}\max_i(\lvert\partial_x\Upsilon\rvert/\Delta x)\le1$, equal to Eq. (41) at second order ($\mathsf w_{\mathrm{GL}}=1/2$) (App. B, Thms B.3, B.4, Eq. (B.12)). **Proved**
17. $\phi_1$ and the partial densities are TVD in the Phase-Field step under Eq. (41) at first order; the second-order case "follows [88, 66]" (Thm C.1). **Proved** (first order; see Printed slips for Eq. (C.2))
18. Replacing the nonlinear Eq. (42) by the linear $\nabla\cdot(\{\!\{\phi_1\}\!\}\{\!\{1-\phi_1\}\!\}\nabla \Upsilon)=\nabla\cdot J_1$ (Eq. (43)) costs at most $O(\Delta x)$ near interfaces, where the shock-capturing scheme is below first order anyway, so the overall accuracy is not degraded (§3.2.4). **Stated**
19. With full implicitness of the Laplacian and $\Gamma_{\mathrm m}\Delta t/\varepsilon_{\mathrm I}^2\le1/4$ the conservative Allen–Cahn update keeps the order parameter in $[0,1]$ (citing [39]). The choice $\Gamma_{\mathrm m}=0.5\varepsilon_{\mathrm I}\max\lvert v\rvert$ gives $\max\lvert v\rvert\Delta t/\varepsilon_{\mathrm I}\le1/2$, less restrictive than the hyperbolic CFL condition (§3.3). **Stated**
20. The scheme is at best second order (midpoint-rule face fluxes, primitive-variable computation). $\nu\le0.5$ is needed in MUSCL–Godunov for the Riemann problems not to interact and for bound preservation in the hyperbolic step (§3.4). **Stated**
21. Air–helium Riemann problem: the interface thickness stays at 6–7 cells with $\varepsilon_{\mathrm I}/\Delta x=1.5$ and keeps growing without the Phase-Field term. With it, the volume fraction is insensitive to the TVD limiter (§4.1, Fig. 3). **Shown**
22. $\varepsilon_{\mathrm I}/\Delta x=0.1$ gives 1–2 cells and $2.0$ gives 8–9 cells. Values below 1 may produce mass overshoots near the interface, so $\Delta x\le\varepsilon_{\mathrm I}\le2\Delta x$ is recommended (§4.1, Fig. 4). **Shown**
23. Gas–liquid Riemann problem (1000 cells): the Phase-Field term keeps the interface at 4–5 cells with $\varepsilon_{\mathrm I}/\Delta x=1$ (§4.2, Fig. 5). **Shown**
24. Water-disk advection ($100\times100$, density ratio near 1000): without the Phase-Field term the disk turns diamond-like through mesh anisotropy; with it, the thickness stays at 4–5 cells and the disk stays circular. Conservation errors and $v$, $p$ errors are at round-off with or without the term (§4.3, Figs. 6–7). **Shown**
25. Shock–bubble interaction: the interface thickness holds at 4–5 cells for the whole run with $\varepsilon_{\mathrm I}/\Delta x=1$. Without the Phase-Field term a non-negligible amount of air diffuses into the helium bubble (§4.4, Figs. 8–9). **Shown**
26. Initializing the volume fraction exactly at 0 and 1 produces negative round-off $\phi_1$ after a few steps in the shock–bubble problem, with or without the Phase-Field term; the range $[10^{-15},1-10^{-15}]$ avoids it (§4.4). **Shown**
27. Violating Def. 1 (mass by WENO5 with a positivity limiter, volume fraction by MUSCL) creates mass spikes near the interface. Violating Def. 2 (volume fraction updated with $\nabla\cdot J_1$, mass with $\tilde J_1$) creates mass spikes of up to 40 % and a thickened mass interface, while, the authors state, the volume fraction looks similar (§5.1, Figs. 10–12). **Shown**
28. Def. 1 alone suffices for temperature equilibrium in the hyperbolic step, a weaker condition than in [53]. The equality of the pressure-based and temperature-based reconstructed internal energies (Lemma 5.1) "was not realized in [53]" (Thm 5.2, Remark 5.2.1). **Proved**
29. The Phase-Field step also preserves temperature equilibrium (Lemma 5.3, Thm 5.4), and the normalized temperature errors in the advection test are of the same order as in [53] (§5.2, Fig. 13). **Proved** and **Shown**

# Printed slips

- §4.3, Eq. (50): the text describes "a disk of water in air" with Phase 1 air and Phase 2 water, but Eq. (50) prints $\phi_1=1$ inside the disk and $\phi_1=0$ outside, which makes the disk phase 1, air. Either the phase labels or the $\phi_1$ values are inverted.
- Appendix C, Eq. (C.2): the printed identity $(\tilde j_1)_x|_{i+1/2}-(\tilde j_1)_x|_i=(1-\phi_1)^{**}|_{i-1/2}\max\big((\partial_x\Upsilon)^{**}|_{i+1/2},0\big)(\phi_{1,i+1}-\phi_{1,i})$ does not hold in general. From Eqs. (38) and (C.1) the min terms cancel and the left side is $\phi_{1,i+1}(1-\phi_1)_i\max(\partial_x\Upsilon|_{i+1/2},0)-\phi_{1,i}(1-\phi_1)_{i-1}\max(\partial_x\Upsilon|_{i-1/2},0)$. With $\phi_{1,i}=\phi_{1,i+1}=0.5$, $\partial_x\Upsilon|_{i+1/2}=1$ and $\partial_x\Upsilon|_{i-1/2}=0$, the left side is $0.25$ and the right side is $0$. The mean-value step of the TVD proof of Thm C.1 therefore has a gap. The bound-preservation Thm 3.2 does not use it *(compiler check, not in the sources)*.
- Eqs. (49)–(50) print the initial data without units or scaling, while the equation-of-state parameters are in Pa and J/kg ($p=714$ against $p_{\infty,2}=10^9$ Pa in Eq. (49); $p=4.819\times10^{-5}$ with $\rho_2=1$ in Eq. (50)). The §5.2 values $C^T_1=701.27$ and $C^T_2=223.37$ J/(kg K) follow from Eq. (22), $C^T_k=(p+p_{\infty,k})/((\gamma_k-1)\rho_kT)$, with $p=101325$ Pa, $\rho_1=1.204$, $\rho_2=1000$ kg/m³ and $T=300$ K. So Eq. (50) is scaled by the water density and by a pressure scale that is not printed *(compiler check, not in the sources)*.
- §4.3: "an angle of 450 relative to the grid" for 45°.
- Conclusion: "Discrete Galerkin (DG) discretization" for discontinuous Galerkin. "unphyscial" (§1).
- Ref. [5] prints "S. Osher, A. Sethian" for Osher & Sethian (1988); recorded as printed.

The shock–bubble data (51) are consistent: a Mach 1.22 shock in air ($\gamma=1.4$, $p=101325$ Pa, $\rho=1.204$) gives the pressure ratio 1.5698, so $p=159061$ Pa, a density of 1.657 and a velocity jump of 114.5 m/s, matching the printed $159060$, $1.658$ and $114.49$ *(compiler check, not in the sources)*.

# Notation map

| Huang & Johnsen 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha_p$ | $\phi_k$ | volume fraction (§10); **collision** with the weights $\alpha_k$ and the DG blending $\alpha$; the source's phase index $p$ becomes $k$ |
| $\rho_p$, $\rho$ | $\rho_k$, $\rho$ | phase and mixture density |
| $(\alpha_1\rho_1)$, $((1-\alpha_1)\rho_2)$ | $\phi_1\rho_1$, $\phi_2\rho_2$ | partial densities ("mass") |
| $N$ | $N_\phi$ (local) | number of phases; **collision** with the DG degree $N$ |
| $\mathbf u$, $\mathbf u_p$ | $v$, $v_k$ | mixture and phase velocity |
| $P$, $T$ | $p$, $T$ | pressure (**collision**: source $p$ is the phase index), temperature |
| $\gamma_p$, $P^\infty_p$ | $\gamma_k$, $p_{\infty,k}$ | stiffened-gas parameters |
| $A^P_p,B^P_p,B^T_p,C^T_p,D_p$ | as printed (local) | stiffened-gas coefficients, $A^P=1/(\gamma-1)$, $B^P=\gamma p_\infty/(\gamma-1)$, $B^T=p_\infty$ |
| $c_p$, $c$ | $c_k$, $c$ | phase and mixture sound speed |
| $\mathbf J_p$, $\tilde{\mathbf J}_1$ | $J_k$, $\tilde J_1$ (local) | Phase-Field flux, continuous and discrete; **collision** with the Jacobian $J$ |
| $K_p$ | $K_k$ (local) | $K_k=0$ Allaire, $K_k=\rho c^2/(\rho_kc_k^2)-1$ Kapila; the runs use $K_1=0$ |
| $\mathbf m$ | $\mathsf m$ (local) | consistent mass flux, Eq. (5) |
| $\boldsymbol\sigma$, $\mathbf q$, $\mathbf q^{nc}$, $\mathbf q^{nc}_s$ | $\sigma$, $q_{\mathrm h}$, $q^{\mathrm{nc}}$ (local); entropy flux in words | stress, heat flux, Phase-Field energy and entropy fluxes |
| $\mathbf U$, $\mathbf V$, $\mathbf W$ | $u$, primitive, characteristic variables | |
| $f^{(+)}$, $f^{(-)}$ | $f^{\uparrow}$, $f^{\downarrow}$ (local) | upwind and downwind face values with respect to $\nabla \Upsilon$ (or $\tilde J_1$); **collision** with the registry's left and right states $u^\mp$ |
| $f^L$, $f^R$ (App. B) | $f^-_{i+1/2}$, $f^+_{i+1/2}$ | left and right face states |
| $\bar f$ (Eq. (43)) | $\{\!\{f\}\!\}$ | linear interpolation to faces |
| $Q$ | $\Upsilon$ (local) | auxiliary potential; **collision** with the SBP matrix $Q$ |
| $\delta=10^{-6}$ | — | regularization of the Poisson coefficient |
| $\phi$, $M$, $\eta$, $g$, $W$ | $\phi_1$, $\Gamma_{\mathrm m}$, $\varepsilon_{\mathrm I}$, $g_{\mathrm w}$ and $\sqrt{g_{\mathrm w}}$ (local) | conservative Allen–Cahn; **collisions** with $M$ (Mach), $\eta$ (entropy), $W$ (Lorentz factor) |
| $\beta_{IMP}$ | as printed | implicitness of the Laplacian, default 0; not a smoothness indicator |
| $\omega_{GL}$ | $\mathsf w_{\mathrm{GL}}$ | Gauss–Lobatto weight, $1/2$ at second order |
| $N_I$ | $N_{\mathrm I}$ (local) | average number of cells across the interface, Eq. (47) |
| CFL | $\nu$ | $\Delta t\max((\lvert v\rvert+c)/\Delta x)$ |

# Reference list

The paper prints 89 references, numbered [1]–[89], with no DOIs. The list
is merged complete into the [bibliography](/bibliography.md) with `citedby`
including `huang-2023`. Same-author same-year works take suffixes in
printed order: Huang 2020 [38]/[39], Huang 2021 [37] (PhD thesis), [41],
[42], Huang 2022 [40], [43], [44], Joshi 2018 [33]/[76], and Harten 1997
[68]/[88] (reprints). Huang 2022 [40] (Huang, Lin & Ardekani, J. Comput.
Appl. Math. 408:114116) is a different work from the ingested
[Huang et al. (2022)](/sources/huang-2022.md) (implicit shock tracking),
so its key needs a suffix that keeps them apart. Ref. [70] (Shu 1998) is a
chapter in Lecture Notes in Mathematics 1697, and ref. [25] is a chapter
with no publisher printed. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–11 (2026-10-23/24). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Conservative phase-field interface methods](/methods/phase-field-method.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
