---
type: Software
title: "Grackle (chemistry and cooling library)"
description: "Open-source C/Fortran library, extracted from Enzo, that advances non-equilibrium primordial chemistry (6, 9 or 12 species) and radiative cooling and heating point by point inside a host code's time step, with a sequential first-order backward-difference update sub-cycled under a 10% change limit, Cloudy metal-cooling tables, dust, UV backgrounds and self-shielding, used by 14 host codes."
status: established
aliases: [Grackle, Pygrackle, libgrackle]
tags: [software, cooling, chemistry, time-integration, cosmology, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Grackle

Grackle is an open-source library that integrates non-equilibrium
primordial (H, D, He) chemistry and radiative cooling and heating for a
host hydrodynamics code. It was extracted in 2012 from
[Enzo](/software/enzo.md)'s cooling and chemistry solver, itself from
Anninos et al. (1997)
([Smith et al. (2017)](/sources/smith-2017.md), §2). Its primordial
chemistry is "closely based on" Enzo's, but it includes processes absent
from Enzo 2.5, e.g. tunnelling in H$_2$ collisional dissociation (§3,
§3.1).

## Code

* Repository `bitbucket.org/grackle/grackle` (Table 1). Versions 1.0
  (2014-01-10) to 3.0 (2016-11-01) (Table 2); the paper describes the 3.0
  API (§6.1).
* Compute-heavy kernels in Fortran; C, C++ and Fortran bindings; Python
  through Cython as **Pygrackle**, which also runs one-zone models
  (§6.1–§6.2, §7.2.1).
* **API** (§6.1): five functions, `solve_chemistry`,
  `calculate_cooling_time`, `calculate_temperature`, `calculate_pressure`
  and `calculate_gamma` (the ratio of specific heats is altered from the
  monatomic value only by H$_2$). Parameters live in a `chemistry_data`
  struct, units in a units struct, and fields in `grackle_field_data`
  (1D/2D/3D arrays with ghost-zone start and end indices); 3.0 moved to this
  struct to keep future signatures stable.

## Coupling to the host

`solve_chemistry` receives a time step, usually the host's hydrodynamic
step, and the fields (density, internal energy, optional species and
heating arrays), and updates species densities and internal energy in
place (§3.2, §6.1). It is thus an operator-split, point-local source step:
"each discretization point (particle or cell) can be evolved independently
of the others" (§7.2.1). The paper does not say at which stage of a host
step it is called, and states no conservation property of the update
(mass, charge or element totals are not discussed). See
[Integrating cooling and chemistry source terms](/methods/radiative-cooling-integration.md).

## Chemistry and energy integration

From [Smith et al. (2017)](/sources/smith-2017.md), §3.2 and §4:
* **Networks** (§3.1–§3.2): 6 species (H, H$^+$, e$^-$, He, He$^+$,
  He$^{++}$), 9 (adds H$_2$, H$^-$, H$_2^+$) or 12 (adds D, D$^+$, HD),
  updated in that fixed empirical order (Anninos et al. 1997). H$_2^+$ is
  set to its equilibrium value (eq. 8). A tabulated
  ionization-equilibrium mode is the alternative.
* **Update** (eqs. 5–7): each species obeys
  $\partial_t n_i = C_i - D_i n_i$, advanced by
  $$n_i^{\mathrm{new}} = \frac{C_i\,\Delta t_{\mathrm{sub}} + n_i^{\mathrm{old}}}{1 + D_i\,\Delta t_{\mathrm{sub}}}$$
  with $C_i$ and $D_i$ evaluated with the densities already updated in the
  same step. A full BDF scheme is **not** implemented, "due to the
  difficulty of evaluating the $C_i$ and $D_i$ at the advanced time"; the
  sequential partial updates with sub-cycling "mimic" one.
* **Sub-cycling** (eqs. 9, 11): sub-steps of
  $0.1\min(n_{\mathrm H}/\dot n_{\mathrm H},\ n_{\mathrm e}/\dot n_{\mathrm e})$
  (absolute values not printed) and of $0.1\,e/\dot e$ for the energy
  equation $de/dt = -\dot e_{\mathrm{cool}} + \dot e_{\mathrm{heat}}$;
  with both active the minimum is used. After more than 50 sub-steps the
  analytic time derivatives are replaced by the change over the previous
  sub-step, to stop "very small steps and regularly overshooting the
  equilibrium value".
* **Temperature** (§4.1.2, eqs. 12–14): for the tabulated solver,
  $e = k_{\mathrm B}T/[(\gamma-1)\mu m_{\mathrm H}]$ is solved iteratively
  for $T$ from $\mu = 1$ with a damped update of $\mu$ and a metal
  correction ($\mu_Z \equiv 16$), converging "to within 1% in just a few
  iterations" (asserted); the non-equilibrium solver computes $T$ directly
  from pressure and number density (§7.2.2).

## Physics

From [Smith et al. (2017)](/sources/smith-2017.md), §§4–5:
* **Tables** (§4.1.2, §4.2): primordial equilibrium tables in $T$ (no
  radiation) or in redshift, density and $T$ with a UV background, for
  cooling, heating and $\mu$, interpolated linearly in log space. Metal
  cooling tables from Cloudy, computed at Solar metallicity and scaled by
  the local metallicity (elements to Zn), keeping the metal contribution
  of runs with all elements minus H/He-only runs. HDF5 storage.
* **CMB floor** (eq. 15): $\Lambda(T) - \Lambda(T_{\mathrm{CMB}})$,
  also for metals, so gas below $T_{\mathrm{CMB}}$ is heated.
* **Dust** (§4.3, eqs. 16–18): grain temperature from an instantaneous
  energy balance solved by Newton's method (no tolerance printed),
  Hollenbach & McKee (1989) gas–grain transfer, piecewise grain opacity,
  CMB-only grain heating, constant dust-to-metal ratio.
* **H$_2$ chemical heating** (§4.1.1) after Omukai (2000).
* **UV backgrounds** (§4.2.1, §5): Faucher-Giguère et al. (2009), Haardt
  & Madau (2012) or none; optional Rahmati et al. (2013) self-shielding
  fit in three variants, off by default; no shielding correction for the
  metal tables, which "can cause large errors" (§5.1). Radiative-transfer
  rates can be passed in by the host (§5.2).

## Validity limits

[Smith et al. (2017)](/sources/smith-2017.md), §8.1, Fig. 7–8:
temperatures from about 1 K to $10^9$ K. The high-density metal table spans
$10^{-6}$ to $10^{12}$ cm$^{-3}$, with extrapolation down to $10^{-10}$
"still valid"; the tables miss the transition of cooling from $\propto\rho^2$
to $\propto\rho$, so extrapolation above them "may result in vast
over-prediction". Everything assumes optically thin gas. The cooling
length $c_s t_{\mathrm{cool}}$ must be resolved, or radiative losses are
over-predicted in a run-away cycle.

## Parallelization and performance

From [Smith et al. (2017)](/sources/smith-2017.md), §7.2:
* No communication; "completely thread-safe after the initialisation
  step". Arrays are assumed Fortran-ordered; OpenMP threads the outer two
  loops with one innermost slice per thread (§7.2.1).
* **Serial** (§7.2.2, Fig. 5): $64^3$ cells spanning
  $\log(n_{\mathrm H}/\mathrm{cm^{-3}})\in[-1,3]$, $\log(T/\mathrm K)\in[1,8]$,
  $\log(Z/Z_\odot)\in[-4,0]$, 500 yr, one 2.4 GHz Xeon E5645 core:
  $8.6\times10^5$, $5.7\times10^5$ and $3.2\times10^5$ cell updates per
  second for the equilibrium, 6- and 9-species solvers; 1.01 and 2.67
  sub-cycles per solve (equilibrium, non-equilibrium). Cost is set by the
  number of sub-cycles, not of cells. Recorded as printed: the 9-species
  solver is said to take 164% more time than the equilibrium one, while
  the printed rates give about 169%.
* **OpenMP** (§7.2.3, Fig. 6): 20 threads on two Xeon E5-2670 v2,
  parallel efficiency about 60–90% at $16^3$ cells and 80–90% at $64^3$
  for the expensive routines.

## Verification

From [Smith et al. (2017)](/sources/smith-2017.md), §7.1, all through
Pygrackle under pytest:
* **Unit systems**: the same physical state in different internal units
  must give cooling times agreeing to 4 decimal places; density units may
  differ by "roughly 31 orders of magnitude" before that fails (§7.1.1).
* **Collisional ionization equilibrium** against analytic H/He ionization
  states for $T = 10^4$–$10^9$ K (§7.1.2; tolerance not printed).
* **Answer tests** (cooling rate versus $T$, constant-density cooling,
  one-zone free-fall collapse at $Z = 0$ and $10^{-3}Z_\odot$) compare with
  stored outputs that were validated by manual inspection, so they guard
  against regressions, not errors (§7.1.3–§7.1.5).
* No time-step convergence study, no comparison against a stiff reference
  integrator and no code-to-code comparison are presented.

## Host codes

Fourteen are listed (§8.2): AREPO, ART-I, ART-II, CHANGA, Cosmos++,
[Enzo](/software/enzo.md), Gadget-3, [GAMER](/software/gamer.md),
GASOLINE, Gear, Gizmo, RAMSES (the host of
[RAMSES-RT](/software/ramses-rt.md), whose own thermochemistry is a
different implementation), SPHS and SWIFT.

# Citations

1. [Smith et al. (2017)](/sources/smith-2017.md), §§2–8, Tables 1–2,
   Figs. 5–8 (arXiv v2).
