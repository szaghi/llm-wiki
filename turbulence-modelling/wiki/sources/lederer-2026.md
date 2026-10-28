---
type: Source
title: "Lederer et al. (2026) — High-Order Projection-Based Upwind Method for Simulation of Transitional Turbulent Flows"
description: "Applies high-order projection-based upwinding (HOPU) of an exactly divergence-free mixed stress method, now advanced with a Chorin-type projection scheme, to transitional flow over the Eppler 387 airfoil; lift, drag and the separation bubble match standard upwind implicit LES, while the turbulent boundary layer improves on coarse meshes."
resource: "doi:10.1002/fld.70103"
source_kind: paper
authors: [Lederer P.L., Mooslechner X., Schöberl J.]
year: 2026
venue: "Int. J. Numer. Methods Fluids, article fld.70103"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_International_Journal_for_Numerical_Methods_in_Fluids_Lederer_HighOrder_ProjectionBased_Upwind_Method_for_Simulation_of_Tr.pdf"
tags: [implicit-les, numerical-dissipation, transition, separated-flow, incompressible-flow, high-order]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

Lederer et al. (2026) carry the authors' earlier
[high-order projection-based upwind (HOPU) method](/methods/high-order-projection-based-upwind-method.md)
(Lederer et al. 2023) from channel and periodic-hill flow to transitional
aerodynamic flow. The spatial discretization is the same hybrid mass
conserving mixed stress (MCS) method: an $H(\mathrm{div})$-conforming
Raviart–Thomas velocity of degree $N$ with a pressure of degree $N$
(exactly divergence-free velocity), a trace-free normal–tangential
continuous stress of degree $N+1$, a hybrid facet velocity, weakly imposed
stress symmetry and the DG upwind convective form. The time integration is
new: the IMEX Runge–Kutta scheme of 2023 is replaced by a Chorin-type
projection (operator splitting). Step 1 solves an implicit Stokes-like
problem with explicit convection; static condensation gives a symmetric
positive definite Schur complement, solved by preconditioned conjugate
gradients with an element-wise BDDC preconditioner that becomes purely
local for $\nu\Delta t\ll1$. Step 2 projects onto exactly divergence-free
velocities through a hybridized mixed Poisson problem solved with algebraic
multigrid.

Standard upwind [implicit LES](/definitions/implicit-les.md) and adaptive
HOPU, with no explicit [LES](/definitions/large-eddy-simulation.md)
subgrid model, are compared on the
[Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md) at $Re_c=10^5$,
angle of attack $10^\circ$, and $Re_c=3\cdot10^5$, $4^\circ$, against the
NASA TM 4062 experiments. Both cases have a
[laminar separation bubble](/definitions/laminar-separation-bubble.md) with
turbulent reattachment. Pressure distribution, $C_L$, $C_D$ and the bubble
are essentially identical between the two methods. In the
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md) HOPU
reduces the overprediction of $u^+$ above the viscous sublayer of the
[law of the wall](/definitions/law-of-the-wall.md) and of $k^+$ and
$R_{12}^+$, most clearly on the coarsest mesh at $Re_c=10^5$. The
[numerical dissipation](/properties/numerical-dissipation.md) argument is
the 2023 one: confining the upwind penalty to the high-order part of the
facet jump leaves the laminar instabilities that lead to transition
untouched. The paper positions HOPU against
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md) and
DG-based implicit LES of the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) family;
the MCS method is not a DGSEM. The adaptive settings differ from the 2023
paper (thresholds, indexing, update every 10th step): they are two versions
of the method, not a contradiction. No timings or scaling data are reported.

# Version read

arXiv preprint 2408.06698v1 [cs.CE], 13 August 2024, typeset in the Wiley
journal template with placeholder production fields; 18 pages, all read,
equation pages checked visually. The metadata above are those of the
published version (Int. J. Numer. Methods Fluids, 2026, article
fld.70103; no volume on the Crossref card), whose content was not seen.
Title and authors match Crossref apart from capitalization. Equation,
section, figure and table numbers on this page are those of arXiv v1.

# Key claims

Page-local symbols, as on the
[HOPU page](/methods/high-order-projection-based-upwind-method.md): $l$ the
HOPU facet projection degree ($0\le l\le N$), $l_{\mathrm{loc}}$ its facet
value, $\mathcal P^l$ the facet-wise $L^2$ projection onto tangential
polynomials of degree $l$, $r_J$ the jump indicator and $r_{J,i}$ its
thresholds; $x_s$, $x_r$ the separation and reattachment locations, $c$
the chord; meshes m1–m3 coarse to fine.

