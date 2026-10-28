---
type: Method
title: "Tensor-basis neural network and the integrity basis"
description: "A neural network that predicts the scalar coefficients of Pope's ten-tensor integrity basis from invariants of the mean strain and rotation, so the learned Reynolds-stress anisotropy is objective by construction; other regressors learn the same expansion, larger bases supply invariant features, and eight-term and Lund–Novikov bases carry the idea to LES subgrid stresses and heat fluxes."
status: established
aliases: [Lund–Novikov basis, nonlinear algebraic SGS model, MANA, TBNN, tensor basis neural network, integrity basis, Pope tensor basis, general effective-viscosity hypothesis, minimal integrity basis, invariant input features, LES tensor basis]
tags: [neural-network, data-driven, rans, symbolic-regression]
timestamp: 2026-10-28T01:53:00Z
---

# Tensor-basis neural network and the integrity basis

The **integrity basis** of Pope (1975) writes the normalized Reynolds-stress
anisotropy as a finite sum of ten tensors $T^{(n)}_{ij}$ formed from the
mean strain-rate and rotation-rate tensors, with scalar coefficients
$g^{(n)}$:

$$b_{ij}=\sum_{n=1}^{10}g^{(n)}\,T^{(n)}_{ij},\qquad R_{ij}=2k\left(\tfrac13\delta_{ij}+b_{ij}\right).$$

When the Reynolds stress depends only on the local mean velocity gradient,
the Cayley–Hamilton theorem makes such a basis exact. Duraisamy et al.
(2019, §2 L2) recall this as an L2-level representation (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
for the layers). The **tensor-basis neural network** (TBNN) of Ling,
Kurzawski & Templeton (2016) keeps the basis. A neural network predicts the
coefficients $g^{(n)}(\boldsymbol\zeta;\boldsymbol\theta)$ from invariants
$\boldsymbol\zeta$ of the strain and rotation tensors, and the result is a
learned [nonlinear eddy-viscosity](/definitions/boussinesq-hypothesis.md)
closure that is objective by construction (Duraisamy 2021, §III.A, Eq. 4;
Duraisamy et al. 2019, §5.3, Eqs. 11–12).

## Construction

Duraisamy (2021, §III.A, Eq. 4) writes the TBNN closure as, in registry
notation,

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

The two reviews print neither the individual tensors nor the normalization
of the strain and rotation inside them; they refer to Pope (1975).
Duraisamy (2021, Table I, §V) gives the strain-rate tensor times
$k/\varepsilon$ as an example of the local non-dimensionalization of RANS
features. [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md)
print the full basis (next section).

## The ten tensors and five invariants (Agrawal & Koutsourelakis 2024)

Agrawal & Koutsourelakis (2024, §2.2.1, Eqs. 14–17, Table 1) restate Pope's
basis after Ling et al. With the mean strain and rotation made
dimensionless by $k/\varepsilon$, $\mathsf S_{ij}=\tfrac{k}{\varepsilon}\langle S_{ij}\rangle$
and $\mathsf W_{ij}=\tfrac{k}{\varepsilon}\langle\Omega_{ij}\rangle$
(registry §11; matrix products, $\mathsf I$ the identity), the
tensors are

$$\begin{aligned}
T^{(1)}&=\mathsf S, & T^{(2)}&=\mathsf S\mathsf W-\mathsf W\mathsf S,\\
T^{(3)}&=\mathsf S^2-\tfrac13\operatorname{tr}(\mathsf S^2)\mathsf I, & T^{(4)}&=\mathsf W^2-\tfrac13\operatorname{tr}(\mathsf W^2)\mathsf I,\\
T^{(5)}&=\mathsf W\mathsf S^2-\mathsf S^2\mathsf W, & T^{(6)}&=\mathsf W^2\mathsf S+\mathsf S\mathsf W^2-\tfrac23\operatorname{tr}(\mathsf S\mathsf W^2)\mathsf I,\\
T^{(7)}&=\mathsf W\mathsf S\mathsf W^2+\mathsf W^2\mathsf S\mathsf W, & T^{(8)}&=\mathsf S\mathsf W\mathsf S^2-\mathsf S^2\mathsf W\mathsf S,\\
T^{(9)}&=\mathsf W^2\mathsf S^2+\mathsf S^2\mathsf W^2-\tfrac23\operatorname{tr}(\mathsf S^2\mathsf W^2)\mathsf I, & T^{(10)}&=\mathsf W\mathsf S^2\mathsf W^2-\mathsf W^2\mathsf S^2\mathsf W,
\end{aligned}$$

