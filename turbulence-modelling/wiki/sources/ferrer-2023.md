---
type: Source
title: "Ferrer et al. (2023) — HORSES3D: A high-order discontinuous Galerkin solver for flow simulations and multi-physics applications"
description: "Reference description of HORSES3D, an open-source Fortran discontinuous Galerkin spectral element framework: split-form entropy-stable discretizations, anisotropic p-adaptation by truncation-error estimation, explicit and implicit time integration, and modules for RANS, explicit and implicit LES, multiphase flow, shock capturing, particles, aeroacoustics and immersed boundaries."
resource: "doi:10.1016/j.cpc.2023.108700"
source_kind: paper
authors: [Ferrer E., Rubio G., Ntoukas G., Laskowski W., Mariño O., Colombo S., Mateo-Gabín A., Marbona H., Manrique de Lara F., Huergo D., Manzanero J., Rueda-Ramírez A., Kopriva D., Valero E.]
year: 2023
venue: "Comput. Phys. Commun. 287:108700"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Computer_Physics_Communications_Ferrer_A_high-order_discontinuous_Galerkin_solver_for_flow_simulat.pdf"
tags: [software, dg, les, implicit-les, mesh-adaptation, entropy-stable]
timestamp: 2026-10-25T20:39:00Z
---

# Summary

Ferrer et al. (2023) describe [HORSES3D](/software/horses3d.md), the
open-source (MIT) object-oriented Fortran framework of the NUMATH group
(Universidad Politécnica de Madrid) built on the
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
on curvilinear hexahedra, with Gauss or Gauss–Lobatto nodes. It is a software
paper: no new method is derived, and most figures come from the group's
earlier papers. It enters this bundle as the reference description of a code
used for scale-resolving simulation.

The discretization offers a list of Riemann and viscous fluxes and, on
Gauss–Lobatto nodes, energy- and entropy-stable split forms
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
extended by the group to the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) equations (the
negative variant is the code's RANS model) and to Navier–Stokes/Cahn–Hilliard
flows. Anisotropic p-adaptation is driven by truncation-error
($\tau$-)estimation or by interface tracking
([mesh adaptation](/methods/mesh-adaptation.md)), with mortar coupling of
non-conforming faces. Time integration ranges from low-storage Runge–Kutta to
p-multigrid, BDF and Rosenbrock schemes. Hybrid MPI+OpenMP parallelization
reaches 86% of the ideal speed-up at 600 cores on a
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) test.

For turbulence the code provides
[large-eddy simulation](/definitions/large-eddy-simulation.md) with the
[Smagorinsky](/methods/smagorinsky-model.md), WALE and
[Vreman](/methods/vreman-model.md) models and the group's
[spectral-vanishing-viscosity](/methods/spectral-vanishing-viscosity.md)
Smagorinsky model, and [implicit LES](/definitions/implicit-les.md) through
dissipative Riemann fluxes, an enlarged interior-penalty parameter, or split
forms combined with SVV. The authors argue that DG
[numerical dissipation](/properties/numerical-dissipation.md) acts mainly on
the under-resolved high wavenumbers. Shock capturing uses an SVV-filtered
entropy-stable artificial viscosity with a density-gradient sensor, an
alternative to [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).
The other modules are an artificial-compressibility solver, Lagrangian
particles, Ffowcs Williams–Hawkings acoustics and a volume-penalization
[immersed boundary method](/methods/immersed-boundary-method.md). Table 1
compares the code with Nek5000, Nektar++, Semtex, deal.II,
[FLEXI](/software/flexi.md)/Fluxo, Trixi and PyFR. The paper defines
[DNS](/definitions/direct-numerical-simulation.md) only in passing.

# Version read

