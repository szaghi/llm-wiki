---
type: Benchmark
title: "Periodic hill"
description: "The streamwise-periodic channel with a hill constriction, a smooth-wall separation and reattachment test: at hill-height Reynolds number about 10,600 for hybrid RANS/LES, implicit LES and learned RANS corrections, at 5600 for finite-element implicit LES and, as a parametrized family, learned RANS corrections, and at 2800 for data assimilation and DG and gas-kinetic implicit LES."
status: established
aliases: [periodic hills, ERCOFTAC UFR 3-30, Fröhlich periodic hill, hill flow, parametrized periodic hills]
tags: [benchmark, separated-flow, hybrid-rans-les, pans, data-driven, field-inversion, implicit-les, gas-kinetic]
timestamp: 2026-10-26T15:57:00Z
---

# Periodic hill

A channel whose lower wall carries a series of smooth constrictions (hills)
of height $h$, simulated over one hill-to-hill period with periodic
streamwise and spanwise boundaries and no-slip walls at top and bottom. The
flow separates from the hill crest on a curved surface and reattaches on the
floor, so it tests the prediction of smooth-body separation, of the
reattachment length and of the Reynolds stresses in a separated shear layer
without the ambiguity of an inflow condition. The Reynolds number $Re_h$ is
built on the bulk velocity and $h$. In this bundle it serves three purposes:
a coarse-grid test of hybrid RANS/LES and of high-order implicit LES, and a
training and testing case for data-driven RANS corrections and wall models.
The sources use three Reynolds numbers, each with its own reference data:
$Re_h\approx10{,}600$ (the configuration of Fröhlich et al. and ERCOFTAC),
5600 (the parametrized family of Xiao et al.), and 2800; the ingested sources
do not relate the three. [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md)
add the configuration of Fröhlich et al. ($9h\times3.035h\times4.5h$) itself
at $Re_h=5600$, 10,600 and 37,000, against the experiment of Rapp and,
at the first two, the LES of Breuer et al., so that this geometry, not the
parametrized family, is also run at 5600.

## Configuration

| Item | [Dzanic et al. (2022)](/sources/dzanic-2022.md) | [Haering et al. (2022)](/sources/haering-2022.md) |
|---|---|---|
| Name of the configuration | that of Fröhlich et al. (§3.1) | ERCOFTAC UFR 3-30 (§V B) |
| Reynolds number | $Re_h=10{,}595$ (bulk velocity, $h$) | $Re_h=10{,}600$ |
| Period (streamwise length) | crest-to-crest $9h$ | "single peak-to-peak period", printed $9.5h$ (see Qualifications) |
| Height, span | $3.035h$, $4.5h$ | $3.035h$, $4.5h$ |
| Flow-rate control | pressure-gradient controller at constant mass flow, Eq. (25) | bulk-velocity body force, applied only for $y>1$ |
| Mach number | 0.1 (compressible solver) | incompressible solver |
| Statistics | 20 flow-throughs, last 10 averaged, plus spanwise averaging | 50 samples over 20 flow-throughs |
| Reference data | LES of Fröhlich et al. | experiment of Rapp & Manhart; wall-resolved LES of Breuer et al. (dynamic Smagorinsky, over 13M cells) |

The Reynolds numbers differ only by rounding. The printed period lengths
differ ($9h$ against $9.5h$); see Qualifications.

## Runs

**Hybrid RANS/LES on coarse grids.**
[Haering et al. (2022)](/sources/haering-2022.md), §V B, Table II, Figs.
9–12, run the [active model split](/methods/active-model-split.md) method
with the $\overline{v^2}$–$f$ base model on three grids. They put the first
point at $\Delta y^+\approx1$ at the bottom wall and about 2 at the top, in
wall units built from $u_\tau$ at the hill top:

| Grid | $N_x\times N_y\times N_z$ | $\Delta x^+$ (mean) | $\Delta z^+$ | Cells | Reduction against WRLES |
|---|---|---|---|---|---|
| Fine | $190\times120\times40$ | 47 | 112 | about 0.9M | 14 |
| Medium | $140\times120\times30$ | 63 | 150 | about 0.5M | 25 |
| Coarse | $95\times110\times20$ | 95 | 225 | about 0.2M | 62 |

