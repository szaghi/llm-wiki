---
type: Source
title: "Wang et al. (2021) — IDDES method based on differential Reynolds-stress model and its application in bluff body turbulent flows"
description: "IDDES built on the SSG/LRR-ω Reynolds-stress model through the turbulent kinetic energy dissipation, with a general construction of DES for length-scale-equation models and a theoretical DES constant, calibrated on decaying isotropic turbulence and compared with SST-IDDES on tandem cylinders and a transonic launch-vehicle buffet."
resource: "doi:10.1016/j.ast.2021.107207"
source_kind: paper
authors: [Wang G., Li Q., Liu Y.]
year: 2021
venue: "Aerosp. Sci. Technol. 119:107207"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Aerospace_Science_and_Technology_Wang_IDDES_method_based_on_differential_Reynolds-stress_model_and.pdf"
tags: [des, reynolds-stress-model, hybrid-rans-les, numerical-dissipation, bluff-body]
timestamp: 2026-10-29T07:41:00Z
---

# Summary

Wang et al. (2021) build an improved delayed
[detached-eddy simulation](/methods/detached-eddy-simulation.md) (IDDES) on
the SSG/LRR-$\omega$ [differential Reynolds-stress model](/methods/reynolds-stress-model.md)
of DLR, called RSM-IDDES, in the unstructured finite-volume solver HUNS3D.
The first contribution is a general construction of DES-type
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) methods for any RANS model
with a length-scale equation. The RANS–LES switch acts only in the
dissipation of turbulent kinetic energy. Under equilibrium the LES branch
reduces to the [Smagorinsky model](/methods/smagorinsky-model.md), which
gives the model length scale proportional to the grid scale and a
closed-form DES constant from $C_s$ and the coefficients of the
length-scale equation. For the two branches of the
[SST](/methods/k-omega-sst-model.md) the estimate is 0.805 and 0.630,
against the calibrated 0.78 and 0.61. The RSM branches, which share the BSL
$\omega$ equation, get the same values. In the RSM the isotropic dissipation
tensor carries the IDDES length scale of Shur et al. (2008), and the
modelled Reynolds stress acts as the subgrid stress in the LES region, with
no [Boussinesq](/definitions/boussinesq-hypothesis.md) closure there.

The constant is calibrated on decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
(Comte-Bellot–Corrsin, $64^3$) with the adaptive-dissipation Roe scheme
used in the applications. The result, 0.3 (SSG) and 0.5 (LRR), lies well
below theory, which the authors attribute to
[numerical dissipation](/properties/numerical-dissipation.md). RSM-IDDES and
SST-IDDES are compared on the ATAAC tandem cylinders
([circular-cylinder wake](/benchmarks/circular-cylinder-wake.md),
$Re_D=1.6\times10^5$) and on the transonic buffet of the NASA Model 11
hammerhead launch vehicle ($M=0.81$), a flow likened to an axisymmetric
[backward-facing step](/benchmarks/backward-facing-step.md). RSM-IDDES gives
an earlier Kelvin–Helmholtz instability, smaller subgrid stresses, finer
resolved structures, a better position of the $C_p$ fluctuation peak, and a
shedding frequency of 176 Hz against 172 Hz (SST-IDDES) and 179–180 Hz
(experiment). IDDES is chosen because it avoids grid-induced separation and
[log-layer mismatch](/definitions/log-layer-mismatch.md) "to a certain
extent". [PANS](/methods/partially-averaged-navier-stokes.md), PITM and ZDES
are named as other hybrid strategies.

# Version read

Version of record (Elsevier typeset, Aerosp. Sci. Technol. 119 (2021)
107207; received 8 July 2021, online 12 November 2021), 13 pages, all read,
with pp. 3–6 and 12 read visually because the equations of §2.2–2.4 and
Appendix A are garbled in the text layer. Page 1 agrees with Crossref.

# Key claims

