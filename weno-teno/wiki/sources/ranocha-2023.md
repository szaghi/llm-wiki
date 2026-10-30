---
type: Source
title: "Ranocha et al. (2023) — Efficient Implementation of Modern Entropy Stable and Kinetic Energy Preserving Discontinuous Galerkin Methods for Conservation Laws"
description: "Implementation and single-core performance study of flux-differencing DGSEM in Trixi.jl and FLUXO: a surface-absorbing flux-differencing operator, skew-symmetry halving, directional curvilinear volume fluxes, division-reduced logarithmic means, precomputation and SIMD, with measured costs against overintegration and Gauss collocation."
resource: "doi:10.1145/3625559"
source_kind: paper
authors: [Ranocha H., Schlottke-Lakemper M., Chan J., Rueda-Ramírez A.M., Winters A.R., Hindenlang F., Gassner G.J.]
year: 2023
venue: "ACM Trans. Math. Softw. 49:1-30"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_ACM_Transactions_on_Mathematical_Software_Ranocha_Efficient_Implementation_of_Modern_Entropy_Stable_and_Kineti.pdf"
tags: [dg, entropy-stable, kinetic-energy-preserving, numerical-flux, software, performance]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper studies how to implement [flux differencing](/methods/flux-differencing.md)
efficiently for the [DGSEM](/methods/dgsem.md) on tensor-product quadrilateral and
hexahedral elements, mainly for the compressible Euler equations on one CPU core. The
volume term $\sum_jD_jf^{(j)}$ is replaced by
$\sum_j\sum_k2(D_j)_{ik}f^{\mathrm{vol},(j)}(u_i,u_k)$ with a symmetric two-point
volume flux, built on [summation-by-parts operators](/operators/summation-by-parts-operator.md).
With an [entropy-conservative flux](/methods/entropy-conservative-flux.md) in the volume
and an entropy-dissipative surface flux the scheme has
[entropy stability](/properties/entropy-stability.md). The kinetic-energy-preserving
flux of Shima et al. and Ranocha's entropy-conservative flux also give
[kinetic energy preservation](/properties/kinetic-energy-preservation.md) and
pressure-equilibrium preservation. Flux differencing is more robust than the strong
form but needs about $N+1$ times as many flux evaluations.

Each technique is measured in two open-source codes, [Trixi.jl](/software/trixi-jl.md)
(Julia) and [FLUXO](/software/fluxo.md) (Fortran). The techniques are: a
flux-differencing operator that absorbs the surface correction into the volume term;
skew-symmetry, which halves the number of two-point flux evaluations; directional
volume fluxes along averaged contravariant vectors on curvilinear meshes, which keep
the tensor-product sparsity (with the usual care for
[free-stream preservation](/properties/free-stream-preservation.md)); logarithmic-mean
algorithms with fewer divisions; precomputation of primitive variables and logarithms;
compile-time options; and explicit SIMD. Surface fluxes such as the
[local Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) and
[HLL](/methods/hll-riemann-solvers.md) are timed in microbenchmarks. A strengthened
[isentropic vortex](/benchmarks/isentropic-vortex.md) is used only for timing.

Julia and Fortran reach similar serial performance. In 3D, flux differencing is
competitive with overintegration. Entropy-stable Gauss collocation costs 1.5 to 5 times
as much as Gauss–Lobatto DGSEM. With SIMD, the cost per degree of freedom is
$2.6\times10^{-8}$ to $6.5\times10^{-8}$ s at $N=3$ in 3D. The paper proves no
theorems; all evidence comes from benchmarks. The paper also cites
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md) as related
work.

# Version read

arXiv 2112.10517v2 [cs.MS], stamped 19 Sep 2023, with the title block dated
"April 4, 2022": an author version, not the ACM typeset version of record. It has 31
pages: text on pp. 1–25, references on pp. 26–31. The arXiv file prints no DOI or
journal reference, so the published identity comes from Crossref (ACM TOMS 49(4),
1–30, 2023). Title and authors match page 1. Section, equation, table and figure
numbers are those of the arXiv v2.

# Key claims

