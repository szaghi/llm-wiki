---
type: Method
title: "Block-structured adaptive mesh refinement"
description: "Hierarchical h-refinement of Cartesian or mapped meshes in nested levels of patches or fixed-size blocks: Berger–Oliger/Colella patch refinement in AMROC, tree-based block refinement on GPUs, in PARAMESH and in ForestClaw, the refinement criteria, coarse–fine transfer including Active Flux point values and divergence-preserving prolongation, sub-cycling with and without time interpolation, and the measured savings and accuracy against uniform meshes."
status: established
aliases: [AMR, SAMR, block-structured AMR, structured adaptive mesh refinement, patch-based AMR, tree-based AMR, quadtree AMR, octree AMR]
tags: [amr, finite-volume, finite-difference, software, gpu, mhd]
timestamp: 2026-10-23T23:50:00Z
---

# Block-structured adaptive mesh refinement

Block-structured adaptive mesh refinement covers the regions that need
resolution with a hierarchy of finer and finer logically rectangular
grids, each level refining the one below by an integer factor (2 in
every source of the bundle), while the rest of the domain stays coarse.
The integrator works on each block as on a uniform grid; the adaptation
supplies ghost data at coarse–fine boundaries, transfers data when the
hierarchy changes, and keeps the coarse and fine fluxes consistent. It
is h-refinement, in contrast with the r-adaptation of an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) and with the
degree adaptation of [hp-adaptation](/methods/hp-adaptation.md). The
sources build on the patch algorithm of Berger & Oliger and Berger &
Colella, as recalled by [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md)
§2.5, [Bai & Li (2022)](/sources/bai-2022.md) §2.2 and
[Matsushita & Aoki (2021)](/sources/matsushita-2021.md) §3.5.

## Two organizations of the hierarchy

**Patches clustered from flagged cells.** In
[AMROC](/software/amroc.md), as Peng et al. describe it, cells are
flagged on each level, the flags are clustered into rectangular patches
of the next level (clustering-efficiency threshold 0.7, buffer of two
cells), and the levels form a nested hierarchy; the solver is
independent of the adaptation, and the hierarchy is rebuilt at every
time step of the next coarser level (§2.5).

**Trees of fixed-size blocks.** Matsushita & Aoki use a quadtree or
octree whose leaves are uniform blocks of $4^2$ or $4^3$ cells, one CUDA
thread block per leaf and one thread per cell, with 2:1 balance between
neighbours, Morton ordering of the leaves, a pre-allocated GPU memory
pool defragmented on the CPU, and a Morton-curve domain decomposition
for several GPUs, rebuilt at every remeshing (§3.5, §4).
[Browne et al. (2022)](/sources/browne-2022.md) §3 use a customized
PARAMESH (blocks of $40\times40$ cells in 2D and $50\times14\times12$ in
3D, up to nine levels). Bai & Li describe their mesh as a quadtree-like
multi-level Cartesian mesh (§2.2).
[Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) implement
[Active Flux](/methods/active-flux.md) in [ForestClaw](/software/forestclaw.md), a quadtree (or
multi-block forest) of quadrants managed by p4est, each quadrant holding a
Cartesian patch with the same number of cells on every level
($16\times16$ in all their tests), with 2:1 balance between adjacent
quadrants and coarsening only when all four siblings satisfy the
criterion (§3). [Paula, Adami & Adams (2023)](/sources/paula-2023.md)
run their multiphase [discrete-equations method](/methods/discrete-equations-method.md)
in ALPACA, whose block-based multiresolution adapts the mesh by Harten's
wavelet analysis of the cell averages and keeps shocks and interfaces on
the finest level; their "effective resolution" is that finest level
(§2.2).
[Zaghi et al. (2023)](/sources/zaghi-2023.md) build the same kind of
octree in [ADAM](/software/adam.md): identical blocks of $8^3$ to $32^3$
cells with 26 ghost regions each, 2:1 balance, the tree stored in a hash
map keyed by a 64-bit integer that linearizes level and block
coordinates, and Morton-curve load balancing across MPI processes
(§2.2). Matsushita & Aoki and Zaghi et al. agree on the split of labour:
the field lives and is advanced on the GPU, the tree is managed serially
on the CPU. In ADAM the GPU field array is transposed so that the block
index is contiguous, for coalesced access, and is copied to the CPU only
at input/output and AMR updates, refinement and coarsening themselves
being done on the CPU (§2.2, Fig. 3).

