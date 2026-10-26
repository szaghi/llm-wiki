---
type: Method
title: "Tensor-basis neural network and the integrity basis"
description: "A neural network that predicts the scalar coefficients of Pope's ten-tensor integrity basis from invariants of the mean strain and rotation, so the learned Reynolds-stress anisotropy is objective by construction; random forests, gene-expression programming, sparse and deep symbolic regression learn the same expansion, and larger integrity bases supply invariant input features."
status: established
aliases: [TBNN, tensor basis neural network, integrity basis, Pope tensor basis, general effective-viscosity hypothesis, minimal integrity basis, invariant input features]
tags: [neural-network, machine-learning, rans, data-driven, symbolic-regression]
timestamp: 2026-10-26T07:37:00Z
---

# Tensor-basis neural network and the integrity basis

The **integrity basis** of Pope (1975) writes the normalized Reynolds-stress
anisotropy as a finite sum of ten tensors $T^{(n)}_{ij}$ formed from the
mean strain-rate and rotation-rate tensors, with scalar coefficients
$g^{(n)}$:

$$b_{ij}=\sum_{n=1}^{10}g^{(n)}\,T^{(n)}_{ij},\qquad R_{ij}=2k\left(\tfrac13\delta_{ij}+b_{ij}\right).$$

When the Reynolds stress depends only on the local mean velocity gradient,
the Cayley–Hamilton theorem makes such a basis exact. This is recalled by
Duraisamy et al. (2019, §2 L2) as an L2-level representation (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
for the layers). The **tensor-basis neural network** (TBNN) of Ling,
Kurzawski & Templeton (2016) keeps the basis. A neural network predicts the
coefficients $g^{(n)}(\boldsymbol\zeta;\boldsymbol\theta)$ from invariants
$\boldsymbol\zeta$ of the strain and rotation tensors, and the result is a
learned [nonlinear eddy-viscosity](/definitions/boussinesq-hypothesis.md)
closure that is objective by construction (Duraisamy 2021, §III.A, Eq. 4;
Duraisamy et al. 2019, §5.3, Eqs. 11–12).

## Construction

As recalled by Duraisamy (2021, §III.A, Eq. 4), the TBNN closure is, in
registry notation,

$$R_{ij}=2k\left(\tfrac13\delta_{ij}+\sum_{n=1}^{10}g^{(n)}(\boldsymbol\zeta;\boldsymbol\theta)\,T^{(n)}_{ij}\right).$$

Its parts are:

- **Basis.** The ten tensors $T^{(n)}_{ij}$ are built from the mean
  strain-rate and rotation-rate tensors of the RANS solution.
- **Features.** $\boldsymbol\zeta$ holds five invariants of those two
  tensors, which Duraisamy calls "objective by definition".
- **Output.** The network returns only the ten scalar coefficients. The
  tensorial structure, and with it rotational invariance, comes from the
  basis and not from the network.
- **Scales.** $k$ is the model's own turbulent kinetic energy.

The sources print neither the individual tensors nor the normalization of
the strain and rotation inside them; they refer to Pope (1975). Duraisamy
(2021, Table I, §V) gives the strain-rate tensor times $k/\varepsilon$ as an
example of the local non-dimensionalization of RANS features.

**Extensions.** As recalled by Duraisamy (2021, §III.A), the TBNN idea has
been extended to turbulent heat fluxes and scalar fluxes.

## Other regressors on the same basis

The integrity basis is the common skeleton of several learned RANS closures
surveyed in both reviews. They differ in how the coefficients $g^{(n)}$
are represented.

| Regressor | Representation of $g^{(n)}$ | Recalled by |
|---|---|---|
| neural network (TBNN, Ling et al. 2016) | network of the invariants; no explicit expression | Duraisamy et al. (2019, §5.3); Duraisamy (2021, §III.A) |
| random forests (Kaandorp & Dwight) | tree ensemble on the same basis | Duraisamy (2021, §III.A) |
| gene-expression programming (Weatheritt & Sandberg 2016, 2017) | explicit algebraic expressions in the invariants | Duraisamy et al. (2019, §5.3); Duraisamy (2021, §III.A) |
| sparse regression, SpaRTA (Schmelzer et al.) | sparse linear combination of tensor-polynomial candidate functions of the invariants | Duraisamy (2021, §III.A, §IV.A) |
| deep symbolic regression (an LSTM expression generator trained by a risk-seeking policy gradient) | explicit polynomial-type expressions in two normalized invariants, on the 2D three-tensor basis | read directly: Tang et al. (2023) |

