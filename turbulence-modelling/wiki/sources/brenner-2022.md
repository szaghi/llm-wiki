---
type: Source
title: "Brenner et al. (2022) — Efficient assimilation of sparse data into RANS-based turbulent flow simulations using a discrete adjoint method"
description: "Variational field inversion of a cell-wise multiplier on a frozen k-ε eddy viscosity from sparse averaged-LES velocity and skin-friction data on the periodic hill, with a discrete adjoint in foam-extend whose parameter Jacobian is assembled from built-in finite-volume operators, total-variation regularization and Helmholtz filtering."
resource: "doi:10.1016/j.jcp.2022.111667"
source_kind: paper
authors: [Brenner O., Piroozmand P., Jenny P.]
year: 2022
venue: "J. Comput. Phys. 471:111667"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Brenner_Efficient_assimilation_of_sparse_data_into_RANS-based_turbul.pdf"
tags: [field-inversion, adjoint, rans, periodic-hill, eddy-viscosity]
timestamp: 2026-10-27T15:46:00Z
---

# Summary

Brenner et al. (2022) correct a linear eddy-viscosity RANS model by a
spatially varying multiplier $\beta(\boldsymbol x)$ of the eddy viscosity,
$\nu_{\mathrm{eff}}=\nu+\beta\nu_t$, where $\nu_t$ comes from a converged
[$k$-$\varepsilon$](/methods/k-epsilon-model.md) solution and is then
frozen; only $\beta$ (one value per cell) is optimized. This is the
inversion half of [field inversion and machine learning](/methods/field-inversion-machine-learning.md):
no learning model is trained, and the recovered fields are offered as
future training data. The correction keeps the
[Boussinesq form](/definitions/boussinesq-hypothesis.md). The loss is a
volume-weighted velocity discrepancy at reference cells plus a
"total-variation" (neighbour-difference) regularization; its gradient
comes from a discrete stationary adjoint in foam-extend 4.0
([OpenFOAM](/software/openfoam.md)): the transposed block-coupled forward
matrix gives the adjoint system, and the parameter Jacobian is assembled
"semi-analytically" by discretizing the only $\beta$-dependent term,
$\nabla\cdot(\beta\nu_t\nabla\langle\boldsymbol u\rangle)$, with built-in
implicit operators, instead of finite differences, complex step or
automatic differentiation. The pressure-residual part of the gradient is
dropped. Positivity comes from an exponential-linear map, checkerboard
artefacts are removed by a Helmholtz filter, and the update is a modified
Gauss–Newton step.

On the [periodic hill](/benchmarks/periodic-hill.md) at $Re_h=10\,595$
with averaged-LES reference data, synthetic-truth tests recover the
velocity but not $\beta$ (non-uniqueness). The adjoint gradient has the
correct sign in 84% of cells against finite differences. Full-field and
sparse velocity data are matched, the regularization curing over-fitting
at sparse points. Interior data alone do not improve $C_f$; adding
$C_f$-derived wall data shows a trade-off between wall and interior
agreement. The stress–strain alignment is "neither considerably nor
consistently improved". The paper places its correction among
[model-form error](/definitions/model-form-uncertainty.md) remedies and
contrasts it with [ensemble Kalman](/methods/ensemble-kalman-closure-calibration.md)
calibration; the introduction cites [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
and near-wall [grid-cost](/results/les-grid-point-requirements.md)
scalings, and the abstract offers the fields for
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) closure
enhancement.

# Version read

Version of record (Elsevier, open access; received 11 March 2021, online
29 September 2022), 23 pages, all read; equation pages also read
visually because the text layer drops glyphs. Page 1 matches the
metadata; no identity issue. Equation, section and figure numbers are
those of this version.

# Key claims

