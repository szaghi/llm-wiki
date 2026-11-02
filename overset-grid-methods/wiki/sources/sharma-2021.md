---
type: Source
title: "Sharma et al. (2021) — Overset meshes for incompressible flows: On preserving accuracy of underlying discretizations"
description: "Studies how overset information exchange affects incompressible-flow accuracy: verifies when linear fringe interpolation suffices and when higher order is needed as the overlap shrinks with the mesh, adds a polynomial-augmented RBF point-cloud interpolation, and compares a single coupled linear system with additive-Schwarz coupling."
resource: "doi:10.1016/j.jcp.2020.109987"
source_kind: paper
authors: [Sharma A., Ananthan S., Sitaraman J., Thomas S., Sprague M.A.]
year: 2021
venue: "J. Comput. Phys. 428:109987"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2021_Crossref_Journal_of_Computational_Physics_Sharma_Overset_meshes_for_incompressible_flows_On_preserving_accura.pdf"
tags: [overset-grid, interpolation, incompressible, finite-volume, hole-cutting]
timestamp: 2026-11-02T14:53:00Z
---

# Summary

Sharma, Ananthan, Sitaraman, Thomas and Sprague study how data exchange between [overset
meshes](/definitions/overset-grid.md) affects the accuracy and cost of [incompressible
flow](/methods/incompressible-flow-on-overset-grids.md) simulations. The setting is blade-resolved
wind-farm simulation with Nalu-Wind (second-order node-centred finite volumes, BDF2, incremental
approximate projection) and the TIOGA assembler, whose [implicit hole
cutting](/methods/implicit-hole-cutting.md) counts a preset number of cells. Its [point
classification](/definitions/point-classification.md) is field, fringe and hole; its [domain
connectivity](/definitions/domain-connectivity.md) is said to be interchangeable with other
assembly tools.

**Fringe interpolation.** Because TIOGA counts cells, the overlap $d$ between the [fringe
points](/definitions/fringe-point.md) of two meshes shrinks with the mesh, $d\propto h$. The paper
restates the [interpolation-order requirement](/results/interpolation-order-requirement.md) of
Chesshire & Henshaw: with constant $d$, linear interpolation ($q=2$) keeps second order; with
$d\propto h$ it does so for first-order PDEs but not for second-order (elliptic) ones, which need
$q\ge3$. Model problems on Cartesian meshes confirm it with tensor-product Lagrange [inter-grid
interpolation](/methods/inter-grid-interpolation.md). For unstructured donors the paper proposes a
Gaussian radial-basis-function interpolation on a point cloud, augmented with polynomials and
rearranged into shape functions so that it can enter a single linear system. Quadratic augmentation
is needed for elliptic second order; construction costs about 5 times Lagrange and grows
quadratically with the cloud size. Larger stencils also burden the [donor
search](/methods/donor-search.md).

**System coupling.** An overset single system, with the interpolation equations as constraint rows
(a solver-level coupling, discussed on [explicit and implicit
interpolation](/definitions/explicit-and-implicit-interpolation.md); the stencils themselves hold
field points only), is compared with overset
additive Schwarz, which solves each mesh separately and updates fringes in Jacobi fashion. The
elliptic proxy needs up to 153 Schwarz iterations; the hyperbolic one needs two.

Nalu-Wind tests use a manufactured solution ([twilight-zone flow](/methods/twilight-zone-flow.md)),
a decaying [Taylor vortex](/benchmarks/taylor-green-vortex.md) and [flow past a stationary and a
rotating cylinder](/benchmarks/flow-past-circular-cylinder.md), the latter on a [moving
mesh](/methods/moving-overset-grid.md). Linear interpolation with 2–4 Picard iterations and one
Schwarz iteration stays within 1 % of the single system. Extra Picard iterations beat extra Schwarz
iterations: splitting errors dominate. The paper accepts non-conservative interpolation away from
shocks, leaving [conservative interfaces](/methods/conservative-overset-interface.md) out of scope.
For the parallel setting see [parallel overset grid
assembly](/methods/parallel-overset-grid-assembly.md).

# Version read

