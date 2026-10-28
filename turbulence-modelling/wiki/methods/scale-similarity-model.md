---
type: Method
title: "Scale-similarity and mixed subgrid-scale models"
description: "Scale-similarity and deconvolution models build the subgrid stress, or a subgrid scalar variance, from the resolved field rather than from an eddy viscosity; the sources agree that they reproduce the stress structure but are under-dissipative or unstable alone, and mix them with an eddy viscosity, add numerical dissipation, or derive an eddy viscosity from their flux."
status: established
aliases: [similarity model, Bardina model, mixed model, structural SGS model, approximate deconvolution, approximate deconvolution model, ADM, D3M, DIAD, DDM, direct deconvolution model, Layton–Lewandowski model, non-Boussinesq SGS model, modified Leonard stress model, stabilized mixed model, dynamic mixed model, dynamic iterative approximate deconvolution, DIAD_W]
tags: [les, sgs-model, filtering, combustion]
timestamp: 2026-10-28T07:10:00Z
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
member of the class. **Mixed models** add an eddy-viscosity term, such as
[Smagorinsky](/methods/smagorinsky-model.md), to supply the dissipation that
the structural part lacks.

## Forms

[Abe (2021)](/sources/abe-2021.md) (§II B, Eqs. 6–11) prints two forms with
a top-hat test filter $\hat\cdot$ of twice the grid-filter width. Citing
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

[Domaradzki (2024)](/sources/domaradzki-2024.md) (§1, Eqs. 1.3–1.4)
recalls the original Bardina form, built with the grid filter applied
twice, $\overline{\bar u_i\bar u_j}-\bar{\bar u}_i\bar{\bar u}_j$, and the
form of Liu, Meneveau & Katz with a wider test filter,
$c_L(\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j)=c_LL_{ij}$,
tested with $c_L=1$ for the full tensor ($c_L$ page-local). Abe's
$C_L=0.5$ multiplies the deviatoric part of $L_{ij}$ in Abe's own model,
so the two printed coefficients scale different tensors and are not
recorded as a disagreement. Domaradzki (§1) cites Liu et al., who found
good correlations with box and Gaussian filters and much weaker ones with a
sharp spectral cutoff, and Brun, Friedrich & da Silva, who recast the
Métais–Lesieur structure-function
model as a similarity-type model, the one link between the two classes.

## Agreed properties

- **Good a priori structure, too little dissipation.** The Bardina model
  shows much better tensor correlations with filtered channel DNS than
  eddy-viscosity models a priori, but is under-dissipative a posteriori and
  needs added Smagorinsky dissipation ([Agrawal et al. 2022](/sources/agrawal-2022.md),
  §V). [Vela-Martín (2022)](/sources/velamartin-2022.md) (§2.2) gives the
  same assessment: similarity models reproduce the stress structure and
  give numerically stable [backscatter](/definitions/energy-backscatter.md)
  but are insufficiently dissipative, hence the mixed model (Zang, Street &
  Koseff 1993, cited); the tensor-diffusivity model (Winckelmans et
  al. 2001, cited) behaves the same way.
  [Prakash et al. (2022)](/sources/prakash-2022.md) (§I–II), citing earlier
  a priori studies, state the same for the whole structural class
  (gradient, similarity, approximate deconvolution): high stress and flux
  correlation, under-predicted local dissipation, and an energy pile-up at
  high resolved wavenumbers. Domaradzki (2024, §1, §2.3) and
  [Kim et al. (2024)](/sources/kim-2024.md) (§1) recall the same: high
  correlation and accurate backscatter a priori (Bardina et al.; Liu et
  al.), insufficient dissipation, and divergent or inaccurate LES a
  posteriori. Domaradzki explains the missing dissipation by the missing
  information: the similarity stress built from the LES field contains no
  interaction with the true subgrid scales beyond the mesh cutoff, which
  sit in the remainder of the full stress.
- **Instability when used alone.** Abe (2021, §V) states that a pure
  scale-similarity model "often causes numerical instability", and recalls
  from the author's earlier work that the $k_{\mathrm{sgs}}$ of BRD did not
  always work a posteriori on coarse grids, which is why the author's mixed
  model carries a transport equation for $k_{\mathrm{sgs}}$ (below).
  [Qi et al. (2022)](/sources/qi-2022-b.md) (§1) recall the same pairing
  for compressible LES: gradient and scale-similarity models correlate
  highly with the subgrid stress and energy flux but are unstable, citing
  the linear stability analysis of Vreman et al. (1996), while
  eddy-viscosity models are purely dissipative and correlate poorly. Their
  answer, like Abe's, carries $k_{\mathrm{sgs}}$ in a transport equation,
  and uses the structural (gradient) term to set the coefficients of an
  eddy viscosity (see [gradient model](/methods/gradient-model.md)).
  Prakash et al. (2022, §II) attribute the instability risk to model
  backscatter through the resolved-energy balance (see
  [gradient model](/methods/gradient-model.md)).
- **Backscatter.** Because the model stress is not tied to the strain,
  $\Pi=-\tau_{ij}\bar S_{ij}$ can be negative locally without the numerical
  instability of a negative eddy viscosity (Vela-Martín 2022, §2.2). In the
  author's view, eliminating backscatter "may be unnecessary or undesirable"
  for such models (§8). Prakash et al. (2022, §II), above, treat model
  backscatter instead as a stability risk.
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
a reattachment length ($x_R$, registry §11) $x_R/H=7.19$ against the experimental 6.51 (+10.4%), and its SGS energy
and shear stress "generally correspond well" to the filtered reference
(§IV A–B, Table II, Figs. 7–8). With the cube-root width (mSMM) the bubble
lengthens to $x_R/H=7.43$ (+14.1%) (§IV D, Table III). The projection
that the SMM removes everywhere is the one that
[optimal clipping](/methods/gradient-model.md) removes where the structural
model backscatters *(compiler check, not in the sources)*. Abe (§V) cites
Inagaki & Kobayashi (2020), who report that an algebraic local-equilibrium
$k_{\mathrm{sgs}}$ may work on coarse grids.

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

**Compressible dynamic mixed model.** [Helm & Martín (2022)](/sources/helm-2022.md)
(§II, Eqs. 9–10) run LES of hypersonic compression-ramp interactions with
the one-coefficient dynamic mixed model of Martín, Piomelli & Candler
(2000, cited), for the Favre-filtered subgrid stress
$\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$ and the
subgrid heat flux. In registry notation (Favre filter written with the
tilde; the paper writes it with a hat and the test filter with a second
hat), the stress model is

