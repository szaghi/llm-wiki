---
type: Method
title: "WALE model"
description: "The wall-adapting local eddy-viscosity (WALE) model builds a static subgrid eddy viscosity from an invariant of the squared resolved velocity gradient that vanishes in pure shear; the sources print its formula with constants 0.325 and 0.5, find its dissipation small beside numerical dissipation, and find it the least dissipative of three models in high-order LES."
status: established
aliases: [WALE, wall-adapting local eddy-viscosity model, Nicoud–Ducros model]
tags: [les, sgs-model, eddy-viscosity, numerical-dissipation]
timestamp: 2026-10-26T10:06:00Z
---

# WALE model

The **wall-adapting local eddy-viscosity (WALE) model**, attributed by the
sources to Nicoud & Ducros (1999), closes the deviatoric
[subgrid stress](/definitions/large-eddy-simulation.md) with a static
eddy viscosity, $\tau^d_{ij}=-2\nu_t\bar S_{ij}$, built from both the
strain and the rotation of the resolved field. In the form printed by
[Lederer et al. (2023)](/sources/lederer-2023.md) (§3.1), written with the
resolved velocity,

$$\nu_t=(C_w\Delta)^2\,\frac{(\mathcal G^2)^{3/2}}{(\bar S_{ij}\bar S_{ij})^{5/2}+(\mathcal G^2)^{5/4}},$$

$$\mathcal G^2=\tfrac16\Big[(\bar S_{kl}\bar S_{kl})^2+(\bar\Omega_{kl}\bar\Omega_{kl})^2\Big]+\tfrac23\,\bar S_{kl}\bar S_{kl}\,\bar\Omega_{mn}\bar\Omega_{mn}+2\,\bar S_{ik}\bar S_{kj}\bar\Omega_{jl}\bar\Omega_{li},$$

with $\mathcal G^2$ (page-local) the invariant of "the square of the
velocity-gradient tensor" on which the authors say the model is based,
$C_w$ the model constant and $\Delta$ the filter width. Lederer et al.
describe the model as accounting for strain and rotation and capturing the
near-wall behaviour "without dynamic procedure or damping functions".
Because $\bar\Omega$ appears only in pairs, the sign convention of the
rotation tensor does not matter *(compiler check, not in the sources)*.

[Duan & Wang (2024)](/sources/duan-2024.md) (§2.3, Eqs. 11–14) print the
model through the traceless symmetric part of the squared velocity
gradient, $\mathcal S_{ij}=\tfrac12(g_{ik}g_{kj}+g_{jk}g_{ki})-\tfrac13\delta_{ij}g_{kl}g_{lk}$
with $g_{ij}=\partial_i\bar u_j$ (page-local; their $S^d_{ij}$), or
equivalently
$\mathcal S_{ij}=\bar S_{ik}\bar S_{kj}+\bar\Omega_{ik}\bar\Omega_{kj}-\tfrac13\delta_{ij}(\bar S_{mn}\bar S_{mn}-\bar\Omega_{mn}\bar\Omega_{mn})$,
and write $\nu_t=(C_w\Delta)^2(\mathcal S_{ij}\mathcal S_{ij})^{3/2}/[(\bar S_{ij}\bar S_{ij})^{5/2}+(\mathcal S_{ij}\mathcal S_{ij})^{5/4}]$.
This is the formula above with $\mathcal G^2=\mathcal S_{ij}\mathcal S_{ij}$:
expanding the square of their second form gives the invariant of Lederer
et al. term by term *(compiler check, not in the sources, verified on a
random traceless gradient)*. Duan & Wang state the advantages as an
eddy viscosity containing both strain and rotation, reduced near the wall
with the proper asymptotic behaviour.

## Behaviour in pure shear

For a unidirectional shear $\bar u(y)$ with $\partial_y\bar u=a$:
$\bar S_{kl}\bar S_{kl}=\bar\Omega_{kl}\bar\Omega_{kl}=a^2/2$ and
$\bar S_{ik}\bar S_{kj}\bar\Omega_{jl}\bar\Omega_{li}=-a^4/8$, so
$\mathcal G^2=a^4/12+a^4/6-a^4/4=0$ and $\nu_t=0$: the model switches
itself off in laminar shear and at a wall where the flow is locally
parallel *(compiler check, not in the sources)*. Lederer et al. (2023, §4.1)
state that no eddy viscosity is applied in the viscous sublayer of their
channel LES, which all their cases capture accurately.

