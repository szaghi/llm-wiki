---
type: Method
title: "Block-structured adaptive mesh refinement"
description: "Hierarchical h-refinement of Cartesian or mapped meshes in nested patches or fixed-size blocks (AMROC, PARAMESH, ForestClaw, ADAM, AthenaK, AMReX): refinement criteria, coarse–fine transfer from second-order to WENO, divergence-preserving and Active Flux transfers, refluxing and its conservation analysis, sub-cycling with and without time interpolation, and measured savings and accuracy against uniform meshes."
status: established
aliases: [AMR, SAMR, block-structured AMR, structured adaptive mesh refinement, patch-based AMR, tree-based AMR, quadtree AMR, octree AMR]
tags: [amr, finite-volume, finite-difference, software, gpu, mhd]
timestamp: 2026-10-24T05:59:00Z
---

# Block-structured adaptive mesh refinement

Block-structured adaptive mesh refinement covers the regions that need
resolution with a hierarchy of finer and finer logically rectangular
grids, each level refining the one below by an integer factor (2 in
every computation of the bundle; [Wang et al. (2026)](/sources/wang-2026.md)
also tabulate transfer coefficients for a factor of 4), while the rest of
the domain stays coarse.
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
[Liang & Fu (2026)](/sources/liang-2026.md) (§3.1) use the same kind of
cell-average multiresolution (after Harten, Bihari & Harten, as recalled)
on the pyramid data structure of Han, Hu & Adams: blocks of 4 cells in 1D
and $4\times4$ in 2D are the unit of adaptation, flagged empty or occupied,
with ghost memory permanently allocated, and only leaf blocks are
advanced, by a [converged ENO](/methods/converged-eno.md) finite-volume
scheme with local time stepping aimed at steady states.
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
[Stone et al. (2026)](/sources/stone-2026.md) keep the design of Athena++
in their Kokkos rewrite [AthenaK](/software/athenak.md): MeshBlocks in an
octree (binary tree or quadtree in 1D and 2D) labelled by Z-ordering,
communication between levels only at block boundaries, flux corrections at
level boundaries for conservation, one time step for all levels, and
task-list execution (§2). New are the **MeshBlockPacks**, which aggregate
all MeshBlocks of a device so that one kernel launch covers them, an idea
the authors credit to the Parthenon framework; the variables of a pack are
$(N+1)$-dimensional device arrays whose extra index is the MeshBlock, the
tree is built and refined on the host, and prolongation and restriction of
all blocks are done at once in parallel kernels (§2). Load balancing
assigns each MeshBlock a cost proportional to its cells and physics modules
and redistributes blocks while keeping Z-ordering (§5.2). Wang et al.
(2026) build their finite-difference AMR on AMReX, regridding every
`regrid_int` steps (§6).

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

