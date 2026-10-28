---
type: Source
title: "Fanizza et al. (2025) — Adjoint-based optimization for non-linear inverse problems with high-order discretization of the compressible RANS equations"
description: "Discrete-adjoint field inversion of the compressible Spalart–Allmaras RANS model on a high-order modal discontinuous Galerkin discretization, comparing four correction terms on a laminar circular cylinder, a square cylinder and a supersonic shock–boundary-layer interaction, with dense and sparse wall-pressure data."
resource: "doi:10.1016/j.apm.2025.115984"
source_kind: paper
authors: [Fanizza B., Stefanin Volpiani P., Renac F., Martin E., Sipp D.]
year: 2025
venue: "Appl. Math. Model. 142:115984"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Applied_Mathematical_Modelling_Fanizza_Adjoint-based_optimization_for_non-linear_inverse_problems_w.pdf"
tags: [rans, field-inversion, spalart-allmaras, dg, compressible, separated-flow]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Fanizza et al. (2025) carry out the inversion step of
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
(variational data assimilation, without the learning step) for the steady
compressible [Spalart–Allmaras model](/methods/spalart-allmaras-model.md).
The model is discretized with a high-order modal discontinuous Galerkin method
in ONERA's Aghora code: BR2 viscous fluxes, Roe or local Lax–Friedrichs
convective fluxes, and an orthonormal modal basis. That basis is a relative of
the nodal [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md),
not the DGSEM itself. The authors argue that corrections inferred on diffusive
second-order finite-volume discretizations also absorb discretization error, so
high-order discretizations are needed for the corrections to carry model error
only ([model-form uncertainty](/definitions/model-form-uncertainty.md)).

The correction field is sought in the DG space. Its gradient comes from a
discrete adjoint, solved by flexible inner–outer GMRES with a single-precision
inner solve. A mass-matrix change of variable makes the gradient passed to
L-BFGS mimic the continuous inner product. Ensemble Kalman methods are named as
an alternative for steady problems
([ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)).
Four corrections are compared: a momentum and energy source, an eddy-viscosity
multiplier, a source proportional to $\tilde\nu$ in the SA equation, and a
production multiplier. They are tested in three cases:
- a laminar [circular cylinder](/benchmarks/circular-cylinder-wake.md) at
  $Re=80$, against time-averaged DNS;
- a [square cylinder](/benchmarks/square-cylinder-flow.md) at $Re=22\,000$;
- a [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  at $M_\infty=2.28$.

All three take their reference data from
[direct numerical simulation](/definitions/direct-numerical-simulation.md).

The square-cylinder ranking (momentum source first, eddy-viscosity multiplier
failing) agrees with the incompressible study of
[Cato et al. (2023)](/sources/cato-2023.md). In the interaction, only the
momentum source corrects the near-wall flow and $C_f$ with dense velocity data.
The authors attribute this to its independence from the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md). With sparse
wall-pressure data the momentum source cuts the $C_p$ error by three orders of
magnitude but leaves $C_f$ wrong, and an $L^2$ penalty does not repair it.

# Version read

The version of record (Elsevier typeset, open access CC BY 4.0, 24 pages), all
read. Pages 4, 7, 8, 11, 20 and 21 were also checked visually for equations
and tables. Title, five authors, venue and DOI on page 1 match the published
identity, and there is no identity problem.

# Key claims

