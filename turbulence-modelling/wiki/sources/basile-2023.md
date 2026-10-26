---
type: Source
title: "Basile et al. (2023) — Hybrid RANS/LES Simulations and Aeroacoustic Analysis of Jet Flows using an hp-Adaptive Discontinuous Galerkin Method"
description: "Extends an hp-adaptive modal discontinuous Galerkin strategy to unsteady hybrid RANS/LES with ZDES mode 0+1 on the negative Spalart–Allmaras model, driving refinement by time-averaged error and modal-decay smoothness indicators, and computes the flow and far-field noise of the PPRIME Mach 0.9 round jet with fewer degrees of freedom than reference simulations."
resource: "doi:10.1007/s10494-022-00376-0"
source_kind: paper
authors: [Basile F., Chapelier J.-B., Laraufie R., Frey P.]
year: 2023
venue: "Flow Turbul. Combust. 110:239-273"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Flow_Turbulence_and_Combustion_Basile_Hybrid_RANSLES_Simulations_and_Aeroacoustic_Analysis_of_Jet.pdf"
tags: [hybrid-rans-les, des, dg, mesh-adaptation, aeroacoustics]
timestamp: 2026-10-25T16:03:00Z
---

# Summary

Basile et al. (2023) extend their hp-adaptation strategy for discontinuous
Galerkin (DG) methods, built earlier for steady laminar and RANS flows, to
unsteady [hybrid RANS/LES](/definitions/hybrid-rans-les.md). The closure is
zonal [detached-eddy simulation](/methods/detached-eddy-simulation.md) (ZDES)
"mode 0+1" on the negative
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md). RANS is forced
inside the nozzle and DES runs elsewhere. The DES length scale is specific to
DG, $\Delta_{\mathrm{vol}}/(N+1)$ with $\Delta_{\mathrm{vol}}=|K|^{1/3}$, and the
near-wall functions are set to $f_{v1}=1$, $f_{v2}=0$, $f_w=1$ in LES mode. The
solver is the modal DG code CODA (Roe flux with a Harten-type entropy fix,
BR1 viscous terms, three-stage explicit Runge–Kutta).

[Mesh adaptation](/methods/mesh-adaptation.md) is driven by an error estimator.
It sums a min–max-normalized small-scale energy density (the momentum energy
in the highest modal level) and an inter-element momentum jump, both averaged
in time. A smoothness indicator decides between $h$ and $p$: $\sigma$ is the
least-squares decay exponent of the modal energy, $E^{(q)}\simeq Cq^{-\sigma}$.
Its threshold $5/3$ is taken from the inertial-range slope. Smooth elements
gain one polynomial degree. The other elements are refined isotropically by
the MMG remesher, and each step doubles the degree-of-freedom count.

The test is the isothermal PPRIME round jet ($M_j=0.9$, $Re_D\simeq10^6$) on
three meshes of 11.6, 18.9 and 31.7 million degrees of freedom with
$1\le N\le3$. Refinement lengthens the potential core. The intermediate mesh
is closest to experiment on the centreline, while the finest mesh overpredicts
the core length but agrees with the finest ZDES and
[implicit LES](/definitions/implicit-les.md) references, which use more
degrees of freedom. Far-field noise from a closed-surface Ffowcs
Williams–Hawkings integral is within about 1–2 dB of experiment. The authors
attribute the remaining discrepancies to the missing turbulent tripping in
the nozzle and to the short averaging time.

# Version read

HAL deposit hal-04567955v1 (submitted 3 May 2024): the authors' accepted
manuscript in the Springer Nature 2021 LaTeX template, not the version of
record. It has 44 PDF pages: a HAL cover and manuscript pages 1–43, all read.
Locators on this page use the manuscript numbering (not journal pages
239–273). The HAL cover prints the DOI and the title capitalization of the
metadata. The filename year (2022) is the online-first year, and the issue
year is 2023. There is no identity problem.

# Key claims

