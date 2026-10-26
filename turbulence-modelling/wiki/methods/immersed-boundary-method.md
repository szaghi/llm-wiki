---
type: Method
title: "Immersed boundary methods"
description: "Immersed boundary methods impose solid walls on grids that do not conform to them, by reconstructing values at boundary or ghost points or by a penalization source; this page covers the variants used for DNS and LES, their coupling with wall models in a lattice Boltzmann solver, and the loss of near-wall stress they cause."
status: established
aliases: [IBM, immersed boundary, ghost-point forcing, volume penalization, IB wall model]
tags: [immersed-boundary, wall-model, lattice-boltzmann, les, dns]
timestamp: 2026-10-26T05:06:00Z
---

# Immersed boundary methods

An **immersed boundary method (IBM)** represents a solid body on a grid that
does not conform to its surface (a Cartesian or octree mesh, or a
high-order mesh that ignores the body), and imposes the wall condition
either by **reconstructing** the flow variables at grid points near or inside
the body from the wall value and the surrounding fluid, or by a
**penalization source term** that drives the velocity towards the body
velocity inside a mask. In the sources it carries DNS of pipe flow on a
Cartesian mesh, implicit LES of a capsule wake, wall-modelled LES of a car
body in a lattice Boltzmann code, and rotating blades in a DG code. Two
sources report a less accurate near-wall field: the wall distance of the
near-wall nodes varies along the surface and the method does not conserve
fluxes across the immersed surface (Cai et al. 2022), and a softly imposed
no-slip condition can leave a residual wall velocity (Vicente Cruz &
Lamballais 2023).

## Variants

**Reconstruction at boundary points (lattice Boltzmann).** In the ProLB
solver used by [Cai et al. (2022)](/sources/cai-2022.md), §II.B.1, the
boundary points are grid points just off the surface; along the wall normal
through each, fictitious reference points are placed at distances $h$ and
$2h$ ($h$ the local grid size; page-local $q_b$, $q_s$, $q_1$, $q_2$ the
values at the boundary point, the surface and the two reference points, $d$
the distance of the boundary point to the surface), their values
interpolated from the neighbours. Linear Dirichlet reconstruction reads
$$q_b=\frac{h\,q_s+d\,q_1}{d+h}$$
(Eq. 17); the quadratic Dirichlet (Eq. 16) and Neumann (Eq. 18) forms are
printed in lattice units (see Qualifications), and the linear Neumann
condition is $q_b=q_1$ (Eq. 19). The lattice populations at boundary points
are rebuilt from the macroscopic state as the equilibrium plus a
non-equilibrium part computed from the finite-difference strain rate
(Eq. 20); bounce-back is noted as limited to no-slip walls.

**Ghost-point forcing (finite differences).** In [STREAmS](/software/streams.md),
[Placco et al. (2023)](/sources/placco-2023.md), §2, tag grid nodes as fluid
or solid, compute their distance to the interface, and enforce no-slip and
no-penetration through ghost nodes filled with values interpolated from the
fluid (method of Piquet et al. and of De Vanna et al., the latter a
sharp-interface method for moving bodies in compressible viscous flow, as
recalled; no equations printed).

**Reconstruction inside the solid (compact finite differences).**
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md), §3,
reconstruct the solution inside the solid so that the sixth-order compact
schemes of Xcompact3d can differentiate across the domain as if it were
periodic; the no-slip condition is imposed softly and can leave a residual
wall velocity, and the treatment is not kinetic-energy conserving
(footnote 6). They assume that the reconstruction keeps the implicit filter
homogeneous, which their LES analysis needs (§2.1).

**Volume penalization (DG).** [Ferrer et al. (2023)](/sources/ferrer-2023.md),
§4.7, Eqs. (27)–(29), add to the momentum and energy equations of
[HORSES3D](/software/horses3d.md) a source
$$\frac{\chi}{\eta_p}\Big(\rho(\boldsymbol u_s-\boldsymbol u),\ \tfrac{\rho}{2}\big(|\boldsymbol u_s|^2-|\boldsymbol u|^2\big)\Big),$$
with $\chi=1$ in the solid and 0 in the fluid, $\eta_p$ the permeability and
$\boldsymbol u_s$ the body velocity (page-local; Ferrer et al. write $\eta$).
The mask is built by ray tracing of an STL surface on a surface-area-heuristic
k-d tree, parallel in OpenMP and MPI, and surface quantities are recovered
by inverse-distance weighting of the nearest degrees of freedom. The
demonstration is a horizontal-axis wind turbine with rotating blades
($N=3$ near the rotor and wake, $N=2$ elsewhere), shown qualitatively.

