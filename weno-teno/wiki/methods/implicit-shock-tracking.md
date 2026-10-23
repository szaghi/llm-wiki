---
type: Method
title: "Implicit shock tracking and moving DG (MDG-ICE)"
description: "Implicit shock tracking makes the mesh geometry an unknown and moves element faces onto discontinuities, by weakly enforcing the flux-jump condition (MDG-ICE; the MDG+ICE variant of Luo, Absillis and Nourgaliev) or by minimizing an enriched DG residual constrained by the DG equations (HOIST, made robust by Huang and Zahr, run slab by slab in space–time by Naudet and Zahr)."
status: established
aliases: [MDG-ICE, MDG+ICE, HOIST, space-time HOIST, slab-based HOIST, high-order implicit shock tracking, moving discontinuous Galerkin with interface condition enforcement, moving discontinuous Galerkin with interface conservation enforcement, implicit discontinuity tracking, shock fitting by optimization]
tags: [shock-tracking, dg, numerical-flux]
timestamp: 2026-10-23T23:55:00Z
---

# Implicit shock tracking and moving DG (MDG-ICE)

Shock capturing keeps the mesh fixed and lets the scheme smear a
discontinuity over a few cells. **Implicit shock tracking** instead makes
the positions of the mesh vertices unknowns, solved together with the flow.
The extra equations are the *interface condition*: across every element
face the normal flux is continuous,

$$[\![F(u_h)\cdot n]\!]=F(u_h^+)\cdot n-F(u_h^-)\cdot n=0,$$

with page-local $F$ the flux (space–time flux in unsteady problems) and $n$ the face normal. In a space–time formulation $F$
includes the time component $u$, and the condition is the
[Rankine–Hugoniot jump condition](/definitions/rankine-hugoniot-condition.md)
along a moving face. It holds automatically in smooth regions. Across a
discontinuity it can hold only if a face lies on the discontinuity, so
enforcing it drives faces onto shocks and contacts.
[Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) develop the
MDG+ICE variant of this approach for the compressible Euler equations
(§I–III).
[Huang & Zahr (2022)](/sources/huang-2022.md) group MDG-ICE with a second
method of the same class, the High-Order Implicit Shock Tracking (HOIST)
method of Zahr and Persson, which reaches the aligned mesh by optimization
rather than through the interface condition: both "discretize the
conservation law on a mesh without knowledge of the flow field and pose
an optimization problem over the discrete flow variables and nodal
coordinates", and only one topological mesh operation, element removal,
is needed (§1). Unlike explicit shock tracking, which fits a known
discontinuity as an internal boundary, neither needs the shock topology
in advance.

## MDG-ICE (Corrigan, Kercher & Kessler)

As recalled by Luo et al. (§3.2), the moving DG method with interface
condition enforcement (MDG-ICE) of Corrigan, Kercher and Kessler works as
follows:

