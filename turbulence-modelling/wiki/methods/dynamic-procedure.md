---
type: Method
title: "Dynamic procedure and the Germano identity"
description: "The dynamic procedure computes subgrid-model coefficients from the resolved field through the Germano identity between grid- and test-filter stresses, solved by least squares with averaging or clipping; the sources report its forms, regularizations, failures near walls and on coarse grids, and its tensorial extension."
status: established
aliases: [dynamic Smagorinsky model, DSM, Germano identity, Germano–Lilly procedure, dynamic SGS model, Lagrangian dynamic model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-25T19:45:00Z
---

# Dynamic procedure and the Germano identity

The **dynamic procedure** replaces a fixed model coefficient by one computed
from the resolved field. The resolved field is filtered a second time with a
**test filter** $\hat\cdot$ of width $\hat\Delta>\Delta$, and the model is
required to be consistent at the two filter levels. The sources attribute
the procedure to Germano et al. (1991), its least-squares form to Lilly
(1992) and the compressible form to Moin et al. (1991). Applied to the
[Smagorinsky model](/methods/smagorinsky-model.md) it gives the **dynamic
Smagorinsky model (DSM)**, the SGS model of the wall-modelled LES of Goc et
al. (2021, tunnel cases), Lozano-Durán et al. (2022) and Agrawal et al.
(2022, as baseline).

## Germano identity

Let $\mathcal T_{ij}=\widehat{\overline{u_iu_j}}-\hat{\bar u}_i\hat{\bar u}_j$
denote the subgrid stress at the test-filter level (page-local symbol). The
resolved (Leonard) stress of the registry,
$L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j$, is
computable from $\bar u$ and satisfies the exact identity

$$L_{ij}=\mathcal T_{ij}-\hat\tau_{ij}.$$

Modelling both $\mathcal T_{ij}$ and $\tau_{ij}$ with the Smagorinsky form at
widths $\hat\Delta$ and $\Delta$, and taking $C_s$ out of the test filter,
gives for the deviatoric parts

$$L^d_{ij}=2(C_s\Delta)^2M_{ij},\qquad M_{ij}=\widehat{\lvert\bar S\rvert\bar S_{ij}}-\Big(\frac{\hat\Delta}{\Delta}\Big)^2\lvert\hat{\bar S}\rvert\hat{\bar S}_{ij},$$

an overdetermined system for one unknown, solved by least squares:

$$(C_s\Delta)^2=\frac{\langle L_{ij}M_{ij}\rangle}{2\langle M_{ij}M_{ij}\rangle}.$$

This is Eqs. (6)–(8) of [Agrawal et al. (2022)](/sources/agrawal-2022.md)
(§II.B), translated: they define the resolved stress and $M_{ij}$ with the
opposite signs ($L^{\mathrm{A}}=-L$, $M^{\mathrm{A}}=-M$), which leaves the
coefficient unchanged *(compiler check, not in the sources)*. Since $M_{kk}=0$ in incompressible flow, the contraction
$L_{ij}M_{ij}$ uses only the deviatoric part of $L_{ij}$ *(compiler check,
not in the sources)*. The averaging $\langle\cdot\rangle$ is over
homogeneous directions or time. Agrawal et al. note that pulling $C_s$
outside the test filter is strictly valid only with such averaging, and
that clipping or averaging is needed against negative eddy viscosity. The
only input is the ratio $\hat\Delta/\Delta$, set to 2 by Agrawal et al.
(§III).

## Implementations in the sources

| Source | Variant | Test filter, averaging |
|---|---|---|
| Agrawal et al. (2022), §II.B, §VII–VIII | DSM, incompressible and in charLES | $\hat\Delta/\Delta=2$; homogeneous directions (HIT, channel), time (Gaussian bump) |
| [Flad & Gassner (2017)](/sources/flad-2017.md), App. D | DSM in split-form DG, channel at $Re_\tau=590$ | Galerkin projection to degree 3 in $x$–$z$ planes with $N=7$, width ratio $N/N_{\mathrm{test}}=7/3\approx2.3$; average over wall-parallel planes within a DG cell |
| [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §II.B | DSM of Moin et al. (1991) with Lilly's modification, charLES | not printed |
| [Goc et al. (2021)](/sources/goc-2021.md), §2.1 | compressible DSM (Germano et al. 1991; Moin et al. 1991), for the in-tunnel aircraft cases | not printed |
| [Griffin et al. (2023)](/sources/griffin-2023.md), §4 | dynamic compressible model accounting only for variable properties (Moin et al. 1991) | not printed |
| [Beck & Kurz (2023)](/sources/beck-2023.md), §V | DSM after Moin et al. (1991) in DG (FLEXI) | not printed |
| [Abe (2021)](/sources/abe-2021.md), §II A, Eq. (5) | DSM (Germano et al. 1991; Lilly 1992), $\nu_t=C\Delta^2\lvert\bar S\rvert$ with $C\Delta^2$ computed as one product | not printed |
| [Prakash et al. (2022)](/sources/prakash-2022.md), §III | DSM and dynamic mixed model in the stabilized finite-element code PHASTA | $\hat\Delta/\Delta=\sqrt3$, filters of Tejada-Martínez & Jansen; homogeneous directions |
| [Fowler et al. (2022)](/sources/fowler-2022.md), §5; [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), App. B | Lagrangian scale-dependent dynamic model (Bou-Zeid et al. 2005) in LESGO | averaging along fluid-particle paths (Meneveau, Lund & Cabot 1996, as recalled by Fowler et al.) |

Fowler et al. (2022, §4.2) borrow the Lagrangian averaging of the dynamic
model for the time integration of their wall model (semi-Lagrangian upstream
interpolation of the previous value). Vadrot et al. (2023b, App. B, Fig. 18)
find that replacing the anisotropic minimum-dissipation model by the
Lagrangian scale-dependent dynamic model changes the channel WMLES mean
velocity at $Re_\tau=5200$ very little, for the equilibrium and for the
learned wall models alike.

## Independence of the filter-width definition

Because the procedure returns the product $(C_s\Delta)^2$, the definition of
$\Delta$ drops out once $\hat\Delta/\Delta$ is fixed. [Abe (2021)](/sources/abe-2021.md)
(§II A) states that the DSM therefore "does not depend explicitly on the
filter-width definition", and in an a priori test on high-aspect-ratio
cells in the free shear layer behind a backward-facing step it returns
"generally reasonable" eddy viscosities with some overestimation
downstream, where the static Smagorinsky model with the cube-root width is
strongly suppressed (§IV C, Fig. 9b). [Prakash et al. (2022)](/sources/prakash-2022.md)
(§III) use the same property for their dynamic mixed model, computing
$(C_G\Delta)^2$ directly because "the optimal definition of $\Delta$ for
anisotropic grids is not yet known" ($C_G$ the mixed-model coefficient, page-local). See
[large-eddy simulation](/definitions/large-eddy-simulation.md) for the
filter-width question.

## Behaviour reported

- **Homogeneous turbulence.** In decaying HIT ($Re_\lambda=70$, $32^3$ LES
  against $128^3$ DNS) DSM matches filtered DNS in energy and dissipation
  after a transient, with decay exponent about $-1.35$ against $-1.37$; in
  forced HIT ($Re_\lambda=315$, $128^3$) and for $Re_\lambda\to\infty$ it
  recovers the $k^{-5/3}$ spectrum (Agrawal et al. 2022, §VII.A–C). In the
  Taylor–Green vortex, Dairay et al. are recalled by
  [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§4.1) to
  find that the procedure gives $C_s\approx0.1$ after breakdown; Thiry et al.
  are recalled to obtain a near-constant spectral eddy viscosity with DSM
  (§6.3).
- **Coarse DG.** In DG LES of forced HIT at $Re_\lambda\approx180$, DSM is
  close to DNS at 36 degrees of freedom per direction but deviates at 24.
  The authors call it plausible, without investigating it, that the test
  filter then no longer lies in the similarity range (Beck & Kurz 2023, §V B, Fig. 9). DSM
  is beaten by no-model LES at $N=3$ and by the RL-optimized models at
  $N=5$ and 8 (§V A, Fig. 8). It performs comparably to the RL-Quad model on
  a deformed mesh (App. A).
- **Channel.** Split-form DG LES with DSM at $Re_\tau=590$ ($8^3$ elements,
  $N=7$) gives better Reynolds-stress profiles than DG ILES (Flad &
  Gassner 2017, §6.2, Fig. 11). In the WMLES channel at $Re_\tau=4200$ with
  20 points per half-height, DSM needs clipping of the SGS stress at the
  second off-wall point, as Morinishi & Vasilyev are recalled to report at
  $Re_\tau=395$; the Kármán-constant error is 7% (Agrawal et al. 2022,
  §VII.D, Figs. 8, 10). Lozano-Durán et al. (2022, §IV.B, App. B) calibrate
  the mean-velocity error of charLES WMLES with DSM at
  $\varepsilon_u\approx0.08\,\Delta/\delta$ and observe a non-monotonic
  convergence around $\Delta/\delta\approx0.03$–$0.05$ (see
  [wall-modelled LES](/methods/wall-modelled-les.md)).
- **Finite-element LES** (Prakash et al. 2022, §III.B, Table 4, Figs. 4–10).
  In forced isotropic turbulence at $\nu=10^{-12}$, DSM has no energy
  pile-up and follows the $k^{-5/3}$ slope but over-predicts energy at
  intermediate wavenumbers; in the Taylor–Green vortex at $Re=1600$ it
  under-predicts the resolved dissipation and the high-wavenumber energy;
  in channel flow at $Re_\tau=590$ it under-predicts $C_f$ (0.0047 and
  0.0049 on the coarse and medium meshes against 0.0058 from DNS). The
  dynamic mixed model with the [gradient model](/methods/gradient-model.md)
  is the most accurate model of the paper in the channel ($C_f=0.0053$,
  0.0055) but decays too fast and under-predicts the resolved dissipation in
  the Taylor–Green vortex, significantly even on $128^3$.
- **Smooth-body separation.** On the Gaussian bump, DSM and Vreman show
  non-monotonic grid convergence of $C_f$ (separation on the coarse grid,
  lost on the medium one, back on the fine one), whereas the tensor-coefficient
  extension converges monotonically (Agrawal et al. 2022, §VIII).
- **Stress magnitude.** Citing Jiménez & Moser, [Haering et al. (2022)](/sources/haering-2022.md)
  (§II B) recall that DSM gives subgrid stresses "nearly five times smaller
  than the true filtered stress" in channel flow, in support of their
  statement that a simple eddy viscosity cannot represent both the mean
  subgrid stress and the subgrid energy transfer.
- **Negative viscosity.** The local coefficient can become negative (local
  [backscatter](/definitions/energy-backscatter.md)), which generally
  destabilizes the computation; clipping or homogeneous averaging restores
  $\nu_t>0$ everywhere ([Vela-Martín 2022](/sources/velamartin-2022.md),
  §2.2, recalling Germano et al. 1991 and Meneveau & Katz 2000).

## Dynamic wall models (inline)

[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Introduction, p. 2)
recall dynamic (slip) wall models, the first author's earlier work, which
are free of a priori coefficients and follow from consistency between the
filtered velocity at the wall and a differential filter kernel. They state
that these models are robust to Reynolds number and grid but sensitive to
the numerical method and SGS model, which they attribute to near-wall
numerical errors, and that they have been used only in structured
incompressible solvers. This motivates their
[reinforcement-learning wall model](/methods/machine-learning-wall-model.md),
whose states they argue "do not depend heavily on numerics or SGS models,
unlike filtered velocities or eddy viscosity values required in the dynamic
model" (p. 10).

## Extension to a coefficient tensor

[Agrawal et al. (2022)](/sources/agrawal-2022.md) apply the identity to a
tensor coefficient $C_{ij}$ with four free components, solved by least
squares from a 6×4 system; see the
[dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md).

## Qualifications

- Flad & Gassner (2017, App. D, Eqs. D.1–D.4) print
  $C_S\Delta^2=-\tfrac12\langle L_{ij}M_{ij}\rangle/\langle M_{ij}M_{ij}\rangle$
  with $L_{ij}$ in the registry sign,
  $M_{ij}=\widehat{\lvert S\rvert S^d_{ij}}-(\hat\Delta/\Delta)\lvert\hat S\rvert\hat S^d_{ij}$
  and the model $\tau_{ij}=-2C_S\Delta^2\lvert S\rvert S^d_{ij}$. Applying
  the Germano identity to that model at both levels gives
  $L^d_{ij}=2C_S\Delta^2\big[\widehat{\lvert S\rvert S^d_{ij}}-(\hat\Delta/\Delta)^2\lvert\hat S\rvert\hat S^d_{ij}\big]$
  and hence a plus sign and a squared width ratio *(compiler check, not in
  the sources)*. The printed sign and exponent are inconsistent with the
  printed $L$, $M$ and model unless an unstated convention applies. Flad &
  Gassner also call the definition of $L_{ij}$ (Eq. D.3) "the Germano
  identity".

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.B, Eqs. (6)–(8); §III; §VII.A–D, Figs. 3–10; §VIII.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §6.2, Fig. 11; App. D, Eqs. (D.1)–(D.4).
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §V A–B, Figs. 8–9; App. A.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B; §IV.B; App. B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II B.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §4.2; §5.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II A; App. B, Fig. 18.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.2.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §4.1; §6.3.
- [Abe (2021)](/sources/abe-2021.md) — §II A, Eq. (5); §IV C, Fig. 9(b).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §II; §III; §III.B, Table 4, Figs. 4–10.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Introduction, p. 2; p. 10.
