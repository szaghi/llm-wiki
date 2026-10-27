---
type: Source
title: "Prakash et al. (2022) — Optimal Clipping of Structural Subgrid Stress Closures for Large-Eddy Simulation"
description: "Proposes optimal clipping, the Frobenius-nearest backscatter-free projection of a structural subgrid stress, which yields a parameter-free local mixed model; with Clark's gradient model it keeps the a priori stress correlation lost by standard clipping and improves wall-resolved channel LES at Re_tau 590."
resource: "doi:10.2514/1.j061775"
source_kind: paper
authors: [Prakash A., Jansen K.E., Evans J.A.]
year: 2022
venue: "AIAA J. 60:6897-6909"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_AIAA_Journal_Prakash_Optimal_Clipping_of_Structural_Subgrid_Stress_Closures_for_L.pdf"
tags: [les, sgs-model, eddy-viscosity, a-priori-a-posteriori, energy-cascade]
timestamp: 2026-10-27T16:00:00Z
---

# Summary

Prakash et al. (2022) address a known weakness of structural subgrid-scale
models for [large-eddy simulation](/definitions/large-eddy-simulation.md):
Clark's [gradient model](/methods/gradient-model.md), Bardina's
[scale-similarity model](/methods/scale-similarity-model.md) and approximate
deconvolution correlate well with the exact SGS stress but underpredict the
mean SGS dissipation and produce local model
[backscatter](/definitions/energy-backscatter.md), which can destabilize a
simulation. Standard clipping sets the model stress to zero wherever
$-\tau^M_{ij}\bar S_{ij}<0$; it restores dissipation but lowers the
correlation with the exact stress. Mixed models with a tuned or
[dynamic](/methods/dynamic-procedure.md) coefficient share the drawback.

*Optimal clipping* replaces the model stress by the symmetric tensor nearest
to it in the Frobenius norm among the tensors without local backscatter. The
KKT conditions give a closed form, $\tau^{\mathrm{OC}}_{ij}=\tau^M_{ij}-\lambda\bar S_{ij}$
with $\lambda=\max(\tau^M_{kl}\bar S_{kl}/\bar S_{mn}\bar S_{mn},0)$. This is a
mixed model whose eddy viscosity $\lambda/2$ is evaluated pointwise, with no
test filter, no averaging and no parameter. The authors offer it as a
mathematical justification of the mixed-model form.

