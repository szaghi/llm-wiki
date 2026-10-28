---
type: Method
title: "Anisotropic minimum-dissipation model"
description: "The anisotropic minimum-dissipation (AMD) model is an eddy-viscosity subgrid model built from directional grid spacings and switched off where the resolved flow feeds no energy to the subgrid; the sources give its constant, use it under learned wall models, compare it with dynamic and learned closures, and find it insensitive to cell anisotropy in bump WMLES."
status: established
aliases: [AMD model, AMD, minimum-dissipation model, Rozema model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-28T07:08:00Z
---

# Anisotropic minimum-dissipation model

The **anisotropic minimum-dissipation (AMD) model** of Rozema et al.
(2015, cited by the sources) is an eddy-viscosity closure of the
deviatoric [subgrid stress](/definitions/large-eddy-simulation.md),
$\tau^d_{ij}=-2\nu_t\bar S_{ij}$, whose viscosity uses the grid spacing of
each direction separately and vanishes where the resolved velocity gradient
does not feed the subgrid scales. As printed by
[Sirignano & MacArt (2023)](/sources/sirignano-2023.md) (§3.2, Eq. 3.5),
with summation over $k$, $l$, $m$,

$$\nu_t=C_{\mathrm{AMD}}\,\frac{\max\!\big[-\Delta_k^2\,\partial_k\bar u_i\,\partial_k\bar u_j\,\bar S_{ij},\,0\big]}{\partial_l\bar u_m\,\partial_l\bar u_m},$$

where $\Delta_k$ (registry §11) is the mesh spacing in direction $k$ of a
non-uniform mesh, and $C_{\mathrm{AMD}}=0.3$ "for second-order central
discretizations". The isotropic part of the stress is absorbed into the
pressure (§3.2, Eq. 3.3).

## Structure

- **Directional length scales.** The spacings enter inside the sum over
  derivative directions, not through one scalar filter width, which is the
  property the sources cite: the model "is known to perform well in highly
  anisotropic grids" ([Bae & Koumoutsakos 2022](/sources/bae-2022.md),
  Methods p. 13) and "is known to outperform the DS model on highly
  anisotropic meshes" (Sirignano & MacArt 2023, §3.2, citing Zahiri &
  Roohi). The scalar-width problem it avoids is discussed under
  [high-aspect-ratio cells](/definitions/large-eddy-simulation.md).
- **No backscatter, switched off in non-transferring regions.** The
  $\max[\cdot,0]$ makes $\nu_t\ge0$, so the model never
  [backscatters](/definitions/energy-backscatter.md), and $\nu_t=0$ where
  the numerator is negative.
- **Relation to the gradient model.** The numerator is, up to the factor
  12, the local energy flux $\Pi$ of the [gradient model](/methods/gradient-model.md)
  with directional widths, $\tau_{ij}=\tfrac1{12}\sum_k\Delta_k^2\partial_k\bar u_i\partial_k\bar u_j$
  (the form printed by [Qi et al. (2022)](/sources/qi-2022-b.md), Eq. 3.12,
  with $C_0=1/12$); hence
  $\nu_t=12\,C_{\mathrm{AMD}}\max(\Pi_{\mathrm{grad}},0)/(\partial_l\bar u_m\partial_l\bar u_m)$
  with $\Pi_{\mathrm{grad}}$ (page-local) that flux, so only its positive
  (forward-scatter) part enters the viscosity *(compiler check, not in
  the sources)*.
- **Minimum dissipation.** [Vela-Martín (2022)](/sources/velamartin-2022.md)
  (§8) cites minimum-dissipation models (Verstappen; Rozema et al.) as already embodying the idea that strong positive fluctuations
  of the flux need not be modelled, in line with its own
  backscatter-free reformulation of the subgrid flux. [Prakash et al. (2022)](/sources/prakash-2022.md)
  (§II) list AMD among the remedies for a flow-dependent Smagorinsky
  coefficient, as a model that uses the minimum eddy viscosity.

## As the solver model of learned wall models

- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Methods p. 13) train
  reinforcement-learning wall models in a staggered second-order
  finite-difference channel LES with the AMD model, so the learned policy
  adapts to that solver and SGS model; see
  [machine-learning wall models](/methods/machine-learning-wall-model.md).
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) (§II A, App. B,
  Fig. 18) use AMD as the baseline SGS model of their
  [LESGO](/software/lesgo.md) half-channel WMLES. Replacing it by the
  Lagrangian scale-dependent [dynamic model](/methods/dynamic-procedure.md)
  changes the mean velocity at $Re_\tau=5200$ very little, for the
  equilibrium and the learned wall models alike, "indicating that the
  learned models are not significantly adjusted to compensate for
  deficiencies in the SGS model".

## Against dynamic Smagorinsky and learned closures

Sirignano & MacArt (2023) compare no-model LES, dynamic Smagorinsky (DS),
AMD and two adjoint-trained [neural-network closures](/methods/neural-network-sgs-model.md)
on rectangular prisms in confined cross-flow (aspect ratio 1, 2, 4;
$Re_0=1000$ and 2000 on the prism height; LES on $1/64$ or $1/512$ of the
DNS points; second-order staggered finite differences, no wall model):

