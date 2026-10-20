---
type: Benchmark
title: "Double Mach reflection"
description: "Woodward and Colella's Mach 10 shock reflecting off a 30-degree wedge, run to t = 0.2; the sources use it to measure the cost of asynchronous local time stepping against a global step, the start-up transient that error-based step-size control handles while CFL-based control crashes, and single-stage Lax–Wendroff against Runge–Kutta flux reconstruction."
status: established
aliases: [DMR, double Mach reflection problem, Woodward–Colella double Mach reflection]
tags: [verification, step-size-control, ssp, multirate]
timestamp: 2026-10-20T16:00:00Z
---

# Double Mach reflection

The double Mach reflection problem of Woodward and Colella, as the sources set it up,
sends a Mach 10 shock in an ideal gas ($\gamma=1.4$, page-local) along a wall inclined
at 30° to it. In the usual rotated form the domain is $[0,4]\times[0,1]$, the wall starts
at $x=\tfrac16$ on the bottom boundary, and the data are, in page-local density,
pressure and velocity,

$$(\rho,p,u,v)=\begin{cases}\big(8,\ 116.5,\ 4.125\sqrt3,\ -4.125\big)&\text{behind the shock},\\ (1.4,\ 1,\ 0,\ 0)&\text{ahead of it},\end{cases}$$

integrated to $t=0.2$ ([Unfer (2021)](/sources/unfer-2021.md), §4.5). The reflected
shocks, the Mach stems and a slip line that rolls up into vortices make it a standard
test of shock capturing; for time integration it is a large, shock-dominated
computation with a strongly non-uniform admissible step.

## Configurations in the sources

* **Asynchronous local time stepping** (Unfer 2021, §4.5, Figs. 10–11): multi-slope
  MUSCL finite volumes, CFL 0.4, 3840×960 cells for the synchronous SSPRK(3,3) and the
  asynchronous ARK3 runs, and 240×60 cells with four levels of asynchronous AMR for
  ARK3/AAMR. Unfer notes an artefact at the top boundary, as Kemm did.
* **Error-based step-size control with AMR** ([Ranocha et al. (2025)](/sources/ranocha-2025.md),
  §5.1, Fig. 7): DGSEM of degree 4 with subcell shock capturing, an initial grid of 80
  uniform elements refined by p4est AMR every two steps, the Zhang–Shu positivity limiter
  after every stage, and the embedded pair SSP3(2)4[3S*$_+$].

* **Single-stage Lax–Wendroff against Runge–Kutta flux reconstruction**
  ([Babbar et al. (2022)](/sources/babbar-2022.md), §12, Figs. 41–43): degree 2 on
  $960\times240$ cells with a TVB limiter (parameter 100), the same post- and pre-shock
  states.
* **Lax–Wendroff with AMR and error-based steps** ([Babbar & Chandrashekar (2025)](/sources/babbar-2025.md),
  §6.1.3): degree 4, a $16\times5$ base mesh refined by a Löhner indicator up to six levels
  (80 to 2411 to 7793 elements, against 327,680 for the uniform finest mesh), error-based
  step-size control with the PID controller of Ranocha et al. at tolerances $10^{-6}$.

## What it shows

* **Cost of a global step.** Synchronous SSPRK(3,3) takes 169,499 s, asynchronous ARK3
  85,502 s and ARK3/AAMR 4,643 s, speed-ups of 1.98 and 36.51 (Unfer 2021, §4.5). The
  time-averaged asynchronous speed-up number, the operation saving a perfectly efficient
  cell-wise scheme would achieve, is 4.6 without and 144 with AMR. The measured gain is
  thus about 0.43 of the theoretical one without AMR and about a quarter with it
  *(compiler check, not in the source)*; Unfer attributes the shortfall to random memory access (§3.1), and
  he uses the AMR ratio $144/36.51\approx4$ to project the gain of a reacting run (§4.7). ARK3 also shows more slip-line roll-ups than SSPRK(3,3) at equal mesh, which he
  reads as lower numerical dissipation (§4.5, Conclusion). See
  [local time stepping](/methods/local-time-stepping.md).
* **Cold start.** With error-based control the step starts much smaller and needs about
  100 steps to reach its asymptotic effective CFL number, automatically; CFL-based
  control "crashes in the first few steps even with $\nu=0.01$" (Ranocha et al. 2025,
  §5.1, Fig. 7). See [step-size control](/methods/step-size-control.md).

* **One step versus many stages.** Lax–Wendroff flux reconstruction with time-averaged
  dissipation and face-extrapolated fluxes resolves the flow like Runge–Kutta flux
  reconstruction, and Runge–Kutta needs between about 1.1 and 1.6 times its wall-clock time,
  depending on the degree and grid (Babbar et al. 2022, Figs. 41–43); the limiter runs once per
  step instead of once per stage (§7). See
  [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md).
* **Error-based control of a single-stage method.** Babbar & Chandrashekar (2025) build the
  embedded solution of their one-stage scheme by truncating the time-averaged flux one order
  lower and dropping the interface terms; on this problem the method runs with the default
  tolerance, and the AMR keeps the element count below 2.4 % of the uniform mesh (§5.2, §6.1.3;
  see [step-size control](/methods/step-size-control.md)).

## Qualifications

* Babbar et al. (2022) and Babbar & Chandrashekar (2025) report no hardware for their timings
  and element counts.

* Unfer's baseline is his own code in synchronous mode, with the asynchronous data
  structures and their overhead (§4.1); the speed-ups are against that, not against an
  optimized synchronous code. The lower dissipation of ARK3 is inferred from contour plots
  only.
* The positivity limiter in Ranocha et al. (2025) acts after every stage and the AMR
  after accepted steps; both are callbacks, "not seen" by the error estimator
  (§5.1, Algs. 1–2, §8).

# Citations

- [Unfer (2021)](/sources/unfer-2021.md) — §3.1 (asynchronous speed-up number), §4.1, §4.5 (Figs. 10–11), §4.7, Conclusion.
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §5.1, Fig. 7; Algs. 1–2, §8 (callbacks unseen by the estimator).
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §7, §12 (Figs. 41–43); arXiv v1.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §5.2, §6.1.3; arXiv v4.
