---
type: Source
title: "Stone et al. (2026) — AthenaK: A Performance-portable Version of the Athena++ Adaptive Mesh Refinement Framework"
description: "Describes AthenaK, a Kokkos reimplementation of the Athena++ block-based AMR framework with finite-volume Newtonian, relativistic and radiation MHD solvers (PLM, PPM and WENO-Z reconstruction, HLL-family and Roe fluxes, constrained transport, first-order flux correction), verified on standard tests and benchmarked on CPUs and GPUs up to 65,536 GPU dies."
resource: "doi:10.3847/1538-4365/ae3717"
source_kind: paper
authors: [Stone J.M., Mullen P.D., Fielding D., Grete P., Guo M., Kempski P., Most E.R., White C.J., Wong G.N.]
year: 2026
venue: "Astrophys. J. Suppl. Ser. 283:27"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_The_Astrophysical_Journal_Supplement_Series_Stone_ttAthenaKtt_A_Performance-portable_Vers.pdf"
tags: [software, gpu, amr, mhd, finite-volume, relativistic]
timestamp: 2026-10-24T05:59:00Z
---

# Summary

Stone et al. (2026) describe [AthenaK](/software/athenak.md), a from-scratch
reimplementation of the block-based [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
framework and fluid solvers of Athena++ in the Kokkos performance-portability model,
so that one source runs on CPUs and on NVIDIA, AMD and ARM hardware. The AMR design
is inherited (octree of MeshBlocks, Z-ordering, communication between levels only at
boundaries, flux correction at level boundaries, one time step for all levels,
task lists). New are MeshBlockPacks, which put all MeshBlocks of a device in one
structure processed by one kernel launch, device-resident data, run-time physics
selection, templated Riemann solvers to limit register spill, and Cartesian-only
coordinates. The authors relate it to [IDEFIX](/software/idefix.md), the Kokkos
version of [PLUTO](/software/pluto.md) ([Lesur et al. (2023)](/sources/lesur-2023.md)).

The numerics are recalled, not new: finite-volume reconstruct–solve–advance schemes
with PLM, the [piecewise parabolic method](/methods/piecewise-parabolic-method.md)
with the Colella–Woodward limiters ("PPM4") or the extremum-preserving limiters of
McCorquodale et al. ("PPMX"), and [WENO-Z](/methods/weno-z.md), always on primitive
variables ([characteristic reconstruction](/methods/characteristic-decomposition.md)
is not implemented); [Lax–Friedrichs](/methods/lax-friedrichs-flux.md),
[HLLE, HLLC, HLLD](/methods/hll-riemann-solvers.md) and
[Roe](/methods/roe-riemann-solver.md) fluxes; low-storage
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) and [IMEX](/methods/imex-runge-kutta.md)
integrators; [constrained transport](/methods/constrained-transport.md); and a
first-order flux correction that recomputes the face fluxes of a cell with
piecewise-constant states and the Lax–Friedrichs flux when density or pressure would
turn negative, an a posteriori fallback in the spirit of
[MOOD](/methods/mood-a-posteriori-limiting.md). Physics: Newtonian hydrodynamics and
MHD with explicit diffusion, two-fluid ion–neutral MHD, special and general
[relativistic](/definitions/relativistic-hydrodynamics.md) hydrodynamics and MHD,
gray radiation transport and particles.

Verification uses [linear waves](/benchmarks/linear-acoustics-tests.md) (fourth order
with PPMX and WENO-Z, second order with PLM and PPM4, but second order for the fast
MHD wave), [Shu–Osher](/benchmarks/shu-osher-problem.md),
[Brio–Wu](/benchmarks/brio-wu-shock-tube.md), relativistic
[blast waves and cylindrical explosions](/benchmarks/mhd-blast-wave.md), and a
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) tracer test. The
largest run is driven MHD [turbulence](/benchmarks/compressible-isotropic-turbulence.md)
on $10{,}240^3$ cells on 65,536 GPU dies. Performance reaches 1077 million cell
updates per second for 3D hydrodynamics on one Grace Hopper, AMR costs about 20% per
cell update on an A100, and weak scaling exceeds 97% on 2048 A100s.

