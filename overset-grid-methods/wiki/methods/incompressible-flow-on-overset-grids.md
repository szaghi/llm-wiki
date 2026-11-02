---
type: Method
title: "Incompressible flow on overlapping grids"
description: "Incompressible Navier–Stokes on overlapping grids: Henshaw's fourth-order velocity–pressure method with div u = 0 on the boundary, quartic interpolation and divergence damping; second-order finite-volume projection and projection–artificial-compressibility schemes; single-system versus Schwarz coupling of the grids; and the interpolation order the elliptic pressure needs."
status: established
aliases: [incompressible Navier–Stokes on composite grids, velocity–pressure formulation, pressure Poisson formulation, CGINS method, fourth-order incompressible overlapping-grid method, overset single system, overset additive Schwarz, overset Schwarz coupling]
tags: [incompressible, composite-grid, high-order, finite-volume, interpolation]
timestamp: 2026-11-02T14:53:00Z
---

# Incompressible flow on overlapping grids

[Henshaw (1994)](/sources/henshaw-1994.md) solves the incompressible
Navier–Stokes equations on curvilinear
[composite overlapping grids](/definitions/composite-overlapping-grid.md) in
2-D and 3-D, fourth-order accurate in space. The scheme is a method of lines
in **velocity–pressure form**. The velocity is advanced explicitly by the
momentum equations, and at every stage the pressure is recomputed from a
Poisson equation. The extra boundary condition that closes this system is
$\nabla\cdot\mathbf u=0$ on $\partial\Omega$. The component grids are coupled
by quartic Lagrange [interpolation](/methods/inter-grid-interpolation.md)
with two receptor lines. The elliptic and composite-grid machinery is that of
[CMPGRD](/software/cmpgrd.md) and of
[Chesshire & Henshaw (1990)](/sources/chesshire-1990.md). The pressure $p$
on this page is kinematic (divided by density).

Two later sources take a second-order finite-volume route for wind-energy and
particle-laden turbulent flows.
[Sharma et al. (2021)](/sources/sharma-2021.md) use an incremental
approximate pressure projection in the node-centred code Nalu-Wind, with
TIOGA assembling the overset meshes, and study how the interpolation order
and the coupling of the per-mesh linear systems affect accuracy.
[Horne & Mahesh (2021)](/sources/horne-2021.md) replace the projection by a
coupled projection–artificial-compressibility scheme in a cell-centred
unstructured code on GPUs, so that fringe values can be injected into the
pressure equation. Their sections below follow Henshaw's.

## Formulations and the pressure boundary condition

The **velocity–divergence form** is (Eq. (1))
$$\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u+\nabla p=\nu\nabla^2\mathbf u+\mathbf f,\quad \nabla\cdot\mathbf u=0\ \text{in }\Omega;\qquad B(\mathbf u,p)=0\ \text{on }\partial\Omega,$$
with $n_d$ physical boundary conditions $B$. Taking the divergence of the
momentum equation gives the **velocity–pressure form** that is discretized
(Eq. (2)):
$$\begin{aligned}&\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u+\nabla p=\nu\nabla^2\mathbf u+\mathbf f,\qquad \nabla^2p+\sum_{m=1}^{n_d}\nabla u_m\cdot\partial_{x_m}\mathbf u=\nabla\cdot\mathbf f\quad\text{in }\Omega,\\ &B(\mathbf u,p)=0,\qquad \nabla\cdot\mathbf u=0\quad\text{on }\partial\Omega .\end{aligned}$$

Henshaw (§1.2) states, without proof ("it is not hard to show"), that with
$\nabla\cdot\mathbf u=0$ on the boundary the velocity–pressure form is well
posed and consistent with, and equivalent to, the velocity–divergence form
for smooth solutions. Using instead the normal component of the momentum
equation as the pressure condition (the choice Gresho & Sani recommend, as
recalled by Henshaw) does not make the forms equivalent. Nothing then stops
the divergence from being nonzero inside the domain if it is nonzero on the
boundary, and that condition alone leaves the system under-determined, as
recalled from Strikwerda. Henshaw reads the formulation of Karniadakis et al.
as imposing $\nabla\cdot\mathbf u=0$ implicitly: they write
$\nabla^2\mathbf u=\nabla(\nabla\cdot\mathbf u)-\nabla\times\nabla\times\mathbf u$
and set $\nabla(\nabla\cdot\mathbf u)=0$. Henshaw states that on staggered
grids the condition occurs naturally.

