---
type: Software
title: "MIPS"
description: "Nonlinear full-MHD initial-value code on a cylindrical (R, φ, Z) finite-difference grid with third-order upwind convection, fourth-order central differences and explicit RK4, whose numerics are shared by the fluid part of MEGA; benchmarked against the ideal stability code MINERVA on an n = 3 infernal mode and extended to stellarators."
status: established
aliases: [MIPS code]
tags: [code, mhd, full-mhd, finite-differences, tokamak, stellarator, verification]
timestamp: 2026-10-16T12:00:00Z
---

# MIPS

MIPS is a nonlinear full-MHD initial-value code (Todo et al. 2010, as cited
by [Sato et al. (2024)](/sources/sato-2024.md), §2). In Sato et al. it is
the MHD reference against which the
[kinetic-thermal-ion](/methods/kinetic-thermal-ions.md) runs of
[MEGA](/software/mega.md) are compared, and the fluid part of MEGA uses the
same numerics (§2).

## Model

Visco-resistive full MHD with a scalar pressure
([Sato et al. (2024)](/sources/sato-2024.md), Eqs. 1–5):

$$\begin{aligned}
\rho\frac{\partial\mathbf v}{\partial t}&=-\rho(\mathbf v\cdot\nabla)\mathbf v-\nabla p+\mathbf J\times\mathbf B-\nabla\times(\nu\rho\nabla\times\mathbf v)+\tfrac43\nabla(\nu\rho\nabla\cdot\mathbf v),\\
\frac{\partial p}{\partial t}&=-\nabla\cdot(p\mathbf v)-(\Gamma-1)p\nabla\cdot\mathbf v+(\Gamma-1)\nabla\cdot\left[\kappa\nabla(p-p_{\mathrm{eq}})\right],\\
\mathbf E&=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_{\mathrm{eq}}),\qquad\frac{\partial\mathbf B}{\partial t}=-\nabla\times\mathbf E,\qquad\mu_0\mathbf J=\nabla\times\mathbf B,
\end{aligned}$$

with $\nu$ a kinematic viscosity and $\kappa$ an isotropic thermal
diffusivity. Resistive and thermal dissipation act on the perturbations
only ($p-p_{\mathrm{eq}}$, $\mathbf J-\mathbf J_{\mathrm{eq}}$). No
continuity equation is printed (the density is initially uniform) and no
Ohmic-heating term appears (recorded on the Source page).

## Numerics

- **Grid.** Cylindrical $(R,\phi,Z)$ finite differences (the paper writes
  $r$ for the major radius). [Nikulsin et al. (2022)](/sources/nikulsin-2022.md)
  (§I) likewise single out MIPS as the stellarator-capable code using a
  cylindrical grid rather than a flux-surface-aligned one.
- **Spatial scheme.** Convection terms by the Kawamura–Kuwahara third-order
  upwind scheme (Kawamura & Kuwahara 1984, as cited); all other terms by
  fourth-order central differences
  ([Sato et al. (2024)](/sources/sato-2024.md), §2).
- **Time integration.** Explicit fourth-order Runge–Kutta (§2).
- **Toroidal wedge.** For the $n=3$ runs, $\phi\in[0,2\pi/3]$ with periodic
  boundaries, so only $n=3$ and its harmonics are kept; default grid
  $256\times48\times256$ in $(R,\phi,Z)$ (§2).
- **Hardware.** NIFS Plasma Simulator (NEC SX-Aurora TSUBASA vector
  engines) and Fugaku; no GPU and no run times are reported (§2,
  Acknowledgements). Wall boundary conditions are not stated.

## Verification: MIPS against MINERVA

On the $n=3$ ideal [infernal mode](/definitions/infernal-mode.md) of a
circular $\beta_0=5.7\%$ equilibrium, with $\nu=\kappa=0$, the MIPS growth
rate approaches the MINERVA ideal eigenvalue ($\approx0.0057\tau_A^{-1}$,
$\tau_A=R_0/v_A$) at high $S$, and the radial velocity of MIPS matches the
MINERVA displacement structure: dominant $m=4$, $m=5,6$ outward, $m=3$
inward ([Sato et al. (2024)](/sources/sato-2024.md), §3.1.1, Figs. 2–3).
The $(256,64,256)$ and $(512,64,512)$ meshes give "almost identical"
results; the coarse $(128,64,128)$ mesh is about 20% high at $S\ge10^7$, and
the finer meshes sit about 5% above MINERVA at $S=10^8$ (figure reading).
The production runs use 48 toroidal points, fewer than the 64 of the
convergence test, without comment (recorded on the Source page). MINERVA is
one of the linear ideal codes listed on
[linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md).

## Stellarator extension

MIPS has been extended to stellarators, as cited by
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (§I) and by
[Ramasamy et al. (2024)](/sources/ramasamy-2024.md) (§1) among the
nonlinear stellarator MHD codes; neither paper compares with it.

# Citations

- [Sato et al. (2024)](/sources/sato-2024.md): model (Eqs. 1–5), numerics, the MINERVA benchmark, infernal-mode runs.
- [Nikulsin et al. (2022)](/sources/nikulsin-2022.md): MIPS as a cylindrical-grid stellarator MHD code.
- [Ramasamy et al. (2024)](/sources/ramasamy-2024.md): MIPS cited among stellarator extensions.
