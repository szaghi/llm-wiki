---
type: Method
title: "Immersed-boundary and cut-cell methods"
description: "Treatments of walls and interfaces off the mesh: ghost-cell immersed boundaries and the bilinearly complete reconstruction, cut cells and the small-cell problem, volume penalization with flux reconstruction, image lines, ghost points with a wall model, signed-distance extrapolation on adaptive meshes, cut against ghost cells at cold walls, and true-boundary reconstruction for embedded DG."
status: established
aliases: [immersed boundary method, IBM, ghost-cell method, GCM, ghost-cell immersed boundary, cut-cell method, CCM, embedded boundary, HBCGCM, BCGCM, volume penalization, Brinkman penalization, IDW-IP, image line, HO-e, discrete forcing, eikonal extrapolation]
tags: [immersed-boundary, finite-volume, flux-reconstruction, interface-capturing, multiphase]
timestamp: 2026-10-23T23:45:00Z
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
As [Wang et al. (2022a)](/sources/wang-2022.md) §1 put it, cut cells are
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

## High-order image lines for flux reconstruction

[Funada & Imamura (2023)](/sources/funada-2023.md) build sharp-interface,
discrete-forcing wall conditions for Huynh's
[flux reconstruction](/methods/flux-reconstruction.md) on hierarchical
Cartesian grids, for inviscid flow, and aim at keeping the design order
$N+1$ up to the wall; they recall that earlier immersed-boundary methods
are second order or lower, and Kou et al.'s volume penalization first
order near the wall (§1). Cells are fluid, wall (cut by the body) or body
cells. At every flux point on a fluid/wall-cell face a wall-side state is
built and the common flux (SLAU) is computed from it and the fluid-side
trace (§2.3, Figs. 4–5). The wall conditions are those of an adiabatic slip
wall with curvature, written as $v_n=0$, $\partial_nH=0$,
$\partial_n(p\rho^{-\gamma})=0$ and $\partial_nv_t=v_t/R_{\mathrm c}$
(page-local normal and tangential velocity $v_n$, $v_t$, wall curvature
radius $R_{\mathrm c}$; Eq. (15)); the paper calls them equivalent to the
set in $\rho$, $p$, $v_t$ of Eq. (14). Four constructions:

- **LO.** One image point on the wall normal at $3\Delta x$; density,
  pressure and tangential velocity copied, normal velocity scaled
  linearly with distance. First order (§2.3.1, Eqs. (16)–(17)).
- **HO-i/c.** An *image line* of length $d_{\mathrm{IL}}$ along the normal,
  with $N+1$ image points at the Gauss points of the line. The states at
  points $2,\dots,N+1$ come from the FR polynomials of their fluid cells;
  the first point is eliminated by imposing the four conditions on the
  Lagrange interpolant at the wall end, e.g.
  $v_{n,1}=-\sum_{i\ge2}\ell_i(-1)v_{n,i}/\ell_1(-1)$ for $v_n=0$ and the
  analogous derivative conditions for $H$ and $p\rho^{-\gamma}$; the
  degree-$N$ line polynomials are then evaluated at the flux point (§2.3.2,
  Eqs. (18)–(19)).
- **HO-i/f.** The same with $R_{\mathrm c}\to\infty$, i.e.
  $\partial_nv_t=0$ (Eq. (20)).
- **HO-e.** As HO-i/c for $v_n$, $H$, $p\rho^{-\gamma}$, but $v_t$ is
  extrapolated to the flux point from a second set of image points lying
  wholly in the fluid; no curvature is needed (Eq. (21), Fig. 8).

The second image point must lie in a fluid cell,
$d_{\mathrm{IL}}(1+\xi_2)/2\ge\sqrt{d}\,\Delta x$ with $\xi_2$ its Gauss
coordinate and $d$ the space dimension (Eq. (22)); the bounds are
$1.79$, $2.83$, $4.29\,\Delta x$ for $N=1,2,3$ in 2D and $2.20$, $3.46$,
$5.25\,\Delta x$ in 3D, and the lengths used are $3,3,5\,\Delta x$ (2D) and
$3,5,7\,\Delta x$ (3D). In 3D the line polynomials are built in the plane of
the normal and the tangential velocity direction at the second image
point (Eq. (23)). Where an image line would enter a cell containing
another body, the wall is treated as a step-wise face (§2.3.2).