1. The hp-adaptation strategy of the authors' earlier steady laminar/RANS work is extended to unsteady hybrid RANS/LES on hybrid prism/tetrahedron meshes. Static adaptation is driven by time-averaged error and smoothness indicators (§3, §3.3, §3.4). **Shown**
2. ZDES mode 0+1 replaces the wall distance $d$ in the SA destruction term with $d$ in RANS zones and with $\min(d,C_{DES}\tilde\Delta_{DES})$ in DES zones. $C_{DES}$ is "usually set to 0.65", calibrated on decaying homogeneous turbulence (§2.2, Eq. 6). **Stated**
3. The paper lists three differences from classical DES: (i) $\tilde\Delta_{DES}$ uses the cube root of the element volume, not the largest cell dimension; (ii) it is divided by the number of one-dimensional degrees of freedom, $\tilde\Delta_{DES}=\Delta_{\mathrm{vol}}/(N+1)$, after Lorteau et al.; (iii) in LES mode $f_{v1}=1$, $f_{v2}=0$, $f_w=1$ (Eq. 7) (§2.2). **Stated** (design choice)
4. In LES regions the eddy viscosity scales as $\rho\tilde\nu\sim|\boldsymbol\omega|\tilde d^2_{ZDES}$, so it decreases with the square of the element size. The adaptation lowers $\mu_t$ in the shear layer progressively from hpG1 to hpG3 (§2.2; §4.2.2, Fig. 7). **Shown** (qualitatively, contour plots)
5. User zoning, with RANS forced inside the nozzle, prevents grid-induced separation of attached boundary layers (§2.2). **Stated**
6. The coupled estimator (small-scale energy density plus jump, each min–max normalized, Eq. 10) is reliable for both high and low $N$. The small-scale energy density alone is reliable only at high $N$, and the jump indicator is accurate at every degree (§3.1). **Stated** (justified from the authors' earlier work)
7. The small-scale energy density has a physical meaning for turbulence: it is the turbulent energy at the cut-off wavenumber of the discretization, related to subgrid activity, as in spectral eddy-viscosity models (§1). **Stated**
8. The new smoothness indicator is the decay exponent $\sigma$ of $E^{(q)}\simeq Cq^{-\sigma}$, with threshold $\sigma_{\mathrm{thr}}=5/3$ (the inertial-range slope). It replaces the Mavriplis decay-rate formulation and is argued to suit scale-resolving flows, because the modal spectrum inside an element spans the scales between the mesh cut-off and the cut-off of the full discretization (§3.2, Eqs. 11–12). **Stated** (no separate validation in this paper)
9. Chapelier et al. evaluated the under-resolution threshold a priori on Taylor–Green DNS at $Re=5000$ and found values very close to the $-5/3$ slope. The indicator behaved consistently on irregular meshes, at various degrees and on various flows (§3.2). **Stated** (cited)
10. The $q=0$ coefficient is excluded from the regression because it biases the decay rate, so $\sigma$ exists only for $N\ge2$. Elements with $N=1$ are "fictitiously" marked smooth and always gain one degree (§3.2). **Stated** (design choice)
11. Starting the hybrid RANS/LES adaptation from a RANS-hp-adapted mesh is preferred to a very coarse initial mesh. A very coarse mesh would prevent turbulent structures from developing, could cause instabilities and would need many unsteady adaptation steps (§3.3). **Stated**
12. The error estimator does not need a long accumulation time to become representative in poorly resolved zones: here $T_{\epsilon\sigma}=30t_c$ against $T_{\mathrm{stats}}=150t_c$, with $t_c=D/U_j$ (§3.3, §4.1). **Stated**
13. Forcing $N=1$ in elements with centres at $x_c>35D$ and $r_c>10D$ makes a sponge layer that damps turbulent structures and strong sound waves and lowers cost. No significant spurious acoustic reflection is observed at the sponge or at interfaces between degrees (§4.1, Fig. 2). **Shown** (qualitative)
14. The estimator marks the lipline and the centreline at the end of the potential core as most unresolved. Lipline elements, already at $N_{\max}=3$, are $h$-refined at both steps; centreline elements are first $p$-enriched (hpG2) and then $h$-refined (hpG3). In scale-resolving runs the degrees of freedom concentrate in the turbulent shear layers, whereas in the earlier RANS runs they concentrated in the high-gradient zone of the potential core (§4.2.1, Figs. 3–4). **Shown**
15. Refining the plume ($h$ and $p$) slows the centreline velocity decay and lengthens the potential core. hpG2 is closer to experiment than the finer hpG3, which overpredicts the core length. Shur et al. and Gand & Huet report the same trend, and so to a lesser extent do Brès et al. and Lorteau et al. (§4.2.3, Fig. 9). **Shown**
16. Candidate causes of the overlong potential core are implicit LES and the missing nozzle–jet feedback loop (Shur et al.), the missing turbulent injection or tripping in the nozzle (Lorteau et al.), and insufficient resolution. The authors think a combination is responsible and give no formal answer (§4.2.3). **Stated**
17. Spurious peaks in the centreline rms profiles, strongest on hpG1 and decreasing with adaptation, are attributed to DG inter-element discontinuities on coarse elements (also seen in an a priori DG/LES projection of DNS by Beck et al.) and to poor sampling on the axis, where there is no azimuthal averaging (§4.2.3, Fig. 10). **Shown** / **Stated** (cause)
18. Under-resolution just downstream of the nozzle exit speeds up the transition of the mixing layer, giving higher, apparently better, turbulence intensities on hpG1. The finer runs underpredict turbulence intensities for $x/D<10$, as the reference simulations do, and the rms levels approach experiment for $x/D>10$ with adaptation (§4.2.3, Figs. 10, 12). **Shown**
19. The finest hp mesh (31.7 M degrees of freedom) uses fewer degrees of freedom than the unstructured DG ($N=3$) LES of Lorteau et al. (78 M) and the structured finite-volume ZDES of Gand & Huet (48 M and 154 M) "while achieving very close results" (§4.2.3, Table 1). **Shown**
20. Far-field PSD: noise is overpredicted on hpG1 and hpG2 at all angles. Refinement lowers the PSD, most at low frequency. hpG3 predicts the medium-frequency levels well and slightly underpredicts low frequencies at low angles. At high angles the medium-frequency PSD is overpredicted at all three resolutions, which the authors attribute to vortex roll-up and pairing outside the untripped nozzle (§4.4, Fig. 14). **Shown**
21. OASPL ($0.05<St<3$): hpG3 overpredicts by about 1 dB (polar array) and 2 dB (cylindrical array) at high angles and underpredicts by 1–2 dB for $\theta<40^\circ$, with $\theta$ the observation angle from the jet axis (§4.4, Fig. 15). **Shown**
22. The acoustic results are globally independent of the choice of FW-H control surface among S1–S4 and the closing discs D1–D3. Only the S1-D3 results are shown (§4.3). **Shown** (asserted; data not displayed)
23. Longer simulations ($T_{\mathrm{stats}}>300D/U_j$) are needed to reduce the uncertainty from low-frequency phenomena (§4.4). **Stated**
24. Pure $p$-adaptation on a fixed mesh needs very high degrees. These complicate load balancing, raise the cost per degree of freedom and can cause instability from aliasing or too little numerical dissipation. This motivates $hp$- rather than $p$-adaptation for DG LES (§1). **Stated**
25. On Taylor–Green tests in the authors' earlier work, high-order DG describes turbulence more accurately than low-order DG at an equal number of degrees of freedom, so $N=3$ is desirable in the mixing layer (§4.2.1). **Stated** (cited own work)

# Printed slips

- **Eq. 18 (§3.4, step 8).** The paper prints "$p^*_{K,i+1}=\max(p_{K,i}+1,p_{max})$". The marking rules of Eqs. 15–16 admit an element for enrichment only if $p_{K,i}+1\le p_{max}$, and on such elements the printed $\max$ always returns $p_{max}$. The text describes enrichment by one degree per step (for example $N=2$ to $N=3$ from hpG1 to hpG2). *(Compiler check, not in the sources.)*
- **§3.4, after Eq. 19.** "Let $N_{i+1}$ be the number of dofs in the $i$-th mesh, and $N^*_{i+1}$ be the number of dofs in the new $(i+1)$-th mesh … $N^*_{i+1}=f_r\cdot N_i$". The first symbol is $N_i$ in the formula.
- **§3.4.** The degree-of-freedom count is "increased at each adaptation step by a fixed percentage $f_r$". In use, $f_r=2$ is a multiplicative factor ("twice the number of dofs", §4.1).
- **§3.4, step 5.** The text says elements "presenting fixed geometry or a $p1=$ discretization, are marked for p-enrichment", but Eq. 15 covers only the fixed elements, and the $N=1$ case is in Eq. 16. The wording "$p1 =$" is garbled.
- **Eq. 12.** "$\forall q\in(1,p_K)$" is printed as an open interval. The text excludes only $q=0$.
- **§4.3, cone radii.** The paper prints "$r/D = 3.68, 4, 4.35, 4.72$ respectively for S1, S2, S3, S4", from upstream radii 0.68, 1, 1.35, 1.7. S1–S3 each grow by exactly $3.00D$, and S4 grows by $3.02D$. The paper does not say whether S4's cone differs. *(Compiler check, not in the sources.)*
- **§4.1.** "$r_h=4$ such that … the edge of the equilateral triangle can at most divide by four its size". The adaptation is three-dimensional on tetrahedra.
- **References.** [82] prints the fourth author as "Frey, R.", while the paper's own byline has Frey P. [37] prints "Computational Physics Communications 257, 107492". [75] prints "7nd European Conference". [87] carries LaTeX residue in its title ("up to re h= 10, 595 \text {Re} {H}= 10 {,} 595"). [6, 13, 65, 73] print the publisher address as "???".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, $p_K$, $p_{\min}$, $p_{\max}$ | $N$ (polynomial degree), $N_{\min}=1$, $N_{\max}=3$ | **collision:** the source's $p$ is the degree, not the pressure; "DG-4o" means $N=3$ |
| $N$ | (number of elements) | **collision:** not the polynomial degree |
| $N_i$, $N^*_{i+1}$ | (degrees of freedom of mesh $i$, target for mesh $i+1$) | |
| $K$, $\lvert K\rvert$, $\mathcal T_K$ | (element, its volume, tessellation) | |
| $h$ | $h$ | element size, as in the registry |
| $\phi_K^l$, $u_K^l$, $d_q$ | (hierarchical orthonormal modal basis, modal coefficient, index set of total degree $q$) | modal DG on simplices and prisms, not DGSEM |
| $\{\{\cdot\}\}$, $[[\cdot]]$ | $\{\!\{\cdot\}\!\}$, (jump) | |
| $\boldsymbol\sigma_h$, $\mathbf L_h$ | (BR1 auxiliary gradient, global lifting operator) | **collision:** not the viscous stress $\sigma_{ij}$ and not the smoothness indicator |
| $\tilde\nu$, $f_{v1}$, $f_{v2}$, $f_w$, $\tilde S$ | $\tilde\nu$, $f_{v1}$, $f_{v2}$, $f_w$, $\tilde S$ | SA working variable and functions; $\kappa=0.41$ |
| $\mu_t=\rho\tilde\nu f_{v1}$ ($\tilde\nu\ge0$), $0$ ($\tilde\nu<0$) | $\mu_t$ | negative SA, Eq. 5 |
| $\tilde\omega$ | $\lvert\boldsymbol\omega\rvert$ | vorticity magnitude; **collision:** not the specific dissipation $\omega$ |
| $d_w$ | $d$ | wall distance |
| $\tilde d_{ZDES}$, $C_{DES}$, $\tilde\Delta_{DES}$ | (ZDES length scale), $C_{DES}=0.65$, (DES length scale $\Delta_{\mathrm{vol}}/(N+1)$) | registry $\Delta$ is the filter width; here the DES length is a page-local quantity |
| $\Delta_{vol}=\sqrt[3]{\lvert K\rvert}$, $\Delta_{max}$ | (cube root of element volume, largest cell dimension) | |
| $(\rho\mathbf v)_h$ | $\rho\boldsymbol u$ (discrete momentum) | the source writes velocity $\mathbf v$ |
| $\epsilon_{SSED,K}$, $\epsilon_{JUMP,K}$, $\epsilon_K$, $\epsilon^*$ | (small-scale-energy, jump and coupled error indicators; target error) | **collision:** not the dissipation rate $\varepsilon$ |
| $E^{(q)}$, $a_K^{(q)}$ | (modal energy and gathered modal amplitude at degree $q$) | **collision:** not the spectrum $E(k)$; $q$ is a polynomial degree, not a wavenumber |
| $\sigma$, $\sigma_{thr}=5/3$ | (modal decay exponent, threshold) | **collision:** not $\sigma_{ij}$ or the SA/SST diffusion constants |
| $m_n$, $r_h$, $f_r$, $h_{grad}$ | (assumed convergence rate, maximum refinement factor 4, degree-of-freedom growth factor 2, MMG gradation 1.5) | |
| $t_c=D/U_j$, $T_{trans}$, $T_{\epsilon\sigma}$, $T_{stats}$ | (convective time; transient, indicator and statistics windows $50t_c$, $30t_c$, $150t_c$) | |
| $M_j$, $Re_D$, $D$ | $M$ (jet exit), $Re_D$, (nozzle diameter 0.05 m) | |
| $\theta$ | (observation angle from the jet axis) | **collision:** not the momentum thickness |
| $St=fD/U_j$ | $St$ | |
| "mean", "rms" | $\langle\cdot\rangle$ (time average, plus azimuthal average off axis) | no averaging operator is printed |

# Reference list

90 printed references, numbered style [1]–[90]. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Reference
[44] is an undated NASA Glenn web page ("Acoustic Reference Nozzle with Mach
0.97, Unheated Jet Flow", accessed 2021-10-15) with no printed author. It is
entered under a corporate NASA key with the citing year. Reference [87] has a
title garbled by LaTeX residue and is transcribed with the residue removed and
noted. Reference [64] (Leicht et al., CEAS Aeronautical Journal 2016) prints
no volume or pages. There are no printed duplicates and no unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunk 6. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Vreman model](/methods/vreman-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
