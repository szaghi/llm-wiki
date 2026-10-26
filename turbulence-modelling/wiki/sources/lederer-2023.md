---
type: Source
title: "Lederer et al. (2023) — High-order projection-based upwind method for implicit large eddy simulation"
description: "Introduces high-order projection-based upwinding (HOPU), which confines the upwind dissipation of an exactly divergence-free mixed finite-element method to the high-order part of the velocity jump, and compares it with implicit LES and with a projection-based variational multiscale WALE model in channel and periodic-hill flow."
resource: "doi:10.1016/j.jcp.2023.112492"
source_kind: paper
authors: [Lederer P.L., Mooslechner X., Schöberl J.]
year: 2023
venue: "J. Comput. Phys. 493:112492"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Computational_Physics_Lederer_High-order_projection-based_upwind_method_for_implicit_large.pdf"
tags: [implicit-les, numerical-dissipation, les, sgs-model, incompressible-flow]
timestamp: 2026-10-26T07:42:00Z
---

# Summary

Lederer et al. (2023) compare three ways of running scale-resolving
simulations of under-resolved, wall-bounded incompressible turbulence with a
high-order, exactly divergence-free, hybridized mixed finite-element method:
the mass conserving mixed stress (MCS) method, with an $H(\mathrm{div})$
Raviart–Thomas velocity, a normal–tangential continuous trace-free stress and
weakly imposed stress symmetry. Convection uses a DG upwind form and the
IMEX Runge–Kutta scheme ARS(2,2,2), with explicit convection, so the linear
system is factorized once. The code is built on NGSolve/Netgen.

The three approaches are (i) [implicit LES](/definitions/implicit-les.md),
where the upwind jump term of the convective form is the only dissipation;
(ii) a projection-based variational multiscale (VMS) method cast into the
MCS stress, with the eddy viscosity of the [WALE model](/methods/wale-model.md)
acting only on the small resolved scales (an eddy-viscosity closure in the
sense of the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md));
(iii) the paper's contribution,
[high-order projection-based upwinding](/methods/high-order-projection-based-upwind-method.md)
(HOPU), which applies the upwind penalty only to the part of the tangential
velocity jump orthogonal to facet polynomials of degree $l$, with an
adaptive variant that picks $l$ facet by facet from a jump indicator. The
motivation is the authors' observation that velocity jumps, and hence
upwind [numerical dissipation](/properties/numerical-dissipation.md), are
largest near the wall.

Tests are the [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
at $Re_\tau=392.24$ against the [DNS](/definitions/direct-numerical-simulation.md)
of Moser, Kim and Mansour, and the [periodic hill](/benchmarks/periodic-hill.md)
at $Re_h=2800$. VMS–WALE is no better than implicit LES and is slightly worse
at the coarsest resolutions; adaptive HOPU markedly improves the $N=3$
channel mean velocity and the near-wall spectrum, and the coarse-mesh hill
statistics near reattachment, while $N=6$ results are unaffected. The
authors read adaptive HOPU as "a wall model approach for standard DG ILES";
as defined in §3.3 it prescribes no wall stress and uses no matching height,
unlike the methods of [wall-modelled LES](/methods/wall-modelled-les.md). The paper lists the drawbacks of explicit
[LES](/definitions/large-eddy-simulation.md) filtering as motivation, and
cites DG-based implicit LES in the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) family
as context; the MCS method itself is not a DGSEM. No analysis of the HOPU
form (stability, consistency) is given.

# Version read

arXiv preprint 2301.01678v1 [physics.flu-dyn], 4 January 2023 (amsart
layout), 24 pages, all read; equation pages checked visually. The metadata
above are those of the published version (J. Comput. Phys. 493:112492,
2023), whose content was not seen. Title and authors on page 1 match the
Crossref record. Equation, section, figure and table numbers on this page
are those of arXiv v1.

# Key claims

