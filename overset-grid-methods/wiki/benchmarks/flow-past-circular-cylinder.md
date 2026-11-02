---
type: Benchmark
title: "Flow past a circular cylinder"
description: "The circular cylinder on a background grid plus a body-fitted annular grid as the basic overset test: subcritical and supercritical Euler flow (1983), manufactured and Mach 2 impulsive-start Navier–Stokes convergence studies (1990), fourth-order incompressible flow at Re 100 and Wannier's Stokes solution (1994), and shock diffraction (1995)."
status: established
aliases: [cylinder in cross flow, cylinder in a channel, impulsively started cylinder, Wannier flow, shock diffraction by a cylinder]
tags: [benchmark, chimera, composite-grid, high-order, incompressible, compressible]
timestamp: 2026-11-02T11:28:00Z
---

# Flow past a circular cylinder

The smallest non-trivial [overset grid](/definitions/overset-grid.md) is a
Cartesian background grid with a body-fitted annular (polar) grid around a
circular cylinder: one hole, one ring of receptors on each grid, a smooth
geometry and flows with known reference solutions. Chunk-1 sources use it to check that the
overlap does not perturb the solution, to measure convergence rates across
the interpolation boundary, and to watch shocks and vortices cross it.

## Cases

**Subcritical and supercritical Euler flow (Benek et al. 1983, p. 376,
Figs. 8–10).** [Benek et al. (1983)](/sources/benek-1983.md): 2-D Euler on
a two-level hierarchy, a $51\times51$ stretched Cartesian grid ($\ell=1$)
and a polar grid with 85 circumferential and 30 radial points ($\ell=2$);
the overlap is "extensive", from the sixth to the thirtieth radial point.
Interpolation is the linear Taylor formula ($q=2$).
- $M_\infty=0.25$: the overset solution and a single-grid Euler solution on
  a $90\times70$ polar grid are "indistinguishable", and both agree
  favourably with a potential solution with Prandtl–Glauert correction
  ($C_p$ against $x/R$, Fig. 9).
- $M_\infty=0.5$ (supercritical): two vortices form, then shed
  asymmetrically, as described by Salas; the vortices "appear to experience
  no difficulty crossing between grids" (Fig. 10).

**Manufactured Navier–Stokes solution, cylinder in a channel (Chesshire &
Henshaw 1990, §6.4 Test 1, Fig. 18, Tables V–VI).**
[Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) force the
compressible Navier–Stokes equations so that $\rho$, $u$, $v$, $T$ equal
chosen trigonometric functions ($Re=50$, $M=0.85$, $Pr=1$, $\gamma=1.4$);
no-slip cylinder, subsonic inflow and outflow, symmetry top and bottom; two
component grids (background and annulus) at three resolutions with spacing
ratio $2:\sqrt2:1$: $70\times50$ and $51\times7$; $99\times71$ and
$72\times10$; the finest printed "$139\times199$" and $101\times13$. Maximum
errors at $t=1$ fall by ratios 2.0–2.2 between successive grids
(e.g. $\rho$: 0.52, 0.25, 0.12), the factor 2 that second order gives when
$h$ shrinks by $\sqrt2$, interpolation included. See [twilight-zone flow](/methods/twilight-zone-flow.md).

**Impulsively started cylinder at Mach 2 (Chesshire & Henshaw 1990, §6.4
Test 2, Figs. 19–21, Tables VII–VIII).** $Re=50$, $M=2.0$, $Pr=0.71$,
isothermal no-slip cylinder, supersonic inflow; the viscous bow shock forms
and moves upstream, crossing the interpolation boundary nearly parallel to
it. Same three grids; self-convergence ratios
$\lVert u_1-u_3\rVert/\lVert u_2-u_3\rVert$ (subscripts: grid level, $u_3$
the finest), expected 3 for second order: 2.5–4.8 in the max norm and
2.8–4.0 in $\ell_2$ at $t=1$ and $t=10$. On the coarsest grid the shock "has
some difficulty crossing the interpolation boundary" (contours do not join
smoothly); on the two finer grids it is well represented. Discretization
and interpolation are non-conservative; the authors hold that conservation
is "not crucial" when the shock is resolved (§6.4).

