---
type: Source
title: "Witherden et al. (2025) — PyFR v2.0.3: Towards industrial adoption of scale-resolving simulations"
description: "Release description of the flux-reconstruction code PyFR v2.0.3: cross-platform backends and kernel engineering, four stabilization strategies including entropy filtering, mixed elements, conservative metrics, a synthetic-eddy plugin, supersonic Taylor–Green validation and strong scaling on Frontier and Alps."
resource: "doi:10.1016/j.cpc.2025.109567"
source_kind: paper
authors: [Witherden F.D., Vincent P.E., Trojak W., Abe Y., Akbarzadeh A., Akkurt S., Alhawwary M., Caros L., Dzanic T., Giangaspero G., Iyer A.S., Jameson A., Koch M., Loppi N., Mishra S., Modi R., Sáez-Mischlich G., Park J.S., Vermeire B.C., Wang L.]
year: 2025
venue: "Comput. Phys. Commun. 311:109567"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Computer_Physics_Communications_Witherden_PyFR_v203_Towards_industrial_adoption_of_scale-resolving_sim.pdf"
tags: [flux-reconstruction, software, gpu, high-order, shock-capturing, implicit-les]
timestamp: 2026-10-28T17:01:00Z
---

# Summary

Witherden et al. (2025) describe release 2.0.3 of
[PyFR](/software/pyfr.md), the open-source Python framework for the
high-order [flux reconstruction](/methods/flux-reconstruction.md)
approach of Huynh, aimed at scale-resolving simulation (LES, under-resolved
DNS, [DNS](/definitions/direct-numerical-simulation.md)) near complex
geometry, and list what more than 30 releases added since v0.1.0 with
industrial adoption as the aim. Performance portability: C/OpenMP, CUDA,
HIP, OpenCL and Metal backends at feature parity through a Mako-derived
kernel language; GiMMiK and libxsmm operator multiplications auto-tuned
against dense BLAS at run time; an array-of-structures-of-arrays layout;
task graphs; cache blocking; GPU-aware MPI. Stability of under-resolved
runs, which the paper equates with [implicit LES](/definitions/implicit-les.md):
[modal filtering](/methods/explicit-modal-filtering.md), quadrature-based
flux anti-aliasing, Persson–Peraire
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
and positivity-preserving entropy filtering. Geometry: prisms,
tetrahedra and affine-base pyramids with weighted and balanced
partitioning, and the curl-form conservative metric that restores
[free-stream preservation](/properties/geometric-conservation-law.md) on
curved meshes. Further: adaptive time stepping, an artificial-compressibility
incompressible solver, HDF5 files and plugins, among them a
synthetic-eddy [inflow-turbulence](/methods/inflow-turbulence-generation.md)
source term.

The supersonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $M=1.25$, $Re=1600$ ($N=3$ hexahedra, entropy filtering) matches a
$2048^3$ TENO reference in enstrophy and shows dilatational dissipation
closer to it than the
[DG](/methods/discontinuous-galerkin-spectral-element-method.md)
(with [subcell finite volumes](/methods/subcell-finite-volume-shock-capturing.md)
in [FLEXI](/software/flexi.md)) and
[spectral difference](/methods/spectral-difference-method.md) solvers of
the same comparison at equal resolution, which the authors read as low
shock-capturing [dissipation](/properties/numerical-dissipation.md)
(the [WENO/TENO](/methods/weno-scheme.md) code is the reference). A
subsonic vortex on 13.9 million tetrahedra scales from 16 to 2048 GPUs on
Frontier and Alps with efficiency 0.46 and 0.47, and per-GPU throughput
rose 49.2 times over a decade. Applications listed include
[turbine cascades](/benchmarks/turbine-cascade.md),
[channel flow](/benchmarks/turbulent-channel-flow.md), wind-turbine
[actuator-line](/methods/actuator-line-model.md) work, and other
industrial high-order codes such as [Nektar++](/software/nektar-plus-plus.md)
are named. Evidence is numerical; of the four stabilization strategies only entropy
filtering is run in the paper, the others are described with citations.

# Version read

Version of record (Elsevier, open access CC BY, section "Computer
Programs in Physics"; received 21 August 2024, accepted 25 February 2025,
online 28 February 2025), 14 pages, all read; Eq. (7) and the metric
sentence of §3.4 were checked visually. Page 1 matches the metadata (20
authors, same order). Program at the CPC Library
(doi:10.17632/vmgh4kfjk6.1), BSD 3-clause. Numbering on this page is
that of the version read.

