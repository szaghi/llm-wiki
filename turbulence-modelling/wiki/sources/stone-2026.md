---
type: Source
title: "Stone et al. (2026) — AthenaK: A Performance-portable Version of the Athena++ Adaptive Mesh Refinement Framework"
description: "Describes AthenaK, a Kokkos reimplementation of the Athena++ block-based adaptive-mesh framework with Newtonian, relativistic, two-fluid and radiation MHD solvers, a first-order flux-correction positivity fallback and particle modules; verification tests, turbulence demonstration runs up to 10,240³ cells and single-GPU and weak-scaling performance to 65,536 GPUs."
resource: "doi:10.3847/1538-4365/ae3717"
source_kind: paper
authors: [Stone J.M., Mullen P.D., Fielding D., Grete P., Guo M., Kempski P., Most E.R., White C.J., Wong G.N.]
year: 2026
venue: "Astrophys. J. Suppl. Ser. 283:27"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_The_Astrophysical_Journal_Supplement_Series_Stone_ttAthenaKtt_A_Performance-portable_Vers.pdf"
tags: [gpu, mesh-adaptation, mhd, astrophysics, software]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Stone et al. (2026) describe [AthenaK](/software/athenak.md), a from-scratch
reimplementation of the block-based [adaptive mesh refinement](/methods/mesh-adaptation.md)
framework of Athena++ in the Kokkos performance-portability model. The AMR
design is kept (octree of MeshBlocks, Z-ordering, communication between levels
only at boundaries, flux correction at level boundaries, a uniform time step
across levels, task lists); the changes are the aggregation of all MeshBlocks
of a device into a MeshBlockPack so that one kernel launch covers them all,
device-resident data, boundary buffers packed in device kernels and exchanged
by point-to-point MPI, uniform Cartesian coordinates only, and run-time choice
of physics. The solvers (Newtonian hydrodynamics and MHD with explicit
diffusion, two-fluid ion–neutral MHD with IMEX drag, special- and
general-relativistic MHD, gray GR radiation, tracer and test particles) are
Godunov finite-volume schemes with PLM, PPM or WENO-Z reconstruction of
primitive variables ([WENO schemes](/methods/weno-scheme.md)), HLL-family or
Roe solvers, SSP Runge–Kutta and constrained transport, plus a first-order
flux correction: a cell whose density or pressure would turn negative has all
its face fluxes recomputed with first-order reconstruction and a local
Lax–Friedrichs solver (see
[numerical dissipation](/properties/numerical-dissipation.md)).

