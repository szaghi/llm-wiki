---
type: Benchmark
title: "Heat equation"
description: "The linear heat equation u_t = Delta u + g, semi-discretized to y' = Ly + g with -L symmetric positive definite, is the model parabolic problem; the parallel-in-time sources use it to show one-iteration ParaDiag solves, Parareal contraction factors and low-rank Parareal convergence, and many other pages use it as a stiff linear test."
status: established
aliases: [diffusion equation, linear diffusion, 2D heat equation, 1D heat equation]
tags: [stiff, parallel, verification, linear-algebra]
timestamp: 2026-10-20T10:00:00Z
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
  $\vartheta\Delta+(1-\vartheta)\Delta$ to analyse exponential integrators with a partial
  linear part (see [stability function](/definitions/stability-function.md)).
- [Blanes et al. (2024)](/sources/blanes-2024.md) (§6.1, Eq. 6.13): dimensional (LOD/ADI) splitting of the 2D
  problem (see [operator splitting](/methods/operator-splitting.md)).

## Qualifications

- Gander & Palitta's Theorem 3.1 covers this problem; their comparisons of ParaDiag
  variants, however, use a nonsymmetric advection–diffusion problem, where it does not
  apply.
- Jin et al. (2025) compare against the serial fine solution, not the exact solution; their
  efficiencies are simulated, not measured.
- All three parallel-in-time sources were read as arXiv preprints.

# Citations

- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §6.1 (Eq. (6.1), Table 6.1), Thm. 3.1.
- [Jin et al. (2025)](/sources/jin-2025.md) — arXiv v2: Example 4.1, §4.2 (Figs. 4.2–4.3, Table 4.2), Thm. 3.2.
- [Carrel et al. (2023)](/sources/carrel-2023.md) — arXiv v2: §4.1 (Eq. (27), Figs. 3–4), Lemma 4.1, Cor. 4.2.
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §5.1.
- [Munch et al. (2024)](/sources/munch-2024.md) — §5.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §6.2.
- [Caliari et al. (2024)](/sources/caliari-2024.md) — §2.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.1 (Eq. 6.13).