1. A general construction of DES-type methods for models with a turbulent length-scale equation modifies only the dissipation of turbulent kinetic energy (Eq. 16): $\varepsilon=k^{3/2}/(C_{\mathrm{DES}}\Delta)$ in the LES region and $k^{3/2}/l_{\mathrm{RANS}}$ in the RANS region; this "ensures that the original model is returned in the RANS region and the Smagorinsky subgrid-scale stress model is obtained under the assumption of equilibrium turbulence in the LES region" (§2.3). **Derived**
2. Under equilibrium the model length scale is proportional to the grid scale, $\ell=[C_{\phi1}/(C_{\ell\varepsilon}C_{\phi2})]^{-1/4}C_s\Delta$ (Eqs. 13–14, §2.3). **Derived**
3. Theoretical DES constant $C_{\mathrm{DES}}=C_s[C_{\phi1}/(C_{\ell\varepsilon}C_{\phi2})]^{3/4}$, depending only on the coefficients of the length-scale equation and $C_s$ (Eq. 16, §2.3). **Derived**
4. SST-based DES: $C_{\mathrm{DES},k\text{-}\omega}=0.805$ ($C_s=0.18$, $C_{\phi1}=0.55$, $C_{\phi2}=0.83$) and $C_{\mathrm{DES},k\text{-}\varepsilon}=0.630$ ($C_{\phi1}=0.44$, $C_{\phi2}=0.92$), "with calibration values of 0.78 and 0.61, respectively" (§2.3). **Derived**. Eq. 16 with $C_{\ell\varepsilon}=0.09$ reproduces 0.805 and 0.630 *(compiler check, not in the sources)*.
5. SSG/LRR-$\omega$ DES has the same estimates, $C_{\mathrm{DES,SSG}}=0.630$ and $C_{\mathrm{DES,LRR}}=0.805$, "since the theoretical estimation of $C_{DES}$ is only related to some coefficients in the length-scale equation and Smagorinsky coefficient $C_S$" (§2.3). **Derived**
6. Because $C_{\mathrm{DES}}$ sets the effective Smagorinsky coefficient of the LES region, a dynamic $C_{\mathrm{DES}}$ yields a dynamic Smagorinsky model there (§2.3, citing He et al. [42]). **Stated**
7. In computation $C_{\mathrm{DES}}$ departs from the theoretical value because of numerical dissipation; the theoretical value "only provides a reference", and calibration on a basic flow such as decaying isotropic turbulence is needed (§2.3). **Stated**
8. With the adaptive-dissipation Roe scheme, $C_{\mathrm{DES,SSG}}=0.3$ and $C_{\mathrm{DES,LRR}}=0.5$ match the Comte-Bellot–Corrsin spectra at $t^*=2.0$; larger values (SSG 0.4, 0.5, 0.61; LRR 0.65, 0.78) "yield too much dissipation in the small turbulent scales" (§3.1, Fig. 1). **Shown**
9. From $C_s\approx C_\Delta^{-1}(1.5C_K)^{-3/4}$ [45] and Eq. 16, $C_{\mathrm{DES}}$ should be lowered when the inertial-range level is below experiment, and raised otherwise (§3.1). **Stated**
10. With the plain Roe scheme at dissipation factor 0.05, the same $C_{\mathrm{DES,LRR}}=0.5$, $C_{\mathrm{DES,SSG}}=0.3$ "show better performance at the high-wavenumber" (App. B, Fig. B1). **Shown**
11. Tandem cylinders: mean $C_p$ on both cylinders is "almost identical" between RSM-IDDES and SST-IDDES and agrees with experiment (§3.2, Fig. 4). **Shown**
12. Tandem cylinders: SST-IDDES slightly over-predicts the $C_p$ RMS peaks on the downstream cylinder (vortex impingement at 45° and 315°); RSM-IDDES agrees better, including separation near 110° and 250° (§3.2, Fig. 5). **Shown**
13. Tandem cylinders: SST-IDDES delays the shear-layer instability; RSM-IDDES gives a shorter shear layer and more small-scale structures, as in the PIV (§3.2, Fig. 6). **Shown**
14. Tandem cylinders, primary shedding frequency (Table 1): SST-IDDES 172 Hz, RSM-IDDES 176 Hz, experiment 179 Hz (A) and 180 Hz (B); SPL at A 115.6, 114.3, 116.5 dB and at B 137.6, 136.8, 138.6 dB; the text says the fluctuation level is "captured well by both DDES within 1.8% error margin" (§3.2). **Shown**
15. Hammerhead: the shear-layer instability of RSM-IDDES starts earlier and the vortices after breakdown are smaller (§3.3, Fig. 9a). **Shown**
16. Hammerhead: all subgrid-stress components of RSM-IDDES are smaller than those of SST-IDDES in the shear-layer and breakdown regions; after Spalart [31], smaller subgrid stress unlocks the Kelvin–Helmholtz instability faster (§3.3, Figs. 10, 13). **Shown** (mechanism **Stated**)
17. Hammerhead: both models match the mean $C_p$; RSM-IDDES is closer in the recirculation $0.35<x<0.65$ behind the boat tail (§3.3, Fig. 11a). **Shown**
18. Hammerhead: the experimental $C_p$ RMS peak, estimated at $x=0.58$, is matched in position by RSM-IDDES, while SST-IDDES places it near $x=0.62$; both over-predict its magnitude, RSM-IDDES less (§3.3, Figs. 11b, 12b). **Shown**
19. Hammerhead: the mean shear layer of RSM-IDDES is shorter, reaches the wall earlier and forms a smaller separation bubble (§3.3, Figs. 12–13). **Shown**
20. Both models resolve more than 80% of the turbulent kinetic energy along the extraction line, taken as meeting the DES resolution requirement [58] (§3.3, Fig. 14b). **Shown**
21. Velocity-fluctuation spectra are broadband; RSM-IDDES has larger amplitude in the separation bubble at middle and high frequency, with few differences outside it (§3.3, Fig. 15). **Shown**
22. Spatial spectra: the low-wavenumber content is nearly identical; RSM-IDDES has more energy at medium and high wavenumbers and a wider $k^{-5/3}$ range (§3.3, Fig. 16). **Shown**
23. RSM-IDDES captures the anisotropy-driven processes of the separated flow "because the exact production terms" of the RSM (§4). **Stated**
24. IDDES is chosen because it avoids grid-induced separation and log-layer mismatch "to a certain extent" (§1, §2.4). **Stated**

