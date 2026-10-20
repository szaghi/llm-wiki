---
type: Software
title: "Trixi.jl"
description: "Trixi.jl is a Julia DGSEM framework for hyperbolic and hyperbolic–parabolic conservation laws whose semi-discretizations the sources integrate with OrdinaryDiffEq.jl; it supplies Jacobian spectra for stability-polynomial optimization, hosts paired explicit Runge–Kutta with AMR partitioning, is a test bed for error-based step-size control, and is the library under TrixiLW.jl."
status: established
aliases: [Trixi, Trixi.jl DGSEM]
tags: [software, multirate, step-size-control, verification]
timestamp: 2026-10-20T08:00:00Z
---

# Trixi.jl

Trixi.jl is a Julia framework for discontinuous Galerkin spectral element (DGSEM)
discretizations of hyperbolic and hyperbolic–parabolic conservation laws (compressible
Euler and Navier–Stokes, ideal and resistive GLM-MHD, linearized Euler, shallow water and
others), on tree meshes with adaptive refinement, p4est meshes and curved structured
meshes. It is a spatial code: in the sources it generates the semi-discrete system
$y'=f(t,y)$, and the time integration is done by
[OrdinaryDiffEq.jl](/software/differentialequations-jl.md) or by integrators implemented
alongside it. Four ingested sources from the group that develops it use it, and a fifth,
from another group, builds a single-stage scheme on it as a library.

## Role in the sources

- **Spectra for stability polynomials.** Trixi.jl's algorithmic differentiation gives the
  Jacobian $J$ of the DGSEM semi-discretization, whose spectrum feeds the optimization of
  stability polynomials ([Doehring et al. 2024](/sources/doehring-2024.md), spectra of the Burgers, shallow-water, MHD and isentropic-vortex test cases;
  [optimal stability polynomials](/methods/optimal-stability-polynomial.md)).
  [Doehring et al. (2024b)](/sources/doehring-2024-b.md) (§4.1) build the sparse Jacobian at
  full resolution by algorithmic differentiation and estimate the boundary of its spectrum
  with shifted Arnoldi runs (ARPACK through Arpack.jl) seeded by the convex hull of a
  reduced-resolution spectrum: about 30 s for 930 eigenvalues of a $16384\times16384$
  Kelvin–Helmholtz Jacobian, against more than 11 minutes for its full eigendecomposition.
- **Paired explicit Runge–Kutta with AMR partitioning.** The multirate
  [P-ERK](/methods/paired-explicit-runge-kutta.md) schemes of Doehring et al. (2024b, §6) and
  [Doehring et al. (2025)](/sources/doehring-2025.md) are implemented in Trixi.jl. Each cell
  is assigned to a family member by its level (TreeMesh) or its shortest edge (p4est), and
  the element, interface, boundary and mortar loops of the spatial operator are restricted
  to index sets per member, reassigned at every mesh change; mortars go to the member of
  the fine neighbour. Partitioning overhead is 0.3–4.4 % of runtime and memory overhead
  7–34 % (Doehring et al. 2024b, §7). No extra MPI communication is needed relative to a
  standard Runge–Kutta method, a statement not tested on distributed runs (§6.3).
- **Memory-bound performance.** Both P-ERK papers find runtime savings below the savings in
  right-hand-side evaluations, because the code is memory-bound and partitioning loses data
  locality: a standalone P-ERK with 76.2 % more evaluations is only 46.8 % slower
  (Doehring et al. 2024b, §7.1.1), and on a 3D linearized-Euler case only about half of the
  theoretical speedup is realized (Doehring et al. 2025, §6.2).
- **Error-based step-size control.** [Ranocha et al. (2025)](/sources/ranocha-2025.md) run
  their comparison of error-based and CFL-based [step-size control](/methods/step-size-control.md)
  in Trixi.jl with OrdinaryDiffEq.jl, and repeat it in a second, independent code (SSDC on
  [PETSc TS](/software/petsc-ts.md)). In that coupling adaptive mesh refinement and CFL
  control are callbacks after accepted steps and positivity limiters act after every stage,
  so the error estimator never sees them (§2.3–2.5, §8).

- **A single-stage scheme on top of Trixi.jl.** [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md)
  (§1, §6) implement [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)
  in TrixiLW.jl, which loads Trixi.jl through Julia's package manager and extends it by
  multiple dispatch rather than forking it. It reuses Trixi.jl's curved meshes (from
  HOHQMesh.jl), its three-level AMR controller and its postprocessing, replaces the
  method-of-lines time loop by the single-stage update, and adds an error-based step-size
  controller of the Ranocha et al. type, with the per-element error accumulated inside the
  residual loop. The design of the authors' earlier 1-D/2-D code was "inspired by Trixi.jl"
  ([Babbar et al. 2022](/sources/babbar-2022.md)), which takes its fifth-order reference
  Runge–Kutta method in the 2-D tests from [DifferentialEquations.jl](/software/differentialequations-jl.md).

## Test cases run in Trixi.jl in the bundle

[Isentropic vortex](/benchmarks/isentropic-vortex.md) with AMR,
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md),
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (3D, enstrophy-based AMR),
periodic shear layer, visco-resistive Orszag–Tang vortex, Rayleigh–Taylor instability and
the MHD rotor (Doehring et al. 2024b, §5, §7); laminar SD7003 airfoil and a coupled
Euler/acoustic-perturbation vortex pair (Doehring et al. 2025, §6); double Mach reflection,
astrophysical jet and Kelvin–Helmholtz cases (Ranocha et al. 2025, §4–6); through TrixiLW.jl,
a Mach 2000 jet, Kelvin–Helmholtz, double Mach reflection, forward-facing step, rotating
Couette flow, curvilinear isentropic vortex, Mach 3 cylinder, Mach 4 blunt body and transonic
NACA0012 (Babbar & Chandrashekar 2025, §6).

## Qualifications

- The four Trixi.jl-group sources share authors with the Trixi.jl developers; their speedups are
  measured in one code base, and Doehring et al. (2025) state no hardware for some runs.
- Trixi.jl is cited in printed reference lists under its JuliaCon 2022 proceedings paper,
  whose key collides with an ingested source; the bibliography keeps them apart (noted on
  the Source pages of Doehring et al. 2025 and Ranocha et al. 2025).

# Citations

- [Doehring et al. (2024)](/sources/doehring-2024.md) — DGSEM spectra of the Burgers, shallow-water, 1D MHD and isentropic-vortex test cases computed with Trixi.jl.
- [Doehring et al. (2024b)](/sources/doehring-2024-b.md) — §4.1, §5, §6.1–6.3 (Listings 1–2), §7 (Tables 7–12).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §6 (DGSEM validation and applications, §6.2).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §2.3–2.5 (Algorithm 2), §4–6, §8.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §1, §5.2 (Algorithms 1, 3), §6 (TrixiLW.jl on Trixi.jl).
- [Babbar et al. (2022)](/sources/babbar-2022.md) — code design inspired by Trixi.jl; RK65 from DifferentialEquations.jl in the 2-D tests.
