---
type: Benchmark
title: "Zel'dovich pancake"
description: "A 1D cosmological test in which a single sinusoidal mode collapses into a caustic in an expanding matter-only background, forming shocks around a dense central sheet; it checks comoving hydrodynamics with gravity and discriminates between dual-energy switches."
status: established
aliases: [Zeldovich pancake, Zel'dovich pancake test, pancake collapse]
tags: [benchmark, cosmology, hydro, self-gravity, dual-energy, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Zel'dovich pancake

**Set-up.** A one-dimensional box in comoving coordinates (scale
factor $a$) holds one sinusoidal perturbation whose wavelength equals the
box size. The initial density, velocity and temperature are given in
Lagrangian form, so that the mode reaches its caustic (the "pancake") at a
prescribed caustic redshift, after which shocks bound a dense central
sheet. The background is matter-only
(matter density parameter 1), with initial temperature 100 K. Both runs
below use a box of $64$ Mpc in units of the dimensionless Hubble parameter
(value 0.5), start at redshift 20 and end at redshift 0
([Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.9, eqs. 105–107,
after Anninos et al. 1994;
[Villasenor et al. (2021)](/sources/villasenor-2021.md), §3.1,
eqs. 36–39). Both take the background density as the critical density
(Bryan et al., Fig. 12 caption, with a background temperature of 100 K).
Villasenor et al. state the caustic redshift as 1 and an initial
temperature that scales with density to the power $2/3$. The formulas are
on the Source pages.

Villasenor et al. use it to test the choice of
[dual-energy formalism](/methods/dual-energy-formalism.md) (below).

## Runs

* **[Enzo](/software/enzo.md)**
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.9, Fig. 13):
  64 root cells, refinement ratio $r_{\mathrm{ref}} = 4$, 2 levels
  (effective resolution 1024), PPM. The shocks and the central peak are
  resolved "at the correct locations". The comparison is qualitative; no
  error norm is printed.
* **[Cholla](/software/cholla.md)**
  ([Villasenor et al. (2021)](/sources/villasenor-2021.md), §3.1, Fig. 1):
  stated to replicate the Bryan et al. (2014) set-up, on $N = 256$
  uniform cells, compared with Enzo at redshift 0. Density and temperature
  differ by less than 10 % only at the sharp features of the shocks; the
  velocity differs by about 20 % at the shock fronts and where it is close
  to zero, by less than 10 % elsewhere inside the shocked region, and all
  fields differ by less than 1 % outside it. The resolution and solver
  settings of the Enzo comparison run are not stated.
* **Dual-energy variant** (same source, §3.1). With the truncation-error
  criterion of Teyssier (2015) instead of Cholla's Enzo-like switch, the
  code selects the advected internal energy throughout, "the central
  shock at z = 1 is suppressed", and the central profiles differ
  significantly from Enzo's.

**Variants.** Enzo ran it on a 2-level AMR hierarchy (effective 1024
cells), Cholla on a uniform grid of 256 cells; the physical parameters
are the same as far as both papers print them.

**What it shows.** The test discriminates between dual-energy switches:
a switch that keeps the advected internal energy in shocked gas removes
the pancake's shock heating
([Villasenor et al. (2021)](/sources/villasenor-2021.md), §3.1).

## Later uses (batch 10)

* **RAMSES** ([Teyssier (2002)](/sources/teyssier-2002.md), §3.7, eqs. 28–30): Einstein–de Sitter, baryon fraction 0.1, collapse at $1+z = 10$, start at $1+z = 100$, 32 coarse cells, 6 levels (formal 2048). These parameters differ from the Bryan/Villasenor set-up. Refining on density only (shocks unrefined) gives profiles "almost indistinguishable in the center" from refining shocks too, with no oscillation; qualitative.

# Citations

1. [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.9, eqs. 105–107, Fig. 13 (arXiv v1).
2. [Villasenor et al. (2021)](/sources/villasenor-2021.md), §3.1, eqs. 36–39, Fig. 1 (arXiv v2).
3. [Teyssier (2002)](/sources/teyssier-2002.md), §3.7.
