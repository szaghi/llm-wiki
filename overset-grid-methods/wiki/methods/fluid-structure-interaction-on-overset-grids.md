---
type: Method
title: "Fluid–structure interaction on overlapping grids"
description: "Partitioned fluid–structure coupling on moving and deforming overlapping grids: Henshaw and Schwendeman's rigid bodies driven by compressible flow with a predictor–corrector Newton–Euler integrator, and Banks et al.'s added-mass partitioned scheme whose impedance-weighted interface projection stays stable for light nonlinear solids where the traditional partitioned scheme fails."
status: established
aliases: [FSI on overlapping grids, FSI on overset grids, FSI-DCG, deforming composite grids, added-mass partitioned algorithm, AMP scheme, rigid-body coupling on overlapping grids]
tags: [fsi, moving-grid, composite-grid, compressible, overset-grid]
timestamp: 2026-11-02T15:27:00Z
---

# Fluid–structure interaction on overlapping grids

In **fluid–structure interaction (FSI) on overlapping grids** the fluid is
computed on a [composite overlapping grid](/definitions/composite-overlapping-grid.md)
whose body-fitted component grids follow the structure, while the structure
moves as a rigid body or deforms as a solid. Each time step couples three
pieces: the motion of the grids and the recomputed
[domain connectivity](/definitions/domain-connectivity.md)
(see [moving overset grids](/methods/moving-overset-grid.md)), the fluid
update, and the structural update driven by the fluid's traction. In the two
sources that treat the coupling as their subject the fluid is inviscid and
compressible and the coupling is *partitioned*: fluid and structure are
advanced by separate solvers that exchange interface data
([Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md),
[Banks et al. (2016)](/sources/banks-2016.md)). Banks et al. also discretize
the *solid* on its own overlapping grid.

## Rigid bodies (Henshaw & Schwendeman)

**Equations.** Henshaw & Schwendeman (2006, §2, Eqs. (4)–(5)) move each rigid
body by the Newton–Euler equations with inviscid loading and no body force:
$$\frac{d\mathbf x_{\mathrm{cg}}}{dt}=\mathbf v_{\mathrm{cg}},\qquad m_b\frac{d\mathbf v_{\mathrm{cg}}}{dt}=\boldsymbol{\mathcal F}=-\int_{\partial\mathcal B}p\,\mathbf n\,dS,\qquad\boldsymbol{\mathcal M}=-\int_{\partial\mathcal B}(\mathbf x-\mathbf x_{\mathrm{cg}})\times p\,\mathbf n\,dS,$$
with $\partial\mathcal B$ the body surface (page-local) and $\mathbf n$ its
unit normal. The rotation obeys Euler's equations in
the principal axes of the inertia tensor $\mathsf I_b$; in 2-D,
$I_3\dot\omega_3=\mathcal M_3$ (page-local components). Grid points attached
to the body move rigidly,
$\mathbf x(t)=\mathbf x_{\mathrm{cg}}(t)+\mathsf R(t)\mathsf R(0)^{-1}\big(\mathbf x(0)-\mathbf x_{\mathrm{cg}}(0)\big)$,
where the columns of $\mathsf R$ are the principal axes, and their velocity is
the grid velocity $\mathbf u_g$ of the mapped equations.

**Integrator.** The body state is advanced by a leap-frog predictor and a
trapezoidal corrector (§4.3). With page-local superscripts $n$ (time level)
and $\mathrm p$ (predicted):
$$\begin{aligned}
\mathbf v^{\mathrm p}&=\mathbf v^{n-1}+2\Delta t\,\dot{\mathbf v}^n, &\mathbf x^{\mathrm p}&=2\mathbf x^n-\mathbf x^{n-1}+\Delta t^2\,\dot{\mathbf v}^n,\\
\mathbf v^{n+1}&=\mathbf v^n+\tfrac{\Delta t}{2}\big(\dot{\mathbf v}^n+\dot{\mathbf v}^{\mathrm p}\big), &\mathbf x^{n+1}&=\mathbf x^n+\tfrac{\Delta t}{2}\big(\mathbf v^n+\mathbf v^{\mathrm p}\big),
\end{aligned}$$
for the centre of gravity $\mathbf x=\mathbf x_{\mathrm{cg}}$,
$\mathbf v=\mathbf v_{\mathrm{cg}}$, and likewise for the angular velocity and
the principal axes. Both stages are second order. The leap-frog is chosen for
its low dissipation for purely imaginary eigenvalues, and the corrector
handles perturbations off the imaginary axis; the first step uses an
unspecified second-order single-step method. The predicted grid is moved, the
connectivity updated, the fluid advanced, and the grid then corrected with
the new loads, without recomputing the connectivity after the corrector
(§3.4; see [moving overset grids](/methods/moving-overset-grid.md)).