For sparse regression, Duraisamy (2021, §IV.A) prints the loss as a squared
error plus an $\ell_1$ penalty on the weights. The sparsity-enforcing
regularizer eliminates model terms and so simplifies the model form
(§III.A). As recalled there, Beetham et al. extend the approach to
multiphase RANS (drag production, drag exchange, pressure strain, viscous
dissipation).

## The two-dimensional basis and the linear/non-linear split (Tang et al. 2023)

[Tang et al. (2023)](/sources/tang-2023.md) (arXiv v1, §II C 2) print
the reduced basis that Pope (1975) gives for statistically
two-dimensional flow, as recalled there: the coefficients depend on at
most two invariants and three tensors suffice. With the mean strain and
rotation made dimensionless by $k/\varepsilon$,
$\mathsf S_{ij}=\tfrac{k}{\varepsilon}\langle S_{ij}\rangle$ and
$\mathsf W_{ij}=\tfrac{k}{\varepsilon}\langle\Omega_{ij}\rangle$
(page-local, as on [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md);
the paper's $\boldsymbol S$, $\boldsymbol R$, Eq. 11, whose sign
convention for $\nabla\boldsymbol u$ is not stated),

$$T^{(1)}_{ij}=\mathsf S_{ij},\qquad T^{(2)}_{ij}=\mathsf S_{ik}\mathsf W_{kj}-\mathsf W_{ik}\mathsf S_{kj},\qquad T^{(3)}_{ij}=\mathsf S_{ik}\mathsf S_{kj}-\tfrac13\delta_{ij}\mathsf S_{kl}\mathsf S_{lk},$$

with invariants $I_1=\mathsf S_{ij}\mathsf S_{ji}$ and
$I_2=\mathsf W_{ij}\mathsf W_{ji}$ (page-local; Eqs. 13–14).

**Convention.** The paper's anisotropy is $R_{ij}/k-\tfrac23\delta_{ij}$
(Eq. 10), twice the registry $b_{ij}$. In registry form its split (Eqs.
15–16, 19) reads

$$b_{ij}=-C_\mu\mathsf S_{ij}+b^\perp_{ij},\qquad b^\perp_{ij}=0.35\sum_{m=1}^{3}G^m(I_1,I_2)\,T^{(m)}_{ij},$$

with $b^\perp_{ij}$ the non-linear part (page-local) and $G^m$ the
paper's coefficients. The paper prints the linear part as
$-2C_\mu\boldsymbol S$ and the prefactor of the sum as $\beta/10=0.7$
(Eq. 19; Eq. 16 omits it); $-C_\mu$ and 0.35 are those factors halved with
the anisotropy *(compiler check, not in the sources)*. The linear part is
the $k$-$\varepsilon$ eddy viscosity with
$C_\mu=0.09$, solved implicitly; only $b^\perp_{ij}$ is learned (§II C 2).
The authors call this split "necessary": injecting the whole learned
Reynolds stress explicitly is ill-conditioned and magnifies small errors
in the RANS iterations (as recalled from their refs. 19, 46, 47; see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)).

**Regressor.** The coefficients $G^m$ are found by deep symbolic
regression as explicit expressions, so Galilean and rotational invariance
hold by construction and the model runs in a RANS code "without the need
to deploy a deep learning environment" (§I, §IV). The learned expressions,
the realizability factor and the results are on
[symbolic-regression closures](/methods/symbolic-regression-closure.md).
A contribution analysis on the training hill finds the linear part and
$T^{(1)}$ dominating the shear component of the anisotropy, $T^{(2)}$ the
largest contributor to the streamwise normal component and $T^{(3)}$ to
the spanwise one (§III C, Fig. 11).

## Integrity bases as sources of invariant features

An integrity basis can also serve the input side of a learned closure. Its
invariants are rotationally invariant scalars that a network can take as
features, whatever it outputs.
[McConkey et al. (2022)](/sources/mcconkey-2022.md) follow the procedure of
Wu et al. (as recalled there, §III C) and build the Spencer–Rivlin minimal
integrity basis of four tensors:

- the mean strain-rate tensor $S_{ij}$ and rotation-rate tensor
  $\Omega_{ij}$;
- an antisymmetric tensor built from $\nabla k$;
- an antisymmetric tensor built from the gradient of the wall-normal stress
  variable of their $v^2$-$f$-type base model.

