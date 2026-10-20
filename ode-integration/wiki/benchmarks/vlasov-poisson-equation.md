---
type: Benchmark
title: "Vlasov–Poisson equation (Landau damping, two-stream instability)"
description: "The electrostatic Vlasov–Poisson system for a plasma distribution function, with the bump-on-tail, Landau-damping, two-stream and Penning-trap set-ups; the sources use it as a hyperbolic kinetic test for Parareal with exponential Runge–Kutta propagators and with particle-in-Fourier and particle-in-cell propagators."
status: established
aliases: [Vlasov-Poisson system, Landau damping, two-stream instability, bump-on-tail instability, Penning trap]
tags: [kinetic, parallel, exponential, verification]
timestamp: 2026-10-20T10:00:00Z
---

# Vlasov–Poisson equation (Landau damping, two-stream instability)

The **Vlasov–Poisson system** evolves the phase-space distribution $\mathfrak f(x,v,t)$
(page-local, to keep $f$ for the right-hand side) of electrons in their self-consistent
electric field $E=-\nabla\phi$:

$$\partial_t\mathfrak f+v\cdot\nabla_x\mathfrak f+\frac{q_e}{m_e}\big(E+v\times B_{\mathrm{ext}}\big)\cdot\nabla_v\mathfrak f=0,\qquad-\Delta\phi=\frac{\rho_e-\rho_i}{\varepsilon_0},$$

with an immobile neutralizing ion background $\rho_i$ and optional external fields
([Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md), §2; electron charge
$q_e$, mass $m_e$, permittivity $\varepsilon_0$ are page-local physical constants). In
normalized 1D–1V form, $\partial_t\mathfrak f+v\,\partial_x\mathfrak f+E\,\partial_v\mathfrak f=0$, $\partial_xE=-1+\int\mathfrak f\,dv$
([Buvoli & Minion (2024)](/sources/buvoli-2024.md), Eq. (56)). The free-streaming term is
hyperbolic, with purely imaginary spectrum after a Fourier transform in $x$; the problem is
non-diffusive, which is why the sources use it as a hard case for
[Parareal](/methods/parareal.md).

## Set-ups

| set-up | source | initial datum and parameters | discretization |
|---|---|---|---|
| bump-on-tail | Buvoli & Minion (2024), §6.3, Eq. (57), App. G | $\mathfrak f_0=\big(\frac{0.9}{\sqrt{2\pi}}e^{-v^2/2}+\frac{0.2}{\sqrt{2\pi}}e^{-2(v-4.5)^2}\big)\big(1+0.04\cos(0.3x)\big)$, $x\in[0,20\pi]$, $v\in[-8,8]$, $t\le50$ | 1024 Fourier modes in $x$, 1024 points in $v$; linear part $i\,\omega_xk_xv$ diagonal; [exponential Runge–Kutta](/methods/exponential-integrators.md) |
| Landau damping (weak) | Muralikrishnan & Speck (2025), §6.1.1 | $\mathfrak f_0=(2\pi)^{-3/2}e^{-\lvert v\rvert^2/2}\prod_{x_i\in\{x,y,z\}}(1+0.05\cos(0.5x_i))$ on $[0,4\pi]^3$, $T=19.2$ | 3D–3V particle-in-Fourier (PIF) or particle-in-cell (PIC) |
| two-stream instability | Muralikrishnan & Speck (2025), §6.1.2 | two Gaussian beams of width $0.1$ at $v_z=\pm\pi/2$, perturbation $1+0.01\cos(0.5z)$, $T=19.2$ | as above |
| Penning trap | Muralikrishnan & Speck (2025), §6.1.3 | $B_{\mathrm{ext}}=(0,0,5)$, quadrupole $E_{\mathrm{ext}}$, Gaussian particles in $[0,25]^3$; frequencies 4.875, 1.1, 0.125 (periods 1.29, 5.7, 50.3) | as above |