**Unstructured simplices in space–time shock tracking.** Outside the
block-structured family, [Naudet & Zahr (2024)](/sources/naudet-2024.md)
(§3.3, §4.5) refine the curved simplex meshes of their slab-based
space–time [implicit shock tracking](/methods/implicit-shock-tracking.md)
element by element. A refined element is split in its straight-sided
parent and mapped through its isoparametric map and the domain map, which
keeps the refined mesh conforming and curved (Eqs. (31)–(34)). Simplices
are refined by splitting an edge at its midpoint, together with every
simplex that shares the edge, or in 2D by uniform 1→4 refinement with
neighbours refined or edge-split (§3.3.2, Fig. 6); space–time prisms
extruded from the spatial mesh are cut into $N_d=dN_{d-1}+2$ simplices,
$N_2=4$, $N_3=14$, $N_4=58$, by splitting every face and connecting it to
a central node (Eq. (35); page-local $N_d$, $d$ the space–time dimension).
Simplices are kept because element removal by edge collapse, which the
tracking needs, is defined in any dimension (§3). Refinement interrupts the
tracking optimization at an iteration whose residual is below a user
threshold, while the element count stays below a user limit (§4.5).

## Refinement criteria

- **Scaled gradients.** Peng et al. flag a cell when an undivided
  difference of a chosen scalar $w$ (page-local) in any of four
  directions, axes and diagonals, exceeds a threshold $\epsilon_w$
  (Eq. 21), with thresholds on $T$, $\rho$ and $p$. Bai & Li refine by
  pressure-gradient magnitude, or by distance from the interface.
- **Richardson error estimation.** Peng et al. compare one step of
  $2\Delta t$ with two steps of $\Delta t$ of an order-$o$ method
  (page-local): their difference is $(2^{o+1}-2)\,\mathcal C\Delta t^{o+1}$
  to leading order (Eqs. 22–25), so
  $\tau^w\approx\lvert w(\bar Q)-w(Q)\rvert/(2^{o+1}-2)$ estimates the
  local truncation error, computed on a twice coarser grid by
  restriction; a cell is flagged when $\tau^w/\max(\lvert w\rvert,S_w)$
  exceeds a threshold, and then all four fine cells under it (Eqs. 26–27;
  page-local symbols). They apply it to species mass fractions, with a
  scale of 1 % of the maximal Chapman–Jouguet mass fraction.
- **Gradients with hysteresis.** Zaghi et al. mark blocks (not cells)
  by the density-gradient modulus in shock problems and by the enthalpy
  gradient in a vortex test, with a split threshold above the
  recomposition threshold to avoid flip-flop; eight siblings recompose
  only if all exist and all are marked (§2.2).
- **Interface distance.** Matsushita & Aoki refine a leaf when the
  smallest level-set value in it is below $\sqrt3$ times the block length
  of its children, $\min\lvert\Phi\rvert<\sqrt3\,dh_{n+1}b$ (Eq. 47;
  page-local), so the finest leaves follow the interface
  ([level-set methods](/methods/level-set-method.md)).
- **Disturbance indicators.** Browne et al. track a wavepacket with a
  composite of normalized disturbance vorticity, pressure, pressure
  gradient and, away from the wall, temperature,
  $\varphi=\max_k\big(\lvert\tilde{\mathsf d}_k\rvert/\max\lvert\tilde{\mathsf d}_k\rvert\big)$,
  with $\tilde{\mathsf d}_k$ the tracked disturbance quantities and the
  inner maximum over the disturbance mesh (page-local; the source's
  $\tilde\phi$), coarsening a block where $\varphi$ falls below a lower
  threshold and refining where it exceeds an upper one, both scaled by
  $2^{L_{\max}-n}$ on level $n$ (Eqs. 66–68). The pressure gradient,
  90° out of phase with the pressure, fills holes in the mesh between
  pressure peaks (Figs. 8–10).

