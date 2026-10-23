---
type: Software
title: "DifferentialEquations.jl"
description: "DifferentialEquations.jl (OrdinaryDiffEq.jl), the Julia/SciML integrator suite as it appears in the sources: host of the Rosenbrock Rodas family and Rodas5P, of optimized low-storage pairs with PID control, its benchmarking tools, and its reported scope limits."
status: established
aliases: [OrdinaryDiffEq.jl, DiffEqDevTools.jl, SciMLBenchmarks.jl]
tags: [software, stiff, step-size-control, runge-kutta]
timestamp: 2026-10-19T11:55:00Z
---

# DifferentialEquations.jl

DifferentialEquations.jl is the Julia suite of differential-equation
solvers of the SciML organization (Rackauckas–Nie, as cited by the
sources); its ODE integrators live in the package OrdinaryDiffEq.jl. No
source of this bundle is a software paper about it: the sources use it
as the host in which new methods are implemented and benchmarked, and
this page records what they report. Two of them contribute methods to it:
[Steinebach (2023)](/sources/steinebach-2023.md) (Rosenbrock methods) and
[Ranocha et al. (2022)](/sources/ranocha-2022.md) (explicit low-storage
pairs and step-size controllers).

## Rosenbrock methods and Rodas5P

Steinebach (2023) describes the [Rosenbrock–Wanner](/methods/rosenbrock-wanner-method.md)
methods of the Rodas family available in the package for stiff ODEs and
index-1 DAEs $My'=f(t,y)$: Rodas3, Rodas4, Rodas4P, Rodas4P2 and Rodas5,
with ROS3P; Ros3prl2, Rodas4PR2 and ROS3PL were not in the package at the
time (§1–§2). He states that Rodas5 is widely used there (§1), and that
its original literature gives no dense output, so the package
interpolated Rodas5 with Hermite polynomials, which apply only to ODE
problems (§1, p. 4).

His new method [Rodas5P](/methods/rodas5p.md) and a new order-4 dense
output for both Rodas5 and Rodas5P are implemented in OrdinaryDiffEq.jl,
and the coefficients are published only there: "All coefficients of the
methods can be found there in particular" (§3, p. 12). He recommends
Rodas5P "as a standard method for stiff problems and index-1 DAEs for
medium to high accuracy requirements" in the package (§5). He also
argues that automatic differentiation, available in the package, makes
the per-step Jacobian of Rosenbrock methods "more and more obsolete" as
a drawback (abstract, §1). See [dense output](/methods/dense-output.md)
and [order reduction](/definitions/order-reduction.md) for what the new
coefficients fix.

**Benchmarking tools.** Steinebach's work–precision diagrams are made
with DiffEqDevTools.jl (`WorkPrecisionSet`), measuring the $l_2$ error
over all steps and the $L_2$ error at 100 interpolated points, with a
Rodas4P2 reference at $\mathrm{rtol}=\mathrm{atol}=10^{-14}$; the
pollution problem is taken from SciMLBenchmarks.jl (§4). No hardware is
stated for the timings. The free coefficients of Rodas5P were fixed by
nonlinear least squares with Nelder–Mead from Optim.jl (§3, step 9).

## Explicit pairs and step-size control

