---
type: Source
title: "Huang et al. (2025) — A new high-order RKDG method based on the TENO-THINC scheme for shock-capturing"
description: "Third-order modal RKDG shock capturing on Cartesian grids: a TENO troubled-cell indicator flags cells, a TENO-THINC limiter replaces the troubled polynomial with a compact boundary-variation-diminishing choice between a TENO stencil combination and a THINC jump, tested on inviscid Euler problems against a WENO limiter."
resource: "doi:10.1016/j.jcp.2024.113459"
source_kind: paper
authors: [Huang H., Li X., Fu L.]
year: 2025
venue: "J. Comput. Phys. 520:113459"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Computational_Physics_Huang_A_new_high-order_RKDG_method_based_on_the_TENO-THINC_scheme.pdf"
tags: [shock-capturing, dg, weno, numerical-dissipation, high-order]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Huang et al. (2025) build a shock-capturing limiter for the third-order
Runge–Kutta discontinuous Galerkin method with a modal Legendre basis
($N=2$) on uniform 1-D and 2-D Cartesian grids. The paper belongs to
shock-capturing numerics; no turbulent flow, LES or closure is computed.
Its relevance to the bundle is the low-[dissipation](/properties/numerical-dissipation.md)
handling of discontinuities in the
[DG](/methods/discontinuous-galerkin-spectral-element-method.md) family (a
modal RKDG, not DGSEM), next to the
[subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
alternatives the introduction cites (§1).

The method has three parts. A TENO
[troubled-cell indicator](/definitions/shock-sensor.md), from the authors'
earlier work (Huang & Fu 2024), computes smoothness measures of the cell's
own polynomial and its two neighbours over the cell, separates scales with
a power $q=6$ and flags the cell when its own normalized measure falls
below a cutoff $C_T=10^{-4}$. A TENO-THINC limiter then forms two
candidates: a [TENO](/methods/weno-scheme.md)-type equal-weight combination
of the retained neighbour polynomials ($C_T=10^{-5}$), and a THINC
(tangent of hyperbola) jump reconstruction of the interface values,
converted back to a quadratic that keeps the cell average. A compact
boundary-variation-diminishing (BVD) selector picks THINC when its total
boundary variation against the unlimited neighbour polynomials is smaller
than TENO's by a threshold. Systems are limited in characteristic
variables; 2-D is handled direction by direction on the modal
coefficients, with the mixed mode always limited by TENO.

The tests are inviscid Euler problems: linear advection (third order kept,
the indicator never fires), the Sod and Lax shock tubes, the
Woodward–Colella blast waves, the Shu–Osher problem, double Mach
reflection, 2-D Riemann configuration 7 and the single-mode inviscid
[Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-mixing.md), the
last a shock-capturing test and not a turbulent mixing layer. Against the
simple WENO limiter of Zhong & Shu (2013) with the same indicator,
TENO-THINC gives sharper discontinuities and richer small-scale structure
at a small extra cost. The introduction cites TENO as an
[implicit LES](/definitions/implicit-les.md) model and a TENO limiter for
the [spectral difference method](/methods/spectral-difference-method.md);
neither is used here.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 520 (2025) 113459;
received 19 April 2024, available online 30 September 2024); 20 pages, all
read, with pp. 5–6 checked visually. Page 1 agrees with Crossref.

# Key claims