- the flow is discretized by [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
  on space–time elements (or on space for steady problems);
- the space–time coordinates of the vertices are unknowns;
- the interface condition is tested against the *discontinuous* trace
  space, $\int_e[\![F(u_h)\cdot n]\!]\,v_h\,dS=0$ for all $v_h$ in that
  space (Eq. (3.6)).

For a 1D unsteady problem this gives $n_{\mathrm{face}}\times n_{\mathrm{basis}}\times n_{\mathrm{eqns}}$
equations for $2\,n_{\mathrm{poin}}$ geometric unknowns, an over-determined
and large system (Fig. 2; page-local counts of faces, face basis functions,
equations and vertices). Luo et al. credit the method with implicit
detection and tracking of all discontinuity types, rarefaction heads and
tails included, without a Riemann solver or a limiter.

## MDG+ICE (Luo, Absillis & Nourgaliev)

Luo et al. change three things (§3.2–3.5):

1. **Continuous trace space.** The interface condition is tested against
   the continuous, vertex-based trace space (Eq. (3.7)), as in embedded
   DG. This gives $n_{\mathrm{poin}}\times n_{\mathrm{eqns}}$ equations. For
   a scalar law the interface system is square.
2. **Time-fixed mesh and one slab per step.** Vertices move only in $x$,
   not in $t$. Each step solves one space–time slab $[t^n,t^{n+1}]$, with
   the $x$-coordinates of the vertices at $t^{n+1}$ as geometric unknowns.
   The interface condition is not enforced on the slab faces, where the
   flux is upwind "according to the causality principle" (Fig. 4). The 1D
   tests in the paper use a single slab over the whole time interval.
3. **No Riemann solver.** Since the interface condition defines the face
   flux at convergence (Eq. (3.14)), interior faces use the central average
   $\tfrac12\big(F(u_h^-)\cdot n+F(u_h^+)\cdot n\big)$ (Eq. (3.15)). No
   limiter, ENO/WENO reconstruction or
   [artificial viscosity](/methods/artificial-viscosity.md) is used. The
   authors state that an upwind space–time flux consistent with (3.14)
   "remains an open problem" (§3.3).

**Nonlinear solver.** The flow and geometry residuals form an
over-determined system $\mathbf R(\mathbf U)=0$, solved as
$\min\tfrac12\lVert\mathbf R\rVert^2$ by Levenberg–Marquardt and the
adaptive nonlinear least-squares algorithm of Dennis, Gay and "Walsh" (as printed; §3.4,
Eqs. (3.16)–(3.17)). The abstract calls the problem "regularized", but
§3.4 gives no regularization term or stopping criterion.

**Mesh management.** Elements next to an unfitted interface flatten as the
residual falls. Elements with a negative or too small Jacobian are removed
by edge swaps with cap removal, edge collapse for needles and an edge split
after each collapse, which keeps the numbers of triangles, points and
boundary faces fixed (§3.5, Figs. 6–7). The solver tolerates tangled
meshes and negative density or pressure during the iterations, but the
authors call solutions on tangled meshes "either non-physical or
meaningless".

## HOIST (Zahr & Persson; Huang & Zahr)

**Formulation** (Huang & Zahr §2–4, recalled from Zahr & Persson). A
steady law, or an unsteady one written as a steady law in space–time,
$\nabla\cdot F(u)=S(u)$ with page-local $F$, is discretized by
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) on simplices
with total degree $N$; the element map is continuous and of degree
$q_{\mathrm g}$ (page-local; the source's $q$). Let $\mathbf u$ be the DG
coefficients and $\mathbf x=\phi(\mathbf y)$ the nodal coordinates as a
function of free parameters $\mathbf y$ (page-local). With $\mathbf r$ the
standard DG residual (test degree $N$, smoothed upwind or smoothed Roe
flux with the Harten–Hyman entropy fix) and $\mathbf R$ the *enriched*
residual (test degree $N+1$, central flux), HOIST solves

$$\min_{\mathbf u,\mathbf y}\ \tfrac12\lVert\mathbf R(\mathbf u,\phi(\mathbf y))\rVert_2^2+\tfrac{\kappa_{\mathrm m}^2}2\lVert\mathbf R_{\mathrm{msh}}(\phi(\mathbf y))\rVert_2^2\quad\text{subject to}\quad \mathbf r(\mathbf u,\phi(\mathbf y))=0$$

(Eqs. (27)–(31); page-local mesh-penalty weight $\kappa_{\mathrm m}$, not
the kinetic energy, and $\mathbf R_{\mathrm{msh}}$ an element distortion
measure against an ideal element). The enriched residual is a surrogate
for the violation of the infinite-dimensional weak form; minimizing it
drives faces onto discontinuities, "which endows the method with
r-adaptive behavior" (§1). Because the constraint is the standard DG
system with an upwind flux, the authors state that HOIST inherits
consistency, conservation and stability of DG independently of the
objective; the central flux appears only in $\mathbf R$, "because it is
smooth and conservative" (Remark 5). No limiter or artificial viscosity is
used, and the solver never needs a converged DG solution on a
non-aligned mesh.

**Difference from MDG-ICE/MDG+ICE** *(compiler check, not in the
sources: comparison of Huang & Zahr's Remark 5 with Luo et al.'s
§3.3)*. MDG+ICE imposes the face condition as equations and uses a
central interior flux in the converged scheme; HOIST keeps an upwind DG
system as the constraint and uses the central flux only in the objective.
The two converged solutions are thus defined by different fluxes. Huang
& Zahr state that most of their developments "will apply to MDG-ICE with
minor modifications" (§1).

**Boundary-preserving parametrization** (§3.2, Eqs. (17)–(26)). The node
coordinates are an affine function $\mathbf x=A\mathbf y+\mathbf b$ built
from the normals of all planar boundaries through each node, so that
nodes stay on every planar boundary, edge and corner they start on;
directions of free motion are chosen greedily closest to the null space
of the normal matrix. Curved boundaries still need the earlier analytic
treatment.

**Solver** (§5.1). A sequential quadratic programming method with a
Levenberg–Marquardt Hessian approximation advances $(\mathbf u,\mathbf y)$
together, with a backtracking line search on an $\ell_1$ merit function.
Huang & Zahr change four parts of the solver of Zahr, Shi & Persson,
which they find "not sufficiently robust" for high Mach numbers and
complex discontinuity surfaces (§5.1.4): a new merit penalty parameter
(Eq. (46), after Nocedal–Wright), replacing one that caused scaling
mismatch and many line-search iterations; an isotropic linear-elasticity
mesh regularizer in the Hessian; an adaptive $\kappa_{\mathrm m}$ that
keeps the residual term slightly dominant, since a single a priori value
"does not work well in practice" (Eq. (51)); and three robustness
measures applied after each step during the first $M$ iterations
(page-local).

**Robustness measures** (§5.2).

1. *Element removal by edge collapse.* An element whose volume, edge
   ratio or Jacobian ratio is too small (four tests, Eqs. (56)–(60), with
   tolerances 0.2, $10^{-10}$, 0.2, 0 in four of the nine cases of Table A.4,
   varied in the others) has its shortest edge collapsed.
   This works for simplices of any degree in any dimension, since
   collapsing any edge of a simplex sends its volume to zero. The kept
   endpoint is the one on more boundaries; on a tie, the one where the
   multi-valued DG solution has the largest range, so that nodes on a
   shock stay on it.
2. *Straightening.* Curved elements with a small ratio of the infimum to
   the supremum of the map's Jacobian are made straight-sided instead of
   removed (Eq. (61)).
3. *Re-initialization.* Elements flagged by the Persson–Peraire modal
   sensor on density, and their neighbours not separated from them by a
   large jump, are reset to a patch average that does not cross the shock
   (Eqs. (62)–(69); [troubled-cell indicator](/definitions/troubled-cell-indicator.md)).
   Without it the solver stalls on the accelerating-shock Burgers problem
   at $N=3$ (Figs. 17–19).

The iteration starts from the shock-agnostic mesh and the first-order
finite-volume ($N=0$) solution for every $N$, which removes the degree
homotopy of the earlier method; an $L^2$ projection of the exact solution
or an artificial-viscosity solution as initial guess "did not offer
noticeable advantages" (§5.3, Remark 22). All element collapses occur in
early iterations (Remark 18).

**Evidence** (Huang & Zahr §6; $N=q_{\mathrm g}=2$ unless stated).

| test | mesh (initial → final elements) | result |
|---|---|---|
| 3D linear advection, planar and curved discontinuity | 324 tetrahedra, $N=0$ | 29 SQP iterations, residuals $O(10^{-10})$ and $O(10^{-8})$, no removal (planar); 12 collapses, $O(10^{-8})$ and $O(10^{-4})$ (curved) |
| space–time [Burgers](/benchmarks/burgers-equation-tests.md), accelerating shock | 72 triangles, $N=q_{\mathrm g}=1,2,3$ | shock tracked in about 20 iterations; refinement study in Table 2 |
| space–time Burgers, shock formation and merger | 400 triangles, $N=2,3$ | formation and the space–time triple point of the merger tracked from an uninformed mesh |
| quasi-1D nozzle, shock at $x=7.94$ | 12 elements, $N=2$ | "indistinguishable from the exact solution"; Persson–Peraire [artificial viscosity](/methods/artificial-viscosity.md) needs 50 elements at $N=4$ and smears the shock |
| space–time [Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md), $N=2$, $q_{\mathrm g}=1$ | 108 → 84 | shock, contact, rarefaction head and tail tracked, in that order (iterations about 27, 52, 66, 106) |
| Mach 2 diamond in a tunnel | 220 → 201 | all shocks and four triple points tracked; the slip line from the trailing-edge triple point is not |
| Mach 5 scramjet | 1442 → 1299 and 2679 → 2523 | the fine mesh tracks all discontinuities, the slip line included |
| Mach 2 flow over a sphere (3D) | 511 → 491 quadratic tetrahedra | stagnation pressure 5.6465 against 5.6404, 0.11 % |

The 0.11 % agrees with the normal-shock pitot formula at $M=2$,
$\gamma=1.4$, which gives $p_0/p_\infty=5.6404$ *(compiler check, not in
the sources)*. On the nozzle the observed rates of the $L^1$ density error
and of the shock-position error are near $N+1$ for $N=1$–$5$ (Table 3),
while the artificial-viscosity reference at $N=2$ converges below first
order, which the authors attribute to the smoothing of the discontinuity
and the corruption of the downstream solution (§6.3, Fig. 26).

## Slab-based space–time HOIST (Naudet & Zahr)

[Naudet & Zahr (2024)](/sources/naudet-2024.md) carry HOIST from steady
problems, and from the single space–time domains of Huang & Zahr, to
unsteady problems solved **slab by slab**: the law in $d'$ space
dimensions is written as a steady law in $d=d'+1$ dimensions on a slab
$\Omega_x\times(t_0,t_1)$, HOIST is applied to one slab, and the next
slab starts from the top of the previous one, with no global coupling in
time (§1, §2.2, §4). Embedding implicit tracking in a method-of-lines
time discretization, they state, suits only limited shock motion and
cannot handle shock–shock or shock–boundary interactions without complex
mesh operations; in space–time a moving shock is a stationary surface
and an intersection is a triple point (§1).

**Space–time fluxes from spatial ones** (§2.2, Eqs. (7)–(17)). With
space–time flux $[f(u)\ \ u]$ and unit normal $(n_x,n_t)$,
$n_x=\lvert n_x\rvert\eta_x$ (page-local symbols), the projected Jacobian is
$\lvert n_x\rvert A(u;\eta_x)+n_tI$, with the eigenvalues of the spatial
Jacobian scaled by $\lvert n_x\rvert$ and shifted by $n_t$ and the same
eigenvectors. Any linearized-Riemann flux of the form
$\tfrac12\big(F(u^+)+F(u^-)\big)\cdot n+\tfrac12\tilde A(u^+-u^-)$, among
them the [Roe](/methods/roe-riemann-solver.md), Vijayasundaram and
[Rusanov](/methods/lax-friedrichs-flux.md) fluxes, therefore has a
space–time version written entirely with spatial quantities; e.g. the
space–time Roe matrix is $R\,\big\lvert\lvert n_x\rvert\Lambda+n_tI\big\rvert\,L$
at the Roe average (Eq. (15)). The authors present this as removing "one
of the implementation burdens associated with space-time methods".
(The source's convention puts $W^+$ inside the element and $W^-$
outside, the reverse of the registry's $u^\pm$.)

**Slab meshes** (§3). The spatial mesh of a slab is taken from the top
of the previous slab, extruded into prisms and split into simplices,
because element removal by edge collapse, key to robust tracking, is
well defined for simplices in any dimension. Each prism face is split by
an orientation-independent rule and connected to a central node, giving
$N_d=dN_{d-1}+2$ simplices per prism, $N_2=4$, $N_3=14$, $N_4=58$ (Eq.
(35); a constrained Delaunay split gives 11 tetrahedra without a central
node); the larger splits were observed to make shock fitting more
robust (Remark 9). Curved high-order refinements are obtained by
splitting the straight parent element and mapping through the
isoparametric map, which keeps them conforming (Eqs. (31)–(34)).

**Slab-specific devices** (§4). The temporal coordinate of the top nodes
is a single extra unknown, so the optimizer can move the slab top onto a
shock–boundary interaction (the translating top boundary of an earlier
MDG-ICE work, Eq. (37)); the bottom of later slabs is fixed and
interpolated from the previous slab; time is rescaled, $t=t^\star\hat t$,
to keep space–time simplices well shaped; elements are $h$-refined where
the enriched residual or the Persson–Peraire modal sensor exceeds $1\,\%$
of its maximum (Eqs. (43)–(45); see
[troubled-cell indicator](/definitions/troubled-cell-indicator.md),
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)); and
regions of known upstream flow are removed and replaced by a shock
boundary condition. Each slab is solved by the SQP method of Huang &
Zahr from the DG($p=0$) solution on the reference mesh (Algorithm 1).

**Evidence** (§5; no convergence-order study, deferred to the
single-slab work):

| test | setup | result |
|---|---|---|
| [Burgers](/benchmarks/burgers-equation-tests.md), accelerating shock leaving the domain | 192 $P_2$ simplices, $S=1,2,4,8$ slabs | residuals converge faster and deeper as slabs are added (Fig. 9); shock boundary conditions remove over half of the elements (Fig. 11) |
| Burgers, shock formation and merger | 1 slab, 96 → 207 triangles after 8 refinement rounds | formation point resolved, agreement with a fine second-order FV run at $t=0.1$ |
| 2D Burgers, curved shock | 3 slabs, 448 $P_2$ tetrahedra in slab 1 | curving shock tracked |
| shallow-water [dam break](/benchmarks/dam-break-problem.md) with walls | 5 slabs, 32 triangles in slab 1 | shock and rarefaction tracked through the wall reflections |
| [Sod tube](/benchmarks/sod-and-lax-shock-tubes.md) with walls to $t=1$ | 6 slabs, 65 simplices in slab 1 | all waves, a generalized triple point, shock–shock and shock–contact interactions tracked |
| [Shu–Osher problem](/benchmarks/shu-osher-problem.md) to $T=2$ with a wall at $x=5$ | 5 slabs, refinement and shock boundary conditions | relative $L^2$ error $3.97\times10^{-4}$ against a second-order FV superbee reference |

When two events occur at nearly the same time, the single translating
top cannot track both on a coarse mesh; HOIST tracked the stronger
shock–contact interaction, and freeing the top nodes individually tracks
both but may violate causality, which no constraint enforces yet
(§5.3.1, Fig. 18). The authors call the extrude-and-split approach
inefficient in 3D and impractical in 4D space–time (§6).

## Why the jump condition fits discontinuities

Luo et al. verify the mechanism on Riemann data, along a straight
space–time face from $(x_i^n,t^n)$ to $(x_i^{n+1},t^{n+1})$ (Lemmas 1–2,
Eqs. (3.8)–(3.13)):

- **Linear advection**, $\partial_tu+a_0\partial_xu=0$ with page-local
  speed $a_0$: the interface condition holds iff
  $x_i^{n+1}=x_i^n+a_0(t^{n+1}-t^n)$, so the contact moves at the
  advection speed.
- **Burgers**, $\partial_tu+\partial_x(u^2/2)=0$: it holds iff
  $x_i^{n+1}=x_i^n+\tfrac12(u_l+u_r)(t^{n+1}-t^n)$, with page-local left
  and right states $u_l$, $u_r$, the Rankine–Hugoniot shock speed.

The intermediate equations (3.9) and (3.12) print a plus sign between the
two terms. With the face normal proportional to $(\Delta t,-\Delta x)$ the
sign is minus, and only then do the printed conclusions (3.10) and (3.13)
follow *(compiler check, not in the sources)*. No entropy condition enters:
the Burgers equation is satisfied equally by an entropy-violating jump with
$u_l<u_r$ *(compiler check, not in the sources)*.

## Evidence

| test | mesh | result (Luo et al.) |
|---|---|---|
| [Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md), $t=0.2$ | 8 space–time quadrilaterals, six degenerate at the origin | shock and contact fitted as true discontinuities; rarefaction head and tail "virtually resolved exactly" at $N=2,3$; an initial grid with a negative-volume element changes nothing significant |
| Lax problem, $t=0.15$ | 8 quadrilaterals | same behaviour |
| [123 (receding-flow) problem](/benchmarks/double-rarefaction-problem.md), $t=0.15$ | 16 quadrilaterals, $N=2$ | the two cells at the initial jump collapse and are removed; profiles without "overheating" |
| Noh problem, $\gamma=5/3$, $t=1$ | 4 quadrilaterals, $N=1$ | residuals reach $10^{-8}$–$10^{-9}$ in about 50 iterations; solution "virtually identical" to the exact one |
| Mach 3 flow past a 15° wedge | 189 triangles, $N=1$ | oblique shock fitted in about 20 iterations |
| Mach 2 diamond wedge in a channel | 500 triangles, $N=1$ | shock reflection, shock–shock interaction and expansion fan resolved |
| half cylinder at $M_\infty=8$ and $15$ | 315 and 497 triangles, $N=1$ | bow shock fitted, no [carbuncle](/definitions/carbuncle-phenomenon.md) |

The space–time elements are tensor-product, of degree $N$ in each variable
*(compiler check, not in the sources: the printed abscissae equal
$\log_{10}(1/\sqrt{(N+1)^2\cdot3\cdot8})$)*. Under p-refinement the $L^2$ space–time density error falls with slopes
8.75 and 10.48 (Sod) and 6.59 and 8.44 (Lax) against
$\log(1/\sqrt{\mathrm{DOFs}})$, three degrees per problem (§IV.A–B,
Tables 1). No test compares with a shock-capturing scheme.

## Qualifications

- **Scope of the claims.** The authors write that MDG+ICE reaches "the
  formal rate of p-convergence even for discontinuous solutions … that no
  other numerical methods can", and that it removes overheating "which no
  other numerical methods can". The first rests on three data points per
  problem. They cite but do not discuss the optimization-based implicit
  shock tracking of Zahr & Persson (ref. 44); see *Uniqueness of
  high-order convergence* below.
- **"Interface conservation" is not discrete conservation.** Luo et al.
  write that shock capturing has "a fatal flaw" because interface
  conservation "can never be achieved for discontinuities" (§I). Their
  interface conservation is the pointwise face condition above. A
  conservative shock-capturing scheme is discretely conservative, which is
  what the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) uses;
  the two statements concern different properties *(compiler check, not
  in the sources)*.
