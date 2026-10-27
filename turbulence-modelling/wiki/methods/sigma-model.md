---
type: Method
title: "Sigma model"
description: "The Sigma model of Nicoud et al. builds a static subgrid eddy viscosity from the singular values of the resolved velocity gradient; the sources use it with constants 1.3–1.35 in jet-noise, spectral-element and finite-volume wall-modelled and learned-closure LES, where it is over-dissipative in coarse isotropic turbulence but accurate in channel spectra."
status: established
aliases: [σ model, σ-model, sigma subgrid-scale model, Nicoud model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-27T05:46:00Z
---

# Sigma model

The **Sigma model** is a static eddy-viscosity closure of the deviatoric
[subgrid stress](/definitions/large-eddy-simulation.md),
$\tau^d_{ij}=-2\nu_t\bar S^d_{ij}$, whose viscosity is built from the
singular values of the resolved velocity-gradient tensor
$\partial_j\bar u_i$. The sources attribute it to Nicoud et al. (2011).
Let $\varsigma_1\ge\varsigma_2\ge\varsigma_3\ge0$ denote those singular
values and $C_\sigma$ the model constant (page-local symbols; the sources
write $\sigma_1,\sigma_2,\sigma_3$, which would collide with the registry's
viscous stress $\sigma_{ij}$). [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md)
(§2.1, Eqs. 4–5) print the model as

$$\nu_t=(C_\sigma\Delta)^2\mathcal D_\sigma,\qquad \mathcal D_\sigma=\frac{\varsigma_3(\varsigma_1-\varsigma_2)(\varsigma_2-\varsigma_3)}{\varsigma_1^2},$$

with $\mathcal D_\sigma$ (page-local) the model's differential operator, in
a compressible LES where it gives the dynamic viscosity
$\mu_t=\bar\rho\nu_t$ (the paper writes $\mu_{SGS}=(C_m\Delta)^2\mathcal D_m$
without the density; see Qualifications). It is a member of the
eddy-viscosity family of the [Smagorinsky](/methods/smagorinsky-model.md),
[WALE](/methods/wale-model.md) and [Vreman](/methods/vreman-model.md)
models: its flux $\Pi=\nu_t\lvert\bar S\rvert^2\ge0$ is purely
dissipative and cannot represent [backscatter](/definitions/energy-backscatter.md)
*(compiler check, not in the sources)*.

## Properties of the operator

From the printed form *(compiler check, not in the sources)*:

- $\mathcal D_\sigma=0$ whenever $\varsigma_3=0$, i.e. for any velocity
  gradient of rank at most two, which includes every two-dimensional,
  two-component field and solid-body rotation (two equal singular values, the
  third zero);
- $\mathcal D_\sigma=0$ when two singular values coincide, e.g. for pure
  shear ($\varsigma_2=\varsigma_3=0$) and for isotropic expansion
  ($\varsigma_1=\varsigma_2=\varsigma_3$);
- $\mathcal D_\sigma$ has the dimension of a velocity gradient, so the
  viscosity scales like the Smagorinsky one.

The near-wall behaviour is what the sources use. [Mukha et al. (2025)](/sources/mukha-2025.md)
(§II.D) give a cubic near-wall asymptote, $\nu_t\sim y^3$, "as WALE", and
call the Sigma model WALE's successor; the Vreman viscosity has a linear
asymptote.

## Constants

| $C_\sigma$ | Context | Source |
|---|---|---|
| 1.35, the recommendation of Nicoud et al. (cited) | wall-modelled LES in the continuous spectral-element code Nek5000 ($N=7$) | Mukha et al. (2025), §II.D |
| 1.3, "the smallest coefficient in the recommended range" | reference model for learned closures in Fourier-spectral LES | [Wu & Lele (2026)](/sources/wu-2026.md), §5.1, §5.1.1 |
| not printed | second-order finite-volume LES of a jet | Moratilla-Vega et al. (2024), §2.1 |
| not printed | second-order finite-volume wall-modelled LES of an airfoil (OpenFOAM) | [Nuca et al. (2025)](/sources/nuca-2025.md), §II, §VI |

Wu & Lele (2026, §5.1) choose it as their baseline because its "coefficient
range works for many different flows and does not require clipping for
channel flow", whereas the [dynamic Smagorinsky model](/methods/dynamic-procedure.md)
"may need clipping" (Meneveau et al. 1996, as cited). Mukha et al. (2025)
take the subgrid length scale as the largest Gauss–Lobatto–Legendre
spacing of the element, assigned to the whole element, and do not force
$\nu_t$ to zero at the wall (§II.D).

## Use and results in the sources

- **Jet-noise LES.** Moratilla-Vega et al. (2024, §2.1) close the LES of a
  cold Mach 0.75 round jet with the Sigma model, in a second-order
  cell-vertex finite-volume code whose Roe-type upwind dissipation is
  scaled by a smoothing parameter of 0.3–1. The LES supplies sources to a
  high-order acoustic solver; the paper attributes no result to the
  subgrid model itself (see [numerical dissipation](/properties/numerical-dissipation.md)).
- **Spectral-element wall-modelled LES.** Mukha et al. (2025, §III.C,
  Figs. 6–8) compare Sigma with Vreman and a high-pass relaxation filter
  in channel flow at $Re_\tau\approx8000$ on their finest mesh.
  - All three give an accurate modelled wall stress and no
    [log-layer mismatch](/definitions/log-layer-mismatch.md).
  - Sigma visibly reduces $\nu_t$ toward the wall, whereas Vreman shows no
    discernible decrease; the authors conclude that "not only the
    asymptotic behavior … but also how fast the model transitions towards
    the asymptote" matters.
  - The lower near-wall dissipation gives a more oscillatory solution,
    with stronger wiggles from derivative jumps across element faces, and
    the wall stress computed from the mean wall gradient deviates from the
    modelled one by $-25.72\%$, against $8.07\%$ with Vreman and $-84.85\%$
    with the filter.
  
  Details are on [wall-modelled LES](/methods/wall-modelled-les.md),
  [spectral-element method](/methods/spectral-element-method.md) and
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md).
- **Earlier wall-modelled LES, as cited.** Mukha et al. (2025, §III.C)
  recall that Blanchard et al. (cited) found WALE and Sigma to over-predict
  the wall stress in channel wall-modelled LES, while WALE performed well
  in other studies; they conclude that accuracy is "a strong function of
  the combination of the boundary conditions, SGS model and numerical
  method" (see [WALE](/methods/wale-model.md)).
