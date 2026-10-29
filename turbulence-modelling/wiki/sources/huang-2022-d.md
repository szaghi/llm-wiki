---
type: Source
title: "Huang et al. (2022b) — High-order compact finite volume schemes for solving the Reynolds averaged Navier-Stokes equations on the unstructured mixed grids with a large aspect ratio"
description: "Fourth-order compact finite-volume RANS solver with the Spalart–Allmaras model on unstructured mixed grids: variational-reconstruction weights optimized for large-aspect-ratio near-wall cells, and an exponential-decay procedure that keeps the SA working variable positive without the negative-SA model."
resource: "doi:10.1016/j.jcp.2022.111458"
source_kind: paper
authors: [Huang Q.-M., Ren Y.-X., Wang Q., Pan J.-H.]
year: 2022
venue: "J. Comput. Phys. 467:111458"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Huang_High-order_compact_finite_volume_schemes_for_solving_the_Rey.pdf"
tags: [rans, spalart-allmaras, high-order, numerical-dissipation, high-lift]
timestamp: 2026-10-29T10:10:00Z
---

# Summary

Huang et al. (2022b) build a cell-centred finite-volume RANS solver of up
to fourth order on 2-D unstructured mixed grids. It uses the compact
variational reconstruction of Wang, Ren, Pan et al. and the standard
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md). Two
obstacles of high-order RANS are addressed. The first is the loss of
reconstruction accuracy on near-wall quadrilaterals with aspect ratios of
$10^2$–$10^3$ ([boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)).
The second is negative eddy viscosity, which Gibbs-type oscillations of
$\tilde\nu$ produce at the under-resolved outer edge of the boundary layer.

