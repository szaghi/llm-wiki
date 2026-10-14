---
type: Definition
title: "Magnetic nozzle"
description: "A diverging applied magnetic field that guides an expanding plasma and converts electron thermal energy into directed ion momentum, its reaction force acting on the field coils or magnets; models range from analytic thrust integrals and 1D kinetic solutions to 2D collisionless fluid models, and plasma detachment from the field lines remains unsettled."
status: established
aliases: [magnetic plasma nozzle, MN, magnetic nozzle expansion]
tags: [magnetic-nozzle, helicon, plume, fluid, kinetic]
timestamp: 2026-10-14T00:00:00Z
---

# Magnetic nozzle

A magnetic nozzle is a diverging, applied magnetic field downstream of a
plasma source. It confines and guides the expanding plasma, and converts
the thermal energy of the electrons, which carry most of the energy in the
low-pressure, $T_e\gg T_i$ plasmas of radiofrequency thrusters, into axial
ion momentum ([Takahashi (2019)](/sources/takahashi-2019.md), §2, §4). It
is the acceleration stage of [helicon plasma thrusters](/definitions/helicon-plasma-thruster.md),
of VASIMR (where ion-cyclotron-heated perpendicular ion energy is converted
to axial energy) and of ECR thrusters (§2). The reaction to the thrust
gained in the nozzle acts on the field coils or permanent magnets (§4).

## How thrust arises

The nozzle contribution is the Lorentz force between the radial field
component $B_r$ and the azimuthal electron current, which in the reviewed
measurements is dominated by the electron-diamagnetic current; see
[thrust decomposition of a magnetic nozzle](/results/magnetic-nozzle-thrust-decomposition.md)
for $F=F_s+F_B+F_w$ and its measurements
([Takahashi (2019)](/sources/takahashi-2019.md), §4, §5.5).
[Takahashi (2019)](/sources/takahashi-2019.md), §4 and §5.5.2, reports that
the 2D fluid model of Ahedo & Merino (2010) concluded that the main force
on the nozzle comes from the electron Hall current, whereas the measured
azimuthal current in HPT-I (Takahashi et al. 2016) is dominated by the
diamagnetic term; the review takes the diamagnetic side. Both positions are
reported through this one review.

## Electron thermodynamics in the expansion

* **Polytropic closure.** Electron cooling in the nozzle is described by
  $T_e\propto n_e^{\gamma-1}$; see
  [polytropic electron closure](/definitions/polytropic-electron-closure.md).
  [Takahashi (2019)](/sources/takahashi-2019.md), §5.7, reports measured
  values $\gamma\sim1$–1.2 (Sheehan et al. 2014; Zhang et al. 2016; Little &
  Choueiri 2016) and $\gamma\sim1.17$ for non-Maxwellian distributions, and
  two later measurements (Takahashi et al. 2018; Kim et al. 2018) in which
  trapped electrons are isothermal ($\gamma\sim1$) and free electrons nearly
  adiabatic ($\gamma\to5/3$). The effective $\gamma$ remains open.
* **Kinetic justification.** In the paraxial kinetic nozzle model reported by
  [Ahedo (2023)](/sources/ahedo-2023.md) (Eqs. 47–53, Fig. 5), electrons
  form reflected, free and doubly trapped populations yet satisfy the
  paraxial fluid equations. Far downstream the parallel heat flux is
  convective, proportional to the parallel enthalpy flux, which yields a
  polytropic law for the parallel temperature that also depends on $B$;
  the fitted exponent is $\gamma-1=0.23$, the perpendicular temperature
  tends to zero and the parallel one to a finite value. The potential falls
  to about $-3\,T_{e0}/e$ by 400 normalized lengths (read from the figure),
  where $T_{e0}$ is the upstream temperature.
* **Anomalous parallel cooling.** A Fourier law with an added anomalous
  parallel collisionality, 10–100 times the collisional one, recovers the
  observed parallel cooling in an electrodeless thruster (Ahedo, Eq. 64,
  citing Zhou et al.); its stated origin is the emptying of regions of the
  electron velocity distribution.

