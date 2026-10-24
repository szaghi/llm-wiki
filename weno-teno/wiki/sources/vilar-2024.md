---
type: Source
title: "Vilar & Abgrall (2024) — A posteriori local subcell correction of high-order discontinuous Galerkin scheme for conservation laws on two-dimensional unstructured grids"
description: "Proves that a DG scheme on a triangle or polygon split into as many subcells as degrees of freedom is exactly a subcell finite-volume scheme with reconstructed fluxes, and uses it for an a posteriori MOOD-type correction that replaces only the fluxes of troubled subcells by first-order fluxes, with sixth-order tests on very coarse unstructured meshes."
resource: "doi:10.1137/22m1542696"
source_kind: paper
authors: [Vilar F., Abgrall R.]
year: 2024
venue: "SIAM J. Sci. Comput. 46:A851-A883"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_SIAM_Journal_on_Scientific_Computing_Vilar_A_Posteriori_Local_Subcell_Correction_of_High-Order_Disconti.pdf"
tags: [dg, limiting, bound-preserving, finite-volume]
timestamp: 2026-10-23T15:15:00Z
---

# Summary

Vilar & Abgrall (2024) extend to two-dimensional unstructured grids the *a posteriori local
subcell correction* (APLSC) that Vilar introduced in 1D. The theoretical core is an
[equivalence of DG and subcell finite volumes](/results/dg-subcell-finite-volume-equivalence.md).
A $\mathbb P^N$ [discontinuous Galerkin](/methods/discontinuous-galerkin.md) scheme on a cell
split into $N_N=(N+1)(N+2)/2$ subcells is exactly a finite-volume scheme on the subcell means.
The fluxes on the interior subcell faces are specific *reconstructed fluxes*, and the DG
numerical flux is kept on the cell boundary. The subdivision is arbitrary, triangles,
quadrilaterals or Voronoi-type polygons, provided the matrix from moments to subcell means is
invertible. Two equivalent expressions of the reconstructed fluxes are derived. One comes from
the DG residual through the generalized inverse of the subcell graph Laplacian. The other is the
interior polynomial flux minus the boundary flux jump, distributed by *sub-resolution basis
functions*.

