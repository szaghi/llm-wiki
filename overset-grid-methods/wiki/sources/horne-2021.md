---
type: Source
title: "Horne & Mahesh (2021) — A hardware accelerated unstructured overset method to simulate turbulent fluid flow"
description: "Ports a massively parallel unstructured overset method to GPUs: hole cutting and donor search reduced to overlap queries answered by a linear bounding volume hierarchy plus the GJK test, and an incompressible solver with a pressure-rate term that lets overset values be injected into the pressure equation."
resource: "doi:10.1016/j.jcp.2021.110574"
source_kind: paper
authors: [Horne W.J., Mahesh K.]
year: 2021
venue: "J. Comput. Phys. 444:110574"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2021_Crossref_Journal_of_Computational_Physics_Horne_A_hardware_accelerated_unstructured_overset_method_to_simula.pdf"
tags: [domain-connectivity, hole-cutting, unstructured, parallel, incompressible, moving-grid]
timestamp: 2026-11-02T11:44:00Z
---

# Summary

Horne and Mahesh move their massively parallel unstructured [overset](/definitions/overset-grid.md)
method, built for many [moving bodies](/methods/moving-overset-grid.md) in turbulent incompressible
flow, onto GPUs. The paper has two parts.

**Accelerated assembly.** In the CPU code the two most expensive [domain
connectivity](/definitions/domain-connectivity.md) steps were [hole cutting](/methods/hole-cutting.md)
and the pairing of reconstruction cells with partners, i.e. [donor search](/methods/donor-search.md).
Both reduce to one query: find every object of a group that overlaps a given object, the query
solved in ray tracing and collision detection. A linear bounding volume hierarchy is built on the
GPU from Morton codes, a radix sort and Karras's parallel construction, and traversed with a
per-thread stack. The Gilbert–Johnson–Keerthi (GJK) test then decides exact overlap of convex
polyhedra. Cutting proceeds by explicit cutting volumes, fine-detail cutting with the hierarchy and
GJK, and a flood fill; a binary mask switches cells on or off ([point
classification](/definitions/point-classification.md)), and cutting also trims the overlap
([overlap optimization](/methods/overlap-optimization.md)). Cells next to masked cells or on the
outer edges of a mesh are [receptors](/definitions/fringe-point.md). On randomly placed cuboids the
assembly runs about 15 times faster than the CPU code. See [parallel and GPU overset grid
assembly](/methods/parallel-overset-grid-assembly.md).

**Modified solver.** For [incompressible flow on overlapping
grids](/methods/incompressible-flow-on-overset-grids.md) the predictor–corrector projection of the
earlier code is replaced by a coupled scheme. A pressure-rate term $\epsilon\,dp/dt$ with
$\epsilon=\Delta t$ is added to the continuity equation, together with a pressure Laplacian. This
removes the splitting error and lets the reconstructed overset values (the earlier code's
[inter-grid interpolation](/methods/inter-grid-interpolation.md)) be injected directly into the
pressure equation, so the earlier penalty coupling is dropped. In the terms of [explicit and implicit
interpolation](/definitions/explicit-and-implicit-interpolation.md), the coupling is now inside the
implicit system. A corrected two-point flux handles skewed cells; mixed-precision iterative
refinement and asynchronous work queues complete the GPU solver.

Tests: a [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) with a rotated empty patch
(second order; kinetic energy follows the analytic decay up to $Re=10^9$); [flow past a
sphere](/benchmarks/flow-past-sphere.md) at $Re=3700$ (within 1–5 % of the DNS reference, 8 to 56
times faster than the original code); a freely falling sphere (12 to 20 times faster).

# Version read

The Elsevier typeset version of record, J. Comput. Phys. 444 (2021) 110574, 19 pages, all read; the
text extraction is complete, and pp. 7–12 and 15–17 were also read visually for the equations,
Algorithm 1, captions and the results table. Page 1 matches Crossref. Numbering below is that of
this version.

# Key claims

1. The CPU unstructured overset method of the authors' 2019 papers scaled to 492,000 cores for
   100,000 moving spheres; this paper adds on-node GPU acceleration. (§1) **Stated**
2. In the CPU timings, cutting and reconstruction-partner pairing were the two most expensive
   assembly operations; the communication-pattern step is mostly MPI with little potential, so only
   the first two move to GPUs. (§2) **Stated**
3. Cutting and partner pairing share one core operation: given an object, find all overlapping
   objects of a group. (§2) **Stated**
4. A bounding volume hierarchy over $N_{\mathrm{obj}}$ objects has exactly $2N_{\mathrm{obj}}-1$
   nodes. (§2, Fig. 4) **Stated**
5. If the cells of each partition move rigidly, the Morton ordering and the node connectivity are
   fixed after initialization; only vertices and bounding boxes are updated. (§2) **Stated**
6. Morton coordinates are normalized by the partition size, so lower floating-point precision can be
   used. (§2) **Stated**
