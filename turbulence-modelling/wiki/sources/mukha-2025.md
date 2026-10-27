---
type: Source
title: "Mukha et al. (2025) — Wall-modeled large-eddy simulation based on spectral-element discretization"
description: "Algebraic wall-stress WMLES in the continuous-Galerkin spectral-element code Nek5000, tested on channel flow at Re_τ≈8000 and a flat-plate boundary layer: Neumann against viscosity-based wall conditions, input time averaging, Vreman, Sigma and filter closures, and the SEM-specific momentum imbalance."
resource: "doi:10.1063/5.0283984"
source_kind: paper
authors: [Mukha T., Parsani M., Schlatter P.]
year: 2025
venue: "Phys. Fluids 37:105158"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Physics_of_Fluids_Mukha_Wall-modeled_large-eddy_simulation_based_on_spectral-element.pdf"
tags: [wmles, wall-model, spectral-element, sgs-model, log-layer-mismatch, channel-flow]
timestamp: 2026-10-27T15:54:00Z
---

# Summary

Mukha et al. (2025) implement algebraic
[wall-modelled LES](/methods/wall-modelled-les.md) in the incompressible
[continuous-Galerkin spectral-element](/methods/spectral-element-method.md)
code [Nek5000](/software/nek5000.md). The discretization uses $N=7$ on
Gauss–Lobatto–Legendre nodes, the $P_N$–$P_{N-2}$ formulation, 3/2
over-integration and BDF3/EXT3 time stepping. The
[equilibrium wall model](/methods/equilibrium-wall-model.md) is Spalding's
[law of the wall](/definitions/law-of-the-wall.md). The modelled stress is
imposed in one of two ways. The first is the "traditional" Neumann condition, enforced weakly, on
the wall-parallel velocity. The second, new for spectral elements, is a
"viscosity-based" condition: no-slip plus a wall value of the subgrid
viscosity that reproduces the modelled stress. Closure is either explicit,
with the [Vreman](/methods/vreman-model.md) or the Sigma model, or implicit
through Nek5000's high-pass relaxation filter ([implicit LES](/definitions/implicit-les.md)).

In [channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau\approx8000$ with the Neumann condition and Vreman, the mean velocity
is within 1% of DNS for $y>0.1\delta$ on meshes of 2, 4 and 8 elements per
$\delta$. The modelled-stress error stays below 1%. Second-order statistics
need about four elements per $\delta$
([grid requirements](/results/les-grid-point-requirements.md)). No
[log-layer mismatch](/definitions/log-layer-mismatch.md) appears even where
the subgrid shear stress exceeds the resolved one at the first off-wall
node, which the authors read as contradicting the Brasseur & Wei criterion.
Time-averaging the wall-model input reduces the stress error
[a priori but not a posteriori](/definitions/a-priori-and-a-posteriori-testing.md).
For algebraic models the matching height matters more than the averaging.

Three difficulties are specific to spectral elements. Velocity derivatives
jump across element faces and produce spikes of $\nu_t$. The weak Neumann
condition lets the stress computed from the wall gradient differ from the
modelled one by 8 to 85%, depending on the
[subgrid model](/definitions/large-eddy-simulation.md) and its
[dissipation](/properties/numerical-dissipation.md). Global momentum is
not conserved, which ruins the viscosity-based condition: its stress errors
from the driving pressure gradient are 16 to 38%. On a zero-pressure-gradient
[flat-plate boundary layer](/benchmarks/turbulent-boundary-layer.md) fed with
[precursor inflow planes](/methods/inflow-turbulence-generation.md), $C_f$ is
within 2% of wall-resolved LES on the finest mesh. The Reynolds stresses are
on par with published WMLES, including
[building-block-flow](/methods/building-block-flow-wall-model.md) results. The
closure is a [Boussinesq](/definitions/boussinesq-hypothesis.md) eddy
viscosity; the introduction cites WMLES with
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) and
the [WALE model](/methods/wale-model.md), and DG wall models
([DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)).

# Version read

arXiv preprint 2404.05378v1 (8 April 2024, header "Dated: April 9, 2024"),
not the version of record; 25 pages, all read (pages 4 and 15 checked
visually). **Author list differs:** the preprint has two authors (Mukha,
Schlatter); the published article (Crossref) has three (Mukha, Parsani,
Schlatter). The frontmatter follows Crossref. Numbers, equations and
references here are those of the preprint; the published version can differ.
The code is released as `nekwmles` (GitHub, printed in the preprint).

