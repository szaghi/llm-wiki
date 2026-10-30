---
type: Source
title: "Liang & Fu (2026) — Finite-volume converged ENO scheme with adaptive mesh resolution for steady-state compressible flow simulation"
description: "Finite-volume fifth-order converged ENO (CENO) scheme with hysteretic TENO-type stencil selection, a noise filter that freezes the stencil flags, and cell-average multiresolution AMR driven by a smoothness-indicator detector with a frozen buffer band, so that steady Euler residuals fall to near machine zero."
resource: "doi:10.1016/j.cpc.2025.109912"
source_kind: paper
authors: [Liang T., Fu L.]
year: 2026
venue: "Comput. Phys. Commun. 319:109912"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_Computer_Physics_Communications_Liang_Finite-volume_converged_ENO_scheme_with_adaptive_mesh_resolu.pdf"
tags: [teno, finite-volume, amr, smoothness-indicator, shock-capturing]
timestamp: 2026-10-23T20:40:00Z
---

# Summary

Liang & Fu (2026) carry their finite-difference
[converged ENO](/methods/converged-eno.md) (CENO) scheme (Liang & Fu, J.
Comput. Phys. 519, 2024, not ingested) over to finite volumes and couple it
with cell-average multiresolution [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
(Harten and Bihari multiresolution on the pyramid block structure of Han, Hu
and Adams), for steady compressible Euler flows whose residual should fall to
machine zero. The premise, taken from the finite-difference paper, is that
[WENO-Z](/methods/weno-z.md) and [TENO](/methods/targeted-eno.md) stall at
steady state because the reconstruction formula (stencil choice and weights)
at a fixed interface keeps changing in time.

There are three contributions. (1) A stencil selection for finite volumes:
a TENO-type cut-off whose threshold depends on whether the stencil was kept
at the previous step (hysteresis), plus a noise filter that freezes the
flags whenever the global [smoothness indicator](/definitions/smoothness-indicator.md)
$\tau_{\mathrm C}=\lvert2\beta_0-(\beta_1+\beta_2)\rvert$ is below the local
mesh width. The reconstruction is prioritized: the 5-point fifth-order linear
value if the large stencil is smooth, otherwise a renormalized combination
of the two 2-point stencils. (2) An adaptation criterion built from a
discontinuity detector $\chi_{\mathrm d}\in(0,1]$ computed from the
already-available $\beta_k$, with refine and coarsen thresholds $0.3<0.7$
that leave a band in which the mesh is frozen. (3) A residual for
time-varying meshes, computed on a fixed virtual root level obtained by
recursive coarsening of the leaf data.

The tests are a 1D stationary shock and six 2D [steady shock problems](/benchmarks/steady-shock-problems.md)
(oblique shock, regular shock reflection, supersonic flow past a plate,
heterolateral and ipsilateral shock interactions, multiple shock reflection),
plus static detection tests that include the
[Jiang–Shu composite profile](/benchmarks/jiang-shu-composite-advection.md).
CENO-AMR residuals settle near machine zero, while uniform-mesh FV WENO5-Z
and TENO5 stall in 2D. The mid-point flux rule makes the multi-D scheme second
order overall, which the authors state. User CPU time is 0.16–0.53 of
WENO5-Z's at the finest effective resolution.

# Version read

The archive file is the version of record (Elsevier typeset, CPC 319 (2026)
109912), 22 pages, all read; pp. 3–4, 6–10, 14–15 and 19 checked on the page
images. Title, authors, venue and DOI on page 1 match the Crossref record.
The paper prints a code repository, https://github.com/LMNS3d/CENO-AMR (§4.2).
Label in this bundle: Liang & Fu (2026), distinct from
[Liang et al. (2025)](/sources/liang-2025.md) and from Liang & Fu (2024a/b).
Every claim, equation and number on this page is that of the version of
record.

# Key claims

Registry notation: $\bar u_i$, $u^\mp_{i+1/2}$ (source $u^L$, $u^R$),
$\beta_k$ (Jiang–Shu, Eq. (18)), $\gamma_k=\big(1+\tau_{\mathrm C}/(\beta_k+\epsilon)\big)^6$
(registry $C=1$, $q=6$, $\epsilon=10^{-8}$), $\chi_k$, $\delta_k$, $C_T$, $d_k$,
$\omega_k$. Page-local: stencils $S_0$ (5-point, large), $S_1=\{\bar u_{i-1},\bar u_i\}$,
$S_2=\{\bar u_i,\bar u_{i+1}\}$ (not the registry's upwind numbering);
$\tau_{\mathrm C}=\lvert2\beta_0-(\beta_1+\beta_2)\rvert$; $\tilde\delta_k$,
$\hat\delta_k$ the previous and the temporary flag; $C_{T0}$, $C_{T1}$ the two
cut-offs; $c_1$, $c_2$ the prediction coefficients (source $\gamma_k$);
$\chi_{\mathrm d}$ the discontinuity detector (source $\chi$); $\Delta\beta_{ij}$;
$\varepsilon_{\mathrm r}$, $\varepsilon_{\mathrm c}$ the refine and coarsen
thresholds; $\mathrm{Res}_A$ the root-level residual.

1. Following the authors' finite-difference paper, non-convergence to steady state is attributed to "the unsteady effect of shock-induced numerical instability on the nonlinear weighting process as well as the resultant variation of the numerical formula for the spatially fixed cell interface flux at different time instants" (§1, §3.2.3). **Stated** (cited)
2. Earlier remedies (the Zhang–Shu smoothness indicator, the upwind-biased eigenvector evaluation of Zhang, Jiang and Shu) reduce the residual to machine zero "in many test problems", but the residual "is difficult to reduce to near machine zero when encountering strong shocks passing through the boundaries of the computational domain" (§1). Of the post-shock-oscillation-removal schemes, among them [Wan & Xia (2022)](/sources/wan-2022.md), the paper says that "the numerical solution from these schemes still can not converge to a steady state straightforwardly for some two-dimensional steady-state problems with shock interactions and reflections" (§3.2.3). **Stated**
3. Hysteretic cut-off: $\hat\delta_k=0$ if $\chi_k<C_{T,k}$, else 1, with $C_{T,k}=C_{T0}=10^{-1}$ if $\tilde\delta_k=0$ and $C_{T,k}=C_{T1}$ otherwise, $C_{T1}=10^{-10}$ for $S_0$ and $10^{-8}$ for $S_1$, $S_2$ (Eq. (21)). **Stated** (design)
4. Despite the hysteresis, "stable shock-capturing capabilities are still maintained in general applications due to the strong scale separation properties of Eq. (17)" (p. 7). **Stated**
5. In finite volumes there is no dissipative global Lax–Friedrichs splitting before the reconstruction, so small noise from AMR and from shocks crossing smooth regions is "magnified exponentially due to the power function in Eq. (17)" and changes the formula needlessly (p. 7). **Stated**
6. Taylor expansion: $\tau_{\mathrm C}=\big\lvert\big(\tfrac23u'u'''-\tfrac53(u'')^2\big)\Delta x^4+O(\Delta x^6)\big\rvert$, so $\tau_{\mathrm C}$ removes the common $u'^2\Delta x^2$ term of the $\beta_k$ (Eqs. (22)–(23)). **Derived** (see Printed slips on Eq. (22))
7. Noise filter: $\delta_k=\tilde\delta_k$ if $\tau_{\mathrm C}<\Delta x$, else $\delta_k=\hat\delta_k$; the local $\Delta x$ as threshold gives "scale-adaptive filtering in multi-resolution grids" (Eq. (24)). **Stated** (design)
8. Prioritized reconstruction: if $\delta_0=1$ the fifth-order linear value $u^-_{i+1/2}=\tfrac1{60}(2\bar u_{i-2}-13\bar u_{i-1}+47\bar u_i+27\bar u_{i+1}-3\bar u_{i+2})$ is used; otherwise $\omega_k=d_k\delta_k/(d_1\delta_1+d_2\delta_2)$, $d_1=1/3$, $d_2=2/3$, which is the third-order scheme when both flags are 1, and dropping a stencil "such that the ENO property is achieved" (§3.2.4, Eqs. (12), (25)–(26)). **Stated**
9. Detector: $\chi_{\mathrm d}=\min(\Delta\beta_{01},\Delta\beta_{02},\Delta\beta_{12})$, $\Delta\beta_{ij}=(2\beta_i^2\beta_j^2+\epsilon)/(\beta_i^4+\beta_j^4+\epsilon)\in(0,1]$; $\Delta\beta_{ij}\approx1$ when $\beta_i\approx\beta_j$ and $\approx0$ when one stencil is crossed by a discontinuity (Eqs. (27)–(28)). **Derived** (bound from $2ab\le a^2+b^2$)
10. $\chi_{\mathrm d}$ flags discontinuities and non-smooth regions in four static profiles on $[0,2]$, $N=400$ (Fig. 3). **Shown**
11. Adaptation: refine a block if any cell has $\chi_{\mathrm d}<\varepsilon_{\mathrm r}$, coarsen it if all cells have $\chi_{\mathrm d}>\varepsilon_{\mathrm c}$, otherwise keep it; $\varepsilon_{\mathrm r}=0.3$, $\varepsilon_{\mathrm c}=0.7$ "based on preliminary numerical experiments" (§3.3). **Stated** (design)
12. The criterion is problem-independent because it works in characteristic space on a fixed interval, needs only block-local data (no inter-level dependency, unlike Harten-type prediction errors) and costs little because the $\beta_k$ are already computed (Remarks 1–3). **Stated**
13. Harten-type prediction-error criteria need case-by-case thresholds and inter-level communication "impractical for extensive parallelization within distributed-memory architectures" (§3.3). **Stated**
14. Classical AMR keeps refining and coarsening at steady state, which changes the reconstruction formula and stops the residual from reaching machine zero (§1, §3.3). **Stated**
15. The prediction operator (fifth order, $c_1=-22/128$, $c_2=3/128$) is conservative between levels, $P_{l+1\to l}\circ P_{l\to l+1}=\mathrm{Id}$ (§3.1, Eqs. (8)–(10)). **Stated** (cited)
16. Multi-D finite volumes with the mid-point flux rule are "overall-speaking second-order" for nonlinear multi-D problems; citing Zhang, Zhang and Shu, Gaussian and mid-point finite-volume WENO "tend to produce comparable simulation results for more general non-smooth shocked problems" (§4.1). **Stated**
17. The residual on the virtual root level (Eq. (31)) reproduces the variations of the finest leaf blocks on a fixed data structure, because coarsening is "conservative, unique and exact" (§4.2). **Stated**
18. 1D steady shock ($M_\infty=2$, finest $N=512$, $t=12$): all schemes reach near machine zero, and "the present CENO-AMR scheme exhibits the lowest numerical residual during the simulation process" (§5.1, Fig. 5). **Shown**
19. Oblique steady shock (finest $1024\times512$): only the CENO-AMR residual settles to machine-zero level; WENO5-Z and TENO5 show post-shock oscillations; compression ratios above 90 %; "not very sensitive" to $(\varepsilon_{\mathrm r},\varepsilon_{\mathrm c})$ over five pairs (§5.2, Figs. 6–10). **Shown**
20. Regular shock reflection (finest $2048\times512$): shocks without the oscillations of WENO5-Z and TENO5, residual close to machine zero, compression above 90 % (§5.3, Figs. 11–15). **Shown**
21. Supersonic flow past a plate ($25^\circ$, $M_\infty=3$, finest $1024\times512$): only the CENO-AMR residual reaches machine zero (§5.4, Figs. 16–18). **Shown**
22. Heterolateral shock interaction: CENO-AMR residual "around $10^{-13}$", WENO5-Z and TENO5 "around $O(1)$"; compression above 85 % (§5.5, Figs. 19–21). **Shown**
23. Ipsilateral shock interaction: WENO5-Z and TENO5 residuals "reduced to around $10^{-1}$", CENO-AMR to machine-zero level (§5.6, Figs. 22–24). **Shown**
24. Multiple shock reflection (finest $4096\times512$): superior convergence of CENO-AMR, compression above 90 % (§5.7, Figs. 25–26). **Shown**
25. User CPU time (Table 1), WENO5-Z / TENO5 / CENO-AMR: 1D shock 14.67 / 15.66 / 5.98 s; oblique shock 683,543 / 722,219 / 189,665; regular reflection 1,214,910 / 1,416,870 / 305,889; plate 775,052 / 777,715 / 126,187; heterolateral 353,849 / 499,693 / 186,841; ipsilateral 851,890 / 982,024 / 362,167; CENO-AMR ratios 0.408, 0.277, 0.252, 0.163, 0.528, 0.425. No hardware, core count or compiler is printed (§5.8). **Shown**
26. CENO-AMR cuts user CPU time by about 59 % and 62 % against WENO5-Z and TENO5 in 1D and about 75 % and 78 % on the regular reflection (§5.8). **Shown** *(compiler check, not in the sources: $1-5.98/14.67=0.592$, $1-5.98/15.66=0.618$, $1-305889/1214910=0.748$, $1-305889/1416870=0.784$)*
27. All tests: $\gamma=1.4$, HLLC flux, SSP-RK2 with local time stepping, CFL 0.4, blocks of 4 cells (1D) or $4\times4$ (2D), all stencils initialized as smooth (§5). **Stated**
28. The residual settles "close to machine zero" in all benchmarks, compression ratios are "typically higher than 80 %", and the ENO behaviour is better than that of FV WENO and TENO "designed for unsteady-state problems" (§6). **Shown** (summary of §5)

# Printed slips

- **Eq. (22), Taylor expansions of the $\beta_k$.** Printed: $\beta_0=u'^2\Delta x^2+\tfrac{13}{12}u''^2\Delta x^4+\big(\tfrac{781}{720}u'''^2-\tfrac1{360}u''u''''-\tfrac1{15}u'u^{(5)}\big)\Delta x^6$, $\beta_{1,2}=u'^2\Delta x^2\mp u'u''\Delta x^3+\big(\tfrac14u''^2+\tfrac13u'u'''\big)\Delta x^4$. *(Compiler check, not in the sources: inserting Taylor-expanded point values $u(x_j)$ into Eq. (19) reproduces these coefficients exactly; inserting the cell averages $\bar u_j$ of the finite-volume scheme gives $\beta_0=u'^2\Delta x^2+\big(\tfrac{13}{12}u''^2+\tfrac1{12}u'u'''\big)\Delta x^4+\big(\tfrac{1043}{960}u'''^2+\tfrac7{80}u''u''''-\tfrac{21}{320}u'u^{(5)}\big)\Delta x^6$ and $\beta_{1,2}=u'^2\Delta x^2\mp u'u''\Delta x^3+\big(\tfrac14u''^2+\tfrac5{12}u'u'''\big)\Delta x^4$. The printed expansions are those of the finite-difference setting. The $\Delta x^4$ term of $\tau_{\mathrm C}$ in Eq. (23) is the same in both settings, so the argument for $\tau_{\mathrm C}$ stands; the $\Delta x^6$ terms differ.)*
- Eq. (21), p. 7: "will be reduced to $C_{T1}=10^{-10}$ and $C_{T1}=10^{-8}$ [1,19,20], respectively": one symbol, two values (large and small stencils).
- Eq. (25) has a zero denominator when $\delta_0=\delta_1=\delta_2=0$; the paper does not say what is done then.
- "A unique fifth-order polynomial $u_0(x)=\sum_{l=0}^{r-1}a_lx^l$" with $r=5$ has degree 4, and the "second-order polynomials" of $S_1$, $S_2$ have degree 1 (order-of-accuracy wording).
- Symbol reuse: $\chi_k$ (Eq. (20)) and $\chi$ (Eq. (27)); $\gamma_k$ for the prediction coefficients (Eqs. (9)–(10)) and the TENO measure (Eq. (17)); $\varepsilon=10^{-8}$ in both Eqs. (17) and (28).
- The caption of Algorithm 1 cites [54,55], the Riemann-solver papers, for the multi-D implementation.
- References: [8] and [43] are the same work (Jiang & Shu 1996) and [12] and [57] are the same work (Borges et al. 2008); [20] prints "P. Targeted" among the authors (the first title word); [10] prints no journal; [39] runs the title into "Appl. Compress. Euler Equ. 59 (2009) 2303–2321" with no journal; [26] prints no venue; [51] prints "J. Comput. Phy.s."; "Fig. 20 illustrate".