7. GJK needs 3–5 iterations for most tests here; it is exact for convex polyhedra up to float
   precision, and most cells and faces are convex. (§1, §2) **Stated**
8. Bounding-box overlap alone is not a reliable overlap test for general unstructured cells, so GJK
   follows the hierarchy query. (§2) **Stated**
9. Overall assembly speed-up about 15 times on 4 nodes (4 V100 GPUs and one 24-core Xeon Gold 6126
   each), about 40,000 cells per processor, 100 random configurations. (§4.1, Fig. 10) **Shown**
10. The cutting and partner-pairing kernels gain $O(10)$ to $O(100)$ times, growing with cell
    loading (6,250 to 960,000 cells per core). (§4.1, Fig. 11) **Shown**
11. The comparison is not like-for-like: "a non-trivial portion of the speed-up is due to the new
    algorithms … rather than just through the use of GPUs". (§4.1) **Stated**
12. Projection schemes give pressure matrices with condition number $O(h^{-2})$; Shen's
    formulation with $\epsilon=\Delta t$ gives $O(\Delta t/h^2)$, i.e. $O(h^{-1})$ for a
    CFL-limited $\Delta t$. (§3.1, Eq. (6)) **Stated**
13. With $\epsilon=\Delta t$ the added term is $O(\Delta t)$ in the mass equation, since
    $p^{n+1}-p^n=O(\Delta t)$; it replaces the splitting error. (§3.1, Eq. (7)) **Derived**
14. The standard projection method has at best $O(\Delta t^{1/2})$ pressure accuracy on general
    meshes because of the artificial condition $\partial p/\partial n=0$; the new method takes the
    normal momentum balance as the pressure boundary condition. (§3.1, Eq. (8)) **Stated**
15. The pressure Laplacian kept in the continuity equation removes odd–even decoupling on the
    collocated grid and damps spurious compressible waves. (§3.1) **Stated**
16. The primal–dual correction of the two-point flux (Eq. (10)) recovers it exactly on unskewed
    meshes and keeps the system symmetric; a purely dual-reconstructed normal gradient would make it
    non-symmetric and possibly not positive definite. (§3.2) **Stated**
17. Because of $\epsilon\,dp/dt$, overset reconstructions can be injected directly into the pressure
    equation and the system stays solvable by plain iterative solvers; the penalty method, with its
    all-to-all stencils and weight tuning, is removed, and no penalty error enters the velocity
    divergence near overset boundaries. (§3.2) **Stated**
18. Over-decomposition into asynchronous per-GPU work queues leaves one synchronization per
    iteration, the global residual-norm reduction. (§3.3, Fig. 9) **Stated**
19. Only halo data move between CPU and GPU during a run; timing experiments found this critical.
    (§3.3) **Stated**
20. Mixed-precision iterative refinement (single-precision red–black SOR inside a double-precision
    outer loop) gives a double-precision result at mostly single-precision cost. (§3.3,
    Algorithm 1) **Stated**
21. Taylor–Green vortex with an empty patch rotated 25° about each axis, about 30 % overlap: second
    order in $\mathbf u$ and $p$, with errors "several orders of magnitude" below the earlier
    predictor–corrector code. (§4.2.1, Fig. 13) **Shown**
22. Total kinetic energy follows the analytic decay for all Reynolds numbers tested, up to
    $Re=10^9$; errors at overset boundaries stay bounded. (§4.2.1, Fig. 14) **Shown**
23. Sphere at $Re=3700$: $C_d=0.392$ (DNS 0.394), wake length $2.2D$ (DNS $2.2D$), $St=0.22$ (DNS
    0.215, experiment 0.225), a 1–5 % match; the wake spectrum shows roughly a $-5/3$ slope.
    (§4.2.2, Table, Figs. 17–18) **Shown**
24. On one node (4 V100) the speed-up over the original method is 8 to 56 times, depending on GPU
    count and loading; the algorithmic change alone gives about 2 times on CPUs. (§4.2.2, Fig. 16)
    **Shown**
25. Freely falling sphere (Galileo number 291, density ratio 7.8; 2 nodes with 2 V100 each):
    12 to 20 times faster over 100 steps despite dynamic connectivity. (§4.2.3, Fig. 20) **Shown**
26. The conclusion states a speed-up of 15 to 50 times over a pure-MPI implementation at high cell
    loadings. (§5) **Stated** (see Printed slips)

# Printed slips

- **Algorithm 1:** "$r=Ax-b$", solve "$Ae=r$", update "$x=x+e$". Then $A(x+e)=2Ax-b$, which equals
  $b$ only if $x$ was already the solution; convergence needs $r=b-Ax$ or $x=x-e$ *(compiler check,
  not in the sources)*.
