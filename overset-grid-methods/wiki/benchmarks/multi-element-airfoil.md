---
type: Benchmark
title: "Multi-element airfoils"
description: "High-lift and flapped airfoils as overset test cases: the SKF 1.1 with manoeuvre flap on a three-level Chimera hierarchy (1983), the inviscid three-element airfoil of the conservative interface (1995), the 30P30N assembled automatically by PEGASUS 5 (2003), and the two-flap Joukowsky airfoil on a composite grid (1990)."
status: established
aliases: [three-element airfoil, high-lift airfoil, 30P30N, SKF 1.1 with flap, flapped airfoil]
tags: [benchmark, chimera, domain-connectivity, conservation, compressible]
timestamp: 2026-11-02T15:42:00Z
---

# Multi-element airfoils

An airfoil with slat and/or flaps is the 2-D configuration that motivates
[overset grids](/definitions/overset-grid.md): each element gets its own
body-fitted grid, the elements' grids cut holes in one another and in a
background grid, and the narrow gaps between elements make
[hole cutting](/methods/hole-cutting.md) and donor choice delicate.
[Benek et al. (1983)](/sources/benek-1983.md) open the Chimera paper with
this example (Fig. 1): grids $G_2$–$G_4$ around the elements could carry
Navier–Stokes equations while the background grid carries Euler or
potential equations; only Euler is demonstrated. Four sources use such
airfoils, each to test a different part of the method.

[Chan (2009, §2, Fig. 1)](/sources/chan-2009.md) retells the same origin in
the NASA Ames history: "using two- and three-element airfoils as
illustrations, a single field grid was constructed around each airfoil
independently", field points of one airfoil's grid lying "inside the outer
mold line of another airfoil" are removed ("blanked points"), and the
points next to holes and on grid boundaries without a flow-solver boundary
condition become fringe points interpolated from a neighbouring grid. Chan's
Fig. 1 sketches the two kinds, hole-boundary fringe points in the background
grid and outer-boundary fringe points of the embedded grid (see
[fringe points](/definitions/fringe-point.md)). Chan credits this framework
to Steger, Dougherty and Benek (1983, ASME FED-Vol. 5), a record distinct
from the AIAA paper of Benek et al. (1983) read here; Chan reports no
airfoil computation. Among Chan's applications, an advanced subsonic
transport with pylons, nacelles and deployed high-lift devices (§11,
Fig. 5) is shown as surface grids only.

## Cases

**SKF 1.1 with manoeuvre flap (Benek et al. 1983, p. 377, Figs. 15–20).**
2-D Euler, implicit approximate factorization. The flap is cut from the aft
part of the SKF 1.1 supercritical airfoil, deflected $10^\circ$ relative to
the main-element chord, with a gap about 1.5 times that of the experiment.
Three-level [hierarchy](/definitions/grid-hierarchy.md): a background
O-mesh ($\ell=1$, $105\times28$) wrapping an airfoil O-mesh ($\ell=2$,
$105\times46$) that contains the main element, and a flap O-mesh ($\ell=3$,
$55\times16$); each mesh overlaps itself by 5 points at its cut, the
$\ell=1$/$\ell=2$ overlap is a uniform 5 points, the $\ell=2$/$\ell=3$
overlap varies; the flap grid cuts a hole in the airfoil grid and the
airfoil grid cuts one in the background grid. Interpolation is the linear
Taylor formula ($q=2$, called "first order" in the paper).
Cases $M_\infty=0.6$ and $0.7$, $\alpha=3^\circ$, against experiment:
agreement is better at 0.6; suction peaks are over-predicted on main element
and flap; at 0.7 the suction-side expansion is over-predicted, the shock
lies too far aft, and the Mach contours show difficulty where the shock
meets a mesh boundary. The single-element SKF 1.1 at $M_\infty=0.76$,
$\alpha=2.5^\circ$ (two-level, same meshes without the flap) shows the same
mismatch near the shock–grid-boundary intersection, tentatively attributed
to the non-conservative interpolation; that case converged 3 times faster
than the single grid (pp. 376–377).

**Inviscid three-element airfoil (Wang 1995, §5.3, Figs. 14–17).** Slat,
main element and trailing-edge flap, experiment of Valarezo et al.:
$M_\infty=0.2$, $\alpha=0.2^\circ$, $Re=9\times10^6$, computed inviscid with
the fully conservative interface of
[Wang (1995)](/sources/wang-1995.md) (finite volume, MUSCL with minmod, Roe
flux). Three zones: slat $85\times7$, main $209\times79$, flap $136\times9$,
outer boundary 10 chords away. $C_p$ agreement is "generally fairly good".
The slat and flap residuals fall to about $10^{-5}$–$10^{-6}$ by 3000
iterations, but the main-element residual stalls after about 1500 iterations
with limit-cycle-like oscillation, attributed to leading-edge separation in
an inviscid model of a physically turbulent flow. See
[conservative overset interface](/methods/conservative-overset-interface.md).

