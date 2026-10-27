---
type: Method
title: "Field inversion and machine learning"
description: "Field inversion infers a spatial correction field of a RANS model from data by solving a PDE-constrained inverse problem; FIML learns that field from local flow features and embeds it in the solver. Sources compare which term to correct, show non-unique and over-fitted inversions, gate corrections out of attached layers, and invert on high-order DG."
status: established
aliases: [FIML, field inversion, field-inversion and machine-learning, inference before learning, variational data assimilation, non-parametric correction, Reynolds-force vector]
tags: [field-inversion, data-driven, rans, uncertainty-quantification, separated-flow]
timestamp: 2026-10-26T20:51:00Z
---

# Field inversion and machine learning

**Field inversion** (FI) treats a correction of a RANS closure as an unknown
field, $\beta(\boldsymbol x)$, and infers it from data by solving an inverse
problem constrained by the model equations. In the representative example
of Duraisamy et al. (2019, §5.1), $\beta$ multiplies the production term of
the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md). The inferred
field belongs to one geometry and one flow condition. **Field inversion and
machine learning** (FIML) generalizes it in three steps. Field inversion is
run on several datasets. A regression model
$\beta\approx f(\boldsymbol\zeta;\boldsymbol\theta)$ is then trained on the
inferred fields as a function of local flow features $\boldsymbol\zeta$.
Finally, the learned map is embedded in the RANS solver as a correction
(Duraisamy et al. 2019, §5.4; Duraisamy 2021, §IV.B, Eqs. 7–8). The
sources present FIML as a remedy for the inconsistency between
learning from DNS and predicting in RANS (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Place in the modelling framework

Duraisamy et al. (2019, §2) sort RANS modelling assumptions into four
layers:

- **L1**, the information lost by averaging, which they call
  "fundamentally irrecoverable";
- **L2**, the representation of $R_{ij}$ in terms of the averaged
  variables (e.g. the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md));
- **L3**, the functional form of the model operators;
- **L4**, the coefficient values.

Calibrating coefficients, by Bayesian inference or otherwise, addresses L4
only (§5.1). A spatially varying field is needed because the discrepancy
enters through the divergence of the Reynolds stress and is "likely
spatially varying" (§4.1). Field inversion instead lets the data inform the
L3 operators. The authors read the inferred multiplier as data acting on the
functional form (§5.1). See
[model-form uncertainty](/definitions/model-form-uncertainty.md) for the
layers and for the realizability-constrained perturbation alternatives.

## Step 1: field inversion

Let $\boldsymbol Y$ denote the available data (page-local: observables
such as $C_p$, $C_f$, sparse velocities, or a lift coefficient), and
$\boldsymbol Y_{\mathrm m}(\beta)$ the same observables computed by the
augmented model. Duraisamy (2021, Eq. 7) writes FI for dataset $i$ as

$$\min_{\beta^{(i)}}\ \mathcal L\big[\boldsymbol Y^{(i)},\boldsymbol Y^{(i)}_{\mathrm m}(\beta^{(i)})\big]\quad\text{subject to the augmented RANS equations,}$$

which yields a problem-specific field $\beta^{(i)}(\boldsymbol x,t)$. Two
properties follow from this form. FI is consistent with the model, and it
does not require full-field DNS (§IV.B). Duraisamy et al. (2019, box p. 7)
give the Bayesian reading. With Gaussian prior and likelihood, the maximum
a posteriori (MAP) estimate minimizes a data misfit weighted by the
observation covariance plus a prior misfit weighted by the prior covariance.
Using only the posterior mode makes the estimate deterministic (§3.2).
[Yan et al. (2022)](/sources/yan-2022.md) (§2.1, Eq. 6) write the same MAP
problem explicitly. With Gaussian, pointwise-independent data and
correction values and a prior mean $\beta=1$ (the baseline model), FI
minimizes

$$\mathcal L=\sum_i\sigma_{\mathrm{obs}}^{-2}\big(Y_i-Y_{\mathrm m,i}(\beta)\big)^2+\sum_j\sigma_\beta^{-2}(\beta_j-1)^2,$$

where $\beta_j$ is the value of $\beta$ at grid point $j$ and
$\sigma_{\mathrm{obs}}$, $\sigma_\beta$ (page-local) are the observation and
prior standard deviations (the paper calls them variances, but they enter
as $\sigma^{-2}$). The second term is a regularization; relative to the
data misfit its weight is $\sigma_{\mathrm{obs}}^2/\sigma_\beta^2$ *(compiler
check, not in the sources)*.

**Solvers.** Duraisamy et al. (2019, §5.1) list adjoint-based optimization
and derivative-free iterative ensemble Kalman methods. Yan et al. (2022,
§2.2, Eqs. 7–11) use the discrete adjoint of the ADflow solver, built with
the Tapenade automatic-differentiation tool, with one adjoint solve giving
the gradient with respect to every $\beta_j$. An augmented discrete adjoint
holds a constraint fixed during the inversion: the lift coefficient on the
airfoils, the bulk velocity on the hills, where the driving volume force
is adjusted automatically. Yan et al. (2022, §1) list Markov-chain Monte
Carlo and the ensemble Kalman filter for the full posterior, and call the
MAP estimate "field inversion or data assimilation". The ensemble route is
described on
[ensemble Kalman calibration of closures](/methods/ensemble-kalman-closure-calibration.md),
where [Wang et al. (2023c)](/sources/wang-2023-c.md) use it in LES to
calibrate one constant of a subgrid model against filtered-DNS energy
spectra; in their §V they place adjoint-based variational methods, nudging
and the ensemble Kalman filter side by side as a posteriori alternatives
to a priori learning.

**What is inverted.** Duraisamy et al. (2019, §5.1) recall three kinds of
inversion:

- an eddy-viscosity field from full-field DNS velocity (Dow & Wang);
- multipliers of transport-equation terms from limited surface data, for
  channel flow, shock/boundary-layer interaction, curvature and separation
  (Duraisamy et al.; Singh & Duraisamy);
- Reynolds-stress magnitude and anisotropy from sparse velocity data
  (Xiao et al.; Wu et al.).

Duraisamy (2021, §IV.B) adds the mean-flow momentum equation as a target.
Yan et al. (2022) invert the production multiplier of Spalart–Allmaras
from deliberately scarce data: the experimental lift coefficient alone
(S809 airfoil), DNS mean-velocity profiles at a few stations (parametrized
hills), and lift alone or lift and drag (iced airfoil).

**Representative example.** As recalled by Duraisamy et al. (2019, §5.1,
Figs. 4–5, from Singh & Duraisamy 2016), $\beta$ multiplies the production
term of Spalart–Allmaras in a channel with a convex wall. It is inferred
only from LES $C_f$ on the lower convex wall. The inverted model reproduces
the LES velocity and Reynolds stresses well and improves considerably on
both SA and its rotation–curvature variant SARC. The review states that the
trend of the inferred field is consistent with convex curvature reducing
turbulence, and that the comparison suggests SARC needs improvement in the
log layer. The review gives no Reynolds number for this case.

