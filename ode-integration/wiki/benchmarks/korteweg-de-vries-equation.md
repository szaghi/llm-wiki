---
type: Benchmark
title: "Korteweg–de Vries equation"
description: "The dispersive KdV equation u_t + 6uu_x + u_xxx = 0, its generalized and linear variants and its 2D relative, the Kadomtsev–Petviashvili equation; the third derivative makes explicit steps scale like Δx³, so the sources test explicit–implicit–null stabilization, energy-relaxed IMEX, additive polynomial methods, positivity-corrected SDIRK and exponential Parareal on them."
status: established
aliases: [KdV equation, KdV, generalized KdV equation, Korteweg–de Vries, Kadomtsev–Petviashvili equation, KP equation, KP-I]
tags: [verification, imex, structure-preserving, stiff, positivity, parallel]
timestamp: 2026-10-20T06:18:00Z
---

# Korteweg–de Vries equation

The Korteweg–de Vries (KdV) equation

$$u_t+6uu_x+u_{xxx}=0$$

is the model of weakly nonlinear dispersive waves; on a periodic domain it conserves
the mass $\int u$, the energy $\int\tfrac12u^2$ and the Whitham invariant
$\int(2u^3-u_x^2)$, and it has soliton solutions
([Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md), §6, Eqs. (32)–(33)). For time
integration its point is the third derivative: a semi-discretization has
$\lVert D_3\rVert=O(\Delta x^{-3})$ (page-local third-derivative matrix), so an
explicit method needs $h=O(\Delta x^3)$, and the sources treat the dispersive term
implicitly (§6) or through an implicitly treated linear surrogate
([Tan et al. (2022)](/sources/tan-2022.md), §1).

## Variants and data

* **Soliton data** (Biswas & Ketcheson 2023, §6, App. B): one soliton
  $u=\beta_1\operatorname{sech}^2\big(\sqrt{\beta_1}(x-2\beta_1t)/\sqrt2\big)$ with
  $\beta_1=1$ on $[-20,60]$, $N=512$, $t\in[0,20]$; two solitons ($\beta=0.5,1$) on
  $[-80,80]$, $N=1024$, $t\in[-25,25]$; three solitons ($\beta=0.4,0.7,1$) on
  $[-130,130]$, $N=1536$, $t\in[-50,50]$; steps $0.1$ or $0.01$ (page-local soliton
  amplitudes $\beta_j$). Space: the split-form Fourier semi-discretization of Ranocha,
  Mitsotakis & Ketcheson, which conserves discrete mass and energy for any $\Delta x$
  (Eqs. (34)–(35), as recalled).
* **Linear dispersion** $u_t+u_{xxx}=0$ with $u_0=\sin x$ on $(-\pi,\pi)$, $T=1$
  (Tan et al. 2022, §4.2.1, Eq. (4.8), Tables 4.11–4.12).
* **Generalized KdV** $u_t+(u^3)_x+(u(u^2)_{xx})_x=0$ with the travelling-wave solution
  $u=\sqrt{2\alpha}\cos((x-\alpha t)/2)$, $\alpha=0.1$, on $(-\tfrac32\pi,\tfrac52\pi)$ to
  $T=\pi$ (Tan et al. 2022, §4.2.1, Eq. (4.9), Tables 4.13–4.14), and a 2D version with
  $\alpha=0.5$ to $T=1$ (§4.2.2, Eq. (4.11), Tables 4.17–4.18;
  page-local wave speed $\alpha$). The dispersive term has a solution-dependent
  coefficient, so an implicit treatment of it would be nonlinear.
* **Zakharov–Kuznetsov**, a 2D relative with $u_{xxx}+u_{xyy}$ and a manufactured source
  (Tan et al. 2022, §4.2.2, Eq. (4.10), Tables 4.15–4.16).

* **Advection–dispersion form with positivity shift** ([Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md),
  §4.1.4, Eq. 43): $u_t+\alpha uu_x+\varrho u_x+\nu_{\mathrm d}u_{xxx}=0$ (page-local
  coefficients $\alpha$, $\varrho$, $\nu_{\mathrm d}$, whose values are not printed), periodic
  finite volumes recast as a
  [production–destruction system](/definitions/production-destruction-system.md) with an
  interface-flux destruction matrix, the solution shifted to be positive, $u_0=6\operatorname{sech}^2x$
  on what the figures show as $[-10,10]$; runs to $t=0.35$ (snapshots), $[0,2]$ (mass) and
  $[0,1.7]$ (timing, about one soliton crossing).
