---
type: Method
title: "Discontinuous Galerkin method"
description: "The discontinuous Galerkin (DG) semi-discretization of a conservation law with piecewise polynomials of degree N coupled only through numerical fluxes, its modal, nodal and space–time variants, its Runge–Kutta time stepping and CFL limit, the cell-average update behind bound preservation, and the stabilization and adaptation strategies the sources attach to it."
status: established
aliases: [DG, RKDG, Runge–Kutta discontinuous Galerkin, modal DG, nodal DG, space–time DG, LDG, local discontinuous Galerkin, discontinuous spectral element method, DSEM]
tags: [dg, numerical-flux, limiting, bound-preserving]
timestamp: 2026-10-22T20:00:00Z
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
  read.
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
- **Moment equations with reconstruction.** [Li, Shu & Qiu (2022)](/sources/li-2022-d.md)
  test the conservation law with $1$ and $(x-x_i)/\Delta x$ on each cell
  (§2.1, Eqs. (2.2)–(2.4)). These two functions span $\mathbb P^1(I_i)$, so
  the equations are the weak form of $\mathbb P^1$ DG *(compiler check, not
  in the sources)*. They
  evolve the cell average and the first moment, but do not carry a DG
  polynomial: the point values needed by the flux and by the volume
  integral of $f(u)$ come from a multi-resolution Hermite-WENO
  reconstruction on a compact stencil, sixth order on three cells
  ([Hermite WENO](/methods/hermite-weno.md)).

Three further formulations:

- **Local DG for viscous terms.** [Du & Yang (2022)](/sources/du-2022-b.md)
  discretize the multi-species reacting Navier–Stokes equations by LDG: the
  gradient is an auxiliary DG variable solved element by element with a
  central flux, and the convective and diffusive fluxes are treated as one
  total flux with a single Lax–Friedrichs-type penalty (§3, Eqs.
  (3.2)–(3.5), after X. Zhang's positivity-preserving DG for Navier–Stokes).
  Yu & Hesthaven use an LDG-type mixed form with centred viscous fluxes for
  their artificial-viscosity term (§2), PyFR uses BR1 or BR2 (Dzanic et al.,
  §4.2; Dzanic & Witherden, §4.2).
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
stringent (Eq. (2.23)). For stiff chemistry, Du & Yang (2022) replace
SSP-RK by a third-order conservative modified exponential Runge–Kutta
method; on a stiff test with source coefficient $10^6$, SSP-RK3 at the
same step blows up on the two coarsest meshes and needs $\tfrac25$ of it
(Table 6.2).

Cui et al. (2024), Remark 7.7, cite the linear-stability restriction of
$\mathbb P^N$-DG with an $(N+1)$-stage Runge–Kutta method as an empirical
formula. In 2D it reads

$$\Delta t\Big(\frac{a^{(1)}}{\Delta x}+\frac{a^{(2)}}{\Delta y}\Big)\le\frac1{2N+1},$$

with $a^{(d)}$ the maximum wave speed in direction $d$. Peng et al. (2024)
run their OEDG tests at CFL $1/(2N+1)$ (§5). Peng et al.'s Prop. 4.6,
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
  Shu–Osher problem (§2.6, §3.1.5).
- **Blending with a low-order scheme.** The nodal DG update is convexly
  blended with a compatible subcell finite-volume update, element by element
  or interface by interface, with a priori or a posteriori blending
  coefficients
  ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  [convex limiting](/methods/convex-limiting.md); Rueda-Ramírez et al.
  (2022)).
- **Damping and filtering.** Oscillation-free DG adds stiff damping terms to
  the semi-discrete system. The [OEDG](/methods/oedg.md) method of Peng et al.
  (2024) instead solves the damping step exactly after each Runge–Kutta stage
  as a modal filter. This preserves the cell average and the scale and
  evolution invariance. For linear advection it keeps the optimal
  fully-discrete $L^2$ estimate $O(\Delta x^{N+1}+\Delta t^{r_{\mathrm{RK}}})$ under
  $N>d/2$, $r>d/2+1$, a stable underlying RKDG scheme and a lower bound on
  the deviation of $u_h$ from its average (Thm 4.1). Dzanic & Witherden
  (2022) filter instead with an exponential modal filter whose strength is
  chosen per element, after each Runge–Kutta stage, as the smallest one
  that makes the nodal values positive and satisfy a local minimum entropy
  bound ([entropy filtering](/methods/entropy-filtering.md)).
