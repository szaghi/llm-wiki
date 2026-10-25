---
type: Method
title: "Boundary-layer-conforming grids for wall-modelled LES"
description: "Grids whose local isotropic cell size follows the local boundary-layer thickness, floored by a minimum grid Reynolds number at leading edges and capped by surface curvature; the boundary-layer-thickness estimate they need, their cost, and the evidence that they reduce WMLES error at fewer points than constant-size grids."
status: established
aliases: [BL-conforming grid, boundary-layer-conforming mesh, delta-conforming grid]
tags: [wmles, mesh-adaptation, boundary-layer, wall-model]
timestamp: 2026-10-25T13:44:00Z
---

# Boundary-layer-conforming grids for wall-modelled LES

A boundary-layer-conforming (BL-conforming) grid sets the local, isotropic cell
size $\Delta$ of a [wall-modelled LES](/methods/wall-modelled-les.md) to a fixed
fraction of the local boundary-layer thickness, $\Delta\approx\delta/n_\delta$,
so that every boundary layer is resolved by the same number of points
$n_\delta$ (page-local) across its thickness. [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)
formulate it, build it for the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
in [CharLES](/software/charles.md), and compare it with constant-size grids;
they state that all published WMLES cost estimates assume such a grid, yet
"WMLES of an aircraft geometry has never been conducted using a true
BL-conforming grids until the present work" (§III.B). [Goc et al. (2021)](/sources/goc-2021.md)
(§2.2) cite the same work as the route to reducing WMLES cost, and use the
simpler constant-size practice described below.

## Grid-size rule

Because $\delta\to0$ at leading edges, the rule needs a floor; because $\delta$
can exceed the local radius of curvature, it needs a cap. Lozano-Durán et al.
(2022, §III.A, Eq. 2) set

$$\Delta(\boldsymbol x)\approx\min\left[\max\left(\frac{1.2\,\delta}{n_\delta},\ \frac{Re_\Delta^{\min}\,\nu}{U_\infty}\right),\ \frac{R_c}{2}\right],$$

with $R_c$ the local surface radius of curvature (page-local), the factor 1.2 a
margin to contain the instantaneous boundary layer, and
$Re_\Delta^{\min}=\Delta_{\min}U_\infty/\nu$ "the minimum local Reynolds number
that we are willing to marginally resolve": where the boundary layer is
thinner than $\delta_{\min}=n_\delta\Delta_{\min}$ the grid size stays at
$\Delta_{\min}$. The grid is locally isotropic and blends to a far-field size
(200 mm in their case). Both of their gridding strategies build Voronoi cells
from hexagonally close-packed seeds; for the constant-size grids they state
ten Lloyd iterations to smooth the transitions between layers.

The two parameters separate two questions: $n_\delta$ sets the accuracy of
the developed boundary layers, $Re_\Delta^{\min}$ the treatment of the leading
edge.

## Estimating the boundary-layer thickness

The rule needs $\delta$ on the whole surface before the production grid
exists. Lozano-Durán et al. (2022, §III.A, Eqs. 3–4) run two simulations on a
preliminary constant-size grid ($\Delta=2$ mm): a WMLES, and an inviscid one
(free-slip walls, no SGS model). The boundary-layer edge is the surface where
the time-averaged velocities differ by 1 %,

$$\frac{\lVert\langle\boldsymbol u_I\rangle-\langle\boldsymbol u\rangle\rVert}{\lVert\langle\boldsymbol u_I\rangle\rVert}=0.01 ,$$

with $\boldsymbol u_I$ the inviscid velocity (page-local), and $\delta$ at a
surface point is its distance to that edge surface. Layers thinner than 2 mm at
the leading edge are extrapolated by a power law; Q-criterion isosurfaces as
edge surface gave similar results. On the Juncture Flow $\delta$ runs from
about 0 at the wing leading edge to about 30 mm at the wing trailing edge and
over 50 mm on the aft fuselage (Fig. 5c).

## Cost

Counting only points inside the boundary layer (Eq. 5),
$N_{\mathrm{pts}}=\iint_{S}n_\delta\,\Delta^{-2}\,dA$, and for a flat plate with
$\delta/x=0.16\,Re_x^{-1/7}$ and $Re\gg Re_\Delta^{\min}$ (Eq. 6, App. A),

$$N_{\mathrm{pts}}\sim n_\delta^{13/6}\,Re\,\left(Re_\Delta^{\min}\right)^{-5/6},\qquad N_{\mathrm{steps}}\sim\tilde t\,Re\left(Re_\Delta^{\min}\right)^{-1},$$

with $\tilde t$ the run length in flow-through times (page-local). With the
leading-edge extent fixed instead of $Re_\Delta^{\min}$ the exponent of
$n_\delta$ becomes 3 (Eq. 14). Further consequences are on the
[grid-point requirements](/results/les-grid-point-requirements.md) page.

## Evidence