Page-local symbols: $l$ is the HOPU facet projection degree ($0\le l\le N$),
$l_{\mathrm{loc}}$ its facet-local value, $r_J$ the HOPU jump indicator and
$r_{J,i}$ its thresholds (the source's $\eta$, $\eta_i$), $m$ the degree of
the VMS large-scale space, $\mathcal P^l$ the facet $L^2$ projection onto
degree $l$, $N_e$ the number of elements per direction of the channel, as on
the [HOPU page](/methods/high-order-projection-based-upwind-method.md).

1. The MCS method yields the minimal numerical dissipation needed for inf-sup stability of the underlying Stokes system, less than an interior-penalty HDG method, which makes it attractive as an implicit-LES baseline (§1.1). **Stated** (cites [15])
2. With a Raviart–Thomas velocity space of degree $N$ and a pressure space of degree $N$, the discrete divergence maps onto the pressure space (Eq. 5), so Eq. (7c) enforces an exactly divergence-free discrete velocity (§2.2). **Stated** (property cited from [19])
3. Treating diffusion and incompressibility implicitly and convection explicitly with ARS(2,2,2) preserves exact divergence-freeness, needs no nonlinear solver, and the linear system is assembled and factorized once; the elimination is possible only through hybridization (§2.2). **Stated**
4. Exact quadrature of all forms is "of crucial importance for the stability of the method in turbulent flow regime": $N$ Gauss points per direction for $a_h$, $N+1$ for $b_{1h}$, $b_{2h}$, and $\frac{3(N+1)}{2}$ for $c_h$ (§2.2, end). **Stated** (no evidence shown)
5. In the projection-based VMS, an empty large-scale space recovers classical LES, and $m$ high enough that the strain lies in the large-scale space switches the model off; small $m$ means larger model impact (§3.1). **Derived**
6. The MCS VMS form follows from the scale-separated stress $\sigma=2\big((\nu+\nu_t)S_{ij}-\nu_tg_{ij}\big)$, with $g_{ij}$ the $L^2$ projection of $S_{ij}$ onto symmetric element-wise polynomials of degree $m$ (Eqs. 12–14); it adds $g_{ij}$ as an unknown (§3.1). **Derived**
7. Because $\nu_t$ varies in time, the VMS matrix is recomputed only after a fixed interval, which "highly reduces the computational effort and has shown to be of negligible impact on the simulation" (§3.1). **Stated** (no data; interval not given)
8. The upwind jump term of Eq. (9) is "recognized" as the main source of stability in under-resolved flow; in under-resolved turbulence the jumps grow and add local diffusion (§3.2). **Stated** (cites [33])
9. In highly under-resolved simulations the velocity jumps are larger near the wall than in the outer flow, giving excessive near-wall upwind dissipation not needed for stability (§3.3, Figs. 2, 3, 10). **Shown** (jump indicator for the channel, $6^3$ elements, $N=3$, and the coarse hill)
10. HOPU replaces the jump $[\![u_h]\!]$ by $(I-\mathcal P^l)[\![u_h]\!]$ in the upwind integral, confining numerical dissipation to high-order jump components; $l=0$ nearly recovers standard upwinding, $l=N$ gives a central flux (§3.3). **Derived** (definition and limit cases)
11. As $h\to0$, $[\![u_h]\!]\to0$ and the effect of upwinding, and of HOPU, vanishes (§3.3). **Stated**
12. Adaptive HOPU: $l_{\mathrm{loc}}=i$ when $r_{J,i}<r_J\le r_{J,i+1}$, with $r_{J,0}=0<r_{J,1}<\dots<r_{J,N+1}=1$; $l_{\mathrm{loc}}$ is recomputed after every time step (§3.3). **Derived** (definition)
13. In the channel the MCS method needs no bulk-velocity or wall-stress controller: testing the momentum equation with a constant streamwise velocity gives $\sum_T\int_Tf_x\,dx=\sum_T\int_{\partial T\cap\partial\Omega_D}(\sigma_h)_{nt,x}\,ds$ with $(\sigma_h)_{nt,x}=\tau_w$, so the forcing directly fixes the wall stress (§4). **Derived**
14. For all methods, mesh refinement converges the channel statistics to DNS, and even the highly under-resolved settings give meaningful predictions (§4.1, Figs. 1, 4, Table 2). **Shown**
15. $N=6$ gives overall better results than $N=3$ at roughly equal DOF, attributed to a broader resolved range and to dissipation acting on high-frequency modes only (§4.1). **Shown** (attribution **Stated**)
16. VMS (WALE; $m=1$ for $N=3$, $m=3$ for $N=6$) gives roughly the same results as implicit LES on $12^3$ and $16^3$ elements at $N=3$ and on $6^3$ and $8^3$ at $N=6$, because the eddy viscosity vanishes with resolution; on $6^3$ at $N=3$ and $4^3$ at $N=6$ VMS is slightly worse for all quantities, damps more, under-resolves the buffer layer and offsets $u^+$ (§4.1, Fig. 1). **Shown**
17. The model applies no eddy viscosity in the viscous sublayer, which all cases capture accurately (§4.1). **Stated** / **Shown**
18. Adaptive HOPU (thresholds $\{0.025,0.05,0.1\}$ for $N=3$; $\{0.005,0.015,0.03,0.07,0.12,0.2\}$ for $N=6$) significantly improves $u^+$ at $N=3$, especially on $6^3$ elements, resolving the buffer region and improving the log and outer regions; $N=6$ shows no remarkable differences (§4.1, Fig. 4). **Shown**
19. Relative error of the bulk Reynolds number (Table 2) on $6^3$, $12^3$, $16^3$ elements at $N=3$: implicit LES 13.4%, 3.1%, 1.1%; VMS 16.3%, 4.7%, 2.7%; HOPU 0.7%, 1.0%, 0.6%; the authors call it only a rough error estimate (§4.1). **Shown**
20. Reynolds stresses show no significant differences except a slight near-wall improvement with HOPU, best on $6^3$ elements at $N=3$ (§4.1, Fig. 5). **Shown**
21. Energy spectra ($12^3$ elements, $N=3$, planes $y^+=5$ and $40$): all methods match the low wavenumbers; VMS adds dissipation in the mid-to-high range; HOPU reduces excessive damping and gives "a much better prediction of the high wave number range" at $y^+=5$ (§4.1, Fig. 6). **Shown**
22. Periodic hill ($N=3$, coarse and fine meshes): all methods reproduce $u^+$ reasonably; on the coarse mesh HOPU gives better $v^+$ at $x=3h_h,5h_h,8h_h$ (the reattachment region) than implicit LES, and implicit LES and VMS are not fundamentally different (§5.1, Fig. 8). **Shown**
23. Periodic hill, coarse mesh: the Reynolds stresses mostly overestimate the DNS; HOPU gives significantly better $R_{22}^+$ and $R_{12}^+$ than implicit LES, VMS slight to no improvement (§5.1, Fig. 9). **Shown**
24. On the coarse hill, implicit LES has a high jump indicator near the lower wall and downstream of the hill, peaking next to the separation point (§5.1, Fig. 10). **Shown**
25. Conclusion: the SGS model (WALE within VMS) is not fundamentally different from no model and its added dissipation "can harm the implicit dissipation mechanism"; adaptive HOPU "can be interpreted as a wall model approach for standard DG ILES"; whether the jump indicator is the best criterion is left open (§6). **Stated**

# Printed slips

- **Eq. (9) and the HOPU form:** the upwind term is printed $\frac12(u_h\cdot n)[\![u_h]\!]\cdot[\![v_h]\!]$, without an absolute value on $u_h\cdot n$ (and, in Eq. 9, without $\int_E$). *(Compiler check, not in the sources: with the signed normal velocity the term is not sign-definite; the dissipative upwind term the text describes carries $|u_h\cdot n|$.)*
- **MCS VMS system (p. 9):** the momentum test functions are written "$\forall(v_h,\hat v_h,\gamma_h)$", where Eq. (7b) uses $\eta_h$; $\gamma_h$ is the unknown.
- **§2.2:** "We use $k$ Gaussian quadrature points in each direction for $a_h(\cdot,\cdot)$" in a sentence claiming exact integration. *(Compiler check, not in the sources: $a_h$ integrates the product of two stresses of degree $N+1$, degree up to $2N+2$ per direction, while $n$-point Gauss quadrature is exact to degree $2n-1$; exactness needs $N+2$ points.)*
- **Table 3:** the periodic-hill gDOF ($43.2\cdot10^3$ coarse, $331.0\cdot10^3$ fine) equal the channel values of Table 1 for $6^3$ and $12^3$ elements. *(Compiler check, not in the sources: the hill meshes have $12\times8\times6=576$ and $24\times16\times12=4608$ elements at the same $N=3$, against $216$ and $1728$ channel elements, so either the hill element counts or the hill gDOF are misprinted.)*
- **Fig. 5 caption:** "over $y^+$ for the $p=6$ test case", while the figure shows both degrees and the paper's degree symbol is $k$.
- **Eq. (2f)** writes $\partial\Omega_W$ where Eq. (1d) and the text use $\partial\Omega_D$.
- **WALE formula (§3.1):** $\omega^2(u_h)$ is not defined (only $\epsilon^2=\epsilon:\epsilon$ is), and $\epsilon^2(u_h)\epsilon^2(u_h)$ is written as a product of scalars.
- **Language:** "no-slip boundary conditions in order to intimidate rigid walls" (§4, for "imitate"); "assased" (§5).
- **References:** [36] (Balakumar & Ilhwan) prints no year; [11] prints the journal as "Numerical Methods in Fluids 91"; [18] (Raviart & Thomas) prints "vol. 606 … 2006", while [22] prints "Lecture Notes in Math., Vol. 606" with year 1977.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $p$, $\nu$ | $u_i$, $p$, $\nu$ | incompressible, $\rho=1$, kinematic pressure |
| $\epsilon(u)=\frac12(\nabla u+\nabla u^T)$ | $S_{ij}$ | WALE written with $\epsilon^2=\epsilon:\epsilon=S_{ij}S_{ij}$ |
| $\omega(u)=\mathrm{skew}(\nabla u)$ | $\Omega_{ij}$ | **collision:** not the specific dissipation rate |
| $\sigma=2\nu\epsilon(u)$ | $\sigma_{ij}$ | trace-free pseudo-stress; in VMS $2((\nu+\nu_t)S_{ij}-\nu_tg_{ij})$ |
| $\gamma$, $\eta_h$ | — | weak-symmetry multiplier ($=\Omega_{ij}$) and its test function; **collision:** not the ratio of specific heats, not the Kolmogorov length |
| $k$ | $N$ | polynomial degree of velocity and pressure; stress degree $N+1$; Fig. 5 writes $p$ |
| $N$; $N_x,N_y,N_z$ | $N_e$ (page-local); $N_x\times N_y\times N_z$ | elements per direction (channel); hill mesh; **collision:** not the polynomial degree |
| $\eta$, $\eta_i$, $\eta_{loc}$ | $r_J$, $r_{J,i}$, (facet value of $r_J$) (page-local) | HOPU jump indicator $\int_E\lvert(I-\mathcal P^l)[\![u_h]\!]\rvert\,ds\big/\int_E\lvert\langle u_h\rangle\rvert\,ds$ and thresholds; **collision:** not the Kolmogorov length |
| $\Pi^l_{\hat V}$, $\Pi_{L_h}$ | $\mathcal P^l$ (page-local), (element $L^2$ projection) | **collision:** $\Pi$ is the SGS energy flux |
| $l$, $l_{loc}$, $m$ | $l$, $l_{\mathrm{loc}}$, $m$ (page-local) | HOPU facet degree; VMS large-scale degree |
| $\langle\cdot\rangle$ | $\{\!\{\cdot\}\!\}$ | facet average; **collision:** not a Reynolds average |
| $[\![\phi]\!]=\phi^T-\phi^{T'}$ | (jump) | |
| $(\cdot)_{nn}$, $(\cdot)_{nt}$ | — | normal–normal, normal–tangential traces |
| $\nu_t$, $C_w=0.5$ | $\nu_t$, $C_w$ | WALE eddy viscosity and constant |
| $\Delta=\sqrt[3]{\Delta x\Delta y\Delta z}/(k+1)$ | $\Delta=h/(N+1)$ | filter width; $\Delta x,\Delta y,\Delta z$ are element sizes |
| $u_t$, $Re_t$ | $u_\tau$, $Re_\tau$ | $Re_\tau=u_\tau\delta/\nu=392.24$, $\delta=1$ |
| $\bar{(\cdot)}$ ("mean operator") | $\langle\cdot\rangle$ | time and homogeneous-direction average; **collision:** not the LES filter |
| $\overline{u_i'u_j'}^+$ | $R_{ij}^+$ | $(\overline{u_iu_j}-\bar u_i\bar u_j)/u_t^2$, positive convention |
| $h$ (hill), $Re=U_bh/\nu$ | $h_h$ (hill height, page-local), $Re_h$ | **collision:** $h$ is the element size |
| $\Delta y_W^+$ | (size of the wall element over $N+1$, wall units) | *(compiler check, not in the sources: the stretching map $\Phi$ evaluated at the first element edge, times $392.24$, over $N+1$, gives 11.72, 4.31, 3.00, 13.64, 6.70, 4.31, matching Table 1)* |
| $E^+$, $\kappa$ | $E(k)$, $k$ | normalized spectrum, wavenumber; **collision:** $\kappa$ is not the von Kármán constant |
| gDOF | — | DOFs left after static condensation of $\sigma_h$, $\gamma_h$ |

# Reference list

36 printed references, numbered style ([1]–[36]), with titles. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. No DOI or arXiv identifier is printed. [36] (Balakumar & Ilhwan)
prints no year and is keyed with the citing paper's year; [25] and [27]
print no venue; [18] prints a volume and year that disagree with [22] for
the same lecture-notes volume. [15] and [21] share an author-year stem and
take suffixes in printed order. No printed duplicates.

# Pages created or updated

Chunk 4 (2026-10-26). This source is cited on:

- [Periodic hill](/benchmarks/periodic-hill.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [High-order projection-based upwind (HOPU) method](/methods/high-order-projection-based-upwind-method.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [WALE model](/methods/wale-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
