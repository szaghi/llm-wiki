---
type: Method
title: "Tensor-basis neural network and the integrity basis"
description: "A neural network that predicts the scalar coefficients of Pope's ten-tensor integrity basis from invariants of the mean strain and rotation, so the learned Reynolds-stress anisotropy is objective by construction; random forests, gene-expression programming and sparse regression learn the same expansion."
status: established
aliases: [TBNN, tensor basis neural network, integrity basis, Pope tensor basis, general effective-viscosity hypothesis]
tags: [neural-network, machine-learning, rans, data-driven, symbolic-regression]
timestamp: 2026-10-25T13:43:00Z
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

For sparse regression, Duraisamy (2021, §IV.A) prints the loss as a squared
error plus an $\ell_1$ penalty on the weights. The sparsity-enforcing
regularizer eliminates model terms and so simplifies the model form
(§III.A). As recalled there, Beetham et al. extend the approach to
multiphase RANS (drag production, drag exchange, pressure strain, viscous
dissipation).

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

# Citations

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (L2, Cayley–Hamilton), §5.2–§5.3, Eqs. 11–12 (tensor-basis expansion, TBNN, gene-expression programming, features).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A, Eq. 4 (TBNN), random forests, symbolic and sparse regression, §IV.A (a priori training, sparse loss), §V (features), §VII (interpretability).
