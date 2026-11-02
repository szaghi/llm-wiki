---
type: Method
title: "Shock capturing on overlapping grids"
description: "How shocks, detonations and material interfaces are captured on overset grids: what happens when a discontinuity crosses an interpolation boundary, the Godunov-type schemes run on each component grid, Picard et al.'s limited intersection-weighted transfer and corner-radius limiter, the patch-to-substrate cell-size ratio (artifacts above 4), slip-wall conditions, and the measured accuracy for discontinuous flows."
status: established
aliases: [shock capturing on overset grids, shocks crossing overset boundaries, Chimera shock capturing, Godunov methods on overlapping grids, compressible flow on overlapping grids]
tags: [shock-capturing, compressible, finite-volume, overset-grid, multiphase]
timestamp: 2026-11-02T15:27:00Z
---

# Shock capturing on overlapping grids

**Shock capturing on overlapping grids** runs a conservative, upwind,
slope-limited scheme on each component grid $G_k$ and couples the grids
through the receptors. The component-grid schemes are single-grid
shock-capturing schemes; what the overset setting adds is the **crossing of a discontinuity through an interpolation
boundary**, where the receptor values are transferred rather than updated
by fluxes. The sources examine three consequences: loss of global
conservation, new extrema created by the transfer, and resolution jumps
between grids. They answer them in two ways: a conservative interface
([conservative overset interface](/methods/conservative-overset-interface.md)),
or non-conservative transfer with enough resolution, limiting and a bounded
cell-size ratio.

## Shocks crossing interpolation boundaries

The founding sources report the problem on steady and unsteady shocks:

- [Benek et al. (1983)](/sources/benek-1983.md) see mismatch and "hash" where
  the shock of the SKF 1.1 airfoil ($M_\infty=0.76$, $\alpha=2.5^\circ$)
  crosses the overlap boundary and attribute it, provisionally, to the
  non-conservative interpolation (pp. 376–377, Figs. 13–14); with the
  maneuver flap at $M_\infty=0.7$ they again find difficulty with the shock at
  the mesh boundary (p. 377, Figs. 19–20).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) find that the bow
  shock of an impulsively started cylinder at Mach 2, $Re=50$ "has some
  difficulty crossing the interpolation boundary" on the coarsest grid only
  (§6.4, Fig. 19a).
- [Wang (1995)](/sources/wang-1995.md) moves a slow shock through a
  rectangular minor grid: the original Chimera interpolation develops
  instabilities that dissipate the shock until it disappears, while the
  conservative interface passes it through (§5.2).

The later sources compute shocks, detonations and contact discontinuities
crossing interpolation boundaries without a conservative interface:

- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) on moving grids
  with AMR, including detonations;
- [Picard et al. (2021)](/sources/picard-2021.md) on static finite-volume
  patches, with a stationary shock, a bow shock, a shock–bubble interaction
  and the double Mach reflection;
- [Banks et al. (2016)](/sources/banks-2016.md) with a shock hitting a
  deformable solid.

Picard et al. observe "no spurious reflection" when the moving front shock
of their Mach-3 cylinder crosses from the substrate into the patch (§4.3,
Fig. 14). Chan (2009) recalls Meakin's result that tri-linear fringe
interpolation keeps formal accuracy "provided the flow solution is smoothly
resolved by all participant grids in the overlapped zones"
([Chan (2009)](/sources/chan-2009.md), §7); Chan does not discuss
discontinuities crossing the overlap. Sharma et al. (2021) state that the lack of conservation does not
degrade the solution if the overlap is away from shocks and discontinuities
([Sharma et al. (2021)](/sources/sharma-2021.md), §1).

## Schemes on the component grids

**Second-order Godunov on mapped moving grids.** Henshaw & Schwendeman
(2006, §4.2, Eqs. (9)–(13)) solve the reactive Euler equations on each
component grid, moving or not, in the mapped form with grid velocity given
on [moving overset grids](/methods/moving-overset-grid.md):

- cell averages are taken in the parameter space of each grid;
- fluxes come from a second-order slope-limited Godunov method with a Roe
  approximate Riemann solver, with face states from a Taylor expansion about
  the cell centre whose time derivatives are replaced through the
  quasi-linear form, with upwind filtering and minmod limiting of the
  characteristic variables;
- the update divides the flux differences by the cell's area factor and adds
  the dilatation term of the moving grid, a form the authors call
  "semi-conservative";
- the stencil is 5 points wide, so two ghost lines are needed; Cartesian
  grids use metric-free formulas to save CPU time and memory;
- a stiff reactive source is split off by Strang splitting and integrated
  with an adaptive Runge–Kutta (2,3) pair;
- one global time step serves every grid,
  $\Delta t=C_{\mathrm{CFL}}\min_k\Delta t_k$, with the page-local safety
  factor $C_{\mathrm{CFL}}=0.9$ (Eq. (13)).

