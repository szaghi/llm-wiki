---
type: Method
title: "Immersed boundary methods"
description: "Immersed boundary methods impose walls on non-conforming grids by reconstruction at boundary or ghost points, penalization or direct forcing; this page covers the DNS, LES and RANS variants, the Lagrangian weight, flexible blades, wall functions with a modelling height, wall-pressure reconstruction, Reynolds averaging of penalized flows, and the near-wall errors reported."
status: established
aliases: [IBM, volume penalization immersed boundary method, VP-IBM, fluid resistance, immersed boundary, ghost-point forcing, volume penalization, IB wall model, direct-forcing immersed boundary, Lagrangian weight, modelling height, ghost-cell direct forcing]
tags: [immersed-boundary, wall-model, lattice-boltzmann, les, dns, rans]
timestamp: 2026-10-26T15:48:00Z
---

# Immersed boundary methods

An **immersed boundary method (IBM)** represents a solid body on a grid that
does not conform to its surface (a Cartesian or octree mesh, or a
high-order mesh that ignores the body), and imposes the wall condition
either by **reconstructing** the flow variables at grid points near or inside
the body from the wall value and the surrounding fluid, or by a
**penalization source term** that drives the velocity towards the body
velocity inside a mask, or by **direct forcing** computed on Lagrangian
surface markers and spread to the grid. In the sources it carries DNS of pipe flow on a
Cartesian mesh, implicit LES of a capsule wake, wall-modelled LES of a car
body in a lattice Boltzmann code, rotating blades in a DG code, an
elastic beam in turbulent cross-flow in a lattice Boltzmann code, DNS and
neural-network LES of a cylinder wake on a staggered finite-volume mesh
([Kim et al. 2024](/sources/kim-2024.md)), hybrid RANS/LES in a lattice
Boltzmann code ([Mozaffari et al. 2024](/sources/mozaffari-2024.md)) and
steady wall-function RANS of high-lift aircraft on octree Cartesian grids
([Constant et al. 2024](/sources/constant-2024.md)). Three
sources report a less accurate near-wall field: the wall distance of the
near-wall nodes varies along the surface and the method does not conserve
fluxes across the immersed surface (Cai et al. 2022), a softly imposed
no-slip condition can leave a residual wall velocity (Vicente Cruz &
Lamballais 2023), and with direct forcing the interpolation and spreading
operators are not reciprocal, which leaves a boundary slip error
([Cheylan et al. 2023](/sources/cheylan-2023.md)). A fourth error concerns
the wall pressure: extrapolating it unchanged from the first fluid point
across a modelled layer misplaces the suction peak and corrupts the
near-field pressure drag at strong incidence (Constant et al. 2024).

## Variants

**Reconstruction at boundary points (lattice Boltzmann).** In the
[ProLB](/software/prolb.md) solver used by [Cai et al. (2022)](/sources/cai-2022.md), §II.B.1, the
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
Mozaffari et al. (2024, §2.2, Fig. 1) describe the same ProLB treatment:
reference points at successive distances of the local grid size along the
normal, linear or quadratic reconstruction by boundary type (Dirichlet for
inflow or no-slip velocity, Neumann for outflow), populations rebuilt from
the equilibrium and the symmetric velocity gradient; with a wall model the
tangential velocity at the reference point gives $u_\tau$, and the
velocity and turbulence quantities of the first off-wall node follow from
the wall law. They state that, with the isotropic mesh of ProLB, refining
the grid enough to resolve the boundary layer at high Reynolds number is
"too expensive", hence the wall model.

**Mass source and momentum forcing (staggered finite volume).**
Kim et al. (2024, §2.1, Eqs. 2.1–2.2) use the immersed boundary method of
Kim, Kim & Choi (2001, as recalled), which adds a mass source/sink $q$ to
the continuity equation, $\partial_i\bar u_i-q=0$, and a momentum forcing
$f_i$ to the momentum equations, on a staggered Cartesian mesh with
second-order central differences (energy-conserving, no numerical
dissipation, as stated), a fractional-step method with third-order
Runge–Kutta for convection and Crank–Nicolson for diffusion. The same
formulation carries both the DNS ($\tau_{ij}=0$, $1025\times501\times128$
points) and the LES of the circular cylinder at $Re_D=3900$; see
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) and
[neural-network SGS models](/methods/neural-network-sgs-model.md). Second-order
central differences produce spurious oscillations near the front of the
cylinder, removed by switching to QUICK upwinding for $x/D<-0.25$ without
changing the wake at this Reynolds number (§4.2.1, Fig. 9 inset).