Ranocha et al. (2022) contribute to DifferentialEquations.jl their new
low-storage embedded pairs RK3(2)5[3S\*$_+$], RK4(3)9[3S\*$_+$],
RK5(4)10[3S\*$_+$] and their FSAL variants, with optimized PID controller
parameters, and they implemented the PID controller there (§2.2, §6).
Their coefficients were refined in extended precision with Julia and
Optim.jl so that the order conditions hold at least to quadruple
precision (§6). The production runs of that paper, however, use
[PETSc TS](/software/petsc-ts.md), not Julia. See
[low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
and [step-size control](/methods/step-size-control.md).

[Ranocha et al. (2025)](/sources/ranocha-2025.md) run these methods in OrdinaryDiffEq.jl
coupled to the DG code Trixi.jl and document the implementation (§2.3–2.5, Algorithm 2):

- names: `BS3()`, `RDPK3SpFSAL35()`, `RDPK3SpFSAL49()` (the fourth-order nine-stage pair; the
  "3" in the name does not denote its order) and `SSPRK43()`;
- the error norm is scaled with the old solution $y_n$ (PETSc uses $\hat y_{n+1}$) and floored
  at about $2.2\times10^{-16}$; the arctan limiter and the acceptance test on the limited
  step factor are the defaults; the last step is clipped to the final time, and a time within
  100 units in the last place of it is snapped onto it;
- adaptive mesh refinement and CFL-based step control are callbacks executed after accepted
  steps, and positivity limiters act after every stage; callbacks are invisible to the error
  estimator (§8).

[Doehring et al. (2025)](/sources/doehring-2025.md) take all the optimized fourth-order
comparison methods of their paired-explicit study from OrdinaryDiffEq.jl (§6).

**Relaxation.** [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) describe the package as
combining [relaxation](/methods/relaxation-runge-kutta.md) with FSAL pairs "naively": the
accepted step is relaxed after error control, so the next step's first stage must be
re-evaluated, one extra right-hand-side evaluation per step (§1). Their FSAL-R and R-FSAL
variants avoid it and were verified against the package's schemes; the relaxation parameter
is computed with Algorithm 748 of Alefeld, Potra and Shi from Roots.jl (§2–3; see
[embedded pairs](/methods/embedded-runge-kutta-pair.md)).

## Related Julia packages

[BSeries.jl and RootedTrees.jl](/software/bseries-jl.md) analyse
Runge–Kutta and Rosenbrock methods symbolically; RootedTrees.jl is part
of SciML. [Zhang (2024)](/sources/zhang-2024.md) built his
search for high-order explicit methods on his own Julia package RungeKuttaToolKit (RKTK) and
the extended-precision library MultiFloats.jl, outside SciML (§3–4; see
[order conditions](/results/runge-kutta-order-conditions.md)). Ketcheson and Ranocha state, citing others, that Julia "can be
at least as fast as" Fortran, C or C++ ([Ketcheson and Ranocha (2023)](/sources/ketcheson-2023.md), §4).

## Scope as reported

Reynolds et al. (2023) state that, among PETSc/TS, Trilinos/Tempus and
DifferentialEquations.jl, only PETSc supported multirate methods
([Reynolds et al. (2023)](/sources/reynolds-2023.md), §1). The statement
is dated to the preprint (2022) and is not contradicted by the other
sources, which do not discuss multirate support.

## Qualifications

- Feature lists here are those named in the sources (2022–2023); they
  are not an inventory of the package.
- Steinebach's recommendation of Rodas5P is a family-level, benchmark-based
  judgement: on index-1 DAEs its errors are about 3–4× larger than
  Rodas5's at equal steps, and on the transistor amplifier "Rodas5P
  cannot beat Rodas5" (Steinebach 2023, Table 5, §4).

# Citations

- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Rodas family, Hermite interpolation), §3 (implementation in OrdinaryDiffEq.jl, Optim.jl), §4 (DiffEqDevTools.jl, SciMLBenchmarks.jl), §5.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2.2 (PID controller implemented in DifferentialEquations.jl), §6 (new pairs contributed; extended-precision refinement).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1 (multirate support among libraries).
- [Ketcheson and Ranocha (2023)](/sources/ketcheson-2023.md) — §1, §4 (RootedTrees.jl in SciML; Julia performance claim).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §2.3–2.5 (Algorithm 2, OrdinaryDiffEq.jl names and defaults), §8.
- [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) — §1 (naive relaxation with FSAL), §3 (implementation, Roots.jl).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §6 (comparison methods).
- [Zhang (2024)](/sources/zhang-2024.md) — §3–4 (RKTK, MultiFloats.jl).
