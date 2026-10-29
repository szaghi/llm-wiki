---
type: Method
title: "Explicit algebraic Reynolds-stress models"
description: "RANS closures that give the Reynolds-stress anisotropy as an explicit sum of Pope's integrity-basis tensors with invariant-dependent coefficients: the classical equilibrium-derived forms and BSL-EARSM, the learned forms (gene-expression programming, sparse and sparse Bayesian regression with a production correction), and their heat-flux analogue."
status: established
aliases: [EARSM, EASM, ASM, algebraic stress model, explicit algebraic stress model, explicit algebraic Reynolds stress model, BSL-EARSM, non-linear eddy-viscosity model, generalized eddy-viscosity hypothesis, stochastic EARSM, SBL-SpaRTA EARSM]
tags: [rans, reynolds-stress-model, eddy-viscosity, data-driven, symbolic-regression, turbomachinery]
timestamp: 2026-10-29T16:21:00Z
---

# Explicit algebraic Reynolds-stress models

An explicit algebraic Reynolds-stress model (EARSM, also EASM) expresses
the anisotropy of the Reynolds stress as an explicit function of the
mean strain and rotation, without transporting the stresses:

$$b_{ij}=\sum_{n=1}^{10}g^{(n)}(I_1,\dots,I_5)\,T^{(n)}_{ij},$$

with $T^{(n)}$ the ten integrity-basis tensors of Pope (1975) built from
the mean strain and rotation scaled by a turbulence time scale, and
$g^{(n)}$ scalar functions of five invariants (registry §3). The first
term, with $g^{(1)}<0$, is the [Boussinesq](/definitions/boussinesq-hypothesis.md)
relation; the others add the non-linear stress–strain dependence that a
[differential Reynolds-stress model](/methods/reynolds-stress-model.md)
would produce. Classical EARSMs derive the $g^{(n)}$ from the
Reynolds-stress transport equations; data-driven ones learn them
([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §3.2, Eqs. 2–4;
[Cherroud et al. (2022)](/sources/cherroud-2022.md), §1, §2.1).

## Form

Sandberg & Zhao (2022) write the stress as the Boussinesq term plus the
expansion, labelling the three parts (§3.2, Eq. 2; kinematic,
incompressible form in registry notation, with their sign convention
corrected as on the Boussinesq page):

$$R_{ij}-\tfrac23k\delta_{ij}=\underbrace{-2\nu_t\langle S^d_{ij}\rangle}_{\text{linear Boussinesq}}+\underbrace{2k\,g^{(1)}T^{(1)}_{ij}}_{\text{additional linear term}}+\underbrace{2k\sum_{n=2}^{10}g^{(n)}T^{(n)}_{ij}}_{\text{additional non-linear terms}}.$$

Sandberg & Zhao build the basis from the mean strain and rotation
multiplied by a turbulence time scale $t_{\mathrm{turb}}$ of the host model
(page-local). Written with the time scale $k/\varepsilon$, that is with the
registry's $\mathsf S_{ij}=(k/\varepsilon)\langle S_{ij}\rangle$ and
$\mathsf W_{ij}=(k/\varepsilon)\langle\Omega_{ij}\rangle$, the first four
tensors and the five invariants are (Eqs. 3–4; the others in the source)

$$T^{(1)}=\mathsf S,\quad T^{(2)}=\mathsf S\mathsf W-\mathsf W\mathsf S,\quad T^{(3)}=\mathsf S^2-\tfrac13\operatorname{tr}(\mathsf S^2)\,\mathbf I,\quad T^{(4)}=\mathsf W^2-\tfrac13\operatorname{tr}(\mathsf W^2)\,\mathbf I,$$

$$I_1=\operatorname{tr}(\mathsf S^2),\quad I_2=\operatorname{tr}(\mathsf W^2),\quad I_3=\operatorname{tr}(\mathsf S^3),\quad I_4=\operatorname{tr}(\mathsf W^2\mathsf S),\quad I_5=\operatorname{tr}(\mathsf W^2\mathsf S^2).$$

Cherroud et al. (2022) use the time scale $1/\omega$ of the
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) host, as in Pope (1975) and
Gatski & Speziale (1993) (§2.1, Eq. 8): page-local
$\mathsf S^\omega_{ij}=\langle S_{ij}\rangle/\omega$ and
$\mathsf W^\omega_{ij}=\langle\Omega_{ij}\rangle/\omega$ replace $\mathsf S$,
$\mathsf W$ in the tensors, and with $\omega=\varepsilon/(\beta^*k)$,
$\mathsf S^\omega=\beta^*\mathsf S$ *(compiler check, not in the sources)*. Sandberg &
Zhao take the time scale from a frozen solution of the $\omega$ or
$\varepsilon$ equation with the reference mean velocity and stresses
(Parneix et al. 1998), so that it is consistent with the transport
equation the model will run with, and recall Weatheritt & Sandberg's
finding, from barycentric maps, that normalizing by this time scale is
inappropriate near walls (§3.2, §4.1).

