---
type: Source
title: "Lodares et al. (2022) — An entropy–stable discontinuous Galerkin approximation of the Spalart–Allmaras turbulence model for the compressible Reynolds Averaged Navier–Stokes equations"
description: "Entropy-stable Gauss–Lobatto DGSEM for compressible RANS with the Spalart–Allmaras model: the entropy is augmented by ½ρν̃², the SA two-point flux and wall conditions are proved stable when c_b2≤1, and the scheme is verified by manufactured solutions, a random-state test and NASA flat-plate and NACA 0012 cases."
resource: "doi:10.1016/j.jcp.2022.110998"
source_kind: paper
authors: [Lodares D., Manzanero J., Ferrer E., Valero E.]
year: 2022
venue: "J. Comput. Phys. 455:110998"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Lodares_An_entropystable_discontinuous_Galerkin_approximation_of_the.pdf"
tags: [rans, spalart-allmaras, dg, entropy-stable, kinetic-energy-preserving]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Lodares et al. (2022) build a provably entropy-stable
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) on
Gauss–Lobatto nodes (summation-by-parts with simultaneous approximation
terms) for the compressible RANS equations closed by the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) under the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md). The
authors know of no earlier rigorous entropy-stable DGSEM for RANS.

In the continuous analysis the Navier–Stokes entropy (the kinetic energy
or the thermodynamic entropy) is augmented by
$\mathcal E_{\mathrm{SA}}=\tfrac12\rho\tilde\nu^2$. Its entropy variables
are non-zero exactly where the Navier–Stokes ones vanish, so the analysis
splits into the known Navier–Stokes part and an independent SA part. The
SA part is entropy-stable if $c_{b2}\le1$ and the SA diffusion coefficient
is non-negative. A variant of the negative-SA model with a clipped
diffusion coefficient ensures the latter. Entropy can then grow only at the
rate $\rho\tilde\nu(P_{\tilde\nu}-D_{\tilde\nu})$, where production exceeds
destruction.

In the discrete scheme, the Navier–Stokes split forms extend to the SA
equation by multiplying the two-point momentum by the arithmetic mean
$\{\!\{\tilde\nu\}\!\}$. This covers Pirozzoli's
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
flux and Chandrashekar's
[entropy-conserving](/properties/entropy-conservation.md) flux. The
product satisfies Tadmor's condition for the SA entropy with any momentum
average. The scheme adds an upwind SA interface flux, BR1 viscous fluxes
and entropy-stable adiabatic walls. Entropy dissipation enters only
through the interface fluxes, which can be switched off for
entropy-conserving central runs
([numerical dissipation](/properties/numerical-dissipation.md)).
Steady states are reached by a pseudo-transient implicit Euler solver with
a finite-difference Jacobian and CFL numbers up to $10^{12}$.

Verification covers three tests. A 3-D
[manufactured solution](/methods/method-of-manufactured-solutions.md)
shows spectral convergence. A random initial state at vanishing viscosity
makes the standard DG scheme diverge, while both split forms stay stable.
The NASA TMR [flat plate](/benchmarks/turbulent-boundary-layer.md) and
[NACA 0012](/benchmarks/naca-0012-airfoil.md) cases run on the coarsest
TMR meshes and approach the fine-grid finite-volume reference as $N$
rises. The flat-plate profile is compared with the
[law of the wall](/definitions/law-of-the-wall.md). The authors
contrast their approach with the $\ln\omega$ working variable of Bassi et
al. for the [$k$-$\omega$ model](/methods/k-omega-model.md). They propose
to couple entropy-stable RANS near walls with entropy-stable LES as a
basis for [detached-eddy simulation](/methods/detached-eddy-simulation.md).

# Version read

Version of record (J. Comput. Phys. 455:110998, open access; received 13
January 2021, accepted 16 January 2022), 27 article pages, all read;
equations on pp. 4–5 and 12–19 and the figures checked visually. The file
carries the publisher-appended Corrigendum (J. Comput. Phys. 464:111369,
doi:10.1016/j.jcp.2022.111369), which only adds a missing funding
acknowledgement and corrects no technical content. Page-1 title, four
authors and DOI match the metadata above. The paper names no software. No
identity problem. Numbering on this page is that of this version.

# Key claims

