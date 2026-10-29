---
type: Source
title: "Vandenhoeck et al. (2022) — Development of an implicit high-order flux reconstruction solver for the Langtry-Menter Laminar-Turbulent Transition RANS model"
description: "Implicit high-order flux reconstruction solver in COOLFluiD for compressible RANS with a log-omega k-omega SST model and the Langtry–Menter transition model: semi-analytical Jacobian, source-Jacobian treatments, verification on the Wieghardt plate and ERCOFTAC T3 cases, O(N²) cost per degree of freedom."
resource: "doi:10.1016/j.cpc.2022.108408"
source_kind: paper
authors: [Vandenhoeck R., Lani A., Steelant J.]
year: 2022
venue: "Comput. Phys. Commun. 278:108408"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Computer_Physics_Communications_Vandenhoeck_Development_of_an_implicit_high-order_flux_reconstruction_so.pdf"
tags: [rans, transition, flux-reconstruction, k-omega, high-order, software]
timestamp: 2026-10-29T10:06:00Z
---

# Summary

Vandenhoeck et al. (2022) present what they call, to their knowledge, the
first [flux reconstruction](/methods/flux-reconstruction.md) (FR) solver for
the compressible RANS equations with laminar–turbulent transition, built in
the open-source C++ platform [COOLFluiD](/software/coolfluid.md). Two
closures are implemented. The first is the 2003
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) rewritten to
transport $\ln\omega$ instead of $\omega$: the idea of Bassi et al. (2005)
for the [Wilcox $k$-$\omega$ model](/methods/k-omega-model.md) under
[DG](/methods/discontinuous-galerkin-spectral-element-method.md), here
extended to SST, which adds a transformed cross-diffusion term. Transporting
$\ln\omega$ removes the steep near-wall rise of $\omega$ that destabilized
high-order polynomials and keeps $\omega>0$. The second is the
Langtry–Menter
[local-correlation-based transition model](/methods/local-correlation-based-transition-model.md)
(SST-2003-LM2009), rewritten in $\ln\omega$.

The FR scheme (Huynh, VCJH correction functions, BR2 diffusion, AUSM$^+$-up
convection) runs fully implicit: backward Euler, Newton linearization and
PETSc GMRES. The FR operator is differentiated analytically into six
Jacobian blocks, and the physical-flux derivatives are taken by finite
differences (a "semi-analytical" Jacobian). Of five source-term Jacobian
treatments compared on the ERCOFTAC T3A case, the decoupled one is retained.

Verification uses Wieghardt's fully turbulent
[flat plate](/benchmarks/turbulent-boundary-layer.md) up to $N=6$ against
experiment, Spalding's [law of the wall](/definitions/law-of-the-wall.md)
and a DG reference, and the
[ERCOFTAC T3A, T3B and T3A−](/benchmarks/ercoftac-t3-flat-plate.md)
bypass-transition cases on a 143-element mesh. Higher orders converge to a
common solution and stay accurate with a first-element height
$y_1^+\simeq25$ without [wall functions](/methods/rans-wall-function.md).
The authors argue that the implicit FR cost per degree of freedom can at
best scale as $O(N^2)$, and single-thread timings follow that scaling.

# Version read

Version of record (Comput. Phys. Commun. 278:108408; received 21 April 2021,
accepted 4 May 2022), 22 pages, all read; pp. 3–5 and 14 read visually
because the extracted equations were garbled. Page-1 title, authors and DOI
match the metadata above. No identity problem. Numbering on this page is
that of this version.

# Key claims

