---
type: Source
title: "Fidkowski (2022) — Output-based error estimation and mesh adaptation for unsteady turbulent flow simulations"
description: "Adjoint-weighted-residual output error estimates and mesh adaptation for time-averaged outputs of chaotic flows without unsteady adjoints: a field-inversion-corrected Spalart–Allmaras RANS model fitted to the mean unsteady state supplies a steady surrogate adjoint, driving p-adaptation and anisotropic metric optimization in a high-order DG solver on 2-D airfoils."
resource: "doi:10.1016/j.cma.2022.115322"
source_kind: paper
authors: [Fidkowski K.J.]
year: 2022
venue: "Comput. Methods Appl. Mech. Engrg. 399:115322"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Fidkowski_Output-based_error_estimation_and_mesh_adaptation_for_unstea.pdf"
tags: [mesh-adaptation, error-estimation, adjoint, field-inversion, dg, spalart-allmaras]
timestamp: 2026-10-27T15:30:00Z
---

# Summary

Fidkowski (2022) addresses output-based (adjoint-weighted-residual) error
estimation and [mesh adaptation](/methods/mesh-adaptation.md) for unsteady
chaotic simulations, whose time-averaged outputs such as the mean lift are
of engineering interest but whose unsteady adjoints are unstable (shown for
all three test cases) or need costly regularization. The author avoids the
unsteady adjoint: for statistically steady flows, a steady augmented model,
the [Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS equations
with the production term multiplied by a correction field
$\beta(\boldsymbol x)$, is trained by
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
to reproduce the time-averaged unsteady state. Its steady adjoint,
restricted to the original Navier–Stokes residual components, serves as a
surrogate for the time-averaged unsteady adjoint.

Two estimates follow: E1 weights a time-averaged fine-space ($N+1$)
unsteady residual perturbation, sampled during the unsteady run, by this
surrogate adjoint; E2 is the steady adjoint-weighted residual of the
augmented system. A new inversion objective weights the state mismatch by
the adjoint times the element residual Jacobian, so that the inversion also
targets interior accuracy where the output is sensitive. The element
indicators drive fixed-fraction $N$-adaptation and anisotropic metric
optimization (MOESS) in a high-order DG solver (Roe and BR2 fluxes, $N=2$;
see the [DGSEM page](/methods/discontinuous-galerkin-spectral-element-method.md)
for the bundle's DG material), with 2–4 unsteady runs per adapted mesh and
no state storage or checkpointing.

The tests are 2-D: the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at
$M=0.2$, $7^\circ$, $Re=10^4$ (unsteady laminar separation) and
$Re=2\times10^4$ (a [laminar separation bubble](/definitions/laminar-separation-bubble.md)
with breakdown near 40% chord and reattachment near 60%), and a high-lift
airfoil at $17^\circ$, $Re=10^6$ computed with a simplified
[DES](/methods/detached-eddy-simulation.md) whose wall distance is
attenuated by a fixed, mesh-independent function. FIML-based MOESS converges
the mean lift with fewer degrees of freedom than uniform, residual-based and
RANS-based refinement; estimates are within about a factor of 2 late in the
adaptation. Adapting on the uncorrected RANS model converges to a wrong lift
with small error estimates, because [model-form error](/definitions/model-form-uncertainty.md)
dominates there.

# Version read

Version of record (Comput. Methods Appl. Mech. Engrg. 399 (2022) 115322;
received 8 April 2022, available online 18 July 2022), 28 pages (main text
pp. 1–25, references pp. 25–28), all read; Eqs. (2), (5), (7), (11)–(13),
(19)–(23) and Fig. 1 also read visually. Page-1 title, single author and
DOI match the metadata. No identity problem. Numbering on this page is that
of this version.

# Key claims

Page-local symbols: $\Psi$ the discrete output adjoint, $\bar\Psi$ and
$\Psi'$ its time mean and fluctuation (the source's overbar is a time
average, not an LES filter); $J$ the output; $\mathbf R$ the spatial
residual; $\tilde{\mathbf U}$, $\tilde{\mathbf R}$, $\tilde\Psi$ the state,
residual and adjoint of the augmented (corrected RANS) system (the tilde is
neither a Favre filter nor the SA variable); $\mathbf I^r$ the restriction
from augmented to original states; $\mathcal F^{\mathrm{dist}}$,
$\mathcal F^{\mathrm{AWR}}$ the inversion objectives; $\gamma_{\mathrm{Tik}}$
the Tikhonov weight (the source's $\gamma$).

1. Unsteady adjoints are unstable for chaotic systems, which prevents their direct use in long-time sensitivities or error estimates; long averaging times also make adjoint storage impractical (§1). **Stated**
2. The direct unsteady adjoint of the time-averaged lift is unstable in each of the three test cases (Figs. 4, 11, 17). **Shown**
3. The method needs one unsteady primal simulation per adaptive iteration and no state storage or checkpointing; only the time-averaged state and, for E1, the time-averaged fine-space residual are stored (§1, §3, §5.3). **Stated**
4. Splitting $\Psi=\bar\Psi+\Psi'$, $\delta\mathbf R=\delta\bar{\mathbf R}+\delta\mathbf R'$ gives $\delta\bar J\approx\bar\Psi^T\delta\bar{\mathbf R}+\frac1{T_f-T_i}\int\Psi'^T\delta\mathbf R'\,dt$; for chaotic statistically steady problems the author assumes the first term dominates because adjoint and residual fluctuations decorrelate (§4, Eqs. 17–18). **Derived** (with that assumption)
5. For an augmented system that keeps the original residuals additively (Eq. 7), the restricted augmented adjoint $\mathbf I^r\delta\tilde\Psi_h$ is the output sensitivity to perturbations of the original residual, and is used as the surrogate $\delta\bar\Psi_h\approx\mathbf I^r\delta\tilde\Psi_h$ (§4, Eq. 23); this would be lost if the steady system were entirely new equations. **Derived**
6. The estimates are good only when the FIML correction is small: the first term of Eq. (23) must not be small against the other two (§4). **Stated**
7. Being residual-based, E1 and E2 vanish asymptotically with refinement, although they need not converge to the actual unsteady error (§4). **Stated**
8. The conservative estimate $\sum_e|\delta\Psi_e^T\delta\mathbf R_e|$ is more robust for chaotic simulations, avoiding unpredictable inter-element cancellation, but is not a bound; underestimation is possible on under-resolved meshes (§5.1, Eq. 24). **Stated**
9. Field inversion by L-BFGS (10-update history, 20 iterations, each a steady RANS solve) lowers the objective by 2–3 orders of magnitude and then stagnates; its cost is at least an order of magnitude below the unsteady simulation (§3.1). **Stated**
10. A broad range of $\gamma_{\mathrm{Tik}}$ is acceptable; the default is $10^{-7}$ (§3.1). **Stated**
11. The network (one hidden layer of 30 sigmoid neurons, inputs the dimensional state, its gradient and the wall distance; Adam, learning rate 0.001, mini-batch 1000, 500,000 iterations) costs at least two orders of magnitude less than the unsteady solve; it is a single-use model retrained at each adaptive iteration, not a general closure (§3.2). **Stated**
12. With E2 several cheap steady MOESS iterations can be sub-cycled on the augmented system, so 2–3 unsteady simulations suffice; with E1, 3–4 unsteady simulations reach the optimal mesh (§5.2). **Stated**
13. NACA 0012, $Re=10^4$: the uncorrected RANS converges quickly but under-predicts the mean lift (modelling error); FIML MOESS gives very good results even at 3000 degrees of freedom; output-based $N$-adaptation is the only other close approach, residual-based $N$-adaptation does not approach the correct lift (§6.1, Fig. 5). **Shown**
14. The E1 estimates of $N$-adaptation are "reasonably accurate (within a factor of 2)" (§6.1, Fig. 7). **Shown**
15. At 9000 degrees of freedom ($Re=10^4$): E1 with $\mathcal F^{\mathrm{dist}}$ gives output 0.7355, estimate 0.0057, actual error 0.0045; E1 with $\mathcal F^{\mathrm{AWR}}$ 0.7353, 0.0051, 0.0047; E2 with $\mathcal F^{\mathrm{dist}}$ 0.7175, 0.0087, 0.0225. E2 adaptation converges slowest, attributed to less trailing-edge refinement, which matters more for the unsteady simulation than for steady RANS (§6.1, Table 1). **Shown**
16. $\mathcal F^{\mathrm{AWR}}$ gives tighter estimates than $\mathcal F^{\mathrm{dist}}$, while the actual errors change little, attributed to better interior FIML fields and adjoint (§6.1, Table 1, Fig. 3). **Shown**
17. Output-adapted meshes for the unsteady flow have thicker, more isotropic boundary-layer refinement and refinement where the upper-surface laminar flow breaks into vortices; RANS-adapted meshes have highly anisotropic elements along the surface (§6.1, Fig. 9). **Shown**
18. NACA 0012, $Re=2\times10^4$: breakdown at about 40% chord and a separation bubble reattaching at about 60%; the uncorrected RANS gives no bubble and a persistent, mesh-independent lift error with imperceptibly small estimates (§6.2, Figs. 10, 12). **Shown**
19. At 20,250 degrees of freedom ($Re=2\times10^4$), E1 with $\mathcal F^{\mathrm{AWR}}$ gives output 0.6569, estimate 0.0024, actual error 0.0011; this combination performs best and, except on the coarsest mesh, gives the most reliable estimates (§6.2, Table 2). **Shown**
20. Residual-based $N$-refinement oscillates away from the exact value in the last adaptive iterations (§6.2). **Shown**
21. High-lift airfoil, $Re=10^6$: RANS severely under-predicts lift with a larger separation (modelling, not discretization, error); FIML methods approach the exact output with decreasing estimates, which at the finest meshes over-predict the error by about a factor of two, attributed to the conservative sum (§6.3, Fig. 18, Table 3). **Shown**
22. From a poor isotropic 13,500-degree-of-freedom mesh, FIML MOESS with E1 recovers in about three adaptive iterations, with accurate estimates from the fourth (§6.3, Fig. 19). **Shown**
23. The simplified DES replaces the mesh-dependent DES length by a fixed attenuation of the wall distance, $d\leftarrow d_{\max}\tanh(d/d_{\max})$ with $d_{\max}=0.02$ chord, to remove model changes across adapted meshes; applying the method to more realistic DES models is called a natural extension (§2.1, Eq. 3). **Stated**
24. Conclusions: estimates are reasonably accurate, especially late in the adaptation; E1 is slightly better than E2; unweighted-residual adaptation performs poorly, distracted by wake and far-field residuals; uncorrected RANS adaptation gives incorrect results, and the cases were chosen outside the usual applicability of RANS (§7). **Shown** / **Stated**
25. The method extends directly to 3-D, not attempted because of cost (§7). **Stated**
26. The time step is fixed a priori so that the spatial error dominates the temporal one by at least an order of magnitude; the statistical error is monitored by splitting the averaging window into two halves (§5.3). **Stated**

# Printed slips

- **§2.3, p. 4:** "The adjoint, as a residual sensitivity, then weights the
  adjoint to produce the output error."
- **§7 against §6.1:** §7 calls the $Re=10^4$ case "low-Reynolds number
  large-eddy simulation", while §6.1 describes the unsteady runs as the
  compressible Navier–Stokes equations without a turbulence model.
- **§7:** the summary says the correction is determined "using the surface
  stress distribution as the figure of merit", without the paper's own
  $\mathcal F^{\mathrm{AWR}}$ objective.
- **p. 25:** the single-author paper prints "The authors declare…".
- **References:** [14] "compution"; [2] "372 (2022) (2014)"; [41] "AIAA J.
  Aircraft"; [50] "ICCFD7, (1902) 2012"; [47] no venue; [40] no volume or
  pages; [71] issue "(15)".

# Notation map

| Fidkowski | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, $p_e$ | $N$ | DG polynomial degree (per element); default 2, maximum 5 in the code |
| $N$ | (number of discrete unknowns) | **collision** with the registry $N$, the polynomial degree |
| $h$, $H$ (subscripts) | (fine $N+1$ and coarse spaces) | not the cell size |
| $\tilde\nu$, $P$, $D$, $f_n$, $c_{b2}$, $\sigma$ | $\tilde\nu$, (SA production, destruction, negative-SA function, constants) | conservative negative-SA form; constants not printed |
| $\beta(\vec x)$, $\boldsymbol\beta$ | $\beta(\boldsymbol x)$ | production multiplier, nominal 1, $N=1$ DG field |
| $d$, $d_{\max}$ | $d$, (attenuation distance) | |
| $\bar{\mathbf U}$, $\bar J$, $\bar\Psi$ | $\langle\cdot\rangle$ (time average) | the overbar is not an LES filter here |
| $\tilde{\mathbf U}$, $\tilde{\mathbf R}$, $\tilde\Psi$ | (augmented-system quantities, page-local) | **collision:** the tilde is not a Favre filter |
| $\Psi$, $\delta\Psi_h$ | (adjoint; fine adjoint minus its coarse projection) | |
| $\gamma$ | $\gamma_{\mathrm{Tik}}$ (page-local) | **collision** with the ratio of specific heats |
| $\boldsymbol\sigma$, $\sigma(\cdot)$ | (viscous stress tensor on the surface; sigmoid) | $\sigma$ also an SA constant |
| $\mathbf R_e$ | (element residual, Eq. 13; MOESS rate tensor, §5.2) | reused symbol in the source |
| $\mathbf x_0$, $\mathbf x_1$, $\mathbf W_i$, $\mathbf b_i$ | $\boldsymbol\zeta$, (hidden layer), $\boldsymbol\theta$ | network inputs and parameters |
| $M$, $\alpha$, $Re$ | $M$, (angle of attack), $Re_c$ | **collision:** $\alpha$ is not the DG blending factor |

# Reference list

75 printed references, numbered style with DOIs for most. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Same-author same-year works take suffixes in printed order
(Fidkowski 2011 a–c and 2012 a–b, Wang 2014, Singh 2017, Ceze 2015, Yano
2012 thesis and paper). Two printed keys name works other than the bundle's
Source pages of the same key: ref. [36] (Li, Hulshoff & Hickel 2021,
CMAME 379:113733) is not li-2021, and ref. [30] (Wang Q. 2013, J. Comput.
Phys. 235) is not wang-2013; they are keyed `li-2021-j` and `wang-2013-g`.
Irregular items: [47] without venue, [75] report without institution, [69]
TensorFlow (software), [40] without volume or pages. No printed duplicates.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