**30P30N (Rogers et al. 2003, "Multi-Element Airfoil", Figs. 9–10).** The
three-element high-lift airfoil of the McDonnell Douglas / NASA Langley
experiment, used to compare [PEGASUS 5](/software/pegasus-5.md) with
PEGASUS 4 connectivity. Grid: 7 zones, 313,000 points (previously used with
PEGASUS 4 in an automated grid-generation procedure). PEGASUS 5 ran in 65 s
on one SGI R10K 250 MHz processor; the only input changes were a global
OFFSET of 2 and OFFSET 5 for both box grids. OVERFLOW solutions at
$M_\infty=0.2$, $Re=9\times10^6$, $\alpha=8.1^\circ$: no visible $C_p$
difference between the PEGASUS 4 and PEGASUS 5 grid systems; both have
higher suction peaks than the experiment. The Cartesian hole map lacks the
resolution for the very thin slat trailing edge, so the actual hole in the
main-element grid ends too close to it; overlap optimization enlarges the
effective hole (Fig. 9).

**Airfoil with two flaps (Chesshire & Henshaw 1990, §6.5, Figs. 22–24,
Table XI).** A Joukowsky main airfoil with two flaps on a
[composite overlapping grid](/definitions/composite-overlapping-grid.md)
built by [CMPGRD](/software/cmpgrd.md): 8101 points, compressible
Navier–Stokes (CGNVT) at $M_\infty=0.5$, $Re=310$ on the main-airfoil length,
implicit on the airfoil and flap grids and explicit on the background.
Grid construction 9.3 s and 0.725 s per step on an IBM 3090VF. Streamlines
and contours only; a comparison with experiment is explicitly disclaimed.

## What each case tests

| Source | Configuration | Flow model | Tested aspect | Reference data |
|---|---|---|---|---|
| Benek et al. (1983) | SKF 1.1 + flap | Euler | hierarchical holes; shocks across overset boundaries | experiment |
| Chesshire & Henshaw (1990) | Joukowsky + 2 flaps | Navier–Stokes, $Re=310$ | composite-grid generation and implicit–explicit solver | none |
| Wang (1995) | slat + main + flap | Euler | conservative interface in narrow gaps | experiment |
| Rogers et al. (2003) | 30P30N | Navier–Stokes (OVERFLOW) | automatic connectivity versus manual PEGASUS 4 | experiment, PEGASUS 4 solution |

No ingested source reports a grid-convergence study or a measured order of
accuracy on a multi-element airfoil. Wang (1995) and Rogers et al. (2003)
both run at $M_\infty=0.2$, $Re=9\times10^6$, but they cite different
experimental reports (Wang: Valarezo et al. 1991; Rogers et al.: Chin et
al. 1993) and Wang does not name the configuration, so the identity of the
two geometries is not established by the sources.

## Multiple solver instances

[Li & Wang (2022)](/sources/li-2022.md) compute the 30P30N with each element as a separate solver instance coupled by dynamic overset assembly, compare surface pressure with experiment and simulate a notional flap deployment (§5.1) ([parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md)).

## Assembly with small gaps

[Ding et al. (2026)](/sources/ding-2026.md) assemble a multi-element airfoil, a circular array of cylinders, multiple spheres and a wing–pylon–store configuration with hybrid hole cutting and island removal (Abstract).

## Qualifications

- Benek et al. (1983) print the airfoil mesh as "G12" in the Fig. 13
  legend, while the text and the other figures call it the level-2 grid
  ("$G_{21}$" in their notation).
- For the single-mesh SKF 1.1 reference grid, Benek et al. (1983, p. 376)
  state that the overlap of "two points on each side" of the cut "reduces
  the effective number of azimuthal points to 100" from 105: five shared
  points (the cut line and two on each side) give $105-5=100$, the same
  5-point overlap as at the cut of the chimera meshes *(compiler check,
  not in the sources)*.
- Wang's three-element case runs an inviscid model of a turbulent flow; the
  residual stall is the author's attribution, not a demonstrated cause.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — Fig. 1 and p. 374 (motivating multi-element airfoil); pp. 376–377, Figs. 11–20 (SKF 1.1, with and without manoeuvre flap).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §6.5 I, Figs. 22–24, Table XI; p. 60 (grid construction time).
- [Wang (1995)](/sources/wang-1995.md) — §5.3, Figs. 14–17.
- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Multi-Element Airfoil", Figs. 9–10.
- [Chan (2009)](/sources/chan-2009.md) — §2, Fig. 1 (two- and three-element airfoils as the illustration of the Chimera framework; field, hole and fringe points); §11, Fig. 5 (high-lift transport surface grids).
- [Li & Wang (2022)](/sources/li-2022.md) — §5.1.
- [Ding et al. (2026)](/sources/ding-2026.md) — Abstract.