- **Stability of the central flux.** The central interior flux is said to
  enhance stability for under-resolved flows. The paper attributes
  stability to the converged interface condition and gives no analysis.
- **"Optimal" rates in HOIST.** Huang & Zahr's captions say the
  segment-wise slopes tend "to at least the optimal rate ($p+1$)". Their
  printed slopes mostly support this for the shock position, but the
  final-segment slopes of the Burgers solution error are 2.88 ($N=2$) and
  3.73 ($N=3$) and decrease with refinement (Table 2), and on the nozzle
  the density slope at $N=2$ falls to 2.26 and the shock-position slope at
  $N=4$ to 4.50 (Table 3). "Optimal" holds approximately, not uniformly.
- **Shock capturing called globally first order.** Huang & Zahr write
  that limiters, WENO and artificial viscosity are first order near shocks,
  "which translates into a globally first-order accurate scheme" (§1). The
  paper's own evidence is the sub-first-order $L^1$ convergence of one
  artificial-viscosity run on the nozzle (§6.3); no capturing scheme is
  run on the other problems. Their remark that WENO has "not
  been demonstrated on unstructured meshes for practical problems" is
  theirs; this bundle holds unstructured WENO-type reconstructions
  ([WLS-ENO](/methods/wls-eno.md),
  [unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md)).
