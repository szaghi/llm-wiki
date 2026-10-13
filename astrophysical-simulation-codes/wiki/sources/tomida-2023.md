---
type: Source
title: "Tomida & Stone (2023) — The Athena++ Adaptive Mesh Refinement Framework: Multigrid Solvers for Self-Gravity"
description: "Describes the geometric multigrid Poisson solver of Athena++: cell-centred 7-point Laplacian, red-black Gauss-Seidel with over-relaxation 1.15, V(1,1) cycles and full multigrid, and on AMR a full-approximation-scheme V-cycle over the whole hierarchy with a conservative fine-coarse ghost formula that needs no flux correction; second order, about 0.125 error reduction per V-cycle on uniform grids, and one FMG sweep costing about 15% of an MHD step."
resource: "doi:10.3847/1538-4365/acc2c0"
source_kind: paper
authors: [Tomida K., Stone J.M.]
year: 2023
venue: "Astrophys. J. Suppl. 266:7"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2023-ApJS-Tomida-1038471538-4365acc2c0.pdf"
tags: [software, self-gravity, multigrid, amr, performance, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper adds geometric multigrid solvers for the self-gravity Poisson
equation $\nabla^2\Phi = 4\pi G\rho$ to the octree-block AMR framework and
task-based execution of [Athena++](/software/athena-plus-plus.md). The
discretization is cell-centred and second order: a 7-point Laplacian,
volume-weighted restriction, trilinear prolongation, a higher-order
prolongation for full multigrid (FMG), and a red–black Gauss–Seidel
smoother with $\omega_{\mathrm{SOR}} = 1.15$ in V(1,1) cycles (§2.3). With
mesh refinement the full approximation scheme (FAS) is used, and the whole
hierarchy is solved in one V-cycle rather than level by level (§3.3.1).
Fine-coarse boundaries use a "mass-conservation" ghost-cell formula that
makes the area-averaged fine gradient equal the coarse gradient, so no flux
correction step is needed (§3.3.2). Merged into
[Athena++](/software/athena-plus-plus.md),
[Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md),
[conservative self-gravity](/methods/conservative-self-gravity.md) and
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Discretization** (§2.1, eqs. 1–8). 7-point stencil (eq. 3) on uniform,
   isotropic Cartesian cells, $\Phi$ and $\mathbf g$ cell-centred like the
   hydro variables. Defect equation $L_h\delta_h = d_h$ (eq. 8). Curvilinear
   coordinates are future work (§5).
2. **Smoother** (§2.2, §2.3.2, eqs. 14–16). Red–black Gauss–Seidel with
   over-relaxation, red cells ($i+j+k$ even) first. The multigrid smoother
   uses $\omega_{\mathrm{SOR}} = 1.15$, chosen to damp high frequencies, not
   the SOR-optimal value of eq. 16. Cost scalings in cells per direction
   $N_x$: Jacobi or Gauss–Seidel $O(N_x^5)$, optimal SOR $O(N_x^4)$, multigrid
   $O(N_x^3)$.
3. **Transfer operators** (§2.3.1, eqs. 17–18, Fig. 1). Restriction is the
   volume average over the $2\times2\times2$ children. Prolongation is
   trilinear, 1D weights $\tfrac14, \tfrac34, 0$ (even fine index) and
   $0, \tfrac34, \tfrac14$ (odd). The FMG prolongation, called "third-order
   tricubic", uses $\tfrac{5}{32}, \tfrac{30}{32}, -\tfrac{3}{32}$ and its
   mirror.
4. **Coarsest level** (§2.3.2, eq. 19). Solved exactly from ghost values if
   it is one cell; otherwise smoothed as many times as its largest cell
   count per direction.
5. **Cycles** (§2.3.3–2.3.4, Algorithms 1–2). Only the V-cycle, V(M,N) with
   $M, N \in \{0,1,2\}$, typically V(1,1). FMG (Brandt 1977) restricts the
   source to all levels, solves the coarsest and alternates FMG prolongation
   and one V-cycle per level upward; it needs no initial guess, and one
   sweep costs about two V-cycles (§4.1.1).
6. **FAS on AMR** (§2.3.5, Algorithm 3). The defect-correction scheme is
   ill-defined across AMR levels because defects at different resolutions
   cannot be combined; FAS restricts the potential as well and solves the
   full equation on every level. Always used with mesh refinement;
   equivalent to the correction scheme for linear problems on uniform grids.
7. **Boundary conditions** (§2.3.6, App. A). Periodic, zero-gradient,
   zero-fixed, user-defined, and isolated via a multipole expansion up to
   hexadecapoles about the centre of mass. With FAS the physical boundary
   values are applied on every level, on the domain surface rather than at
   ghost centres. With all-periodic or all-zero-gradient boundaries the mean
   source is subtracted and the mean potential fixed at zero.
8. **Stopping** (§2.3.7, eqs. 20–21). Volume-weighted RMS defect on the
   finest level against a threshold, or a fixed iteration count. Modes "FMG"
   (recommended) and "MGI" (initial guess, then V-cycles).
9. **Data structure** (§3.2.1). The solver reuses the hydro MeshBlocks,
   which must be cubic with $2^n$ cells per side (stricter than Athena++ AMR
   itself), $n_{\mathrm g} = 1$. MeshBlock levels live in per-block objects;
   below the level where each MeshBlock is one cell, the "RootGrid" levels
   live in a separate object.
10. **Parallelization** (§3.2.5). MPI + OpenMP; ghost exchange before each
    red and each black sweep; the TaskList overlaps computation and
    communication. At the transition level the data are gathered to every
    rank with `MPI_Allgather` and every rank solves the RootGrid levels
    redundantly. The RootGrid and Octet levels are **not parallelized**
    (§3.4, §4.2.2).
11. **AMR V-cycle** (§3.3.1, Fig. 3). Octree with 2:1 level jumps (§3.1).
    All MeshBlock-level objects are restricted to one cell first; refined
    blocks then become cells of "Octet" objects ($2^3$ cells plus ghosts),
    which are smoothed and restricted down to the RootGrid; the upward pass
    mirrors this. Chosen over Trottenberg et al. (2001), which removes
    locally refined grids first, because it keeps the number of objects, and
    hence the load balance, constant down to the Octet levels.
12. **Global versus level-by-level solves** (§3.3.1, App. B, Fig. 13).
    Level-by-level solvers (ART, RAMSES, Enzo, Ramsey et al. 2018) are called
    not self-consistent, since coarse solutions miss fine-scale mass. In the
    binary test at $h = 1/64$ the root-region error is "a few
    $\times10^{-4}$" with the full AMR multigrid and about 1% with a root-only
    solve. The inference that level-by-level is less accurate "by more than
    one order of magnitude" is a stated "rough estimate": no level-by-level
    solver was implemented.
13. **Fine-coarse ghost formula** (§3.3.2, eqs. 23–27, Fig. 4a). Constraint:
    the coarse face gradient equals the area average of the four fine face
    gradients (eq. 23). Fine ghost
    $\Phi_{\mathrm{ghost}} = \tfrac13\Phi_{\mathrm{fine}} + \tfrac23\Phi_{\mathrm{coarse,interp}}$
    (eq. 26) and coarse ghost
    $\Phi_{\mathrm{ghost}} = \tfrac43\bar\Phi_{\mathrm{fine}} - \tfrac13\Phi_{\mathrm{coarse}}$
    (eq. 27), with $\bar\Phi_{\mathrm{fine}}$ the area average of the first
    fine layer. One set of independent communications, **no flux-correction
    step**; contrasted with SFUMATO (Matsumoto 2007), which uses flux
    correction. It is the "Π stencil" of Feng et al. (2018), reported to
    behave better in some cases than their "△ stencil". The red–black
    pattern cannot be kept across level boundaries.
14. **Prolongation boundary** (§3.3.2, Fig. 4b). Before prolongation,
    ghosts (including edges and corners) are filled by restriction and
    trilinear prolongation, also for the FMG prolongation; the overall order
    stays second.
15. **Coupling to hydrodynamics** (§3.2.3, eq. 22). One multigrid solve per
    substep of the integrator (VL2, RK2 or RK3). Momentum and energy sources
    follow the cell-centred scheme of Mullen et al. (2021): face
    accelerations from potential differences, averaged to cell centres, and
    an energy source from Riemann mass fluxes times face accelerations;
    curl-free. Energy is **not** conserved exactly (the Mullen et al.
    conservative energy scheme is not used), and neither momentum nor energy
    is conserved to round-off because the potential carries a residual.
16. **Time stepping** (§3.1). Athena++ uses one global time step with AMR,
    no subcycling, argued to suit non-local physics such as gravity and
    implicit radiation (§3.1, §5).
17. **Cost model** (§3.4). One V-cycle costs about $\tfrac87 N_x^3$ work
    units; the RootGrid cost grows with the cube of the MeshBlock count per
    direction, so that count should not exceed the cells per MeshBlock side
    on uniform grids.

**Tests** (§4; performance on a Cray XC50 with 2× Xeon Skylake 6148 per node,
flat MPI). Sinusoidal density on a periodic uniform grid ($h = 1/16$ to
$1/1024$): error reduction factor about 0.125 per V-cycle, full convergence
in 10–15 iterations, second order for FMG and MGI (Fig. 5); weak scaling from
2 to 200 nodes at 89.6%, 73.2%, 45.7% (one FMG sweep; $128^3$, $64^3$, $32^3$
blocks) and 92.9%, 78.8%, 56.3% (FMG plus 10 V-cycles); multigrid beats the
FFT solver at scale; one FMG sweep costs about 15% and FMG plus 10 V-cycles
about 70% of an MHD step with $64^3$ blocks (§4.1.2, Fig. 6). Binary
potential on AMR with isolated boundaries (4 levels): second order, reduction
factor about 0.2 falling to about 0.5, attributed to persistent errors at level
boundaries (§4.2.1, Figs. 7–8); strong scaling of 18,432 MeshBlocks from 36 to
2,304 processes, where multigrid is about 2–6 times slower than MHD on the same
blocks, attributed to the unparallelized RootGrid and Octet levels (§4.2.2,
Fig. 9). [Jeans wave](/benchmarks/jeans-wave.md): stable case about second
order, unstable case showing that unconverged gravity breaks symmetry (§4.3,
Figs. 10–11). Magnetized protostellar collapse as a demonstration: 9 levels,
finest cell 0.326 au, about 4,900 core-hours, gravity about 85–90% of the run
time (§4.4, Fig. 12).

# Notation map

| Tomida & Stone (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $\Phi$ | |
| $\mathbf g$, $G$, $\rho$, $h$ | $\mathbf g$, $G$, $\rho$, $h$ | |
| $l$ (multigrid level, $l = 0$ coarsest) | words | **collision:** registry $l$ is the AMR level with $l = 0$ the root; multigrid levels extend below the root; $l$ is also the multipole degree (App. A) |
| $L_h$ | words | discrete Laplacian; distinct from $\mathcal L(u)$ |
| $f_h = 4\pi G\rho$ | words | **collision** with the flux $f(u)$ |
| $d_h$ | words (defect) | **collision** with $d$, the number of dimensions |
| $\delta_h$, $\epsilon_h$ | words | discretized and true error |
| $I^{l-1}_l$, $I^l_{l-1}$, $I'^{\,l}_{l-1}$ | words | restriction, prolongation, FMG prolongation |
| $\omega$ | $\omega_{\mathrm{SOR}}$ | $\omega$ is also the Jeans-wave frequency and a rotation rate |
| $D$ | $d$ | |
| $\tau$ (pseudo-time, eq. 9) | words | **collision** with the Valencia $\tau$ |
| $2^n$, $N_G$ | $N_{\mathrm b}$, $n_{\mathrm g}$ | $n$ is also an iteration index |
| $\Gamma$ | $\gamma$ | |
| CF | words | error reduction factor per V-cycle |

# Pages created or updated

* Updated [Athena++](/software/athena-plus-plus.md),
  [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md),
  [Conservative self-gravity](/methods/conservative-self-gravity.md).
* Created [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md),
  [Jeans wave](/benchmarks/jeans-wave.md).
* Also cited on [Enzo (AMR code for cosmological and astrophysical fluid flow)](/software/enzo.md).
* Also cited on (batch 3) [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md), [AthenaK (performance-portable Kokkos version of the Athena++ AMR framework)](/software/athenak.md).
* Also cited on (batch 4) [FLASH](/software/flash.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2023-ApJS-Tomida-1038471538-4365acc2c0.pdf`.
   * **Version.** arXiv:2302.13903v1 (27 Feb 2023), 28 pages with Appendices
     A–B; the submitted preprint, not the refereed version of record (the
     arXiv API lists only v1). Code: Athena++, C++11, MPI as the only external
     dependency (§3.2), BSD licence (§5),
     `https://github.com/PrincetonUniversity/athena` (footnote 5); software
     citation Athena++ v21.0, doi:10.5281/zenodo.4455880.
   * **Identity.** doi:10.3847/1538-4365/acc2c0, checked on Crossref (title and
     authors match): Astrophys. J. Suppl. Ser. 266(1):7, online 2023-04-27,
     issue 2023-05-01.
   * **How it was read.** Text extraction, all sections; eq. 24 checked
     visually on page 14. Figures 5–9 read only through the numbers quoted in
     the text. The analytic binary potential (unnumbered) and the real
     spherical harmonics (App. A) are garbled in the text layer and not
     reproduced.
   * **Recorded as printed.** Eq. 24 divides the transverse coarse difference
     by $2h$ with $h$ the fine spacing, while the two coarse centres are $4h$
     apart, yet eq. 25 applies the fine-centre offset $\pm\tfrac h2$ as if
     the result were a gradient: a possible factor-of-2 inconsistency, not
     resolved. The FMG prolongation is called "third-order tricubic", but its
     printed 3-point weights are quadratic Lagrange weights at $\mp\tfrac14$
     (third-order accurate), not a 4-point cubic.
   * **Reference list:** 52 entries, equal to the Crossref reference count.
     "In preparation" works (Yang et al., Ono et al., Stone et al.) are not in
     the list and not merged. Stone, Mihalas & Norman (1992, ApJS 80:819) is keyed `stone-1992-b`.
