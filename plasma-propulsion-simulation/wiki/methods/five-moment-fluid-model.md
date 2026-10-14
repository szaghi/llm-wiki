---
type: Method
title: "Five-moment electron fluid model"
description: "Non-neutral, inertial fluid model that evolves density, momentum and energy of electrons and ions with Poisson's equation, applied in 2D axial–radial to a Hall thruster with an energy-limited kinetic wall flux and two ion populations; on a shared set-up it gives a discharge current of 10.1 A against 14.7 A from PIC-MCC, for which its authors name the missing anisotropic electron pressure as the probable cause."
status: established
aliases: [5M model, five-moment model, five-moment fluid, inertial electron fluid model, full-fluid moment model]
tags: [fluid, hall-thruster, kinetic, pic, sheath, wall-interaction, numerics, verification]
timestamp: 2026-10-14T00:00:00Z
---

# Five-moment electron fluid model

The five-moment (5M) model keeps what the drift-diffusion
[electron fluid model](/methods/electron-fluid-model.md) drops: electron
inertia and charge separation. Each species carries density, momentum and
energy, and the potential comes from Poisson's equation.
[Troyetsky et al. (2026)](/sources/troyetsky-2026.md) apply it in 2D
axial–radial to a Hall thruster and compare it with an in-house PIC-MCC code
on the same set-up; an earlier 1D comparison (Yamashita et al.) agreed with
PIC-MCC in discharge current within 0.5 % (attributed, §Results).

**Naming.** Ahedo (2023, eqs. 1–3) calls a model with isotropic pressure and no
heat flux the closed isotropic adiabatic 5-moment model, and the same model
with a Fourier heat flux the 8-moment model. The 5M model of Troyetsky et al.
carries a Fourier heat flux for the electrons, so it is an 8-moment model in
Ahedo's count ([Ahedo (2023)](/sources/ahedo-2023.md), §3;
[Troyetsky et al. (2026)](/sources/troyetsky-2026.md), eqs. 3–5, 10–13).

## Equations

Per species $s$, with isotropic pressure $p_s=n_sT_s$ ($T_s$ in energy units)
([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), eqs. 3–5):
$$\begin{aligned}
&\partial_tn_s+\nabla\cdot(n_s\mathbf u_s)=(\text{source}),\\
&\partial_t(n_s\mathbf u_s)+\nabla\cdot\left(n_s\mathbf u_s\mathbf u_s+\frac{p_s}{m_s}\mathsf I\right)=\frac{q_sn_s}{m_s}\left(\mathbf E+\mathbf u_s\times\mathbf B\right)+(\text{collisional}),\\
&\partial_t\left[n_s\left(\tfrac32T_s+\tfrac12m_s|\mathbf u_s|^2\right)\right]+\nabla\cdot\left[n_s\left(\tfrac52T_s+\tfrac12m_s|\mathbf u_s|^2\right)\mathbf u_s+\mathbf q_s\right]=q_sn_s\mathbf E\cdot\mathbf u_s+(\text{collisional}).
\end{aligned}$$
Without the inertial term the steady state recovers drift-diffusion (p. 4).

* **Electron collisions** (eqs. 6–9). Krook momentum exchange with each other
  species; $\nu_e=\nu_{en}+(\text{inelastic})+\nu_{\mathrm{ano}}$ with
  $\nu_{en}=2.5\times10^{-13}\,n_n$ (after Boeuf & Garrigues); excitation and
  electron–ion Coulomb collisions neglected; ionization energy loss 12.13 eV
  (Xe), rate from Biagi v8.97 cross sections with a Maxwellian distribution.
* **Anomalous transport** (eq. 8). Bohm-type
  $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\omega_{ce}/16$, isotropic, with
  $\alpha_{\mathrm B}=0.16$ for $x<2.25$ cm, a linear ramp, and
  $\alpha_{\mathrm B}=4$ for $x\ge2.75$ cm (the paper's coefficients 0.01 and
  0.25 multiply $\omega_{ce}$). The authors call this step profile "not
  representative" of experimentally inferred ones and choose it for the
  benchmark. See
  [anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md).
* **Heat flux** (eqs. 10–13). Fourier law with a field-aligned conductivity
  tensor (Mitchner–Kruger), the perpendicular conductivity being the parallel
  one divided by $1+\Omega_e^2$; $\mathbf q_i=0$.
* **Two ion populations** (eqs. 14–26). High- and low-energy Xe$^+$ fluids.
  Ionization and charge-exchange products are split between them by a fraction
  that is piecewise linear in the local potential: 0 below 30 V and 0.999
  above 60 V, the non-unity value being needed for stability. Charge-exchange
  cross sections after Miller et al. See
  [charge-exchange ions](/definitions/charge-exchange-ions.md).
* **Poisson** (eqs. 40–41). Cell-centred potential, face fields, second-order
  central differences; HYPRE GMRES with a PFMG preconditioner, the same solver
  as the PIC code. Dielectric walls take a Neumann condition from the
  accumulated surface charge. Permittivity scaled with $f_\varepsilon=10$
  ($\varepsilon_0\to f_\varepsilon^2\varepsilon_0$), which the authors note
  affects sheath width, acceleration-region location and peak $T_e$ (see
  [permittivity, ion-mass and geometric scaling](/methods/pic-acceleration-scaling.md)).

## Energy-limited kinetic flux (ELKF) wall condition

