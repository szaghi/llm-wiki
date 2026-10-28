---
type: Property
title: "Geometric conservation law and free-stream preservation"
description: "On curvilinear grids a discretization preserves a uniform flow only if its discrete metric terms satisfy the metric identities, and on moving grids a temporal identity too; the sources meet this geometric conservation law with curl-form DGSEM and flux-reconstruction metrics, conservative finite-difference and gas-kinetic metrics, moving-grid flux reconstruction and moving-mesh DGSEM, and note curved elements as an aliasing source."
status: established
aliases: [GCL, geometric conservation law, free-stream preservation, freestream preservation, metric identities, discrete metric identities]
tags: [dg, gas-kinetic, flux-reconstruction, high-order, compressible, implicit-les]
timestamp: 2026-10-28T17:00:00Z
---

# Geometric conservation law and free-stream preservation

When a conservation law $\partial_tU+\nabla\cdot F=0$ is solved on a
curvilinear grid, each element or cell is the image of a reference
(computational) element under a map $\boldsymbol x(\boldsymbol\xi)$ with
Jacobian determinant $\mathcal J$ (registry §11), and the equation is
transformed to
$$\mathcal J\,\partial_tU+\sum_{i=1}^{3}\frac{\partial}{\partial\xi^i}\big(\mathcal J\boldsymbol a^i\cdot F\big)=0,$$
with $\mathcal J\boldsymbol a^i$ the contravariant (metric) vectors (Krais et
al. 2021, §3.1, Eqs. 5–7; [Kurz et al. 2025](/sources/kurz-2025.md), §2.2,
Eqs. 11–13; page-local symbols, the registry's $\xi$, $\xi_i$ are reference
coordinates and nodes). A uniform state $U=\mathrm{const}$ has a constant
physical flux, so it remains a solution of the transformed equation only if
$$\sum_{i=1}^{3}\frac{\partial(\mathcal J a^i_n)}{\partial\xi^i}=0,\qquad n=1,2,3,$$
the **metric identities** *(compiler check, not in the sources: with $F$
constant the flux term reduces to $\sum_n F_n\sum_i\partial(\mathcal J a^i_n)/\partial\xi^i$;
the sources state only the requirement)*. A discretization in which the discrete metric terms
satisfy the discrete version of these identities is **free-stream
preserving**; the requirement is called the **geometric conservation law
(GCL)**. The sources below meet it in high-order
[LES](/definitions/large-eddy-simulation.md) and
[DNS](/definitions/direct-numerical-simulation.md) codes on curved and
stretched grids.

## DGSEM: curl-form metric terms

For the [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md),
[Krais et al. (2021)](/sources/krais-2021.md), §3.1, Eq. (4), compute the
metric terms in the **curl form**
$$\mathcal J a^i_n=-\hat{\boldsymbol x}_i\cdot\nabla_\xi\times\big(x_l\nabla_\xi x_m\big),\qquad i,n=1,2,3,\quad (n,m,l)\ \text{cyclic},$$
($\hat{\boldsymbol x}_i$ the Cartesian unit vector, page-local) and state,
citing Kopriva, that it satisfies the metric identities discretely, which
free-stream preservation on curved meshes requires. The same curl form is
Eq. (11) of the GPU code [GALÆXI](/software/galaexi.md) (Kurz et al. 2025,
§2.2), which keeps [FLEXI](/software/flexi.md)'s discretization.
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §3, use the
conservative Kopriva form for the same reason, and
[Morsbach et al. (2024)](/sources/morsbach-2024.md), §2, obtain free-stream
preservation in DLR's TRACE DGSEM by mapping the equations to the reference
element following Kopriva and Gassner (2016).

## Flux reconstruction: cross-product against curl-form metrics

[Witherden et al. (2025)](/sources/witherden-2025.md), §3.4, Fig. 7,
explain why [PyFR](/software/pyfr.md) v2.0.3 abandoned the cross-product
metric of its first release: on curved grids the cross-product metric has
a polynomial order twice that of the shape function, so truncation and
aliasing errors can leave the divergence of the approximated metric
non-zero and free-stream preservation is lost. The conservative metric
(Kopriva; Abe et al., as cited) builds the metric terms "as the curl of the
function", divergence-free irrespective of the approximation error. Their Fig. 7 shows a free
stream on cubically curved tetrahedra at $N=2$ with both metrics, as a
visual comparison without error norms. For straight-sided (linear)
elements the code computes the metrics on the fly from the $3\times8=24$
vertex terms, instead of storing $3^2\times125=1125$ terms for a hexahedron
at $N=4$, to save memory bandwidth (§3.4). The condition under which
Vermeire (2024) keeps cross-product metrics free-stream preserving
(mapping degree not above the solution degree, Gauss points, DG-recovering
correction) is below.