The construction, translated. With $\phi_\ell=C_\mu^{-1}k^m\varepsilon^n$ the
length-scale variable ($\omega$: $m=-1$, $n=1$; $\varepsilon$: $m=0$, $n=1$),
$\ell=C_\ell k^{m/n+3/2}\phi_\ell^{-1/n}$, and homogeneous-turbulence forms of
the $k$ and $\varepsilon$ equations, the $\phi_\ell$ equation reads
$D\phi_\ell/Dt=C_{\phi1}(\phi_\ell/k)\nu_t|S|^2-C_{\phi2}(\phi_\ell/k)\varepsilon$
(Eq. 12). Equilibrium with $\nu_t=\sqrt k\,\ell$ and $\varepsilon=C_{\ell\varepsilon}k^{3/2}/\ell$
gives $\nu_t=\sqrt{C_{\phi1}/(C_{\ell\varepsilon}C_{\phi2})}\,\ell^2|S|$ (Eq.
13); matching $\nu_t=(C_s\Delta)^2|S|$ gives
$$\varepsilon=\begin{cases}\dfrac{k^{3/2}}{C_{\mathrm{DES}}\Delta},\quad C_{\mathrm{DES}}=C_s\Big[\dfrac{C_{\phi1}}{C_{\ell\varepsilon}C_{\phi2}}\Big]^{3/4} & \text{LES region},\\ \dfrac{k^{3/2}}{l_{\mathrm{RANS}}},\quad l_{\mathrm{RANS}}=\dfrac{\sqrt k}{C_\mu\omega} & \text{RANS region (SST, RSM)},\end{cases}$$
with $C_{\mathrm{DES}}=F_1C_{\mathrm{DES,LRR}}+(1-F_1)C_{\mathrm{DES,SSG}}$ (Eqs. 16–18).
In the RSM the dissipation tensor becomes $\tfrac23\bar\rho k^{3/2}/l_{\mathrm{IDDES}}\,\delta_{ij}$
with $k=\tfrac12R_{ii}$, $l_{\mathrm{IDDES}}=\hat f_d(1+f_e)l_{\mathrm{RANS}}+(1-\hat f_d)C_{\mathrm{DES}}\Delta$
and $\Delta=\min[\max(C_wd,C_w\Delta_{\max},d_{wn}),\Delta_{\max}]$, $C_w=0.15$ (Eq. 20).

# Printed slips

