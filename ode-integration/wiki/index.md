---
okf_version: "0.1"
---

# ode-integration — Knowledge Bundle

Numerical time integration of ordinary differential equations and of
method-of-lines semi-discretizations of PDEs: Runge–Kutta theory, implicit,
Rosenbrock, IMEX, additive and multirate methods, splitting, stability
notions and structure preservation, asymptotic-preserving schemes, deferred
correction and ADER, positivity-preserving (Patankar) schemes,
parallel-in-time methods, step-size control, stage solvers, integrator
software and learned integrators.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($h$ the step, $Y_i$ stage values, $q$ stage order and
$q_{\mathrm w}$ weak stage order, $R(z)$ the stability function, $\mathcal C$
the SSP coefficient, $\phi_k$ with the factorial normalization), and the
[update log](/log.md).

**Corpus:** complete — all 128 sources of the archive ingested in seven chunks. Chunk 1: two *Acta
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
stages. Chunk 4: local time stepping, adaptive and IMEX multirate
infinitesimal methods, multirate exponential methods, nonlinearly
partitioned Runge–Kutta, exponential integrators (stiff order conditions,
Lawson, φ-function evaluation), explicit–implicit–null and Quinpi schemes.
Chunk 5: modified Patankar and other positivity-preserving schemes,
bound-preserving flux limiting, parallel-in-time integration (Parareal,
ParaDiag, parallel SDC), efficient and two-derivative deferred correction,
ADER-DG for ODEs, Lax–Wendroff flux reconstruction, exponential time
differencing for nondiagonal linear parts. Chunk 6: invariant-domain
preserving explicit and IMEX time stepping, Lyapunov stability of Patankar
schemes, fully discrete entropy inequalities, additive polynomial (FIMEX)
integrators, multirate Runge–Kutta–Chebyshev, N-split operator splitting,
Irksome extensions, dual time stepping, and learned integrators. Chunk 7: ten founding papers — stiffness and BDF ([Curtiss & Hirschfelder 1952](/sources/curtiss-1952.md)), A-stability and the order barrier for multistep methods ([Dahlquist 1963](/sources/dahlquist-1963.md)), implicit Runge–Kutta processes ([Butcher 1964](/sources/butcher-1964.md)), the Dormand–Prince pair ([Dormand & Prince 1980](/sources/dormand-1980.md)), TVD Runge–Kutta time discretizations ([Shu & Osher 1988](/sources/shu-1988.md)) and the SSP review ([Gottlieb et al. 2001](/sources/gottlieb-2001.md)), IMEX Runge–Kutta ([Ascher et al. 1997](/sources/ascher-1997.md); [Kennedy & Carpenter 2003](/sources/kennedy-2003.md)), the exponential-integrators review ([Hochbruck & Ostermann 2010](/sources/hochbruck-2010.md)) and relaxation Runge–Kutta ([Ketcheson 2019](/sources/ketcheson-2019.md)). The [bibliography](/bibliography.md) lists the works the sources cite.

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
   [B-convergence](/definitions/b-convergence.md),
   [discrete maximal regularity](/results/discrete-maximal-regularity.md).
2. **Stiffness and order reduction.** [Stiffness](/definitions/stiffness.md), [stage order](/definitions/stage-order.md),
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
   [Padé-based schemes](/methods/pade-time-integration.md),
   [additive polynomial (FIMEX) integrators](/methods/polynomial-time-integrators.md), the [Newmark method](/methods/newmark-method.md),
   [differential-algebraic equations](/definitions/differential-algebraic-equation.md),
   and [solving the stage equations](/methods/implicit-stage-solvers.md); stiff test problems:
   [Van der Pol](/benchmarks/van-der-pol-oscillator.md), [Robertson](/benchmarks/robertson-problem.md),
   [FitzHugh–Nagumo](/benchmarks/fitzhugh-nagumo-model.md), [flow past a cylinder](/benchmarks/flow-past-cylinder.md),
   the [Cahn–Hilliard equation](/benchmarks/cahn-hilliard-equation.md).