* **Kadomtsev–Petviashvili equation**, the 2D relative
  $(u_t+6uu_x+u_{xxx})_x+3\sigma_{\mathrm{KP}}^2u_{yy}=0$, with $\sigma_{\mathrm{KP}}^2=-1$ (KP-I,
  unstable line soliton) or $+1$ (KP-II) (page-local) ([Buvoli & Minion (2024)](/sources/buvoli-2024.md),
  §6.1–6.2, Eqs. 52–55): KP-I in evolution form on $[-8\pi,8\pi]\times[0,8\pi]$, periodic,
  $972\times750$ Fourier points with 3/2 dealiasing, the antiderivative $\partial_x^{-1}$
  replaced by $-i/\kappa_x$ (zero at $\kappa_x=0$), $u_0=2\operatorname{sech}^2\big((x+4\pi)+\tfrac15\cos(y/4)\big)$,
  final time 4, fine step $2^{-16}$; it forms a 2D soliton.

* **Cosine data, Fourier space** ([Buvoli & Southworth (2023)](/sources/buvoli-2023.md),
  §6.1): $u_t=-\big(\delta\,u_{xxx}+\tfrac12(u^2)_x\big)$ with $\delta=0.022$ as printed
  (page-local $\delta$), $u_0=\cos\pi x$ on $[0,2]$, periodic, final time
  $3.6/\pi$; 512 Fourier modes with 3/2 dealiasing, integrated in Fourier space as
  $y'=Ly+N(t,y)$ with diagonal $L$, the dispersive part implicit and the nonlinear part
  explicit; reference by a 32nd-order exponential spectral deferred correction method; relative
  maximum-norm error.

Tan et al. use fourth-order central finite differences and $P^2$ local DG, periodic
data and $h=\Delta x$ throughout (§2.2, §4.2).

## What it shows

* **Explicit–implicit–null stabilization of dispersion.** Adding and subtracting
  $\vartheta\,c_{\max}\partial_x^3u$ (page-local: $\vartheta$ the stabilization ratio,
  $c_{\max}$ the largest coefficient of the third derivative, sign chosen by the wind
  direction) and treating only the added copy implicitly with ARS(4,4,3) gives linear
  constant-coefficient stage solves for the nonlinear equations. The numerical Fourier
  threshold $\vartheta\ge0.54$ is sharp on these tests: with $\vartheta=0.53$ the linear
  dispersive run explodes on fine meshes ($L^1$ error $1.01\times10^1$ for finite
  differences and $7.33\times10^2$ for DG at $N=1280$), while $\vartheta=0.54$ is third
  order with errors near $10^{-9}$ (Tan et al. 2022, §4.2.1, Tables 4.11–4.12); generalized
  KdV shows the same split between 0.53 and 0.54, with a mild error penalty for a large
  ratio ($\vartheta=10$), unlike on diffusion problems (Tables 4.13–4.14). See
  [explicit–implicit–null method](/methods/explicit-implicit-null-method.md).
* **Relaxation with IMEX methods and long-time error growth.** With the dispersive term
  implicit and the nonlinear term explicit in the Kennedy–Carpenter pairs ARK3(2)4L[2]SA
  and ARK4(3)6L[2]SA, energy relaxation reduces the maximal energy change on one soliton
  from $5.38\times10^{-2}$ and $1.05\times10^{-2}$ to about $10^{-15}$, and turns quadratic
  error growth into linear growth, as theory predicts for one soliton (Biswas & Ketcheson
  2023, §6.1.1, Table 1, Fig. 11). With two solitons the two relaxed methods grow
  sublinearly or between linearly and quadratically; with three, growth stays quadratic,
  though smaller, because the energy of each soliton drifts linearly, so mass and energy
  conservation do not guarantee linear error growth for multi-soliton data (§6.1.2–6.1.3,
  §7, Figs. 12–13). See [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md)
  and [IMEX Runge–Kutta](/methods/imex-runge-kutta.md).

* **Positivity correction of SDIRK on a dispersive problem.** Nurkhametova et al. (2026,
  §5.1.4, §5.2.4, §5.3, Tables 4, 6, Figs. 9–10, 23–24) post-process SDIRK21, SDIRK32 and
  SDIRK43 with their Patankar predictor–corrector (see
  [modified Patankar methods](/methods/modified-patankar-methods.md)). Correcting the final
  stage removes undershoots of about $10^{-4}$ at $t=0.35$ without visible distortion and keeps
  mass to round-off ($7.40\times10^{-16}$ against $8.88\times10^{-16}$ uncorrected); correcting
  every stage "exhibited severely distorted dynamics" (not shown), so only the final-stage
  correction is recommended here. Fixed-step slopes are 1.72, 3.37 and 3.85 for the three
  methods, and the correction costs 94.5 % more runtime with SDIRK43 (MATLAB on a laptop).
