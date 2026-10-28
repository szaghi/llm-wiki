---
type: Source
title: "Najafiyazdi et al. (2023) — Large eddy simulation on unstructured grids using explicit differential filtering: A case study of Taylor-Green vortex"
description: "Explicit elliptic differential filter extended to unstructured triangles, quadrilaterals, tetrahedra and hexahedra and designed with a generalized Z-transform (conservation, complete attenuation at the grid cut-off, element-wise stability), used in van Cittert approximate-deconvolution LES with continuous finite elements on Comte-Bellot–Corrsin decay and the Taylor–Green vortex."
resource: "doi:10.1016/j.jcp.2022.111833"
source_kind: paper
authors: [Najafiyazdi M., Mongeau L., Nadarajah S.]
year: 2023
venue: "J. Comput. Phys. 476:111833"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Computational_Physics_Najafiyazdi_Large_eddy_simulation_on_unstructured_grids_using_explicit_d.pdf"
tags: [filtering, approximate-deconvolution, les, taylor-green-vortex, unstructured-grids]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

Najafiyazdi et al. (2023) extend the explicit differential filter of
Najafi-Yazdi, Najafi-Yazdi & Mongeau (2015) from structured to
two- and three-dimensional unstructured grids (linear triangles and
tetrahedra, bilinear quadrilaterals and hexahedra) and use it as the
filter of a van Cittert approximate deconvolution model, a
[scale-similarity](/methods/scale-similarity-model.md) closure in the
fully deconvolved form of Mathew et al., without eddy viscosity or
relaxation regularization, in a continuous Galerkin finite-element
solver of the compressible Navier–Stokes equations with RK4. The filter
solves $\bar\phi+a_{\mathrm D}\partial^2_{\xi_i\xi_i}\bar\phi=\phi+b_{\mathrm D}\partial^2_{\xi_i\xi_i}\phi$
in the reference coordinates of each element, discretized into a sparse
system $\mathbf M\bar\Phi=\mathbf N\Phi$. Unlike Germano's differential
filter, whose single parameter fixes roll-off, cut-off and attenuation,
the second parameter allows complete attenuation at the grid cut-off.
A generalized Z-transform on the unstructured stencil of a node yields
element-wise conditions for conservation of constants, complete
attenuation at the grid cut-off (which fixes the nodal $b_{\mathrm D,k}$)
and a sufficient stability condition bounding $a_{\mathrm D,k}/b_{\mathrm D,k}$;
the remaining freedom sets the filter cut-off. Any differential filter on
a non-uniform grid loses commutation with differentiation, a point for
the [LES](/definitions/large-eddy-simulation.md) filtering requirements;
see also
[explicit modal filtering](/methods/explicit-modal-filtering.md).

On [Comte-Bellot–Corrsin decay](/benchmarks/homogeneous-isotropic-turbulence.md)
($64^3$ Cartesian, perturbed and tetrahedral meshes) the spectrum shows a
$-5/3$ range with complete suppression at the grid cut-off. On the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) the filtered
solver reproduces the [DNS](/definitions/direct-numerical-simulation.md)
of Brachet et al. at $Re=200$; at $Re=1600$ higher deconvolution order
gives less dissipation and a more accurate vorticity-based dissipation,
and the $64^3$ result is reported more accurate than the
[flux reconstruction](/methods/flux-reconstruction.md) and
[spectral difference](/methods/spectral-difference-method.md) LES of Bull &
Jameson at $N=1$. Grid perturbation delays and distorts the dissipation
peak and the tetrahedral mesh peaks early, read through the difference of
energy-based and vorticity-based dissipation as a measure of
[numerical dissipation](/properties/numerical-dissipation.md). The filter
and deconvolution are the only dissipation (in the sense of
[implicit LES](/definitions/implicit-les.md) comparisons); the
[Smagorinsky model](/methods/smagorinsky-model.md) is cited as not
preserving the laminar instability modes of the vortex.

# Version read

Version of record (J. Comput. Phys. 476:111833, Elsevier typeset;
received 1 Feb 2022, online 14 Dec 2022), 32 pages, all read; Table 1 was
read visually because its hexahedron rows were garbled in the text
extraction. Page-1 title, authors and DOI match the metadata. No identity
problem. Numbering on this page is that of this version.