4. **Nonlinear stability and structure.**
   [SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md), which began as
   [total variation diminishing](/definitions/total-variation-diminishing.md) time discretizations,
   versus [strong stability](/properties/strong-stability.md) for linear seminegative
   problems, proved with the [energy method](/methods/runge-kutta-energy-method.md)
   ([diagonal Padé schemes](/results/diagonal-pade-strong-stability.md),
   [superviscosity stabilization](/methods/superviscosity-stabilized-runge-kutta.md));
   [positivity preservation](/properties/positivity-preservation.md) of
   [production–destruction systems](/definitions/production-destruction-system.md) by
   [modified Patankar methods](/methods/modified-patankar-methods.md) and
   [adaptive-weight Runge–Kutta methods](/methods/adaptive-weight-runge-kutta.md), and of
   hyperbolic schemes by [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)
   and [invariant-domain preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md),
   with the [Lyapunov stability of positive, conservative schemes](/results/lyapunov-stability-positive-conservative-schemes.md)
   (test problem: the [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md));
   [multiderivative methods and the backward derivative condition](/methods/multiderivative-runge-kutta.md);
   [relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md) and
   [entropy stability](/properties/entropy-stability.md) of the fully discrete scheme
   (the [fully discrete cell entropy inequality](/results/fully-discrete-cell-entropy-inequality.md)),
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
   [embedded pairs](/methods/embedded-runge-kutta-pair.md) such as the [Dormand–Prince 5(4) pair](/methods/dormand-prince-5-4.md),
   [step-size control](/methods/step-size-control.md),
   [low-storage schemes](/methods/low-storage-runge-kutta.md),
   [dense output](/methods/dense-output.md),
   [extrapolation methods](/methods/extrapolation-methods.md),
   [von Neumann stability analysis](/definitions/von-neumann-stability-analysis.md); benchmarks: the
   [linear advection equation](/benchmarks/linear-advection-equation.md), the
   [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and the
   [isentropic vortex](/benchmarks/isentropic-vortex.md).
6. **Additive, partitioned and multirate methods.**
   [IMEX and additive Runge–Kutta](/methods/imex-runge-kutta.md) (the [Kennedy–Carpenter ARK methods](/methods/kennedy-carpenter-ark-methods.md)),
   [semi-implicit and linearly implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md),
   [GARK](/methods/generalized-additive-runge-kutta.md),
   [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md),
   [IMEX-MRI-GARK](/methods/imex-mri-gark.md), [IMEX-MRI-SR](/methods/imex-mri-sr.md),
   [multirate exponential methods](/methods/multirate-exponential-methods.md),
   [multirate Runge–Kutta–Chebyshev](/methods/multirate-runge-kutta-chebyshev.md),
   [local time stepping](/methods/local-time-stepping.md),
   [nonlinearly partitioned Runge–Kutta](/methods/nonlinearly-partitioned-runge-kutta.md),
   [explicit–implicit–null time marching](/methods/explicit-implicit-null-method.md), [multirate GARK](/methods/multirate-gark.md),
   [multirate linear stability](/definitions/multirate-linear-stability.md) and its
   [A-stability barriers](/results/multirate-a-stability-barriers.md); test problem: the
   [Brusselator](/benchmarks/brusselator.md).
7. **Splitting and composition.** [Operator splitting](/methods/operator-splitting.md),
   [composition methods](/methods/composition-methods.md), their
   [order conditions](/results/splitting-order-conditions.md), the
   [negative-coefficient barrier](/results/negative-coefficient-barrier.md) and its escape through
   [complex coefficients](/methods/complex-coefficient-splitting.md);
   [exponential integrators](/methods/exponential-integrators.md) with their
   [stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md),
   [Lawson methods](/methods/lawson-methods.md) and
   [φ-function evaluation](/methods/phi-function-evaluation.md); test problems: the
   [Gray–Scott model](/benchmarks/gray-scott-model.md), the
   [nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md).
8. **Multiscale problems.** [Asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md),
   [uniform accuracy for relaxation systems](/results/uniform-accuracy-relaxation-systems.md),
   [BGK penalization](/methods/bgk-penalization.md),
   [micro–macro decomposition](/methods/micro-macro-decomposition.md),
   [Quinpi](/methods/quinpi.md); test problems: the
   [linear hyperbolic relaxation system](/benchmarks/hyperbolic-relaxation-system.md), the
   [Broadwell model](/benchmarks/broadwell-model.md), the [Gresho vortex](/benchmarks/gresho-vortex.md),
   [colliding acoustic pulses](/benchmarks/colliding-acoustic-pulses.md); compressible-flow tests: the
   [Sod shock tube](/benchmarks/sod-shock-tube.md), [double Mach reflection](/benchmarks/double-mach-reflection.md),
   the [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md), the
   [Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md).
9. **Linear multistep methods.** [Linear multistep methods](/methods/linear-multistep-method.md),
   [zero-stability](/definitions/zero-stability.md),
   [Dahlquist's order barrier for A-stable multistep methods](/results/dahlquist-second-barrier.md), the
   [BDF methods](/methods/backward-differentiation-formula.md),
   [G-stability](/properties/g-stability.md) and the
   [multiplier energy technique](/methods/multiplier-energy-technique.md) with its results on
   [BDF6](/results/bdf6-energy-stability.md) and
   [variable-step BDF2](/results/variable-step-bdf2-stability.md);
   [IMEX-BDF](/methods/imex-linear-multistep-methods.md) and
   [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).
10. **Iterative high-order time integrators.** [Deferred correction](/methods/deferred-correction.md),
   [ADER](/methods/ader-time-integration.md) and their
   [equivalence](/results/dec-ader-equivalence.md);
   [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md), a
   single-stage Taylor scheme.
11. **Parallel-in-time integration.** [Overview](/methods/parallel-in-time-integration.md),
    [Parareal](/methods/parareal.md), [ParaDiag](/methods/paradiag.md),
    [parallel-across-the-method SDC](/methods/parallel-sdc.md); test problems: the
    [heat equation](/benchmarks/heat-equation.md), the
    [Allen–Cahn equation](/benchmarks/allen-cahn-equation.md), the
    [Vlasov–Poisson equation](/benchmarks/vlasov-poisson-equation.md).
12. **Learned integrators.** [Learned time integrators](/methods/learned-time-integrators.md):
    neural surrogates with exact conservation laws, operator networks for stiff
    kinetics, and Runge–Kutta physics-informed networks.
13. **Software.** [SUNDIALS](/software/sundials.md) with [ARKODE](/software/arkode.md) and
    [CVODE](/software/cvode.md), [Irksome](/software/irksome.md),
    [BSeries.jl](/software/bseries-jl.md), [DifferentialEquations.jl](/software/differentialequations-jl.md),
    [Trixi.jl](/software/trixi-jl.md),
    [PETSc TS](/software/petsc-ts.md), [pySDC](/software/pysdc.md).

## Catalog

[Definitions](/definitions/index.md) · [Methods](/methods/index.md) ·
[Results](/results/index.md) · [Properties](/properties/index.md) ·
[Benchmarks](/benchmarks/index.md) · [Software](/software/index.md) ·
[Sources](/sources/index.md) · [Bibliography](/bibliography.md)