**Ghost-cell direct forcing with a modelling height (RANS, octree
Cartesian grids).** Constant et al. (2024, §3) extend the ghost-cell
direct-forcing method of Péron et al. (as recalled) in ONERA's FastS
second-order finite-volume solver for steady RANS with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md). Three point
families are used: **target (forcing) points**, at least two layers on the
solid side; **image points**, the projection of each target point along the
wall normal onto a watertight surface built from the first computed cell
centres, where the solution is interpolated (second order) from computed
donors; and **wall points**, the projection onto the body surface, which
store wall data for post-processing (§3, Figs. 3, 6). The values at a
target point A are set from the image point B by an
[equilibrium wall model](/methods/equilibrium-wall-model.md), Musker's
algebraic law $M(y^+)$ (page-local) inverted by Newton–Raphson for $u_\tau$,
held constant along the normal (§3.2, Eqs. 6–11):

- tangential velocity $u_A=u_\tau M(y_A^+)$, normal velocity linear to
  zero at the wall, $v_A=(y_A/y_B)v_B$;
- the SA working variable from $\nu_t=\kappa u_\tau y_AD$ with van Driest
  damping $D=1-\exp(-y_A^+/19)$ and $\kappa=0.41$, which the authors state
  valid "in the log layer and down to the wall", by solving
  $\tilde\nu_A^4-\nu_t\tilde\nu_A^3-\nu_t\nu^3c_{v1}^3=0$ (Eq. 8), the
  inversion of $\nu_t=\tilde\nu f_{v1}$ (*compiler check, not in the
  sources*: substituting $f_{v1}=\chi^3/(\chi^3+c_{v1}^3)$ gives this
  quartic);
- temperature by the Crocco–Busemann relation (adiabatic walls), density
  from the ideal gas, and **pressure $p_A=p_B$**, the constant
  wall-normal-pressure hypothesis.

The **modelling height** $H_{\mathrm{mod}}$ (page-local; it plays the role
of the matching height $h_{\mathrm{wm}}$) is the distance below which grid
points are target points rather than computed ones. In the authors' earlier
"F42" approach (Constant et al. 2021, as recalled) it is one global value
estimated from a flat-plate correlation and a user target $y^+_{\mathrm{target}}$
"ideally set between 50 and 500" for the first computed cells,
$$H_{\mathrm{mod}}=\sqrt2\,\frac{y^+_{\mathrm{target}}\,L}{Re\sqrt{f(Re)}},\qquad f(Re)=0.058\,Re^{-0.2}$$
(Eq. 5, $L$ the reference length); placing all forcing points below
$H_{\mathrm{mod}}$ removes the spurious near-wall oscillations of $C_p$ and
$C_f$ of the original IBM–wall-function coupling (§3.1, Fig. 6). Cai et
al. (2022) report such oscillations for wall models on immersed boundaries
too (next section), with a different remedy.

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

**Direct forcing for zero-thickness flexible blades (staggered finite
volume).** [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md), §2.3, couple
672 highly flexible ribbons of an aquatic canopy, each a Cosserat rod, to a
second-order finite-volume LES on a staggered Cartesian grid with the
direct-forcing IBM of Tschisgale & Fröhlich (as recalled): Lagrangian
markers carry the ribbon velocity, and the coupling force is interpolated
and spread with the three-dimensional smoothed delta function of Roma,
Peskin & Berger. The blades are thinner than the grid, so each rod element
is a zero-thickness quadrangle carrying markers at half the grid spacing
$\Delta_g=(\Delta x\Delta y\Delta z)^{1/3}$ (page-local), with marker area
about $(\Delta_g/2)^2$ and the condition $S_{ml}\Delta_g\le\Delta_g^3$
($S_{ml}$ the marker area, page-local); the
[Smagorinsky](/methods/smagorinsky-model.md) viscosity ($C_s=0.15$) is damped
near the blades with the same delta function. Because the blades are not
boundaries of the fluid domain, the double-averaged canopy force equals the
averaged IBM force exactly, so form and viscous drag cannot be separated
(§5.1, §5.3). The authors call DNS of the problem "not feasible" and their
LES "close to a DNS" (§3.2–3.3, App. C). [Rismondo et al. (2025)](/sources/rismondo-2025.md)
recall IBM-based LES of rotor wakes by Posa et al. but use body-fitted meshes.

