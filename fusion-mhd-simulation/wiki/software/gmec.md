---
type: Software
title: "GMEC"
description: "Zhejiang University gyrokinetic-MHD energetic-particle code: linearized reduced MHD (models A–C) in global field-aligned coordinates with fourth-order finite differences, RK4, shifted-metric stabilization and C++20 compile-time symbolic equation generation, plus gyrokinetic δf energetic particles coupled by pressure; benchmarked against MAS on ballooning and tearing modes and against M3D-K and multi-code results on TAEs and RSAEs."
status: established
aliases: [GMEC_I, Gyro-kinetic MHD Energetic-particle Code]
tags: [code, reduced-mhd, hybrid-kinetic, energetic-particles, alfven-eigenmode, finite-differences, ballooning, tearing, benchmark]
timestamp: 2026-10-16T00:00:00Z
---

# GMEC

GMEC (Gyro-kinetic MHD Energetic-particle Code) is a hybrid kinetic-MHD
initial-value code for energetic-particle (EP) driven Alfvén instabilities
in burning plasmas, developed by Fu's group at Zhejiang University. Part I
presents the MHD-only foundation, GMEC_I
([Jiang et al. (2024)](/sources/jiang-2024.md), §I); Part II adds the
gyrokinetic particle solver and the EP–MHD coupling
([Liu et al. (2024)](/sources/liu-2024.md), §I). See
[hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md).

## Physics models

* **Reduced MHD, linearized, no equilibrium flow** (Jiang et al. 2024, §II;
  see [reduced MHD](/methods/reduced-mhd.md)):
  * Model A: zero-$\beta$ vorticity equation and parallel Ohm's law with
    resistivity, Strauss's model plus a resistive term (Eqs. 1–5).
  * Model B: finite $\beta$ with a pressure equation in the slow-sound
    approximation, keeping the compressibility of the $E\times B$ flow (Eqs.
    6–8).
  * Model C: adds ion diamagnetic drift through gyroviscous cancellation and
    isothermal-electron pressure terms in Ohm's law (Eqs. 9–12).
  The vorticity is
  $\varpi=\nabla\cdot(v_A^{-2}\nabla_\perp\delta\Phi)$, with $\delta\Phi$ the
  perturbed electrostatic potential and $\delta A_\parallel$ the perturbed
  parallel vector potential.
* **Energetic particles** (Liu et al. 2024, §II): gyrokinetic guiding-centre
  equations of M3D-K pushed by RK4, [δf](/methods/delta-f-method.md) weights
  with $P_\phi$ approximated by its flux term, a four-point gyro-average
  adapted from GTC to non-orthogonal field-aligned coordinates, and
  [pressure coupling](/methods/pressure-and-current-coupling.md): the EP
  pressure perturbation enters the curvature term of the model-B vorticity
  equation (Eqs. 1, 5–22). Electrons and thermal ions are fluid; nonlinear
  fluid terms are omitted; "particle nonlinearity is included fully" (§II A).

## Coordinates and discretization

* **Field-aligned coordinates** $x$ (radial flux label), $y$ (poloidal
  angle), $z$ (toroidal angle minus the integrated field-line pitch), built on
  Boozer coordinates in Part I and PEST straight-field-line coordinates in Part
  II, with the twist-shift condition at the $y$ boundary. The domain is
  global: field lines cover whole flux surfaces, unlike flux tubes (Jiang et
  al. 2024, §III; Liu et al. 2024, §II B). See
  [field-aligned coordinates](/methods/field-aligned-coordinates.md).
* **Boundary instability and its cures.** The integrated shear is not
  periodic, so the radial basis vector is discontinuous at the twist-shift
  boundary and drives a numerical instability (growth $0.21\,v_A/R_0$ for an
  $n=20$ ballooning case). A vorticity diffusion large enough to suppress it
  biases the physical growth rate low by 7 %; Scott's shifted metric, or the
  new "simple shifted metric" whose local toroidal coordinate is the Boozer
  angle, removes it without bias, both giving $0.087\,v_A/R_0$ (Jiang et al.
  2024, §III, §VIII, Figs. 10–12). The simple shifted metric lets a PIC
  module push particles on the field grid without field-to-particle
  interpolation, at the price of a non-zero radial–binormal metric element
  (§III C). Part II instead uses a vorticity dissipation of $10^{-6}$
  (normalized), stated to "affect little" the results (Liu et al. 2024, §II A,
  App. C).
* Arbitrary-order finite differences in all three directions, five-point
  stencils by default, biased near boundaries; all equilibrium derivatives are
  precomputed and stored (Jiang et al. 2024, §IV B). Ideal-conductor radial
  boundaries (§IV C).
* **Symbolic generation.** A C++20 metaprogramming "Compile-time Symbolic
  Solver" expands the vector equations into components, applies the stencils,
  assembles the implicit and Poisson matrices and merges coefficients, which
  makes the parallel-current evaluation 6× faster at `-O2`; schemes and
  boundary conditions are template parameters, so changes require recompiling
  (Jiang et al. 2024, §V, §VII). See
  [symbolic code generation](/methods/symbolic-code-generation.md).