## Constants and filter widths

| $C_w$ | $\Delta$ | Context | Source |
|---|---|---|---|
| 0.5 | $\sqrt[3]{\Delta x\Delta y\Delta z}/(N+1)$, element size over $N+1$ ($N$ the paper's $k$) | eddy viscosity of a projection-based variational multiscale model in a hybrid mixed finite-element method | Lederer et al. (2023), §3.1 |
| 0.325 | not printed | second-order finite-volume LES (OpenFOAM), choice justified in the authors' earlier paper | [Saini et al. (2023)](/sources/saini-2023.md), §2.1, Table 1 |
| not printed | not printed | compressible LES of a fan stage in AVBP | [Lewis et al. (2023)](/sources/lewis-2023.md), §3.2.1 |
| 0.325 quoted ("often estimated"), value used not printed | $V^{1/3}$, $V^{1/3}/\sqrt{N+1}$, $V^{1/3}/(N+1)$ for an element of volume $V$ | high-order flux-reconstruction LES, wall-resolved and wall-modelled | Duan & Wang (2024), §2.3, §3 |
| not printed (model cited to an application paper) | not printed | compressible finite-difference LES of channel and periodic hill | [Wang et al. (2024)](/sources/wang-2024.md), §3.2–3.3 |
| not printed | not printed | second-order OpenFOAM reference LES of a low-Reynolds-number backward-facing step, training data for a learned RANS closure | [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md), §3.2 |

The printed constants belong to different codes, filter widths and
uses (a small-scale VMS viscosity against a classical LES model); no
source calibrates the value. Duan & Wang calibrate the filter width
instead (below).

## Use in the sources

- **Variational multiscale model on DG-type ILES.** Lederer et al. (2023,
  §3.1, §4.1, §5.1, Figs. 1, 6, 8–9) let the WALE viscosity act only on the
  small resolved scales: the strain is reduced by its $L^2$ projection on
  element-wise polynomials of degree $m$ ($m=1$ for $N=3$, $m=3$ for $N=6$).
  In channel flow at $Re_\tau=392.24$ the model gives about the same
  statistics as the no-model [implicit LES](/definitions/implicit-les.md)
  at the finer resolutions, where in the authors' explanation the eddy
  viscosity vanishes with increasing resolution, and slightly worse ones at the coarsest: more damping, an
  under-resolved buffer layer and an offset in $u^+$; the bulk-Reynolds-number
  error is 16.3%, 4.7% and 2.7% for $N=3$ on $6^3$, $12^3$ and $16^3$
  elements, against 13.4%, 3.1% and 1.1% without model (Table 2). The
  spectra at $y^+=5$ and 40 show added dissipation at mid-to-high
  wavenumbers. On the [periodic hill](/benchmarks/periodic-hill.md) at
  $Re=2800$ it brings slight to no improvement. The authors conclude that
  the explicit model "can harm the implicit dissipation mechanism" (§6).
- **Measured against numerical dissipation.** Saini et al. (2023, §5,
  Figs. 7–16) split the non-viscous dissipation of a second-order
  finite-volume LES with WALE into the model part and the numerical part
  (the residual of the discrete resolved-energy budget). The numerical
  part is 65–75% (Taylor–Green vortex at $Re=1600$) and 80–90% (combustor
  port flow) of it; $\mathcal E_{\mathrm{num}}$ is 4–12 times the WALE
  dissipation in the turbulent subdomains of the port flow
  ($\mathcal E_{\mathrm{num}}$ page-local, the numerical dissipation rate
  integrated over a subdomain). In the downstream subdomain, refining from
  16 to 48 million points lowers the normalized WALE and numerical
  dissipation by 40% and 30%. The
  authors' hypothesis for the small model share is that numerical
  dissipation already damps the velocity gradients on which WALE acts
  (§5.2). See [numerical dissipation](/properties/numerical-dissipation.md).
- **Turbomachinery noise.** Lewis et al. (2023, §3.2–3.3) run two
  wall-modelled LES of the [ACAT1 fan stage](/benchmarks/acat1-fan-stage.md)
  with WALE in the compressible Lax–Wendroff code AVBP (95 and 210 million
  cells) with an algebraic wall law; they attribute the differences between
  the two runs, such as a stator separation present only on the coarser
  mesh, to wall-mesh refinement.
- **High-order flux reconstruction, wall-resolved and wall-modelled.**
  Duan & Wang (2024, §5) compare WALE with the
  [Vreman](/methods/vreman-model.md) and
  [Smagorinsky](/methods/smagorinsky-model.md) models in the FR/CPR solver
  hpMusic with three filter widths (d1 $V^{1/3}$, d2 $V^{1/3}/\sqrt{N+1}$,
  d3 $V^{1/3}/(N+1)$; see the Vreman page). WALE is the least dissipative
  of the three on the inviscid and viscous
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (§5.1, Figs.
  5–7). In the wall-resolved channel at $Re_\tau=180$ ($N=3$) it matches
  DNS in the viscous sublayer and, with d2 or d3, over the whole layer,
  slightly better than Vreman (§5.3, Figs. 9–10). In the wall-modelled
  channel at $Re_\tau=5200$ it is inconsistent across degrees: best with
  d1 at $N=2$ (where even d1 lacks dissipation), better with all widths at
  $N=3$ and 4 (best d1), best with d2 at $N=5$, where lowering the eddy
  viscosity from d1 to d3 shifts the velocity profile upwards, reversing
  the trend of $N=2$–4; the authors call this "strange" and leave it
  unexplained (§5.4, Figs. 11–14). At $Re_\tau=544$, $N=3$, d1 is again
  best for WALE (Fig. 15). They therefore recommend Vreman rather than WALE
  for high-order wall-modelled LES (§6).
- **TKE budgets with two convective schemes.** [Wang et al. (2024)](/sources/wang-2024.md)
  (§3.2–3.3) use WALE in compressible LES of the
  [channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=180$,
  $M_b=0.2$ and of the [periodic hill](/benchmarks/periodic-hill.md) at
  $Re_h=10\,595$ to compare a second-order kinetic-energy-preserving
  central scheme with a sixth-order upwind one; see
  [numerical dissipation](/properties/numerical-dissipation.md).
- **Reference LES of other studies.** Agrawal & Koutsourelakis (2024,
  §3.2) generate the mean fields that train their
  [model-form-uncertainty](/definitions/model-form-uncertainty.md) closure
  with an OpenFOAM WALE LES (1,428,920 degrees of freedom, CFL < 0.3) of a
  [backward-facing step](/benchmarks/backward-facing-step.md) at
  $Re=300$–1100. Among the periodic-hill studies tabulated by
  [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md)
  (Tables 2–3), a DG ($N=3$) WALE LES of De La Llave Plata et al. gives a
  reattachment at $x/h=3.9$ ($Re=10\,600$) and 3.2 ($Re=37\,000$), against
  Rapp's measured 4.21 and 3.76.
- **Listed in codes.** WALE is among the explicit LES models of the DG code
  [HORSES3D](/software/horses3d.md) ([Ferrer et al. 2023](/sources/ferrer-2023.md),
  §4.1), with no formula printed. [Haering et al. (2022)](/sources/haering-2022.md)
  (§V D) list it with Smagorinsky and [Vreman](/methods/vreman-model.md)
  among fluctuating-viscosity models whose correlation with the strain
  adds to the mean stress (see [active model split](/methods/active-model-split.md)).

## Qualifications

- Lederer et al. (2023) define $\epsilon^2(u_h)=\epsilon(u_h):\epsilon(u_h)$
  for the strain but leave the rotation square $\omega^2(u_h)$ undefined;
  it is read here as $\bar\Omega_{kl}\bar\Omega_{kl}$ by analogy. They
  write the products $\epsilon^2\epsilon^2$ and $\omega^2\omega^2$ as
  products of scalars, as transcribed above.
- Only Lederer et al. print the formula; Saini et al. and Lewis et al. use
  the model without it, so the page cannot check whether their
  implementations use the same invariant or filter width.

# Citations

- [Lederer et al. (2023)](/sources/lederer-2023.md) — §3.1, Eqs. (10)–(14) and WALE formula; §4.1, Figs. 1, 6, Table 2; §5.1, Figs. 8–9; §6.
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, Table 1; §5.1–5.2, Figs. 7–16; §6.
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2.1; §3.3.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §2.3, Eqs. (11)–(14); §3, Eqs. (28)–(30); §5.1–5.4, Figs. 5–15; §6.
- [Wang et al. (2024)](/sources/wang-2024.md) — §3.2–3.3.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §3.2.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — Tables 2–3.
