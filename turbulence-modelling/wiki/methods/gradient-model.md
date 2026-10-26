---
type: Method
title: "Gradient (Clark) model and the clipping of structural SGS models"
description: "Clark's gradient model approximates the subgrid stress by a truncated Taylor expansion of the filter; it correlates well with the exact stress but under-dissipates and backscatters, so it is clipped or mixed. Optimal clipping is the Frobenius-nearest backscatter-free stress, a parameter-free mixed model."
status: established
aliases: [Clark model, gradient model, nonlinear gradient model, tensor-diffusivity model, optimal clipping, standard clipping, GM-OC, GM-SC]
tags: [les, sgs-model, filtering, eddy-viscosity]
timestamp: 2026-10-26T07:41:00Z
---

# Gradient (Clark) model and the clipping of structural SGS models

The **gradient model**, attributed by the sources to Clark et al. (1979),
is a structural subgrid-scale model: it estimates the
[subgrid stress](/definitions/large-eddy-simulation.md)
$\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ from the leading term of a
Taylor expansion of the filter, without assuming alignment with the
resolved strain. Like the [scale-similarity model](/methods/scale-similarity-model.md)
it reproduces the structure of the exact stress well a priori, but it
under-predicts the mean subgrid dissipation and produces local
[backscatter](/definitions/energy-backscatter.md), which can destabilize an
LES. It is therefore used clipped, or mixed with a
[Smagorinsky](/methods/smagorinsky-model.md) term. **Optimal clipping**
([Prakash et al. 2022](/sources/prakash-2022.md)) is the closest
backscatter-free tensor to the model stress and turns out to be a mixed
model whose eddy viscosity is switched on only where the structural model
backscatters.

## The model

For an isotropic box filter of width $\Delta$, Prakash et al. (2022, §III,
Eq. 16) write

$$\tau^{\mathrm G}_{ij}=\frac{\Delta^2}{12}\,\partial_k\bar u_i\,\partial_k\bar u_j ,$$

with $\Delta=(\Delta_1\Delta_2\Delta_3)^{1/3}$ as for the Smagorinsky model
($\Delta_i$ the filter width along $x_i$, page-local). For a
coordinate-aligned anisotropic box filter they write (Eqs. 17–18)
$\tau^{\mathrm G}_{ij}=\tfrac1{12}G_{ik}A_{kl}G_{jm}A_{ml}$ with
$G_{ij}=\partial_j\bar u_i$ and $A=\mathrm{diag}(\Delta_1,\Delta_2,\Delta_3)$,
which is

$$\tau^{\mathrm G}_{ij}=\frac1{12}\sum_k\Delta_k^2\,\partial_k\bar u_i\,\partial_k\bar u_j$$

*(compiler check, not in the sources)*. In their a posteriori LES the filter
width is the computational grid size. The model stress has a positive
trace and is the full tensor, not its deviatoric part. Its local flux
$\Pi^{\mathrm G}=-\tau^{\mathrm G}_{ij}\bar S_{ij}$ (superscript G
page-local) can take either sign.

Prakash et al. (2022, §I–II), citing earlier a priori studies, summarize
the class of structural models (gradient, Bardina similarity, approximate
deconvolution): high correlation of the model stress and of the model flux
with the exact ones, under-predicted local dissipation, and hence an energy
pile-up at the highest resolved wavenumbers even in isotropic turbulence.
Eddy-viscosity models make the opposite trade: they assume local alignment
of $\tau^d_{ij}$ with $\bar S_{ij}$, which a priori studies do not support,
and correlate poorly with the exact stress. [Agrawal et al. (2022)](/sources/agrawal-2022.md)
(§I, §VII.A) list the Clark model with Bardina's and Stolz–Adams
deconvolution among the non-Boussinesq models that need an added
Smagorinsky term.

## Stability and backscatter

With periodic or homogeneous boundaries and no forcing, the resolved energy
obeys (Prakash et al. 2022, §II, Eqs. 4–6, citing earlier work)

$$\frac{d}{dt}\int_\Omega\tfrac12\bar u_i\bar u_i\,d\Omega=-\int_\Omega\big(2\nu\bar S_{ij}-\tau_{ij}\big)\bar S_{ij}\,d\Omega ,$$

