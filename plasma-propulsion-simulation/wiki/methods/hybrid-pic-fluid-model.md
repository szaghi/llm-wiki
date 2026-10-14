---
type: Method
title: "Hybrid PIC–fluid models"
description: "Thruster models that move ions and neutrals as macroparticles (PIC, with MCC or DSMC collisions) and treat electrons as a fluid, usually quasi-neutral, from Boltzmann or polytropic relations to drift-diffusion with a generalized Ohm's law; the standard compromise for Hall-thruster, ion-thruster, helicon and plume simulation."
status: established
aliases: [hybrid PIC, hybrid particle-fluid model, hybrid fluid-kinetic model, PIC-ion/fluid-electron model, hybrid PIC-DSMC, EP2PLUS]
tags: [hybrid, pic, fluid, dsmc, hall-thruster, ion-thruster, plume, numerics, review]
timestamp: 2026-10-14T00:00:00Z
---

# Hybrid PIC–fluid models

A hybrid model moves the heavy species (ions, often neutrals) as macroparticles
and represents the electrons by a fluid or an algebraic relation. It removes
the electron scales that make fully kinetic
[PIC-MCC](/methods/pic-mcc.md) expensive. In 2005 it was the standard
approach for plasma thrusters ([Boyd (2005)](/sources/boyd-2005.md), §2.2.2);
in 2023 it is used for gridded-ion, Hall, helicon and plume problems
([Taccogna et al. (2023)](/sources/taccogna-2023.md), §§III A, IV A).

## Justification

* **Time scales.** Electrons are much faster than ions; their distribution,
  though not Maxwellian, is compact enough for a fluid temperature and
  pressure ([Boyd (2005)](/sources/boyd-2005.md), §2.2.2). In a fully
  kinetic code the steps are ordered
  $\Delta t_n\sim10^2\Delta t_i\sim10^4\Delta t_e$; a fluid electron allows an
  electron step of the order of the ion step and larger cells, which cuts cost
  by about two orders of magnitude, "say from 3 months to 1 day"
  ([Ahedo (2023)](/sources/ahedo-2023.md), Introduction).
* **Quasi-neutrality.** For $T_e$ of several eV, quasi-neutrality holds down to
  plasma densities of about $10^{14}$ m$^{-3}$, far below thruster values,
  except in the inter-grid regions of ion thrusters
  ([Boyd (2005)](/sources/boyd-2005.md), §2.2.2; stated without
  derivation). Hall-thruster values $n_e\sim10^{18}$ m$^{-3}$ and
  $T_e\sim50$ eV give $\lambda_D\approx50$ µm against a device of about 2 cm;
  resolving $\lambda_D$ would need more than 400 cells per direction
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.2).
* **What is lost.** Hybrid plume models avoid the electron CFL, $\omega_{pe}$,
  $\omega_{ce}$ and Debye constraints but miss kinetic electron cooling
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A).

## Cycle

The standard electric-propulsion hybrid ([Boyd (2005)](/sources/boyd-2005.md),
§2.2.2): ion densities from the particles give $n_e=n_i$; the potential comes
from the electron momentum equation and $\mathbf E=-\nabla\phi$; ions are
accelerated by $m_i\,\mathrm d\mathbf v/\mathrm dt=q_i\mathbf E$ (eq. 2.4) and
moved; heavy-species collisions follow by
[DSMC](/methods/dsmc.md) or Monte Carlo collisions. In hybrid Hall codes about
100 particles per cell suffice for heavy-species properties
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.1).

## Electron closures in use

