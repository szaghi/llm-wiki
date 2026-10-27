---
type: Source
title: "Wang et al. (2023c) — Ensemble data assimilation-based mixed subgrid-scale model for large-eddy simulations"
description: "Proposes EnKF-MM, a mixed SGS model of the gradient (Clark) model plus a Smagorinsky term whose single coefficient is calibrated a posteriori by an ensemble Kalman filter against filtered-DNS energy spectra; in forced and decaying isotropic turbulence and a temporal mixing layer it beats the dynamic Smagorinsky, dynamic mixed and pure gradient models."
resource: "doi:10.1063/5.0160482"
source_kind: paper
authors: [Wang Y., Yuan Z., Wang J.]
year: 2023
venue: "Phys. Fluids 35:085107"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Physics_of_Fluids_Wang_Ensemble_data_assimilation-based_mixed_subgrid-scale_model_f.pdf"
tags: [les, sgs-model, data-driven, a-priori-a-posteriori, energy-cascade]
timestamp: 2026-10-27T16:02:00Z
---

# Summary

Wang et al. (2023c) build EnKF-MM, a mixed subgrid-scale model for
incompressible [LES](/definitions/large-eddy-simulation.md). The structural
part is the [gradient (Clark) model](/methods/gradient-model.md),
$\frac{\Delta^2}{12}\partial_k\bar u_i\partial_k\bar u_j$, with its Taylor-expansion
coefficient kept fixed. The dissipative part is a
[Smagorinsky](/methods/smagorinsky-model.md) term with one constant
coefficient. That coefficient is calibrated a posteriori by an
[ensemble Kalman filter](/methods/ensemble-kalman-closure-calibration.md):
an ensemble of LESs, each with its own coefficient, starts from the same
filtered-DNS field. The state of each member is its energy spectra at several
observation instants plus its coefficient, and the observation is the
filtered-DNS spectrum. The Kalman analysis updates the coefficients, and the
loop restarts from the same field. The energy spectrum is the target because
point-to-point matching of a chaotic flow is meaningless. The calibration
runs through the LES itself, a posteriori (see
[model-consistent training](/methods/model-consistent-training.md)).

In forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
at $Re_\lambda\approx160$ ($64^3$ LES, Gaussian filter, filter-to-grid ratio
2) the calibration converges to $C_{\mathrm f}\approx0.00738$, far below the classical
value. In a temporally evolving mixing layer, a shifting step and ensemble
inflation are needed, and the coefficient is $C_{\mathrm f}\approx0.01$. A posteriori,
EnKF-MM is closer to filtered DNS than the
[dynamic](/methods/dynamic-procedure.md) Smagorinsky model, the dynamic mixed
model ([scale-similarity and mixed models](/methods/scale-similarity-model.md))
and the pure gradient model, in spectra, kinetic energy, strain and rotation
PDFs, the [SGS energy flux](/definitions/energy-backscatter.md) and structure
functions. The dynamic models over-dissipate the small scales, while the pure
gradient model under-dissipates and diverges at $Re_\lambda=259$. The best
a priori SGS-stress accuracy, that of the gradient model, does not give the
best a posteriori statistics
([a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

# Version read

arXiv preprint arXiv:2305.11112v3 [physics.flu-dyn], stamped 6 July 2023
("Dated: 7 July 2023"), AIP manuscript template with placeholder lines
("AIP/123-QED", "PACS numbers: Valid PACS appear here"), 42 pages, all read.
The metadata above are those of the published article (Phys. Fluids
35:085107); the DOI is not printed on the preprint. Page 1 title and authors
match the published record. Page, equation and figure numbers on this page
are those of arXiv v3. In the bundle this paper is Wang et al. (2023c).

# Key claims

1. The EnKF-MM model is $\tau_{ij}=\frac{\Delta^2}{12}\partial_k\bar u_i\,\partial_k\bar u_j-C_{\mathrm f}\Delta^2|\bar S|\bar S_{ij}$ (Eq. 14; printed coefficient $C_D$; the term has no factor two, so $C_{\mathrm f}$ corresponds to $2C_s^2$, §III). Only the dissipative coefficient is calibrated; the gradient-model coefficient keeps its original value to retain its a priori SGS accuracy (§II.A). **Stated**; the justification is the authors' earlier adjoint optimization (ref. 88), in which the structural coefficient stayed close to its original value. **Stated**
2. The state vector of each ensemble member has size $n\times k_c+1$: the energy spectra at $n$ observation instants plus the member's coefficient; the observation matrix selects the spectrum entries, so the spectrum is a state variable and no observation operator built from flow variables is needed (§II.B, Eqs. 15–16). **Stated**
3. The observation noise is set at machine-error level, uniform in $(-1,1)\times10^{-7}$, because the observations come from DNS (§III, Tables II, IV). **Stated**
4. Forced isotropic turbulence: with 10 or 20 members, 50 iterations, observation interval 0.3 large-eddy turnover times over 6 turnover times and initial coefficients uniform in $(0,0.05)$, the calibration converges to $C_{\mathrm f}\approx0.00738$; the ensemble spread decreases and saturates (§III, Fig. 2, Table II). **Shown**
5. The calibrated value is much smaller than the classical $2C_s^2\approx0.05$ ($C_s=0.16$), which the authors read as dominance of the structural part (§III; App. C: "no more than 20 percent of its original value"). **Shown** (value) / **Stated** (interpretation)
6. In forced isotropic turbulence the dynamic Smagorinsky and dynamic mixed models slightly overestimate the large-scale energy and underestimate the small-scale energy (strong SGS dissipation); the pure gradient model strongly underestimates the large-scale and overestimates the small-scale energy (insufficient dissipation); EnKF-MM is closest to filtered DNS in spectrum and kinetic-energy evolution (§III, Fig. 3). **Shown**
7. Adding the dissipative part slightly degrades the SGS-stress PDFs relative to the pure gradient model, but EnKF-MM remains better than the dynamic models, whose PDFs are narrower; the dynamic mixed model is better than the dynamic Smagorinsky model (§III, Fig. 4). **Shown**
8. "Accurately reconstructing the SGS stress may not guarantee the adequate prediction of other important flow statistics": the gradient model gives the best SGS-stress PDF and the worst kinetic energy (§III, Figs. 3–4). **Shown**
9. PDFs of $\bar S_{11}$, $\bar S_{12}$, $|\bar S|$, $\bar\Omega_{12}$, $|\bar\Omega|$: the dynamic models give narrower PDFs with overestimated peaks, the gradient model wider PDFs with underestimated peaks; EnKF-MM is best (§III, Figs. 5–7). **Shown**
10. SGS energy flux $\Pi=-\tau_{ij}\bar S_{ij}$: the dynamic Smagorinsky model is strictly positive; the dynamic mixed model gives some backscatter through its similarity part; the gradient model gives a wider PDF than filtered DNS and overestimates backscatter, mostly through its poor prediction of the filtered strain rate; EnKF-MM is most accurate (§III, Eq. 21, Fig. 8). **Shown** (PDFs) / **Stated** (attribution)
11. Longitudinal structure functions of orders 2, 4, 6, 8: all models are accurate at large separations; at small separations the gradient model is too high and the dynamic models too low, increasingly with the order; EnKF-MM is best at all orders but degrades with the order, which the authors say "can be a result of targeting the energy spectrum which is a second-order statistical quantity" (§III, Eq. 22, Fig. 9). **Shown**
12. Mixing layer: a shifting step that moves every member's coefficient by the difference between the best member's and the ensemble-mean coefficient "must be additionally incorporated" for convergence (§IV, Eq. 25). **Stated** (no run without shifting is shown)
13. Mixing layer: without inflation, 20 and 40 members converge while 10 are insufficient; with inflation factor 1.5, 10 members reach the same level, $C_{\mathrm f}\approx0.01$; with inflation the spread saturates higher (§IV, Eq. 26, Fig. 11, Table IV). **Shown**
14. The ensemble Kalman filter, as a statistical minimization, "does not to the same degree suffer from the typical problem of falling into a local minima as in the traditional parameter-estimation methods" (§IV, citing Evensen). **Stated**
15. Mixing-layer momentum thickness: all models give a linear-growth region; the dynamic Smagorinsky model delays transition; the dynamic mixed model captures transition better but drifts later; the gradient model over- then under-predicts; EnKF-MM is best (§IV, Fig. 12). **Shown**
16. Mixing-layer spectra at $t/\tau_\theta=600$ and 800: the gradient model is much worse than in isotropic turbulence, "presumably due to the absence of control by the large-scale forcing"; the dynamic models overestimate the large-scale energy; EnKF-MM is most reasonable (§IV, Fig. 13). **Shown**
17. Mixing-layer kinetic energy: the dynamic models are much higher than filtered DNS in the linear-growth region, the gradient model much lower; EnKF-MM captures the reduced growth rate (§IV, Fig. 14). **Shown**
18. All models predict the mean streamwise velocity reasonably; the gradient model's mean profile is better than the dynamic models' despite a much worse kinetic energy (§IV, Fig. 15). **Shown**
19. Reynolds shear stress (printed $-\langle u_1u_2\rangle$): EnKF-MM is reasonable, the dynamic models tangibly worse, the gradient model strongly underestimates it (§IV, Fig. 16). **Shown**
20. Q-criterion iso-surfaces at $t/\tau_\theta=800$: the dynamic models give larger vortex structures, the gradient model much smaller ones, EnKF-MM is closest to filtered DNS (§IV, Eq. 27, Fig. 17). **Shown** (qualitative)
21. Machine-learning SGS models with excellent a priori accuracy often under-perform or become unstable a posteriori and need hyper-viscosity, regulation of negative SGS flux or additional filtering, which reduces their efficiency (§V). **Stated** (cited)
22. The ensemble Kalman filter is "numerically more convenient" than the adjoint-based variational method; for this one-parameter problem finite differences would also work; the filter is more promising for high-dimensional optimization (§V). **Stated**
23. The gradient model requires a filter with finite moments; Gaussian and top-hat filters share the second moment. EnKF-MM calibrated with Gaussian filtered DNS also outperforms the other models when the initial fields and test filters are top-hat, without recalibration (App. A, Eq. A1, Fig. 18). **Shown**
24. The model calibrated at $Re_\lambda=160$, $\Delta=16h_{\mathrm{DNS}}$, outperforms the other models at $Re_\lambda=259$ with $\Delta=16h_{\mathrm{DNS}}$ and $32h_{\mathrm{DNS}}$; the pure gradient model diverges at $Re_\lambda=259$, $\Delta=16h_{\mathrm{DNS}}$ (App. B, Fig. 19, Table V). **Shown**
25. Decaying isotropic turbulence from $Re_\lambda=259$: EnKF-MM gives the best spectra at 4.8 and 9.6 turnover times and the best kinetic-energy decay (App. B, Figs. 20–21). **Shown**
26. EnKF-FM, the Smagorinsky term alone with a recalibrated coefficient, gives $C_{\mathrm f}=0.01$, "about 36 percent larger" than 0.00738; it reproduces the spectrum reasonably except for a high-wavenumber overestimate, but is tangibly worse than EnKF-MM in the $|\bar S|$ and $|\bar\Omega|$ PDFs and the worst of all models for the SGS energy flux (App. C, Figs. 22–24). **Shown**
27. For significantly different flow configurations EnKF-MM should be recalibrated; for similar configurations with different parameters it applies with acceptable accuracy (§II.B, App. B). **Stated** / **Shown** (isotropic-turbulence variants only)
28. Applying the method to wall-bounded LES needs "further adjustments of EnKF and improvements for computational efficiency" (§VI). **Stated**

# Printed slips

- **Eq. 24 (momentum thickness):** integration limits $-L_2/4$ to $L_2/4$, whereas Eq. 23 defines the initial profile on $0<x_2\le L_2$ with the layer centred at $x_2=L_2/2$; the shift of the integration variable is not stated. $\langle\Delta U\rangle$ carries averaging brackets although $\Delta U$ is a constant.
- **Fig. 15:** panel (a) ordinate $\langle u_3\rangle(y)$, panel (b) $\langle w\rangle(y)$, abscissa "$y$", whereas the text uses $x_2$.
- **Fig. 5 caption:** "forced forced HIT". Typos "subgird" (p. 3), "stablize" (p. 4), "Gaussion" (p. 9, App. A).
- **Abstract:** "The model coefficients are determined through the EnKF", whereas a single coefficient is determined.
- **Ref. 5:** cites [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) as "Annu. Rev. Fluid Mech. 51, 537 (2019)"; the published record of that work gives pages 357–377.
- **Ref. 79:** journal printed "J. Acousti. Sci. Amer."; **Ref. 10:** "pp, 195".

# Notation map

| Wang et al. (2023c) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline f$, $\overline\Delta$ | $\bar f$, $\Delta$ | LES filter (Gaussian; top-hat in App. A) and its width |
| $\widetilde f$, $\widetilde{\overline\Delta}=2\overline\Delta$ | $\hat f$, $\hat\Delta=2\Delta$ | **collision:** the source's tilde is the test filter, not a Favre filter |
| $\tau_{ij}=\overline{u_iu_j}-\overline u_i\overline u_j$ | $\tau_{ij}$ | positive trace; agrees |
| $\tau^A_{ij}$ | $\tau^d_{ij}$ | deviatoric SGS stress |
| $\overline S_{ij}$, $\lvert\overline S\rvert=\sqrt{2\overline S_{ij}\overline S_{ij}}$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | factor two; agrees |
| $\overline\Omega_{ij}$, $\lvert\overline\Omega\rvert$ | $\bar\Omega_{ij}$, $\lvert\bar\Omega\rvert$ | agrees |
| $C_{Smag}$ | $C_s$ | classical 0.16 |
| $C_D$ | $C_{\mathrm f}$ (registry §11, as on [EnKF calibration](/methods/ensemble-kalman-closure-calibration.md)) | **collision:** registry $C_D$ is the drag coefficient; no factor 2 in Eq. 14, so $C_{\mathrm f}=2C_s^2$ |
| $C_{Dmax}$ | upper bound of the initial $C_{\mathrm f}$ | 0.05 |
| $L_{ij}$, $M_{ij}$, $\alpha_{ij}$, $\beta_{ij}$ | $L_{ij}$ (Germano identity), Lilly's $M_{ij}$ | $L_{ij}$ written with the test filter as hat in the registry |
| $C_1$, $C_2$, $h^A_{1,ij}$, $h_{2,ij}$ | (dynamic mixed model coefficients and basis tensors) | |
| $\Pi=-\tau_{ij}\overline S_{ij}$ | $\Pi$ | positive = forward transfer; agrees |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | homogeneous-direction average; agrees |
| $u^{rms}=\sqrt{\langle u_iu_i\rangle}$ | (three-component rms) | **not** a per-component rms; $Re_\lambda=u^{rms}\lambda/(\sqrt3\nu)$ |
| $\lambda$, $\eta$, $\varepsilon$, $Re_\lambda$ | $\lambda$, $\eta$, $\varepsilon$, $Re_\lambda$ | agree |
| $L_I$ | $L$ | integral length scale |
| $\tau=L_I/u^{rms}$ | $T_E$ (large-eddy turnover time, registry §11) | **collision** with $\tau_{ij}$; written in words on this page |
| $E(k)$, $E^{true}(k)$, $k_{max}$ | $E(k)$, filtered-DNS spectrum, $k_c$ | |
| $h_{DNS}$, $h_{LES}$ | $h_{\mathrm{DNS}}$, $h_{\mathrm{LES}}$ | grid spacings; filter-to-grid ratio $\Delta/h_{\mathrm{LES}}=2$ |
| $e_i$, $P$, $K$, $H$, $R$, $q$, $w_i$ | $\boldsymbol e_i$, $\mathsf P$, $\mathsf K$, $\mathsf H$, $\mathsf R$, $\boldsymbol q$, $\boldsymbol w_i$ (page-local on [EnKF calibration](/methods/ensemble-kalman-closure-calibration.md): state, ensemble covariance, Kalman gain, observation matrix, noise covariance, observation, noise) | **collisions:** $K$ (spectral TKE), $w_i$ (quadrature weights), avoided by the sans-serif and bold forms |
| $N$, $N_{iter}$, $n$, $\Delta t_{Obs}$ | $N_e$ (ensemble size, page-local), iterations, observation instants, observation interval | **collision:** $N$ is not the polynomial degree |
| $F$, $\sigma_C$ | (inflation factor, ensemble spread of the coefficient) | |
| $x_1$, $x_2$, $x_3$ (mixing layer) | $z$, $y$, $x$ | spanwise, normal, streamwise in the source |
| $\Delta U$, $\theta$, $\theta_0$, $\tau_\theta=\theta_0/\Delta U$ | (velocity difference, momentum thickness, its initial value), $\tau_\theta$ (time unit, registry §11) | $\theta$ agrees with the registry's momentum thickness |
| $S^L_n$ | (longitudinal structure function of order $n$, normalized by $u^{rms}$) | |

# Reference list

111 printed references, numbered (AIP superscript style), titles printed. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` wang-2023-c. Two cited works are ingested sources:
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md) (ref. 5, page printed
537, see Printed slips) and
[Vadrot et al. (2023a)](/sources/vadrot-2023.md) (ref. 18). Ref. 40 (Li,
Tian & Li 2022, Phys. Fluids 34:065108) shares its first-author-year key with
the ingested [Li & Liu (2022)](/sources/li-2022.md) but is a different work
(`li-2022-g`). Ref. 88 (Yuan et al., arXiv:2301.08423, 2023) is a
preprint entry. Same-author same-year works take suffixes in printed order.
Ref. 33 (Visbal et al., AIAA paper 2003-4098) and ref. 23 (Bardina et al.,
"AIAA paper 80, 1357") are entered as printed. No printed duplicates or
unparseable items.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunk 6. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Temporally developing mixing layer](/benchmarks/temporal-mixing-layer.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Ensemble Kalman filter calibration of turbulence closures](/methods/ensemble-kalman-closure-calibration.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