- **Smoothness-indicator agreement with a buffer band.** Liang & Fu (2026)
  (§3.3, Eqs. (27)–(28)) flag cells by the agreement of the three
  smoothness indicators $\beta_0,\beta_1,\beta_2$ the reconstruction has
  already computed (one five-point, two two-point stencils):
  $$\chi_{\mathrm D}=\min_{k<l}\frac{2\beta_k^2\beta_l^2+\epsilon}{\beta_k^4+\beta_l^4+\epsilon}\in(0,1],\qquad\epsilon=10^{-8}$$
  (page-local $\chi_{\mathrm D}$, the source's $\chi$, not the TENO $\chi_k$),
  close to 1 where the indicators agree and small at discontinuities, in
  characteristic variables. A block is refined if any cell has
  $\chi_{\mathrm D}<\varepsilon_{\mathrm r}$, coarsened if all cells have
  $\chi_{\mathrm D}>\varepsilon_{\mathrm c}$, and left unchanged otherwise, with
  $\varepsilon_{\mathrm r}=0.3<\varepsilon_{\mathrm c}=0.7$ "based on preliminary
  numerical experiments" (page-local thresholds). The authors introduce the band between
  the two thresholds so that the mesh freezes once the flow is steady. The
  authors call the criterion problem-independent because its range is
  fixed, block-local (unlike Harten-type prediction-error criteria, which
  need inter-level data and case-by-case thresholds) and cheap (Remarks
  1–3), and judge hybrid-scheme shock detectors unsuitable for steady
  adaptation (§3.3). Over five threshold pairs the solutions are "not very
  sensitive" to them (§5.2–5.3, Figs. 9–10, 14–15). Zaghi et al.'s split
  and recomposition thresholds above also form such a band, stated there
  as a guard against flip-flop.

- **Thresholds on a flow variable.** Stone et al. refine where the density
  exceeds the background by a factor of 1.1 (2D MHD blast) or by half the
  wave amplitude (AMR scaling test), and by pressure in the Komissarov
  cylindrical explosions (§3.5, §5.1–5.2). Wang et al. refine where
  $\rho>1.19$ in a dynamic-refinement convergence test, where the
  dilatation falls below a user threshold (value not given) in decaying
  isotropic turbulence, and on fixed thin sheets in their Euler–Burgers
  test (§6.1–6.4). Their [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
  does not refine: it chooses the transfer operator (below).

**When to remesh.** Matsushita & Aoki remesh when the interface has
moved $2\Delta x_{\min}$, estimated from the acoustic time step
(Eq. 42); Browne et al. every $n_{\mathrm R}=\Delta t_{x,b}/\Delta t$
steps, with $\Delta t_{x,b}=\Delta x\,n_{x,b}/(u+c)$ the time the
fastest wave needs to cross a block of $n_{x,b}$ cells (Eqs. 64–65).
On their three-dimensional flat plate this amounted to 520
refinement steps in about 130,000 time steps (§5).

**Remeshing that never stops.** Liang & Fu (2026) state that classical
adaptation keeps refining and coarsening at a steady state because of its
sensitivity, which changes the reconstruction formula from step to step
and keeps the residual from reaching machine zero (§1, §3.3); their buffer
band is the remedy. Because the leaf set changes in time, they measure the
residual on a fixed virtual root level, obtained by recursively averaging
the leaf data up to it,
$\mathrm{Res}=\frac1{4N_{\mathrm{root}}}\sum_i\big(\lvert R^\rho_i\rvert+\lvert R^{\rho v_1}_i\rvert+\lvert R^{\rho v_2}_i\rvert+\lvert R^E_i\rvert\big)$
with $R_i=(u^{n+1}_i-u^n_i)/\Delta t$ per conserved variable (§4.2, Eq. (31);
page-local).

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

- **Flux correction with a positivity fallback.** In AthenaK the
  first-order flux correction (FOFC), which recomputes all face fluxes of a
  cell with piecewise-constant states and the local Lax–Friedrichs flux when
  density or pressure would turn negative, must be applied before the flux
  corrections at level boundaries (Stone et al. §3). Staggered
  [constrained transport](/methods/constrained-transport.md) complicates the
  ghost-zone and flux-conservation logic of AMR but is "critical for some
  problems" (§3.2).

**High-order transfer on a cell-centred finite-difference layout.**
[Wang et al. (2026)](/sources/wang-2026.md) analyse coarse–fine transfer for
fifth-order finite-difference [WENO-JS](/methods/weno-js-reconstruction.md)
with characteristic Lax–Friedrichs splitting. Earlier high-order
finite-difference AMR, as they recall it (Shen, Qiu & Christlieb; Sebastian
& Shu for multidomains), is node-based: coarse and fine solution points
coincide at the interface, transfers are point-wise interpolations, and
there is no location at which coarse and fine fluxes can be reconciled
(§1, §3.1). They place solution points at cell centres and flux points at
faces, the staggered layout of [WCNS](/methods/weighted-compact-nonlinear-scheme.md)
and spectral difference, equivalent to the node-based scheme on a uniform
grid, so that patch boundaries are flux points and refluxing applies
(§2.1, §3.1). Two closures follow:

- **AMR-Berger&Colella** (second order, conservative): limited
  piecewise-linear prolongation that keeps the coarse value and
  volume-weighted restriction, with cell values read as cell averages; with
  refluxing the composite totals change only through physical boundary
  fluxes (App. B, Eq. (B.7)).
- **AMR-WENO** (non-conservative): a fifth-order WENO interpolation for
  prolongation, re-derived for cell-centred children of ratio 2 and 4. For
  ratio 2 the child at $x_i-\Delta x_{\mathrm c}/4$ uses three 3-point
  coarse candidates with linear weights $d_k=(15/64,\,21/32,\,7/64)$, the
  other child following by reflection, and Jiang–Shu indicators integrated
  over the coarse cell (Tables 1–2; page-local $\Delta x_{\mathrm c}$,
  $\Delta x_{\mathrm f}$ the coarse and fine spacings). Restriction is a
  central WENO interpolation on six fine points with four 3-point
  candidates and $d_k=(1/32,\,15/32,\,15/32,\,1/32)$, optimally sixth
  order, on the conserved variables without upwind bias; two fine ghost
  cells complete the stencil near patch edges (§3.2.2, Table 3, App. A).
  The authors state that it keeps at least third order near
  discontinuities (App. A), without a demonstration.

Their error analysis (Apps. C–D) states that non-conservative transfers
change the composite mass by $O(\Delta x)$ at discontinuities and
$O(\Delta x^p)$ in smooth regions, accumulating over restrictions, which
refluxing cannot repair; the violated discrete
[Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md) balance shifts
the shock speed by $O(\Delta x)$, a drift visible for slowly moving shocks
(App. C). Berger–Colella transfers degrade the local truncation error of
fine points whose stencil crosses the interface to $O(\Delta x_\ell)$ and
the global $L_1$ truncation error to $O(\Delta x^2)$ whatever the order $p$
of the scheme (Eqs. (D.13), (D.21)); $p$th-order WENO prolongation loses at
most one order locally and none globally, because the number of interface
points is bounded, giving $\min(p,q)$ with a $q$th-order Runge–Kutta method
(Eqs. (D.17), (D.25)–(D.26)).

They describe three ways a discontinuity meets the hierarchy (§5.1): it
stays on the finest level (errors confined to the coarse level); it crosses
a coarse–fine interface (conservation errors, curable by flux correction
in the cell-centred layout); or it is refined or coarsened abruptly, when
the WENO restriction picks one-sided stencils, steepens the shock and
corrupts the coarse values that are then advanced. Since, in their words,
"no single interpolation scheme can simultaneously maintain high-order
accuracy in smooth regions and guarantee conservation at discontinuities",
**AMR-HybridWENO** uses WENO transfers in smooth regions and second-order
linear interpolation in space and time, with slopes "constrained using a
local Lax-Friedrichs limiter", in cells flagged by a Roe-averaged Lax-type
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) with a
mapped pressure curvature, plus flux correction (§5.2–5.3, Eqs. (44)–(50)).
They also find WENO interpolation "significantly more robust than the
Lagrange interpolation of comparable order" (§5.3); on double Mach
reflection both pure WENO and Lagrange transfers fail at once with negative
density (§6.4.2).

**Multiresolution prediction.** In Liang & Fu (2026) coarsening averages
the two children, $\bar u^l_i=\tfrac12(\bar u^{l+1}_{2i}+\bar u^{l+1}_{2i+1})$, and
refinement predicts them from the parent and its neighbours,
$\hat u^{l+1}_{2i,\,2i+1}=\bar u^l_i\pm\sum_{m=1}^2\mathsf c_m(\bar u^l_{i+m}-\bar u^l_{i-m})$
with $\mathsf c_1=-22/128$, $\mathsf c_2=3/128$, fifth order and conservative
between levels (Eqs. (8)–(10); page-local $\mathsf c_m$, the source's
$\gamma_k$). *(Compiler check, not in the sources: for $u=x$ the
prediction returns the exact child averages $x_i\mp\Delta x/4$ of the
parent spacing $\Delta x$.)*

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
(Table 3).

**Sub-cycling with Runge–Kutta-consistent time interpolation.** Wang et
al. (2026) (§3.3, Eqs. (8)–(9)) sub-cycle with SSP-RK3 and fill fine ghost
cells by the time interpolant adapted from McCorquodale & Colella,
$$u(t^n+\eta\Delta t_{\mathrm c})=u^n+k_1\eta+\big(-\tfrac56k_1+\tfrac16k_2+\tfrac23k_3\big)\eta^2+O(\Delta t_{\mathrm c}^3),$$
with $k_1,k_2,k_3$ the stage increments ($\Delta t$ included) and
$\eta\in[0,1]$ the time fraction (page-local), aligned with the stage times
of the fine step so that ghost and interior values do not differ enough to
trigger the WENO weights. At $\eta=1$ it returns
$u^n+\tfrac16k_1+\tfrac16k_2+\tfrac23k_3$, the SSP-RK3 update *(compiler
check, not in the sources)*. Refluxing is written for a generic $s$-stage
Runge–Kutta method, the coarse cell next to the interface being corrected
by $\sum_mb_m\,\delta\hat f\,\Delta t/\Delta x$, $\delta\hat f$ the coarse–fine
flux difference of stage $m$ and $b_m$ the Runge–Kutta weights (§3.4, Eqs.
(10)–(12); page-local). Stone et al. (2026) use one time step on all
levels instead (§2); in their efficiency test the AMR run still takes a
larger step than the uniform one, because the largest wave speeds lie on
the coarse grid (§5.1).

**Spectral analysis of the composite operator.** Wang et al. (§4) extend
the Fourier analysis of the
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
to AMR by a Bloch-wave analysis of a periodic coarse–fine–coarse macro-cell
with linear weights: the cell-centred closures disperse less than the
node-based one for $\vartheta\in[1.5,2.5]$, AMR-WENO stays closest to the
uniform fifth-order operator near the grid cutoff, all closures add
dissipation from $\vartheta\approx2$ (Fig. 5), and the global spectra lie in
the closed left half-plane, inside the SSP-RK3 stability region up to a
fine-level CFL number of 1.43 (Eqs. (38)–(42), Fig. 6). Paula et al. adapt the time step after every finest-level step
by local time stepping, which lets them use the CFL numbers of uniform
grids (§2.2).

## Measured savings

| Source | Problem | Adaptive against uniform |
|---|---|---|
| Peng et al. §4.1, Table 3 | blunt-body combustion, Mach 4.18, to 0.2 ms | 308.6 against 240.0 CPU h at 7 µm (two levels), 1193.5 against 1286.7 at 3.5 µm (three), 5521.6 against 9590.6 at 1.75 µm (four), a factor 1.74 |
| Browne et al. §5, Table 6 | hypersonic flat-plate wavepacket | about 55 million against 91.7 million points (linear), 66 million against 715 million (strongly nonlinear): 60 % and 9 % |
| Zaghi et al. §3.2, Table 1 | 3D shock diffraction by a sphere, finest spacing 0.015625 | 350.3 million cells in 684,258 blocks; the authors' uniform-grid figure is "8 billions", a $1280^3$ grid has $2.1\times10^9$ *(compiler check, not in the sources)* |
| Stone et al. §5.1, Fig. 20 | 2D MHD blast, one A100 GPU, pressure ratio 100 | uniform $4096^2$ at 181 Mzcps against AMR ($1024^2$ root, two levels) at 141 Mzcps, about 20 % overhead; the AMR run takes 18 % of the wall-clock time ("5.4× faster" in the caption), with essentially identical density |
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

Liang & Fu (2026) (§5.8, Table 1) compare user CPU time on steady Euler
problems against uniform finite-volume WENO5-Z at the finest resolution:
their adaptive scheme takes 0.408 of it on a 1D stationary shock
($N=512$), 0.277 on an oblique shock ($1024\times512$), 0.252 on a regular
shock reflection ($2048\times512$), 0.163 on supersonic flow past a plate,
0.528 and 0.425 on two shock interactions ($1024\times512$), with
compression ratios of the finest-level leaf cells above 85–90%; uniform
TENO5 takes 1.003–1.412 of the WENO5-Z time. No hardware is stated, and
the ratios are of whole runs, which differ in mesh and reconstruction,
the adaptive one with local time stepping ([steady shock problems](/benchmarks/steady-shock-problems.md)).

Stone et al. (§5.2, Fig. 22) run AMR weak scaling on Frontier up to 4096
GPU dies with a sound wave refined on its crests: super-linear scaling while
the MeshBlock size grows, and nearly perfect scaling with fixed $32^3$
MeshBlocks, with over 5 million MeshBlocks moved for load balancing at the
largest size. They attribute the 20 % overhead partly to the small work per
MeshBlock of a 2D mesh (§5.1).

**Accuracy and robustness of high-order transfers.** Wang et al. (2026)
measure on a two-level grid (ratio 2): $L_1$ density orders 4.35, 4.86,
5.40 for a manufactured steady Navier–Stokes solution, and 4.65, 4.83,
4.92 for smooth unsteady advection with dynamic refinement and
$\Delta t=0.2\Delta x^2$ (Table 6;
[manufactured solutions](/definitions/method-of-manufactured-solutions.md)).
Without flux correction the conservation error of the smooth problem
converges at fifth order (Table 7); with flux correction, they state
without a table, the coarse–fine flux mismatch limits it to second order
(§6.1). On slowly moving Mach 2 and Mach 3 shocks crossing seven
coarse–fine interfaces, WENO transfers without flux correction distort at
the first interface and with it oscillate and later fail, while
HybridWENO keeps a sharp shock to $t=30$ (Mach 3, Fig. 12;
[steady shock problems](/benchmarks/steady-shock-problems.md)). On the Sod
and Lax tubes regridding every 5 or 10 steps makes AMR-WENO oscillate and
overshoot the shock speed while HybridWENO matches the uniform reference;
at `regrid_int` = 2 they coincide (Figs. 13–14). In decaying
[compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
at $M_{t,0}=1.0$ on a $64^3$ base with two levels, pure WENO transfers fail
at $t\approx3.4\tau_{\mathrm e}$ while shocklet regions are coarsened, Berger–Colella
transfers are the most dissipative, and HybridWENO survives with a
dissipation that approaches that of WENO transfers (§6.4.3, Figs. 21–22;
page-local $\tau_{\mathrm e}$ the eddy time).

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
  (Browne et al., Wang et al. (2026)), finite-difference WENO of unstated
  order (Zaghi et al.; WENO3 in their appendix), finite-volume PLM, PPM and
  WENO-Z (Stone et al.) and discontinuous Galerkin (Bai & Li). Only Wang et
  al. (2026) analyse the truncation and conservation errors of the
  coarse–fine interface for a high-order scheme (Apps. C–D, a static
  two-level 1D hierarchy). Zaghi et al. state only that level jumps "seem
  to not pollute the solution" of a WENO3 vortex (Appendix). Calhoun et al.
  measure third-order convergence of Active Flux on refined grids, a
  measurement rather than an analysis of the interface error (§4).
- **Wang et al. (2026) on earlier transfers.** They call the argument of
  Shen, Qiu & Christlieb, that the conservation loss of node-based
  transfers at shocks is hidden under the overlying fine grid, "overly
  idealized", because it assumes discontinuities confined to the finest
  level; at `regrid_int` = 2 they reproduce agreement with that work, and
  at 5 and 10 they show failures (§1, §5.1, §6.3.1). They report, as a
  summary of Sebastian & Shu, that Lagrange interpolation was found more
  efficient and accurate enough at multidomain interfaces, while they find
  WENO interpolation more robust in AMR with regridding (§1, §5.3). Neither
  earlier work is a source of the bundle; the settings differ.
- **Strict conservation and its scope (Wang et al. 2026).** The abstract
  and §3.4 claim strict conservation at coarse–fine interfaces by flux
  correction; Appendix B proves global conservation for the
  Berger–Colella closure only, and Appendix C states that refluxing does
  not restore it when the transfers are non-conservative, as the WENO ones
  are. The second-order conservation error with flux correction (§6.1) is
  stated without a table. The CFL bound 1.43 and the Bloch spectra concern
  the linear-weight operator.
- **Printed slips in Wang et al. (2026).** In Table 7 the density errors
  $5.95\times10^{-4}$ and $2.13\times10^{-5}$ give the order
  $\log_2(5.95\times10^{-4}/2.13\times10^{-5})=4.80$, while 5.02 is printed,
  the density orders repeating those of the momentum column *(compiler
  check, not in the sources)*. Appendix B prints the coarse update as
  $U^{n+1}_{\ell-1,i}=U^n_{\ell-1,i}-\frac{\Delta t_{\ell-1}}{\Delta x_{\ell-1}}\big(F_{\ell-1,i+1/2}-F_{\ell-1,i-1/2}\big)+\mathcal R_{\ell-1,i}$
  with $\mathcal R_{\ell-1,i}=\frac{\Delta t_{\ell-1}}{\Delta x_{\ell-1}}\big(\bar F_\ell-F_{\ell-1,i+1/2}\big)$
  (Eqs. (B.3), (B.6); page-local $U$, $F$, $\bar F_\ell$ the time-averaged
  fine flux, $\mathcal R$ the reflux term), for a coarse cell whose right
  face $i+1/2$ is the interface; substituted, this gives
  $-\frac{\Delta t}{\Delta x}\big(2F_{\ell-1,i+1/2}-\bar F_\ell-F_{\ell-1,i-1/2}\big)$
  instead of replacing $F_{\ell-1,i+1/2}$ by $\bar F_\ell$, which needs
  $\mathcal R_{\ell-1,i}=\frac{\Delta t_{\ell-1}}{\Delta x_{\ell-1}}\big(F_{\ell-1,i+1/2}-\bar F_\ell\big)$
  *(compiler check, not in the sources)*. The caption of Fig. 6
  nondimensionalizes the eigenvalues with $\Delta x_{\mathrm c}$, Eq. (38)
  with $\Delta x_{\mathrm f}$.
- **Stone et al.'s AMR claims** are measurements on one GPU and on
  Frontier (Figs. 20, 22); the 20 % overhead and 5.4 × speed-up concern a
  2D blast, which the authors expect to overstate the overhead.
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
- Liang & Fu (2026) do not state which time step enters the root-level
  residual under local time stepping (§4.2), and their multi-dimensional
  scheme uses the mid-point flux rule, second order overall (§4.1); the
  residual levels of their uniform-mesh comparators concern their own
  finite-volume implementations with HLLC.
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
- [Liang & Fu (2026)](/sources/liang-2026.md) — §1; §3.1, Eqs. (8)–(10); §3.3, Eqs. (27)–(28), Remarks 1–3; §4.1–4.2, Eqs. (30)–(31); §5, Eq. (32), Figs. 9–10, 14–15; §5.8, Table 1.
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §3, §3.3 (Eqs. (31)–(35), Remarks 9–10, Fig. 6); §4.5 (Eqs. (43)–(45)); §5.1.2 (Figs. 12–13); §5.3.2 (Figs. 19–21).
- [Stone et al. (2026)](/sources/stone-2026.md) — §2; §3 (FOFC), §3.2, §3.5; §5.1, Fig. 20; §5.2, Fig. 22.
- [Wang et al. (2026)](/sources/wang-2026.md) — §1; §2.1; §3.1–3.4, Eqs. (8)–(12), Tables 1–3; §4, Eqs. (38)–(42), Figs. 5–6; §5.1–5.3, Eqs. (44)–(50); §6.1–6.4, Tables 6–7, Figs. 12–14, 21–22; Apps. A–D.
