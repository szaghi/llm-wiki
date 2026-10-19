---
type: Benchmark
title: "Gresho vortex"
description: "Stationary incompressible vortex with piecewise-linear velocity, run as a compressible flow at Mach numbers down to 10^-4 to test whether all-Mach IMEX and semi-implicit time integrators keep the vortex and its kinetic energy with a step independent of the Mach number."
status: established
aliases: [Gresho–Chan vortex, triangular vortex, low-Mach Gresho vortex]
tags: [imex, asymptotic-preserving, verification, stiff]
timestamp: 2026-10-19T23:00:00Z
---

# Gresho vortex

The **Gresho vortex** is a steady solution of the incompressible Euler equations: a
rotating vortex whose tangential velocity rises linearly to a peak and falls back, held in
balance by a radial pressure gradient. Run as a compressible flow with the background
pressure scaled by $1/\mathrm{Ma}^2$, it tests low-Mach
[asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) schemes: the time
step should not depend on the Mach number, the vortex should stay stationary, and its
kinetic energy should be kept ([Boscheri & Pareschi (2021)](/sources/boscheri-2021.md),
§4.3; [Orlando & Bonaventura (2025)](/sources/orlando-2025.md), §5.5).

## Set-up

Page-local symbols: radius $r$ from the vortex centre, tangential velocity $u_\theta$,
density $\rho$, pressure $p$, background pressure $p_0$, Mach number $\mathrm{Ma}$, ratio
of specific heats $\kappa$ (the registry reserves $\gamma$). With $\rho=1$ (Boscheri &
Pareschi 2021, §4.3):

$$u_\theta=\begin{cases}5r, & r<0.2,\\ 2-5r, & 0.2\le r<0.4,\\ 0, & r\ge0.4,\end{cases}\qquad
p=\begin{cases}p_0+\frac{25}2r^2, & r<0.2,\\ p_0+\frac{25}2r^2+4\big(1-5r-\ln0.2+\ln r\big), & 0.2\le r<0.4,\\ p_0-2+4\ln2, & r\ge0.4,\end{cases}$$

with $p_0=\rho/(\kappa\mathrm{Ma}^2)$, so the peak velocity is 1 and the pressure
fluctuation is $O(1)$ against a background $O(\mathrm{Ma}^{-2})$. The pressure is
continuous at $r=0.2$ and $r=0.4$ *(compiler check)*.

- **Boscheri & Pareschi (2021):** 3D domain $[-0.5,0.5]^3$ with Dirichlet boundaries,
  $80\times80\times4$ cells (also $h_x=1/40$), $\mathrm{Ma}=10^{-1},10^{-2},10^{-3}$, final
  time $0.4\pi$, Courant number 0.15 or 0.25 on the material speed, semi-implicit IMEX
  finite volumes of orders 2 and 3.
- **Orlando & Bonaventura (2025):** 2D domain $(0,1)^2$, periodic, $80\times80$ DG elements
  of degree 2, $h=2\times10^{-3}$, three rotations, $\mathrm{Ma}=10^{-3}$ and $10^{-4}$, with
  $p_0=\rho_0u_{\theta,\max}^2/(\kappa\mathrm{Ma}^2)$; ideal gas, a stiffened-gas water
  model and a Peng–Robinson gas (§5.5, Eqs. (115)–(119)).

## What it tests and results

- **Mach-independent step.** Boscheri & Pareschi run the same step at all three Mach
  numbers and the vortex is preserved (Fig. 9). Orlando & Bonaventura's step corresponds
  to an advective Courant number about 0.32 and acoustic Courant numbers about 320
  ($\mathrm{Ma}=10^{-3}$) and 3200 ($\mathrm{Ma}=10^{-4}$) (§5.5).
- **Kinetic energy.** Boscheri & Pareschi report $K/K_0$ at the final time of 0.997
  (second order) and 0.998 (third order) on the fine mesh, 0.984 and 0.988 on the coarse
  mesh, with nearly overlapping curves for the three Mach numbers (Fig. 10). Orlando &
  Bonaventura report relative kinetic energy 0.999981, 0.999977, 0.999968 after one, two and
  three rotations for the ideal gas at both Mach numbers, 0.999984–0.999977 for water and
  0.999981–0.999968 for Peng–Robinson (Tables 6–8), against a loss of about 1.5% after one
  rotation that they quote for two earlier schemes.

The time integrators are the semi-implicit SA DIRK(3,4,3) and SA SSP(3,3,2) pairs
([semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md)) in Boscheri
& Pareschi, and a Kennedy–Carpenter third-order
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) pair with a Picard-iterated pressure
equation in Orlando & Bonaventura.

## Qualifications

- The kinetic-energy figures mix time and space errors and differ in mesh, order, domain,
  boundary conditions and final time; they are not a comparison of the time integrators.
- Boscheri & Pareschi write $M=2,3$ for the order of the reconstruction in the same section
  where $M$ is the Mach number (§4.3), and their reference for the vortex is printed without
  venue or year.

# Citations

- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §4.3 (Figs. 9–10); arXiv v1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §5.5 (Eqs. (115)–(119), Tables 6–8); HAL v2.
