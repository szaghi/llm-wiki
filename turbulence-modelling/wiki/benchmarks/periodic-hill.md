---
type: Benchmark
title: "Periodic hill"
description: "The streamwise-periodic channel with a hill constriction, a smooth-wall separation and reattachment test: at hill-height Reynolds number about 10,600 for hybrid RANS/LES and implicit LES on coarse grids, as the parametrized hill family at 5600 for learned RANS corrections, and at 2800 for data assimilation and physics-informed networks."
status: established
aliases: [periodic hills, ERCOFTAC UFR 3-30, Fröhlich periodic hill, hill flow, parametrized periodic hills]
tags: [benchmark, separated-flow, hybrid-rans-les, pans, data-driven, field-inversion]
timestamp: 2026-10-26T05:07:00Z
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
do not relate the three.

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
errors of 16.7% to 28.2%.

## Qualifications

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

# Citations

- [Haering et al. (2022)](/sources/haering-2022.md) — §V B, Table II, Figs. 9–12; §V C, Figs. 14–15.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.1, Table 1, Figs. 2–6.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3, Figs. 6–7 (recalled results).
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I, §IV B (recalled training data and results).
- [Yan et al. (2022)](/sources/yan-2022.md) — §1; §3.2, Eq. (17), Table 2, Figs. 11–22.
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — §II A–F, Figs. 1–6; §III D; §IV B, Figs. 15–21.
- [Cato et al. (2023)](/sources/cato-2023.md) — §IV A–B, Table II, Figs. 8–10.
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — §3, Table 1, Fig. 6; §4.