**Evidence** (steady inviscid flows, $L_2$ error of $p\rho^{-\gamma}$ against
its free-stream value, $N=1,2,3$; §3):

| test | LO | HO-i/f | HO-i/c | HO-e |
|---|---|---|---|---|
| bump channel, $M=0.5$: order | below $N+1$ | below $N+1$ | $N+1$ | $N+1$ |
| bump, $N=2$, $\Delta x_{\min}=0.01$: $C_d$ (ideal 0) | $2.7\times10^{-5}$ | $3.6\times10^{-5}$ | $7.8\times10^{-7}$ | $1.0\times10^{-7}$ |
| [cylinder](/benchmarks/flow-past-circular-cylinder.md), $M=0.3$, $N=2$: $C_d$ | $5.0\times10^{-2}$ | $1.2\times10^{-2}$ | $9.1\times10^{-5}$ | $4.5\times10^{-4}$ |
| sphere, $M=0.2$, $N=2$: $C_d$ | $1.5\times10^{-2}$ | $1.4\times10^{-2}$ | $7.0\times10^{-4}$ | $9.0\times10^{-4}$ |

(Figs. 12, 17–19, 23; Tables 1–3.) HO-i/c and HO-e reach order $N+1$ on all
three, with errors one to three orders of magnitude below LO and HO-i/f on
the bump; ignoring the wall curvature (HO-i/f) loses the order. The
authors recommend HO-e for complex geometries because it needs no wall
curvature (§3.4, §4); on the cylinder and the sphere HO-i/c has the smaller
drag error (Tables 2–3). On the non-uniform cylinder and sphere grids the
order is read against $1/\Delta x_{\min}$, because against the square root
of the number of degrees of freedom the slopes are "much steeper" than the
design order (§3.3).

## Ghost points with a wall model

[De Vanna et al. (2023c)](/sources/devanna-2023-c.md)
use a sharp-interface ghost-point method in the finite-difference solver
[URANOS](/software/uranos.md), after the group's earlier work: bodies are
closed polygons, grid points are flagged solid or fluid by ray tracing,
and the ghost set is the solid points within $n_g$ points of a fluid point,
$n_g$ the stencil half-width (page-local; §2.3, Eq. (9)). Each ghost point
has a wall-normal probe and an image point in the fluid, with bilinear
(2D) or trilinear (3D) interpolation there. Dirichlet values are imposed
as $\mathsf q_g=2\mathsf q_b-\mathsf q_{\mathrm{ip}}$ and Neumann values as
$\mathsf q_g=\mathsf q_{\mathrm{ip}}$ on the primitive variables ($\mathsf q$ as
above), e.g.
$v_g=-v_{\mathrm{ip}}$ for no-slip and $p_g=p_{\mathrm{ip}}$ (Eqs. (15)–(18);
page-local $b$ boundary point, ip image point). The authors call this
near-wall treatment second order and note its limitation at high Reynolds
number: the image point lies far from the wall in viscous units, so
friction and heat flux are underestimated. Their remedy is a
[wall model](/methods/wall-modeled-les.md) imposed through the ghost-point
viscosity, $\mu_g=2\mu_{\mathrm{eff}}-\mu_{\mathrm{ip}}$, switched on point by
point where the local inner-scaled spacing is too coarse (§3.5,
Eqs. (21)–(25)). Walls in their channel, pipe, boundary-layer and
compression-ramp tests are all immersed blocks (§4).

## Signed-distance extrapolation on adaptive meshes

