---
type: Method
title: "Particle-mesh N-body in grid codes"
description: "Collisionless (dark-matter) particles coupled to a grid code by cloud-in-cell mass deposit, a mesh Poisson solve for the total gas-plus-particle density, and cloud-in-cell force interpolation, advanced by drift–kick–drift in Enzo and kick–drift–kick in Cholla; force-stencil and Green's-function choices change small-scale matter power by up to tens of per cent."
status: established
aliases: [particle-mesh, PM, cloud-in-cell, CIC, PM N-body, kick-drift-kick, drift-kick-drift]
tags: [self-gravity, cosmology, time-integration, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Particle-mesh N-body in grid codes

Cosmological grid codes carry collisionless matter as particles and
compute its gravity on the mesh: the particle mass is deposited onto the
grid, the Poisson equation is solved for the total density of gas and
particles, and the acceleration is interpolated back to the particles. In
comoving coordinates the source is $\frac{4\pi G}{a}$ times the total
density minus its mean
([Bryan et al. (2014)](/sources/bryan-2014.md), §2.1, eq. 8;
[Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.4, eq. 16).

## Deposit and interpolation

* **Cloud-in-cell (CIC).** Both codes deposit particle mass with CIC
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §5.2;
  [Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.5). In
  [Cholla](/software/cholla.md) the 1D weight of a cell is one minus the particle–cell-centre
  distance divided by $h$, for distances below $h$ (eq. 25).
* **Same kernel both ways.** Cholla interpolates the force to the
  particles with the same CIC weights "to avoid self-forces"
  ([Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.5).
* **Force softening.** In [Enzo](/software/enzo.md)'s point-source gravity test the force
  rolls over at about 1.6 fine cell widths (0.8 root widths), which the
  paper calls consistent with CIC; tangential errors drop on the fine grid
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.6, Fig. 10).
  Enzo's effective force resolution is about twice the cell size (§5.1).
* CIC is also used outside the N-body setting: FLASH sink particles take
  the gas-to-sink acceleration by first-order CIC interpolation of the
  mesh acceleration ([Federrath et al. (2010)](/sources/federrath-2010.md),
  §2.4.2; see [sink particles](/methods/sink-particles.md)).

## Mesh solve and force stencil

* **Enzo** solves the root grid by FFT, periodic with either the
  continuous Green's function (minus the inverse squared wavenumber) or a
  finite-difference one (eq. 61), or isolated by the James (1977) method;
  subgrids use multigrid ([Bryan et al. (2014)](/sources/bryan-2014.md),
  §5.1; see [Poisson solvers for self-gravity](/methods/multigrid-self-gravity.md)).
* **Cholla** solves by FFT on its uniform grid with the Green's function
  of the second-order centred discrete Laplacian (Hockney & Eastwood
  1988), using the PFFT library, and differences the potential at fourth
  order,
  $$g_{x,i} = -\frac{1}{12h}\left(\Phi_{i-2} - 8\Phi_{i-1} + 8\Phi_{i+1} - \Phi_{i+2}\right)$$
  ([Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.4,
  eqs. 17–19; the paper writes the derivative of the potential, the sign
  here follows $\mathbf g = -\nabla\Phi$).
* **Sensitivity** (same source, §3.2, Fig. 2). In a dark-matter-only
  comparison ($256^3$ particles on a $256^3$ grid), switching Cholla to a
  second-order potential gradient (eq. 40, to match Nyx) changes the
  small-scale matter power spectrum by about 15 %; switching between the
  discrete-Laplacian and the continuous Green's function (the latter to
  match Enzo) changes it by "as much as ≈ 28%". With each code's stencil
  and Green's function matched, Cholla agrees with Nyx, Ramses and Enzo to
  sub-per-cent levels (Nyx about 0.05 % at small scales, Ramses about
  0.7 % at small scales by redshift 0, Enzo below 0.3 %). The sub-per-cent
  agreement thus required matching each code's gradient stencil and
  Green's function.

## Time integration

* **Enzo: drift–kick–drift** (eq. 62). Before the deposit, positions are
  advanced by half a step with the old velocity for time-centring.
  Particles live on the finest grid covering them and take that level's
  time step ([Bryan et al. (2014)](/sources/bryan-2014.md), §5.2). In the
  orbit test ($32^3$, a test particle at 0.3 box lengths from a unit-mass
  primary, 200 orbits) the mean specific energy has a standard deviation
  of 0.276 % and a maximum deviation of 0.546 % (§11.2.7, Fig. 11).
* **Cholla: kick–drift–kick** after Miniati & Colella (2007), in comoving
  form: a half kick with the acceleration at $t^n$, a full drift with the
  half-step velocity divided by the half-step scale factor, and a half
  kick with the acceleration at $t^{n+1}$ (eqs. 26–28). The paper states
  that it allows variable time steps and, being symplectic, "conserves an
  integral of motion on average"; none of the paper's tests (§3) isolates
  the particle integrator
  ([Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.5). The
  particle time step is a Courant-like limit with coefficient 0.3 on the
  cell size over the particle speed, combined with the gas and expansion
  limits into one global step (§2.8, eqs. 33–35).
* The two papers do not compare the integrators with each other.

## Placement in the step

Cholla orders the step as: time step; extrapolate the potential to the
half step; hydrodynamic update; gravity source terms; chemistry; particle
kick and drift; CIC deposit; Poisson solve for the new potential; new
acceleration; final particle kick. The FFT solver and the particles run on
the host CPUs, the hydrodynamics on the GPUs
([Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.9).

# Citations

1. [Bryan et al. (2014)](/sources/bryan-2014.md), §§2.1, 5.1–5.2, 11.2.6–11.2.7, eqs. 8, 61–62 (arXiv v1).
2. [Villasenor et al. (2021)](/sources/villasenor-2021.md), §§2.4–2.5, 2.8–2.9, 3.2, eqs. 16–19, 25–28, 33–35, 40 (arXiv v2).
3. [Federrath et al. (2010)](/sources/federrath-2010.md), §2.4.2.
