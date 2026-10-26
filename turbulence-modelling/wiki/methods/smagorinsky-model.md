---
type: Method
title: "Smagorinsky model"
description: "The Smagorinsky model closes the deviatoric subgrid stress with an eddy viscosity (C_s Δ)²|S̄|; the sources report its constants, filter-width definitions in element methods and on high-aspect-ratio cells, its interaction with numerical error, and its a priori and a posteriori behaviour."
status: established
aliases: [Smagorinsky eddy-viscosity model, static Smagorinsky model, SSM, constant-coefficient Smagorinsky]
tags: [les, sgs-model, eddy-viscosity, numerical-dissipation]
timestamp: 2026-10-26T15:49:00Z
---

# Smagorinsky model

The **Smagorinsky model** closes the deviatoric part of the
[subgrid-scale stress](/definitions/large-eddy-simulation.md) with an eddy
viscosity proportional to the square of a length $C_s\Delta$ and to the
resolved strain-rate magnitude:

$$\tau^d_{ij}=-2\nu_t\bar S_{ij},\qquad \nu_t=(C_s\Delta)^2\lvert\bar S\rvert,\qquad \lvert\bar S\rvert=\sqrt{2\bar S_{ij}\bar S_{ij}} .$$

This is the form of [Agrawal et al. (2022)](/sources/agrawal-2022.md)
(§II.A, Eqs. 4–5), [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§4.1, Eqs. 24–26), [Beck & Kurz (2023)](/sources/beck-2023.md) (§III B,
Eqs. 9–10, written for the dynamic viscosity
$\mu_t=\bar\rho\nu_t$) and [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
(§4.4.1, Eqs. 26–27, with the coefficient written $\theta$ and the closure
term $\nabla\cdot(2\nu_t\bar S)$). It is the [Boussinesq](/definitions/boussinesq-hypothesis.md)
closure applied to the subgrid scales; its model flux
$\Pi=-\tau_{ij}\bar S_{ij}=\nu_t\lvert\bar S\rvert^2\ge0$ is purely
dissipative, so it cannot represent [backscatter](/definitions/energy-backscatter.md).
The sources attribute it to Smagorinsky (1963). The coefficient can be
computed from the resolved field by the [dynamic procedure](/methods/dynamic-procedure.md),
and [Vreman's model](/methods/vreman-model.md) and the
[tensor-coefficient model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
are variants of the same eddy-viscosity idea.

## The coefficient

| Value of $C_s$ | Context | Source |
|---|---|---|
| about 0.17 | isotropic turbulence, inertial-range resolution (Lilly, cited) | Agrawal et al. (2022, §II.A) |
| about 0.1 | shear flows (Deardorff, cited) | Agrawal et al. (2022, §II.A) |
| 0.18 | Lilly's analytical value $\pi^{-1}(3C_K/2)^{-3/4}$ with Kolmogorov constant $C_K=1.4$ (page-local symbol), as cited | Vicente Cruz & Lamballais (2023, §6.5) |
| 0.1 | reference constant for the Taylor–Green vortex and pipe; a dynamic procedure is recalled to give about 0.1 after breakdown | Vicente Cruz & Lamballais (2023, §4.1) |
| 0.17 | static baseline (SSM) in DG LES of forced HIT; the authors remark it is valid in principle only for specific explicit filters | Beck & Kurz (2023, §V) |
| 0.12 | on a dissipation-free split-form DG baseline | [Flad & Gassner (2017)](/sources/flad-2017.md), Fig. 7 |
| 0.17 | small–small VMS variant on DG ILES | Flad & Gassner (2017), Fig. 3 |
| 0.000–0.144 | fitted per grid, filter and formulation on 2D forced turbulence by grid search on the a posteriori error | Agdestein & Sanderse (2025), App. B.5, Table B.5 |
| 0.17 | "the common choice", 3D forced turbulence | Agdestein & Sanderse (2025), App. G.2 |
| 0.1 | with van Driest damping $A^+=25$, called "generally used constants"; a priori test on a backward-facing-step shear layer | [Abe (2021)](/sources/abe-2021.md), §II A, Eqs. (3)–(4) |
| 0.2 | viscosity amplitude of an SVV-filtered LES in DG ($N=8$) | [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §6.1, Eq. (125) |
| 0.17 | static baseline in DG LES of forced HIT, "theoretical $C_s=0.17$ suggested" in the literature (no citation) | [Kurz et al. (2023)](/sources/kurz-2023.md), §3.5 |
| 0–0.5 | element-wise range of a reinforcement-learned coefficient | Kurz et al. (2023), §3.4 |
| 0.16 | "estimated … by Lilly for isotropic turbulence", as printed; the value used in the runs is not stated | [Duan & Wang (2024)](/sources/duan-2024.md), §2.2 |
| 0.16 | "classical" value, "determined through theoretical arguments for isotropic turbulence", stated to be over-dissipative in transition | [Wang et al. (2023c)](/sources/wang-2023-c.md), §II.A |
| $\sqrt{0.01/2}\approx0.071$ | coefficient of a Smagorinsky term alone, calibrated a posteriori by an ensemble Kalman filter against filtered-DNS spectra of forced isotropic turbulence ($C_{\mathrm f}=2C_s^2=0.01$, $C_{\mathrm f}$ page-local, the paper's $C_D$) | Wang et al. (2023c), App. C |
| trained, value not reported | 1D Burgers closure baseline, filter width the coarse grid spacing | [van Gastelen et al. (2024)](/sources/vangastelen-2024.md), §4.1.1 |
| 0.14 (0.21 for a Burgers test); range "usually" $0.12<C_s<0.21$ | continuous spectral-element LES of atmospheric-type flows, $\Delta=\min(h_x,h_y,h_z)/(N+1)$ | [Reddy et al. (2026)](/sources/reddy-2026.md), §3.1 |
| 0.15 | wall-resolved LES of a flexible aquatic canopy; the value of earlier canopy LES (0.17 in another group) | [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md), §2.1 |
| 0.1 | decaying isotropic turbulence, sharp spectral filter at $k_c=10$; constraint of a physics-informed neural operator | [Zhao et al. (2025)](/sources/zhao-2025.md), §3.1 |
| $\sqrt{0.001}\approx0.032$ | temporal mixing layer, same use | Zhao et al. (2025), §3.2 |
| 0.098–0.112 / 0.186–0.198 | learned from one trajectory of Smagorinsky-LES data / of filtered-DNS data, for weights $\gamma'\ge5$ of the coefficient loss | Zhao et al. (2025), §4, Table 4 |
| 0.16, inside the Vreman constant $2.5C_s^2$ | spectral-element wall-modelled LES | [Mukha et al. (2025)](/sources/mukha-2025.md), §II.D |

Lilly's value is consistent with the recalled formula: $\pi^{-1}(2.1)^{-3/4}\approx0.18$
*(compiler check, not in the sources)*. The square root in the Wang et
al. row is a *compiler check, not in the sources*: they write the
Smagorinsky part as $-C_{\mathrm f}\Delta^2\lvert\bar S\rvert\bar S_{ij}$ and state
$C_{\mathrm f}=2C_s^2$; inside their mixed model the same calibration gives
$C_{\mathrm f}\approx0.00738$, about 0.061 in $C_s$ (see the
[gradient model](/methods/gradient-model.md)). The EnKF-calibrated
coefficient alone is "about 36 percent larger" than the mixed one and
about a fifth of the classical $C_{\mathrm f}\approx0.05$ (App. C, §III). The fitted 2D coefficients of
Agdestein & Sanderse decrease with resolution and reach 0.000 for the
divergence-inconsistent formulation at $\bar n=256$, which the authors
explain by the Smagorinsky term not being divergence-free; they are
error-optimal fits, not model constants. [Prakash et al. (2022)](/sources/prakash-2022.md)
(§II), citing earlier work, state that the optimal $C_s$ is flow dependent,
which motivates the dynamic procedure; they use no fixed value.
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (§II, Eqs. 3–4)
write $\nu_t=C_s\mathcal L^2\lvert\bar S\rvert$ with $\mathcal L$ the
effective grid scale, so their $C_s$ is the square of the registry's; they
call its flow dependence its main drawback (no single universal constant
across flows, §II) and Smagorinsky "one of the most dissipative models"
(§IV), and do not print the value used. The square root in Zhao et al.'s
mixing-layer row is a *compiler check, not in the sources*: they print
$C_{\mathrm{Smag}}=\sqrt{0.001}$.

**A coefficient learned from data.** [Zhao et al. (2025)](/sources/zhao-2025.md)
(§4, Eqs. 25–26, Table 4, Figs. 19–23) make $C_s$ a trainable parameter of
their [physics-informed neural operator](/methods/neural-operator-les-surrogate.md).
The coefficient is fitted by the residual of the filtered equations on a
single 11-frame trajectory, while the operator is trained on the
Smagorinsky-closed equations.

- **Smagorinsky-LES data.** With data from an LES run at $C_s=0.1$, the
  learned value is 0.0982–0.1123 for loss weights $\gamma'\ge5$; the
  method recovers the coefficient that generated the data.
- **Filtered-DNS data.** With filtered DNS of decaying isotropic turbulence
  ($32^3$, sharp cutoff at $k_c=10$), it settles at 0.1856–0.1983.
- **Same a posteriori result.** Both coefficients give comparable a
  posteriori results, and the authors note that the learned value "is not
  always unique".

The filtered-DNS value is fitted to the LES residual of one filtered
trajectory. It lies within 0.01 of the 0.18 that Vicente Cruz & Lamballais
(2023) derive from Lilly's value (see the table above) *(compiler check,
not in the sources)*.

## Filter width in element methods

In DG, Beck & Kurz (2023, Eq. 11) take $\Delta=\sqrt[3]{\mathrm{Vol}}/(N+1)$
for an element of volume Vol and polynomial degree $N$ and note that the
choice is not unique. [Haering et al. (2022)](/sources/haering-2022.md)
(§II C) argue that the cube root of the cell volume overestimates the
resolution of high-aspect-ratio cells. [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
keep $\Delta$ as a parameter independent of the mesh; their cell-based
variant $\nu_t=(C_s\Delta x)^2\lvert\bar S\rvert$ (Eq. 47) shows that
$C_s$ and $\Delta/\Delta x$ are not separately identifiable: running
$\Delta x=\Delta/5$ with $C_s=0.1$ is the same model as $\Delta=\Delta x$
with $C_s=0.5$. [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md)
(§6.1, Eq. 125) define $\Delta^3=\mathrm{Vol}/(N+1)^3$ for DG elements, the
cube of the Beck & Kurz width.

[Duan & Wang (2024)](/sources/duan-2024.md) (§3, Eqs. 28–30) compare the
widths $V^{1/3}$, $V^{1/3}/\sqrt{N+1}$ and $V^{1/3}/(N+1)$ ($V$ the
element volume, $N$ the paper's $P$) for Smagorinsky,
[WALE](/methods/wale-model.md) and [Vreman](/methods/vreman-model.md) in a
flux-reconstruction solver, with an element-averaged eddy viscosity and
zero interface flux of the subgrid stress (Eqs. 26–27). Smagorinsky is the
most dissipative of the three on the Taylor–Green vortex (§5.1, Figs.
5–7), and in the wall-resolved channel at $Re_\tau=180$ ($N=3$) it
"performs very poorly" with all three widths because of its large
near-wall eddy viscosity (§5.3, Figs. 9–10); their wall-modelled
comparisons use only WALE and Vreman (§5.4). Their stress has the sign of
the viscous stress, $+2\bar\rho\nu_tS_{ij}$ added to it, with the full
(not deviatoric) strain (§2.1–2.2).

## Filter width on high-aspect-ratio cells

[Abe (2021)](/sources/abe-2021.md) tests the model a priori in the free
shear layer behind a [backward-facing step](/benchmarks/backward-facing-step.md),
on a coarse grid with $\Delta x=\Delta z=0.1H$ and wall-normal spacing down
to $10^{-3}H$ ($\Delta x/\Delta y\sim100$ in the shear layer), against a
fine LES filtered to that grid. With the cube root
$\Delta=(\Delta x\Delta y\Delta z)^{1/3}$ (also the definition of Prakash
et al. 2022, §II, after Deardorff), the Smagorinsky viscosity is "much
smaller than the reference data", "clearly suppressed by the extremely
narrow grid width in the y-direction" (§IV C, Fig. 9a). With
$\Delta=\max(\Delta x,\Delta y,\Delta z)$ (the author's mSM) it has "a
reasonable distribution even in the shear layer" (§IV D, Fig. 10). The
author concludes that "the effect of a grid width in one direction much
smaller than in other directions must be excluded in determining the filter
width" (§V). The [dynamic procedure](/methods/dynamic-procedure.md), which
computes $(C_s\Delta)^2$ as one product, does not depend explicitly on the
definition of $\Delta$ (§II A). The same suppression appears in the
algebraic subgrid energy obtained by equating the Smagorinsky viscosity to
a one-equation viscosity $C_{\mathrm{sgs}}f_{\mathrm{sgs}}\sqrt{k_{\mathrm{sgs}}}\Delta$
(§IV E, Eqs. 18–20): $k_{\mathrm{sgs}}=0.04\,(f_S^4/f_{\mathrm{sgs}}^2)\,\Delta^2\lvert\bar S\rvert^2$
in the registry's $\lvert\bar S\rvert$, the paper's $0.08\,(f_S^4/f_{\mathrm{sgs}}^2)\Delta^2\bar S_{ij}\bar S_{ij}$
with $C_s=0.1$, $C_{\mathrm{sgs}}=0.05$; the registry form is
*(compiler check, not in the sources)*. See [large-eddy simulation](/definitions/large-eddy-simulation.md)
for the filter-width question across the sources.

## Interaction with numerical error

Vicente Cruz & Lamballais (2023, §6.3, Figs. 7–12), on the Taylor–Green
vortex at $Re=40\,000$ with sixth-order compact differences:

- in the standard condition $\Delta x=\Delta$ with $C_s=0.1$, the model
  cannot control the energy pile-up near the mesh cutoff and overestimates
  the total dissipation; the authors attribute this to the interaction of
  differentiation errors with the model, not to the model itself, and note
  that reducing $C_s$ would worsen it;
- at fixed $\Delta=\pi/108$, numerical convergence through the breakdown
  requires $\Delta x=\Delta/5$, i.e. $C_s=0.5$ in the cell-based form, at a
  cost factor $5^4=625$; $\Delta x=\Delta/2.5$ still thermalizes;
- at fixed cost, $\Delta=2.5\Delta x$ (cell-based $C_s=0.25$) gives better
  total dissipation than $\Delta=\Delta x$ and cuts the maximum spectral
  deviation by more than a factor 4, so "$C_s=0.25$ and even $C_s=0.5$ is
  highly preferable to the common choice $C_s=0.1$";
- at convergence the model acts as a weak filter, with effective transfer
  function about 0.6 at the filter wavenumber, and its a posteriori
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) has "no
  common features" with the a priori one: of the right order at low
  wavenumbers but nearly constant and vanishing near the cutoff, with the
  drop scaling on the mesh cutoff (a signature of numerical error).

[Flad & Gassner (2017)](/sources/flad-2017.md) (§1, §4) find the same
dependence on the baseline in DG. Added to de-aliased DG ILES with Roe
dissipation, Smagorinsky or small–small VMS Smagorinsky gives no
significant improvement on coarse DHIT "independent of the SGS model
constants used" (Fig. 3). Added to a dissipation-free
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
split-form DG at $48^3$ degrees of freedom, Smagorinsky with $C_s=0.12$
gives what the authors call the first successful coarse-resolution DG LES,
better than ILES in energy and dissipation spectra (Fig. 7). Their argument
is that a dissipation-free baseline separates stability from model
dissipation.
The model does not damp pressure and density fluctuations, so the
pressure–dilatation oscillates unless a low-dissipation Roe flux is added
(§5.1).

## Variants

- **Wall damping.** The model does not vanish at a wall; Van Driest damping
  is recalled as the classical fix (Agrawal et al. 2022, §II.A) and is used
  with Smagorinsky in the pipe LES of Vicente Cruz & Lamballais (2023,
  §7.3), where the SGS viscosity reaches about $3\nu$ instantaneously and
  $0.3\nu$ on average near the wall; the damping form is not printed there.
[Abe (2021)](/sources/abe-2021.md) (§II A, Eq. 4) prints it:
$\nu_t=(C_sf_S\Delta)^2\lvert\bar S\rvert$ with
$f_S=1-\exp(-y^+/A^+)$, $A^+=25$; in §IV E (Eq. 20) the author switches to
$f_S=\sqrt{1-\exp[-(y^+/A^+)^3]}$, "considering the correct near-wall
limiting behavior".
- **Small–small VMS.** The strain is computed from high-pass filtered
  (polynomial-projection) gradients (Flad & Gassner 2017, App. B,
  Eq. B.1).
- **Plateau–cusp addition.** A modal cusp eddy viscosity added to
  Smagorinsky, modelled on the Chollet–Lesieur
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)
  (Flad & Gassner 2017, App. C).
- **Elementwise coefficient by reinforcement learning.** Beck & Kurz (2023,
  §III B, Eqs. 12–15) let a policy choose $C_s$ per DG element, either
  constant (RL-Const) or a constant plus a second-Legendre-mode parabola
  (RL-Quad), clipped at zero. The trained distributions are strongly skewed
  towards small $C_s$, and RL-Quad places its maximum at the element centre
  (§V B); see [reinforcement-learning closures](/methods/reinforcement-learning-closure.md).
- **Element-wise coefficient, element-local policy.** In a related paper
  of the same group, [Kurz et al. (2023)](/sources/kurz-2023.md) (§3.4, §4.2–4.4,
  Figs. 6, 8) learn one $C_s\in[0,0.5]$ per DG element from the momentum
  field inside the element only, with the form $\mu_t=\bar\rho(C_s\Delta)^2\lvert\bar S\rvert$
  (Eq. 19). Most predicted values are close to zero with a decaying tail;
  at 24 degrees of freedom per direction the policy uses almost the whole
  range up to 0.5, at 48 its largest value does not exceed 0.3. A policy
  trained at 36 degrees of freedom predicts up to 0.4 and one trained at 48
  up to 0.3 on either resolution, from which the authors conclude that the
  coefficient distribution is a property of the discretization the policy
  was trained on ("discretization-adapted" models; see
  [discretization-consistent closure](/definitions/discretization-consistent-closure.md)).
- **Shear-improved Smagorinsky in lattice Boltzmann.** [Cheylan et al. (2023)](/sources/cheylan-2023.md)
  (§2.7, Eqs. 37–38), following Lévêque et al. (cited), subtract from
  $\lvert\bar S\rvert$ the norm of a low-pass time-filtered strain rate,
  so that the viscosity responds only to the fluctuating shear, with the
  local lattice spacing as filter width. The eddy viscosity enters the
  [lattice Boltzmann](/methods/lattice-boltzmann-method.md) relaxation time
  as $(\nu+\nu_t)/c_s^2+\tfrac12\Delta t$ ($c_s$ the lattice sound speed,
  $\Delta t$ the time step, page-local). It is used for a turbulent
  fluid–structure benchmark at $Re=10\,000$; the constant and the
  normalization of the strain norm are not printed.
- **Smagorinsky limit of DDES.** [Delassaux et al. (2023)](/sources/delassaux-2023.md)
  (§4.1.3) state that under local equilibrium (production equal to
  dissipation) the subgrid model of SST-based delayed
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)
  reduces to the Smagorinsky–Lilly model; the derivation is not given.
- **Mixed explicit–implicit.** Smagorinsky added to implicit SVV
  (Vicente Cruz & Lamballais 2023, §6.5); see
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
- **SVV-filtered Smagorinsky in DG.** [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md)
  (§6.1) use the Smagorinsky viscosity ($C_s=0.2$) as the amplitude of an
  artificial viscous flux that a modal spectral-vanishing-viscosity filter
  with kernel $(i/N)^{P}$ weights, in an entropy-stable form. On the
  inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  ($8^3$ elements, $N=8$, kinetic-energy-preserving split form with a
  low-dissipation Roe flux), the unfiltered model ($P=0$) is excessively
  dissipative, and $P\approx0.1$ gives a spectrum close to $k^{-5/3}$ at
  $t=20$ (Fig. 4); see [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
- **Mixed with a structural model.** A Smagorinsky term stabilizes the
  [gradient model](/methods/gradient-model.md); optimal clipping derives a
  pointwise coefficient for it (Prakash et al. 2022, §II). In the
  compressible dynamic mixed model of [Helm & Martín (2022)](/sources/helm-2022.md)
  (§II, Eq. 9) the eddy-viscosity part is a dynamic Smagorinsky term
  $-2C_1\Delta^2\bar\rho\lvert\tilde S\rvert\tilde S^d_{ij}$ ($C_1$
  page-local, Favre filter as tilde) with
  $\Delta=(\Delta_\xi\Delta_\eta\Delta_\zeta)^{1/3}$ over the computational
  directions; used alone it lengthens a hypersonic separation by 30% (see
  [scale-similarity models](/methods/scale-similarity-model.md)).
- **SVV-Smagorinsky in HORSES3D.** [Ferrer et al. (2023)](/sources/ferrer-2023.md)
  (§4.1) list Smagorinsky, WALE (Nicoud & Ducros, as cited) and Vreman as
  the explicit LES models of the [HORSES3D](/software/horses3d.md) DG code,
  with the group's SVV-Smagorinsky combination, said to keep dissipation low
  in laminar flow while "providing the correct dissipation for all
  wave–number ranges in turbulent regimes" (citing Manzanero et al.). The
  paper prints no model equation, constant or filter width.

- **Compressible temporal LES of aircraft wakes.** [Bouhafid et al. (2024)](/sources/bouhafid-2024.md)
  (§2.2, Eq. 2.6; §4.1) model both the Favre-filtered subgrid stress
  $\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$ and the subgrid heat
  flux with the Smagorinsky model in the ONERA finite-volume solver CHARME
  (second-order HLLC fluxes), in a periodic box that continues a RANS
  solution of the aircraft into the vortex and dissipation regimes of the
  wake (160 million cells, $\Delta/r_c=0.1$ in the descent zone, $r_c$ the
  vortex core radius, page-local). The constant, filter width and subgrid
  Prandtl number are not printed.
- **1D Burgers baseline.** In the 1D closure study of van Gastelen et al.
  (2024, §4.1.1, Eqs. 54–55) the constant-coefficient model, written on
  the coarse grid with filter width equal to the grid spacing, is trained
  like the network parameters. It is chosen because a cited study found it
  "the best performing non-machine learning closure … outperforming the
  dynamic Smagorinsky model" on Burgers (cited). It is too
  dissipative in the spectra (§4.6), yet it beats no closure over the
  whole viscosity range of the extrapolation test, where a vanilla
  convolutional network degrades as $\nu$ decreases and the
  structure-preserving closure is best (§4.7, Fig. 13); see
  [neural-network SGS models](/methods/neural-network-sgs-model.md).

- **Near immersed bodies.** In the canopy LES of
  [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) (§2.1, §2.3, §3.3,
  App. C), $\nu_t$ is damped near the immersed blades with the smoothed
  delta function used for the
  [immersed-boundary](/methods/immersed-boundary-method.md) interpolation,
  "as required by the Smagorinsky model employed".
  - The authors recall that halving or doubling $C_s$ "had practically no
    effect" in the earlier canopy study of their group (Tschisgale et al.).
  - The subgrid contribution to the mean drag is smaller than the viscous
    one everywhere.
  - The LES activity parameter (defined on the
    [large-eddy simulation](/definitions/large-eddy-simulation.md) page)
    has mean 0.11.
- **Spectral-element LES with discontinuities.**
  [Reddy et al. (2026)](/sources/reddy-2026.md) (§5–9) compare Smagorinsky
  with [Vreman](/methods/vreman-model.md) and the
  [residual-based dynamic model](/methods/residual-based-dynamic-sgs-model.md)
  at polynomial degree $N=4$.
  - **Tracer transport.** Smagorinsky keeps tracer discontinuities sharp,
    but with errors in the extrema of 0.12 and 0.15 kg/kg.
  - **Burgers test.** It produces Gibbs oscillations: it oscillates
    "severely" without diverging (§6.2).
  - **Density current.** It resolves Kelvin–Helmholtz rotors at the
    coarsest spacing. It is the only model whose front position does not
    advance monotonically with refinement (15 034, 15 117, 15 091 m at 50,
    25, 12.5 m).
  - **Taylor–Green vortex.** It dissipates more kinetic energy than Vreman.
  - The full strain, not its deviatoric part, enters the closure (Eq. 4).
- **Physics-informed constraint.** Zhao et al. (2025, §2.5, Eqs. 3–5, 17)
  train a [neural operator](/methods/neural-operator-les-surrogate.md) on
  the residual of the LES equations closed by Smagorinsky. Its accuracy is
  "bounded by" that model (§6), and its a posteriori results are close to
  Smagorinsky LES rather than to filtered DNS (§3.1).

## A priori and a posteriori behaviour

[Duraisamy (2021)](/sources/duraisamy-2021.md) (§IV.A) cites Smagorinsky
as the example that a priori success is "neither a necessary … nor a
sufficient condition" for a good model. [Vela-Martín (2022)](/sources/velamartin-2022.md)
(§8), citing Clark et al. (1979), Meneveau (1994) and Borue & Orszag (1998)
for the poor a priori correlation of eddy-viscosity models, offers an
explanation of their success: the SGS stress is defined only up to a
divergence-free gauge, and equivalent stresses correlate with one another
only at 0.4–0.6 (§6.3), so a low a priori correlation need not mean poor
modelling. [Haering et al. (2022)](/sources/haering-2022.md) (§II B), citing
filtered-turbulence data, state that a simple eddy viscosity cannot
represent both the mean subgrid stress and the subgrid energy transfer: the
stress–strain correlation is "of order 20% or less", against one for an
eddy-viscosity model. They add (§V D) that a fluctuating Smagorinsky
viscosity correlated with the strain contributes to the mean stress even
when meant only for the fluctuations (their critique of a two-velocity
hybrid that uses Smagorinsky on the fluctuating strain).

In 3D forced turbulence Agdestein & Sanderse (2025, App. G.2) find
Smagorinsky ($C_s=0.17$) too dissipative at high wavenumbers compared with
a learned closure; in 2D decaying turbulence it is more dissipative than no
model (App. G.1). In DG LES of forced HIT at $N=5$ it over-damps the high
wavenumbers where no-model LES piles energy up (Beck & Kurz 2023, §V B,
Fig. 9). Smagorinsky is among the SGS models available in FLEXI ([Krais et al. 2021](/sources/krais-2021.md), §2.2.3)
and LESGO ([Vadrot et al. 2023b](/sources/vadrot-2023-b.md), §II A;
[Vadrot et al. 2023a](/sources/vadrot-2023.md), §II.A, which does not say
which of LESGO's models its runs use), and is
the base of the dynamic model used in the wall-modelled LES of
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) (§II.B).
Prakash et al. (2022, §II), citing a priori studies, state that the
alignment of $\tau^d_{ij}$ with $\bar S_{ij}$ assumed by the model does not
hold and that eddy-viscosity models correlate poorly with the exact stress.
The finest DG reference LES of the PPRIME jet listed by [Basile et al. (2023)](/sources/basile-2023.md)
(Table 1, Lorteau et al.) uses Smagorinsky at $N=3$ with 78 million
degrees of freedom.

**Alignment.** [Kim et al. (2022)](/sources/kim-2022.md) (§III E,
Eq. 27, Figs. 15–20, Table IV) quantify the alignment assumption in
channel flow at $Re_\tau=180$, applying all models to the same resolved
field. The angle between $-\tau^d_{ij}$ and $\bar S_{ij}$ is zero by
construction for a linear eddy-viscosity model, whereas in filtered DNS
its mean is near $\pi/2$ at all heights. The correlation of $\bar S_{xy}$
with $-\tau_{xy}$ is $-0.20$ and 0.19 at $y^+\approx15$ and 50 in
filtered DNS, against 0.95 and 0.94 for the dynamic Smagorinsky model. The
eddy viscosity obtained from the eigenvalue ratio of $-\tau^d_{ij}$ and
$\bar S_{ij}$ is "one order of magnitude larger" in filtered DNS than in
every model. An eddy-viscosity form of their learned model over-predicts
the mean velocity like the dynamic model, while the tensor form does not;
the authors conclude that "the eddy-viscosity assumption could seriously
limit the performance" and that the non-alignment, "rather than the level
of eddy viscosity", matters more (§III C, §IV). The conclusion rests on
these correlations, angle PDFs and eigenvalue ratios; see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md).

[Maejima & Kawai (2025)](/sources/maejima-2025.md) (§1) give the same
reason for preferring other closures in coarse wall turbulence. The
eddy-viscosity approach "expresses the SGS stresses as scalar multiples of
the velocity gradient tensor, which does not hold well in real turbulence",
and they recall Jiménez & Moser on the poor performance of eddy-viscosity
models in coarse wall-bounded LES.

The dynamic form is also the baseline of the transformer neural-operator
surrogate of [Li et al. (2024)](/sources/li-2024.md) (§II B, Eq. 7, with
$\tau^d_{ij}=-2C_s^2\Delta^2\lvert\bar S\rvert\bar S_{ij}$). There it is
the most accurate model for the isotropic-turbulence spectrum at high
wavenumbers and for the rms statistics (§V A). [Cao et al. (2024)](/sources/cao-2024.md)
(§3.3) state, citing earlier work, that constrained LES performs "slightly
better than the explicit LES with Smagorinsky model" in a supersonic
channel.

A learned stress shows the same alignment when it is given only the strain:
the neural-network SGS model of [Kang et al. (2023)](/sources/kang-2023.md)
(§3.1, Table 3, Figs. 4–6) with $\bar S_{ij}$ as its only input returns a
stress with correlation $-0.82$ between $\bar S_{12}$ and $\tau_{12}$,
against $-0.28$ in filtered DNS of forced isotropic turbulence; it "only
rescales the given input", predicts no backscatter, and performs a
posteriori almost identically to the dynamic Smagorinsky model.

[Domaradzki (2024)](/sources/domaradzki-2024.md) (§3.1) quotes "the
value around 0.4 found for the standard Smagorinsky model" for the
correlation of subgrid transfers, against 0.81 between the subgrid
transfer of the
[autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md),
an eddy-viscosity model too, and that of the similarity stress it is built
from; the paper sets this against the common view that eddy-viscosity
models correlate poorly with exact subgrid quantities. Domaradzki adds
that Smagorinsky and Chollet–Lesieur models must assume the
inertial-range form and the Kolmogorov constant, which the autonomous
model predicts (§3.3), and recalls that the spectral viscosity of the
Smagorinsky model is approximately uniform in wavenumber (Siegel &
Domaradzki 1994; for the dynamic form, Thiry et al. 2019), consistent with
the nearly constant a posteriori spectral viscosity found by Vicente Cruz
& Lamballais (2023, §6.3; see
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)).

**Isotropic turbulence a posteriori.** In decaying isotropic turbulence at
$Re_\lambda=240$, the authors call Smagorinsky "one of the most dissipative
models", evident in the spectra, and the Smagorinsky-based models deviate
more than the fractional model from filtered DNS in the third-order
structure function (Seyedi & Zayernouri
2022, §IV, Figs. 8, 10); a priori its stress correlation is below that of
the [fractional SGS model](/methods/fractional-sgs-model.md) (§III.2,
Fig. 4).

**Smagorinsky against learned and implicit closures.** In DG LES of
forced isotropic turbulence at $Re_\lambda\approx180$ with $N=5$ and 7,
static Smagorinsky ($C_s=0.17$) is over-dissipative near the resolution
limit, no-model LES piles energy up, and the learned element-wise
coefficient matches the DNS spectrum (Kurz et al. 2023, §4.2, Fig. 6);
this repeats the over-damping that Beck & Kurz (2023) report at $N=5$.
On the Taylor–Green vortex at $Re=1600$ ($32^3$ elements, $N=3$),
Smagorinsky and [Vreman](/methods/vreman-model.md) models adapted to DG
give a lower peak of the dissipation rate, a higher dissipation rate before
$t/t_c=8$ ($t_c$ the convective time) and significant dissipation at mid
wavenumbers, and are "clearly" inferior to
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md)
([Kou et al. 2023](/sources/kou-2023.md), §4.2, Fig. 12); the constants and
filter width are not printed. The dynamic form is the baseline of the
learned closures of Kang et al. (2023), [Sirignano & MacArt (2023)](/sources/sirignano-2023.md)
(§3.2, Eq. 3.4) and of the WMLES of [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md),
and of the a priori analysis of [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md)
(§IV B); results are on the [dynamic procedure](/methods/dynamic-procedure.md)
page.

## Qualifications

- Cheylan et al. (2023, Eq. 37) print the viscosity as
  $\nu_t=(C_S^2\Delta x)^2(\lvert S\rvert-\mathcal S)$, with $C_S$ called "the
  Smagorinsky constant" and $\mathcal S$ the time-filtered strain norm;
  with the registry form $(C_s\Delta)^2\lvert\bar S\rvert$ the constant
  would appear squared once, not twice *(compiler check, not in the
  sources)*. No value is printed, so the convention cannot be checked
  against a number.

- Flad & Gassner (2017) use two conventions for the coefficient: App. A and
  App. B print $\nu_t=C_S^2\Delta^2\lvert S\rvert$, App. C and App. D print
  $C_S\Delta^2\lvert S\rvert$, with "$C_S=0.13^2$" in App. C (i.e.
  $C_s=0.13$ in the registry form). They do not state whether $\lvert S\rvert$ carries the
  factor 2.

- Abe (2021) labels two damping functions with the same symbol $f_S$
  (Eq. 4 and Eq. 20) and says so in §IV E; the a priori test of §IV C cites
  Eq. (4).
- Prakash et al. (2022) do not define $\lvert\bar S\rvert$, and
  Mateo-Gabín et al. (2022) do not define the $\lvert\mathsf S\rvert$ of
  their Eq. (125). The same symbol appears in their Eq. (25), whose
  dissipation $\mu_a\big(2\lvert\mathsf S\rvert^2-\tfrac23(\nabla\cdot\boldsymbol u)^2\big)$
  equals the Navier–Stokes value only if
  $\lvert\mathsf S\rvert^2=S_{ij}S_{ij}$; if Eq. (125) uses it in the same
  sense, their $C_S=0.2$ corresponds to the registry's
  $C_s=0.2\cdot2^{-1/4}\approx0.17$ *(compiler check, not in the sources)*.
  Mateo-Gabín et al. write the viscosity $\mu_a=C_S^2\Delta^2\lvert\mathsf S\rvert$
  without a density factor, immaterial for their test with $\rho\approx1$.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.A, Eqs. (4)–(5).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §4.1, Eqs. (24)–(26), (47); §6.3, Figs. 7–12; §6.5; §7.3.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III B, Eqs. (9)–(15); §V A–B, Figs. 8–11.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1, Fig. 3; §4, Fig. 7; §5.1; App. A–C.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §4.4.1, Eqs. (26)–(27); App. B.5, Table B.5; App. G.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.2, Eq. (2.8); §6.3; §8.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II B–C; §V D.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II A (LESGO SGS models).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A.
- [Abe (2021)](/sources/abe-2021.md) — §II A, Eqs. (3)–(4); §IV C–E, Eqs. (18)–(20), Figs. 9–10, 12; §V.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §II, Eq. (3).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §6.1, Eq. (125), Fig. 4.
- [Basile et al. (2023)](/sources/basile-2023.md) — Table 1.
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §II, Eqs. (3)–(4); §III.2, Fig. 4; §IV, Figs. 8, 10.
- [Kim et al. (2022)](/sources/kim-2022.md) — §III C; §III E, Eq. (27), Figs. 15–20, Table IV; §IV.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II, Eq. (9).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §3.3, Eq. (19); §3.4–3.5; §4.2–4.4, Figs. 6, 8.
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §2.7, Eqs. (37)–(38).
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1.3.
- [Kang et al. (2023)](/sources/kang-2023.md) — §3.1, Table 3, Figs. 4–6.
- [Kou et al. (2023)](/sources/kou-2023.md) — §4.2, Fig. 12.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §3.2, Eq. (3.4).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.2.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §IV B, Eq. (22).
- [Duan & Wang (2024)](/sources/duan-2024.md) — §2.1–2.2, Eqs. (8)–(10); §3, Eqs. (26)–(30); §5.1, §5.3, Figs. 5–10.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §II.A, Eqs. (11), (14); §III; App. C.
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — §4.1.1, Eqs. (54)–(55); §4.6–4.7, Fig. 13.
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — §2.2, Eq. (2.6); §4.1.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.A.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §3.1; §3.3.
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §2.1, Eq. (4); §3.1, Eq. (8); §5.2; §6.2; §7.2; §8.2, Table 2.
- [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §2.1, Eq. (2.4); §2.3; §3.3; App. C.
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §2.1, Eq. (5); §2.5, Eq. (17); §3.1–3.2; §4, Eqs. (25)–(26), Table 4, Figs. 19–23; §6.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.D.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §II B, Eqs. (7)–(8); §V A 2.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv v1: §3.3.