**Wall condition.** The moving body's wall is a slip wall,
$\mathbf n\cdot(\mathbf u-\mathbf u_g)=0$. Its numerical boundary condition
fills the ghost temperature from a compatibility condition that contains the
wall acceleration (§5, Eq. (14)); it is described on
[shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).

**Verification.** The pressure-driven piston (§6.2.2, Table 3) moves a
1-D piston of mass 2 and area 1 by the gas pressure behind it, against an
exact solution, on a moving grid that cuts a hole in a fixed grid. The flow
has a jump in the first derivative at the rarefaction head, and the errors at
$t=1$ converge at rate 0.71 in the max norm, 1.32–1.34 in the 1-norm and about
1.05 in the 2-norm, which the authors call consistent with linear-advection
theory for non-smooth solutions. The errors of the piston position and
velocity fall by a factor 3.7 per halving of the spacing, close to second
order (Fig. 13). The shock-driven cylinder (§6.3.2) and the 26 free cylinders
in a detonation (§7.2) are computed with the same coupling; see
[shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md).

## Deforming solids: the added-mass partitioned scheme (Banks et al.)

**Deforming composite grids.** Banks et al. (2016, §4.1) discretize the fluid
domain and the solid domain each by its own overlapping grid of structured
component grids, boundary-fitted near boundaries and Cartesian in the bulk.
The fluid grids next to the interface deform: after the interface points are
advanced, a hyperbolic grid generator regenerates them by marching from the
interface, and the Overture grid generator Ogen recomputes holes and
interpolation points every step. The solid is computed in Lagrangian reference
coordinates on static grids. Separate solvers of the Overture framework
advance the fluid (Cgcns) and the solid (Cgsm) under a multi-physics
controller (Cgmp) ([Overture](/software/overture.md)). The fluid uses the
mapped Euler equations with grid velocity and the second-order Godunov scheme
of Henshaw & Schwendeman, adjusted for free-stream preservation on deforming
grids (§4.2, Eq. (31)).

**Solid on overlapping grids.** The solid is a first-order system for
displacement, velocity and nominal stress of a hyperelastic material
(Saint Venant–Kirchhoff or neo-Hookean), solved by a second-order
characteristic upwind Godunov scheme (§2, §4.2). In 2-D the system has eight
characteristic speeds, four of them zero (the tangential stress and the
displacement). Upwinding damps the p- and s-wave components but not these
neutrally stable ones, and the authors "find it necessary to add numerical
dissipation to the approximations to suppress possible weak instabilities at
grid overlaps" (§4.2): a fourth-order dissipation acting on the tangential
stress and the displacement, which adds $O(\Delta r^4/\Delta t)=O(\Delta r^3)$,
below the scheme's $O(\Delta r^2)$ truncation error ($\Delta r$ the parameter
spacing; Eqs. (38)–(40)). The added dissipation that cures weak instabilities
at overlaps in other wave problems is on
[high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md).

