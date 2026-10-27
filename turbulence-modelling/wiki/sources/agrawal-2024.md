---
type: Source
title: "Agrawal & Koutsourelakis (2024) — A probabilistic, data-driven closure model for RANS simulations with aleatoric, model uncertainty"
description: "A Reynolds-stress closure made of a tensor-basis neural network plus a latent stochastic discrepancy field with a sparsity prior, trained by variational inference through an adjoint RANS solver on sparse mean-velocity and pressure data, with probabilistic predictions on a backward-facing step."
resource: "doi:10.1016/j.jcp.2024.112982"
source_kind: paper
authors: [Agrawal A., Koutsourelakis P.S.]
year: 2024
venue: "J. Comput. Phys. 508:112982"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Computational_Physics_Agrawal_A_probabilistic_data-driven_closure_model_for_RANS_simulatio.pdf"
tags: [data-driven, uncertainty-quantification, rans, tensor-basis, model-consistent-training]
timestamp: 2026-10-26T10:27:00Z
---

# Summary

Agrawal & Koutsourelakis (2024) propose a probabilistic Reynolds-stress
closure for steady incompressible RANS with two additive parts. The parametric
part is the [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
of Ling et al., Pope's ten-tensor expansion of the anisotropy with
network coefficients; with only $g^{(1)}=-0.09$ it reduces to the
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md), whose
[linear eddy-viscosity](/definitions/boussinesq-hypothesis.md) form confines
the anisotropy to the plane-strain line. The stochastic part is a latent
random discrepancy field $\boldsymbol\delta_R$, piecewise constant on 52
subdomains, under an automatic-relevance-determination prior that switches
it off where the network suffices and so localizes where the closure is
inadequate. The authors call the error it represents *aleatoric* model error,
which "remain[s] random even in the limit of infinite data", and the
parameter uncertainty *epistemic* (§1, §2.2). The
[model-form uncertainty](/definitions/model-form-uncertainty.md) page
records how other sources classify it.

Training is [model-consistent](/methods/model-consistent-training.md)
("trajectory regression", the a posteriori side of
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)):
no Reynolds-stress data are used, only time-averaged velocity and pressure
from LES at about 8% of the RANS nodes. The posterior is approximated by
stochastic variational inference, with point estimates for the network
weights and precisions and Gaussians for the discrepancy, and the gradients
come from a discrete adjoint of a FEniCS finite-element RANS solver coupled to
PyTorch. The authors set this against adjoint
[field inversion](/methods/field-inversion-machine-learning.md) works that keep
the linear eddy viscosity, and cite
[symbolic-regression closures](/methods/symbolic-regression-closure.md) among
data-driven alternatives. On a two-dimensional
[backward-facing step](/benchmarks/backward-facing-step.md) (expansion ratio 2,
trained at $Re_h=300$, 700, 900, 1100 and tested at 500, reference LES with
the [WALE model](/methods/wale-model.md)) the predicted mean fields agree with
LES and their credible intervals envelop it in most places; both
recirculation zones appear, and the reattachment length is $10.06\pm1.21$
against the LES value of 9.10 and 5.61 for $k$-$\varepsilon$.

# Version read