| Electron model | Use | Source |
|---|---|---|
| [Boltzmann relation](/methods/boltzmann-electron-model.md), isothermal, quasi-neutral | ion-thruster plume impingement (EX-PWS) | [Cai et al. (2018)](/sources/cai-2018.md), eqs. 7–9 |
| Boltzmann relation with nonlinear Poisson, quasi-1D | helicon double-layer channel | [Gallo et al. (2021)](/sources/gallo-2021.md), eqs. 13–18 |
| Boltzmann with fixed $T_e$, sometimes two populations | gridded-ion extraction | [Taccogna et al. (2023)](/sources/taccogna-2023.md), §III A c |
| [Polytropic](/definitions/polytropic-electron-closure.md) or convective heat-flux closure, quasi-neutral or nonlinear Poisson | plumes | [Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A, eq. 16 |
| 4-moment polytropic electrons, Poisson in non-neutral subregions | 3D plumes (EP2PLUS, below) | [Ahedo (2023)](/sources/ahedo-2023.md), eqs. 68–72 |
| [Drift-diffusion](/methods/electron-fluid-model.md) with anisotropic mobility and energy equation | Hall thrusters, $r$–$z$ | [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2; [Boyd (2005)](/sources/boyd-2005.md), §3.4 |
| Drift-diffusion on a [magnetic-field-aligned mesh](/methods/magnetic-field-aligned-mesh.md) | Hall and electrodeless thrusters ([HYPHEN](/software/hyphen.md)) | [Ahedo (2023)](/sources/ahedo-2023.md), §3 |
| Fluid electrons, PIC ions | helicon thrusters | [Taccogna et al. (2023)](/sources/taccogna-2023.md), §III B, ref. 173 |
| None: $\phi$ and $T_e$ prescribed | Hall-thruster channel heavy species | [Gallo et al. (2021)](/sources/gallo-2021.md), §2, Fig. 5 |

## Hall-thruster hybrids

* **Lineage (reported).** Boyd (2005, §3.4) lists Komurasaki & Arakawa
  (steady 2D fluid electrons, flux-tube ions), Garrigues et al. (1D PIC ions),
  Fife & Martinez-Sanchez (2D hybrid with electron sub-cycling, "numerically
  expensive"), Koo & Boyd (the same model applied to the P5 thruster, domain
  from a virtual anode line to the cathode line) and the Hagelaar/Boeuf group,
  and calls the last three "the state of the art". Their accuracy "depends
  heavily" on the electron mobility: on the P5 centreline the measured
  potential lies between a Bohm-mobility and a wall-collision-mobility run
  ([Boyd (2005)](/sources/boyd-2005.md), Fig. 16; see
  [anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)).
* **Catalogue (2019).** Taccogna & Garrigues (Tab. I) list 20 fluid and
  hybrid Hall models (1D $z$, 1D $r$, 2D $z$–$r$, one 2D $z$–$\theta$) with
  their SEE treatment, time dependence and potential solver. In a 2D $r$–$z$
  hybrid (Bareilles et al. 2003; 5 mg/s Xe, 300 V) the equipotentials follow
  the field lines in the plume but form a concave lens in the channel, from
  the density term of the
  [thermalized potential](/definitions/thermalized-potential.md) (§2.5,
  Fig. 4). Fitting a hybrid to discharge current and performance
  overestimates the acceleration-region length; adjusting the $\mu_\perp$
  profile to LIF ion velocities shortens it (§2.5, Fig. 5, after Garrigues et
  al. 2009).
* **Heavy-species kinetics.** A direct-kinetic upwind scheme for the heavy
  species shows numerical broadening of the energy distributions against Monte
  Carlo; ions hitting walls are neutralized and re-emitted as neutrals;
  neutrals are injected half-Maxwellian at the anode and reflected diffusely
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.1). In
  [Gallo et al. (2021)](/sources/gallo-2021.md) (§2.2) an ion that hits a
  wall is converted to a neutral.
* **Sheath edge.** A quasi-neutral model does not automatically meet the Bohm
  criterion; PIC ions need a forcing method at the quasi-neutral boundary
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.3;
  [Ahedo (2023)](/sources/ahedo-2023.md), Appendix). See
  [secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md).

## Plume hybrids