The new boundary condition of the paper (eqs. 31–36). Wall fluxes of mass,
momentum and energy are one-sided moments of a drifting Maxwellian, integrated
not from zero normal speed but from the speed an electron needs to cross the
potential drop of half a boundary cell, $\sqrt{2e|\phi_b|/m_e}$ with $\phi_b$
the boundary field times half the cell size. This mimics the boundary field
and an unresolved virtual cathode under secondary emission. With a zero
threshold it reduces to the kinetic flux method. The authors call ELKF "a
robust solution" against SEE and inverse-sheath instabilities; without it the
5M model "eventually faced runaway electron emission" (p. 21), and the
abstract says it "plays a critical role in obtaining a steady-state solution".
See [secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md).

## Discretization

([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), §Numerical methods,
eqs. 37–39)
* Cell-centred finite volumes, uniform grid $\Delta x=0.1$ mm; MUSCL
  reconstruction of primitive variables with a van Leer limiter (second
  order).
* Interface flux: Steger–Warming flux-vector splitting with an entropy fix at
  sonic points; local Lax–Friedrichs splitting behaved similarly, global
  Lax–Friedrichs was too diffusive where wave speeds are low, near the cathode
  boundary.
* Time: explicit SSP-RK2 for electron mass and momentum and all ion equations.
  The electron energy equation is decoupled and semi-implicit, a θ-method with
  θ = 0.5 in which only the mean-energy diffusion is implicit, with lagged
  conductivity (as in Mikellides & Katz), because of "the severe timestep
  restriction imposed by the large field-aligned thermal conductivity".
  Collision sources are explicit.
* Time step: adaptive, CFL 0.4 and $\Delta t<0.4\cdot2\pi/\omega_{pe}$;
  average about 8 ps.
* MPI; about 3 days on 50 cores for 50 µs, against about 5 weeks on 100 cores
  for the PIC-MCC run of the same case.

## Comparison with PIC-MCC (shown)

Set-up shared by both codes: Cartesian $x$ (axial, $z$) – $y$ (radial, $r$),
azimuth $\theta$ normal to the plane; channel 2.5 cm × 1.5 cm, plume 2.5 cm ×
3.5 cm; $B_y$ Gaussian with peak 0.015 T (printed as 150 G) at the exit; Xe at 5 mg/s, 300 V;
quasi-steady neutral model that suppresses the 10–30 kHz breathing mode;
linear SEE yield for BN; same anomalous profile, cross sections and Poisson
solver ([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), §Simulation
setup, Fig. 1, eqs. 1, 42–43). PIC-MCC: $\Delta x=0.2$ mm, $\Delta t=10$ ps,
40 particles per cell per species initially, $W=1.068\times10^8$, Boris
push, null-collision MCC (see [PIC-MCC](/methods/pic-mcc.md)).

| Quantity | 5M | PIC-MCC |
|---|---|---|
| Discharge current | 10.1 A | 14.7 A |
| Peak $\phi$ | 319 V at $x\approx0.9$ cm | 310 V at $x=1.1$ cm |
| Peak plasma density | at $x=0.8$ cm | about 70 % higher, at $x=1.1$ cm |
| Peak $T_e$ | about 2.7 times lower than PIC-MCC | — |
| Field lines | isothermal | strongly non-isothermal |
| Space-charge-limited sheath near $x\approx2.1$ cm | absent | present, with trapped secondaries |

Sources: §Results, Figs. 4–9. The ion temperature maxima, 16 eV (5M) and
25 eV (PIC-MCC), are not explicitly labelled as ion values (p. 17).

**Momentum analysis** (eqs. 48–49, Figs. 10–11). In 5M the azimuthal drag
dominates the bulk, while inertial shear terms dominate in sheaths, near the
anode and at the anode–wall corners, where they produce lobes of current that
a drift-diffusion model would miss. In PIC-MCC, between $x=1.25$ and
2.25 cm, the axial momentum structure correlates most with the radial gradient
of the off-diagonal ($r\theta$) electron pressure component, which 5M lacks;
the authors name this anisotropic pressure, together with sheath kinetics, as
the probable cause of the current gap, and note that 5M numerical diffusion
could enhance its cross-field transport (p. 16).

**Conductivity study** (Figs. 12–15). Scaling the parallel conductivity by
1, 0.1, 0.01 and 0.005 raises the discharge current by only 0.1 A and makes
field lines non-isothermal, but degrades the electron current and velocity
fields; below 0.005, oscillations from neutral depletion appear. The authors
conclude that ad-hoc Fourier-law tuning is insufficient; unshown preliminary
results with a Dufour term from 9- and 14-moment closures reduce the
field-aligned heat flux without tuning (p. 29).

## Electron inertia elsewhere

Ahedo (2023, eqs. 37–43, Fig. 3) adds azimuthal electron inertia to a 1D axial
fluid model: it matters near the anode, around the cathode and in the near
plume, where it bounds the azimuthal electron velocity to the order of the
electron thermal speed, and changes $\phi$ and $T_e$ little. This motivated a
limiter on the azimuthal electron velocity in [HYPHEN](/software/hyphen.md)
([Ahedo (2023)](/sources/ahedo-2023.md), p. 14). A generalized Bohm criterion
for normal and inverse anode sheaths requires full electron inertia in the 1D
equations (Appendix).

# Citations

1. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), eqs. 1–49, Figs. 1–15, pp. 4, 16–19, 21, 26–29.
2. [Ahedo (2023)](/sources/ahedo-2023.md), §3, eqs. 1–3, 37–43, Fig. 3, p. 14, Appendix.