[Zaghi et al. (2023)](/sources/zaghi-2023.md) couple the immersed-boundary
method of Di Mascio & Zaghi with block-structured
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) in
[ADAM](/software/adam.md). The body is the zero level of a signed distance
$\phi_{\mathrm d}$ (page-local; positive inside the body), with normal
$n=\nabla\phi_{\mathrm d}/\lvert\nabla\phi_{\mathrm d}\rvert$
([level-set methods](/methods/level-set-method.md)). The solution is
extrapolated into the body by marching
$\partial_\tau\mathsf q+n\cdot\nabla\mathsf q=0$ in a pseudo-time $\tau$
(page-local) towards steady state; one propagation step at a CFL number
close to 1 per Runge–Kutta stage suffices, as they recall from the earlier
paper (§3.1.1, Eq. (10)). The wall conditions are then imposed through the
fluxes of the cells cut by the zero level. The coupling fixes an order per
time step: adapt the grid if needed and recompute $\phi_{\mathrm d}$; then, in
each Runge–Kutta stage, update the ghost cells, run the extrapolation steps
with their own ghost updates, impose the immersed-boundary conditions and
compute the residual (§3.1.1). The test is the 3D diffraction of a strong
shock by a sphere on up to 350 million cells and 256 GPUs
([shock diffraction](/benchmarks/shock-diffraction.md)); the immersed
boundary is not assessed separately from the AMR (§3).

## Ghost cells against cut cells at cold and reacting walls

[Başkaya et al. (2024)](/sources/baskaya-2024.md) compare wall treatments
for hypersonic flows in chemical non-equilibrium with gas–surface
interaction, on a curated set of eight verification and validation cases
(§4, Table 1; author preprint). All three solvers use the same
thermochemistry library, so the authors attribute the differences to the
numerics:

- **body-fitted (BF)**: US3D, modified Steger–Warming flux with MUSCL,
  implicit relaxation to steady state;
- **cut cells (IB-CC)**: INCA, a block-Cartesian AMR finite-volume solver
  with third-order [WENO](/methods/weno-js-reconstruction.md), HLLC, RK3 and
  Strang-split chemistry. Its "cut-element" method keeps every intersection
  of the Cartesian grid with the surface triangulation, possibly several
  cut-elements per cut cell, and balances the fluxes over the fluid part of
  each cut cell with face fluxes scaled by wetted areas; small cut cells
  are mixed or merged with neighbours. Ghost cells are kept as well, so
  that unmodified stencils work everywhere (§3, §3.2);
- **ghost cells (IB-GP)**: CHESS, Steger–Warming splitting with MUSCL, and
  INCA itself with the cut-cell flux treatment switched off (§3.2, §5).

The authors describe the ghost-cell method as not strictly conservative,
with errors from the nonlinearity of the flux, the image-point
interpolation and the interface curvature (§3). Results on the HEG
cylinder (radius 0.045 m, $M_\infty=8.98$, 5-species air;
[flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)):

| wall | finding |
|---|---|
| inert adiabatic | shock stand-off and dissociation agree for all three (Fig. 7) |
| inert isothermal, $T_w=300$ K | BF and IB-CC agree "almost exactly"; stagnation heat flux 7.345 (BF) and 7.144 (IB-CC) MW/m² on the medium–fine meshes against an experimental $7.402\pm0.220$; IB-GP 0.167 MW/m², with a larger stand-off distance (Table 7, Fig. 8) |
| fully catalytic, 300 K | BF and IB-CC in "excellent agreement", IB-CC 0.2 % below BF (Fig. 11) |

On a graphite ablator in nitrogen plasma both ghost-cell solvers
overpredict the mass blowing rate. Because INCA-GP and INCA-CC differ only
in the conservative flux treatment, and INCA-GP's heat flux is closer to
the body-fitted one than CHESS's but still "clearly wrong", the authors
conclude that conservation errors of ghost-cell methods cause the large
errors at cold walls, acting as an unphysical surface blowing (§5, Fig.
18). They expect these errors to converge at the truncation rate of the
base scheme, so to matter only where the wall gradients of the conserved
variables are large, cold isothermal and reacting walls and not adiabatic
ones (§5); no convergence study of the conservation error is shown. They
reject the explanation of Brahmachary et al., linear interpolation of
temperature, because the cut-cell method also reconstructs to second order
and predicts correctly (§4.5.2). The conservative cut cells of Wang et al.
above likewise lose the least mass on the rotating vortex.