Registry notation and the symbols of the [SBP](/operators/summation-by-parts-operator.md) and
[flux-differencing](/methods/flux-differencing.md) pages: $N$ is the DG degree, $d$ the space
dimension, $D_j$ the derivative matrix in direction $j$, $\mathcal R$ the volume-to-boundary
restriction, $B_\partial$ the boundary quadrature and $N_j$ the normal multiplication (see the
Notation map).

1. On Legendre–Gauss–Lobatto (LGL) tensor-product elements, the strong-form volume term needs $d(N+1)^d$ flux evaluations and flux differencing needs $\mathcal O(d(N+1)^{d+1})$. Without the fluxes, both need $\mathcal O(d(N+1)^{d+1})$ floating-point operations (§2, Table 1). **Derived**
2. With a diagonal mass matrix and diagonal boundary operators, the flux-differencing form (2.5) can be written in locally conservative form. It is entropy-conservative or entropy-dissipative when the volume flux is entropy-conservative and the surface flux is entropy-conservative or entropy-dissipative. For any symmetric volume flux it has the accuracy of the derivative operator (§2, after (2.5)). **Stated**
3. The operator $\widetilde D_j=2D_j-M^{-1}\mathcal R^\top B_\partial N_j\mathcal R$ (2.7) absorbs the surface term $M^{-1}\mathcal R^\top B_\partial\sum_jN_j\mathcal Rf^{(j)}$ into the volume term. This gives the form (2.10), which needs no pointwise flux evaluations at surface nodes. The cancellation uses the consistency of $f^{\mathrm{vol},(j)}$ (§2.1, (2.7)–(2.10)). **Derived**
4. $M\widetilde D_j$ is skew-symmetric (2.11), so $(\widetilde D_j)_{ii}=0$. With symmetric volume fluxes only the pairs $i<k$ need evaluating, which "saves more than half" of the volume-flux evaluations (§2.2). **Derived**
5. On curvilinear meshes, $(D_j)_{ik}=J_i^{-1}\sum_n\{\!\{Ja^{(n)}_j\}\!\}_{ik}(D_{n,\xi})_{ik}$, where $\{\!\{Ja^{(n)}_j\}\!\}_{ik}$ is the arithmetic mean of the metric term $Ja^{(n)}_j$ at nodes $i$ and $k$ (2.17). Reordering the sums (2.19) turns the volume term into one directional volume flux per reference direction $n$, along the averaged contravariant vector $\{\!\{Ja^{(n)}\}\!\}_{ik}$, which keeps the tensor-product sparsity (§2.3). **Derived**
6. A directional volume flux costs only slightly more than a Cartesian one, so the sparsity-preserving form (2.19) is preferred to the Cartesian-flux form (2.18) (§2.3, Table 2). **Shown**
7. Algorithm 2 computes a logarithmic mean $\{\!\{a\}\!\}_{\log}$ with fewer divisions. It forms $\varsigma=f_\xi^2$ directly from $a^\pm$ with one division, where $f_\xi=(\xi_a-1)/(\xi_a+1)$ and $\xi_a=a^-/a^+$, and switches to a Horner-form series when $\varsigma<10^{-4}$ (64 bit). Algorithm 3 computes the inverse logarithmic mean in the same way (§3.1). **Stated** (the series is not analysed)
8. Replacing the series term (3.5) by the multiplication form (3.6) "does not result in significant performance differences" on the hardware available (§3.1). **Shown** (no numbers)
9. Rewriting $1/\{\!\{\rho/p\}\!\}_{\log}$ as $p^+p^-/\{\!\{\rho^+p^-,\rho^-p^+\}\!\}_{\log}$ (3.11) avoids further divisions and gives "a speed-up on modern hardware" (§3.2). **Stated**
10. The directional flux of Shima et al. (3.7) preserves kinetic energy and pressure equilibrium but is not entropy-conservative. The directional Ranocha flux (3.10) is entropy-conservative, kinetic-energy preserving and pressure-equilibrium preserving (§3.2). **Stated** (the properties are cited)
11. The baseline cost per degree of freedom grows linearly in $N$, as Table 1 predicts. Trixi.jl's P4estMesh costs about as much as its StructuredMesh in 2D and about 5 % more in 3D. The Cartesian TreeMesh is up to 33 % faster with the cheap flux and up to 20 % faster with the entropy-conservative flux; in 2D the gap is about ten percentage points smaller (§4.1, Fig. 1). **Shown**
12. FLUXO (Intel Fortran 19.1.3) and Trixi.jl (Julia 1.7.0) have similar serial cost. Restricting FLUXO to AVX2 lowers its performance by up to 19 % (§4.1, Fig. 1). **Shown**
13. In flux microbenchmarks, Cartesian volume fluxes are the fastest and the directional versions are 5 % to 20 % slower. Rotated fluxes with a precomputed rotation are 10 % to 2 times slower than directional ones, and rotating on the fly costs a further 10 % to 3 times. LLF and HLL timings lie between those of the Shima and Ranocha fluxes. Recommendation: implement directional fluxes directly, not through rotations (§4.2, Table 2). **Shown** (but see Printed slips)
14. Flux differencing versus overintegration (OI), volume terms only, one element (Fig. 2). In 3D with the Shima flux, flux differencing is cheaper than any OI for $3\le N\le5$, and lies between OI with $N+1$ and $N+2$ for $5<N\le7$. With the entropy-conservative flux it lies between OI with $N+1$ and $N+2$ for $N\in\{3,4\}$, and between OI with $\lfloor3N/2\rfloor$ and $2N$ for $N>5$. In 2D it is relatively more expensive, but with cheap fluxes still faster than OI with $2N$ (§5). **Shown**
15. Flux differencing has stability guarantees that overintegration usually lacks. Where overintegration fails, flux differencing stays stable. Overintegration also increases stiffness, by "roughly … a factor of two" in the time-step restriction (§5). **Stated** (cited)
16. In 3D with $N\le3$, the most relevant case for CFD, flux differencing can be faster than overintegration with one extra node per direction (§5, §9). **Shown**
17. In entropy-stable Legendre–Gauss collocation with hybridized SBP operators and entropy projection, (6.1)–(6.3), the volume integral dominates the runtime. Flux differencing takes about 66 % ($N=3$) to 91 % ($N=15$) of the time in 2D and 65 % to 89 % in 3D; the entropy projection takes 11 % to 4 % in 2D and 14 % to 6 % in 3D (§6, Fig. 3). **Shown**
18. Entropy-conservative Gauss collocation costs 1.5 to 5 times as much as entropy-conservative LGL-DGSEM, and the gap closes with increasing order in 3D. The earlier estimate that a degree-$N$ Gauss scheme costs about as much as a degree-$(N+1)$ LGL scheme "was optimistic", because it ignored the entropy projection, the interpolation to face nodes and the lifting (§6, Fig. 4, footnote 4). **Shown**
19. Precomputing primitive variables speeds up the volume terms by about 5 % to 25 %, more in 3D than in 2D and more for cheap fluxes than for entropy-conservative ones. The memory overhead is at most about one half (Cartesian 3D) or one quarter (curved meshes), and can be reduced to one element's worth (§7.1, Fig. 5). **Shown**
20. Precomputing $\log\rho$ and $\log p$ reduces the number of logarithms from $\mathcal O(d(N+1)^{d+1})$ to $\mathcal O((N+1)^d)$. The speedup depends on the data: about 10 % for the isentropic vortex, 25 % to 55 % for sinusoidal data and 60 % to 75 % for random data. Near-constant states take the series branch, where precomputing is slightly slower (§7.2, Fig. 6). **Shown**
21. In FLUXO, fixing the volume flux at compile time gains about 5 % (inlining), and fixing $N$ as well gains up to 15 %. In Trixi.jl, inlining helps cheap fluxes and curved meshes most: up to about 2 times on curved meshes against about 25 % on TreeMesh (§7.3, Figs. 7–8). **Shown**
22. Flux-differencing volume terms have a high operational intensity, so a roofline model predicts them to be compute-bound. The measured roofline (Fig. 9) puts many SIMD points in the memory-bound region, especially for the cheap flux, because precomputation lowers the operational intensity (§8). **Shown**
23. The SIMD-optimized volume terms (AoSoA layout per element, precomputed primitives and logarithms) on an Intel Core i7-8700K (AVX2) at $N=3$ reach vectorization ratios of 98.36 % to 99.26 % and 15.25 to 21.44 GFlop/s, which is 20.69 % to 29.09 % of the FMA peak. Under SIMD, precomputing logarithms gives up to about a 2 times speedup (§8, Table 3). **Shown**
24. With SIMD, the cost per degree of freedom no longer grows linearly in $N$. In 2D it decreases roughly linearly for $N\in\{3,\dots,7\}$; in 3D it plateaus up to $N=6$ or $7$. The total speedup is 20 % to 3 times in 2D and 30 % to 3 times in 3D (§8, Figs. 10–11). **Shown**
25. Final 3D costs per degree of freedom at $N=3$ on the i7-8700K are $2.6\times10^{-8}$ s (Cartesian) and $4.3\times10^{-8}$ s (unstructured curved) for the Shima flux, and $4.2\times10^{-8}$ s and $6.5\times10^{-8}$ s for the Ranocha flux (§9). **Shown**
26. With MPI, scaling is expected to be sublinear up to a full node and close to ideal across nodes, as shown elsewhere. Non-conservative terms and MPI are left to other work (§9). **Stated**