- **Solution variation.** Calhoun et al. refine a patch where
  $q_{\max}-q_{\min}>0.001$ (advection) or
  $\lvert p_{\max}-p_{\min}\rvert\ge0.001$ (acoustics), and where a
  centred difference quotient of $q$ is at least 15 (two-dimensional
  Burgers, where the same cells are also limited); in convergence tests
  they force the refinement along a diagonal band instead (§4).
- **Residual and modal sensor (space–time DG).** Naudet & Zahr refine
  every element whose enriched DG residual (test degree one above the
  trial degree) is at least $c_1$ times the largest one, or whose
  Persson–Peraire sensor on the first conserved variable is at least $c_2$
  times the largest one, $c_1=c_2=0.01$ by default (§4.5, Eqs. (43)–(45);
  page-local $c_1$, $c_2$;
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md)). On
  Burgers shock formation and merging, eight rounds turn 96 quadratic
  triangles into 207 and resolve the formation point (§5.1.2,
  Figs. 12–13); on the [Shu–Osher problem](/benchmarks/shu-osher-problem.md),
  run to $T=2$, refinement and the removal of the known upstream region
  resolve the shock formation and post-shock oscillations, with a relative
  $L^2$ error of $3.97\times10^{-4}$ against a refined finite-volume
  reference (§5.3.2, Figs. 19–21).

**When to remesh.** Matsushita & Aoki remesh when the interface has
moved $2\Delta x_{\min}$, estimated from the acoustic time step
(Eq. 42); Browne et al. every $n_{\mathrm R}=\Delta t_{x,b}/\Delta t$
steps, with $\Delta t_{x,b}=\Delta x\,n_{x,b}/(u+c)$ the time the
fastest wave needs to cross a block of $n_{x,b}$ cells (Eqs. 64–65).
On their three-dimensional flat plate this meant 520
refinement steps in about 130,000 time steps (§5).

## Coarse–fine transfer

- **Restriction.** On a Cartesian mesh the coarse value is the mean of
  its $n^2$ fine values; on a mapped mesh Peng et al. take the
  area-weighted mean $Q_c=\sum_kA_{f,k}Q_{f,k}/A_c$ (Eqs. 28–29),
  conservative even when the mapped fine cells do not tile the coarse
  one exactly, at the price of accuracy when their areas do not sum to
  $A_c$.
- **Prolongation.** Peng et al. interpolate bilinearly from the four
  nearest coarse cells, with weights obtained on a mapped mesh by
  solving the bilinear map of the coarse cell centres for the fine
  centre by Newton's method, gradient descent as fallback (Eqs. 30–31;
  0.75 and 0.75 on a Cartesian mesh with factor 2). Matsushita & Aoki
  prolong with a central-difference coarse gradient,
  $f^{\mathrm f}=f^{\mathrm c}+(r^{\mathrm f}-r^{\mathrm c})\cdot\nabla f^{\mathrm c}$
  (Eq. 48), and fill ghost cells at level gaps by copying for
  cell-centred and by interpolation for staggered variables; linear
  interpolation reproduces the uniform-mesh rising-bubble position
  better than copying (Fig. 22). Bai & Li synchronize levels by $L^2$
  projections of the DG polynomials, a transfer they call conservative
(§2.2).
  Zaghi et al. fill ghost cells between blocks of different levels by
  second-order interpolation (§2.2); refinement and coarsening of the
  field are interpolations whose order is not stated.
- **Point values and averages (Active Flux).** The degrees of freedom of
  Active Flux are a cell average plus point values at corners and edge
  midpoints, shared between cells, and each cell carries the biquadratic
  reconstruction that interpolates its eight boundary values and matches
  its average. Calhoun et al. coarsen by averaging the four fine averages
  and copying the coarse point values from the fine vertices, discarding
  fine values that are not at coarse locations; they refine by evaluating
  the coarse reconstruction at the fine point locations and computing the
  fine averages by the two-dimensional Simpson rule, which is exact for
  the biquadratic, so the four fine averages sum exactly to the coarse
  one and the transfer is conservative (§3.1, Figs. 3–4).
- **Flux consistency.** Matsushita & Aoki average fine fluxes on coarse
  faces at level gaps, which keeps the phase field conserved (§4); their
  mass error stays at $10^{-16}$ on uniform and adaptive grids (§5.1).
  Calhoun et al. use the Berger–Colella conservative fix, updating both
  coarse and fine cells at a coarse–fine face with the fluxes of the
  finer grid (§3.2).
