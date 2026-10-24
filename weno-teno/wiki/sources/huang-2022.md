---
type: Source
title: "Huang & Zahr (2022) — A robust, high-order implicit shock tracking method for simulation of complex, high-speed flows"
description: "Makes high-order implicit shock tracking (HOIST) robust: a boundary-preserving affine node parametrization, a modified SQP solver with new merit penalty and adaptive mesh penalty, and element collapse, straightening and re-initialization, so that a shock-agnostic mesh converges to a shock-aligned DG solution at near-optimal rates."
resource: "doi:10.1016/j.jcp.2022.110981"
source_kind: paper
authors: [Huang T., Zahr M.J.]
year: 2022
venue: "J. Comput. Phys. 454:110981"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Huang_A_robust_high-order_implicit_shock_tracking_method_for_simul.pdf"
tags: [shock-tracking, dg, space-time, unstructured-mesh]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper makes the High-Order Implicit Shock Tracking (HOIST) method of Zahr
& Persson robust for complex high-speed flows
([implicit shock tracking](/methods/implicit-shock-tracking.md)). HOIST is a
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) discretization on
a mesh whose nodal coordinates are unknowns: the standard DG residual (upwind
or [Roe](/methods/roe-riemann-solver.md) flux with the Harten–Hyman entropy
fix) is the constraint of an optimization problem whose objective is the DG
residual in an enriched test space of degree $N+1$ plus a mesh-distortion
penalty. Minimizing it drives element faces onto discontinuities, so shocks
become inter-element jumps and no limiter or
[artificial viscosity](/methods/artificial-viscosity.md) is needed. Unlike
explicit shock tracking, which computes the shock motion from the
[Rankine–Hugoniot conditions](/definitions/rankine-hugoniot-condition.md),
HOIST does not impose them (§1, §2.1).

Three contributions: an automatic affine node parametrization that keeps every
node on the planar boundaries it starts on; a modified SQP solver
(Levenberg–Marquardt Hessian, new $\ell_1$ merit penalty, adaptive mesh
penalty, linear-elasticity regularizer); and three robustness measures applied
in the early iterations: shock-aware edge collapse that removes degenerate
simplices, straightening of ill-conditioned curved elements, and
re-initialization of elements flagged by the Persson–Peraire modal sensor
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)) to a
patch average that does not cross the shock. The solver then starts from a
shock-agnostic mesh and the first-order finite-volume solution for any degree.
The authors call this "r-adaptive behavior" (§1); the nodes move as unknowns of the
optimization, not under a monitor function as in a [moving mesh](/methods/adaptive-moving-mesh.md).

Nine tests cover 3D linear advection, space–time
[Burgers](/benchmarks/burgers-equation-tests.md) (accelerating shock; shock
formation and merger), a quasi-1D nozzle against Persson–Peraire artificial
viscosity, the space–time [Sod tube](/benchmarks/sod-and-lax-shock-tubes.md), a
Mach 2 [diamond-wedge channel](/benchmarks/supersonic-diamond-wedge-channel.md),
a Mach 5 scramjet and Mach 2 flow over a sphere. Convergence is close to
$O(h^{N+1})$ in solution and shock position, though not uniformly on the finest
meshes. The paper dismisses [WENO](/methods/weno-js-reconstruction.md)-type
capturing as needing large stencils. It does not discuss the
[carbuncle](/definitions/carbuncle-phenomenon.md) or
[HLL-type solvers](/methods/hll-riemann-solvers.md).

# Version read

