---
type: Source
title: "Chen et al. (2024b) — Advances and challenges in developing a stochastic model for multi-scale fluid dynamic simulation: One-dimensional turbulence"
description: "Review of Kerstein's one-dimensional turbulence model: eddy sampling and acceptance, eddy-energy models, triplet map and kernel transformation, the incompressible, Lagrangian-compressible and the authors' conservative compressible variants, and the LES-ODT and ODTLES couplings, with eight open challenges for compressible three-dimensional use."
resource: "doi:10.1016/j.cja.2024.03.001"
source_kind: paper
authors: [Chen C., Gao T., Liang J., Zhang L., Sun M.]
year: 2024
venue: "Chin. J. Aeronaut. 37(11):1–23"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Chinese_Journal_of_Aeronautics_CHEN_Advances_and_challenges_in_developing_a_stochastic_model_for.pdf"
tags: [review, les, sgs-model, compressible, wall-model]
timestamp: 2026-10-28T07:03:00Z
---

# Summary

Chen et al. (2024b) review [one-dimensional turbulence](/methods/one-dimensional-turbulence.md)
(ODT), Kerstein's stochastic multi-scale model that represents turbulence on
a line aligned with the largest mean gradient. A deterministic module
advances one-dimensional truncated equations (in the original model,
diffusion only); a stochastic module samples candidate eddies of size $l_e$ at
position $y_0$, accepts them with a probability built from an eddy rate
density and an eddy-energy model, and implements them by a measure-preserving
triplet map plus a kernel transformation that moves energy between velocity
components. Statistics are ensemble averages over independent realizations.

The review covers the incompressible formulations (scalar, vector with the
kernel transformation, variable density, buoyant with a baroclinic term,
adaptive mesh, cylindrical and spherical), the compressible Lagrangian model
of Jozefik et al. (2016), and the authors' own conservative compressible ODT,
which triplet-maps the conserved variables so that shock-capturing schemes
can be used. It reports that model's improvements, reproduced from the
authors' earlier papers, on supersonic [channel flow](/benchmarks/turbulent-channel-flow.md)
and on Richtmyer–Meshkov mixing (see [shock-generated turbulence](/results/shock-generated-turbulence.md)).
Two couplings with [LES](/definitions/large-eddy-simulation.md) are
described: LES-ODT, with ODT as a subgrid closure (finite-volume and
finite-difference frameworks, the latter with a [Smagorinsky](/methods/smagorinsky-model.md)
stress) or as a near-wall closure that acts like a
[wall model](/methods/wall-modelled-les.md); and ODTLES, three orthogonal
families of ODT lines on a coarse grid. Applications include
[mixing layers](/benchmarks/temporal-mixing-layer.md),
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) and
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-mixing.md) configurations.

The authors argue that top-down "parameterization" closures cannot carry
bottom-up transfer (see [energy backscatter](/definitions/energy-backscatter.md)),
that [hybrid RANS/LES](/definitions/hybrid-rans-les.md) trades accuracy for
cost, and class ODT, with vortex dynamics and the
[lattice Boltzmann method](/methods/lattice-boltzmann-method.md), among
Kerstein's "autonomous microstructure evolution" approaches. No ODT-based
method has yet simulated three-dimensional high-speed compressible
turbulence; a conservative compressible LES-ODT is proposed and eight
challenges are listed.

# Version read

Version of record (Elsevier, open access CC BY-NC-ND; received 27 November
2023, online 6 March 2024), 23 pages, all read, the equation pages and the
eddy-energy tables checked visually. Page 1 matches Crossref, which omits the
issue number (11). The review is written by the developers of the
conservative compressible ODT it promotes.

# Key claims

