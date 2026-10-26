---
type: Source
title: "Agrawal et al. (2022) — Non-Boussinesq subgrid-scale model with dynamic tensorial coefficients"
description: "Introduces the dynamic tensor-coefficient Smagorinsky model, a traceless non-Boussinesq SGS closure with four coefficients fitted to the Germano identity, and tests it a priori on channel DNS and a posteriori on isotropic turbulence, wall-modelled channel flow and the Gaussian speed bump."
resource: "doi:10.1103/physrevfluids.7.074602"
source_kind: paper
authors: [Agrawal R., Whitmore M.P., Griffin K.P., Bose S.T., Moin P.]
year: 2022
venue: "Phys. Rev. Fluids 7:074602"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physical_Review_Fluids_Agrawal_Non-Boussinesq_subgrid-scale_model_with_dynamic_tensorial_co.pdf"
tags: [sgs-model, non-boussinesq, wmles, separated-flow]
timestamp: 2026-10-25T13:45:00Z
---

# Summary

Agrawal et al. (2022) propose the
[dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
(DTCSM), a subgrid-scale closure for incompressible
[LES](/definitions/large-eddy-simulation.md) that drops the stress–strain
alignment of the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md).
It starts from Moin's tensor-coefficient form of the
[Smagorinsky model](/methods/smagorinsky-model.md),
$\tau^d_{ij}=-(C_{ik}\bar S_{kj}+C_{jk}\bar S_{ki})\lvert\bar S\rvert\Delta^2$.
The constraints $C_{11}=C_{22}=C_{33}$ and $C_{ij}=-C_{ji}$ ($i\ne j$) make
the model traceless and leave four coefficients, which the
[dynamic procedure](/methods/dynamic-procedure.md) fits to the Germano
identity by least squares. Only the isotropic coefficient dissipates. The
antisymmetric part is equivalent to a strain–rotation commutator term, the
form of the Lund–Novikov velocity-gradient expansion.

[A priori](/definitions/a-priori-and-a-posteriori-testing.md) on filtered
[channel](/benchmarks/turbulent-channel-flow.md) DNS at $Re_\tau=395$ and
$2000$, DTCSM correlates better with the exact stress than the dynamic
Smagorinsky model (DSM), most of all near the wall, while the dissipation
correlations are identical. The coefficients vanish in laminar flow, and
$\tau_{12}\sim y^{+3}$ at a wall without damping functions. A posteriori,
DTCSM dissipates like DSM in decaying and forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
In [wall-modelled LES](/methods/wall-modelled-les.md) of channel flow at
$Re_\tau=4200$ with an [equilibrium wall model](/methods/equilibrium-wall-model.md),
the error in the log-law slope ($\kappa$) falls from 7% (DSM) to 5%, and
DTCSM needs none of the clipping DSM needs. With [CharLES](/software/charles.md)
on the Boeing Gaussian bump (spanwise-periodic and three-dimensional), DTCSM
converges monotonically toward the reference $C_f$ and $C_p$ on three grids,
recovers the favourable-pressure-gradient $C_f$ peak and, on the finest grid,
the separation bubble. The [Vreman model](/methods/vreman-model.md) misses
the separation on the 3D bump. The paper also discusses the
[scale-similarity model](/methods/scale-similarity-model.md) as the
classical non-Boussinesq alternative, as well as
[energy backscatter](/definitions/energy-backscatter.md),
[log-layer mismatch](/definitions/log-layer-mismatch.md) and the
[law of the wall](/definitions/law-of-the-wall.md) underlying the wall model.
DTCSM costs up to about 15% more than DSM.

# Version read

Accepted manuscript made available via CHORUS (manuscript dated 3 May
2022), 25 PDF pages: one CHORUS cover page and 24 manuscript pages, some
with revision highlighting. Not the APS version of record. The cover sheet
and Crossref give the author order Agrawal, Whitmore, Griffin, Bose, Moin;
the manuscript title block lists Bose separately under a second
affiliation. Metadata (year, venue, DOI) are those of the published
version. Equation, section and figure numbers on this page are those of the
manuscript.