## Time integration, solvers and parallelism

* Explicit RK4; the resistive and numerical-diffusion terms are implicit
  (Jiang et al. 2024, §IV D). In Part II, RK4 for both MHD and particles with
  $\Delta t\approx0.01\,\tau_A$; RK4 is unstable for $\Delta t/\tau_A\ge0.04$
  (Liu et al. 2024, §II C, App. C).
* The potential comes from a 2D Poisson problem in $(x,z)$, obtained by
  dropping parallel derivatives (an $O(k_\parallel/k_\perp)$ error), solved by
  PARDISO with Intel TBB (Jiang et al. 2024, §IV; Liu et al. 2024, §II B).
* MPI domain decomposition in $y$ only, with Intel TBB inside a node; CPU
  only. Strong scaling reaches about 60 % at 1792 cores (Part I, $1024\times256\times64$)
  and about 63 % at 896 cores (Part II, $256\times64\times16$, $5\times10^6$
  markers), weak scaling 0.97–1.0 (Jiang et al. 2024, §IV E; Liu et al. 2024,
  App. B). Gyro-averaging dominates the particle cost: $2\times10^4$ steps take
  about 0.4 h with drift-kinetic and 3.2 h with gyrokinetic EPs on 896 cores
  (Liu et al. 2024, §III B, Table I).
* Equilibria come from analytic circular models, [VMEC](/software/vmec.md)
  (converted to Boozer coordinates) or [DESC](/software/desc.md) (Jiang et al.
  2024, §VI C; Liu et al. 2024, §II D).

## Verification and benchmarks

* **MAS eigenvalue code** (Jiang et al. 2024, §IX; see
  [linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md)):
  * ideal [ballooning modes](/definitions/ballooning-mode.md), $n=4$–20 and a
    pressure scan through second stability: growth rates within 4 %
    (Fig. 18); the $n=20$ case costs 17 s on 448 cores;
  * drift-ballooning modes (model C): frequency within 1 %, growth rate within
    20 % (Fig. 23);
  * 2/1 [tearing mode](/definitions/tearing-mode.md) ($R=10$ m, $a=1$ m, DESC
    equilibrium): both codes follow $\gamma\propto\eta^{3/5}$ below
    $\eta=10^{-6}\,\Omega$ m (Fig. 28).
* **Particle orbits** against analytic formulas to second order in the
  inverse aspect ratio and against FP3D;
  $\mathcal E$ and $P_\phi$ conserved to better than $10^{-7}$ over
  $10^4\,\tau_A$; resonant-island width slope $1.14\times10^{-3}$ against the
  analytic $1.26\times10^{-3}$ (Liu et al. 2024, §III A, Fig. 7).
* **$n=3$ TAE** (here and below $\tau_A=R_0/v_A$ on axis): good agreement with M3D-K over a $\beta_h$ scan;
  $\omega\tau_A=0.261$, $\gamma\tau_A=0.039$ at $\beta_h=0.02$ (Liu et
  al. 2024, §III B, Figs. 8, 11).
* **[ITPA $n=6$ TAE](/benchmarks/itpa-tae-benchmark.md)**: at $T_h=400$ keV
  without FLR, $\omega\tau_A=0.279$, $\gamma\tau_A=0.027$; growth rates
  close to the other codes and M3D-C1-K, FLR roughly halving them (Liu et al.
  2024, §III C, Fig. 14). See [TAE](/definitions/toroidal-alfven-eigenmode.md).
* **[DIII-D RSAE](/benchmarks/diii-d-rsae-benchmark.md)**: $n=4$ mode at
  $\omega\tau_A=0.093$, $\gamma\tau_A=0.0046$, localized at $q_{\min}$
  with $m=12$ dominant; $n=3$–6 dispersion close to the multi-code results,
  peak at $n=5$ (§III D, Figs. 15–17). See
  [RSAE](/definitions/reversed-shear-alfven-eigenmode.md).

## Limitations

* Only linear fluid physics so far, with a single-$n$ filter in the hybrid
  runs; fluid nonlinearity and thermal-ion kinetics are deferred (Jiang et
  al. 2024, §II; Liu et al. 2024, §I, §IV).
* The production dissipation $10^{-6}$ lies one decade below the value at
  which the TAE frequency visibly drops (Liu et al. 2024, App. C, Fig. 21).
* The comparison curves of the ITPA and RSAE benchmarks are copied from Liu et
  al. (2022), not from the original benchmark papers (Liu et al. 2024,
  §III C–D).

# Citations

1. [Jiang et al. (2024)](/sources/jiang-2024.md) — §§I–IX, Figs. 6–28.
2. [Liu et al. (2024)](/sources/liu-2024.md) — §§I–IV, App. B–C, Table I.