# Notation map

| Liang & Fu | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u_i$, $\bar u^l_i$ | $\bar u_i$ (level $l$) | cell averages |
| $u^L_{i+1/2}$, $u^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| $u^L_{k,i+1/2}$ | $u^{(k)}$ at $x_{i+1/2}$ | |
| $S_0$; $S_1$, $S_2$ | $S_0$ large; $S_1$, $S_2$ two-point (local numbering) | **numbering**: $S_0$ is not the most upwind stencil |
| $\beta_k$ | $\beta_k$ | Jiang–Shu, cell averages |
| $\tau=\lvert2\beta_0-(\beta_1+\beta_2)\rvert$ | $\tau_{\mathrm C}$ (local) | **collision**: not the WENO-Z $\tau_5=\lvert\beta_0-\beta_2\rvert$ |
| $\gamma_k$ (Eq. (17)) | $\gamma_k$ with $C=1$, $q=6$ | |
| $\gamma_k$ (Eqs. (9)–(10)) | $c_k$ (local) | **collision** with the TENO measure and with $\gamma$ |
| $\chi_k$ | $\chi_k$ | |
| $\chi$, $\chi_i$ (Eq. (27)) | $\chi_{\mathrm d}$ (local) | **collision** with $\chi_k$ |
| $\eta_k=\beta_k^2$, $\Delta\beta_{ij}$ | $\beta_k^2$, $\Delta\beta_{ij}$ (local) | |
| $\hat\delta_k$, $\tilde\delta_k$, $\delta_k$ | $\hat\delta_k$, $\tilde\delta_k$ (local), $\delta_k$ | |
| $C_{T,k}$, $C_{T0}$, $C_{T1}$ | $C_T$ per stencil, two values (local) | |
| $d_1$, $d_2$, $\omega_k$ | $d_k$, $\omega_k$ | |
| $\varepsilon$ | $\epsilon$ | $10^{-8}$ |
| $\varepsilon_r$, $\varepsilon_c$ | $\varepsilon_{\mathrm r}$, $\varepsilon_{\mathrm c}$ (local) | |
| $P_{l+1\to l}$, $P_{l\to l+1}$ | projection and prediction operators | Harten multiresolution |
| $\mathrm{Res}_A$, $\mathrm{CR}_1$, $\mathrm{CR}_2$ | root-level residual, compression ratios (local) | |
| $u,v,w$ | $v_1,v_2,v_3$ | |

