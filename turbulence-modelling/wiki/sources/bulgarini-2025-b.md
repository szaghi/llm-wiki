---
type: Source
title: "Bulgarini et al. (2025b) — Efficient h-adaptive isogeometric discontinuous Galerkin solver for turbulent flows"
description: "Two-dimensional isogeometric DG solver for compressible RANS with the Spalart–Allmaras model on rational Bézier elements extracted from CAD NURBS, with anisotropic h-adaptation by knot insertion; four refinement indicators compared, speed-ups up to about six on a transonic NACA 0012 and three on the T106A cascade."
resource: "doi:10.1016/j.jcp.2025.113763"
source_kind: paper
authors: [Bulgarini D., Ghidoni A., Noventa G., Rebay S.]
year: 2025
venue: "J. Comput. Phys. 526:113763"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Computational_Physics_Bulgarini_Efficient_h-adaptive_isogeometric_discontinuous_Galerkin_sol.pdf"
tags: [dg, mesh-adaptation, rans, spalart-allmaras, high-order, turbomachinery]
timestamp: 2026-10-29T05:08:00Z
---

# Summary

Bulgarini et al. (2025b) present a two-dimensional
[isogeometric discontinuous Galerkin](/methods/isogeometric-analysis.md)
solver for the compressible RANS equations closed with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md), coupled with
anisotropic $h$-[adaptation](/methods/mesh-adaptation.md). The geometry is
a NURBS patch taken from the CAD; Bézier extraction (knot insertion until
every interior knot has multiplicity $N$) splits it into rational Bézier
elements whose rational Bernstein basis is both the geometry map and the
DG solution and test space, so the CAD boundary is exact at every
refinement level. Refinement is again knot insertion at the parametric
mid-point of the parent element, in one or both directions, managed in a
quad-tree, with exact transfer of the solution on refinement and a
conservative least-squares projection on coarsening. The discretization
follows the Brescia DG lineage (Roe flux, BR2 viscous flux, the
pressure-gradient-directed [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
of Bassi et al. driven by a flux-jump residual, the
[shock sensor](/definitions/shock-sensor.md) being that residual, the
negative-$\tilde\nu$ modification of Crivellini et al., implicit backward
Euler pseudo-time stepping); the DG basis is modal rational Bézier, not
the nodal [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md).

Four refinement indicators (small-scale energy density, spectral decay,
local and global non-conformity) are compared on the steady laminar
[cylinder](/benchmarks/circular-cylinder-wake.md) at $Re=40$: all give a
speed-up of about two against a uniformly fine mesh, spectral decay is
judged best and anisotropic refinement beats isotropic. A new anisotropy
indicator compares the parametric components of a Jacobian-weighted mean
gradient with a factor-3 threshold. Validation covers Ringleb flow, the
laminar flat plate and the turbulent flat plate against the
[law of the wall](/definitions/law-of-the-wall.md) and Wieghardt's data
([turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).
Adaptation takes the turbulent plate from $y_1^+=100$ to about 1 with
about 60% fewer DoFs and less time than a reference mesh, gives up to
about $5.9\times$ speed-up at 0.34% drag deviation on the transonic
[NACA 0012](/benchmarks/naca-0012-airfoil.md), and up to about $2.6\times$
at 0.17% loss deviation on the T106A
[turbine cascade](/benchmarks/turbine-cascade.md). Linear-boundary meshes
at equal DoFs produce spurious near-wall behaviour and convergence
problems that curved NURBS boundaries avoid. All cases are steady;
evidence is numerical.

# Version read

Version of record (Elsevier, open access CC BY; received 23 August 2024,
revised 12 December 2024, accepted 17 January 2025, online 21 January
2025), 22 pages, all read; pages 4, 5 and 7–11 checked visually for
equations. Page 1 matches the metadata (title, four authors, venue, DOI)
and prints the placeholder MSC codes "0000, 1111". A different paper of
the same group and year, [Bulgarini et al. (2025)](/sources/bulgarini-2025.md),
is not cited here. Numbering on this page is that of the version read.

# Key claims

Page-local symbols (as on [isogeometric analysis](/methods/isogeometric-analysis.md)): $W_i$ the NURBS weights and $R^N_i$ the
NURBS (rational Bézier) basis functions of degree $N$; $\mathbf J$ the
Jacobian matrix of the parametric map (determinant $\mathcal J$);
$\nu_{\mathrm{av}}$ the artificial-viscosity coefficient (the source's
$\epsilon_p$); $(\xi,\eta)$ the parametric coordinates ($\eta$ is not the
Kolmogorov length here); $I_K^{\mathrm{SSED}}$, $I_K^{\mathrm{SD}}$,
$I_K^{\mathrm{LNC}}$, $I_K^{\mathrm{GNC}}$ the refinement indicators of
element $K$; $f_{\mathrm{ref}}$ the percentage of elements flagged for refinement;
$\zeta_{\mathrm L}$ the cascade total-pressure loss coefficient (the
source's $\zeta$).

1. Bézier extraction by repeated knot insertion (interior multiplicity raised to $N$) turns a NURBS patch into rational Bézier elements suitable for DG without changing the geometry; inserting an existing knot lowers the continuity from $C^{N-r}$ to $C^{N-r-1}$ (§2.3, Eqs. 6–7, Fig. 3). **Stated**
2. Geometry and solution use the same rational Bézier basis of degree $N$ per element (Eq. 23), with integrals evaluated in parametric space through the NURBS Jacobian (Eq. 26) (§3.3). **Derived**
3. Gauss–Legendre quadrature with at least $(N+1)^d$ points integrates non-polynomial functions accurately over a highly curved, distorted degree-5 NURBS element of mean aspect ratio about $6\times10^5$, thickness $10^{-6}$–$10^{-7}$ and curvature 6000 mesh units, representative of boundary-layer elements (§3.3, Figs. 5–6). **Shown**
4. Negative $\tilde\nu$ is handled with the modification of Crivellini et al. [26] of the source term (Eqs. 13–14), diffusion coefficient (Eq. 15) and clipped $r$ with $r_{\max}=10^3$ (Eq. 16); free stream $\tilde\nu_\infty=10^{-3}\nu_\infty$ (§3.2). **Stated**
5. The element size of the Bassi et al. artificial viscosity, $h=(\Delta x^{-2}+\Delta y^{-2})^{-1/2}$ (Eq. 31), is unsuitable for Bézier patches because the control points do not interpolate the element borders; the minimum distance between element corners (after Duvigneau [29]) is used (§3.4). **Stated**
6. Refinement by knot insertion transfers the solution exactly; coarsening uses a least-squares projection plus a conservation correction (Eqs. 36–38) and loses information (§4.1). **Derived**
7. Coarsening "had a negligible impact, as refinement was generally performed on converged high-order steady solutions" (§4.2). **Stated**
8. New anisotropy indicator: the parametric components of the Jacobian-weighted mean gradient (Eqs. 44–45) decide; split along $\xi$ if the $\xi$ component exceeds three times the $\eta$ one, along $\eta$ in the reverse case, isotropically otherwise (Algorithm 1). **Stated** (efficiency shown in claims 10, 13–15)
9. On the $Re=40$ cylinder all four indicators mark separation and recirculation-edge regions and adapt symmetrically; SSED over-refines the detachment area; GNC and SSED refine areas outside the regions of interest; SD is "the most effective overall"; LNC performs similarly and "should be used for lower solution approximations" (§4.3, Fig. 9). **Shown**
10. All indicators give "a computational speed-up of ≈ 2 times" against the fine reference (4608 elements, $N=3$, 73 728 DoFs, $C_{D,\mathrm{ref}}=1.41764$), SD slightly more efficient, anisotropic refinement more efficient than isotropic (§4.3, Fig. 10). **Shown**
11. Ringleb flow on linear-boundary meshes develops spurious shocks in the recompression area; curved high-order boundaries are needed for accuracy and stability; $L^2$ error convergence is shown for $N=1$–5, without tabulated orders (§5.1, Figs. 11–12). **Shown**
12. Laminar flat plate ($M=0.3$, $Re=10^6$, 1290 linear elements, $N=4$) and turbulent flat plate ($M=0.2$, $Re=1.1\times10^7$, 8800 linear elements, $y_1^+<1$, $N=4$) agree "perfectly" with Blasius and with the law of the wall and Wieghardt's data in $C_f$ and velocity profile (§§5.2–5.3, Figs. 13–14). **Shown**
13. Adapted turbulent flat plate: from 36×32 = 1152 patches at $y_1^+=100$ to 1834 patches at $y_1^+\approx1$; the adapted results match the reference while the coarse mesh is badly wrong in the viscous sublayer and only slightly off in $C_f$; DoFs and computing time fall by about 60% against a 4617-element $y_1^+=1$ mesh (§6.1, Fig. 15). **Shown**
14. Transonic NACA 0012 ($M_\infty=0.751$, $Re=3.91\cdot10^6$, $\alpha=1.99^\circ$): coarse 48×35 = 1680 patches adapted to 8308 (fine reference 15 360); SD targets shock, boundary layer, wake and separation bubble; adaptation improves the shock location and $C_p$, $C_f$ against McDevitt et al.; the coarse-mesh $C_f$ is "completely wrong" (§6.2, Table 1, Figs. 16–18). **Shown**
15. NACA 0012 speed-up against $f_{\mathrm{ref}}$: 6%, 46 528 DoFs, about $5.9\times$, $C_D=1.80805\cdot10^{-2}$, 0.34% deviation; 12%, 81 232, about $2.9\times$, 1.90%; 20%, 132 928, about $2.7\times$, 1.88%; $C_{D,\mathrm{ref}}=1.80200\cdot10^{-2}$ (Table 2). **Shown**
16. At about equal DoFs, linear boundaries trigger spurious near-wall phenomena that prevent complete convergence of the NACA 0012 case and distort $C_p$, $C_f$ near the leading edge; for the T106A the effect is weaker (subsonic), but full convergence required a lower exponent of the CFL law (§§6.2–6.3, Figs. 19, 23). **Shown**
17. T106A: 9 NURBS surfaces of degree 2, coarse 933 patches adapted to 5106 (fine 6847); SD targets boundary layer, wake, leading and trailing edges and the first half of the pressure side; the adapted suction-side $C_f$ is "in perfect agreement" with the fine-mesh reference (§6.3, Table 3, Figs. 20–22). **Shown**
18. T106A speed-up against $f_{\mathrm{ref}}$: 5%, 33 392 DoFs, about $2.6\times$, $\zeta_{\mathrm L}=2.421\cdot10^{-2}$, 0.17%; 10%, 56 800, about $1.7\times$, 1.49%; 15%, 81 696, about $1.5\times$, 0.24%; $\zeta_{\mathrm L,\mathrm{ref}}=2.417\cdot10^{-2}$; all deviations below 1.5% (Table 4). **Shown**
19. A lower $f_{\mathrm{ref}}$ gives fewer DoFs and higher efficiency at comparable accuracy (up to about $6\times$ for the NACA 0012, about $3\times$ for the T106A) (§§6.2–6.3). **Shown**
20. SD "emerges as the best" indicator, and the anisotropic strategy "guarantees up to ≈ 6× speed-up with respect to the standard non-refined meshes" (§7). **Shown** (on the cases above)
21. Future work: non-ideal equations of state, adjoint-based CAD shape optimization in the NURBS-DG framework, $hp$-refinement (§7). **Stated**

The model in registry notation (Eqs. 9–12): the SA working variable
$\tilde\nu$ (conserved as $\tilde\nu$, not $\rho\tilde\nu$) with source
$c_{b1}\tilde S\tilde\nu-c_{w1}f_w(\tilde\nu/d)^2+\tfrac{c_{b2}}{\sigma}\nabla\tilde\nu\cdot\nabla\tilde\nu$,
$\tilde S=\lvert\Omega\rvert+\tilde\nu f_{v2}/(\kappa^2d^2)$ with
$\lvert\Omega\rvert=\sqrt{2\Omega_{ij}\Omega_{ij}}$, $\nu_t=\tilde\nu f_{v1}$,
and $c_{b1}=0.1355$, $c_{b2}=0.622$, $c_{v1}=7.1$, $\sigma=2/3$,
$c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$, $c_{w2}=0.3$, $c_{w3}=2$,
$\kappa=0.41$, as printed. For $\chi<0$ (Eqs. 13–14) the source becomes
$c_{b1}S\tilde\nu g_n+c_{w1}(\tilde\nu/d)^2+\tfrac{c_{b2}}{\sigma}\nabla\tilde\nu\cdot\nabla\tilde\nu$
with $g_n=1-10^3\chi^2/(1+\chi^2)$, and the diffusion coefficient is
$\tilde\nu(1+\chi)$ for $\chi\ge0$ and $\tilde\nu(1+\chi+\tfrac12\chi^2)$
for $\chi\le0$ (Eq. 15). Motivation (§3.2): the eddy viscosity drops to
near zero in a layer that narrows with $Re$, and in high-order DG this
produces oscillatory solutions with negative $\tilde\nu$. The shock term
(Eqs. 27–30) is $\nu_{\mathrm{av}}=Ch^2\lvert s_p\rvert/\lvert p\rvert$,
$C=0.2$, acting along $\boldsymbol b=\nabla p/(\lvert\nabla p\rvert+\varepsilon)$,
with $s_p$ built from the jump between numerical and physical interface
fluxes; it "is always and everywhere active, but introduces a numerical
viscosity only where nonphysical oscillations occur". The indicators
(Eqs. 39–43): $I_K^{\mathrm{SSED}}$ the $L^2$ norm of the difference
between the degree-$N$ momentum and its projection on degree $N-1$
(Eq. 40 normalizes it by the element size), $I_K^{\mathrm{SD}}$ the same
norm divided by the norm of the degree-$N$ momentum, $I_K^{\mathrm{LNC}}$
the maximum and $I_K^{\mathrm{GNC}}$ the sum over faces and quadrature
points of the normalized momentum jump; the top $f_{\mathrm{ref}}$% of
elements are refined. The validation law of the wall is $u^+=y^+$ and
$u^+=\kappa^{-1}\ln y^++B$ with $\kappa=0.41$, $B=5$.

# Printed slips

- **Eq. (8), energy equation:** the viscous work is printed with $(\nabla\mathbf u-\nabla\mathbf u^T)$, while the momentum equation of Eq. (8) and the viscous flux of Eq. (19) use $(\nabla\mathbf u+\nabla\mathbf u^T)$; the heat flux "$-k\nabla T$" stands outside the divergence.
- **Symbol $k$:** thermal conductivity in Eq. (8), von Kármán constant 0.41 in Eqs. (10)–(12), capital $K$ in $r^*=\tilde\nu/(\tilde SK^2d^2)$ of Eq. (16), and $\kappa=0.41$ in §5.3.
- **Eq. (13):** the negative branch uses $S$ without tilde, not defined in the paper.
- **Eq. (34):** prefactor $1/N$ with the sum running to $m$; $N$ is not defined there.
- **Eqs. (36)–(37):** the father expansion sums $i=0,\dots,n_g$ with $n_g$ defined as "the number of quadrature points"; Eq. (37) defines $\mathbf b$ without a basis function in the integrand.
- **Eq. (39) text:** "where $(\rho\mathbf q)_{h,p-1}$ is the projection of the discrete momentum density", while the formula has $(\rho\mathbf u)_{h,p-1}$.
- **§4.2 (iv):** GNC "evaluates the $L^2$ norm of all the jumps", while Eq. (43) is a plain sum of normalized jump norms.
- **Attributions:** "as identified by Persson et al. [24]", ref. [24] having first author Nguyen (Nguyen, Persson, Peraire); "as described by Bassi et al. [30]", ref. [30] being Z.J. Wang (ed.), *Adaptive High-Order Methods in CFD* (World Scientific 2011).
- **Table 3:** the caption says "distributions on the blade and DoFs", the column reports "Elements".
- **Table 5 against Figs. 15–18:** Table 5 lists the adaptation degree as $\mathbb P^1$ (flat plate) and $\mathbb P^2$ (NACA 0012), while the figure captions state "$\mathbb P^3$ solution approximation" for the same cases.
- **Wording:** §1 calls the flat-plate cases "incompressible", run at $M=0.3$ and $M=0.2$ with the compressible solver; §4 calls the $M=0.1$ cylinder "incompressible". $\mathrm{CFL}_{\min}$, $\mathrm{CFL}_{\max}$, the CFL exponent and the coarsening threshold are not reported.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, $\mathbb P^p$ | $N$ | NURBS/Bézier degree equals the DG degree; $p$ is also pressure (Eqs. 28–29, 46) |
| $(\xi,\eta)$ | $(\xi,\eta)$ (page-local) | parametric coordinates; **collision:** $\eta$ is the registry's Kolmogorov length |
| $\boldsymbol\Xi$, $N_i^p$, $R_i^p$, $\mathbf P_i$ | knot vector, B-spline and NURBS bases, control points (page-local) | |
| $w_i$ | $W_i$ | **collision** with the quadrature weights $w_i$ |
| $\mathbf J_\Omega$ | $\mathbf J$, $\mathcal J=\det\mathbf J$ | |
| $P$, $p$ | $p$ | pressure |
| $k$, $K$ | $\kappa$ (Eqs. 10–12, 16); thermal conductivity (Eq. 8) | **collision** with the turbulent kinetic energy |
| $\Omega=\sqrt{2\boldsymbol\omega:\boldsymbol\omega}$, $\boldsymbol\omega$ | $\lvert\Omega\rvert$, $\Omega_{ij}$ | **collision:** $\boldsymbol\omega$ is the rotation tensor, not the vorticity vector; $\Omega$ also the domain |
| $\tilde\nu$, $\chi$, $\tilde S$, $f_{v1}$, $f_{v2}$, $f_w$, $g$, $r$ | as in the registry and the SA page | |
| $\xi$ (Eq. 15) | SA diffusion coefficient | **collision** with the parametric coordinate |
| $d$ | $d$ (Eq. 9); number of dimensions (Eq. 17) | |
| $\epsilon_p$, $C$, $h_{\Omega_j}$, $\mathbf b$ | $\nu_{\mathrm{av}}$, $C$, $h$, $\boldsymbol b$ | |
| $[\![\cdot]\!]$ | $[\![\cdot]\!]$ | jump |
| $\hat{\mathbf F}$ | $f^*$ | Roe and BR2 |
| $\eta_J^{SSED}$, $\eta_J^{SD}$, $\eta_J^{LNC}$, $\eta_J^{GNC}$ | $I_K^{\mathrm{SSED}}$, $I_K^{\mathrm{SD}}$, $I_K^{\mathrm{LNC}}$, $I_K^{\mathrm{GNC}}$ (page-local) | $\eta$ is the registry's Kolmogorov length |
| $ne^{adp}$ | $f_{\mathrm{ref}}$ (page-local) | |
| $y_1^+$, $u^+$, $u_\tau$ | $y_1^+$, $u^+$, $u_\tau$ | first-element $y^+$ from the element height |
| $\zeta$ | $\zeta_{\mathrm L}$ | **collision** with the registry's feature vector $\boldsymbol\zeta$ |
| $C_d$, $C_D$ | $C_D$ | |

# Reference list

40 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [19]
is the bundle source [Ims & Wang (2023)](/sources/ims-2023.md); no other
cited work falls on the key of a planned or ingested source. [21], [24],
[33] and [34] (AIAA meeting papers) print no year and no venue, the year
being taken from the printed DOI, and [21], [24], [30], [34] print a
publisher URL in an "arXiv:" field; [23] is an undated web item ("N.L.R.
Center, Sst-vm expected results - 2d zero pressure gradient flat plate")
without URL; [11] prints "vol. 128, 2015" without publisher; [17] and
[29] print no page numbers; [22], [32], [38] and [39] print no venue;
[25] prints a stray "1" after its title. No item is printed twice and none
is unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Isogeometric analysis and isogeometric discontinuous Galerkin](/methods/isogeometric-analysis.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