The particle runs advance particles with second-order kick–drift–kick velocity Verlet or the
Boris scheme; PIF deposits charge directly onto Fourier modes by nonuniform FFTs and is
charge-, momentum- and semi-discretely energy-conserving, while PIC deposits on a grid and
solves Poisson by FFT (§2–3).

## Results

**Exponential Parareal, bump-on-tail.** With $N=2048$ slices, ERK3 coarse and ERK4 fine
propagators and repartitioning, three coarse steps per slice converge monotonically to fine
accuracy in eight iterations, reaching error $6.6\times10^{-8}$ 24 times faster than serial
ERK4 in a measured run on 2048 cores, with model and measured speedup in close agreement. Two coarse steps fail to converge although the linear convergence analysis predicts
(barely) convergence; the authors' candidate reasons are the nonlinearity, the marginal
configuration and a possibly stiff nonlinear term $E\,\partial_v\mathfrak f$ (Buvoli &
Minion 2024, §6.3, Fig. 16). The gain is larger than for the dispersive KP equation (about
10×) because the problem has no highly oscillatory temporal components, so the coarse step
can be 21.3 times the fine step against 10.6 for KP (§6.3).

**Particle Parareal, error scalings.** The Parareal error follows the predicted scalings in
particles per cell, mesh width, nonuniform-FFT tolerance and, for Landau damping with the PIF
coarse propagator, the square of the coarse step per iteration; with the PIC coarse propagator
the Landau-damping error is dominated by particle noise and shows no convergence in the
coarse step. The two-stream instability behaves like Landau damping (Muralikrishnan & Speck
2025, §6.2, Figs. 1–5). The Penning trap converges only like the first power of the coarse
step, with no explanation; with time coarsening over the whole interval it converges so slowly
that Parareal must run in 16 blocks (§6.2.3, App. A.5).

**Particle Parareal, speedup.** On up to 1536 A100 GPUs (32 in space, 48 in time), the
speedup of the timed Parareal runs over space-only parallelization, whose reference time is
extrapolated from one 768-step Penning-trap run scaled by 8, is 4.2 (Landau damping), 4.7 (two-stream)
and 2.4 (Penning trap), and 5.8, 5.6, 4.4 with an order-7 B-spline shape function in the fine
propagator, at about $10^9$ particle pushes per second (§6.3, Fig. 6). The energy error of
Parareal iterates with the PIC coarse propagator is orders of magnitude larger than serial PIF
until convergence, while momentum is conserved to near machine precision in every iteration
(App. A.2, Figs. 8–9).

## Qualifications

- **Speedups measured against different baselines.** Buvoli & Minion's 24× is against serial
  ERK4 with the same fine step; Muralikrishnan & Speck's numbers are against spatial
  parallelization alone, with one reference time for all three set-ups, extrapolated from a
  Penning-trap run of one eighth of the steps (§6.3).
- **Penning-trap order.** The observed $O(h_{\mathcal G}^{k})$ instead of $O(h_{\mathcal G}^{2k})$
  ($h_{\mathcal G}$ the coarse step, page-local) is unexplained by the authors; see
  [Parareal](/methods/parareal.md).
- **Printed slips in Buvoli & Minion's §6.3.** The text labels the two configurations with
  $N_g=1$ and $N_g=2$ coarse steps, while Table 4b has $N_g\in\{2,3\}$, and the App. G
  integral is printed over $[0,20\pi]$ in $v$ although $v\in[-8,8]$ (recorded on the Source
  page).
- Both sources were read as arXiv v2 preprints.

# Citations

- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — arXiv v2: §6.3 (Eqs. (56)–(57), (60), Table 4b, Fig. 16); App. G.
- [Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md) — arXiv v2: §2–3; §6.1.1–6.1.3; §6.2 (Figs. 1–5); §6.3 (Fig. 6); App. A.2, A.5.
