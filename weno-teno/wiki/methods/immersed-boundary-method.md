---
type: Method
title: "Immersed-boundary and cut-cell methods"
description: "Treatments of walls and material interfaces that do not follow the mesh: sharp-interface ghost-cell immersed boundaries filling solid cells from mirror or image points, the bilinearly complete hybrid reconstruction of Wang et al., cut cells with the small-cell problem, cell merging and real–ghost mixing, and the diffuse-interface volume penalization that Kou et al. couple with high-order flux reconstruction."
status: established
aliases: [immersed boundary method, IBM, ghost-cell method, GCM, ghost-cell immersed boundary, cut-cell method, CCM, embedded boundary, HBCGCM, BCGCM, volume penalization, Brinkman penalization, IDW-IP]
tags: [immersed-boundary, finite-volume, flux-reconstruction, interface-capturing, multiphase]
timestamp: 2026-10-23T10:00:00Z
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
Both are *sharp-interface* methods. A third family, **volume
penalization**, is a *diffuse-interface* method: it only marks points as
inside or outside the body and adds a relaxation source there, so the
exact wall position is not represented
([Kou et al. (2022)](/sources/kou-2022.md), §1, §4.6).

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

## Volume penalization with flux reconstruction

[Kou et al. (2022)](/sources/kou-2022.md) couple Brinkman-type volume
penalization with high-order [flux reconstruction](/methods/flux-reconstruction.md)
on Cartesian grids for the compressible Navier–Stokes equations over
static and rigidly moving bodies; they present the combination with a
high-order method as the "aim and novelty" of the work (§1).

**Penalized equations** (§4.1, Eqs. (23)–(26)). A sharp mask
$\chi_{\mathrm s}(x,t)$ (page-local; 1 in the solid, 0 in the fluid) is
evaluated at the solution points, and every covered solution point is
penalized. With solid velocity $v_{\mathrm s}$ and penalization parameter
$\eta_{\mathrm p}$ (page-local, physically a permeability), the source
added to the right-hand side is

$$S(u)=\frac{\chi_{\mathrm s}}{\eta_{\mathrm p}}\begin{pmatrix}0\\ \rho v_{\mathrm s}-\rho v\\ \tfrac12\rho\lvert v_{\mathrm s}\rvert^2-\tfrac12\rho\lvert v\rvert^2\end{pmatrix},$$

which relaxes momentum and kinetic energy towards the solid motion; the
continuity equation is not penalized, and the wall is adiabatic, after
Abgrall et al. as recalled. No-slip on a static body is $v_{\mathrm s}=0$.

**Stiff source and time stepping** (§4.1, Eqs. (27)–(35)). The source is
treated by Strang splitting: a half step of the source, a full
three-stage SSP Runge–Kutta step of the convective and viscous terms, a
second half step of the source. The source sub-steps are either explicit
Euler or a linearized backward Euler step, which Kou et al. present as "a
new approach proposed in this paper", while citing similar implicit
treatments for compressible and incompressible multiphase flows. For
$v_{\mathrm s}=0$ the Jacobian $\partial S/\partial u$ has $-1/\eta_{\mathrm p}$
on the momentum diagonal and the row $\tfrac1{\eta_{\mathrm p}}\big(\tfrac12\lvert v\rvert^2,-v^\top,0\big)$
for the energy, and $I-\tfrac{\Delta t}2\,\partial S/\partial u$ has a
closed-form inverse, so no linear solve is needed. The implicit forcing
allows $\eta_{\mathrm p}$ "about one or two orders of magnitude" smaller
than explicit forcing at a given step; no table quantifies this.
Explicit treatment requires $\Delta t<\eta_{\mathrm p}$, as recalled
(§4.6).

**Error structure** (§4.6, Eqs. (44)–(46), as recalled from the
penalization literature). The error splits into a penalization error
$\propto\eta_{\mathrm p}^{1/2}$ for Dirichlet conditions ($\eta_{\mathrm p}$
for Neumann) and a discretization error whose rate is the smaller of the
scheme's order and the regularity of the penalized solution at the
boundary. The error saturates at $\Delta t\approx\eta_{\mathrm p}$, which
gives the rule used throughout, $\eta_{\mathrm p}=\Delta t$, with $\Delta t$
fixed by the CFL condition.