# Key claims

1. Boussinesq SGS models assume that the SGS stress is aligned with the resolved strain rate, and a priori DNS analyses show this is locally invalid (Abstract; §I; §III). **Stated**
2. DTCSM starts from Moin's tensor-coefficient Smagorinsky model, Eq. (11), whose general form has nine coefficients and is not guaranteed to be traceless (§III.A). **Stated**
3. The constraints $C_{11}=C_{22}=C_{33}$ and $C_{ij}=-C_{ji}$ ($i\ne j$) (Eq. 12) make the model traceless for incompressible flow, reducing the free coefficients from nine to four (§III.A; App. A). **Derived**
4. The four coefficients are computed dynamically from the Germano identity, written in registry sign as $L_{ij}=-\Delta^2(C_{ik}M_{kj}+C_{jk}M_{ki})$ with $M_{ij}=(\hat\Delta/\Delta)^2\lvert\hat{\bar S}\rvert\hat{\bar S}_{ij}-\widehat{\lvert\bar S\rvert\bar S_{ij}}$, by solving the over-determined system in the least-squares sense (Lilly), Eqs. (13), (B1)–(B4). **Derived**
5. Only $C_{11}$ (equivalently $C_{22}$, $C_{33}$) dissipates large-scale energy; the antisymmetric terms are non-dissipative (§III.A). **Stated**
6. As in DSM, the only input parameter is the test-to-grid filter-width ratio, $\hat\Delta/\Delta=2$ (§III; §X). **Stated**
7. A priori, on filtered channel DNS at $Re_\tau=395$ and $2000$ (commutative filter with three vanishing moments, width three grid spacings), DTCSM gives higher stress-tensor correlations (Eq. 14) than DSM, improving with $Re_\tau$, with the largest gain near the wall (§V; Fig. 1). **Shown**
8. A priori, DTCSM and DSM have the same dissipation-rate correlations across the channel, since only the Smagorinsky-type terms dissipate (§V; Fig. 2). **Shown**
9. Changing the a priori filter width from two to four grid spacings leaves the qualitative trends unchanged (§V, "not shown"). **Stated**
10. The Bardina scale-similarity model has much better a priori tensor correlations than DTCSM but is under-dissipative a posteriori and needs added Smagorinsky dissipation (§V). **Stated**
11. In sufficiently resolved laminar flow $L_{ij}\to0$, so the DTCSM coefficients vanish (§VI). **Derived**
12. With a test filter that does not act in the wall-normal direction and $u^+\sim y^+$, $v^+\sim y^{+2}$, $w^+\sim y^+$: $C_{11}\sim y^{+3}$, $C_{12}\sim y^{+2}$, $C_{13}\sim0$, $C_{23}\sim y^{+2}$, hence $\tau_{12}\sim y^{+3}$ without damping functions (§VI; App. B). **Derived** (the solution of the system is asserted, not shown step by step)
13. Decaying isotropic turbulence at $Re_\lambda=70$ (LES $32^3$, DNS $128^3$): DSM and DTCSM follow the filtered DNS in $k_{\mathrm{res}}$ and dissipation after a transient of up to one eddy turnover; decay exponent $\approx-1.35$ for both models against $\approx-1.37$ for box-filtered DNS (§VII.A; Figs. 3–4). **Shown**
14. DTCSM dissipates as well as DSM "without any ad hoc modifications to the dynamic procedure", unlike constant-coefficient non-Boussinesq models [5, 13] (§VII.A). **Shown** (isotropic turbulence) / **Stated** (for [5, 13])
15. Forced isotropic turbulence at $Re_\lambda=315$ (LES $128^3$ against filtered $1024^3$ DNS of Cardesa et al.): both models recover the $k^{-5/3}$ range and match the filtered-DNS spectra (§VII.B; Fig. 5). **Shown**
16. Isotropic turbulence as $Re_\lambda\to\infty$ ($128^3$): DTCSM and DSM recover K41 scaling; the run without a model shows $k^2$ equipartition (§VII.C; Fig. 6). **Shown**
17. WMLES of channel flow at $Re_\tau=4200$ (20 points per half-height, $\Delta^+\approx200$, equilibrium wall model, $h_{\mathrm{wm}}$ at the second off-wall point): DTCSM slightly improves the log-region mean velocity; the error in $\kappa$ against the DNS value $0.38$ drops from 7% (DSM) to 5% (DTCSM) (§VII.D; Fig. 8). **Shown**
18. Near-wall streamwise and wall-normal intensities are lower with DTCSM than with DSM, closer to unfiltered DNS (§VII.D; Fig. 9). **Shown**
19. DSM needed clipping of the SGS stress at the second off-wall point in this WMLES; DTCSM needed none (§VII.D; Fig. 10). **Shown**
20. Both dynamic models under-predict the SGS stress in the under-resolved first cells, which raises the resolved fluctuations and flattens the mean-velocity slope; only profiles at $y\ge h_{\mathrm{wm}}$ are plotted (§VII.D). **Stated**
21. Spanwise-periodic Gaussian bump ($Re_L=2\times10^6$): DTCSM converges monotonically toward the quasi-DNS $C_f$ on three grids, while DSM and Vreman converge non-monotonically (separation on the coarse grid, lost on the medium, back on the fine) (§VIII.A; Fig. 13). **Shown**
22. On the fine grid DTCSM recovers the favourable-pressure-gradient $C_f$ peak that DSM under-predicts; both dynamic models give the quasi-DNS bubble extent, Vreman a smaller one (§VIII.A; Figs. 13–14). **Shown**
23. 3D bump ($Re_L=3.41\times10^6$): DSM separates on the coarse grid, both dynamic models lose the separation on the medium grid and both separate on the fine grid ($y^+\sim30$ at the first cell upstream), with bubble size matching Gray et al.; DTCSM is monotonic in $C_f$ and $C_p$ and gives the best fine-grid $C_p$ against Williams et al. (§VIII.B; Figs. 15–16). **Shown**
24. Both dynamic models capture the small mid-span $C_p$ rise at the apex and the counter-rotating vortex pair of the oil-flow pictures; Vreman misses the separation, the pressure rise and the vortex pair even on the finest grid (§VIII.B; Figs. 17–19). **Shown**
25. Both dynamic models predict the suction peak because it is mainly inviscid; a free-slip run (not shown) also predicts it (§VIII.B). **Stated**
26. DTCSM costs up to about 1.15 times DSM: 15 against 13 GPU-node-hours per flow-through on the 52 M-cell spanwise-periodic mesh, 112 against 100 on the 452 M-cell 3D mesh (NVIDIA V100 nodes) (§IX; Tables IV–V). **Shown**
27. With the constraints, DTCSM can be rewritten as $\tau^d_{ij}=-2C_{11}\Delta^2\lvert\bar S\rvert\bar S_{ij}-\Lambda\Delta^2(\bar S_{ik}\bar\Omega_{kj}-\bar\Omega_{ik}\bar S_{kj})$, with $\lvert\bar S\rvert C^d_{ij}=-\Lambda\bar\Omega_{ij}$; this is the form of the two-term velocity-gradient expansion of Lund & Novikov [39], so DTCSM accounts explicitly for large-scale rotation (App. C; Eq. C3). **Derived**
28. Prior work [20] shows that DSM gives more accurate integrated quantities and separation extents than static-coefficient models on realistic aircraft (§I). **Stated**