- **Eq. (11):** the Taylor–Green field $u=-\cos(2\pi x)\sin(2\pi y)f$, $v=\sin(2\pi x)\cos(2\pi y)f$
  is the classical field shifted by a quarter period in $x$ and $y$, and the shift reverses the
  sign of its pressure: unit density requires $p=-0.25(\cos4\pi x+\cos4\pi y)f^2$, while the paper
  prints $+0.25$ *(compiler check, not in the sources)*.
- **§1:** "O(100) TFLOPS (10^9 FLOPS)".
- **Eq. (3):** the third line prints "$\frac{u^{n+1}-u^*}{\delta}t$"; Eq. (4), obtained by adding
  lines 1 and 3, has $\delta t$ in the denominator.
- **Eq. (10) and text:** the equation dots the gradient $\partial p_{pd}/\partial x$ with
  $n_f-n_{12}$, while the text calls it the "dual reconstructed normal gradient"; the text also
  writes $n_{1,2}$.
- "TPFA" in §1 but "TFPA" in §3.2 and the Fig. 7 caption; "convect hull" (§2).
- **§4.2.2:** "the near wake spacing is chosen to be D = 0.014D"; "to further evaluate to evaluate".
- **Fig. 16:** abscissa labels "150000, 6480000, 12000000, 2304000", not monotone.
- **Speed-up ranges:** abstract "upwards of 50 times", §4.2.2 8–56 times, §4.2.3 12–20 times, §5
  "ranging from 15x to 50x".
- **References:** the results table cites "Rodriguez et al., 2011" without a number (ref. [32]);
  ref. [32] prints "A. Olivia" and "re = 3700"; ref. [4] prints pages "3316–33333".
- Symbol overloads: $u^n$ is the face-normal velocity in Eq. (1) and time level $n$ in Eqs.
  (3)–(8); $n_f$ is the number of faces in Eq. (9) and the face normal in Eq. (10); $f$ is the
  force in Eq. (2) and the decay factor in Eq. (11).

# Notation map

| Horne & Mahesh (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overset mesh, background mesh | $G_k$ (unstructured) | one or more partitions per mesh |
| mask, "cutting" | $\iota_k$ (on/off only) | cut cells $\mathcal H_k$ |
| reconstruction cell | $\mathcal R_k$ | cells next to cut regions and on mesh outer edges |
| reconstruction partner | donor cell, $\mathcal S_{\mathbf i}$ | supercell interpolant of the earlier paper |
| $u_i$, $p$, $\rho$, $\nu$ | $u_m$, $p$, $\rho$, $\nu$ | |
| $u^n$, $u^n_{mesh}$ (Eq. 1) | $\mathbf u\cdot\mathbf n_f$, $\mathbf u_g\cdot\mathbf n_f$ | **superscript $n$ means "normal", not the time level** |
| $\delta t$, $\delta x$ | $\Delta t$, $h$ | |
| $\epsilon$ | coefficient of $dp/dt$ | page-local; $\epsilon=\Delta t$ |
| $\triangle$ | $\nabla^2$ | |
| $C$, $V$ | discrete convective, viscous terms | **$V$ is not a cell volume** |
| $A_f$, $d_f$ | $S_f$, centroid distance across face $f$ | |
| $n_f$ | number of faces (Eq. 9), face normal $\mathbf n_f$ (Eq. 10) | **the registry $n_f$ is the number of fringe layers** |
| $n_{12}$ | unit vector between centroids | |
| $N_{obj}$, $N_{cell}$, $N_{gpu}$ | objects, cells per partition, GPUs per node | page-local |
| $f=e^{-8\pi^2\nu t}$ | decay factor | **not the body force $\mathbf f$** |
| $D$, $C_d$, $C_p$, $L_w$, $St$, $Ga$, $m^*$ | sphere diameter, drag and pressure coefficients, wake length, Strouhal, Galileo numbers, density ratio | |
| TPFA, BVH, LBVH, AABB, OOB, GJK | two-point flux approximation, (linear) bounding volume hierarchy, axis-aligned and object-oriented boxes, Gilbert–Johnson–Keerthi test | |

# Reference list

37 printed references, numbered [1]–[37]. All 37 are merged complete into the
[bibliography](/bibliography.md) with `citedby` horne-2021; no DOI is printed. The authors' two
2019 papers, refs. [1] (mesh connectivity) and [2] (moving bodies), are `horne-2019` and
`horne-2019-b`. Oddities kept as printed: ref. [9] venue "Comput. Fluid Dyn. J. 374 (2018)"
without pages; ref. [18] without volume; ref. [24] without pages; ref. [25] printed in proceedings
style.

# Pages created or updated

Chunk 2 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Flow past a sphere](/benchmarks/flow-past-sphere.md)
- [Taylor–Green vortex (two-dimensional exact decaying solution)](/benchmarks/taylor-green-vortex.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Donor search](/methods/donor-search.md)
- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)
- [Twilight-zone flow (manufactured solutions)](/methods/twilight-zone-flow.md)
