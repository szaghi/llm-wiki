---
okf_version: "0.1"
---

# ode-integration — Knowledge Bundle

Numerical time integration of ordinary differential equations and of
method-of-lines semi-discretizations of PDEs: Runge–Kutta theory, implicit,
Rosenbrock, IMEX, additive and multirate methods, splitting, stability
notions and structure preservation, asymptotic-preserving schemes, deferred
correction and ADER, step-size control, stage solvers and integrator
software.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($h$ the step, $Y_i$ stage values, $q$ stage order and
$q_{\mathrm w}$ weak stage order, $R(z)$ the stability function, $\mathcal C$
the SSP coefficient, $\phi_k$ with the factorial normalization), and the
[update log](/log.md).

**Corpus:** chunks 1–3 of 6 ingested (60 of the archive's 118 sources). Chunk 1: two *Acta
Numerica* reviews ([Blanes et al. 2024](/sources/blanes-2024.md) on splitting,
[Jin 2022](/sources/jin-2022.md) on asymptotic-preserving schemes), the
B-series paper of [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md), three
software papers (SUNDIALS, ARKODE, Irksome) and fourteen papers on Runge–Kutta
theory and practice: weak stage order, SSP pairs and multiderivative SSP,
strong stability, stability polynomials, step-size control, Rodas5P,
fully implicit stage solvers, multirate GARK and IMEX-MRI-GARK, DeC and
ADER. Chunk 2: relaxation and entropy-stable time stepping, paired-explicit
and stabilized (Chebyshev, Legendre) methods, embedded pairs and step-size
control for compressible flow, low-storage and high-order explicit methods,
TASE operators and deferred correction. Most files are arXiv preprints; each
Source page states the version read. Chunk 3: linear multistep and BDF
methods (energy and G-stability, variable steps), IMEX-BDF and IMEX-RK for
relaxation and low-Mach problems, semi-implicit IMEX, fully implicit stage
solvers at scale, Padé and Newmark schemes, boundary data for Runge–Kutta
stages. The [bibliography](/bibliography.md) lists the works the sources cite.

## Reading guide

1. **Runge–Kutta foundations.** The [Runge–Kutta method](/definitions/runge-kutta-method.md)
   and its [order conditions](/results/runge-kutta-order-conditions.md), written
   through [B-series](/definitions/b-series.md), whose composition and substitution
   laws drive [backward error analysis](/methods/backward-error-analysis.md) and
   [processing and effective order](/methods/processing-and-effective-order.md).
   Linear stability: the [stability function](/definitions/stability-function.md),
   [A-, L- and algebraic stability](/properties/a-stability.md),
   [stiff accuracy](/properties/stiff-accuracy.md),
   [symplecticity](/properties/symplecticity.md),
   [B-convergence](/definitions/b-convergence.md).
2. **Stiffness and order reduction.** [Stage order](/definitions/stage-order.md),
   [order reduction](/definitions/order-reduction.md) and its cure through
   [weak stage order](/definitions/weak-stage-order.md) and
   [boundary conditions for the stages](/methods/runge-kutta-stage-boundary-treatment.md), with its
   [barriers](/results/weak-stage-order-barriers.md) and the schemes built on it
   ([DIRK](/methods/dirk-high-weak-stage-order.md),
   [explicit](/methods/explicit-runge-kutta-high-weak-stage-order.md)); the model problem is the
   [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md).
3. **Implicit methods and their linear algebra.**
   [DIRK/SDIRK/ESDIRK](/methods/diagonally-implicit-runge-kutta.md),
   [fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md),
   [Rosenbrock–Wanner and W-methods](/methods/rosenbrock-wanner-method.md) and
   [Rodas5P](/methods/rodas5p.md), [TASE operators](/methods/tase-operators.md),
   [Padé-based schemes](/methods/pade-time-integration.md), the [Newmark method](/methods/newmark-method.md),
   [differential-algebraic equations](/definitions/differential-algebraic-equation.md),
   and [solving the stage equations](/methods/implicit-stage-solvers.md); stiff test problems:
   [Van der Pol](/benchmarks/van-der-pol-oscillator.md), [Robertson](/benchmarks/robertson-problem.md),
   [FitzHugh–Nagumo](/benchmarks/fitzhugh-nagumo-model.md), [flow past a cylinder](/benchmarks/flow-past-cylinder.md).
4. **Nonlinear stability and structure.**
   [SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
   versus [strong stability](/properties/strong-stability.md) for linear seminegative
   problems, proved with the [energy method](/methods/runge-kutta-energy-method.md)
   ([diagonal Padé schemes](/results/diagonal-pade-strong-stability.md),
   [superviscosity stabilization](/methods/superviscosity-stabilized-runge-kutta.md));
   [positivity preservation](/properties/positivity-preservation.md);
   [multiderivative methods and the backward derivative condition](/methods/multiderivative-runge-kutta.md);
   [relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md) and
   [entropy stability](/properties/entropy-stability.md) of the fully discrete scheme,
   [pseudo-energy-preserving methods](/methods/pseudo-energy-preserving-runge-kutta.md),
   [discrete adjoints](/methods/discrete-adjoint-runge-kutta.md); test problems: the
   [Kepler problem](/benchmarks/kepler-problem.md), the
   [BBM equation](/benchmarks/benjamin-bona-mahony-equation.md), the
   [Burgers equation](/benchmarks/burgers-equation.md).
5. **Explicit methods in practice.** [Optimal stability polynomials](/methods/optimal-stability-polynomial.md),
   [stabilized Chebyshev and Legendre methods](/methods/stabilized-explicit-runge-kutta.md),
   [paired explicit (P-ERK) methods](/methods/paired-explicit-runge-kutta.md),
   [internal stability](/definitions/internal-stability.md),
   [mixed precision](/methods/mixed-precision-runge-kutta.md),
   [embedded pairs](/methods/embedded-runge-kutta-pair.md),
   [step-size control](/methods/step-size-control.md),
   [low-storage schemes](/methods/low-storage-runge-kutta.md),
   [dense output](/methods/dense-output.md); benchmarks: the
   [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and the
   [isentropic vortex](/benchmarks/isentropic-vortex.md).
6. **Additive, partitioned and multirate methods.**
   [IMEX and additive Runge–Kutta](/methods/imex-runge-kutta.md),
   [semi-implicit and linearly implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md),
   [GARK](/methods/generalized-additive-runge-kutta.md),
   [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md) and
   [IMEX-MRI-GARK](/methods/imex-mri-gark.md), [multirate GARK](/methods/multirate-gark.md),
   [multirate linear stability](/definitions/multirate-linear-stability.md) and its
   [A-stability barriers](/results/multirate-a-stability-barriers.md); test problem: the
   [Brusselator](/benchmarks/brusselator.md).
7. **Splitting and composition.** [Operator splitting](/methods/operator-splitting.md),
   [composition methods](/methods/composition-methods.md), their
   [order conditions](/results/splitting-order-conditions.md), the
   [negative-coefficient barrier](/results/negative-coefficient-barrier.md) and its escape through
   [complex coefficients](/methods/complex-coefficient-splitting.md);
   [exponential integrators](/methods/exponential-integrators.md).
8. **Multiscale problems.** [Asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md),
   [uniform accuracy for relaxation systems](/results/uniform-accuracy-relaxation-systems.md),
   [BGK penalization](/methods/bgk-penalization.md),
   [micro–macro decomposition](/methods/micro-macro-decomposition.md); test problems: the
   [linear hyperbolic relaxation system](/benchmarks/hyperbolic-relaxation-system.md), the
   [Broadwell model](/benchmarks/broadwell-model.md), the [Gresho vortex](/benchmarks/gresho-vortex.md).
9. **Linear multistep methods.** [Linear multistep methods](/methods/linear-multistep-method.md),
   [zero-stability](/definitions/zero-stability.md), the
   [BDF methods](/methods/backward-differentiation-formula.md),
   [G-stability](/properties/g-stability.md) and the
   [multiplier energy technique](/methods/multiplier-energy-technique.md) with its results on
   [BDF6](/results/bdf6-energy-stability.md) and
   [variable-step BDF2](/results/variable-step-bdf2-stability.md);
   [IMEX-BDF](/methods/imex-linear-multistep-methods.md) and
   [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).
10. **Iterative high-order time integrators.** [Deferred correction](/methods/deferred-correction.md),
   [ADER](/methods/ader-time-integration.md) and their
   [equivalence](/results/dec-ader-equivalence.md).
11. **Software.** [SUNDIALS](/software/sundials.md) with [ARKODE](/software/arkode.md) and
    [CVODE](/software/cvode.md), [Irksome](/software/irksome.md),
    [BSeries.jl](/software/bseries-jl.md), [DifferentialEquations.jl](/software/differentialequations-jl.md),
    [PETSc TS](/software/petsc-ts.md).

## Catalog

[Definitions](/definitions/index.md) · [Methods](/methods/index.md) ·
[Results](/results/index.md) · [Properties](/properties/index.md) ·
[Benchmarks](/benchmarks/index.md) · [Software](/software/index.md) ·
[Sources](/sources/index.md) · [Bibliography](/bibliography.md)
