---
type: Method
title: "Divergence-free reconstruction"
description: "Reconstructs point values of the magnetic field from face data so that the interpolated field itself satisfies the divergence constraint to high order."
status: established
tags: [high-order, reconstruction, divergence-constraint, constrained-transport]
timestamp: 2026-10-08T00:00:00Z
---

# Divergence-free reconstruction

The reconstruction step that lets a
[constrained-transport](/methods/constrained-transport.md)-type scheme keep
its divergence guarantee **above second order**. Introduced by
[Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md) from the
observation that the staggered cell-averaged constraint
$D_h^{\mathrm{f}} B_h = 0$ ([notation](/notation.md)) is an exact statement
about *cell averages*: at second order, averages and point values coincide
to $O(h^2)$ and the constraint is inherited pointwise, but for higher-order
schemes the two separate — and reconstructing each field component by
independent one-dimensional interpolations produces "a numerical
$\nabla\cdot\mathbf{B}$ of any size."

**Requirement**: the multidimensional interpolant of the field must be
built so that, for reconstruction accuracy of order $r$, the divergence of
the interpolated field vanishes to order $r{+}1$, with each normal
component continuous along its own longitudinal coordinate (discontinuities
admitted only transversally, where the characteristic modes live). The
reconstruction is therefore a *constrained, genuinely multidimensional*
interpolation of face data — the high-order generalization of the
prolongation problem: any operator producing point/fine values from face
averages must commute with the divergence to the scheme's order, or the
built-in invariant is silently destroyed at the reconstruction stage.

**What does not need reconstructing**
([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md) §2.2).
* A face component is continuous across a discontinuity along its own
  coordinate. Its two face values already give the cell value and the
  parallel derivative to second order, so it is reconstructed only
  transversally.
* The parallel derivative may still jump. By the divergence relation and
  the commutativity of two-point differences, its jump equals transverse
  differences of the other components.
* Above second order, they reconstruct the vector potential as a scalar and
  take the face fields as its *fixed-stencil* two-point curl. Reconstructing
  $A$ alone is not enough; the fixed stencil is what preserves the
  divergence.

## The Balsara TVD construction

[Balsara (2001)](/sources/balsara-2001.md) §III gives a concrete
second-order realization: minmod-limited linear profiles for each face
field, completed by zone-interior quadratic vector polynomials
($a_{yy} = b_{xx} = 0$; coefficients bound by the continuous divergence-free
constraint) — the reconstructed field is divergence-free **at every point
of the zone**, reduces exactly to standard TVD reconstruction under 1D
variation, and supplies left/right Riemann states on faces. Its
area-weighted integration over fine faces is precisely the
[$P_D$ prolongation](/operators/divergence-free-prolongation.md), which is
why reconstruction quality governs AMR transfer quality.

## Continuous interpolation and its limit

[Tóth & Roe (2002)](/sources/toth-roe-2002.md) §3.3 give continuous
interpolating polynomials matching their discrete transfer formulas
(useful for field-line/streamline tracing) — continuous in the normal
component but with an **unavoidable transverse discontinuity** at cell
boundaries at this polynomial order: flux conservation forbids matching the
transverse gradients from both sides. The discontinuity decays at second
order. A structural caution for any claim of globally smooth
divergence-free reconstruction at low order.

## Consolidation (Balsara 2004)

[Balsara (2004)](/sources/balsara-2004.md) turns the reconstruction into
the scheme-design workhorse: limiting is applied to the **face-centered
fundamental variables** (TVD, characteristic, and WENO $r = 2, 3$
variants), the zone-centered field is defined as the *volume average of
the reconstruction polynomial* rather than an ad hoc arithmetic mean, the
normal component stays $C^0$-continuous at faces (eliminating the jump
that troubled seven-wave Riemann solvers), and the construction extends to
cylindrical, spherical, and tetrahedral meshes — carrying divergence-free
AMR to those geometries in the same stroke.

## Beyond second order (Balsara 2009)

[Balsara (2009)](/sources/balsara-2009.md) carries the
construction to third and fourth order in a Legendre-moment basis.
* Face components are expanded in face moments: 3, 6 and 10 per face at
  orders 2, 3 and 4.
* Interior components are complete expansions one order higher in their
  own direction.
* Two structural facts:
  1. The face moments to order $r$ fix every interior coefficient needed
     at order $r$, so the faces carry all the information.
  2. The coefficients the constraint leaves free are set by **minimizing
     the integrated magnetic energy** in the zone, which the author links
     to pressure positivity.
* The constant-term relation is the integral form of
  $D_h^{\mathrm{f}} B_h = 0$, so the high-order reconstruction stays
  consistent with the exactly held staggered invariant.