The Elsevier typeset version of record, J. Comput. Phys. 428 (2021) 109987, 29 pages, all read;
Eqs. (3)–(6), (9)–(25), (27), (29)–(31), Algorithms 1–2 and Table 1 were also checked visually.
Page 1 matches Crossref in title, the five authors in order, and DOI. Numbering below is that of
this version.

# Key claims

The paper writes $O(\psi)$ for the polynomial degree of the interpolant, so its $O(\psi)=1$ is
$q=2$ and $O(\psi)\ge2$ is $q\ge3$; its $O(PDE)$ is the PDE order $2s$.

1. Interpolating the solution does not guarantee global conservation, but the loss does not degrade
   the solution if the overlap is away from shocks; incompressible schemes have no shocks, though
   mass conservation may matter for the pressure correction. (§1) **Stated**
2. Points are field points (equations solved), fringe points (interpolated values; their sources
   are donor points) and hole points (no solution). (§1, Fig. 1) **Stated**
3. After Chesshire & Henshaw, for second-order discretizations: if $d$ is constant under
   refinement, $q=2$ suffices; if $d\propto h$, $q=2$ suffices for $2s=1$ while $q\ge3$ is required
   for $2s=2$. (§3.1) **Stated**, verified below
4. TIOGA marks as mandatory fringe the nodes of a preset number of cells inward from each outer
   boundary, then keeps a preset number of nodes beyond them as field points on both meshes so that
   $d>0$, "which would otherwise result in a singular system"; without intervention $d$ shrinks with
   refinement. (Fig. 4) **Stated**
5. Elliptic proxy, single system, $d=3h$: linear Lagrange interpolation ($q=2$) degrades second
   order; quadratic ($q=3$) preserves it; cubic gains nothing more. (§4.1.1, Fig. 10) **Shown**
6. With constant $d$, linear interpolation preserves second order for the elliptic proxy. (§4.1.1,
   Fig. 11) **Shown**
7. RBF interpolation with a radial donor cloud of radius $2.5h$ (20 donors) needs at least
   quadratic polynomial augmentation (the paper's $C^2$) to preserve second order for $2s=2$;
   linear augmentation is insufficient. (§4.1.1, Fig. 13) **Shown**
8. First-order hyperbolic proxy (linear advection, periodic): linear Lagrange interpolation
   preserves second order; higher order has little or no effect. (§4.1.2, Fig. 15) **Shown**
9. Advection–diffusion proxy (Péclet numbers about 3, 30, 300): high Péclet numbers behave like the
   hyperbolic case; as the Péclet number approaches 1, higher-order interpolation is needed. (§4.1.3,
   Fig. 16) **Shown**
10. Constructing the RBF interpolants costs about 5 times the Lagrange ones on the finest mesh, and
    the gap grows with refinement. (§4.1.4, Fig. 17a) **Shown** (MATLAB code, no hardware stated)
11. The cost of one quadratic-augmented RBF interpolant grows quadratically with the donor-cloud
    size (tested up to 2200 points). (§4.1.4, Fig. 17b) **Shown**
12. On structured non-Cartesian meshes Lagrange interpolation needs a nonlinear solve for the
    receptor's parameter coordinates, so the RBF/Lagrange cost gap "will be much lower". (§3.1.1,
    §4.1.4) **Stated**
13. Interpolation constraint rows in a single system introduce noise in algebraic-multigrid
    coarsening; additive Schwarz avoids them. (§3.2) **Stated**
14. Additive Schwarz on the elliptic proxy needs a tolerance of $10^{-5}$ on the change between
    iterations to match the single-system error; the iteration counts at that tolerance are 19, 47,
    90, 153 for $h=0.2,0.1,0.05,0.025$. (§4.2.1, Table 1, Fig. 18) **Shown**
15. The authors report the Schwarz iteration count growing as $O(h^{-2})$, consistent with
    overlapping-Schwarz theory for overlaps proportional to $h$. (§4.2.1, Fig. 19) **Stated** (see
    Printed slips)
16. The Schwarz iteration count was unchanged with Lagrange instead of RBF interpolation. (§4.2.1)
    **Stated** (not tabulated)
17. With GMRES and a deliberately weak ILU preconditioner, Schwarz cost falls by doing one Krylov
    iteration per GMRES solve; the single system remains cheapest in Krylov iterations. (§4.2.1,
    Figs. 21–22) **Shown**