as printed in Table 1 ($T^{(7)}$: see Qualifications), with the
coefficients functions of the five invariants
$\operatorname{tr}(\mathsf S^2)$, $\operatorname{tr}(\mathsf W^2)$,
$\operatorname{tr}(\mathsf S^3)$, $\operatorname{tr}(\mathsf W^2\mathsf S)$,
$\operatorname{tr}(\mathsf W^2\mathsf S^2)$ (Eq. 16), and
$R_{ij}=2k b_{ij}+\tfrac23k\delta_{ij}$ as in the registry (Eqs. 14, 17).
With $g^{(1)}=-0.09$ and all other coefficients zero the expansion
"degenerates" to the standard $k$-$\varepsilon$ model (§2.2.1); in
registry form $b_{ij}=-C_\mu\mathsf S_{ij}$ with $C_\mu=0.09$, the
Boussinesq closure *(compiler check, not in the sources)*. The authors
state that the linear model restricts the anisotropy to the plane-strain
line of the barycentric map and, citing Kaandorp & Dwight, that the TBNN
can reach other realizable states (§2.2.1). Their $k$ and $\varepsilon$
come from the standard transport equations (App. A).

**A TBNN trained a posteriori.** Unlike the a priori TBNNs surveyed above,
their network (8 hidden layers of 30 nodes, Leaky ReLU, as in Ling et al.;
6970 parameters, Table 3) is trained without any Reynolds-stress data,
from sparse LES mean velocity and pressure through an adjoint RANS solver,
together with a stochastic stress discrepancy (§2.2–2.2.4; see
[model-consistent training](/methods/model-consistent-training.md) and
[model-form uncertainty](/definitions/model-form-uncertainty.md)). A random
initialization "led to divergence of the solution even after applying the
stabilization schemes"; the network was pre-trained on baseline
$k$-$\varepsilon$ closure data with added noise (§3.3). On a
[backward-facing step](/benchmarks/backward-facing-step.md) at step-height
Reynolds number 500 the learned stress "captures the basic features" of
the LES stress although no stress data were used, with the largest errors
at $5<x/h<10$ (§3.4, Fig. 7). The authors also state that, for
prediction, their network needs no baseline RANS fields as input, unlike
the TBNNs of Ling et al., Kaandorp & Dwight, Wang et al. and Geneva &
Zabaras (§2.2.5), and that a direct comparison with those works is not
possible because they blend the predicted stress with the baseline
near-wall stress through case-dependent functions (§3.4).

**Extensions.** Duraisamy (2021, §III.A) cites extensions of the TBNN idea
to turbulent heat fluxes and scalar fluxes.

## The basis in a review of stress and heat-flux learning (Sandberg & Zhao 2022)

[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) (§3.2, Eqs. 2–4)
print the same ten tensors and five invariants, built from the strain
and rotation multiplied by a turbulence time scale (the frozen-$\omega$
time scale of Parneix et al. in the works they review), and split the
expansion into the Boussinesq term, an "additional linear term"
$2k\,g^{(1)}T^{(1)}$ and nine non-linear terms; classic explicit algebraic
models obtain the coefficients analytically under weak equilibrium (see
[explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)).
They recall, citing the original works (§4.1–4.2):

- **Square duct.** A TBNN trained on duct, channel, jets in crossflow, a
  square cylinder and a converging–diverging channel improved the
  anisotropy a priori and the duct corner vortices a posteriori, on a duct
  at another Reynolds number and on a wavy wall (Ling et al. 2016).
- **Jets in crossflow.** A TBNN and a gene-expression model, trained on an
  inline jet and tested a priori on a skewed one, both improved greatly on
  the linear model and both failed where the streamwise vorticity is
  strongest.
- **Near-wall normalization.** Weatheritt & Sandberg (2017) found, with
  barycentric maps, that normalizing the strain and rotation by the time
  scale is inappropriate near walls.
- **Heat flux.** The same construction gives a tensor-diffusivity
  expansion of the turbulent heat flux (Younis et al. 2005), with ten
  basis tensors built from the normalized strain, rotation and Reynolds
  stress and eleven invariants $J_0$–$J_{10}$ that include the temperature
  gradient (Eqs. 6–7); a deep TBNN-type network with embedded frame
  invariance learns its coefficients (Milani et al. 2021). Including the
  temperature gradient in the invariants violates the linearity principle
  for a passive scalar, which the review accepts because temperature in
  compressible flow is not strictly passive (§3.3). A TBNN trained on one
  flow class and tested on another performed about as well as the
  baseline, read by the review as "might not perform as poorly as
  believed" (§4.2.1).

## A data-driven explicit algebraic correction with posteriors (Cherroud et al. 2022)

