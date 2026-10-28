---
type: Benchmark
title: "NASA wall-mounted hump"
description: "The NASA wall-mounted hump at chord Reynolds number 936,000 and Mach 0.1, a separation behind a two-dimensional bump whose measured reattachment the sources print at 1.10 or 1.15 chords: a training case of field inversion and symbolic regression, an unseen test of blended RANS corrections and of recalibrated Spalart–Allmaras constants, and a test of hybrid RANS/LES and nonequilibrium wall models."
status: established
aliases: [wall-mounted hump, NASA hump, WMH]
tags: [benchmark, separated-flow, rans, field-inversion, data-driven, hybrid-rans-les, wmles]
timestamp: 2026-10-28T12:25:00Z
---

# NASA wall-mounted hump

A two-dimensional bump of chord $c$ mounted on a flat wall in a wind
tunnel. The incoming turbulent boundary layer separates from the aft part
of the hump and reattaches downstream on the flat wall: in the experiment
quoted by [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (Table 11)
the bubble runs from $0.62c$ to $1.15c$. The quantities compared are the separation and reattachment points, $C_p$
and $C_f$ along the wall and velocity profiles in and behind the bubble.
The sources run it at $Re_c=9.36\times10^5$ on the hump chord ($c=1$ m),
with the experiments of Greenblatt et al. (as printed by
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md)), the skin-friction
measurements of Naughton et al., and the wall-resolved LES of Uzun & Malik
([Wu et al. (2025)](/sources/wu-2025.md)) as reference. In this bundle it
is a separated-flow case for data-driven corrections of the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md), used for
training in one source and as an unseen test in the other, and, through
two reviews, a test of [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
and [wall-modelled LES](/methods/wall-modelled-les.md). The two
sources that print the measured reattachment give different values from
two reports of the experiment (see Qualifications). All $x$ below are in units of $c$.

[Heinz (2020)](/sources/heinz-2020.md), §5.2, gives the geometry of the
experiment of Greenblatt et al.: chord $c=0.42$ m, crest height 0.0537 m,
the hump mounted on a splitter plate 0.0127 m thick in a tunnel 0.771 m
wide and 0.508 m high, nominal test-section height 0.382 m above the
plate, hump width 0.584 m between end plates; $Re_c\approx936{,}000$ on
the free-stream velocity and the chord, $M=0.1$, "which allows both
incompressible and compressible simulations".

## Configurations in the sources

| Item | [Wu et al. (2025)](/sources/wu-2025.md), §3.1.2, §3.3.2 | [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §5.1.2 |
|---|---|---|
| Role | training case of field inversion and symbolic regression | unseen test of a learned blend of expert corrections |
| Flow | $Re_c=0.936\times10^6$, inlet velocity 14.88 m/s | $Re_c=936{,}000$ |
| Model | SST with a multiplier $\beta(\boldsymbol x)$ of the $\omega$ destruction, classic or gated by the DDES shielding function | SST, a separated-flow expert, a jet expert and their random-forest blend |
| Solver | OpenFOAM simpleFoam; DAFoam discrete adjoint | modified OpenFOAM, 2D steady |
| Grid | not printed | $409\times109$ |
| Reference | LES of Uzun & Malik (velocity at 40 points); $C_f$ of Naughton et al. | experiments of Greenblatt et al. |

## What the case tests

**Field inversion with and without an attached-layer mask.**
[Wu et al. (2025)](/sources/wu-2025.md) (read in the authors' Word
manuscript) invert, by SLSQP with discrete-adjoint gradients, a spatial
multiplier $\beta(\boldsymbol x)$ of the destruction term of the SST
$\omega$ equation against the LES streamwise velocity at 40 points in the
separated region, with an $L_2$ penalty on $\beta-1$ (Eq. 18; see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
In the classic inversion the multiplier acts everywhere; in the
conditioned inversion it enters as $(\beta-1)f_d+1$, with $f_d$ the DDES
shielding function of [delayed DES](/methods/detached-eddy-simulation.md),
so that it vanishes in the attached boundary layer (Eqs. 5–6).

- Both converge in about 140 iterations; the objective falls by 61.7%
  (classic) and 66.7% (conditioned) (Fig. 9).
- The classic inversion raises $\beta$ to about 2 near the shear layer and
  also inside the attached boundary layer at the top of the hump, where it
  "could disrupt the calibration" of SST; the conditioned one raises it to
  4–5 only around the separated shear layer (Fig. 12).
- Combined with a curved backward-facing step (see
  [backward-facing step](/benchmarks/backward-facing-step.md)), the
  inversion data are fitted by
  [symbolic regression](/methods/symbolic-regression-closure.md) to the
  closed forms $\beta-1=-\tfrac{3}{500}\lambda_5\tanh(-0.092\lambda_2)$
  (SR-CLS) and $\beta-1=\min(0.00435\lambda_2^2,3.806)$ (SR-CND), with
  $\lambda_2$, $\lambda_5$ (page-local) the invariants
  $\mathrm{tr}(\mathsf W^2)$ and $\mathrm{tr}(\mathsf W^2\mathsf S^2)$ of the
  mean rotation and strain scaled by $1/(\beta^*\omega)=k/\varepsilon$
  (registry §11 $\mathsf W_{ij}$, $\mathsf S_{ij}$) (Table 4).
- Run in the solver, both models cut the mean square error of $C_f$
  against the measurements in the separated region to about 6.7% of that
  of SST; at the hump top SR-CND matches SST, while SR-CLS, whose $\beta$
  rises there, has 160% of the SST error (§3.3.2, Figs. 21–22).

The authors explain both models (§3.2): they raise $\beta$ where the scaled
rotation or strain is large; larger $\beta$ lowers $\omega$, raises the eddy
viscosity and the momentum transfer into the recirculation, and shrinks the
separation, consistent with the finding of earlier work they cite that RANS
models underestimate eddy viscosity in separated shear layers.

**An unseen test of blended expert corrections.**
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (read in arXiv v2)
apply three SST-based experts and a
[blend](/methods/turbulence-model-aggregation.md) whose space-dependent
weights a random forest predicts from local features of the baseline
solution, trained on a channel, a jet, periodic hills, a
converging–diverging channel and a curved step, but not on the hump.
Separation bubble (Table 11):

| Model | separation | reattachment | length |
|---|---|---|---|
| experiment | 0.62 | 1.15 | 0.53 |
| SST | 0.62 | 1.24 | 0.62 |
| separated-flow expert | 0.62 | 1.03 | 0.41 |
| jet expert | 0.62 | 1.7 | 1.08 |
| blend | 0.62 | 1.14 | 0.52 |

Mean absolute errors (Table 10):

| Model | $U/U_{\mathrm{ref}}$ | $C_f$ | $C_p$ |
|---|---|---|---|
| jet expert | 0.24 | $2.17\times10^{-3}$ | 0.09 |
| SST | 0.06 | $7.53\times10^{-4}$ | 0.03 |
| separated-flow expert | 0.06 | $4.21\times10^{-4}$ | 0.05 |
| blend | 0.04 | $3.86\times10^{-4}$ | 0.04 |

The blend predicts the bubble within $0.01c$ and has the lowest velocity
and $C_f$ errors, SST the lowest $C_p$ error. In the core flow all weights
tend to 1/3, which the authors read as insensitivity of that region to the
turbulence model (Fig. 12d). In latent projections of the features the hump
lies mostly inside the training region (§5.1, Fig. 10).

**Spalart–Allmaras in finite volume and high-order DG, with recalibrated
constants.** [An et al. (2025)](/sources/an-2025.md), §4.3, Table 7,
Figs. 25–27, run the hump at $M=0.1$, $Re_c=9.36\times10^5$, as a
validation flow of the constant set they obtained by
[Bayesian calibration](/methods/bayesian-closure-calibration.md) on the
[backward-facing step](/benchmarks/backward-facing-step.md) and the
[Gaussian bump](/benchmarks/gaussian-bump.md): two-dimensional steady RANS
with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) in
second-order finite volume (CFL3D, $409\times109$, $y^+\approx1$, the grid
size Oulghelou et al. print) and in the authors' third-order
discontinuous Galerkin solver ($211\times61$, $y^+\approx5$), against the
experiment of Greenblatt et al. (part 2, as cited). With the standard
constants the DG skin friction is already better than the finite-volume
one and captures the bubble size and reattachment "aligning closely with
experimental measurements" despite discrepancies at the peaks, while its
$C_p$ errors are "marginally larger"; the recalibrated constants give
"limited improvements" overall, the DG run improving $C_p$ at the crest
transitions and in the separation. No separation or reattachment value is
printed, so the run cannot be placed in the tables of this page.

**Hybrid RANS/LES and wall-modelled LES compared.**
[Heinz (2020)](/sources/heinz-2020.md), §5.2, Table 3, Figs. 10–11,
compiles reattachment predictions against the experimental value
$x_R=1.10$ printed there ($x_R$ registry §11):

| Method | cited study | $x_R$ | error |
|---|---|---|---|
| RANS | Lardeau & Billard | 1.188–1.305 | 8%–18.6% |
| LES | Uzun & Malik | 1.095 | 0.5% |
| DES | Probst et al. | 1.114–1.152 | 1.3%–4.7% |
| WMLES | Iyer & Malik | 1.035–1.105 | 5.9%–0.5% |
| source-term method | Woodruff | 1.08–1.19 | 1.8%–8.2% |

The author uses the case to show "resolution deficiencies" of hybrid methods:
WMLES and DES miss the double-peak structure of $C_f$ in the bubble (Figs.
10–11, the latter taken from Probst et al.), and the RANS errors reach
18.6%. [Bose & Park (2018)](/sources/bose-2018.md), §4.3, cite
wall-modelled LES of the hump of Greenblatt et al. (2006a,b) at an inflow
$Re_\tau\approx2000$ (Avdis et al. 2009; Park 2017) that finds the full
[nonequilibrium wall model](/methods/nonequilibrium-wall-model.md) better
than [equilibrium wall models](/methods/equilibrium-wall-model.md) in the
separation bubble and the recovery region. Both reviews compile results;
neither runs the hump. See also
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

**A reference resolution for aircraft WMLES.**
[Kiris et al. (2023)](/sources/kiris-2023.md), §I, cite the WMLES of the
hump by Park (2017) among the academic WMLES of nonequilibrium boundary
layers in spanwise-periodic domains, with the Gaussian bump, canonical
shock/boundary-layer interactions and airfoil buffet, whose grid spacing
per unit span is substantially finer than that of full-airframe WMLES
with fewer than $10^9$ degrees of freedom, which they therefore call
coarse-grid simulations. Because none of the high-lift submissions they
review had the resolution needed for smooth-body separation on the flaps,
they call for continued WMLES research on the hump and the Gaussian bump
(§VI 1f; see [NASA CRM-HL](/benchmarks/nasa-crm-high-lift.md)). They run
no hump case.

**Grid convergence of WMLES on the hump, as cited.** Two wall-modelling
studies cite Park's WMLES of the hump as the reference grid-convergence
study of a separated flow. [Hu et al. (2024)](/sources/hu-2024.md), §1,
cite its three grids of 11.7 M, 12.9 M and 36.3 M cells: the
[nonequilibrium wall model](/methods/nonequilibrium-wall-model.md) had
"mostly converged" on the medium grid, the
[equilibrium wall model](/methods/equilibrium-wall-model.md) converged
more slowly and less monotonically, and no-slip LES without a wall model
was only marginally worse on the medium and fine grids, which they read
as those grids approaching wall-resolved resolution. In §2 they cite its
convergence trend, up to $Re_\tau\approx5000$, as consistent with their
estimate that a quantity on the scale of $\delta$ converges on grids of
$O(10)$ cells per $\delta$ (see
[wall-modelled LES](/methods/wall-modelled-les.md)).
[Zhou & Bae (2024)](/sources/zhou-2024-b.md), §1, name it with Iyer &
Malik's study of the [Gaussian bump](/benchmarks/gaussian-bump.md) as the
noteworthy contributions on WMLES of separated flow, which they call
sparse next to the attached-flow sensitivity studies. Neither runs the
hump.

**What the sources share.** Both shorten the SST separation by a
correction aimed at the separated shear layer: Wu et al. by a learned
$\omega$-destruction multiplier, Oulghelou et al. by a separated-flow expert,
which on the hump reattaches at 1.03 against 1.24 for SST and 1.15 measured
(Table 11). In both, a correction active in the attached layer degrades the
attached parts of the flow: at the hump top in Wu et al. (SR-CLS, 160% of
the SST error), and on the flat plate and airfoil in Oulghelou et al. (the
non-baseline experts; see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md) and
[NACA 0012](/benchmarks/naca-0012-airfoil.md)).

## Qualifications

- Wu et al. use the hump for training and Oulghelou et al. as an unseen
  test; Wu et al. print no bubble length, so the two baseline SST runs
  cannot be compared numerically.
- The $C_f$ error of [Wu et al. (2025)](/sources/wu-2025.md) is a mean
  square error relative to SST, that of
  [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) an absolute mean
  error; Oulghelou et al. do not define it by formula.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) state that the
  blend "generally outperforms" the experts; on the hump it is best on two
  of three metrics, consistent with their Table 10.
