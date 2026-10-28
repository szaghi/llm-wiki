---
type: Source
title: "Idelsohn et al. (2024) — The P-DNS Method for Turbulent Fluid Flows: An Overview"
description: "Overview of pseudo-direct numerical simulation: a two-scale method whose sub-coarse-mesh stress comes from an off-line database of DNS on periodic representative volume elements, convected with the coarse flow and relaxed by a memory model, tested on canonical flows against coarse-mesh LES and extended to particle-laden flows."
resource: "doi:10.1007/s11831-023-10004-3"
source_kind: paper
authors: [Idelsohn S.R., Gimenez J.M., Larreteguy A.E., Nigro N.M., Sívori F.M., Oñate E.]
year: 2024
venue: "Arch. Comput. Methods Eng. 31:973–1021"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Archives_of_Computational_Methods_in_Engineering_Idelsohn_The_P-DNS_Method_for_Turbulent_Fluid_Flows_An_Overview.pdf"
tags: [les, sgs-model, data-driven, dns, variational-multiscale, review]
timestamp: 2026-10-27T21:09:00Z
---

# Summary

Idelsohn et al. (2024) review their [pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md)
(P-DNS), introduced in 2020. P-DNS splits the velocity into a piecewise
linear coarse part and a fine remainder, computes the fine scale off-line
by [DNS](/definitions/direct-numerical-simulation.md) on small periodic
domains (representative volume elements, RVEs), stores the results in a
problem-independent dimensionless database, and convects the fine
instabilities with the coarse velocity through virtual particles (PFEM-2
or a particle finite-volume method). The authors frame it as a
[variational multiscale](/methods/variational-multiscale-method.md) variant
whose fine scale is solved numerically, as an off-line form of FE², and as
a reduced-order model. Under stated assumptions the only fine-to-coarse
contribution is an "inertial stress tensor", the product of fine
velocities averaged over the RVE: the analogue of the subgrid stress of
[LES](/definitions/large-eddy-simulation.md), here without a universality
assumption. Internal RVEs under jump-periodic shear are indexed by two
shear Reynolds numbers obtained by rotating the coarse strain; wall RVEs
are Couette-like; a time-developing boundary-layer RVE with a velocity
enrichment targets developing boundary layers on very coarse meshes, a
data-based counterpart of [wall functions](/methods/rans-wall-function.md)
(a term the paper does not use).
A memory model relaxes the stress toward the database equilibrium.

The examples (from earlier papers) are 1-D Poiseuille and Couette flows on
3–4 cells, a spatially developing mixing layer, decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), the
[backward-facing step](/benchmarks/backward-facing-step.md) at
$Re_h=5000$, the [square cylinder](/benchmarks/square-cylinder-flow.md) at
$Re=22\,000$ and flat-plate [boundary layers](/benchmarks/turbulent-boundary-layer.md);
the LES comparator is the dynamic [one-equation subgrid kinetic-energy model](/methods/subgrid-kinetic-energy-equation-model.md)
of Kim & Menon on the same coarse meshes, and P-DNS is reported closer to
DNS and experiment. The second part (about 40% of the paper) extends P-DNS
to particle-laden flows (turbulence modulation from particle-laden RVEs, a
[channel](/benchmarks/turbulent-channel-flow.md) against static
[Smagorinsky](/methods/smagorinsky-model.md) LES and
[$k$-$\varepsilon$](/methods/k-epsilon-model.md) URANS, and a continuous
particle method implemented in [OpenFOAM](/software/openfoam.md)).

# Version read

Version of record (Springer, review article; received 28 June 2023,
accepted 11 September 2023, online 24 October 2023), 49 pages
(pp. 973–1021), all read (pp. 978–980, 984, 996–997, 1002–1003 also
visually for the equations). Page 1 matches the metadata; the filename
year 2023 is the online year. No identity issue. The results are those of
the authors' earlier papers, summarized here.

# Key claims

