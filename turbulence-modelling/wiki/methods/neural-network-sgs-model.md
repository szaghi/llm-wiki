---
type: Method
title: "Neural-network subgrid-scale models"
description: "LES closures in which a neural network maps resolved-field features to the subgrid stress, its divergence, a model coefficient or an energy-conserving operator; trained a priori, by reinforcement learning or through the solver. Covers inputs, multi-filter fusion, normalization, invariance, structure preservation, cost against dynamic models and backscatter."
status: established
aliases: [ANN-SGS model, GAN SGS model, fusion network, T-SR-FU, energy-conserving neural closure, structure-preserving closure, ANN-SGS mixed model, deep-learning LES closure, DL-LES, neural-network LES closure, data-driven SGS model, S-106H, SL-106H, SL-180C, DL-AR1, DL-AR2, multi-filter training, TBNN-GNN]
tags: [neural-network, sgs-model, les, data-driven]
timestamp: 2026-10-28T07:06:00Z
---

# Neural-network subgrid-scale models

A **neural-network SGS model** replaces the closure of the filtered
Navier–Stokes equations, or part of it, by a network
$f(\boldsymbol\zeta;\boldsymbol\theta)$ evaluated from resolved-field
features $\boldsymbol\zeta$ at each grid point or element. What the
network returns differs between the sources: the six components of the
subgrid stress $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ (Kang et al.
2023; Kim et al. 2022), a stress whose divergence stands for every
unclosed term (Sirignano & MacArt 2023), or the coefficient of an
analytical model (Kurz et al. 2023). How it is trained differs too: a
priori on filtered DNS (Kang et al.), by
[reinforcement learning](/methods/reinforcement-learning-closure.md) in
the running LES (Kim et al.; Kurz et al.), or through the adjoint of the
LES equations (Sirignano & MacArt); see
[model-consistent training](/methods/model-consistent-training.md) and
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).
Duraisamy (2021, §III.A) cites other networks that model the SGS force
$\partial_j\tau_{ij}$ directly (Beck et al.; Xie et al.), "since
small errors in the subgrid scale *stresses* can otherwise generate large
errors in the momentum equation".

## The models in the sources

| Source | Output | Inputs | Network | Training |
|---|---|---|---|---|
| [Kang et al. (2023)](/sources/kang-2023.md) | 6 components of $\tau_{ij}$ | single point: $\bar S_{ij}$ (S models) or $\bar S_{ij}$ and $L_{ij}$ (SL, "mixed") | 2 hidden layers of 12 neurons, Leaky ReLU, linear output | supervised on filtered DNS |
| [Kim et al. (2022)](/sources/kim-2022.md) | 6 components of $\tau_{ij}$ (or a scalar $\nu_t$), times $\Delta^2$ | single point: $\partial_i\bar u_j$ and grid size, in wall units | 6 hidden layers of 128 units | DRL on two mean profiles |
| [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) | a $3\times3$ tensor $h_{ij}$ whose divergence replaces all unclosed terms | the filtered velocity-gradient tensor | gated feed-forward, tanh, 50 units per layer | adjoint-based, in the LES |
| [Kurz et al. (2023)](/sources/kurz-2023.md) | one Smagorinsky $C_s\in[0,0.5]$ per DG element | the element's momentum field (or five velocity-gradient invariants) | 3D CNN, four convolution layers | PPO in the running LES |
| [Kim et al. (2024)](/sources/kim-2024.md) | 6 components of $\tau_{ij}$ | single point: $\bar S_{ij}$ or $\partial_j\bar u_i$, alone (G) or with their test-filtered copies (T) | fully connected; "fusion" variant with two 64-node branches subtracted | supervised on box-filtered DNS of a cylinder wake |
| [Maejima & Kawai (2025)](/sources/maejima-2025.md) | a velocity field 8 times finer in $x$ and $z$, from which $\tau_{ij}$ is filtered | wall-parallel planes of $(u,v,w)$ of a very coarse LES | 2-D CNNs: CycleGAN generator, then conditional Wasserstein GAN | unsupervised on unpaired LES/filtered-DNS planes, then supervised on filtered-DNS/DNS pairs |
| [Wu & Lele (2026)](/sources/wu-2026.md) | 8 coefficients of a tensor basis for $\tau_{ij}$ | invariants and magnitudes of the resolved velocity gradient on a mesh stencil | graph network front end, tensor-basis output, about 24,000 parameters | supervised on DNS filtered with one to three filter shapes |
| [Xu et al. (2023)](/sources/xu-2023.md) | coefficients of a nonlinear tensor basis for the deviatoric stress, its trace and the SGS heat flux (compressible) | single point: invariants of grid-width-normalized resolved strain, rotation and temperature gradient, and a local Reynolds number | ten networks, two hidden layers of 10 neurons each in the final model, tensor-basis merge layer | supervised on filtered DNS of one channel |
| [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) | skew-symmetric and dissipative operators acting on the coarse solution and auxiliary SGS variables (1D) | coarse solution, SGS variables, coarse right-hand side | CNN, two hidden layers, kernel 5 | hybrid derivative and trajectory fitting |

Agdestein & Sanderse (2025) train a CNN on the discrete commutator error
of a staggered grid (see
[divergence-consistent LES](/methods/divergence-consistent-les.md) and
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)).