## Finite volumes from discrete grid points: the curvilinear gas-kinetic scheme

[Cao et al. (2024)](/sources/cao-2024.md) extend the
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md) to
meshes given only by discrete points (HGKS-cur). Their metric terms are the
Jacobian-scaled cofactors of the map, e.g. for the first computational
direction (§2.1, Eq. 5; $(\xi,\eta,\zeta)$ the computational coordinates,
page-local, not the Kolmogorov length or input features; subscripts
derivatives; the hat marks a metric term, not the test filter)
$$\hat\xi_x=y_\eta z_\zeta-z_\eta y_\zeta,\qquad \hat\xi_y=z_\eta x_\zeta-x_\eta z_\zeta,\qquad \hat\xi_z=x_\eta y_\zeta-y_\eta x_\zeta,$$
and cyclically for $\eta$ and $\zeta$. To satisfy the GCL they (§2.3):

1. compute the grid derivatives at the grid points with fourth-order central
   differences, e.g.
   $(\boldsymbol x_\xi)_{ijk}=\frac{1}{12\Delta\xi}\big[8(\boldsymbol x_{i+1,j,k}-\boldsymbol x_{i-1,j,k})-(\boldsymbol x_{i+2,j,k}-\boldsymbol x_{i-2,j,k})\big]$
   (Eq. 10);
2. evaluate the metric terms in a **symmetric conservative form**, a
   half-sum of derivatives of products of coordinates and grid derivatives
   (Eq. 11, "to preserve the GCL", citing Deng et al. 2011 and Xu et al.
   2016);
3. interpolate them dimension by dimension to the two Gauss points of each
   face with cubic Lagrange formulae;
4. reconstruct, with fifth-order [WENO](/methods/weno-scheme.md) in
   computational space, the cell-integrated Jacobian and the
   Jacobian-weighted conservative variables, and recover point values as
   $Q=(\mathcal JQ)/\mathcal J$ ($Q$ the conservative variables,
   page-local).

**Test.** A uniform state $\rho=p=u=v=w=1$ on two sinusoidally perturbed
meshes of $10^3$ to $160^3$ cells keeps $L^1$ errors at $O(10^{-15})$ to
$O(10^{-14})$ (6.2119E-15 at $10^3$ to 4.6088E-14 at $160^3$ on mesh 1),
"machine zero", so "the geometric conservation law is well preserved"
(§3.1, Table 3). The same meshes give fourth- to fifth-order convergence for
an advected density wave (orders 4.03 to 4.65, Tables 1–2). The scheme is
then used as [implicit LES](/definitions/implicit-les.md) of a compressible
[channel](/benchmarks/turbulent-channel-flow.md) and of a
[periodic hill](/benchmarks/periodic-hill.md) whose mesh is built from
discrete bottom-wall points (§3.3–3.4).

## Finite differences: metrics with the flux scheme

[Ma et al. (2022)](/sources/ma-2022.md), §2, Eqs. (1)–(2), solve the
compressible equations in curvilinear coordinates with a weighted compact
nonlinear finite-difference scheme (Jacobian-scaled conservative
variables and transformed fluxes, page-local as above) and compute the
grid metrics "with the same scheme as the flux derivatives" so that the
geometric conservation law is satisfied, citing Deng et al. (2011) and a
second GCL study (refs. 35–36). They print no free-stream test; their
implicit LES of a cylinder, the T106A
[turbine cascade](/benchmarks/turbine-cascade.md) and an open cavity run
on curvilinear block-structured grids (§3). The same Deng et al. (2011)
is one of the two works Cao et al. (2024) cite for their symmetric
conservative form above. [Wu et al. (2023)](/sources/wu-2023-b.md), §1,
§2.2.1, state that the fourth-order WCNS of the multi-block structured
code PHengLEI satisfies the geometric conservation law (citing two GCL
works) and run it on the curvilinear grids, up to 27 million cells, of
the [30P30N high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md);
they print neither the metric form nor a free-stream test. The scheme is
on [weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md).
The same statement, with the same two citations, returns in the group's
SATES-σ paper, [Wu et al. (2024)](/sources/wu-2024.md), §2.3, whose
PHengLEI runs use the linear fourth-order WCNS on multi-block grids of a
supercritical cylinder and of the 30P30N airfoil (12.8 and 26.4 million
cells); again no metric form or free-stream test is printed. The group's
smooth-TENO paper, [Wu et al. (2024b)](/sources/wu-2024-b.md), §I, lists
"good freestream and vortex preservation on curvilinear grids" among the
advantages of WCNS over finite-difference WENO and its applicability to
complex grids "when satisfying the GCL" (citing its refs. 26, 27 and 40); its
PHengLEI runs (30P30N airfoil, supersonic base flow) again print neither
the metric form nor a free-stream test.