Banks et al. (2016, §4.2) use this fluid scheme with a Roe-type solver and
centred differences for the dilatation term, adjusted for free-stream
preservation on deforming grids.

**MUSCL–Hancock with HLLC on unstructured cells.** Picard et al. (2021, §2,
§3.1) solve a five-equation two-component Euler model (two partial
densities, momentum, total energy and one volume fraction, with a
non-conservative term for the volume fraction) by a cell-centred finite-volume
scheme on polygonal cells: piecewise-linear reconstruction of primitive
variables with least-squares gradients, the slope limiter they call the
"K-limiter of Dubois", the HLLC approximate Riemann solver and MUSCL–Hancock
time integration, second order in space and time, at CFL 0.4 in the shock
and 2-D tests.

**Roe with MUSCL in primitive variables.** Wang (1995, §4) uses MUSCL with
minmod in primitive variables, Roe flux-difference splitting and implicit
backward Euler, on both sides of his conservative interface.

## Transfer of discontinuous data between grids

**Lagrange interpolation.** Henshaw & Schwendeman interpolate with a
tensor-product Lagrange formula in the donor's parameter space (§3.1) and do
not discuss conservation or limiting at the overlap. The receptors of their
refinement grids are filled the same way
([AMR on overlapping grids](/methods/amr-on-overset-grids.md)).

**Limited, intersection-weighted reconstruction.** Picard et al. fill $n_f=2$
layers of receptor ("ghost") cells on each grid, the number a second-order
flux at the first non-receptor face needs to be independent of the patch
boundary (§3.2.3), with a volume-weighted average of the donor cells' limited
linear reconstructions evaluated at the barycentres of the cell
intersections (§3.2.4, Eq. (15); formula on
[conservative overset interface](/methods/conservative-overset-interface.md)).
They show that the standard limiter is not enough there (§3.2.5,
Eqs. (16)–(19), Figs. 5–6). With $\mathbf q^{\min}_c$, $\mathbf q^{\max}_c$
the extreme values over cell $V_c$ and its neighbours, the limiter is
$$\Phi_c=\min\!\Big(1,\;K_{\mathrm D}\,\frac{\min\big(\mathbf q^{\max}_c-\mathbf q_c,\;\mathbf q_c-\mathbf q^{\min}_c\big)}{\max_{\mathbf y}\nabla\mathbf q_c\cdot(\mathbf y-\mathbf x_c)}\Big),\qquad K_{\mathrm D}=0.75,$$
where in the standard form $\mathbf y$ runs over the face centres of $V_c$,
the same search radius as the Barth–Jespersen limiter ($\Phi_c$, $K_{\mathrm D}$
page-local). The intersection barycentre at which a donor cell's
reconstruction is evaluated can lie farther from its centre than every face
centre, increasingly so as the cell-size ratio grows, so the transfer can
create new local extrema. Picard et al.'s **modified limiter** lets $\mathbf y$
run over the *corners* of $V_c$ instead, which makes it valid "whatever the
location of the ghost cell and the cell ratio". Sharma et al. (2021, §3.1.2)
give the reason monotonicity matters on overset grids in general:
non-monotone interpolation can create or amplify extrema that grow cycle
after cycle and lead to exponential instability in high-Reynolds-number flow
when meshes overlap in chaotic high-gradient regions.

**Conservative interface.** Wang's alternative removes the overlap on the
major grid and exchanges Riemann fluxes across the minor grid's boundary; it
is on [conservative overset interface](/methods/conservative-overset-interface.md).

## Cell-size ratio between patch and substrate

