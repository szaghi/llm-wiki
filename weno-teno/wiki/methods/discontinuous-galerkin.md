---
type: Method
title: "Discontinuous Galerkin method"
description: "The discontinuous Galerkin (DG) semi-discretization of a conservation law with piecewise polynomials of degree N coupled only through numerical fluxes, its modal, nodal, space–time and central (overlapping-mesh) variants, its Runge–Kutta time stepping and CFL limit, the cell-average update behind bound preservation, and the stabilization and adaptation strategies the sources attach to it."
status: established
aliases: [DG, RKDG, central DG, CDG, Runge–Kutta discontinuous Galerkin, modal DG, nodal DG, space–time DG, LDG, local discontinuous Galerkin, discontinuous spectral element method, DSEM]
tags: [dg, numerical-flux, limiting, bound-preserving]
timestamp: 2026-10-24T06:00:00Z
---

# Discontinuous Galerkin method

The discontinuous Galerkin (DG) method approximates the solution of
$\partial_tu+\partial_xf(u)=0$ by a function $u_h$ whose restriction to every
cell $I_i$ is a polynomial, $u_h\vert_{I_i}\in\mathbb P^N$, with no continuity
across interfaces. Cells interact only through a two-point numerical flux
$h(u^-,u^+)$ at the interfaces. The design order is $N+1$. For a scalar law
the flux is monotone, and for a system it is an approximate Riemann solver.
With an explicit Runge–Kutta stepper the scheme is called RKDG
([Peng, Sun & Wu (2024)](/sources/peng-2024.md), §2.1, citing Reed–Hill and
Cockburn–Shu).

## Semi-discrete weak form

Multiplying by a test function $v\in\mathbb P^N(I_i)$ and integrating by
parts on $I_i$ gives Peng et al.'s Eq. (2.2):

$$\int_{I_i}\partial_tu_h\,v\,dx=\int_{I_i}f(u_h)\,\partial_xv\,dx-\hat f_{i+1/2}\,v^-_{i+1/2}+\hat f_{i-1/2}\,v^+_{i-1/2},\qquad \hat f_{i+1/2}=h\big(u^-_{i+1/2},u^+_{i+1/2}\big),$$

for all $v\in\mathbb P^N(I_i)$. Here $v^-_{i+1/2}$ is the trace from cell $i$
and $v^+_{i-1/2}$ the trace from cell $i$ at its left face, so both are inner
traces of $I_i$. The ODE system is written $\frac{d}{dt}u_h=\mathcal L(u_h)$.
In several dimensions, on an element $K$ with
$u_h\vert_K\in\mathbb P^N(K)$ (total degree $\le N$), the volume term becomes
$\int_Kf(u_h):\nabla v$ and the boundary term a sum of face integrals of
$h$ against the outward normal (Peng et al. (2024), Eq. (3.3)). Tensor-product
spaces $\mathbb Q^N$ on Cartesian cells are the other common choice
([Cui, Ding & Wu (2024)](/sources/cui-2024.md), §1, §7).

Two families of bases appear in the sources:

- **Modal bases.** These are orthogonal (scaled Legendre) bases, in which the
  zeroth coefficient is the cell average. The OEDG damping step of Peng et
  al. is diagonal in such a basis
  ([OEDG](/methods/oedg.md)). On unstructured meshes of arbitrary element
  shape, [Basile et al. (2022)](/sources/basile-2022.md) build a
  hierarchical orthonormal modal basis per element by modified Gram–Schmidt
  on monomials, so the mass matrix is diagonal and the modes group by total
  degree. Their solver CODA uses a Roe flux with a Harten-type entropy fix,
  BR1 for the viscous terms and implicit backward Euler with matrix-free
  GMRES (§2.3). The grouping by degree is what their
  [hp-adaptation](/methods/hp-adaptation.md) estimator and smoothness test
  read. [Maltsev et al. (2023)](/sources/maltsev-2023.md) use instead a
  cell-centred Taylor basis, the monomials $(x-x_c)^{p}(y-y_c)^{q}(z-z_c)^{r}$
  of total degree $\le N$ scaled by $h^{p+q+r}$ with $h$ the square root
  of the cell volume, minus their cell means, so that every mode but the
  zeroth has zero mean (§2.1, Eq. (6); page-local exponents and $h$). One
  basis serves tetrahedra, hexahedra, prisms, pyramids, triangles and
  quadrilaterals, integrated by decomposition into simplices, and the
  authors chose a modal basis to avoid the under-integration errors of
  nodal implementations. Without the scaling by $h$ they "could not achieve
  higher than 4th of accuracy", which they attribute to the conditioning of
  the mass matrix (§2.1; no data shown). The same Taylor basis carries the
  finite-volume reconstruction of their hybrid scheme (see below).
  Rescaled Taylor monomials about the barycentre are also the spatial
  basis of the [ADER](/methods/ader-scheme.md)-DG schemes of
  [Ciallella et al. (2024)](/sources/ciallella-2024.md) on triangles
  (scaled by the incircle diameter, §3.2) and
  [Gaburro et al. (2024)](/sources/gaburro-2024.md) on polygons (scaled by
  the radius of gyration, Eqs. (22)–(24); both arXiv v1).
  [Cernetic et al. (2023)](/sources/cernetic-2023.md) use tensor products
  of orthonormal scaled Legendre polynomials truncated at total degree
  $N$, $(N+1)(N+2)(N+3)/6$ functions per cube, on uniform Cartesian
  meshes, with Gauss quadrature of $N+1$ points per direction, more than
  polynomial integrands need, because the flux integrands are rational
  functions of the state (§2.3–2.4, Eqs. (13)–(18); accepted manuscript).
  [Huang & Fu (2024)](/sources/huang-2024.md) use the scaled Legendre basis
  $1$, $(x-x_i)/\Delta x$, $((x-x_i)/\Delta x)^2-\tfrac1{12}$ of RKDG, whose
  coefficients their limiter rebuilds (§3, Eqs. (16)–(23)).
- **Nodal bases.** These are Lagrange bases at Legendre–Gauss–Lobatto nodes
  $\xi_j$ with collocated quadrature. The result is the
  [DGSEM](/methods/dgsem.md), whose mass matrix is diagonal and whose
  derivative matrix is a
  [summation-by-parts operator](/operators/summation-by-parts-operator.md)
  ([Ranocha et al. (2023)](/sources/ranocha-2023.md), Ex. 2.3;
  [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md),
  §2.1). The nodal setting is the basis of
  [flux differencing](/methods/flux-differencing.md) and of the
  [entropy-stable](/properties/entropy-stability.md) DG schemes. Nodal
  DG can also be obtained as the [flux reconstruction](/methods/flux-reconstruction.md)
  scheme with DG correction functions; [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md)
  and [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) run nodal DG
  in this form in [PyFR](/software/pyfr.md), from $\mathbb P^2$ up to
  $\mathbb P^{14}$, on quadrilaterals, triangles, tetrahedra and prisms
  (Dzanic et al., §4.1, §5; Dzanic & Witherden, §4.2). With an orthonormal
  modal basis alongside, nodal values and modal coefficients are related
  by a Vandermonde matrix, which is what modal filters act on
  ([entropy filtering](/methods/entropy-filtering.md); Dzanic & Witherden,
  §2.3, Alg. 2). [Yu & Hesthaven (2022)](/sources/yu-2022.md) use nodal
  DG on LGL nodes in 1D and $\alpha$-optimized nodes on triangles with an
  orthonormal Legendre or Dubiner modal basis, whose coefficient decay
  their [artificial viscosity](/methods/artificial-viscosity.md) reads (§2).
  [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) run nodal
  entropy-stable DG on quadrilaterals and triangles with diagonal-norm
  multidimensional SBP operators: tensor-product LGL nodes on quadrilaterals,
  and on triangles volume nodes that contain $(N+1)$-point Gauss–Lobatto
  face nodes, with volume quadrature exact for degree $2N-1$ and face
  quadrature for degree $2N$ (§3.1, Fig. 1; arXiv v2).

Two algebraic rewritings of the same semi-discretization appear in
[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md):