**Networks as deconvolution.**
[Valencia et al. (2026)](/sources/valencia-2026.md) (§I) write that the
approximate deconvolution framework of the
[scale-similarity model](/methods/scale-similarity-model.md) "has been
extended later on with data-driven methods", citing neural-network blind
deconvolution (Maulik & San; Maulik et al., two-dimensional turbulence)
and deep-learning or GAN super-resolution of turbulent velocity fields
(Liu et al.; Deng et al.), the line to which the
[super-resolution SGS models](/methods/super-resolution-sgs-model.md)
belong. Valencia et al. themselves test only non-learned deconvolution,
a priori; in compressible isotropic turbulence those models reach
correlations above 0.99 with the total unresolved stress at a
filter-to-grid ratio of 4 (Table VII; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

**A network against an explicit expression.**
[Li et al. (2021)](/sources/li-2021.md) run the artificial-neural-network
model of Xie, Yuan & Wang (2020), as cited, as a comparator for their
[gene-expression-programming](/methods/symbolic-regression-closure.md)
subgrid model in $128^3$ LES of forced isotropic turbulence ($\Delta$ of
16 DNS spacings, LES spacing $\Delta/2$, filtered DNS at
$Re_\lambda\approx260$ as reference; §III C). Network and explicit model
agree closely with filtered DNS in the energy spectrum, the longitudinal
structure functions of order 2, 4 and 6, the PDFs of velocity increments
and of the subgrid stress, where the network's PDFs are slightly wider,
and the PDF of the SGS energy flux with its backscatter tail; the dynamic
Smagorinsky and dynamic mixed models do not (Figs. 2–8). In the
subgrid-stress PDFs network and explicit model differ only in the extreme
tails (Fig. 5); they also differ in cost (below). Li et al. survey the
earlier network SGS models in §I (Sarghini et al. 2003, Wang et al. 2018,
Zhou et al. 2019, Beck et al. 2019, Xie et al. 2019–2020, Park & Choi
2021, as cited). As for applications, Sandberg & Michelassi (2022, §4.3)
state that, to their knowledge, machine-learned subgrid models "have yet
to be employed" in blade- or stage-level turbomachinery simulations.

**A network explained, then replaced by constants (Wang et al. 2022).**
[Wang et al. (2022)](/sources/wang-2022-j.md) start from their group's
earlier network-based spatial gradient model, summarized in §II.C: the
subgrid stress is a quadratic form in the first-order filtered velocity
gradients at the seven points of a stencil (the local point and its six
axis neighbours), with 49 dimensionless coefficients supplied by a network
trained on forced isotropic-turbulence DNS. Only 19 of them mattered, and
they were nearly constant and patterned: about $+0.18$ for the
local–local product, about $-0.016$ for local–neighbour products and about
$+0.016$ for each neighbour with itself (§II.C, Table I). The authors show
that this pattern is a discretization of the second-order truncation of
the higher-order [gradient model](/methods/gradient-model.md): a Taylor
expansion of the neighbour gradients, or upwind and downwind differences
of the second-order gradients, both give the constants $1/8$, $-1/144$,
$+1/144$ for a filter-to-grid ratio of two, the SGM-7-19 model (§III,
App. A, Eqs. 15–20; derivation on the gradient-model page). They read the
network as having found "the most accurate way to approximate" the
higher-order gradient model with first-order gradients, and the constant
model as "not a case-by-case result inspired by a particular outcome of
ANN" (§III). The price of dropping the network is a small loss of a
priori accuracy at $\Delta$ of 16 DNS spacings (correlation coefficients
for $\tau_{11}$, $\tau_{12}$: 0.985, 0.981 for the 19-term network,
0.973, 0.973 for SGM-7-19, 0.945, 0.946 for the classical gradient model;
Table II), which the authors attribute to higher-order gradients the
network captures implicitly. A posteriori, in forced isotropic turbulence
and a temporal mixing layer, SGM-7-19 is closest to filtered DNS among
the dynamic Smagorinsky, dynamic mixed and implicit LES runs, at 1.5 and
1.7 times the subgrid-model cost of dynamic Smagorinsky (dynamic mixed:
2.1 and 2.3; Table V). Backscatter is clipped for stability (§IV). The
two tables print the network coefficients differently: Table I gives
$\mp1.6\times10^{-2}$ for the neighbour coefficients, consistent with the
text's "one order" below the local one, and Table II gives $\mp0.0016$.

## Learned closures in reacting-flow LES (as reviewed by Ihme et al. 2022)

[Ihme et al. (2022)](/sources/ihme-2022.md) (§4.1.4) review learned
closures of the filtered reacting-flow equations, whose unclosed terms
they group into the filtered chemical source (turbulence–chemistry
interaction), the subgrid convective flux (stresses and scalar transport)
and the subgrid molecular diffusion (Eq. 72). As cited there:

- a deep network for the joint filtered density function of mixture
  fraction and progress variable outperforms algebraic models at large
  filter widths, a priori, on MILD-combustion DNS;
- a U-Net CNN that takes only the filtered progress variable
  outperforms physics-based closures of the subgrid flame-surface density,
  a priori, on DNS with impulsively changed inlet conditions;
- a feedforward network for the filtered scalar dissipation rate of the
  progress variable reproduces small-scale features at small filter
  ratios, with discrepancies growing as the filter widens (Fig. 31);
- CNN and feedforward networks model unresolved stresses, filtered
  sources and subgrid progress-variable transport in premixed jet and
  V-flames.

Their summary: supervised learning "often outperform[s] physics-based
closure models in a priori studies; however, caution is warranted for
extrapolating these findings to a posteriori applications", since models
trained on filtered DNS "can be unstable due to the accumulation of small
errors over a large number of timesteps when evaluated a posteriori"
(§4.1.4; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
Their example of a remedy is a knowledge-guided loss (see
[super-resolution SGS models](/methods/super-resolution-sgs-model.md)),
and they state that most combustion applications to date are a priori
tests on idealized problems (§6).

[Nista et al. (2023)](/sources/nista-2023.md) (§1) place their
generative super-resolution closure of premixed flames in this line,
against the a priori successes of earlier network closures of reacting
LES (their refs. 6–10) and the a posteriori convergence problems they
cite; their own study is a priori only. Its finding bears on any
supervised network: trained on one flame, the closure generalizes across
Reynolds and Karlovitz numbers while the filter-to-Kolmogorov ratio
$\Delta/\eta$ stays near its training value and degrades on a hydrogen
flame where it does not (§4.1–4.2, §4.4); the method and the printed
ratios are on
[super-resolution SGS models](/methods/super-resolution-sgs-model.md).

Networks also regress thermochemistry with no subgrid stress involved:
in passing, [Kumar et al. (2023)](/sources/kumar-2023.md) (§3.4, Fig. 5)
close the source terms and diffusivities of transported principal
components in a DNS of a turbulent premixed flame with small networks
trained on a two-dimensional species DNS; the method is described on
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
and on its Source page.

Two non-learned closures of compressible LES position themselves against
learned ones: [Zhang et al. (2022d)](/sources/zhang-2022-h.md) (§I) state
that many data-driven models, built on the ideal-gas assumption, omit the
thermodynamic subgrid terms of real gases, and call their deconvolution
model "independent of DNS data" (see
[scale-similarity model](/methods/scale-similarity-model.md));
[Zhang et al. (2022b)](/sources/zhang-2022-f.md) (§I) survey
neural-network subgrid models only in their introduction.

## Supervised mixed network (Kang et al. 2023)

**Architecture and data (§2.4).** A multilayer perceptron with layer map
$X^n_i=\sigma(\sum_jW^n_{ij}X^{n-1}_j+b^n_i)$ (page-local), two hidden
layers of 12 neurons and a linear output of six stress components. The
loss is the mean squared error over the six independent components
against filtered DNS (Eq. 2.10); mini-batches of 128, Adam at $10^{-4}$,
$5\times10^5$ iterations. Isotropic turbulence supplies $2\times10^8$
samples from 30 snapshots (80% training); channel flow
$3.5\times10^7$ from five fields. The inputs are single-point, a choice
made for numerical stability, following Park & Choi (2021), and for low
cost. Grid and test filters are Gaussian with $\hat\Delta/\Delta=\sqrt5$
in isotropic turbulence (top-hat filters gave "no considerable
differences"), and fourth-order commutative discrete filters with
$\Delta=4$ and $\hat\Delta=8$ DNS spacings in the channel (§2–§3.5).

**Inputs: strain alone or strain plus resolved stress.** With $\bar S_{ij}$
alone the network "only rescales the given input" and predicts a stress
nearly aligned with the strain: a priori, in forced isotropic turbulence
at $Re_\lambda=106$, the correlation of $\bar S_{12}$ with the predicted
$\tau_{12}$ is $-0.8217$, against $-0.2806$ in filtered DNS (§3.1, Table
3). Like an eddy-viscosity model it cannot backscatter, and a posteriori
it performs almost identically to the dynamic Smagorinsky model. Adding
the six components of the resolved stress
$L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j$, the term
of the [dynamic mixed models](/methods/scale-similarity-model.md), raises
the a priori correlation of the deviatoric stress with filtered DNS from
0.3509–0.3692 to 0.7040–0.7176 (Table 4) and reproduces the PDF of the
SGS dissipation including backscatter. In LES the mixed network runs
stably "without any ad hoc procedures", whereas the algebraic dynamic
models need averaging in homogeneous directions and clipping, without
which they overestimate both backscatter and forward scatter and diverge
"within tens of time steps" (§3.1, §3.3; see
[energy backscatter](/definitions/energy-backscatter.md)). Among
similarity terms tried as second input (modified Leonard term, $L_{ij}$,
the [gradient-model](/methods/gradient-model.md) term), $L_{ij}$ is best
overall; the gradient term gives the largest spectral errors on coarse
grids, which the authors attribute to its truncation error (App. C).

**Normalization for generalization (§2.4, §3.2).** Inputs are divided by
the volume average of their tensor norm, $\bar S_{ij}/\langle\lvert\bar S\rvert\rangle$
and $L_{ij}/\langle\lvert L\rvert\rangle$ (here $\langle\cdot\rangle$ is a
volume or plane average and $\lvert\cdot\rvert$ the $L_2$ norm of the
tensor, as in the paper). The output would need $\langle\lvert\tau\rvert\rangle$,
unknown in LES, so it is replaced by an estimate: the norm of the
gradient-model term $\tfrac1{12}\Delta^2\partial_k\bar u_i\partial_k\bar u_j$
in isotropic turbulence, whose ratio to the filtered-DNS norm stays the
most constant across $Re_\lambda$ and across training-to-test filter-width
ratios $1/2$, 1 and 2 (Fig. 10); and $\langle\lvert L\rvert\rangle$ in the
channel, because the gradient term has an incorrect near-wall scaling
(citing Liu et al. 1994). The design rule is that the normalized
input and output distributions must not change with Reynolds number or
resolution; otherwise a "prior probability shift" degrades the model.
Normalizations by wall units, or by the rms velocity and Taylor
microscale, fail on untrained grids because they ignore the filter-width
change (App. E).

**Results.**

- *Isotropic turbulence.* Models trained at $Re_\lambda=106$, 286 or both
  perform almost identically, so one Reynolds number and one resolution
  suffice there (§3.2). Trained on forced turbulence only, the mixed
  networks predict decaying turbulence on $24^3$, $48^3$, $96^3$ and (at
  $Re_\lambda=286$) $128^3$ grids more accurately than dynamic
  Smagorinsky, stably (Table 5, Figs. 13–17).
- *Against algebraic mixed models.* The network beats the one- and
  two-parameter dynamic mixed models a posteriori in decaying turbulence
  although its a priori correlation is lower than that of the
  two-parameter model with a Clark term (0.70–0.72 against 0.91; §3.3,
  Table 6).
- *Channel flow at $Re_\tau=180$* ($48^3$, $\Delta x^+=47.2$,
  $\Delta z^+=15.7$). The network trained on channel data gives
  $C_f=0.0092$ against 0.0085 in filtered DNS, 0.0072 for dynamic
  Smagorinsky and 0.0103 without model, and better mean velocity, rms
  velocities and Reynolds shear stress than dynamic Smagorinsky (§3.5,
  Table 11). It also beats it on untrained coarser
  ($32\times48\times32$) and finer ($64^3$) grids and at $Re_\tau=395$
  (Figs. 26–27). The strain-only network underpredicts the mean velocity
  at $Re_\tau=395$.
- *Training flow matters for the mean shear.* Trained on isotropic
  turbulence only, the mixed network is stable in the channel and gives
  good fluctuations but underpredicts the mean velocity, attributed to the
  vanishing mean off-diagonal SGS stress of isotropic training data; a
  network trained jointly on both flows is accurate in both (§3.5, Fig.
  29). Normalizing by plane averages instead of volume averages makes the
  mean SGS shear stress vanish at the wall and improves the mean velocity
  of the isotropic-trained model (§3.6, Fig. 30).
- *SGS anisotropy.* In the anisotropy-invariant map of the plane-averaged
  SGS stress (Lumley–Newman form), the channel-trained mixed network
  reaches the two-component limit at the wall like filtered DNS; the
  strain-only network stays near the isotropic origin (§3.7, Fig. 32).
  The authors consider the use of $L_{ij}$ "the most important factor"
  for generalization to an untrained channel flow, since $L_{xy}$ follows
  the near-wall distribution of $\tau_{xy}$ while $\bar S_{xy}$ grows
  toward the wall (§3.7, Fig. 31).

**Reference DNS and forcing (App. A).** With the negative-viscosity
forcing that Langford & Moser (1999) report using, the authors obtain
$Re_\lambda=122.9$ instead of 164; the deterministic forcing of Machiels
(1997) gives 164.7 and reproduces the reported statistics, and is used
for all analyses (Table 14; see
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).

## Nonlinear algebraic network for compressible wall-bounded LES (Xu et al. 2023)

[Xu et al. (2023)](/sources/xu-2023.md) close both the SGS stress and the
SGS heat flux of Favre-filtered compressible LES, page-local
$Q_j=\widetilde{u_jT}-\tilde u_j\tilde T$, with a network that returns
the coefficients of an algebraic tensor expansion rather than the
stresses (the expansion, its invariants and the grid-width normalization
are on [tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
The viscous unclosed terms are neglected and the subgrid turbulent
diffusion is approximated through $\tau_{ij}$, so only $\tau_{ij}$ and
$Q_j$ are modelled (§2.1).

**Four variants (§3).** The coefficients come from the
[Germano identity](/methods/dynamic-procedure.md) (ODNA, MDNA) or from a
network (OANA, MANA), with the original gradients (O) or with every
gradient multiplied by the local grid width in its direction, $\Delta_k$
(registry §11), and $\Delta$ replaced by one (M, "modified"). The authors
motivate the modification by the near-wall grid anisotropy
$\Delta_y\ll\Delta_x,\Delta_z$, which the isotropic
$\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$ ignores (§3.2), and the network
coefficients by the ad hoc averaging and clipping of the dynamic
procedure (§1).

**Network and training (§3.1, Tables 1–2, Eqs. 3.19–3.26).** One network
per output component: six for the deviatoric stress, one for its trace,
three for $Q_j$, ten in all. Each has two hidden layers of $N_h$ neurons
(MANA-1: $N_h=10$; 20 and 40 change little a priori, Figs. 9, 11), a
leaky-ReLU activation, a coefficient layer and a merge layer that
multiplies the coefficients by the basis tensors, so the loss, the mean
squared error over mini-batches of 1000, acts on the SGS term itself.
Inputs are four dimensionless invariants of the resolved strain and
rotation (six for the heat flux) and the local Reynolds number
$\bar\rho\lvert\tilde{\boldsymbol u}\rvert d/\tilde\mu$ with $d$ the wall
distance, standardized in each wall-parallel plane; targets and basis
tensors are divided by the plane r.m.s. of the
[gradient-model](/methods/gradient-model.md) estimate of the same term.
The data are about $1.8\times10^7$ samples of one filtered DNS (channel at
$Re=3000$, $M=1.5$, isothermal walls; top-hat filter ratios 8 and 4 in
$x$ and $z$), split 60/15/25%, trained with Adam at an initial learning
rate $10^{-3}$ for 2000 epochs. Adam beat Adadelta and Adagrad, and
leaky ReLU beat sigmoid, ReLU and ELU (App., Figs. 32–33).

**A priori (§2.2, §3, Figs. 1–12).** The dynamic Smagorinsky, Vreman and
WALE models have plane-wise correlations $C$ "almost lower than 0.6" (metrics defined on [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)) and relative errors $E_r$
near 1.0, which the authors attribute to the linear stress–strain
alignment of eddy-viscosity models (see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). OANA-2
reaches $C>0.6$ for most components with $E_r\approx0.8$, "still not a
well-performing model"; the grid-width normalization lifts the dynamic
model most below $y^+=50$; MANA-1 reaches $C>0.91$ and $E_r<0.4$ for all
components and reproduces the plane-averaged SGS fluxes of kinetic energy
and temperature variance, which the eddy-viscosity models and MDNA
"significantly underestimate". The authors credit all three ingredients:
the nonlinear form, the normalization and the network (§3.3).

**A posteriori (§4, Tables 3–8).** Sixth-order central differences and
third-order Runge–Kutta; [implicit LES](/definitions/implicit-les.md)
here means the same scheme with no model. Against DNS filtered at the LES
resolution:

- *Training channel, untrained grid* ($64\times65\times64$, filter ratios 6
  and 2; $\Delta x^+\approx43$, $\Delta y_w^+\approx0.9$,
  $\Delta z^+\approx14$). MANA's van Driest velocity in the log region is
  "fully consistent" with filtered DNS; the eddy-viscosity models give a
  larger and the unmodelled run a slightly lower one, which the authors
  read as excessive and insufficient SGS dissipation. MANA matches the
  r.m.s. velocities, Reynolds shear stress, r.m.s. temperature and
  streamwise heat flux; the other runs overpredict the r.m.s. peaks and
  place them further from the wall (Figs. 13–16).
- *Untrained flows.* Channels at $Re=4880$, $M=3.0$ and $Re=7000$,
  $M=1.0$ (an "extremely sparse" grid, $\Delta x^+\approx78$–81), a
  near-incompressible channel at $M=0.2$, and a spatially developing
  adiabatic boundary layer at $M=2.25$: MANA stays closest to filtered
  DNS, with slightly larger buffer-layer peaks of $\tilde v_{\mathrm{rms}}$
  and the Reynolds shear stress in the first two and a slight
  overestimation of $u$, $v$ and temperature fluctuations in the boundary
  layer (§4.2–4.4).
- *Backscatter.* The eddy-viscosity models give only positive SGS fluxes;
  MANA gives both signs, as filtered DNS does, without clipping, and its
  PDFs of both fluxes at $y^+=15$ collapse on filtered DNS (Figs. 18–20;
  see [energy backscatter](/definitions/energy-backscatter.md)). The
  dynamic model "strongly overestimates" the mean SGS kinetic-energy flux
  and Vreman and WALE underestimate it (Fig. 17).

The authors attribute the transfer to untrained grids to the grid-width
information "inherently embedded in the input and tensor bases", and
contrast it with "black box" networks that map filtered quantities to SGS
terms directly (Park & Choi 2021; Xie et al. 2019, as cited), which in
their view "cannot have a good performance in untrained cases" (§4.1,
§5).

## Fusion network for a cylinder wake (Kim et al. 2024)

Kim et al. (2024) build pointwise fully connected SGS models for LES of
flow over a [circular cylinder](/benchmarks/circular-cylinder-wake.md),
which the authors present as a first step toward networks for complex
geometries (§1). Page-local: $D$ is the cylinder diameter, $U$ the
free-stream velocity, $L_r$ the mean recirculation length.

**Data (§2.2).** Box-filtered DNS at $Re_D=3900$ ($1025\times501\times128$
points, immersed boundary, second-order central differences), filtered to
the LES grid with a one-sided box near the wall; 25 snapshots over about
20 shedding cycles, four spanwise planes, a box $-1\le x/D\le6$,
$-1.5\le y/D\le1.5$, about $4.08\times10^6$ samples. A second, coarser
data set comes from the same DNS by a spanwise box test filter applied to
the filtered field, instead of a second DNS on another grid as in Park &
Choi (2021). Inputs and outputs are normalized by $U$ and $D$, because wall
units do not suit a wake and rms normalization needs statistics unknown at
an untrained Reynolds number (§3.3).

**Architectures (§3.1–3.3, Table 2, Eqs. 3.1–3.3).** G models take the
grid-filtered $\bar S_{ij}$ (SR, 6 inputs) or $\partial_j\bar u_i$ (VG, 9
inputs), with two hidden layers of 128 nodes, batch normalization and
ReLU, as in Park & Choi (2021). T-nFU models concatenate grid- and
test-filtered inputs into the same network. The new **fusion** (FU)
models feed the two levels to separate branches of two 64-node layers and
subtract their outputs before the linear output layer. The authors
motivate the late fusion by video-classification networks (Karpathy et al.)
and by the [Germano identity](/methods/dynamic-procedure.md): the
difference between the two levels should let the network use the
resolved stress $L_{ij}$. The loss is the mean squared error over the six
components (Eq. 3.2).

**Results (Table 3).**

| Grid (cells) | DNS | no model | dynamic Smagorinsky | G-SR | G-VG | T-SR-FU | T-VG-FU |
|---|---|---|---|---|---|---|---|
| training, $449\times271\times64$ | 1.56 | 1.25 | 1.32 | 1.51 | 1.56 | 1.59 | 1.56 |
| coarser, $353\times213\times64$ | 1.56 | 0.74 | 0.80 | 1.16 | 1.07 | 1.55 | 1.49 |
| finer, $545\times301\times64$ | 1.56 | — | 1.45 | 1.22 | 1.39 | 1.62 | 1.57 |

The entries are $L_r/D$ at $Re_D=3900$; a dash marks a value not quoted
here. The nFU networks fail
($L_r/D=0.79$ and 1.28 on the training grid), consistent with their
wrong-signed a priori shear stress (§4.1–4.2; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
Trained at $Re_D=3900$, the fusion networks predict $Re_D=5000$
($L_r/D=1.45$ and 1.47 against 1.39 in DNS, dynamic model 1.35) and
$Re_D=10\,000$ (T-SR-FU $L_r/D=0.85$, base-pressure coefficient $-1.17$,
$C_D=1.10$ against the experimental 0.82, $-1.13$, 1.14; dynamic model
$L_r/D=0.62$) (§4.2.3). The authors conclude that several filtered data
sets of different filter sizes plus fusion give networks that work on
grids other than the training grid (§4.2.2). In channel flow at
$Re_\tau=178$ the fusion idea also beats G-SR and the dynamic model on an
untrained coarser grid (App. D). On still coarser cylinder grids every
LES diverges, including the dynamic model and no model; T-SR-FU runs only
when the SGS stress is clipped to zero wherever backscatter occurs (App.
C; see [energy backscatter](/definitions/energy-backscatter.md)).

## Multi-filter training for solver robustness (Wu & Lele 2026)

[Wu & Lele (2026)](/sources/wu-2026.md) (arXiv v2) attribute the a
posteriori degradation of supervised networks to a distribution shift
between training data and LES, with an output source (the stress
statistics depend on the filter shape) and an input source (complex
inputs are sensitive to aliasing and to the numerical method); see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

**Model (§3.1, Figs. 2–3, Eqs. 3.5–3.9).** A graph network with skip and
residual connections learns the input stencil (after Abekawa et al., as
cited) and feeds two branches of $1\times1$ convolutions that return the
coefficients of an eight-term tensor basis for the full $\tau_{ij}$ (see
[tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
Inputs are either "complex", the three invariants of the resolved
velocity-gradient tensor $\bar A_{ij}=\partial_j\bar u_i$ (page-local: its
trace $P_A$, $Q_A=\tfrac12[P_A^2-\operatorname{tr}(\bar A^2)]$ and
$R_A=\det\bar A$, with $P_A$ masked to zero in incompressible flow) plus
$\lvert\bar S\rvert$ and $\lvert\bar\Omega\rvert$, or "simple",
$P_A$, $\lvert\bar S\rvert$, $\lvert\bar\Omega\rvert$. Inputs are max–min
normalized; the basis and the stress are normalized locally by powers of
$\lvert\bar A\rvert$ and by $\Delta^2\lvert\bar A\rvert^2$. The loss adds
the relative root-mean-square errors of $\tau_{ij}$ and of the SGS
dissipation $\Pi=-\tau_{ij}\bar S_{ij}$ (Eq. 3.9). A variant with three
more layer-normalization layers (ALN) serves as an architecture
perturbation.

**Training filters (§3.0.1–3.0.2, Eqs. 3.3–3.4).** Training data are
built with up to three filter shapes, used together as one training set:

- the box filter;
- a "discrete spatial cosine filter", the compact positive kernel
  $G(r)=\Delta^{-1}[1+\cos(2\pi r/\Delta)]$ for $\lvert r\rvert\le\Delta/2$,
  a 33-point stencil for $\Delta=16$ DNS spacings, whose spectral
  oscillations peak at 0.028 against 0.22 for the box filter;
- the box filter followed by the two-thirds dealiasing cutoff
  $\mathcal D$ (page-local), $\tau^{\mathcal D}_{ij}=\mathcal D(\overline{u_iu_j})-\mathcal D(\bar u_i)\mathcal D(\bar u_j)$,
  which "completely changes the subgrid stress field" (§3.2.2, Fig. 4).

The filters do not mimic any solver's transfer function; the aim is to
keep the network from overfitting "to filter peculiarities". A sharp
spectral cutoff is excluded because a filter oscillatory in physical
space creates spurious small scales (§2.1). Data: forced isotropic
turbulence at $Re_\lambda=433$ ($1024^3$) and channel flow at
$Re_\tau=1000$, filtered to 16 and 32 DNS spacings, 80/10/10 split; every
network sees both flows (§3.2.1).

**Results (§5–6, Tables 3–4).** Sum spectral errors (page-local SSE, the
summed absolute log-difference of LES and filtered-DNS spectra) in forced
isotropic turbulence on $64^3$:

| Network (complex inputs; original architecture unless stated) | Fourier-spectral solver, 2/3 dealiasing | sixth-order compact solver |
|---|---|---|
| box only | 18.87 | 32.58 |
| box + dealiasing filter | 4.0 | — |
| box + cosine filter | — | 11.93 |
| cosine filter only | — | 35.33 |
| all three filters | 4.58 | 14.22 |
| box only, ALN architecture | 5.56 | 9.50 |
| static Smagorinsky, $C=0.18$ | 16.6 | — |
| [sigma model](/methods/sigma-model.md), $C=1.3$ | 13.34 | — |

A dash marks a run not reported. Findings:

- *Single-filter networks are fragile.* The box-only network is
  under-dissipative with high-wavenumber pile-up, and its error changes
  markedly with the architecture, which the authors read as layer
  normalization "masking its lack of robust physical knowledge" (§5.1.2,
  §6.2.2). Two-filter results barely move (4.0 against 3.93 with ALN).
- *Simple inputs make the variants consistent* (SSE 3.68–4.98 and
  7.56–15.84 in the two solvers), and two-filter training "will often do
  no worse than training on one filter" (§5.1.3, §5.2.3).
- *One network, two solvers.* The three-filter network runs in both
  solvers without retraining and beats the box-only network in both; it
  is not optimal because it was also trained on a filter that does not
  apply to the compact solver (§5.2.1, §8).
- *Coarser grid and channel.* On $32^3$ two-filter training again
  corrects the box-only network. In wall-modelled channel LES at
  $Re_\tau=1000$ ($128\times96\times32$, the wall model of Bou-Zeid et
  al. as cited) the box-only complex network "completely fails" with
  unphysical spectra, and the box + dealiasing network gives mean
  velocity and Reynolds stresses "oftentimes" more accurate than the
  sigma model (§6.1–6.2).
- *Baselines.* The static Smagorinsky model and the sigma model are
  over-dissipative in isotropic turbulence; they reproduce the
  longitudinal flatness better than the networks, which the authors
  attribute to over-dissipation, while the networks reproduce the PDF of
  resolved enstrophy production far better (§5.1.1).

The authors limit the conclusion to two high-order solvers; lower-order
solvers remain to be tested (§7–8).

## Energy-conserving closure with SGS variables (van Gastelen et al. 2024)

van Gastelen et al. (2024) build a closure that is stable for any network
weights yet allows backscatter, for 1D Burgers and Korteweg–de Vries
equations in a discretize-first setting (see
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)
for the filter and the exact energy split). Page-local: $\bar{\boldsymbol u}\in\mathbb R^I$
is the coarse solution, $\boldsymbol s\in\mathbb R^I$ one auxiliary SGS
variable per coarse cell, $\boldsymbol a=[\bar{\boldsymbol u};\boldsymbol s]$,
$\mathbf M_2$ the block-diagonal coarse mass matrix (the paper's
$\Omega_2$), and $f_H$ the coarse energy-conserving discretization.

**SGS variables (§3.2, App. C).** Each $s_i$ is a linear compression of
the subgrid content of cell $i$, with the compression vector taken from
the first left singular vector of subgrid snapshots, so that
$\tfrac12\|\boldsymbol s\|^2$ approximates the subgrid energy. The exact
choice $s_i=\pm\sqrt{\text{local subgrid energy}}$ "resulted in poor
performance": small model errors flipped signs and runs diverged.

**Closure (§3.1, Eqs. 33–37).**

$$\frac{d\boldsymbol a}{dt}=\begin{bmatrix}f_H(\bar{\boldsymbol u})\\\boldsymbol 0\end{bmatrix}+\mathbf M_2^{-1}(\mathbf K-\mathbf K^T)\boldsymbol a-\mathbf M_2^{-1}\mathbf Q^T\mathbf Q\,\boldsymbol a,$$

with state-dependent matrices $\mathbf K$, $\mathbf Q$ built from four
output channels of a CNN times parameterized convolutions (§3.3, Eqs.
43–46). The skew-symmetric term exchanges energy between resolved and
SGS variables without creating it; the dissipative term removes it. The
approximate total energy $\mathcal E_s=\tfrac12\boldsymbol a^T\mathbf M_2\boldsymbol a$
obeys

$$\frac{d\mathcal E_s}{dt}=\bar{\boldsymbol u}^T\mathbf M_Hf_H(\bar{\boldsymbol u})-\|\mathbf Q\boldsymbol a\|_2^2,$$

($\mathbf M_H$ the coarse mass matrix), so the closure is stable for any
weights when $f_H$ conserves energy, and the resolved energy can still
grow by exchange with $\boldsymbol s$. Momentum is conserved to machine
precision by making the weights of the relevant convolutions sum to zero
(§3.3.3, Eqs. 47–50). The dissipative term is included because the fine
operator dissipates at least as much as the coarse one, which the authors
show only numerically (App. B, Fig. B.17); it is omitted for KdV (§4.2).

**Results (§4).** Against a vanilla CNN closure, a trained constant
Smagorinsky model and no closure, at equal degrees of freedom (the
structure-preserving model has $2I$):

- it improves on no closure by about one order of magnitude in integrated
  error and beats Smagorinsky on Burgers (§4.3.1, Fig. 7);
- in accuracy it is roughly on par with the vanilla CNN, which is better on
  KdV for most resolutions but gives no stable model at the two finest
  (§4.3.1);
- every seed gives stable runs, while CNN replicas are "hit or miss"
  (§4.4, Fig. 8);
- total energy always decreases on Burgers while resolved energy
  oscillates by backscatter, as in filtered DNS (§4.5, Fig. 10);
- it is best throughout a viscosity range of $10^{-3}$ to $10^{-1}$ after
  training on $10^{-2}$ to $10^{-1}$ (§4.7, Fig. 13), and in a 3-fold
  space and 5-fold time extrapolation of KdV it keeps the DNS
  resolved-energy distribution where the CNN injects nonphysical energy
  (§4.8, Figs. 14–16).

For 3D the authors expect the analogue of $\boldsymbol s$ to be "probably
the sub-grid scale stress tensor", with several SGS equations (§5).

## Super-resolution closure for very coarse wall-bounded LES (Maejima & Kawai 2025)

Maejima & Kawai (2025) reconstruct a fine velocity field from the coarse
LES and filter products of its sub-cell fluctuations to obtain the stress;
the method, data and budgets are on
[super-resolution SGS models](/methods/super-resolution-sgs-model.md).
Points that bear on neural SGS models in general:

- **Training input.** On grids where the energetic near-wall eddies are
  not resolved ($\Delta x^+=72$, $\Delta z^+=36$ in channel flow at
  $Re_\tau\approx1000$), the resolved field differs from filtered DNS, so
  models trained on filtered DNS meet a different input in use; the
  authors therefore train the first stage without paired data (§1, §3.1;
  see [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
- **Spatial against pointwise inputs.** Pointwise velocity-gradient inputs
  "may not be able to appropriately distinguish the non-physical
  structures" that convolutional networks see (§7).
- **Grid dependence.** Convolutions act in computational coordinates, so
  the wall-unit resolution must be similar in training and use (§7).
  Within that limit the model trained at $Re_\tau\approx1000$ runs at
  $Re_\tau\approx2000$ on the same wall-unit grid with mean velocity in
  good agreement with DNS (Figs. 28–29).
- **Backscatter kept, not removed.** Stresses are clipped only where the
  effective viscosity falls below $\nu_{\mathrm{clip}}\approx-2\bar\nu_w$
  ($\bar\nu_w$ the mean kinematic viscosity at the wall, page-local);
  less clipping gives a better mean velocity, about $-3\bar\nu_w$ is
  unstable (§3.2, App. C; see
  [energy backscatter](/definitions/energy-backscatter.md)).
- **Result.** In the coarsest LES the bulk flow rate is over-predicted by
  10%, against 23% with the selective mixed-scale model (§6.1).

## Networks that replace the solver instead of the closure

[Li et al. (2024)](/sources/li-2024.md) and
[Zhao et al. (2025)](/sources/zhao-2025.md) learn the time advance of the
filtered velocity on the LES grid with neural operators and roll it out
without an LES solver; Zhao et al. train it on the residual of the
Smagorinsky-closed filtered equations. Neither models $\tau_{ij}$; both
compare with dynamic or static Smagorinsky LES on the same grid. See
[neural-operator surrogates of LES](/methods/neural-operator-les-surrogate.md).

## Stabilization that a priori networks need

Wang et al. (2023c, §V), citing the literature, state that
machine-learning SGS models with excellent a priori accuracy often
under-perform or go unstable a posteriori, and need hyper-viscosity,
regulation of negative SGS flux or additional filtering, which reduces
their efficiency. Kang et al. (2023, §3.1) state that their network LES
"becomes stable without any ad hoc procedures". Kim et al. (2024) run
their fusion networks without such fixes on the training grid and on
untrained grids (Table 3), and clip the stresses where backscatter occurs
only on still coarser grids, where the dynamic model and no model also
diverge (App. C).

## Adjoint-trained network for bluff-body LES (Sirignano & MacArt 2023)

The network of Sirignano & MacArt (2023, §2.1, Eq. 2.7) is a gated
feed-forward network. With input features $\boldsymbol\zeta$ the filtered
velocity-gradient components at a grid point (the paper's $z$), weights $W^k$,
biases $b^k$, $\sigma=\tanh$ and $\odot$ the elementwise product:

$$\begin{aligned}H^1&=\sigma(W^1\boldsymbol\zeta+b^1),\qquad H^2=\sigma(W^2H^1+b^2),\\H^3&=G^1\odot H^2,\quad G^1=\sigma(W^5\boldsymbol\zeta+b^5),\\H^4&=\sigma(W^3H^3+b^3),\\H^5&=G^2\odot H^4,\quad G^2=\sigma(W^6\boldsymbol\zeta+b^6),\\h(\boldsymbol\zeta;\boldsymbol\theta)&=W^4H^5+b^4,\end{aligned}$$

with 50 hidden units per layer; the gates are likened to those of
LSTM and GRU networks and add nonlinearity. The output is a $3\times3$
tensor $h_{ij}$ whose divergence replaces the subgrid-stress divergence
and the extra terms of filtering at the body and of filter–derivative
non-commutation on the non-uniform mesh (§2). One network and one
parameter set serve the whole domain, near the walls and far from them,
so there is no separate [wall model](/methods/machine-learning-wall-model.md);
the LES do not resolve $y^+=10$ at most stations, yet the near-wall mean
profiles "generally slightly outperform" the
[anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
and "dramatically outperform" dynamic Smagorinsky and no-model LES (§4.3,
Fig. 10). In boundary-layer regions no-model and dynamic-Smagorinsky LES
give "incorrectly large" resolved Reynolds stresses where filtered DNS is
near zero (§4.2, Figs. 8–9). Training and drag results are on
[model-consistent training](/methods/model-consistent-training.md).

## Invariance and constraints

- Sirignano & MacArt (2023, §2.1): velocity-gradient inputs make the model
  Galilean invariant, not rotationally invariant; tensor-basis networks
  are future work (§7; see
  [tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
- Kim et al. (2022, §II E) impose reflectional equivariance and a zero
  stress at the wall, not rotational or Galilean invariance; a tensor
  basis brought no conclusive gain.
- Kurz et al. (2023, §3.4) offer the velocity-gradient invariants as a
  Galilean-invariant input, following Novati et al.; they trained slower
  and ended worse than the element's raw momentum field (§4.3).
- Kang et al. (2023) state no invariance property of their network.
- Xu et al. (2023, §3) take invariants of the resolved strain and
  rotation (and of a temperature-gradient vector) as inputs and return the
  coefficients of a tensor basis; the grid-width normalization multiplies
  each gradient component by the spacing in its direction, a choice tied
  to the grid axes.
- Kim et al. (2024, §3.1) use pointwise inputs normalized by $U$ and $D$;
  no invariance property is stated.
- van Gastelen et al. (2024, §3.3) build translation equivariance into
  the convolutional operators and enforce momentum and energy
  conservation exactly (to the time-integration error, §6).
- Wu & Lele (2026, §3.1) feed invariants and magnitudes of the resolved
  velocity gradient and return the coefficients of a tensor basis, so the
  tensorial structure comes from the basis; they replace the
  tensor-basis invariants by the velocity-gradient invariants because the
  former are costly.

## Cost against the dynamic model

| Source | Comparison | Ratio to the dynamic Smagorinsky model |
|---|---|---|
| Kang et al. (2023, §3.4, Figs. 23–24) | SGS-stress evaluation, 16 CPU cores, 100 steps, forward pass in the LES code | network 0.71 (12 neurons), 0.89 (24), 1.42 (48); algebraic mixed models 1.68–2.24 |
| Kang et al. (2023, §1), cited | earlier ANN-SGS models | 1.3 (Park & Choi 2021), 1.8 (Wang et al. 2018), 2.4 (Yuan et al. 2020), 15 (Xie & Wang 2019), 256 (Xie et al. 2020a) |
| Kim et al. (2024, App. E, Table 6) | 18 cores, cylinder LES at $Re_D=3900$, training grid | SGS-stress evaluation about 10 (G-SR) and 6.5 (T-SR-FU); whole time step about 2.5 and 2 |
| Kim et al. (2024, App. E) | T-SR-FU on the coarser grid against dynamic Smagorinsky on the finer grid, similar accuracy | 2.113 s against 2.986 s per time step, about half the grid points |
| Xu et al. (2023, §4.1, Table 4) | 1000 time steps of the whole LES, 80 CPU cores (Intel Xeon Gold 6148), dynamic Smagorinsky about 15.4 s | MANA 0.79; Vreman 0.28, WALE 0.29, no model 0.26; the dynamic nonlinear model MDNA about 2.54 |
| Xu et al. (2023, §1), cited | earlier ANN-SGS models | 1.3 (Park & Choi 2021), 1.8 (Wang et al. 2018), 2.4 (Yuan et al. 2020), 15 (Xie et al. 2019), 256 (Xie et al. 2020), the same figures as Kang et al. cite |
| Kurz et al. (2023, §4.2) | policy evaluation against the dynamic procedure, one CPU core, 48 DOF, unoptimized | about 1.1 |
| Li et al. (2021, §III F, Fig. 13) | time per iteration, 16 cores (Intel Xeon E5-2670), several grids; network of Xie et al. (2020) against GEP, dynamic Smagorinsky and dynamic mixed models | not printed: the network "much more expensive" than all others, more so on larger grids; GEP slightly above the dynamic Smagorinsky model and below the dynamic mixed one |

## Qualifications

- **Printed activation.** Kang et al. (2023, §2.4, p. A38-8) print the
  Leaky ReLU as $\sigma(x)=\max[-0.02x,x]$. For $x<0$ this returns
  $-0.02x>0$, a non-monotone function; a leaky ReLU with slope 0.02 for
  negative arguments is $\max[0.02x,x]$ *(compiler check, not in the
  sources)*. Whether the code
  used the printed form cannot be told from the paper.
- **Printed activation (Xu et al.).** Xu et al. (2023, §3.1, p. A4-15)
  print the leaky ReLU as $\sigma(x)=\max[-0.1x,x]$, citing Ling et al.
  (2016) and Xie et al. (2020).
- **Scope of Xu et al.'s generalization claim.** MANA is trained on one
  channel at one Reynolds number, Mach number and filter (§3.1); the
  untrained tests are four channels and one boundary layer, all with the
  same sixth-order central solver (§4). Their trained weights are in the
  supplementary material, not read here.
- **Printed Reynolds number.** The caption of Kang et al.'s Fig. 10 gives
  $Re_\lambda=106$, 168 and 286; the DNS cases are at 106, 164 and 286
  (Table 1).
- **Illegible equation.** In Kang et al.'s Eq. 3.4, the second term of the
  tensor $H_{ij}$ of the one-parameter dynamic mixed model is typeset with
  colliding accents and is not legible; it is not reconstructed here (see
  [scale-similarity model](/methods/scale-similarity-model.md)).
- **Scope of the stability claim.** The mixed network's stability without
  clipping is shown in pseudospectral isotropic turbulence and a
  fourth-order finite-difference channel (Kang et al. 2023, §2–§3). The
  cost ratios are relative to dynamic Smagorinsky with test filtering in
  the authors' solvers; no static model is timed.
- **Comparisons are not on common cases.** The models of the first table
  are tested on isotropic turbulence, channel flow, bluff-body wakes and
  1D model equations, with different solvers and references; no source compares
  supervised, RL and adjoint training of the same network on one case
  except Sirignano & MacArt (2023, §5), who compare supervised and adjoint
  training (see
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
- **Fusion layer as printed.** Kim et al. (2024) describe the fusion
  network as having "two and one hidden layers before and after fusion"
  (§3.2, Fig. 5b), but Eq. 3.3 has after the fusion only the subtraction
  and the linear output layer, with no weights or activation in between.
  Their App. D gives the channel training grid as $16\times97\times16$ and,
  a few lines later and in the Fig. 19 caption, as $16\times49\times16$.
- **Energy conservation, two wordings.** van Gastelen et al. (2024) report
  energy conservation of their closure "up to machine precision
  (single-precision)" (§4.5, Fig. 9) and, in the conclusion, "up to a time
  discretization error" (§6). Eq. 37 is a semi-discrete identity; an
  explicit time integration conserves the energy only up to its
  time-integration error *(compiler check, not in the sources)*.
- **1D only.** The energy-conserving closure is demonstrated on Burgers
  and KdV, not on Navier–Stokes turbulence (van Gastelen et al. 2024, §5).
- **Scope and printed slips of Wu & Lele (2026).** The Smagorinsky
  coefficient 0.18 is not said to be $C_s$ rather than another
  convention, and no SSE is printed for the baselines in the compact
  solver. Table 1 names the local-normalization two-filter networks
  "ALN-L" and Tables 3–4 "Original-L"; the conclusion (§8) reverses the
  one-filter/two-filter comparison of the abstract and §4. The version
  read is the post-review arXiv v2, not the journal typesetting.
- **Deep-learning closures as seen from equation discovery.**
  [Jakhar et al. (2026)](/sources/jakhar-2026.md) (arXiv v3, p. 1) cite
  criticisms of deep-learning SGS closures (large training data, lack of
  interpretability, poor out-of-distribution generalization) and obtain
  their closure from 100 filtered-DNS snapshots by sparse regression (see
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)).
- **Notation.** Kang et al. write the third filter level of their
  two-parameter models as a tilde, which this bundle reserves for the
  Favre filter. Sirignano & MacArt write the adjoint variables with a
  hat, which this bundle reserves for the test filter, and use $G$ both
  for the filter kernel and for the gates.

# Citations

- [Kang et al. (2023)](/sources/kang-2023.md) — §1 (earlier costs), §2.4, Eqs. 2.9–2.10 (architecture, loss, normalization), §3.1, Tables 3–4, Figs. 4–8; §3.2, Figs. 10–17, Table 5; §3.3, Table 6, Figs. 19–22; §3.4, Figs. 23–24; §3.5, Tables 9–11, Figs. 25–29; §3.6, Fig. 30; §3.7, Figs. 31–32; App. A, Table 14; App. C; App. E.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §2, Eqs. 2.2–2.3; §2.1, Eq. 2.7; §4.2–§4.3, Figs. 8–10; §7.
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: §II C, §II E (actor, outputs, constraints, tensor basis).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §3.4, Fig. 4 (CNN policy, inputs), §4.2 (cost), §4.3, Fig. 7 (inputs compared).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A (networks for the SGS force, cited).
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §4.4.2 (CNN on the discrete commutator error).
- [Kim et al. (2024)](/sources/kim-2024.md) — §1, §2.2, §3.1–3.3, Table 2, Eqs. 3.1–3.3 (data, inputs, fusion architecture); §4.1–4.2, Table 3 (a priori, a posteriori, grids and Reynolds numbers); App. C (clipping on coarse grids); App. D (channel); App. E, Table 6 (cost).
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — arXiv v5: §3.1–3.3, Eqs. 33–50 (closure, SGS variables, momentum constraint); App. B, App. C; §4.2–4.8, Figs. 7–16; §5; §6.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §V (stabilization of a priori networks, from the literature).
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1, §3.1–3.2 (training input, pipeline, clipping); §6.1, Fig. 22; §7, Figs. 28–29 (Reynolds-number transfer, CNN grid dependence, pointwise inputs); App. C.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §I, §IV–V (neural operator replacing the LES solver).
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §2.5, §3 (physics-informed neural operator replacing the LES solver).
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §1, §2.1, §3–3.3, Eqs. 3.3–3.9, Figs. 1–4, Table 1 (model, filters, data); §5–6, Tables 3–4, Figs. 5–20 (a posteriori results); §7–8.
- [Li et al. (2021)](/sources/li-2021.md) — §I (earlier network SGS models surveyed); §III C, Figs. 2–8 (network of Xie et al. as comparator); §III F, Fig. 13 (cost).
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §4.3 (no machine-learned SGS model yet in turbomachinery simulations).
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — arXiv v3: p. 1 (criticisms of deep-learning closures, cited).
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §I (data-driven extensions of deconvolution, cited); Table VII (a priori level of non-learned deconvolution).
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §II.C, Table I (coefficients of the earlier network reproduced); §III, App. A, Eqs. 15–23, Table II (SGM-7-19 from the network pattern, a priori correlations); §IV–V, Table V (a posteriori, cost, backscatter clipping).
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §4.1.4, Eq. 72, Fig. 31 (learned reacting-flow closures reviewed; a priori against a posteriori caution); §6.
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §I (data-driven models and real-gas subgrid terms).
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — §I (neural-network models surveyed, in passing).
- [Xu et al. (2023)](/sources/xu-2023.md) — §1 (cited costs, black-box networks); §2.1–2.2, Figs. 1–3 (equations, baselines); §3.1–3.3, Tables 1–2, Eqs. 3.19–3.43, Figs. 4–12 (variants, network, training, a priori); §4, Tables 3–8, Figs. 13–31 (a posteriori, backscatter, cost); §5; App., Figs. 32–33.
- [Kumar et al. (2023)](/sources/kumar-2023.md) — §3.4, Fig. 5 (passing: networks for principal-component thermochemistry terms, not a subgrid closure).
- [Nista et al. (2023)](/sources/nista-2023.md) — §1 (network closures of reacting LES, a priori successes cited); §4.1–4.2, §4.4 ($\Delta/\eta$ generalization criterion, a priori only).
