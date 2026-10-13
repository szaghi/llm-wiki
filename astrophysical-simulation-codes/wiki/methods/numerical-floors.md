---
type: Method
title: "Density and pressure floors"
description: "Lower bounds imposed on density, pressure, internal energy or temperature (and, in GRMHD, ceilings on magnetization and Lorentz factor) after an update or a failed recovery; the sources show that floors are non-conservative by construction, that their form and injection frame differ widely between codes, that they set the plasma state of magnetically dominated regions without changing the bulk dynamics, and that first-order flux fallbacks reduce how often they act."
status: established
aliases: [floors, density floor, pressure floor, temperature floor, atmosphere floor, ceilings, floor reset]
tags: [mhd, hydro, relativity, conservation, primitive-recovery]
timestamp: 2026-10-12T00:00:00Z
---

# Density and pressure floors

A **floor** is a lower bound imposed on a primitive variable — density,
gas pressure, internal energy or temperature — when an update or a
[primitive-variable recovery](/methods/primitive-variable-recovery.md)
would produce a value below it; GRMHD codes add **ceilings** on the
magnetization or the Lorentz factor $W$. A floor changes the conserved
variables of the cell, so it is not conservative. The sources differ on
the variables floored, the floor values, and how the inserted mass and
energy are placed.

## Non-relativistic codes

* **Castro, density-floor reset** ([Katz et al. (2016)](/sources/katz-2016.md),
  §2.1). A non-conservative reset is chosen over a positivity-preserving
  diffusive flux. A cell below the floor (typically $10^{-5}$ g cm$^{-3}$)
  copies density, momentum, energy and temperature from its densest
  neighbour if that one is above the floor; otherwise it is set to the
  floor density and the temperature floor (typically $10^5$ K) at rest and
  its thermodynamics recomputed — "very rare", a "last resort". Typical
  trigger: the trailing edge of a star moving across the grid. The
  original Castro already applied a density floor after each step
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §5.1).
* **Castro, temperature floor in the EOS** ([Katz et al. (2016)](/sources/katz-2016.md),
  §2.2). When the Newton–Raphson $(\rho, e)\to T$ inversion does not
  converge, $T$ is set to a floor (typically $10^5$ K). The paper keeps
  $e$ (energy-conserving, thermodynamically inconsistent) rather than
  resetting $e$ to match $T$, which is more accurate in strong 1D shocks
  but drifts total energy over long runs. See
  [general equations of state](/methods/general-equation-of-state.md).
* **Athena++ AMR.** New blocks are prolongated in conserved variables with
  a pressure floor, which breaks energy but not mass or momentum
  conservation ([Stone et al. (2020)](/sources/stone-2020.md), §2.1.5).
* **Tabulated EOS.** Floors on $p$, $\rho e$ and $\rho$ are recommended
  so that requests stay on the table
  ([Coleman (2020)](/sources/coleman-2020.md), §3.2).
* **Disk-wind atmosphere** ([Bai (2017)](/sources/bai-2017.md), §2.5).
  Density floor at $10^{-8}$ times the midplane density at the same
  radius, to stop excessive density drop in the initial atmosphere; once
  the wind is launched the atmosphere stays "well above the floor value".

## Relativistic codes

* **Athena++** floors density and gas pressure, never the magnetic field
  ([Stone et al. (2020)](/sources/stone-2020.md), §4). In the EHT
  comparison it also adds mass or internal energy to keep the
  magnetization below 100 and the plasma beta above $10^{-3}$, and limits
  the normal-frame Lorentz factor to 50
  ([Porth et al. (2019)](/sources/porth-2019.md), §4.1.1).
* **Suggested common floor** (Porth et al. 2019, §4, after McKinney &
  Gammie 2004): density $10^{-5}$ and pressure $\tfrac13\times10^{-7}$ at
  $r_{\mathrm g}$, falling as the radius (in $r_{\mathrm g}$) to the powers
  $-3/2$ and $-5/2$. Groups chose their own.