# Printed slips

1. §III.A (after Eq. 12) and App. C call the constraints of Eq. (12) "realizability constraints", while App. A, titled "Proof of tracelessness", and §III.A derive them as tracelessness constraints.
2. §VIII.B: "For DTCSM, as the grid is refined, the trough of $C_f$ moves towards DNS monotonically": the 3D-bump reference is the experiment of Gray et al. [24], not a DNS.
3. Fig. 6 caption: "Comparison … between filtered-DNS and SGS models", while the legend and §VII.C compare with the K41 spectrum.
4. Eq. (4) writes $\tau_{kk}$ without the "sgs" superscript of the surrounding equations; Eq. (11) and App. C drop the overbars on $S$.
5. Typos: "Guassian" (§I), "Smagorsinky-model-type" (§VII.A), "finite-different, Cartesian-staggered meshes" (§VII.D), "upto" (§X); "Iyer and Malik [26]" and "Iyer et al. [26]" for the same reference (§VIII.B).
6. The abstract cites "Meneveau and Liu, Ann. Rev. Fluid Mech. 2002" and "Stolz and Adams, Phys. of Fluids, 1999", neither of which is in the printed reference list.

# Notation map

| Agrawal et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f=\int\mathcal G f\,dx'$ | $\bar\phi=G*\phi$ | LES filter, assumed to commute with differentiation |
| $\widehat{(\cdot)}$ | $\hat\phi$ | test filter, $\hat\Delta/\Delta=2$ |
| $\tau^{sgs}_{ij}=\overline{u_iu_j}-\bar u_j\bar u_i$ | $\tau_{ij}$ | same positive-trace convention |
| $\bar S_{ij}$, $\lvert S\rvert=\sqrt{2\bar S_{ij}\bar S_{ij}}$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | factor two present; overbars often dropped in §III and the appendices |
| $L_{ij}=-\widehat{\bar u_i\bar u_j}+\hat{\bar u}_i\hat{\bar u}_j$ | $-L_{ij}$ | **opposite sign** to the registry's $L_{ij}$ |
| $M_{ij}$ | $M_{ij}$ | $\Delta^2$ kept outside |
| $C_{ij}$, $C^d_{ij}$, $\Lambda$ | — | DTCSM coefficient tensor, its antisymmetric part, rotation-term coefficient |
| $R_{ij}$ (App. C) | $\bar\Omega_{ij}$ | **collision**: rotation-rate tensor, not the Reynolds stress $R_{ij}$; not defined in the paper |
| $C_s$ | $C_s$ | |
| $\alpha_{ij}=\partial\bar u_i/\partial x_j$, $\beta_{ij}$, $B_\beta$ (Vreman) | — | **collision** with $\alpha$ (DG/FV blending) and $\beta(\boldsymbol x)$ (field inversion) |
| $\rho$ (Eq. 14) | — | **collision**: averaged correlation coefficient, not density |
| $tke$, $\epsilon$ (Eq. 15) | $k_{\mathrm{res}}$, $\varepsilon$ | resolved kinetic energy; viscous plus SGS dissipation |
| $\kappa$ | $\kappa$; $k$ | **collision**: von Kármán constant (§VII.D) and wavenumber (Figs. 5–6); the wavenumber is $k$ in the registry |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | homogeneous-direction, time or volume average |
| $h_{wm}$ | $h_{\mathrm{wm}}$ | second off-wall point (channel), first (bump) |
| $Re_L$, $L$ | $Re$ on the bump width $L$ | |
| $h_0$, $x_0$, $z_0$ | — | bump height, Gaussian length, spanwise taper scale |

# Reference list

64 printed references in numbered alphabetical style ([1]–[64]), merged
complete into the [bibliography](/bibliography.md) with `citedby`
`agrawal-2022`. No printed duplicates. Two works cited in the abstract
(Meneveau & Liu 2002; Stolz & Adams 1999) are not in the list and are not
merged. Incomplete items: [12] prints no volume, [17] no article number,
[39] is a CTR Annual Research Briefs report, [33] an NCAR manuscript.
Ref. [23] (Flow 2021) is the source `goc-2021`; ref. [22], a CTR Annual
Research Briefs paper of 2021 by Goc, Bose and Moin on the high-lift common
research model, is a distinct work.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunk 2. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Vreman model](/methods/vreman-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [CharLES](/software/charles.md)
