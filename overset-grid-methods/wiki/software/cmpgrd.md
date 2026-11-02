---
type: Software
title: "CMPGRD and its solver suite (CGINS, CGNVT, CGES, CGMG, DSK)"
description: "Chesshire and Henshaw's Fortran composite overlapping grid generator: component-grid mappings and stretching, the ordering-based six-step classification that builds the composite grid with given interpolation and discretization widths, donor search by Newton inversion of the mapping, the DSK data structure, and the solvers built on it, with grid-construction and per-step timings."
status: established
aliases: [CMPGRD]
tags: [software, composite-grid, domain-connectivity, interpolation, high-order]
timestamp: 2026-11-02T11:41:00Z
---

# CMPGRD and its solver suite

CMPGRD is the composite overlapping grid generator of
[Chesshire & Henshaw (1990)](/sources/chesshire-1990.md): given component
grids $G_k$, $k=1,\dots,n_g$, each defined by a mapping
$\mathbf x=\mathbf d_k(\mathbf r)$ of the unit square (later the unit cube),
it determines which points are discretization points $\mathcal D_k$,
receptors $\mathcal R_k$ and unused points $\mathcal H_k$, and supplies the
interpolation data, producing a
[composite overlapping grid](/definitions/composite-overlapping-grid.md). It
is written in standard Fortran, about $10^4$ lines without the graphics
interface, and had "recently been extended" to three dimensions (§1;
p. 9). The idea came from the composite-mesh program of B. Kreiss,
but the 1990 version, "with its general algorithm for determining the
overlapping regions, its interpolation procedures, data structures, and
interactive graphics", is "radically different" from it; Pärt adapted an
early version for finite volumes, and CMPGRD also generates cell-centred
grids (p. 9). [Henshaw (1994)](/sources/henshaw-1994.md) builds the
fourth-order incompressible solver CGINS on CMPGRD grids (§5).

## Component grids (§3.1)

A component grid is given either by a user subroutine returning
$\mathbf d_k$ and its first derivatives, or interactively with CMPGRD's
graphical tools (run on IBM VM/CMS, CRAY CTSS, DEC VMS and UNIX systems,
p. 12). Built-in tools include Coons-patch (transfinite) mappings and
stretching functions composed from tanh line-clustering terms and log-cosh
spacing-transition ramps, normalized so that $r\in[0,1]$ maps onto
$[0,1]$ (p. 13, Figs. 6–8); the same ramps build boundary curves with
smoothed corners, from which thin boundary-fitted grids are extruded along
normals (§5.4, Figs. 15, 26). Each component grid can be generated almost
independently; "it is wise" to have about equal spacings where grids overlap
(p. 11).

## Composite grid algorithm (§3.2)

The parameters are the interpolation width $q$ (`iw(m,k1,k2)`, per direction
$m$ and per receptor/donor grid pair), the discretization width $q_{\mathrm d}$,
the minimum allowable overlap, and the ordering of the grids: a higher $k$
has higher priority, so the result changes with the order (Fig. 9). A
centred three-point formula needs one line of receptors, a five-point one
two (p. 14). The flag array `kr` is the registry's mask $\iota_k$ with one
difference: `kr` stores $k$ itself on $\mathcal D_k$ where $\iota_k=1$; it
stores $-k'$ on a receptor whose donor grid is $k'$ and $0$ on unused
points (pp. 18, 21). The six steps, in the registry's notation:

1. set every point's flag to $n_g$;
2. for each physical-boundary point of each grid, mark the closest point of
   every other grid that contains it as unused (this seeds the exterior
   region, which grows in step 3);
3. repeat until no change: each point tries, from the highest grid down, to
   be interpolated from a grid $k'>k$, else to be a valid discretization
   point, else interpolated from the highest $k'<k$, else unused (validity
   depends on the neighbours' status, hence the fixed-point iteration);
4. mark donor-stencil points needed by receptors that interpolate from lower
   grids;
5. from the lowest grid up, delete receptors needed by no discretization
   point and no other grid, turn receptors that can be discretization points
   into discretization points, and mark points of higher grids needed as
   donors;
6. restore the sign convention.

