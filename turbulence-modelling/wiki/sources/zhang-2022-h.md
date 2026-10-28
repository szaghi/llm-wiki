---
type: Source
title: "Zhang et al. (2022d) — Dynamic iterative approximate deconvolution model for large-eddy simulation of dense gas compressible turbulence"
description: "Applies the dynamic iterative approximate deconvolution (DIAD) model to LES of decaying compressible isotropic turbulence of a dense gas (PP11, Martin–Hou equation of state), closing the real-gas subgrid pressure, pressure work and internal-energy terms in scale-similarity form; DIAD beats dynamic Smagorinsky a priori and a posteriori, and the thermodynamic terms matter little."
resource: "doi:10.1063/5.0128776"
source_kind: paper
authors: [Zhang C., Yuan Z., Duan L., Wang Y., Wang J.]
year: 2022
venue: "Phys. Fluids 34:125103"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Zhang_Dynamic_iterative_approximate_deconvolution_model_for_large-.pdf"
tags: [les, compressible, sgs-model, approximate-deconvolution, real-gas, a-priori-a-posteriori]
timestamp: 2026-10-28T07:06:00Z
---

# Summary

Zhang et al. (2022d) apply the dynamic iterative approximate deconvolution
(DIAD) model of Yuan et al. (2021) to [large-eddy simulation](/definitions/large-eddy-simulation.md)
of decaying compressible [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
of a dense gas, the perfluorocarbon PP11 near its critical point, at
initial $M_t=0.4$ and 0.8. A dense gas has a fundamental derivative of gas
dynamics below one and needs the Martin–Hou equation of state and the Chung
transport model; because pressure and internal energy are nonlinear in
$(\rho,T)$, the Favre-filtered equations carry, besides the subgrid stress
and turbulent diffusion, a subgrid pressure, a subgrid
density–temperature correlation of the internal energy, a subgrid pressure
work and a subgrid internal-energy flux (after Giauque et al. 2021).

DIAD reconstructs approximately unfiltered density, velocity and
temperature as a weighted sum over a local stencil, with domain-wide
weights from a constrained least-squares fit, iterated twice; every
subgrid term, including those built on the equation of state, is then
evaluated in [scale-similarity](/methods/scale-similarity-model.md) form.
The baseline is the [dynamic Smagorinsky](/methods/dynamic-procedure.md)
model with a dynamic isotropic part, which drops the thermodynamic terms; a
variant DIAD_W also drops them. With $512^3$ DNS (hybrid compact and
[WENO](/methods/weno-scheme.md) scheme), a Gaussian filter of width
$16h_{\mathrm{DNS}}$ and LES on $64^3$, DIAD correlates
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) above 0.98
with the filtered-DNS terms (the internal-energy flux at $M_t=0.4$ above
0.96). A posteriori DIAD and DIAD_W reproduce the kinetic-energy decay,
spectra and the PDFs of the subgrid energy flux, including its
[backscatter](/definitions/energy-backscatter.md) tail, of the deviatoric
stress, strain rate and vorticity, while the
[Smagorinsky](/methods/smagorinsky-model.md) baseline is over-dissipative.
The thermodynamic subgrid terms have little effect on velocity and
thermodynamic spectra in these cases. The DNS
dissipation used for normalization includes the
[pressure-dilatation](/definitions/pressure-dilatation.md) term. [Implicit LES](/definitions/implicit-les.md)
of dense gases is cited in the introduction only.

# Version read

Version of record (AIP; submitted 30 September 2022, accepted 7 November
2022, published online 1 December 2022), 25 PDF pages (an AIP cover page
and article pages 125103-1 to 125103-24), all read; equation pages read
visually because text extraction garbles the formulas. Page 1 matches the
metadata. No identity problem. Numbering on this page is that of this
version.

# Key claims