Turbulence appears only in demonstration runs, none analysed as a turbulence
result: driven isothermal [compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
on $10{,}240^3$ cells on 65,536 Frontier GPUs, a supernova in a turbulent
multiphase medium on $2048^3$, a 2D magnetorotational run at $Re=Rm=10^6$,
two-fluid driven turbulence on $1200^3$, and test particles in $1280^3$ MHD
turbulence, all forced in a periodic box (the setting of
[forced isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
here magnetized). The performance claims are over $10^9$ cell updates per
second for 3D hydrodynamics on one Grace Hopper processor, about 80%
weak-scaling efficiency on 65,536 GPUs (single GCDs), and an AMR blast run on one A100
with "roughly 20%" lower throughput than a uniform mesh but 18% of its wall-clock time.

# Version read

Version of record (AAS, CC BY 4.0; received 24 September 2024, revised
29 December 2025, accepted 7 January 2026, published 26 February 2026),
25 pages, all read; equations on pp. 3–5, 7–8, 10–15 checked visually.
Page 1 matches the Crossref metadata; Crossref renders the fifth author as
"Guo 郭 M.明.", page 1 prints "Minghao Guo (郭明浩)". The code is public under a
BSD-3 licence (footnote 14). Numbering is that of this version.

# Key claims

Page-local symbols: Mzcps millions of cell updates per second; $M_{\mathrm A}$
the Alfvén Mach number; $\alpha_{\mathrm d}$ the ion–neutral drag coefficient;
$\rho_{\mathrm i}$, $\rho_{\mathrm n}$, $\boldsymbol v_{\mathrm i}$,
$\boldsymbol v_{\mathrm n}$ ion and neutral densities and velocities;
$\kappa_{\mathrm{th}}$ the thermal conductivity; $N_{\mathrm{dim}}$ the number
of dimensions; $D_i$ a diffusion coefficient; $\lambda_{\max,i}$ the largest
signal speed in direction $i$.

1. AthenaK exceeds $10^9$ cell updates per second for 3D hydrodynamics on one NVIDIA Grace Hopper (1077 Mzcps hydro, 565 MHD) (Abstract, §5.1, Table 1). **Shown**
2. Weak scaling of the non-relativistic hydro and MHD solvers reaches 80% parallel efficiency on 65,536 GPUs ("single GCDs") of Frontier (Abstract, §5.2, §6). **Stated** (no figure for that run)
3. GRMHD and radiation-GRMHD weak scaling exceeds 97% on 512 Polaris nodes (2048 A100) and 90% on 128 Crusher nodes, with a drop above eight nodes attributed to "networking issues" (§5.2, Fig. 21). **Shown**
4. Packing all MeshBlocks of a device "greatly enhances performance when there are a large number of small MeshBlocks on the same device"; few temporaries and templated options (Riemann solvers) reduce register spilling (§2). **Stated**
5. Only uniform Cartesian coordinates are supported; coordinate differences are argued to be at truncation-error level, the main loss being 2D axisymmetric runs (§2). **Stated**
6. First-order flux correction: if density or pressure of any cell would become negative in an SSP-RK stage, all its face fluxes are recomputed with first-order reconstruction and a local Lax–Friedrichs solver, before the level-boundary flux correction; it acted about once per $10^{10}$ cell updates in the supersonic turbulence of Lemaster & Stone (2009), and "significantly reduces the need for floors" in GRMHD (§3). **Stated** (method) / **Shown** (Komissarov tests, Fig. 10)
7. 1D hydro linear waves converge at fourth order with PPMX and WENO-Z until nonlinear or round-off effects dominate, at second order with PPM4 and PLM (§3.1, Fig. 1). **Shown**
8. 1D MHD linear waves converge at fourth order with RK3 plus PPMX or WENO-Z for slow and Alfvén waves, while the fast wave "only converges at second order, even in one dimension" (§3.2, Fig. 3). **Shown**
9. On the Shu–Osher problem with 200 cells, WENO-Z with RK3 captures the small scales better than PLM with RK2 (§3.1, Fig. 1). **Shown**
10. Driven isothermal MHD turbulence on $10{,}240^3$ cells ($256^3$ MeshBlocks, 65,536 GPUs, WENO-Z, RK2, HLLD), solenoidal real-space driving over "$1\le2\pi k/L_{\mathrm{box}}\le3$", rms sonic Mach 0.5, mean field at $M_{\mathrm A}=2$, saturation at $\delta B/\bar B\approx3$ over four turnover times (§3.2, Fig. 4). **Shown** (demonstration)
11. A supernova blast in a turbulent, thermally unstable medium: $(32\ \mathrm{pc})^3$, $2048^3$ cells, RK3, PPM4, HLLC, flux correction, $2.4\times10^3$ GPU hours (§3.1, Fig. 2). **Shown** (demonstration)
12. Explicit viscous diffusion converges at second order, consistent with second-order differencing of the viscous stress (§3.3, Fig. 5). **Shown**
13. A 2D magnetorotational run without net flux at $8192^2$ on eight GPUs with $Re=Rm=10^6$, $Pm=1$ shows many plasmoids after 10 orbits (§3.3, Fig. 6). **Shown** (demonstration)
14. Ion–neutral drag $\boldsymbol S=\alpha_{\mathrm d}\rho_{\mathrm i}\rho_{\mathrm n}(\boldsymbol v_{\mathrm i}-\boldsymbol v_{\mathrm n})$ is integrated by IMEX; the IMEX2 of "Pareshi & Russo (2005)" (as printed) overshoots and oscillates in a stiff relaxation test, while the positivity-preserving IMEX2+ of Krapp et al. (2024) converges smoothly (§3.4, Eq. 11, Fig. 7). **Shown**
15. In two-fluid turbulence ($1200^3$, sonic Mach about 10, $M_{\mathrm A}\approx1$) the ionization fraction can fluctuate strongly (citing Hu et al. 2024), though little at the strong coupling $\alpha_{\mathrm d}=10^6$ of Fig. 8 (§3.4). **Stated** / **Shown**
16. Flux correction lets AthenaK integrate Komissarov's relativistic MHD cylindrical explosions without the flooring, background modification or artificial viscosity that other codes need (§3.5, Fig. 10). **Shown** (qualitative)
17. Bondi accretion in Cartesian Kerr–Schild coordinates converges at second order; the Blandford–Znajek monopole recovers $\Omega_{\mathrm{field}}/\Omega_H\simeq1/2$; Cartesian GRMHD does not conserve angular momentum to machine precision (§3.6, Figs. 12–13). **Shown** / **Stated**
18. Lagrangian Monte Carlo tracers follow mass better than velocity-interpolated tracers but are more diffusive than the fluid, which more particles cannot mitigate (§4.1, Fig. 18). **Stated**
19. Single-device Mzcps (hydro/MHD, linear wave, PLM, RK2, HLLE): Apple M1 Pro 34/11; Xeon Gold 6326 63/33; V100 298/158; A100 614/298; MI250 405/190; H100 677/290; Grace Hopper 1077/565 (Table 1). **Shown**
20. On an A100, MeshBlocks of $64^3$, $32^3$, $16^3$ instead of $128^3$ lower 614 Mzcps to 413, 242, 126 (§5.1). **Shown**
21. On GH200 the code runs at 8% of peak FLOPs (single kernels up to 22%); an RTX 3070 Ti reaches 74.9 (40.2) Mzcps for hydro (MHD) in double precision, about four times slower than a V100, because the kernels are bandwidth-bound (§5.1). **Shown**
22. Per-solver Mzcps on Xeon/A100/GH: hydro 63/614/1077, MHD 33/298/565, SR hydro 16/378/653, SRMHD 20/178/297, GR hydro 13/281/445, GRMHD 12/120/227, radiation GR hydro 6.2/109/211 (Table 2). **Shown**
23. A 2D MHD blast on one A100: a uniform $4096^2$ mesh runs at 181 Mzcps, AMR ($1024^2$ root, two levels) at 141 Mzcps ("roughly 20% overhead"), while needing only 18% of the wall-clock time ("5.4× faster", Fig. 20 caption) with essentially identical density (§5.1, Fig. 20). **Shown**
24. AMR weak scaling on Frontier to 4096 dies (diagonal sound wave, dynamic refinement) is super-linear when MeshBlocks grow from $16^3$ to $128^3$ and nearly perfect with fixed $32^3$ MeshBlocks, with over 5 million MeshBlocks migrated for load balance (§5.2, Fig. 22). **Shown**

The time step is $\Delta t\le\mathrm{CFL}\min_i(\Delta x_i/\lambda_{\max,i})$,
"generally" with $\mathrm{CFL}\le1/N_{\mathrm{dim}}$ (Eq. 3), and
$\Delta t\le\mathrm{CFL}_{\mathrm{diff}}\min_i(\Delta x_i^2/(2N_{\mathrm{dim}}D_i))$
for explicit diffusion (Eq. 10).

$1-141/181\approx0.22$ and $1/0.18\approx5.6$, against the printed
"roughly 20%" and "5.4× faster" *(compiler check, not in the sources)*.

# Printed slips

- **§4.2 against §3.2 and Fig. 4:** §4.2 refers to "the $4096^3$ turbulence simulation described in Section 3.2 and Figure 4"; §3.2 and the Fig. 4 caption give $10{,}240^3$.
- **Fig. 6 caption against §2:** the caption calls the MRI run "a 2D (axisymmetric) simulation"; §2 states that "2D axisymmetric calculations are not possible with AthenaK".
- **§3.3 against the Fig. 5 caption:** the text puts the diffusion profiles in the right panel and the $L_1$ errors in the left; the caption has them the other way round.
- **§3.5 against the Fig. 9 caption:** "a relativistic MHD blast wave test" in the text, "the SRMHD shock-tube test" in the caption.
- **Text against the reference list:** Zhu et al. and Fields et al. are cited as 2024 in the text and listed as 2025.
- **§3.4:** the paragraph on extending the two-fluid model to dust in protoplanetary disks is printed twice.
- **§3.4 and reference list:** the IMEX authors are printed "Pareshi, L., & Russo, G. 2005".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol U$, $\boldsymbol F$, $\boldsymbol W$, $\boldsymbol S$ | conserved variables, fluxes, primitives, sources | Eq. (1) |
| $\boldsymbol v$, $\rho$, $p_g$, $u_g$, $E$ | $\boldsymbol u$, $\rho$, $p$, internal energy, $E$ | |
| $C$ | isothermal sound speed | |
| $\boldsymbol B$, $p_m=B^2/2$ | $\boldsymbol B$ | magnetic pressure printed $B^2/2$ (no $4\pi$), unlike the registry's Gaussian $\boldsymbol b$; the C-shock set-up prints $B_y/\sqrt{4\pi}$ |
| $\boldsymbol\Pi$ (Eq. 6) | $\sigma_{ij}$ | viscous stress; **collision** with the SGS flux $\Pi$ |
| $\kappa$ | $\kappa_{\mathrm{th}}$ (page-local) | **collision** with the von Kármán $\kappa$ |
| $\eta$ | $\eta_m$ | resistivity; **collision** with the Kolmogorov length |
| $Re_M$, $Pm$ | $Rm$, $Pm$ | |
| $\mathcal M=v_{\mathrm{rms}}/c_s$, $M_s$ | $M_t$ | rms sonic Mach number |
| $M_A$ | $M_{\mathrm A}$ (page-local) | Alfvén Mach number |
| $\alpha$ (§3.4) | $\alpha_{\mathrm d}$ (page-local) | drag; the source also uses $\alpha$ for the lapse and the absorptivity |
| $\sigma$ | (magnetization; Gaussian width) | overloaded in the source |
| $N+1$ (Kokkos Views) | (array rank) | $N$ the number of dimensions, **not** the polynomial degree |
| $N_{dim}$, CFL, CFL$_{diff}$ | $N_{\mathrm{dim}}$ (page-local), CFL | |
| PLM, PPM4, PPMX, WENOZ | piecewise-linear, PPM (Colella–Woodward limiters), PPM (extremum-preserving), WENO-Z | |
| FOFC | first-order flux correction | |
| GCD | one graphics compute die | counted as one GPU ("65,536 GPUs (in this case, single GCDs)") |
| Mzcps | page-local | performance metric |

The relativistic, GR and radiation symbols of §§3.5–3.7 ($\Gamma$, $u^\mu$,
$b^\mu$, $T^\mu_\nu$, $g$, $\alpha$, $\beta^i$, $I$) have no registry entry
and are not used on the concept pages.

# Reference list

91 printed references, author–year (AAS) style, alphabetical, no DOIs, titles
printed only for books and the ASCL entry. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Guo, Kim &
Stone (2025, ApJ 990:49) and Hu et al. (2024, MNRAS 527:3945) share author-year keys with different ingested works and are keyed `guo-2025-c` and `hu-2024-b`.
Lesur et al. (2023a, 2023b) take suffixes in printed order; Prather (2024)
and Visser (2007) are arXiv preprints kept as such; the IMEX reference
is recorded with the printed spelling "Pareshi"; Zhu et al. and Fields et al.
are listed as 2025. Boris (1970) prints page 3 only; Rodriguez Bueno (2023) is
a meeting abstract. No item is unparseable.

# Pages created or updated

Chunk 16 (2026-10-29). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
- [AthenaK](/software/athenak.md)
