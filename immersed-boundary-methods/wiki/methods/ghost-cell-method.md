---
type: Method
title: "Ghost-cell immersed boundary method"
description: "Sharp-interface discrete-forcing method that assigns values to ghost points inside the body so that the boundary condition holds at the boundary point on the normal through each ghost point, usually by interpolating at an image point in the fluid and extrapolating along the normal; its stencils, conditioning fixes, Neumann and Robin conditions, compressible and high-order versions."
status: established
aliases: [GCIBM, ghost-cell IBM, ghost-point method, image-point method, hybrid Cartesian immersed boundary, HCIB]
tags: [ghost-cell, sharp-interface, discrete-forcing, reconstruction, compressible, incompressible]
timestamp: 2026-11-08T18:32:00Z
---

# Ghost-cell immersed boundary method

A **ghost cell** (ghost point, ghost node) is a grid point inside the body
$\Omega_s$ that belongs to the stencil of at least one fluid point. A
ghost-cell method computes a value $w^G$ at each ghost point such that the
boundary condition is satisfied at a nearby point of $\Gamma$; the interior
scheme is then applied unchanged at every fluid point
([Tseng & Ferziger 2003](/sources/tseng-2003.md), §2.2;
[Mittal & Iaccarino 2005](/sources/mittal-2005.md), discrete-forcing section). No equation is
solved in the body beyond the ghost layer, and no force term enters the fluid
equations, so the boundary is sharp
([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md)).
In the [classification](/definitions/immersed-boundary-method.md) it is a
discrete-forcing method that imposes the boundary condition directly; Tseng
and Ferziger note that it can be read as [direct forcing](/methods/direct-forcing.md)
with the force active only at ghost cells. The device descends from the
[ghost fluid method](/methods/ghost-fluid-method.md) for material interfaces
(Tseng & Ferziger 2003, §1).

## Construction

1. **Classify** grid points as fluid or solid from the surface description
   (line segments in 2-D, a triangulated surface in 3-D,
   [Mittal et al. 2008](/sources/mittal-2008.md), §2.2); ghost points are
   solid points with a fluid neighbour — one layer for second-order stencils,
   two for a fifth-order WENO stencil
   ([Chaudhuri et al. 2011](/sources/chaudhuri-2011.md), §2.2).
2. **Boundary point.** From each ghost point drop the normal to $\Gamma$; its
   foot $\mathbf x_{BI}$ (boundary intercept) is where the condition is
   imposed. Mittal et al. (2008) search the nearest surface vertex and
   elements, take the shortest normal intercept when several exist, and fall
   back to the closest surface point when none does.
3. **Image point.** Extend the normal into the fluid to the image point
   $\mathbf x_{IP}$, with $\mathbf x_{BI}$ midway between ghost and image point.
   Interpolate $w_{IP}$ from the fluid nodes around it — bilinear or trilinear
   ([Ghias et al. 2007](/sources/ghias-2007.md); Mittal et al. 2008), or
   inverse-distance weighting (Chaudhuri et al. 2011).
4. **Extrapolate** along the normal with the boundary condition:

$$w^G=2\,w_{BI}-w_{IP}\ \ \text{(Dirichlet)},\qquad w^G=w_{IP}-\Delta l\,\frac{\partial w}{\partial n}\Big|_{BI}\ \ \text{(Neumann)},$$

   with $\Delta l$ the ghost-to-image distance. A Robin condition combines the
   Dirichlet and Neumann systems (Tseng & Ferziger 2003, §2.5).

Tseng and Ferziger (2003, §2.3) also extrapolate directly from a polynomial
fitted through the boundary point and the nearest fluid nodes — linear
($3\times3$ Vandermonde system in 2-D, $4\times4$ in 3-D) or quadratic ($6\times6$,
$10\times10$) — and find both keep overall second order.

## Conditioning

Direct extrapolation produces large negative weights when $\Gamma$ passes
close to a fluid node used in the fit, so $|w^G|$ can exceed its neighbours
and the iteration diverge. The remedies are the image point, which keeps the
weights positive (Majumdar et al., used by Tseng & Ferziger 2003), and moving
the boundary point onto a fluid node closer than $0.1\,\Delta x$ (after Gibou et
al.). When an image-point cell contains the ghost node itself (or another
solid node), Ghias et al. (2007, §2.4) and Mittal et al. (2008, §2.2)
replace that node's row in the Vandermonde system by the boundary condition
at $\mathbf x_{BI}$; the interpolation stays well posed for all positions, and
no lower-order fix is needed, unlike the Cartesian-direction extrapolation of
Gibou et al.'s ghost-fluid Poisson solver, which falls back to first order for
small distances. Ghost values that appear in each other's stencils are
coupled and are solved iteratively; the system is diagonally dominant
(Mittal et al. 2008).

## Variants in the sources

| source | flow | grid and scheme | interpolation |
|---|---|---|---|
| [Tseng & Ferziger (2003)](/sources/tseng-2003.md) | incompressible, LES, ocean model | Cartesian, collocated or staggered (separate weights per variable) | linear or quadratic fit, image point, inverse-distance option |
| [Ghias et al. (2007)](/sources/ghias-2007.md) | viscous compressible, subsonic | non-conformal curvilinear, central/QUICK, RK3–CN | bilinear in computational space |
| [Mittal et al. (2008)](/sources/mittal-2008.md) | incompressible, 3-D moving and deforming bodies | non-uniform Cartesian, collocated with face velocities, multigrid | trilinear; [fresh-cell](/definitions/fresh-cell-problem.md) interpolation |
| [Chaudhuri et al. (2011)](/sources/chaudhuri-2011.md) | inviscid compressible with shocks | uniform Cartesian, fifth-order WENO, RK3 | inverse-distance weighting with solid nodes excluded; ghost data per direction at corners |

