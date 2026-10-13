---
type: Source
title: "Hoppe, Winter, Adami & Adams (2022) — ALPACA: a level-set based sharp-interface multiresolution solver for conservation laws"
description: "The CPC record of ALPACA, an MPI-parallel C++20 finite-volume code for compressible multi-phase flow on a block octree with Harten-type multiresolution refinement, adaptive local time stepping, a cited resolution-jump flux correction and a one-byte interface tagging system, weak-scaled to 512 SuperMUC-NG nodes; no divergence-constraint content."
resource: "doi:10.1016/j.cpc.2021.108246"
source_kind: paper
authors: [Hoppe N., Winter J.M., Adami S., Adams N.A.]
year: 2022
venue: "Comput. Phys. Commun. 272:108246"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2022-CPC-Hoppe-101016jcpc2021108246.pdf"
tags: [amr, tree-amr, multiresolution, subcycling, production-code]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

ALPACA is an MPI-parallel C++20 finite-volume framework for multi-phase
compressible Navier–Stokes flows. Each phase uses a Riemann solver with
WENO/TENO reconstruction. Immiscible phases are coupled by a sharp-interface
level-set method with conservative interface interaction (cut cells,
a two-material interface Riemann solver, ghost-fluid extrapolation,
small-cell mixing). The load is reduced by a block-based Harten-type
multiresolution (MR) algorithm on a binary, quad or octree of fixed-size
blocks, with adaptive local time stepping. The paper's new contribution is
an **interface tagging system** that confines the multi-phase overhead to
the finest level and to a narrow band.

**The paper has no divergence-constraint content**: no MHD, no
incompressible projection, no cleaning, no elliptic solve. $\mathrm{div}(u)$
appears only inside the compressible viscous stress tensor (eq. 6). It is
ingested as AMR infrastructure under the bundle's AMR-frameworks
assignment: a block-tree code with multiresolution refinement, local time
stepping and a coarse–fine flux correction.

# Key claims

1. **Discretization** (§§2–3, eqs. 1–44). Compressible NSE with gravity,
   Fourier heat flux and Newtonian stress, closed by an EOS. Cut cells
   carry volume fractions and face apertures. The semi-discrete phase
   balance sums aperture-weighted face fluxes, interface exchange fluxes
   and volume forces (eq. 27). The level set is reinitialized after
   Sussman et al. Explicit SSP Runge–Kutta advances both the flow and the
   level set. The time step is the CFL-scaled minimum of convective,
   viscous, volume-force, heat and capillary limits (eqs. 43–44), with
   CFL < 1 for full cells.
2. **Modularity** (§4, Table 2, §7.2). Roe, LLF, GLF, HLL, HLLC and HLLC-LM
   Riemann solvers; WENO-3 to WENO-9 variants and TENO-5; RK-2 and RK-3;
   four EOS families. Building blocks are chosen at compile time through
   CRTP.
3. **Multiresolution representation** (§5, eqs. 45–46). The solution is
   expanded in scaling functions plus wavelet details on dyadic grids
   (refinement ratio 2, implied by eq. 45). A prediction operator (coarse to
   fine) and a "conservative averaging" operator (fine to coarse) are
   stated to be consistent: averaging a prediction returns the coarse data.
   With interpolation wavelets the detail is the prediction error (eq. 46).
   Details "below a level-dependent threshold" are set to zero; zero
   details mean coarsen, non-zero details mean refine.
   **The threshold value, its level dependence, and the stencil and order
   of the prediction are not given**; they are deferred to Hoppe et al.
   (arXiv:2012.04385) and Harten-type MR references.
4. **Tree and blocks** (§§5–6).
   * Nodes are parents or leaves, and parents are kept: ancestor storage
     is counted in the compression metric $C_{mr}$ (§10).
   * Refinement is block-wise. Every block on every level holds a fixed
     number of cells, "e.g. $32^3$". The authors concede lower compression
     than cell-based MR but call it "of little relevance for
     three-dimensional cases".
   * A block is the domain-decomposition unit. Halo cells carry inter-block
     dependencies.
   * "The halo concept ensures the graded-tree property even for arbitrary
     resolution jumps between neighboring blocks" (§5). **No 2:1 level
     limit between neighbouring blocks is stated.**
