---
type: Benchmark
title: "Nonlinear Schrödinger equation"
description: "The cubic nonlinear Schrödinger equation on periodic domains, Fourier-discretized so that its stiff linear part is diagonal with a purely imaginary spectrum; the sources use it to test exponential Runge–Kutta methods, exponential Parareal with repartitioning, and adaptive spectral deferred correction against additive Runge–Kutta pairs."
status: established
aliases: [NLS, NLS equation, cubic nonlinear Schrödinger equation, focusing nonlinear Schrödinger equation]
tags: [verification, exponential, parallel, stiff, step-size-control]
timestamp: 2026-10-20T06:18:00Z
---

# Nonlinear Schrödinger equation

The cubic nonlinear Schrödinger (NLS) equation, written here as

$$i\,\partial_tu=-\Delta u+V(x)\,u+g\,\lvert u\rvert^2u$$

(page-local: $u$ the complex wave function, $V$ a potential, $g$ the nonlinearity
coefficient, focusing for $g<0$ and defocusing for $g>0$), is a dispersive, non-dissipative
test for time integrators. On a periodic domain with a Fourier pseudo-spectral
discretization the Laplacian becomes the diagonal matrix $L=\operatorname{diag}(-i\kappa^2)$
over the wavenumbers $\kappa$ (page-local), so the stiff linear part is skew-Hermitian with
a purely imaginary spectrum whose size grows like $\Delta x^{-2}$, while the cubic term is
mildly stiff. Exponential integrators and IMEX splittings treat $L$ exactly or implicitly;
the test then probes what the non-dissipative spectrum does to stability and to iterative
(parallel-in-time, deferred-correction) solvers. Its diagonal $L$ makes the
[φ-functions](/methods/phi-function-evaluation.md) elementwise.

## Set-ups in the sources

| Source | Equation as printed | Domain, data | Space | Run |
|---|---|---|---|---|
| [Luan (2021)](/sources/luan-2021.md), §6, Ex. 6.2 | $i\partial_t\Psi=-\partial_{xx}\Psi+(V+\lambda\lvert\Psi\rvert^2)\Psi$, $V=1/(1+\sin^2x)$, $\lambda=1$ | $[-\pi,\pi]$ periodic, $\Psi_0=e^{\sin2x}$ | 128 Fourier modes, $L=\operatorname{diag}(-i\kappa^2)$ | $T=3$, 64 to 1024 steps, reference by MATLAB `ode15s` at tolerance $10^{-14}$ |
| [Buvoli & Minion (2024)](/sources/buvoli-2024.md), §4, Eqs. 16–21 | $iu_t+u_{xx}+2\lvert u\rvert^2u=0$ | $[-4\pi,4\pi]$ periodic, $t=14$ | 1024 Fourier points, 3/2-rule dealiasing, integrated in Fourier space, $\kappa=n/4$ | fine step $h=14/2^{16}$ |
| [Saupe et al. (2025)](/sources/saupe-2025.md), §3.3, Eqs. 27–28 | $u_t=i\Delta u+2i\lvert u\rvert^2u$ (2D) | $2\pi$-periodic square, $u_0=\frac1{\sqrt2}\big(\frac1{1-\cos(x+y)/\sqrt2}-1\big)$, $t=1$ | FFT; IMEX with the Laplacian implicit and the cubic term explicit | errors against the analytic solution of Akhmediev et al. (as recalled) |

In the form above Luan's problem has $g=\lambda=1>0$ (defocusing, with a potential), while
Buvoli & Minion and Saupe et al. solve the focusing equation with $g=-2$ and $V=0$ *(compiler
check of the printed forms, not in the sources)*; this is a difference of test problems, not of
conventions. Luan calls his system "mildly stiff".

**Buvoli & Minion's three initial data** (Eqs. 19–21) differ in how much high-frequency
content they carry:

- $u_0=1+\tfrac1{100}\cos(x/4)$, a modulated plane wave;
- the same plus $\tfrac1{100}\cos(45x/4)$, one added high-frequency mode;
- $u_0=1+\tfrac1{100}\sum_{n=1}^{45}\cos(nx/4)$, 45 modes.

Their spectral estimates (Eqs. 27–28) for the partitioned linear analysis are
$\rho(L)=(341/4)^2$ and a nonlinear-Jacobian spectral radius of about 2 (since
$\lvert u\rvert\le1.0001$ throughout), i.e. $h\lvert\lambda\rvert\in[0,1.6]$ for the linear part
and $[-4.3,4.3]\times10^{-4}$ for the nonlinear part at the fine step.

## What it shows

**Exponential Runge–Kutta methods reach their orders on a unitary problem.** Luan's
expRK4s6 and expRK5s10 reach orders 4 and 5 and are more accurate and faster than the older
expRK4s5 and expRK5s8 (Luan 2021, §6, Fig. 6.2; see
[exponential integrators](/methods/exponential-integrators.md)). The skew-Hermitian $L$
generates a unitary group, not an analytic semigroup, so these orders are evidence outside the
hypotheses of the convergence theorem on
[stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md).

**Exponential Parareal needs repartitioning.** Buvoli & Minion (2024, §4, Table 3, Figs. 2–4)
run [Parareal](/methods/parareal.md) with exponential Runge–Kutta propagators (fine: the
fourth-order method of Krogstad; coarse: the third-order Cox–Matthews method; 2048
processors, 32 fine steps and one coarse step per slice), in LibPFASST on 64 Cori nodes:

- with the classical exponential integrators, Parareal **diverges**: the error grows
  monotonically after the second iteration;
- with the **repartitioned** integrators of Buvoli & Minion (2022), which move a small
  damping operator from the nonlinear into the linear part and rotate the spectrum of $L$
  by $\rho=\pi/128$ into the left half-plane (see
  [exponential integrators](/methods/exponential-integrators.md)), Parareal converges to the
  fine solution (error $3\times10^{-9}$), up to 38.5 times faster than serial fine
  integration in theory and 10.4 times in the measured run, which is communication-bound;
- with one added high-frequency mode the repartitioned iteration stays stable but stalls at
  $3\times10^{-7}$ for up to six iterations; with up to 160 iterations the classical one
  produces NaN after the ninth, and the repartitioned one converges after 150, with a
  theoretical speedup of at most 10.16;
- with the 45-mode data a single coarse step per slice does not converge in six iterations;
  two or three coarse steps improve convergence "significantly" at the cost of speedup.

**Linear analysis predicts which Fourier modes converge.** On the partitioned Dahlquist
equation the authors bound the Parareal error matrix and compute the widest convergent strip
$r_1^{\max}=0.073,\,0.133,\,0.188$ for one, two and three coarse steps (page-local $r_1^{\max}$,
a bound on $h\lvert\lambda\rvert$ of the linear part). Monotone convergence is then predicted
exactly for the Fourier coefficients with $\lvert n\rvert\le73$, 99 and 118, and the
mode-by-mode errors of the NLS runs confirm this "very accurately"; coefficients outside the
strip stay near coarse accuracy (§5.4–5.5, Figs. 6–8). Their general conclusion: on
non-diffusive PDEs Parareal reaches fine accuracy only on low-frequency modes, and
high-order dispersive terms with Fourier pseudo-spectral discretizations are the hardest
case (§5.7, §7). See [parallel-in-time integration](/methods/parallel-in-time-integration.md).

**Adaptive SDC against additive Runge–Kutta pairs.** Saupe et al. (2025, §4, Figs. 7–10)
run IMEX spectral deferred correction with residual tolerance $10^{-4}$ times the error
tolerance:

- step-size adaptivity beats fixed-step and iteration-count-adaptive SDC, and the
  variant that adapts both the step and the number of sweeps is "particularly efficient" on
  the PDE examples (§4.1, Fig. 7; see [step-size control](/methods/step-size-control.md));