In Henshaw's scheme the normal momentum equation is still applied on the
boundary, but as a *numerical* boundary condition. It supplies the Neumann
condition for the discrete pressure equation.

## Discretization

**Grids and differences** (§2). Each component grid $G_k$ is the image of the
unit cube under $\mathbf d_k$. Indices run two lines beyond the boundary
(ghost points) to carry fourth-order centred differences. Derivatives are
formed in $\mathbf r$ and mapped by the chain rule with the metric
$\partial r_n/\partial x_m$ supplied by CMPGRD (non-conservative form). With
$E_{\pm m}$ the shifts in direction $m$, the operators are
$$\partial_{r_m}u\approx\frac{(-E_{+m}^2+8E_{+m}-8E_{-m}+E_{-m}^2)\,u_{\mathbf i}}{12\,\Delta r_m},\qquad \partial^2_{r_m}u\approx\frac{(-E_{+m}^2+16E_{+m}-30+16E_{-m}-E_{-m}^2)\,u_{\mathbf i}}{12\,\Delta r_m^2},$$
assembled into the fourth-order operators $\nabla_4$, $\nabla_4\cdot$ and
$\nabla^2_4$. The semi-discrete equations at interior points are
$$\tfrac{d}{dt}\mathbf u_{\mathbf i}+(\mathbf u_{\mathbf i}\cdot\nabla_4)\mathbf u_{\mathbf i}+\nabla_4p_{\mathbf i}-\nu\nabla^2_4\mathbf u_{\mathbf i}-\mathbf f_{\mathbf i}=0,\qquad \nabla^2_4p_{\mathbf i}+\sum_m\nabla_4u_{m,\mathbf i}\cdot D_{4x_m}\mathbf u_{\mathbf i}-\nabla_4\cdot\mathbf f_{\mathbf i}=0,$$
where $D_{4x_m}$ (page-local) is the fourth-order $x_m$-derivative.

**Numerical boundary conditions** (Eq. (3), §2). Consider a Dirichlet
velocity condition $\mathbf u=\mathbf u_B$. At each boundary point the scheme
imposes:
- $\mathbf u_{\mathbf i}=\mathbf u_B$;
- $\nabla_4\cdot\mathbf u_{\mathbf i}=0$;
- the fourth-order normal derivative of $\nabla_4\cdot\mathbf u_{\mathbf i}$
  set to zero;
- the momentum equation;
- the pressure equation.

On the second ghost line, the tangential velocity and the pressure are
extrapolated, $\mathbf t_\mu\cdot(E_{+m}-1)^4\mathbf u_{\mathbf i}=0$ and
$(E_{+m}-1)^4p_{\mathbf i}=0$, with undivided differences and tangents
$\mathbf t_\mu$, $\mu=1,\dots,n_d-1$. In 3-D this gives 12 equations for the
12 unknowns at a boundary point and its two ghosts. Henshaw (§1.1) states
that a second-order version exists that does not need these extra
conditions. At edges of 3-D grids the ghost values come from a Taylor
formula whose mixed second derivative is fixed by
$\partial_{r_m}(\nabla\cdot\mathbf u)=0$, $m=1,2$, and a diagonal
sixth-difference extrapolation of the edge-parallel velocity; at vertices a
Taylor formula with only tangential second derivatives is used (§4.2,
Eqs. (15)–(17)).

**Time stepping** (§3, Eqs. (5)–(8)). Each explicit stage (Runge–Kutta or
multistep) runs in four steps:
1. update interior velocities;
2. solve the boundary and ghost conditions for the velocity, using a pressure
   $p^*$ extrapolated in time in the tangential momentum condition (stated to
   be harmless "from the theory" of the companion stability paper);