## Fluid models

* **2D collisionless, polytropic.** With isotropic polytropic electrons and
  no collisions, the electron equations of [Ahedo (2023)](/sources/ahedo-2023.md),
  Eqs. 54–60, become algebraic: no electron current across the magnetic
  surfaces, parallel current proportional to $B$ along each surface, the
  combination $\phi-\frac{\gamma}{\gamma-1}\frac{T_e}{e}$ constant on each
  surface (the polytropic analogue of the
  [thermalized potential](/definitions/thermalized-potential.md)), and
  isorotation of the electrons. The electron current then follows without
  an Ohm's law; ions are solved by the method of characteristics.
* **Two-fluid momentum balance.** The thrust integrals of
  [Takahashi (2019)](/sources/takahashi-2019.md), §4, Eqs. 10–20, rest on a
  steady axisymmetric two-fluid balance with cold ions, inertialess
  electrons, quasi-neutrality and the radial ion inertia neglected.
* **Hybrid codes.** [HYPHEN](/software/hyphen.md) and the 3D plume code
  EP2PLUS ([hybrid PIC–fluid model](/methods/hybrid-pic-fluid-model.md)) treat electrodeless-thruster nozzles and
  plumes with fluid electrons and PIC ions ([Ahedo (2023)](/sources/ahedo-2023.md),
  Figs. 2, 7). For the HYPHEN ECR thruster case, with a plume domain of 3–4
  channel widths, there is "practically no cooling along the magnetic
  lines" (p. 21).
* **Quasi-1D kinetic ions.** [Gallo et al. (2021)](/sources/gallo-2021.md),
  §3, §4.4, follow heavy-species macroparticles along the outermost field
  line of a helicon nozzle (0–0.6 m, 2000 nodes) with
  [Boltzmann electrons](/methods/boltzmann-electron-model.md) whose density
  scales with the inverse square of the local duct radius, and solve a
  nonlinear 1D Poisson equation. Results are on the
  [current-free double layer](/definitions/current-free-double-layer.md)
  page.
* [Takahashi (2019)](/sources/takahashi-2019.md), §4, states that the
  wave-propagation and plasma-flow models of the nozzle "have not been
  compared with the experiments yet".

## Detachment

The plasma must leave the closed field lines for the thrust to be net.
[Takahashi (2019)](/sources/takahashi-2019.md), §5.8, reviews three
mechanisms, all attributed to others, and calls the question "still in
argument":

* **Ion detachment** by demagnetization, observed as beam deviation about
  10 cm downstream, a 20° divergence at the beam edge, and streamline
  detachment measured by a calibrated Mach probe.
* **Electron detachment** by cross-field transport: Hooper (1993) gives a
  perpendicular electron drift, relative to the flow speed, scaling as the
  product of the electron and ion gyroradii computed with the flow speed,
  over the squared field-line curvature radius (Eq. 31);
  Ahedo & Merino recast it as outward diffusion with ion demagnetization;
  turbulence-driven anomalous diffusion is also proposed.
* **MHD detachment** by field-line stretching when the flow becomes
  super-Alfvénic, $M_A>1$ (Arefiev & Breizman 2005). In pulsed experiments
  up to 5 kW (Takahashi & Ando 2017) the plasma-induced field changes from
  a decrease of $B_z$ near the exit to an increase (stretching) farther
  downstream at $M_A\sim0.2$–0.25; the review's dimensional analysis of
  ideal MHD (Eqs. 32–36) gives 0.3–0.4, and the field change is only a few
  percent of the applied field. The review calls the agreement
  "qualitative".

# Citations

1. [Takahashi (2019)](/sources/takahashi-2019.md), §2, §4, Eqs. 10–20, §5.5, §5.7, §5.8, Eqs. 31–36.
2. [Ahedo (2023)](/sources/ahedo-2023.md), Eqs. 47–60, Eq. 64, Figs. 2, 5, 7.
3. [Gallo et al. (2021)](/sources/gallo-2021.md), §3, §4.4, Eqs. 13–18.