## Step 2: learning the inferred fields

Inferred fields are tied to one geometry and flow condition. Duraisamy et
al. (2019, §5.2) name the remedy: map the discrepancy from physical space
to a feature space. They credit Tracey et al. (2013) with this step.
Duraisamy (2021, §I) calls it the key advance over the earlier
uncertainty-quantification work.

FIML collects the fields of $k$ datasets,
$\{\beta^{(1)},\dots,\beta^{(k)}\}$, with their model-computed features
$\{\boldsymbol\zeta^{(1)}_{\mathrm m},\dots,\boldsymbol\zeta^{(k)}_{\mathrm m}\}$
(page-local: subscript $\mathrm m$ marks a quantity computed from the
model's own solution). It then solves the supervised problem

$$\min_{\boldsymbol\theta}\ \mathcal L\big[\{\beta^{(i)}\},\,f(\{\boldsymbol\zeta^{(i)}_{\mathrm m}\};\boldsymbol\theta)\big]$$

(Duraisamy 2021, Eq. 8). Duraisamy writes $k$ for the number of datasets;
it is not the turbulent kinetic energy. The difference from a
priori learning is that both targets and features come from model
solutions, not from coarse-grained DNS. Duraisamy (2021, §V) gives the
feature guidelines: local non-dimensionalization, rotational, reflectional
and frame invariance of the features and of the normalizing variables, and
a preference for local features. Wall distance, wall-stress measures and
pressure-gradient features have proved important as non-local surrogates.

## Step 3: prediction

The learned $f$ is embedded in the solver, so the RANS equations are solved
with $\beta=f(\boldsymbol\zeta_{\mathrm m};\boldsymbol\theta)$ evaluated
from the running solution. As recalled by Duraisamy et al. (2019, §5.4,
Fig. 8, from Singh et al. 2017), a data-driven Spalart–Allmaras model for
airfoils with separation improves the surface pressure markedly over the
baseline, even when the data are "very limited experimental measurements,
such as the lift coefficient". As recalled by Duraisamy (2021, §VII),
FIML-augmented models improve predictions on cases close to their training
set, e.g. an airfoil of slightly different shape. Duraisamy (2021, §IV.B)
states that FIML has been used in transition modelling as well as
turbulence modelling.

## Application to separated flows (Yan et al. 2022)

Yan et al. (2022) apply the three steps to the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) in 2D steady
RANS of three separated flows, with $\beta(\boldsymbol x)$ multiplying only
the production term $c_{b1}\tilde S\tilde\nu$ ($\beta=1$ recovers the
baseline; §2.1, Eq. 5), the same form as the representative example above.

**Physical motivation.** As recalled there (§1), models are calibrated in
equilibrium shear flows where $P_k/\varepsilon$ is about 1.4 to 1.8, while
in separating shear layers, corner separation and compressor boundary
layers production can greatly exceed dissipation. Ad hoc fixes generalize
poorly: as recalled by the authors, Rumsey's separation fix of SST improves
the periodic hill but worsens backward-step flows, and LES of Fang et al.
shows production both increased and decreased in such regions, where the
authors' own earlier separating-shear-layer fix only increased it. The
authors read $\beta$ as "closely related to the equilibrium state of the
turbulence".

**Non-uniqueness and physics-shaped priors.** Many correction fields
reduce the observed error enough (§3.1.1, Figs. 4–5). Without
regularization, inversion on the hills gives an irregular field with no
general tendency, which "might be not physical" (§3.2.1, Fig. 18). The
authors shape the prior from the nonequilibrium mechanism: a nonuniform
$\sigma_\beta$ (on S809, 200 for $x<1.0$ and 20 for $x>1.0$, Eq. 15, with
$x$ not defined in the paper; motivated by the strong adverse pressure
gradient near the boundary layer) or corrections
confined to a box over the separating shear layer (hills, Case 2). A
uniform prior with the same weight (Case 3) gives a correction similar to
the box-limited one, which the authors take as evidence that FI captures
the [model-form uncertainty](/definitions/model-form-uncertainty.md) in the
critical region "with less human intervention" (§3.2.1, Table 2).

**Where the corrections sit.** On the hills and the iced airfoil the
inferred $\beta$ is below one at the start of the separating shear layer
and above one downstream, so turbulent mixing is both reduced and enhanced
(§3.2.1, §3.3.1, Figs. 18, 26). The enhanced region coincides, by visual
comparison, with the region where the authors' earlier
$k$-$\overline{v^2}$-$\omega$ separation fix activates (where
$P_k/\varepsilon\gg1$) and with Rumsey's fix region (Figs. 11, 18, 27). On
S809 at $8^\circ$ and $14^\circ$ the inversion from lift alone suppresses
production mainly in the strong adverse-pressure-gradient region and
enlarges the separation (Fig. 6).

**Unobserved quantities improve.** On S809 the pressure distribution
improves though only lift was observed (Fig. 7). On the hills the
lower-wall $C_f$ improves though only velocity was observed (Fig. 16). On
the iced airfoil (GLC305 with horn-ice shape 944, $M=0.12$,
$Re_c=3.5\times10^6$) baseline SA gives $C_L=0.393$ and 0.495 at $4^\circ$
and $6^\circ$ against 0.489 and 0.669 measured; inversion on lift and drag
(FI1) matches both to the printed digits, inversion on lift alone (FI2)
gives $C_D=0.0648$ and 0.0950 against 0.0566 and 0.1024, and FI1 gives the
better pressure plateau. The authors conclude that more observations make
the assimilation more credible (§3.3.1, Table 3, Fig. 28). At $6^\circ$ the
corrected separation bubble covers about half the chord instead of the
whole airfoil (Fig. 25).

