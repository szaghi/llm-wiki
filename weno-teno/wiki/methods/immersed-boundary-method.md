---
type: Method
title: "Immersed-boundary and cut-cell methods"
description: "Treatments of walls and material interfaces that do not follow the mesh on Cartesian grids: sharp-interface ghost-cell immersed boundaries that fill solid cells from mirror or image points, the bilinearly complete hybrid reconstruction of Wang et al., and cut-cell methods with their small-cell problem, cell merging and real–ghost mixing."
status: established
aliases: [immersed boundary method, IBM, ghost-cell method, GCM, ghost-cell immersed boundary, cut-cell method, CCM, embedded boundary, HBCGCM, BCGCM]
tags: [immersed-boundary, finite-volume, interface-capturing, multiphase]
timestamp: 2026-10-22T20:00:00Z
---

# Immersed-boundary and cut-cell methods

An immersed-boundary method keeps a Cartesian (or block-structured)
mesh and represents a wall, or a material interface, that crosses its
cells; in the sources the geometry is given by a signed-distance
[level set](/methods/level-set-method.md) (Wang et al. §2.2, Bai & Li
§2.5.1). The two families in the
sources differ in what they do with the crossed cells. A **ghost-cell
method** (GCM) leaves the fluid cells untouched and fills the cells just
inside the solid ("ghost cells", those with at least one fluid
neighbour) with values that make the fluid scheme see the boundary
condition. A **cut-cell method** (CCM) cuts each crossed cell along the
boundary and applies the finite-volume or DG update to the cut part.
As [Wang et al. (2022)](/sources/wang-2022.md) §1 put it, cut cells are
strictly conservative but suffer from the small-cell problem: an
explicit time step limited by the smallest cut cell, ill-conditioning
for implicit schemes.

## Ghost-cell immersed boundaries

In the notation of Wang et al. §2.3 (page-local symbols), the ghost
point $g$ lies at distance $r_G$ inside the solid from its normal
projection $p$ on the wall, and the mirror point $m$ at the same distance
into the fluid.

**Baseline method.** The ghost value is the mirror value with the
normal velocity reversed: for a slip wall
$\mathsf q_g=\mathsf q_m$, $v_{n,g}=-v_{n,m}$, $v_{t,g}=v_{t,m}$, and for a no-slip
wall also $v_{t,g}=-v_{t,m}$, with $\mathsf q$ the other primitive variables
(Eqs. 16–18). The mirror value is bilinearly interpolated from the four
surrounding cell centres. This is the method of
[AMROC](/software/amroc.md). When the ghost cell is close to the wall,
some of those four centres lie in the solid, the interpolation is
"incomplete", and its error is first order, vanishing only as the mirror
point approaches a fluid node (Fig. 1, Eqs. 37–38).

**Bilinearly complete reconstruction (BCGCM).** After Chi et al., Wang
et al. push the interpolation point (the image point $i$) to distance
$\delta=\sqrt2\,\Delta x$ from the wall, where in 2D a complete stencil
of four fluid centres always exists, and add an extrapolation point $e$
a further $r_E$ along the normal ($r_E=r_G$); a larger $\delta$ causes
"severe" extrapolation errors. A quadratic Taylor expansion along the
normal through $i$, $e$ and $p$ gives the mirror value. For variables
with a Neumann condition $\partial_n\mathsf q=0$ at the wall,

$$
\mathsf q_m=\frac{\mathsf q_i\big((\delta+r_E)^2-r_G^2\big)-\mathsf q_e\big(\delta^2-r_G^2\big)}{r_E^2+2\delta r_E},
$$

and for the normal velocity with $v_n=0$ at the wall,

$$
v_{n,m}=\frac{v_{n,e}\,\delta r_G(r_G-\delta)+v_{n,i}\,r_G(r_E+\delta-r_G)(r_E+\delta)}{\delta(r_E^2+\delta r_E)}
$$

(Eqs. 30, 32), the quadratic interpolants of the data evaluated at the
mirror point *(compiler check, not in the sources)*. The remainder is
written $o\big((\delta+r_E)^2\big)$, on which the paper bases its claim
of "theoretically proven" second-order accuracy.

**Hybrid method (HBCGCM).** Because the new error grows with
$\delta+r_E$, Wang et al. keep the baseline interpolation wherever the
mirror point has a complete stencil and use the new reconstruction only
for ghost cells too close to the wall (§2.3.2). The switching test is
described in words, not as a formula.

**Evidence.** All variants run in AMROC with second-order
[MUSCL–Hancock](/methods/muscl-hancock.md) and an approximate Riemann
solver; the cut-cell comparison runs in AMReX (§1, §2.1).

- *Unit test* (1000 random functions per case, incomplete stencils,
  grid size from 1 to $10^{-5}$): with exact image and extrapolation
  values the new reconstruction has mean observed orders 2.97 and 3.02
  against 1.92 and 1.96 for linear extrapolation; with bilinearly
  interpolated inputs 2.02 and 2.11 against 1.09 and 0.96 for the
  baseline (Figs. 4–5).
- *Prandtl–Meyer expansion* over a straight wall, deflections 20°–50°:
  observed $L^2$ orders of the entropy error near the wall 1.13–1.25
  (baseline), 1.16–1.25 (BCGCM) and 1.33–1.37 (HBCGCM), against about
  1.14 that Pember et al. report for another immersed-boundary method