On the Juncture Flow at $Re=2.4\times10^6$ (crank chord), Lozano-Durán et al.
(2022, §V) compare five constant-size grids (C-D7 to C-D0.5, 14–174 M cells,
31–398 thousand core-hours) with three BL-conforming ones:

| Case | $n_\delta$ | $Re_\Delta^{\min}$ | $\Delta_{\min}$ | Cells | Core-hours |
|---|---|---|---|---|---|
| C-N5-R2e3 | 5 | $2.8\times10^3$ | 0.6 mm | 12 M | 27 000 |
| C-N10-R2e3 | 10 | $2.8\times10^3$ | 0.3 mm | 40 M | 90 000 |
| C-N5-R5e3 | 5 | $5.6\times10^3$ | 1.3 mm | 6 M | 13 000 |

- BL-conforming grids are more accurate at all three stations; at the
  wing–body juncture and the separated trailing edge they lower the error
  constant $c_u$ of $e_u=c_u(\Delta/\delta)^{a_u}$ (page-local, see
  [wall-modelled LES](/methods/wall-modelled-les.md)) and leave the rate
  $a_u$ unchanged (§V.C, Fig. 17a).
- C-N5-R2e3 (12 M cells) beats the constant-size C-D2 (31 M) at the juncture
  and trailing edge "using only one fourth of the number of grid points in each
  spatial direction (namely, a factor of 64 less points in the local volume)";
  the number of control volumes is therefore "a misleading metric" of WMLES
  quality (§V.C, Fig. 16).
- **Why constant-size grids lose.** A constant-size grid is agnostic of
  $\delta$: it puts less than one point per $\delta$ on the nose and wing
  leading edge and up to hundreds on the aft fuselage (§III.A). Errors made at
  the under-resolved leading edge are advected downstream over a recovery
  length $\Delta x_e\approx\Gamma U_\infty\delta_0/u_\tau$, about $300\delta_0$
  in high-$Re$ zero-pressure-gradient layers (page-local $\Delta x_e$,
  $\Gamma$, $\delta_0$). Re-plotting errors against an upstream
  Gaussian-averaged thickness collapses the constant-size fuselage errors onto
  the channel reference, "confirming that the diminished performance of
  constant-size grids is merely a matter of downstream error propagation"
  (§V.C, Fig. 17b).
- **Leading-edge parameter.** Halving $Re_\Delta^{\min}$ improves downstream
  profiles; errors converge as $(Re_\Delta^{\min})^{a}$ with $a\approx1$–2,
  steeper than in $n_\delta$, so leading-edge requirements are less demanding
  than those of the developed layers (§V.D, Fig. 19d). A model
  $e_u\sim n_\delta^{-1}\left[1+\Gamma Re_\Delta^{\min}n_\delta/\big(Re_x-(Re_\Delta^{\min}n_\delta/0.16)^{7/6}\big)\right]$
  with $\Gamma=300$ reproduces the trend. The under-resolved region for
  $Re_\Delta^{\min}<10^4$ covers less than 10 % of the chord (§III.B, Fig. 6b).
- The wall pressure is insensitive to all of this (errors below 5 % on every
  grid); the advantage concerns the velocity field.

## Constant-size practice for comparison

Goc et al. (2021, §3, §4) size their [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
grids uniformly and isotropically in all directions for about ten points
across the main-element trailing-edge boundary layer, $\delta_{99}/\Delta\approx10$,
predicted by a zero-pressure-gradient correlation on the mean aerodynamic
chord, with extra clustering at the slat leading edge for the inviscid
acceleration; the leading edges thus receive fewer points per $\delta$. They
generalize the practice as "a chosen $O(1)$ number of cells per boundary-layer
thickness at the trailing edge of the main element", complemented near leading
edges by keeping the grid spacing times the pressure gradient small for the
scheme used. This sufficed for $C_{L,\max}$ within five lift counts; the
coarsest grid under-predicts the outboard slat and main-element suction,
which they link to under-resolved leading-edge acceleration (§3.2, Fig. 9).

## Qualifications

- The method has one source of evidence, on one geometry and one Reynolds
  number; its rule depends on a preliminary WMLES and inviscid solution.
- Lozano-Durán et al. contrast their low leading-edge sensitivity at small
  angle of attack with NACA 0012 cases in which the whole-chord solution
  depended strongly on leading-edge grid details (Goc, personal communication,
  as they recall it, §V.D).
- Printed slips in the version read (arXiv v1): §V.D gives
  $Re_\Delta^{\min}=2.6\times10^3$ and $5.8\times10^3$ for C-N5-R2e3 and
  C-N5-R5e3, while §V.A, the Fig. 18 caption and the case names give
  $2.8\times10^3$ and $5.6\times10^3$; §V.A says "the first six cases" use
  constant-size grids where five are listed.

# Citations

- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §III.A, Eqs. (2)–(4), Figs. 3–5; §III.B, Eqs. (5)–(7), Fig. 6; §V.A–V.E, Figs. 16–21; App. A, Eqs. (13)–(14).
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.2; §3, Fig. 9; §4.