The variational reconstruction minimizes a sum of weighted interface jumps
of the polynomial and its derivatives. For the first obstacle, the authors
choose the derivative weights by a 1-D Fourier (modified-wavenumber)
analysis under a monotonicity constraint, with the objective of Ponziani et
al. ([numerical dissipation](/properties/numerical-dissipation.md) and
dispersion; compare [low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).
They choose the geometric weight by a 2-D analysis on stretched rectangles,
which gives the exponent $1/2$, and carry both choices over to arbitrary
grids. A static reconstruction of a manufactured boundary-layer profile
([method of manufactured solutions](/methods/method-of-manufactured-solutions.md),
used for reconstruction accuracy only) confirms the gain.

For the second obstacle they propose an exponential-decay procedure. Near
the minimum of $\tilde\nu$ the SA equation reduces to
$\partial_t\ln(\rho\tilde\nu)\approx r_0<0$, so $\rho\tilde\nu$ decays
exponentially. The implicit residual is modified accordingly in the cells
where the update would fall below a threshold. Neither the negative-SA
model nor a reconstruction limiter is then needed.

Tests include the NASA TMR [flat plate](/benchmarks/turbulent-boundary-layer.md),
the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $15^\circ$ on three
meshes, and the [30P-30N three-element airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
at $16^\circ$ (a configuration distinct from the
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)).
The fourth-order scheme matches the fine-grid reference skin friction on
the flat plate, reaches a 0.19% lift error on the finest NACA 0012 mesh
against 14.88% at second order, and removes a spurious trailing-edge
separation. It is also more efficient per unit accuracy. The wall-resolved
grids ($y^+\approx0.5$–1) need no
[wall functions](/methods/rans-wall-function.md). The paper places its
scheme beside the [DG](/methods/discontinuous-galerkin-spectral-element-method.md)
approaches to high-order RANS, and uses a troubled-cell detector with a
WBAP limiter only for the start-up of the 30P-30N case (compare
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).

# Version read

Version of record (J. Comput. Phys. 467:111458; received 14 November 2021,
accepted 4 July 2022), 39 pages, all read; equations on pp. 3, 10–13, 19,
21–23 checked visually because text extraction dropped $\Omega$ and
$\varpi$. Page-1 title, four authors and DOI match the metadata above. No
identity problem. Numbering on this page is that of this version.

# Key claims

1. A three-step optimization (derivative weights in 1-D, the geometric weight on uniform 2-D rectangles, then generalization to unstructured grids) makes the variational reconstruction more accurate on large-aspect-ratio quadrilaterals; the authors call the approach "of course not rigorous" but necessary, because direct optimization on general grids is "impossible" (§2.4). **Stated**
2. The derivative weights depend only on $p+q$, $\mathcal W^D_f(p,q)=\varpi_{p+q}d_{ij}^{p+q}$ (Eq. 26), with $\varpi_0=1$ and $\varpi_{p_1+q_1}\le\varpi_{p_2+q_2}$ when $p_1+q_1\ge p_2+q_2$ (Eq. 27); violating Eq. 27 "is likely" to cause instability "according to our experience" (§2.4). **Stated**
3. Optimized derivative weights (Table 1): cubic constrained $\varpi_1=0.5295$, $\varpi_2=\varpi_3=0.2117$; cubic unconstrained $0.1407$, $0.0402$, $0.0804$; quadratic constrained $0.4643$, $0.1559$; quadratic unconstrained $0.0812$, $0.0201$; against Pan et al. ($1$, $1/2$, $1/6$), Cheng et al. ($1$, $1/2$) and Li et al. ($1/2$, $1/4$) (§2.4.1). **Shown**
4. The unconstrained weights give better dispersion and dissipation curves but schemes that are "not robust", which the authors attribute to their much smaller dissipation (leading term $-3.23\times10^{-3}\theta_w^8\,at/\Delta x$ against $-2.24\times10^{-2}\theta_w^8\,at/\Delta x$ constrained) (§2.4.1, Fig. 4). **Shown** (robustness asserted, not displayed)
5. The 1-D scheme with cubic variational reconstruction is fourth order: $\lim\mathrm{Im}(\theta_w')\,at/\Delta x\approx-\tfrac12\varpi_3^2\theta_w^8\,at/\Delta x=O(\Delta x^7)$ and $\lim\mathrm{Re}(\theta_w')/\theta_w\approx1+\theta_w^4/720$; the optimization does not change the order (§2.4.1). **Derived**
6. The optimal weights of a higher-degree reconstruction are not the extension of the lower-degree ones; each degree is optimized separately (§2.4.1). **Shown**
7. For the 2-D linear reconstruction the normalized objective is minimized for $a_g\ge1/2$ at every aspect ratio and advection angle tested; $a_g=1/2$ is chosen (§2.4.2, Fig. 7). **Shown**
8. For the 2-D quadratic reconstruction at aspect ratio 1000, $a_g=1/2$ is optimal for horizontal advection and $a_g=3/2$ for inclined advection; since the objective varies slowly for $a_g\ge0$, $a_g=1/2$ is taken as "near-optimal", "even for the cubic reconstruction" (§2.4.2, Fig. 8). **Shown** (cubic extrapolated, tested in claim 10)
9. Final weights for unstructured 2-D grids: $\mathcal W^G_f=(S_{i,j}/d_{ij})^{1/2}$ (Eq. 51) and $\mathcal W^D_f(p,q)=\varpi_{p+q}d_{ij}^{p+q}$ (Eq. 50) with Table 2 values; two 3-D variants are proposed, not verified (§2.4.3). **Stated**
10. Static cubic reconstruction of a manufactured boundary-layer profile, $L_2$ error of $\partial u/\partial y$ on mesh 1 (uniform, aspect ratio 500) / mesh 2 (curved, about 1000) (Table 3): Pan et al. $3.49\times10^{-3}$ / $6.84\times10^{-2}$; Cheng et al. $5.22\times10^{-3}$ / $1.38\times10^{-3}$; optimal derivative weights with the geometric weight of Pan et al. divergent / $1.50\times10^{-1}$; with that of Li et al. $1.39\times10^{-3}$ / $8.04\times10^{-4}$; fully optimized $1.39\times10^{-3}$ / $7.33\times10^{-4}$ (§2.4.3). **Shown**
11. Optimal derivative weights combined with the geometric weight of Pan et al. give very poor results, so the geometric weight must be optimized too (§2.4.3). **Shown**
12. Negative eddy viscosity in high-order SA solutions comes from Gibbs oscillations where the grid is too coarse, typically at the boundary-layer edge, and can make the computation diverge (§2.5, Fig. 12). **Stated** (cited)
13. Near the minimum of $\tilde\nu$, neglecting diffusion and $O(h)$ terms and freezing the bracket at a reference state, the SA equation becomes $\partial_t\ln(\rho\tilde\nu)\approx r_0$; when negative $\tilde\nu$ appears "it usually comes with" $r_0<0$, so $\rho\tilde\nu$ decays exponentially and stays non-negative while $\rho>0$ (§2.5, Eqs. 53–57). **Derived**
14. The exponential-decay residual $\mathsf R^{*}_i=\frac{(\rho\tilde\nu)^n_i}{\Delta t}\big(e^{\mathsf R^n_i\Delta t/(\rho\tilde\nu)^n_i}-1\big)$ (Eq. 66) tends to zero when $\mathsf R^n_i\to0$ with $(\rho\tilde\nu)^n_i>0$, or when $(\rho\tilde\nu)^n_i\to0$ with $\mathsf R^n_i<0$, so it does not prevent convergence (§2.5, Eqs. 67–68). **Derived**
15. With the exponential-decay procedure the standard SA model suffices for a positive eddy viscosity; the negative-SA modification is not needed (§2.1, §2.5). **Shown** (NACA 0012 at $15^\circ$, Figs. 14–18; no side-by-side comparison with negative SA)
16. The procedure changes neither the SA model nor the reconstruction, works with implicit time integration and, acting only on the residual, applies to any spatial discretization (§2.5). **Stated**
17. In the NACA 0012 test at CFL 20, the corrected cells lie near the boundary-layer edge and move downstream; the cells needing the final direct replacement are far fewer and vanish near convergence (§2.5, Figs. 15–18). **Shown**
18. Flat plate ($Re=5\times10^6$, $M=0.2$, $137\times97$ cells): both schemes converge the density increment to about $10^{-10}$; the fourth-order skin friction agrees "very well" with CFL3D on the $545\times385$ grid, the second-order one differs slightly and under-predicts the log-region velocity (§3.1, Figs. 20–23). **Shown**
19. NACA 0012 at $15^\circ$: the second-order scheme does not converge lift and drag on mesh 3 and differs largely from experiment even on the finest grid; fourth-order lift is accurate on mesh 3 and drag on meshes 2 and 3, and fourth-order $C_p$ curves overlap across grids (§3.2, Figs. 25–28). **Shown**
20. The second-order scheme predicts a trailing-edge separation bubble on all three meshes; the fourth-order scheme a small one on mesh 1 and none on meshes 2–3; the bubbles and the large eddy viscosity near them degrade the second-order lift, drag and upper-surface $C_p$ (§3.2, Fig. 29). **Shown**
21. Lift and efficiency $E=1/(\epsilon T)$ (Table 6, reference $C_L=1.526$): second order on meshes 1–4 gives $C_L=1.183$, $1.277$, $1.299$, $1.437$ (errors 22.48%, 16.32%, 14.88%, 5.74%; relative CPU 1, 1.82, 3.01, 22.02); fourth order on meshes 1–3 gives $1.393$, $1.499$, $1.523$ (8.72%, 1.77%, 0.19%; CPU 1.43, 2.75, 4.50); second-order efficiency falls and fourth-order efficiency rises on refinement (§3.2, Fig. 30). **Shown**
22. 30P-30N at $16^\circ$ on 53,870 cells: the optimized fourth-order scheme predicts lift and drag closer to the DLR reference than the fourth-order scheme of Pan et al.; both beat second order; its skin friction is closer to the $N=4$ DG result of Burgess & Mavriplis (1,119,530 degrees of freedom); all schemes miss some peaks (§3.3, Figs. 33–34). **Shown**
23. The fourth-order scheme carries the high-eddy-viscosity slat wake to the outlet while the second-order scheme dissipates it quickly; the authors link this to the improved skin friction (§3.3, Fig. 35). **Shown**
24. The WBAP limiter with a shock detector is used on the 30P-30N case only to stabilize the first iterations; few cells are flagged at convergence, so the results are unaffected (§3.3). **Stated**
25. On the same grid the high-order scheme is costlier but more efficient at equal accuracy (§4). **Shown** (Table 6)

# Printed slips

- **Constraint direction, p. 13:** "According to Eq. (27), we introduce the following constraint $\varpi_1\le\varpi_2\le\varpi_3$" reverses Eq. 27, which requires $\varpi_3\le\varpi_2\le\varpi_1$; the constrained values of Table 1 ($0.5295\ge0.2117\ge0.2117$; $0.4643\ge0.1559$) follow Eq. 27.
- **LU-SGS citation:** LU-SGS is cited as [49] (§2.2, §2.5), but [49] is Reichardt (1951), a wall-law paper; Reichardt's title is printed "Vollstndige".
- **Figure number, p. 19:** "the friction coefficient data … shown in Fig. 8 are fitted"; the fit is in Fig. 9.
- **Friction velocity, p. 19:** $u_\tau=\sqrt{\rho_0u_0^2C_f/\rho}=\sqrt{a\rho_0u_0^2x^b/2\rho}$ with $C_f=ax^b$: the two forms differ by the factor $1/2$ under the root.
- **Table 6, second order, mesh 4:** *(compiler check, not in the sources)* $(1.526-1.437)/1.526=5.83\%$, printed 5.74%; the printed efficiency 0.791 agrees with 5.74% and CPU 22.02.
- **§3.2:** mesh 4 is "an even smaller mesh … consisting of 143700 cells", the largest mesh of the study.
- **Eq. 3** prints the RANS flux symbols $F_{c,i}$, $F_{v,i}$ where the SA fluxes $\tilde F_{c,i}$, $\tilde F_{v,i}$ are meant.
- **Rotation tensor:** $\omega_{ij}=\tfrac12(\partial u_i/\partial x_j+\partial u_j/\partial x_i)$, printed with a plus sign, is the strain-rate tensor, although $\Omega=\sqrt{2\omega_{ij}\omega_{ij}}$ is called the vorticity.
- **Section references:** §2.5 says the LU-SGS procedure (Eq. 17) was "introduced in Section 2.1"; it is in §2.2.
- **Minor:** "between of the fourth- and second-order schemes" (Fig. 30 caption), "turbulent and viscosity" (Fig. 35 caption), "One the other hand" (§3.2); ref. [17] repeats "basic formulation".

# Notation map

| Huang et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\hat\upsilon$, $\rho\hat\upsilon$ | $\tilde\nu$, $\rho\tilde\nu$ | SA working variable; **collision:** hat is the test filter in the registry |
| $\mu_L$, $\mu_T=\rho\hat\upsilon f_{v1}$ | $\mu$, $\mu_t$ | |
| $\hat\kappa$ | $\kappa$ | von Kármán constant 0.41 |
| $\Omega=\sqrt{2\omega_{ij}\omega_{ij}}$ | $\lvert\Omega\rvert$ | printed $\omega_{ij}$ is the symmetric tensor (Printed slips); **collision:** $\omega$ is the specific dissipation rate in the registry |
| $C_{b1},\dots,C_{t4}$, $\sigma$ | $c_{b1},\dots,c_{t4}$, $\sigma$ | constants as printed: $\sigma=2/3$, $c_{b1}=0.1355$, $c_{b2}=0.622$, $c_{w2}=0.3$, $c_{w3}=2$, $c_{v1}=7.1$, $c_{t3}=1.2$, $c_{t4}=0.5$ |
| SA diffusion $(\mu_L+\mu_T)/\sigma$ | $(\mu+\mu_t)/\sigma$ | as printed (Eqs. 3, 6) |
| $\sigma_{ij}$ | $2(\mu+\mu_t)S^d_{ij}$ | viscous stress plus the Boussinesq closure, no $\tfrac23\rho k$ term; **collision:** the registry $\sigma_{ij}$ is the molecular stress only |
| overbar ($\bar U_i$, $\overline{\rho\hat\upsilon}_i$) | $(\cdot)_i$ cell average | **collision:** not an LES filter |
| $\bar R_{T,i}$, $\bar R^{n+1,*}_{T,i}$ | $\mathsf R_i$, $\mathsf R^*_i$ (page-local) | SA residual and its exponential-decay modification |
| $\tilde R^n_0$ | $r_0$ (page-local) | frozen decay rate; **collision** with the registry tilde |
| $\delta=10^{-6}$ | $\delta_{\mathrm{EDP}}$ (page-local) | positivity threshold; **collision** with the boundary-layer thickness |
| $k$ (reconstruction degree) | (linear, quadratic, cubic) | **collision** with the TKE |
| $\omega^G_f$, $\omega^D_f(p,q)$, $\varpi_n$ | $\mathcal W^G_f$, $\mathcal W^D_f(p,q)$, $\varpi_n$ (geometric and derivative weights; weight parameters; page-local, as on [boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)) | **collision:** $\omega$ is the specific dissipation rate |
| $\alpha$ (§2.4) | $a_g$ (page-local, as on the boundary-layer-conforming-grid page) | exponent of the geometric weight; $\alpha$ also the angle of attack |
| $\lambda$, $\lambda_{ij}=S_{i,j}/d_{ij}$ | (aspect ratio; face-length to centroid-distance ratio) | **collision** with the Taylor microscale |
| $\kappa$, $\kappa'$ (§2.4) | $\theta_w$, $\theta_w'$ (page-local) | non-dimensional and modified wavenumber; $\kappa$ is also the conductivity (§2.1) and the von Kármán constant (Eq. 52) |
| $\upsilon$ (Eq. 52), $u^+$, $y^+$, $u_\tau$ | $\nu$, $u^+$, $y^+$, $u_\tau$ | $\upsilon$ also an objective-function parameter |
| $E=1/(\varepsilon T)$ | $E=1/(\epsilon T)$ (page-local) | efficiency; $E$ also total energy and objective function |
| $Ma$, $Re$ | $M$, $Re_c$ (airfoils) | |
| O2, O4 | second-, fourth-order scheme | |

# Reference list

70 printed references, numbered. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [1]
(Wang et al. 2013, Int. J. Numer. Methods Fluids 72) is the same work as
the ingested [Wang et al. (2013)](/sources/wang-2013.md). Ref. [67] (Li, Chen & Ren, J. Comput. Phys.
448:110770) is a different work from the ingested [Li & Liu (2022)](/sources/li-2022.md) and is keyed `li-2022-c`; ref. [37] (Wang L. et al. 2013, AIAA) is keyed `wang-2013-e`. Ref. [65], the NASA Turbulence Modeling Resource web page,
is undated. Same-author same-year works take suffixes in printed order
(Wang 2016, [2], [3]; Bassi 1997, [14], [15]; Zhang 2012, [23], [24];
Wang 2013, [1], [37]). Refs. [37] and [39] print only a place and an AIAA
paper number; ref. [49] is cited in the text for LU-SGS (Printed slips).
No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-27), cited further in chunk 11. This source is cited on:

- [30P30N three-element high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Boundary-layer-conforming grids for wall-modelled LES](/methods/boundary-layer-conforming-grid.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Low-dissipation low-dispersion schemes with shock sensor](/methods/low-dissipation-low-dispersion-scheme.md)
- [Method of manufactured solutions](/methods/method-of-manufactured-solutions.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