**Learning step.** A fully connected network (three hidden layers, sigmoid
activations, batch normalization, z-score inputs, Adam, mean-squared loss)
maps eight local features to $\beta$: $\chi$, the SA production and its
ratio to destruction, the strain-rate magnitude and its ratio to the
vorticity magnitude, a Reynolds-stress magnitude, a modified DES shielding
function $1-\tanh(r_d^{0.5})$ and $\lvert\nabla\tilde\nu\rvert$ (§2.3; the
norm conventions and $r_d$ are not defined in the paper). Networks are
preferred to Gaussian processes and random forests because their
evaluation cost does not grow with the training set, which matters for a
model called at every grid point and iteration (§2.3). Network size and
epochs are chosen by the a posteriori error of the embedded model, not by
the validation loss, because the two are not monotonically related
(§3.1.2, Table 1; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

**Prediction results.**

| Case | Training data | Network, samples | A posteriori result |
|---|---|---|---|
| S809, $M=0.10$, $Re_c=2\times10^6$ | FI at $8^\circ$ and $14^\circ$ | (16, 16, 8), 300 epochs, 88 658 | lift error 2.4% at $8^\circ$, $-0.1\%$ at $14^\circ$ (Table 1); lift and drag improved at $Re_c=1$, 2 and $3\times10^6$ over a range of incidence, drag not used in FI (Fig. 10) |
| Parametrized hills, $Re_b=5600$ | FI on two hill-width factors | (32, 16, 8), 11 200 | closer to DNS than SA in most regions at an interpolated width (1.0) and extrapolated widths (0.5, 1.5); "can still be further promoted" (§3.2.2, Fig. 22) |
| GLC305/944 | FI1 at $4^\circ$ and $6^\circ$ | (64, 32, 16), 2000 epochs, 131 328 | lift error from $-21.5\%$ to $-7.0\%$ ($4^\circ$) and $-26.8\%$ to $-5.5\%$ ($6^\circ$); drag error from 6.4% to 3.5% and $-7.1\%$ to $-6.3\%$ (Table 4); good for incidence below $6^\circ$, deteriorating beyond (Fig. 33) |

The hills are the parametrized family of Xiao et al. (hill width scaled at
fixed height, $Re_b=5600$ on crest height and bulk velocity at the crest),
not the configuration of the [periodic hill](/benchmarks/periodic-hill.md)
benchmark at $Re_h=10{,}595$ (§3.2). All evidence is 2D steady RANS.

## Which term to correct (Cato et al. 2023)

[Cato et al. (2023)](/sources/cato-2023.md) study the inversion step alone.
They ask which of six space-dependent correction fields gives the best
fit, and which would be easiest to learn afterwards. The authors call them
"non-parametric" corrections. All six are compared with the same meshes,
numerics and cost, each optimized alone (§II B).

**Setting.**

- *Model.* Steady 2D incompressible RANS with the negative
  [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) of
  Crivellini et al., without the trip term; the vorticity magnitude is
  regularized with a constant $10^{-5}$ (§II A, Eqs. 2–4).
- *Discretization.* Continuous finite elements in FreeFEM++: bubble-enriched
  P1 for velocity, P1 for pressure and $\tilde\nu$, which "results in a
  first-order accurate scheme". Advection is stabilized by a simplified
  SUPG, and the steady equations are solved by Newton's method with the
  MUMPS direct solver. First cells lie below $y^+=1$ (§II E).
- *Data and cost.* Dense mean velocity from averaged DNS over the whole
  domain. The cost is
  $\mathcal L=\tfrac12\int_\Omega\lVert\langle\boldsymbol u\rangle_{\mathrm m}-\langle\boldsymbol u\rangle\rVert^2\,\mathrm d\Omega$,
  with no regularization (Eq. 6).
- *Gradients.* Adjoint equations are derived in continuous form (App. A).
  In practice the adjoint operator is the transpose of the discrete Newton
  Jacobian, combined with the continuous gradient expressions (Eq. 12). A
  finite-difference gradient test checks them (App. B).
- *Optimizer.* L-BFGS (SciPy), with a change of variables because the
  gradients are defined in the $L^2$ inner product (§II D).

**The six corrections (Eq. 5).** In registry notation, with subscript
$\mathrm m$ for the model's solution and $\mathcal P$, $\mathcal D$,
$\mathcal C$ (page-local) the Spalart–Allmaras production, destruction and
cross-diffusion terms, the augmented equations are

$$\begin{aligned}
\langle\boldsymbol u\rangle_{\mathrm m}\cdot\nabla\langle\boldsymbol u\rangle_{\mathrm m}+\nabla\langle p\rangle_{\mathrm m}-\nabla\cdot\big(2\nu\langle\boldsymbol S\rangle_{\mathrm m}\big)&=\nabla\cdot\big[2(1+\varphi)\nu_t\langle\boldsymbol S\rangle_{\mathrm m}+\boldsymbol\Psi\big]+\boldsymbol f_u,\\
\langle\boldsymbol u\rangle_{\mathrm m}\cdot\nabla\tilde\nu-\nabla\cdot\big(\nu_{\tilde\nu}\nabla\tilde\nu\big)&=\beta\,\mathcal P-\mathcal D+\mathcal C+f_{\tilde\nu}+g_{\tilde\nu}\,\tilde\nu,
\end{aligned}$$

plus continuity. Here $\nu_{\tilde\nu}$ is the model's diffusion
coefficient, and every correction is a function of $\boldsymbol x$
(page-local symbols):

| Correction | Where it acts | Keeps the Boussinesq form |
|---|---|---|
| $\boldsymbol f_u$ | momentum forcing vector, "not conservative in general" | no |
| $\boldsymbol\Psi=\begin{pmatrix}\psi_1&\psi_2\\\psi_2&-\psi_1\end{pmatrix}$ | trace-free symmetric tensor whose divergence forces momentum (conservative) | no |
| $\beta$ | multiplier of the model's production, after Singh & Duraisamy | yes |
| $f_{\tilde\nu}$ | additive source in the $\tilde\nu$ equation | yes |
| $g_{\tilde\nu}$ | source proportional to $\tilde\nu$; acts only where $\tilde\nu\neq0$ | yes |
| $\varphi$ | multiplier $(1+\varphi)$ of $\nu_t$ in the momentum equation | yes |

The four model-side corrections correct "only the length-scale of the
turbulence ... not the structure of the Reynolds-stresses" (§II B). The
authors state that $\boldsymbol\Psi$ is defined only up to
$(\psi_1+\partial_x\Phi,\ \psi_2+\partial_y\Phi)$ with
$\partial_{xx}\Phi+\partial_{yy}\Phi=0$ ($\Phi$ page-local), which gives
the same force. This freedom could be used to impose realizability (§II B).
The adjoint gradients show where each correction can act. The gradient for
$g_{\tilde\nu}$ (and for $\beta$) lives where $\tilde\nu$ (respectively
the production) overlaps the adjoint $\tilde\nu$. The gradient for
$f_{\tilde\nu}$ lies "more upstream", where the adjoint is largest, so
this correction can act in a "non-physical upstream region, where
Reynolds stresses are weak" (§II C).

**Test cases.**

- a converging–diverging channel at $Re=12{,}600$ on the inlet reference
  velocity (DNS of Marquillie et al.), with a thin adverse-pressure-gradient
  separation that baseline SA places too far downstream (§III);
- the [periodic hill](/benchmarks/periodic-hill.md) at bulk $Re=2800$
  (§IV);
- a square cylinder at $Re=22{,}000$ (DNS of Trias et al. 2015), with
  separation fixed at the corners and no error table (§V).

**Fit quality (Tables I–III).** The errors are global relative $L^2$ errors
of the velocity, $E_u$, and of the wall skin friction, $E_{C_f}$
(page-local names).

| Correction | channel $E_{C_f}$ | channel $E_u$ | hill $E_{C_f}$ | hill $E_u$ | square cylinder (Table III) |
|---|---|---|---|---|---|
| none (baseline SA) | 0.39 | $4.9\times10^{-2}$ | 0.38 | $7.1\times10^{-2}$ | — |
| $\boldsymbol f_u$ | 0.059 | $3.1\times10^{-3}$ | 0.17 | $3.8\times10^{-3}$ | best |
| $\boldsymbol\Psi$ | 0.057 | $2.9\times10^{-3}$ | 0.26 | $3.7\times10^{-3}$ | best |
| $\beta$ | 0.18 | $8.4\times10^{-3}$ | 0.27 | $3.2\times10^{-2}$ | partial |
| $f_{\tilde\nu}$ | 0.19 | $8.1\times10^{-3}$ | 0.23 | $7.8\times10^{-3}$ | partial |
| $g_{\tilde\nu}$ | 0.12 | $4.6\times10^{-3}$ | 0.20 | $7.5\times10^{-3}$ | best |
| $\varphi$ | 0.23 | $1.2\times10^{-2}$ | 0.30 | $4.3\times10^{-2}$ | failure |

- *Momentum corrections.* $\boldsymbol f_u$ and $\boldsymbol\Psi$ fit best
  everywhere. In the channel the cost falls by "almost three orders of
  magnitude" (§III B, Fig. 3).
- *Best model-side correction.* $g_{\tilde\nu}$ comes close to the momentum
  corrections in all three cases. On the square cylinder it "performed
  almost as well as the source terms in the momentum equations" (§V B). It
  also lowers the cost faster than $f_{\tilde\nu}$ in the channel and on
  the hill (§IV B).
- *Eddy-viscosity multiplier.* $\varphi$ is the poorest and fails on the
  square cylinder. Its gradient stays on a "high plateau" while the other
  gradients fall by three to four orders of magnitude (App. B, Fig. 21). In
  the channel it "rapidly interrupts the L-BFGS iterations". The authors
  call the problem ill-conditioned, in agreement with Dow & Wang (§III B).
- *Robustness.* Corrections placed on the transport model "improve[s]
  numerical robustness regardless of the test case" compared with $\varphi$
  (§VII).
- *Skin friction.* The $L^2$ velocity cost favours the bulk over thin
  near-wall regions, so profiles of $u^+$ scaled with each fit's own
  $u_\tau$ show differences that the DNS scaling hides (§III B, Fig. 4).

**Over-learning.** In the channel, $g_{\tilde\nu}$, $f_{\tilde\nu}$ and
$\beta$ recover the mean velocity "very accurately", but "at the expense of
large eddy-viscosity corrections, which very strongly overshoot the
reference values"; the authors call this "a classical over-learning
situation" (§III B, Fig. 6). The reference is a DNS estimate of the eddy
viscosity (Eq. 18, recalled from Volpiani et al. 2022), which the authors
call an approximation that is good for attached flows. Translated to the
registry it reads
$\nu_t=-(R_{ij}-\tfrac23k\delta_{ij})S_{ij}/(2S_{kl}S_{kl})$, the
least-squares fit of the Boussinesq form, and it coincides with the optimal
eddy viscosity of Wu et al. used by
[McConkey et al. (2022)](/sources/mcconkey-2022.md) (§II A, Eq. 6)
*(compiler check, not in the sources)*. In the same channel, the $\varphi$
fit gives a $(1+\varphi)\nu_t$ "pretty much in agreement" with that
estimate, noisy only where the flow separates (Fig. 6f). The authors
propose two untested regularizations: a penalty on the squared correction,
or on the distance of $\nu_t$ from the baseline RANS value (Eqs. 19–20).

**Stress alignment does not decide the mean flow.** The authors measure the
alignment of Reynolds stress and mean strain with Schmitt's indicator
(Eq. 21), masked to $k>0.1k_{\max}$, with a plotted threshold of 0.8.

- *Channel.* The indicator falls below 0.8 near the wall behind the bump
  in reverse flow, yet the $g_{\tilde\nu}$ fit reconstructs that region well
  (§III C, Fig. 7).
- *Hill.* It is below 0.8 "in much of the domain below" the hill crest
  height, yet $f_{\tilde\nu}$ and $g_{\tilde\nu}$ recover the DNS velocity
  and skin friction. The authors conclude that "missing the proper stress
  alignment does not play a large role for predicting the mean flow" (§IV,
  Figs. 8–10).