Page-local symbols: $\boldsymbol f_{\mathrm{DA}}$ is the momentum and energy
correction source (multiplied by $\rho$). $\varphi$ is the eddy-viscosity
multiplier, entering as $(1+\varphi)\mu_t$ (the source's $\chi_h$).
$g_{\tilde\nu}$ (registry §11) is the proportional SA source, entering as
$\rho\tilde\nu g_{\tilde\nu}$ (the source's $f_{\tilde\nu}$; Cato et al.'s
$g_{\tilde\nu}$). $\beta$ is the production multiplier with prior 1 (the
source's $1+\beta$). These labels follow the field-inversion page. $\alpha_p$
is the penalty weight.

1. Corrections learned on low-order, diffusive second-order finite-volume discretizations are likely to contain a strong discretization component and may not extrapolate to other meshes or codes. High-order discretizations will be "mandatory" if learned corrections are to compensate only modelling errors (§1). **Stated**
2. Before this work FIML had mostly used low-order discretizations, "with the notable exception of Ferrero et al. [26], who used a DG method to treat subsonic flows" (§1). **Stated**
3. DG methods reach accuracy comparable to finite volumes with fewer degrees of freedom, which shrinks the optimization problem. They "handle shock capturing as effectively as FV methods and outperform continuous finite element methods in this regard" (§1). **Stated**
4. On the first square-cylinder adjoint system, GMRES(180) with block ILU(0) does not converge. FGMRES (outer and inner Krylov sizes 60) converges in 12 000 matrix–vector products, and FGMRES-DR, recycling 18 deflation vectors per restart, in 8000. Preconditioned GMRES would need a Krylov size of 860 to match FGMRES, "at prohibitive or even unaffordable costs", so flexible inner–outer solvers "turn out to be necessary" for such stiff adjoint problems (§3.4.1, Fig. 2). **Shown**
5. The inner preconditioned GMRES runs in single precision with single-precision matrices, which "allows to half the memory for matrix storage" and speeds up the computation. The forward solver also stores its block-ILU(0) preconditioner in single precision (§3.4.1, §2.4). **Stated**
6. The gradient is passed to L-BFGS in the variable $\tilde{\boldsymbol\Theta}=\mathbf L\boldsymbol\Theta$, with $\mathbf M=\mathbf L^\top\mathbf L$ the diagonal mass matrix of the orthonormal modal basis. This lets L-BFGS, which uses canonical inner products, work with a gradient that mimics the continuous inner product (§3.4.2, Eqs. 37–41). **Derived**
7. Laminar cylinder ($Re=80$, $M=0.15$): the steady baseline overestimates the wake. The momentum source with dense velocity data and no penalty gives axial momentum "in good agreement with DNS for all polynomial degrees" $N=1,2,3$ (§4.1, Figs. 4–5). **Shown**
8. Laminar cylinder: the cost falls by more than three orders of magnitude at $N=1$ and more than four at $N=2$ and $N=3$, with the lowest value at $N=2$, the lowest degree at which the baseline is free of mesh-dependency errors. Higher degrees add degrees of freedom that the mean flow does not need and that complicate the optimization (§4.1, Fig. 6). **Shown**
9. Recommendation: "conduct DA problems at the lowest degree $p$ for which the baseline model exhibits no grid-dependency errors" (§4.1). **Stated**
10. Square cylinder ($Re=22\,000$, $M=0.1$, $N=2$, DNS of Trias et al. [56]): RANS overestimates the recirculation bubble. The momentum source corrects the velocity best, followed by $g_{\tilde\nu}$ and $\beta$, while $\varphi$ "lacks precision" and cannot correct the flow. This agrees with Cato et al. [10] (§4.2, Fig. 7). **Shown**
11. Square-cylinder cost: $\varphi$ stalls on a plateau "from the very first iterations". The cost falls by at least one order of magnitude with $\beta$, more than one with $g_{\tilde\nu}$ and more than two with the momentum source (§4.2, Fig. 8). **Shown**
12. The momentum source needs more iterations on the square cylinder. The authors attribute this to an optimization problem three times larger than with $g_{\tilde\nu}$: in 2D, two momentum scalars and one energy scalar against one SA scalar (§4.2). **Stated**
13. Interaction with dense data (cost weighted by wall distance, Eq. 42): only the momentum source reduces the cost, by one to two orders of magnitude, while $\varphi$, $g_{\tilde\nu}$ and $\beta$ stay on a plateau (§4.3.1, Fig. 9). Normalized errors (velocity / $C_p$ / $C_f$, Table 1): momentum source 0.049 / 0.1825 / 0.0998; $\varphi$ 0.250 / 0.5788 / 0.5689; $g_{\tilde\nu}$ 0.257 / 0.2076 / 0.8920; $\beta$ 0.339 / 0.2829 / 1.1450. **Shown**
14. "Only the source term $\mathbf f_{\rm DA}$ allows to improve the prediction of physical quantities which do not appear explicitly in the cost function" (§4.3.1). **Shown** (Table 1)
15. The corrections $\varphi$, $g_{\tilde\nu}$ and $\beta$ "are still constrained by the Boussinesq assumption", while the momentum source corrects the divergence of the Reynolds stress and does not depend on it. The authors give this as a second reason for its better near-wall reconstruction in the interaction, where the Reynolds stress is not aligned with the viscous stress (§4.3.1). **Stated**
16. With dense data the momentum source matches the DNS in the boundary layer ($x=30$), at separation ($x=32.5$), at the shock reflection ($x=35$) and downstream ($x=37.5$). $C_f$ still mismatches in the first part of the bubble but agrees at and after reattachment, and the wall pressure improves strongly where the shock impinges (§4.3.1, Figs. 11–12). **Shown**
17. Degree and mesh (momentum source): on the $350\times250$ grid, $N=1$ (grid-converged there) gives the lowest minimum of the six runs. On the $175\times125$ grid, $N=2$ (grid-converged there) does. The coarse-grid $N=2$ run "converges to a local minimum" with satisfactory velocity and bubble size at half the optimization size (§4.3.2, Fig. 13). **Shown**
18. The interaction needs the steady problem to converge at every optimizer iteration. Accurate wall quantities need high-fidelity data interpolated onto grids refined enough near the wall (§4.3.2). **Stated**
19. Interaction with sparse data (wall $C_p$ only, Eq. 43; Table 2), velocity / $C_p$ / $C_f$: momentum source 0.488 / 0.00106 / 0.8540; $\varphi$ 0.458 / 0.17357 / 1.657; $g_{\tilde\nu}$ 0.542 / 0.04961 / 1.700; $\beta$ 0.427 / 0.05982 / 1.559. The momentum source reduces the $C_p$ error by three orders of magnitude, and all four reduce the velocity error by about the same amount. The three Boussinesq-type corrections make $C_f$ worse than the baseline over the whole wall (§4.3.3). **Shown**
20. With sparse wall-pressure data the velocity improves everywhere except near the wall at the bubble, and $C_f$ still disagrees with the DNS (§4.3.3, Figs. 14–15). **Shown**
21. An $L^2$ penalty on the correction (Eq. 44) degrades the velocity and wall-pressure errors and improves the skin-friction error, "particularly when the penalty is sufficiently strong to outweigh the objective function" (§4.3.4, Table 3). **Shown** (see Printed slips)
22. With the penalty the norm of every correction falls (Table 4), but the near-wall mean velocity and $C_f$ "did not significantly improve". Advanced regularization using prior knowledge of the flow physics or of turbulence modelling is needed for sparse data (§4.3.4, §5). **Shown**/**Stated**
23. The Tapenade-differentiated adjoint gradient for $\varphi$ agrees with a forward finite-difference estimate. The large relative error at small steps is attributed to numerical error in the division (App. A, Fig. A.16). **Shown**
24. Discrete adjoints give more accurate gradients than continuous adjoints and avoid deriving adjoint equations and boundary conditions, but can cost more in large 3D computations. Continuous-adjoint gradient errors are "generally small enough" in most practical cases, citing [15] (§1). **Stated**
25. Correction fields can detect failures of RANS models and guide models that add terms to the linear Boussinesq Reynolds stress (§5). **Stated**

# Printed slips

- **Penalty weights, Table 3 against Table 4 (pp. 20–21):** for $g_{\tilde\nu}$, Table 3 prints $\alpha_p=10^{-3},10^{-2}$ and Table 4 prints $10^{-4},10^{-3}$. For $\beta$, Table 3 prints $10^{-4},10^{-3}$ and Table 4 prints $10^{-3},10^{-2}$. The momentum-source and $\varphi$ values agree.
- **§4.3.4 against Tables 2–3:** the text says the velocity and wall-pressure errors "are degraded, due to the introduction of the penalty term". Tables 2 and 3 print velocity errors that rise only for the momentum source (0.488 to 0.502 and 0.515). They fall for $\varphi$ (0.458 to 0.406 and 0.433) and for $g_{\tilde\nu}$ (0.542 to 0.395 and 0.431), and for $\beta$ they print 0.427 against 0.416 and 0.513. The $C_p$ error for $\varphi$ at $\alpha_p=10^{-5}$ falls (0.17357 to 0.1576).
- **§4.3.1 against Table 1:** "For the other three DA tests, the three errors are reduced by less than one order of magnitude", while Table 1 gives the $\beta$ correction a $C_f$ error of 1.1450, above the baseline's normalized value of 1.
- **Fig. 3 against Eq. (40):** Fig. 3 computes $\mathbf G=\nabla_\Theta\mathcal J_h$ "by Eq. (41)" and then $\tilde{\mathbf G}=\mathbf L\mathbf G$. Eq. (40) gives $(\mathbf L^\top)^{-1}\nabla_\Theta\mathcal J_h$ for the same quantity. From Eqs. (37)–(38), $\delta\mathcal J_h=\mathbf G^\top\mathbf L^{-1}\delta\tilde{\boldsymbol\Theta}$, so Eq. (40) holds, and $\mathbf L\mathbf G$ equals it only if $\mathbf G$ is the mass-scaled gradient $\mathbf M^{-1}\nabla_\Theta\mathcal J_h$ *(compiler check, not in the sources)*.
- **Dimension of the momentum-source space (§3.3):** printed $\mathbf f_{\rm DA}\in(\mathcal V_h^p)^{d+2}$. The printed vector has $d+3$ components, and the derivative matrix of Eq. (24) has $d+1$ free columns.
- **Eddy-viscosity multiplier (§3.3):** printed $(1+\chi_h)\mu_t(\nabla\mathbf v+\nabla\mathbf v^\top-\tfrac23\mathrm{Tr}(\nabla\mathbf v))$ without the identity, which §2.1 writes as $-\tfrac23(\nabla\cdot\mathbf v)\mathbf I$.
- **Polynomial space (§2.3):** called "tensor products of polynomials and of total degree at most $p$", while $N_p=(p+d)!/(p!d!)$ and the counts 3, 6, 10 at $p=1,2,3$ are total-degree dimensions.
- **Coarse-grid wall resolution (§4.3.2):** halving the elements in each direction is said to raise $\Delta y^+_{\mathrm{wall}}$ "by a factor of four", which the paper does not explain.
- **Eq. (42)** prints the weight $w(\mathbf x)$ outside the $L^2$ norm.
- **Typos:** "spacial" (several), "is attempt" (abstract), "computed form the adjoint approach" and "finite different approach" (App. A).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u=(\rho,\rho\mathbf v^\top,\rho E,\rho\tilde\nu)^\top$ | $(\rho,\rho\boldsymbol u,E,\rho\tilde\nu)$ | **collision:** the source's $\mathbf u$ is the state vector and $\mathbf v$ the velocity; the source's $E$ is per unit mass |
| $\tilde\nu$ | $\tilde\nu$ | SA working variable; agrees |
| $\hat\chi=\rho\tilde\nu/\mu$ | $\chi=\tilde\nu/\nu$ | equal; the hat is not a test filter |
| $\mu_t=\rho\tilde\nu f_{v1}$ | $\mu_t$ | agrees |
| $\boldsymbol\tau_l$ | $\sigma_{ij}$ | viscous stress |
| $\boldsymbol\tau_t=\mu_t(\nabla\mathbf v+\nabla\mathbf v^\top-\tfrac23(\nabla\cdot\mathbf v)\mathbf I)$ | $-\langle\rho\rangle(R_{ij}-\tfrac23k\delta_{ij})$, modelled as $2\mu_tS^d_{ij}$ | **sign:** a momentum flux added to the viscous stress; no $k$ term (SA has no $k$) |
| $\varkappa=0.41$ | $\kappa$ | |
| $d_w$ | $d$ | wall distance |
| $\tilde S=\lVert\nabla\times\mathbf v\rVert_2+\tilde\nu f_{v2}/(\varkappa^2d_w^2)$ | $\tilde S$ (SA modified vorticity) | **collision:** not a strain magnitude |
| $c_{b1}$, $c_{b2}$, $\sigma$, $c_{v1}$, $c_{w1}$–$c_{w5}$ | same | SA constants; $c_{w4}=0.21$, $c_{w5}=1.5$ (Spalart–Garbaruk) |
| $p$ (DG degree) | $N$ | **collision:** also the pressure $p$ |
| $k$ (element size) | $h$ | **collision:** not the turbulent kinetic energy |
| $\omega_n$ (quadrature weights) | $w_n$ | **collision:** not the specific dissipation rate |
| $N_p=(p+d)!/(p!d!)$, $N_g=(p+1)^d$ | (page-local) | modal basis size, quadrature points |
| $\mathbf f_{\rm DA}=(0,\mathbf f_{xyz},f_e+\mathbf v^\top\mathbf f_{xyz},0)^\top$ | $\boldsymbol f_{\mathrm{DA}}$ (page-local) | **collision:** not the body force $f_i$ alone |
| $\chi_h$, $(1+\chi_h)\mu_t$ | $\varphi$, $(1+\varphi)\mu_t$ (page-local) | as on the field-inversion page |
| $\rho\tilde\nu f_{\tilde\nu}$ | $\rho\tilde\nu g_{\tilde\nu}$ (registry §11) | Cato et al.'s proportional source |
| $(1+\beta)c_{b1}\tilde S\rho\tilde\nu$ | $\beta\,c_{b1}\tilde S\rho\tilde\nu$ | the source's $\beta$ is the registry's $\beta-1$ (prior 0 against prior 1) |
| $\mathcal J_h$, $\mathcal M$, $\mathcal P$, $\alpha_p$ | $\mathcal L$, (measurement and penalty operators), $\alpha_p$ | cost function (Eq. 18) |
| $\mathbf Z$, $\mathbf M=\mathbf L^\top\mathbf L$, $\tilde{\boldsymbol\Theta}$ | (adjoint state, mass matrix, scaled control) | page-local |
| $\delta_0$ | $\delta$ | inlet boundary-layer thickness of the interaction |
| $C_p$, $C_f$ | $C_p$, $C_f$ | agree; $C_p$ is also the specific heat in §2.1 ($c_p$ in the registry) |
| a priori / a posteriori metrics (§3.5) | — | **collision:** metrics inside or outside the cost function, not the registry's a priori and a posteriori testing |

# Reference list

74 printed references, numbered [1]–[74], all parsed. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. [10] is the ingested [cato-2023](/sources/cato-2023.md), printed with the
DOI only, and ref. [24] is the ingested
[duraisamy-2019](/sources/duraisamy-2019.md). Ref. [22] (Liu, Zhang & Xia
2022, Aerosp. Sci. Technol. 126:107328) received the printed key `liu-2022`,
which belongs to a different ingested work, and is re-keyed `liu-2022-f`.
Refs. [10], [11], [14], [72] and [73] print DOIs without article numbers.
Ref. [4] prints the year 2005 for J. Appl. Mech. 73(3). Ref. [37] is ICCFD7
with a URL, [52] a thesis with a theses.fr URL, [55] a chapter of the IDIHOM
book and [74] ETMM14 proceedings. No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Flow past a square cylinder](/benchmarks/square-cylinder-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Ensemble Kalman filter calibration of turbulence closures](/methods/ensemble-kalman-closure-calibration.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
