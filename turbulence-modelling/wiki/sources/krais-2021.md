---
type: Source
title: "Krais et al. (2021) — FLEXI: A high order discontinuous Galerkin framework for hyperbolic–parabolic conservation laws"
description: "Describes the open-source FLEXI tool chain (HOPR mesh generator, DGSEM solver with split forms, mortars and finite-volume subcell shock capturing, POSTI post-processing), its implementation, scaling and reproducibility features, and shows implicit LES, shock–vortex and wall-modelled cavity-noise applications."
resource: "doi:10.1016/j.camwa.2020.05.004"
source_kind: paper
authors: [Krais N., Beck A., Bolemann T., Frank H., Flad D., Gassner G., Hindenlang F., Hoffmann M., Kuhn T., Sonntag M., Munz C.D.]
year: 2021
venue: "Comput. Math. Appl. 81:186-219"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Computers_amp_Mathematics_with_Applications_Krais_FLEXI_A_high_order_discontinuous_Galerkin_framework_for_hype.pdf"
tags: [software, dg, kinetic-energy-preserving, implicit-les, aeroacoustics]
timestamp: 2026-10-26T20:48:00Z
---

# Summary

Krais et al. (2021) present [FLEXI](/software/flexi.md), an open-source (GNU
GPL v3.0) high-order framework for hyperbolic–parabolic conservation laws,
aimed at scale-resolving simulation (DNS, LES) of the compressible
Navier–Stokes equations and at direct aeroacoustics. The tool chain has three
parts. HOPR generates curved high-order hexahedral meshes, ordered along a
space-filling curve in an HDF5 format. The solver is a
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
on Legendre–Gauss or Legendre–Gauss–Lobatto nodes, with explicit low-storage
Runge–Kutta time integration, MPI parallelization with latency hiding, mortar
interfaces, split forms for [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
or entropy-conserving formulations, and a hybrid
[DG/finite-volume subcell shock-capturing](/methods/subcell-finite-volume-shock-capturing.md)
scheme. POSTI is a ParaView plugin that reuses solver routines for parallel
high-order visualization.

The paper derives the DGSEM in weak and strong form on curvilinear elements,
the BR1 lifting, the $L^2$ mortar projection, the split-form volume integral
and the DG-to-FV transfer. It gives time-step restrictions with empirical
correction factors, describes the data structures and operation counts, and
reports strong scaling on a Cray XC40. Reproducibility rests on a hierarchy of
regression tests and on a "userblock", appended to every state file, that
records the parameter file, git revision, local patch and build configuration.

For turbulence modelling the paper is peripheral: it lists, without formulas
or constants, implicit LES through the discretization, explicit
[Smagorinsky](/methods/smagorinsky-model.md), $\sigma$ and [Vreman](/methods/vreman-model.md)
models, a Larsson-type [wall-stress model](/methods/equilibrium-wall-model.md)
and [Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS initialisation.
Its applications are a wall-resolved [implicit LES](/definitions/implicit-les.md)
of a NACA 64418 airfoil at $Re=10^6$ with a kinetic-energy-preserving split
form (about 117 million DOF), an inviscid shock–vortex interaction with the
hybrid DG/FV scheme, and a zonal wall-modelled LES with direct noise
computation of an open cavity, compared with experiment.

# Version read

arXiv preprint arXiv:1910.02858v1 [cs.CE], 7 October 2019 ("Preprint submitted
to Computers and Mathematics with Applications, October 8, 2019"), 57 pages.
The metadata above are those of the published version (Comput. Math. Appl.
81:186–219, 2021). Title and authors match (the preprint prints
"hyperbolic-parabolic" with a hyphen). Section, equation, figure and page
numbers on this page are those of the arXiv v1.

# Key claims

1. FLEXI is an open-source high-order tool chain (HOPR mesh generation, DGSEM solver, POSTI post-processing) released under GNU GPL v3.0 (§1, §2, Fig. 1). **Stated**
2. Simulations with over 1 billion DOF on 100,000 cores with "perfect strong scaling performance are possible" (§2.2.2). **Stated**
3. A DNS of a spatially developing supersonic turbulent boundary layer up to $Re_\theta=3878$ at $M=2.67$ used 1.458 billion DOF per variable (§2.2.2, Fig. 8, citing ref. [24]). **Stated** (a picture only)
4. The HOPR mesh is ordered along a space-filling curve, so the same mesh file can be read in parallel by any number of domains, each receiving a contiguous element range (§2.1.1, Fig. 3). **Stated**
5. Interpolating the surface displacement into the volume with radial basis functions spreads the curving distortion over the first cell layers and "dramatically" improves the scaled Jacobian at the NACA0012 leading edge (§2.1.3, Fig. 6). **Shown** (qualitative)
6. For an agglomerated serrated-nozzle mesh (20.6 million linear elements to 322,110 high-order elements, geometry degree 4), curving all elements leaves 10 invalid elements, boundary-only curving 61, one curved layer 10, and 2–4 curved layers none (§2.1.4, Table 1). **Shown**
7. Metric terms computed in curl form (Eq. 4) satisfy the metric identities discretely, which free-stream preservation requires (§3.1). **Stated** (citing Kopriva)
8. With collocated interpolation and quadrature nodes the mass matrix is diagonal. It is exact for Legendre–Gauss nodes (quadrature exact to degree $2N+1$) and a lumped approximation for Legendre–Gauss–Lobatto nodes (exact to $2N-1$) (§3.1, Eq. 15). **Derived**
9. Weak and strong DGSEM forms are analytically and discretely identical for LGL quadrature, and for LG nodes with special care for the internal fluxes (§3.1). **Stated**
10. The mortar method treats three non-conforming interface types (2:1 in either side direction, 4:1) by interpolating to the small sides and projecting the fluxes onto the big side in $L^2$ (§3.2, Eqs. 43–51). **Derived**
11. Strong-form DGSEM on LGL nodes has the diagonal-norm summation-by-parts property. Its volume integral can be rewritten with symmetric, consistent two-point fluxes $f^{\#}$ (Eq. 52), giving a split-form DG that is kinetic-energy preserving or entropy conserving depending on $f^{\#}$. Dissipative surface fluxes (e.g. Roe type) can be added (§3.3, Eqs. 52–54). **Stated/Derived**
12. In hybrid DG/FV shock capturing, a troubled element is reinterpreted as $(N+1)^d$ equispaced finite-volume subcells (same number of DOF, same data structures), advanced with a first- or second-order TVD scheme limited on primitive variables. The hybrid operator incurs "almost no additional computational cost" compared with pure DG (§2.2.3, §4.1). **Stated** (claim 21 measures 15–20%)
13. The DG-to-FV transfer is conservative, $\boldsymbol U^{FV}=V_{DG\Rightarrow FV}\boldsymbol U$, and the inverse Vandermonde matrix transfers back (§4.1, Eqs. 57–63). **Derived**
14. Troubled-cell switching uses an upper and a lower threshold instead of one, which prevents excessive back-and-forth switching and reduces the sensitivity to the user-defined value (§4.3, Fig. 16). **Stated** ("numerical studies have shown", no data)
15. Explicit time steps: $\Delta t\le\mathrm{CFL}\,c^{c}_{RK}(N)\,h/(\lambda^c(2N+1))$ (convective) and $\Delta t\le\mathrm{CFL}_d\,c^{v}_{RK}(N)\,h^2/(\lambda^v(2N+1))$ (viscous), with the factors derived from numerical experiments so that $\mathrm{CFL}\le1$ is linearly stable. For FV subcells, $\Delta t\le\mathrm{CFL}\,c^{c}_{RK}(0)\,h_{FV}/\lambda^c$ with $h_{FV}=h/(N+1)$, so the DG time step is the smaller one (§4.4, Eqs. 65–67). **Stated**
16. Operation counts per element and variable: volume fluxes $3(N+1)^3$, flux transformation $9(N+1)^3$, volume integral $3(N+1)^4$, surface fluxes $3(N+1)^2$, surface integral $6(N+1)^3$ (LG) or $6(N+1)^2$ (LGL), prolongation $6(N+1)^3$ (LG) or a $6(N+1)^2$ copy (LGL). Operations per DOF scale as $O(N)$ (§5.6, Table 3). **Derived** (estimates)
17. Measured memory per DOF (Navier–Stokes) decreases with $N$: 1.47 KiB at $N=1$, 0.74 KiB at $N=5$, 0.567 KiB at $N=12$ (Table 4). "At N = 5, we only need around 740 MB to store 1 Mio. DOFs" (§5.6). **Shown**
18. Strong scaling (Hazel Hen, Cray XC40, free stream on a Cartesian cube, $N=6$, LG nodes, 100 time steps, 5 repetitions): pure DG scales super-linearly (efficiency above 100%), which the authors attribute to cache effects, and efficiency "even for the largest cases does not drop below 70%" (§5.8, Fig. 20). **Shown**
19. The performance index of pure DG is nearly constant from about 100,000 DOF per core up to the largest loads, with an optimum near 10,000 DOF per core. Below that, latency dominates (§5.8, Fig. 20). **Shown**
20. The hybrid DG/FV operator (half the domain DG, half FV) shows weaker or no super-linear behaviour, attributed to the extra memory of the FV operator (§5.8). **Shown**
21. The performance of the hybrid DG/FV method is about 15–20% worse than that of pure DG (§5.8). **Shown**
22. NACA 64418 wall-resolved implicit LES at $Re=10^6$, $M=0.2$, angle of attack $4^\circ$: split DG with Pirozzoli's kinetic-energy-preserving flux, $N=7$ (eighth order), about 117 million DOF per variable on 229,620 elements. $C_p$ agrees excellently with XFoil except near the suction-side trailing edge, where the LES shows separation (negative $C_f$) that XFoil cannot predict (§7.1, Fig. 24). **Shown**
23. The airfoil run used 12,000 cores (9,800 DOF per core) and 47,000 CPU hours per convective time unit, with a performance index of 1.35 µs. The index is larger than in §5.8 mostly because of the extra work of the split-form volume integral (§7.1). **Shown**
24. Shock–vortex interaction ($M=1.5$ shock, Euler, $200\times100$ cells, fifth order, entropy-conserving Chandrashekar flux in DG cells, JST-type pressure indicator): the FV subcells stay in the immediate vicinity of the shock, no spurious waves are emitted, and the vortex survives past the shock because DG is used downstream (§7.2, Fig. 25). **Shown** (qualitative)
25. Cavity direct noise computation (zonal LES with anisotropic linear forcing and recycling–rescaling inflow, Kawai–Larsson wall model with the Vreman model, $N=7$, 30 million DOF, $Re_\theta=6300$, $U_\infty=42.5$ m/s): the cavity pressure spectrum agrees with experiment in peak level and width above 2 kHz and captures the first two Rossiter modes and the first quarter-wave mode below 2 kHz. The Vreman model "helps to reduce artificial pressure fluctuations caused by the wall-model" (§7.3, Fig. 27). **Shown**
26. FLEXI resolves hydrodynamic–acoustic interaction in cavity flows "which can not be captured by state-of-the-art hybrid approaches" (§7.3). **Stated**
27. LES in FLEXI uses implicitly filtered equations. Implicit closure through the discretization (choice of numerical flux) is available for well-resolved LES. Also available: explicit Smagorinsky, $\sigma$ and Vreman eddy-viscosity models, filtering for filter-based LES and VMS, a Larsson-type wall-stress model, and Spalart–Allmaras RANS initialisation by pseudo-time stepping (§2.2.3, item 3). **Stated** (no formulas or constants printed)

Two printed statements differ in magnitude. §2.2.2 claims "perfect strong scaling performance" (claim 2), while §5.8 reports efficiencies down to 70% on at most 49,152 cores (claim 18). §2.2.3 says the hybrid DG/FV operator has "almost no additional computational cost" (claim 12), while §5.8 measures it "about 15 − 20% worse" (claim 21).

# Printed slips

- **Eq. 46 (p. 24).** Printed $\underline{\boldsymbol U}^U_{:j}=I^L\cdot\underline{\boldsymbol U}^B_{:j}$ and $\underline{\boldsymbol U}^L_{:j}=I^U\cdot\underline{\boldsymbol U}^B_{:j}$. By Eqs. 43 and 45 ($I^L_{im}=\ell_m(\eta^L_i)$), the lower side uses $I^L$ and the upper side $I^U$: the superscripts are swapped.
- **Eq. 64 (p. 29).** The flux at face $i+\tfrac12,j$ is printed with arguments $(\boldsymbol U^{FV-},\boldsymbol U^{FV-},\mathcal N)$, while the other three faces carry $(\boldsymbol U^{FV-},\boldsymbol U^{FV+},\mathcal N)$.
- **§2.1.1 (p. 4).** "an arbitrary number of domains (≥ number of elements)": each domain must own at least one element, so the number of domains cannot exceed the number of elements.
- **§5.8 (p. 40).** "49.152 cores" uses a decimal point as thousands separator (49,152).
- **Typos:** "therefor" (abstract), "real word applications" (§1), "stategies" (§2.1.3), "discretly" (§3.1), "get's" (§5.6), "seemed smooth" for "deemed" (§4.3), "only thread the immediate vicinity" for "treat" (§7.2).
- **Eq. 31 (p. 21)** *(compiler check, not in the sources)*. Printed $\hat D_{ij}=-\frac{\omega_i}{\omega_j}D_{ji}$. In the weak-form volume term of Eq. 9, with test function $\ell_i$, quadrature gives $\sum_mw_m\mathcal F_mD_{mi}$. Dividing by the diagonal mass $w_i$ with the sign of Eq. 30 gives $\hat D_{im}=-\frac{w_m}{w_i}D_{mi}$, that is $\hat D_{ij}=-\frac{w_j}{w_i}D_{ji}$. The printed weight ratio is inverted. The same equation's $\hat\ell_i=\ell_i/\omega_i$ divides by $w_i$, as this derivation does.
- **Fig. 20 legend against the §5.8 text** *(compiler check, not in the sources)*. The caption says "the number of elements is given in the legend", and the legend runs from $6^3\cdot2^1$ to $6^3\cdot2^{12}$. The text gives meshes from $[6\times6\times6]=6^3\cdot2^0$ to $[96\times96\times48]=442\,368=6^3\cdot2^{11}$ elements. The text range matches 49,152 cores at 9 elements per core ($442\,368/9=49\,152$) and the minimum of 24 cores ($216/9$). Legend and text differ by one power of two.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\vec U$, $\vec F^c$, $\vec F^v$ | (conserved variables, convective and viscous fluxes) | |
| $N$ | $N$ | solution polynomial degree; "eighth order" is $N=7$ |
| $N_{geo}$ | (geometry degree) | independent of $N$ |
| $\vec\xi=(\xi^1,\xi^2,\xi^3)$ | $\xi_i$ | reference coordinates |
| $\xi_i$, $\omega_i$ | $\xi_i$, $w_i$ | quadrature nodes and weights (LG or LGL) |
| $D_{rs}$, $\hat D_{ij}$ | $D_{ij}$, (weak-form differentiation matrix) | |
| $\ell_j$ | (Lagrange polynomial) | |
| $\mathcal J$, $\mathcal J\vec a^i$ | $\mathcal J$ (registry §11), (contravariant metric terms) | Jacobian determinant of the element map |
| $\vec f^*$ | $f^*$ | interface numerical flux, convective part only |
| $\vec F^{\#,l}$, $\vec{\mathcal F}^{\#,l}$ | $f^{\#}$ | two-point volume flux (physical, contravariant) |
| $\{\!\{\cdot\}\!\}$ | $\{\!\{\phi\}\!\}$ | agrees |
| $w=2/(N+1)$ | $h_{\mathrm{sub}}$ (page-local) | subcell width in reference space; **collision:** registry $w_i$ are quadrature weights |
| $V_{DG\Rightarrow FV}$ | (DG-to-FV Vandermonde matrix) | |
| $\Delta x$, $\Delta x_{DG}$, $\Delta x_{FV}$ | $h$, $h$, $h_{FV}$ | element and subcell sizes; registry $\Delta$ is the filter width |
| $\gamma^1_{RK}$, $\gamma^2_{RK}$ | $c^{c}_{RK}$, $c^{v}_{RK}$ (page-local) | empirical time-step factors; **collision:** registry $\gamma$ is the ratio of specific heats; values not printed |
| $\lambda^c$, $\lambda^v$ | $\lambda^c$, $\lambda^v$ (page-local) | largest convective speed, largest diffusion eigenvalue; superscripted to avoid the registry $\lambda$ (Taylor microscale) |
| PID | (performance index) | wall time × cores / (DOF × time steps × RK stages), Eq. 68 |
| $Ma$ | $M$ | |
| $c_p$, $c_f$ | $C_p$, $C_f$ | |
| $Re$, $Re_\theta$ | $Re_c$, $Re_\theta$ | chord Reynolds number $U_\infty c/\nu$ |
| $x^+$, $y^+$, $z^+$ | $\Delta x^+/(N+1)$, … | wall-unit element spacings divided by $N+1$ (§7.1) |
| $T^*=c/U_\infty$ | (convective time unit) | |

The paper defines no subgrid stress, filter, Reynolds stress or eddy-viscosity
notation; LES is "implicitly filtered".

# Reference list

94 printed references in numbered style ([1]–[94]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. [28] is the ingested source [Flad & Gassner (2017)](/sources/flad-2017.md).
Refs. [12], [19] and [93] print no volume or pages; ref. [20] (HDF Group)
prints the year range 1997–2019; ref. [41] prints "The visualization handbook
717 (2005)"; ref. [36] prints the article number "15-00418" as pages; ref. [94]
prints its DOI as a URL. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2, 4, 6, 7, 8. This source is cited on:

- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Vreman model](/methods/vreman-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [FLEXI](/software/flexi.md)
