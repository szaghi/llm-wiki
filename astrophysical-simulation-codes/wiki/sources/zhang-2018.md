---
type: Source
title: "Zhang, Schive & Chiueh (2018) — Magnetohydrodynamics with GAMER"
description: "Extends the GPU-accelerated octree-patch AMR code GAMER to ideal MHD with Athena's CTU and VL unsplit integrators plus constrained transport, keeps the divergence free across levels with Balsara (2001) prolongation and coarse-fine EMF correction, and reports 1.2e8 (single) / 5.5e7 (double) cell updates per second on one P100 and about 70% weak and strong scaling efficiency on 1024 Blue Waters GPU nodes."
resource: "doi:10.3847/1538-4365/aac49e"
source_kind: paper
authors: [Zhang U.-H., Schive H.-Y., Chiueh T.]
year: 2018
venue: "Astrophys. J. Suppl. 236:50"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2018-ApJS-Zhang-1038471538-4365aac49e.pdf"
tags: [software, mhd, amr, constrained-transport, gpu, performance, unsplit, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

GAMER is a GPU-accelerated AMR code built on an octree of fixed-size
patches. This paper extends it from hydrodynamics to ideal MHD. The MHD
update takes the two unsplit schemes of Athena, CTU and the
MUSCL-Hancock (VL) predictor-corrector, each with constrained transport on
a staggered mesh, PLM or PPM reconstruction, and HLLE, HLLD or Roe
Riemann solvers. On the AMR hierarchy the divergence of $\mathbf B$ stays
zero through area-averaged restriction, EMF correction on coarse-fine
edges and Balsara (2001) divergence-free prolongation (§3). The
parallel design is inherited from GAMER. The solver runs on the GPU on
patch groups of $2^3$ patches. AMR bookkeeping runs concurrently on
OpenMP threads, and MPI ranks are load-balanced level by level along a
Hilbert curve (§4). Merged into [GAMER](/software/gamer.md),
[constrained transport](/methods/constrained-transport.md),
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md) and
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Equations** (§2, eqs. 1–9). Ideal MHD only, conservative form, ideal-gas
   equation of state, units with the magnetic pressure $\tfrac12 B^2$;
   total pressure $P^* = p + \tfrac12 B^2$ and electric field
   $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$. The paper does not
   use self-gravity, radiation, resistivity or relativity. Cartesian grids
   with cubic cells on every level (§3.1).
2. **Constrained transport** (§3.1, eqs. 10–16, Fig. 1). $u$ is
   volume-averaged at cell centres, $\mathbf B$ area-averaged on faces and
   $\boldsymbol{\mathcal E}$ line- and time-averaged on edges. The CT update
   (eq. 13) preserves the discrete divergence (eq. 16) exactly. The ghost
   zone is one cell wider than in pure hydro.
3. **CTU+CT** (§3.2), 8 steps: reconstruct, Riemann solve, edge EMF,
   $\Delta t/2$ CT and conservative update, transverse-flux-gradient
   correction of the interface states, second Riemann solve, second edge
   EMF from the half-step $\mathbf B$ and velocity, full update. **VL+CT**,
   7 steps (MUSCL-Hancock): first-order fluxes, edge EMF, $\Delta t/2$
   predictor, reconstruction, Riemann solve, edge EMF, full update. Both
   are stated second order in space and time. CTU "is generally less
   diffusive" because of the transverse correction, so it is used for all
   accuracy tests.
4. **Edge EMF** (§3.2, CTU step 3). It is built from the interface
   electric field, the interface $\mathbf B$ and the cell-centre velocity.
   The averaging variant is not named, and Gardiner & Stone (2005, 2008) is
   not cited. Whether reconstruction uses primitive or characteristic
   variables is not stated.