[Cherroud et al. (2022)](/sources/cherroud-2022.md) (§2.1, Eqs. 5–8) use
the 2-D form, $T^{(1)}$–$T^{(3)}$ with the strain and rotation divided by
$\omega$ and the two invariants $I_1$, $I_2$ (page-local: the squared
norms of these normalized tensors, $I_2$ written without a minus sign),
for an additive correction $b^\Delta_{ij}$ of the SST anisotropy and a
production correction $b^R_{ij}$ (registry §11). They place the $T^{(1)}$
term as an additive correction of $\nu_t$ and the $T^{(2)}$, $T^{(3)}$
terms as the quadratic terms of the Gatski–Speziale and Wallin–Johansson
explicit algebraic models, and contrast the "black-box" TBNN with their
"open-box" sparse Bayesian expressions (§1). Their results are on
[symbolic-regression closures](/methods/symbolic-regression-closure.md).

## Other regressors on the same basis

The integrity basis is the common skeleton of several learned RANS closures
surveyed in both reviews. They differ in how the coefficients $g^{(n)}$
are represented.

| Regressor | Representation of $g^{(n)}$ | Cited in |
|---|---|---|
| neural network (TBNN, Ling et al. 2016) | network of the invariants; no explicit expression | Duraisamy et al. (2019, §5.3); Duraisamy (2021, §III.A); Sandberg & Zhao (2022, §4.1); He et al. (2022, §1); Cherroud et al. (2022, §1) |
| random forests (Kaandorp & Dwight) | tree ensemble on the same basis | Duraisamy (2021, §III.A) |
| gene-expression programming (Weatheritt & Sandberg 2016, 2017) | explicit algebraic expressions in the invariants | Duraisamy et al. (2019, §5.3); Duraisamy (2021, §III.A); Sandberg & Zhao (2022, §4.1) |
| sparse regression, SpaRTA (Schmelzer et al.) | sparse linear combination of tensor-polynomial candidate functions of the invariants | Duraisamy (2021, §III.A, §IV.A); Sandberg & Zhao (2022, §3.4, Eq. 8); Cherroud et al. (2022, App. B, which print three SpaRTA models) |
| deep symbolic regression (an LSTM expression generator trained by a risk-seeking policy gradient) | explicit polynomial-type expressions in two normalized invariants, on the 2D three-tensor basis | read directly: Tang et al. (2023) |
| gene-expression programming for the LES subgrid stress | constant coefficients of $T^{(1)}$–$T^{(4)}$ of the $\lvert\bar S\rvert$-normalized basis | read directly: Li et al. (2021) |
| neural network for the compressible LES stress and heat flux (Xu et al. 2023) | network of four (heat flux: six) invariants and a local Reynolds number, on the Lund–Novikov five-tensor basis plus four trace terms and a four-vector heat-flux basis | read directly: Xu et al. (2023) |
| gene-expression programming on phase-locked turbine data (Akolekar et al. 2019) | functions of two invariants on four basis tensors | Sandberg & Michelassi (2022, §4.3, Eq. 2) |
| sparse Bayesian regression, SBL-SpaRTA (Cherroud et al. 2022) | sparse selection from monomials of $I_1$, $I_2$ with Gaussian posteriors, on the 2D three-tensor basis normalized by $\omega$; used for an additive anisotropy and a $k$-equation correction of SST | read directly: Cherroud et al. (2022); used by Oulghelou et al. (2025) |

For sparse regression, Duraisamy (2021, §IV.A) prints the loss as a squared
error plus an $\ell_1$ penalty on the weights. The sparsity-enforcing
regularizer eliminates model terms and so simplifies the model form
(§III.A). The review cites Beetham et al., who extend the approach to
multiphase RANS (drag production, drag exchange, pressure strain, viscous
dissipation).

## The two-dimensional basis and the linear/non-linear split (Tang et al. 2023)