Fig. 11 prints the flag arrays of a square-plus-annulus example after each
step. The cost is estimated at $O(n_g^2N_{\mathrm{pts}})$ operations
(p. 21). Chesshire & Henshaw call the algorithm "fundamentally different"
from those of B. Kreiss and of Benek et al. and "by far, the most important
and most difficult result of this paper" (p. 14). They conjecture without
proof that if a valid composite grid exists for one ordering it exists for
all (p. 16). The classification is defined on
[point classification](/definitions/point-classification.md); the algorithm
as a hole-cutting and overlap-minimizing procedure is discussed on
[hole cutting](/methods/hole-cutting.md),
[implicit hole cutting](/methods/implicit-hole-cutting.md) and
[overlap optimization](/methods/overlap-optimization.md).

**Donor search (p. 21).** To decide whether $\mathbf x$ can be interpolated
from $G_{k'}$: a bounding-rectangle test; a walk from an initial guess to
the nearest grid point (with a global search over boundary points if the
walk stops on the boundary); Newton iteration for
$\mathbf r'=\mathbf d_{k'}^{-1}(\mathbf x)$ from that point. See
[donor search](/methods/donor-search.md).

## Output and data structure (§4)

CMPGRD writes grid point locations, mapping derivatives (`rsxy`), the list
of receptors with donor grid $k'$, donor coordinates $\mathbf r'$, the
lower-left stencil corner and the interpolation and discretization widths
(pp. 26, 28). The data live in the DSK package: a directory–file structure
inside one large Fortran array, where `dskloc` returns a pointer and the
array is then passed to subroutines as an ordinary Fortran array (p. 25).
Henshaw (1994) supplies $\mathbf r'$ and the metrics $\partial r_m/\partial
x_n$ at vertices from CMPGRD for the fourth-order solver (§2, §4.1).

## Solvers and utilities built on it

| Name | Role | Source |
|---|---|---|
| CGINT, CGINTE | implicit and explicit interpolation (stencils may or may not contain receptors) | Chesshire & Henshaw (1990), §5.2 |
| CGEL | sparse direct (Yale) solver for linear elliptic systems on composite grids, second or fourth order | Chesshire & Henshaw (1990), §5.5 |
| CGMG | composite-grid multigrid; CMPGRD generates the coarse composite levels | Chesshire & Henshaw (1990), §5.5; Henshaw (1994), §5 |
| CGNVT | second-order, non-conservative compressible Navier–Stokes solver with per-grid implicit–explicit time stepping | Chesshire & Henshaw (1990), §6 |
| CGES | composite grid equation solver | Henshaw (1994), §5 |
| CGINS | fourth-order incompressible Navier–Stokes solver, 2-D and 3-D in one Fortran program | Henshaw (1994), §5 |

Interpolation in all of them is tensor-product Lagrange interpolation in the
donor's parameter coordinates, which "makes arbitrary-order interpolation
easy and less error-prone" (Chesshire & Henshaw 1990, p. 28); Henshaw (1994,
§4.1) uses width $q=5$ (triquartic, $5\times5\times5$ stencil) with two
lines of receptors. The widths CMPGRD must be given follow the
[interpolation-order requirement](/results/interpolation-order-requirement.md);
see also [explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md),
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
and [twilight-zone flow](/methods/twilight-zone-flow.md).

## Timings

| Case | Quantity | Value | Hardware |
|---|---|---|---|
| cylinder in a channel, grids $G_1$, $G_2$, $G_3$ of increasing resolution | grid construction | 1.6 s, 3.1 s, 7.2 s | IBM 3090VF |
| airfoil with two flaps, 8101 points | grid construction | 9.3 s | IBM 3090VF |
| CGNVT on the coarsest cylinder grid, explicit | per step | 0.11 s, $31\times10^{-6}$ s per point | IBM 3090VF |
| same, cylinder grid implicit | per step | 0.21 s, $59\times10^{-6}$ s per point; twice the time step, slightly cheaper overall | IBM 3090VF |
| CGNVT, airfoil with two flaps | per step | 0.725 s, $89\times10^{-6}$ s per point | IBM 3090VF |
| CGINS, cylinder at $Re=100$, 14,581 points, fourth order | per step | 1.5 s: pressure solve 27%, explicit interpolation 2%, time stepping 43%, boundary conditions 7% | IBM RS/6000-530 |
| CGINS, sphere in a channel, three grids | per step | 45.0 s: GMRES pressure solve 42%, implicit interpolation 17%, time stepping 28%, boundary conditions 9% | IBM RS/6000-530 |

