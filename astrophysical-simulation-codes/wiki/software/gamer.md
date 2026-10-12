---
type: Software
title: "GAMER (GPU-accelerated octree AMR code), MHD extension"
description: "GPU-accelerated octree patch-based AMR code whose MHD extension runs Athena's CTU+CT and VL+CT unsplit schemes on the GPU per group of eight patches, keeps the divergence-free constraint across levels with Balsara prolongation and EMF correction, and overlaps GPU work with CPU-side AMR operations under hybrid MPI/OpenMP/GPU parallelism."
status: established
aliases: [GAMER, GAMER-MHD]
tags: [software, mhd, amr, gpu, constrained-transport, unsplit, riemann-solver, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# GAMER

GAMER is a GPU-accelerated AMR hydrodynamics code on an octree of patches
(Schive et al. 2010, 2012, 2017). [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md)
extend it to ideal MHD ("GAMER-MHD").

## Code

* Repository `https://github.com/gamer-project/gamer` (Software statement).
  Version, licence and language are not printed; the paper speaks of "CUDA
  thread block" and "CUDA stream", and uses OpenMP and MPI (§4).

## Equations

Ideal MHD only, conservative form, magnetic permeability 1 (§2, eqs. 1–9):

$$\begin{aligned}
&\partial_t\rho + \nabla\cdot(\rho\mathbf v) = 0,\qquad
\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v - \mathbf B\mathbf B + P^*\mathsf I) = 0,\\
&\partial_t E + \nabla\cdot\left[(E+P^*)\mathbf v - \mathbf B(\mathbf B\cdot\mathbf v)\right] = 0,\qquad
\partial_t\mathbf B + \nabla\times\boldsymbol{\mathcal E} = 0,
\end{aligned}$$

with $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$ and
$E = \frac{p}{\gamma-1} + \frac12\rho|\mathbf v|^2 + \frac12|\mathbf B|^2$.
Ideal-gas EOS only; no gravity, radiation, resistivity or relativity is used
or discussed in the MHD paper. Cartesian grids only, with cubic cells on each
level (§3.1).

## Solvers