- **Residual-distribution form.** The element residual
  $\Phi^K=\oint_{\partial K}h\cdot n$ is split into nodal sub-residuals
  $\Phi^K_\sigma=-\int_K\nabla\varphi_\sigma\cdot f(u_h)+\oint_{\partial K}\varphi_\sigma\,h\cdot n$
  (page-local basis function $\varphi_\sigma$ of node $\sigma$), whose sum
  over the element is the boundary flux; in this form DG, continuous
  Galerkin and flux reconstruction are residual-distribution schemes
  (§2.1, Eqs. (6)–(9)).
- **Operator form.** With diagonal-norm
  [summation-by-parts operators](/operators/summation-by-parts-operator.md),
  $\frac{d}{dt}u=\mathrm{VOL}+\mathrm{SURF}$ with
  $\mathrm{VOL}=-D_jf^{(j)}$ and a surface term from the numerical flux at
  the element boundary (§2.2, Eqs. (20)–(21), Ex. 2.3).

Both forms carry the element-wise
[entropy correction term](/methods/entropy-correction-term.md).

Two further formulations appear:

- **Space–time DG.** [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md)
  treat time as an extra coordinate: a 1D unsteady problem becomes a 2D
  problem in $(x,t)$ with flux $(f(u),u)$, discretized by DG on space–time
  elements, slab by slab (§2–3.1, Eqs. (2.4)–(3.4)). They list as advantages
  arbitrary orders in space and time, an automatically satisfied geometric
  conservation law, and remeshing without conservative interpolation.
  Moving the element faces with the solution gives
  [implicit shock tracking](/methods/implicit-shock-tracking.md).
  [Huang & Zahr (2022)](/sources/huang-2022.md) also solve unsteady
  problems as steady ones in $d$-dimensional space–time, with nodal DG of
  total degree $N$ on curved simplices whose element map is continuous and
  of its own degree, and add an *enriched* residual, the same DG form
  tested with degree $N+1$, which they call a surrogate for the violation
  of the infinite-dimensional weak form (§1); minimizing it over the node positions is the
  HOIST method (§2.3, §4, Eqs. (8)–(14)).
  [Naudet & Zahr (2024)](/sources/naudet-2024.md) run the same enriched
  space–time DG slab by slab on simplex meshes extruded from the top of
  the previous slab, on a fixed reference slab mapped to the physical one,
  and build the space–time numerical flux from the spatial one: the
  space–time projected Jacobian is the spatial one scaled by the length
  of the spatial part of the normal and shifted by its time component,
  with unchanged eigenvectors (§2.2–2.4, Eqs. (7)–(28)).