# Key claims

Page-local symbols: $N_{\mathrm{el}}$ the number of elements; GDoF/s the
number of degrees of freedom divided by the time of one right-hand-side
evaluation, in billions.

1. PyFR v2.0.3 reaches complete feature parity across the C/OpenMP, CUDA, HIP, OpenCL and Metal backends through a Mako-derived domain-specific language (§3.1, Fig. 2). **Stated**
2. The language supports reductions (an argument annotated `reduce(op)` is reduced into memory by atomic operations), and read-only arguments likely to be reused are loaded automatically into GPU shared memory (§3.1). **Stated**
3. Products $\mathsf C\leftarrow\mathsf A\mathsf B+\beta_{\mathrm{mm}}\mathsf C$ with a constant operator $\mathsf A$ are served by GiMMiK on CUDA/HIP (unrolled kernels that skip zero entries) and libxsmm on CPUs, benchmarked against dense BLAS at run time with the fastest selected; when the flux points are a subset of the solution points the product is skipped (§3.1). **Stated**
4. The v0.1.0 structure-of-arrays layout is replaced by an array-of-structures-of-arrays packing whose stride is chosen from the hardware vector length, with a second level of blocking on CPUs (§3.1, Fig. 3). **Stated**
5. On the 2d-inc-cylinder case on an NVIDIA V100 the run time is 256 s without and 122 s with task graphs (§3.1). **Shown**
6. On HIP, task graphs are emulated by serial stream submission because "preliminary studies show their performance to be inferior to launching kernels directly"; Metal likewise; OpenCL uses out-of-order queues and events (§3.1). **Stated**
7. Cache blocking of FR "can improve performance by a factor of two" (citing [15, 16]); the solution and flux of eight $N=4$ hexahedra for the Euler equations in double precision need 160 kB (§3.1). **Stated**
8. GPU-aware MPI is supported; "in the most extreme cases, twofold performance improvements have been observed when running on clusters of NVIDIA A100 GPUs [20]" (§3.1). **Stated**
9. PyFR is often used for under-resolved DNS, "also referred to as ILES", where FR suffers aliasing-driven instabilities [21]; four stabilization strategies are offered (§3.2). **Stated**
10. Quadrature-based least-squares projection of the flux (Polyquad rules) gives results "markedly superior to those produced by modal filtering [23]", and in 3D with an anti-aliasing degree one above $N$ the run time is "typically doubled" (§3.2). **Stated**
11. Modal filtering is conservative and inexpensive but indiscriminate, with free parameters (strength, frequency, cut-off modes); artificial viscosity [24] needs parameterization and can reduce the maximum stable explicit time step (§3.2). **Stated**
12. Entropy filtering [25–28] applies a modal filter only in elements that violate positivity of density or pressure or a minimum-entropy condition (the minimum discrete entropy of the element and its Voronoi neighbours at the previous step); it "does not explicitly require any problem-dependent parameterisation", and a small fixed tolerance in the entropy constraint is not varied between problems and does not affect positivity (§3.2). **Stated**
13. Pyramids require an affine quadrilateral base; prisms and tetrahedra are fully supported (§3.3). **Stated**
14. Mixed-element partitioning cannot use one set of element weights because the relative cost depends on "around half a dozen" parameters; built-in METIS/SCOTCH (re)partitioning, MPI wait-time tracking and balanced partitioning (equal counts of each element type per domain, possibly non-contiguous) are offered (§3.3, Fig. 6). **Stated** (Fig. 6 illustrative)
15. The cross-product metric of v0.1.0 has twice the polynomial order of the shape function on curved grids, so the divergence of the discrete metric can be non-zero and free-stream preservation is lost; the conservative metric [31, 32] builds the metric terms as a curl and is divergence-free regardless of approximation error (§3.4, Fig. 7: free stream, $N=2$, cubically curved tetrahedra). **Shown** (Fig. 7, visual)
16. For linear elements the metrics are computed on the fly: an $N=4$ hexahedron has $(N+1)^3=125$ solution points and $3^2\times125=1125$ metric terms, against $3\times8=24$ vertex values (§3.4). **Stated**
17. Adaptive time stepping uses low-storage Runge–Kutta methods with embedded pairs, the normalized error estimate deciding acceptance and step size (§3.5). **Stated**
18. The incompressible solver combines artificial compressibility with dual time stepping, accelerated by polynomial multigrid and variable local time stepping (§3.6). **Stated**
19. Mesh and solution files use HDF5 with 64-bit integers ("in excess of four billion elements" per partition), embed every configuration file used, and export high-order and parallel VTU (§3.7). **Stated**
20. The turbulence-generation plugin implements the synthetic eddy method of [40, 41] as a source term with prescribed intensity and length scale; its cost scales with the number of eddies intersecting an element, not with the total injected; eddies are generated from one unsigned 32-bit seed by a device-side PCG generator (§3.8). **Stated**
21. Supersonic Taylor–Green vortex ($M=1.25$, $Re=1600$), $16^3$–$128^3$ hexahedra, $N=3$, Gauss–Lobatto points, entropy filtering: enstrophy is "in excellent agreement" with the Chapelier et al. [69] reference ($2048^3$ DoF, TENO) (§5.1, Fig. 11). **Shown**
22. PyFR "generally show[s] less shock dissipation", with $\varepsilon_d$ closer to the reference than the other element solvers of the comparison (CODA, FLEXI, SD3D) at equal resolution and order, "indicating that the entropy filtering shock capturing approach does not introduce excessive numerical dissipation" (§5.1, Fig. 12, Table 1). **Shown**
23. PyFR simulations were shortlisted for the 2016 Gordon Bell Prize, at 13.7 DP-PFLOP/s (58% of peak) on 18,000 K20X GPUs of Titan [75] (§5.2). **Stated**
24. Strong scaling, subsonic vortex ($M=0.08$, constant viscosity, $N_{\mathrm{el}}=12\times105^3=13{,}891{,}500$ tetrahedra, "seventh-order solution polynomials", $\alpha$-optimized points, double precision): Frontier (MI250X, no HIP-aware MPI) 26.21 to 1537.68 GDoF/s from 16 to 2048 ranks, efficiency 1.00 to 0.46; Alps (GH200, CUDA-aware MPI) 96.07 to 5753.96 GDoF/s, efficiency 1.00 to 0.47, superlinear (1.04–1.05) between 32 and 256 ranks (Tables 2–3). **Shown**
25. One GH200 is about 3.7 times faster than one MI250X GCD, attributed to memory bandwidth (4 TiB/s against 1.6 TiB/s per GCD, about 1.2 commonly achieved) and caches (208 KiB per SM against 16 KiB per CU; 50 MiB against 8 MiB L2) (§5.2). **Stated** *(Compiler check, not in the sources: $96.07/26.21=3.67$ from Tables 2–3.)*
26. At 2048 ranks both systems scale similarly while the NVIDIA one moves about 3.7 times more data over the same Slingshot network, "suggest[ing] that the network is not the limiting factor on Frontier"; the limitation is related to the absence of HIP-aware MPI and native HIP graphs (§5.2). **Stated**
27. Per-GPU throughput improved by a factor 49.2, from 0.122 GDoF/s per K40c (v0.2.2, fourth-order, tetrahedral-dominated mesh) to 6.004 GDoF/s per GH200 (16-rank case of Table 3), called "conservative" because seventh- against fourth-order polynomials need more FLOPs per DoF (§5.2). **Shown** *(Compiler check, not in the sources: $96.07/16=6.004$ and $6.004/0.122=49.2$.)*
28. "PyFR is now sufficiently performant and robust to be used for industrial SRS"; future work concerns training, meshing and data-processing practice and when scale-resolving simulation should complement or replace RANS (§6). **Stated**

