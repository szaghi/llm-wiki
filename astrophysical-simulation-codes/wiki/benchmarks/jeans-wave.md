---
type: Benchmark
title: "Jeans wave"
description: "A small-amplitude self-gravitating sound wave, oblique to a periodic 3D grid, whose Jeans dispersion relation gives a stable oscillation or exponential growth depending on wavelength; it measures the order of accuracy of coupled hydrodynamics and self-gravity, the effect of Poisson-solver error, and energy conservation through collapse."
status: established
aliases: [Jeans linear wave, Jeans instability test]
tags: [benchmark, self-gravity, hydro, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Jeans wave

**Set-up.** A uniform, self-gravitating gas carries a plane sound wave of
relative amplitude $10^{-6}$ whose wavevector is oblique to a periodic 3D
grid. Linearizing the hydrodynamic equations with the Poisson equation
$\nabla^2\Phi = 4\pi G\rho$ gives a dispersion relation in
which the squared angular frequency equals $c_s^2$ times the squared
wavenumber minus $4\pi G\rho$ ([Tomida & Stone (2023)](/sources/tomida-2023.md),
eq. 33; [Mullen et al. (2021)](/sources/mullen-2021.md), eq. 87). The wave
oscillates when its wavelength is below the Jeans length and grows
otherwise; the ratio of wavelength to Jeans length is the control
parameter (Tomida & Stone set $G$ through it).
It is the self-gravitating analogue of the
[linear wave convergence test](/benchmarks/linear-wave-convergence.md).

## Stable wave (wavelength half the Jeans length in both)

* [Tomida & Stone (2023)](/sources/tomida-2023.md), §4.3, Fig. 10. Box
  $1\times0.5\times0.5$, wavevector $(2\pi, 4\pi, 4\pi)$ (wavelength
  1/3), $\rho = p = 1$, adiabatic $\gamma = 5/3$ with an
  isothermal perturbation; PLM, VL2, HLLC; gravity from the
  [multigrid Poisson solver](/methods/multigrid-self-gravity.md). The RMS
  of the L1 errors of density, momentum and total energy is about second
  order. With a single FMG sweep and no further V-cycles it is "precisely
  second order" and dominated by the gravity error; with a fully converged
  potential the error is smaller but slightly below second order, which
  the authors attribute to the slope limiter.
* [Mullen et al. (2021)](/sources/mullen-2021.md), §4.2.1, eqs. 84–89,
  Fig. 3. Gardiner–Stone geometry: domain $(3, 3/2, 3/2)$ with
  $2N\times N\times N$ cells, wavevector along $(1/3, 2/3, 2/3)$, wavelength
  1, $\rho = 1$, $p = 1/\gamma$, $\gamma = 5/3$; one period; $N = 8$ to
  256; FFT Poisson solver; HLLC; error is the volume-averaged L1 norm of
  density (eq. 89). Strictly second order for all six combinations of
  VL2, RK2 or RK3 with PLM or PPM; the higher-order options almost always
  give lower errors at fixed $N$ (L1 from about $10^{-6}$ to $10^{-10}$ in
  Fig. 3).

## Unstable wave (collapse)

* [Tomida & Stone (2023)](/sources/tomida-2023.md), §4.3, Fig. 11.
  Wavelength 1.1 Jeans lengths, $t = 1.5$. A converged potential keeps
  the growth symmetric, while a single FMG sweep without V-cycles breaks
  the symmetry and fragments early: in noise-sensitive problems the
  gravity error must be controlled. The stripes in Fig. 11a come from loss
  of significance, not from the solver.
* [Mullen et al. (2021)](/sources/mullen-2021.md), §4.2.2, eq. 90, Fig. 4.
  Wavelength 3/2 Jeans lengths. The gas collapses to a sheet at about 3
  and to filaments at about 7 Jeans-length sound-crossing times, run to
  about 10. Kinetic, thermal and gravitational energies vary by factors of
  about 20 or more of the initial thermal energy, yet the total energy
  (with the gravitational energy of eq. 32) is conserved to round-off: its
  relative change stays within $\pm1\times10^{-13}$ (Fig. 4). Total linear
  momentum is also conserved.

**What it shows.** Coupled hydro–gravity schemes reach second order on
oblique grids; the residual error of an iterative Poisson solver can
dominate the hydrodynamic error and seed spurious fragmentation
([Tomida & Stone (2023)](/sources/tomida-2023.md), §4.3); and a
conservative gravity coupling holds total energy to round-off through
nonlinear collapse ([Mullen et al. (2021)](/sources/mullen-2021.md),
§4.2.2).

# Citations

1. [Tomida & Stone (2023)](/sources/tomida-2023.md), §4.3 (arXiv v1).
2. [Mullen et al. (2021)](/sources/mullen-2021.md), §4.2 (arXiv v1).