- **Positivity during the iterations.** Huang & Zahr state that accepted
  iterates cannot have negative density or pressure because the line
  search guarantees a sufficient decrease of the merit function
  (Remark 20). No argument is given; MDG+ICE, by contrast, tolerates
  negative states during the iterations.
- **Printed slips in Huang & Zahr.** The initial condition of the
  accelerating-shock Burgers problem (Eq. (78)) prints a constant right
  state $-\mu_2$, which contradicts their exact solution (79) and shock
  path (80); these two are consistent with each other and with the
  Rankine–Hugoniot speed, and correspond to the right state
  $\mu_2(z-1)$ at $t=0$ (page-local parameters $\mu_1=4$, $\mu_2=3$ and
  space coordinate $z$) *(compiler check, not in the sources)*. Eq. (21)
  prints $Z_I\hat x^u_I$ where its derivation and Eq. (22) need
  $B_IZ_I\hat x^u_I$, and §5.2.2 gives one straightening tolerance (0.05)
  where Table A.4 lists per-case values.
- **Uniqueness of high-order convergence.** Luo, Absillis & Nourgaliev
  (2021) write that the MDG method attains "the formal rate of
  p-convergence even for discontinuous solutions and solutions with
  singularities, that no other numerical methods can to the best of our
  knowledge" (§IV.A), and in the abstract and conclusions an "exponential rate of
  convergence" on the Sod and Lax tubes, citing but not discussing Zahr &
  Persson's HOIST. Huang & Zahr (2022) report for HOIST h-convergence at
  rates near $N+1$ for both the solution and the shock position on
  discontinuous Burgers and quasi-1D nozzle problems (Tables 2–3) and
  claim "the optimal convergence rate of the underlying discretization
  even for flows containing discontinuities" (abstract). The two claims
  concern different refinements (p against h); Huang & Zahr make no
  p-convergence claim and do not discuss Luo et al.'s, so the sources do
  not contradict each other. Moved here from *Contradictions* at the
  chunk-4 deep lint (2026-10-23).