# Reference list

The paper prints 59 references, numbered [1]–[59]. The list is merged
complete into the [bibliography](/bibliography.md), with `citedby`
including `liang-2026`. Refs. [8] = [43] (Jiang & Shu 1996) and [12] = [57]
(Borges et al. 2008) are printed duplicates and are merged as one work each.
The three Liang & Fu 2024 works are cited in the order [1] (J. Comput. Phys.
519:113386, the finite-difference CENO paper, not ingested), [23] (J.
Comput. Phys. 497:112618, the ingested [Liang & Fu (2024a)](/sources/liang-2024.md))
and [25] (Comput. Phys. Commun. 302:109236, the ingested
[Liang & Fu (2024b)](/sources/liang-2024-b.md)); they are matched by volume
and page, not by printed order, and [1] takes a new disambiguated key. Refs.
[22], [26] and [42] are the ingested [Takagi et al. (2022)](/sources/takagi-2022.md),
[Fu (2023)](/sources/fu-2023.md) and [Wan & Xia (2022)](/sources/wan-2022.md).
Refs. [2] and [48] are keyed by the surnames von Neumann and Asunción. Refs.
[10], [20], [26] and [39] print incomplete venues or garbled authors
(above), but every item is parsed.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunks 11–12 (2026-10-24/30). This source is cited on:

* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Converged ENO (CENO)](/methods/converged-eno.md)
* [ENO property](/definitions/eno-property.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Steady shock problems](/benchmarks/steady-shock-problems.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [WENO-Z weights](/methods/weno-z.md)
