---
type: Benchmark
title: "NASA wall-mounted hump"
description: "The NASA wall-mounted hump at chord Reynolds number 936,000 and Mach 0.1, a separation behind a two-dimensional bump whose measured reattachment the sources print at 1.10 or 1.15 chords: a training case of field inversion and symbolic regression, an unseen test of blended RANS corrections, and a test of hybrid RANS/LES and nonequilibrium wall models."
status: established
aliases: [wall-mounted hump, NASA hump, WMH]
tags: [benchmark, separated-flow, rans, field-inversion, data-driven, hybrid-rans-les, wmles]
timestamp: 2026-10-27T11:01:00Z
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
  $\mathrm{tr}(\hat\Omega^2)$ and $\mathrm{tr}(\hat\Omega^2\hat S^2)$ of the
  mean rotation and strain scaled by $1/(\beta^*\omega)$ (Table 4).
- Run in the solver, both models cut the mean square error of $C_f$
  against the measurements in the separated region to about 6.7% of that
  of SST; at the hump top SR-CND matches SST, while SR-CLS, whose $\beta$
  rises there, has 160% of the SST error (§3.3.2, Figs. 21–22).

Both models raise $\beta$ where the scaled rotation or strain is large;
larger $\beta$ lowers $\omega$, raises the eddy viscosity and the momentum
transfer into the recirculation, and shortens the bubble, consistent with
the finding of earlier work the authors cite that RANS models
underestimate eddy viscosity in separated shear layers (§3.2).

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

**What the sources share.** Both find baseline SST too late in
reattachment and both shorten the bubble by raising the eddy viscosity in
the separated shear layer, by a learned $\omega$-destruction multiplier
(Wu et al.) or by a separated-flow expert that itself shortens it too much
(Oulghelou et al.). Both report that a correction active in the attached
layer degrades the attached parts of the flow: at the hump top in Wu et
al. (SR-CLS), and on the flat plate and airfoil in Oulghelou et al. (the
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