Page-local symbols: $\Gamma_{\mathrm{fd}}$ the fundamental derivative of gas
dynamics; $p_{\mathrm{MH}}(\rho,T)$, $e_{\mathrm{MH}}(\rho,T)$ the
Martin–Hou pressure and internal energy (the source's $MH_P$, $MH_E$);
$\check p=p_{\mathrm{MH}}(\bar\rho,\tilde T)$ and $\check e=e_{\mathrm{MH}}(\bar\rho,\tilde T)$
(the source's $\hat p$, $\hat E_{int}$, not test-filtered quantities);
$\Phi_{\mathrm{sgs}}=\bar p-\check p$ the subgrid pressure;
$\Xi_{\mathrm{sgs}}=\overline{\rho e}-\bar\rho\check e$ the subgrid
density–temperature correlation; $\mathcal P_j=\overline{pu_j}-\check p\tilde u_j$
the subgrid pressure work; $\Psi_j=\bar\rho(\widetilde{eu_j}-\check e\tilde u_j)$
the subgrid internal-energy flux; $J_j=\tfrac12\bar\rho(\widetilde{u_iu_iu_j}-\tilde u_i\tilde u_i\tilde u_j)$
the subgrid turbulent diffusion; $(\cdot)^\star$ a DIAD-deconvolved field;
$N_i$ the DIAD iteration count; $h_{\mathrm{DNS}}$, $h_{\mathrm{LES}}=\Delta/2$
the grid spacings; $C(\cdot)$, $E_r(\cdot)$ the a priori correlation
coefficient and relative error (Eqs. 37–38). $\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$
is the registry's compressible subgrid stress.

1. For a dense gas $\Gamma_{\mathrm{fd}}<1$ ($>1$ for an ideal gas); BZT gases have a region of negative $\Gamma_{\mathrm{fd}}$ near the liquid–vapour coexistence curve, with expansion shocks, mixed shock–fan waves and shock splitting (§I, Eq. 1). **Stated**
2. The unclosed terms of the Favre-filtered dense-gas equations are $\Phi_{\mathrm{sgs}}$, $\tau_{ij}$, $\Xi_{\mathrm{sgs}}$, $\mathcal P_j$, $\Psi_j$ and $J_j$ (Eqs. 18–23); the nonlinearities of the viscous, heat-flux and viscous-work terms are negligible and dropped, following ref. 6 (§II). **Stated**
3. Few LES studies of non-ideal gases exist, and many data-driven models, limited by the ideal-gas assumption, do not treat thermodynamic unclosed terms; DIAD is "independent of DNS data, very accurate and flexible, and suitable for complex SGS terms" (§I). **Stated**
4. In LES of compressible ideal gases (ref. 95, [Zhang et al. 2022b](/sources/zhang-2022-f.md)) DIAD was more accurate than the dynamic Smagorinsky, dynamic mixed, gradient and approximate deconvolution models a priori and a posteriori (§I). **Stated**
5. A $512^3$ DNS with $k_{\max}\eta\ge2.0$ gives converged statistics at all scales; Table III gives $k_{\max}\eta=3.09$ ($M_t=0.4$) and 3.26 ($M_t=0.8$) (§III A, citing refs. 97, 104). **Stated**
6. The Gaussian filter of width $\Delta=16h_{\mathrm{DNS}}$, $\Delta/\eta\approx16$, "covers the inertial range"; LES on $64^3$ with $h_{\mathrm{LES}}=\Delta/2$ (§III B, Eq. 24). **Stated**
7. DIAD settings: $N_i=2$, stencil size $N_{\mathrm{st}}=3$ with $\Delta/h=2$ (§III B). **Stated**
8. The scale-similarity form of DIAD (Eq. 27), e.g. $\Phi_{\mathrm{sgs}}=\overline{p_{\mathrm{MH}}(\rho^\star,T^\star)}-p_{\mathrm{MH}}(\bar\rho^\star,\tilde T^\star)$, is preferred to the direct form (Eq. 26) because it "is considered to satisfy the symmetry and feasibility conditions and can guarantee the physical reliability of the SGS model" (§III B, refs. 27, 94). **Stated**
9. A priori at $\Delta=16h_{\mathrm{DNS}}$: except $\Psi_1$ at $M_t=0.4$, the correlation coefficients of $\tau_{11}$, $\tau_{12}$, $\Phi_{\mathrm{sgs}}$, $\mathcal P_1$ (and $\Psi_1$ at $M_t=0.8$) exceed 0.98 with relative errors below 0.2; for $\Psi_1$ at $M_t=0.4$ the correlation exceeds 0.96 and the relative error is below 0.3 (§IV A, Figs. 1–2). **Shown**
10. A priori, as the turbulence decays, the DIAD correlation coefficients increase and the relative errors decrease (§IV A, Figs. 1–2). **Shown**
11. Root-mean-square values, $M_t=0.4$/0.8: in the energy equation $\partial_j\mathcal P_j$ 2.357/4.112, $\partial_j\Psi_j$ 0.0835/0.382, $\partial_jJ_j$ 7.582/5.563 (Table IV); in the momentum equation $\partial_j\tau_{1j}$ 1.657/1.434, $\partial_1\Phi_{\mathrm{sgs}}$ 0.101/0.386 (Table V) (§IV A). **Shown**
12. The thermodynamic subgrid terms grow markedly with $M_t$; $\Phi_{\mathrm{sgs}}$ and $\Psi_j$ are an order of magnitude smaller than the other unclosed terms of their equations; compressibility affects the relative magnitude of $\partial_j\tau_{1j}$ and $\partial_1\Phi_{\mathrm{sgs}}$ less (§IV A). **Shown**
13. Cost per time step on 32 cores (Xeon Gold 6140), $M_t=0.4$/0.8: dynamic Smagorinsky 0.241/0.245 s, DIAD_W 0.274/0.282 s, DIAD 0.339/0.334 s; DIAD_W and the dynamic model "similar", DIAD "lightly larger" (Table VI, §IV B). **Shown**
14. A posteriori, the DIAD PDF of $\mathcal P_1$ agrees with filtered DNS at $t/T_E=0.56$, 1.12, 2.24 for both $M_t$ (Fig. 3). **Shown**
15. The PDF of $\Psi_1$ is very close to filtered DNS for both $M_t$, with a longer tail at $M_t=0.8$ (Fig. 4). **Shown**
16. The PDF of $\Phi_{\mathrm{sgs}}$ is well reconstructed at $M_t=0.4$; at 0.8 DIAD underestimates its negative tail (Fig. 5). **Shown**
17. Kinetic-energy decay: DIAD is closest to filtered DNS, DIAD_W very close (the thermodynamic terms barely affect it), the dynamic Smagorinsky model too high after $t/T_E\approx1$ (Fig. 6). **Shown**
18. Velocity spectra: DIAD and DIAD_W agree with filtered DNS; the dynamic Smagorinsky model underestimates the high wavenumbers "because of its high dissipation"; including the thermodynamic terms or not matters little; $k_c=\pi/\Delta=16$ (Fig. 7). **Shown**
19. Subgrid energy flux normalized by the DNS dissipation: the dynamic Smagorinsky model underestimates it (narrower PDFs), DIAD and DIAD_W predict the PDFs accurately; the negative (backscatter) tail is longer at $M_t=0.8$, i.e. more local inverse transfer under strong compressibility (Fig. 8). **Shown**
20. Deviatoric stress PDFs ($\tau^d_{11}$, $\tau^d_{12}$): the dynamic Smagorinsky model is markedly narrower than filtered DNS, DIAD accurate (Figs. 9–10). **Shown**
21. Normalized strain-rate PDFs: the dynamic Smagorinsky tails are clearly too low, DIAD and DIAD_W almost overlap filtered DNS; normalized vorticity PDFs: the dynamic Smagorinsky model underestimates the tails, DIAD is better at both $M_t$ (Figs. 11–13). **Shown**
22. Vorticity contours at $t/T_E=2.24$: DIAD and DIAD_W capture more small-scale structures; the dynamic Smagorinsky model lacks small vortices through excessive dissipation (Figs. 14–15). **Shown**
23. Temperature, density and pressure spectra: DIAD and DIAD_W very similar; the temperature spectrum grows markedly with $M_t$; DIAD deviates slightly at small scales at $M_t=0.4$ and agrees at 0.8; the dynamic Smagorinsky model is clearly too low at small scales (Figs. 16–18). **Shown**
24. Correlations between $\tau_{11}$ and the thermodynamic subgrid terms are near zero except $C(\Phi_{\mathrm{sgs}},\tau_{11})$, "nearly 0.5" initially at $M_t=0.4$ and "gradually increase from around 0.2" at $M_t=0.8$ (Fig. 19; see Printed slips). **Shown**
25. The derivatives of $\mathcal P_j$, $J_j$ and $\tau_{1j}$ dominate, those of $\Phi_{\mathrm{sgs}}$ and $\Psi_j$ are relatively small; the thermodynamic subgrid terms have little influence on the velocity field and neglecting them has little effect "in the present study" (§V). **Shown**

The baseline (Eqs. 33–36) closes $\tau^d_{ij}$ with
$-2C_s^2\Delta^2\lvert\tilde S\rvert\tilde S^d_{ij}$, the trace with
$\tau_{kk}=2C_I\Delta^2\lvert\tilde S\rvert^2$ and
$J_j\approx\tfrac12\tilde u_j\tau_{kk}+\tilde u_i\tau_{ij}$, $C_s^2$ and
$C_I$ by domain-averaged least squares with a test filter
$\hat\Delta=2\Delta$; the source does not define $\lvert\tilde S\rvert$.
The DIAD stencil weights solve a constrained least-squares system with
$\sum W_{l,m,n}=1$ (Eq. 25, Algorithm 1), the same construction as in
[Zhang et al. (2022b)](/sources/zhang-2022-f.md).

# Printed slips

- **After Eq. (9):** "$u^{rms}=\sqrt{\langle u_1^2+u_3^2+u_3^2\rangle}$" ($u_3$ twice, no $u_2$).
- **Eq. (10):** $\lambda=\sqrt{u^{rms}/\langle(\partial u_1/\partial x_1)^2+(\partial u_2/\partial x_2)^2+(\partial u_3/\partial x_3)^2\rangle}$. The numerator is a velocity and the denominator an inverse time squared, so the right side is not a length *(compiler check, not in the sources)*.
- **Eqs. (33)–(34) against Eq. (36):** the model forms carry no $\bar\rho$ ("$-2C_s^2\Delta^2|\tilde S|(\ldots)$", "$\tau_{kk}=2C_I\Delta^2|\tilde S|^2$"), while $\tau_{ij}$ (Eq. 19) and the dynamic-procedure terms $\alpha_{ij}=-2\Delta^2\bar\rho|\tilde S|(\ldots)$, $\alpha=2\bar\rho\Delta^2|\tilde S|^2$ (Eq. 36) carry it.
- **Eq. (30):** $P_j=\overline{MH_P(\rho^*,T^*)u_j^*}-MH_P(\bar\rho^*,\tilde T^*)\tilde u_i^*$, free index $j$ on the left and $i$ in the last term (Eq. 21 has $\hat p\tilde u_j$).
- **Subgrid energy flux, §IV B:** $\Pi=\tau_{ij}\tilde S_{ij}$ is printed with "positive value ($\Pi>0$) indicates the forward energy transfer". With the paper's own Eq. (33) and $C_s^2>0$, the deviatoric contribution $\tau^d_{ij}\tilde S^d_{ij}=-2C_s^2\Delta^2\lvert\tilde S\rvert\tilde S^d_{ij}\tilde S^d_{ij}\le0$, so under the printed definition the deviatoric part of the baseline's $\Pi$ is non-positive *(compiler check, not in the sources)*.
- **Table III** labels the integral length column "$L_f$", the symbol §II uses for the reference length (the integral scale is $L_I$, Eq. 11).
- **Abstract against §IV A:** the abstract excepts "the SGS internal energy flux" from the 0.98/0.2 bounds, §IV A only $\Psi_1$ at $M_t=0.4$.
- **Fig. 19 text:** at $M_t=0.4$, $C(\Phi,\tau_{11})$ "is nearly 0.5 in the initial stage … and then increases as the turbulence decays (gradually approaching 0)".
- **References:** ref. 4 prints "S. B. Pope and S. B. Pope"; ref. 1 prints "B. Halpern" as the author of *Large Eddy Simulation of Complex Engineering and Geophysical Flows* (as in [Zhang et al. 2022b](/sources/zhang-2022-f.md), ref. 44).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f$, $\tilde f=\overline{\rho f}/\bar\rho$ | $\bar f$, $\tilde f$ | |
| $\hat f$ (DSM) | $\hat f$, $\hat\Delta=2\Delta$ | test filter |
| $\hat p$, $\hat E_{int}$, $\hat\sigma_{ij}$, $\hat\mu$, $\hat\kappa$ | $\check p$, $\check e$, … (page-local) | **collision:** functions of $(\bar\rho,\tilde T)$, not test-filtered |
| $MH_P$, $MH_E$ | $p_{\mathrm{MH}}$, $e_{\mathrm{MH}}$ (page-local) | Martin–Hou equation of state |
| $E_{int}$ | $e$ (internal energy per unit volume, page-local) | **collision:** the registry's $E$ is the total energy |
| $\rho^*$, $u_i^*$, $T^*$ | $\rho^\star$, $u_i^\star$, $T^\star$ | **collision** with the semi-local $(\cdot)^*$ of the registry |
| $\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$ | $\tau_{ij}$ | positive trace |
| $\tau^A_{ij}$ | $\tau^d_{ij}$ | deviatoric part |
| $\Phi$, $\Xi$, $P_j$, $\Psi_j$, $J_j$ | $\Phi_{\mathrm{sgs}}$, $\Xi_{\mathrm{sgs}}$, $\mathcal P_j$, $\Psi_j$, $J_j$ (page-local) | **collision** within the source: $\Psi$ is also the generic DIAD variable |
| $\Pi=\tau_{ij}\tilde S_{ij}$ | $-\Pi$ by formula | **sign:** the registry writes $\Pi=-\tau_{ij}\bar S_{ij}$; the source states $\Pi>0$ is forward transfer |
| $\epsilon^{DNS}=\langle-p\theta\rangle+\langle\sigma_{ij}S_{ij}/Re\rangle$ | $\varepsilon$ with the pressure-dilatation part | $\theta$ is the velocity divergence (**collision** with the momentum thickness) |
| $C_s^2$, $C_I$ | $C_s^2$, $C_I$ | |
| $\mathscr L_{ij}$, $\mathscr M_{ij}$, $\alpha_{ij}$, $\beta_{ij}$ | $L_{ij}$ (density-weighted), $M_{ij}$ (page-local), … | dynamic procedure |
| $N_s$, $R=\Delta/\Delta_s$, $N_i$, $W_{l,m,n}$ | $N_{\mathrm{st}}$, $\Delta/h$, $N_i$, $W_{l,m,n}$ | **collision:** $R$ is also the gas constant |
| $\Delta_{DNS}$, $h_{LES}$ | $h_{\mathrm{DNS}}$, $h_{\mathrm{LES}}$ | |
| $\Gamma$ | $\Gamma_{\mathrm{fd}}$ (page-local) | |
| $M_t=u^{rms}/\langle c\rangle$ | $M_t$ | $u^{rms}$ the three-component rms |
| $Re_\lambda$, $\lambda$, $\eta$, $L_I$ | $Re_\lambda$, $\lambda$, $\eta$, $L$ | $\lambda$ as printed in Eq. (10) |
| $\tau=L_I/u^{rms}$ | $T_E$ | **collision** with $\tau_{ij}$ |
| $\alpha=PrE_cM$ | (page-local) | **collision** with the DSM $\alpha$, $\alpha_{ij}$ |
| $\varepsilon$ (DIAD error bound) | (page-local) | **collision** with the dissipation rate |
| fDNS | filtered DNS | |

# Reference list

114 printed references, numbered (AIP) style. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Ref. 95
is the ingested [zhang-2022-f](/sources/zhang-2022-f.md), ref. 23 the
ingested [wang-2022-j](/sources/wang-2022-j.md), ref. 51 the ingested
[duraisamy-2019](/sources/duraisamy-2019.md). Ref. 93 (Li, Pei & Bai 2022,
Phys. Fluids 34:085104) and ref. 49 (Prakash, Jansen & Evans 2022,
Comput. Methods Appl. Mech. Eng. 399:115457) are different works from the
ingested [li-2022](/sources/li-2022.md) and
[prakash-2022](/sources/prakash-2022.md) and are keyed `li-2022-l` and `prakash-2022-c`. Ref. 94
(Yuan et al. 2021, the DIAD paper) is the second Yuan 2021 work in printed
order. Four AIAA papers (refs. 19, 20, 38, 86) are recorded with their
paper numbers. Ref. 4 (Pope) prints the author twice. No item is
unparseable.

# Pages created or updated

Chunk 11 (2026-10-27), cited further in chunk 14. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Compact finite-difference schemes](/methods/compact-finite-difference-scheme.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