**Stokes flow near a moving wall (Henshaw 1994, §5.1.1, Table IV,
Fig. 2).** [Henshaw (1994)](/sources/henshaw-1994.md) compares the
fourth-order incompressible solver with Wannier's exact Stokes solution for
a cylinder near a wall moving at constant speed: two overlapping grids,
$27^2\cup(9\times43)$ and $53^2\cup(17\times85)$; velocity error
$7.3\times10^{-4}\to5.6\times10^{-5}$ ($\sigma=3.7$), maximum divergence
$8.5\times10^{-3}\to3.8\times10^{-4}$ ($\sigma=4.5$). Interpolation is
width $q=5$ (biquartic) with two receptor lines. The values of wall speed,
radius and wall distance are not printed. See
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

**Unsteady flow at $Re=100$ (Henshaw 1994, §5.1.2, Figs. 3–5, Table V).**
Cylinder of radius 1/2 at the origin in $[-2.5,15]\times[-3.5,3.5]$,
$\nu=1/100$ (Reynolds number on diameter and unit inflow speed), projected
uniform initial flow, slip walls, no-slip cylinder; 14,581 points, fourth
order. A Kármán vortex street appears only after $t\approx40$; the ratio of
maximum divergence to maximum vorticity stays below about
$3\times10^{-3}$. No Strouhal number or drag is reported. Cost 1.5 s per
step on an IBM RS/6000-530 (pressure solve 27%, explicit interpolation 2%).

**Shock diffraction (Wang 1995, §5.4, Figs. 18–20).** A planar $M=1.5$
shock impinges on a circular cylinder on a Cartesian background plus a
body-fitted polar grid (sizes not given), with the fully conservative
interface of [Wang (1995)](/sources/wang-1995.md). Shocks and slip lines
pass through and along the interface; agreement with an experimental
shadowgraph is described as "very good" (qualitative). See
[conservative overset interface](/methods/conservative-overset-interface.md).

## Measured convergence across the overlap

| Source | Problem | Interpolation | Observed rate |
|---|---|---|---|
| Chesshire & Henshaw (1990) | manufactured compressible NS | as built by CMPGRD for a second-order scheme | error ratio 2.0–2.2 per refinement by $\sqrt2$ (second order) |
| Chesshire & Henshaw (1990) | Mach 2 impulsive start | same | self-convergence ratios 2.5–4.8 (expected 3) |
| Henshaw (1994) | Wannier Stokes flow | $q=5$, two receptor lines | $\sigma=3.7$ (velocity), 4.5 (divergence) |

The rates agree with the
[interpolation-order requirement](/results/interpolation-order-requirement.md)
in the sense that both papers choose interpolation widths by it; neither
varies the width on the cylinder case. Benek et al. (1983) and Wang (1995)
report no convergence rate.

## Qualifications

- Chesshire & Henshaw (1990, Table V) print the finest background grid as
  $139\times199$, while the stated spacing ratio and the coarser entries
  ($70\times50$, $99\times71$) give about $139\times99$ *(compiler check,
  not in the sources)*.
- Their Test 2 text compares contours "at times $t=1$ and $t=3$", while the
  Fig. 19 caption labels panels $t=2$ and $t=3$; and Table VIII prints an
  $\ell_2$ ratio of 3.6 for $T$ at $t=1$ where its own entries give
  $0.035/0.012\approx2.9$ *(compiler check, not in the sources)*.
- Henshaw (1994) prints the Wannier parameters with lowercase $s$ in two
  definitions and uses $D$ both for the wall distance and for the constant
  $-U$.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 376, Figs. 8–10 (Euler cylinder, $M_\infty=0.25$ and $0.5$).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §6.4 Tests 1–2, Figs. 18–21, Tables V–VIII.
- [Henshaw (1994)](/sources/henshaw-1994.md) — §5.1.1 Table IV, Fig. 2 (Wannier); §5.1.2 Figs. 3–5, Table V ($Re=100$).
- [Wang (1995)](/sources/wang-1995.md) — §5.4, Figs. 18–20 (shock diffraction).