- Eq. (18): the subscript is printed "$C_{DES,k-\varpi}$" for $k$-$\omega$.
- §2.2: "Here the hat represents the Favre average", while the printed symbol is a tilde.
- §3.2: "captured well by both DDES within 1.8% error margin": both methods are IDDES, and the RSM-IDDES SPL at A in Table 1 (114.3 against 116.5 dB) differs by 1.89% *(compiler check, not in the sources)*.
- §3.2: "Compared with experimental data (180 Hz)", while Table 1 gives 179 Hz at A and 180 Hz at B.
- $\phi$ denotes both the length-scale variable (§2.3) and the dissipation factor of the adaptive Roe scheme (App. A–B).
- Typos: "faring boat tail", "Ames research centers" (§3.3).
- Ref. [17] prints "Jee SolKeun, Karim Shariff", given name and surname inverted, and the text cites "Solkeun [17]".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\rho\tilde R_{ij}=\overline{\rho u_i''u_j''}$ | $\langle\rho u_i''u_j''\rangle=\bar\rho R_{ij}$ | positive convention; the overbar is a Reynolds average here |
| $\tilde U_i$, $\tilde{(\cdot)}$ | $\langle u_i\rangle_\rho$, Favre average | **collision:** the source's tilde is a Favre (Reynolds) average, not a Favre filter |
| $R^{SGS}_{ij}=2\bar\rho\upsilon_t\tilde S_{ij}-\tfrac23\bar\rho\tilde k\delta_{ij}$ | $-\bar\rho\tau_{ij}$ | **collision:** negative convention |
| $\tilde k$ | $k$ (RANS) or $k_{\mathrm{sgs}}$ (LES region) | $\tfrac12R_{ii}$ |
| $\upsilon_t$, $\upsilon$ | $\nu_t$, $\nu$ | |
| $\tilde S_{ij}$, $\lvert\tilde S_{ij}\rvert$ | $S_{ij}$, $\lvert S\rvert$ | the source's modulus carries the factor two |
| $\tilde W_{ij}$, $\Omega$ (App. A) | $\Omega_{ij}$, $\lvert\Omega\rvert$ | |
| $P_{ij}$, $\Pi_{ij}$, $\varepsilon_{ij}$, $D_{ij}$, $M_{ij}$ | (Reynolds-stress budget terms, page-local) | only $P_{ij}$ and $\varepsilon_{ij}$ printed |
| $\phi$ (§2.3) | $\phi_\ell$ (page-local) | **collision** with the source's own adaptive-dissipation factor |
| $\ell$, $C_\ell$, $C_{\ell\varepsilon}$, $C_{\phi1}$, $C_{\phi2}$, $m$, $n$ | same (page-local) | |
| $C_S$ | $C_s$ | 0.18 |
| $C_{DES}$, $l_{RANS}$, $l_{LES}$, $l_{IDDES}$, $\tilde f_d$, $f_e$, $C_w$, $\Delta_{\max}$, $d_{wn}$ | $C_{\mathrm{DES}}$, $l_{\mathrm{RANS}}$, $l_{\mathrm{LES}}$, $l_{\mathrm{IDDES}}$, $\hat f_d$, $f_e$, $C_w$, $\Delta_{\max}$, $d_{wn}$ | as on the [DES](/methods/detached-eddy-simulation.md) page (the tilde is not a Favre filter) |
| $d$ | $d$ | wall distance |
| $F_1$ | $F_1$ | blends LRR (near wall) and SSG |
| $C_K$, $C_\Delta$ | (Kolmogorov constant, filter-ratio constant, page-local) | |
| $\phi$, $\phi_{\max}$, $CH1$–$CH3$, $L_{turb}$, $K$, $g$, $B$, $\tau$ (App. A) | (adaptive Roe scheme parameters, page-local) | **collision:** $B$, $K$, $\tau$ |
| $Q=\tfrac12(\Omega_{ij}\Omega_{ij}-S_{ij}S_{ij})$ | $Q$-criterion | |
| $C_{p,avg}$, $C_{p,rms}$ | $C_p$, (rms of $C_p$) | |
| $Ma$, $Re_D$, $Re$ | $M$, $Re_D$, $Re$ | hammerhead $Re$ on the 12-in booster diameter |
| $\kappa$ (Fig. 16) | $k$ (wavenumber) | **collision** with the von Kármán constant |

# Reference list

58 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. No printed
duplicates. [17] (Jee & Shariff 2014) prints given name and surname
inverted; [19] and [20] (Aerosp. Sci. Technol.) print no volume; [37]
(Harten & Hyman) prints year 1982 with a DOI string containing "(83)"; [51]
is the ATAAC web page without author or year; [58] is Pope's *Turbulent
Flows* with pages 558–561.

# Pages created or updated

Chunk 7 (2026-10-26), cited further in chunk 11. This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Hammerhead launch-vehicle buffet](/benchmarks/hammerhead-launch-vehicle-buffet.md)
- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