**Direct forcing with Lagrangian markers (lattice Boltzmann).** In the
[ProLB](/software/prolb.md) set-up of Cheylan et al. (2023, §2.2, Eqs. 5–10)
the body surface carries Lagrangian markers $\boldsymbol X_k$, distinct from
the Eulerian lattice nodes $\boldsymbol x_j$. Each step (1) moves the
markers with the body, (2) advances the [lattice Boltzmann](/methods/lattice-boltzmann-method.md)
step without the body, giving a predicted velocity $\boldsymbol u^*$, (3)
interpolates $\rho$ and $\rho\boldsymbol u^*$ to the markers with a
regularized discrete delta kernel $\delta_h$ (page-local), (4) computes the
marker force $\boldsymbol F_k=\frac{2}{\Delta t}\big(I[\rho]\boldsymbol U^d-I[\rho\boldsymbol u^*]\big)$
that drives the interpolated velocity to the body velocity $\boldsymbol U^d$
(page-local $I[\cdot]$ the interpolation, Eq. 9), (5) spreads it back to the
nodes,
$$\boldsymbol f(\boldsymbol x_j)=\sum_k\boldsymbol F_k\,\delta_h(\boldsymbol x_j-\boldsymbol X_k)\,W_k\qquad(\text{Eq. 10, }W_k=\Delta S_k),$$
and (6) corrects the velocity and the populations with that body force
(Guo forcing, Eqs. 3–4). Three kernels are tested: a cosine kernel of
half-width 1.5, a four-point kernel and the three-point kernel of Roma et
al. (Eqs. 13–15). The authors state that the prediction step, which solves
the fluid without the solid first, regularizes the intermediate field and
reduces grid locking, so the kernel need not be chosen to suppress it
(§2.3).

**The Lagrangian weight.** $W_k$ is the volume of influence of a marker, which
"cannot be computed directly" because the marker set is a surface; setting
it to the cell volume has no justification (Cheylan et al. 2023, §2.4,
Eqs. 16–17). Requiring that spreading and then interpolating a constant
returns it (reciprocity) gives, in units of the cell volume, the linear
system
$$\sum_lA_{kl}W_l=1,\qquad A_{kl}=\sum_j\delta_h(\boldsymbol x_j-\boldsymbol X_k)\,\delta_h(\boldsymbol x_j-\boldsymbol X_l)$$
(Eqs. 18–21, after Pinelli et al. and Favier et al.; page-local $A_{kl}$),
solved by direct inversion or BiCGSTAB. Gsell et al.'s analytical
correction, as recalled, neglects curvature and keeps only the marker
itself, $W_k=1/\sum_j\delta_h(\boldsymbol x_j-\boldsymbol X_k)^2$ (Eq. 23).
Cheylan et al. propose a third form from a Taylor expansion of the
reciprocity condition about neighbouring markers, assuming a fine marker
spacing and a smooth field (no wall discontinuity):
$$W_l=\frac{1}{\sum_k\sum_j\delta_h(\boldsymbol x_j-\boldsymbol X_k)\,\delta_h(\boldsymbol x_j-\boldsymbol X_l)}\qquad(\text{Eq. 28}),$$
which needs no linear solve and, they state, accounts for curvature and is
usable whatever the solid/fluid size ratio and kernel (§2.4.2). It is the
reciprocal of the row sum of $A_{kl}$, i.e. exact for the linear system
when $W$ is uniform *(compiler check, not in the sources)*. On uniform grids
a single mean weight is used for all markers (§3.1.4, §3.2).

## Reynolds averaging of a volume-penalized flow