1. The continuous RANS–SA system with entropy $\mathcal E=\mathcal E_{\mathrm{NS}}+\tfrac12\rho\tilde\nu^2$ satisfies the entropy law (Eq. 50), in which the time derivative of the total entropy plus its boundary flux plus $\Theta$ times the pressure work is bounded by $-\int\rho\tilde\nu(D_{\tilde\nu}-P_{\tilde\nu})\,d\boldsymbol x$ (§3.2, Eqs. 38–50). **Derived**
2. The SA contribution is dissipative provided $c_{b2}\le1$ and $\nu_{\mathrm{SA}}\ge0$; entropy can grow only where $P_{\tilde\nu}>D_{\tilde\nu}$, and "if the destruction of turbulent viscosity leads over the production, the system will be fully–stable" (§3.2, Eq. 49). **Derived**
3. For $\tilde\nu<0$ the negative-model source $(P-D)_{\mathrm{neg}}=c_{b1}(1-c_{t3})\lvert\Omega\rvert\tilde\nu+c_{w1}(\tilde\nu/d)^2\ge0$, since $c_{t3}>1$, so $\tilde\nu(D-P)_{\mathrm{neg}}\ge0$ and the source is dissipative (§2, Eq. 16; §3.2). **Derived**
4. The SA diffusion coefficient is set to $\nu_{\mathrm{SA}}=\max(\nu+f_n\tilde\nu,0)$ for $\tilde\nu<0$, a variant of the negative-SA model, "to strictly ensure positivity of the diffusion coefficient" (§2, Eqs. 16–17). **Stated** (design choice used in the proof)
5. The entropy analysis decouples: the SA entropy variables $\boldsymbol W_{\mathrm{SA}}=(-\tilde\nu^2/2,0,0,0,0,\tilde\nu)$ vanish in entries 2–5 and the Navier–Stokes ones in entry 6, so "no modification of the NSE part will be required" (§3.2, Eqs. 39–43). **Derived**
6. Any Navier–Stokes two-point flux of the general form (Eq. 68) extends to SA through the last component $\widehat{\rho U}\{\!\{\tilde\nu\}\!\}$, which satisfies Tadmor's jump condition for the SA entropy for any momentum average $\widehat{\rho U}$, using $2[\![\tilde\nu]\!]\{\!\{\tilde\nu\}\!\}=[\![\tilde\nu^2]\!]$ (§4.3, §5.1.2, Eqs. 87–89). **Proved**
7. The SA interface flux $F^{\star}_{6}=F^{\star}_{1}\{\!\{\tilde\nu\}\!\}-\tfrac12\lambda_\nu\lvert F^{\star}_{1}\rvert[\![\tilde\nu]\!]$ produces interface entropy $\tfrac12\lambda_\nu\lvert(\rho U_n)^\star\rvert[\![\tilde\nu]\!]^2\ge0$: entropy-conserving for $\lambda_\nu=0$, entropy-stable for $\lambda_\nu=1$ (§4.4, Eq. 74; §5.2.1, Eq. 107). **Proved**
8. The BR1 interior viscous boundary terms vanish, by $[\![a]\!]\{\!\{b\}\!\}+\{\!\{a\}\!\}[\![b]\!]=[\![ab]\!]$ (§5.2.1, Eq. 108). **Proved**
9. The SA viscous volume term is non-negative (§5.1.3, Eqs. 93–94). **Proved**
10. Free- and no-slip adiabatic walls built from the mirrored ghost state $(\rho,-\rho U_n,\rho V_n,\rho W_n,\rho E,-\rho\tilde\nu)$ give dissipative inviscid boundary terms and exactly vanishing viscous boundary terms (§4.5.1, §5.2.2, Eqs. 75–77, 110–115). **Proved**
11. Inflow and outflow (Riemann-invariant) boundaries "can increase and/or decrease the entropy"; no stability is claimed for them (§4.5). **Stated**
12. The semi-discrete entropy laws of the kinetic-energy-preserving scheme (Pirozzoli flux with Lax–Friedrichs, Eq. 116) and of the thermodynamic-entropy scheme (Chandrashekar flux with matrix dissipation, Eq. 118) reproduce the continuous law (Eq. 50); the entropy derivative is negative apart from the pressure-work term of the kinetic-energy scheme (§5.3). **Proved**
13. The proofs hold on 3-D unstructured meshes of curvilinear hexahedra, the metric identities being preserved discretely by Kopriva's conservative curl form (Abstract, §4.2). **Stated** (proof assumes the discrete metric identities)
14. The approach extends to any discretization with the summation-by-parts property, "may also be followed for other RANS turbulence models, or be taken as a basis for a detached eddy simulation model" coupling entropy-stable RANS near walls with entropy-stable LES (§1, §8). **Stated**
15. Manufactured solution: the standard, Pirozzoli and Chandrashekar forms all converge spectrally in $N$; the Chandrashekar form "exhibits a higher $L^2$ error and certain even-odd behavior in the density state variable" (§7.1, Figs. 3–4). **Shown**
16. Table 1, $h$-convergence exponents of the total error (standard / Pirozzoli / Chandrashekar): $N=2$: 0.72 / 0.77 / 1.42; $N=4$: 3.06 / 3.16 / 4.33; $N=6$: 4.95 / 4.59 / 5.83; $N=8$: 7.09 / 6.49 / 7.34; $N=9$: 7.77 / 8.14 / 8.60; for $\rho\tilde\nu$ at $N=9$: 5.83 / 5.21 / 7.74 (meshes of $4^3$ to $10^3$ elements, central fluxes) (§7.1). **Shown**
17. Random-state test ($\mu=\kappa_{\mathrm{th}}=10^{-8}$, $N=10$, $10^3$ elements, central fluxes): the standard DG scheme diverges, while the Chandrashekar form keeps a non-increasing thermodynamic entropy with zero entropy remainder and the Pirozzoli form a zero kinetic-energy remainder (§7.2, Figs. 5–6). **Shown**
18. Flat plate ($M=0.2$, $Re=5\times10^6$) on the coarsest TMR mesh (816 elements) with the Pirozzoli form: $C_f$, the eddy-viscosity profile and $u^+(y^+)$ at $x=0.97008$ are "in good agreement" with the FUN3D $545\times385$ reference (§7.3, Figs. 7–8). **Shown**
19. NACA 0012 ($M=0.15$, $Re_c=6\times10^6$) on the coarsest TMR $113\times33$ grid, $N=2$–6: at $N=6$, $C_L=1.0894$, $C_D=0.01250$ at $\alpha=10^\circ$ (reference 1.0909, 0.01231) and $C_L=1.5502$, $C_D=0.02144$ at $\alpha=15^\circ$ (1.5461, 0.02124); $C_D=0.00813$ for $N=2$–6 at $\alpha=0^\circ$ (0.00819) (§7.4, Table 2). **Shown**
20. The implicit steady solver "shows good convergence behavior for all the tested polynomial orders", with CFL numbers reaching about $10^{12}$ by switched evolution relaxation (§6, §7.4, Fig. 1). **Shown**
21. Kinetic energy is not a mathematical entropy in the strict sense (unbounded pressure work; it cannot bound $\rho e$), but kinetic-energy-preserving schemes are robust and cheaper for subsonic flow, while thermodynamic-entropy schemes are preferred for supersonic flow (§3.1). **Stated** (cited)
22. The Lax–Friedrichs flux is stable with the kinetic-energy-preserving scheme; Roe-type fluxes with the symmetric part replaced by the two-point flux, used elsewhere, are "not formally stable" (§4.4). **Stated**
23. A finite-difference Jacobian is preferred to hand linearization for flexibility across models and schemes; its cost is cut by mesh colouring and the quasi-compact Gauss–Lobatto BR1 stencil (§6, Fig. 2). **Stated**

