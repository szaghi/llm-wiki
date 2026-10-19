# Benchmarks

Standard test problems.

* [Brusselator](/benchmarks/brusselator.md) — The one-dimensional advection–diffusion–reaction Brusselator, a three-species stiff reaction system with a fast relaxation term, is the shared test of IMEX, multirate and nonlinear-solver studies; the page gives the variants, parameters and splittings used and what each test showed.
* [Isentropic vortex](/benchmarks/isentropic-vortex.md) — Exact smooth solution of the compressible Euler equations, a vortex advected by a uniform stream, used to measure temporal convergence order and accuracy-limited cost of time integrators: explicit embedded pairs with PID control and fully implicit Runge–Kutta methods with block preconditioning.
* [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md) — The scalar stiff test problem $y'=\lambda(y-g(t))+g'(t)$, whose smooth exact solution $g$ is independent of the stiffness $\lambda$; it isolates the stiff-regime error of a one-step method, exposes order reduction through the stage-order residuals, and grounds weak stage order and Scholz's Rosenbrock conditions. Includes the multirate Kværnø–Prothero–Robinson variant.
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) — Three-dimensional periodic vortex flow used to test time integrators on compressible-flow semidiscretizations: inviscid at low Mach number as a stability-limited test for explicit pairs and step-size controllers, and viscous at Re 1600 for optimized many-stage Runge–Kutta methods.