The FR update of §2 in registry notation: on element $n$ the equations
are mapped to reference coordinates $\xi_i$ with the transformed flux
$\mathcal J\,\mathbf J^{-1}\boldsymbol f$ (Eq. 3); the solution is
interpolated to the flux points (Eq. 4), a common normal flux $f^*$ is
computed there by a Riemann solver (Eq. 5), the internal normal flux is
interpolated to the same points (Eq. 6), and the divergence at the
solution points is the divergence of the interpolated internal flux plus
the correction functions weighted by $f^*$ minus the internal normal flux
(Eq. 7). The TGV diagnostics are
$\varepsilon_s=(2\pi)^{-3}\int\mu\,\omega_i\omega_i\,\mathrm dV$ and
$\varepsilon_d=\tfrac43(2\pi)^{-3}\int\mu(\nabla\cdot\boldsymbol u)^2\,\mathrm dV$
(Eqs. 9–10), Sutherland viscosity with reference temperature 273 K.

# Printed slips

- **Eq. (7):** the correction term is printed $\big(\mathfrak F_\alpha f^{(f_\perp)}_{\sigma n\alpha}-f^{(f_\perp)}_{\sigma n\alpha}\big)$, without the tildes and the $C$ superscript of the common flux $\tilde f^{C(f_\perp)}_{\sigma n\alpha}$ defined in Eq. (5) and the text, and with the Riemann solver $\mathfrak F_\alpha$ multiplying a single flux value; the second line begins with a stray "$*$" before the "$+$".
- **Eqs. (5)–(6):** the normal is $\hat{\mathbf n}^{(f)}_{\sigma n}$ in Eq. (5), $\mathbf n^{(f)}_{\sigma n}$ in the text and Eq. (6).
- **§2, third step:** "the transformed discontinuous flux at the solution points $\tilde{\mathbf f}^{(u)}_{\sigma n\alpha}$ from the solution at solution points $\mathbf u^{(u)}_{\sigma n\alpha}$" uses the flux-point index $\sigma$ where Eq. (6) uses $\zeta$; the flux-point index is introduced with the same letter $\zeta$ as the solution-point index.
- **Eq. (2):** non-overlap is printed $\bigcap_{n=1}^N\boldsymbol\Omega_n=\emptyset$.
- **References:** [16] and [48] print the DOIs "10.52843/gpnpwx" and "10.52843/47ly7q" without the "cassyni." infix of the other Cassyni DOIs; [34] (Chorin) is printed as J. Comput. Phys. 135 (2) (1997) 118–125; [47], [48] print "L.C. Roca" and [66], [67] "Lidia Caros".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\wp$ | $N$ | solution polynomial degree; "third-order polynomials" are $N=3$ (order 4 in Table 1); "seventh-order solution polynomials" (§5.2) is not resolved between degree and order |
| $N$ | $N_{\mathrm{el}}$ (page-local) | **collision:** number of elements, not the polynomial degree |
| $\alpha$ | field-variable index | **collision** with the DG blending factor $\alpha$; "$\alpha$-optimised" points are a point set |
| $u_\alpha$, $\mathbf f_\alpha$ | conservative variables, flux | |
| $\tilde{\mathbf x}$, $\tilde\nabla$ | $\xi_i$, $\partial/\partial\xi_i$ | reference coordinates |
| $\mathcal M_n$, $\mathbf J_n$, $J_n$ | element map, Jacobian matrix, $\mathcal J$ | |
| $\mathfrak F_\alpha$, $\tilde f^{C(f_\perp)}$ | $f^*$ | interface numerical flux |
| $\mathbf g^{(f)}_\sigma$ | FR correction function of flux point $\sigma$ | |
| $\ell^{(u)}_\zeta$ | nodal Lagrange basis on the solution points | |
| $\varepsilon_s$, $\varepsilon_d$ | $\varepsilon_s$, $\varepsilon_d$ | solenoidal and dilatational dissipation, with $\mu$ |
| $\boldsymbol\omega$, $\mu$, $\mathbf u$ | $\omega_i$, $\mu$, $\boldsymbol u$ | |
| Ma, Re | $M$, $Re$ | 1.25 and 0.08; 1600 |
| $\mathsf A$, $\mathsf B$, $\mathsf C$, $\beta$ | $\mathsf A$, $\mathsf B$, $\mathsf C$, $\beta_{\mathrm{mm}}$: operator, input, output matrices; scalar | page-local, as on [PyFR](/software/pyfr.md) |
| uDNS / ILES | [implicit LES](/definitions/implicit-les.md) | the paper equates the two terms |
| GDoF/s | GDoF/s (page-local) | |

# Reference list

76 printed references, numbered style; many are PyFR Seminar Series talks
with Cassyni DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Four printed
works fall on keys of planned or ingested bundle sources that are
different works (Dzanic & Witherden 2022, J. Comput. Phys. 468:111501;
Liang 2024, a PyFR seminar; Liang & Hu 2024, Renew. Energy; Volpiani et
al. 2024, J. Aircr. 61) and are keyed `dzanic-2022-b`, `liang-2024-c`, `liang-2024-d` and `stefaninvolpiani-2024`. Three items are
bundle sources: [8] [Goc et al. (2021)](/sources/goc-2021.md), [72]
[Krais et al. (2021)](/sources/krais-2021.md) and [69]
[Chapelier et al. (2024)](/sources/chapelier-2024.md) (printed without
article number). No item is unparseable and none is printed twice.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Actuator line and actuator disk models](/methods/actuator-line-model.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [FLEXI](/software/flexi.md)
- [Nektar++](/software/nektar-plus-plus.md)
- [PyFR](/software/pyfr.md)
