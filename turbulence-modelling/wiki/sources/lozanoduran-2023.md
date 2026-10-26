---
type: Source
title: "Lozano-Durán & Bae (2023) — Machine learning building-block-flow wall model for large-eddy simulation"
description: "Introduces the building-block-flow wall model: a neural-network classifier and per-regime predictors, trained on solver-consistent wall-modelled LES of seven canonical flows, that return the wall stress with a confidence score; validated a posteriori from laminar boundary layers to the NASA high-lift and Juncture Flow models."
resource: "doi:10.1017/jfm.2023.331"
source_kind: paper
authors: [Lozano-Durán A., Bae H.J.]
year: 2023
venue: "J. Fluid Mech. 963:A35"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Fluid_Mechanics_Lozano-Durán_Machine_learning_building-block-flow_wall_model_for_large-ed.pdf"
tags: [wall-model, wmles, machine-learning, neural-network, high-lift]
timestamp: 2026-10-26T07:39:00Z
---

# Summary

Lozano-Durán & Bae (2023) propose the
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
(BFWM) for [wall-modelled LES](/methods/wall-modelled-les.md), the full form
of a preliminary 2020 version and a member of the
[machine-learning wall models](/methods/machine-learning-wall-model.md).
The premise is that a finite set of simple canonical flows contains the
near-wall physics needed to predict the wall stress of complex flows, and
that the missing near-wall subgrid effect is a probability-weighted
combination of the building blocks. The seven blocks are freestream, laminar
channel, turbulent [channel](/benchmarks/turbulent-channel-flow.md), turbulent
Poiseuille–Couette flow under favourable and adverse pressure gradient and at
separation, and a channel with a sudden spanwise pressure gradient; the
database draws on about 500 [DNS](/definitions/direct-numerical-simulation.md).
Six dimensionless inputs from a two-point wall-normal stencil feed a
classifier, which gives the probability of each block, and one predictor per
block; a nearest-neighbour confidence score accompanies each prediction,
explicitly not an error bound (a point of
[model-form uncertainty](/definitions/model-form-uncertainty.md)).

Training data are not filtered DNS but wall-modelled LES in the target solver
[CharLES](/software/charles.md) with a mean-exact SGS correction and a wall
boundary condition sampled from the DNS wall-stress distribution, so that the
model is consistent with the solver's numerical errors and grids, a
[discretization-consistent](/definitions/discretization-consistent-closure.md)
choice argued against [a priori](/definitions/a-priori-and-a-posteriori-testing.md)
training on filtered DNS; the model must be retrained for each solver.
Validation is a posteriori with the dynamic [Smagorinsky](/methods/smagorinsky-model.md)
model ([dynamic procedure](/methods/dynamic-procedure.md)) and the
[Vreman](/methods/vreman-model.md) model, against the algebraic
[equilibrium wall model](/methods/equilibrium-wall-model.md) built on the
[law of the wall](/definitions/law-of-the-wall.md): laminar and
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md), pipe
flow at $Re_\tau\approx40\,000$, Poiseuille–Couette flows, the spanwise-forced
channel, the NASA CRM-HL high-lift model and the
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md) on a
[boundary-layer-conforming grid](/methods/boundary-layer-conforming-grid.md).
Errors are split into internal (wall model) and external (SGS model at the
input point). The BFWM cuts internal errors and matches or beats the
equilibrium model, but external SGS errors dominate the total; the authors
conclude that better wall-modelled LES requires better SGS models.
"Implicitly filtered LES" in the paper means grid-implied filtering with an
explicit SGS model, not [implicit LES](/definitions/implicit-les.md) without
a model; the [LES](/definitions/large-eddy-simulation.md) filter question it
raises is that of the SGS tensor of such simulations. The solver is
kinetic-energy conserving ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
and the cost argument cites the [grid-point requirements](/results/les-grid-point-requirements.md)
of wall-resolved and wall-modelled LES.

# Version read

Version of record (Cambridge University Press, open access CC BY 4.0;
received 13 December 2022, accepted 31 March 2023), 34 pages (A35-1 to
A35-34), all read; equation pages checked visually where text extraction
lost symbols. Page 1 matches the Crossref record. Equation, section, figure
and table numbers on this page are those of the version of record.

# Key claims