The last one replaces the pressure-gradient tensor of Wu et al., whose terms
were "numerically unstable in our experience" (§III C). The result is 47
basis tensors (page-local $\mathcal B_1,\dots,\mathcal B_{47}$, a different
object from Pope's $T^{(n)}$). Their first and second invariants,
$I_1(\mathcal B)=\mathrm{tr}\,\mathcal B$ and
$I_2(\mathcal B)=\tfrac12[(\mathrm{tr}\,\mathcal B)^2-\mathrm{tr}(\mathcal B^2)]$
(page-local), are the candidate features.

**Two-dimensional reduction.** In 2D incompressible flow many of these
invariants vanish identically, directly or through continuity, and all
third invariants vanish because each of the four base tensors has zero
determinant. A symbolic evaluation (Maple) leaves 29 non-zero first and
second invariants, which the authors call "an outcome not previously
discussed in detail" (§III C, App. A, Table II). With three heuristic
scalars and the base model's normalized wall-normal stress, the network
receives 33 Galilean-invariant features, "one of the richest feature sets
used in a data-driven turbulence closure model" (§III C, Table I). In a
three-dimensional flow, adding the second invariants doubles the count from
47 to 94 (§III C, §V).

**Outputs without a tensor basis.** The outputs of McConkey et al. are not
basis coefficients. One network predicts a non-negative optimal eddy
viscosity, the other the three independent components of the remaining
non-linear part of the anisotropy (§III B; see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). Because
those components are predicted directly, the authors state that this part
"is not invariant under coordinate transformations", and propose a
tensor-basis neural network for it as future work (§V).

**Feature importance.** By a SHAP analysis of the eddy-viscosity network,
the base model's normalized wall-normal stress is the most important
feature. Among the invariants, the first invariants of
$\mathcal B_9=\mathcal A^2S$ and $\mathcal B_7=\Omega^2S^2$ rank second and
third, where $\mathcal A$ (page-local) is the antisymmetric tensor of the
wall-normal-stress gradient. For $\mathcal B_7$ the second invariant ranks
only twenty-fifth, while for $\mathcal B_5$ (the square of the
antisymmetric tensor of $\nabla k$) the second invariant ranks much higher
than the first (§IV C, Fig. 22). The paper's Table II defines the basis
tensors.

**Dataset and training.** The training data are the authors' curated
dataset (McConkey et al. 2021, as recalled in §III D). Its periodic-hill
part pairs RANS fields of the base model with DNS of Xiao et al. for five
hill-steepness factors 0.5, 0.8, 1.0, 1.2 and 1.5 of the parametrized
[periodic hill](/benchmarks/periodic-hill.md) family at $Re_h=5600$, with
14,751 points per case. The factor 1.2 is held out for testing, an
interpolation within the family, and the other four are used with 4-fold
cross-validation by geometry (§III D–E). Both networks have 14 hidden
layers of 30 SELU neurons; the eddy-viscosity network ends in an
exponential activation that makes its output non-negative (§III B). The
a priori and a posteriori results are on
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

## Assessment in the sources

- **Interpretability.** Duraisamy et al. (2019, §5.3) note that the TBNN
  gives "no explicit expression for the resulting model". Gene-expression
  programming gives explicit algebraic stress models. Duraisamy (2021,
  §VII) adds that interpretable models from symbolic regression do not
  automatically generalize beyond their training scenarios.
- **Generalization.** As recalled by Duraisamy et al. (2019, §5.3),
  gene-expression-programming models trained on low-Reynolds-number DNS of
  a backward-facing step and used at high Reynolds number show "a high
  level of uncertainty" on the [periodic hill](/benchmarks/periodic-hill.md).
- **Training.** In the TBNN as surveyed, targets and invariants are
  extracted from DNS, i.e. the network is trained a priori. Duraisamy
  (2021, §IV.A) states that such training "establishes the consistency of
  the ML model with the DNS field, but does not guarantee consistency with
  the RANS or LES environment" (see
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
  and [model-consistent training](/methods/model-consistent-training.md)).
- **Tensor basis in an LES closure.** [Kim et al. (2022)](/sources/kim-2022.md)
  (§II E) tried a tensor-basis neural network for rotational invariance in
  their [reinforcement-learning SGS model](/methods/reinforcement-learning-closure.md)
  of channel flow. It "did not conclusively help improve DRL performance,
  presumably due to strong anisotropy of the near-wall turbulence". No
  results are shown. Their actor instead outputs the six SGS stress
  components directly and imposes only reflectional equivariance and a zero
  wall value.
- **Invariance of an LES network without a basis.**
  [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) (§2.1) feed
  their LES closure the full filtered velocity-gradient tensor and output
  the stress components directly; the model is Galilean invariant but not
  rotationally invariant. They name tensor-basis networks and rotationally
  invariant inputs as future work (§7; see
  [neural-network SGS models](/methods/neural-network-sgs-model.md)).