[Llorente (2024)](/sources/llorente-2024.md), a theoretical letter with no
computations, asks how the URANS equations should be penalized when a body
is represented by volume penalization. Page-local symbols: $\chi$ the mask
(1 in the body, 0 outside; registry $\chi$ is the Spalart–Allmaras ratio,
which does not occur here), $\eta_p$ the penalization parameter (the
source's $\eta$, called permeability; typical values $10^{-7}$ to
$10^{-10}$, citing Ménez et al.; it has the dimension of time in Eq. 2b,
*compiler check, not in the sources*), $\boldsymbol u_b$ the body velocity,
$u^{\mathrm{rel}}_i=u_i-u_{b,i}$ the relative velocity (the source's $w_i$,
renamed because $w_i$ are the registry's quadrature weights),
$\mathcal R=\chi/\eta_p$ the **fluid resistance** (inverse permeability; the
source's $\mathscr R_\eta$), $\mathcal T_c=\mathcal L/\mathcal U$ and
$\mathcal T_d=\mathcal L^2/\nu$ convective and diffusive times of
characteristic scales $\mathcal L$, $\mathcal U$. The source's overbar is
the Reynolds (ensemble) average, written $\langle\cdot\rangle$ here as in the
registry; its tilde is the Favre average, written $\langle\cdot\rangle_\rho$.

**Penalized equations.** The incompressible momentum equation carries the
source $s_i=\mathcal R\,(u_i-u_{b,i})$ (Eqs. 2a–2b), and, as the letter
cites from Angot, Bruneau & Fabrie, the penalized solution converges to the
no-slip one as $\eta_p\to0$ with error $\propto\eta_p^{1/2}$ for Dirichlet
conditions (p. 2). Articles on penalized turbulent flow, of which the
letter cites Yu & Yu (2022) as an example, add
$\chi\eta_p^{-1}(\langle u_i\rangle-\langle u_{b,i}\rangle)$ to the URANS
equations (p. 3, Eqs. 3–4).

**Time-scale condition.** Non-dimensionalizing and multiplying by
$\eta_p/\mathcal U$ shows the penalty dominating when
$\eta_p\ll\mathcal T_c\ll\mathcal T_d$ (Eq. 6), which the author identifies
with the intermediate damping regime of Hester, Vasil & Burns (2021).
Inside the body the mean velocity then obeys
$\partial_t\langle u_i\rangle+\langle u_i\rangle/\eta_p=\langle u_{b,i}\rangle/\eta_p$, whose solution,
expanded by repeated integration by parts, is
$$\langle u_i\rangle=\langle u_{b,i}\rangle+\sum_{k=1}^{\infty}(-1)^k\eta_p^k\Big[\frac{\partial^k\langle u_{b,i}\rangle}{\partial t^k}-\frac{\partial^k\langle u_{b,i}\rangle}{\partial t^k}\Big|_{t=0}e^{-t/\eta_p}\Big]\qquad(\text{Eq. 7c}),$$
an "artificial velocity" that vanishes only for a body at rest or in uniform
motion.

**Averaging the penalized equations.** Treating $\mathcal R$ as a fluid
property that fluctuates when the body moves, Reynolds averaging of the
penalty source gives
$$\langle s_i\rangle=\langle\mathcal R\rangle\langle u^{\mathrm{rel}}_i\rangle+\langle\mathcal R'u^{\mathrm{rel}\prime}_i\rangle\qquad(\text{Eq. 9c}),$$
with a resistance–velocity correlation that "arises because the body is
moving". Requiring $\langle u_i\rangle=\langle u_{b,i}\rangle$ in the body at all times closes
it as $\langle\mathcal R'u^{\mathrm{rel}\prime}_i\rangle=-\partial_t\langle u_{b,i}\rangle$ (Eq. 11),
so the closed URANS-VP momentum equation carries the extra source
$-\chi\,\partial_t\langle u_{b,i}\rangle$, minus the body acceleration
(Eqs. 12a–12d). For a fixed body the two procedures, penalizing URANS and
averaging the penalized Navier–Stokes equations, coincide. Theorem 1 bounds
the $L^2$ norm of the solution by that of the body velocity when
$\nu+\nu_t\ge0$, a continuous-level energy estimate (contrast the discrete
property of [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
Sketches extend the argument to a Neumann thermal condition imposed by
characteristics-based penalization and to compressible flow with Favre
averaging, where $\langle\rho\mathcal R'u^{\mathrm{rel}\prime\prime}_i\rangle=-\partial_t\big(\langle\rho\rangle\langle u_{b,i}\rangle_\rho\big)$
(pp. 9–10). The author concludes that deriving penalized turbulence
equations "without due care may lead to overlooking terms crucial for
accurately modelling turbulence in such penalized flows".

**Eddy-viscosity form as printed.** The letter writes the Reynolds stress as
$R_{ij}:=-\overline{u_i'u_j'}=\nu_t\,\partial\overline u_i/\partial x_j$ (p. 4,
overbar the Reynolds average), i.e. $\langle u_i'u_j'\rangle=-\nu_t\,\partial_j\langle u_i\rangle$
in registry notation: the opposite sign convention to the registry's
$R_{ij}=\langle u_i'u_j'\rangle$, the non-symmetric velocity gradient instead
of $2\langle S_{ij}\rangle$, and no $\tfrac23k\delta_{ij}$ term, so it is not
the [Boussinesq](/definitions/boussinesq-hypothesis.md) closure
$R_{ij}-\tfrac23k\delta_{ij}=-2\nu_t\langle S_{ij}\rangle$. In Theorem 1 it
enters only through the sign of the total viscosity $\nu+\nu_t$.

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

- **Direct-forcing guidelines** (Cheylan et al. 2023, §3.1–3.2, Tables
  2–11; laminar cylinder at $Re=100$ and Poiseuille channel): the three
  weights give velocity profiles within 1% of each other, with boundary slip
  errors $10^{-4}$ (Eq. 28), $5\times10^{-5}$ (BiCGSTAB) and $10^{-5}$
  (inversion) at relative costs 1, 1.6 and 2.25; the slip error scales with
  the Courant number $U_0\Delta t/h$; narrower kernels are better ("a
  flatter function gives a bigger error"); a marker spacing between 0.8 and
  1.2 grid spacings is recommended, too many markers making the weighted
  run crash below about 0.785 grid spacings (two near-identical rows of
  $A_{kl}$), too few letting fluid leak; applying the weight lowers the
  cylinder drag error from 0.066 to 0.037 and the channel mass-flow error by
  about three times. The weight corrects the slip but not the wall velocity
  gradient, which the regularized kernels diffuse, so the near-wall solution
  is first order in grid size while the far field is insensitive (§3.2).

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

## Local modelling height and wall-pressure reconstruction

Constant et al. (2024) identify two failures of a single global
$H_{\mathrm{mod}}$ at strong incidence and correct both outside the solver.

**Modelling-height adaptation.** On the
[NACA 0012](/benchmarks/naca-0012-airfoil.md) at $M=0.15$, $Re_c=6\times10^6$,
the flat-plate estimate holds at zero incidence, but on the suction side at
high incidence the image-point $y^+$ departs strongly from
$y^+_{\mathrm{target}}$: for $y^+_{\mathrm{target}}=300$ the leading-edge
maximum is "close to 300%" above it at $15^\circ$ (§4.1, Fig. 10), so the
wall function is applied where the boundary layer is thin and not yet in
equilibrium. After a converged run, the stored $y^+$ is used to convert
target points into computed points wherever the $y^+$ one layer below,
estimated as $y^+_{n-1}\approx y^+_n(1-h/y_n)$ for a mesh aligned with the
wall (Eq. 19), still exceeds $y^+_{\mathrm{target}}$; the first two target
rows are never changed (§4.2, Fig. 11). Only the interpolation data are
recomputed (no mesh change, no new wall distance) and the run restarts warm;
the authors contrast this static single-pass update with the dynamic
relocation of forcing points of Xu & Liu (as recalled, §4.2). At $15^\circ$
($y^+_{\mathrm{target}}=100$) it lowers the maximum suction-side image-point
$y^+$ from 435 to 243 (§6.1, Fig. 18). For the first 10% of the chord the
equilibrium law still cannot represent the velocity profile; beyond it the
log region is established (§6.1, Figs. 19–21). On the two-dimensional
multi-element airfoil a warm restart costs about a third of the initial
run, and the non-adapted run on the finest mesh needs four times the
iterations of the coarsest (§6.2, Fig. 28).

**Wall pressure from a second image layer.** The default wall pressure is
the zeroth-order $p_w=p_{B_1}$ (Eq. 21). Pressure gradients at the first
image points oscillate strongly, especially at the leading edge, while at a
**second layer of image points**, placed at $H_{\mathrm{mod}}+\epsilon$ with
$\epsilon=2\sqrt{d_s}\,h$ ($d_s$ the space dimension, page-local; Eq. 20),
they are smooth without filtering (§6.1, Fig. 22). The wall pressure is then
extrapolated along the normal $\boldsymbol n$ to first or second order,
$$p_w=p_{B_2}-\partial_np\big|_{B_2}\,\lvert WB_2\rvert+\tfrac12\,\partial_{nn}p\big|_{B_2}\,\lvert WB_2\rvert^2$$
(Eqs. 22–25; the first-order form drops the last term), the derivatives
computed with the solver's gradient operator, applied twice for the second
derivative. The reconstruction acts only in post-processing: refining the
IBM mesh at fixed $y^+_{\mathrm{target}}=100$ divides by four the distance
over which the zero-normal-gradient assumption acts yet changes the error
little, which the authors read as evidence that correcting the pressure at
the target points during the run would gain little (§5.1, Figs. 12–13).
They agree with Cai et al. (2021, as recalled) that far-field integration
of the drag beats near-field integration on immersed boundaries, but locate
the near-field error in the post-processed wall pressure, not in the field
solution (§5.1).

**Effect on forces.** NACA 0012 at $15^\circ$ against a body-fitted
wall-resolved RANS ($C_D=20.85\times10^{-3}$, $C_L=1.516$): global
$H_{\mathrm{mod}}$ with zeroth-order pressure gives $C_D=40.44\times10^{-3}$
(94% error), adaptation alone $30.57\times10^{-3}$ (47%), adaptation and
second-order pressure $24.51\times10^{-3}$ (17%) with $C_L=1.476$ (2.6%)
(Table 3). Friction drag stays close to the reference; the error is pressure
drag, and with first- or second-order reconstruction near-field and
far-field drag agree (§6.1, Fig. 25). The residual ≈20% at $15^\circ$ is
attributed to the equilibrium wall model at the leading edge and to the
sensitivity of the case (§6.1). On the multi-element airfoil ($M=0.2$,
$Re=5\times10^6$, $16^\circ$) the adapted second-order drag error falls with
the mesh, 42%, 27%, 23%, 22% against a body-fitted FUN3D solution
(Table 6), and the authors conclude that both corrections are needed
whatever the resolution (§6.2). On the
[NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
($M=0.2$, $Re=5.49\times10^6$ on the mean aerodynamic chord,
$17.05^\circ$; 2.4 billion Cartesian cells with $y^+_{\mathrm{target}}=500$,
built in under seven hours from the surface mesh alone) the drag error
falls from 9.1% to 1.5% and the lift error from 13% to 8.4% against a
550-million-cell body-fitted LAVA solution (§6.3, Tables 8–9). The authors
name a non-equilibrium (pressure-gradient-aware) wall model and a hybrid
RANS/LES extension as the next steps (§7).

## The lattice Boltzmann host solver

ProLB (see also [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)), as summarized by Cai et al. (2022, §II.A): D3Q19 lattice, a
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

## Turbulent fluid–structure interaction

Cheylan et al. (2023, §2.5–2.7, §3.3–3.4) couple the direct-forcing IBM in
ProLB with the finite-element structural solver Calculix through an
explicit staggered scheme: each step the fluid sends marker forces and the
structure returns marker displacements, with a second-order
Hilber–Hughes–Taylor predictor–corrector for the structure. On a
three-dimensional flapping flag ($Re=200$, mass ratio 1) the force
histories agree better with the literature with the weight than without
(stated as a 20% error reduction in the abstract and 20–30% in the
conclusions; no number in §3.3 backs it). On an elastic beam behind a fixed
cylinder at $Re=10^4$ with solid-to-fluid density ratio 1, an LES with the
shear-improved [Smagorinsky](/methods/smagorinsky-model.md) model of
Lévêque et al., coupled to the lattice Boltzmann relaxation time, gives
Strouhal numbers 0.185 and 0.101 against 0.175 and 0.103 of Breuer et al.;
the second-order structural prediction gives a less noisy lift spectrum
than a first-order one (Table 13, Fig. 19). The authors state that LES is
"not well established in the FSI context" and that the IBM avoids the
grid-motion equation of an arbitrary Lagrangian–Eulerian method (§1).

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

Mozaffari et al. (2024, §3.3, Figs. 16–24, Table 3) revisit the case in
the same solver with $k$-$\omega$ SST-based hybrids (IDDES and continuous
eddy simulation, see [hybrid RANS/LES](/definitions/hybrid-rans-les.md))
instead of LES, on a $45.8\times10^6$-node octree grid with
$\Delta x_{\min}=1.3$ mm, and the explicit equilibrium wall model of Cai &
Sagaut (no pressure-gradient term). With the wall model on the body
**neither hybrid separates on the slant**, at $25^\circ$ or $35^\circ$,
which the authors attribute to the equilibrium wall model in a mild adverse
pressure gradient and to the missing instability that would switch the
hybrid to LES mode. With a zero-velocity Dirichlet condition instead
(although $y^+\approx100$–150 on the slant) the flow separates; IDDES then
reproduces the $35^\circ$ wake topology with $C_D=0.2819$ against
0.2580–0.32 in the experiments listed, while continuous eddy simulation
separates already on the roof ($C_D=0.3779$); at $25^\circ$ IDDES separates
late and does not reattach, attributed to $y^+\approx100$–150 on the slant. See
[Ahmed body](/benchmarks/ahmed-body.md).

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
- Vicente Cruz & Lamballais (2023), Cai et al. (2022) and Cheylan et al.
  (2023) all report that the immersed treatment degrades the near-wall
  solution (residual wall velocity; lost Reynolds stress; slip error and a
  diffused wall gradient, first order near the wall); the three concern
  different methods and are not compared.
- Cheylan et al. (2023) contradict, by their own account, the conclusion
  of Zhou & Balachandar that the weight has little effect on the Eulerian
  force (§3.1.4–3.1.5); the earlier work is not ingested here.
- **Recommended marker spacing.** Cheylan et al. recommend 0.8 to 1.2 grid
  spacings (§3.1.5), while their best cylinder cases (15 and 20, Table 9)
  use $0.00628/0.005=0.01256/0.01=1.256$ *(compiler check, not in the
  sources)*; Table 8 shows a crash at 0.785 itself, the text a limit
  "below 0.785".
- **Wall model or no-slip on the Ahmed slant.** Cai et al. (2022) find
  that, on their fine grid, the wall law with the near-wall stress
  enhancement outperforms a no-slip condition on slant and base, while
  Mozaffari et al. (2024) find that the equilibrium wall model suppresses
  slant separation and a no-slip condition restores the observed topology.
  The finest spacings coincide ($4.5\times10^{-3}H$ with $H=288$ mm is
  1.3 mm, *compiler check, not in the sources*), but the turbulence
  treatments and wall laws differ (Vreman LES with a constrained-LES
  near-wall viscosity and stress enhancement against SST-based IDDES with
  the explicit Cai & Sagaut law), so the two findings concern different
  set-ups, and neither source runs the other's. Both agree that the coarse or
  wall-model-dominated runs fail to separate (Cai et al. 2022, coarse grid;
  Mozaffari et al. 2024, §3.3).
- **Constant normal pressure.** Constant et al. (2024, §1) state that most
  recent IBM work for high-Reynolds-number flow assumes constant pressure
  across the whole modelled boundary layer, which "can ultimately lead to
  significant errors" in direct force integration.
- **Printed slips (Constant et al.).** §3.1 defines the flat-plate height
  $y_0$ as that of a first cell "for which $y^+=0$"; Eq. 5 is the height
  for $y^+=1$ times $y^+_{\mathrm{target}}$ (with $C_f=f(Re)$ and
  $u_\tau=U\sqrt{f/2}$, *compiler check, not in the sources*). §3.2
  calls $u=\boldsymbol u\cdot\boldsymbol t$ and $v=\boldsymbol u\cdot\boldsymbol n$
  "the normal and tangential components", in swapped order. Table 3 prints
  a lift error of 5.6% for the global-height case, while its own values
  give $(1.516-1.416)/1.516=6.6\%$ *(compiler check, not in the sources)*.
- **Closure by requirement (Llorente 2024).** The correlation
  $\langle\mathcal R'u^{\mathrm{rel}\prime}_i\rangle$ is called one that "cannot … be closed, like
  for the Reynolds stress tensor" (p. 6) and is then closed exactly by
  requiring perfect penalization in the body, which the letter's own
  Eq. (7c) shows does not hold for finite $\eta_p$; Theorem 1 uses the same
  assumption ($\langle u^{\mathrm{rel}}_i\rangle=0$ in the body). The result is a kinematic body
  acceleration forcing, independent of turbulence. Printed slips: the final
  energy identity of Theorem 1 lacks the time integral that Eq. (13)
  carries; the dissipation integral is called "negative semi-definite"
  although it is non-negative for $\nu+\nu_t\ge0$; the diffusive flux of
  the penalized heat equation is printed with a $+$ sign that makes it
  anti-diffusive *(compiler check, not in the sources)*. The version read
  is the author accepted manuscript.
- **Printed slips (Cheylan et al.).** Eq. (12) raises the kernel to the
  power $k$ in the moment condition; the beam case prints a solid density
  of $10^4$ kg/m³ with a fluid density of $10^3$ kg/m³ and a density ratio
  of 1, and a time step of $1.15\times10^4$ s (Table 12); Eq. (40) calls a
  profile linear in $r$ parabolic.

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §II.A, Eqs. (1)–(15) (lattice Boltzmann, HRR collision, Vreman model); §II.B.1, Eqs. (16)–(20) (boundary-point reconstruction); §II.C.1, Eqs. (24)–(27), Fig. 1 (wall model on the IBM, constrained LES); §III, Tables I–II, Eq. (28); §IV, Table III, Figs. 4–9 (Ahmed body).
- [Placco et al. (2023)](/sources/placco-2023.md) — §2 (ghost-point-forcing IBM in STREAmS); §3 (grid).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.7, Eqs. (27)–(29), Fig. 14 (volume penalization, ray tracing, wind turbine).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1; §3, footnote 6 (reconstruction inside the solid, soft no-slip); §7.1, Fig. 24 (pipe DNS and LES).
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §1; §2.1–2.4, Eqs. (1)–(28) (lattice Boltzmann host, direct forcing, kernels, Lagrangian weight); §2.5–2.7, Eqs. (29)–(38) (structural scheme, coupling, LES); §3.1–3.2, Tables 2–11 (cylinder, Poiseuille); §3.3–3.4, Tables 12–13, Figs. 12–19 (flag, beam); §4.
- [Constant et al. (2024)](/sources/constant-2024.md) — HAL author manuscript hal-04731107v1: §1; §3, Eqs. (5)–(11), Figs. 3, 6 (ghost-cell direct forcing, modelling height, Musker wall function); §4.1–4.2, Eq. (19), Figs. 10–11 (adaptation); §5.1–5.2, Eqs. (20)–(25), Figs. 12–15 (second image layer, wall-pressure reconstruction); §6.1–6.3, Tables 3, 6, 8–9, Figs. 18–28 (NACA 0012, 2DMEA, HL-CRM); §7.
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1, Eqs. (2.1)–(2.2) (mass source and momentum forcing, discretization); §4.2.1, Fig. 9 (QUICK near the cylinder front).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — HAL accepted manuscript hal-04921212v1: §2.2, Fig. 1 (reference-point reconstruction with a wall model); §3.3, Figs. 16–24, Table 3 (Ahmed body, wall model against no-slip).
- [Llorente (2024)](/sources/llorente-2024.md) — author accepted manuscript: pp. 2–4, Eqs. (1)–(6) (penalized and conventionally penalized URANS equations, time-scale condition); p. 5, Eq. (7) (artificial velocity); pp. 6–8, Eqs. (8)–(12) (fluid resistance, averaged source, closure, closed system); pp. 8–10, Theorem 1, thermal and compressible extensions.
- [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §2.3 (direct-forcing IBM for flexible ribbons, Roma kernel, marker condition); §3.2–3.3; §5.1, §5.3 (canopy force equals the averaged IBM force); App. C.
- [Rismondo et al. (2025)](/sources/rismondo-2025.md) — introduction (IBM-based LES of rotor wakes by Posa et al. recalled; body-fitted meshes used).
