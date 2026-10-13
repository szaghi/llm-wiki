---
type: Source
title: "Caddy & Schneider (2024) — Cholla-MHD: An Exascale-Capable Magnetohydrodynamic Extension to the Cholla Astrophysical Simulation Code"
description: "Adds ideal MHD to the GPU-native code Cholla with the VL+CT integrator, HLLD and characteristic PLM/PPM, keeps all data GPU-resident and recomputes rather than stores derived fields, verifies on 3D wave, field-loop, Riemann, blast and Orszag–Tang tests, and weak-scales to 74,088 MI250X GCDs of Frontier at about 80 % efficiency."
resource: "doi:10.3847/1538-4357/ad464a"
source_kind: paper
authors: [Caddy R.V., Schneider E.E.]
year: 2024
venue: "Astrophys. J. 970:44"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2024-ApJ-Caddy-1038471538-4357ad464a.pdf"
tags: [software, mhd, gpu, cuda, constrained-transport, unsplit, riemann-solver, performance, scaling, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper adds ideal MHD to [Cholla](/software/cholla.md), a GPU-native,
static-Cartesian-mesh, finite-volume astrophysical code in C++/CUDA
(Schneider & Robertson 2015). The MHD uses the VL+CT integrator of Stone &
Gardiner (2009), now Cholla's default in place of CTU, the HLLD solver of
Miyoshi & Kusano (2005), and PLM or PPM (Felker & Stone 2018)
reconstruction limited in characteristic variables (§2.2). The GPU design
keeps all data resident on the GPU, recomputes the cell-centred field and
the primitive variables instead of storing them, fuses piecewise-constant
reconstruction into the Riemann kernel, chooses CUDA or HIP at compile time
through one macro header, and runs MPI directly between GPU buffers
(§2.3). The verification suite has 3D linear-wave and circularly
polarized Alfvén-wave convergence, a 3D field loop, five MHD Riemann
problems, a blast wave and an Orszag–Tang vortex (§3.1). Throughput is
about $2.4\times10^8$ cell updates per second per MI250X GCD and
$2.59\times10^8$ per A100, with weak scaling to 74,088 GCDs of Frontier
($19{,}278^3$ cells) (§3.2). The paper also documents a GoogleTest,
GitHub Actions and Jenkins testing framework (§4).

# Key claims

1. **Equations** (§2.1, eqs. 1–10). Ideal MHD, conservative form, magnetic
   permeability 1, total pressure $P^*$, ideal-gas equation of state only.
2. **VL+CT** (§2.2, steps 1–10): PCM predictor, HLLD, edge EMFs, half-step
   update of $u$ and face $\mathbf B$, PLM/PPM at the half step, HLLD, edge
   EMFs, full update, then first-order operator-split extra physics and the
   MPI ghost exchange. Chosen over CTU as "more robust".
3. **Time step** (§2.2.1, eq. 11): one global step, minimum over cells and
   directions of the cell size over $|v|+c_f$; formally $\nu \le 0.5$, in
   practice unstable at 0.5 and stable at 0.4, typically 0.3 (footnote 4).
   The global reduction runs on the GPU with an integer-encoded
   `atomicMax` (from RAPIDS cuML) and then an MPI all-reduce (§2.3.3).
4. **CT** (§2.2.4, eqs. 13–18, Fig. 1). Cell-centred $\mathbf B$ is the
   face average (eq. 13); edge EMFs follow the Gardiner–Stone upwind
   construction with a cell-centre reference $-\mathbf v\times\mathbf B$,
   upwinded by the sign of the face-normal velocity (eq. 16).
5. **Reconstruction** (§2.2.2, §2.2.6): PCM is "too diffusive" for both
   steps; characteristic PLM with the Stone et al. (2008) eigenvectors and
   the LeVeque (2002) limiter; PPM after Felker & Stone (2018) is "formally
   second order" in this integrator.
6. **Riemann solver** (§2.2.3, Table 1): HLLD only; normal field from the
   face, transverse field reconstructed from the cell-centred average.
7. **GPU design** (§2.3.1–§2.3.2). All data GPU-resident (older Cholla
   copied conserved arrays to and from the GPU each step); only conserved
   variables are stored; fusing PCM into the Riemann kernel saved about
   10 % runtime, fusing characteristic PLM cost 10–15 % through lower
   occupancy; CUDA-to-HIP macro header; GPU-direct MPI; HDF5 output from the
   CPU (footnote 5).
8. **Capacity** (§1): about $500^3$ cells per 80 GB A100, $459^3$ per
   MI250X GCD.
9. **Performance** (§3.2, Figs. 13–14): see Tests; no CPU baseline.
10. **Testing and CI** (§4): GoogleTest unit, integration and system tests;
    floating-point match by $10^{-14}$ absolute or 4 ULP; CUDA builds tested,
    HIP builds only compiled.

# Tests

All 3D, all in the automated suite (§3.1); CFL number not stated for the
accuracy tests.
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md)
  (§3.1.1, Fig. 2): grid-aligned, $N\times16\times16$, $N = 16$–512,
  $A = 10^{-6}$; second order for all four families; PPM about 10× lower
  errors than PLM.
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
  (§3.1.2, Fig. 3): $2N\times N\times N$, $N = 8$–256; second order; no PPM
  gain.
