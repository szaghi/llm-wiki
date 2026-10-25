---
type: Method
title: "Wall-modelled large-eddy simulation"
description: "LES that resolves the outer-layer eddies and replaces the near-wall viscous region by a wall-stress model: its definition and cost advantage, the grid-dependent error scaling of mean quantities, the interaction with SGS models, non-monotonic grid convergence, and its demonstrations on aircraft and separated flows."
status: established
aliases: [WMLES, wall-modeled LES, wall-stress-modelled LES, LES with approximate boundary conditions]
tags: [wmles, les, wall-model, boundary-layer, separated-flow]
timestamp: 2026-10-25T13:44:00Z
---

# Wall-modelled large-eddy simulation

Wall-modelled LES (WMLES) is [large-eddy simulation](/definitions/large-eddy-simulation.md)
whose grid resolves eddies that scale with the boundary-layer thickness
$\delta$ but not the viscous near-wall region; the no-slip condition is
replaced by a wall-stress (Neumann) boundary condition computed by a wall model
from the LES state at a matching height $h_{\mathrm{wm}}$
([Goc et al. 2021](/sources/goc-2021.md), §2.2;
[Lozano-Durán et al. 2022](/sources/lozanoduran-2022.md), §II.A). Its
point is cost: the grid count no longer depends on the viscous length near the
wall (see [grid-point requirements](/results/les-grid-point-requirements.md)).
In the classification of Larsson et al. (2016), recalled by
[Fowler et al. (2022)](/sources/fowler-2022.md) (§1) and
[Haering et al. (2022)](/sources/haering-2022.md) (§II), wall-stress models,
where the LES extends to the wall, are distinct from
[hybrid RANS/LES](/definitions/hybrid-rans-les.md), where a RANS region covers
the inner layer. This page covers the wall-stress kind.

## Wall models

| Model | Idea | Page |
|---|---|---|
| Equilibrium (ODE or algebraic) | constant-stress inner layer, law of the wall inverted at $h_{\mathrm{wm}}$ | [equilibrium wall model](/methods/equilibrium-wall-model.md) |
| LaRTE | transport equation for the friction-velocity vector, relaxing towards equilibrium with the inertia of the layer below $h_{\mathrm{wm}}$; optional laminar Stokes-layer stress | [LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md) |
| Inverse velocity transformation | incompressible ODE mapped to compressible profiles plus an algebraic temperature–velocity relation | [inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md) |
| Learned (supervised or reinforcement learning) | network maps LES state to $\tau_w$ or to its update | [machine-learning wall models](/methods/machine-learning-wall-model.md) |

Fowler et al. (2022, §1) and [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md)
(§I, §II.A) also recall zonal two-layer models on a separate RANS mesh (whose
cost can approach wall-resolved LES), the integral wall model of Yang et al.
(2015), the dynamic slip wall model of Bose & Moin (2014) and Bae et al. (2019),
and a POD-inspired model; none is formulated in the sources read.

## Error scaling: WMLES as a convergence study

Lozano-Durán et al. (2022, §IV.A) argue that WMLES is intrinsically
grid-dependent — "the grid size is an explicit variable of the governing
equations" — and must be assessed by convergence studies. Following
Lozano-Durán & Bae, as they recall it, they posit for a mean quantity $q$
the relative error (page-local symbols $e_q$, $b_q$, $a_q$)

$$e_q=\frac{\lVert\langle q_{\mathrm{exp}}\rangle-\langle q\rangle\rVert}{\lVert\langle q_{\mathrm{exp}}\rangle\rVert}=b_q\left(\frac\Delta\delta\right)^{a_q},$$

with $\Delta$ the local isotropic grid size, which is also the implicit filter
width. Their results:

- **Wall pressure** is an outer-layer, inviscid quantity: under the
  thin-boundary-layer approximation the wall pressure equals the inviscid
  pressure, so $b_p\ll1$ and $a_p\approx0$ (Eq. 10). $C_p$ errors stay below
  5 % on all their grids, even with 0–1 points per $\delta$, and a free-slip
  run without SGS model gives nearly the same $C_p$ (§V.E, Figs. 20–21).
- **Mean velocity** scales with $a_u=0$ when $\Delta/\delta$ lies in the
  shear-dominated range and $a_u=1$ in the inertial range (Eq. 11). In
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md) at
  $Re_\tau=4200$ ([CharLES](/software/charles.md), dynamic Smagorinsky,
  equilibrium wall model, $\Delta/\delta=1/3,1/5,1/10$) they find
  $e_u\approx0.08\,\Delta/\delta$, with the same linear trend from a staggered
  finite-difference solver (§IV.B, Fig. 7b). The difference between DNS and an
  inviscid solution, about 15 %, bounds the mean-velocity error of even a poor
  WMLES of canonical flows.