**Fluid–solid Riemann problem and the interface projection.** The coupling
solves a linearized Riemann problem in the direction normal to the interface,
between the fluid's incoming acoustic characteristic and the solid's incoming
p- and s-wave characteristics (§3.1). Its solution gives the interface normal
velocity $v^I$ and normal traction $\tau^I$ as **impedance-weighted averages**
of the predicted fluid values ($v$, $\tau$) and solid values ($\bar v$,
$\bar\tau$, rotated to the fluid's interface frame and scaled by the area
ratio of Nanson's relation), with the fluid impedance $z=\rho a$, an effective
solid impedance $\bar z$, the predicted tangential solid traction
$\bar\tau_t$ and a coupling coefficient $\bar k$ (all page-local). The
*full projection* (§3.2, Eq. (28)) reads
$$\begin{aligned}
v^I&=\frac{\bar z\,\bar v+z\,v}{\bar z+z}+\frac{\tau-\bar\tau}{\bar z+z}+\frac{\bar k\,\bar\tau_t}{\bar z+z},\\
\tau^I&=\frac{\bar z^{-1}\bar\tau+z^{-1}\tau}{\bar z^{-1}+z^{-1}}+\frac{v-\bar v}{\bar z^{-1}+z^{-1}}-\frac{\bar z^{-1}\bar k\,\bar\tau_t}{\bar z^{-1}+z^{-1}},
\end{aligned}$$
with, for $\theta_{\mathrm p}$ the angle between the rotated p-wave
eigenvector and the interface normal and $\bar z_{\mathrm p}$, $\bar z_{\mathrm s}$
the scaled p- and s-wave impedances (page-local),
$$\bar z=\frac{\bar z_{\mathrm p}\bar z_{\mathrm s}}{\bar z_{\mathrm s}\cos^2\theta_{\mathrm p}+\bar z_{\mathrm p}\sin^2\theta_{\mathrm p}},\qquad\bar k=\frac{\sin\theta_{\mathrm p}\cos\theta_{\mathrm p}(\bar z_{\mathrm p}-\bar z_{\mathrm s})}{\bar z_{\mathrm s}\cos^2\theta_{\mathrm p}+\bar z_{\mathrm p}\sin^2\theta_{\mathrm p}}\qquad\text{(Eq. (27))}.$$
The *simplified projection* (Eq. (29)) drops $\bar\tau_t$, which is zero to
truncation-error level because zero tangential traction is enforced every
step, and replaces $\bar z$ by the linear p-wave impedance
$\bar\rho\bar c_{\mathrm p}$, $\bar c_{\mathrm p}=\sqrt{(\bar\lambda+2\bar\mu)/\bar\rho}$,
with $\bar\rho$ the solid's reference density and $\bar\lambda$, $\bar\mu$
its Lamé constants (page-local; not the registry's viscosities). The authors
justify it when the deformation gradient is a small perturbation of a
rotation, state that both projections have the same formal order because both
are linear combinations of the interface conditions, and use the simplified
one in all runs except the explicit comparisons, where the two are
indistinguishable (§3.2, §5.2, §6, Fig. 19).

The weighting decides which side controls the interface: for a heavy solid
($\bar z\gg z$) the interface follows the solid, for a very light solid it is
"determined by the fluid" (§1). The *traditional partitioned* (TP) scheme
imposes the solid velocity as the fluid's boundary condition and the fluid
traction as the solid's load, a one-sided Dirichlet–Neumann coupling that
Banks et al. relate to the one-sided Riemann problem of Farhat et al. (as
recalled, §1). The interface projection imposes no time-step restriction:
$\Delta t$ is the smaller of the fluid and solid time steps (§4.2).

**Procedure** (§4.3, Procedure 1): compute $\Delta t$; predict the interface
motion and regenerate the interface grids; update the overlapping-grid
connectivity; advance the fluid from the old to the predicted grid and the
solid on its static grid without interface conditions; project the interface
velocity and traction; apply the fluid and solid boundary conditions with the
projected values; correct the interface grids to the projected interface.
Interface ghost values come from the existing moving-slip-wall (fluid) and
traction-wall (solid) compatibility conditions, which, the authors state,
eases embedding the projection in existing partitioned solvers (§4.3).

**Stability and accuracy.** The density of the fluid is set to
$\rho_0=\gamma/\delta_\rho$ against a solid of unit density, with the
page-local ratio parameter $\delta_\rho=10$ (heavy solid), 1 (medium) and 0.1
(light). On a rotating elastic disk inside a fluid annulus, compared with a
1-D radially symmetric reference solution on a grid 10 times finer (§5.2,
Figs. 12–14), max-norm rates at $t=0.5$ are:

| solid | $\rho$ | $v_1$ | $v_2$ | $T$ | displacement | velocity | stress | TP scheme |
|---|---|---|---|---|---|---|---|---|
| heavy, $\delta_\rho=10$ | 2.01 | 2.02 | 2.03 | 2.01 | 2.39 | 2.20 | 2.48 | stable, rates within 0.01 |
| medium, $\delta_\rho=1$ | 1.89 | 1.89 | 1.90 | 1.89 | 2.39 | 2.20 | 2.49 | unstable |
| light, $\delta_\rho=0.1$ | 1.94 | 1.65 | 1.49 | 2.35 | 2.36 | 2.13 | 2.45 | unstable |

The full and simplified projections give identical tables (the light case
differs in one error ratio). The instability of the TP scheme for light
solids is the *added-mass instability* of partitioned coupling; the light
case "approaches an inviscid fluid with a free surface" (§5.2). On an elastic
piston with a manufactured solution, where the interface motion is
prescribed, the rates are 1.87–2.10 for all fluid and solid variables
(§5.1, Fig. 8); this test checks accuracy, not stability. See
[twilight-zone flow](/methods/twilight-zone-flow.md).

**Demonstrations.** A Mach-1.3 planar shock hits a light ($\bar\rho=0.1$)
tilted elliptical solid on four component grids (§6): neo-Hookean and rigid
solids translate and rotate significantly, while the linear-elastic model,
which assumes small deformation gradients, barely rotates; elastic solids
delay the bow shock relative to the rigid body by the elastic-wave transit
time. The finest grid has about 2.2 million points, only about 8,800 on the
two curvilinear grids, so the cost is dominated by the static Cartesian grids.
A neo-Hookean beam in a channel, loaded by a Mach-1.1 shock-driven inflow,
bends by about 40 % of its length (heaviest case) or bends over and starts to
recover (lightest case), with matching centrelines on the two finest grids
(§7, Figs. 22–23).

## Other coupled applications on overset grids

- Meakin & Suhs (1989) name the Body Dynamics Function of the moving-body
  cycle but prescribe all trajectories, calling it the "weak link"
  ([Meakin & Suhs (1989)](/sources/meakin-1989.md), §II, §IV); Noack (2005)
  couples a 6-DOF motion controller to SUGGAR and the flow solver through
  named pipes ([Noack (2005)](/sources/noack-2005.md), §VII). See
  [moving overset grids](/methods/moving-overset-grid.md).
- Chan (2009, §10–11) recalls OVERFLOW-D's 6-DOF dynamics with body contact
  detection and impact dynamics, and a CH-47 dual-rotor helicopter trimmed
  with coupled CFD and computational structural dynamics
  ([Chan (2009)](/sources/chan-2009.md)).
- Horne & Mahesh (2021) integrate 6-DOF rigid bodies in incompressible
  turbulent flow on unstructured overset meshes and time a freely falling
  sphere on GPUs ([Horne & Mahesh (2021)](/sources/horne-2021.md), §1,
  §4.2.3).
- Picard et al. (2021) list moving deformable structures crossing the overlap
  boundary and an immersed-boundary FSI extension as future work
  ([Picard et al. (2021)](/sources/picard-2021.md), §5).

## Flexible structures and freely moving bodies (2022 sources)

- [Delcour et al. (2022)](/sources/delcour-2022.md) couple a commercial finite-volume code and a beam model with quasi-Newton (IQN-ILS) strong coupling for a flexible cylinder in axial flow; the Chimera component mesh deforms with the cylinder, so large motions keep body-fitted boundary layers; water experiments are reproduced and air compressibility above inlet Mach 0.66 accelerates second-mode flutter (§3–§4).
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) couple freely falling cylinders strongly with the flow on moving overset grids: overset and single-grid fall velocities differ by about 0.2 % for one cylinder and at most 4 % for three (§3.4).
- [Zhao et al. (2022)](/sources/zhao-2022.md) compute particle sedimentation, a spinning ball and a self-propelled flapping foil, the body motion driven by the computed forces (§III).
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) compute a sedimenting cylinder (§6).