From [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §3.1–§3.2.
* **Discretization**: finite volume with cell-averaged $u$, face-area-averaged
  $\mathbf B$ and time- and line-averaged edge EMFs; the CT update preserves
  the discrete divergence exactly (eqs. 10–16). The ghost-zone width is one
  cell larger than for pure hydro because of the staggered field. See
  [constrained transport](/methods/constrained-transport.md).
* **Edge EMF**: evaluated from the interface EMFs, the interface field and the
  cell-centre velocity, as in Athena; the averaging variant is not named, and
  Gardiner & Stone (2005, 2008) are not cited.
* **Reconstruction**: PLM and PPM; primitive or characteristic variables are
  not stated.
* **Riemann solvers**: HLLE, HLLD, Roe. See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **Integrators** (see [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md)):
  CTU+CT (Colella 1990 as extended in [Athena](/software/athena.md)), 8 steps,
  and VL+CT (MUSCL-Hancock), 7 steps; both second order in space and time.
  CTU "is generally less diffusive than the VL scheme due to the transverse
  flux gradient correction" and is used for all accuracy tests.
* Courant factor 1/2 and $\gamma=5/3$ in all tests (§5).

## Adaptive mesh refinement

From [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §3.3; see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* Octree of patches of $N_{\mathrm b}^3$ cells (FLASH-like), $r_{\mathrm{ref}}=2$;
  the figures use $N_{\mathrm b}=8$. Nesting or 2:1 rules are not stated.
* **Restriction**: covered coarse cells get volume averages of the conserved
  variables and area averages of the face field.
* **Refluxing and EMF correction**: at a leaf coarse cell next to a
  coarse–fine interface, the flux difference corrects the conserved variables,
  and EMF differences on coarse–fine edges correct the coarse face field,
  needed for conservation and $\nabla\cdot\mathbf B=0$.
* **Prolongation**: conservative interpolation of conserved variables (order
  not stated); Balsara (2001) divergence-free reconstruction of the face field.
  In 2D, fine faces on coarse faces are filled by piecewise-linear
  interpolation preserving the coarse face average, and interior fine faces
  from a quadratic-in-space field whose ten coefficients are fixed by seven
  independent face-matching conditions and three conditions of zero divergence
  (Fig. 2, eq. 17).
* **Time stepping**: update level $l$, evolve level $l+1$ until synchronized,
  correct level $l$, then (de)refine level $l+1$; adaptive (subcycled) steps,
  details deferred to Schive et al. (2017).

## GPU design and parallelism

From [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §4 (Fig. 3):
* **Patch groups**: 8 neighbouring patches form a group of
  $(2N_{\mathrm b})^3$ cells, computed by one CUDA thread block; grouping
  reduces ghost-zone overhead.
* **Memory**: all data live in host memory; only "a small number of patch
  groups (typically a few hundreds)" are sent to the GPU at a time; ghost zones
  are allocated only temporarily for the groups being updated.
* **Overlap**: CUDA streams overlap kernels with host–device transfers; CPU
  "preparation" (gather a group and its ghosts from the octree, interpolating
  ghosts if needed) and "closing" (scatter results back) run concurrently with
  the GPU, parallelized with OpenMP. AMR correction and refinement stay on the
  CPU because they are much cheaper than the solver. An earlier GAMER result
  reports CPU/GPU concurrency often above 90% (§1).
* **Distributed memory**: MPI with a Hilbert-curve decomposition computed
  independently per level, for level-by-level load balance.

## Performance

From [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §5.2:
* **Single GPU** (Tesla P100, uniform grid, VL + PLM + Roe): saturates beyond
  about $2\times10^6$ cells at about $1.2\times10^8$ cell updates per second in
  single and $5.5\times10^7$ in double precision (Fig. 18).
* **CPU comparison** (Intel Xeon E5-2680, 14 cores, double precision, same
  scheme): GAMER-CPU about $5.0\times10^6$ cell updates per second;
  [Athena++](/software/athena-plus-plus.md) $7.7\times10^6$, 1.5× faster,
  "likely due to the more optimized implementation of vectorization".
* **Strong scaling** on Blue Waters XK nodes (one 16-core Opteron + one Tesla
  K20X each; CTU + PPM + Roe, single precision, AMR, hybrid MPI/OpenMP/GPU):
  $1.5\times10^{10}$ cell updates per second at 2048 nodes; 70% parallel
  efficiency and 57% "doubling efficiency" (the time ratio when halving the
  node count, minus 1) at $10^3$ nodes. At 2048 nodes the MPI time is only
  about 5× and refinement about 6× smaller than at 64 nodes, against an ideal
  32×, the main cause of the efficiency drop (Figs. 19–20).
* **Weak scaling** (replicated problem, 1 to 4096 nodes): $5\times10^{10}$ cell
  updates per second at 4096 nodes, AMR about equal to uniform-grid
  performance; 70% efficiency at $10^3$ nodes updating $2\times10^{11}$ cells
  (text), 85% at 512 nodes (Fig. 22 caption). The MPI time fraction grows for
  512 nodes and more, attributed plausibly to the network topology; the
  proposed fix is to overlap MPI with CPU/GPU work (§6).

## Verification

From [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §5.1:
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md): slow,
  Alfvén and fast waves along the 3D box diagonal, PLM + Roe, double
  precision; all errors second order (Fig. 4).
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): $256^2$ base plus 3
  levels against a $1024^2$ uniform reference; AMR/uniform ratios of magnetic
  and gas pressure about 1 except at shocks and reconnection layers (Figs.
  9–10).
* [MHD blast wave](/benchmarks/mhd-blast-wave.md) in 3D, uniform $512^3$
  against AMR $256^3$ plus 3 levels: fast shocks in 1–2 cells, contacts in 4–5;
  a "finger" structure at the slow-shock nose, confirmed physical by rotated
  runs (Figs. 11–14).
* Also: Ryu–Jones 2a (discontinuities in 2–4 cells), the Torrilhon problem
  (the spurious compound wave vanishes with resolution, L1 error proportional
  to the cell count to the power $-3/4$ up to $2^{18}$ cells), and a new ABC
  force-free field relaxation test, which conserves total energy to machine
  precision and also serves as the scaling benchmark.

## Later uses (batch 3)

GAMER keeps all data in host memory and streams patch groups to the GPU.
The seven batch-3 codes below state their data placement, and all do the
opposite: the solution stays resident on the device (see
[porting compressible-flow codes to GPUs](/methods/gpu-porting.md)). These are
contrasting designs of different codes, not contradictions.

* **[Cholla](/software/cholla.md)** used the host-resident design first: its
  older versions ran "an extreme version of the 'offload' model", copying
  the conserved arrays between CPU and GPU every step. The current version
  keeps all data on the GPU, sends MPI messages directly from GPU buffers,
  and leaves only initial conditions and file I/O on the CPU; the change is
  credited with a "considerable speedup", not timed
  ([Caddy et al. (2024)](/sources/caddy-2024.md), §2.3.1, §5).
* **[IDEFIX](/software/idefix.md)** keeps all arrays and loops on the device,
  the host serving I/O ([Lesur et al. (2023)](/sources/lesur-2023.md), §3.1, §6).
* **[AthenaK](/software/athenak.md)** keeps all field data on the device,
  moved to the host only for output, and runs prolongation and restriction
  on the device; only the block tree stays on the host
  ([Stone et al. (2026)](/sources/stone-2026.md), §2).
* **[gPLUTO](/software/gpluto.md)**: "The entire computational workload is
  handled by the GPUs", with no host–device transfers during computation,
  using CUDA Unified Memory plus explicit data directives
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §3.1, §3.3).
* **[GRaM-X](/software/gram-x.md)**: "all data are stored on the
  accelerator's built-in memory at all times", moved to the host only for
  I/O, with the AMR operations of its driver GPU-enabled
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §III, §III C).
* **[ADAM](/software/adam.md)** is the closest design: like GAMER it keeps the
  octree and the refinement on the CPU, but its field stays on the GPU for
  the whole compute phase and is copied to the host only at I/O and AMR
  updates. Its serial AMR update grows from 0.74 s at 1562 blocks to
  527.97 s at 684,258 blocks ([Zaghi et al. (2023)](/sources/zaghi-2023.md),
  §2.2, §3.2, Table 1), whereas GAMER overlaps its CPU-side AMR work with
  the GPU solver.
* **[STREAmS](/software/streams.md)** (no AMR) copies its solution to the
  device once before time marching and back at the end
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.1). It
  implements the remedy GAMER proposes for its growing MPI share, overlap
  of communication with computation (interior fluxes during the ghost
  exchange), and reports about 97% weak-scaling efficiency on 1024 V100
  GPUs (§4.3, Fig. 13). GRaM-X, without such overlap, also blames
  ghost-zone communication for its 40–50% weak-scaling efficiency at 2304
  nodes, measured against one node of 6 GPUs
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §V B). The three
  efficiencies are not on a common baseline (see
  [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md)).

GAMER's single-P100 throughput (above) cannot be set against the batch-3
figures as a speed-up: the GPU generations (P100 against V100, A100, H100),
the schemes, the precision (GAMER prints it; Cholla and Quokka do not) and
the normalization (per GPU against per node of 4 GPUs for gPLUTO) all differ
([Caddy et al. (2024)](/sources/caddy-2024.md), §3.2;
[Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4;
[Rossazza et al. (2026)](/sources/rossazza-2026.md), §4; see
[cell-update throughput](/definitions/cell-updates-per-second.md)).

# Citations

1. [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §§1–6 (arXiv v4).
2. [Caddy et al. (2024)](/sources/caddy-2024.md), §§2.3.1, 3.2, 5.
3. [Lesur et al. (2023)](/sources/lesur-2023.md), §§3.1, 6.
4. [Stone et al. (2026)](/sources/stone-2026.md), §2 (arXiv v1).
5. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §§3.1, 3.3, 4.
6. [Shankar et al. (2023)](/sources/shankar-2023.md), §§III, V B (arXiv v2).
7. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §§2.2, 3.2, Table 1.
8. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §§4.1, 4.3, Fig. 13.
9. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.