# Printed slips

- **Eq. 93, p. 15:** the term introduced as "those concerning the SA model" carries the superscript NS (and a plain $J$ for $\mathcal J$), while the surrounding Eqs. 91–94 label the SA terms SA.
- **Reference code for NACA 0012:** Table 2 labels the reference "Ref. (FUN3D, 897×257)", all Fig. 10 legends "Ref. (CFL3D, 897 x 257 grid)". *(compiler check, not in the sources)* The Table 2 reference values ($C_D=0.00819$ at $0^\circ$; $C_L=1.0909$, $C_D=0.01231$ at $10^\circ$) equal the CFL3D Spalart–Allmaras values that [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) print (Tables 3–4), not their FUN3D values (0.008120; 1.0983, 0.01242): the reference is the CFL3D solution.
- **Spelling:** "Chadrashekar form" (§7.2, p. 21).
- **Name of the second configuration:** "thermodynamic entropy stable scheme" (§4.6), "thermodynamic entropy conserving schemes with the matrix dissipation numerical flux" (§5.3), "thermodynamic entropy conserving one" (Abstract); with matrix dissipation the scheme is entropy-stable.
- **Flat-plate orders:** the text and Fig. 7b describe a sequence $N=6$–10 started from the $N=6$ solution, while Fig. 8 shows $N=4$, 7, 10; the $N=4$ run is not described.
- **References:** [43] "NASA Technical Memorandum, vol. 101, 1989, 086" (the TM number split into volume and page); [41] author "I. ANSYS".

# Notation map

