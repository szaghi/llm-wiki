---
type: Source
title: "Liang & Fu (2024) — A new type of non-polynomial based TENO scheme for hyperbolic conservation laws"
description: "Fifth-order finite-difference TENO variant whose TENO5 flags only select one of six target stencils (5, 4 or 3 points), on which a Gaussian RBF reconstruction of the primitive with an adaptive shape parameter gives the flux; flagged discontinuities take the TENO-THINC tanh flux, with no linear weights."
resource: "doi:10.1016/j.jcp.2023.112618"
source_kind: paper
authors: [Liang T., Fu L.]
year: 2024
venue: "J. Comput. Phys. 497:112618"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Liang_A_new_type_of_non-polynomial_based_TENO_scheme_for_hyperboli.pdf"
tags: [teno, rbf, finite-difference, low-dissipation, thinc, spectral-analysis]
timestamp: 2026-10-23T23:55:00Z
---

# Summary

Liang & Fu (2024a) propose a fifth-order finite-difference scheme of the
[TENO](/methods/targeted-eno.md) family in which non-polynomial reconstructions
replace the polynomial candidates. The authors argue that polynomials represent
sharp transitions poorly. They also criticize earlier
[RBF-based WENO](/methods/rbf-weno.md) for three things: a fixed basis
everywhere, linear weights that are costly or may not exist for a non-polynomial
basis, and shape-parameter optimization by ratios of high derivatives, which is
unstable at critical points.

The scheme has three parts.

- **Stencil selection.** The TENO5 scale separation and cut-off ($q=6$,
  $C_T=10^{-5}$) only classify the three 3-point candidates. Their flags
  $(\delta_0,\delta_1,\delta_2)$ select one of six target stencils of 5, 4, 4,
  3, 3, 3 points, each using as many smooth points as possible without crossing
  the non-smooth region. The flux is the single reconstruction on the target
  stencil: there is no convex combination and no linear weights, and the order
  falls from 5 to 4 to 3.
- **Gaussian RBF reconstruction.** Gaussians centred at the interfaces
  interpolate the primitive of the flux. Taylor truncation at
  $O(\lambda_{\mathrm s}^2\Delta x^2)$ gives explicit fluxes: the polynomial
  fluxes plus $\lambda_{\mathrm s}^2\Delta x^2$-weighted zero-sum correction
  stencils.
- **Adaptive shape parameter.** The shape parameter
  $\lambda_{\mathrm s}\in[3,6]$ is set by a Ren et al.-type smoothness ratio.

In cells flagged as genuine discontinuities by the detector of Liang et al.
(2022), the flux is the two-steepness tanh interpolation of that work
([TENO-THINC](/methods/teno-thinc.md)).

The evidence is numerical: an approximate dispersion relation, fifth order on a
Gaussian pulse, and 1D and 2D Euler benchmarks against WENO5-Z, TENO5 and TENO6.
The scheme costs about $1.4\times$ TENO5 and $1.5\times$ WENO5-Z on the double
Mach reflection, and the authors report sharper or more resolved structures on
every test. No theorem is proved. The paper is distinct from Liang & Fu (2024b)
([liang-2024-b](/sources/liang-2024-b.md)), the TENO and skew-symmetric
splitting scheme.

# Version read