- **Locality.** Existing feature sets use only local quantities.
  Non-local, non-equilibrium features, such as streamline integration
  (Hamlington & Dahm), could extend predictive capability (Duraisamy et al.
  2019, §5.3).

## Relation to perturbation approaches

The integrity basis fixes the representation and learns the coefficients.
Another family keeps the baseline model's stress and learns a discrepancy
in its eigen-decomposition: the eigenvalues, the eigenvectors (orientation,
as Euler angles or unit quaternions) and $k$. Both reviews survey this
family (Duraisamy et al. 2019, §5.2–§5.3; Duraisamy 2021, §III.A). They
describe two ways of obtaining invariance: tensor invariants of the
eigen-decomposition, or the integrity basis itself. See
[model-form uncertainty](/definitions/model-form-uncertainty.md).

## Qualifications

- **Convention difference between the two reviews.** Duraisamy (2021,
  Eq. 4) expands the anisotropy, with the isotropic part
  $\tfrac23k\delta_{ij}$ written separately, as on this page. Duraisamy et
  al. (2019, Eqs. 11–12) print the expansion
  $\boldsymbol\tau=\sum_{n=1}^{10}c^{(n)}\mathbf T^{(n)}$ for the full
  Reynolds stress, with no separate isotropic term. That review does not
  say whether one of the basis tensors is taken as the identity. Neither
  review presents the difference as a disagreement; it is recorded here as
  a difference of writing.
- Duraisamy (2021, §III.A) credits the TBNN to "Ling and Templeton [28]";
  the cited work has three authors (Ling, Kurzawski & Templeton). The same
  paragraph credits a random-forest variant to Kaandorp & Dwight, but the
  reference it gives ([32]) is a duplicate of another entry and not their
  work. The attribution here follows the text.
- McConkey et al. (2022, Table II) print the same expression for different
  basis tensors that are marked differently (zero and non-zero invariants):
  $\mathcal B_{15}$ and $\mathcal B_{16}$, $\mathcal B_{18}$ and
  $\mathcal B_{26}$, $\mathcal B_{19}$ and $\mathcal B_{27}$. Table II marks
  21 tensors with a non-zero first invariant, while Table I and the text use
  20 first invariants (the first invariant of $\mathcal B_{44}$ is absent)
  and 29 invariants in all. The paper does not explain the difference.
- McConkey et al. (2022) write the rotation-rate tensor as $R$ and the
  integrity-basis tensors as $B_n$; this page uses $\Omega_{ij}$ and
  $\mathcal B_n$, because $R_{ij}$ is the Reynolds stress and $B$ the
  log-law intercept in the registry. The version read is arXiv v1.
- Tang et al. (2023) write the coefficients $G^m$ and the basis
  $\boldsymbol T^m$ (labelled $\lambda_i$, $T^i$ in their Fig. 11); this page
  writes $G^m$, $T^{(m)}$. Their $\boldsymbol R$ is the normalized rotation
  tensor, written $\mathsf W_{ij}$ here.

## Contradictions

- **Do sparse-regression closures have invariant-dependent coefficients?**
  Tang et al. (2023, §III B) state that the closures "discovered by some
  other approaches, such as sparse regression and fast function
  extraction, only contain constant coefficients that keep unchanged for
  the whole computational domain", whereas the coefficients of their
  deep-symbolic-regression closure "vary with the invariants at different
  grid points"; they claim "a degree of superiority" from this, with no
  comparison run. Duraisamy (2021, §III.A) describes the sparse regression
  of Schmelzer et al. as acting "on a library of candidate functions which
  are written as tensor polynomials of the aforementioned invariants".
  Both sources recall Schmelzer et al. (2020), which is not ingested (Tang
  et al. also Beetham & Capecelatro); neither prints a sparse-regression
  model. *Open.*

# Citations

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (L2, Cayley–Hamilton), §5.2–§5.3, Eqs. 11–12 (tensor-basis expansion, TBNN, gene-expression programming, features).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A, Eq. 4 (TBNN), random forests, symbolic and sparse regression, §IV.A (a priori training, sparse loss), §V (features), §VII (interpretability).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — arXiv v1: §III B (outputs), §III C, Table I (33 features), App. A, Table II (47-tensor basis, vanishing invariants in 2D), §IV C, Fig. 22 (SHAP), §V (TBNN for the non-linear part, 3D count).
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: §II E (tensor-basis network tried in DRL, no conclusive gain).
- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §I, §II C 2, Eqs. 10–16 (2D basis, convention, linear/non-linear split, conditioning), §III B (claim on constant coefficients), §III C, Fig. 11 (contributions), §IV.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §2.1 (Galilean but not rotational invariance), §7 (tensor-basis networks as future work).