5. **AMR** (§3.3). Octree of patches of $N_{\mathrm b}^3$ cells
   ($N_{\mathrm b} = 8$ in the captions of Figs. 9 and 11), $r_{\mathrm{ref}} = 2$.
   Restriction by volume averages (cell data) and area averages (face
   $\mathbf B$). Refluxing corrects the coarse conserved variables, and the
   coarse-fine edge EMF difference corrects the coarse face $\mathbf B$.
   Prolongation: conservative interpolation for $u$ (order not stated);
   Balsara (2001) divergence-free reconstruction for $\mathbf B$ (eq. 17,
   Fig. 2), 10 coefficients fixed by 7 independent face-matching equations
   plus 3 from the vanishing divergence. Level order: update $l$, evolve
   $l+1$ until synchronized, correct $l$, (de)refine $l+1$. Levels are
   subcycled ("higher levels can have smaller time-steps"). A 2:1 nesting
   rule is not stated.
6. **GPU design** (§4, Fig. 3). Eight patches form a patch group of
   $(2N_{\mathrm b})^3$ cells, computed by one CUDA thread block. All data
   live in host memory, and only a few hundred patch groups are sent to the
   GPU at a time. CUDA streams overlap transfers with kernels. The CPU
   preparation (gather patches, fill ghost zones) and closing (scatter
   results) steps run concurrently with the GPU on OpenMP threads, and AMR
   operations stay on the CPU. MPI decomposition follows a Hilbert curve
   computed per level.
7. **Single-device performance** (§5.2, Fig. 18). VL + PLM + Roe on a
   uniform grid, Tesla P100: about $1.2\times10^8$ cell updates per second
   in single precision and $5.5\times10^7$ in double, saturating beyond about
   $2\times10^6$ cells. On a 14-core Intel Xeon E5-2680 in double precision,
   GAMER-CPU saturates at about $5.0\times10^6$ and Athena++ reaches
   $7.7\times10^6$, 1.5 times faster, "likely due to the more optimized
   implementation of vectorization". Footnote 1 quotes Athena++ on Intel KNL
   at $5\times10^7$ (single) and $3\times10^7$ (double) cells per second
   (J. Stone, private communication).
8. **Scaling** (§5.2, Figs. 19–22). Blue Waters XK nodes (one 16-core
   Opteron 6276 and one Tesla K20X each), CTU + PPM + Roe, single
   precision, AMR. Strong scaling 64 to 2048 nodes: $1.5\times10^{10}$ cell
   updates per second at 2048 nodes; 70% parallel efficiency and 57%
   "doubling efficiency" $T(M/2)/T(M) - 1$ at $10^3$ nodes; AMR operations
   about 9% and MPI about 6% of the time at 64 nodes. Weak scaling 1 to 4096
   nodes: $5\times10^{10}$ cell updates per second at 4096 nodes; 70%
   efficiency at $10^3$ nodes updating $2\times10^{11}$ cells (text) and 85%
   at 512 nodes (Fig. 22 caption); AMR performance about equal to the
   uniform grid. The proposed remedy for the growing MPI share is
   non-blocking communication overlapped with computation (§6).

**Tests** (§5.1, all $\gamma = 5/3$, Courant number $\nu = 1/2$):
[linear waves](/benchmarks/linear-wave-convergence.md) (slow, Alfvén and
fast along the 3D box diagonal, amplitude $10^{-6}$, PLM + Roe, double
precision: all errors $\propto N^{-2}$, Fig. 4); RJ2a and Torrilhon shock
tubes (512 cells, PPM + Roe; the Torrilhon spurious compound wave vanishes
with resolution, $L_1$ error $\propto N^{-3/4}$ over $2^9$ to $2^{18}$ cells,
Fig. 8); the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) with
AMR ($256^2$ base plus 3 levels, refined on $\vert\mathbf J\vert/\vert\mathbf B\vert$,
compared with $1024^2$ uniform, Figs. 9–10); a 3D
[MHD blast wave](/benchmarks/mhd-blast-wave.md) ($512^3$ uniform against
$256^3$ plus 3 levels, Figs. 11–14); and a new ABC force-free field
relaxation test, total energy conserved to machine precision and magnetic
helicity above 98%, also used as the scaling problem (Figs. 15–17).

