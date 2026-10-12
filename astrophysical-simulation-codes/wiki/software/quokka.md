---
type: Software
title: "Quokka"
description: "GPU-native block-structured AMR radiation hydrodynamics code on AMReX: method-of-lines RK2-SSP hydrodynamics with PPM and HLLC, gray two-moment radiation with a reduced speed of light, a pluggable local Eddington-factor closure and HLL fluxes, explicit radiation subcycled per level, and a local Newton–Raphson matter–radiation exchange."
status: established
aliases: [QUOKKA, quokka-code]
tags: [software, radiation, reduced-speed-of-light, amr, gpu, hydro, riemann-solver, time-integration, performance, scaling, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Quokka

Quokka is a two-moment radiation hydrodynamics code with subcycled,
block-structured AMR, written for GPUs from the start
([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §1.2). The
authors call it the first code with two-moment AMR radiation
hydrodynamics on GPUs (§1.2). The design choice, explicit radiation
transport under a [reduced speed of light](/definitions/reduced-speed-of-light.md)
rather than implicit radiation, is argued from GPU arithmetic intensity,
simple memory access and control flow, and the absence of global
communication (§1.2, §2.2.2).

## Code

* Built on AMReX through its lower-level `AMRCore` interface, which
  supplies grid generation, coarse–fine interpolation, domain
  decomposition and parallel communication; Quokka itself does the time
  stepping and the refinement criteria (§2.2). AMReX 21.09 is cited.
* Public on GitHub (§1.2, Data Availability); the URL is a hyperlink only
  (`https://github.com/BenWibking/quokka-code`) and no version or release
  is named. Licence and language are not printed; the build uses NVIDIA
  `nvcc` (§3.1.9).
* The paper does not describe the GPU programming model beyond AMReX, the
  data layout, memory management, host–device transfers or the I/O
  format. Stated: one MPI rank per GPU, and CUDA-aware MPI did not improve
  performance (§4.1).

## Equations

Inviscid, non-relativistic, gray radiation hydrodynamics in local
thermodynamic equilibrium, in the mixed frame, without scattering; the
radiation four-force is kept to first order in $\vert\mathbf v\vert/c$
(§2.1, eqs. 2–17). With $\hat c$ the reduced speed of light (eqs. 11–17,
read from the rendered page):
$$\begin{aligned}
\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v + p\mathsf I) &= \rho\kappa_{\mathrm F}\mathbf F_{\mathrm r}/c,\\
\partial_t E + \nabla\cdot[(E+p)\mathbf v] &= -c\rho\left(\kappa_{\mathrm P}a_{\mathrm r}T^4 - \kappa_{\mathrm E}E_{\mathrm r}\right) - \rho\kappa_{\mathrm F}\frac{\mathbf v}{c}\cdot\mathbf F_{\mathrm r},\\
\partial_t E_{\mathrm r} + \nabla\cdot\left(\frac{\hat c}{c}\mathbf F_{\mathrm r}\right) &= \hat c\rho\left(\kappa_{\mathrm P}a_{\mathrm r}T^4 - \kappa_{\mathrm E}E_{\mathrm r}\right) + \rho\kappa_{\mathrm F}\frac{\hat c}{c}\frac{\mathbf v}{c}\cdot\mathbf F_{\mathrm r},\\
\partial_t\mathbf F_{\mathrm r} + \nabla\cdot\left(c\hat c\,\mathsf P_{\mathrm r}\right) &= -\hat c\rho\kappa_{\mathrm F}\mathbf F_{\mathrm r},
\end{aligned}$$
where $a_{\mathrm r}$ is the radiation constant and $\kappa_{\mathrm P}$,
$\kappa_{\mathrm E}$, $\kappa_{\mathrm F}$ are the Planck-, energy- and
flux-mean opacities.
* The two four-force terms beyond the flux term (the "relativistic work
  term") are dropped, because they matter only where velocity over light
  speed times optical depth is of order one or more, a regime where the
  reduced speed of light cannot be used (§2.1).
* $\kappa_{\mathrm F}$ is approximated by the Rosseland mean and
  $\kappa_{\mathrm E}$ by the Planck mean, flagged as an extra
  approximation (§2.1).
* With $\hat c \neq c$ the system conserves neither total energy nor
  momentum (§2.1, citing [Skinner & Ostriker (2013)](/sources/skinner-2013.md)).

## Operator splitting

Each hydrodynamic step is (i) one explicit hydro update, (ii) a set of
subcycled explicit radiation-transport updates, and (iii) a purely local
implicit matter–radiation coupling update, run once per radiation
subcycle (§2.2, §2.2.3).

## Hydrodynamics solver

From [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1.
* **Time integration.** Method of lines with RK2-SSP; see
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
  A stability-polynomial analysis gives a signal speed equal to the
  maximum over cells of the sum over directions of directional velocity
  plus $c_s$ (eq. 19); because that bound is only necessary, Quokka uses
  $d\max(\vert\mathbf v\vert + c_s)$ (eq. 20), so
  $$\Delta t = \nu\,\frac{h}{\max(\vert\mathbf v\vert + c_s)},$$
  and the paper defines its CFL number $\nu$ as a stability coefficient
  divided by $d$ (eq. 21). For forward Euler and RK2-SSP on linear
  constant-coefficient systems that coefficient is 1, so the maximum
  stable CFL number in 3D is $1/3$. Using $\max(\vert\mathbf v\vert + c_s)$
  without the factor $d$ can violate the eq. 19 bound (footnote 3). A
  Quokka CFL number is therefore not on the same scale as one defined on a
  per-direction minimum.
* **Stability.** The method of lines with higher-order reconstruction is
  not stable with forward Euler but is stable under eq. 21 with
  Runge–Kutta of order at least 2, the same finding as
  [Stone et al. (2020)](/sources/stone-2020.md) for
  [Athena++](/software/athena-plus-plus.md); single-step
  characteristic-tracing PPM does not have the problem. The method of
  lines takes a step formally smaller than CTU by $1/d$, which the authors
  accept as more robust, citing CTU instability in supersonic turbulence
  with strong cooling unless the CFL number is below about 0.1 (Schneider
  & Robertson 2017).
* **Reconstruction.** PPM (Colella & Woodward 1984) on primitive
  variables, with the interface value at $x_{i+1/2}$ equal to $7/12$ of the
  sum of the values in cells $i$ and $i+1$ minus $1/12$ of the sum of the
  values in cells $i-1$ and $i+2$, regrouped symmetrically about the
  interface for exact floating-point symmetry (eq. 22, after Stone et al.
  2020). No Colella–Woodward slope limiting or contact
  steepening: interface states are clipped to the range of the cell and
  its two neighbours, then the Colella–Woodward overshoot correction is
  applied, and at extrema the reconstruction reverts to linear rather than
  constant. Formally second order; fourth-order PPM is rejected because it
  prevents per-cell local source evaluation (footnote 4). PLM with the MC
  limiter is a compile-time option.
* **Shock flattening.** Colella–Woodward flattening is insufficient in
  multiple dimensions; Quokka uses the multidimensional flattening of
  Miller & Colella (2002) and no artificial viscosity. Flattening is
  "essential" in the stationary shock tube, LeBlanc, slow-shock and
  radiative-shock tests (§§3.1.3, 3.1.4, 3.1.6, 3.3.3).
* **Riemann solver.** HLLC with wave speeds and intermediate states from
  the primitive-variable Riemann solver (Toro 2013); the face-average flux
  is taken as the face-centred flux (second order). The HLLC carbuncle is
  acknowledged and not yet fixed; the planned fix is an adaptive switch to
  HLL perpendicular to strong shocks. See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

## Radiation solver

From [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.2; see
[M1 radiation transport](/methods/m1-radiation-transport.md).
* **Closure.** Local variable Eddington tensor; Levermore (1984) by
  default, the same algebraic form as the M1 closure,
  $\mathsf f_{\mathrm E} = \frac{1-\chi_{\mathrm E}}{2}\mathsf I + \frac{3\chi_{\mathrm E}-1}{2}\hat{\mathbf n}\hat{\mathbf n}$,
  $\chi_{\mathrm E} = \frac{3+4f_{\mathrm r}^2}{5+2\sqrt{4-3f_{\mathrm r}^2}}$
  (eqs. 23–25), with the direction term dropped at zero flux. Minerbo
  (1978) is also provided, and any map from $f_{\mathrm r}$ to
  $\chi_{\mathrm E}$ can be plugged in "at no cost in computational
  performance". Non-local Eddington tensors are left to future work.
* **Reconstruction.** PPM (or PLM) on $E_{\mathrm r}$ and on the reduced
  flux vector $\mathbf F_{\mathrm r}/(cE_{\mathrm r})$, without flattening.
  Reconstructing the reduced flux suppresses $\vert\mathbf F_{\mathrm r}\vert > cE_{\mathrm r}$
  in 1D but not in multiple dimensions; for the closure only, the flux is
  rescaled to $\vert\mathbf F_{\mathrm r}\vert = cE_{\mathrm r}$ when
  exceeded. PLM is needed for optically thin fronts not aligned with the
  grid.
* **Flux.** HLL with wave speeds computed with the Eddington factors
  frozen at the start of the step (Balsara 1999), so the closure can be
  swapped without changing the solver; the authors contrast this with
  solvers "restricted to a single local closure" (González et al. 2007;
  [Skinner & Ostriker (2013)](/sources/skinner-2013.md); Skinner et al.
  2019).
* **Optically thick correction.** A correction of the Riemann solver of
  the Audit et al. (2002) type is disabled in cells where it would produce
  a causality-violating state; the authors recommend refining on the
  gradient of the optical depth per cell.

## Matter–radiation coupling

From [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.3.
* **Energy exchange.** Backward Euler, single-material scheme of Howell &
  Greenough (2003) extended to $\hat c$: two residuals (gas internal energy
  and radiation energy) solved by Newton–Raphson with a $2\times2$
  Jacobian (eqs. 26–38). Convergence is tested relative to the total
  $\rho e + (c/\hat c)E_{\mathrm r}$ (plus the source); the default
  tolerance is $10^{-10}$ ("larger tolerances produce unacceptably
  inaccurate solutions"), lowered to about $10^{-15}$ for very stiff
  problems; the iteration aborts after 400 iterations.
* **Momentum.** Backward-Euler flux absorption,
  $\mathbf F_{\mathrm r}$ divided by $1 + \rho\kappa_{\mathrm F}\hat c\Delta t$
  with $\kappa_{\mathrm F}$ from the updated temperature; the gas momentum
  receives minus the flux change over $c\hat c$ (after Skinner et al. 2019).
  The radiation work is applied as the change of gas kinetic energy, added
  to the gas energy and subtracted, times $\hat c/c$, from $E_{\mathrm r}$
  (eqs. 39–43).

## Mesh and AMR

From [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §§2.2, 2.2.4;
see [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* Berger–Oliger / Berger–Colella block-structured AMR, cell-averaged on
  Cartesian grids, $r_{\mathrm{ref}} = 2$ only ("to minimize numerical
  glitches" at coarse–fine boundaries), $h_l = h_0/2^l$ and subcycled
  $\Delta t_l = \Delta t_0/2^l$.
* Linear conservative interpolation when refining, conservative average
  when derefining, and a flux-register synchronization "at the end of
  every two time steps on level $l>0$", which keeps conservation to
  machine precision.
* **Radiation subcycling across levels.** The coarse step is chosen so
  that the radiation substeps per level step are at most a set maximum,
  and the coarse–fine radiation flux mismatch is added to the adjacent
  coarse cells at the end of each level advance. A maximum of one
  reproduces the flux synchronization of
  [RAMSES-RT](/software/ramses-rt.md); the default, used in all tests, is
  10; too large a value can break positivity of $E_{\mathrm r}$ or flux
  causality on the coarse level.
* Grid sizes are set by AMReX `blocking_factor` and `max_grid_size`
  (128 and 128 in the uniform-grid runs, 32 and 128 in the AMR run, §4).

## Parallelization and performance

All numbers are from [Wibking & Krumholz (2022)](/sources/wibking-2022.md),
§4, on Gadi (NCI) `gpuvolta` nodes with 4 NVIDIA Tesla V100-SXM2-32GB per
node (NVLink 2.0) unless stated. Precision is not stated. The metric is
millions of cell updates per GPU per wall-clock second, with one MPI rank
per GPU.
* **Hydro weak scaling** (3D periodic Sedov blast, $256^3$ cells per GPU
  in $128^3$ grids, CFL 0.25, 100 steps; Tables 1–2). PPM: 113.34 on 1
  GPU, 70.68 on 4 (the 100 % reference), 57.75 on 32 (81.70 %), 58.50 on
  256 (82.76 %). PLM: 157.75, 85.94 (100 %), 74.77 (87.00 %), 65.18
  (75.84 %). Efficiencies are relative to one 4-GPU node. The per-GPU
  drop of about 40 % from 1 to 4 GPUs is attributed (hypothesis) to
  intra-node GPU-to-GPU bandwidth; $256^3$ local grids gave only a few per
  cent more.
* **RHD weak scaling** (radiation-driven shell, 50 steps, 10 radiation
  substeps per hydro step; Table 3): 22.55, 10.32 (100 %), 7.92
  (76.75 %), 7.87 (76.19 %) on 1, 4, 32 and 256 GPUs. The drop of about
  2× from 1 to 4 GPUs is attributed to the ghost-cell exchange of every
  radiation substep.
* **Single node of 4 NVIDIA A100** ($256^3$ per GPU; Table 4): Sedov PPM
  254.05 on 1 GPU and 150.26 on 4; radiation shell 39.04 and 18.17. Ghost
  filling takes 2.00 % and 42.03 % (hydro), 3.12 % and 53.27 % (RHD) of
  the wall time on 1 and 4 GPUs; with perfect overlap the 1-to-4 GPU
  efficiency would exceed 99 % (hydro) and 96 % (RHD). The authors call
  Quokka "as far as we are aware, the fastest PPM hydrodynamics code that
  currently exists".
* **AMR strong scaling** (radiation shell, $256^3$ root plus 2 levels,
  PLM, CFL 0.3, 50 steps, `blocking_factor` 32; Table 5): 4.95, 4.30,
  3.26 and 2.61 per GPU on 4, 8, 16 and 32 GPUs, i.e. 100 %, 86.70 %,
  65.83 % and 52.69 % efficiency (speed-up 4.21× on 32 against 4).
  Single-node per-GPU AMR performance is about 50 % below the uniform
  grid; the loss is attributed to fewer than $256^3$ cells per GPU per
  level and to sequential level-by-level stepping. Guidance: keep at
  least $256^3$ cells per GPU per level.
* **CPU comparison.** The RHD update rate per CPU core (GPU rate divided
  by the cores of a node) is "comparable to or better than" Athena++
  hydrodynamics on CPUs; no Athena++ number is printed, and the
  comparison is node-normalized, not cost-normalized (§4.1). The abstract
  and §1.2 claim that Quokka is "substantially faster than any other
  public RHD code"; the paper reports no head-to-head measurement.

## Verification

[Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3, run 9
hydrodynamic, 5 radiation and 4 radiation-hydrodynamic tests.
* **Hydrodynamics** (§3.1). [Linear sound wave](/benchmarks/linear-wave-convergence.md)
  with second-order convergence; stationary contact preserved exactly
  (HLLC); stationary and LeBlanc shock tubes, where flattening is
  essential; [Shu–Osher](/benchmarks/shu-osher-shock-tube.md) at 400 cells
  against an Athena++ reference; Jin & Liu slow-moving shock (residual
  post-shock oscillations; a characteristic-PPM fix is deferred); Einfeldt
  1-2-3 strong rarefaction; [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
  with 4 AMR levels on one GPU (peak $32{,}768^2$, about 4.5 h, no
  visible level-boundary artefacts); and the
  [Liska–Wendroff implosion](/benchmarks/liska-wendroff-implosion.md),
  exactly symmetric only with symmetric flux summation and the `nvcc`
  option `fmad=false`, because fused multiply–add contraction breaks
  source-level symmetry (§3.1.9).
* **Radiation** (§3.2). Marshak wave against the Su & Olson (1996)
  diffusion solution; Su–Olson transport problem, where regions with
  $\chi_{\mathrm E} < 1/3$ cannot be represented by any local closure;
  radiation–matter energy exchange (agreement better than one part in
  $10^5$ per step, and the reduced-speed-of-light equilibrium shift); the
  [radiation shadow test](/benchmarks/radiation-shadow-test.md); a beam
  with a transient bow-shock-like artefact at its head, attributed to the
  nonlinear local closure.
* **Radiation hydrodynamics** (§3.3). Radiation pressure tube
  (Krumholz et al. 2007), within 0.2 % of the diffusion solution;
  optically thin radiation-driven wind; the
  [subcritical radiative shock](/benchmarks/subcritical-radiative-shock.md),
  0.4 % gas-temperature L1 error; radiation-driven dust shell
  (Skinner & Ostriker 2013), with shell velocities slightly below
  thin-shell theory.
* A 3D Sedov blast serves only as the scaling workload (§4.1); see
  [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md).

## Software quality

An automated suite of 20 test problems with exact-solution checks runs on
every commit and pull request, together with SonarQube static analysis
("We have detected several bugs affecting solution correctness in other
hydrodynamics codes using this tool", footnote 5)
([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3).

## Limitations stated

* HLLC carbuncle not fixed (§2.2.1); slow-shock oscillations remain
  (§3.1.6).
* Local closures cannot represent $\chi_{\mathrm E} < 1/3$ and produce
  shadow and beam artefacts (§§3.2.2, 3.2.4, 3.2.5).
* The reduced speed of light biases closed-system equilibria (§3.2.3) and
  no constant $\hat c$ preserves the ordering of hydrodynamic, diffusion
  and light speeds everywhere (§5.1).
* Multi-GPU efficiency is limited by ghost-cell filling, and AMR
  efficiency by small per-level work per GPU (§4).

# Citations

1. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §§1.2, 2.1–2.2.4, 3.1–3.3, 4–4.2, 5.1 (arXiv v2).
2. [Stone et al. (2020)](/sources/stone-2020.md), the method-of-lines stability finding that Wibking & Krumholz (2022), §2.2.1, reproduce.
3. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), as cited by Wibking & Krumholz (2022) for energy non-conservation and the closure-specific HLL solver.