# Key claims

1. WMLES in a CG spectral-element solver with Spalding's law and the Vreman model reaches "state-of-the-art accuracy" for channel flow and the flat-plate boundary layer (Abstract, §V). **Shown**
2. Channel at $Re_\tau\approx8000$, Neumann condition, Vreman: the mean-velocity error does not exceed 1% for $y>0.1\delta$ on meshes M1–M3; M2 has the smallest error, with no gain from M2 to M3 (§III.B.1, Fig. 1). **Shown**
3. Second-order statistics: near-wall over-prediction of $R_{11}$ and under-prediction of $R_{22}$, $R_{33}$; a strong accuracy gain from M2 to M3; WMLES needs "at least 4 elements across the boundary layer in all three spatial directions" for second-order statistics (§III.B.1, Fig. 2, §IV.A). **Shown**
4. Relative errors of the modelled wall stress $\tau_w^{\mathrm{wm}}$: 0.71%, 0.76%, −0.54% (M1–M3); of the stress from the mean wall gradient $\tau_w^{\mathrm{wall}}$: 12.58%, 10.86%, 8.07%; of the stress from the driving pressure gradient $\tau_w^{\nabla p}$: 1.95%, 0.96%, −3.84% (Table II). **Shown**
5. Because the Neumann condition is enforced weakly, $\tau_w^{\mathrm{wall}}$ equals $\tau_w^{\mathrm{wm}}$ only asymptotically under refinement; $\tau_w^{\mathrm{wall}}$ "should essentially be disregarded", and $\tau_w^{\mathrm{wm}}$, which sets the slope of the linear Reynolds shear stress profile, is the dynamically relevant value; "This issue is unique to the finite element method" (§II.C.2–3, Eqs. 7–12, §III.B.2). **Derived** and **Shown**
6. The difference between $\tau_w^{\nabla p}$ and $\tau_w^{\mathrm{wm}}$ measures the global momentum imbalance of the discretization (plus time-averaging error) and is of the order of the wall-model error (§III.B.2). **Shown**
7. CG spectral elements conserve mass globally for a locally divergence-free velocity, but not momentum, since velocity derivatives jump across element faces; the jumps fade with refinement and are negligible at wall-resolved resolution but significant for WMLES (§II.B). **Stated**, then **Shown** in §III
8. An "LES buffer layer" (Brasseur & Wei) appears in inner-scaled profiles and shrinks with refinement, but no log-layer mismatch occurs on any mesh, although the resolved shear stress is below the subgrid one near the wall on M1: "the dominance of the resolved shear stress over the modeled one near the wall is not a necessary condition for capturing the log-layer" (§III.B.2, Fig. 3, §V). **Shown**
9. The indicator $\Phi=\kappa y^+\,\mathrm d u^+/\mathrm dy^+$ exposes derivative discontinuities at element faces; the jumps converge only for $y>0.25\delta$ on M2 and M3, at the edge of the log layer (§III.B.2, Fig. 3). **Shown**
10. Spalding's law with $\kappa=0.387$, $B=4.2$ is not exact at $y=h_{\mathrm{wm}}$: the stress error is −0.04% at $h_{\mathrm{wm}}=0.2\delta$; the stress error is about twice the input-velocity error (§III.B.3, App. A, Fig. 19). **Shown**
11. A priori, feeding the mean $\langle u\rangle$ at $h_{\mathrm{wm}}$ (infinite averaging) gives stress errors 0.06%, 0.2%, −1.07% (M1–M3); fluctuations in the input shift the error toward over-prediction (§II.C.1, Table III). **Shown**
12. A priori averaging on M2: most of the error reduction is reached at $\Delta t_{\mathrm{avg}}=50\Delta t=0.01\,\delta/u_\tau$, where the mean of the stress magnitude and the magnitude of the mean stress start to overlap (range tested 0 to $5\times10^3\Delta t=\delta/u_\tau$) (§III.B.3, Fig. 4). **Shown**
13. $50\Delta t$ lies in the inertial subrange of the temporal spectrum of $u'$ at $h_{\mathrm{wm}}$, consistent with Calafell et al.; the diffusion time $h_{\mathrm{wm}}/(\kappa u_\tau)\approx0.51\,\delta/u_\tau$ (Hosseinzade & Bergstrom) and $\delta/u_\tau$ belong to large-scale motions; the temporal stability of the direction of $\tau_w^{\mathrm{wm}}$ is proposed as a criterion for choosing $\Delta t_{\mathrm{avg}}$ (§III.B.3, Fig. 4). **Shown** / **Stated** (proposal)
14. A posteriori runs with $\Delta t_{\mathrm{avg}}=5,10,50,500\,\Delta t$ show "no systematic accuracy gain", because the sampled velocity itself changes with $\Delta t_{\mathrm{avg}}$; for algebraic wall models $h_{\mathrm{wm}}$ matters more than $\Delta t_{\mathrm{avg}}$, "at odds with" Yang et al. (2017) (§III.B.3, Fig. 5). **Shown**
15. The divergence without time averaging reported for Nek5000 WMLES by Gillyns et al. (2022) was not encountered (§II.C.1). **Shown** (by absence)
16. On M3, Vreman, Sigma and high-pass filtering all give an accurate $\tau_w^{\mathrm{wm}}$ and no log-layer mismatch; lower near-wall dissipation gives a more oscillatory solution but a thinner LES buffer layer (§III.C, Fig. 6). **Shown**
17. Derivative jumps propagate into spikes of $\nu_t$, "just numerical artifacts"; continuity of velocity derivatives is "a missing component in the current WMLES methodology" (§III.C, Fig. 7). **Shown**
18. Sigma visibly lowers $\nu_t$ toward the wall; Vreman shows no visible decrease although asymptotically $\nu_t\sim y$: "not only the asymptotic behavior … but also how fast the model transitions towards the asymptote" matters (§III.C). **Shown**
19. High-pass filtering (two modes, strength 100) increases near-wall oscillations and the core variance, over-predicting $R_{11}$; filtering alone "does not introduce enough damping to avoid the contamination of the solution with numerical artifacts" (§III.C, Fig. 8). **Shown**
20. The error of $\tau_w^{\mathrm{wall}}$ on M3 depends strongly on the closure: 8.07% (Vreman), −25.72% (Sigma), −84.85% (filter); more near-wall dissipation brings $\tau_w^{\mathrm{wm}}$ and $\tau_w^{\mathrm{wall}}$ closer (§III.C). **Shown**
21. Near-wall $\nu_t$ has no significant effect on the log-layer mismatch, which "appears to contradict the theory of Brasseur and Wei", with the caveat that only one of their three criteria was examined (§III.C). **Shown**
22. Viscosity-based condition: $\tau_w^{\mathrm{wm}}=\tau_w^{\mathrm{wall}}$ by construction (errors −0.91%, −0.85%, −2.26%), but the $\tau_w^{\nabla p}$ errors are 38.05%, 25.73%, 15.65% (M1–M3); the mean velocity is strongly under-predicted for $y^+\lessapprox2500$ and over-predicted in the core, all Reynolds stresses strongly over-predicted; with fixed-$Re_\tau$ forcing the stress is "strongly under-predicted". The cause is the violation of momentum conservation; the attempt is "largely unsuccessful" (§III.D, Table IV, Figs. 9–10, §V). **Shown**
23. Since $\nu_t$ is a scalar, the viscosity-based condition cannot set the direction of $\tau_w$; with spanwise strain present, the streamwise modelled stress is below the stress magnitude even for an exact magnitude (§II.C.4). **Derived**
24. The viscosity-based condition allows blending wall-resolved and wall-modelled LES by setting the wall $\nu_t=0$ where the grid resolves the inner layer (De Vanna et al.); it has long been used in OpenFOAM; Bae & Lozano-Durán found it somewhat more accurate than Neumann in a finite-difference code (§II.C.4). **Stated**
25. Flat-plate boundary layer: the shape factor agrees with references after the inflow adapts; the outer-scaled mean velocity is slightly over-predicted, improving with spanwise refinement (M3 "virtually indistinguishable" at $Re_\theta=4000$); Reynolds stresses are more accurate than in the channel; $C_f$ from $\tau_w^{\mathrm{wm}}$ is within 2% of wall-resolved LES on the finest mesh (§IV.B, Figs. 13–16). **Shown**
26. The gain from spanwise refinement, with outer scales already resolved, suggests a dependence on $\Delta z^+$, which "would violate th[e] premise of WMLES being independent of inner-scale resolution" (§IV.B). **Stated** (speculation)
27. Spalding's law with $\kappa=0.41$ and $B=5.5$ (App. A; "a more classical set of values" in §IV.A, which prints $B=5.2$) gives about ±1% stress error with boundary-layer DNS or wall-resolved LES input, an order of magnitude above the tuned channel case; the law reaches its logarithmic limit near $y^+=150$, close to the wake at low $Re$ (§IV.A, App. A, Figs. 20–21). **Shown**
28. Published comparisons: OpenFOAM WMLES (Mukha et al. 2021, about 2 elements per $\delta_{99}$) is less accurate; Lozano-Durán & Bae (2023) report 10–30% velocity and 5–15% stress deviations on coarser meshes; a dynamic-slip wall model is "well within" 4% in $C_f$; the present results are "on par with the state of the art, possibly outperforming it" for $R_{11}$ (§IV.B). **Stated**
29. Sampling inside the wall-adjacent element by spectral interpolation to arbitrary $h_{\mathrm{wm}}$ caused no accuracy problem (§II.C.1, §V). **Shown**
30. A structured mesh cannot keep the spanwise element size adapted to $\delta_{99}$, which grows about eightfold over the domain; 4 elements per $\delta_{99}$ at the inlet is already wall-resolved-like (about $10\delta_\nu$), so WMLES needs coarsening in $x$ and $y$ (§IV.A, Fig. 12). **Shown** / **Stated**

