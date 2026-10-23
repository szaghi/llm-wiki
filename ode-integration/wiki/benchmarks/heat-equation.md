---
type: Benchmark
title: "Heat equation"
description: "The linear heat equation u_t = Delta u + g, semi-discretized to y' = Ly + g with -L symmetric positive definite, is the model parabolic problem; the sources use it for ParaDiag and Parareal convergence, order reduction of DIRK and Radau IIA methods, stage preconditioners, multirate Chebyshev speed-ups on locally refined meshes and Runge–Kutta PINNs."
status: established
aliases: [diffusion equation, linear diffusion, 2D heat equation, 1D heat equation]
tags: [stiff, parallel, verification, linear-algebra]
timestamp: 2026-10-20T06:18:00Z
---

# Heat equation

The **heat equation** $\partial_tu=\Delta u+g$ on a bounded domain with
Dirichlet or Neumann data becomes, after spatial discretization, the linear system
$y'=Ly+g(t)$ with $-L$ symmetric positive definite (with a mass matrix for finite
elements). Its spectrum is real and negative and spreads like $\Delta x^{-2}$, so an
explicit method needs $h=O(\Delta x^2)$, while an
[A-stable](/properties/a-stability.md) method has no step restriction. It is the model
parabolic problem: dissipative, with a one-sided Lipschitz constant equal to the largest
eigenvalue of $L$, which is negative. That is the setting in which most
[parallel-in-time](/methods/parallel-in-time-integration.md) theory is proved.

## Set-ups in the parallel-in-time sources

| source | problem | discretization | use |
|---|---|---|---|
| [Gander & Palitta (2024)](/sources/gander-2024.md), §6.1, Eq. (6.1) | $(0,1)^2$, $t\in(0,1]$, $u=0$ on the boundary, $g=0$, $u_0=xy(x-1)(1-y)$ | five-point finite differences, $\Delta x=1/(n+1)$; up to $1\,048\,576$ unknowns; backward Euler with $N\in\{256,512,1024\}$ steps | [ParaDiag](/methods/paradiag.md) capacitance solve |
| [Jin et al. (2025)](/sources/jin-2025.md), Example 4.1 | $(0,\pi)$, homogeneous Dirichlet; (a) $u_0=x^{10}(x-\pi)^{10}/(\pi/2)^{10}$, $g=0$, $T=1$; (b) $u_0=\chi_{(0,\pi/2)}$, $g=\cos t\sin x$, $T=1$; (c) $u_0=2\chi_{(0,\pi/2)}-1$, $g=50\sin(2\pi(x+t))$, $T=100$ | P1 finite elements, $\Delta x=\pi/1000$; fine Lobatto IIIC or Radau IIA | [Parareal](/methods/parareal.md) with optimized coarse propagators |
| [Carrel et al. (2023)](/sources/carrel-2023.md), §4.1 | differential Lyapunov equation $X'=AX+XA+CC^\top$ with $A$ the 1D Dirichlet Laplacian on $[-1,1]$, i.e. the 2D heat equation on $[-1,1]^2$ in matrix form, $t\in[0,2]$ | centred differences, $n\in\{50,100,200\}$ | low-rank Parareal |

## Results

**ParaDiag in one iteration.** For the 2D problem, Gander & Palitta's bound
$1+1/(h\lambda_{\min}(-L))$ on the condition number of the capacitance matrix is $13.97$,
$26.94$, $52.88$ for $N=256$, $512$, $1024$, growing linearly in $N$ and independent of the
spatial size; the actual spectrum lies in $[1,1.004]$, and a single Galerkin iteration
reaches relative residual below $10^{-8}$ for every size (§6.1, Table 6.1). Here
$\lambda_{\min}(-L)=(8/\Delta x^2)\sin^2(\pi\Delta x/2)\approx2\pi^2$, which reproduces the printed bounds with $h=1/N$ *(compiler check, not in the source)*.