* Coupled to WENO face reconstruction and SSP-RK, the finite-volume scheme
  meets its design order (2.0, 3.0, 4.4–4.5 on smooth 2D and 3D problems).
* This is the finite-volume counterpart of the point-value high-order CT of
  [UCT](/methods/upwind-constrained-transport.md). There the invariant
  lives on deconvolved variables; here it lives on face moments.

## Projecting point values instead of building polynomials

[Ding & Wu (2024)](/sources/ding-2024.md) enforce a discrete divergence condition on the
*output* of an ordinary WENO reconstruction. No divergence-free polynomial
is built.
* The normal-field traces on a cell's faces are corrected by the
  minimal-norm shift that makes their face-quadrature
  ($D_h^{\mathrm{f}}$-type) divergence $\delta$ vanish
  ([notation](/notation.md)). In 2D the shifts are
  $\Delta x\,\delta/(2(1+(\Delta x/\Delta y)^2))$ on the $x$-faces and
  $\Delta y\,\delta/(2(1+(\Delta y/\Delta x)^2))$ on the $y$-faces, with
  opposite signs on opposite faces.
* At second order this is exactly a slope correction of the linear
  reconstruction. At higher order it keeps the reconstruction's accuracy.
* The construction is cell-local. Unlike the
  Balsara construction above, it does not make
  the normal field continuous across faces; the face jumps are left to a
  source term
  ([positivity–divergence coupling](/results/positivity-divergence-coupling.md)).
* Without the projection, fifth-order FV-WENO on Orszag–Tang, the rotor
  and the blast shows growing divergence error, oscillations and
  nonphysical structure.

## One degree down: curl-constrained reconstruction

[Balsara, Käppeli, Boscheri & Dumbser (2023)](/sources/balsara-2023.md) carry the construction one level down the complex, to vector fields
whose curl is constrained. Such fields arise in first-order hyperbolic
models of heat conduction, hyperelasticity, multiphase flow, first-order
reductions of the Einstein equations and the Schrödinger equation.
* **Collocation.** The vector is an edge quantity in $V_h^1$, and the
  potential that drives it sits at vertices, in $V_h^0$. If every edge
  sharing a vertex uses the same, multidimensionally upwinded, vertex
  potential, the update is a discrete gradient and the circulation over
  every face is held: $C_h G_h = 0$ ([notation](/notation.md)) plays the
  role $D_h C_h = 0$ plays for CT.
* **Reconstruction.** One-dimensional WENO along the edges supplies the
  edge moments. Correction terms that vanish on the edges then make the
  interior polynomial exactly curl-free, or give it a prescribed curl. In
  3D the prescribed curl is itself a divergence-free face field,
  reconstructed with the divergence-free construction above. Each 3D zone
  carries six circulation conditions, of which five are independent,
  against one divergence condition.
* **The same structure as the divergence-free case.** At fourth order the
  edge moments no longer fix every mode. Zone-centred modes are needed,
  and five free parameters remain in 2D. They are fixed by least squares
  against an ordinary finite-volume WENO reconstruction, which keeps the
  constraint exact. This parallels the face/volume split and the
  energy-minimizing choice of Balsara (2009).
* **A multidimensional Riemann solver is required** at the vertices. At
  first order the scheme reduces to properly upwinded advection with
  multidimensional dissipation. Von Neumann analysis gives maximum CFL
  numbers of 1.15 at third order and 1.30 at fourth order.
* **Measured.** The curl stays at machine precision with design order 2 to
  4. Fourth order preserves the quadratic energy best over long runs. A
  zone-centred Godunov scheme shows curl errors 2–4 orders of magnitude
  larger, and it builds up circulation unregulated by the physical source
  term.

## The controlled-class alternative

[Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md)
skip this construction at third and fifth order. They keep $B$ as a
collocated point value, reconstruct along 1D stencils, and control the
divergence with [GLM](/methods/glm-divergence-cleaning.md). The authors
count the absence of genuinely multidimensional interpolation as a
benefit. The trade is the constraint class: no discrete divergence is held.

# Citations

1. [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md), §3–4.
2. [Balsara (2001)](/sources/balsara-2001.md), §III.
3. [Tóth & Roe (2002)](/sources/toth-roe-2002.md), §3.3.
4. [Balsara (2004)](/sources/balsara-2004.md), §§3–4.
5. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§2.2–2.2.2.
6. [Balsara (2009)](/sources/balsara-2009.md), §§2–4.
7. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md), §§1, 5.
8. [Ding & Wu (2024)](/sources/ding-2024.md), §2.3, Examples 4.2–4.4.
9. [Balsara, Käppeli, Boscheri & Dumbser (2023)](/sources/balsara-2023.md), §§2–5.