**Geometry and surface data** (§4.2–4.4). The mask of a convex body given
by Lagrangian marker points comes from a simplified ray casting (two
intercepts along one coordinate line; non-convex bodies need intersection
counting); a rigidly moving body is handled by mapping each solution
point back to the body frame at $t=0$, $\chi_{\mathrm s}(x,t)=\chi_{\mathrm s}(\tilde x,0)$,
with the rigid-body velocity prescribed (Eqs. (36)–(38)). Wall pressure
and shear stress come from inverse-distance weighting at an interpolation
point on the wall normal (IDW-IP, after Bharadwaj and Ghosh), using only
fluid points, $2$ to $3$ times the number of solution points of a
near-wall element. Evaluating the element polynomial at the wall instead
uses non-physical solid values and gives strongly oscillatory pressure
and wall vorticity (App. C, Fig. C.24).

**Evidence** (§5, App. D).

| test | setting | result |
|---|---|---|
| 1D penalized advection–diffusion | 80 elements, $\Delta t=10^{-7}$ | penalization error $O(\eta_{\mathrm p}^{1/2})$ at large $\eta_{\mathrm p}$; FR order kept with exact solid data, about first order globally with boundary-value solid data (§5.1) |
| cylinder, $\mathrm{Re}=40$, $M=0.2$ | $h=0.03D_{\mathrm c}$–$0.01D_{\mathrm c}$ (page-local diameter $D_{\mathrm c}$), degree 2–3 | $L/D_{\mathrm c}=2.27$–$2.30$, separation angle $51.2°$–$52.0°$, $C_d=1.50$–$1.52$, against body-fitted FR $2.24$, $51.0°$, $1.53$ (Table 1) |
| NACA0012, $\mathrm{Re}=5000$, $M=0.5$, $2°$ | $h=0.004$ chord, degree 2 | accuracy improves as $\eta_{\mathrm p}$ decreases down to $\Delta t$, then saturates and oscillates (Fig. 15) |
| sphere, $\mathrm{Re}=100$, $M=0.2$ | $h=0.03D_{\mathrm c}$, degree 2 | $C_d\approx1.06$ against 1.08 and 1.09 in the literature (§5.4) |
| pitching–plunging NACA0012, $\mathrm{Re}=1000$, $M=0.2$ | degrees 1–3 | forces agree with a body-fitted reference and smooth out as the degree grows (§5.5) |
| compressible cylinder (Canuto–Taira), $M=0.1$–$0.5$ | degree 2 | drag, wake lengths, lift and Strouhal trends reproduced (App. D) |

Local p-refinement near the wall reproduces the uniform degree-3 cylinder
result with 28 % of the degrees of freedom (Fig. 14;
[h- and hp-adaptation](/methods/hp-adaptation.md)). Smoothing the mask
with a Gaussian reduces near-wall pressure oscillations but adds
friction error at the leading edge and is not used (App. B).

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
- Volume penalization with boundary-value solid data loses the high
  order at the wall: Kou et al.'s global rate is about first order, by
  their account from the low regularity across the boundary (§4.6, §5.1).
  The FR order survives only away from the wall or with exact solid data.
- Kou et al.'s statement that volume penalization "has not been studied
  with the high-order methods" sits next to their own citations of
  penalization with Fourier spectral (Kolomenskiy & Schneider) and
  pseudo-spectral methods (§1).
- Kou et al.'s closed-form Jacobian (Eq. (34)) is that of the source with
  $v_{\mathrm s}=0$; with a moving body the momentum rows gain density
  derivatives $\chi_{\mathrm s}v_{\mathrm s}/\eta_{\mathrm p}$, and which
  Jacobian is used for the moving cases is not stated *(compiler check,
  not in the sources)*. They print the $\eta_{\mathrm p}$ convergence as
  "$O(\eta^{-1})$" and "$O(\eta^{-0.5})$"; the rates as
  $\eta_{\mathrm p}\to0$ are $O(\eta_{\mathrm p})$ and
  $O(\eta_{\mathrm p}^{1/2})$, consistent with their Eq. (45) (§5.1).
- Wang et al.'s vortex test calls the wall a slip wall in one paragraph and a
  no-slip wall in another; the two coincide only where the vortex
  velocity vanishes at the wall.

# Citations

- [Wang et al. (2022)](/sources/wang-2022.md) — §1; §2.1–2.3, Eqs. (16)–(38), Figs. 1–2; §3.1–3.7, Tables 1–2, Figs. 3–20.
- [Bai & Li (2022)](/sources/bai-2022.md) — §1; §2.2; §2.5.2–2.5.3, Eqs. (27)–(29); Appendix A.
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §1 (accepted manuscript).
- [Deng (2023)](/sources/deng-2023.md) — §8, Fig. 38.
- [Kou et al. (2022)](/sources/kou-2022.md) — §1, §4.1 Eqs. (23)–(35), §4.2–4.4 Eqs. (36)–(43), §4.6 Eqs. (44)–(46), §5.1–5.5 Table 1, Figs. 8–21, Apps. B–D.