Steady RANS reattaches at about $x=7$ (in units of $h$) against a
reference value of about $x=4$. The hybrid model brings reattachment and the
mean streamwise velocity close to experiment and wall-resolved LES at all
three resolutions. The medium and fine grids give nearly the same
reattachment length. The vertical velocity at $x=0.5$ and $1.0$ stays close
to RANS, because the separating shear layer is still almost fully modelled
there. The fine grid over-predicts $\langle u'u'\rangle$ and $\langle
v'v'\rangle$ in the recirculation region. The authors state a cost reduction
"by a factor of 30 or more due to larger timesteps" against the wall-resolved
LES, without timings. They also estimate that wall-modelled LES of the hill
(grid sizes no larger than 8%, 2% and 5% of $\delta$ in the streamwise,
spanwise and wall-normal directions) would need about 12M cells on a
structured grid, or about 1.6M with a streamwise-varying grid, both above
the 0.9M of their fine grid (§V B). Lowering the resolution coefficient to
$C_r=0.2$ on the coarse grid gives the best mean velocity, through error
cancellation, with over-predicted stresses (§V C).

**High-order PANS and implicit LES at equal degrees of freedom.**
[Dzanic et al. (2022)](/sources/dzanic-2022.md), §3.1, Table 1, Figs. 3–6,
compare [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
(with the [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) closure,
$f_k=0.2$ and $0.3$) and no-model under-resolved DNS, which they equate
with [implicit LES](/definitions/implicit-les.md), on flux-reconstruction
grids of $64\times64\times32$ degrees of freedom: $N=1$ on
$32\times32\times16$ elements ($\Delta y^+=1.8$) and $N=3$ on
$16\times16\times8$ elements ($\Delta y^+=1.0$, with $\Delta y^+$ estimated
from a flat-plate friction velocity). The grids carry 97% fewer degrees of
freedom than the reference LES and 85% fewer than an earlier low-order PANS.
The authors state that $f_k<0.2$ is not supported at this resolution.
Results:

- at $N=1$ both PANS and the no-model run over-predict reversed flow in
  $0\le x\le5$; at $N=3$ both improve, and PANS with $f_k=0.2$ agrees
  "excellently" with the reference mean velocity;
- $\langle u'u'\rangle$: the no-model run over-predicts it at both orders,
  while PANS improves markedly from $N=1$ to $N=3$;
- $\langle v'v'\rangle$ and $\langle u'v'\rangle$: the $N=3$ no-model run
  shows large spurious oscillations, which the authors attribute to aliasing
  in under-resolved high-order schemes; high-order PANS does not, which they
  attribute to the eddy viscosity of the model;
- the spread between the two $f_k$ values is smaller at $N=3$.

The authors read the comparison as evidence that the lower
[numerical dissipation](/properties/numerical-dissipation.md) of high-order
schemes benefits a hybrid model more than a no-model simulation.

**Data-driven RANS corrections.** As recalled by
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.3, Figs. 6–7, the
random-forest Reynolds-stress discrepancy models of Wang et al. (2017) and
Wu et al. (2018b), trained on separated flows in other geometries (or on a
periodic hill of slightly different shape), improve the predicted
anisotropy and mean velocity on the periodic hill. The gene-expression
programming models of Weatheritt & Sandberg, trained on a backward-facing
step, show "a high level of uncertainty" on it. The review gives no
Reynolds number for these cases. See
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
and [model-form uncertainty](/definitions/model-form-uncertainty.md).

**Field inversion on the parametrized hill family.** A different
configuration from the one of the table above:
[Yan et al. (2022)](/sources/yan-2022.md), §3.2, use the DNS database of
Xiao et al. for periodic hills of parametrized geometry, in which the hill
width is scaled by a factor (written $\alpha_h$ here, page-local; the
source writes $\alpha$, which it also uses for the angle of attack) at fixed
hill height, at a Reynolds number of 5600 built on the crest height and the
bulk velocity at the crest. The cases are 2D steady RANS with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) on an
$81\times77$-point grid (shown for $\alpha_h=0.8$), with no-slip top and
bottom walls, periodic inflow and outflow, and a volume force adjusted to
hold the bulk velocity. [Field inversion](/methods/field-inversion-machine-learning.md)
multiplies the SA production by a field $\beta(\boldsymbol x)$ and fits DNS
mean-velocity profiles at stations (Eq. 17), with three regularizations
(Table 2): none, which gives an irregular correction field with no general
tendency; a weight $8\times10^{-6}$ with corrections confined to a box over
the separating shear layer; and the same weight everywhere. The two
regularized inversions give similar fields: production decreased at the
start of the separating shear layer and increased downstream, in the region
where the authors' earlier nonequilibrium modifier and Rumsey's separation
fix act (Figs. 11, 18). The inversion on velocity alone also improves the
lower-wall skin friction, which was not in the objective, and the separation at the
hill top and the reattachment (Figs. 16–17). A network with hidden layers
(32, 16, 8), trained on two geometries, reproduces the inversions and,
embedded in the solver, brings velocity profiles closer to DNS than baseline
SA at an interpolated width ($\alpha_h=1.0$) and at two extrapolated widths
(0.5, 1.5) "in most regions" (§3.2.2, Figs. 19–22). Yan et al. also recall
Rumsey's finding that enhanced mixing in the separated shear layer improves
the periodic hill but worsens backward-facing-step flows (§1; see
[backward-facing step](/benchmarks/backward-facing-step.md)).