$$\tau_{ij}=-2C_1\Delta^2\bar\rho\lvert\tilde S\rvert\tilde S^d_{ij}+\bar\rho\big(\widehat{\tilde u_i\tilde u_j}-\hat{\tilde u}_i\hat{\tilde u}_j\big),$$

with a dynamic coefficient $C_1$ (page-local) on the eddy-viscosity part
only and unit coefficient on the scale-similar part, which is the
registry's resolved stress $L_{ij}$ built from the Favre-filtered
velocity; the heat-flux model has the same structure with a dynamic
coefficient and a dynamic subgrid turbulent Prandtl number.
$\Delta=(\Delta_\xi\Delta_\eta\Delta_\zeta)^{1/3}$ over the computational
directions, the test filter is a top-hat in computational space, and the
coefficients are averaged in the spanwise direction (see
[dynamic procedure](/methods/dynamic-procedure.md)). The paper prints
these equations in curvilinear coordinates, with the strain of the
transformed velocity and with the density of the scale-similar stress
term written $\rho$ where the heat-flux model has $\bar\rho$. The authors' rationale (§IV F) matches the agreed
properties above: eddy-viscosity models give only a "dissipative drain",
scale-similar models a local exchange between the smallest resolved and
the subgrid scales but too little subgrid dissipation (citing the a
priori study of Martín et al., in which the mixed model improves the
correlation and rms amplitude of the stress and heat flux in compressible
isotropic turbulence).

Their ablation (§IV F, Figs. 30–33) is a posteriori. With the scale-similar
terms switched off (dynamic eddy viscosity only):

- the Mach 3, 24° ramp changes its separation length by less than 5%, and
  the attached Mach 7, 8° ramp its peak corner reverse-flow probability
  from 31% to 35%;
- the separated Mach 7.2, 33° ramp lengthens its separation by 30% (§IV F
  and §V; "as much as a 32%" in the abstract);
- the incoming boundary layers are identical, and the difference sits in
  the separation shear layer, whose spreading rate falls from 0.194 to
  0.173, "nearly a 10% decrease"; lower spreading means lower entrainment
  and a larger bubble.