## Resolution near an immersed wall

- **Wall-resolved DNS.** Vicente Cruz & Lamballais (2023, §7.1) compute pipe
  flow at $Re_\tau=1000$ on $768\times768\times1920$ points with a uniform
  $\Delta x^+=\Delta y^+\approx3$ and no near-wall refinement, in excellent
  agreement with the DNS of El Khoury et al., and suggest that a first
  wall-normal spacing of one wall unit "may be somewhat over-demanding". In
  LES on the same IBM (uniform $\Delta x^+\approx9$) the friction-velocity
  error is $+15.3\%$ without model, $+9.6\%$ with Smagorinsky and van Driest
  damping and $-1.8\%$ with implicit spectral vanishing viscosity; see
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
- **Unresolved walls.** Placco et al. (2023) do not report the near-wall
  resolution of the capsule at $Re=10^6$ on their $2048\times672\times672$
  rectilinear grid. Cai et al. (2022, §III, Table I) estimate a viscous
  sublayer height of $3.4\times10^{-5}H$ against a finest spacing of
  $4.5\times10^{-3}H$ on their fine grid ($H$ the body height), and state
  that resolving the viscous sublayer or the Kolmogorov scale is not
  feasible on their hierarchical grid, hence the wall model.

## Wall models on immersed boundaries

Cai et al. (2022, §I, §II.C.1) state, citing the group's earlier studies,
that IBMs coupled with wall models on Cartesian grids produce spurious
oscillations of wall pressure and skin friction and over-estimate the mean
skin friction, because the wall distance of near-wall nodes varies and the
under-resolved velocity profile is steep, which makes the result sensitive to
the interpolation and gradient schemes. Their procedure:

1. invert an explicit [equilibrium wall model](/methods/equilibrium-wall-model.md)
   at the neighbouring fluid points (a blended viscous/log law inverted in
   closed form with the Lambert $W$ function, so no Newton iteration is
   needed) and interpolate the **friction velocity**, not the velocity, to
   the boundary points, which smooths the surface quantities even with
   inverse-distance weighting because $u_\tau$ varies smoothly;
2. set the tangential velocity at the boundary point from the forward wall
   law, the normal velocity to zero, and the wall-stress direction to that of
   the near-wall fluid;
3. compute gradients by weighted least squares and correct the wall-normal
   gradient of the tangential velocity, "highly underestimated regardless of
   the accuracy of the gradient schemes", with a discrete wall-law gradient.

**Loss of near-wall stress.** Because the IBM is not conservative across the
non-fitted surface, the total Reynolds stress near the wall is not
maintained, so skin friction deviates and, in LES, turbulence development is
strongly delayed (Cai et al. 2022, §II.C.1). Their remedy is a constrained-LES
eddy viscosity applied over a few grid points from the wall, which adds to a
mixing-length RANS viscosity
$\nu_t^{\mathrm{RANS}}=\nu\kappa y^+(1-e^{-y^+/19})^2$ the resolved stress
projected on the mean strain,
$$\nu_t^{\mathrm{hyb}}=\frac{2\nu_t^{\mathrm{RANS}}\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle+R^{\mathrm{LES}}_{ij}\langle\tilde S_{ij}\rangle}{2\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle},\qquad R^{\mathrm{LES}}_{ij}=\langle\tilde u_i\tilde u_j\rangle-\langle\tilde u_i\rangle\langle\tilde u_j\rangle$$
(Eq. 27, positive-trace resolved stress; page-local superscripts). Contracting
the condition that modelled plus resolved stress equal the RANS stress,
$-2\nu_t^{\mathrm{hyb}}\langle\tilde S_{ij}\rangle+R^{\mathrm{LES}}_{ij}=-2\nu_t^{\mathrm{RANS}}\langle\tilde S_{ij}\rangle$,
with $\langle\tilde S_{ij}\rangle$ gives Eq. 27 *(compiler check, not in the
sources)*. The authors state that it tends to the RANS viscosity in attached
layers and to the LES viscosity in separated ones; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[wall-modelled LES](/methods/wall-modelled-les.md).

## The lattice Boltzmann host solver