- among the parallel variants, the step-and-sweep-adaptive diagonal SDC on three processes
  is the most efficient (§4.1, Fig. 9; see
  [parallel SDC](/methods/parallel-sdc.md) and [pySDC](/software/pysdc.md));
- against the fifth-order additive Kennedy–Carpenter pair ARK5(4), at least one adaptive
  parallel SDC variant is faster, except at low accuracy, where ARK5(4) wins; this is the
  only one of their four problems on which a Runge–Kutta method wins anywhere (§4.2, Fig. 10).

## Linear Schrödinger uses elsewhere in the bundle

Several pages use the **linear** Schrödinger equation, in runs or in recalled theory, which shares the purely imaginary
spectrum but not the cubic term:

- weak-stage-order DIRK methods recover full order on a linear Schrödinger problem with
  time-dependent Dirichlet data, $u_t=\frac{i\omega}{k^2}u_{xx}+f$ with fourth-order finite
  differences ([Biswas et al. 2023](/sources/biswas-2023.md), §6.3, Fig. 4; see
  [DIRK methods of high weak stage order](/methods/dirk-high-weak-stage-order.md));
- Strang splitting of the pseudo-spectral equation with a smooth periodic potential has a
  global error $\le Ch^2\lVert u_0\rVert_{H^2}$ independent of the grid, a result the survey
  recalls from Jahnke and Lubich without a run ([Blanes et al. 2024](/sources/blanes-2024.md), §6.3; see
  [operator splitting](/methods/operator-splitting.md)), and processed, complex-coefficient
  and Magnus-type methods for Schrödinger equations are on
  [processing and effective order](/methods/processing-and-effective-order.md),
  [complex-coefficient splitting](/methods/complex-coefficient-splitting.md) and
  [exponential integrators](/methods/exponential-integrators.md);
- for the semiclassical equation, time splitting with exact sub-flows is
  [asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) in time for
  observables, but large steps do not in general give correct observables for the
  **nonlinear** equation ([Jin 2022](/sources/jin-2022.md), §3.4, as recalled from Bao, Jin &
  Markowich 2003).

## Qualifications

- Buvoli & Minion's speedups are against serial fourth-order exponential integration with the
  same fine step, not against the best serial method at equal error (§4).
- Printed slips in Buvoli & Minion (2024), arXiv v2: the Fourier-space nonlinearity (Eq. 17)
  is printed with $\lvert u\rvert u$ ("abs" not squared) where Eq. 16 has $\lvert u\rvert^2u$;
  the mode eigenvalue (Eq. 44) is printed $+in^2/16$ where $L=\operatorname{diag}(-i\kappa^2)$
  gives $-in^2/16$; and $\bar\lambda_1$ is defined as $i\rho(L)$ in Eq. 24 but written
  without $i$ in §5.1.
- Saupe et al. never state the number of collocation nodes or their type, so their observed
  tolerance-proportionality exponent of 5/4 cannot be checked against their own formula
  (§4.1; see [step-size control](/methods/step-size-control.md)).

# Citations

- [Luan (2021)](/sources/luan-2021.md) — §6, Example 6.2, Fig. 6.2; arXiv v1.
- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — §4 (Eqs. 16–21, Table 3, Figs. 2–4), §5.1 (Eqs. 26–28), §5.4–5.5 (Figs. 6–8), §5.7, §7, App. C; arXiv v2.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — §3.3 (Eqs. 27–28, Fig. 4), §4.1 (Figs. 7–9), §4.2 (Fig. 10); arXiv v2.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §6.3, Fig. 4 (linear Schrödinger).
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.3 (Strang error bound, linear Schrödinger).
- [Jin (2022)](/sources/jin-2022.md) — §3.4 (nonlinear Schrödinger observables, as recalled).