[Tang et al. (2023)](/sources/tang-2023.md) (arXiv v1, §II C 2) print,
citing Pope (1975), the reduced basis for statistically two-dimensional
flow: the coefficients depend on at most two invariants and three tensors
suffice. With the mean strain and
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
in the RANS iterations (citing their refs. 19, 46, 47; see
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

## Pope's basis for the subgrid stress, regressed by GEP (Li et al. 2021)

[Li et al. (2021)](/sources/li-2021.md) (§II B, Eqs. 9–14) carry Pope's
ten-tensor basis, "following Pope" via Schoepplein et al. (2018) as cited,
to the deviatoric LES subgrid stress of isotropic turbulence, with the
coefficients found by gene-expression programming instead of a network
(the search and the model are on
[symbolic-regression closures](/methods/symbolic-regression-closure.md)).
The scales are the filter width and the resolved strain magnitude instead
of $k/\varepsilon$:

$$\tau^d_{ij}=\frac{\Delta^2\lvert\bar S\rvert^2}{2}\sum_{n=1}^{10}g^{(n)}(I_1,\dots,I_4)\,T^{(n)}_{ij}(\mathsf s,\mathsf w),\qquad \mathsf s_{ij}=\frac{\sqrt2\,\bar S_{ij}}{\lvert\bar S\rvert},\quad \mathsf w_{ij}=\frac{\sqrt2\,\bar\Omega_{ij}}{\lvert\bar S\rvert},$$

with $\mathsf s$, $\mathsf w$ as in registry §11 and the ten tensors those of the
Agrawal & Koutsourelakis section above with $\mathsf S\to\mathsf s$, $\mathsf W\to\mathsf w$.
The paper normalizes by $\sqrt{\bar S_{mn}\bar S_{mn}}=\lvert\bar S\rvert/\sqrt2$
and writes the prefactor $(\Delta\sqrt{\bar S_{mn}\bar S_{mn}})^2$; the
factors $\sqrt2$ and $\tfrac12$ above carry this into the registry's
$\lvert\bar S\rvert$ *(compiler check, not in the sources)*. The
coefficients take the first four of the five invariants
$I_1=\operatorname{tr}(\mathsf s^2)$, $I_2=\operatorname{tr}(\mathsf w^2)$,
$I_3=\operatorname{tr}(\mathsf s^3)$, $I_4=\operatorname{tr}(\mathsf w^2\mathsf s)$
(page-local; Eq. 14). With this normalization
$I_1=\mathsf s_{ij}\mathsf s_{ij}=2\bar S_{ij}\bar S_{ij}/\lvert\bar S\rvert^2=1$
at every point, so one of the four features is constant *(compiler check,
not in the sources)*; the paper does not comment.

**How many tensors (Table II, Fig. 1).** The mean a priori correlation
coefficient of $\tau^d_{ij}$ with filtered DNS, each value the best of 20
GEP runs, is 0.321, 0.630, 0.640, 0.888, 0.889, 0.869, 0.883, 0.854, 0.774
and 0.764 for $N_0=1,\dots,10$ basis tensors. It stops rising at four and
falls beyond seven, which the authors attribute to the larger search space
at fixed hyperparameters (100 individuals, 500 generations), not to the
basis (§III B).

**Which tensors (Table IV).** With constant coefficients, $T^{(2)}$ alone
gives a correlation of 0.5403, $T^{(4)}$ alone 0.6944, the two together
0.8792, adding $T^{(1)}$ 0.8831, adding $T^{(3)}$ 0.8874, all four 0.8885:
the two rotation-carrying tensors carry the model. $T^{(1)}$ and $T^{(3)}$
are spread evenly in space, $T^{(2)}$ and $T^{(4)}$ "concentrate in
specific areas", with spiky PDFs and extreme values ($T^{(4)}$ between $-326.83$
and $167.24$ against $\pm0.82$ for $\mathsf s$; Table V, Figs. 9–10), and
$\lvert T^{(4)}\rvert$ correlates with the $Q$ criterion normalized by
the paper's squared strain magnitude $\bar S_{mn}\bar S_{mn}$, which the
paper writes as $\tfrac12(\lvert\omega\rvert^2-1)$ in its own symbols
(Eqs. 24–25). The bound $\lvert\mathsf s_{ij}\rvert\le\sqrt{2/3}\approx0.8165$
of a unit-norm trace-free symmetric tensor is consistent with the printed
extremes 0.816 and $-0.817$ *(compiler check, not in the sources)*.

## An eight-term basis for the subgrid stress (Wu & Lele 2026)

[Wu & Lele (2026)](/sources/wu-2026.md) (arXiv v2, §3.1, Eq. 3.5) carry
the tensor-basis output to LES. With $\bar{\mathbf S}$ and
$\bar{\boldsymbol\Omega}$ the matrices of the resolved $\bar S_{ij}$ and
$\bar\Omega_{ij}$ (not normalized by $k/\varepsilon$), $\mathbf I$ the
identity and $c_1,\dots,c_8$ (page-local) the coefficients the network
predicts, the full subgrid stress (not only its deviator) is

$$\begin{aligned}\tau_{ij}={}&c_1\mathbf I+c_2\bar{\mathbf S}+c_3\bar{\mathbf S}^2+c_4\bar{\boldsymbol\Omega}^2+c_5(\bar{\mathbf S}\bar{\boldsymbol\Omega}-\bar{\boldsymbol\Omega}\bar{\mathbf S})+c_6\bar{\boldsymbol\Omega}\bar{\mathbf S}\bar{\boldsymbol\Omega}\\&+c_7(\bar{\mathbf S}^2\bar{\boldsymbol\Omega}-\bar{\boldsymbol\Omega}\bar{\mathbf S}^2)+c_8(\bar{\boldsymbol\Omega}\bar{\mathbf S}\bar{\boldsymbol\Omega}^2-\bar{\boldsymbol\Omega}^2\bar{\mathbf S}\bar{\boldsymbol\Omega}),\end{aligned}$$

