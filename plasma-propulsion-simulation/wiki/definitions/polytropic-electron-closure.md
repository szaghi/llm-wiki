---
type: Definition
title: "Polytropic electron closure and plume cooling"
description: "Closure of the electron energy equation by a polytropic law, $T_e\\propto n_e^{\\gamma-1}$, equivalent to a purely convective heat flux; used in plume and magnetic-nozzle models, where measured, kinetic and fitted indices range from near-isothermal to adiabatic and depend on the electron population and direction."
status: established
aliases: [polytropic closure, polytropic electrons, polytropic index, electron cooling, convective heat-flux closure, polytropic law]
tags: [fluid, hybrid, plume, magnetic-nozzle, helicon, kinetic, review]
timestamp: 2026-10-14T00:00:00Z
---

# Polytropic electron closure and plume cooling

## Definition

A polytropic closure replaces the electron energy equation by
$$p_e\propto n_e^{\gamma},\qquad\text{equivalently}\qquad T_e\propto n_e^{\gamma-1}$$
([Takahashi (2019)](/sources/takahashi-2019.md), §5.7, eqs. 27–28). The
adiabatic index is the number of degrees of freedom plus two, divided by the
number of degrees of freedom: $5/3$ for three
([Takahashi (2019)](/sources/takahashi-2019.md), §5.7). $\gamma=1$ is
the isothermal [Boltzmann relation](/methods/boltzmann-electron-model.md).

**Asymptotic potential.** In a quasi-neutral expansion the isothermal
potential falls without bound ($\phi\to-\infty$) as the density vanishes,
whereas the polytropic one tends to the finite value
$-\frac{\gamma}{\gamma-1}\frac{T_e}{e}$, with $T_e$ taken at the point where
$\phi=0$ ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A,
eq. 16). In a 2D collisionless magnetic nozzle,
$\phi-\frac{\gamma}{\gamma-1}\frac{T_e}{e}$ is constant along each magnetic
line ([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 54–60; see
[thermalized potential](/definitions/thermalized-potential.md)).

## Equivalence with a convective heat flux

* A purely convective heat flux is equivalent to a polytropic law
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A, ref. 239).
  For isotropic electrons the correspondence is
  $$\mathbf q_e=\left(\frac{\gamma}{\gamma-1}-\frac52\right)n_eT_e\mathbf u_e,$$
  which is the paper's relation between $\gamma$ and the heat-flux coefficient
  rewritten in $\gamma$.
* With only convective energy flux, $\frac{\gamma}{\gamma-1}n_eT_e\mathbf u_e$,
  the sourceless, stationary, collisionless electron equations give a
  polytropic law along electron streamlines
  ([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 65–67).
* In a paraxial magnetic nozzle the far-plume parallel heat flux is found to be
  convective, proportional to the parallel temperature, density and parallel
  velocity. The parallel energy balance then gives a polytropic law for the
  parallel temperature that also depends on $B$: the parallel temperature times
  $(B/n_e)^{\gamma-1}$ is constant, and the coefficient of the convective flux
  is $\frac{\gamma}{\gamma-1}-\frac32$ (the paper's
  $\gamma$–coefficient relation rewritten in $\gamma$)
  ([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 47–53). The $\frac32$ in
  place of $\frac52$ reflects the single (parallel) degree of freedom; the
  two relations are not in conflict.

## Values of the index

| Setting | Index | Source |
|---|---|---|
| Paraxial kinetic magnetic-nozzle model, fit to the parallel temperature | $\gamma-1=0.23$ | [Ahedo (2023)](/sources/ahedo-2023.md), Fig. 5c (shown, ref. 65) |
| Measured in helicon nozzles (Sheehan et al. 2014; Zhang et al. 2016; Little & Choueiri 2016) | about 1–1.2 | [Takahashi (2019)](/sources/takahashi-2019.md), §5.7 (reported) |
| Non-Maxwellian electron energy distributions (Zhang et al. 2016) | about 1.17, strongly dependent on the distribution shape | [Takahashi (2019)](/sources/takahashi-2019.md), §5.7 (reported) |
| Trapped / free electrons (Takahashi et al. 2018; Kim et al. 2018) | about 1 / tending to $5/3$ | [Takahashi (2019)](/sources/takahashi-2019.md), §5.7, Figs. 18–19 (reported) |
| SPT-100 plume, best fit (Giono et al.) | 1.2–1.5 | [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.6 (reported) |
| Hybrid plume runs reproduced in the review (Cichocki et al.; Araki) | 1.1; 1.3 | [Taccogna et al. (2023)](/sources/taccogna-2023.md), Figs. 9, 13 (model inputs) |
| Full-PIC planar plume, parallel / perpendicular cooling | tending to 1 / reaching and passing the planar adiabatic value 2 | [Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A, Figs. 10–11 (reported, refs. 243–246) |

These are different quantities (parallel or perpendicular temperature,
trapped or free population, magnetized or unmagnetized expansion), so their
spread is not a contradiction. Takahashi reports that earlier thruster models
treat $\gamma$ as a control parameter or take it from measurement, attributes
the near-isothermal readings to electron trapping by electric fields, and calls
the effective $\gamma$ in space an open question; the free electrons doing work
on the nozzle as on an adiabatic wall is consistent with the diamagnetic thrust
model ([Takahashi (2019)](/sources/takahashi-2019.md), §5.7; see
[thrust decomposition of a magnetic nozzle](/results/magnetic-nozzle-thrust-decomposition.md)).

## Where the closure fails

* Ahedo (2023, eqs. 68–72) reports that ref. 29 showed the polytropic law
  inadequate in the near region of a Hall thruster; the 4-moment polytropic
  electron model of EP2PLUS ([hybrid PIC–fluid model](/methods/hybrid-pic-fluid-model.md)) is being upgraded to an
  8-moment model.
* Taccogna et al. (2023, §IV A) report that hybrid polytropic plume models fail
  to reproduce $T_e$ in magnetized Hall-thruster plumes (ref. 238) and in
  unmagnetized expansions (refs. 242–246), and that full PIC shows
  anisotropic cooling that a scalar index cannot carry.
* A HYPHEN run of an ECR thruster with a plume domain of
  3–4 channel widths shows "practically no cooling along the magnetic lines"
  ([Ahedo (2023)](/sources/ahedo-2023.md), Fig. 2, p. 21). An anomalous
  parallel collisionality 10–100 times the collisional value in the parallel
  Fourier law recovers the observed parallel cooling in an electrodeless
  thruster (ref. 41); Ahedo attributes it to the emptying of regions of the
  velocity distribution, not to turbulent transport (eq. 64).

# Citations

1. [Ahedo (2023)](/sources/ahedo-2023.md), eqs. 47–60, 64–72, Figs. 2, 5, p. 21.
2. [Takahashi (2019)](/sources/takahashi-2019.md), §5.7, eqs. 27–28, Figs. 18–19.
3. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A, eq. 16, Figs. 9–11, 13.
4. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.6, eq. 36.