- **Finite-volume airfoil WMLES.** Nuca et al. (2025, §II, §VI, App. B)
  close the wall-modelled LES of the Aérospatiale A-airfoil near stall
  with the Sigma model, in OpenFOAM (`pimpleFoam`, second-order linear
  convection in the turbulent region blended with second-order upwind in
  laminar and free-stream regions) with the libWallModelledLES library, on
  $18.7\times10^6$ cells with 10–12 cells across the local boundary-layer
  thickness. The subgrid model is not their subject: the run tests
  explicit approximations of algebraic and ODE
  [equilibrium wall models](/methods/equilibrium-wall-model.md), and no
  result is attributed to the Sigma model.
- **Reference for learned closures.** Wu & Lele (2026) run Sigma
  ($C_\sigma=1.3$) and static Smagorinsky as references for
  [neural-network SGS models](/methods/neural-network-sgs-model.md) in the
  Fourier-spectral solver PadeOps with two-thirds dealiasing.
  - **Forced isotropic turbulence, $64^3$, $Re_\lambda=433$** (§5.1.1,
    Table 3, Fig. 5). Sigma is over-dissipative: its sum of log-spectrum
    errors, a metric of the paper, is 13.34, against 16.6 for Smagorinsky
    and 4.0 for the best two-filter network. The traditional models
    reproduce the longitudinal flatness better than the networks, which the
    authors attribute to their over-dissipation lowering the variance, and
    the enstrophy-production PDF worse.
  - **Coarser grid, $32^3$** (§6.1, Fig. 13). Sigma is still
    over-dissipative, "although less so for this grid resolution, despite
    using the same coefficient"; no model captures the
    enstrophy-production PDF at that resolution.
  - **Wall-modelled channel at $Re_\tau=1000$, $128\times96\times32$**
    (§6.2.1, Figs. 15–16). Sigma and the two-filter network reproduce the
    streamwise spectrum, whereas Smagorinsky piles up energy at high
    wavenumbers; the two-filter network gives "oftentimes … the most
    accurate profiles even when compared to the Sigma model" for the
    Reynolds stresses.

## Qualifications

- Moratilla-Vega et al. (2024) print the viscosity as $\mu_{SGS}$ without
  a density factor and print neither $C_\sigma$ nor $\Delta$; the density
  in $\mu_t=\bar\rho\nu_t$ is added here to make it a dynamic viscosity
  *(compiler check, not in the sources)*.
- Mukha et al. (2025) and Wu & Lele (2026) print no formula; the form above
  is that of Moratilla-Vega et al., and the constants of the table are
  assumed to multiply the same expression. Wu & Lele's 1.3 and Mukha et
  al.'s 1.35 come from different flows, codes and filter widths; none of
  the sources calibrates the constant.

# Citations

- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §2.1, Eqs. (4)–(6).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.D; §III.C, Figs. 6–8.
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §5.1, §5.1.1, Table 3, Fig. 5; §6.1, Fig. 13; §6.2.1, Figs. 15–16.
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §II; §VI; App. B.