## Embedded boundaries for DG: reconstruction on the true boundary

[Ciallella et al. (2024)](/sources/ciallella-2024.md) treat curved walls in
modal [ADER](/methods/ader-scheme.md)-[DG](/methods/discontinuous-galerkin.md)
on triangulations whose boundary $\partial\Omega_h$ differs from the true
boundary $\partial\Omega$: conformal straight-sided meshes, and fully
embedded meshes whose surrogate boundary is detached from it (§1, §4;
arXiv v1). Imposing the boundary data on $\partial\Omega_h$ limits DG to
second order, and to first-order boundary consistency on embedded meshes
(§4). Their method transfers the Reconstruction for Off-site Data (ROD) of
Costa, Clain et al. from finite volumes to DG (§5, page-local symbols):

- **Reconstruction.** In each boundary element the DG polynomial used in
  the boundary flux is replaced by a polynomial of the same degree in a
  monomial basis, fitted by weighted least squares to the element's own
  predictor values at its quadrature points, under linear constraints
  $\mathsf a_\Gamma\varphi+\mathsf b_\Gamma\partial_n\varphi=g_\Gamma$ (page-local
  Robin coefficients and data) at the projections of the boundary-face
  quadrature points onto $\partial\Omega$ along the normal; Lagrange
  multipliers give a saddle-point system (Eqs. (22)–(29)). Unlike the
  finite-volume ROD, which needs a neighbour stencil of about $1.5$ times
  the number of coefficients found by a search, the DG version uses only
  the element's own polynomial (Remark 3). For $N=2$ and $N=3$ the local
  systems are $9\times9$ and $14\times14$ (§7).
- **Space–time variant.** Written in the ADER predictor's space–time basis,
  one constrained solve per space–time boundary element replaces one per
  sub-time node (Eqs. (30)–(33); see the ADER page).
- **Curved slip walls.** After Chertock, Coco, Kurganov & Russo the slip
  condition on a curved wall is imposed as
  $v_n=0$, $\partial_n(p\rho^{-\gamma})=0$, $\partial_nH=0$ and
  $\partial_nv_t-v_t\,\kappa_{\mathrm c}=0$ (page-local normal and tangential
  velocity $v_n$, $v_t$; boundary curvature $\kappa_{\mathrm c}$ as in the registry; Eqs. (16)–(21)), linear in
  $(v_n,p\rho^{-\gamma},H,v_t)$, which are obtained by a space–time $L_2$
  projection of the predictor; the normal and tangent come from a level set
  (Eqs. (34)–(35), Remark 5). This is the set of wall conditions that Funada
  & Imamura impose with image lines, their $\partial_nv_t=v_t/R_{\mathrm c}$
  with $\kappa_{\mathrm c}=1/R_{\mathrm c}$ up to the sign convention of the
  curvature *(compiler check, not in the sources)*. Troubled boundary cells
  flagged by the a posteriori limiter use a corrected wall flux after
  Krivodonova & Berger instead, said to be at most third order (§5.3.2).

**Evidence** (§6). On a manufactured steady Euler solution with Dirichlet
data on a trefoil-like boundary, the uncorrected scheme converges at second
order for $N=1$–3 (Table 2), the reconstruction at finest-level rates 2.02,
2.82, 4.10 on conformal meshes ($\rho$ error $1.5035\times10^{-10}$ at $N=3$,
Table 4), and non-monotonically on embedded meshes, e.g. 3.76, 4.17, 1.53,
4.47 for the space–time variant at $N=3$ (Table 7), which the authors call
typical of embedded methods because the surrogate boundary approaches the
true one depending on how it cuts the background mesh. With curved slip
walls on the supersonic vortex between concentric arcs the authors state
order $N$ rather than $N+1$, because the Neumann and Robin conditions use
polynomial derivatives (finest-level rates 2.04–2.11, 2.07–2.09, 2.40–2.57
for $N=1,2,3$), against uncorrected rates below 2 with errors that grow
with $N$ and a crash at $N=3$ on the coarsest mesh (Tables 9–10). They
point to neighbour information for the derivative polynomials of the
Neumann and Robin cells, as in the finite-volume ROD of Costa et al., to
recover the order (§6.2). A Mach 1.3
shock–cylinder interaction at $N=3$ with subcell limiting gives smooth
contours where naive reflecting walls generate spurious waves (§6.3,
Figs. 8–9).