**Parareal contraction.** With backward Euler as coarse propagator the observed contraction
is about $0.3$ at $N_f=100$ fine steps per slice ($N_f$ page-local), as the Yang–Yuan–Zhou bound predicts; with
optimized coarse propagators it is far smaller, and with $N=5$ slices the error is exactly
zero after five iterations (finite termination) (Jin et al. 2025, §4.2, Fig. 4.2). For the
discontinuous data of case (b) the rates still follow Theorem 3.2, and the optimized coarse
propagator needs 2 ($N_f=20$) or 9 ($N_f=100$) fewer iterations than backward Euler to reach
$10^{-8}$ (Fig. 4.3). For case (c), $N_f=100$, target accuracy $10^{-7}$, iterations drop from
10–11 to 4 and the simulated efficiency rises from 7.7–13.1 % to 17.0–34.5 % (Table 4.2).

**Low-rank Parareal.** On the Lyapunov form, the convergence rate is independent of the
coarse rank, the fine rank and $n$, despite the stiffness growing with $n$, and is faster for
larger slices $\Delta T\in\{0.02,0.04,0.08\}$, as the dissipative theory predicts (Carrel et
al. 2023, §4.1, Figs. 3–4). The paper also proves that the Lyapunov solution has low-rank
approximations with error decaying exponentially in the rank (Lemma 4.1, Cor. 4.2).

## Set-ups in the accuracy, solver and multirate sources

| source | problem | discretization | use |
|---|---|---|---|
| [Kirby & MacLachlan (2025)](/sources/kirby-2025.md), §4.1 | $(0,1)^2$, manufactured $u=e^{-0.1t}\sin(\pi x)\cos(\pi y)$, Dirichlet data imposed on the stage values, $T=1$ | serendipity elements of degree 2 and 3 on $N\times N$ squares, $h=\kappa/N$ with $\kappa\in\{1,4,8\}$ ($\kappa$ page-local) | [order reduction](/definitions/order-reduction.md) and [stage preconditioners](/methods/implicit-stage-solvers.md) in [Irksome](/software/irksome.md) |
| Kirby & MacLachlan (2025), §2.1, Fig. 2 | 1D on $[0,1]$, $u(0,x)=0$, $u(t,0)=u(t,1)=1$ for $t>0$ (incompatible data) | P1 elements on 10 intervals, three-stage Lobatto IIIC, $h=0.05$ to $t=0.5$ | [boundary data on the stages](/methods/runge-kutta-stage-boundary-treatment.md) |
| [Abdulle et al. (2022)](/sources/abdulle-2022.md), §5.2 | $(0,1)^2$, $T=1/2$, homogeneous Dirichlet, zero initial data, manufactured $u=\sin^2(\pi x_1)\sin^2(\pi x_2)\sin^2(\pi t)$ | first-order DG on $2^j\times2^j$ simplices, $j=2,\dots,5$, refined twice in $(1/4,3/4)^2$; $h=2^{-j}$ | [multirate Runge–Kutta–Chebyshev](/methods/multirate-runge-kutta-chebyshev.md) on a locally refined mesh |
| Abdulle et al. (2022), §5.3 (Eq. (5.4)) | two $10\times5$ rectangles joined by a channel of width $\delta$ (page-local), homogeneous Neumann data, zero initial data, source $\sin^2(10\pi t)\,e^{-5\lVert x-x_c\rVert^2}$ centred in the upper rectangle, $T=0.1$ | DG on a Delaunay mesh, mesh size about $0.015$; $\delta=2^{-k}$, $k=0,\dots,15$ | multirate speed-up when a few elements are very small |
| [Akrivis et al. (2025)](/sources/akrivis-2025.md), §5.4.1–5.4.2 | $(0,1)^2$, $u_t=0.02\,\Delta u$, homogeneous Neumann data, $t\in[0,1]$; initial data a smooth cosine bump, or the indicator, of the disk of radius $0.1$ centred at $(0.6,0.7)$ | physics-informed neural network in space, three-stage Gauss, Lobatto IIIA or Radau IIA in time, 40 time nodes | [learned time integrators](/methods/learned-time-integrators.md) (Runge–Kutta PINNs) |

## Results of these set-ups