arXiv preprint 2206.09733v1 [math.NA], 20 June 2022 ("Preprint submitted to
Computer Physics Communications, June 22, 2022"), 54 pages, all read; the
program-summary fields for the CPC library link are unfilled and the
developer's repository is given as private. The metadata above are those of
the published version (Comput. Phys. Commun. 287:108700, 2023). Identity
issue: Crossref lists 14 authors, adding Marbona H. between Mateo-Gabín and
Manrique de Lara; the preprint prints 13 authors without Marbona. The title
differs only in capitalization ("a high-order"). Content of the published
version was not seen. Section, equation, figure and reference numbers on this
page are those of arXiv v1.

# Key claims

1. HORSES3D solves compressible Navier–Stokes (with or without shocks), incompressible Navier–Stokes, RANS and LES turbulence models, particle dynamics, multiphase flows and aeroacoustics in a DGSEM framework, parallelized with MPI and OpenMP and "showing good scalability for up to 1000 processors" (Abstract). **Stated**
2. Program summary: Fortran 2008, MIT licence, optional METIS, MPI, HDF5, MKL, PETSc; curvilinear conforming hexahedral meshes in GMSH, HDF5 and SpecMesh/HOHQMesh formats; §3 calls it "a Fortran 2003 object-oriented solver" (Program summary, §3.1). **Stated**
3. With an error scaling as $(\mathrm{dof})^{N}$, equal accuracy of a low- and a high-order method gives $(\mathrm{dof})_{HO}=\exp[(N_{LO}/N_{HO})\log(\mathrm{dof})_{LO}]$; for $N_{LO}=2$, $N_{HO}=5$ and $10^8$ low-order dof this is about 1.6k dof, "a factor of 60000 decrease", acknowledged as optimistic because of near-wall resolution (§1). **Derived** *(compiler check, not in the sources: $10^{3.2}\approx1585$, consistent)*
4. Aircraft aerodynamics with low-order methods typically needs "an order of 50 to 100M" dof (§1). **Stated**
5. In Table 1 (12 capabilities, eight codes) HORSES3D is the only code ticked for RANS and the only one ticked for all twelve; the authors conclude it "provides a unique set of capabilities" (§2, Table 1). **Stated**
6. Convective fluxes: central, Lax–Friedrichs, Rusanov, Roe, low-dissipation Roe, Roe–Pike, matrix dissipation; viscous fluxes: Bassi–Rebay 1 and 2, symmetric interior penalty (§3.3). **Stated**
7. Gauss–Legendre nodes are "more accurate", but Gauss–Lobatto nodes give energy- or entropy-stable schemes through the summation-by-parts property, which enhances robustness "especially in the presence of high numerical aliasing (e.g., under-resolved turbulence)" (§§3.3, 3.5). **Stated** (cites [36–38])
8. Split forms available: Morinishi, Ducros, Kennedy–Gruber, Pirozzoli, entropy-conserving, Chandrashekar (§3.5). **Stated**
9. Entropy-stable schemes have been extended by the group to the Spalart–Allmaras equations [52] and to Navier–Stokes/Cahn–Hilliard with local p-adaptation [53] (§3.5). **Stated**
10. p-adaptation is anisotropic (a separate degree $N$ in each direction of each element); p-non-conforming faces are coupled by the mortar method, "which does not retain entropy stability" (§3.6). **Stated**
11. Truncation-error ($\tau$-)estimation is the preferred adaptation sensor: it "targets the source of the discretisation error", is cheap compared with adjoint methods, and the truncation error controls all functional errors [3]; in one step it selects the lowest degree per element and direction meeting a threshold, extrapolating when none of degrees 1 to $N$ meets it (§§3.6.1–3.6.2). **Stated** (cites [3,5,56–59])
12. The truncation-error threshold "does not have any direct physical or engineering meaning", a drawback now bypassed by linking it to a flow functional [60] (§3.6.2). **Stated**
13. Multiphase adaptation refines elements containing the interface, $0.1\le c\le0.9$ for the Cahn–Hilliard phase field $c$ (§3.6.2, Fig. 2). **Stated**
14. Time integration: low-storage RK3 by default, RK4; for steady problems nonlinear p-multigrid (FAS) with explicit and semi-implicit (BIRK, LU-SGS, ILU(0)) smoothers; for unsteady ones BDF1–5 or a sixth-order Rosenbrock scheme; analytic Jacobian for Navier–Stokes, colored numerical Jacobian when e.g. Spalart–Allmaras is included (§3.7, Fig. 4). **Stated**; FAS convergence on a laminar NACA0012 ($Re_c=5000$, $M=0.5$) with explicit and BIRK smoothers for $N=2$ and $5$ (Fig. 3). **Shown**
15. Hybrid MPI+OpenMP strong scaling on a $64^3$ Taylor–Green vortex reaches "86% of the ideal performance for 600 cores and P = 6"; pure MPI scales worse than the hybrid (§3.8, Fig. 5). **Shown**
16. RANS uses the negative Spalart–Allmaras model [76,64]; the NASA Common Research Model at $M=0.85$, $Re=5\cdot10^6$, $2.3^\circ$ is computed with $N=2$ and split-form inviscid fluxes (§4.1, Fig. 6). **Shown** (pressure contours only)
17. Explicit LES models: Smagorinsky, WALE, Vreman and the SVV-Smagorinsky model [74], which "was capable of maintaining low dissipation levels for laminar flows, while providing the correct dissipation for all wave–number ranges in turbulent regimes" (§4.1). **Stated** (cites [74]); no model equations, constants or filter widths are given.
18. DG dissipation and dispersion errors are confined to high wavenumbers, so numerical dissipation acts primarily on the under-resolved scales, making DG "very suitable for ILES" (§4.1). **Stated** (cites [84,29,85–87])
19. Implicit LES options: dissipative Riemann solvers, an interior-penalty parameter above the coercivity minimum [29], and energy-stable split forms combined with SVV (§4.1). **Stated**
20. Implicit LES of the NACA0012 at $Re_c=10^6$ with 18 000 hexahedra and $N=4$ (2.2 million dof) gives lift and drag polars in "very good agreement with the experimental data" (§4.1, Fig. 7, adapted from [90]). **Shown** (experimental source not named)
21. The artificial-compressibility formulation (Eqs. 9–11) with dual time stepping avoids the inf–sup condition at the cost of a velocity that is not divergence-free (§4.2). **Stated**
22. The Navier–Stokes/Cahn–Hilliard model (Eqs. 12–14) is entropy stable and conserves phase; its p-non-conforming extension is entropy stable [53] (§4.3, Fig. 8). **Stated**
23. Shock capturing filters an artificial viscous flux (Navier–Stokes or Guermond–Popov) with an SVV kernel; entropy stability requires filtering "only one half" of the factorized flux (Eq. 18); a density-gradient sensor (Eq. 19) adds unfiltered dissipation in troubled elements; forward-facing step at $M=3$, 3653 elements, $N=7$ (§4.4, Fig. 9, from [106]). **Stated**/**Shown**
24. Lagrangian point particles with Stokes drag, gravity, radiative heating, parcels and two-way coupling; the radiated particle-laden channel does not exactly match the three-dimensional reference [108], attributed to neglected inlet preferential concentration and to parcels creating local temperature peaks (§4.5, Figs. 10–11). **Shown**
25. Ffowcs Williams–Hawkings analogy in convective form, solid or permeable surfaces, quadrupoles neglected; a stationary monopole in a moving medium ($M_0=0.5$) gives a good frequency and "relative error of around 7% for the amplitude" (§4.6, Fig. 12). **Shown**
26. NACA0012 at $Re_c=10^5$, $M=0.4$: the far-field directivity at $r=2c$ has "the expected dipole shape" (§4.6, Fig. 13). **Shown** (qualitative)
27. Volume-penalization immersed boundary (Eqs. 27–28) with a ray-traced STL mask on a KD-tree and inverse-distance surface reconstruction (Eq. 29), demonstrated on a wind turbine with rotating blades, $N=3$ near the rotor and wake and $N=2$ elsewhere (§4.7, Fig. 14). **Shown** (qualitative)
28. Test cases run in GitHub workflows on every pull request, with a monthly fuller suite across compilers and serial and parallel builds (§5.1). **Stated**
29. Future work: neural-network corrective forcing to give a low-order DG solution high-order accuracy [124,125], and a Python interface (§6). **Stated**

# Printed slips

- **Scalability.** The abstract claims "good scalability for up to 1000 processors" and §3.8 speaks of up to a thousand cores; the quantitative statement in the text is "86% of the ideal performance for 600 cores and P = 6".
- **Eq. (2)**, first row, third column: "$\rho u_3$" where the other entries use $v$ ($\rho v_3$), p. 8.
- **§3.2:** the state vector carries $\rho e$ and the text calls $e$ "total energy", but the enthalpy is printed $H=E+p/\rho$ (p. 9).
- **Language:** "Fortran 2008" (Program summary) against "a Fortran 2003 object-oriented solver" (§3).
- **Wall models:** the Program summary and §1 list LES models "including wall models"; no wall model is described in §4.1 or in its turbulence-model box.
- **Fig. 2:** the caption speaks of "the initial condition and the flow configuration at $t=2$ s", but both sub-captions read "$t = 2$" (p. 16).
- **§4.6 (p. 29):** "flow velocity fluctuations ($v_i$), surface velocities ($v_i$)", one symbol for two quantities; "$Q_i$, $L_{ij}$, $T_{ij}$ are the loading, thickness, and quadrupole terms, respectively", while Eqs. (25)–(26) build the thickness pressure from $Q_i$ and the loading pressure from $L_{ij}$; p. 30 drops the primes of $p'_T$, $p'_L$.
- **§4.2 (p. 22):** "$c_0^2$ is the artificial speed of sound".
- **References:** [16] and [40] are the same work printed twice (Gassner, Winters & Kopriva, J. Comput. Phys. 327 (2016) 39–66); [67] prints no authors; [113] prints the author pair twice; [1] prints a garbled author list ("R. Fidkowski, K.and Abgrall"); [70] "graph coloring blems"; [110] "J. E. F. Williams" for Ffowcs Williams; §3.5 "Chandrasekar" against the references' "Chandrashekar"; §4.1 "Riemman solvers".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol u=[\rho,\rho v_1,\rho v_2,\rho v_3,\rho e]^T$ | (conservative state vector) | **collision:** the registry's $\boldsymbol u$ is the velocity |
| $\vec v$ (§3), $\vec u$ (§§4.2–4.3, 4.7) | $\boldsymbol u$ | velocity |
| $e$, $E$, $H$ | (total energy and enthalpy per unit mass) | **collision:** the registry's $E$ is per unit volume; the source mixes $e$ and $E$ |
| $\boldsymbol\tau=\mu(\nabla\vec v+\nabla\vec v^T)-\frac23\mu\boldsymbol I\nabla\cdot\vec v$ | $\sigma_{ij}$ | **collision:** the registry's $\tau_{ij}$ is the SGS stress |
| $\kappa$ | (thermal conductivity) | **collision:** not the von Kármán constant |
| $P$, $P_x,P_y,P_z$, $P_{av}$ | $N$, (degree $N$ per direction, in words), (average degree) | **collision:** the registry's $N_x$ is a grid size, so the directional degrees get no symbol here |
| $J$, $\nabla_\xi$, $\vec\xi$ | (mapping Jacobian), (reference gradient), $\xi$ | |
| $\phi_j$ | (test function) | |
| $c$, $\phi$ (§3.6.2) | (Cahn–Hilliard phase field, page-local $c$) | |
| $\mu$ (§4.3), $\eta$ (§4.3) | (chemical potential), (viscosity) | **collision:** $\mu$ is the viscosity elsewhere; $\eta$ is not the Kolmogorov length |
| $M_0$ (§4.3), $M_0$ (§4.6) | (mobility), $M$ | **collision:** one symbol for a mobility and a free-stream Mach number |
| $\mathrm{Re}$, $\mathrm{Fr}$, Ma | $Re$ (chord-based, $Re_c$), (Froude number), $M$ | |
| $\mathcal F$, $\star$, $\overleftrightarrow{\mathbf F}_a$ | (SVV filter kernel, filtering, artificial flux) | **collision:** not the registry's numerically induced filter $\mathcal F_h$ |
| $S=-\rho s$, $s$, $\boldsymbol w$ | (mathematical entropy, physical entropy, entropy variables) | **collision:** $S$ is not the strain magnitude; $\boldsymbol w$ not quadrature weights |
| $s_\rho$ | (density-gradient sensor) | page-local |
| $\beta$ (§4.5) | (particles per parcel) | **collision:** not the field-inversion correction $\beta$ |
| $St$ (Fig. 11) | (Stokes number) | **collision:** the registry's $St$ is the Strouhal number |
| $T_{ij}$, $Q_i$, $L_{ij}$ | (Lighthill tensor, thickness and loading terms) | **collision:** $L_{ij}$ is not the Leonard stress, $T_{ij}$ not a temperature |
| $\chi$, $\eta$ (§4.7) | (immersed-boundary mask, permeability) | **collision:** $\chi$ is not the SA ratio $\tilde\nu/\nu$ |

# Reference list

127 printed references, numbered style ([1]–[127]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Refs. [16] and [40] are a printed duplicate and fold into one entry. Ref.
[67] prints no authors and is entered under a placeholder author. Ref. [88]
is the ingested [flad-2017](/sources/flad-2017.md). Ref. [106] (Mateo-Gabín,
Manzanero & Valero 2021, no venue) is the pre-publication form of the ingested
[mateogabin-2022](/sources/mateogabin-2022.md) and stays a separate preprint
entry. Ref. [73] prints no book title; [23] (HOHQMesh) and [126] (MFEM) are
undated software.

# Pages created or updated

Chunk 3 (2026-10-25). This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Vreman model](/methods/vreman-model.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [FLEXI](/software/flexi.md)
- [HORSES3D](/software/horses3d.md)