The momentum equation (Eqs. 1–4), translated, with the overbar of the implicit grid filter omitted ($u_i$, $p$, $S_{ij}$ stand for $\bar u_i$, $\bar p$, $\bar S_{ij}$; the source prints none):
$$\frac{\partial u_i}{\partial t}+u_j\frac{\partial u_i}{\partial x_j}=-\frac1\rho\frac{\partial p}{\partial x_i}+\frac{\partial}{\partial x_j}\Big[2(\nu+\nu_t)S_{ij}\Big]+f_{\mathrm{hp},i},\qquad f_{\mathrm{hp},i}=\chi_f\,(u_i-u^{\mathrm{lp}}_i),$$
with $u^{\mathrm{lp}}_i$ the velocity passed through the modal low-pass filter of Nek5000 and $\chi_f$ its strength (registry §11; sign as printed), the symbols of the [spectral-element](/methods/spectral-element-method.md) page. The viscosity-based condition (Eqs. 13–14), with $\tau_w$ kinematic:
$$\nu_t\big|_{\mathrm{wall}}=\frac{\lvert\tau_w^{\mathrm{wm}}\rvert}{2\sqrt{S_{xy}^2+S_{zy}^2}}-\nu .$$
Input averaging (Eqs. 5–6): $u^{\mathrm{wm}}_n\leftarrow\epsilon_{\mathrm{avg}}u^{\mathrm{wm}}_n+(1-\epsilon_{\mathrm{avg}})u^{\mathrm{wm}}_{n-1}$, $\epsilon_{\mathrm{avg}}=\Delta t/(\Delta t+\Delta t_{\mathrm{avg}})$. Model constants: Vreman constant $2.5C_s^2$ with $C_s=0.16$; Sigma constant 1.35; the subgrid length scale is the largest GLL spacing of the element (§II.D).