arXiv preprint 2307.02432v2 (15 April 2024; footer "Preprint submitted to
Journal of Computational Physics, April 16, 2024"), the authors' preprint, not
the typeset version of record. 33 pages (main text pp. 1–27, Appendices A–B
pp. 28–30, references pp. 30–33), all read. Equation, figure, table and page
numbers are those of the preprint. Title and authors match the published
identity.

# Key claims

1. Model-consistent ("trajectory regression") training with a differentiable RANS solver allows training on indirect data (mean velocity and pressure) instead of Reynolds-stress data; non-intrusive "model regression" does not guarantee accurate mean fields, since small errors in the stress can be amplified by the solve (§1, §2.2). **Stated**
2. Even with model-consistent training the learned closure carries an aleatoric model error, from an insufficient parametric form and from local input features that do not carry enough information (the locality assumption); it remains whatever the amount of training data (§1, §2.2). **Stated**
3. The parameter uncertainty in $\boldsymbol\theta$ is epistemic, its posterior collapsing to a Dirac delta with infinite data, whereas the latent discrepancy "remain[s] random even in the limit of infinite data" (§2.2, after Eq. 13). **Stated**
4. "To the authors' knowledge, uncertainty quantification has not been addressed for data-driven turbulence model training with indirect observations" (§1). **Stated**
5. A differentiable RANS solver in automatic-differentiation frameworks "has not been accomplished yet" to the authors' knowledge; sensitivities come instead from an adjoint (§1). **Stated**
6. With $g^{(1)}=-0.09$ and all other $g^{(n)}=0$ the expansion (Eq. 15) degenerates to the classical $k$-$\varepsilon$ model (§2.2.1). **Stated**
7. The linear eddy-viscosity model restricts the anisotropy to the plane-strain line; citing barycentric realizability maps, the tensor-basis architecture can explore other realizable states (§2.2.1). **Stated**
8. The ARD prior (Eqs. 20–21, $\alpha_0=\beta_0=10^{-3}$) removes the redundancy between $\boldsymbol\theta$ and $\boldsymbol\delta_R$, favouring solutions where the parametric model covers most of the domain; an infinite precision forces a zero discrepancy (§2.2.2). **Stated**
9. The discrepancy depends on grid and geometry: it can be used for unseen conditions in the same geometry (another Reynolds number, inlet or boundary conditions), not for another geometry (§2.2.3, §2.2.5). **Stated**
10. Prediction needs no baseline RANS data as network input, unlike earlier tensor-basis works (§2.2.5). **Stated**
11. Random initialization of the network "led to divergence of the solution even after applying the stabilization schemes"; the network was pre-trained on baseline closure data with added noise (§3.3). **Shown** (reported, no figure)
12. Without any stress observations the learned stress captures the basic features of the LES Reynolds stress at $Re_h=500$, while $k$-$\varepsilon$ "severely under/over-estimates its magnitude and misrepresents its spatial variability"; the largest errors are at $5<x/h<10$ (§3.4, Fig. 7c). **Shown**
13. The inferred precision is small where the learned stress deviates most from LES ($5<x/h<10$) and very large, i.e. practically no discrepancy, far downstream where the flow is almost parabolic (§3.4, Fig. 7). **Shown**
14. Although the stress field has discrepancies, the predicted mean fields agree well with LES, which the authors read as non-uniqueness of the inverse problem, "also reported by other works" (§3.4). **Shown**
15. The model predicts both recirculation zones in close agreement with LES; $k$-$\varepsilon$ "underestimates the size of the first recirculation zone and almost completely misses the second one" (§3.4, Fig. 8). **Shown**
16. The predictive standard deviation is largest around the shear layers; the credible intervals (±2 standard deviations, Fig. 11) envelop the LES values "in most areas" and are very tight near the inlet (§3.4, Figs. 8, 11). **Shown**
17. The pressure predictions single out the reattachment zone (around $x/h\approx10$), where the posterior standard deviation is higher (§3.4, Fig. 10). **Shown**
18. With observations at about 8% of the nodes and few near the wall, the predicted streamwise velocity captures the backflow in the first recirculation zone, which $k$-$\varepsilon$ misses; ±3 standard deviations envelop the LES downstream (§3.4, Fig. 12). **Shown**
19. Cost relative to the baseline $k$-$\varepsilon$ RANS at $Re_h=500$: LES 7679, the proposed solver 1.3; the text says the LES is "roughly 6000 times more computationally demanding" than the proposed model (§3.4, Table 4). **Shown**
20. Reattachment length $x_R/h$ at $Re_h=500$: LES 9.10; Biswas et al. 8.9 (at expansion ratio 1.9423); $k$-$\varepsilon$ 5.61; Geneva & Zabaras 5.52; proposed $10.06\pm1.21$ (±3 standard deviations), the only prediction that envelops the LES value (§3.4, Table 5). **Shown**
21. The low reattachment of Geneva & Zabaras "could be attributed to the lack of the stochastic, model correction term" (§3.4). **Stated** (conjecture)
22. The evidence lower bound could serve as a Bayesian model-comparison criterion and drive adaptive subdomain partitions (§2.2.4). **Stated** (not carried out)
23. The network follows Ling et al.: 8 hidden layers of 30 nodes, Leaky ReLU, $\dim\boldsymbol\theta=6970$ (§3.3, Table 3). **Stated**
24. A direct comparison with earlier tensor-basis works is not possible because they blend baseline near-wall stresses with predicted ones through case-dependent functions (§3.4). **Stated**

The closure (Eqs. 13, 17, 19–21), with $\mathsf S_{ij}$, $\mathsf W_{ij}$ the mean strain and rotation scaled by $k/\varepsilon$, $W$ the Boolean map from $N_g$ grid points to $N_d$ subdomains and $\Lambda^E$ the ARD precisions (page-local, as on the model-form-uncertainty page):
$$\boldsymbol R=\boldsymbol R_{\boldsymbol\theta}+\boldsymbol\delta_R,\qquad R_{\boldsymbol\theta,ij}=2k\sum_{n=1}^{10}g^{(n)}_{\boldsymbol\theta}(I_1,\dots,I_5)\,T^{(n)}_{ij}+\tfrac23k\delta_{ij},\qquad \boldsymbol\delta_R=W\boldsymbol E,\qquad p(\boldsymbol E\mid\Lambda^E)=\prod_{J=1}^{N_d}\mathcal N\big(\boldsymbol E_J\mid0,\mathrm{diag}(\Lambda^E_J)^{-1}\big),$$
where $\boldsymbol R$ and $\boldsymbol\delta_R$ collect the nodal stress components, $I_1=\mathrm{tr}(\mathsf S^2)$, …, $I_5=\mathrm{tr}(\mathsf W^2\mathsf S^2)$, and each $\Lambda^E_{J\ell}$ has a $\mathrm{Gamma}(10^{-3},10^{-3})$ hyperprior. The likelihood is Gaussian with variances of 1% of each observable's mean square, a tolerance rather than a noise model (§2.2.3). **Stated**

# Printed slips

- **Basis tensor $T^{(7)}$ (Table 1):** the caption calls the basis tensors symmetric, but $T^{(7)}$ is printed as $\mathsf W\mathsf S\mathsf W^2+\mathsf W^2\mathsf S\mathsf W$; since $(\mathsf W\mathsf S\mathsf W^2)^T=-\mathsf W^2\mathsf S\mathsf W$, the printed sum is antisymmetric and the symmetric combination is the difference *(compiler check, not in the sources)*; see [tensor-basis neural network](/methods/tensor-basis-neural-network.md).
- **Viscosity name:** §2.1.1 calls $\nu$ "the dynamic viscosity", §3.1 the "kinematic viscosity"; Eq. 1 uses it as kinematic.
- **Sign of the Reynolds stress:** Eq. 9 defines $\tau^{RS}=-\langle\tilde u_i\tilde u_j\rangle$ and Eq. 10 sets $k=-\tfrac12\mathrm{tr}(\tau^{RS})$, but Eqs. 10, 14 and 17 write the stress as $\tfrac23kI+\dots$, the form of the positive convention; the trace of Eq. 10 gives $k=+\tfrac12\mathrm{tr}\,\tau$ *(compiler check, not in the sources)*.
- **Table 2:** five viscosities (3.33, 2.00, 1.42, 1.11, $0.909\times10^{-3}$) are listed "for training data generation" for four training Reynolds numbers; with $u_b=h=1$ they correspond to 300, 500, 704, 901, 1100, i.e. the test case is included *(compiler check, not in the sources)*. Fig. 2 shows only 1100, 900 and 700 as training settings.
- **§2.2.3:** $\dim\hat z^{(m)}=N_{obs}$, but $\Sigma=\mathrm{diag}(\sigma_1^2,\dots,\sigma^2_{3N_{obs}})$.
- **Footnote 2 (p. 13):** $E^{(m)}_\tau=\mu^{(m)}_E+\mathrm{diag}(\sigma_E^{2,(m)})\phi$ multiplies by the variance; Algorithm 1 uses $\mu^{(m)}_E+\sigma^{(m)}_E\odot\phi$.
- **Eq. 29:** quantified "$\forall i\in\{1,\dots,M\}$" with index $m$; Algorithm 1 and §3.2 write $\{\hat z^{(i)}\}_{m=1}^M$.
- **Appendix A:** "As the Reynolds number is increased, the convection term dominates, leading to stability", where the context requires instability.
- **Fig. 10 caption** (pressure contours): rows labelled "(⟨u⟩)" and "(σ(u))".
- **§3.2:** a 10% draw per node "yield[s] approximately 8% of the grid points"; the paper does not reconcile the two numbers.
- **Table 3:** $\dim\boldsymbol\theta=6970$, while a fully connected 5–30×8–10 network with all biases has 7000 parameters *(compiler check, not in the sources)*.
- **Reference list:** [53] and [64] are the same work (Ahmed et al. 2021, Phys. Fluids 33:091301); [3] prints "NNASA/CR-2014-218178".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U_i$, $P$ | $u_i$, $p$ (instantaneous) | |
| $u_i$, $p$ | $\langle u_i\rangle$, $\langle p\rangle$ | lower case is the time average |
| $\tilde u_i$, $\tilde p$ | $u_i'$, $p'$ | **collision:** the tilde is the Reynolds fluctuation, not a Favre filter |
| $\tau^{RS}=-\langle\tilde u_i\tilde u_j\rangle$ | $-R_{ij}$ | **negative convention**; Eqs. 10, 14, 17 use the positive form (see Printed slips) |
| $\tau$, $\tau_\theta$ | $R_{ij}$ (discrete, three components per node in 2D), its network part | **collision** with the SGS stress $\tau_{ij}$ |
| $\epsilon$ | $\varepsilon$ | |
| $\epsilon_\tau$, $E_\tau$ | $\boldsymbol\delta_R$, $\boldsymbol E$ (discrepancy and its subdomain values, page-local) | **collision:** $\epsilon_\tau$ is not a dissipation |
| $W$, $N_d$, $\Lambda$ | $W$, $N_d$, $\Lambda^E$ (page-local) | $12180\times52$ |
| $N$ | $N_g$ (number of grid points, page-local) | **collision** with the polynomial degree $N$ |
| $\bar S=\tfrac12(\nabla u+\nabla u^T)$ | $\langle S_{ij}\rangle$ | **collision:** the overbar is not an LES filter |
| $S$, $\Omega$ (Eq. 14) | $\mathsf S_{ij}$, $\mathsf W_{ij}$ | scaled by $k/\varepsilon$ (registry §11) |
| $b$, $b_\theta$ | $b_{ij}$ | $\tau=2kb+\tfrac23kI$ matches the registry in the positive convention |
| $T^{(k)}$, $G^{(k)}$, $I_1,\dots,I_5$ | $T^{(n)}$, $g^{(n)}$, $I_1,\dots,I_5$ | $G$ also names the discrete operator $G(z)$ |
| $\theta$ | $\boldsymbol\theta$ | |
| $\nu$ (Eq. 18) | $\nu_\theta$ (precision of the weight prior, page-local) | **collision** with the viscosity |
| $z=[u,p]^T$, $G$, $B$, $R$ | (discrete state, operator, divergence matrix, residual) | **collision:** $R$ is not the Reynolds stress |
| $\xi$, $q_\xi$, $F(\xi)$ | (variational parameters, density, evidence lower bound) | **collision** with the reference coordinate $\xi$ |
| $\lambda$ | (adjoint vector) | **collision** with the Taylor microscale |
| $Re=uh/\nu$ | $Re_h$ | step height and inlet bulk velocity |
| $h$, $H$ | (step height, channel height) | **collision:** $h$ is not an element size |
| $x_{reattach}$ | $x_R$ | |

# Reference list

96 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. References [53] and
[64] are a printed duplicate (Ahmed et al. 2021), folded into one entry.
References [7] and [8] are the ingested sources
[Duraisamy (2021)](/sources/duraisamy-2021.md) and
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md). Seven arXiv preprints
([18], [27], [54], [55], [78], [79], [93]) are kept as their own entries;
[86] (Celik et al. 2005) is printed without a venue.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunk 6. This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
- [WALE model](/methods/wale-model.md)
- [OpenFOAM](/software/openfoam.md)