## Curved elements as a source of aliasing

[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md), §2.2, Eqs. (19)–(21),
note a second effect of the element map in high-order
[flux reconstruction](/methods/flux-reconstruction.md): a non-constant,
non-linear isoparametric Jacobian is a "geometrical-aliasing source",
besides the non-linearity of the equations. They test their
[modal filters](/methods/explicit-modal-filtering.md) on a
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$
whose grid points are displaced sinusoidally,
$x'=x+(l/n_x)A\sin(k_g\pi y/l)\sin(k_g\pi z/l)$ and cyclically, with
$k_g=4$, $A=0.4$, $l=2\pi$ ($n_x$ elements per direction; all page-local,
after Abe et al. and Trojak et al., cited), and find the results
similar to those on the undistorted mesh (§4.3, Eqs. 50–52,
Figs. 15–18). The test addresses stability and accuracy of the filtered
scheme on curved elements, not free-stream preservation.

The same group's incompressible flux-reconstruction implicit LES,
[Vermeire (2024)](/sources/vermeire-2024.md), §3, Eqs. (8)–(9), maps each
element with a polynomial of degree $N_m$ (page-local, the source's $p_m$;
quadratic, except linear when the solution degree is $N=1$) and states,
citing two earlier works, that cross-product-form metrics are
free-stream preserving with Gauss solution points and the DG-recovering
correction function provided $N_m\le N$. The condition is stated, not
tested in the paper, whose cases are the Taylor–Green vortex, a
turbulent channel and the [SD7003 airfoil](/benchmarks/sd7003-airfoil.md).

## Moving and deforming grids: the temporal identity

When the map depends on time, $\boldsymbol x(\boldsymbol\xi,t)$, the
transformed equations carry the grid velocity, and a third identity joins
the two spatial ones. [Liu et al. (2022b)](/sources/liu-2022-g.md), §2.1,
Eqs. (2)–(8), write it for the two-dimensional arbitrary
Lagrangian–Eulerian (ALE) Navier–Stokes equations of their
[flux-reconstruction](/methods/flux-reconstruction.md) (FR/CPR) solver on
moving triangular grids ($(\xi,\eta)$ the reference coordinates as above,
$\xi_x$, $\xi_t$, … the metric terms, $\boldsymbol V_g=(x_t,y_t)$ the grid
velocity, page-local):
$$\begin{aligned}
&\partial_\xi(\mathcal J\xi_x)+\partial_\eta(\mathcal J\eta_x)=0,\qquad \partial_\xi(\mathcal J\xi_y)+\partial_\eta(\mathcal J\eta_y)=0,\\
&\partial_t\mathcal J+\partial_\xi(\mathcal J\xi_t)+\partial_\eta(\mathcal J\eta_t)=0,\qquad \xi_t=-\boldsymbol V_g\cdot\nabla\xi,\quad \eta_t=-\boldsymbol V_g\cdot\nabla\eta .
\end{aligned}$$
With these identities the equations take the physical-domain form
$\partial_tQ+\partial_xF+\partial_yG-\boldsymbol V_g\cdot\nabla Q=0$
($Q$ the conservative variables, $F$, $G$ the fluxes; Eq. 8), which is the
form they discretize. They state that "the first two laws can easily be
satisfied when high-order spatial discretization is used", while the
third, which involves both temporal and spatial derivatives of the
Jacobian and the metrics, "needs special treatment". They enforce it with
a **GCL error compensation** approach, citing earlier moving-grid
spectral-difference and CPR work (their refs. 58, 61, 62; see
[spectral difference method](/methods/spectral-difference-method.md)).
Their third-order FR/CPR scheme keeps its order on a grid deformed by a
prescribed sinusoidal motion: the $L_2$ errors of a scalar wave fall from
$1.24\times10^{-2}$ to $1.76\times10^{-5}$ on $10\times10$ to $80\times80$
quadrilaterals split into triangles, observed orders 3.1–3.2, against
3.0–3.4 on the stationary grids (§3.1.1, Table 1). The grid itself moves
by an algebraic quintic blending of the boundary displacement (§2.5). All
their flows are laminar ($Re=100$–1000); turbulence models are named as
future work (§4).

