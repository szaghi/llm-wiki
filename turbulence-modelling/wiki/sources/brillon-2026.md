---
type: Source
title: "Brillon & Nadarajah (2026) — Large eddy simulation using nonlinearly stable flux reconstruction"
description: "Assessment of split-form, provably entropy-stable nonlinearly stable flux reconstruction (NSFR) for DNS, implicit LES and eddy-viscosity LES of the Taylor–Green vortex and Comte-Bellot–Corrsin decaying turbulence: stable without upwinding or over-integration, about half the cost of over-integrated DG, SGS models not recommended."
resource: "doi:10.1016/j.compfluid.2026.107232"
source_kind: paper
authors: [Brillon J., Nadarajah S.]
year: 2026
venue: "Comput. Fluids 319:107232"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Computers_amp_Fluids_Brillon_Large_eddy_simulation_using_nonlinearly_stable_flux_reconstr.pdf"
tags: [flux-reconstruction, implicit-les, entropy-stable, numerical-dissipation, sgs-model, high-order]
timestamp: 2026-10-26T20:48:00Z
---

# Summary

Brillon & Nadarajah (2026) assess the nonlinearly stable
[flux reconstruction](/methods/flux-reconstruction.md) (NSFR) schemes of
Cicchino et al., implemented in the open-source PHiLiP code, for
scale-resolving simulation of wall-free turbulence. NSFR writes the convective
volume term in split form with a two-point flux evaluated on entropy-projected
variables, which makes it provably entropy stable without upwind dissipation
and without over-integration. The baseline is the Ismail–Roe
entropy-conserving flux, the correction parameter $c_{DG}$, Gauss–Legendre flux
nodes, SIPG viscous fluxes and SSP-RK3.

