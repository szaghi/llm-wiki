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

## Later uses (batch 2): 1D and 2D variants

[Jiang et al. (2013)](/sources/jiang-2013.md) run the test in 1D and 2D in
[Athena](/software/athena.md) to verify their conservative total-energy
coupling (see [conservative self-gravity](/methods/conservative-self-gravity.md)):
CTU, HLLC, Courant number 0.8, uniform cells, periodic boundaries, FFT
Poisson solver (Table 1, §5). Background uniform and adiabatic with
$c_s^2 = \gamma p/\rho$, $\gamma = 5/3$, relative density perturbation
$10^{-6}$; the dispersion relation is the one above (eq. 17), with Jeans
length $\sqrt{\pi c_s^2/(G\rho)}$. "Non-conservative" (nc) below means
their variant with the conservative momentum flux but a source-form energy
update.

**Stable wave** (wavelength half the Jeans length; error after one
period, relative L2 norm, eq. 18):
* 1D (§4.1.1, sims. B–F, Fig. 1 right): 32 to 512 cells per Jeans length;
  the error of $\Phi$ converges at second order. Total energy (eq. 19) is
  conserved to round-off; the nc algorithm also conserves energy "to very
  high precision" in 1D.
* 2D oblique, wavevector components equal (§4.1.2, sims. B2–F2, Fig. 2):
  $23^2$ (wavelength 16 cells) to $362^2$ (256 cells); the density error
  converges at second order, from about $10^{-7}$ to about $10^{-10}$ as
  read from the figure; the nc algorithm is "essentially identical" (not
  plotted).

**Unstable wave** (wavelength twice the Jeans length):
* 1D growth (§4.1.1, sim. A, Fig. 1 left): 256 cells (Jeans length 128
  cells); the volume integral of $\Phi^2$ follows the linear growth rate
  until saturation.
* 2D collapse (§4.1.2, sims. H–O, Jc; Table 2, Figs. 3–5): the
  perturbation is raised by 2 % at the box centre relative to the edges to
  force collapse to a single filament. With the conservative scheme total
  energy is conserved to round-off, also on a Mach 10 advected background
  ($91^2$, sim. P). The nc scheme's fractional total-energy error between
  the start and virialization is 0.65, 0.32, 0.18, 0.09, 0.05 for
  $\gamma = 5/3$ ($22^2$ to $362^2$ cells) and 0.09, 0.05, 0.03 for
  $\gamma = 4/3$, "roughly $O(1/N)$"; the error accumulates where kinetic
  energy peaks (Fig. 3), and the nc clump becomes asymmetric and rotates
  from zero angular momentum (Fig. 5). Recorded as printed: Fig. 5 is at
  "t = 1.1" without units, inconsistent with the time scale of Figs. 3–4;
  the text announces "three snapshots" in Fig. 4 and lists four.

These variants are grid-aligned (1D) or have equal wavevector components
(2D), unlike the oblique 3D
set-ups above, and use the unstable wavelength 2 Jeans lengths rather than
1.1 or 1.5.

# Citations

1. [Tomida & Stone (2023)](/sources/tomida-2023.md), §4.3 (arXiv v1).
2. [Mullen et al. (2021)](/sources/mullen-2021.md), §4.2 (arXiv v1).
3. [Jiang et al. (2013)](/sources/jiang-2013.md), §§4.1, 5, Tables 1–2 (arXiv v2).