- **Central DG on overlapping meshes.** [Ding & Wu (2024b)](/sources/ding-2024-b.md)
  use the central DG (CDG) method, recalled from the literature they
  cite, which evolves two copies of the solution, on a primal mesh and
  on a dual mesh shifted by half a cell, and evaluates every flux on the
  other copy, which is continuous there, so no Riemann solver is needed
  (§3.1, Remark 1). In 1D the primal cell average obeys

  $$\frac{d}{dt}\bar u^{\mathrm I}_j=\frac{\bar u^{\mathrm J}_j-\bar u^{\mathrm I}_j}{\tau_{\max}}-\frac{f\big(u^{\mathrm J}_h(x_{j+1/2})\big)-f\big(u^{\mathrm J}_h(x_{j-1/2})\big)}{\Delta x},$$

  where $\bar u^{\mathrm J}_j$ is the average over $I_j$ of the dual
  solution, the first term is the CDG numerical dissipation and
  $\tau_{\max}$, the largest stable time step, scales it (Eq. (24);
  page-local superscripts I, J for primal and dual and $\tau_{\max}$),
  and the dual average obeys the mirror equation. Because the dual
  solution jumps inside a primal cell, volume integrals are split at the
  cell centre and integrated on each half (Eqs. (21)–(22)). Ding & Wu
  extend CDG to special relativistic MHD with a general equation of
  state, make it bound-preserving in 1D and 2D and locally
  divergence-free in 2D (below, and
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
- **Moment equations with reconstruction.** [Li, Shu & Qiu (2022d)](/sources/li-2022-d.md)
  test the conservation law with $1$ and $(x-x_i)/\Delta x$ on each cell
  (§2.1, Eqs. (2.2)–(2.4)). These two functions span $\mathbb P^1(I_i)$, so
  the equations are the weak form of $\mathbb P^1$ DG *(compiler check, not
  in the sources)*. They
  evolve the cell average and the first moment, but do not carry a DG
  polynomial: the point values needed by the flux and by the volume
  integral of $f(u)$ come from a multi-resolution Hermite-WENO
  reconstruction on a compact stencil, sixth order on three cells
  ([Hermite WENO](/methods/hermite-weno.md)).

Further formulations and boundary treatments:

- **Local DG for viscous terms.** [Du & Yang (2022)](/sources/du-2022-b.md)
  discretize the multi-species reacting Navier–Stokes equations by LDG: the
  gradient is an auxiliary DG variable solved element by element with a
  central flux, and the convective and diffusive fluxes are treated as one
  total flux with a single Lax–Friedrichs-type penalty (§3, Eqs.
  (3.2)–(3.5), after X. Zhang's positivity-preserving DG for Navier–Stokes).
  Yu & Hesthaven use an LDG-type mixed form with centred viscous fluxes for
  their artificial-viscosity term (§2). Lin, Chan & Tomas (2023) use an
  LDG-type form in the entropy variables, $\Theta_d=\partial w/\partial x_d$ and
  viscous flux $\sigma_d=\sum_{d'}\mathsf K_{dd'}\Theta_{d'}$ with the symmetric
  positive semi-definite blocks $\mathsf K_{dd'}$ of the symmetrized viscous operator
  and central interface averages (page-local $\Theta$, $\sigma$, $\mathsf K$, as on [Bassi–Rebay](/methods/bassi-rebay-viscous-discretization.md)), so the
  entropy-stable DG dissipates entropy also for Navier–Stokes, as recalled
  from Chan's earlier work (§4, Eq. (15), Thm. 4.1). PyFR uses BR1 or BR2 (Dzanic et al.,
  §4.2; Dzanic & Witherden, §4.2), and [Kou et al. (2022)](/sources/kou-2022.md)
  use the LDG common solution $\{\!\{u\}\!\}-\beta_{\mathrm{LDG}}[\![u]\!]$ and
  viscous flux $\{\!\{f_v\}\!\}+\tau_{\mathrm{LDG}}[\![u]\!]+\beta_{\mathrm{LDG}}[\![f_v]\!]$
  with $\beta_{\mathrm{LDG}}=0.5$, $\tau_{\mathrm{LDG}}=0.1$ (page-local
  parameters and viscous flux $f_v$) inside
  [flux reconstruction](/methods/flux-reconstruction.md) (§3, Eqs. (9),
  (15)).
  [Cernetic et al. (2023)](/sources/cernetic-2023.md) implemented BR1 and
  abandoned it: it triples the cost of the gradient solve in 3D, gives
  unphysically large in-cell derivatives for initial data with large jumps
  and, they write, "does not converge rapidly at high order" (§3.1). They
  take the interface value and gradient of the viscous flux instead from
  the $L^2$ projection of the two neighbouring polynomials onto one
  polynomial of degree $N+1$ in the normal direction, on an overlap domain
  covering a fraction $f_{\mathrm o}$ (page-local) of each cell, after the
  recovery method of van Leer & Nomura; $f_{\mathrm o}=3/4$ gives the
  expected diffusion orders for $N\le2$ and $f_{\mathrm o}=1$ is needed above
  (§3.2, Eqs. (29)–(36)). The projection is a precomputed sparse map, and
  exchanging the two partial sums costs no more communication than an
  average.
- **Bassi–Rebay lifting for viscous terms.** The modal solver of
  [Alberti et al. (2025)](/sources/alberti-2025.md) and the reacting
  multicomponent solver of [Ching et al. (2025)](/sources/ching-2025.md)
  use BR2, a primal form in which the interface viscous flux is the average
  of the flux evaluated at the broken gradient plus a penalized face-local
  lifting of the solution jump; Ching et al. write the primal form with a
  generic penalty, either BR2 or a Lax–Friedrichs-type term
  $\tfrac{\beta_{\mathrm v}}2(u^+-u^-)$, page-local coefficient $\beta_{\mathrm v}$
  (§3, Eq. (3.2)). Alberti et al. make BR1 and BR2 entropy stable by an
  extra projection of the viscous flux. See
  [Bassi–Rebay viscous discretizations](/methods/bassi-rebay-viscous-discretization.md).
- **Entropy-projected modal DG.** Alberti et al. (2025) solve for the
  conservative variables in an orthonormal hierarchical physical-space
  basis but evaluate every spatial operator at the $L^2$ projection of the
  entropy variables, and remove the remaining quadrature error of the
  entropy balance with an
  [entropy correction term](/methods/entropy-correction-term.md); the
  uncorrected projection scheme is already "much more robust" than their
  conservative-variable DG (§2, §3.1.2;
  [entropy projection](/methods/entropy-projection.md)).
- **FR as DG with a modified mass matrix.** [Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md)
  write energy-stable flux reconstruction on curvilinear hexahedra as
  conservative strong DG with $M_K$ replaced by $M_K+K_{\mathrm{FR}}$
  (page-local correction operator) and approximate its inverse by a
  weight-adjusted tensor-product projection, so that only a diagonal matrix
  is inverted per element (§3.2, §4;
  [flux reconstruction](/methods/flux-reconstruction.md)). Their baseline
  conservative strong DG uses a Lagrange flux basis collocated on the
  quadrature nodes (Eqs. (24)–(25)); on Gauss nodes at $N=5$ it diverges on
  the inviscid Taylor–Green vortex where the entropy-conservative scheme
  does not (§7.3–7.4).
- **Non-conservative products in multiphase flow.**
  [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) discretize the Kapila
  five-equation model by modal DG on Cartesian meshes, writing the
  volume-fraction equation as $\partial_t\phi_1+\nabla\cdot(\phi_1v)=\chi_1\phi_1\nabla\cdot v$
  with page-local $\chi_1=1/(\rho_1c_1^2)\big/\big(\phi_1/(\rho_1c_1^2)+\phi_2/(\rho_2c_2^2)\big)$
  (§2.1; [five-equation model](/definitions/five-equation-model.md)). The
  source integral is split into the cell interior, where $v$ is
  re-interpolated at $N+1$ Gauss–Lobatto nodes so that the Gauss quadrature
  of $\partial_xv$ equals the jump $v^-_{i+1/2}-v^+_{i-1/2}$ exactly
  although $v=\rho v/\rho$ is rational, and the interfaces, where the
  velocity jump is shared between the two cells with HLL-speed weights
  $-s^-/(s^+-s^-)$ and $s^+/(s^+-s^-)$ (Eqs. (2.8), (2.10), Remark 2.1;
  [HLL solvers](/methods/hll-riemann-solvers.md)). The earlier averaging
  discretization is formally second order; with it the $l^1$ orders of
  $\mathbb P^2$ and $\mathbb P^3$ drop to about 1.7–2.0 in 1D, against 3.25–3.77
  and 4.40–4.51 for the new form (Remark 2.2, Tables 2–3). With the new form the
  scheme for $\phi_2=1-\phi_1$ has exactly the same form as that for
  $\phi_1$ (what the authors call the symmetry of the volume fractions, not
  a spatial symmetry), which is what proves $\phi_1\le1$, and the scheme keeps uniform velocity and pressure across an
  isolated interface (Lemma 2.5, Thms. 2.6–2.7; [OEDG](/methods/oedg.md)).
- **Primitive variables with a conservation defect.**
  [Gaburro et al. (2024)](/sources/gaburro-2024.md) evolve a non-conservative
  set of variables, $(\rho,v_1,v_2,p)$ plus a material marker, in both the
  predictor and the corrector of an [ADER](/methods/ader-scheme.md)-DG
  scheme, with path-integral fluctuations at the faces
  ([path-conservative schemes](/methods/path-conservative-scheme.md);
  §3.3, Eqs. (32)–(34)). Such a scheme satisfies the cell balance only up to
  a local conservation defect, which they prove vanishes as $h\to0$ for
  smooth solutions and at contacts, so that a modified
  [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) holds (Props.
  1–5); at shocks it does not, and the shock-triggered subcells are
  recomputed in conservative variables (§4.4, Eq. (67)).
- **Curved boundaries on straight-sided or embedded meshes.** Ciallella
  et al. (2024) note that ghost-state boundary conditions imposed on the
  straight faces of a conformal linear triangulation make DG at best
  second order whatever $N$, and first order in boundary consistency on a
  fully embedded mesh whose surrogate boundary is detached from the true
  one (§4, Fig. 1). On a manufactured steady Euler solution the uncorrected
  scheme converges at rates 2.00–2.01 for $N=1,2,3$ alike, e.g. $\rho$ error
  $2.6792\times10^{-5}$ at $N=3$ on the finest level (Table 2). Their remedy, a
  constrained least-squares boundary reconstruction on the true boundary,
  is on [immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md).
- **DG on point clouds.** [Du, Shu & Zhong (2022)](/sources/du-2022.md)
  run DG on polygonal, possibly non-convex cells built by grouping
  Voronoi regions of scattered data points, each cell holding at least
  $\dim\mathbb P^N=(N+1)(N+2)/2$ points; two neighbouring cells may share
  several edges (§2.2, after Du & Shu).
- **Sharp-interface cut cells.** [Bai & Li (2022)](/sources/bai-2022.md)
  run RKDG on Cartesian cells cut by a level-set interface between two
  fluids. Each fluid's cut cell is updated on the whole cell with a mixed
  polynomial, the $L^2$ projection of the real-fluid polynomial on its own
  part and a ghost-fluid polynomial on the other part (§2.5.2, Eqs.
  (27)–(28)), so small cut cells do not restrict the time step
  ([level-set and ghost-fluid methods](/methods/level-set-method.md)).

## Time stepping and the CFL limit

Peng et al. (2024) write the $s$-stage, $r_{\mathrm{RK}}$th-order explicit Runge–Kutta
method in Shu–Osher form,
$u_h^{n,\ell+1}=\sum_{m\le\ell}\big(c_{\ell m}u_h^{n,m}+\Delta t\,d_{\ell m}\mathcal L(u_h^{n,m})\big)$
with $\sum_mc_{\ell m}=1$ (page-local coefficients $c_{\ell m}$, $d_{\ell m}$;
§2.1). The [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) members are the
convex combinations of forward-Euler steps. Rueda-Ramírez et al. (2022) use
three-stage SSP-RK3 at CFL 0.5 in all their tests (§5). Wu & Shu (2023) use
SSP-RK3 at CFL 0.15 ([Wu & Shu (2023)](/sources/wu-2023-b.md), §7). Du,
Shu & Zhong (2022) use SSP-RK3 at CFL 0.3 ($N=1$) and 0.18
($N=2$), with $\Delta t\sim h^{4/3}$ for $N=3$ accuracy tests (§4); Bai &
Li (2022) use $\Delta t=\mathrm{CFL}\min\big(\Delta x/(\lvert v_1\rvert+c),\Delta y/(\lvert v_2\rvert+c)\big)$
with CFL 0.2 (0.1–0.3 on the Shu–Osher problem) and a three- or four-stage Runge–Kutta method (Eq. (30));
Dzanic & Witherden (2022) use SSP-RK3 and Dzanic et al. (2022) classical
RK4; Yu & Hesthaven (2022) use the five-stage fourth-order low-storage
Runge–Kutta method of Carpenter & Kennedy. Yu & Hesthaven state the
explicit restriction with an artificial viscosity $\mu$ as
$\Delta t\sim\mathrm{CFL}/\big(a N^2/h+\mu N^4/h^2\big)$, which they call
stringent (Eq. (2.23)). Maltsev et al. (2023) use third-order TVD Runge–Kutta with
$\Delta t=\nu\,\frac1{2N+1}\min_i(h_i/a_i)$, $h_i$ a characteristic cell length
and $a_i$ the maximum wave speed, the same for their DG and finite-volume
parts, at $\nu=0.5$, and $0.3$ for the Schardin, Taylor–Green and sonic-boom
runs (§2.3, Eq. (32), §3). Lin, Chan & Tomas
(2023) use SSPRK(3,3) with a step set by their positivity condition
$\Delta t=\nu\min_im_i/(2\lambda_i)$, page-local graph-viscosity sums
$\lambda_i$ and lumped masses $m_i$; they recall that this step scales as
$O(h/N^2)$ and has been observed to be 2–3 times smaller than the largest
stable high-order DG step, and with explicit viscous terms the parabolic
restriction $O(h^2\mathrm{Re})$ adds to it (§5 Remarks 1–2, §7, Eq. (57)).
Cernetic et al. (2023) take $\Delta t=f_{\mathrm{CFL}}\,h/\big[2(N+1)(c_{\max}+\lvert v\rvert_{\max})\big]$
with $f_{\mathrm{CFL}}=0.5$ (0.3 for strong blast waves) and SSP Runge–Kutta
methods whose order rises with $N$, up to five stages and fourth order; for
$N+1>4$ they saw no dominance of the time error, which they attribute to the
small Courant factor (§2.5, Eq. (23)). Huang & Fu (2024) run third-order
RKDG ($N=2$) with SSP-RK3 at CFL 0.15 (§6). The ADER-DG schemes of Ciallella
et al. (2024) and Gaburro et al. (2024) are one-step and bound the step by
$1/(2N+1)$ times a mesh ratio ([ADER schemes](/methods/ader-scheme.md)).
For stiff chemistry, Du & Yang (2022) replace
SSP-RK by a third-order conservative modified exponential Runge–Kutta
method; on a stiff test with source coefficient $10^6$, SSP-RK3 at the
same step blows up on the two coarsest meshes and needs $\tfrac25$ of it
(Table 6.2).

Cui et al. (2024), Remark 7.7, cite the linear-stability restriction of
$\mathbb P^N$-DG with an $(N+1)$-stage Runge–Kutta method as an empirical
formula. In 2D it reads

$$\Delta t\Big(\frac{a^{(1)}}{\Delta x}+\frac{a^{(2)}}{\Delta y}\Big)\le\frac1{2N+1},$$

with $a^{(d)}$ the maximum wave speed in direction $d$. Peng et al. (2024)
run their OEDG tests at CFL $1/(2N+1)$ (§5). Cao et al. (2026) use
$\Delta t=C_{\mathrm{cfl}}/\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)$ with
$C_{\mathrm{cfl}}=0.3$, $0.16$, $0.1$ for $N=1,2,3$, below $1/(2N+1)$, with
SSP-RK3 on discontinuous problems and an $(N+1)$-stage Runge–Kutta method of
order $N+1$ on smooth ones (§6; page-local $C_{\mathrm{cfl}}$). Peng et al.'s Prop. 4.6,
collected from the RKDG stability literature, states for $r_{\mathrm{RK}}$th-order
$r_{\mathrm{RK}}$-stage Runge–Kutta on linear problems that the $L^2$ stability estimate
$\|u_h^{n+1}\|^2\le(1+C_s\Delta t)\|u_h^n\|^2$ (their Assumption 4.5,
page-local constant $C_s$) holds under $\Delta t\le C\,\Delta x^{\mathsf k}$ (page-local exponent
$\mathsf k$, not the kinetic energy $\kappa$) with the following exponents:

- $\mathsf k=1+1/r_{\mathrm{RK}}$ for $r_{\mathrm{RK}}\equiv1\pmod 4$;
- $\mathsf k=1+1/(r_{\mathrm{RK}}+1)$ for $r_{\mathrm{RK}}\equiv2\pmod4$;
- $\mathsf k=1$ and $C_s=0$ for $r_{\mathrm{RK}}\equiv3\pmod4$;
- $\mathsf k=1$ and $C_s=0$ after combining two or three steps for $r_{\mathrm{RK}}\equiv0\pmod4$.

## The cell-average update

Taking $v=1$ in the weak form gives the update of the cell average. It is
identical to a finite-volume scheme. In 1D with forward Euler it reads
$\bar u_i^{n+1}=\bar u_i^n-\frac{\Delta t}{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)$
(Cui et al. (2024), Eq. (1.5)). In multi-D the face integrals are evaluated
by Gauss quadrature (Eq. (7.2); Wu & Shu (2023), Eqs. (6.6)–(6.8)). This
identity is the hinge of the Zhang–Shu bound-preserving framework:

1. A [cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
   writes $\bar u_i$ as a convex combination of point values that includes
   the interface traces.
2. The [scaling limiter](/methods/zhang-shu-scaling-limiter.md)
   $\tilde u_h=\theta(u_h-\bar u)+\bar u$ puts those point values in $G$.
3. The update is then a convex combination of first-order bound-preserving
   steps under a CFL condition proportional to the boundary weight
   $\varpi$.

Cui et al. (2024) prove that the classical Gauss–Lobatto decomposition is
optimal in 1D and on $\mathbb Q^N$. On $\mathbb P^N$ it is not, and the
optimal bound-preserving CFL number for balanced directional wave speeds,
$a^{(1)}/\Delta x=a^{(2)}/\Delta y$ (their anisotropy parameter set to zero), is
1.5–1.75 times the classical one.
For example, it is $1/4$ against $1/6$ for $N=2,3$ (Table 1). With a
Lax–Friedrichs flux ($c_0=1$), the optimal bound-preserving CFL number is
weaker than $1/(2N+1)$ for every $N\le9$ except $N=8$ (Remark 7.7). See
[bound preservation](/properties/bound-preservation.md).

Wu & Shu (2023) apply the same cell-average route to multicomponent ideal
MHD. There the bound-preserving property of the DG cell average requires a
discrete divergence-free condition on $B$. They obtain it with a locally
divergence-free DG basis plus a discretized Godunov-symmetrization source
term. The resulting high-order scheme is provably bound-preserving under
$(1+\varepsilon_B)\nu_W\le\mathsf w^{\mathrm{GL}}_1$ (Thm 6.4). Here
$\nu_W$ is their two-directional CFL number, $\mathsf w^{\mathrm{GL}}_1$ the
first weight of the $\lceil(N+3)/2\rceil$-point Gauss–Lobatto rule, and
$\varepsilon_B$ the ratio of the normal-$B$ jump terms to the viscosity
parameters (all three page-local). Their tests use the third-order case
$N=2$. See
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

[Liu & Wu (2025)](/sources/liu-2025.md) (§3; arXiv v2) take the same
route for ideal MHD with an [OEDG](/methods/oedg.md) scheme on Cartesian
meshes. The magnetic field lies in the locally divergence-free space of
Li & Shu. The [Godunov–Powell term](/definitions/godunov-powell-source-term.md)
is added **only to the cell-average equations**, since weak positivity
involves only the averages. The higher moments evolve with the plain
OEDG scheme (§3.2). For a locally divergence-free field the cell-average
source comes only from the normal-field jumps at the interfaces. Each jump
is split between the two neighbours with the HLL weights
$-s^-/(s^+-s^-)$ and $s^+/(s^+-s^-)$, which the authors call an "upwind"
discretization (Eqs. (45)–(49)). With the geometric-quasilinearization
form of the admissible set and new two-state HLL inequalities, their
Thm. 1 proves admissible cell averages under an explicit CFL condition.
The hypotheses are an admissible solution at the decomposition nodes and
HLL speeds that bound the Wu–Shu estimates (Eqs. (58)–(66);
[geometric quasilinearization](/methods/geometric-quasilinearization.md)).
The Zhang–Shu decomposition gives
$\Delta t(a^{(1)}/\Delta x+a^{(2)}/\Delta y)\le1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ with
$N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$ Gauss–Lobatto points (Cor. 1), which is $\tfrac16$
for $N=2$ *(compiler check, not in the sources)*. The optimal
Cui–Ding–Wu decomposition gives $1/(4+2\lvert\varkappa\rvert)$ for $N=2,3$,
with the registry's anisotropy
$\varkappa=(a^{(1)}\Delta y-a^{(2)}\Delta x)/(a^{(1)}\Delta y+a^{(2)}\Delta x)$
(Cor. 2, Remark 3;
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
On the shock–cloud interaction, switching off the damping step makes the
run fail, and removing the source term or the positivity limiter gives
negative cell-average pressure (§4.2.4). On the Mach 800 and 10000 jets,
disabling any of the three makes "the code immediately fail" (§4.2.6).

Yan, Abgrall & Wu (2024) carry it to the Kapila model: if $\phi_1\in[0,1]$
and the state lies in the admissible set at the Gauss and Gauss–Lobatto
points of every cell, the forward-Euler cell average stays admissible under
$\Delta t/\Delta x\le\min\big\{1/(\mathcal A_1+\mathcal A_2),\ \varpi/\max(s^+-s^-)\big\}$,
with page-local $\mathcal A_1$, $\mathcal A_2$ the interior-source and
interface CFL terms and $\varpi$ the boundary weight of their Gauss–Lobatto cell-average decomposition; the
positivity part is proved through the
[geometric quasilinearization](/methods/geometric-quasilinearization.md)
of the admissible set (Thms. 2.7, 2.12; 2D Thms. 3.6, 3.10). Their tests
use CFL $1/(2N+1)$ and report the ratio $\mathcal A_1/\mathcal A_2\ll1$, so
the bound is not restrictive (§4, Figs. 9, 21).

[Ching et al. (2025)](/sources/ching-2025.md) split the cell-average update
of the Navier–Stokes equations into two halves,
$\bar u^{n+1}=\tfrac12\big(\bar u^{n+1}_{\mathrm c}+\bar u^{n+1}_{\mathrm v}\big)$,
a convective-only and a viscous-only update each with step $2\Delta t$
(Eq. (4.12)). The convective half is kept in an entropy-bounded set by an
invariant-region-preserving flux; the viscous half is a convex combination
with a Lax–Friedrichs-type viscous penalty, proved positivity preserving
for curved elements and any positive quadrature, with the cell-average
decomposition of Lv & Ihme that need not contain the endpoints (Thms. 6, 8,
Eqs. (4.17), (4.33);
[positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md),
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
At a zero species concentration with inward diffusive flux no penalty
keeps the update non-negative, since the positivity limiter acts only at
finitely many points; they scale the interface gradient instead (§4.7,
Remark 11).

Ding & Wu (2024b) carry the route to the central DG scheme above for
relativistic MHD, with the admissible set $D>0$, $p>0$, $\lvert v\rvert<1$
written by [geometric quasilinearization](/methods/geometric-quasilinearization.md)
as constraints linear in $u$. **Theorem 3.1 (1D):** if the cell averages
and the point values of both copies at the $N_{\mathrm{GL}}$-point
Gauss–Lobatto nodes of the two half-cells are admissible,
$N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$, the forward-Euler cell averages
stay admissible for $\tau_{\max}\le\tfrac{\varpi}{2}\Delta x$ with
$\varpi=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ the endpoint weight and
$\Delta t=\theta_{\mathrm C}\tau_{\max}$, $\theta_{\mathrm C}\in(0,1]$
(page-local); in 1D the normal field stays constant exactly, which
gives the required discrete divergence-free condition (Remark 3).
**Theorem 4.1 (2D):** for the locally divergence-free scheme with the
discretized symmetrization source, on a feasible
[cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
extended to overlapping meshes by splitting each cell into four quarter
cells, the cell averages stay admissible under
$\tau_{\max}\big(\alpha_1/\Delta x+\alpha_2/\Delta y\big)\le\varpi/2$, with
$\alpha_\ell\ge1$ (page-local) growing with the normal-field jumps
(Eqs. (57)–(63)). The divergence terms of the fluxes and of the source
cancel exactly, by Gauss exactness and the divergence theorem on the
quarter cells, inside which the field is divergence-free (Eqs.
(70)–(74)). With the optimal Cui–Ding–Wu decomposition $\varpi=1/4$ for
$N=2,3$, against $1/6$ for the Gauss–Lobatto tensor rule (Cors.
4.1–4.2). **Theorem 4.2:** without the source terms, bound preservation
needs globally coupled discrete divergence-free conditions, which the
local scaling limiter does not keep; the authors leave enforcing both
together open (§4.7). As with Wu & Shu, the limiter must also make the
Gauss flux-quadrature points admissible, because the flux needs a
primitive-variable recovery there, a requirement the authors note does
not arise in non-relativistic MHD (Remark 6). Their tests use $N=2$,
SSP-RK3 and $\Delta t=0.25\Delta x$ (1D),
$\Delta t=0.25/(1/\Delta x+1/\Delta y)$ (2D), above the bounds
$\tau_{\max}\le\Delta x/12$ ($\varpi=\tfrac16$, 1D) and
$\tau_{\max}(\alpha_1/\Delta x+\alpha_2/\Delta y)\le\tfrac18$ ($\varpi=\tfrac14$, 2D)
of the theorems *(compiler check, not in the sources: $\Delta t\le\tau_{\max}$
and $\alpha_\ell\ge1$)*, which they call sufficient but not always necessary
(§5; $\tau_{\max}$ and $\theta_{\mathrm C}$ of the runs are not printed); third order is observed on smooth Alfvén waves, and every
shock test fails without the bound-preserving limiter (see
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md),
[MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md),
[MHD shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md),
[high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md),
[bound preservation](/properties/bound-preservation.md)).

Du & Yang (2022) apply the cell-average route to the LDG scheme for
reacting multi-species Navier–Stokes. A numerical flux that is
"consistent", $\hat f\cdot\mathsf v=0$ for the page-local constant vector
$\mathsf v$ with $u\cdot\mathsf v=\rho-\sum_k\rho Y_k$, makes the
semi-discrete and the fully discrete schemes preserve $\sum_kY_k=1$ exactly
(Thms 3.1–3.2), so that positivity of every partial density gives
$Y_k\le1$ without a separate upper-bound limiter. Their penalty
(Lemma 4.1) makes $u\pm\beta_{\mathrm{LF}}^{-1}f$ admissible for the total flux, and the
bound-preserving CFL condition is
$\frac{\Delta t}{\Delta x}\max\beta_{\mathrm{LF}}\le\varpi$ times the time integrator's
factor $\approx0.793$ (Thms 4.1–4.3, with page-local penalty $\beta_{\mathrm{LF}}$; see
[bound preservation](/properties/bound-preservation.md)).
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) assume without
proof that the element mean of nodal DG and FR with DG correction
functions evolves like a first-order finite-volume scheme and therefore
satisfies positivity and a local minimum entropy principle under SSP time
stepping, a CFL condition and a suitable Riemann solver (§2.2, Eq. (10));
their filter rests on that assumption.

## Stabilization of discontinuous solutions

Unmodified DG oscillates at discontinuities, and the sources attach five
distinct remedies, plus the sharp-interface treatment of material
interfaces.

- **Limiters that overwrite troubled cells.** A
  [troubled-cell indicator](/definitions/troubled-cell-indicator.md) flags
  cells, and a WENO or Hermite-WENO reconstruction replaces the polynomial
  there. Cui et al. (2024) apply the Qiu–Shu WENO limiter before the
  bound-preserving limiter in their Examples 3–5 (§8). Wu & Shu (2023) apply
  a locally divergence-free WENO limiter in cells flagged by the KXRCF
  indicator (§7). Du, Shu & Zhong (2022) make the simple WENO limiter of
  Zhong & Shu cheaper for systems on triangles and point clouds by
  projecting only two polynomials per direction to characteristic
  variables; they save about 6–55 % of the CPU time on shocked problems
  ([WENO limiters for DG](/methods/weno-limiter-dg.md)). Bai & Li (2022)
  use a TVB minmod limiter, and a WENO limiter for their two-phase
  Shu–Osher problem (§2.6, §3.1.5). Maltsev et al. (2023) overwrite on
  unstructured mixed-element meshes: at every Runge–Kutta stage the
  unlimited modal DG solution is checked a priori, by a KXRCF-like shock
  detector or by MOOD-type positivity and relaxed-maximum-principle
  criteria, and in flagged cells the modes $1,\dots,K_{\mathrm b}$ (all but the cell
  average, $K_{\mathrm b}+1$ the number of basis functions, page-local) are replaced by the
  coefficients of a CWENOZ least-squares reconstruction of the same order
  built from neighbouring averages in the same Taylor basis (§2.4, Eq.
  (33), §2.5; [CWENO](/methods/cweno.md)). Keeping mode 0 keeps
  conservation, and matching the orders, DG($\mathbb P^N$) with
  CWENOZ($N+1$), avoids an accuracy mismatch. The hybrid costs 1.4–1.5 times
  pure DG on coarse meshes with many flagged cells and about 1.05 times on
  fine ones (Table 1). Re-checking at every stage or freezing the flag for
  the step makes a negligible difference (§3.2). The authors conclude that
  fine tuning of the switch is "not a necessity" when the finite-volume
  scheme has the DG order, and mandatory with an order mismatch (§4),
  while their shock detector flags up to 100 % of the cells of a smooth
  advection at $N=4$ on coarse meshes (Table B.3); see
  [troubled-cell indicator](/definitions/troubled-cell-indicator.md) and
  [WENO limiters for DG](/methods/weno-limiter-dg.md). They argue that
  subcell limiters, which keep more DG information, are not straightforward
  on meshes with arbitrary elements, transition layers and bad-quality
  cells (§2.4).
  [Huang & Fu (2024)](/sources/huang-2024.md) carry TENO stencil selection
  into both steps of third-order RKDG on Cartesian grids. Their
  troubled-cell indicator forms $\gamma_n=1/(\beta_n+10^{-3})^6$ from the
  smoothness indicators of the DG polynomials of cells $i-1$, $i$, $i+1$,
  normalizes them and flags cell $i$ when its own share falls below
  $C_T=10^{-4}$, direction by direction in 2D (§4.3, §5.1, Eqs. (32)–(35)).
  In flagged cells their limiter keeps the cell average and rebuilds the
  first and second modes from compact candidate polynomials, Hermite-type
  with neighbouring first moments, combined with linear weights restricted
  to the candidates that survive a TENO cut-off (§4.4, §5.2;
  [troubled-cell indicator](/definitions/troubled-cell-indicator.md),
  [WENO limiters for DG](/methods/weno-limiter-dg.md),
  [TENO](/methods/targeted-eno.md)).
  On the 1D and 2D density waves the indicator flags no cell, so the errors
  equal those of the unlimited scheme, e.g. $L^1$ errors $3.53\times10^{-7}$ to
  $6.94\times10^{-10}$ at $N_x=100$ to 800 and rates 2.99–3.00 in 1D (Table 1),
  2.98–2.99 in 2D (Table 3).
  [Huang et al. (2025a)](/sources/huang-2025.md) keep that indicator and
  replace the limiter by a choice between an equal-weight TENO
  combination of the three DG polynomials and a THINC polynomial. The
  choice is made by a compact BVD rule on unlimited neighbour traces
  ([WENO limiters for DG](/methods/weno-limiter-dg.md)).
- **Blending with a low-order scheme.** The nodal DG update is convexly
  blended with a compatible subcell finite-volume update, element by element
  or interface by interface, with a priori or a posteriori blending
  coefficients
  ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  [convex limiting](/methods/convex-limiting.md); Rueda-Ramírez et al.
  (2022)). The ADER-DG schemes of Ciallella et al. (2024) and Gaburro et
  al. (2024) recompute flagged elements a posteriori on subcells with a
  second-order MUSCL–Hancock scheme
  ([MOOD-type a posteriori limiting](/methods/mood-a-posteriori-limiting.md),
  [ADER schemes](/methods/ader-scheme.md)).
  [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) switch
  whole elements instead, from p-adaptive DG to a finite-volume scheme on
  refined subcells ([h- and hp-adaptation](/methods/hp-adaptation.md)).
  Lin, Chan & Tomas (2023) blend element-wise, with one coefficient per
  element, a high-order entropy-stable DG update and a low-order
  positivity-preserving graph-viscosity update on a sparse low-order SBP
  operator; because both are conservative and entropy stable, the blend
  keeps the semi-discrete cell entropy inequality (Thm. 6.2), while subcell
  convex limiting with positivity as the only constraint cannot be shown to
  keep it (App. B.1). See
  [bound preservation](/properties/bound-preservation.md) and
  [entropy stability](/properties/entropy-stability.md).
- **Damping and filtering.** Oscillation-free DG adds stiff damping terms to
  the semi-discrete system. The [OEDG](/methods/oedg.md) method of Peng et al.
  (2024) instead solves the damping step exactly after each Runge–Kutta stage
  as a modal filter. This preserves the cell average and the scale and
  evolution invariance. For linear advection it keeps the optimal
  fully-discrete $L^2$ estimate $O(\Delta x^{N+1}+\Delta t^{r_{\mathrm{RK}}})$ under
  $N>d/2$, $r_{\mathrm{RK}}>d/2+1$, a stable underlying RKDG scheme and a lower bound on
  the deviation of $u_h$ from its average (Thm 4.1). Dzanic & Witherden
  (2022) filter instead with an exponential modal filter whose strength is
  chosen per element, after each Runge–Kutta stage, as the smallest one
  that makes the nodal values positive and satisfy a local minimum entropy
  bound ([entropy filtering](/methods/entropy-filtering.md)).
  Liu & Wu (2025) apply the OEDG step to ideal MHD in two forms (§2.4).
  For the non-magnetic variables the damping is **componentwise**, one
  coefficient per component through a Hadamard product. For the in-plane
  field it is **locally divergence-free**: one coefficient per edge, the
  larger of those of $B_1$ and $B_2$, multiplies whole divergence-free basis
  vectors, so the damped field stays divergence-free in each cell
  (Eqs. (16)–(35), Remark 2). [Liu et al. (2025b)](/sources/liu-2025-b.md)
  keep the damping in the semi-discrete system instead, as an
  entropy-stable oscillation-free DG for MHD. The term is
  $-\sigma(u_h)(u_h-\bar u_h)$, with one scalar $\sigma$ per element built
  from the interface jumps of the solution and its first derivative.
  These are scaled by the local largest characteristic speed and divided
  by the squared local oscillation (Eq. (3.16)). It is integrated by an
  explicit step followed by a closed-form implicit damping step in each
  Runge–Kutta stage, so the damping does not restrict the time step
  (§3.3, Eq. (3.21); [entropy stability](/properties/entropy-stability.md)).
  [Cao et al. (2026)](/sources/cao-2026.md) damp once per time step
  instead of once per stage: after the last Runge–Kutta stage the
  polynomial of each cell becomes the convex combination
  $(1-\theta^{\mathrm{OS}}_i)\bar u_i+\theta^{\mathrm{OS}}_iu_h$, with one
  exponential factor $\theta^{\mathrm{OS}}_i$ for all non-mean modes,
  built from entropy-induced distances between the cell's extrapolated
  polynomial and its two neighbours (page-local; §2.1–2.3,
  [COS(DG)](/methods/cos-dg.md)). Because the step only blends with the
  cell average, it works unchanged for modal and nodal DG, conserves, does
  not increase the $L^2$ norm or the cell integral of any convex entropy,
  and perturbs an $(N+1)$th-order accurate solution by $O(\Delta x^{N+1})$
  (Thms 2.2, 2.4, 4.1). It costs 15.6–18.8 % of the run time against
  35.3–40.6 % for the OE step of OEDG on the same 1D problems (Table 3).
- **Artificial viscosity.** Two sources give sensors for nodal DG: the
  time-reversibility defect of Dzanic et al. (2022), which gives a
  separate viscosity for every conserved variable, and the modal decay
  rate predicted by a neural network of Yu & Hesthaven (2022). Cernetic et
  al. (2023) replace slope limiting altogether by a viscosity field carried
  as an extra DG variable and evolved in time, with a compression source,
  a source from the growth rate of the Persson–Peraire modal sensor and a
  decay over $f_\tau h/((N+1)c)$ (page-local $f_\tau=0.5$); the applied viscosity is
  $\alpha_{\mathrm{AV}}c\,h/(N+1)$ with page-local $\alpha_{\mathrm{AV}}\le1$ (as on the artificial-viscosity page) (§4.1,
  Eqs. (43)–(46)). See
  [artificial viscosity](/methods/artificial-viscosity.md) and
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md).
- **Fitting the discontinuity.** Implicit shock tracking moves the element
  faces onto discontinuities, so that no limiter, reconstruction or
  artificial viscosity is needed. Luo et al. (2021) use a plain central
  flux at interior faces (§3.3,
  [implicit shock tracking](/methods/implicit-shock-tracking.md)). Huang
  & Zahr (2022) keep the standard upwind DG equations as a constraint and
  minimize the enriched residual over the node positions; a modal sensor
  is used only to reset oscillatory elements during the iterations
  (Remark 5, §5.2.3).

[Pazner (2021)](/sources/pazner-2021.md) gives the
invariant-domain-preserving variant of the blending remedy. Pazner's low-order
scheme is a graph-viscosity method built on a sparsified, $O(1)$-stencil
derivative operator, and the high-order nodal DG update is limited
subcell by subcell (§3–4). Applying graph viscosity to the full DG operator
instead makes the low-order method more diffusive as $N$ grows at fixed
degrees of freedom, because each node couples to $O(N)$ others (§3.4,
Fig. 1; [convex limiting](/methods/convex-limiting.md)).

Li, Shu & Qiu (2022d) flag troubled cells with a modified KXRCF indicator,
an indicator from the RKDG literature, in which the power of $h$ in the
denominator is $(l+1)/3$ with $l=5$ the reconstruction degree instead of
the original $(N+1)/2$ (Eqs. (2.25), (2.32)–(2.34);
[troubled-cell indicator](/definitions/troubled-cell-indicator.md)).

[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) contrast the first remedy
with their continuous-Galerkin scheme, which never modifies the finite
element solution. They use the HWENO reconstruction only to compute a
blending factor between high- and low-order stabilization, and they propose
this as an alternative to WENO limiters for DG (§1, Remark 2;
[WENO-stabilized continuous Galerkin](/methods/weno-stabilized-continuous-galerkin.md)).
Their claim that the hybrid is "easier to analyze than DG-WENO schemes" is
stated, not demonstrated (§8).

- **A posteriori viscosity in a compatible finite element scheme.**
  [Zampa & Dumbser (2025)](/sources/zampa-2025.md) (§3.2–3.3; arXiv v1)
  use DG only for the explicit convective parts of a semi-implicit scheme
  for weakly compressible flow. The momentum is in a Raviart–Thomas space
  and is convected by DG with a split flux plus Rusanov dissipation
  ([split convective forms](/methods/split-convective-forms.md)). The
  entropy is transported by a path-conservative DG scheme
  ([path-conservative schemes](/methods/path-conservative-scheme.md)).
  Troubled elements get an a posteriori artificial viscosity
  ([MOOD](/methods/mood-a-posteriori-limiting.md)).
- **Sharp material interfaces.** Bai & Li (2022) keep the two fluids
  separate across a level-set interface. Ghost-fluid states and cut-cell
  mixing replace any smearing of the interface (see the cut-cell item
  above).

## Accuracy

Lin, Chan & Tomas (2023) observe, with their positivity limiter, rates
between $O(h^N)$ and $O(h^{N+1})$ for a $M_0=3$ and $20$ viscous shock and a
strong isentropic vortex (minimum density $2.145\times10^{-3}$) on which
unlimited entropy-stable DG fails; the limiter is active only on coarse
meshes (Tables 3–9). Maltsev et al. (2023) find that pure DG reaches close
to design order on the isentropic vortex while CWENOZ of the same order
needs finer meshes (quadrilaterals, $N=4$: DG $L^2$ errors
$2.97\times10^{-4}$ to $1.14\times10^{-9}$, CWENOZ $7.64\times10^{-2}$ to
$7.20\times10^{-4}$ on 8 to 64 edges; Table 1). With all cells forced
troubled the hybrid keeps the design order of CWENOZ (Table B.4); with active
detectors its observed orders exceed the design order (up to 6.89) because
the flagged fraction falls under refinement, and the authors say they
should not be read as convergence rates (App. B).

Peng et al. (2024) observe optimal order $N+1$ for advection, Burgers and
1D Euler. They also observe order $N+2$ superconvergence of cell averages and
downwind point values for OEDG (Table 1). This superconvergence is proved
only for semi-discrete oscillation-free DG, not for the fully discrete OEDG
(§5.1). Cui et al. (2024) observe order $N+1$ for $N=2,4,6,8$ with the
scaling limiter active (Tables 3–6). At equal accuracy the optimal
decomposition cuts CPU time by 20–50 % (§8).

On discontinuous problems the gain of high degree is smaller. Bai & Li
(2022) find, at an equal number of elements, that $\mathbb P^1$ and
$\mathbb P^3$ beat $\mathbb P^0$ on a gas–water shock–bubble problem but
"seem the same", and at equal degrees of freedom the three degrees agree
up to slight differences; on their two-phase Shu–Osher problem
$\mathbb P^1$ and $\mathbb P^3$ at equal degrees of freedom are basically
consistent and better than $\mathbb P^0$ (§3.1.4–3.1.5, Figs. 12–14). Yu &
Hesthaven (2022) find, at fixed degrees of freedom, that accuracy on the
Shu–Osher problem decreases with the degree on coarse meshes and that the
degrees almost coincide on fine ones (§5.3.2). Dzanic et al. (2022) and
Dzanic & Witherden (2022) obtain first-order $L^1$ convergence on the Sod
shock tube for $\mathbb P^2$–$\mathbb P^7$ with their shock capturing; at
fixed degrees of freedom the first finds a marginally lower error at
higher degree, the second a marginally lower error at lower degree
(Dzanic et al., Table 1; Dzanic & Witherden, Tables 3–4). The two studies
use different shock-capturing methods, so this is not a contradiction.
Cernetic et al. (2023), with their evolved viscosity, capture a shock
within one cell with a 20–80 % width proportional to $h/(N+1)$ for
$N\ge1$ (Figs. 3–4), and find on the Woodward–Colella blast wave that the
degree-7 run on 100 cells matches the degree-1 run on 400 cells, which has
the same number of degrees of freedom; an eighth-order WENO run of Zhao et
al. on 400 cells is closer to the reference with half the degrees of
freedom of their degree-7 run (§5.3, Figs. 7–8). They conclude that real
discontinuities converge only at first order and that at equal degrees of
freedom high-order DG captures shocks as accurately as a second-order
method (§5.3;
[Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md)).
On smooth problems they observe rate $N+1$ for $N=0$–7, slightly above it
except at $N=0$, on the
[isentropic vortex](/benchmarks/isentropic-vortex.md) and exponential
decay of the error with $N$ at fixed mesh, down to a floor of about
$10^{-11}$ that they attribute to the truncated vortex at the periodic box
edge (§5.1, Fig. 5). On the viscous Kelvin–Helmholtz problem the dye
error of $64$ cells at fourth order equals that of the finite-volume code
ATHENA on 2048 cells, and among runs with equal degrees of freedom the
highest order has the lowest error (§6.3, Figs. 14–15;
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)).

Boundaries cap the order independently of the interior scheme. With the
straight-face boundary treatment above, Ciallella et al. (2024) measure
second order for $N=1$–3 (Table 2); with their boundary reconstruction the
rates rise to 2.02, 2.82 and 4.10 at the finest level (Table 4). With
slip-wall conditions that involve normal derivatives, on the supersonic
vortex between concentric arcs, the authors state order $N$ rather than
$N+1$; their finest-level rates are 2.04–2.11, 2.07–2.09 and 2.40–2.57 for
$N=1,2,3$ (§6.2, Table 10).

## Qualifications

- The CFL bound $1/(2N+1)$ is cited by Cui et al. (2024) as an empirical
  formula, not a theorem.
- The sources use different symbols for the degree: Peng et al. and Cui
  et al. write $k$, Ranocha et al., Pazner, Luo et al. and Basile et al.
  write $p$, Wu & Shu write $K$, and Rueda-Ramírez et al. write $N$; Bai
  & Li, Du, Shu & Zhong and Du & Yang write $k$; Abgrall et al., Cicchino
  et al. and the two Dzanic papers write $p$; Yu & Hesthaven write $P$;
  Huang & Zahr write $p$ and Kou et al. $P$; Liu & Wu (2025), Liu et al.
  (2025b), Huang et al. (2025a) and Cao et al. (2026) write $k$; Liu et al. (2025c) write $k$
  for the degree of the face polynomials, with tensor degree $k+1$ in the
  cells; Zampa & Dumbser write $r$ for $\mathrm{RT}_r$ and
  discontinuous degree-$r$ spaces; Mossier et al. and Lin,
  Chan & Tomas write $N$; Maltsev et al. write $r$; Ciallella et al. write
  $M$ and Gaburro et al. $N$; Huang & Fu write $k$; Cernetic et al. define
  the degree $n$ and the order $p=n+1$ but label most figures, Table 1 and
  part of the text by the degree under the name $p$ (e.g. the text calls
  the degree-1, 3, 7 runs of Fig. 7 "order $p=2$, 4, 8" while the figure
  labels them $p=1$, 3, 7), so their $p$ is read from context. All are translated to $N$ here. Dzanic et al. use $u^+$ for
  the trace of the element of interest and $u^-$ for the neighbour, and
  Dzanic & Witherden print opposite labels in text and figure; this page
  writes inner and outer traces in words.
- Bai & Li (2022) state in their introduction that for DG "the local
  conservation can not be easily guaranteed" (§1), in a passing comparison
  with finite volumes, and give no argument. The statement is kept as
  theirs, not as a contradiction: no source argues the opposite in so many
  words, but the cell-average update above (Cui et al. (2024), Eq. (1.5))
  is a finite-volume update with single-valued fluxes and so is locally
  conservative on a fixed mesh, and the loss of conservation in Bai & Li's
  scheme comes from the cut-cell and ghost-fluid treatment and the
  deletion of isolated structures, whose mass loss they record (§2.5.3)
  *(compiler check, not in the sources)*.
- Maltsev et al. (2023) run their modal DG on the under-resolved
  inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  without over-integration, modal filtering or split-form fluxes; it does
  not crash, but they state that it is not free of aliasing errors
  (§3.6). Their Eq. (5) calls $\frac1{d!}\prod_{l=1}^d(N+l)$ the number of
  degrees of freedom $K$, but for $N=1$, $d=2$ it gives 3, the number of
  basis functions $K+1$ of their Eq. (2) *(compiler check, not in the
  sources)*.
- Liu & Wu (2025) read the $L^1$ orders 2.92, 4.24, 4.61, 3.55, 3.19 of
  their 2D sine wave (Table 2) as "consistently" third order. Only the
  finest pair is near 3. They print the 1D mesh column of Table 1 as
  "100 × 100" to "3200 × 3200" for a 1D problem. The printed orders
  match halving $\Delta x$ from 100 to 3200 cells, e.g.
  $\log_2(7.3204\times10^{-6}/8.0642\times10^{-7})=3.18$ *(compiler check,
  not in the sources)*.
- Luo et al.'s claim that the central flux suffices rests on the converged
  interface condition. It does not carry over to DG on a fixed mesh, where
  the sources above use upwind-type numerical fluxes.

# Citations

- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — §2.1 Eq. (2.2), Eq. (3.3), Prop. 4.6, Thm 4.1, §5.1 Table 1.
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Eq. (1.5), Eq. (7.2), Thm 7.1, Remark 7.7, Table 1, §8.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — Eqs. (6.6)–(6.8), Thm 6.4, §7.
- [Ding & Wu (2024b)](/sources/ding-2024-b.md) — §3.1 Eqs. (17)–(24), Remarks 1, 3, 6, Thm. 3.1; §4.3–4.7 Eqs. (57)–(74), Thms. 4.1–4.2, Cors. 4.1–4.2; §5.
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §2.2–2.4 Eqs. (7)–(28).
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §1, Remark 2, §8.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2, Ex. 2.3.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, §5.
- [Basile et al. (2022)](/sources/basile-2022.md) — §2.3 Eqs. (15)–(23) (author manuscript).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §2, §3.1–3.3 Eqs. (2.4)–(3.15) (author manuscript).
- [Li, Shu & Qiu (2022d)](/sources/li-2022-d.md) — §2.1 Eqs. (2.2)–(2.4), Eqs. (2.25), (2.32)–(2.34) (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — §3, §3.4 Fig. 1, §4 (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §2.1 Eqs. (6)–(9), §2.2 Eqs. (20)–(21), Ex. 2.3 (arXiv v4).
- [Bai & Li (2022)](/sources/bai-2022.md) — §1, Eqs. (3)–(6), §2.5.2–2.5.3 Eqs. (27)–(28), §2.6, Eq. (30), §3.1.4–3.1.5 Figs. 12–14.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §2.1–2.2, §3, §4.
- [Du & Yang (2022)](/sources/du-2022-b.md) — §3 Eqs. (3.2)–(3.5), Thms 3.1–3.2, Lemma 4.1, Thms 4.1–4.3, Table 6.2.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §4.1–4.2, §5, Table 1 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §2.2–2.3 Eq. (10), §4.2, Alg. 2, Tables 3–4 (arXiv v3).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §2 Eq. (2.23), §5.3.2.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §2.3 Eqs. (8)–(14), §4, Remark 5, §5.2.3 (arXiv v2).
- [Kou et al. (2022)](/sources/kou-2022.md) — §3 Eqs. (9), (15).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §4, §7.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §3.1, §4 Eq. (15) Thm. 4.1, §5 Remarks 1–2, §6 Thm. 6.2, §7 Eq. (57), Tables 3–9, App. B.1 (arXiv v2).
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2.1 Eqs. (2)–(9), §2.3 Eq. (32), §2.4 Eq. (33), §2.5, §3.1–3.2, §3.6, §4, Table 1, App. B Tables B.3–B.4.
- [Cao et al. (2026)](/sources/cao-2026.md) — §2.1–2.3, Thms 2.2, 2.4, 4.1; §6, Table 3.
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — accepted manuscript (arXiv v2): §2.3–2.5 Eqs. (13)–(23), §3.1–3.2 Eqs. (29)–(36), §4.1 Eqs. (43)–(46) Figs. 3–4, §5.1 Fig. 5, §5.3 Figs. 7–8, §6.3 Fig. 14.
- [Ciallella et al. (2024)](/sources/ciallella-2024.md) — arXiv v1: §3.2, §4 Fig. 1, §6.1 Tables 2, 4, §6.2 Table 10.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — arXiv v1: §3.1–3.3 Eqs. (22)–(34), §4.1–4.4 Props. 1–5, Eq. (67).
- [Huang & Fu (2024)](/sources/huang-2024.md) — §3 Eqs. (16)–(23), §4.3–4.4 Eqs. (32)–(50), §5.1–5.2, §6 Tables 1, 3.
- [Alberti et al. (2025)](/sources/alberti-2025.md) — §2 Eqs. (7), (11)–(15), §3.1.2.
- [Ching et al. (2025)](/sources/ching-2025.md) — §3 Eq. (3.2), §4.2–4.4 Eqs. (4.12), (4.17), (4.33), Thms. 6, 8, §4.7 Remark 11.
- [Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md) — §3.2 Eqs. (24)–(25), (36), §4, §7.3–7.4.
- [Liu & Wu (2025)](/sources/liu-2025.md) — arXiv v2: §2.4 Eqs. (14)–(35), Remarks 1–2; §3.2 Eqs. (45)–(49); §3.3–3.6 Eqs. (50)–(72), Thm. 1, Cors. 1–2, Remark 3; §4 Tables 1–2, §4.2.4, §4.2.6.
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §3.2 Eqs. (3.15)–(3.16), §3.3 Eq. (3.21).
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — §3.1 (degree convention).
- [Huang et al. (2025a)](/sources/huang-2025.md) — §2, §3, §4.
- [Zampa & Dumbser (2025)](/sources/zampa-2025.md) — arXiv v1: §3.2.2–3.2.3 Eqs. (7)–(10), §3.3.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — §2.1 Eqs. (2.8), (2.10), Remarks 2.1–2.2, Lemma 2.5, Thms. 2.6–2.7, 2.12; §3 Thms. 3.6, 3.10; §4 Tables 2–3, Figs. 9, 21.
