---
type: Benchmark
title: "Flow past a circular cylinder"
description: "The circular cylinder on a background grid plus a body-fitted annular grid as the basic overset test: Euler flow (1983), manufactured and Mach 2 Navier–Stokes convergence studies (1990), fourth-order incompressible flow (1994), shock diffraction (1995), interpolation order at Re 100 and side-by-side cylinders (2005), a moving cylinder and Maxwell tests (2006), and stationary and rotating cylinders at Re 200 (2021)."
status: established
aliases: [cylinder in cross flow, cylinder in a channel, impulsively started cylinder, Wannier flow, shock diffraction by a cylinder, side-by-side cylinders, rotating cylinder]
tags: [benchmark, chimera, composite-grid, high-order, incompressible, compressible]
timestamp: 2026-11-02T15:09:00Z
---

# Flow past a circular cylinder

The smallest non-trivial [overset grid](/definitions/overset-grid.md) is a
Cartesian background grid with a body-fitted annular (polar) grid around a
circular cylinder: one hole, one ring of receptors on each grid, a smooth
geometry and flows with known reference solutions. The sources use it to
check that the overlap does not perturb the solution, to measure
convergence rates across the interpolation boundary, to compare
interpolation orders and inter-grid coupling strategies, and to watch
shocks and vortices cross it.

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

**Low-Mach viscous flow at $Re_D=100$ with high-order interpolation
(Sherer & Scott 2005, §5.3, Fig. 19).** [Sherer & Scott (2005)](/sources/sherer-2005.md)
run their sixth-order compact scheme with a tenth-order filter at
$M_\infty=0.1$, $Re_D=100$, $D=1$, $\Delta t=0.002$, on three grid systems:
a single O-grid (reference), the same grid split into two O-grids coupled by
direct injection, and an overset version in which the outer O-grid is
rotated so that no points coincide. The overlap is uniform and minimal: the
smallest that avoids "circular interpolation" (a donor point that is itself
a receptor of the grid it serves) with a two-point fringe ($n_f=2$). The
drag-coefficient histories show fourth- and sixth-order explicit Lagrange
interpolation ($q=4$, $q=6$) matching direct injection, fourth-order
B-spline interpolation worse because the small overlap puts receptors in
the outer subintervals of the stencil, and second-order interpolation
($q=2$) worst. No drag or Strouhal value is tabulated. The interpolation
families are on [inter-grid interpolation](/methods/inter-grid-interpolation.md)
and the solver on
[high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md).

**Two side-by-side cylinders (Sherer & Scott 2005, §5.3, Figs. 20–22).**
Two cylinders of diameter $D=1$, centres $1.3D$ apart and not staggered, on
seven grids (a polar grid per cylinder, a wake grid, background grids)
split into 32 parallel blocks, with mutual hole cutting and sixth-order
explicit interpolation, $Re_D=100$. At a probe $4D$ downstream and
$2.65D$ off the axis the fundamental Strouhal number is $S_F\approx0.09$,
matching the experimental value of about 0.09 the authors cite; the
asymmetric gap flow is reproduced qualitatively.

**Stationary and rotating cylinder at $Re=200$ (Sharma et al. 2021,
§4.3.3–4.3.4, Figs. 26–34).** [Sharma et al. (2021)](/sources/sharma-2021.md)
use the case to test inter-grid coupling in an incompressible node-centred
finite-volume solver (Nalu-Wind, implicit BDF2) with assembly by the TIOGA
library. Setup: a thin 3-D box $30\times20\times0.1$ with the cylinder
($D=1$) 10 diameters from the inflow; a near-body O-type grid overlapping a
Cartesian background; $U_\infty=1$, $\rho=1$, $\mu=0.005$, so $Re=200$;
linear Lagrange interpolation ($q=2$).
- Solving all grids as one linear system with the interpolation equations
  as constraint rows (the "overset single system"), the drag coefficient
  and Strouhal number converge asymptotically under refinement and agree
  with the literature values they cite (Braza et al., Henderson, Farrant et
  al., Posdziech & Grundmann) (§4.3.3, Fig. 29).
