---
type: Method
title: "Dynamic tensor-coefficient Smagorinsky model"
description: "The dynamic tensor-coefficient Smagorinsky model (DTCSM) replaces the scalar Smagorinsky coefficient by a traceless-constrained coefficient tensor with four components fitted dynamically, giving a non-Boussinesq stress that dissipates like dynamic Smagorinsky and converges monotonically in wall-modelled LES of the Gaussian bump."
status: established
aliases: [DTCSM, tensor-coefficient Smagorinsky model, non-Boussinesq dynamic SGS model]
tags: [les, sgs-model, eddy-viscosity, wmles, separated-flow]
timestamp: 2026-10-27T15:49:00Z
---

# Dynamic tensor-coefficient Smagorinsky model

The **dynamic tensor-coefficient Smagorinsky model (DTCSM)** of
[Agrawal et al. (2022)](/sources/agrawal-2022.md) is a non-Boussinesq
subgrid-scale model: the scalar coefficient of the
[Smagorinsky model](/methods/smagorinsky-model.md) is replaced by a
$3\times3$ tensor $C_{ij}$ (page-local symbol), so the model stress need
not be aligned with the resolved strain. The coefficients are fitted by the
[dynamic procedure](/methods/dynamic-procedure.md). The starting point is
the tensor-coefficient form of Moin (1993), which Agrawal et al. cite
(§III.A, Eq. 11):

$$\tau^d_{ij}=-\big(C_{ik}\bar S_{kj}+C_{jk}\bar S_{ki}\big)\lvert\bar S\rvert\Delta^2 ,$$

which has nine coefficients and is not traceless in general.

## Constraints and dissipation

Agrawal et al. (§III.A, Eq. 12; App. A) impose

$$C_{11}=C_{22}=C_{33},\qquad C_{ij}=-C_{ji}\ (i\ne j),$$

so that the trace $-2C_{ik}\bar S_{ki}\lvert\bar S\rvert\Delta^2$ vanishes
for incompressible flow; four coefficients $C_{11},C_{12},C_{13},C_{23}$
remain. With $C_{ij}=C_{11}\delta_{ij}+C^a_{ij}$, $C^a$ antisymmetric, and
$\lvert\bar S\rvert C^a_{ij}=-\Lambda\bar\Omega_{ij}$ (page-local $\Lambda$),
the model becomes (App. C, Eq. C3)

$$\tau^d_{ij}=-2C_{11}\Delta^2\lvert\bar S\rvert\bar S_{ij}-\Lambda\Delta^2\big(\bar S_{ik}\bar\Omega_{kj}-\bar\Omega_{ik}\bar S_{kj}\big),$$

a Smagorinsky term with $C_{11}$ in place of $C_s^2$ plus the strain–rotation
term of the two-term velocity-gradient expansion of Lund & Novikov
(cited). Agrawal et al. write the rotation-rate tensor as $R_{ij}$
without defining it; it is written $\bar\Omega_{ij}$ here. Only $C_{11}$
dissipates resolved energy (§III.A): the second term gives
$\Pi$-contribution
$\Lambda\Delta^2\,\mathrm{tr}(\bar S\bar S\bar\Omega-\bar S\bar\Omega\bar S)=0$
by cyclicity of the trace *(compiler check, not in the sources)*. The model
thus [dissipates](/definitions/energy-backscatter.md) like a Smagorinsky
model while its antisymmetric part redistributes stress without energy
exchange.

## Dynamic fit

With the Germano identity at test-to-grid width ratio 2, Agrawal et al.
(Eq. 13, App. B) obtain $L_{ij}=\Delta^2(C_{ik}M_{kj}+C_{jk}M_{ki})$ with
$M_{ij}$ as in the [dynamic procedure](/methods/dynamic-procedure.md) (their
$L$ and $M$ carry the opposite sign, which cancels). Absorbing $\Delta^2$
into $C$, the system is (Eq. B2)

$$\begin{pmatrix}L_{11}\\L_{22}\\L_{33}\\L_{12}\\L_{13}\\L_{23}\end{pmatrix}=
\begin{pmatrix}
2M_{11}&2M_{12}&2M_{13}&0\\
2M_{22}&-2M_{12}&0&2M_{23}\\
2M_{33}&0&-2M_{13}&-2M_{23}\\
2M_{12}&M_{22}-M_{11}&M_{23}&M_{13}\\
2M_{13}&M_{23}&M_{33}-M_{11}&-M_{12}\\
2M_{23}&-M_{13}&-M_{12}&M_{33}-M_{22}
\end{pmatrix}
\begin{pmatrix}C_{11}\\C_{12}\\C_{13}\\C_{23}\end{pmatrix},$$

solved by normal equations (Eqs. B3–B4) with spatial averaging in
homogeneous directions (HIT, channel) or temporal averaging (bump). Like
dynamic Smagorinsky, the only input is the test-to-grid filter-width ratio.

**Limits.** In well-resolved laminar flow $L_{ij}\to0$ and the
coefficients vanish (§VI). Near a wall, with a test filter that does not act
in the wall-normal direction, $C_{11}\sim y^{+3}$, $C_{12}\sim y^{+2}$,
$C_{23}\sim y^{+2}$, $C_{13}\sim0$, so $\tau_{12}\sim y^{+3}$ without
damping functions (§VI, App. B).