- **Artificial viscosity.** Two sources give sensors for nodal DG: the
  time-reversibility defect of Dzanic et al. (2022), which gives a
  separate viscosity for every conserved variable, and the modal decay
  rate predicted by a neural network of Yu & Hesthaven (2022). See
  [artificial viscosity](/methods/artificial-viscosity.md) and
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md).
- **Fitting the discontinuity.** Implicit shock tracking moves the element
  faces onto discontinuities, so that no limiter, reconstruction or
  artificial viscosity is needed. Luo et al. (2021) use a plain central
  flux at interior faces (§3.3,
  [implicit shock tracking](/methods/implicit-shock-tracking.md)).

[Pazner (2021)](/sources/pazner-2021.md) gives the
invariant-domain-preserving variant of the blending remedy. His low-order
scheme is a graph-viscosity method built on a sparsified, $O(1)$-stencil
derivative operator, and the high-order nodal DG update is limited
subcell by subcell (§3–4). Applying graph viscosity to the full DG operator
instead makes the low-order method more diffusive as $N$ grows at fixed
degrees of freedom, because each node couples to $O(N)$ others (§3.4,
Fig. 1; [convex limiting](/methods/convex-limiting.md)).

Li, Shu & Qiu (2022) flag troubled cells with a modified KXRCF indicator,
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

- **Sharp material interfaces.** Bai & Li (2022) keep the two fluids
  separate across a level-set interface. Ghost-fluid states and cut-cell
  mixing replace any smearing of the interface (see the cut-cell item
  above).

## Accuracy

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

## Qualifications

- The CFL bound $1/(2N+1)$ is cited by Cui et al. (2024) as an empirical
  formula, not a theorem.
- The sources use different symbols for the degree: Peng et al. and Cui
  et al. write $k$, Ranocha et al., Pazner, Luo et al. and Basile et al.
  write $p$, Wu & Shu write $K$, and Rueda-Ramírez et al. write $N$; Bai
  & Li, Du, Shu & Zhong and Du & Yang write $k$; Abgrall et al., Cicchino
  et al. and the two Dzanic papers write $p$; Yu & Hesthaven write $P$. All are translated to $N$ here. Dzanic et al. use $u^+$ for
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
- Luo et al.'s claim that the central flux suffices rests on the converged
  interface condition. It does not carry over to DG on a fixed mesh, where
  the sources above use upwind-type numerical fluxes.

# Citations

- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — §2.1 Eq. (2.2), Eq. (3.3), Prop. 4.6, Thm 4.1, §5.1 Table 1.
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Eq. (1.5), Eq. (7.2), Thm 7.1, Remark 7.7, Table 1, §8.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — Eqs. (6.6)–(6.8), Thm 6.4, §7.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §1, Remark 2, §8.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2, Ex. 2.3.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, §5.
- [Basile et al. (2022)](/sources/basile-2022.md) — §2.3 Eqs. (15)–(23) (author manuscript).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §2, §3.1–3.3 Eqs. (2.4)–(3.15) (author manuscript).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §2.1 Eqs. (2.2)–(2.4), Eqs. (2.25), (2.32)–(2.34) (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — §3, §3.4 Fig. 1, §4 (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §2.1 Eqs. (6)–(9), §2.2 Eqs. (20)–(21), Ex. 2.3 (arXiv v4).
- [Bai & Li (2022)](/sources/bai-2022.md) — §1, Eqs. (3)–(6), §2.5.2–2.5.3 Eqs. (27)–(28), §2.6, Eq. (30), §3.1.4–3.1.5 Figs. 12–14.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §2.1–2.2, §3, §4.
- [Du & Yang (2022)](/sources/du-2022-b.md) — §3 Eqs. (3.2)–(3.5), Thms 3.1–3.2, Lemma 4.1, Thms 4.1–4.3, Table 6.2.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §4.1–4.2, §5, Table 1 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §2.2–2.3 Eq. (10), §4.2, Alg. 2, Tables 3–4 (arXiv v3).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §2 Eq. (2.23), §5.3.2.