**Two-dimensional mean flows.** Cherroud et al. recall from Pope (1975)
that in a two-dimensional mean flow only $T^{(1)}$–$T^{(3)}$ are linearly
independent and only $I_1$, $I_2$ are non-zero, so
$b_{ij}=\sum_{n=1}^3g^{(n)}(I_1,I_2)T^{(n)}_{ij}$ (Eq. 7); Sandberg & Zhao use
$T^{(1)}$–$T^{(4)}$ with $I_1$, $I_2$ for statistically two-dimensional flows
(§4.1), as Sandberg & Michelassi (2022) do (see Qualifications).
Cherroud et al. note that the $T^{(1)}$ term is an additive correction of
the eddy viscosity, while $T^{(2)}$ and $T^{(3)}$ are the quadratic terms
of the Gatski–Speziale and Wallin–Johansson models (§2.1).

## Classical EARSMs

The classical coefficients are derived analytically from the
Reynolds-stress transport equations under the weak-equilibrium
assumption (Rodi 1976) and calibrated (Gatski & Speziale 1993; Wallin &
Johansson 2000), and "most formulations" keep only quadratic and cubic
terms (Sandberg & Zhao 2022, §3.2). Extended bases (Kenjereš et al. 2005)
and physics-based input features (Wang et al. 2019) are cited as
generalizations (§3.2).

**The algebraic stress model of 1974.** Launder & Spalding (1974) present the
algebraic stress model, "of recent origin and not yet thoroughly tested",
as an extension of the $k$-$\varepsilon$ model
([Launder & Spalding (1974)](/sources/launder-1974.md), §2.4, Eqs.
2.4-2–2.4-3). Because the modelled dissipation and pressure–strain of the
stress transport equation contain no stress gradients, eliminating
$DR_{ij}/Dt$ and the diffusion $\mathcal D_{ij}$ leaves algebraic relations
$R_{ij}=f\big(R_{pq},k,\varepsilon,\partial_m\langle u_l\rangle\big)$ (Eq.
2.4-3; see the [Reynolds-stress model](/methods/reynolds-stress-model.md)
for the transport equation). Launder (as cited) neglected convection and
diffusion; Rodi (as cited) took the convection of $R_{ij}$ proportional to
$(Dk/Dt)R_{ij}/k$, and likewise for diffusion; the authors find the two
give only small differences in practice. $k$ and
$\varepsilon$ come from the $k$-$\varepsilon$ equations, optionally with the
production computed from the algebraic stresses. As printed, the relation
gives the stresses implicitly, with $R_{pq}$ on both sides of Eq. 2.4-3. The
model predicts the secondary flow of fully developed square-duct flow and
its effect on the axial-velocity contours, where the isotropic
$k$-$\varepsilon$ viscosity gives no cross-plane motion (Tatchell's
computation, as cited; §3.9, Fig. 3.9; see the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)).

**BSL-EARSM.** Menter et al. (2012) combine the Wallin–Johansson
stress–strain relation with the transport equations of the SST model to
reduce free-stream sensitivity; Cherroud et al. (2022) run it in
[OpenFOAM](/software/openfoam.md) on three separated flows (periodic hill
$Re=10\,595$, converging–diverging channel $Re=12\,600$, curved
backward-facing step $Re=13\,700$), and their learned single-term models,
"almost as robust and cheap as SST", perform significantly better (App.
C, Figs. C.9–C.11). Other uses of EARSMs in the bundle are reference
runs: the drag of the [Ahmed body](/benchmarks/ahmed-body.md) and the DG
RANS of the [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md) (see those
pages). On the 35° Ahmed body, the RANS-EARSM of Guilmineau et al. quoted by
[Wang et al. (2024d)](/sources/wang-2024-k.md) gives a total drag
coefficient of 0.437 against 0.279 measured, the largest of the listed
simulations (IDDES 0.346, DES 0.316, RANS 0.300; Table I, as cited).

