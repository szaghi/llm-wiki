---
type: Benchmark
title: "Double Mach reflection"
description: "Woodward and Colella's Mach 10 shock reflecting off a 30-degree wedge, run to t = 0.2; the sources use it to measure the cost of asynchronous local time stepping against a global step and the start-up transient that error-based step-size control handles while CFL-based control crashes."
status: established
aliases: [DMR, double Mach reflection problem, Woodward–Colella double Mach reflection]
tags: [verification, step-size-control, ssp, multirate]
timestamp: 2026-10-20T05:00:00Z
---

# Double Mach reflection

The double Mach reflection problem of Woodward and Colella, as both sources set it up,
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

## What it shows

* **Cost of a global step.** Synchronous SSPRK(3,3) takes 169,499 s, asynchronous ARK3
  85,502 s and ARK3/AAMR 4,643 s, speed-ups of 1.98 and 36.51 (Unfer 2021, §4.5). The
  time-averaged asynchronous speed-up number, the operation saving a perfectly efficient
  cell-wise scheme would achieve, is 4.6 without and 144 with AMR. The measured gain is
  thus about 0.43 of the theoretical one without AMR and about a quarter with it
  *(compiler ratios)*; Unfer attributes the shortfall to random memory access (§3.1), and
  he uses the AMR ratio $144/36.51\approx4$ to project the gain of a reacting run (§4.7). ARK3 also shows more slip-line roll-ups than SSPRK(3,3) at equal mesh, which he
  reads as lower numerical dissipation (§4.5, Conclusion). See
  [local time stepping](/methods/local-time-stepping.md).
* **Cold start.** With error-based control the step starts much smaller and needs about
  100 steps to reach its asymptotic effective CFL number, automatically; CFL-based
  control "crashes in the first few steps even with $\nu=0.01$" (Ranocha et al. 2025,
  §5.1, Fig. 7). See [step-size control](/methods/step-size-control.md).

## Qualifications

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