* [Field-loop advection](/benchmarks/field-loop-advection.md) (§3.1.3,
  Figs. 4–5): tilted spherical loop, $N = 32$–256; normalized magnetic
  energy at $t = 2$ about 0.97 ($N = 256$) and 0.80 ($N = 32$) read from
  Fig. 4; divergence about $10^{-17}$–$10^{-15}$; PPM oscillations, so
  Fig. 5 uses PLM.
* MHD Riemann problems (§3.1.4, Table 2, Figs. 6–10): the
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) ($\gamma = 2$,
  $t = 0.1$; PPM oscillates with primitive or characteristic limiting, PLM
  does not), Dai & Woodward (Ryu & Jones 2a), Ryu & Jones 1a and 4d,
  Einfeldt strong rarefaction; visual only.
* [MHD blast wave](/benchmarks/mhd-blast-wave.md) (§3.1.5, Fig. 11):
  $200\times300\times200$, plasma beta 0.2; unstable at beta 0.02.
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (§3.1.6,
  Fig. 12): $192^3$, $t = 0.5$; qualitative.
* Weak scaling (§3.2, Fig. 13): Frontier MI250X, one GCD per rank, double
  precision, $459^3$ cells per GCD, slow magnetosonic wave, PLM, 100 steps,
  1 to 74,088 GCDs; about 80 % efficiency (printed numbers conflict, below).
* Strong scaling (§3.2, Fig. 14): $459^3$ cells in total, about 6100 steps;
  80 % at 32 GPUs, 67.2 % at 64, above 50 % until 256, plateau near 512.
* A100 $2.59\times10^8$ and V100 $1.6\times10^8$ cell updates per
  GPU-second (abstract, §3.2); precision and problem size not stated.

# Notation map

| Caddy & Schneider (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $E$ | $\rho$, $\mathbf v$, $E$ | same |
| $P$ (eq. 12 writes $p$) | $p$ | the paper mixes $P$ and $p$ |
| $P_T = P + \tfrac12 B^2$ | $P^*$ | permeability 1; test set-ups still carry $\sqrt{4\pi}$ factors |
| $\epsilon$ (internal energy density) | $\rho e$ | registry $e$ is specific |
| $U$, $W$ | $u$, primitive variables (words) | no registry primitive-state symbol |
| $\mathbf F^n_{x,i+1/2,j,k}$ | $\hat f_{i+1/2}$ | numerical flux |
| $W_{L,i+1/2}$, $W_{R,i-1/2}$ | $u^-_{i+1/2}$, $u^+_{i-1/2}$ (primitive form) | L = minus side |
| $a$ (characteristic variables) | words | **collision:** registry $a$ is the cosmological scale factor |
| $C_{CFL}$ | $\nu$ | |
| $\Delta x$, $\Delta y$, $\Delta z$ | $h$ per direction | the paper allows unequal spacing |
| $c_f$, $c_s$ (fast, slow magnetosonic) | $c_f$; slow speed in words | **collision:** registry $c_s$ is the sound speed |
| $\mathcal E$, $\varepsilon$ (Table 1) | $\boldsymbol{\mathcal E}$ | two glyphs for the electric field |
| $\mathcal E^{ref}$ | cell-centre $\boldsymbol{\mathcal E}$ | words |
| $\mathbf A$, $A$ (vector potential; also wave amplitude) | words | **collision** with $A(u)$ and inside the paper |
| $N$ | $N$ | cells per dimension |
| $\beta$ (plasma beta); $\alpha$, $\beta$ (rotation angles) | words | **collision:** registry $\beta^i$ is the shift vector |
| $\mu_0$ | — | set to 1 |

# Pages created or updated

* Created [Cholla](/software/cholla.md),
  [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Athena](/software/athena.md),
  [Constrained transport](/methods/constrained-transport.md),
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md).
* Per the batch plan, also cited on: [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md),
  [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md),
  [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Linear wave convergence](/benchmarks/linear-wave-convergence.md),
  [Field-loop advection](/benchmarks/field-loop-advection.md),
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md),
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md),
  [MHD blast wave](/benchmarks/mhd-blast-wave.md).