## Qualifications

- Funada & Imamura's image lines reach order $N+1$ with curved slip-wall
  conditions on the same variables, while Ciallella et al. reach about $N$;
  the two treatments differ (image lines through fluid cells in FR, against
  constrained reconstruction inside one DG element) and are tested on
  different problems, so the difference is not a contradiction.
- Ciallella et al. write that "in all cases, the expected convergence of
  $M+1$ is achieved" (§6.1, their $M$ the degree), while their $N=2$ rates
  on conformal meshes are 2.61–2.99 (Table 4) and their embedded rates
  oscillate between 0.57 and 4.50 (Tables 5, 7). The order columns of their
  Table 5 are not reproduced by the printed errors and the mesh sizes of
  their Table 3 (e.g. $N=1$, $\rho$: 2.42, 1.50, 0.73, 2.50 against the printed
  2.26, 1.64, 0.74, 2.26), whereas those of Table 7 are, to about $\pm0.04$
  *(compiler check, not in the sources)*. Their cost saving of about 10 %
  for the space–time variant is given without timings.
- Başkaya et al.'s evidence is two second-order ghost-cell
  implementations; higher-order or conservatively corrected ghost-cell
  variants, such as those above, are not tested. Their read version is the
  submitted preprint, whose numbers may differ from the version of record.
- Funada & Imamura assert, without derivation, that their two wall
  condition sets (14) and (15) are equivalent for smooth 2D inviscid flow.
  $\partial_nH=0$ and $\partial_n(p\rho^{-\gamma})=0$ at the wall hold when
  $H$ and the entropy are uniform in the field, as in all their tests
  *(compiler check, not in the sources)*. Their Eq. (28) prints the
  entropy error with the density ratio inverted, $\frac p{p_\infty}\big(\frac\rho{\rho_\infty}\big)^\gamma-1$,
  which does not vanish for isentropic changes; the entropy function is
  $p\rho^{-\gamma}$ (their Eq. (15c)) *(compiler check, not in the
  sources)*. The value of $\gamma$ is not printed.
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

- [Wang et al. (2022a)](/sources/wang-2022.md) — §1; §2.1–2.3, Eqs. (16)–(38), Figs. 1–2; §3.1–3.7, Tables 1–2, Figs. 3–20.
- [Bai & Li (2022)](/sources/bai-2022.md) — §1; §2.2; §2.5.2–2.5.3, Eqs. (27)–(29); Appendix A.
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §1 (accepted manuscript).
- [Deng (2023)](/sources/deng-2023.md) — §8, Fig. 38.
- [Kou et al. (2022)](/sources/kou-2022.md) — §1, §4.1 Eqs. (23)–(35), §4.2–4.4 Eqs. (36)–(43), §4.6 Eqs. (44)–(46), §5.1–5.5 Table 1, Figs. 8–21, Apps. B–D.
- [Funada & Imamura (2023)](/sources/funada-2023.md) — §1, §2.3 Eqs. (14)–(23), Figs. 4–9, §3.2–3.4 Tables 1–3 Figs. 12–25, §4.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §2.3 Eqs. (9), (15)–(18), §3.5 Eqs. (21)–(25), §4.
- [Zaghi et al. (2023)](/sources/zaghi-2023.md) — §3, §3.1.1 Eq. (10).
- [Başkaya et al. (2024)](/sources/baskaya-2024.md) — author preprint: §3, §3.2, §4 Table 1, §4.5 Table 7 Figs. 7–11, §4.6, §5 Fig. 18.
- [Ciallella et al. (2024)](/sources/ciallella-2024.md) — arXiv v1: §1, §4 Eqs. (15)–(21), §5 Eqs. (22)–(36), Remarks 3–5, §6 Tables 2, 4, 5, 7, 9, 10, Figs. 8–9, §7.
