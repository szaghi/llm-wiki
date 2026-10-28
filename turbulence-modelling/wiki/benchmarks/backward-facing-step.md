---
type: Benchmark
title: "Backward-facing step"
description: "Turbulent flow over a sudden expansion with fixed separation at the step edge and downstream reattachment: it measures LES filter widths, adaptive IDDES meshes, learned RANS closures, high-order RANS wall functions and the k-τ model, and ZDES shielding on a lattice Boltzmann solver, at step Reynolds numbers 300 to 40,000; the curved variant trains corrected SST models."
status: established
aliases: [BFS, backstep, backward-facing step flow, sudden expansion, Kasagi–Matsunaga step, Vogel–Eaton step, Driver–Seegmiller step, A3C step, curved backward-facing step, CBFS]
tags: [benchmark, separated-flow, les, hybrid-rans-les, mesh-adaptation, data-driven, uncertainty-quantification, field-inversion, rans, dg, lattice-boltzmann, spectral-element]
timestamp: 2026-10-27T20:45:00Z
---

# Backward-facing step

A turbulent channel or boundary-layer flow passes a downward step of height
$H$ (page-local symbol) into a wider duct. The flow separates at the step
edge, so the separation point is fixed by the geometry, and the shear layer
that leaves the edge rolls up, grows and reattaches on the lower wall at a
distance $x_R$ (page-local, measured from the step) that is the main
quantity of interest; a secondary corner bubble sits at the foot of the step.
The expansion ratio is the downstream over the upstream duct height, and the
Reynolds number $Re_H$ is built on $H$ and a reference velocity of the
incoming flow. Because separation is fixed, the case isolates what a model
or a grid does to the free shear layer: its growth rate sets $x_R$. In this
bundle it tests the definition of the LES filter width on cells of high
aspect ratio, mesh adaptation for hybrid RANS/LES, the transfer of a
learned RANS closure to a geometry it was not trained on, and the limit of
a RANS wall function in the recirculation, a RANS model without wall
distance in spectral elements, and the shielding of a zonal detached-eddy
simulation on the isotropic grids of a lattice Boltzmann solver.

## Configurations in the sources

| Item | [Abe (2021)](/sources/abe-2021.md) | [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) |
|---|---|---|
| Experiment | PTV of Kasagi & Matsunaga | Vogel & Eaton |
| Expansion ratio | 1.5 | 1.25 (printed 5/4) |
| Reynolds number | $Re_\tau=290$ in the driver channel (on its half-height, equal to $H$); $Re_H\approx5700$ (experiment about 5500) | $Re_H=28{,}000$ |
| Inflow | periodic driver channel $6.4H\times2H\times3.2H$ at constant pressure gradient | precursor RANS channel matching a boundary-layer thickness of $1.07H$ |
| Domain | $3H$ upstream, $30H$ downstream, span $3.2H$ (periodic) | $-4H$ to $20H$, span $4H$ (symmetry planes) |
| Model | the author's hybrid LES/RANS model, run as LES with a stabilized mixed SGS model; wall-resolved | IDDES based on $k$-$\omega$ SST: RANS in the attached boundary layers, LES after separation |
| Grids | uniform $\Delta x=\Delta z=0.025H$, $0.05H$, $0.1H$ ($\Delta x^+=7.25$, 14.5, 29) up to $x=12H$; same $y$ grid, $\Delta y/H$ from $10^{-3}$ to 0.07 | fixed fine mesh of $9.3\times10^6$ cells ($\Delta x^+\le120$, $\Delta z^+\le60$); adapted meshes of $1.3\times10^6$ to $9.9\times10^6$ cells from an initial mesh with $\Delta x^+=240$, $\Delta z^+=120$ |
| Reference $x_R/H$ | 6.51 | 6.66 |

## What the case tests