**Order reduction and its cure.** On the 2D problem with degree-2 elements, backward Euler
is suboptimal in $L^2$ for every $\kappa$, and Alexander's three-stage L-stable DIRK
(order 3, stage order and weak stage order 1) loses $L^2$ accuracy at $\kappa=8$; Radau IIA
with $s\ge2$ stages and the weak-stage-order-3 DIRK WSODIRK433 keep the optimal spatial rate
(Kirby & MacLachlan 2025, §4.1, Fig. 3). With cubic elements the loss of Alexander's DIRK is
larger, and Radau IIA(2) (order 3, stage order 2) loses $L^2$ but not $H^1$ accuracy at large
steps, while Radau IIA(3), Radau IIA(4) and WSODIRK433 stay dominated by the spatial error
(Fig. 4). See [weak stage order](/definitions/weak-stage-order.md) and
[DIRK methods with high weak stage order](/methods/dirk-high-weak-stage-order.md).

**Stage preconditioners.** On the same problem with FGMRES and one algebraic multigrid
cycle per diagonal block, block Jacobi and block Gauss–Seidel need outer iteration counts that
grow with the number of stages $s$, while the Rana-type $LD$ preconditioner stays nearly flat;
at $s=4$, read from the plot, about 47, 22 and 10 iterations against about 7 for a DIRK, and
run times of the $LD$ preconditioner and of the DIRK are "very comparable" (Kirby &
MacLachlan 2025, §4.1, Fig. 5). The text puts this study on a $256\times256$ mesh, the caption
of Fig. 5 on a $64\times64$ mesh.

**Incompatible boundary data.** Imposing the time derivative of the boundary data on the stage
derivatives sees a zero boundary derivative when the boundary jumps to 1 at $t=0^+$, and
returns the steady zero solution; imposing the data on the stage values captures the approach
to $u\equiv1$ (Kirby & MacLachlan 2025, §2.1, Fig. 2).

**Multirate stabilized stepping.** On the locally refined square, RKC and mRKC both converge at
first order in space–time in $H^1$ with similar errors, and mRKC needs far fewer outer stages
$s$, with a constant inner stage number (Abdulle et al. 2022, §5.2, Fig. 12). In the channel
problem the stiffness scales like $\delta^{-2}$ while the slow spectral radius stays almost
constant; with $h=0.01$ the CPU-time speed-up of mRKC over RKC is always at least 1 and reaches
about 40, with relative $L^2$ and $H^1$ differences between the two solutions of at most
$3\times10^{-4}$ (Fig. 15). In work–precision diagrams mRKC is 10 to 70 times faster than the
second-order RKC2 at $\delta=2^{-12}$, while implicit Euler is about as efficient as mRKC at
$\delta=2^{-6}$ and always slightly faster at $\delta=2^{-12}$, which the authors attribute to
the symmetric linear Laplacian favouring implicit Euler (Fig. 16).

**Runge–Kutta PINNs.** The three Runge–Kutta PINNs have a smaller final-time misfit than a
PINN with uniform time sampling (given four times as many time points) and keep the total heat
$\int_\Omega u$ almost constant, which uniform sampling does not (Akrivis et al. 2025,
§5.4.1–5.4.2, Figs. 1–4). For the discontinuous initial datum the Gauss and Lobatto IIIA
PINNs oscillate near $t=0$ while Radau IIA smooths, which the authors relate to the known
smoothing behaviour of the underlying methods (Fig. 5): Gauss and Lobatto IIIA have
$\lvert R(\infty)\rvert=1$, Radau IIA has $R(\infty)=0$ (see
[stability function](/definitions/stability-function.md)). All evidence is graphical. The
same paper proves discrete maximal $L^2$ regularity for the abstract parabolic problem
$u'+\mathcal Au=f$ ($\mathcal A$ page-local, self-adjoint positive) with variable steps
(see [discrete maximal regularity](/results/discrete-maximal-regularity.md)).

## Other uses in the bundle

The heat equation recurs as a stiff linear test throughout the bundle:

- [Gardner et al. (2022)](/sources/gardner-2022.md) (§5.1): 2D, $4096^2$ grid; CVODE's BDF
  8.8 s against ARKODE's DIRK 67.3 s (see [BDF](/methods/backward-differentiation-formula.md)).
