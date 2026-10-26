---
type: Benchmark
title: "Backward-facing step"
description: "Turbulent flow over a sudden channel expansion, with fixed separation at the step edge, a free shear layer and downstream reattachment: the reattachment length as a measure of LES filter widths at Re_H about 5700, of adaptive IDDES meshes at 28,000, of a transferred learned RANS closure at 5000, and of a probabilistic learned closure at 300–1100."
status: established
aliases: [BFS, backstep, backward-facing step flow, sudden expansion, Kasagi–Matsunaga step, Vogel–Eaton step]
tags: [benchmark, separated-flow, les, hybrid-rans-les, mesh-adaptation, data-driven, uncertainty-quantification]
timestamp: 2026-10-26T10:26:00Z
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
aspect ratio, mesh adaptation for hybrid RANS/LES, and the transfer of a
learned RANS closure to a geometry it was not trained on.

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
| Biswas et al. (as recalled; expansion ratio 1.9423) | 8.9 |
| $k$-$\varepsilon$ baseline | 5.61 |
| TBNN of Geneva & Zabaras (as recalled) | 5.52 |
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

**RANS corrections.** As recalled by
[Yan et al. (2022)](/sources/yan-2022.md), §1, Rumsey found that enhancing
the mixing in the separated shear layer of the $k$-$\omega$ SST model
improves the [periodic hill](/benchmarks/periodic-hill.md) but worsens
backward-facing-step flows, an example of a separation fix that does not
generalize. As recalled by [Duraisamy et al. (2019)](/sources/duraisamy-2019.md),
§5.3, gene-expression-programming RANS models trained on a backward-facing
step showed a high level of uncertainty when applied to the periodic hill.

## Qualifications

- The configuration of [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md)
  ($Re_H$ from 300 to 1100) lies below those of the other configurations
  on this page ($Re_H$ 5000 to 28,000); the authors cite Armaly et al. for the existence of the
  secondary recirculation zone above $Re_H\approx400$ but do not discuss
  whether the regime is turbulent, and use $k$-$\varepsilon$ and LES there.
  Their Table 2 lists five viscosities for four training Reynolds numbers;
  the second, $2.00\times10^{-3}$, corresponds to the test case $Re_H=500$
  *(compiler check, not in the sources)*.

- The two configurations differ in expansion ratio (1.5 against 1.25),
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
  hill (as recalled by Duraisamy et al.), while the closure of Tang et al.,
  trained on the hill, improved the step profiles. The two concern different
  model families and opposite directions of transfer, so they do not
  contradict each other.

# Citations

- [Abe (2021)](/sources/abe-2021.md) — §III, Table I; §IV A–D, Tables II–III, Figs. 4–11; App. B, Table IV.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §4.1–4.5, Tables 1–2, Figs. 6–15; §6.
- [Yan et al. (2022)](/sources/yan-2022.md) — §1 (recalled result of Rumsey).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3 (recalled result).
- [Tang et al. (2023)](/sources/tang-2023.md) — §III A, §III D, Table I, Fig. 16.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §2.2.3, §2.2.5; §3.1–3.4, Tables 2–5, Figs. 4–12.
