---
type: Source
title: "Huang et al. (2025) — A new high-order RKDG method based on the TENO-THINC scheme for shock-capturing"
description: "Compact limiter for third-order RKDG: in cells flagged by Huang and Fu's TENO indicator, a compact BVD rule chooses between an equal-weight TENO combination of the three neighbouring DG polynomials and a quadratic fitted to THINC interface values, extended to 2D dimension by dimension on the modal coefficients."
resource: "doi:10.1016/j.jcp.2024.113459"
source_kind: paper
authors: [Huang H., Li X., Fu L.]
year: 2025
venue: "J. Comput. Phys. 520:113459"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Huang_A_new_high-order_RKDG_method_based_on_the_TENO-THINC_scheme.pdf"
tags: [dg, limiting, teno, thinc, bvd, troubled-cell]
timestamp: 2026-10-23T20:29:00Z
---

# Summary

Huang et al. (2025a) build a limiter for third-order ($N=2$, modal Legendre basis)
Runge–Kutta [discontinuous Galerkin](/methods/discontinuous-galerkin.md) methods on
uniform 1D and Cartesian 2D meshes, as a follow-up of
[Huang & Fu (2024)](/sources/huang-2024.md), whose TENO
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) it reuses with
$\epsilon=10^{-3}$, $q=6$ and $C_T=10^{-4}$.

In a troubled cell the "TENO-THINC limiter" ([WENO limiters for DG](/methods/weno-limiter-dg.md))
builds two candidate polynomials from the three-cell stencil. The TENO candidate is
the equal-weight average of those DG polynomials of $I_{i-1}$, $I_i$, $I_{i+1}$
that survive a second [TENO](/methods/targeted-eno.md) cut-off ($C_T=10^{-5}$,
$\epsilon=10^{-10}$); there are no linear weights. The THINC candidate is the unique
quadratic that keeps the cell integral and takes at both interfaces the
[THINC](/methods/thinc-reconstruction.md) values computed from the three cell
averages ($\beta_{\mathrm T}=1.6$). A compact
[BVD](/definitions/boundary-variation-diminishing.md) rule picks one of them by
comparing their total boundary variation against the *unlimited* DG traces of the
neighbours, rather than their reconstructed ones, so the whole limiter stays on the
three-cell stencil. Systems are limited in local characteristic variables. In 2D
the TENO and THINC weights computed on the trace polynomials along $y=y_j$
(respectively $x=x_i$) rebuild only the $x$-only (respectively $y$-only) modal
coefficients; the mixed coefficient is always the average of the two TENO
combinations. The paper is the DG transplant of the finite-difference
[TENO-THINC](/methods/teno-thinc.md) scheme of
[Takagi et al. (2022)](/sources/takagi-2022.md).

Tests (SSP-RK3, CFL 0.15, local Lax–Friedrichs flux) show third order with no cell
flagged on 1D and 2D [density waves](/benchmarks/density-wave-advection.md). Against
the Zhong–Shu simple WENO limiter driven by the same indicator they show sharper
discontinuities and more small-scale structure on [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
[Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md), 2D Riemann
[configuration 7](/benchmarks/two-dimensional-riemann-problems.md) and
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md). Evidence is visual
except for the accuracy tables, one timing table and troubled-cell counts.

# Version read

The archive file is the version of record (J. Comput. Phys. 520:113459, online 30
September 2024, issue 2025), 20 pages, all read (pp. 5–7 checked on the page
images). Page 1 matches the Crossref record. Label in this bundle: Huang et al.
(2025a); [Huang et al. (2025b)](/sources/huang-2025-b.md) is the deepMTBVD paper
of Huang, Cheng, Ying, Deng & Xiao, which cites this one.

# Key claims

Registry notation: DG degree $N=2$ (source $k$), DG polynomial $p_i$ on $I_i$
(source $p_i$ or $u^h_i$), modal coefficients $u^{(l)}_i$ (local, $u^{(0)}_i=\bar u_i$),
smoothness indicators $\beta_k$, TENO measures $\gamma_k$, $\chi_k$, $\delta_k$,
$C_T$, regularization $\epsilon$ (source $\varepsilon$, $\varepsilon_1$), THINC
steepness $\beta_{\mathrm T}$ (source $\beta$), normalized position $\varsigma$
(source $\alpha$). Page-local: $\omega_l$ the TENO-limiter weights (source $w_l$),
$\mathrm{TBV}_i$ the total boundary variation, $\epsilon^{\mathrm{BVD}}_{1,2}$ its
thresholds.