**Machine-learning wall models.**
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §I and §IV B, recall
that the wall model of Zhou et al. was trained on channel and periodic-hill
data at $Re_h=5600$ to $10{,}595$ and was reported to perform well a priori
but poorly a posteriori on periodic hills. In their own a priori
law-of-the-wall tests the same network over-predicts the wall stress,
increasingly with $Re_\tau$ (§IV B, Fig. 12; see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).

**Learned eddy viscosity and anisotropy on the parametrized family.**
[McConkey et al. (2022)](/sources/mcconkey-2022.md) use the same DNS family
of Xiao et al. at $Re_h=5600$, with the steepness factor $\alpha_h=0.5$,
0.8, 1.0, 1.2, 1.5 (which in their description varies both the hill slope and
the domain length; 14,751 points per case), as base RANS runs with an
elliptic-relaxation model of the $v^2$-$f$ family (the $k$-$\varepsilon$-$\phi$-$f$ form) in OpenFOAM on wall-resolved
meshes (§II E–F, §III D). Even the eddy viscosity fitted to the DNS
anisotropy by least squares leaves errors of order 100% in every component of
the anisotropy at $\alpha_h=1.2$; the linear approximation fails for all
components during separation and for the wall-normal component also during
reattachment (§II B, Figs. 1–3). Injecting DNS-derived closure terms into the RANS equations
("conditioning" test), the fully explicit Reynolds-stress anisotropy gives a
streamwise-velocity RMSE of $2.613\times10^{-3}$ m/s, while the non-negative
fitted eddy viscosity treated implicitly plus the remaining anisotropy
treated explicitly gives $2.265\times10^{-4}$ m/s; the authors note that the
explicit run needed first-order schemes for stability (§II C, Figs. 5–6; see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). Two neural
networks trained on the other four geometries and injected once into the
converged base solution move the reattachment point from $x_R/h=5.42$ (base
model) to 4.10, against 4.50 in the DNS, errors of 20% and 8.9% (§IV B,
Fig. 21). The test geometry is an interpolation within the family.

**Data assimilation at $Re=2800$.** [Cato et al. (2023)](/sources/cato-2023.md),
§IV, assimilate a dense DNS mean-velocity field (they cite the DNS of
Gloerfelt & Cinnella and of Xiao et al. without saying which they use)
into steady 2D RANS with the negative Spalart–Allmaras variant, at a bulk
Reynolds number of 2800, by adjoint-based optimization of one
space-dependent corrector at a time (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
Relative errors in skin friction and mean velocity (Table II):

| Corrector | $E_{C_f}$ | $E_u$ |
|---|---|---|
| baseline RANS | 0.38 | $7.1\times10^{-2}$ |
| momentum forcing vector | 0.17 | $3.8\times10^{-3}$ |
| divergence of a trace-free symmetric tensor | 0.26 | $3.7\times10^{-3}$ |
| multiplier $\beta$ of SA production (prior 1; printed $1+\beta$ with prior 0) | 0.27 | $3.2\times10^{-2}$ |
| additive source in the SA equation | 0.23 | $7.8\times10^{-3}$ |
| source proportional to $\tilde\nu$ | 0.20 | $7.5\times10^{-3}$ |
| multiplier of $\nu_t$ in the momentum equation | 0.30 | $4.3\times10^{-2}$ |

The Boussinesq alignment indicator they use is below 0.8 in much of the
domain below one hill height, yet the two source-type correctors of the SA
equation recover the DNS velocity and skin friction; the authors conclude
that "missing the proper stress alignment does not play a large role for
predicting the mean flow" (§IV A–B, Figs. 8–10).

**Physics-informed networks at $Re=2800$.**
[Eivazi et al. (2022)](/sources/eivazi-2022.md), §3, Fig. 6, Table 1, solve
the 2D RANS equations with a
[physics-informed neural network](/methods/physics-informed-neural-network.md)
that outputs the mean velocity, pressure and the three Reynolds-stress
components, with no turbulence model: the loss combines the RANS residuals
with data on the boundaries only (velocity and Reynolds stresses at the inlet
and outlet of the subdomain $1<x/h<5$, pressure on all boundaries), taken from
a spectral-element DNS at a Reynolds number of 2800 on the crest height and
the bulk velocity at the crest. Relative $\ell_2$ errors are 2.77% for the
streamwise velocity, 19.70% for the wall-normal velocity, 8.61% for the
pressure, and 28.18%, 16.70% and 20.24% for $\langle u'u'\rangle$,
$\langle u'v'\rangle$ and $\langle v'v'\rangle$. The authors call the
separated region and the reattachment point "accurately predicted", judged
from figures; no reattachment length is printed.

**Symbolic-regression closure on the parametrized family.**
[Tang et al. (2023)](/sources/tang-2023.md) (read in arXiv v1) train a
[symbolic-regression closure](/methods/symbolic-regression-closure.md) for
the non-linear part of the Reynolds-stress anisotropy on the single hill
$\alpha_h=0.8$ of the Xiao et al. DNS family at $Re=5600$ (hill height),
and test it on $\alpha_h=0.5$ and 1.0 (§III A, D). The base model is the
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) in OpenFOAM
(SIMPLE, about 9600 cells, cyclic inlet and outlet, 20,000 iterations to a
residual of about $10^{-10}$, Table I); the learned term is computed once
from the converged baseline, frozen and injected, and the linear part is
re-converged (loose coupling, §II D). A priori on the training hill the
baseline gets the shear component of the anisotropy roughly right but the
diagonal components "far removed" from DNS near the bottom wall, while the
learned model "captures the correct sign" of all components, with the
largest gains for the streamwise and wall-normal normal components in the
separated region (§III C, Fig. 7). A posteriori the baseline
under-predicts the separation bubble and the learned model enlarges it
toward DNS (Fig. 9). On the test hills the anisotropy is "markedly
improved", the mean velocity improves on $\alpha_h=1.0$, but the
improvement in the recirculation region is "not distinguishable" on the
steeper $\alpha_h=0.5$, which the authors ascribe to its more severe
separation (§III D, Figs. 12–15). A second reward function yields a much
longer expression whose velocity field is "strikingly close" to that of the
first (§III E, Fig. 19).

