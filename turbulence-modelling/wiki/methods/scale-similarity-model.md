---
type: Method
title: "Scale-similarity and mixed subgrid-scale models"
description: "Scale-similarity and deconvolution models build the subgrid stress from the resolved field itself rather than from an eddy viscosity; the sources agree that they reproduce the stress structure and allow stable backscatter but are under-dissipative, hence mixed with a Smagorinsky term."
status: established
aliases: [similarity model, Bardina model, mixed model, structural SGS model, approximate deconvolution, non-Boussinesq SGS model]
tags: [les, sgs-model, filtering, combustion]
timestamp: 2026-10-25T13:42:00Z
---

# Scale-similarity and mixed subgrid-scale models

**Structural** (non-Boussinesq) subgrid-scale models estimate the
[subgrid stress](/definitions/large-eddy-simulation.md) $\tau_{ij}$ from the
resolved field without assuming that it is aligned with the resolved strain.
The **scale-similarity model**, attributed by the sources to Bardina et al.
(1980), assumes that the smallest resolved scales interact with the subgrid
scales as the next-larger scales do with the smallest resolved ones, and
builds the stress from products of the resolved velocity re-filtered at the
grid level. Deconvolution models recover an approximation of the
unfiltered field from $\bar u$ and filter its products. **Mixed models** add
an eddy-viscosity term, usually [Smagorinsky](/methods/smagorinsky-model.md),
to supply the dissipation that the structural part lacks. None of the
sources cited here prints the similarity formula; this page records what
they report about the class.

## Agreed properties

- **Good a priori structure, too little dissipation.** The Bardina model
  shows much better tensor correlations with filtered channel DNS than
  eddy-viscosity models a priori, but is under-dissipative a posteriori and
  needs added Smagorinsky dissipation ([Agrawal et al. 2022](/sources/agrawal-2022.md),
  §V). [Vela-Martín (2022)](/sources/velamartin-2022.md) (§2.2) gives the
  same assessment: similarity models reproduce the stress structure and
  give numerically stable [backscatter](/definitions/energy-backscatter.md)
  but are insufficiently dissipative, hence the mixed model (Zang, Street &
  Koseff 1993, as recalled); the tensor-diffusivity model (Winckelmans et
  al. 2001, as recalled) behaves the same way.
- **Backscatter.** Because the model stress is not tied to the strain,
  $\Pi=-\tau_{ij}\bar S_{ij}$ can be negative locally without the numerical
  instability of a negative eddy viscosity (Vela-Martín 2022, §2.2). In the
  author's view, eliminating backscatter "may be unnecessary or undesirable"
  for such models (§8).
- **Limits of a priori correlation.** Agrawal et al. (2022, §V) note that
  component-wise correlations do not measure alignment, and Vela-Martín
  (2022, §6.3, §8) shows that equivalent stress representations correlate
  only at 0.4–0.6, so that a poor a priori correlation is not by itself
  evidence of poor modelling. Neither source draws the converse conclusion
  for the high correlation of similarity models.

## Velocity-gradient (nonlinear) form

Agrawal et al. (2022, App. C, Eq. C3) show that their
[dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
can be rewritten as a Smagorinsky term plus a strain–rotation commutator
term $\propto\Delta^2(\bar S_{ik}\bar\Omega_{kj}-\bar\Omega_{ik}\bar S_{kj})$,
the form of the two-term velocity-gradient expansion of Lund & Novikov (as
recalled). They list the Bardina similarity model, the Clark gradient model
and Stolz–Adams deconvolution as earlier non-Boussinesq models that need an
added Smagorinsky term, whereas their dynamic coefficients supply enough
dissipation without one (§I, §VII.A).

## Approximate deconvolution

[Domingo & Vervisch (2023)](/sources/domingo-2023.md) (§3.1) describe
approximate deconvolution of a resolved scalar $\bar\phi$ in LES of premixed
flames. Inverting the truncated expansion of a Gaussian filter of width
$\Delta$ gives

$$\phi\approx\bar\phi-\frac{\Delta^2}{24}\nabla^2\bar\phi ,$$

which the authors identify with a backward application of the IEM
micro-mixing model with relaxation time $\Delta^2/(24D_\phi)$
($D_\phi$ the molecular diffusivity, page-local). The deconvolved scalar is
used to compute the nonlinear terms, which are then explicitly filtered;
iterative and neural-network variants exist. Domingo & Vervisch compare
this three-dimensional deconvolution with a structural model that
deconvolves with one-dimensional filtered flamelets. A priori, the
flamelet version's error grows with the subgrid flame wrinkling up to a
threshold, for filter widths of 0.75 to 3 laminar flame thicknesses
(Fig. 5). A posteriori, with LES at $170$–$640\ \mu$m, it overestimates the
CH$_4$ and O$_2$ consumption more than the three-dimensional deconvolution,
and it enhances the overestimation of CO (Fig. 6).

The same second-order operator appears as the continuous Germano
differential filter $\bar u=(1-\Delta^2/24\,\nabla^2)^{-1}u$ recalled by
[Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) (§3.4, Eq. 20),
which the formula above inverts exactly, since
$(1-\Delta^2/24\,\nabla^2)\bar u=u$ *(compiler check, not in the sources)*. [Duraisamy (2021)](/sources/duraisamy-2021.md)
(§III.B) recalls the approximate deconvolution of Stolz & Adams, which
inverts a known filter kernel analytically, and contrasts it with
neural-network deconvolution on a local stencil, where no kernel is
assumed.

## Mixed explicit–implicit model

[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§6.5)
test a different mixture: Smagorinsky ($C_s=0.1$, 0.18) added to an
implicit [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
The Smagorinsky part restores the low-wavenumber plateau of the spectral
eddy viscosity and removes the bottleneck, but the total dissipation does
not improve.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §I; §V; §VII.A; App. C, Eq. (C3).
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.2; §6.3; §8.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §3.1, Eq. (8), Figs. 5–7.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §3.4, Eq. (20).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.B.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.5, Figs. 20–22.