# Printed slips

- (2.19) drops the factor $1/J_i$ that appears in (2.18), without saying that it has been factored out.
- Def. 2.4 writes the symmetry of a Cartesian flux as $f^{\mathrm{num},j}(u_1,u_2)=f^{\mathrm{num}}_j(u_2,u_1)$: the direction index moves from superscript to subscript.
- (2.12)–(2.13) write the metric components with mixed super- and subscript placement, while the text and (2.14) use $(Ja)^n_j$.
- Def. 2.4 restricts directional fluxes to unit normals $n\in S^{d-1}$, but (2.19) evaluates them at the unnormalized averaged contravariant vectors, and Algorithm 4 rescales by $\lVert\tilde n\rVert$. The scaling is linear, so the use is implied but not stated.
- §5 covers the expensive flux in 3D for "$p\in\{3,4\}$" and "$p>5$" and leaves $p=5$ out. The same section says "polynomial degree ≤ 3" where §9 says "$p=3$".
- §7.2: "computing $\log(x)+\log(y)$ takes between $11.5\pm3.8$ ns": the "between" has no second bound.
- Typos: "for the the compressible Euler equations" (Fig. 2 caption), "competetive" (§5).
- Several DOIs and URLs in the reference list are cut off at the right margin: [35], [42], [46], [50] (URL only), [55], [67], [69], and possibly [17].
- §4.2 against Table 2 *(compiler check, not in the sources)*: the text says that Cartesian fluxes are "between 5 % and 20 % more efficient" than directional ones, and that precomputed rotation is "between 10 % … and 2×" more expensive than directional. The ratios computed from the printed Table 2 timings are: directional/Cartesian 1.27 for the Shima flux in 3D (12.1/9.5 ns); 0.98 for HLL in 3D (22.9/23.3 ns), where the directional flux is faster; rotated-precomputed/directional at most 1.55 (Shima 3D, 18.7/12.1 ns). The text hedges with "usually" ("usually the most efficient", "usually between"), but the printed ranges do not match the table.