1. On the 1D density wave the indicator flags no cell: the WENO limiter, the TENO-THINC limiter and no limiter give identical errors, $L^1$ from $3.53\times10^{-7}$ ($N=100$) to $6.94\times10^{-10}$ ($N=800$), orders 2.99, 3.00, 3.00, and $L^\infty$ from $5.56\times10^{-7}$ to $1.09\times10^{-9}$, orders 3.00 (§5.1.1, Table 1). **Shown**
2. With the TENO-THINC limiter applied in every cell, the errors equal the unlimited ones, because the BVD rule detects no discontinuity and the TENO step leaves $p_i$ unchanged when all three stencils are smooth (§5.1.1, Table 2). **Shown**
3. On the 2D density wave ($[0,2]^2$, $t=2$) the indicator flags nothing: $L^1$ from $1.22\times10^{-4}$ ($20^2$) to $2.46\times10^{-7}$ ($160^2$), orders 2.98, 2.98, 2.99; $L^\infty$ orders 3.03, 3.00, 3.00 (§5.1.2, Table 3). **Shown**
4. The indicator separates "high-wavenumber physical fluctuations and genuine discontinuities from smooth regions" with one fixed parameter set for all cases, unlike the TVB-minmod and KXRCF indicators, whose critical parameter depends on the solution (abstract, §1, §3.1). **Stated** (the fixed parameters are used throughout §5; TVB and KXRCF are not run)
5. The limiter's cut-off $C_T=10^{-5}$ is chosen "as a balance of the good numerical robustness and the low dissipation property"; a larger $C_T$ in the indicator flags more cells, a larger $C_T$ in the limiter adds dissipation (§3.2.1). **Stated**
6. The limiter uses $\epsilon=10^{-10}$, not the indicator's $10^{-3}$, because there it "also acts as a cutoff of the smoothness measurements", after Castro et al. (§3.2.1). **Stated**
7. The THINC polynomial is fixed uniquely by three conditions, $\int_{I_i}p^{\mathrm{THINC}}_i\,dx=\int_{I_i}p_i\,dx$ and the THINC values at $x_{i\mp1/2}$, because a quadratic has three coefficients (§3.2.2, Eq. (21)). **Derived**
8. THINC is used only on locally monotone data: if $(\bar u_{i-1}-\bar u_i)(\bar u_i-\bar u_{i+1})<10^{-15}$ the interface value falls back to $\bar u_i$ (§3.2.2, after Takagi et al.). **Stated**
9. The BVD rule takes $p^{\mathrm{THINC}}_i$ if $\mathrm{TBV}^{\mathrm{TENO}}_i-\mathrm{TBV}^{\mathrm{THINC}}_i>\max\big(\epsilon^{\mathrm{BVD}}_1,\epsilon^{\mathrm{BVD}}_2(\mathrm{TBV}^{\mathrm{THINC}}_i+\mathrm{TBV}^{\mathrm{TENO}}_i)\big)$, $\epsilon^{\mathrm{BVD}}_1=10^{-10}$, $\epsilon^{\mathrm{BVD}}_2=10^{-3}$, where $\mathrm{TBV}_i=\lvert p^{\bullet}_i(x_{i-1/2})-p_{i-1}(x_{i-1/2})\rvert+\lvert p^{\bullet}_i(x_{i+1/2})-p_{i+1}(x_{i+1/2})\rvert$ uses the unlimited neighbour polynomials (Eqs. (22)–(24)). The BVD of Jiang et al. (2021) "depends on more stencils, as it requires the reconstructed values of neighboring cells", and the new rule is "significantly simpler than its predecessors" (§1, §3.2.3). **Stated**
10. Hermite WENO limiters "are not consistent" between 1D and 2D because they use different basis functions per dimension; the dimension-by-dimension construction "could potentially serve as a general approach" to extend 1D limiters to 2D (§1, §4). **Stated**
11. In 2D the mixed coefficient $u^{(3)}_{ij}$ is always rebuilt by TENO, never by THINC, "to enhance robustness", and no BVD rule is applied to it (§4.2.2–4.2.3). **Stated**
12. Sod and Lax (100 points): the limiter is oscillation-free and less dissipative than the simple WENO limiter, and the BVD rule labels the genuine discontinuities "accurately" (§5.2, Figs. 1–2). **Shown** (visual)
13. Lax problem: 163.07 s with the WENO limiter, 172.08 s with the TENO-THINC limiter (Table 4); the authors conclude that efficiency "is not affected obviously" since troubled cells are a small part of the domain. No hardware is stated. **Shown** *(compiler check, not in the sources: the ratio is 1.055, an overhead of about 5.5%.)*
14. Woodward–Colella (400 points, reference WENO5-JS on 4000): the TENO-THINC limiter resolves the density peak "much more effectively" and the shocks more sharply (§5.3, Fig. 3). **Shown** (visual)
15. Shu–Osher (500 points, reference WENO5-JS on 2000): less dissipative in $2\le x\le5$ and $7.4\le x\le9.5$, similar in $5.6\le x\le7.4$; the improvement is "not as obvious as in other cases", as for the finite-difference TENO-THINC schemes (§5.4, Fig. 4). **Shown** (visual)
16. Double Mach reflection ($1200\times300$, $1600\times400$): both limiters are oscillation-free and the TENO-THINC limiter resolves "much richer small-scale structures"; near $x=2.6$, $y=0.1$ the WENO limiter gives a "better large vortical structure", which the authors attribute to the inviscid problem having no convergent solution (§5.5, Fig. 5). **Shown** (visual; the attribution **Stated**)
17. On $1200\times300$ the indicator flags 34 681 cells (9.63% of the domain) and the BVD rule selects THINC in 6476 (1.8% of the domain) (§5.5, Fig. 6). **Shown** *(compiler check, not in the sources: $34\,681/360\,000=9.63\%$ and $6476/360\,000=1.80\%$, that is 18.7% of the flagged cells.)*
18. 2D Riemann configuration 7 ($1000^2$, $1500^2$, $t=0.25$): richer vortical structures (§5.6, Fig. 7). **Shown** (visual)
19. Rayleigh–Taylor ($150\times600$, $300\times1200$, $\gamma=5/3$): "significantly richer small-scale structures", with the flow symmetry broken by round-off because of the low dissipation (§5.7, Fig. 8; see [symmetry preservation](/properties/symmetry-preservation.md)). **Shown** (visual)
20. The limiter is "straightforward to implement into existing RKDG codes, as it only relies on compact stencils"; unstructured meshes are future work (§6). **Stated**
21. RKDG on unstructured meshes and with arbitrary order addresses "the main limitations of finite-difference and finite-volume methods, respectively" (§1). **Stated**