18. Hyperbolic proxy with linear interpolation: two Schwarz iterations per Picard iteration and one
    Krylov iteration per solve match the single system and keep second order. (§4.2.2, Fig. 23)
    **Shown**
19. With explicit time stepping one Schwarz iteration may suffice for hyperbolic systems; with
    implicit BDF more may be needed, depending on stiffness. (§4.2.2) **Stated**
20. Decaying Taylor vortex, single system, linear interpolation: second order at $\mu=0.001$ (cell
    Reynolds number about 400 on the coarsest mesh), not at $\mu=0.5$ (about 1). (§4.3.1, Fig. 25)
    **Shown**
21. Because Navier–Stokes flows can develop low-Reynolds structures and the pressure equation is
    elliptic, higher-order interpolation is "strongly recommended" for design-order accuracy.
    (§4.3.1) **Stated**
22. Stationary cylinder, $Re=200$, single system, linear interpolation: $C_d$ and $St$ converge and
    agree with the literature. (§4.3.3, Fig. 29) **Shown**
23. Under Schwarz coupling, several Picard iterations are more accurate than several Schwarz
    iterations, because repeated pressure solves with an uncorrected intermediate velocity create
    global pressure errors: splitting errors dominate inter-mesh errors. (§4.3.3, Fig. 30) **Shown**
24. Two Picard iterations with one Schwarz iteration give $C_d$, $C_l$ and $St$ within 1 % of the
    single system, even on the coarsest mesh. (§4.3.3, Figs. 30–31) **Shown**
25. Rotating cylinder (surface speed 3 times the free stream, moving mesh): one vortex is shed;
    $C_l$ converges in space and time and agrees with the literature; Schwarz with a few Picard
    iterations stays within 1 % of the single system. (§4.3.4, Figs. 32–34) **Shown**
26. For advection-dominated problems, linear interpolation and Schwarz coupling with 2–4 Picard
    iterations and one Schwarz iteration differ from the single system by less than 1 %;
    higher-order interpolation is not needed for engineering quantities. (§5) **Shown** (cylinder
    cases)
27. Non-monotone interpolation can create or amplify extrema cycle after cycle and cause exponential
    instability in high-Reynolds flows when meshes overlap in high-gradient regions. (§3.1.2)
    **Stated**

# Printed slips

- **Eq. (11):** the third Lagrange factor prints the denominator $z_j-z_n$ in a product over
  $n\ne k$; by the pattern of the first two it is $z_k-z_n$.
- **Algorithms 1 and 2:** with $\mathbf r_k=\mathbf b_k-\mathbf A_k\boldsymbol\phi_k$ and
  $\mathbf A_k\Delta\boldsymbol\phi_{k+1}=\mathbf r_k$, the printed update
  $\boldsymbol\phi_{k+1}=\boldsymbol\phi_k-\Delta\boldsymbol\phi_{k+1}$ gives
  $2\boldsymbol\phi_k-\mathbf A_k^{-1}\mathbf b_k$; the update must be $+$, as Eq. (3)'s definition
  of the increment also implies *(compiler check, not in the sources)*.
- **Eq. (27):** "$\phi^{exact}=e^{-\kappa\pi^2t}\sin(\pi(x-ct))+\sin(\pi(y-ct))+A$" decays only the
  first term; the second term alone does not satisfy the advection–diffusion equation, so the
  decay factor must multiply both, $e^{-\kappa\pi^2t}[\sin(\pi(x-ct))+\sin(\pi(y-ct))]+A$, which
  the text's "$\phi\to A$" also requires *(compiler check, not in the sources)*.
- **Eq. (8):** "$\partial_t\phi+c\nabla\cdot\phi=0$" takes the divergence of a scalar; the exact
  solution (26) satisfies $\partial_t\phi+c(\partial_x\phi+\partial_y\phi)=0$.
- **After Eq. (22):** "The lower the value of $\sigma$, the sharper … the approximation"; with
  $R=e^{-\sigma r^2}$ a lower $\sigma$ gives wider, flatter bases *(compiler check, not in the
  sources)*.
- **§4.1.1:** the background mesh is printed "$(-2,2)\times(2,2)$" (Fig. 7a labels the lower-left
  corner "−2, 2"), while the near-body mesh uses corner notation
  "$(-1.13625,-1.13625)\times(0.86375,0.86375)$".