# Printed slips

- Spalding constant for the boundary layer: §IV.A "here with κ = 0.41 and B = 5.2"; Appendix A "Here, we use κ = 0.41 and B = 5.5".
- Spalding error at $h=0.2\delta$: "only −0.04%" (§III.B.3) and "about 0.05%" (Appendix A).
- Fig. 10 legend labels the meshes "M0, M1, M2", while the text and Table IV use M1–M3.
- Node counts: both Tables I and V say "total number of nodes in the mesh", but Table I equals $(N+1)^3=512$ nodes per element times the element count (M1: $16\cdot4\cdot12\cdot512\approx0.39\times10^6$), while Table V equals $N^3=343$ per element (M1: $519\cdot15\cdot28\cdot343\approx75\times10^6$) *(compiler check, not in the sources)*.
- Eq. 5 uses the same symbol $u^{wm}_n$ on both sides for the averaged and the instantaneous value.
- Fig. 20 caption: "with DNS mean velocity data as input", while the text uses wall-resolved LES data as the reference.
- Typos: "a an excellent" (Abstract), "sin the next subsection" (§III.B.1), "Schaltter & Örlü", "Saplding's law", "Eitel-Amor el al." (figure legends), "strong affect" (§III.D).
- Ref. [26] printed "Physics of Fluids 33, 35108"; several references print no volume.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $p$ (implicitly filtered) | $\bar u_i$, $\bar p$ | no overbar printed |
| $S_{ij}=\partial_ju_i+\partial_iu_j$ | $2S_{ij}$ | **collision:** no factor $\tfrac12$ in the source |
| $\tau_{ij}=(\nu+\nu_{sgs})S_{ij}$ | $2(\nu+\nu_t)S_{ij}=\sigma_{ij}/\rho-\tau^d_{ij}$ | **collision:** viscous plus subgrid, opposite sign to the registry's $\tau_{ij}$ |
| $\nu_{sgs}$ | $\nu_t$ | not forced to zero at the wall |
| $\tilde u$ | $u^{\mathrm{lp}}$ (modally low-pass-filtered velocity, page-local) | **collision:** not a Favre filter |
| $f_{hp}$, $\chi$ | $f_{\mathrm{hp},i}$ (relaxation term, page-local), $\chi_f$ (strength, registry §11) | **collision:** $\chi$ is the SA ratio |
| $N$ | $N$ | $N=7$ |
| $h$ | $h_{\mathrm{wm}}$ | **collision:** not an element size; $0.2\delta$ or $0.2\delta_{99}(x)$ |
| $\tau_w^{wm}$, $\tau_w^{wall}$, $\tau_w^{\nabla p}$, $\tau_w^{apri}$ | $\tau_w$ with page-local superscripts | modelled; from the mean wall gradient; from the driving pressure gradient; a priori |
| $\epsilon$ (averaging weight) | $\epsilon_{\mathrm{avg}}$ (page-local) | **collision** with $\varepsilon$ |
| $\epsilon[q]$ (relative error) | $e_q$ | §11 |
| $\Delta t_{avrg}$, $t_{diff}$ | $\Delta t_{\mathrm{avg}}$, $h_{\mathrm{wm}}/(\kappa u_\tau)$ | |
| $\kappa$, $B$ | $\kappa$, $B$ | 0.387/4.2 (channel), 0.41/5.2 or 5.5 (boundary layer) |
| $\langle u'u'\rangle$, $\langle u'v'\rangle$ | $R_{11}$, $R_{12}$ | positive convention |
| $\Phi$ | $\kappa y^+\,\mathrm du^+/\mathrm dy^+$ (log-law indicator, page-local) | **collision** with the Ducros factor $\Phi_i$ |
| $\delta_{sgs}$ | (thickness of the LES buffer layer, page-local) | Brasseur & Wei |
| $c_f$ | $C_f$ | |
| $\delta$, $\delta_{99}$, $\delta^*$, $\theta$, $H$ | $\delta$, $\delta_{99}$, $\delta^*$, $\theta$, (shape factor) | |
| $U_b$, $U_0$ | (bulk velocity), $U_\infty$ (local maximum of the mean velocity) | |
| $C_s$, $C_\sigma$ | $C_s$, $C_\sigma$ (registry §11) | Vreman $2.5C_s^2$, $C_s=0.16$; $C_\sigma=1.35$ |
| $N_x$, $N_y$, $N_z$, $N_{gll}$ | element counts, total GLL nodes | **collision:** $N_x$ counts elements here, not grid points |

# Reference list

52 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Reference [10]
(Huang et al. 2022, Phys. Fluids 34:105129) is a different work from the
ingested Huang et al. (2022) and takes the key `huang-2022-c`; [9], [40] and [51] are the
ingested Gillyns et al. (2022), Goc et al. (2021) and Lozano-Durán & Bae
(2023). [52] prints both an arXiv identifier and the published JFM form and is
one entry. Several items print no volume ([13], [14], [38]–[42]). No printed
duplicates.

# Pages created or updated

Chunk 6 (2026-10-26), cited further in chunks 7, 10. This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Building-block-flow wall model](/methods/building-block-flow-wall-model.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Sigma model](/methods/sigma-model.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Vreman model](/methods/vreman-model.md)
- [WALE model](/methods/wale-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nek5000 and NekRS](/software/nek5000.md)
- [OpenFOAM](/software/openfoam.md)
