---
type: Method
title: "Gas–surface interaction models"
description: "Boundary models for neutrals and ions striking a wall in particle codes: Maxwell specular–diffuse reflection, the Schamberg model, normal and tangential momentum and energy accommodation coefficients, sticking, sputtering and ion neutralization, with their measured effect on plume force, satellite drag and propellant utilization."
status: established
aliases: [Maxwell reflection model, accommodation coefficients, wall reflection model, diffuse reflection, Schamberg model]
tags: [wall-interaction, dsmc, plume, numerics]
timestamp: 2026-10-14T00:00:00Z
---

# Gas–surface interaction models

A particle code needs a rule for what leaves a wall when a neutral or an
ion arrives. The sources use the Maxwell model (each re-emission is
specular with some probability and diffuse otherwise), the Schamberg model,
and accommodation coefficients that interpolate between specular and full
thermal accommodation.

## Neutral reflection

* **Maxwell and Schamberg.** [Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. III C d, Fig. 8, name the Maxwell (specular/diffuse probability) and
  Schamberg models for thruster neutrals, report that purely diffuse
  reflection overestimates the neutral residence time, and that the choice
  matters when $\eta_m$ is below 70%. Neutral density can be up to 10 times
  the plasma density.
* **Fully diffuse, fully accommodated.** The satellite-aerodynamics DSMC of
  [Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md), §4, §5.1,
  applies the Maxwell model per surface triangle, with a specular fraction
  constant over the surface and independent of incidence angle, and full
  accommodation of the diffuse part to the wall temperature; the baseline
  is fully diffuse.
* **Diffuse re-emission with ray tracing.** The heavy-species PIC of
  [Gallo et al. (2021)](/sources/gallo-2021.md), §2.2–2.3, Eq. 5, detects
  wall crossings at every Runge–Kutta sub-step, rewinds the crossing
  sub-step, finds the boundary hit first from the crossing times, and
  re-emits the particle with a Maxwellian velocity at the wall temperature
  (850 K in the Hall case, §4.1).
* **Partial accommodation.** The standalone neutral simulation that sets the
  plume neutral profile of [Troyetsky et al. (2026)](/sources/troyetsky-2026.md)
  (§Neutral transport) uses partially accommodated reflection at the pole
  pieces, with accommodation 0.8.

## Accommodation coefficients

[Cai et al. (2018)](/sources/cai-2018.md), §2.2, eqs. 10–14, Table 1, use
Maxwell reflection with species-dependent coefficients on an aluminium plate
in an ion-thruster plume:

* $\alpha_n$ is the incident minus reflected normal momentum flux, divided
  by the incident normal momentum flux minus that of molecules re-emitted at
  the wall temperature; $\alpha_\tau$ is the incident minus reflected
  tangential momentum flux over the incident one (eqs. 10–11).
* The normal coefficient varies with incidence angle through the empirical
  formula of Corey et al. (eq. 12): its ratio to the normal-incidence value
  is the cube of the cosine of the incidence angle plus an empirical
  constant times the squared sine, divided by one plus the inverse of the
  normal-incidence value. (The exponent is typeset ambiguously; the reader
  took it as 3, the Corey et al. form.)
* Table 1, normal-incidence normal coefficient, empirical constant,
  $\alpha_\tau$: Xe 0.90, 0.846, 0.80; Xe$^+$ 0.96, 0.846, 0.90; Xe$^{2+}$
  0.97, 0.846, 0.95. Cai et al. report, citing Kim et al., that the normal
  coefficient is well below 1 for ion energies under 100 eV and approaches 1
  above about 400 eV.
* The reflected speed is
  $\sqrt{v_n^2(1-\alpha_n)^2+(v_{t1}^2+v_{t2}^2)(1-\alpha_\tau)^2}$, with
  $v_n$ the incident normal and $v_{t1},v_{t2}$ the incident tangential
  components of $\mathbf v$; its direction is drawn from two random angles
  (eqs. 13–14).
* **Energy accommodation of recombined ions.**
  [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III C, Eq. 15:
  the mean energy of the emitted particle is $(1-\alpha_E)$ times the impact
  energy plus $2\alpha_E$ times the wall temperature (energy units).
  Simulations generally assume $\alpha_E\approx1$; a lower $\alpha_E$
  reduces $\eta_m$.

## Ions at the wall

* An ion striking a wall returns as a neutral in
  [Gallo et al. (2021)](/sources/gallo-2021.md), §2.2, and is neutralized on
  impact in [Cai et al. (2018)](/sources/cai-2018.md), §2.2.
* [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III C, report
  that in unshielded Hall thrusters the integrated ion wall flux reaches up
  to 40% of the total ion production; ion reflection is negligible above an
  ion-to-wall mass ratio of 2; Xe implantation in Al is 0.2–0.5% at normal
  incidence above 300 eV; recombination probabilities are 7% for N and 17%
  for O (their ref. 57).

## Sticking and sputtering

* [Cai et al. (2018)](/sources/cai-2018.md), §2.2, take a sticking
  coefficient of 0 as baseline, justified by the observed sputter erosion
  of the plate. The plate force is the sum of incident, reflected and
  sputtered momentum fluxes (eq. 15), with Yamamura's sputtering model and
  the Table 2 inputs (Xe on Al; sublimation energy 3.39 eV; threshold
  energy 69.20 eV normal, 72.25 eV oblique).

## Sensitivity of results to the wall model

* Setting the sticking coefficient to 1 lowers the computed plate force by
  about 0.1–0.25% at 0.6–1.0 m and shifts the incident momentum ratios of
  Xe$^+$ and Xe by up to about 1.25% (Fig. 5, read from the figure);
  sputtering adds a small increment to the force (Fig. 4)
  ([Cai et al. (2018)](/sources/cai-2018.md), §4.1).
* Raising the specular fraction from 0 to 0.3 changes the satellite drag
  coefficient by 0.000–6.178% (Table 3), while the pitching-stability
  derivative at zero incidence varies by a factor of about 10, non-monotonically
  (Table 4: $-9.51\times10^{-4}$ to $-9.64\times10^{-3}$ deg$^{-1}$). The
  paper concludes the surface model "does not influence strongly the
  coefficients", which the tables support for drag only
  ([Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md), §5.1).
* Reversed propellant injection, which relies on wall reflection of
  neutrals, raises $\eta_m$ by at most 30% in a DSMC study reported by
  [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III C d.

These models are the wall boundary conditions of
[DSMC](/methods/dsmc.md) and of the heavy-species part of
[hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md). Electron
emission from walls is on
[secondary electron emission](/definitions/secondary-electron-emission.md).

# Citations

1. [Cai et al. (2018)](/sources/cai-2018.md), §2.2, eqs. 10–15, Tables 1–2, §4.1, Figs. 4–5.
2. [Mungiguerra et al. (2018)](/sources/mungiguerra-2018.md), §4, §5.1, Tables 3–4.
3. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III C, Eq. 15, Sec. III C d, Fig. 8 (accepted manuscript).
4. [Gallo et al. (2021)](/sources/gallo-2021.md), §2.2, §2.3, Eq. 5, §4.1.
5. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), §Neutral transport.
