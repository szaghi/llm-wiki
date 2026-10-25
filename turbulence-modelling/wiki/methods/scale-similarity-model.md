---
type: Method
title: "Scale-similarity and mixed subgrid-scale models"
description: "Scale-similarity and deconvolution models build the subgrid stress from the resolved field itself rather than from an eddy viscosity; the sources give Bardina-type and modified-Leonard forms, agree that they reproduce the stress structure but are under-dissipative or unstable alone, and mix them with an eddy viscosity."
status: established
aliases: [similarity model, Bardina model, mixed model, structural SGS model, approximate deconvolution, non-Boussinesq SGS model, modified Leonard stress model, stabilized mixed model, dynamic mixed model]
tags: [les, sgs-model, filtering, combustion]
timestamp: 2026-10-25T19:45:00Z
---

# Scale-similarity and mixed subgrid-scale models

**Structural** (non-Boussinesq) subgrid-scale models estimate the
[subgrid stress](/definitions/large-eddy-simulation.md) $\tau_{ij}$ from the
resolved field without assuming that it is aligned with the resolved strain.
The **scale-similarity model**, attributed by the sources to Bardina et al.
(1980), assumes that the smallest resolved scales interact with the subgrid
scales as the next-larger scales do with the smallest resolved ones, and
builds the stress from products of the resolved velocity re-filtered at a
second level. Deconvolution models recover an approximation of the
unfiltered field from $\bar u$ and filter its products. The
[gradient (Clark) model](/methods/gradient-model.md) is the Taylor-series
member of the class. **Mixed models** add an eddy-viscosity term, usually
[Smagorinsky](/methods/smagorinsky-model.md), to supply the dissipation that
the structural part lacks.

## Forms

[Abe (2021)](/sources/abe-2021.md) (§II B, Eqs. 6–11) prints two forms with
a top-hat test filter $\hat\cdot$ of twice the grid-filter width. Recalling
the Bardina concept $(\bar u_i-\bar{\bar u}_i)(\bar u_j-\bar{\bar u}_j)$
(Eq. 6), the author's **Bardina-type model** (BRD, from the author's
earlier work) is

$$\tau^d_{ij}=C_B\big[(\bar u_i-\hat{\bar u}_i)(\bar u_j-\hat{\bar u}_j)\big]^d,\qquad k_{\mathrm{sgs}}=\frac{C_B}2(\bar u_k-\hat{\bar u}_k)(\bar u_k-\hat{\bar u}_k),\qquad C_B=2,$$

and the **modified-Leonard-stress model** (mLND, concept attributed to
Germano 1986) is

$$\tau^d_{ij}=C_L\,L^d_{ij},\qquad L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j,\qquad C_L=0.5,$$

with $L_{ij}$ the resolved stress of the [Germano identity](/methods/dynamic-procedure.md)
and $k_{\mathrm{sgs}}=\tfrac{C_L}2L_{kk}$. The superscript $d$ denotes the
deviatoric part. The author states that $C_B$ and $C_L$ "were determined
only to successfully predict a reasonable level of the SGS values".

## Agreed properties

- **Good a priori structure, too little dissipation.** The Bardina model
  shows much better tensor correlations with filtered channel DNS than
  eddy-viscosity models a priori, but is under-dissipative a posteriori and
  needs added Smagorinsky dissipation ([Agrawal et al. 2022](/sources/agrawal-2022.md),
  §V). [Vela-Martín (2022)](/sources/velamartin-2022.md) (§2.2) gives the
  same assessment: similarity models reproduce the stress structure and
  give numerically stable [backscatter](/definitions/energy-backscatter.md)
  but are insufficiently dissipative, hence the mixed model (Zang, Street &
  Koseff 1993, as recalled); the tensor-diffusivity model (Winckelmans et
  al. 2001, as recalled) behaves the same way.
  [Prakash et al. (2022)](/sources/prakash-2022.md) (§I–II), citing earlier
  a priori studies, state the same for the whole structural class
  (gradient, similarity, approximate deconvolution): high stress and flux
  correlation, under-predicted local dissipation, and an energy pile-up at
  high resolved wavenumbers.
- **Instability when used alone.** Abe (2021, §V) states that a pure
  scale-similarity model "often causes numerical instability", and recalls
  from the author's earlier work that the $k_{\mathrm{sgs}}$ of BRD did not
  always work a posteriori on coarse grids, which is why the author's mixed
  model carries a transport equation for $k_{\mathrm{sgs}}$ (below).
  Prakash et al. (2022, §II) attribute the instability risk to model
  backscatter through the resolved-energy balance (see
  [gradient model](/methods/gradient-model.md)).
- **Backscatter.** Because the model stress is not tied to the strain,
  $\Pi=-\tau_{ij}\bar S_{ij}$ can be negative locally without the numerical
  instability of a negative eddy viscosity (Vela-Martín 2022, §2.2). In the
  author's view, eliminating backscatter "may be unnecessary or undesirable"
  for such models (§8). This is a difference of emphasis with the two
  sources above, which treat model backscatter as a stability risk to be
  removed.