**Naming and classification.** [Luckring & Rizzi (2024)](/sources/luckring-2024.md)
class the algebraic Reynolds-stress model with the second-moment closures,
not with the eddy-viscosity ("first-order") models, and state that ARSM,
EARSM and EASM "all refer to the same thing", existing in "various versions
… in two-equation form" (§2.4.1, footnote 5); the differential form is on
the [Reynolds-stress model](/methods/reynolds-stress-model.md) page. As an
example of RANS against DNS they cite an EARSM computation of the
[NACA 4412](/benchmarks/naca-4412-airfoil.md) in the EDGE code whose mean
velocity correlates with the DNS of Hosseini et al. at $Re_c=4\times10^5$,
$\alpha=5^\circ$ (§2.4.1.1, Fig. 43, as cited).

**The quadratic commutator term in a shock interaction (a priori).**
[Yu et al. (2023b)](/sources/yu-2023-b.md) (§IV, Eqs. 17–19, Fig. 17)
test the Boussinesq relation and one quadratic extension on DNS of Mach 5
oblique-shock/boundary-layer interactions (wedge angles $14^\circ$,
$10^\circ$, $6^\circ$). With the Favre-averaged traceless strain
$S^d_{ij}$ and rotation $\Omega_{ij}$, the density-weighted Reynolds stress
$R_{ij}=\langle\rho u_i''u_j''\rangle$ and page-local coefficients $\mu_t$,
$\mu_{t2}$, the extension reads

$$-\big(R_{ij}-\tfrac13R_{kk}\delta_{ij}\big)=2\mu_tS^d_{ij}+\mu_{t2}\big(S^d_{ik}\Omega_{kj}-\Omega_{ik}S^d_{kj}\big),$$