## Accuracy and conservation

The Dirichlet condition is imposed to second order because $\Delta l=O(h)$;
with a second-order interior scheme the velocity is second order locally and
globally (Mittal et al. 2008, §2.2; Ghias et al. 2007, §3, both by grid
refinement). Tseng and Ferziger (2003, §3) measure overall second order with
linear and quadratic reconstruction alike. Chaudhuri et al. (2011, §3) find
second order at the boundary with a fifth-order interior scheme around a
shocked cylinder, and show that dropping the interpolation (imposing only zero
normal velocity) turns a $34.5^\circ$ oblique shock into $31.9^\circ$ with spurious
oscillations. Ghost-cell methods are not discretely conservative; Ghias et
al. (2007, §2.5) state the trade-off: such methods choose local second-order
accuracy over strict conservation, while only cut cells deliver both
([discrete conservation](/properties/discrete-conservation.md)).

## Moving bodies

A ghost-cell method needs a value for points that leave the body during a
step ([fresh-cell problem](/definitions/fresh-cell-problem.md)). Mittal et
al. (2008) handle 3-D moving and deforming bodies, infinitely thin plates and
membranes (ghost cells on both sides), and a video-reconstructed fish fin.

## Later variants

- **Directional ghost values.** [Ou et al. (2022)](/sources/ou-2022.md), §2,
  give each ghost point one value per coordinate direction, each reconstructed
  in 1-D along that grid line with the boundary condition imposed at the line's
  intersection with $\Gamma$, as at a real domain boundary; no normals or image
  points are needed, Dirichlet, Neumann and Robin conditions (including
  surface-reaction coefficients) enter a Taylor-series extrapolation, and a
  first-order fallback handles fluid points too close to the intersection. With
  a sixth-order interior scheme reduced to fourth and fifth order next to the
  boundary, the local error converges at nearly second order for all three
  condition types.
- **Ghost states for moving boundary faces.** [Natarajan et al. (2022)](/sources/natarajan-2022.md)
  compute the flux on a moving embedded-boundary face from a Riemann problem
  with a reflected ghost state whose normal velocity is $2\mathbf u_\Gamma\cdot\mathbf n-u_n$.
- **Boundary cells without normals.** [Ni et al. (2022)](/sources/ni-2022.md)
  treat the cells occupied by material points next to the fluid as ghost cells
  whose velocity is set to the structure's
  ([fluid–structure coupling](/methods/fluid-structure-coupling.md)).
- **Curvilinear background grids.** [Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md),
  §3, review the curvilinear immersed boundary (CURVIB) method, which
  reconstructs velocities at immersed-boundary nodes along the normal on a
  curvilinear background grid, used for heart valves and biological flows.

## GPU and thin, sharp-edged bodies

[Raj et al. (2023)](/sources/raj-2023.md) port a sharp-interface
reconstruction method on a staggered grid to GPUs (OpenACC/CUDA): intercepted
and "thin" cells are identified from a triangulated surface by ray casting,
variables are reconstructed along the nearest surface normal, a
multi-directional forcing handles sharp edges such as airfoil trailing edges,
and field extension to near-boundary solid points reduces
[spurious force oscillations](/definitions/spurious-force-oscillations.md) of
moving bodies. They report more than a 100-fold speed-up on an NVIDIA V100 for
an oscillating sphere, growing with mesh size, and compare AMD and NVIDIA GPUs.
[Ménez et al. (2023)](/sources/menez-2023.md) borrow ghost cells with two image
points to impose adiabatic walls in volume penalization.

## High order

Ghost-cell treatments that keep third or higher order — polynomial
weighted-least-squares ghost values with or without image points, DG
polynomials at image points, hybrid compact–WENO interiors — are compared on
[high-order immersed boundary treatments](/methods/high-order-immersed-boundary.md)
([Turner et al. 2024](/sources/turner-2024.md); [Huang et al. 2024](/sources/huang-2024.md);
[Qi et al. 2024](/sources/qi-2024.md); [Marashi & Hejranfar 2025](/sources/marashi-2025.md)).

# Citations

- [Tseng & Ferziger (2003)](/sources/tseng-2003.md) — §1, §2.2–2.6, §3.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — discrete-forcing section (ghost-cell methods).
- [Ghias et al. (2007)](/sources/ghias-2007.md) — §1, §2.4, §2.5, §3.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §1, §2.2, §3.
- [Chaudhuri et al. (2011)](/sources/chaudhuri-2011.md) — §2.2, §3.
- [Sotiropoulos & Yang (2014)](/sources/sotiropoulos-2014.md) — §3.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md) — §2.
- [Ni et al. (2022)](/sources/ni-2022.md) — §5.
- [Ou et al. (2022)](/sources/ou-2022.md) — §2–§3.
- [Ménez et al. (2023)](/sources/menez-2023.md) — §3.
- [Raj et al. (2023)](/sources/raj-2023.md) — §2–§5.
- [Turner et al. (2024)](/sources/turner-2024.md) — §2.
- [Huang et al. (2024)](/sources/huang-2024.md) — §2.
- [Qi et al. (2024)](/sources/qi-2024.md) — §3.
- [Marashi & Hejranfar (2025)](/sources/marashi-2025.md) — §3.