after Stallcup & Dahm (2022) and the authors' earlier work, as cited. All
eight tensors are symmetric *(compiler check, not in the sources)*. The
basis has an identity term in place of Pope's trace-free forms, so the
isotropic part of $\tau_{ij}$ is learned too.

**Inputs.** The paper lists seven invariants of $\bar{\mathbf S}$ and
$\bar{\boldsymbol\Omega}$ (Eq. 3.6) but, because they are costly,
replaces them by the three invariants of the resolved velocity-gradient
tensor and the magnitudes $\lvert\bar S\rvert$, $\lvert\bar\Omega\rvert$
("complex" inputs), or by the first invariant and the two magnitudes
("simple" inputs). A graph network, not a perceptron, maps the inputs on
a mesh stencil to the coefficients, so that the stencil is learned
(after Abekawa et al., as cited). The basis tensors and the stress are
normalized locally by powers of the velocity-gradient magnitude (Eqs.
3.7–3.8).

**Outcome.** The basis is the same in every network of the paper; what
decides the a posteriori quality is the training filter and the input
set. Simple inputs make the a posteriori results consistent across
architectures, because higher powers of the velocity gradient "suffer
more from numerical artifacts such as aliasing" (§5.1.3, §7). Details are
on [neural-network SGS models](/methods/neural-network-sgs-model.md).

## A nonlinear basis for compressible subgrid stress and heat flux (Xu et al. 2023)

[Xu et al. (2023)](/sources/xu-2023.md) (§3.1, Eqs. 3.1–3.18) expand
the SGS stress of Favre-filtered compressible LES in the five-tensor basis
of Lund & Novikov (1992), as cited, built from the resolved strain
$\tilde S_{ij}$ and rotation $\tilde\Omega_{ij}$, plus four scalar terms
for the trace, and the SGS heat flux in four vectors after Vollant et al.
(2017) and Wang et al. (2007), as cited. In matrix notation, with
$\lVert\tilde S\rVert=\sqrt{\operatorname{tr}(\tilde S^2)}=\lvert\tilde S\rvert/\sqrt2$,
page-local basis tensors $\mathsf A^{(m)}$ and coefficients
$C^{\mathrm A}_m$, $C^{\mathrm I}_m$, $C^{\mathrm Q}_m$, and the paper's
stress per unit mass written $\tau_{ij}/\bar\rho$ in the registry's
compressible convention:

$$\begin{aligned}\frac{\tau^d_{ij}}{\bar\rho}&=\Delta^2\Big(C^{\mathrm A}_1\lVert\tilde S\rVert\mathsf A^{(1)}+C^{\mathrm A}_2\mathsf A^{(2)}+C^{\mathrm A}_3\mathsf A^{(3)}+C^{\mathrm A}_4\mathsf A^{(4)}+\frac{C^{\mathrm A}_5}{\lVert\tilde S\rVert}\mathsf A^{(5)}\Big)_{ij},\\\mathsf A^{(1)}&=\tilde S^d,\quad\mathsf A^{(2)}=\tilde S\tilde\Omega-\tilde\Omega\tilde S,\quad\mathsf A^{(3)}=\tilde S^2-\tfrac13\operatorname{tr}(\tilde S^2)\mathbf I,\\\mathsf A^{(4)}&=\tilde\Omega^2-\tfrac13\operatorname{tr}(\tilde\Omega^2)\mathbf I,\quad\mathsf A^{(5)}=\tilde\Omega\tilde S^2-\tilde S^2\tilde\Omega,\\\frac{\tau_{kk}}{\bar\rho}&=\Delta^2\Big(C^{\mathrm I}_0\lVert\tilde S\rVert^2+C^{\mathrm I}_1\lVert\tilde S\rVert\operatorname{tr}\tilde S+C^{\mathrm I}_2\operatorname{tr}(\tilde S^2)+C^{\mathrm I}_3\operatorname{tr}(\tilde\Omega^2)\Big),\\Q_j&=\Delta^2\Big(C^{\mathrm Q}_1\lvert\tilde S\rvert\partial_j\tilde T+C^{\mathrm Q}_2\tilde S_{jk}\partial_k\tilde T+C^{\mathrm Q}_3\tilde\Omega_{jk}\partial_k\tilde T+C^{\mathrm Q}_4\frac{\tilde S_{jk}\tilde S_{kl}}{\lvert\tilde S\rvert}\partial_l\tilde T\Big),\end{aligned}$$

with $Q_j=\widetilde{u_jT}-\tilde u_j\tilde T$ (page-local) and
$\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$. The stress coefficients
depend on four dimensionless invariants built from
$\operatorname{tr}(\tilde S^2)$, $\operatorname{tr}(\tilde\Omega^2)$,
$\operatorname{tr}(\tilde S^3)$, $\operatorname{tr}(\tilde\Omega^2\tilde S)$
and $\operatorname{tr}(\tilde\Omega^2\tilde S^2)$ (Pope 1975; Lund &
Novikov 1992, as cited), the heat-flux coefficients on six invariants of
$\tilde S_{ij}$ and of the vector $\Delta^2\lvert\tilde S\rvert\partial_i\tilde T$
(Eqs. 3.16, 3.18); a local Reynolds number is added to both input sets
(Table 1).