5. **Local time stepping** (§5, Algorithms 1, 3, Table 5). Coarser levels
   take larger steps. The number of finest-level (micro) steps per
   coarsest-level (macro) step is printed as $2^{l_{max}-1}$ (p. 7), with
   $l_{max}$ the finest level. The time step is readjusted after every
   micro step, following Kaiser et al.
6. **Coarse–fine coupling** (Algorithms 1–3).
   * At a resolution jump, the halo update fills halo cells by prediction
     from the coarser level, otherwise by copy from the same-level
     neighbour. Algorithm 1 applies it to the right-hand side as well as to
     the solution.
   * Right-hand sides are averaged up the tree at every stage.
   * Halo cells on the fine side of a jump are integrated in time with the
     same Runge–Kutta operator as the interior, driven by the predicted
     right-hand side. The paper describes no temporal interpolation of
     ghost data.
   * After each stage the solution is averaged to the next-coarser level.
   * At the last Runge–Kutta stage a "Resolution jump flux correction" is
     applied (Algorithm 1). **No formula, register description or
     conservation measurement is given**; everything is deferred to Kaiser
     et al. (2019, J. Comput. Phys. X 4:100038). Conservation at jumps is
     asserted by reference only.
7. **Interface tagging** (§6, eqs. 47–49, Figs. 2–3), the novelty.
   * Single-phase nodes hold one fluid block. Multi-phase nodes hold two
     fluid blocks, plus a level-set block if they are leaves. All nodes
     hold a tag block. Nine rules govern refinement, allocation and
     deallocation.
   * Only single-phase nodes take part in MR coarsening and refinement;
     leaves are refined to the finest level as the interface approaches, so
     interfaces always sit on the finest level.
   * One-byte tags: 0 for cut cells, ±3 for the cut-cell neighbour band
     (±1 cell), ±7 for the extension band (±3 cells), ±8 for the
     reinitialization band (±4 cells); the sign is that of the level set.
     Coarse tags are the product of the fine tags, then reset from distance.
8. **Parallelization** (§7.1). MPI only, with compiler-generated SIMD; **no
   GPU**. Lightweight topology is separated from heavy data, which sit in a
   rank-local hash map keyed by unique node ids. Load balancing uses a
   level-wise [space-filling curve](/definitions/space-filling-curve.md)
   (type not stated here); parents go to the rank holding most of their
   children. The load is rebalanced every micro step if the topology
   changed.
9. **Performance** (§§9–10; SuperMUC-NG, 48 Skylake cores per node).
   * Profiling: the level set takes about 25–26 % of runtime, MR routines
     8.5–9.3 %, flux computation "> 52 − 66%".
   * **Weak scaling** (§9.1, Fig. 20b): two-phase Sod tube to 512 nodes
     (24 576 cores), about 685 billion DOFs of which 100 billion are
     computed. The text says efficiency "stays above 75% for all
     workloads". Read from Fig. 20b at 512 nodes: about 0.84 (standard
     executable) and about 0.74–0.75 (shuffle executable).
   * **Strong scaling** (§9.2, Fig. 21): 3D RMI, about 2.6 million to
     85 billion DOFs, core counts to about $3\cdot10^4$ on the figure axis.
     Graphical only; no efficiency number is given.
   * **Compression** (§10, Fig. 22): multi-phase cells $C_v > 90\%$,
     level-set cells $C_{ls} > 92\%$, and $\mathcal O(10^{10})$ effective
     DOFs at compression above 90 %.
10. **Positioning** (§1, author assertions with citations). MR gives
    "larger compression" and "better" error control than AMR; the block
    concept is taken from wavelet collocation and AMR.

