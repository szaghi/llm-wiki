---
type: Method
title: "Dynamic procedure and the Germano identity"
description: "The dynamic procedure computes subgrid-model coefficients from the resolved field through the Germano identity between grid- and test-filter stresses, solved by least squares with averaging or clipping; the sources report its forms, regularizations, failures near walls and on coarse grids, and its tensorial extension."
status: established
aliases: [dynamic Smagorinsky model, DSM, Germano identity, Germano–Lilly procedure, dynamic SGS model, Lagrangian dynamic model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-26T07:19:00Z
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
| [Kim et al. (2022)](/sources/kim-2022.md), §II | DSM (Germano et al. 1991; Lilly 1992), baseline of a learned channel model; the coefficient written $C^2$ absorbs $\Delta^2$, i.e. $C^2=(C_s\Delta)^2$ in the form above | $\hat\Delta=2\Delta$; horizontal (wall-parallel) average |
| [Helm & Martín (2022)](/sources/helm-2022.md), §II, Eqs. (9)–(10) | compressible one-coefficient dynamic mixed model of Martín, Piomelli & Candler (2000): dynamic eddy-viscosity, eddy-diffusivity coefficients and subgrid turbulent Prandtl number | top-hat test filter in computational space; local ensemble average in the spanwise direction; coefficients transformed to curvilinear coordinates after Armenio et al. |
| [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §II.2 | DSM as baseline, and the identity on forces for the [fractional SGS model](/methods/fractional-sgs-model.md) | $\hat\Delta=2\Delta$, box filter; average over homogeneous directions |
| [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md), §IV B, Eq. (22); App. C | DSM, a posteriori in channel flow and as the eddy viscosity of an a priori diagnostic | test filter by first-order Taylor expansion in all three directions, $\hat\Delta/\Delta=2$; wall-parallel plane average; negative coefficient clipped to zero |
| [Kang et al. (2023)](/sources/kang-2023.md), §3.2–3.3, Eqs. (3.2)–(3.8) | DSM, one-parameter dynamic mixed model, two two-parameter mixed models (below) | Gaussian, $\hat\Delta/\Delta=\sqrt5$ (isotropic turbulence); volume or wall-parallel averages; negative coefficients clipped |
| [Kurz et al. (2023)](/sources/kurz-2023.md), App. A, Eqs. (A.1)–(A.3) | DSM element by element in DG (FLEXI), baseline of a learned closure | modal cut-off to degree 2 ($N=5$) or 3 ($N=7$); numerator and denominator averaged over the element; $\mu_t$ clipped to $[-100\mu,1000\mu]$ |
| [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §3.2; §2.5 | DSM with Lilly's modification in charLES; also the baseline stress of a mean-matching corrected SGS model used to generate wall-model training data | not printed |
| [Sirignano & MacArt (2023)](/sources/sirignano-2023.md), §3.2 | DSM, "the standard approach", baseline of learned closures | test filter, least squares, average over homogeneous directions |

Fowler et al. (2022, §4.2) borrow the Lagrangian averaging of the dynamic
model for the time integration of their wall model (semi-Lagrangian upstream
interpolation of the previous value). Vadrot et al. (2023b, App. B, Fig. 18)
find that replacing the anisotropic minimum-dissipation model by the
Lagrangian scale-dependent dynamic model changes the channel WMLES mean
velocity at $Re_\tau=5200$ very little, for the equilibrium and for the
learned wall models alike.

## Two-parameter mixed models

[Kang et al. (2023)](/sources/kang-2023.md) (§3.3, Eqs. 3.5–3.8; after
Anderson & Meneveau, as recalled) apply the identity to a model with two
coefficients, $\tau_{ij}=-2C_1\Delta^2\lvert\bar S\rvert\bar S_{ij}+C_2B_{ij}$,
with $B_{ij}$ (page-local) a structural term: the resolved stress $L_{ij}$
(their DTM$_{\mathrm{sim}}$) or the Clark [gradient](/methods/gradient-model.md)
term $\Delta^2\partial_k\bar u_i\partial_k\bar u_j$ (DTM$_{\mathrm{nl}}$).
With $M'_{ij}=2\Delta^2M_{ij}$ and $N_{ij}$ (both page-local) the
Smagorinsky and structural terms of the identity, least squares gives

$$C_1=\frac{\langle L_{ij}M'_{ij}\rangle\langle N_{kl}N_{kl}\rangle-\langle L_{ij}N_{ij}\rangle\langle M'_{kl}N_{kl}\rangle}{\langle M'_{ij}M'_{ij}\rangle\langle N_{kl}N_{kl}\rangle-\langle M'_{ij}N_{ij}\rangle^2},\qquad
C_2=\frac{\langle L_{ij}N_{ij}\rangle\langle M'_{kl}M'_{kl}\rangle-\langle L_{ij}M'_{ij}\rangle\langle M'_{kl}N_{kl}\rangle}{\langle M'_{ij}M'_{ij}\rangle\langle N_{kl}N_{kl}\rangle-\langle M'_{ij}N_{ij}\rangle^2}.$$

For DTM$_{\mathrm{sim}}$ the structural term at the test level needs a third
filter of width $5\Delta$. Their $M_{ij}$ is printed as
$-2\hat\Delta^2\lvert\hat{\bar S}\rvert\hat{\bar S}_{ij}+2\Delta^2\widehat{\lvert\bar S\rvert\bar S_{ij}}$,
which is $M'_{ij}$ here, so their one-parameter coefficient
$\langle L_{ij}M'_{ij}\rangle/\langle M'_{ij}M'_{ij}\rangle$ is $C_s^2$
*(compiler check, not in the sources)*. The one-parameter dynamic mixed
model (after Zang, Street & Koseff, modified by Vreman et al., as recalled)
subtracts the similarity part from $L_{ij}$ before the least squares (see
[scale-similarity models](/methods/scale-similarity-model.md)).

## The identity on forces

A model posed on the subgrid force $\partial_j\tau_{ij}$ rather than on
the stress needs the identity in divergence form,
$\partial_jL_{ij}=\partial_j\mathcal T_{ij}-\partial_j\hat\tau_{ij}$.
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (§II.2,
Eqs. 16–22) use it for the [fractional SGS model](/methods/fractional-sgs-model.md):
with the same coefficient at both levels the identity becomes
$\partial_jL_{ij}=C_{\mathrm{fr}}Q_i$, a vector equation for one unknown, and Lilly's
least squares gives $C_{\mathrm{fr}}=\langle Q_i\partial_jL_{ij}\rangle/\langle Q_iQ_i\rangle$
($C_{\mathrm{fr}}$, $Q_i$ page-local, defined there). The model operator does not
commute with the test filter, so $Q_i$ contains both the operator applied
to the test-filtered velocity and the test-filtered operator; for the
fractional Laplacian the two differ, shown with PDFs at fractional order
0.6 (Fig. 1). The coefficient is averaged over homogeneous directions to
avoid long-lived negative values (p. 10).

The same paper compares the effect of the procedure on a local and on a
nonlocal model. A priori, in isotropic turbulence at $Re_\lambda=240$, it
raises the stress correlation of the fractional model markedly but barely
that of the Smagorinsky model: "dynamic local models do not necessarily
increase the correlation coefficient remarkably" (§III.2, Fig. 4).

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
- **Wall-resolved channel, coarse grids** ([Kim et al. 2022](/sources/kim-2022.md),
  §III C–E, Figs. 7, 10, 12–13, Table IV). In channel LES at
  $(\Delta x^+,\Delta z^+)=(70.7,35.3)$, DSM over-predicts the mean
  velocity in the buffer and log layers and, at $Re_\tau=180$, 360 and
  720, the Reynolds shear stress; the authors call its dissipation
  insufficient. On the coarser grid $(94.2,47.1)$ the peak mean subgrid
  shear stress of the filtered DNS is about three times that of DSM. Applied
  to the same resolved field, DSM correlates almost perfectly with the
  strain: the correlation of $\bar S_{xy}$ with $-\tau_{xy}$ is 0.95 and
  0.94 at $y^+\approx15$ and 50, against $-0.20$ and 0.19 in the filtered
  DNS, and that of $\lvert\bar S\rvert^3$ with the local subgrid
  dissipation 0.92 and 0.88 against 0.01 and 0.28. Learned
  [reinforcement-learning](/methods/reinforcement-learning-closure.md)
  models trained on mean statistics do better on the means.
- **Compressible mixed model** ([Helm & Martín 2022](/sources/helm-2022.md),
  §III–IV F). With the dynamic coefficients above, the mixed model
  reproduces DNS of Mach 3, 7 and 10 boundary layers and two
  compression-ramp interactions; dropping its scale-similar part leaves
  the dynamic eddy viscosity alone and lengthens the Mach 7 separation by
  30% (see [scale-similarity models](/methods/scale-similarity-model.md)).
- **A priori backscatter.** The DSM gives backscatter at 20% and 18% of
  the points at two filter widths in
  box-filtered isotropic turbulence, against 26% and 30% in the filtered
  DNS, and over-predicts the tails of the PDF of the subgrid dissipation,
  which the authors link to the need for averaging a posteriori (Seyedi &
  Zayernouri 2022, §III.2, Fig. 5). A posteriori, in decaying isotropic
  turbulence, the resolved-energy decay of the fractional model agrees
  better with the filtered DNS than that of DSM, and the difference is
  "more remarkable" at the wider filter the authors class as
  very-large-eddy simulation than at the LES one (§IV, Fig. 9).
- **Averaging and clipping are needed; a learned mixed model does without**
  ([Kang et al. 2023](/sources/kang-2023.md), §3.1–3.5, Tables 4, 6, 9,
  11, Figs. 5–6, 20, 24–25). All four algebraic dynamic models are stable
  only with averaging over homogeneous directions and clipping of negative
  coefficients; without them they "significantly overestimate both
  backscatter and forward scatter" and diverge "within tens of time
  steps". In decaying isotropic turbulence the DTM$_{\mathrm{sim}}$ similarity
  coefficient $C_2$ turns negative and is clipped to zero after
  $t/T_{e,0}\ge1.62$ ($T_{e,0}$ the initial eddy-turnover time), so the
  model then behaves like DSM, consistent with Anderson & Meneveau (as
  recalled), for whom this happens when the test filter exceeds the
  integral scale. A priori the DSM stress correlates worst with the
  filtered-DNS stress (0.27–0.30 in isotropic turbulence, 0.19 for the
  shear stress in channel flow), DTM$_{\mathrm{nl}}$ best (0.91). In channel
  flow at $Re_\tau=180$ on $48^3$, DSM over-predicts the mean velocity and
  $\bar u_{\mathrm{rms}}$, under-predicts the other two r.m.s. components and
  gives $C_f=0.0072$ against 0.0085 from filtered DNS. Evaluating the SGS
  stress costs, relative to DSM, 2.24 (one-parameter mixed), 2.05
  (DTM$_{\mathrm{sim}}$), 1.68 (DTM$_{\mathrm{nl}}$) and 0.71 for their
  [neural-network mixed model](/methods/neural-network-sgs-model.md), which
  needs no averaging or clipping.
- **Coarse wall-resolved channel** ([Inagaki & Kobayashi 2023](/sources/inagaki-2023.md),
  App. C, Table I, Figs. 16–17). DSM LES at $Re_\tau=400$ predicts the DNS
  mean velocity at $(\Delta x^+,\Delta z^+)=(26.2,13.1)$ and $(52.4,26.2)$
  and overestimates it at $(105,52.4)$; at the medium resolution it
  over-predicts the streamwise and shear resolved Reynolds stresses and
  under-predicts the other two. A priori, the DSM eddy viscosity is less
  dissipative than the energy-matching one: at $y^+\approx40$ the total
  subgrid dissipation of the streamwise resolved Reynolds stress is twice
  the DSM estimate (§IV B). See [energy backscatter](/definitions/energy-backscatter.md)
  for the energy-matching eddy viscosity.
- **DG, element-wise** ([Kurz et al. 2023](/sources/kurz-2023.md), §4.2,
  §4.5, App. A, Figs. 6, 9). In forced isotropic turbulence at
  $Re_\lambda\approx180$ the element-wise DSM reproduces the DNS spectrum
  about as well as a reinforcement-learned element-wise Smagorinsky
  coefficient at 32, 36 and 48 degrees of freedom per direction, and
  significantly worse at 24, where the authors' "likely explanation" is
  that the test filter is not in the scale-similar range, the same
  explanation as Beck & Kurz (2023) above. At $Re_\lambda\approx240$ both
  show some energy build-up near the cutoff. Unclipped, the element-wise
  DSM "occasionally produced huge" coefficients that deteriorated the
  solution "quite drastically"; with the clipping above, the range had very
  limited influence. The learned policy costs about 10% more than the
  dynamic procedure on one CPU core.
- **Wall-modelled LES of complex flows** ([Lozano-Durán & Bae 2023](/sources/lozanoduran-2023.md),
  §4.2–4.8). With DSM and Vreman models at the matching location, the
  wall-stress error is dominated by "external" SGS errors once the wall
  model is accurate; in pipe flow at $Re_\tau\approx40\,000$ on the coarsest
  grid ($R/\Delta\approx5$, $R$ the pipe radius) the authors attribute a low
  near-wall shear and a low wall-model confidence to poor DSM performance.
- **Bluff bodies** ([Sirignano & MacArt 2023](/sources/sirignano-2023.md),
  §4.1–4.3, Table 2, Figs. 8–10). DSM under-predicts the drag of
  rectangular prisms (e.g. 2.15 against 2.45 from filtered DNS) and gives
  "incorrectly large" resolved Reynolds stresses in the boundary layers;
  the [AMD model](/methods/anisotropic-minimum-dissipation-model.md) and
  the learned closures do better.
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

- Kurz et al. (2023, §4.2) find the DSM about as accurate as the learned
  model at 32–48 degrees of freedom, while Beck & Kurz (2023, §V A) report
  it beaten by their learned models at $N=5$ and 8; the policies, inputs
  and resolutions differ between the two papers of the same group, and
  both find the DSM weakest at 24 degrees of freedom, so the statements are
  not recorded as a contradiction.

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
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §II.2, Eqs. (16)–(22), Fig. 1; §III.2, Figs. 4–5; §IV, Fig. 9.
- [Kim et al. (2022)](/sources/kim-2022.md) — §II (DSM baseline); §III C–E, Figs. 7, 10, 12–13, Table IV.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II, Eqs. (9)–(10); §III; §IV F.
- [Kang et al. (2023)](/sources/kang-2023.md) — §3.1–3.5, Eqs. (3.2)–(3.8), Tables 4, 6, 9, 11, Figs. 5–6, 20, 24–25.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §IV B, Eq. (22); App. C, Table I, Figs. 16–17.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §4.2; §4.5, Figs. 6, 9; App. A, Eqs. (A.1)–(A.3).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.5; §3.2; §4.2–4.8.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §3.2; §4.1–4.3, Table 2, Figs. 8–10.
