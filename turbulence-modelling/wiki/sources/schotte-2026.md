---
type: Source
title: "Schotte et al. (2026) — An anisotropic unstructured mesh adaptation strategy for Discontinuous Galerkin methods with application to compressible turbulent flow problems"
description: "Metric-based anisotropic mesh adaptation for steady SA-neg RANS with modal DG in CODA: a Mach-number Hessian from a DG weak form sets orientations and anisotropy, a DG small-scale error estimator sets element sizes; tested on HLPW4 and RAE2822 airfoils, the CRM-HL wing-body and the ONERA M6 wing."
resource: "doi:10.1016/j.compfluid.2026.107138"
source_kind: paper
authors: [Schotte A., Chapelier J.-B., Basile F., Laraufie R., Pernet S.]
year: 2026
venue: "Comput. Fluids 315:107138"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Computers_amp_Fluids_Schotte_An_anisotropic_unstructured_mesh_adaptation_strategy_for_Dis.pdf"
tags: [mesh-adaptation, dg, rans, spalart-allmaras, high-lift, compressible]
timestamp: 2026-10-26T20:51:00Z
---

# Summary

Schotte et al. (2026) propose a metric-based anisotropic
[mesh adaptation](/methods/mesh-adaptation.md) strategy for steady RANS with a
high-order modal discontinuous Galerkin discretization (hierarchical
orthonormal basis on simplices; the bundle's DG page is the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) one), in
the ONERA–DLR–Airbus solver CODA with the remesher Tucanos. The closure is the
negative [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
(SA-neg); transonic cases use Laplacian
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md) with
the Persson–Peraire sensor and a positivity limiter.

The continuous-mesh framework of Loseille and Alauzet gives an optimal metric
from the Hessian of a sensor, which controls the interpolation error exactly
only for piecewise-linear approximations. Instead of the costlier high-order
metric theories, the authors follow Venditti and Darmofal: the Hessian of the
Mach number fixes orientations and anisotropic quotients, while an isotropic
DG error estimator fixes element sizes. The element Hessian, computed by a DG
weak form projected onto constants, is divided by its "global density" and
multiplied by the estimator before entering the $L^4$-optimal metric. The two
estimators measure the energy of the highest-degree momentum modes (SSED, and
SSL, which adds a lifting term).

A priori tests on analytical functions show that the DG weak-form Hessian
beats Tucanos' reconstructions. With SA-neg RANS on the HLPW4 three-element
airfoil, the RAE2822 airfoil, the HLPW5
[CRM-HL](/benchmarks/nasa-crm-high-lift.md) wing-body at root-chord
$Re=5.6\times10^6$ and the ONERA M6 wing, the unscaled Hessian works for $N=1$
and acceptably for $N=2$, and scaling (best with SSL) improves $N=2$ and $N=3$.
Adapted DG beats uniformly refined finite-volume and finite-element results at
equal degrees of freedom, matches a lift-targeted goal-oriented solver at
intermediate complexity, and is similar in accuracy to a feature-based
adaptive finite-volume solver on the M6 wing.

# Version read

HAL deposit hal-05567956v2 (deposited 7 July 2026) of the journal-typeset
version of record (Elsevier layout, CC BY 4.0), 21 PDF pages (HAL cover and
journal pp. 1–20), all read; journal pp. 2–10 and 13 checked visually. Title,
authors, venue and DOI match Crossref. Locators are those of the journal
pages.

# Key claims

1. The main theoretical contribution is a size-based error indicator tailored for DG: the Mach-number Hessian gives orientations and anisotropic ratios, a DG spectral error estimator gives element sizes (Hessian scaling) (§1, §3.2, Eq. 21). **Stated** / **Derived**
2. To the authors' knowledge this is the first published demonstration of high-order DG metric-based adaptation for complex 3-D cases including a full high-lift aircraft configuration (§1). **Stated**
3. The implicit assumption is that the Hessian's orientations and anisotropic quotients stay adequate for $N=2$ and $N=3$, "a sweet spot for modal DG applied to complex configurations"; it "might become less and less valid as the order is increased" (§3). **Stated**
4. A Hessian constant per element suffices because the elements are linear; projecting $\nabla(\partial_iw)$ onto constants gives $H^*_K=\frac1{|K|}\int_{\partial K}\nabla w\,\boldsymbol n^\top d\gamma$, symmetrized as $H_K=\frac12[H^*_K+(H^*_K)^\top]$ (asymmetric through quadrature), with the face gradient the average of the two lifted gradients (§3.1, Eqs. 15–19). **Derived**
5. On the 2-D X-shaped function (complexity 5000, 7 iterations, $N=1$), the exact and the CODA BR1 Hessians give faster convergence of the $L^2$ interpolation error and a lower plateau; Tucanos' $L^2$-projection and least-squares Hessians and the CODA BR2 Hessian plateau higher and are "equivalent"; CODA BR1 is the optimal reconstruction (§3.3, Figs. 3–4). **Shown**
6. On the 3-D smooth-shock function (complexity 100 000, 15 iterations) the best meshes come "surprisingly" from BR1 and BR2; the CODA Hessians capture the small $yz$ variations that Tucanos misses because its Hessian uses a nodally interpolated solution; BR1 reaches the lowest plateau (§3.3, Figs. 6–7). **Shown**
7. The multiscale estimator in $L^4$ norm with the Mach Hessian is used for second-order computations; $L^4$ is chosen because it improves the convergence of the adaptation (§4.1). **Stated**
8. DG degree staging ($N=0$, then $N=1$ with higher modes zero, and so on) makes the implicit solver robust; solution transfer between meshes uses DG interpolation up to $N=1$ modes, "the best compromise between efficiency and robustness", except the CRM wing-body, restarted at $N=2$ "without any complications" (§4.1). **Stated**
9. Residuals are converged to $10^{-10}$ in 2-D and $10^{-6}$ in 3-D (§4.1; §2.4 says $10^{-6}$ for all). **Stated**
10. Three-element airfoil (HLPW4, $M=0.2$, $16°$, $Re_c=5\times10^6$): $N=2$ is more converged than $N=1$ at equal complexity; Table 2: $N=1$ 100 779 DOF, $C_L=3.796$, $C_D=0.06172$; $N=2$ 102 924, 3.798, 0.06104; $N=2$ SSED 106 050, 3.802, 0.06106; $N=2$ SSL 108 804, 3.802, 0.06092 (§4.2, Table 2). **Shown**
11. At $N=2$ Hessian scaling outperforms the unscaled Hessian, SSL slightly better than SSED (§4.2, Fig. 11). **Shown**
12. At $N=3$ scaled Hessians give better integrated values and boundary-layer meshes; unscaled, very large isotropic elements remain; "the Hessian without scaling does not represent well the error in $p=3$ and needs a correction"; spectral indicators gain efficiency with order (§4.2, Figs. 10, 12). **Shown** (last part **Stated**)
13. All adaptation strategies are more efficient than the FUN3D uniform refinement; the lift-targeted goal-oriented GGNS is more efficient at the coarser complexity, while at finer complexity $N=2$ SSL gives slightly more accurate drag and similar or slightly less accurate lift (§4.2). **Shown**
14. $C_p$ and $C_f$ of the adapted results agree with FUN3D (§4.2, Fig. 13). **Shown**
15. RAE2822 case 9 ($M=0.734$, $2.79°$, $Re_c=6.5\times10^6$): $N=1$ and $N=2$ SSL refine the shock more finely at similar DOF, SSED the least; Table 4: $N=1$ 67 395 DOF, $C_L=0.8235$, $C_D=0.01893$; $N=2$ 63 378, 0.8238, 0.01894; $N=2$ SSED 69 954, 0.8222, 0.01884; $N=2$ SSL 37 560, 0.8229, 0.01885; finite-volume hexahedra 230 084, 0.816, 0.0189 (§4.3, Table 4, Fig. 15). **Shown**
16. On RAE2822 the scaled strategies are less accurate on very coarse meshes but converge earlier, SSL with the fewest DOF; the adapted strategies "always provide a higher $C_l$ and lower $C_d$" than finite volume, whose results are not mesh converged on the finest grid (§4.3, Fig. 16; see Printed slips). **Shown**
17. CRM-HL wing-body (HLPW5, $M=0.2$, $11°$, $Re=5.6\times10^6$ on the root chord): SSL scaling captures the tip vortex better than the unscaled Hessian at $N=2$ ("+2 drag counts and +0.1 lift counts"); $N=2$ needs about $8\times10^6$ fewer DOF than $N=1$ for similar integrated values (§4.4, Figs. 19–21). **Shown**
18. On the CRM-HL wing-body all adapted DG strategies "clearly outperform FUN3D, CHAMPS and CODA FV solutions" in drag and lift; $N=1$ drag is slightly less accurate except at the finest complexity, equivalent to USM3D at equal DOF (§4.4, Figs. 20–21). **Shown**
19. The unscaled Mach Hessian "still performs well with $p=2$" on the CRM, which the authors call "surprising" (§4.4). **Shown**
20. Adaptation reaches near-wall $y^+$ close to 1 on the CRM at $N=1$, with anisotropic ratios up to $10^5$ (§4.4, Fig. 22). **Shown**
21. ONERA M6 (case 2308, $M=0.84$, $3.06°$, $Re=14.6\times10^6$ on the root chord) is run at $N=1$ only, because high-order steady implicit runs with shocks do not converge systematically and unconverged solutions corrupt the estimators; lambda shock, boundary layer, wake and tip vortex are captured (§4.5, Fig. 23). **Shown** / **Stated**
22. On the M6 wing results are "overly dissipative at lower mesh complexities" but improve with complexity; converged adapted results beat non-adaptive benchmarks and match Wolf with feflo.a using the same estimator; $C_p$ cuts match NASA data (§4.5, §5, Figs. 24–25). **Shown**
23. $N=1$ and $N=2$ complexities are chosen to conserve DOF; for $N=3$ this was impossible because linear boundary elements constrain the element count; curved boundary elements are a perspective (§4.2). **Stated**
24. Perspectives: $hp$-adaptation ($N=1$ at shocks, higher $N$ in smooth high-error regions) and curved boundary elements (§4.5, §5). **Stated**
25. The compact DG stencil allows exact residual Jacobians for implicit steady RANS, unlike finite-volume schemes with extended stencils on skewed tetrahedra (§1). **Stated**

# Printed slips

- §2.1 defines $\mathbf S=(\nabla\mathbf v+(\nabla\mathbf v)^\top)$ without the factor $\frac12$, while Eq. 3 writes $\boldsymbol\tau=2\mu\mathbf S^D=\mu(T)(\nabla\mathbf v+(\nabla\mathbf v)^\top-\frac23(\nabla\cdot\mathbf v)\mathbf I)$, which needs $\mathbf S=\frac12(\nabla\mathbf v+(\nabla\mathbf v)^\top)$ *(compiler check, not in the sources)*.
- Eq. 20 writes $H_K=d_K^{2/d}\mathcal R_K^\top\mathrm{diag}(r_{i,K}^{-2})\mathcal R_K$ with the global density $d_K=\sqrt{\det H_K}|K|$; with Eq. 12's quotients the right-hand side equals $|K|^{2/d}H_K$, the identity holding only for the pointwise density of Eq. 14 *(compiler check, not in the sources)*.
- Eq. 22 labels the estimator $e^{SSE}_K$ in the section on SSED (SSED is Eq. 23).
- §3.3: domain "$\Omega=[-0.5,0,5]^3$" for $[-0.5,0.5]^3$.
- Fig. 10 caption: "complexity $\mathcal C=80000$", a value absent from Table 1.
- §2.4 gives residual convergence "up to $10^{-6}$ for all residuals", §4.1 gives $10^{-10}$ in 2-D.
- §4.3: "the artificial viscosity method described in is employed" (missing reference).
- §4.3: "always provide … lower $C_d$ compared to the Finite Volume simulations", while Table 4 prints finite-volume $C_D=0.0189$ against 0.01893 ($N=1$) and 0.01894 ($N=2$).
- §4.3 "(see Table 3)" and §4.4 "(see Table 5)" point to tables of adaptation complexities for reference-solver results.
- Ref [41] prints the authors as "Xavier Garnaud Jérôme Robert"; ref [42] carries database residue; ref [44], an INRIA report, is labelled "(Ph.D. thesis)".

# Notation map

| Schotte et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$ (DG degree), DG-$p1$ | $N$ | **collision:** $p$ is also the $L^p$ exponent ($L^4$) |
| $\mathrm p$ | $p$ | pressure |
| $\mathbf v$ | $\boldsymbol u$ | velocity; the source's $\mathbf u$ is the conservative vector |
| $\boldsymbol\tau=2\mu\mathbf S^D$ | $\sigma_{ij}=2\mu S^d_{ij}$ | see Printed slips for $\mathbf S$ |
| $P_r$ | $Pr$ | 0.72 |
| $K$, $\lvert K\rvert$, $h$ | (element, its volume), $h$ | |
| $N$ | (number of elements; complexity in Eq. 10) | **collision:** $N$ is the polynomial degree in the registry |
| $\eta$ | (BR2 stabilization parameter, 3 in 2-D, 4 in 3-D) | **collision:** $\eta$ is the Kolmogorov length in the registry |
| $\mathcal M$, $\mathcal C(\mathcal M)$ | (metric tensor, complexity) | |
| $H_u$, $H_K$ | (Hessian of the sensor; element Hessian) | |
| $\mathcal R$, $\lambda_i$, $h_i$, $r_i$, $d$ | (orientations, eigenvalues, sizes, anisotropic quotients, density) | **collision:** $d$ is also the dimension and the wall distance in the registry |
| $e_K^{SSED}$, $e_K^{SSL}$ | (DG small-scale error estimators) | |
| $\beta$, $t$ | (gradation parameters) | **collision:** not the field-inversion $\beta$ |
| $M_\infty$, $Re_c$, $Re_{c_{root}}$ | $M$, $Re_c$ (chord, root chord) | |
| $C_l$, $C_d$ | $C_L$, $C_D$ | |

# Reference list

52 printed references, numbered. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. [10] (Alauzet et
al. 2022) is the ingested source alauzet-2022 and [19] (Basile et al. 2023)
the ingested source basile-2023. Undated web pages ([5], [6], [49], [51],
[52]) take the citing year with a note. No printed duplicates.

# Pages created or updated

Chunk 7 (2026-10-26), cited further in chunk 8. This source is cited on:

- [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