* Also cited on (batch 3) [Sod shock tube](/benchmarks/sod-shock-tube.md), [Adaptive mesh refinement in astrophysical codes](/methods/adaptive-mesh-refinement.md), [GAMER (GPU-accelerated octree AMR code), MHD extension](/software/gamer.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2024-ApJ-Caddy-1038471538-4357ad464a.pdf`.
   * **Version.** arXiv:2402.05240v2 [astro-ph.GA], 1 May 2024 ("Draft
     version May 3, 2024", AASTeX631), 39 pages; a preprint or accepted
     manuscript, not the typeset article. Code: `https://github.com/cholla-hydro/cholla`
     (§5); the version used is the Zenodo record "Caddy & Schneider 2024,
     v3.x" (doi:10.5281/zenodo.10927183).
   * **Identity.** doi:10.3847/1538-4357/ad464a, checked on Crossref (same
     two authors and title): Astrophys. J. 970(1):44, print 2024-07-01,
     online 2024-07-15.
   * **How it was read.** Text extraction of all sections; the CFL passage
     checked on the rendered page 8 (the text layer's "0.44" is 0.4 plus
     footnote marker 4), eqs. 19–32 on page 11, the Orszag–Tang set-up on
     page 27. Error and timing values in Figs. 2–4, 13 and 14 are read from
     plots.
   * **Recorded as printed.**
     * Eq. 15 adds the two derivative terms per direction and eq. 17 writes
       the example derivative as face minus reference, the opposite
       arrangement to Stone et al. (2008), eq. 81; only one derivative is
       printed, so convention or misprint cannot be decided.
     * Index typos: eqs. 19 and 29 print identical $y$- and $z$-flux terms
       in each difference; eq. 22's right-hand side and both sides of
       eq. 32 carry the wrong face index; eq. 18 prints "i.j.k"; §2.2.8 says
       "Repeat step 3" for step 4.
     * Eq. 11 uses one $c_f$ for all directions and eq. 12 contains only
       the $x$-component of $\mathbf B$.
     * Orszag–Tang field amplitude printed "$B_0 = 1\sqrt{4\pi}$", ambiguous
       between $1/\sqrt{4\pi}$ and $\sqrt{4\pi}$; the velocity has the
       opposite sign to Stone et al. (2008).
     * Weak-scaling numbers: §3.2 text $2.36\times10^8$ and $1.89\times10^8$
       per GCD, total $1.40\times10^{13}$; Fig. 13 caption $2.04\times10^8$
       and $1.67\times10^8$, total $1.24\times10^{13}$; both say 82.2 %,
       §5 says 80 % and "14.0 trillion". The text values give 0.80 and the
       plotted times support about 80 %.
     * Strong scaling: "at most a ≈ 55% drop in efficiency" at
       $128^3$–$256^3$ cells per GPU is a loose bound; the measured
       67.2 % at $115^3$ is a smaller drop.
   * **Reference list:** 96 printed entries, merged complete. The
     self-citation "Caddy, R., Schneider, E., Villasenor, B., et al. 2024"
     is the Zenodo code archive, keyed `caddy-2024-b`, distinct from this
     paper. Misprints folded with notes: Brio & Wu (1988) printed with page
     40 for 400; Einfeldt et al. (1991) printed with page 213 for 273;
     Ryu & Jones (1995) printed ApJ 422:228 (Crossref 442:228); Van Leer
     printed "2006" for the 2003 AIAA paper (`vanleer-2006-b`); the printed
     Toro (2009) DOI does not resolve on Crossref. The bibliography holds
     1509 entries after this batch.
