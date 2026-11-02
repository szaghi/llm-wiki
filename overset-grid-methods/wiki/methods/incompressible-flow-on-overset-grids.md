---
type: Method
title: "Incompressible flow on overlapping grids"
description: "Henshaw's fourth-order method of lines for incompressible Navier–Stokes on curvilinear composite overlapping grids: velocity–pressure form with a pressure Poisson equation and the boundary condition div u = 0, ghost-point numerical boundary conditions, quartic interpolation, divergence damping, and fourth-order convergence on overlapping 2-D and 3-D grids."
status: established
aliases: [incompressible Navier–Stokes on composite grids, velocity–pressure formulation, pressure Poisson formulation, CGINS method, fourth-order incompressible overlapping-grid method]
tags: [incompressible, composite-grid, high-order, finite-difference, interpolation]
timestamp: 2026-11-02T11:28:00Z
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