ProLB, as summarized by Cai et al. (2022, §II.A): D3Q19 lattice, a
BGK-type equation whose relaxation time $\tau_r$ (page-local) sets the total
viscosity $\nu+\nu_t=c_s^2(\tau_r-\Delta t/2)$ with lattice sound speed
$c_s=1/\sqrt3$, the weakly compressible Navier–Stokes equations recovered
for $M<0.3$ by Chapman–Enskog expansion. Plain BGK is not stable at high
Reynolds number, so a hybrid recursive regularized collision adds a
hyper-viscosity weighted by a parameter "chosen as close to unity as
possible". The subgrid model is [Vreman's](/methods/vreman-model.md),
$\nu_t=2.5C_s^2\Delta^2\sqrt{B_\beta/A_\beta}$ with $C_s\approx0.1$ and
$\Delta$ the grid size. The time step is tied to the finest grid,
$\Delta t=(c_s/c_0)\Delta x_{\min}$ with $c_0$ the physical sound speed, so the
Mach number is raised from 0.12 to 0.24 to double the time step, on the
argument that it barely affects nearly incompressible results (§III, citing
Fares).

## Application: Ahmed body with a 35° slant

Cai et al. (2022, §III–§IV, Tables II–III) compute the Ahmed body at
$Re_H=7.68\times10^5$ against the Lienhart & Becker experiment on octree
grids of $1.36\times10^7$ (coarse, $\Delta x_{\min}=9.0\times10^{-3}H$) and
$4.03\times10^7$ cells (fine, $4.5\times10^{-3}H$), comparing a wall model on
the whole body ("wall-law") with a no-slip condition imposed on slant and
base ("no-slip"). On the coarse grid the wall-law flow does not separate on
the slant, which the authors attribute to the assumed alignment of wall
stress and velocity and to too little near-wall turbulent stress; on the
fine grid it separates massively, and "overall on the fine grid, the
wall-law boundary condition outperforms the no-slip boundary condition" in
the velocity profiles, while no-slip separates too early on the slant. They
state that "enhancing the Reynolds stress close to wall is very essential to
drive the flow to separate in the immersed boundary framework"; no run
without the enhancement is shown. Drag coefficients (near-field/far-field):
wall-law fine 0.2347/0.2380, coarse 0.2742/0.2912; no-slip fine
0.2553/0.2588, coarse 0.2548/0.2486; experiments 0.279 (Meile et al., same
$Re_H$) and 0.26 (Ahmed et al.).

## Qualifications

- Cai et al. (2022) print the quadratic reconstructions as
  $q_b=-\frac{-2q_s+dq_2+d^2q_2-2d^2q_1-4dq_1}{(d+2h)(d+h)}$ (Eq. 16) and
  $q_b=(4q_1-q_2)/(3h)$ (Eq. 18), dimensionally consistent only for $h=1$
  (lattice units), while the linear Eq. 17 keeps $h$. Quadratic interpolation
  through $q_s$ at the wall and $q_1$, $q_2$ at $d+h$, $d+2h$ gives
  $q_b=\frac{2h^2q_s+2d(d+2h)q_1-d(d+h)q_2}{(d+h)(d+2h)}$, equal to Eq. 16 for
  $h=1$, and a zero normal gradient gives $q_b=(4q_1-q_2)/3$ *(compiler check,
  not in the sources)*.
- Cai et al. (2022) state that the fine-grid wall-law drag is closer to the
  experiment of Meile et al. than the body-fitted IDDES of Guilmineau et al.
  (0.3452); against the other body-fitted entries of their Table III
  ($k$-$\omega$ SST 0.2999, EARSM 0.2603, DES 0.3156) and against their own
  no-slip fine run it is not, and the coarse wall-law case, which does not
  separate on the slant, is the closest to 0.279 *(compiler check, not in the
  sources)*. Their judgement in favour of the wall law rests on velocity
  profiles.
- Cai et al. (2022) do not print how $\nu_t^{\mathrm{hyb}}$ returns to the
  subgrid viscosity away from the wall, nor the value of $\kappa$.
- Vicente Cruz & Lamballais (2023) and Cai et al. (2022) both report that the
  immersed treatment degrades the near-wall solution (residual wall velocity;
  lost Reynolds stress); the two concern different methods and are not
  compared.

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §II.A, Eqs. (1)–(15) (lattice Boltzmann, HRR collision, Vreman model); §II.B.1, Eqs. (16)–(20) (boundary-point reconstruction); §II.C.1, Eqs. (24)–(27), Fig. 1 (wall model on the IBM, constrained LES); §III, Tables I–II, Eq. (28); §IV, Table III, Figs. 4–9 (Ahmed body).
- [Placco et al. (2023)](/sources/placco-2023.md) — §2 (ghost-point-forcing IBM in STREAmS); §3 (grid).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.7, Eqs. (27)–(29), Fig. 14 (volume penalization, ray tracing, wind turbine).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1; §3, footnote 6 (reconstruction inside the solid, soft no-slip); §7.1, Fig. 24 (pipe DNS and LES).