**High-order DG implicit LES at $Re=2800$.**
[Lederer et al. (2023)](/sources/lederer-2023.md) (read in arXiv v1), §5,
run the geometry of Mellen, Fröhlich & Rodi with crest-to-crest length
$9h$, height $3.0335h$ and span $4.5h$, at $Re=2800$ on the bulk velocity
and $h$, with a dynamically controlled forcing, against the DNS of
Balakumar & Ilhwan. The discretization is the exactly divergence-free
hybridized mixed finite-element (MCS) method at $N=3$ on two curved meshes,
$12\times8\times6$ and $24\times16\times12$ elements (Table 3). Three
treatments are compared: [implicit LES](/definitions/implicit-les.md)
with upwind jump dissipation only, a projection-based variational
multiscale model with the [WALE](/methods/wale-model.md) eddy viscosity,
and the authors' adaptive
[high-order projection-based upwinding](/methods/high-order-projection-based-upwind-method.md),
which removes upwind dissipation from the low-order part of the velocity
jump. All three reproduce the mean streamwise velocity reasonably; on the
coarse mesh the adaptive upwinding improves the wall-normal velocity near
reattachment ($x=3h$, $5h$, $8h$) and markedly improves $\langle
v'v'\rangle$ and $\langle u'v'\rangle$, which the no-model run mostly
over-predicts, while the WALE model brings little or no improvement (§5.1,
Figs. 8–9). The jump indicator of the no-model run peaks near the
separation point and along the lower wall (Fig. 10).

**Symbolic-regression corrections of SST on the parametrized family.**
[Wu et al. (2025)](/sources/wu-2025.md), §4.1, test two corrections of the
$\omega$-destruction term of [$k$-$\omega$ SST](/methods/k-omega-sst-model.md),
fitted by [symbolic regression](/methods/symbolic-regression-closure.md)
to [field-inversion](/methods/field-inversion-machine-learning.md) data of a
curved backward-facing step and the
[NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md), on the
hills of Xiao et al. with width factors $\alpha_h=0.5$, 0.8 and 1.0 at
$Re=5600$, against the DNS of that database. The hill is therefore a test
of transfer to a new geometry, not a training case. Three grids with
$\Delta y^+<1$ (OpenFOAM simpleFoam) change the integrated friction
coefficient by less than $10^{-4}$, and by about $5\times10^{-5}$ between
medium and fine. For $\alpha_h=0.8$ baseline SST does not reattach before
the next hill, both corrected models reattach at about $x=6.0$ (in units
of the hill height), and the DNS at about 5.2 (Figs. 24–27). Both models
improve velocity profiles and $C_f$; the correction of the gated model
(SR-CND), switched off in attached boundary layers by the DDES shielding
function, sits in the separated shear layer, while that of the ungated
model (SR-CLS) is more diffuse and active near the attached upper wall
(§4.1).

**Expert blending at $Re_h=10{,}595$.**
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (arXiv v2), §4.2.3,
use the Fröhlich configuration ($Re_h=10{,}595$ on the hill height and the
bulk velocity at the crest, 2D steady RANS on a $120\times130$ grid, LES of
Breuer et al. and Temmerman et al. as reference) as one of three training
flows of a separated-flow correction of SST and of a learned
[blend of expert models](/methods/turbulence-model-aggregation.md).
Separation and reattachment, in $x/h$ (Table 6):