# Notation map

| Ranocha et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$ (polynomial degree) | $N$ | **collision**: the source also uses $p$ for pressure (§3), which stays $p$ |
| $c$ (number of conserved variables) | $m$ | |
| $u$, $f^j$ | $u$, $f^{(j)}$ | agree; the source's direction superscript $j$ becomes $(j)$ |
| $\varrho$, $v$, $p$, $\gamma$ | $\rho$, $v$, $p$, $\gamma$ | |
| $e$ (specific total energy), $\varrho e$ | $E/\rho$, $E$ | **collision**: registry $e$ is the specific internal energy |
| $D_j$ | $D_j$ | derivative (SBP) matrix in direction $j$; agrees with the SBP and flux-differencing pages |
| $M$ | $M$ | mass (norm) matrix, diagonal for LGL; agrees |
| $R$ (restriction to the boundary nodes) | $\mathcal R$ (local) | **collision** with the right-eigenvector matrix $R$; renamed here |
| $B$ | $B_\partial$ (local) | boundary quadrature matrix, as on the SBP page; the registry's 1D $B=\mathrm{diag}(-1,0,\dots,0,1)$ is $\mathcal R^\top B_\partial N_1\mathcal R$ for LGL |
| $N_j$ (normal multiplication) | $N_j$ (local) | kept, as on the SBP page; the direction subscript separates it from the degree $N$ |
| $\widetilde D_j$ | $\widetilde D_j$ | flux-differencing operator (2.7) |
| $f^{\mathrm{num},j}$, $f^{\mathrm{num}}(u_{\mathrm{in}},u_{\mathrm{out}},n)$ | $h(u^-,u^+)$ | surface flux; directional form along $n$ |
| $f^{\mathrm{vol},j}$ | $f^{\mathrm{vol}}$ in direction $(j)$ | symmetric two-point volume flux |
| $U$, $F^j$ | $\eta$, $F_\eta^{(j)}$ | mathematical entropy and entropy flux; entropy-dissipative means production $\le0$ |
| $w=\partial_uU$, $\psi^j$ | $w$, $\psi^{(j)}$ | agree |
| $u_-$, $u_+$; $a_-$, $a_+$ | $u^-$, $u^+$; $a^-$, $a^+$ | left and right states of a two-point flux; agree. **Collision**: registry $a$ is a wave speed; here $a$ is any argument of a mean |
| $[[a]]$, $\{\{a\}\}$, $\{\{a\}\}_{\log}$ | $[\![a]\!]$, $\{\!\{a\}\!\}$, $\{\!\{a\}\!\}_{\log}$ | agree |
| $((a;b))=(a_+b_-+a_-b_+)/2$ | — | product mean, not in the registry; used only inside (3.7), (3.10) |
| $\xi=a_-/a_+$, $f$, $u=f^2$ (Algorithms 1–3) | $\xi_a$, $f_\xi$, $\varsigma$ (local) | **collision** with the nodes $\xi_j$, the flux $f$ and the state $u$; renamed here |
| $\varepsilon=10^{-4}$ (series switch) | threshold on $\varsigma$ | not the WENO $\epsilon$ |
| $J$, $(Ja)^n_j$ | $J$, $Ja^{(n)}_j$ | Jacobian and contravariant metric terms; agree |
| $\alpha^{j,n}_{i,k}$ | $\{\!\{Ja^{(n)}_j\}\!\}_{ik}$ | the arithmetic mean it is, as on the flux-differencing page; **collision** with the blending coefficient $\alpha$ |
| $D_{n,\xi}$ | $D$ in reference direction $n$ | |
| $Q_{h,j}$, $B_{h,j}$ | — | hybridized SBP operator and boundary matrix (§6); **collision**: registry $Q=MD$ |
| $\tilde u$ | — | entropy-projected states at volume and surface points |
| $\varepsilon$ (§4.1, vortex strength 20) | vortex strength (local) | never $\epsilon$ |
| $T$ | — | final time, and temperature $p/\rho$ in (4.1) |
| PID | cost per degree of freedom | time per right-hand-side evaluation per node, not per node and variable |

# Reference list

The paper prints 77 references, numbered [1]–[77] and sorted alphabetically by first
author. The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `ranocha-2023`. Same-author same-year works take suffixes in
printed order (Chan 2019 [7]/[8], Fernández 2014 [13]/[14], Gassner 2013 [21]/[22],
Ranocha 2018 [46]/[48], Ranocha 2021 [50]–[53], [55]). The DOIs of [35], [42], [46],
[55], [67] and [69] are cut off at the margin, so no DOI is recorded for them. The URL
of [50] is cut off but its DOI is complete, and the DOI of [17] is possibly truncated.
[34], [51], [52], [58] and [62] carry no volume or pages. No item is unparseable.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–12 (2026-10-22/30). This source is cited on:

* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Entropy projection](/methods/entropy-projection.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [FLEXI](/software/flexi.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [FLUXO](/software/fluxo.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Logarithmic mean](/operators/logarithmic-mean.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Trixi.jl](/software/trixi-jl.md)