Page-local symbols: $u^>_i$, $p^>$ the coarse (piecewise linear) and
$u^<_i$, $p^<$ the fine velocity and pressure (the source's $u^c_i$,
$u^f_i$; a discretization split, not a filter); $\mathcal T_{ij}=\rho u^<_iu^<_j$
the inertial stress tensor and $\hat{\mathcal T}_{ij}$ its average
over a nodal domain or an RVE; $H$ the RVE side; $\mathrm{Id}_{ij}=G_{ij}H^2\rho/\mu$
the instability index tensor ($G_{ij}$ the coarse velocity gradient) and
$\mathrm{Id}_1$, $\mathrm{Id}_2$ its two reduced parameters; $t_r$,
$C_\tau$, $W_\tau$, $b$, $C_1$, $C_2$, $Re^*$ the memory
model; $Is$ the shape index of the boundary-layer RVE; $St_p$ the Stokes
number.

1. P-DNS rests on four ideas: numerical solution of both scales; off-line DNS of the fine scale on RVEs; storage in a problem-independent dimensionless database used as a surrogate; convection of the fine instabilities by the coarse velocity (Abstract, §1.4, Fig. 1). **Stated**
2. P-DNS is a variation of VMS (fine scale solved numerically instead of approximated through Green functions), an evolution of FE² with the expensive part off-line, and a reduced-order model (§1.4). **Stated**
3. The premise is that the very-fine-discretization result is "the correct one" without turbulence models or stabilization; as the coarse mesh is refined P-DNS tends to DNS (§1.4). **Stated**
4. P-DNS "does not assume universality in the sub-grid (more specifically sub-coarse-mesh) model and, thus is free from the LES limitation that would have imposed a usually excessive requirement on the fine mesh size" (§1.4). **Stated**
5. With fine fields of zero mean and zero mean gradient over each nodal domain $\Omega^l$ (Eq. 15), both parts divergence-free (Eq. 18), a linear coarse velocity in $\Omega^l$, and the term $\int_{\Omega^l}\rho\,D^{u^>}u^<_i/Dt\,d\Omega$ neglected ("validity has yet to be shown by the numerical results"), the only fine-to-coarse contribution is $\mathcal T_{ij}$ (Eqs. 19–23, §2.4). **Derived**
6. Replacing $\mathcal T_{ij}$ by its average over $\Omega^l$ is exact for linear finite-element or finite-volume weighting functions; the approximation enters when the average is taken over the RVE instead (Eqs. 24–27, §2.5–2.6). **Derived**
7. The RVE size should lie between the local coarse mesh size and twice that value; periodic RVEs exclude waves of length $2H$, so RVEs of neighbouring cells may overlap (§2.6, §2.7.3). **Stated**
8. With rotations and coarse incompressibility the nine components of $\mathrm{Id}_{ij}$, computed from the symmetric part of $G_{ij}$, reduce to two parameters $\mathrm{Id}_1$, $\mathrm{Id}_2$ (Eqs. 28–29, Appendix 1). **Derived**
9. RVE runs need no convection stabilization, only incompressibility stabilization, because they are DNS (§2.7.3). **Stated**
10. Internal RVEs under sudden shear jumps ($\mathrm{Id}$ from 200 to 600) relax as a dynamical system with $t_r=C_\tau/((G^B+G^A)/2)$, $C_\tau\simeq1$ (Eq. 37, Fig. 5, 100 realizations for $\mathrm{Id}=400\to200$). **Shown**
11. The revised memory model (Eqs. 38–40) uses $W_\tau=C_1b^3+C_2(1-b^3)$ with $C_1=6.8$, $C_2=4.0$ calibrated on decaying isotropic turbulence, and freezes the initial shear for a perturbation Reynolds number $Re\le Re^*=15$ (§2.9). **Stated** (calibration from an earlier paper)
12. 1-D Poiseuille ($Re=1.65\times10^5$, 4 cells) and Couette ($Re=4\times10^4$, 3 cells): the P-DNS mean velocity "closely matches the DNS solution" (Table 1, Fig. 6). **Shown**
13. 2-D Poiseuille: $\langle u^>_x\rangle=0.378$ m/s, $Re=1.5\times10^5$, friction factor 0.014 against 0.016 from the Moody diagram (§2.10.1, Fig. 7). **Shown**
14. Spatially developing mixing layer (meshes A $128\times30$, B $256\times61$, C $512\times121$): the transported effective viscosity $\mathcal T_{xy}/G_{xy}$ falls as the coarse mesh is refined, "equivalent to moving the limit between what is considered large and small scales"; B and C agree with the Oster & Wygnanski experiments, A gives less than half the turbulence intensity, and standard LES on grids like A and B "is not able to capture the instabilities" (§2.10.2, Figs. 9–10). **Shown** (LES statement **Stated**, no figure)
15. Decaying isotropic turbulence ($Re_{u'}\approx60$ and $\approx500$): P-DNS gives a reasonable kinetic-energy decay down to $4^3$ coarse cells, whereas LES is accurate at $32^3$ and departs as the mesh coarsens (§2.10.3, Fig. 12). **Shown**
16. Taylor–Green vortex: at $64^3$ all solutions are close to the $512^3$ DNS; at $32^3$ LES underestimates the energy decay, while P-DNS overestimates it between $\hat t=5$ and 8 and agrees in most of the final phase (§2.10.4, Fig. 13). **Shown**
17. Backward-facing step, $Re_h=5000$, 142K cells: $x_R=6.05h_s$ (P-DNS), $5.1h_s$ (LES), $6.1h_s$ (DNS), experiment $(6\pm0.15)h_s$ (§2.10.5, Fig. 16). **Shown**
18. Square cylinder, $Re=22\,000$, 2M cells against a 300M-cell DNS (P-DNS / LES / DNS): $St=0.127/0.115/0.132$; $\langle C_D\rangle=2.551/2.701/2.18$; $C_{D,\mathrm{rms}}=0.233/0.293/0.205$; $\langle C_L\rangle=0.044/0.049/0.002$; $C_{L,\mathrm{rms}}=1.574/1.771/1.71$; $L_r=1.108/1.404/1.04$ (Table 2). **Shown**
19. The time-developing boundary-layer RVE is "a unique problem that has to be solved only once" in dimensionless form; its database inputs are $\mathrm{Id}_1$ and a shape index $Is$, which falls from 1.0 to about 0.82 when the boundary layer reaches $2H$ (§2.11, Eqs. 59–61). **Stated** / **Derived**
20. The boundary-layer RVE leaves out pressure-gradient effects (separation, recirculation) (§2.11.1). **Stated**
21. Flat plate: the laminar boundary layer, entirely inside the first row of cells, agrees "excellently" with Blasius in $\delta$ and $C_f$; the turbulent one, reaching the second row, agrees "remarkably" with Schlichting's $C_f$; transition is a threshold switch between the laminar and turbulent databases (§2.12, Figs. 23, 25). **Shown**
22. Particle-laden RVEs (126 runs): large particles enhance the carrier turbulent kinetic energy above a concentration threshold that grows with $\mathrm{Id}$; small particles attenuate it in almost all configurations; no fixed threshold at $St_p=10$ appears, but a dependence on inter-particle distance does (§3.2.1, Fig. 27). **Shown**
23. Particle-laden channel at $Re=57\,000$: P-DNS on $36\times12\times12$ cells reproduces the DNS change of mean velocity and kinetic energy between laden and unladen flow; static Smagorinsky LES fails from the unresolved boundary layer; URANS $k$-$\varepsilon$ shows a negligible difference, "indicating that ensemble averaged solutions cannot predict turbulence modulation" (§3.2.2, Fig. 28). **Shown**
24. For exhaled saliva droplets P-DNS and LES give similar penetration, so turbulence modulation can be neglected at low mass loading (§3.2.3, Fig. 29). **Shown**
25. The continuous particle method agrees with a DPMFoam reference for settling clouds and a chimney plume, where a passive scalar fails (§3.4, Figs. 30–34). **Shown**
26. The overhead of the continuous particle method is the database evaluation, independent of the number of particles; a timing comparison with DPM "requires further study" (§4). **Stated**
27. "For homogeneous fluids problems presented in the literature, using coarse and medium mesh sizes, P-DNS provides better match to the experimental data than LES"; "LES methods do not comply with the self-similarity property or the averaged symmetry over the time of the flow"; P-DNS "may be cheaper than LES because it avoids the LES requirement of using fine enough meshes to capture every large eddy" (§4). **Stated**

The coarse momentum equation in registry notation (Eq. 21, finite-element
form; Eq. 22 is the finite-volume form):
$\int_{\Omega^l}N^l\rho\,[D^{u^>}u^>_i/Dt-B_i]\,d\Omega+\int_{\Omega^l}\partial_jN^l\,(\sigma^>_{ij}-\hat{\mathcal T}_{ij}-p^>\delta_{ij})\,d\Omega=0$,
with $\hat{\mathcal T}_{ij}\approx\frac{1}{\Omega^R}\int_{\Omega^R}\rho u^<_iu^<_j\,d\Omega$
(Eq. 27), stored in the database in the dimensionless form
$\mathcal T_{ij}H^2\rho/\mu^2$ against $(\mathrm{Id}_1,\mathrm{Id}_2)$. It is a
positive-trace product of fine velocities without trace removal; the
Reynolds stress is reconstructed as the covariance of the coarse field
plus $\langle\mathcal T_{xy}\rangle/\rho$ (§2.10.2). The memory model
(Eqs. 35–36) is $\mathcal T^{n+1}_{ij}=m\,\mathcal T^n_{ij}+(1-m)\,\mathcal T^{\mathrm{eq},n+1}_{ij}$,
$m=e^{-\Delta t/t_r}$, with $\mathcal T^{\mathrm{eq}}_{ij}$ the
database equilibrium for the present coarse state.

# Printed slips

- **§2.10.6 against Table 2:** "Using P-DNS with the automatic memory model results in lR = 1.04 which is, again, closer to the DNS reference", while Table 2 prints $L_r=1.04$ for the DNS and 1.108 for P-DNS.
- **§2.10.6:** "the profile of the components of the time-averaged Reynolds stress tensor, see Fig. 18b, c", while the caption places velocities in (b, c) and Reynolds stresses in (d, e).
- **§3.2.2:** "such coarse grid size, 0.04 cm, enables homogenizing the particles as their diameter (200 μm) is smaller than the fine grid size, 0.04/80 cm ≈ 500 μm". *(Compiler check, not in the sources: 0.04 cm = 400 μm and 0.04 cm/80 = 5 μm.)*
- **Eq. (69):** the particle equation is printed with $\frac{dv_i}{dx}$.
- **§3.2.1:** $\tau_p=\rho d_p^2/(18\nu)$. *(Compiler check, not in the sources: with $\nu$ kinematic this has the units of kg s m$^{-3}$, not a time; Eq. (93) prints $\tau^k=\rho^k(d^k)^2/(18\mu)$, which is a time.)*
- **§2.10.3, step 2(a):** "$k^c=u^c_iu^c_i$", without the factor ½. *(Compiler check, not in the sources: Eq. (42) uses $u^c_iu^c_i/2$, and step 2(c), $T^\rho_{ij}=\frac23\rho k^f\delta_{ij}$, with $K^f=T^\rho_{ii}/(2\rho)$, gives $K^f=k^f$ only for $k$ defined with the ½.)*
- **Remark 3 (§3.3):** "This dimensionless data must be rescaled as indicated in Table 1", while Table 1 of this paper is the 1-D test set-up.
- **§3.4.2 against the Fig. 34 caption:** the text calls the $\Pi^p_x$ planes vertical and the $\Pi^p_y$ planes horizontal; the caption reads "a horizontal planes Πx1 and Πx3, b horizontal planes Πx2 and Πx4, c vertical planes".
- **§2.11:** Eq. (58) defines $\hat t$, the database inputs and §2.11.4 write $\tilde t$; the isotropic-turbulence normalization is printed "K∕∕K0".
- **Typos:** "P-DNS mexthod", "the tree meshes analyzed", "freezed".
- **References:** [50] "Feyel J-LCF (2000)" and [52] "Fritzen MHF (2016)" print merged author names; [47] "Rasthofer U, Gravemeier C"; [40] publisher "American Cancer Society, Atlanta"; [105] "J Comput Part Mech (under review, X)".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u^c_i$, $p^c$; $u^f_i$, $p^f$ | $u^>_i$, $p^>$; $u^<_i$, $p^<$ | coarse (piecewise linear) and fine parts; a discretization split, no filter kernel |
| $T_{ij}$, $T^c_{ij}$, $T^f_{ij}$ | $\sigma_{ij}$, $\sigma^>_{ij}$, $\sigma^<_{ij}$ | viscous stress $\mu(\partial_ju_i+\partial_iu_j)$; **collision:** $T$ is not the temperature |
| $T^\rho_{ij}=\rho u^f_iu^f_j$, $\widehat T^\rho_{ij}$ | $\mathcal T_{ij}$, $\hat{\mathcal T}_{ij}$ (page-local) | positive trace, density included; **collision:** the hat is a spatial average, not the test filter |
| $\widetilde T^\rho_{ij}=T^\rho_{ij}H^2\rho/\mu^2$ | (dimensionless $\mathcal T_{ij}$) | **collision:** tilde is not a Favre filter |
| $\overline{\widetilde T}{}^\rho_{ij}$ | $\mathcal T^{\mathrm{eq}}_{ij}$ | database equilibrium stress; **collision:** overbar is not the LES filter |
| $G_{ij}$, $G^s_{ij}$ | $\partial_ju^>_i$, $S^>_{ij}$ | coarse velocity gradient and strain rate |
| $S_{ij}$ (Appendix 1) | (rotation matrix) | **collision** with the strain-rate tensor |
| $\mathrm{Id}_{ij}$, $\mathrm{Id}_1$, $\mathrm{Id}_2$, $\mathrm{Id}$, $H$ | same (page-local) | shear Reynolds numbers of the RVE |
| $\tau$, $C_\tau$, $W_\tau$, $\beta$, $C_1$, $C_2$, $Re^*$ | $t_r$, $C_\tau$, $W_\tau$, $b$, $C_1$, $C_2$, $Re^*$ (page-local) | memory model; **collision:** $\beta$ is not the field-inversion multiplier |
| $\nu_{eff}=T^\rho_{xy}/G_{xy}$ | $\mathcal T_{xy}/\partial_yu^>_x$ (page-local) | **collision** with the registry's projected $\nu_{\mathrm{eff}}$; carries $\rho$ |
| $k$ (LES comparator) | $k_{\mathrm{sgs}}$ | Kim & Menon dynamic one-equation model |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time average |
| $l_R$ (square cylinder), $l_r/h$ (step) | $L_r$, $x_R/h_s$ | $h_s$ the step height (page-local; $h$ is the cell size) |
| $St$ (Table 2), $St=\tau_p/\tau_e$ (§3) | $St$ (Strouhal), $St_p$ (Stokes, page-local) | **collision** |
| $Re_{u'}$, $Re_h$, $Re_\delta$ | same | rms-velocity, step-height and boundary-layer Reynolds numbers |
| $c^k$, $c$, $d^k$, $\eta^k$, $\epsilon^k$ | (concentration, fluid fraction, diameter, Rosin–Rammler spread, volume fraction; page-local) | **collision:** $\eta^k$ is not the Kolmogorov length |

# Reference list

105 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug; [50] and
[52] are entered with their author names as printed, [105] is an
under-review item. The cited Heinz review [25] and Wang et al. [74] (cited
as the source of the Taylor–Green DNS data) are the ingested
[heinz-2020](/sources/heinz-2020.md) and [wang-2013](/sources/wang-2013.md).
Same-author same-year works are keyed in printed order (Gimenez 2021,
Idelsohn 2022). No item is unparseable.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Flow past a square cylinder](/benchmarks/square-cylinder-flow.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Pseudo-direct numerical simulation (P-DNS)](/methods/pseudo-direct-numerical-simulation.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [One-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
- [Variational multiscale method](/methods/variational-multiscale-method.md)
- [OpenFOAM](/software/openfoam.md)