arXiv:2105.00139v2 [math.NA] (margin stamp 13 Jan 2022, footer "Preprint
submitted to Elsevier, January 14, 2022"), 45 pages, all read, text extraction
clean; not the typeset version of record, and the preprint prints no DOI. Page 1
title and authors match Crossref. Equation, remark, table and reference
numbers cited here are those of this preprint.

# Key claims

Registry notation (see the notation map): the source's DG degree $p$ is $N$,
its mesh-mapping degree $q$ is $q_{\mathrm g}$, its state $U$ is $u$, its
velocity $v$ and pressure $P$ are $v$, $p$; its optimization variables
$(u,x,y)$ are written $(\mathbf u,\mathbf x,\mathbf y)$ and its mesh penalty
$\kappa$ is $\kappa_{\mathrm m}$, as on
[implicit shock tracking](/methods/implicit-shock-tracking.md).

1. Shock-capturing approaches (limiters, WENO, artificial viscosity) are first-order near shocks, "which translates into a globally first-order accurate scheme" (§1). **Stated**
2. HOIST and MDG-ICE form the class of implicit shock tracking: both discretize on a mesh made without knowledge of the flow and solve an optimization problem over flow variables and nodal coordinates whose solution is a discontinuity-aligned mesh; the only topological operation needed is element removal (§1). **Stated**
3. Planar boundaries and their intersections are preserved exactly by the affine parametrization $\mathbf x=A\mathbf y+\mathbf b$ built from the boundary normals at each node, provided no element inverts (§3.2, Eqs. (17)–(26)). **Derived**
4. Because the standard DG equations with upwind flux are the constraint, HOIST inherits consistency, conservation and stability of DG independently of the objective; the enriched residual uses a central flux "because it is smooth and conservative" (Remark 5). **Stated**
5. The $\ell_1$ merit penalty $\mu_k$ of Eq. (46) ($\varpi=1.2$, $\rho=0.95$) replaces $\mu_k=2\lVert\hat\lambda(z_k)\rVert_\infty$ of Zahr et al. (2020), which caused scaling mismatch and many line-search iterations (§5.1.1, Remark 9). **Stated**
6. The mesh regularizer is an isotropic linear-elasticity stiffness matrix (modulus inversely proportional to reference element volume) instead of independent Poisson stiffness matrices; "Both choices lead to similar performance" (Remark 10). **Stated**
7. A single a-priori mesh penalty $\kappa_{\mathrm m}$ "does not work well in practice"; the adaptive rule (51) keeps the residual term slightly dominant over the mesh term, and its updates stop on their own (Remark 11). **Derived** (heuristic)
8. The baseline SQP solver of Zahr et al. (2020) "is not sufficiently robust" for high-Mach flows and complex discontinuity surfaces (§5.1.4). **Stated**
9. Element removal by collapsing the shortest edge is well defined for simplex meshes of any polynomial degree in any dimension, since collapsing any edge of a simplex sends its volume to zero (§5.2.1). **Derived**
10. Collapse endpoint rule: keep the endpoint on more boundaries (boundary preservation, a hard constraint); on ties keep the endpoint where the multi-valued DG solution has the largest range (shock preservation) (§5.2.1, Figs. 5–7). **Stated** (design rule, illustrated)
11. Re-initializing oscillatory elements (Persson–Peraire sensor, Eq. (62)) and their non-shock-crossing neighbours to a patch average is necessary for robust convergence: for the accelerating Burgers shock at $N=3$ the solver stalls without it (Fig. 19 against Figs. 17–18). **Shown**
12. Negative pressures or densities cannot occur at accepted iterates because the backtracking line search guarantees sufficient decrease of the merit function (Remark 20). **Stated** (argued, no proof)
13. All element collapses occur in early iterations, so the optimization problem is fixed in the asymptotic regime (Remark 18). **Shown** (observed)
14. The SQP starts from the shock-agnostic mesh and the first-order finite-volume ($N=0$) solution for every $N$, $q_{\mathrm g}$; the degree homotopy of Zahr et al. (2020) is no longer needed, and $L^2$-projected exact or artificial-viscosity initial guesses "did not offer noticeable advantages" (§5.3, Remark 22). **Shown** / **Stated**
15. Planar 3D advection: 29 SQP iterations bring the DG residual to $O(10^{-10})$ and the enriched residual to $O(10^{-8})$ with no element removed, Newton-like after iteration 23 (§6.1.1, Fig. 13). **Shown**
16. Curved 3D advection ($q_{\mathrm g}=2$): residuals reach $O(10^{-8})$ and $O(10^{-4})$ with 12 collapses and no Newton-like convergence, attributed to the exact solution not lying in the nonlinear approximation space (§6.1.2). **Shown** (attribution Stated)
17. Accelerating Burgers shock: 1, 1 and 7 elements removed for $N=1,2,3$; the discontinuity is mostly tracked after 20 iterations; "$p=2$ tends to be the 'sweet' spot" (§6.2.1). **Shown**
18. Accelerating Burgers shock, $h$-refinement: "optimal convergence rate for $E_\phi$ and better-than-optimal convergence rates in $E_{z_s}$" (§6.2.1, Table 2, Fig. 20). **Shown**; the final-segment $E_\phi$ slopes for $N=2,3$ are 2.88 and 3.73 (see Printed slips).
19. Shock formation and merger in space–time Burgers are tracked from a mesh with no knowledge of them; in under-resolved formation regions a steep continuous feature is represented by a growing discontinuity (§6.2.2, Figs. 21–22). **Shown**
20. Nozzle: $N=2$ HOIST on 12 elements is "indistinguishable from the exact solution"; Persson–Peraire artificial viscosity needs 50 elements at $N=4$ for a similar solution, with the shock smeared; HOIST converges in about 20 SQP iterations (§6.3, Figs. 24–25). **Shown**
21. Nozzle, $h$-refinement: HOIST "achieves optimal convergence rates, $O(h^{p+1})$, for all polynomial degrees considered for both error metrics", while artificial viscosity at $N=2$ is "limited to sub-first-order convergence rate" (§6.3, Table 3, Fig. 26). **Shown**; see Printed slips for the finest-level slopes. *(compiler check, not in the sources: recomputing the slopes of Tables 2–3 as $\log(E_i/E_{i+1})/\log(h_i/h_{i+1})$ from the printed data reproduces every printed slope to within $\pm0.02$.)*
22. Space–time Sod ($N=2$, $q_{\mathrm g}=1$): 108 → 84 elements; shock, contact and rarefaction head and tail are tracked, in order of strength (shock near iteration 27, contact 52, head 66, tail 106) (§6.4.1, Fig. 29). **Shown**
23. The enriched-residual objective tracks both discontinuities and continuous features with discontinuous derivatives (rarefaction head and tail) (§6.4.1). **Shown**
24. Mach 2 diamond ($N=q_{\mathrm g}=2$): 220 → 201 elements; all shocks and four generalized triple points tracked; the slip line from the trailing-edge triple point is not tracked on this coarse mesh (§6.4.2, Remark 23). **Shown**
25. Mach 5 scramjet ($N=q_{\mathrm g}=2$): 1442 → 1299 and 2679 → 2523 elements; the fine mesh tracks every discontinuity from the inlet corner, slip line included, which the coarse mesh tracks only partially (§6.4.3, Figs. 33–34). **Shown**
26. Mach 2 sphere (3D, $N=q_{\mathrm g}=2$): 511 → 491 quadratic tetrahedra; stagnation pressure 5.6465 against the analytical 5.6404, relative error 0.11% (§6.4.4). **Shown**. *(compiler check, not in the sources: the Rayleigh pitot formula at $M=2$, $\gamma=1.4$ gives $p_{02}/p_\infty=5.6404$, so the pressure is scaled by the free-stream static pressure and $\gamma=1.4$, neither printed.)*
27. For the sphere the ideal elements must be the reference elements; driving elements to equilateral tetrahedra caused many collapses near the fixed sphere surface, "which can cause the HOIST simulation to fail" (Remark 24). **Shown** / **Stated**
28. A shock-capturing method would need many more elements near all discontinuity surfaces and triple points of the diamond problem (§6.4.2). **Stated** (no capturing run shown)
29. Open issues: iterative solvers and preconditioners for the SQP system, boundary-preserving parametrization of curved boundaries, viscous laws, slab-based space–time for complex unsteady flows (§7). **Stated**

# Printed slips

- Eq. (78), accelerating Burgers shock: the initial condition is printed $\phi_0(z)=\mu_1H(-z)-\mu_2H(z)$, a constant right state $-3$, which would give a constant shock speed $0.5$; the exact solution (79) at $t=0$ gives $\mu_2(z-1)$ for $z>0$. *(compiler check, not in the sources: $u=\mu_2(z-1)/(1+\mu_2t)$ solves Burgers, and the shock path (80) satisfies the Rankine–Hugoniot speed against it; (79)–(80) are consistent and the intended datum is $\mu_1H(-z)+\mu_2(z-1)H(z)$.)*
- Eq. (80): "$z_s$ … is the shock speed"; $z_s(t)$ is the shock position.
- Eq. (21): "$[B_IY_I]^{-1}(B_I\hat X_I-Z_I\hat x_I^u)$" mixes dimensions; substituting (20) into (19) gives $B_IZ_I\hat x^u_I$, as Eq. (22) has.
- Eq. (30): $R_{msh}$ is given domain $\mathbb R^{N_y}$ but acts on $\phi(y)\in\mathbb R^{N_x}$; Eq. (36): $c$ has codomain $\mathbb R^{N_u}$ but $N_y$ components; Eq. (45): "$f(z+\alpha\Delta z_k)$" should read $z_k$.
- §6.1.1: "$\partial\Omega_{i+d}$ has outward unit normal $\eta_i=e_i$" should be $\eta_{i+d}=e_i$.
- §6.4.3: "similar features to the diamond case (Section 6.4.3)"; the diamond case is §6.4.2.
- Table 2 caption ("slope … tends to at least the optimal rate ($p+1$)") against the printed $m(E_\phi)$: 5.88, 3.92, 2.88 for $N=2$ and 6.60, 5.21, 3.73 for $N=3$, falling below $N+1$ on the finest segment.
- Table 3: same caption; $m(E_\rho)$ for $N=2$ is 3.00, 2.84, 2.26, $m(E_{x_s})$ for $N=2$ is 2.94, 2.90, 2.92 and for $N=4$ ends at 4.50.
- §5.2.2: "$c_{14}=0.05$ in this work", against per-case values 0.01, 0, $10^{-4}$ in Table A.4.
- Remark 11 writes $f_{msh}(u_k)$ for $f_{msh}(y_k)$; §5.2.3 writes $\mathcal E_{init}$ for $\mathcal E_{reinit}$.
- References [18] and [20] are the same Harten & Hyman (1983) paper, printed twice; ref. [24] (Kercher & Corrigan, Comput. Math. Appl.) prints no volume and the page range 1490–1519 of ref. [25]; ref. [14] "January January 2018"; "Discontinous" (ref. [10], §1).

# Notation map

| Huang & Zahr (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\nabla\cdot F(U)=S(U)$ | $\sum_d\partial_{x_d}f^{(d)}(u)=S(u)$ | $d$ counts space–time dimensions for unsteady problems |
| $U$; $\rho$, $v$, $E$, $P$ | $u$; $\rho$, $v$, $E$, $p$ | **the source's $p$ is the DG degree** |
| $p$, $p'=p+1$ | $N$, $N+1$ | DG solution and enriched test degrees |
| $q$ | $q_{\mathrm g}$ | degree of the mesh mapping; **$q$ is the weight exponent in the registry** |
| $\mathcal G$, $G$, $g$ | kept, $J$ | domain map, deformation gradient, Jacobian determinant |
| $r$, $R$ | $\mathbf r$, $\mathbf R$ | standard and enriched DG residuals; **$r$ is the stencil size and $R$ the eigenvector matrix in the registry** |
| $u$, $x$, $y$, $z=(u,y)$ | $\mathbf u$, $\mathbf x$, $\mathbf y$, $z$ | DG coefficients, nodal coordinates, free coordinates, combined variable |
| $\phi(y)=Ay+b$ | kept | node parametrization; **$\phi$ is also the Burgers unknown (§6.2)** |
| $f=f_{err}+\kappa^2f_{msh}$, $R_{msh}$ | kept, $\kappa\to\kappa_{\mathrm m}$, $R_{msh}\to\mathbf R_{\mathrm{msh}}$ | objective; **$f$ is the flux and $\kappa$ the kinetic energy in the registry** |
| $\alpha_k$, $\varphi_k$, $\mu_k$, $\varpi$, $\rho$ | kept | line search; **$\alpha$ collides with $\alpha_k$, $\varpi$ with the boundary weight, $\rho$ with density** |
| $\gamma_k$, $\tau$, $\sigma_{1,2}$, $D_k$ | kept | regularization and its adaptation; **$\gamma$, $\tau$ collide with the gas constant and the WENO-Z indicator** |
| $s_e$, $\chi$, $\Pi_{p-1}$ | kept | Persson–Peraire sensor on the density, projection on degree $N-1$ |
| $c_1,\dots,c_8$, $c_{14}$ | kept | removal, straightening and re-initialization tolerances; $c_{14}$ is a name |
| $\bar{\mathcal H}$ | $h(u^-,u^+)$ | numerical flux in reference coordinates |
| $\mu_1$, $\mu_2$ | kept | problem parameters (Burgers states, nozzle areas) |
| $\gamma$ | $\gamma$ | ratio of specific heats; value not printed |

# Reference list

48 printed references in numbered style, alphabetical order, all parsed and
merged complete into the [bibliography](/bibliography.md) with `citedby`
`huang-2022`. Refs. [18] and [20] are the same Harten & Hyman (1983) work
printed twice and are merged as one entry; ref. [24] prints no volume and a
page range identical to ref. [25], kept as printed; refs. [11] and [14] are
AIAA papers, refs. [15] and [21] arXiv preprints; ref. [47] (AIAA J. 59(1))
prints the year 2020. Three Zahr 2020 works and two Corrigan 2019 works are
told apart by venue.

# Pages created or updated

Chunk 4 (2026-10-22), cited further in chunks 5–11 (2026-10-22/24). This source is cited on:

* [Adaptive moving mesh finite differences](/methods/adaptive-moving-mesh.md)
* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Implicit shock tracking and moving DG (MDG-ICE)](/methods/implicit-shock-tracking.md)
* [Rankine–Hugoniot jump condition](/definitions/rankine-hugoniot-condition.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Supersonic flow in a diamond-wedge channel](/benchmarks/supersonic-diamond-wedge-channel.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
