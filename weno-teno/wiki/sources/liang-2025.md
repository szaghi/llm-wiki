---
type: Source
title: "Liang et al. (2025) — Efficient Arbitrary-High-Order TENO Schemes with Local Adaptive Dissipation for Compressible Flow Simulation on Unstructured Meshes"
description: "Fifth- to seventh-order finite-volume TENO-E schemes for unstructured meshes: a variance-of-relative-jumps troubled-cell indicator switches between the linear large-stencil reconstruction of conserved variables and a characteristic TENO step whose cut-off is set from the same indicator, with about half the cost of CWENO of the same order."
resource: "doi:10.1007/s10915-025-02918-w"
source_kind: paper
authors: [Liang T., Shyy W., Fu L.]
year: 2025
venue: "J. Sci. Comput. 104:1"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Scientific_Computing_Liang_Efficient_Arbitrary-High-Order_TENO_Schemes_with_Local_Adapt.pdf"
tags: [teno, unstructured-mesh, troubled-cell, hybrid-scheme, finite-volume, performance]
timestamp: 2026-10-23T19:54:00Z
---

# Summary

Liang et al. (2025) build fifth-, sixth- and seventh-order finite-volume
[TENO](/methods/targeted-eno.md) schemes for the compressible Euler equations
on unstructured triangular, tetrahedral and hexahedral meshes, named TENO5-E,
TENO6-E and TENO7-E, in the open-source code UCNS3D. There are three
ingredients. A new [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
takes the absolute relative jumps of the density cell average between the
target cell and each neighbour of its large central-biased stencil and
compares their variance with a fixed threshold $10^{-3}$. A
[hybrid](/methods/hybrid-weno.md) switch then applies, in untroubled cells, the
linear high-order least-squares reconstruction of the large stencil directly
to the conserved variables, with no
[characteristic decomposition](/methods/characteristic-decomposition.md) and no
weights. In troubled cells a TENO step in characteristic variables keeps the
whole large stencil when it passes the cut-off, and otherwise averages the
surviving third-order directional stencils with equal weights. Third, the
cut-off is [adaptive](/methods/adaptive-teno.md): $C_{T,i}=10^{-\lfloor\mathsf e_i\rfloor}$
with $\mathsf e_i$ mapped from the same variance by a cubic kernel, so $C_T$
runs from $10^{-10}$ (weak fluctuation) to $10^{-6}$ (strong shock). The
authors argue that the first-order jumps separate fluctuations from
discontinuities better than the high-order differences inside the
[smoothness indicators](/definitions/smoothness-indicator.md). All parameters
are fixed across orders and tests.

The comparison schemes are CWENO5/6/7 in UCNS3D. TENO-E reaches the design
order on a periodic [density wave](/benchmarks/density-wave-advection.md) on
triangles and is monotone on the [Sod tube](/benchmarks/sod-and-lax-shock-tubes.md).
It resolves more small-scale structure in the [Shu–Osher problem](/benchmarks/shu-osher-problem.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[2D Riemann](/benchmarks/two-dimensional-riemann-problems.md) configurations 8
and 16, Schardin's [shock–wedge problem](/benchmarks/shock-diffraction.md),
an [implosion-type problem](/benchmarks/explosion-and-implosion-problems.md)
inside multiple circles, a 3D shock–cone interaction and the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md). Total wall time is
about 0.52–0.88 of CWENO's in the tabulated cases. No theorem is proved.

# Version read

The archive file is the version of record (Springer typeset, open access CC
BY 4.0), 40 pages, all read; pp. 4–12 and 28–32 checked on the page images.
Title, authors, venue and DOI on page 1 match the Crossref record. Label in
this bundle: Liang et al. (2025); [Liang & Fu (2026)](/sources/liang-2026.md),
the converged ENO paper, is a different work. Every claim, equation and
number on this page is that of the version of record.

# Key claims

Registry notation: $\beta_k$ the Jiang–Shu-type indicators integrated over
the reference cell (source $\mathcal{SI}_k$), $\epsilon$, $q$, $\chi_k$,
$\delta_k$, $C_T$, $d_k$ as in the registry. Page-local: $S_{\mathrm c}$ the
large central-biased stencil of the target order and $S_0,\dots,S_{K_{\mathrm d}-1}$
the $K_{\mathrm d}$ third-order directional stencils (source $\mathcal S_K$,
$\mathcal S_k$, $K$); $\upsilon_k=1/(\beta_k+\epsilon)^q$ the TENO measure
without global indicator; $\mathsf r_{i,k}$ the relative density jump to
neighbour $k$ (source $\gamma_{i,k}$), $N_{\mathrm n}$ the number of
neighbours, $\mathsf v_i$ their variance (source $\sigma_i$), $C_{\mathrm v}$
its threshold (source $\mathcal C$), $\mathcal D_i$ the troubled-cell flag;
$\mathsf e_i$, $m_i$, $g_{\mathrm c}$, $\mathsf b_1$, $\mathsf b_2$,
$\mathsf v_L$, $\mathsf v_U$ the cut-off map (source $\psi_i$, $m_i$, $g$,
$\beta_1$, $\beta_2$, $\sigma_L$, $\sigma_U$).

1. The optimal linear weights of classical unstructured WENO vary strongly with mesh topology and can be negative; raising the directional stencils to the target order removes this but is expensive (§1). **Stated**
2. The high-order undivided differences of the WENO/TENO smoothness indicators are "over-sensitive" to both high-wavenumber fluctuations and discontinuities and do not scale-separate them, so fluctuations are treated as dissipatively as discontinuities (§1, §3.3.4). **Stated**
3. With a fixed $C_T$, a small value gives low dissipation but may oscillate and a large value is robust but dissipative; "Up to now, the deficient compromise between stable shock-capturing and high-resolution properties is inevitable for unstructured meshes" (§1). **Stated**
4. The linear reconstruction uses $N_s=2N_k$ stencil cells and a least-squares solve, for robustness on poor-quality meshes (§3.1). **Stated**
5. Troubled-cell indicator: $\mathsf r_{i,k}=\lvert\bar\rho_{i,k}-\bar\rho_{i,0}\rvert/\bar\rho_{i,0}$, $\mathsf v_i=\frac1{N_{\mathrm n}}\sum_{k=1}^{N_{\mathrm n}}\big(\mathsf r_{i,k}-\mathrm{avg}_k\,\mathsf r_{i,k}\big)^2$, and $\mathcal D_i=1$ iff $\mathsf v_i\ge C_{\mathrm v}$ (Eqs. (19)–(20), §3.3.2). **Stated** (design), performance **Shown**
6. Density alone, in physical space, with $C_{\mathrm v}=10^{-3}$ is "sufficient" by "extensive numerical experiments"; the value is fixed for all orders and tests (§3.3.2). **Shown** (by the tests of §4)
7. Unlike KXRCF, case-sensitive through a scaling parameter, and the Fu–Shu indicator, whose threshold depends on the polynomial degree, the new indicator needs no case-dependent tuning (§3.3.2). **Stated** (the double-Mach troubled-cell maps are compared only with figures of other papers)
8. Hybrid weighting (Eq. (21)): the linear high-order reconstruction of the conserved variables where $\mathcal D_i=0$, TENO in characteristic variables where $\mathcal D_i=1$; characteristic projection and weights are skipped in smooth regions (§3.3.3). **Stated** (design)
9. TENO step: $\upsilon_k=1/(\beta_k+\epsilon)^q$, $\epsilon=10^{-12}$, $q=6$; $\chi_k=\upsilon_k/\sum_l\upsilon_l$; $\delta_k=0$ if $\chi_k<C_T$, else 1. If $\delta=1$ on $S_{\mathrm c}$ the reconstruction is the large-stencil polynomial; otherwise $\sum_k\omega_kP_k$ over the directional stencils with $\omega_k\propto d_k\delta_k$, $d_k=1/K_{\mathrm d}$ (Eqs. (22)–(27)). **Stated** (design, after the unstructured TENO of [Ji et al. (2022)](/sources/ji-2022.md), [Ji et al. (2023)](/sources/ji-2023.md))
10. The directional stencils are third order and the large central-biased stencil carries the target order; stencils are built with the Naive Cell-Based (central) and Type-3 (directional) algorithms of Tsoutsanis (§3.3.1, Figs. 2–3). **Stated**
11. Adaptive cut-off: $C_{T,i}=10^{-\lfloor\mathsf e_i\rfloor}$, $\mathsf e_i=\mathsf b_1-\mathsf b_2\big(1-g_{\mathrm c}(m_i)\big)$, $g_{\mathrm c}(m)=(1-m)^2(1+2m)$, $m_i=\big(\min(\mathsf v_U,\mathsf v_i)-\mathsf v_L\big)/(\mathsf v_U-\mathsf v_L)$, $\mathsf b_1=10$, $\mathsf b_2=4$, $\mathsf v_L=10^{-3}$, $\mathsf v_U=10^{-2}$; $C_T\to10^{-6}$ for $\mathsf v_i>\mathsf v_U$ and $\to10^{-10}$ for $\mathsf v_i\approx\mathsf v_L$ (Eq. (28), §3.3.4). **Stated** (design)
12. Rationale for (11): low-order smoothness measures are "more sensitive to discontinuities than to high-wavenumber fluctuations", citing Ren et al. (§3.3.4). **Stated**
13. TENO-E recovers the background linear scheme exactly in smooth regions, whereas CWENO recovers it only asymptotically (§3.3.5). **Stated**
14. The bounds of $C_T$ add parameters but are "rather generally applicable since they function in the spectral space"; the CWENO choice $\lambda'_K=10^4$ is "relatively ad hoc" (§3.3.5). **Stated**
15. Design order on uniform triangles (periodic density wave, $h=2/13$ to $1/80$): final $L_\infty$ orders 4.95, 5.81, 6.99 and $L_2$ orders 4.92, 6.02, 6.85 for TENO5-E, TENO6-E, TENO7-E (Table 1). **Shown**
16. TENO6-E is below design order between $h=1/20$ and $1/40$: $L_\infty$ 5.53, $L_2$ 5.75 (Table 1). **Shown**
17. Sod tube on triangles, $h\approx1/60$: all schemes monotone near the shock and the contact (Fig. 4). **Shown**
18. Shu–Osher on triangles, $h\approx1/20$: TENO-E resolves the post-shock fluctuations "significantly better" than CWENO of the same order (Figs. 5–6). **Shown**
19. Double Mach reflection ($h\approx1/125$, $1/200$, $1/280$): TENO-E resolves more small-scale structure; $C_T\approx10^{-6}$ near strong shocks and smaller in density fluctuations; "about 50% cheaper" than CWENO of the same order (Figs. 7–12). **Shown**
20. Riemann configuration 8 ($h\approx1/550$): total time ratios TENO5-E 0.52, TENO6-E 0.64, TENO7-E 0.88 against CWENO5 = 1.00 (CWENO6 1.16, CWENO7 1.42); reconstruction time 0.43, 0.55, 0.80 (CWENO6 1.19, CWENO7 1.46) (Table 2). **Shown**
21. Riemann configuration 16: total time ratios 0.57, 0.68, 0.86 (CWENO6 1.25, CWENO7 1.52); reconstruction 0.49, 0.60, 0.78 (CWENO6 1.29, CWENO7 1.61) (Table 3). **Shown**
22. Shock–wedge interaction (about 1,627,638 triangles, CFL 0.6): total time ratios 0.56, 0.67, 0.79 (CWENO6 1.12, CWENO7 1.33); reconstruction 0.48, 0.59, 0.72 (CWENO6 1.14, CWENO7 1.38); more tip vortices captured (Table 4, Fig. 18). **Shown**
23. Implosion inside multiple circles (911,276 triangles): TENO6-E total cost 20583.60 s, "about 44.2%" of CWENO6's 46562.19 s, with richer interfacial instabilities (§4.7, Fig. 20). **Shown**
24. 3D shock–cone ($M_s=1.3$, 2,495,825 tetrahedra): "very few elements are misidentified" by the indicator outside the shock and the torus vortex (Figs. 22–23). **Shown**
25. Inviscid Taylor–Green vortex ($64^3$, $128^3$ hexahedra): TENO6-E preserves kinetic energy better and has a more energetic spectrum than CWENO6; reconstruction time 11966.31 s and 153987.56 s, "about 35.2% and 27.0%" of CWENO6's 33930.79 s and 570238.01 s (§4.9, Figs. 24–27). **Shown**
26. TENO-E typically needs "only 50% computational costs of the corresponding CWENO schemes at the same mesh resolution" (§5). **Shown** (Tables 2–4, §§4.7, 4.9)
27. The indicator needs extra communication across processor boundaries, an overhead outweighed by skipping characteristic decomposition and weights in smooth regions (§3.3.5). **Stated** (no parallel timing; the hardware is "the same workstation with the same Linux system", §4)
28. Riemann solver: HLL, chosen over Roe and HLLC "due to its simplicity and superior robustness"; time integration SSP-RK3, CFL 0.4 by default and 0.6 in the shock–wedge, shock–cone and Taylor–Green cases (§2, §4). **Stated**

# Printed slips

- **Eqs. (10)–(11), coefficient count.** Eq. (10) writes $P=\sum_{l=0}^{N_k}a_l\psi_l=\overline{\mathbf U}_0+\sum_{l=1}^{N_k}a_l\psi_l$, so $N_k$ counts the non-constant basis functions, but Eq. (11) gives $N_k=\frac1{n_d!}\prod_{m=1}^{n_d}(r+m)$, the number of all monomials of degree $\le r$ including the constant. *(Compiler check, not in the sources: for $n_d=2$, $r=2$, Eq. (11) gives $3\cdot4/2=6$, while there are 5 non-constant monomials $\xi,\eta,\xi^2,\xi\eta,\eta^2$; the two equations differ by one.)*
- **§3.3.4, lower limit of $C_T$.** The text says that for $\sigma_i\approx\sigma_L$ "$C_{T,i}$ decreases to $10^{-\beta_1}$". *(Compiler check, not in the sources: TENO is invoked only where $\sigma_i\ge\mathcal C=10^{-3}=\sigma_L$, so $m_i\in[0,1]$; $g$ decreases from 1 to 0 on $[0,1]$, so $\psi_i\in[6,10]$, and $\psi_i=10$ only at $\sigma_i=\sigma_L$ exactly. With the floor, $C_{T,i}=10^{-10}$ is attained only there; any $\sigma_i>\sigma_L$ gives $C_{T,i}\ge10^{-9}$.)*
- Eq. (7) calls $P$ "an $r$th-order approximation" with error $h^{r+1}$, and Eq. (18) calls $r$ "the polynomial order": $r$ is the polynomial degree.
- Eq. (18) prints the measure as "$(d\xi,d\eta,d\zeta)$".
- §3.3.2 calls $\sigma_i$ "the mean squared deviation", as Eq. (19) is, but also describes it as "the average absolute difference" between the $\gamma_{i,k}$ and their mean.
- Symbol reuse: $N_e$ is the number of stencil neighbours in Eq. (19) and the number of mesh elements in Table 1; $\psi$ is a basis function (Eq. (10)) and the cut-off exponent (Eq. (28)); $\beta$ is a multi-index (Eq. (18)) and the constants $\beta_1$, $\beta_2$ (Eq. (28)); $\omega_\kappa$ are quadrature weights and $\omega_k$ CWENO weights.
- References: ref. [1] prints the authors as "Von, N.J., Richtmyer, R."; ref. [54] prints only "Woodward, P." where the text says "Woodward and Colella [54]"; refs. [7] and [44] are the same work (Jiang & Shu 1996); ref. [13] prints garbled editors "Johnson, B.C., Tadmor, C.W."; ref. [40] (HLL) is printed as pp. 53–79 of a 1997 Springer volume with no book title.

# Notation map

| Liang, Shyy & Fu | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\overline{\mathbf U}_i$ | $u$, $\bar u_i$ | bold vectors not used in the registry |
| $\mathbf U_{i,j,L}$, $\mathbf U_{i,j,R}$ | $u^-$, $u^+$ at the face | |
| $\mathbf F^{\mathbf n_{i,j}}$ | normal numerical flux $h(u^-,u^+)$ | HLL |
| $u,v,w$ | $v_1,v_2,v_3$ | |
| $r$ | polynomial degree (local) | **collision** with the registry $r$, the WENO stencil width |
| $\mathcal S_K$; $\mathcal S_0,\dots,\mathcal S_{K-1}$ | $S_{\mathrm c}$; $S_0,\dots,S_{K_{\mathrm d}-1}$ (local) | **collision**: source $K$ counts directional stencils, registry $K$ is the TENO stencil width |
| $\mathcal{SI}_k$ | $\beta_k$ | Jiang–Shu type over the reference cell |
| $\lambda_K$, $\lambda'_K$, $\lambda_k$ | $d_k$; $\lambda'_K$ (CWENO, local) | TENO-E uses $d_k=1/K_{\mathrm d}$ |
| $\omega_k$, $\alpha_k$ | $\omega_k$, $\alpha_k$ | CWENO exponent 4, $\epsilon=10^{-14}$ |
| $\upsilon_k$, $\chi_k$ | $\upsilon_k$ (local), $\chi_k$ | $\upsilon_k$ has no global indicator, unlike the registry $\gamma_k$ |
| $\delta_k$, $C_T$, $C_{T,i}$ | $\delta_k$, $C_T$, $C_{T,i}$ | agree |
| $\gamma_{i,k}$ | $\mathsf r_{i,k}$ (local) | **collision** with $\gamma$ and $\gamma_k$ |
| $\sigma_i$, $N_e$, $\mathcal C$, $\mathcal D_i$ | $\mathsf v_i$, $N_{\mathrm n}$, $C_{\mathrm v}$, $\mathcal D_i$ (local) | **collision** of $\sigma_i$ with the TENO-A mapping $\sigma_i$ |
| $\psi_i$, $m_i$, $g$, $\beta_1$, $\beta_2$, $\sigma_L$, $\sigma_U$ | $\mathsf e_i$, $m_i$, $g_{\mathrm c}$, $\mathsf b_1$, $\mathsf b_2$, $\mathsf v_L$, $\mathsf v_U$ (local) | **collision** of $\beta_{1,2}$ with $\beta_k$, of $g$ with the mapping $g(\omega)$ |
| $\varepsilon$ | $\epsilon$ | $10^{-12}$ (TENO-E), $10^{-14}$ (CWENO) |
| $h$ | $\approx\lvert V_i\rvert^{1/n_d}$, "approximate edge length" | |

# Reference list

The paper prints 61 references, numbered [1]–[61], with no DOIs. The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
including `liang-2025`. Refs. [7] and [44] are a printed duplicate (Jiang &
Shu 1996) and are merged as one work. Ref. [1] is keyed by the surname von
Neumann. Ref. [29] (Tsoutsanis & Dumbser, Comput. Fluids 225:104961) is a
different work from the ingested [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md)
and takes its disambiguated key; ref. [34] (Fu L., Hu & Adams) and ref. [46]
(Fu G. & Shu) share a surname-year and are matched by volume and page. Refs.
[31], [32], [36], [37], [38], [43] and [48] are the ingested
[Liang & Fu (2024a)](/sources/liang-2024.md), [Liang & Fu (2024b)](/sources/liang-2024-b.md),
[Ji et al. (2022)](/sources/ji-2022.md), [Ji et al. (2023)](/sources/ji-2023.md),
[Fu (2023)](/sources/fu-2023.md), [Maltsev et al. (2023)](/sources/maltsev-2023.md)
and [Fu (2021)](/sources/fu-2021.md). Refs. [5] and [40] (Harten et al.) are
matched by title. No item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunks 11–12 (2026-10-24/30). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Converged ENO (CENO)](/methods/converged-eno.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [ENO property](/definitions/eno-property.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Shock diffraction](/benchmarks/shock-diffraction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