* **EX-PWS** ([Cai et al. (2018)](/sources/cai-2018.md), §2): 3D unstructured
  tetrahedral PIC-DSMC with Boltzmann electrons ($T_e=3.5$ eV,
  $n_0=10^{16}$ m$^{-3}$) and no Poisson solve; cells are required to be
  *larger* than $\lambda_D$ (about $10^{-5}$ m) and of the order of the mean
  free path (about 0.1 m), which is consistent only because no Poisson
  equation is solved. About 2 million cells, $\Delta t=10^{-7}$ s, $W=2\times10^8$.
  The axial plume force on a plate at 0.6–1.0 m agrees with a thrust balance
  within a maximum relative error of 16.36 % (§4.1, Fig. 4). See
  [EX-PWS](/software/ex-pws.md).
* **Boundary conditions.** Taccogna et al. (2023, §IV A) report that adding
  non-neutral regions to a hybrid plume model raises the ion backflow current
  by about 20 % (Fig. 9, $\gamma=1.1$, after Cichocki et al.), and that
  full-PIC plumes show density errors of isothermal-Boltzmann hybrids in the
  plume periphery (Figs. 10–11, after Wang & Hu). Ahedo (2023, eq. 63,
  Fig. 6) compares the local zero-current condition of 2D hybrid codes with a
  global current-free condition: the global one is "more robust", while
  plume current loops under the local one depend strongly on plume size.

## EP2PLUS

EP2PLUS is a 3D hybrid code for thruster plumes from the UC3M EP2 group
([Ahedo (2023)](/sources/ahedo-2023.md), §3, eqs. 68–72, ref. 84):

* **Ions:** particles (PIC) (eq. 68).
* **Electrons:** a 4-moment model with a
  [polytropic closure](/definitions/polytropic-electron-closure.md); the
  elliptic equation is written for the polytropic analogue of the
  [thermalized potential](/definitions/thermalized-potential.md).
* **Non-neutral subregions:** Poisson's equation is solved where
  quasi-neutrality fails (eq. 68).
* **Mesh:** 3D Cartesian, because a
  [magnetic-field-aligned mesh](/methods/magnetic-field-aligned-mesh.md) is
  impractical in 3D and inapplicable with an induced, time-dependent field. On
  this mesh the code is reliable only for effective Hall parameters up to
  50–100 (ref. 87).
* **Upgrade:** an 8-moment electron model, eqs. 71–72 (ref. 89), motivated by
  ref. 29, which showed the polytropic law inadequate in the near region of a
  Hall thruster.

Language, parallelization, discretization and run times are not given in the
source. The run shown is the near plume of a gridded ion thruster with
3 × 5-hole grids (Fig. 7, after ref. 86): unmagnetized, no turbulence model,
polytropic electrons. Ion density spans $10^{14}$–$10^{17}$ m$^{-3}$; a
non-neutral region surrounds the grids; the cathode electron current paths
are shown, with complete current cancellation downstream of the cathode
([Ahedo (2023)](/sources/ahedo-2023.md), Fig. 7; values read from the
figure).

## Cost and parallelism

* Gallo et al. (2021, §§2.6, 4.3) run a heavy-species-only 2D code in MATLAB
  with a CUDA kernel: 55.75 min on a GPU against 101.2 min on a multicore CPU,
  without an electron fluid (see
  [GPU acceleration of particle codes](/methods/gpu-acceleration-of-pic.md)).
* Boyd (2005, §3.4) reports that unsteady hybrid fluid–particle models take
  many hours where steady multi-fluid models take minutes.

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §§2.2.2, 3.4, eq. 2.4, Fig. 16.
2. [Cai et al. (2018)](/sources/cai-2018.md), §§2.1–2.3, 4.1, eqs. 7–9, Fig. 4.
3. [Gallo et al. (2021)](/sources/gallo-2021.md), §§1, 2, 2.2, 2.6, 4.3, eqs. 13–18, Fig. 5.
4. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.1–2.3, 2.5, Tab. I, Figs. 4–5.
5. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §§III A, III B, IV A, eq. 16, Figs. 9–11.
6. [Ahedo (2023)](/sources/ahedo-2023.md), Introduction, §3, eqs. 63, 68–72, Figs. 6–7, Appendix.