so the resolved energy decays if and only if
$\int_\Omega\tau_{ij}\bar S_{ij}\,d\Omega\le\int_\Omega2\nu\bar S_{ij}\bar S_{ij}\,d\Omega$.
Too much model backscatter can make the resolved energy grow. A pointwise
condition $\tau_{ij}\bar S_{ij}\le2\nu\bar S_{ij}\bar S_{ij}$ is sufficient;
the clipping procedures enforce the stronger pointwise condition of no
model backscatter, $\tau^{\mathrm M}_{ij}\bar S_{ij}\le0$, i.e.
$\Pi^{\mathrm M}\ge0$ ($\tau^{\mathrm M}$ any base model stress,
page-local). The authors say the pointwise condition is sufficient, not
necessary.

## Three ways to stabilize a structural model

**Mixed model.** Clark et al. are recalled as having first stabilized the
gradient model by adding an eddy viscosity (Prakash et al. 2022, §II,
Eq. 7):

$$\tau^{\mathrm{mix}}_{ij}=\tau^{\mathrm G}_{ij}-2\nu_t\bar S_{ij},\qquad \nu_t=(C_G\Delta)^2\lvert\bar S\rvert ,$$

with $C_G$ (page-local) a constant or, in the **dynamic mixed model** (DMM),
a coefficient from the [dynamic procedure](/methods/dynamic-procedure.md).
A fixed $C_G$ needs tuning: too large is over-dissipative and inaccurate in
laminar–turbulent transition, too small unstable (citing Vreman, Geurts &
Kuerten). The authors add that the claim that an added Smagorinsky term
barely affects structural accuracy "is not guaranteed mathematically", and
that the homogeneous averaging of the DMM can itself lower it.

**Standard clipping** (attributed to Liu, Meneveau & Katz; Eq. 9) sets the
model stress to zero wherever it backscatters:

$$\tau^{\mathrm{SC}}_{ij}=\begin{cases}0,&\Pi^{\mathrm M}<0,\\ \tau^{\mathrm M}_{ij},&\Pi^{\mathrm M}\ge0.\end{cases}$$

It raises the model dissipation at the cost of the correlation with the
exact stress. Dynamic regularization (Vollant et al., as recalled), which
removes the backscattering terms of a decomposition of the gradient model,
is said to share this drawback (§I).

**Optimal clipping** (Prakash et al. 2022, §II, Eqs. 10–15) replaces
$\tau^{\mathrm M}$ by its Frobenius-nearest symmetric tensor in the
admissible set $\mathcal A=\{\boldsymbol\tau\in\mathrm{Sym}(3):\tau_{ij}\bar S_{ij}\le0\}$
(page-local):

$$\tau^{\mathrm{OC}}_{ij}=\arg\min_{\boldsymbol\tau\in\mathcal A}\tfrac12\sum_{i,j}\big(\tau_{ij}-\tau^{\mathrm M}_{ij}\big)^2 .$$

If $\tau^{\mathrm M}\in\mathcal A$ the minimizer is $\tau^{\mathrm M}$.
Otherwise the constraint is active and the six independent components and a
Lagrange multiplier $\lambda_{\mathrm{oc}}$ (page-local; the paper's
$\lambda$) solve a linear $7\times7$ KKT system (Eq. 12) whose solution is

$$\tau^{\mathrm{OC}}_{ij}=\tau^{\mathrm M}_{ij}-\lambda_{\mathrm{oc}}\bar S_{ij},\qquad
\lambda_{\mathrm{oc}}=\max\!\Big(\frac{\tau^{\mathrm M}_{kl}\bar S_{kl}}{\bar S_{mn}\bar S_{mn}},\,0\Big),$$

the paper's Eqs. (13)–(15), with Eq. (15) written as
$-\min\{-\tau^{\mathrm M}_{ij}\bar S_{ij}/(\bar S_{ij}\bar S_{ij}),0\}$. The
authors state uniqueness without a detailed proof. Their reading
(after Eq. 15): $\tau^{\mathrm{OC}}$ *is* a mixed model, the structural
stress plus an eddy-viscosity term with

$$\nu_t=\frac{\lambda_{\mathrm{oc}}}2=\frac{\max(-\Pi^{\mathrm M},0)}{\lvert\bar S\rvert^2}$$