Indicator and limiter, as printed. Eq. (11): $\beta_l=\sum_{s=1}^2\int_{I_i}\Delta x^{2s-1}\big(p_l^{(s)}(x)\big)^2dx$, $l=i-1,i,i+1$, with $\gamma_l=(\beta_l+\epsilon)^{-q}$, $\chi_l=\gamma_l/\sum_m\gamma_m$, and $I_i$ troubled iff $\chi_i<C_T$. In the limiter, $\omega_l=\delta_l/\sum_m\delta_m$ unless all three $\delta_l=1$, when $p_i$ is kept, and $p^{\mathrm{TENO}}_i=\omega_{i-1}p_{i-1}+\omega_ip_i+\omega_{i+1}p_{i+1}$ (Eq. (19)). THINC: $\hat u_{i+1/2}=f_{\mathrm m}+f_{\mathrm j}\frac{\mathcal A+\mathcal T}{1+\mathcal A\mathcal T}$, $\mathcal A=\frac{\mathrm{sgn}(\varsigma)}{\mathcal T}\frac{\mathcal B-1}{\mathcal B+1}$, $\mathcal B=e^{\lvert\varsigma\rvert\beta_{\mathrm T}}$, $\mathcal T=\tanh(\beta_{\mathrm T}/2)$, $\varsigma=(\bar u_i-f_{\mathrm m})/f_{\mathrm j}$, $f_{\mathrm m}=\tfrac12(\bar u_{i+1}+\bar u_{i-1})$, $f_{\mathrm j}=\tfrac12(\bar u_{i+1}-\bar u_{i-1})$ (Eq. (20)). Time step: $\Delta t\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)=0.15$ (Eq. (37)).

# Printed slips