**Grid-width normalization (§3.2, Eqs. 3.27–3.43).** In the "modified"
models every velocity and temperature gradient is multiplied by the local
grid spacing in its direction, $\partial/\partial(x_k/\Delta_k)$ with
$\Delta_k$ as in registry §11, the starred strain and rotation built from
these gradients replace the original ones in both the basis and the
invariants, and $\Delta$ is set to one. The authors argue that this
"inherently embed[s]" the grid anisotropy near the wall in the inputs and
the basis.

**Coefficients.** The Germano identity (ODNA, MDNA) or ten small networks
whose merge layer multiplies the coefficients by the basis, so the loss
acts on the SGS term (OANA, MANA). With the dynamic procedure the
normalized model is "sometimes unstable" a posteriori on coarse grids;
with the network it reaches a priori correlations above 0.91 and is
stable a posteriori without clipping (§3.2, §4.1). The network, training
and results are on
[neural-network SGS models](/methods/neural-network-sgs-model.md).

## Integrity bases as sources of invariant features

An integrity basis can also serve the input side of a learned closure. Its
invariants are rotationally invariant scalars that a network can take as
features, whatever it outputs.
[McConkey et al. (2022)](/sources/mcconkey-2022.md) follow, citing it
(§III C), the procedure of Wu et al. and build the Spencer–Rivlin minimal
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
dataset (McConkey et al. 2021, cited in §III D). Its periodic-hill
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
- **Generalization.** Duraisamy et al. (2019, §5.3) cite
  gene-expression-programming models trained on low-Reynolds-number DNS of
  a backward-facing step that show "a high level of uncertainty" when used
  at high Reynolds number on the [periodic hill](/benchmarks/periodic-hill.md);
  Sandberg & Zhao (2022, §4.1) describe GEP models trained on a
  backward-facing step as giving excellent a posteriori periodic-hill
  predictions, some individuals being non-realizable and unstable. Both are
  second-hand accounts of cited work (see
  [backward-facing step](/benchmarks/backward-facing-step.md)).
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
- **Tensor basis in a supervised LES closure.** Wu & Lele (2026) keep
  the tensor-basis output for the subgrid stress and obtain a posteriori
  results that are stable across architectures once inputs are simple and
  training uses several filters (above); unlike Kim et al. (2022), they do
  not compare against a network without a basis.
- **Basis plus grid information in a compressible LES closure.** Xu et
  al. (2023, §3.3) credit the a priori gain of their model to three
  ingredients together: the nonlinear basis, the grid-width normalization
  and network coefficients; each variant missing one of them is weaker a
  priori (Figs. 4, 6–8, 10).
- **Invariance by construction (turbomachinery review).** Sandberg &
  Michelassi (2022, §4.3) cite Ling et al. (2016) and Weatheritt &
  Sandberg (2016) for combining the Cayley–Hamilton theorem with machine
  learning "to ensure that physical constraints are inherently
  satisfied", and state that, to their knowledge, machine-learned subgrid
  models "have yet to be employed" in blade- or stage-level simulations.
- **Locality.** Agrawal & Koutsourelakis (2024, §2.2.1) call the
  postulate that the stress at a point depends only on flow features at
  that point "a very strong assumption for flows that exhibit strong
  inhomogeneity", and model the resulting error with a stochastic
  discrepancy that remains "random even in the limit of infinite data"
  (§1, §2.2).
- **Invariance by architecture (combustion review).**
  [Ihme et al. (2022)](/sources/ihme-2022.md) (§3.5.1) cite the TBNN of
  Ling et al. as "one of the first architectures tailored for fluid
  modeling" and classify it as knowledge entering through the
  architecture, as opposed to the loss (see
  [physics-informed neural networks](/methods/physics-informed-neural-network.md));
  they describe its invariance as Galilean invariance obtained by merging
  the outputs of two networks, whereas the reviews above describe the
  rotational invariance supplied by the basis.