# Version read

Version of record, Astrophys. J. Suppl. Ser. 283:27 (25 pp.), 2026 March, CC BY 4.0,
25 pages, all read (text layer plus page images of pp. 3–13 and 15–16). Page 1 matches
the Crossref record: title, the nine authors in the printed order, venue and DOI.
The Crossref title carries `<tt>` markup around the code names, which is typesetting,
not title text; the fifth author, printed "Minghao Guo (郭明浩)", is recorded as
Guo M. Received 2024 September 24, published 2026 February 26. Label in this bundle:
Stone et al. (2026).

# Key claims

Registry notation: conserved state $u$ (source $\boldsymbol U$), flux $f$ (source
$\boldsymbol F$), velocity $v$, pressure $p$ (source $p_g$), magnetic field $B$,
electric field $\mathcal E$ (source $\boldsymbol E$), Lorentz factor $W$ (source
$\Gamma$), relativistic enthalpy $w_{\mathrm h}$ (source $w$), resistivity
$\eta_{\mathrm m}$ (source $\eta$), maximum signal speed $a$ (source $\lambda_{\max}$),
CFL number $\nu$. Page-local: $u_{\mathrm{prim}}$ the primitive vector (source
$\boldsymbol W$), $\alpha_{\mathrm{in}}$ the ion–neutral drag coefficient (source
$\alpha$), $N_{\mathrm{dim}}$ the number of dimensions.