Picard et al. (§3.2.1, Eqs. (10)–(11)) measure the resolution jump at the
overlap by a local ratio for each receptor cell of the patch, the largest
ratio of the size of an overlapping substrate donor cell to its own size, and
a global ratio $\kappa_h$, the maximum over the patch receptors (registry §9;
Picard et al.'s $\chi$, a symbol the registry reserves). $\kappa_h>1$ means the
patch is finer; in all tests the patch spacing is the substrate spacing
divided by $\kappa_h$. Their evidence:

| test | $\kappa_h$ tested | finding |
|---|---|---|
| 1-D sine advection, substrate of 200 cells (§4.1, Table 2) | 1–16 | L1 error falls only from $5.61\times10^{-5}$ to $4.01\times10^{-5}$: the coarse substrate dominates; the transfer does not spoil the solution |
| stationary Mach-1.5 shock on the patch boundary, non-coincident interfaces (§4.2, Table 4) | 2–16 | conservation defect 0.115–0.599 % |
| Mach-3 cylinder, substrate of 100 cells on the perimeter (§4.3, Tables 6–7) | 1, 2, 4 | drag within 1.47 %, 0.27 %, 0.5 % of a uniformly fine grid; bow-shock standoff 0.428, 0.395, 0.372 against the analytical 0.3649 (1.95 % at $\kappa_h=4$) |
| Mach-1.22 shock on a helium bubble, substrate of 50 cells per diameter (§4.4, Fig. 25) | 1–8 | quality improves with $\kappa_h$ "without any discernable numerical damage", limited by the substrate |
| double Mach reflection, substrate of 80 cells per metre (§4.5, Figs. 29–31) | 2, 4, 8 | $\kappa_h=2,4$ agree very well with uniform fine grids; at $\kappa_h=8$ the abrupt spacing change perturbs the slip lines and the jet |

They conclude that artifacts arise when $\kappa_h$ is "at least greater than 4"
and recommend $\kappa_h\le4$ (§4.5, §5). The cost ratios of the uniformly fine
grid to the Chimera grid at equal minimum spacing (no hardware stated) are
0.97, 2.3 and 3.5 in CPU time and 0.97, 2.41 and 3.8 in memory for the
cylinder at $\kappa_h=1,2,4$ (Table 6), and 0.39, 1.14, 2.38, 2.54 (CPU) and
0.43, 1.30, 2.67, 3.62 (memory) for the double Mach reflection at
$\kappa_h=1,2,4,8$ (Table 8).

Picard et al. state their bubble result against Pärt-Enander & Sjögreen
(1994, not ingested here): "Unlike what Pärt-Enander and Sjögreen observed, we
show that refining a patch model in a overlapping grid strategy improves the
quality of the solution without any discernable numerical damage" (§4.4). Their
own double-Mach-reflection result limits this to moderate ratios.

## Slip walls on curved moving bodies

Henshaw & Schwendeman (2006, §5, Eqs. (14)–(20)) derive a numerical slip-wall
condition for body-fitted component grids (their SW-BC). The analytic
condition is $\mathbf n\cdot(\mathbf u-\mathbf u_g)=0$. The ghost temperature
comes from the normal-momentum compatibility condition: the normal pressure
derivative, divided by $\rho$, equals the curvature term (fluid acceleration
along the curved wall) minus the normal wall acceleration. The other ghost
values come from a limited third-order extrapolation that reduces to
first-order extrapolation near discontinuities. A density condition valid
only for isentropic flow is avoided because shocks change the entropy. On a
smoothly accelerating cylinder (§6.3.1, Table 4) the condition gives
self-convergence max-norm rates of 2.03, 1.83, 1.84 ($\rho$, $v$, $T$), while
reflection (symmetry) conditions, "sometimes used" on curved slip walls, give
1.56, 1.04, 1.57 and visibly non-smooth pressure contours at the wall.

## Accuracy for discontinuous flows

- **Rates below two.** Henshaw & Schwendeman's pressure-driven piston, whose
  solution has a jump in the first derivative, converges at 0.71 in the max
  norm and 1.32–1.34 in the 1-norm (§6.2.2, Table 3); the shock-driven
  cylinder (Mach-1.5 shock, uniform grids of $h_j=1/(10j)$, $j=8,16,32$)
  converges at 1.47–1.49 in the 1-norm by self-convergence (§6.3.2, Table 5;
  see [shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md)).
  A smooth supersonic expansion on a single curved grid gives 1.77–1.95 in the
  max norm (§6.1, Table 1).
- **Overlap versus single grid.** Picard et al. find the patch solution with
  $\kappa_h=1$ within about 2 % of the single grid in L1 error for advection
  (§4.1, Table 1), the time-averaged drag of the Mach-3 cylinder within
  0.27–1.7 % of the single grid (§4.3, Table 5), and the double Mach
  reflection's Mach stems, reflected shocks and slip lines coinciding with the
  single mesh, with a few oscillations in the substrate attributed to the
  transfers interfering with acoustic waves (§4.5, Fig. 28).
- **Detonations.** In Henshaw & Schwendeman's detonation initiated by an
  impulsively moved cylinder, the shock position converges with resolution,
  but the von Neumann pressure peak is not fully converged on the finest grid
  (§7.1, Fig. 21).

## Multiphase and solid impacts

Picard et al. carry a gas–gas material interface across the patch boundary:
a Mach-1.22 shock in air hits a helium bubble placed only in a patch rotated
by $30^\circ$; with $\kappa_h=1$ the Chimera result agrees with the single grid,
with a slight loss of symmetry at the finest resolution attributed to the
rotated patch (§4.4, Figs. 23–24). Banks et al. compute a Mach-1.3 shock
hitting a light elastic ellipse on deforming grids (§6); see
[fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md).

## Discontinuous Galerkin coupling as a limiter, and coincident points

[Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) rebuild the higher modes of DG artificial-boundary cells by WENO reconstruction, which also limits the solution when a shock crosses the overset boundary; Sod and Lax shock tubes and three 2-D Riemann problems pass without oscillation ([discontinuous Galerkin methods on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md), §4.3–4.4). [Teschner & Mundt (2022)](/sources/teschner-2022.md) avoid interpolation near the axis of a blunt body by coincident points and compute a supersonic hemisphere cylinder with AUSM-type fluxes ([interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md)). [Delcour et al. (2022)](/sources/delcour-2022.md) report local supersonic pockets terminated by shocks across a deforming Chimera mesh (§4.2).

## Shock-aligned overset grids

[Kochi & Ramakrishna (2023)](/sources/kochi-2023.md) confine shock capturing to an overset grid: troubled-cell data of a coarse DG solution locate the shock, a refined structured overset grid aligned with it is built (partly by hand), and the solver is rerun with the high-resolution flux and limiter only on that grid. The shock then lies on a grid line with very small thickness, decreasing with the order; a refined but unaligned overset grid does better than the coarse grid and worse than the aligned one. Tests: ramp, shock reflection, a cylinder bow shock (stand-off checked against an analytical method) and a Mach reflection (Abstract, Conclusions).

## Qualifications

- Picard et al. state that the K-Dubois limiter "acts on the primitive
  variables" (§3.2.5) but apply it in the transfer to gradients of the
  conservative variables (Eq. (15)), calling it "the limiter also used for the
  gradient reconstruction" of Eq. (9); which variables the transfer limiter
  bounds is ambiguous. Whether the corner-radius limiter replaces the standard
  one in every cell or only in donor cells is not stated.
- Picard et al. attribute the limiter to Dubois while their reference for it
  is printed under the names Solyga & Galon (unpublished, 2015).
- Picard et al.'s conclusion puts the conservation impact at "an order of
  magnitude of 0.1 % of the initial state", while their Tables 3–4 give
  0.115–0.635 % for non-coincident interfaces.
- Printed slips in Picard et al. (2021), version read (HAL author manuscript):
  - Table 1 prints the single-grid order at 100 cells as 1.595, while
    $\log_2(1.609\times10^{-4}/5.499\times10^{-5})=1.549$; the other nine
    printed orders agree with the printed errors *(compiler check, not in the
    sources)*;
  - Table 5 prints the drag difference at 400 cells as 0.47 %, while the
    printed forces give $\lvert202164-203000\rvert/203000=0.41$ % *(compiler
    check, not in the sources)*;
  - in §4.4 the printed $x$ and $y$ intervals of the domain are swapped
    relative to the bubble position and Fig. 20, the patch is printed as a
    $6\times10^{-3}$ m square although it must contain a bubble of diameter
    $50\times10^{-3}$ m, and Eq. (26) assigns the post-shock state to the side
    of the shock that holds the bubble;
  - in §4.3 the cylinder size $D=1$ m is called a radius while the standoff is
    normalized by $D$ and the initial shock is placed "8 cylinder diameters"
    upstream, and the front shock is given a Mach number of 1.
- Henshaw & Schwendeman's Fig. 20 caption prints $t=0.035$ for the right
  column, which the text and panels give as $t=0.35$.
- Cost ratios in Picard et al. come without hardware, parallel setup or
  absolute timings.
- None of the sources measures how the conservation defect of a
  non-conservative transfer moves a shock: Wang's concern about wrong jump
  conditions or locations (§5) is neither confirmed nor refuted by the later
  tests, which compare with single-grid solutions and analytical standoff
  distances.

# Citations

- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §3.1; §4.2 (Eqs. (9)–(13)); §5 (Eqs. (14)–(20)); §6.1–6.3 (Tables 1, 3–5); §7.1 (Figs. 20–21).
- [Picard et al. (2021)](/sources/picard-2021.md) — §2; §3.1; §3.2.1 (Eqs. (10)–(11)); §3.2.3; §3.2.4 (Eq. (15)); §3.2.5 (Eqs. (16)–(19), Figs. 5–6); §4.1–4.5 (Tables 1–8, Figs. 11, 14, 20–31); §5.
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.2, §6.
- [Wang (1995)](/sources/wang-1995.md) — §4, §5, §5.2.
- [Benek et al. (1983)](/sources/benek-1983.md) — pp. 376–377 (Figs. 13–14, 19–20).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §6.4, Fig. 19a.
- [Chan (2009)](/sources/chan-2009.md) — §7 (Meakin's result as recalled).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1, §3.1.2.
- [Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) — §4.3–4.4.
- [Teschner & Mundt (2022)](/sources/teschner-2022.md) — §3–§4.
- [Delcour et al. (2022)](/sources/delcour-2022.md) — §4.2.
- [Kochi & Ramakrishna (2023)](/sources/kochi-2023.md) — Abstract, Conclusions.
