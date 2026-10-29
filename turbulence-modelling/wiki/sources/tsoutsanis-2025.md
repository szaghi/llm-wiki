---
type: Source
title: "Tsoutsanis & Nogueira (2025) — Arbitrary-order unstructured finite-volume methods for implicit large eddy simulation of turbulent flows with adaptive dissipation/dispersion adjustment (ADDA)"
description: "Introduces ADDA, an a priori cell-by-cell control of numerical dissipation for implicit LES with arbitrary-order CWENOZ finite volumes on unstructured meshes: a filtered-energy-ratio sensor switches the central linear weight and scales the Riemann-flux dissipation; tested on inviscid and supersonic Taylor–Green vortices, the SD7003 airfoil and a transonic cylinder."
resource: "doi:10.1016/j.jcp.2024.113653"
source_kind: paper
authors: [Tsoutsanis P., Nogueira X.]
year: 2025
venue: "J. Comput. Phys. 523:113653"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Computational_Physics_Tsoutsanis_Arbitrary-order_unstructured_finite-volume_methods_for_impli.pdf"
tags: [implicit-les, numerical-dissipation, finite-volume, weno, high-order, compressible]
timestamp: 2026-10-29T05:09:00Z
---

# Summary

Tsoutsanis & Nogueira (2025) address the control of numerical dissipation
and dispersion in [implicit LES](/definitions/implicit-les.md) with
high-order non-oscillatory finite-volume schemes on unstructured
mixed-element meshes. Their premise is that too little dissipation lets
energy build up unphysically in the high modes while too much damps the
resolved scales, that dissipation and dispersion are entangled for
non-linear schemes on unstructured meshes, and that dispersion-relation
tools ([eigensolution analysis](/methods/eigensolution-analysis.md)) do
not extend usefully to that setting
([numerical dissipation](/properties/numerical-dissipation.md)). Earlier
automatic dissipation adjustment is either tied to structured meshes or
a posteriori, which is awkward with implicit dual-time stepping.

The contribution is the ADDA algorithm, implemented in the open-source
UCNS3D code. At every time step and in every cell it (i) computes an
energy ratio $E_{\mathrm R}$ of the momentum reconstructed by the
unlimited central-stencil polynomial, unfiltered and filtered by a weak
and a strong sharp modal filter on the Taylor basis (the filters act only
as a sensor, see [explicit modal filtering](/methods/explicit-modal-filtering.md));
(ii) classifies the cell by two thresholds and sets the unnormalized
central linear weight of the CWENOZ reconstruction
([WENO schemes](/methods/weno-scheme.md)) to 2 (more dissipation) or 1000
(less); (iii) for Roe and Rusanov fluxes, raises or lowers a multiplier
$c^{\mathrm F}_i\in[0.5,1]$ of the flux dissipation in steps of 0.05,
resetting it to 1 when the non-linear central weight signals a
discontinuity ([shock sensors](/definitions/shock-sensor.md)).

