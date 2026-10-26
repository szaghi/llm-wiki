---
type: Method
title: "Vreman model"
description: "Vreman's static eddy-viscosity model builds the subgrid viscosity from an invariant of the resolved velocity-gradient tensor so that it vanishes in many laminar flows; the sources print it in two index orders with constants from 0.08 to 0.17, and use it in aircraft, channel, lattice Boltzmann, DG and shock-interaction LES."
status: established
aliases: [Vreman eddy-viscosity model, Vreman (2004) model, static-coefficient Vreman model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-26T05:09:00Z
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

## Other printed forms and constants

[Kim et al. (2022)](/sources/kim-2022.md) (§II, §III C) and
[Cai et al. (2022)](/sources/cai-2022.md) (§II.A, Eqs. 11–15) print the
model with the opposite index order, $\alpha_{ij}=\partial_i\bar u_j$, and
$\beta_{ij}=\alpha_{mi}\alpha_{mj}$ weighted by the grid spacing. Kim et
al. use a direction-dependent spacing,
$\beta_{ij}=\Delta_m^2\alpha_{mi}\alpha_{mj}$ (summed over $m$, $\Delta_m$
the grid size in direction $m$, page-local), and Cai et al. a single
$\Delta$ equal to the grid size; Cai et al. also write
$B_\beta=\tfrac12[(\mathrm{tr}\,\beta)^2-\mathrm{tr}(\beta^2)]$, the second
invariant of $\beta$. For a single $\Delta$ the two index orders give the
same viscosity: one $\beta$ is $\Delta^2G^TG$ and the other $\Delta^2GG^T$
for the velocity-gradient matrix $G$, which share their invariants, and
$\alpha_{ij}\alpha_{ij}$ is the same *(compiler check, not in the
sources)*. With direction-dependent $\Delta_m$ only the form of Kim et al.
is defined.

| $C_s$ in $\nu_t=2.5C_s^2\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$ | Context | Source |
|---|---|---|
| about 0.17 | the Smagorinsky coefficient | Agrawal et al. (2022), §II.C |
| 0.08 | static baseline and pretraining target in wall-resolved channel LES | Kim et al. (2022), §III C |
| about 0.1, "the Smagorinsky constant" | lattice Boltzmann LES of the Ahmed body | Cai et al. (2022), §II.A |

[Blind et al. (2023)](/sources/blind-2023.md) (§2.3, §3, §3.3) use "the
Vreman model constant" 0.03 for wall-resolved channels, the value of
Toosi & Larsson (as recalled), and 0.11 for the wall-modelled channel,
"from previous experience". The paper does not print the model formula,
so it cannot be decided whether these values are $C_s$ or the prefactor
$2.5C_s^2$ of the table. Their length scale is the DG one,
$\Delta=\mathrm{Vol}^{1/3}/(N+1)$ for an element of volume Vol and degree
$N$ (the paper's $P$), with $N=5$.

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

- **Shock/boundary-layer interaction over a flexible panel.**
  [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) (§3) use the Vreman
  model in a compressible finite-volume wall-modelled LES on unstructured
  hexahedra in arbitrary Lagrangian–Eulerian form, with the Kawai–Larsson
  equilibrium wall model, hybrid ENO/central second-order numerics and a
  digital-filter inflow, coupled to a finite-element panel solver for a
  Mach 3 oblique-shock interaction ($Re_\infty=49.4\times10^6$ m$^{-1}$,
  $\delta_0=4$ mm, about 20 million cells spanwise-periodic). No formula or
  constant of the model is printed. See [wall-modelled LES](/methods/wall-modelled-les.md).
- **Jet reference LES.** Among the reference simulations of the PPRIME
  $M_j=0.9$ round jet listed by [Basile et al. (2023)](/sources/basile-2023.md)
  (Table 1), the LES of Brès et al. uses the Vreman model with a
  second-order finite-volume scheme on 16 and 69 million cells, with
  turbulent injection in the nozzle; Basile et al. note that dof
  comparisons with it are not like-for-like, because it uses a wall model
  and turbulent injection (§4.2.3).

- **Wall-resolved channel, learned-model baseline.** Kim et al. (2022, §II,
  §III C, Fig. 7) use the static Vreman model ($C_s=0.08$) as a baseline
  and as the pretraining target of their
  [reinforcement-learning SGS model](/methods/reinforcement-learning-closure.md),
  noting that it needs only first derivatives and no ad hoc averaging. At
  $Re_\tau=180$ on $(\Delta x^+,\Delta z^+)=(70.7,35.3)$ it predicts the
  mean velocity reasonably but over-estimates the Reynolds shear stress and
  under-predicts the mean subgrid transport $\langle\partial_j(\tau_{ij}\bar u_i)\rangle$
  compared with filtered DNS. Pretraining on Vreman converges slightly
  faster than on the dynamic Smagorinsky model (§II D, no results shown).
- **Lattice Boltzmann LES with an immersed boundary.** Cai et al. (2022,
  §II.A, §II.C.1) use the model in the lattice Boltzmann solver ProLB on
  octree Cartesian grids for the Ahmed body with a 35° slant; near the wall
  a constrained-LES eddy viscosity built on it imposes the total shear
  stress of a mixing-length RANS model (see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
  [immersed boundary methods](/methods/immersed-boundary-method.md)).
- **DG grid adaptation.** Blind et al. (2023, §2.2–2.3) use the model in
  [FLEXI](/software/flexi.md) to estimate the LES modelling residual that
  drives [mesh adaptation](/methods/mesh-adaptation.md): the residual is
  evaluated on a test-filtered field with only the Vreman length scale
  changed, to $\hat\Delta=[(N+1)/(N_f+1)]^{1/3}\Delta$ for a modal test
  filter that keeps degrees up to $N_f=3$ ($N_f$ page-local, as on the
  mesh-adaptation page; the paper's $M$). In the
  wall-modelled channel at $Re_\tau=2000$ the constant 0.11 is used with a
  Spalding wall law at $h_{\mathrm{wm}}=0.1\delta$ (§3.3). See
  [wall-modelled LES](/methods/wall-modelled-les.md).
- **HORSES3D.** The model is one of the explicit LES models of the
  [HORSES3D](/software/horses3d.md) DG code, with Smagorinsky and WALE
  ([Ferrer et al. 2023](/sources/ferrer-2023.md), §4.1; no formula printed).

## Fluctuating viscosity and the mean stress

[Haering et al. (2022)](/sources/haering-2022.md) (§V D) list Vreman with
Smagorinsky and WALE as fluctuating-viscosity models: used as the
energy-transfer part of their model-split hybrid, their correlation with
the strain gives a contribution to the mean stress that would have to be
computed and subtracted from the mean-stress model.

## Qualifications

- Blind et al. (2023, §2.3) state that the test-level eddy viscosity is "a
  factor of $[(P+1)/(M+1)]^{2/3}\approx1.59$ larger"; with the printed
  $P=5$ (the registry's $N$) and $M=3$ (here $N_f$), $(6/4)^{2/3}\approx1.31$ *(compiler
  check, not in the sources)*, so the printed number or the printed
  exponent is wrong. The page records the version read (arXiv
  2301.03199v1).
- The constants in the table belong to different flows, filter-width
  definitions and codes; none of the sources calibrates the constant.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.C, Eqs. (9)–(10); §VIII.A–B, Figs. 13–19.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1; §3.1–3.2.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §3.1.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §7.3, Fig. 27.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Basile et al. (2023)](/sources/basile-2023.md) — §4.2.3, Table 1.
- [Kim et al. (2022)](/sources/kim-2022.md) — §II; §II D; §III C, Fig. 7.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.A, Eqs. (11)–(15); §II.C.1.
- [Blind et al. (2023)](/sources/blind-2023.md) — §2.2–2.3; §3; §3.3.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1.