(registry form: *compiler check, not in the sources*), which is exactly the
viscosity needed to remove the model backscatter and vanishes where there
is none. They offer this as "some mathematical justification for the use of
mixed SGS models". The model is parameter-free, computed pointwise with no
test filter and no homogeneous averaging (claimed to cut the evaluation cost
against a DMM, without timings), and, like other mixed formulations, is
said to keep the near-wall scaling of the base model. It applies unchanged
to Bardina's model, to approximate deconvolution or to a data-driven
$\tau^{\mathrm M}$; the authors report tests with Bardina's model and with
their own data-driven model with similar trends, results not shown (§II,
§IV). The paper does not treat the case $\bar S_{ij}=0$, where Eqs. (13)
and (15) are undefined.

Where the base model backscatters ($\Pi^{\mathrm M}<0$), Eqs. (13)–(14)
give $\tau^{\mathrm{OC}}_{ij}\bar S_{ij}=0$, the zero flux that standard
clipping also gives there, and elsewhere both return $\tau^{\mathrm M}$:
pointwise
$\Pi^{\mathrm{OC}}=\Pi^{\mathrm{SC}}$ *(compiler check, not in the
sources)*. This explains the a priori result below that the two procedures
have the same mean dissipation, and it places all their difference in the
stress structure.

## A priori results

On box-filtered DNS of forced isotropic turbulence from the Johns Hopkins
database at $Re_\lambda=418$ (Prakash et al. 2022, §III.A, Tables 1–2,
Figs. 1–3), measured by a summed stress correlation coefficient C.C.
(Eq. 19) and the relative error of the mean energy flux
$\mathrm{R.E.F.}=(\langle\Pi^{\mathrm M}\rangle-\langle\Pi\rangle)/\langle\Pi\rangle$
(Eq. 20; both page-local):

- **isotropic filter**, $\Delta\approx6.5\eta$–$68\eta$: the unclipped
  gradient model is highly correlated at all widths but has negative R.E.F.
  (too little dissipation); standard clipping improves R.E.F. and lowers
  C.C.; optimal clipping keeps the unclipped C.C. with an SGS dissipation
  "identical to that of the standard clipped gradient model";
- **book-type filter** ($\Delta_1=15\eta$, $\Delta_2=\Delta_3$ up to
  $292\eta$): C.C. first falls with aspect ratio, then levels off; standard
  clipping loses more correlation than under isotropic filtering, optimal
  clipping keeps it; anisotropy lowers R.E.F. for all models, which the
  authors partly attribute to more model backscatter;
- **pencil-type filter** ($\Delta_1=\Delta_2=15\eta$, $\Delta_3$ up to
  $292\eta$): standard-clipping C.C. "deteriorates significantly", optimal
  clipping stays close to the unclipped model, and clipping "dramatically
  improves" the model dissipation, which without clipping drops strongly at
  high aspect ratio.

## A posteriori results

Prakash et al. (2022, §III.B) run the stabilized finite-element code PHASTA
(SUPG/PSPG/grad-div, trilinear elements, generalized-$\alpha$) with no
model (NM), dynamic Smagorinsky (DS), and the gradient model unclipped
(GM-NC), with standard clipping (GM-SC), optimal clipping (GM-OC) and as a
dynamic mixed model (GM-DMM, test-filter ratio $\sqrt3$).

- **Forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)**,
  $\nu=10^{-12}$, $32^3$–$128^3$ elements (§III.B.1, Fig. 4): NM and GM-NC
  pile energy up at the highest resolved wavenumbers; DS has no pile-up but
  over-predicts intermediate wavenumbers, as does GM-DMM; both clipped
  models give much better spectra, optimal clipping "a slightly longer
  inertial subrange and less energy pileup".
- **[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)** at
  $Re=1600$, $64^3$ and $128^3$ (§III.B.2, Figs. 5–7): all models match the
  filtered-DNS resolved energy on $128^3$, and all but GM-DMM on $64^3$
  (GM-DMM decays too fast). DS under-predicts the resolved dissipation,
  GM-DMM more so (significantly even on $128^3$), GM-NC over-predicts it;
  GM-SC and GM-OC are the most accurate, OC slightly better than SC in the
  coarse-mesh spectra.
- **[Channel flow](/benchmarks/turbulent-channel-flow.md)** at
  $Re_\tau=590$, wall-resolved, coarse $48\times111\times48$ and medium
  $64\times133\times64$ elements (§III.B.3, Tables 3–4, Figs. 8–10). Skin
  friction against DNS $C_f=0.0058$ (bulk-velocity based):