**Tests** (§8): 1D Gaussian-bell convergence (single and two-phase,
finest level 1 to 7; "the scheme of lowest-order dominates the overall
convergence order", graphical only), 2D shear-drop deformation against
Taylor's law, 2D SF6/air Richtmyer–Meshkov, air–helium, air–R22 and
water–air shock–bubble interactions in 2D and 3D against published
references. None involves a divergence constraint.

# Notation map

| Hoppe et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $l_m$ (MR level) | $l$ | |
| dyadic grids | $r = 2$ | the paper's own $r$ is the micro-step counter, not the refinement ratio |
| $\mathcal P$ (prediction) | $P$ | stencil and order not stated |
| $\mathcal A$ (conservative averaging) | $R$ | $\mathcal A\mathcal P = I$ is the registry $R P = I$, on cell averages |
| $\mathcal H$ with `include_jumps` | $\Gamma$ | order $q$ not stated |
| $\Delta x$ | $h$, $H$ | |
| $d^{l_m}_k$, $\psi^{l_m}_k$ (details, wavelets) | words | $\psi$ collides with $\psi_h$ |
| $\phi$ (level set) | words | collides with $\phi_h$ and $\phi_{\mathrm g}$ |
| $\tilde D$, $\tilde D_{NSE}$ (right-hand sides) | words | collide with $D_h$ and $\mathcal D$ |
| $\mathcal E$ (time evolution) | words | collides with $E_h$ and the $\mathcal E^{\circ}$, $\mathcal E^{\alpha}$, $\mathcal E^{c}$ EMFs |
| $A^{\xi_a}$ (face apertures) | words | collides with $A_h$ |

# Pages created or updated

* Updated [Block-structured AMR](/definitions/block-structured-amr.md) (MR-driven block tree with kept parents, halos advanced by predicted right-hand sides, local time stepping).
* Updated [Refluxing](/methods/refluxing.md) (flux correction stated by citation only).

# Citations

1. `~/papers/mosaic/div-free-amr/2022-CPC-Hoppe-101016jcpc2021108246.pdf`.
   * **Version.** The published Elsevier version, 20 pages. Received
     12 Mar 2021, accepted 23 Nov 2021, online 1 Dec 2021.
   * **Identity.** doi:10.1016/j.cpc.2021.108246, checked on Crossref:
     Comput. Phys. Commun. 272:108246, March 2022, four authors (Hoppe and
     Winter contributed equally). Program library DOI 10.17632/5zr3sg83ct.1;
     code at https://gitlab.lrz.de/nanoshock/ALPACA (GPLv3).
   * **How it was read.** Text extraction, all sections. Eqs. 16–24 and
     27–44 were checked on the rendered pp. 4 and 6; eq. 13 and the
     volume-force criterion of eq. 44 were not rendered in full.
   * **Defects in the paper.**
     * The micro-step count $2^{l_{max}-1}$ (p. 7) and the micro-step range
       $0,\dots,2^{l_{max}}$ of Table 5 do not obviously agree; Table 5
       also uses an operator "$\vee$" that is not defined.
     * Eq. 50 prints the second Gaussian as $5.0\exp((x-1.5)^2)$, which is
       not a decaying bell (a coefficient and sign are missing).
     * Fig. 4 names a "WENO-1" scheme that is not in Table 2.
   * **Reference list:** 99 entries, all merged; Crossref's
     reference count agrees. The key `hoppe-2022` already existed in the
     bibliography (cited by [Zaghi et al. (2023)](/sources/zaghi-2023.md)).
     Identity resolutions: Berger & Colella 1989 is `berger-colella-1989`;
     Jiang & Shu 1996 is `jiang-shu-1996`; LeVeque's 2nd edition is
     `leveque-1992` (distinct from `leveque-1990`); Munz, Ommes & Schneider
     (Comput. Phys. Commun. 130:83) is `munz-2000-b`; Cohen, Kaber, Müller
     & Postel (Math. Comp. 72:183) is `cohen-2001-b`; Toro's shallow-water
     book is `toro-2001-b`; Vasilyev 2000 is `vasilyev-2000-b`; Fedkiw 1999
     is `fedkiw-1999-b`; Balsara, Garain & Shu (2016) is `balsara-2016-b`;
     Fleischmann, Adami & Adams (2020, J. Comput. Phys. 423) is
     `fleischmann-2020-b`. DOIs printed in the list filled three entries.