# Key claims

The filter parameters are written $a_{\mathrm D}$, $b_{\mathrm D}$
(registry §11; the source's $\alpha$, $\beta$, nodal $\alpha_k$, $\beta_k$),
the wavenumber normalized by the grid spacing $k$, the filter and grid
cut-off wavenumbers $k_f$ and $k_c$ (the source's $\kappa_f$, $\kappa_g$),
the deconvolution order $N_{\mathrm{AD}}$, the relaxation factor $\chi_f$,
the Taylor–Green kinetic energy and enstrophy $E_{\mathrm{TG}}$ and
$\mathcal Z$ (page-local, as on the Taylor–Green page), and the energy- and
vorticity-based dissipation rates $\epsilon_E=-\mathrm dE_{\mathrm{TG}}/\mathrm dt$
and $\epsilon_\omega=2(\mu/\rho_0)\mathcal Z$.

1. The differential filter can be built on unstructured 2-D and 3-D grids by element-wise Galerkin discretization of Eq. (10) in each element's reference coordinates, giving $\mathbf M\bar\Phi=\mathbf N\Phi$ (§3.2, Eqs. 27–29). **Derived**
2. Filter parameters must be chosen after discretization: complete attenuation at $k=\pi$ requires $b_{\mathrm D}=1/4$ for a central finite-difference discretization, $1/\pi^2$ for the continuous filter and $1/12$ for a finite-element formulation (§3.1, Eq. 13). **Derived**
3. Germano's elliptic filter, transfer function $1/(1+\Delta^2k^2)$, attenuates at all wavenumbers but never removes oscillations completely; its roll-off, cut-off attenuation and cut-off wavenumber are all controlled by one parameter, so lowering the effective resolved wavenumber costs commutation error and anti-aliasing (§3, Eq. 11). **Stated**
4. The continuous Najafi-Yazdi filter has $\hat G(k)=(1-b_{\mathrm D}k^2)/(1-a_{\mathrm D}k^2)$; $b_{\mathrm D}=1/k_c^2$ gives complete attenuation at $k_c$, and for $a_{\mathrm D}<b_{\mathrm D}$ it is attenuating, $|\hat G|\le1$, for $0\le b_{\mathrm D}k^2<1$ (§3.1, Eq. 12). **Derived**
5. Any differential filter discretized on an unstructured or non-uniform grid, even in 1-D, loses commutation with differentiation because the filter width varies in space (Eq. 18); it commutes only in continuous form on uniform grids (§3.1). **Stated** (argued from Eq. 18)
6. Conservation of constants is equivalent to $n_{i,i}+\sum_{j\ne i}n_{i,j}=m_{i,i}+\sum_{j\ne i}m_{i,j}$, enforced element-wise (§4.1, Eqs. 32–34). **Derived**
7. A sufficient condition for filter stability, $|\mathcal H|\le1$, is the element-wise inequality (41), written as a stability index $I_f\ge0$ (Eq. 42); being only sufficient, it can be more dissipative than necessary (§4.5). **Derived**
8. For the bilinear quadrilateral, complete attenuation at the grid cut-off gives $b_{\mathrm D}=(1,-2/3,2,-2/3)$ ("exactly the same values as were obtained for structured grids") and $n^{(e)}_{1,j}=1/4$; stability then requires $a_{\mathrm D,2}/b_{\mathrm D,2}>1$ and $a_{\mathrm D,3}/b_{\mathrm D,3}<a_{\mathrm D,2}/b_{\mathrm D,2}$ (App. B.1, Eqs. B.15–B.18, 46; Fig. 3 compares a brute-force search with the analytic region). **Derived** and **Shown**
9. Table 1 gives the conditions for all four elements: triangle $b_{\mathrm D,k}=1/12$, tetrahedron $b_{\mathrm D,k}=3/40$, each with $a_{\mathrm D,1}/b_{\mathrm D,1}=1$ and the other ratios below 1; hexahedron $b_{\mathrm D}=(1,-7/9,4/3,-7/9,-7/9,4/3,14/9,4/3)$ with $a_{\mathrm D,2,4,5}/b_{\mathrm D,2,4,5}>1$, $a_{\mathrm D,3}/b_{\mathrm D,3}<-\tfrac34+\tfrac74a_{\mathrm D,2}/b_{\mathrm D,2}$ (likewise 6, 8) and $a_{\mathrm D,7}/b_{\mathrm D,7}<\tfrac97+4a_{\mathrm D,2}/b_{\mathrm D,2}-\tfrac{30}{7}a_{\mathrm D,3}/b_{\mathrm D,3}$ (Table 1). **Derived**
10. For linear elements complete attenuation can be obtained along $\xi$ and $\eta$ or along $\xi=\eta$, not both; bilinear and higher-order elements achieve it in all directions (App. B.2). **Stated**
11. On a 2-D Cartesian quadrilateral grid a brute-force study gave $a_{\mathrm D,2}/b_{\mathrm D,2}=1.2$, $a_{\mathrm D,3}/b_{\mathrm D,3}=1.05$, with $|k_f|\ge3\pi/4$ and $|\hat G|\ge0.9$ for $|k|\le\pi/2$ (§4.6). **Shown** (no figure)
12. For aeroacoustics $k_f\ge\pi/2$ is customary and $k_f\ge3\pi/4$ ideal (§4.6). **Stated**
13. The discrete filter is Galilean invariant and orientation-independent; "No mathematical proof will be attempted here" (§§4.3, 4.7). **Stated**
14. Repeated application of the filter equals one application with a larger radius, but the result need not belong to the same filter family (§4.8). **Stated**
15. Comte-Bellot–Corrsin decay ($Re_M=34\,000$, $N_{\mathrm{AD}}=8$, hexahedron ratios $1$, $1.2$, $1.1$, $1.05$): the spectrum reproduces turbulence below $k=8/\Delta x$ with a $-5/3$ slope and complete suppression at the grid cut-off on the $64^3$ Cartesian, 20%-perturbed and unstructured meshes; the unstructured mesh is slightly more dissipative but retains some energy beyond the structured cut-off because the filter adapts to the smaller local tetrahedra ($k_f\approx3\pi/4$ relative to the local grid size) (§6.1, Fig. 6). **Shown**
16. Taylor–Green DNS at $Re=200$ on $256^3$ and on an unstructured mesh (about 5 million nodes, 29.6 million tetrahedra), with the filter for dealiasing, is "nearly identical" to Brachet et al., with negligible $\epsilon_E/\epsilon_\omega$ and $\epsilon_E-\epsilon_\omega$ errors (§6.2, Figs. 7–8). **Shown**
17. Taylor–Green LES at $Re=1600$ on $64^3$ with $N_{\mathrm{AD}}=5$, 7, 8, 10 and $\chi_f=0.8$: the energy-based dissipation rates are almost identical up to $t^*\approx4$ (laminar structures unaffected), and for $t^*$ between 4 and 7 higher order gives less dissipation (§6.2, Fig. 10). **Shown**
18. The $64^3$ LES is more accurate in both $\epsilon_E$ and $\epsilon_\omega$ than the FR-NDG, FR-OFR and FR-SD LES of Bull & Jameson (printed "128 degrees of freedom, i.e. p1 Legendre polynomials on a $64^3$ grid") (§6.2, Fig. 10). **Shown**
19. $N_{\mathrm{AD}}=10$ remains stable but $\epsilon_E$ oscillates and slightly over-predicts the peak, while $\epsilon_\omega$ follows the DNS to $t^*\approx12$; the oscillations are attributed conjecturally to temporary energy pile-up near the grid cut-off or to aliasing below $k_f$ (§6.2). **Shown** (explanation **Stated**)
20. The vorticity-based dissipation becomes more accurate with increasing order, since higher order preserves scales near the grid cut-off (§6.2, Fig. 10b). **Shown**
21. A 10% grid perturbation has no significant effect until the dissipation peak ($t^*\approx9$) and over-estimates afterwards; 20% under-estimates before the peak, over-estimates after it and moves it from $t^*\approx9$ to 10; that grid anisotropy delays the breakdown of anisotropic vortices is "merely conjectures" (§6.2, Fig. 11). **Shown** (explanation **Stated**)
22. On the unstructured mesh the energy-based dissipation peaks earlier, $t^*\approx7.6$ ($N_{\mathrm{AD}}=8$) and 8.5 ($N_{\mathrm{AD}}=10$), with an under-estimated peak, attributed to the stronger filter on linear tetrahedra; raising the order from 8 to 10 brings the rates closer to the DNS (§6.2, Fig. 12). **Shown**
23. No energy pile-up near $k_c=32$ appears in any LES spectrum; the vorticity spectra $\Phi_{22}$ decay rapidly near the cut-off, and the perturbed grids show more high-wavenumber dissipation and less inertial-range vorticity at $t^*\approx3.2$, supporting the grid-anisotropy hypothesis (§6.2, Fig. 13). **Shown**
24. All reported DNS and LES results use the approximately deconvolved velocity $u^*=D_{N_{\mathrm{AD}}}\bar u$ (§6.2). **Stated**
25. Explicit filtering also stabilizes continuous Galerkin for incompressible flows, as shown against SUPG in the first author's thesis (§1). **Stated** (cited)

# Printed slips

- **Abstract against §6.1:** "Decaying isotropic homogeneous turbulence at a Reynolds number 3, 400" against "$Re_M=34{,}000$".
- **Eq. (B.17):** printed $12\beta_1+6\beta_2+3\beta_3+6\beta_4=8$. *(compiler check, not in the sources)* With the stated solution $\beta_1=1$, $\beta_2=\beta_4=-2/3$, $\beta_3=2$, Eq. (B.16) gives 8 but the printed (B.17) gives 10; and (B.16) minus the printed (B.17) forces $\beta_2=0$, while the text concludes $\beta_4=\beta_2$ from the pair.
- **Eq. (B.42):** $n^{(e)}_{1,6}=(32+15\beta_1+15\beta_2+3\beta_3+3\beta_4+15\beta_5+15\beta_6+3\beta_7+3\beta_8)$ is printed without the $\frac1{432}$ prefactor of its siblings (B.39, B.44). *(compiler check, not in the sources)* With the stated values (B.45) the bracket equals 54, and $54/432=1/8$ is the value of (B.46).
- **Eqs. (B.19), (B.47):** the linear triangle and tetrahedron shape functions are printed $N_1=(1-\xi)(1-\eta)$ and $N_1=(1-\xi)(1-\eta)(1-\zeta)$, with $N_2=\xi$, $N_3=\eta$ (and $N_4=\zeta$). *(compiler check, not in the sources)* These do not sum to one ($(1-\xi)(1-\eta)+\xi+\eta=1+\xi\eta$) and are not linear; the $n$ coefficients of (B.23)–(B.25) and (B.51)–(B.54) are consistent with the stated $\beta$ values.
- **§4.2, Eq. (37):** "both $|\theta_n|\le-\pi/2$ and $|\theta_m|\le-\pi/2$ hold".
- **§6.2 against Fig. 9:** "The small ripples seen in Fig. 9b suggest ... at $t^*\approx3.2$", while the caption places $t^*\approx3.2$ in panel (a) and 8.85 in (b).
- **Filter cut-off of the Taylor–Green LES:** §6.2 gives $k_f\approx\pi/2$ for the hexahedron ratios $(1.1,1.05,1.025)$ and $k_f\approx3\pi/5$ for tetrahedra; the Fig. 13 caption says "all using filter cut-off wavenumber $\kappa_f\approx0.8\pi$".
- **§6.1 against Fig. 6:** "non-dimensional time $t^*=48.3$" against "τ ≈ 48.3" in the caption; the experimental stations are $t^*=42$, 98, 171.
- **§1:** "The effectiveness of an ADM in anti-aliasing and acting as a model for the SGS contribution in the Lighthill stress tensor" ends without a verb.
- **Headings:** §4.3 and §4.7 are both titled "Galilean invariance"; §4.7 argues orientation independence.
- **References:** [23] and [63] print the same work (Stolz, Adams & Kleiser 2002) twice with different publisher strings; [1] volume "372 (2022) (2014)"; [41] "9 (N21) (2008) 1468–5248" as pages.

# Notation map

| Najafiyazdi et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u$, $\bar\phi$ | $\bar u$, $\bar\phi$ | explicit LES filter, agree |
| $\tilde u$ | $\tilde u$ | Favre filter, agree |
| $G$, $G_G$, $G_{NY}$ | $G$, $\hat G(k)$ | filter operator and transfer functions (Germano, Najafi-Yazdi) |
| $u^*$, $\phi^*_N$, $D_N$ | $u^*$, $D_{N_{\mathrm{AD}}}$ | approximately deconvolved field, as on the [scale-similarity page](/methods/scale-similarity-model.md); **collision:** the star is not the semi-local scaling |
| $N$ (ADM order) | $N_{\mathrm{AD}}$ | **collision** with the polynomial degree $N$; $N$ is also the number of stencil points in App. A |
| $\delta$ | $\delta_{\mathrm G}$ | filter radius of Germano's differential filter (registry §11), $k_f=1/\delta_{\mathrm G}$ there |
| $\beta$ (Eq. 4) | (order exponent of the deconvolution error, $\ge2(N_{\mathrm{AD}}+1)$) | unrelated to the filter $\beta$ |
| $\alpha$, $\beta$, $\alpha_k$, $\beta_k$ | $a_{\mathrm D}$, $b_{\mathrm D}$, $a_{\mathrm D,k}$, $b_{\mathrm D,k}$ | registry §11; **collision** with the DG/FV blending $\alpha$, the field-inversion $\beta(\boldsymbol x)$ and the exponential-filter strength $\alpha_f$ |
| $\xi_i$ ($\xi$, $\eta$, $\zeta$) | $\xi_i$ | reference-element coordinates; **collision:** $\eta$ is not the Kolmogorov length |
| $\mathbf M$, $\mathbf N$, $m_{pq}$, $n_{pq}$ | same | filter matrices; $\mathbf M$ is also the FEM mass matrix of Eq. 68 |
| $\mathcal H\{z_k\}$, $\hat r_{d,j}$, $I_f$ | same | generalized Z-transform transfer function, normalized offsets, stability index (page-local) |
| $\kappa$, $\kappa_f$, $\kappa_g$ | $k$, $k_f$, $k_c$ | wavenumber (spectral meaning), filter cut-off ($\lvert\mathcal H\rvert=1/2$), grid cut-off |
| $\omega$ (relaxation factor) | $\chi_f$ | 0.8; **collision** with the vorticity $\boldsymbol\omega$ |
| $\epsilon_E$, $\epsilon_\omega$, $E$, $\zeta$ | $\epsilon_E$, $\epsilon_\omega$, $E_{\mathrm{TG}}$, $\mathcal Z$ | energy- and vorticity-based dissipation rates (page-local), kinetic energy and enstrophy; $\zeta$ is not a reference coordinate here |
| $\Phi_{22}$ | (one-dimensional cross-stream vorticity spectrum) | page-local |
| $S_{i,j}$, $\Omega_{i,j}$ | $S_{ij}$, $\Omega_{ij}$ | agree |
| $\tau_{i,j}$ | $\sigma_{ij}$ | viscous stress; **collision** with the SGS stress $\tau_{ij}$ |
| $k$ (Eq. 57) | (thermal conductivity) | **collision** with the turbulent kinetic energy |
| $Re_M$, $M$, $U_0$ | $Re_M$, (grid mesh size), $U_0$ | Comte-Bellot–Corrsin grid Reynolds number; **collision:** $M$ is not the Mach number |
| $t^*$ | $t^*$ | $tU_0/M$ for decay; dimensionless time of the Taylor–Green vortex |
| $p1$ | $N=1$ | degree of the Bull & Jameson comparison |

# Reference list

79 printed references, numbered [1]–[79], all parseable. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. [23] and [63] print the same work (Stolz, Adams & Kleiser 2002)
and fold into one entry. Ref. [76] (Wang et al. 2013, Int. J. Numer.
Methods Fluids 72) is the ingested [wang-2013](/sources/wang-2013.md).
Same-author same-year works take suffixes in printed order (Stolz 1999,
two works; Germano 1986, two works). [72] (Jammy et al.) is printed
without volume or pages, with its DOI.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