The review of high-order discontinuous schemes for multiphase flow of
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §4.5, states the same
requirement for Lagrangian and ALE DG that track material interfaces with
element edges (all cited): the discretization must first be cast in ALE
form, the GCL (Thomas & Lombard) must hold, and the most consistent route
to a fully conservative ALE formulation is a space–time DG formulation,
which satisfies the GCL automatically when all space–time integrations
are exact. A marker-point front tracking on a fixed mesh avoids moving
the mesh but loses geometric exactness: corners erode and the enclosed
mass drifts (§4.5, Fig. 7). None of these is run on a turbulent flow.

[Sugaya & Imamura (2021)](/sources/sugaya-2021.md) avoid grid
deformation altogether. Their hierarchical Cartesian grid moves rigidly
with the body, and they separate this rigid-grid "moving grid method"
from the deformable-grid approach, for which they cite the GCL paper of
Thomas & Lombard (§1). The grid-motion flux $Q\,V_n$ ($V_n$
the normal grid velocity of a face, page-local) is folded into the
inviscid flux by a Galilean transformation (§2.1, Eqs. 1–9; see
[immersed boundary methods](/methods/immersed-boundary-method.md)). They
do not discuss a GCL. For a rigid motion $\mathcal J$ does not change in
time and the grid velocity $\boldsymbol V_{\mathrm{trans}}+\boldsymbol\omega_{\mathrm g}\times\boldsymbol r$
($\boldsymbol\omega_{\mathrm g}$ the angular velocity of the grid, page-local)
is divergence-free, so the temporal identity of Liu et al. above holds
exactly *(compiler check, not in the sources)*. Their test of the moving formulation is a Galilean one: a steady
Spalart–Allmaras RANS of a NACA 0012 at $Re=6\times10^6$, relative Mach
number 0.15, $\alpha=10^\circ$, run with the stream on a fixed grid and
with the grid moving through quiescent air. The two runs give density
residual norms of $4.85717\times10^{-11}$ and $4.85718\times10^{-11}$ at
step 15,000. They call the differences "in the order of machine zero",
and $C_p$, $C_f$ and eddy-viscosity profiles are identical (§3.1, Table 3,
Figs. 5–8).

**The temporal identity discretized in the DGSEM.** For deforming
meshes in [FLEXI](/software/flexi.md), [Gao et al. (2023)](/sources/gao-2023.md),
§3.1, Eqs. (16)–(39), write the arbitrary Lagrangian–Eulerian DGSEM on a
fixed reference time with the mesh velocity $\boldsymbol w=\partial_\tau\boldsymbol x$
and its contravariant components $W^i=\mathcal J\boldsymbol a^i\cdot\boldsymbol w$
(page-local; $\tau$ the reference time, not a stress), so that the
convective flux becomes $\mathcal J\boldsymbol a^i\cdot F-W^iU$, and the
GCL in reference space reads
$$\partial_\tau\mathcal J+\sum_{i=1}^3\frac{\partial(-W^i)}{\partial\xi^i}=0,$$
with $-W^i$ the "GCL flux" (Eq. 28). Free-stream preservation needs both
the metric identities (citing Kopriva) and this law. They discretize the
GCL in strong form with the same tensor-product Lagrange basis on LGL nodes
as the flow variables, interpolating $\mathcal J$, $\boldsymbol w$ and
$-W^i$ in that basis (Eqs. 31–39); its surface flux needs no Riemann
solver because the mesh velocity is continuous, the interface mesh
velocity being interpolated from the geometric mesh. The interior mesh
moves by radial-basis-function interpolation of the interface
displacement, and the fluid is subcycled with a cubic-in-time
interpolation of the mesh position and velocity at each Runge–Kutta stage
(§3.3). The scheme carries the implicit LES of a Mach 2 shock/boundary-layer
interaction over an elastic panel (see the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) page);
no free-stream test on the deforming mesh is shown, while
[Thawait et al. (2023)](/sources/thawait-2023.md), §II A, D, run the
arbitrary Lagrangian–Eulerian transport of a commercial finite-volume
solver for an aerothermoelastic fin without discussing a GCL.

## Qualifications