1. HOPU applied to the Eppler 387 leaves pressure distribution, lift, drag and separation/reattachment essentially unchanged relative to standard upwind implicit LES: e.g. $Re_c=10^5$, $10^\circ$, m1: implicit LES $C_L=1.274$, $C_D=0.0432$; HOPU $C_L=1.271$, $C_D=0.0436$; $Re_c=3\cdot10^5$, $4^\circ$, m1: both $C_L=0.767$, $C_D=0.0116$ (§4.1, Table 2). **Shown**
2. Experimental reference values (McGhee et al. 1988): $Re_c=10^5$, $10^\circ$: $C_L=1.200$, $C_D=0.0413$; $Re_c=3\cdot10^5$, $4^\circ$: $C_L=0.792$, $C_D=0.0109$, $x_s/c=0.40$, $x_r/c=0.58$ (Table 2). **Stated** (cited experiment)
3. Finest-mesh implicit LES (m3): $Re_c=10^5$, $10^\circ$: $C_L=1.259$, $C_D=0.0411$, $x_s/c=0.010$, $x_r/c=0.027$; $Re_c=3\cdot10^5$, $4^\circ$: $C_L=0.759$, $C_D=0.0113$, $x_s/c=0.467$, $x_r/c=0.560$ (Table 2). At $Re_c=3\cdot10^5$ the experiment separates earlier than the simulation (§4.1). **Shown**
4. The bubble extent from $x_s/c$ to $x_r/c$ grows with resolution; at $Re_c=10^5$ the coarse meshes fail to predict a meaningful bubble, giving a smaller separation or "an (unphysical) almost natural transition" (§4.1, Table 2, Fig. 4). **Shown**
5. The $C_p$ mismatch near the leading edge is attributed to the finite computational domain (§4.1). **Stated**
6. In the viscous sublayer ($y^+<5$) all runs reproduce $u^+$ accurately; for $y^+>10$ implicit LES and HOPU differ significantly, especially on m1, HOPU overpredicting less (§4.2, Fig. 7). **Shown**
7. At $Re_c=10^5$, HOPU on m1 performs "almost as well as the ILES m3" for the velocity profiles (§4.2, Fig. 7). **Shown**
8. HOPU improves more at $Re_c=10^5$, $10^\circ$ than at $Re_c=3\cdot10^5$, $4^\circ$, attributed to the larger extent of turbulent flow (§4.2, §5). **Shown** (attribution **Stated**)
9. HOPU velocity profiles "exhibit an under-dissipative behaviour" because the upwind term penalizes only part of the tangential velocity (§4.2). **Stated**
10. $k^+$ and $R_{12}^+$ from HOPU are less prone to overprediction than with standard upwinding at most locations (§4.2, Figs. 8–9). **Shown**
11. The sharp peak of $\delta^*$ at separation and its later reduction are not captured by the highly under-resolved implicit LES on m1, m2; HOPU differs negligibly from implicit LES in $\delta^*$, $\theta$ and the shape factor (§4.2, Fig. 10, $Re_c=3\cdot10^5$). **Shown**
12. The finest grid gives "precise prediction of transition phenomena" against experiment, read by the authors as an advantage of the low-dissipation MCS method preserving small-scale instabilities (§5). **Shown** (interpretation **Stated**)
13. Laminar disturbances leading to transition are "not significantly affected" by the HOPU convection stabilization, and HOPU improves the turbulent part of the boundary layer "regardless of the transition mechanism" (§5). **Stated** (evidence: the two cases)
14. Grid convergence: the $L^2$ norm of the difference of mean $C_p$ between consecutive meshes falls below 0.01 at m3, which is taken as the grid-independent reference (§4). **Shown**
15. The projection step yields $[\![\boldsymbol g_h\cdot\boldsymbol n]\!]=0$ pointwise ($\boldsymbol g_h$ the source's $\tilde{\boldsymbol u}_h$), hence $\boldsymbol g_h$ lies in the $H(\mathrm{div})$ velocity space, and the update is pointwise divergence-free because the discrete divergence maps into the pressure space (§2.3). **Derived**
16. The step-1 Schur complement $S=A-BM^{-1}B^t$ is symmetric positive definite: $-BM^{-1}B^t$ is spectrally equivalent to an HDG-like stiffness matrix and $A$ is the velocity mass matrix; the stress–multiplier block $M$ is invertible by inf-sup stability (cited) (§2.3). **Stated**/**Derived**
17. For $\nu\Delta t\ll1$ the mass term dominates $S$, the BDDC primal constraints can be skipped, and the preconditioner becomes purely local with "optimal parallel scalability" (§2.3). **Stated** (no scaling data shown)
18. The condensed step-2 matrix is symmetric positive definite (cited Boffi et al.) and is solved with PETSc GAMG (§2.3). **Stated**
19. Exact quadrature of all bilinear forms is "crucial for maintaining the stability of the method, especially in turbulent flow regimes" (§2.2). **Stated**
20. Explicit SGS models are excluded "due to their inferior performance compared to ILES in a DG framework for wall-bounded flow problems" (§3, citing Lederer et al. 2023 and Fernandez et al. 2017). **Stated**
21. DG upwind dissipation acts inherently on the high-order part of the solution, as shown for linear convection–diffusion by Moura et al. (§3.1). **Stated**
22. With $l=N$, $\mathcal P^l=I$ and convection is central; with $\mathcal P^l$ the zero operator the standard upwind form (Eq. 9) is recovered (§3.2). **Derived**
23. Velocity jumps are significantly larger in turbulent wall-bounded regions than in laminar and outer regions (§4, Fig. 3, mode of $l_{\mathrm{loc}}$ on m1). **Shown**
24. Whether the absolute jump $r_J$ is the best indicator is "currently uncertain"; future work is to improve the variant and extend it to fully turbulent high-$Re$ flows (§5). **Stated**

# Printed slips

- **Eq. (5):** printed "$-\frac{1}{\nu}(\sigma,\tau)-(\nabla\cdot\tau,u)-(\gamma,\tau)=0$", while Eq. (2a) carries $-\frac{1}{2\nu}\sigma$ and the text calls $a_h$ "the same 1/(2ν)-scaled L2-inner product as the first term in (5)" (§2.2, pp. 4–5).
- **Eq. (12):** the update is printed "$u^{n+1}_h=u^n_h+\Delta t(u^*_h-\tilde u_h)$". *(Compiler check, not in the sources: in Eq. (10) $u^*_h$ is a velocity, and in Eq. (11) $\tilde u_h$ ($\boldsymbol g_h$ on the HOPU page) is the part of $u^*_h$ removed by the divergence-free projection, also a velocity; adding $\Delta t$ times a velocity to $u^n_h$ is dimensionally inconsistent, and the consistent update is $u^{n+1}_h=u^*_h-\tilde u_h$.)*
- **§4, p. 11:** "Averaging starts after 5 characteristic time lengths (U∞ /c)"; $U_\infty/c$ is an inverse time (the convective time is $c/U_\infty$).
- **$C_{uu}$ (p. 7):** printed "$(\nabla\phi_{u,j}\cdot\phi_{u,j})\cdot\phi_{u,i}$", with $\phi_{u,j}$ repeated also in the facet term: a nonlinear term written as a matrix with a repeated index.
- **Equation numbering (p. 10):** the HOPU form spans the lines labelled (15) and (16); the text refers to "the last integral in (15)", which is on line (16).
- **Undefined facet set:** the facet velocity space requires $\hat v_h=0$ on $\mathcal F_h^D$, but only $\mathcal F_h^I$, $\mathcal F_h^W$, $\mathcal F_h^N$ are defined, with the non-zero Dirichlet facets placed in $\mathcal F_h^I$ (§2.1–2.2).
- **Symbol clash and naming:** $\eta_h$ is the test function of the skew space (Eq. 7b) and $\eta$ the HOPU jump indicator (§3.2); the threshold rule writes $\eta_{loc}$, defined only as $\eta$.
- **Mesh labels:** m1–m3 in Table 1 and the text, M1–M3 in Table 2. §1.2 calls the cases "transient flows", elsewhere "transitional".
- **References:** [16] (Fernandez et al., AIAA 2017) prints "URL 10.1002/fld.4763", the DOI of [14] (Fehn et al. 2019); [14] prints the journal as "Numerical Methods in Fluids 91"; [9] (Chorin) prints the journal as "American Mathematical Society 22"; [35] (Raviart–Thomas) prints "vol. 606, 2006" with no book title.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $p$, $\nu$ | $u_i$, $p$, $\nu$ | incompressible, kinematic pressure |
| $\epsilon(u)=\frac12(\nabla u+\nabla u^t)$ | $S_{ij}$ | |
| $\omega(u)=\gamma$ | $\Omega_{ij}$ | skew part of $\nabla u$, MCS weak-symmetry variable; **collision:** not $\omega$, not the ratio of specific heats |
| $\sigma=2\nu\epsilon(u)$ | $\sigma_{ij}$ | trace-free viscous stress, MCS unknown |
| $k$ | $N$ | degree of the Raviart–Thomas velocity and the pressure, $N=3$; stress degree $N+1$ |
| $l$, $l_{loc}$ | $l$, $l_{\mathrm{loc}}$ (page-local) | HOPU facet projection degree |
| $\Pi^l_{\hat V}$ | $\mathcal P^l$ (page-local) | **collision:** $\Pi$ is the SGS energy flux |
| $\eta$, $\eta_i$, $\eta_{loc}$ | $r_J$, $r_{J,i}$ (page-local) | jump indicator $\int_E\lvert(I-\mathcal P^l)[\![u_h]\!]\rvert ds/\int_E\lvert\{\!\{u_h\}\!\}\rvert ds$; thresholds $\{0.1,0.2,0.3,0.4\}$ with $r_{J,-1}=0$, standard upwinding below $r_{J,0}$; **collision:** not the Kolmogorov length |
| $\langle\cdot\rangle$, $[\![\cdot]\!]$ | $\{\!\{\cdot\}\!\}$, (jump) | facet average; **collision:** not a Reynolds average |
| $u^*_h$, $\tilde u_h$ | $\boldsymbol u_h^*$, $\boldsymbol g_h$ (page-local, as on the [HOPU page](/methods/high-order-projection-based-upwind-method.md)) | intermediate velocity; projection-step velocity; **collision:** the tilde is not a Favre filter |
| $\overline{(\cdot)}$ | $\langle\cdot\rangle$ | time and spanwise average; **collision:** not the LES filter |
| $n$, $n^+$ | $y$, $y^+$ | local wall-normal coordinate |
| $\lvert u_t\rvert^+$ | $u^+$ | mean tangential velocity in wall units, local $u_\tau$ |
| $K^+$ | $k^+$ | mean turbulent kinetic energy in wall units |
| $\overline{u'v'}^+$ | $R_{12}^+$ | kinematic Reynolds shear stress, plotted negative |
| $\kappa=0.41$, $C^+=5.2$ | $\kappa$, $B$ | log-law constants, "fitted for mild adverse pressure gradients", log layer $40<y^+<200$ |
| $\delta^*$, $\theta$, $H$ | $\delta^*$, $\theta$, $H$ (shape factor) | |
| $c_p$, $c_l$, $c_d$ | $C_p$, $C_L$, $C_D$ | |
| $Re$ | $Re_c$ | chord Reynolds number (not defined explicitly in the paper) |
| $\alpha$ | (angle of attack, written out) | **collision:** $\alpha$ is the DG/FV blending factor |
| $x_s/c$, $x_r/c$ | $x_s/c$, $x_r/c$ (page-local) | separation and reattachment locations |
| $\Delta y_w$ | (wall-nearest element height) | element height, not over $N+1$ |

# Reference list

41 printed references, numbered style ([1]–[41]), almost alphabetical
([32], [36], [37] out of order), with titles. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. [24]
(Kou et al. 2023) and [26] (Lederer et al. 2023) are the ingested sources
of those keys. Printed oddities: [16] carries a copied DOI (that of [14]),
dropped and noted; [5] and [12] are book chapters without a book title;
[16] has no venue beyond "AIAA, Denver"; [35] has no book title. [15]/[16]
(Fernandez et al. 2017) and [19]/[20] (Gopalakrishnan et al. 2020) share
author-year stems and take suffixes in printed order; the bibliography
already held the two Fernandez et al. (2017) works with the opposite
suffix assignment, so their identities are decided by venue (J. Comput.
Phys. 336 against the AIAA Denver paper), not by key. No printed
duplicates.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [High-order projection-based upwind (HOPU) method](/methods/high-order-projection-based-upwind-method.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