- *Square cylinder.* It exceeds 0.8 only in "a few areas" (§V A, Fig. 12).

See [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md).

**The Reynolds-force vector.** The mean flow depends on the Reynolds
stresses only through the force they exert. In registry notation it is
$f^R_i=-\partial_jR_{ij}+\tfrac23\partial_ik$ (page-local name and symbol;
Eqs. 7–8, the gradient part being absorbed in the pressure).

- *Stresses not identified.* With only mean velocity in the cost there is
  "no a-priori reason" for the inferred stresses to match the DNS (§II B).
- *Square cylinder.* Baseline SA stresses are "very weak compared to the
  DNS". Assimilation raises them, but no correction matches the DNS
  stresses, not even $\boldsymbol\Psi$ with its large drop of the cost, and
  near the corners the $\boldsymbol\Psi$ and $g_{\tilde\nu}$ stresses are
  wrong. Hence "the mean-flow prediction can be accurate even though the
  Reynolds stresses are wrong" (§V C, Figs. 16–17).
- *Force against stress.* $\boldsymbol\Psi$ captures the streamwise force
  component reasonably well despite wrong stresses: "even with the wrong
  stresses, it is possible to have accurate mean fields, as long as the
  Reynolds force vector is correctly represented". $\boldsymbol f_u$
  captures the streamwise component but not the cross-stream one (Figs.
  18–19).
- *Realistic stresses from $g_{\tilde\nu}$.* $g_{\tilde\nu}$ "manages to
  capture a realistic stress tensor especially in the wake region", and its
  force field approximates the DNS better in the recirculation (Figs.
  17–19).
- *As a learning target.* As recalled there (§I), Cruz et al. and Berrone &
  Oberto proposed the Reynolds-force vector as the target of machine
  learning, to avoid the ill-conditioning of injecting learned stresses.

**What to learn next (§VI, Table III).**

- $\boldsymbol f_u$ and $\boldsymbol\Psi$ are dimensional vectors and
  tensors. They need more resources, and rotational invariance is "non
  trivial (especially in 3D)".
- $\beta$ and $\varphi$ are dimensionless scalars.
- $f_{\tilde\nu}$ and $g_{\tilde\nu}$ are scalars but "not naturally
  dimensionless".

The summary table ranks $\boldsymbol f_u$, $\boldsymbol\Psi$ and
$g_{\tilde\nu}$ best in all three cases. For skin friction the conclusions
name the same three (§VII). Only dense velocity data were treated; sparse
data are left to future work.

## A stochastic stress discrepancy (Agrawal & Koutsourelakis 2024)

[Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) infer a
correction of a different kind and in one stage. Their closure of steady
incompressible RANS is the sum of a parametric part, a
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
and an additive discrepancy $\boldsymbol\delta_R$ (page-local, as on the
model-form-uncertainty page) of the discrete Reynolds-stress field (§2.2.2, Eq. 13). The discrepancy is a
latent random field, piecewise constant on $N_d=52$ fixed subdomains of
the 12 180-node mesh, with a separate realization for each training flow
and an automatic-relevance-determination prior that switches it off where
the parametric part suffices (Eqs. 19–21, Table 3). Network weights and
the discrepancy are inferred together, by stochastic variational inference,
from sparse LES mean velocity and pressure at about 8% of the mesh nodes;
the gradients come from a discrete adjoint of a FEniCS finite-element RANS
solver coupled to PyTorch (§2.2.3–2.2.4, App. B). Prediction propagates
samples of the discrepancy through the solver (§2.2.5, Eq. 32); details are
on [model-form uncertainty](/definitions/model-form-uncertainty.md).