**Filter width on high-aspect-ratio cells.** [Abe (2021)](/sources/abe-2021.md)
uses the shear layer downstream of the step because it lies far from walls
while the wall-normal spacing there stays very small ($\Delta x/\Delta y\sim100$
on the coarse grid). Grid convergence of the LES gives $x_R/H=6.54$, 6.67
and 7.19 (+0.5%, +2.5%, +10.4%) on the fine, medium and coarse grids (Table
II); the fine field, whose SGS share is negligible, is filtered to the
coarse resolution to give reference SGS stresses. A priori, the
[Smagorinsky model](/methods/smagorinsky-model.md) with the filter width
$\Delta=(\Delta x\Delta y\Delta z)^{1/3}$ strongly under-predicts the
equivalent SGS eddy viscosity in the shear layer, while the
[dynamic procedure](/methods/dynamic-procedure.md), the
[scale-similarity models](/methods/scale-similarity-model.md) and the
stabilized mixed model (filter width $\sqrt{\max(\Delta x\Delta y,\Delta y\Delta z,\Delta z\Delta x)}$)
agree with the reference (§IV C, Fig. 9). Swapping the widths reverses the
outcome (§IV D, Fig. 10), and a posteriori the coarse run with the cube-root
width lengthens the bubble to $x_R/H=7.43$ (+14.1%, Table III). The author
concludes that a spacing much smaller than the others must be excluded from
$\Delta$ (see [large-eddy simulation](/definitions/large-eddy-simulation.md)).
Without SGS model the coarse run gives $x_R/H=7.60$ (+16.7%), against 7.19
with the model, which the author reads as a sudden loss of accuracy of
[implicit LES](/definitions/implicit-les.md) on coarse grids (App. B, Table
IV).

**Mesh adaptation for hybrid RANS/LES.** [Mozaffari et al. (2022)](/sources/mozaffari-2022.md),
§4, use the step to calibrate an average-based adaptive refinement for
[detached-eddy simulation](/methods/detached-eddy-simulation.md) (see
[mesh adaptation](/methods/mesh-adaptation.md)). Refinement driven by the
instantaneous pressure–velocity Hessian ends with $6.6\times10^6$ cells,
peaks near $2\times10^7$, and gives $x_R/H=8.35$ (25% error) with a
perturbed skin friction. Averaging the refinement criterion in time gives a
converging mesh; lowering the threshold refines it and brings $x_R$ toward
experiment: 18.7%, 5.1% and 3.6% error with $1.3$, $2.5$ and $9.9$ million
cells, against 9.6% for the $9.3$-million-cell fixed fine mesh (Table 2).
Refinement boxes in the shear layer on the initial mesh give
$\approx2\times10^6$-cell meshes with $-2.5\%$ and $-5.4\%$ errors, which the
authors attribute to the earlier appearance of resolved turbulence rather
than to refinement of the recirculation zone, where the Hessian criterion
does not refine (§4.3–4.5). From the fine IDDES they identify Strouhal
numbers $fH/U_\infty$ of 0.86 (Kelvin–Helmholtz) and 0.43 (vortex pairing)
near the step, 0.22 (step mode) and 0.11 (shedding) at $x=6.67H$, and 0.008
(flapping), and recommend averaging windows of 4 to 10 periods of the
phenomenon to be averaged out (§4.4, §6).

**What the two studies share.** Both find that the reattachment length is
governed by how the grid and model treat the separated shear layer, and both
find the error to be an over-long bubble on under-resolved or poorly
modelled shear layers: the coarse grids and the cube-root filter width in
[Abe (2021)](/sources/abe-2021.md), the instantaneous or coarse adapted
meshes in [Mozaffari et al. (2022)](/sources/mozaffari-2022.md).

**Wall function in the recirculation.**
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.3, use the step of
Driver & Seegmiller at $Re_H=36{,}000$ (on $H$ and the free-stream
velocity at $x/H=-4$) and $M_\infty=0.128$ to test an explicit
[RANS wall function](/methods/rans-wall-function.md) in a high-order
modal discontinuous Galerkin solver for the
[Wilcox $k$-$\omega$ model](/methods/k-omega-model.md), run steady.
The domain spans $-115<x/H<50$ and $0<y/H<9$, with a symmetry boundary for
$-115<x/H<-110$; the wall-resolved reference mesh has 4750 elements, and
meshes whose first element has height $y_1^+=5$, 10, 20, 40 and 80 (2300
to 3700 elements; the outer resolution is also coarsened here) are run at
polynomial degrees $N=1$ to 6. The case stops at $y_1^+=80$, where only six
wall-normal elements are left across the step. Pressure and skin-friction
coefficients on the lower wall and profiles of the mean streamwise
velocity and of the turbulence intensity agree with the reference and with
the experiment for all $y_1^+\le80$ and all $N$; at $N=6$ the $C_f$
difference grows for $y_1^+>10$, and only in the recirculation region,
where the [law of the wall](/definitions/law-of-the-wall.md), valid only
for fully developed boundary layers, returns a wrong $u_\tau$. Because the
underestimated $C_f$ affects only the velocity in the viscous sublayer,
the velocity and turbulence-intensity profiles still agree (§4.3, Figs.
10–11). No reattachment length is printed. On the zero-pressure-gradient
plate the same function stays accurate up to $y_1^+=320$ (see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).