## Results

- **A priori.** On filtered channel DNS at $Re_\tau=395$ and 2000 (filter
  width three grid sizes), DTCSM has higher stress-tensor correlations than
  DSM, improving with $Re_\tau$ and most near the wall; dissipation
  correlations are identical, since only the Smagorinsky-type part
  dissipates (§V, Figs. 1–2). The Bardina [similarity model](/methods/scale-similarity-model.md)
  correlates better a priori but under-dissipates a posteriori.
- **Isotropic turbulence.** Decaying HIT at $Re_\lambda=70$ ($32^3$): decay
  exponent about $-1.35$ for DTCSM and DSM against $-1.37$ for filtered DNS.
  Forced HIT at $Re_\lambda=315$ and HIT at $Re_\lambda\to\infty$ ($128^3$):
  $k^{-5/3}$ recovered (§VII.A–C).
- **WMLES channel** at $Re_\tau=4200$ ($\Delta^+\approx200$, 20 points per
  half-height, equilibrium wall model matched at the second off-wall point):
  the log-layer slope improves slightly, the Kármán-constant error drops
  from 7% (DSM) to 5% against the DNS value 0.38, near-wall intensities are
  lower, and no clipping is needed where DSM needs it (§VII.D, Figs. 8–10).
- **Cost** up to about 1.15 times DSM: 15 against 13 GPU-node-hours per
  flow-through on the 52-million-cell spanwise-periodic bump, 112 against
  100 on the 452-million-cell 3D bump, on NVIDIA V100 nodes (§IX,
  Tables IV–V).

## Gaussian bump (inline)

The Boeing Gaussian speed bump is a smooth-body separation benchmark. In
the form printed by Agrawal et al. (§VIII, Eq. 16) its height is
$h(x,z)=\tfrac{h_0}{2}e^{-(x/x_0)^2}\{1+\mathrm{erf}([L/2-2z_0-|z|]/z_0)\}$
with $h_0=0.085L$ and $x_0=0.195L$, where $L$ is the bump width. The
spanwise-periodic variant uses $h_0e^{-x^2/x_0^2}$. Agrawal et al. run
wall-modelled LES in [charLES](/software/charles.md) on Voronoi grids
(see [wall-modelled LES](/methods/wall-modelled-les.md)):

- **Spanwise-periodic bump**, $Re_L=2\times10^6$, grids of 3, 12 and 52
  million cells, reference the quasi-DNS of Uzun & Malik. DTCSM converges
  monotonically towards the reference $C_f$, especially in the separation
  region, whereas DSM and Vreman separate on the coarse grid, lose the
  separation on the medium grid and recover it on the fine one. On the fine
  grid DTCSM recovers the favourable-pressure-gradient $C_f$ peak that DSM
  underpredicts (Figs. 13–14).
- **3D bump**, $Re_L=3.41\times10^6$, 29, 117 and 452 million cells,
  references the surface pressure of Williams et al., skin friction of Gray
  et al. and oil flow. On the fine grid ($y^+\sim30$ at the first cell)
  both dynamic models separate with a bubble size agreeing with Gray et
  al.; DTCSM is monotonic in $C_f$ and $C_p$ and gives the best $C_p$. Both
  dynamic models capture the apex $C_p$ rise and the counter-rotating
  vortex pair, which the [Vreman model](/methods/vreman-model.md) misses
  (Figs. 15–19). The suction peak is mainly inviscid; a free-slip run
  (not shown) also predicts it.

Each of the two geometries is run on three grid levels.

## Place among anisotropic SGS models

[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (§I) cite the
model (their ref. [9]) among the non-eddy-viscosity or anisotropic SGS
models that "improve the prediction of the statistics of turbulent flows"
(refs. [4–11]) and among the anisotropic models that "prohibit backward
scatter" (refs. [4–9]), from which they conclude that "additional stress,
apart from energy transfer, can improve the performance of LES". In the
DTCSM the antisymmetric part of the coefficient tensor is such a stress
(see Constraints and dissipation). Their own analysis of
such energy-transfer-free stresses in coarse channel LES is on
[energy backscatter](/definitions/energy-backscatter.md).

## Qualifications

- Agrawal et al. call the constraints of Eq. (12) "realizability
  constraints" (§III.A, App. C), but derive them as tracelessness
  constraints (App. A, "Proof of tracelessness"); Eq. (12) constrains
  the trace only, not the positive semi-definiteness of the stress.
- §III.A speaks of "five independent equations with four coefficients",
  while Eq. (B2) has six rows. With $M_{kk}=0$ the first three rows of the
  right-hand side sum to zero, so the fit can match only the deviatoric part
  of $L_{ij}$ *(compiler check, not in the sources)*; the paper does not say
  whether $L_{ij}$ is made traceless before the solve.
- §VIII.B says that the $C_f$ trough moves "towards DNS" on the 3D bump,
  whose reference is the experiment of Gray et al.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §III.A, Eqs. (11)–(13); §V, Figs. 1–2; §VI; §VII.A–D, Figs. 3–10; §VIII, Eq. (16), Figs. 13–19; §IX, Tables IV–V; Apps. A–C, Eqs. (B2)–(B4), (C3).
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §I; §II A.