- **Keeping the linear closure instead.**
  [Shan et al. (2023)](/sources/shan-2023.md) (§I) review the TBNN, a
  later variant and an ensemble-Kalman-trained TBNN as nonlinear
  eddy-viscosity alternatives, and themselves learn only a scalar: a
  network maps six invariant mean-flow features to the Spalart–Allmaras
  variable $\tilde\nu$, which sets $\nu_t$ in the
  [Boussinesq closure](/definitions/boussinesq-hypothesis.md) (§II.C; see
  [field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
  They list the linear stress representation among the uncertainties
  their model leaves untouched (§IV).
- **Locality (reviews).** Existing feature sets use only local quantities.
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
- Agrawal & Koutsourelakis (2024) print $\dim\boldsymbol\theta=6970$ for
  5 inputs, 8 hidden layers of 30 and 10 outputs (Table 3); a fully
  connected network of that shape with biases on every layer has 7000
  parameters, 30 more than printed *(compiler check, not in the
  sources)*. Their Eq. 9 defines the
  Reynolds stress with a minus sign, $-\langle u_i'u_j'\rangle$, while
  Eqs. 10, 14 and 17 use the positive-trace form adopted here.
- Agrawal & Koutsourelakis (2024, Table 1) call the basis tensors
  symmetric but print $T^{(7)}=\mathsf W\mathsf S\mathsf W^2+\mathsf W^2\mathsf S\mathsf W$.
  With $\mathsf S$ symmetric and $\mathsf W$ antisymmetric,
  $(\mathsf W\mathsf S\mathsf W^2)^T=-\mathsf W^2\mathsf S\mathsf W$, so the
  printed sum is antisymmetric; the difference
  $\mathsf W\mathsf S\mathsf W^2-\mathsf W^2\mathsf S\mathsf W$ is the
  symmetric combination, and the other nine printed tensors are symmetric
  *(compiler check, not in the sources)*. Li et al. (2021, Eq. 13) print
  $T^{(7)}$ as that difference, $\omega s\omega^2-\omega^2s\omega$ in their
  symbols.
- Li et al. (2021) print $\lvert T^{(4)}\rvert=\lvert\omega\rvert^2$ (Eq.
  25, their normalized rotation $\omega$). With $T^{(4)}=\mathsf w^2-\tfrac13\operatorname{tr}(\mathsf w^2)\mathsf I$
  and $\mathsf w$ antisymmetric, $\mathsf w^2$ has eigenvalues
  $0,-c^2,-c^2$ with $2c^2=\lvert\mathsf w\rvert^2$ (here
  $\lvert\mathsf w\rvert=\sqrt{\mathsf w_{ij}\mathsf w_{ij}}$, the paper's
  norm, without the registry's factor two), so $T^{(4)}$ has
  eigenvalues $\tfrac13\lvert\mathsf w\rvert^2$,
  $-\tfrac16\lvert\mathsf w\rvert^2$, $-\tfrac16\lvert\mathsf w\rvert^2$
  and $\lvert T^{(4)}\rvert=\lvert\mathsf w\rvert^2/\sqrt6$ *(compiler
  check, not in the sources)*; the proportionality, which is what the
  argument uses, holds. In Eq. 24 the middle expression carries the
  normalized $\lvert s\rvert^2$ in the prefactor where the dimensional
  strain magnitude is needed; the final form
  $\tfrac12(\lvert\omega\rvert^2-1)$ is consistent with
  $Q=\tfrac12(\lvert\Omega\rvert^2-\lvert S\rvert^2)$ in their unscaled
  magnitudes *(compiler check, not in the sources)*. Their Table II
  header prints the sixth stress component as $\tau_{12}$ a second time
  where Fig. 5 shows $\tau_{23}$; §III D and Table V call the normalized
  rotation $\Omega$, which Eq. 12 names $\omega$.
- Oulghelou et al. (2025, Eqs. 7–10) normalize the strain and rotation of
  the basis by the specific dissipation rate, $S_{ij}/\omega$ and
  $\Omega_{ij}/\omega$, instead of by $\varepsilon/k$; with
  $\omega=\varepsilon/(\beta^*k)$ their $T^{(1)}$ is $\beta^*\mathsf S$ and
  their $T^{(2)}$, $T^{(3)}$ carry $\beta^{*2}$, so their coefficients
  differ from those of the $k/\varepsilon$ normalization by these factors
  *(compiler check, not in the sources)*. Their basis corrects an SST
  model additively, $b_{ij}=-\nu_t\langle S_{ij}\rangle/k+b^\Delta_{ij}$
  (page-local $b^\Delta_{ij}$), and a second expansion feeds a
  production-like term of the $k$ equation; the blending of such models
  is on [model aggregation](/methods/turbulence-model-aggregation.md).
- Xu et al. (2023, Eqs. 3.11, 3.37) print the scalar trace $\tau_{kk}$
  as a sum that contains the identity, $T^I_1=I\cdot\mathrm{Tr}(\tilde S)$
  and the like; the scalar form above drops the identity, since a scalar
  cannot equal a tensor sum *(compiler check, not in the sources)*. Their
  Table 2 labels the coefficients of the modified models without the star
  that the text uses. The paper writes the basis $T^A_m$, $T^I_m$; this
  page writes $\mathsf A^{(m)}$ to keep $T^{(n)}$ for Pope's basis.
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
  Both sources cite Schmelzer et al. (2020), which is not ingested (Tang
  et al. also Beetham & Capecelatro); neither prints a sparse-regression
  model. [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (arXiv v2)
  print two corrected models (three non-zero terms), from the sparse
  Bayesian variant SBL-SpaRTA. They describe the method as regressing the
  coefficients from "a large dictionary of monomials" of the invariants
  $I_1$, $I_2$ (§2.1, Eqs. 8–10), and every model they print has constant
  coefficients: $5.21\,T^{(2)}$ and $0.681\,T^{(1)}$ for the
  separated-flow expert, $0.25\,T^{(1)}$ for the jet expert (Table 1).
  [Cherroud et al. (2022)](/sources/cherroud-2022.md) (App. A–B) print
  sparse Bayesian models with invariant-dependent coefficients at small
  sparsity, e.g.
  $[(-0.496\pm0.0133)+(21.6\pm0.366)I_1+(17.4\pm0.374)I_2]\,T^{(1)}$ in the
  anisotropy correction at $\lambda=10^2$ (Eq. A.1). The models selected by a posteriori
  cross-validation are constant ($0.8433\,T^{(1)}$, $0.382\,T^{(1)}$,
  $0.197\,T^{(1)}$ for the production correction; Eqs. A.13–A.15), and the
  three deterministic SpaRTA models of Schmelzer et al. that they reprint
  are constant too (e.g. $0.1\,T^{(1)}+4.09\,T^{(2)}$, App. B). Tang et
  al.'s text does not say whether the claim concerns the method or the
  published models. *Open.*

# Citations

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (L2, Cayley–Hamilton), §5.2–§5.3, Eqs. 11–12 (tensor-basis expansion, TBNN, gene-expression programming, features).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A, Eq. 4 (TBNN), random forests, symbolic and sparse regression, §IV.A (a priori training, sparse loss), §V (features), §VII (interpretability).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — arXiv v1: §III B (outputs), §III C, Table I (33 features), App. A, Table II (47-tensor basis, vanishing invariants in 2D), §IV C, Fig. 22 (SHAP), §V (TBNN for the non-linear part, 3D count).
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: §II E (tensor-basis network tried in DRL, no conclusive gain).
- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §I, §II C 2, Eqs. 10–16 (2D basis, convention, linear/non-linear split, conditioning), §III B (claim on constant coefficients), §III C, Fig. 11 (contributions), §IV.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §2.1 (Galilean but not rotational invariance), §7 (tensor-basis networks as future work).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §2, Eqs. 1–2, 7–10 (additive correction on the 2D basis, $\omega$ normalization); §2.1, Table 1 (SBL-SpaRTA dictionary and printed constant-coefficient models).
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §3.1, Eqs. 3.5–3.8, Figs. 2–3 (eight-term LES basis, inputs, graph front end, normalization); §5.1.3, §7.
- [Li et al. (2021)](/sources/li-2021.md) — §II B, Eqs. 9–14 (basis for the subgrid stress, normalization, invariants); §III B, Table II, Fig. 1 (number of tensors); Tables IV–V, §III D, Figs. 9–10, Eqs. 24–25 (ablation, vortical tensors, $Q$).
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §4.3, Eq. 2 (GEP coefficients on four basis tensors; Ling et al. cited; ML subgrid models not yet used in turbomachinery).
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — arXiv v2: §1, §2.2–2.2.5, Eqs. 9–10, 14–17, Table 1 (basis, invariants, $k$-$\varepsilon$ limit, locality); §3.3, Table 3 (architecture, pre-training); §3.4, Fig. 7 (learned stress); App. A.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.2, Eqs. 2–4 (basis, time scale, linear and non-linear terms); §3.3, Eqs. 6–7 (heat-flux basis, invariants, linearity principle); §4.1–4.2.1 (TBNN and GEP results of cited works).
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §1 (black-box against open-box); §2.1, Eqs. 5–8 (2-D basis normalized by $\omega$); App. A, Eqs. A.1, A.13–A.15; App. B (constant and invariant-dependent coefficients).
- [He et al. (2022)](/sources/he-2022-b.md) — §1 (TBNN as an L2 correction, in passing).
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §3.5.1 (TBNN as an architecture-level knowledge-guided model).
- [Shan et al. (2023)](/sources/shan-2023.md) — §I (TBNN variants reviewed); §II.C (scalar eddy-viscosity network instead); §IV (linear representation left as an uncertainty).
- [Xu et al. (2023)](/sources/xu-2023.md) — §3.1, Eqs. 3.1–3.18, Table 1 (Lund–Novikov basis, trace terms, heat-flux basis, invariants); §3.2, Eqs. 3.27–3.43, Table 2 (grid-width normalization); §3.3; §4.1 (MDNA unstable).