1. AthenaK reimplements the Athena++ block-based AMR framework in Kokkos; little of the design changed, the implementation is new (§2). **Stated**
2. MeshBlockPacks reduce kernel launches and "greatly enhance performance when there are a large number of small MeshBlocks on the same device" (§2). **Stated**
3. Few temporaries per kernel and templated algorithmic options such as Riemann solvers reduce register spill and "can greatly improve performance" (§2). **Stated**
4. Devices with at least 80 GB store and integrate up to $512^3$ cells each (§2). **Stated**
5. Only uniform Cartesian coordinates are supported, the authors arguing that coordinate effects are at truncation-error level; 2D axisymmetric runs are not possible (§2). **Stated**
6. Reconstruction (PLM, PPM4, PPMX, WENO-Z) always acts on primitive variables; characteristic reconstruction is not implemented, "largely because of the complexity of the implementation for general relativistic flows" (§3). **Stated**
7. $\Delta t\le\nu\min_d(\Delta x_d/a_d)$ with $\nu\le1$ and generally $\nu\le1/N_{\mathrm{dim}}$ (Eq. (3)); Colella's CTU integrator is not implemented because it does not extend easily to relativistic equations (§3). **Stated**
8. First-order flux correction: in each Runge–Kutta stage, if density or pressure in a cell would become negative, the fluxes on all its faces are recomputed with first-order reconstruction and the Lax–Friedrichs flux, before the AMR level-boundary flux correction; it fires about once in $10^{10}$ cell updates in the supersonic-turbulence application of Lemaster & Stone, yet "greatly improves the stability of calculations in extreme regimes" and reduces the need for floors (§3). **Stated**
9. Positivity loss of multidimensional higher-order finite-volume schemes at high kinetic or magnetic energy is caused by truncation error, not round-off (§3). **Stated**
10. 1D hydrodynamic linear waves: fourth-order $L_1$ convergence for PPMX and WENO-Z until nonlinearity or round-off dominates, second order for PPM4 and PLM (§3.1, Fig. 1). **Shown**
11. Shu–Osher with 200 cells: WENO-Z with RK3 resolves small scales better than PLM with RK2 (§3.1, Fig. 1). **Shown**
12. 1D MHD linear waves: fourth order with RK3 and PPMX or WENO-Z for slow and Alfvén waves, but the fast wave converges at second order "even in one dimension"; PPM4 and PLM give second order for all waves (§3.2, Fig. 3). **Shown**
13. Brio–Wu with primitive reconstruction rings slightly near the compound wave; characteristic reconstruction would reduce it (§3.2, Fig. 3). **Shown** (ringing) / **Stated** (remedy)
14. Explicit viscous fluxes with second-order differencing converge as $N_x^{-2}$ on a diffusing Gaussian (§3.3, Fig. 5). **Shown**
15. In a stiff ion–neutral drag relaxation ($\alpha_{\mathrm{in}}=6\times10^3$) the second-order Pareschi–Russo IMEX scheme overshoots with damped oscillations, the positivity-preserving scheme of Krapp et al. (2024) converges smoothly (§3.4, Fig. 7). **Shown**
16. The two-fluid module holds a steady C-shock over 10 flow times on 200 cells (§3.4, Fig. 7). **Shown**
17. With the first-order flux correction, Komissarov's relativistic MHD cylindrical explosions run robustly, where many finite-volume codes need floors, background modification or artificial viscosity (§3.5, Fig. 10). **Shown** (qualitative)
18. The Cartesian general-relativistic MHD module does not conserve angular momentum to machine precision (§3.6). **Stated**
19. General-relativistic Bondi accretion converges at second order with RK2, PLM and HLLE (§3.6, Fig. 12). **Shown**
20. Radiation linear wave: better than first-order convergence although the operator-split backward-Euler source update is first order in time, attributed to dominant advection errors (§3.7, Fig. 15). **Shown**
21. Single-device performance (PLM, RK2, HLLE, linear wave), hydrodynamics / MHD in millions of cell updates per second: Apple M1 Pro 34 / 11, Xeon Gold 6326 63 / 33, V100 298 / 158, A100 614 / 298, MI250 405 / 190, H100 677 / 290, Grace Hopper 1077 / 565 (Table 1). **Shown**
22. On an A100, MeshBlocks of $64^3$, $32^3$ and $16^3$ cells give 413, 242 and 126 million cell updates per second against 614 for $128^3$ (§5.1). **Shown**
23. On a GH200 the code reaches 8% of theoretical peak overall, single kernels up to 22% (Nsight Compute, §5.1); on an RTX 3070 Ti, 74.9 / 40.2 million cell updates per second in double precision, about 4× slower than a V100 rather than the ≈26× of the FLOP ratio, because the kernels are bandwidth-bound (§5.1). **Shown**
24. Solver costs (Table 2): relativistic and radiation solvers are slower than Newtonian hydrodynamics on every platform, MHD about 2× slower than hydrodynamics (§5.1). **Shown**
25. 2D MHD blast on one A100: uniform $4096^2$ at 181 against AMR (root $1024^2$, two levels) at 141 million cell updates per second, about 20% AMR overhead per update, identical density, AMR in 18% of the wall-clock time (§5.1, Fig. 20). **Shown**
26. Weak scaling: above 97% up to 2048 A100s (Polaris), above 90% up to 1024 GPU dies (Crusher) for GR(R)MHD, about 80% on 65,536 dies (Frontier); AMR weak scaling is nearly perfect with fixed $32^3$ MeshBlocks (§5.2, Figs. 21–22). **Shown**

# Printed slips