| Model | $C_f$ coarse | $C_f$ medium |
|---|---|---|
| DS | 0.0047 | 0.0049 |
| GM-NC | 0.0063 | 0.0063 |
| GM-SC | 0.0047 | 0.0050 |
| GM-DMM | 0.0053 | 0.0055 |
| GM-OC | 0.0051 | 0.0053 |

  DS and GM-SC under-predict near-wall velocity and over-predict it in the
  log region; GM-NC over-predicts the turbulent kinetic energy peak; GM-OC
  and GM-DMM give much better Reynolds shear stress, GM-DMM slightly better
  than GM-OC at the price of explicit filtering and homogeneous averaging at
  every step.

The authors attribute the channel-flow gain of optimal over standard
clipping to structural accuracy, since the a priori dissipation of the two
is identical; they mark this as a hypothesis ("we believe", "We
hypothesize", §III.B.3, §IV). They conclude that in HIT and the TGV the
improvement of optimal over standard clipping "was not significant", that
for wall-resolved LES of wall-bounded flow it "may yield significantly
improved results", and that where clipping is needed for stability optimal
clipping "should be selected over standard clipping" (§IV).

## Related construction: the stabilized mixed model

[Abe (2021)](/sources/abe-2021.md) (§II C, Eqs. 12–16) uses a
**stabilized mixed model** (SMM), the author's own earlier model: a
one-equation eddy viscosity plus an "extra anisotropic term" built from a
similarity stress $\tau'_{ij}=(\bar u_i-\hat{\bar u}_i)(\bar u_j-\hat{\bar u}_j)$
(page-local; see
[scale-similarity models](/methods/scale-similarity-model.md)) from which
its linear eddy-viscosity projection is removed,

$$\tau'_{ij}-(-2\nu'\bar S_{ij}),\qquad \nu'=-\frac{\tau'^{\,d}_{kl}\bar S_{kl}}{2\bar S_{mn}\bar S_{mn}} ,$$