3. solve the pressure Poisson equation, with the Neumann condition from the
   normal momentum equation,
   $\mathbf n\cdot\nabla_4p_{\mathbf i}=-\mathbf n\cdot\big(\partial_t\mathbf u_{\mathbf i}+(\mathbf u_{\mathbf i}\cdot\nabla_4)\mathbf u_{\mathbf i}-\nu\nabla^2_4\mathbf u_{\mathbf i}-\mathbf f\big)$,
   and extrapolation on the second ghost line;
4. form $\nabla p$ and the new right side.

On a grid orthogonal to the boundary, the ghost-point equations decouple
point by point. On non-orthogonal grids they are iterated in correction mode,
which converges quickly unless the grid is very skewed (§4.3). The runs use a
second-order Adams predictor–corrector.

**Singular pressure system** (§3, Eqs. (9)–(14)). With Neumann data the
discrete matrix $\mathsf A$ is singular: the pressure is fixed only up to a
constant. The discrete form of the compatibility condition
$\int_\Omega f_p\,d\mathbf x=\int_{\partial\Omega}g\,ds$ holds only to fourth
order. Here $f_p$ and $g$ are page-local names for the right side and the
Neumann data of $\nabla^2p=f_p$, $\partial_np=g$ (Eq. (10)). Henshaw therefore solves the bordered system
$$\begin{bmatrix}\mathsf A&\mathbf 1\\ \mathbf 1^T&0\end{bmatrix}\begin{bmatrix}\mathbf p\\ \varsigma\end{bmatrix}=\begin{bmatrix}\mathbf b\\ \beta\end{bmatrix},$$
where $\mathbf 1$ is the right null vector, $\mathbf b$ the right side and
$\beta$ the pressure level. The multiplier $\varsigma$ (page-local) measures
the compatibility violation and is expected to be $O(h^4)$. The available
solvers are sparse direct (Yale), bi-CG-squared or GMRES, and composite-grid
multigrid. Chesshire & Henshaw (1990) report that multigrid convergence on
composite grids is "almost as good" as on a single grid (§5.5, as recalled
there from Henshaw & Chesshire's multigrid paper).

**Inter-grid coupling** (§4.1). Receptors are filled by triquartic Lagrange
interpolation ($q=5$, $5\times5\times5$ stencils) in the donor's unit-cube
coordinates, with two receptor lines. The order is chosen by the criterion
of Chesshire & Henshaw; see
[interpolation order and overlap requirements](/results/interpolation-order-requirement.md).

## Discrete divergence and its damping

The discrete divergence (page-local symbol
$\vartheta_{\mathbf i}=\nabla_4\cdot\mathbf u_{\mathbf i}$) obeys a discrete
convection–diffusion equation (§4.4):
$$\tfrac{d}{dt}\vartheta_{\mathbf i}+(\mathbf u_{\mathbf i}\cdot\nabla_4)\vartheta_{\mathbf i}-\nu\nabla^2_4\vartheta_{\mathbf i}=\mathcal T_{\mathbf i},\qquad \vartheta_{\mathbf i}=0\ \text{and its normal derivative zero on }\partial\Omega .$$
The forcing $\mathcal T_{\mathbf i}=O(h^4)$ (page-local) collects the
commutation errors of the discrete operators. The interpolation conditions
are a further source of divergence. Henshaw adds a damping term to the
pressure equation,
$$\nabla^2_4p_{\mathbf i}+\sum_m\nabla_4u_{m,\mathbf i}\cdot D_{4x_m}\mathbf u_{\mathbf i}-\nabla_4\cdot\mathbf f_{\mathbf i}-C_d\,\nu\,\mathcal V_{\mathbf i}\,\vartheta_{\mathbf i}=0,\qquad \mathcal V_{\mathbf i}=\sum_m\Delta x_{m,\mathbf i}^{-2},$$
which adds $-C_d\nu\mathcal V_{\mathbf i}\vartheta_{\mathbf i}$ to the
divergence equation. The coefficient $C_d$ is usually 1. The damping reduces
the divergence but cannot make it exactly zero. Henshaw contrasts it with
projection and MAC methods, as recalled there, which add a term
$\propto\vartheta_{\mathbf i}/\Delta t$ and make the new velocity exactly
divergence-free.

Initial data are projected: $\mathbf u_0=\mathbf u_I+\nabla\phi$ with
$\nabla^2\phi=-\nabla\cdot\mathbf u_I$ and $\mathbf n\cdot\nabla\phi=0$, using
the pressure operator. For non-smooth data, smoothing and projection
alternate until the divergence stops decreasing (§4.5).

## Projection and artificial-compressibility schemes

**Incremental approximate projection** (Sharma et al. 2021, §2,
Eqs. (3)–(6)). Each step runs $K$ Picard iterations ($K=1$ for linear and
$K=3$ for nonlinear problems "out of experience", §4). Iteration $k$ solves,
with $\mathsf A_{\mathrm u}$ the linearized momentum operator (time derivative,
diffusion, advection; not the pressure matrix $\mathsf A$ above), $\mathbf u^*$ the intermediate velocity, $\delta p$ the
pressure increment and $\gamma_{\mathrm b}$ the variable-step BDF2
coefficient (page-local symbols),
$$\begin{aligned}&\mathsf A_{\mathrm u}(\mathbf u^*_{k+1}-\mathbf u_k)=\mathbf f-\mathsf A_{\mathrm u}\mathbf u_k-\nabla p_k,\\ &-\tfrac{\Delta t}{\gamma_{\mathrm b}}\nabla^2\delta p_{k+1}=-\nabla\cdot\big(\rho\,\mathbf u^*_{k+1}+\tfrac{\Delta t}{\gamma_{\mathrm b}}\nabla p_k\big)+\tfrac{\Delta t}{\gamma_{\mathrm b}}\nabla^2p_k,\\ &\mathbf u_{k+1}=\mathbf u^*_{k+1}-\tfrac{\Delta t}{\gamma_{\mathrm b}\rho}\nabla\delta p_{k+1}.\end{aligned}$$
The projection is approximate: the discrete $\nabla\cdot\nabla$ differs from the
discrete $\nabla^2$. For a constant step $\gamma_{\mathrm b}=3/2$ *(compiler
check, not in the sources)*. Time stepping is implicit BDF2 at a maximum CFL
number of 1. Sharma et al. keep the density $\rho$; their tests take
$\rho=1$. The momentum step is parabolic but advection-dominated, the
pressure step elliptic, which is why the two need different interpolation
orders (below).

**Projection combined with artificial compressibility** (Horne & Mahesh 2021,
§3.1, Eqs. (2)–(8)). Starting from a Crank–Nicolson projection, Horne &
Mahesh take all predicted terms at the new level and add the material
derivative of pressure to the continuity equation:
$$\frac{\mathbf u^{n+1}-\mathbf u^n}{\Delta t}+\tfrac12\big(\mathcal C^{n+1}+\mathcal C^n\big)-\tfrac12\big(\mathcal L^{n+1}+\mathcal L^n\big)=-\nabla p^{n+1},\qquad \epsilon_{\mathrm{ac}}\frac{dp}{dt}+\nabla\cdot\mathbf u^{n+1}=\Delta t\,\nabla^2p^{n+1},$$
with $\mathcal C$, $\mathcal L$ the discrete convective and viscous terms (page-local; $\mathcal V_{\mathbf i}$ above is Henshaw's spacing factor) and
$\epsilon_{\mathrm{ac}}$ the artificial-compressibility coefficient
(page-local). They choose $\epsilon_{\mathrm{ac}}=\Delta t$, after Shen's
analysis as recalled there, which proves $O(\Delta t)$ accuracy of the pure
artificial-compressibility scheme with this choice; the added term is then
$O(\Delta t)$ in the continuity equation (Eq. (7)). Velocity and pressure are
solved at the same level, so there is no splitting error. Further stated
properties: the condition number falls from $O(\Delta x^{-2})$ (projection) to
$O(\Delta t/\Delta x^2)$; the pressure Laplacian removes odd–even decoupling on
the collocated grid and damps spurious compressible waves; and the pressure
boundary condition is the normal momentum balance,
$-\partial_np^{n+1}=\mathbf n\cdot\big((\mathbf u^{n+1}-\mathbf u^n)/\Delta t+\mathcal C^{n+1}-\mathcal L^{n+1}\big)$
(Eq. (8)), instead of the $\partial_np=0$ of the projection method, which the
authors say limits pressure accuracy to $O(\Delta t^{1/2})$ on general meshes
(as recalled there). As recalled there, artificial compressibility on overset
grids had previously needed dual time stepping (Tang et al.). Laplacians use
a two-point flux approximation with a primal–dual correction for skewed
cells, which keeps the system symmetric (§3.2, Eq. (10)).

## Coupling the component grids

**Interpolation as boundary data for the pressure.** Henshaw (1994) solves
the pressure equation on the whole composite grid with the composite-grid
sparse and multigrid solvers (above). Horne & Mahesh (§3.2) earlier enforced pressure
continuity across overlapping meshes by a penalty method, which needed
all-to-all stencil weights and tuning; with $\epsilon_{\mathrm{ac}}\,dp/dt$ in
the continuity equation they inject the reconstructed fringe values directly
into the pressure equation and the system stays solvable by plain iterative
solvers, with no penalty error in the divergence near overset boundaries.

**Single system versus Schwarz iteration** (Sharma et al. 2021, §3.2,
Algorithms 1–2). In the overset single system (OSS) the fringe interpolation
equations are constraint rows of one linear system over all meshes. In
overset additive Schwarz (OAS) each mesh's system is solved separately with
field-point rows only, and the fringe values are then updated from the other
meshes, Jacobi fashion, over $n_{\mathrm{oc}}$ "overset corrector" iterations
(page-local). The authors prefer OAS for parallelism across meshes, for using
different solvers per mesh, and because constraint rows add noise to
algebraic-multigrid coarsening (stated without a test). The
[explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
page relates the two to Chesshire & Henshaw's terms. Findings:
- *Elliptic proxy* (diffusion, quadratic-reproducing RBF interpolation): OAS
  needs a tight inter-iteration tolerance, $10^{-5}$, to match the OSS error,
  and then $n_{\mathrm{oc}}=19$, 47, 90 and 153 for $h=0.2$, 0.1, 0.05 and
  0.025 (Table 1). The counts did not change with Lagrange interpolation. With
  GMRES and a weak ILU preconditioner, doing one Krylov iteration per OAS solve
  instead of converging each lowers the cost, but OSS stays cheapest in Krylov
  iterations (Figs. 21–22).
- *Hyperbolic proxy* (linear advection, linear interpolation): two corrector
  iterations per Picard iteration match OSS and keep second order (Fig. 23).
  The authors state that with explicit time stepping one may suffice.
- *Navier–Stokes, cylinder at $Re=200$*: extra Picard iterations, which
  repeat the projection, are more effective than extra corrector iterations,
  because repeated pressure solves with an uncorrected intermediate velocity
  introduce global pressure errors; split-operator errors dominate the
  inter-mesh errors. Two Picard iterations with one corrector iteration give
  drag, lift and Strouhal statistics within 1% of OSS, even on the coarsest
  mesh (§4.3.3, Figs. 30–31).

**Interpolation order.** For an elliptic equation with the fringe gap
shrinking with $h$, linear interpolation loses second order and quadratic
keeps it; linear suffices for advection (Sharma et al., §4.1). With linear
interpolation a decaying Taylor vortex keeps second order at cell Reynolds
number about 400 and loses it at about 1 (§4.3.1, Fig. 25). Sharma et al.
therefore "strongly recommend" higher-order interpolation for incompressible
flow, because the pressure equation is elliptic and low-Reynolds structures
occur, yet conclude that for advection-dominated engineering problems linear
interpolation with OAS (2–4 Picard iterations, one corrector iteration) gives
quantities within 1% of OSS (§5). See
[interpolation order and overlap requirements](/results/interpolation-order-requirement.md).

## Verification and demonstrations

- **Twilight-zone tests** on a square, a rotated square, an overlapping
  circle, a cube and a two-patch spherical shell give $\sigma\approx4$ for
  velocity and pressure and 4.2–5.8 for the divergence. See
  [twilight-zone flow](/methods/twilight-zone-flow.md).
- **Wannier flow** (§5.1.1, Table IV, Fig. 2). Wannier's exact Stokes
  solution for a cylinder near a wall moving at speed $U$ (as recalled by
  Henshaw) is computed on two overlapping grids, $(27^2)\cup(9\times43)$ and
  $(53^2)\cup(17\times85)$. The velocity error falls from
  $7.3\times10^{-4}$ to $5.6\times10^{-5}$ ($\sigma=3.7$), and the maximum
  divergence from $8.5\times10^{-3}$ to $3.8\times10^{-4}$ ($\sigma=4.5$).
  The values of $U$, the radius and the wall distance are not printed.
- **Cylinder at $Re=100$** (§5.1.2, Figs. 3–5, Table V). Radius 1/2, domain
  $[-2.5,15]\times[-3.5,3.5]$, $\nu=1/100$, 14,581 points. A Kármán street
  appears after $t\approx40$, and max divergence over max vorticity stays
  below about $3\times10^{-3}$. Each step takes 1.5 s on an IBM RS/6000-530:
  pressure solve 27%, explicit interpolation 2%, Adams predictor–corrector
  43%, boundary conditions 7%. No Strouhal number or drag is reported. See
  [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md).
- **Sphere in a channel** (§5.2, Fig. 6, Table VIII). Sphere of radius 1 in
  $[-2.2,2.2]^3$, three component grids $(35^3)\cup2(25^2\times9)$,
  $\nu=0.05$, 10,728 interpolation points. Each step takes 45.0 s: GMRES
  pressure solve 42%, implicit interpolation 17%.
- **Taylor vortices.** Sharma et al. (2021) (§4.3.1) translate a decaying
  Taylor vortex across an overset mesh (OSS, linear interpolation; second
  order at low viscosity, degraded at high viscosity). Horne & Mahesh (2021)
  (§4.2.1, Figs. 13–14) run a Taylor–Green vortex in a triply periodic unit box
  with an empty overset patch half the box size, rotated 25° about each axis,
  about 30% overlap: second order in velocity and pressure, errors "several
  orders of magnitude" below their earlier predictor–corrector scheme, and
  total kinetic energy following the analytic decay up to $Re=10^9$. See
  the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).
- **Cylinders** (Sharma et al. 2021, §4.3.3–4.3.4). A stationary cylinder at
  $Re=200$ on a near-body O-mesh and a Cartesian background ($30\times20\times0.1$
  box, OSS, linear interpolation) gives drag and Strouhal number converging
  under refinement and agreeing with the literature; a rotating cylinder at
  rotation rate 3 (moving near-body mesh) sheds a single vortex and its lift
  converges in space and time. OAS with a couple of Picard iterations and one
  corrector iteration is within 1% of OSS in both. See
  [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md).
- **Sphere at $Re=3700$** (Horne & Mahesh 2021, §4.2.2): 12 million cells,
  spacing $0.015D$, drag coefficient 0.392 (reference DNS 0.394), wake length
  $2.2D$ and Strouhal number 0.22, within 1–5% of the references; on one node
  with one to four V100 GPUs the speed-up over the authors' earlier CPU method
  is 8x–56x, depending on the GPU count and cell loading (§4.2.2, Fig. 16). See
  [flow past a sphere](/benchmarks/flow-past-sphere.md) and
  [parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md).

## Qualifications

- **Equivalence not proved here.** The equivalence of the two formulations
  under $\nabla\cdot\mathbf u=0$ is stated, not proved. Stability and accuracy
  are deferred to the companion paper by Henshaw, Kreiss & Reyna (as recalled
  in §1). Henshaw places the pressure-boundary-condition question against
  Gresho & Sani's recommendation (as recalled by Henshaw). This page
  records it as Henshaw's argued position, not as a proved result.
- **Space order only.** Fourth order is spatial. The computations use a
  second-order time integrator at small $\Delta t$.
- **Non-conservative.** The interpolation is non-conservative and acts as a
  divergence source (§4.4); see
  [conservative overset interface](/methods/conservative-overset-interface.md).
  Sharma et al. (2021) (§1) state that the lack of conservation does not
  degrade incompressible solutions, which have no shocks, though mass
  conservation may matter for the pressure-correction step; Horne & Mahesh
  (2021) do not discuss mass conservation of the injected pressure.
- **Divergence of the coupled scheme.** Horne & Mahesh's continuity equation
  carries an $O(\Delta t)$ term, so the velocity is divergence-free only to
  that order; second order is shown with space and time refined together at
  fixed CFL, with no separate temporal test.
- **Corrector-iteration growth.** Sharma et al. (§4.2.1) state that the OAS
  iteration count grows as $O(h^{-2})$ (Fig. 19). Their own Table 1 at
  tolerance $10^{-5}$ gives $153/19=8.05$ over an eightfold refinement,
  exponent 1.00, with successive exponents 1.31, 0.94 and 0.77 *(compiler
  check, not in the sources)*. The table indicates $O(h^{-1})$ or slower.
- **Printed update signs** *(compiler checks, not in the sources)*. Sharma
  et al.'s Algorithms 1–2 print $\boldsymbol\phi_{k+1}=\boldsymbol\phi_k-\Delta\boldsymbol\phi_{k+1}$
  with residual $\mathbf b-\mathsf A\boldsymbol\phi_k$ and
  $\mathsf A\Delta\boldsymbol\phi=\mathbf r$; Horne & Mahesh's Algorithm 1
  prints $r=Ax-b$, $Ae=r$, $x=x+e$. In both, one sign must flip for the
  iteration to converge.
- **Printed slips in Henshaw (1994):**
  - The second-difference operator is printed with denominator
    $24(\Delta r_m)^2$. Applied to $r^2$ this gives 1 instead of 2, so the
    denominator must be $12(\Delta r_m)^2$, as written above.
  - In the edge formula Eq. (17), every second-order Taylor coefficient is
    printed at half its value. The vertex formula on the same page is
    correct.
  - Eq. (7) prints $\nabla_4\mathbf u$ for the viscous term, where §2 and
    §4.3 have the Laplacian.
  - The sphere case is given 47,550 active points in the text and 17,550 in
    Table VIII.
  - In the Wannier parameters, lowercase $s$ is printed for $S$, and $D$
    denotes both the wall distance and the constant $-U$.

# Citations

- [Henshaw (1994)](/sources/henshaw-1994.md) — §1.1–1.2 (Eqs. (1)–(3), pressure boundary condition; Gresho & Sani, Strikwerda, Karniadakis et al. as recalled), §2 (Eq. (4), differences, numerical boundary conditions), §3 (Eqs. (5)–(14)), §4.1–4.5 (Eqs. (15)–(17)), §5 (Tables I–VIII, Figs. 1–6).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §5.1 (mapping method), §5.3 (interpolation order), §5.5 (CGEL, CGMG multigrid rates).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1, §2 (Eqs. (3)–(9)), §3.2 (Algorithms 1–2), §4.1–4.2 (Table 1, Figs. 10–23), §4.3 (Figs. 25–34), §5.
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §3.1 (Eqs. (2)–(8); Shen, Tang et al. as recalled), §3.2 (Eq. (10), injection), §3.3 (Algorithm 1), §4.2.1–4.2.2 (Figs. 13–18, Table).
