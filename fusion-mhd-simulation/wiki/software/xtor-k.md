---
type: Software
title: "XTOR-K"
description: "Global hybrid code coupling two-fluid MHD to full-f, full-orbit (Boris–Buneman) kinetic ions through a kinetic pressure term, with the implicit Newton–Krylov fluid step and the particle push nested in a Picard iteration; in the NLED-AUG benchmark it reproduces the near-axis EPM at 166 kHz and the counter-rotating TAE at −196 kHz, but its growth rates are buried in full-f noise."
status: established
aliases: [XTOR-K code]
tags: [hybrid-kinetic, extended-mhd, energetic-particles, alfven-eigenmode, particles, time-integration, verification]
timestamp: 2026-10-16T18:35:00Z
---

# XTOR-K

XTOR-K is a global [hybrid kinetic-MHD](/methods/hybrid-kinetic-mhd.md) code
(Brochard 2020, 2025): two-fluid equations with bulk-ion and electron
temperature evolution, coupled to full-$f$ particle-in-cell kinetic ions
through a kinetic pressure term in the perpendicular equation of motion
([Vlad et al. (2025)](/sources/vlad-2025.md), §6).
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§I) list it among the
hybrid MHD–kinetic codes, and [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)
and [Zhang et al. (2021)](/sources/zhang-2021.md) (§1) mention its fluid
parent, XTOR-2F, among nonlinear MHD codes.

## Model and numerics

From Vlad et al. (2025), §6:
* **Coupling.** [Pressure coupling](/methods/pressure-and-current-coupling.md)
  in the perpendicular momentum equation; quasi-neutrality
  $n_e=Z_in_i+\sum_kZ_kn_k$ is imposed at every fluid step.
* **Time integration.** A fully implicit, preconditioned Newton–Krylov solver
  advances the fluid (see
  [implicit time integration](/methods/implicit-time-integration.md)); the
  kinetic ions are pushed by Boris–Buneman (full orbit, 24 steps per cyclotron
  period, 16 particle steps per fluid step; see
  [particle pushers](/methods/particle-pushers.md)). Both are nested in a
  Picard iteration at every fluid step until fluid and kinetic parts converge
  together, with velocity moments extracted after each fluid advance inside the
  iteration.
* **Grids.** The fluid uses $(s,\theta,\phi)$ with $s$ the square root of the
  initial poloidal flux (its normalization is not stated) and $\theta$ the
  geometric angle, FFTs in both angles and linear
  finite differences in radius ($204\times64\times8$ in the benchmark). The
  kinetic part uses a toroidal FFT and a Cartesian $(R,Z)$ grid ($400\times400\times8$);
  $3.072\times10^8$ markers initially.
* **Parallelism.** Radial domain decomposition for the fluid; domain cloning
  or decomposition for the kinetic part, decomposition being required with
  binary collisions.

## Benchmark restrictions and results

For the [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md) the fluid
model is restricted to ideal MHD with very small viscosity, and after every
fluid step only the $n=1$ component of the field increments is kept, whereas
XTOR-K normally evolves all $n$ including $n=0$ (Vlad et al. 2025, §6). The
abstract and §1 call the model "non-linear resistive two-fluid MHD"; the
benchmark configuration is the restricted one.

Results (Vlad et al. 2025, §6–7, Figs. 11–13):
* The full-$f$ Maxwellian initial distribution is not a kinetic equilibrium and
  relaxes within about 0.05 ms toward an ORB5-like profile; the other codes
  suppress this relaxation in their δf equations (§2, §6).
* The total energy is too noisy to use, so the 2/1 and 3/1 components of the
  radial velocity at two radii are tracked instead; no growth rate can be
  measured, because the linear phase is buried in full-$f$ PIC noise.
* An $m=2$-dominated [EPM](/definitions/energetic-particle-mode.md) near
  $s\approx0.2$, with linear growth ending at about 0.25 ms and 166 kHz in early
  saturation; a counter-rotating [TAE](/definitions/toroidal-alfven-eigenmode.md)
  at $s\approx0.4$ with $m=2,3$ of comparable amplitude at −196 kHz. The authors
  call these "in good agreement" with the other codes, but no nonlinear-phase
  frequencies of the other codes are tabulated (the linear values are 127–180
  kHz).
* EP flattening somewhat stronger than ORB5's, strong edge transport, and a
  profile almost frozen between 0.248 and 0.605 ms (Fig. 13).

## Limitations

* Full-$f$ noise hides the linear phase (Vlad et al. 2025, §6).
* The chirping of the XTOR-K EPM is not reported, so the chirping-direction
  spread between HYMAGYC/MEGA (down) and ORB5 (up) is not resolved by it (§3–6;
  recorded on the [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md)).
* Full-$f$ relaxation also complicates the JOREK energetic-particle benchmarks,
  which share the full-$f$ choice ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md),
  §IV A).

# Citations

1. [Vlad et al. (2025)](/sources/vlad-2025.md) — §1, §2, §§6–7, Figs. 11–13.
2. [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §I, §IV A.
3. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — code mentions.
4. [Zhang et al. (2021)](/sources/zhang-2021.md) — §1.