(Chesshire & Henshaw 1990, §6.4 p. 55, §6.5 p. 60, Tables X–XI; Henshaw
1994, Tables V, VIII.) For CGNVT on the coarsest grid the sparse solver
takes 2,673,907 of 2,802,678 storage words (Table IX); for explicit stepping
the overhead of composite grids over a single-grid code is essentially the
flag array plus interpolation arrays (p. 55). Henshaw attributes the
sphere's 17% interpolation share to its 10,728 receptors, a high fraction of
all points (§5.2).

## Lineage and successor

[Henshaw & Schwendeman (2006, §1)](/sources/henshaw-2006.md) place CMPGRD in
the composite-grid line: the approach "was described by Volkov", developed
further by Starius and by Kreiss, "which led to the CMPGRD tools of
Chesshire and Henshaw", while "Steger and associates at NASA independently
conceived of the approach which they called Chimera grids". The 2006
papers no longer run CMPGRD: their composite grids come from Ogen, the
overlapping grid generator of the C++ framework
[Overture](/software/overture.md) (Henshaw & Schwendeman 2006, §3.1;
[Henshaw 2006](/sources/henshaw-2006-b.md), §9.4, uses Overture for the
Maxwell code mx). The CMPGRD concepts carry over unchanged: component grids
as mappings of the unit square or cube, the three point classes
(discretization, interpolation, unused), tensor-product Lagrange
interpolation in the donor's parameter space, and interpolation widths set
by the [interpolation-order requirement](/results/interpolation-order-requirement.md).
Henshaw (2006, §4) states that rule for the second-order wave equation as
$q=p+1$ for a $p$th-order scheme, "following" Chesshire & Henshaw (1990);
for the fourth-order Maxwell scheme this is $q=5$, the width CGINS uses
(Henshaw 1994). What Ogen adds, a per-step incremental update for moving
grids, is on the Overture page.

## Qualifications

- Step 5 and step 6 of the printed pseudo-code (Chesshire & Henshaw 1990,
  p. 20) carry slips: step 5's last assignment prints "kr(i′,j′,k′) −
  |kr(i′,j′,k′)|" without the assignment arrow, and step 6 prints
  "|kr(i′,j′,k′)|" with primed indices, while its test and its other
  branch use the unprimed point $kr(i,j,k)$; step 4 prints the full
  assignment "kr(i′,j′,k′) ← −|kr(i′,j′,k′)|".
- Table IX's sparse-solver subtotal prints 2,673,907, while its parts
  (72,241 and 2,601,766) sum to 2,674,007; the grand total 2,802,678 equals
  128,771 plus the printed subtotal *(compiler check, not in the sources)*.
- Henshaw (1994) gives the sphere case as "47,550 active grid points" in the
  text (§5.2) and "17,550" in Table VIII.
- Neither paper shows the grid generator's behaviour in 3-D.

# Citations

- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §1 and p. 9 (CMPGRD origin, features, size); §3.1 pp. 11–13 (component grids, stretching, platforms); §3.2 pp. 14–21, Figs. 9–11 (parameters, flag array, six steps, donor search, cost); §4 p. 25 (DSK); §5.2 p. 28 (interpolation data, CGINT/CGINTE); §5.4 (smoothed corners); §5.5 (CGEL, CGMG); §6 (CGNVT), Tables IX–XI; p. 55, p. 60 (timings).
- [Henshaw (1994)](/sources/henshaw-1994.md) — §2 and §4.1 (CMPGRD-supplied coordinates, metrics, triquartic interpolation); §5 (CGINS, CGES, CGMG, DSK); Tables V, VIII (timings).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §1 (Volkov–Starius–Kreiss lineage leading to CMPGRD; Chimera conceived independently); §3.1 (Ogen as the grid generator used).
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §4 (point classes, tensor-product Lagrange interpolation, width $q=p+1$ after Chesshire & Henshaw); §9.4 (mx built on Overture).