* **Code-specific floors in the EHT comparison** (§4.1):
  * [H-AMR](/software/h-amr.md): density at least the larger of the squared
    fluid-frame field strength over 20 and the suggested density floor;
    internal energy at least the larger of that squared field over 750 and
    $3.33\times10^{-8}$ times the radius to the power $-5/2$ (§4.1.5).
  * iharm3D: density above the squared field over 50, internal energy
    above the squared field over 2500, density above the internal energy
    over 50, Lorentz factor below 50.
  * KORAL: internal energy over $\rho c^2$ between $10^{-8}$ and $10^2$,
    squared field over internal energy at most $10^5$, squared field over
    $\rho c^2$ at most 50, $W \le 20$.
  * BHAC with staggered fields needed floors 10 times higher, because
    interpolating staggered fields to cell centres "introduces an
    additional error"; ten-times-lower floors were no problem for its
    centred-field Flux-CT runs (§4.1.2).
* **Injection frame** (Porth et al. 2019, §4.1.5). Inserting the floor mass
  in the drift frame avoids the velocity runaway of fluid-frame injection
  and the drag of injection in the frame of zero-angular-momentum
  observers.
* **Effect on results** (Porth et al. 2019, §6.3). Floors differ widely
  between codes and set the plasma state of the magnetically dominated
  funnel, whose parameters "should not be taken at face value"; the effect
  on jet opening angle and profile is minor. See
  [EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md).
* **Zero-temperature floor in recovery**
  ([Kastaun et al. (2021)](/sources/kastaun-2021.md), §III A, §V D). When
  the recovered $e$ falls below the zero-temperature value, only the
  conserved energy $\tau$ is changed; $D$ and $S_i$ are untouched, so there
  is no momentum drift, but the positive bias causes **spurious heating**
  until the thermal energy reaches the width of the energy-error
  distribution.
* **Excision** ([Stone et al. (2026)](/sources/stone-2026.md), §3.6).
  [AthenaK](/software/athenak.md) applies floors inside the horizon, within
  half the sum of the outer and inner horizon radii; the BHAC Cartesian
  run of the EHT comparison evolves the horizon interior with the same
  algorithm plus density and pressure cut-offs $10^{-2}$ and $10^{-4}$
  (Porth et al. 2019, §4.1.2).

## Reducing the need for floors

AthenaK's first-order flux correction (Lemaster & Stone 2009), which
recomputes the fluxes of a cell with first-order reconstruction and LLF
when density or pressure would turn negative, "significantly reduces the
need for floors" in GRMHD accretion; with it the relativistic cylindrical
explosions of Komissarov (1999) run "robustly" without the floors,
background changes or artificial viscosity that other codes need
([Stone et al. (2026)](/sources/stone-2026.md), §3, §3.5, Fig. 10; visual
only). The authors attribute the loss of positivity to truncation error,
not round-off (§3). See
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
Castro chose the floor reset over a positivity-preserving diffusive flux
([Katz et al. (2016)](/sources/katz-2016.md), §2.1).

# Citations

1. [Porth et al. (2019)](/sources/porth-2019.md), §4, §4.1.1–§4.1.5, §6.3 (arXiv v2).
2. [Katz et al. (2016)](/sources/katz-2016.md), §2.1–§2.2 (arXiv v2).
3. [Almgren et al. (2010)](/sources/almgren-2010.md), §5.1 (arXiv v1).
4. [Stone et al. (2020)](/sources/stone-2020.md), §2.1.5, §4.
5. [Coleman (2020)](/sources/coleman-2020.md), §3.2 (arXiv v3).
6. [Bai (2017)](/sources/bai-2017.md), §2.5 (arXiv v1).
7. [Kastaun et al. (2021)](/sources/kastaun-2021.md), §III A, §V D (arXiv v2).
8. [Stone et al. (2026)](/sources/stone-2026.md), §3, §3.5–§3.6, Fig. 10 (arXiv v1).