The authors contrast this with the field inversions above: earlier
adjoint-based inversions "retain" the linear eddy-viscosity model, and
others ignore the model error of the learned closure (§1). Their
discrepancy is tied to the grid and geometry: it carries over to other
Reynolds numbers or boundary conditions in the same geometry, not to a new
geometry (§2.2.3, §2.2.5). On a [backward-facing step](/benchmarks/backward-facing-step.md)
(expansion ratio 2, trained at four step-height Reynolds numbers from 300
to 1100, tested at 500) the predicted reattachment length is
$x_R/h=10.06\pm1.21$ (three standard deviations) against 9.10 in LES,
5.61 for the baseline $k$-$\varepsilon$ model and 5.52 for a tensor-basis
network trained on stress data by Geneva & Zabaras (§3.4, Table 5). The
inferred discrepancy is largest at $5<x/h<10$, where the parametric
stress errs most, and practically zero far downstream (Fig. 7). The mean
fields agree with LES although the learned stresses do not, which the
authors read as non-uniqueness of the inverse problem, "also reported by
other works" (§3.4). One run of their solver costs 1.3 baseline RANS runs, the reference LES
7679 (Table 4).

## Conditioned field inversion (Wu et al. 2025)

[Wu et al. (2025)](/sources/wu-2025.md) (author manuscript) correct the
destruction term of the $\omega$ equation of the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) and ask whether
the correction spoils the baseline where the baseline was right.
Page-local: $\beta_\omega$ is the $\omega$-destruction coefficient of SST
(the blended $\beta_1$, $\beta_2$; the paper's $\theta$), $\gamma_\omega$
its $\omega$-production coefficient, $\sigma_\omega$ its $\omega$-diffusion
coefficient.

**Why classic inversion breaks attached flow (§2.1, Eqs. 3–4).** Citing
Wilcox, the authors state that the log layer of $k$-$\omega$ models requires
$\beta_\omega-\beta^*\gamma_\omega=\kappa^2\sqrt{\beta^*}\,\sigma_\omega$
with $\kappa=0.41$. With the classic correction
$-\beta(\boldsymbol x)\beta_\omega\rho\omega^2$ the constraint becomes
$\beta\beta_\omega-\beta^*\gamma_\omega=\kappa^2\sqrt{\beta^*}\sigma_\omega$,
so any $\beta\ne1$ in the log layer breaks the calibration; the authors add
that wake-law calibrations under pressure gradient are affected too.

**Conditioned inversion (Eqs. 5–6).** The destruction term becomes

$$-\big[(\beta(\boldsymbol x)-1)f_d+1\big]\beta_\omega\rho\omega^2,\qquad f_d=1-\tanh\big[(8r_d)^3\big],\quad r_d=\frac{\mu+\mu_t}{\rho\kappa^2d^2\sqrt{\partial_ju_i\,\partial_ju_i}},$$

with $f_d$ the DDES shielding function of Spalart et al. (2006) as printed
(see [detached-eddy simulation](/methods/detached-eddy-simulation.md)):
$f_d=0$ inside the attached boundary layer, where the model is exactly
SST, and 1 outside, where the correction acts. The same gate is used in
inversion and in prediction. The assumption, stated by the authors, is
that the baseline computes the attached boundary layer accurately and
needs no change there (§1); the justification is that separation errors
arise mainly in the separated shear layer, outside the shielded region
(§2.1, citing earlier studies). The authors state that no earlier work applied such a
filter in the inversion stage; filters had been used for zonal models,
adverse-pressure-gradient detection and cost reduction (§1).

**Inversion set-up (Eqs. 7–15, 18).** Cost
$\lambda_{\mathrm{QoI}}\sum_i(Y_i-Y_{\mathrm m,i})^2+\lambda_{L2}\sum_j(\beta_j-1)^2$
on LES streamwise velocity at 30 random points in the separation region
(curved backward-facing step) or 40 (wall-mounted hump), with
$\lambda_{\mathrm{QoI}}$ set so that the cost is about 1 at $\beta\equiv1$
and $\lambda_{L2}=10^{-5}$ to $10^{-4}$ chosen as large as still gives a
"decent drop" in error (rule of thumb: penalty 10–20% of the final data
error). SLSQP with discrete-adjoint gradients from DAFoam on
[OpenFOAM](/software/openfoam.md), Jacobians by automatic differentiation.

| Training case | Cost reduction, classic | Cost reduction, conditioned | Where $\beta$ departs from 1 |
|---|---|---|---|
| curved [backward-facing step](/benchmarks/backward-facing-step.md), $Re_h=13\,700$ | 88.3% | 74.7% | classic: shear layer and the attached layer upstream of the step; conditioned: shear layer only |
| [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md), $Re_c=0.936\times10^6$ | 61.7% | 66.7% | classic: about 2 near the shear layer and inside the attached layer on the hump top; conditioned: 4–5 around the shear layer only |

(§3.1, Figs. 4–12; about 140 SLSQP iterations on the hump.) The
inverted fields are then fitted by symbolic regression to closed forms
(see [symbolic-regression closures](/methods/symbolic-regression-closure.md)),
SR-CLS from the classic and SR-CND from the conditioned data, inserted
into the corresponding equations and called at every iteration; they add
about 15% and 10% to the runtime, against about 30 times for a random
forest called every iteration, as reported by Yin et al., whom they cite (§3.2).

**Generalizability levels (§1, Table 1).** The authors grade field
inversion and machine learning by four levels: **L1**, geometries similar
to the training ones; **L2**, no degradation of the baseline in simple
attached flows; **L3**, the same separation mechanism in other geometries
and Reynolds numbers; **L4**, different separation mechanisms. Most
earlier studies, they state, test only L1; they cite Spalart for making
L2 a hard constraint. As they cite, an inversion-trained model built
on an adverse-pressure-gradient plate failed on the zero-pressure-gradient
plate (Rumsey et al.), and Gaussian-process deactivation of corrections
gained L2 at the cost of L1 and L3 (Pepper, Ho et al.).

**Results (§3.3, §4, Tables 5–7).**

| Test | Level | SST | SR-CLS | SR-CND |
|---|---|---|---|---|
| hump, $C_f$ error in the separation zone (vs experiment) | training | 100% | about 6.7% of SST | about 6.7% of SST |
| hump top, $C_f$ error | training | 100% | 160% of SST | about equal to SST |
| [periodic hills](/benchmarks/periodic-hill.md), slope factor 0.8, $Re=5600$: reattachment (DNS $x\approx5.2$) | L1/L3 | no reattachment before the next hill | about 6.0 | about 6.0 |
| NLR-7301 two-element airfoil, $C_{L,\max}$ (exp. 3.03), stall angle (exp. $14.1^\circ$) | L3 | 2.84, $11.1^\circ$ | 2.94, $13.1^\circ$ | 3.00, $13.1^\circ$ |
| SAE notchback, $C_D$ (exp. 0.207) | L3 | 0.181 | 0.209 | 0.211 |
| 25° [Ahmed body](/benchmarks/ahmed-body.md), velocity-profile error | L3 | 0.677 | 0.069 | 0.072 |
| zero-pressure-gradient [flat plate](/benchmarks/turbulent-boundary-layer.md), $Re_L=10^7$ | L2 | matches data | over-predicts $C_f$, wrong log layer, $\beta\approx1.06$ in the layer | matches SST, $\beta=1$ |
| [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $0^\circ$, $Re_c=6\times10^6$ | L2 | reference | over-predicts $C_f$ | about SST |

On the notchback, SR-CLS raises $\beta$ near the wall and distorts the
upper-surface $C_p$; SR-CND keeps $\beta=1$ there and has smaller $C_p$
errors (§4.3). The NLR-7301 runs use a compressible code (CFL3D) other
than the training code, stably (§4.2). The authors conclude that the
conditioned version has L3 generalizability similar to the classic one
while keeping L2 (§5). All evidence is numerical, with grid checks on
three meshes for the test cases.

## Field inversion on a high-order DG discretization (Fanizza et al. 2025)

[Fanizza et al. (2025)](/sources/fanizza-2025.md) study the inversion step
alone for compressible steady RANS with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
(Spalart–Garbaruk $c_{w2}$ correction, negative-SA limiting), discretized
by a high-order modal discontinuous Galerkin method (orthonormal
total-degree basis, BR2 viscous fluxes, Roe or local Lax–Friedrichs
convective fluxes) in ONERA's Aghora code (§2). The motivation (§1):
corrections inferred on diffusive second-order finite-volume
discretizations carry discretization error and may not extrapolate to
other meshes or codes (see
[discretization-consistent closure](/definitions/discretization-consistent-closure.md));
the authors state that earlier field inversion used low-order discretizations
except Ferrero et al. (DG, subsonic).

**Optimization (§3, Eqs. 16–41).** The correction is sought in the DG
polynomial space, one set of modal coefficients per element; the cost is
an $L^2$ data misfit, optionally plus an $L^2$ penalty on the correction.
The gradient is a discrete adjoint consistent with the discretization,
with residual derivatives from Tapenade automatic differentiation, checked
against finite differences (App. A). The optimizer is L-BFGS; because it
uses Euclidean inner products, the gradient is rescaled by the Cholesky
factor of the (diagonal) mass matrix so that it mimics the continuous
$L^2$ gradient and is mesh-independent (Eqs. 37–41). The stiff adjoint
systems need a flexible inner–outer GMRES: on the square cylinder,
GMRES(180) with block ILU(0) does not converge, flexible GMRES converges in
12 000 matrix–vector products and its deflated-restart variant in 8000;
the inner solve runs in single precision, halving matrix storage (§3.4.1,
Fig. 2).

**Four corrections (§3.3).** In the convention of this page (production
multiplier with baseline 1):

| Paper's name | Correction | Corresponds to Cato et al.'s |
|---|---|---|
| DA-$\boldsymbol f$ | source $\rho\boldsymbol f$ in momentum, with its power $\boldsymbol u\cdot\boldsymbol f$ plus a heat-flux correction in energy | $\boldsymbol f_u$ |
| DA-$\chi$ | multiplier $(1+\chi)$ of $\mu_t$ in the Reynolds stress, kept positive by a smooth limiter | $\varphi$ |
| DA-$f_{\tilde\nu}$ | source $\rho\tilde\nu f_{\tilde\nu}$ in the SA equation | $g_{\tilde\nu}$ |
| DA-$\beta$ | multiplier $\beta$ of the SA production (the paper's $1+\beta$) | $\beta$ |

(Correspondence by the printed forms; the paper attributes its third term
to Cato et al. as a source term in the SA equation.)

**Results (§4).**

- *Laminar cylinder, $Re=80$, $M=0.15$ (§4.1, Figs. 4–6).* With dense
  time-averaged DNS velocity, the momentum source fits the mean flow at
  polynomial degrees 1, 2 and 3; the cost falls by more than three orders
  of magnitude at degree 1 and more than four at 2 and 3, lowest at degree
  2, the lowest at which the baseline is free of grid dependence. The
  authors recommend running data assimilation "at the lowest degree $p$
  for which the baseline model exhibits no grid-dependency errors".
- *[Square cylinder](/benchmarks/square-cylinder-flow.md), $Re=22\,000$,
  $M=0.1$ (§4.2, Figs. 7–8).* Ranking: momentum source best (cost down by
  more than two orders), then $f_{\tilde\nu}$ (more than one) and $\beta$
  (at least one); the eddy-viscosity multiplier stalls on a plateau "from
  the very first iterations". The authors state agreement with Cato et al.
  (2023), whose incompressible ranking is the same (section above).
- *[Shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md),
  $M_\infty=2.28$, $9.5^\circ$ deflection, DNS reference (§4.3).*
  Normalized errors (1 = baseline):

  | Data | Correction | velocity | $C_p$ | $C_f$ |
  |---|---|---|---|---|
  | dense velocity, wall-weighted | momentum source | 0.049 | 0.1825 | 0.0998 |
  | | $\chi$ | 0.250 | 0.5788 | 0.5689 |
  | | $f_{\tilde\nu}$ | 0.257 | 0.2076 | 0.8920 |
  | | $\beta$ | 0.339 | 0.2829 | 1.1450 |
  | wall $C_p$ only | momentum source | 0.488 | 0.00106 | 0.8540 |
  | | $\chi$ | 0.458 | 0.17357 | 1.657 |
  | | $f_{\tilde\nu}$ | 0.542 | 0.04961 | 1.700 |
  | | $\beta$ | 0.427 | 0.05982 | 1.559 |

  (Tables 1–2.) With dense data only the momentum source lowers the cost
  by one to two orders of magnitude and corrects quantities absent from the
  cost; the authors add that the three other corrections "are still
  constrained by the Boussinesq assumption", whereas the source corrects
  the Reynolds-stress divergence directly, which matters where the stress
  is not aligned with the strain (§4.3.1; see
  [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). With wall
  pressure only, the source cuts the $C_p$ error by three orders of
  magnitude, all four reduce the velocity error similarly, and the three
  Boussinesq-type corrections make $C_f$ worse than the baseline over the
  whole wall (§4.3.3). An $L^2$ penalty on the correction reduces its norm
  but does not significantly improve the near-wall velocity and $C_f$; the
  authors conclude that sparse data need regularization built on physical
  prior knowledge (§4.3.4, §5, Tables 3–4).

The paper also proposes the inferred fields as detectors of RANS-model
failure (§5). Discrete adjoints give more accurate gradients than
continuous ones, the authors state, at higher cost in large 3-D problems
(§1).

## Generalization across flow classes

[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (§1) state that
corrections trained on narrow flow classes "do not generalize to radically
different flows, and often deteriorate the representation of canonical
flows", while training on many flows at once "may lead to a soft
compromise solution". Their answer is to keep several class experts and
blend them with learned weights (see
[model aggregation](/methods/turbulence-model-aggregation.md)); the answer
of Wu et al. (2025) is to switch the correction off where the baseline is
trusted. Both protect attached flow: the blend reproduces SST in a channel
at $Re_\tau=1000$, the conditioned model reproduces it on the flat plate.

## Consistency claims

Both reviews argue that FIML is preferable to learning directly from DNS,
because the training targets come from the environment in which the model
is used:

- Duraisamy et al. (2019, §5.4, §6) recommend that inference precede
  learning, which "enforces consistency" between the learning and
  prediction environments.
- Duraisamy (2021, §IV.B) states a weaker version. FIML "promotes"
  consistency, but imperfections of the regression step (Eq. 8)
  reintroduce inconsistency. Only an integrated optimization, in which the
  learned map sits inside the constraint and the loss is evaluated on model
  outputs, "ensures full consistency" (Eq. 9; see
  [model-consistent training](/methods/model-consistent-training.md)).
- The integrated route has a cost: features must be chosen before
  inference. The separate FI and ML stages are more flexible (§IV.B).
- Yan et al. (2022, §3.1.2, Table 1) give a concrete instance of the
  inconsistency that Duraisamy (2021) assigns to the regression step: on
  S809, regression error and a posteriori lift error of the embedded model
  are not monotonically related across twelve network settings. The paper
  keeps the two-step form and moves the model selection, not the training,
  into the solver (see
  [model-consistent training](/methods/model-consistent-training.md)).
- Cato et al. (2023, §I) give the same reason for the two steps: features
  computed from DNS can make the learned field "inconsistent with the RANS
  model structure", and correcting the Reynolds stresses directly can be
  ill-conditioned. Their results add a caveat for the first step: the
  inferred field is consistent with the model, but not unique, and it can be
  over-fitted.
- Two further sources take other routes to data in RANS. McConkey et
  al. (2022) train on labels computed from DNS and inject the prediction
  once into a converged RANS solution, the open-loop alternative described
  on [model-consistent training](/methods/model-consistent-training.md).
  [Eivazi et al. (2022)](/sources/eivazi-2022.md) solve the RANS equations
  with a [physics-informed neural network](/methods/physics-informed-neural-network.md)
  closed by boundary data instead of a turbulence model. Neither paper
  compares itself with field inversion.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) take the
  integrated route for LES, with no inferred field in between: the
  network parameters $\boldsymbol\theta$ are optimized directly through the
  continuous adjoint of the LES equations (§2.2, Eqs. 2.9–2.10; see
  [model-consistent training](/methods/model-consistent-training.md)). As
  recalled there (§1), adjoint-based model-consistent RANS closures go
  back to Parish & Duraisamy (2016), with further work by He, Liu & Gan
  (2018) and an adjoint eddy-viscosity correction by Brenner et al. (2022).
  The authors state that "traditional one- or two-equation closures", or
  any multiparametric closure, could replace the network in the same
  adjoint framework (§2, §7).

## Qualifications

- **Identifiability.** Duraisamy (2021, §VII, Fig. 4) shows a
  model-consistent inference in channel flow. An anisotropy perturbation is
  inferred from mean-velocity data. It reproduces the mean velocity and the
  Reynolds shear stress accurately, but not the anisotropy. The author
  states that using the full Reynolds-stress tensor as data would remedy
  this. No Reynolds number is given. Yan et al. (2022, §3.1.1, §3.2.1)
  meet the same problem as the non-uniqueness of $\beta$ when the data
  are a single integral quantity, and answer it with priors rather than
  with more data, except on the iced airfoil, where adding drag to lift
  improves the unobserved pressure (§3.3.1). Cato et al. (2023) show the
  same limit with dense data. Mean velocity over the whole domain fixes
  neither the Reynolds stresses (square cylinder, §V C) nor the eddy
  viscosity (channel, §III B, Fig. 6). The tensor correction
  $\boldsymbol\Psi$ is non-unique by construction (§II B).
- **Regime of the stochastic-discrepancy test.** The backward-facing-step
  cases of Agrawal & Koutsourelakis (2024) have step-height Reynolds
  numbers of 300 to 1100, with WALE LES references and a
  $k$-$\varepsilon$ baseline (§3.1–3.2).
  The paper also prints the isotropic part of the Reynolds stress with a
  sign inconsistent with its Eq. 9 definition $-\langle u_i'u_j'\rangle$
  (Eqs. 10, 14), and its Table 2 lists five viscosities for four training
  Reynolds numbers; this page uses the positive registry convention.
- **Generalization.** Duraisamy (2021, §VII) states that "the goal of more
  generalizable models has, however, not been achieved". Machine-learning
  regressions are interpolative in feature space (§V), and a model with
  $n$ features needs data that populate an $n$-dimensional space (the
  paper's $d$; renamed here because $d$ is the wall distance).
- **L1 errors remain.** Single-point, Markovian closures carry structural
  errors that no learned correction removes (Duraisamy 2021, §VII;
  Duraisamy et al. 2019, §2).
- The two reviews use different symbols for the same objects. Duraisamy
  et al. (2019) write the data as $\boldsymbol\theta$, the features as
  $\boldsymbol\eta$ and the discrepancy as $\boldsymbol\delta$. Duraisamy
  (2021) writes the data as $Y$, the features as $\tilde\eta_m$, the
  network weights as $w$ and the inferred field as $\delta^i_m$. This page
  translates all of them to the registry.
- Duraisamy (2021) prints Eq. 7 with the parametric model
  $\delta_m(\tilde\eta_m;w)$ in the constraint, although the optimization
  variable is the field $\delta^i_m$. The text also introduces the data as
  "$\tilde Y^i$" while the loss uses $Y^i$. This page writes the
  constraint with the field being inferred, as the surrounding text
  describes.
- Yan et al. (2022) print slips that bear on the numbers above. The text
  of §3.2.2 names the two hill training geometries as width factors 0.5
  and 0.8, while the same section calls 0.5 an extrapolation case; the
  training set is therefore ambiguous as printed. The periodic-hill
  objective (Eq. 17) carries an index mismatch ($\lambda_i$ under a sum
  over $j$), and the text then uses a scalar weight $\lambda=8\times10^{-6}$.
  Table 4's baseline SA errors ($-21.5\%$, $-26.8\%$ in lift) do not equal
  the relative errors computed from Table 3 ($-19.6\%$, $-26.0\%$)
  *(compiler check, not in the sources)*; the reductions quoted above are
  those of Table 4.
- Yan et al. (2022) write the SA working variable as $\tilde\nu$ and the
  data as $d_i$, the model prediction as $h_i(\boldsymbol\beta)$, the
  features as $\eta$; this page translates them to $Y_i$,
  $Y_{\mathrm m,i}(\beta)$ and $\boldsymbol\zeta$. The paper's $\alpha$ is
  both the angle of attack and the hill-width factor; the page uses words
  for both.
- **Convention of the production multiplier.** Cato et al. (2023, Eq. 5)
  write it as $(1+\beta)$ with baseline $\beta=0$. Duraisamy et al. (2019)
  and Yan et al. (2022) write $\beta$ with baseline $\beta=1$. This page
  writes $\beta$ throughout, so Cato et al.'s field is $\beta-1$ here. The
  paper's tilde marks the model's solution (here subscript $\mathrm m$), its
  overbar the DNS mean (here $\langle\cdot\rangle$). Its
  $\nabla_s=\nabla+\nabla^T$ is twice the strain-rate operator. Its letters
  $\xi$, $\gamma$, $\delta$, $\boldsymbol R_{\gamma\delta}$ and
  $\tilde{\boldsymbol f}_u$ are translated to $\varphi$, $\psi_1$,
  $\psi_2$, $\boldsymbol\Psi$ and $\boldsymbol f_u$, because the registry
  gives the originals other meanings. Its $k$ is both the turbulent kinetic
  energy and the von Kármán constant.
- **Printed slips in Cato et al. (2023).** Eq. 9 prints the DNS stress as
  $-\nabla\cdot(\overline{\boldsymbol u'\otimes\boldsymbol u'})+\tfrac23k\boldsymbol I$,
  a vector added to a tensor. The text calls it "the traceless Reynolds
  stress tensor" (§V C), which fits the form without the divergence.
  Eq. 2b prints the DNS mean $\overline{\boldsymbol u}$ in the viscous term
  of the model equation, where Eq. 5 has the model's velocity. The 0.86
  threshold is attributed to Schmitt, but the figures and text use 0.8
  (§III C, §V A).
- **Scope of the conditioned inversion.** Wu et al. (2025) train on two
  separations from curved surfaces (curved step, hump) and test mostly
  separation from edges or shear layers; their Table 1 example of L3 for
  smooth-surface separation is not tested on its own. The method assumes
  that no correction is needed inside attached boundary layers (§1); where
  $f_d=0$ the model is exactly SST (Eq. 5), so it cannot change a
  separation onset decided inside the shielded layer *(compiler check, not
  in the sources)*.
- **Printed slips in Wu et al. (2025).** §3.2 refers to the features of
  "Table 3" (they are in Table 2); the Fig. 44 caption writes "SST-CLS" for
  SR-CLS; Table 7 is captioned as mean square errors while its row is
  labelled RMSE; §4.5 refers to Figure 45 for the airfoil grid (it is Fig.
  49); the integrated friction coefficient of Eq. 21 divides the already
  dimensionless $C_f$ by a dynamic pressure. The paper writes the eddy
  viscosity as $\mu_t$, $\mu_T$ and $\nu_t$ interchangeably and uses
  $\gamma$ also for a sample ratio.
- **Fanizza et al. (2025): text against tables.** §4.3.1 says the three
  other corrections reduce "the three errors" by less than an order of
  magnitude, but Table 1 gives the production multiplier a $C_f$ error of
  1.1450, above the baseline. §4.3.4 says the penalty degrades the
  velocity and wall-pressure errors; against Table 2, Table 3 shows the
  velocity error improving for the $\chi$, $f_{\tilde\nu}$ and (at one
  weight) $\beta$ corrections *(compiler check, not in the sources)*. Tables
  3 and 4 print different penalty weights for the $f_{\tilde\nu}$ and
  $\beta$ runs. The correction space is written $(\mathcal V_h^p)^{d+2}$
  while the printed source vector has $d+1$ free components, and the
  polynomial space is described as tensor-product although its dimension
  $(p+d)!/(p!d!)$ is that of total-degree polynomials. The
  Reynolds-number of the shock interaction is not printed.
- **Ranking in Cato et al. (2023).** Table III rates $f_{\tilde\nu}$ in the
  top class and $\beta$ in the middle class for the channel, while Table I
  gives the two nearly equal errors there ($E_u$ $8.1\times10^{-3}$ against
  $8.4\times10^{-3}$; $E_{C_f}$ 0.19 against 0.18). On the hill the ranking
  follows Table II. All three cases are 2D steady RANS with dense velocity
  data.

# Citations

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (layers L1–L4), §3.2 and box p. 7 (MAP), §4.1, §5.1 (field inversion, Figs. 4–5), §5.2 (feature space), §5.4 and §6 (FIML, Fig. 8; inference before learning).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §I, §IV.B, Eqs. 7–9 (FI, FIML, integrated training), §V (features), §VII (identifiability, Fig. 4; generalization).
- [Cato et al. (2023)](/sources/cato-2023.md) — HAL author manuscript: §I (FIML rationale, Reynolds-force targets), §II A–E, Eqs. 2–12 (model, six corrections, cost, adjoint, optimizer, discretization), §III B–C, Figs. 3–7, Table I, Eqs. 18–21 (channel, over-learning, alignment), §IV, Figs. 8–10, Table II (hill), §V, Figs. 11–19 (square cylinder, stresses, Reynolds force), §VI–VII, Table III; App. B, Figs. 20–21.
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — arXiv v1: §II A, Eq. 6 (optimal eddy viscosity, compared with Cato et al.'s Eq. 18), §II D (open-loop injection).
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — arXiv v1: §1–2 (RANS closed by boundary data, no turbulence model).
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §1 (adjoint-based RANS closures recalled), §2, §2.2, Eqs. 2.9–2.10, §7 (integrated adjoint training of an LES closure).
- [Yan et al. (2022)](/sources/yan-2022.md) — accepted manuscript, §1, §2.1–2.3, Eqs. 5–11, 14–17; §3.1 (S809, Figs. 4–7, 10, Table 1); §3.2 (parametrized hills, Figs. 11, 13–22, Table 2); §3.3 (GLC305/944, Figs. 25–33, Tables 3–4).
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — arXiv v2: §1 (earlier adjoint inversions), §2.2.2–2.2.5, Eqs. 13, 19–21, 32, App. B (stochastic discrepancy, adjoint, variational inference); §3.1–3.4, Fig. 7, Tables 2–5 (backward-facing step).
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §II.B (ensemble Kalman calibration), §V (data-assimilation alternatives).
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §1, Table 1 (L1–L4, earlier work); §2.1, Eqs. 1–6 (log-layer constraint, conditioned inversion); Eqs. 7–15, 18 (cost, adjoint); §3.1, Figs. 4–12; §3.2 (cost of the learned models); §3.3, §4, Tables 5–7, Figs. 15–50; §5.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §1 (discretization error, adjoints, earlier DG work); §2–3, Eqs. 1–41, Fig. 2 (DG RANS, corrections, discrete adjoint, gradient scaling, flexible GMRES); §4.1–4.3, Figs. 4–15, Tables 1–4; §5; App. A.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §1 (class-specific corrections, multi-flow training).