1. The TVB minmod and KXRCF troubled-cell indicators depend on a solution-dependent critical parameter and need case-by-case tuning; popular limiters "fail to guarantee the high-order property in the smooth regions" (Abstract, §1). **Stated**
2. A WENO finite-volume reconstruction used as an RKDG limiter (Qiu & Shu) needs $2N+1$ neighbouring cells for degree-$N$ polynomials (§1). **Stated**
3. The TENO indicator, with $\epsilon_{\mathrm{IS}}=10^{-3}$, $q=6$, $C_T=10^{-4}$, separates high-wavenumber fluctuations and discontinuities from smooth regions "with a set of uniform parameters for all cases" (§3.1, Eqs. 11–14). **Shown** (one parameter set for every test)
4. In the smooth 1-D and 2-D accuracy tests the indicator flags no cell; errors with the WENO limiter, with TENO-THINC and with no limiter are identical, and the scheme keeps third order (Tables 1, 3). **Shown**
5. With the TENO-THINC limiter forced on everywhere, the 1-D accuracy errors still equal those of the unlimited scheme: the BVD never selects THINC in smooth flow and TENO keeps the polynomial when all three stencils are smooth (§5.1.1, Table 2). **Shown**
6. 1-D accuracy: $L_1$ errors 3.53E-07, 4.43E-08, 5.55E-09, 6.94E-10 on $N_x=100$–800 (orders 2.99, 3.00, 3.00); $L_\infty$ 5.56E-07 to 1.09E-09 (orders 3.00) (Table 1). **Shown**
7. 2-D accuracy: $L_1$ errors 1.22E-04 to 2.46E-07 on $20^2$–$160^2$ (orders 2.98–2.99); $L_\infty$ 2.03E-04 to 3.87E-07 (orders 3.00–3.03) (Table 3). **Shown**
8. The limiter's cutoff ($10^{-5}$, Eq. 17) differs from the indicator's ($10^{-4}$) because a larger indicator cutoff flags more cells while a larger limiter cutoff adds dissipation; $10^{-5}$ balances robustness and low dissipation (§3.2.1). **Stated**
9. The limiter's regularizer $10^{-10}$ differs from the indicator's $10^{-3}$ "since it also acts as a cutoff of the smoothness measurements" (§3.2.1). **Stated**
10. The new BVD needs only the compact three-cell stencil and is "significantly simpler" than its predecessors (Sun et al. 2016; Jiang et al. 2021), because the neighbour interface values come from the unlimited polynomials, not from reconstructed ones (§3.2.3, Eq. 24). **Stated**
11. THINC is valid only in locally monotone regions; if $(\bar u_{i-1}-\bar u_i)(\bar u_i-\bar u_{i+1})<10^{-15}$ the first-order interface value is used (§3.2.2). **Stated**
12. Hermite WENO limiters are "not consistent" between 1-D and 2-D because their bases differ; the dimension-by-dimension strategy removes the inconsistency and "could potentially serve as a general approach" (§1, §4). **Stated**
13. Sod and Lax (100 cells): TENO-THINC is oscillation-free and less dissipative than the WENO limiter, and the BVD flags the genuine discontinuities (§5.2, Figs. 1–2). **Shown**
14. Cost on Lax's problem: 163.07 s (WENO) against 172.08 s (TENO-THINC), since troubled cells are few and THINC/BVD act only there; hardware not stated (§5.2, Table 4). **Shown**
15. Blast waves (400 cells; reference WENO5-JS on 4000 points): TENO-THINC resolves the density peak "much more effectively" and the shocks more sharply (§5.3, Fig. 3). **Shown**
16. Shu–Osher (500 cells): TENO-THINC is less dissipative in parts of the wave train and similar elsewhere; the gain is smaller than in the other cases, as for the finite-difference TENO-THINC (§5.4, Fig. 4). **Shown**
17. Double Mach reflection ($1200\times300$, $1600\times400$): TENO-THINC resolves richer small-scale structures; near $x=2.6$, $y=0.1$ the WENO limiter gives "the better large vortical structure", attributed to the inviscid problem having no convergent solution (§5.5, Fig. 5). **Shown**
18. Double Mach reflection at $1200\times300$: 34 681 troubled cells (9.63%), of which the BVD selects THINC in 6476 (1.8% of the domain, 18.7% of the troubled cells) (§5.5, Fig. 6). **Shown**
19. 2-D Riemann configuration 7 ($1000^2$, $1500^2$): richer vortical structures with TENO-THINC (§5.6, Fig. 7). **Shown**
20. Rayleigh–Taylor instability ($150\times600$, $300\times1200$): "significantly richer small-scale structures"; the low dissipation lets round-off break the symmetry (§5.7, Fig. 8). **Shown**
21. The limiter is "straightforward to implement into existing RKDG codes" because it relies only on compact stencils; unstructured meshes are future work (§6). **Stated**
22. TENO schemes have been validated for gas dynamics, multiphase flows, MHD, detonation, fluid–structure–acoustics interaction and turbulence simulation (§1). **Stated**
23. "There is no essential difference" in the TENO scheme between modal and nodal DG bases (§1). **Stated**

The indicator and limiter, translated (cell $i$, neighbour polynomials
$p_k$, $k\in\{i-1,i,i+1\}$, cell width $h$):
$$\mathrm{IS}_k=\sum_{s=1}^{2}\int_{I_i}h^{2s-1}\Big(\frac{d^sp_k}{dx^s}\Big)^2dx,\qquad \gamma^{\mathrm T}_k=\frac{1}{(\mathrm{IS}_k+\epsilon_{\mathrm{IS}})^{q}},\qquad \chi^{\mathrm T}_k=\frac{\gamma^{\mathrm T}_k}{\sum_m\gamma^{\mathrm T}_m},\qquad \delta^{\mathrm T}_k=\begin{cases}0,&\chi^{\mathrm T}_k<C_T\\1,&\text{otherwise}\end{cases}$$
(cell troubled iff $\delta^{\mathrm T}_i=0$), and, unless all $\delta^{\mathrm T}_k=1$,
$p_i^{\mathrm{TENO}}=\sum_k\mathsf w_kp_k$ with
$\mathsf w_k=\delta^{\mathrm T}_k/\sum_m\delta^{\mathrm T}_m$ (Eqs. 15–19). The BVD rule (Eq. 24)
selects THINC when
$\mathrm{TBV}^{\mathrm{TENO}}-\mathrm{TBV}^{\mathrm{THINC}}>\max(10^{-10},10^{-3}(\mathrm{TBV}^{\mathrm{THINC}}+\mathrm{TBV}^{\mathrm{TENO}}))$,
with THINC steepness $\beta_{\mathrm{TH}}=1.6$. In 1-D, Eq. (19)
combines whole neighbour polynomials, and the paper states no step that
keeps the cell average of the TENO candidate, whereas it enforces it for
THINC (Eq. 21) and in 2-D modifies only the modes $l\ge1$ *(compiler
check, not in the sources)*.