- **Limits of a priori correlation.** Agrawal et al. (2022, §V) note that
  component-wise correlations do not measure alignment, and Vela-Martín
  (2022, §6.3, §8) shows that equivalent stress representations correlate
  only at 0.4–0.6, so that a poor a priori correlation is not by itself
  evidence of poor modelling. Neither source draws the converse conclusion
  for the high correlation of similarity models. Prakash et al. (2022,
  §III.B.3, §IV) do argue the converse for channel flow, as a hypothesis:
  their optimally clipped model, which keeps the a priori correlation of
  the gradient model, beats standard clipping, which lowers it, at equal a
  priori dissipation.

## A priori evidence on anisotropic cells

Abe (2021, §IV C, Fig. 9) tests the models a priori on a fine LES of the
shear layer behind a [backward-facing step](/benchmarks/backward-facing-step.md)
($Re_\tau=290$ in the driver channel), top-hat filtered in $x$ and $z$ to a
coarse grid whose cells have $\Delta x/\Delta y\sim100$ in the shear layer.
The comparison quantity is the equivalent eddy viscosity of a stress,
$-\tau^d_{ij}\bar S_{ij}/(2\bar S_{kl}\bar S_{kl})$ (Eq. 17), which
reproduces its local energy transfer, forward and backward (see
[energy backscatter](/definitions/energy-backscatter.md)). BRD and mLND
agree well with the reference; mLND matches the instantaneous
$k_{\mathrm{sgs}}$ best, which the author attributes to the high
correlation of its stress with the true one (§IV E, Figs. 12–13). Their
formulas (Eqs. 7–11) contain no filter-width parameter $\Delta$, only the
test filter *(compiler check, not in the sources)*, whereas the cube-root
$\Delta$ suppresses the Smagorinsky viscosity on these cells (see
[large-eddy simulation](/definitions/large-eddy-simulation.md)). The good
a priori agreement sits beside the author's statement (§V) that a pure
similarity model often causes numerical instability.

## Mixed models

**Stabilized mixed model (inline).** Abe (2021, §II C, Eqs. 12–16) uses the
author's stabilized mixed model (SMM), which combines a one-equation eddy
viscosity with a stabilized similarity term:

$$\tau^d_{ij}=-2\nu_t\bar S_{ij}+2k_{\mathrm{sgs}}b^{\mathrm{EAT}}_{ij},\qquad \nu_t=C_{\mathrm{sgs}}f_{\mathrm{sgs}}\sqrt{k_{\mathrm{sgs}}}\,\Delta ,$$

where $b^{\mathrm{EAT}}_{ij}$ (page-local) is the
similarity stress $\tau'_{ij}=(\bar u_i-\hat{\bar u}_i)(\bar u_j-\hat{\bar u}_j)$
minus its linear eddy-viscosity projection $-2\nu'\bar S_{ij}$
with $\nu'=-\tau'^{\,d}_{kl}\bar S_{kl}/(2\bar S_{mn}\bar S_{mn})$ ($\tau'_{ij}$, $\nu'$ page-local), divided by
its trace, minus $\tfrac13\delta_{ij}$. $k_{\mathrm{sgs}}$ obeys a transport
equation with production $-\tau_{ij}\partial_j\bar u_i$, diffusion with
$\nu+\nu_t/\sigma_k$ and dissipation
$C_\varepsilon k_{\mathrm{sgs}}^{3/2}/\Delta+2\nu k_{\mathrm{sgs}}/y^2$;
$f_{\mathrm{sgs}}$ is a wall damping based on a Kolmogorov-velocity wall
coordinate. Constants: $C_{\mathrm{sgs}}=0.05$, $A_0=30$, $C_l=4$,
$C_\varepsilon=0.835$, $\sigma_k=0.5$. The filter width is
$\Delta=\sqrt{\max(\Delta x\Delta y,\Delta y\Delta z,\Delta z\Delta x)}$,
changed from the cube root of the author's original model. The author
states, from earlier work, that the extra term "yields no undesirable extra
energy transfer". On the coarse step grid the SMM gives
a reattachment length (page-local $x_R$) $x_R/H=7.19$ against the experimental 6.51 (+10.4%), and its SGS energy
and shear stress "generally correspond well" to the filtered reference
(§IV A–B, Table II, Figs. 7–8). With the cube-root width (mSMM) the bubble
lengthens to $x_R/H=7.43$ (+14.1%) (§IV D, Table III). The projection
that the SMM removes everywhere is the one that
[optimal clipping](/methods/gradient-model.md) removes where the structural
model backscatters *(compiler check, not in the sources)*. Inagaki & Kobayashi (2020), as recalled by Abe (§V), report that
an algebraic local-equilibrium $k_{\mathrm{sgs}}$ may work on coarse grids.