- **Constrained vector fields.** For face-collocated fields with an
  involution constraint, $\nabla\cdot B=0$ or $\nabla\cdot D=\rho_{\mathrm q}$
  (page-local $D$, the electric displacement, and $\rho_{\mathrm q}$, the
  charge density), prolongation must also satisfy the constraint on every
  new fine zone. [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md)
  keep the coarse facial data on the fine faces that overlie coarse faces,
  reconstruct only the new internal faces, and either use an analytically
  exact fourth-order divergence-preserving reconstruction or a WENO-type
  face interpolation followed by a least-squares touch-up that enforces
  the fine-zone constraint to round-off
  ([divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md)).
  The charge density, an unconstrained zone-averaged variable, is
  prolonged by finite-volume WENO at design orders 2–5 (Table 12).

## Time sub-cycling and edge-field defect correction

Balsara et al. (2023) §7 describe a two-level step for a Faraday-type
update with refinement ratio 2, proper nesting and time sub-cycling,
adapted from Balsara (2001). The coarse mesh steps from $t^n$ to
$t^{n+1}$ with an ADER predictor; the fine mesh takes two steps of
$\Delta t/2$, its ghost zones prolonged from the coarse solution at
$t^n$ and from the stored coarse space–time predictor at $t^{n+1/2}$.
The predictor may fill ghost zones but "can never be used to
re-initialize a fine mesh", because it is only approximately
divergence-preserving. Consistency of the composite mesh requires each
coarse face to equal the mean of its four fine faces after the step
(Eq. 47), which holds only if each coarse edge electric field equals
the space–time average of the coinciding fine edge fields (Eq. 48).
**Defect correction** enforces this: the coarse edge fields at
fine–coarse interfaces are stored, the coinciding fine edge fields are
accumulated with weight $\frac14$ over the fine steps, and one coarse
update with the defects replaces them, also correcting the transverse
coarse faces (Eqs. 50–52); **restriction** then resets coarse faces that
overlie fine faces by area averaging. It is the edge-field analogue of
flux refluxing, and both steps give primacy to the fine mesh. Without
defect correction, they state, a sub-cycled composite mesh develops
late-time instabilities or a localized build-up of divergence at
fine–coarse interfaces (§7). On a 2D Maxwell pulse scattering off a
dielectric cylinder with a static refined patch they observe design
orders 2, 3 and 4 on the finest mesh pair, an undivided divergence of
$10^{-14}$–$10^{-12}$, and no late-time instability, error pile-up or
mesh imprinting over many thousands of steps (§9, Tables 13–15,
Figs. 13–15).

**Sub-cycling without time interpolation.** Calhoun et al. (§3.2,
Figs. 5–6) advance level $\ell+1$ with $\Delta t_{\ell+1}=\Delta t_\ell/2$
but, unlike Berger–Oliger–Colella, never interpolate coarse ghost data in
time: two ghost layers are reconstructed around each patch, the first
layer is advanced together with the interior and used at intermediate
times, and at synchronized times the ghost data are replaced by averaged
or interpolated data from the neighbours. For their constant-state
preserving Active Flux on a swirling flow, global time stepping keeps
constants exactly on adaptive grids, because a coarse flux equals the mean
of its two fine fluxes (Corollary 4.3); with sub-cycling the
intermediate-time fine fluxes are not balanced by coarse ones, and a
constant field shows an error of $10^{-13}$ against about $10^{-16}$
without sub-cycling (§4.3; [free-stream preservation](/properties/free-stream-preservation.md)).
On smooth swirl data sub-cycling does not change the accuracy noticeably
(Table 3). Paula et al. adapt the time step after every finest-level step
by local time stepping, which lets them use the CFL numbers of uniform
grids (§2.2).

## Measured savings