[A priori](/definitions/a-priori-and-a-posteriori-testing.md), on
box-filtered DNS of forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at
$Re_\lambda=418$, optimal clipping keeps the correlation of the unclipped
gradient model, while standard clipping loses it, more so for anisotropic
filters. The mean energy flux is the same for both. A posteriori, in the
stabilized finite-element code PHASTA, both clippings remove the
energy pile-up of the unclipped and no-model ([implicit](/definitions/implicit-les.md))
runs in forced isotropic turbulence and are the most accurate in the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$. The
[numerical dissipation](/properties/numerical-dissipation.md) of the
stabilization is stated to be much smaller than the SGS dissipation. In
wall-resolved [channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=590$, optimal clipping clearly beats standard clipping for $C_f$,
mean velocity and shear stress, and comes close to the dynamic mixed model,
which is slightly better but costlier. The authors attribute the gain to
structural accuracy. [Smagorinsky](/methods/smagorinsky-model.md) appears as
the functional baseline, and the cost argument for LES over DNS cites
[grid-point estimates](/results/les-grid-point-requirements.md).

# Version read

arXiv preprint arXiv:2201.09122v2 [physics.flu-dyn], 23 February 2022,
single-column, 25 pages, all read (equations on pp. 5–9 checked visually);
not the AIAA typeset version of record, whose volume and pages cannot be
checked against the file. The arXiv title writes "Large Eddy Simulation"
without the hyphen of the published title; authors and order match. Section,
equation, figure and table numbers on this page are those of the arXiv v2.

# Key claims

1. Structural models (gradient, scale-similarity, ADM) give SGS stresses highly correlated with the exact stress, and model dissipation highly correlated with the exact flux $\Pi$, but underpredict local SGS dissipation, which leads to energy pile-up at high resolved wavenumbers even in isotropic turbulence (§I, §II, citing [8, 9]). **Stated**
2. Eddy-viscosity models assume local alignment of the deviatoric SGS stress with $\bar S_{ij}$; a priori studies show it does not hold and such models have low stress correlation (§II, citing [5, 9]). **Stated**
3. For anisotropic wall-bounded flows at moderate resolution an accurate SGS stress is needed for accurate statistics, whereas for isotropic turbulence accurate dissipation suffices (§I–II, citing Baggett et al. [14]). **Stated**
4. With periodic or homogeneous boundaries and no forcing, $\frac{d}{dt}\int_\Omega\tfrac12\bar u_i\bar u_i\,d\Omega+\int_\Omega(2\nu\bar S_{ij}-\tau_{ij})\bar S_{ij}\,d\Omega=0$, so resolved energy decays iff $\int_\Omega\tau_{ij}\bar S_{ij}\,d\Omega\le\int_\Omega2\nu\bar S_{ij}\bar S_{ij}\,d\Omega$; excessive model backscatter can make it grow (Eqs. 4–6, citing [20]). **Derived**
5. Fixed-coefficient mixed models (Clark plus Smagorinsky, Eq. 7) need a tuned $C_G$: too large is over-dissipative and inaccurate in transition, too small is unstable; the dynamic mixed model addresses this (§II). **Stated**
6. Standard clipping (Eq. 9) raises model dissipation at the cost of the correlation between true and modelled stresses (§II). **Stated** (shown a priori in Figs. 1–3)
7. Optimal clipping (Eqs. 10–11) is the Frobenius-nearest symmetric tensor to $\tau^M$ in $\mathcal S=\{\tilde\tau\in\mathrm{Sym}(3):\tilde\tau_{ij}\bar S_{ij}\le0\}$; if $\tau^M\notin\mathcal S$ the minimizer is unique and solves the linear $7\times7$ KKT system of Eq. 12 (§II). **Derived** (uniqueness asserted, not proved in detail)
8. Closed form: $\lambda=\tau^M_{ij}\bar S_{ij}/(\bar S_{kl}\bar S_{kl})$ (Eq. 13), $\tau^{\mathrm{OC}}_{ij}=\tau^M_{ij}-\lambda\bar S_{ij}$ (Eq. 14), valid in both cases with $\lambda=-\min\{-\tau^M_{ij}\bar S_{ij}/(\bar S_{kl}\bar S_{kl}),0\}$ (Eq. 15). **Derived**
9. The optimally clipped model is a mixed model whose eddy viscosity is half the Lagrange multiplier, exactly what removes the model backscatter; it reverts to the structural model where there is none. This gives "some mathematical justification for the use of mixed SGS models" (§II, after Eq. 15). **Derived**. Where $\lambda>0$, Eqs. 13–14 give $\tau^{\mathrm{OC}}_{ij}\bar S_{ij}=0$, the local model flux that standard clipping also gives, so the two clippings have the same pointwise model flux *(compiler check, not in the sources)*.
10. Optimal clipping needs no additional filtering or homogeneous averaging, unlike a dynamic mixed model, which "significantly reduces the model evaluation cost"; it is parameter-free (Abstract, §II). **Stated** (no timings)
11. Like other mixed formulations [21], optimal clipping keeps the near-wall scaling of the underlying structural model (§II). **Stated**
12. Optimal clipping applies unchanged to Bardina's model, ADM or a data-driven model; the authors tested it with Bardina's model and the data-driven model of [22], with similar trends (§II, §IV). **Stated** (results not shown)
13. A priori, isotropic box filter (JHTDB, $Re_\lambda=418$, $\Delta\approx6.5\eta$–$68\eta$): the unclipped gradient model is highly correlated with the exact stress at all widths but underpredicts the mean flux; standard clipping improves the flux but lowers the correlation; optimal clipping keeps the unclipped correlation and has an SGS dissipation "identical to that of the standard clipped gradient model" (§III.A.1, Fig. 1). **Shown**
14. A priori, book-type filter ($\Delta_1=15\eta$, $\Delta_2=\Delta_3$ up to $292\eta$): the correlation first falls with aspect ratio, then levels off; standard clipping lowers it more than for isotropic filters; optimal clipping keeps it; anisotropy lowers the mean flux of all models, partly through more model backscatter; both clippings dissipate more and degrade less (§III.A.2, Fig. 2). **Shown**
15. A priori, pencil-type filter ($\Delta_1=\Delta_2=15\eta$, $\Delta_3$ up to $292\eta$): the standard-clipping correlation "deteriorates significantly", optimal clipping stays close to the unclipped model, and clipping "dramatically improves" the model dissipation at high aspect ratio; other fine-direction widths behave alike (not shown) (§III.A.2, Fig. 3). **Shown**
16. Forced isotropic turbulence at $\nu=10^{-12}$: the SUPG/PSPG/grad-div numerical dissipation of PHASTA is "significantly smaller" than the SGS dissipation of every explicit model (§III.B.1). **Stated** (from numerical experiments not shown)
17. Forced isotropic turbulence: the no-model and unclipped gradient runs show large pile-up at the highest resolved wavenumbers; dynamic Smagorinsky has none and follows $k^{-5/3}$ but overpredicts intermediate wavenumbers; both clippings give much better spectra, optimal clipping "a slightly longer inertial subrange and less energy pileup"; the dynamic mixed model has no pile-up but overpredicts intermediate wavenumbers (§III.B.1, Fig. 4). **Shown**
18. Taylor–Green vortex, $Re=1600$: all models match the filtered-DNS resolved kinetic energy on $128^3$, and all but the dynamic mixed model on $64^3$, which decays too fast (§III.B.2, Fig. 5). **Shown**
19. Taylor–Green resolved dissipation: dynamic Smagorinsky underpredicts it, the dynamic mixed model more so (significantly even on $128^3$), the unclipped gradient model overpredicts it (especially on $64^3$), and the two clippings are the most accurate (§III.B.2, Fig. 6). **Shown**
20. Taylor–Green spectra at $t=9$: dynamic Smagorinsky and dynamic mixed underpredict high-wavenumber energy; the gradient model without, with standard and with optimal clipping are closest to filtered DNS, optimal slightly better than standard on the coarse mesh (§III.B.2, Fig. 7). **Shown**
21. Channel, $Re_\tau=590$, $C_f$ on coarse/medium meshes (Table 4): DNS 0.0058; dynamic Smagorinsky 0.0047/0.0049; no clipping 0.0063/0.0063; standard clipping 0.0047/0.0050; dynamic mixed 0.0053/0.0055; optimal clipping 0.0051/0.0053 (§III.B.3). **Shown**
22. Channel mean velocity (bulk scaling): dynamic Smagorinsky and standard clipping underpredict near the wall and overpredict in the log region; no clipping overpredicts near the wall; optimal clipping and dynamic mixed are the most accurate, dynamic mixed slightly better on the coarse mesh (§III.B.3, Fig. 8). **Shown**
23. Channel TKE and Reynolds shear stress (resolved plus time-averaged subgrid): no clipping significantly overpredicts the TKE peak on both meshes; the others slightly overpredict it on the coarse mesh and are close to DNS on the finer one; optimal clipping and dynamic mixed give much better shear stress, dynamic mixed slightly better (§III.B.3, Figs. 9–10). **Shown**
24. The small edge of the dynamic mixed model costs explicit filtering and homogeneous averaging at every step; the gain of optimal over standard clipping in channel flow is attributed to structural accuracy, since their a priori model dissipation is the same ("we believe", §III.B.3; "We hypothesize", §IV). **Stated** (hypothesis)
25. In isotropic turbulence and the Taylor–Green vortex the improvement of optimal over standard clipping "was not significant", but for wall-resolved LES of wall-bounded flow it "may yield significantly improved results"; where clipping is needed for stability optimal clipping "should be selected"; clipping may beat the dynamic mixed model in transitional flows (§IV). **Stated**

# Printed slips

- **Eq. 7.** The eddy-viscosity term is printed $-2\nu_tS_{ij}$ with unbarred $S_{ij}$, while $\nu_t$ uses $|\bar{\mathbf S}|$ and the filtered strain is $\bar S_{ij}$ everywhere else.
- **Eq. 8.** The pointwise no-backscatter condition is printed with the exact stress, "$\tau_{ij}\bar S_{ij}\le0$", while the text concerns the model stress $\tau^M_{ij}$.
- **Eq. 17.** $G_{ij}=\partial u_i/\partial x_j$ is printed with the unfiltered velocity; Eq. 16 uses $\bar u_i$.
- **Eqs. 6 and 23.** Integrals printed without $d\Omega$.
- **Eq. 19 and "C.C. = 1".** C.C. is printed as a plain double sum $\sum_i\sum_j$ of per-component correlation coefficients, and called the "mean correlation coefficient", yet "A perfect SGS model has C.C. = 1". Nine unit terms sum to 9, so a normalization (or a mean) is missing from the printed formula *(compiler check, not in the sources)*.
- **Flow-through time (§III.B.3, p. 18).** Printed "$T=\bar u_b/L_x$", the inverse of a time; $L_x/\bar u_b$ is meant *(compiler check, not in the sources)*.
- **Shear stress (§III.B.3).** "the gradient model without clipping also overpredicts the Reynolds shear stress. On the other hand, the dynamic Smagorinsky model and the gradient model without clipping significantly underpredict the Reynolds shear stress": the same model is said to over- and underpredict.
- **Mesh name (§III.B.3, p. 19).** "the fine mesh resolution predictions": the meshes are "coarse" and "medium" (Table 3).
- **Model labels.** Table 4 writes AGM-NC, AGM-SC, AGM-DMM, AGM-OC; the text defines GM-NC, GM-SC, GM-OC, GM-DMM; "AGM" is not defined.
- **Table 3.** $\Delta x^+$ of the coarse mesh is printed 78; $2\pi\cdot590/48=77.2$ *(compiler check, not in the sources)*.
- **Typo.** "Smagorsinsky" (§IV).

# Notation map

| Prakash et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u_i$, $\bar p$, overbar | $\bar u_i$, $\bar p$ | LES filter, incompressible |
| $\bar S_{ij}$ | $\bar S_{ij}$ | |
| $\lvert\bar S\rvert$ | $\lvert\bar S\rvert$ | not defined in the paper; no factor-two convention stated |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | full tensor, positive trace |
| $\tau^M_{ij}$, $\tau^{M,d}_{ij}$ | $\tau^M_{ij}$ (page-local), its deviatoric part | modelled stress |
| $\tau^{M-mixed}_{ij}$, $\tau^{M-SC}_{ij}$, $\tau^{M-OC}_{ij}$ | (mixed, standard-clipped, optimally clipped stress) | written $\tau^{\mathrm{SC}}$, $\tau^{\mathrm{OC}}$ on this page |
| $\tilde\tau_{ij}$ | (trial tensor) | **collision:** not a Favre filter |
| $\mathcal S$ | $\mathcal A$ (backscatter-free set, page-local, as on the [gradient model](/methods/gradient-model.md) page) | printed both $\mathcal S$ and $S$; **collision** with the strain magnitude |
| $\lambda$ | $\lambda_{\mathrm{oc}}$ (Lagrange multiplier, $\nu_t=\lambda_{\mathrm{oc}}/2$, page-local, as on the gradient-model page) | **collision:** not the Taylor microscale |
| $\Pi$, $\Pi^M$ | $\Pi=-\tau_{ij}\bar S_{ij}$, model flux | positive = forward transfer, as in the registry |
| $C_s$, $C_G$ | $C_s$, $C_G$ (page-local) | $C_G$ the mixed-model coefficient, $(C_G\Delta)^2$ computed dynamically |
| $\Delta$, $\Delta_i$ | $\Delta$, (directional widths) | $\Delta=(\Delta_1\Delta_2\Delta_3)^{1/3}$; a posteriori the grid size |
| $G_{ij}$, $A_{ij}$ | $\partial_j\bar u_i$, (filter-width tensor $\mathrm{diag}(\Delta_1,\Delta_2,\Delta_3)$) | |
| C.C., R.E.F. | (stress correlation coefficient, relative error of the mean flux) | Eqs. 19–20 |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | spatial average at one time |
| $\epsilon$, $C$ | $\varepsilon$, (Kolmogorov constant 1.6) | |
| $E_k(t)$, $\epsilon(t)$ | (resolved kinetic energy and dissipation of the TGV) | $\epsilon(t)$ is enstrophy-based |
| $\bar u_b$, $Re_b$ | (bulk velocity), $Re_b=\bar u_b\delta/\nu=10975$ | the bar on $\bar u_b$ is not a filter |
| $C_f=\tau_w/(\tfrac12\rho\bar u_b^2)$ | $C_f$ | bulk-velocity based |

# Reference list

37 printed references in numbered style, all parsed and merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Ref.
[22] (Prakash, Jansen & Evans, arXiv:2106.13410) is printed as a preprint
and keeps its own 2021 entry. Ref. [25] (PHASTA on GitHub) is a corporate
software entry; ref. [34] (Shoraka 2017) a PhD thesis; Bardina et al.
(1980) an AIAA paper. Refs. [27]–[29] print a doubled "https://doi.org/"
prefix, recorded once. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunks 4, 6. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Bottleneck effect in the energy spectrum](/definitions/bottleneck-effect.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