(§3.3, Table 1). Over a
  curved wall the boundary-region entropy errors are
  $1.01\times10^{-4}$, $8.78\times10^{-5}$ and $2.32\times10^{-5}$
  (Fig. 13).
- *Stationary rotating vortex* in a circular wall: HBCGCM has the
  smallest mass loss and errors among the ghost-cell variants; the
  conservative cut-cell method loses less mass than all of them, but its
  mass loss converges more slowly (Figs. 9–10).
- *[Double Mach reflection](/benchmarks/double-mach-reflection.md)* off
  a 36° ramp: all four methods place the discontinuities alike; on
  $1500\times1200$ against a $6000\times4800$ reference, HBCGCM has the
  lowest density errors ($L^1$ total/boundary
  $2.3\times10^{-4}$/$5.0\times10^{-4}$, against
  $7.2\times10^{-4}$/$3.0\times10^{-3}$ baseline and
  $4.2\times10^{-4}$/$2.1\times10^{-3}$ cut cells; Table 2).
- *Schardin's problem* (a Mach 1.34 shock on a triangular obstacle):
  triple-point and vortex trajectories agree with experiment and theory
  (Figs. 16–18); *blunt-body
  [shock-induced combustion](/benchmarks/shock-induced-combustion.md)*:
  oscillation frequency within 1.4 % of Lehr's 725 kHz (Fig. 19).
- *Cost*: on one core the cut-cell method is much more expensive than
  any ghost-cell variant, and HBCGCM costs less than BCGCM and little
  more than the baseline (Fig. 20; timings not printed in the text).

## Cut cells at material interfaces

[Bai & Li (2022)](/sources/bai-2022.md) use cut cells for a
fluid–fluid interface in a discontinuous Galerkin solver: each crossed
cell is split by a straight line into two cut cells, one per fluid. To
avoid both the time step of the small cut cell and the geometric
merging of small cells with neighbours (their earlier method, which
"could not" follow topology changes), each fluid's state is projected,
together with a ghost-fluid state on the other part, onto a polynomial
on the whole cell, which is then updated like a regular cell
("real–ghost mixing"; see [level-set methods](/methods/level-set-method.md)
for the formula). Their earlier finite-volume version, a weighted
average of real and ghost cut-cell values, is the degree-zero case.
Cells cut twice and three-dimensional cut types are handled by the same
projection (§2.5.2–2.5.3, Appendix A). Unlike the conservative
cut-cell methods Wang et al. compare with, each fluid is updated with
ghost-fluid data on the other part of the cell, so the update does not
conserve mass, momentum and energy across the interface *(compiler
check, not in the sources)*; the paper measures only the mass removed
by deleting isolated structures (Fig. 6).

[Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) §1 give the
same small-cell argument for leaving AMROC's level-set and ghost-fluid
boundaries: a body-fitted mesh "can also avoid extremely small time
steps, which may occur in some small cut cells", and the level-set
treatment is sometimes expensive when many cells are cut.

**Also in the bundle.** [Deng (2023)](/sources/deng-2023.md) §8
runs [ROUND](/methods/round-scheme.md) in a finite-difference
immersed-boundary code on a [shock diffraction](/benchmarks/shock-diffraction.md)
over a cylinder, and states that its compact stencil needs fewer ghost
nodes and "speeds up" the method; no timing is given.

## Qualifications

- Wang et al. call their method "second-order accurate", with the
  little-o remainder of a quadratic expansion; the observed global order
  near the wall in their Euler tests is 1.33–1.37, and the local orders
  2–3 come from the algebraic unit test. The coupled limited solver is
  not analysed.
- Their unit-test comparison with Chi et al.'s reconstruction uses
  functions that, by the authors' own statement, violate that method's
  assumptions, so Chi et al.'s method comes out worse than linear
  extrapolation.
- That HBCGCM "has higher convergence than CCM" is inferred from the
  rate of mass-loss decay, while the cut-cell method has the smaller
  mass loss; it is not a statement about solution convergence.
- Wang et al. print the coefficient of the wall value $\mathsf q_p$ in their
  general mirror formula (Eq. 23) with the wrong sign: for $r_G=0$ it
  must be $+1$, the printed one gives $-1$ *(compiler check, not in the
  sources)*. Eqs. 30 and 32, used for walls at rest, are unaffected;
  a moving wall with a non-zero Dirichlet value would be. They also
  print the stationary-vortex pressure in a form that does not satisfy
  the radial balance it is derived from, and a curved-wall profile
  that leaves $0.6<x<0.7$ undefined.
- Their vortex test calls the wall a slip wall in one paragraph and a
  no-slip wall in another; the two coincide only where the vortex
  velocity vanishes at the wall.

# Citations

- [Wang et al. (2022)](/sources/wang-2022.md) — §1; §2.1–2.3, Eqs. (16)–(38), Figs. 1–2; §3.1–3.7, Tables 1–2, Figs. 3–20.
- [Bai & Li (2022)](/sources/bai-2022.md) — §1; §2.2; §2.5.2–2.5.3, Eqs. (27)–(29); Appendix A.
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §1 (accepted manuscript).
- [Deng (2023)](/sources/deng-2023.md) — §8, Fig. 38.