normalized by its trace, minus $\tfrac13\delta_{ij}$ ($\nu'$ page-local).
Because $\bar S_{kk}=0$, $-2\nu'\bar S_{ij}=\lambda_{\mathrm{oc}}\bar S_{ij}$
with $\tau^{\mathrm M}=\tau'$ and the $\max(\cdot,0)$ of Eq. (15) left out
(Eq. 13): the SMM removes from the similarity stress the same projection
that optimal clipping removes where the structural model backscatters, but
everywhere. What remains is orthogonal to $\bar S_{ij}$, so the extra term
carries no energy flux *(compiler check, not in the sources)*. Abe states
from earlier work that the term "yields no undesirable extra energy
transfer between the GS and SGS components" and that a pure similarity
model "often causes numerical instability" (§II C, §V). The two sources do
not cite each other.

## Gradient term as an energy-transfer-free anisotropic stress

[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (§IV B, Eq. 20)
use the gradient term, with directional widths $\Delta_\alpha$ (page-local),
$\tau^{\mathrm a}_{ij}=\sum_\alpha\Delta_\alpha^2\partial_\alpha\bar u_i\partial_\alpha\bar u_j$
(page-local), as the shape of the anisotropic remainder of the subgrid
stress, the part that carries no energy transfer (see
[energy backscatter](/definitions/energy-backscatter.md)). Following Abe's
strategy (as recalled), they remove its eddy-viscosity projection with
$\nu^{\mathrm a}=-\tau^{\mathrm a}_{ij}\bar S_{ij}/(2\bar S_{kl}\bar S_{kl})$
(page-local) and scale it by the exact subgrid energy:

$$\tau^{\mathrm{ani}}_{ij}=\tau_{\ell\ell}\,\frac{\tau^{\mathrm a\,d}_{ij}+2\nu^{\mathrm a}\bar S_{ij}}{\tau^{\mathrm a}_{mm}},$$

the construction of the stabilized mixed model above with the gradient
term in place of the similarity stress. The text recalls the Taylor
relation with the factor $\tfrac1{12}$; Eq. (20) omits it, which the
normalization by $\tau^{\mathrm a}_{mm}$ makes immaterial *(compiler
check, not in the sources)*. A priori, on
channel DNS at $Re_\tau=400$ filtered at $(\Delta x^+,\Delta z^+)=(105,52.4)$
(§IV B, Fig. 13), the gradient version gives a streamwise anisotropic
redistribution whose profile differs from the filtered DNS, and the right
(productive) sign of the spanwise component, though with small intensity;
the similarity version is closer to the filtered DNS overall (see
[scale-similarity models](/methods/scale-similarity-model.md)).

## Gradient term in learned and two-parameter models

[Kang et al. (2023)](/sources/kang-2023.md) use the gradient term
$\tau^{\mathrm G}_{ij}=\tfrac1{12}\Delta^2\partial_k\bar u_i\partial_k\bar u_j$
(page-local), with one isotropic $\Delta$, in
three roles (§3.2–3.3, App. C, Figs. 10, 19, 21):

- **Normalization of a learned stress.** Among the volume-averaged norms of
  the gradient term, of the modified Leonard term and of the resolved
  stress $L_{ij}$, the gradient term keeps the most constant ratio to the
  norm of the filtered-DNS stress over $Re_\lambda$ and over filter widths
  half and twice the training one; it scales the output of their
  [neural-network SGS model](/methods/neural-network-sgs-model.md) in
  isotropic turbulence. In channel flow they use $L_{ij}$ instead, because
  the gradient term "is known to have an incorrect near-wall scaling" (Liu
  et al., as recalled).
- **Learned-model input.** Added to $\bar S_{ij}$ as an input, it predicts
  the decay of the kinetic energy best, but gives the largest spectral
  errors at the lowest wavenumbers on $48^3$ and $24^3$ grids, which the
  authors attribute to the Taylor-series truncation error growing on
  coarse grids.
- **Dynamic two-parameter mixed model** (DTM$_{\mathrm{nl}}$, Smagorinsky
  plus Clark term, coefficients from the
  [dynamic procedure](/methods/dynamic-procedure.md)): the best a priori
  stress correlation of the paper (0.91 in isotropic turbulence), stable
  only with averaging and clipping, 1.68 times the DSM cost of evaluating
  the stress; a posteriori in forced isotropic turbulence its energy
  spectrum is nearly identical to that of the learned mixed model.

The eddy viscosity of the
[anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
is proportional to the positive part of the gradient-model flux with
directional widths (*compiler check, not in the sources*; see that page).

## Qualifications

- Prakash et al. (2022) define C.C. (Eq. 19) as a plain double sum of
  per-component correlation coefficients, yet state that a perfect model has
  C.C. = 1; with nine terms the printed sum would give 9 for a perfect model
  *(compiler check, not in the sources)*, so a normalization is missing from
  the printed formula; the text calls C.C. the "mean correlation
  coefficient".
- In §III.B.3 the paper says the unclipped gradient model over-predicts the
  Reynolds shear stress and, two sentences later, that "the dynamic
  Smagorinsky model and the gradient model without clipping significantly
  underpredict" it; the parallel statements on $C_f$ and velocity, and the
  conclusion in §IV, group DS with standard clipping. The paper also calls
  the medium channel mesh "fine" once, and Table 4 labels the variants
  AGM-NC, AGM-SC, AGM-DMM, AGM-OC without defining "AGM".
- Eq. (7) prints the eddy-viscosity term with the unfiltered $S_{ij}$, Eq. (8)
  prints the no-backscatter condition with the exact stress $\tau_{ij}$
  where the text means the model stress, and Eq. (17) prints $G_{ij}$ with
  the unfiltered velocity.
- The flow-through time of the channel runs is printed as
  $T=\bar u_b/L_x$, the inverse of a time.
- The evidence for optimal clipping is one paper with one base model shown,
  three canonical flows and one code; the authors' claim about other base
  models rests on results not shown.

# Citations

- [Prakash et al. (2022)](/sources/prakash-2022.md) — §I–II, Eqs. (1)–(15); §III, Eqs. (16)–(20); §III.A, Tables 1–2, Figs. 1–3; §III.B.1–3, Tables 3–4, Figs. 4–10; §IV.
- [Abe (2021)](/sources/abe-2021.md) — §II C, Eqs. (12)–(16); §V.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §I; §VII.A.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §IV B, Eqs. (19)–(20), Fig. 13.
- [Kang et al. (2023)](/sources/kang-2023.md) — §3.2, Fig. 10; §3.3, Eq. (3.8), Table 6, Figs. 19, 21, 24; §3.5; App. C.