Page-local symbols: $\beta(\boldsymbol x)$ the registry's field-inversion
multiplier (the source's $\alpha$); $\beta'$ its unconstrained
optimization variable; $\mathcal L=\mathcal L_U+\mathcal L_\beta$ the
cost (discrepancy plus regularization); $\mathcal R$ the discrete
residual; $\boldsymbol\lambda_{\mathrm{adj}}$ the adjoint variables;
$C^{tv}$, $C^d$ the regularization weights; $\ell_H$ the Helmholtz
filter width; $\omega_{\mathrm{GN}}$ the Gauss–Newton relaxation;
$\mathcal L_{\mathrm{tol}}$ the cost target; $c_{RS}$ Schmitt's
stress–strain alignment coefficient in the form of Eq. (42).

1. Parametric calibration of RANS coefficients (EnKF, polynomial chaos, ABC) gives limited improvements because no universal optimal values may exist (§1). **Stated**
2. Model-form errors arise at three levels (averaging, functional form of the Reynolds stress, functions within the model); for linear eddy-viscosity models only the third (how $\nu_t$ is computed) can be improved (§1). **Stated**
3. With $\nu_{\mathrm{eff}}=\nu+\beta\nu_t$ (Eq. 7) the Boussinesq form is kept, and the results "satisfy conservation of momentum since the divergence operator is applied to the modified term" (§2.1.1). **Stated**
4. The problem is $\min_\beta\mathcal L(\beta,\langle\boldsymbol u\rangle)$ subject to $\mathcal R(\beta,\langle\boldsymbol u\rangle)=0$ and $\beta>0$ (Eq. 8); positivity ensures stability of the forward solver (§2.1.2). **Stated**
5. The adjoint gradient $\mathrm d\mathcal L/\mathrm d\beta=\mathrm d\mathcal L_\beta/\mathrm d\beta-\boldsymbol\lambda_{\mathrm{adj}}^T\partial\mathcal R/\partial\beta$ (Eq. 14) costs about one forward solve, independent of the number of parameters (§2.1.3–2.1.4). **Derived**
6. Writing the residual as linear in $\beta$, $A_\beta\beta-b_\beta=0$ (Eq. 17), gives $\partial\mathcal R/\partial\beta=A_\beta$; here the only $\beta$-term is $\nabla\cdot(\beta\nu_t\nabla\langle\boldsymbol u\rangle)$ (Eqs. 37–38), assembled with built-in operators; the abstract states all partial derivatives cost "approximately one forward solution step". **Derived**
7. The explicit pressure contribution $\boldsymbol\lambda_{\mathrm{adj},p}^T\partial\mathcal R_p/\partial\beta$ is omitted (Eqs. 21–22) for lack of implicit operators; its effect "was not further investigated" (§2.3). **Stated**
8. Finite-difference check at 156 cells along the centrelines, steps $10^{-3}$ to $10^{-1}$, forward tolerance tightened to $10^{-10}$: "significant difference between the adjoint and finite difference gradients in some cells"; at step $10^{-2}$ the complete gradient field has the correct sign for 84% of values (§3.3, Fig. 8). **Shown**
9. The conclusion states that the method "is able to produce accurate cost function gradients" despite the neglected pressure part (§4); printed beside claims 7 and 8. **Stated**
10. Synthetic test (prescribed $\beta^{ref}$, full-field streamwise velocity, no regularization): the optimized velocity profiles "agree very well" with the reference, while the recovered $\beta$ (range [0.21, 1.95]) does not match $\beta^{ref}$, showing non-uniqueness (§3.2, Figs. 6–7). **Shown**
11. Full-field averaged-LES streamwise velocity ($\omega_{\mathrm{GN}}=1$, $\mathcal L_{\mathrm{tol}}=5.00\times10^{-12}$, no regularization): profiles coincide except at near-crest velocity peaks; wall shear stress is not improved by interior data (§3.4, Fig. 9). **Shown**
12. Per-iteration cost drops sharply after the first steps because each forward solve is warm-started (§3.4). **Stated**
13. Cost-history oscillations come from the variable Gauss–Newton step (§3.4). **Stated**
14. Sparse data without regularization yield unphysical $\beta$ peaks at reference points and large test-point discrepancy (over-fitting); dense data give $\beta\in[0.01,11.9]$ (§3.5, Fig. 11). **Shown**
15. Regularization with $C^{tv}=10^{-12}$ (face neighbours) gives smooth $\beta$ and velocity; in the sparse case the test-point cost reaches lower values than without it, not in the dense case (§3.5, Figs. 12, 14, 15). **Shown**
16. The deviation-from-initial regularization "did not prove to perform well" (§3.5). **Stated**
17. Large $C^{tv}$ produces checkerboard artefacts in $\beta$ that do not affect the velocity; a Helmholtz filter with $\ell_H=0.033$ removes them (range [0.44, 4.60] after filtering) at a slightly higher cost (§2.7, §3.5). **Shown**
18. Because of non-uniqueness, comparing $\beta$ fields across data distributions is not meaningful; where velocity gradients are tiny $\beta$ does not affect the velocity (§3.5). **Stated**
19. The alignment $c_{RS}$ after assimilation is comparable to the baseline, "neither considerably nor consistently improved", while mean velocities are (§3.5, Fig. 13). **Shown**
20. An equivalent eddy viscosity estimated from the averaged LES shows no qualitative improvement of the optimized eddy viscosity relative to it (§3.5). **Stated**
21. Wall-only reference data give good $C_f$ but worse interior profiles than the baseline RANS (§3.6). **Stated**
22. Combined wall ($C_f$-derived) and interior data with $C^{tv}=5\cdot10^{-12}$: $C_f$ well recovered, interior profiles improved but deviating near the lower wall — "there seems to be a Pareto front" (§3.6, Fig. 16). **Shown**
23. Sparsely distributed wall data give noisy $\beta$ and $C_f$ even with stronger regularization (§3.6). **Stated**
24. Whether the wall-data deviations come from the eddy-viscosity assumption or from the method and regularization cannot be decided conclusively (§3.6). **Stated**
25. Results "considerably depend on the locations of the reference values and the values of the hyperparameters" (§4). **Stated**
26. Ensemble Kalman methods suffer from the curse of dimensionality (citing [23]); nudging corrects only the state, not parameters (§1.1). **Stated**
27. Brenner et al. (§1) cite Xiao & Jenny [1] for a near-wall resolution cost of wall-bounded flows scaling as $Re^3$ for DNS and $Re^{1.8}$ for LES. **Stated**

*(Compiler check, not in the sources.)* From Eqs. (2)–(3) the divergence
of the Boussinesq stress is
$\partial_j[\nu_t(\partial_j\langle u_i\rangle+\partial_i\langle u_j\rangle)]$;
with continuity the second part is
$\partial_j\nu_t\,\partial_i\langle u_j\rangle$, which is non-zero when
the eddy viscosity varies in space. Eq. (6), on which Eq. (7) builds,
keeps only $\partial_j(\nu_{\mathrm{eff}}\partial_j\langle u_i\rangle)$.
The paper does not say whether the implementation keeps the second
term; claim 3 stands as printed.

# Printed slips

- Eq. (2): the viscous term is printed $\nu\,\partial^2U_i/\partial x_jx_j$.
- After Eq. (42): "where $\overline R_{ij}$ is the anisotropic stress tensor, $\overline R_{ij}$ the averaged strain rate tensor".
- Fig. 13 caption: "good alignment (blue), i.e., smaller than 0.86, and bad alignment (red), i.e., larger than 0.86", while §2.11 states $\rho_{RS}>0.86$ for alignment and $\rho_{RS}=1$ for perfect alignment.
- §3.3: "the approximations made in the adjoint gradient approach presented (cf. Eq. (24))" — Eq. (24) is the finite-difference perturbation; the approximation is Eq. (22).
- Fig. 8 caption: "The adjoint gradient values $\left.\frac{df}{d\alpha}\right|_{FD}$ are plotted over the corresponding finite difference gradient values $\left.\frac{df}{d\alpha}\right|_{adj}$" — subscripts opposite to the text and axis labels.
- §3 opening announces "two main reasons" for the configuration; the second is never given.
- §3.5: "Two different reference data distributions are considered, as featured in Fig. 10" — Fig. 10 shows three (dense, intermediate, sparse); "Fig. 12 (left)" for panels arranged top/bottom.
- §3.5: "Also in Fig. 14, some checkerboard patterns can be observed in the optimized $\alpha$ field" — Fig. 14 shows velocity and wall-shear profiles.
- §3.5: "as described in 2." (section number truncated); "lover values".
- §3.6: the text assigns Fig. 16a to "the combined full wall and sparse field reference data"; the caption says "dense (left) and intermediate (right) internal reference data distributions".
- Eq. (33), $\tilde\alpha=\left(\frac{1}{1+l^2}(\mathbb I-l^2\nabla^2)\right)^{-1}\alpha$. *(Compiler check, not in the sources: a uniform field $c$ is returned as $(1+l^2)c$, i.e. $1.0011\,c$ at $l=0.033$; the filter does not preserve constants as printed.)*

# Notation map

| Brenner et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U_i$, $p$ | $\langle u_i\rangle$, $p$ | kinematic; after Eq. (6) $p$ is $p/\rho+\tfrac23k$ |
| $\tau_{ij}=\tfrac23k\delta_{ij}-\nu_t(\partial_jU_i+\partial_iU_j)$ | $R_{ij}$ | same positive-trace convention; enters Eq. (2) as $-\partial_j\tau_{ij}$ |
| $\epsilon$ | $\varepsilon$ | |
| $\nu_t$, $\nu_{eff}=\nu+\alpha\nu_t$ | $\nu_t$, $\nu_{\mathrm{eff}}$ | $\nu_{\mathrm{eff}}$ here is molecular plus corrected eddy viscosity, not §11's projected effective viscosity |
| $\alpha$ | $\beta(\boldsymbol x)$ | **collides with the registry's DG blending factor $\alpha$**; translated to the field-inversion multiplier |
| $\alpha'$ | $\beta'$ | page-local optimization variable, Eq. (32) |
| $f$, $f_U$, $f_\alpha$ | $\mathcal L$, $\mathcal L_U$, $\mathcal L_\beta$ | loss |
| $R$, $R_U$, $R_p$ | $\mathcal R$, $\mathcal R_U$, $\mathcal R_p$ | **$R$ collides with the Reynolds stress $R_{ij}$** |
| $\lambda$ | $\boldsymbol\lambda_{\mathrm{adj}}$ | **$\lambda$ is the Taylor microscale in the registry** |
| $\Delta$ (step size) | step size, no symbol | **$\Delta$ is the filter width in the registry** |
| $\omega$ (relaxation) | $\omega_{\mathrm{GN}}$ | **$\omega$ is the specific dissipation rate in the registry** |
| $l$ | $\ell_H$ | Helmholtz filter width, units not stated |
| $\rho_{RS}$, $\overline R_{ij}$, $\overline S_{ij}$ | $c_{RS}$, $R_{ij}-\tfrac23k\delta_{ij}$, $\langle S_{ij}\rangle$ | **overbar is a Reynolds average here, not the LES filter**; $\rho$ is not density |
| $C_f$, $U_b$, $H$ | $C_f$, bulk velocity at the crest, hill height | $Re_h=U_bH/\nu$ |

# Reference list

49 printed references, numbered style [1]–[49], DOIs printed for most.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. No printed duplicates and no unparseable items.
[29] He C. et al. 2018 and [35] He P. et al. 2018 share an author-year
key family, resolved by volume and page against existing entries; [41]
Ben Ali et al. is printed as a working paper (HAL) and kept as a
preprint; [17] is Duraisamy et al. (2019).

# Pages created or updated

Chunk 10 (2026-10-27), cited further in chunk 14. This source is cited on:

- [Periodic hill](/benchmarks/periodic-hill.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Bayesian calibration of turbulence-model coefficients](/methods/bayesian-closure-calibration.md)
- [Ensemble Kalman filter calibration of turbulence closures](/methods/ensemble-kalman-closure-calibration.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [OpenFOAM](/software/openfoam.md)