A DNS of the viscous [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $Re=1600$, $M=0.1$ with $256^3$ degrees of freedom agrees with the
literature in kinetic energy, dissipation, enstrophy and spectra
([direct numerical simulation](/definitions/direct-numerical-simulation.md)),
but the node-wise pressure dilatation oscillates; collocated nodes and added
Roe dissipation damp the oscillation. Under-resolved runs at $96^3$ to $24^3$
DOF stay stable without added dissipation, cost about half as much as
over-integrated strong DG for $N\in[5,12]$, and reach CFL limits up to 2.6
times larger with the correction parameter $c_+$. The choice among
entropy-conserving, [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
and [pressure-equilibrium-preserving](/properties/pressure-equilibrium-preservation.md)
two-point fluxes makes no visible difference. The paper separates
[implicit LES](/definitions/implicit-les.md) (no model) from "implicitly
filtered LES" with an explicit model; the
[Smagorinsky model](/methods/smagorinsky-model.md), its shear-improved and
high-pass-filtered variants and the [dynamic](/methods/dynamic-procedure.md)
model all lower the peak enstrophy and are "not recommended" with NSFR. The
effective viscosity $Re\,\varepsilon/(2\zeta)$ and the pressure-dilatation
budget serve as measures of [numerical dissipation](/properties/numerical-dissipation.md).
A collocated $N=3$ NSFR run on $128^3$ DOF reproduces the Comte-Bellot–Corrsin
decaying grid-turbulence spectra
([homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md))
with a smaller kinetic-energy error than the finite-difference and
correction-procedure-via-reconstruction computations it is compared with.

# Version read

arXiv preprint arXiv:2411.12108v1 [physics.flu-dyn], 18 November 2024, 59
pages (text pp. 1–52, references pp. 53–57, Appendix A pp. 58–59), all read;
pp. 11–12 (Eqs. 51–61) checked visually. The version of record (Comput.
Fluids, 2026) was not read and can differ in content, numbers and reference
list; the DOI is not printed in the file. Title and authors match Crossref.
Equation, table, figure and section numbers below are those of arXiv v1.

# Key claims

1. NSFR (split form, Ismail–Roe two-point flux) is stable for the DNS of the viscous TGV with no added dissipation, upwinding, over-integration or turbulence model, with both Gauss–Legendre (uncollocated) and Gauss–Lobatto (collocated) flux nodes; kinetic energy and dissipation rate agree with the $512^3$ reference of Dairay et al. (§3.1.1, Fig. 2). **Shown**
2. The schemes with Roe dissipation ($N=3$ NSFR with Roe, $N=3$ strong DG with Roe and over-integration) are more dissipative than the reference for a short period of the decay phase; Roe dissipation lowers the peak enstrophy (§3.1.1, Fig. 2b). **Shown**
3. The "observed" pressure dilatation $-\varepsilon_P=\varepsilon-\varepsilon_v$ (Eq. 105) of the $256^3$, $N=7$ runs lies between the $N=3$ DG result of Chapelier et al. and the $512^3$ DRP result of DeBonis for $t^*\in(7,15)$ and matches DeBonis elsewhere; NSFR is less dissipative than the DG reference, which the authors attribute to the absence of upwinding and over-integration (§3.1.1, Fig. 3a). **Shown**
4. Computing $\varepsilon_P$ from node-wise pressure and velocity divergence over-predicts its magnitude for all schemes; the authors suspect the representation of the velocity divergence (after Bull and Jameson) and confine the issue to on-the-fly post-processing (§3.1.1, Fig. 3b). **Shown** (cause **Stated**)
5. Collocated NSFR has a much smaller $\varepsilon_P$ fluctuation than uncollocated NSFR; lower $N$ gives larger fluctuations; Riemann-solver dissipation damps them, as Flad and Gassner also found (§3.1.1, Figs. 3b, 4a). **Shown**
6. All DNS schemes keep the effective viscosity $\nu_{\mathrm{effective}}\approx Re\,\varepsilon/(2\zeta)$ within 4.5% of the physical viscosity; for $t^*>5$ the collocated $N=7$ scheme is closest to 1 (§3.1.1, Fig. 4b, Eq. 100). The sentence on which scheme exceeds 1 contradicts the paper's own reading of the ratio (see Printed slips). **Shown**
7. Oversampling the polynomial field onto $2(N+1)$ equidistant nodes per element and direction before the FFT removes an apparent pile-up of energy near the cutoff $k_c$, as observed by Carton de Wiart et al. (§3.1.1, Fig. 6; §3.1.2, Fig. 9). **Shown**
8. Integrating the spectrum up to $k_c$ reproduces the kinetic energy at $t^*=9$ with relative errors 0.082685%, 0.236968%, 0.522544% with oversampling against 0.148560%, 1.100619%, 5.026020% without, for $256^3$ ($N=7$), $96^3$ ($N=5$) and $64^3$ ($N=7$) DOF (Table 4, Eqs. 106–107). **Shown**
9. Baseline NSFR is stable on all under-resolved grids ($96^3$ with $N=5$, $64^3$ with $N=7$, $48^3$ and $24^3$ with $N=5$) without added dissipation; at $96^3$ the dissipation rate tracks the DNS up to the peak at $t^*\approx8$; per DOF, $N=7$ captures the enstrophy better than $N=5$ (§3.1.2, Fig. 8). **Shown**
10. Strong DG without over-integration ($N=7$, $64^3$) fails in the transitional phase around $t^*=6$: "a linearly stable scheme can be unstable in the absence of over-integration" (§3.1.3, Fig. 11). **Shown**
11. NSFR reaches a higher peak enstrophy than over-integrated strong DG at all resolutions; at $64^3$ the over-integrated scheme's dissipation rate is slightly more accurate through transition; NSFR shows large pressure-dilatation oscillations that the upwinded strong DG does not; spectra are similar (§3.1.3, Fig. 11). **Shown**
12. CPU time per SSP-RK3 step ($4^3$ elements, 16 MPI processes, 10 repetitions, $N\in[1,12]$) follows the expected scaling for both schemes; for $N\in[5,12]$ over-integrated strong DG costs about twice as much as split-form NSFR (§3.1.3, Fig. 12). **Shown**
13. With $N+1$ quadrature points Gauss–Legendre is exact for degree $2N+1$ and Gauss–Lobatto for $2N-1$; $2(N+1)$ points per direction are needed to integrate the cubic nonlinearity of the viscous flux exactly (§3.1.4). **Stated**
14. At $N=5$, $96^3$ DOF, collocated NSFR departs from the expected dissipation rate near $t^*\approx5$ and its $t^*=9$ spectrum is off for $k^*\in(10,20)$; with three extra quadrature points both node choices agree, and uncollocated NSFR without over-integration already matches them: "with sufficient integration accuracy, the solution is independent of the choice of flux nodes" (§3.1.4, Fig. 13). **Shown**
15. The collocated scheme has much smaller pressure-dilatation fluctuations than the uncollocated and partially over-integrated ones (except near $t^*\approx5$), suggesting that the fluctuations come from interpolating the flux to the face nodes (§3.1.4, Fig. 13c). **Shown** (interpretation **Stated**)
16. The dissipation-rate peaks order as $c_+>c_{HU}>c_{SD}>c_{DG}$ (larger $c$, more dissipation); spectra are similar; no value of $c$ damps the pressure-dilatation oscillations (§3.1.5, Fig. 14). **Shown**
17. CFL limits at $N=5$, $96^3$, with the authors' "physically consistent" criterion (stable and $E_K$ non-increasing): $c_{DG}$ NSFR 0.26, $c_+$ NSFR 0.36, over-integrated strong DG with Roe 0.14, about 1.9 and 2.6 times the strong-DG value, $c_+$ about 38% above $c_{DG}$ (Table 5, §3.1.5). **Shown**
18. Runs at the CFL limits stay very close to CFL 0.10 through transition; "by using $c_+$ we can obtain a solution similar to that of $c_{DG}$ and strong DG at about half the computational cost" (§3.1.5, Fig. 15). **Shown**
19. The two-point flux (Ismail–Roe, entropy conserving; Kennedy–Gruber, kinetic-energy preserving; Chandrashekar, both; Chandrashekar modified by Ranocha, also pressure-equilibrium preserving) gives nearly identical spectra, $E_K$, $\varepsilon$, enstrophy and effective viscosity, with negligible pressure-dilatation differences near $t^*=12.5$, 15, 20; Kennedy–Gruber is cheapest (§3.1.6, Fig. 16). **Shown**
20. Roe or L2Roe face dissipation lowers the peak enstrophy (L2Roe slightly less) and leaves the $t^*=9$ spectrum nearly unchanged; the authors call added Lax–Friedrichs upwinding "anti-dissipative" (peak enstrophy above the projected DNS, more small-scale energy); Lax–Friedrichs and Roe almost remove the pressure-dilatation oscillations (§3.1.7, Fig. 17; §2.9.1). **Shown**
21. Collocated NSFR with upwind dissipation has pressure-dilatation oscillations "drastically smaller" than both the dissipation-free collocated scheme and the uncollocated DNS (§3.1.7, Fig. 18). **Shown**
22. Eddy-viscosity SGS models (Smagorinsky, shear-improved, high-pass-filtered variants, dynamic Smagorinsky, all with a low-Reynolds-number correction) raise the dissipation rate marginally, lower the peak enstrophy, reduce but do not remove the pressure-dilatation oscillations, and dissipate energy at $k^*\in(25,40)$ where the baseline already has a deficit: "the SGS models considered in this work are not recommended for the LES of transitional turbulent free-shear flows using NSFR" (§3.1.8, Fig. 19). **Shown**
23. Collocated strong DG at $N=5$ without over-integration is unstable; a high-pass-filtered shear-improved Smagorinsky model stabilizes it but gives wrong dissipation and spectra, while over-integrated strong DG follows the DNS: "a stable scheme without any de-aliasing can lead to inaccuracies" (§3.1.8, Fig. 20). **Shown**
24. Comte-Bellot–Corrsin decaying turbulence with collocated $N=3$ NSFR on $32^3$ elements ($128^3$ DOF, $96^3$ unique, $k_c=48$), CFL 0.2: spectra at $t^*=1,2$ agree with the experiment; kinetic-energy error at $t^*=2$ is 1.36% ($k_c=48$) and 5.30% (truncated at $k_c=31$) against 29.81% (sixth-order finite differences, $64^3$), 15.55% ($N=5$ CPR, $78^3$) and 29.75% ($N=1$ CPR, $126^3$); the lower errors are "expected to be partially due" to more unique DOF and oversampling (Table 6, Eq. 112). **Shown**
25. To the authors' knowledge this is "the first study on the use of a provably entropy conserving and stable high-order flux reconstruction method for the simulation of viscous turbulent flows" (§1, §3.1). **Stated**
26. Flad and Gassner reported a cost reduction by at least a factor 3 with kinetic-energy-preserving split-form DG in their code, and that L2Roe dissipation attenuates pressure-dilatation oscillations (§1, §2.9.3). **Stated** (cited)

# Printed slips

- Table 2 and the captions of Figs. 5–6 print $k_c=122$ for $N=7$ on $32^3$ elements; Eq. 103 ($k_c=N_{\mathrm{el}}N/2$) gives $32\times7/2=112$, which is also $(\text{unique DOF})^{1/3}/2=224/2$ *(compiler check, not in the sources)*; the other rows of Tables 2–3 follow Eq. 103.
- Table 3 prints $k_{\mathrm{grid}}=4$ for $4^3$ elements; Eq. 104 ($N_{\mathrm{el}}/2$) gives 2 *(compiler check, not in the sources)*.
- Dynamic-model clipping: §2.6.4 clips $C_D\in[0,C_S^2]$ with $C_S=0.10$ (upper bound 0.01), §3.1.8 says it "is clipped at $C_{max}=0.1$"; $C_D$ multiplies $\Delta^2$ (Eq. 53), so the two bounds differ.
- Eq. 54 prints $C_D=-\frac12\langle L_{ij}M_{ij}\rangle_e/\langle M_{ij}M_{ij}\rangle_e$. With $\nu_t=C_D\Delta^2|S|$, the positive-trace stress $\tau^d_{ij}=-2C_D\Delta^2|S|S^d_{ij}$ and the Germano identity, $L^d_{ij}=2C_DM_{ij}$ with $M_{ij}$ as printed in Eq. 56, hence $C_D=+\frac12\langle L_{ij}M_{ij}\rangle/\langle M_{ij}M_{ij}\rangle$ *(compiler check, not in the sources)*.
- Test filter: §2.6.4 calls it "similar to that detailed in Section 2.6.3" (a modal high-pass truncation keeping degrees above $N_f$), while §3.1.8 speaks of "Galerkin projection operations" with test-filter degree 3 and Eq. 58 assigns the wider width $\hat\Delta=\overline V_e^{1/3}/(N_f+1)$ of a low-pass filter.
- p. 6, after Eq. 4: "$T_{ref}$ is the reference viscosity" (a temperature; the next clause names $\mu_{ref}$).
- §3.1.5: "Hyunh's g2 scheme" for Huynh.
- §3.1.1 (pp. 19, 22): "$\nu_{\mathrm{effective}}<1$ … less dissipative than it should be", then "for $t^*>5$ the non-dimensional effective viscosity is greater than 1 at all times except for the p3 uncollocated dissipation free scheme … only this scheme was ever more dissipative than it should be"; by the first definition the exception is the less dissipative scheme.
- §3.2.2: "nearly a quarter of that for the FDS scheme" for $5.30/29.81=0.18$ *(compiler check, not in the sources)*; "fives times less" for "five times".

# Notation map

| Brillon & Nadarajah | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, $p_e$, "p5" | $N$ | polynomial degree; $N_p=(N+1)^3$ |
| $P$ | $p$ | pressure |
| $v_i$ | $u_i$ | velocity |
| $U$, $W$ | (conserved, primitive variables) | **collision:** $W$ is also the quadrature-weight matrix (Eqs. 70–71) |
| $\tau_{ij}$ | $\sigma_{ij}$ | viscous stress |
| $\tau^{sgs}_{ij}=2\rho\nu_t S^d_{ij}$ | $-\bar\rho\,\tau^d_{ij}$ | source stress enters like a viscous stress (negative of the registry convention); resolved fields carry no bar in the source |
| $\sqrt{2S_{ij}S_{ij}}$ | $\lvert S\rvert$ | agrees |
| $C_S=0.10$, $C_D$ | $C_s$, $C_s^2$ (dynamic) | $C_D$ multiplies $\Delta^2$ |
| $\Delta_e=\overline V_e^{1/3}/(p_e+1)$ | $\Delta$ | element volume to the one-third over $N+1$ |
| $\widehat{(\cdot)}$, $\widehat\Delta$, $p^L$, $p_{TF}$ | $\hat\phi$, $\hat\Delta$, $N_f$ | **collision:** the hat is also the high-pass modal filter (§2.6.3) and the Ismail–Roe averaged states (§2.7.1) |
| $\widetilde{(\cdot)}$ | (Roe average; entropy-projected variables) | **collision:** not a Favre filter |
| $\bar S_{ij}=\langle S_{ij}\rangle_e$ | (element-mean strain of the shear-improved model) | **collision:** overbar is an element average, not the LES filter |
| $\langle\cdot\rangle$ | (volume average over the domain) | **collision:** not a Reynolds average |
| $\varepsilon=-dE_K/dt$, $\varepsilon_v$, $\varepsilon_P$, $\varepsilon_\zeta$ | $\varepsilon$ and its viscous, pressure-dilatation and enstrophy-based parts | page-local subscripts |
| $\zeta$ | (enstrophy, $\frac12\langle\rho\omega_k\omega_k\rangle/\langle\rho\rangle$) | |
| $\nu_{\mathrm{effective}}$ | (effective-viscosity ratio $Re\,\varepsilon/(2\zeta)$) | distinct from §11 $\nu_{\mathrm{eff}}$ of a projected stress |
| $\kappa$, $\kappa_c$, $\kappa_{grid}$ | $k$, $k_c$, (grid cutoff $N_{\mathrm{el}}/2$) | **collision:** $\kappa$ is also the thermal conductivity (Eqs. 7–8) |
| $\{\{\cdot\}\}$, $(\cdot)^{\ln}$ | $\{\!\{\phi\}\!\}$, $\phi^{\ln}$ | arithmetic mean agrees; logarithmic mean page-local, written as on [entropy conservation](/properties/entropy-conservation.md) |
| $F^r_{c,m}$ | $f^{\#}$ (matrix of two-point fluxes) | |
| $c_{DG}$, $c_{SD}$, $c_{HU}$, $c_+$ | (ESFR correction parameter values) | |
| GL, GLL | (Gauss–Legendre, Gauss–Lobatto nodes) | |
| iLES, ILES | (implicitly filtered LES with a model, implicit LES without) | **collision:** other sources use "iLES" for implicit LES |
| $Re_\infty$, $M_\infty$ | $Re$, $M$ | TGV with $L=1$ |
| $M$ | (element count, §2.7; grid mesh size, §3.2) | **collision:** not a Mach number |

# Reference list

92 printed references, numbered in order of first citation, no DOIs printed.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Reference [42] (Flad & Gassner 2017) is the ingested
source flad-2017 and [57] (Duan & Wang 2024) the ingested source duan-2024.
Three arXiv preprints ([41], [65], [80]) stay distinct entries. No printed
duplicates; incomplete items: [17] no volume, [33] no pages, [51], [53],
[56], [72] no venue or publisher, [66], [88] no volume, [49] (PHiLiP
software) no URL, [92] a CTR report.

# Pages created or updated

Chunk 7 (2026-10-26), cited further in chunk 10. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