| Model | separation | reattachment | bubble length |
|---|---|---|---|
| LES | 0.21 | 4.7 | 4.49 |
| SST | 0.25 | 7.67 | 7.42 |
| separated-flow expert | 0.25 | 4.4 | 4.15 |
| jet expert | 0.25 | 8.23 | 7.98 |
| blend | 0.265 | 4.82 | 4.555 |

The blend has the lowest $C_f$ error ($2.07\times10^{-3}$ against
$2.37\times10^{-3}$ for SST and $2.65\times10^{-3}$ for the separated-flow
expert), while the separated-flow expert has the lowest velocity error
(0.06 against 0.09 for the blend and 1.37 for SST; Table 7).

**Compressible implicit LES with a gas-kinetic scheme at $Re=2800$.**
[Cao et al. (2024)](/sources/cao-2024.md) (read in arXiv v1), §3.4, run
the [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
on curvilinear meshes built from discrete points (bottom-wall points of
Gloerfelt & Cinnella) as an [implicit LES](/definitions/implicit-les.md),
with no subgrid model. The flow is compressible at $M=0.2$ (on the bulk
velocity), constant viscosity, $Pr=0.72$, isothermal walls, domain
$9h\times3.036h\times4.5h$; the target $Re=2800$ is held only to about
2730 because the mass flux varies over the cross-section (Fig. 12).
Separation and reattachment, in $x/h$ (Table 6):

| Run | cells | separation | reattachment |
|---|---|---|---|
| DNS, Peller & Manhart (incompressible, immersed boundary) | 47.68 M | 0.21 | 5.41 |
| LES with approximate deconvolution, Ziefle et al. | 0.64 M | 0.21 | 5.30 |
| H1, $100^3$ | 1.0 M | 0.23 | 5.18 |
| H2, $200\times100\times100$ | 2.0 M | 0.20 | 5.15 |
| H3, $400\times200\times200$ | 16.0 M | 0.24 | 5.52 |

The authors find $C_p$ closer to the DNS than the explicit LES, and state
that the explicit LES overpredicts the normalized Reynolds stresses,
especially the shear stress, so that "the explicit LES model may pollute"
this low-Reynolds-number separated flow, while the implicit LES agrees
with the DNS (Figs. 14–16). They note in the same paragraph that the
explicit-LES statistics are density-weighted while the DNS and implicit-LES
ones are not. H3 improves the Reynolds stresses, but the authors judge the
improvement not worth its cost and conclude that coarse grids suffice for
implicit LES of low-Reynolds-number separated flows (§3.4).

**Stabilized finite-element implicit LES at $Re_h=5600$, 10,600 and 37,000.**
[Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) run the
open-source code Lethe, continuous-Galerkin $Q_1$–$Q_1$ finite elements
with SUPG/PSPG stabilization and implicit BDF2 time stepping, with no SGS
model: the stabilization term, a stabilization parameter times the strong
momentum residual, is the only added dissipation, which they call
[implicit LES](/definitions/implicit-les.md) (§1, §2). The domain is
$9h\times3.035h\times4.5h$ with a flow-rate controller; one flow-through
takes 9 s in their units, and statistics start after 207 s. The meshes
have $2.5\times10^5$ (coarse), $5\times10^5$, $10^6$ (regular) and
$4\times10^6$ (fine) hexahedra, 1.1 to 16 million degrees of freedom,
against 12.4 million cells of the reference LES of Breuer et al. (Tables
1, 4). At $Re_h=5600$ the averaged $\Delta y^+$ is 1.66, 1.16 and 0.61,
$\Delta x^+$ 2.96, 2.40, 1.39 and $\Delta z^+$ 4.20, 2.26, 1.51 on the
coarse, regular and fine meshes, with $\Delta y^+$ built on half the
distance of the wall-nearest node (App. B, Table B.6).

- **Validation.** Mean velocity and Reynolds stresses agree well with the
  experiment of Rapp and the LES of Breuer et al. (§4.1, Figs. 4–5).
- **Time step.** Reattachment points $x_R/h$, with the CFL number in
  parentheses (Table 5; Rapp 4.83, Breuer et al. 5.09):

| $\Delta t$ [s] | coarse | regular | fine |
|---|---|---|---|
| 0.1 | 4.73 (2.2) | 4.40 (3.2) | 4.35 (5.1) |
| 0.05 | 4.87 (0.9) | 4.59 (1.6) | 4.74 (2.8) |
| 0.025 | 5.07 (0.5) | 4.80 (0.7) | 4.83 (1.2) |
| 0.0125 | 5.37 (0.2) | 4.88 (0.4) | 4.85 (0.6) |

  On the coarse mesh a smaller time step degrades the mean velocity and
  above all the Reynolds stresses, which the authors explain by the
  stabilization parameter decreasing with $\Delta t$ and so removing
  dissipation; on the fine mesh all time steps except the largest give
  similar results close to Breuer et al., even at CFL ≈ 2.8 (§4.2,
  Figs. 6–8).
- **Averaging.** Profiles change very little between averaging end times
  of 500 and 1000 s; error bands of the reattachment point by the
  $\pm c/\sqrt{T}$ method of Krank et al. shrink markedly after 500 to 600
  s, from which the authors require at least 700 s (§4.3, Fig. 12). The
  reattachment point approaches the experiment non-monotonically with mesh
  refinement, and the $10^6$- and $4\times10^6$-cell meshes give very close
  values (§4.3, §5).
- **Higher Reynolds numbers** ($\Delta t=0.025$ s, 800 s of averaging; very
  coarse $1.2\times10^5$, coarse and intermediate meshes): at
  $Re_h=10{,}600$ reattachment at 4.54, 4.90 and 4.01 against Rapp 4.21 and
  Breuer et al. 4.69, good mean velocity and over-predicted Reynolds
  stresses; at 37,000 reattachment at 4.20, 4.09 and 3.49 against Rapp
  3.76, velocity under-predicted in the lower and over-predicted in the
  upper channel, and all Reynolds stresses over-predicted (§4.4,
  Figs. 13–16).
- **Cost** on 40-core Skylake nodes: 3647 to 9400 core-hours on the coarse
  mesh and 116,667 to 188,000 on the fine mesh for 1000 s at $Re_h=5600$,
  depending on the time step (App. C, Table C.9). The authors leave a
  comparison with explicit time stepping out of scope and conclude, without
  an equal-accuracy cost comparison, that implicit LES "can reduce the
  computational effort" (§5).

**Upwind against central convection in LES at $Re_h=10{,}595$.**
[Wang et al. (2024)](/sources/wang-2024.md), §3.3, run LES with the
[WALE model](/methods/wale-model.md) at $M=0.2$ on grids of $48^3$,
$64^3$, $96^3$ and $196\times128\times186$ cells, with about 100
flow-through times averaged, comparing the second-order
kinetic-energy-preserving split form KGP2 (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md))
with OPT6, the linear sixth-order optimized upwind reconstruction with a Roe
flux. The separation point $x/h$ is (Table 2):