Tests: the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
on hexahedral and tetrahedral meshes against the Brachet et al. DNS
dissipation; the [SD7003 airfoil](/benchmarks/sd7003-airfoil.md) at
$Re_c=60\,000$, where CWENOZ4 on 5.3M cells beats second-order MUSCL on
12.3M cells and ADDA lowers the dissipation inside the
[laminar separation bubble](/definitions/laminar-separation-bubble.md);
the supersonic viscous Taylor–Green vortex at $M=1.25$, $Re=1600$ against
CODA and OpenSBLI data of [Chapelier et al. (2024)](/sources/chapelier-2024.md);
and a transonic [circular cylinder](/benchmarks/circular-cylinder-wake.md)
at $Re_D=166\,000$, $M_\infty=0.8$. The ADDA overhead is 1.8–8.2%. The paper
calls the "build-up of energy in the high modes" it targets "unphysical"
(§1) and does not discuss the [bottleneck effect](/definitions/bottleneck-effect.md);
references from [discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
and [PyFR](/software/pyfr.md) runs serve as SD7003 data, and decaying
compressible [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
appears only in the literature review.

# Version read

Version of record (Elsevier, open access CC BY; received 3 April 2024,
revised 20 September 2024, accepted 2 December 2024, online 6 December
2024), 34 pages, all read; the smoothness-indicator symbols and the
flowchart (pp. 6–8) read visually. Page 1 matches the metadata (title,
both authors, venue, DOI); no identity issue. A data set is deposited at
doi:10.57996/cran.ceres-2638. Equation, figure, table and section numbers
are those of this version. "A priori" and "a posteriori" are used in the
limiting sense (dissipation decided before or after the update), not in
the sense of [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

# Key claims

Page-local symbols: $r$ the degree of the reconstruction polynomial (order
of accuracy $r+1$; CWENOZ$n$ is the $n$-th-order scheme); $K$ the number
of polynomial coefficients; $d_s$, $d_1$ the normalized linear weights of
the directional and central stencils and $d'_1$ the unnormalized central
weight, $d_1=1-1/d'_1$ (the source's $\lambda_s$, $\lambda_1$,
$\lambda'_1$); $a_s$, $\mathsf w_s$ the unnormalized and normalized
non-linear weights and $\mathrm{IS}_s$ the smoothness indicator (registry
§11); $E_{\mathrm R}$ the energy ratio, $\mathrm{LT}$, $\mathrm{UT}$ its
lower and upper thresholds; $c^{\mathrm F}_i$ the flux-dissipation
multiplier of cell $i$ (the source's $d_i$); $C_{\mathsf w}$ the
threshold on $\mathsf w_1$ that resets $c^{\mathrm F}_i$; $\Lambda_{\max}$
the largest wave speed of the Rusanov flux; $z_{\mathrm{LM}}$ the blending
of the low-Mach correction; $\varepsilon_t=\varepsilon_s+\varepsilon_d$
the total dissipation; $x_s$, $x_r$ the separation and reattachment
abscissae.

1. A method with very low dissipation is unsuitable for implicit LES on under-resolved grids because it produces an unphysical "build-up" of energy in the high modes; implicit LES needs "the right amount" of dissipation and dispersion (§1). **Stated**
2. For non-linear methods on unstructured meshes dissipation and dispersion are entangled: dispersion errors become more pronounced when dissipation is reduced, and increased dissipation overwhelms them (§1, §4.1). **Stated**
3. A posteriori dissipation strategies (as in Nogueira et al. [25]) are hard to implement with implicit time stepping, because cells with inadmissible solutions influence the whole domain through the linear system; hence an a priori approach (§1). **Stated**
4. Dispersion-relation analysis is limited to linear methods (or 1-D without non-linear interactions), and its extension to unstructured meshes "leads to results that are not understandable and therefore of unclear value at present" (§1, §4.1, citing Ruano et al. [88] and Pirozzoli [87]). **Stated**
5. ADDA has three procedures — energy-ratio measurement, CWENOZ adaptation through $d'_1$, flux-dissipation adaptation through $c^{\mathrm F}_i$ — executed for every cell and face at every explicit Runge–Kutta step or every physical time step of dual-time stepping (§4, Fig. 3, Remark 4). **Derived** (algorithm definition)
6. Of seven candidate filters (Table 1), only filter 1 (sharp) and filter 7 (exponential, strength 32/8, order 8/8) give a useful $E_{\mathrm R}$ signal on the inviscid Taylor–Green vortex with CWENOZ4 at $64^3$; filter 4's variation is "very close to machine precision" and the others stay flat (§4.1, Fig. 5). **Shown**
7. The mean $E_{\mathrm R}$ rises as the Taylor–Green vortex transitions and then stabilizes; cells with $E_{\mathrm R}\gg1$ indicate an unphysical build-up of energy in the high modes, not only under-resolution (§4.1, Figs. 5–6). **Shown**
8. Tetrahedral and hybrid meshes show more cells with $E_{\mathrm R}>1.2$ than the hexahedral mesh even at $t=2$, "indicative of their dispersive properties" (§4.1, Fig. 6, citing [90]). **Shown**
9. The thresholds $\mathrm{LT}=0.95$ and $\mathrm{UT}=1.2$ are chosen from the filter-1 and filter-7 experiments; fine-tuning is out of scope (§4.1, Eq. 36). **Stated**
10. Raising the polynomial degree or the central linear weight reduces numerical dissipation and improves agreement with the Brachet et al. DNS and with the Kolmogorov slope on the $64^3$ hexahedral mesh (§5.1, Figs. 8–10). **Shown**
11. ADDA with the Roe flux (acting on $d'_1$ and $c^{\mathrm F}_i$) performs better than ADDA with HLLC (acting on $d'_1$ only) on the inviscid Taylor–Green vortex (§5.1, Figs. 8–10). **Shown**
12. The low-Mach correction of Simmonds et al. strongly improves the hexahedral-mesh results; ADDA brings hexahedral ($128^3$) and tetrahedral ($64^3$-equivalent, about 2M cells each) results into much closer agreement, with or without the correction; ADDA with the correction greatly reduces the double peak of the dissipation rate near $t\approx9.5$, which the correction affects most (§5.1, Figs. 11–12). **Shown**
13. ADDA introduces high-frequency oscillations in the dissipation-rate history, attributed to the 0.05 step of $c^{\mathrm F}_i$; a 0.01 step reduces them and 0.1 increases them (§5.1). **Stated** (no figure for the alternative steps)
14. Neither ADDA nor the low-Mach correction alone brings the hexahedral results close to the tetrahedral ones; the tetrahedral mesh with the same number of elements outperforms the best hexahedral result in the spectrum (§5.1, Fig. 13). **Shown**
15. ADDA overhead on the inviscid Taylor–Green vortex is 1.8–8.2%: CWENOZ3 6.1%/8.2% (HLLC/Roe), CWENOZ4 4.8%/6.5%, CWENOZ5 2.7%/3.1%, CWENOZ6 1.8%/2.2%; normalized CPU times 1.00, 2.37, 4.21, 5.80 for CWENOZ3–6 without ADDA (ARCHER2, 2 nodes, 16 MPI processes × 16 OpenMP threads, $64^3$ hexahedra); the Roe variant costs more because of the interprocessor exchange of $c^{\mathrm F}_i$ (§5.1, Table 3). **Shown**
16. SD7003 ($M=0.2$, angle of attack $8^\circ$, $Re_c=60\,000$): CWENOZ4 on mesh A (5.3M cells) agrees better in $C_p$ and $C_f$ with the PyFR, Star-CCM, DGSEM and FDLI3D references than MUSCL2 even on mesh B (12.3M); ADDA further improves $C_f$ (§5.2, Fig. 19). **Shown**
17. SD7003 integral values (Table 4), $C_L$/$C_D$/$x_s/c$/$x_r/c$: MUSCL2-A 0.918/0.050/0.026/0.26; MUSCL2-B 0.933/0.041/0.023/0.23; CWENOZ4-A 0.926/0.044/0.039/0.28; CWENOZ4-ADDA-A 0.927/0.045/0.041/0.27; "Frank et al." [12] 0.923/0.045/0.027/0.310; Galbraith & Visbal [13] 0.917/0.044/0.031/0.303. **Shown**
18. Second-order MUSCL schemes are "unsuitable for iLES simulations at under-resolved grid settings, due to their excessive dissipation characteristics", with unpredictable changes of skin friction, separation and reattachment from mesh A to B (§5.2). **Shown** (on this case)
19. On SD7003, ADDA selects low dissipation in the laminar separation bubble, switches rapidly to high-dissipation-dominant behaviour in the turbulent region, then back to low dissipation further downstream (§5.2, Fig. 18). **Shown**
20. Supersonic viscous Taylor–Green vortex ($M=1.25$, $Re=1600$): without ADDA, CWENOZ5 under-predicts the total dissipation; ADDA improves it substantially on both meshes, and CWENOZ6-ADDA agrees best with CODA (modal DG, fourth order) and OpenSBLI (TENO6) at $128^3$ from Chapelier et al. [114] and with Lusher & Sandham [113]; hexahedral and tetrahedral results converge to each other (§5.3, Fig. 22). **Shown**
21. The total-dissipation spike between $t=2$ and 4 seen at very fine resolutions is driven by a sudden peak of the dilatational dissipation $\varepsilon_d$ (shocklets) at $t=2.8$ (§5.3, Fig. 22, from reference data). **Stated** (shown through the reference data)
22. In the supersonic Taylor–Green vortex the tetrahedral mesh agrees better with the Kolmogorov slope at $t=12$, attributed to the inherently lower dissipation of tetrahedra (§5.3, Fig. 23). **Shown**
23. Using the non-linear central weight of the density prevents very-low-dissipation settings in cells whose stencils cross strong density gradients (§5.3, Fig. 24). **Shown** (qualitative)
24. Transonic cylinder ($Re_D=166\,000$, $M_\infty=0.8$, about 12M cells): CWENOZ4-ADDA gives a shorter wake, more resolved structures and more high-dissipation regions than CWENOZ3-ADDA; $C_p$ agrees with Macha [116] and Murthy & Rose [115] up to $83^\circ$, beyond which all predictions are sensitive (§5.4, Figs. 26–29). **Shown**
25. ADDA is generic for non-oscillatory schemes (WENO, WENOZ, TENO, TENOZ, TENO-A, CWENO, CWENOZ) and extensible to DG and hybrid DG–finite-volume methods; an extension to wall-modelled LES is planned (§4.2, §6). **Stated**
26. $c^{\mathrm F}_i<0.5$ was found not robust for Roe and Rusanov fluxes on the problems used, hence $c^{\mathrm F}_i\in[0.5,1]$ (§4.3). **Stated**

The scheme in registry notation. The CWENOZ polynomial is
$p^{\mathrm{cwenoz}}=\sum_s\mathsf w_sp_s$ with
$\mathsf w_s=a_s/\sum_sa_s$, $a_s=d_s\big(1+(\tau_{\mathrm U}/(\epsilon+\mathrm{IS}_s))^b\big)$,
$\tau_{\mathrm U}=\sum_{s\ge2}|\mathrm{IS}_s-\mathrm{IS}_1|/(s_t-1)$,
$\epsilon=h^4$, $b=4$ (Eqs. 17–21); directional stencils are of degree 1,
the central one of arbitrary degree; $d_1=1-1/d'_1$, $d_s=(1-d_1)/(s_t-1)$
(Eqs. 22–23). The energy ratio (Eq. 29) is
$$E_{\mathrm R}=\frac{\int_{V_i}\big((\rho\boldsymbol u)_{\mathrm R}-(\rho\boldsymbol u)_{\mathrm W}\big)^2dV}{\int_{V_i}\big((\rho\boldsymbol u)_{\mathrm R}-(\rho\boldsymbol u)_{\mathrm S}\big)^2dV},$$
with $\mathrm R$, $\mathrm W$, $\mathrm S$ the unfiltered, weakly and
strongly filtered reconstructions; the filtered polynomials multiply each
coefficient by $\hat G(\vartheta^{\mathrm t}_m)$, with
$\vartheta^{\mathrm t}_m$ the total Taylor degree of the mode. The
classification (Eq. 36) is: $E_{\mathrm R}>\mathrm{UT}$ increase
dissipation ($d'_1=2$), $E_{\mathrm R}<\mathrm{LT}$ reduce it
($d'_1=1000$), unmodified in between *(compiler check, not in the
sources: Eq. 22 gives $d_1=0.5$ and $0.999$ for $d'_1=2$ and 1000)*. The
flux (Eq. 38) is
$\boldsymbol F=\tfrac12(\boldsymbol F_L+\boldsymbol F_R)-\tfrac12c^{\mathrm F}_i\Lambda_{\max}(\boldsymbol U_R-\boldsymbol U_L)$,
with $c^{\mathrm F}=\max(c^{\mathrm F}_{i,L},c^{\mathrm F}_{i,R})$ at each
face for conservation (Remark 6). The low-Mach correction (Eq. 27)
modifies only the face-normal velocity,
$u^*_{n,L}=\tfrac12[(1+z_{\mathrm{LM}})u_{n,L}+(1-z_{\mathrm{LM}})u_{n,R}]$
(and symmetrically), $z_{\mathrm{LM}}=\min(1,\max(M_L,M_R))$. Viscous face
gradients carry a penalty $\tfrac43(\boldsymbol U_R-\boldsymbol U_L)\boldsymbol n/L$
over the distance $L$ between cell centres (Eq. 28). Time stepping:
explicit SSP RK4 (CFL 1.4 on the inviscid vortex), or second-order dual
time stepping with an implicit approximate Jacobian and matrix-free
LU-SGS. The supersonic vortex diagnostics are
$\varepsilon_s=\frac1{\rho_0Re\,V}\int\mu\,\omega_i\omega_i\,dV$ and
$\varepsilon_d=\frac{4}{3\rho_0Re\,V}\int\mu(\nabla\cdot\boldsymbol u)^2dV$
(Eqs. 45–46).

# Printed slips

- **Eq. (4), third line:** "$\Theta_z=u\tau_{zz}+v\tau_{zy}+w\tau_{zz}+\dots$": the first term repeats $\tau_{zz}$ where the pattern of the first two lines gives $\tau_{zx}$.
- **Eq. (17):** "$p_s(z,y,z)$" for $p_s(x,y,z)$.
- **Eq. (14):** the range "$0\le p_k+q_k+r_k\le K$", while $K$ is the number of coefficients and the maximum degree is $r$ (Table 1, text of Eq. 30).
- **§3.1:** $h_0$ is "defined as the square root of the volume of the considered cell". *(Compiler check, not in the sources: in three dimensions the square root of a volume has the dimension of a length to the power 3/2, so $h_0$ as printed is not a length.)*
- **Eq. (24)** is introduced as "the smoothness indicator $\mathcal{SI}_m$" and defines $\mathcal{SI}_s$; the directional linear weight is stated "$\lambda_s=1$" (pp. 6–7) while Eq. (23) gives $(1-\lambda_1)/(s_t-1)$.
- **§4.3:** "when a cell has been tagged for increasing its dissipation through the increase of ($\lambda_1$)", while §4.2 and §5.1 increase dissipation by reducing the central weight to $A=2$.
- **Remark 5:** the reset threshold is printed "$(\omega_1<C)$, with ($C<0.999$) for this study", an inequality instead of a value; the flowchart (Fig. 3) uses $\omega_1\le C$ against $\omega_1>C$.
- **Table 1, filter 1:** "$\eta_{max}=r-2/r-1$" (strong/weak), while the text says the weak sharp filter removes the degree-$r$ terms and the strong one also the degree-$(r-1)$ terms, and Eq. (31) zeroes only $\eta=\eta_{max}$; the three statements do not agree as printed.
- **Table 3:** the CWENOZ6 block lists "CWENOZ5-ADDA-HLLC" and "CWENOZ5-ADDA-Roe" (5.90, 5.92).
- **Overhead:** "approximately (1.8 − 8%)" (§5.1) and "(2-8%)" (§6) against the Table 3 maximum of 8.2%.
- **Fig. 22 caption:** "dilatational dissipation $\varepsilon_t$" for $\varepsilon_d$.
- **§5.3:** the dissipation spike is attributed to "very fine resolutions ($768^3$)" and two sentences later to "very fine mesh resolutions ($2048^3$)"; the source of the $2048^3$ data is not named. The supersonic case uses an "explicit Runge-Kutta 3rd-order scheme" that §3.4 does not introduce.
- **§4.1:** "increase at ($t=8-6$)" (reversed range).
- **Table 4 against §5.2:** the text says "marginal differences are noticed in the separation location and reattachment between all predictions", while Table 4 prints $x_s/c=0.039$ and 0.041 for CWENOZ4 and CWENOZ4-ADDA against 0.027 and 0.031 for the references, and $x_r/c=0.27$–0.28 against 0.303–0.310.
- **Citations:** ref. [12] (first author Beck) is cited as "Frank et al. [12]"; ref. [112] (Tsoutsanis, extended bounds limiter) is cited for "the Barth and Jespersen limiter [112]"; ref. [64] is printed as J. Comput. Phys. 475 (2023) with a DOI token of 2019.
- Typos: "Unfortunalely" (§1), "It needs to be stresses" (§5.1).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\mathbf U_i$ | $\boldsymbol U$, $\boldsymbol U_i$ (page-local) | conserved variables, cell average; no filter bar (implicit LES) |
| $\tau_{ij}=\mu_l(\partial_ju_i+\partial_iu_j-\tfrac23\partial_ku_k\delta_{ij})$ | $\sigma_{ij}$ | **collision:** viscous stress, not the SGS stress $\tau_{ij}$ |
| $\mu_l$, $Pr=0.72$, $\gamma=1.4$ | $\mu$, $Pr$, $\gamma$ | Sutherland law |
| $r$ | $r$ (page-local) | reconstruction degree; the registry's $N$ is kept for element methods; **collision** with the exponent $r_k$ |
| $h_0$, $h_c$ | $h$ | cell size (printed as the square root of the volume) |
| $\lambda_s$, $\lambda_1$, $\lambda'_1$ ($A=2$, $B=1000$) | $d_s$, $d_1$, $d'_1$ (page-local) | linear weights; **collision** with the Taylor microscale $\lambda$ |
| $\tilde\omega_s$, $\omega_s$ | $a_s$, $\mathsf w_s$ (registry §11) | **collision** with the vorticity and with the quadrature weights $\omega_\alpha$ (registry $w_i$) |
| $\mathcal{SI}_s$, $\mathcal{OI}_{kq}$ | $\mathrm{IS}_s$ (registry §11), $\mathcal{OI}_{kq}$ (page-local) | |
| $\tau$, $\epsilon=h_c^4$, $b=4$ | $\tau_{\mathrm U}$ (registry §11), $\epsilon$, $b$ | global smoothness indicator; **collision:** $\tau$ is not a stress |
| $ER$, $LT$, $UT$ | $E_{\mathrm R}$, $\mathrm{LT}$, $\mathrm{UT}$ (page-local) | |
| $\sigma(\eta)$, $\sigma_k$ | $\hat G(\vartheta^{\mathrm t}_m)$ | modal filter transfer function |
| $\eta$, $\eta_c$, $\eta_{max}$ | $\vartheta^{\mathrm t}_m$, $\vartheta^{\mathrm t}_c$, $\vartheta^{\mathrm t}_{\max}$ (registry §11) | total Taylor degree; **collision** with the Kolmogorov length $\eta$ |
| $a$, $s$ (exponential filter) | $\alpha_f$, $s_f$ (registry §11) | strength and order |
| $d_i$ | $c^{\mathrm F}_i$ (page-local) | flux-dissipation multiplier of the whole dissipation term of Eq. (38) (not the $c_{\mathrm{diss}}$ of registry §11) |
| $C$ | $C_{\mathsf w}$ (page-local) | reset threshold on $\mathsf w_1$ |
| $\lambda_{max}$ | $\Lambda_{\max}$ (page-local) | Rusanov wave speed |
| $z$, $M_L$, $M_R$ | $z_{\mathrm{LM}}$ (page-local), $M_L$, $M_R$ | low-Mach correction |
| $\alpha=4/3$, $L_{int}$ | (page-local) | viscous penalty and centre distance; **collision** with the DG blending $\alpha$ and the angle of attack |
| $E_K$, $\varepsilon_t$, $\varepsilon_s$, $\varepsilon_d$ | $E_k$, $\varepsilon_t$ (page-local), $\varepsilon_s$, $\varepsilon_d$ (registry §11) | normalized kinetic energy; total, solenoidal, dilatational dissipation |
| $\omega$ (in $\varepsilon_s$) | $\omega_i$ | vorticity |
| $M_{ref}$, $Re$ | $M$, $Re$ | vortex: unit length; airfoil: chord ($Re_c$); cylinder: diameter ($Re_D$) |
| $t_c$ | (page-local) | convective time $c/U_\infty$ or $D/U_\infty$ |
| $C_L$, $C_D$, $C_P$, $C_f$, $x_s$, $x_r$ | $C_L$, $C_D$, $C_p$, $C_f$, $x_s$, $x_r$ (page-local) | |
| $y^+$, $x^+$, $z^+$ | $y_1^+$, $\Delta x^+$, $\Delta z^+$ | first-cell sizes in wall units |

# Reference list

116 printed references, numbered style ([1]–[116]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. [114] is the ingested [Chapelier et al. (2024)](/sources/chapelier-2024.md),
[15] the ingested [Deng et al. (2022)](/sources/deng-2022.md), [86]
[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md), [27]
[Ma et al. (2022)](/sources/ma-2022.md), and [101] the ingested review
[Maltsev et al. (2022)](/sources/maltsev-2022.md). Three cited works share
a key with a different ingested work and are keyed `maltsev-2022-b`, `cao-2022-c` and `huang-2022-c` respectively: ref.
[61] (Maltsev, Tsoutsanis & Skote, hybrid finite-volume/DG framework,
ECCOMAS 2022), ref. [16] (Cao, Zhao & Chen, quantitative analysis of
implicit LES, Phys. Fluids 34) and ref. [30] (Huang et al., wall models in
spectral/hp implicit LES, Phys. Fluids 34). Several Elsevier references
print a volume without an article number; ref. [85] (Dzanic et al.) is an
arXiv preprint; ref. [81] is printed "AIAA paper 6 (1991-1596)"; ref.
[64] carries a 2019 DOI with a 2023 volume. No item is unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [SD7003 airfoil](/benchmarks/sd7003-airfoil.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Bottleneck effect in the energy spectrum](/definitions/bottleneck-effect.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Eigensolution (dispersion–dissipation) analysis](/methods/eigensolution-analysis.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [PyFR](/software/pyfr.md)