# Notation map

| Zhang et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf V$, $\mathbf M = \rho\mathbf V$ | $\mathbf v$, $\rho\mathbf v$ | |
| $P$ | $p$ | gas pressure |
| $P^*$ | $P^*$ | total pressure |
| $e$ | $E$ | **collision:** the paper's $e$ is the total energy density; registry $e$ is specific internal energy |
| $\mathbf E$ | $\boldsymbol{\mathcal E}$ | **collision:** registry $E$ is the total energy density |
| $\mathbf B$ | $\mathbf B$ | units with $\mu = 1$; Table 1 values carry $(4\pi)^{-1/2}$ |
| $\mathbf J$ | $\mathbf J$ | refinement criterion $\vert\mathbf J\vert/\vert\mathbf B\vert$ |
| $U$, $F_x$, $F^{n+1/2}_{x,i-1/2,j,k}$ | $u$, $\mathbf f(u)$, $\hat f_{i-1/2}$ | |
| $\delta x$, $\Delta h(k)$ | $h$, $h_l$ | |
| $k$, $n$, $l$ (level) | $l$ | **collision:** the paper's $n$ is also the time index and the ABC mode number |
| $\delta t$, Courant safety factor | $\Delta t$, $\nu$ | |
| $N$ (cells per patch side) | $N_{\mathrm b}$ | $N$ is also the total cell count in $E_{L1}$ |
| $C_s$, $C_A$ | $c_s$, $c_A$ | |
| $\mathbf A$; $A$, $B$, $C$ | words | **collision** with $A(u)$; ABC amplitudes kept test-local |

# Pages created or updated

* Created [GAMER](/software/gamer.md).
* Updated [Constrained transport](/methods/constrained-transport.md),
  [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* Updated [Linear wave convergence](/benchmarks/linear-wave-convergence.md),
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md),
  [MHD blast wave](/benchmarks/mhd-blast-wave.md).
* Also cited on [Athena++ (block-based AMR framework for astrophysical MHD)](/software/athena-plus-plus.md), [Athena (astrophysical MHD code)](/software/athena.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2018-ApJS-Zhang-1038471538-4365aac49e.pdf`.
   * **Version.** arXiv:1804.03479v4 (21 Jun 2018), 29 pages including the
     appendix; the author preprint, not the typeset article. Code repository
     printed: `https://github.com/gamer-project/gamer`. Language, licence and
     code version are not printed (CUDA, OpenMP and MPI are named in §4).
   * **Identity.** doi:10.3847/1538-4365/aac49e, checked on Crossref (title
     and authors match page 1): Astrophys. J. Suppl. Ser. 236(2):50, June
     2018 (print 2018-06-01, online 2018-06-20).
   * **How it was read.** Text extraction, all sections and the appendix;
     eqs. 1–17 checked on the rendered page 4 and Table 1 on page 9.
     Appendix equations (A1–A21, the stability proof for the $n = 1$ ABC
     field) summarized, not reproduced. Linear-wave grid sizes and errors
     appear only in Fig. 4.
   * **Recorded as printed.** §5.2 says the per-node performance at 64
     nodes is "only about 0.82 times lower than the GPU performance", read
     here as about 82% of the single-GPU throughput. The abstract's 70% at
     1024 nodes and the Fig. 22 caption's 85% at 512 nodes refer to
     different node counts.
   * **Reference list:** 75 entries, no titles printed. Parker (1957) is
     printed with volume 4 and merged into `parker-1957` (J. Geophys. Res.
     62:509); the Balsara (2001) MNRAS paper is keyed `balsara-2001-c`;
     Taylor (1950) is keyed `taylor-1950-b`.