1. ODT reduces the simulation to a one-dimensional domain: a deterministic module solves truncated one-dimensional equations, a stochastic module samples, filters and implements eddy events, and averaging over $N_r$ realizations gives the mean fields; "one-dimensional" refers to the domain, not to the turbulence (§2.1, Fig. 1). **Stated**
2. Eddy acceptance probability $P_a=\lambda_e\Delta t_s/[g_1(l_e)g_2(y_0)]$, with $g_1g_2$ an assumed joint PDF of size and position whose form "will not affect the calculated results" but affects efficiency (§2.2.2, Eq. 1, citing Sutherland et al. 2010). **Stated**
3. Eddy rate density $\lambda_e=C_e/(l_e^2\tau_e)$, $C_e$ the first free parameter; $\tau_e$ follows from the eddy energy, $\tfrac12\rho l_e(l_e/\tau_e)^2\sim E_{\mathrm{kin}}+E_{\mathrm{pe}}-E_{\mathrm{visc}}$ (§2.2.2, Eqs. 2–3). **Stated**
4. Kerstein's 1999 model had $C_e=1$, a free parameter $A_e$, and $(l_e/\tau_e)^2\sim(A_e\Delta u)^2-(16\nu/l_e)^2$ (Table 1, Eq. 4). **Stated**
5. The 2001 vector formulation adds the kernel transformation (pressure scrambling), moving energy from the dominant to the other two components, with the redistribution constant $\alpha_e$ (second free parameter) and the viscous penalty $Z_e$ (third), viscous sink $Z_e\nu^2/l_e^2$ (§2.2.2, Eq. 6). **Stated**
6. The triplet map (Eq. 9) is measure-preserving, so mass, momentum and energy integrals are conserved; it compresses the profile in the eddy interval to one third, copies it three times and flips the middle copy, keeping continuity (§2.2.3, Fig. 3). **Stated**
7. The kernel transformation $u_i(y)\to u_i(\mathcal M(y))+c^K_iK_e(y)$, $K_e(y)=y-\mathcal M(y)$, acts on velocity only; scalars are only triplet-mapped (§2.2.4, Eq. 10, Fig. 4). **Stated**
8. McDermott's buoyant eddy-energy model (Eq. 8) has an empirical parameter $B$ "with a value of 2.2", with gravity components satisfying $g^2+g_c^2=(9.8)^2$ (§2.2.2). **Stated**
9. Ashurst & Kerstein (2005) simulated mixing layers with density ratios 1, 2, 4, 8 and convective Mach numbers 0.3, 0.7, 1.1; growth rates agreed at 0.3 and 0.7 with "a large discrepancy between ODT and DNS growth rates" at 1.1, which the review blames on the incompressible framework and a simple kinematic model (§2.3.4, §3.1). **Stated**
10. The compressible Lagrangian ODT of Jozefik et al. (2016) keeps a truncated convective term in non-conservative primitive-variable form; applied to shock tubes, Richtmyer–Meshkov instability and deflagration-to-detonation, it deviated significantly in mixing-zone width and turbulent kinetic energy for Richtmyer–Meshkov (§2.3.1, §3.2, Fig. 9). **Stated**
11. The conservative compressible ODT solves one-dimensional conservative equations in $(\rho,\rho u_i,E,\rho Y_\alpha)$, so shock-capturing schemes can be used; it triplet-maps the conserved variables (Eq. 18) and then applies the two-degree-of-freedom kernel transformation to the velocity (§2.3.1, §2.3.3–2.3.4, Fig. 10). **Stated**
12. That model agrees with DNS mean velocity in the viscous sublayer, buffer and log layers of supersonic channel flow (Fig. 11, from Chen et al. 2022) and predicts Richtmyer–Meshkov mixing width and kinetic energy significantly better than the Lagrangian model (Fig. 12, from Gao et al. 2023). **Shown** (figures reproduced from the authors' earlier papers)
13. Gao et al. suspected the Lagrangian model fails on Richtmyer–Meshkov through "the inability of the Lagrangian framework to incorporate the conservation governing equation and the shock capturing scheme" (§3.2). **Stated**
14. LES-ODT in finite-volume form (McDermott 2005): ODT lines in three directions cross at LES cell centres, are initialized from the resolved field, iterated within each LES step, and feed reconstructed subgrid quantities back, a bidirectional exchange (§2.4.1, Fig. 5a). **Stated**
15. LES-ODT in finite-difference form (Echekki and co-workers): three equation sets at LES nodes, ODT intersection nodes and ODT inner nodes; the LES solves continuity and momentum with a Smagorinsky subgrid stress, while ODT closes mixing and heat release (§2.4.1, Fig. 5b). **Stated**
16. ODTLES: ODT sheet grids along the three directions on a coarse three-dimensional mesh; coarse quantities are integral averages over the ODT grids, and continuity is solved at the resolved scale to stop random errors accumulating (§2.4.2, Fig. 6). **Stated**
17. ODT as a near-wall LES closure (Schmidt et al. 2003): ODT momentum flux filtered in time and space gives the subgrid stresses, LES pressure and velocity drive ODT, over an overlap region several LES cells thick; validated on channel flow at $Re_\tau$ from 395 to 10000 against DNS (§3.3, Figs. 13–16). **Stated**
18. Freire & Chamecki (2021): an ODT wall model for LES of smooth and rough channels resolves near-wall fluctuations within the first LES cell at a cost "considerably higher" than LES alone but reasonable for a fixed-grid code (§3.3). **Stated**
19. Glawe et al.: an implicit–explicit time scheme for ODTLES relaxes the CFL condition and resolves channel flow up to $Re_\tau=2040$ on one single-board computer, in strong agreement with DNS (§3.3). **Stated**
20. Gonzalez-Juez et al. (2011): ODTLES of a no-slip channel, a channel with a free-slip wall, a lid-driven cavity and a square duct agreed well with DNS (§3.3). **Stated**
21. Lignell et al. (2018): cylindrical ODT of temporal pipe flow at $Re_\tau=550$, 1000, 2000 is in "excellent agreement" with DNS; the spatial formulation was used for round jets and a jet flame (§3.1). **Stated**
22. Conventional subgrid closures ("parameterization", top-down) assume subgrid isotropy and fail near walls; hybrid RANS/LES trades accuracy for cost, with an empirical RANS–LES interface and loss of high-frequency information under Reynolds averaging (§4.1). **Stated**
23. ODT is a process-based autonomous-microstructure-evolution method like vortex dynamics, but its elements represent the statistical effect of vortices; vortex dynamics serves low-speed flows, while ODT extends to compressible and reacting flows (§4.1). **Stated**
24. No ODT-related method has yet simulated three-dimensional high-speed compressible turbulence; LES-ODT and ODTLES are limited to three-dimensional low-speed flows, and LES-ODT is more mature than ODTLES (§3, §4.2, §6). **Stated**
25. The authors propose a conservative compressible LES-ODT (a Chinese patent, ref. 72) and list eight challenges: LES-to-ODT initialization, coupling framework, efficient subgrid ODT solution, subgrid feedback, shock–eddy interaction, tying the free parameters to the local flow, curvilinear coordinates and parallelization; GPU and quantum computing are named as future efficiency "multipliers" (§5). **Stated**

The triplet map (Eq. 9), in page-local notation ($\mathcal M$ the map, $l_e$
the eddy size, $y_0$ its lower end; $y$ is the ODT-line coordinate):

$$\mathcal M(y)=y_0+\begin{cases}3(y-y_0), & y_0\le y<y_0+\tfrac13l_e,\\ 2l_e-3(y-y_0), & y_0+\tfrac13l_e\le y\le y_0+\tfrac23l_e,\\ 3(y-y_0)-2l_e, & y_0+\tfrac23l_e<y\le y_0+l_e,\\ y-y_0, & \text{otherwise}.\end{cases}$$

The two-degree-of-freedom kernel transformation (Eq. 19) is
$u_i(y)\to u_i(\mathcal M(y))+b^K_iJ_e(y)+c^K_iK_e(y)$,
$J_e=|K_e|$, the $b^K_iJ_e$ term enforcing momentum
conservation in the eddy interval for variable density.

# Printed slips

- §2.4.1 says that in LES-ODT "the traditional 'top-down' modeling strategy … is abandoned"; §3.3 writes "This 'top-down' turbulence modeling strategy, referred to as LES-ODT", contrasted with the "bottom-up" ODTLES.
- §4.2 prints "Gao$^{52,53,55,56}$ and Chen$^{54}$ et al."; ref. 52 has first author Chen, and §2.3.2 and Table 2 print "Chen$^{49,52,54}$ and Gao$^{53,55}$".
- The viscous penalty is printed as $Z$ in Eqs. 6, 7, 16, as $Z/2$ in Eqs. 14, 15, 17, and as $Z^2/2$ in Eq. 8 (the page-local $Z_e$).
- Eq. 14: substituting the printed $E^{DL}_{\mathrm{pe}}$ of Eq. 11 into its first line gives a Darrieus–Landau term with prefactor $16/(27\rho_{KK}l)$, while its second line carries $8l^2/(27\rho_{KK})$ (printed symbols, $l$ the eddy size); the two differ by the factor $l^3/2$ *(compiler check, not in the sources)*.
- The nomenclature defines $\rho_0$, $\rho_e$ and $\bar\rho$ all as "average density within eddy interval", and $\mu_e$ and $\bar\mu$ both as the average viscosity there.
- "stand-along" (§3.1, twice), "has always being" (Abstract); ref. 91 author printed "Fröhlichi".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y$ (or $x$), $l$, $y_0$ ($x_0$) | $y$, $l_e$, $y_0$ (ODT-line coordinate, eddy size, eddy lower end, page-local) | the line is not necessarily wall-normal; $x$ in the compressible formulas |
| $N$ | $N_r$ (number of realizations, page-local) | **collision** with the polynomial degree $N$ |
| $P_a$, $\Delta t_s$, $g_1$, $g_2$ | (acceptance probability, sampling interval, assumed PDFs, page-local) | |
| $\lambda(y_0,l,t)$ | $\lambda_e$ (eddy rate density, page-local) | **collision** with the Taylor microscale $\lambda$ |
| $\tau$ | $\tau_e$ (eddy time, page-local) | **collision** with $\tau_{ij}$ |
| $C$, $\alpha$, $Z$, $A$ | $C_e$, $\alpha_e$, $Z_e$, $A_e$ (ODT free parameters, page-local) | **collision:** $\alpha$ is the DG blending factor |
| $f(y)$ | $\mathcal M(y)$ (triplet map, page-local) | **collision** with $f_i$ (body force) |
| $K(y)$, $J(y)$, $b_i$, $c_i$ | $K_e(y)$, $J_e(y)$, $b^K_i$, $c^K_i$ (kernels and amplitudes, page-local) | **collision:** $K$ is the spectral TKE, $b_{ij}$ the anisotropy |
| $E_{kin}$, $E_{pe}$, $E_{visc}$, $E_{grav}$, $E_{baro}$ | (eddy-energy contributions, page-local) | **collision** with $E$ (total energy) |
| $\rho E$ | $E$ | total energy per unit volume |
| $C_s$ (Eq. 12) | $C_{\mathrm{STI}}$ (shock-energy scaling factor, page-local) | **collision** with the Smagorinsky $C_s$ |
| $Ma$, $c$, $\Delta U$ | $M$, (sound speed downstream of the shock, velocity jump, page-local) | |
| $\rho_0$, $\rho_e$, $\bar\rho$, $\mu_e$, $\bar\mu$ | (eddy-interval averages, page-local) | **collision:** the overbar is not the LES filter |
| $\rho_{KK}$, $\rho_K$ | (density-dimensioned kernel quantities, page-local, kept) | defined in the cited works |
| $\theta$ | (passive scalar, page-local) | **collision** with $\theta$ (momentum thickness) |
| $Ma_c$, $s$ | $M_c$ (convective Mach number), (density ratio, page-local) | |
| $Re_\tau$ | $Re_\tau$ | agree |

# Reference list

103 printed references, numbered style, ordered by first citation, no DOIs
printed. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` this slug. Same-author same-year works are keyed in printed
order; ref. 65 (an erratum to ref. 44) and ref. 72 (a Chinese patent) are
their own entries; references printed "[Chinese]" keep that note. Ref. 91 is
keyed `frohlich-2008` with the author spelling as printed. Ref. 7 is the
ingested [cogo-2022](/sources/cogo-2022.md); four printed keys that collide
with slugs of different works are keyed `li-2022-n` (ref. 15), `liu-2022-o` (ref. 16), `gao-2023-c` (ref. 53) and `zhang-2024-c` (ref. 2). All items
parsed.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Temporally developing mixing layer](/benchmarks/temporal-mixing-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [One-dimensional turbulence (ODT)](/methods/one-dimensional-turbulence.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