## Hydroelastic ships in potential flow

[Zhou et al. (2024)](/sources/zhou-2024.md) compute the hydroelastic response of flexible ships at zero forward speed with generalized modes of an Euler–Bernoulli beam in a potential-flow solver on overlapping curvilinear grids, validated against experiments and reference solutions on three cases; they derive both disputed forms of the hydrostatic stiffness of flexible modes and show the buoyancy terms equivalent for pure elastic motions (Abstract, Conclusions).

## Qualifications

- Banks et al. state that both projections "show the expected second-order
  accuracy for all three cases" (§5.2), while the light-solid fluid velocity
  rates are 1.65 and 1.49; the authors note that the error ratios of this
  case approach 4 under refinement.
- The rotating-disk test is radially symmetric, so the tangential-traction
  term of the full projection plays no role in it; the identity of the full
  and simplified tables there does not test that term.
- The rotating disk is said to be set into motion "by an initial angular
  velocity", with $\omega_0$ a "rotation rate parameter", while the printed
  initial condition gives a purely radial initial velocity and zero angular
  displacement (§5.2, p. 1053); the paper does not resolve which is meant.
- Printed slips in Banks et al. (2016):
  - the post-shock state of the Mach-1.3 shock is printed as
    $[\rho,v_1,v_2,p]=[1.516,0.5233,0,1.191]$ (§6). For $\gamma=1.4$ and an
    ambient state $\rho=p=1$ the normal-shock relations give $\rho=1.516$,
    $v_1=0.5233$ and $p=1+\tfrac{2\gamma}{\gamma+1}(M^2-1)=1.805$; the printed
    1.191 equals $p/\rho=1.805/1.516$, the temperature *(compiler check, not in
    the sources)*;
  - the static solid grid is printed on $[-2.75,0.75]\times[1.75,1.75]$, an
    interval of zero width in $x_2$ (§6);
  - §5.1 computes on grids "$j=2,\dots,5$" while the spacing $1/(10j)$ and the
    tabulated $h=1/20,\dots,1/160$ correspond to $j=2,4,8,16$;
  - the caption of Fig. 14 calls the $\delta_\rho=0.1$ table "medium solid",
    while its title says "light solid";
  - the conclusions abbreviate neo-Hookean as both "NE" and "NH".