| Source | Problem | Adaptive against uniform |
|---|---|---|
| Peng et al. §4.1, Table 3 | blunt-body combustion, Mach 4.18, to 0.2 ms | 308.6 against 240.0 CPU h at 7 µm (two levels), 1193.5 against 1286.7 at 3.5 µm (three), 5521.6 against 9590.6 at 1.75 µm (four), a factor 1.74 |
| Browne et al. §5, Table 6 | hypersonic flat-plate wavepacket | about 55 million against 91.7 million points (linear), 66 million against 715 million (strongly nonlinear): 60 % and 9 % |
| Zaghi et al. §3.2, Table 1 | 3D shock diffraction by a sphere, finest spacing 0.015625 | 350.3 million cells in 684,258 blocks; the authors' uniform-grid figure is "8 billions", a $1280^3$ grid has $2.1\times10^9$ *(compiler check, not in the sources)* |
| Matsushita & Aoki §6.3 | liquid-jet breakup | 11 h on one GPU against an estimated 501,840 core-hours of an incompressible uniform-mesh reference, explicitly not a fair comparison |

Peng et al. find that refinement pays off only at high resolution,
because their body-fitted domain is already tight around the region of
interest (§4.1); their refinement-criterion study shows the cost
changing from 974.2 to 2424.0 CPU h as the thresholds are halved twice
(Table 4). Matsushita & Aoki measure that tree management on the CPU
takes 70 % of the adaptation time but that the adaptation is not
dominant, about 90 % of the run being GPU computation, and a weak
scaling efficiency of 81 % overall and 95 % for the fluid part on 128
V100 GPUs, the tree not yet being parallel (§4.2–4.3, Figs. 13–17).
Zaghi et al. do not report the share of the run spent in adaptation;
their AMR update is the cost that grows with the block count: halving
the finest spacing at fixed coarsest spacing multiplies the cells by
about 4–5 instead of 8 and the grind time by less than 3 overall
(ratios 2 to 32), but the serial AMR update grows from 0.74 s (1562
blocks, 1 GPU) to 527.97 s (684,258 blocks, 256 GPUs), which they call
acceptable for statistically stationary flows and problematic for
transient ones; in strong scaling on 3.6 million cells the AMR update
only falls from 4.25 s to 1.84 s between 1 and 32 GPUs (§3.2, Table 1,
Figs. 5, 7). Browne et al. compare finite-difference adaptive points with a DNS that
is Fourier-spectral in the spanwise direction, a caveat they state
(§5).

**Accuracy on refined grids.** Calhoun et al. measure third order of
Active Flux on adaptive grids, in $L^1$ (Tables 1–4). Advecting a
smoothed disc, refinement that follows the solution (levels 3–6) matches
the finest uniform grid, $1.07\times10^{-6}$ against $1.07\times10^{-6}$
(EOC 2.985 against 2.987), whereas refinement along a fixed diagonal
band (levels 5–6) matches the coarser uniform grid (Table 1). For solid-body
rotation the adaptive levels 3–7 give $5.92\times10^{-7}$ against
$5.83\times10^{-7}$ on the uniform level 7 (Table 2), and on the
acoustics test of Lukáčová et al. the adaptive grid is about as accurate
as the coarser uniform one (Table 4).

## Qualifications

- [Wang et al. (2022a)](/sources/wang-2022.md) implement their
  ghost-cell [immersed boundary](/methods/immersed-boundary-method.md)
  in AMROC but run it on uniform grids; combining it with adaptive
  refinement is left to future work (§1, §4).
