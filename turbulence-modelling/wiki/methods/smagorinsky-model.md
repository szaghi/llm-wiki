---
type: Method
title: "Smagorinsky model"
description: "The Smagorinsky model closes the deviatoric subgrid stress with an eddy viscosity (C_s Δ)²|S̄|; the sources report its constants, filter-width definitions in element methods, its interaction with numerical error, and its a priori and a posteriori behaviour."
status: established
aliases: [Smagorinsky eddy-viscosity model, static Smagorinsky model, SSM, constant-coefficient Smagorinsky]
tags: [les, sgs-model, eddy-viscosity, numerical-dissipation]
timestamp: 2026-10-25T13:42:00Z
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
| about 0.17 | isotropic turbulence, inertial-range resolution (Lilly, as recalled) | Agrawal et al. (2022, §II.A) |
| about 0.1 | shear flows (Deardorff, as recalled) | Agrawal et al. (2022, §II.A) |
| 0.18 | Lilly's analytical value $\pi^{-1}(3C_K/2)^{-3/4}$ with Kolmogorov constant $C_K=1.4$ (page-local symbol), as recalled | Vicente Cruz & Lamballais (2023, §6.5) |
| 0.1 | reference constant for the Taylor–Green vortex and pipe; a dynamic procedure is recalled to give about 0.1 after breakdown | Vicente Cruz & Lamballais (2023, §4.1) |
| 0.17 | static baseline (SSM) in DG LES of forced HIT; the authors remark it is valid in principle only for specific explicit filters | Beck & Kurz (2023, §V) |
| 0.12 | on a dissipation-free split-form DG baseline | [Flad & Gassner (2017)](/sources/flad-2017.md), Fig. 7 |
| 0.17 | small–small VMS variant on DG ILES | Flad & Gassner (2017), Fig. 3 |
| 0.000–0.144 | fitted per grid, filter and formulation on 2D forced turbulence by grid search on the a posteriori error | Agdestein & Sanderse (2025), App. B.5, Table B.5 |
| 0.17 | "the common choice", 3D forced turbulence | Agdestein & Sanderse (2025), App. G.2 |

Lilly's value is consistent with the recalled formula: $\pi^{-1}(2.1)^{-3/4}\approx0.18$
*(compiler check, not in the sources)*. The fitted 2D coefficients of
Agdestein & Sanderse decrease with resolution and reach 0.000 for the
divergence-inconsistent formulation at $\bar n=256$, which the authors
explain by the Smagorinsky term not being divergence-free; they are
error-optimal fits, not model constants.

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
with $C_s=0.5$.

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
  $0.3\nu$ on average near the wall. The damping form is not printed.
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
- **Mixed explicit–implicit.** Smagorinsky added to implicit SVV
  (Vicente Cruz & Lamballais 2023, §6.5); see
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).

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
and LESGO ([Vadrot et al. 2023b](/sources/vadrot-2023-b.md), §II A), and is
the base of the dynamic model used in the wall-modelled LES of
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) (§II.B).

## Qualifications

- Flad & Gassner (2017) use two conventions for the coefficient: App. A and
  App. B print $\nu_t=C_S^2\Delta^2\lvert S\rvert$, App. C and App. D print
  $C_S\Delta^2\lvert S\rvert$, with "$C_S=0.13^2$" in App. C (i.e.
  $C_s=0.13$ in the registry form). They do not state whether $\lvert S\rvert$ carries the
  factor 2.

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
