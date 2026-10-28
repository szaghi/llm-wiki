---
type: Method
title: "Dynamic procedure and the Germano identity"
description: "The dynamic procedure computes subgrid-model coefficients from the resolved field through the Germano identity between grid- and test-filter stresses, solved by least squares with averaging or clipping; the sources report its forms, regularizations, failures near walls and on coarse grids, and its tensorial extension."
status: established
aliases: [dynamic Smagorinsky model, DSM, Germano identity, Germano–Lilly procedure, dynamic SGS model, Lagrangian dynamic model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-27T21:09:00Z
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
| [Fowler et al. (2022)](/sources/fowler-2022.md), §5; [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), App. B | Lagrangian scale-dependent dynamic model (Bou-Zeid et al. 2005) in LESGO | averaging along fluid-particle paths (Meneveau, Lund & Cabot 1996, cited by Fowler et al.) |
| [Kim et al. (2022)](/sources/kim-2022.md), §II | DSM (Germano et al. 1991; Lilly 1992), baseline of a learned channel model; the coefficient written $C^2$ absorbs $\Delta^2$, i.e. $C^2=(C_s\Delta)^2$ in the form above | $\hat\Delta=2\Delta$; horizontal (wall-parallel) average |
| [Helm & Martín (2022)](/sources/helm-2022.md), §II, Eqs. (9)–(10) | compressible one-coefficient dynamic mixed model of Martín, Piomelli & Candler (2000): dynamic eddy-viscosity, eddy-diffusivity coefficients and subgrid turbulent Prandtl number | top-hat test filter in computational space; local ensemble average in the spanwise direction; coefficients transformed to curvilinear coordinates after Armenio et al. |
| [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §II.2 | DSM as baseline, and the identity on forces for the [fractional SGS model](/methods/fractional-sgs-model.md) | $\hat\Delta=2\Delta$, box filter; average over homogeneous directions |
| [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md), §IV B, Eq. (22); App. C | DSM, a posteriori in channel flow and as the eddy viscosity of an a priori diagnostic | test filter by first-order Taylor expansion in all three directions, $\hat\Delta/\Delta=2$; wall-parallel plane average; negative coefficient clipped to zero |
| [Kang et al. (2023)](/sources/kang-2023.md), §3.2–3.3, Eqs. (3.2)–(3.8) | DSM, one-parameter dynamic mixed model, two two-parameter mixed models (below) | Gaussian, $\hat\Delta/\Delta=\sqrt5$ (isotropic turbulence); volume or wall-parallel averages; negative coefficients clipped |
| [Kurz et al. (2023)](/sources/kurz-2023.md), App. A, Eqs. (A.1)–(A.3) | DSM element by element in DG (FLEXI), baseline of a learned closure | modal cut-off to degree 2 ($N=5$) or 3 ($N=7$); numerator and denominator averaged over the element; $\mu_t$ clipped to $[-100\mu,1000\mu]$ |
| [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §3.2; §2.5 | DSM with Lilly's modification in charLES; also the baseline stress of a mean-matching corrected SGS model used to generate wall-model training data | not printed |
| [Sirignano & MacArt (2023)](/sources/sirignano-2023.md), §3.2 | DSM, "the standard approach", baseline of learned closures | test filter, least squares, average over homogeneous directions |
| [Kim et al. (2024)](/sources/kim-2024.md), §2.1, §3.2, §4.2 | DSM (Germano et al. 1991; Lilly 1992), baseline of neural-network models of a cylinder wake, finite differences with an immersed boundary | box test filter in the spanwise (homogeneous) direction only, $\hat\Delta_z=2\Delta_z$ ($\Delta_z$ page-local, the spanwise grid size); coefficient averaged over $z$ |
| [Wang et al. (2023c)](/sources/wang-2023-c.md), §II.A, Eq. (12) | DSM (Lilly's least-squares form) and a two-coefficient dynamic mixed model, baselines in isotropic turbulence and a temporal mixing layer, pseudo-spectral | Gaussian, $\hat\Delta=2\Delta$; average over homogeneous directions |
| [Domaradzki (2024)](/sources/domaradzki-2024.md), §3.3, Eqs. (3.4)–(3.7) | identity in energy form, applied to the coefficient of the [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md) | the model's own graded filter; local and domain average |
| [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md), §2.4, §3.3.2 | DSM of the reference LES (LESOCC, Breuer et al.) of the periodic hill, as cited there | not printed |
| [Brillon & Nadarajah (2026)](/sources/brillon-2026.md), §2.6.4, Eqs. (53)–(58); §3.1.8 | DSM in nonlinearly stable flux reconstruction, with the low-Reynolds-number correction of Meyers & Sagaut; coefficient written $C_D$ in $\nu_t=C_D\Delta^2\lvert\bar S\rvert$, i.e. $C_D=C_s^2$ | modal test filter to degree 3 at $N=5$, width $V^{1/3}/4$ against $\Delta=V^{1/3}/6$ ($V$ the element volume), so $\hat\Delta/\Delta=1.5$ *(compiler check, not in the sources)*; element averages of numerator and denominator; clipped (see Qualifications) |
| [Jakhar et al. (2026)](/sources/jakhar-2026.md), App. D | DSM (Germano et al., cited) and a dynamic Leith model, baselines in forced two-dimensional turbulence | not printed; "positive clipping" enforces $\nu_t\ge0$ |
| [Li et al. (2024)](/sources/li-2024.md), §II B, Eqs. (7)–(11) | DSM (Lilly's least squares) and a two-coefficient dynamic mixed model, baselines of a neural-operator surrogate in forced isotropic turbulence and a temporal mixing layer, pseudo-spectral | test filter $\hat\Delta=2\Delta$, and a second filter of width $4\Delta$ for the mixed model's structural term; average over the whole domain, so the coefficients are spatially uniform at each time |
| [Pan & Zhang (2023)](/sources/pan-2023.md), §II.D, Eqs. (16)–(19) | dynamic Smagorinsky–Lilly model of ANSYS-Fluent (Lilly's "minimum error method"), reference LES of a centrifugal impeller; printed as $L^d_{ij}=C_s^2M^{\mathrm P}_{ij}$ with $M^{\mathrm P}_{ij}=2\Delta^2\widehat{\lvert\bar S\rvert\bar S_{ij}}-2\hat\Delta^2\lvert\hat{\bar S}\rvert\hat{\bar S}_{ij}$ ($M^{\mathrm P}$ page-local) $=2\Delta^2M_{ij}$, and $C_s^2=\langle L_{ij}M^{\mathrm P}_{ij}\rangle/\langle M^{\mathrm P}_{ij}M^{\mathrm P}_{ij}\rangle$, the formula above *(compiler check, not in the sources)* | default Fluent test filter; averaging not specified |
| [Volpiani (2024)](/sources/volpiani-2024.md), App. 2, Eqs. (33)–(40) | compressible Germano–Lilly model (Germano et al.; Lilly; Spyropoulos & Blaisdell, cited) with Favre-filtered strain and density-weighted $L_{ij}$ and $M_{ij}$, coefficient $C_d=C_s^2$, and a dynamic Yoshizawa coefficient $C_I=\langle L_{kk}\rangle/\langle2\hat\Delta^2\hat{\bar\rho}\lvert\hat{\tilde S}\rvert^2-2\Delta^2\widehat{\bar\rho\lvert\tilde S\rvert^2}\rangle$ for the isotropic part ($C_I$ page-local) | $\hat\Delta=2\Delta$; kernel and averaging not printed |
| [Zhao et al. (2021)](/sources/zhao-2021-c.md), §III.A, Eqs. (15)–(16); §III.D | DSM (Germano et al. 1991; Vreman et al. 1997, as cited) in a high-order gas-kinetic finite-volume code, wall-resolved channel; its coefficient is reused unchanged as $C_d$ of a dynamic Clark mixed model | test filter $2\Delta$; average over the homogeneous $x$–$z$ planes; positive-part clipping "so that backscatter is eliminated" |
| [Li et al. (2021)](/sources/li-2021.md), §III C | DSM (Moin et al. 1991, as cited), comparator of a gene-expression-programming model in forced isotropic turbulence, pseudospectral | not printed |
| [Valencia et al. (2026)](/sources/valencia-2026.md), §I, §V C | DSM and dynamic mixed model as a priori baselines in explicitly filtered compressible isotropic turbulence | not printed |
| [Chen et al. (2022)](/sources/chen-2022-g.md), §4.1, Eqs. (26)–(29) | Germano–Lilly least squares, printed $C_s^2=\langle L^{\mathrm C}_{ij}M^{\mathrm C}_{ij}\rangle/\langle M^{\mathrm C}_{ij}M^{\mathrm C}_{ij}\rangle$ with $L^{\mathrm C}_{ij}=-L^d_{ij}$ and $M^{\mathrm C}_{ij}=-2\Delta^2M_{ij}$ ($L^{\mathrm C}$, $M^{\mathrm C}$ page-local), which is the formula above *(compiler check, not in the sources)*; finite-difference reference LES of a channel beside residual-based VMS | widths not printed; average over homogeneous directions |
| [Qi et al. (2022)](/sources/qi-2022-b.md), §4.1 | compressible DSM (Germano et al.; Lilly) and the dynamic $k_{\mathrm{sgs}}$-equation model of Chai & Mahesh (cited), baselines of a test-filter-free model (below) | box test filter, $\hat\Delta=2\Delta$, $\Delta=(\Delta x\Delta y\Delta z)^{1/3}$ |
| [Wang et al. (2022)](/sources/wang-2022-j.md), §II B | DSM (Lilly's least squares) and a two-coefficient dynamic mixed model, baselines of a constant-coefficient spatial gradient model in forced isotropic turbulence and a temporal mixing layer | Gaussian, $\hat\Delta=2\Delta$; average over homogeneous directions |
| [Cao et al. (2022b)](/sources/cao-2022-c.md), §III, Eqs. (12)–(13), App. A | DSM inside a gas-kinetic finite-volume scheme (eddy viscosity through the collision time), coefficient $C_d$ multiplying $\bar\Delta^2$, i.e. $C_s^2$ | discrete 27-point top-hat test filter, the tensor product of the weights $(\tfrac14,\tfrac12,\tfrac14)$, width $2\bar\Delta$; average over the whole domain, so one value per time step |
| [Zhang et al. (2022b)](/sources/zhang-2022-f.md), App., Eqs. (A1)–(A24) | density-unweighted DSM with dynamic coefficients for the deviatoric stress, the Yoshizawa trace, the subgrid mass flux, heat flux and density–temperature correlation; density-unweighted two-coefficient dynamic mixed model for the same terms | $\hat\Delta=2\Delta$ (a filter of width $4\Delta$ for the mixed model's test-level structural terms); averages over the domain |
| [Zhang et al. (2022d)](/sources/zhang-2022-h.md), Eqs. (33)–(36) | Favre DSM with a dynamic Yoshizawa coefficient $C_I$ for the isotropic part, thermodynamic subgrid terms of a dense gas neglected; baseline of iterative deconvolution | $\hat\Delta=2\Delta$; averages over the domain |
| [Li et al. (2022)](/sources/li-2022-k.md), §II C, Eqs. (10)–(15) | compressible DSM of Moin et al. (cited) with Lilly's least squares, used to make the constant of a Reynolds-stress-model-based IDDES dynamic (below) | volume-weighted average over the direct face neighbours of a cell on hybrid unstructured meshes, $\hat\Delta=a\Delta$ with $a=2$ "in general"; the same neighbour average for numerator and denominator; negative $C_s^2$ clipped to zero |

Fowler et al. (2022, §4.2) borrow the Lagrangian averaging of the dynamic
model for the time integration of their wall model (semi-Lagrangian upstream
interpolation of the previous value). Vadrot et al. (2023b, App. B, Fig. 18)
find that replacing the anisotropic minimum-dissipation model by the
Lagrangian scale-dependent dynamic model changes the channel WMLES mean
velocity at $Re_\tau=5200$ very little, for the equilibrium and for the
learned wall models alike.

## Two-parameter mixed models

[Kang et al. (2023)](/sources/kang-2023.md) (§3.3, Eqs. 3.5–3.8; after
Anderson & Meneveau, cited) apply the identity to a model with two
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
model (after Zang, Street & Koseff, modified by Vreman et al., cited)
subtracts the similarity part from $L_{ij}$ before the least squares (see
[scale-similarity models](/methods/scale-similarity-model.md)).

[Li et al. (2024)](/sources/li-2024.md) (§II B, Eqs. 9–11) print the same
two-coefficient least squares for a dynamic mixed model. Their structural
term is the similarity stress formed with the test filter ($2\Delta$), and
its test-level counterpart uses a second filter of width $4\Delta$. Their Eqs. (10)–(11)
build the Smagorinsky part of the identity from
$-2\Delta^2\lvert\bar S\rvert\bar S_{ij}$, so the coefficient $C_1$
multiplies that term. The model as printed in their Eq. (9),
$C_1\Delta^2\lvert\bar S\rvert\bar S_{ij}$, lacks the factor $-2$ (see
Qualifications).

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
  Taylor–Green vortex,
  [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§4.1)
  cite Dairay et al. as finding that the procedure gives $C_s\approx0.1$
  after breakdown, and (§6.3) Thiry et al. as obtaining a near-constant
  spectral eddy viscosity with DSM.
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
  second off-wall point, as Agrawal et al. cite Morinishi & Vasilyev
  reporting at $Re_\tau=395$; the Kármán-constant error is 7% (Agrawal et al. 2022,
  §VII.D, Figs. 8, 10). Lozano-Durán et al. (2022, §IV.B, App. B) calibrate
  the mean-velocity error of charLES WMLES with DSM at
  $e_u\approx0.08\,\Delta/\delta$ and observe a non-monotonic
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
  model then behaves like DSM, consistent with Anderson & Meneveau (cited), for whom this happens when the test filter exceeds the
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
- **Circular-cylinder wake** ([Kim et al. 2024](/sources/kim-2024.md),
  §4.1–4.2, Table 3, Figs. 6, 8–13). Against filtered DNS at $Re_D=3900$,
  DSM gives a recirculation length $L_r/D=1.32$ (DNS 1.56; $L_r$
  page-local) on the training grid $449\times271\times64$, 0.80 on the
  coarser $353\times213\times64$ and 1.45 on the finer $545\times301\times64$,
  where it "agrees well" with DNS; its base pressure is $-C_{pb}=0.94$
  against 0.87. At untrained $Re_D=5000$ it gives 1.35 against 1.39, and at
  $Re_D=10\,000$ 0.62 against the measured 0.82 (no model 0.51). A priori
  its backscatter is zero. The pointwise neural-network models with
  grid- and test-filtered inputs fused by subtraction keep their accuracy
  on the untrained grids; the authors motivate the subtraction by the
  Germano identity, the difference of the two levels standing for $L_{ij}$
  (§3.2; see [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
  and [neural-network SGS models](/methods/neural-network-sgs-model.md)).
  A full time step costs about 2 (fused model) to 2.5 (grid-filtered
  input only) times a DSM step on the same grid (App. E).
- **Over-dissipation in isotropic turbulence and a mixing layer**
  ([Wang et al. 2023c](/sources/wang-2023-c.md), §III–IV, Figs. 3–17). DSM
  and the dynamic mixed model slightly over-estimate large-scale and
  under-estimate small-scale energy in forced isotropic turbulence at
  $Re_\lambda\approx160$ and give narrower PDFs of strain and rotation. In
  a temporal mixing layer DSM delays transition (the dynamic mixed model
  captures it better), and both over-predict the kinetic energy in the
  linear-growth region and the size of vortical structures; the DSM
  subgrid flux is strictly positive. An ensemble-Kalman-calibrated mixed
  model does better (see [gradient model](/methods/gradient-model.md) and
  [ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)).
- **Baseline of a neural-operator surrogate**
  ([Li et al. 2024](/sources/li-2024.md), §V, Figs. 6–21, Tables I–II).
  The setting is a posteriori LES on $64^3$ in forced
  [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
  at $Re_\lambda\approx100$, with sharp spectral filtering at $k_c=21$. The
  DSM run also applies the filtered-DNS forcing at the two largest
  wavenumbers.
  - **DSM in isotropic turbulence.** DSM is closest to filtered DNS in the
    rms velocity and vorticity, and more accurate than the learned
    surrogate in the spectrum for $k\ge18$.
  - **Mixed model in isotropic turbulence.** The dynamic mixed model
    underestimates the spectrum at low wavenumbers and "significantly
    overestimates" it at high ones.
  - **Velocity increments.** Both models deviate in the PDFs of velocity
    increments beyond $0.5$ rms.
  - **Temporal mixing layer.** In the
    [temporal mixing layer](/benchmarks/temporal-mixing-layer.md) DSM
    underestimates the momentum thickness during transition and
    overestimates it in the linear-growth region. Both models predict
    larger vortical structures than filtered DNS, in line with Wang et al.
    (2023c) above.
  - **Global averaging.** Both models average their coefficients over the
    whole domain, in the mixing layer as in isotropic turbulence (§II B).
    See
    [neural-operator surrogates](/methods/neural-operator-les-surrogate.md).
- **A dynamic coefficient that fails.** Applied to the constant $C_{\mathrm A}$
  (page-local, the non-dimensional constant of the constant variant) of the
  [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md),
  the energy form of the identity gives wildly fluctuating local values and
  a domain-averaged $C_{\mathrm A}=-3.9$ with standard deviation of order $10^3$ in
  forced isotropic turbulence (Domaradzki 2024, §3.3). In the
  domain-averaged identity the two terms multiplied by $C_{\mathrm A}$ are
  comparable, so a large $C_{\mathrm A}$, and excessive dissipation, would be
  needed (Eq. 3.7). The author's argument: the procedure picks a model first and fits its coefficient,
  so the predicted subgrid transfer for the same field depends on the
  model chosen; Domaradzki judges it not useful for the method. The paper
  also recalls,
  as Vicente Cruz & Lamballais do above, that Thiry, Winckelmans &
  Duponcheel found the spectral viscosity of DSM "essentially uniform over
  all wavenumbers" (§3.3).
- **Periodic hill reference LES.** Breuer et al.'s LESOCC LES with DSM
  (12.4 million cells, $Re_h=5600$) reattaches at $x/h=5.09$ against Rapp's
  measured 4.83; Breuer et al. attribute the slightly under-predicted
  pressure to the SGS model, which delays separation and lengthens the
  bubble; Prieto Saavedra et al. (2024, §3.3.2, Table 1) cite these
  results.
  See [periodic hill](/benchmarks/periodic-hill.md).
- **Negative viscosity.** The local coefficient can become negative (local
  [backscatter](/definitions/energy-backscatter.md)), which generally
  destabilizes the computation; clipping or homogeneous averaging restores
  $\nu_t>0$ everywhere ([Vela-Martín 2022](/sources/velamartin-2022.md),
  §2.2, recalling Germano et al. 1991 and Meneveau & Katz 2000). The
  learned 1D closure of [van Gastelen et al. (2024)](/sources/vangastelen-2024.md)
  (§1) cites the dynamic localization model with a subgrid-energy equation
  (Ghosal et al., cited) as an earlier way to admit backscatter
  stably by modelling the subgrid energy, the route their own closure
  takes (see [energy backscatter](/definitions/energy-backscatter.md)).

- **Not needed on an entropy-stable baseline.** In implicitly filtered LES
  of the Taylor–Green vortex at $Re=1600$ with nonlinearly stable
  [flux reconstruction](/methods/flux-reconstruction.md) ($96^3$ degrees
  of freedom, $N=5$), DSM, like the static Smagorinsky variants, lowers the
  peak enstrophy and removes energy at wavenumbers 25–40, where the
  dissipation-free scheme already has a deficit; the authors recommend none
  of these models for that scheme ([Brillon & Nadarajah 2026](/sources/brillon-2026.md),
  §3.1.8, Fig. 19; see [Smagorinsky model](/methods/smagorinsky-model.md)).
- **Two-dimensional turbulence** ([Jakhar et al. 2026](/sources/jakhar-2026.md),
  Fig. 2, App. D). The dynamic Leith model takes
  $\nu_t=(C_l\Delta)^3\lvert\nabla\bar\omega_z\rvert$ ($C_l$ page-local,
  $\bar\omega_z$ the filtered out-of-plane vorticity, as on the Source page) with $C_l$ computed
  dynamically. A priori, over four cases of forced two-dimensional
  turbulence, the ratio of the domain-averaged interscale energy transfer
  to that of filtered DNS is $-28.48\pm15.38$ for DSM and $-6.91\pm2.73$ for
  dynamic Leith, against $-62.24\pm37.80$ for static Smagorinsky; the
  ratios for the enstrophy transfer are $-1.49\pm0.45$ and $-0.37\pm0.06$
  against $-3.22\pm1.18$. The dynamic forms give ratios of smaller magnitude but keep the
  sign of a purely diffusive closure (see
  [energy backscatter](/definitions/energy-backscatter.md)).
- **Taylor–Green vortex on split forms.** Volpiani (2024, §5, Fig. 15d)
  finds that the dynamic model on a kinetic-energy-preserving split-form
  central scheme does not improve on the multiscale Smagorinsky models at
  $Re=1600$, and that all the explicit models are beaten by a
  relaxation-filtered implicit LES without model (see
  [Smagorinsky model](/methods/smagorinsky-model.md) and
  [explicit modal filtering](/methods/explicit-modal-filtering.md)).
- **A priori against the total subfilter stress.** In explicitly filtered
  compressible isotropic turbulence, Valencia et al. (2026, Tables VI–VII)
  find the DSM correlating with the total unresolved stress at only
  0.12–0.27 with relative errors of 1.02–1.96, and the dynamic mixed model
  at 0.91 with relative errors of 0.44–0.49, both nearly insensitive to the
  filter-to-grid ratio, against 0.97–0.999 for deconvolution models (see
  [scale-similarity model](/methods/scale-similarity-model.md)).
- **Reference LES of an impeller in rotating stall.** Pan & Zhang (2023,
  §III) use the dynamic model as the benchmark against which
  [DES and DDES](/methods/detached-eddy-simulation.md) are ranked, on the
  same 12.33-million-cell grid (maximum $y^+\approx1.2$). Its validation
  against PIV shows "remarkable discrepancy", which they attribute to the
  experimental rig; the impeller head is 3.75% above the measured value.
- **Best explicit model behind implicit LES in a gas-kinetic channel**
  ([Zhao et al. 2021](/sources/zhao-2021-c.md), §V, Tables V–VII,
  Figs. 2–19). In wall-resolved channel flow at nominal $Re_\tau=180$
  ($96^3$) and 395 ($96^3$, $128^3$), the clipped plane-averaged DSM gives
  the highest realized $Re_\tau$ of the four explicit models (175.47 against
  DNS 178.12 at 180; 359.54 and 375.22 against 392.24 at 395) and is
  "superior" to the Vreman, WALE and dynamic Clark models, but below the
  no-model run (see [implicit LES](/definitions/implicit-les.md)). At
  $Re_\tau=180$ it matches the DNS Reynolds shear stress better than iLES
  (§V.B). The authors explain its rank thus: "the numerical dissipation in
  this model is relatively small as a result of the dynamic coefficient"
  (§V.B; §VI). It costs 0.613 s per step
  against 0.520 s for no model on $64\times96\times64$ (Table III).
- **Comparator of a symbolic-regression model**
  ([Li et al. 2021](/sources/li-2021.md), §III C, Figs. 2–6). In a
  posteriori LES of forced isotropic turbulence ($128^3$, filter width 16
  DNS spacings), DSM spectra are damped near the cutoff and "energy-rich"
  at lower wavenumbers; DSM underpredicts the small-separation structure
  functions, more for higher orders, and gives the narrowest PDFs of the
  anisotropic stress components, which the authors attribute to its pure
  dissipation. Its subgrid flux is strictly positive (see
  [energy backscatter](/definitions/energy-backscatter.md)). A
  gene-expression-programming tensor model and a neural network do better
  at about the cost of DSM for the former (see
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)).
- **Realizability.** [Heinz (2020)](/sources/heinz-2020.md) (§2.1), in a
  hybrid RANS/LES review, states that dynamic LES that does not honour
  realizability, the DSM, "is often computationally unstable", that the
  averaging or clipping used against this reduces the backscatter of LES,
  and that "fully realizable dynamic LES" (Mokhtarpoor & Heinz, cited) is
  stable without either.
- **Clipping as a reason to prefer another baseline.** [Wu & Lele (2026)](/sources/wu-2026.md)
  (§5.1) choose the [Sigma model](/methods/sigma-model.md) rather than DSM
  as the reference of their learned closures, because the Sigma coefficient
  "does not require clipping for channel flow", whereas DSM "may need
  clipping" (Meneveau et al. 1996, as cited).
- **Coarse channel against a residual-based closure.** On a
  $32\times64\times32$ channel mesh at $Re_\tau=180$, [Chen et al. (2022)](/sources/chen-2022-g.md)
  (§4.2, §5, Figs. 1–3) find that DSM agrees with DNS in the inner layer,
  unlike static [Smagorinsky](/methods/smagorinsky-model.md), and dissipates
  less than Smagorinsky in the inner layer and more in the outer layer; the
  residual-based [variational multiscale](/methods/variational-multiscale-method.md)
  LES on the same mesh gives better mean velocity than both.
- **Degradation on coarse compressible grids.** In compressible channel
  flow at $M=1.5$ (DNS $Re_\tau=220$), DSM gives $Re_\tau=213$, 208 and 201
  on three successively coarser LES grids, and the dynamic $k_{\mathrm{sgs}}$
  model 215, 210 and 208 (Qi et al. 2022, Tables 2–4). In a converging
  spherical Richtmyer–Meshkov mixing layer both dynamic models deviate from
  DNS in the mixing-layer radii between 0.075 and 0.12 ms, which the authors
  attribute, hedged with "Perhaps", to strong anisotropy and inhomogeneity
  that "cannot meet the requirement of scale invariance for the traditional
  dynamic procedure" (§4.3, Figs. 22–23).
- **Spectral-element dynamic model.** [Tonicello et al. (2022)](/sources/tonicello-2022.md)
  (§5) cite the "promising results" of their own preliminary LES of a
  similar ramp configuration (Tonicello et al. 2021, cited) with the
  spectral-element dynamic model of Chapelier & Lodato (2016, cited); the
  paper shows no data of it.

- **Gas-kinetic implicit against explicit LES.** On the compressible
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $M=0.1$,
  $Re=1600$ ($256^3$), the domain-averaged dynamic coefficient of Cao et
  al. (2022b) "is always positive"; DSM is the best of their explicit
  models but its total subgrid dissipation, estimated a posteriori as
  $-\mathrm dE_k/\mathrm dt$ minus the resolved physical dissipation, stays
  between that of implicit LES and of static Smagorinsky and Vreman
  ($2.1\times10^{-5}$, $2.0\times10^{-4}$, $8.6\times10^{-4}$,
  $9.4\times10^{-5}$ at $t=2.5$, 5, 10, 15, against $1.5\times10^{-5}$,
  $1.4\times10^{-4}$, $6.7\times10^{-4}$, $1.8\times10^{-5}$ for implicit
  LES; §IV C, Fig. 8, Table II). They note that the coefficient is usually
  clipped to non-negative values for stability and then cannot represent
  backscatter (§IV B; see [implicit LES](/definitions/implicit-les.md) and
  [energy backscatter](/definitions/energy-backscatter.md)).
- **Over-dissipation against structural models.** In forced isotropic
  turbulence ($128^3$ LES of a $1024^3$ DNS at $Re_\lambda\approx250$) DSM
  over-estimates the spectrum at low and under-estimates it at high
  wavenumbers and over-predicts the peak of the strain-rate PDF; in a
  temporal mixing layer it captures the transitional growth of the
  momentum thickness but deviates in the linear-growth region and
  over-estimates the Reynolds shear stress (Wang et al. 2022, §IV–V, Figs.
  2–4, 9, 15). In decaying compressible isotropic turbulence the
  density-unweighted DSM (Zhang et al. 2022b, §IV B, Figs. 5–17) and the
  Favre DSM of a dense gas (Zhang et al. 2022d, §IV B, Figs. 6–15) are
  over-dissipative: kinetic energy too high in the decay, high-wavenumber
  spectrum too low, PDFs of subgrid flux, deviatoric stress, strain and
  vorticity too narrow, against iterative deconvolution (see
  [scale-similarity models](/methods/scale-similarity-model.md)).

## Dynamic coefficient of a hybrid RANS/LES length scale

[Li et al. (2022)](/sources/li-2022-k.md) apply the procedure to a
[detached-eddy simulation](/methods/detached-eddy-simulation.md) built on
the SSG/LRR-$\omega$ [Reynolds-stress model](/methods/reynolds-stress-model.md).
In the authors' earlier RSM-based IDDES (cited, ingested as
[Wang et al. 2021](/sources/wang-2021-l.md)) the dissipation of the
modelled stresses is isotropic, $\varepsilon=k^{3/2}/l_{\mathrm{DES}}$, and
in the LES region $l_{\mathrm{LES}}=C_{\mathrm{DES}}\Delta$; under
equilibrium the branch is "Smagorinsky-like" with

$$C_{\mathrm{DES}}=C_kC_s,\qquad C_k=\Big[\frac{C_{\phi1}}{C_{\ell\varepsilon}C_{\phi2}}\Big]^{3/4},$$

$C_{\phi1}$, $C_{\phi2}$ the production and destruction coefficients of the
length-scale equation and $C_{\ell\varepsilon}=0.09$ (Eqs. 6–9; $C_k$,
$C_{\phi1}$, $C_{\phi2}$, $C_{\ell\varepsilon}$ page-local). Making $C_s$
dynamic makes $C_{\mathrm{DES}}$ dynamic, so the calibration of
$C_{\mathrm{DES}}$ on decaying isotropic turbulence, which the authors
call grid- and scheme-dependent (citing Mockett) and over-dissipative in
mean shear, is no longer needed (§I, §II C). With $C_k=1.67$ (SSG branch)
and 2.78 (LRR branch), $C_{\mathrm{DES}}=0.3$ and 0.5 at $C_s=0.18$, the
recommended values of their solver (§III A; $1.67\times0.18=0.3006$,
$2.78\times0.18=0.5004$ *(compiler check, not in the sources)*). Decaying isotropic turbulence of Comte-Bellot &
Corrsin on $64^3$ is matched with both branches and is insensitive to
$C_k$ (Fig. 3). On the [periodic hill](/benchmarks/periodic-hill.md) at
$Re=10\,595$ (about 1.1 million cells) the resolved Reynolds stresses move
closer to the reference data than with the constant coefficient (§III B,
Figs. 9–11). On the [hammerhead launch vehicle](/benchmarks/hammerhead-launch-vehicle-buffet.md)
($M=0.81$) the dynamic coefficient lowers the modelled stress in the
vortex-development region and the peak $C_{p,\mathrm{rms}}$ at the
experimental maximum, 0.0554 against 0.0719 with the constant coefficient,
0.0897 with SST-IDDES and 0.0454 in the experiment, with the mean $C_p$
unchanged (§III C, Figs. 16, 18). The authors credit "more appropriate
assessment of the turbulent dissipation" (Fig. 12); the convective fluxes
are second-order Roe fluxes.

## A test-filter-free coefficient: the quasi-dynamic procedure

[Qi et al. (2022)](/sources/qi-2022-b.md) (§3.2, Eqs. 3.8–3.26) fix the
coefficients of a compressible one-equation model locally from the
transported subgrid kinetic energy, with no test filter, hence
"quasi-dynamic". The leading term of the series expansion of a filtered
product (after Bedford & Yeo and Pomraning & Rutland, cited),

$$\overline{fg}-\bar f\bar g\approx C_0\Delta_k^2\,\partial_k\bar f\,\partial_k\bar g,$$

with $C_0$ (page-local) and $\Delta_k$ the grid spacing in direction $k$,
gives the [gradient-model](/methods/gradient-model.md) stress
$\tau_{ij}\approx C_0\Delta_k^2\bar\rho\,\partial_k\tilde u_i\partial_k\tilde u_j$,
the gradient model for $C_0=1/12$ (Eq. 3.12). Two constraints close it:

1. **Trace.** Equating the trace of the expanded stress to
   $2\bar\rho k_{\mathrm{sgs}}$ gives
   $C_0=2k_{\mathrm{sgs}}/(\Delta_l^2\,\partial_l\tilde u_k\partial_l\tilde u_k)$
   (Eq. 3.15).
2. **Flux.** The [Smagorinsky](/methods/smagorinsky-model.md) coefficient
   is set by equating the anisotropic part of the Smagorinsky flux to the
   anisotropic part of the expanded flux $-\tau_{ij}\tilde S_{ij}$
   (Eq. 3.21), while the isotropic part of the stress is taken directly as
   $2\bar\rho k_{\mathrm{sgs}}$ instead of from Yoshizawa's model.

Because the same filter acts at a point, the authors assume the same
$C_0$ for every expanded term, and so obtain a dynamic subgrid Prandtl
number from the divergence of the expanded heat flux (Eq. 3.23), a dynamic
subgrid Schmidt number (Eq. 4.8), and closures of the pressure-dilatation,
solenoidal and dilatational dissipation terms of the
$k_{\mathrm{sgs}}$ equation (Eqs. 3.24–3.26). A priori, on box-filtered DNS
of the $M=1.5$ channel, the $C_0$ inferred from each expanded term agrees
with that of Eq. (3.15), and the modelled flux and wall-normal heat flux
correlate with the exact ones at about 0.95 or above, against "much lower"
values for DSM and the dynamic $k_{\mathrm{sgs}}$ model (Figs. 2–4).
A posteriori $C_0$ peaks near 0.08 and the subgrid Prandtl number near 0.8
(Fig. 10). The quasi-dynamic model keeps $Re_\tau=220$, 221 and 218 on the
three grids against 220 in the DNS (Tables 2–4), predicts transition onset
and the skin-friction peak of a supersonic ($M=2.25$) flat-plate boundary
layer on all three grids where DSM and the dynamic $k_{\mathrm{sgs}}$
model fail on the coarsest (Figs. 16–17), and follows the Richtmyer–Meshkov
mixing layer throughout (Figs. 22–23). The authors call the weaker grid
dependence "a certain characteristic of scale adaptivity" (§4.1); it rests
on three grids per flow (Figs. 5, 16). Per step on 112 CPUs it costs $7.22\times10^{-2}$ s
against $4.13\times10^{-2}$ s for DSM and $7.38\times10^{-2}$ s for the
dynamic $k_{\mathrm{sgs}}$ model (Table 5), which the authors call
"slightly longer" than DSM; the ratio is 1.75 *(compiler check, not in the
sources)*.

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

[Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) (§6, Eqs. 6.1–6.9)
derive a dynamic slip length for their volume-filtered
[immersed-boundary](/methods/immersed-boundary-method.md) wall-modelled LES
from the Germano identity, with a test filter of the same kernel type and
width $\hat\Delta>\Delta$. They assume that the slip relation (wall slip
velocity equal to a slip length times the wall-normal gradient of the
filtered velocity) holds instantaneously at both filter levels, and that
for a flat wall the slip length scales as
$(\hat\Delta/\Delta)^{n_1+1}$ between the levels, with $n_1\approx0.53$
the exponent of their a priori fit (page-local). The wall-parallel normal
component of the identity then gives a quadratic for the slip length,
solved explicitly by its positive root, with a separate slip length per
direction. They contrast this with the dynamic slip model of Bose & Moin
(cited), which assumes a linear dependence on the width ratio, one slip
length for all directions and a least-squares solution. The procedure is
proposed but not tested. The slip model itself is on
[wall-modelled LES](/methods/wall-modelled-les.md).

The wall-modelling review of [Bose & Park (2018)](/sources/bose-2018.md)
(§2.3, Eqs. 15–16) describes the first author's dynamic slip-wall model:
a Germano differential filter whose regularization length vanishes at the
wall gives the Robin condition $\bar u_i-C\Delta_w\partial_n\bar u_i=0$
(slip length $C\Delta_w$, page-local), and the slip length is computed by a
Germano-like dynamic procedure, so the model has no empirical coefficient.
It reverts to no slip in laminar regions ($C\Delta_w\to0$, §4.1). The
authors name the robustness of the dynamic procedure, which is "sensitive
to SGS model and numerics", as its limit; Bae & Koumoutsakos (2022, above)
also state that these models are sensitive to the numerical method and
SGS model. Bose & Park also state, citing Sayadi & Moin, that dynamic
procedures deactivate SGS models in laminar boundary layers (§4.1); see
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md) and
[wall-modelled LES](/methods/wall-modelled-les.md).

## Extension to a coefficient tensor

[Agrawal et al. (2022)](/sources/agrawal-2022.md) apply the identity to a
tensor coefficient $C_{ij}$ with four free components, solved by least
squares from a 6×4 system; see the
[dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md).

## Qualifications

- Zhang et al. (2022d) print the dynamic Smagorinsky stress and its
  isotropic part (Eqs. 33–34) without $\bar\rho$, while their subgrid stress
  (Eq. 19) and the Germano terms of Eq. (36) carry it; with Eq. (36) as
  printed the model terms are $C_s^2$ and $C_I$ times density-weighted
  tensors *(compiler check, not in the sources)*. They do not define
  $\lvert\tilde S\rvert$.
- Qi et al. (2022) state no clipping or averaging of $C_0$ or of the
  Smagorinsky coefficient of Eq. (3.21), whose denominator can vanish, and
  in Eqs. (3.23) and (4.8) take $\bar\rho$ and the subgrid Prandtl and
  Schmidt numbers outside the divergence, which is exact only where they
  are locally uniform *(compiler check, not in the sources)*.

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
- Li et al. (2024, arXiv v2) print the dynamic mixed model as
  $\tau_{ij}=C_1\Delta^2\lvert\bar S\rvert\bar S_{ij}+C_2(\cdots)$ (Eq. 9).
  Their Germano tensors (Eqs. 10–11) use
  $h_{1,ij}=-2\Delta^2\lvert\bar S\rvert\bar S_{ij}$, and the least-squares
  formulas solve $L_{ij}\approx C_1M_{ij}+C_2N_{ij}$, which is consistent
  only with $-2C_1\Delta^2\lvert\bar S\rvert\bar S_{ij}$ in the model. The
  printed Eq. (9) is therefore off by a factor $-2$ *(compiler check, not
  in the sources)*.
- Brillon & Nadarajah (2026, arXiv v1) print two different clippings:
  $C_D\in[0,C_S^2]$ with $C_S=0.10$, i.e. an upper bound of 0.01 (§2.6.4),
  and a coefficient "clipped at $C_{max}=0.1$ so that it is never more
  dissipative than the classical Smagorinsky model" (§3.1.8). They print
  $C_D=-\tfrac12\{L_{ij}M_{ij}\}_e/\{M_{ij}M_{ij}\}_e$
  (Eq. 54, with the element average written $\{\cdot\}_e$ here) with $L_{ij}$ in the
  registry sign and
  $M_{ij}=\Delta^2\widehat{\lvert\bar S\rvert\bar S^d_{ij}}-\hat\Delta^2\lvert\hat{\bar S}\rvert\hat{\bar S}^d_{ij}$,
  which is $\Delta^2$ times the $M_{ij}$ of this page; the identity above
  then gives $C_D=+\tfrac12\{L_{ij}M_{ij}\}_e/\{M_{ij}M_{ij}\}_e$,
  so the printed minus sign is inconsistent with the printed $L_{ij}$ and
  $M_{ij}$ *(compiler check, not in the sources)*. They describe the test
  filter as "similar to" their modal high-pass filter (§2.6.4) but also as
  a Galerkin projection to degree 3 (§3.1.8), which is a low-pass
  operation, and their test-filter width is larger than $\Delta$; the table
  above follows the low-pass reading.

- Zhao et al. (2021, Eqs. 15–16) print $\mu_t=\bar\rho C\Delta^2\lvert\bar S\rvert$,
  $L_{ij}$ in the registry sign,
  $M^{\mathrm Z}_{ij}=\hat\Delta^2\lvert\hat{\bar S}\rvert\hat{\bar S}_{ij}-\Delta^2\widehat{\lvert\bar S\rvert\bar S_{ij}}$
  ($M^{\mathrm Z}$ page-local, $-\Delta^2$ times the $M_{ij}$ of this page)
  and $C=[\langle M^{\mathrm Z}_{ij}L_{ij}\rangle/\langle M^{\mathrm Z}_{kl}M^{\mathrm Z}_{kl}\rangle]_+$.
  With the model stress $-2C\Delta^2\lvert\bar S\rvert\bar S_{ij}$ at both
  levels the identity gives $L^d_{ij}=-2CM^{\mathrm Z}_{ij}$ and
  $C=-\tfrac12\langle L_{ij}M^{\mathrm Z}_{ij}\rangle/\langle M^{\mathrm Z}_{kl}M^{\mathrm Z}_{kl}\rangle$;
  the printed formula lacks the factor $-\tfrac12$, and with the printed
  definitions its positive part would keep the anti-dissipative sign
  *(compiler check, not in the sources)*. The paper states no other sign
  convention.
- Volpiani (2024, Eq. 38) prints the numerator of $C_d$ as
  $\langle(L_{ij}-\tfrac13L_{ij}\delta_{ij})M_{ij}\rangle$, where the
  deviatoric part needs the trace $L_{kk}$.
- Pan & Zhang (2023) write the subgrid stress with the opposite sign of
  the registry ($\tau_{ij}-\tfrac13\tau_{kk}\delta_{ij}=+2\nu_t\bar S_{ij}$,
  Eq. 14) and denote the test filter by a tilde; their Eq. (17) agrees with
  the registry's $L_{ij}$ (see the table). They also describe the same LES
  as "the implicit filtered LES approach" of the code (§III.A), see
  [implicit LES](/definitions/implicit-les.md).

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
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1; §3.2; §4.1–4.2, Table 3, Figs. 6, 8–13; App. E.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §II.A, Eq. (12); §III–IV, Figs. 3–17.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §3.3, Eqs. (3.4)–(3.7).
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §2.4, Table 1; §3.3.2.
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — §1.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §II B, Eqs. (7)–(11); §V A 2, Figs. 6–10; §V B 2, Figs. 16–21.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv v1: §2.6.4, Eqs. (53)–(58); §3.1.8, Fig. 19.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — arXiv v3: Fig. 2; App. D.
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §5.1.
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §6, Eqs. (6.1)–(6.9).
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §II.D, Eqs. (14)–(19); §III.A–C, Table II, Fig. 8.
- [Volpiani (2024)](/sources/volpiani-2024.md) — §5, Fig. 15; App. 2, Eqs. (33)–(40).
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §I; §V C, Tables VI–VII.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §III.A, Eqs. (15)–(16); §III.D; §V, Tables III, V–VII, Figs. 2–19; §VI.
- [Li et al. (2021)](/sources/li-2021.md) — §III C, Figs. 2–6.
- [Heinz (2020)](/sources/heinz-2020.md) — §2.1.
- [Bose & Park (2018)](/sources/bose-2018.md) — §2.3, Eqs. (15)–(16); §4.1.
- [Chen et al. (2022)](/sources/chen-2022-g.md) — §4.1, Eqs. (26)–(29); §4.2, Figs. 1–2; §5, Fig. 3.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §3.2, Eqs. (3.8)–(3.26); §4.1, Tables 2–5, Figs. 2–5, 10; §4.2, Figs. 16–17; §4.3, Eqs. (4.6)–(4.8), Figs. 22–23.
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §5.
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §II B; §IV, Figs. 2–4; §V, Figs. 9, 15, Table V.
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §III, Eqs. (12)–(13); App. A, Eq. (A1); §IV B; §IV C, Fig. 8, Table II.
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — App., Eqs. (A1)–(A24); §IV B, Figs. 5–17.
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — Eqs. (33)–(36); §IV B, Figs. 6–15.
- [Li et al. (2022)](/sources/li-2022-k.md) — §I; §II C, Eqs. (6)–(15); §III A, Fig. 3; §III B, Figs. 9–11; §III C, Figs. 16, 18.