**Constant and dynamic mixed models.** Prakash et al. (2022, §II, Eq. 7)
recall the mixed model $\tau^{\mathrm M}_{ij}-2(C_G\Delta)^2\lvert\bar S\rvert\bar S_{ij}$
($C_G$ page-local) and its dynamic version, in which the
[dynamic procedure](/methods/dynamic-procedure.md) supplies $(C_G\Delta)^2$
directly because the right $\Delta$ on anisotropic grids is unknown. With
the gradient model as structural part, the dynamic mixed model is the most
accurate model in their channel flow at $Re_\tau=590$ but over-dissipative
in the Taylor–Green vortex at $Re=1600$, and over-predicts intermediate
wavenumbers in forced isotropic turbulence (§III.B). Their **optimal
clipping** derives a mixed model with a pointwise eddy viscosity and no
coefficient; it is on the [gradient-model](/methods/gradient-model.md) page.

## Velocity-gradient (nonlinear) form

Agrawal et al. (2022, App. C, Eq. C3) show that their
[dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
can be rewritten as a Smagorinsky term plus a strain–rotation commutator
term $\propto\Delta^2(\bar S_{ik}\bar\Omega_{kj}-\bar\Omega_{ik}\bar S_{kj})$,
the form of the two-term velocity-gradient expansion of Lund & Novikov (as
recalled). They list the Bardina similarity model, the Clark gradient model
and Stolz–Adams deconvolution as earlier non-Boussinesq models that need an
added Smagorinsky term, whereas their dynamic coefficients supply enough
dissipation without one (§I, §VII.A).

## Approximate deconvolution

[Domingo & Vervisch (2023)](/sources/domingo-2023.md) (§3.1) describe
approximate deconvolution of a resolved scalar $\bar\phi$ in LES of premixed
flames. Inverting the truncated expansion of a Gaussian filter of width
$\Delta$ gives

$$\phi\approx\bar\phi-\frac{\Delta^2}{24}\nabla^2\bar\phi ,$$

which the authors identify with a backward application of the IEM
micro-mixing model with relaxation time $\Delta^2/(24D_\phi)$
($D_\phi$ the molecular diffusivity, page-local). The deconvolved scalar is
used to compute the nonlinear terms, which are then explicitly filtered;
iterative and neural-network variants exist. Domingo & Vervisch compare
this three-dimensional deconvolution with a structural model that
deconvolves with one-dimensional filtered flamelets. A priori, the
flamelet version's error grows with the subgrid flame wrinkling up to a
threshold, for filter widths of 0.75 to 3 laminar flame thicknesses
(Fig. 5). A posteriori, with LES at $170$–$640\ \mu$m, it overestimates the
CH$_4$ and O$_2$ consumption more than the three-dimensional deconvolution,
and it enhances the overestimation of CO (Fig. 6).

The same second-order operator appears as the continuous Germano
differential filter $\bar u=(1-\Delta^2/24\,\nabla^2)^{-1}u$ recalled by
[Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) (§3.4, Eq. 20),
which the formula above inverts exactly, since
$(1-\Delta^2/24\,\nabla^2)\bar u=u$ *(compiler check, not in the sources)*. [Duraisamy (2021)](/sources/duraisamy-2021.md)
(§III.B) recalls the approximate deconvolution of Stolz & Adams, which
inverts a known filter kernel analytically, and contrasts it with
neural-network deconvolution on a local stencil, where no kernel is
assumed. [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§2) run their
wall-modelled channel LES in Nek5000 with its approximate deconvolution
model, a high-pass-filter model "not a simple eddy-viscosity SGS model"
whose relaxation parameter (`filterWeight`, 10) sets the dissipation; the
paper prints no equation.

## Mixed explicit–implicit model

[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§6.5)
test a different mixture: Smagorinsky ($C_s=0.1$, 0.18) added to an
implicit [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
The Smagorinsky part restores the low-wavenumber plateau of the spectral
eddy viscosity and removes the bottleneck, but the total dissipation does
not improve.

## Qualifications

- Abe's (2021) a priori reference is a fine LES with an SGS model, not DNS;
  the author justifies it by the small SGS share of its statistics (§IV B,
  Fig. 5). The a priori comparison projects the stresses on $\bar S_{ij}$
  (equivalent eddy viscosity) rather than correlating components.

# Citations

- [Abe (2021)](/sources/abe-2021.md) — §II B, Eqs. (6)–(11); §II C, Eqs. (12)–(16); §IV A–E, Eq. (17), Tables II–III, Figs. 7–13; §V.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §I–II, Eq. (7); §III.B; §IV.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §I; §V; §VII.A; App. C, Eq. (C3).
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.2; §6.3; §8.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §3.1, Eq. (8), Figs. 5–7.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §3.4, Eq. (20).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.B.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.5, Figs. 20–22.