| Grid or reference | KGP2 | OPT6 |
|---|---|---|
| $48^3$ | 0.26 | — |
| $64^3$ | 0.24 | — |
| $96^3$ | 0.20 | — |
| $196\times128\times186$ | 0.20 | 0.20 |
| DNS of Krank et al. / LES of Breuer et al. / LES of Fröhlich et al. (as cited) | 0.20 / 0.19 / 0.22 | |

First-order statistics change little with the grid, second-order statistics
and the terms of the turbulent-kinetic-energy budget do; OPT6 agrees with
the references "even in $48^3$ grids", above all in the budget balance,
while KGP2 converges with refinement. The authors read a budget imbalance as
a sign of insufficient resolution and recommend the high-order upwind
scheme for budget analysis (§3.3, §5, Figs. 5–6); see
[numerical dissipation](/properties/numerical-dissipation.md). The two
schemes differ in order of accuracy (second against sixth) as well as in
dissipation (§2.3–2.5).

## What the case shows

Two sources agree that the case discriminates between models chiefly
through the separated region: the reattachment point and the Reynolds
stresses in the recirculation bubble. The hybrid results of
[Haering et al. (2022)](/sources/haering-2022.md) and the high-order PANS
results of [Dzanic et al. (2022)](/sources/dzanic-2022.md) both reach
reference-level mean velocity on grids one to two orders of magnitude
smaller than wall-resolved LES, while second-order statistics remain the
sensitive quantity (excess stresses in the bubble on the finest hybrid grid;
oscillatory stresses in high-order no-model runs). See also
[hybrid RANS/LES](/definitions/hybrid-rans-les.md).

Two of the data-driven RANS studies state a related point: on the hill, a
good mean velocity does not require a correct Reynolds-stress tensor.
[Cato et al. (2023)](/sources/cato-2023.md) recover velocity and skin
friction with eddy-viscosity-type correctors where the stresses are poorly
aligned with the strain; [McConkey et al. (2022)](/sources/mcconkey-2022.md)
find the velocity errors after injection smaller than the errors of the
injected closure term and conclude that "the RANS equations can suppress
rather than amplify errors in the closure prediction" (§IV B, Fig. 20).
[Eivazi et al. (2022)](/sources/eivazi-2022.md), Table 1, make no such
statement; their streamwise-velocity error is 2.77% against Reynolds-stress
errors of 16.7% to 28.2%. [Tang et al. (2023)](/sources/tang-2023.md),
§III E, report the same insensitivity between two learned closures of very
different form, and explain it by the mean velocity being a first-order
statistic and the Reynolds stress a "less converged" second-order one.