**The $k$-$\tau$ model on the Driver–Seegmiller step.**
[Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §3.3, run the
same experiment at $Re=37{,}425$ (on the step height and the incoming
free-stream velocity), inlet at $x/H=-4$, outlet at $40H$, channel heights
$8H$ upstream and $9H$ downstream, inlet profiles from 2D RANS channel runs
fitted to the measured inlet profile. The [$k$-$\tau$ model](/methods/k-tau-model.md)
and the authors' regularized $k$-$\omega$ run in [Nek5000](/software/nek5000.md)
at $p=7$ (2553 elements, 125,840 unique points, mean first-point
$y^+=0.21$; $p=2$ to 9 checked), the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
in [OpenFOAM](/software/openfoam.md) on meshes up to 165,072 cells (mean
$y^+=0.49$):

| Model | $x_R/H$ |
|---|---|
| $k$-$\tau$ (Nek5000) | 6.48 |
| regularized $k$-$\omega$ (Nek5000) | 6.49 |
| SST (OpenFOAM, fine) | 6.44 |
| experiment | 6.26 |
| Menter (1994), as cited: $k$-$\omega$ / SST | 6.4 / 6.5 |

All models under-predict the downstream velocity; OpenFOAM SST
under-predicts $C_f$, "a known behavior of the SST model"; at comparable
resolution the Nek5000 $C_f$ profiles are more consistent than OpenFOAM's,
and $p=4$ and $p=7$ give indistinguishable $C_f$ (Figs. 9–12). The
turbulent kinetic energy downstream departs from SST, which the authors
explain by the absence of blending functions in their $k$-$\tau$ model and
by different model parameters (§3.3). On the same step
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md) (above) report pressure,
skin-friction and profile agreement with their wall function at all
degrees $N=1$–6 for $y_1^+\le80$, and print no reattachment length.

**Zonal detached-eddy simulation on a lattice Boltzmann solver.**
[Husson et al. (2024)](/sources/husson-2024.md), §4.2, use the step of the
A3C combustion chamber (experiment of Moreau et al. as cited): $H=0.035$ m,
$u_0=50$ m/s, $T=520$ K, $Re_H=40{,}000$, boundary-layer thickness $0.37H$
at separation, span $2H$, periodic. They compare ZDES mode 2 (2020) on
the D3Q19 [lattice Boltzmann method](/methods/lattice-boltzmann-method.md)
of [ProLB](/software/prolb.md), with an
[immersed boundary](/methods/immersed-boundary-method.md) and a
linearized Spalart–Allmaras wall law, against the body-fitted
wall-resolved ZDES of Deck & Renard on a Navier–Stokes finite-volume
solver (Table 1):

| Run | $\Delta y^+$ at the step | nodes | wall model |
|---|---|---|---|
| ZDES and RANS, lattice Boltzmann | 15 | $44.7\times10^6$ | yes |
| ZDES and RANS, Navier–Stokes (Deck & Renard) | 1 | $3.9\times10^6$ | no |

Isotropy makes the lattice grid locally much finer than the Navier–Stokes
one ($\Delta z_{NS}\approx10\Delta z_{LBM}$ for $0\le x/H\le1$). The
shielding function computed a priori from the RANS lattice solution agrees
with that of the Navier–Stokes ZDES despite the different numerics and
grids; the vorticity-thickness growth of the shear layer agrees; early
two-dimensional Kelvin–Helmholtz rollers are more pronounced in the
Navier–Stokes run; the eddy viscosity is destroyed quickly and the
instabilities develop alike in both, so the authors conclude that the lattice solver adds no further delay in the
formation of instabilities (§4.2.2, Figs. 7–10). Mean velocity profiles at
four stations agree very well with the Navier–Stokes ZDES, and the
streamwise RMS shows a "fair common tendency" with it and with the
experiment; the near-wall differences at the first station are attributed
to the wall model, which imposes a zero-pressure-gradient profile inside
the recirculation (Fig. 11). No reattachment length is printed. See
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md).