- Fig. 9: §3.5 calls it "a relativistic MHD blast wave test given in S20 as proposed by A. Mignone et al. (2012)", the caption "the SRMHD shock-tube test"; the panel is a 1D $B_y(x)$ profile.
- Fig. 5: §3.3 places the Gaussian profiles in the right panel and the $L_1$ errors in the left; the caption has profiles left and convergence right.
- §4.2 refers to "the $4096^3$ turbulence simulation described in Section 3.2 and Figure 4"; §3.2 and Fig. 4 describe a $10{,}240^3$ simulation.
- §2 says "2D axisymmetric calculations are not possible with AthenaK"; the Fig. 6 caption calls the MRI run "a 2D (axisymmetric) simulation".
- The text cites "H. Zhu et al. 2024" and "J. Fields et al. 2024"; the reference list has Zhu et al. 2025 (ApJS 278, 50) and Fields et al. 2025 (ApJS 276, 35).
- "Pareshi, L." for Pareschi in the text and the reference list.
- §3.2: the driving spectrum "$1\le2\pi k/L_{\rm box}\le3$, peaking at $2\pi k=2L_{\rm box}$" is dimensionally inconsistent for a wavenumber $k$ *(compiler check, not in the sources)*.
- The Kestener (2017) reference title prints "MUSCL-Handcock".

# Notation map

| Stone et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol U$, $\boldsymbol F$, $\boldsymbol S$ | $u$, $f$, $S(u)$ | $\boldsymbol S$ is also the SRMHD stress tensor of Eq. (12) |
| $\boldsymbol W$ | $u_{\mathrm{prim}}$ (local) | **collision** with the Lorentz factor $W$ |
| $\rho$, $\boldsymbol v$, $p_g$, $E$ | $\rho$, $v$, $p$, $E$ | |
| $u_g$ | $\rho e$ | internal energy per volume; **collision** with the conserved state $u$ |
| $p_m$, $p^*$ | $\tfrac12\lvert B\rvert^2$, total pressure | Heaviside–Lorentz-type units |
| $\boldsymbol E$ (electric field) | $\mathcal E$ | §10; **collision** with the total energy $E$ |
| $\Gamma$ | $W$ | Lorentz factor |
| $w$ | $w_{\mathrm h}$ | **collision** with the entropy variables $w$ |
| $D$, $\boldsymbol M$ | relativistic density and momentum (local) | **collision** of $D$ with the differentiation matrix |
| $\lambda_{\max,i}$ | $a$ in direction $d$ | |
| CFL | $\nu$ | |
| $\eta$, $\kappa$, $\nu$ | $\eta_{\mathrm m}$, thermal conductivity, viscosity (local) | **collisions** with the entropy $\eta$, kinetic energy $\kappa$, CFL number $\nu$ |
| $\alpha$ | drag $\alpha_{\mathrm{in}}$, lapse, absorptivity (local) | triple use |
| $\sigma$ | magnetization (local) | |
| $\beta$ | $\beta_{\mathrm p}$ | plasma beta |
| PLM, PPM4, PPMX, WENOZ | reconstruction options | PPM4 = Colella–Woodward limiters, not a fourth-order method |
| RK1–RK4, IMEX2, IMEX3, IMEX2+ | SSP and IMEX Runge–Kutta methods | |
| Mzcps | millions of cell updates per second | |

# Reference list

The paper prints 91 references, author–year (AAS style), journal articles without
titles. The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `stone-2026`. The two "Lesur et al. 2023" works are told apart by
venue: 2023b (A&A 677:A9, IDEFIX) is [Lesur et al. (2023)](/sources/lesur-2023.md),
and 2023a (ASP Conf. Ser. 534:465) takes its own key. "Pareshi, L." is matched to
Pareschi & Russo (J. Sci. Comput. 25:129). Several printed first-author keys name
works other than the bibliography's entries of the same key (Bai 2017, Hu 2024,
Wang 2011, Zhang 2019 (AMReX), Zhu 2025, Schneider 2015) and are kept apart by
volume and page. Prather (2024) and Visser (2007) are arXiv preprints. No item is
unparseable.

# Pages created or updated

Chunk 11 (2026-10-24). This source is cited on:

* [AthenaK](/software/athenak.md)
* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Linear acoustics tests](/benchmarks/linear-acoustics-tests.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Piecewise parabolic method (PPM)](/methods/piecewise-parabolic-method.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
