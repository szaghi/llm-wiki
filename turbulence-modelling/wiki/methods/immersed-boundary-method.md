---
type: Method
title: "Immersed boundary methods"
description: "Immersed boundary methods impose walls on non-conforming grids by reconstruction, ghost points, volume penalization, direct forcing or weak variational enforcement; this page covers DNS, LES and RANS variants, stiff penalization, the Lagrangian weight, wall functions and wall-stress fluxes, moving grids, volume filtering with wall-slip models, Reynolds averaging of penalized flows, and near-wall errors."
status: established
aliases: [IBM, moving Cartesian grid, volume penalization immersed boundary method, VP-IBM, fluid resistance, immersed boundary, ghost-point forcing, volume penalization, Brinkman penalization, IB wall model, direct-forcing immersed boundary, Lagrangian weight, modelling height, ghost-cell direct forcing, volume-filtering immersed boundary method, VMIB, variational multiscale immersed boundary, weak Dirichlet immersed boundary, single ghost cell, IBMLES, immersed boundary-modelled LES, wall-slip model, slip-length model]
tags: [immersed-boundary, wall-model, lattice-boltzmann, les, dns, rans]
timestamp: 2026-10-28T01:53:00Z
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
Boltzmann code ([Mozaffari et al. 2024](/sources/mozaffari-2024.md);
[Husson et al. 2024](/sources/husson-2024.md)) and
steady wall-function RANS of high-lift aircraft on octree Cartesian grids
([Constant et al. 2024](/sources/constant-2024.md)) and two wall-modelled
LES submissions of a high-lift workshop
([Kiris et al. 2023](/sources/kiris-2023.md)), RANS and DDES of
pitching airfoils and a hovering rotor on Cartesian grids that move
rigidly with the body ([Sugaya & Imamura 2021](/sources/sugaya-2021.md)), DNS of a heated
rough-wall channel in a spectral difference code
([D'Ayer et al. 2026](/sources/dayer-2026.md)), and an a priori
volume-filtering framework for wall-modelled LES in which the wall slip is
the modelled quantity ([Rickard & Kasbaoui 2026](/sources/rickard-2026.md)),
variational multiscale LES with weakly imposed no-slip on finite elements
([Kang & Masud 2022](/sources/kang-2022.md)), and wall-modelled LES of
hypersonic boundary layers and shock interactions on a Cartesian
finite-difference solver ([van Noordt et al. 2022](/sources/vannoordt-2022.md)), and
wall-modelled LES of wind-turbine wakes over two-dimensional hills on a
pseudo-spectral grid ([Zhang et al. 2022e](/sources/zhang-2022-i.md)). Three
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
With volume penalization in a high-order code, D'Ayer et al. (2026)
report wall-vorticity oscillations confined to cells that the body cuts.
Kang & Masud (2022, §5.2) attribute a slight overestimate of the velocity
fluctuations in a sphere wake to "slight slipping" of the fluid at the
weakly enforced wall, and van Noordt et al. (2022, §4) find the wall heat
transfer very sensitive to the artificial dissipation added at the
immersed boundary.
Rickard & Kasbaoui (2026, §1) state, citing earlier work, that IB forcing
on non-uniform grids can produce spurious stress oscillations that corrupt
the near-wall eddy viscosity, and cite Verzicco (2023) as suggesting that
IBs in LES may only be possible on uniform grids with IB-adapted wall
models.

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

**Sharp-interface direct forcing at fluid-side nodes (lattice
Boltzmann, RANS and hybrid RANS/LES).** Husson et al. (2024, §3.2, Fig. 2,
Eqs. 40–43) use, in a development branch of ProLB, the method of their
earlier work, which they cite and classify after Kang & Hassan as
direct forcing with a sharp interface. The forcing nodes are the fluid
nodes next to the wall, and all their populations are overwritten by the
equilibrium plus the regularized non-equilibrium part built from the
reconstructed density, velocity and strain rate (Eq. 40). Through each
forcing node an interpolation point is placed along the wall normal at the
fixed distance $d_{\mathrm{IP}}=2.5\Delta y$ (page-local), "to limit local
scheme staggering, avoiding low-noise streamwise pressure oscillations";
density and velocity there come from weighted least squares over the eight
surrounding nodes. Each step (1) interpolates at the interpolation point,
(2) inverts the wall law there by Newton–Raphson for $u_\tau$, (3) sets the
forcing-node tangential velocity from the linearized law below (with
$y_c=d_{\mathrm{IP}}$), its density equal to the interpolated one, its
normal velocity by linear extrapolation and the Spalart–Allmaras variable
to $\chi=\kappa y^+$, (4) computes velocity gradients (second-order centred
where possible, first-order one-sided otherwise, after Degrigny et al.) and
overwrites the wall-normal gradient of the tangential velocity, in the
wall frame, by its analytical value, and (5) rebuilds the populations.
Step 4 is the gradient correction that Cai et al. (2022) also apply (see
the section on wall models on immersed boundaries below).
On a flat plate inclined to the lattice the forcing nodes form a
staircase and the wall normal is not lattice-aligned, which the authors
note makes wall-normal-gradient sensors harder to evaluate; the hybrid
RANS/LES shielding still holds there (§4.1.2, Fig. 5).

**Terrain in a pseudo-spectral LES (cited, not detailed).** Zhang et al.
(2022e, §II A) represent two-dimensional $\cos^2$ hills (height 40 and
20 mm, slopes 0.4 and 0.2) in the [LESGO](/software/lesgo.md) solver,
pseudo-spectral in the horizontal directions, by the immersed boundary
method of Chester, Meneveau & Parlange, which they cite, so that the
Cartesian grid is left unchanged; the forcing and the wall treatment on
the immersed terrain are not described. The flat bottom carries a
rough-wall log-law stress computed from the velocity at the first grid
point averaged by a filter twice the grid filter. On the steep hill the
LES agrees overall with the wind-tunnel mean velocity of Cao & Tamura,
including the reverse flow, but underpredicts the streamwise turbulence
intensity in the lower hill wake at the downwind foot, which the authors
attribute, citing Yang et al., to the classical (equilibrium) wall model
in recirculating flow (§III A, Fig. 4); the grid study of App. A
($192\times64\times97$ chosen) settles the bare-hill turbulence intensity
from the second of four grids on. The rotor is an
[actuator disk](/methods/actuator-line-model.md).
[Stanly et al. (2022)](/sources/stanly-2022.md), whose solver MIRACLES
carries an immersed boundary method in its name, model the turbine tower
as an actuator line instead and name an immersed-boundary tower as future
work (§2.1, §2.3, §6).

**Mass source and momentum forcing (staggered finite volume).**
Kim et al. (2024, §2.1, Eqs. 2.1–2.2) use the immersed boundary method of
Kim, Kim & Choi (2001), which they cite and which adds a mass source/sink $q$ to
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
direct-forcing method of Péron et al., which they cite, in ONERA's FastS
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
"F42" approach (Constant et al. 2021, which they cite) it is one global value
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
Placco et al. cite them; no equations printed).

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

**Volume penalization with an exactly integrated stiff source (spectral
difference).** D'Ayer et al. (2026, §2.2–2.4) implement Brinkman volume
penalization in JAGUAR, the CERFACS–ONERA compressible
[spectral difference](/methods/spectral-difference-method.md) solver, on
hexahedra (solution points at first-kind Chebyshev nodes, flux points at
the two cell ends and the $N-1$ interior Legendre–Gauss points, Roe flux,
BR1 gradients, five-stage fourth-order SSP Runge–Kutta). Page-local:
$\boldsymbol U=(\rho,\rho\boldsymbol u,\rho e)$ the conservative state with
$e=E/\rho$ the total energy per unit mass, $\boldsymbol F_c$, $\boldsymbol F_v$
the convective and viscous fluxes, $\Omega$ the solid, $\chi$ and $\eta_p$
the mask and permeability as above, $\boldsymbol s_p$ the penalization source. The system
$\partial_t\boldsymbol U+\nabla\cdot(\boldsymbol F_c-\boldsymbol F_v)+\boldsymbol s_p=0$
carries
$$\boldsymbol s_p=-\frac{\chi}{\eta_p}\big(0,\ \rho\boldsymbol u_\Omega-\rho\boldsymbol u,\ \rho e_\Omega-\rho e\big)$$
(Eqs. 12–13, 16), with target velocity $\boldsymbol u_\Omega=0$ and target
energy $e_\Omega=c_vT_\Omega$ ($c_v$ the specific heat at constant volume,
page-local) for an isothermal wall. Density is not penalized, only
Dirichlet conditions can be imposed, and the authors call this form
"adapted for flow at subsonic Mach numbers" (§2.3). Where the HORSES3D
source of Ferrer et al. drives the energy towards the kinetic energy of the
body velocity, this one relaxes the total energy to the internal energy of
the wall temperature, a convention difference between the two
implementations.

The source is stiff as $\eta_p\to0$. D'Ayer et al. (§2.4) cite explicit
stability limits $\Delta t_{\max}=\eta_p$ for a pseudo-spectral scheme with
second-order Adams–Bashforth (Kolomenskiy & Schneider) and
$\Delta t_{\max}=\tfrac{6}{11}\eta_p$ with third-order Adams–Bashforth
(Jause-Labert). Their remedy is a two-part Strang
splitting: a half step of the penalization sub-problem, a full step of the
unchanged spectral-difference Runge–Kutta update, and a second half step,
the penalization sub-problems being integrated exactly,
$$\boldsymbol U(t)=\chi\big[(1-r_p)\mathsf A\boldsymbol U_\Omega+r_p\mathsf B\boldsymbol U_0\big]+(1-\chi)\boldsymbol U_0,\qquad r_p=e^{-t/\eta_p},$$
at $t=\Delta t/2$ (Eqs. 18–23; page-local $\boldsymbol U_0$ the sub-step
initial state, $\boldsymbol U_\Omega=(\rho,\rho\boldsymbol u_\Omega,\rho e_\Omega)$,
$\mathsf A=\mathrm{diag}(0,\boldsymbol I,1)$, $\mathsf B=\mathrm{diag}(1,\boldsymbol I,1)$).
The splitting error is printed as $O(\Delta t^3)$ (Eq. 21, citing Strang).
The authors state that this "makes possible the use of any value of
$\eta$ without limiting the time step", fix $\eta_p=10^{-10}$ s in every run,
leave $\Delta t$ to the CFL condition, and state that the exact sub-steps do
not increase the cost (no timings given). They also state (Eq. 15, citing
Engels et al.) that the total error splits into the modelling error of the
penalized problem and its discretization error, which can depend on
$\eta_p$, so lowering $\eta_p$ need not lower the total error; $\eta_p$ is not
varied in the paper. The drag follows from the volume integral of the
penalization term, $C_D=\big(\tfrac12\rho_\infty u_\infty^2D\big)^{-1}\int_\Omega(\rho/\eta_p)(\boldsymbol u_\Omega-\boldsymbol u)\,dV$
in its streamwise component (Eq. 26), and wall data by inverse-distance
weighting at interpolation points, as in the flux-reconstruction
penalization of Kou et al. (2022), which they cite. Citing Mittal & Iaccarino,
the authors call continuous IBMs such as penalization "usually restricted
to first-order accuracy near the boundary" (§1); they report no
order-of-accuracy study.

**Direct forcing for zero-thickness flexible blades (staggered finite
volume).** [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md), §2.3, couple
672 highly flexible ribbons of an aquatic canopy, each a Cosserat rod, to a
second-order finite-volume LES on a staggered Cartesian grid with the
direct-forcing IBM of Tschisgale & Fröhlich, which they cite: Lagrangian
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
cite IBM-based LES of rotor wakes by Posa et al. but use body-fitted meshes.

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
correction, as Cheylan et al. cite it, neglects curvature and keeps only the marker
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

**Weak Dirichlet enforcement by variational multiscale analysis (finite
elements).** [Kang & Masud (2022)](/sources/kang-2022.md), §2–4, impose
the no-slip condition weakly on a surface immersed in a fixed linear
hexahedral or tetrahedral finite-element mesh (the variational multiscale
immersed boundary, VMIB). They start from a mixed weak form in which a
Lagrange multiplier $\boldsymbol\lambda_I$ (page-local) enforces
$\boldsymbol u=\boldsymbol g$ on the immersed surface $\Gamma_I$, split
the velocity into resolved and unresolved parts,
$\boldsymbol u=\boldsymbol u^>+\boldsymbol u^<$, and solve the unresolved
problem locally in the band of cut elements with an "interfacial bubble"
that peaks on the cut facet, keeping the generalized-$\alpha$ time
discretization and the inertia of the unresolved scales inside it (their
laminar predecessor dropped that inertia). Three results follow (§3.2):

- a closed-form, element-wise stabilization tensor $\mathsf T_I$
  (page-local) that depends on the fluid properties, the linearized
  Navier–Stokes operator, the time-integrator parameters and the cut-cell
  geometry (the fluid volume and facet area of each cut element), so the
  method has no user-chosen penalty parameter (Eqs. 32–34);
- an analytical $\boldsymbol\lambda_I$, the wall traction plus a
  stabilization term, which removes the multiplier as an unknown (Eq. 36);
- the unresolved velocity on $\Gamma_I$,
  $\boldsymbol u^<=-(\boldsymbol u^>-\boldsymbol g)$ (Eq. 37), the error of
  the no-slip enforcement, which the authors use as an element-wise
  a posteriori error indicator (Eq. 64).

Substituted into the resolved problem, the interface terms are, in order,
consistency, adjoint consistency, mass conservation and stabilization
(Eq. 41); the authors set them side by side with CutFEM and
immersogeometric analysis, whose penalty parameters are chosen by
guidelines rather than derived (Table 1). A ghost-penalty-type term
adapted from a level-set stabilization is added (Eq. 48), and turbulence
is closed by the residual-based
[variational multiscale](/methods/variational-multiscale-method.md) LES
model (§3.4). Two lemmas state that the unresolved interface velocity
tends to its previous value as $\Delta t\to0$ and that the stabilization
stays bounded by a positive-definite tensor in that limit, so it does not
vanish at small time steps (Eqs. 28–29, 43–44). The surface is an STL
triangulation independent of the mesh; cut elements are found by
triangle–triangle overlap tests, the others classified by ray tracing,
fully fictitious elements removed, and cut elements integrated on
adaptive sub-cells (§4, Box 2). $\lVert\mathsf T_I\rVert$ grows for small
cut facets, between 1 and 1000 on the cylinder (Figs. 14–15). Applications
are the [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) at
$Re_D=3900$, a sphere at $Re_D=10^4$ and a 1:10 high-speed train at
$Re=7.2\times10^5$ on the train width; the no-slip error stays within 3%
of the inflow velocity on the cylinder and the sphere and 1% on the train
(Figs. 16, 29, 35). On the sphere, $C_D=0.410$ and 0.405,
$-C_{pb}=0.288$ and 0.305 and separation angles of $86.0^\circ$ and
$86.3^\circ$ at $\Delta t=0.01$ and 0.0025, against 0.402, 0.272,
$84.7^\circ$ for the DNS of Rodríguez et al. as reported (Table 5).

**Ghost-cell method with a single ghost cell (high-order finite
differences, hypersonic WMLES).** [van Noordt et al. (2022)](/sources/vannoordt-2022.md)
build a sharp ghost-cell IBM in CHAMPS, a Cartesian finite-difference
solver with block-structured octree refinement, for
[wall-modelled LES](/methods/wall-modelled-les.md) of compressible and
hypersonic flows, which they state is, to their knowledge, the first
published hypersonic turbulent simulation combining WMLES and an IBM
(§1). The convective flux blends a fourth-order kinetic-energy- and
entropy-preserving centred flux (Kuya et al.; see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md))
with a third-order WENO flux-vector-splitting flux,
$\hat f=(1-\sigma_b)\hat f_{\mathrm{cent}}+\sigma_b\hat f_{\mathrm{WENO}}$
($\sigma_b$ the registry's upwind fraction; Eq. 8), with prescribed
$\sigma_b$ in the first three irregular cells (§2.3). Its numerical
choices at the wall are:

- *one ghost cell only.* The second ghost layer "introduces large numerical
  errors as it is essentially extrapolated", so new two-candidate WENO
  boundary stencils are derived, one deliberately downwind-biased
  (Eqs. 21–24); a run with two ghost cells "does not yield accurate
  results" (§3.2, Fig. 16). The face values are third order, the flux
  derivative at the first irregular point second order (§2.3, §2.7);
- *a stability-chosen boundary stencil.* The free parameter of the
  downwind-biased stencil is set from the spectra and
  $\varepsilon$-pseudospectra of the RK4-discretized advection operator
  (§2.8, Figs. 8–10);
- *least-squares viscous stencils* at irregular faces that match the
  interior order and leading truncation-error coefficients, with the
  wall-adjacent derivative solved by a pseudo-inverse to remove the
  singularity as the wall distance vanishes (§2.4, Eqs. 29–31);
- *two-point ray sampling.* Rays from the centroids of the surface
  triangles carry two sampling points, one at a fixed number of grid
  spacings and one at a fixed distance in outer units (also the wall-model
  exchange point); ghost values come from third-order least-squares
  interpolation, surface reconstruction and a second-order extrapolation
  (zero-gradient pressure, mirrored normal velocity, linearly extrapolated
  tangential velocity; §2.6, Algorithm 1, Eqs. 41–42). The fixed-distance
  projection bypasses the small-cell problem.

Manufactured solutions on a unit sphere give interpolation orders
$L_2$/$L_\infty$ of 2.30–3.00, ghost-cell filling 2.84–2.96 ($L_2$) and
1.86–1.99 ($L_\infty$), and convective and viscous operators of second order
at the boundary (Tables 1–2; see
[method of manufactured solutions](/methods/method-of-manufactured-solutions.md)).
The wall model and the validation are in the next section.

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
- **Penalization at high order** (D'Ayer et al. 2026, §3, Tables 1–3). On
  the steady [cylinder](/benchmarks/circular-cylinder-wake.md) at $Re_D=40$,
  $M=0.2$, $N=2$ (body-fitted mesh 182k cells and 1.63M solution points,
  IBM mesh 263k cells and 2.37M points, near-wall cell size $0.01D$), the
  body-fitted and penalized runs give recirculation length $2.27D$ and
  $2.25D$, separation angle $52.2^\circ$ and $52.1^\circ$, drag coefficient
  1.55 and 1.54, against 2.27, $52.0^\circ$, 1.52 of Kou et al. (2022) and of
  Choi et al., which they cite: differences below 1%. Wall $C_p$ agrees; the
  wall vorticity oscillates near the surface, which the authors attribute
  to cells partly inside the body, where a polynomial cannot represent the
  discontinuous solution (a Runge phenomenon), and they find the penalized
  run more sensitive to mesh resolution than the body-fitted one (study not
  shown); they avoid local refinement to limit cost and propose automatic
  $hp$-refinement near the interface as future work (§4). In the
  [turbulent channel](/benchmarks/turbulent-channel-flow.md) at
  $Re_\tau=400$ over staggered hemispheres of height $k_r=\delta/20$ (page-local; Wu et
  al.'s RH400-20-4 geometry, which they cite), heated by a volumetric source
  with isothermal walls, cropped to a minimal channel of
  $L_x^+\approx1009$, $L_z^+\approx240$ (as printed), with $N=3$, the
  penalized DNS (25M degrees of freedom, $\Delta x^+=1.73$,
  $\Delta z^+=1.50$, $\Delta y^+_0=0.51$) is compared with a body-fitted
  JAGUAR run (17M), a body-fitted finite-volume AVBP run (14M, the thermal
  reference) and the DNS of Wu et al. (859M): mean velocity and temperature
  agree below the minimal-channel critical height $y^+_c=0.4L_z^+$, and the
  Reynolds stresses and turbulent heat fluxes agree within about 5%, the
  over-predicted $\langle v'v'\rangle^+$ and under-predicted
  $\langle w'w'\rangle^+$ being common to all minimal-channel runs (§3.2,
  Figs. 7–10). They argue that in the fully rough regime the drag increase
  is mainly pressure drag, so the near-wall gradient errors of the IBM,
  which affect viscous drag, should not spoil the roughness effect (§3.1).

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

**Linearized wall law below the interpolation point.** Husson et al.
(2024, §3.1, Eqs. 37–39) impose the analytical Spalart–Allmaras wall law
of Allmaras & Johnson, which they cite and call consistent with the
buffer layer of the Spalart–Allmaras model (its nine constants printed to
16 digits; see [law of the wall](/definitions/law-of-the-wall.md)), and
linearize it below a cut-off $y_c$ citing Tamaki et al.,
$u^+(y^+)=u^+(y_c^+)-(y_c^+-y^+)\,\mathrm du^+/\mathrm dy^+(y_c^+)$. The
motivation is that on coarse grids the steep near-wall gradients of the
law cannot be captured and cause oscillations and wrong $C_f$; removing the
nodes nearest the wall by a distance threshold, as others do, leaves too
few nodes in thin layers. The momentum deficit of the linear profile is
offset by a constant eddy viscosity below $y_c$, obtained by replacing, for
$d<y_c$, the damping function by
$f'_{v1}=r_{\mathrm{lin}}(\chi r_{\mathrm{lin}})^3/\big(c_{v1}^3+(\chi r_{\mathrm{lin}})^3\big)$,
$r_{\mathrm{lin}}=y_c/d$ (page-local). The authors state that both the
immersed treatment and the linearization rest on the equilibrium
boundary-layer hypothesis, so discrepancies are expected near separation
and in recirculation; they report such near-wall differences in the
recirculation of a backward-facing step and in the slat cove of a
three-element airfoil (§4.2.2, §4.3.2). They mention ODE wall models on
embedded grids as costlier and possibly unstable on non-body-fitted grids
(§3.1).

[Bose & Park (2018)](/sources/bose-2018.md), §2.1, §3, cite an
extension of the integral wall model of Yang et al. (2015) to immersed
boundaries and the wall-modelled sharp immersed boundary of Dhamankar et
al. (2016); the review lists both among
implementation studies it does not discuss (see
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).

**Wall stress applied as a flux on a sharp immersed boundary (hypersonic
flows).** In the ghost-cell IBM of [van Noordt et al. (2022)](/sources/vannoordt-2022.md)
(previous section), an ODE
[equilibrium wall model](/methods/equilibrium-wall-model.md) for momentum
and energy, with a van Driest-damped mixing length in the semi-local
coordinate $y^*$ ($\kappa=0.41$, $A^+=17$; Eqs. 34–37), is solved at the
centroids of the surface triangles from the LES state at the outer
sampling point; the wall shear stress and heat flux are interpolated to
the intersections of grid lines with the surface and applied there
directly as viscous fluxes (§2.5, Fig. 4). The authors contrast this with
the dynamic slip (Robin) condition of Bose & Moin, which they do not use
(§2.6; see [slip-wall models](/methods/slip-wall-model.md)). A
transition sensor switches the wall-model eddy viscosity off where the
resolved flow is laminar; its threshold is tuned to the reference
transition location (§3.2, Eq. 58). Findings (§3, §4):

- channel at $Re_\tau=5200$: moving the exchange point between 3 and
  $4\Delta x_{\min}$ and the inner sampling point between 0.5 and
  $1.5\Delta x_{\min}$ has no significant effect; interior dissipation
  matters much more than that of the irregular cells (best $\sigma_b=0.0125$
  inside, 0.05, 0.025, 0.0125 in the first three irregular cells); the
  log-region deviation from the DNS "has almost completely vanished"
  with refinement, while the inner Reynolds stresses stay poor against the
  DNS, as for body-fitted WMLES (Figs. 12–14; see
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md));
- Mach-6 transitional flat plate and shock/boundary-layer interaction:
  heat transfer is "very sensitive" to the dissipation added at the
  immersed boundary; on a grid rotated by 0 to $12^\circ$ the peak heat
  transfer agrees within about 5% and the separation bubble grows slightly
  with the angle, which the authors attribute to irregular points
  appearing in the streamwise direction (Figs. 16, 21–24; see
  [shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md));
- Mach-7.2 $8^\circ$ compression ramp against the DNS of Priebe & Martín:
  the fine grid captures the wall pressure, the coarse grid raises it too
  early and overpredicts instantaneous separation; the minimum $C_f$ is
  "notably higher" than the DNS, which the authors relate to the pressure
  gradient and convection that the equilibrium model omits (Figs. 26–27);
- coarse–fine refinement interfaces partly reflect acoustic waves from the
  transition region back into the boundary layer, visible in the
  wall-normal Reynolds stress though negligible in the means (§3.3.2,
  Fig. 24; see [mesh adaptation](/methods/mesh-adaptation.md)).

**Immersed boundaries in a multi-code high-lift assessment.**
[Kiris et al. (2023)](/sources/kiris-2023.md) summarize the wall-modelled
LES group of the fourth AIAA High-Lift Prediction Workshop on the
[NASA CRM high-lift model](/benchmarks/nasa-crm-high-lift.md). Two of its
nine submissions "utilized Cartesian isotropic grids with the geometry
represented via their respective immersed boundary formulations" (§II.1):
the [lattice Boltzmann](/methods/lattice-boltzmann-method.md) code
PowerFLOW (W-032; 475 million points, a proprietary pressure-aware wall
model) and the finite-difference code FFVHC-ACE (W-049; 11.2 billion
points, a second-order kinetic-energy- and entropy-preserving scheme, the
CSM subgrid model and an equilibrium wall model, wall-normal spacing
3.2 mm at a 7 m full-scale chord; Tables 1–2). The authors note that W-049
"could be perceived as an outlier since it utilizes an immersed boundary
formulation, although its models are nonproprietary" (§II.5). Both
predict inboard stall from the wing–pylon juncture (their topology B,
§IV). Kiris et al. (§I) take the success of Cartesian grids, as they cite
from the previous workshop, and of Voronoi grids as a suggestion that
near-unity aspect ratios are needed near maximum lift, at the price of a
larger wall-normal spacing, and point to the off-body vortices that
isotropic grids suit; they reach no conclusion on isotropic against
anisotropic grids (§VI; see [wall-modelled LES](/methods/wall-modelled-les.md)).

## Moving bodies on rigidly moving Cartesian grids

[Sugaya & Imamura (2021)](/sources/sugaya-2021.md) extend the
hierarchical Cartesian-grid solver UTCart to bodies in motion by moving
the whole Cartesian grid rigidly with the body. They contrast this with
fixed-grid immersed boundaries, in which cells change from body to fluid
as the body moves (the "fresh cell" problem, with spurious pressure
oscillations; they cite Seo & Mittal) and in which a boundary layer has
to be resolved while it sweeps through the cells (§1). With the grid
attached to the body, the wall-cell classification and the image points
are computed once at the start, and the turbulent boundary layer stays in
the same cells, so the wall-function treatment of the stationary solver
carries over (§2.2, Conclusion). They call theirs the first study that
combines immersed boundaries and wall functions on Cartesian grids with a
moving grid for unsteady turbulent flow around moving bodies (§1).

**Moving-grid flux.** The grid-motion flux $Q\,V_n$ ($Q$ the conservative
variables, $V_n=\boldsymbol V\cdot\boldsymbol n$ the face-normal grid
velocity, page-local) is folded into the inviscid flux by a Galilean
transformation $\mathsf T$ (page-local) to variables relative to the grid,
$$F(Q,\boldsymbol n)-Q\,V_n=\mathsf T^{-1}F(\mathsf TQ,\boldsymbol n),\qquad \mathsf TQ=\big(\rho,\ \rho(\boldsymbol u-\boldsymbol V),\ \rho e_{\mathrm i}+\tfrac12\rho\lvert\boldsymbol u-\boldsymbol V\rvert^2\big),$$
($e_{\mathrm i}$ the internal energy per unit mass, page-local), so that the
SLAU approximate Riemann solver acts on grid-relative states and the result
is transformed back (§2.1, Eqs. 4–9, after Nishikawa and Muffo et al.).
For the cell-to-cell flux they use the
dimension-by-dimension finite-volume scheme of Tamaki & Imamura, which
they cite: fourth order where the grid is uniform and second order at faces
where the cell size changes, because the least-squares gradient is first
order there; they therefore call it a "high-order scheme". A rigid grid
velocity $\boldsymbol V=\boldsymbol V_{\mathrm{trans}}+\boldsymbol\omega_{\mathrm g}\times\boldsymbol r$
($\boldsymbol\omega_{\mathrm g}$ the angular velocity of the grid,
page-local) varies linearly over a face, which adds the correction
$-\frac{h^2}{12}(\partial_YV_n)(\partial_YQ)$ ($Y$ the face-tangential
coordinate) to the quadrature-modification flux and keeps the
face-averaged flux $O(h^4)$ (§2.3, Eqs. 22–26). Only the inviscid flux is
high order; the viscous flux is second-order central.

**Wall condition at the face centre** (§2.2, Table 1, Eqs. 10–15,
extending Tamaki et al. 2017). Walls are imposed at the face
centres (FC) between fluid cells and cells cut by the body. The image
point (IP) lies on the wall normal through the face centre at
$d_{\mathrm{IP}}=2\Delta x$ from the wall ($\Delta x$ the near-wall cell
size), its values interpolated linearly with the gradient of the fluid
cell that contains it. With $u_n$, $u_t$ the wall-normal and tangential
velocities, $V_{n,w}$, $V_{t,w}$ those of the wall, $d_{\mathrm{FC}}$ the
wall distance of the face centre and $f(y^+)$ the Spalart–Allmaras wall law
(page-local subscripts):
$$\begin{aligned}
u_{n,\mathrm{FC}}&=u_{n,\mathrm{IP}}-\frac{u_{n,\mathrm{IP}}-V_{n,w}}{d_{\mathrm{IP}}}\,(d_{\mathrm{IP}}-d_{\mathrm{FC}}),\\
u_{t,\mathrm{FC}}&=u_{t,\mathrm{IP}}-u_\tau\,f'(y^+_{\mathrm{IP}})\,(y^+_{\mathrm{IP}}-y^+_{\mathrm{FC}}),\\
u_\tau f(y^+_{\mathrm{IP}})&=u_{t,\mathrm{IP}}-V_{t,w},
\end{aligned}$$
the last solved for $u_\tau$ by Newton–Raphson with
$\partial f/\partial u_\tau=(y^+/u_\tau)f'(y^+)$. For a wall at rest it is
the original condition of Tamaki et al. The temperature is extrapolated
linearly from the image point; the pressure at the face centre is taken
from the fluid cell that owns the face instead of the image point, a
change the authors report as "a small improvement" in simple tests,
without showing it; the density follows from the equation of state. The
near-wall Spalart–Allmaras modification of Tamaki et al. is used but not
printed. See [RANS wall functions](/methods/rans-wall-function.md).

**Validation** (§3–4):

- *Galilean invariance.* A steady Spalart–Allmaras RANS of the
  [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re=6\times10^6$,
  $\alpha=10^\circ$ and relative Mach number 0.15 gives the same residual
  history (differences "in the order of machine zero") and the same $C_p$,
  $C_f$, velocity and eddy-viscosity profiles with the stream on a fixed
  grid and with the grid moving through quiescent air, in agreement with
  the body-fitted code FaSTAR; $y^+_{\mathrm{IP}}\approx230$ at $x/c=0.5$
  (§3.1, Table 3, Figs. 4–8; see the
  [geometric conservation law](/properties/geometric-conservation-law.md)).
- *Pitching airfoil.* On AGARD Case 3 (NACA 0012, $M_\infty=0.6$,
  $Re=4.8\times10^6$, $\alpha=4.86^\circ+2.44^\circ\sin\omega t$, reduced
  frequency 0.081), the $C_l$ hysteresis loop with its inversion near
  $\alpha\approx6^\circ$ and the shock and suction-peak positions agree with
  experiment and with the body-fitted FUN3D; the pitching-moment
  difference from experiment is about 0.005, "almost the same" as with the
  body-fitted grid (§3.2, Figs. 10–13). Because the conservation laws are
  not strictly satisfied near the body with immersed boundaries, the
  authors compare with this conservative body-fitted solution (§3.2).
- *Hovering rotor.* DDES-p (a delayed detached-eddy simulation whose
  modified shielding protects RANS regions where the streamwise spacing is
  small on Cartesian grids, not printed) of the
  [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md) on 75 and
  149 million cells, $y^+_{\mathrm{IP}}$ up to about 500 on the coarser
  grid: thrust coefficient 0.00514–0.00521 and figure of merit 0.594–0.618
  across grids and schemes, surface pressure and tip-vortex trajectories
  in agreement with experiment, and finer wake vortices with secondary
  braid structures with the high-order scheme than with MUSCL (§4,
  Tables 6–7, Figs. 17–19; see
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

They cite earlier work for the acceptability of immersed boundaries with
wall functions "when $y^+$ is approximately 500 or less" for the surface
pressure (§3.1).

## Volume filtering and wall-slip models for LES

[Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) derive the IB force
from filtering rather than from a discretization, extending the
volume-filtering IB method of Dave et al., which they cite, valid in its "DNS
limit", to wall-modelled LES, which they call **immersed boundary-modelled
LES (IBMLES)**. Page-local symbols: $\mathbb I_f$ the fluid indicator,
$\varphi_f$ the fluid volume fraction ($\alpha_f$ in the source, renamed
because $\alpha$ is the registry's blending factor and $\alpha_f$ its
modal-filter strength), $\Delta_f$ the support
width of the kernel ($\delta_f$ in the source), $S_w$ the wall surfaces,
$\boldsymbol n$ the wall normal pointing into the fluid, $\boldsymbol u_w$
the wall velocity, $\boldsymbol T=-p\boldsymbol I+2\mu\boldsymbol S$ the
total fluid stress (incompressible), $\boldsymbol F_{\mathrm{IB}}$ the IB
force density, $\boldsymbol u_{\mathrm{slip}}$ the wall slip,
$\boldsymbol\ell$ the slip lengths and $\boldsymbol\Lambda$ the gradient
ratios, one per direction, with streamwise components $\ell_x$, $\Lambda_x$
(the source's $\boldsymbol\lambda$, renamed because $\lambda$ is the Taylor
microscale).

**Filter.** The incompressible equations are convolved with a unitary,
symmetric kernel $G$ of compact support ($G=0$ for
$\lVert\boldsymbol y\rVert\ge\Delta_f/2$) that is truncated by $\mathbb I_f$
and **not rescaled** near walls, unlike wall-resolved LES (filter refined
near the wall) and the truncated-and-rescaled filter of Bose & Moin,
which they cite (§2.1, Fig. 1):
$$\varphi_f=G*\mathbb I_f,\qquad \varphi_f\,\bar{\boldsymbol u}=G*(\mathbb I_f\boldsymbol u)$$
(Eqs. 2.6–2.7), so $\varphi_f=\tfrac12$ at a planar wall for any symmetric
kernel and filtered fields extend $\Delta_f/2$ into the solid. The commutation
terms are then exact surface integrals,
$$\overline{\nabla\phi}-\nabla\bar\phi=\frac1{\varphi_f}\Big((\nabla\varphi_f)\,\bar\phi-\iint_{S_w}\boldsymbol n\,\phi\,G(\boldsymbol x-\boldsymbol y)\,dS\Big)$$
(Eq. 2.11, with analogues for divergence and time derivative), which the
authors contrast with the commutation errors that most wall-resolved and
wall-modelled LES ignore and that "can be of the order of the subgrid
terms" (§2.1, citing Ghosal & Moin and others).

**Filtered momentum equation.** With $\tau_{ij}$ the registry's SGS stress
(here the full, not deviatoric, $\overline{u_iu_j}-\bar u_i\bar u_j$),
$$\rho\big(\partial_t(\varphi_f\bar{\boldsymbol u})+\nabla\cdot(\varphi_f\bar{\boldsymbol u}\bar{\boldsymbol u})\big)=\varphi_f\nabla\cdot\big(\boldsymbol T^{R}+\boldsymbol T^{\mathrm{res}}-\rho\boldsymbol\tau\big)+\boldsymbol F_{\mathrm{IB}}$$
(Eq. 2.22), where $\boldsymbol T^R$ is the stress built from $\bar p$ and
$\bar{\boldsymbol u}$ (including a $-\tfrac23\nabla\cdot\bar{\boldsymbol u}$
term, since $\bar{\boldsymbol u}$ is not solenoidal near walls) and
$\boldsymbol T^{\mathrm{res}}=\overline{\boldsymbol T}-\boldsymbol T^R$ the
**residual viscous stress**, closed but non-trivial (Eqs. 2.16–2.18): at the
wall it is linear in the slip (Eq. 2.27). The IB force, to
$O(\Delta_f^2)$,
$$\boldsymbol F_{\mathrm{IB}}\approx-\iint_{S_w}\boldsymbol n\cdot\big(\boldsymbol T-\boldsymbol T^R-\boldsymbol T^{\mathrm{res}}+\rho\boldsymbol\tau\big)\,G\,dS$$
(Eq. 2.24), is non-zero only in a band of width $\Delta_f$ around the surface.
Eq. (2.25) expresses the wall stress through the wall values of the
filtered stresses and the time derivative of the slip velocity $\boldsymbol u_{\mathrm{slip}}=\bar{\boldsymbol u}|_w-\boldsymbol u_w$
(Eq. 2.19), which is therefore the only unclosed wall quantity: "modelling
the wall slip is in essence a turbulence wall model" (§4), an alternative to
supplying the wall stress from a conventional wall model, which the
authors note could also be done (§2.3). No-slip holds only in the DNS limit
$\Delta_f^+<1$ (§2.3); at wall-modelled filter sizes the no-slip forcing of
most IB methods "is not valid" (§1). See
[wall-modelled LES](/methods/wall-modelled-les.md).

**A priori magnitudes** (§3, Figs. 5–10; Lee & Moser
[channel](/benchmarks/turbulent-channel-flow.md) DNS at $Re_\tau=5200$
filtered with a cosine kernel at $\Delta_f^+=50$–300 on a uniform
post-processing grid of spacing $\Delta_f/16$): the mean streamwise slip is
$6.93u_\tau$ at $\Delta_f^+=50$ and $13.5u_\tau$ at $\Delta_f^+=300$, growing
logarithmically; mean wall-normal and spanwise slips are negligible; the
slip r.m.s. is about $1.5u_\tau$ streamwise, $0.3u_\tau$ spanwise and
$0.02u_\tau$ wall-normal, and the slip field carries near-wall streaks at
$\Delta_f^+=50$ and outer-layer structures at $\Delta_f^+=300$. Above
$y^+\approx\Delta_f^+$ the filtered mean velocity recovers the log law; the
peak SGS stress grows from $0.24\tau_w$ to $0.57\tau_w$ over the range; the
residual viscous stress, of compact support within $\Delta_f/2$ of the wall,
exceeds the filtered viscous stress at every filter size.

**Slip closures** (§4–§5). (i) A **Van Driest slip model**: the slip of the
volume-filtered Van Driest profile ($\kappa=0.41$, $A^+=26$; Eq. 4.2),
approximated for $\Delta_f^+\ge100$ by
$$\frac{\langle u_{\mathrm{slip}}\rangle}{u_\tau}\approx\frac{1}{\varphi_{f,w}}\Big(\frac{1}{2\kappa}\ln\frac{\Delta_f^+}{2}+a_0+b_0\,(\Delta_f^+)^{-n_0}\Big)$$
(Eqs. 4.5, 5.4, 7.1; page-local constants $(a_0,b_0,n_0)=(0.972,-72.0,0.9523)$
for the cosine kernel, $0.81\pm0.21$, $-67.5\pm4.5$, $0.92\pm0.03$ across four
kernels), in "excellent agreement" with the filtered DNS. (ii) A
**slip-length model** from the exact commutation identity at the wall,
$$\boldsymbol u_{\mathrm{slip}}=\frac{\varphi_{f,w}}{\partial_n\varphi_f|_w}\Big(\overline{\partial_n\boldsymbol u}\big|_w-\partial_n\bar{\boldsymbol u}\big|_w\Big),\qquad \boldsymbol\ell=\frac{\varphi_{f,w}\,(\boldsymbol\Lambda-1)}{\partial_n\varphi_f|_w}$$
(Eqs. 4.8, 4.13; $\boldsymbol\Lambda$ the ratio of the mean filtered wall gradient to
the mean wall gradient of the filtered velocity, per direction), which the
authors present as a derivation, valid for curved and moving walls whose
curvature the filter resolves, of the Bose & Moin slip condition that they
say "suffers from the commutation errors" and handles only planar static
walls. Fitted on the channel, $\Lambda_y=\Lambda_z=1$ and
$\Lambda_x=1+0.251(\Delta_f^+)^{0.5385}$, giving
$\ell_x^+=0.0798(\Delta_f^+)^{1.5385}$ for the cosine kernel (Eqs. 4.25–4.27),
roughly $\Lambda_x\approx1+0.3(\Delta_f^+)^{0.5}$ and
$\ell_x^+\approx0.08(\Delta_f^+)^{1.5}$ across kernels; with $\varphi_{f,w}=\tfrac12$
and $\partial_y\varphi_f|_w=G_1(0)=\pi/(2\Delta_f)$ for the cosine kernel
($G_1$ the one-dimensional factor of the tensor-product kernel, page-local),
$0.5\times0.251\times2/\pi=0.0799$ *(compiler check, not in the sources)*.
$\boldsymbol\Lambda\to(1,1,1)$ and $\boldsymbol\ell\to0$ as $\Delta_f\to0$, recovering no-slip. Cosine,
triangle, parabolic and triweight kernels change the results little
(stress profiles within 1% at $\Delta_f^+=300$). (iii) A dynamic slip length
from the [Germano identity](/methods/dynamic-procedure.md), with the test
level scaled as $\hat\ell_x=(\hat\Delta_f/\Delta_f)^{n_1+1}\ell_x$ ($n_1$ the
exponent of $\Lambda_x$) and solved explicitly rather than by least
squares, is proposed but not tested (§6).

The study is a priori only: no forward IBMLES is run, a posteriori tests
are deferred, the SGS stress is expected to be closed by existing models
such as dynamic Smagorinsky, the constants come from a single
$Re_\tau=5200$, and rough, deforming or strongly separated walls are
excluded (§4.2, §7).

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
relocation of forcing points of Xu & Liu, which they cite (§4.2). At $15^\circ$
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
They agree with Cai et al. (2021), which they cite, that far-field integration
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
BGK-type equation whose relaxation time $\tau_{\mathrm{LB}}$ sets the total
viscosity $\nu+\nu_t=c_s^2(\tau_{\mathrm{LB}}-\Delta t/2)$ with lattice sound speed
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
- **Penalization error exponent.** D'Ayer et al. (2026) print the
  modelling error as $\lVert\boldsymbol U-\boldsymbol U_\eta\rVert=O(\eta_p^{-1/2})$
  (Eq. 14; $\boldsymbol U_\eta$ the penalized solution, page-local), which
  grows as $\eta_p\to0$, against their own statement that the
  penalized solution converges as $\eta_p\to0$; Llorente (2024, p. 2) cites the
  Angot–Bruneau–Fabrie estimate as an error $\propto\eta_p^{1/2}$.
- **Printed slips (D'Ayer et al.).** With $\mathsf A=\mathrm{diag}(0,\boldsymbol I,1)$
  as printed, Eq. (23) gives the density $\chi r_p\rho_0$ in the solid,
  decaying to zero, while the density row of $\boldsymbol s_p$ is zero, so
  the exact sub-problem keeps $\rho_0$ *(compiler check, not in the
  sources)*. The channel of 8 roughness patterns of length $\sqrt3\,d$,
  $d=4k_r$, $k_r=\delta/20$, has $L_x=2.77\delta$, i.e. $L_x^+\approx1109$ at
  $Re_\tau=400$, against the printed 1009; $L_z^+=240$ checks *(compiler
  check, not in the sources)*. Both values satisfy the minimal-channel
  condition $L_x^+\ge1000$ that the authors quote. The version read is the
  HAL submitted manuscript (May 2025), which prints four authors where the
  published record lists three.
- **Printed inconsistencies (Rickard & Kasbaoui).** The Fig. 6 caption calls
  the streamwise slip fluctuations "approximately 10 % or less of mean slip
  values", while the text gives r.m.s. $1.5u_\tau$ against means of
  $6.93u_\tau$ and $13.5u_\tau$, i.e. 22% at $\Delta_f^+=50$ and 11% at 300
  *(compiler check, not in the sources)*. §4.1 calls the Van Driest slip
  approximation accurate for $\Delta_f^+\ge50$, while Fig. 11(b), Eq. (5.4) and
  Eq. (7.1) state $\Delta_f^+\ge100$; Eq. (4.5) gives $6.32u_\tau$ at
  $\Delta_f^+=50$ against the filtered-DNS $6.93u_\tau$, and $13.5u_\tau$ at
  300 *(compiler check, not in the sources)*. In Eq. (2.25) the bracket adds
  an acceleration to the divergence of $\boldsymbol T^R+\boldsymbol T^{\mathrm{res}}$,
  a force per unit volume, so a factor $1/\rho$ is missing there *(compiler
  check, not in the sources)*.
- **Wall-normal gradient (Husson et al.).** Their Eq. (43) sets the
  wall-normal gradient of the tangential velocity at the forcing node to
  $\big[c_{v1}^3+(\kappa y^+_{\mathrm{IP}})^3\big]/\big[c_{v1}^3+(\kappa y^+_{\mathrm{IP}})^3(1+\kappa y^+_{\mathrm{IP}})\big]\,u_\tau$.
  The fraction is $\mathrm du^+/\mathrm dy^+=1/(1+\chi f_{v1})$ of the
  Spalart–Allmaras equilibrium layer with $\chi=\kappa y^+$ (from the
  paper's Eqs. 18–19 and a total stress $(\nu+\nu_t)\,\partial u/\partial y=u_\tau^2$); the dimensional gradient is that
  fraction times $u_\tau^2/\nu$, not $u_\tau$, and it is evaluated at the
  interpolation point while the left-hand side is at the forcing node
  *(compiler check, not in the sources)*. Eq. (41) uses a wall distance $y$
  that the paper does not define.
- **Moving grids (Sugaya & Imamura 2021).** No order-of-accuracy test of
  the moving-grid extension is shown: the fourth-order claim on uniform
  patches rests on the cited Tamaki & Imamura (2017). The "first study"
  claim is the authors'; they cite earlier immersed-boundary DES of
  rotorcraft (Park, Linton & Thornber 2020). Their Eq. (22)
  prints the prefactor $1/\Delta x$ against limits $\pm\Delta X/2$ and
  expands $Q$ without the $1/2!$ of their Eq. (16); the printed final line
  follows from $\frac1h\int_{-h/2}^{h/2}\eta^2\,d\eta=h^2/12$ with the
  $\eta^2$ term absorbed into the face average *(compiler check, not in the
  sources)*.
- **No-slip forcing or modelled wall law.** Rickard & Kasbaoui (2026) state
  that the no-slip forcing of most IB methods is not valid at wall-modelled
  filter sizes and model the filtered slip; Cai et al. (2022), Constant et
  al. (2024) and Mozaffari et al. (2024) instead impose a wall law at
  off-wall reconstruction points. The approaches act on different
  quantities, the first is tested only a priori, and no source compares
  them.

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §II.A, Eqs. (1)–(15) (lattice Boltzmann, HRR collision, Vreman model); §II.B.1, Eqs. (16)–(20) (boundary-point reconstruction); §II.C.1, Eqs. (24)–(27), Fig. 1 (wall model on the IBM, constrained LES); §III, Tables I–II, Eq. (28); §IV, Table III, Figs. 4–9 (Ahmed body).
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §I (Cartesian and Voronoi grids at the previous workshop, aspect ratio); §II.1–2, §II.5, Tables 1–2 (two immersed-boundary Cartesian submissions, W-049 as outlier); §IV (stall topology B); §VI (grid isotropy).
- [Placco et al. (2023)](/sources/placco-2023.md) — §2 (ghost-point-forcing IBM in STREAmS); §3 (grid).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.7, Eqs. (27)–(29), Fig. 14 (volume penalization, ray tracing, wind turbine).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1; §3, footnote 6 (reconstruction inside the solid, soft no-slip); §7.1, Fig. 24 (pipe DNS and LES).
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §1; §2.1–2.4, Eqs. (1)–(28) (lattice Boltzmann host, direct forcing, kernels, Lagrangian weight); §2.5–2.7, Eqs. (29)–(38) (structural scheme, coupling, LES); §3.1–3.2, Tables 2–11 (cylinder, Poiseuille); §3.3–3.4, Tables 12–13, Figs. 12–19 (flag, beam); §4.
- [Constant et al. (2024)](/sources/constant-2024.md) — HAL author manuscript hal-04731107v1: §1; §3, Eqs. (5)–(11), Figs. 3, 6 (ghost-cell direct forcing, modelling height, Musker wall function); §4.1–4.2, Eq. (19), Figs. 10–11 (adaptation); §5.1–5.2, Eqs. (20)–(25), Figs. 12–15 (second image layer, wall-pressure reconstruction); §6.1–6.3, Tables 3, 6, 8–9, Figs. 18–28 (NACA 0012, 2DMEA, HL-CRM); §7.
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1, Eqs. (2.1)–(2.2) (mass source and momentum forcing, discretization); §4.2.1, Fig. 9 (QUICK near the cylinder front).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — HAL accepted manuscript hal-04921212v1: §2.2, Fig. 1 (reference-point reconstruction with a wall model); §3.3, Figs. 16–24, Table 3 (Ahmed body, wall model against no-slip).
- [Llorente (2024)](/sources/llorente-2024.md) — author accepted manuscript: pp. 2–4, Eqs. (1)–(6) (penalized and conventionally penalized URANS equations, time-scale condition); p. 5, Eq. (7) (artificial velocity); pp. 6–8, Eqs. (8)–(12) (fluid resistance, averaged source, closure, closed system); pp. 8–10, Theorem 1, thermal and compressible extensions.
- [Husson et al. (2024)](/sources/husson-2024.md) — §3.1, Eqs. (36)–(39) (SA analytical wall law, linearization, modified $f_{v1}$); §3.2, Fig. 2, Eqs. (40)–(43) (fluid-side direct forcing, interpolation point, five-step algorithm); §4.1.2, Fig. 5 (inclined plate); §4.2.2, §4.3.2 (near-wall discrepancies in recirculation).
- [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §2.3 (direct-forcing IBM for flexible ribbons, Roma kernel, marker condition); §3.2–3.3; §5.1, §5.3 (canopy force equals the averaged IBM force); App. C.
- [Rismondo et al. (2025)](/sources/rismondo-2025.md) — introduction (IBM-based LES of rotor wakes by Posa et al. cited; body-fitted meshes used).
- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — HAL submitted manuscript hal-05075852v1: §1; §2.2 (spectral difference in JAGUAR); §2.3, Eqs. (11)–(15) (Brinkman penalization, error decomposition); §2.4, Eqs. (16)–(23) (stiffness limits, Strang splitting, exact penalization sub-steps); §3.1, Eqs. (24)–(26), Tables 1–2, Figs. 3–5 (cylinder at $Re_D=40$); §3.2, Eqs. (27)–(28), Table 3, Figs. 7–10 (rough minimal channel at $Re_\tau=400$); §4.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §1 (fixed against moving grids, fresh cells); §2.1, Eqs. (1)–(9) (moving-grid flux, Galilean transformation); §2.2, Eqs. (10)–(15), Table 1 (face-centre wall condition with wall velocity); §2.3, Eqs. (16)–(26) (high-order flux and its moving-grid correction); §3.1–3.2, Tables 2–3, Figs. 4–13 (NACA 0012, AGARD Case 3); §4, Tables 6–7, Figs. 17–19 (Caradonna–Tung rotor).
- [Zhang et al. (2022e)](/sources/zhang-2022-i.md) — §II A (immersed-boundary terrain in LESGO, log-law wall stress); §III A, Fig. 4 (steep-hill validation, wall-model attribution); App. A, Table I, Fig. 22 (grid study).
- [Stanly et al. (2022)](/sources/stanly-2022.md) — §2.1 (MIRACLES); §2.3 (tower as an actuator line instead of a body); §6 (immersed-boundary tower as future work).
- [Bose & Park (2018)](/sources/bose-2018.md) — §2.1, §3 (integral wall model and wall-modelled sharp immersed boundary, cited).
- [Kang & Masud (2022)](/sources/kang-2022.md) — §2.2, Eqs. (5)–(9) (mixed form); §3.1–3.3, Eqs. (10)–(48), Table 1 (VMIB derivation, stabilization tensors, multiplier, interface terms, lemmas, ghost penalty); §3.4–3.5 (residual-based VMS LES); §4, Boxes 1–2 (algorithm, classification, quadrature); §5.1–5.3, Tables 3–5, Figs. 7–35 (cylinder, sphere, train).
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §1; §2.3, Eqs. (8)–(24) (hybrid flux, single-ghost-cell WENO closure); §2.4, Eqs. (25)–(31) (irregular viscous stencils); §2.5, Eqs. (32)–(37) (wall model as flux); §2.6, Algorithm 1, Eqs. (38)–(42) (ray-based ghost filling); §2.7–2.8, Tables 1–2, Figs. 8–10 (MMS, pseudospectra); §3.1–3.4, Figs. 12–27; §4.
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §1 (IB in LES, non-uniform grids, no-slip at WMLES filter sizes); §2.1–2.3, Eqs. (2.1)–(2.27), Fig. 1 (volume filter, commutation identities, residual viscous stress, IB force, wall slip); §3, Figs. 5–10 (a priori channel at $Re_\tau=5200$); §4.1, Eqs. (4.1)–(4.5), Fig. 11 (Van Driest slip); §4.2, Eqs. (4.6)–(4.27), Figs. 12–13 (slip length); §5, Tables 1–2 (kernels); §6, Eqs. (6.1)–(6.9) (dynamic slip length); §7.