- Eq. (11) prints the integration domain $I_i$ for all three polynomials $p_{i-1},p_i,p_{i+1}$, so the neighbour polynomials are extrapolated into $I_i$. The same indicator in [Huang & Fu (2024)](/sources/huang-2024.md), Eq. (32), integrates each $u_n$ over its own cell $I_n$, and §3.1 says the indicator of that paper is reused. One of the two printed domains differs from what was run; this paper alone does not decide which.
- Eq. (19) combines the full neighbour polynomials, means included, and no shift to $\bar u_i$ is printed in 1D, while the 2D Eqs. (27)–(29) recombine only the non-constant modes and keep $u^{(0)}$. *(Compiler check, not in the sources: as printed, the average of $p^{\mathrm{TENO}}_i$ over $I_i$ is $\sum_l\omega_l\frac1{\Delta x}\int_{I_i}p_l\,dx$, which differs from $\bar u_i$ in general when $\omega_{i\pm1}\ne0$, so the printed 1D formula is not conservative.)*
- §3.3: "hyperbolic conversion laws"; "One-dimensional systems of conservation laws are introduced can be written as".
- References: [3] "R.J. LeVeque, R.J. Leveque" for a single-author book; [58] and [60] printed without volume.

# Notation map

| Huang, Li & Fu | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ | $N$ | DG degree, here 2 |
| $v^{(i)}_l$, $c_l$; $v_l$, $a_l$ | scaled Legendre basis and its norms (local) | $v_2=((x-x_i)/\Delta x)^2-1/12$; **collision** of $a_l$ with the wave speed |
| $u^{(l)}_i$, $u^{(l)}_{ij}$ | $u^{(l)}_i$ (local) | modal coefficients; $u^{(0)}=\bar u$ |
| $u^h_i$, $p_i(x)$ | $u_h\vert_{I_i}$, $p_i$ | |
| $u^{L,R}_{i+1/2}$, $\hat f_{i+1/2}$ | $u^\mp_{i+1/2}$, $\hat f_{i+1/2}$ | local Lax–Friedrichs flux in §5 |
| $\beta_l$, $\gamma_l$, $\chi_l$, $\delta_l$, $C_T$ | $\beta_k$, $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$ | $\gamma_l$ without the TENO constant $C$ and without $\tau$ |
| $\varepsilon$, $\varepsilon_1$ | $\epsilon$ | $10^{-3}$ (indicator), $10^{-10}$ (limiter) |
| $w_l$, $w^{(x,\mathrm{TENO})}$, $w^{(x,\mathrm{THINC})}$ | $\omega_l$ and direction-wise weights (local) | the 2D THINC weights solve Eq. (31) and are not constrained to $[0,1]$ |
| $\beta$ (THINC) | $\beta_{\mathrm T}$ | **collision** with $\beta_k$ |
| $\alpha$, $\bar u_+$, $\bar u_-$, $A$, $B$, $T$ | $\varsigma$, $f_{\mathrm m}$, $f_{\mathrm j}$, $\mathcal A$, $\mathcal B$, $\mathcal T$ | **collision** of $\alpha$ with $\alpha_k$ and of $\bar u_\pm$ with one-sided states |
| $\mathrm{TBV}_i$, $\varepsilon^{\mathrm{BVD}}_{1,2}$ | $\mathrm{TBV}_i$, $\epsilon^{\mathrm{BVD}}_{1,2}$ (local) | |
| $R_i$, $R_i^{-1}$, $\tilde{\mathbf U}_i$ | $R_i$, $L_i$, $\zeta$ | the state defining $R_i$ is not stated |
| $S^{(x)}_{\max}$ | $a^{(1)}$ | |
| $\gamma$ (gas), $u$, $v$ | $\gamma$, $v_1$, $v_2$ | **collision** of $\gamma$ with $\gamma_k$ |

# Reference list

The paper prints 68 references, numbered [1]–[68]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `huang-2025`. Ref.
[1] is the ingested [Huang & Fu (2024)](/sources/huang-2024.md) and ref. [54] the
ingested [Takagi et al. (2022)](/sources/takagi-2022.md). Ref. [31] (Huang, Liang &
Fu, Commun. Comput. Phys. 33:1106), printed as the only Huang 2023 item, is the
ingested [Huang et al. (2023)](/sources/huang-2023-b.md), matched by volume and page; ref. [57] (Li, Lv & Fu, Int. J. Multiph. Flow 173) is a
different work from the planned source of the same key and takes a disambiguated
key. Five Fu 2019 items and the Cockburn 1989 and Qiu 2005 pairs are suffixed in
printed order and matched by volume and page; ref. [58] is printed without its
volume. No printed duplicates; no item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunk 11 (2026-10-24). This source is cited on:

* [Boundary variation diminishing (BVD)](/definitions/boundary-variation-diminishing.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [TENO-THINC](/methods/teno-thinc.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO limiters for discontinuous Galerkin](/methods/weno-limiter-dg.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
