---
type: Method
title: "Block-structured adaptive mesh refinement"
description: "Hierarchical h-refinement of Cartesian or mapped meshes in nested levels of patches or fixed-size blocks: Berger–Oliger/Colella patch refinement in AMROC, tree-based block refinement on GPUs and in PARAMESH, the refinement criteria (gradients, Richardson error estimates, interface distance, disturbance indicators), coarse–fine transfer, and the measured savings over uniform meshes."
status: established
aliases: [AMR, SAMR, block-structured AMR, structured adaptive mesh refinement, patch-based AMR, tree-based AMR, quadtree AMR, octree AMR]
tags: [amr, finite-volume, finite-difference, software, gpu, multiphase]
timestamp: 2026-10-22T20:00:00Z
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
- **Flux consistency.** Matsushita & Aoki average fine fluxes on coarse
  faces at level gaps, which keeps the phase field conserved (§4); their
  mass error stays at $10^{-16}$ on uniform and adaptive grids (§5.1).

## Measured savings

| Source | Problem | Adaptive against uniform |
|---|---|---|
| Peng et al. §4.1, Table 3 | blunt-body combustion, Mach 4.18, to 0.2 ms | 308.6 against 240.0 CPU h at 7 µm (two levels), 1193.5 against 1286.7 at 3.5 µm (three), 5521.6 against 9590.6 at 1.75 µm (four), a factor 1.74 |
| Browne et al. §5, Table 6 | hypersonic flat-plate wavepacket | about 55 million against 91.7 million points (linear), 66 million against 715 million (strongly nonlinear): 60 % and 9 % |
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
Browne et al. compare finite-difference adaptive points with a DNS that
is Fourier-spectral in the spanwise direction, a caveat they state
(§5).

## Qualifications

- [Wang et al. (2022)](/sources/wang-2022.md) implement their
  ghost-cell [immersed boundary](/methods/immersed-boundary-method.md)
  in AMROC but run it on uniform grids; combining it with adaptive
  refinement is left to future work (§1, §4).
- Browne et al. give three different savings figures: 60 % and 9 % in
  Table 6, "about 10%" in the abstract, and "about 5%" in §5.
- Peng et al.'s second-order claim on mapped adaptive meshes is
  verified by [manufactured solutions](/definitions/method-of-manufactured-solutions.md)
  with static refinement only.
- The bundle's sources use refinement with second-order finite volumes
  (Peng et al., Matsushita & Aoki), fifth-order finite differences
  (Browne et al.) and discontinuous Galerkin (Bai & Li); none analyses
  the accuracy of the coarse–fine interface for its high-order scheme.

# Citations

- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §2.5, Eqs. (21)–(31), Fig. 2; §3.1; §4.1–4.2, Tables 3–4 (accepted manuscript).
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.5, Eqs. (42), (47)–(48); §4, Figs. 6–17; §5.1, Figs. 21–22; §6.3.
- [Browne et al. (2022)](/sources/browne-2022.md) — §3, §3.4, Eqs. (64)–(68), Figs. 8–10; §5, Table 6.
- [Bai & Li (2022)](/sources/bai-2022.md) — §1, §2.2.
- [Wang et al. (2022)](/sources/wang-2022.md) — §1, §4.
