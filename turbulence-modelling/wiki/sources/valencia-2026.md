---
type: Source
title: "Valencia et al. (2026) — A priori assessment of deconvolution-based models for large eddy simulation sub-filter scale turbulent stress tensors in compressible homogeneous isotropic turbulence"
description: "A priori comparison, in explicitly filtered LES of decaying compressible isotropic turbulence, of four deconvolution closures (ADM, D3M, DIAD, DDM) against dynamic Smagorinsky and dynamic mixed models, using filtered and downsampled DNS on LES-like grids; the filter-to-grid ratio decides deconvolution accuracy."
resource: "doi:10.1063/5.0321479"
source_kind: paper
authors: [Valencia S., Córdova J., Mendiburu A.Z., Bravo L., Khare P., Celis C.]
year: 2026
venue: "Phys. Fluids 38:055101"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Physics_of_Fluids_Valencia_iA_priorii_assessment_of_deconvolution-b.pdf"
tags: [les, sgs-model, scale-similarity, filtering, a-priori-a-posteriori, compressible]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Valencia et al. (2026) test, a priori, four deconvolution closures of the
sub-filter stress of compressible [LES](/definitions/large-eddy-simulation.md),
the structural family of the
[scale-similarity and mixed models](/methods/scale-similarity-model.md):
the approximate deconvolution model (ADM, a van Cittert series whose
zeroth order is scale similarity), the discrete direct deconvolution model
(D3M, a truncated Taylor inverse of the Gaussian filter on a 3-, 5- or
7-point stencil), the dynamic iterative approximate deconvolution model
(DIAD, least-squares local stencil weights, iterated) and the spectral
direct deconvolution model (DDM, exact inversion of the Gaussian transfer
function with a limiter). The baselines are the dynamic
[Smagorinsky](/methods/smagorinsky-model.md) model, with its coefficient
from the [Germano identity](/methods/dynamic-procedure.md), and the
dynamic mixed model. All are cast in the explicitly filtered LES framework
of Radhakrishnan & Bellan, in which a known filter of width $\Delta$
larger than the grid spacing $h$ is applied to the equations.