- Solving the grids separately with fringe values exchanged between
  iterations (overset additive Schwarz), two outer (Picard) iterations with
  one exchange each give maximum, minimum and mean drag, lift extremes and
  Strouhal number within 1% of the single-system solution, even on the
  coarsest mesh; extra Picard iterations help more than extra exchange
  iterations, which the authors read as split-operator errors dominating
  inter-grid errors (§4.3.3, Figs. 30–31).
- With the near-body grid rotating clockwise at a rotation rate (surface
  speed over $U_\infty$) of 3 (Sharma et al.'s $\alpha$, not written as a
  symbol here because the registry's $\alpha$ is the angle of attack), a single vortex is shed, the lift coefficient converges in space
  and time and agrees with Mittal & Kumar (2003) and Padrino & Joseph
  (2006) as cited, and the Schwarz variant stays within 1% of the single
  system (§4.3.4, Figs. 32–34). This is the bundle's only rotating-cylinder
  case; see [moving overset grids](/methods/moving-overset-grid.md) and
  [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).
Node counts are given in figures only and are not transcribed here.

**Smoothly accelerating cylinder, inviscid (Henshaw & Schwendeman 2006,
§6.3.1, Figs. 14–15, Table 4).** [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md)
move a cylinder of radius $1/2$ with centre $x_{\mathrm{cg}}(t)=-1+2\sin^4(\pi t/24)$
through a channel $[-2,2]\times[-5/4,5/4]$ (periodic in $x$, slip walls),
gas initially at rest with $\rho=\gamma=1.4$, $p=1$, using an annular grid
that moves with the body over a fixed Cartesian grid; spacing
$h_j=1/(10j)$ with 6 radial intervals. Self-convergence on $j=4,8,16$ at
$t=6$ measures the slip-wall boundary condition on a curved moving wall:
their compatibility-based condition gives max-norm rates 2.03, 1.83, 1.84
($\rho$, $v$, $T$), the reflection (symmetry) condition 1.56, 1.04, 1.57
with errors several times larger and non-smooth wall pressure. The shocked
variants of the same geometry (a Mach 1.5 shock driving a free cylinder)
are on [shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md),
with the Mach 3 cylinder of [Picard et al. (2021)](/sources/picard-2021.md).

**Other physics on the cylinder-in-a-channel grid (Henshaw 2006, §10.1,
§10.3).** [Henshaw (2006)](/sources/henshaw-2006-b.md) reuses the geometry
for Maxwell's equations: a Cartesian grid on $[-2,2]^2$ ($61\times61$
points) with an annulus of radii $1/2$ and $3/4$ ($81\times5$), refined
twice by factors 2, perfect-conductor boundaries, manufactured solution
at $t=1$. The fourth-order scheme with $q=5$ interpolation gives max-norm
rates 4.40, 3.93, 4.02 for $E_x$, $E_y$, $H_z$ and 3.94 for the normalized
divergence. Plane-wave scattering by a dielectric cylinder is on
[Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md).

[Horne & Mahesh (2021)](/sources/horne-2021.md) validate their GPU overset
solver on a sphere at $Re=3700$, not on a cylinder
([flow past a sphere](/benchmarks/flow-past-sphere.md)).

## Measured convergence across the overlap

| Source | Problem | Interpolation | Observed rate |
|---|---|---|---|
| Chesshire & Henshaw (1990) | manufactured compressible NS | as built by CMPGRD for a second-order scheme | error ratio 2.0–2.2 per refinement by $\sqrt2$ (second order) |
| Chesshire & Henshaw (1990) | Mach 2 impulsive start | same | self-convergence ratios 2.5–4.8 (expected 3) |
| Henshaw (1994) | Wannier Stokes flow | $q=5$, two receptor lines | $\sigma=3.7$ (velocity), 4.5 (divergence) |
| Henshaw & Schwendeman (2006) | accelerating cylinder, Euler, self-convergence | Lagrange, width not stated | $\sigma=1.83$–2.03 (max norm) with their slip-wall condition |
| Henshaw (2006) | Maxwell, manufactured | $q=5$ | $\sigma=3.93$–4.40 (max norm) |
| Sharma et al. (2021) | $Re=200$ cylinder | $q=2$ | asymptotic convergence of $C_d$, $St$ (rates not printed) |
| Sherer & Scott (2005) | $Re_D=100$ cylinder | $q=2,4,6$; B-spline | drag histories only; $q\ge4$ matches direct injection |