* **Exponential Parareal on a dispersive 2D problem.** With exponential Runge–Kutta
  propagators and repartitioning, [Parareal](/methods/parareal.md) on 8192 slices does not
  converge monotonically on KP-I: the error drops fast, then plateaus. With three coarse steps
  per slice it reaches the accuracy of the serial fine integrator; after 28 iterations, errors
  $2.7\times10^{-7}$, $1.3\times10^{-8}$ and $1.8\times10^{-9}$ (one, two, three coarse steps) are
  reached 9.09, 10.15 and 11.71 times faster than serial fine integration. Because one step of
  the 2D problem is expensive relative to communication, the theoretical and achieved speedups
  agree here, unlike on the 1D [nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md)
  (Buvoli & Minion 2024, §6.2, Table 4a, Fig. 14; see
  [exponential integrators](/methods/exponential-integrators.md)).

* **Additive polynomial methods with parallel stages.** On the cosine data the
  seventh-order FIMEX-Radau*(5,2) (Radau IIA implicit part, explicit part extrapolated from the
  previous step, two order-raising iterations) is the most efficient serial method for
  relative errors below $10^{-2}$; computing its five independent explicit evaluations on five
  OpenMP threads makes it the most efficient at every accuracy, about 2 times faster than any
  Runge–Kutta method at error $10^{-2}$ and about 30 times faster than their fourth-order
  IMEX Runge–Kutta comparator below $10^{-4}$ (14-core Intel Xeon E5-2683 v3; FFTs single-threaded).
  The fourth-order FIMEX-Radau*(3,2) converges at order 4 over most of the step range, beats
  that comparator, and stores three solution vectors instead of five (Buvoli & Southworth 2023,
  §6.1.2, Fig. 5). See [polynomial time integrators](/methods/polynomial-time-integrators.md)
  and [parallel-in-time integration](/methods/parallel-in-time-integration.md).

## Qualifications

* Buvoli & Southworth (2023) print the dispersive term as $\delta\,u_{xxx}$ with
  $\delta=0.022$ and describe the experiment as identical to one in two works they cite,
  without naming the problem further (§6.1). Their §6.1.2 text discusses FIMEX-Radau*(2,1) while Fig. 5 shows
  FIMEX-Radau*$(q,2)$. They were read as arXiv v2.

* Nurkhametova et al. (2026) give neither the coefficients, the mesh nor the positivity shift of
  their KdV run, and the all-stage failure is asserted without figures. Their SDIRK32 and
  SDIRK43 have negative weights, which the positivity guarantee of the corrector excludes, so the
  guarantee does not cover two of the three methods on this problem *(compiler check of the
  printed tableaux)*; see [modified Patankar methods](/methods/modified-patankar-methods.md)).
* Buvoli & Minion's full KP run needed 256 nodes, so the convergence curves were computed
  serially and the achieved speedups extrapolated from a parallel run on $t\in[0,1]$ (§6.1–6.2).
  Printed slips: Table 4a lists the fine and coarse integrators swapped (ERK3 fine, ERK4 coarse,
  against the text), Fig. 13(b) shows the solution "at $t=8$" beyond the final time 4, §6 writes
  the line soliton as $2p^2\operatorname{sech}(\cdot)$ for $\operatorname{sech}^2$, and "256
  nodes (8096 compute cores)" should read 8192.

* Biswas & Ketcheson (2023) leave open why the two-soliton case does not show the
  three-soliton effect (§6.1.3).
* Tan et al. (2022) need the wind direction of the dispersive term to be fixed; a sign
  change inside a cell would need a spatially varying stabilization coefficient and a
  central flux, which they do not analyse (§2.2).

# Citations

- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §6 (Eqs. (32)–(39)), App. B, §6.1.1–6.1.3 (Table 1, Figs. 11–13), §7.
- [Tan et al. (2022)](/sources/tan-2022.md) — §1, §2.2, §4.2.1 (Eqs. (4.8)–(4.9), Tables 4.11–4.14), §4.2.2 (Eqs. (4.10)–(4.11), Tables 4.15–4.18).
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §4.1.4 (Eq. 43), §5.1.4, §5.2.4, §5.3 (Tables 4, 6, Figs. 9–10, 23–24); CSL technical report version.
- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — §6.1–6.2 (Eqs. 52–55, 58, Table 4a, Figs. 13–14); arXiv v2.
- [Buvoli & Southworth (2023)](/sources/buvoli-2023.md) — §6.1, §6.1.2 (Fig. 5); arXiv v2.