- **Corners.** Near a second wall the error is controlled by the local shear
  length $u_\tau/|\mathrm dU/\mathrm dy|$, so $e_u\sim\Delta/d$ with $d$ the
  distance to the nearest wall (§IV.B).
- **Resolved stresses** are under-predicted where the subgrid share is large,
  since the experimental stress is approximately the resolved plus the mean
  SGS stress; turbulence-intensity errors scale as $(\Delta/\delta)^{2/3}$ with
  10–30 % values (§V.B, recalled from Lozano-Durán & Bae).

On the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md) the
mean-velocity error is 3–8 % on the fuselage with $b_u\approx0.14$ (above the
channel value because of upstream error propagation), about 15 % in the
wing–body juncture with $a_u\approx0.4$, and about 100 % in the separated
trailing-edge corner with $a_u\approx0.6$ (§V.B, Fig. 15). Errors generated at
an under-resolved leading edge travel downstream over a recovery length of
about $300\delta_0$; a [boundary-layer-conforming grid](/methods/boundary-layer-conforming-grid.md)
lowers $b_u$ but not $a_u$ (§V.C).

The error of the wall model itself splits into external (LES velocity at the
matching point) and internal (model constants) parts, analysed on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) page.

## Agreement on what converges first

Three sources agree that outer, pressure-dominated quantities converge at much
coarser grids than near-wall and separated quantities. Lozano-Durán et al.
(2022) find $C_p$ insensitive to resolution and the separation bubble about
15 % smaller than the oil-film measurement (§V.F). Goc et al. (2021, §3) predict
$C_{L,\max}$ of the [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
within five lift counts at about ten points across the trailing-edge boundary
layer, while drag errors persist at the finest free-air grids (§3.2) and the
flap separation bubble collapses on the finest in-tunnel grid (§3.3).
[Agrawal et al. (2022)](/sources/agrawal-2022.md) (§VIII.B) note that the
suction peak of the Gaussian bump is primarily inviscid and is predicted by a
free-slip run, whereas separation needs the finest grid (first cell at
$y^+\sim30$ upstream).

## Grid convergence can be non-monotonic

- **Channel.** Lozano-Durán et al. (2022, App. B, Figs. 23–24) find the
  mean-velocity error departs from $e_u\sim\Delta$ around
  $\Delta/\delta\approx0.03$–$0.05$ in both CharLES and a staggered
  finite-difference solver, and recovers the linear trend below 0.03. Runs
  without SGS model and with the exact DNS mean wall stress show a qualitative
  change at a critical $\Delta_c/\delta\approx0.03$–$0.05$: noisy structure
  above it, near-wall streaks below it. The authors "still lack a satisfactory
  explanation of the phenomenon and … a robust remedy".
- **Separated flows.** On the spanwise-periodic Gaussian bump
  ($Re_L=2\times10^6$), dynamic Smagorinsky and Vreman separate on the coarse
  grid, lose the separation on the medium grid and recover it on the fine grid,
  while the [dynamic tensor-coefficient model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
  converges monotonically towards the quasi-DNS $C_f$ (Agrawal et al. 2022,
  §VIII.A, Fig. 13). Agrawal et al. recall similar non-monotonic behaviour in
  high-lift aircraft simulations. Goc et al. (2021, §3.3) report that the
  flap separation bubble seen experimentally and on their coarse and medium
  in-tunnel grids is suppressed on the finest one, recall a similar collapse
  under refinement by Iyer & Malik (2021) for a Gaussian bump, and leave cause
  and remedy open.

## Interaction with the SGS model

The wall model and the SGS model ([large-eddy simulation](/definitions/large-eddy-simulation.md)) act on the
same under-resolved first cells.

- Both dynamic models of Agrawal et al. (2022, §VII.D) under-predict the SGS
  stress there; the [dynamic procedure](/methods/dynamic-procedure.md) needed
  clipping at the second off-wall point at $Re_\tau=4200$, the tensor-coefficient
  model none, and the log-region slope error relative to $\kappa=0.38$ fell
  from 7 % to 5 % (Figs. 8–10). They impose $d\tau_{ij}/dy=0$ at the wall for
  the SGS stress, because resolved stresses do not vanish at the wall of a
  coarse WMLES.
- Fowler et al. (2022, §5.1) attribute the WMLES–DNS differences in
  $\langle u'u'\rangle$ (under-predicted) and $\langle w'w'\rangle$
  (over-predicted) near the wall to grid and SGS model, because two different
  wall models give the same statistics.
- Vadrot et al. (2023b, App. B) find little effect of replacing the
  anisotropic minimum-dissipation SGS model by a Lagrangian scale-dependent
  dynamic model at $Re_\tau=5200$, for the equilibrium and the learned models
  alike.
- [Krais et al. (2021)](/sources/krais-2021.md) (§7.3) report that the Vreman
  model "helps to reduce artificial pressure fluctuations caused by the
  wall-model" in a high-order DG zonal LES of an open cavity.
- [Griffin et al. (2023)](/sources/griffin-2023.md) (§4) recall that
  stress-based wall models over-predict near-wall resolved fluctuations through
  a wall-blocking effect (Bae et al. 2018).
- [Implicit LES](/definitions/implicit-les.md) without wall model is not a
  substitute at WMLES resolution: implicit
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  predicts $u_\tau$ in pipe flow at $Re_\tau=2000$ within about 1.9 % at
  $\Delta x^+=9$ but under-predicts it by more than 12 % at $\Delta x^+=18$, and the authors
  conclude it "cannot be used alone in the context of WMLES"
  ([Vicente Cruz & Lamballais 2023](/sources/vicentecruz-2023.md), §7.4).

Low numerical dissipation is a precondition: Goc et al. (2021, §2.3) call
[numerical dissipation](/properties/numerical-dissipation.md) "extremely
detrimental" for coarse LES and use kinetic-energy- and entropy-preserving
schemes ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

## Demonstrations

- **High-lift aircraft** (Goc et al. 2021): JAXA Standard Model at
  $Re_c=1.96\times10^6$, $M_\infty=0.172$, $Re_\tau\approx5000$; Vreman (free
  air) or dynamic Smagorinsky (in tunnel) with the equilibrium wall model; 32 M
  Voronoi cells give the lift curve and $C_{L,\max}$; wind-tunnel walls and
  nacelle are needed for the inboard separation and the pitching-moment
  kickback. A medium-grid run costs about $40\times10^3$ core-hours (21 h on
  2000 CPU cores, 48 min on 96 V100 GPUs), comparable to a steady RANS run of
  the workshop; the authors judge WMLES of high-lift aircraft "on the threshold
  of readiness for industrial use" (§4–5).
- **Wing–body juncture** (Lozano-Durán et al. 2022): the juncture flow at
  $Re=2.4\times10^6$ on the crank chord, eight grids from 6 M to 174 M cells,
  13–398 thousand core-hours.
- **Smooth-body separation** (Agrawal et al. 2022, §VIII): the Boeing Gaussian
  bump, spanwise-periodic ($Re_L=2\times10^6$, against quasi-DNS) and 3D
  ($Re_L=3.41\times10^6$, against experiment); on the finest grid both dynamic
  models predict the bubble and the counter-rotating vortex pair, while
  Vreman misses separation in 3D.
- **Non-equilibrium channel** (Fowler et al. 2022, §5.2): sudden spanwise
  pressure gradient at $Re_{\tau0}=1000$.
- **Compressible channels** (Griffin et al. 2023, §4): $M_b=0.7$–$4$,
  $Re_\tau=320$–$1800$, 12 points per half-height.

## Qualifications

- Haering et al. (2022, §V.B) estimate a WMLES of the [periodic hill](/benchmarks/periodic-hill.md)
  at about 12 M cells (structured) or 1.6 M (streamwise-varying grid), using
  spacings of at most 8 %, 2 % and 5 % of $\delta$; both exceed the 0.9 M cells
  of their fine [active model split](/methods/active-model-split.md) grid. The
  estimate is theirs; no WMLES of the hill is run.
- Locators of Lozano-Durán et al. (2022) refer to the arXiv v1 preprint read, not the AIAA Journal version.

# Citations

- [Goc et al. (2021)](/sources/goc-2021.md) — §1–5, Figs. 5–14, Tables 1–2.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II–V, Eqs. (8)–(12), Figs. 7, 15–24; App. B.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D, §VIII, Figs. 8–19.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §1; §5.1–5.2.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I; §II.A; App. B.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1; §4.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II; §V.B.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §7.4, Fig. 28.
- [Krais et al. (2021)](/sources/krais-2021.md) — §7.3, Fig. 27.