| Lodares et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\vec u$, $p$, $e$, $T$ (no accents) | $\langle\rho\rangle$, $\langle\boldsymbol u\rangle_\rho$, … | Favre-averaged variables printed without tilde or overbar |
| $\tau=(\mu+\mu_t)(2\mathsf S-\tfrac23\nabla\cdot\vec u\,\mathsf I_3)$ | $2(\mu+\mu_t)S^d_{ij}$ | total viscous plus Boussinesq stress; no $\tfrac23\rho k$ (one-equation model) |
| $\mathsf S$, $\mathsf W$ | $S_{ij}$, $\Omega_{ij}$ | |
| $\Omega=\sqrt{2\mathsf W:\mathsf W}$ | $\lvert\Omega\rvert$ | **collision:** $\Omega$ is also the domain |
| $\tilde\nu$, $\chi=\tilde\nu/\nu$ | $\tilde\nu$, $\chi$ | agree |
| $k$ (SA) | $\kappa$ | von Kármán constant; **collision** with the TKE |
| $\kappa$, $\kappa_t$ | $\kappa_{\mathrm{th}}$, $\kappa_{\mathrm{th},t}$ (page-local) | heat conductivities; **collision** with the von Kármán constant |
| $P$, $D$ | $P_{\tilde\nu}$, $D_{\tilde\nu}$ (page-local) | SA production and destruction; not $P_k$ |
| $\hat\sigma$ | $\nu_{\mathrm{SA}}$ (page-local) | $\nu+\tilde\nu$ or $\max(\nu+f_n\tilde\nu,0)$; **collision:** hat is the test filter |
| $\sigma$, $c_{b1}$, $c_{b2}$, $c_{w1}$, $c_{t3}$, $c_{n1}$, $f_{t2}=0$ | same | only $\sigma=2/3$, $c_{b2}=0.622$ printed |
| $\mathcal E$, $\mathbf w$, $\mathcal E^{SA}=\tfrac12\rho\tilde\nu^2$, $\mathbf w^{SA}$ | $\mathcal E$, $W$ (page-local), $\mathcal E_{\mathrm{SA}}$, $\boldsymbol W_{\mathrm{SA}}$ (registry §11) | mathematical entropy and entropy variables; SA part in subscript form (see [entropy conservation](/properties/entropy-conservation.md)) |
| $\mathcal K$, $\mathcal S=-\rho s/(\gamma-1)$ | (kinetic energy, thermodynamic entropy) | page-local |
| $\Theta$, $\mathcal W_p$ | (0 thermodynamic entropy, 1 kinetic energy; pressure work) | page-local |
| $\langle\cdot\rangle$, $\langle\cdot,\cdot\rangle$ | $\int(\cdot)\,d\boldsymbol x$, $L^2$ inner product | **collision:** not a Reynolds average |
| $\{\{\cdot\}\}$, $[\![\cdot]\!]$, $\rho^{\ln}$ | $\{\!\{\cdot\}\!\}$, $[\![\cdot]\!]$, $\phi^{\ln}$ (registry §11) | jump right minus left |
| $\mathbf F^\#$, $\mathbf F^\star$ | $f^{\#}$, $f^*$ | two-point volume flux, interface flux |
| $N$, $\mathcal J$ | $N$, $\mathcal J$ | agree |
| $\lambda^{LxF}$, $\lambda^{MD}$, $\lambda_\nu$ | (0/1 switches of Lax–Friedrichs, matrix dissipation, SA upwinding) | page-local |
| CFL growth factor $k$ | (page-local) | **collision** with the TKE and the SA $k$ |
| $M$, $Re$ | $M$, $Re$ ($Re_c$ for the airfoil) | the flat-plate reference length is not printed |

# Reference list

68 printed references, numbered. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [54]
(Flad & Gassner 2017) is the ingested [flad-2017](/sources/flad-2017.md);
ref. [1] (Wang et al. 2013, "High-order CFD methods") is the same work as
the ingested source [Wang et al. (2013)](/sources/wang-2013.md). Ref. [37] is the arXiv preprint of the
ingested [mateogabin-2022](/sources/mateogabin-2022.md) and stays a
distinct preprint entry. Ref. [38] is the NASA Turbulence Modeling
Resource web site (printed 2020). Same-author same-year works take
suffixes in printed order (Kompenhans 2016, [7], [8]; Manzanero 2020,
[9], [21], [22], [24]; Bassi 2014, [33], [35]; Fisher 2013, [12], [57]).
Incomplete items: [9], [22], [36] print an article number but no volume;
[55], [66], [68] print no venue; [62] only a DOI; [43] and [41] are
malformed (Printed slips). No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Method of manufactured solutions](/methods/method-of-manufactured-solutions.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