On the scale-resolving side, two sources report no-model high-order runs
whose Reynolds stresses miss the reference while the mean velocity is
reasonable: [Lederer et al. (2023)](/sources/lederer-2023.md), §5.1, find
the Reynolds stresses of their coarse runs mostly over-estimated and
reduce the error with adaptive high-order projection-based upwinding, which
their jump indicator places near the separation point and the lower wall,
while the WALE model gives slight to no improvement; at $Re_h\approx10{,}600$
the $N=3$ no-model run of [Dzanic et al. (2022)](/sources/dzanic-2022.md)
over-predicts $\langle u'u'\rangle$ and oscillates in $\langle v'v'\rangle$
and $\langle u'v'\rangle$, which PANS removes.

Three sources now give the reattachment or separation of the Fröhlich
configuration against the same references: at $Re_h\approx10{,}600$
Haering et al. quote a reference reattachment of about $x=4$, Prieto
Saavedra et al. print Rapp 4.21 and Breuer et al. 4.69, and Wang et al.
print the separation point (0.19 to 0.22 across the cited references). In
the two studies that vary the grid at $Re_h\approx10{,}600$, the mean
velocity is good on all grids, while the Reynolds stresses are
over-predicted ([Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md), §4.4)
or, with the budget terms, depend on the grid and the scheme
([Wang et al. (2024)](/sources/wang-2024.md), §3.3).

## Qualifications

- The reattachment of [Cao et al. (2024)](/sources/cao-2024.md) does not
  change monotonically with the grid (H1 5.18, H2 5.15, H3 5.52 against DNS
  5.41; Table 6), and their conclusion that coarse grids suffice is drawn
  from H1 and H2 (§3.4). They normalize $C_f$ and $C_p$ by
  $\langle\rho_b\rangle\langle U_b\rangle^2$, without the factor
  $\tfrac12$ (§3.4), so their values are twice those normalized with it.
  Their printed wall-normal mapping
  $y=\tfrac{3-y_0}{2}\tanh(b_g(\eta/1.5\pi-1))/\tanh(b_g)+\tfrac{3+y_0}{2}$,
  on the printed computational range $\eta\in[-1.5\pi,1.5\pi]$, gives
  $y=(3+y_0)/2$ at $\eta=1.5\pi$, not the top wall of the
  $3.036h$-high domain *(compiler check, not in the sources)*.
- [Wu et al. (2025)](/sources/wu-2025.md) print the integrated friction
  coefficient (Eq. 21) as the integral of $C_f$ divided by
  $\tfrac12\rho U_b^2L$, dimensionally inconsistent unless the integrand
  is the wall shear stress *(compiler check, not in the sources)*.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) give the reference
  length of the hill as the hill height (Table 5, Fig. 9) but as "the
  channel half-height (full channel height $=2L$)" in the Fig. 7 caption.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) call the
  value 5.09 of Breuer et al. "experimental" in the Table 5 caption,
  although it is the LES value; print the fine-mesh uncertainties as
  "±0.4" against ±0.05 for the other meshes; name the $10^6$- and
  $4\times10^6$-cell meshes "regular" and "fine" in the text and "fine" and
  "very fine" in the Fig. 12 caption; and call 500 s and 1000 s "averaging
  periods" of 44 and 88 flow-throughs. With the 9 s flow-through implied by
  "207 s, or after 23 hills", 500 s and 1000 s are about 56 and 111
  flow-throughs, while 44 and 88 flow-throughs (396 and 792 s) are close to
  averaging windows from 207 s to 600 s and to 1000 s *(compiler check,
  not in the sources)*. Their Appendix A hill polynomials
  are printed with intervals in units of $h$ but coefficients that work
  with $x$ in millimetres for a 28 mm hill *(compiler check, not in the
  sources)*.
- [Wang et al. (2024)](/sources/wang-2024.md) print the domain as
  $9H\times4.5H$ without the channel height, and list OPT6 in Table 2 only
  for the finest grid while Figs. 5–6 show it on all four.

- [Dzanic et al. (2022)](/sources/dzanic-2022.md) print "cross-section ...
  in the streamwise-spanwise plane" (§3.1, Fig. 2 caption) for a section
  that is extruded in the spanwise direction, so the plane is the
  streamwise–wall-normal one; their figures normalize by $U_\infty$ and $H$
  while the text defines the bulk velocity and $h$.
