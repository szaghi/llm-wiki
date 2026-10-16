---
type: Software
title: "M3D-C1-K"
description: "Kinetic-MHD hybrid built on M3D-C1: δf energetic-particle markers pushed by RK4 guiding-centre integration or a GPU-accelerated slow-manifold Boris algorithm, coupled to the implicit finite-element MHD by pressure or current coupling, which the authors derive to be equivalent; benchmarked on the linear n=1 fishbone, the ITPA n=6 TAE and the DIII-D RSAE cases."
status: established
aliases: [M3D-C^1-K]
tags: [code, hybrid-kinetic, energetic-particles, alfven-eigenmode, particles, gpu, finite-elements, benchmark]
timestamp: 2026-10-16T00:00:00Z
---

# M3D-C1-K

M3D-C1-K adds an energetic-particle (EP) module to [M3D-C1](/software/m3d-c1.md)
and so forms a [hybrid kinetic-MHD](/methods/hybrid-kinetic-mhd.md) code
([Liu et al. (2022)](/sources/liu-2022.md), Abstract, §1). Its targets are
long-time nonlinear EP physics such as chirping and kink or tearing modes with
EPs; slow-manifold Boris is named as a candidate pusher for runaway electrons
(§7). [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§I, §II) list it
with MEGA, (X)HMGC, XTOR-K and M3D-K as hybrid codes, and with HMGC and
HYMAGYC as codes that couple an explicit EP contribution to an implicit MHD
advance.

## Particle model

* **Pushers** (see [particle pushers](/methods/particle-pushers.md)):
  * RK4 integration of the drift-kinetic guiding-centre equations of M3D-K
    (Littlejohn Lagrangian, 5D phase space) (Liu et al. 2022, §2, Eqs. 1–4).
  * The slow-manifold Boris algorithm of Xiao & Qin (2021): the standard
    Boris full-orbit push applied to the Pauli particle, with the mirror force
    $-\mu\nabla B$ folded into an effective electric field. This allows steps
    longer than the gyro-period while particles stay near the slow manifold;
    one RK4 guiding-centre step initializes each marker (§2, Eqs. 5–6). The
    curvature drift comes from the Boris push itself, so only first
    derivatives of the finite-element fields are needed, whereas the RK4
    guiding-centre push needs second derivatives, which dominate its cost by
    profiling (§2).
* **Weights.** [δf](/methods/delta-f-method.md) with
  $f_0=f_0(P_\phi,\mathcal E,\mu)$; linear runs use equilibrium orbits; the
  compression correction of Belova (1997) is applied; markers are loaded by
  Monte Carlo from $f_0$ (§3, Eqs. 7–13).
* **FLR.** An optional four-point gyro-average for both field gather and
  deposition (§3, Eq. 14).
* **Moments.** $\delta p_{\parallel h}$ and $\delta p_{\perp h}$ are deposited
  by Galerkin projection onto the finite-element test functions with a
  $\delta$-function particle shape, then a mass-matrix solve; with the
  high-order polynomials this gives noisy, spiky pressures (§3, Eqs. 15–18).
  See [particle-to-mesh projection](/methods/particle-to-mesh-projection.md).

## Coupling to the MHD

Two schemes are implemented (§4; see
[pressure and current coupling](/methods/pressure-and-current-coupling.md)):
* **Pressure coupling** (M3D-K style): the momentum equation carries
  $-\nabla\cdot\mathsf P_h$ with
  $\mathsf P_h=p_{\parallel h}\mathbf b\mathbf b+p_{\perp h}(\mathsf I-\mathbf b\mathbf b)$;
  all components of $\nabla\cdot\mathsf P_h$ are kept, and the time derivative
  of the EP momentum density is dropped in all directions (Eqs. 19–21).
* **Current coupling** (MEGA style): the momentum equation carries
  $(\mathbf J-\mathbf J_h)\times\mathbf B$, with the EP current made of
  parallel, drift and magnetization parts; the $-q_hn_h\mathbf E$ term on the
  bulk is omitted because it cancels the $E\times B$ part of
  $\mathbf J_h\times\mathbf B$ (Eqs. 22–27).
* **Equivalence.** In the drift-kinetic limit $\mathbf J_h\times\mathbf B$
  equals the perpendicular part of $\nabla\cdot\mathsf P_h$ (Eq. 25), so the
  same moments serve both schemes; "for all the simulations we have
  conducted, the two coupling schemes give almost the same results" (§4,
  Figs. 3, 5). $n_h\ll n_i$ is assumed throughout.