**Out-of-geometry test of a learned RANS closure.**
[Tang et al. (2023)](/sources/tang-2023.md) (read in arXiv v1), §III A
and D, use a step at $Re_H=5000$ on the step height, with the geometry and
reference data of the Jovic & Driver experiment and the DNS of Le, Moin &
Kim: about 46,000 cells, a fixed inlet velocity profile, a zero-gradient
outlet and no-slip walls, 20,000 iterations of steady RANS (Table I). Their
[symbolic-regression closure](/methods/symbolic-regression-closure.md) for
the non-linear anisotropy, trained on a single
[periodic hill](/benchmarks/periodic-hill.md) and injected in frozen form
on top of the [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md), gives
velocity profiles "much closer" to DNS and experiment than the baseline in
the near-step region shown (Fig. 16). The comparison is restricted to that
region because full-field reference data were not available to the authors,
and no reattachment length is printed.

**A DNS-database subgrid closure on the same step.**
[Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.5, Figs.
14–16, run the step at $Re_H=5000$ with
[pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md),
whose subgrid stress comes from a database of DNS on representative volume
elements, and with the dynamic $k$-equation LES of Kim & Menon (see
[subgrid kinetic-energy equation models](/methods/subgrid-kinetic-energy-equation-model.md)),
on 142,000 cells with 20 cells per step height. The domain is $30H$ long,
including a $10H$ inlet section, $6H$ high and $4H$ wide (periodic span,
symmetry top, fixed total pressure at the outlet); the inflow is a
flat-plate turbulent boundary-layer profile with digital-filter
fluctuations, and the run lasts 800 time units with $\Delta t=0.02$, the
last 600 averaged. From the zero crossing of $C_f$:

| Solution | $x_R/H$ |
|---|---|
| experiment (Jovic & Driver), confirmed by oil-flow visualization | $6\pm0.15$ |
| DNS (6 million cells, Le, Moin & Kim) | 6.1 |
| P-DNS | 6.05 |
| LES (dynamic $k$-equation) | 5.1 |

On the same coarse mesh the database closure thus lands within the
experimental band and the LES 15% short of it *(compiler check, not in
the sources)*.

**Probabilistic learned closure at low Reynolds number.**
[Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) (read in arXiv
v2), §3, use a step of expansion ratio 2 (downstream channel height $2H$),
with $Re_H$ built on the step height and the inlet bulk velocity, as the
test of their Bayesian closure (see
[model-form uncertainty](/definitions/model-form-uncertainty.md)): a
[tensor-basis neural network](/methods/tensor-basis-neural-network.md) for
the Reynolds stress plus a stochastic discrepancy field, trained through an
adjoint of a finite-element RANS solver
([model-consistent training](/methods/model-consistent-training.md)) on
sparse mean velocity and pressure only.

- Reference data: OpenFOAM LES with the [WALE model](/methods/wale-model.md),
  domain $27H\times2H\times H$ periodic in $z$, 1,428,920 degrees of
  freedom, averaged in time and span (§3.2). Training at $Re_H=300$, 700,
  900 and 1100; test at $Re_H=500$. About 8% of the 12,180 nodes of the 2D
  RANS mesh ("approximately 1000" points) are observed (§3.2, Fig. 4).
- Baseline: the [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md)
  (simpleFoam, 35,709 degrees of freedom), which "underestimates the size
  of the first recirculation zone and almost completely misses the second
  one"; the learned model predicts both (§3.4, Fig. 8).
- Reattachment length at $Re_H=500$ (Table 5):

| Model | $x_R/H$ |
|---|---|
| LES (reference) | 9.10 |
| Biswas et al. (as cited; expansion ratio 1.9423) | 8.9 |
| $k$-$\varepsilon$ baseline | 5.61 |
| TBNN of Geneva & Zabaras (as cited) | 5.52 |
| probabilistic closure, mean ± 3 std | $10.06\pm1.21$ |

  Only the probabilistic prediction envelops the LES value; the authors
  attribute the short bubble of Geneva & Zabaras to "the lack of the
  stochastic, model correction term", a conjecture they do not test (§3.4).
- Cost relative to one baseline RANS run (Table 4): LES 7679, the
  differentiable RANS solver 1.3.

The step here plays a different role from the other configurations: the
learned closure is trained and tested in the same geometry at different
Reynolds numbers, because its discrepancy field is tied to the grid and
geometry (§2.2.3, §2.2.5).

**The curved backward-facing step as training data.** Three sources use
the curved variant (CBFS), a step of height $H$ with a curved surface, at
$Re_H=13{,}700$ (on the step height and the inlet centre-channel velocity,
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md)), with the wall-resolved LES of Bentaleb et al. as reference, to
train corrections of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
in OpenFOAM:

- [Wu et al. (2025)](/sources/wu-2025.md), §3.1.1 and §3.3.1, run
  [field inversion](/methods/field-inversion-machine-learning.md) of a
  multiplier $\beta(\boldsymbol x)$ of the $\omega$-destruction term against the
  LES streamwise velocity at 30 random points in the separation region
  ($H=1$ m, inlet centre velocity 1 m/s). Classic inversion lowers the
  objective by 88.3% and the conditioned inversion, whose correction is
  switched off in attached boundary layers by the DDES shielding function,
  by 74.7% (Fig. 4); the classic one also raises $\beta$ in the attached
  layer upstream of the step, the conditioned one only in the separated
  shear layer (Fig. 7); both inversions fix the separation zone that SST
  overpredicts (Fig. 5). Baseline SST reattaches at $x=6.0$ (Fig. 15);
  both [symbolic-regression](/methods/symbolic-regression-closure.md)
  models trained on the inversion data improve the reattachment and $C_f$
  in the reattachment region (Figs. 15–17). No LES reattachment value is
  printed.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (arXiv v2), §4.2.3,
  use the CBFS (grid $140\times150$; at $x=-7.34H$, $Re_\theta\approx1190$
  and $\delta\approx0.8H$) as one of the three training flows of a
  separated-flow expert correction and of a learned
  [blend of expert models](/methods/turbulence-model-aggregation.md).
  Separation and reattachment, in $x/H$ (Table 6):