- **Drag** (§4.1, Table 2). Drag coefficients, filtered DNS / no model /
  DS / AMD / learned model trained on AR 1 / learned model trained on AR 2
  at $Re_0=2000$: 2.45 / 1.88 / 2.15 / 2.53 / 2.43 / 2.51 (AR 1,
  $Re_0=1000$); 1.94 / 1.61 / 1.65 / 1.96 / 1.90 / 1.95 (AR 2, 1000);
  2.09 / 1.62 / 1.68 / 1.89 / 1.84 / 1.96 (AR 2, 2000); 1.61 / 1.53 / 1.54
  / 1.67 / 1.54 / 1.61 (AR 4, 1000). AMD is the closest of the three
  non-learned models to filtered DNS in all four cases *(compiler check,
  not in the sources)*; the authors state that in all cases it "is
  outperformed by the in-sample or nearest DL model".
- **Boundary layers** (§4.2, Figs. 8–9). No-model and DS LES give
  "incorrectly large" resolved Reynolds stresses where filtered DNS tends
  to zero; AMD improves this but keeps a larger scatter of the normal
  resolved stresses than the learned closures.
- **Near-wall mean profiles** (§4.3, Fig. 10). With the first points
  outside $y^+=10$ in most places, the learned closures "generally slightly
  outperform the AMD model and dramatically outperform" DS and no-model
  LES. For AR 2 at $Re_0=2000$, AMD is not more accurate than DS or no-model
  LES for the cross-stream velocity.
- **Unseen geometries** (§6, Figs. 13–14), run at $Re_0=1000$ in a second
  solver: AMD is the least accurate model for an equilateral triangular
  prism, and, with no-model LES, predicts two recirculation regions behind
  a cylinder where DNS and the learned closures have none.

## Separated flow and anisotropic cells in wall-modelled LES

[Zhou & Bae (2024)](/sources/zhou-2024-b.md) compare AMD (constant 0.3,
which "is determined solely by the choice of numerical method", §2.1) with
the [Vreman model](/methods/vreman-model.md) ($c=0.025$ and 0.07),
[dynamic Smagorinsky](/methods/dynamic-procedure.md), a
[mixed similarity model](/methods/scale-similarity-model.md) and no model,
in wall-modelled LES of the spanwise-periodic
[Gaussian bump](/benchmarks/gaussian-bump.md) at $Re_L=2\times10^6$, with
the wall stress of the reference simulation imposed so that only the
subgrid model, the grid and the wall boundary condition vary. The solver
is an incompressible, energy-conserving second-order unstructured finite
volume code.

- **Separation and dissipation** (§3.1, Figs. 4–5, 10–11). On the
  baseline isotropic mesh ($\Delta_c/L=4.76\times10^{-4}$, $\Delta_c$ the
  cube root of the cell volume, page-local) AMD is one of three models that
  separate on the leeward side. Of the eddy-viscosity models it gives the
  largest mean eddy viscosity in the boundary layer, of the order of the
  molecular one, and the largest subgrid dissipation
  $-\tau_{ij}\bar S_{ij}$; subgrid dissipation dominates the viscous one
  throughout the boundary layer.
- **Grid convergence** (§3.1–3.2, Figs. 8, 14). The separation length
  converges to the reference $L_s/L=0.32$ non-monotonically with AMD,
  "leading to a spurious diminishment or shrinking of the separation
  bubble upon mesh refinement", with all three wall boundary conditions.
- **Anisotropic cells** (§3.3, Figs. 17–20). With cells of aspect ratio
  $\Delta_x:\Delta_y:\Delta_z=4:1:2$ at the same cell volume, AMD's $C_p$
  and first-cell velocity are barely changed, whereas Vreman $c=0.025$ and
  the mixed model change over the whole domain. The authors explain this
  by AMD being the only model of the set that does not use the cube root of
  the cell volume as filter width; the explanation is not isolated by a
  separate test.

## Qualifications

- The anisotropic-cell robustness found by Zhou & Bae (2024, §3.3) comes
  with a separation length that converges non-monotonically on isotropic
  grids, so robustness to anisotropy and accuracy for separation are
  distinct properties there.
- The advantage on anisotropic meshes is cited from other work (Bae &
  Koumoutsakos 2022; Sirignano & MacArt 2023, citing Zahiri & Roohi); in Sirignano &
  MacArt's own tests AMD beats DS on drag but is the least accurate model
  on the triangular prism.
- $C_{\mathrm{AMD}}=0.3$ is tied by Sirignano & MacArt to second-order
  central discretizations. Bae & Koumoutsakos (2022) and Vadrot et al.
  (2023b) do not print the formula or the constant.
- Sirignano & MacArt (2023, §7) summarize that the learned closures and AMD
  "had similar error for the RMS velocity components", while §4.2 states
  that the learned closures match filtered DNS more closely "for all cases
  and all statistics": an internal difference in the strength of the claim.
- [Pan & Zhang (2023)](/sources/pan-2023.md) (§I) cite AMD papers, with a
  modulated [gradient model](/methods/gradient-model.md), among "novel
  sub-grid-scale stress models based on pressure gradient", in a
  literature survey of pump LES; they do not use AMD. The formula above,
  as printed by Sirignano & MacArt (2023), contains velocity gradients and
  grid spacings only, no pressure gradient *(compiler check, not in the
  sources)*.

# Citations

- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §3.2, Eqs. (3.3)–(3.5); §4.1, Table 2; §4.2, Figs. 8–9; §4.3, Fig. 10; §6, Figs. 13–14; §7.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Methods, p. 13.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II A; App. B, Fig. 18.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §8.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §II.
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §I.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §3.2, Eq. (3.12) (gradient-model form used in a compiler check).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.1; §3.1, Figs. 4–5, 8, 10–11; §3.2, Fig. 14; §3.3, Figs. 17–20.