The reference is a [DNS](/definitions/direct-numerical-simulation.md) of
decaying compressible [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
on $512^3$ with the finite-volume code PeleC (seventh-order
[WENO-Z](/methods/weno-scheme.md) inside PPM), initial $M_t=0.6$ and
$Re_\lambda=100$. The [a priori](/definitions/a-priori-and-a-posteriori-testing.md)
protocol is called "stringent": the DNS is top-hat filtered to emulate the
implicit grid filter, downsampled to $128^3$, $64^3$ or $32^3$, then
Gaussian filtered with $\Delta/h=1,2,4$, the three retained cases sharing
the same $\Delta$. The target is the total unresolved stress, which
includes a grid-truncation part no deconvolution can recover. At
$\Delta/h=1$ the spectrum overlaps the [implicit LES](/definitions/implicit-les.md)
one and ADM fails. At $\Delta/h=2$ all deconvolution models reach
correlations of about 0.97–0.985, at $\Delta/h=4$ above 0.994; DDM is the
best and DIAD the least accurate, the dynamic Smagorinsky model stays
below 0.3 and the dynamic mixed model near 0.91. The structural
[gradient model](/methods/gradient-model.md), the functional
[WALE](/methods/wale-model.md) model and
[neural-network](/methods/neural-network-sgs-model.md) extensions of
deconvolution appear only in the introduction.

# Version read

Version of record (AIP typeset, Phys. Fluids 38, 055101 (2026), CC BY 4.0;
submitted 7 January 2026, published online 1 May 2026); 31 PDF pages (an
AIP cover sheet and journal pp. 055101-1 to -30), all read, with the
equation pages checked visually. Page 1 agrees with Crossref.

# Key claims

1. In explicitly filtered LES the total unresolved stress splits exactly as $\tau^{\mathrm{tot}}_{ij}=\tau^{\mathrm{gr}}_{ij}+\tau^{\mathrm{sf}}_{ij}$ (grid truncation plus explicit filtering), assuming the explicit filter commutes with the grid projection; deconvolution recovers only $\tau^{\mathrm{sf}}_{ij}$, and $\tau^{\mathrm{gr}}_{ij}$ "can be neglected only when its magnitude is significantly smaller" (§II C, Eqs. 23–29). **Derived**
2. The explicitly filtered equations, with $\tau^{\mathrm{ef}}_{ij}=\overline{\rho u_iu_j}-\overline{\bar\rho\tilde u_i\tilde u_j}$ and the analogous heat flux, differ from conventional LES only in the filtered resolved product; substitution recovers the classical filtered equations (§II C, Eqs. 17–22). **Derived**
3. For pressure, viscous stress and heat conduction $\overline{f(\phi)}$ is replaced by $f(\bar\phi)$, the error being "negligible" (§II B). **Stated**
4. The Gaussian filter, $\hat G(k)=\exp(-k^2\Delta^2/24)$, is chosen for smoothness, isotropy, positive definiteness and analytic invertibility; with enough scale separation ($\Delta/h\approx4$) different invertible filters give similar trends (§III, Eqs. 30, 48). **Stated**
5. ADM of order 0 is the scale-similarity model; order 5 "typically provides a relatively high accuracy so it has been widely adopted in previous studies" (§III A). **Stated**
6. The second-order discrete inverse Gaussian filter is $\phi^*_j=-\frac{1}{24}\alpha^2(\bar\phi_{j+1}+\bar\phi_{j-1})+\frac{1}{12}(12+\alpha^2)\bar\phi_j$ with $\alpha=\Delta/h$; Table II gives the fourth- and sixth-order stencils (§III B, Eq. 42). **Derived**
7. The resolved kinetic energy after top-hat filtering and downsampling falls with the filter width: 99.7% ($256^3$), 98.7% ($128^3$), 95% ($64^3$), 83.6% ($32^3$), 59.1% ($16^3$) (Table III). **Shown**
8. On a given grid the grid-truncation energy hardly depends on $\Delta/h$ (1.3% on $128^3$, 5.0–5.3% on $64^3$, 16.4–17.0% on $32^3$), while the sub-filter energy grows with it; for $\Delta/h=1$ it is below the grid-truncation energy, for $\Delta/h\ge2$ above (Table IV). **Shown**
9. The three retained cases lose 15–20% of the kinetic energy: $\Delta/h=4$ ($128^3$) about 17%, 92% of it sub-filter; $\Delta/h=2$ ($64^3$) about 19%, 72% sub-filter; $\Delta/h=1$ ($32^3$) a comparable fraction, about 3.5% sub-filter (§V B, Table IV). **Shown**
10. Explicit filtering does not move the grid cutoff $k_c\approx\pi/h$, it only damps energy below it; the $\Delta/h=1$ spectra essentially overlap the implicit-LES spectrum (Fig. 3). **Shown**
11. ADM: at $\Delta/h=1$, correlation below 0.15 and relative error above 0.98 at order 5 (case excluded); at $\Delta/h=2$ about 0.98 and 0.25; at $\Delta/h=4$ above 0.99 and below 0.1; gains saturate beyond order 5 (§V B 1, Figs. 5–6). **Shown**
12. ADM probability density functions at order 0 are much narrower than the reference; at order 5 and $\Delta/h=4$ they collapse onto it including the tails; at $\Delta/h=2$ a low-wavenumber deficit in the stress spectra remains, attributed to grid truncation (Figs. 7–8). **Shown**
13. D3M improves monotonically with order (2, 4, 6); at $\Delta/h=4$ the correlation exceeds 0.995 and the error falls below 0.10 by order 4; order 4 is chosen as the accuracy–cost compromise (§V B 2, Figs. 9–10). **Shown**
14. D3M is more sensitive to $\Delta/h$ than ADM, a larger ratio "improves the conditioning of the inversion" (§V B 2). **Stated**
15. DIAD converges in about two iterations; stencil size 3 against 5 matters little; the chosen setting is a 5-point stencil, filter-to-stencil ratio 2, two iterations (§V B 3, Figs. 13–16). **Shown**
16. DDM: at $\Delta/h=2$ correlations 0.9809 ($\tau_{xx}$), 0.9849 ($\tau_{xy}$) and relative errors 0.2402, 0.1881; at $\Delta/h=4$ 0.9989, 0.9992, 0.0626, 0.0457 (§V B 4, Table V). **Shown**
17. DDM is a practical upper bound of reconstruction accuracy for periodic compressible isotropic turbulence with Gaussian filtering, unusable on non-periodic or non-uniform grids because it needs FFTs (§III D, §V B 4, §VI). **Stated** (bound supported by Tables VI–VII)
18. At $\Delta/h=2$ (Table VI; $C_{xx}$, $C_{xy}$, $E_{xx}$, $E_{xy}$): ADM 0.9795, 0.9839, 0.2469, 0.1946; D3M 0.9792, 0.9838, 0.2445, 0.1931; DIAD 0.9735, 0.9800, 0.2649, 0.2153; DDM as in claim 16; dynamic Smagorinsky 0.2726, 0.1369, 1.2955, 1.0203; dynamic mixed 0.9057, 0.9144, 0.4923, 0.4543. **Shown**
19. At $\Delta/h=4$ (Table VII): ADM 0.9968, 0.9976, 0.0909, 0.0755; D3M 0.9972, 0.9980, 0.0897, 0.0712; DIAD 0.9946, 0.9964, 0.1023, 0.0892; DDM as in claim 16; dynamic Smagorinsky 0.2562, 0.1156, 1.9644, 1.0459; dynamic mixed 0.9126, 0.9089, 0.4386, 0.4483. **Shown**
20. The dynamic Smagorinsky model gives narrower $\tau_{xy}$ and shifted $\tau_{xx}$ distributions, wrong spectra at all scales and over-smoothed or "excessively coherent, biased" fields; the dynamic mixed model improves but underestimates tails and spectral content (§V C, Figs. 20–23). **Shown**
21. The two baselines are only weakly sensitive to $\Delta/h$, read as a structural limitation of eddy-viscosity formulations; the deconvolution models improve strongly from 2 to 4 (§V C). **Shown**
22. Cost, from cited a posteriori works and not measured here: D3M and DDM about 20% of ADM, ADM about half of the dynamic mixed model, DIAD the most demanding deconvolution model (§V C). **Stated**
23. This is the first joint comparison of the recent deconvolution models at LES-like rather than DNS resolution (§I). **Stated**
24. Classical a priori tests on the DNS grid "tend to overestimate model accuracy because the filtered and resolved fields share the same grid resolution" (§I). **Stated**
25. Accurate sub-filter reconstruction in explicitly filtered LES "demands closures capable of compensating for the filtering operation, a requirement fulfilled exclusively by deconvolution-based approaches" (§VI). **Stated** (a priori evidence only)
26. Limitations: isotropic turbulence only; wall-bounded, shocked and reacting flows, a posteriori stability and non-uniform grids are future work; post-processing times are no cost estimate (§V C, §VI). **Stated**

The closures, translated ($\phi^*$ the deconvolved field, $G$ the
Gaussian filter operator):
$$\phi^*=\sum_{n=0}^{N_{\mathrm{AD}}}(I-G)^n\bar\phi\ \ (\text{ADM}),\qquad \hat\phi^*(k)=\min\Big[e^{k^2\Delta^2/24},\,\varepsilon_{\mathrm{DD}}^{-1}\Big]\,\hat{\bar\phi}(k),\ \varepsilon_{\mathrm{DD}}=0.01\ \ (\text{DDM}),$$
with the model stress $\overline{\rho^*u^*_iu^*_j}-\overline{\bar\rho^*\tilde u^*_i\tilde u^*_j}$
(Eq. 33) built from $\rho^*$ and $u^*_i=(\bar\rho\tilde u_i)^*/\rho^*$
(Eq. 32). The $\min$ in the DDM limiter is the text's reading of Eq. (50).
The metrics are the correlation coefficient and the relative error
$\langle(\tau^{\mathrm{ref}}-\tau^{\mathrm m})^2\rangle^{1/2}/\langle(\tau^{\mathrm{ref}})^2\rangle^{1/2}$
over the domain (Eqs. 53–54).

# Printed slips

- Table II, sixth-order D3M: the centre coefficient is printed $\frac{5\alpha^6+168\alpha^4-2352\alpha^2+20736}{20736}$; with $-2352\alpha^2$ the stencil weights sum to $1-94080\alpha^2/414720\neq1$, with $+2352\alpha^2$ exactly to 1 *(compiler check, not in the sources)*. Order 4 is the one used, so the results are unaffected.
- Eq. (8): $q_j=\frac{c_p\mu}{Pr}\frac{\partial T}{\partial x_j}$ without the minus sign of Fourier's law, while Eq. (3) carries $-\partial q_j/\partial x_j$.
- Eq. (50): the regularized inverse is printed as the set $\{[\exp(-k^2\Delta^2/24)]^{-1},\varepsilon^{-1}\}$ without the "min" the text implies.
- Eq. (39): "$1+(1-G)+(1-G)^2++(1-G)^3\dots$" (doubled plus).
- Table IV: the last column is headed "$E^{SFS}_k/E^{SGS}_k$ [%]" but holds plain ratios (0.06 to 11.56).
- §V B 3: DIAD "surpassing $C\approx0.995$ for FGR = 4", while Table VII gives $C_{xx}=0.9946$ (§V C says "exceed 0.994").
- §V C: deconvolution models reduce the relative error from $\Delta/h=2$ to 4 "by nearly half", while Tables VI–VII show reductions by factors of about 2.4–4.1 (e.g. ADM $E_{xx}$ 0.2469 to 0.0909, a factor 2.7) *(compiler check, not in the sources)*.
- §V C: classical models show "only marginal improvement" from $\Delta/h=2$ to 4, while the dynamic Smagorinsky $E_{xx}$ worsens (1.2955 to 1.9644) and its $C_{xx}$ drops (0.2726 to 0.2562).
- §III D attributes the DDM limiter to "the original formulation proposed for the DDM approach, 29", but ref. 29 is the D3M preprint of Chang et al. (2024).
- §V A: "from 99.7% at $\Delta/\Delta_{DNS}=2\%$"; Abstract: "ratios re considered"; §V B 1: "AMD orders"; Table II caption: "for D3M2".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\Delta$ | $\Delta$ | explicit (Gaussian) filter width |
| $\Delta$, $\Delta_{LES}$ | $h$ | LES grid spacing (and top-hat width) |
| $\Delta_{DNS}$ | (DNS grid spacing, page-local) | $2\pi/512$ |
| FGR, $\alpha$ | $\Delta/h$ | filter-to-grid ratio |
| $\bar f$, $\tilde f$ | $\bar\phi$, $\tilde\phi$ | filter (implicit or explicit) and Favre filter |
| $(\cdot)^L$, $u^S_i$ | (grid projection, sub-grid part; page-local) | |
| $G$, $\hat G(k)$ | $G$, $\hat G(k)$ | Gaussian kernel and transfer function |
| $\tau_{ij}=\overline{\rho u_iu_j}-\bar\rho\tilde u_i\tilde u_j$ | $\tau_{ij}$ (compressible form) | positive trace, full tensor |
| $\tau^{ef}_{ij}$ | $\tau^{\mathrm{ef}}_{ij}$ (page-local) | explicitly filtered sub-filter stress |
| $\tau^{Total}$, $\tau^{SGS}$, $\tau^{SFS}$ | $\tau^{\mathrm{tot}}$, $\tau^{\mathrm{gr}}$, $\tau^{\mathrm{sf}}$ (page-local) | **collision:** the source's "SGS" is the grid-truncation part only |
| $\xi_j$, $\xi^{ef}_j$ | (sub-filter heat flux, page-local) | **collision:** not quadrature nodes |
| $\sigma_{ij}$, $S_{ij}$ | $\sigma_{ij}$, $S_{ij}$ | |
| $\phi^*$, $D$, $AD^N$, $DD$ | $\phi^*$ and deconvolution operators (page-local) | |
| $N$ (ADM order; also $\bar\Delta=N\Delta$) | $N_{\mathrm{AD}}$; $\Delta/h$ | **collision:** not the polynomial degree |
| $N_s$, $R=\bar\Delta/\Delta_s$, $W$, $N_i$, $\lambda$ | ($N_{\mathrm{st}}$, the DIAD stencil size; filter-to-stencil ratio, weights, iteration, multiplier; page-local) | **collision:** $R$ is not $R_{ij}$; $\lambda$ not the Taylor microscale |
| $\varepsilon$ | $\varepsilon_{\mathrm{DD}}$ (DDM limiter; also the DIAD tolerance) | **collision:** not the dissipation rate |
| $C$, $E_{rel}$, $\beta$ | (correlation coefficient, relative error, regression slope; page-local) | **collision:** $\beta$ is not the field-inversion multiplier |
| $M_{t,0}$, $Re_{\psi,0}$, $\psi_0=2/k_0$ | $M_t$, $Re_\lambda$, $\lambda$ | initial values; $\psi_0$ plays the Taylor microscale |
| $\tau=\psi_0/u_{rms,0}$ | $T_E$ | **collision:** a time, not a stress |
| $E^{fDNS}_k$, $E^{SGS}_k$, $E^{SFS}_k$ | (resolved, grid-truncation, sub-filter kinetic energy; page-local) | |
| $E(k)$, $k_c$ | $E(k)$, $k_c$ | |

# Reference list

54 printed references, numbered AIP style with titles. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Preprints are kept as their own entries: ref. 29 (Chang et al.,
arXiv 2024), ref. 44 (Córdova et al., arXiv 2023) and ref. 47 (Motheau &
Wakefield, arXiv, dated 2020), the last being the preprint of ref. 51 (same
title), kept distinct. Ref. 37 prints "T. Poinsot, Denis Veynante:
Theoretical and Numerical Combustion"; ref. 17 is a technical report.
Ref. 32 is [Volpiani (2024)](/sources/volpiani-2024.md) and ref. 14
[Qi et al. (2022)](/sources/qi-2022-b.md); refs. 6 and 31 are the
bundle-planned works keyed zhang-2022-f and zhang-2022-h.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [WALE model](/methods/wale-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