## MHD side, time stepping and parallelism

The MHD is M3D-C1's high-order 3D finite elements with potentials, advanced
implicitly or semi-implicitly on CPUs with MPI domain decomposition; the step
is not CFL-limited (Liu et al. 2022, §1, §5). Particles are subcycled between
two MHD steps with frozen fields (§5). The push uses particle-based
parallelization (one thread per particle for several steps, no particle
migration, as in GTC), OpenACC on GPUs or OpenMP on CPUs selected at compile
time; each GPU holds the whole-mesh field, gathered with MPI-3 shared memory
inside a node; deposition is done on the CPUs (§5).

**GPU timing** (Summit, 4 nodes, DIII-D-like mesh of 4 planes × 5679
elements, 50 push steps): 134.22 s for the CPU RK4 push (8 POWER9 CPUs),
12.65 s for the GPU RK4 push (24 V100), 10.32 s for the GPU Boris push with a
4× smaller step, i.e. about 11× from porting alone. The text says 16 million
particles, the caption 4 million (§5, Fig. 2). Further GPU optimization is
judged not worthwhile because the push is already close to the CPU MHD time
(§5).

## Verification and benchmarks

All from Liu et al. (2022) unless cited otherwise.
* **Orbit conservation** (DIII-D-like static field, run to 2 s): RK4
  accumulates errors in $P_\phi$ and $\mathcal E$ (about $5.5\times10^{-3}$ and
  $-1.5\times10^{-3}$ for a passing particle), while slow-manifold Boris errors
  stay bounded (about $10^{-4}$ in $P_\phi$); the advantage matters only for
  runs beyond about 500 ms (§2, Fig. 1).
* **Linear $n=1$ fishbone** (Fu 2006 setup): growth rate and frequency agree
  with M3D-K and NIMROD "except for the mode real frequency at large
  $\beta_h/\beta_{\mathrm{total}}$"; the mode changes from ideal kink to
  fishbone as $\beta_h/\beta$ rises from 0 to 0.75 (§6.1, Fig. 3). See
  [fishbone](/definitions/fishbone.md).
* **[ITPA $n=6$ TAE](/benchmarks/itpa-tae-benchmark.md)**: "close to the
  results from gyrokinetic, hybrid-MHD and eigenvalue codes"; FLR roughly
  halves the growth rate at high $T_h$ (peak about $22\times10^3$ s$^{-1}$
  with FLR against about $42\times10^3$ s$^{-1}$ without, figure reading)
  (§6.2, Fig. 5). [Liu et al. (2024)](/sources/liu-2024.md) (§III C, Fig. 14)
  find GMEC growth rates close to M3D-C1-K's; the comparison curves are taken
  from Liu et al. (2022). See [TAE](/definitions/toroidal-alfven-eigenmode.md).
* **[DIII-D RSAE](/benchmarks/diii-d-rsae-benchmark.md)** (#159243, $n=3$–6,
  FLR): "agree well" with other initial-value MHD and gyrokinetic codes;
  largest growth at $n=4$–5, the $n=4$ mode localized at $q_{\min}$ and
  dominated by $m=12$ (§6.3, Figs. 7–8). See
  [RSAE](/definitions/reversed-shear-alfven-eigenmode.md).

## Limitations and benchmark spread

* The fishbone frequency is about 15–20 % below M3D-K and NIMROD at
  $\beta_h/\beta=0.5$–0.75 (figure reading: about 0.030 against 0.035–0.036
  in units of $\tau_A^{-1}$ at 0.75); the paper does not attribute the gap,
  though it loads EPs on local rather than orbit-averaged $\psi$ (§6.1, Fig. 3).
* RSAE growth rates at $n=5$–6 (about $2.3$ and $1.7\times10^4$ s$^{-1}$) sit
  with the lower group of codes, well below NOVA and FAR3D (figure reading,
  undiscussed) (§6.3, Fig. 7).
* $\delta$-function deposition gives noisy pressures with high-order
  polynomials (§3).
* For short-time-scale problems (GAE, CAE) the CPU MHD dominates the cost;
  MHD GPU porting is planned (§7).
* Version caveat: arXiv v1 read; the published version may differ.

# Citations

1. [Liu et al. (2022)](/sources/liu-2022.md) — §§1–7, Figs. 1–8.
2. [Liu et al. (2024)](/sources/liu-2024.md) — §III C, Fig. 14.
3. [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §I, §II.