- The two coarse-grid studies use different reference data (LES of
  Fröhlich et al. against experiment plus the LES of Breuer et al.), so their
  error levels are not directly comparable.
- [Haering et al. (2022)](/sources/haering-2022.md), §V B, print the
  domain as "a single peak-to-peak period of the periodic hill in the
  streamwise direction of dimensions $9.5h\times3.035h\times4.5h$" for
  the ERCOFTAC case UFR 3-30, whose database URL they print;
  [Dzanic et al. (2022)](/sources/dzanic-2022.md), §3.1, Fig. 2, give the
  crest-to-crest distance of the configuration of Fröhlich et al. as
  $9h$, with the same height and span. Haering et al. state the length
  nowhere else in the text. The ingested sources do not decide whether
  $9.5h$ is a printed slip or a different domain: the papers that define
  the case (Fröhlich et al. 2005; Breuer et al. 2009, not ingested) would.
  The entry was recorded as an open contradiction at drafting and moved
  here at the chunk-1 deep lint, because neither paper makes a claim about
  the other's domain.
- The parametrized hills of [Yan et al. (2022)](/sources/yan-2022.md)
  ($Re=5600$ on crest height and crest bulk velocity, variable hill width)
  are a family distinct from the $Re_h\approx10{,}600$ configuration of
  Haering et al. and Dzanic et al.; results are not comparable across the
  two. Yan et al. were read in an accepted manuscript, which names the
  training geometries $\alpha_h=0.5$ and 0.8 in the text (§3.2.2) while
  Figs. 19–21 show 0.8 and 1.2 as the training cases and call 0.5 an
  extrapolation; only training at 0.8 and 1.2 is consistent with the
  interpolation and extrapolation labels *(compiler check, not in the
  sources)*.

- [McConkey et al. (2022)](/sources/mcconkey-2022.md) (read in arXiv v1)
  print absolute RMSE values of the fitted anisotropy components in the
  Fig. 1 legend; they are not used here, only the errors "on the order of
  100%" stated in the text (§II B).
- [Cato et al. (2023)](/sources/cato-2023.md) (read in a HAL author
  manuscript) attribute an alignment threshold of 0.86 to Schmitt but use 0.8
  in their figures and text.
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) were read in arXiv v1, a
  6-page preprint that prints no network sizes beyond the architecture, no
  collocation counts and no citation for the hill DNS.
- [Lederer et al. (2023)](/sources/lederer-2023.md), §5, print the height
  as $3.0335h$, against $3.035h$ in Dzanic et al. and Haering et al., and
  their crest-to-crest length $9h$ agrees with Dzanic et al. The global
  degrees of freedom of their two hill meshes (Table 3, 43.2 and 331.0
  thousand) are exactly those of their $6^3$- and $12^3$-element channel meshes
  (Table 1) although the element counts differ (576 and 4608 elements
  against 216 and 1728) at the same $N=3$ *(compiler check, not in the
  sources)*; the paper does not comment on it.
- [Tang et al. (2023)](/sources/tang-2023.md) (arXiv v1) list the
  barycentric stations of the training hill as starting at $x/h=1.5$ in the
  text and at $0.5$ in the Fig. 8 caption and panels (§III C), and swap the
  equation numbers of their two models in the captions of Figs. 17–18. Their
  anisotropy is $R_{ij}/k-\tfrac23\delta_{ij}=2b_{ij}$ in this bundle's
  notation (Eq. 10).

# Citations

- [Haering et al. (2022)](/sources/haering-2022.md) — §V B, Table II, Figs. 9–12; §V C, Figs. 14–15.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.1, Table 1, Figs. 2–6.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3, Figs. 6–7 (recalled results).
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I, §IV B (recalled training data and results).
- [Yan et al. (2022)](/sources/yan-2022.md) — §1; §3.2, Eq. (17), Table 2, Figs. 11–22.
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — §II A–F, Figs. 1–6; §III D; §IV B, Figs. 15–21.
- [Cato et al. (2023)](/sources/cato-2023.md) — §IV A–B, Table II, Figs. 8–10.
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — §3, Table 1, Fig. 6; §4.
- [Tang et al. (2023)](/sources/tang-2023.md) — §II D; §III A–E, Table I, Figs. 7–19.
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §5, §5.1, Table 3, Figs. 7–10.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §1–2; §3.2–3.3, Tables 1–4; §4.1–4.4, Table 5, Figs. 4–16; §5; App. A–C, Tables B.6–B.8, C.9.
- [Wang et al. (2024)](/sources/wang-2024.md) — §2.3–2.5; §3.3, Table 2, Figs. 5–6; §5.
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §4.1, Eq. 21, Figs. 23–27.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §4.2.3, Tables 5–7, Figs. 7–9.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv v1: §1; §3.4, Table 6, Figs. 10–16.
