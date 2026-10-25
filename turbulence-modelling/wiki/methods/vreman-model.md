---
type: Method
title: "Vreman model"
description: "Vreman's static eddy-viscosity model builds the subgrid viscosity from an invariant of the resolved velocity-gradient tensor so that it vanishes in many laminar flows; the sources give its form and report its use in aircraft LES, burner LES and cavity noise, and its failure to separate on the Gaussian bump."
status: established
aliases: [Vreman eddy-viscosity model, Vreman (2004) model, static-coefficient Vreman model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-25T13:42:00Z
---

# Vreman model

The **Vreman model** is an eddy-viscosity closure of the deviatoric
[subgrid stress](/definitions/large-eddy-simulation.md),
$\tau^d_{ij}=-2\nu_t\bar S_{ij}$, with a static coefficient and a viscosity
built from an invariant of the resolved velocity-gradient tensor. The
sources cite Vreman (2004). Only
[Agrawal et al. (2022)](/sources/agrawal-2022.md) print it (§II.C, Eqs. 9–10):

$$\nu_t=2.5\,C_s^2\sqrt{\frac{B_\beta}{\alpha_{ij}\alpha_{ij}}},\qquad
\alpha_{ij}=\partial_j\bar u_i,\qquad
\beta_{ij}=\Delta^2\alpha_{mi}\alpha_{mj},$$

$$B_\beta=\beta_{11}\beta_{22}-\beta_{12}^2+\beta_{11}\beta_{33}-\beta_{13}^2+\beta_{22}\beta_{33}-\beta_{23}^2 ,$$

with $C_s\approx0.17$, the Smagorinsky coefficient (so the prefactor is
$2.5C_s^2\approx0.072$, *compiler check, not in the sources*). The symbols
$\alpha_{ij}$, $\beta_{ij}$, $B_\beta$ are page-local, and the index order
of $\alpha_{ij}$ and of the contraction in $\beta_{ij}$ is that printed by
Agrawal et al. Agrawal et al. state that the model gives zero dissipation
in laminar base flows with two velocity components and does not
overpredict dissipation in transitional flows. Unlike the
[dynamic procedure](/methods/dynamic-procedure.md), it needs no test
filter and no averaging; Agrawal et al. (§II.A) recall that the plain
[Smagorinsky model](/methods/smagorinsky-model.md), by contrast, does not
vanish at walls without damping.

## Use in the sources

- **High-lift aircraft.** [Goc et al. (2021)](/sources/goc-2021.md)
  (§2.1, §3.1–3.2) use the static-coefficient Vreman model with an
  equilibrium wall model for the free-air computations of the JAXA Standard
  Model at $Re_c=1.96\times10^6$, $M_\infty=0.172$, in two low-dissipation
  codes (charLES, Alya). At baseline resolution (charLES 32 million cells,
  $\delta_{99}/\Delta\approx10$ at the main-element trailing edge) the lift
  curve, $C_{L,\max}$ and stall onset are captured reasonably; the in-tunnel
  cases switch to the dynamic Smagorinsky model. See
  [JAXA Standard Model](/benchmarks/jaxa-standard-model.md).
- **Burner LES.** In the LES zones around the embedded DNS box of a premixed
  Bunsen jet, the SGS momentum fluxes "are modeled" with a citation of
  Vreman's paper, the model not being named in the text
  ([Domingo & Vervisch 2023](/sources/domingo-2023.md), §3.1).
- **Cavity noise.** [Krais et al. (2021)](/sources/krais-2021.md) (§7.3)
  run a zonal wall-modelled LES of an open cavity in FLEXI ($N=7$, 30
  million degrees of freedom per variable, $Re_\theta=6300$) with the
  Kawai–Larsson wall model and the Vreman model, which "helps to reduce
  artificial pressure fluctuations caused by the wall-model". Vreman is
  also listed among FLEXI's eddy-viscosity models (§2.2.3).
- **Gaussian bump.** Agrawal et al. (2022, §VIII) compare Vreman with the
  dynamic Smagorinsky and the
  [tensor-coefficient](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
  models in charLES wall-modelled LES. On the spanwise-periodic bump
  ($Re_L=2\times10^6$) Vreman converges non-monotonically in $C_f$ (as DSM
  does) and predicts a smaller separation bubble than the quasi-DNS
  (Figs. 13–14). On the 3D bump ($Re_L=3.41\times10^6$, up to 452 million
  cells) it misses the separation, the apex pressure peak and the
  counter-rotating vortex pair even on the finest grid (Figs. 15–19),
  agreeing with Iyer & Malik, who are recalled to find no separation with
  Vreman up to 450 million control volumes.

## Fluctuating viscosity and the mean stress

[Haering et al. (2022)](/sources/haering-2022.md) (§V D) list Vreman with
Smagorinsky and WALE as fluctuating-viscosity models: used as the
energy-transfer part of their model-split hybrid, their correlation with
the strain gives a contribution to the mean stress that would have to be
computed and subtracted from the mean-stress model.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.C, Eqs. (9)–(10); §VIII.A–B, Figs. 13–19.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1; §3.1–3.2.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §3.1.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §7.3, Fig. 27.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D.