- **First-order claim.** Naudet & Zahr state that shock-capturing
  methods reduce the accuracy "near discontinuities, and therefore
  globally, to first-order", and that their accuracy "will always be
  limited to first-order" (§1), without naming a norm or a region. The
  reconstruction pages of this bundle report design-order convergence on
  smooth solutions (e.g. [WENO-JS](/methods/weno-js-reconstruction.md)).
- **Printed slips in Naudet & Zahr.** The accelerating-shock initial
  condition (Eq. (47)) prints the same constant right state $-\mu_2$ as
  Huang & Zahr's Eq. (78) above, while their exact solution and shock
  path (Eqs. (48)–(49)) again correspond to $\mu_2(x-1)$; Remark 10
  speaks of splitting a triangular prism into four tetrahedra, while
  every split without added vertices has three *(compiler check, not in
  the sources)*; and the Shu–Osher slab is described as 20 spatial
  elements giving 160 simplices, where the $N_2=4$ split used elsewhere
  gives 80 *(compiler check, not in the sources)*.
- **Title.** Page 1 of the manuscript read says "Interface Conservation
  Enforcement"; the published title, per Crossref, says "interface
  condition enforcement".

# Citations

- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §I, §3.1–3.5 Eqs. (3.1)–(3.17), Lemmas 1–2, Figs. 2–7, §IV.A–E Figs. 8–28, Tables 1, §V (author manuscript).
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §1, §2.2 Eqs. (7)–(17), §3 Eqs. (29)–(35), Remarks 9–10, §4 Eqs. (36)–(45), Algorithm 1, §5 Figs. 9–21, §6.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §1, §2–3 Eqs. (1)–(26), §4 Eqs. (27)–(37), Remarks 5–8, §5.1 Eqs. (38)–(55), Remarks 9–11, §5.2 Eqs. (56)–(70), Remarks 13–20, §5.3 Remark 22, §6 Eqs. (78)–(87), Tables 2–3, Figs. 13–34, App. A Table A.4 (arXiv v2).