| Model | separation | reattachment | bubble length |
|---|---|---|---|
| LES (Bentaleb et al.) | 0.81 | 4.36 | 3.55 |
| SST | 1.06 | 4.65 | 3.59 |
| separated-flow expert | 1.33 | 3.84 | 2.51 |
| jet expert | 0.81 | 6.33 | 5.52 |
| blend | 1.08 | 4.52 | 3.44 |

  Here baseline SST already gives the bubble length within 0.04$H$ and the
  lowest $C_f$ error ($4.83\times10^{-4}$ against $5.05\times10^{-4}$ for
  the blend, Table 7); the separated-flow expert, trained partly on this
  flow, gives a bubble $1.04H$ shorter than the LES.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md), §4.1–4.2, use the
  CBFS ($Re=13{,}700$ on the inlet velocity and the step height, upstream
  channel height $8.52H$, mesh $140\times150$, slip upper boundary, inlet
  from a fully developed boundary-layer simulation, steady RANS) as one of
  three flows, with the [periodic hill](/benchmarks/periodic-hill.md) and
  a converging–diverging channel, of a leave-one-out training of
  SBL-SpaRTA: sparse Bayesian regression of an additive anisotropy
  correction $b^\Delta_{ij}$ and a production correction $b^R_{ij}$ of SST
  on the two-dimensional integrity basis $T^{(1)}$–$T^{(3)}$ (see
  [explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
  and [symbolic-regression closures](/methods/symbolic-regression-closure.md)).
  The CBFS is a training flow in scenarios 1 (with the hill) and 3 (with
  the channel) and the test flow of scenario 2 (Table 1). The three models
  selected by a posteriori cross-validation (sparsity parameter
  $2\times10^5$) keep $b^\Delta_{ij}=0$ and a single production term
  proportional to $T^{(1)}_{ij}$, with posterior coefficients
  $0.8433\pm0.0142$, $0.382\pm0.0184$ and $0.197\pm0.0156$ in scenarios 1,
  2 and 3 (Eqs. A.13–A.15); the correction raises the eddy viscosity in
  the separated region and reattaches the boundary layer (§4.2). With
  $\pm3\sigma$ bands from second-order polynomial chaos (three RANS runs
  per model): velocity profiles are clearly better than SST, especially in
  the CBFS recirculation, where the bands of the model trained on CBFS and
  channel are too narrow to cover the LES (Fig. 5); the separation and
  reattachment points improve and the bands encompass the LES ones
  (Fig. 6); the skin friction in the attached regions is slightly worse
  than baseline, most visibly for the model with the largest coefficient,
  with the LES values still inside the bands; $k$ is over-predicted in the
  separated regions (Fig. 7). Cross-validated on velocity alone, the best
  CBFS model is a richer one with non-zero $b^\Delta_{ij}$ (sparsity
  parameter $10^4$, Table 2). The learned models also beat the BSL-EARSM of
  Menter et al. (as cited) on the three flows (App. C). No separation or
  reattachment values are printed in the text.

**RANS corrections.**
[Yan et al. (2022)](/sources/yan-2022.md), §1, cite Rumsey's finding that enhancing
the mixing in the separated shear layer of the $k$-$\omega$ SST model
improves the [periodic hill](/benchmarks/periodic-hill.md) but worsens
backward-facing-step flows, an example of a separation fix that does not
generalize. [Wang et al. (2021)](/sources/wang-2021-l.md), §3.3, describe
the transonic flow behind the boat tail of the NASA Model 11 hammerhead
launch vehicle, on which they test a Reynolds-stress-based IDDES (see
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and
[hammerhead launch-vehicle buffet](/benchmarks/hammerhead-launch-vehicle-buffet.md)), as one
that "can be regarded as an axisymmetric back-step flow", citing earlier
work. [Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.3, cite
gene-expression-programming RANS models trained on a backward-facing
step that showed a high level of uncertainty when applied to the periodic hill.
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §4.1, cite the
same transfer from their group's work: gene-expression-programming
anisotropy models trained on a backward-facing step gave "excellent" a
posteriori periodic-hill predictions with only the first four basis
tensors and two invariants, while some individuals had very large
coefficients, non-realizable stresses and unstable runs, which symbolic
transparency let the authors remove, though not robustly automatically.
The same review lists the curved step among the three two-dimensional
flows on which SpaRTA was demonstrated (§3.4).

## Qualifications

- The configuration of [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md)
  ($Re_H$ from 300 to 1100) lies below those of the other configurations
  on this page ($Re_H$ 5000 to 36,000); the authors cite Armaly et al. for the existence of the
  secondary recirculation zone above $Re_H\approx400$ but do not discuss
  whether the regime is turbulent, and use $k$-$\varepsilon$ and LES there.
  Their Table 2 lists five viscosities for four training Reynolds numbers;
  the second, $2.00\times10^{-3}$, corresponds to the test case $Re_H=500$
  *(compiler check, not in the sources)*.

- On the CBFS Wu et al. and Oulghelou et al. print different baseline SST reattachment
  points: $x=6.0$ ([Wu et al. (2025)](/sources/wu-2025.md), Fig. 15, with
  $H=1$ m) against $x/H=4.65$
  ([Oulghelou et al. (2025)](/sources/oulghelou-2025.md), Table 6), at the
  same $Re_H$ and against the same LES. Neither paper states the origin of
  $x$ in a way that lets the two be compared, so the difference is recorded
  here, not as a contradiction. Wu et al. call the SST separation
  overpredicted; Oulghelou et al. find SST nearly exact in bubble length.
- The configurations of [Abe (2021)](/sources/abe-2021.md) and
  [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) differ in expansion ratio (1.5 against 1.25),
  Reynolds number ($Re_H\approx5700$ against 28,000), inflow and modelling
  level (wall-resolved LES against IDDES), so their reattachment errors are
  not comparable with each other.
- [Abe (2021)](/sources/abe-2021.md), §III, defines the velocity in $Re_H$
  as "the mean velocity at the center of the driver channel" while calling
  it the bulk velocity.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) were read in an
  author manuscript. They give the fine mesh as $9.2\times10^6$ cells in
  §4.1 and $9.3\times10^6$ in Table 2, and print the skin-friction
  coefficient as $\tau_w/(\tfrac12\rho U_\infty)$, without squaring the
  velocity.
- The step of [Tang et al. (2023)](/sources/tang-2023.md) ($Re_H=5000$,
  Jovic & Driver) is a third configuration; its comparison is qualitative
  (profiles), so it adds no reattachment-length datum. In §III D the
  authors attribute the DNS to Jovic & Driver and the experiment to Le, Moin
  & Kim, the reverse of their own §III A and of the printed reference
  titles.
- Two sources now report how learned or corrected RANS models trained on
  one separated geometry carry over to the other: the gene-expression
  models trained on the step showed "a high level of uncertainty" on the
  hill (as cited by Duraisamy et al., §5.3), while the closure of Tang et al.,
  trained on the hill, improved the step profiles. The two concern different
  model families and opposite directions of transfer, so they do not
  contradict each other.
- The step-to-hill transfer of gene-expression-programming models is
  described in two ways: "a high level of uncertainty"
  ([Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.3) and
  "excellent" a posteriori predictions, with some unstable, non-realizable
  individuals ([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md),
  §4.1). Both are accounts of cited work, not the sources' own
  computations, so the two are recorded side by side, not as a
  contradiction.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) and
  [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) run the CBFS on the
  same $140\times150$ grid against the same LES. Cherroud et al. print the
  limited production of their frozen $k$-equation (Eq. 11) as
  $2k(-\tfrac{\nu_t}{k}\langle S_{ij}\rangle+b^\Delta_{ij})\partial_j\langle u_i\rangle$;
  with their own Eq. 2 (the stress enters the momentum equation as
  $-\partial_jR_{ij}$) and Boussinesq anisotropy $-\nu_t\langle S_{ij}\rangle/k$
  (Eq. 4), the production $-R_{ij}\partial_j\langle u_i\rangle$ is
  $2k(\tfrac{\nu_t}{k}\langle S_{ij}\rangle-b^\Delta_{ij})\partial_j\langle u_i\rangle$,
  the opposite sign *(compiler check, not in the sources)*. Their
  production correction $R=2k\,b^R_{ij}\partial_j\langle u_i\rangle$
  (Eq. 12) follows the printed convention of Eq. 11, so the sign of the
  printed $b^R_{ij}$ coefficients relative to $\nu_t$ depends on it; the
  statement that the correction raises the eddy viscosity is theirs (§4.2).

- The Driver–Seegmiller step is given $Re_H=36{,}000$ (free-stream
  velocity at $x/H=-4$) by [Ghidoni et al. (2026)](/sources/ghidoni-2026.md)
  and $Re=37{,}425$ (incoming free-stream velocity) by
  [Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §3.3; neither
  comments on the other value, and the two are recorded side by side.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) call their
  OpenFOAM meshes coarse, medium and fine but write that "the coarse and
  fine meshes … show good agreement, however the coarsest mesh profile
  differs significantly" (§3.3).
- [Husson et al. (2024)](/sources/husson-2024.md) write, for
  $x/H\ge1.5$, that "the LBM grid resolution is finer than the LBM one"
  (§4.2.2), where one of the two is the Navier–Stokes grid; no averaging
  time is printed for the step.

# Citations

- [Abe (2021)](/sources/abe-2021.md) — §III, Table I; §IV A–D, Tables II–III, Figs. 4–11; App. B, Table IV.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §4.1–4.5, Tables 1–2, Figs. 6–15; §6.
- [Yan et al. (2022)](/sources/yan-2022.md) — §1 (cited result of Rumsey).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3 (cited result).
- [Tang et al. (2023)](/sources/tang-2023.md) — §III A, §III D, Table I, Fig. 16.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §2.2.3, §2.2.5; §3.1–3.4, Tables 2–5, Figs. 4–12.
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §3.1.1, Eq. 18, Figs. 3–7; §3.3.1, Figs. 15–18.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §4.1; §4.2.3, Tables 5–7, Figs. 7–9.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §4.3, Figs. 9–11 (Driver–Seegmiller step, wall function).
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §3.3 (hammerhead flow likened to an axisymmetric step; see [hammerhead launch-vehicle buffet](/benchmarks/hammerhead-launch-vehicle-buffet.md)).
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §2.10.5, Figs. 14–16.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.3, Figs. 7–12.
- [Husson et al. (2024)](/sources/husson-2024.md) — §4.2.1–4.2.2, Table 1, Figs. 6–11.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §2.1–2.2, Eqs. 2, 4, 11, 12; §4.1–4.2, Tables 1–2, Figs. 5–7; App. A, Eqs. A.13–A.15; App. C.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.4; §4.1 (cited step-to-hill transfer of GEP models).