# Printed slips

- §3.3: "one-dimensional scalar hyperbolic conversion laws" (for conservation), and in the same paragraph the garbled "One-dimensional systems of conservation laws are introduced can be written as".
- Ref. [3] prints the author twice: "R.J. LeVeque, R.J. Leveque".
- Refs. [58] ("J. Comput. Phys. (2024) 113156") and [60] ("Arch. Hist. Exact Sci. (1979) 129–160") print no volume.
- $\beta$ denotes both the smoothness measure (Eq. 11) and the THINC steepness (Eq. 20); $\gamma$ both the scale-separated measure and the ratio of specific heats (notation clashes, not errors).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ (polynomial degree), $\mathbb P^k$ | $N$ | $N=2$ throughout |
| $N$, $N_x\times N_y$ (cells) | $N_x$, $N_x\times N_y$ | **collision:** a grid count, not the degree |
| $\Delta x$, $\Delta y$ | $h$ | uniform cells |
| $v_l^{(i)}$, $u_i^{(l)}$ | (modal Legendre basis and coefficients, page-local) | $l=0$ is the cell average |
| $p_i(x)$, $u^h$ | (cell polynomial, page-local) | **collision:** $p$ is not the pressure in §3 |
| $\bar u_i$, $\bar u_\pm$ | (cell average; half-sum and half-difference of neighbour averages) | **collision:** bar is not the LES filter |
| $\beta_l$ (Eq. 11) | $\mathrm{IS}_k$ | registry §11 smoothness indicator; the source's cell index $l$ is written $k$ (the source's $l$ also numbers the modes) |
| $\gamma_l$, $\chi_l$ | $\gamma^{\mathrm T}_k$, $\chi^{\mathrm T}_k$ (scale-separated and normalized measures, page-local) | **collision:** $\gamma$ is not the ratio of specific heats here |
| $\varepsilon$, $\varepsilon_1$ | $\epsilon_{\mathrm{IS}}$ (page-local) | $10^{-3}$ (indicator), $10^{-10}$ (limiter); **collision:** not the dissipation rate |
| $q$, $C_T$, $\delta_l$ | $q$, $C_T$, $\delta^{\mathrm T}_k$ (page-local) | |
| $w_l$ | $\mathsf w_k$ | normalized weights, equal over retained stencils |
| $\beta$ (THINC), $\alpha$, $A$, $B$, $T$ | $\beta_{\mathrm{TH}}$ and auxiliary quantities (page-local) | **collision:** $\alpha$ is not the DG blending factor, $B$ not the log-law intercept |
| $\hat u_{i\pm1/2}$ | (THINC interface values) | hat is not a test filter |
| $\mathrm{TBV}$, $\varepsilon^{\mathrm{BVD}}_{1,2}$ | same (page-local) | total boundary variation and thresholds |
| $R_i$ | (right-eigenvector matrix) | **collision:** not $R_{ij}$ |
| $\rho$, $u$, $v$, $p$, $E$, $\gamma$ | $\rho$, $u$, $v$, $p$, $E$, $\gamma$ | Euler; $\gamma=1.4$ ($5/3$ for Rayleigh–Taylor) |
| $\hat f_{i\pm1/2}$ | $f^*$ | local Lax–Friedrichs flux |

# Reference list

68 printed references, numbered style, no DOIs printed. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. No printed duplicates; ref. [3] doubles its author, and refs. [58]
and [60] print no volume. Ref. [1] is the bundle source
[Huang & Fu (2024)](/sources/huang-2024.md) and ref. [54] is
[Takagi et al. (2022)](/sources/takagi-2022.md). Refs. [33] (Li, Fu &
Adams 2021), [57] (Li, Lv & Fu 2024) and [58] (Chen & Fu 2024) are works distinct from the bundle sources keyed li-2021, li-2024 and chen-2024 and are keyed `li-2021-h`, `li-2024-g` and `chen-2024-d`.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