The correction follows the [MOOD](/methods/mood-a-posteriori-limiting.md) paradigm. A DG
candidate is computed and projected to subcell means. Each subcell is tested by a physical
admissibility detector (bounds, positivity, NaN) and a numerical one: a relaxed discrete maximum
principle with a vertex-based smooth-extremum relaxation, a
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) at subcell level. Only on the
faces of troubled subcells is the reconstructed flux replaced by a first-order Lax–Friedrichs
flux. The scheme stays conservative at subcell level and keeps the DG solution in the other
subcells of the same cell, unlike the [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
schemes that recompute the whole troubled cell. The first-order fallback gives
[bound preservation](/properties/bound-preservation.md) by construction. A new variant blends
first-order and reconstructed fluxes with weights decreasing away from the troubled subcell; it
needs fewer correction iterations.

The tests are mostly sixth-order ($\mathbb P^5$) on very coarse triangular meshes of 100 to 1054
cells: linear advection, [solid-body rotation](/benchmarks/solid-body-rotation.md), 2D
[Burgers](/benchmarks/burgers-equation-tests.md), the [KPP rotating wave](/benchmarks/kpp-rotating-wave.md),
a polar [Sod tube](/benchmarks/sod-and-lax-shock-tubes.md), a [Sedov blast](/benchmarks/sedov-blast-wave.md)
with background pressure $10^{-14}$ and the Mach 3 [forward-facing step](/benchmarks/forward-facing-step.md).
The crenel profile of the linear-advection tests is a
[material-interface-type advection](/benchmarks/material-interface-advection.md) test. Four
subdivisions are compared: uncorrected DG is identical on all four, and with correction the
uniform ones resolve better.

# Version read

The archive file is the HAL preprint hal-03910148v1, "submitted on 21 Dec 2022", 39 PDF pages
(HAL cover page plus 38 paper pages), all read; pp. 6–9, 11, 14, 20, 31 and 36 were checked on
the page images. Title and authors match the Crossref record of the version of record (SIAM J.
Sci. Comput. 46:A851–A883, 2024), whose DOI is not printed in the preprint. Every page,
equation, figure and reference number on this page is that of the preprint and may differ from
the typeset article.

# Key claims

Registry notation (see the Notation map). Page-local: $\mathcal S_m$ the subcells of a cell
$K$; $\bar u_m$ the subcell means (submeans), $\bar U$ their vector, $U$ the vector of DG
moments, $\Phi$ the DG residual vector; $P$ the projection matrix moments → submeans; $A$ the
subcell adjacency matrix (orientation signs), $\mathsf D$ the diagonal of subcell areas,
$\mathsf B$ the boundary-flux vector, $\mathsf Q=\mathsf DP$; $L=AA^\top$ the subcell graph
Laplacian (not the left-eigenvector matrix) and $L^{+}$ its generalized inverse; $\hat F$ the
vector of face-integrated reconstructed fluxes.

1. A $\mathbb P^N$ DG scheme on any polygonal cell split into $N_N$ subcells with invertible $P$ is exactly $N_N$ subcell finite-volume schemes with reconstructed fluxes $\hat F=-A^\top L^{+}(\mathsf QM^{-1}\Phi+\mathsf B)$, where $L^{+}=(L+\lambda_{\mathrm g}\Pi)^{-1}-\Pi/\lambda_{\mathrm g}$, $\Pi=\frac1{N_N}\mathbf 1\otimes\mathbf 1$, any $\lambda_{\mathrm g}\ne0$ (§2.1, Eqs. 2.22–2.26, Thm. 2.1). **Derived**
2. Equivalently, the reconstructed flux is the interior flux minus the boundary jump distributed by the sub-resolution basis functions: $\hat F=F-A^\top L^{+}G$, with $G$ collecting $\int_{\partial K}\tilde b_m\,(f_h\cdot n-h)\,dS$ (§2.2, Eqs. 2.28–2.38, Thm. 2.2). **Derived**
3. The two theorems are "perfectly equivalent"; the residual form (2.23) is easier to implement and needs no sub-resolution basis functions (§2.2). **Stated**
4. In (2.23) only $\Phi$ and $\mathsf B$ depend on time; $P$, $A$ and $L^{+}$ can be precomputed and, for cells mapped to one reference element, depend only on the order and the subdivision (Remark 2). **Stated**
5. Setting the correction function $E(\cdot)=0$ in $\hat F=F-E(f_h\cdot n-h)$ gives Wang's spectral volume scheme (Remark 4). **Stated**
6. The one-to-one map needs as many subcells as degrees of freedom; with more subcells a least-squares return through a left inverse $R$, $RP=I_{N_N}$, is possible (§2, Remark 1). **Stated**
7. "Up to our knowledge", APLSC is the only technique working on totally unstructured grids that modifies the scheme locally at subcell level without affecting the solution everywhere in the cell (§3, p. 10). **Stated**
8. The corrected scheme is conservative at subcell level by construction; only troubled subcells and their first face neighbours are recomputed (§3.3). **Stated**
9. Because the fallback is a first-order finite-volume scheme, the maximum principle (scalar) or positivity (systems) holds by construction, provided the initial submeans are computed by integration on the subcells and mapped to moments by $P^{-1}$, not by nodal interpolation or $L^2$ projection (Remark 8). **Stated**
10. The blended correction (3.7), $\tilde F_{mp}=\alpha_{mp}\,(\text{first-order flux})+(1-\alpha_{mp})\hat F_{mp}$ with $\alpha_{mp}=1,\tfrac34,\tfrac12,\tfrac14$ on the faces of the troubled subcell, of its face neighbours, of its node neighbours and of their face neighbours, gives on the sixth-order Burgers test (576 cells, structured subdivision): 10 % corrected subcells on average for the original correction against 14 %; mean correction iterations 2.86 (max 6) against 1.46 (max 3); run time 2 min 22 s against 2 min 15 s (§3.4, Figs. 6–9; hardware not stated). **Shown**
11. Sixth-order APLSC-DG on smooth linear advection converges at sixth order and the correction never activates, so the smooth-extremum relaxation works (Table 1: $L^1$ orders 6.00, 5.97, $L^2$ 6.00, 5.96, $L^\infty$ 5.96, 5.41 for $h=1/10,1/20,1/40$; $L^1$ errors $1.62\times10^{-7}$, $2.53\times10^{-9}$, $4.03\times10^{-11}$) (§4.1.1). **Shown**
12. Crenel advection, sixth order, 576 cells, one period: uncorrected DG has minimum $-0.06$ and maximum $1.06$; APLSC-DG minimum $8.5\times10^{-6}$ and maximum 1 (Fig. 12). **Shown**
13. Uncorrected DG, written as subcell finite volumes with reconstructed fluxes (2.40), gives exactly the same solution for all four subdivisions (crenel, fourth order, 576 cells, five periods; Figs. 16–18). **Shown**
14. The $\|\cdot\|_\infty$ condition numbers of $P$ grow with the degree and are higher for structured than polygonal, and for uniform than non-uniform, subdivisions ($\mathbb P^3$: 31.75, 29.28, 27.89, 26.94; Table 2). **Shown**
15. With the correction, uniform subdivisions resolve linear advection much better than non-uniform ones; the difference comes mainly from the numerical detector, "highly dependent of the subcell aspect ratio", and is slight with the physical detector only (§4.1.1, Figs. 19–21). **Shown**
16. Solid-body rotation, sixth order, 576 cells: the global maximum principle holds (minimum $6.7\times10^{-10}$, maximum 0.97 at $t=2\pi$) (Fig. 22). **Shown**
17. KPP: uncorrected sixth-order DG is non-entropic and oscillatory; APLSC-DG on 1054 cells captures the entropic spiral; structured and Voronoi subdivisions are similar at fourth order (Figs. 33–34). **Shown**
18. For the Euler equations the discrete maximum principle is tested on the total energy only, and the physical detector requires positive density and internal energy (§4.3). **Stated**
19. Sedov with the energy in the subcell at the origin (total energy 1947.5 there, $2.5\times10^{-14}$ elsewhere) and initial pressure $10^{-14}$ runs at sixth order on 271 cells; "Any scheme lacking positivity-preserving property or a rigorous stabilization technique would fail" (§4.3.2, Figs. 38–39). **Shown** (failure claim **Stated**)
20. The Mach 3 forward-facing step runs at sixth order on 680 cells with no corner refinement and no modification of the scheme (Fig. 41). **Shown**
21. APLSC also performs well at third order on fine meshes (polar Sod on 10 571 cells, Sedov on 2894 cells) (Figs. 37, 40). **Shown**
22. The time step of the combined DG/subcell scheme is $\Delta t=\min\big(\min_K\frac{d_K}{2N+1},\min_{K,m}d_m\big)/a$, with $d_K$, $d_m$ the cell and subcell lengths (area over perimeter) (Eqs. 4.1–4.2). **Stated**

# Printed slips

- §3.4, p. 16: "because the dimension of $P^5$ is 20, each cell has been accordingly subdivided into 20 subcells". By the paper's own formula, $N_5=(5+1)(5+2)/2=21$.
- §4.2.1, p. 27: the Burgers initial datum is printed $u_0(\boldsymbol x)=\sin(2\pi(x,y))$, elsewhere $\sin(2\pi(x+y))$.
- Caption of Fig. 28: "6th-order uncorrected DG solution ... on a 576 cells mesh"; the text cites Fig. 28 for "a very coarse grid made of 242 cells".
- §4.2, p. 27: the subcell-wise neighbourhood of the non-linear tests is said to be "depicted in Figure 10", which shows the cell-wise set of the linear tests; the subcell-wise set is Fig. 27.
- §3.3, step 4, p. 13: a LaTeX artefact "[left = {]" before $\tilde F_{mp}$. §4, p. 17: a sentence without verb ("In this two-dimensional framework the two types of subdivisions introduced respectively in Figure 1(a) and 1(c).").
- §4.2.2 (KPP): $u_0=7\pi/2$ "if $x<\frac12$", with a non-bold $x$ where the paper writes points as $\boldsymbol x$.
- Reference list: [3] and [4] are the same work (Boris & Book, SHASTA, JCP 11:38–69, 1973) printed twice; [56] and [57] print the same "J. Comp. Phys., 178:210–251, 2002" for two different titles (Wang; Wang & Liu, part II); [52] (Vilar's 1D paper) is printed "J. Comp. Phys. 387", 2018.

# Notation map

| Vilar & Abgrall (HAL v1) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ | $N$ | DG degree; "$(k+1)$th order", so "6th order" is $\mathbb P^5$ |
| $N_k=(k+1)(k+2)/2$ | $N_N$ (local) | dimension of $\mathbb P^N$ in 2D, number of subcells |
| $\omega$, $\omega_c$ | domain, cell $K$ | $\omega$ is not a WENO weight |
| $\sigma^c_m$, $u^c_m$, $U_c$ | modal basis $b_m$ (local), moments, $U$ | $\sigma$ is not the affine scaling |
| $S^c_m$ | $\mathcal S_m$ (local) | subcell; **collision** with the candidate stencils $S_k$ |
| $\overline u^c_m$, $\overline U_c$ | $\bar u_m$, $\bar U$ | submeans |
| $M_c$ | $M$ | mass matrix (modal, not diagonal) |
| $\Phi_c$ | $\Phi$ (local) | DG residual vector |
| $P_c$, $R_c$ | $P$, $R$ (local) | projection matrix and left inverse; $R$ is not the eigenvector matrix |
| $\mathcal F_n$, $\mathcal F(u,v,\boldsymbol n)$ | $h$ | DG numerical flux, global Lax–Friedrichs |
| $\gamma$ (in 2.5, 4.1) | $a$ | maximum wave speed; **collision** with $\gamma$, ratio of specific heats (§4.3) |
| $\widehat F_n$, $\widehat F_{mp}$, $\widehat F_c$ | $\hat F$ (local) | reconstructed flux, face-integrated |
| $\widetilde F_{mp}$ | $\tilde F_{mp}$ (local) | corrected flux |
| $\boldsymbol F^c_h$, $F_{mp}$, $F_c$ | $f_h$, $F$ (local) | $L^2$ projection of the interior flux onto $(\mathbb P^{N+1})^2$ and its face integrals |
| $\varepsilon^c_{mp}$ | orientation sign (local) | entries of $A$; not a regularization |
| $A_c$, $D_c$, $B_c$, $Q_c=D_cP_c$ | $A$, $\mathsf D$, $\mathsf B$, $\mathsf Q$ (local) | **collision** of $D$, $B$, $Q$ with the SBP matrices |
| $L_c=A_cA_c^t$, $\mathcal L_c^{-1}$, $\Pi$, $\lambda$ | $L$, $L^{+}$, $\Pi$, $\lambda_{\mathrm g}$ (local) | **collision** of $L$ with $R^{-1}$ and of $\mathcal L$ with the semi-discrete operator |
| $\phi_m$, $\widetilde\phi_m$ | $b^{\mathrm{sr}}_m$, $\tilde b_m$ (local) | sub-resolution basis functions |
| $\theta_{mp}$ | $\alpha_{mp}$ | DG–FV blending per face, 1 = first-order FV; **collision** with the Zhang–Shu $\theta$ |
| $\delta$, $\mathcal N(S^c_m)$ | relaxation and neighbourhood of the numerical detector (local) | $\delta$ is not the TENO flag |
| $d_c$, $d^c_m$ | $d_K$, $d_m$ (local) | cell and subcell lengths |
| $\rho$, $\boldsymbol q=\rho\boldsymbol v$, $E$, $p$ | $\rho$, $\rho v$, $E$, $p$ | agree |
| $\varepsilon=E-\frac12\lvert\boldsymbol q\rvert^2/\rho$ | $\rho e$ | internal energy per volume, $p=(\gamma-1)\rho e$ |

# Reference list

The file prints 62 references, numbered [1]–[62] in roughly alphabetical order. The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` including
`vilar-2024`. The printed duplicate [3]/[4] (Boris & Book 1973) and the two Wang 2002 items
[56]/[57] that print one volume and page range are recorded as printed and flagged for the
merge. Ref. [59] (Wu & Shu, geometric quasilinearization) is printed as a 2021 preprint and is
kept apart from the published SIAM Review article. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunk 10 (2026-10-23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Equivalence of DG and subcell finite volumes](/results/dg-subcell-finite-volume-equivalence.md)
* [KPP rotating wave](/benchmarks/kpp-rotating-wave.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Sedov blast wave](/benchmarks/sedov-blast-wave.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Solid-body rotation](/benchmarks/solid-body-rotation.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