1. To the authors' knowledge, the solver is the first FR solver for RANS flows with laminar–turbulent transition; earlier FR-RANS work used Spalart–Allmaras and Wilcox $k$-$\omega$ only (Abstract, §0). **Stated**
2. With the original SST-2003 model, the steep near-wall increase of $\omega$ can make FR unstable, and high-order polynomials need not keep $\omega$ positive; transporting $\ln\omega$, whose near-wall distribution is much smoother, removes the instability and guarantees $\omega>0$ (§1.1). **Stated** (reported experience, no figure)
3. The $\ln\omega$ equation (Eq. 5) is conservative in $\ln\omega$ but not in $\omega$; Bassi et al. showed no significant discrepancy against the original $k$-$\omega$ model (§1.1). **Stated**
4. Compared with Bassi et al. (Wilcox model), Eq. 5 carries the transformed SST cross-diffusion term $2(1-F_1)\rho\sigma_{\omega2}\,\omega^{-1}\partial_jk\,\partial_j\ln\omega$ (Eq. 17) and the term $(\mu+\sigma_\omega\mu_t)\,\partial_k\ln\omega\,\partial_k\ln\omega$ from transforming the diffusion term (Eq. 18) (§1.1.1). **Derived**
5. The limiter $\max(k,0)$ (Eq. 20) is needed only in the initial transient from a uniform field for the cases considered (§1.1.1). **Stated**
6. The correlation value $Re_{\theta t}$ cannot be obtained explicitly from Eqs. 33–35; Newton–Raphson on $\theta_t$ is stopped at 10 iterations or at a relative change below $10^{-6}$, the latter generally reached first (§1.2.1, Eqs. 39–41). **Stated**
7. The semi-analytical FR Jacobian splits into six terms $J_{e,u}+J_{e,q}+J^I_{f,u}+J^I_{f,q}+J^D_{f,u}+J^D_{f,q}$ (Eq. 87); the gradient at a solution point of a tensor element depends on $3N_{\mathrm{dim}}(N+1)$ states, the element's and its $2N_{\mathrm{dim}}$ neighbours' (§3.2.2, Eqs. 67–87, Fig. 5). **Derived**
8. A purely finite-difference Jacobian is costly and does not scale with order, because the whole FR procedure is repeated for every perturbed solution-point variable (§3.2.1). **Stated**
9. The physical-flux derivatives are computed numerically because their cost is small against the analytical FR Jacobian; extension to a fully analytical Jacobian is "straightforward" (§3.2.2). **Stated**
10. In the $N=2$ T3A case with the CFL number rising exponentially from 10 to a limit of 1250, all source-Jacobian schemes, the analytical one included, run at CFL 1250; without a source-term Jacobian the limit had to be lowered to 500 (§3.2.3, Fig. 6). **Shown**
11. The fully numerical Jacobian stagnates in convergence and is less efficient; the approximate (negative-part) Jacobian schemes, with and without a time-step restriction, first speed up convergence and then stagnate (§3.2.3, Fig. 6). **Shown**
12. Full analytical and diagonal source Jacobians perform similarly; the decoupled treatment (no derivatives with respect to the mean-flow variables, SST and Langtry–Menter blocks decoupled) converges slightly faster and is used in all further cases (§3.2.3, Fig. 6). **Shown**
13. The source-based time-step restriction of Merci et al. is generally less severe than the convective/diffusive one, in agreement with Merci et al. (§3.2.3). **Shown**
14. For $N=4$ T3A started from the converged $N=3$ solution at CFL 200, the source-Jacobian schemes do not differ significantly; $N=2$ at CFL 1250 needs about 700–1000 iterations to reach a (logarithmic) residual of $-13$, $N=4$ at CFL 200 about 500 (§3.2.3, Fig. 7). **Shown**
15. At a no-slip wall the wall distance $d_1$ in the ghost value of $\ln\omega$ should be 0 (infinite $\omega$); the distance of the element's first degree of freedom is used instead (§3.3.1, Eq. 88). **Stated**
16. Wieghardt plate on mesh A ($y_1^+\simeq10$): the higher-order velocity profiles coincide and agree with experiment, Spalding's law and the DG $N=2$ reference of Bassi et al.; the $N=4$ $C_f$ lies considerably closer to experiment than lower orders and the DG reference (§4.1, Fig. 9). **Shown**
17. Mesh B ($y_1^+\simeq25$): discontinuities visible at $N=5$ disappear at $N=6$; $N=4$ on mesh A and $N=5$, $N=6$ on mesh B coincide, so accurate results are obtained at $y_1^+\simeq25$ without wall functions, larger than state-of-the-art second-order finite-volume solvers allow without wall-extended functions (Abstract, §4.1, Fig. 10). **Shown** (the finite-volume comparison **Stated**)
18. T3 cases on the 143-element mesh: low orders are inadequate ($N=0$ shows no transition); higher orders approach experiment and the two highest coincide; T3A and T3A− results are very close to the finite-volume reference of Langtry and Menter (about 39,000 elements, rounded leading edge), and for T3A− coincide with it (§4.2, Figs. 12–13). **Shown**
19. For T3B the FR solution is "remarkably closer" to experiment than the finite-volume reference, attributed "most likely" to FR accuracy (§4.2, Fig. 12b). **Shown** (attribution **Stated**)
20. The T3A $N=5$ $C_f$ is nearly identical for the VCJH parameters $c_{\mathrm{SD}}$, $c_{\mathrm{DG}}$, $c_{\mathrm{HU}}$ (the source's $c_{SD}$, $c_{DG}$, $c_{g2}$) (§4.2, Fig. 14). **Shown**
21. Transition onset in T3A− is predicted significantly earlier than in the experiment, so its profiles are not compared (§4.2). **Shown**
22. T3A and T3B profiles at $N=5$: $u^+$ agrees with experiment and with Suluksna–Juntasaro; $k^+$ agrees with Suluksna–Juntasaro but under-predicts the experimental near-wall values (attributed to the Langtry–Menter model itself); $-\langle u'v'\rangle^+$ agrees with Suluksna–Juntasaro but over-predicts the experimental peak; the model does not reproduce the experimental maximum of $k^+$ during transition (§4.2, Figs. 15–16). **Shown**
23. Per element the implicit FR Jacobian costs $O(N^{N_{\mathrm{dim}}+1})$ and diffusive fluxes add an $O(N)$ factor per term, so the time per degree of freedom can at best scale as $O(N^2)$, irrespective of dimension (§4.3). **Derived**
24. Single-thread timings (Intel Core i7 9700K, PETSc GMRES) of wall time per degree of freedom per iteration follow the $O(N^2)$ scaling, slightly under-performing at high order; the two Langtry–Menter equations raise the wall time but not its order scaling (§4.3, Fig. 17). **Shown**
25. High-order finite-element-type methods have higher accuracy per degree of freedom than low-order ones, "proven for the present solver" in the authors' earlier work (§4.3). **Stated**

# Printed slips

- **§3.2.2, between Eqs. 82 and 83:** "Using expression (52) to compute $_fu^n_j$ and $_fu^n_j$" prints the same symbol twice; the second should be the current-element value $_fu^c_j$, as in Eq. 82.
- **§3.2.2:** "the analytical expression for $\partial_fF_i^D/\partial_lu_j|_q$ and $\partial_fF_i^D/\partial_mq^b_j|_u$ needs to be computed for the specific interface flux scheme": in context (the interface terms $J^I$ cannot be simplified) the derivatives meant are of the interface flux $F^I$, not of $F^D$.
- **§4.1 against §3.3.2:** "$Tu_\infty$ is $10^{-2}$" for the Wieghardt plate, while §3.3.2 defines $Tu_\infty$ "in percentage"; the unit of the printed value is ambiguous.
- **Symbol clash:** $P$ is both the production of $k$ (Eq. 6) and the polynomial degree (§2 onward).
- **References:** [64] prints "Y. Saad, M.H. Schultz Gmres" (a title word fused into the author list); [9] "AIAA Paper 4079, 2007, 2007" and [19] "AIAA Pap. 44 (2011) 2011" repeat the year.
- **Typo:** "straightforward to extend to solver" (§3.2.2).
- *(compiler check, not in the sources)* The piecewise correlations of $F_{l1}$ and $Re_{\theta c}$ (Eqs. 24, 29) join at their breakpoints to within about 1% ($F_{l1}$: 13.837 against 13.840 at 400, 0.496 against 0.5 at 596, 0.3188 on both sides at 1200; $Re_{\theta c}$: 1278.07 against 1276.89 at 1870), and the element counts of the meshes ($(22+6)\times28=784$, $(22+6)\times14=392$, $(10+3)\times11=143$) agree with the totals: no slip there.

# Notation map

| Vandenhoeck et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u_i$, $p$, $e_0$, $h_0$ (no tilde) | $\langle\rho\rangle$, $\langle u_i\rangle_\rho$, … | Favre-averaged variables printed without accents; $e_0$ excludes $k$ |
| $\tau_{ij}=2\mu_t(S_{ij}-\tfrac13\partial_ku_k\delta_{ij})-\tfrac23\rho k\delta_{ij}$ | $-\langle\rho u_i''u_j''\rangle$ | **sign convention:** force-per-area (negative-trace) Reynolds stress; registry $R_{ij}$ has positive trace |
| $\tilde\tau_{ij}$ | (total viscous plus Reynolds stress) | **collision:** tilde means "total", not a Favre filter |
| $S=\sqrt{2S_{ij}S_{ij}}$, $\sqrt{2\Omega_{ij}\Omega_{ij}}$ | $\lvert S\rvert$, $\lvert\Omega\rvert$ | agree (factor two) |
| $\tilde\omega=\ln\omega$ | $\tilde\omega_\ell=\ln\omega$ (registry §11) | **collision:** the registry tilde is the Favre filter or the SA variable $\tilde\nu$ |
| $P$ (Eq. 6), limited by $10\beta^*\rho\omega k$ | $P_k$ (limited, dynamic form $\langle\rho\rangle P_k$) | **collision:** $P$ also the polynomial degree |
| $P$ (§2 on), P0–P6 | $N$, $N=0$–$6$ | polynomial degree; order $N+1$ |
| $\hat\gamma_1$, $\hat\gamma_2$ | $\gamma_\omega$ (registry §11) | $5/9$, $0.44$; the hat is not a test filter |
| $\beta_1$, $\beta_2$, $\beta^*$, $\sigma_k$, $\sigma_\omega$, $a_1$ | $\beta_\omega$ (§11), $\beta^*$, $\sigma_k$, $\sigma_\omega$, $a_1$ | $\beta_1=0.075$, $\beta_2=0.0828$, $\beta^*=0.09$, $\sigma_{\omega2}=0.856$, $a_1=0.31$ |
| $F_1$, $F_2$, $F_3$, $CD_{k\omega}$ | $F_1$, $F_2$ (+ page-local $F_3$, $CD_{k\omega}$) | $F_1=\max(F_{1,\mathrm{SST}},F_3)$ in the transition model |
| $\gamma$ with an accent (adiabatic index) | $\gamma$ | 1.4; on this page $\gamma$ otherwise denotes the intermittency (registry clash list) |
| $F_l$, $F_{l1}$, $F_{sl}$, $F_{os}$, $F_t$ | $F_{\mathrm{length}}$, $F_{l1}$, $F_{sl}$, $F_{\mathrm{onset}}$, $F_{\mathrm{turb}}$ | page-local names of the [transition-model page](/methods/local-correlation-based-transition-model.md) |
| $\gamma$, $\gamma_{eff}$, $\gamma_{sep}$ | $\gamma$ (transition pages), $\gamma_{\mathrm{eff}}$, $\gamma_{\mathrm{sep}}$ | intermittency |
| $\tilde{Re}_{\theta t}$ | $\mathcal R_{\theta t}$ | page-local on the [transition-model page](/methods/local-correlation-based-transition-model.md); **collision** with the registry tilde |
| $Re^{eq}_{\theta t}$, $Re_{\theta c}$ | $Re_{\theta t}$ (correlation value), $Re_{\theta c}$ | as on the transition-model page |
| $Re_V=\rho Sd^2/\mu$, $Re_\omega$, $R_T=\rho k/(\mu\omega)$, $R_y=\rho d\sqrt k/\mu$ | $Re_V$, $Re_\omega$, $R_T$ (page-local), $R_y$ (registry §11) | $Re_V$ is built on $\lvert S\rvert$ here |
| $Tu$, $Tu_\infty$ | $Tu$ | percent |
| $d$, $d_1$ | $d$; $d_1$ distance of the first solution point | |
| $y_1^+$ | $y_1^+$ (registry §11) | based on the first-element height, not the first degree of freedom |
| $-uv^+=\mu_t\,\partial_yu_x/(\rho u_\tau^2)$ | $-\langle u'v'\rangle^+$ | computed from the eddy viscosity, not a resolved stress |
| $N_{dim}$, $N_s=(P+1)^{N_{dim}}$ | $N_{\mathrm{dim}}$, $(N+1)^{N_{\mathrm{dim}}}$ | |
| $h_f$, $c_{SD}$, $c_{DG}$, $c_{g2}$ | (VCJH correction functions); $c_{\mathrm{SD}}$, $c_{\mathrm{DG}}$, $c_{\mathrm{HU}}$, the named values of the correction parameter $c_{\mathrm{FR}}$ (page-local on the flux-reconstruction page) | $c_{g2}$ is Huynh's $g_2$ scheme, written $c_{\mathrm{HU}}$ on the [flux-reconstruction page](/methods/flux-reconstruction.md) |
| $J_{e,u}$, …, $J^D_{f,q}$ | (Jacobian blocks) | page-local |
| $\varepsilon$ (Eq. 65) | (finite-difference step, $10^{-7}$) | **collision:** not the dissipation rate |

# Reference list

75 printed references, numbered in Elsevier CPC style, mostly without
titles, no DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Three undated
NASA Turbulence Modeling Resource web pages ([36], [39], [40], accessed
December 2020) are keyed with the citing paper's year. Same-author
same-year works take suffixes in printed order (Lani 2013 [32], [58];
Castonguay 2011 [20], [42], [44]; Vandenhoeck 2019 [45], [73]). Parsing
notes: [64] fuses "Gmres" into the authors (entered as Saad & Schultz,
SIAM J. Sci. Stat. Comput. 7:856–869, 1986); [9] and [19] repeat the year;
[49] and [52] print no pages, [59] no volume; [53] and [54] print the first
author "A.A. Laguna" and [56] "A. Alvarez Laguna", keyed as printed. No
printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [ERCOFTAC T3 flat-plate transition cases](/benchmarks/ercoftac-t3-flat-plate.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Method of manufactured solutions](/methods/method-of-manufactured-solutions.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [COOLFluiD](/software/coolfluid.md)
