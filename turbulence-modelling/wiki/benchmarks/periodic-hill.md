---
type: Benchmark
title: "Periodic hill"
description: "The streamwise-periodic channel with a hill constriction at hill-height Reynolds number about 10,600, a smooth-wall separation and reattachment test for hybrid RANS/LES, implicit LES and learned RANS corrections, here run on grids 14 to 60 times smaller than wall-resolved LES."
status: established
aliases: [periodic hills, ERCOFTAC UFR 3-30, Fröhlich periodic hill, hill flow]
tags: [benchmark, separated-flow, hybrid-rans-les, pans, data-driven]
timestamp: 2026-10-25T13:45:00Z
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

**Machine-learning wall models.**
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §I and §IV B, recall
that the wall model of Zhou et al. was trained on channel and periodic-hill
data at $Re_h=5600$ to $10{,}595$ and was reported to perform well a priori
but poorly a posteriori on periodic hills. In their own a priori
law-of-the-wall tests the same network over-predicts the wall stress,
increasingly with $Re_\tau$ (§IV B, Fig. 12; see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).

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

# Citations

- [Haering et al. (2022)](/sources/haering-2022.md) — §V B, Table II, Figs. 9–12; §V C, Figs. 14–15.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.1, Table 1, Figs. 2–6.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3, Figs. 6–7 (recalled results).
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I, §IV B (recalled training data and results).