Version of record (Elsevier typeset, "Journal of Computational Physics 497
(2024) 112618"), 21 pages, all read. Pages 4, 5, 8, 9 and 13 were checked
visually for equations that the text extraction garbled. Page 1 matches
Crossref (title, authors, venue, DOI). It was received 28 June 2023 and
published online 31 October 2023. Equation, table and figure numbers are those
of this version.

# Key claims

Registry notation (see the notation map): weights $\omega_k$ (source $w_k$),
indicators $\beta_k$ (source $\beta_{k,r}$), regularization $\epsilon$ (source
$\varepsilon$), Gaussian shape parameter $\lambda_{\mathrm s}$ (source
$\lambda$), shape constants $\lambda_0$, $\lambda_\Delta$ (source $\alpha_1$,
$\alpha_2$), and, as on [adaptive TENO](/methods/adaptive-teno.md), mapping
$\varphi$ (source $g$), measure $\mu_d$ (source $m$), Ren-type ratio $\sigma_i$
(source $\eta_i$), threshold $C_r$ (source $c_r$) and regularization
$\epsilon_\sigma$ (source $\varepsilon$ of Eq. 31), discontinuity flag $\zeta^{\mathrm D}_i$ (source $\zeta_i$). The
candidate stencils keep the source's TENO numbering, $S_0=\{i-1,i,i+1\}$
central, $S_1=\{i,i+1,i+2\}$, $S_2=\{i-2,i-1,i\}$, not the registry's
upwind-first order.

1. Polynomial interpolation, the building block of WENO and TENO fluxes, is "not suitable to represent the flow scale with sharp transitions such as high-wavenumber fluctuations or discontinuities" (Abstract, §1). **Stated**
2. Existing non-polynomial WENO variants have three drawbacks: one fixed basis over the whole domain, complicated and time-consuming linear weights for a non-polynomial basis "especially when the global accuracy order is larger than third", and unstable division of higher-order derivatives in shape-parameter optimization, especially at critical points (§1). **Stated**
3. In classical TENO5, when any candidate is non-smooth, the renormalized combination of the other two "will not achieve any accuracy order" beyond that of a single candidate, because the $d_k$ are designed for the three-stencil fifth-order combination (§3.1). **Stated**
4. For non-polynomial reconstructions the linear weights "may become challenging to calculate or even do not exist" (§3.1), or "may become negative for some mesh typologies" (§5). **Stated**
5. The six flag combinations of $(\delta_0,\delta_1,\delta_2)$ define six target stencils, each using as many smooth data as possible without crossing the non-smooth region; near discontinuities the reconstruction "recursively degenerate[s] from fifth-order to fourth-order until the third-order reconstruction" (§3.1, Fig. 2). **Stated** (the orders are **Derived** in Eq. 29). *(Compiler check, not in the sources: the all-zero combination, which the paper does not list, cannot occur, since $\sum_k\chi_k=1$ forces $\max_k\chi_k\ge1/3>C_T$.)*
6. On a target stencil $\{I_{i-r_{\mathrm L}},\dots,I_{i+r_{\mathrm R}}\}$ the Gaussian RBF interpolant of the primitive satisfies $R(x)=H(x)+O(\Delta x^{r_{\mathrm L}+r_{\mathrm R}+2})$ and $R'(x)=h(x)+O(\Delta x^{r_{\mathrm L}+r_{\mathrm R}+1})$ (Eqs. 23–24). **Stated**
7. The truncated RBF fluxes of Eq. (25) have the error expansions of Eq. (29): fifth order on the 5-point stencil, fourth order on the two 4-point stencils, third order on the three 3-point stencils, with the $\lambda_{\mathrm s}^2$ terms entering at the same power of $\Delta x$ as the polynomial truncation terms (§3.2, Eqs. 26–29). **Derived** *(Compiler check, not in the sources: substituting Taylor expansions of the cell averages into Eq. (25) reproduces the leading terms of Eq. (29) for all six fluxes; at $\lambda_{\mathrm s}=0$ the fluxes are the fifth-order upwind flux, the two fourth-order fluxes and the three third-order candidate fluxes of Eq. (8). See Printed slips for the $\Delta x^6$ term of $R'_1$.)*
8. The shape parameter is $\lambda_{\mathrm s}=\lambda_0+\lambda_\Delta\big(1-\varphi(\mu_d)\big)$ with $\varphi(\mu_d)=(1-\mu_d)^4(1+4\mu_d)$, $\mu_d=1-\min\big(1,\min(\sigma_{i-1},\sigma_i,\sigma_{i+1})/C_r\big)$ and $\sigma_i=\dfrac{\lvert2(f_i-f_{i-1})(f_{i+1}-f_i)\rvert+\epsilon_\sigma}{(f_i-f_{i-1})^2+(f_{i+1}-f_i)^2+\epsilon_\sigma}$, $\epsilon_\sigma=10^{-40}$; $C_r=0.4$ and $\lambda_0=\lambda_\Delta=3$ are "determined by numerical experiments" (Eqs. 30–32). **Stated**
9. For $\mu_d\approx0$ the kernel is flat ($\lambda_{\mathrm s}\to\lambda_0$), suited to smooth low-wavenumber scales. For $\mu_d\approx1$ it is sharp ($\lambda_{\mathrm s}\to\lambda_0+\lambda_\Delta$), suited to high-wavenumber fluctuations (§3.2). **Stated**
10. As $\Delta x\to0$ the Gaussian RBF reconstruction "will degenerate to the classical polynomial reconstruction with strong numerical robustness and stability" (§3.2). **Stated**
11. The [approximate dispersion relation](/definitions/approximate-dispersion-relation.md) on 128 points shows dispersion and dissipation of the nonlinear RBF scheme better than TENO5 and WENO5-Z, and "the background linear scheme can be restored exactly up to an intermediate wavenumber" (§3.2, Fig. 3). **Shown**
12. In cells flagged by the detector (Eq. 34) the flux is the tanh interpolation of Eq. (35) with $\mathcal A=0.91$, raised to $\mathcal A=1.23$ where the stricter sensor of Eq. (36) also holds, "the same value" as in Liang et al. (2022) (§3.3). **Stated** (background)
13. Eq. (35) "cannot be deployed" where $(f_{i+1}-f_i)(f_i-f_{i-1})\le\epsilon=10^{-15}$; the first-order flux $\hat f_{i+1/2}=f_i$ is used there (§3.3). **Stated**
14. The very low dissipation of the present scheme and of TENO5 can break flow symmetry through round-off, so the symmetry-preserving technique of Fleischmann et al. is used (§4). **Stated**
15. Gaussian pulse advection: "the desired fifth-order convergence is achieved without order degeneration" in $L_\infty$ (§4.1, Fig. 4; the grid sequence is only in the figure). **Shown**
16. Sod (100 points, $t=0.2$) and Lax (100 points, $t=0.14$): all schemes agree with the exact solution; the present scheme captures Sod's shock and contact more sharply and resolves the Lax rarefaction better (§4.2, Figs. 5–6). **Shown**
17. Interacting blast waves (400 points, $t=0.038$, Roe flux with entropy fix): TENO5 needs $C_T=10^{-4}$ to be stable. The present scheme captures shocks as sharply as WENO5-Z and TENO5 and resolves the density peak better (§4.3, Fig. 7). **Shown**
18. Shu–Osher (200 cells, $t=1.8$): "significantly better resolutions than WENO5-Z and TENO5" of shocklets and high-wavenumber density fluctuations (§4.4, Fig. 8). **Shown**
19. Double Mach reflection: better slip-line structures than WENO5-Z, TENO5 and "even the six-point low-dissipation TENO6" at $400\times100$ and $1000\times250$; the $400\times100$ result is similar to WENO5-Z and TENO5 at $1000\times250$ (§4.5, Figs. 9–10). **Shown**
20. Double Mach reflection wall times (Table 1): $400\times100$: WENO5-Z 36.51 s, TENO5 40.04 s, TENO6 45.00 s, present 55.23 s; $1000\times250$: 593.16 s, 630.89 s, 717.20 s, 895.52 s. "The cost increase from deploying the present scheme is not significant". Hardware is not stated (§4.5). **Shown** (the judgement is **Stated**) *(Compiler check, not in the sources: present/TENO5 = 1.38 and 1.42, present/WENO5-Z = 1.51 on both grids.)*
21. Rayleigh–Taylor ($64\times256$, $t=1.95$): more small-scale structures than WENO5-Z and TENO5, and premultiplied kinetic-energy spectra more energetic at small scales (§4.6, Figs. 11, 12a). **Shown**
22. Kelvin–Helmholtz ($400\times400$, $t=0.5$): WENO5-Z is more dissipative; the present scheme preserves total kinetic energy better than WENO5-Z and TENO5, and its spectrum is more energetic "for most of the length scales" (§4.7, Figs. 12b, 13). **Shown**
23. 2D Riemann configurations 3, 8 and 11 ($800\times800$): more vortical structures than WENO5-Z, TENO5 and TENO6 (§4.8, Figs. 14–16). **Shown**
24. All cases run "without the necessity of parameter tuning case by case" for the present scheme (Abstract, §5). **Stated** (consistent with §4, where only TENO5's $C_T$ changes)
25. RBF reconstructions depend on distance only, which suits unstructured meshes; the authors suggest enlarging directional stencils to the target order, or combining RBF with CWENO or unstructured TENO (§5). **Stated**

# Printed slips

- §1: "Borgers et al. [8]"; ref. [8] is Borges, Carmona, Costa & Don.
- Eq. (16): $R(x)=\sum_n\alpha_n\Phi(\boldsymbol x)$ does not index the kernel by $n$, although $\Phi(\boldsymbol x)=\phi(\lVert x-x_n\rVert)$ depends on $n$.
- §3.1 prints the conditions as products, e.g. "$\delta_1\delta_2=0$, $\delta_0=1$". They must mean $\delta_1=\delta_2=0$: read literally they overlap the cases of $\hat f^2$ and $\hat f^3$.
- §3.1 never maps the combination labels $\hat f^n_{i+1/2}$ to the fluxes $R'_n$ of Eq. (25). By stencil content, $\hat f^2$ ($\delta_1=0$, target $\{i-2,\dots,i+1\}$) is $R'_3$ and $\hat f^3$ ($\delta_2=0$, target $\{i-1,\dots,i+2\}$) is $R'_2$, so the two numberings are swapped for these cases. *(Compiler check, not in the sources: the stencils of $R'_2$ and $R'_3$ read off Eq. (25).)*
- Eq. (29), $R'_1$: the expansion is closed with "$-12h^{(4)}\Delta x^6\lambda^2+O(\Delta x^7)$", but the $\Delta x^6$ term also holds $\tfrac1{140}h^{(6)}$, i.e. $R'_1=h-\Delta x^5\big(\tfrac12\lambda_{\mathrm s}^2h'''+\tfrac1{60}h^{(5)}\big)+\Delta x^6\big(\tfrac15\lambda_{\mathrm s}^2h^{(4)}+\tfrac1{140}h^{(6)}\big)+O(\Delta x^7)$. The leading order is unaffected. *(Compiler check, not in the sources: Taylor expansion of the cell averages of $h$ about $x_{i+1/2}$.)*
- Eq. (27) prints the integrated first term as "$h_{i+1/2}\xi$" inside a bracket whose other terms are in $(\xi-x_{i+1/2})$; the result line is correct.
- Symbol clashes in print: $\alpha_j$ (RBF coefficients, Eq. 21) and $\alpha_1,\alpha_2$ (shape constants, Eq. 32); $k$ as candidate index and as right extent of the target stencil (Eq. 18); $\varepsilon$ with the values $10^{-40}$ and $10^{-15}$.

# Notation map

| Liang & Fu (2024a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f(u)$, $f_j$ | $u$, $f$, $f_j$ | scalar law with $f'(u)>0$; systems by Roe-average characteristic projection |
| $h(x)$, $H(x)$ | kept (page-local) | implicit function whose cell averages are the point fluxes, and its primitive from the left end of the target stencil; **$h$ is also the shallow-water depth and the two-point flux $h(u^-,u^+)$** |
| $\hat f_{i+1/2}$ | $\hat f_{i+1/2}$ | numerical flux; agrees |
| $S_0$, $S_1$, $S_2$ | $S_0$, $S_1$, $S_2$ | **TENO numbering, central stencil first, not the registry's upwind-first** |
| $\hat f_{k,i+1/2}$ | $\hat f^{(k)}_{i+1/2}$ | candidate flux |
| $d_k$ | $d_k$ | TENO5 linear weights $0.6,0.3,0.1$; absent from the new scheme |
| $\beta_{k,r}$ | $\beta_k$ | Jiang–Shu indicator, $r=3$ |
| $\tau_5$ | $\tau_5$ | here $\lvert\beta_1-\beta_2\rvert$, the two non-central candidates |
| $\gamma_k$, $q$, $\chi_k$, $\delta_k$, $C_T$ | agree | $C=1$ implicit; $C_T=10^{-5}$ ($10^{-4}$ for TENO5 in §4.3) |
| $w_k$ | $\omega_k$ | TENO5 weights |
| $\varepsilon$ | $\epsilon$ | $10^{-40}$ (Eqs. 9, 31) and $10^{-15}$ (fallback of Eq. 35) |
| $\hat f^n_{i+1/2}$, $R'_n$ | kept | flux of flag combination $n$ and RBF flux on target stencil $n$ (numberings differ, see Printed slips) |
| $r$, $k$ (Eq. 18) | $r_{\mathrm L}$, $r_{\mathrm R}$ | extents of the target stencil; **$r$ is the WENO stencil size, $k$ the candidate index** |
| $\phi$, $\Phi$ | kept | Gaussian kernel $\exp(-\lambda_{\mathrm s}^2x^2)$ |
| $\alpha_j$ (Eq. 21) | $c_j$ (page-local) | RBF coefficients; **$\alpha$ collides with $\alpha_k$** |
| $\lambda$ | $\lambda_{\mathrm s}$ | shape parameter, as on the [RBF-WENO](/methods/rbf-weno.md) page, multiplies physical distance; **$\lambda$ is the eigenvalue in the registry** |
| $\alpha_1$, $\alpha_2$ | $\lambda_0$, $\lambda_\Delta$ | shape constants, both 3 |
| $g(m)$ | $\varphi(\mu_d)$ | mapping, as on [adaptive TENO](/methods/adaptive-teno.md) and [RBF-WENO](/methods/rbf-weno.md); **$g$ is the mapped-WENO function in the registry** |
| $\eta_i$, $\theta_i$, $m$, $c_r$, $\varepsilon$ (Eq. 31) | $\sigma_i$, $\min(\sigma_{i-1},\sigma_i,\sigma_{i+1})$, $\mu_d$, $C_r$, $\epsilon_\sigma$ | Ren-type ratio, its three-point minimum, measure, threshold and regularization, as on [adaptive TENO](/methods/adaptive-teno.md); **$\eta$ is the entropy and $\theta$ the Zhang–Shu factor in the registry** |
| $\zeta_i$ | $\zeta^{\mathrm D}_i$ | discontinuity-location flag of Liang et al. (2022); **$\zeta$ is the characteristic variable and the Z+ ratio in the registry** |
| $\mathcal A$ | $\mathcal A$ | tanh steepness, as the THINC profile parameter of §10 |
| $L(u)$ | $\mathcal L(u)$ | semi-discrete operator; SSP-RK3, CFL 0.4 |

# Reference list

The paper prints 69 references, numbered [1]–[69]. All are parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby` including
`liang-2024`. Same-author same-year works take suffixes by identity: Fu 2019
[24]/[36], Guo & Jung 2017 [41]/[47], and Tsoutsanis 2021 [14]/[15],
where [15] (J. Sci. Comput. 89) is the bundle's Source `tsoutsanis-2021`. [34]
is URANOS, the Source `devanna-2023-b`. [37] prints no volume, only the article
number 112273. [54] ends its author list with "et al." and [63] prints only "P.
Woodward". [50] (Micchelli) is recorded as printed, a Springer 1984 item. No
printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-23). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [RBF-based WENO](/methods/rbf-weno.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [TENO-THINC](/methods/teno-thinc.md)