Page-local symbols: $Re_{y,1}=u_1y_1/\nu$ and $Re_{y,2}=u_2y_2/\nu$ are the
local Reynolds numbers (registry §11 $Re_y$) at the first and second
off-wall control volumes, $u_1$, $u_2$ the wall-parallel velocity magnitudes
there; $\varphi_{12}$ the angle between the two velocities and
$\varphi_{1w}$ that between the first velocity and the wall stress (the
source's $\gamma_{12}$, $\gamma_{1w}$); $Re_P$, $Re_U$ the
pressure-gradient and moving-wall Reynolds numbers; $G_{zx}$ the ratio of
spanwise to streamwise mean pressure gradient; $\mathcal A_1$ the acceleration
magnitude and $\dot\varphi_1$ the angular rate of the first-point velocity;
$\check u_1$ the exponentially time-averaged $u_1$; $p_i$ the class
probabilities; $e_{\tau_w}$ the relative wall-stress error (the symbols of the
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
page).

1. A finite set of simple building-block flows contains the essential physics for generalizable wall models; the effect of the missing near-wall SGS in wall-modelled LES of complex flows is a linear combination of the near-wall behaviour of the building blocks (§2.2, assumptions (i)–(ii)). **Stated**
2. Six parameters determine the wall stress of each building block ($Re_\tau$ or $Re_P$, $Re_U$, $G_{zx}$, $tu_\tau/\delta$, turbulent or not, laminar or freestream), and correspondingly six dimensionless local inputs are fed to the model: $Re_{y,1}$, $Re_{y,2}$, $\varphi_{12}$, $\mathcal A_1y_1^3/\nu^2$, $\dot\varphi_1y_1^2/\nu$, $k_1/k_{m1}$ (§2.2, §2.3, Eq. 2.3). **Stated**
3. A two-point stencil suffices; the seven-point stencil of Lozano-Durán & Bae (2020) "greatly complicated the model implementation without providing important benefits" (§2.2). **Stated**
4. The DNS database for the turbulent blocks holds roughly 500 simulations (§2.3). **Stated**
5. Training on wall-modelled LES with a mean-exact SGS correction and an exact wall-stress boundary condition in the target solver guarantees consistency with the solver's numerical errors and grids, unlike filtered DNS, because the SGS tensor of implicitly filtered LES does not coincide with the stress of the filtered Navier–Stokes equations (§2.5). **Stated** (argued, cited)
6. Training grids are isotropic with $\delta/\Delta=5,10,20,40,80,160,380$, and finer grids are trained on DNS so that the model converges to no-slip; runs last 10 eddy-turnover times $\delta/u_\tau$, and shortening them below 3 "significantly reduced the performance of the ANNs"; 1000–10 000 snapshots per case; the mean-flow direction is rotated from −45° to 45° in 5° steps to augment the data (§2.6). **Stated** (training-length finding not shown)
7. The classifier confusion matrix classifies most samples correctly, with intentional overlap between contiguous blocks; the only unintentional misclassification is zero-pressure-gradient samples labelled favourable (printed column precision 85.2% and 83.5%); freestream and laminar are 100% (Fig. 5, §2.6). **Shown**
8. Each network trained in about 12 h on 4 NVIDIA A100 GPUs; wall-modelled LES with the BFWM costs 1.1–1.3 times the same solver with the algebraic equilibrium model, without optimization (§2.6). **Shown** (reported timings)
9. Laminar boundary layer ($Re_x=10^4$–$10^6$): mean velocity within 5% for all four SGS/wall-model combinations; classified laminar with confidence near 100% except near the inlet, labelled freestream there with lower confidence; internal BFWM errors below 1% after the inflow transient, equilibrium-model errors always above 20% (§4.2, Fig. 8). **Shown**
10. In the laminar case the equilibrium-model runs benefit from cancellation of internal and external errors, and external SGS errors severely reduce the BFWM accuracy (§4.2, Fig. 8d). **Shown**
11. Zero-pressure-gradient turbulent boundary layer ($Re_\theta$ 800–2000): mean profiles deviate about 10–30% from DNS; classified correctly with almost 100% confidence over most of the domain, but as unsteady or adverse near the inlet with confidence falling from 40% to 20%; averaged internal wall-stress error below 0.5% (BFWM) against about 2% (equilibrium); total errors 5–15% for both (§4.3, Fig. 9). **Shown**
12. Pipe flow at $Re_\tau\approx40\,000$, beyond the $Re_\tau\le10\,000$ channel training range: classified as channel-like on all grids, confidence above 95% for $R/\Delta>5$ and below 60% at $R/\Delta\approx5$ (attributed to poor dynamic-Smagorinsky performance); internal errors below 5% for both wall models; total error 4–12%, mildly better with the BFWM; non-monotonic grid convergence (§4.4, Fig. 10). **Shown**
13. Poiseuille–Couette flows at $Re_U=14\,000$ (adverse $Re_P\times10^{-3}=-1.40$ to $-0.76$, favourable $1.02$ to $1.49$, $\delta/\Delta=10$): classification accurate with confidence above 90%; the BFWM beats the equilibrium model in internal errors under adverse gradient and separation; "ZPG cases are all predicted accurately by both wall models, with errors below 3 %" (§4.5, Figs. 11–12). **Shown**
14. Under adverse gradient and separation the equilibrium model has the smaller total error "for the wrong reasons": it underpredicts the wall stress while near-wall mean velocities are overpredicted; under favourable gradient the total error rises from 5% to 20% with increasing gradient for both models, the BFWM still better (§4.5). **Shown**
15. Channel with sudden spanwise pressure gradient ($G_{zx}=80$, initial $Re_\tau=700$, $\delta/\Delta=10$): mean flow within 5% at the second grid point; the classifier detects the change at $t=0$ with high confidence; internal BFWM errors below 1% at all times; the BFWM predicts the mild drop of the streamwise wall stress and the rise and fall of $\varphi_{1w}$, which the equilibrium model misses ($\varphi_{1w}=0$ by construction) (§4.6, Fig. 13). **Shown**
16. NASA CRM-HL ($Re=5.49\times10^6$ on the mean aerodynamic chord, $M_\infty=0.20$, 30 million points, 0–20 points per boundary-layer thickness, dynamic Smagorinsky, $7^\circ$ and $19^\circ$): the BFWM gives moderate improvements over the equilibrium model, especially near stall and most clearly in pitching moment; the exception is $C_L$ at low incidence, where the equilibrium model's better prediction is attributed to error cancellation ("it has been reported", no citation) (§4.7, Fig. 15). **Shown** / **Stated**
17. The BFWM "has never 'seen' an aircraft-like flow": the blocks deliberately exclude aerofoils, wings and bumps to avoid overfitting (§2.3, §4.7). **Stated**
18. CRM-HL confidence: below 20% at the leading edges of nacelle, slats and flaps (no points per boundary-layer thickness) and in the separated regions at the wing tip and near the root; random inputs give 0% (§4.7, Fig. 16). **Shown**
19. NASA Juncture Flow ($Re=2.4\times10^6$ on the Yehudi-break chord, $5^\circ$, 5 points per $\delta$): upstream fuselage classified 88% zero/12% favourable gradient with 98% confidence, errors below 2% for both models; wing–body juncture 52% adverse/41% zero/7% separation, confidence 82%, BFWM better; trailing-edge corner separation 56% separation, confidence 22%, BFWM better but "far from satisfactory" (Table 1, §4.8, Fig. 18). **Shown**
20. The trailing-edge separation bubble is $0.3\delta$ thick while $\Delta\approx0.2\delta$, one grid point across the bubble; external SGS errors dominate there (§4.8). **Shown**
21. The present BFWM is more accurate on the Juncture Flow than the preliminary 2020 version trained on filtered DNS (§4.8). **Stated** (no side-by-side data)
22. Internal errors can prevent wall-modelled LES from converging to DNS under grid refinement until the grid is DNS-like (§4.1). **Stated**
23. The main limit of BFWM accuracy is the external error of the SGS model; a better wall model alone does not suffice unless the SGS model also improves (§4.7, §5(4), §6). **Shown** (across cases)
24. Ling et al. (2022) extended the building-block approach to the SGS model and greatly improved the CRM-HL $C_L$, $C_D$ and $C_M$ (§5(4), §6). **Stated**
25. The confidence score measures similarity to the training data, not an error bound: low confidence may still give accurate predictions and vice versa (§5(2)). **Stated**
26. The BFWM must be retrained for each flow solver, because consistency with numerics and grids is solver-dependent (§5(3)). **Stated**
27. Performance is controlled mainly by the physical assumptions, not by the network architecture; feed-forward networks of 5 hidden layers with 20–30 neurons gave accurate results but may be far from optimal (§5(5), §6). **Stated**
28. The BFWM has no specific mechanism for laminar-to-turbulent transition (§5(1)). **Stated**

The models in registry notation: the prediction is the class-weighted sum
$\tau_wy_1/(\mu\check u_1)=\sum_ip_i\,\tau^{(i)}_wy_1/(\mu\check u_1)$,
$\varphi_{1w}=\sum_ip_i\varphi^{(i)}_{1w}$ (Eq. 2.6), with
$\check u_1$ an exponential time average; the mean-exact SGS stress is
$\tau^{\mathrm{ESGS}}_{ij}=\tau^{\mathrm{base}}_{ij}+\Delta\tau_{ij}$, the correction forcing
the plane-averaged velocity to the DNS mean (Eq. 2.5); the equilibrium model
uses $u^+=y^++a_1(y^+)^2$ for $y^+<23$ and $u^+=\kappa^{-1}\ln y^++B$ above,
$\kappa=0.41$, $B=5.2$, with the input velocity at the second grid point
(Eq. 3.1).

# Printed slips

- **§2.1:** the requirement list is numbered "(i) … (ii) … (ii) … (iv)" (p. A35-5).
- **§2.3, item (5):** "the ratio of streamwise to spanwise mean pressure gradients $\Pi=(dP/dz)/(dP/dx)$", while the formula is spanwise over streamwise and §4.6 says "The ratio of spanwise to streamwise mean pressure gradient is $\Pi=80$".
- **§4.5:** "these validation cases are not included in the training or testing set discussed in § 2.5"; the training and test sets are discussed in §2.6.
- **§4.5:** "ZPG cases are all predicted accurately by both wall models, with errors below 3 %", in a section that contains only adverse, separated and favourable cases.
- **Training ranges against printed cases:** §2.3 states training for $Re_U$ from $5\times10^3$ to $2\times10^4$ and $Re_P$ from $-1.2\times10^3$ to $1.2\times10^3$; the Fig. 3(b,c) captions show building-block DNS at $Re_U=22\,360$, and the §4.5 validation uses $Re_P\times10^{-3}$ down to $-1.40$ and up to $1.49$.
- **§2.6:** "the lost function" (loss).
- **Symbol reuse:** $a_1$ is the acceleration input (Eq. 2.1) and the polynomial coefficient of the equilibrium model (Eq. 3.1); $N$ is the number of inputs (§2.2), the grid parameter $\Delta=h/N$ and the samples per category (§2.6).
- **Fig. 9 caption:** repeats the profile shift "$u/U_\infty=(x/L_0-1)/5$" of the Fig. 8 caption.
- **References:** two entries are labelled "Lozano-Durán & Bae 2019a" (J. Fluid Mech. 868 and J. Comput. Phys. 392), while §4.4 cites a "2019b" with no matching label; the entry "LOZANO-DURÁN, A. ÁN & ARRANZ, G. 2022" is cited in the text (§5(2)) as "Lozano-Durán & Adrián 2022", and the same "A. ÁN" appears in Vinuesa et al. (2022); "POINSOT, T.J & LELEF, S.K 1992".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x,y,z$ (building blocks) | $x,y,z$ | §4.8 (Juncture Flow): $y$ spanwise, $z$ vertical; **collision** with the registry's wall-normal $y$ |
| $y_\perp$, $y_\perp^+$ | $y$, $y^+$ | local wall-normal coordinate (Eq. 3.1) |
| $h$ | $\delta$ | channel half-height; **collision:** $h$ is the element size |
| $u_1y_1/\nu$, $u_2y_2/\nu$ | $Re_{y,1}$, $Re_{y,2}$ | local Reynolds numbers (registry §11) |
| $\gamma_{12}$, $\gamma_{1w}$, $\dot\gamma_1$ | $\varphi_{12}$, $\varphi_{1w}$, $\dot\varphi_1$ (page-local) | angles and angular rate; **collision:** $\gamma$ is the ratio of specific heats |
| $a_1$ (Eq. 2.1); $a_1$ (Eq. 3.1) | $\mathcal A_1$ (page-local acceleration magnitude at the first control volume); $a_1$ (equilibrium-model coefficient) | overloaded in the source |
| $k_1$, $k_{m1}$ | $k$ (at the first point), (mean kinetic energy there) | relative to the wall |
| $\bar{(\cdot)}$ | $\check{(\cdot)}$ (page-local exponential time average, time scale $10\Delta/\sqrt{k_{m1}}$) | **collision:** the overbar is the LES filter |
| $\langle\cdot\rangle_{xz}$, $\langle\cdot\rangle_{xzt}$ | $\langle\cdot\rangle$ | averages over homogeneous directions (and time) |
| $\Delta$; $N$ in $\Delta=h/N$ | $\Delta$; $n$ (page-local), $\Delta=\delta/n$ | cube root of the control volume, the implicit filter width; isotropic training grids $n=5$–$380$; **collision:** $N$ is the polynomial degree |
| $Re_P=\pm\sqrt{\lvert dP/dx\rvert/\rho}\,h/\nu$, $Re_U=U_th/\nu$ | $Re_P$, $Re_U$ (page-local) | + favourable, − adverse |
| $\Pi=(dP/dz)/(dP/dx)$ | $G_{zx}$ (page-local) | **collision:** $\Pi$ is the SGS energy flux |
| $p^i_{class}$, $p_{conf}$, $d_i$, $d_s$ | $p_i$, $p_{\mathrm{conf}}$, $d_{\mathrm{in}}$, $d_s$ (page-local) | class probability, confidence from $d_s/d_{\mathrm{in}}$ clipped at 1 |
| $\boldsymbol w_c$, $\boldsymbol w_p$ | $\boldsymbol\theta$ | classifier and predictor weights |
| $\tau^{ESGS}_{ij}$, $\tau^{base}_{ij}$, $\Delta\tau^{SGS}_{ij}$ | $\tau^{\mathrm{ESGS}}_{ij}$, $\tau^{\mathrm{base}}_{ij}$, $\Delta\tau_{ij}$ (page-local) | no sign or trace convention printed |
| $\tau_w$ | $\tau_w$ | magnitude of the wall-stress vector |
| $\kappa=0.41$, $B=5.2$ | $\kappa$, $B$ | as printed |
| $\epsilon_{\tau_w}$ | $e_{\tau_w}$ | relative wall-stress error (registry §11 $e_q$); definition not printed |
| $Re_x$, $Re_\theta$, $\delta_i$, $\delta_o$ | $Re_x$, $Re_\theta$, $\delta_{99}$ at inlet and outlet | |
| $R$, $U_{cl}$ | (pipe radius, centreline velocity) | |
| $C_L$, $C_D$, $C_M$ | $C_L$, $C_D$, (pitching-moment coefficient) | |

# Reference list

91 printed references, author–year (JFM) style. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug.
Lozano-Durán, Bose & Moin (2022) is the ingested
[lozanoduran-2022](/sources/lozanoduran-2022.md); Lozano-Durán & Arranz
(2022, Phys. Rev. Res.) is a different work, keyed `lozanoduran-2022-b`. Also
ingested: [bae-2022](/sources/bae-2022.md),
[duraisamy-2019](/sources/duraisamy-2019.md),
[duraisamy-2021](/sources/duraisamy-2021.md) and
[goc-2021](/sources/goc-2021.md). Printed irregularities: the label
"Lozano-Durán & Bae 2019a" is used twice; a garbled co-author "A. ÁN" in two
entries; Towne et al. (2022, accepted, arXiv) and Bae & Lozano-Durán (2022,
arXiv preprint) stay separate preprint entries; GMGW-HLPW (2022) has a
corporate author.

# Pages created or updated

Chunk 4 (2026-10-26). This source is cited on:

- [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Boundary-layer-conforming grids for wall-modelled LES](/methods/boundary-layer-conforming-grid.md)
- [Building-block-flow wall model](/methods/building-block-flow-wall-model.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Machine-learning wall models](/methods/machine-learning-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Vreman model](/methods/vreman-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [CharLES](/software/charles.md)