- **§4.2.1:** the text reports "a convergence rate of $O(h^{-2})$" for the Schwarz iteration count,
  but Table 1 at tolerance $10^{-5}$ gives $153/19=8.05$ over an 8-fold refinement, an exponent of
  1.00, and 0.72 at tolerance $10^{-2}$ ($6\to27$) *(compiler check, not in the sources)*.
- **Eq. (13):** the vector ends with $R_n$ while the cloud has $N_d$ nodes, and $r_{\mathbf x}$ in
  (14) depends on $i$ without an index.

# Notation map

| Sharma et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| mesh $m$, $M$ meshes | $G_k$, $n_g$ | |
| field, fringe, hole points | $\mathcal D_k$, $\mathcal R_k$, $\mathcal H_k$ | no iblank values; orphans not discussed |
| donor points | $\mathcal S_{\mathbf i}$ | |
| fringe gap $d$ | $d$ | same meaning: distance between the fringe points of the two meshes |
| $h$ | $h$ | |
| $\psi_i(\mathbf x)$ | $\alpha_{\mathbf j}$ | fringe interpolation weights |
| $O(\psi)$ | $q-1$ | polynomial degree: **"linear" $O(\psi)=1$ is $q=2$ (second order)** |
| $O(PDE)$ | $2s$ | 1 hyperbolic, 2 elliptic |
| $N_d$ | $q$ (Lagrange, per direction); cloud size (RBF) | page-local double use |
| $C^p$ | polynomial augmentation of degree $m_{\mathrm p}$ (page-local) | **the paper's "continuity"; not the discretization order $p$** |
| $\sigma$ | Gaussian shape parameter $\epsilon_{\mathrm g}$ (page-local) | **the registry $\sigma$ is the observed convergence rate**; $\boldsymbol\sigma$ is also the stress |
| $\boldsymbol\alpha$, $\boldsymbol\beta$, $R_i$, $P_j$ | RBF and polynomial coefficients $\mathbf a$, $\mathbf b$; basis functions $g_l$, $P_j$ (page-local) | **not the weights $\alpha_{\mathbf j}$** |
| $\alpha$ (§4.3.4) | rotation rate (surface speed / $U_\infty$) | **the registry $\alpha$ is the angle of attack** |
| $\tau=\Delta t/\gamma$, $\gamma$ | $\Delta t/\gamma_{\mathrm b}$, $\gamma_{\mathrm b}$ (page-local): projection factor, BDF2 coefficient | **$\gamma$ is not the ratio of specific heats** |
| $\mathbf u$, $p$, $\rho$, $\mu$ | $\mathbf u$, $p$, $\rho$, $\mu$ | |
| OSS | single system, interpolation as constraint rows | solver-level coupling; the stencils are explicit (field donors only) |
| OS, OAS, $OC$ | overset (additive) Schwarz; Schwarz iteration count $n_{\mathrm{oc}}$ (page-local) | Jacobi-type fringe update between per-mesh solves |
| $K$, $k$ | Picard iterations, index | |
| $L_2$ (Eq. 23) | $\lVert e\rVert_2$ (RMS over all nodes) | |
| MMS | twilight-zone flow | |

# Reference list

92 printed references, numbered [1]–[92]. All 92 are merged complete into the
[bibliography](/bibliography.md) with `citedby` sharma-2021; no DOI is printed. Chesshire and
Henshaw (ref. [14]) is `chesshire-1990`. Rai's two 1986 papers are `rai-1986` (ref. [13], J. Comput.
Phys.) and `rai-1986-c` (ref. [29], Comput. Fluids), the `-b` suffix being taken by another Rai 1986
paper in the bibliography. TIOGA's papers are refs. [53] (`roget-2014`) and [62] (`brazell-2016`).
Ref. [6] prints "G. Vijaykumar" and "Z. Fredrik", kept as printed. AIAA paper numbers are entered
as page fields.

# Pages created or updated

Chunk 2 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Taylor–Green vortex (two-dimensional exact decaying solution)](/benchmarks/taylor-green-vortex.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Donor search](/methods/donor-search.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
- [Twilight-zone flow (manufactured solutions)](/methods/twilight-zone-flow.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)