The authors relate the effect to the convective Mach number of about 2 of
that shear layer (about 1 in the Mach 3 case, taken from their earlier
work) and conclude that the conservative exchange of the scale-similar
term is "necessary for the simulation of this condition" (§V). The
effect is shown for one separated case, computed by LES only (the paper's
DNS cover the boundary layers, the Mach 3 ramp and the attached Mach 7
ramp); see [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Dynamic mixed model as a baseline.** [Wang et al. (2023c)](/sources/wang-2023-c.md)
(§II.A, §III–IV) use a two-coefficient dynamic mixed model, a Smagorinsky
term plus the deviatoric resolved stress $L_{ij}$ at test-filter level
($\hat\Delta=2\Delta$), both coefficients from the Germano identity by
least squares. In forced isotropic turbulence and a temporal mixing layer
it over-dissipates the small scales like dynamic Smagorinsky, though its
subgrid-stress PDFs are better than those of dynamic Smagorinsky (Fig. 4);
its similarity part gives some backscatter in the PDF
of $\Pi=-\tau_{ij}\bar S_{ij}$, where dynamic Smagorinsky is strictly
positive (Fig. 8). The authors' own mixed model, a gradient term with an
ensemble-Kalman-calibrated Smagorinsky coefficient, does better; it is on
the [gradient-model](/methods/gradient-model.md) page. They also recall
that the gradient model is more accurate a priori than the
scale-similarity model (§II.A).

[Li et al. (2024)](/sources/li-2024.md) (§II B, Eqs. 9–11; §V) use a
two-coefficient dynamic mixed model, a Smagorinsky term plus the resolved
stress, as a baseline for a
[neural-operator surrogate](/methods/neural-operator-les-surrogate.md) in
the same two flows. The coefficients are fitted by least squares over the
whole domain, and the structural term at test level needs a second filter
of width $4\Delta$; see the
[dynamic procedure](/methods/dynamic-procedure.md), which also records a
printed factor slip in their Eq. (9). The results are a posteriori:

- **Forced isotropic turbulence** ($Re_\lambda\approx100$, $64^3$). The
  mixed model underestimates the spectrum at low wavenumbers and
  "significantly overestimates" it at high ones. It overestimates the
  structure functions at short separations, and its vorticity PDF deviates
  significantly from filtered DNS. It is less accurate than dynamic
  Smagorinsky there (Figs. 6–10).
- **Temporal mixing layer.** It overestimates the momentum thickness, its
  spectrum is too high at low wavenumbers and too low at high ones, and it
  predicts larger vortical structures than filtered DNS (Figs. 16–21).
  This matches the over-prediction of structure size reported by Wang et
  al. (2023c).
- **Cost.** Its cost per time node is 166.4 CPU s against 105.6 s for
  dynamic Smagorinsky in isotropic turbulence (Table I).

[Li et al. (2021)](/sources/li-2021.md) (§III C, Figs. 2–8) run the
dynamic mixed model of Liu, Meneveau & Katz (cited; formula not printed)
as a comparator of a gene-expression-programming model in a posteriori LES
of forced isotropic turbulence ($128^3$, filter width 16 DNS spacings,
$Re_\lambda\approx260$). Its spectrum is damped near the cutoff like that
of dynamic Smagorinsky, and it underpredicts the small-separation
structure functions. Its anisotropic-stress PDFs are better than dynamic
Smagorinsky's, which the authors attribute to the scale-similarity part,
but its PDF of the subgrid flux $\Pi$ still "differs significantly" from
filtered DNS, and its stress structures are larger and more diffuse,
attributed to extra dissipation. The learned tensor-basis model (see
[gradient model](/methods/gradient-model.md) for its coefficients) does
better on all these measures at a lower cost per iteration than this
model (§III F, Fig. 13).

**Splitting dissipative and non-dissipative parts.**
[Maejima & Kawai (2025)](/sources/maejima-2025.md) (§1) recall the same
assessment as the agreed properties above. The scale-similarity model of
Bardina et al. reproduces the stress components "more accurately" but
poorly predicts the dissipation. Abe's 2013 model, which they cite, splits the
subgrid stress into dissipative and non-dissipative parts and so improves
coarse-grid wall turbulence. Analyses of that model, they write, showed
that the added terms redistribute velocity fluctuations among directions.
Their own [super-resolution model](/methods/super-resolution-sgs-model.md)
reaches a similar redistribution through spanwise
[backscatter](/definitions/energy-backscatter.md) (§6.2.3).

**Dynamic mixed models with one and two parameters.** [Kang et al. (2023)](/sources/kang-2023.md)
(§3.3, Eqs. 3.4–3.8) compare three algebraic dynamic mixed models with a
learned one in isotropic turbulence and channel flow:

- the one-parameter dynamic mixed model (DMM; Zang, Street & Koseff,
  modified by Vreman, Geurts & Kuerten, cited),
  $\tau^d_{ij}=-2C\Delta^2\lvert\bar S\rvert\bar S_{ij}+\big[\overline{\bar u_i\bar u_j}-\bar{\bar u}_i\bar{\bar u}_j\big]^d$,
  whose similarity part is the modified Leonard term (Bardina et al.;
  Germano, cited) and whose coefficient comes from the
  [dynamic procedure](/methods/dynamic-procedure.md) applied to $L_{ij}$
  minus the test-level difference of the similarity term. The second term
  of that difference, Eq. (3.4), is illegible in the version of record
  (colliding accents); it is not reconstructed here;
- two two-parameter models after Anderson & Meneveau (cited), with
  dynamic coefficients on both the Smagorinsky term and the structural term,
  the resolved stress $L_{ij}$ (DTM$_{\mathrm{sim}}$) or the Clark
  [gradient](/methods/gradient-model.md) term (DTM$_{\mathrm{nl}}$); the
  formulas are on the [dynamic procedure](/methods/dynamic-procedure.md)
  page.

Results (Tables 4, 6, 9, Figs. 19–22, 24): a priori correlations of the
traceless stress with filtered DNS in isotropic turbulence are 0.71–0.72
(DMM), 0.52–0.54 (DTM$_{\mathrm{sim}}$) and 0.91 (DTM$_{\mathrm{nl}}$),
against 0.27–0.30 for dynamic Smagorinsky; in channel flow at
$Re_\tau=180$ DMM has the best shear-stress correlation, 0.88. All three
need averaging and clipping to stay stable; in decaying isotropic
turbulence the similarity coefficient of DTM$_{\mathrm{sim}}$ turns
negative and is clipped, so the model degenerates to dynamic Smagorinsky.
They cost 1.6–2.2 times dynamic Smagorinsky per stress evaluation. A
[neural-network mixed model](/methods/neural-network-sgs-model.md) that
takes $\bar S_{ij}$ and $L_{ij}$ as inputs, with an a priori correlation
comparable to that of DMM (0.70–0.72), gives the most accurate spectra and energy decay of
all models in decaying isotropic turbulence, needs no averaging or
clipping, and costs 0.71 times dynamic Smagorinsky: "higher correlation
coefficients of the SGS stress in an a priori test do not guarantee more
accurate LES results" (§3.3). Among the similarity inputs
tested (modified Leonard term, $L_{ij}$, gradient term), $L_{ij}$ works
best; the authors call it "the most important factor for generalization to
an untrained turbulent channel flow" (§3.7, App. C).

**Similarity stress as an energy-transfer-free anisotropic term.**
[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (§IV B, Eq. 19,
Fig. 13) test the similarity part of the stabilized mixed model (the
"SGS-Reynolds" term $(\bar u_i-\hat{\bar u}_i)(\bar u_j-\hat{\bar u}_j)$,
$\hat\Delta/\Delta=2$), with its eddy-viscosity projection removed and
scaled by the exact subgrid energy, as a model of the anisotropic remainder
of the subgrid stress (see [energy backscatter](/definitions/energy-backscatter.md)).
A priori on channel DNS at $Re_\tau=400$ with a coarse filter
($\Delta x^+,\Delta z^+=105,52.4$) it is the closest of three models to
the filtered-DNS anisotropic redistribution; it gives the right
(productive) sign of the spanwise component even without the projection
removed, but with small intensity. The gradient version is farther from
filtered DNS, and a quadratic strain–rotation model gives the wrong sign of
the spanwise component. Variants that keep the energy transfer of the
structural term give strongly negative streamwise redistribution, far from
filtered DNS. Their earlier study (Inagaki & Kobayashi 2020, cited)
found the similarity version better than the gradient version a
posteriori, because it amplifies small-scale fluctuations near the cutoff.

**Similarity model as a pretraining target.** [Kim et al. (2022)](/sources/kim-2022.md)
(§II D) report that pretraining their reinforcement-learning SGS model on
the scale-similarity model made the training unstable because the LES
itself was numerically unstable, which, they write, suggests that clipping
is needed; they do not use it as a
baseline "because the DSM usually outperforms it" (§II, §I). No results
are shown for either statement.

**Similarity stress as the source of an eddy viscosity.** Domaradzki
(2024, §2.4) uses the similarity stress not as the closure but as the
carrier of the energy transfer: its local flux $-L_{ij}\hat{\bar S}_{ij}$,
filtered once more, divided by $\lvert\hat{\bar S}\rvert^2$, gives an
eddy viscosity with no adjustable constant, applied in Boussinesq form (the
[autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)).
Its subgrid transfer correlates with that of the similarity stress at
0.81, against about 0.4 quoted for Smagorinsky, and it keeps local
backscatter without instability in isotropic turbulence (§3.1). The author
reads $L_{ij}$ of a Gaussian filter also as a deconvolution model, the
Gaussian being exactly invertible (§3.1). Domaradzki (§1) cites Bardina
et al. and Liu et al. for the statement that similarity and deconvolution
models fail in actual LES; the paper runs no LES with the similarity
stress itself as the closure (§3).

### Mixed similarity model in wall-modelled LES of a separated flow

[Zhou & Bae (2024)](/sources/zhou-2024-b.md) (§2.1, Eq. 1) use the mixed
similarity model of Bardina et al. and Sarghini, Piomelli & Balaras
(cited), with explicit filtering,

$$\tau_{ij}=-2(C_s\Delta)^2\lvert\bar S\rvert\bar S_{ij}+\big(\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j\big),$$

that is a Smagorinsky term with $C_s=0.13$ ("without undergoing any
optimization") and the similarity term $L_{ij}$ with unit coefficient, the
secondary filter $\hat\cdot$ "chosen here as Gaussian filtering" (width
not printed) and $\Delta$ the cube root of the cell volume. They call it
"a nonlinear model capable of accounting for the anisotropy of SGS
stress". In wall-modelled LES of the spanwise-periodic
[Gaussian bump](/benchmarks/gaussian-bump.md) at $Re_L=2\times10^6$ with
the reference mean wall stress imposed:

- **Larger bubble, consistent across meshes** (§3.1, Figs. 4, 8, 9). The
  model over-predicts the separation bubble ("significantly larger" than
  the reference on the baseline mesh) and the leeward boundary-layer
  thickness, but gives bubble sizes consistent across four isotropic
  meshes, which the authors read as a possible benefit of the stress
  anisotropy.
- **Highest dissipation** (§3.1, Figs. 7, 10–11). It gives the highest
  subgrid dissipation $-\tau_{ij}\bar S_{ij}$ at all stations and the
  lowest first-cell velocity ("strong near-wall dissipation"), and
  subgrid dissipation dominates the viscous one throughout the boundary
  layer.
- **Anisotropic cells** (§3.3, Fig. 17). On cells of aspect ratio
  $4:1:2$ the bubble is enlarged on the two coarsest meshes and strongly
  reduced on the baseline one, so the mesh consistency seen on isotropic
  meshes is lost; the authors attribute this to the cube-root filter width.

## Velocity-gradient (nonlinear) form

Agrawal et al. (2022, App. C, Eq. C3) show that their
[dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
can be rewritten as a Smagorinsky term plus a strain–rotation commutator
term $\propto\Delta^2(\bar S_{ik}\bar\Omega_{kj}-\bar\Omega_{ik}\bar S_{kj})$,
the form of the two-term velocity-gradient expansion of Lund & Novikov (cited). They list the Bardina similarity model, the Clark gradient model
and Stolz–Adams deconvolution as earlier non-Boussinesq models that need an
added Smagorinsky term, whereas their dynamic coefficients supply enough
dissipation without one (§I, §VII.A).

## Approximate deconvolution

**Historical origin, as recounted.** [Kim & Leonard (2024)](/sources/kim-2024-b.md)
(§3.1, §2.2) recall that Leonard's formal derivation of the filtered
equations (1973, 1974) produced, beside the stresses to be modelled, "an
additional, deterministic stress-like term that would account for some of
the SGS stresses without modeling", now called the tensor-diffusivity
model (Leonard 2015) and "the first term of the deconvolution method"
(Stolz et al. 2001), all cited. With the Orszag–Patterson spectral code,
Leonard and Patterson (unpublished, 1973) found that about 40% of the
total nonlinear transfer to the subgrid scales was due to the filtered
nonlinear term. No equation is printed; the tensor-diffusivity model is
an alias of the [gradient model](/methods/gradient-model.md) in this
bundle.


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
differential filter $\bar u=(1-\Delta^2/24\,\nabla^2)^{-1}u$ cited by
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

**The approximate deconvolution model (ADM) and its two filters.**
[Caban et al. (2026)](/sources/caban-2026.md) (§2, Eqs. 8–12) write the
Stolz–Adams model for incompressible LES as
$\tau_{ij}=\overline{u^*_iu^*_j}-\bar u_i\bar u_j$, with the deconvolved
velocity $u^*_i=Q\,\bar u_i$ from the truncated van Cittert series

$$Q=\sum_{n=0}^{N_{\mathrm{AD}}}(I-G_{\mathrm{EF}})^n,\qquad \hat Q=\frac{1-(1-\hat G_{\mathrm{EF}})^{N_{\mathrm{AD}}+1}}{\hat G_{\mathrm{EF}}},$$

so that the momentum equation carries $\partial_j\overline{u^*_iu^*_j}$ and
no explicit dissipation. Here $N_{\mathrm{AD}}$ (registry §11) is the number
of series terms, $N_{\mathrm{AD}}=5$ in their LES, and $G_{\mathrm{EF}}$
(page-local) is the "effective filter" assumed in the inversion, which
need not be the LES filter $G$ that forms $\overline{u^*_iu^*_j}$ (§4). The
authors model the filter that the discretization itself imposes,
$\mathcal F_h$ (registry), as the product of the filters induced by the
first-derivative scheme and by the interpolations of their half-staggered
grid (see [numerical dissipation](/properties/numerical-dissipation.md)),
and try $G_{\mathrm{EF}}=\mathcal F_hG$, $G$, $\mathcal F_h$, or explicit
compact and finite-difference filters of orders 2–10. If the true filter
acting on the solution is $H$ (page-local), the deconvolution error is
$\hat{\mathcal E}=1-\hat Q\hat H$ (page-local), which tends to
$1-\hat H/\hat G_{\mathrm{EF}}$ as $N_{\mathrm{AD}}\to\infty$ and so does
not vanish (§4.1, Eqs. 36–37): deconvolving with a filter of higher order
than $H$ attenuates $u^*$, one of lower order amplifies it near the filter
cutoff. A priori on isotropic-turbulence DNS at $Re_\lambda=100$
($384^3$, LES grid $64^3$, Gaussian $G$ with $\Delta=2h$), the stress error
is largest at high wavenumbers for every $G_{\mathrm{EF}}$, including the
exact numerical one; with a second-order finite-difference
$G_{\mathrm{EF}}$ it grows with $N_{\mathrm{AD}}$, with second- and
fourth-order compact filters it falls up to $N_{\mathrm{AD}}=4$–6 and
then stays constant, and the authors advise a small $N_{\mathrm{AD}}$
(§4.2, Fig. 8).

The **Layton–Lewandowski model** is the case $N_{\mathrm{AD}}=0$,
$u^*_i=\bar u_i$ (Caban et al. 2026, Eq. 12):
$\tau_{ij}=\overline{\bar u_i\bar u_j}-\bar u_i\bar u_j$, so that the
resolved momentum equation is the unclosed one with its advective term
filtered, $\partial_t\bar u_i+\partial_j\overline{\bar u_i\bar u_j}+\dots$.
The authors place it in the scale-similarity family of Bardina; its second
term is not re-filtered, unlike the Bardina form cited by Domaradzki
above *(compiler check, not in the sources)*. They note it "has not gained
widespread popularity".

**Results in the transitional Taylor–Green vortex** at $Re=1600$, LES on
$64^3$ against their own DNS, error of the kinetic-energy history up to
$t=20$ (Caban et al. 2026, §5.4, Tables 4–9; see
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)):

- the Layton–Lewandowski model is stable with every explicit LES filter
  tested (finite-difference and compact, orders 2–6) even with the
  non-dissipative spectral interpolation, with which the no-model,
  Smagorinsky and Vreman runs at $\Delta=2h$ are unstable; its best error,
  $2.03\times10^{-2}$ with a sixth-order compact filter and explicit
  regularization, is about 10% below the best implicit LES (§5.4.1,
  Table 5);
- ADM with $N_{\mathrm{AD}}=5$ is unstable with non-dissipative
  interpolation for most filter combinations, which the authors attribute
  to deconvolution amplifying the subfilter energy and the aliasing of
  $u^*_iu^*_j$; it is stable with dissipative interpolation or explicit
  regularization, so it "requires some level of numerical dissipation", in
  line with the relaxation term of Stolz and Adams (§5.4.2, §6);
- the best ADM ($G$ and $G_{\mathrm{EF}}$ both sixth-order compact filters,
  dissipative interpolation) gives $2.31\times10^{-2}$, about twice as
  accurate as the eddy-viscosity models but no better than the
  Layton–Lewandowski model or [implicit LES](/definitions/implicit-les.md);
  ADM "does not deliver the anticipated improvement" (§5.4.2, §6);
- building the numerically induced filter into $G_{\mathrm{EF}}$ helps only
  when $G$ is of low order (§5.4.2, Tables 7–9).

The authors restrict these conclusions to $Re=1600$ on $64^3$, and the
interpolation effects to staggered or half-staggered algorithms (§6).
Their treatment of the numerically induced filter as part of the
closure is the theme of [discretization-consistent closures](/definitions/discretization-consistent-closure.md).

[Jakhar et al. (2026)](/sources/jakhar-2026.md) (p. 5) view the
finite-order gradient closures as truncations of the nonlocal
deconvolution operator, their fourth-order one being "the minimal local
truncation" that captures the leading nonlocal effects (see
[gradient model](/methods/gradient-model.md)).

**Compressible ADM with a differential filter on unstructured grids.**
[Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) (§2, Eqs. 3–6)
write the same van Cittert iteration, $u^{(j+1)}=u^{(j)}+(\bar u-Gu^{(j)})$
from $u^{(0)}=\bar u$, whose truncation after $N_{\mathrm{AD}}$ terms
recovers $u$ up to an error of order $\delta_{\mathrm G}^{2(N_{\mathrm{AD}}+1)}$
or higher in the filter radius $\delta_{\mathrm G}$ (registry §11), and
close the nonlinear terms by $\overline{uu}\approx\overline{u^*u^*}$. They
note that ADM represents the interactions among scales above the grid
cut-off and the dissipative effect of the subgrid scales, while the
interactions below the cut-off need a functional model or a
regularization (§2, citing Stolz et al.). They adopt the form of Mathew et
al. (cited), in which all equations are solved for deconvolved variables,
$\partial_tu^*+\partial_jF_j(u^{**})\approx0$, "to avoid using the penalty
regularization method" (Eq. 6), and add no eddy viscosity: at each step
the Favre-filtered conserved variables are filtered by the
[differential filter](/methods/explicit-modal-filtering.md) of the paper
and deconvolved again (Algorithm 1), on a continuous-Galerkin
finite-element discretization with RK4. Filtering and deconvolution are
thus the only closure. The order $N_{\mathrm{AD}}=8$ follows the
literature they cite (§6.1); runs use orders 5, 7, 8 and 10 and a
"relaxation factor" of 0.8, whose place in the equations is not printed
(§6.2). The approximate velocity $u\approx Q\bar u$ is used for all
reported statistics (§6.2). Results:

- **Decaying isotropic turbulence** of Comte-Bellot & Corrsin on $64^3$
  Cartesian, 20%-perturbed and tetrahedral meshes ($N_{\mathrm{AD}}=8$):
  the energy spectrum follows the $-5/3$ range with complete suppression
  at the grid cut-off; the tetrahedral mesh is slightly more dissipative
  but keeps some energy beyond the structured cut-off, because the filter
  follows the smaller local element size (§6.1, Fig. 6; see
  [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).
- **[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)** at
  $Re=1600$, $M=0.1$, on $64^3$ (274 625 nodes): the energy-based
  dissipation rates of all orders coincide up to $t^*\approx4$, so
  filtering and deconvolution leave the laminar stage alone; between
  $t^*=4$ and 7 a higher order dissipates less, and the vorticity-based
  dissipation becomes more accurate with increasing order because scales
  near the cut-off are kept. $N_{\mathrm{AD}}=10$ stays stable but its
  energy-based rate oscillates and slightly over-predicts the peak, which
  the authors attribute, as a conjecture, to a temporary energy pile-up
  near the cut-off or to aliasing (§6.2, Fig. 10). No energy pile-up at
  the grid cut-off appears in any LES spectrum (Fig. 13).
- **Against flux reconstruction.** The authors report their $64^3$
  results as more accurate in both dissipation measures than the
  flux-reconstruction LES of Bull & Jameson (cited), printed as having
  "128 degrees of freedom, i.e. p1 Legendre polynomials on a $64^3$ grid"
  (§6.2, Fig. 10).
- **Grid quality.** A 10% grid perturbation changes the dissipation only
  after the peak ($t^*\approx9$); a 20% perturbation under-estimates it
  before the peak, over-estimates it after and delays the peak to
  $t^*\approx10$, and the authors conjecture ("merely conjectures") that
  grid anisotropy delays the breakdown of anisotropic vortices. On the
  unstructured mesh the peak comes earlier ($t^*\approx7.6$ and 8.5 for
  orders 8 and 10) and lower, which they attribute to the stronger filter
  on linear tetrahedra (§6.2, Figs. 11–12).

## Deconvolution models under explicit filtering: an a priori ranking

[Valencia et al. (2026)](/sources/valencia-2026.md) compare four
deconvolution closures with the [dynamic](/methods/dynamic-procedure.md)
Smagorinsky (DSM) and dynamic mixed (DMM) models, a priori, in
compressible decaying [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
(DNS on $512^3$, initial turbulent Mach number 0.6 and Taylor Reynolds
number 100). All are cast in explicitly filtered LES (see
[large-eddy simulation](/definitions/large-eddy-simulation.md)), where an
explicit Gaussian filter of width $\Delta$ acts on a grid of spacing $h$
and the filter-to-grid ratio $\Delta/h$ (FGR) is the free parameter. A
generic deconvolution operator $D$ gives $\phi^*=D\bar\phi$ for density
and the Favre-weighted momentum and energy, and the model stress is the
explicitly filtered difference

$$\tau^{\mathrm{ef}}_{ij}=\overline{\rho^*u^*_iu^*_j}-\overline{\bar\rho^*\tilde u^*_i\tilde u^*_j}$$

(§III, Eqs. 31–33; $\phi^*$, $D$ page-local, $\tau^{\mathrm{ef}}_{ij}$
registry §11),
with the Gaussian kernel of transfer function
$\hat G(k)=\exp(-k^2\Delta^2/24)$ (Eqs. 30, 48). The four operators are:

- **ADM**, the truncated van Cittert series $\sum_{n=0}^{N_{\mathrm{AD}}}(I-G)^n$
  written above, whose $N_{\mathrm{AD}}=0$ "reduces to the
  scale-similarity model" (§III A, Eqs. 34–36, Table I); order 5 is
  selected;
- **D3M**, the discrete direct deconvolution model: the Taylor series of
  the Gaussian filter inverted term by term and truncated on a
  three-, five- or seven-point stencil, the second-order one being
  $\phi^*_j=-\tfrac{1}{24}(\Delta/h)^2(\bar\phi_{j+1}+\bar\phi_{j-1})+\tfrac1{12}\big(12+(\Delta/h)^2\big)\bar\phi_j$,
  the stencil form of their second-order inverse
  $\phi^*=\bar\phi-\tfrac{\Delta^2}{24}\partial_x^2\bar\phi$ (Eq. 40), which
  is the one-dimensional form of the operator of Domingo & Vervisch above
  (§III B, Eqs. 37–42, Table II); order 4 is selected;
- **DIAD**, the dynamic iterative approximate deconvolution: weights on an
  $N_{\mathrm{st}}^3$ stencil ($N_{\mathrm{st}}$ registry §11) fitted by constrained least squares
  from resolved data only, with the weights summing to one, iterated
  (§III C, Eqs. 43–46); $N_{\mathrm{st}}=5$, filter-to-stencil ratio 2 and two
  iterations are selected;
- **DDM**, the spectral direct deconvolution: exact inversion of
  $\hat G$, bounded in magnitude by $1/\varepsilon_{\mathrm{DD}}$ with
  $\varepsilon_{\mathrm{DD}}=0.01$ (registry §11), which needs FFTs, hence a
  periodic uniform grid (§III D, Eqs. 47–50).

**Protocol.** The DNS is top-hat filtered, to emulate the implicit filter
of a centred finite-volume scheme, downsampled to an LES grid, then
explicitly Gaussian filtered at FGR 1, 2 or 4 (§V A). The reference is the
*total* unresolved stress, the sum of a grid-truncation part, which no
deconvolution recovers, and the subfilter part,
$\tau^{\mathrm{tot}}_{ij}=\tau^{\mathrm{gr}}_{ij}+\tau^{\mathrm{sf}}_{ij}$,
under the assumption that the explicit filter and the grid projection
commute (§II C, Eqs. 23–29). For a given grid the grid-truncation energy
hardly depends on FGR (1.3% of the kinetic energy on $128^3$, 5.0–5.3% on
$64^3$, 16.4–17.0% on $32^3$), while the subfilter energy grows with it
and exceeds the grid-truncation energy from FGR 2 on (Table IV). The three
retained cases share $\Delta=16h_{\mathrm{DNS}}$ ($h_{\mathrm{DNS}}$ the
DNS spacing, page-local): $128^3$ at FGR 4, $64^3$ at FGR 2, $32^3$ at
FGR 1. Accuracy is measured by the correlation coefficient and the
relative rms error of $\tau_{xx}$ and $\tau_{xy}$ (Eqs. 53–54).

**Results** (Tables V–VII; $C_{xx}$, $C_{xy}$, relative errors
$E_{xx}$, $E_{xy}$):

| model | FGR 2: $C_{xx}$ / $C_{xy}$ | FGR 2: $E_{xx}$ / $E_{xy}$ | FGR 4: $C_{xx}$ / $C_{xy}$ | FGR 4: $E_{xx}$ / $E_{xy}$ |
|---|---|---|---|---|
| ADM | 0.9795 / 0.9839 | 0.2469 / 0.1946 | 0.9968 / 0.9976 | 0.0909 / 0.0755 |
| D3M | 0.9792 / 0.9838 | 0.2445 / 0.1931 | 0.9972 / 0.9980 | 0.0897 / 0.0712 |
| DIAD | 0.9735 / 0.9800 | 0.2649 / 0.2153 | 0.9946 / 0.9964 | 0.1023 / 0.0892 |
| DDM | 0.9809 / 0.9849 | 0.2402 / 0.1881 | 0.9989 / 0.9992 | 0.0626 / 0.0457 |
| DSM | 0.2726 / 0.1369 | 1.2955 / 1.0203 | 0.2562 / 0.1156 | 1.9644 / 1.0459 |
| DMM | 0.9057 / 0.9144 | 0.4923 / 0.4543 | 0.9126 / 0.9089 | 0.4386 / 0.4483 |

- FGR 1 is excluded for its "extremely poor" ADM performance (correlation
  below 0.15, relative error above 0.98 at order 5); the authors attribute
  the gain at FGR 4 to the larger share of the subfilter stress in the
  total stress, and the residual error at lower FGR to grid truncation
  (§V B 1).
- DDM is the most accurate and serves as a practical upper bound for
  periodic flows; DIAD is the least accurate deconvolution model; D3M
  improves monotonically with its order and is "more sensitive to FGR"
  than ADM (§V B 2–4).
- The deconvolution models improve strongly from FGR 2 to FGR 4, the
  eddy-viscosity-based DSM and DMM hardly change, which the authors read
  as a structural limitation of eddy-viscosity formulations (§V C).
- DSM gives narrow $\tau_{xy}$ and shifted $\tau_{xx}$ distributions and
  wrong stress spectra at all scales; DMM is better but under-predicts the
  tails and the spectral content (§V C, Figs. 20–23).
- Costs are taken from cited a posteriori work (refs. 5, 30), not measured: D3M and DDM at
  about 20% of the ADM cost, ADM about half the DMM cost, DIAD "generally
  the most computationally demanding" deconvolution model (§V C).

The authors conclude that the filter-to-grid ratio is the decisive
parameter and that compensating for the explicit filter is "a requirement
fulfilled exclusively by deconvolution-based approaches" (§VI). This rests
on a priori correlation in isotropic turbulence; they defer a posteriori
stability, wall-bounded and shock-laden flows and non-uniform grids to
future work (§V C, §VI). A posteriori, Caban et al. (2026, above) find
that ADM needs numerical dissipation and does not beat implicit LES; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

## Iterative deconvolution in compressible LES, a posteriori

Two papers of one group run the dynamic iterative approximate
deconvolution (DIAD, after Yuan et al. 2021, cited) in actual compressible
LES of decaying isotropic turbulence, with a Gaussian filter of width 16
DNS spacings, an LES grid of spacing $\Delta/2$ and filtered DNS as the
reference. The algorithm is the one listed above: starting from
$\phi^0=\bar\phi$, each iterate is a weighted sum of filtered values on an
$N_{\mathrm{st}}^3$ stencil, the weights solve a constrained least-squares
system built from domain averages of the filtered iterate with the weights
summing to one, and the iteration stops after a set number of steps or
when the refiltered iterate matches $\bar\phi$ within a tolerance
(Algorithm 1 of both). Both use $N_{\mathrm{st}}=3$, stencil spacing
$\Delta/2$ and two iterations, and both evaluate the closure in the
scale-similarity form, e.g. $\overline{\rho^*u^*_iu^*_j}-\overline{\rho^*}\,\overline{u^*_i}\,\overline{u^*_j}$,
rather than the direct form $\overline{\rho^*u^*_iu^*_j}-\bar\rho\bar u_i\bar u_j$,
because Yuan et al. (cited) showed it to satisfy symmetry and
realizability conditions.

- **Density-unweighted filtering.** [Zhang et al. (2022b)](/sources/zhang-2022-f.md)
  close all subgrid terms of the plain-filtered compressible equations
  (stress, mass flux, density–temperature correlation, heat flux,
  turbulent diffusion; see [large-eddy simulation](/definitions/large-eddy-simulation.md))
  with ADM (van Cittert, $N_{\mathrm{AD}}=4$, recommended 3–5 for
  stability), DIAD, the [gradient model](/methods/gradient-model.md), and
  density-unweighted versions of the dynamic Smagorinsky (DSM) and dynamic
  mixed (DMM) models with two least-squares coefficients per term (§III B,
  App. Eqs. A1–A24), at $M_t=0.4$ and 0.8 ($1024^3$ DNS, LES $128^3$). A
  priori, ADM and DIAD correlate above 0.98 with the exact stress and heat
  flux, with relative errors below 0.2, DIAD best; DIAD improves
  significantly from one to two iterations and hardly beyond (§IV A,
  Figs. 1–3). A posteriori, DIAD best reproduces the kinetic-energy decay,
  spectra, PDFs of the subgrid flux, deviatoric stress, strain, vorticity
  and heat flux; ADM is under-dissipative, over-estimating the
  high-wavenumber energy and under-estimating the mean subgrid flux; DSM
  and DMM are over-dissipative with narrow PDFs (§IV B, Figs. 5–23). The
  left (backscatter) tail of the subgrid-flux PDF lengthens with $M_t$
  (see [energy backscatter](/definitions/energy-backscatter.md)). Cost per
  step on 32 cores: gradient model 0.32 s, ADM 0.68 s, DSM 0.85 s, DIAD
  0.87–0.88 s, DMM 1.41 s (Table III).
- **Dense gas.** [Zhang et al. (2022d)](/sources/zhang-2022-h.md) apply
  DIAD to a dense gas (the perfluorocarbon PP11 near its critical point,
  Martin–Hou equation of state), whose Favre-filtered equations carry
  thermodynamic subgrid terms because pressure and internal energy are
  nonlinear in density and temperature: a subgrid pressure, a subgrid
  pressure work, an internal-energy correlation and an internal-energy
  flux (§II, Eqs. 18–23, after Giauque et al., cited; see
  [large-eddy simulation](/definitions/large-eddy-simulation.md)). DIAD
  evaluates every term in scale-similar form with the equation of state
  applied to the deconvolved fields, e.g. the subgrid pressure as
  $\overline{p(\rho^*,T^*)}-p(\bar\rho^*,\tilde T^*)$ (Eqs. 26–32). A
  priori ($512^3$ DNS, LES $64^3$, $M_t=0.4$ and 0.8) the correlations
  exceed 0.98 with relative errors below 0.2, except the internal-energy
  flux at $M_t=0.4$ (above 0.96, error below 0.3) (§IV A, Figs. 1–2). A
  posteriori, DIAD and DIAD without the thermodynamic terms (DIAD_W) both
  beat a DSM with dynamic isotropic part, which is over-dissipative; DIAD
  reproduces the PDFs of the pressure work and internal-energy flux and,
  at $M_t=0.4$, of the subgrid pressure, whose negative tail it
  under-estimates at 0.8; dropping the thermodynamic terms changes the
  velocity and thermodynamic spectra little "in the present study"
  (§IV B, Figs. 3–18; §V). Cost per step: DSM 0.24 s, DIAD_W 0.27–0.28 s,
  DIAD 0.33–0.34 s (Table VI).

**Relative accuracy of DIAD, side by side.** Valencia et al. (2026) rank
DIAD the least accurate of their four deconvolution models a priori and
the most costly (table above), while Zhang et al. (2022b) find it more
accurate than ADM, the gradient model and the dynamic models, a priori and
a posteriori, and Zhang et al. (2022d, §I) cite that result. The set-ups
differ: Valencia et al. use explicitly filtered LES, a reference that
includes the grid-truncation stress, Favre deconvolution with
$N_{\mathrm{st}}=5$ and ADM of order 5; Zhang et al. use the filtered-DNS
subfilter stress, density-unweighted fields, $N_{\mathrm{st}}=3$ and ADM
of order 4. At filter-to-grid ratio 2 the gaps in Valencia et al.'s
correlations are small (DIAD 0.9735 against ADM 0.9795 for $\tau_{xx}$).

**Dynamic mixed model in incompressible LES.** [Wang et al. (2022)](/sources/wang-2022-j.md)
(§II B, §IV–V) use the two-coefficient DMM (Smagorinsky term plus the
resolved stress at test-filter level, least-squares coefficients) as a
baseline: in forced isotropic turbulence and a temporal mixing layer it
over-estimates low-wavenumber and under-estimates high-wavenumber energy,
produces larger vortical structures than filtered DNS, is worse than DSM
in momentum thickness, and induces strip-shaped noise in a mixing layer
seeded with linear-stability modes (Figs. 2, 9, 16, 18–20); its multiple
filtering operations make it 2.1–2.3 times as costly as DSM (Table V).
Their constant-coefficient spatial gradient model is on the
[gradient-model](/methods/gradient-model.md) page.

**Deconvolution and subgrid-velocity reconstruction.**
[Hausmann et al. (2022)](/sources/hausmann-2022.md) (§I) note that
deconvolution recovers no length scales below the LES cutoff (citing the
dynamic deconvolution of Park et al.), which motivates their
[subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md)
when the small-scale velocity itself is needed.

## Similarity model for a subgrid scalar variance

The similarity idea also closes scalar second moments. In LES of
supersonic hydrogen combustion with a flamelet/progress-variable table,
[Tang et al. (2022)](/sources/tang-2022.md) (§2.2, Eqs. 15–16) compare two
closures of the subgrid variance of the mixture fraction $Z$ (page-local),
$\widetilde{Z''^2}$, one of the three look-up coordinates of the table (see
[flamelet-tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)).
The algebraic one is a scale-similarity estimate with a test filter of
twice the grid-filter width,

$$\widetilde{Z''^2}=c_Z\big(\widehat{\tilde Z^2}-\hat{\tilde Z}^2\big),\qquad \hat\Delta=2\Delta,$$

($c_Z$ page-local, value not printed) evaluated by a seven-point discrete
formula (Eq. 16), whose printed form contains no coefficient, which
amounts to $c_Z=1$ *(compiler check, not in the sources)*. The other is a transport equation for $\widetilde{Z''^2}$
with modelled scalar dissipation (turbulent Schmidt number 0.5 and a
dissipation constant of 40, Eq. 17). The
authors describe the similarity estimate as having "no historical
effects": it carries no transport or dissipation of the variance. In the
DLR strut-injector scramjet it gives variances locally up to about 0.01
but concentrated below 0.001, against a lower-peaked, wider distribution
below 0.002 from the transport equation; it raises the heat release
near the injector and shortens the flame lift-off, and the transport
equation agrees better with the measured temperature at $x=125$ mm
(§3.1, Figs. 5–7). In a cavity-stabilized combustor with transverse
injection the similarity variance is higher over almost the whole jet
wake, which the authors link to over-intense combustion and an upstream
boundary-layer separation; the transport equation matches the wall
pressure better (§3.2, Figs. 12–16). They recommend the transport
equation "if computing resources allow" (§4).

## Mixed explicit–implicit model

[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§6.5)
test a different mixture: Smagorinsky ($C_s=0.1$, 0.18) added to an
implicit [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
The Smagorinsky part restores the low-wavenumber plateau of the spectral
eddy viscosity and removes the
[bottleneck](/definitions/bottleneck-effect.md), but the total dissipation
does not improve.

## Qualifications

- Valencia et al. (2026) print the sixth-order D3M centre coefficient
  with $-2352(\Delta/h)^2$ (Table II); the stencil weights then do not
  sum to one, while $+2352(\Delta/h)^2$ makes them sum to one and matches
  $-\tfrac{1}{24}(\Delta/h)^2$ times the sixth-order central second
  difference *(compiler check, not in the sources)*. The selected order is
  4, so their results are unaffected. Their text says the relative error
  falls "by nearly half" from FGR 2 to FGR 4, whereas Tables VI–VII give
  reductions by factors of 2.4–4.1 for the four deconvolution models
  (ADM $E_{xx}$ 0.2469 to 0.0909) *(compiler check, not in the sources)*; and DSM's
  $E_{xx}$ worsens, 1.2955 to 1.9644, where the text speaks of "marginal
  improvement" of the classical models. The DSM and DMM formulas,
  constants and test filter are not printed.

- Najafiyazdi et al. (2023) compare their S64 finite-element LES
  ($64^3$ elements, 274 625 nodes, Table 2) with flux-reconstruction runs
  printed as "128 degrees of freedom, i.e. p1 Legendre polynomials on a
  $64^3$ grid" (§6.2); their "relaxation factor" 0.8 is not placed in an
  equation.

- Zhou & Bae (2024) print the similarity term with unit coefficient and
  do not print the width of the Gaussian secondary filter; their eddy
  viscosity of Fig. 5 is the Smagorinsky part only.
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
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II, Eqs. (9)–(10); §IV F, Figs. 30–33; §V.
- [Kim et al. (2022)](/sources/kim-2022.md) — §I; §II; §II D.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §II B, Eqs. (9)–(11); §V A 2–3, Figs. 6–10, Table I; §V B 2, Figs. 16–21.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1; §6.2.3.
- [Kang et al. (2023)](/sources/kang-2023.md) — §3.3, Eqs. (3.4)–(3.8), Tables 4, 6, 9, Figs. 19–22, 24; §3.7; App. C.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §I; §IV B, Eqs. (19)–(21), Fig. 13.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §1, Eqs. (1.3)–(1.4); §2.3–2.4, Eqs. (2.36)–(2.47); §3.1.
- [Kim et al. (2024)](/sources/kim-2024.md) — §1.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §II.A; §III, Figs. 3–8; §IV.
- [Caban et al. (2026)](/sources/caban-2026.md) — §2, Eqs. (8)–(12); §4.1–4.2, Eqs. (36)–(39), Figs. 6–8; §5.4.1–5.4.2, Tables 4–9; §6.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — p. 5.
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.2, Eqs. (15)–(17); §3.1, Figs. 5–7; §3.2, Figs. 12–16; §4.
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §I; §II C, Eqs. (23)–(29); §III A–D, Eqs. (30)–(50), Tables I–II; §V A–C, Tables III–VII, Figs. 20–23; §VI.
- [Li et al. (2021)](/sources/li-2021.md) — §III C, Figs. 2–8; §III F, Fig. 13.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §1; §3.2.
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — §III B, Eqs. (27)–(31), Algorithm 1; App., Eqs. (A1)–(A24); §IV A, Figs. 1–3; §IV B, Figs. 5–23, Table III.
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §I; §II, Eqs. (18)–(23); §III B, Eqs. (25)–(32), Algorithm 1; §IV A, Figs. 1–2; §IV B, Figs. 3–18, Table VI; §V.
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §II B; §IV, Fig. 2; §V, Figs. 9, 16, Table V; App. B, Figs. 18–20.
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §I.
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) — §2, Eqs. (3)–(6), Algorithm 1; §6.1, Fig. 6; §6.2, Figs. 10–13.
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.1, Eq. (1); §3.1, Figs. 4–5, 7–11; §3.3, Fig. 17.
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §2.2; §3.1.