- Neither source states the width or order of the inter-grid interpolation it
  uses (Banks et al. defer to earlier work; Henshaw & Schwendeman name a
  tensor-product Lagrange interpolant).

# Citations

- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §2 (Eqs. (4)–(5)); §3.4 (Fig. 6); §4.3 (predictor–corrector); §5 (Eq. (14)); §6.2.2 (Table 3, Fig. 13); §6.3.2; §7.2.
- [Banks et al. (2016)](/sources/banks-2016.md) — §1; §2; §3.1–3.2 (Eqs. (26)–(29)); §4.1; §4.2 (Eqs. (31), (38)–(40)); §4.3 (Procedure 1); §5.1 (Fig. 8); §5.2 (Figs. 12–14); §6 (Figs. 16–19); §7 (Figs. 22–23); §8.
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II BDF, §IV.
- [Noack (2005)](/sources/noack-2005.md) — §VII.
- [Chan (2009)](/sources/chan-2009.md) — §10, §11 (Fig. 9).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §1, §4.2.3.
- [Picard et al. (2021)](/sources/picard-2021.md) — §5.
- [Delcour et al. (2022)](/sources/delcour-2022.md) — §3–§4.
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §3.4.
- [Zhao et al. (2022)](/sources/zhao-2022.md) — §III.
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §6.
- [Zhou et al. (2024)](/sources/zhou-2024.md) — Abstract, Conclusions.