whose second term has the structure of $T^{(2)}$ without the time-scale
normalization; the authors take the form from Gatski & Speziale, Craft et
al. and Jongen & Gatski, as they cite them. The best-fit linear eddy
viscosity (least-squares projection of the DNS stress on $S^d_{ij}$)
reconstructs $-R_{12}$ well upstream and downstream but "severely"
over-predicts it in the interaction zone, especially along the rising
shear layer, where stress and strain are not aligned; with $\mu_{t2}$
calibrated to the residual of the linear fit, the reconstructed stress
collapses onto the DNS. The authors justify one extra term by the
traceless stress having two effective independent components in the
two-dimensional mean flow. The test is a priori only: their RANS (§V)
keeps the linear [$k$-$\omega$ SST](/methods/k-omega-sst-model.md), which
remains inaccurate inside the interaction zone, and they state that a
nonlinear term would be needed there but not if only wall quantities
matter (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
and [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

## Learned EARSMs

In the learned forms the $g^{(n)}$ become functions found by regression,
either a priori on frozen high-fidelity fields or in the loop with the solver.
The [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
is the neural counterpart; the symbolic forms are on the
[symbolic-regression closures](/methods/symbolic-regression-closure.md)
page.

### Gene-expression programming

Sandberg & Zhao (2022, §4.1) review the gene-expression-programming (GEP)
EARSMs of their group, all on $T^{(1)}$–$T^{(4)}$ for 2-D flows:

- trained on a backward-facing step, a model using the first four basis
  tensors and two invariants gave "excellent" a posteriori predictions of
  the [periodic hill](/benchmarks/periodic-hill.md); some individuals of
  the population had very large coefficients, non-realizable stresses and
  unstable runs, which the symbolic form makes easy to remove by
  inspection but not robustly automatically;
- CFD-driven training (each candidate run in RANS and scored on the mean
  flow, Zhao et al. 2020) for high- and low-pressure-turbine wake mixing
  gave simpler models than frozen training and improved the wake profiles
  in all a posteriori tests on other geometries, "predominantly due to
  increasing the amount of diffusion" (see
  [turbine cascades](/benchmarks/turbine-cascade.md) and
  [model-consistent training](/methods/model-consistent-training.md));
- on jets in crossflow (trained on an inline jet, tested a priori on a
  skewed one) GEP and a TBNN both improved greatly on the linear baseline
  but missed the anisotropy where the streamwise vorticity is strongest;
- on a junction flow (Weatheritt & Sandberg 2019) recursive feature
  elimination reduced the number of basis tensors and the cost included
  the divergence of the stress; the a priori error fell strongly but the
  a posteriori velocity improved only marginally;
- for flows with periodic unsteadiness the training data are phase-locked
  or triple-decomposed, as the [spectral gap](/definitions/spectral-gap.md)
  allows (§4.4).

Sandberg & Michelassi (2022) describe the phase-locked GEP model of
Akolekar et al. (2019) with $T^{(1)}$–$T^{(4)}$ (Eq. 2): good on its training
phase, poor on some others, with two models sufficient over the
wake-passing cycle ([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md),
§4.3, Fig. 7).

### Sparse regression with a production correction

The SpaRTA approach of Schmelzer et al. (2020), which both sources cite,
regresses a library of candidate functions with sparsity
promotion and adds a second learned term: a correction $R$ of the
production in the $k$- and $\omega$-equations, itself expanded on the basis
(Sandberg & Zhao 2022, §3.4, Eq. 8; Cherroud et al. 2022, §2.1, Eqs.
12–13). In Cherroud et al.'s notation (registry §11; tensors and
invariants built from $\mathsf S^\omega$, $\mathsf W^\omega$),

$$b_{ij}=b^0_{ij}+b^\Delta_{ij},\qquad b^0_{ij}=-\frac{\nu_t}{k}\langle S_{ij}\rangle,\qquad
R=2k\,b^R_{ij}\,\partial_j\langle u_i\rangle,\qquad b^{\Delta}_{ij},\,b^R_{ij}=\sum_{n=1}^{3}g^{\Delta,R}_n(I_1,I_2)\,T^{(n)}_{ij},$$

with $g^{\Delta}_n$, $g^R_n$ page-local (the source's $\alpha^\Delta_n$,
$\alpha^R_n$); Sandberg & Zhao write $R=k\,a^R_{ij}\partial_j\langle u_i\rangle$ with
$a^R_{ij}$ on all ten tensors. The targets come from the
"$k$-corrective-frozen" procedure: the SST $k$- and $\omega$-equations are
solved with the high-fidelity mean velocity, $k$ and $b^\Delta$ frozen,
giving $\omega$ and the residual $R$ that makes the frozen $k$-equation
consistent, with the production limited to $10\beta^*\omega k$ (Cherroud et
al., §2.1, Eqs. 9–11). Correcting the eddy viscosity and time scale
through the transport equations favours models consistent with the
solver and reduces the error propagation of ill-conditioned explicit
injection (§2.1).

**SBL-SpaRTA.** Cherroud et al. (2022) replace the deterministic
regression and re-fit of SpaRTA by sparse Bayesian learning (relevance
vectors with a demi-Bayesian LASSO hyper-prior of sparsity parameter
$\lambda$), so that term selection and coefficient posteriors come in one
step (§3, Eqs. 16–27). Each coefficient function is drawn from 25
monomials of $I_1$, $I_2$ per tensor, 75 candidates per target and 150 in
all (Eq. 14). $\lambda\in\{10^2,10^3,10^4,10^5,2\times10^5\}$ is chosen a
posteriori: the posterior-mean models are run in OpenFOAM and scored by
the mean-square errors of velocity, $k$, shear stress and $C_f$ relative to
SST, in leave-one-out scenarios over the three flows (§3–4, Eqs. 29–32).

- Increasing $\lambda$ sparsifies $b^\Delta$; $b^R$ reduces to one $T^{(1)}$
  term whatever $\lambda$, its coefficient falling with $\lambda$, and above
  $2\times10^5$ both vanish (§4.2, App. A).
- The selected models, all at $\lambda=2\times10^5$, have $b^\Delta=0$ and
  $b^R=g^R_1T^{(1)}$ with $g^R_1=0.8433\pm0.0142$, $0.382\pm0.0184$ and
  $0.197\pm0.0156$ for the three training scenarios (Eqs. A.13–A.15),
  against the deterministic SpaRTA models $0.39\,T^{(1)}$; $b^\Delta=0.1\,T^{(1)}+4.09\,T^{(2)}$
  with $1.39\,T^{(1)}$; and $0.93\,T^{(1)}$ (App. B). Average improvement
  scores are 6.0%, 28% and 31% (Table 2).
- Cross-validated on velocity alone, models with non-zero $b^\Delta$ win,
  which the authors attribute to representing the stress by the mean
  velocity gradient only (Table 2, §4.2).
- The posteriors, propagated by second-order Hermite polynomial chaos
  (three CFD runs per one-coefficient model), give $\pm3\sigma$ bands that
  widen where the prediction departs from LES; velocity and $C_f$ improve
  over SST, $k$ is overpredicted in separated regions, and the small
  separation of the converging–diverging channel is not located (§4.2,
  Figs. 5–7).

The authors read the result as showing that, for these 2-D separated
flows, a tuned eddy viscosity through the production correction is
generally sufficient, which they contrast with the 3-D wall-mounted cube
of Huijing et al. (2021), where non-linear terms matter (§5); Sandberg &
Zhao quote that 3-D study as needing "both a non-linear anisotropy model
and a production correction" (§4.1). See
[model-form uncertainty](/definitions/model-form-uncertainty.md) for the
uncertainty bands.

## Explicit algebraic heat-flux models

Sandberg & Zhao (2022, §3.3, §4.2) review the analogous expansion of the
turbulent heat flux, with $T'$ the temperature fluctuation and $\langle T\rangle$
the mean temperature (page-local), after Younis et al. (2005): the flux is
$\sqrt k$ times a sum of tensors (built from the scaled strain and
rotation and the
normalized stress) applied to a normalized temperature gradient, with
coefficients depending on the $I_m$ and on eleven invariants that
contain the temperature gradient (Eqs. 6–7). Special cases:

- **gradient diffusion (GDH)**, only the first coefficient, equal to
  $1/Pr_t$: $-\langle u_i'T'\rangle=(\nu_t/Pr_t)\,\partial_i\langle T\rangle$ (Eq. 9);
- **generalized gradient diffusion (GGDH, Daly & Harlow)**, a flux along
  $R_{ij}\partial_j\langle T\rangle$ divided by a turbulence frequency (Eq. 12);
- **higher-order GGDH (Abe & Suga)**, along $R_{ik}R_{kj}\partial_j\langle T\rangle$
  divided by $k$ and a frequency (Eq. 13).

Yu et al. (2023b, §IV, Eqs. 22–26, Fig. 20) test a priori on their Mach 5
shock-interaction DNS three one-term nonlinear additions to gradient
diffusion, $\langle u_i'T'\rangle=-\kappa_t\partial_i\langle T\rangle-\kappa_{t2}\,\mathsf M_{ik}\partial_k\langle T\rangle$
(page-local diffusivities $\kappa_t$, $\kappa_{t2}$; the paper writes
Reynolds fluctuations and means for the heat flux), with the tensor
$\mathsf M_{ik}$ (page-local) the mean velocity gradient
$\partial_k\langle u_i\rangle$ (Eq. 24), the strain $S^d_{ik}$ (Eq. 25) or
the rotation $\Omega_{ik}$ (Eq. 26). Gradient diffusion alone
reconstructs the wall-normal flux except in the interaction zone; the
velocity-gradient term makes it worse, the strain term gives a minor
gain, and the rotation term "works much better". The authors cite Gatski &
Speziale, So et al. and Wang et al. for such forms and caution that
shock-motion-induced fluctuations should not be modelled with the
turbulent ones. Their RANS keeps gradient diffusion with a
pressure-gradient-dependent $Pr_t$ (see
[turbulent Prandtl number](/definitions/turbulent-prandtl-number.md)).

Learned heat-flux closures cited in the review: random forests on the
invariants plus wall-distance Reynolds number and $\nu_t/\nu$ (Milani et
al. 2018, 2019, the invariants carrying about 55% of feature importance);
frame-invariant deep networks (Milani et al. 2021); GEP for a spatially
varying $1/Pr_t$, which gave mean $Pr_t$ of 0.42–0.6 on trailing-edge slots
against the "typical" 0.85–0.9 (Haghiri & Sandberg 2020); CFD-driven GEP with
wall temperature in the cost, mean $Pr_t=0.32$ (Lav et al. 2021); and a
GEP model on the GGDH, HoGGDH and a mixed stress–strain term after
recursive feature elimination ranked those tensors first, beating
eddy-diffusivity models a posteriori on a jet in crossflow (Weatheritt et
al. 2020; Eq. 14) (§4.2). Including the temperature gradient in the
invariants violates the linearity principle for a passive scalar, which
the reviewers accept because temperature in compressible turbulence is
not strictly passive (§3.3). Multi-expression, multi-objective
CFD-driven training of a stress and a heat-flux closure together, with a
Pareto front over velocity and temperature errors, improved both in
vertical natural convection over separately trained models (Waschkowski
et al. 2022; §4.5, Eq. 17).

## Qualifications

- Sandberg & Zhao (2022) define the stress as
  $-\langle\rho\rangle\langle u_i''u_j''\rangle$ and print Eqs. 1–2 in the form of
  the positive-trace stress; the form above uses the registry convention
  (see the [Boussinesq](/definitions/boussinesq-hypothesis.md) page).
- Sandberg & Zhao print $I_2=\mathsf W_{mn}\mathsf W_{nm}$ (their scaled
  rotation, lower-case $w$ in the source), that is $\operatorname{tr}(\mathsf W^2)\le0$; Cherroud et al. print
  $I_2=\Omega^*_{mn}\Omega^*_{mn}$, that is
  $\mathsf W^\omega_{mn}\mathsf W^\omega_{mn}\ge0$: the same invariant with
  opposite sign (and a different time scale), so learned
  coefficient functions of $I_2$ are not interchangeable between the two
  conventions *(compiler check, not in the sources)*.
- Cherroud et al. (§2.1, after Pope 1975) state that only
  $T^{(1)}$–$T^{(3)}$ are linearly independent in a 2-D mean flow; Sandberg
  & Zhao and Sandberg & Michelassi use $T^{(1)}$–$T^{(4)}$ for 2-D flows. By
  the statement Cherroud et al. print, the fourth tensor is then a
  combination of the others *(compiler check, not in the sources)*;
  neither Sandberg paper discusses this.
- Cherroud et al. print the limited production of their frozen
  $k$-equation as $\min\big(2k(-\tfrac{\nu_t}{k}\langle S_{ij}\rangle+b^{\Delta}_{ij})\partial_j\langle u_i\rangle,\,10\beta^*\omega k\big)$
  (Eq. 11). With their stress $R_{ij}=2k(\tfrac13\delta_{ij}+b^0_{ij}+b^\Delta_{ij})$
  entering the momentum equation as $-\partial_jR_{ij}$ (Eq. 2), the
  production is $-R_{ij}\partial_j\langle u_i\rangle=2k(\tfrac{\nu_t}{k}\langle S_{ij}\rangle-b^\Delta_{ij})\partial_j\langle u_i\rangle$,
  the opposite sign *(compiler check, not in the sources)*; $R$ (Eq. 12)
  follows the printed convention, so the sign of the $g^R_1$ values
  relative to $\nu_t$ depends on it.
- Cherroud et al. print the noise standard deviation of the $\lambda=10^4$
  production model of scenario 3 as 0.358 (Eq. A.9), against 0.0358–0.0364
  for the same scenario at the other $\lambda$ (Eqs. A.3, A.6, A.12, A.15).
- Sandberg & Zhao print GGDH and HoGGDH (Eqs. 12–13) with $\tau_{ij}$, which
  after Eq. 6 is defined as the dimensionless $\langle u_i'u_j'\rangle/2k$;
  with that meaning neither printed form has the dimensions of a heat
  flux, and both do with the dimensional stress, which the list above
  uses; their middle and right-hand expressions agree only if the
  frequency is $\varepsilon/k$ rather than $\omega=\varepsilon/(\beta^*k)$
  *(compiler check, not in the sources)*. Their Eq. 7 prints the same
  tensor for the invariants $J_1$ and $J_4$, and "$C_{GDDH}$" for $C_{GGDH}$.

# Citations

- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.2 Eqs. 1–4, §3.3 Eqs. 5–7, §3.4 Eq. 8, §4.1, §4.2 Eqs. 9–15, §4.4, §4.5 Eq. 17.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §1, §2.1 Eqs. 2–13, §2.2 Eq. 14, §3 Eqs. 16–32, §4.2 Table 2 Figs. 1–7, §5, Apps. A–C.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §4.3, Eq. 2, Fig. 7.
- [Yu et al. (2023b)](/sources/yu-2023-b.md) — §IV, Eqs. 17–19, Fig. 17 (a priori quadratic commutator term in a Mach 5 shock interaction); Eqs. 22–26, Fig. 20 (nonlinear heat-flux terms); §V (linear SST kept in RANS).
- [Wang et al. (2024d)](/sources/wang-2024-k.md) — Table I (Ahmed-body drag of a cited RANS-EARSM).
- [Launder & Spalding (1974)](/sources/launder-1974.md) — §2.4, Eqs. 2.4-2–2.4-3 (implicit algebraic stress model of Launder and Rodi, as cited), §3.9, Fig. 3.9 (square-duct secondary flow).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §2.4.1 and footnote 5 (ARSM = EARSM = EASM, classification with second-moment closures); §2.4.1.1, Fig. 43 (EDGE EARSM against NACA 4412 DNS, as cited).