The rates of the first two rows agree with the
[interpolation-order requirement](/results/interpolation-order-requirement.md)
in the sense that both papers choose interpolation widths by it; neither
varies the width on the cylinder case. Sherer & Scott (2005) are the only
source that varies the interpolation order on a cylinder, and find that
$q=2$ visibly degrades a sixth-order solver's drag history while $q\ge4$
does not. Benek et al. (1983), Wang (1995) and Picard et al. (2021) report
no convergence rate on an unshocked cylinder.

## Moving and incompressible cylinders (2022 sources)

| source | case | result |
|---|---|---|
| [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) | steady cylinder at $Re=200$ on two overlapping grids; impulsively started and stopped cylinders at $Re=40$, 200, 550 on a moving foreground grid | $C_D=1.3430$, $St=0.1979$, within the literature ranges (Table 3); drag histories agree with references (Figs. 13–17) |
| [Hedayat et al. (2022)](/sources/hedayat-2022.md) | rotationally oscillating cylinder ($Re=300$); in-line oscillating cylinder ($Re=100$, $KC=5$); freely falling cylinders | torque agrees with the single grid; velocity profiles agree with the experiment of Dütsch et al.; fall velocity within 0.2 % of the single grid (§3.2–3.4) |
| [Zhao et al. (2022)](/sources/zhao-2022.md) | transversely oscillating cylinder at $Re=40$ with an immersed boundary on a translating overset grid | smooth forces with single-donor linear reconstruction, noisy forces with inverse distance (§III A) |

## Qualifications

- Chesshire & Henshaw (1990, Table V) print the finest background grid as
  $139\times199$, while the stated spacing ratio and the coarser entries
  ($70\times50$, $99\times71$) give about $139\times99$ *(compiler check,
  not in the sources)*.
- Their Test 2 text compares contours "at times $t=1$ and $t=3$", while the
  Fig. 19 caption labels panels $t=2$ and $t=3$; and Table VIII prints an
  $\ell_2$ ratio of 3.6 for $T$ at $t=1$ where its own entries give
  $0.035/0.012\approx2.9$ *(compiler check, not in the sources)*.
- Henshaw (2006, Table 1) prints the $E_x$ rate as 4.40; a least-squares
  fit of the printed errors over the three grids gives
  $\tfrac12\log_2(9.1\times10^{-5}/2.2\times10^{-7})=4.35$, and 4.33–4.37
  over the rounding of the printed two-digit errors, while the other three
  rates of the table reproduce within 0.06 *(compiler check, not in the
  sources)*.
- Henshaw (1994) prints the Wannier parameters with lowercase $s$ in two
  definitions and uses $D$ both for the wall distance and for the constant
  $-U$.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 376, Figs. 8–10 (Euler cylinder, $M_\infty=0.25$ and $0.5$).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §6.4 Tests 1–2, Figs. 18–21, Tables V–VIII.
- [Henshaw (1994)](/sources/henshaw-1994.md) — §5.1.1 Table IV, Fig. 2 (Wannier); §5.1.2 Figs. 3–5, Table V ($Re=100$).
- [Wang (1995)](/sources/wang-1995.md) — §5.4, Figs. 18–20 (shock diffraction).
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §5.3, Figs. 19–22 ($Re_D=100$ single cylinder, interpolation order; two side-by-side cylinders, $S_F\approx0.09$).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §6.3.1, Figs. 14–15, Table 4 (smoothly accelerating cylinder, slip-wall conditions).
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §10.1, Table 1 (Maxwell manufactured solution on the cylinder-in-channel grid); §10.3 (dielectric cylinder).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §4.3.3, Figs. 26–31 (stationary cylinder, $Re=200$, single system versus Schwarz coupling); §4.3.4, Figs. 32–34 (rotating cylinder, rotation rate 3).
- [Picard et al. (2021)](/sources/picard-2021.md) — §4.3 (Mach 3 cylinder, cross-reference).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §4.2.2 (sphere used instead of a cylinder).
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §5.3, Table 3, Figs. 13–17.
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §3.2–3.4.
- [Zhao et al. (2022)](/sources/zhao-2022.md) — §III A.