- Not every adaptive high-order code in the bundle refines the mesh.
  [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) call their
  FLEXI scheme "hp-adaptive", but the "h" is a finer finite-volume
  subcell grid inside limited elements and the DG mesh never changes
  at run time (§1, §4; see [h- and hp-adaptation](/methods/hp-adaptation.md),
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
  [IDEFIX](/software/idefix.md) has no AMR; [Lesur et al. (2023)](/sources/lesur-2023.md)
  note that its sequential, dimension-by-dimension ghost-zone exchange,
  faster than a simultaneous 26-neighbour exchange on GPUs, "would not
  suit an AMR version", and point to the Kokkos-based Parthenon framework
  for AMR (§3.4, §6).
- Balsara et al. (2023) show the time-dependent order of accuracy only
  in 2D, on a static two-level mesh with linear media and a final time of
  about $5.7\times10^{-8}$ s; their claim of a "conceptually tight
  solution" of the late-time instability of composite-mesh
  electrodynamics rests on that single test (§9).
- Browne et al. give three different savings figures: 60 % and 9 % in
  Table 6, "about 10%" in the abstract, and "about 5%" in §5.
- Peng et al.'s second-order claim on mapped adaptive meshes is
  verified by [manufactured solutions](/definitions/method-of-manufactured-solutions.md)
  with static refinement only.
- The bundle's sources use refinement with second-order finite volumes
  (Peng et al., Matsushita & Aoki), fifth-order finite differences
  (Browne et al.), finite-difference WENO of unstated order (Zaghi et
  al.; WENO3 in their appendix) and discontinuous Galerkin (Bai & Li);
  none analyses the accuracy of the coarse–fine interface for its
  high-order scheme. Zaghi et al. state only that level jumps "seem to
  not pollute the solution" of a WENO3 vortex (Appendix). Calhoun et al.
  measure third-order convergence of Active Flux on refined grids, a
  measurement rather than an analysis of the interface error (§4).
- Calhoun et al. call theirs "the first implementation of the Active
  Flux method on adaptively refined Cartesian grids" (Abstract). The
  stationarity-preserving acoustic evolution operator of Barsukow et al.
  keeps discrete steady states on a regular grid, but their solver with
  it becomes unstable on adaptive grids (§4.6, Conclusions); the operator
  they use is not stationarity preserving. In their Table 4 the adaptive
  row prints EOCs 3.1045 ($p$) and 2.8564 ($v$), while the printed errors
  give $\log_2(1.64\times10^{-4}/2.06\times10^{-5})=2.99$ and
  $\log_2(3.33\times10^{-5}/3.87\times10^{-6})=3.11$ *(compiler check,
  not in the sources)*.
- Naudet & Zahr's refinement is unstructured and driven by the tracking
  optimization; it has no coarse–fine interfaces, sub-cycling or
  refluxing, and the paper gives no convergence-order study (§5). Their
  Remark 10 states that a triangular prism split without interior points
  needs "four simplices" ($N_3=4$); a triangular prism without Steiner
  points is cut into three tetrahedra, e.g. $\{1,2,3,4\}$, $\{2,3,4,5\}$,
  $\{3,4,5,6\}$ for bottom vertices 1–3 and top vertices 4–6 *(compiler
  check, not in the sources)*.
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) argue for
  r-adaptation instead: the dyadic refinement of AMR produces spurious
  reflection, refraction and scattering of waves at refinement jumps,
  which corrupts Noh and Rayleigh–Taylor solutions and persists or
  worsens under refinement, citing work with RAGE and FLASH (§1.1, §7.1);
  this is a stated argument, not a test of this bundle
  ([adaptive moving mesh](/methods/adaptive-moving-mesh.md)).

# Citations

- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §2.5, Eqs. (21)–(31), Fig. 2; §3.1; §4.1–4.2, Tables 3–4 (accepted manuscript).
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.5, Eqs. (42), (47)–(48); §4, Figs. 6–17; §5.1, Figs. 21–22; §6.3.
- [Browne et al. (2022)](/sources/browne-2022.md) — §3, §3.4, Eqs. (64)–(68), Figs. 8–10; §5, Table 6.
- [Bai & Li (2022)](/sources/bai-2022.md) — §1, §2.2.
- [Wang et al. (2022a)](/sources/wang-2022.md) — §1, §4.
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §1; §7, Eqs. (43)–(52), Figs. 8–10; §8.7, Table 12; §9, Tables 13–15, Figs. 12–15.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §3.4; §6 (arXiv v1).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1, §4 (no mesh adaptation).
- [Zaghi, Salvadore, Di Mascio & Rossi (2023)](/sources/zaghi-2023.md) — §2.2, Figs. 2–3; §3.2, Table 1, Figs. 5–7; Appendix.
- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — arXiv v2: §3.1–3.2, Figs. 3–6; §4.1–4.6, Corollary 4.3, Tables 1–4; Conclusions.
- [Paula, Adami & Adams (2023)](/sources/paula-2023.md) — §2.2 (ALPACA multiresolution and local time stepping).
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) — arXiv v2: §1.1, §7.1 (argument against dyadic refinement).
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §3, §3.3 (Eqs. (31)–(35), Remarks 9–10, Fig. 6); §4.5 (Eqs. (43)–(45)); §5.1.2 (Figs. 12–13); §5.3.2 (Figs. 19–21).