- **Printed metric formula (Cao et al. 2024, arXiv v1, Eq. 11).** The
  printed $\hat\xi_x=\tfrac12\big((zy_\eta)_\zeta-(yz_\eta)_\zeta+(zy_\zeta)_\eta-(yz_\zeta)_\eta\big)$
  expands to $z\,y_{\eta\zeta}-y\,z_{\eta\zeta}$, not to the cofactor
  $y_\eta z_\zeta-z_\eta y_\zeta$ of Eq. (5); the combination
  $\tfrac12\big((zy_\eta)_\zeta-(zy_\zeta)_\eta+(yz_\zeta)_\eta-(yz_\eta)_\zeta\big)$
  does reproduce it *(compiler check, not in the sources)*. In the printed
  $\hat\xi_y$ the last two terms are identical and cancel, and $\hat\xi_z$
  has the printed structure of $\hat\xi_x$. The free-stream test of Table 3
  shows that the code preserves the GCL.
- The DGSEM sources state free-stream preservation as a property of their
  metric evaluation (Krais et al. 2021; Kurz et al. 2025) and show no
  free-stream test on curved meshes (Krais et al.'s free-stream runs are
  Cartesian scaling tests, §5.8); Cao et al. (2024) test it.
- Gao et al. (2023) show the order and free-stream behaviour of their
  ALE DGSEM by citation of the group's earlier work (Krais et al.;
  Schnücke et al.), not by a test in the paper.
- On cross-product metrics in flux reconstruction, Witherden et al. (2025,
  §3.4) print that on curved grids their discrete divergence "may be
  non-zero", which led PyFR to the curl form; Vermeire (2024, §3,
  Eqs. 8–9) prints that they are free-stream preserving with Gauss points
  and a DG-recovering correction when the mapping degree does not exceed
  the solution degree. Neither prints a quantitative free-stream test.
- Liu et al. (2022b) do not print the error-compensation terms, and give
  no free-stream test on the deforming grid; the deforming-grid result
  they show is the order of accuracy of Table 1.

# Citations

- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv 2107.08609v1: §2.1, Eqs. (3)–(6) (transformed BGK equation, metric terms, Jacobian-weighted variables); §2.3, Eqs. (10)–(11) (metric evaluation from discrete points, symmetric conservative form, Gauss-point interpolation, WENO in computational space); §3.1, Tables 1–3 (accuracy, free-stream preservation); §3.3–3.4.
- [Krais et al. (2021)](/sources/krais-2021.md) — §3.1, Eqs. (4)–(7) (curl-form metric terms, metric identities, free-stream preservation).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv 2404.12703v2: §2.2, Eqs. (11)–(13) (curl-form metric terms in GALÆXI).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §3 (conservative Kopriva form of the metric terms).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2 (free-stream preservation in the TRACE DGSEM).
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §2.1, Eqs. (2)–(8) (ALE transformation, three GCL identities, error compensation); §2.5 (grid deformation); §3.1.1, Table 1 (order on stationary and deforming grids); §4.
- [Ma et al. (2022)](/sources/ma-2022.md) — §2, Eqs. (1)–(2) (curvilinear transformation; metrics computed with the flux scheme for the GCL).
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §2.2, Eqs. (19)–(21) (curved-element Jacobian as a geometric aliasing source); §4.3, Eqs. (50)–(52), Figs. 15–18 (Taylor–Green vortex on a sinusoidally perturbed mesh).
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §1 (rigid against deformable moving grids); §2.1, Eqs. (1)–(9) (moving-grid flux); §3.1, Table 3, Figs. 5–8 (stationary against moving grid).
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1, §2.2.1 (GCL of the fourth-order WCNS in PHengLEI, cited); §2.3 (multi-block grids of the 30P30N airfoil).
- [Gao et al. (2023)](/sources/gao-2023.md) — §3.1, Eqs. (16)–(39) (ALE DGSEM, mesh velocity in reference space, GCL flux, strong-form discretization); §3.3 (RBF mesh deformation, subcycling).
- [Thawait et al. (2023)](/sources/thawait-2023.md) — §II A, Eq. (5); §II D, Eqs. (16)–(17) (ALE transport and diffusion-based mesh smoothing; no GCL discussed).
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.3 (GCL of the WCNS in PHengLEI, cited; passing).
- [Vermeire (2024)](/sources/vermeire-2024.md) — §3, Eqs. (8)–(9) (cross-product metrics free-stream preserving with Gauss points and FRDG when the mapping degree does not exceed the solution degree, cited).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.5, Fig. 7 (GCL for Lagrangian and ALE DG, space–time DG, fixed-mesh front tracking; review).
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §3.4, Fig. 7 (cross-product against conservative curl-form metric in PyFR; on-the-fly metrics for linear elements).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §I (free-stream preservation of WCNS on curvilinear grids and the GCL, cited; passing).