- [Heinz (2020)](/sources/heinz-2020.md) prints the errors of Table 3
  relative to $x_R=1.10$; they check against the printed $x_R$ values,
  and against the 1.15 of Oulghelou et al. the LES value 1.095 would be
  4.8% short *(compiler check, not in the sources)*.
- **Measured reattachment point of the hump.**
  [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), arXiv v2, §5.1.2,
  Table 11, print the experimental separation bubble from $x=0.62$ to 1.15
  (length 0.53), citing the skin-friction measurements of Naughton, Viken &
  Greenblatt (2006, their ref. [73]); they take the configuration from
  Greenblatt et al. (their ref. [62]). [Heinz (2020)](/sources/heinz-2020.md),
  §5.2, Table 3, prints the experimental reattachment point as $x_R=1.10$,
  with "±0.5" in the error column (e/%), citing Greenblatt et al. (2006,
  "Experimental investigation of separation control – Part 1", their ref.
  [253], the same report as Oulghelou et al.'s ref. [62]). Both present the
  value as the measured reattachment of the same hump flow at
  $Re_c=936{,}000$, from two different reports on that experiment (a skin-friction
  report and Part 1 of the separation-control study); neither discusses the
  other value. Each source cites a different report of the experiment, so
  the two values are set side by side here rather than recorded as a
  contradiction between the sources.

# Citations

- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §2.1, Eqs. 5–7; §2.2, Table 2; §3.1.2, Eq. 18, Figs. 8–12; §3.2, Table 4; §3.3.2, Figs. 19–22.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §5.1, Fig. 10; §5.1.2, Tables 10–11, Figs. 12–14.
- [Heinz (2020)](/sources/heinz-2020.md) — §5.2, Tables 2–3, Figs. 9–11 (compiled results).
- [Bose & Park (2018)](/sources/bose-2018.md) — §4.3 (cited results).
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §I; §VI 1f (cited as a resolution reference and recommended case; not run).
- [Hu et al. (2024)](/sources/hu-2024.md) — §1; §2 (cited grid-convergence study of Park; not run).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §1 (cited; not run).
- [An et al. (2025)](/sources/an-2025.md) — §4.3, Table 7, Figs. 25–27.