- [Munch et al. (2024)](/sources/munch-2024.md) (§5): 3D, stage-parallel
  [fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md) up to 147,456
  processes (see [implicit stage solvers](/methods/implicit-stage-solvers.md)).
- [Biswas et al. (2023)](/sources/biswas-2023.md) (§6.2): numerical boundary layers of width
  $O(h^{1/2})$ that cost half an order in $u_x$ when weak stage order is below the order (see
  [order reduction](/definitions/order-reduction.md)).
- [Caliari et al. (2024)](/sources/caliari-2024.md) (§2): split as
  $\vartheta\Delta+(1-\vartheta)\Delta$ on a periodic domain for a Fourier stability analysis
  of exponential integrators with a partial linear part; the runs are on variable-coefficient
  linear and nonlinear diffusion and on advection–diffusion–reaction problems (see [stability function](/definitions/stability-function.md)).
- [Blanes et al. (2024)](/sources/blanes-2024.md) (§6.1, Eq. 6.13): dimensional (LOD/ADI) splitting of the 2D
  problem, as an illustration of the construction with no numerical run (see
  [operator splitting](/methods/operator-splitting.md)).
- [Goswami et al. (2023)](/sources/goswami-2023.md) (§2–3, Eq. (1)): the 1D equation
  $u_t=\nu u_{xx}$ ($\nu$ the diffusivity, page-local) is the model problem of their
  truncation-error analysis of [low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md)
  stages with delayed halo data; their numerical runs are on advection–diffusion (see
  [linear advection equation](/benchmarks/linear-advection-equation.md)), not on pure
  diffusion.

## Qualifications

- Gander & Palitta's Theorem 3.1 covers this problem; their comparisons of ParaDiag
  variants, however, use a nonsymmetric advection–diffusion problem, where it does not
  apply.
- Jin et al. (2025) compare against the serial fine solution, not the exact solution; their
  efficiencies are simulated, not measured.
- All three parallel-in-time sources were read as arXiv preprints.
- **Printed inconsistency in Kirby & MacLachlan (2025).** The text places the solver study of
  §4.1 on a $256\times256$ mesh, the caption of Fig. 5 on a $64\times64$ mesh with cubic
  elements; which one was run is not recoverable from the paper.
- **Printed inconsistency in Abdulle et al. (2022).** The caption of Fig. 13 shows the channel
  solution "at $t=1$", while the problem is posed to $T=0.1$.
- Kirby & MacLachlan (2025) and Abdulle et al. (2022) solve with a source term or
  manufactured solution, not the homogeneous equation; Akrivis et al. (2025) do not state the
  reference solution of their misfit plots, and label panels "$t=1$" and "$t=2$" for a problem
  posed on $[0,1]$. Abdulle et al. and Akrivis et al. were read as arXiv preprints.

# Citations

- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §6.1 (Eq. (6.1), Table 6.1), Thm. 3.1.
- [Jin et al. (2025)](/sources/jin-2025.md) — arXiv v2: Example 4.1, §4.2 (Figs. 4.2–4.3, Table 4.2), Thm. 3.2.
- [Carrel et al. (2023)](/sources/carrel-2023.md) — arXiv v2: §4.1 (Eq. (27), Figs. 3–4), Lemma 4.1, Cor. 4.2.
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §5.1.
- [Munch et al. (2024)](/sources/munch-2024.md) — §5.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §6.2.
- [Caliari et al. (2024)](/sources/caliari-2024.md) — §2.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.1 (Eq. 6.13).
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §2.1 (Fig. 2), §4.1 (Figs. 3–5).
- [Abdulle et al. (2022)](/sources/abdulle-2022.md) — arXiv v6: §5.2 (Fig. 12), §5.3 (Eq. (5.4), Figs. 13–16).
- [Akrivis et al. (2025)](/sources/akrivis-2025.md) — arXiv v2: §4, §5.4.1–5.4.2 (Eqs. (126)–(129), Figs. 1–5).
- [Goswami et al. (2023)](/sources/goswami-2023.md) — §2–3 (Eq. (1)).
